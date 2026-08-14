# Despliegue ERP Almahue (Docker)

Preparación para un host compartido (p. ej. Bluehosting) con **Docker**.  
La alineación de red/puertos/BD con stacks ya existentes en el servidor es **fase 2** (no documentada aquí con credenciales ni acceso al host).

## Requisitos

- Docker Engine + Compose v2
- Node 20 solo si construyes fuera de Docker
- PostgreSQL 15+ **externo o compartido** (recomendado). Schema Prisma: **`erp`**
- Variables en `ERP/.env` (partir de `.env.example` o `.env.production.example`)

## Arquitectura de ejemplo

| Servicio | Imagen | Rol |
|----------|--------|-----|
| `api` | `erp_back/Dockerfile` | NestJS + Prisma (`PORT` interno 3001) |
| `web` | `erp_front/Dockerfile` | Estáticos Vite servidos con nginx; proxy `/api` → `api:3001` |
| `db` | Postgres 16 (profile `db`) | **Opcional**, solo laboratorio local |

Por defecto el compose **no** levanta Postgres: `DATABASE_URL` debe apuntar a un servidor existente.

## Variables obligatorias

| Variable | Dónde | Notas |
|----------|--------|--------|
| `DATABASE_URL` | api | Incluir `?schema=erp`. Ej: `postgresql://user:pass@host:5432/dbname?schema=erp` |
| `JWT_SECRET` | api | Secreto largo; no usar el valor de ejemplo |
| `FRONTEND_URL` | api | Origen exacto del front (CORS) |
| `VITE_API_URL` | build web | Bake en el bundle. Preferir `/api/v1` (mismo origen + nginx) o URL pública absoluta |

Opcionales útiles: `CORS_ORIGINS` (lista CSV), `JWT_EXPIRES_IN`, `RUN_MIGRATE`, nombres de contenedor/red/puertos (`ERP_*`).

## Build de imágenes

Desde `ERP/`:

```bash
cp .env.example .env   # ajustar
docker compose build
# o
./scripts/build-images.sh
# Windows: .\scripts\build-images.ps1
```

Front: si cambias `VITE_API_URL` / `VITE_APP_TITLE`, **rebuild** de `web` (son build-time).

## Arranque

```bash
# Solo api + web (BD externa)
docker compose up -d

# Laboratorio con Postgres local
docker compose --profile db up -d
# Con profile db, DATABASE_URL típico:
# postgresql://almahue:almahue@db:5432/almahue?schema=erp
```

Puertos host por defecto: API `3001`, web `8080` (configurables).

## Migraciones Prisma

Estrategia recomendada en BD compartida: **one-shot explícito**, no auto al boot.

1. Asegurar schema en Postgres (una vez):

```sql
CREATE SCHEMA IF NOT EXISTS erp;
```

2. Aplicar migraciones:

```bash
docker compose run --rm --no-deps api npx prisma migrate deploy
# o ./scripts/migrate.sh  |  .\scripts\migrate.ps1
```

Alternativa: `RUN_MIGRATE=true` en el entorno del contenedor `api` (entrypoint). Evitar en prod compartida salvo que controles el arranque.

`prisma generate` ocurre en el **build** de la imagen. En runtime solo hace falta `migrate deploy` + `node dist/main.js`.

## Front ↔ API (reverse proxy)

- **Compose / mismo origen:** `VITE_API_URL=/api/v1` y nginx del contenedor `web` proxya `/api/` al servicio `api`.
- **Proxy del host (fase Bluehost):** exponer `web` (y/o `api`) detrás de nginx/Apache del servidor; alinear `FRONTEND_URL` y, si aplica, `VITE_API_URL` absoluta.

## Red compartida (fase 2)

Si el host ya tiene una red Docker con otras apps:

```bash
export ERP_NETWORK_NAME=nombre-red-existente
docker compose -f docker-compose.yml -f docker-compose.shared-net.example.yml up -d
```

Ajustar `ERP_*_CONTAINER` y puertos host para no colisionar. Detalle de credenciales BD / proxy del servidor: fuera de alcance de este documento.

## Conexión SSH al server

Para que un agente (o tú) ejecute comandos remotos **sin guardar passwords** en el repo:

1. Desde `ERP/` (Windows): `.\scripts\connect-ssh.ps1`
2. Ingresa host, puerto (default 22), usuario y, si aplica, ruta a la clave privada.
3. Eso escribe solo en `ERP/.deploy/` (gitignored): `ssh.env` + `ssh_config` con el alias `erp-deploy`.

Comandos reutilizables:

```powershell
ssh -F .deploy/ssh_config erp-deploy "uname -a"
.\scripts\remote.ps1 -- uname -a
```

**Auth:** preferir clave SSH (`ssh-keygen` + pubkey en `authorized_keys`). Si solo tienes password, autentícate una vez en una terminal interactiva fuera del agente; el agente no puede ingresar el password de forma fiable. Nunca guardes contraseñas en archivos del repo.

## Producción independiente (vendora-prod)

Stack propio en `/opt/almahue_erp` (no reutiliza `almahue_postgres` / `vendora_postgres`):

```bash
cd /opt/almahue_erp
docker compose -f docker-compose.prod.yml --env-file .env up -d --build
```

| Recurso | Valor |
|---------|--------|
| Contenedores | `almahue_erp_api`, `almahue_erp_web`, `almahue_erp_postgres` |
| Red / volumen | `almahue_erp_net` / `almahue_erp_pgdata` |
| Host bind | API `127.0.0.1:4010`, Web `127.0.0.1:4011` (PG sin publicar) |
| **URL por IP (sin DNS)** | **`http://45.7.229.46/almahue-erp/`** |
| Nginx IP | `almahue-ip` → locations `/almahue-erp/` (web 4011) y `/almahue-erp/api/` (api 4010); fragmento en `deploy/nginx-almahue-erp-path.conf` |
| Front subpath | `VITE_BASE_PATH=/almahue-erp/`, `VITE_API_URL=/almahue-erp/api/v1` (rebuild web) |
| Dominio propuesto | `https://almahue-erp.vndev.cl` (opcional; DNS pendiente) |
| TLS | Solo cuando haya DNS: `sudo certbot --nginx -d almahue-erp.vndev.cl` |

Secretos (`JWT_SECRET`, `POSTGRES_PASSWORD`, `DATABASE_URL`) se generan en el `.env` del server. Detalle operativo: `/opt/almahue_erp/SERVER.md`.

### Acceso por path en la IP

Freshlink/Almahue sigue en `http://45.7.229.46/`. El ERP vive en **`/almahue-erp/`** (mismo `default_server`, sin DNS).

1. Build web con subpath (`VITE_BASE_PATH` + `VITE_API_URL` en `.env`).
2. Nginx host: strip del prefijo al proxyar al contenedor web (`proxy_pass …4011/`) y API directa a `4010`.
3. CORS: incluir origen `http://45.7.229.46` (el path no forma parte del Origin).
4. Health: `http://45.7.229.46/almahue-erp/api/v1/health`

## Deploy fase 2 (aprobaciones / AdminConcepto) en prod

Checklist detallado para actualizar `http://45.7.229.46/almahue-erp/` desde el código actual: **[DEPLOY-PROD-FASE2.md](./DEPLOY-PROD-FASE2.md)** (sync, rebuild, migraciones, seed opcional, QA re-test).

## Checklist rápido

1. `.env` sin secretos de ejemplo
2. `DATABASE_URL` con `?schema=erp` y schema creado
3. `docker compose build && docker compose up -d`
4. `prisma migrate deploy` (incluye OV/stock, aprobación comercial y `20260815200000_huerfanos_ficha_inventario` si aplica)
5. Abrir `http://localhost:8080` (o URL pública) y verificar login / API
6. Prod (`45.7.229.46`): seguir **[DEPLOY-PROD-FASE2.md](./DEPLOY-PROD-FASE2.md)** — no asumir migrate hasta deploy explícito
