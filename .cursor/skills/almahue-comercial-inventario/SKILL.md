---
name: almahue-comercial-inventario
description: Cotización Compras vs Orden de venta Ventas, stock por bodega, flete, lookup RUT. Use when working on documentos comerciales, OV, cotizaciones, inventario, emitir factura, o insumos/bodegas.
---

# Comercial e inventario (Reu6 D7, D11–D17)

## Dos documentos distintos

| Menú | Tipo | Receptor | Convierte a | Stock |
|---|---|---|---|---|
| Compras › Cotizaciones | `COTIZACION` | Proveedor | OC | No |
| Ventas › Orden de venta | `ORDEN_VENTA` | Cliente | Factura | Sí, al confirmar |

No reutilizar `CotizacionesPage` para ventas. No poner cotización de cliente en Ventas.

## Inventario

- Saldo físico = `StockInsumoBodega.cantidad`.
- Al **autorizar** OV (último paso de cadena): `ReservaStock` ACTIVA **7 días** (no descuenta físico).
- Disponible = físico − reservas ACTIVA no vencidas.
- Al **confirmar** OV: consume reserva (`CONSUMIDA`) + movimiento `SALIDA_VENTA`.
- Factura **no** mueve stock otra vez.
- Mantenedor: Insumos › Stock por bodega / producto (`/insumos/stock`).
- **Emitir** factura exige OV propia facturable (`APROBADO`/`EMITIDO`); no alta libre de FACTURA.

## Precio y flete

- D16: no vender bajo costo (`ventaBajoCosto` = `BLOQUEAR` por defecto). Sin concepto «merma» (no aplica a fruta).
- D17: `tipoLinea: FLETE` — línea extra, no recargo SII.

## Lookup RUT (D7)

`GET /comercial/lookup-rut?rut=` filtrado por `empresaId`: sociedad, clientes, proveedores.

## Huecos (no «ya está»)

- Lookup RUT: sociedad + clientes + proveedores + flag `esProductor`. **Maestro Productor** sigue fuera (no hay entidad `Productor`).
- `ventaBajoCosto` en `Empresa` (default **BLOQUEAR**) + validación OV. **Sí hay UI** Admin › Empresas (retest 19/08).
- Wizard **Emitir** (`/comercial/emitir`): FACTURA/NC/ND/GUIA (pantalla de **emisión**). Libro ventas es el libro, no el alta. Borradores DTE viven en Emitir. No ampliar a COTIZ/NP/OC. Factura desde OV: cuenta por línea **opcional** en piloto.
- FLETE: en OV como `tipoLinea`; cotización/emitir pueden no ofrecerlo igual. Canonical DTE **no auditado** (recargo SII).
- Catálogo `pantallas-permisos` alineado 14/08 (OV/Guías en Ventas; Cotizaciones en Compras). Revalidar si cambia el menú.
- Guías de despacho: **hay UI** Ventas › Guías (`/comercial/guias-despacho`); despacho logístico sigue incompleto.
- Recepción OC **no** incrementa `StockInsumoBodega`; entrada por Insumos › Movimientos (`ENTRADA_PROVEEDOR`).

## Cadena y OC (piloto 18/08)

- Flag `comercialRequiereAprobacion` **ON** (migración `20260818180000`). Confirmar OV exige `AUTORIZADA` si el monto entra en cadena. Factura desde OV: sin segunda cadena.
- Wizard OC: **Guardar borrador** (`BORRADOR`) vs **Enviar a aprobación** (`PENDIENTE_APROBACION`). Correlativo `OC-AAAA-NNNN` al crear en wizard; cotiz→OC usa `OC-{folio}-{ts}`.

## No implementar / no restaurar

- Traspaso gastos próxima temporada (Reu6 diferido).
- DTE GoSocket real sin credenciales ni CAF en portal. El ERP tiene HTTP a `billing-gateway` (skill `almahue-billing-dte`); SII live sigue fuera.
- **No** restaurar cotización → nota de pedido → factura (Reu5). Cotización Compras convierte a **OC**.

