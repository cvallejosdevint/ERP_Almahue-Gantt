#!/usr/bin/env python3
"""Adjunta capturas legacy faltantes a tarjetas nuevas Reunión 1."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"
LEGACY = Path(__file__).resolve().parent / "pantallas-legacy"

ATTACH = {
    "Mock — Proformas y facturas (contratistas)": [
        "16-proformas-contratista.png",
    ],
    "Mock — Traspaso contable y cierre de mes (contratistas)": [
        "17-traspaso-cierre-contratistas.png",
    ],
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
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode()
        return json.loads(raw) if raw else None


def upload(card_id: str, fp: Path):
    url = f"{BASE}/cards/{card_id}/attachments?key={KEY}&token={TOKEN}&name={urllib.parse.quote(fp.name)}"
    subprocess.run(["curl", "-s", "-S", "-X", "POST", url, "-F", f"file=@{fp}"], check=True)


def main():
    cards = api("GET", f"/boards/{BOARD}/cards", {"fields": "name,id,closed"})
    by_name = {c["name"]: c for c in cards if not c.get("closed")}
    for name, files in ATTACH.items():
        card = by_name.get(name)
        if not card:
            print("skip card", name)
            continue
        existing = {a.get("name") for a in (api("GET", f"/cards/{card['id']}/attachments") or [])}
        for fn in files:
            fp = LEGACY / fn
            if not fp.is_file():
                print("missing file", fp)
                continue
            if fn in existing:
                print("already", name, fn)
                continue
            upload(card["id"], fp)
            print("attached", name, fn)


if __name__ == "__main__":
    main()
