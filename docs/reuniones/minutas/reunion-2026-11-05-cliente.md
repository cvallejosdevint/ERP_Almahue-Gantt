# Reunion Almahue - 05/11/2026 (Minuta para desarrollo)

| Parametro | Detalle |
|---|---|
| **Fecha** | 05/11/2026, desde ~10:00 (02:46:01) |
| **Fuente** | `Screen Recording 2026-11-05 124610.mp4` |
| **Transcripcion** | [`transcripcion-2026-11-05-reunion.md`](../transcripciones/transcripcion-2026-11-05-reunion.md) |
| **Modelo STT** | faster-whisper `large-v3` + lexico ERP (`tools/transcript-lexico`) |

**Sala:** María Jesús (MJ), Francisca (Fran), Carlos (Devint, comparte pantalla). Sergio entra de oyente cerca de `[01:33]`. Agustín no está: MJ relata lo que le pidió después del 03/11. Lupe no está; se agenda para tesorería.

**Nota:** Lo que propone Carlos es hipotesis hasta que MJ o Fran lo confirman. Si esta minuta y la transcripcion chocan, gana la transcripcion.

---

## 1. Roles, auditoria y organigrama `[07:17 - 01:17:23]`

* **Dos cuentas que parametrizan el sistema:** gerente general y jefatura de contabilidad. No operan el dia a dia. La cuenta maestra no lleva nombre de persona; la usa quien configura (MJ menciona a Mario / TI). `[20:46]`, `[21:11]`, `[21:57]`
* **El resto no es administrador.** Una jefatura ve la auditoria de su modulo, no la de todos los modulos, y no elimina, mueve ni agrega parametros. `[21:20]`, `[16:39]`
* **Lo simple, confirmado por MJ:** el acceso se define por rol y cargo (que pagina lee o escribe). No lo decide la jefatura del area en el momento: lo pide y lo deja la parametrizacion general, porque el dato es confidencial. `[28:10]`, `[28:21]`, `[28:27]`
* **Ver lo de los demas:** hoy los analistas del mismo rol pueden ver y corregir el trabajo del otro, y queda el registro de quien lo hizo. MJ lo da por bueno. `[31:31]`, `[31:49]`, `[33:36]`
* **Administradores por modulo:** se dejan de usar. El check del rol cubre el acceso. Carlos lo resume y la sala asiente. `[34:28]`, `[35:26]`, `[01:11:42]`, `[01:11:55]`
* **Jefatura = cadena de aprobacion**, no un rol administrador. Si falta la jefatura, se suple reemplazandola. `[32:29]`, `[32:57]`, `[33:09]`
* **Organigrama:** vista que se arma con el jefe marcado en el usuario. Titulos que pide Fran: gerencia general, gerencia de area, jefatura, analista. Es informativo. No arma la cadena ni el monto. `[01:13:24]`, `[01:14:54]`, `[01:17:18]`, `[01:17:21]`

## 2. Cadenas de aprobacion `[36:10 - 01:11:55]`

* **Los grupos se mantienen.** Carlos propuso quitarlos `[45:52]`. MJ lo corrige: cada area compra con un tope distinto (abastecimiento, comercial, COMEX, recursos humanos, contabilidad). El grupo es el area. Gerencia de area y gerencia general se repiten en cada grupo. `[52:59]`, `[53:18]`, `[53:29]`, `[53:37]`
* **Siempre pasa por la jefatura**, aunque el monto sea chico. Si supera el tope de esa jefatura, sigue a gerencia de area (Agustin) y despues a gerencia general (Nico). Tres niveles. No se salta a la jefatura. `[48:46]`, `[49:17]`, `[49:24]`, `[49:49]`, `[01:00:41]`
* **El ultimo eslabon tambien tiene tope.** Sirve para frenar un error de tipeo. Si la orden pasa ese tope, no entra a la cadena: se bloquea y se muestra que excede el monto de gerencia. Ejemplo de sala: tope de Nico en 400 millones; si fueran 4.000 hay que subir el tope a mano y mientras tanto no se aprueba. `[01:03:04]`, `[01:03:21]`, `[01:04:31]`, `[01:05:02]`
* **Misma cadena para CLP, USD y yuanes.** El tope se carga por moneda. Al tipear el monto en pesos, el sistema propone la conversion del dia (Banco Central) y deja editarla. Ese numero queda guardado; no se recalcula solo despues. `[01:05:10]`, `[01:06:27]`, `[01:08:14]`, `[01:08:27]`, `[01:09:09]`
* **Bugs vistos en el servidor de la demo:** no deja agregar un nivel despues del ultimo eslabon (en local si). Quien tiene rol administrador no aparece para armar la cadena (le paso a MJ). `[57:30]`, `[57:59]`, `[58:39]`
* **Para entrar al grupo** la persona necesita un rol con acceso al modulo. Eso MJ lo confirma. `[37:49]`, `[38:11]`

## 3. Insumos, orden de aplicacion, receta y packing `[04:19 - 05:25]` y `[01:33:23 - 02:16:06]`

* **Tres entradas al cierre de bodega**, pedido de Agustin via MJ: orden de aplicacion (agricola), receta (ALM / packing) e ingreso manual. Las tres centralizan bodega. `[04:19]`, `[04:25]`
* **Falta el Excel de recetas.** El manual quedo primero porque no habia archivo. Cuando manden el formato, la carga automatica convive con el tipeo. `[05:02]`, `[02:12:41]`
* **Orden de aplicacion:** la dosificacion por hectarea calcula la cantidad. Puede llevar mas de un insumo, cada uno con su unidad (no se suman litros con kilos). El centro de costo es de la orden (el cuartel), no de cada linea. Falta el elemento de costo; no cerraron si va en la orden o en la linea. Van a enviar una orden real. `[01:34:45]`, `[01:35:48]`, `[01:36:26]`, `[01:37:47]`, `[01:38:30]`, `[01:36:47]`
* **La orden de aplicacion pasa por la cadena de insumos.** `[01:39:14]`
* **Receta:** la crea la jefatura, sin cadena. El consumo si pasa por aprobacion. `[01:44:30]`, `[01:44:33]`, `[01:44:41]`
* **La receta no queda amarrada a un solo packing.** Queda al embalaje. En el consumo se indica cuanto uso cada packing de esa receta. El packing se muestra porque sirve saber quien consumio. `[02:13:10]`, `[02:13:19]`, `[02:13:39]`, `[02:14:15]`
* **Centro de costo en la receta**, no solo al consumir. Un centro puede tener muchas recetas. Filtro por centro en la lista. `[02:15:23]`, `[02:15:36]`, `[02:15:43]`, `[02:15:57]`
* **Precio del consumo:** precio promedio de lo que hay en bodega ese mes (stock anterior incluido). No se reescribe el mes ya consumido si al mes siguiente cambia el promedio. No se consume guia por guia ni de la mas antigua a la mas nueva. `[01:46:17]`, `[01:51:08]`, `[01:58:28]`, `[01:59:06]`, `[02:06:18]`
* **El promedio sale de cantidad y costo de lo recibido**, no de editar el precio a mano en el maestro. El maestro no deberia inventar el precio: lo mueven las guias. `[01:51:42]`, `[01:52:21]`, `[01:53:24]`
* **Cierre de bodega:** pidieron el listado de cuentas que faltan en el mapeo. En la sala se nombro merma. Esa palabra choca con la regla de negocio ya cerrada (merma no existe). No se agrega hasta que manden el detalle y se contraste. `[02:16:45]`, `[02:16:55]`

## 4. Guias, recepcion y devolucion `[01:59:22 - 02:11:25]`

* **Devolucion:** se busca la guia solo para traer el precio de llegada. No se descuenta el stock de esa guia. El documento de salida es nuevo. Puede devolverse aunque esas unidades ya se hayan consumido. Si se devuelve al precio promedio, la nota de credito del proveedor no calza. `[01:59:22]`, `[02:04:12]`, `[02:07:17]`, `[02:07:46]`, `[02:08:12]`
* **Recepcion:** al recibir se elige el articulo del maestro (codigo y nombre de la guia no alcanzan). El stock sube cuando se confirma la recepcion, no al solo registrar la guia. `[02:09:47]`, `[02:10:05]`, `[02:10:19]`
* **Adjunto:** fotos o documentos de como llego el packing, en la guia recibida. MJ acepta. `[02:10:29]`, `[02:10:50]`

## 5. Activo fijo `[02:17:22 - 02:27:09]`

* El grafico de depreciacion mensual, arriba del listado, queda bien. `[02:18:10]`
* **Todo nace en la orden de compra.** Tipo `activo fijo` en la OC. No se crea el maestro al elegir el tipo, ni antes de la orden, ni directo contra la factura. `[02:19:12]`, `[02:20:38]`, `[02:21:18]`, `[02:21:37]`, `[02:21:56]`
* **El maestro se crea cuando la OC esta recepcionada** (llego el producto). La factura puede llegar despues. El alta lista solo OC recepcionadas de ese tipo y avisa si todavia no tienen factura. Estados: recepcionado y facturado. `[02:23:21]`, `[02:24:31]`, `[02:24:45]`, `[02:25:04]`, `[02:25:19]`, `[02:25:48]`
* La factura se asocia en el libro de compras y ahi se ve el activo relacionado. `[02:26:01]`
* Al cierre de activos fijos viajan la cuenta al debe, la cuenta al haber y la depreciacion. No pidieron otro campo. `[02:18:26]`, `[02:19:11]`

## 6. Reversa de proforma y asientos `[05:53 - 06:39]` y `[02:31:38 - 02:40:19]`

* **No hay reapertura del mes.** La correccion se guarda en la linea. No queda un asiento de ajuste aparte ni un asiento de reversa nuevo. `[05:55]`, `[06:14]`, `[02:31:51]`, `[02:33:28]`, `[02:33:34]`
* Auditoria: quien, cuando, quien aprobo y como quedo. El reporte (libro mayor) muestra solo comprobantes activos. Lo anulado y lo pendiente no entran al reporte. La solicitud de reversa guarda lo que no debe verse en el reporte. `[06:39]`, `[02:32:13]`, `[02:32:20]`, `[02:38:06]`
* Si la proforma tenia factura, se desasocia, se corrige y se vuelve a asociar la factura que quedo liberada. `[02:33:06]`
* **Anular no borra la fila.** La jefatura anula con motivo. Otra persona puede solicitarlo y la jefatura lo aprueba, sin tope de monto y sin cadena de montos. Editar y anular son dos acciones. `[02:34:07]`, `[02:36:19]`, `[02:39:11]`, `[02:40:10]`, `[02:40:16]`, `[02:38:58]`
* El asiento manual sigue: ajustes y reclasificaciones que no nacen de un modulo. `[02:35:19]`, `[02:35:28]`

## 7. Lo que queda fuera de esta sala

* **CAF / emision:** en productivo GoSocket se acabaron los CAF. Carlos habla con Pablo. La proxima semana quieren recibir DTE en el libro de compras y cerrar al menos un modulo. Muestra el jueves siguiente. `[02:27:09]`, `[02:27:31]`, `[02:28:02]`
* **Reportes por modulo:** cuando el modulo funcione, reunion con la jefatura de ese departamento. MJ quiere ver que piden ellos, no solo lo que ella ve. `[02:28:02]`, `[02:28:37]`
* **Tesoreria:** Lupe y Agustin. Carlos confirma el lunes. Sigue pendiente el proyectado que Lupe pidio en comentarios. `[02:42:01]`, `[02:42:42]`, `[02:42:47]`
* **Proforma parcial:** una factura no tiene que cubrir la proforma completa. MJ dice que eso ya esta. El porcentaje que Carlos recordaba en la OC madre no quedo cerrado: ella lo recuerda por cantidad, no por un campo porcentaje. `[02:30:02]`, `[02:30:20]`, `[02:29:19]`

## 8. Compromisos

1. Sacar de la operacion el mantenedor de administradores por modulo. El acceso queda en el rol. Devint. `[01:11:42]`
2. Corregir en el servidor: agregar nivel despues del ultimo eslabon, y que un usuario administrador del modulo pueda entrar al grupo. Devint. `[57:59]`, `[58:39]`
3. Topes por moneda (CLP, USD, yuan) con propuesta del tipo de cambio del dia, editable y fija. Bloqueo con mensaje si la OC supera el ultimo tope. Devint. `[01:09:09]`, `[01:05:02]`
4. Receta por embalaje, consumo repartido por packing, centro de costo en la receta, precio promedio del mes al consumir. Devint. `[02:13:10]`, `[02:15:43]`, `[01:51:08]`
5. Devolucion al precio de la guia, sin mover el stock de esa guia. Stock de la guia recibida solo al confirmar la recepcion. Adjunto en la guia. Devint. `[02:07:46]`, `[02:10:19]`, `[02:10:50]`
6. Activo fijo solo desde OC tipo activo fijo ya recepcionada, con aviso si falta factura. Devint. `[02:24:45]`, `[02:25:19]`
7. Anular asiento (no borrar) con motivo, jefatura o solicitud a la jefatura. Libro mayor solo con activos. Devint. `[02:36:19]`, `[02:38:06]`
8. Cliente envia: Excel de recetas, orden de aplicacion real, listado de cuentas del cierre de bodega. `[05:02]`, `[01:36:47]`, `[02:16:55]`
9. Lunes: Carlos confirma el avance. Se coordina a Lupe para tesoreria. `[02:44:51]`, `[02:42:42]`

---

## Referencias

- Transcripcion: [`../transcripciones/transcripcion-2026-11-05-reunion.md`](../transcripciones/transcripcion-2026-11-05-reunion.md)
- Matriz de pisos entre dias: [`../../requerimientos/matriz-acuerdos-por-dia-2026-11-05.md`](../../requerimientos/matriz-acuerdos-por-dia-2026-11-05.md)
- Auditoria contra el sistema: [`../../requerimientos/auditoria-acuerdos-sistema-2026-11-05.md`](../../requerimientos/auditoria-acuerdos-sistema-2026-11-05.md)
