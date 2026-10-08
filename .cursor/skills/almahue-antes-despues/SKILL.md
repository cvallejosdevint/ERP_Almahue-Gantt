---
name: almahue-antes-despues
description: >-
  Arma la comparación antes/después y el recorrido HTML de una pantalla del ERP
  Almahue, con capturas Playwright y recuadros NUEVO. Use when the user asks for
  antes, después, recorrido, comparacion.html, capturas de presentación, marcadores
  o pins sobre una pantalla del ERP.
---

# Antes, después y recorrido

Salida de una sesión, para otro chat o para mostrar el cambio. No publiques en GitHub Pages ni hagas commit salvo que lo pidan.

Carpeta: `docs/sesiones/<tema>-YYYY-MM-DD/`.

| Archivo | Qué es |
|---|---|
| `antes-<pantalla>.png` | La pantalla como estaba |
| `despues-<pantalla>.png` | La pantalla como está, sin recuadros |
| `despues-<pantalla>-marcado.png` | La misma, con recuadros verdes |
| `comparacion.html` | Pares antes / después. Copia [plantilla-comparacion.html](plantilla-comparacion.html) |
| `recorrido.html` | Pasos con pins. Copia [plantilla-recorrido.html](plantilla-recorrido.html) |

No inventes otro layout. Copia la plantilla y reemplaza títulos, imágenes y textos.

## Captura

Playwright (`plugin-playwright-playwright`). No uses el navegador interno de Cursor.

- Front local `http://localhost:5174`. Si no responde, `.cursor/scripts/start-local-stack.ps1`.
- Login demo `admin@almahue.local` / `Admin123!` solo si la sesión no está abierta.
- La foto muestra menú, contenido y paneles laterales. No achiques el viewport. No uses zoom del navegador: recorta la ventana.
- Captura del viewport, no de la página completa.
- No pulses Guardar, Sincronizar, Contabilizar, Vincular, Enviar ni Pagar para sacar la foto. Si el cambio está en un modal, ábrelo y detente antes del botón que confirma.
- Si cambias el periodo de la sesión para encuadrar, déjalo como estaba.
- El después de un combo o una lista tiene que mostrarlos abiertos. Un desplegable cerrado no sirve de después.
- Si el antes ya existe en otra sesión y esa pantalla no cambió, copia ese PNG. No la vuelvas a sacar.

## Recuadro NUEVO

Solo en el después de la comparación. Mide cada control nuevo con `getBoundingClientRect` (píxeles CSS). Lee el ancho del PNG. La escala es `anchoPng / anchoCss`. En esta máquina el PNG sale a 1920 y el CSS a 1536, así que la escala es 1,25. Dibujar el CSS directo sobre el PNG corre el recuadro.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .cursor/skills/almahue-antes-despues/marcar-nuevo.ps1 `
  -Image docs/sesiones/<tema>-YYYY-MM-DD/despues-<pantalla>.png `
  -Scale 1.25 `
  -Boxes "x,y,w,h;x,y,w,h"
```

`Boxes` va en píxeles CSS, separados por `;`. El script escribe `despues-<pantalla>-marcado.png` al lado. Color `rgb(21,128,61)`, trazo 4, texto NUEVO en Segoe UI 12 negrita. Si el recuadro corta la fila de arriba, súbelo o bájalo hasta que rodee solo el control nuevo.

## Pins del recorrido

Van en el PNG sin marcar. `x` e `y` son porcentaje del ancho y del alto de esa imagen, y el centro del pin cae sobre el control.

```
x = (rect.x + rect.width / 2) * escala / anchoPng * 100
y = (rect.y + rect.height / 2) * escala / altoPng * 100
```

Abre el HTML y comprueba el pin. Si no cae en el botón, campo o combo, corrige el porcentaje. No achiques la ventana para acercarlo.

Cada pin dice de dónde sale el dato y qué no se apretó. Un paso por pantalla. La clase de color es `compras`, `ventas`, `conta`, `teso` o `param`.

## Texto

Español. No uses raya larga ni flecha. El párrafo de cabecera ocupa el ancho de la columna: no le pongas `max-width` de 60 a 85 caracteres. En cada par, di qué cambió y qué no se guardó. Los enlaces entre carpetas de `docs/sesiones/` tienen que existir. La comparación usa la imagen marcada. El recorrido usa la imagen sin marcar.
