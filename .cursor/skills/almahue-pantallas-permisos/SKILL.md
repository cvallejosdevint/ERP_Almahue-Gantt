---
name: almahue-pantallas-permisos
description: Catálogo de pantallas vs Sidebar y modulo:read/write; OC Compras vs OV Ventas. Use when editing pantallas-permisos, roles, or menu routes.
---

# Pantallas vs menú

## Catálogo vs Sidebar

Catálogo `pantallas-permisos` **alineado** con `Sidebar.tsx` (2026-08-21): OV y Guías bajo Ventas; Compras = OC, Aprobaciones, Recepciones, Libro. **Sin** Cotizaciones.

Al editar roles, menú o el catálogo:

- Alinear nombres con D11: compras arrancan en OC (cotiz = referencia); OV Ventas → stock → factura.
- Permisos `modulo:read` / `modulo:write`. Grupos/escalas de aprobación = **solo Compras**.
- Redirect `/comercial/cotizaciones` y `/compras/cotizaciones` → `/compras/ordenes` (bookmarks, no menú).

## No

- No reintroducir menú ni página de Cotizaciones.
- No reintroducir cotización de cliente en Ventas.
- Wizard **Emitir** es la pantalla de alta FACTURA/NC/ND/GUIA; el **Libro ventas** no emite. No usarlo para cotiz/NP/OC.
- Productor no es maestro; no añadir pantalla de productor sin pedido.
- SMTP / cobranza R4-18 / DTE real: diferidos, no pantallas nuevas por omisión.
