---
name: almahue-pantallas-permisos
description: Catálogo de pantallas vs Sidebar y modulo:read/write; OV vs Cotizaciones. Use when editing pantallas-permisos, roles, or menu routes.
---

# Pantallas vs menú

## Catálogo vs Sidebar

Catálogo `pantallas-permisos` **alineado** con `Sidebar.tsx` (2026-08-14; revalidado ciclo C 18/08): OV, Aprobaciones y Guías bajo Ventas; Cotizaciones bajo Compras.

Al editar roles, menú o el catálogo:

- Alinear nombres con D11: Cotizaciones Compras → OC; OV Ventas → stock → factura.
- Permisos `modulo:read` / `modulo:write`. **Comercial sí** es módulo de reglas de aprobación (grupos OV).
- Redirect `/comercial/cotizaciones` no es el menú de Ventas.

## No

- No reintroducir cotización de cliente en Ventas.
- Wizard **Emitir** es la pantalla de alta FACTURA/NC/ND/GUIA; el **Libro ventas** no emite. No usarlo para cotiz/NP/OC.
- Productor no es maestro; no añadir pantalla de productor sin pedido.
- SMTP / cobranza R4-18 / DTE real: diferidos, no pantallas nuevas por omisión.
