#Requires -Version 5.1
$ErrorActionPreference = 'Stop'
$Ffmpeg = 'C:\OctoPrint\ffmpeg.exe'
$ToolDir = $PSScriptRoot
$Repo = (Resolve-Path (Join-Path $ToolDir '..\..')).Path
$Fuentes = Join-Path $Repo 'docs\erp-planificacion\agrosoft-levantamiento\fuentes'
$Videos = Join-Path $Fuentes 'videos'
$Whisper = Join-Path $Fuentes 'whisper-local'
$Src = 'C:\Users\c\Videos\Screen Recordings'

function Ensure-Wav {
  param([string]$Video, [string]$Wav)
  $dir = Split-Path $Wav -Parent
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  if ((Test-Path -LiteralPath $Wav) -and (Get-Item -LiteralPath $Wav).Length -gt 100KB) {
    Write-Host "WAV ok $Wav"
    return
  }
  if (-not (Test-Path -LiteralPath $Video)) { throw "Falta video: $Video" }
  Write-Host "ffmpeg -> $Wav"
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  & $Ffmpeg -y -i $Video -vn -ac 1 -ar 16000 -c:a pcm_s16le $Wav
  $code = $LASTEXITCODE
  $ErrorActionPreference = $prev
  if ($code -ne 0 -or -not (Test-Path -LiteralPath $Wav)) { throw "ffmpeg fallo $Video ($code)" }
}

$jobs = @(
  @{
    id = 'reu5'
    video = (Join-Path $Videos 'reunion5-2026-08-03.mp4')
    dir = 'reu5'
    title = 'Reu5 2026-08-03 (Whisper large-v3)'
    fuente = $null
    driveParent = '1ngQEINfyiHPVu5nDZFt8Zsasgh65sob9'
    driveOldId = '119rdMx8D9Ffdgc8lFAGKqpp37gmFZZoO'
  }
  @{
    id = '2026-08-19'
    video = (Join-Path $Src 'Screen Recording 2026-08-19 162555.mp4')
    dir = '2026-08-19-demo-interno'
    title = 'Demo interno Carlos/Sergio 2026-08-19 (Whisper large-v3)'
    fuente = $null
    driveParent = '1gZSKcB0KbSL8WqoHKSncjv0doF2J5vu8'
    driveOldId = '1fsjs8lgDFwYCrOBXP7BywPMnaCi31f8r'
  }
  @{
    id = '2026-08-05-gosocket'
    video = (Join-Path $Src 'Screen Recording 2026-08-05 120048.mp4')
    dir = '2026-08-05-gosocket-interna'
    title = 'Interna GoSocket Carlos/Sergio 2026-08-05 (Whisper large-v3)'
    fuente = $null
    driveParent = '1hNVPuBh0Sus28YzE2KCOMBr8KpbkVpuB'
    driveOldId = $null
  }
  @{
    id = '2026-09-14-tesoreria'
    video = (Join-Path $Videos 'reunion-2026-09-14-interna-tesoreria-carlos-sergio.mp4')
    dir = '2026-09-14-interna-tesoreria'
    title = 'Interna tesoreria cartolas Carlos/Sergio 2026-09-14 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-14-interna-tesoreria.md')
    driveParent = $null
    driveOldId = $null
  }
  @{
    id = 'sergio-2026-09-10'
    video = (Join-Path $Src 'Screen Recording 2026-09-10 102149.mp4')
    dir = 'sergio-2026-09-10'
    title = 'Interna Carlos/Sergio 2026-09-10 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-10-interna-carlos-sergio.md')
    driveParent = '1llT43AOQYLNDNFso1VtuFoD7DusIgq8z'
    driveOldId = '1VQR-YoBUJJNZmx9mhnD00oVZq4DV7hBF'
  }
  @{
    id = '2026-09-01-trello'
    video = (Join-Path $Src 'Screen Recording 2026-09-01 132744.mp4')
    dir = 'sergio-2026-09-01'
    title = 'Interna Trello cartola Carlos/Sergio 2026-09-01 (Whisper large-v3)'
    fuente = $null
    driveParent = '1AHxWmJshoHsCN6sBG4FeNa-Hz7fUL6xh'
    driveOldId = '1cgvHYTFDN4HyCRgDro6HCE3ozvvKg1E1'
  }
  @{
    id = '2026-08-20-manana'
    video = (Join-Path $Src 'Screen Recording 2026-08-20 105836.mp4')
    dir = '2026-08-20-manana'
    title = 'Interna Carlos/Sergio manana 2026-08-20 (Whisper large-v3)'
    fuente = $null
    driveParent = '1_NFQMYrTNhBsvpZHTgrSQTWM9aR58iG2'
    driveOldId = '19WH1zy7pVWkOA2hQ4CpF1B09dLgNz9yM'
  }
  @{
    id = '2026-09-03'
    video = (Join-Path $Src 'Screen Recording 2026-09-03 110956.mp4')
    dir = '2026-09-03-interna'
    title = 'Interna Carlos/Sergio 2026-09-03 (Whisper large-v3)'
    fuente = $null
    driveParent = '1Ek8-flw-8mngWjcdDO5b0Vel46HzoB6A'
    driveOldId = '1_G_3FbxzNlnKGeB0m65xK34-bNueD-8B'
  }
  @{
    id = '2026-08-04-gosocket'
    video = (Join-Path $Src 'Screen Recording 2026-08-04 123705.mp4')
    dir = '2026-08-04-gosocket'
    title = 'GoSocket con MJ 2026-08-04 (Whisper large-v3)'
    fuente = $null
    driveParent = '1kNU8nqt3yMRo8WLpOYPUFznaPufMuer1'
    driveOldId = $null
  }
  @{
    id = 'reu3'
    video = (Join-Path $Videos 'reunion3-2026-07-28.mp4')
    dir = 'reu3'
    title = 'Reu3 2026-07-28 (Whisper large-v3)'
    fuente = $null
    driveParent = '1G2e1pzqAk7Q0LxfPtMqajKQdzjPfCYDJ'
    driveOldId = '1TohdPw_LnhPO80k0TQgMhvc7-rrKO3T9'
  }
  @{
    id = '2026-09-07'
    video = (Join-Path $Videos 'Screen Recording 2026-09-07 162654.mp4')
    dir = '2026-09-07-interna'
    title = 'Interna Carlos/Sergio 2026-09-07 (Whisper large-v3)'
    fuente = $null
    driveParent = '1xaYS2NrTVsawjJX5FANZfdf4ZtaTI8yC'
    driveOldId = '1U1nIoUjnDstb9DuNM_sMQtTZIhQ2zu9z'
  }
  @{
    id = '2026-08-20-tarde'
    video = (Join-Path $Src 'Screen Recording 2026-08-20 174935.mp4')
    dir = '2026-08-20-tarde'
    title = 'Cliente Lupe y Mario 2026-08-20 tarde (Whisper large-v3)'
    fuente = $null
    driveParent = '1IQzJ3rA_B24_VA0hJIpOPj07azZV5Yyt'
    driveOldId = '1CpXaaqaLZMBvmKmSAzJ4Qwyw-qWLDLFf'
  }
  @{
    id = '2026-09-14-manana'
    video = (Join-Path $Videos 'reunion-2026-09-14-interna-manana-carlos-sergio.mp4')
    dir = '2026-09-14-interna-manana'
    title = 'Interna Carlos/Sergio manana 2026-09-14 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-14-interna-manana.md')
    driveParent = $null
    driveOldId = $null
  }
  @{
    id = '2026-09-14-mediodia'
    video = (Join-Path $Videos 'reunion-2026-09-14-interna-mediodia-carlos-sergio.mp4')
    dir = '2026-09-14-interna-mediodia'
    title = 'Interna Carlos/Sergio mediodia 2026-09-14 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-14-interna-mediodia.md')
    driveParent = $null
    driveOldId = $null
  }
  @{
    id = '2026-08-13-kickoff'
    video = (Join-Path $Src 'Screen Recording 2026-08-13 123318.mp4')
    dir = '2026-08-13-kickoff-gosocket'
    title = 'Kickoff GoSocket 2026-08-13 (Whisper large-v3)'
    fuente = $null
    driveParent = '1qwcK999JrJSJIqXyY8IvrvUJZ_vAg79n'
    driveOldId = $null
  }
  @{
    id = '2026-08-25-erp'
    video = (Join-Path $Src 'Screen Recording 2026-08-25 112308.mp4')
    dir = '2026-08-25-erp-interna'
    title = 'Interna ERP Carlos/Sergio 2026-08-25 (Whisper large-v3)'
    fuente = $null
    driveParent = '1xoD2PPSOH_Xk_GcC4gFTLLdJxeZEUwsn'
    driveOldId = $null
  }
  @{
    id = '2026-08-25-kickoff'
    video = (Join-Path $Src 'Screen Recording 2026-08-25 122402.mp4')
    dir = '2026-08-25-kickoff-gosocket'
    title = 'Kickoff GoSocket 2026-08-25 (Whisper large-v3)'
    fuente = $null
    driveParent = '1jBQgIUIvZUl-TmBZKMjQBIkj-p5LASfj'
    driveOldId = $null
  }
  @{
    id = 'reu6'
    video = (Join-Path $Src 'Screen Recording 2026-08-06 170730.mp4')
    dir = 'reu6'
    title = 'Reu6 2026-08-06 MJ y Agustin (Whisper large-v3)'
    fuente = $null
    driveParent = '1xRzs8i5yttetyyYd0EZqX0hKq0Vg8fqh'
    driveOldId = '1pUhBr02NSAVhRamhIZAzD8WQ9vWCxLaW'
  }
  @{
    id = 'demo-2026-09-10'
    video = (Join-Path $Videos 'reunion-2026-09-10-demo-cliente.mp4')
    dir = 'demo-2026-09-10'
    title = 'Demo cliente avances 2026-09-10 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-10-demo-cliente.md')
    driveParent = '15ny579CdVB2-WZDZwqTz-Y2pXH2EAH5A'
    driveOldId = '1c-ijfpRu9do_4Uwlfpi--4ewgs-Ob14p'
  }
  @{
    id = '2026-08-27-tesoreria-ui'
    video = (Join-Path $Src 'Screen Recording 2026-08-27 172119.mp4')
    dir = '2026-08-27-tesoreria-ui'
    title = 'Interna tesoreria UI Carlos/Sergio 2026-08-27 (Whisper large-v3)'
    fuente = $null
    driveParent = '1QQz2Sisz71uWCVbpD0I5fHa07KKnSTI-'
    driveOldId = $null
  }
  @{
    id = '2026-09-08-seguimiento'
    video = (Join-Path $Src 'Screen Recording 2026-09-08 123129.mp4')
    dir = '2026-09-08-seguimiento-gosocket'
    title = 'Seguimiento GoSocket 2026-09-08 (Whisper large-v3)'
    fuente = $null
    driveParent = '1795kwsTaDMN51uxO5vWarsNBcjBUD3dc'
    driveOldId = $null
  }
  @{
    id = '2026-09-08-recap'
    video = (Join-Path $Src 'Screen Recording 2026-09-08 130041.mp4')
    dir = '2026-09-08-recap'
    title = 'Recap Carlos/Sergio 2026-09-08 (Whisper large-v3)'
    fuente = $null
    driveParent = '1Jnj0S8Cq-2ZTQ__2UuCkfSOsFzkmHxQY'
    driveOldId = $null
  }
  @{
    id = 'reu2'
    video = (Join-Path $Videos 'reunion2-2026-07-23.mp4')
    dir = 'reu2'
    title = 'Reu2 2026-07-23 (Whisper large-v3)'
    fuente = $null
    driveParent = '1wSj_ydbt2TlOkKeIl7FHkalomzARuezG'
    driveOldId = '1IzyDFppCGtJHPH4lnp3GuTCZJedKVoDS'
  }
  @{
    id = 'reu4'
    video = (Join-Path $Videos 'reunion4-2026-07-30.mp4')
    dir = 'reu4'
    title = 'Reu4 2026-07-30 (Whisper large-v3)'
    fuente = $null
    driveParent = '1erykUjjfIiS1ue2m77JvvhJB8e0FrVDQ'
    driveOldId = '18fgey_RAOKtfESS6fxJOny47TlqSEabi'
  }
  @{
    id = '2026-09-14-demo'
    video = (Join-Path $Videos 'reunion-2026-09-14-demo-avances.mp4')
    dir = '2026-09-14-demo-avances'
    title = 'Demo cliente avances 2026-09-14 (Whisper large-v3)'
    fuente = (Join-Path $Fuentes 'transcripcion-2026-09-14-demo-avances.md')
    driveParent = $null
    driveOldId = $null
  }
  @{
    id = 'reu1'
    video = (Join-Path $Videos 'reunion1-2026-07-21.mp4')
    dir = 'reu1'
    title = 'Reu1 2026-07-21 (Whisper large-v3)'
    fuente = $null
    driveParent = '1dWXHflMukKNxMB_9I0tCb-siGRQDeB3k'
    driveOldId = '1Xea2op_5vr8U_kgWVP11va1JdXiZfmzs'
  }
)

$jsonJobs = @()
foreach ($j in $jobs) {
  $wav = Join-Path (Join-Path $Whisper $j.dir) 'audio.wav'
  Ensure-Wav -Video $j.video -Wav $wav
  $out = Join-Path (Join-Path $Whisper $j.dir) 'transcripcion-whisper.md'
  $copy = @()
  if ($j.fuente) { $copy += $j.fuente }
  $jsonJobs += [ordered]@{
    id = $j.id
    audio = $wav
    out = $out
    title = $j.title
    source = $j.video
    copyTo = $copy
    driveParent = $j.driveParent
    driveOldId = $j.driveOldId
  }
}

$outJson = Join-Path $ToolDir 'jobs-v3.json'
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($outJson, ($jsonJobs | ConvertTo-Json -Depth 6), $utf8NoBom)
Write-Host "WROTE $outJson jobs=$($jsonJobs.Count)"
