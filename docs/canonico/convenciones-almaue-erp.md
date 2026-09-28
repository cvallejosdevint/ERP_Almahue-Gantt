# Convenciones Almahue → Patrón ERP

Análisis de `almahue_back` y `almahue_front` como referencia arquitectónica para el ERP (dominio distinto).

## Stack confirmado

| Capa | Tecnología |
|---|---|
| Backend | NestJS 10, TypeScript 5, Prisma 7.8, PostgreSQL 16, JWT + RBAC |
| Frontend | React 19, Vite 8, TanStack Query 5, react-router 7, Tailwind v4 |
| Infra | Docker Compose, Swagger `/api/docs`, nginx en prod |

## Patrón backend por módulo

Orden obligatorio (cadena que bloquea al frontend):

```
1. prisma/schema.prisma     → modelos + relaciones + empresaId (tenant)
2. prisma/migrations/       → migración versionada
3. prisma/seeds/            → datos demo mínimos
4. src/modules/<mod>/*.module.ts
5. dto/*.dto.ts             → class-validator
6. *.service.ts             → lógica + filtro tenant
7. *.controller.ts          → REST + @ApiTags + @RequirePermissions
8. app.module.ts            → registro del módulo
```

Referencia: [`almahue_back/src/app.module.ts`](../../almahue_back/src/app.module.ts) — guards globales `JwtAuthGuard` + `PermissionsGuard`.

### Auth y tenant (Core ERP)

| Artefacto Almahue | Equivalente ERP |
|---|---|
| `Exportadora` | `Empresa` |
| `exportadoraId` | `empresaId` |
| `src/auth/tenant.util.ts` | Mismo patrón multi-tenant |
| `@Public()`, `@RequirePermissions()` | Igual |
| Refresh token rotativo | Igual |

## Patrón frontend por módulo

Orden obligatorio:

```
1. src/types/domain.ts           → interfaces TypeScript
2. src/services/real/api.ts      → funciones axios por endpoint
3. src/lib/permissions.ts        → permisos read/write del módulo
4. src/features/<mod>/           → pages, components, hooks
5. src/App.tsx                   → ruta + ProtectedRoute
6. src/i18n/locales/es.json      → claves i18n
```

Referencia: [`almahue_front/src/lib/permissions.ts`](../../almahue_front/src/lib/permissions.ts).

### Capa HTTP

- [`http.ts`](../../almahue_front/src/services/http.ts): axios, Bearer JWT, refresh en 401.
- [`api.ts`](../../almahue_front/src/services/api.ts): fachada; en ERP usar **siempre API real** (sin mock en prod).

## Permisos RBAC por módulo ERP

| Módulo | Permisos |
|---|---|
| core/admin | `admin:read`, `admin:write` |
| contabilidad | `contabilidad:read`, `contabilidad:write` |
| inventario | `inventario:read`, `inventario:write` |
| compras | `compras:read`, `compras:write` |
| ventas | `ventas:read`, `ventas:write` |
| produccion | `produccion:read`, `produccion:write` |
| rrhh | `rrhh:read`, `rrhh:write` |
| integraciones | `integraciones:read`, `integraciones:write` |
| reportes | `reportes:read` |

## Componentes compartidos reutilizables

| Componente Almahue | Uso ERP |
|---|---|
| `DataTable` + `@tanstack/react-table` | Todos los listados |
| `PageHeader`, `KPI`, `Modal` | Layout estándar |
| `features/catalog/` hooks cascada | Catálogos jerárquicos (plan cuentas, BOM) |
| `lib/exportExcel.ts` + `xlsx` | Reportes y exportaciones |
| `react-hook-form` + `zod` | Formularios complejos (asientos, OC, pedidos) |
| `recharts` | Dashboard y reportes |

## Regla Back → Front

```
BACK (schema + endpoints + permisos + seeds)
  └─► FRONT (types + api client + UI)
```

El frontend de un módulo **no inicia** hasta que existan:
1. Endpoints documentados en Swagger
2. Permisos registrados en seeds
3. Al menos 1 registro seed para pruebas

## Integraciones (patrón EMC Almahue)

Módulo `integrations/` con:
- `@nestjs/schedule` para jobs
- Logs de sync + reintentos
- UI admin en `/admin/integraciones`

Aplicable a SII/DTE y conciliación bancaria en ERP.

## Supuestos declarados

- ERP usa misma estructura de repos separados (`erp_back`, `erp_front`), no monorepo.
- Sin mobile v1.
- Contabilización automática centralizada en `ContabilizacionService` (nuevo, no existe en Almahue).
