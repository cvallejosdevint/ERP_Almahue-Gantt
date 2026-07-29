# Construye imágenes Docker del ERP (api + web).
# Uso: .\scripts\build-images.ps1
# Vars opcionales: ERP_API_IMAGE, ERP_WEB_IMAGE, VITE_API_URL, VITE_APP_TITLE

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
  Write-Error "Docker no está en PATH. Instala Docker Desktop / engine y reintenta."
}

$ApiTag = if ($env:ERP_API_IMAGE) { $env:ERP_API_IMAGE } else { 'almahue-erp-api:local' }
$WebTag = if ($env:ERP_WEB_IMAGE) { $env:ERP_WEB_IMAGE } else { 'almahue-erp-web:local' }
$ViteApi = if ($env:VITE_API_URL) { $env:VITE_API_URL } else { '/api/v1' }
$ViteTitle = if ($env:VITE_APP_TITLE) { $env:VITE_APP_TITLE } else { 'Almahue ERP v1' }

Write-Host "==> Building $ApiTag"
docker build -t $ApiTag .\erp_back
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "==> Building $WebTag (VITE_API_URL=$ViteApi)"
docker build `
  --build-arg "VITE_API_URL=$ViteApi" `
  --build-arg "VITE_APP_TITLE=$ViteTitle" `
  -t $WebTag `
  .\erp_front
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "OK. Imágenes: $ApiTag , $WebTag"
