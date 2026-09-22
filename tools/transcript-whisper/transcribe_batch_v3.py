"""Carga large-v3 una vez y transcribe una lista JSON de jobs."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from faster_whisper import WhisperModel

PROMPT = (
    "Reunión de ERP agrícola en Chile. Español chileno. "
    "Vocabulario: Almahue, AlmaWeb, Agrosoft, cotización, orden de compra, "
    "orden de venta, proforma, cartola, GoSocket, SII, CAF, folio, "
    "nota de crédito, nota de débito, centro de costo, PIN, MJ, Agustín."
)


def _prepend_nvidia_cuda_bins() -> None:
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


def write_md(out: Path, title: str, source: str, model: str, device: str, compute: str, segments, info) -> int:
    lines = [
        f"# {title}",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        f"Modelo: faster-whisper `{model}` {device} {compute} + VAD",
        f"Fuente: {source}",
        "No es fuente de requisitos. Contrastar con tl;dv y minutas MJ/Agustín.",
        "",
    ]
    n = 0
    for seg in segments:
        t0 = int(seg.start)
        hh, rem = divmod(t0, 3600)
        mm, ss = divmod(rem, 60)
        stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
        text = (seg.text or "").strip()
        if not text:
            continue
        lines.append(f"- [{stamp}] {text}")
        n += 1
        try:
            print(f"[{stamp}] {text}", flush=True)
        except UnicodeEncodeError:
            print(f"[{stamp}] {text.encode('ascii', 'replace').decode('ascii')}", flush=True)
    body = "\n".join(lines) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print(f"WROTE {out} chars={len(body)} segs={n}", flush=True)
    return n


def already_v3(path: Path) -> bool:
    if not path.is_file():
        return False
    head = path.read_text(encoding="utf-8", errors="replace")[:800]
    return "`large-v3`" in head and "cuda" in head


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--jobs", required=True)
    p.add_argument("--model", default="large-v3")
    p.add_argument("--device", default="cuda")
    p.add_argument("--compute-type", default="float16")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()

    jobs = json.loads(Path(args.jobs).read_text(encoding="utf-8-sig"))
    _prepend_nvidia_cuda_bins()
    print(f"LOAD model={args.model} device={args.device} {args.compute_type}", flush=True)
    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)

    ok = 0
    skip = 0
    fail = 0
    for job in jobs:
        audio = Path(job["audio"])
        out = Path(job["out"])
        title = job.get("title") or "Transcripción Whisper local"
        source = job.get("source") or audio.name
        copy_raw = job.get("copyTo") or []
        if isinstance(copy_raw, str):
            copy_to = [Path(copy_raw)]
        else:
            copy_to = [Path(x) for x in copy_raw]
        print(f"==== {job.get('id', out.parent.name)} ====", flush=True)
        if not audio.is_file():
            print(f"SKIP missing audio {audio}", flush=True)
            fail += 1
            continue
        if not args.force and already_v3(out):
            print(f"SKIP already large-v3 {out}", flush=True)
            skip += 1
            for dest in copy_to:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
            continue
        try:
            segments, info = model.transcribe(
                str(audio),
                language="es",
                vad_filter=True,
                initial_prompt=PROMPT,
                condition_on_previous_text=False,
            )
            write_md(out, title, source, args.model, args.device, args.compute_type, segments, info)
            for dest in copy_to:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
                print(f"COPIED {dest}", flush=True)
            ok += 1
        except Exception as e:
            print(f"FAIL {job.get('id')}: {e}", flush=True)
            fail += 1
    print(f"DONE ok={ok} skip={skip} fail={fail}", flush=True)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
