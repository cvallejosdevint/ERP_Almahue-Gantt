#!/usr/bin/env python3
"""
Suaviza el tono de tarjetas Reunión 2 (índice + N1–N4) al estilo negocio
de las primeras versiones del tablero ERP / export Almahue Market.

- Reescribe descripciones (Actualización arriba + legacy/registro abajo)
- Edita solo comentarios «Update» recientes demasiado técnicos (PUT texto)
- Nunca borra comentarios
- No toca comentarios originales «Solicitudes Reunión 2» / «Registro original»

Uso:
  python suavizar-tono-trello-reu2.py
  python suavizar-tono-trello-reu2.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
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

# shortLink → contenido nuevo
INDEX_ID = "DAITP1gF"

# Descripciones N1–N4: tono mock temprano (qué hace / para quién / qué se ve)
N_SCREENS: dict[str, dict] = {
    "kD5faLBC": {
        "label": "N1",
        "desc": """**Actualización** · 23/07/2026

Pantalla de ingreso diario de labores de contratista. El digitador registra, día a día, la mano de obra por empresa, fecha, centro de costo o cuartel, labor y tipo de pago (jornada o trato), pudiendo ajustar el precio según la situación del día.

Inspirada en la usabilidad de AgroSmart: entrada rápida y clara, sin obligar el flujo rígido tarifario → contrato → producción.

Adjuntos: capturas del mock ERP demo y referencia de la reunión.

---

**Pantalla nueva · Reunión 2**

Para quién: digitadores de contratistas (uso diario en terreno/oficina).

Qué se puede hacer:
• Registrar varias labores del mismo día
• Elegir labor y ver actividades relacionadas
• Editar el precio al momento del ingreso
• Dejar listo el promedio para asociar después a proforma o factura

---

**Referencia de la reunión**

Capturas del sistema cliente / AgroSmart usadas en la demo (adjuntas).
Sirven de guía visual; el mock ERP no copia pantalla por pantalla el legado.""",
        "update_comments": {
            # id known from fetch — also match by needle
            "Update 23/07/2026": (
                "**Update 23/07/2026** · Pantalla nueva de Reunión 2 lista con capturas "
                "del mock demo y de la referencia de la reunión."
            ),
        },
    },
    "TbhPZfMp": {
        "label": "N2",
        "desc": """**Actualización** · 23/07/2026

Pantalla para asociar en bloque las labores diarias a una proforma o factura. El usuario selecciona varias labores y las vincula hasta calzar el monto del documento.

Pedido en Reunión 2 con referencia AgroSmart: selección múltiple y calce de montos, sin forzar un flujo rígido de un solo paso.

Adjuntos: captura del mock ERP demo y referencia de la reunión.

---

**Pantalla nueva · Reunión 2**

Para quién: quien cierra el periodo de contratistas (digitador avanzado / analista).

Qué se puede hacer:
• Ver labores pendientes de asociar
• Seleccionar varias a la vez
• Asociarlas a proforma o factura
• Controlar que el monto calce antes de confirmar

---

**Referencia de la reunión**

Captura de asociación a facturas del sistema de referencia (adjunto).""",
        "update_comments": {
            "Update 23/07/2026": (
                "**Update 23/07/2026** · Pantalla nueva de Reunión 2 lista con capturas "
                "del mock demo y de la referencia de la reunión."
            ),
        },
    },
    "8wHl30Q3": {
        "label": "N3",
        "desc": """**Actualización** · 23/07/2026

Pantalla para cargar la cartola bancaria (Excel o PDF) como base oficial de la conciliación. Complementa la pantalla de Conciliación bancaria: primero se sube la cartola y luego se concilia.

Pedido en Reunión 2; el cliente enviará ejemplos de archivos reales.

Adjuntos: captura del mock ERP demo y referencia de la reunión.

---

**Pantalla nueva · Reunión 2**

Para quién: tesorería / quien concilia bancos.

Qué se puede hacer:
• Cargar cartola en Excel o PDF
• Filtrar por banco, mes contable, formato y estado
• Ver periodo de la cartola, montos por contabilizar y usuario que cargó
• Usar esa cartola como fuente para la conciliación diaria o semanal

---

**Referencia de la reunión**

Captura de carga de cartola del sistema actual (adjunto).""",
        "update_comments": {
            "Update 23/07/2026": (
                "**Update 23/07/2026** · Pantalla nueva de Reunión 2 lista con capturas "
                "del mock demo y de la referencia de la reunión."
            ),
            "Update mock ERP (fidelidad": (
                "**Update mock ERP · fidelidad vs reunión**\n\n"
                "Se ajustó la pantalla de carga de cartola para acercarla a lo visto en la reunión:\n"
                "• Menú de Conciliaciones: Ingreso cartola · Conciliación · Pagos/calce\n"
                "• Filtros: búsqueda, banco, mes contable, formato Excel/PDF, estado\n"
                "• Columnas: banco, mes contable, periodo, por contabilizar, usuario\n"
                "• Ejemplos de cartolas de junio y julio para probar\n\n"
                "Fuera de alcance por ahora: reportes completos de cheques/resumen banco "
                "y copia visual exacta del sistema antiguo.\n\n"
                "Captura adjunta regenerada."
            ),
        },
    },
    "iMCx4eXp": {
        "label": "N4",
        "desc": """**Actualización** · 23/07/2026

Pantalla de anticipos a productores: registrar el anticipo y calzarlo en forma parcial contra facturas o liquidaciones, sin hacer traspasos manuales confusos.

En el sistema actual esto vive mezclado con pagos a proveedores; aquí queda como pantalla propia para dejar el flujo más claro (también se relaciona con Pagos y tipo de cambio).

Adjuntos: captura del mock ERP demo y referencia de la reunión.

---

**Pantalla nueva · Reunión 2**

Para quién: tesorería / pagos a productores.

Qué se puede hacer:
• Buscar por productor, banco, moneda y tipo de documento
• Ver saldo, monto calzado y pendiente de pagar
• Registrar anticipo con glosa y tipo de cambio
• Calzar parcialmente contra documentos sin ensuciar el traspaso

---

**Referencia de la reunión**

Captura de anticipos del sistema actual (adjunto).""",
        "update_comments": {
            "Update 23/07/2026": (
                "**Update 23/07/2026** · Pantalla nueva de Reunión 2 lista con capturas "
                "del mock demo y de la referencia de la reunión."
            ),
            "Update mock ERP (fidelidad": (
                "**Update mock ERP · fidelidad vs reunión**\n\n"
                "En el sistema actual los anticipos aparecen dentro de Pago a Proveedores. "
                "El mock deja una pantalla dedicada y muestra:\n"
                "• Filtros por productor, banco, moneda, tipo de documento y estado\n"
                "• Columnas de comprobante, productor, banco, forma de pago, vencimiento, "
                "total, saldo y tipo de cambio\n"
                "• Formulario con glosa y tasa de cambio\n\n"
                "Fuera de alcance por ahora: mezclar en la misma grilla facturas y anticipos "
                "con edición línea a línea como en el legado.\n\n"
                "Captura adjunta regenerada."
            ),
        },
    },
}

INDEX_UPDATE = """**Actualización** · 23/07/2026

Quedaron creadas y enlazadas las cuatro pantallas nuevas pedidas en la Reunión 2 (mock demo + captura de referencia):

• [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC)
• [Asociación labores a proforma/factura](https://trello.com/c/TbhPZfMp)
• [Carga cartola bancaria](https://trello.com/c/8wHl30Q3)
• [Anticipos productores](https://trello.com/c/iMCx4eXp)

El registro completo de la reunión se mantiene **abajo** (no se borra).
Los avances posteriores van como comentarios nuevos."""

INDEX_UPDATE_COMMENT = """**Update 23/07/2026 — pantallas nuevas Reunión 2**

Quedaron listas las cuatro pantallas nuevas de la Reunión 2 (mock demo + referencia de la reunión):

• Ingreso diario labores (contratistas): https://trello.com/c/kD5faLBC
• Asociación labores a proforma/factura: https://trello.com/c/TbhPZfMp
• Carga cartola bancaria: https://trello.com/c/8wHl30Q3
• Anticipos productores: https://trello.com/c/iMCx4eXp

Los enlaces están en la descripción. El comentario de registro original se conserva."""


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


def soft_registro_text(registro: str) -> str:
    """Suaviza jerga puntual del registro sin romper códigos de seguimiento (como Reu 1)."""
    replacements = [
        ("Seed Digitador contratistas / Analista / Admin", "Perfiles Digitador contratistas / Analista / Admin"),
        ("Checks lectura/escritura por pantalla (UI permisos)", "Marcas de lectura/escritura por pantalla"),
        ("Sync Banco Central configurable (auto/manual + hora)", "Actualizar Banco Central (automático o manual + hora)"),
        ("Centros de costo: contacto encargado + seed Mario", "Centros de costo: contacto encargado + lista de Mario"),
        ("_(proceso — tarjeta índice)_", "_(proceso — esta tarjeta)_"),
        ("_OPT / fase siguiente_", "_opcional / fase siguiente_"),
        ("_PEND-02 → REQ_", "_pedido cerrado como diseño_"),
        ("PEND-02 → REQ cerrado como diseño N:1 / multi-mes", "Pedido cerrado: varias proformas a una factura / multi-mes"),
        ("→ OUT (DEC-12)", "→ fuera de alcance v1 (niveles de bodega)"),
        ("confirmar niveles OUT (DEC-12); sin pantalla nueva", "niveles de bodega fuera de alcance v1; sin pantalla nueva"),
        ("sin traspaso manual sucio", "sin traspaso manual confuso"),
        ("niveles OUT v1", "niveles de almacenamiento fuera de alcance v1"),
    ]
    out = registro
    for a, b in replacements:
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

    results: list[tuple[str, str]] = []

    # --- N1–N4 ---
    for short, spec in N_SCREENS.items():
        card = api("GET", f"/cards/{short}", {"fields": "name,desc,shortUrl,id"})
        assert card
        new_desc = spec["desc"].strip() + "\n"
        print(f"{spec['label']} {card['name']} -> {card['shortUrl']}")
        if args.dry_run:
            print("  [dry] desc len", len(new_desc))
        else:
            api("PUT", f"/cards/{card['id']}", {"desc": new_desc})
            print("  desc ok")

        comments = list_comments(card["id"])
        for a in comments:
            text = (a.get("data") or {}).get("text") or ""
            for needle, new_text in spec["update_comments"].items():
                if needle in text and text.strip() != new_text.strip():
                    print(f"  comment Update match: {needle!r}")
                    if args.dry_run:
                        print("  [dry] would edit", a["id"][:8])
                    else:
                        update_comment_text(a["id"], new_text)
                        print("  comment ok", a["id"][:8])
                    break

        results.append((spec["label"], card["shortUrl"]))

    # --- Indice ---
    idx = api("GET", f"/cards/{INDEX_ID}", {"fields": "name,desc,shortUrl,id"})
    assert idx
    _old_upd, body = split_actualizacion(idx.get("desc") or "")
    if not body:
        body = (idx.get("desc") or "").strip()
    # Conservar registro; suavizar jerga puntual
    if body.startswith("**Registro original"):
        soft_body = soft_registro_text(body)
    else:
        soft_body = "**Registro original Reunión 2** _(conservado)_\n\n" + soft_registro_text(body)

    new_idx_desc = f"{INDEX_UPDATE.strip()}\n\n---\n\n{soft_body.strip()}\n"
    print(f"INDICE {idx['name']} -> {idx['shortUrl']}")
    if args.dry_run:
        print("  [dry] desc len", len(new_idx_desc))
    else:
        api("PUT", f"/cards/{idx['id']}", {"desc": new_idx_desc})
        print("  desc ok")

    for a in list_comments(idx["id"]):
        text = (a.get("data") or {}).get("text") or ""
        if "Update 23/07/2026 — pantallas nuevas Reunión 2" in text:
            if text.strip() != INDEX_UPDATE_COMMENT.strip():
                print("  comment Update indice")
                if args.dry_run:
                    print("  [dry] would edit", a["id"][:8])
                else:
                    update_comment_text(a["id"], INDEX_UPDATE_COMMENT)
                    print("  comment ok", a["id"][:8])
            break

    # Comentario Registro original: suavizar solo si menciona template/API (tecnico)
    for a in list_comments(idx["id"]):
        text = (a.get("data") or {}).get("text") or ""
        if "Registro original Reunión 2" in text and ("API" in text or "template" in text or "build_desc" in text):
            new_reg = (
                "**Registro original Reunión 2** · 23/07/2026\n\n"
                "Índice de solicitudes, pantallas nuevas, correcciones sobre pantallas "
                "existentes, decisiones, pendientes y compromisos de la Reunión 2.\n\n"
                "El detalle completo (con enlaces) está en la descripción de esta tarjeta, "
                "sección «Registro original Reunión 2»."
            )
            print("  comment Registro original (suavizar)")
            if args.dry_run:
                print("  [dry] would edit", a["id"][:8])
            else:
                update_comment_text(a["id"], new_reg)
                print("  comment ok", a["id"][:8])
            break

    results.append(("Indice", idx["shortUrl"]))

    print("\n=== LISTO ===")
    for label, url in results:
        print(f"{label}: {url}")


if __name__ == "__main__":
    main()
