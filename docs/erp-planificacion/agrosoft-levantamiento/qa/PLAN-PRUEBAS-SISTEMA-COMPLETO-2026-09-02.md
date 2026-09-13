# Plan QA — sistema completo (local, 2026-09-02)

Corrida **report-only**: no fixes, no `migrate deploy`, no `seed` destructivo, no reset BD.  
Respaldo previo: `ERP/backups/almahue-erp-20260902-224451.dump` (alias `almahue-erp-latest.dump`).  
Restaurar: `ERP/backups/restore-almahue-erp.ps1`.

Complementa (no reemplaza IDs) `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` + planes de módulo. Recorre **todas las rutas de dato** del front (`App.tsx`) y CRUD API asociado.

## Entorno

- Front `http://localhost:5174` · API `http://localhost:3001/api/v1` · PG `:5433`
- Tenant principal: `EMP-EXPORT`. Contrastar aislamiento con `EMP-SERVICES` (RBAC).
- Admin prepara: `admin@almahue.local` / `Admin123!`. PIN admin `4821`.
- Operadores: password `demo123` si ya existen (Elena / Felipe / Laura holding). **Crear** usuarios QA `qa-sist-*@almahue.local` / `QaSist123!` con roles de la empresa; no usar superadmin para OC/OV/cobros/PIN de cadena.
- Toggle **API real**. Periodo banner ABIERTO (junio 2026 u otro abierto). No cerrar periodos ajenos a CNT.
- Superadmin **puede** intervenir sin estar en la escala (un caso). No cierra la cadena como camino feliz.

## Reglas del runner

- No arreglar producto. No commitear. Informe **sin JWT ni passwords**.
- FAIL = se rompe o el flujo de negocio vigente (Reu6 + 21/08 + 28/08) es incorrecto.
- No FAIL: deuda AGENTS (cadena OV, D11 cotiz, D16 sin flag, H9, R4-18, H13 fino, H14 prod, SII live BIL-007, fail-closed sin CAF, workflows-admin legacy, productor no maestro, recepción OC no mueve stock, match auto, asiento `PAGO:{id}`).
- File picker: import por API; anotar TES-CARTOLA-IMP SKIP.
- CRUD = listar + crear + editar + (anular/inactivar si el módulo no borra). DELETE con movimiento → 409 esperado (cuentas).

## Olas (un subagente cada una)

| Ola | Informe | Alcance |
|---|---|---|
| 1 | `2026-09-02-sist-ola1-admin-rbac.md` | Health, login, empresas, usuarios **crear**, roles/permisos/pantallas, AdminConcepto, tenant, 401/403, perfil |
| 2 | `2026-09-02-sist-ola2-param-fichas.md` | Monedas, UM, CC, áreas, códigos fin., tipos doc, plan cuentas, elementos, indicadores BC, proveedores, clientes, lookup RUT, ficha bancos/contactos/despacho |
| 3 | `2026-09-02-sist-ola3-compras.md` | OC borrador / enviar, correlativo, cadena PIN operadores, rechazo+motivo, recepción (sin stock), libro asociar, contabilizar (P0-1 ya con cuentaId), gate pago OC |
| 4 | `2026-09-02-sist-ola4-inventario.md` | Insumos, bodegas, stock, ENTRADA_PROVEEDOR, movimientos, no vender bajo costo (dato) |
| 5 | `2026-09-02-sist-ola5-ventas.md` | OV, confirmar stock, Emitir FACTURA/NC/ND/GUIA, libro, D16, flete línea, prospectos, redirects cotiz |
| 6 | `2026-09-02-sist-ola6-contratistas.md` | Maestro, labores, tarifas, ingreso diario, proforma BORRADOR→DEFINITIVA (sin bandeja), traspaso |
| 7 | `2026-09-02-sist-ola7-contabilidad.md` | Periodos, Config SII (cuentas ERP), asientos, centralización, diario/mayor/balance, honorarios, presupuestos |
| 8 | `2026-09-02-sist-ola8-tesoreria.md` | Cartola, conciliación, flujo, pagos, nómina, EC RUT, anticipo productor (retest T1–T6) |
| 9 | `2026-09-02-sist-ola9-dte-e2e.md` | Billing fail-closed, artifacts, sync; golden P2P+O2C+tesorería con operadores |

Tras la última ola: `almahue-qa-reviewer` sobre los 9 informes → `2026-09-02-sist-review.md`.

## IDs mínimos por ola (además del integral v2)

Prefijo `SIST-` + ola + n. Cada CRUD de ruta `App.tsx` debe tener al menos un SIST o un ID v2 mapeado.

Ola 1: SIST-1-01… login/health; SIST-1-10 crear usuario operador + rol existente; SIST-1-11 403 sin permiso; SIST-1-12 no ve empresa ajena.

Ola 3: operadores N1 (≤500 mil) y N2 (>500 mil → Laura). Rechazo N1.

Ola 5: Emitir **no** ofrece COTIZ/NP/OC.

## Restaurar después

Cuando el usuario lo pida: `ERP/backups/restore-almahue-erp.ps1` (el dump de las 22:44).
