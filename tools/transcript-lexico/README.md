# Lexico chileno para transcripciones

Dos capas. Whisper no puede cargar un diccionario entero en el prompt (recorta cerca de 224 tokens).

1. **Prompt** (`initial-prompt.txt`): nombres del ERP y unos modismos, para que el modelo no parta `cachái` ni `GoSocket`.
2. **Post-proceso** (`normalization.json` + `normalize.py`): unifica grafias que el ASR ya dejo mal. Lo llaman `transcribe_one.py` y `transcribe_batch_v3.py` al escribir el markdown.

La lista de Wiktionary no se aplica sola. Hay mas de mil lemas y muchos son palabras normales (`papa`, `mina`, `once`). Sustituirlas en una reunion de ERP cambiaria frases que estaban bien.

## Comandos

```powershell
cd E:\source\repos\Almahue\tools\transcript-lexico
python normalize.py
python scan.py
python fetch_wiktionary.py
```

`scan.py` solo informa coincidencias en `docs/reuniones/transcripciones/`. No reescribe esos archivos: son la cita de las reuniones.

`fetch_wiktionary.py` guarda `data/chilenismos-wiktionary.json`. Wikimedia pide un User-Agent; el script ya lo manda.
