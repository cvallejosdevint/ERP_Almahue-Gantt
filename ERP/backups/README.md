# Backups BD Almahue ERP

Snapshot previo a ensayo de demostración o QA que muta datos.

## Archivos

| Archivo | Uso |
|---|---|
| `almahue-erp-20260902-224451.dump` | Respaldo **completo** pre-QA sistema 02/09 (pg_dump `-Fc` de toda la BD `almahue`) |
| `almahue-erp-latest.dump` | Alias estable (siempre el último dump) |
| `dump-almahue-erp.ps1` | Crear un dump nuevo |
| `restore-almahue-erp.ps1` | Restaurar |

Dumps `.dump` / `.sql` están en `.gitignore`.

## Restaurar (vuelve la BD al momento del dump)

Desde `ERP/backups` en PowerShell. **Para el API** (Nest en watch). Luego:

```powershell
.\restore-almahue-erp.ps1
```

O un dump concreto:

```powershell
.\restore-almahue-erp.ps1 -DumpFile 'almahue-erp-20260902-224451.dump'
```

Reinicia o deja que Nest recargue. Health debe seguir `db=ok`.

`--clean` borra/recrea objetos de la BD destino. No apuntar a otra base.

## Nuevo dump

```powershell
.\dump-almahue-erp.ps1
```
