---
name: almahue-deploy
description: Deploy, seed y SSH del ERP Almahue a producción (45.7.229.46). Use when deploying, rebuilding Docker, prisma migrate, seeding prod/local, or using remote.ps1 / connect-ssh.
---

# Deploy ERP Almahue

## Host

- Dir: `/opt/almahue_erp`
- Compose: `docker-compose.prod.yml` + `.env` (**nunca sobrescribir `.env`**)
- URL: `http://45.7.229.46/almahue-erp/`
- SSH: `ERP/.deploy/ssh_config` alias `erp-deploy` · `ERP/scripts/remote.ps1`

```powershell
cd ERP
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && docker compose -f docker-compose.prod.yml --env-file .env up -d --build"
```

Bake front: `VITE_BASE_PATH=/almahue-erp/`, `VITE_API_URL=/almahue-erp/api/v1`. Rebuild `web` si cambian.

## Migraciones

Solo `prisma/migrations/`. `RUN_MIGRATE=true` al boot. No dejar DDL en `prisma/sql/`. En prod verificar, antes de demo de ventas/aprobaciones: `20260813230000_stock_ov_ficha` y `20260818180000_comercial_aprobacion_piloto_on` (H14: no asumir).

Smoke post-deploy: checklist en `ERP/DEPLOY-PROD-FASE2.md` §5–6. Mínimo: health 200; `GET /grupos-aprobacion` sin token → **401** (404 = imagen vieja); AdminConcepto re-login.

## Seed

`npm run seed` + `seed:aprobaciones-f2` **destruye** config de aprobaciones EMP-1. No en prod con datos reales sin acuerdo.

## Build front

`npx tsc -b` pasa en local. El Dockerfile web sigue con `npx vite build` (bake más corto); no implica deuda de tipos.

## Additional resources

- Comandos y checklist: [reference.md](reference.md)
- `ERP/DEPLOY.md`, `ERP/DEPLOY-PROD-FASE2.md`
