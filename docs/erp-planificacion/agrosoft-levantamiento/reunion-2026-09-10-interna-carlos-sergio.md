# Interna Carlos ↔ Sergio — 10/09/2026 (~18 min)

**No es requisito de cliente.** Hablan Carlos Vallejos y Sergio (proveedor). Pedido posterior del usuario: recortar el panel de totales de exportación al mínimo que se ve en esta demo.

- Video (no en git): `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-09-10 102149.mp4` (~18:07)
- ASR: [`fuentes/transcripcion-2026-09-10-interna-carlos-sergio.md`](fuentes/transcripcion-2026-09-10-interna-carlos-sergio.md) (Whisper `small`; hay garabatos de ASR)
- Recorrido en pantalla: OV de exportación `10160689`, paso 3 COMEX, panel derecho **Cálculo de totales** aún en pesos ($11.100) mientras el formulario ya tenía USD 11.100 y pesos 9.435.000.

## Qué pidió Sergio del panel (mínimo)

En `[05:06]`–`[05:16]`, sobre el panel **Cálculo de totales** (no sobre el formulario COMEX):

> «Sería bueno ahí, los cálculos totales, poner la moneda… Ayer me di cuenta que aquí no tenía como esos cálculos en la exportación, tengo que agregárselo.»

En el video el formulario COMEX ya tenía: moneda USD, TC, monto dólar, monto pesos, países, vía, cláusula, puertos, bultos. **Eso no es el panel.** El hueco era que el panel derecho seguía como venta nacional (CLP, sin moneda).

**Mínimo en el panel (exportación):**

| Fila | Por qué |
|---|---|
| Subtotal / neto / exento / IVA / Total **en USD** | mismos totalizadores de siempre, con moneda |
| Moneda (13 · USD) | «poner la moneda» |
| Tipo de cambio | ya estaba en el form; el panel lo resume |
| Total CLP | «monto pesos» / conversión que también se manda al DTE |

**No van en el panel** (siguen en el formulario COMEX, paso 3): países, vía, cláusula, modalidad, puertos, tipo/cantidad de bulto, marca.

## Otros puntos de la misma grabación (hipótesis interno)

- `[02:07]`–`[03:06]` precios unitarios en dólares; TC → pesos; sync Banco Central no corría en local.
- `[03:06]`–`[04:38]` bulto numérico; países y puertos con código Aduana/SII; marcar obligatorios con asterisco.
- `[04:58]` guardar TC en borrador.
- `[06:16]`–`[06:44]` DTE debe ir en dólares **y** pesos (origen + conversión).
- `[07:02]`–`[10:07]` Libro de ventas: discriminar tipos SII (39, 41, 33, 34, 56, 61, 52, **110**, 111, **112** NC export). Código + nombre en la columna; filtro avanzado. (La 111 ND export vs 112 NC: Sergio dudó; el catálogo SII es 111 ND / 112 NC.)
- `[11:34]`–`[11:54]` alcance demo de la tarde: emisión export + NC (GoSocket). «Hasta ahí no más.»
- `[12:02]`–`[13:40]` API Banco Central (cuenta Devint, caduca anual): **no** exponer API key al cliente; queda como soporte interno.
- `[16:26]`–`[17:18]` pedir que Mario/Lupe usen lo implementado; siguiente palo: contabilizar ventas, después compras SII.

## Código local (post-reunión)

El panel de OV/exportación dejó de listar todo COMEX. Extra = moneda + TC + Total CLP; las filas de cálculo llevan sufijo USD.
