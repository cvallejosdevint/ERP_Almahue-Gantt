#!/usr/bin/env python3
"""
Sube a Trello el registro Reunión 2 (sin crear pantallas nuevas N1–N4):

1. Crea etiqueta `Solicitudes reunión 2` (si no existe)
2. Crea índice `Reunión 2 - Registro demo (23/07/2026)` en En QA Almahue
3. Descripción estilo Reu 1: links reales a mocks existentes;
   pantallas nuevas → texto «pendiente de actualizar hipervinculo a card»
4. Adjunta las 20 capturas de pantallas-legacy/reunion2/
5. En mocks existentes: etiqueta + comentario Solicitudes Reunión 2
   (Bodegas / Registro compra: solo comentario)

Uso:
  $env:TRELLO_KEY = "..."
  $env:TRELLO_TOKEN = "..."
  python crear-tarjeta-reunion2-trello.py
  python crear-tarjeta-reunion2-trello.py --dry-run
  python crear-tarjeta-reunion2-trello.py --skip-attachments
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

KEY = os.environ.get("TRELLO_KEY", "") or os.environ.get("TRELLO_API_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    # Opcional: archivo local no versionado
    env_file = Path(__file__).resolve().parent / ".env.trello"
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
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN (env o .env.trello)")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"
ID_BOARD_LONG = "6a54f9864b98b4fe9372bb74"
ID_QA_ALMAHUE = "6a54f9be2f15b6cbeb89dfdd"
CARD_NAME = "Reunión 2 - Registro demo (23/07/2026)"
LABEL_SOL2 = "Solicitudes reunión 2"
LEGACY2 = Path(__file__).resolve().parent / "pantallas-legacy" / "reunion2"
PENDING = "_pendiente de actualizar hipervinculo a card_"

# Mocks existentes a etiquetar + comentar (B1–B11)
COMMENTS_WITH_LABEL: dict[str, str] = {
    "Mock — Tarifas de contratista": """**Solicitudes Reunión 2**

• [R2-C02] Precio editable en control/ingreso diario (no atar siempre al tarifario rígido).
• [R2-C03] Actividades filtradas por labor seleccionada (hoy salen todas).
• Bug legacy confirmado: al agregar labor en mismo CC se borran tarifas; refresh manual.
• Ref: captura 01, 02 · DEC-11 (UX AgroSmart).""",
    "Mock — Proformas y facturas (contratistas)": """**Solicitudes Reunión 2**

• [R2-C05] Permitir N proformas → 1 factura (hoy AgroSoft no asocia 2 proformas).
• [R2-C05] Periodo flexible / multi-mes (dejar de forzar 1 proforma = 1 mes calendario).
• [PEND-02 → REQ] Actualiza alcance vs comentario Reunión 1 (1:1).
• Ref: captura 03, 04 · DEC-11.""",
    "Mock — Traspaso contable y cierre de mes (contratistas)": """**Solicitudes Reunión 2**

• [R2-C06] Cierre de mes: asiento facturas por recibir contratistas vs costo MO contratada (suma proformas del periodo).
• Confirmar tasas CLP/USD/CNY/EUR al traspasar.
• Ref: demo Rodrigo + DEC-11 (contabilidad sigue modelo AgroSoft).""",
    "Mock — Libro comercial": """**Solicitudes Reunión 2**

• [R2-V01] Al reversar, reutilizar datos del documento para el nuevo folio (reversado + reversador + nuevo).
• [R2-V02] Confirmación antes de grabar si viene de una reversa.
• [R2-V03] Quitar utilidad de «Guardar» (no sale en reportes ni contabilidad); solo «Grabar y contabilizar».
• [R2-V04] Búsqueda de clientes robusta/rápida.
• Ref: captura 08, 09.""",
    "Mock — Conciliación bancaria": """**Solicitudes Reunión 2**

• [R2-T02] Conciliación diaria/semanal tomando cartola como fuente oficial.
• [R2-T03] Link directo al asiento contable cuando hay diferencia.
• [R2-T04] Reversa selectiva de movimientos (no solo mes completo).
• Mejorar búsqueda/eliminación de cartolas históricas.
• Ref: captura 11, 12, 13 · ver también Mock Carga cartola (nuevo — pendiente crear).""",
    "Mock — Pagos": """**Solicitudes Reunión 2**

• [R2-T06] Diferencia de tipo de cambio en ambos sentidos (pago CLP/factura USD y viceversa).
• Calce pago–factura con validación (no grabar sin seleccionar documentos).
• Anticipos productores → ver Mock — Anticipos productores (tarjeta nueva — pendiente crear).
• Ref: captura 10, 15.""",
    "Mock — Roles y permisos": """**Solicitudes Reunión 2**

• [R2-R01] Perfiles: Digitador contratistas / Analista / Administrador.
• [R2-R02] Permisos por pantalla: marcas de lectura/escritura (claras en la UI).
• [R2-R03] Digitador: solo procesos diarios del módulo + empresas visibles; Analista: diarios + informes, sin parametrización ni cierre.
• Ref: captura 17, 20 · DEC-13.""",
    "Mock — Monedas": """**Solicitudes Reunión 2**

• [R2-K01] Botón/config «traer Banco Central»; automático o manual + hora.
• Diferenciar indicadores del sistema vs datos actuales BC.
• Ref: captura 16 · DEC-06 / DEC-05.""",
    "Mock — Indicadores Banco Central": """**Solicitudes Reunión 2**

• [R2-K01] Vista de indicadores vigentes + acción actualizar / última sync.
• Coordinar con Mock — Monedas (misma solicitud R2-K01).
• Ref: captura 16.""",
    "Mock — Centros de costo": """**Solicitudes Reunión 2**

• [R2-K02] Campo contacto/encargado del CC (opcional).
• [PEND-06] Cargar lista actualizada que enviará Mario.
• Ref: captura 18.""",
    "Mock — Facturación electrónica (GoSocket)": """**Solicitudes Reunión 2**

• [R2-G01 / DEC-14] Go-live DTE cliente ~01/09 independiente del ERP AlmaWeb.
• Integración libro compras ERP↔GoSocket puede diferirse; no bloquea facturación electrónica.
• Sergio coordina reunión soporte vs avance ERP básico.""",
}

# Solo comentario (sin etiqueta obligatoria)
COMMENTS_ONLY: dict[str, str] = {
    "Mock — Bodegas": """**Solicitudes Reunión 2**

• [DEC-12] Niveles de almacenamiento OUT v1 (no parametrizados / no usados).
• No construir pantalla de niveles. PEND-03 cerrado.""",
    "Mock — Registro de compra (factura)": """**Solicitudes Reunión 2**

• [PEND-01] Cliente confirmó alerta OC exento vs factura afecta. Afinar casos mixtos/combustible en mock.
• No cambia anti-cruzado P-08 de Reunión 1.""",
}


def api(method: str, path: str, data: dict | None = None):
    q = {"key": KEY, "token": TOKEN}
    body = None
    headers = {}
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


def upload_file(card_id: str, filepath: Path):
    url = f"{BASE}/cards/{card_id}/attachments?key={KEY}&token={TOKEN}&name={urllib.parse.quote(filepath.name)}"
    # Windows paths: prefer absolute with forward slashes for curl -F
    file_arg = str(filepath.resolve())
    subprocess.run(
        ["curl", "-s", "-S", "-X", "POST", url, "-F", f"file=@{file_arg}"],
        check=True,
        capture_output=True,
    )


def add_comment(card_id: str, text: str):
    """Solo agrega. Nunca DELETE ni PUT de comentarios (no reemplazar originales)."""
    api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def list_comments(card_id: str) -> list[dict]:
    return api("GET", f"/cards/{card_id}/actions", {"filter": "commentCard", "limit": "50"}) or []


def has_comment_with(card_id: str, *needles: str) -> bool:
    for a in list_comments(card_id):
        text = (a.get("data") or {}).get("text") or ""
        if all(n in text for n in needles):
            return True
    return False


def strip_actualizacion(desc: str) -> str:
    s = (desc or "").strip()
    if not s.startswith("**Actualización**"):
        return s
    parts = s.split("\n---\n", 1)
    return parts[1].strip() if len(parts) == 2 else s


def card_map() -> dict[str, dict]:
    cards = api("GET", f"/boards/{BOARD}/cards", {"fields": "name,shortUrl,id,closed,idLabels"})
    return {c["name"]: c for c in cards if not c.get("closed")}


def find_by_substr(m: dict[str, dict], *subs: str) -> dict | None:
    for name, c in m.items():
        if all(s.lower() in name.lower() for s in subs):
            return c
    return None


def label_link(card: dict | None) -> str:
    """Link markdown estilo Reunión 1 (sin title vacío)."""
    if not card:
        return PENDING
    short = card["name"].replace("Mock — ", "")
    return f"[{short}]({card['shortUrl']})"


def refs(*cards: dict | None) -> str:
    parts = [label_link(c) for c in cards]
    # Evitar repetir PENDING varias veces seguidas
    out: list[str] = []
    for p in parts:
        if p == PENDING and out and out[-1] == PENDING:
            continue
        out.append(p)
    return " · ".join(out) if out else PENDING


def item(code: str, tema: str, card_line: str, *notes: str) -> str:
    """Bullet estilo Reunión 1: - **CODE** tema + links indentados + notas en itálica."""
    lines = [f"- **{code}** {tema}", f"  {card_line}"]
    for n in notes:
        if not n:
            continue
        note = n if n.startswith("_") else f"_{n}_"
        lines.append(f"  {note}")
    return "\n".join(lines)


def plain_item(tema: str, card_line: str) -> str:
    return f"- {tema}\n  {card_line}"


def build_desc(m: dict[str, dict]) -> str:
    """Descripción con el mismo formato markdown que la card Reunión 1 en Trello."""
    g = lambda *s: find_by_substr(m, *s)  # noqa: E731

    tarifas = g("Mock — Tarifas")
    proformas = g("Mock — Proformas")
    traspaso = g("Mock — Traspaso")
    libro = g("Mock — Libro comercial")
    conciliacion = g("Mock — Conciliación")
    pagos = g("Mock — Pagos")
    roles = g("Mock — Roles")
    monedas = g("Mock — Monedas")
    indicadores = g("Mock — Indicadores Banco Central")
    cc = g("Mock — Centros de costo")
    plan = g("Mock — Plan de cuentas")
    gosocket = g("Mock — Facturación electrónica")
    bodegas = g("Mock — Bodegas")
    registro = g("Mock — Registro de compra")
    flujo = g("Mock — Flujo de caja")
    clientes = g("Mock — Clientes")
    usuarios = g("Mock — Usuarios")

    # Pantallas nuevas Reu 2 (N1–N4)
    ingreso = g("Mock — Ingreso diario labores")
    asociacion = g("Mock — Asociación labores")
    cartola = g("Mock — Carga cartola")
    anticipos = g("Mock — Anticipos productores")

    parts = [
        "**Reunión 2 - Registro demo**",
        "",
        "**Fecha:** 23/07/2026",
        "**Objetivo:** Cerrar Ventas + Tesorería; rediseñar Contratistas con referencia AgroSmart; alinear roles, Trello y GoSocket.",
        "",
        "---",
        "",
        "**CONTRATISTAS (rediseño UX)**",
        "",
        item("R2-C01", "Ingreso diario labores (estilo AgroSmart)", label_link(ingreso), "Pantalla nueva"),
        item("R2-C02", "Precio editable en control diario (sin tarifario rígido previo)", refs(ingreso, tarifas)),
        item("R2-C03", "Actividad filtrada por labor seleccionada", refs(tarifas, ingreso)),
        item("R2-C04", "Asociación masiva labores → proforma / factura (calce monto)", label_link(asociacion), "Pantalla nueva"),
        item("R2-C05", "N proformas → 1 factura + periodo multi-mes", label_link(proformas), "PEND-02 → REQ"),
        item("R2-C06", "Cierre mes: asiento facturas por recibir vs costo MO contratada", label_link(traspaso)),
        "",
        "**VENTAS / LIBRO**",
        "",
        item("R2-V01", "Reutilizar datos al reversar documento (nuevo folio + asientos)", label_link(libro)),
        item("R2-V02", "Confirmación antes de grabar documento proveniente de reversa", label_link(libro)),
        item("R2-V03", "Eliminar utilidad de «Guardar»; solo «Grabar y contabilizar»", label_link(libro)),
        item("R2-V04", "Búsqueda de clientes robusta", refs(libro, clientes)),
        "",
        "**TESORERÍA**",
        "",
        item("R2-T01", "Carga cartola Excel + PDF", label_link(cartola), "Pantalla nueva (o ampliar Conciliación)"),
        item("R2-T02", "Conciliación diaria/semanal desde cartola (fuente oficial)", label_link(conciliacion)),
        item("R2-T03", "Link directo al asiento cuando hay diferencia", label_link(conciliacion)),
        item("R2-T04", "Reversa selectiva de movimientos (no solo mes completo)", label_link(conciliacion)),
        item(
            "R2-T05",
            "Anticipos productores — calce parcial sin traspaso manual confuso",
            refs(pagos, anticipos),
            "Pantalla/flujo nuevo o ampliación Pagos",
        ),
        item("R2-T06", "Diferencia TC bidireccional (CLP↔USD)", label_link(pagos)),
        item("R2-T07", "Control por cobrar/pagar y atraso >90 días (roadmap)", refs(pagos, flujo), "opcional / fase siguiente"),
        "",
        "**ROLES Y PERMISOS**",
        "",
        item("R2-R01", "Perfiles Digitador contratistas / Analista / Admin", label_link(roles)),
        item("R2-R02", "Marcas de lectura/escritura por pantalla", label_link(roles)),
        item(
            "R2-R03",
            "Digitador: solo procesos diarios del módulo asignado + empresas visibles",
            refs(roles, usuarios),
        ),
        "",
        "**CATÁLOGOS E INDICADORES**",
        "",
        item("R2-K01", "Actualizar Banco Central (automático o manual + hora)", refs(monedas, indicadores)),
        item("R2-K02", "Centros de costo: contacto encargado + lista de Mario", label_link(cc), "PEND-06"),
        item("R2-K03", "Elementos de costo — lista actualizada Mario", label_link(plan), "PEND-06"),
        "",
        "**INTEGRACIONES / PROCESO**",
        "",
        item("R2-G01", "GoSocket ~01/09 independiente del ERP; libro compras diferible", label_link(gosocket)),
        item("R2-G02", "Feedback asíncrono Trello + reunión semanal martes", "_(proceso — esta tarjeta)_"),
        "",
        "---",
        "",
        "**PANTALLAS NUEVAS (Reunión 2 · MockUp + Solicitudes reunión 2 + Fuera Gantt F1 · Reunión 2)**",
        "",
        f"1. Ingreso diario labores (contratistas) — {label_link(ingreso)}",
        f"2. Asociación labores a proforma/factura — {label_link(asociacion)}",
        f"3. Carga cartola bancaria (PDF/Excel) — {label_link(cartola)}",
        f"4. Anticipos productores (calce parcial) — {label_link(anticipos)}",
        "",
        "---",
        "",
        "**CORRECCIONES SOBRE PANTALLAS EXISTENTES** _(etiqueta Solicitudes reunión 2 — comentario nuevo; no reemplaza Reu 1)_",
        "",
        plain_item("Tarifas de contratista — R2-C02, R2-C03", label_link(tarifas)),
        plain_item("Proformas y facturas (contratistas) — R2-C05", label_link(proformas)),
        plain_item("Traspaso contable y cierre de mes — R2-C06", label_link(traspaso)),
        plain_item("Libro comercial — R2-V01…V04", label_link(libro)),
        plain_item("Conciliación bancaria — R2-T02…T04", label_link(conciliacion)),
        plain_item("Pagos — R2-T05, R2-T06", label_link(pagos)),
        plain_item("Roles y permisos — R2-R01…R03", label_link(roles)),
        plain_item("Monedas / Indicadores Banco Central — R2-K01", refs(monedas, indicadores)),
        plain_item("Centros de costo — R2-K02", label_link(cc)),
        plain_item("Facturación electrónica (GoSocket) — R2-G01", label_link(gosocket)),
        plain_item("Bodegas — niveles de bodega fuera de alcance v1; sin pantalla nueva", label_link(bodegas)),
        "",
        "---",
        "",
        "**DECISIONES FIRMES (DEC-11 a DEC-15)**",
        "",
        item(
            "DEC-11",
            "Contratistas tipo AgroSmart (ingreso diario + asociación masiva)",
            refs(ingreso, asociacion, proformas),
        ),
        item("DEC-12", "Niveles de almacenamiento fuera de alcance v1", label_link(bodegas)),
        item("DEC-13", "Roles Digitador contratistas / Analista / Admin", label_link(roles)),
        item("DEC-14", "GoSocket 01/09 independiente del ERP", label_link(gosocket)),
        item("DEC-15", "Feedback Trello + reunión semanal martes", "_(proceso)_"),
        "",
        "**PENDIENTES CLIENTE**",
        "",
        f"- **PEND-01** Afecto/Exento — regla borde (alerta vista; afinar mixtos/combustible): {label_link(registro)}",
        f"- **PEND-02** Pedido cerrado: varias proformas a una factura / multi-mes: {label_link(proformas)}",
        "- **PEND-03** → fuera de alcance v1 (niveles de bodega)",
        "- **PEND-04** AlmaWeb / dashboards (Mario, agosto)",
        "- **PEND-05** Cartola Excel+PDF (Agustín)",
        "- **PEND-06** Lista CC + elementos de costo (Mario)",
        "",
        "**COMPROMISOS / ACCIONES**",
        "",
        "1. Agustín: Excel + PDF cartola",
        "2. Mario: CC + elementos de costo",
        "3. Carlos: link Trello + capturas actualizadas (lunes)",
        "4. Sergio: coordinar GoSocket vs ERP básico",
        "5. Equipo: roles Digitador / Analista / Admin",
        "6. Martes: reunión planificación semanal",
        "",
        "**FUERA DE ALCANCE REUNIÓN 2** _(no abrir ahora)_",
        "",
        "- Dashboard ejecutivo / Power BI (Mario agosto)",
        "- Maquinaria",
        "- Niveles de almacenamiento",
        "- Integración ERP↔GoSocket libro compras online en septiembre (diferible)",
    ]
    return "\n".join(parts)


def ensure_label_sol2(labels: list[dict]) -> str:
    for lab in labels:
        if lab.get("name") == LABEL_SOL2:
            return lab["id"]
    created = api(
        "POST",
        "/labels",
        {"idBoard": ID_BOARD_LONG, "name": LABEL_SOL2, "color": "purple"},
    )
    print("Etiqueta creada:", LABEL_SOL2, created["id"])
    return created["id"]


def already_has_reu2_comment(card_id: str) -> bool:
    return has_comment_with(card_id, "Solicitudes Reunión 2")


def merge_index_desc(existing_desc: str, registro: str) -> str:
    """
    Convención: Actualización (si hay) ARRIBA; registro original ABAJO.
    Si ya había Actualización, se conserva ese bloque y se refresca el registro.
    Si no, se escribe solo el registro (alta inicial).
    """
    s = (existing_desc or "").strip()
    if s.startswith("**Actualización**"):
        parts = s.split("\n---\n", 1)
        update_block = parts[0].strip()
        body = registro
        if not body.startswith("**Registro original"):
            body = f"**Registro original Reunión 2** _(conservado)_\n\n{body}"
        return f"{update_block}\n\n---\n\n{body}"
    return registro


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-attachments", action="store_true")
    parser.add_argument("--skip-comments", action="store_true", help="Solo índice")
    args = parser.parse_args()

    m = card_map()
    desc = build_desc(m)
    labels = api("GET", f"/boards/{BOARD}/labels")
    lab_sol2 = ensure_label_sol2(labels) if not args.dry_run else "dry"

    existing = None
    for c in m.values():
        if "Registro demo" in c["name"] and "Reunión 2" in c["name"]:
            existing = c
            break

    if args.dry_run:
        print("=== DRY RUN descripción (primeras 40 líneas) ===")
        print("\n".join(desc.splitlines()[:40]))
        print("...")
        print("PENDING count:", desc.count(PENDING))
        print("Comments+label:", len(COMMENTS_WITH_LABEL))
        print("Comments only:", len(COMMENTS_ONLY))
        missing = [n for n in list(COMMENTS_WITH_LABEL) + list(COMMENTS_ONLY) if n not in m]
        if missing:
            print("MISSING CARDS:", missing)
        else:
            print("All target cards found.")
        return

    if existing:
        print("Índice ya existe:", existing["shortUrl"])
        prev = api("GET", f"/cards/{existing['id']}", {"fields": "desc"}) or {}
        merged = merge_index_desc(prev.get("desc") or "", desc)
        api(
            "PUT",
            f"/cards/{existing['id']}",
            {"name": CARD_NAME, "desc": merged, "idList": ID_QA_ALMAHUE},
        )
        # Asegurar etiqueta
        api("POST", f"/cards/{existing['id']}/idLabels", {"value": lab_sol2})
        card_id = existing["id"]
        short_url = existing["shortUrl"]
        # Comentario ancla de registro: solo si falta (nunca borrar Update ni otros)
        if not has_comment_with(card_id, "Registro original Reunión 2"):
            add_comment(
                card_id,
                "**Registro original Reunión 2**\n\n"
                "Índice de solicitudes y decisiones de la Reunión 2. "
                "Detalle completo en la descripción (sección registro / inferior).",
            )
            print("comentario Registro original añadido")
    else:
        card = api(
            "POST",
            "/cards",
            {
                "name": CARD_NAME,
                "desc": desc,
                "idList": ID_QA_ALMAHUE,
                "pos": "top",
                "idLabels": lab_sol2,
            },
        )
        card_id = card["id"]
        short_url = card["shortUrl"]
        print("Índice creado:", short_url)
        add_comment(
            card_id,
            "**Registro original Reunión 2**\n\n"
            "Índice de solicitudes y decisiones de la Reunión 2. "
            "Detalle completo en la descripción.",
        )
        print("comentario Registro original creado")

    if not args.skip_attachments:
        existing_att = {a.get("name") for a in (api("GET", f"/cards/{card_id}/attachments") or [])}
        pngs = sorted(LEGACY2.glob("*.png"))
        for fp in pngs:
            if fp.name in existing_att:
                print("adjunto ya:", fp.name)
                continue
            upload_file(card_id, fp)
            print("adjunto:", fp.name)
            time.sleep(0.25)

    if not args.skip_comments:
        # Refresh map after possible create
        m = card_map()
        for name, text in COMMENTS_WITH_LABEL.items():
            c = m.get(name)
            if not c:
                print("SKIP (no card):", name)
                continue
            # idLabels add
            api("POST", f"/cards/{c['id']}/idLabels", {"value": lab_sol2})
            if already_has_reu2_comment(c["id"]):
                print("comentario ya existe:", name)
            else:
                add_comment(c["id"], text)
                print("comentario+etiqueta:", name)
            time.sleep(0.2)

        for name, text in COMMENTS_ONLY.items():
            c = m.get(name)
            if not c:
                print("SKIP (no card):", name)
                continue
            if already_has_reu2_comment(c["id"]):
                print("comentario ya existe:", name)
            else:
                add_comment(c["id"], text)
                print("comentario:", name)
            time.sleep(0.2)

    print("OK ->", short_url)


if __name__ == "__main__":
    main()
