# Resultados QA — Ola A integral ERP v2

**Fecha:** 2026-08-15  
**Entorno:** local · Postgres `:5433` · API `http://localhost:3001/api/v1` · Front `http://localhost:5174`  
**Ejecutor:** almahue-qa-runner  
**Plan:** `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (Ola A)  
**Commit front referencia OV/Emitir:** `ERP/erp_front` `2035773` (branch `feature/backend-core`)

No incluir JWT ni passwords.

---

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| **PASS** | 20 |
| **FAIL** | 0 |
| **BLOCKED** | 2 |
| **SKIP (HEREDADO)** | 7 |
| **Total casos Ola A** | 29 |

**Gate Ola A:** 0 FAIL P0. Bloque billing por `.env` sin stub inline. Seed demo re-aplicado en corrida (`npm run seed:demo-propuesta`). Jest **150** tests PASS (SMK-008).

**Veredicto runner:** **LISTO_PARA_OLA_B** con deuda de entorno billing documentada.

---

## Precondiciones §3 + checklist §8

| Check | Resultado | Evidencia |
|---|---|---|
| API `:3001` health | PASS | `GET /health` → `status=ok`, `db=ok` |
| Front `:5174` | PASS | `/login` HTTP 200; dashboard post-login |
| Postgres `:5433` | PASS | Prisma migrate status: schema up to date (46 migraciones) |
| Seeds §3.1 | PASS* | `seed:demo-propuesta` ejecutado en corrida; ALM-* presentes |
| `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=true` | **FAIL checklist** | `.env`: `BILLING_GATEWAY_ENABLED=false`; sin `BILLING_STUB_INLINE` |
| Periodo `2026-08` ABIERTO | PASS | `GET /periodos-contables` |
| Stock `INS-ALM-CEREZA` BOD-ALM-FRIG > 0 | PASS | `GET /insumos/INS-ALM-CEREZA/stock-bodegas` → qty **4840** |
| Tenant EMP-1 | PASS | `GET /auth/me` → `empresaId=EMP-1` |

\* Seeds base (`npm run seed`, `seed:aprobaciones-f2`) asumidos vigentes; solo se re-ejecutó `seed:demo-propuesta` al detectar folios ALM en estado inconsistente.

---

## Conteo por bloque

| Bloque | PASS | FAIL | BLOCKED | SKIP |
|---|---:|---:|---:|---:|
| Smoke SMK | 8 | 0 | 0 | 0 |
| Ventas VEN (retest) | 8 | 0 | 0 | 0 |
| RBAC | 3 | 0 | 0 | 0 |
| Billing BIL | 0 | 0 | 2 | 0 |
| E2E (retest mínimo) | 3 | 0 | 0 | 0 |
| ADM HEREDADO | 0 | 0 | 0 | 7 |
| **Total** | **20** | **0** | **2** | **7** |

---

## Casos ejecutados

### Smoke (SMK)

| ID | Resultado | Evidencia |
|---|---|---|
| SMK-001 | PASS | `GET /health` 200 `db=ok` |
| SMK-002 | PASS | `POST /auth/login` 201 (admin) |
| SMK-003 | PASS | `GET /auth/me` 200 `empresaId=EMP-1` `bandejaModulos=[Compras,Contratistas,Comercial]` |
| SMK-004 | PASS | `GET /clientes` 200 count=2 tenant EMP-1 |
| SMK-005 | PASS | Periodo `2026-08` `ABIERTO` |
| SMK-006 | PASS | Stock cereza BOD-ALM-FRIG qty=4840 (post `seed:demo-propuesta`) |
| SMK-007 | PASS | UI `/` — «Hola, Admin», KPIs OC/proformas, usuario admin |
| SMK-008 | PASS | `npm test` erp_back exit 0 — 19 suites, **150** tests |

### Ventas — retest Emitir / lookup (VEN)

| ID | Resultado | Evidencia |
|---|---|---|
| VEN-021 | PASS | UI `/comercial/emitir` — selector solo FACTURA, NC, ND, GUIA (sin COTIZ/NP/OC) |
| VEN-023 | PASS | UI borrador `DOC-ALM-FAC-BORR` (ALM-FAC-101): línea Cereza qty=180 precio=2800 precargada |
| VEN-024 | PASS | UI misma factura: artículo Cereza bloqueado (selector collapsed); spinbutton precio editable (2800) |
| VEN-025 | PASS | UI OV `DOC-ALM-OV-BORR` contexto=ov: tipo SERVICIO → textbox «Descripción del servicio» sin bodega |
| VEN-026 | PASS | UI `/comercial/guias-despacho` carga + `GET /guias-despacho` 200; GUIA en selector Emitir |
| VEN-029 | PASS | `GET /lookup-rut?rut=76.111.000-K` → `clientes` length=1 |
| VEN-030 | PASS | `GET /lookup-rut?rut=76.543.210-K` → `proveedores` length=1 |
| VEN-031 | PASS | Lookup productor → `productores` length=1, `productor=true` (H1) |

### Seguridad (RBAC)

| ID | Resultado | Evidencia |
|---|---|---|
| RBAC-001 | PASS | `GET /documentos/DOC-SEED-NC-1` con `X-Empresa-Id: EMP-2` → 404 |
| RBAC-007 | PASS | Catálogo `pantallas-permisos.ts` Ventas = 6 ítems alineados Sidebar (Órdenes de venta, sin Cotizaciones bajo Ventas — H4) |
| RBAC-014 | PASS | `GET /aprobaciones-ov` **mgonzalez@almahue.cl** 200 (1 pendiente); Jorge 403 sin `comercial:read` (esperado OC-only) |

### Billing (BIL)

| ID | Resultado | Evidencia |
|---|---|---|
| BIL-001 | BLOCKED | `.env` `BILLING_GATEWAY_ENABLED=false`; sin stub inline — contabilizar stub no habilitado |
| BIL-002 | BLOCKED | Mismo entorno; disclaimer stub visible en UI Emitir pero flujo contabilizar stub no ejecutable |

### E2E — retest mínimo §9

| ID | Resultado | Evidencia |
|---|---|---|
| E2E-002 | PASS | API: `ALM-OV-002` (`DOC-ALM-OV-PEND`) estado `PENDIENTE_APROBACION` |
| E2E-003 | PASS | API: `ALM-OV-004` `APROBADO` + `ALM-FAC-101` borrador; UI borrador FAC cargado |
| E2E-006 | PASS* | Seed ALM-* verificado + UI smoke rutas demo (dashboard, OV, emitir, guías); recorrido 15 min no filmado |

\* E2E-006 documentado por API + navegación UI; sin video/capturas archivadas en esta corrida.

---

## HEREDADO / SKIP — baseline aprobaciones 20/20

No re-ejecutados según §1.8 plan v2 y alcance Ola A.

| ID | Resultado | Referencia baseline |
|---|---|---|
| ADM-009 | SKIP (HEREDADO) | `2026-08-12-veredicto-unificado.md` · `qa-retest-seed.mjs` 20/20 |
| ADM-010 | SKIP (HEREDADO) | idem |
| ADM-011 | SKIP (HEREDADO) | idem |
| ADM-012 | SKIP (HEREDADO) | idem (S1/S5/S6 simulador) |
| ADM-013 | SKIP (HEREDADO) | Consolidado ADM-012 v2 |
| ADM-014 | SKIP (HEREDADO) | Consolidado ADM-012 v2 |
| ADM-015 | SKIP (HEREDADO) | Baseline seed + spec AC |

---

## Defectos vs deuda

| ID / tema | Clasificación | Nota |
|---|---|---|
| BIL-001, BIL-002 | Entorno | Activar `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=true` en `.env` API |
| RBAC-014 Jorge 403 | No defecto | Aprobador OC sin `comercial:read`; bandeja OV validada con María (designado Comercial) |
| Checklist §8.1 billing | Entorno | Pendiente para retest BIL en Ola A |

---

## Retest sugerido (post-fix entorno)

1. Activar flags billing en `ERP/erp_back/.env` y reiniciar API → re-ejecutar BIL-001–002.
2. Ola B según plan v2 (PAR, CNT, TES, CTR profundo).
3. `almahue-qa-reviewer` sobre este informe.

---

## Artefactos

- JSON anonimizado: `resultados/2026-08-15-integral-erp-ola-a.json`
- Scripts corrida: `ERP/.qa-tmp/ola-a-api.mjs`, `ola-a-final.mjs`, `rbac-007.mjs`
