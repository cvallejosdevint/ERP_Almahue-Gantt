"""Transcribe one WAV with faster-whisper → markdown with timestamps."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from faster_whisper import WhisperModel


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--audio", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--title", default="Transcripción Whisper local")
    p.add_argument("--source", default="")
    p.add_argument("--model", default="small")
    p.add_argument(
        "--prompt",
        default=(
            "Reunión de ERP agrícola en Chile. Español chileno. "
            "Vocabulario: Almahue, AlmaWeb, Agrosoft, cotización, orden de compra, "
            "orden de venta, proforma, cartola, GoSocket, SII, CAF, folio, "
            "nota de crédito, nota de débito, centro de costo, PIN, MJ, Agustín."
        ),
        help="initial_prompt para sesgar ASR a léxico chileno/ERP",
    )
    args = p.parse_args()

    audio = Path(args.audio)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio),
        language="es",
        vad_filter=True,
        initial_prompt=args.prompt,
    )

    lines = [
        f"# {args.title}",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        f"Modelo: faster-whisper `{args.model}` CPU int8 + VAD",
        f"Fuente: {args.source or audio.name}",
        "No es fuente de requisitos. Contrastar con tl;dv y minutas MJ/Agustín.",
        "",
    ]
    for seg in segments:
        t0 = int(seg.start)
        hh, rem = divmod(t0, 3600)
        mm, ss = divmod(rem, 60)
        stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
        text = (seg.text or "").strip()
        if not text:
            continue
        lines.append(f"- [{stamp}] {text}")
        try:
            print(f"[{stamp}] {text}", flush=True)
        except UnicodeEncodeError:
            print(f"[{stamp}] {text.encode('ascii', 'replace').decode('ascii')}", flush=True)

    body = "\n".join(lines) + "\n"
    out.write_text(body, encoding="utf-8")
    print(f"WROTE {out} chars={len(body)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
