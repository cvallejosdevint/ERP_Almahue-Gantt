# Acuerdos definitivos — 10/09/2026

Fuente primaria: transcripciones `fuentes/`. Minutas tl;dv = índice. Cliente en sala = requisito. Carlos/Sergio = hipótesis. Reu5 **no cuenta**. Reloj Reu1–Reu5: marca ÷10.

Este archivo **no borra** acuerdos viejos: cada reunión queda intacta; la columna «Vigente» dice si un acuerdo posterior lo pisó.

Documento hermano visual: canvas `acuerdos-reuniones-almahue.canvas.tsx`.

---

## Cómo se lee

| Capa | Qué es |
|---|---|
| **Intacta** | Lo dicho ese día, con hablante |
| **Piso** | Un acuerdo posterior que cambia el alcance |
| **Definitivo** | Texto vigente **hoy** (cliente + ratificación dueño 03/09) |
| **Estado código** | CUMPLE / PARCIAL / PENDIENTE / CORTADO |

Cadena de autoridad: transcripción cliente > Reu6 > Reu4 > Reu3 > Reu1–2 (as-is). Lupe/Mario **no** pisan Reu6 **salvo** ratificación del usuario (03/09: D4 solo OC y D11 cotiz suprimida).

---

## Reuniones por fecha (ERP)

| Fecha | Id | Cliente | Valor req. | Transcripción |
|---|---|---|---|---|
| 21/07 | Reu1 | MJ, Rodrigo | Alto · as-is Agrosoft | `transcripcion.md` (reloj ×10) |
| 23/07 | Reu2 | MJ, Rodrigo | Alto · as-is | `transcripcion-reunion2.md` |
| 28/07 | Reu3 | MJ | Medio-alto | `transcripcion-reunion3.md` |
| 30/07 | Reu4 | MJ | Medio (sin gerencia) | `transcripcion-reunion4.md` |
| 03/08 | Reu5 | **nadie** | **Nulo** | `transcripcion-reunion5.md` |
| 04–05/08 | GoSocket | Pablo + MJ | Técnico emisión | minuta + QA |
| 06/08 | Reu6 | MJ, Agustín | Alto | `transcripcion-reunion6.md` (reloj real) |
| 19/08 | Demo interno | nadie | Nulo | `transcripcion-2026-08-19-demo-interno.md` |
| 20/08 AM | Sergio | nadie | Nulo | `transcripcion-2026-08-20-reunion-sergio.md` |
| 20/08 PM | Lupe, Mario | Alto operativo compras/teso | `transcripcion-2026-08-20-tarde-lupe-mario.md` |
| 28/08 | Tesorería | MJ, Lupe, Fran, Mario | Alto tesorería | `transcripcion-2026-08-28-tesoreria-mj-lupe.md` |
| 01/09 | Kickoff GS | Pablo (sin MJ) | Técnico | minuta kickoff |
| 03/09 | Interna + **R dueño** | — | Cortes D4/D11 | transcripción interna + AGENTS |
| 07/09 | Interna | nadie | Hipótesis NC/cuentas | `transcripcion-2026-09-07-interna-carlos-sergio.md` |
| 08/09 | MJ + GoSocket | MJ, Pablo | Alto ventas locales | tl;dv 6aa022cc… |

---

## Pisos (quién gana)

| Tema | Antes | Quién pisa | Definitivo hoy |
|---|---|---|---|
| Aprobaciones OV / Comercial | Reu6 D4 minuta: OC+proformas+comercial (en sala: cadena **OC**; Comercial = Carlos) | 20/08 Lupe/Mario (pregunta cerrada) **no pisa** solo; **usuario 03/09 sí** | **Solo OC**. OV: Guardar → `CONFIRMADA`. Sin bandeja ventas |
| Proformas con PIN | Reu3 MJ + Reu4 | Código 21/08 + R 03/09; **0 menciones** 19–20/08 | **Cortado**: BORRADOR→DEFINITIVA con `contratistas:write` |
| Cotización | Reu6 MJ: **mover a Compras** | Lupe 20/08 «solo OC» + R 03/09 | **Suprimida** como documento; ref. opcional en OC |
| Cuenta / CC en venta | Reu4: imputar al emitir | MJ 08/09 + diseño 03/09 | **Solo al contabilizar**, CC **por ítem** |
| Flujo caja eje | Lupe 20/08: por banco | MJ 28/08: por **moneda** | Por moneda |
| GoSocket | Reu2 MJ: **libro compras en línea** | Llamadas ago: onboarding **emisión** | Ambos: emisión vía gateway **sí**; recepción compras **pendiente** |
| «Guardar» en libro ventas | Reu2: no ensuciar libro | Reu4 + P0-4 | Borradores en **Emitir**, no en Libro |
| Config SII | Reu4 conservar tibio | Minuta Reu5 lo ata a GoSocket (**falso**) | Panel ERP interno; GoSocket no lo usa |

Reu5 **no pisa nada**. Cotiz→NP→factura de Reu5 **no entra**.

---

## Acuerdo definitivo (texto vigente)

### Ventas / DTE

1. Las ventas parten de **orden de venta**. Stock al **confirmar**. Factura electrónica = DTE desde OV confirmada (Emitir).
2. Libro de ventas = DTE emitidos. `EMITIDO` = por contabilizar (cuenta + CC por ítem). Contabilizar **no** re-emite.
3. NC CodRef 1/2/3 amarrada a factura origen; confirmación al emitir; correcciones **no** mueven bodega (Almahue fruta). Reintegro bodega = **solo ALM**.
4. D16: no vender bajo **precio de compra** del maestro (fallback `costoPromedio` si el maestro no tiene compra).
5. Flete = línea adicional (`tipoLinea` FLETE).
6. Exportación DTE: spool nacional + campos; códigos aduana; país recepción. **Pendiente** set con Pablo/MJ.
7. Historial factura ↔ NC/ND en Libro.

### Compras / aprobaciones

8. Sin solicitud de compra: arranque = **OC**. Cadena PIN **solo OC**. Factura a OC no aprobada: destacar; no contabilizar ni pagar hasta `APROBADO`.
9. Cotización: no hay CRUD (corte 03/09). Referencia tipo/folio/fecha en OC.
10. Libro compras: asociar OC por RUT; carga masiva con dedup (pedido Reu3; CSV actual es parcial).

### Tesorería (28/08 manda sobre 20/08 en eje de flujo)

11. Cartola import → asiento `CARTOLA:{id}`; conciliar/contabilizar 1:1. Pago/cobro = calce + CC; **sin** asiento `PAGO:{id}`.
12. Flujo caja lectura, filtro **moneda**. Triple moneda CLP/USD/yuan en **toda** contabilización (pedido MJ).
13. Nómina = semana de compromiso; no muta DTE.
14. Estado de cuenta por RUT.

### Contratistas

15. N proformas → 1 factura; labores diarias. **Sin** bandeja PIN (cortado). Cierre mes + TC + centralización.

### GoSocket

16. Emisión API (CAF/cert Almahue; XML/folio partner). Contabilización = solo ERP.
17. Objetivo cliente Reu2 (**recepción → libro compras**) **sigue pendiente**.

---

## Estado en código (10/09)

| Definitivo | Código |
|---|---|
| OV → stock → Emitir → Libro CC/cuenta por ítem | CUMPLE (QA 09/09: contabilizar FA-1013 sin re-emitir) |
| Sin cuenta/CC en Emitir | CUMPLE |
| Confirmación NC | CUMPLE (CodRef 2 UI; 3 misma rama) |
| Historial NC/ND | CUMPLE |
| Aprobaciones solo OC / cotiz suprimida | CORTADO_RATIFICADO |
| D16 precio compra | CUMPLE (D16 no ejercitado en QA) |
| Cartola import + pago sin `PAGO:` | CUMPLE |
| Mantenedor CC | CUMPLE (`/catalogos/centros-costo`) |
| Triple moneda / mayor | PENDIENTE |
| GoSocket libro compras recepción | PENDIENTE |
| Exportación set pruebas | PENDIENTE |
| Reversa contable en UI Libro | PARCIAL (API sí, botón no) |
| Factura `ANULADO` + ocultar Anular post CodRef 1 | PARCIAL |
| Reintegro ALM | PARCIAL (`DEVOLUCION_NC`; no sociedad-específico) |
| Guía logística / traslado bodega | PARCIAL |
| SMTP | PENDIENTE |
| Carga Excel SII + dedup solape | PARCIAL (CSV/folio) |
| Reversa 472/473/474 reutilizable | PARCIAL / hueco UX |

---

## Transcripción: español de Chile (sin APIs de pago)

tl;dv es español neutro y **no es requisito**. Pipeline local ya existe:

1. `ffmpeg` → WAV 16 kHz mono (`tools/transcript-whisper/batch-reu.ps1`)
2. `faster-whisper` `es` + VAD + **`initial_prompt` léxico chileno/ERP** (`transcribe_one.py`)
3. Limpieza Ollama `qwen2.5-coder:14b` + `tools/transcript-ollama/prompts/system-es-cl.md`
4. Contrastar vs transcripción cliente; Whisper para reloj del MP4

Huecos: Reu6 Whisper apuntaba al MP4 **11:00** (otro Meet). Mapeo corregido a **17:07**. Limpieza Ollama del lote Reu1–6 **pendiente**. Reu1–5 tl;dv: reloj ×10. Whisper **no diariza**.

No re-transcribir el lote ahora (horas de CPU). Corrida puntual: `.\batch-reu.ps1 -Reu 6` cuando el WAV de 17:07 esté extraído.

---

## Intactos que nadie pisó (siguen pidiendo trabajo)

- R2-13 recepción GoSocket → libro compras
- R2-05 reversa reutilizable en UI
- R3-06 dedup carga SII por solape
- A28-04 triple moneda
- A08g-05 exportación + RG Pablo
- A08g-06 bodega ALM
- R1-06 NC compra al precio de factura origen (patrón inventario)
