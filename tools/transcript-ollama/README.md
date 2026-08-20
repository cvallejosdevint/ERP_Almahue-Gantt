# Transcripciones locales (Ollama)

Depura `docs/erp-planificacion/agrosoft-levantamiento/fuentes/transcripcion*.md` **sin APIs de pago**.

## Requisitos

- `E:\Ollama\ollama.exe` (o `ollama` en PATH)
- Modelos en `E:\OllamaModels` (`OLLAMA_MODELS`)
- Modelo por defecto: `qwen2.5-coder:14b` (el que ya está en la máquina)

v1 **no** transcribe video: usa los `.md` ya extraídos. Whisper local es opcional futuro.

**Importante:** no uses `ollama run` redirigido en PowerShell (captura el spinner TTY). El script llama `POST http://127.0.0.1:11434/api/generate`.

## Uso

```powershell
$env:OLLAMA_MODELS = 'E:\OllamaModels'
cd E:\source\repos\Almahue\tools\transcript-ollama
.\run-clean.ps1
```

Salida: `out/reunionN-limpia.md` (gitignored). Consolidar a `docs/transcripcion-limpia-v2.md` en Fase 1.

Skill Cursor: `.cursor/skills/almahue-transcript-local/SKILL.md`
