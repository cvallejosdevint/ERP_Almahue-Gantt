# Plan Trello — mover mocks a review cliente

**Fecha:** 2026-07-30  
**Tablero:** https://trello.com/b/wixKcrP0/almahue-erp

## Nombre de columna

| Texto pedido | Real en tablero |
|---|---|
| «WA Almahue» / «En Kua al Mawe» (minuta) | **`En QA Almahue`** (`idList=6a54f9be2f15b6cbeb89dfdd`) |

## Estado local (snapshot — puede estar desactualizado)

- ~25 cards `Mock — *` en **En proceso**
- Capturas en `docs/trello-capturas-erp-mock/` (muchas con rutas/UI viejas)
- ~24 pantallas nuevas **sin captura** (compras, cartolas, periodos, plantilla docs, etc.)

## Bloqueante

Faltan en el entorno: `TRELLO_KEY` + `TRELLO_TOKEN`.

```powershell
cd E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento
$env:TRELLO_KEY = "..."
$env:TRELLO_TOKEN = "..."
$env:TRELLO_BOARD = "wixKcrP0"
python extraer-trello.py
```

## Secuencia cuando haya credenciales

1. Snapshot fresco (`extraer-trello.py`)
2. Actualizar `docs/trello-capturas-erp-mock/capture.mjs` (rutas nuevas)
3. Front en `npm run dev` + regenerar PNG
4. Parche/script: mover `Mock — *` → **En QA Almahue** + re-adjuntar capturas
5. Crear cards faltantes (Compras, Cartolas, Periodos, …) directo en QA
6. Re-snapshot y checklist de adjuntos

## Criterio

Solo mover a **En QA Almahue** pantallas listas para review cliente (minuta Reu3). No mover OUT/Presupuestos/Reporte ejecutivo sin decisión producto.
