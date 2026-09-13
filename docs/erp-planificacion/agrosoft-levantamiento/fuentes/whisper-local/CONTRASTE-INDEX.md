# Contraste ASR local (Whisper) vs tl;dv — reuniones Almahue

**Objetivo:** comparar lo que ya tenemos pegado de **tl;dv** con una transcripción **local** (faster-whisper + limpieza ES-CL), sin APIs de pago.  
**Regla:** ni tl;dv ni Whisper son requisitos. Gana **minuta MJ/Agustín** (Reu6 > Reu5 > Reu4) + código.

**Pipeline:** `tools/transcript-whisper/batch-reu.ps1` → `fuentes/whisper-local/reuN/transcripcion-whisper.md`  
**Estado corrida:** ver checklist abajo (se actualiza al cerrar cada reu).

---

## Checklist

| Reu | Video | Whisper | Limpieza Ollama | Contraste vs tl;dv |
|---|---|---|---|---|
| 5 | `videos/reunion5-…` (~43m) | ✅ | pend. (opcional) | ✅ `contraste-reu5-whisper-vs-tldv.md` |
| 3 | `videos/reunion3-…` (~58m) | ✅ | pend. (opcional) | ✅ `contraste-reu3-whisper-vs-tldv.md` |
| 2 | `videos/reunion2-…` (~81m) | ✅ | pend. | ✅ `contraste-reu2-whisper-vs-tldv.md` |
| 4 | `videos/reunion4-…` (~94m) | ✅ | pend. | ✅ `contraste-reu4-whisper-vs-tldv.md` |
| 1 | `videos/reunion1-…` (~116m) | ✅ | pend. | ✅ `contraste-reu1-whisper-vs-tldv.md` |
| 6 | Screen Rec. 2026-08-06 11:00 (~59m) | ✅ (audio **sospechoso**) | pend. | ⚠️ `contraste-reu6-whisper-vs-tldv.md` — **MP4 equivocado** |

ETA orientativa CPU `small`: ~0,5–0,7× duración del audio (el lote completo puede llevar **varias horas**).

---

## Método de contraste (por reunión)

Para cada reu, el archivo `contraste-reuN-whisper-vs-tldv.md` responde:

1. **Cobertura:** ¿Whisper perdió tramos que tl;dv sí tiene (o al revés)?
2. **Reloj:** ¿timestamps alineados al MP4? (Reu4 ya tenía desfase tl;dv documentado −5:51)
3. **Speakers:** tl;dv etiqueta Speaker 00/01/…; Whisper no diariza → riesgo de mezclar voces
4. **Decisiones de negocio:** lista A/B  
   - A = aparece en ambos  
   - B = solo tl;dv / solo Whisper → validar con minuta canónica
5. **Falsos amigos ASR:** GoSocket, SII, CAF, PIN, cotización, OC, OV, AlmaWeb, etc.
6. **Veredicto:** qué usar para planificar (casi siempre: **minuta** > contraste > ASR crudo)

---

## Hallazgos globales (se llena al avanzar)

- **Reu5:** cobertura Whisper ≈ tl;dv; Whisper mejor para reloj del MP4; tl;dv mejor para speakers. Minuta tl;dv atribuye mal action items a Sergio (ya documentado).
- **Reu3:** cobertura similar; Whisper **pierde** el literal «GoSocket» (ASR). Usar tl;dv/minuta para partner DTE.
- **Reu2:** cobertura similar; Whisper pierde «GoSocket» y escribe «pro forma» vs «proforma» de tl;dv. Foco: contratistas / tarifario / Agrosmart.
- **Reu4:** cobertura OK; Whisper sí captura algunas menciones GoSocket.
- **Reu1:** cobertura OK (reunión temprana).
- **Reu6:** ⚠️ el Screen Recording mapeado **no es** la reunión ERP (sellers/Walmart). Usar minuta Reu6 + tl;dv; corregir `batch-reu.ps1` Video path.

---

## Archivos tl;dv de referencia

| Reu | Transcripción larga | Minuta tl;dv |
|---|---|---|
| 1 | `fuentes/transcripcion.md` | — |
| 2 | `fuentes/transcripcion-reunion2.md` | `reunion2-minuta-tldv-2026-07-23.md` |
| 3 | `fuentes/transcripcion-reunion3.md` | `reunion3-minuta-tldv-2026-07-28.md` |
| 4 | `fuentes/transcripcion-reunion4.md` | `reunion4-minuta-tldv-2026-07-30.md` |
| 5 | `fuentes/transcripcion-reunion5.md` | `reunion5-minuta-tldv-2026-08-03.md` |
| 6 | `fuentes/transcripcion-reunion6.md` | — (canónica: `reunion6-minuta-2026-08-06.md`) |
