# Contraste Reu5 — Whisper local vs tl;dv (03/08/2026)

**Video:** `fuentes/videos/reunion5-2026-08-03.mp4` (~42:32)  
**Whisper:** `whisper-local/reu5/transcripcion-whisper.md` (~38k chars, reloj 00:02→42:31)  
**tl;dv largo:** `transcripcion-reunion5.md` (~32k chars, con speakers)  
**Minuta tl;dv:** `reunion5-minuta-tldv-2026-08-03.md`  
**Canónica producto:** `reunion5-minuta-2026-08-03.md`

---

## Cobertura

| Señal | Whisper | tl;dv |
|---|---|---|
| Longitud | Más denso (segmentos cortos) | Turnos por speaker |
| Reloj | Alineado al MP4 de punta a punta | Pegado tl;dv; puede desfasar (como Reu4) |
| Diarización | No (todo corrido) | Speaker 00≈Carlos, 01≈Sergio |
| Temas clave (conteo aprox.) | PIN 27, aprob 28, periodo 20, borrador 29, cotiz 7, cartola 1, GoSocket 2 | Muy similar |

**Veredicto cobertura:** ambos cubren el mismo arco (~42 min). Whisper no “perdió” la reunión; tl;dv es más legible por turnos.

---

## Decisiones / temas (ambos)

Aparecen en **Whisper y tl;dv** (y en la minuta tl;dv):

- Aprobaciones con **PIN por usuario** (no un PIN global); demo con rol ejemplo / demo123.
- Confirmación / seguridad al cambiar PIN (correo / clave de cuenta) — pedido en sala.
- OC: centro de costo por ítem.
- Emisión: pantalla redimensionable; panel lateral de resumen.
- Libro de compras: totalizados.
- Filtros / estética de libros; menú de acciones tipo Better Software (tl;dv nombra “Better”; Whisper puede haberlo deformado).
- Periodos: paginación; limitar vista; historial apertura/cierre; motivo al reabrir.
- Cotizaciones: folio clickeable; borradores admin con filtro usuario.
- Estado de cuenta: factura 88001; tipo de movimiento.
- Cartolas bancarias (mencionado al cierre).
- Quedan para el día siguiente ajustes.

---

## Solo tl;dv / solo Whisper (cuidado)

| Hallazgo | Lectura |
|---|---|
| Minuta tl;dv atribuye casi todo a “Sergio implementar…” | **Sesgo tl;dv.** La nota del propio archivo y la minuta canónica: **Carlos** implementa; Sergio pide/valida. |
| Whisper sin speakers | No usar Whisper para atribuir “quién dijo”. |
| ASR (“Shibuya”, “Vacancito”, etc. al cierre) | Ruido; ignorar. |
| “Better Software” | Claro en tl;dv/minuta; Whisper puede no literalizar la marca. |

---

## Reloj

Whisper arranca ~00:02 y cierra ~42:31 ≈ duración del MP4. Preferir **timestamps Whisper** si hay duda con el player. tl;dv sirve para el texto por speaker.

---

## Veredicto Reu5

| Para… | Usar |
|---|---|
| Quién habló / action items “quién” | Minuta canónica + tl;dv speakers (corregido) |
| Minuto exacto en el video | Whisper local |
| Requisitos de producto | Minuta canónica Reu5 / Reu6 si aplica; **no** ASR crudo |

No hay divergencia de negocio grave entre ambas transcripciones en esta reunión: el riesgo real es la **atribución errónea a Sergio** en la minuta tl;dv automática.
