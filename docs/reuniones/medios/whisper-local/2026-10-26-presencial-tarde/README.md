# Audio tarde 26/10/2026

Fuente original rota: `C:\Users\c\Desktop\26-10-2026 15.20.m4a` (~109 MB, sin `moov`).

**Reparado 27/10** con [untrunc](https://github.com/anthwlock/untrunc) usando referencia `26-10-2026 12.33.m4a` (mismo celular):

| Archivo | Duracion ffmpeg | Notas |
|---|---|---|
| `26-10-2026-15-20-repaired.m4a` (esta carpeta) | ~01:53:49 | Escuchar antes de confiar; untrunc puede estirar duracion vs real |
| `C:\Users\c\Desktop\26-10-2026 15.20 REPARADO.m4a` | copia para el usuario |

Si suena acelerado/lento, reintentar: `untrunc.exe -sv referencia.m4a roto.m4a`

**Problema original:** el contenedor MP4/M4A no tenia atom `moov` (grabacion no finalizada o copia interrumpida). `ffmpeg` respondia `moov atom not found`.

**Que hacer en el celular:**

1. Abrir la nota de voz en la app de grabacion y dejar que termine de procesar.
2. Volver a copiar el archivo al PC (USB o Drive), o exportar/compartir desde la app.
3. Verificar con `ffmpeg -i archivo.m4a` que muestre `Duration` sin error.

Cuando exista un archivo valido, transcribir con:

```powershell
cd E:\source\repos\Almahue
# wav
& C:\OctoPrint\ffmpeg.exe -y -i "C:\Users\c\Desktop\26-10-2026 15.20.m4a" -vn -ac 1 -ar 16000 -c:a pcm_s16le docs\reuniones\medios\whisper-local\2026-10-26-presencial-tarde\audio.wav
# whisper
& C:\Users\c\AppData\Local\Programs\Python\Python312\python.exe tools\transcript-whisper\transcribe_one.py --audio docs\reuniones\medios\whisper-local\2026-10-26-presencial-tarde\audio.wav --out docs\reuniones\transcripciones\transcripcion-2026-10-26-presencial-tarde.md --title "Reunion presencial Almahue 2026-10-26 tarde" --source "26-10-2026 15.20.m4a" --model large-v3 --device cuda --compute-type float16
```
