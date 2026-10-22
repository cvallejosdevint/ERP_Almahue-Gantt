---
name: almahue-modulo
description: Orden obligatorio para crear o extender un módulo Nest/React del ERP Almahue. Use when adding a module, screen, Prisma model, API endpoint, or feature folder.
---

# Nuevo módulo ERP

## Backend (`ERP/erp_back`)

1. `prisma/schema.prisma` — modelo + `empresaId` + `@@schema("erp")`
2. `prisma/migrations/` — nunca solo `prisma/sql/`
3. Seed mínimo si hace falta demo
4. `src/modules/<mod>/*.module.ts`
5. `dto/*.dto.ts` — class-validator
6. `*.service.ts` — filtrar tenant
7. `*.controller.ts` — REST + `@ApiTags` + `@RequirePermissions`
8. Registrar en `app.module.ts`

## Frontend (`ERP/erp_front`)

1. `src/types/domain.ts`
2. `src/services/real/api.ts` — axios, API real
3. `src/lib/permissions.ts`
4. `src/features/<mod>/`
5. Ruta + `ProtectedRoute` en `App.tsx`
6. i18n `es.json` si aplica

Permisos: `modulo:read` / `modulo:write`. Listados: patrón DataTable existente.

Al añadir pantalla: actualizar el catálogo `pantallas-permisos` (alineado con Sidebar desde 14/08; no reintroducir desfase). No meter cotización en Ventas (D11: Cotizaciones = Compras; OV = Ventas).

Stock de insumos: siempre `empresaId` + `bodegaId` (`StockInsumoBodega`). No usar solo `Insumo.stock` global para ventas.
