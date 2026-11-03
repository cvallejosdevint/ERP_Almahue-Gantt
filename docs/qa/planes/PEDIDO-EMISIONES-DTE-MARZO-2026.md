# Pedido DTE marzo 2026 — solo ALM SERVICES → ALMAHUE EXPORT

**Para el otro chat (billing-gateway / GoSocket sandbox).**  
**No incluye ventas Export → cliente** (eso va por ERP Emitir o hilo aparte).

| Rol | Valor |
|-----|--------|
| Emisor (todas las filas) | **ALM SERVICES SPA** · RUT `77.032.639-7` · tenant `EMP-SERVICES` |
| Receptor (todas) | **ALMAHUE EXPORT SPA** · RUT `77.032.638-9` |
| BillerId / CAF | El de **EMP-SERVICES** en Admin (no el de EXPORT) |
| Manifiesto JSON | [`marzo-2026-manifiesto-emision.json`](../fixtures/marzo-2026-manifiesto-emision.json) → clave **`emisionesAlmAAlmahue`** |

## Por qué solo ALM → Almahue

El sandbox **rechaza** `SendDocument` cuando el RUT emisor del XML no coincide con el certificado del biller (casos previos con RUT proveedor/contratista ficticio). Para probar **insumos, guías, libro compras, proformas, NC/ND compras** con emisión real, **un solo emisor ALM** factura a Export; en ERP las OC/PF siguen identificadas por glosa y montos (`OC-2026-MAR-*`, `PF-MAR26-001`).

Tras emitir: `POST /registros-compra/sync` en Export (marzo 2026) o pegar folios con `npm run mar26:aplicar-folios-dte`.

---

## Tabla para el chat emisor (copiar tal cual)

Todas: **emisor** `77.032.639-7` · **receptor** `77.032.638-9` · **biller** SERVICES.

| Caso | tipoDte | Neto CLP | numeroInterno | idempotencyKey | Uso en ERP |
|------|---------|----------|---------------|----------------|------------|
| BIL-MAR-01 | **33** | 2.450.000 | F-MAR26-SVC-001 | `MAR26:EMP-SERVICES:F:INTERCO-001` | Intercompany · `REG-MAR26-INTERCO-001` |
| BIL-MAR-02 | **52** | (guía) | G-MAR26-INS-001 | `MAR26:EMP-SERVICES:G:OC-001` | Guía insumos · `OC-2026-MAR-001` / bodega |
| BIL-MAR-03 | **33** | 1.585.000 | F-MAR26-OC-001 | `MAR26:EMP-SERVICES:F:OC-001` | Factura OC urea · `REG-MAR26-OC-001` |
| BIL-MAR-04 | **52** | (guía) | G-MAR26-INS-002 | `MAR26:EMP-SERVICES:G:OC-002` | Guía · `OC-2026-MAR-002` |
| BIL-MAR-05 | **33** | 890.000 | F-MAR26-OC-002 | `MAR26:EMP-SERVICES:F:OC-002` | Factura embalaje · `REG-MAR26-OC-002` |
| BIL-MAR-06 | **33** | 4.200.000 | F-MAR26-CTR-001 | `MAR26:EMP-SERVICES:F:CTR-001` | Proforma · `PF-MAR26-001` · `REG-MAR26-CTR-001` |
| BIL-MAR-07 | **34** | 450.000 exenta | F-MAR26-EX-001 | `MAR26:EMP-SERVICES:F:EX-001` | Factura exenta · `REG-MAR26-EXENTA-001` |
| BIL-MAR-08 | **61** | 150.000 | NC-MAR26-OC-001 | `MAR26:EMP-SERVICES:NC:OC-001` | NC ref **F-MAR26-OC-001** · CodRef **3** |
| BIL-MAR-09 | **56** | 200.000 | ND-MAR26-CTR-001 | `MAR26:EMP-SERVICES:ND:CTR-001` | ND ref **F-MAR26-CTR-001** · CodRef **3** |

**Orden:** 01 → 06 facturas y guías base; 07 exenta; 08–09 NC/ND (requieren folio/GID de referencia ya emitido o datos ref en XML según GoSocket).

### Tipos que consume el ERP en estos módulos

| tipoDte | Módulo |
|---------|--------|
| 33 | Libro compras, match OC, asociar proforma, contabilizar |
| 34 | Libro compras exenta, activo fijo / tipo documento |
| 52 | Guía insumos (`GuiaInsumoRecibida`), sync compras |
| 61 / 56 | Libro compras NC/ND, referencias, devoluciones |

---

## Respuesta que necesitamos del chat

| numeroInterno | folioOficial | GlobalDocumentId | status |
|---------------|-------------|------------------|--------|

Con PDF/XML cuando existan.

---

## ERP local (Carlos / este chat)

```bash
cd ERP/erp_back
npm run seed:marzo-2026-export    # OC/PF/registros calzados + proveedor ALM en maestro EXPORT
npm run mar26:emit-manifiesto-alm # solo emisionesAlmAAlmahue (si gateway arriba)
npm run mar26:aplicar-folios-dte  # tras pegar folios en qa-results JSON
```

Ventas (33/52/61/56 **Export → cliente**): ver `emisionesVentasExportLocal` en el manifiesto; **no** pedirlas al chat ALM.

**No usar** `npm run mar26:emit-manifiesto` (deprecado; apuntaba al manifiesto viejo en `.qa-tmp`). Solo `mar26:emit-manifiesto-alm` o este pedido en billing.
