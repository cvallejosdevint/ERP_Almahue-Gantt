#!/usr/bin/env python3
"""
Extrae listas + tarjetas de un tablero Trello existente (API gratis).

Útil antes de importar: ver qué hay (~25 tarjetas), evitar duplicados, diff.

Setup: mismas credenciales que importar-trello.py
  https://trello.com/power-ups/admin  → API Key + Token
  URL del tablero → TRELLO_BOARD = XXXX

Uso (PowerShell):
  # A) Desde export JSON del tablero (sin API):
  python extraer-trello.py --from-json "c:\\Users\\c\\Downloads\\wixKcrP0 - almahue-erp.json"

  # B) Desde API:
  $env:TRELLO_KEY = "..."
  $env:TRELLO_TOKEN = "..."
  $env:TRELLO_BOARD = "XXXXXXXX"
  python extraer-trello.py

Salida (en esta carpeta):
  trello-snapshot.json   — dump completo
  trello-snapshot.md     — legible por lista
  trello-snapshot.csv    — lista, título, labels, url
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT_JSON = BASE / "trello-snapshot.json"
OUT_MD = BASE / "trello-snapshot.md"
OUT_CSV = BASE / "trello-snapshot.csv"


def api(method: str, path: str, key: str, token: str, data: dict | None = None) -> dict | list:
    params = {"key": key, "token": token}
    body = None
    headers = {}
    if method == "GET" and data:
        params.update(data)
    url = f"https://api.trello.com/1{path}?{urllib.parse.urlencode(params)}"
    if method != "GET" and data:
        body = urllib.parse.urlencode(data).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise SystemExit(f"Trello API {method} {path} → {e.code}: {err}") from e


def creds() -> tuple[str, str, str]:
    key = os.environ.get("TRELLO_KEY") or os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_TOKEN")
    board = os.environ.get("TRELLO_BOARD") or os.environ.get("TRELLO_BOARD_ID")
    if not key or not token or not board:
        raise SystemExit(
            "Faltan variables de entorno:\n"
            "  TRELLO_KEY / TRELLO_TOKEN / TRELLO_BOARD\n"
            "Ver IMPORTAR-TRELLO.md"
        )
    # Acepta URL completa o solo el shortLink / id
    if "trello.com/b/" in board:
        board = board.rstrip("/").split("/b/")[1].split("/")[0]
    return key, token, board


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrae snapshot de un tablero Trello")
    parser.add_argument(
        "--from-json",
        metavar="FILE",
        help="Parsea un export JSON local (sin API)",
    )
    args = parser.parse_args()
    if args.from_json:
        from _parse_export import main as parse_main

        sys.argv = ["_parse_export.py", args.from_json]
        parse_main()
        return

    key, token, board_id = creds()

    board = api("GET", f"/boards/{board_id}", key, token, {"fields": "name,url,shortLink"})
    lists = api(
        "GET",
        f"/boards/{board_id}/lists",
        key,
        token,
        {"fields": "name,closed,pos", "filter": "open"},
    )
    cards = api(
        "GET",
        f"/boards/{board_id}/cards",
        key,
        token,
        {
            "fields": "name,desc,idList,url,shortUrl,labels,idLabels,closed,pos,due,idChecklists",
            "filter": "open",
            "attachments": "true",
            "attachment_fields": "name,url,mimeType",
            "checklists": "all",
            "checklist_fields": "name",
        },
    )

    list_by_id = {lst["id"]: lst for lst in lists}
    # Orden de listas por pos
    ordered_lists = sorted(lists, key=lambda x: x.get("pos", 0))

    snapshot = {
        "board": board,
        "lists": ordered_lists,
        "cards": cards,
        "counts": {
            "lists": len(ordered_lists),
            "cards": len(cards),
        },
    }
    OUT_JSON.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown
    md: list[str] = [
        f"# Snapshot Trello: {board.get('name', board_id)}",
        "",
        f"- URL: {board.get('url', '')}",
        f"- Listas abiertas: **{len(ordered_lists)}**",
        f"- Tarjetas abiertas: **{len(cards)}**",
        "",
    ]
    cards_by_list: dict[str, list] = {lst["id"]: [] for lst in ordered_lists}
    orphan: list = []
    for c in cards:
        lid = c.get("idList")
        if lid in cards_by_list:
            cards_by_list[lid].append(c)
        else:
            orphan.append(c)

    for lst in ordered_lists:
        group = sorted(cards_by_list[lst["id"]], key=lambda x: x.get("pos", 0))
        md.append(f"## {lst['name']} ({len(group)})")
        md.append("")
        if not group:
            md.append("_Sin tarjetas_")
            md.append("")
            continue
        for c in group:
            labels = ", ".join(lb.get("name") or lb.get("color", "") for lb in c.get("labels") or [])
            label_s = f" `{labels}`" if labels else ""
            md.append(f"- [{c['name']}]({c.get('shortUrl') or c.get('url')}){label_s}")
            desc = (c.get("desc") or "").strip()
            if desc:
                first = desc.splitlines()[0][:120]
                md.append(f"  - _{first}_")
            atts = c.get("attachments") or []
            if atts:
                md.append(f"  - Adjuntos: {len(atts)}")
            checks = c.get("checklists") or []
            if checks:
                n_items = sum(len(ch.get("checkItems") or []) for ch in checks)
                md.append(f"  - Checklists: {len(checks)} ({n_items} ítems)")
        md.append("")

    if orphan:
        md.append(f"## (sin lista) ({len(orphan)})")
        md.append("")
        for c in orphan:
            md.append(f"- {c['name']}")
        md.append("")

    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    # CSV
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lista", "titulo", "labels", "url", "adjuntos", "tiene_desc"])
        for lst in ordered_lists:
            for c in sorted(cards_by_list[lst["id"]], key=lambda x: x.get("pos", 0)):
                labels = "|".join(lb.get("name") or lb.get("color", "") for lb in c.get("labels") or [])
                w.writerow(
                    [
                        lst["name"],
                        c["name"],
                        labels,
                        c.get("shortUrl") or c.get("url") or "",
                        len(c.get("attachments") or []),
                        "si" if (c.get("desc") or "").strip() else "no",
                    ]
                )

    print(f"Tablero: {board.get('name')} — {board.get('url')}")
    print(f"Listas: {len(ordered_lists)} | Tarjetas: {len(cards)}")
    for lst in ordered_lists:
        n = len(cards_by_list[lst["id"]])
        print(f"  {lst['name']}: {n}")
    print()
    print(f"Escrito: {OUT_MD.name}")
    print(f"Escrito: {OUT_CSV.name}")
    print(f"Escrito: {OUT_JSON.name}")


if __name__ == "__main__":
    main()
    sys.exit(0)
