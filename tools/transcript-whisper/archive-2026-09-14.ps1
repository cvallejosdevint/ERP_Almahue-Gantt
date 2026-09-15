#Requires -Version 5.1
$ErrorActionPreference = 'Stop'
$Ffmpeg = 'C:\OctoPrint\ffmpeg.exe'
$Py = (Get-Command python).Source
$ToolDir = $PSScriptRoot
$Repo = (Resolve-Path (Join-Path $ToolDir '..\..')).Path
$Fuentes = Join-Path $Repo 'docs\erp-planificacion\agrosoft-levantamiento\fuentes'
$Videos = Join-Path $Fuentes 'videos'
$SrcRoot = 'C:\Users\c\Videos\Screen Recordings'
$WhisperRoot = Join-Path $Fuentes 'whisper-local'

New-Item -ItemType Directory -Force -Path $Videos | Out-Null

$jobs = @(
  @{
    Src = 'Screen Recording 2026-09-14 104939.mp4'
    Dest = 'reunion-2026-09-14-interna-manana-carlos-sergio.mp4'
    Dir = '2026-09-14-interna-manana'
    Title = 'Interna Carlos/Sergio manana 2026-09-14 (~40 min)'
    Md = 'transcripcion-2026-09-14-interna-manana.md'
  }
  @{
    Src = 'Screen Recording 2026-09-14 120227.mp4'
    Dest = 'reunion-2026-09-14-interna-mediodia-carlos-sergio.mp4'
    Dir = '2026-09-14-interna-mediodia'
    Title = 'Interna Carlos/Sergio mediodia 2026-09-14 (~38 min)'
    Md = 'transcripcion-2026-09-14-interna-mediodia.md'
  }
  @{
    Src = 'Screen Recording 2026-09-14 174419.mp4'
    Dest = 'reunion-2026-09-14-demo-avances.mp4'
    Dir = '2026-09-14-demo-avances'
    Title = 'Demo cliente ERP Almahue - Avances 2026-09-14 (~77 min)'
    Md = 'transcripcion-2026-09-14-demo-avances.md'
  }
  @{
    Src = 'Screen Recording 2026-09-14 183258.mp4'
    Dest = 'reunion-2026-09-14-interna-tesoreria-carlos-sergio.mp4'
    Dir = '2026-09-14-interna-tesoreria'
    Title = 'Interna tesoreria cartolas Carlos/Sergio 2026-09-14 (~13 min)'
    Md = 'transcripcion-2026-09-14-interna-tesoreria.md'
  }
)

foreach ($j in $jobs) {
  $src = Join-Path $SrcRoot $j.Src
  $dest = Join-Path $Videos $j.Dest
  $wdir = Join-Path $WhisperRoot $j.Dir
  $wav = Join-Path $wdir 'audio.wav'
  $whisperMd = Join-Path $wdir 'transcripcion-whisper.md'
  $fuenteMd = Join-Path $Fuentes $j.Md
  New-Item -ItemType Directory -Force -Path $wdir | Out-Null

  Write-Host "==== COPY $($j.Dest) ====" -ForegroundColor Cyan
  if (-not (Test-Path $dest) -or (Get-Item $dest).Length -lt 1MB) {
    Copy-Item -LiteralPath $src -Destination $dest -Force
  } else {
    Write-Host "ya existe $dest"
  }

  Write-Host "==== WAV $($j.Dir) ====" -ForegroundColor Cyan
  if (-not (Test-Path $wav) -or (Get-Item $wav).Length -lt 1MB) {
    $ErrorActionPreference = 'Continue'
    & $Ffmpeg -y -i $src -vn -ac 1 -ar 16000 -c:a pcm_s16le $wav
    $ffExit = $LASTEXITCODE
    $ErrorActionPreference = 'Stop'
    if ($ffExit -ne 0 -or -not (Test-Path $wav)) { throw "ffmpeg fallo $($j.Src) ($ffExit)" }
  } else {
    Write-Host "ya existe $wav"
  }

  Write-Host "==== WHISPER $($j.Dir) ====" -ForegroundColor Cyan
  & $Py (Join-Path $ToolDir 'transcribe_one.py') `
    --audio $wav `
    --out $whisperMd `
    --title $j.Title `
    --source $j.Src `
    --model small
  Copy-Item -LiteralPath $whisperMd -Destination $fuenteMd -Force
  Write-Host "COPIED $fuenteMd" -ForegroundColor Green
}

Write-Host 'ALL_DONE_2026_09_14' -ForegroundColor Green
