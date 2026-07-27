#!/usr/bin/env python3
"""Elimina referencias al video (tl;dv) de descripciones, comentarios y adjuntos en Trello."""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"

TLDV_RE = re.compile(
    r"https?://(?:www\.)?tldv\.io[^\s\)\]\"']*",
    re.IGNORECASE,
)
MD_LINK_TLDV_RE = re.compile(
    r"\[[^\]]*\]\(\s*https?://(?:www\.)?tldv\.io[^)]*\)",
    re.IGNORECASE,
)
VIDEO_LINE_RE = re.compile(
    r"^\s*(?:\*\*)?Video(?:\*\*)?:.*(?:tldv|tl;dv).*\n?",
    re.IGNORECASE | re.MULTILINE,
)
SOLICITUDES_TLDV_RE = re.compile(
    r"\*\*Solicitudes Reunión 1\*\*\s*·\s*(?:\[[^\]]+\]\([^)]+\)|https?://[^\s]+)\s*\n?",
    re.IGNORECASE,
)
SOLICITUDES_CODIGO_TLDV_RE = re.compile(
    r"(\*\*Solicitudes Reunión 1\*\*\s*·\s*)(?:C-\d+|P-\d+|I-\d+|K-\d+[^·\n]*)\s*·\s*https?://[^\s\n]+",
    re.IGNORECASE,
)


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


def clean_text(text: str) -> str:
    if not text:
        return text
    s = text
    s = MD_LINK_TLDV_RE.sub("", s)
    s = TLDV_RE.sub("", s)
    s = VIDEO_LINE_RE.sub("", s)
    s = SOLICITUDES_TLDV_RE.sub("**Solicitudes Reunión 1**\n", s)

    def repl_solicitud(m: re.Match) -> str:
        return m.group(1).rstrip()

    s = SOLICITUDES_CODIGO_TLDV_RE.sub(repl_solicitud, s)
    # Normalizar encabezados de comentario: "Solicitudes Reunión 1 · C-07 · " -> "Solicitudes Reunión 1 · C-07"
    s = re.sub(
        r"(\*\*Solicitudes Reunión 1\*\*\s*·\s*(?:C-\d+|P-\d+|I-\d+|K-\d+(?:\s*/\s*K-\d+)?))\s*·?\s*$",
        r"\1",
        s,
        flags=re.MULTILINE,
    )
    s = re.sub(r"[ \t]+·[ \t]*\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def main():
    cards = api("GET", f"/boards/{BOARD}/cards", {"fields": "name,desc,shortUrl", "filter": "all"})
    changed = 0

    for card in cards:
        cid = card["id"]
        name = card["name"]
        desc = card.get("desc") or ""
        new_desc = clean_text(desc)
        if new_desc != desc.strip():
            api("PUT", f"/cards/{cid}", {"desc": new_desc})
            print("desc:", name[:55])
            changed += 1

        for att in api("GET", f"/cards/{cid}/attachments") or []:
            url = att.get("url") or ""
            if "tldv.io" in url.lower():
                api("DELETE", f"/cards/{cid}/attachments/{att['id']}")
                print("  del attach:", att.get("name") or url[:60])
                changed += 1

        actions = api(
            "GET",
            f"/cards/{cid}/actions",
            {"filter": "commentCard", "fields": "data,date", "limit": "1000"},
        ) or []
        for act in actions:
            text = (act.get("data") or {}).get("text") or ""
            if "tldv.io" not in text.lower() and "tl;dv" not in text.lower():
                continue
            new_text = clean_text(text)
            if not new_text:
                api("DELETE", f"/actions/{act['id']}")
                print("  del comment vacío:", name[:40])
                changed += 1
                continue
            if new_text != text.strip():
                api("PUT", f"/cards/{cid}/actions/{act['id']}/comments", {"text": new_text})
                print("  comment:", name[:40])
                changed += 1

    print(f"Listo. Cambios: {changed}")


if __name__ == "__main__":
    main()
