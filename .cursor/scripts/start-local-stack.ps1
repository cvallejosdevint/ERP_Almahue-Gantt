# Arranque local Almahue: ERP API :3001, front :5174, billing-gateway :3040.
# Idempotente: si el puerto ya escucha, no lanza otro proceso.
$ErrorActionPreference = 'Continue'

$AlmahueRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$BillingRoot = Join-Path (Split-Path $AlmahueRoot -Parent) 'billing-gateway'

function Test-Listening([int]$Port) {
  try {
    $client = New-Object System.Net.Sockets.TcpClient
    $client.Connect('127.0.0.1', $Port)
    $client.Close()
    return $true
  } catch {
    return $false
  }
}

function Get-NpmCmd {
  $cmd = Get-Command npm.cmd -ErrorAction SilentlyContinue
  if ($cmd) { return $cmd.Source }
  $fallback = Join-Path $env:ProgramFiles 'nodejs\npm.cmd'
  if (Test-Path $fallback) { return $fallback }
  return $null
}

function Start-NpmDev {
  param(
    [string]$Dir,
    [string]$NpmScript,
    [int]$Port,
    [string]$Title
  )
  if (-not (Test-Path (Join-Path $Dir 'package.json'))) {
    Write-Host "[skip] $Title : no hay package.json en $Dir"
    return
  }
  if (-not (Test-Path (Join-Path $Dir 'node_modules'))) {
    Write-Host "[skip] $Title : falta node_modules (npm install en $Dir)"
    return
  }
  if (Test-Listening $Port) {
    Write-Host "[ok] $Title ya escucha en :$Port"
    return
  }
  $npm = Get-NpmCmd
  if (-not $npm) {
    Write-Host "[skip] $Title : npm.cmd no está en PATH"
    return
  }
  Write-Host "[start] $Title -> $Dir (npm run $NpmScript) :$Port"
  Start-Process -FilePath $npm -ArgumentList @('run', $NpmScript) -WorkingDirectory $Dir -WindowStyle Minimized
}

if (Test-Listening 5433) {
  Write-Host '[ok] Postgres :5433'
} else {
  $svc = Get-Service -ErrorAction SilentlyContinue | Where-Object { $_.Name -like 'postgresql*' } | Select-Object -First 1
  if ($svc -and $svc.Status -ne 'Running') {
    try {
      Start-Service -Name $svc.Name
      Write-Host "[start] servicio $($svc.Name)"
    } catch {
      Write-Host "[aviso] Postgres no escucha en :5433 y no se pudo iniciar $($svc.Name)"
    }
  } else {
    Write-Host '[aviso] Postgres no escucha en :5433; el API fallará hasta levantarlo'
  }
}

Start-NpmDev -Dir (Join-Path $AlmahueRoot 'ERP\erp_back') -NpmScript 'start:dev' -Port 3001 -Title 'ERP API'
Start-NpmDev -Dir (Join-Path $AlmahueRoot 'ERP\erp_front') -NpmScript 'dev' -Port 5174 -Title 'ERP Front'

if (Test-Path (Join-Path $BillingRoot 'package.json')) {
  Start-NpmDev -Dir $BillingRoot -NpmScript 'start:dev' -Port 3040 -Title 'billing-gateway'
} else {
  Write-Host "[skip] billing-gateway no encontrado en $BillingRoot"
}
