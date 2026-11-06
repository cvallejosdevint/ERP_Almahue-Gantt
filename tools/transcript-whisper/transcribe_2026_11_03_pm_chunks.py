"""Retranscribe PM 2026-11-03 en chunks de 30 min (evita OOM FFT)."""
from __future__ import annotations

import sys
import subprocess
import time
from pathlib import Path

_TOOL = Path(__file__).resolve().parent
_REPO = _TOOL.parents[1]
_LEXICO = _REPO / "tools" / "transcript-lexico"
sys.path.insert(0, str(_TOOL))
sys.path.insert(0, str(_LEXICO))

from normalize import load_hotwords, load_initial_prompt, normalize_chilean_transcript  # noqa: E402
from transcribe_one import _prepend_nvidia_cuda_bins  # noqa: E402
from faster_whisper import WhisperModel  # noqa: E402

FFMPEG = r"C:\OctoPrint\ffmpeg.exe"
PM_WAV = _REPO / "docs/reuniones/medios/whisper-local/2026-11-03-reunion-pm/audio.wav"
CHUNK_DIR = PM_WAV.parent / "chunks"
OUT_PM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-pm.md"
OUT_AM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-am.md"
OUT_FULL = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md"
SEG = 1800  # 30 min


def split_wav() -> list[Path]:
    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    for old in CHUNK_DIR.glob("chunk_*.wav"):
        old.unlink()
    pattern = str(CHUNK_DIR / "chunk_%03d.wav")
    subprocess.run(
        [FFMPEG, "-y", "-i", str(PM_WAV), "-f", "segment", "-segment_time", str(SEG), "-c", "copy", pattern],
        check=True,
    )
    return sorted(CHUNK_DIR.glob("chunk_*.wav"))


def transcribe_pm() -> str:
    _prepend_nvidia_cuda_bins()
    chunks = split_wav()
    print(f"Chunks: {len(chunks)}")
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    prompt = load_initial_prompt()
    hotwords = load_hotwords()

    lines = [
        "# Reunion Almahue 2026-11-03 PM (Whisper large-v3 + lexico)",
        "",
        "Modelo: faster-whisper `large-v3` cuda float16 + VAD (chunks 30 min)",
        "Fuente: Screen Recording 2026-11-03 173934.mp4 (02:38:24)",
        "Normalizacion: tools/transcript-lexico.",
        "",
    ]

    for i, chunk in enumerate(chunks):
        offset = i * SEG
        print(f"\n--- chunk {i+1}/{len(chunks)} offset={offset}s ---")
        segments, _info = model.transcribe(
            str(chunk),
            language="es",
            vad_filter=True,
            beam_size=5,
            initial_prompt=prompt,
            hotwords=hotwords,
            condition_on_previous_text=False,
        )
        for seg in segments:
            t0 = int(seg.start) + offset
            hh, rem = divmod(t0, 3600)
            mm, ss = divmod(rem, 60)
            stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
            text = normalize_chilean_transcript((seg.text or "").strip())
            if not text:
                continue
            lines.append(f"- [{stamp}] {text}")
            print(f"[PM {stamp}] {text[:70]}", flush=True)

    body = "\n".join(lines) + "\n"
    OUT_PM.write_text(body, encoding="utf-8")
    return body


def merge_full() -> None:
    am = OUT_AM.read_text(encoding="utf-8") if OUT_AM.is_file() else ""
    pm = OUT_PM.read_text(encoding="utf-8")
    full = (
        "# Reunion Almahue 2026-11-03 (Whisper large-v3 + lexico)\n\n"
        "Sesiones: AM (~42 min) + PM (~2 h 38 min). Screen recordings Windows.\n\n"
        "## Parte AM\n\n"
        + "\n".join(am.splitlines()[8:])
        + "\n## Parte PM\n\n"
        + "\n".join(pm.splitlines()[8:])
    )
    OUT_FULL.write_text(full, encoding="utf-8")


def main() -> int:
    t0 = time.time()
    transcribe_pm()
    merge_full()
    print(f"\nPM ok en {time.time()-t0:.0f}s -> {OUT_PM}")
    print(OUT_FULL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
