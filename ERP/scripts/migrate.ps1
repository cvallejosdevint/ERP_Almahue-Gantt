# Aplica migraciones Prisma contra DATABASE_URL del .env / entorno.
# Uso: .\scripts\migrate.ps1

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
  Write-Error "Docker no está en PATH."
}

if (-not $env:DATABASE_URL -and (Test-Path .\.env)) {
  Get-Content .\.env | ForEach-Object {
    if ($_ -match '^\s*#' -or $_ -match '^\s*$') { return }
    $pair = $_.Split('=', 2)
    if ($pair.Length -eq 2 -and -not [string]::IsNullOrWhiteSpace($pair[0])) {
      $name = $pair[0].Trim()
      $val = $pair[1].Trim()
      if (-not (Test-Path "Env:$name")) {
        Set-Item -Path "Env:$name" -Value $val
      }
    }
  }
}

if (-not $env:DATABASE_URL) {
  Write-Error "Define DATABASE_URL en el entorno o en .env"
}

Write-Host "==> prisma migrate deploy (schema erp)"
docker compose run --rm --no-deps `
  -e "DATABASE_URL=$env:DATABASE_URL" `
  api npx prisma migrate deploy
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "OK"
