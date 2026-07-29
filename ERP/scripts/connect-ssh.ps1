# Configura una conexión SSH reutilizable (sin contraseñas en disco).
# Uso: .\scripts\connect-ssh.ps1
# Tras configurar: ssh -F .deploy/ssh_config erp-deploy '<cmd>'
# o: .\scripts\remote.ps1 -- uname -a

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$DeployDir = Join-Path $Root '.deploy'
$EnvFile = Join-Path $DeployDir 'ssh.env'
$ConfigFile = Join-Path $DeployDir 'ssh_config'
$HostAlias = 'erp-deploy'

function Resolve-DefaultIdentity {
  $sshDir = Join-Path $HOME '.ssh'
  $candidates = @(
    (Join-Path $sshDir 'id_ed25519'),
    (Join-Path $sshDir 'id_rsa'),
    (Join-Path $sshDir 'id_ecdsa')
  )
  foreach ($path in $candidates) {
    if (Test-Path -LiteralPath $path) { return $path }
  }
  return (Join-Path $sshDir 'id_ed25519')
}

function Expand-UserPath([string]$Path) {
  if ([string]::IsNullOrWhiteSpace($Path)) { return $Path }
  if ($Path.StartsWith('~/') -or $Path.StartsWith('~\')) {
    return Join-Path $HOME $Path.Substring(2)
  }
  if ($Path -eq '~') { return $HOME }
  return [System.IO.Path]::GetFullPath($Path)
}

if (-not (Get-Command ssh -ErrorAction SilentlyContinue)) {
  Write-Error "ssh no está en PATH. Instala OpenSSH Client (Windows Features) o Git for Windows."
}

Write-Host ""
Write-Host "=== Conexion SSH ERP (sin guardar passwords) ===" -ForegroundColor Cyan
Write-Host "Los datos se escriben solo en ERP/.deploy/ (gitignored)."
Write-Host ""

$hostInput = Read-Host "Host / IP"
if ([string]::IsNullOrWhiteSpace($hostInput)) {
  Write-Error "Host/IP es obligatorio."
}

$portInput = Read-Host "Puerto SSH [22]"
if ([string]::IsNullOrWhiteSpace($portInput)) { $portInput = '22' }
$port = 0
if (-not [int]::TryParse($portInput, [ref]$port) -or $port -lt 1 -or $port -gt 65535) {
  Write-Error "Puerto invalido: $portInput"
}

$userInput = Read-Host "Usuario SSH"
if ([string]::IsNullOrWhiteSpace($userInput)) {
  Write-Error "Usuario es obligatorio."
}

$defaultIdentity = Resolve-DefaultIdentity
$identityPrompt = "Ruta clave privada [$defaultIdentity] (Enter = default, o vacio forzado con 'none')"
$identityInput = Read-Host $identityPrompt
if ([string]::IsNullOrWhiteSpace($identityInput)) {
  $identityFile = $defaultIdentity
} elseif ($identityInput.Trim().ToLowerInvariant() -eq 'none') {
  $identityFile = $null
} else {
  $identityFile = Expand-UserPath $identityInput.Trim()
}

if ($identityFile -and -not (Test-Path -LiteralPath $identityFile)) {
  Write-Warning "No existe la clave: $identityFile"
  Write-Host "Puedes generarla con: ssh-keygen -t ed25519 -C `"tu@email`""
  Write-Host "Luego copia la pubkey al server (ssh-copy-id o pegar ~/.ssh/*.pub en authorized_keys)."
}

New-Item -ItemType Directory -Force -Path $DeployDir | Out-Null

# ssh.env — variables para wrappers / agentes
$envLines = @(
  "# Generado por scripts/connect-ssh.ps1 — NO commitear",
  "SSH_HOST=$hostInput",
  "SSH_PORT=$port",
  "SSH_USER=$userInput"
)
if ($identityFile) {
  $envLines += "SSH_IDENTITY=$identityFile"
} else {
  $envLines += "SSH_IDENTITY="
}
Set-Content -LiteralPath $EnvFile -Value $envLines -Encoding utf8

# ssh_config — Host alias reutilizable
$configLines = @(
  "# Generado por scripts/connect-ssh.ps1 — NO commitear",
  "Host $HostAlias",
  "  HostName $hostInput",
  "  Port $port",
  "  User $userInput"
)
if ($identityFile) {
  # Forward slashes ayudan a OpenSSH en Windows
  $idForSsh = ($identityFile -replace '\\', '/')
  $configLines += "  IdentityFile $idForSsh"
  $configLines += "  IdentitiesOnly yes"
}
$configLines += "  StrictHostKeyChecking accept-new"
$configLines += ""
Set-Content -LiteralPath $ConfigFile -Value $configLines -Encoding utf8

Write-Host ""
Write-Host "Escrito:" -ForegroundColor Green
Write-Host "  $EnvFile"
Write-Host "  $ConfigFile"
Write-Host ""
Write-Host "Probando conexion..." -ForegroundColor Cyan

$sshArgs = @(
  '-F', $ConfigFile,
  '-o', 'BatchMode=yes',
  '-o', 'ConnectTimeout=15',
  $HostAlias,
  'echo OK && uname -a && whoami'
)

& ssh @sshArgs
$exit = $LASTEXITCODE

Write-Host ""
if ($exit -eq 0) {
  Write-Host "Conexion OK." -ForegroundColor Green
} else {
  Write-Host "Fallo la prueba SSH (exit $exit)." -ForegroundColor Yellow
  Write-Host ""
  Write-Host "Si el server pide password: el agente NO puede tipearlo de forma fiable."
  Write-Host "Opciones recomendadas:"
  Write-Host "  1) Generar clave:  ssh-keygen -t ed25519"
  Write-Host "  2) Subir pubkey al server (authorized_keys), p.ej. desde una terminal interactiva:"
  Write-Host "       type `$env:USERPROFILE\.ssh\id_ed25519.pub | ssh -p $port ${userInput}@${hostInput} `"mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys`""
  Write-Host "  3) O autenticarte una vez en tu terminal (ssh interactivo) fuera del agente."
  Write-Host "Luego vuelve a ejecutar: .\scripts\connect-ssh.ps1"
}

Write-Host ""
Write-Host "=== Para el agente Cursor ===" -ForegroundColor Cyan
Write-Host "Dile al agente: usa ssh -F ERP/.deploy/ssh_config erp-deploy '<cmd>'"
Write-Host ""
Write-Host "Ejemplos (desde ERP/):"
Write-Host "  ssh -F .deploy/ssh_config erp-deploy `"uname -a`""
Write-Host "  .\scripts\remote.ps1 -- uname -a"
Write-Host "  .\scripts\remote.ps1 -- docker ps"
Write-Host ""
