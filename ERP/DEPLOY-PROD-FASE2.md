# Deploy producción — Fase 2 Aprobaciones

Guía para actualizar **`http://45.7.229.46/almahue-erp/`** desde el código local actual (AdminConcepto, grupos/escalas, simulador, fix API 403).

## Estado actual (2026-08-12)

| Aspecto | Prod (`/opt/almahue_erp`) | Local (repo) |
|---------|---------------------------|--------------|
| API grupos | `workflows-admin` (legacy) | `grupos-aprobacion`, `escalas-aprobacion`, … |
| `GET /grupos-aprobacion` | **404** | **200** |
| UI Reglas de aprobación | Lista legacy vacía | Árbol + Niveles + Simulador |
| `seed-aprobaciones-fase2.ts` | **No existe** | Sí |
| Fix JWT `adminConceptoModulos` | **No** | Sí |
| Usuarios QA (Claudia, Luis, …) | **No** (~10 usuarios seed UAT) | Sí (tras seed f2) |
| Contenedores | Up 11 días, healthy | — |
| SSH | `ERP/.deploy/ssh_config` → `erp-deploy` (45.7.229.46:2222) | Configurado |

**Conclusión:** hay que **subir código + rebuild + migraciones** antes de re-ejecutar QA en prod.

---

## Pre-requisitos

- [ ] Código local compila: `cd erp_back && npm run build`
- [ ] SSH operativo desde `ERP/`:

```powershell
.\scripts\remote.ps1 -- docker compose -f /opt/almahue_erp/docker-compose.prod.yml ps
```

- [ ] **No sobrescribir** `/opt/almahue_erp/.env` (secretos prod).
- [ ] Ventana de mantenimiento corta (~5–15 min rebuild).
- [ ] *(Opcional)* Backup BD:

```powershell
.\scripts\remote.ps1 -- docker exec almahue_erp_postgres pg_dump -U erp -d erp -n erp -Fc -f /tmp/erp-backup-pre-f2.dump
```

---

## 1. Sincronizar código al servidor

El host **no usa git** en `/opt/almahue_erp`; el deploy es copia de archivos + rebuild Docker.

### Opción A — tarball (recomendada, desde `ERP/` en Windows)

```powershell
cd E:\source\repos\Almahue\ERP

# Empaquetar sin secretos ni artefactos pesados
tar -czf $env:TEMP\almahue-erp-f2.tgz `
  --exclude=erp_back/node_modules `
  --exclude=erp_back/dist `
  --exclude=erp_front/node_modules `
  --exclude=erp_front/dist `
  --exclude=.env `
  --exclude=.qa-tmp `
  --exclude=qa-tmp `
  erp_back erp_front docker-compose.prod.yml deploy scripts `
  DEPLOY.md DEPLOY-PROD-FASE2.md .env.production.example

scp -F .deploy/ssh_config $env:TEMP\almahue-erp-f2.tgz erp-deploy:/tmp/

.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && tar xzf /tmp/almahue-erp-f2.tgz && rm /tmp/almahue-erp-f2.tgz"
```

### Opción B — rsync (WSL / Git Bash)

```bash
rsync -avz --delete \
  --exclude node_modules --exclude dist --exclude .env \
  -e "ssh -F ERP/.deploy/ssh_config" \
  ERP/erp_back ERP/erp_front ERP/docker-compose.prod.yml ERP/deploy ERP/scripts \
  erp-deploy:/opt/almahue_erp/
```

---

## 2. Verificar `.env` de producción

En el servidor, confirmar (no reemplazar el archivo entero):

```bash
grep -E '^(VITE_BASE_PATH|VITE_API_URL|FRONTEND_URL|CORS_ORIGINS|RUN_MIGRATE)=' /opt/almahue_erp/.env
```

Valores esperados para acceso por IP:

| Variable | Valor |
|----------|--------|
| `VITE_BASE_PATH` | `/almahue-erp/` |
| `VITE_API_URL` | `/almahue-erp/api/v1` |
| `FRONTEND_URL` | `http://45.7.229.46/almahue-erp` |
| `CORS_ORIGINS` | incluir `http://45.7.229.46` |
| `RUN_MIGRATE` | `true` (migrate al boot) |

Si faltan `VITE_*`, agregarlos al `.env` **antes** del rebuild de `web`.

---

## 3. Rebuild y reinicio

```powershell
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && docker compose -f docker-compose.prod.yml --env-file .env up -d --build"
```

Solo front (si solo cambió UI / `VITE_*`):

```powershell
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && docker compose -f docker-compose.prod.yml --env-file .env up -d --build --force-recreate web"
```

Esperar health:

```powershell
.\scripts\remote.ps1 -- curl -sS http://127.0.0.1:4010/api/v1/health
.\scripts\remote.ps1 -- curl -sS -o /dev/null -w "%{http_code}" http://127.0.0.1:4010/api/v1/grupos-aprobacion
```

- Health → JSON con `"status":"ok"`.
- `grupos-aprobacion` sin token → **401** (no 404). **404 = deploy viejo aún activo.**

Revisar migraciones en logs:

```powershell
.\scripts\remote.ps1 -- docker logs almahue_erp_api --tail 40
```

Buscar: `prisma migrate deploy` sin errores.

---

## 4. Datos demo / seed fase 2

El seed **`npm run seed:aprobaciones-f2`**:

- Hace **upsert** de usuarios U-7…U-58 (password demo `demo123`).
- **Borra y recrea** grupos, escalas, nodos y AdminConcepto de la empresa (`EMP-1`).
- Asigna PIN `4821` al pool de aprobadores.
- Amplía permisos de `ROL-2` con `compras:write`.

**⚠️ En prod con datos reales:** no ejecutar el seed completo sin acuerdo. Alternativas:

1. **Solo QA/demo:** ejecutar seed en ventana controlada.
2. **Prod mixto:** configurar manualmente vía UI Admin (export/import JSON desde local).
3. **Solo AdminConcepto:** asignar en Admin → Administradores de concepto (requiere usuarios existentes).

### Ejecutar seed (entorno demo / UAT)

```powershell
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && docker compose -f docker-compose.prod.yml --env-file .env run --rm --no-deps api npx ts-node -r tsconfig-paths/register prisma/seed-aprobaciones-fase2.ts"
```

Si `ts-node` no está en imagen prod, usar contenedor one-off con dev deps o ejecutar contra `DATABASE_URL` desde máquina local apuntando al túnel SSH (solo en lab).

---

## 5. Smoke test post-deploy

| # | Comando / acción | Esperado |
|---|------------------|----------|
| 1 | `curl http://45.7.229.46/almahue-erp/api/v1/health` | 200 OK |
| 2 | Login `admin@almahue.local` / `Admin123!` | Dashboard OK |
| 3 | `/admin/aprobaciones` como admin | UI nueva (Árbol, Simulador, Import/Export) |
| 4 | Simulador S1: Luis 200k GRP-COMPRAS-1 | Cadena → Jorge (suplencia) |
| 5 | Login Claudia `cvargas@almahue.cl` / `demo123` *(tras seed)* | Solo menú Reglas de aprobación |
| 6 | Claudia → GET grupos (DevTools Network) | 200, 12 grupos Compras, 0 Contratistas |
| 7 | Ricardo `rmunoz@almahue.cl` | 8 grupos Contratistas |
| 8 | Claudia → `/admin/usuarios` | Bloqueado |
| 9 | Freshlink `http://45.7.229.46/` | Sin regresión |

**Importante:** usuarios AdminConcepto deben **cerrar sesión y volver a entrar** para JWT con `adminConceptoModulos`.

---

## 6. Checklist QA front (re-test completo)

### A. Admin — Simulador

| ID | Solicitante | Monto | Grupo | Resultado esperado |
|----|-------------|-------|-------|-------------------|
| S1 | Luis Herrera | 200.000 | GRP-COMPRAS-1 | Jorge Sánchez (suplente María) |
| S2 | Diego | 500.000 | GRP-COMPRAS-2 | Pablo Núñez |
| S3 | María | 100.000 | GRP-COMPRAS-1 | Jorge (sin auto-aprobación jefa) |
| S4 | Bruno | 800.000 | GRP-COMPRAS-6 (AND) | Laura Soto + co-aprobador |
| S5 | Luis | 3.000.000 | GRP-COMPRAS-1 | Jorge → Claudia (escala) |
| S6 | Diego | 400.000 | Contratistas | Pablo Núñez |

### B. AdminConcepto

| Usuario | Módulo | Verificar |
|---------|--------|-----------|
| Claudia (Compras) | Compras | Árbol 12 grupos; combo solo Compras; mutaciones OK |
| Ricardo (Contratistas) | Contratistas | 8 grupos; sin acceso Compras |
| Ambos | — | Sin `/admin/usuarios`; re-login tras deploy |

### C. Flujo operativo OC

Bandeja runtime: Jorge (U-3) ve pendientes **sin** `compras:read` global (`bandejaModulos`). Cubierto en local por OC2/OC3 del plan con seed.

| Paso | Actor | Esperado | Nota |
|------|-------|----------|------|
| Crear OC | Luis | Guardar y enviar a aprobación | Validar formulario Nº OC |
| Bandeja | Jorge | Ver pendiente en `/compras/aprobaciones` | Re-login si se cambiaron reglas |
| Aprobar PIN | Jorge / cadena | OC avanza | PIN demo `4821` |
| Bandeja | María | Pendientes según reglas | — |

### D. Regresión prod existente

- [ ] Login usuarios actuales (mgonzalez, jsanchez, …)
- [ ] Módulos que ya usaban (contratistas, compras lectura)
- [ ] Notificaciones dashboard
- [ ] HTTPS `https://45.7.229.46/almahue-erp/` (si aplica)

---

## 7. Rollback rápido

Si el deploy falla:

```powershell
# Restaurar tarball anterior (si se guardó backup en /opt)
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && docker compose -f docker-compose.prod.yml --env-file .env up -d --build"

# Restaurar BD (si se hizo dump)
.\scripts\remote.ps1 -- docker exec almahue_erp_postgres pg_restore -U erp -d erp --clean --if-exists /tmp/erp-backup-pre-f2.dump
```

Imágenes Docker previas: `docker images | grep almahue-erp` en el host.

---

## Referencias

- Operación diaria: `/opt/almahue_erp/SERVER.md`
- Nginx subpath: `deploy/nginx-almahue-erp-path.conf`
- Plantilla env: `.env.production.example`
- Seed: `erp_back/prisma/seed-aprobaciones-fase2.ts` → `npm run seed:aprobaciones-f2`
- SSH local: `.\scripts\connect-ssh.ps1` → `.\scripts\remote.ps1 -- <cmd>`
