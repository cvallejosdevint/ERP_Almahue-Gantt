> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# Fix gaps permisos UI + retest

Fecha: 2026-07-31

## Cambios aplicados

### 1. Botones Aprobar/Rechazar OC
- Nuevo helper `canResolverOcPendiente` en `erp_front/src/lib/workflowAprobacion.ts`
- `AprobacionesOcPage` solo muestra Aprobar/Rechazar si el usuario es el jefe asignado, tiene `*` o `compras:aprobar-all`
- Legado sin `aprobadorId`: no muestra acciones de resolución

### 2. Rutas por módulo (`App.tsx`)
Antes un único `ProtectedRoute` con `anyOf` que incluía `contratistas:read` abría Compras/Contab/Tesorería/etc.

Ahora grupos separados:
- `admin:read` → `/admin/*`
- `catalogos:read` → parametrización
- `compras:read` → `/compras/*`
- `contratistas:read` → `/contratistas/*`
- `insumos:read` → insumos
- `contabilidad:read` → contabilidad/presupuestos
- `tesoreria:read` → tesorería
- `comercial:read` → ventas
- Proveedores: `catalogos:read` **o** `compras:read`

### 3. Sidebar por permisos
Cada bloque del menú declara `anyOf`; se ocultan módulos sin permiso (no solo Administración).

### 4. Escritura OC
Sin `compras:write`: se ocultan **Nueva OC**, **Editar** y **Anular**.

## Retest

| Capa | Estado |
|------|--------|
| Helper OC (asserts node) | PASS |
| API flujos OC/PF + RBAC | **Bloqueado**: Postgres `localhost:5433` caído (`health.db=error`, login 500). Docker no disponible en PATH. |
| UI roles | Pendiente de re-ejecutar al levantar la BD |

## Cómo revalidar (cuando la BD esté arriba)

```powershell
# BD en :5433, luego:
cd E:\source\repos\Almahue\ERP\erp_back; npm run start:dev
cd E:\source\repos\Almahue\ERP\erp_front; npx vite --port 5174 --host 127.0.0.1
```

Usuarios QA (`QaTest123!`):
- `qa.aprobador@almahue.local` → ve Aprobar en OC/proformas
- `qa.solicitante@almahue.local` → pide aprobación, sin Aprobar
- `qa.lectura@almahue.local` → sin Nueva OC / sin Aprobar / sin Admin
- `jsanchez@almahue.cl` / `demo123` → sin menú Compras; `/compras/ordenes` redirige a `/`
