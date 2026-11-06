# Pedido DTE agosto 2026 - solo ALM SERVICES → ALMAHUE EXPORT

Emisor: **ALM SERVICES SPA** (`77.032.639-7` / `EMP-SERVICES`).  
Receptor: **ALMAHUE EXPORT SPA** (`77.032.638-9` / `EMP-EXPORT`).  
Manifiesto: [`docs/qa/fixtures/agosto-2026-manifiesto-emision.json`](../fixtures/agosto-2026-manifiesto-emision.json).  
Script: `npm run ago26:emit-manifiesto-alm` (desde `ERP/erp_back`).

## Estado 05/11/2026

| Resultado | Casos |
|-----------|--------|
| **OK (PENDING + folio)** | Guias 52: BIL-AGO-02/04/06 (folios 63/64/65). Exenta 34: BIL-AGO-11 (folio 54). |
| **BLOCKED CAF** | Todas las facturas 33 (BIL-AGO-01/03/05/07/08/09/10): GoSocket `There are no primary ranges`. |
| **SKIPPED** | NC/ND (12-13) hasta existir folio de la factura de referencia. |

Cargar CAF de **factura (33)** para RUT `77.032.639-7` en portal sandbox GoSocket (Gestion de folios). Guias y exenta ya tienen rango. Luego:

```bash
cd ERP/erp_back
npm run ago26:emit-manifiesto-alm -- --solo=BIL-AGO-01
# repetir por cada 33 rechazado (mismas idempotencyKey = reintento OK)
```

Reporte: `ERP/erp_back/qa-results/ago26-emit-alm-report.json` (gitignored).

## Tabla de emisiones

| Caso | tipo | Neto | numeroInterno | Fecha | Uso ERP |
|------|------|------|---------------|-------|---------|
| BIL-AGO-01 | 33 | 1.850.000 | F-AGO26-OC-001 | 05/08 | OC servicios `OC-2026-AGO-001` |
| BIL-AGO-02 | 52 | 1.440.000 | G-AGO26-INS-001A | 08/08 | OC insumos madre parcial 60% |
| BIL-AGO-03 | 33 | 1.440.000 | F-AGO26-INS-001A | 09/08 | Factura hija .1 |
| BIL-AGO-04 | 52 | 960.000 | G-AGO26-INS-001B | 18/08 | OC insumos madre parcial 40% |
| BIL-AGO-05 | 33 | 960.000 | F-AGO26-INS-001B | 19/08 | Factura hija .2 |
| BIL-AGO-06 | 52 | 960.000 | G-AGO26-INS-002 | 12/08 | OC insumos simple |
| BIL-AGO-07 | 33 | 960.000 | F-AGO26-INS-002 | 13/08 | Factura OC insumos 002 |
| BIL-AGO-08 | 33 | 3.500.000 | F-AGO26-CTR-001 | 20/08 | Proforma completa `PF-AGO26-001` |
| BIL-AGO-09 | 33 | 1.000.000 | F-AGO26-CTR-002A | 22/08 | Proforma parcial 1/2 |
| BIL-AGO-10 | 33 | 800.000 | F-AGO26-CTR-002B | 28/08 | Proforma parcial 2/2 |
| BIL-AGO-11 | 34 | 320.000 | F-AGO26-EX-001 | 25/08 | Exenta sin OC |
| BIL-AGO-12 | 61 | 120.000 | NC-AGO26-OC-001 | 27/08 | NC ref F-AGO26-OC-001 |
| BIL-AGO-13 | 56 | | 150.000 | ND-AGO26-CTR-001 | 29/08 | ND ref F-AGO26-CTR-001 |

Guia operativa de vinculacion en Export: [`docs/qa/resultados/2026-11-05-agosto-guia-vinculacion-alm.md`](../resultados/2026-11-05-agosto-guia-vinculacion-alm.md).
