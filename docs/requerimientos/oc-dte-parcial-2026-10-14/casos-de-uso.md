# Casos de uso: OC parcial, madre/hija y factura parcial

Fecha de lectura: 2026-10-14. Fuente primaria: transcripciones. El deck de Mario se usa solo como el documento que el armó. Si el deck y la sala chocan, gana la transcripcion.

Carlos y Sergio en la sala se tratan como hipotesis del equipo. Un caso entra aqui cuando el cliente lo dice, o cuando el cliente confirma la frase (por ejemplo "Exacto"). No hay caso inventado para tapar un silencio.

## 1. Reuniones leidas y quien era cliente

| Reunion | Archivo | Cliente en la sala | Que se busco |
|---|---|---|---|
| 2026-09-23 dudas | `docs/reuniones/transcripciones/transcripcion-2026-09-23-dudas-cliente.md` | Mario y Lupe. Agustin no estuvo (contingencia familiar). Maria Jesus de vacaciones. | Tramo 27:27 a 39:02, y el cierre 01:00:52. |
| 2026-09-24 | `docs/reuniones/transcripciones/transcripcion-2026-09-24-reunion-cliente.md` | Lupe, Fran y Sigrid. Mario presenta el diagrama (lo nombran en 13:09 y 34:05). | Factura parcializada, 14:22 a 30:07, y el comentario de 33:56. |
| 2026-10-01 | `docs/reuniones/transcripciones/transcripcion-2026-10-01-reunion-cliente.md` | Maria Jesus, Fran y Lupe. Mario habia avisado que estaria, pero al inicio estaba en otra reunion. | OC madre/hija (47:07) y guias vs factura (55:22). |
| 2026-10-06 GoSocket y contratistas | `docs/reuniones/transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md` | Maria Jesus. Pablo es de GoSocket, no es el cliente del ERP. | Proforma parcial frente a OC madre (24:45 y 36:27). |
| 2026-09-14 demo de avances | `docs/reuniones/transcripciones/transcripcion-2026-09-14-demo-avances.md` | Mario, Maria Jesus y Lupe. Esperaban a Agustin. | No hablan de OC hija ni de factura parcial. Si hablan de factura sin OC y de OC aun no aprobada (23:03 a 26:31). Queda en los casos limite, no como caso de hija. |

Deck, no es reunion: `docs/reuniones/compartidos/mj-contratistas-2026-10-06/texto-ppt-mario.md`, diapositivas 3 a 7 (en el texto, diapositivas 5 a 9: recepcion, llegada de factura, validaciones, registro contable, cierre con saldo).

Busqueda en el resto de transcripciones con cliente (parcial, hija, madre, recepcion, factura, DTE, GoSocket), sin armar caso porque no describen OC madre/hija ni factura parcial de compra:

- `transcripcion-2026-09-10-demo-cliente.md`: sin esas palabras en el sentido de OC.
- `transcripcion-2026-08-28-tesoreria-mj-lupe.md`: sin esas palabras.
- `transcripcion-2026-08-20-tarde-lupe-mario.md`: "parcial" es pago total, anticipo o parcial de una factura ya contabilizada. No es OC.
- `transcripcion.md` (as-is Agrosoft, Reu1): el informe de OC tiene estado "recepcionada parcial" o "recepcionada total". Es la pantalla actual, no el diseno madre/hija.
- `transcripcion-reunion2.md` [12:30:40]: el equipo dice que Sergio comento "facturas parciales". No hay caso dicho por el cliente.
- Reu5 (`transcripcion-reunion5.md`): no cuenta. No hubo cliente.
- Reu3, Reu4 y Reu6: no aparece factura parcial de OC ni OC hija.

Los locutores de Whisper casi nunca traen nombre. Donde el archivo no rotula la voz, se dice "locutor no rotulado" y se usa la pista de la sala (primera persona operativa, "nos ha tocado", "corrigeme Lupe", "Carlos, entendio").

## 2. Casos

### CU-01. El proveedor factura en partes una OC grande

- Quien: cliente, sala 23/09. Locutor no rotulado. "Nos ha tocado".
- Donde: `transcripcion-2026-09-23-dudas-cliente.md` [27:18] a [27:41], y el ejemplo [28:07] a [28:38].
- Que pasa: se emite una OC por un total (ejemplo de la sala: OC 100 por 100.000 y 10 cajas). El proveedor no factura el total junto. Puede facturar el 50% este mes y el otro 50% dos meses despues. En insumos les pasa seguido: la OC sale por un monto grande y la mercaderia llega por tandas.
- Documento: factura del proveedor, parcial. En el ejemplo viene asociada a la OC 100.
- Madre: queda como la OC grande de control (la 100).
- Hija: por cada factura parcial se genera una hija que neta con esa factura. La primera es la 100.1. Cuando llega el resto, la 100.2. Si al final cantidad y monto calzan, se cierra el caso.
- Contabilidad: la pregunta de la sala es como contabilizar para que no quede todo el tiempo parcializado. La respuesta de quien contabiliza esta en CU-02.
- Alerta si no calza: este caso es el camino feliz de la parcial. El descalce esta en CU-07 y CU-08.

### CU-02. Se recepciona la parcial, nace la hija y solo la hija se contabiliza

- Quien: cliente operativo, sala 23/09. Locutor no rotulado, en primera persona ("yo tengo mil cajas", "yo recepcione cien"). La sala le pide a Lupe que corrija el alcance de insumos [34:47]; el tramo no trae un "si" rotulado de Lupe.
- Donde: `transcripcion-2026-09-23-dudas-cliente.md` [28:50] a [29:05], [32:02] a [34:29] y [34:47] a [35:17]. Confirmado por el cliente el 01/10 [47:20] a [47:43].
- Que pasa: la madre ya esta aprobada. Lo que falta es la recepcion, y la recepcion se hace parcial. Ejemplo: la OC es por mil cajas (o mil maletas) y la factura llega por cien. El sistema deja recepcionar solo esas cien. Esa recepcion queda como hija 1, con los datos de cabecera de la madre. El detalle no es el de toda la madre: es el de lo recibido. Cuando llegan 200 mas, es la hija 2 de la misma OC. Cada hija va consumiendo el saldo de la grande. Si al final cantidad y monto quedan machos, la madre se cierra.
- Documento: factura de monto menor que la OC. La hija se crea con el movimiento y el monto de la factura recibida. El asiento de ese movimiento es solo de esa parcial (la transcripcion dice "solo con tiempo"; el sentido del parrafo es el monto de lo recepcionado, no el total de la madre).
- Madre: no contabiliza nada. Sirve de control. El 01/10 el cliente lo dice asi: la madre es solo un dato informativo y no se ve en ningun modulo que no sea insumos. El equipo responde que contabilizan los hijos y la madre queda informativa. El cliente cierra con "Exacto".
- Hija: es la que se contabiliza. Hereda la cabecera. El detalle es el de la recepcion.
- Contabilidad: la hija, por el monto recepcionado. La madre, nada.
- Alerta si no calza: no es alerta de "menor". Menor es este caso. El 24/09 [14:22] a [14:39] corrigen una lectura del diagrama: si la cantidad es menor al saldo, no queda como alerta; se genera la hija por el monto de la factura.

### CU-03. Monto igual al de la OC: se cierra y se contabiliza, sin armar parcial

- Quien: cliente, sala 23/09. Locutor no rotulado, en el mismo intercambio que CU-02. El 24/09 lo retoman como "el caso facil".
- Donde: `transcripcion-2026-09-23-dudas-cliente.md` [34:18] a [34:23]. `transcripcion-2026-09-24-reunion-cliente.md` [19:49] a [20:35].
- Que pasa: la factura trae el mismo monto que la OC. No se abre el problema de la parcial. Queda cerrado y contabilizado en el acto. El 24/09 lo separan del caso hija: el total se registra de una vez; las hijas 100.1 y 100.2 son el otro camino, hasta completar el total.
- Documento: factura por el total de la OC.
- Madre: se cierra. No se describe una hija.
- Hija: no se genera en este caso.
- Contabilidad: se contabiliza esa orden y se cierra.
- Alerta si no calza: no aplica. El caso es el calce.

### CU-04. La madre tiene varias lineas y la factura cubre una sola

- Quien: cliente, sala 23/09 [29:49] a [30:32]. Lo retoma el 24/09 [15:51] a [16:36] como "el ejemplo que yo les di".
- Donde: los dos archivos de arriba.
- Que pasa: una OC puede tener dos o tres lineas. Cada linea tiene su cuenta y su centro de costo. La factura de este mes corresponde a la primera linea. La hija se crea con una sola linea, la de esa factura, y respeta la cuenta y el centro de costo de esa linea. Si una segunda factura llega otra vez por la linea 1, no calza: alerta o rechazo. Si llega por la linea 2, completa la madre, con la cuenta y el centro de costo de la linea 2.
- Documento: factura parcial asociada a una linea de la madre.
- Madre: sigue abierta hasta que las lineas se completen. Es "la que manda": el usuario original ya dejo cuenta y centro de costo. Contabilidad no los inventa al armar la hija (`transcripcion-2026-09-24-reunion-cliente.md` [15:07] a [15:43]).
- Hija: una linea, la de la factura. Hereda cuenta y centro de costo de esa linea de la madre.
- Contabilidad: la hija, con la cuenta y el centro de costo de la linea.
- Alerta si no calza: segunda factura de la misma linea: "no va a ser macho. Va a tener la alerta o la va a rechazar" [30:32].
- Limite dicho en la misma sala, sin solucion cerrada: el proveedor trae codigos de producto distintos a los de Almahue. Si dos lineas valen lo mismo, la factura por ese monto no dice a que linea pertenece. El 23/09 [30:54] a [31:51] el equipo lo plantea. El 24/09 [18:17] a [19:41] quedan en que no es automatico y piden un caso real de OC multi-linea con factura parcial. No hay regla de negocio que cierre ese reconocimiento.

### CU-05. En la recepcion el usuario digita las cantidades por linea y al guardar nace la hija

- Quien: cliente, sala 24/09. Locutor no rotulado. Le pregunta a Carlos si entendio [27:18]. Fran es citada por otro locutor [28:19] ("como decia Fran, va rebajando").
- Donde: `transcripcion-2026-09-24-reunion-cliente.md` [25:10] a [28:15].
- Que pasa: la madre se crea con codigos distintos. Ejemplo: primer item 100 cajas, segundo item bolsas. Llega una factura por 20 cajas y 10 bolsas. El usuario, en la recepcion, anota el item y recepciona 20 cajas y 10 bolsas. Para una factura parcial el sistema levanta todas las lineas de la madre y el usuario digita solo las cantidades, por linea. Al guardar se genera la hija con esa cantidad y ese detalle.
- Documento: factura parcial. Debe venir referenciando la madre. Si no viene, el usuario la referencia a mano (eso enlaza con CU-09). Si el monto de la madre es mayor que el de la factura, se levanta un modal con el detalle de la madre para digitar cantidades.
- Madre: no se levanta de nuevo la cantidad total. El saldo pendiente es la cantidad de la madre menos lo ya recepcionado en las hijas.
- Hija: nace al guardar la recepcion, con las cantidades digitadas. Puede llevar mas de una linea (cajas y bolsas en el mismo ejemplo). Esto es distinto del ejemplo de CU-04, donde la hija era de una sola linea porque la factura era de una sola linea. Los dos ejemplos estan dichos.
- Contabilidad: no se detalla el asiento en este tramo. Sigue CU-02: se contabiliza la hija, no la madre.
- Alerta si no calza: si la ultima factura no tiene espacio en el saldo, no se fuerza. Pasa a CU-07.

### CU-06. La hija no vuelve a aprobacion; la madre si, cuando hay que modificarla

- Quien: sala 24/09. Locutor no rotulado. Primero pregunta si la hija pasa por aprobacion y enseguida se corrige: la hija no pasa.
- Donde: `transcripcion-2026-09-24-reunion-cliente.md` [28:48] a [30:07].
- Que pasa: una factura parcial menor que la madre igual crea la hija. Esa hija no entra a la cadena. Queda aprobada porque es parte de la madre, que ya paso por aprobacion. La asociacion se hace en la recepcion y la hija sigue directo. La cadena se vuelve a usar solo cuando hay que modificar la madre porque el valor se paso (o, en CU-08, porque sobra saldo).
- Documento: factura parcial menor que la madre.
- Madre: sigue aprobada. Solo vuelve a aprobacion si hay que editar su monto.
- Hija: se crea y queda aprobada. No recorre la cadena.
- Contabilidad: no se agrega otra regla en este tramo.
- Alerta si no calza: si la ultima hija no cabe, queda en espera. El usuario aprieta solicitar modificaciones de la madre para crear el monto que falta. Ver CU-07.

### CU-07. La factura trae mas que la OC

- Quien: sala 23/09. Un locutor plantea el caso (cotizaron mil, en el camino pidieron doscientas mas, la OC quedo en mil y la factura llega por mil doscientas). La respuesta operativa es modificar la OC. El 24/09 lo recorren sobre el diagrama de Mario.
- Donde: `transcripcion-2026-09-23-dudas-cliente.md` [35:31] a [38:18]. `transcripcion-2026-09-24-reunion-cliente.md` [21:21] a [22:22] y [28:23] a [30:07].
- Que pasa: las hijas van consumiendo el saldo. Si la ultima factura llega por un monto mayor y por mas cajas, queda pendiente, "en el aire". No se recepciona por encima. El usuario que ve la factura o la recepcion pide modificar la madre (agrandarla) para que la ultima factura calce, y ahi se cierra. Si el monto nuevo cruza un tramo de la cadena (ejemplos de la sala: de 1.000 a 10.000, o de 7.000 a 10.000), vuelve a aprobacion y la persona explica por que pide mas. Tiene que salir rapido: la sala habla de menos de siete dias, porque despues de ese plazo el documento pasa automatico. Si el tramite de aprobacion no alcanza, lo que se dice es rechazar y pedir que refacturen.
- Documento: factura (y la recepcion asociada) por encima del saldo de la madre.
- Madre: se edita al alza y vuelve a la cadena que corresponda al monto nuevo. Es una aprobacion de modificacion, no una OC nueva.
- Hija: la que no cabe queda en espera hasta que la madre tenga espacio. No se aprueba ella; se aprueba la modificacion de la madre.
- Contabilidad: mientras no calza, la factura no se contabiliza y la OC no coincide en los montos.
- Alerta: el ERP marca en rojo que hay una factura que no cuadra con la OC. El usuario va al encargado y regulariza el mismo dia, en la frase de la sala.

### CU-08. Quedo saldo y no va a llegar otra factura: se achica la madre y se cierra

- Quien: sala 24/09, al recorrer el cierre de OC con saldo del diagrama. Locutor no rotulado. Lupe, Fran y Sigrid estan en la reunion; Mario es quien trae el diagrama.
- Donde: `transcripcion-2026-09-24-reunion-cliente.md` [20:55] a [22:22].
- Que pasa: la madre se va completando porque rebaja cantidad o monto. Si la tercera llegada se pasa, es CU-07. Si quedo corto y nunca va a llegar otra factura, hay que cerrarla: se manda a aprobacion, el gerente aprueba, se achica la OC y queda saldada. La sala lo resume: sirve tanto para mas como para menos.
- Documento: no llega el documento que faltaba. El hecho es la ausencia de esa factura.
- Madre: se modifica a la baja, pasa por aprobacion y se cierra.
- Hija: no se describe una hija nueva para el saldo que no va a llegar. Las hijas ya recepcionadas son lo que queda.
- Contabilidad: no se dicta un asiento de cierre en este tramo.
- Alerta si no calza: no es una alerta de factura. Es un cierre pedido por el usuario, con aprobacion.

### CU-09. La factura llega sin referencia de OC

- Quien: sala 23/09. La frase de implementar la notificacion la dice el equipo. Lupe es la que esta nombrada en [39:44] y [42:12]: ella revisa, y si no viene OC o no existe, no la crea desde el libro.
- Donde: `transcripcion-2026-09-23-dudas-cliente.md` [38:34] a [42:12]. El 24/09 [27:32] a [27:40] lo repiten: la factura se asocia a la madre, que deberia venir referenciada; si no viene, hay que referenciarla.
- Que pasa: en el XML de la factura no viene la OC. Tiene que quedar alerta y la opcion de asignar a mano. El listado muestra OC de ese proveedor que sigan abiertas y pendientes de asignacion, no las que ya estan asociadas a una factura. Hay dos alertas distintas, dichas en la sala: (1) llego la factura y no existe OC de ese proveedor; (2) existe OC, pero no venia referenciada, y hay que asignarla. Si no existe, contabilidad no genera la OC desde el libro: por permisos, Lupe se comunica con quien la pidio, esa persona crea la OC y le avisa para contabilizar. El equipo llega a ofrecer un boton que redirige al generador, sin saltarse la aprobacion; Lupe corrige el permiso.
- Documento: factura (XML) sin referencia de OC. No es, por si sola, una factura parcial.
- Madre: si existe y esta abierta, se asigna a mano. Si no existe, la crea quien pide la compra, no quien contabiliza.
- Hija: este caso no dice que nazca una hija. La parcial, si el monto es menor, sigue CU-02 y CU-05 despues de asociar.
- Contabilidad: no se contabiliza hasta asociar OC o proforma. Eso ya esta dicho antes del tramo, [25:36].
- Alerta: factura sin referencia. El 14/09 el cliente agrega el mismo borde, sin hablar de hija: ver seccion 3.

### CU-10. Insumos: varias guias en el mes y una factura al cierre, asociada a la OC

- Quien: cliente, sala 01/10. Locutor no rotulado, en primera persona operativa ("a nosotros los materiales nos llegan con guia"). Le confirman a Sergio: la guia no se asocia a la OC; la asociacion es la factura de fin de mes. El cliente dice "Exacto".
- Donde: `transcripcion-2026-10-01-reunion-cliente.md` [55:22] a [57:10].
- Que pasa: todo lo que es insumo se ingresa con guia. Lo demas entra con factura directa. La guia que usan es fisica; la pide el jefe de abastecimiento. Ejemplo dicho: la madre dice 100 cajas; cada semana entregan 10; en el mes hay 4 guias de 10; a fin de mes el proveedor emite la factura por las 40 existencias. La guia sirve para ingresar el material a bodega, porque la bodega tiene que estar al dia. La que se asocia a la OC es la factura de fin de mes. En insumos se listan las guias recibidas. La devolucion de material, si se rechaza la factura, la nombran solo para ALM, que es la sociedad con insumos.
- Documento: guias fisicas de despacho (varias) y, despues, una factura por la suma del mes. No dicen que la guia sea un DTE de GoSocket. En la misma sala dudan si GoSocket traera las guias recibidas (codigo 52) o solo las emitidas, porque en el RCV del SII las guias no aparecen.
- Madre: la OC de las 100 cajas sigue siendo la referencia de la factura de fin de mes, no de cada guia.
- Hija: en este tramo el cliente no dice que cada guia cree una hija. Dice que la guia no se asocia a la OC.
- Contabilidad: no se dicta el asiento. La bodega se actualiza con la guia. La asociacion comercial con la OC es la factura.
- Alerta si no calza: no la definen en este ejemplo. El equipo anota que hay que validar con Pablo si esas guias estan en documentos recibidos.

### CU-11. La proforma de contratistas no se factura parcial

- Quien: Maria Jesus, sala 06/10. El equipo pregunta si la proforma puede facturarse como una OC madre (ejemplo: proforma de 9.600 y factura de 5.600). Ella dice que no.
- Donde: `transcripcion-2026-10-06-gosocket-contratistas.md` [24:45] a [25:33] y [36:27] a [36:37].
- Que pasa: la proforma no queda parcializada contra la factura. Ellos eligen las proformas del mes, le mandan el detalle al contratista y el contratista emite la factura. Una factura recibida puede juntar N proformas. Tiene que calzar. Si no calza, se modifica la proforma (y el ingreso diario de origen) y vuelve a aprobacion. No es el flujo de la hija.
- Documento: factura del contratista por el total de las proformas que se le enviaron.
- Madre / hija: no se usan. La comparacion con la OC madre la hace el equipo; el cliente la descarta para la proforma.
- Contabilidad: no se describe en este tramo. La asociacion es proforma(s) aprobada(s) y enviada(s) contra la factura, en documentos recibidos.
- Alerta si no calza: no queda una parcial abierta. Se edita la proforma en disputa.

## 3. Casos limite dichos en la sala

- Factura mayor que la orden: CU-07. Mil pedidas y factura por mil doscientas, o la ultima parcial que se pasa del saldo. No se guarda la recepcion de mas. Se modifica la madre y vuelve a aprobacion. Si no alcanza el plazo de siete dias, rechazar y pedir refacturacion. Alerta roja de factura que no cuadra.
- Segunda factura de la misma linea: CU-04 [30:32]. Alerta o rechazo. Otra linea de la misma madre si se acepta, con la cuenta y el centro de costo de esa linea.
- Factura sin referencia de OC: CU-09. El 14/09, sin hablar de hija, el cliente agrega tres hechos (`transcripcion-2026-09-14-demo-avances.md` [24:00] a [26:31]): en la practica si llega factura de una OC que aun esta en aprobacion ("en teoria no, en la practica si"); no se rechaza sola ni se bloquea la aceptacion, porque el cambio de habito es progresivo; se destaca el documento. El 90% de las facturas llega sin OC y quedan pendientes de emitir la OC. Tambien se destacan las que referencian una OC no aceptada. A los ocho dias, si no se rechaza, pasa como aprobado. Eso es aceptacion del documento, no creacion de hija.
- Monto igual, no parcial: CU-03. Se cierra y se contabiliza. No nace hija.
- Insumos y el resto: el 23/09 [28:38] y [34:47] dicen que el parcial les pasa sobre todo en insumos (cajas y materiales), con OC grande y recepcion por tandas. El 01/10 [55:22] a [55:33] dice que solo el insumo entra con guia y que lo demas es factura directa. La sala no dice que servicios o activo fijo tengan prohibida la hija. Esa prohibicion esta solo en el deck (diapositiva 5).
- Varias guias y una factura de fin de mes: CU-10. La guia mueve bodega. La factura es la que se asocia a la OC.
- Proforma: CU-11. No se parcializa. Una factura puede cubrir varias proformas, no una fraccion de una proforma.
- Reconocimiento automatico de la linea: CU-04, limite abierto. Codigo del proveedor distinto al de Almahue. Piden un caso real. No quedó regla.

## 4. Deck de Mario frente a la sala

Archivo: `docs/reuniones/compartidos/mj-contratistas-2026-10-06/texto-ppt-mario.md`. Es el documento que Mario armo (version 1.2, septiembre 2026). El 24/09 lo recorren. El 01/10 Maria Jesus dice que le hizo modificaciones chicas a algunas diapositivas.

Coincide con lo dicho en la sala:

- Diapositiva 5: en insumos, una recepcion menor al saldo crea una OC hija y rebaja el saldo. Una recepcion mayor no se guarda y pide modificar la OC. El 24/09 [14:22] corrige que "menor" no es alerta.
- Diapositiva 6: la factura referencia la OC madre. Si no viene la referencia, contabilidad la asigna.
- Diapositiva 7: si la factura no calza, no se asocia y queda pendiente. El creador modifica la OC (vuelve a aprobacion) o rechaza. El rechazo, en el deck, es reclamo en GoSocket y la OC conserva el saldo. La sala del 23/09 dice rechazar y pedir refacturacion, y la alerta roja; no dicta el codigo de reclamo GoSocket en ese tramo.
- Diapositiva 8: la hija ya existe cuando llega la factura, y la factura se asocia. Encaja con CU-05 (la hija nace al guardar la recepcion), no con un DTE que cree la hija solo.
- Diapositiva 9: si el saldo no se va a recibir, se ajusta la madre a lo recibido, pasa por la cadena del monto nuevo y se cierra. Es CU-08. El deck agrega que la modificacion puede ser positiva o negativa. La sala del 24/09 tambien dice "tanto para mas como para menos".

Choca con la sala. Gana la transcripcion:

- Diapositiva 5 y 6: la recepcion con guia registra el numero de guia, deja "factura pendiente", y la factura se reconoce por numero de guia o de factura. El 01/10 el cliente dice lo contrario para insumos: la guia fisica solo ingresa a bodega; no se asocia a la OC; la factura de fin de mes es la que se asocia. Cuatro guias de 10 y una factura por 40.
- Diapositiva 6: "una factura puede cubrir varias OC hijas, pero no una OC hija en partes". Esa frase no esta dicha en las transcripciones leidas. La sala dice otra cosa: cada factura parcial crea su hija (100.1, 100.2), y una hija de una linea no acepta una segunda factura de la misma linea (CU-04).
- Diapositiva 5: servicios o activo fijo solo admiten recepcion completa y no crean hija. La sala no lo dice. Dice que el caso parcial es sobre todo de insumos, y que lo que no es insumo llega con factura directa.

## 5. Lo que el codigo hace hoy y no es el caso de la reunion

La hija solo nace en `solicitarCierreSaldoOc` (`ERP/erp_back/src/modules/compras/compras.service.ts`), y solo si la madre tiene recepcion confirmada. Ahi la hija no es el trozo facturado. Es el saldo que falta: la madre se achica al monto recibido y vuelve a `PENDIENTE_APROBACION`; la hija queda en `BORRADOR` por el saldo, con otro correlativo, no con el numero 100.1. Si no hay recepcion confirmada, no hay hija. Si ya hay una hija activa, no deja crear otra.

El DTE de GoSocket no crea hija. `vincularOcRegistroCompra` (y el sync que usa el mismo calce) solo escribe la OC elegida en el registro de compra. Dos DTE parciales de la misma madre pueden quedar los dos asociados a esa madre.

`assertFacturaCompletaOcHija` (`libro-compras-factura-match.util.ts`) corre cuando la OC vinculada ya es hija (`ocPadreId`). No crea nada. Alerta si esa hija ya tiene otro registro no anulado (`OC_HIJA_YA_FACTURADA`) o si el monto de la factura no es el total de la hija (`OC_HIJA_PARCIAL`). Si la hija todavia no existe, esa funcion no dispara el caso de la reunion.
