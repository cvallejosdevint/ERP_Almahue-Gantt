# Gaps muestra 21/10/2026

Cadena nueva ALM > Export. Sin secretos.

## Producto (cerrado en codigo local)

- `LineaCompraDto` acepta `elementoCostoId` / `elementoCosto`. La recepcion CONFIRMADA usa linea o header. Alias `RECEPCIONADA` > `CONFIRMADA` (el estado del documento OC sigue siendo RECEPCIONADA).
- Wizard OC: combo Elemento en la linea si la cuenta `requiereElemento`.
- `POST registros-compra/sync` solo upserta DTE con FchEmis en `[desde, hasta]`. Sin fecha usable no inserta. No auto-vincula OC si el XML no trae referencia. Folio 64 se conserva. Folios sandbox 56-63 no se rehidratan.
- Contabilizar DTE `tipoLinea=SERVICIO`: no exige articulo inventariable si hay `insumoId` o descripcion. Libro ventas ya manda CC si la cuenta lo pide.
- `POST /documentos/:id/convertir` responde `{ origen, convertido }`. Usar `convertido.id`.

## Datos de la muestra

- OC Export: OC-2026-0001 (RECEPCIONADA)
- DTE ALM folio oficial 64, estado CONTABILIZADA
- DTE Export folio oficial 93, estado CONTABILIZADA
- Libro compras factura 64 asociada a la OC, asiento 20260003
- Recepcion asiento 20260004
- Activo Equipo packing muestra, factura 64, neto 50000
- Ingreso diario CTR + proforma PF-00001 DEFINITIVA (periodo 2026-10)
- Pago TEF ALM calce folio 64, estado PENDIENTE (sin cartola). CC y nomina leen ese folio.
- Movimiento `ENTRADA_PROVEEDOR` facturaRef 64 (servicio) y facturaRef 65 (guia 57 / OC-2026-0002).
- Camino bueno INSUMOS 21/10: ALM emitio guia 52 folio 57 y factura 33 folio 65. Export: OC-2026-0002 APROBADA > recepcion guia > Vincular 65 > Aceptar GoSocket > Contabilizar madre asiento 20260006. Recibo SII de la guia 57 sigue Error (GoSocket HTTP 502 GOSOCKET_INVALID_RESPONSE) tras 3 reintentos del 30 y del 32; no bloquea bodega ni asiento ni el cierre.
- NC/ND/34/110 no se emitieron contra 65 para no romper el cuadre. Vias cubiertas: Emitir ALM (52 y 33), Traer guias, OC INSUMOS, asociar guia, Vincular OC, Aceptar, Contabilizar madre (tambien desde Libro de guias).
- Cierre de bodega 2026-10 ejecutado. Asiento 20260007 tipo CIERRE origen CIERRE-BODEGA:2026-10, 66250 (SALIDA_VENTA: debe 6-2-02-01-003 AJUSTES DE INVENTARIO / haber 1-1-08-01-003 EXISTENCIA INSUMOS). Periodo contable sigue ABIERTO. Entradas 64 y 65 no reasientan: ya estaban en COMPRAS 20260003 y 20260006.
- Facturas sandbox 61, 62 y 63: OC-2026-0003 / 0004 / 0005 SERVICIO (9500, 20000, 30000), PIN 4821, asociadas en libro. Siguen EMITIDO (no se contabilizaron para no mover el cuadre de 64/65).

## Speech / bitacora

- Cartola import-only: no se finge Excel. Flujo/conciliacion sin cartola.
- Aprobaciones CTR: pantalla con speech "sin cadena" (D4). El codigo de `marcarProformaDefinitiva` todavia arma `PENDIENTE_APROBACION` si hay grupo; en la muestra se cerro a DEFINITIVA por API. No se reabre bandeja ni PIN de proformas.
- Reporteria ventas SII / cliente-producto: endpoints 200. Si la grilla no muestra 93, el corte de la hoja no calza con el DTE; no se relleno con fixtures viejos.
- Front: `ActivoFijoPages.tsx` tenia un `=` suelto (overlay Vite). Se quito.

## Legado

APIs o bookmarks **sin hoja** en `MENU` de `ERP/erp_front/src/app/Sidebar.tsx`. Prefijo Nest: `/api/v1`. **No reabrir D11 / D4 / D7.** No restaurar CRUD de cotizaciones, cadena de OV ni buscador RUT en Emitir.

- **Cotizaciones (D11, no reabrir).** No hay controller `cotizaciones` ni item MENU. La cotizacion del proveedor es referencia opcional (`referenciaTipo` / folio / fecha) en la OC. `POST /api/v1/documentos` con `tipo=COTIZACION` responde 400; `GET /api/v1/documentos?tipo=COTIZACION` lista vacia; `GET /api/v1/documentos/:id` de una COTIZACION historica responde 404; `POST /api/v1/documentos/:id/convertir` rechaza origen COTIZACION (tampoco NP). Bookmarks: `/compras/cotizaciones` y `/comercial/cotizaciones` redirigen a `/compras/ordenes`. No hay atajo cotiz > OC.
- **`workflows-admin` (DK-G8, no promover).** CRUD en `admin.controller.ts` sobre `WorkflowConfig`: `GET` / `POST /api/v1/workflows-admin`, `PUT` / `DELETE /api/v1/workflows-admin/:id` (`admin:read` / `admin:write`). No hay hoja MENU. Administracion > Reglas de aprobacion (`/admin/aprobaciones`) usa grupos + escalas. El cliente `getWorkflowsAdmin` existe en `api.ts` y ninguna pantalla lo llama. `computeCadenaAprobacion` aun puede cruzar ese pool: no mezclarlo con grupos/escalas ni armar UI nueva.
- **`buscarReceptor` (D7, no reabrir).** No hay ruta Nest ni metodo. Se elimino de Ventas > Emitir DTE (el receptor se elige por nombre). `GET /api/v1/lookup-rut` sigue vivo para ficha / OV / proveedores; no es `buscarReceptor` y no debe volver a Emitir.
- **`GET /api/v1/workflows` (lectura operativa, no es pantalla).** `ComercialController.getWorkflows`: digitadores con `comercial:read` / `compras:read` / `contratistas:read` (o `admin:read`) leen `WorkflowConfig` sin exigir `admin:read`. Sin hoja MENU. Wrapper front `getWorkflows` en `api.ts`; las pantallas de reglas van a `grupos-aprobacion` / `escalas-aprobacion`. Sigue vivo para digitadores; no tomarlo como fuente de verdad de la cadena.

Datos de IDs: `muestra.json`.
