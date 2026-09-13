from faster_whisper import WhisperModel

AUDIO = r"E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento\fuentes\whisper-local\demo-2026-09-10\audio.wav"
OUT = r"E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento\fuentes\whisper-local\demo-2026-09-10\transcripcion-whisper.md"

model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=8)
segments, info = model.transcribe(
    AUDIO,
    language="es",
    beam_size=5,
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=700),
)

header = (
    "# Demo cliente 2026-09-10 (Whisper local)\n\n"
    f"Idioma: {info.language} (p={info.language_probability:.2f})\n"
    "Modelo: faster-whisper `small` CPU int8 + VAD\n"
    "Fuente: Screen Recording 2026-09-10 171320.mp4 (~01:14:14)\n"
    "Copia: fuentes/videos/reunion-2026-09-10-demo-cliente.mp4 (gitignored)\n\n"
)

print(f"duracion {info.duration:.0f}s", flush=True)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(header)
    for s in segments:
        m, sec = divmod(int(s.start), 60)
        line = f"- [{m:02d}:{sec:02d}] {s.text.strip()}"
        f.write(line + "\n")
        f.flush()
        print(line, flush=True)
