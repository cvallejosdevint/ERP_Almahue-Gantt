# Especificacion para desarrollo v2 - Presentacion cliente 14/10/2026

Correccion de `especificacion-desarrollo.md` (v1). La v1 sigue vigente en lo que este documento no corrige. Donde chocan, gana esta v2.

**Destinatario:** equipo de desarrollo.
**Fuente:** `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md`, mas el 01/10 y el 06/10 cuando el cliente ya habia cerrado el punto y esta sala no lo anulo.

## Por que existe esta version

La v1 uso esta regla: si la sala del 14/10 no lo dicto palabra por palabra, no se pide. Esa regla corto pedidos que ya estaban cerrados, o que se siguen de como el ERP ya recibe los documentos. El caso que lo mostro: las guias de despacho. Carlos dijo en la sala que el sistema ya las esta recibiendo, Maria Jesus dijo que la hija nace cuando le llega el documento con el despacho, y la v1 dejo el canal abierto. La pantalla pidio tipear una guia nueva.

Regla de esta v2:

- Si la factura recibida ya entra por GoSocket, la guia recibida usa el mismo cano.
- Un cierre dicho por el cliente en una sala anterior, que esta sala no anulo, sigue vigente.
- Lo que la sala dejo en "hay que validar", o lo que solo dijo el equipo, sigue fuera.

## REQ-V2-1. La guia recibida llega desde GoSocket

Origen: 14/10 [35:22], [37:50] a [37:56], [50:28], [51:21]. 06/10 con Pablo [02:51] a [04:58]. 01/10 [57:03] a [57:16].

- El libro de guias de Insumos / Bodega lista las guias de despacho que ya llegaron al inbox de GoSocket. El codigo SII es el 52.
- Folio, fecha, proveedor, neto y lineas salen del documento. El usuario no los tipea.
- La guia fisica es el control del jefe de abastecimiento: se contrasta con la digital. No reemplaza a la digital.
- Asociar es elegir la orden madre y la bodega de destino. Si el documento no trae bodega, esa es la unica captura.
- Sin madre no se asocia. Si no cabe en el saldo, o la madre esta cerrada, no se recepciona y no nace la hija.
- La guia que llego y todavia no tiene madre queda en el libro, pendiente.
- El libro de compras no crea una factura con la guia. El tipo 52 no es una linea del libro de compras.

**Aceptacion:** Traer de GoSocket deja en el libro solo documentos tipo 52, con los datos del XML. No hay alta de "nueva guia".

## REQ-V2-2. Ver PDF y ver XML, con descarga

Origen: el mismo gesto que el libro de compras ya tiene sobre la factura recibida. La sala pidio ver las guias recibidas [50:28]. El documento es el que llego, no un resumen armado a mano.

- En la fila hay dos acciones, como en los otros libros: **Ver PDF** y **Ver XML**.
- El clic en la fila no abre el documento.
- Cada vista trae la descarga: PDF en la del PDF, XML en la del XML.
- Si GoSocket aun no tiene el archivo, la pantalla lo dice.

**Aceptacion:** desde la guia se abre el PDF y, por otra accion, el XML. Ambos se pueden descargar.

## REQ-V2-3. La guia trae lineas y de esas lineas nace la hija

Origen: 14/10 [39:35], [37:21].

- Una guia es un documento con varias lineas, como la factura. No es un solo articulo y una sola cantidad.
- Cada linea se calza con un articulo del maestro y con una linea de la madre.
- La hija queda aprobada por el parcial de esas lineas. El precio que cuenta contra el saldo de la madre es el de la madre.
- El stock entra en la bodega elegida, una entrada por articulo.

**Aceptacion:** una guia con dos lineas que caben en la madre deja una sola hija, con esas dos lineas, y dos entradas de stock.

## REQ-V2-4. La hija nace aprobada. No abre otra cadena

Origen: 14/10 [37:50] y [53:15]. El 24/09 ya se habia dicho que la hija no recorre la cadena y que solo la edicion de la madre vuelve a aprobacion. Esta sala no lo anulo: Maria Jesus dijo que la madre se aprueba una vez y que la hija se aprueba con la guia.

- La madre la crea el jefe y esa es la que recorre la cadena.
- La hija la genera el administrativo al recepcionar la guia. Queda aprobada.
- Subir o bajar la madre si vuelve a la cadena. Eso no cambia.

**Aceptacion:** recepcionar una guia no deja la hija en pendiente de aprobacion.

## REQ-V2-5. El comprobante es peso y dolar, con el yuan al lado

Origen: 01/10 [32:41] a [33:23]. El cliente lo cerro ahi. El 14/10 Carlos recordo que ya estaba pedido [56:51] y nadie lo anulo. La v1 lo saco del alcance porque en esta sala no se volvio a dictar.

- La contabilidad es siempre peso y dolar, aunque el movimiento venga en otra moneda.
- Si el usuario no informa el tipo de cambio, se usa el del dia, el del Banco Central.
- El yuan se muestra en paralelo.

**Aceptacion:** un comprobante de un movimiento en otra moneda muestra peso, dolar y yuan, con el tipo de cambio del dia cuando no se ingreso uno.

## REQ-V2-6. Si el contratista no reclama, la proforma enviada queda aceptada

Origen: 06/10 [28:45] a [28:57]. Maria Jesus: ella envia la proforma y, si no le reclaman precios o trabajos, la da por aprobada para asociarla a la factura. Si hay diferencia, se revisa y se edita el ingreso. El 14/10 no lo anulo. La v1 lo dejo afuera porque no se repitio.

- La proforma aprobada por jefatura se envia al contratista.
- Si el contratista no reclama, esa proforma se puede asociar a la factura recibida.
- Si reclama precio o jornada, se edita el ingreso de origen y se vuelve a enviar. No se asocia mientras este en cuestion.

**Aceptacion:** una proforma enviada y no reclamada se puede vincular a la factura. Una proforma reclamada no se vincula hasta corregirla.

## Lo que la v1 dejo bien fuera, y sigue fuera

- Precio cero en el ingreso diario. En [59:15] quedo "hay que validar".
- La frase que sono a nota de credito. No se entiende y nadie la cerro.
- Una segunda modificacion de la madre pedida a contabilidad, dicha por una voz sin nombre.
- Guias emitidas en el libro de guias. Lo nombro Sergio. El cliente confirmo las recibidas.
- Numero de la hija con guion. Lo mostro Carlos. El cliente no lo dicto.
- Unir los dos botones de notificar. Lo propuso el equipo.
- Impedir que el administrador apruebe una orden. Lo nombro el equipo. Nadie lo pidio.
