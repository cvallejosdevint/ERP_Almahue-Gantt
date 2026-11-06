"""Genera minuta markdown + HTML interactivo desde transcripcion consolidada 2026-11-03."""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from transcribe_2026_11_03 import build_interactive_html, ollama_minuta  # noqa: E402

OUT_FULL = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md"
OUT_AM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-am.md"
OUT_PM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-pm.md"
MINUTA = _REPO / "docs/reuniones/minutas/reunion-2026-11-03-cliente.md"
HTML = _REPO / "docs/reuniones/minutas/reunion-2026-11-03-cliente-interactiva.html"


def load_items(path: Path, session: str) -> list[dict]:
    items = []
    if not path.is_file():
        return items
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- ["):
            continue
        m = __import__("re").match(r"- \[(\d{2}:\d{2}(?::\d{2})?)\] (.*)", line)
        if m:
            items.append({"session": session, "stamp": m.group(1), "text": m.group(2), "anchor": ""})
    return items


def main() -> int:
    if not OUT_FULL.is_file():
        raise SystemExit(f"Falta {OUT_FULL}")
    full = OUT_FULL.read_text(encoding="utf-8")
    print("Ollama minuta...")
    try:
        minuta = ollama_minuta(full)
    except Exception as e:
        print(f"Ollama: {e}")
        minuta = "# Reunion 2026-11-03\n\nVer transcripcion consolidada.\n"
    MINUTA.write_text(minuta, encoding="utf-8")
    items = load_items(OUT_AM, "AM") + load_items(OUT_PM, "PM")
    HTML.write_text(build_interactive_html(minuta, items), encoding="utf-8")
    print(MINUTA)
    print(HTML)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
