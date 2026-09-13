# Whisper local — reuniones Almahue (vs tl;dv)

No usa APIs de pago. ASR = `faster-whisper` (CPU). Limpieza = Ollama `qwen2.5-coder:14b` + prompt ES-CL.

## Mapa

| Reu | Video | Transcripción tl;dv (ya en repo) | Minuta tl;dv | Whisper local (salida) |
|---|---|---|---|---|
| 1 | `videos/reunion1-2026-07-21.mp4` (~1h56) | `transcripcion.md` | — | `whisper-local/reu1/` |
| 2 | `videos/reunion2-2026-07-23.mp4` (~1h21) | `transcripcion-reunion2.md` | `reunion2-minuta-tldv-…` | `whisper-local/reu2/` |
| 3 | `videos/reunion3-2026-07-28.mp4` (~58m) | `transcripcion-reunion3.md` | `reunion3-minuta-tldv-…` | `whisper-local/reu3/` |
| 4 | `videos/reunion4-2026-07-30.mp4` (~1h34) | `transcripcion-reunion4.md` | `reunion4-minuta-tldv-…` | `whisper-local/reu4/` |
| 5 | `videos/reunion5-2026-08-03.mp4` (~43m) | `transcripcion-reunion5.md` | `reunion5-minuta-tldv-…` | `whisper-local/reu5/` |
| 10/09 interna | `Screen Recording 2026-09-10 102149.mp4` | — | — | `whisper-local/sergio-2026-09-10/` |

Audio/WAV y frames: **gitignored** (pesados). Solo `.md` de ASR y contrastes van a git.

## Orden de corrida

Más corto primero: **5 → 3 → 2 → 4 → 1 → 6**.

## Cómo

```powershell
cd E:\source\repos\Almahue\tools\transcript-whisper
.\batch-reu.ps1 -Reu 5          # una
.\batch-reu.ps1 -Reu 5,3,2      # varias
.\batch-reu.ps1 -All            # todas las de videos/
```
