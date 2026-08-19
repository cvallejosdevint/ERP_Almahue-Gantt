---
name: almahue-transcript-local
description: Depura transcripciones de reuniones Almahue con Ollama local (español de Chile). Use when cleaning fuentes/transcripcion*.md, extracting decisions, or avoiding paid transcription APIs.
---

# Transcripciones locales

No uses APIs de pago (tl;dv, OpenAI, etc.) para limpiar transcripciones.

## Cómo

1. Runtime: `E:\Ollama\ollama.exe`, modelos `E:\OllamaModels`.
2. Ejecutar [`tools/transcript-ollama/run-clean.ps1`](../../../tools/transcript-ollama/run-clean.ps1).
3. Prompt: [`tools/transcript-ollama/prompts/system-es-cl.md`](../../../tools/transcript-ollama/prompts/system-es-cl.md).
4. Consolidar salida `tools/transcript-ollama/out/` → `docs/transcripcion-limpia-v2.md`.

## Reglas de contenido

- Filtrar modismos; extraer valor de negocio.
- Carlos/Sergio en demo = hipótesis. Requisitos = Agustín / MJ + minutas (Reu6 > Reu5 > Reu4).
- **Prohibido** el concepto de mermas (no existe en el negocio).
- Cotización Compras → OC. OV Ventas → stock → factura.

v1 lee `.md` existentes; no transcribe `.mp4` (Whisper local = futuro).
