> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# 07 — Flujo completo API (Reu4)

Fecha: 2026-07-31T19:09:09.471Z
Base: `http://127.0.0.1:5174/api/v1` (proxy Vite → Nest :3001)
Postgres: `localhost:5433`

## Veredicto

**PASS** (API + UI smoke MODO REAL): barrido GET sin 404/401/5xx de ruta; flujo RBAC OC/proformas cumple; jerarquía UI alineada con backend. Un soft-gap de UI (Anular sin `compras:write`) se corrigió en front.

- GET estáticos: **54 OK** / **0 fail crítico** / 0 HTTP 400
- Flujo aprobaciones: **19 pass** / **0 fail** / 0 skip
- Smoke UI roles: **5/5** (solicitante, aprobador, lectura, digitador, admin)
- Gaps críticos front↔Nest: **0**

## Logins

| Usuario | Email | OK |
|---------|-------|----|
| admin | admin@almahue.local | OK |
| aprobador | qa.aprobador@almahue.local | OK |
| solicitante | qa.solicitante@almahue.local | OK |
| lectura | qa.lectura@almahue.local | OK |
| digitador | jsanchez@almahue.cl | OK |

## 1) Barrido GET (admin vía proxy)

Paths únicos en `real/api.ts`: **180** (GET estáticos: **54**). Incluye `gosocket/status`.

| Path | Status | Clase |
|------|--------|-------|
| `actividades` | 200 | OK |
| `anticipos-productores` | 200 | OK |
| `aprobaciones-oc` | 200 | OK |
| `asientos` | 200 | OK |
| `auth/me` | 200 | OK |
| `balance-8-columnas?periodo=2026-07` | 200 | OK |
| `bodegas` | 200 | OK |
| `cartolas-bancarias` | 200 | OK |
| `clientes` | 200 | OK |
| `conciliaciones` | 200 | OK |
| `config-contable-sii` | 200 | OK |
| `contratistas` | 200 | OK |
| `cuentas` | 200 | OK |
| `cuentas-corrientes` | 200 | OK |
| `dashboard/kpis` | 200 | OK |
| `dashboard/notificaciones` | 200 | OK |
| `dashboard/tendencia` | 200 | OK |
| `documentos` | 200 | OK |
| `documentos-aging` | 200 | OK |
| `dtes` | 200 | OK |
| `elementos-costo` | 200 | OK |
| `empresas` | 200 | OK |
| `factores-honorario` | 200 | OK |
| `gosocket/status` | 200 | OK |
| `guias-despacho` | 200 | OK |
| `indicadores-bc` | 200 | OK |
| `ingresos-labor-diario` | 200 | OK |
| `insumos` | 200 | OK |
| `labores` | 200 | OK |
| `libro-comercial` | 200 | OK |
| `libro-diario?periodo=2026-07` | 200 | OK |
| `mayor?periodo=2026-07&cuentaId=1` | 200 | OK |
| `monedas` | 200 | OK |
| `movimientos-bodega` | 200 | OK |
| `movimientos-caja` | 200 | OK |
| `ordenes-compra` | 200 | OK |
| `pagos` | 200 | OK |
| `periodos-contables` | 200 | OK |
| `presupuestos` | 200 | OK |
| `proformas-contratista` | 200 | OK |
| `prospectos` | 200 | OK |
| `proveedores` | 200 | OK |
| `recepciones-oc` | 200 | OK |
| `registros-compra` | 200 | OK |
| `reportes-contables` | 200 | OK |
| `roles` | 200 | OK |
| `sync-bc-meta` | 200 | OK |
| `tarifas-contratista` | 200 | OK |
| `tipos-documento` | 200 | OK |
| `unidades` | 200 | OK |
| `usuarios` | 200 | OK |
| `workflows` | 200 | OK |
| `workflows-admin` | 200 | OK |
| `health` | 200 | OK |

### GET parametrizados (probe)

| Path | Status | Nota |
|------|--------|------|
| `cartolas-bancarias/:param/movimientos` | 404 | 404 entidad (ruta existe) |
| `conciliaciones/:param/movimientos` | 404 | 404 entidad (ruta existe) |
| `cuentas-corrientes/:param/movimientos` | 200 | ok/other |
| `dtes/:param/estado` | 404 | 404 entidad (ruta existe) |
| `gosocket/documentos/:param/:param` | 404 | falso positivo: segundo segmento debe ser pdf|xml (literal Nest); ruta existe |
| `ui/table-preferences/:param` | 200 | ok/other |

## 2) Flujo aprobaciones (pass/fail)

| Paso | Status | Resultado | Nota |
|------|--------|-----------|------|
| solicitante_crear_OC_PENDIENTE | 201 | PASS |  |
| solicitante_crear_OC_2_para_rechazo | 201 | PASS |  |
| solicitante_aprobar_OC_debe_403 | 403 | PASS | PUT estado APROBADO sobre OC EMITIDO con bandeja pendiente |
| lectura_crear_OC_debe_403 | 403 | PASS |  |
| digitador_GET_compras_debe_403 | 403 | PASS |  |
| aprobador_listar_bandeja_aprobaciones-oc | 200 | PASS |  |
| aprobador_listar_ordenes_compra | 200 | PASS |  |
| aprobador_aprobar_OC | 200 | PASS | OC.estado=EMITIDO al crear; aprobación vía PUT APROBADO |
| aprobador_rechazar_OC | 200 | PASS |  |
| solicitante_pedir_aprobacion_proforma | 200 | PASS | ya existía PENDIENTE_APROBACION |
| solicitante_aprobar_proforma_debe_403 | 403 | PASS |  |
| digitador_aprobar_proforma_debe_403 | 403 | PASS |  |
| aprobador_aprobar_proforma_definitiva | 201 | PASS |  |
| aprobador_rechazar_proforma | 201 | PASS |  |
| admin_workflows_compras_con_aprobadores | 200 | PASS |  |
| admin_workflows_contratistas_con_aprobadores | 200 | PASS |  |
| admin_GET_workflows | 200 | PASS |  |
| aprobador_bandeja_pendientes_detalle | 200 | PASS | AprobacionOc.estado=PENDIENTE (OC puede seguir EMITIDO) |
| gosocket_documentos_pdf_ruta | 200 | PASS | Front usa /pdf|/xml literal; probe UUID/UUID no es gap real |

### Contrato observado

- `POST ordenes-compra` con `estado: EMITIDO` + `aprobadorId` → OC queda **EMITIDO** y se crea fila en **aprobaciones-oc** (`PENDIENTE`).
- Aprobar/rechazar: `PUT ordenes-compra/:id` con `estado: APROBADO|RECHAZADO` (solo jefe asignado).
- Solicitante al aprobar → **403**. Lectura al crear → **403**. Digitador (`jsanchez@almahue.cl`) GET compras → **403**.
- Proformas: `solicitar-aprobacion` / aprobar vía `definitiva` / `rechazar`. No existe `.../aprobar`.
- `workflows-admin`: módulos Compras y Contratistas con `aprobadorIds` (incluye U-16 QA Aprobador).

## 3) Gaps front ↔ Nest

No hay inconexiones críticas entre `real/api.ts` y controllers Nest. El barrido GET no devolvió 404 de ruta ni 5xx.

**Gaps críticos: ninguno.**

Rutas Nest sin uso directo en front (informativo): **13**.

### Observaciones soft

- **OC_ESTADO_EMITIDO_VS_PENDIENTE**: POST ordenes-compra con estado EMITIDO no cambia OC a PENDIENTE; la pendiente vive en aprobaciones-oc

## 4) Smoke UI MODO REAL (browser)

Proxy Vite `:5174` → Nest `:3001`. Badge **MODO REAL** + **GOSOCKET DEMO** visibles en todos los roles.

| Rol | Menú / acciones | Resultado |
|-----|-----------------|-----------|
| QA Solicitante | Compras/Ventas/Contratistas; **Nueva OC** sí; **Aprobar** no; sin Administración | PASS |
| QA Aprobador | Bandeja `/compras/aprobaciones` con **Aprobar** / **Rechazar** | PASS |
| QA Lectura | Sin Nueva OC / sin Aprobar; solo `*:read` | PASS (tras fix Anular) |
| Digitador (`jsanchez`) | Solo Contratistas; **Nueva proforma** sí; bandeja aprobaciones **sin** Aprobar/Rechazar | PASS |
| Admin | `/admin/aprobaciones` reglas Compras/Contratistas con QA Aprobador (QAAPROB) | PASS |

### Fix aplicado en esta pasada

- `ComprasPages.tsx`: botones **Anular** (lista OC) y **Editar/Anular/Carga/Registrar** (libro compras) ahora requieren `compras:write`. Antes lectura veía Anular en grilla aunque el API denegaría escritura.

Captura: [`capturas-flujo-completo/admin-reglas-aprobacion.png`](./capturas-flujo-completo/admin-reglas-aprobacion.png).

## Conteos finales

```json
{
  "getPass": 54,
  "getFail": 0,
  "get400": 0,
  "flowPass": 19,
  "flowFail": 0,
  "flowSkip": 0,
  "uiSmokePass": 5,
  "criticalGaps": 0,
  "highGaps": 0,
  "frontUniquePaths": 180,
  "nestRoutes": 194
}
```

Artefacto crudo: [`07-FLUJO-COMPLETO-API.json`](./07-FLUJO-COMPLETO-API.json).