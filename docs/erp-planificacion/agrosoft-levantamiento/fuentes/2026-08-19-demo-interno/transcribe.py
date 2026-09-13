from faster_whisper import WhisperModel

audio = r"E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento\fuentes\2026-08-19-demo-interno\audio.wav"
out = r"E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento\fuentes\transcripcion-2026-08-19-demo-interno.md"

model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio, language="es", vad_filter=True)
lines = [
    "# Transcripción bruta (Whisper local small, ES)",
    "",
    f"Idioma detectado: {info.language} (p={info.language_probability:.2f})",
    "Fuente: Screen Recording 2026-08-19 162555.mp4 (~11:47)",
    "No es fuente de requisitos. Limpieza posterior con Ollama.",
    "",
]
for seg in segments:
    t0 = int(seg.start)
    mm, ss = divmod(t0, 60)
    lines.append(f"- [{mm:02d}:{ss:02d}] {seg.text.strip()}")
    print(f"[{mm:02d}:{ss:02d}] {seg.text.strip()}", flush=True)

text = "\n".join(lines) + "\n"
with open(out, "w", encoding="utf-8") as f:
    f.write(text)
print("WROTE", out, "chars", len(text))
