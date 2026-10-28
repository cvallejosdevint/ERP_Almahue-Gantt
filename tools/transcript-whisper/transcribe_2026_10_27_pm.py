"""Transcribe la grabacion de la tarde del 27-10-2026 15.24.m4a (PM) con faster-whisper large-v3 en CUDA float16.
Aplica normalizacion de lexico chileno y nombres del ERP Almahue.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

# Prepend NVIDIA CUDA DLLs
try:
    import site
    for root in site.getsitepackages() + [str(Path(sys.prefix) / "Lib" / "site-packages")]:
        nvidia = Path(root) / "nvidia"
        if not nvidia.is_dir():
            continue
        for sub in ("cublas", "cuda_runtime", "cudnn", "cuda_nvrtc"):
            bin_dir = nvidia / sub / "bin"
            if bin_dir.is_dir():
                os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")
except Exception as e:
    print(f"Aviso CUDA path: {e}")

_TOOL_DIR = Path(__file__).resolve().parent
_REPO = _TOOL_DIR.parents[1]
_LEXICO = _REPO / "tools" / "transcript-lexico"
if str(_LEXICO) not in sys.path:
    sys.path.insert(0, str(_LEXICO))

from normalize import load_hotwords, load_initial_prompt, normalize_chilean_transcript
from faster_whisper import WhisperModel

def main():
    wav_path = _REPO / "docs" / "reuniones" / "medios" / "whisper-local" / "2026-10-27-reunion-tarde" / "audio.wav"
    out_whisper = _REPO / "docs" / "reuniones" / "medios" / "whisper-local" / "2026-10-27-reunion-tarde" / "transcripcion-whisper.md"
    out_transcripciones = _REPO / "docs" / "reuniones" / "transcripciones" / "transcripcion-2026-10-27-reunion-tarde.md"
    log_path = _REPO / "docs" / "reuniones" / "medios" / "whisper-local" / "2026-10-27-reunion-tarde" / "transcribe.log"

    drive_dir = Path(r"G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 15 - 2026-10-26 a 2026-11-01\2026-10-27 Reunion PM")
    try:
        drive_dir.mkdir(parents=True, exist_ok=True)
        drive_transcripcion = drive_dir / "transcripcion.md"
    except Exception as e:
        print(f"Aviso Google Drive no disponible: {e}")
        drive_transcripcion = None

    print(f"Iniciando transcripcion Whisper large-v3 PM en CUDA float16...")
    print(f"Audio WAV: {wav_path}")
    print(f"Fuente original: C:\\Users\\c\\Desktop\\27-10-2026 15.24.m4a")
    t0_start = time.time()

    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    prompt = load_initial_prompt()
    hotwords = load_hotwords()

    segments, info = model.transcribe(
        str(wav_path),
        language="es",
        vad_filter=True,
        beam_size=5,
        initial_prompt=prompt,
        hotwords=hotwords,
        condition_on_previous_text=False,
    )

    lines = [
        "# Reunion Almahue 2026-10-27 PM (Tarde) - Whisper large-v3 + lexico",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        "Modelo: faster-whisper `large-v3` cuda float16 + VAD",
        "Fuente: C:\\Users\\c\\Desktop\\27-10-2026 15.24.m4a (01:47:50, tarde)",
        "Normalizacion: tools/transcript-lexico (grafias chilenas y nombres del ERP).",
        "",
    ]

    log_lines = []
    count = 0
    for seg in segments:
        count += 1
        t0 = int(seg.start)
        hh, rem = divmod(t0, 3600)
        mm, ss = divmod(rem, 60)
        stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
        text = normalize_chilean_transcript((seg.text or "").strip())
        if not text:
            continue
        line = f"- [{stamp}] {text}"
        lines.append(line)
        log_lines.append(f"[{stamp}] {text}")

        if count % 30 == 0:
            print(f"[{stamp}] {text}", flush=True)

    full_transcript = "\n".join(lines) + "\n"

    # Guardar transcripciones
    out_whisper.parent.mkdir(parents=True, exist_ok=True)
    out_whisper.write_text(full_transcript, encoding="utf-8")
    out_transcripciones.parent.mkdir(parents=True, exist_ok=True)
    out_transcripciones.write_text(full_transcript, encoding="utf-8")

    if drive_transcripcion:
        try:
            drive_transcripcion.write_text(full_transcript, encoding="utf-8")
            print(f"- Guardado en Google Drive: {drive_transcripcion}")
        except Exception as e:
            print(f"Aviso guardado Drive: {e}")

    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    elapsed = time.time() - t0_start
    print(f"\nTranscripcion Whisper PM finalizada con exito en {elapsed:.1f}s ({elapsed/60:.1f} min)!")
    print(f"- Segmentos procesados: {count}")
    print(f"- Guardado en: {out_whisper}")
    print(f"- Guardado en: {out_transcripciones}")

if __name__ == "__main__":
    main()
