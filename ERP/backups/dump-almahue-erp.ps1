# Dump completo de la BD local Almahue ERP (pg_dump -Fc).
# Uso: .\dump-almahue-erp.ps1
param(
  [string]$EnvFile = (Join-Path $PSScriptRoot '..\erp_back\.env')
)
$ErrorActionPreference = 'Stop'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$dumpName = "almahue-erp-$stamp.dump"
$dumpPath = Join-Path $PSScriptRoot $dumpName
$latestPath = Join-Path $PSScriptRoot 'almahue-erp-latest.dump'
$envLine = Get-Content $EnvFile | Where-Object { $_ -match '^DATABASE_URL=' } | Select-Object -First 1
if (-not $envLine) { throw 'DATABASE_URL no encontrado en .env' }
$url = $envLine.Substring(13).Trim().Trim('"').Trim("'")
if ($url -notmatch 'postgresql://([^:]+):([^@]+)@([^:/]+):(\d+)/([^?]+)') { throw 'No se pudo parsear DATABASE_URL' }
$dbUser = $Matches[1]; $dbPass = $Matches[2]; $dbHost = $Matches[3]; $dbPort = $Matches[4]; $dbName = $Matches[5]
$env:PGPASSWORD = $dbPass
$pgDump = 'C:\Program Files\PostgreSQL\18\bin\pg_dump.exe'
if (-not (Test-Path $pgDump)) {
  $alt = Get-ChildItem 'C:\Program Files\PostgreSQL\*\bin\pg_dump.exe' | Select-Object -First 1
  if (-not $alt) { throw 'pg_dump no encontrado' }
  $pgDump = $alt.FullName
}
Write-Host "Dump ${dbHost}:${dbPort}/${dbName} -> $dumpName (completo, sin owner/acl) ..."
& $pgDump -h $dbHost -p $dbPort -U $dbUser -d $dbName -Fc --no-owner --no-acl -f $dumpPath
if ($LASTEXITCODE -ne 0) { throw "pg_dump exit $LASTEXITCODE" }
Copy-Item $dumpPath $latestPath -Force
$size = (Get-Item $dumpPath).Length
Write-Host "Listo. $dumpName ($([math]::Round($size/1MB, 2)) MiB). Alias: almahue-erp-latest.dump"
Write-Host "Restaurar: .\restore-almahue-erp.ps1"
