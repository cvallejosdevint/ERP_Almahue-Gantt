"""Informa que cambiaria el diccionario en las transcripciones ya guardadas.

No escribe sobre los markdown de origen. Esos archivos son la cita de las reuniones.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from normalize import ROOT, diff_stats, load_rules, normalize_chilean_transcript

DEFAULT_SRC = ROOT.parents[1] / "docs" / "reuniones" / "transcripciones"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--src", default=str(DEFAULT_SRC))
    p.add_argument("--out", default=str(ROOT / "out" / "informe-normalizacion.md"))
    args = p.parse_args()
    src = Path(args.src)
    rules = load_rules()
    files = sorted(src.glob("*.md"))
    lines = [
        "# Informe de normalizacion chilena",
        "",
        "Dry-run. No modifica las transcripciones.",
        "",
        "| Archivo | Reemplazos | Reglas |",
        "|---|---:|---|",
    ]
    total = 0
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        stats = diff_stats(text, rules)
        n = sum(stats.values())
        total += n
        detail = ", ".join(f"{k}={v}" for k, v in stats.items()) or "-"
        lines.append(f"| {path.name} | {n} | {detail} |")
    lines.append("")
    lines.append(f"Total de sustituciones que cambian texto: {total}")
    lines.append("")
    lines.append("Una grafia que ya estaba bien (GoSocket, Almahue, AlmaWeb) no se cuenta.")
    lines.append("")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {out} coincidencias={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
