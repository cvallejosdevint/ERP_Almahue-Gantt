# Restaurar backup Almahue ERP
# Uso: .\restore-almahue-erp.ps1
#      .\restore-almahue-erp.ps1 -DumpFile 'almahue-erp-20260730-144430.dump'
param(
  [string]$DumpFile = 'almahue-erp-latest.dump',
  [string]$EnvFile = (Join-Path $PSScriptRoot '..\erp_back\.env')
)
$ErrorActionPreference = 'Stop'
$dumpPath = if ([IO.Path]::IsPathRooted($DumpFile)) { $DumpFile } else { Join-Path $PSScriptRoot $DumpFile }
if (-not (Test-Path $dumpPath)) { throw "No existe $dumpPath" }
$envLine = Get-Content $EnvFile | Where-Object { $_ -match '^DATABASE_URL=' } | Select-Object -First 1
if (-not $envLine) { throw 'DATABASE_URL no encontrado en .env' }
$url = $envLine.Substring(13).Trim().Trim('"').Trim("'")
if ($url -notmatch 'postgresql://([^:]+):([^@]+)@([^:/]+):(\d+)/([^?]+)') { throw 'No se pudo parsear DATABASE_URL' }
$dbUser = $Matches[1]; $dbPass = $Matches[2]; $dbHost = $Matches[3]; $dbPort = $Matches[4]; $dbName = $Matches[5]
$env:PGPASSWORD = $dbPass
$pgRestore = 'C:\Program Files\PostgreSQL\18\bin\pg_restore.exe'
if (-not (Test-Path $pgRestore)) {
  $alt = Get-ChildItem 'C:\Program Files\PostgreSQL\*\bin\pg_restore.exe' | Select-Object -First 1
  if (-not $alt) { throw 'pg_restore no encontrado' }
  $pgRestore = $alt.FullName
}
Write-Host "Restaurando $dumpPath -> ${dbHost}:${dbPort}/${dbName} ..."
& $pgRestore -h $dbHost -p $dbPort -U $dbUser -d $dbName --clean --if-exists --no-owner --no-acl $dumpPath
Write-Host 'Listo. Reinicia erp_back si estaba corriendo.'
