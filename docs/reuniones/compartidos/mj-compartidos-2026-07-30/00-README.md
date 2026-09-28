# Fuentes compartidas por María Jesús (compromiso Reu4)

**Origen:** Tarjeta Trello (sin comentarios) · carpeta local “docs almahue MJ”  
**Fecha compromiso en sala:** Reu4 30/07/2026 (~01:13:45 / lista de “por compartir”)  
**Ingestado al monorepo:** 2026-08-06

## Inventario → uso

| Archivo | Compromiso Reu4 | Uso en ERP / billing-gateway |
|---|---|---|
| `EMISION_DE_NOTA_DE_CREDITO_Y_DEBITO_FACTURAS_CIERRE_COMEX.docx` | Manual facturación / NC-ND **exportación** | **Crítico** para DTE **110/111/112** y canónico export (ver extracto) |
| `INVENTARIO_A_MAYO.xlsx` | Inventario Excel AlmaWeb | Insumos/bodega (diferido AlmaWeb); hojas Analisis Inventario / VENTA / COMPRA |
| `Conta_Libro_DiarioExcel.xlsx` | Libro diario | Referencia formato contable / reportes |
| `Conta_Libro_MayorDolarExcel_….xlsx` | Libro mayor | Referencia mayor multi-moneda (USD) |
| `Balance8Columnas_Excel_….xlsx` | Balance | Validar UI Balance 8 columnas (R4-15) |
| `06-CARTOLA_JUNIO_2026.xls` | Excel cartolas | Tesorería: calce / parsers (hojas ALM CLP, Scotiabank, USD, Yuan…) |
| `ReportePorTipomovExcel_(7).xlsx` | Extra (no listado explícito) | Tipo de movimiento CC / aging — útil tesorería |

## Extractos (texto/buscable)

- [`extractos/EMISION_NC_ND_COMEX.txt`](extractos/EMISION_NC_ND_COMEX.txt) — procedimiento Acepta → campos a replicar en ERP/GoSocket  
- `extractos/*_preview.txt` — primeras filas de cada Excel

## Hallazgos clave del manual COMEX (para billing-gateway)

Procedimiento actual en **Acepta** (legacy). Al migrar a ERP + GoSocket hay que cubrir:

| Campo / regla | Valor / nota de negocio |
|---|---|
| Tipo doc referencia | **110** (factura exportación) |
| Motivo NC/ND cierre | “corrige monto” |
| ID Fiscal receptor extranjero | RUT fijo **55.555.555-5** |
| Código producto | Mismo de la factura (ej. `003`) |
| Descripción línea | Especie + embalaje (ej. `CEREZA 5 KN`) |
| Precio neto | `total_neto_USD / cajas` con **6 decimales** (archivo Comex) |
| UoM / cantidad | **caja** / cajas del embarque |
| Transporte | “DESPACHO POR CUENTA DEL EMISOR” |
| Modalidad venta | consignación libre o bajo condición (embarque) |
| Cláusula | FOB o CIF |
| Vía | marítima o aérea |
| Puertos | embarque + desembarque (de factura/Comex) |
| Bultos | tipo **22** (caja cartón), marca `-` |
| Observación | `TC` + tipo de cambio de la factura |
| Moneda | **13 — Dólar USA** |
| Otra moneda (CLP) | USD × TC; monto exento otra moneda = mismo CLP |
| Naming archivo | `ND 1263 EMB 65` (NC/ND + folio + embarque) |

Esto cierra el hueco “manual exportación MJ” que faltaba antes de diseñar el mapper **110/112** del gateway.

**Propuesta de implementación (flujo + UI, 10/09):** [`../../analisis-reuniones/10-propuesta-dte-exportacion-2026-09-10.md`](../../analisis-reuniones/10-propuesta-dte-exportacion-2026-09-10.md)

## Relación con otros packs

- GoSocket API: [`../gosocket-2026-08-05/`](../gosocket-2026-08-05/)  
- Plan gateway: [`../../partners-hub/00-PLAN-IMPLEMENTACION.md`](../../partners-hub/00-PLAN-IMPLEMENTACION.md)

## Pendiente aún (no vino en este pack)

- Ejemplos PDF timbrados / representación gráfica negocio (Pablo pidió si hay PDFs)  
- ApiKeys sandbox (reunión SII)  
- Archivo Excel “Comex” de un embarque real (el manual lo cita como fuente de cajas/montos) — útil como fixture
