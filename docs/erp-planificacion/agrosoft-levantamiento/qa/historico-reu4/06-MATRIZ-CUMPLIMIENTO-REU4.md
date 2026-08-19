> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: minuta Reu6 + [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; D11/OV/grupos no eran el modelo vigente.

# Matriz de cumplimiento Reu4 — minuta + transcripción vs producto

**Fecha validación:** 31/07/2026  
**Entorno:** MODO REAL · `http://127.0.0.1:5174` → Nest `:3001` · Postgres `:5433`  
**Fuentes:** [`reunion4-minuta-2026-07-30.md`](../../docs/erp-planificacion/agrosoft-levantamiento/reunion4-minuta-2026-07-30.md) · [`transcripcion-reunion4.md`](../../docs/erp-planificacion/agrosoft-levantamiento/fuentes/transcripcion-reunion4.md)  
**Capturas:** [`capturas-cumplimiento/`](./capturas-cumplimiento/)

Leyenda: **Cumple** · **Parcial** · **Pendiente** · **Diferido** · **Propuesta** (sin código)

---

## 1. Decisiones de producto (D1–D17)

| # | Decisión (minuta) | Evidencia transcripción | Estado | Evidencia UI / código |
|---|---|---|---|---|
| D1 | CC por empresa; sin columna empresa | MJ [01:20:30]; Sergio [01:26:21]–[01:44:11] | **Cumple** | `CentrosCostoPage` columnas Código/Nombre/Encargado/Desde/Estado. Captura `R4-03-centros-costo.png` |
| D2 | Proforma aprobada: sin edit; solo asociar factura; reversa con clave | MJ [02:42:20] | **Cumple** | `canEditRow` solo `BORRADOR`; DEFINITIVA → Asociar + Reversar. `R4-04-proformas.png` |
| D3 | Clave de reversa **por usuario** | MJ [02:42:20] | **Cumple** | Modal pide clave personal (Mi Perfil); API `reversarProforma` |
| D4 | OC a factura solo aprobadas + recepcionadas | Sergio [03:35:41]; MJ [03:32:20] | **Cumple** | Filtro `RECEPCIONADA\|CONTABILIZADA\|FACTURADO` en registro compra |
| D5 | Despachos → bodega; **no** libro ventas | Contexto ventas / inventario | **Cumple** | Pestaña Despachos removida del libro; nota apunta a Insumos › Movimientos |
| D6 | Libro = emitidos/contabilizados; reverso contable | MJ [05:06:31]–[05:25:30] | **Cumple** | Subtitle + acción “Reverso contable”; totales RCV |
| D7 | Emisión: cuenta + CC en detalle emisión | Sergio [06:08:51]; MJ [06:14:01] | **Cumple** | `EmitirDocumentoPage` paso Ítems: Cuenta + CC requeridos al emitir |
| D8 | Quitar Emitir del libro | MJ [06:04:40] | **Cumple** | Sin botón Emitir/Nuevo en libro; menú Ventas › Emitir |
| D9 | Cotizaciones: registro hasta definir flujo | Mute → re-pregunta [07:01:10]; MJ [07:02:41]–[07:08:11] | **Cumple** (alcance) | Página cotizaciones activa; flujo aprobación **no cerrado** (pregunta abierta) |
| D10 | Inventariable / AlmaWeb paso | Minuta + materiales MJ | **Pendiente** | Sin flag `inventariable` en modelo/UI insumos |
| D11 | Plan/indicadores/elementos/CC → Parametrización; periodos en Contabilidad | Minuta | **Cumple** | Sidebar Parametrización con plan/indicadores/CC; periodos en Contabilidad |
| D12 | Panel SII config conservar | Minuta | **Cumple** | Config contable SII en Contabilidad (integración DTE removida hasta docs) |
| D13 | Contabilidad electrónica = 2ª etapa | Minuta | **Diferido** | Fuera de slice |
| D14 | Cartola Excel → calzar | MJ [10:55:30]; Sergio [11:06:00] | **Parcial** | Import genérico CSV/Excel/PDF ya existe; falta alinear Excel tipo MJ |
| D15 | Editar vencimiento solo rol tesorería | MJ [13:51:41]–[13:55:30] | **Cumple** | Aging: edit inline si `tesoreria:write`. `R4-17-nominas-aging.png` |
| D16 | Renombrar CC → Estado de cuenta | Sergio [14:56:30]; MJ [15:03:10] | **Cumple** | Label menú + página. `R4-17-estado-cuenta.png` |
| D17 | Plan cuentas 5 niveles / import Excel | Sergio [15:22:30]+ | **Parcial** | Import + niveles ya en código; falta validar Excel cliente MJ |

---

## 2. Action items Dev (R4-01…R4-25)

| ID | Acción | Pri. | Estado | Notas / captura |
|---|---|---|---|---|
| R4-01 | Búsqueda de rol | Jueves | **Cumple** | Input dedicado «Buscar rol por nombre…» + búsqueda de grilla |
| R4-02 | Selector pantallas por módulo (parcial/completo) | Jueves | **Cumple** | `RolesPage`: buscar módulo/pantalla + toggle módulo completo / columna R-W |
| R4-03 | Sin columna empresa en CC | Jueves | **Cumple** | `R4-03-centros-costo.png` |
| R4-04 | Lock proforma + asociar + clave | Jueves | **Cumple** | `R4-04-proformas.png` |
| R4-05 | OC elegibles en libro compras | Jueves | **Cumple** | Filtro estados recepción/contab/facturado |
| R4-06 | Cuenta + CC en emitir | Jueves | **Cumple** | Confirmado en wizard paso 2 (código + UI) |
| R4-07 | Quitar Emitir del libro | Jueves | **Cumple** | `R4-07-09-libro-ventas.png` |
| R4-08 | Reenvío PDF/XML | Post/DTE | **Diferido** | Integración DTE/GoSocket **eliminada** del código hasta documentación oficial |
| R4-09 | Totalizado tipo RCV | Jueves | **Cumple** | Cards Documentos/Neto/IVA/Exento/Total |
| R4-10 | Folio → representación gráfica | Post | **Cumple** | Click folio / PDF en libro; watermark BORRADOR auto |
| R4-11 | Carga Excel AlmaWeb | Depende MJ | **Pendiente** | Sin import Excel en insumos; material externo |
| R4-12 | Flag inventariable + NC reingreso | Post | **Pendiente** | Sin campo/modelo inventariable ni reingreso NC |
| R4-13 | Mover plan/afines a Parametrización | Jueves | **Cumple** | Redirects desde Contabilidad + menú Param |
| R4-14 | Factor honorario historial/vigencia | Post | **Cumple** | `vigenciaHasta` + badge Vigente en API/UI Honorarios |
| R4-15 | Menú Balance 8 columnas | Jueves | **Cumple** | 8 grupos de columnas + KPIs. `R4-15-balance-8-columnas.png` |
| R4-16 | Carga Excel cartolas | Depende MJ | **Parcial** | Import genérico UI+API listo; falta Excel tipo MJ + calce documentado |
| R4-17 | Edición vencimiento por rol | Jueves | **Cumple** | `R4-17-nominas-aging.png` |
| R4-18 | Propuesta módulo cobranza | Propuesta | **Propuesta** | Doc listo; sin feature UI |
| R4-19 | Conciliación: default pendientes + resumen cant/monto | Jueves | **Cumple** | KPI Conciliados/Pendientes; tab Pendientes. `R4-19-conciliacion.png` |
| R4-20 | Renombrar Estado de cuenta | Jueves | **Cumple** | |
| R4-21 | Filtro Todos / Pendientes | Jueves | **Cumple** | `R4-17-estado-cuenta.png` |
| R4-22 | Link pago y factura desde estado cuenta | Jueves | **Cumple** | Columna Ver con links a cartola/pago/factura; destinos respetan `?q=` |
| R4-23 | Import plan 5 niveles | Depende Excel | **Parcial** | Import Excel + niveles en código; falta smoke con Excel MJ |
| R4-24 | Impresión OC detalle | Post | **Cumple** | Print OC con líneas + distribución CC |
| R4-25 | Mantenedor códigos financieros | Post | **Pendiente** | Solo campo libre en anticipos; sin catálogo |

---

## 3. Interrupciones / ruido en la llamada (transcripción)

No hay corte literal de Meet en el texto; sí hay **pérdidas de continuidad** donde conviene re-preguntar en la próxima reu:

| ts | Qué pasó | Tema en riesgo | Pregunta a cerrar |
|---|---|---|---|
| [07:01:10] | «Está muteada María Jesús» | Cotizaciones / aprobación | ¿Cotizaciones quedan solo registro, o se define flujo de aprobación (jefatura) para temporada? |
| [11:04:11] | Sergio: «se me fue, era de la conciliación» | Flujo cartola ↔ conciliación | ¿La conciliación es solo vista de pendientes post-cartola, o también calce contable paralelo? |
| [13:44:21] | Re-compartir pantalla | Vencimiento + trazabilidad | Sergio preguntó trazabilidad de edición de vencimiento; MJ respondió **solo por rol**. ¿Audit log quién/cuándo es MVP o post? |
| [14:35:01] | MJ: «Ahí me perdí un poco de las cuentas corrientes» | Estado de cuenta | Confirmar que el nombre **Estado de cuenta** y filtro Todos/Pendientes quedó entendido (luego se aclaró [14:47:51]–[15:08:11]) |
| [14:05:20]–[14:15:41] | Propuesta cobranza aceptada («Sí, buenísimo») | R4-18 | Alcance MVP: ¿solo por cobrar ventas, o también por pagar? ¿Mail real o bitácora primero? |

### Gaps de la reu no numerados como R4-XX

| Tema | Estado | Nota |
|---|---|---|
| Cliente exportación + RUT externo | Pendiente | No en schema/UI Cliente |
| Aduana / país / puertos en emisión export | Pendiente | Depende docs DTE + manual MJ |
| NC exportación precargada | Pendiente | Post |
| Roles temporales | **Cumple** MVP | `rolVigenciaDesde/Hasta` + bloqueo login |
| Informe bodega por tipo documento | Pendiente | Material MJ #6 |
| Audit log edición vencimiento | **Cumple** MVP | Historial JSON + columna «Última edición» en aging |
| Anticipos ALM vs AlmaWeb (dual) | Pendiente | Solo anticipos productores |

---

## 4. Resumen ejecutivo de cumplimiento (slice jueves)

| Bucket | IDs |
|---|---|
| Listos para demo | R4-01…10, 13–15, 17, 19–22, 24 (+ D1–D9, D11, D15–D16); audit vencimiento; roles temporales MVP |
| Parciales (código base, falta cerrar) | R4-16/D14, R4-23/D17 |
| Propuesta (no código) | **R4-18** |
| Bloqueados post / MJ / DTE | R4-08, R4-11, R4-12/D10, R4-25, D13 |
| Gaps minuta **no** R4-XX | Exportación (tipo cliente + aduana/puertos + NC precarga); informe bodega por tipo doc; anticipos duales ALM/AlmaWeb; decisión final cotizaciones (Sergio) |

**Veredicto (re-auditoría 31/07):** el slice jueves está cerrado. Siguen pendientes reales; varios “Pendiente” de la matriz eran **parciales** (cartolas/import plan ya tienen código). No hay más gaps del slice jueves sin listar.
