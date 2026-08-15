# Plan de pruebas integral — ERP Almahue v2

**Fecha:** 2026-08-15  
**Versión:** 2.0 (Fase 3 pipeline QA)  
**Plan anterior:** `PLAN-PRUEBAS-INTEGRAL-ERP-COMPLETO-2026-08-15.md` v1.0 — **no editar**  
**Análisis integridad:** `resultados/2026-08-15-analisis-integridad-qa-v1.md` — veredicto **REQUIERE_RETRABAJO**  
**Referencias:** `AGENTS.md`, `HUERFANOS-H1-H14.md`, `DEMO-PROPUESTA-LOCAL.md`, `PLAN-PRUEBAS-APROBACIONES.md`, `REUNION-CHECKLIST-APROBACION-COMERCIAL.md`, `reunion6-minuta-2026-08-06.md`.

**Convención de IDs:** prefijo módulo + tres dígitos (`ADM-001`, `VEN-014`, …). Mapa legados en §10.3.

**Columnas de ejecución v2:**

| Columna | Significado |
|---|---|
| **Prioridad** | P0 bloquea demo/salida · P1 flujo principal · P2 profundidad |
| **Estado ejec.** | `EJECUTAR` · `HEREDADO` · `SKIP` · `BLOCKED` |
| **Ola** | A retest P0 · B módulos sin cobertura · C E2E ALM-* · — transversal |

---

## 1. Resumen ejecutivo y alcance

### 1.1 Objetivo v2

Ejecutar el plan integral con **trazabilidad**, **menos duplicados** y **oleadas ordenadas**. v2 corrige inconsistencias del análisis v1 (commit OV, Emitir obsoleto, baseline parcial, HUERFANOS vs deuda Fase 5).

### 1.2 Cambios respecto a v1

| Tema | v1 | v2 |
|---|---|---|
| Commit OV Emitir | `2035773` (ambiguo repo) | **`ERP/erp_front` commit `2035773`**, branch `feature/backend-core` — «Fase 1: unificar OV con wizard Emitir» |
| Emitir mezcla COTIZ/NP/OC | Casos negativos + DK-EMITIR | **Código restringe** (`EmitirDocumentoPage`); casos UI validan solo FACTURA/NC/ND/GUIA — **no** casos «mezcla permitida» |
| Baseline ~36 % | No distinguido | Bloque **HEREDADO** (~41 casos) — no re-ejecutar salvo regresión |
| Orden | Fases 0–7 lineales | **Ola A → B → C** con retest mínimo §9 del análisis |
| HUERFANOS H1–H8 | Mezclado con DEBT Fase 5 | Tabla §1.8 — **PASS esperado**, no FAIL por deuda obsoleta |
| Duplicados lookup/simulador | FIC-009/010, ADM-013/014, etc. | Consolidados — ver §12 |

### 1.3 Alcance por entorno

| Entorno | URL | Alcance v2 | Restricciones |
|---|---|---|---|
| **Local** | Front `:5174` · API `:3001/api/v1` | Ola A obligatoria; Ola B según tiempo; Ola C con seed demo | Postgres `:5433`; seeds §3.1 |
| **Prod piloto** | `45.7.229.46/almahue-erp/` | Solo E2E-008 + SMK API | **BLOCKED** hasta migrate H14 |

### 1.4 Decisiones Reu6 (D1–D20) — foco QA

Sin cambios sustantivos vs v1 §1.3. **v2 añade:** D4 cadena OV = código listo; `comercialRequiereAprobacion=true` en seed demo — **no SKIP** por DK-D4 salvo decisión reunión documentada en informe.

### 1.5 Fase 1 OV — wizard Emitir unificado

| Atributo | Valor |
|---|---|
| **Repositorio** | `ERP/erp_front` |
| **Branch** | `feature/backend-core` |
| **Commit** | `2035773` |
| **Comportamiento** | `/comercial/emitir` solo **FACTURA / NC / ND / GUIA**; producto inventariable desde **OV confirmada** (`contexto=ov` o selección OV paso 1) |
| **Casos** | VEN-021, VEN-023–026 (consolidado vs v1) |
| **Obsoleto** | Retest UI-E2 (14/08) que esperaba COTIZ/NP/OC en Emitir — **descartar como evidencia** |

### 1.6 Conteo casos v2

| Prefijo | Módulo | v1 | v2 | Δ |
|---|---|---:|---:|---:|
| SMK | Smoke | 8 | 8 | 0 |
| ADM | Administración | 22 | 20 | −2 |
| PAR | Parametrización | 18 | 18 | 0 |
| CMP | Compras | 24 | 23 | −1 |
| VEN | Ventas / comercial | 32 | 31 | −1 |
| INV | Inventario | 18 | 16 | −2 |
| CTR | Contratistas | 22 | 21 | −1 |
| CNT | Contabilidad | 20 | 20 | 0 |
| TES | Tesorería | 18 | 18 | 0 |
| FIC | Ficha contraparte | 12 | 10 | −2 |
| BIL | Billing stub | 8 | 7 | −1 |
| RBAC | Seguridad / tenant | 15 | 15 | 0 |
| E2E | Golden path ALM-* | 8 | 8 | 0 |
| **Total** | | **225** | **215** | **−10** |

| Métrica | Valor |
|---|---|
| Casos `EJECUTAR` (nueva corrida) | **~174** |
| Casos `HEREDADO` (baseline confiable) | **~41** |
| Casos `SKIP` / `BLOCKED` documentados | **~14** |

### 1.7 Oleadas de ejecución

```text
Ola A — Retest P0 (gate salida v2)
  Precondiciones §3 + checklist runner §8
  → SMK-001–008
  → Retest mínimo análisis §9 (excl. HEREDADO salvo regresión declarada)
  → Duración estimada: 3–4 h (1 QA) · 1,5–2 h (2 QA API/UI paralelo)

Ola B — Módulos sin cobertura (~36 % evidencia previa)
  → PAR, CNT, TES, CTR profundo, ADM restante, INV movimientos UI
  → Duración: 4–6 h

Ola C — E2E golden ALM-*
  → seed:demo-propuesta obligatorio
  → E2E-006 → E2E-001 → E2E-002 → E2E-003 → E2E-004 → E2E-005
  → Duración: ~1,5 h (+ E2E-007 opcional 3 h sin seed)

Regresión post-deploy / hotfix
  → Re-ejecutar HEREDADO del módulo afectado + Ola A subset
```

### 1.8 Baseline HEREDADO — no re-ejecutar salvo regresión

Fuente: `2026-08-12-veredicto-unificado.md` (20/20 aprobaciones), Fase 5 post-fix OV API, `qa-retest-seed-results.json`.

| Bloque | IDs | Evidencia | Re-ejecutar si |
|---|---|---|---|
| Aprobaciones seed 20/20 | ADM-009–011, ADM-012 (S1/S5/S6), CMP-004–008, CTR-005–007 (API bandeja) | `ERP/.qa-tmp/qa-retest-seed.mjs` | Cambio reglas/PIN/AdminConcepto |
| OV API core post-fix | VEN-002–008, VEN-016–018 | Fase 5 + scripts API | Cambio stock/OV/convertir |
| Smoke API parcial | SMK-001–006 | Informes 12–14/08 | migrate/seed/health |
| Jest regresión | SMK-008 | 136 tests PASS | Cambio backend testado |
| AdminConcepto API | ADM-010–011 (parcial AC) | Spec AC PASS | Cambio JWT módulos |

**Ola A sigue ejecutando** casos con evidencia UI pendiente o post-fix sin informe dedicado (VEN-021–026, RBAC-001/007/014, ADM-022, E2E-002/003/006).

### 1.9 HUERFANOS H1–H8 vs deuda Fase 5

| ID | Tema | Estado código | Casos v2 | Clasificación QA |
|---|---|---|---|---|
| H1 | Productor lookup | **Listo** | VEN-031 | PASS esperado — **no** DEBT DK-D7 |
| H2 | UI `ventaBajoCosto` | **Listo** | ADM-002, VEN-013 | PASS esperado — retest UI ADM-002 |
| H3 | Aprobación OV | **Listo (off)** | VEN-009–012 | PASS con flag true en seed; SKIP solo si reunión desactiva |
| H4 | pantallas-permisos | **Listo** | RBAC-007 | PASS esperado — **no** gap Sidebar |
| H5 | Print ficha | **Listo** | FIC-006 | PASS esperado |
| H6 | Flag inventariable | **Listo** | INV-002, INV-004 | PASS esperado |
| H7 | NC reingreso bodega | **Listo** | INV-010 | **P0 Ola A** — retest obligatorio |
| H8 | Guías despacho UI | **Listo** | VEN-026 | **P0 Ola A** |
| H9–H13 | SMTP, Acepta, Excel, comparador | Externo/diferido | RBAC-009, TES-004, CMP-024 | SKIP válido |
| H14 | Prod migrate | Doc listo | E2E-008, SMK prod | BLOCKED prod |

### 1.10 Tiempo estimado v2

| Oleada | Duración |
|---|---|
| Ola A (retest P0) | 3–4 h |
| Ola B (back-office) | 4–6 h |
| Ola C (E2E ALM-*) | 1,5 h (+ 3 h E2E-007 opcional) |
| **Sesión mínima viable** | **½ día** (Ola A + E2E-006) |
| **Sesión completa** | **1–1,5 días** (1 QA) |

---

## 2. Matriz módulo × tipo de prueba

Leyenda: **●** obligatorio v2 · **○** Ola B/C · **—** no aplica · **H** HEREDADO baseline · **S** SKIP

| Módulo | API | UI | E2E | Jest | RBAC | Tenant | Ola | Notas |
|---|---|---|---|---|---|---|---|---|
| Smoke | ● | ● | ○ | ● | ○ | ● | A | Bloquea todo si FAIL |
| Admin | ● | ● | ○ | ● | ● | ● | A/B | ADM-009–012 H; ADM-022 A |
| Parametrización | ● | ● | ○ | ● | ● | ● | B | 17 % cobertura previa |
| Compras | ● | ● | ● | ● | ● | ● | A/C | CMP-004–008 H; CMP-012–013 A |
| Ventas | ● | ● | ● | ● | ● | ● | A/C | VEN-002–018 H; VEN-021–026 A |
| Inventario | ● | ● | ● | ● | ○ | ● | A/B | INV-010 A |
| Contratistas | ● | ● | ○ | ● | ● | ● | B/C | 18 % cobertura previa |
| Contabilidad | ● | ● | ○ | ● | ● | ● | B | 10 % cobertura previa |
| Tesorería | ● | ● | ○ | ● | ● | ● | B | TES-004 S |
| Ficha | ● | ● | ○ | — | ○ | ● | B | Lookup → VEN-029–031 |
| Billing | ● | ○ | ○ | ● | ○ | ● | A | BIL-001–002 A |
| Seguridad | ● | ● | ○ | ○ | ● | ● | A | RBAC-001/007/014 A |
| E2E | — | — | ● | — | ○ | ● | C | seed demo obligatorio |

---

## 3. Precondiciones

### 3.1 Infraestructura local (obligatorio Ola A)

```bash
cd ERP/erp_back
npx prisma migrate deploy
npm run seed
npm run seed:aprobaciones-f2
npm run seed:demo-propuesta
```

**Migraciones críticas:** `20260813230000_stock_ov_ficha`, `20260814180000_comercial_aprobacion_ov`, `20260814180000_tipo_doc_nd_guia`, `20260815200000_huerfanos_ficha_inventario`.

### 3.2 Variables `.env` API

```env
BILLING_GATEWAY_ENABLED=true
BILLING_STUB_INLINE=true
```

Sin esto → **BIL-*** = BLOCKED.

### 3.3 Health y sesión

| Check | Comando / acción | Esperado |
|---|---|---|
| API | `GET /health` | `status: ok`, `db: ok` |
| Front | Abrir `/login` | Formulario carga |
| Periodo | `GET /periodos-contables` | `2026-08` ABIERTO |
| Stock demo | `GET /insumos/INS-ALM-CEREZA/stock-bodegas` | `BOD-ALM-FRIG` qty > 0 **sin** movimiento manual |

### 3.4 Usuarios demo

| Rol | Email | Password | Uso |
|---|---|---|---|
| Admin | `admin@almahue.local` | `Admin123!` | Smoke, E2E, simulador |
| Claudia | `cvargas@almahue.cl` | `demo123` | AdminConcepto Compras |
| Ricardo | `rmunoz@almahue.cl` | `demo123` | AdminConcepto Contratistas |
| Luis | `lherrera@almahue.cl` | `demo123` | Alta OC (solicitante cadena) |
| Jorge | `jsanchez@almahue.cl` | `demo123` | Bandeja OC + PIN |
| María | `mgonzalez@almahue.cl` | `demo123` | Suplente / bandeja |
| PIN | — | `4821` | Pool aprobadores |

**AdminConcepto:** re-login tras cambiar `adminConceptoModulos` (ADM-022).

### 3.5 Datos seed ALM-* (`DEMO-PROPUESTA-LOCAL.md`)

| Folio | Uso |
|---|---|
| `ALM-COT-001` | CMP cotización → OC · E2E-001 |
| `ALM-OC-001` | CMP aprobación pendiente |
| `ALM-OC-003` | CMP recepción + registro |
| `ALM-OV-002` | VEN aprobación OV · E2E-002 |
| `ALM-OV-004` | VEN stock → factura · E2E-003 |
| `ALM-FAC-101` | BIL stub DTE |

Empresa `EMP-1`: `comercialRequiereAprobacion=true`, umbral `$500.000`, `ventaBajoCosto=BLOQUEAR`.

### 3.6 Prod

E2E-008 BLOCKED hasta checklist H14. No seed demo en prod.

---

## 4. Tabla maestra de ejecución por ola

Formato: **ID · Prioridad · Estado · Evidencia esperada · Script/comando**

### 4.0 Ola A — Retest P0 (obligatorio)

| ID | P | Estado | Evidencia esperada | Script / comando |
|---|---|---|---|---|
| SMK-001 | P0 | EJECUTAR | JSON health `db: ok` | `curl -s http://localhost:3001/api/v1/health` |
| SMK-002 | P0 | EJECUTAR | Login 200, permisos sin token en log | `POST /auth/login` |
| SMK-003 | P0 | EJECUTAR | `empresaId`, `bandejaModulos` | `GET /auth/me` |
| SMK-004 | P0 | EJECUTAR | Solo tenant EMP-1 | `GET /clientes` + `X-Empresa-Id: EMP-1` |
| SMK-005 | P0 | EJECUTAR | Periodo 2026-08 ABIERTO | `GET /periodos-contables` |
| SMK-006 | P0 | EJECUTAR | Stock cereza > 0 | `GET /insumos/INS-ALM-CEREZA/stock-bodegas` |
| SMK-007 | P0 | EJECUTAR | Captura Dashboard post-login | UI manual |
| SMK-008 | P0 | EJECUTAR | Exit 0 ~136 tests | `cd ERP/erp_back && npm test` |
| ADM-009 | P0 | HEREDADO | Claudia ve Compras, no Usuarios | `qa-retest-seed.mjs` · UI si regresión |
| ADM-010 | P0 | HEREDADO | 12 grupos Compras API | idem |
| ADM-011 | P0 | HEREDADO | `GET /usuarios` 403 Claudia | idem |
| ADM-012 | P0 | HEREDADO | Simulador S1/S5/S6 cadenas correctas | UI `/admin/aprobaciones` simulador |
| ADM-015 | P1 | EJECUTAR | Modal `APROBADOR_SIN_BANDEJA` | UI manual |
| ADM-022 | P0 | EJECUTAR | Captura JWT `adminConceptoModulos` post re-login | UI tras cambio reglas |
| CMP-004 | P0 | HEREDADO | OC $2,5M EMITIDO Luis | seed / retest seed |
| CMP-005 | P0 | HEREDADO | OC en bandeja Jorge | idem |
| CMP-006 | P0 | HEREDADO | `ALM-OC-001` APROBADO PIN | idem |
| CMP-007 | P0 | HEREDADO | María ve bandeja | idem |
| CMP-008 | P0 | HEREDADO | Usuario fuera cadena no ve OC | idem |
| CMP-012 | P0 | EJECUTAR | `matchOk: true` ALM-OC-003 | API `POST /registros-compra` |
| CMP-013 | P0 | EJECUTAR | `matchOk: false` monto distinto | API mismo endpoint |
| VEN-002 | P0 | HEREDADO | OV PRODUCTO 201 BORRADOR | Fase 5 API / script OV |
| VEN-003 | P0 | HEREDADO | Línea SERVICIO 201 | idem |
| VEN-004 | P0 | HEREDADO | Línea FLETE 201 | idem |
| VEN-005 | P0 | HEREDADO | Confirmar 400 stock insuficiente | idem |
| VEN-006 | P0 | HEREDADO | Confirmar OK + SALIDA_VENTA | idem |
| VEN-007 | P0 | HEREDADO | Stock decrementado (incl. coherencia INV) | idem |
| VEN-008 | P0 | HEREDADO | Splits multi-bodega OK | idem |
| VEN-009 | P0 | EJECUTAR | `PENDIENTE_APROBACION` OV $800k | API + flag true |
| VEN-010 | P0 | EJECUTAR | `ALM-OV-002` AUTORIZADA PIN UI | `/comercial/aprobaciones` |
| VEN-011 | P0 | EJECUTAR | OV $3,8M dos pasos PIN | checklist comercial caso B |
| VEN-012 | P1 | EJECUTAR | Omite auto-aprobación solicitante | checklist caso C |
| VEN-016 | P0 | HEREDADO | convertir FACTURA desde OV | API |
| VEN-017 | P0 | HEREDADO | 400 lock cantidad factura OV | API |
| VEN-018 | P0 | HEREDADO | 200 cambio precio factura OV | API |
| VEN-021 | P0 | EJECUTAR | Captura selector: solo FACTURA/NC/ND/GUIA (commit `2035773`) | UI `/comercial/emitir` |
| VEN-023 | P0 | EJECUTAR | Líneas precargadas `ALM-OV-004` | UI `contexto=ov` |
| VEN-024 | P0 | EJECUTAR | Producto bloqueado; precio editable | UI Emitir |
| VEN-025 | P1 | EJECUTAR | SERVICIO texto libre sin stock | UI Emitir |
| VEN-026 | P0 | EJECUTAR | Guía GUIA listada H8 | UI `/comercial/guias-despacho` |
| VEN-029 | P0 | EJECUTAR | `cliente: true` lookup | `GET /lookup-rut?rut=` |
| VEN-030 | P0 | EJECUTAR | `proveedor: true` | idem |
| VEN-031 | P0 | EJECUTAR | `productor: true`, `productores[]` H1 | RUT seed productor |
| RBAC-001 | P0 | EJECUTAR | 404/403 doc EMP-2 | API post-fix RB1 |
| RBAC-007 | P0 | EJECUTAR | Captura catálogo = Sidebar H4 | UI admin roles |
| RBAC-014 | P0 | EJECUTAR | `GET /aprobaciones-ov` 200 designado | API bandeja Comercial |
| INV-010 | P0 | EJECUTAR | Movimiento `DEVOLUCION_NC` + delta H7 | API/UI post NC contabilizada |
| BIL-001 | P0 | EJECUTAR | Folio stub `ALM-FAC-101` | Contabilizar API |
| BIL-002 | P0 | EJECUTAR | Disclaimer stub visible | UI Emitir → contabilizar |
| E2E-002 | P0 | EJECUTAR | Secuencia capturas ALM-OV-002 → stock | `DEMO-PROPUESTA-LOCAL.md` §4 |
| E2E-003 | P0 | EJECUTAR | ALM-OV-004 → FAC-101 stub | idem paso 7 |
| E2E-006 | P0 | EJECUTAR | Demo 15 min completa | idem §4 íntegro |

### 4.1 Ola B — Módulos sin cobertura (P1/P2)

Casos restantes no listados en §4.0 como HEREDADO ni SKIP. Ejecutar por módulo en orden:

**ADM (restante):** ADM-001–008, ADM-013–014 → cubiertos por ADM-012; ADM-016–021 — P1/P2  
**PAR:** PAR-001–018 — P1 (plan cuentas PAR-006–010 P1)  
**CMP (restante):** CMP-001–003, CMP-009–011, CMP-014–021, CMP-023 — P1  
**VEN (restante):** VEN-001, VEN-013–015, VEN-019–020, VEN-027–028, VEN-032 — P1  
**INV:** INV-001–008, INV-011–017 — P1 (INV-014 SKIP D14)  
**CTR:** CTR-001–004, CTR-008–011, CTR-013–022 — P1 (CTR-018 SKIP G4)  
**CNT:** CNT-001–020 — P1 (CNT-007 destructivo — solo BD QA)  
**TES:** TES-001–003, TES-005–016, TES-018 — P1 (TES-004 SKIP H13, TES-017 SKIP)  
**FIC:** FIC-001–008, FIC-011–012 — P1  
**BIL:** BIL-003–007 — P1 (BIL-006/007 SKIP)  
**RBAC:** RBAC-002–006, RBAC-008–013, RBAC-015 — P1  

### 4.2 Ola C — E2E golden

| ID | P | Estado | Evidencia | Script |
|---|---|---|---|---|
| E2E-001 | P0 | EJECUTAR | Video/capturas ALM-COT → OC → apr → recepción | Manual / `run-e2e-manual.mjs` |
| E2E-002 | P0 | — | Ver §4.0 | — |
| E2E-003 | P0 | — | Ver §4.0 | — |
| E2E-004 | P1 | EJECUTAR | Proforma → PIN → factura | Seed contratistas |
| E2E-005 | P1 | EJECUTAR | Centralización + tesorería showcase | Manual |
| E2E-006 | P0 | — | Ver §4.0 | — |
| E2E-007 | P2 | EJECUTAR | Greenfield sin seed | `PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md` |
| E2E-008 | P0 | BLOCKED | SMK prod post H14 | Prod tras deploy |

---

## 5. Casos por módulo (detalle Given/When/Then)

Prioridad y estado en cabecera de cada subsección. Casos eliminados en v2 — ver §12.

### 5.1 Smoke (SMK) — 8 casos · Ola A

Sin cambios sustantivos vs v1 §4.1. Todos P0 `EJECUTAR` salvo que SMK-001–006 pueden marcarse HEREDADO si corrida &lt;24 h y mismo commit.

### 5.2 Administración (ADM) — 20 casos (−2)

| ID | P | Estado | Tipo | Given | When | Then |
|---|---|---|---|---|---|---|
| ADM-001 | P2 | EJECUTAR | UI | Admin | `/admin/empresas` | Listado seed |
| ADM-002 | P1 | EJECUTAR | UI/API | Admin | Editar flags EMP-1 H2 | Guardado OK |
| ADM-003 | P2 | EJECUTAR | API | Admin | `GET /empresas` | Solo accesibles |
| ADM-004 | P2 | EJECUTAR | UI | Admin | Crear `EMP-QA` | Selector header |
| ADM-005 | P2 | EJECUTAR | UI | Admin | Usuario 2 empresas | Selector login |
| ADM-006 | P2 | EJECUTAR | API | Admin | `POST /usuarios` | 201 tenant OK |
| ADM-007 | P1 | EJECUTAR | UI | Admin | Rol sin PIN en rol D5 | Guardado OK |
| ADM-008 | P1 | EJECUTAR | API | Rol limitado | `GET /usuarios` | 403 |
| ADM-009 | P0 | HEREDADO | UI | Claudia | `/admin/aprobaciones` | Solo Compras |
| ADM-010 | P0 | HEREDADO | API | Claudia | `GET /grupos-aprobacion` | 12 Compras |
| ADM-011 | P0 | HEREDADO | API | Claudia | `GET /usuarios` | 403 |
| ADM-012 | P0 | HEREDADO | UI | Admin | Simulador **S1** Luis $200k, **S5** $3M, **S6** Diego $400k CTR | Cadenas Jorge/Claudia/Pablo |
| ADM-015 | P1 | EJECUTAR | UI | Admin | Aprobador sin bandeja en escala | Modal `APROBADOR_SIN_BANDEJA` |
| ADM-016 | P1 | EJECUTAR | UI | Admin | Plantilla OC D18 | Preview HTML |
| ADM-017 | P2 | EJECUTAR | API | Admin | Export reglas JSON | version 1 |
| ADM-018 | P2 | EJECUTAR | API | Admin | Import aprobador inválido | Error claro |
| ADM-019 | P1 | EJECUTAR | UI | Admin | Módulo Comercial reglas | Grupos editables D4 |
| ADM-020 | P2 | SKIP | UI | Sin MSAL | Botón Microsoft | Deshabilitado DK-D19 |
| ADM-021 | P2 | EJECUTAR | API | Admin master | Aprobar OC ajena D2 | 200 + advertencia |
| ADM-022 | P0 | EJECUTAR | UI | Admin cambia AdminConcepto | Re-login | JWT actualizado |

**Eliminados v2:** ADM-013, ADM-014 → consolidados en ADM-012.

### 5.3 Parametrización (PAR) — 18 casos · Ola B

Igual v1 §4.3. PAR-006–010 P1 (D9/D10). PAR-016 P1 RBAC menú.

### 5.4 Compras (CMP) — 23 casos (−1)

Igual v1 §4.4 salvo:

| ID | P | Estado | Nota |
|---|---|---|---|
| CMP-004–008 | P0 | HEREDADO | Cadena OC seed 20/20 |
| CMP-012–013 | P0 | EJECUTAR | Match 3 vías Ola A |
| CMP-024 | P2 | SKIP | H10 comparador 3 cotiz |

**Eliminado v2:** CMP-022 → cubierto por E2E-001 (mismo flujo ALM-COT-001).

### 5.5 Ventas (VEN) — 31 casos (−1)

| ID | P | Estado | Nota |
|---|---|---|---|
| VEN-002–008 | P0 | HEREDADO | OV API core |
| VEN-009–012 | P0 | EJECUTAR | Aprobación OV — **no SKIP** con seed flag true |
| VEN-013 | P1 | EJECUTAR | Bloqueo bajo costo H2 |
| VEN-016–018 | P0 | HEREDADO | Factura desde OV API |
| VEN-021 | P0 | EJECUTAR | Solo FACTURA/NC/ND/GUIA — **incluye** verificación sin COTIZ/NP/OC |
| VEN-023–026 | P0/P1 | EJECUTAR | Emitir contexto OV + guías H8 |
| VEN-029–031 | P0 | EJECUTAR | Lookup H1/D7 — canonical API |

**Eliminados v2:** VEN-022 (duplicado VEN-021).

### 5.6 Inventario (INV) — 16 casos (−2)

| ID | P | Estado | Nota |
|---|---|---|---|
| VEN-007 | — | — | Coherencia stock post-OV (antes INV-009) |
| INV-010 | P0 | EJECUTAR | NC reingreso H7 |
| INV-014 | P2 | SKIP | D14 tránsito |
| INV-015 | P2 | SKIP | AlmaWeb externo |

**Eliminados v2:** INV-009 (duplicado VEN-007), INV-018 (paso 1 E2E-006).

### 5.7 Contratistas (CTR) — 21 casos (−1)

CTR-005–007 HEREDADO parcial (API). CTR-018 SKIP G4.

**Eliminado v2:** CTR-012 → ver ADM-012 S6.

### 5.8–5.12 CNT, TES, FIC, BIL, RBAC

Sin reducción de conteo vs v1 salvo:

**FIC (−2):** FIC-009, FIC-010 eliminados → VEN-029, VEN-031.  
**BIL (−1):** BIL-008 eliminado → VEN-026. BIL-006/007 SKIP.

**RBAC:** RBAC-001, 007, 014 P0 Ola A. RBAC-008 deuda G8. RBAC-009 SKIP H9.

### 5.13 E2E — 8 casos · Ola A/C

Sin cambios de ID. E2E-002/003/006 en Ola A; E2E-001/004/005 en Ola C.

---

## 6. Criterios PASS / FAIL / BLOCKED / SKIP / HEREDADO

| Estado | Definición |
|---|---|
| **PASS** | Then cumplido con evidencia |
| **FAIL** | No cumple y no está en deuda §6.1 |
| **BLOCKED** | Entorno (migrate, seed, API, prod H14) |
| **SKIP** | Gap documentado — no regresión |
| **HEREDADO** | Baseline confiable §1.8 — registrar «sin re-ejecución» salvo regresión |

### 6.1 Gaps conocidos (actualizado v2)

| Ref | Tema | Casos | Nota v2 |
|---|---|---|---|
| DK-D4 | Flag comercial off por reunión | VEN-009–012 | SKIP solo si decisión explícita en informe |
| DK-EMITIR | Wizard Emitir | VEN-021 | **Cerrado en código** `2035773`; PASS tras Ola A UI |
| DK-D7 / H1 | Productor | VEN-031 | **Listo** — no DEBT |
| DK-D11 / H4 | pantallas-permisos | RBAC-007 | **Listo** — PASS esperado |
| DK-D16 / H2 | ventaBajoCosto | ADM-002, VEN-013 | **Listo** UI |
| DK-D14 | Tránsito venta | INV-014 | SKIP |
| DK-D20 / H14 | Prod migrate | E2E-008 | BLOCKED |
| DK-DTE / H11 | GoSocket real | BIL-007 | SKIP |
| DK-G9 | SMTP PIN | RBAC-009 | SKIP |
| DK-H10 | 3 cotiz comparativas | CMP-024 | SKIP |
| DK-H13 | Excel cartolas | TES-004 | SKIP |
| DK-R4-18 | Cobranza | TES-017 | SKIP |
| DK-G4 | Ingreso diario demo | CTR-018 | SKIP |
| DK-G5 | Traspaso narrativa | CTR-014 | SKIP narrativa |
| DK-G8 | workflows-admin | RBAC-008 | Deuda — no FAIL |
| DK-D19 | SSO Microsoft | ADM-020 | SKIP sin `.env` |
| DK-G10 | NP legacy showcase | — | No mezclar Recorrido B |

### 6.2 Severidad defectos

P0 demo/tenant/stock/asiento · P1 flujo principal · P2 menor · P3 cosmético.

---

## 7. Evidencias requeridas

| Tipo | Evidencia mínima | Almacenamiento |
|---|---|---|
| API | JSON anonimizado sin JWT | `qa/resultados/YYYY-MM-DD-integral-erp.json` |
| UI P0/P1 | Captura + URL + usuario | `qa/resultados/evidencias/` |
| E2E | Secuencia capturas o video | Idem |
| HEREDADO | Referencia artefacto baseline + fecha | Columna Notas informe |
| Jest | Exit 0 + log si falla | Terminal / CI |

Plantilla: `qa/resultados/PLANTILLA.md`.

---

## 8. Checklist integridad runner (obligatorio)

El ejecutor **DEBE** cumplir antes y durante la corrida (fuente: análisis integridad §8).

### 8.1 Entorno

- [ ] Postgres `:5433`; API `:3001`; front `:5174`
- [ ] `npx prisma migrate deploy` sin pendientes (4 migraciones §3.1)
- [ ] `npm run seed` + `npm run seed:aprobaciones-f2` + `npm run seed:demo-propuesta`
- [ ] `.env`: `BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=true`
- [ ] Periodo `2026-08` ABIERTO; stock INS-ALM-CEREZA > 0 sin movimiento manual

### 8.2 Sesión y usuarios

- [ ] Tenant `EMP-1` en header y sesión
- [ ] OC solicitante **Luis**, aprobador **Jorge** + PIN `4821`
- [ ] AdminConcepto Claudia/Ricardo: **re-login** tras cambios reglas (ADM-022)
- [ ] No usar admin como solicitante OC en prueba cadena

### 8.3 Evidencia

- [ ] JSON por corrida en `qa/resultados/YYYY-MM-DD-integral-erp.json`
- [ ] **Prohibido** JWT/passwords en markdown
- [ ] UI P0/P1: captura + URL + usuario
- [ ] Post-fix: corrida nueva o subconjunto declarado — no editar conteos viejos

### 8.4 Clasificación

- [ ] FAIL solo si no está en §6.1 + HUERFANOS + AGENTS
- [ ] BLOCKED = seed/migrate/API caída
- [ ] HEREDADO documentado con ref baseline
- [ ] DK-D4: no FAIL si flag off **por decisión** reunión

### 8.5 Cierre

- [ ] ≥ 90 % PASS excl. SKIP/BLOCKED/HEREDADO
- [ ] 0 FAIL P0 abiertos
- [ ] `almahue-qa-reviewer` sobre informe final
- [ ] Veredicto único post-fix reconciliado

### 8.6 Automatización

| Bloque | Herramienta | Casos |
|---|---|---|
| Aprobaciones | `ERP/.qa-tmp/qa-retest-seed.mjs` | HEREDADO 20/20 |
| Aprobaciones API | `ERP/erp_back/scripts/qa-aprobaciones-integral.ts` | ADM/CMP/CTR API |
| Smoke API | curl / script integral propuesto | SMK-001–006 |
| Jest | `npm test` erp_back | SMK-008 |
| E2E Playwright | `ERP/qa-e2e/run-e2e-manual.mjs` | E2E-001–006 parcial |
| Demo seed | `npm run seed:demo-propuesta` | Precondición ALM-* |

---

## 9. Orden de ejecución v2

```text
Fase 0 — Gate (BLOCKED detiene)
  Checklist §8.1 → SMK-001–006 → seed completo §3.1 → SMK-008

Ola A — Retest P0 (~55 casos EJECUTAR + HEREDADO documentado)
  SMK-007 → ADM-022 → bloque HEREDADO aprobaciones (registrar sin rerun)
  → CMP-012–013 → VEN-009–012 → VEN-021–026 → VEN-029–031
  → RBAC-001, 007, 014 → INV-010 → BIL-001–002
  → E2E-002 → E2E-003 → E2E-006

Ola B — Cobertura módulos
  PAR → INV movimientos → CTR profundo → CNT → TES → ADM resto → FIC UI

Ola C — E2E golden
  E2E-001 → E2E-004 → E2E-005 → (E2E-007 opcional)

Cierre
  Informe único · reviewer · actualizar puntero resultados/README
```

**Criterio salida v2:** Ola A 100 % PASS (0 FAIL P0); ≥ 90 % plan total excl. SKIP/BLOCKED/HEREDADO.

---

## 10. Anexo

### 10.1 Módulos Nest

Igual v1 §10.1.

### 10.2 Rutas front

Igual v1 §10.2. Redirect `/comercial/cotizaciones` → Compras (CMP).

### 10.3 Mapa IDs legados

Igual v1 §10.3. **v2:** OV12–14 → solo VEN-029–031 (no FIC-009/010).

### 10.4 Permisos clave

Igual v1 §10.4.

### 10.5 Usuarios demo

Igual v1 §3.4 y `PLAN-PRUEBAS-APROBACIONES.md`.

### 10.6 Scripts y artefactos

| Artefacto | Uso v2 |
|---|---|
| `qa-retest-seed.mjs` | Baseline HEREDADO aprobaciones |
| `qa-aprobaciones-integral.ts` | Regresión API aprobaciones |
| `run-e2e-manual.mjs` | E2E Playwright |
| `seed:demo-propuesta` | Ola A/C ALM-* |
| `prepare-demo-sergio.ts` | Pre-demo compras |
| `validate-demo-counts.ts` | Conteos showcase |

---

## 11. Control de cambios

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-08-15 | Plan integral 225 casos (v1, no editar) |
| 2.0 | 2026-08-15 | Fase 3 pipeline: oleadas A/B/C, HEREDADO, −10 casos, commit `2035773` erp_front, retest §9, checklist §8, HUERFANOS H1–H8 |

---

## 12. Delta v2 vs v1 — casos eliminados/consolidados

### 12.1 Resumen numérico

| Métrica | v1 | v2 | Δ |
|---|---:|---:|---:|
| Total IDs | 225 | 215 | **−10** |
| EJECUTAR (estimado) | 225 | ~174 | −41 heredados |
| HEREDADO | 0 | ~41 | +41 |
| SKIP/BLOCKED | ~14 | ~14 | 0 |

### 12.2 Lista eliminados/consolidados

| ID v1 | Acción v2 | Motivo |
|---|---|---|
| **VEN-022** | Consolidado en **VEN-021** | Misma verificación UI: selector Emitir sin tipos compra; código `2035773` ya restringe |
| **FIC-009** | Consolidado en **VEN-029** | Lookup RUT API — un solo ID canonical (análisis §7.1.7) |
| **FIC-010** | Consolidado en **VEN-031** | Productor lookup H1 — duplicado con VEN-031 |
| **INV-009** | Eliminado — ref **VEN-007** | Misma aserción stock post-OV confirmada |
| **INV-018** | Eliminado — ref **E2E-006** paso 1 | Demo inventario duplicaba recorrido 15 min |
| **ADM-013** | Consolidado en **ADM-012** | Simulador S5 $3M — sub-caso de ADM-012 |
| **ADM-014** | Consolidado en **ADM-012** | Simulador S6 Contratistas — sub-caso de ADM-012 |
| **CTR-012** | Eliminado — ref **ADM-012** S6 | Duplicado simulador Diego $400k |
| **CMP-022** | Eliminado — ref **E2E-001** | Recorrido ALM-COT-001 → OC → aprobación ya en E2E |
| **BIL-008** | Consolidado en **VEN-026** | Guía GUIA UI — mismo flujo H8 |

### 12.3 Casos obsoletos de enfoque (no ID — actualización criterio)

| Tema v1 / retest 14/08 | Tratamiento v2 |
|---|---|
| UI-E2 «Emitir permite COTIZ/NP/OC» | **Descartar evidencia** — contradice `2035773` |
| DK-EMITIR «mezcla tipos» como FAIL | **Cerrado en código**; validar VEN-021 PASS |
| OV14 DEBT productor Fase 5 | **Reclasificar** — H1 listo; ejecutar VEN-031 |
| Fase 1 «pantallas desfasado» | **Obsoleto** — H4 listo; RBAC-007 PASS esperado |
| G1 «sin seed OV» | **Mitigado** — `seed:demo-propuesta` obligatorio Ola A/C |

### 12.4 Sin cambio de ID (referencia rápida)

SMK, PAR, CNT, TES, RBAC, E2E mantienen IDs; VEN/ADM/INV/FIC/CMP/CTR/BIL reducen por tabla §12.2.

---

**Fin del plan v2.** Ejecutor: `almahue-qa-runner` → `almahue-qa-reviewer`. Entrada pipeline: análisis `2026-08-15-analisis-integridad-qa-v1.md` veredicto **REQUIERE_RETRABAJO** → salida esperada tras Ola A: **LISTO_PARA_OLA_B**.
