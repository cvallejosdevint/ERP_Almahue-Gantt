---
name: almahue-ficha-contraparte
description: Ficha única cliente/proveedor (bancos, contactos, despacho); productor aún no maestro. Use when editing FichaContraparte or lookup-rut.
---

# Ficha de contraparte

## As-is (D7–D8)

- Ficha única cliente/proveedor: bancos, contactos, despacho, historial, `solicitadoPor`.
- **Cliente nacional:** dirección fiscal + comuna **obligatorias** (SII HED-3-845/846). Ciudad se completa con comuna si viene vacía. El alta en Ventas › Clientes y `createCliente`/`updateCliente` fallan sin esos datos. `getClientes` incluye `direcciones` de ficha.
- Helpers en `modules/ficha/`; sin controller propio obligatorio.
- UI: `FichaContraparteModal`, clientes comercial, `FichaProveedoresPage`.
- Lookup RUT (`GET /comercial/lookup-rut`): sociedad + clientes + proveedores. Flag `esProductor` + arreglo `productores[]`. **No hay maestro Productor** (entidad aparte).

## No

- PDF servidor: no hay; sí hay print HTML «Imprimir solicitud» (H5 piloto).
- No inventar entidad Productor ni pantalla maestra hasta pedido.
- SMTP, cobranza R4-18 y DTE real: diferidos, no van en ficha.

D11: cotización usa proveedor; OV usa cliente. No mezclar receptores.
