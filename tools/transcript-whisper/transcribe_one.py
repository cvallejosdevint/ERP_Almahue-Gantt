"""Transcribe one WAV with faster-whisper → markdown with timestamps."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from faster_whisper import WhisperModel


def _prepend_nvidia_cuda_bins() -> None:
    """CTranslate2 needs cublas64_12.dll on PATH (pip nvidia-*-cu12 wheels)."""
    try:
        import site
    except ImportError:
        return
    extra: list[str] = []
    for root in site.getsitepackages() + [str(Path(sys.prefix) / "Lib" / "site-packages")]:
        nvidia = Path(root) / "nvidia"
        if not nvidia.is_dir():
            continue
        for sub in ("cublas", "cuda_runtime", "cudnn", "cuda_nvrtc"):
            bin_dir = nvidia / sub / "bin"
            if bin_dir.is_dir():
                extra.append(str(bin_dir))
    if extra:
        os.environ["PATH"] = os.pathsep.join(extra) + os.pathsep + os.environ.get("PATH", "")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--audio", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--title", default="Transcripción Whisper local")
    p.add_argument("--source", default="")
    p.add_argument("--model", default="small")
    p.add_argument("--device", default="cpu", help="cpu | cuda | auto")
    p.add_argument(
        "--compute-type",
        default="int8",
        dest="compute_type",
        help="cpu: int8. cuda: float16 o int8_float16",
    )
    p.add_argument("--cpu-threads", type=int, default=0, dest="cpu_threads")
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

    if args.device in ("cuda", "auto"):
        _prepend_nvidia_cuda_bins()

    kw = {"device": args.device, "compute_type": args.compute_type}
    if args.cpu_threads:
        kw["cpu_threads"] = args.cpu_threads
    model = WhisperModel(args.model, **kw)
    segments, info = model.transcribe(
        str(audio),
        language="es",
        vad_filter=True,
        initial_prompt=args.prompt,
        condition_on_previous_text=False,
    )

    lines = [
        f"# {args.title}",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        f"Modelo: faster-whisper `{args.model}` {args.device} {args.compute_type} + VAD",
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
