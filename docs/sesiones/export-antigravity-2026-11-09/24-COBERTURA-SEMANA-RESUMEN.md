# Cobertura acuerdos semana pasada · resumen PM

Fuentes:
- En QA 05/11: [Cobertura En QA 05/11](859b0b56-dd8c-476b-8523-216ca0e1288b) → `22-COBERTURA-EN-QA-05-11.md`
- 03/11 + packing: [Cobertura 03/11 + packing](7f044369-c560-4f0d-8ead-f38e33f91847) → `20-COBERTURA-03-11-PACKING.md`

## Matriz

| # | Acuerdo | Veredicto | Nota |
|---|---|---|---|
| 23-28 | Reversa / proformas / libro / guías hijas / calce | CUBIERTO | |
| 29-34, 36 | Organigrama 4 niveles, roles, usuarios, ramas, jefatura, tope GG, AND/OR | CUBIERTO en código | **BLOQUEADO operar** sin migrate `20261109`+`20261110` |
| 35 | Topes multimoneda + TC BC editable | **CUBIERTO** | Fix [Fix #35 TC](f5f603c5-06ab-4585-a73d-49c62aef85d6) · `23-FIX-35-TIPO-CAMBIO-OC.md` |
| 37-38 | Recetas packing / promedio ponderado | CUBIERTO | |
| 39 | Confirmar guía con adjuntos | **CUBIERTO** | Fix [Fix #39 adjuntos](77876ab7-f6e1-427d-af82-0c0708f4c087) · `21-FIX-39-ADJUNTOS.md` |

## Bloqueantes para “funciona en demo local”

1. **P0** Aplicar migraciones organigrama (controlado; no prod a ciegas).
2. ~~#35 / #39~~ cerrados. Queda migrate organigrama + seed/simulador.
3. Recomendado: seed organigrama + alinear simulador UI a `POST aprobaciones/simular` (aún calcula local).
