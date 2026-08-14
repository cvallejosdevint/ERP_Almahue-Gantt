# Fase 5 — Lista unificada de fixes

**Fecha:** 2026-08-14  
**Fuente:** ejecución plan Fase 4 + cruce Fase 1 (`2026-08-14-fase1-as-is-to-be.md`) y P0 demo Fase 3.

---

## Resumen ejecutivo

**¿Listo para demo cliente?** **No listo** para Recorrido B/C completo sin mitigaciones: el núcleo OV (confirmar, stock, factura, bajo costo) **pasa en API**, aprobaciones **20/20**, y compras OC→aprobación→recepción **pasa** con usuario correcto; pero hay un **fallo de aislamiento tenant (RB1)**, **lookup RUT roto frente a maestros seed**, **regresión Jest**, y **datos seed** (stock por bodega en cero, cotización sin proveedor) que obligan preparación manual antes de demo.

### Top 5 fixes (defectos nuevos / bloqueantes demo)

| Prioridad | ID | Módulo | Acción |
|-----------|-----|--------|--------|
| P0 | RB1 | Auth/tenant | Validar `X-Empresa-Id` vs `empresaId` del recurso en `GET /documentos/:id` (y revisar patrón global) |
| P1 | OV12/OV13 | Comercial | Corregir `lookup-rut`: matching RUT normalizado vs `Cliente`/`Proveedor` seed |
| P1 | JT-RUN | QA/insumos | Actualizar mocks `insumos.service.spec` (bodega/`StockInsumoBodega`) |
| P1 | JT-RUN | QA/comercial | Ajustar tipos en `comercial.service.spec` (`documentoOrigenId`, `folioOrigen`) |
| P1 | SM6 / G1 | Seed/inventario | Poblar `StockInsumoBodega` en seed showcase o migrar stock legacy → bodega default |

---

## Tabla unificada

| ID caso | Sev. | Módulo | Descripción | Clasificación | Acción sugerida |
|---------|------|--------|-------------|---------------|-----------------|
| RB1 | P0 | Seguridad | Documento EMP-1 legible con header EMP-2 (usuario mono-empresa) | defecto nuevo | Filtrar por tenant en findUnique + rechazar header inconsistente con JWT |
| OV12 | P1 | Comercial | Lookup no devuelve cliente existente (`76.111.000-K`) | defecto nuevo | Unificar normalización RUT en query y BD |
| OV13 | P1 | Comercial | Lookup no devuelve proveedor seed | defecto nuevo | Idem OV12 |
| JT-RUN | P1 | QA | 4 tests insumos + suite comercial no compila | defecto nuevo | Arreglar specs (no producto) |
| SM6 prep | P1 | Inventario/seed | Tras seed, bodega Central qty=0 pese stock legacy | defecto datos / G1 | Seed o script prep demo |
| OV15 | P2 | Comercial/compras | Cotización BORRADOR sin proveedor → no convierte a OC | entorno/datos | Completar `DOC-SEED-COT-BORR` en seed |
| CP2 (admin) | P2 | Compras | OC con solicitante fuera de grupo → 400 esperado | comportamiento OK | Documentar: usar Luis Herrera en guiones |
| OV1–OV10, OV17 | — | Comercial | Flujo OV P0 | PASS | Mantener en regresión API |
| E/S/AC/OC/R/V | — | Aprobaciones | 20/20 script | PASS | Gate pre-demo |
| CP1,3–5,7–8,10 | — | Compras | Cableado OC/recepción/matching | PASS | Retest tras cambios compras |
| OV11 | P2 | Comercial | Sin UI `ventaBajoCosto` | deuda DK-D16 | Pantalla admin empresa |
| OV14 | — | Comercial | Sin productor | deuda DK-D7 | No FAIL |
| OV16 | — | Comercial | Cotiz→factura | deuda DK-D11 | API ya rechaza |
| RB8 | — | Admin | workflows-admin legacy | deuda DK-LEGACY | No promover |
| DK-D4 | — | Aprobaciones | Sin cadena OV/factura | deuda | No vender en demo |
| DK-EMITIR | P2 | Comercial UI | Wizard emitir mezcla tipos | deuda Fase 1 | Restringir UI |
| DK-D11 catálogo | P2 | Permisos | pantallas-permisos vs menú | deuda Fase 1 | Skill pantallas-permisos |
| DK-D20 | P1 | Deploy | Prod sin migrate OV | deuda entorno | Deploy explícito |
| CT2–CT11, TB*, CTR2–7 | P2 | Back-office | No ejecutado Fase 5 | gap cobertura | Segunda pasada QA |
| R2 | P2 | Front | Build no corrido | SKIP | `tsc -b && vite build` pre-release |

---

## Cruce Fase 1 gaps

| Gap Fase 1 | Evidencia Fase 5 | Estado |
|------------|------------------|--------|
| Flujo OV→stock→factura (alta demo) | OV1–OV6, OV8–OV10 PASS | **Mitigado API**; UI no probada |
| Emitir documento mezcla tipos | No probado UI | Sigue DK-EMITIR |
| `ventaBajoCosto` sin UI | OV10 PASS API | Sigue DK-D16 |
| Lookup productor | OV14 DEBT | Sigue DK-D7 |
| pantallas-permisos desfasado | No retest UI | Sigue D11 doc |
| Prod vs local OV | Local migrate OK | Sigue DK-D20 |
| Aprobación solo OC/proformas | Oleada 2 PASS | Sigue DK-D4 |

---

## Cruce Fase 3 P0 (demo)

| P0 Fase 3 | Fase 5 |
|-----------|--------|
| Recorrido B (OV + stock) | API PASS con prep movimiento bodega |
| Aprobaciones estables | 20/20 PASS post-seed |
| AdminConcepto re-login | AC1 PASS (no retest UI) |
| Tenant/permisos | RB2–RB4 PASS; **RB1 FAIL** bloquea confianza multi-empresa |

---

## Veredicto

- **Demo ventas (API):** viable con **entrada manual a bodega** y sin depender de lookup RUT.  
- **Demo compras:** viable con usuarios seed (Luis + Jorge) y PIN 4821.  
- **Demo cliente formal:** **no listo** hasta corregir **RB1** y alinear seed/lookup; ejecutar retest UI Recorridos A/B/C pendiente.

---

## Estado post-fix (2026-08-14)

| ID | Estado | Evidencia |
|----|--------|-----------|
| **RB1** | **RESUELTO** | `getDocumento` usa `resolveOperationalEmpresa` + `findFirst({ id, empresaId })`. Retest API: Luis + `X-Empresa-Id: EMP-2` → **403** (antes 200 con doc EMP-1). |
| **OV12** | **RESUELTO** | `lookupRut` normaliza RUT y filtra clientes en memoria. Retest: `76111000-K` → 1 cliente (`CLI-SEED-1B`). |
| **OV13** | **RESUELTO** | Idem proveedores. Retest: `76543210-K` → 1 proveedor (`PROV-SEED-1`). |
| **JT-RUN** | **RESUELTO** | `npm test` → **18 suites, 136 tests PASS** (insumos mocks bodega/stock + tipos comercial.service.spec). |
| **SM6 / G1** | **RESUELTO** | `seed.ts` hace upsert `StockInsumoBodega` Urea/Bodega Central qty=1200. Retest: `stock-bodegas` Central **1200** sin movimiento manual. |
| **OV15** | **RESUELTO** | Cotizaciones showcase (`DOC-SEED-COT-*`) con `proveedorId` + receptor RUT proveedor (flujo Compras D11). |

**Pendiente sin cambio:** DK-D16, DK-D7, DK-D4, DK-EMITIR, DK-D20, retest UI Recorridos A/B/C, oleadas CT/TB/CTR profundas.
