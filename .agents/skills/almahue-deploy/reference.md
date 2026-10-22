# Comandos

Sync código (Windows, desde `ERP/`):

```powershell
tar -czf $env:TEMP\almahue-erp.tgz --exclude=erp_back/node_modules --exclude=erp_back/dist --exclude=erp_front/node_modules --exclude=erp_front/dist --exclude=.env erp_back erp_front docker-compose.prod.yml deploy scripts
scp -F .deploy/ssh_config $env:TEMP\almahue-erp.tgz erp-deploy:/tmp/
.\scripts\remote.ps1 -- bash -lc "cd /opt/almahue_erp && tar xzf /tmp/almahue-erp.tgz"
```

Health:

```powershell
.\scripts\remote.ps1 -- curl -sS http://127.0.0.1:4010/api/v1/health
```

Seed one-off (imagen node + volume `erp_back`): requiere `npx prisma generate` si el client no está generado.
