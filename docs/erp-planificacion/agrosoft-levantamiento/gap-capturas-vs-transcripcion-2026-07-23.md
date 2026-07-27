# Gap analysis: capturas ERP demo ↔ transcripciones Reu 1 / Reu 2

**Fecha:** 23/07/2026 (actualizado implementación gaps)  
**Capturas:** `capturas-validacion-erp/reu1/`, `reu2/`  
**Transcripciones:**
- Reu 1: `fuentes/transcripcion.md`
- Reu 2: `fuentes/transcripcion-reunion2.md` *(extraída del chat; no hace falta volver a pegarla)*

**Alcance:** contenido **mencionado en reunión** que **no se ve** (o se ve incompleto) en las capturas del ERP demo.  
No re-lista lo que ya está OK en `validacion-capturas-reu1-reu2-2026-07-23.md`.

---

## Veredicto corto

| Bloque | Resultado |
|---|---|
| Flujos mockeables Reu 1 + Reu 2 | Cubiertos en capturas (demo) |
| Gaps G1–G2 | Cerrados (capturas previas) |
| Gaps G3–G5, G7–G8 + R1-07 | **Implementados en demo 23/07** — regenerar capturas |
| G6 UX AgroSmart | PARCIAL diseño (no clon visual; OUT de scope) |

---

## A) Falta o parcial en capturas (sí se dijo en transcripción)

| # | Tema (cita / marca temporal) | Captura actual | Estado | Qué falta ver en demo |
|---|---|---|---|---|
| G1 | **Reversa selectiva de conciliación** — Reu2 ~07:43–07:50 | `reu2/09-conciliacion-movimientos.png` | **OK (cerrado)** | Modal Movimientos + botón Desconciliar por fila |
| G2 | **Confirmación borrador → definitiva (proforma)** — Reu2 ~01:56–02:04 | `reu2/02-proformas-confirm-definitiva.png` | **OK (cerrado)** | Modal resumen + «Sí, emitir definitiva» |
| G3 | **Nóminas de pago + atraso >90 días (tesorería)** — Reu2 ~09:11 | — (nueva ruta) | **OK demo** | `/tesoreria/nominas` — KPI + filtro >90 días; **capturar** |
| G4 | **Login: temporada + mes contable** — Reu1 ~00:40 | — | **OK demo** | Modal post-login + selector en header; **capturar** |
| G5 | **Alerta afecto/exento OC vs factura** — Reu2 ~11:58 | `reu1/10-registro-compra.png` | **OK demo** | Banner + toast + fila FAC-8809 inconsistente; **re-capturar** |
| G6 | **UX tipo AgroSmart (clon amigable)** — Reu2 ~02:50–04:17 | `reu2/03`, `04` | **PARCIAL (diseño)** | Flujos OK; no es clon visual del legado (fuera de scope) |
| G7 | **Contabilizar desde cartola** — Reu2 ~07:23 | `reu2/08-carga-cartola.png` | **OK demo** | Modal Movimientos + Contabilizar pendientes; **re-capturar** |
| G8 | **Cadena contable de reversa en ventas (IDs)** — Reu2 ~05:35 | `reu2/06-libro-comercial.png` | **OK demo** | Columna cadena Asi. 472/473/474; **re-capturar** |

---

## B) Menciones en transcripción que **sí** aparecen en capturas

| Tema | Transcripción | Evidencia captura |
|---|---|---|
| Precio editable en ingreso diario (sin tarifario rígido) | Reu2 ~01:45, ~03:03 AgroSmart | `03-ingreso-diario-form.png` — «Precio unitario editable» |
| Actividad filtrada por labor | Reu2 ~01:36 (dolor AgroSoft al revés) | Form ingreso + tarifas — label filtrado |
| N proformas → 1 factura / multi-mes | Reu2 ~02:26–02:40 | `02-proformas-n1.png` — periodo `2026-06/2026-07`, «Asociar factura» |
| Asociación labores → proforma/factura | Reu2 ~03:30–03:51 | `04-asociacion-labores.png` |
| Libro ventas: reutilizar datos al reversar; solo grabar y contabilizar | Reu2 ~04:39–05:46 | `06-libro-comercial.png` |
| Cartola Excel + mejora PDF; buscar/borrar | Reu2 ~06:43, ~07:35 | `08-carga-cartola.png` — FMT EXCEL/PDF, buscar, papelera |
| Anticipos con calce parcial | Reu2 ~08:06–08:20 | `10-anticipos.png` — PARCIAL / Calzar / saldo |
| TC bidireccional (CLP↔USD) | Reu2 ~08:32–08:53 | `07-pagos-tc-form.png` — monedas + dif. TC |
| Roles Digitador / Analista / Admin + matriz | Reu2 ~09:57 | `11-roles-matriz.png` |
| Sync Banco Central | demo Reu2 | `13` / `14` |
| Contacto encargado en CC | Reu2 / Mario | `12-centros-encargado.png` |
| GoSocket / WhatsApp indep. ERP (~01/09) | Reu2 ~12:03–12:07 | `15-gosocket-dec14.png` |
| OUT niveles almacenamiento | DEC-12 Reu2 | Sin pantalla (correcto) |

---

## C) Dicho en reunión pero **fuera de alcance demo** (no tratar como bug de captura)

| Tema | Por qué no es gap de captura |
|---|---|
| Flujo AgroSoft completo: contrato + enrolamiento + faena + folio | Decisión explícita: reemplazar por modelo tipo AgroSmart (ingreso diario) |
| Power BI / reportes malos de AgroSmart | Fuera del mock ERP; AlmaWeb / control de gestión |
| Bug sesión compartida (empresa ajena al re-login) | Comportamiento de sesión backend; no pantalla |
| Cambio Acepta → WhatsApp / GoSocket | Integración externa; banner DEC-14 basta en demo |
| Elementos de costo rígidos por área (Mario) | Mejora parametrización; no pantalla dedicada en set de capturas |
| Reunión martes planificación | Operativo, no producto |

---

## D) Prioridad sugerida (restantes)

1. **Regenerar capturas** G3, G4, G5, G7, G8 + R1-07 (distribución CC en form OC).  
2. **G6** — no clon visual AgroSmart (aceptado PARCIAL).  
3. **Backend N:1 proformas** — migración aditiva `20260723220000_proformas_n1_factura` + API `proformaIds[]` (demo ya tenía N:1).

---

## E) Nota sobre archivos de transcripción

- Reu 1 ya estaba en repo: `fuentes/transcripcion.md`  
- Reu 2 quedó materializada en: `fuentes/transcripcion-reunion2.md`  
No hace falta volver a pegar la Reu 2 en el chat salvo que quieras reemplazarla por una versión limpia (TLDV export, etc.).
