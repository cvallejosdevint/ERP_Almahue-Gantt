# Dibuja recuadros NUEVO sobre un PNG de despues.
# Boxes: pixeles CSS "x,y,w,h;x,y,w,h". Scale = anchoPng / anchoCss (1.25 en captura Playwright a 1920).
param(
  [Parameter(Mandatory = $true)][string]$Image,
  [double]$Scale = 1,
  [Parameter(Mandatory = $true)][string]$Boxes,
  [string]$Out
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$srcPath = (Resolve-Path -LiteralPath $Image).Path
if (-not $Out) {
  $dir = Split-Path -Parent $srcPath
  $name = [IO.Path]::GetFileNameWithoutExtension($srcPath)
  $Out = Join-Path $dir ($name + '-marcado.png')
}

$src = [System.Drawing.Image]::FromFile($srcPath)
$bmp = New-Object System.Drawing.Bitmap $src.Width, $src.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
$g.DrawImage($src, 0, 0, $src.Width, $src.Height)

$color = [System.Drawing.Color]::FromArgb(255, 21, 128, 61)
$pen = New-Object System.Drawing.Pen $color, 4
$font = New-Object System.Drawing.Font 'Segoe UI', 12, ([System.Drawing.FontStyle]::Bold)
$brush = New-Object System.Drawing.SolidBrush $color

foreach ($part in ($Boxes -split ';')) {
  $chunk = $part.Trim()
  if (-not $chunk) { continue }
  $n = @($chunk.Split(',') | ForEach-Object { [double]$_.Trim() })
  if ($n.Count -lt 4) { throw "Caja invalida: $chunk" }
  $x = [int][Math]::Round($n[0] * $Scale)
  $y = [int][Math]::Round($n[1] * $Scale)
  $w = [int][Math]::Round($n[2] * $Scale)
  $h = [int][Math]::Round($n[3] * $Scale)
  if ($w -lt 1 -or $h -lt 1) { throw "Caja sin area: $chunk" }
  $g.DrawRectangle($pen, $x, $y, $w, $h)
  $size = $g.MeasureString('NUEVO', $font)
  $ly = [Math]::Max(0, $y - [int][Math]::Ceiling($size.Height) - 2)
  $g.DrawString('NUEVO', $font, $brush, $x, $ly)
}

$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$pen.Dispose(); $font.Dispose(); $brush.Dispose(); $g.Dispose(); $bmp.Dispose(); $src.Dispose()
Write-Output $Out
