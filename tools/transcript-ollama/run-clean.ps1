#Requires -Version 5.1
$ErrorActionPreference = 'Stop'
$ToolDir = $PSScriptRoot
$Repo = (Resolve-Path (Join-Path $ToolDir '..\..')).Path
$Fuentes = Join-Path $Repo 'docs\erp-planificacion\agrosoft-levantamiento\fuentes'
$OutDir = Join-Path $ToolDir 'out'
$PromptFile = Join-Path $ToolDir 'prompts\system-es-cl.md'
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$env:OLLAMA_MODELS = if ($env:OLLAMA_MODELS) { $env:OLLAMA_MODELS } else { 'E:\OllamaModels' }
$Model = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { 'qwen2.5-coder:14b' }
$Api = if ($env:OLLAMA_HOST) { $env:OLLAMA_HOST.TrimEnd('/') } else { 'http://127.0.0.1:11434' }
$System = Get-Content -Raw -Encoding UTF8 $PromptFile

$files = Get-ChildItem -Path $Fuentes -Filter 'transcripcion*.md'
foreach ($f in $files) {
  Write-Host "Limpiando $($f.Name) via $Api/api/generate ($Model) ..."
  $body = Get-Content -Raw -Encoding UTF8 $f.FullName
  if ($body.Length -gt 18000) { $body = $body.Substring(0, 18000) + "`n`n[TRUNCADO para contexto local]" }
  $prompt = @"
$System

Transcripcion ($($f.Name)):
$body

Devuelve solo Markdown estructurado. Prohibido hablar de mermas.
"@
  $payload = @{
    model = $Model
    prompt = $prompt
    stream = $false
    options = @{ temperature = 0.2 }
  } | ConvertTo-Json -Depth 5
  $resp = Invoke-RestMethod -Method Post -Uri "$Api/api/generate" -ContentType 'application/json; charset=utf-8' -Body ([System.Text.Encoding]::UTF8.GetBytes($payload)) -TimeoutSec 600
  $outFile = Join-Path $OutDir ($f.BaseName + '-limpia.md')
  Set-Content -Path $outFile -Value $resp.response -Encoding UTF8
  Write-Host "OK $outFile"
}
Write-Host "Listo. Consolida a docs/transcripcion-limpia-v2.md"
