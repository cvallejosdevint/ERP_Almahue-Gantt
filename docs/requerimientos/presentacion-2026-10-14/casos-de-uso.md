# Casos de uso - presentacion 2026-10-14

Fuente de esta sala: `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md`.

La transcripcion manda. Una minuta, si existiera, seria solo indice. Carlos y Sergio son hipotesis: un caso entra si lo dice el cliente (Agustin, Maria Jesus, Lupe, Mario, Rodrigo, Fran/Lafran) o si el cliente confirma la frase. Si la voz no trae nombre, se dice y se usa la pista de la sala.

Presentes desde [02:21], dicho por Maria Jesus: Mario, Rodrigo, Lafran y ella. Antes de [02:15] la grabacion es interna (Diego, Jose, Carlos, Sergio) y no genera casos. La visita de la semana del 26 y el acceso a Trello tampoco.

Empresa de lectura, cuando alguien contraste con el sistema: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`, API `http://localhost:3001/api/v1`.

No se armo ningun caso con el Word ni con `especificacion-otro-modelo.txt`. Si una frase solo estaba ahi, no entro.

## Reuniones leidas

| Archivo | Que es | Para esta sala |
|---|---|---|
| `transcripcion-2026-10-14-presentacion.md` | Sala con Maria Jesus, Mario, Rodrigo y Lafran | Fuente de los casos |
| `transcripcion-2026-10-14-jose-sergio.md` | Interna Jose y Sergio, sin cliente, el mismo dia y antes de la presentacion | No aplica. No es fuente. Un tramo trata a la madre como si ya estuviera contabilizada; la sala de la tarde dijo que la madre no mueve nada |
| `transcripcion-2026-10-06-gosocket-contratistas.md` | Pablo (GoSocket) y Maria Jesus. El propio archivo avisa que no es fuente de requisitos | No genera casos nuevos. Corrobora el modulo de contratistas que ella misma explico (proforma = orden del modulo, varias proformas a una factura, envio al contratista). La duda de si la guia recibida llega por GoSocket quedo para validar con Pablo y esta sala no la cerro |
| `transcripcion-2026-10-01-reunion-cliente.md` | Hay cliente. El archivo avisa que no es fuente de requisitos | No pisa a la tarde del 14/10. El 01/10 la guia solo entraba a bodega y la factura se asociaba a la orden. El 14/10 la guia hace nacer la hija. Gana el 14/10 |
| `transcripcion-2026-09-24-reunion-cliente.md` | Lupe, Fran y Sigrid | Corrobora que editar la madre, para mas o para menos, vuelve a aprobacion. Choca en el tramo automatico por monto: el 24/09 se dibujo exento / jefatura / gerencia. El 14/10 Maria Jesus, que ese dia estaba de vacaciones cuando se tomo esa decision, lo rechazo. Gana el 14/10. El multi-item con varios centros de costo quedo sin ejemplo real. El "historial" del rechazo quedo en "podriamos" |
| `transcripcion-2026-09-23-dudas-cliente.md` | Mario y Lupe. Agustin no estuvo. Maria Jesus estaba de vacaciones | No es fuente de esta sala. El bosquejo (proforma como la orden del modulo; la hija se contabiliza y la madre no) no choca. El detalle de líneas, centros de costo y quien crea la hija en contabilidad lo cerro despues la sala del 14/10, y de otro modo: la hija nace en insumos con la guia |
| `transcripcion.md` (Reu1) | As-is de Agrosoft | No es requisito nuevo. Muestra la imputacion que Maria Jesus repitio el 14/10: costo del trabajo y facturas por recibir contratistas |
| `transcripcion-reunion2.md` (Reu2) | As-is de Agrosoft, con el dolor del tarifario | No es requisito nuevo. Explica por que el 14/10 preguntaron por el precio y por que una factura necesita mas de una proforma. Agrosoft dejaba una proforma por mes |
| `transcripcion-reunion3.md` (Reu3) | Recorrido del sistema nuevo sobre capturas de Agrosoft. El cliente nombra "traspaso contable y cierre de mes" | No agrega casos que la sala del 14/10 no haya vuelto a decir. El tipo de cambio en esa pantalla no se repitio el 14/10 |
| `transcripcion-reunion4.md` | Sala anterior de aprobaciones y proformas | No pisa este flujo. Si chocara con Reu6, ganaria Reu6. En madre, hija y cierre de contratistas no hay choque que mueva estos casos |
| `transcripcion-reunion5.md` | Interna Carlos y Sergio | No cuenta. No hubo cliente |
| `transcripcion-reunion6.md` | Reu6 | No aplica a madre/hija ni al cierre de contratistas. Carlos (hipotesis) nombra aprobaciones de comercial; esta sala no reabre la orden de venta. "Proforma" ahi, en un tramo, es para vender, no el documento de contratistas |
| Internas (`2026-08-19`, `2026-08-20` manana, `2026-09-03`, `2026-09-07`, `2026-09-10`, `2026-09-14` manana, mediodia y tesoreria, `2026-09-21`, `2026-09-22`, `2026-09-23` Carlos-Sergio, `2026-10-13` Carlos-Sergio, GoSocket kickoff y QA) | Sin cliente, o el cliente no cierra este flujo | No aplican como fuente |

Otras salas con cliente que tocan el mismo tema solo se citan abajo cuando la frase es del cliente y no choca con el 14/10. No se convirtieron en casos propios.

## Casos

### CU-01. Al elegir la labor, la actividad sale sola

- Quien: voz sin nombre. Pista: estan en parametrizacion de contratistas, mirando el ingreso. La frase "antes teniamos el problema" es de quien carga el modulo. Carlos acaba de preguntarle a Rodrigo. En [16:53] otra voz, tambien sin nombre, dice que el area agricola es la que mas usa contratistas y que el ingreso les tiene que quedar comodo.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [07:29] y [16:24]. El dolor de tener que recordar a que labor pertenece la actividad esta en el as-is `transcripcion-reunion2.md` [01:45:51].
- Que pasa: en el ingreso diario se elige la labor y la actividad asociada aparece sola. Antes habia que buscar cual labor correspondia.
- Documento: ingreso diario de contratistas.
- Que debe quedar: la actividad no se busca a mano. Sale de la labor parametrizada. El ingreso es el que usa el area agricola.

### CU-02. El ingreso diario lleva el detalle; el gasto va a una sola cuenta

- Quien: Maria Jesus. Carlos le pregunta donde va el centro de costo y ella corrige la cuenta. En [14:27] habla en primera persona ("cuando yo le asocio la factura").
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [10:41], [10:55], [13:55], [14:04]. El as-is de la misma imputacion esta en `transcripcion.md` [02:51:40].
- Que pasa: hoy la cuenta del contratista va a mano de obra contratista. El detalle se lee por centro de costo, labor y actividad. Ella dice que ambos van en el ingreso diario. Carlos cree que la cuenta se asigna por linea al armar la proforma. Ella lo corrige: en el ingreso diario se asocia la labor, no una cuenta por linea. En la proforma queda el detalle del mes por labor, centro de costo y monto, y todo eso va a la cuenta mano de obra contratista.
- Documento: ingreso diario y proforma.
- Que debe quedar: centro de costo, labor y actividad quedan en el ingreso diario. La proforma no pide una cuenta distinta por linea. El gasto de esas lineas es la cuenta mano de obra contratista.

### CU-03. Varios ingresos diarios arman una proforma

- Quien: Maria Jesus confirma el agrupado. Carlos describe la pantalla y ella dice "Exacto", y sigue ella con el jefe de campo.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [12:50] y [13:07]. El 06/10 ella ya lo habia dicho: se seleccionan las faenas diarias y de ahi sale la proforma (`transcripcion-2026-10-06-gosocket-contratistas.md` [13:46], [17:45], [19:54]).
- Que pasa: los ingresos diarios de un contratista se eligen y se agrupan en una proforma. Pueden ser varios. No hace falta una proforma por cada dia, salvo el caso del dia suelto del CU-25.
- Documento: proforma de contratistas, armada desde ingresos diarios.
- Que debe quedar: la proforma es el agrupado de los ingresos diarios elegidos de ese contratista. Esos ingresos ya no quedan libres para otra proforma.

### CU-04. La proforma la aprueba el jefe de campo

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [13:08]. El 06/10 ella cerro que la que pasa por aprobacion de jefatura es la proforma, no cada ingreso suelto como flujo definitivo (`transcripcion-2026-10-06-gosocket-contratistas.md` [24:05] y [29:48]). En esa sala, un momento antes, dijo que el ingreso diario se iba a jefatura; despues, al ver la pantalla, dejo la aprobacion en la proforma. Vale lo que quedo y lo que repitio el 14/10.
- Que pasa: agrupados los ingresos, la proforma se aprueba. Quien aprueba es el jefe de campo. Con eso se da por hecho que las labores se hicieron en la semana que corresponde.
- Documento: proforma.
- Que debe quedar: sin aprobacion del jefe de campo la proforma no queda lista para el traspaso del CU-05. La aprobacion es de la proforma.

### CU-05. El asiento del mes es uno, al cierre, y suma las proformas aprobadas

- Quien: Maria Jesus. Le recuerda a Carlos el cierre mensual. Carlos pregunta si se contabilizan una a una y ella dice que no.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [11:19], [11:45], [11:58], [13:20], [13:40]. El nombre del menu ya lo habia usado el cliente en `transcripcion-reunion3.md` [04:25:21] y [04:26:30]: se centraliza el mes, no contratista por contratista.
- Que pasa: ella cierra el mes y recien ahi se traspasa a contabilidad. Entran las proformas aprobadas de ese mes. No se contabiliza cada proforma al aprobarla. El asiento es uno solo, totalizado.
- Documento: cierre de mes de contratistas y su asiento.
- Que debe quedar: aprobar una proforma no genera el asiento. Al cerrar el mes, las proformas aprobadas de ese mes salen en un asiento centralizado.

### CU-06. El gasto queda en el mes de la proforma

- Quien: Maria Jesus. Carlos le pregunta si el traspaso es solo de las aprobadas o tambien de las ya asociadas a factura.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [12:06].
- Que pasa: la proforma puede quedar en octubre y la factura llegar con fecha de noviembre. El gasto de octubre tiene que reconocerse en octubre.
- Documento: proforma aprobada y factura recibida del contratista.
- Que debe quedar: el mes del gasto es el mes de la proforma aprobada. No se espera la fecha de la factura para reconocer ese gasto.

### CU-07. Mano de obra contra facturas por recibir, y despues la factura contra el proveedor

- Quien: Maria Jesus, en primera persona.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [14:27]. Misma mecanica en el as-is `transcripcion.md` [02:51:40] y en `transcripcion-reunion2.md` [02:56:10] y [03:03:10].
- Que pasa: el asiento de las proformas deja mano de obra contratista contra facturas por recibir contratista. Cuando ella asocia la factura, facturas por recibir queda contra el proveedor. Con esas dos partes, el gasto queda contra el proveedor.
- Documento: asiento del cierre y factura recibida del contratista.
- Que debe quedar: centralizar no usa la cuenta del proveedor. Asociar la factura recibida saca facturas por recibir y deja al proveedor. El gasto no se duplica.

### CU-08. El cierre es un menu bajo auditoria

- Quien: voz de la clienta a la que Carlos le repite el nombre. Pista: acaba de explicar el cierre y Carlos le pregunta como dejar el menu. Ella lo nombra.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [15:04], [15:21], [15:30].
- Que pasa: en contratistas, abajo de auditoria, tiene que haber traspaso contable y cierre de mes. Ahi se informa que mes se cierra y se hace el traspaso.
- Documento: menu de contratistas.
- Que debe quedar: el cierre no es un boton suelto en cada proforma. Es el menu "Traspaso contable y cierre de mes", bajo auditoria, y el usuario dice que mes cierra.

### CU-09. Al traspaso entran todas las aprobadas; la pendiente no es gasto

- Quien: voz sin nombre, de quien lleva el registro de gasto ("nuestro registro de gasto"). Pista: Carlos pregunta si el listado es todas las proformas o una por contratista, y si la pendiente de aprobacion pinta algo.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [20:19] y [20:28].
- Que pasa: el listado del traspaso muestra todas las proformas aprobadas de contratistas, no una sola por contratista. Mientras esta pendiente de aprobacion, es un dato informativo. No entra al registro de gasto.
- Documento: listado del traspaso contable.
- Que debe quedar: se listan todas las aprobadas. Una pendiente se puede ver, y no se contabiliza.

### CU-10. La proforma aprobada se puede avisar al contratista por correo

- Quien: voz sin nombre. Pista: acaban de ver "notificar a contratista" y el correo con el documento, y responden "Buenisimo, si". Carlos nombra a Mario justo despues, para la configuracion del correo, y Mario no agrega otra regla.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [18:24] y [19:22]. El 06/10 Maria Jesus dijo que la proforma se le envia al contratista para que emita la factura (`transcripcion-2026-10-06-gosocket-contratistas.md` [25:57] y [27:56]).
- Que pasa: con la proforma lista, notificar al contratista envia el correo. El aviso puede llevar el documento.
- Documento: proforma.
- Que debe quedar: existe el aviso por correo al contratista, con el documento de la proforma. Unir o no los dos botones que Carlos mostro no quedo dicho por el cliente.

### CU-11. El correo de la orden de compra es interno

- Quien: voz sin nombre. Pista: estan en la plantilla de compras y la frase es de quien se manda el correo entre el departamento ("nosotros nos mandemos"). Despues, al ver copia, externos y adjuntos, la misma reaccion es "Buenisimo" [26:03].
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [22:22] y [26:03].
- Que pasa: el correo de la orden de compra no es el aviso al proveedor. Es informacion interna, de un area a otra.
- Documento: orden de compra, en el envio de correo.
- Que debe quedar: el destinatario previsto del correo de compras es un usuario interno del departamento. La pantalla que Carlos mostro para copiar a externos no la pidio el cliente en esta sala.

### CU-12. La madre es la negociacion; se contabiliza la hija

- Quien: Maria Jesus. Sergio la nombra en [29:50]. Ella responde el uso de la madre y, mas tarde, "la madre solamente informativa".
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [29:09], [34:43], [40:01], [45:49]. El 01/10 el cliente ya habia dicho que la madre es informativa y solo de insumos (`transcripcion-2026-10-01-reunion-cliente.md` [47:20]). Esa parte no choca.
- Que pasa: la orden de compra madre sirve para negociar con el proveedor. No mueve stock ni contabilidad. Lo que se contabiliza es la hija.
- Documento: orden de compra madre y orden de compra hija.
- Que debe quedar: la madre no se contabiliza. La hija si puede contabilizarse. La madre no se asocia en el libro de compras como si fuera la orden que calza la factura.

### CU-13. La hija nace al recepcionar la guia en insumos

- Quien: Maria Jesus. Sergio propone que la hija nazca al asociar una factura parcial. Ella deja otro flujo: la hija se hace con la guia, en bodega.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [35:06], [36:47], [37:43], [37:50], [39:35], [39:56], [40:05]. Choca con `transcripcion-2026-10-01-reunion-cliente.md` [56:33], donde la guia solo actualizaba bodega y la asociacion a la orden esperaba la factura. Gana esta sala.
- Que pasa: primero existe la madre, que es informativa. El material entra a bodega con guia de despacho. Esa guia, asociada a la madre, genera la orden de compra hija. La hija no la crean a mano desde el libro de compras. La guia es solo bodega. Insumos es el unico modulo de este flujo.
- Documento: guia de despacho recibida, orden de compra madre y orden de compra hija.
- Que debe quedar: sin madre no hay donde asociar la guia. Al recepcionar la guia contra la madre, queda creada la hija por el parcial de esa guia. El libro de compras no crea la hija.

### CU-14. Varias guias del mes y una factura: en compras se asocian las hijas

- Quien: Maria Jesus. Sergio le repregunta si las diez guias quedan en la madre y si despues la factura toma las hijas. Ella dice que si, y corrige: no se asocia la guia, se asocia la orden de compra hija.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [35:15], [38:21], [39:08], [40:12], [41:01].
- Que pasa: en el mes pueden llegar varias guias y una sola factura. Ejemplo de ella: diez guias y una facturacion. Al asociar la factura en el libro de compras tiene que salir el listado de lo que llego de ese proveedor, no un calce solo por monto. Lo que se marca son las hijas ya nacidas de esas guias.
- Documento: factura recibida de proveedor, en el libro de compras, y las ordenes de compra hija.
- Que debe quedar: una factura puede tomar varias hijas del mismo proveedor. Esas hijas ya existen porque hubo guia. La guia no es la linea que se asocia en el libro de compras.

### CU-15. Las guias se ven en insumos, no en el libro de compras

- Quien: Maria Jesus. Dice "solo insumos bodega" y, cuando Carlos pregunta si insumos lleva libro de compras, responde que no: es el libro de guia.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [37:43], [50:28], [51:12], [51:26].
- Que pasa: insumos muestra las guias de despacho recibidas y ahi se asocian a la madre para crear hijas. El libro de compras no es el lugar de la guia. Cuando la hija ya esta y se asocia a la factura, recien pasa al libro de compras.
- Documento: libro de guias en insumos bodega, y libro de compras.
- Que debe quedar: insumos tiene libro de guias y no tiene libro de compras. El libro de compras no lista la guia para asociarla.

### CU-16. Insumos ve madre e hija; compras solo ve la hija lista para contabilizar

- Quien: Maria Jesus en el tramo en que separa los mundos ("solo insumo", "tienen que esperarme": contabilidad no toma lo que aun no esta recepcionado). La visibilidad la va cerrando la sala entre [46:58] y [55:58].
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [46:58], [47:17], [49:56], [54:42], [55:16], [55:53], [55:58].
- Que pasa: insumos es un mundo aparte. Ahi se ve la madre y la hija. A compras no pasan las madres para asociarlas. En compras solo se ven las hijas ya recepcionadas y listas para contabilizar. Una orden pendiente o solo aprobada, si no esta recepcionada, en ese modulo no existe. Quien solo tiene insumos, por ejemplo el administrativo de abastecimiento, igual ve sus ordenes en insumos. Compras puede ver la hija que salio de insumos, no el trabajo pendiente de bodega.
- Documento: orden de compra madre, orden de compra hija, libro de compras.
- Que debe quedar: la madre no aparece para asociar en compras. La hija aparece en compras solo si ya fue recepcionada. Insumos muestra madre e hija. El perfil de insumos no depende de entrar a compras para ver lo suyo.

### CU-17. Servicio es una a una; insumos llega por partes

- Quien: Maria Jesus. Carlos pregunta como se llama el otro tipo y la sala dice "servicios". Ella distingue los dos y dice que si a un flujo de aprobacion por tipo.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [52:10], [52:21], [52:40].
- Que pasa: hay orden de compra de insumos y orden de compra de servicios. La de servicio se aprueba y se recepciona, y es siempre una a una. La de insumos es la que llega en partes y usa madre e hija.
- Documento: orden de compra, con tipo servicio o insumos, y su flujo de aprobacion.
- Que debe quedar: el flujo de madre, guia e hija es solo insumos. La de servicio no se parte en hijas. La regla de aprobacion se puede distinguir por esos dos tipos.

### CU-18. La madre la crea el jefe; la hija, el administrativo

- Quien: Maria Jesus. Carlos dice que le habian contado que el jefe genera la orden y ella confirma. Despues cierra los dos roles.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [52:42], [53:15].
- Que pasa: una sola persona tiene la potestad de crear la madre: el jefe. La hija la genera el administrativo, al recepcionar en insumos.
- Documento: orden de compra madre y orden de compra hija.
- Que debe quedar: crear la madre no esta abierto a cualquiera del grupo. Crear la hija es del administrativo de insumos, en la recepcion de la guia, no un alta manual en compras.

### CU-19. No hay monto que se salte la aprobacion

- Quien: Maria Jesus. Estaba de vacaciones cuando se dejo la aprobacion automatica y dice que no esta de acuerdo.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [32:29], [32:52], [33:38]. Choca con `transcripcion-2026-09-24-reunion-cliente.md` [04:24] y [06:11], donde se dibujo un tramo automatico. Gana esta sala.
- Que pasa: ella recibe muchas facturas de 10.000 o 15.000 pesos, del orden de 300 en el mes, y por eso se habia pensado un automatico por monto. Ese recorte tambien dejaria afuera almuerzo o libreria, que no deberian aprobarse solos. Pide que hasta un monto de 5 pesos pase por aprobacion. Carlos propone que no exista un "no pasa por la cadena" y que se respete el primer eslabon desde cero. Ella dice que lo dejaria todo con aprobacion.
- Documento: orden de compra, en su cadena de aprobacion.
- Que debe quedar: no hay tramo exento por monto. Toda orden entra a la cadena, desde el primer eslabon. Los topes de ejemplo de la demo (5.000, 10.000, o un primer tramo hasta 500.000) no los fijo ella en esta sala.

### CU-20. Subir o bajar la madre vuelve a pasar por aprobacion

- Quien: Maria Jesus. "Yo dejaria edicion, sea para abajo o para arriba, con aprobacion."
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [32:03], [41:07], [49:39]. El 24/09 Lupe y Fran ya habian dicho que pasar el monto o quedar corto vuelve a la cadena (`transcripcion-2026-09-24-reunion-cliente.md` [21:29] y [22:14]). No choca.
- Que pasa: la madre se aprueba una vez, porque el real lo traen las hijas. Si falta cupo para recepcionar una guia, abastecimiento no la recibe: pide que le modifiquen la madre. Esa edicion, para arriba o para abajo, pasa por aprobacion. El control del cupo es en la recepcion, no al vincular en compras.
- Documento: orden de compra madre.
- Que debe quedar: la aprobacion inicial de la madre no se repite en cada hija. Si la madre se edita, el monto nuevo recorre la cadena, baje o suba. Sin cupo, la guia no se recepciona hasta esa modificacion.

### CU-21. Cerrar la madre por menos se hace en insumos

- Quien: Maria Jesus. El ejemplo de las cajas es de ella. Carlos pregunta donde se cierra y ella dice que en insumos.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [43:59], [44:30], [45:01], [46:02].
- Que pasa: la madre sigue abierta mientras falta por llegar lo negociado. Si estimaron fruta de mas y al proveedor le dicen que de 100 cajas necesitan 50, ahi se cierra. Pueden cerrarla cuando el monto recibido es menor. El cierre es en insumos. Lo que se asocia con guia o factura sigue al libro de compras. La aprobacion de ese cierre es la del CU-20: sirve para dejar la madre cerrada.
- Documento: orden de compra madre, en insumos.
- Que debe quedar: cerrar por una estimacion menor es una accion de la madre en insumos, no en el listado de compras. La madre cerrada no sigue recibiendo guias por el saldo que se corto.

### CU-22. El pendiente de la madre se mira en insumos

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [47:48], [48:13].
- Que pasa: hay que ver cuanto le falta a la madre. Eso se ve en insumos. Quien calza la factura con la orden de compra solo necesita que calcen. No revisa si llego material o si falta por llegar.
- Documento: saldo de la orden de compra madre, y calce en el libro de compras.
- Que debe quedar: el pendiente de la madre esta en insumos. El libro de compras no muestra ese saldo como condicion para asociar la hija con la factura.

### CU-23. Los reportes contables salen en PDF, y el estado de resultados tambien en Excel

- Quien: voz sin nombre. Pista: le hablan a Carlos al terminar la muestra de contabilidad y piden formato PDF. Responden "formato de todo". Otra voz, tambien sin nombre, pide ver si el estado de resultados se descarga a Excel. Carlos dice que no estaba y que van a dejar Excel y PDF. La respuesta es "Ah, ya".
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [57:42], [58:12], [58:54], [59:03].
- Que pasa: en pantalla estaban comprobantes, libro diario, libro mayor, balance de ocho columnas y estado de resultados. Piden PDF de todos. Del estado de resultados piden poder descargar Excel, y aceptan que tambien quede el PDF.
- Documento: reportes de contabilidad nombrados en la muestra.
- Que debe quedar: esos reportes se exportan a PDF. El estado de resultados, ademas, se exporta a Excel. Los campos de cabecera que una voz de implementacion dijo haber visto siempre (empresa, nombre del reporte, periodo) no los dicto el cliente.

### CU-24. Con factura recibida, la proforma no se edita

- Quien: Maria Jesus. Pregunta ella. La respuesta "no deberia porque va a estar facturado" la hace suya: "Si, es que eso, no deberia porque va a estar facturado."
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [01:00:39] y [01:00:53].
- Que pasa: si la proforma ya esta asociada a una factura recibida, no se edita. La factura es el ultimo control para no quedar con una diferencia con el contratista.
- Documento: proforma asociada a factura recibida.
- Que debe quedar: proforma facturada queda cerrada a edicion. No se le cambian ingresos diarios ni montos.

### CU-25. El dia sin proforma no se corre de mes, y una factura puede tomar varias

- Quien: Maria Jesus. Lo dicen en la sala y en [01:03:01] lo atribuyen a ella.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [01:01:15], [01:02:22], [01:02:38], [01:02:48]. El 06/10 ella ya habia dicho que puede haber 10 proformas para una factura y que la proforma no se factura parcial (`transcripcion-2026-10-06-gosocket-contratistas.md` [13:54] y [25:14]). El as-is de Agrosoft, una proforma por mes, es el limite que estan dejando atras (`transcripcion-reunion2.md` [02:26:01]).
- Que pasa: si hay 29 dias con proforma y un dia trabajado sin proforma, ese dia no se va solo a septiembre ni a octubre ni queda eterno como dato suelto. Para control, ella hace una proforma de ese dia. Si no, el dia queda desfasado. Se trabaja contra proforma. Se pueden hacer varias proformas y despues juntarlas en la factura.
- Documento: ingreso diario sin proforma, proforma y factura recibida del contratista.
- Que debe quedar: un ingreso no pasa de mes por el cierre. Para entrar al mes necesita su proforma, aunque sea de un solo dia. Una factura puede asociar varias proformas. La proforma no se deja facturada a medias: se manda el detalle que el contratista tiene que facturar.

## Lo que la sala dejo abierto (no es caso)

- Precio cero en el ingreso diario. En [59:15] preguntan si se puede guardar sin precio. Carlos dice que hoy tira error. Preguntan si esta bien poder ingresarlo en cero. Una voz dice "hay que validar". Maria Jesus explica el trabajo a trato: la cantidad se conoce el dia de la labor y el precio, a veces, recien al cierre. Otra voz propone dejar un precio estimativo y editarlo despues. Nadie cerro "se permite precio 0". En el as-is (`transcripcion-reunion2.md` [01:45:51]) ese precio tardio ya era un dolor de Agrosoft. Sigue abierto.
- Editar ingresos cuando la proforma esta aprobada y todavia no tiene factura. En [01:00:17] ella lo pregunta. La respuesta mezcla "con solicitud" y "modificacion de la orden de compra". Ella dice "ya, ok" y sigue. Lo que si cerro es el CU-24, el caso ya facturado.
- Una frase que suena a nota de credito si hay diferencia antes de la factura ([01:01:09], "orden de credito"). No se entiende y nadie la cerro.
- Si "Traspaso contable y cierre de mes" es un menu o dos. Carlos lo pregunta en [15:38]. Lo que sigue, en [16:24], ya esta hablando de la labor y la actividad. El nombre y el lugar (bajo auditoria) si quedaron: CU-08.
- Una segunda modificacion de la madre, pedida a contabilidad, y una sola chance de cambio. Lo dice una voz sin nombre entre [30:44] y [31:36], y remata "como ella le dice". Maria Jesus no lo repite. Lo que ella si cerro es el CU-20 y el CU-21.
- Cabecera del PDF con datos de la empresa, nombre del reporte y periodo. Lo dice quien implementa ("siempre he visto"), en [58:16]. El cliente pidio el formato, no esos campos. El Excel "de las columnas de la grilla" tambien es de esa voz.
- Peso, dolar y yuan, y los vencimientos en el comprobante. Carlos dice en [56:51] que se los habian pedido. En esta sala nadie los vuelve a cerrar. El 24/09 hubo una conversacion de tipo de cambio que aqui no se repitio.
- Historial o tracking de por que se rechazo una orden. No esta en esta transcripcion. El 24/09 quedo en "podriamos dejarle un tracking" (`transcripcion-2026-09-24-reunion-cliente.md` [06:37]). No es caso.
- La hija pasa o no por la cadena. El 24/09 dijeron que la hija no pasa y que solo la edicion de la madre vuelve a aprobacion. El 14/10 Maria Jesus dijo que la madre se aprueba una vez (CU-20) y no repitio la frase de la hija.
- Varias lineas de la madre con centros de costo distintos, y como se reparte una factura parcial. El 24/09 lo dejaron esperando un caso real (`transcripcion-2026-09-24-reunion-cliente.md` [19:28]). Esta sala no lo cerro.
- Si la guia de la recepcion es la fisica o la que viene por GoSocket (codigo 52). Quedo para Pablo el 01/10 y el 06/10. Esta sala hablo de la guia en bodega y no distinguio el canal.
- Folio de la hija con guion 1, guion 2. Lo muestra Carlos en [28:50]. El cliente no lo cerro.
- El silencio del contratista como si hubiera aprobado la proforma. Maria Jesus lo dijo el 06/10 (`transcripcion-2026-10-06-gosocket-contratistas.md` [28:45]). El 14/10 no lo repitio. El aviso por correo si quedo: CU-10.
- Tipo de cambio en la pantalla de cierre de contratistas. Lo pidio el cliente en Reu3 (`transcripcion-reunion3.md` [04:28:21]). El 14/10 no lo repitio.
