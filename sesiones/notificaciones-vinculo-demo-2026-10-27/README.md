# Demo notificaciones solicitud vínculo cuenta

API local reiniciada y front en `http://localhost:5174` (modo real).

## Credenciales usadas (holding QA local)

| Rol | Email | Clave |
|-----|-------|-------|
| Admin | `admin@almahue.local` | `Admin123!` |
| Compras (operador) | `erojas@almahuexport.cl` | `demo123` |

Empresa operativa: **ALMAHUE EXPORT SPA** (`EMP-EXPORT`).

## Capturas

| Archivo | Qué muestra |
|---------|-------------|
| `01-admin-notificaciones-lista.png` | Bandeja admin con avisos «Vínculo cuenta» |
| `02-admin-notificacion-detalle-aceptar-rechazar.png` | Detalle con Aceptar / Rechazar |
| `03-plan-cuentas-arbol-permisos.png` | Plan unificado: árbol + permisos a la derecha |
| `04-operador-mis-solicitudes.png` | **Mis solicitudes** (sidebar, sobre Cerrar sesión) |
| `05-operador-notificaciones-lista.png` | Operador: enviada + rechazada |
| `06-operador-notificacion-rechazo-detalle.png` | Detalle del rechazo con motivo |
| `07-topbar-menu-mis-solicitudes.png` | Menú usuario (topbar): Mis solicitudes sobre Cerrar sesión |

## Flujo reproducible

1. Operador: POST `solicitudes-vinculo-cuenta` (o desde OC «Solicitar al administrador»).
2. Admin: **Notificaciones** > Aceptar o Rechazar.
3. Operador: **Mis solicitudes** y **Notificaciones**.

## Fix aplicado en este turno

Las funciones de vínculo cuenta no estaban exportadas en `src/services/api.ts`; el detalle de notificación fallaba con `getSolicitudVinculoCuenta is not a function`. Corregido con `pickApi` + stubs en mock.
