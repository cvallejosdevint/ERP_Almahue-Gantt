# Revisión QA — Ola A integral ERP v2

**Fecha:** 2026-08-15  
**Revisor:** almahue-qa-reviewer  
**Informe revisado:** `2026-08-15-integral-erp-ola-a.md` / `.json`  
**Plan:** `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (Ola A)  
**Veredicto encargado proyecto:** `2026-08-15-veredicto-encargado-proyecto.md` (emitido en paralelo)

---

## 1. Integridad de la corrida

| Criterio checklist §8 | Cumplido | Nota |
|---|---|---|
| 8.1 Entorno (API/front/DB) | **Sí** | Health, migrate 46, periodo ABIERTO, stock 4840 |
| 8.1 Seeds §3.1 | **Parcial** | `seed:demo-propuesta` re-ejecutado; base/f2 asumidos vigentes |
| 8.1 Billing `.env` | **No** | `BILLING_GATEWAY_ENABLED=false`; sin `BILLING_STUB_INLINE` |
| 8.2 Sesión / usuarios | **Parcial** | Tenant EMP-1 OK; **ADM-022 no ejecutado** |
| 8.3 Evidencia | **Sí** | JSON anonimizado; sin JWT; UI P0 con URL/usuario en VEN/RBAC |
| 8.4 Clasificación | **Sí** | BLOCKED/HEREDADO documentados; sin FAIL de producto |
| 8.5 Cierre Ola A completa | **No** | ~29/55 casos P0 Ola A; varios EJECUTAR omitidos |

**Conclusión integridad:** la corrida es **válida y reproducible** para el subconjunto ejecutado (smoke, retest Emitir/lookup, RBAC, E2E API mínimo). **No** cumple el alcance completo de Ola A según §9 (orden: ADM-022 → CMP-012–013 → VEN-009–012 → INV-010 → BIL). Evidencia **suficiente** para lo probado; **insuficiente** para cerrar Ola A al 100 %.

---

## 2. BIL-001 / BIL-002 — BLOCKED

| ID | Clasificación | Fundamento |
|---|---|---|
| BIL-001 | **Entorno** | `.env` con `BILLING_GATEWAY_ENABLED=false`; stub inline no configurado |
| BIL-002 | **Entorno** | Mismo; UI muestra disclaimer stub pero contabilizar no habilitado |

No es defecto de producto. El código y `.env.example` documentan los flags. Retest tras activar `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=true` y reiniciar API.

---

## 3. HEREDADO ADM-009–015

| ID | ¿HEREDADO aceptable? | Nota |
|---|---|---|
| ADM-009–014 | **Sí** | Baseline `2026-08-12-veredicto-unificado.md` + `qa-retest-seed.mjs` 20/20 (§1.8 plan v2) |
| **ADM-015** | **No** | Plan v2 marca **EJECUTAR** (P1): modal `APROBADOR_SIN_BANDEJA` en UI — el runner lo omitió como HEREDADO por error |

Revalidar ADM-009–014 solo si cambian reglas/PIN/AdminConcepto o post-deploy prod.

---

## 3.1 Billing — fix entorno aplicado (post-revisión)

Tras la corrida Ola A se activó en `ERP/erp_back/.env`:

- `BILLING_GATEWAY_ENABLED=true`
- `BILLING_STUB_INLINE=true`

**Pendiente:** reiniciar API y retest **BIL-001, BIL-002**.

## 4. Defectos nuevos vs deuda conocida

| Hallazgo | Tipo | Acción |
|---|---|---|
| BIL BLOCKED | Deuda entorno | Activar flags billing local |
| VEN-009–012 no ejecutados | Cobertura Ola A | Retest con flag `comercialRequiereAprobacion` (D4) |
| CMP-012–013 no ejecutados | Cobertura Ola A | Retest match 3 vías |
| INV-010 no ejecutado | Cobertura Ola A | Retest NC → reingreso bodega (H7) |
| ADM-022 no ejecutado | Cobertura Ola A | Retest re-login AdminConcepto |
| **ADM-015** marcado HEREDADO por runner | **Error clasificación** | Retest modal `APROBADOR_SIN_BANDEJA` (plan EJECUTAR) |
| E2E-006 parcial (sin video) | Deuda evidencia | Ola C o capturas pre-demo |
| RBAC-014 Jorge 403 | **No defecto** | Aprobador OC sin `comercial:read`; bandeja OV validada con mgonzalez |
| Emitir, lookup H1, pantallas H4, guías H8 | **PASS** | Cierra deuda documental pre-14/08 |

**Defectos P0 nuevos en producto:** **ninguno** reportado en Ola A.

---

## 5. Veredicto revisor

**`REQUIERE_RETEST`**

El runner declaró `LISTO_PARA_OLA_B` de forma **prematura**: el gate formal Ola A (§9) exige 100 % PASS P0 **EJECUTAR**; faltan casos listados en §6 y checklist §8.1 billing (fix aplicado, retest pendiente).

Alineado con veredicto encargado proyecto: **GO condicionado** demo local; **No-Go** prod y Ola B/C plenas.

---

## 6. Retest mínimo recomendado

**Antes de declarar Ola A cerrada o iniciar Ola B con confianza alta:**

1. **Billing:** reiniciar API (flags ya en `.env`) → **BIL-001, BIL-002**
2. **Ola A pendiente (una sesión):** **ADM-022**, **ADM-015**, **CMP-012–013**, **VEN-009–012**, **INV-010** — JSON + capturas §8.3
3. **Opcional pre-demo:** E2E-002/003 completos en UI (PIN, capturas); no bloquea retest mínimo

**No** re-ejecutar ADM-009–014 salvo regresión en reglas aprobación.

---

## 7. Referencias cruzadas

| Documento | Relación |
|---|---|
| `2026-08-15-veredicto-encargado-proyecto.md` | GO demo condicionado; No-Go prod; acciones §6 |
| `2026-08-15-analisis-integridad-qa-v1.md` | Origen checklist §8 |
| `HUERFANOS-H1-H14.md` | H1/H4/H8 PASS Ola A; H14 prod pendiente |

---

## 8. Post-retest (2026-08-15)

Tras este informe se ejecutó retest mínimo §6: [`2026-08-15-integral-erp-ola-a-retest.md`](2026-08-15-integral-erp-ola-a-retest.md) — **11 PASS, 0 FAIL, 0 BLOCKED** (`OLA_A_RETEST_OK`).

| Gap original | Estado post-retest |
|---|---|
| BIL-001/002 | PASS (billing stub) |
| VEN-009–012 | PASS (API; VEN-010 UI headless sin filas — nota reviewer) |
| CMP-012/013 | PASS |
| INV-010 | PASS |
| ADM-022, ADM-015 | PASS |

Cierre formal: pendiente [`2026-08-15-revision-ola-a-cierre.md`](2026-08-15-revision-ola-a-cierre.md) (`almahue-qa-reviewer`).

---

*Revisión documental. Sin re-ejecución de pruebas en esta sesión.*
