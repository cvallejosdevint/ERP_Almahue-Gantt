> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: minuta Reu6 (D19) + código auth. Motivo: carpeta de guion D11 invertido; SSO sigue SKIP sin `.env`.

# SSO Microsoft Entra ID — plan local / pruebas (URL publicada)

**Objetivo:** dos vías de login en paralelo — **email+clave ERP** y **botón Microsoft** — sin reemplazar la clave local.  
**Ambiente de prueba publicado (IP):** `http://45.7.229.46/almahue-erp/`

## Arquitectura

```
[Login UI]
  ├─ Email + clave  → POST /auth/login          → JWT ERP (igual que hoy)
  └─ Botón Microsoft → MSAL (popup) → id_token
                         → POST /auth/microsoft → valida Entra JWKS
                         → vincula Usuario por email/UPN
                         → emite el mismo JWT ERP
```

Tras autenticar, el resto del ERP no cambia (RBAC, empresa, PIN, etc.).

## Redirect URI a registrar en Entra (importante)

En **App registration › Authentication › SPA** agregar:

| Ambiente | Redirect URI (exacto) |
|---|---|
| **Publicado (IP)** | `http://45.7.229.46/almahue-erp/login` |
| Dev local (opcional) | `http://127.0.0.1:5174/login` |
| Dev local (opcional) | `http://localhost:5174/login` |

Microsoft exige coincidencia **exacta** (path `/almahue-erp/login` incluido).

## Prerrequisitos (IT / desarrollador)

1. Cuenta Azure (gratis) o tenant Almahue.
2. Registrar app en **Microsoft Entra ID › App registrations**:
   - Tipo: **Single-page application (SPA)**
   - Redirect URI: el de la tabla arriba (empezar por la IP publicada)
   - API permissions: `openid`, `profile`, `email`
3. Copiar **Application (client) ID** y **Directory (tenant) ID**.
4. En el ERP (servidor), usuario de prueba con el **mismo email** que la cuenta Microsoft.

## Variables en el servidor publicado

En el `.env` del host / stack prod (`FRONTEND_URL` ya apunta a la IP):

```
MICROSOFT_AUTH_ENABLED=true
MICROSOFT_TENANT_ID=<directory-id>
MICROSOFT_CLIENT_ID=<application-id>
FRONTEND_URL=http://45.7.229.46/almahue-erp
CORS_ORIGINS=http://45.7.229.46,http://45.7.229.46/almahue-erp
```

Reiniciar API tras cambiar env. El front ya calcula el redirect con `VITE_BASE_PATH=/almahue-erp/`.

## Texto para pedir a IT del cliente

> Necesitamos una App Registration SPA en Entra ID del tenant Almahue para SSO del ERP.
>
> Redirect URI de pruebas: `http://45.7.229.46/almahue-erp/login`
>
> Por favor enviar:
> - Directory (tenant) ID
> - Application (client) ID
>
> No se requiere Client Secret (flujo SPA + PKCE).

## Endpoints

| Método | Ruta | Auth | Descripción |
|---|---|---|---|
| GET | `/auth/microsoft/config` | Public | `{ enabled, tenantId, clientId }` |
| POST | `/auth/microsoft` | Public | Body `{ idToken }` → sesión ERP |

## Mientras esperamos IDs de Almahue

Dejar `MICROSOFT_AUTH_ENABLED=false` (sin Tenant/Client). El login muestra el botón **Iniciar con Microsoft** **deshabilitado** y el aviso de pendiente; el login con clave sigue activo.

## Criterios de aceptación

1. Login local sigue OK en `http://45.7.229.46/almahue-erp/login`
2. Con `ENABLED=false`: botón Microsoft visible pero deshabilitado
3. Con env habilitado + IDs: botón activo → popup → entra al ERP
4. Usuario inexistente / inactivo → error claro

## Fuera de alcance (esta iteración)

- Forzar SSO / desactivar clave local
- JIT crear usuarios
- Dominio DNS (cuando exista, se agrega otro Redirect URI https)
