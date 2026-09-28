# Tipos de referencia (Agrosoft → ERP)

Fuente: pantalla Agrosoft **TIPOS DE REFERENCIAS** (57 registros, 2026-08-25).

Catálogo versionado: `ERP/erp_back/prisma/data/tipos-referencia-agrosoft.json`.

Carga (idempotente, no pisa alias de otros módulos):

```bash
cd ERP/erp_back
npm run seed:tipos-referencia
```

También corre dentro de `npm run seed` y `npm run seed:qa-desde-cero`. En producción usar **solo** `seed:tipos-referencia` (no el seed completo).

UI: Parametrización › Tipos de documento, módulo **Referencia**.

## Qué cubre el ERP hoy vs el listado

| Capa | Qué hay |
|---|---|
| Catálogo `TipoDocumento` | Alias por módulo (Compras/Comercial/Tesorería…) + ahora los **57** códigos Agrosoft en módulo `Referencia`. |
| Emisión DTE (`mapTipoDte`) | Solo `FACTURA`/`NC`/`ND`/`GUIA` → SII **33, 34, 110, 61, 112, 56, 111, 52**. |
| Config contable SII (seed) | **33, 34, 61, 46** (+ cuentas internas CLIENTES/PROVEEDORES/IVA). |
| Wizard Emitir | FACTURA / NC / ND / GUIA. No boletas 35/39 ni honorarios 1000–1005. |
| Libro de compras | `RegistroCompra` no guarda el código SII/referencia de Agrosoft. |

Códigos del listado **ausentes del seed previo** (solo catálogo Referencia): 1004, 104, 106, 111, 112, 30–35, 43, 45, 46, 55, 56, 60–62, 71, 77, 78, BVE, y los numéricos SII 33/34/etc. como código de referencia (antes se usaban alias FAE/FCE/NC).

Códigos que **ya existían** como alias de módulo: 1000–1003, 1005, 101, 110, 70, 75, 76, 914, ABO, ANT, APE, BOL (boleta ventas, no rendición), CAR, CHQ, CHQM, COB, DEP, EGR, FEX, FFMM, ING, LET, OC, PAE, PAG, PROV, REC, TRA, TRANS, VAL, VB, BL.
