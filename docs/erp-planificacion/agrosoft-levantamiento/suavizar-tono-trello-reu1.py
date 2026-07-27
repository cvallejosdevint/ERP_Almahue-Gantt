#!/usr/bin/env python3
"""
Suaviza el tono de tarjetas Mock Reunión 1 (+ índice) al estilo negocio
de los mocks tempranos del tablero ERP / export Almahue Market.

- Reescribe descripciones (negocio primero; códigos C/P/I/K en cabecera breve o índice)
- Conserva Actualización arriba + legacy abajo cuando aplica
- Edita solo comentarios «Update» muy técnicos o «Seed» en Solicitudes Reu2 compartidas
- Nunca borra comentarios
- No toca N1–N4 Reunión 2

Uso:
  python suavizar-tono-trello-reu1.py
  python suavizar-tono-trello-reu1.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEY = os.environ.get("TRELLO_KEY", "") or os.environ.get("TRELLO_API_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    env_file = ROOT / ".env.trello"
    if env_file.is_file():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k in ("TRELLO_KEY", "TRELLO_API_KEY") and not KEY:
                KEY = v
            elif k == "TRELLO_TOKEN" and not TOKEN:
                TOKEN = v

if not KEY or not TOKEN:
    raise SystemExit("Faltan TRELLO_KEY / TRELLO_TOKEN (env o .env.trello)")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"
INDEX_ID = "q2197Ajs"

# --- 9 pantallas nuevas (Fuera Gantt F1): reescritura completa tono negocio ---
NUEVAS: dict[str, dict] = {
    "t7UOc695": {
        "label": "Tarifas",
        "desc": """**Actualización** · 24/07/2026

Pantalla de tarifas de contratista: tabla de líneas con labor, actividad, precio, unidad, centro de costo y vigencia. Se pueden agregar, editar o eliminar líneas sin que se borren las demás (problema visto en el sistema actual).

Pedido en Reunión 1; no estaba en la carta Gantt F1 original.

Adjuntos: captura de referencia de la reunión.

---

**Pantalla mock · Reunión 1**

Para quién: quien parametriza contratistas (administrador / analista).

Qué se puede hacer:
• Mantener varias tarifas por contratista y centro de costo
• Definir labor, actividad, unidad y vigencia
• Evitar perder líneas al agregar una nueva

---

**Registro**

C-03 · Relacionado C-04 / DEC-01 · DEC-03
Captura de referencia adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "VkWjIsgY": {
        "label": "Proformas",
        "desc": """**Actualización** · 24/07/2026

Pantalla de proformas y facturas de contratistas. Se lleva el documento desde borrador hasta definitiva y luego a factura, con control de estados claros.

Pedido en Reunión 1; el cliente traerá ejemplos del área agrícola. Quedó pendiente el caso de facturas parciales (varias proformas a una factura), retomado en Reunión 2.

Adjuntos: captura del mock / referencia.

---

**Pantalla mock · Reunión 1**

Para quién: quien cierra el periodo de contratistas.

Qué se puede hacer:
• Crear y seguir proformas (borrador → definitiva → facturada)
• Asociar proforma a factura
• Ver qué queda pendiente antes del cierre de mes

---

**Registro**

C-06 · PEND-02 (ampliado en Reunión 2)
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "4YtaOhkG": {
        "label": "Traspaso",
        "desc": """**Actualización** · 24/07/2026

Pantalla de traspaso contable y cierre de mes de contratistas. El administrador confirma las tasas (peso, dólar, yuan, euro) y cierra el periodo; el digitador no puede cerrar ni traspasar.

Pedido en Reunión 1.

Adjuntos: captura del mock / referencia.

---

**Pantalla mock · Reunión 1**

Para quién: administrador (cierre y traspaso).

Qué se puede hacer:
• Revisar el periodo a cerrar
• Confirmar tasas de cambio al traspasar
• Cerrar el mes dejando el traspaso listo para contabilidad

---

**Registro**

C-07
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "lfDobMAR": {
        "label": "OC",
        "desc": """**Actualización** · 24/07/2026

Pantalla de orden de compra de servicios administrativos. Se emite la OC sin pasar por una solicitud de compra previa, con distribución a centros de costo y control de que los montos cuadren.

Pedido en Reunión 1 (compras = servicios; materiales van por insumos/bodega).

Adjuntos: capturas de OC y distribución por centro de costo.

---

**Pantalla mock · Reunión 1**

Para quién: compras / administración.

Qué se puede hacer:
• Crear OC de servicios sin solicitud previa
• Distribuir montos por centro de costo y validar cuadratura
• Buscar y listar OC por proveedor (más reciente primero)
• Ver tipo de cambio informativo al crear (el efectivo se aplica en recepción)

---

**Registro**

P-01 · P-03 · P-05 · DEC-02 · DEC-07
Capturas adjuntas.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "bo27nMNG": {
        "label": "Recepción",
        "desc": """**Actualización** · 24/07/2026

Pantalla de recepción de orden de compra. Aquí se confirma lo recibido y se aplica el tipo de cambio efectivo (en productores puede usarse un promedio).

Pedido en Reunión 1.

Adjuntos: captura de referencia.

---

**Pantalla mock · Reunión 1**

Para quién: quien recepciona compras / administración.

Qué se puede hacer:
• Recepcionar una OC aprobada
• Ver y aplicar el tipo de cambio en la recepción
• Dejar la compra lista para el registro de factura

---

**Registro**

P-07
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "Q3IBpE4g": {
        "label": "Registro compra",
        "desc": """**Actualización** · 24/07/2026

Pantalla de registro de compra (factura). Evita cruzar proveedor o factura con una OC que no corresponde. Queda pendiente afinar la política de afecto/exento con el cliente.

Pedido en Reunión 1.

Adjuntos: captura de referencia.

---

**Pantalla mock · Reunión 1**

Para quién: compras / administración.

Qué se puede hacer:
• Registrar la factura contra la OC correcta
• Evitar proveedor o documento cruzado
• Ver alertas de afecto/exento cuando aplique

---

**Registro**

P-08 · PEND-01
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "L0UmX7HT": {
        "label": "Bodegas",
        "desc": """**Actualización** · 24/07/2026

Pantalla de bodegas por empresa activa. Cada compañía ve y administra solo sus bodegas, sin mezclar datos entre empresas.

Pedido en Reunión 1. Los niveles de almacenamiento quedaron fuera de alcance de la primera versión.

Adjuntos: captura de referencia.

---

**Pantalla mock · Reunión 1**

Para quién: insumos / bodega / administración.

Qué se puede hacer:
• Ver bodegas de la empresa activa
• Crear o activar/desactivar bodegas
• Usarlas después en movimientos de stock

---

**Registro**

I-01 · DEC-03 · (niveles: fuera de alcance v1)
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "0MWTEhwf": {
        "label": "Movimientos",
        "desc": """**Actualización** · 24/07/2026

Pantalla de movimientos de bodega y notas de crédito por devolución. Permite registrar entradas, traslados y devoluciones; la NC usa el precio de la factura (sin FIFO/LIFO).

Pedido en Reunión 1. También se parametriza cómo se contabilizan esos movimientos.

Adjuntos: captura de referencia.

---

**Pantalla mock · Reunión 1**

Para quién: insumos / bodega / contabilidad de apoyo.

Qué se puede hacer:
• Registrar movimientos de bodega
• Emitir NC de devolución al precio de factura
• Revisar la parametrización contable por tipo de movimiento

---

**Registro**

I-03 · I-04 · I-05
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
    "UapIPyOu": {
        "label": "Indicadores BC",
        "desc": """**Actualización** · 24/07/2026

Pantalla de indicadores del Banco Central (tipo de cambio y valores del día). Sirve de base para operaciones y reportes en peso, dólar, yuan y euro; los domingos y feriados se rellenan con el valor hábil anterior.

Pedido en Reunión 1. Se coordina con el catálogo de monedas.

Adjuntos: captura de referencia.

---

**Pantalla mock · Reunión 1**

Para quién: contabilidad / tesorería / quien consulta el TC del día.

Qué se puede hacer:
• Ver indicadores vigentes
• Actualizar valores desde Banco Central
• Usar CLP, USD, CNY y EUR en el resto del ERP

---

**Registro**

K-05 · DEC-05 · DEC-06
Captura adjunta.""",
        "update_comments": {},
        "add_update": (
            "**Update 24/07/2026** · Descripción en tono negocio "
            "(qué hace la pantalla / para quién / qué se puede hacer)."
        ),
    },
}

# Mocks Gantt F1 ya en tono negocio: solo quitar pie meta + enriquecer Para quién / Qué se puede hacer
GANTT_F1: dict[str, dict[str, str | list[str]]] = {
    "VTvcL8JM": {
        "para": "cualquier usuario del ERP",
        "hacer": [
            "Ingresar con correo y contraseña",
            "Elegir la empresa con la que va a trabajar",
            "Ver siempre la empresa activa en pantalla",
        ],
    },
    "He2yB51U": {
        "para": "operación diaria (no reemplaza Power BI / AlmaWeb)",
        "hacer": [
            "Ver KPIs del mes (ventas, pendientes, caja, presupuesto)",
            "Revisar tendencia y últimos movimientos",
            "Detectar alertas operativas (OC, proformas, TC del día)",
        ],
    },
    "rYa9lRan": {
        "para": "administrador del ERP",
        "hacer": [
            "Ver el listado de empresas",
            "Dar de alta una empresa nueva",
            "Mantener el aislamiento por empresa activa",
        ],
    },
    "CSpgLHIY": {
        "para": "administrador",
        "hacer": [
            "Ver quién tiene acceso",
            "Asignar empresa y perfil",
            "Dar de alta o ajustar usuarios (~15 en total)",
        ],
    },
    "TmBrM6uq": {
        "para": "administrador",
        "hacer": [
            "Definir perfiles (Administrador / Digitador / Intermedio)",
            "Marcar lectura o escritura por pantalla",
            "Auditar cambios de permisos (quién / cuándo)",
        ],
    },
    "X9AcyElf": {
        "para": "administración / contabilidad",
        "hacer": [
            "Mantener monedas de trabajo (CLP, USD, CNY, EUR)",
            "Usarlas en pagos, compras y reportes",
            "Relacionarlas con indicadores del Banco Central",
        ],
    },
    "Ceyi3VQg": {
        "para": "administración / catálogos",
        "hacer": [
            "Mantener unidades agro (kg, litros, cajas, horas, etc.)",
            "Estandarizar cantidades en todo el ERP",
        ],
    },
    "Q2xb0xJU": {
        "para": "administración / quien imputa gastos",
        "hacer": [
            "Ver centros de costo solo de la empresa activa",
            "Crear o dar vigencia a un centro de costo",
            "Asignar contacto o encargado cuando corresponda",
        ],
    },
    "ELDfezvB": {
        "para": "administración",
        "hacer": [
            "Clasificar documentos operativos (OC, factura, NC, proforma, asiento)",
            "Indicar en qué área del ERP se usan",
        ],
    },
    "hKlug52V": {
        "para": "contabilidad",
        "hacer": [
            "Mantener el plan de cuentas",
            "Marcar flags (centro de costo, área, especie, variedad, elemento)",
            "Gestionar elementos de costo e historial de factores",
        ],
    },
    "BA5QdHMc": {
        "para": "contabilidad",
        "hacer": [
            "Ver asientos en borrador o contabilizados",
            "Ingresar un asiento nuevo",
            "Cargar comprobantes masivos con cuadratura debe/haber",
        ],
    },
    "kZwP8QUC": {
        "para": "contabilidad / gerencia",
        "hacer": [
            "Abrir balance, estado de resultados, mayor y flujo",
            "Ver resumen del periodo activo",
        ],
    },
    "atF82W4s": {
        "para": "tesorería (uso secundario en v1)",
        "hacer": [
            "Ver entradas y salidas de caja",
            "Registrar un movimiento por fecha y concepto",
        ],
    },
    "deMXSU4X": {
        "para": "tesorería / pagos",
        "hacer": [
            "Ver pagos pendientes, programados y realizados",
            "Registrar un pago con tipo de cambio manual si aplica",
            "Calzar pago con documentos",
        ],
    },
    "jarqjx0C": {
        "para": "quien administra contratistas",
        "hacer": [
            "Dar de alta contratistas con RUT único y vigencia",
            "Parametrizar labor y actividad (sin módulo Mano de Obra)",
            "Ir a tarifas desde el maestro",
        ],
    },
    "PjY4vlMg": {
        "para": "insumos / compras de materiales",
        "hacer": [
            "Mantener el maestro familia + subfamilia + descripción",
            "Evitar artículos duplicados",
            "Ver stock y costo promedio",
        ],
    },
    "INraR0g3": {
        "para": "aprobadores de OC / jefatura",
        "hacer": [
            "Ver pendientes con badge",
            "Aprobar o rechazar con líneas y centros de costo visibles",
            "Configurar reglas por monto y área",
        ],
    },
}

FOOTER_RE = re.compile(
    r"\n---\n\s*\*\*Fase Gantt:\*\*[^\n]*\n?",
    re.I,
)

INDEX_UPDATE = """**Actualización** · 24/07/2026

Las descripciones de las pantallas Mock de Reunión 1 quedaron en tono negocio (qué hace / para quién / qué se puede hacer), alineadas con el estilo de las primeras versiones del tablero y con Reunión 2.

El registro completo de la reunión (códigos C / P / I / K, DEC, PEND y enlaces) se mantiene **abajo**."""

# Soft replacements only inside index registro body
INDEX_SOFT = [
    ("PEND-03 - sin mock aún", "PEND-03 — pendiente de pantalla (validar con materiales)"),
    ("_PEND-03 - sin mock aún_", "_PEND-03 — pendiente de pantalla_"),
    ("(mocks Gantt sin etiqueta Reunión 1)", "(pantallas Gantt sin etiqueta Reunión 1)"),
    ("sin mock en v1", "sin pantalla en v1"),
]

# Comentarios Reu2 en tarjetas compartidas Reu1: suavizar «Seed» (no son N1–N4)
COMMENT_SOFT: list[tuple[str, list[tuple[str, str]]]] = [
    (
        "TmBrM6uq",  # Roles
        [
            (
                "Seed roles: Digitador contratistas / Analista / Administrador.",
                "Perfiles: Digitador contratistas / Analista / Administrador.",
            ),
            (
                "UI permisos: checks lectura/escritura por pantalla (no solo strings).",
                "Permisos: marcas de lectura/escritura por pantalla.",
            ),
        ],
    ),
    (
        "Q2xb0xJU",  # Centros de costo
        [
            (
                "Seed con lista actualizada que enviará Mario.",
                "Cargar lista actualizada que enviará Mario.",
            ),
        ],
    ),
]


def api(method: str, path: str, data: dict | None = None):
    q = {"key": KEY, "token": TOKEN}
    body = None
    headers: dict[str, str] = {}
    if method == "GET":
        if data:
            q.update(data)
        url = f"{BASE}{path}?{urllib.parse.urlencode(q)}"
    else:
        url = f"{BASE}{path}?{urllib.parse.urlencode(q)}"
        if data is not None:
            body = urllib.parse.urlencode(data).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} → {e.code}: {err}") from e


def list_comments(card_id: str) -> list[dict]:
    return api("GET", f"/cards/{card_id}/actions", {"filter": "commentCard", "limit": "50"}) or []


def update_comment_text(action_id: str, text: str) -> None:
    api("PUT", f"/actions/{action_id}/text", {"value": text})


def add_comment(card_id: str, text: str) -> None:
    api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def extract_images(desc: str) -> str:
    """Conserva bloques de imagen markdown + líneas de pie asociadas."""
    lines = (desc or "").splitlines()
    keep: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("![") and "](" in line:
            block = [line]
            if i + 1 < len(lines):
                nxt = lines[i + 1]
                if (
                    nxt.strip()
                    and not nxt.strip().startswith("![")
                    and not nxt.strip().startswith("**Fase Gantt")
                    and not nxt.strip().startswith("---")
                    and not nxt.strip().startswith("**Actualización")
                ):
                    block.append(nxt)
                    i += 1
            keep.extend(block)
            keep.append("")
        i += 1
    out: list[str] = []
    for line in keep:
        if line == "" and out and out[-1] == "":
            continue
        out.append(line)
    return "\n".join(out).strip()


def attachment_images(card_id: str) -> str:
    """Fallback: arma markdown desde adjuntos si la desc no tenía ![]."""
    atts = api("GET", f"/cards/{card_id}/attachments", {"fields": "name,url,previews"}) or []
    blocks: list[str] = []
    for a in atts:
        name = a.get("name") or "captura"
        previews = a.get("previews") or []
        url = previews[-1].get("url") if previews else a.get("url")
        if not url:
            continue
        # preferir nombre .webp en alt si el preview lo es
        alt = Path(name).stem + (".webp" if "webp" in url else Path(name).suffix)
        blocks.append(f"![{alt}]({url})")
    return "\n\n".join(blocks).strip()


def ensure_images(new_desc: str, old_desc: str, card_id: str) -> str:
    if "![" in new_desc:
        return new_desc
    imgs = extract_images(old_desc) or attachment_images(card_id)
    if not imgs:
        return new_desc
    return new_desc.rstrip() + "\n\n---\n\n**Capturas**\n\n" + imgs + "\n"

def first_paragraphs(desc: str, max_paras: int = 2) -> str:
    """Toma párrafos de negocio al inicio (antes de imágenes / ---)."""
    text = FOOTER_RE.sub("\n", desc or "")
    chunks: list[str] = []
    buf: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("![") or line.strip().startswith("---"):
            break
        if not line.strip():
            if buf:
                chunks.append("\n".join(buf).strip())
                buf = []
                if len(chunks) >= max_paras:
                    break
            continue
        if line.strip().startswith("**Fase Gantt"):
            break
        buf.append(line)
    if buf and len(chunks) < max_paras:
        chunks.append("\n".join(buf).strip())
    return "\n\n".join(chunks).strip()


def build_gantt_desc(old_desc: str, para: str, hacer: list[str]) -> str:
    lead = first_paragraphs(old_desc, 2)
    images = extract_images(old_desc)
    bullets = "\n".join(f"• {h}" for h in hacer)
    parts = [
        "**Actualización** · 24/07/2026",
        "",
        lead,
        "",
        f"Para quién: {para}.",
        "",
        "Qué se puede hacer:",
        bullets,
    ]
    if images:
        parts.extend(["", "---", "", images])
    parts.extend(
        [
            "",
            "---",
            "",
            "**Registro**",
            "",
            "Pantalla del mock demo · Reunión 1",
        ]
    )
    return "\n".join(parts).strip() + "\n"


def soft_index_body(body: str) -> str:
    out = body
    for a, b in INDEX_SOFT:
        out = out.replace(a, b)
    return out


def split_actualizacion(desc: str) -> tuple[str, str]:
    s = (desc or "").strip()
    if not s.startswith("**Actualización**"):
        return "", s
    parts = s.split("\n---\n", 1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return s, ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    results: list[tuple[str, str, str]] = []

    # --- Pantallas nuevas (Fuera Gantt) ---
    for short, spec in NUEVAS.items():
        card = api("GET", f"/cards/{short}", {"fields": "name,desc,shortUrl,id"})
        assert card
        old_desc = card.get("desc") or ""
        new_desc = ensure_images(spec["desc"].strip() + "\n", old_desc, card["id"])

        print(f"NUEVA {spec['label']} {card['name']} -> {card['shortUrl']}")
        if args.dry_run:
            print("  [dry] desc len", len(new_desc))
        else:
            api("PUT", f"/cards/{card['id']}", {"desc": new_desc})
            print("  desc ok")

        comments = list_comments(card["id"])
        has_soft_update = any(
            "Update 24/07/2026" in ((a.get("data") or {}).get("text") or "")
            for a in comments
        )
        if spec.get("add_update") and not has_soft_update:
            print("  add Update suave")
            if args.dry_run:
                print("  [dry] would comment")
            else:
                add_comment(card["id"], spec["add_update"])
                print("  comment ok")

        results.append((spec["label"], card["shortUrl"], "nueva-rewritten"))

    # --- Mocks Gantt F1 ---
    for short, meta in GANTT_F1.items():
        card = api("GET", f"/cards/{short}", {"fields": "name,desc,shortUrl,id"})
        assert card
        old = card.get("desc") or ""
        new_desc = build_gantt_desc(
            old,
            str(meta["para"]),
            list(meta["hacer"]),  # type: ignore[arg-type]
        )
        print(f"F1 {card['name']} -> {card['shortUrl']}")
        if args.dry_run:
            print("  [dry] desc len", len(new_desc))
        else:
            api("PUT", f"/cards/{card['id']}", {"desc": new_desc})
            print("  desc ok")
        results.append((card["name"], card["shortUrl"], "f1-softened"))

    # --- Comentarios Seed en tarjetas compartidas ---
    for short, reps in COMMENT_SOFT:
        card = api("GET", f"/cards/{short}", {"fields": "name,shortUrl,id"})
        assert card
        for a in list_comments(card["id"]):
            text = (a.get("data") or {}).get("text") or ""
            new_text = text
            for old, new in reps:
                new_text = new_text.replace(old, new)
            if new_text != text:
                print(f"COMMENT soft {card['name']} {a['id'][:8]}")
                if args.dry_run:
                    print("  [dry] would edit")
                else:
                    update_comment_text(a["id"], new_text)
                    print("  comment ok")

    # --- Índice ---
    idx = api("GET", f"/cards/{INDEX_ID}", {"fields": "name,desc,shortUrl,id"})
    assert idx
    _old_upd, body = split_actualizacion(idx.get("desc") or "")
    if not body:
        body = (idx.get("desc") or "").strip()
    # Si ya había Actualización, el body es el registro; si no, todo es registro
    soft_body = soft_index_body(body)
    new_idx = f"{INDEX_UPDATE.strip()}\n\n---\n\n{soft_body.strip()}\n"
    print(f"INDICE {idx['name']} -> {idx['shortUrl']}")
    if args.dry_run:
        print("  [dry] desc len", len(new_idx))
    else:
        api("PUT", f"/cards/{idx['id']}", {"desc": new_idx})
        print("  desc ok")

    idx_comments = list_comments(idx["id"])
    has_idx_update = any(
        "Update 24/07/2026" in ((a.get("data") or {}).get("text") or "")
        for a in idx_comments
    )
    idx_update = (
        "**Update 24/07/2026 — tono negocio Reunión 1**\n\n"
        "Se alinearon las descripciones de los Mock de Reunión 1 "
        "(pantallas Gantt F1 + pantallas nuevas) al tono negocio, "
        "igual que Reunión 2. Códigos C/P/I/K, DEC y PEND siguen en este índice. "
        "No se borró historial ni comentarios originales."
    )
    if not has_idx_update:
        print("  add Update indice")
        if args.dry_run:
            print("  [dry] would comment")
        else:
            add_comment(idx["id"], idx_update)
            print("  comment ok")

    results.append(("Indice", idx["shortUrl"], "index"))

    # resumen
    out_path = ROOT / "_tmp_reu1_suavizado_resultado.md"
    lines = ["# Resultado suavizar Reu1\n"]
    for label, url, kind in results:
        lines.append(f"- [{kind}] {label}: {url}")
    out_path.write_text("\n".join(lines), encoding="utf-8")

    print("\n=== LISTO ===")
    for label, url, kind in results:
        print(f"{kind}\t{label}\t{url}")
    print(f"Resumen: {out_path}")


if __name__ == "__main__":
    main()
