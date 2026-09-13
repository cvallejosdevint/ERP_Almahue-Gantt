# 2026-08-03 — R5 (**interna** Carlos ↔ Sergio)

- Video: `fuentes/videos/reunion5-2026-08-03.mp4` (**42:32**)
- Transcripción: `fuentes/transcripcion-reunion5.md` (reloj tl;dv; tramo largo ≈ ÷10 vs MP4)
- Refs UI que Sergio ya había pasado: `fuentes/sergio-ui-ref-2026-08-03/`
- Meet: solo **Carlos** + **Sergio**. **Nadie del cliente.** No es backlog. Sirve para ver *qué hipotetizaron* y qué pantallas de **referencia** (dtemite / DiffSii) copiaron
- Demo ERP: `localhost:5174`, modo real, periodo **agosto 2026**. Deploy a server **no** se subió (errores)

Hitos en `hitos/`. Nombres `12m00-rol-pin` y `18m00-usuario` **no coinciden** con el still: a esa hora Sergio ya comparte **otros productos**.

## 00:00–06:00 — PIN (ERP)

| t | Pantalla | Qué hipotetizan |
|---|---|---|
| 01:00 | Admin › Roles · **Aprobar con PIN (4 dígitos)** checked | Flag **por rol**; el PIN es **por usuario** (perfil). Reset en el propio perfil |
| audio | (mismo) | Carlos quiere mail al cambiar PIN. Sergio: si ya tienen la sesión, da igual; mejor **confirmar con la clave de la cuenta** (sin SMTP). Trazabilidad de quién cambió el PIN |

## 06:00–12:00 — bandeja + referencia dtemite

| t | Pantalla | Nota |
|---|---|---|
| 06:30 | `/contratistas/aprobaciones` · `PF-DEMO-PEND-01` $520.000 a **QA Aprobador** | Copy: «si no te la solicitaron, avisamos». Admin ve todas y puede aprobar **a nombre de** (Sergio: «súper jefe»; «consultarlo» con el cliente — **no consultado aquí**) |
| audio | OC | CC **por ítem**, no solo cabecera. PIN también en compras |
| 12:00 | **`pro.dtemite.cl/LibroVentas`** (empresa dtemite, no Almahue) | Sergio: resumen **por tipo** (FE / exenta / NC) + lista; NC resta. Minimizable. Folio = botón PDF. **No es Agrosoft** |

## 12:00–25:00 — DiffSii (producto Sergio) + libro Almahue

| t | Pantalla | Nota |
|---|---|---|
| 18:00 | **`saas.diffsii.cl`** Libro comercial | Acciones fila: facturar, PDF, mail, adjunto, anular. Enviar correo / adjuntos = UX a copiar; SMTP ERP aún no. **No es requisito MJ** |
| audio | (DiffSii) | Filtros en todos los libros. Preview = print del navegador |
| 25:00 | Almahue `/comercial/libro` | Cards neto/IVA/exento/total. Check **Ver todos los períodos** + advertencia RCV vs mes activo. Folio 80001 CONTABILIZADA. Botón **Borradores (1)** |

## 25:00–42:00 — borradores, param, periodos, tesorería

| t | Pantalla | Hipótesis (no cliente) |
|---|---|---|
| 32:00 | mismo libro | Factura 88001 + **cotización** 88003 EMITIDO. Acciones **PDF** / **Reverso contable** / Grabar y contabilizar. Sergio: cotiz ≈ OC; `+` cliente = panel lateral (no modal sobre modal). Totales: neto, exento, IVA, desc/recargo global y de línea. **«Ventas no van con CC; OC y facturas recibidas sí»** (Sergio — contrastar MJ en R4: CC en emisión de venta) |
| audio | Borradores | Lista **por usuario**; admin no ve los ajenos salvo filtro. Al finalizar se borra el borrador. Libro = contabilizado; borradores fuera o con filtro |
| audio | Periodos | Sergio: no «todos los periodos» (22.000 DTE/mes pega el browser) → **rango anual** / paginación. Quitar toggle de periodo «activo» duplicado. **Trazabilidad** quién abre/cierra + **comentario** al reabrir |
| audio | Param | Carlos: productores **duplicados**; sacar de Compras (dijo que MJ pidió param). Config SII = **fantasmeo IA** hasta docs GoSocket |
| 39:00 | Tesorería › Estado de cuenta · modal Pacífico $1.190.000 | Tipo movimiento venta/compra. Bug: factura 88001 no lista bien (BD limpia) |
| 41:30 | Tesorería › Pagos | Copy TC al calzar monedas. Filas $980.000 + **Cartola TRX-7781**. Cartolas/conciliación: **Carlos no las tocó** |

Cierre: se citan para «mañana» (eso es R6 **06/08** con cliente, no el 04).

## Qué **no** arrastrar como pedido Almahue

- Toda esta reunión: **interna**.
- UX **dtemite** y **DiffSii** = referencia de Sergio, no Agrosoft ni MJ.
- Aprobación de **cotizaciones** y admin «súper jefe»: hipótesis; el corte posterior (20/08 + 03/09) dejó cadena **solo OC**.
- «Ventas sin CC» (Sergio) vs R4 MJ/Sergio (CC en emisión): gana **transcripción con MJ**.
