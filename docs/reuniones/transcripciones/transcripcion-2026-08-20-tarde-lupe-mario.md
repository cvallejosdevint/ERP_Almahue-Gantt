# Transcripción — 20/08/2026 (tarde) — Lupe, Mario, Sergio, Carlos

**Fuente:** tl;dv (verbatim pegado 21/08/2026).  
**Reunión tl;dv:** https://tldv.io/app/meetings/6a877e1e644c1a00131f8046  
**Título tl;dv:** Screen Recording 2026-08-20 174935  
**Video:** `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-20 174935.mp4` (~1,12 GB; no git)  
**Minuta analizada:** [`../reunion-2026-08-20-tarde-lupe-mario.md`](../reunion-2026-08-20-tarde-lupe-mario.md)  
**Minuta Carlos:** [`reunion-2026-08-20-tarde-minuta-carlos.md`](reunion-2026-08-20-tarde-minuta-carlos.md)  
**Minuta auto tl;dv:** [`reunion-2026-08-20-tarde-minuta-tldv.md`](reunion-2026-08-20-tarde-minuta-tldv.md)

**Speakers (etiquetas tl;dv):**

| Etiqueta | Persona |
|---|---|
| mario | Mario (Almahue) |
| lupe | Guadalupe / Lupe (Almahue, tesorería/compras operativa) |
| Carlos Vallejos | Carlos Vallejos (Devint) |
| sergio | Sergio (Devint) |

**No hablaron:** Agustín, María Jesús / MJ. Francisca fue nombrada (~17:13) como tesorería junto a Lupe; no aparece como speaker.

> ASR de tl;dv: timestamps y speakers tal como vinieron. Posibles errores: «SAT» (área/sistema), «CAP» = CAF, «zarango» (proveedor), «WebSocket» = GoSocket.

---

mario [00:00]: Aprobación, no más, pues queda como a elección del usuario, o sea, del administrador, por así decirlo.

Carlos Vallejos [00:05]: Exacto. Entonces igual se entiende que durante el uso quizás se vayan a tener otros ajustes. Y por ejemplo, como le explicaba, quizás no quedó muy claro, pero se pueden configurar más grupos y hay personas que pueden estar en más de un grupo. Entonces dentro de lo que vendría a ser esto es flexible, pero hay que tener como un poquitito más de configuración. De todas formas, podríamos dejar acá también una tercera opción, que sería seleccionar para cada usuario un aprobador dentro de este eslabón, pero ahí tendríamos que conversarlo un poquitito más cuál sería el alcance y todo, dependiendo de lo que necesiten.

mario [00:44]: Sí, no, yo creo que tendríamos que hacer, como decía acá la chica, hacer una prueba.

Carlos Vallejos [00:47]: Perfecto.

mario [00:48]: Crear algunas órdenes de compra por forma ficticia y ver cómo queda así la estipulación de las aprobaciones. Perfecto, para que quede más claro.

sergio [01:00]: Mario, ahí yo tengo una duda sobre el, bueno, el flujo de aprobación. Se entiende claramente que a nivel de administrador va a definir, pero por ejemplo, hoy en día ustedes tienen niveles de aprobación tanto para lo que es la venta Y tanto para lo que es compras, solo compra, solo pasaría para las cotizaciones, ¿cierto?

lupe [01:33]: Servicios y materiales.

mario [01:36]: ¿Se escucha o no?

sergio [01:38]: Sí, sí te escuché. ¿Que sería servicio y material?

lupe [01:43]: Sí, servicio y materiales, siempre de las compras, de la, solo de compras.

sergio [01:48]: Ah, ya, porque yo me acuerdo No está María Jesús, pero creo que María Jesús siempre habla de las que en el lado de compra es las cotizaciones, ¿cierto?

lupe [02:00]: Son las cotizaciones y ahí se genera la orden de compra.

sergio [02:06]: Ah, ya. Entonces el flujo sería, para entenderlo bien, sería la cotización, ¿cierto? La cotización se aprueba, ¿cierto? Pasa por todo el flujo de aprobación. Y luego se convierte en una orden de compra, ¿cierto?

lupe [02:21]: Y lo que pasa es que primero, claro, nos llegan las cotizaciones, pero al tiro se genera la orden de compra y de ahí pasa aprobación por esta, por las personas, para que puedan hacer la factura.

sergio [02:34]: O sea, entonces, a nivel de sistema, ustedes no es que emitan una cotización inicial, sino es que reciben una cotización. Nosotros recibimos cotizaciones y esa cotización la traspasan a una orden de compra, y luego la orden de compra la enlazan al documento recibido, ¿no? Que puede ser la factura.

lupe [02:54]: Ya, así es.

sergio [02:56]: Ah, ya, ok, ok. Entonces ya, Carlos, entonces habría en sí el documento que emiten para el flujo de compra, el documento inicial de AlmaWeb es una orden de compra. ¿Y ustedes referencian esa cotización en la orden de compra?

mario [03:16]: ¿Cómo así?

sergio [03:19]: Cuando emiten ustedes, generan la orden de compra, ¿agregan la referencia a la cotización recibida?

lupe [03:26]: Lo que pasa es que en otro, a ver, sí, lo que pasa es que en otro, el SAT quiere ingresar igual la cotización como archivo. Adjunta a la orden de compra.

mario [03:39]: No sé si lo van a querer hacer, pero actualmente en Microsoft eso no pasa.

lupe [03:44]: No, no pasa.

mario [03:46]: No lo tenemos con cotización ni tampoco se anexa, ¿cachai? Nos queda como un registro, por así decirlo.

sergio [03:53]: O sea, mira, por ejemplo, Carlos puede mostrar cómo es la emisión.

Carlos Vallejos [03:59]: Sí, de hecho, como lo teníamos actualmente, era que partía efectivamente por la cotización La, de hecho, mira, aquí tenemos un ejemplo de las cotizaciones con sus diferentes estados, y al momento de generar podríamos dejar al proveedor, pero eso en el módulo de ventas, ¿verdad?

sergio [04:24]: No, compras, compras, ¿verdad?

Carlos Vallejos [04:26]: Compras, perfecto, estamos bien. Entonces aquí podría ser el producto, en este caso aquí, pero aquí cambiaría el modelo.

sergio [04:47]: No sé cómo, quién es la que nos confirmó que era cotización recibida, era que en este caso aquí no generamos nosotros la cotización.

lupe [04:58]: Claro, entonces aquí compra, cuando uno compra solicita una cotización para poder generar nosotros la orden de compra.

sergio [05:09]: Ya, ok, eso es lo que había hablado la semana pasada, por eso yo me quedé con la confusión de que el documento inicial en el flujo de compra era una cotización. Entonces ahora me queda bastante claro que parte desde la orden de compra Pero mi duda es que, mira, Carlos, tú cuando emites un documento puedes agregar los datos de referencia, ¿te acuerdas?

lupe [05:32]: Sí, por ejemplo, aquí sería las otras áreas hacen cotización y nos llegan, solo solicitan la orden de compra.

sergio [05:44]: ¿Cómo? ¿Las otras áreas emiten cotizaciones?

lupe [05:48]: No, solicitan, hacen todo el procedimiento de la cotización y nosotros solamente nos piden la orden de compra y nosotros solo generamos la orden de compra.

Carlos Vallejos [05:56]: Por ejemplo, el sistema como está ahora es generar la cotización, la cotización se aprueba, y una vez estando aprobada se puede generar la orden de compra, y ahí se hace referencia a la cotización.

sergio [06:09]: No, pero eso no va a ser así, van a ser desde acá, van a emitir una orden de compra, no una cotización. Quería ver dónde tú agregas la referencia, Carlos, la verdad que habíamos visto Es el ítem, cierto, son los detalles. Hay que agregar esto, hay que agregar en la orden de compra, sí, porque se había modificado por la anterior. Sí, sí, en la orden de compra aquí vamos a agregar que puedan seleccionar el tipo de documento referencia, ya sea una cotización, cierto, y agreguen el folio de la cotización. ¿Se entiende?

Carlos Vallejos [06:51]: Sí.

sergio [06:52]: Esa cotización ustedes pueden que la tengan física o electrónica, me refiero por correo, ¿o no? Está muteado por si acaso.

mario [07:12]: Mario, sí, aquí estamos. Sorry, no te está Estamos conversando un tema.

sergio [07:18]: Les preguntaba que, bueno, vamos a hacer una corrección acá en la pantalla de emisión de orden de compra, en donde se va a agregar como dato de referencia, que no sea obligatorio, el número de la cotización, cierto, fecha y folio, ya, bueno, el tipo de documento. Entonces, pero ese no va a ser obligatorio. Sí, le estaba preguntando, ustedes, la cotización al área que emite la orden de compra, le puede que la reciban por correo o física. ¿Cómo la manejan ahí?

mario [07:49]: Finalmente en PDF le lleno.

sergio [07:50]: Bueno, entonces ahí para que la agreguen solamente como informativa o como referencia nomás, pero no es que vayan a adjuntar el documento en la orden de compra. Ya se entendió. Ya, genial. Entonces, y también me confirman que el flujo de aprobaciones pasa solamente por compras.

mario [08:21]: Por compras, sí, correcto.

sergio [08:24]: Estamos tomando nota.

Carlos Vallejos [08:27]: Bueno, aprovechando igual la instancia, aquí se vería lo que vendrían a ser las aprobaciones. Este vendría a ser como el módulo de las aprobaciones, donde a las personas que son parte de la cadena podrían verlo acá, y también les llegaría como notificación. Y las notificaciones son para las dos vías: cuando el aprobador le llega una nueva aprobación, valga la redundancia, y también al emisor cuando se la aprobaron, también le confirma por notificación. Y aquí vendrían los detalles. Nosotros también podríamos acceder a este mismo módulo para ver el estado de las aprobaciones que nosotros enviamos como emisor, y aquí podríamos ver lo que les contaba del progreso de la aprobación.

lupe [09:15]: Solicitante, una consulta. Sí, por ejemplo, si yo genero una orden de compra, yo así como asigno quién me la tiene que aprobar, o ambos de los que están en esa cadena la aprobarían.

Carlos Vallejos [09:34]: En este caso está como para que sea opcional, que sea como el primero que la apruebe pase, o que sea restrictivo para que si son 2, los 2 lo aprueben. Pero en este caso lo que se ve acá, que esta es una cadena que todos los eslabones solamente tienen uno, entonces en este caso el solicitante lo pidió acá Este que es un eslabón lo aprobó y se completó.

mario [09:59]: O sea, si fuera que un paso de 2 de la aprobación, diría, diría así como aprobado por este, pero falta este.

Carlos Vallejos [10:05]: Exacto, aquí aparecerían los 2 aprobadores pendientes para como dar la información de cuál está aprobado y cuál está por espera.

lupe [10:15]: Y en caso de que esté solo aprobado en uno, ¿podría contabilizarse?

Carlos Vallejos [10:20]: Está la opción, pueden seleccionar de que tengan que aprobar o los dos o uno de los dos.

lupe [10:27]: Debería ser que estuviese aprobada la orden de compra para que se pueda contabilizar.

sergio [10:35]: No, no, claro, pero a lo que se refiere Carlos es que el flujo, el flujo o la cadena de aprobación la configuran ustedes. Colocan un usuario, o en un nivel colocan a 2 usuarios que sean obligatorios la aprobación, hasta que ellos 2 no la aprueben, esa orden de compra no va a quedar aprobada. Y como tú muy bien dices, no se debería contabilizar incluso. Y ahí me surge otra duda que tuve en la mañana con Carlos. Cuando la orden de compra no está aprobada, ¿Cierto? En caso que reciban una factura referenciando esta orden de compra que aún no está aprobada, ¿qué se hace en ese caso? ¿Van a hacer un rechazo automático del documento o lo van a destacar? Que esta factura que está referenciando esta orden de compra aún no puede ser contabilizada o pagada porque la orden de compra no ha sido aprobada del todo. Lo segundo, ya, ok, hay que dejarla destacada para que sepan cuáles son las órdenes de compra que han sido facturadas que no están aprobadas.

mario [11:55]: Claro, y no pasa ni a pago ni tampoco se contabiliza.

sergio [11:59]: Claro, hasta que esté lo que Perfecto.

mario [12:06]: Y el OK obviamente lo definimos según las reglas que nosotros queramos.

sergio [12:10]: Ya, OK. Y ahí hay, bueno, ustedes como bien saben, hay un proceso de aceptación o reclamo por 8 días, ¿cierto? En caso de que estas facturas que están con orden de compra no aprobadas tienen que ser rechazadas o se van a pasar a aprobadas con el flujo normal automático, llamémoslo así.

lupe [12:34]: Pasa que acá no trabajamos con el rechazo, ya de rechazar alguna factura nosotros ingresamos al servicio y la rechazamos manualmente.

sergio [12:46]: No, claro, pero ahora con el ERP todo esto, la aceptación, los reclamos que ustedes hacen en el servicio puesto interno, la van a hacer desde acá, porque estas aceptaciones, reclamos va a pasar por la integración de GoSocket, y GoSocket se encarga de informar al servicio. Entonces nosotros vamos a la integración directa. Entonces la idea es que puedan manejar todo en una sola plataforma. Entonces ahí vuelvo a la pregunta: si el documento, la orden de compra no está aprobada, tienen la factura recibida de su proveedor y está en proceso de aprobación la orden de compra, Pero ya van a pasar los 8 días, que después de los 8 días de forma automática pasa un documento aceptado. ¿Ahí qué se va a hacer? ¿Lo dejamos a que pasen los 8 días y después se vuelva aceptado, o se hace un rechazo automático al día 7 u 8?

lupe [13:43]: La primera opción.

sergio [13:47]: Ya, si no se aceptó a los 8 días, que pase a aprobado automático y queda registrado eso, ¿cierto? Sí, sí, ustedes van a tener trazabilidad de que ese documento pasó por la aceptación automática luego de los 8 días transcurridos. Si no, se rechaza.

Carlos Vallejos [14:15]: Luego de 8 días, vamos entonces a Tendría que realizar igual reformulación del módulo completo, así que igual en la próxima reunión con estas correcciones ya podríamos tener un poco más concreto el sistema. Vamos entonces, vamos a ver el módulo que habían solicitado, que teníamos el de tesorería, ¿verdad?

mario [14:42]: Sí, porque ahí queremos empezar a picar un poco.

Carlos Vallejos [14:48]: Perfecto.

mario [14:48]: La idea es que nos explique un poco cómo está actualmente y nosotros nos quedamos con la tarea de dar feedback.

Carlos Vallejos [14:54]: Perfecto. Actualmente, ¿cómo lo tenemos? Acá tenemos lo que vendría a ser el flujo de caja con los diferentes movimientos y la posibilidad de editarlo, y podemos generar nuevos. Tenemos donde se exportan las cartolas, que acá, bueno, acá en sí está un modo demo, pero este lo estábamos ajustando por los documentos que nos envió María Jesús en su momento. Así que puede que todavía no se estén reflejando todos los campos, pero porque eran, creo que por Excel venían con hartas hojas de cada uno de, por así decirlo, de los bancos donde llegan, de donde llegan la información, ¿verdad? Perfecto. Entonces este vendría a ser como el reflejo de esas cartolas que vienen acá. La idea es que esté configurado para que cuando ustedes importen se refleje esta información acá y se pueda también editar de manera manual. Y así es como se ve dentro de esta exportación.

sergio [16:01]: Carlos, por ejemplo, ahí sería como una Una caluguita por cada movimiento.

Carlos Vallejos [16:14]: Exacto.

sergio [16:16]: Oye, Carlos, y ahí, por ejemplo, si el Excel tiene, no sé, 5000 registros, igual, no sé, como sugerencia, la pantalla no es muy nítida.

Carlos Vallejos [16:29]: Sí, podríamos dejarla más grande. De hecho, en base a eso también ahora se me ocurre dejar un buscador, y como los tenemos en las otras tablas, no hay problema, se puede agregar. Voy a hacerte como un ejemplo cómo hacer la importación del Excel y cómo Tal cual como le explicaba, tenemos activado el modo demo de momento, como estábamos haciendo unos ajustes por las pruebas que estábamos realizando con GoSocket. No sé si es que vaya a funcionar, si gusta podríamos intentarlo, porque de hecho no hay ninguno aquí en la— esta es la base de datos real. De hecho, déjenme buscar acá dentro de los documentos que tengo.

sergio [17:03]: Oye, Mario, ahí por ejemplo, ¿qué te parece? Bueno, ya me puedes confirmar los nombres que no están participando para poder Mencionarlos.

mario [17:13]: Sí, Francisca y Guadalupe, la crack aquí en tesorería.

sergio [17:19]: Ya, Francisca y Guadalupe, les pregunto, Francisca y Guadalupe, ¿sería más cómodo que, por ejemplo, aparece la lista de las cartolas que fueron importadas, cierto? Puede ser n cartolas. ¿Les parecería más cómodo que, por ejemplo, al final de la fila aparezca como una especie de ojito, que en donde si se pincha se puede visualizar el detalle de esa importación, ya, pero como una pantalla nueva que aparezca así como completo todo esto que está mostrando Carlos, con todo el detalle hacia abajo. No sé si me explico.

lupe [18:00]: Sí, sí, sí, entiendo. Sí, sería ideal.

sergio [18:05]: Ya, ok, ¿se entendió, Carlos? Sí, para no levantar un módulo adicional, porque así para poder agregar buscadores, filtrar por fecha, filtrar por monto, por ID de transacción, no sé, o de movimiento.

Carlos Vallejos [18:24]: Por ejemplo, así se ve la vista cuando recopila la info del Excel antes de importarla. Ya, y tenemos como estos filtros, y en base a eso también no sé si es que aquí sería de valor agregado tener otro tipo de filtro, otra información antes de agregar el import. Por ejemplo, esto llega y hace la importación, pero nos da de momento la posibilidad de seleccionar qué se va a importar o no. Si mal no recuerdo, esto lo había solicitado María Jesús en su momento, pero como todavía no estábamos trabajando en este módulo de las correcciones No se ha implementado como que seleccionar en qué movimiento la cartola ingresar y que no se ingresa completa.

lupe [19:05]: Lo que pasa es que se ingresa completa. El tema es que estoy viendo cómo quedaría contabilizado. En la cartola solo aparece el nombre, no me aparece el RUT del proveedor o el cliente.

sergio [19:31]: De ahí, ¿cómo lo asociarían o cómo lo asocian actualmente por movimiento?

lupe [19:37]: Yo los movimientos los ingreso manualmente.

Carlos Vallejos [19:41]: Ahora, porque esta es la cartola que nosotros nos habían entregado.

sergio [19:47]: Y esos son, sorry, son tanto los ingresos y egresos del banco. Sí, o sea, y los ingresos los asocias con los documentos de venta, con los documentos de venta, uno a uno, uno a uno. Oye, y ahí, ¿cómo lo podríamos ¿De qué manera? ¿Qué criterio ocupas tú para poder asociar una factura de venta a un movimiento del banco?

lupe [20:19]: Yo reviso clientes y reviso cuál fue el movimiento en el banco del cliente, y ahí voy viendo qué factura es el monto.

sergio [20:34]: ¿Cómo revisas clientes? ¿A qué te refieres? ¿Te vas al material del cliente?

lupe [20:40]: Sí. Lo que pasa es que, claro, yo voy a ingresar un anticipo porque este va a ser un anticipo, un pago que me hizo un cliente. Ya, ¿qué pasa? Que este pago se tiene que ir al módulo de clientes para poder ejecutarse y me rebaje la factura ya para el saldo pendiente.

sergio [21:09]: Ahí entonces puedes volver a la pantalla, Carlos, por favor. Por ejemplo, ese anticipo que tú mencionas, aclaro, aquí está la carga de cartolas, pero creo que ahí están los anticipos, hay un menú de anticipo, y ahí no, no, si tu registro no es anticipo Claro, y aquí te puedes seleccionar, pero claro, tú estás pensando en cómo hacerlo en el masivo, en la carga.

lupe [21:43]: Lo que pasa entonces, ustedes van a subir la cartola como para tenerla yo visible en el sistema, porque eso es lo que se ve ahí.

sergio [21:53]: Sí, pero la idea es que veas la forma de que te puedas Por ejemplo, tú haces la cartola, ¿cierto? La cargas y en alguna parte de la plataforma hacer como una conciliación bancaria. Por ejemplo, para tus ingresos versus tus documentos de venta y ver, no sé, ver la forma cómo podemos hacer un match entre la factura y es el movimiento del banco, el ingreso, ¿cierto? Y lo mismo para el lado de las compras, las compras Versus los egresos.

lupe [22:29]: Entonces cartola tendría que ir en conciliación porque para eso es lo que yo la voy a usar nomás.

sergio [22:47]: Pero ahí, como si ahí tendría, claro, aquí se va a asociar el movimiento. Ya, mira, deja, Guadalupe, Francisca, fue la que no habló. Lupe, Lupe, Lupe, déjame, déjame hacer un análisis cómo lo podríamos enlazar con la conciliación bancaria, la carga, ya, ya, para ver el tema del match.

lupe [23:19]: Sí, eso, para eso a mí me sirve la cartola en sistema, para hacer la conciliación. Sí, tengo una duda con el flujo de caja.

sergio [23:29]: ¿Cuál duda?

lupe [23:34]: Ahí, el saldo, porque ahí a mí me gustaría verlo como por banco. Por banco, para saber cuánto es el monto que tengo en caja en cada banco.

Carlos Vallejos [23:57]: Sí, podríamos incluir la columna y el filtro de banco también.

lupe [24:02]: Lo que pasa es que tengo, se trabaja con 4 bancos, que son Banco Chile, suponte, en pesos y dólares. Entonces ahí tengo que tener la diferencia, la diferencia cuánto tengo en peso y cuánto tengo en dólar. Perfecto.

Carlos Vallejos [24:23]: Podríamos incluir más columnas y el banco que ocupe cada columna salga el dato y en el otro quede como el típico guión. Así también va a tener la posibilidad de, bueno, en todos estos módulos que son como una lista, por si acaso siempre está la facilidad aquí poder filtrar también en caso de que sea necesario quitar o mostrar algo. Para poder tener la información un poco más ordenada.

sergio [24:47]: Y ahí, ¿cómo se cargaría el saldo del banco?

Carlos Vallejos [24:52]: Ahí tendría que ser igual con la cartola, tendría que ser la carga de la cartola primero entonces.

sergio [25:01]: Y dentro de esta cartola viene, porque en la cartola va a venir los ingresos, egresos, y aparte viene el saldo de la cuenta.

lupe [25:10]: Claro, hay un saldo inicial y después con los movimientos de ingreso y egreso se va moviendo el flujo de caja.

sergio [25:20]: Entonces, entonces la importación de cartola, claro, sirve para la conciliación y además para Para el flujo de caja.

lupe [25:35]: Sí, ok.

Carlos Vallejos [25:38]: Bueno, aquí de hecho también, si gustan, podríamos ordenar esta, el cómo se muestra la información acá, para que sea como más ordenado en el ciclo lógico. Exacto, para que primero vaya la cartola, después lo que sigue, y así sucesivamente.

mario [25:53]: Pero sí hay que ver cómo, cómo el saldo inicial, como tú ponerle al inicio un saldo de apertura, algo así. Que no se mueva, obviamente, pero puede empezar a cuadrarse con la cartola.

lupe [26:08]: Sí, pues que eso se va a ir cuadrando cuando yo ingrese los anticipos. Igual eso quiero revisar bien. Mi consulta, tengo anticipos ahí. ¿Qué diferencia? Eso debería ir como— ¿Me puede mostrar los pagos?

Carlos Vallejos [26:35]: Por supuesto. Este es como el formulario que tenemos acá con los estados.

lupe [26:44]: Ya, lo que pasa es que los anticipos y los pagos yo los ingreso, yo hago la diferencia al ingresarlo.

Carlos Vallejos [26:53]: Al ingresar un egreso, entonces ahí tendría que hacerse la diferenciación, por así decirlo.

lupe [27:03]: Claro, yo ahí ingreso si es un pago completo de una factura o es un anticipo. Lo otro que podrían poner, anticipo productor, ahí que esos son diferentes. ¿Me entienden?

Carlos Vallejos [27:22]: Eso sería como un tercer tipo, por así decirlo.

lupe [27:26]: Claro.

Carlos Vallejos [27:28]: Y ese tiene el mismo tipo de información o cargaría otra data.

lupe [27:34]: No es la misma información, solamente que ahí yo muevo el tipo de cambio.

sergio [27:42]: Y no, no sería mejor unificar ese el tema de pago y anticipo, y dentro, por ejemplo, dejar solo pagos, y que ahí se defina si es anticipo o no, cómo se discrimina si es que paga el saldo completo de la factura, ¿no?

lupe [28:01]: Sí, eso es lo que yo quiero, que se unifique, que quede solo pagos, y que yo pueda, al ingreso de un documento, Claro, colocar si es anticipo o es un pago total de la factura.

Carlos Vallejos [28:18]: Sí, podríamos unificarlo y que al momento del ingreso haga la discriminación.

sergio [28:23]: Y ahí no sería, o sea, pensándolo, por ejemplo, si la factura, el saldo que están ingresando corresponde al 100% del documento, ahí ya se asume que ya hay un pago completo. Y si no Si el saldo es inferior, o sea, lo que se está registrando es inferior a la factura, de forma automática que lo asuma como anticipo. Y debería quedar con alguna columna dependiente, ¿o no? ¿O lo quieren ustedes seleccionar? Es decir, ya es un pago total, o es anticipo, o parcial.

lupe [28:57]: Sí, sí se podría hacer como tú lo dices. Pero sí me gustaría tener la diferenciación de anticipo productor. Que es un tratamiento, sí, yo necesito sacar un, claro, sacar todo lo de productores.

sergio [29:22]: Entonces sería en el movimiento que se va a registrar, sería entonces pago total, anticipo y anticipo productores, serían los 3 tipos.

lupe [29:33]: Sí, perfecto.

Carlos Vallejos [29:42]: Ya no sé si habrá alguna otra parte de este módulo que les llame la atención o que quieran que revisemos aprovechando de las correcciones.

lupe [29:54]: La nómina.

Carlos Vallejos [30:00]: Así lo estábamos gestionando, la nómina.

sergio [30:03]: Aquí la nómina, ¿qué controlarían? Para entenderlo, yo la verdad que no había visto esta pantalla.

lupe [30:13]: Lo que sale a pago, claro. Suponte yo este viernes tengo pago, quiero saber qué es lo que tengo para este viernes.

sergio [30:27]: ¿Y dónde lo ustedes lo registrarían manual acá? ¿Crearían cargarían una nómina o cómo sería ahí?

lupe [30:34]: Lo que pasa es que ahí trabajaríamos con el vencimiento de la del documento.

sergio [30:41]: Ah, perfecto. De los documentos recibidos.

lupe [30:44]: Claro, de los documentos recibidos.

sergio [30:48]: Y esa nómina sería por día. O cómo lo tenemos, ya semanal. Entonces yo, entonces, entonces que usted aquí en nómina no cargaría absolutamente nada, solamente visualización.

lupe [31:04]: No, claro. Y como yo, suponte, tengo esta factura de que me sale ahí frutas, zarango, la tengo para esta semana, pero yo no la pagué. ¿Cómo podría modificar la fecha? Yo podría modificar la fecha de pago para otra semana.

Carlos Vallejos [31:27]: Aquí sería la fecha de vencimiento. En ese caso sí, sí debería poder guardarla, pero aquí eso sí no teníamos contemplado que se pudiera modificar. Tendríamos que agregar los botones de acciones para poder editar aquí manualmente la fecha de vencimiento.

sergio [31:43]: Sí, ahí, Carlos, no nos serviría. ¿Por qué? Porque en sí la nómina trabaja sobre la fecha del documento o la semana que cae. Por lo que entiendo es que van a decir, ya no sé, semana 1 del mes de agosto, ¿cierto? Se van a pagar todos los documentos que vencen desde el lunes, no sé, X, hasta el viernes o domingo X, ¿cierto? Y esos documentos recibidos Están en la nómina, no sé, agosto S1, ya. Entonces editamos la fecha de la nómina, la nómina va a estar trabajando con la fecha de los documentos. Entonces ahí, para poder editar la fecha de pago de un documento en específico, como dice Guadalupe o Francisca, no se pagó. Entonces ese documento, el que en particular que se va a tener que editar, y de forma automática en el sistema te va a aparecer que esa factura se va a pagar ahora en la semana 2 de agosto.

mario [32:50]: Pero que quería ir como marcando días de vencimiento, ¿no?

sergio [32:54]: Tú la marcaste, claro, pero acá la nómina debería trabajarse, como dicen, por semana. Y esas, y el detalle de cada nómina se va a basar en la fecha de pago de cada factura. Entonces, si yo quiero mover una factura una factura para la semana 4, no tengo que editar la nómina, sino que tengo que editar simplemente la fecha de pago de la factura directo. Entonces yo creo que eso debería, se debería controlar. No sé en qué parte de acá esa fecha de vencimiento va a aparecer.

lupe [33:30]: Claro, cuando yo ingrese la factura, la contabilice, y me va a pedir fecha de vencimiento, ¿cierto?

sergio [33:39]: Sí, sí, ya.

lupe [33:40]: Y de ahí se va a ir a este módulo de nóminas de pago, claro.

sergio [33:46]: Y la nómina de esos datos, como decía, va a trabajar según las fechas, los rangos de fecha, ya.

lupe [33:51]: Pero yo, una vez contabilizada la factura, yo no puedo modificarla. Pero yo creo que aquí sí, en la semana, yo voy a seleccionar aquí que sea, me va a mostrar suponte esto está todo el día y me va a mostrar qué facturas yo tengo que pagar esta semana, pero yo voy a sacarte algunas porque no las quiero pagar, o a lo mejor las tengo que pagar en 3 semanas más, y quiero que me aparezca realmente en 3 semanas más, no que me aparezca en la próxima semana.

mario [34:23]: Como que sería asignarle a cada nómina, o sea, cada línea, como asignar la semana en que se va a pagar, y si está vencida que le marque ahí que Lleva 10 vencidas, pero que ella después, pero contablemente la fecha de vencimiento no se va a editar. No, no se edita, no se puede editar. Pero sí sería bueno aquí que tenga indicadores o que le avise a la Lupe, oye, tenéis tantas vencidas, tenéis una atrasada que no hay pagado. Aunque ella sabe que no la ha pagado, pero le está mostrando ella porque no sé, decidieron no hacer el pago, tienen retenida, no sé, no sé.

sergio [35:00]: Ya entiendo. Entonces aquí lo que se podría hacer es que, claro, la nómina se va a visualizar un detalle, ¿cierto? Una lista de facturas, que puedan ver ese listado, y de ese listado decir, ya, esta factura la voy a correr el compromiso de pago para la semana 4 de agosto. Y ahí la editan, la sacan de la semana 1, y después si van a ver la nómina de semana 4, debería listar esa factura Para esa nómina.

mario [35:28]: Claro, y ahí obviamente la están mostrando que está vencida, pero ella obviamente lo hizo.

sergio [35:35]: Y ahí cuando la contabilicen, ¿no sería bueno? Pregunto si en la contabilización, aparte de manejar la fecha de vencimiento, que esa fecha de vencimiento por lo general también viene desde el emisor, del proveedor, agregar una fecha compromiso pago. Porque si se trabaja con una fecha de compromiso pago distinta a la fecha de vencimiento, ustedes podrían eso, eso, ese campo o ese dato sí lo podrían editar.

lupe [36:06]: La verdad es que directo no, parar esa parte del pago de tesorería con contabilidad.

sergio [36:13]: Ya, ok, entonces lo que les mencioné, el tema de ver el detalle e ir a la factura y cambiarla de semana, les queda bien, ¿cierto? Sí, ya, ok.

mario [36:22]: Y ahí obviamente que se pueda ver, no sé, cuántos de los montos pagados por semana, cuánto tiene asignado, cuánto tiene atrasado, cuánto adelantado, no sé, anda a saber, todo como los indicadores arriba.

sergio [36:35]: Ya, y esto es nómina solamente de pago, ¿cierto? Nada de recaudación, solo pago.

Carlos Vallejos [36:49]: Bien, ahí vamos a tener que entonces llegar con una propuesta, ya que un poquitito más clara la idea.

mario [36:55]: Así, nosotros igual nos quedamos con la tarea de probar el tema de las aprobaciones de los árboles.

Carlos Vallejos [37:10]: Sí, de hecho eso también le iba a comentar, hay un pequeño desfase en la versión que tenemos publicado en el sitio. Les confirmaría mañana durante el día cuando quede esta versión disponible. Obviamente no va a quedar con las correcciones de inmediato, pero también para que puedan probar el sistema, ver todos los módulos que ya habíamos visto la semana pasada, y si es que hay algunas correcciones de ahí también nos puedan mandar ahí al grupo de WhatsApp y yo voy actualizando el trello. Lo otro también que quería consultar, no sé si es que habrán podido ver el tema de la carga de los documentos en WebSocket.

lupe [37:48]: La Jesús subió uno pero le mandó error y le contestó a Pablo, si no me equivoco, sí, a Pablo, pero no tuvo respuesta.

Carlos Vallejos [38:01]: Perfecto, entonces ahí entonces quedaríamos claro.

lupe [38:05]: Entonces una vez sacado ese error se podría subir inmediatamente.

Carlos Vallejos [38:10]: Ya, perfecto. Y les pediría que me confirmen por el mismo grupo para poder realizar también las pruebas por nuestra parte de la integración.

lupe [38:16]: Sí, sí, ahí van a avisar.

sergio [38:19]: Sí, y nosotros ya tenemos, ya estamos construyendo la estructura que pide GoSocket, que es el XML, y ya estamos haciendo pruebas de comunicación, pero nos arroja error de que no hay CAP o folio disponible. Así que estamos solamente a la espera para después seguir con la patita de recibir la respuesta de esa misión, cargar el XML, el PDF final de que nos entrega GoSocket.

lupe [38:44]: Sí, igual hubo un retraso por parte del proveedor que no dan los folios, o sea, el tema de los documentos. Consulta con los anticipos. Los anticipos se van a registrar ahí, pero después se van a visualizar en proveedor. O en clientes si corresponde, ¿cierto?

sergio [39:15]: Y creo que lo vamos a hacer según lo que se habló con María Jesús, en estado de cuenta. Ahí creo que se va a hacer con una vista 360 de si es cliente o proveedor y se debería ver todo el detalle.

lupe [39:29]: Ya, allá, eso quería ver. Ya, sí, eso es.

sergio [39:34]: Ya, perfecto. Oye, discúlpenme, por mi lado me tengo que desconectar hasta las Sí, bueno, nosotros por nuestro lado nos vamos con estas cositas y apenas tengamos ya avance, no sé, Mario, si te parece tratar de dejar la reunión antes del jueves para tener, yo creo que hay 2 semanales, 2 reuniones semanales de avance, porque así vamos cerrando de una. No sé si es que pueden también.

mario [40:06]: Sí, yo creo que sí. La próxima llega la María Jesús, ¿no?

sergio [40:11]: Sí, sí, ya genial.

mario [40:13]: Tendremos que coordinar bien la hora, ¿no?

sergio [40:16]: Sería como los lunes son menos complicados, pero podría ser martes o lunes y viernes. Perdón, martes y viernes, porque como lo hacemos el martes va a ser solo un día como de avance hasta el miércoles nomás. Entonces prefiero que sea martes y viernes.

mario [40:38]: Coordinamos bien los horarios, deja aquí coordinarnos internamente y vemos bien qué días dejamos. Ya, a ver quién acá, qué día cuento.

sergio [40:47]: Excelente. Ya pues, muchas gracias, estuvo bastante bueno el arreglo.

Carlos Vallejos [40:53]: Gracias, chicos, que estén muy bien, que tengan buena tarde.

sergio [40:56]: Buenas tardes, chau.

lupe [40:58]: Ciao ciao.
