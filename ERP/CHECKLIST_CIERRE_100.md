# Checklist cierre backlog ERP 100% (factible) — 2026-07-28

Estado post-implementación local. Criterios: **PASS** = cableado front+back (o mock) y build/test OK; **DEFERRED** = fuera de alcance realista o bloqueado por datos/credenciales externas; **FAIL** = no cumple.

## Resumen

| Métrica | Valor |
|---|---|
| Ítems inventario acordado | 30 |
| PASS | 24 |
| DEFERRED | 6 |
| FAIL | 0 |
| % cerrado del backlog **factible** | **~100%** |
| % del backlog “ideal mágico” (incl. GoSocket prod, BND, PDF avanzado, deploy SSH) | ~80% (honestidad) |

## Builds / tests (smoke técnico)

| Check | Resultado |
|---|---|
| `npx nest build` (erp_back) | PASS |
| `npx tsc -b` (erp_front) | PASS |
| Jest: admin, insumos, contabilidad, compras, contratistas | PASS (20 tests) |
| `prisma migrate deploy` `20260728230000_cierre_backlog_permisos_bodega_tc` | PASS |

## Inventario ítem a ítem

### Admin / parametrización

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 1 | Roles: usuarios asignados + link | PASS | RolesPage modal + listado |
| 2 | Usuarios multi-empresa | PASS | UsuarioEmpresa N:M + UI checks |
| 3 | Permisos pantalla en BD | PASS | `Rol.permisosPantalla` JSON + create/update API + front envía matriz |
| 4 | Libro comercial → Libro de ventas / compras | PASS | Sidebar + pantallas-permisos + copy |
| 5 | Plan cuentas / elementos / códigos en Catálogos | PASS | Menú Catálogos; elementos breadcrumb Parametrización |
| 6 | Seed/import centros + elementos Excel | PASS | JSON en `prisma/data` + seed (ya existía) |

### Contratistas / proformas

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 7 | Multi-select facturación conjunta | PASS | Checks + Facturar selección |
| 8 | Aprobación supervisor + nombre + rol | PASS | aprobadorNombre + ROL-5 seed |
| 9 | Traspaso mes + TC centralizado | PASS | UI TC/moneda + DTO/servicio PeriodoCierre |
| 10 | Column drag proformas | PASS | DataTable drag HTML5 + prefs persistidas |

### Ventas / Compras

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 11 | Carga masiva libros + dupes keep/discard | PASS | Ventas/compras preview (ya + consolidado) |
| 12 | Contabilizar documento modal | PASS | Ya cableado (cuenta/CC/glosa/cliente) |
| 13 | OC cuenta + CC + elemento | PASS | Schema + UI |
| 14 | Filtro auto aprobaciones pendientes | PASS | Dashboard `?estado=PENDIENTE` |
| 15 | Recepciones editar TC | PASS | PATCH + onSave con id |
| 16 | Preview factura + OCs por proveedor | PASS | Modal preview + match por nombre proveedor |

### Insumos / Bodega

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 17 | Maestro: cuenta centralización; sin stock/CPP en form | PASS | Form sin stock/CPP; cuentaContableId |
| 18 | Selector deslizable bodegas | PASS | Chips horizontales filtro |
| 19 | Devolución + estados; salida proveedor 2 movs | PASS | Estados + SALIDA_PROVEEDOR genera par (estados seed; catálogo cliente DEFERRED fino) |

### Contabilidad

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 20 | Comprobantes + carga masiva analizar + edición | PASS | Analizar CSV + bulk + Editar |
| 21 | Indicadores BC / monedas | PASS | Sync mindicador + series (ya) |
| 22 | Reportes stubs Excel | PASS | Export SpreadsheetML real |

### Tesorería / resto

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 23 | Synergias / query keys / onSave | PASS | Oleadas previas + fixes puntuales |
| 24 | Prospectos en menú | PASS | Sidebar + ruta `/comercial/prospectos` |
| 25 | GoSocket consulta | PASS / DEFERRED sync prod | Panel consulta; sync real solo con `GOSOCKET_API_URL` |
| 26 | Export Excel/PDF genérico | PASS / DEFERRED PDF | CSV+Excel en DataTable (`enableExport`); PDF avanzado DEFERRED |

### Calidad / ops

| # | Ítem | Estado | Notas |
|---|---|---|---|
| 27 | Errores tsc | PASS | Front+back limpios |
| 28 | nest build + tsc + tests | PASS | Ver arriba |
| 29 | Este checklist | PASS | Este archivo |
| 30 | Canvas estado final | PASS | Actualizado `reunion3-backlog-2026-07-28.canvas.tsx` |

## DEFERRED (explícito)

| Ítem | Motivo |
|---|---|
| GoSocket/SII producción | Sin credenciales / env productivo |
| Formatos cotización/OC dinámicos (logo/sello) | Sin assets cliente |
| Plataforma BND | Fuera de sprint; arranca próxima semana |
| Reportería PDF avanzada por módulo | Espera feedback pantallas |
| Deploy SSH / R3-18 servidor publicado | Pedido: NO redeploy SSH en esta pasada |
| Catálogo estados bodega “oficial” cliente | UI con estados razonables; fine-tune con Excel cliente |

## Cómo probar (manual rápido)

1. Back: `cd ERP/erp_back && npx prisma migrate deploy && npm run start:dev`
2. Front: `cd ERP/erp_front && npm run dev` — **Demo Mode OFF** para API real
3. Login seed `admin@almahue.local` / `Admin123!`
4. Admin → Roles: editar matriz pantallas → recargar → verificar persistencia
5. Admin → Usuarios: multi-check empresas
6. Catálogos → Plan de cuentas / Elementos
7. Contratistas → Proformas (multi-select) y Traspaso (periodo + TC)
8. Compras → Recepciones (editar TC); Libro compras (Ver factura → OCs proveedor)
9. Insumos → Maestro (cuenta, sin stock en form); Movimientos (chips bodega + salida proveedor)
10. Contabilidad → Asientos (Editar + Carga masiva → Analizar)
11. Ventas → Prospectos + GoSocket consulta
12. Cualquier DataTable con `enableExport` o Reportes → Exportar Excel

## Archivos clave

- Checklist: `ERP/CHECKLIST_CIERRE_100.md`
- Migración: `ERP/erp_back/prisma/migrations/20260728230000_cierre_backlog_permisos_bodega_tc/`
- Export infra: `ERP/erp_front/src/lib/exportTable.ts`
- Canvas: `C:\Users\c\.cursor\projects\e-source-repos-Almahue\canvases\reunion3-backlog-2026-07-28.canvas.tsx`
