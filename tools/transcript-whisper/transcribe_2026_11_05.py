"""Transcribe la reunion 2026-11-05 con faster-whisper large-v3 y el lexico chileno.

Chunks de 30 min para no repetir el OOM de la sesion PM del 03/11.
"""
from __future__ import annotations

import subprocess
import sys
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
SRC = Path(r"C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-11-05 124610.mp4")
OUT_DIR = _REPO / "docs/reuniones/medios/whisper-local/2026-11-05-reunion"
WAV = OUT_DIR / "audio.wav"
CHUNK_DIR = OUT_DIR / "chunks"
OUT_MD = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-05-reunion.md"
OUT_LOCAL = OUT_DIR / "transcripcion-whisper.md"
SEG = 1800


def extract_wav() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / ".gitignore").write_text("audio.wav\nchunks/\ntranscribe.log\n", encoding="utf-8")
    if WAV.exists() and WAV.stat().st_size > 1_000_000:
        print(f"WAV ya existe: {WAV} ({WAV.stat().st_size} bytes)")
        return
    print("Extrayendo WAV 16 kHz mono...")
    subprocess.run(
        [FFMPEG, "-y", "-i", str(SRC), "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(WAV)],
        check=True,
    )
    print(f"WAV listo: {WAV.stat().st_size} bytes")


def split_wav() -> list[Path]:
    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    existing = sorted(CHUNK_DIR.glob("chunk_*.wav"))
    if existing and sum(p.stat().st_size for p in existing) > 1_000_000:
        print(f"Chunks ya existen: {len(existing)}")
        return existing
    for old in existing:
        old.unlink()
    pattern = str(CHUNK_DIR / "chunk_%03d.wav")
    subprocess.run(
        [FFMPEG, "-y", "-i", str(WAV), "-f", "segment", "-segment_time", str(SEG), "-c", "copy", pattern],
        check=True,
    )
    return sorted(CHUNK_DIR.glob("chunk_*.wav"))


def main() -> int:
    t0 = time.time()
    extract_wav()
    chunks = split_wav()
    print(f"Chunks: {len(chunks)}")
    _prepend_nvidia_cuda_bins()
    print("Cargando Whisper large-v3...")
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    prompt = load_initial_prompt()
    hotwords = load_hotwords()

    lines = [
        "# Reunion Almahue 2026-11-05 (Whisper large-v3 + lexico)",
        "",
        "Idioma: es",
        "Modelo: faster-whisper `large-v3` cuda float16 + VAD (chunks 30 min)",
        "Fuente: Screen Recording 2026-11-05 124610.mp4 (02:46:01)",
        "Normalizacion: tools/transcript-lexico (grafias chilenas y nombres del ERP).",
        "Minuta: docs/reuniones/minutas/reunion-2026-11-05-cliente.md",
        "",
    ]

    for i, chunk in enumerate(chunks):
        offset = i * SEG
        print(f"\n--- chunk {i + 1}/{len(chunks)} offset={offset}s ---", flush=True)
        segments, info = model.transcribe(
            str(chunk),
            language="es",
            vad_filter=True,
            beam_size=5,
            initial_prompt=prompt,
            hotwords=hotwords,
            condition_on_previous_text=False,
        )
        if i == 0:
            lines[2] = f"Idioma: {info.language} (p={info.language_probability:.2f})"
        for seg in segments:
            t = int(seg.start) + offset
            hh, rem = divmod(t, 3600)
            mm, ss = divmod(rem, 60)
            stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
            text = normalize_chilean_transcript((seg.text or "").strip())
            if not text:
                continue
            lines.append(f"- [{stamp}] {text}")
            print(f"[{stamp}] {text[:90]}", flush=True)

    body = "\n".join(lines) + "\n"
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(body, encoding="utf-8")
    OUT_LOCAL.write_text(body, encoding="utf-8")
    print(f"\nTranscripcion lista en {time.time() - t0:.0f}s")
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
