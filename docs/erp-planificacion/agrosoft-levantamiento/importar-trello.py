#!/usr/bin/env python3
"""
Importa listas + tarjetas del levantamiento Agrosoft a un tablero Trello (API gratis).

Setup (una vez, ~2 min):
  1. Abre https://trello.com/power-ups/admin  (o https://trello.com/app-key)
  2. Copia tu API Key
  3. Genera un Token (Allow) y cópialo
  4. Abre tu tablero → URL tipo https://trello.com/b/XXXX/nombre
     El BOARD_ID es XXXX (o el id largo; ambos sirven)

Uso:
  set TRELLO_KEY=...
  set TRELLO_TOKEN=...
  set TRELLO_BOARD=XXXX
  python importar-trello.py

Opciones:
  python importar-trello.py --dry-run     # solo muestra qué crearía
  python importar-trello.py --skip-lists  # usa listas ya existentes por nombre
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "matriz-trazabilidad.csv"

# Orden de listas y qué IDs van a cada una
LIST_ORDER = [
    ("00 Decisiones", []),  # se rellena con DEC/PEND desde decisiones
    ("Contratistas", ["C-01", "C-02", "C-03", "C-04", "C-06", "C-07"]),
    ("Compras", ["P-01", "P-03", "P-04", "P-05", "P-06", "P-07", "P-08"]),
    ("Insumos / Bodega", ["P-02", "I-01", "I-02", "I-03", "I-04", "I-05"]),
    ("Contabilidad", ["K-01", "K-02", "K-03", "K-04", "K-05"]),
    ("Permisos / Config", ["C-05"]),
    ("Pendiente cliente", ["X-01", "G-01", "P-04", "I-02"]),
    ("Backlog OPT", []),
]

DECISION_CARDS = [
    ("DEC-01", "NO implementar Mano de Obra (parametrizar en Contratistas)", "DEC"),
    ("DEC-02", "Eliminar Solicitud de Compra", "DEC"),
    ("DEC-03", "Aislamiento estricto por empresa activa", "DEC"),
    ("DEC-04", "Perfil intermedio + roles independientes", "DEC"),
    ("DEC-05", "Monedas foco: peso, dólar, yuan, euro", "DEC"),
    ("DEC-06", "Indicadores Banco Central + feriados/domingos", "DEC"),
    ("DEC-07", "Compras=servicios; Insumos=materiales (maestro único)", "DEC"),
    ("DEC-08", "15 usuarios / sesiones compartidas — riesgo empresa", "DEC"),
    ("DEC-09", "AlmaWeb + Power BI (Gestión Agrosoft no se usa)", "DEC"),
    ("DEC-10", "Maquinaria OUT v1 (solo mención verbal)", "OUT"),
    ("PEND-01", "Decidir política Afecto/Exento en OC", "PEND"),
    ("PEND-02", "¿Múltiples facturas por contrato contratista?", "PEND"),
    ("PEND-03", "Validar niveles de bodega con materiales", "PEND"),
    ("PEND-04", "Alcance Maquinaria / AlmaWeb / dashboards (Mario agosto)", "PEND"),
]


def ts_to_seconds(ts: str) -> int:
    parts = [int(p) for p in ts.strip().split(":")]
    if len(parts) == 2:
        m, s = parts
        return m * 60 + s
    if len(parts) == 3:
        h, m, s = parts
        return h * 3600 + m * 60 + s
    return 0


def api(method: str, path: str, key: str, token: str, data: dict | None = None) -> dict | list:
    params = {"key": key, "token": token}
    body = None
    headers = {}
    if method == "GET":
        if data:
            params.update(data)
        url = f"https://api.trello.com/1{path}?{urllib.parse.urlencode(params)}"
    else:
        url = f"https://api.trello.com/1{path}?{urllib.parse.urlencode(params)}"
        if data:
            body = urllib.parse.urlencode(data).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            import json

            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise SystemExit(f"Trello API {method} {path} → {e.code}: {err}") from e


def load_rows() -> dict[str, dict]:
    rows = {}
    with CSV_PATH.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r
    return rows


def card_desc(row: dict) -> str:
    t0 = row.get("ts_tldv_inicio") or ""
    t1 = row.get("ts_tldv_fin") or ""
    lines = [
        f"**Etiqueta:** {row.get('etiqueta', '')}",
        f"**Módulo:** {row.get('modulo', '')}",
    ]
    if t0:
        lines.append(f"**Marca temporal reunión:** {t0}" + (f" – {t1}" if t1 else ""))
    if row.get("captura_path"):
        lines.append(f"**Captura local:** `{row['captura_path']}`")
    if row.get("notas"):
        lines.append(f"**Notas:** {row['notas']}")
    lines.append("")
    lines.append("Ver detalle en `docs/erp-planificacion/agrosoft-levantamiento/modulos/`.")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-lists", action="store_true", help="Reutilizar listas existentes por nombre exacto")
    args = ap.parse_args()

    key = os.environ.get("TRELLO_KEY") or os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_TOKEN")
    board = os.environ.get("TRELLO_BOARD") or os.environ.get("TRELLO_BOARD_ID")
    if not args.dry_run and (not key or not token or not board):
        print(
            "Faltan variables de entorno.\n"
            "  TRELLO_KEY / TRELLO_TOKEN / TRELLO_BOARD\n"
            "Ver comentario al inicio de este script.",
            file=sys.stderr,
        )
        sys.exit(1)

    rows = load_rows()
    # Map id -> list name (primera coincidencia en LIST_ORDER gana, excepto pendientes)
    id_to_list: dict[str, str] = {}
    for list_name, ids in LIST_ORDER:
        for i in ids:
            if i not in id_to_list or list_name == "Pendiente cliente":
                # PEND/OUT van preferente a Pendiente si están en esa lista
                if list_name == "Pendiente cliente":
                    id_to_list[i] = list_name
                elif i not in id_to_list:
                    id_to_list[i] = list_name

    # Construir plan de tarjetas
    plan: list[tuple[str, str, str, str]] = []  # list, title, desc, label
    for did, title, label in DECISION_CARDS:
        plan.append(("00 Decisiones", f"[{did}] {title}", f"**Etiqueta:** {label}\n\nVer `00-decisiones.md`.", label))

    for cid, row in rows.items():
        list_name = id_to_list.get(cid, row.get("modulo", "Backlog OPT"))
        # Normalizar nombres de lista desde módulo CSV si no mapeado
        if list_name not in [x[0] for x in LIST_ORDER]:
            mapping = {
                "Contratistas": "Contratistas",
                "Compras": "Compras",
                "Insumos": "Insumos / Bodega",
                "Contabilidad": "Contabilidad",
                "Permisos": "Permisos / Config",
                "Pendiente": "Pendiente cliente",
            }
            list_name = mapping.get(list_name, "Backlog OPT")
        title = f"[{cid}] {row['titulo']}"
        plan.append((list_name, title, card_desc(row), row.get("etiqueta", "REQ")))

    print(f"Plan: {len(plan)} tarjetas en {len({p[0] for p in plan})} listas")
    for list_name, title, _, label in plan:
        print(f"  [{label:4}] {list_name:22} | {title}")

    if args.dry_run:
        print("\n--dry-run: no se creó nada en Trello.")
        return

    # Listas existentes
    existing = api("GET", f"/boards/{board}/lists", key, token, {"cards": "none"})
    by_name = {L["name"]: L["id"] for L in existing if not L.get("closed")}

    list_ids: dict[str, str] = {}
    for list_name, _ in LIST_ORDER:
        if list_name in by_name and args.skip_lists:
            list_ids[list_name] = by_name[list_name]
            print(f"Lista existente: {list_name}")
            continue
        if list_name in by_name:
            list_ids[list_name] = by_name[list_name]
            print(f"Reutiliza lista: {list_name}")
            continue
        created = api("POST", "/lists", key, token, {"name": list_name, "idBoard": board, "pos": "bottom"})
        list_ids[list_name] = created["id"]
        print(f"Creada lista: {list_name}")
        time.sleep(0.2)

    # Evitar duplicados por título exacto
    existing_cards = api("GET", f"/boards/{board}/cards", key, token, {"fields": "name,idList"})
    existing_titles = {c["name"] for c in existing_cards}

    created_n = 0
    skipped = 0
    for list_name, title, desc, _label in plan:
        if title in existing_titles:
            skipped += 1
            continue
        lid = list_ids.get(list_name)
        if not lid:
            print(f"SKIP sin lista: {title}")
            continue
        api(
            "POST",
            "/cards",
            key,
            token,
            {"idList": lid, "name": title, "desc": desc, "pos": "bottom"},
        )
        created_n += 1
        print(f"+ {title}")
        time.sleep(0.25)  # rate limit amable

    print(f"\nListo: {created_n} creadas, {skipped} ya existían.")


if __name__ == "__main__":
    main()
