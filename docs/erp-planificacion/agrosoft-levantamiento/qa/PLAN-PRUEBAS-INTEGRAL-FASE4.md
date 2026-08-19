> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`](PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md) + [`HUERFANOS-H1-H14.md`](HUERFANOS-H1-H14.md). Motivo: oleadas 0–7 previas al pipeline v2; D4/D11/D16/D7 ya no son deuda abierta.

# Plan de pruebas integral — Fase 4 (backend/API prioritario)

**Fecha:** 2026-08-14 (validado contra código Nest 2026-08-14)  
**Objetivo:** plan ejecutable para Fase 5 — detectar bugs, gaps de flujo e inconsistencias sin duplicar planes cerrados.  
**Prioridad:** Jest unitarios → API (curl/script) → smoke integración UI (recorridos demo).  
**Credenciales:** ver `AGENTS.md` (no copiar JWT/passwords en informes).  
**No leer transcripciones.** Carlos/Sergio en demo = hipótesis.  
**Prefijo API:** todas las rutas bajo `http://localhost:3001/api/v1` (ver `main.ts` `setGlobalPrefix('api/v1')`).

---

## 1. Resumen ejecutivo

| Aspecto | Detalle |
|---|---|
| **Alcance** | Smoke entorno, 18 `*.spec.ts`, API por módulo (aprobaciones reutilizada, comercial/OV nuevo, compras, contabilidad, tesorería, contratistas, RBAC) |
| **Planes reutilizados** | `PLAN-PRUEBAS-APROBACIONES.md` (20 casos cerrados local 2026-08-13), `PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md` (34 UI — Fase 5 opcional profundo), veredicto `2026-08-12-veredicto-unificado.md` |
| **Huecos que cubre** | Fase 1 §3 flujos transversales, Fase 3 G1–G10, P0 demo, deuda D4/D11/D16/D7 sin clasificar como defecto |
| **Casos API planificados** | **96 IDs** (+ `JT-RUN` sobre ~120 tests Jest en 18 archivos) |
| **Tiempo estimado** | Oleada 0–1 ~7 min · Oleada 2 ~5 min · Oleadas 3–7 ~50–65 min API · UI recorridos A/B/C ~55 min (opcional misma sesión) |
| **Entorno local** | API `http://localhost:3001/api/v1` · Front `http://localhost:5174` · Postgres `:5433` |
| **Pre-seed recomendado** | `npm run seed` + `npm run seed:aprobaciones-f2` + migrate `20260813230000_stock_ov_ficha`; para Recorrido B/OV: datos manuales o script futuro (G1) |

### Relación con planes existentes

| Plan | Rol en Fase 4 | Ejecutar en Fase 5 |
|---|---|---|
| `PLAN-PRUEBAS-APROBACIONES.md` | Oleada 2 — **no reescribir casos**; referenciar IDs E/S/AC/OC/V/R | `ERP/.qa-tmp/qa-retest-seed.mjs` |
| `PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md` | Fuera de oleadas API; smoke UI profundo sin seed | Playwright `e2e-manual-sin-seed.spec.ts` |
| `almahue-qa-local` SKILL | Convenciones PASS/FAIL/BLOCKED y deuda conocida | Runner + reviewer subagentes |
| Recorridos Fase 3 A/B/C | Smoke integración UI al final o en paralelo | Browser MCP / manual |

---

## 2. Oleada 0 — Smoke (~5 min)

**Precondición global:** API y Postgres levantados. Si `GET /health` falla → **todos BLOCKED**.

| ID | Caso | Endpoint / acción | Precondiciones | Esperado | Clasificación fallo |
|---|---|---|---|---|---|
| SM1 | Health API | `GET /health` | API up | `status: ok`, `db: ok` | BLOCKED entorno |
| SM2 | Login admin | `POST /auth/login` | Usuario demo `AGENTS.md` | 200/201, `token`, `permisos` incluye `*` o set esperado | BLOCKED |
| SM3 | Perfil sesión | `GET /auth/me` | Bearer SM2 | `empresaId`, `permisos`, `bandejaModulos` si aplica | defecto auth |
| SM4 | Tenant header | `GET /clientes` con `X-Empresa-Id: EMP-1` | SM2 | 200, solo clientes EMP-1 | defecto tenant |
| SM5 | Periodo activo | `GET /periodos-contables` | seed agosto 2026 | Periodo `2026-08` estado `ABIERTO` | BLOCKED datos |
| SM6 | Stock bodega pre-OV | `GET /insumos/:id/stock-bodegas` | migrate `20260813230000_stock_ov_ficha` + seed; insumo Urea/seed | Al menos una bodega con `cantidad > 0` | BLOCKED G1 / migrate (prod: DK-D20) |

**Comandos rápidos:**

```bash
curl -s http://localhost:3001/api/v1/health
cd ERP/erp_back && npm run seed && npm run seed:aprobaciones-f2
```

---

## 3. Oleada 1 — Jest (~2 min)

**Comando:** `cd ERP/erp_back && npm test`  
**Criterio:** exit 0 en los 18 archivos; fallo = defecto regresión o mock desactualizado.

### 3.1 Inventario `*.spec.ts` (18 archivos — paths exactos bajo `ERP/erp_back/src/`)

| Archivo | Módulo | Cubre (resumen) | `it()` ~ |
|---|---|---|---|
| `auth/pin-aprobacion.spec.ts` | Auth | Formato PIN, pool workflow, `assertPinAprobacion` | 13 |
| `modules/admin/admin.service.spec.ts` | Admin | Empresa, rol master, usuario tenant | 7 |
| `modules/aprobaciones/approval-engine.spec.ts` | Aprobaciones | Cadena grupos/escalas, suplencia, simulador A/B/C/D | 21 |
| `modules/billing/canonical-builder.spec.ts` | Billing | Mapeo tipo doc DTE stub | 2 |
| `modules/catalogos/bc-schedule.util.spec.ts` | Catálogos | Cron BC sync | 2 |
| `modules/catalogos/catalogos.service.spec.ts` | Catálogos | Moneda, CC tenant, sync BC meta | 5 |
| `modules/comercial/comercial-ov.spec.ts` | Comercial | Cotiz→factura rechazada; confirmar OV + SALIDA_VENTA | 2 |
| `modules/comercial/comercial.service.spec.ts` | Comercial | Clientes, reversar CXC, IVA, NC saldo, cotiz→NP | 12 |
| `modules/compras/compras.service.spec.ts` | Compras | OC cadena, recepción, R4-05 matching 3 vías | 16 |
| `modules/contabilidad/contabilidad.service.spec.ts` | Contabilidad | Mayor arrastre, cuenta D10, rename histórico | 11 |
| `modules/contabilidad/contabilizar.service.spec.ts` | Contabilidad | Asiento cuadrado, periodo cerrado | 4 |
| `modules/contratistas/contratistas.service.spec.ts` | Contratistas | Proforma, aprobación, factura N>1, traspaso cierre | 15 |
| `modules/dashboard/dashboard.service.spec.ts` | Dashboard | KPIs OC/proformas, notificaciones, tendencia | 5 |
| `modules/insumos/insumos.service.spec.ts` | Insumos | Movimientos, anular, confirmar borrador stock | 7 |
| `modules/tesoreria/cartola-parser.util.spec.ts` | Tesorería | CSV/PDF parser base | 4 |
| `modules/tesoreria/tesoreria.service.spec.ts` | Tesorería | Desconciliar, contabilizar cartola duplicada | 2 |
| `modules/tesoreria/parsers/almahue-web.spec.ts` | Tesorería | Excel pack MJ | 1 |
| `modules/tesoreria/parsers/bank-parsers.spec.ts` | Tesorería | Chile, Estado, Santander fixtures | 3 |

**Total:** 18 archivos · **132 `it()`** · suite Jest reporta **~120 tests** ejecutables (según config).

| ID | Caso | Esperado |
|---|---|---|
| JT-RUN | `npm test` suite completa | Exit 0, ~120 tests green |
| JT-COV | Revisar gaps §3.2 tras RUN | Documentar en informe Fase 5 |

### 3.2 Gaps de cobertura Jest por módulo (prioridad ampliar)

| Módulo | Cubierto en Jest | **Falta** (API oleadas 3–7 compensan) |
|---|---|---|
| Comercial OV | Confirmar OV mock; cotiz→factura rechazada | `ventaBajoCosto` BLOQUEAR/PERMITIR_MERMA; splits multi-bodega; FLETE; `lookupRut`; lock qty/desc en factura desde OV; guías despacho |
| Insumos | Movimiento legacy `insumo.stock` | `GET insumos/:id/stock-bodegas`; saldo negativo por bodega; tránsito venta (deuda D14) |
| Tesorería | Parsers + 2 service tests | `cuenta-corriente.service`; conciliación completa; pagos→CC; import cartola archivo |
| Contabilidad | Cuentas, mayor, contabilizar | `centralizacion/preview` y `ejecutar`; periodos abrir/cerrar; import Excel plan |
| Auth | Solo PIN util | `auth.service` login, refresh, Microsoft stub, tenant en JWT |
| Admin | Empresa/usuario parcial | `grupos-aprobacion` CRUD service; import/export config |
| Ficha | — | Sin `*.spec.ts`; ficha vía clientes/proveedores API |
| Billing | Canonical 2 tests | Emisión gateway stub end-to-end |

**Top 5 gaps Jest (ampliar post-Fase 5):** ver §12 del resumen ejecutivo Fase 4.

---

## 4. Oleada 2 — API aprobaciones (~5 min)

**Reutilizar íntegramente** `PLAN-PRUEBAS-APROBACIONES.md`. No duplicar descripción: ejecutar script existente.

| ID | Bloque | Referencia plan | Automatización |
|---|---|---|---|
| E1–E3 | Entorno | §A | `qa-retest-seed.mjs` |
| S1–S6 | Simulador | §B | idem |
| AC1–AC5 | AdminConcepto | §C | AC1 UI; AC2–AC5 API en script |
| OC1–OC4, V1 | Flujo OC | §D | idem |
| R1 | Dashboard María | §E | idem |
| R2 | Build front | §E | `npx tsc -b && npx vite build` en `erp_front` |

**Precondiciones:** seed + `seed:aprobaciones-f2`. AdminConcepto: **re-login** antes de grupos.

**Estado conocido:** 20/20 PASS local (veredicto 2026-08-13). Fase 5: re-ejecutar tras cambios en compras/contratistas; FAIL aquí bloquea oleadas 4 y 6.

**Script alternativo:** `ERP/erp_back/scripts/qa-aprobaciones-integral.ts` (cubre APIs B/D/E + gaps esperados).

---

## 5. Oleada 3 — API comercial / inventario (~15 min)

**Objetivo:** cerrar huecos Fase 1 D11–D17, Fase 3 Recorrido B, G1/G10.  
**Datos:** insumo con `StockInsumoBodega` > 0 (Urea/Bodega Central post-migrate); cliente `CLI-*` seed. **Sin seed OV** (G1): crear OV en runtime antes de OV4–OV9 o marcar BLOCKED.

| ID | Caso | Método / ruta | Permiso | Precondiciones | Datos / body (resumen) | Esperado | Demo Fase 3 |
|---|---|---|---|---|---|---|---|
| OV1 | Crear OV PRODUCTO + splits | `POST /documentos` | `comercial:write` | SM6 stock ≥ qty | `tipo: ORDEN_VENTA`, `estado: BORRADOR`, línea `tipoLinea: PRODUCTO`, `insumoId`, `splits: [{bodegaId, cantidad}]` | 201, `tipo: ORDEN_VENTA`, `estado: BORRADOR` | Recorrido B paso 3 |
| OV2 | Línea SERVICIO sin insumo | `POST /documentos` | `comercial:write` | idem | `tipoLinea: SERVICIO`, sin `insumoId` | 201 | D12 |
| OV3 | FLETE como línea | `POST /documentos` | `comercial:write` | idem | `tipoLinea: FLETE` | 201, `tipoLinea` FLETE | D17 |
| OV4 | Rechazar stock insuficiente | `POST /documentos/:id/confirmar` | `comercial:write` | OV1 qty > stock bodega | — | 400 BadRequest | D15 |
| OV5 | Confirmar OV → movimiento | `POST /documentos/:id/confirmar` | `comercial:write` | OV1 stock OK | — | `estado: APROBADO`; movimiento `SALIDA_VENTA` | Recorrido B paso 3 |
| OV6 | Stock bodega decrementa | `GET /insumos/:id/stock-bodegas` | `insumos:read` o `comercial:read` | post OV5 | — | `cantidad` bodega -= qty OV | Recorrido B paso 1 |
| OV7 | Splits multi-bodega | `POST /documentos` + confirmar | `comercial:write` | 2 bodegas con stock | splits en B1+B2 | 201 + confirm OK | D15 |
| OV8 | Convertir OV → factura | `POST /documentos/:id/convertir` | `comercial:write` | OV5 `estado: APROBADO` | `{ "tipoDestino": "FACTURA" }` | Nueva factura `EMITIDO`, `documentoOrigenId` = OV | Recorrido B paso 4 |
| OV9 | Lock qty/desc factura | `PUT /documentos/:facturaId` | `comercial:write` | post OV8 | Cambiar `cantidad`/`descripcion` en línea | 400 (`assertFacturaLineasLocked`); precio editable OK | D13 |
| OV10 | ventaBajoCosto BLOQUEAR | `POST /documentos` OV | `comercial:write` | default empresa `BLOQUEAR` | precio < `costoPromedio` insumo | 400 | D16 (deuda: sin UI param) |
| OV11 | ventaBajoCosto PERMITIR_MERMA | `POST /documentos` | `comercial:write` | `PUT /empresas/EMP-1` `{ ventaBajoCosto: "PERMITIR_MERMA" }` (admin, **restaurar post-test**) | precio < costo + `mermaMotivo` en línea | 201 | D16 |
| OV12 | lookup RUT cliente | `GET /lookup-rut?rut=` | `comercial:read` \| `compras:read` \| `catalogos:read` | cliente seed | RUT cliente existente | `cliente: true`, `productor: false` | D7 |
| OV13 | lookup RUT proveedor | `GET /lookup-rut?rut=` | idem | proveedor seed | RUT proveedor | `proveedor: true` | D7 |
| OV14 | lookup sin productor | `GET /lookup-rut?rut=` | idem | RUT no maestro | RUT inventado | `productor: false` (deuda conocida) | D7 — **no FAIL** |
| OV15 | Cotización → OC (Compras) | `POST /documentos/:id/convertir` | `compras:write` | cotización `tipo: COTIZACION`, `BORRADOR` | `{ "tipoDestino": "OC" }` | OC en `ordenes-compra` / doc convertido | Recorrido A paso 3 |
| OV16 | Cotización → factura rechazada | `POST /documentos/:id/convertir` | `compras:write` | cotización compras | `{ "tipoDestino": "FACTURA" }` | 400 «cotización… a OC, no a factura» | D11 |
| OV17 | Libro ventas ámbito | `GET /libro-comercial?ambito=ventas` | `comercial:read` | facturas emitidas/contabilizadas seed | default `ventas`; no incluir borradores OV | Solo documentos válidos libro | R4-06/D6 revalidar |

**P0 oleada comercial (ejecutar primero si tiempo corto):** OV1, OV4, OV5, OV6, OV8, OV9, OV10, OV15.

**Deuda conocida (no FAIL):** aprobación comercial OV/factura (D4); wizard Emitir mezcla tipos (validar solo si se abre UI); NP en showcase seed (G10).

---

## 6. Oleada 4 — API compras (~10 min)

**Reutiliza Jest R4-05/P1-10; API valida cableado real.**

| ID | Caso | Método / ruta | Permiso | Precondiciones | Esperado | Fase 3 |
|---|---|---|---|---|---|---|
| CP1 | Listar OC | `GET /ordenes-compra` | `compras:read` | seed EMP-1 | 200, tenant EMP-1 | Recorrido A |
| CP2 | Crear OC EMITIDA | `POST /ordenes-compra` | `compras:write` | periodo abierto, proveedor, CC | `estado: EMITIDO`, aprobación en cadena | OC1 |
| CP3 | Bandeja aprobaciones | `GET /aprobaciones-oc` | bandeja runtime (sin `compras:read` global) | usuario en cadena | Lista filtrada asignación | Recorrido A paso 4 |
| CP4 | Aprobar OC (PIN) | `PUT /ordenes-compra/:id` | aprobador en cadena | OC EMITIDO en bandeja | body: `estado: APROBADO`, `pinAprobacion: "4821"` + campos OC | `APROBADO` | Oleada 2 OC3 |
| CP5 | Recepción borrador → confirmar | `POST /recepciones-oc` + `PATCH /recepciones-oc/:id` | `compras:write` | OC `APROBADO` | POST `estado: BORRADOR` → PATCH `{ estado: "CONFIRMADA" }` | OC `RECEPCIONADA` | Recorrido A paso 6 |
| CP6 | Recepción parcial | `POST /recepciones-oc` | `compras:write` | OC multi-línea | Segunda recepción saldo OK; exceso cantidad → 400 | P1-10 Jest |
| CP7 | Registro sin recepción | `POST /registros-compra` | `compras:write` | OC solo `APROBADO` (sin `RECEPCIONADA`) | 400 | R4-05 Jest |
| CP8 | Registro match 3 vías | `POST /registros-compra` | `compras:write` | OC `RECEPCIONADA` | body `ocNumero`, `monto` = recepcionado → `matchOk: true` | Recorrido A paso 7 |
| CP9 | Registro match fail | `POST /registros-compra` | `compras:write` | OC recepcionada | `monto` ≠ recepción → `matchOk: false` | R4-05 |
| CP10 | Libro compras | `GET /registros-compra` | `compras:read` | registros seed | Lista coherente con OC | Recorrido A paso 7 |
| CP11 | Carga masiva registros | `POST /registros-compra/carga-masiva` | `compras:write` | payload mínimo `items[]` | 200 o validación clara | opcional |

---

## 7. Oleada 5 — API contabilidad + tesorería (~15 min)

**Recorrido C Fase 3.** Datos: `seed-demo-showcase` o `prepare-demo-sergio`.

### Contabilidad (prefijo CT)

| ID | Caso | Endpoint | Precondiciones | Esperado |
|---|---|---|---|---|
| CT1 | Listar periodos | `GET /periodos-contables` | `contabilidad:read` | 2026-08 ABIERTO |
| CT2 | Crear asiento manual | `POST /asientos` | cuentas imputables, periodo abierto | 201 cuadrado |
| CT3 | Asiento descuadrado | `POST /asientos` | débito ≠ crédito | 400 |
| CT4 | Editar contabilizado | `PATCH /asientos/:id` | asiento CONTABILIZADO | 400 |
| CT5 | Cuenta con movimiento DELETE | `DELETE /cuentas/:id` | cuenta con asientos | 409 |
| CT6 | Impacto cuenta | `GET /cuentas/:id/impacto` | cuenta seed | conteos movimientos |
| CT7 | Centralización preview | `POST /centralizacion/preview` | docs pendientes periodo | preview líneas |
| CT8 | Centralización ejecutar | `POST /centralizacion/ejecutar` | solo BD QA / snapshot | asientos generados (opcional destructivo) |
| CT9 | Libro diario | `GET /libro-diario?periodo=2026-08` | asientos seed | líneas periodo |
| CT10 | Balance 8 columnas | `GET /balance-8-columnas?periodo=2026-08` | datos showcase | columnas con saldos |
| CT11 | Mayor arrastre | `GET /mayor?periodo=` | 2 periodos con movimiento | saldo arrastrado (Jest P1-11) |

### Tesorería (prefijo TB)

| ID | Caso | Endpoint | Precondiciones | Esperado |
|---|---|---|---|---|
| TB1 | Cartolas | `GET /cartolas-bancarias` | showcase seed | lista cartolas |
| TB2 | Movimientos cartola | `GET /cartolas-bancarias/:id/movimientos` | cartola seed | filas parseadas |
| TB3 | Preview archivo cartola | `POST /cartolas-bancarias/preview-archivo` | CSV fixture | preview filas |
| TB4 | Conciliaciones | `GET /conciliaciones` | seed | resumen pendientes |
| TB5 | Movimientos conciliación | `GET /conciliaciones/:id/movimientos` | conciliación seed | 200 |
| TB6 | Estado cuenta saldos | `GET /cuentas-corrientes` | clientes con facturas | saldos coherentes |
| TB7 | Estado cuenta detalle | `GET /cuentas-corrientes/:terceroId/movimientos?terceroTipo=CLIENTE` | `tesoreria:read` | cliente con CXC | movimientos ordenados | R4-17 |
| TB8 | Pagos | `GET /pagos` / `POST /pagos` | tesoreria:write | crea pago y calza CC |
| TB9 | Aging sync | `POST /documentos-aging/sync` | facturas pendientes | aging actualizado |
| TB10 | Anticipos | `GET /anticipos-productores` | seed | lista |
| TB11 | Flujo caja | `GET /movimientos-caja` | seed | lista |

**Deuda conocida (no FAIL):** Excel cartolas formato MJ fino; cobranza R4-18; SMTP.

---

## 8. Oleada 6 — API contratistas + ficha (~10 min)

| ID | Caso | Método / ruta | Permiso | Precondiciones | Esperado | Fase 3 |
|---|---|---|---|---|---|---|
| CTR1 | Listar proformas | `GET /proformas-contratista` | `contratistas:read` | seed Sergio/showcase | 200 | Recorrido A alt |
| CTR2 | Crear proforma BORRADOR | `POST /proformas-contratista` | `contratistas:write` | contratista + tarifa | 201 `estado: BORRADOR` | — |
| CTR3 | Solicitar aprobación | `POST /proformas-contratista/:id/solicitar-aprobacion` | `contratistas:write` | reglas Contratistas seed | `PENDIENTE_APROBACION` en cadena | Recorrido contratistas |
| CTR4 | Aprobar con PIN | `POST /proformas-contratista/:id/definitiva` | aprobador en cadena | post CTR3 | body `{ pinAprobacion: "4821" }` → `estado: DEFINITIVA` | Oleada 2 / bandeja |
| CTR5 | Asociar factura | `POST /proformas-contratista/:id/factura` | `contratistas:write` | proforma `DEFINITIVA` | `FACTURADA` | Recorrido A |
| CTR6 | Reversar proforma | `POST /proformas-contratista/:id/reversar` | `contratistas:write` | DEFINITIVA + PIN | BORRADOR | Jest R4-04 |
| CTR7 | Traspaso cierre | `POST /contratistas/traspaso-cierre` | `contratistas:write` | periodo con proformas | asiento o 400 si cerrado | G5 — no confundir con gastos temporada |
| FICHA1 | Ficha proveedor | `GET /proveedores/:id` | `catalogos:read` \| `compras:read` | proveedor con ficha seed (`catalogos.controller`) | bancos/contactos/despacho en payload | D8 |
| FICHA2 | Cliente detalle | `GET /clientes/:id` | `comercial:read` | cliente seed | pestañas ficha en payload | Recorrido B paso 2 |
| FICHA3 | Historial contraparte | `GET /clientes/:id` o `GET /proveedores/:id` | idem | seed con `solicitadoPor` | campos `solicitadoPor` / historial presentes | D8 |

**Deuda:** ingreso diario / asociación labores sin guion demo (G4); productor lookup (D7).

---

## 9. Oleada 7 — RBAC / tenant / seguridad (~10 min)

| ID | Caso | Endpoint / acción | Actor | Esperado |
|---|---|---|---|---|
| RB1 | Cross-tenant documento | `GET /documentos/:id` otro `empresaId` | admin EMP-1 | 404 o 403 |
| RB2 | AdminConcepto usuarios | `GET /usuarios` | Claudia Compras | 403 | AC3 |
| RB3 | Grupos filtrados módulo | `GET /grupos-aprobacion` | Claudia / Ricardo | 12 Compras / 8 Contratistas | AC2, AC4 |
| RB4 | Sin `compras:read` global bandeja | `GET /aprobaciones-oc` | Jorge en cadena | 200 + ítems asignados | OC2 |
| RB5 | Sin permiso módulo | `GET /ordenes-compra` | usuario solo `comercial:read` | 403 |
| RB6 | PIN obligatorio pool | `PUT /ordenes-compra/:id` sin `pinAprobacion` | aprobador en cadena | `estado: APROBADO` sin PIN | 400 PIN requerido |
| RB7 | Header empresa inconsistente | `GET /clientes` `X-Empresa-Id: EMP-2` sin acceso | usuario mono-empresa | 403 o lista vacía |
| RB8 | Legacy workflows-admin | `GET /workflows-admin` | admin | 200 pero **deuda** — no promover | G8 Fase 3 |
| RB9 | Indicadores BC permiso | `GET /indicadores-bc` | `catalogos:read` | 200 | G6 |
| RB10 | Re-login AdminConcepto | Cambiar admin concepto → login | admin | JWT `adminConceptoModulos` actualizado | P0-5 |

---

## 10. Matriz unificada (referencia rápida)

**Total casos planificados:** **96 IDs API** (+ `JT-RUN` sobre ~120 tests Jest).

| Prefijo | Oleada | Cantidad | Fuente |
|---|---|---|---|
| SM | 0 Smoke | 6 | nuevo |
| JT | 1 Jest | 1 (+ inventario 18 archivos) | código |
| E, S, AC, OC, V, R | 2 Aprobaciones | 20 (script) + R2 build opcional | `PLAN-PRUEBAS-APROBACIONES.md` |
| OV | 3 Comercial | 17 | nuevo |
| CP | 4 Compras | 11 | nuevo + Jest R4-05 |
| CT | 5 Contabilidad | 11 | nuevo |
| TB | 5 Tesorería | 11 | nuevo |
| CTR, FICHA | 6 Contratistas | 10 | nuevo |
| RB | 7 Seguridad | 10 | nuevo + AC |

### Orden de ejecución (rápido → profundo)

1. **SM** (5 min) — sin datos, detecta entorno roto  
2. **JT-RUN** (2 min) — regresión unitaria masiva  
3. **Oleada 2** script aprobaciones (5 min) — flujo crítico ya certificado  
4. **OV P0** (8 casos, ~10 min) — mayor riesgo demo ventas  
5. **CP1–CP8** (10 min) — compras estrella  
6. **RB1–RB7** (5 min) — tenant/permisos  
7. **CT1–CT7, TB6–TB7** (10 min) — back-office mínimo Recorrido C  
8. **CTR1–CTR5, FICHA1–FICHA2** (10 min) — contratistas demo  
9. **Resto OV/TB/CT opcional** — profundidad  
10. **UI Recorridos A/B/C** (Fase 3 §3) — smoke integración manual/browser  
11. **E2E sin seed** (34 casos) — solo si hay tiempo o release mayor  

---

## 11. Deuda conocida — tabla «no FAIL»

Registrar como `deuda conocida` o `BLOCKED` (prod), no defecto de producto.

| ID ref | Tema | Fuente | Nota QA |
|---|---|---|---|
| DK-D4 | Sin cadena aprobación OV/factura | Fase 1 D4, AGENTS | OV8 factura directa OK; no esperar bandeja comercial |
| DK-D11 | Cotizaciones menú vs permisos | Fase 1 §4 | Catálogo desfasado; probar API no UI permisos |
| DK-D16 | `ventaBajoCosto` sin UI admin | Fase 1 D16 | OV10/11 vía BD; default BLOQUEAR |
| DK-D7 | Productor en lookup | Fase 1 D7 | OV14: `productor: false` esperado |
| DK-EMITIR | Wizard Emitir mezcla tipos | Fase 1 §3 | No caso API canónico; UI ocultar COTIZ/NP/OC |
| DK-DTE | Billing stub / GoSocket | Fase 1, AGENTS | No probar emisión SII real |
| DK-LEGACY | `workflows-admin` API | Fase 3 G8 | RB8: existe pero deprecado |
| DK-G1 | Sin seed OV E2E | Fase 3 G1 | Preparar datos antes OV5–OV9 o BLOCKED |
| DK-G10 | Showcase NP/cotización cliente | Fase 3 G10 | No mezclar con Recorrido B |
| DK-D20 | Prod sin migrate OV | AGENTS, Fase 3 P0-1 | SM6 BLOCKED en prod hasta deploy |
| DK-D14 | Sin tránsito venta | Fase 1 D14 | No modelado |
| DK-R4-18 | Cobranza mail | Reu4 | No existe |
| DK-G5 | Traspaso cierre ≠ gastos temporada | Fase 3 G5 | Narrativa demo |

---

## 12. Automatización sugerida (no implementada en Fase 4)

### Script propuesto: `ERP/erp_back/scripts/qa-integral-fase4.ts`

Estructura similar a `qa-aprobaciones-integral.ts` y `qa-retest-seed.mjs`:

```typescript
// Bloques: SM → OV → CP → CT → TB → CTR → RB (+ subprocess Oleada 2)
const API = process.env.API_BASE ?? 'http://localhost:3001/api/v1';
const EMP = 'EMP-1';

type Result = { id: string; wave: string; status: 'PASS'|'FAIL'|'BLOCKED'|'DEBT'; evidence: string };

async function login(email: string, password: string) { /* POST /auth/login */ }
async function api(method, path, { token, body, empresaId = EMP }) { /* fetch + X-Empresa-Id */ }
function record(id, wave, status, evidence) { /* push + console */ }

const blocks = {
  SM: async () => {
    // GET /health (Public, health.controller.ts)
    // POST /auth/login, GET /auth/me
    // GET /clientes + X-Empresa-Id
    // GET /periodos-contables
    // GET /insumos/:id/stock-bodegas (precondición G1)
  },
  OV: async (ctx) => {
    // P0: POST /documentos ORDEN_VENTA → confirmar → stock-bodegas → convertir FACTURA → PUT lock
    // lookup-rut x3, cotiz→OC/FACTURA, libro-comercial
    // ensureStock: si SM6 BLOCKED, marcar OV4–OV9 BLOCKED (DK-G1)
  },
  CP: async () => {
    // GET ordenes-compra, POST recepciones-oc, PATCH confirmar
    // POST registros-compra matchOk true/false (tolerancia ±1 CLP según compras.service)
  },
  CT: async () => { /* periodos, asientos, centralizacion/preview */ },
  TB: async () => { /* cuentas-corrientes/:terceroId/movimientos */ },
  CTR: async () => { /* solicitar-aprobacion → definitiva+PIN */ },
  RB: async () => { /* cross-tenant GET /documentos/:id, grupos-aprobacion AdminConcepto */ },
};

async function main() {
  const results: Result[] = [];
  for (const [wave, fn] of Object.entries(blocks)) await fn();
  // subprocess: node ERP/.qa-tmp/qa-retest-seed.mjs → merge E/S/AC/OC/V/R
  // write docs/.../qa/resultados/YYYY-MM-DD-fase5-ejecucion.json (sin JWT)
}
```

**Rutas validadas (no inventar):**

| Caso | Ruta real (`comercial.controller` / otros) |
|---|---|
| Confirmar OV | `POST /documentos/:id/confirmar` |
| Convertir | `POST /documentos/:id/convertir` — `tipoDestino`: `OC` \| `FACTURA` \| `NP` |
| Lookup RUT | `GET /lookup-rut?rut=` |
| Aprobar OC | `PUT /ordenes-compra/:id` + `pinAprobacion` |
| Recepción | `POST /recepciones-oc`, `PATCH /recepciones-oc/:id` |
| Registro compra | `POST /registros-compra` |
| CC detalle | `GET /cuentas-corrientes/:terceroId/movimientos` |
| Proforma aprobar | `POST /proformas-contratista/:id/definitiva` |
| Health | `GET /health` (`@Public`, `health.controller.ts`) |

### Prioridad automatizar

| Prioridad | Bloque | Motivo |
|---|---|---|
| 1 | SM + OV P0 | Bloquea demo ventas (P0-2) |
| 2 | CP R4-05 | Matching OC-factura histórico Reu4 |
| 3 | RB tenant | Seguridad multi-empresa |
| 4 | TB6–TB7 | Estado cuenta demo MJ |
| 5 | Re-invoke Oleada 2 | Regresión aprobaciones en CI |

### Artefactos existentes reutilizar

| Artefacto | Uso |
|---|---|
| `ERP/.qa-tmp/qa-retest-seed.mjs` | Oleada 2 completa |
| `ERP/.qa-tmp/e2e-admin-concepto.spec.ts` | AC1 UI |
| `ERP/.qa-tmp/e2e-manual-sin-seed.spec.ts` | E2E 34 sin seed |
| `ERP/erp_back/scripts/validate-demo-counts.ts` | Conteos showcase (OC, facturas, CC); **no** valida `StockInsumoBodega` — usar SM6 API |
| `ERP/erp_back/scripts/prepare-demo-sergio.ts` | Pre-demo datos compras |
| `ERP/qa-e2e/run-e2e-manual.mjs` | Runner Playwright alternativo |

**package.json** (`erp_back`): solo `test`, `test:e2e` (jest-e2e vacío o mínimo). Sugerencia Fase 5: `"test:qa:fase4": "ts-node scripts/qa-integral-fase4.ts"`.

---

## 13. Criterios de salida Fase 5 → lista unificada de fixes

| Criterio | Acción |
|---|---|
| Oleada 0–2 **BLOCKED** | No continuar; arreglar entorno/seed/migrate |
| Oleada 2 FAIL (regresión aprobaciones) | **P0 fix** antes de comercial |
| OV P0 FAIL | Fix o datos (G1); actualizar guion demo |
| CP8/CP9 FAIL matching | Regresión R4-05 — fix compras |
| RB cross-tenant FAIL | Escalar seguridad |
| FAIL en deuda conocida (DK-*) | Reclasificar; no abrir ticket producto |
| Jest JT-RUN FAIL | Fix unitario o actualizar mock |
| PASS ≥ 90% casos API (excl. DEBT/BLOCKED) | Publicar `2026-08-14-fase5-ejecucion.md` |
| Defectos nuevos | Tabla con severidad + módulo + caso ID |

### Referencia recorridos demo Fase 3

| Recorrido | Casos API alineados | Duración UI |
|---|---|---|
| **A** Compras + aprobaciones | CP1–CP10, Oleada 2 OC, CTR3–CTR5 | ~18 min |
| **B** OV + stock + factura | OV1–OV9, FICHA2, SM5–SM6 | ~20 min |
| **C** Contabilidad + tesorería | CT1–CT11, TB1–TB11 | ~18 min |

---

## 15. Anexo — correcciones aplicadas (validación código 2026-08-14)

| Antes (borrador) | Corregido (código real) | Evidencia |
|---|---|---|
| OV15 `tipoDestino: ORDEN_COMPRA` | `tipoDestino: "OC"` | `ConvertirDocumentoDto`, `comercial.service` L1227 |
| OV11 PATCH BD empresa | `PUT /empresas/:id` campo `ventaBajoCosto` | `admin.controller.ts` |
| CP4 «vía compras.service» | `PUT /ordenes-compra/:id` + `pinAprobacion` | `qa-retest-seed.mjs` OC3, `UpsertOrdenCompraDto` |
| CP5 solo PATCH | POST borrador + PATCH `estado: CONFIRMADA` (o POST directo `CONFIRMADA`) | `compras.service` `updateRecepcion` |
| TB7 `/cuentas-corrientes/:id/movimientos` | `/cuentas-corrientes/:terceroId/movimientos?terceroTipo=CLIENTE` | `tesoreria.controller.ts` L331 |
| CTR4 «resolver» ambiguo | `POST /proformas-contratista/:id/definitiva` tras `solicitar-aprobacion` | `contratistas.controller.ts` |
| FICHA1 proveedores en comercial | `GET /proveedores/:id` en **catálogos** | `catalogos.controller.ts` L179 |
| SM6 `validate-demo-counts` para stock | `GET /insumos/:id/stock-bodegas` | `insumos.controller.ts` L50; script counts no incluye stock bodega |
| ~110 tests Jest | ~120 tests (18 archivos, 132 `it()`) | inventario `*.spec.ts` |
| Total 86 casos | **96 casos API** (conteo por ID en oleadas 0–7) | matriz §10 |

**Duplicados intencionales:** SM2/SM3 solapan E2/login de Oleada 2 — smoke rápido antes del script largo.

---

## 14. Informe Fase 5

Usar plantilla `qa/resultados/PLANTILLA.md` extendida con columnas: `Clasificación` (defecto / deuda / BLOCKED).  
Resumen ejecutivo en `qa/resultados/2026-08-14-fase5-ejecucion.md` (o fecha de ejecución real).
