#!/usr/bin/env python3
"""Analiza backup Trello: tarjetas nuevas, adjuntos faltantes."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BACKUP = sorted(Path(__file__).parent.glob("backups/trello-wixKcrP0-*.json"))[-1]
d = json.loads(BACKUP.read_text(encoding="utf-8"))

NEW_KEYS = [
    "Tarifas de contratista",
    "Proformas",
    "Traspaso",
    "Orden de compra (servicios)",
    "Recepción OC",
    "Registro de compra",
    "Bodegas",
    "Movimientos bodega",
    "Indicadores Banco Central",
]

LEGACY_MAP = {
    "Tarifas de contratista": ["03-tarifas-contratista.png"],
    "Proformas": [],
    "Traspaso": [],
    "Orden de compra (servicios)": ["06-orden-compra.png", "07-distribucion-cc.png"],
    "Recepción OC": ["09-recepcion-oc.png"],
    "Registro de compra": ["10-registro-compra.png"],
    "Bodegas": ["12-bodegas.png"],
    "Movimientos bodega": ["13-nc-devolucion.png"],
    "Indicadores Banco Central": ["15-indicadores-bc.png"],
}


def is_image(att: dict) -> bool:
    name = (att.get("name") or "").lower()
    mime = att.get("mimeType") or ""
    return mime.startswith("image/") or name.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))


print(f"Backup: {BACKUP.name}")
print(f"Exportado: {d.get('exportedAt')}")
print(f"Cards total: {len(d['cards'])}")

open_cards = [c for c in d["cards"] if not c.get("closed")]
print(f"Cards abiertas: {len(open_cards)}")

print("\n=== TARJETAS NUEVAS (Reunión 1) ===")
missing = []
for c in sorted(open_cards, key=lambda x: x["name"]):
    if not any(k.lower() in c["name"].lower() for k in NEW_KEYS):
        continue
    atts = c.get("attachments") or []
    imgs = [a for a in atts if is_image(a)]
    print(f"\n#{c['idShort']} {c['name']}")
    print(f"  Lista: {c.get('listName')} | Etiquetas: {', '.join(c.get('labelNames') or [])}")
    print(f"  Adjuntos: {len(atts)} | Imágenes: {len(imgs)}")
    for a in atts:
        print(f"    · {a.get('name')} [{a.get('mimeType') or 'url'}]")
    key = next(k for k in NEW_KEYS if k.lower() in c["name"].lower())
    legacy = LEGACY_MAP.get(key, [])
    if not imgs:
        print("  ⚠ SIN CAPTURA en Trello")
        missing.append((c, legacy))
    elif legacy:
        names = {a.get("name", "").lower() for a in imgs}
        for lg in legacy:
            if lg.lower() not in names and not any(lg.split(".")[0] in n for n in names):
                print(f"  ? legacy esperado: {lg}")

print("\n=== MOCKS SIN IMAGEN ===")
for c in sorted(open_cards, key=lambda x: x["name"]):
    if "Mock" not in c["name"]:
        continue
    imgs = [a for a in (c.get("attachments") or []) if is_image(a)]
    if not imgs:
        print(f"  #{c['idShort']} {c['name']} ({c.get('listName')})")

print("\n=== RESUMEN CAPTURAS FALTANTES (legacy disponible) ===")
for c, legacy in missing:
    print(f"  {c['name']}: legacy={legacy or 'NO HAY PNG legacy'}")
