# Resultados QA — Ola C integral ERP v2 (E2E golden ALM-*)

**Fecha:** 2026-08-15  
**Entorno:** local · Postgres `:5433` · API `http://localhost:3001/api/v1` · Front `http://localhost:5174`  
**Ejecutor:** almahue-qa-runner  
**Plan:** `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` §4.2, §9 Ola C · `DEMO-PROPUESTA-LOCAL.md` §4  
**Prerequisito:** Ola B **`LISTO_OLA_C`** — `2026-08-15-revision-ola-b-cierre.md`  
**JSON:** `2026-08-15-integral-erp-ola-c.json`  
**Script:** `ERP/.qa-tmp/run-ola-c-e2e.mjs`

No incluir JWT ni passwords.

---

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| **PASS** | 6 |
| **FAIL** | 0 |
| **BLOCKED** | 1 |
| **SKIP** | 1 |
| **Total casos Ola C** | 8 |

**Gate Ola C:** 0 FAIL P0/P1 en casos ejecutados. Billing stub activo (`BILLING_STUB_INLINE`). `seed:demo-propuesta` re-aplicado antes de cada corrida E2E.

**Veredicto runner:** **`PIPELINE_LOCAL_CERRADO`**

Pipeline local integral v2 (Ola A + B + C) cerrado para piloto **local**. Producción permanece **No-Go** hasta H14/E2E-008.

---

## Precondiciones §3 + checklist §8

| Check | Resultado | Evidencia |
|---|---|---|
| API `:3001` health | PASS | `GET /health` → `status=ok`, `db=ok` |
| Front `:5174` | PASS | `/login` HTTP 200; rutas demo sin 500 |
| Seeds | PASS | `npm run seed:demo-propuesta` antes de corrida |
| Billing stub `.env` | PASS | flags activos (corrida Ola A retest) |
| Periodo `2026-08` ABIERTO | PASS | `GET /periodos-contables` |
| Stock `INS-ALM-CEREZA` | PASS | post seed + movimientos E2E |
| Tenant EMP-1 | PASS | sesiones por usuario de prueba |

---

## Casos Ola C

| ID | P | Resultado | Evidencia |
|---|---|---|---|
| E2E-001 | P0 | PASS | `ALM-COT-001` → OC (`cperez` emit) → **Jorge PIN U-3** → recepción CONFIRMADA · registro BORRADOR `matchOk=true` |
| E2E-002 | P0 | PASS | `ALM-OV-002` cadena 3 pasos admin PIN → `AUTORIZADA` → confirmar stock → Δ cereza frigorífico **320** · UI `/comercial/aprobaciones` 200 |
| E2E-003 | P0 | PASS | `ALM-OV-004` `APROBADO` · `ALM-FAC-101` contabilizar → `billingStub=true` `ACCEPTED_STUB` · UI `/comercial/emitir` 200 |
| E2E-004 | P1 | PASS | Jorge crea/solicita proforma · admin PIN → `DEFINITIVA` → factura asociada (`PRF-E2E-*`) |
| E2E-005 | P1 | PASS | `POST /centralizacion/preview` 201 · cartolas/conciliaciones 200 · `POST /pagos` 201 · UI centralización + tesorería |
| E2E-006 | P0 | PASS | Recorrido 15 min: **8/8** rutas HTTP 200 sin 500 · folios seed `ALM-COT-001`, `ALM-OV-002`, `ALM-FAC-101` |
| E2E-007 | P2 | SKIP | Greenfield sin seed — omitido según plan |
| E2E-008 | P0 | BLOCKED | Prod `45.7.229.46` sin migrate H14 — smoke post-deploy no ejecutado |

---

## Log recorrido demo (E2E-006)

1. Inventario › bodegas / insumos  
2. Compras › cotizaciones / aprobaciones / recepción  
3. Ventas › orden de venta / aprobaciones / emitir  

Script adicional: flujos E2E-001–005 vía API + Playwright headless.

---

## Defectos vs deuda

| ID | Clasificación | Nota |
|---|---|---|
| E2E-008 / H14 | Deuda deploy | Prod sin paridad local — BLOCKED esperado |
| E2E-007 | Deuda plan | P2 opcional — SKIP válido |
| OV aprobación UI María | Deuda conocida | Aprobación funcional vía admin superadmin; `mgonzalez` sin `comercial:write` (Ola A) |
| Registro compra E2E-001 | Deuda evidencia | `BORRADOR` en golden path; `CONTABILIZADA` exige cuenta en líneas asiento |

Sin **FAIL** de producto nuevo en Ola C.

---

## Recomendación cierre piloto

| Entorno | Veredicto | Nota |
|---|---|---|
| **Local** | **Go demo / piloto** | Pipeline A+B+C cerrado · golden ALM-* ejecutado |
| **Prod** | **No-Go** | E2E-008 BLOCKED · acordar ventana H14 antes de prometer OV/stock/aprobación remota |

---

## Retest sugerido

- Tras deploy prod: **E2E-008** + smoke API post-migrate H14.
- Opcional: capturas UI con `mgonzalez` en bandeja OV si se exige evidencia visual aprobadores designados.
- Regresión: re-ejecutar `run-ola-c-e2e.mjs` tras cambios en cadena OC/OV o billing stub.

---

*Para revisión: `almahue-qa-reviewer`.*
