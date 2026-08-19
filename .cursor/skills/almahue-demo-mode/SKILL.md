---
name: almahue-demo-mode
description: Datos ficticios del modo demo (toggle front). Use when filling empty demo screens, editing mock fixtures, demo-store, or seed vs mock alignment.
---

# Modo demo Almahue

El toggle **Modo demo / Modo real** (`DemoModeToggle`) enruta lecturas/escrituras a `ERP/erp_front/src/services/mock/` vía `pickApi` en `services/api.ts`. Auth y usuarios siguen en API real.

## Dónde viven los datos

| Qué | Archivo |
|---|---|
| Maestros, asientos, proformas, OC, áreas | `services/mock/fixtures.ts` |
| Bodegas/insumos/clientes MJ | `services/mock/fixtures-almahue-demo.ts` |
| Grupos, escalas, AdminConcepto, suplencias | `services/mock/fixtures-aprobaciones-demo.ts` |
| Store mutable + diario/mayor/traspaso | `services/mock/demo-store.ts` |
| Handlers mock (reset al activar demo) | `services/mock/api.ts` |

Al activar demo se llama `resetDemoStore()` (store + grupos/escalas/delegaciones).

## Pautas

- Tenant `EMP-1`, periodo de trabajo **2026-08 ABIERTO**; 2026-07 y 2026-06 CERRADOS (contraste).
- Personas y PIN: skill `almahue-aprobaciones` → `reference.md` sección **B** (seed EMP-1 / Jorge). El QA desde cero (Laura / EMP-BOOT) no es el toggle demo.
- Compras cotización → OC; Ventas OV → stock → factura. No restaurar cotiz→NP.
- Libro diario/mayor se **derivan** de asientos `CONTABILIZADO` con `lineas` + `cuentaId`. No devolver arrays vacíos.
- Bandeja proformas: al menos una `PENDIENTE_APROBACION`. Traspaso: historial de un mes cerrado + proformas DEFINITIVA/FACTURADA en el mes abierto.
- Áreas de negocio: mismas que seed (`PACK`, `CAMPO`) más packing/frig coherentes.
- `workflows-admin` es pool legacy; la UI de reglas usa **grupos + escalas**.

## Pantallas que no pueden quedar vacías

`/admin/aprobaciones`, `/catalogos/areas-negocio`, `/contratistas/aprobaciones`, `/contratistas/traspaso`, `/contabilidad/libro-diario`, `/contabilidad/mayor`.

Si falta una pantalla: fixture + persistencia en store (no `return []` en `mock/api.ts`).
