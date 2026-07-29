# ERP v1 Web — Almahue / Devint

Monorepo local con backend y frontend del ERP Enterprise (6 meses).

| Proyecto    | Stack                          | Puerto dev |
|-------------|--------------------------------|------------|
| `erp_back`  | NestJS 10, Prisma 7, PostgreSQL | 3001       |
| `erp_front` | Vite 6, React 19, Tailwind 4   | 5174       |

## Requisitos

- Node.js **20 LTS** (ver `.nvmrc` en cada proyecto)
- PostgreSQL 15+ (schema Prisma: `erp`)

## Inicio rápido (dev)

```bash
# Backend
cd erp_back
cp .env.example .env   # ajustar DATABASE_URL
npm install
npx prisma migrate dev --name init
npm run start:dev

# Frontend (otra terminal)
cd erp_front
cp .env.example .env
npm install
npm run dev
```

- API: http://localhost:3001/api/v1  
- Swagger: http://localhost:3001/api/docs  
- Front: http://localhost:5174  

## Docker (prep deploy)

Artefactos en esta carpeta: `Dockerfile` por proyecto, `docker-compose.yml` (API + web; Postgres opcional con `--profile db`), `.env.example` / `.env.production.example`, scripts en `scripts/`.

Guía breve: **[DEPLOY.md](./DEPLOY.md)**

```bash
cp .env.example .env
docker compose build
docker compose up -d
docker compose run --rm --no-deps api npx prisma migrate deploy
```

Por defecto **no** se levanta Postgres: apunta `DATABASE_URL` a una BD externa/compartida (`?schema=erp`).

## Git

Cada carpeta de app es un repositorio independiente (`erp_back`, `erp_front`). Los archivos de compose/docs en `ERP/` viven en el monorepo raíz Almahue.
