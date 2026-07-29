# Ejecuta un comando remoto usando la config de connect-ssh.ps1.
# Uso: .\scripts\remote.ps1 -- uname -a
#      .\scripts\remote.ps1 -- docker ps -a

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$ConfigFile = Join-Path $Root '.deploy\ssh_config'
$HostAlias = 'erp-deploy'

if (-not (Test-Path -LiteralPath $ConfigFile)) {
  Write-Error "No existe $ConfigFile. Ejecuta primero: .\scripts\connect-ssh.ps1"
}

# Separador opcional "--" (estilo: remote.ps1 -- cmd args...)
$argv = @($args)
if ($argv.Count -gt 0 -and $argv[0] -eq '--') {
  $argv = $argv[1..($argv.Count - 1)]
}

if ($argv.Count -eq 0) {
  Write-Host "Uso: .\scripts\remote.ps1 -- <comando remoto>"
  Write-Host "Ej:  .\scripts\remote.ps1 -- uname -a"
  exit 1
}

# Unir args en un solo remote command string (como shell remoto)
$remoteCmd = ($argv | ForEach-Object {
  if ($_ -match '[\s"''`$]') {
    "'" + ($_ -replace "'", "'\''") + "'"
  } else {
    $_
  }
}) -join ' '

if (-not (Get-Command ssh -ErrorAction SilentlyContinue)) {
  Write-Error "ssh no está en PATH."
}

& ssh -F $ConfigFile -o BatchMode=yes $HostAlias $remoteCmd
exit $LASTEXITCODE
