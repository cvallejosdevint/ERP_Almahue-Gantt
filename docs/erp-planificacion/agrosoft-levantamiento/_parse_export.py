#!/usr/bin/env python3
"""Parsea un export JSON de Trello (archivo local) → trello-snapshot.*"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DEFAULT_SRC = Path(r"c:\Users\c\Downloads\wixKcrP0 - almahue-erp.json")


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    d = json.loads(src.read_text(encoding="utf-8"))

    lists = sorted(
        [lst for lst in d.get("lists", []) if not lst.get("closed")],
        key=lambda x: x.get("pos", 0),
    )
    list_by_id = {lst["id"]: lst for lst in lists}
    cards = [c for c in d.get("cards", []) if not c.get("closed")]
    labels_by_id = {lb["id"]: lb for lb in d.get("labels", [])}
    cl_by_card: dict[str, list] = {}
    for ch in d.get("checklists", []):
        cl_by_card.setdefault(ch.get("idCard"), []).append(ch)

    cards_by_list: dict[str, list] = {lst["id"]: [] for lst in lists}
    for c in cards:
        lid = c.get("idList")
        if lid in cards_by_list:
            cards_by_list[lid].append(c)

    def card_labels(c: dict) -> list[str]:
        out = []
        for lid in c.get("idLabels") or []:
            lb = labels_by_id.get(lid)
            if lb:
                out.append(lb.get("name") or lb.get("color") or "")
        if not out and c.get("labels"):
            out = [lb.get("name") or lb.get("color") or "" for lb in c["labels"]]
        return [x for x in out if x]

    def n_attachments(c: dict) -> int:
        if isinstance(c.get("attachments"), list):
            return len(c["attachments"])
        return (c.get("badges") or {}).get("attachments", 0) or 0

    snapshot = {
        "board": {
            "name": d.get("name"),
            "url": d.get("url") or d.get("shortUrl"),
            "id": d.get("id"),
            "shortLink": d.get("shortLink"),
            "source_file": str(src),
        },
        "lists": [{"id": lst["id"], "name": lst["name"], "pos": lst.get("pos")} for lst in lists],
        "cards": [
            {
                "name": c.get("name"),
                "desc": c.get("desc") or "",
                "idList": c.get("idList"),
                "list": list_by_id.get(c.get("idList"), {}).get("name", "?"),
                "url": c.get("shortUrl") or c.get("url"),
                "labels": card_labels(c),
                "attachments": n_attachments(c),
                "pos": c.get("pos"),
            }
            for c in cards
        ],
        "counts": {"lists": len(lists), "cards": len(cards)},
    }
    (BASE / "trello-snapshot.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md: list[str] = [
        f"# Snapshot Trello: {d.get('name')}",
        "",
        f"- URL: {d.get('url') or d.get('shortUrl')}",
        f"- Fuente: `{src.name}`",
        f"- Listas abiertas: **{len(lists)}**",
        f"- Tarjetas abiertas: **{len(cards)}**",
        "",
    ]
    for lst in lists:
        group = sorted(cards_by_list[lst["id"]], key=lambda x: x.get("pos", 0))
        md.append(f"## {lst['name']} ({len(group)})")
        md.append("")
        if not group:
            md.append("_Sin tarjetas_")
            md.append("")
            continue
        for c in group:
            lbs = card_labels(c)
            label_s = f" `{' | '.join(lbs)}`" if lbs else ""
            url = c.get("shortUrl") or c.get("url") or ""
            md.append(f"- [{c['name']}]({url}){label_s}")
            desc = (c.get("desc") or "").strip()
            if desc:
                first = desc.splitlines()[0][:140]
                md.append(f"  - _{first}_")
            n_att = n_attachments(c)
            if n_att:
                md.append(f"  - Adjuntos: {n_att}")
            chs = cl_by_card.get(c["id"], [])
            if chs:
                n_items = sum(len(ch.get("checkItems") or []) for ch in chs)
                md.append(f"  - Checklists: {len(chs)} ({n_items} ítems)")
        md.append("")

    (BASE / "trello-snapshot.md").write_text("\n".join(md), encoding="utf-8")

    with (BASE / "trello-snapshot.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lista", "titulo", "labels", "url", "adjuntos", "tiene_desc"])
        for lst in lists:
            for c in sorted(cards_by_list[lst["id"]], key=lambda x: x.get("pos", 0)):
                w.writerow(
                    [
                        lst["name"],
                        c["name"],
                        "|".join(card_labels(c)),
                        c.get("shortUrl") or c.get("url") or "",
                        n_attachments(c),
                        "si" if (c.get("desc") or "").strip() else "no",
                    ]
                )

    print(f"Tablero: {d.get('name')}")
    print(f"URL: {d.get('url') or d.get('shortUrl')}")
    print(f"Listas: {len(lists)} | Tarjetas: {len(cards)}")
    for lst in lists:
        print(f"  {lst['name']}: {len(cards_by_list[lst['id']])}")
    print(f"OK -> {BASE / 'trello-snapshot.md'}")


if __name__ == "__main__":
    main()
