# Revisión QA — Ola B integral ERP v2

**Fecha:** 2026-08-15  
**Revisor:** almahue-qa-reviewer  
**Entradas:**

| Documento | Rol |
|---|---|
| `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` §4.1, §8, §9 | Alcance Ola B, checklist, orden |
| `2026-08-15-revision-ola-a-cierre.md` | Gate previo **LISTO_OLA_B** |
| `2026-08-15-integral-erp-ola-b.md` / `.json` | Corrida Ola B (runner) |
| `AGENTS.md`, `HUERFANOS-H1-H14.md` | Huecos vigentes / no-FAIL |
| Skill `almahue-tesoreria` | Contexto módulo tesorería |

Sin JWT. Sin re-ejecución de pruebas en esta sesión.

---

## 1. Integridad corrida Ola B

### 1.1 Checklist §8

| Ítem | Estado | Nota revisor |
|---|---|---|
| **§8.1** Postgres `:5433` | **PASS** | Evidencia gate health |
| **§8.1** API `:3001` + `db=ok` | **PASS** | |
| **§8.1** Front `:5174` | **PASS** | Smoke `/login` |
| **§8.1** Seeds §3.1 | **PASS*** | Re-ejecutado `seed:demo-propuesta`; seeds base asumidos vigentes (no re-log de `seed` + `seed:aprobaciones-f2` en informe) |
| **§8.1** Billing stub | **PASS** | `BILLING_GATEWAY_ENABLED` + `BILLING_STUB_INLINE` |
| **§8.1** Periodo `2026-08` ABIERTO | **PASS** | CNT-001 |
| **§8.1** Stock cereza > 0 | **PASS** | `stockTotal=4790` |
| **§8.2** Tenant EMP-1 | **PASS** | Sesión admin coherente |
| **§8.2** Usuarios demo | **PASS** | Claudia, Ricardo, Luis, Jorge usados donde aplica |
| **§8.3** JSON anonimizado | **PASS** | `2026-08-15-integral-erp-ola-b.json` |
| **§8.3** Sin JWT en markdown | **PASS** | |
| **§8.3** UI P0/P1 capturas | **PARCIAL** | Headless Playwright; sin carpeta `evidencias/` por caso |
| **§8.3** Trazabilidad corrida | **RESERVA** | Ver §1.3 — artefacto crudo ≠ informe final |
| **§8.4** Clasificación gaps §6.1 | **PASS** | SKIP/BLOCKED/HEREDADO alineados |
| **§8.5** ≥ 90 % PASS (ejecutar Ola B) | **PASS** | 99/100 = **99 %** excl. SKIP/BLOCKED/HEREDADO en módulos §4.1 |
| **§8.5** 0 FAIL P0 Ola B | **PASS** | Único FAIL es **P1** (`TES-015`) |
| **§8.5** Reviewer | **Este documento** | |

\* Aceptable para corrida incremental si Ola A dejó seeds base; ideal documentar timestamp de `migrate deploy` en próxima corrida.

### 1.2 Orden §9 (Ola B)

Plan: **PAR → INV → CTR → CNT → TES → ADM resto → FIC**.

| Módulo | Orden script `run-ola-b-integral.mjs` | Casos §4.1 en JSON | Observación |
|---|---|---|---|
| PAR | 1.º (API+UI) | 18/18 | Completo |
| INV | 2.º | 16/16 | INV-010 HEREDADO Ola A |
| CTR | 3.º (parcial API; UI mezclada) | 18/18 | CTR-005–007 no listados §4.1 (HEREDADO Ola A baseline) |
| CNT | 4.º | 20/20 | |
| TES | 5.º | 18/18 | |
| ADM resto | 6.º | 20/20 | ADM-009–012/015/022 HEREDADO |
| FIC | 7.º | 10/10 | |

**Conclusión orden:** cumplido en espíritu y secuencia del runner. Opcional §4.1 (CMP/VEN/RBAC/BIL) ejecutado parcialmente al final — correcto según informe.

### 1.3 Reserva de integridad artefactos

| Artefacto | Conteo | Observación |
|---|---|---|
| Informe final `.json` (módulos §4.1) | 99 PASS · 1 FAIL · 7 BLOCKED · 6 SKIP · 7 HEREDADO | Fuente de revisión |
| Tabla resumen `.md` runner | 98 PASS · 8 BLOCKED | **Desfase −1 PASS, +1 BLOCKED** vs JSON (CNT/TES/INV por módulo) |
| `ERP/.qa-tmp/ola-b-integral-results.json` (crudo) | 75 PASS · 9 FAIL · 1 BLOCKED | Corrida anterior o pre-reconciliación; **no** es el informe canónico |
| Script `run-ola-b-integral.mjs` | — | **No incluye** `TES-015`, `CTR-008/009`, `CNT-016`, `ADM-004–006`; esos casos figuran solo en informe reconciliado |

**Veredicto integridad:** el informe final es **usable** como base de gate si se asume reconciliación manual/post-seed no trazada en el script. Para auditoría estricta §8.3, la próxima corrida debe **incorporar TES-015 al runner** y archivar un único JSON sin divergencia crudo/final.

### 1.4 Prioridad encargado (veredicto proyecto §6 ítem 5)

| ID | Resultado informe | ¿Cierra ítem encargado? |
|---|---|---|
| CNT-006 | PASS | Sí — preview centralización |
| CNT-007 | BLOCKED | Parcial — ejecutar no probado (política BD) |
| CNT-008 | PASS | Sí — UI centralización |
| TES-005–010 | PASS salvo **TES-015** | **Parcial** — lectura/conciliación/CXC OK; **crear pago falla** |
| E2E-001 | PENDIENTE (Ola C) | No ejecutado — CMP-001 opcional PASS como gate compras |

---

## 2. TES-015 FAIL — ¿defecto producto vs seed?

| Aspecto | Hallazgo |
|---|---|
| Plan (v1 detalle, v2 §4.1 TES) | P1 · `POST /pagos` → **201** + impacto cuenta corriente |
| Evidencia corrida | Payload `{beneficiario, medio, estado, monto, fecha}` → **500 Internal Server Error** |
| DTO backend (`UpsertPagoDto`) | Campos obligatorios coinciden con payload reportado |
| Contexto mismo entorno | **TES-008** `GET /pagos` 200 · **TES-009** CXC 200 · cartolas/conciliación PASS |
| Skill tesorería | Módulo existe; cobranza R4-18 diferida — **no aplica** a POST pagos |
| Seed | No hay precondición de folio/proforma para crear pago simple; otros endpoints tesorería operan con seed actual |

### Análisis

- **400** sugeriría payload inválido o regla de negocio — no es el caso.
- **500** con DTO mínimo válido, teniendo el mismo tenant/sesión que el resto de TES, apunta a **excepción no controlada** en `createPago` (Prisma, `parseDate`, post-create), no a dato seed faltante.
- **TES-008** valida listado UI+API, no el flujo de escritura; no contradice el FAIL.

### Clasificación

| | |
|---|---|
| **Veredicto** | **Defecto producto P1** |
| No es | Deuda conocida §6.1 / HUERFANOS / SKIP |
| No es | Entorno (API levantada; lecturas OK) |
| No es | Seed insuficiente demostrado |

**Acción:** fix backend `tesoreria.service.createPago` + retest mínimo **TES-015** (idealmente con `proveedorId` seed y sin `movimientoCartolaId` para aislar).

---

## 3. BLOCKED — ¿aceptable?

| ID | Motivo informe | Clasificación revisor | ¿Aceptable gate Ola B? |
|---|---|---|---|
| **CNT-007** | `POST /centralizacion/ejecutar` destructivo — BD compartida | **Entorno + política** — plan §4.1 explícito «solo BD QA» | **Sí** |
| **CNT-016** | Cerrar periodo `2026-08` bloquearía corrida | **Política corrida** | **Sí** |
| **ADM-004** | Crear `EMP-QA` muta seed demo | **Política corrida** (P2) | **Sí** |
| **ADM-005** | Usuario multi-empresa | **Política corrida** (P2) | **Sí** |
| **ADM-006** | `POST /usuarios` | **Política corrida** (P2) | **Sí** |
| **CTR-009** | Sin DEFINITIVA post **CTR-008** (consumió `PRF-SEED-DEF`) | **Datos corrida / orden** — no defecto producto | **Sí** — retest con re-seed o orden inverso |
| **CTR-020** | Sin proforma RECHAZADA en seed corrida | **Datos seed** — gap caso, no regresión | **Sí** — ampliar seed o ejecutar antes de mutaciones |

**Ningún BLOCKED** constituye defecto nuevo Fase 1 ni bloqueo de entorno (API/caída). Todos son **aceptables** para gate Ola B con la deuda documentada de casos destructivos y consumo de seed en corrida única.

---

## 4. Conteo consolidado (JSON canónico, módulos §4.1)

| Métrica | Valor |
|---|---|
| PASS | 99 |
| FAIL | 1 (`TES-015`) |
| BLOCKED | 7 |
| SKIP | 6 |
| HEREDADO | 7 |
| Tasa PASS ejecutar | **99 %** (99/100) |
| Opcional §4.1 extra | +9 PASS, +2 SKIP, +1 HEREDADO (CMP/VEN/RBAC) |

### Defectos y deuda (no FAIL)

| ID / tema | Tipo | Nota |
|---|---|---|
| **TES-015** | **Defecto P1** | Único FAIL abierto |
| CNT-007, CNT-016, ADM-004–006 | Política / entorno | BLOCKED aceptable |
| CTR-009, CTR-020 | Seed / orden corrida | Retest con re-seed |
| INV-014, TES-004, TES-017, CTR-018, ADM-020 | Deuda conocida | SKIP §6.1 |
| INV-010, ADM-009–012, ADM-015, ADM-022 | HEREDADO | Baseline Ola A |
| RBAC-008 | Deuda G8 | PASS deuda — no FAIL |
| ADM-002 | API PASS (`ventaBajoCosto=BLOQUEAR`) | H2; UI headless crudo falló — **no** reclasificar FAIL si API confirma flag |
| VEN-013 | No en Ola B | Retest UI bajo costo sigue pendiente (D16) |

---

## 5. Veredicto

### **`REQUIERE_RETEST`**

**Motivo:** Ola B back-office alcanza **99 %** en casos ejecutables del alcance §4.1 y cumple checklist §8.1/§8.2, pero queda **1 FAIL P1** en escritura de tesorería (`TES-015`) — flujo principal del plan y prerequisito de **E2E-005** (showcase centralización + tesorería).

| Criterio | Estado |
|---|---|
| Gate Ola A (`LISTO_OLA_B`) | Mantenido — sin regresión P0 demostrada |
| Ola B §4.1 ejecutar | **99/100 PASS** |
| 0 FAIL P0 | Cumplido |
| 0 FAIL P1 abierto | **No cumplido** (`TES-015`) |
| BLOCKED aceptables | Cumplido |
| ≥ 90 % plan total v2 | **No** (~50–55 % trazable con opcional pendiente) — criterio piloto completo, no gate Ola B |

**No aplica `BLOQUEADO`** (entorno operativo). **`OLA_B_PARCIAL`** describe cobertura pero no sustituye el gate: el pipeline exige retest antes de Ola C.

---

## 6. ¿Autoriza Ola C (E2E golden)?

**No — condicionada al retest de `TES-015`.**

| Escenario | Autorización |
|---|---|
| **E2E-001** (ALM-COT → OC → aprobación → recepción) | **Condicional** — CMP-001 PASS; riesgo bajo si se limita a compras |
| **E2E-004** (proforma contratistas) | **Condicional** — CTR-022 seed OK; CTR-009/020 BLOCKED no bloquean si E2E usa flujo propio |
| **E2E-005** (centralización + tesorería showcase) | **No** hasta PASS **TES-015** |
| **E2E-002/003/006** (Ola A) | Ya ejecutados parcialmente — capturas/video siguen deuda demo |

**Recomendación:** retest **`TES-015`** → si PASS, emitir addendum **`LISTO_OLA_C`** y arrancar **E2E-001 → E2E-004 → E2E-005** según §9.

---

## 7. Retest mínimo sugerido

| Prioridad | ID | Acción |
|---|---|---|
| **P0 retest** | **TES-015** | Fix `POST /pagos` · payload mínimo DTO + variante con `proveedorId` seed |
| P2 orden | **CTR-009** | Re-seed proformas · ejecutar reversar **antes** de facturar `PRF-SEED-DEF` |
| P2 seed | **CTR-020** | Añadir proforma RECHAZADA al seed o correr en ventana limpia |
| P3 opcional | **CNT-007** | BD QA dedicada o snapshot pre-`ejecutar` |
| P3 opcional | **ADM-004–006** | Ventana aislada si se exigen casos destructivos P2 |
| Deuda demo | **VEN-013**, **ADM-002 UI** | Captura manual bajo costo (H2/D16) |
| Pipeline | Runner | Incorporar TES-015 y casos BLOCKED explícitos al script; un solo JSON final |

**No re-ejecutar** batería Ola B completa salvo regresión en módulo tocado por el fix de pagos.

---

## 8. Referencias cruzadas

| Documento | Relación |
|---|---|
| `2026-08-15-revision-ola-a-cierre.md` | Gate previo sin regresión P0 |
| `2026-08-15-integral-erp-ola-b.json` | Evidencia anonimizada Ola B |
| `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` §4.1, §8, §9 | Alcance y criterios |
| `HUERFANOS-H1-H14.md` | H13 TES-004 SKIP; H11 BIL SKIP |
| `AGENTS.md` | Huecos vigentes — ninguno contradice veredicto |
| `2026-08-15-veredicto-encargado-proyecto.md` §6.5 | Ítem back-office **parcial** por TES-015 |

---

## 9. Addendum post-fix TES-015 (misma fecha)

**Causa raíz:** `estado` inválido (p. ej. `CONFIRMADO`, `REGISTRADO`) propagaba error Prisma → **500**. Valores válidos: `ACTIVO`, `INACTIVO`, `PENDIENTE`, `BORRADOR`.

**Fix:** `parseEstadoGenerico` en `tesoreria.service.ts` → **400** con mensaje claro. Test unitario añadido (Jest **151** tests).

**Runner:** `TES-015` incorporado en `ERP/.qa-tmp/run-ola-b-integral.mjs` con `estado: PENDIENTE`.

**Retest:** [`2026-08-15-integral-erp-ola-b-tes015-retest.md`](2026-08-15-integral-erp-ola-b-tes015-retest.md) — **3 PASS, 0 FAIL** (TES-015 cerrado).

**Gate Ola B:** **`LISTO_OLA_C`** — [`2026-08-15-revision-ola-b-cierre.md`](2026-08-15-revision-ola-b-cierre.md)

---

*Revisión documental. Ejecutor corrida: almahue-qa-runner · Revisor: almahue-qa-reviewer.*
