# Digest cliente 2026-09-10 a 2026-10-01

Solo lo hablado en estas transcripciones. Sin minutas, sin codigo, sin otros markdown.

- `transcripcion-2026-09-10-demo-cliente.md`
- `transcripcion-2026-09-14-demo-avances.md`
- `transcripcion-2026-09-23-dudas-cliente.md`
- `transcripcion-2026-09-24-reunion-cliente.md`
- `transcripcion-2026-10-01-reunion-cliente.md`

Quien figura solo cuando el texto lo nombra o la pregunta va dirigida a esa persona y ella responde. Si no, `no dicho`.

## Facturacion

### FAC-01
- Enunciado: El sistema debe impedir anular una factura de exportacion a la que ya se le hizo una correccion de monto que bajo el total; solo cabe seguir con correccion de monto.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: no dicho (dialogo Carlos y Sergio, antes de que entre el cliente)
- Fuente: transcripcion-2026-09-10-demo-cliente.md [04:49]
- Cita: "ya bajaste un porcentaje" y "tienes que hacer solamente Correccion de monto"

### FAC-02
- Enunciado: El sistema debe emitir la factura de exportacion con el tipo de cambio del dia de la emision.
- Modulo: facturacion
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [17:19]
- Cita: "en la factura en si se ocupa el tipo de cambio del dia de la emision. Siempre."

### FAC-03
- Enunciado: El sistema debe hacer que la nota de credito y la nota de debito respeten el tipo de cambio de la fecha de emision de la factura de origen.
- Modulo: facturacion
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [17:29]
- Cita: "la nota de credito y debito tiene que respetar el mismo tipo de cambio de la fecha de emision, de la factura"

### FAC-04
- Enunciado: El sistema debe traer el tipo de cambio de la factura al armar la nota de credito o debito, y no pedir que se ingrese a mano como unico camino.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [16:43]
- Cita: "una nota de credito debito que haga referencia a esa facturacion, el tipo de cambio se va a llamar de la factura"

### FAC-05
- Enunciado: El sistema debe, en la correccion de monto, mostrar el tipo de cambio de la factura y dejarlo editable; en la anulacion completa solo copia el documento.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [25:12]
- Cita: "en la corrige monto yo dejaria que diera la opcion de poder modificar el tipo de cambio"

### FAC-06
- Enunciado: El sistema debe usar un solo tipo de cambio para toda la factura, no uno por item.
- Modulo: facturacion
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [26:13]
- Cita: "siempre un tipo de cambio para toda la factura"

### FAC-07
- Enunciado: El sistema debe ofrecer en la factura de exportacion pais de destino, pais receptor, clausulas, tipo de cambio y moneda, con yen, euro y dolar.
- Modulo: facturacion
- Clase: pedido
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [16:09]
- Cita: "aqui esta el yen, tambien tenemos el euro y el dolar como se habia solicitado"

### FAC-08
- Enunciado: El sistema debe limitar el selector de monedas de la facturacion a las monedas incluidas en la parametrizacion.
- Modulo: facturacion
- Clase: pedido
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [16:21]
- Cita: "tendrian que irse ligados a los que se ingresan en la parametrizacion"

### FAC-09
- Enunciado: El sistema debe tomar los codigos de comercio exterior desde aduana y el Servicio de Impuestos Internos.
- Modulo: facturacion
- Clase: integracion
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [16:26]
- Cita: "codigos que se estan recopilando directamente de la pagina de aduanas con el servicio impuesto interno"

### FAC-10
- Enunciado: El sistema debe tratar como obligatorios los campos que el manual de facturacion marca como obligatorios.
- Modulo: facturacion
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [34:10]
- Cita: "lo obligatorio son los que estan en el manual de facturacion"

### FAC-11
- Enunciado: El sistema debe filtrar los puertos de embarque o desembarque segun el pais elegido.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [36:40]
- Cita: "si yo pongo China solamente me van a salir los de China"

### FAC-12
- Enunciado: El sistema debe poder cargar puertos que el cliente usa y que no estan en la base de aduana, por ejemplo Shenzhen.
- Modulo: facturacion
- Clase: duda
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [36:34]
- Cita: "le sacamos alto a Shenzhen y no estaba Shenzhen" y "podemos cambiar la base de datos"

### FAC-13
- Enunciado: El sistema debe pedir la via de transporte maritimo o aereo en la factura de exportacion.
- Modulo: facturacion
- Clase: ui
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [37:40]
- Cita: "Y donde va el 100 maritimo aereo" y luego "maritimo aereo, si, eso es muy precioso"

### FAC-14
- Enunciado: El sistema debe mostrar, al avanzar de pestana en la emision, un resumen con el cliente ya elegido para no perder el receptor.
- Modulo: facturacion
- Clase: ui
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [35:56]
- Cita: "en el calculo total, ahi podria ir cliente, para que nosotros veamos en que cliente lo estamos facturando"

### FAC-15
- Enunciado: El sistema debe convertir el monto de exportacion a pesos con el tipo de cambio.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [33:34]
- Cita: "entonces me va a convertir a peso automaticamente con el tipo de cambio al Banco Central"

### FAC-16
- Enunciado: El sistema debe tomar el tipo de cambio que la persona ingresa en la ficha de emision, no solo el automatico.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [33:44]
- Cita: "el tipo de cambio yo lo voy a dar cuando ponga la ficha de emision"

### FAC-17
- Enunciado: El sistema debe dejar la orden de venta confirmada y sin facturar, y facturarla despues en la emision del DTE, con opcion de editar antes de confirmar.
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [39:13]
- Cita: "esta confirmada mas no facturada y para facturarla hay que ir a la emision de DTE"

### FAC-18
- Enunciado: El sistema debe contabilizar la venta desde el libro, con cuenta y centro de costo, sin volver a digitar los datos del documento.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [40:13]
- Cita: "nosotros mismo apretamos la cuenta y se contabiliza Y no hay que ingresar los datos de nuevo"

### FAC-19
- Enunciado: El sistema debe enviar correos distintos desde la casilla de contabilidad: aviso interno de aprobacion, y aviso al cliente con la factura o el XML y el monto total.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [53:41]
- Cita: "diferentes correos, uno van a ser de notificaciones y otro van a ser de notificar la venta" y "juntar la factura o el XML y el monto total"

### FAC-20
- Enunciado: El sistema debe salir con el correo de contabilidad que la empresa ya tiene, contabilidad.maworks.com.
- Modulo: facturacion
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [55:46]
- Cita: "Contabilidad es un correo es contabilidad.maworks.com" y "Vamos a usar ese"

### FAC-21
- Enunciado: El sistema no puede regenerar por la integracion un PDF de GoSocket ya emitido si despues cambia el formato o el logo; eso se hace en el portal.
- Modulo: facturacion
- Clase: integracion
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [55:49]
- Cita: "no existe la opcion de que la API de GoSocket la descargue con la nueva visualizacion si el documento ya fue generado"

## Ventas

### VEN-01
- Enunciado: El sistema debe impedir, en la venta nacional, un precio menor al monto cargado en bodega, y debe ser mayor o igual a ese monto.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [28:33]
- Cita: "lo ideal seria que no fuera menor al monto que esta en bodega"

### VEN-02
- Enunciado: El sistema debe mostrar en la venta nacional el monto que esta en bodega, para aplicar esa restriccion.
- Modulo: ventas
- Clase: ui
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [28:48]
- Cita: "Seria bueno que lo muestre aca tambien" y la respuesta "Si, seria bueno"

### VEN-03
- Enunciado: El sistema debe dejar libre el monto de la venta de exportacion, sin la restriccion de precio de bodega.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [24:10]
- Cita: "en la exportacion, o sea, uno puede poner el monto que uno calcule"

### VEN-04
- Enunciado: El sistema debe contemplar que Almahue vende primero y a fin de mes LM le factura las cajas vendidas, con el stock en cero el ultimo dia.
- Modulo: ventas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [24:28]
- Cita: "almagüe vende y a fin de mes lm le hace la factura por las cajas que vendio" y "stock cero"

### VEN-05
- Enunciado: El sistema debe alimentar la venta de ALM desde la bodega y dejar la venta de Almahue mas flexible porque no tiene bodega.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-10-demo-cliente.md [46:44]
- Cita: "el de ALM se va a alimentar de la bodega, pero el de Almago no tiene bodega"

### VEN-06
- Enunciado: El sistema debe usar centros de costo parametrizados con codigo, por ejemplo cereza y nectarin, y no un texto libre inventado al contabilizar.
- Modulo: ventas
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [40:46]
- Cita: "001 cereza, 002 nectarin" y "hay que subir una base que todo este parametrizado"

### VEN-07
- Enunciado: El sistema debe permitir adjuntar N documentos de respaldo tambien en ventas, no solo un numero de referencia.
- Modulo: ventas
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [12:18]
- Cita: "entonces ahi deberia aplicar para ambos flujos" e "incorporar o adjuntar documentos"

## Inventario

### INV-01
- Enunciado: El sistema debe guardar un precio promedio de bodega solo como dato informativo.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [30:42]
- Cita: "para temas informativos, tuvieramos un precio promedio en bodega"

### INV-02
- Enunciado: El sistema debe valorizar el movimiento de stock con el precio de la orden de compra con la que entro a bodega, no con el promedio.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [30:49]
- Cita: "cuando hacemos cualquier movimiento, considerando como el stock, que tomara el precio de la orden de compra"

### INV-03
- Enunciado: El sistema debe, en una nota de credito o devolucion a proveedor que referencia una factura, dejar poner el precio de esa factura y no forzar el promedio de bodega.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [29:32]
- Cita: "devolucion a proveedor y no nos deja tomar el precio de la factura, sino que nos hace tomar el precio promedio"

### INV-04
- Enunciado: El sistema debe contemplar una orden de compra anticipada por el total, por ejemplo mil unidades, de la que salen varias facturas parciales.
- Modulo: inventario
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [29:10]
- Cita: "orden de compra anticipada" y "cada 100 unidades nos van emitiendo una factura" de "la misma orden de compra de mil unidades"

### INV-05
- Enunciado: El sistema debe ingresar todo insumo con guia; el resto de las compras entra con factura directa.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [55:22]
- Cita: "todo lo que es insumo se ingresa si o si con guia" y "Lo demas aplica todo factura directa"

### INV-06
- Enunciado: El sistema debe usar la guia solo para entrar el material a bodega, y asociar a la orden de compra la factura que llega a fin de mes.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [55:55]
- Cita: "la OCE madre dice 100 cajas, pero semanalmente nos entregan 10" y "a final de mes nos emiten las facturas por las 40"

### INV-07
- Enunciado: El sistema debe recepcionar el material de insumos con la guia fisica que controla el jefe de abastecimiento, no con un flujo de recepcion electronica de guias.
- Modulo: inventario
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [57:10]
- Cita: "Acá las piden fisica, es como un control que hace el jefe de abastecimiento"

### INV-08
- Enunciado: El sistema debe dejar en duda si las guias de despacho (codigo 52) llegan como documentos recibidos en GoSocket, porque en el RCV del SII no aparecen.
- Modulo: inventario
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [57:35]
- Cita: "en el RCB del SI no aparecen las guias" y "en GOSECAD deberian aparecer con el codigo 52"

### INV-09
- Enunciado: El sistema debe permitir devolucion de material a proveedor solo en ALM, cuando se rechaza la factura y hay que sacar el insumo de bodega.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [59:38]
- Cita: "se rechaza la factura y tengan que devolver material" y "eso solamente contaria con lo que es ALM"

### INV-10
- Enunciado: El sistema debe contemplar que en Almahue no hay reintegro de insumos porque es fruta y compran lo justo que venden.
- Modulo: inventario
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [01:00:10]
- Cita: "en Almagüe no hay reintegro porque es fruta" y "compramos lo justo que vendemos"

### INV-11
- Enunciado: El sistema debe dejar la orden de compra madre solo como dato informativo de insumos, sin reflejarla en los demas modulos.
- Modulo: inventario
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [47:20]
- Cita: "la orden de compra madre en realidad sea solamente un dato informativo" y "ningun modulo que no sea de insumos"

## Compras

### COM-01
- Enunciado: El sistema debe traer los documentos recibidos desde GoSocket y trabajarlos en tres estados del SII: pendiente, aceptado y reclamado.
- Modulo: compras
- Clase: integracion
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-14-demo-avances.md [22:06]
- Cita: "los tres estados que actualmente trabaja el servicio puesto interno" y Mario: "yo creo que esta perfecto"

### COM-02
- Enunciado: El sistema debe permitir aceptar y reclamar el documento recibido dentro del ERP, sin entrar al portal del SII.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-14-demo-avances.md [22:48]
- Cita: "si lo integramos en el ARP no va a ser necesario que N usuarios se esten conectando al servicio puesto interno"

### COM-03
- Enunciado: El sistema debe aceptar que llegue una factura referida a una orden de compra que aun esta pendiente de aprobacion, y no rechazarla por eso.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [24:00]
- Cita: "En teoria no, en la practica si" y "no podemos dejar como algo tan rigido"

### COM-04
- Enunciado: El sistema debe destacar la factura que referencia una orden de compra no aprobada, y tambien la que llega sin orden de compra.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [25:01]
- Cita: "que se destaquen los documentos recibidos que esten referenciando una orden de compra que no este aceptada"

### COM-05
- Enunciado: El sistema debe contemplar que la mayoria de las facturas llega sin orden de compra y queda pendiente hasta que esa orden se emita.
- Modulo: compras
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [25:15]
- Cita: "El 90% de las facturas Que llega sin orden de compra"

### COM-06
- Enunciado: El sistema debe dejar la factura sin reclamo en plazo y, vencido ese plazo, pasarla como aceptada.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [26:10]
- Cita: "va a quedar en pendiente hasta los 8 dias ya despues si no se rechaza va a pasar automatico como aprobado"

### COM-07
- Enunciado: El sistema debe avisar, sin rechazar solo, cuando un RUT marcado emite un documento, para poder reclamar a tiempo.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [28:09]
- Cita: "no necesitamos que automaticamente se rechacen, sino que se emite una alerta de que se metio el documento"

### COM-08
- Enunciado: El sistema debe permitir alertas especiales por proveedor, por un tiempo, a varios usuarios, en la campana y por correo, distintas de las alertas del flujo normal.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [30:17]
- Cita: "Alerta especial" "parametrizable en el minuto" "es el tiempo que dure y despues lo eliminais"

### COM-09
- Enunciado: El sistema no debe armar una lista negra que rechace sola al proveedor objetado; el caso puede ser transitorio.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [35:36]
- Cita: "entonces nos va la lista negra" tras explicar que el objetado del SII puede regularizarse

### COM-10
- Enunciado: El sistema debe tratar la factura al contado como ya pagada y pasarla directo al libro, porque no se reclama igual que una a credito.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [32:00]
- Cita: "las que estan al contado pasan directo al libro" y "estan pagados al contado"

### COM-11
- Enunciado: El sistema debe, si la factura llega sin fecha de vencimiento, proponer la condicion de pago del maestro del proveedor.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [12:01]
- Cita: "yo diria tomarse lo que dijimos ayer del proveedor" y "sus condiciones de pago"

### COM-12
- Enunciado: El sistema debe dejar en el proveedor plazos de 30, 60 o 90 dias, editables al armar la orden de compra, y heredarlos a la factura asociada.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [12:31]
- Cita: "puede ser a 30, 60, 90 dias" y "cuando el usuario esta haciendo la orden de compra, lo puede editar"

### COM-13
- Enunciado: El sistema debe alertar a contabilidad si la factura no calza con un proveedor del maestro, y no dejarle movimiento hasta registrarlo.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [13:42]
- Cita: "le va a salir la alerta en este caso a la LUPE, a Contabilidad" y "sin poder hacer movimiento hasta que se registre el proveedor"

### COM-14
- Enunciado: El sistema no debe rechazar de inmediato la factura de un proveedor aun no registrado: hay unos dias para regularizar porque pudo no existir orden de compra.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [14:50]
- Cita: "si tenemos siete dias para hacer el movimiento"

### COM-15
- Enunciado: El sistema debe nacer la orden de compra por digitacion, con la cotizacion o el presupuesto como adjunto, y no generarla sola desde una proforma.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [15:57]
- Cita: "no nace asi como sistematicamente de ahi, al final nace de la digitacion directa de la orden de compra"

### COM-16
- Enunciado: El sistema debe dejar ver, al pagar, la cotizacion, la orden de compra y la factura, con montos y monedas.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [16:55]
- Cita: "esta es la cotizacion, esta es la orden de compra, esta es la factura" y "se registra en todas las monedas"

### COM-17
- Enunciado: El sistema debe exigir cuenta contable y centro de costo en cada linea de la orden de compra, y contabilizar la factura recibida con esos datos.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [25:22]
- Cita: "cada linea de detalle de la orden de compra va a tener una cuenta contable y un centro de costo"

### COM-18
- Enunciado: El sistema no debe contabilizar una factura recibida hasta asociarla a una orden de compra o a una proforma.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [25:36]
- Cita: "las recibidas no se van a poder contabilizar hasta asociar una orden de compra o una proforma"

### COM-19
- Enunciado: El sistema debe tratar la orden de compra grande como madre de control, sin contabilizarla, y contabilizar las hijas que calzan con cada factura parcial.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [28:50]
- Cita: "quien contabiliza? La hija" y "la madre no va a contabilizar nada. Es solamente el control"

### COM-20
- Enunciado: El sistema debe heredar a la hija cabecera, cuenta y centro de costo de la linea de la madre que se esta recepcionando.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [29:31]
- Cita: "de la madre se deberia heredar" y "respeta el centro de costo y la cuenta contable segun la linea"

### COM-21
- Enunciado: El sistema debe, si la factura parcial repite una linea ya consumida, alertar o rechazar ese calce; si cae en otra linea pendiente, completar la madre.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [30:32]
- Cita: "si la factura 2 llega de nuevo por la linea 1, ahi no va a ser macho. Va a tener la alerta o la va a rechazar"

### COM-22
- Enunciado: El sistema no puede calzar solo, por codigo de producto del XML, que linea de la madre corresponde a una factura parcial, porque el proveedor usa otros codigos.
- Modulo: compras
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [30:54]
- Cita: "en el formato de QML, cada proveedor trabaja con codigos de productos totalmente distintos"

### COM-23
- Enunciado: El sistema debe, si la ultima factura trae mas cantidad o mas monto que la madre, dejarla pendiente y obligar a editar la madre, con nueva aprobacion si el monto cambia de tramo.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [36:20]
- Cita: "Va a tener que adelantar la solicitud y que al final se modifique la orden de compra" y "si aumenta, deberia pasar por el flujo de aprobaciones"

### COM-24
- Enunciado: El sistema debe apurar ese descuadre dentro del plazo de aceptacion; si no alcanza, rechazar la factura y pedir que la refacturen.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [37:48]
- Cita: "Si el proceso iba a ser un poco mas largo de siete dias, lo mejor seria que la rechacen y pidan que refacturen"

### COM-25
- Enunciado: El sistema debe marcar en rojo la factura cuyo monto no cuadra con la orden de compra.
- Modulo: compras
- Clase: ui
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [38:18]
- Cita: "el ERP va a estar ahi con la mansaleta en rojo que hay una factura que no cuadra con la orden de compra"

### COM-26
- Enunciado: El sistema debe avisar si la factura llega sin referencia de orden de compra y dejar asignarla a mano.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [38:34]
- Cita: "notificacion cuando la factura viene sin referencia de orden de compra" y "queda la opcion de asignar manualmente"

### COM-27
- Enunciado: El sistema debe listar, al asignar, solo ordenes de compra abiertas de ese proveedor y aun no asociadas a una factura.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [39:21]
- Cita: "te va a listar solamente la orden de compra de ese proveedor, pero que esten pendientes de asignacion"

### COM-28
- Enunciado: El sistema debe distinguir dos alertas: no existe orden de compra del proveedor, o existe y no venia referenciada.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [40:17]
- Cita: "la factura llego y ni siquiera existe orden de compra" o "hay una orden de compra, no viene referenciada"

### COM-29
- Enunciado: El sistema no debe crear la orden de compra desde el libro de compras; contabilidad avisa a la persona que pidio el servicio para que ella la genere.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [41:41]
- Cita: "me comunicaria con la persona encargada y el tiene que volver a hacer la orden de compra"

### COM-30
- Enunciado: El sistema debe dejar elegir al usuario destino, mandarle correo y notificacion, abrir el generador con el RUT, y guardar quien fue avisado y cuando.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [44:08]
- Cita: "Lupe va a tener que decir a esto le tengo que notificar al Mario" y "Se notifico a Mario en la fecha tanto"

### COM-31
- Enunciado: El sistema debe guardar en el maestro del proveedor rubro, representante, cuenta bancaria, contacto y correo, mas condicion de neto, moneda, dias de pago y condicion de IVA.
- Modulo: compras
- Clase: dato
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [02:41]
- Cita: "rubro representante de la cuenta bancaria el contacto mail" y "la condicion del neto la moneda y los dias de pago la condicion del iva"

### COM-32
- Enunciado: El sistema debe, para decidir la cadena de una orden en dolares, bajar el tipo de cambio del dia, pasar el monto a pesos y comparar en pesos.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [03:50]
- Cita: "cuando la oc sea en dolares" "bajar el tipo cambio del dia y transfiere ese monto en pesos"

### COM-33
- Enunciado: El sistema debe aprobar solo si el monto es bajo un limite, pasar por jefatura en el tramo medio, y por jefatura y gerencia si es mayor.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [04:24]
- Cita: "si el monto es menor a x monto pasa una version automatica" "entre x y pasa por aprobacion de jefatura" "si no es mayor" "jefatura, gerencia"

### COM-34
- Enunciado: El sistema debe, si rechazan la orden, devolverla al mismo documento para corregirla y recorrer de nuevo toda la cadena, sin saltar pasos.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [05:00]
- Cita: "le vuelve al usuario" y "tiene que volver a cumplir Todo el paso de nuevo" y "el mismo ID nomas se edita"

### COM-35
- Enunciado: El sistema debe, si al corregir el monto la orden cae en un tramo menor, seguir el flujo de ese tramo nuevo y no obligar de nuevo al gerente.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [06:00]
- Cita: "se genera la orden de compra por un monto menor" "el flujo normal no, en ese caso"

### COM-36
- Enunciado: El sistema debe guardar el historial de la orden y el motivo del rechazo.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [06:39]
- Cita: "tracking a las ordenes de compras para ver el historial y tener la informacion tambien del por que fue rechazada"

### COM-37
- Enunciado: El sistema debe permitir cargar a mano una factura recibida, con su PDF, cuando el XML no llega a GoSocket, sin exigir una segunda sincronizacion.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [09:08]
- Cita: "a veces puede llegar en PDF pero el XML a veces no llega" y "ya se la subo y ya esta"

### COM-38
- Enunciado: El sistema debe dejar adjuntar varios respaldos a la compra, como cotizacion, presupuesto o contrato, porque tesoreria los necesita aunque contabilidad no los use.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [11:49]
- Cita: "en tesoreria es importante que este el documento asociado a la cotizacion al presupuesto"

### COM-39
- Enunciado: El sistema debe dejar la recepcion en pendiente si la cantidad es menor al saldo, si monto o cantidad no coinciden, o si el tipo de cambio no cuadra.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [13:51]
- Cita: "si la cantidad es menor al saldo de la OC queda pendiente" y "tipo cambio cuadra no pasa en estado pendiente"

### COM-40
- Enunciado: El sistema debe, en una factura parcial, abrir las lineas de la madre y dejar digitar solo las cantidades recepcionadas de cada item.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Fran
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [26:36]
- Cita: "la factura me llego por 20 cajas y 10 bolsas" y "solo las cantidades, por linea"

### COM-41
- Enunciado: El sistema debe mostrar en la siguiente recepcion el saldo de la madre menos lo ya recepcionado en las hijas.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [28:03]
- Cita: "no tiene que levantar la cantidad total de la madre, sino la cantidad total menos la orden de compra de hijos"

### COM-42
- Enunciado: El sistema no debe mandar la orden hija por la cadena de aprobacion; solo la madre vuelve a aprobacion si hay que subirla o achicarla para cerrar.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [29:03]
- Cita: "la hija no" "solamente pasa cuando es sobre el valor de la orden de compra"

### COM-43
- Enunciado: El sistema debe, si la madre queda corta y no vendra mas factura, pedir aprobacion para achicarla y dejarla saldada.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [22:10]
- Cita: "si quedo corto y nunca va a llegar una factura hay que cerrarla" y "se achica la OC y queda tambien saldada"

### COM-44
- Enunciado: El sistema debe registrar la compra en pesos, dolares y yuan, y forzar el tipo de cambio de la moneda de la orden para que el registro calce con ella.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [22:33]
- Cita: "tabla de registro en pesos dolares y yuan" y "para calzar los dolares" "un tipo de cambio como muy flexible"

### COM-45
- Enunciado: El sistema debe proponer el tipo de cambio que hace calzar la factura en pesos con los dolares o yuanes de la orden.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [24:31]
- Cita: "lo puede calcular, cosa que calce con los C" y "surgiera el tipo de cambio ideal"

### COM-46
- Enunciado: El sistema debe manejar estos estados de la orden: pendiente de aprobacion, aprobada, recepcion pendiente o recepcionada, factura pendiente, pendiente de pago y pagada.
- Modulo: compras
- Clase: dato
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [30:42]
- Cita: "OCDE pendiente de aprobacion, la OCDE aprobada recepcionada o recepcion pendiente, factura pendiente, pendiente de pago y pagada"

### COM-47
- Enunciado: El sistema debe guardar una base auxiliar de la compra con fechas, numeros, proveedor, item, neto, IVA, moneda de pago y el registro en peso, yuan y dolar.
- Modulo: compras
- Clase: dato
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [31:33]
- Cita: "fechas de creacion los numeros de UC la fecha de documento" "Neto, oliva, la moneda de pago" "Peso, yuan y dolares"

### COM-48
- Enunciado: El sistema debe contemplar proveedor extranjero y factura cargada a mano con monto y tipo de cambio, como reglas del flujo de compra que Mario dejo anotadas.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [32:05]
- Cita: "Asignacion manual Rechazo de factura Proveedor extranjero" "factura cargada manualmente con monto tipo de cambio"

### COM-49
- Enunciado: El sistema debe ofrecer plazos de 30, 60 y 90 dias y tambien un ingreso manual de dias, heredado a la generacion y a la recepcion.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [36:06]
- Cita: "La opcion de 30, 60, 90 y la opcion ingresar manual"

### COM-50
- Enunciado: El sistema debe expresar la condicion de pago en dias de credito que dice la factura, no en una fecha de calendario.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [43:46]
- Cita: "la factura te dice que por cuantos dias es el credito, por 30, 60, 80"

### COM-51
- Enunciado: El sistema debe separar la condicion de pago del neto y la del IVA: en materiales el IVA se paga al mes siguiente y el neto puede ir a 60 dias; a 30 dias se paga la factura completa.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [43:59]
- Cita: "se paga el IVA primero y esa puede tener el neto a 60 dias" y "en una 30 dias se le paga la factura total"

### COM-52
- Enunciado: El sistema debe autocompletar las condiciones desde el proveedor y dejar editarlas en casos especiales.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [43:10]
- Cita: "se podria auto-rellenar" "lo puede cambiar, pero que se le recomiende cual es su condicion"

### COM-53
- Enunciado: El sistema debe definir la cadena de aprobacion por usuario y por grupo, no por rol; el rol solo abre el menu.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [40:45]
- Cita: "La regla de aprobacion es por rol o por usuarios? Es por usuarios"

### COM-54
- Enunciado: El sistema debe pedir PIN para aprobar y un motivo para rechazar la orden de compra.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [51:21]
- Cita: "las aprobaciones como se habian solicitado van con pin" y "el rechazo, pide el motivo"

### COM-55
- Enunciado: El sistema debe, si sube el monto de una orden ya hecha, volver a pasarla por la linea de aprobacion.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [47:52]
- Cita: "hay una modificacion en la orden de compra" "el monto aumenta" "pasar de nuevo tambien por la linea de aprobacion" y la respuesta "Si"

### COM-56
- Enunciado: El sistema debe avisar en el libro de compras si el documento no trae orden vinculada, y dejar asociarla o notificar a quien debe crearla.
- Modulo: compras
- Clase: ui
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [46:01]
- Cita: "ahi nosotros tendriamos que notificar a la persona que deberia crear la orden de compra"

## Contratistas

### CTR-01
- Enunciado: El sistema debe parametrizar labores, actividades, su asociacion, unidades de control y tipos de contrato antes del ingreso diario.
- Modulo: contratistas
- Clase: dato
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [17:56]
- Cita: "la carga de las labores, las actividades, y las asociaciones" "unidades de control y los tipos de contrato"

### CTR-02
- Enunciado: El sistema debe registrar en el ingreso diario lo que se le tiene que pagar al contratista por las labores hechas.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [18:31]
- Cita: "en ingreso diario seria como lo que se le tiene que pagar al contratista" y la respuesta "Si, si es asi"

### CTR-03
- Enunciado: El sistema debe tomar el precio de la labor ya definido, y no dejarlo como digitacion libre; ese valor lo da don Pablo.
- Modulo: contratistas
- Clase: duda
- Voz: no-claro
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [20:14]
- Cita: "el precio yo creo que viene definido por la labor" y "ese valor lo da don Pablo"

### CTR-04
- Enunciado: El sistema debe armar la proforma del contratista con los ingresos diarios que siguen pendientes de asignar.
- Modulo: contratistas
- Clase: ui
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [19:07]
- Cita: "los ingresos pendientes son los ingresos diarios que estan pendientes de asignacion"

### CTR-05
- Enunciado: El sistema debe, en contratistas, tratar la proforma como la orden de compra: el contratista factura referenciandola y ahi se contabiliza.
- Modulo: contratistas
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [21:43]
- Cita: "la proforma es en este modulo, es como la orden de compra" y "Referenciando la proforma"

### CTR-06
- Enunciado: El sistema debe poder asociar en el libro de compras tanto ordenes de compra como proformas, segun el modulo.
- Modulo: contratistas
- Clase: pedido
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [22:38]
- Cita: "en el libro de compras podrian ustedes asociar ordenes de compra y proforma" y la respuesta "Si. Segun el modulo"

### CTR-07
- Enunciado: El sistema debe dejar en espera el cruce de la proforma de contratistas hasta que el cliente revise el flujo por dentro.
- Modulo: contratistas
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [22:48]
- Cita: "en el caso del modulo contratista, no alcanzamos a revisarlo ayer" y "aguantenme un poco como contratista"

### CTR-08
- Enunciado: El sistema debe seguir sin confirmacion de si la proforma se convierte en orden de compra.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [54:12]
- Cita: "tenemos algunas dudas con la proforma si la proforma se ha convertido en orden de compra o no"

### CTR-09
- Enunciado: El sistema debe contemplar que el modulo de contratistas tambien lo usa el area agricola y puede pedir mas detalle que ALM y Almahue.
- Modulo: contratistas
- Clase: duda
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [01:02:55]
- Cita: "el modulo de contratista se ocupa harto tambien por el area agricola y ahi puede necesitar un poco mas de detalle"

## Tesoreria

### TES-01
- Enunciado: El sistema debe cargar la cartola con codigo financiero para el flujo de caja, y no armar ese asiento como banco contra cuenta por pagar.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [36:36]
- Cita: "el asiento de la cartola" "lo que lleva es codigo financiero" "Para el flujo caja, nada mas"

### TES-02
- Enunciado: El sistema debe detallar la contrapartida del movimiento de banco como proveedor, cliente o cuenta de gasto.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [36:56]
- Cita: "el movimiento del banco Va con un codigo financiero Pero la contrapuenta" "si va con detalle" "proveedor, cliente O cuenta de gasto"

### TES-03
- Enunciado: El sistema debe leer el Excel de cartola por pestana de empresa, banco y moneda, y dejar corregir a mano si el nombre de la pestana cambia.
- Modulo: tesoreria
- Clase: dato
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [42:21]
- Cita: "cada uno de los tabs del Excel corresponde a una de las empresas" y "seleccionar el banco y la moneda"

### TES-04
- Enunciado: El sistema debe cargar la cartola en la empresa en la que el usuario esta conectado.
- Modulo: tesoreria
- Clase: regla
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [44:08]
- Cita: "lo que siempre predomina es la empresa en la que estamos actualmente"

### TES-05
- Enunciado: El sistema no debe integrar el banco en linea en la primera puesta en marcha; la cartola sigue por carga y la automatizacion queda para despues.
- Modulo: tesoreria
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-14-demo-avances.md [50:33]
- Cita: "yo prefiero que sigamos asi en primera instancia" y "en el ACRI del proximo ano vamos y lo automatizamos"

### TES-06
- Enunciado: El sistema debe dejar elegir un rango de fechas al cargar la cartola, para subirla por semana o por dia e incluir movimientos con fecha de feriado o de viernes que caen el lunes.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [49:11]
- Cita: "la opcion de seleccionar el dia desde hasta" y "Si, podria, para poder subirla semanal"

### TES-07
- Enunciado: El sistema no debe volver a leer el saldo inicial del mes anterior si ese saldo ya quedo cargado en la cartola previa.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [48:41]
- Cita: "si en la cartola siguiente ya va a tener el saldo inicial de ese pasado, entonces no deberia leerlo"

### TES-08
- Enunciado: El sistema debe contabilizar los egresos contra la nomina de pago, no linea por linea contra la cartola.
- Modulo: tesoreria
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-14-demo-avances.md [57:45]
- Cita: "Contabilizar con la nomina, no con la cartola" y "la nomina ya tiene todos los documentos Que pagaste"

### TES-09
- Enunciado: El sistema debe exigir que los egresos seleccionados calcen a la perfeccion con el monto de la nomina.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [01:02:42]
- Cita: "Seleccionar todos esos egresos y asociarlos a una nomina" y "esa seleccion tiene que calzar" "a la perfeccion"

### TES-10
- Enunciado: El sistema debe dejar los ingresos de clientes para conciliar de a uno, porque no viajan en la nomina de egresos.
- Modulo: tesoreria
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [01:01:57]
- Cita: "los ingresos Hay un problema Yo creo que va a tener que ser uno a uno"

### TES-11
- Enunciado: El sistema podria tener una nomina de ingresos, aparte de la carga de cartola, pero eso quedo como prueba y no como regla cerrada.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [01:04:38]
- Cita: "una nomina de ingresos" y "tenemos que hacer una prueba"

### TES-12
- Enunciado: El sistema debe proponer, al conciliar, un calce por RUT y monto, y otro solo por RUT cuando el monto no es exacto o es parcial.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [53:20]
- Cita: "el match perfecto" "coincide el root del proveedor y el monto" y "el match imperfecto" "solamente con el root"

### TES-13
- Enunciado: El sistema debe mostrar el flujo de caja como total gastado o consumido por codigo financiero, sumando bancos y monedas, y entregar el informe en pesos.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-14-demo-avances.md [01:08:46]
- Cita: "en el flujo de caja solamente nos interesa saber cuanto fue lo que se gasto" y "es el totalizado"

### TES-14
- Enunciado: El sistema debe mostrar en cartolas, en otra vista, cuanto hay en cada banco y en cada moneda de ese banco.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-14-demo-avances.md [01:13:21]
- Cita: "en cartolas podrian haber unos indicadores que digan cuanto saldo por los bancos" y "ahi manda el banco y la moneda"

### TES-15
- Enunciado: El sistema debe dejar asociar egresos de la cartola a la semana de la nomina, en masa o de a uno, con contracuenta, codigo financiero y destino.
- Modulo: tesoreria
- Clase: ui
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [50:11]
- Cita: "para asignar la nomina semanal. Te queda comodo asi" y "Si, si se queda comoda"

### TES-16
- Enunciado: El sistema debe dejar abierto si la contracuenta, el codigo financiero y el destino masivos sirven solo para la nomina o tambien para otros egresos.
- Modulo: tesoreria
- Clase: duda
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [49:36]
- Cita: "desconozco si en algun caso se dara de que varias de las cuentas vayan tambien a la misma contracuenta" y "Lo voy a pensar"

### TES-17
- Enunciado: El sistema debe mostrar los pendientes de nomina de todas las semanas hasta la semana en curso, porque se revisa hacia adelante.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [51:25]
- Cita: "ver todos los pendientes independiente la semana y el mes" y "yo voy revisando para adelante"

### TES-18
- Enunciado: El sistema debe trabajar la nomina por empresa, sin mezclar en una vista los datos de otra empresa.
- Modulo: tesoreria
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [56:25]
- Cita: "cuando este trabajando por empresa al final va a tener que ver por empresa como esta la cosa"

### TES-19
- Enunciado: El sistema debe mostrar las semanas con un conteo de lo pendiente en cada una, la semana actual y la proxima, en pesos y en dolares.
- Modulo: tesoreria
- Clase: ui
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [53:19]
- Cita: "yo voy viendo todas las semanas" y "me meto en esa semana y veo que es lo que tengo que pagar"

### TES-20
- Enunciado: El sistema debe tener en tesoreria un mantenedor de plazos de atraso, con aviso critico configurable y filtros rapidos, por ejemplo 30 y 90 dias.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [58:24]
- Cita: "cuando pase de 30 dias se le agregue el estado critico" y la respuesta "Si, eso si" y "un maestro que este en tesoreria"

### TES-21
- Enunciado: El sistema debe mostrar la nomina de la semana actual, con pendientes y atrasados, y un historico con fechas desde y hasta, mas banderas de atraso con color y nombre.
- Modulo: tesoreria
- Clase: ui
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [49:56]
- Cita: "Aprobado por Lupe, cierto? Si, esta aprobado"

### TES-22
- Enunciado: El sistema debe agrupar el estado de cuenta por RUT y mostrar cuenta por cobrar, cuenta por pagar y el anticipo restado del saldo.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [01:06:06]
- Cita: "la cuenta por cobrar, la cuenta por pagar y menos anticipo en el saldo"

### TES-23
- Enunciado: El sistema debe enlazar el egreso contabilizado de la cartola al proveedor, y contemplar que ese movimiento puede ser un anticipo; el asiento en contabilidad aun no estaba listo el 24-09.
- Modulo: tesoreria
- Clase: duda
- Voz: no-claro
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [01:02:12]
- Cita: "ese movimiento se va a ver en el proveedor porque ese ingreso pudo haber sido un anticipo"

### TES-24
- Enunciado: El sistema debe registrar aperturas de flujo de caja y corregirlas en la moneda de origen, y ofrecer una vista en pesos solo de consulta, con tipo de cambio y fecha.
- Modulo: tesoreria
- Clase: ui
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [01:03:20]
- Cita: "se puede registrar Las aperturas" y "ver la tabla En pesos" "solamente visual no queda en base de datos"

## Contabilidad

### CON-01
- Enunciado: El sistema debe tomar como referencia un asiento de venta real y su comprobante PDF, con libertad de mejorar el formato.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-10-demo-cliente.md [56:36]
- Cita: "Te mando un correo" y "Si se puede mejorar, mejor. Estamos dispuestos a tener cambios en el formato"

### CON-02
- Enunciado: El sistema debe dejar sin cerrar si el centro de costo, el elemento de costo y el area de negocio se exigen en el plan de cuentas o se piden al contabilizar la cartola, la compra y la venta.
- Modulo: contabilidad
- Clase: duda
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-23-dudas-cliente.md [47:49]
- Cita: "para saber donde predomina, donde se hereda, cual dejamos y cual eliminamos" y "vamos a conversarlo"

### CON-03
- Enunciado: El sistema debe llevar la contabilidad siempre en pesos y dolares, aunque el movimiento venga en otra moneda.
- Modulo: contabilidad
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [32:41]
- Cita: "independiente de que trabajemos con otras monedas, siempre nuestra contabilidad es peso y dolar. Siempre."

### CON-04
- Enunciado: El sistema debe traer el tipo de cambio del dia desde el Banco Central cuando no se ingresa, y permitir modificarlo al registrar la factura.
- Modulo: contabilidad
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [32:52]
- Cita: "cuando uno no pone el tipo de cambio" "llamar el dato del banco central" y "el que modificamos cuando ingresamos factura"

### CON-05
- Enunciado: El sistema debe agregar el yuan como tercera columna del comprobante, en todos los casos, ademas de peso y dolar.
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [33:22]
- Cita: "si se puede adicionar el yuan en paralelo tambien" y "esto es para todos los casos"

### CON-06
- Enunciado: El sistema debe guardar el auxiliar como el RUT de la contraparte, sin digito verificador.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [33:48]
- Cita: "El aux es el auxiliar Que seria el root" y "Sin el digito verificador"

### CON-07
- Enunciado: El sistema debe armar la glosa con el comentario ingresado al contabilizar, numero de factura y una descripcion corta, y repetir esa glosa en todas las lineas del comprobante.
- Modulo: contabilidad
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [37:25]
- Cita: "la glosa de abajo Que es la factura, numero de factura Y un poco de la descripcion" y "tambien quede en la cuenta de cliente y quede en la cuenta de IVA"

### CON-08
- Enunciado: El sistema debe nombrar la cuenta de IVA del comprobante de venta como IVA debito, no como caja.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [38:52]
- Cita: "la cuenta que dice caja, esa deberia ser IVA debito"

### CON-09
- Enunciado: El sistema no debe imprimir en el comprobante el nombre del dueno de la empresa.
- Modulo: contabilidad
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [38:39]
- Cita: "aparece el nombre de una persona" y "No, no es necesario. Ese es el nombre de nuestro dueno"

### CON-10
- Enunciado: El sistema debe dejar el area de negocio fuera del uso actual: no se ocupa como parametro ni para gestion.
- Modulo: contabilidad
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [16:23]
- Cita: "actualmente el area de negocio no la usamos mucho, de hecho no la utilizamos como parametro ni siquiera para hacer gestion"

## Admin

### ADM-01
- Enunciado: El sistema debe seguir avanzando tesoreria con Lupe y abastecimiento con Mario mientras Maria Jesus esta de vacaciones.
- Modulo: admin
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-10-demo-cliente.md [13:52]
- Cita: "avancen, por ejemplo, en el modulo de tesoreria, en el modulo de abastecimiento" "tesoreria lo veria Lupe" "abastecimiento, Mario"

### ADM-02
- Enunciado: El sistema debe quedar revisado por Mario en usuarios, roles, permisos, inicio de sesion Microsoft y parametrizacion; por Lupe en contratistas y tesoreria; por Maria Jesus en contabilidad.
- Modulo: admin
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-14-demo-avances.md [11:14]
- Cita: "validar los usuarios, robles y permisos. Yo. Yo, Mario" y "La Lupe" en contratistas y "Maria Jesus" en contabilidad

### ADM-03
- Enunciado: El sistema debe incorporar dos usuarios mas, Agustín y Rafa, invitados por correo.
- Modulo: admin
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-09-14-demo-avances.md [20:27]
- Cita: "las siguientes van a mandar ahi el correo, de Agustin y de Rafa"

### ADM-04
- Enunciado: El sistema debe dejar configurar el servidor de correo de la empresa para que las notificaciones salgan de un correo propio.
- Modulo: admin
- Clase: pedido
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-10-demo-cliente.md [52:35]
- Cita: "dentro de las configuraciones, las parametrizaciones poder agregar un servidor de correo"

### ADM-05
- Enunciado: El sistema debe poder importar y exportar centros de costo, elementos de costo y codigos financieros, y guardar historial de cambios.
- Modulo: admin
- Clase: pedido
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [14:36]
- Cita: "cambios en los centros de costo, elementos de costo, codigo financiero" y "exportar e importar y tener historial de modificaciones"

### ADM-06
- Enunciado: El sistema debe dejar un maestro en vigente o anulado: anulado no se usa y no se borra la historia.
- Modulo: admin
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [17:36]
- Cita: "el anulado es solamente que no se puede utilizar pero no se borra la historia" y "queda como no disponible"

### ADM-07
- Enunciado: El sistema debe configurar por separado los dias de pago del neto y del IVA del proveedor, con dias predefinidos y tambien un numero manual, por ejemplo 45, como sugerencia editable en los demas modulos.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [18:17]
- Cita: "condiciones de pago para el neto y para el IVA" y "yo puedo poner 45 dias, por ejemplo"

### ADM-08
- Enunciado: El sistema debe mantener maestros separados de cliente y de proveedor, y al escribir el RUT copiar los datos si esa persona ya existe en el otro maestro.
- Modulo: admin
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [25:23]
- Cita: "la mayoria es un solo proveedor o solo cliente" "el 98 por ciento" y "al momento yo crear como cliente el mismo root me llame la informacion"

### ADM-09
- Enunciado: El sistema debe dejar la creacion de clientes y proveedores en una jefatura, por seguridad, y no partir el formulario en dos perfiles de usuario.
- Modulo: admin
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [19:48]
- Cita: "la creacion de proveedores y clientes la tengo yo como jefatura" "Por un tema de seguridad"

### ADM-10
- Enunciado: El sistema debe, al consultar un RUT, mostrar los movimientos tanto de proveedor como de cliente, y marcar en la ficha que ese RUT existe en el otro maestro.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [27:11]
- Cita: "consulta del root, me va a salir todos los movimientos que tenga el root, ya sea como proveedor o como cliente"

### ADM-11
- Enunciado: El sistema debe traer indicadores del Banco Central al dar de alta una moneda, permitir monedas sin esa asociacion, y guardar historico sin pisar los montos ya registrados en otros modulos.
- Modulo: admin
- Clase: integracion
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-10-01-reunion-cliente.md [27:49]
- Cita: "se puede de todas formas agregar monedas sin que quede asociado al banco central" y "no esta pensado como para que esto pise la informacion"

### ADM-12
- Enunciado: El sistema debe dejar sin decidir si el maestro de proveedores vive en parametrizacion o se mueve a compras, segun quien tenga permiso de editarlo.
- Modulo: admin
- Clase: duda
- Voz: equipo
- Quien: no dicho
- Fuente: transcripcion-2026-09-24-reunion-cliente.md [48:15]
- Cita: "si es que hay personas que necesitan modificar campos de proveedores pero no acceder a toda la parametrizacion"

### ADM-13
- Enunciado: El sistema debe poder cargarse con informacion historica de Almahue para la marcha blanca, en vez de probar solo con numeros de demostracion.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-10-demo-cliente.md [48:50]
- Cita: "estar trabajando con la informacion de Almagro" "con la informacion historica que tenemos"

## Contradicciones

La reunion mas nueva gana. Aqui solo choques entre estas cinco reuniones.

1. Tipo de cambio de la nota de credito. El 10-09, cerca de [17:29], la nota debe respetar el tipo de cambio congelado de la factura. Minutos despues, [25:12], en correccion de monto ese tipo de cambio se puede editar, precargado desde la factura y no desde el dia; la anulacion sigue copiando el documento. Gana el pedido de las [25:12] del mismo dia. El 01-10 Maria Jesus agrega la regla general: si no se ingresa tipo de cambio, se llama el del dia al Banco Central, y se modifica al ingresar la factura [32:52].

2. Quien fija el tipo de cambio en la emision. El 10-09 el equipo dice que sale solo del Banco Central [33:23]. Enseguida el cliente dice que lo va a dar en la ficha de emision [33:44]. El 01-10 cierra el punto: dato del dia sugerido y editable al registrar la factura [32:52]. Gana el 01-10.

3. Factura sin orden de compra aprobada. El 14-09 no se rechaza sola y no puede ser rigido: se destaca, y a los 8 dias pasa como aceptada si nadie reclama [24:00] [26:10]. El 23-09 no se contabiliza hasta asociar orden o proforma [25:36], el plazo dicho ahi es de 7 dias [14:50] [37:48], y contabilidad avisa a quien debe crear la orden [41:41]. El 01-10 el equipo muestra un prerequisito de orden vinculada para aceptar o rechazar; el cliente no confirma ese bloqueo y si confirma el aviso a quien crea la orden [46:01]. Gana destacar y no contabilizar sin asociacion. No gana un bloqueo duro de aceptar o reclamar. El numero de dias queda en tension: 8 el 14-09 y 7 el 23-09; la cifra mas nueva es 7 y nadie la corrige el 01-10.

4. Orden madre. El 23-09 y el 24-09 la madre es el control de la compra, no se contabiliza, y la hija nace al recepcionar cantidades de la factura parcial [28:50] [26:36]. El 01-10 Maria Jesus limita la madre a un dato informativo que no debe verse fuera de insumos [47:20], y la entrada a bodega de materiales es la guia fisica de la semana; la factura de fin de mes es la que se asocia a la orden [55:55]. Gana el 01-10 para insumos: guia entra stock, factura asocia y contabiliza, madre no sale de insumos. La hija del 24-09 sigue como el documento que contabiliza el parcial.

5. Adjuntos de venta. El 24-09 primero se dice que en ventas no se adjuntan documentos y en compras si [11:31]. En el mismo tramo se corrige: compras y ventas, mas de un archivo [12:18]. Gana el cierre de ese tramo.

6. Ficha cliente y proveedor. El 24-09 los maestros ya estan separados y el RUT hereda datos de uno al otro [47:07]. El 01-10 el equipo propone una sola ficha con marcas de proveedor, productor o cliente. Maria Jesus lo rechaza: siguen separados, la jefatura crea ambos, el 98 por ciento es solo uno de los dos, y al tipear el RUT se copian los datos [19:48] [25:23]. Gana Maria Jesus el 01-10. Productor como tercer tipo de la ficha unica no quedo confirmado.

7. Area de negocio. El 01-10 el equipo la agrega al asiento de venta como campo pendiente. El mismo dia Maria Jesus dice que hoy no la usan ni como parametro ni para gestion [16:23]. Gana la voz del cliente: no es de uso actual. Sigue abierta si control de gestion la va a pedir despues.

8. Cartola y mes anterior. El 14-09 primero se excluye el movimiento del mes anterior, despues se pide cargarlo, despues no duplicar el saldo inicial, y al final un desde-hasta para carga semanal [47:17] [48:12] [48:41] [49:11]. El 24-09 el equipo avisa si la fecha no cae en el mes contable y carga el mes siguiente [01:00:03]. El cliente no cierra ese aviso. Gana, como regla dicha por el cliente, el rango de fechas y no duplicar el saldo inicial del 14-09.

9. Donde se contabiliza el egreso. El 14-09 Maria Jesus pide contabilizar con la nomina y no linea a linea en la cartola [57:45]. El 23-09 y el 24-09 se muestra contabilizar el movimiento de la cartola y, ademas, asociarlo a la semana de nomina; Lupe dice que esa asociacion le acomoda [50:11]. El 24-09 el asiento aun no se ve en contabilidad [01:02:01]. No hay retractacion el 01-10, y Lupe aprueba la vista de nomina [49:56]. Lectura que deja la evolucion: la nomina manda el egreso y la cartola se cruza con ella; el asiento contable de ese cruce no quedo mostrado.

10. Dia 10 del mes siguiente contra dias de credito. Al inicio del 24-09 Mario deja como defecto pesos y pago el dia 10 del mes siguiente [03:08]. Mas tarde, en la misma reunion, el credito es en dias que trae la factura, y neto e IVA van separados [43:46] [43:59]. El 01-10 se ratifica neto e IVA independientes y dias manuales, por ejemplo 45 [18:17]. Gana el detalle del 24-09 en la tarde, ratificado el 01-10. El dia 10 queda como defecto antiguo de esa misma reunion, no como regla final.

11. Proforma de contratistas. El 23-09 se dice que en ese modulo la proforma es la orden de compra y se referencia en la factura [21:43], y en el mismo dia Mario pide no cerrar el modulo [22:48]. El 24-09 se posterga. El 01-10 la duda sigue abierta: si la proforma se convierte en orden de compra [54:12]. Gana dejarlo sin cerrar.

12. Piso de venta y precio del movimiento. El 10-09 la venta nacional no puede ir bajo el monto de bodega [28:33], y la exportacion no usa ese piso [24:10]. Minutos despues, el movimiento de existencia debe tomar el precio de la orden de compra de ingreso, y el promedio es solo informativo [30:42]. No se anulan: una regla es de precio de venta nacional y la otra es de valorizacion de stock y de devolucion. La devolucion no debe usar el promedio [29:32].
