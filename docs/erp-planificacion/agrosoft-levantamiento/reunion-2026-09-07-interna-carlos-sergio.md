# Reunión interna 07/09/2026 — Carlos ↔ Sergio (NC Libro de ventas)

**Grabación:** [`fuentes/videos/Screen Recording 2026-09-07 162654.mp4`](fuentes/videos/Screen%20Recording%202026-09-07%20162654.mp4) (~53 min, gitignored)  
**Quién:** Carlos (desarrollo) y Sergio (Devint). **No hay Agustín ni MJ.**  
**Transcripción bruta:** [`fuentes/transcripcion-2026-09-07-interna-carlos-sergio.md`](fuentes/transcripcion-2026-09-07-interna-carlos-sergio.md)  
**Regla:** Sergio/Carlos = hipótesis de diseño del proveedor. No pisa Reu6 ni la sesión Lupe/Mario 20/08.

---

## Qué se acordó sobre anulación (Libro de ventas)

En el Libro, el botón no es «reverso contable»: es **Anulación** = emitir **nota de crédito** contra la factura.

Al presionar Anulación, un modal pide el **CodRef SII** (nodo referencia del XML):

| CodRef | Texto | UI |
|---|---|---|
| **1** | Anula Documento de Referencia | Confirmar y emitir NC al 100% (sin formulario largo) |
| **2** | Corrige Texto Documento de Referencia | Elegir ítem, ver texto actual, editar; una línea de detalle, cantidad 1, precio 0 |
| **3** | Corrige montos | Formulario con líneas de la factura; la NC es lo que se **rebaja**, no el saldo que queda |

La NC lleva TpoDocRef, FolioRef, FchRef y CodRef 1/2/3 y se envía a GoSocket como un DTE 61 (misma estructura de factura + referencias).

## Otros temas de la misma grabación (no son el alcance de esta tanda)

- Cuentas: Sergio las deja en **Libro** (y opcionalmente al facturar en Emitir), no en la OV. Ya había trabajo previo en código.
- Tracking: si hay NC de anulación total, la factura debería verse **Anulada** a nivel de lista `[39:21]`.
- Carga masiva de facturas pre-ERP `[23:24]`.
- ND «desde cualquier documento» (Carlos `[00:52]`, no aplicado).
- Tarjetas Trello para MJ (operativo, no producto).
