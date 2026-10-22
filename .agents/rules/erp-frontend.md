---
description: Orden front — types, API real, permissions, feature, ruta
globs: ERP/erp_front/**/*.{ts,tsx}
alwaysApply: false
---

# Frontend ERP

Orden: `types/domain.ts` → `services/real/api.ts` → `lib/permissions.ts` → `features/<mod>/` → `ProtectedRoute`.

API **real** (no mock en flujos de producto). Sesión: `localStorage['erp.session']`.

- Menú vs `pantallas-permisos`: Cotizaciones solo Compras; OV y Guías en Ventas. Catálogo alineado 14/08; no reintroducir Cotizaciones en Ventas.
- Wizard **Emitir**: FACTURA/NC/ND/GUIA. Borradores DTE ahí, no en Libro ventas. No usarlo para cotización/NP/OC.
