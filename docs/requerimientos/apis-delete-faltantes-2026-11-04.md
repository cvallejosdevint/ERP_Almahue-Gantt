# APIs DELETE de parametrización (2026-11-04, actualizado 2026-11-05)

## Regla vigente

1. Activar / Desactivar: disponible para quien tenga write del catálogo.
2. Eliminar (hard-delete): **solo administrador** (`ROL-1` o permiso `*`) y **solo si el registro ya está desactivado** (o anulado, en elementos de costo).
3. Si hay FK (P2003): `409 Conflict` - no se borra; hay que quitar referencias.

Helper back: `assertCatalogHardDelete` en `erp_back/src/auth/catalog-hard-delete.util.ts`.  
Helper front: `canHardDeleteCatalogo` en `erp_front/src/lib/permissions.ts`.  
DELETE de catálogos: permiso Nest `admin:write`.

## DELETE implementados (con la regla)

| Recurso | Endpoint |
|---|---|
| Unidades | `DELETE /unidades/:id` |
| Tipos documento | `DELETE /tipos-documento/:id` |
| Centros de costo | `DELETE /centros-costo/:id` |
| Conceptos flujo | `DELETE /conceptos-flujo/:id` |
| Códigos financieros | `DELETE /codigos-financieros/:id` |
| Áreas de negocio | `DELETE /areas-negocio/:id` |
| Elementos de costo | `DELETE /elementos-costo/:id` (solo `vigencia=ANULADO`) |
| Labores / actividades / sectores / faenas | `DELETE /labores|actividades|sectores-contratista|faenas-contratista/:id` |
| AF familias / subfamilias / ubicaciones | `DELETE /activo-fijo/.../:id` |
| Bancos | `DELETE /bancos/:id` |
| Monedas | `DELETE /parametrizacion/monedas/:id` |
| Cuentas contables | `DELETE /cuentas/:id` (cuenta deshabilitada + sin uso) |
| Empresas | `DELETE /empresas/:id` (ya era solo Super Admin; UI exige inactiva) |

## Sin DELETE (solo desactivar / ciclo de vida propio)

| Recurso | Nota |
|---|---|
| Clientes / proveedores / productores | Toggle activo; no hard-delete |
| Insumos (artículos) | Sin flag activa de catálogo; inventariable ≠ baja |
| Bodegas | Toggle activa en UI; **sin** DELETE API |
| Tipos contrato contratista | Falta DELETE si se pide |
| Ficha contratista | Preferir inactivar |
| Usuarios | Solo desactivar |
| Factores honorario / IPC AF / activos fijos bienes | Histórico / baja operativa |
| OC / OV / DTE / asientos / pagos | Anulación / reversa / borrador |

## Auditoría UI (resto)

| Módulo | Estado |
|---|---|
| Parametrización catálogos + AF + contratistas param | Activar/Desactivar + Eliminar (admin, inactivo) |
| Plan de cuentas | Deshabilitar + Borrar solo admin/inactiva |
| Bodegas | Toggle activa cableado |
| Clientes | Toggle activo; sin Eliminar |
| Presupuestos | viewFirst + Eliminar (API propia; no es catálogo param) |
| Tesorería / compras / emitir | Documental; sin hard-delete de maestros |
