# Resultados QA — Fase 5 ejecución integral

**Fecha:** 2026-08-14  
**Entorno:** local (Postgres `:5433`, API `http://localhost:3001/api/v1`)  
**Ejecutor:** almahue-qa-runner + almahue-qa-reviewer (pasada única)  
**Plan:** `qa/PLAN-PRUEBAS-INTEGRAL-FASE4.md`  
**Preparación:** API levantada (`npm run start:dev`); `prisma migrate deploy` (sin pendientes); `npm run seed` + `npm run seed:aprobaciones-f2`. Sin seed inicial, oleada 2 quedó 3/20 PASS (usuarios QA inexistentes).

No incluir JWT ni passwords.

---

## Conteo global

| PASS | FAIL | BLOCKED | SKIP | DEBT | Total IDs |
|------|------|---------|------|------|-----------|
| 52 | 4 | 1 | 36 | 4 | 97 (`96` API + `JT-RUN`) |

**Notas de conteo:** `DEBT` = deuda conocida validada, no defecto nuevo. `R2` (build front) = SKIP. Oleadas 5–6 (CT/TB/CTR profundo) mayormente SKIP por alcance de sesión; smoke puntual CT1/TB6/CTR1/FICHA1 sí ejecutado.

---

## Oleada 0 — Smoke (SM)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| SM1 | PASS | `GET /health` → `status=ok`, `db=ok` |
| SM2 | PASS | Login admin 200 |
| SM3 | PASS | `GET /auth/me` → `empresaId=EMP-1` (con `X-Empresa-Id: EMP-1`) |
| SM4 | PASS | `GET /clientes` → 2 clientes EMP-1 |
| SM5 | PASS | Periodo `2026-08` `ABIERTO` (post-seed) |
| SM6 | PASS | Tras `POST /movimientos-bodega` ENTRADA en Bodega Central, `GET .../stock-bodegas` → `cantidad=100`. **Sin movimiento:** bodega `0` con `stockTotal` legacy > 0 (hueco seed G1) |

---

## Oleada 1 — Jest (JT)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| JT-RUN | FAIL | Exit 1: `insumos.service.spec.ts` 4× `Bodega no encontrada: Central` (mock desactualizado vs `stock-bodega.util`); `comercial.service.spec.ts` no compila (`documentoOrigenId` / `folioOrigen` en union). Resto: 116 tests PASS en 16 suites |

---

## Oleada 2 — Aprobaciones (script `ERP/.qa-tmp/qa-retest-seed.mjs`)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| E1 | PASS | health 200 |
| E2 | PASS | permisos `*` |
| E3 | PASS | sin token → 401 |
| S1 | PASS | simulador cadena Jorge |
| S2 | PASS | Pablo |
| S3 | PASS | Jorge |
| S4 | PASS | Laura → Bruno |
| S5 | PASS | Jorge → Claudia |
| S6 | PASS | Pablo |
| AC1 | PASS | JWT adminConcepto Compras |
| AC2 | PASS | grupos Compras=12 |
| AC3 | PASS | usuarios 403 |
| AC4 | PASS | Contratistas=8 |
| AC5 | PASS | combo JWT módulos |
| OC1 | PASS | OC emitida 201 |
| OC2 | PASS | bandeja veOC |
| OC3 | PASS | PUT APROBADO + PIN |
| OC4 | PASS | veOCajena false |
| R1 | PASS | notificaciones 200 |
| V1 | PASS | escala 400 APROBADOR_SIN_BANDEJA |
| R2 | SKIP | build `erp_front` no ejecutado |

---

## Oleada 3 — Comercial / OV

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| OV1 | PASS | `POST /documentos` OV PRODUCTO + splits 201 |
| OV2 | PASS | línea SERVICIO 201 |
| OV3 | PASS | línea FLETE 201 |
| OV4 | PASS | confirmar qty>stock → 400 |
| OV5 | PASS | confirmar → `APROBADO`, SALIDA_VENTA |
| OV6 | PASS | stock bodega 100→97 |
| OV7 | SKIP | multi-bodega no preparado en sesión |
| OV8 | PASS | convertir → FACTURA 201 |
| OV9 | PASS | PUT factura cambia qty → 400 |
| OV10 | PASS | precio bajo costo → 400 |
| OV11 | DEBT | DK-D16 `PERMITIR_MERMA` sin UI |
| OV12 | FAIL | `GET lookup-rut` RUT cliente seed → `clientes:[]` (normaliza `76111000-K`) |
| OV13 | FAIL | lookup proveedor seed → `proveedores:[]` |
| OV14 | DEBT | DK-D7 sin maestro productor |
| OV15 | BLOCKED | `DOC-SEED-COT-BORR` sin `proveedorId` → convertir OC 400 |
| OV16 | DEBT | DK-D11 cotiz→factura (no ejecutado; cotiz seed incompleta) |
| OV17 | PASS | `GET /libro-comercial?ambito=ventas` 200 |

---

## Oleada 4 — Compras (CP)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| CP1 | PASS | `GET /ordenes-compra` 200 |
| CP2 | PASS | `POST` OC EMITIDA con solicitante **Luis Herrera** (en grupo); admin como solicitante → 400 |
| CP3 | PASS | `GET /aprobaciones-oc` Jorge 200 |
| CP4 | PASS | Jorge PUT APROBADO + PIN 4821 |
| CP5 | PASS | POST recepción borrador + PATCH CONFIRMADA |
| CP6 | SKIP | recepción parcial |
| CP7 | PASS | registro OC solo APROBADO → 400 |
| CP8 | PASS | registro OC `OC-2026-004` RECEPCIONADA, `monto=600000` → `matchOk: true` |
| CP9 | SKIP | match fail explícito |
| CP10 | PASS | `GET /registros-compra` 200 |
| CP11 | SKIP | carga masiva |

---

## Oleada 5 — Contabilidad / Tesorería (muestra)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| CT1 | PASS | periodos 2026-08 ABIERTO |
| CT2–CT11 | SKIP | no ejecutado en sesión |
| TB1–TB5 | SKIP | no ejecutado |
| TB6 | PASS | `GET /cuentas-corrientes` 200 (1 tercero) |
| TB7–TB11 | SKIP | no ejecutado |

---

## Oleada 6 — Contratistas / Ficha (muestra)

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| CTR1 | PASS | `GET /proformas-contratista` 200 (5) |
| CTR2–CTR7 | SKIP | no ejecutado |
| FICHA1 | PASS | `GET /proveedores/:id` 200 |
| FICHA2–FICHA3 | SKIP | no ejecutado |

---

## Oleada 7 — RBAC

| ID | Resultado | Evidencia |
|----|-----------|-----------|
| RB1 | FAIL | `GET /documentos/:id` usuario Luis + `X-Empresa-Id: EMP-2` → **200** (documento EMP-1 visible) |
| RB2 | PASS | Claudia `GET /usuarios` → 403 |
| RB3 | PASS | Claudia grupos Compras=12 |
| RB4 | PASS | Jorge bandeja OC 200 |
| RB5–RB7 | SKIP | no ejecutado |
| RB8 | DEBT | DK-LEGACY workflows-admin |
| RB9 | PASS | `GET /indicadores-bc` 200 |
| RB10 | SKIP | re-login manual |

---

## Defectos vs deuda (resumen)

| ID caso | Clasificación | Nota |
|---------|---------------|------|
| JT-RUN | defecto nuevo | Mocks Jest insumos + tipos comercial.service.spec |
| OV12, OV13 | defecto nuevo | Lookup RUT no resuelve contrapartes seed |
| RB1 | defecto nuevo | Aislamiento tenant header vs documento |
| OV11, OV14, OV16, RB8 | deuda conocida | DK-* |
| OV15 | entorno/datos | Cotización showcase sin proveedor (relacionado DK-G10) |
| SM6 (sin prep) | entorno/datos | DK-G1 stock bodega no poblado en seed |

---

## Retest sugerido

1. Tras fix RB1 y lookup-rut: RB1, OV12–OV13.  
2. Tras fix Jest: `npm test` JT-RUN.  
3. Completar oleadas 5–6 (CT centralización, TB7 estado cuenta, CTR4 PIN).  
4. Seed: alinear `StockInsumoBodega` con stock legacy; cotización BORRADOR con `proveedorId` para OV15.  
5. Re-ejecutar `qa-retest-seed.mjs` tras cada cambio en compras/aprobaciones.

---

## Artefactos locales

- `ERP/.qa-tmp/qa-retest-seed-results.json`  
- `ERP/.qa-tmp/fase5-api-results.json` (corrida parcial inicial)  
- Scripts ad-hoc: `fase5-smoke-ov-prep.mjs`, `fase5-integral-api.mjs`, `fase5-retest-ov.mjs`
