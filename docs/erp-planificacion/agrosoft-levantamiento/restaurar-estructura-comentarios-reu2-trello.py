#!/usr/bin/env python3
"""
Restaura estructura acordada Reunión 2 en Trello (sin borrar comentarios):

- Índice DAITP1gF: descripción = Actualización ARRIBA + registro original ABAJO;
  añade comentario «Registro original» si falta (reconstruido desde template).
- N1–N4: verifica que exista comentario Solicitudes Reunión 2; si falta, lo restaura.
- Nunca DELETE de comentarios; solo POST adicionales / PUT de descripción con merge.

Uso:
  python restaurar-estructura-comentarios-reu2-trello.py
  python restaurar-estructura-comentarios-reu2-trello.py --dry-run
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
UPDATE_DATE = "23/07/2026"
IDX_SHORT = "DAITP1gF"

NEW_SCREENS = {
    "kD5faLBC": """**Solicitudes Reunión 2**

• [R2-C01] Ingreso múltiple / diario de mano de obra contratista.
• [R2-C02] Precio editable según situación del día.
• [DEC-11] Referencia AgroSmart; contabilidad de cierre sigue modelo AgroSoft.
• Ruta demo: `/contratistas/ingreso-diario`.

_Restaurado desde template (script pantallas nuevas)._""",
    "TbhPZfMp": """**Solicitudes Reunión 2**

• [R2-C04] Asociación masiva labores → proforma / factura (calce monto).
• [DEC-11] UX tipo AgroSmart; no forzar flujo rígido AgroSoft.
• Ruta demo: `/contratistas/asociacion`.

_Restaurado desde template (script pantallas nuevas)._""",
    "8wHl30Q3": """**Solicitudes Reunión 2**

• [R2-T01] Carga cartola Excel + PDF.
• [PEND-05] Agustín enviará ejemplos Excel + PDF.
• Ruta demo: `/tesoreria/cartolas`.

_Restaurado desde template (script pantallas nuevas)._""",
    "iMCx4eXp": """**Solicitudes Reunión 2**

• [R2-T05] Anticipos productores — calce parcial sin traspaso manual sucio.
• Relacionado con Mock — Pagos (TC / calce documentos).
• Ruta demo: `/tesoreria/anticipos`.

_Restaurado desde template (script pantallas nuevas)._""",
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
        err = e.read().decode(errors="replace")[:300]
        raise RuntimeError(f"{method} {path} → {e.code}: {err}") from e


def list_comments(card_id: str) -> list[dict]:
    return api("GET", f"/cards/{card_id}/actions", {"filter": "commentCard", "limit": "100"}) or []


def has_comment_with(card_id: str, *needles: str) -> bool:
    for a in list_comments(card_id):
        text = (a.get("data") or {}).get("text") or ""
        if all(n in text for n in needles):
            return True
    return False


def add_comment(card_id: str, text: str):
    api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def strip_actualizacion(desc: str) -> str:
    """Quita bloque Actualización del tope si existe; deja el cuerpo (registro/legacy)."""
    if not desc:
        return ""
    s = desc.strip()
    if not s.startswith("**Actualización**"):
        return s
    parts = s.split("\n---\n", 1)
    if len(parts) == 2:
        return parts[1].strip()
    return s


def compose_desc(update_block: str, body: str) -> str:
    body = body.strip()
    # Evitar doble encabezado de registro
    if body.startswith("**Registro original"):
        return f"{update_block.strip()}\n\n---\n\n{body}"
    return (
        f"{update_block.strip()}\n\n---\n\n"
        f"**Registro original Reunión 2** _(conservado)_\n\n{body}"
    )


def restore_index(dry_run: bool) -> None:
    import importlib.util

    mod_path = ROOT / "crear-tarjeta-reunion2-trello.py"
    spec = importlib.util.spec_from_file_location("reunion2_index", mod_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar {mod_path}")
    idx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(idx)
    idx.KEY = KEY
    idx.TOKEN = TOKEN

    card = api("GET", f"/cards/{IDX_SHORT}", {"fields": "name,desc,shortUrl,id"})
    current_desc = card.get("desc") or ""
    body = strip_actualizacion(current_desc)
    # Preferir regenerado con links actuales (misma fuente que template)
    m = idx.card_map()
    registro = idx.build_desc(m)
    # Si el cuerpo actual ya es un registro completo, usar regenerado (más actualizado en links)
    if "Reunión 2 - Registro demo" in body or "R2-C01" in body:
        body = registro
    else:
        body = body or registro

    update_block = f"""**Actualización** · {UPDATE_DATE}

Se crearon / enlazaron las pantallas nuevas N1–N4 (Mock) con captura ERP demo + captura legacy:

• [Ingreso diario labores (contratistas)](https://trello.com/c/kD5faLBC)
• [Asociación labores a proforma/factura](https://trello.com/c/TbhPZfMp)
• [Carga cartola bancaria](https://trello.com/c/8wHl30Q3)
• [Anticipos productores](https://trello.com/c/iMCx4eXp)

El registro original de la reunión se conserva **abajo** (no se borra).
Los updates van como comentarios adicionales; el comentario de registro se mantiene."""

    new_desc = compose_desc(update_block, body)
    print("Índice:", card["shortUrl"])
    print("  desc actual len=", len(current_desc), "->", len(new_desc))

    if dry_run:
        print("  [dry] PUT desc (Actualización + registro)")
    else:
        api("PUT", f"/cards/{card['id']}", {"desc": new_desc})
        print("  desc actualizada (Actualización arriba + registro abajo)")

    # Comentario de registro original (faltaba; solo existía el Update)
    if has_comment_with(card["id"], "Registro original Reunión 2"):
        print("  comentario Registro original: ya existe")
    else:
        # Comentario ancla (resumen); detalle completo en descripción inferior
        original_comment = f"""**Registro original Reunión 2** · {UPDATE_DATE}

Índice de solicitudes, pantallas nuevas, correcciones sobre mocks existentes, DEC-11…15, pendientes y compromisos de la Reunión 2.

El detalle completo (con hipervínculos a mocks) está en la **descripción** de esta tarjeta, sección «Registro original Reunión 2».

_Restaurado desde template `reunion2-registro-trello-template.md` / `build_desc` — en API solo existía el comentario de Update; no había comentario de registro._"""
        if dry_run:
            print("  [dry] POST comentario Registro original")
        else:
            add_comment(card["id"], original_comment)
            print("  comentario Registro original: restaurado")

    if has_comment_with(card["id"], "Update 23/07/2026 — pantallas nuevas"):
        print("  comentario Update pantallas nuevas: conservado")
    else:
        print("  WARN: no se encontró comentario Update (no se recrea para no duplicar ruido)")


def restore_n_screens(dry_run: bool) -> None:
    for short, text in NEW_SCREENS.items():
        card = api("GET", f"/cards/{short}", {"fields": "name,desc,shortUrl,id"})
        print(f"{card['name']}: {card['shortUrl']}")
        if has_comment_with(card["id"], "Solicitudes Reunión 2"):
            print("  comentario Solicitudes Reunión 2: OK (conservado)")
        else:
            if dry_run:
                print("  [dry] POST Solicitudes Reunión 2 (restaurado desde template)")
            else:
                add_comment(card["id"], text)
                print("  comentario Solicitudes Reunión 2: restaurado desde template")

        # Descripción: asegurar Actualización arriba + cuerpo/legacy abajo
        desc = card.get("desc") or ""
        if desc.startswith("**Actualización**") and "**Legacy" in desc:
            print("  desc: estructura Actualización+Legacy OK")
        elif desc:
            body = strip_actualizacion(desc)
            # Si el body perdió el encabezado de pantalla, no inventar; solo envolver
            update = f"**Actualización** · {UPDATE_DATE}\n\n_(estructura restaurada; contenido legacy/registro abajo)_"
            new_desc = f"{update}\n\n---\n\n{body}"
            if dry_run:
                print("  [dry] PUT desc merge Actualización")
            else:
                api("PUT", f"/cards/{card['id']}", {"desc": new_desc})
                print("  desc: merge Actualización aplicado")
        else:
            print("  WARN: desc vacía")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    restore_index(args.dry_run)
    print()
    restore_n_screens(args.dry_run)
    print("\nListo. No se borró ningún comentario.")


if __name__ == "__main__":
    main()
