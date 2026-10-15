# Digest internas y GoSocket (03/09 a 06/10/2026)

Extraccion solo de las 12 transcripciones pedidas. Voz=cliente solo si el texto atribuye la frase a Agustin, Maria Jose/MJ, Lupe o Mario. El resto del equipo (Carlos, Sergio, Jose, Diego) es voz=equipo. Tecnicos de GoSocket (Pablo, Cristian mencionado) es voz=proveedor.

No se uso otra documentacion.

---

## Ventas

### V-01
- Enunciado: En la orden de venta, al agregar items se arma una grilla (una fila debajo de otra), no una pantalla completa por item.
- Modulo: ventas
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [03:19]
- Cita corta: "que se agregue un campo debajo... se vaya construyendo una grilla"

### V-02
- Enunciado: Guardar la orden de venta valida stock antes de insertar el movimiento y alerta si no hay stock.
- Modulo: ventas
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [06:31]
- Cita corta: "en el boton guardar... va a hacer la validacion ahi... si no hay stock... te deberia tirar alerta"

### V-03
- Enunciado: Guardar la orden de venta vuelve al listado. No salta solo a emitir el DTE.
- Modulo: ventas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [06:49]
- Cita corta: "La orden de venta le da a guardar y te deberia devolver... al libro"

### V-04
- Enunciado: Quedo abierto si la factura se emite directo desde la orden de venta o en un paso aparte. Hay que validarlo con el cliente. El equipo recuerda que, en la reunion con Mario y Lupe, las aprobaciones eran de compras.
- Modulo: ventas
- Clase: duda
- Voz: cliente
- Quien: Mario y Lupe (relato del equipo)
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [07:31]
- Cita corta: "en la reunion con Mario Lu... eso lo compra las aprobaciones... validemoslo con ellos"

### V-05
- Enunciado: Decision de demo: en la orden de venta solo Guardar. Facturar queda en Emitir, en un solo orden, no en los dos lados.
- Modulo: ventas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [15:45]
- Cita corta: "en la orden de venta Guardar... facturar... no lo pondria... una vez por aca... y de aca darle facturar"

### V-06
- Enunciado: Si despues el cliente pide facturar al guardar la orden de venta, se ve en ese momento.
- Modulo: ventas
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [16:08]
- Cita corta: "si ellos despues nos dicen... al momento de guardar la orden de venta tiro facturar... ya lo vemos"

### V-07
- Enunciado: La orden de venta no lleva asignacion de cuenta contable. Se saca de ahi.
- Modulo: ventas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [13:48]
- Cita corta: "solo en el libro de venta, dejalo solo en el libro de venta, y que en la orden de venta no se puede asignar"

### V-08
- Enunciado: Si el cliente tiene correo en el mantenedor, al emitir la orden de venta y al facturar se le envia correo automatico, con opcion de reenviar. El envio queda en el tracking.
- Modulo: ventas
- Clase: pedido
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [21:17]
- Cita corta: "Si el cliente tiene un correo... cuando imitas una orden de venta tienes que informar... cuando tu factures... mandar el correo"

### V-09
- Enunciado: Las alertas verdes de cada paso se reemplazan por una sola alerta cuando el documento ya esta emitido.
- Modulo: ventas
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [22:46]
- Cita corta: "no alertito por cada paso... sino que alertad ya cuando esta emitido no mas"

---

## Facturacion

### F-01
- Enunciado: La fecha de vencimiento no es obligatoria, pero es importante en documentos emitidos y recibidos, y se deja en pantalla.
- Modulo: facturacion
- Clase: dato
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [02:33]
- Cita corta: "La fecha de vencimiento es importante para los documentos tanto emitidos como recibidos... No es obligatorio"

### F-02
- Enunciado: En el maestro de clientes, direccion fiscal, comuna y ciudad son obligatorias porque GoSocket lo pidio.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: GoSocket (relato de Carlos); Sergio confirma que es obligatorio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [04:13]
- Cita corta: "Por lo que habia solicitado Kozoke tuve que agregarle obligatorio la direccion fiscal, la comuna, ciudad"

### F-03
- Enunciado: El usuario ve el PDF dentro del ERP (previsualizacion). La descarga a base queda transparente. El boton no es "descargar".
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [13:35]
- Cita corta: "cuando el buen pinche Ver pdf, no descargarlo... que se te previsualice el pdf y la opcion de descargarlo"

### F-04
- Enunciado: El folio que devuelve GoSocket es el folio de la primera columna. Ese folio es un boton que abre el PDF. El ojito abre el tracking, no el PDF.
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [17:49]
- Cita corta: "El folio que te estan devolviendo... es el folio que tienes que poner... en la primera columna... si tu lo pinchaste abra el pdf"

### F-05
- Enunciado: El tracking del documento lleva fecha y hora de emision, usuario que emitio, y si se envio correo y a que casilla.
- Modulo: facturacion
- Clase: dato
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [19:26]
- Cita corta: "cuando fue emitido la fecha y hora... por que usuario fue emitido... en el tracking deberia salir de que se envio el correo"

### F-06
- Enunciado: GoSocket entrega el folio de una. El estado pendiente es la revision del SII, no un folio pendiente.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [23:15]
- Cita corta: "No deberia ya tener folio pendiente porque gozo que te entrega folio de una... el estado del pendiente realmente la revision del CI"

### F-07
- Enunciado: Al facturar en Emitir se piden las cuentas. En el libro de ventas, el estado "por contabilizar" abre un popup de item y cuenta. La orden de venta no lleva esa asociacion.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [14:19]
- Cita corta: "Al facturar te pide las cuentas... Solamente sacaria de la orden de venta... lo dejaria en el libro de venta y en emitir DT"

### F-08
- Enunciado: El libro de ventas no lista ordenes de venta.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [15:40]
- Cita corta: "en el libro de ventas no deberiamos tener las ordenes de venta"

### F-09
- Enunciado: En el libro de ventas, anular abre un modal con tres notas de credito: anulacion total, correccion de monto y correccion de texto.
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [20:37]
- Cita corta: "ese boton te permite levante 3 opciones: anular total, correccion de monto o correccion de texto"

### F-10
- Enunciado: Anulacion total pide solo confirmar, anula el 100% y crea un documento nuevo tipo nota de credito, con referencia al folio, tipo y fecha.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [21:12]
- Cita corta: "anular total, ahi... te va a emitir la nota de credito de una... no tiene que pedir nada mas"

### F-11
- Enunciado: El codigo de referencia de la nota de credito es 1 anula documento, 2 corrige texto, 3 corrige montos. Va en el nodo de referencia (hasta 40 lineas).
- Modulo: facturacion
- Clase: integracion
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [28:15]
- Cita corta: "1, anula documento referencia. 2, corrige texto. 3, corrige montos... esa informacion tu la mandas en la referencia"

### F-12
- Enunciado: Corregir texto arma un XML de una linea, cantidad uno y precio cero, del tipo "donde dice X debe decir Y".
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [30:48]
- Cita corta: "una pura linea de detalle... donde dice tanto debe decir tanto... cantidad uno y precio cero"

### F-13
- Enunciado: La nota de credito de montos es lo que se rebaja de la factura, no el saldo que queda. El formulario muestra las lineas para informar cantidad y monto a rebajar.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [33:56]
- Cita corta: "La nota de credito es lo que yo voy a rebajar de la factura... si le pase 8... rebajar solo 2"

### F-14
- Enunciado: Si una factura queda anulada por nota de credito, el estado "anulada" se ve en la grilla, sin abrir el tracking. El tracking tambien registra nota de credito y de debito.
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [39:21]
- Cita corta: "si se le emitio una nota de credito y aparece, fue anulada, tiene que aparecer como anulada"

### F-15
- Enunciado: Anular un documento emitido fuera del ERP se resolveria con carga masiva. Quedo para despues.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [23:24]
- Cita corta: "eso lo que vamos a tener que hacer ahi es carga masiva... eso es un tema despues"

### F-16
- Enunciado: Registrar el pago de la factura de venta no se ve en esta etapa. Primero la nota de credito.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-07-interna-carlos-sergio.md [40:05]
- Cita corta: "el tema de registrar ese pago todavia no lo vemos... enfocate eso"

### F-17
- Enunciado: La boleta que mando Maria Jesus trae precio unitario en dolares. El tipo de cambio se ingresa en pesos y calcula el monto en pesos.
- Modulo: facturacion
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus (documento que ella mando)
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [01:41]
- Cita corta: "la boleta que mando la Maria Jesus... Precio unitario le falta... eso se supone va a ser en dolares"

### F-18
- Enunciado: En exportacion, bulto y puerto van con numero. Paises, puertos de embarque y de desembarque usan codigo y glosa de aduana.
- Modulo: facturacion
- Clase: dato
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [03:06]
- Cita corta: "ellos mandaban el bulto como numero... puertos de embarque y desembarque tambien deberian estar con el codigo"

### F-19
- Enunciado: Los campos obligatorios de la factura de exportacion se marcan con asterisco, contra lo que el esquema exige.
- Modulo: facturacion
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [04:24]
- Cita corta: "teneis que validarlo contra lo que es obligatorio y embarcarlo ahi con el asterisco rojito"

### F-20
- Enunciado: La exportacion envia dos monedas: la de origen (dolares) y la de conversion (pesos). Los totales muestran la moneda.
- Modulo: facturacion
- Clase: integracion
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [06:16]
- Cita corta: "se mandan dos... en dolares y en pesos... me faltaba la de conversion... los totales para la exportacion agregar la moneda"

### F-21
- Enunciado: El libro de ventas muestra el tipo con codigo y glosa, y el filtro incluye boleta 39 y 41, factura 33 y 34, guia 52, nota de debito 56, nota de credito 61, factura de exportacion 110, nota de credito de exportacion 111 y nota de debito de exportacion 112.
- Modulo: facturacion
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [07:22]
- Cita corta: "la boleta afecta que es la 39... 110 es una factura de exportacion... 111, nota de credito de exportacion... podriais dejar codigo guion tanto"

### F-22
- Enunciado: No enviar duplicada la descripcion del item. La representacion grafica concatena nodos y el nombre sale dos veces. Dejar el nodo disponible y enviarlo solo si el negocio lo usa.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo (GoSocket)
- Fuente: transcripcion-2026-09-15-gosocket-kickoff.md [03:28]
- Cita corta: "se duplica... eviten hacerlo... dejenlo disponible en el caso de que el negocio lo necesite"

### F-23
- Enunciado: En el ERP se agrega una descripcion opcional del item de bodega, para mandarla en el XML cuando haga falta.
- Modulo: facturacion
- Clase: dato
- Voz: equipo
- Quien: Carlos; Pablo confirma que no hay problema
- Fuente: transcripcion-2026-09-15-gosocket-kickoff.md [04:44]
- Cita corta: "vamos a agregar el apartado de agregar una descripcion que va a ser opcional para los items"

### F-24
- Enunciado: Maria Jesus ya envio representaciones graficas. Pablo las construye y despues se valida la data del documento. El PDF de documentos nuevos sale al emitir. Regenerar un PDF antiguo se hace en el portal, no por API.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo; el material lo mando Maria Jesus
- Fuente: transcripcion-2026-09-15-gosocket-kickoff.md [05:19]
- Cita corta: "crear las representaciones graficas que ya me mando Maria Jesus... Regenerar PDF... por la API no lo puedes hacer"

### F-25
- Enunciado: Antes de emitir al portal de pruebas, el certificado del firmante tiene que estar cargado y con permiso de firma en el SII. Si no, el documento sale rechazado.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [24:16]
- Cita corta: "el certificado ya tiene que estar cargado, porque si no, nos van a salir como rechazado"

### F-26
- Enunciado: Maria Jesus quiere que Mago quede con el representante legal Nico. Pudo anular folios de prueba con el certificado de don Pablo. Pablo dice que el certificado de firma puede ser de cualquier usuario firmante, no solo del representante legal.
- Modulo: facturacion
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion-gosocket-qa.md [24:55]
- Cita corta: "la idea era que el Mawi LM quedara con el representante legal, Nico... me dejo eliminar los folios"

### F-27
- Enunciado: En QA los folios CAF se cargan a mano porque el SII da pocos. En productivo serian automaticos. Si el API dice que no existe el rango, falta folio y lo carga Maria Jesus.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [07:35]
- Cita corta: "en QA... los folios... lo ideal es que los carguemos manual. Ya en productivo seran automaticos"

### F-28
- Enunciado: Un rechazo por error de caratula suele venir de no informar la resolucion, su numero y su fecha.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [07:35]
- Cita corta: "un error de caratula generalmente se ocasiona cuando no se informa correctamente la resolucion"

### F-29
- Enunciado: En QA se pueden crear hasta 10 API keys. En productivo en general se entrega una, y la entrega GoSocket.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [26:53]
- Cita corta: "Para QA tienen limite de 10 API keys... en el productivo se entrega por lo generalmente una"

### F-30
- Enunciado: Las guias de despacho que emite el proveedor deben poder obtenerse en recibidos de GoSocket, para comparar la guia fisica con la digital.
- Modulo: facturacion
- Clase: integracion
- Voz: proveedor
- Quien: Pablo, ante pregunta de Sergio
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [02:51]
- Cita corta: "emitirse una guia y deberia aparecer... en los recibidos de la otra empresa... van a poder tambien adquirir la guia de despacho"

### F-31
- Enunciado: Para cerrar representaciones graficas, GoSocket pide un plan de pruebas: tres o cuatro documentos de cada tipo en QA, y avisar cuando esten, para ver rechazos y reparos con Maria Jesus.
- Modulo: facturacion
- Clase: pedido
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [06:17]
- Cita corta: "coloquen una tabla con los distintos tipos de documentos y prueben... tres documentos de cada tipo"

### F-32
- Enunciado: Alcance que el equipo fija para la demo del 03/09: ordenes de venta, facturacion, integracion GoSocket, ver el PDF y el tracking. Nada mas.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [24:56]
- Cita corta: "la presentacion del dia se enfoque solamente es ordenes de venta la facturacion integracion con go socket visualizacion del pdf el tracking"

### F-33
- Enunciado: Alcance del 10/09 hacia el cliente: emision, nota de credito (tambien al anular) y factura de exportacion, con GoSocket.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [11:35]
- Cita corta: "tenemos que matar esto de exportacion... emision... nota de credito... con el True Socket... y la factura de exportacion"

---

## Compras

### C-01
- Enunciado: El libro de compras se navega por pendientes, aceptados y rechazados, con los datos que devuelva el XML de GoSocket, incluido el PDF.
- Modulo: compras
- Clase: ui
- Voz: equipo
- Quien: Sergio y Jose
- Fuente: transcripcion-2026-09-14-interna-manana.md [04:16]
- Cita corta: "el front del libro de compra... sencillo de navegar entre los pendientes aceptados o rechazados... hay que mostrarlo"

### C-02
- Enunciado: La sincronizacion de compras es manual (boton) y tambien una tarea programada, cada una hora, para los tres estados. GoSocket no limita esa cantidad de llamados.
- Modulo: compras
- Clase: integracion
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [05:28]
- Cita corta: "sincronizar manual... programar cada una hora la sincronizacion de compra aceptado, pendiente, rechazado"

### C-03
- Enunciado: Todo documento recibido parte pendiente. Hay 8 dias para aceptar o reclamar. Solo aceptado se puede contabilizar. Rechazado pasa a rechazados. La aceptacion automatica se menciono y el equipo decide no meterla todavia.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [06:42]
- Cita corta: "dentro de 8 dias tu puedas aceptar o reclamar... si tu aceptas... recien lo puedes contabilizar... aun no, no nos metamos"

### C-04
- Enunciado: Las aprobaciones son solo de compras, no de ventas.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [08:12]
- Cita corta: "en el sistema manejan aprobaciones, tanto para compras como para ventas. No. Solo para compras"

### C-05
- Enunciado: El unico documento que Almahue emite hacia el proveedor es la orden de compra. El proveedor factura referenciando ese numero. La factura se lee del XML.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [10:26]
- Cita corta: "el unico documento que deberias tu emitir hacia tu proveedor es una orden de compra... va a referenciar esa orden de compra"

### C-06
- Enunciado: Si la factura referencia una orden de compra que sigue pendiente de aprobacion, no se acepta y se marca pendiente de aprobacion. Si la OC esta aprobada, la factura puede pasar a aceptada.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [09:03]
- Cita corta: "recibes una factura referenciando una orden de compra que esta en pendiente de aprobacion, esa no podria aceptarse"

### C-07
- Enunciado: La recepcion de compras se trae de GoSocket (sandbox). No hay ambiente de produccion para que el equipo cargue documentos.
- Modulo: compras
- Clase: integracion
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [12:40]
- Cita corta: "no hay produccion, aqui todo lo que el samba es de ellos y si quereis que carguen informacion ellos lo van a hacer"

### C-08
- Enunciado: La fecha de vencimiento del documento recibido es necesaria porque programan pagos por semana. Si el XML no la trae, hay que poder asignarla.
- Modulo: compras
- Clase: dato
- Voz: equipo
- Quien: Sergio (relata como trabaja Almahue)
- Fuente: transcripcion-2026-09-14-interna-manana.md [19:07]
- Cita corta: "La fecha de vencimiento del documento recibido... si el documento no viene con fecha de vencimiento, tenemos que... asignarlo"

### C-09
- Enunciado: Mover un documento de semana es compromiso de pago. No cambia la fecha de vencimiento. Hay una columna de dias de atraso.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio y Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [20:38]
- Cita corta: "puedes mover el documento... pero no cambian la fecha de vencimiento... es como compromiso de pago"

### C-10
- Enunciado: En el libro de compras se ven y descargan el XML y el PDF de GoSocket. Aceptar o rechazar. Al rechazar hay que indicar el tipo (falta de mercaderia o reclamo). Aceptar es una sola accion, no "aceptar" y "aprobar" a la vez.
- Modulo: compras
- Clase: ui
- Voz: equipo
- Quien: Jose y Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [33:05]
- Cita corta: "ver el xml... descargar el PDF... aceptar o rechazar... falta de mercaderia o reclamo"

### C-11
- Enunciado: Se saca la carga de documentos que no vienen con el RUT de la empresa. La carga masiva Excel se mantiene. La sincronizacion XML viene de GoSocket. Quedan las pestanas aceptados, pendientes y rechazados, mas un totalizado.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [30:00]
- Cita corta: "saca esos botones... la carga masiva si ese dejalo... pero solamente en excel yo sincronizo lo de xml"

### C-12
- Enunciado: Solo los documentos aceptados, y con fecha de vencimiento, alimentan la nomina semanal. Al aceptar un pendiente sin fecha, el sistema la pide. No se pone una fecha por defecto. Hay alerta si falta.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [44:43]
- Cita corta: "desde el libro compra que le puedan asociar fecha de vencimiento... solamente los aceptados deben mostrar aca la nomina semanal"

### C-13
- Enunciado: Aceptacion automatica y rechazo automatico no se requieren por ahora. Si se requiere una alerta: al llegar una factura de un RUT dado, notificar a personas definidas.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [51:45]
- Cita corta: "de aceptacion automatica no van a requerir ello, rechazo tampoco... cuando recibas una factura de un root x... notificacion"

### C-14
- Enunciado: Contabilizar compras queda en pausa hasta cerrar la contabilizacion de ventas. Despues se replica, con el debe y el haber al reves. En el libro de compras se eliminan editar y anular.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [50:24]
- Cita corta: "el contabilizar dejemoslo pausado... cuando ya tu cierres contabilizar ventas va a ser la misma para compras"

### C-15
- Enunciado: El boton de registrar pago desde el libro de compras es un pago efectuado. Queda como duda para Lupe, porque lo por pagar de compras va a la nomina semanal. Lo por cobrar seria uno a uno y aun no es un modulo.
- Modulo: compras
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [37:21]
- Cita corta: "ese seria el pago efectuado... esa factura va a estar dentro de lo que es la nomina semanal... el por cobrar ese no"

### C-16
- Enunciado: Despues de 8 dias, si no se rechaza, el SII acepta solo. Pueden llegar aceptados directo de GoSocket. Rechazar sin referencia a orden de compra es una regla que el equipo puede armar, pero la tienen que decidir ellos.
- Modulo: compras
- Clase: duda
- Voz: equipo
- Quien: Jose y Carlos
- Fuente: transcripcion-2026-09-22-interna.md [26:46]
- Cita corta: "despues de los ocho dias si tu no rechazas tu documento se acepta automaticamente por ley... eso tienen que decidirlo ellos"

### C-17
- Enunciado: La fecha que parte el conteo de los 8 dias es la recepcion en el SII. La fecha de recepcion en GoSocket serviria como filtro de llegada.
- Modulo: compras
- Clase: dato
- Voz: equipo
- Quien: Jose
- Fuente: transcripcion-2026-09-22-interna.md [38:20]
- Cita corta: "la fecha importante seria la fecha de recepcion SI, porque a partir de esa fecha tengo yo que contar los 8 dias"

### C-18
- Enunciado: Si la aceptacion se hace en el ERP, se guarda usuario y fecha. Si el documento ya viene aceptado desde GoSocket, no se sabe quien acepto.
- Modulo: compras
- Clase: dato
- Voz: equipo
- Quien: Jose
- Fuente: transcripcion-2026-09-22-interna.md [32:22]
- Cita corta: "fue directamente sincronizado de GoSocket entonces yo no puedo saber quien hizo esa aceptacion... manual... el usuario que lo hizo"

### C-19
- Enunciado: Aceptar en el ERP tambien acepta el documento en GoSocket.
- Modulo: compras
- Clase: integracion
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [04:42]
- Cita corta: "si le doy ahi a aceptar... se aceptan, y tambien se aceptan en GoSocket"

### C-20
- Enunciado: Al enlazar la factura recibida, se listan solo las ordenes de compra de ese proveedor (mismo RUT). En el XML de prueba no venia la referencia 801/802. Hay que preguntarles como van a enlazar la OC.
- Modulo: compras
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [03:14]
- Cita corta: "deberiamos listar solamente las ordenes de compra asociadas a ese root... preguntarnos de que manera van a enlazar la orden de compra"

### C-21
- Enunciado: El rechazo no es un comentario libre. Hay que indicar contenido o mercaderia parcial. Al aceptar un pendiente se deberia poder marcar la fecha de vencimiento. Preguntar si eso vive en el libro o en otro lado.
- Modulo: compras
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [07:04]
- Cita corta: "cuando tu reclamas un documento lo tienes que poner por contenido... o parcial de mercaderia"

### C-22
- Enunciado: Los documentos recibidos ya no se ingresan a mano. Entran por la sincronizacion de GoSocket. Sincronizar trae datos; no es un ida y vuelta.
- Modulo: compras
- Clase: decision
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [09:04]
- Cita corta: "sincronizar es traer datos realmente de GoSocket, no hay como una sincronizacion de ida y vuelta"

### C-23
- Enunciado: En documentos recibidos se podra asociar tanto una orden de compra como una proforma.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus (confirma el "si" de Sergio)
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [24:30]
- Cita corta: "en el modulo de compra documentos recibidos vamos a poder asociar proforma o ordenes de compra. Si"

### C-24
- Enunciado: La carga historica de DTE esta desfasada porque Acepta no dejo respaldo. Maria Jesus estima unos 1000 a 1200 documentos de un ano en AlmaWeb, no en Almahue. Perdieron el historial de AlmaWeb al cambiar de proveedor y tambien el del Mago. El SII deja bajar de a 20. Pablo dice que la carga se hace al final de la implementacion.
- Modulo: compras
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion-gosocket-qa.md [02:05]
- Cita corta: "por el lado de AlmaWeb... debiesen ser alrededor de unos 1000, 1200... perdimos el historial completo"

---

## Contratistas

### K-01
- Enunciado: Presupuestos quedaron pedidos dentro de contabilidad por el tema de contratistas.
- Modulo: contratistas
- Clase: pedido
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-mediodia.md [03:06]
- Cita corta: "Presupuestos... se solicito que se tenian que dejar... de los contratistas"

### K-02
- Enunciado: Ficha de contratista con razon social, especialidad, vigente o no, y fecha hasta la cual esta activo. Al llegar esa fecha pasa a inactivo solo.
- Modulo: contratistas
- Clase: dato
- Voz: equipo
- Quien: Diego (lo saco del video del cliente)
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [56:34]
- Cita corta: "razon social, especialidad, si se mantiene vigente o no... fecha... se va automaticamente a... inactivo"

### K-03
- Enunciado: La parametrizacion de labores, actividades, su asociacion y unidades (caja, hora, kilometro, kilo, tonelada, hora hombre, hectarea) va junta. En el sistema anterior estaba separada y eso era una queja.
- Modulo: contratistas
- Clase: ui
- Voz: equipo
- Quien: Diego
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [58:30]
- Cita corta: "una de las quejas mas grandes... tenian todo separado... se opto fue a centralizar todo"

### K-04
- Enunciado: El permiso es por pagina (lectura o escritura), no por funcion dentro de la pagina. Para separar quien parametriza labores de quien no, cada bloque pasa a submenú.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:01:35]
- Cita corta: "separar esto en paginas distintas... un submenu que se llame labores, actividades"

### K-05
- Enunciado: El tipo de contrato lleva codigo, nombre, cuenta debe, cuenta haber y cuenta administrativa. Esos campos salen del ERP que mostraba el cliente. La cuenta administrativa la pidio Maria Jesus.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:03:13]
- Cita corta: "cuenta administrativa, es el campo que los pidio asi la moneda de Jesus"

### K-06
- Enunciado: La tarifa vigente es por contratista, labor, actividad, unidad de control, centro de costo y fechas desde-hasta. La actividad se filtra por la labor. Todos los campos son obligatorios.
- Modulo: contratistas
- Clase: dato
- Voz: equipo
- Quien: Diego
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:03:46]
- Cita corta: "precio vigente por contratista, labor, actividad, unidad, centro de costos... todos los campos son obligatorios"

### K-07
- Enunciado: El ingreso diario aplica la tarifa vigente y alimenta la proforma. El precio unitario puede ser opcional y, si no se informa, toma la tarifa. Hay que mostrar que tarifa se aplico. Si se edita y el precio cambia, el motivo es obligatorio.
- Modulo: contratistas
- Clase: regla
- Voz: equipo
- Quien: Diego
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:08:18]
- Cita corta: "pudiera ser un precio unitario opcional y si no, que tomara... la tarifa... deberias mostrar que tarifa esta aplicando"

### K-08
- Enunciado: En ingresos diarios, indicadores de total por contratista y por periodo: es lo que se le va a pagar.
- Modulo: contratistas
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:09:28]
- Cita corta: "si yo pinto por contratista que me de un total de cuanto fue la tarifa... o por periodo todo lo que yo he gastado"

### K-09
- Enunciado: Mario, en llamada del 21/09, dice que la proforma es un documento previo a la orden de compra. Despues se genera la OC y esa pasa al flujo de aprobaciones. Desde contratistas se deberia poder crear esa OC.
- Modulo: contratistas
- Clase: decision
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:25:52]
- Cita corta: "La proforma es un documento previo de la orden de compra... se genera la orden de compra y ahi esto pasaria al flujo de aprobaciones"

### K-10
- Enunciado: Duda del equipo, a validar: si Almahue emite la factura de compra del contratista y declara ese impuesto, o si el contratista emite una factura recibida.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:17:26]
- Cita corta: "ellos emitían una factura de compra pero ellos declaraban ese impuesto... quiero validarlo manana si es asi"

### K-11
- Enunciado: El periodo de la proforma solo puede ser un periodo contable abierto. Unidades de medida no se duplican: viven en parametrizacion.
- Modulo: contratistas
- Clase: regla
- Voz: equipo
- Quien: Diego y Carlos
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:18:29]
- Cita corta: "la idea es que tome en consideracion solamente los periodos abiertos... en parametrizacion ya existia tambien unidades de medida"

### K-12
- Enunciado: Traspaso y cierre: asiento del mes, cierre de contratistas, reapertura y bloqueo de captura del mes cerrado. El digitador no entra a parametrizar. Quien no tiene permiso de contabilidad ve el asiento en un modal, sin editar.
- Modulo: contratistas
- Clase: pedido
- Voz: equipo
- Quien: Diego (relato de lo pedido)
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:22:20]
- Cita corta: "pasar lo aprobado de proforma a lo que vendria a ser la parte contable... bloquear captura del mes cerrado"

### K-13
- Enunciado: La pantalla de traspaso y cierre y la de auditoria hay que validarlas con el cliente. Auditoria, segun lo armado, es la trazabilidad (quien, hora, definitiva, reversa). Rodrigo seria el encargado de contratistas; pidieron reunion con el. El mostro AgroSmart el 23/07.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Sergio y Diego
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:32:39]
- Cita corta: "esta pantalla completa hay que dejarla asi como que es lo que buscan de esto... una reunion con Rodrigo"

### K-14
- Enunciado: Checklist que el equipo atribuye a pedidos del cliente, aun pendientes el 22/09: precio en el proceso sin tarifario; avance y asistencia del dia sin precio; tarifario editable en la misma grilla; filtro facturada o pendiente; aprobacion de un supervisor al crear o editar proforma o trabajo diario; la factura del proveedor no cancela las facturas por recibir.
- Modulo: contratistas
- Clase: pedido
- Voz: no-claro
- Quien: cliente no nombrado en esta reunion (checklist de reuniones previas)
- Fuente: transcripcion-2026-09-22-interna.md [25:12]
- Cita corta: "Precio dentro del proceso sin tarifario. Avance y asistencia del dia sin precio... Aprobacion de un supervisor"

### K-15
- Enunciado: El equipo duda si el contratista tiene una especialidad o varias. Tienden a quitar el campo, porque en el ingreso diario igual se elige la labor.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Carlos y Diego
- Fuente: transcripcion-2026-09-22-interna.md [06:51]
- Cita corta: "pueden hacer mas de una labor los contratistas... en el video mencionaban de que se pudiera enlazar... a una especialidad"

### K-16
- Enunciado: Para ingresar un ingreso diario tienen que estar abiertos el cierre de contratistas y el periodo contable. Cerrar contratistas no cierra el periodo para el resto del ERP. Reabrir exige motivo y queda en auditoria.
- Modulo: contratistas
- Clase: regla
- Voz: equipo
- Quien: Diego
- Fuente: transcripcion-2026-09-22-interna.md [14:17]
- Cita corta: "si es que el cierre contratista esta cerrado, no se puede ingresar, y el periodo contable tampoco. Tienen que estar si o si los dos abiertos"

### K-17
- Enunciado: La proforma en borrador, al pasar a definitiva, entra al asiento. "Facturar" no emite un DTE: asocia una factura que ya existe. El equipo corrige que el paso siguiente es la orden de compra, no el libro de compras directo.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Diego y Carlos
- Fuente: transcripcion-2026-09-22-interna.md [11:21]
- Cita corta: "aunque diga factura... es como un registro de compra. No se genera una factura... deberia haber pasado... orden de compra"

### K-18
- Enunciado: Una persona ve contratistas y parametriza todo el modulo (labores, actividades, unidades, tipos de contrato). La parametrizacion sensible no queda abierta a cualquiera.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Sergio y Carlos
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [28:44]
- Cita corta: "son datos sensibles... de contratistas va a haber un encargado... el mismo usuario tiene que parametrizar todo contratista"

### K-19
- Enunciado: Al crear el contratista se hace match con el proveedor (razon social), porque la orden de compra sale contra el proveedor.
- Modulo: contratistas
- Clase: regla
- Voz: equipo
- Quien: Carlos (lo que le dijo Diego)
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [31:16]
- Cita corta: "al momento de generar un contratista hacia el match de que tambien fuera un proveedor para el tema de la orden de compra"

### K-20
- Enunciado: Al armar la proforma, primero se elige el contratista y recien ahi se listan sus ingresos diarios. El numero de proforma es secuencial. El periodo es ano y mes. La previsualizacion es un total que se actualiza al marcar lineas.
- Modulo: contratistas
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [35:19]
- Cita corta: "antes de mostrar estos... deberias seleccionar el contratista... El numero de la proforma debe ser secuencial"

### K-21
- Enunciado: El 23/09 el equipo, apoyado en un video de Maria Jesus, dice que la proforma no pasa por aprobacion: se convierte en orden de compra y la OC es la que se aprueba. Dejan la aprobacion de proforma solo como propuesta. El supervisor en la proforma les sobra.
- Modulo: contratistas
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus (video que cita el equipo)
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [36:53]
- Cita corta: "las proformas que me imagino que el se baso en el video... de la Maria Jesus, las proformas no pasan por aprobacion"

### K-22
- Enunciado: Traspaso y cierre seria un cierre de mes solo de contratistas, para que no entren mas proformas, y esa informacion pasa a contabilidad. Si el cierre contable del mes ya se hizo, las proformas atrasadas pasan al mes siguiente. Hay que validar si son dos cierres.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [38:10]
- Cita corta: "ellos puedan cerrar... contratistas, como el cierre del mes... validemoslo, planteemoslo"

### K-23
- Enunciado: Maria Jesus define el flujo como fusion de AgroSoft y AgroSmart: se salta el contrato (en AgroSmart no hace falta). Se crea el contratista, se registran los dias, se emite la proforma, pasa a aprobacion, facturacion y pago.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [12:23]
- Cita corta: "vamos a saltar el tema del contrato porque no fue necesario si tomamos de base AgroSmart... se emite la proforma, pasa a aprobacion"

### K-24
- Enunciado: La proforma no es una factura. Junta varias informaciones de ingresos diarios. Pueden haber 10 proformas asociadas a una sola factura.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [13:14]
- Cita corta: "la proforma no es una para la factura, sino que son varias informaciones de ingresos diarios... 10 proformas que se asocien a una factura"

### K-25
- Enunciado: Ficha del contratista: codigo numerico secuencial (el 11 si ya hay 10), distinto del codigo de proveedor que es el RUT. Tambien RUT, nombre, direccion y quien lo creo.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [14:13]
- Cita corta: "el codigo, que es el numero del contratista... A diferencia del codigo de proveedores, que es el RUT"

### K-26
- Enunciado: En el ingreso diario: empresa y temporada. El predio es opcional para las dos empresas (agricola lo usa, ALM no). ALM necesita saber si es jornal o a trato. El funcionamiento debe servir si crean mas empresas.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [14:51]
- Cita corta: "quise eliminar el predio o que no sea necesario... por el lado de ALM... jornal o a trato... un dato opcional para las dos"

### K-27
- Enunciado: Datos del ingreso diario: fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duracion, valor unitario del trato o de la jornada, cantidad y total. El trabajador no es necesario.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [16:11]
- Cita corta: "La fecha, el sector, el cuartel, la faena, la forma de pago, la unidad, el contratista, el trabajador no es necesario, la duracion"

### K-28
- Enunciado: Cuartel, faena y contratista tienen mantenedor, no texto libre. Por el lado ALM, faenas puntuales como servicio administrativo o armado de cajas.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [16:55]
- Cita corta: "lo ideal es que tenga mantenedor... por el lado de ALM... servicio administrativo o armado de cajas"

### K-29
- Enunciado: El ingreso diario es el detalle de la proforma. Al guardarlo se envia a aprobacion de la jefatura. Tambien se pueden agrupar: de 30 ingresos, 2 o 3 proformas. Los montos chicos quiza no escalan; la proforma agrupada (ejemplo 30.000 dolares) si deberia aprobarse. Se elige cuantos ingresos mandar y con eso se genera la proforma.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [17:39]
- Cita corta: "cada vez que nosotros ingresemos el ingreso diario y se guarde se envia a aprobacion de la jefatura... esa proforma deberia pasar por aprobacion"

### K-30
- Enunciado: Al crear la proforma se elige el contratista y se listan sus ingresos. Se puede tomar un subconjunto. Esos ingresos ya no quedan disponibles para otra proforma.
- Modulo: contratistas
- Clase: regla
- Voz: equipo
- Quien: Sergio; Maria Jesus confirma el caso
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [23:18]
- Cita corta: "te va a solicitar el contratista... y va a listar todos los ingresos diarios... esas 5... ya no van a estar disponibles"

### K-31
- Enunciado: La proforma, una vez aprobada, se calza con la factura que emita el contratista. No queda parcializada: si la proforma es 9600, no se acepta una factura por 5600. Una factura recibida puede tomar N proformas. El detalle se le manda al contratista para que facture.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [24:05]
- Cita corta: "esta proforma pasaria a aprobacion y una vez que se apruebe... match con la factura... la proforma no quede parcializada"

### K-32
- Enunciado: La proforma se envia al contratista (puede ser semanal, segun el avance) para comparar. Si no reclama precio o jornada, se da por aprobada y se puede asociar la factura. Si hay diferencia, se edita el ingreso diario de origen y la proforma vuelve a la aprobacion interna.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [25:52]
- Cita corta: "la proforma se compara con el contratista y se emite la factura... si llegamos acuerdo poder modificar la reforma... vuelve a pasar por el flujo"

### K-33
- Enunciado: Poder agrupar ingresos por rango de fecha o por labor. Al enviar la proforma, un estado del tipo "enviado a contratista", para no incluirla de nuevo en un segundo envio del mes. Correo al contacto cuando ya esta aprobada.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus (el estado lo propone Sergio y ella acepta el correo)
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [26:33]
- Cita corta: "los ingresos diarios los podamos agrupar en base a rango de fecha o a labor... una vez que esta aprobada se envia al mail"

### K-34
- Enunciado: El proveedor no aprueba dentro del sistema. Con el envio se marca "notificada a proveedor" y solo esas proformas se listan para asociar en compras, salvo que el contratista reclame.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Sergio, a partir de lo que dijo Maria Jesus
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [31:36]
- Cita corta: "el envio al proveedor de la proforma marcarla como notificada a proveedor... solamente las que esten como notificada... deberian listarse en las compras"

### K-35
- Enunciado: Los grupos de aprobacion de proforma y de orden de compra quedan separados. Un grupo no sirve para los dos documentos.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [36:55]
- Cita corta: "si es el grupo de aprobacion es para una pro forma... o es para una orden de compra. Pero no puede ser para ambos"

### K-36
- Enunciado: Hay que volver a incluir el tracking de notificaciones de aprobaciones. Queda por preguntar si hace falta un cierre semanal de proformas.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [33:23]
- Cita corta: "nos faltaria como hacer... las notificaciones de las aprobaciones... preguntar si es que va a ser necesario ese cierre"

### K-37
- Enunciado: KPI por pagina, exportar a Excel o PDF, y filtros o totalizados de tarifas: preguntarselo a Lupe, a quien el equipo trata como encargada del modulo en la reunion del 22/09.
- Modulo: contratistas
- Clase: duda
- Voz: equipo
- Quien: Diego; Carlos dice que Lupe esta encargada
- Fuente: transcripcion-2026-09-22-interna.md [19:23]
- Cita corta: "la Lupe... es la que esta encargada de este modulo... que KPI necesitan por pagina... si es que necesitan exportar"

---

## Inventario

### I-01
- Enunciado: Hay mantenedor de productos y de bodegas, y un visor de producto por bodega. No hay una vista global de todo el stock.
- Modulo: inventario
- Clase: ui
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-mediodia.md [04:08]
- Cita corta: "productos, esta aca... tenemos un mantenedor de bodegas... no tenemos como un global"

### I-02
- Enunciado: La salida a venta nace de la factura y no se edita, porque es un DTE y se podria maquillar el stock. El traspaso entre bodegas va con guia de despacho. Si el movimiento manual quedo mal en el monto, se elimina y se vuelve a cargar.
- Modulo: inventario
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-mediodia.md [06:18]
- Cita corta: "La salida de venta viene desde la factura... ese no se puede editar... pueden maquillar todo el stock"

### I-03
- Enunciado: Falta ver el caso de bodegas con mas de una bodega por item. En la demo del 03/09 el modo demo no lo tomaba bien.
- Modulo: inventario
- Clase: duda
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [03:51]
- Cita corta: "Todavia no agregabamos item a otras bodegas... no me lo esta tomando bien el modo demo"

### I-04
- Enunciado: Las devoluciones de fruta de exportacion irian a merma, no de vuelta a bodega. El sistema no distingue por empresa. Hay que preguntar si, al devolver, se pregunta reintegro a bodega, o si en el mantenedor se marca que insumos pueden volver.
- Modulo: inventario
- Clase: duda
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:44:46]
- Cita corta: "las devoluciones no son para... las exportaciones, ya que es fruta, entonces eso pasa a merma... hay que preguntarles"

---

## Contabilidad

### N-01
- Enunciado: Maria Jesus pidio en el plan de cuentas poder exigir centro de costo, elemento de costo y area de negocio. Eso choca con asociarlos directo en la venta o en la cartola. Hay que preguntarle a ella o a Mario si esos campos se borran del plan. Las tarjetas de contabilidad quedaron asignadas a Mario.
- Modulo: contabilidad
- Clase: duda
- Voz: cliente
- Quien: Maria Jesus (pedido que relata Carlos)
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [09:11]
- Cita corta: "la Maria Jesus me habia dicho que aqui tambien se hacian asociaciones... centro de costo, elemento de costo y aras de negocio"

### N-02
- Enunciado: Al contabilizar un movimiento de cartola se piden contracuenta, codigo financiero y destino. Falta el centro de costo y hay que validar si va, y a que se asocia (el centro de costo ya indicaria el area).
- Modulo: contabilidad
- Clase: duda
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [29:56]
- Cita corta: "te pregunta la cuenta de la contrapartida, el codigo financiero... y el destino. Aqui faltaria el centro de costo"

### N-03
- Enunciado: No se contabiliza en un periodo cerrado o inexistente.
- Modulo: contabilidad
- Clase: regla
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [32:24]
- Cita corta: "la contabilizacion no existe periodo de contabilizacion esta bien porque el periodo esta cerrado"

### N-04
- Enunciado: Contabilidad se alimenta de los asientos de compras, ventas y tesoreria. Despues salen balance, libro mayor y los otros reportes. Los reportes son la ultima pata y el equipo quiere verlos presencial.
- Modulo: contabilidad
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [01:46:23]
- Cita corta: "contabilidad se va a alimentar de los asientos contables nomas... el balance, el libro mayor"

### N-05
- Enunciado: La carga masiva (CCC) se menciono en reuniones y esta implementada, pero no esta aprobada: falta un documento de referencia del SII.
- Modulo: contabilidad
- Clase: duda
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [10:31]
- Cita corta: "habiamos hablado del tema de la carga masiva... No esta aprobado porque no tenemos un documento referente del SI"

---

## Tesoreria

### T-01
- Enunciado: Al contabilizar un egreso de la cartola se selecciona la nomina semanal a la que corresponde. Solo en egresos. En ingresos no hay nomina, porque la entrada la ven cuando llega al banco.
- Modulo: tesoreria
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-tesoreria.md [00:17]
- Cita corta: "cuando los contabilizar te permite seleccionar la nomina, cuando sea egreso... en los ingresos no existe nomina"

### T-02
- Enunciado: Una nomina semanal puede tener varios pagos (ejemplo 100 y 50 a dos proveedores). En la cartola son dos egresos y, al contabilizar, ambos se asocian a esa nomina. Como confirmar el calce de los dos movimientos quedo abierto.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-tesoreria.md [05:46]
- Cita corta: "al momento de contabilizar... este movimiento de 100 lucas y el movimiento de 50... corresponden a la nomina de la semana 2"

### T-03
- Enunciado: La cartola se carga desde Excel, a mano, y discrimina empresa por RUT (ALM y Almahue). Hay que dejarla lista para mas empresas, mas cartolas y mas bancos. El preview queda por moneda y por banco.
- Modulo: tesoreria
- Clase: dato
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [25:51]
- Cita corta: "tienen ALM y tienen ALMAWE... diferentes RUT... esto hay que mejorarlo pensando que... podrian tener mas"

### T-04
- Enunciado: Son cuatro bancos y cada uno tendria tres cuentas: pesos, dolares y yen.
- Modulo: tesoreria
- Clase: dato
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [23:30]
- Cita corta: "cuatro bancos, de los cuales cada uno tiene tres cuentas... en pesos, dolares y yen"

### T-05
- Enunciado: Si la cartola trae movimientos de un periodo anterior, hay que validar con ellos: puede ser un periodo contable ya cerrado, o un pago desfasado.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [27:40]
- Cita corta: "hay periodos que son anteriores que vienen en la cartola... puede ser que ese periodo este contablemente cerrado"

### T-06
- Enunciado: No han dicho si trabajan con cheque. Tampoco esta cerrado si una transferencia puede pagar dos facturas.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Diego y Carlos
- Fuente: transcripcion-2026-09-14-interna-manana.md [34:11]
- Cita corta: "aqui trabajan con cheque, no, no se, buena pregunta, no nos han dicho nada... una transferencia podria pagar dos facturas"

### T-07
- Enunciado: No esta claro si hacen cobranza. La plata de exportacion viene del exterior y la factura ya trae el tipo de cambio, asi que no transforman moneda dentro de una cobranza.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [22:08]
- Cita corta: "no se si hacen cobranza... la plata viene desde china... la factura ya viene con el monto... con el tipo cambio asignado"

### T-08
- Enunciado: Mario dijo en WhatsApp que el concepto es un agrupador para ordenar el flujo de caja. En la imagen, el item es el concepto. El codigo financiero se asocia al concepto. El flujo agrupa por concepto, por codigo financiero y por periodo.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: Mario
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [04:31]
- Cita corta: "el Mario en el grupo de WhatsApp... era un agrupador para ordenar el flujo de cajas... el item... corresponde al concepto"

### T-09
- Enunciado: El totalizado del flujo de caja es del periodo completo, no por semana: saldo caja, ingreso, egreso y saldo.
- Modulo: tesoreria
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [13:22]
- Cita corta: "si, es el totalizado... es por periodo completo... saldo caja... ingreso, egreso, saldo"

### T-10
- Enunciado: Quieren llegar al saldo del Excel, que esta en pesos: sumar todas las monedas convertidas a CLP. Pidieron un filtro rapido por moneda. Falta un totalizado unico en pesos, ademas de los saldos por moneda.
- Modulo: tesoreria
- Clase: pedido
- Voz: no-claro
- Quien: "ellos" / "pidieron" (imagen del grupo, sin nombrar en este tramo)
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [15:28]
- Cita corta: "un filtro rapido que pidieron... lo que quieren es llegar a este saldo... la sumatoria total en pesos"

### T-11
- Enunciado: Pidieron separar el flujo por banco. En cartola, saldos por cada banco y por moneda. Si es filtro o pestana nueva, validarlo con Lupe.
- Modulo: tesoreria
- Clase: pedido
- Voz: no-claro
- Quien: "ellos" / "pidieron"
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [17:47]
- Cita corta: "recuerdo que pidieron que era separarlo por banco... cartolas... saldos por cada banco y por moneda"

### T-12
- Enunciado: En egresos de cartola se pueden marcar varios y asignarlos a una semana (ano, mes y semana), o uno a uno con contracuenta, codigo financiero, destino y nomina. Diciembre se puede pagar en enero o febrero. Solo periodos contables abiertos.
- Modulo: tesoreria
- Clase: ui
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [20:16]
- Cita corta: "si tu filtras por egresos te permite seleccionar varios egresos y asociarlo a una semana... tiene que ser un periodo que este abierto"

### T-13
- Enunciado: En la nomina, despues de 30 dias el equipo propone un subestado "critico"; antes, solo "atrasado". Al pagar, no deben quedar critico ni atrasado: queda pagada y, si corresponde, aplazada. Hay que preguntar si el critico les sirve.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [22:25]
- Cita corta: "despues de 30 dias te muestra este subestado como critico... deberia quedar solamente como pagada y aplazada"

### T-14
- Enunciado: La nomina se ve por semana, con indicadores de la semana y del periodo. Un filtro de todos los pendientes de pago, de todas las semanas, queda como punto para Lupe.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Carlos y Sergio
- Fuente: transcripcion-2026-09-21-interna-sergio-jose-diego.md [26:07]
- Cita corta: "que puedan filtrar todos los que esten pendientes de pago... deja ese punto notado del filtro, a ver si le va a gustar"

### T-15
- Enunciado: Lupe pidio una apertura de los montos disponibles (saldo inicial), por banco y por moneda.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Lupe
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [12:24]
- Cita corta: "la Lupe lo habia dicho que necesitaban tener como una apertura de los montos... Es por banco"

### T-16
- Enunciado: En el flujo de caja, cada concepto tiene total abajo (como en la imagen que mando Mario). Un check deja los totales de ese concepto. Moneda extranjera se convierte a pesos al hacer clic; al pasar el mouse se ve el monto original. Hay filtro por moneda.
- Modulo: tesoreria
- Clase: ui
- Voz: cliente
- Quien: Mario (imagen); "lo que habian pedido" para la conversion
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [13:41]
- Cita corta: "la imagen que mando Mario, aqui por cada concepto tiene un totalizado abajo... monedas extranjeras, te lo convierta a pesos"

### T-17
- Enunciado: Falta exportar el flujo de caja a Excel. Hay que preguntar si el detalle con totalizado lo necesitan en Excel.
- Modulo: tesoreria
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [14:44]
- Cita corta: "Exportacion a Excel no tenemos nada... preguntemoslo si este detalle... lo necesitas en el portal de Excel"

### T-18
- Enunciado: En la nomina se puede aplazar a otra semana o volver a la fecha original. El equipo dice que una de esas acciones ("volver a emision") hay que eliminarla. En cartola falta poder seleccionar mas de un movimiento; los saldos ya estan por banco y moneda.
- Modulo: tesoreria
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [16:28]
- Cita corta: "ese volver a emision... este no, es el que hay que eliminarlo... seleccionar mas de uno... saldo por cada banco y por moneda"

### T-19
- Enunciado: En administracion se crean conceptos y en codigos financieros se asocia el concepto. Al contabilizar la cartola, el codigo financiero arma el flujo de caja por concepto.
- Modulo: tesoreria
- Clase: regla
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [41:34]
- Cita corta: "creaste una pantalla de conceptos... en codigos financieros tu lo asocias el concepto... te va a construir tu flujo de caja"

### T-20
- Enunciado: Lupe es quien ve tesoreria. El equipo quiere una reunion solo de tesoreria con ella, separada de contabilidad.
- Modulo: tesoreria
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-14-interna-manana.md [35:46]
- Cita corta: "coordinar una reunion con la Lupe, que es la nina que se encarga de tesoreria... una reunion exclusiva de eso"

---

## Admin

### A-01
- Enunciado: En el mantenedor de clientes falta el correo. El equipo plantea una pestana de contacto (persona y correo) y, para no atrasar, deja por ahora solo el campo correo.
- Modulo: admin
- Clase: dato
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [20:23]
- Cita corta: "Te falta el campo correo... una pestanita que sea de contacto... deja asi como aqui agregarle el campo correo"

### A-02
- Enunciado: En administracion tienen que poder configurar su servidor de correo (SMTP) para los envios.
- Modulo: admin
- Clase: pedido
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-03-interna-carlos-sergio.md [22:19]
- Cita corta: "dentro de la administracion teneis que dejar para que ellos puedan configurar su SBTP... un servidor de correo"

### A-03
- Enunciado: Los indicadores del Banco Central deben tener, mas adelante, historial y seleccion de monedas. La API del Banco Central caduca cada ano. Decision: no dejar que el cliente ingrese la API key; queda como soporte anual.
- Modulo: admin
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-10-interna-carlos-sergio.md [12:24]
- Cita corta: "puedan tener el historial historico... puedan seleccionar monedas... yo lo dejaria como soporte"

### A-04
- Enunciado: En la orden de compra, la cadena de aprobacion segun el monto se muestra abajo, a todo el ancho: si son cuatro personas, las cuatro; si es una, esa. No mezclada al lado de los montos.
- Modulo: admin
- Clase: ui
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [20:37]
- Cita corta: "si el monto entra dentro de una cadena de aprobacion, que muestre la cadena bajito... ocupa ahi todo el espacio"

### A-05
- Enunciado: El admin ve la bandeja completa. Un usuario normal ve, segun el monto, quienes deben aprobar, y en acciones puede aprobar o rechazar.
- Modulo: admin
- Clase: regla
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-2026-09-23-interna-carlos-sergio.md [20:01]
- Cita corta: "si yo fuera un usuario normal, me saldria, dependiendo del monto, quienes son los que tienen que aprobar... aprobar o rechazar"

---

## Otro

### O-01
- Enunciado: Maria Jesus queria salir a productivo en septiembre (y antes, en agosto con IOFactura), pero esta frenada por el contrato con Cristian y por la habilitacion de YoFacturo. Dice que activarlo les toma uno o dos dias.
- Modulo: otro
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-2026-09-15-gosocket-kickoff.md [09:08]
- Cita corta: "hubiesemos salido a productivo ahora en septiembre pero como tenemos que estar en marcha en el tema de los contratos"

### O-02
- Enunciado: En productivo del portal, lo mas probable es que solo Maria Jesus pueda agregar gente. Pablo le da acceso a ella y ella administra al resto.
- Modulo: otro
- Clase: regla
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [17:49]
- Cita corta: "en productivo, Maria, lo mas probable es que solamente usted tenga el acceso a agregar gente"

### O-03
- Enunciado: El sandbox de GoSocket tiene menos recursos y responde lento. Emitir con fecha del dia para no perder el documento en el filtro. Para ver el error: XML construido contra el archivo de integracion en crudo, y las notas del documento.
- Modulo: otro
- Clase: integracion
- Voz: proveedor
- Quien: Pablo
- Fuente: transcripcion-reunion-gosocket-qa.md [07:35]
- Cita corta: "el ambiente de ECUA, tiene menos recursos... emitan con la fecha del dia... descarga del XML... y en el archivo de integracion... en crudo"

### O-04
- Enunciado: El 06/10 Cristian sigue sin responder el contrato. Pablo va a reenviar el correo para activar al menos IoFacturo. Las pruebas de emision de factura, emitida y recibida, van bien; los duplicados de descripcion ya se corrigieron.
- Modulo: otro
- Clase: integracion
- Voz: proveedor
- Quien: Pablo; Maria Jesus confirma que no hay respuesta
- Fuente: transcripcion-2026-10-06-gosocket-contratistas.md [07:52]
- Cita corta: "algun avance... Cristian respecto al correo. No, no me ha respondido nada... activamos por lo menos Iofacturo"

### O-05
- Enunciado: Maria Jesus se va de vacaciones; la reunion siguiente de GoSocket la lidera Mario. Pablo insiste con el area comercial si no hay contrato en una o dos semanas. Querian respuesta hacia octubre.
- Modulo: otro
- Clase: dato
- Voz: proveedor
- Quien: Pablo; Maria Jesus informa las vacaciones
- Fuente: transcripcion-2026-09-15-gosocket-kickoff.md [06:21]
- Cita corta: "la idea es tener respuesta de aqui a octubre... la reunion de la proxima semana la va a liderar Mario"

---

## Que quedo decidido por el equipo y que quedo bloqueado

### Decisiones del equipo (no son palabra del cliente)

- Orden de venta: Guardar valida stock y vuelve al listado. Facturar solo en Emitir. Sin cuenta contable en la OV. Cuentas por item al facturar y al contabilizar en el libro de ventas. El libro de ventas no lista OV.
- Nota de credito en el libro: tres tipos (anulacion total, texto, montos). Codigos de referencia 1, 2 y 3. La NC rebaja. Anulacion total no pide mas datos. Estado "anulada" visible en la grilla.
- PDF y folio dentro del ERP. Folio de GoSocket en la primera columna. Tracking con usuario, fecha y correo. Alertas solo al quedar emitido.
- Correo automatico al cliente si hay casilla, reenvio, y SMTP en administracion. La API key del Banco Central no la carga el cliente: queda como soporte anual.
- Aprobaciones solo de compras. Factura recibida con OC no aprobada no se acepta.
- Libro de compras: sync desde GoSocket, pestanas pendiente / aceptado / rechazado, sin carga de documentos ajenos al RUT. Contabilizar compras en pausa hasta cerrar ventas. Se eliminan editar y anular. Aceptacion y rechazo automaticos no van por ahora; si una alerta por RUT.
- Solo documentos aceptados y con fecha de vencimiento entran a la nomina. Si falta la fecha, se pide al aceptar. Aplazar cambia la semana de compromiso, no el vencimiento del DTE.
- Egreso de cartola se asocia a la nomina. Ingresos no. Flujo de caja por concepto, codigo financiero y periodo, con total del periodo.
- Cadena de OC visible abajo, a todo el ancho, segun el monto.
- Grupos de aprobacion de proforma y de OC separados (06/10, Sergio).
- Proforma notificada al proveedor (no una aprobacion del proveedor dentro del sistema). Solo esas se asocian en compras.
- El 23/09 el equipo, citando un video de Maria Jesus, habia dejado la proforma fuera de la cadena (pasa a OC y la OC se aprueba). El 06/10 Maria Jesus dice lo contrario en la sala: el ingreso y la proforma si pasan por aprobacion de jefatura. La frase posterior del cliente pisa esa decision interna.
- Salida de venta no se edita. Guia para movimiento entre bodegas.

### Bloqueado por GoSocket o por el cliente

- Contrato y YoFacturo / IOFactura: Cristian no responde (QA de agosto, kickoff 15/09 y 06/10). Maria Jesus no puede salir a productivo. Pablo reenvia el correo. Habilitacion estimada en uno o dos dias una vez firmado.
- Representaciones graficas: Pablo las debe, a partir de lo que mando Maria Jesus. Recien despues se valida la data. Regenerar PDF antiguo solo en el portal.
- Plan de pruebas de 3 o 4 documentos por tipo, pedido el 06/10, todavia no enviado.
- Guia de despacho recibida: Pablo dice que deberia verse en recibidos; falta la prueba entre las dos empresas.
- Factura de exportacion: el 07/09 Carlos dice que GoSocket aun no respondia. El 14/09 queda pendiente mandar el XML a Pablo.
- Carga historica (Almaweb / Acepta / Mago, del orden de 1000 a 1200): Pablo la deja para el final y ofrece otra reunion. El SII baja de a 20.
- Credencial de produccion: el equipo no emite en productivo; el sandbox lo crea GoSocket sin contrato.
- Como enlazar la OC si el XML no trae la referencia: pregunta abierta al cliente (23/09).
- Si rechazar solos las facturas sin referencia a OC: lo tienen que decidir ellos (22/09).
- Fecha de vencimiento cuando no viene: el mecanismo esta propuesto; falta que confirmen donde la marcan.
- Centro de costo, elemento y area en el plan de cuentas versus en la venta: pregunta a Maria Jesus o a Mario. Mario quedo con las tarjetas de contabilidad y no habia reemplazo definido.
- Flujo de caja: separar por banco (filtro o pestana), total unico en pesos, Excel, y el subestado "critico" a los 30 dias: pendientes de Lupe.
- Apertura por banco y moneda la pidio Lupe; el calce fino de varios egresos de una nomina quedo a medias el 14/09.
- Cheque, y si una transferencia paga dos facturas: no se los han dicho.
- Cobranza: no saben si la hacen.
- Contratistas: el 21/09 y el 23/09 faltaba validar traspaso y cierre, auditoria, si emiten factura de compra, KPI y exportacion. El 06/10 Maria Jesus cierra una parte (ficha, ingreso, proforma, no parcializar, aprobacion, envio). Sigue abierto el cierre semanal y el match fino con compras.
- Especialidad unica o multiple del contratista: el video la pedia y el equipo tiende a quitarla.
- Devolucion de fruta a merma o a bodega: pregunta abierta.
- Carga masiva CCC: implementada, no aprobada, falta documento SII.
- Anular DTE emitidos fuera del ERP: carga masiva, dejada para despues.
- Rodrigo (encargado de contratistas que mostro AgroSmart) no esta en estas salas. El 21/09 piden reunion con el.
