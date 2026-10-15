"""Compara la pasada lexico con el Whisper anterior, por marca de tiempo.

No reescribe transcripciones. Informa solo cambios que mueven un termino del ERP,
un nombre o un numero. Una diferencia de segmentacion o de tilde no entra.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

OLD = Path(r"E:\source\repos\Almahue\docs\reuniones\medios\whisper-local")
NEW = Path(r"E:\source\repos\Almahue\docs\reuniones\medios\whisper-lexico")
OUT = Path(r"E:\source\repos\Almahue\docs\requerimientos\toma-limpia-2026-10-13\contraste-whisper-lexico.md")

STAMP = re.compile(r"^- \[(\d{2}:\d{2}(?::\d{2})?)\]\s*(.*)$")
TERM = re.compile(
    r"\b("
    r"gosocket|go socket|almahue|almahue|alma ?web|almaweb|agrosoft|agrisoft|"
    r"proforma|cartola|cuartel|predio|yuan|buk|book|merma|"
    r"cotizaci[oó]n|gu[ií]a|sii|acepta|yofactur\w*|"
    r"\d+\s*d[ií]as|siete|ocho"
    r")\b",
    re.I,
)


def fold(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def secs(stamp: str) -> int:
    parts = [int(x) for x in stamp.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def segments(path: Path) -> list[tuple[int, str]]:
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = STAMP.match(line.strip())
        if m and m.group(2).strip():
            rows.append((secs(m.group(1)), m.group(2).strip()))
    return rows


def terms(text: str) -> set[str]:
    found = set()
    for m in TERM.finditer(text):
        t = fold(m.group(1))
        t = t.replace("go socket", "gosocket")
        t = t.replace("alma web", "almaweb")
        t = t.replace("almahue", "almahue")
        t = t.replace("agrisoft", "agrosoft")
        found.add(t)
    return found


def overlap(a: str, b: str) -> float:
    wa, wb = set(fold(a).split()), set(fold(b).split())
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


def count_terms(rows: list[tuple[int, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for _, text in rows:
        for term in terms(text):
            counts[term] = counts.get(term, 0) + 1
    return counts


def main() -> int:
    lines = [
        "# Contraste Whisper anterior contra pasada lexico",
        "",
        "Misma pista de audio. La pasada nueva usa el prompt chileno, hotwords y el diccionario.",
        "Se compara cada segmento con el anterior mas cercano (8 segundos) y solo si hablan de lo mismo.",
        "Entra un cambio cuando un termino del ERP, un nombre o un numero esta en una version y no en la otra.",
        "Las transcripciones citadas no se modificaron.",
        "",
    ]
    total = 0
    files = 0
    tally: dict[str, list[int]] = {}
    for new in sorted(NEW.glob("*/transcripcion.md")):
        old = OLD / new.parent.name / "transcripcion-whisper.md"
        if not old.is_file():
            lines.append(f"## {new.parent.name}")
            lines.append("")
            lines.append("Sin transcripcion Whisper anterior para comparar.")
            lines.append("")
            continue
        files += 1
        old_rows = segments(old)
        new_rows = segments(new)
        for term, n in count_terms(old_rows).items():
            tally.setdefault(term, [0, 0])[0] += n
        for term, n in count_terms(new_rows).items():
            tally.setdefault(term, [0, 0])[1] += n
        hits = []
        for t, text in new_rows:
            near = [row for row in old_rows if abs(row[0] - t) <= 8]
            if not near:
                continue
            old_t, old_text = min(near, key=lambda row: abs(row[0] - t))
            if overlap(text, old_text) < 0.35:
                continue
            lost = terms(old_text) - terms(text)
            gained = terms(text) - terms(old_text)
            if not lost and not gained:
                continue
            mm, ss = divmod(t, 60)
            hh, mm = divmod(mm, 60)
            stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
            hits.append((stamp, sorted(lost), sorted(gained), old_text[:240], text[:240]))
        if not hits:
            continue
        total += len(hits)
        lines.append(f"## {new.parent.name} ({len(hits)})")
        lines.append("")
        for stamp, lost, gained, old_text, new_text in hits[:8]:
            lines.append(f"- [{stamp}] sale: {', '.join(lost) or '-'} | entra: {', '.join(gained) or '-'}")
            lines.append(f"  - antes: {old_text}")
            lines.append(f"  - ahora: {new_text}")
        if len(hits) > 8:
            lines.append(f"- ... {len(hits) - 8} cambios mas en este archivo")
        lines.append("")
    lines.append("## Conteo de terminos en todo el audio")
    lines.append("")
    lines.append("| Termino | Antes | Ahora |")
    lines.append("|---|---:|---:|")
    for term, (a, b) in sorted(tally.items(), key=lambda kv: abs(kv[1][1] - kv[1][0]), reverse=True):
        lines.append(f"| {term} | {a} | {b} |")
    lines.append("")
    lines.append(f"Archivos comparados: {files}. Segmentos con cambio de termino: {total}.")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"WROTE {OUT} files={files} hits={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
