# Fase 4 — Plan de testing integral (resumen ejecutivo)

**Fecha:** 2026-08-14  
**Validación código:** 2026-08-14 (controllers Nest + 18 `*.spec.ts` + scripts QA)  
**Entregable:** `qa/PLAN-PRUEBAS-INTEGRAL-FASE4.md`  
**Ejecución:** Fase 5 (no se corrieron tests API en Fase 4; solo planificación)

---

## Alcance

Plan de pruebas **ejecutable** con prioridad **backend/API** para encontrar bugs, gaps de flujo e inconsistencias. Reutiliza el plan de aprobaciones cerrado (20/20 local vía `qa-retest-seed.mjs`) y extiende cobertura a comercial/OV, compras matching, contabilidad, tesorería, contratistas, RBAC y smoke de entorno.


| Oleada                 | Foco                                              | Casos ID                     | Tiempo est.        |
| ---------------------- | ------------------------------------------------- | ---------------------------- | ------------------ |
| 0 Smoke                | health, login, tenant, stock bodega               | 6 SM                         | ~5 min             |
| 1 Jest                 | 18 `*.spec.ts` (~120 tests)                       | JT-RUN + inventario          | ~2 min             |
| 2 Aprobaciones         | Reuso E/S/AC/OC/V/R                               | 20 (+ R2 build opc.)         | ~5 min             |
| 3 Comercial/OV         | OV, stock, factura, lookup, FLETE, bajo costo     | 17 OV                        | ~15 min            |
| 4 Compras              | OC, recepción, R4-05 matching                     | 11 CP                        | ~10 min            |
| 5 Contab + Tesorería   | periodos, centralización, cartolas, estado cuenta | 22 CT+TB                     | ~15 min            |
| 6 Contratistas + ficha | proformas, aprobación, ficha contraparte          | 10 CTR+FICHA                 | ~10 min            |
| 7 RBAC / seguridad     | tenant, AdminConcepto, bandeja sin permiso global | 10 RB                        | ~10 min            |
| **Total planificado**  |                                                   | **96 IDs API** (+ ~120 Jest) | **~65–80 min API** |


UI: Recorridos demo **A/B/C** (Fase 3) y E2E sin seed (34) quedan para Fase 5 opcional (~55–90 min adicionales).

---



## Correcciones aplicadas al borrador

1. **OV15:** `tipoDestino` corregido de `ORDEN_COMPRA` → `"OC"` (`ConvertirDocumentoDto`).
2. **OV8:** body explícito `{ "tipoDestino": "FACTURA" }`; OV debe estar `APROBADO` antes de convertir.
3. **OV11:** `ventaBajoCosto` vía `PUT /empresas/:id` (admin), no PATCH directo a BD.
4. **CP4:** aprobación OC = `PUT /ordenes-compra/:id` con `pinAprobacion` (como `qa-retest-seed.mjs` OC3).
5. **CP5:** recepción = `POST /recepciones-oc` (borrador) + `PATCH /recepciones-oc/:id` `{ estado: "CONFIRMADA" }`.
6. **TB7:** ruta corregida a `GET /cuentas-corrientes/:terceroId/movimientos?terceroTipo=CLIENTE`.
7. **CTR4:** flujo `solicitar-aprobacion` **→** `POST .../definitiva` con PIN (no «resolver» genérico).
8. **FICHA1:** proveedores en `catalogos.controller` (`GET /proveedores/:id`), no comercial.
9. **SM6:** precheck stock vía `GET /insumos/:id/stock-bodegas`; `validate-demo-counts.ts` no cubre stock bodega.
10. **Inventario Jest:** 18 archivos confirmados; conteos `it()` actualizados; suite ~**120 tests** (no ~110).
11. **Conteo total:** **96 casos API** por ID (borrador decía 86 por conteo incompleto).

---



## Relación con fases previas


| Fuente                                | Incorporado en plan                       |
| ------------------------------------- | ----------------------------------------- |
| Fase 1 §3 flujos transversales        | Oleadas 3–7 + deuda DK-*                  |
| Fase 3 G1–G10, P0, Recorrido B        | OV P0, SM6, G1 sin seed OV, guion Emitir  |
| Veredicto 2026-08-13                  | Oleada 2 no reescrita; scripts existentes |
| `PLAN-PRUEBAS-APROBACIONES.md`        | Oleada 2 íntegra (20 casos script)        |
| `PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md` | Fuera de oleadas API; referencia profundo |


---



## Inventario Jest (18 archivos — paths exactos)

Todos bajo `ERP/erp_back/src/`:

1. `auth/pin-aprobacion.spec.ts` (13)
2. `modules/admin/admin.service.spec.ts` (7)
3. `modules/aprobaciones/approval-engine.spec.ts` (21)
4. `modules/billing/canonical-builder.spec.ts` (2)
5. `modules/catalogos/bc-schedule.util.spec.ts` (2)
6. `modules/catalogos/catalogos.service.spec.ts` (5)
7. `modules/comercial/comercial-ov.spec.ts` (2)
8. `modules/comercial/comercial.service.spec.ts` (12)
9. `modules/compras/compras.service.spec.ts` (16)
10. `modules/contabilidad/contabilidad.service.spec.ts` (11)
11. `modules/contabilidad/contabilizar.service.spec.ts` (4)
12. `modules/contratistas/contratistas.service.spec.ts` (15)
13. `modules/dashboard/dashboard.service.spec.ts` (5)
14. `modules/insumos/insumos.service.spec.ts` (7)
15. `modules/tesoreria/cartola-parser.util.spec.ts` (4)
16. `modules/tesoreria/tesoreria.service.spec.ts` (2)
17. `modules/tesoreria/parsers/almahue-web.spec.ts` (1)
18. `modules/tesoreria/parsers/bank-parsers.spec.ts` (3)

Números entre paréntesis = bloques `it()` por archivo.

---



## Top 5 gaps de cobertura Jest (confirmados en código)

1. `ventaBajoCosto` **/** `assertLineasMaestro` — `comercial-ov.spec.ts` solo mock `BLOQUEAR` en `beforeEach`; sin tests `PERMITIR_MERMA` ni FLETE aislado (lógica en `comercial.service.ts` L565+).
2. `lookupRut` **y productor** — sin `*.spec.ts`; D7 cubierto solo en oleada API OV12–OV14 (`comercial.controller` `GET lookup-rut`).
3. **Factura desde OV (lock qty/desc)** — `assertFacturaLineasLocked` en service (L622+) **no** aparece en specs; OV9 API obligatorio.
4. **Stock por bodega (**`StockInsumoBodega`**)** — `insumos.service.spec` usa stock legacy; sin tests `GET stock-bodegas` ni saldo negativo por bodega.
5. **Tesorería operativa (**`cuenta-corriente.service`**)** — `tesoreria.service.spec` tiene 2 tests; parsers bien cubiertos pero no CC/conciliación/pagos integrados.

Otros gaps menores: `centralizacion` service, `auth.service`, ficha contraparte (sin spec), billing gateway E2E.

---



## Casos P0 oleada comercial (ejecutar primero en Fase 5)


| ID   | Caso                                              | Por qué P0                          |
| ---- | ------------------------------------------------- | ----------------------------------- |
| SM6  | `GET /insumos/:id/stock-bodegas` > 0              | Precondición Recorrido B paso 1; G1 |
| OV1  | Crear OV PRODUCTO + splits                        | Base Recorrido B; sin seed OV       |
| OV4  | Rechazar confirmar sin stock                      | D15 demo credibilidad               |
| OV5  | `POST /documentos/:id/confirmar` → SALIDA_VENTA   | Core flujo ventas Reu6              |
| OV6  | `GET stock-bodegas` post confirmar                | Evidencia stock multi-bodega        |
| OV8  | `POST .../convertir` `{ tipoDestino: "FACTURA" }` | Recorrido B paso 4                  |
| OV9  | `PUT /documentos/:id` lock qty/desc               | D13                                 |
| OV10 | `ventaBajoCosto` BLOQUEAR                         | D16 default activo                  |
| OV15 | Cotización → OC (`tipoDestino: "OC"`)             | D11 flujo compras                   |


**Pre-requisito datos:** migrate `20260813230000_stock_ov_ficha` + stock en bodega (P0-2 Fase 3). Sin esto → OV4–OV9 **BLOCKED** (DK-G1), no FAIL.

---



## Scripts existentes (reutilizar en Fase 5)


| Script                                             | Uso validado                                         |
| -------------------------------------------------- | ---------------------------------------------------- |
| `ERP/.qa-tmp/qa-retest-seed.mjs`                   | Oleada 2: E1–E3, S1–S6, AC1–AC5, OC1–OC4, V1, R1     |
| `ERP/erp_back/scripts/qa-aprobaciones-integral.ts` | APIs ampliadas aprobaciones + gaps esperados         |
| `ERP/erp_back/scripts/validate-demo-counts.ts`     | Conteos OC/facturas/CC/periodos; **no** stock bodega |
| `ERP/erp_back/scripts/prepare-demo-sergio.ts`      | Limpieza QA + flujo compras presentable (sin OV)     |


---



## Automatización recomendada (siguiente paso)

Crear `ERP/erp_back/scripts/qa-integral-fase4.ts` que:

- Ejecute SM + OV P0 + CP8/CP9 + RB1–RB4 + TB6–TB7.
- Subproceso `qa-retest-seed.mjs` para Oleada 2.
- Helpers `login()` + header `X-Empresa-Id: EMP-1`.
- Salida JSON en `qa/resultados/` sin JWT.
- Entrada npm: `test:qa:fase4` en `package.json`.

Ver estructura detallada en plan §12.

---



## Tabla deuda conocida DK-* (no FAIL)


| ID        | Tema                                     |
| --------- | ---------------------------------------- |
| DK-D4     | Sin cadena aprobación OV/factura         |
| DK-D11    | Cotizaciones menú vs permisos            |
| DK-D16    | `ventaBajoCosto` sin UI admin            |
| DK-D7     | Productor en lookup (`productor: false`) |
| DK-EMITIR | Wizard Emitir mezcla tipos               |
| DK-DTE    | Billing stub / GoSocket                  |
| DK-LEGACY | `workflows-admin` API                    |
| DK-G1     | Sin seed OV E2E                          |
| DK-G10    | Showcase NP/cotización cliente           |
| DK-D20    | Prod sin migrate OV                      |
| DK-D14    | Sin tránsito venta                       |
| DK-R4-18  | Cobranza mail                            |
| DK-G5     | Traspaso cierre ≠ gastos temporada       |


---



## Criterios para cerrar Fase 5

- Sin BLOCKED en SM y Oleada 2.
- OV P0 PASS o BLOCKED documentado (G1).
- FAIL nuevos clasificados vs tabla DK-* (13 ítems).
- ≥ 90% PASS en casos API ejecutables.
- Lista unificada de fixes con ID de caso y severidad.

---



## Archivos actualizados


| Archivo                                                                                                         |
| --------------------------------------------------------------------------------------------------------------- |
| `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-INTEGRAL-FASE4.md`                               |
| `docs/erp-planificacion/agrosoft-levantamiento/qa/resultados/2026-08-14-fase4-plan-testing.md` (este documento) |


