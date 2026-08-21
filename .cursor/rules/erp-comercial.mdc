---
description: Cotización Compras vs Orden de venta Ventas; no mezclar flujos
globs: ERP/erp_{back,front}/**/*.{ts,tsx}
alwaysApply: false
---

# Comercial Almahue

- Cotización (`COTIZACION`) = Compras, receptor proveedor, convierte a **OC** (no NP, no factura).
- Orden de venta (`ORDEN_VENTA`) = Ventas, receptor cliente, stock al **confirmar**, factura copia qty/desc (precio editable).
- No reutilizar `CotizacionesPage` para OV. No cotización de cliente en menú Ventas.
- No usar wizard Emitir para cotización/NP/OC.
- No vender producto bajo costo: regla fija en OV/emisión, no parámetro de empresa ni combo en Admin › Empresas.
- Lookup: sociedad + clientes + proveedores + flag `esProductor`; no hay maestro Productor.
