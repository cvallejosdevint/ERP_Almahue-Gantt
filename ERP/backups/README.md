# Backups BD Almahue ERP

Snapshot previo a ensayo de demostración.

## Archivos

| Archivo | Uso |
|---|---|
| `almahue-erp-20260730-144430.dump` | Backup de esta corrida (formato custom `pg_dump -Fc`) |
| `almahue-erp-latest.dump` | Alias estable (siempre el último) |
| `almahue-erp-20260730-144430.sql` | SQL del schema `erp` (inspección / fallback) |
| `restore-almahue-erp.ps1` | Script de restauración |

## Restaurar en cualquier momento

Desde `ERP/backups` en PowerShell:

```powershell
.\restore-almahue-erp.ps1
```

O un dump concreto:

```powershell
.\restore-almahue-erp.ps1 -DumpFile 'almahue-erp-20260730-144430.dump'
```

Luego reinicia el API si hace falta:

```powershell
cd ..\erp_back
npm run start:dev
```

## Manual

```powershell
$env:PGPASSWORD = '<password del .env>'
& 'C:\Program Files\PostgreSQL\18\bin\pg_restore.exe' `
  -h localhost -p 5433 -U almahue -d almahue `
  --clean --if-exists --no-owner --no-acl `
  .\almahue-erp-latest.dump
```

**Nota:** `--clean` borra/recrea objetos de la BD destino. No ejecutar contra otra base por error.
