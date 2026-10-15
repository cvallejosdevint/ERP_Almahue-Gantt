"""Descarga la categoria ES:Chile de Wiktionary a un JSON de referencia.

La lista no se aplica como reemplazo. Muchos lemas son palabras comunes
(papa, mina, once) que en una reunion de ERP no hay que reescribir.
Sirve para revisar el prompt y el diccionario a mano.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "chilenismos-wiktionary.json"
API = "https://es.wiktionary.org/w/api.php"
UA = "AlmahueERP-transcript-lexico/2026-10-13 (uso interno; contacto local)"


def descargar() -> list[str]:
    terminos: list[str] = []
    cmcontinue = None
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": "Categoría:ES:Chile",
            "cmlimit": "500",
            "format": "json",
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
        url = API + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        members = data.get("query", {}).get("categorymembers", [])
        for item in members:
            titulo = item["title"]
            if any(titulo.startswith(p) for p in ("Categoría:", "Plantilla:", "Apéndice:", "Wikcionario:")):
                continue
            terminos.append(titulo)
        cont = data.get("continue") or {}
        cmcontinue = cont.get("cmcontinue")
        if not cmcontinue:
            break
    return sorted(set(terminos))


def main() -> int:
    terminos = descargar()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(terminos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {OUT} total={len(terminos)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
