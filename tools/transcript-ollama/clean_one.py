"""Limpia la transcripcion de una reunion con Ollama local (qwen2.5-coder:14b) y prompt en espanol de Chile."""
import json
import os
import sys
import urllib.request
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[2]
    prompt_file = root / "tools" / "transcript-ollama" / "prompts" / "system-es-cl.md"
    transcripcion_file = root / "docs" / "reuniones" / "transcripciones" / "transcripcion-2026-10-21-reunion-cliente.md"
    out_dir = root / "tools" / "transcript-ollama" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "transcripcion-2026-10-21-reunion-cliente-limpia.md"
    
    drive_dir = Path(r"G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 14 - 2026-10-19 a 2026-10-25\2026-10-21 Reunion cliente - MJ, Fran y Lupe")

    system_prompt = prompt_file.read_text(encoding="utf-8")
    raw_text = transcripcion_file.read_text(encoding="utf-8")

    user_prompt = f"""{system_prompt}

A continuacion tienes la transcripcion cruda de la reunion del 21/10/2026 con el cliente Almahue (MJ, Fran, Lupe y Carlos de Devint):

---
{raw_text}
---

Instrucciones:
1. Devuelve un documento Markdown estructurado con los temas tratados, decisiones de negocio acordadas, requerimientos explicitos del cliente (MJ / Lupe / Fran), hipotesis de Devint (Carlos) y tareas pendientes.
2. Mantén las referencias de tiempo [MM:SS] de los hitos clave.
3. Prohibido hablar de mermas (no aplica en Almahue).
4. Destaca los acuerdos sobre: Guías manuales y adjuntos Acepta, Órdenes Madre/Hija al 100% y cierre de bodega, Activo fijo (alta desde factura de compras, vida útil en meses, IPC mensual), Contratistas y asignación de usuarios reales.
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

    print("Enviando prompt a Ollama (qwen2.5-coder:14b) con 32k context...")
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req, timeout=900) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        clean_text = res.get("response", "")

    # Guardar en out local
    out_file.write_text(clean_text, encoding="utf-8")
    print(f"Guardado localmente en: {out_file}")

    # Guardar en docs/reuniones/transcripciones
    repo_copy = root / "docs" / "reuniones" / "transcripciones" / "transcripcion-2026-10-21-reunion-cliente-limpia.md"
    repo_copy.write_text(clean_text, encoding="utf-8")
    print(f"Guardado en repo: {repo_copy}")

    # Guardar en G: (Drive)
    if drive_dir.exists():
        drive_copy = drive_dir / "transcripcion-limpia-ollama.md"
        drive_copy.write_text(clean_text, encoding="utf-8")
        print(f"Copiado a Google Drive: {drive_copy}")
    else:
        print(f"Aviso: Ruta de Google Drive no encontrada: {drive_dir}")

if __name__ == "__main__":
    main()
