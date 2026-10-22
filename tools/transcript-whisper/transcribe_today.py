"""Transcribe la reunion de hoy (22/10/2026) con faster-whisper large-v3 en CUDA float16,
aplica normalizacion de lexico chileno y luego genera la minuta/depuracion de negocio con Ollama.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
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
    wav_path = _REPO / "docs" / "reuniones" / "medios" / "whisper-local" / "2026-10-22-reunion" / "audio.wav"
    out_whisper = _REPO / "docs" / "reuniones" / "medios" / "whisper-local" / "2026-10-22-reunion" / "transcripcion-whisper.md"
    out_transcripciones = _REPO / "docs" / "reuniones" / "transcripciones" / "transcripcion-2026-10-22-reunion-cliente.md"
    
    drive_dir = Path(r"G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 14 - 2026-10-19 a 2026-10-25\2026-10-22 Reunion cliente - Tesoreria y Contabilidad")
    drive_dir.mkdir(parents=True, exist_ok=True)
    drive_transcripcion = drive_dir / "transcripcion.md"
    drive_minuta = drive_dir / "minuta.md"
    drive_limpia = drive_dir / "transcripcion-limpia-ollama.md"
    
    repo_minuta = _REPO / "docs" / "reuniones" / "minutas" / "reunion-2026-10-22-cliente.md"
    repo_minuta.parent.mkdir(parents=True, exist_ok=True)

    print(f"Iniciando transcripcion Whisper large-v3 en CUDA float16...")
    print(f"Audio: {wav_path}")
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
        "# Reunion cliente Almahue 2026-10-22 (Whisper large-v3 + lexico)",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        "Modelo: faster-whisper `large-v3` cuda float16 + VAD",
        "Fuente: Recording 2026-10-22 193116.mp4 (01:21:14)",
        "Normalizacion: tools/transcript-lexico (grafias chilenas y nombres del ERP).",
        "Minuta: docs/reuniones/minutas/reunion-2026-10-22-cliente.md",
        "",
    ]

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
        if count % 20 == 0:
            print(f"[{stamp}] {text}", flush=True)

    full_transcript = "\n".join(lines) + "\n"

    # Guardar transcripciones
    out_whisper.write_text(full_transcript, encoding="utf-8")
    out_transcripciones.write_text(full_transcript, encoding="utf-8")
    drive_transcripcion.write_text(full_transcript, encoding="utf-8")
    
    elapsed = time.time() - t0_start
    print(f"\nTranscripcion Whisper finalizada con exito en {elapsed:.1f}s ({elapsed/60:.1f} min)!")
    print(f"- Guardado en: {out_whisper}")
    print(f"- Guardado en: {out_transcripciones}")
    print(f"- Guardado en Drive: {drive_transcripcion}")

    # Descargar modelo de VRAM para dejar espacio completo a Ollama
    del model
    time.sleep(2)

    # Paso 2: Ejecutar Ollama para generar minuta y depuración de negocio
    print("\nIniciando depuracion y minuta con Ollama (qwen2.5-coder:14b)...")
    prompt_file = _REPO / "tools" / "transcript-ollama" / "prompts" / "system-es-cl.md"
    system_prompt = prompt_file.read_text(encoding="utf-8")

    user_prompt = f"""{system_prompt}

A continuacion tienes la transcripcion de la reunion de hoy 22/10/2026 con el cliente Almahue (Tesoreria y Contabilidad):

---
{full_transcript}
---

Instrucciones:
1. Genera una Minuta técnica y ejecutiva completa en Markdown para `docs/reuniones/minutas/reunion-2026-10-22-cliente.md`.
2. Estructura:
   - Encabezado: Fecha, participantes (MJ, Lupe, Fran, Mario si estuvieron, Carlos de Devint), tema principal (Tesorería y Contabilidad).
   - Requerimientos explícitos del cliente (con [MM:SS]).
   - Definiciones y acuerdos contables / tesorería (cartolas, conciliación, pagos, nóminas, tipos de cambio, asientos).
   - Hipótesis u opiniones de Devint (Carlos).
   - Tareas y compromisos acordados para el próximo hito.
3. Prohibido hablar de mermas.
"""

    payload = {
        "model": "qwen2.5-coder:14b",
        "prompt": user_prompt,
        "stream": False,
        "options": {
            "num_ctx": 32768,
            "temperature": 0.2
        }
    }

    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            "http://127.0.0.1:11434/api/generate",
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=900) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            minuta_text = res.get("response", "")

        repo_minuta.write_text(minuta_text, encoding="utf-8")
        drive_minuta.write_text(minuta_text, encoding="utf-8")
        drive_limpia.write_text(minuta_text, encoding="utf-8")
        print(f"Minuta Ollama guardada en repo: {repo_minuta}")
        print(f"Minuta Ollama guardada en Drive: {drive_minuta}")
    except Exception as e:
        print(f"Error generando minuta con Ollama: {e}")

    print("\nProceso completo finalizado exitosamente!")

if __name__ == "__main__":
    main()
