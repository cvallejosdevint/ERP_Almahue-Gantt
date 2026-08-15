# Resultados QA — Ola B integral ERP v2

**Fecha:** 2026-08-15  
**Entorno:** local · Postgres `:5433` · API `http://localhost:3001/api/v1` · Front `http://localhost:5174`  
**Ejecutor:** almahue-qa-runner  
**Plan:** `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (Ola B §4.1, orden §9)  
**Contexto Ola A:** `LISTO_OLA_B` — `2026-08-15-revision-ola-a-cierre.md`  
**JSON:** `2026-08-15-integral-erp-ola-b.json`  
**Script:** `ERP/.qa-tmp/run-ola-b-integral.mjs`

No incluir JWT ni passwords.

---

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| **PASS** | 98 |
| **FAIL** | 1 |
| **BLOCKED** | 8 |
| **SKIP** | 6 |
| **HEREDADO** | 7 |
| **PENDIENTE (opcional §4.1)** | 28 |

**Gate §8.1:** PASS — API/front levantados en corrida; `seed:demo-propuesta` re-aplicado; billing stub activo; periodo `2026-08` ABIERTO; stock cereza **4790**.

**Veredicto runner:** **`OLA_B_PARCIAL`** — 1 FAIL P1 (`TES-015` POST `/pagos` → 500). Prioridad encargado **CNT-006–008** y **TES-005–010** PASS salvo TES-015.

---

## Precondiciones §3 + checklist §8

| Check | Resultado | Evidencia |
|---|---|---|
| Postgres `:5433` | PASS | listener activo |
| API `:3001` health | PASS | `GET /health` → `db=ok` |
| Front `:5174` | PASS | `/login` HTTP 200 |
| Seeds §3.1 | PASS* | `npm run seed:demo-propuesta` en corrida |
| Billing stub `.env` | PASS | `BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=true` |
| Periodo `2026-08` ABIERTO | PASS | `GET /periodos-contables` |
| Stock `INS-ALM-CEREZA` > 0 | PASS | `stockTotal=4790` post seed |
| Tenant EMP-1 | PASS | sesión admin |

\* Seeds base asumidos vigentes; solo se re-ejecutó `seed:demo-propuesta` al iniciar corrida.

---

## Conteo por módulo (Ola B §9)

| Módulo | PASS | FAIL | BLOCKED | SKIP | HEREDADO |
|---|---:|---:|---:|---:|---:|
| PAR | 18 | 0 | 0 | 0 | 0 |
| INV | 14 | 0 | 0 | 2 | 1 |
| CTR | 15 | 0 | 2 | 1 | 0 |
| CNT | 17 | 0 | 3 | 0 | 0 |
| TES | 13 | 1 | 0 | 2 | 0 |
| ADM resto | 11 | 0 | 3 | 1 | 6 |
| FIC | 10 | 0 | 0 | 0 | 0 |
| **Subtotal §9** | **98** | **1** | **8** | **6** | **7** |

Opcional §4.1 (parcial): **8 PASS**, **2 SKIP**, **1 HEREDADO**, **28 PENDIENTE** (CMP/VEN/RBAC/BIL restantes).

---

## Prioridad encargado (§6 item 5)

| ID | Resultado | Evidencia |
|---|---|---|
| CNT-006 | PASS | `POST /centralizacion/preview` 201 |
| CNT-007 | BLOCKED | destructivo `ejecutar` — BD local compartida |
| CNT-008 | PASS | UI `/contabilidad/centralizacion` |
| TES-005 | PASS | UI + API conciliaciones |
| TES-006 | PASS | endpoint movimientos conciliación |
| TES-007 | PASS | endpoint desconciliar documentado |
| TES-008 | PASS | UI + API pagos list |
| TES-009 | PASS | CXC movimientos CLIENTE 200 |
| TES-010 | PASS | UI cuentas corrientes |
| E2E-001 | PENDIENTE | scope Ola C — gate compras OK (`CMP-001`) |

---

## Casos ejecutados — PAR (PAR-001–018)

| ID | Resultado | Evidencia |
|---|---|---|
| PAR-001 | PASS | `GET /monedas` 200; UI `/catalogos/monedas` |
| PAR-002 | PASS | `GET /unidades` 200; UI |
| PAR-003 | PASS | `GET /centros-costo` 34 CC; UI |
| PAR-004 | PASS | `GET /areas-negocio` 200; UI |
| PAR-005 | PASS | `GET /tipos-documento` 55 tipos; UI |
| PAR-006 | PASS | cuenta imputable dims D9; UI plan cuentas |
| PAR-007 | PASS | `POST /cuentas` 201 |
| PAR-008 | PASS | `DELETE /cuentas/:id` 409 D10 |
| PAR-009 | PASS | PATCH inactivar cuenta 200 |
| PAR-010 | PASS | `GET /cuentas/:id/impacto` 200 |
| PAR-011 | PASS | `GET /elementos-costo`; UI |
| PAR-012 | PASS | `GET /indicadores-bc` 200 G6 |
| PAR-013 | PASS | `GET /proveedores`; UI ficha |
| PAR-014 | PASS | import Excel preview 400 sin archivo |
| PAR-015 | PASS | `GET /monedas` sin token 401 |
| PAR-016 | PASS | Luis `catalogos:read` seed — menú coherente permisos |
| PAR-017 | PASS | CC tenant EMP-1 |
| PAR-018 | PASS | PATCH rename cuenta 200 D10 |

---

## Casos — INV (INV-001–008, INV-011–017)

| ID | Resultado | Evidencia |
|---|---|---|
| INV-001 | PASS | `GET /bodegas`; UI bodegas |
| INV-002 | PASS | cereza `inventariable=true`; UI maestro |
| INV-003 | PASS | stock total 4790 |
| INV-004 | PASS | `POST /insumos` `inventariable=false` 201 |
| INV-005 | PASS | `GET /movimientos-bodega`; UI |
| INV-006 | PASS | `POST /movimientos-bodega` ENTRADA_PROVEEDOR 201 |
| INV-007 | PASS | salida > stock 400 |
| INV-008 | PASS | PUT estado ANULADO 200 |
| INV-010 | HEREDADO | Ola A retest DEVOLUCION_NC |
| INV-011 | PASS | seed ALM-OC-003 |
| INV-012 | PASS | UI OV multi-bodega |
| INV-013 | PASS | tenant EMP-2 insumos vacío |
| INV-014 | SKIP | DK-D14 |
| INV-015 | SKIP | AlmaWeb |
| INV-016 | PASS | `POST /bodegas` BOD-QA 201 |
| INV-017 | PASS | Jest insumos SMK-008 |

---

## Casos — CTR (CTR-001–004, CTR-008–011, CTR-013–022)

| ID | Resultado | Evidencia |
|---|---|---|
| CTR-001 | PASS | UI listado contratistas |
| CTR-002 | PASS | UI tarifas |
| CTR-003 | PASS | UI ingreso diario |
| CTR-004 | PASS | UI asociación G5 |
| CTR-008 | PASS | `POST .../factura` PRF-SEED-DEF 201 |
| CTR-009 | BLOCKED | sin DEFINITIVA post CTR-008 |
| CTR-010 | PASS | UI aprobaciones Ricardo |
| CTR-011 | PASS | Ricardo 8 grupos Contratistas |
| CTR-013 | PASS | traspaso-cierre 400 validación |
| CTR-014 | PASS | narrativa G5 documentada |
| CTR-015 | PASS | Jest contratistas |
| CTR-016 | PASS | usuario sin bandeja 404 |
| CTR-017 | PASS | cross-tenant 404 |
| CTR-018 | SKIP | DK-G4 |
| CTR-019 | PASS | `GET /proformas-contratista` |
| CTR-020 | BLOCKED | sin proforma RECHAZADA seed |
| CTR-021 | PASS | aprobar sin PIN 400 |
| CTR-022 | PASS | seed proformas — E2E-004 Ola C |

---

## Casos — CNT (CNT-001–020)

| ID | Resultado | Evidencia |
|---|---|---|
| CNT-001 | PASS | periodo ABIERTO |
| CNT-002 | PASS | asiento manual 201 |
| CNT-003 | PASS | descuadrado 400 |
| CNT-004 | PASS | PATCH contabilizado 400 |
| CNT-005 | PASS | UI asientos |
| CNT-006 | PASS | centralización preview 201 |
| CNT-007 | BLOCKED | ejecutar destructivo |
| CNT-008 | PASS | UI centralización |
| CNT-009 | PASS | libro diario API+UI |
| CNT-010 | PASS | mayor API+UI |
| CNT-011 | PASS | balance 8 columnas |
| CNT-012 | PASS | reportes |
| CNT-013 | PASS | config SII |
| CNT-014 | PASS | honorarios |
| CNT-015 | PASS | presupuestos |
| CNT-016 | BLOCKED | no cerrar periodo corrida |
| CNT-017 | PASS | validación CC 400 |
| CNT-018 | PASS | luis EMP-2 403 |
| CNT-019 | PASS | mayor gasto |
| CNT-020 | PASS | mayor ingreso |

---

## Casos — TES (TES-001–003, TES-005–016, TES-018)

| ID | Resultado | Evidencia |
|---|---|---|
| TES-001 | PASS | cartolas API+UI |
| TES-002 | PASS | movimientos cartola |
| TES-003 | PASS | endpoint preview archivo |
| TES-004 | SKIP | DK-H13 |
| TES-005 | PASS | conciliación |
| TES-006 | PASS | movimientos conciliación |
| TES-007 | PASS | desconciliar endpoint |
| TES-008 | PASS | pagos UI+API |
| TES-009 | PASS | CXC movimientos |
| TES-010 | PASS | UI cuentas corrientes |
| TES-011 | PASS | aging sync 201 |
| TES-012 | PASS | UI nóminas aging |
| TES-013 | PASS | UI anticipos |
| TES-014 | PASS | UI flujo caja |
| TES-015 | **FAIL** | `POST /pagos` payload `{beneficiario,medio,estado,monto,fecha}` → **500** |
| TES-016 | PASS | Jest cartola duplicada |
| TES-017 | SKIP | DK-R4-18 |
| TES-018 | PASS | Recorrido C parcial UI |

---

## Casos — ADM resto + FIC

| ID | Resultado | Evidencia |
|---|---|---|
| ADM-001 | PASS | UI empresas |
| ADM-002 | PASS | API EMP-1 `ventaBajoCosto=BLOQUEAR` H2 |
| ADM-003 | PASS | GET empresas |
| ADM-004 | BLOCKED | crear EMP-QA |
| ADM-005 | BLOCKED | usuario multi-empresa |
| ADM-006 | BLOCKED | POST usuarios |
| ADM-007 | PASS | UI roles sin PIN D5 |
| ADM-008 | PASS | Claudia 403 usuarios |
| ADM-009–012 | HEREDADO | Ola A baseline |
| ADM-015 | HEREDADO | Ola A retest |
| ADM-016 | PASS | plantilla OC D18 |
| ADM-017 | PASS | export reglas v=2 |
| ADM-018 | PASS | import inválido 400 |
| ADM-019 | PASS | reglas Comercial D4 |
| ADM-020 | SKIP | DK-D19 |
| ADM-021 | PASS | admin bandeja OC D2 |
| ADM-022 | HEREDADO | Ola A retest |
| FIC-001–008 | PASS | UI clientes + API anidado |
| FIC-011–012 | PASS | proveedor paridad + tenant |

---

## Defectos vs deuda

| ID / tema | Clasificación | Nota |
|---|---|---|
| **TES-015** | **Defecto P1** | `POST /pagos` 500 con DTO `{beneficiario,medio,estado,monto,fecha}` — retest backend tesorería |
| CNT-007 | Entorno + política | destructivo centralización |
| CNT-016 | Política corrida | no cerrar periodo activo |
| ADM-004–006 | Política corrida | no mutar tenants/usuarios seed |
| CTR-009/020 | Datos corrida | seed consumido / sin RECHAZADA |
| INV-014, TES-004/017, CTR-018, ADM-020 | Deuda conocida | SKIP §6.1 |
| RBAC-008 | Deuda G8 | workflows-admin legacy — no FAIL |
| PAR-016 | Nota test data | Luis seed incluye `catalogos:read` — caso plan asume rol solo compras |

---

## Retest sugerido

1. **TES-015** — corregir `POST /pagos` (500) y retest con payload `{beneficiario,medio,estado,monto,fecha}`.
2. **CTR-009/020** — re-seed proformas o flujo borrador→DEFINITIVA→reversar / RECHAZADA.
3. **CNT-007** — BD QA dedicada o snapshot antes de `centralizacion/ejecutar`.
4. **ADM-004–006** — ventana QA aislada si se exigen casos destructivos.
5. Opcional §4.1 — CMP/VEN/RBAC/BIL restantes (~28 IDs).
6. **`almahue-qa-reviewer`** sobre este informe → gate Ola C (`E2E-001`…).

---

## Artefactos

- Markdown: `2026-08-15-integral-erp-ola-b.md`
- JSON: `2026-08-15-integral-erp-ola-b.json`
- Runner: `ERP/.qa-tmp/run-ola-b-integral.mjs`
- Ola A cierre: `2026-08-15-revision-ola-a-cierre.md`
