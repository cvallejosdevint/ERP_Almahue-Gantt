# Abre un tunel SSH seguro hacia la base de datos PostgreSQL del servidor (almahue_erp_postgres).
# Puerto local expuesto: 5434
# Uso: .\scripts\tunnel-qa-db.ps1

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$ConfigFile = Join-Path $Root '.deploy\ssh_config'
$HostAlias = 'erp-deploy'
$LocalPort = 5434
$RemoteTarget = '172.20.0.3:5432'

if (-not (Test-Path -LiteralPath $ConfigFile)) {
  Write-Error "No existe $ConfigFile. Ejecuta primero: .\scripts\connect-ssh.ps1"
}

Write-Host "==> Abriendo tunel SSH hacia PostgreSQL QA..."
Write-Host "    Local:   localhost:$LocalPort"
Write-Host "    Remoto:  $RemoteTarget (almahue_erp_postgres)"
Write-Host "    BD:      erp_qa (schema: erp)"
Write-Host "    Presiona Ctrl+C para cerrar el tunel cuando termines."
Write-Host ""

& ssh -F $ConfigFile -N -L "${LocalPort}:${RemoteTarget}" $HostAlias
