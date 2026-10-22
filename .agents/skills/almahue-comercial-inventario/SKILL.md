---
name: almahue-comercial-inventario
description: OC Compras (cotiz solo referencia) vs Orden de venta Ventas, stock por bodega, flete, lookup RUT. Use when working on documentos comerciales, OV, inventario, emitir factura, o insumos/bodegas.
---

# Comercial e inventario (Reu6 D7, D11–D17)

## Dos flujos distintos

| Menú | Tipo | Receptor | Convierte a | Stock |
|---|---|---|---|---|
| Compras › Órdenes de compra | `OrdenCompra` | Proveedor | — (cadena PIN) | No (entrada por Insumos) |
| Ventas › Orden de venta | `ORDEN_VENTA` | Cliente | Factura | Sí, al confirmar |

La cotización del proveedor **no es documento del ERP**: campos opcionales `referenciaTipo` / `referenciaFolio` / `referenciaFecha` en la OC. Sin menú Cotizaciones, sin `convertirCotizacionAOc`, sin alta `tipo=COTIZACION`. Redirects `/compras/cotizaciones` y `/comercial/cotizaciones` → `/compras/ordenes`. No poner cotización de cliente en Ventas.

## Inventario

- Saldo físico = `StockInsumoBodega.cantidad`.
- Al **confirmar** OV: movimiento `SALIDA_VENTA` (descuenta físico). Si existiera `ReservaStock` residual, se consume; **no** hay cadena que cree reservas.
- Factura **no** mueve stock otra vez.
- Mantenedor: Insumos › Stock por bodega / producto (`/insumos/stock`).
- **Emitir** factura exige OV propia facturable (`CONFIRMADA`/`EMITIDO`); no alta libre de FACTURA.

## Precio y flete

- D16: no vender producto bajo costo (regla fija en OV/emisión; no hay flag ni combo en Empresa). Sin concepto «merma» (no aplica a fruta).
- D17: `tipoLinea: FLETE` — línea extra, no recargo SII.

## Lookup RUT (D7)

`GET /comercial/lookup-rut?rut=` filtrado por `empresaId`: sociedad, clientes, proveedores.

## Huecos (no «ya está»)

- Lookup RUT: sociedad + clientes + proveedores + flag `esProductor`. **Maestro Productor** sigue fuera (no hay entidad `Productor`).
- `ventaBajoCosto` **eliminado**: la regla es fija (bloquear). No hay UI ni flag en Empresa.
- Wizard **Emitir** (`/comercial/emitir`): FACTURA/NC/ND/GUIA (pantalla de **emisión**). Sin columna de cuenta. Libro ventas: **solo DTE** (sin OV). DTE emitido = «Por contabilizar»; click → cuenta por ítem → `CONTABILIZADA`. OV confirmada se factura desde Emitir. Borradores DTE viven en Emitir. No ampliar a COTIZ/NP/OC.
- FLETE: en OV como `tipoLinea`; cotización/emitir pueden no ofrecerlo igual. Canonical DTE **no auditado** (recargo SII).
- Catálogo `pantallas-permisos` alineado 21/08 (OV/Guías en Ventas; Compras sin Cotizaciones). Revalidar si cambia el menú.
- Guías de despacho: **hay UI** Ventas › Guías (`/comercial/guias-despacho`); despacho logístico sigue incompleto.
- Recepción OC **no** incrementa `StockInsumoBodega`; entrada por Insumos › Movimientos (`ENTRADA_PROVEEDOR`).

## Cadena y OC (21/08)

- Aprobación **solo OC** (grupos/escalas Compras). OV **no** pasa por bandeja: `BORRADOR` → confirmar stock (`CONFIRMADA`) → factura. `APROBADO` es solo OC.
- Wizard OC: **Guardar borrador** (`BORRADOR`) vs **Enviar a aprobación** (`PENDIENTE_APROBACION`). Correlativo `OC-AAAA-NNNN` al crear. Cotización = referencia opcional (tipo, folio, fecha); no hay atajo cotiz→OC.

## No implementar / no restaurar

- Traspaso gastos próxima temporada (Reu6 diferido).
- DTE GoSocket real sin credenciales ni CAF en portal. El ERP tiene HTTP a `billing-gateway` (skill `almahue-billing-dte`); SII live sigue fuera.
- **No** restaurar cotización → nota de pedido → factura (Reu5). **No** restaurar menú/CRUD de Cotizaciones ni convertir `COTIZACION` → OC.

