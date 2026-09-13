#Requires -Version 5.1
<#
.SYNOPSIS
  Extrae WAV 16k mono y transcribe reuniones Almahue con faster-whisper.
.EXAMPLE
  .\batch-reu.ps1 -Reu 5
  .\batch-reu.ps1 -All
#>
param(
  [int[]]$Reu = @(),
  [switch]$All,
  [switch]$SkipExtract,
  [string]$Model = 'small'
)

$ErrorActionPreference = 'Stop'
$ToolDir = $PSScriptRoot
$Repo = (Resolve-Path (Join-Path $ToolDir '..\..')).Path
$Fuentes = Join-Path $Repo 'docs\erp-planificacion\agrosoft-levantamiento\fuentes'
$Videos = Join-Path $Fuentes 'videos'
$OutRoot = Join-Path $Fuentes 'whisper-local'
$Ffmpeg = 'C:\OctoPrint\ffmpeg.exe'
$Py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $Py) { throw 'python no encontrado' }
if (-not (Test-Path $Ffmpeg)) { throw "ffmpeg no encontrado: $Ffmpeg" }

# ffmpeg imprime a stderr; no tumbar el script
$FfmpegErrorAction = $ErrorActionPreference

$Map = @{
  1 = @{ Video = (Join-Path $Videos 'reunion1-2026-07-21.mp4'); Title = 'Reu1 2026-07-21 (Whisper local)'; Tldv = 'transcripcion.md' }
  2 = @{ Video = (Join-Path $Videos 'reunion2-2026-07-23.mp4'); Title = 'Reu2 2026-07-23 (Whisper local)'; Tldv = 'transcripcion-reunion2.md' }
  3 = @{ Video = (Join-Path $Videos 'reunion3-2026-07-28.mp4'); Title = 'Reu3 2026-07-28 (Whisper local)'; Tldv = 'transcripcion-reunion3.md' }
  4 = @{ Video = (Join-Path $Videos 'reunion4-2026-07-30.mp4'); Title = 'Reu4 2026-07-30 (Whisper local)'; Tldv = 'transcripcion-reunion4.md' }
  5 = @{ Video = (Join-Path $Videos 'reunion5-2026-08-03.mp4'); Title = 'Reu5 2026-08-03 (Whisper local)'; Tldv = 'transcripcion-reunion5.md' }
  6 = @{
    # 11:00 era otro Meet (no ERP). R6 cliente = tarde ~17:07.
    Video = 'C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-06 170730.mp4'
    Title = 'Reu6 2026-08-06 (Whisper local, screen recording 17:07)'
    Tldv = 'transcripcion-reunion6.md'
  }
}

if ($All) { $Reu = @(5, 3, 2, 4, 1, 6) }
if (-not $Reu -or $Reu.Count -eq 0) { throw 'Indica -Reu N o -All' }

New-Item -ItemType Directory -Force -Path $OutRoot | Out-Null

foreach ($n in $Reu) {
  if (-not $Map.ContainsKey($n)) { Write-Warning "Reu $n no mapeada"; continue }
  $m = $Map[$n]
  $dir = Join-Path $OutRoot ("reu{0}" -f $n)
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $wav = Join-Path $dir 'audio.wav'
  $md = Join-Path $dir 'transcripcion-whisper.md'
  $vid = $m.Video

  if (-not (Test-Path $vid)) {
    Write-Warning "Falta video: $vid"
    continue
  }

  Write-Host "==== Reu$n ====" -ForegroundColor Cyan
  Write-Host "Video: $vid"

  if (-not $SkipExtract -or -not (Test-Path $wav)) {
    Write-Host "Extrayendo WAV 16k mono..."
    $ErrorActionPreference = 'Continue'
    & $Ffmpeg -y -i $vid -vn -ac 1 -ar 16000 -c:a pcm_s16le $wav 2>$null
    $ffExit = $LASTEXITCODE
    $ErrorActionPreference = 'Stop'
    if ($ffExit -ne 0 -or -not (Test-Path $wav)) { throw "ffmpeg falló ($ffExit) o no creó $wav" }
  }

  Write-Host "Whisper $Model..."
  & $Py (Join-Path $ToolDir 'transcribe_one.py') `
    --audio $wav `
    --out $md `
    --title $m.Title `
    --source $vid `
    --model $Model
  if ($LASTEXITCODE -ne 0) { throw "Whisper falló Reu$n" }
  Write-Host "OK $md"
}

Write-Host "Listo. Limpieza Ollama: tools/transcript-ollama (chunked) o contraste manual."
