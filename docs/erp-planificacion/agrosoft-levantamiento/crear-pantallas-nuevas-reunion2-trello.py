#!/usr/bin/env python3
"""
Crea en Trello las pantallas nuevas N1–N4 de Reunión 2:

  N1 Mock — Ingreso diario labores (contratistas)
  N2 Mock — Asociación labores a proforma/factura
  N3 Mock — Carga cartola bancaria
  N4 Mock — Anticipos productores

Por tarjeta:
  - Lista: En desarrollo (mismo patrón mocks Fuera Gantt)
  - Etiquetas: MockUp + Solicitudes reunión 2 + Fuera Gantt F1 · Reunión 2
  - Descripción: Actualización (demo) arriba + Legacy abajo
  - Adjuntos: captura ERP demo + captura legacy reunión2
  - Comentario Solicitudes Reunión 2

Luego actualiza el índice Reunión 2 (enlaces N1–N4) sin borrar el registro:
  - Descripción índice: bloque **Actualización** ARRIBA + registro original ABAJO
  - Comentarios: nunca DELETE; Update = comentario nuevo adicional
  - Comentario «Solicitudes Reunión 2» / «Registro original» se conserva

Uso:
  $env:TRELLO_KEY = "..."
  $env:TRELLO_TOKEN = "..."
  # o archivo local .env.trello
  python crear-pantallas-nuevas-reunion2-trello.py
  python crear-pantallas-nuevas-reunion2-trello.py --dry-run
  python crear-pantallas-nuevas-reunion2-trello.py --skip-attachments
  python crear-pantallas-nuevas-reunion2-trello.py --skip-index
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

ROOT = Path(__file__).resolve().parent
LEGACY2 = ROOT / "pantallas-legacy" / "reunion2"
DEMO2 = ROOT / "capturas-validacion-erp" / "reu2"

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
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN (env o .env.trello)")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"
ID_BOARD_LONG = "6a54f9864b98b4fe9372bb74"
ID_QA_ALMAHUE = "6a54f9be2f15b6cbeb89dfdd"

LABEL_MOCKUP = "MockUp"
LABEL_SOL2 = "Solicitudes reunión 2"
LABEL_FUERA2 = "Fuera Gantt F1 · Reunión 2"
UPDATE_DATE = "23/07/2026"

# Specs N1–N4 — tono negocio (estilo mocks tempranos / Market observaciones).
# Evitar rutas, seed/fixtures/API y jerga de código en textos visibles de Trello.
NEW_SCREENS: list[dict] = [
    {
        "code": "N1",
        "name": "Mock — Ingreso diario labores (contratistas)",
        "audience": "digitadores de contratistas (uso diario)",
        "blurb": (
            "Pantalla de ingreso diario de labores de contratista. El digitador registra, "
            "día a día, la mano de obra por empresa, fecha, centro de costo o cuartel, labor "
            "y tipo de pago (jornada o trato), pudiendo ajustar el precio según la situación del día.\n\n"
            "Inspirada en la usabilidad de AgroSmart: entrada rápida y clara, sin obligar el "
            "flujo rígido tarifario → contrato → producción."
        ),
        "can_do": [
            "Registrar varias labores del mismo día",
            "Elegir labor y ver actividades relacionadas",
            "Editar el precio al momento del ingreso",
            "Dejar listo el promedio para asociar después a proforma o factura",
        ],
        "demo": [
            DEMO2 / "03-ingreso-diario.png",
            DEMO2 / "03-ingreso-diario-form.png",
        ],
        "legacy": [
            LEGACY2 / "06-agrosmart-ingreso-mano-obra.png",
            LEGACY2 / "07-agrosmart-ui-amigable.png",
        ],
        "comment": """**Solicitudes Reunión 2**

• Ingreso múltiple / diario de mano de obra contratista.
• Precio editable según la situación del día.
• Referencia AgroSmart; el cierre contable sigue el modelo acordado con el cliente.""",
    },
    {
        "code": "N2",
        "name": "Mock — Asociación labores a proforma/factura",
        "audience": "quien cierra el periodo de contratistas",
        "blurb": (
            "Pantalla para asociar en bloque las labores diarias a una proforma o factura. "
            "El usuario selecciona varias labores y las vincula hasta calzar el monto del documento.\n\n"
            "Pedido en Reunión 2 con referencia AgroSmart: selección múltiple y calce de montos."
        ),
        "can_do": [
            "Ver labores pendientes de asociar",
            "Seleccionar varias a la vez",
            "Asociarlas a proforma o factura",
            "Controlar que el monto calce antes de confirmar",
        ],
        "demo": [DEMO2 / "04-asociacion-labores.png"],
        "legacy": [LEGACY2 / "05-agrosmart-asociacion-facturas.png"],
        "comment": """**Solicitudes Reunión 2**

• Asociación masiva de labores a proforma / factura (calce de monto).
• Usabilidad tipo AgroSmart; no forzar un flujo rígido de un solo paso.""",
    },
    {
        "code": "N3",
        "name": "Mock — Carga cartola bancaria",
        "audience": "tesorería / quien concilia bancos",
        "blurb": (
            "Pantalla para cargar la cartola bancaria (Excel o PDF) como base oficial de la "
            "conciliación. Complementa Conciliación bancaria: primero se sube la cartola y luego se concilia.\n\n"
            "Pedido en Reunión 2; el cliente enviará ejemplos de archivos reales."
        ),
        "can_do": [
            "Cargar cartola en Excel o PDF",
            "Filtrar por banco, mes contable, formato y estado",
            "Ver periodo, montos por contabilizar y usuario que cargó",
            "Usar esa cartola como fuente para la conciliación",
        ],
        "demo": [DEMO2 / "08-carga-cartola.png"],
        "legacy": [LEGACY2 / "11-tesoreria-carga-cartola.png"],
        "comment": """**Solicitudes Reunión 2**

• Carga de cartola bancaria en Excel + PDF.
• Agustín enviará ejemplos de archivos reales.""",
    },
    {
        "code": "N4",
        "name": "Mock — Anticipos productores",
        "audience": "tesorería / pagos a productores",
        "blurb": (
            "Pantalla de anticipos a productores: registrar el anticipo y calzarlo en forma "
            "parcial contra facturas o liquidaciones, sin traspasos manuales confusos.\n\n"
            "En el sistema actual vive mezclado con pagos; aquí queda como pantalla propia "
            "(relacionada también con Pagos y tipo de cambio)."
        ),
        "can_do": [
            "Buscar por productor, banco, moneda y tipo de documento",
            "Ver saldo, monto calzado y pendiente de pagar",
            "Registrar anticipo con glosa y tipo de cambio",
            "Calzar parcialmente contra documentos",
        ],
        "demo": [DEMO2 / "10-anticipos.png"],
        "legacy": [LEGACY2 / "14-anticipos-productores.png"],
        "comment": """**Solicitudes Reunión 2**

• Anticipos a productores con calce parcial (sin traspaso manual confuso).
• Relacionado con Pagos (tipo de cambio y calce de documentos).""",
    },
]


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
    url = (
        f"{BASE}/cards/{card_id}/attachments"
        f"?key={KEY}&token={TOKEN}&name={urllib.parse.quote(filepath.name)}"
    )
    file_arg = str(filepath.resolve())
    subprocess.run(
        ["curl", "-s", "-S", "-X", "POST", url, "-F", f"file=@{file_arg}"],
        check=True,
        capture_output=True,
    )


def add_comment(card_id: str, text: str):
    """Solo agrega. Nunca borrar ni reemplazar comentarios existentes."""
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


def compose_update_over_body(update_block: str, body: str) -> str:
    body = (body or "").strip()
    return f"{update_block.strip()}\n\n---\n\n{body}"


def ensure_label(labels: list[dict], name: str, color: str) -> str:
    for lab in labels:
        if lab.get("name") == name:
            return lab["id"]
    created = api(
        "POST",
        "/labels",
        {"idBoard": ID_BOARD_LONG, "name": name, "color": color},
    )
    print("etiqueta creada:", name, created["id"])
    labels.append(created)
    return created["id"]


def find_list_id(lists: list[dict], *names: str) -> str:
    by = {l["name"]: l["id"] for l in lists}
    for n in names:
        if n in by:
            return by[n]
    raise RuntimeError(f"Lista no encontrada. Busqué {names}; hay {list(by)}")


def card_map() -> dict[str, dict]:
    cards = api("GET", f"/boards/{BOARD}/cards", {"fields": "name,shortUrl,id,closed,idLabels"})
    return {c["name"]: c for c in cards if not c.get("closed")}


def build_desc(spec: dict) -> str:
    """Descripción en tono negocio (mocks tempranos): qué hace, para quién, qué se puede hacer."""
    can_do = "\n".join(f"• {x}" for x in spec.get("can_do") or [])
    audience = spec.get("audience") or "usuarios del módulo"
    return "\n".join(
        [
            f"**Actualización** · {UPDATE_DATE}",
            "",
            spec["blurb"].strip(),
            "",
            "Adjuntos: capturas del mock ERP demo y referencia de la reunión.",
            "",
            "---",
            "",
            "**Pantalla nueva · Reunión 2**",
            "",
            f"Para quién: {audience}.",
            "",
            "Qué se puede hacer:",
            can_do,
            "",
            "---",
            "",
            "**Referencia de la reunión**",
            "",
            "Capturas del sistema cliente / AgroSmart usadas en la demo (adjuntas).",
            "Sirven de guía visual; el mock ERP no copia pantalla por pantalla el legado.",
        ]
    )


def already_has_reu2_comment(card_id: str) -> bool:
    return has_comment_with(card_id, "Solicitudes Reunión 2")


def create_or_update_screen(
    spec: dict,
    *,
    id_list: str,
    label_ids: list[str],
    dry_run: bool,
    skip_attachments: bool,
) -> dict:
    m = card_map()
    existing = m.get(spec["name"])
    desc = build_desc(spec)
    id_labels = ",".join(label_ids)

    if dry_run:
        print(f"[dry] {spec['code']} {spec['name']}")
        print("  demo:", [p.name for p in spec["demo"] if p.is_file()])
        print("  legacy:", [p.name for p in spec["legacy"] if p.is_file()])
        return {"name": spec["name"], "shortUrl": "(dry-run)", "id": "dry", "was_update": False}

    was_update = False
    if existing:
        was_update = True
        print("ya existe, actualizo (preservando comentarios):", existing["shortUrl"])
        # Merge: no pisar cuerpo legacy si ya había contenido bajo Actualización
        prev = api("GET", f"/cards/{existing['id']}", {"fields": "desc"}) or {}
        prev_body = strip_actualizacion(prev.get("desc") or "")
        if prev_body and "**Legacy" in prev_body and "**Legacy" in desc:
            # Regenerar desc canónica (Actualización + blurb + Legacy) — no borrar comentarios
            pass
        api(
            "PUT",
            f"/cards/{existing['id']}",
            {"name": spec["name"], "desc": desc, "idList": id_list},
        )
        for lid in label_ids:
            api("POST", f"/cards/{existing['id']}/idLabels", {"value": lid})
        card_id = existing["id"]
        short_url = existing["shortUrl"]
    else:
        card = api(
            "POST",
            "/cards",
            {
                "name": spec["name"],
                "desc": desc,
                "idList": id_list,
                "pos": "top",
                "idLabels": id_labels,
            },
        )
        card_id = card["id"]
        short_url = card["shortUrl"]
        print("creada:", spec["code"], short_url)

    if not skip_attachments:
        existing_att = {a.get("name") for a in (api("GET", f"/cards/{card_id}/attachments") or [])}
        for fp in [*spec["demo"], *spec["legacy"]]:
            if not fp.is_file():
                print("  falta archivo:", fp)
                continue
            if fp.name in existing_att:
                print("  adjunto ya:", fp.name)
                continue
            upload_file(card_id, fp)
            print("  adjunto:", fp.name)
            time.sleep(0.25)

    if not already_has_reu2_comment(card_id):
        add_comment(card_id, spec["comment"])
        print("  comentario Solicitudes Reunión 2 ok")
    else:
        print("  comentario Solicitudes Reunión 2 ya existe (conservado)")

    return {
        "name": spec["name"],
        "shortUrl": short_url,
        "id": card_id,
        "was_update": was_update,
    }


def update_index(created: list[dict], dry_run: bool) -> str | None:
    """Actualiza índice: Actualización ARRIBA + registro ABAJO; comentario Update adicional."""
    import importlib.util

    mod_path = ROOT / "crear-tarjeta-reunion2-trello.py"
    spec = importlib.util.spec_from_file_location("reunion2_index", mod_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar {mod_path}")
    idx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(idx)

    idx.KEY = KEY
    idx.TOKEN = TOKEN

    m = idx.card_map()
    registro = idx.build_desc(m)
    pending = registro.count(idx.PENDING)

    existing = None
    for c in m.values():
        if "Registro demo" in c["name"] and "Reunión 2" in c["name"]:
            existing = c
            break

    if dry_run:
        print(f"[dry] indice PENDING restantes={pending}")
        return existing["shortUrl"] if existing else None

    if not existing:
        print("WARN: no se encontró índice Reunión 2")
        return None

    urls = "\n".join(
        f"• [{c['name'].replace('Mock — ', '')}]({c['shortUrl']})" for c in created
    )
    update_block = f"""**Actualización** · {UPDATE_DATE}

Quedaron creadas y enlazadas las pantallas nuevas pedidas en la Reunión 2 (mock demo + captura de referencia):

{urls}

El registro completo de la reunión se mantiene **abajo** (no se borra).
Los avances posteriores van como comentarios nuevos."""

    full = api("GET", f"/cards/{existing['id']}", {"fields": "desc"}) or {}
    prev_body = strip_actualizacion(full.get("desc") or "")
    # Preferir registro regenerado (links frescos); si el cuerpo no parece registro, conservar
    if "R2-C01" in prev_body or "Reunión 2 - Registro demo" in prev_body:
        body = registro
    else:
        body = prev_body or registro
    if not body.startswith("**Registro original"):
        body = f"**Registro original Reunión 2** _(conservado)_\n\n{body}"

    new_desc = compose_update_over_body(update_block, body)
    api("PUT", f"/cards/{existing['id']}", {"desc": new_desc, "idList": ID_QA_ALMAHUE})

    # Comentario de registro: solo si falta (nunca reemplazar)
    if not has_comment_with(existing["id"], "Registro original Reunión 2"):
        add_comment(
            existing["id"],
            f"""**Registro original Reunión 2** · {UPDATE_DATE}

Índice de solicitudes, pantallas nuevas, correcciones sobre pantallas existentes,
decisiones, pendientes y compromisos de la Reunión 2.

El detalle completo (con enlaces) está en la descripción, sección «Registro original Reunión 2».""",
        )
        print("  comentario Registro original añadido")

    update_needle = f"Update {UPDATE_DATE} — pantallas nuevas Reunión 2"
    if has_comment_with(existing["id"], update_needle):
        print("  comentario Update ya existe (no duplicar)")
    else:
        add_comment(
            existing["id"],
            f"""**{update_needle}**

Quedaron listas las pantallas nuevas de la Reunión 2 (mock demo + referencia de la reunión):

{urls}

Los enlaces están en la descripción. El comentario de registro original se conserva.""",
        )
        print("  comentario Update añadido")

    print("índice actualizado:", existing["shortUrl"], f"(PENDING={pending})")
    return existing["shortUrl"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-attachments", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    args = parser.parse_args()

    # Validar archivos
    missing = []
    for spec in NEW_SCREENS:
        for fp in [*spec["demo"], *spec["legacy"]]:
            if not fp.is_file():
                missing.append(str(fp))
    if missing:
        print("WARN archivos faltantes:")
        for m in missing:
            print(" ", m)

    labels = api("GET", f"/boards/{BOARD}/labels")
    lists = api("GET", f"/boards/{BOARD}/lists", {"fields": "name,id"})
    id_dev = find_list_id(lists, "En desarrollo", "En proceso")

    lab_mock = ensure_label(labels, LABEL_MOCKUP, "blue") if not args.dry_run else "dry"
    lab_sol2 = ensure_label(labels, LABEL_SOL2, "purple") if not args.dry_run else "dry"
    lab_fuera2 = ensure_label(labels, LABEL_FUERA2, "red") if not args.dry_run else "dry"
    label_ids = [lab_mock, lab_sol2, lab_fuera2]

    created: list[dict] = []
    for spec in NEW_SCREENS:
        card = create_or_update_screen(
            spec,
            id_list=id_dev,
            label_ids=label_ids,
            dry_run=args.dry_run,
            skip_attachments=args.skip_attachments,
        )
        created.append(card)
        # Update solo si la tarjeta ya existía (no en el alta inicial)
        if not args.dry_run and card.get("was_update"):
            needle = f"Update {UPDATE_DATE}"
            if has_comment_with(card["id"], needle, "pantalla nueva Reunión 2"):
                print("  comentario Update ya existe")
            else:
                add_comment(
                    card["id"],
                    f"**{needle}** · Pantalla nueva de Reunión 2 actualizada con capturas "
                    f"del mock demo y de la referencia de la reunión "
                    f"(comentario Solicitudes Reunión 2 conservado).",
                )
                print("  comentario Update añadido")
        time.sleep(0.2)

    index_url = None
    if not args.skip_index:
        # Parche runtime: el índice debe resolver N1–N4 por nombre
        index_url = update_index(created, args.dry_run)

    print("\n=== RESUMEN ===")
    for c in created:
        print(c["name"], "->", c["shortUrl"])
    if index_url:
        print("Índice Reunión 2 ->", index_url)


if __name__ == "__main__":
    main()
