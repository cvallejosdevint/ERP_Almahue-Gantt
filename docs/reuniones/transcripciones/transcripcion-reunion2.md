# Transcripción Reunión 2 (23/07/2026)

Fuente: pegada en chat Cursor · video uentes/videos/reunion2-2026-07-23.mp4

Speaker 00 [00:20]: Te la voy a compartir pantalla.

Speaker 01 [01:31]: Acá te tengo que agregar, ¿no? Dame un segundo buscarla.

Speaker 02 [04:00]: Ningún problema.

Speaker 01 [08:10]: Rodrigo va a solicitar unirse a la reunión para poder compartir pantalla.

Speaker 00 [09:40]: Perfecto. Pues, ¿qué es eso?

Speaker 01 [10:10]: ¿Lo compramos? Yo me desconecto.

Speaker 00 [10:41]: No, si lo tengo muteado y lo tengo sin audio.

Speaker 01 [11:01]: Ah, ya.

Speaker 00 [11:10]: Yo solo puedo compartir la pantalla.

Speaker 01 [11:21]: Ya. No, para eso no sirve.

Speaker 00 [12:01]: Estoy aparecido como—

Speaker 02 [12:30]: Tratar de conectarte. Sí, espero que en la siguiente pantalla de la llamada Un momento, que parece que Sergio queda anfitrión porque a mí tampoco me llega la notificación.

Speaker 00 [19:21]: Entrando tuyo, ¿no?

Speaker 02 [19:40]: Por algo suena.

Speaker 01 [20:00]: Si no, ahí va. A ver, a dar el paseo. Ahí estás. Ahí sí.

Speaker 02 [22:10]: Muchas gracias.

Speaker 01 [22:41]: Ya, Carlos, como te comentaba, en la página de Agrosoft nosotros igual hemos tenido varias limitaciones con el tema de los contratistas, cuando ingresamos el tarifario, cuando queremos asignarle a la factura. Y hubo un momento en que acá igual se dio la opción de contratar AgroSmart, que AgroSmart es una página especialista en productores, ok, en el campo. Entonces Rodrigo vio la idea de mostrarte cómo era AgroSoft en la actualidad, ver si podemos ver algún caso práctico y ver la mejora que tiene AgroSmart. Y yo creo que nos vamos a quedar más como con la implementación de AgroSmart.

Speaker 02 [31:10]: Perfecto, sería como llevar esta implementación a la ERP que estamos armando.

Speaker 01 [32:10]: Exacto. Igual comenté que teníamos una limitación al tarifario que nos dejaba visualizar.

Speaker 00 [36:51]: Sí, sí, entonces el módulo contratista cuenta con una base de datos que es esta de acá. La primera. Esa es la primera, que es como un maestro de contratistas. Aquí uno ingresa el nombre del contratista junto con el RUT y esa es como la utilidad de este módulo. Luego está, ya en otra base de datos, que es de labores con actividades.

Speaker 01 [48:00]: Ya le hice el recorrido por la página. Lo que él quería ver si había algún modelo donde pudiéramos ver una proforma y cómo asociarla a la factura.

Speaker 00 [49:30]: Ah, ¿abrir el proceso completo?

Speaker 02 [49:41]: Si es posible sería bueno porque eso igual no le informé, chicos, estoy grabando, así que si podemos tener como el proceso completo sería ideal.

Speaker 00 [50:51]: Ya, entonces aquí por ejemplo le pongo el año, el mes. Aquí vamos a seleccionar el contratista con el que va a trabajar.

Speaker 02 [53:01]: Perfecto.

Speaker 00 [53:41]: Y aquí uno ingresa a la labor. Entonces uno poco a poco va haciendo el tarifario por cada uno de los centros de costos que va a trabajar. Por ejemplo, vamos a abrir carpas. Después se selecciona la unidad de medida, que puede ser por formato o a trato. Selecciona las fechas que va a tomar el tarifario y los centros de costos con los que va a trabajar.

Speaker 01 [59:20]: Perfecto.

Speaker 00 [01:00:00]: Si trabajo en el centro de costos Y coloca la tarifa. Entonces ahí se llenan todas las tarifas, y el problema es que claro, si yo agrego más labores, de amarras laterales, el mismo centro de costo, y le pongo 36.500, me borra los datos anteriores. Entonces yo para poder visualizarlo tengo que volver a entrar al módulo Y volver a seleccionar todo para que aparezcan todos de nuevo.

Speaker 02 [01:06:10]: Y el refresh como que no funciona, tiene que hacerse como manual.

Speaker 00 [01:06:51]: Y claro, lo que conversábamos también es que al final el tarifario es como bien complejo porque a veces los precios van cambiando sobre el mismo, sobre cada una de las plataformas. Entonces como que armar el tarifario, por lo menos para nosotros, como un paso de más. Se nos hace más fácil como colocarlo dentro del mismo proceso de inmediato en vez de hacer un tarifario antes de poder trabajar. De aquí tenemos que hacer ingreso de los contratos y volvemos a seleccionar el mismo contratista, el estado que tiene que estar siempre activo, tipo de contrato mano de obra, la fecha de emisión del trabajo. La fecha en que inicia el trabajo, el 16 hasta el 30 de junio. Y la faena, aquí tenemos que colocar, tenemos hartas, pero al final siempre usamos que una faena agrícola, como un dato, un paso de más. Y aquí colocamos de nuevo la fecha de inicio. Folio 179. Se guarda el folio y no tiene que anotarlo. Pasa al enrolamiento de personal. El folio es 179. Y la faena era esta. Entonces, aquí uno tiene que empezar a anotar los datos de la persona, del contratista. Tiene que escribir el nombre del contratista, que es la fecha en que inicia el trabajo, si está activo, y El jefe de la cuadrilla, y ahí uno guarda. Después de que está hecho el enrolamiento del personal, uno va al control de producción, que aquí es donde uno empieza a ingresar como todas las labores diarias.

Speaker 01 [01:31:11]: Se repiten demasiados pasos en todos los ítems.

Speaker 02 [01:32:01]: Sí, tiene bastante.

Speaker 01 [01:32:30]: Y el problema es que si acá nos damos cuenta que hay un error en el tarifario, hay que volver al inicio.

Speaker 02 [01:34:11]: Sí, está bastante tedioso y son hartas pestañas como que tienen que navegar.

Speaker 01 [01:35:21]: Sí, actualmente está así, pero el modelo de AgroSmart es mucho más amigable.

Speaker 00 [01:36:40]: Muchísimo. Entonces tengo que volver a poner la fecha, la faena, el jefe, y tengo que empezar a seleccionar uno a uno los centros de costo. Aquí hay un tema que, por ejemplo, yo puse abrir carpas y tengo que saberme de memoria cuáles son las actividades, porque se supone que esto es como una ayuda, el que esté en actividad con una labor. Por ejemplo, la actividad es poda, y dentro de poda hay varias actividades relacionadas con la poda. Y aquí funciona al revés, uno ingresa a la labor y después te pide la actividad, y no puede entrar a la labor si no se sabe la actividad. Entonces como que medio enredado.

Speaker 01 [01:43:21]: Y tampoco, si uno por ejemplo pincha la labor, te sale como a qué actividad está asociada, sino que te salen todas, y es innecesario.

Speaker 02 [01:44:51]: Claro, totalmente innecesario. Sería mucho más práctico que aparezcan las asociadas solamente.

Speaker 00 [01:45:51]: Exacto. Entonces, por ejemplo, yo puse abrir carpas, que abrir carpas está en techo, pero si no me acordara no me aparece. Por ejemplo, estoy ahora en una otra actividad que es diversas labores, no está. Para meterme sí o sí a la de techos, pero porque me acuerdo nomás. Claro, me voy aquí a abrir carpas y le puse que era por jornada y me tira automáticamente el precio. Y el precio yo no lo puedo modificar acá porque está en el tarifario. Entonces de repente pasa que terminan de hacer los trabajos y después de que terminan de hacer los trabajos muchas veces se da el precio. Entonces no nos sirve para llevar un control diario sobre quién está yendo, cómo llevar asistencia, o no sé, porque de repente el trabajo dura un mes, entonces se nos haría más fácil ingresar diariamente, pero no podemos porque como no manejamos el precio todavía muchas veces. Y ahí uno guarda. Entonces, cuando se guarda eso, uno se va a la emisión de la proforma.

Speaker 02 [01:56:30]: Perfecto.

Speaker 00 [01:56:40]: Tengo el 179, el 16 del 6. Entonces coloco los contratistas con los que quiero hacer la proforma, que sería el número 6, que era Gómez y Gómez. El folio, y el folio que estaba anotado era el 179. Entonces aquí hay un tema como bien raro, que el reporte se activa con el PDF de acá, y existen 2, uno que es de borrador y el otro definitivo. Entonces como que es bien curioso cómo funciona, porque si uno pone el definitivo, sí o sí se va a emitir como todo el proceso, como que no hay ningún filtro filtro antes, como de si está seguro, como para validarlo, para poder revisar.

Speaker 02 [02:04:21]: Sí, de hecho creo que eso lo habíamos visto con María José, y claro, ahí hace falta de que primero te muestre el borrador y después uno le dé aceptar.

Speaker 00 [02:05:51]: Entonces ahí, por ejemplo, está el borrador y vamos a estar todo lo que yo ingresé. No se visualiza porque lo estoy compartiendo ahora.

Speaker 02 [02:07:51]: Ah, sí, la pestaña.

Speaker 00 [02:08:01]: Sí, en ese caso, mostrar, no mostrar. Déjeme configurar esto bien.

Speaker 01 [02:09:51]: Vamos a ver tus secretos.

Speaker 02 [02:10:51]: Todo queda aquí confidencial por si acaso.

Speaker 00 [02:11:51]: Aquí, por ejemplo, tengo la proforma. Este es el detalle de la proforma. Qué es lo que está dentro de. Y por otro lado muestra como la plantilla principal de esta proforma que me dice cuánto me costó nomás. En este caso sería faena agrícola, que es la faena que seleccioné, la cantidad de lo que haya elegido, en este caso puse una pura jornada, y el precio total que serían 37.500 según lo que fui poniendo. Y me aparece el neto, el IVA, el total. Entonces se supone que uno le va mandando estas cosas a los contratistas para que ellos después puedan hacer la facturación, según lo que nosotros tenemos informado. Ese es más o menos el proceso, y ya cuando uno pone definitiva, lo único que cambia es que, por ejemplo, acá tengo el folio de la factura 0, mientras sea borrador, y me tira el borrador acá. Claro, definitiva, me va a tirar el folio, un nuevo folio que sería el 155 ahora, y me tiraría esto también con el número 155 que sería la proforma.

Speaker 02 [02:25:30]: Perfecto.

Speaker 00 [02:26:01]: Ahora ¿Ya vieron cómo el módulo de los proveedores, cierto? Sí. Voy a pasar un poco al módulo de los proveedores porque después de la proforma uno tiene que asociar la proforma a la factura que nos llega. Entonces, si yo me voy al módulo de proveedores, procesos diarios, coloco aquí tipo de compra que es de contratista, me van a aparecer todas las proformas que tengo activas. En este caso, en la proforma 155, que es la que estaba haciendo recién. Exacto, ya me aparece esa. Ahora, ¿cuál es el tema? Que a veces en proforma nosotros puede que tomemos más de una para una sola factura. Eso es como otro detalle, porque actualmente el sistema, las proformas, nos deja hacer una proforma por mes. Entonces hay veces en las que se juntan 2 meses no sé, pues los últimos días del mes con los primeros días del mes para hacer una factura, entonces necesitamos hacer dos proformas distintas para esa factura. Pero si hacemos las dos proformas, no nos deja asociarlas después dentro de este módulo.

Speaker 02 [02:37:31]: Ah, ok.

Speaker 00 [02:37:50]: Claro, ahora nos sirve solo en el caso de que hagamos una proforma y que esa proforma se haga dentro del mes que llegue la factura, pero si viene de un mes para otro, es medio complicado el proceso.

Speaker 02 [02:39:40]: Me imagino que en ese caso tienen que hacerlo como duplicado, ¿verdad? Para que pueda estar en los 2 meses.

Speaker 00 [02:40:31]: En ese, hasta ahora no lo estamos llevando así, lo hacemos todo dentro del mismo mes. O sea, tenemos como un registro, tenemos 2 registros al final, uno que lo lleva un poco más administrativamente, en el que dicen, no sé, el mismo caso de abrir carpas, se abrió carpa en enero y en febrero, pero yo ingreso todo en febrero en el sistema porque se hace más sencillo hacerlo así.

Speaker 02 [02:43:51]: Claro, lo hacen como el sistema lo permite, pero en, por así decirlo, en un registro aparte dejan en consideración de que un registro que no es solamente es el mes, que conlleva también parte del otro mes.

Speaker 01 [02:45:50]: Exacto, y eso impide que haya un poco de gestión, porque si ven el comportamiento de, no sé, el costo de abrir carpas mensualizado, no se refleja la realidad.

Speaker 02 [02:47:30]: Exacto, no refleja la realidad. Vamos entonces a tenerlo aquí también en consideración para esa implementación de que dé la opción de de ampliar esos días dependiendo de la situación.

Speaker 01 [02:49:20]: Y lo otro es que ahora Rodrigo igual te va a mostrar el módulo de AgroSmart, que aún no nos han eliminado.

Speaker 00 [02:50:11]: Sí, no podríamos poder decirlo.

Speaker 01 [02:50:41]: Claro, esto es confidencial. A donde nosotros cuando vimos la opción de cambiarnos era muy amigable y permitía, tenía más flexibilidad, porque uno podía ingresar el tarifario diario y lo podía editar también.

Speaker 02 [02:53:31]: Ah, perfecto.

Speaker 01 [02:53:40]: Entonces, ¿qué pasaba después? Uno se iba a una pestaña donde estaban todas las labores diarias y uno podía pinchar para poder ver a qué factura lo asociaba, pero no era necesario pincharlas todas. Mira, ahí te va a mostrar, Rodrigo.

Speaker 00 [02:56:10]: Lo otro, un poquito antes de cambiar, en la parte como el efecto contable al final que tiene esto es que cuando yo emito la proforma se me hace Cuando yo hago el cierre de mes, se me hace un asiento en el que me aparece por un lado facturas de contratistas por recibir, y me aparece este de aquí, que es como el asociado a la proforma 155, que es la que estaba haciendo recién, el RUT del contratista y todos los datos, contra el costo por mano de obra contratista, o la cuenta que seleccionemos.

Speaker 02 [03:03:10]: Perfecto.

Speaker 00 [03:03:10]: El efecto contable al final se arma siempre de todo contra mano de obra contratista, contra la suma de todas las proformas que estén dentro del mes. Y ahora en AgroSmart, lo que tiene de bueno es que yo me voy aquí al registro de mano de obra Está viendo que están haciendo como una actualización, así que ahora no está funcionando tan, tan, tan bien el módulo, pero sigue muy práctico, es mucho más sencillo. De aquí uno se mete a mano de obra, ingresar múltiples registros de mano de obra, selecciona la empresa y la fecha. Entonces coloco la fecha acá, coloco el cuartel en el que quiero trabajar. Por ejemplo, este de aquí, la faena, en este caso el mismo tema de abrir carpas, selecciono abrir carpas, selecciono el formato de pago, si es que lo quiero hacer por trato o jornada. Si es jornada, me va a tirar automáticamente la unidad de pago que va a ser por jornada. Si es a trato, ahí yo le voy seleccionando si quiero el trato, no sé, por cantidad de kilos cosechados, por los bins, por los capachos, por lo que sea. Entonces, esta parte no está bien sincronizada. Como están haciendo actualizaciones en AgroSmart, se supone que acá me debería tirar el maestro de contratistas. Entonces me debería dar todos los nombres de los contratistas que tengo ingresados. Ahora funciona solo como para mano de obra como de la misma empresa. Entonces, en vez de eso me dice sí o sí trabajador interno y tengo que colocar uno de los trabajadores que tengamos.

Speaker 02 [03:20:30]: Idealmente aparecieran los contratistas.

Speaker 00 [03:21:10]: Luego tengo las jornadas y la duración. La duración no nos importa mucho en realidad, pero en general lo hacemos como casi todos, que ponen 8 horas. Entonces, si pongo 20 jornadas, me va a multiplicar las 20 por 8 y me va a dar los 160. Y luego coloco el valor dependiendo de lo que quiera de cuál sea el tipo de negocio que sea en esta fecha. Por ejemplo, si es por piso, si es por valor unitario, que en el caso de cuando hago tratos de, por ejemplo, no sé, voy a pagarles por la cantidad de kilos que cosechen, entonces debería colocar el valor unitario de cuánto vale el kilo cosechado acá, y el valor de la jornada. Si es por el día, yo le voy a pagar a las personas 37.500 por Todos los que vengan a trabajar ese día, y ahí al tiro me hace la suma del gasto.

Speaker 02 [03:30:00]: Perfecto.

Speaker 00 [03:30:10]: Guardo el registro. Ahí se suma, yo guardo el registro, y si yo me voy a asignación de facturas Nueva asociación, Santa Pilar. Entonces, si yo me voy a asociación de facturas, aquí me aparecen todas las manos de obra que yo he ejecutado y que todavía no le he asociado a una factura existente. Por ejemplo, aprieto acá, que sería en la fecha 21/10, aplicación de herbicidas, control de maleza, son 150.000 pesos pagados por jornada. Entonces aquí me da la opción, porque estaba conectado con el servicio del AgroSmart, entonces me dice todas las facturas que yo recibí de, en este caso, Sociedad Agrícola Guarachi. Así yo pongo, no sé, la factura 120. Entonces aquí voy a empezar a asociar todas las labores que estén relacionadas a esa factura. Entonces voy colocando esta, esta, esta, y me va sumando cada una de las labores que empecé a anotar anteriormente hasta generar el monto. Si yo ahora le pongo asociar a la factura, me va a dar un total de De esos 2 millones 550 me va a empezar a restar lo que yo le vaya asociando. Si yo le pongo ahora asociar, sería 2 millones 550 menos 825 mil hasta que llegue a calzarlo perfecto.

Speaker 02 [03:50:31]: Perfecto.

Speaker 00 [03:51:00]: Ahora, como nosotros trabajamos un poco al revés, nosotros hacemos la proforma primero a lo mejor se nos haría más sencillo asociarla a una proforma. O sea, después de haber anotado todas las labores diarias, yo poder ver todas las labores que tengo anotadas y decir ya, esta, esta, esta, esta, esta, hago una proforma. No sé si se me entiende.

Speaker 02 [03:54:40]: Sí, sí, están como, bueno, me imagino que esto igual es porque tienen los dos sistemas que tienen que hacerlo de esta forma.

Speaker 01 [03:55:51]: No, actualmente no tenemos los dos sistemas. Intentamos cambiarnos a AgroSmart, pero tuvimos problemas en el módulo de contabilidad. Porque AgroSmart está más ligado como a la gestión del campo, e intentaron suplirlo en la parte contable y no fue bueno, no quedó bien la implementación, no, cero, nos duplicaba registros, nos daba unas centralizaciones súper descuadradas, así que no confiamos en el sistema y nos mantuvimos en AgroSoft.

Speaker 02 [04:00:41]: Entonces este era como el reemplazo en primera instancia del anterior.

Speaker 01 [04:01:31]: Claro, era el reemplazo más que nada por el módulo de contratistas, porque siempre para nosotros ha sido un problema en Agrosoft el módulo de contratistas. Entonces, como este tenía una mejor versión en ese módulo y no iba a suplir la parte contable, vimos la opción de cambiarnos, pero no dio abasto.

Speaker 02 [04:05:30]: ¿Hay alguna utilidad u otra cosa que sería bueno extraer de este AgroSmart que podamos trasladar también al que estamos armando? ¿Alguna otra cosita?

Speaker 00 [04:08:00]: Yo creo que lo mejor de AgroSmart es que simplificaba mucho la tarea para hacer esto. Entonces, si antes, de hecho me acuerdo que cuando empezamos a hacer las proformas de contratistas en AgroSoft La primera vez no alcanzamos a hacer una en todo un día de trabajo porque es muy largo el proceso, es muy engorroso. Si uno se le olvida un dato, tiene que devolverse todo el proceso de trabajo a revisar. Entonces era medio pesada la pega de poder hacer solo una proforma. Entonces AgroSmart, la propuesta que tenía era súper buena. De hecho, el módulo para mí funciona muy bien en ese sentido, solo que en la parte contable no tiene esa conexión. Ese es como el gran problema de AgroSmart. Y por la parte de reportabilidad, casi todo lo pasábamos con Power BI, entonces nosotros terminábamos haciendo mal los reportes, no eran tan útiles tampoco los reportes que entregábamos.

Speaker 02 [04:17:21]: Perfecto, entonces de este software me voy a quedar con esta idea general para reemplazar el que tenemos en el otro sistema. Y en sí solamente sería de este, de este AgroSmart, solamente esta parte. Lo demás, la funcionalidad, hay que basarse netamente en cómo funciona el otro, que el que está correctamente actualmente, ¿verdad? Sí, perfecto, chicos. Ya pasemos nomás con el siguiente punto. Miren, dentro de las dudas que nosotros habíamos tenido, no sé si es que habrá alguna otra cosita que quieran mostrar antes de partir con mis preguntas.

Speaker 01 [04:25:11]: Lo que quedó pendiente la reunión pasada fue el módulo de venta y tesorería.

Speaker 02 [04:26:00]: Exacto, si es que podríamos verlo, porque aquí de hecho lo tengo en las notas de lo que teníamos pendiente. Entonces, pro forma, ya lo tenemos listo.

Speaker 01 [04:32:11]: Bueno, más de él nomás. Ya, mira, acá nosotros quedamos en el módulo contable, después nos fuimos a proveedores y vimos la parametrización y vimos los procesos diarios.

Speaker 02 [04:34:01]: Eso sí, Mari, no estás compartiendo pantalla.

Speaker 01 [04:36:10]: Ahora sí, y ahí sí se ve bien.

Speaker 02 [04:37:00]: Si vos estás a ventanita, la cierras nomás para que no te moleste la vista.

Speaker 01 [04:38:00]: Ya, acá vimos el módulo de proveedores donde estaba la parametrización de cómo se creaban los proveedores y los procesos diarios cuando asignábamos la factura, ¿cierto?

Speaker 02 [04:39:30]: Exacto.

Speaker 01 [04:39:40]: Ya nos faltó el módulo de ventas, que acá nosotros también tenemos para ingresar el libro de compras. Perdón, el libro de ventas. ¿Cuál sería la única limitancia de este módulo? Es que al momento de ingresar todos los datos, si yo la guardo y después la quiero reversar, no puedo solo editar lo que me equivoqué, tengo que ingresar el documento totalmente completo de nuevo.

Speaker 02 [04:44:01]: Entonces es como que tienes que eliminarlo y crearlo de cero.

Speaker 01 [04:44:40]: Sí, si yo me equivoco, por ejemplo, en el módulo de contabilidad, en el módulo de proveedores, yo reverso el registro el registro y puedo editar específicamente la línea que me equivoqué, se agrega y se guarda. En cambio, en este módulo, si yo me equivoco, tengo que reversarlo, pero al reversarlo no me deja editar nada y ahí tengo que ingresar el documento de nuevo.

Speaker 02 [04:49:10]: Sería bueno, porque esto, este tema del editar, te pasa, por ejemplo, cuando tú necesitas editar, puede que te pase, por ejemplo, un día después de que haga el registro de venta, ¿verdad? O por lo general durante el mismo instante. Instante, un momento en el día?

Speaker 01 [04:51:31]: Puede ser en el mismo instante o puede ser cuando ya hacemos la revisión del mes.

Speaker 02 [04:52:20]: Ah, ok. Entonces, en ese caso, porque me imaginaba de que a lo mejor estaba como limitado para que no te permitiera editar, porque no hay ningún, por ejemplo, un dato sensible o algo que vaya a afectar quizás la contabilidad o algo de lo que se vaya a editar en sí. Por lo que tengo entendido, como todo iría a base de datos, debería todo actualizarse junto. Pero no sé si habrá algún dato delicado.

Speaker 01 [04:56:31]: No, no, no. De hecho, se ingresa muy similar al módulo de compras. La diferencia es que acá, no sé si te fijas, pero tiene como más ítems que rellenar. Sí, ya dentro de esos ítems tampoco pides rellenarlos todos. Por ejemplo, acá cuando nosotros ingresamos una venta, ingresamos el tipo de documento. El número, tipo de venta, si lo hacemos al contado, 15 días, 30 días. Y acá nos pide de nuevo los datos, o se duplican, o si acá, por ejemplo, yo pongo una nota de débito, si tiene algo asociado, o nota de crédito. Acá pongo el cliente, voy a poner cualquiera, y estos los trae. Pero lo demás no es necesario rellenarlo: número de despacho, teléfono cliente, fax, nada.

Speaker 02 [05:06:10]: Perfecto.

Speaker 01 [05:06:21]: Y aquí yo pongo el módulo de venta, que voy a poner Mercado Nacional. Centro de costos me despliega todos. Área de negocio. La cantidad 1, 3, precio unitario, y ahí lo agrego. Acá, acá, mira, si yo lo guardo, se me guarda pero no se me va al registro contable. Si yo lo grabo, se me va al registro contable.

Speaker 02 [05:13:20]: Me imagino que ese guardar es como dejarlo como temporal ahí para que veas que esté todo bien.

Speaker 01 [05:14:01]: Como exacto, solo temporal, porque si yo bajo algún reporte tampoco me aparece lo que yo ingresé. Ok, entonces acá yo lo grabo y contabilizo, me quedo. Si yo quiero, ya supongamos que lo quiero revisar acá. Y yo lo quiero reversar porque me equivoqué en poner el cliente. Claro, mira, este no es el que yo ingresé, no me aparece. Sí, está extraño.

Speaker 02 [05:22:00]: De todas formas, el número que se generó lo tenemos en la grabación en caso de cualquier cosita. Después te lo puedo pasar, de hecho va a dejar anotado que fue a los 3 minutos 32 de la grabación.

Speaker 01 [05:24:01]: Ya, buenísimo.

Speaker 02 [05:24:21]: Tenemos el respaldo del numerito en caso de que lo necesiten borrar, como hicimos este ejemplo, grabamos en caso que necesiten borrar. Pero efectivamente ahí no apareció.

Speaker 01 [05:25:41]: De hecho necesito borrarlo porque este me fijé porque no era el cliente que seleccioné, me sale Chamonate y yo seleccioné Sandoval y Fuente.

Speaker 02 [05:27:10]: Sí, sí, y esa búsqueda también está extraña. Ahí terminando la reunión y teniendo el videíto ya guardado completo, te mando.

Speaker 01 [05:28:10]: Se demoró.

Speaker 02 [05:28:11]: Mira, ahí me apareció.

Speaker 01 [05:28:40]: Tengo que meter de nuevo.

Speaker 02 [05:29:00]: Sí.

Speaker 01 [05:29:10]: Ya. Si yo lo reverso y me equivoqué, no sé, en el centro de costo, por ejemplo, no me deja editarlo. No se puede modificar un RV reversado, ingresar todo de nuevo.

Speaker 02 [05:33:21]: En ese caso, por ejemplo, si tú reversas y editas, la idea es que se quede con el mismo ID, ¿verdad? Con el mismo numerito del 472.

Speaker 01 [05:35:00]: No, ahí se puede generar, se supone que cuando yo reverso Se hacen 2 asientos, el que hice inicialmente como reversado, y si lo reverso queda como reversador, que es como la contrapartida para que la contabilidad me dé 0.

Speaker 02 [05:37:30]: Entonces, en ese caso sería reversar, que se borre la ID anterior porque corresponde, y al generar uno nuevo debería generarte un nuevo numerito, pero permitiéndote grabar esta nueva reversa, ¿verdad?

Speaker 01 [05:39:21]: Exacto, claro. En este caso sería, por ejemplo, el 474. Claro, el 472 queda con el original, que es el reversado. El 473 debería ser la reversa para que me quede cero en la contabilidad, y el 474 el nuevo registro.

Speaker 02 [05:42:11]: En sí, lo único que le falta al sistema es cómo poder reutilizar los datos del que reversaste. Exacto. Ya, perfecto. Me imagino que igual está bueno de que no te permita grabar, porque me imagino que en algún momento esto está pensado en que uno puede levantarse del asiento mientras esto, volver y ver, esto no lo dejé guardado. Y sería bueno que el momento de guardar te dé una advertencia de que te diga esto algo que reversaste, ¿está seguro que desea grabarlo nuevamente? ¿Verdad?

Speaker 01 [05:46:20]: Claro, o sea, en este módulo al menos el guardar está de más porque en realidad no se ocupa, porque al guardarlo uno no puede visualizar en ninguna otra parte. Entonces, si comete el error de guardarlo, después yo quiero sacar un informe, me va a aparecer que el documento aún está pendiente de ingreso. Eso no tiene como mayor utilidad. Aquí sería solamente grabar, grabar y contabilizar.

Speaker 02 [05:50:51]: Claro, entonces el proceso sería, por ejemplo, voy a crear una venta, me equivoqué, hago la reserva. La reserva hace los 2 documentos que deben quedar, utilizar esa información que ya está para poder generar una nueva que se va a generar con su número correspondiente. Y en el proceso también de que te pregunte, está utilizando los datos de una reserva, ¿está seguro? Y cuando uno le decía, y los graves, claro, quedó más claro, chicos.

Speaker 01 [05:56:10]: Y por el lado de tesorería, acá tenemos un tema grande porque en este ERP no está, no está hecho para conciliar. Ni para hacer los calces de lo que es el pago y la factura. Entonces, ¿qué pasa? Nosotros lo hacemos, pero lo hacemos de una manera que es como parche, y ahí se generan varias, varias diferencias. Por ejemplo, si yo calzo en dólar, me calcula la diferencia tipo de cambio en peso. Acá, por ejemplo, te voy a mostrar. Mira, aquí, por ejemplo, me aparecen las facturas que yo tengo en el Banco de Chile. Ya, si yo acá tuviera el anticipo del banco o quisiera pagarla porque ya está en la cartola, yo acá ya pongo fecha de hoy, el banco Lo voy a calzar en pesos. Esto es servicio, bueno, comisiones, que a mí igual aquí me permite ingresar el movimiento directo. Y acá me pide el número del movimiento y lo pongo 1. Y entonces si yo lo grabo Mira, me dejó guardar y no había pinchado nada.

Speaker 02 [06:12:20]: Eso no debería dejarte, ¿verdad?

Speaker 01 [06:12:40]: No, debería darme una advertencia que en realidad no estoy pinchando nada. Y mira, estoy en Ya supongamos que voy a pagar esta factura.

Speaker 02 [06:16:40]: Perfecto.

Speaker 01 [06:16:51]: Ya yo la grabo, a mí se me hace el asiento contable de banco y en la rebaja de la factura me abre este comprobante que yo saqué del banco 46.000 pesos y pagué esta factura. Perfecto. Obviamente no me hace diferencia el tipo de cambio porque yo pagué en pesos. Claro. Y en realidad me respeta el tipo de cambio del comprobante. Entonces acá hay la hoja reversa. Aquí me aparece en el comprobante. Si yo esto lo reverso, me permite reversarlo. Y por ejemplo, yo quiero editar el monto. ¿Me deja guardarlo?

Speaker 02 [06:30:20]: Claro.

Speaker 01 [06:30:51]: Ahora, si yo me voy al módulo de tesorería, debería aparecer esa factura con 30 pesos de saldo, que es la actualizada. Claro, si yo me meto, claro, me queda en saldo 30, que fue lo que yo modifiqué para no calzarla completa. ¿Te fijas acá? Sí, que si está el documento pendiente me aparece el total del documento y el mismo saldo, pero si yo la modifico o pago menos me aparece el saldo restante. Sí, entonces estos módulos están súper conectados, pero el módulo de venta queda aparte, no tiene como esa interacción. No, entonces acá ya la voy a reversar porque obviamente ese no corresponde.

Speaker 02 [06:38:11]: Se va a notar en la reversa los días de reunión.

Speaker 01 [06:39:10]: Menos mal le pongo a todo borrar para que sepan que son las pruebas. Pero si tú te fijas, acá me aparece, me aparece el reversado, el reversador, el reversado, el reversador. Perfecto. Que el reversador se hace de manera automática al momento de querer eliminar el movimiento.

Speaker 02 [06:42:10]: Que esa es la idea, que se refleje también de la misma forma en el otro módulo.

Speaker 01 [06:42:41]: Exacto.

Speaker 02 [06:42:50]: Perfecto.

Speaker 01 [06:43:01]: Y entonces acá en tesorería tenemos el proceso de conciliación, pero actualmente nosotros tenemos que subir un archivo Excel con los movimientos de la cartola bancaria. Que eso era quizás una mejora que queríamos hacer, de subir el PDF que nos manda el banco.

Speaker 02 [06:46:20]: Perfecto. En ese caso, ¿tendrán como el Excel y el PDF que les llega al banco para tenerlo acá también?

Speaker 01 [06:47:51]: Se lo tenemos que solicitar al Agustín. Ah, perfecto. Entonces eso quedaría, si nos pueden ir adjuntando durante el día, perfecto.

Speaker 02 [06:49:50]: Así nos basamos directamente en cómo les llega el PDF para que lo puedan cargar.

Speaker 01 [06:51:00]: Exacto. Ya, entonces actualmente nosotros tenemos que subir la cartola y hacer la conciliación. El módulo de conciliación lo hacemos de forma manual porque al momento de subir el Excel no te queda igual el ingreso. Por ejemplo, no sé, la cartola dice transferencia 20 Y nosotros no respetamos el número de comprobante 20, ponemos el 1. Entonces no se te calzan los datos. Ok, yo creo que actualmente está todo calzado. En un mes que no esté conciliado, acá me aparecen todos los datos que yo cargué de la cartola y acá todos los datos de contabilidad. Entonces yo debiese pincharlos todos y en el total debe haber, me debe dar el mismo monto, y ahí recién me deja grabarla y conciliarla.

Speaker 02 [07:01:50]: Perfecto.

Speaker 01 [07:02:30]: Si no me da igual, tengo que ver en cuál de los dos registros me falta información.

Speaker 02 [07:03:10]: Y en ese caso, por ejemplo, cuando tengas, cuando tienes diferencia, ¿este sistema te permite ir directamente como al registro o tienes que ir manualmente?

Speaker 01 [07:04:30]: Tengo que ir manualmente.

Speaker 02 [07:04:41]: Sería bueno que te dé el link directo para ir a modificar el registro.

Speaker 01 [07:05:30]: Exacto, sí, eso sería una mejora también de más rápido. Y generalmente siempre debería estar la diferencia en la parte contable, porque la cartola debiese ser una sola, claro. Pero como nosotros hacemos la cartola manual, que está sujeta a errores humanos, tenemos que buscar en los dos. Entonces a veces no sé, pues tenemos 300 registros mensuales y tenemos que ir por fecha, por monto, e ir calzando de a poco. Y en algún momento te queda algún comprobante en el lado del debe, en el lado del haber.

Speaker 02 [07:12:01]: Eso es lo que me mostrabas de que antes de ayer, de que tenías que ir uno a uno revisando, ¿verdad?

Speaker 01 [07:13:00]: Sí, mira, deja ver si en otra empresa está alguna carta a la pendiente. Ya, mira, por ejemplo, acá falta que suban la cartola. Entonces a mí me aparecen todos los movimientos que se han hecho con banco, y una vez que suban la cartola me van a aparecer todos los movimientos de la cartola.

Speaker 02 [07:20:01]: Perfecto. Y ahí debería hacer match con lo que aparece a la derecha.

Speaker 01 [07:20:31]: Claro, si yo pincho acá y pincho acá, me debiese dar lo mismo.

Speaker 02 [07:21:40]: Captura pantalla. Y también tiene diferencia, claro.

Speaker 01 [07:23:01]: Aquí también falta que suban la cartola. Sí, entonces lo ideal quizás acá sería que uno pudiera subir la cartola diaria o semanal y con la misma cartola ir contabilizando. Claro, quizás pescar el movimiento y el contabilizar, pescar el movimiento y la contabilizar, y ahí aparezcan solamente los movimientos que no están contabilizados, porque ya estando en la cartola son sí o sí los oficiales. Sería como más eficiente de esa forma y menos errores, porque al final si está en la cartola, yo sí o sí tengo que contabilizar lo que está en la cartola. Entonces, el momento de yo contabilizarlo sería ese movimiento conciliado al tiro. Y si yo voy a ver los movimientos pendientes, me van a aparecer al tiro los que me faltan por contabilizar. En cambio, acá lo hacemos al revés, vamos viendo la cartola en el banco, vamos contabilizando, y una vez que ya es fin de mes, porque también no nos enreda subir varias cartolas en el mes, porque cuando uno quiere buscarlas, que es acá cuando las carga, aparecen todas históricas.

Speaker 02 [07:34:41]: Qué bueno.

Speaker 01 [07:35:10]: Si queremos eliminar alguna, tenemos que buscar muy minucioso. Por ejemplo, la de junio. Si yo pongo junio, me aparecen todas las que yo le escribí que es junio.

Speaker 02 [07:37:30]: Claro.

Speaker 01 [07:37:50]: Mira, 2024, 2026. Si yo la pincho, me aparece el estado que están todos los movimientos conciliados. Si aquí hubiera uno pendiente, me aparecería sin conciliar. Listo. Bueno, y ahí podemos ver el proceso de conciliación, reversarlo, el proceso de conciliación cuando tenemos errores.

Speaker 02 [07:42:40]: Podríamos ver esas pantallitas igual para tenerla como antecedente.

Speaker 01 [07:43:30]: Ya, mira, acá está la reversa de la conciliación. Entonces está la empresa, yo pongo el mes Por ejemplo, 06 del 2026, y pongo si quiero reversarlas todas, solo las automáticas o solo las manuales. Como nosotros ingresamos todo manual, pero uno nunca sabe si hay algún, algún saldo que se haya hecho automático, ponemos todas. No te aparece, por ejemplo, un listado del mes y tú que quieras desconciliar solo una. Para poder editarla, porque una vez que uno concilia el movimiento bancario, después uno no lo puede editar en el módulo de contabilidad.

Speaker 02 [07:50:01]: Que eso corresponde, eso está bien, ¿verdad?

Speaker 01 [07:50:41]: No es una limitación, eso está bien, eso está bien. Pero sí nos ha pasado que, por ejemplo, nos damos cuenta en la revisión que, no sé, pues un pago no se fue, por ejemplo, a Santa Pilar y se fue a Los Palos, o se fue al EME. O a otro cliente y queremos solamente modificar ese movimiento, tenemos que reversar todo el mes, modificar el movimiento, volver a conciliar y volver a revisar.

Speaker 02 [07:55:11]: ¿Habrá alguna razón de ser de que sea así de estricto, o es solamente porque no se consideró de que podría haber ese error?

Speaker 01 [07:56:40]: Lo que pasa es que se supone que cuando uno hace el movimiento bancario y lo contabiliza, no deberían haber errores porque el registro es a quién es y el monto que es. Pero, ¿qué pasa al momento de contabilizarlo? Como no se hace directamente del movimiento del banco, uno igual puede cometer errores de equivocarse en el cliente, equivocarse en el proveedor.

Speaker 02 [08:01:01]: Se debería evitar eso haciéndolo en el orden correspondiente, directamente desde acá y no partiendo desde el banco hacia atrás, ¿verdad? Exacto, perfecto. Igual vamos a tener en consideración porque me parece extraño de que sea tan restrictivo. Quiero creer de que es por limitancias, de que no se consideró pensando en que claro, no se debería haber generado esa diferencia, pero igual lo vamos a tener en consideración de que al menos el software lo hacía así, pero dejando la opción de que te permita editar y no tener que hacer todo el mes de nuevo.

Speaker 01 [08:06:50]: Claro, mira, por ejemplo, acá en el módulo que te mostré de calce, que nosotros decimos calce, pero en realidad son los pagos de proveedores o pago de clientes. Si yo estoy ingresando a la cartola, yo acá debiese buscar la factura, pinchar la factura y pagarla. Entonces ahí no va a haber un No debería dar paso a la diferencia. Claro, porque al final yo estoy registrando que efectivamente fue tal factura la que a mí se me pagó. Claro, pero ¿qué pasa? Nosotros acá igual trabajamos con mucho anticipo, entonces el anticipo tú sí o sí lo tienes que ingresar en el módulo de contabilidad. Por ejemplo, te voy a mostrar un producto. Para que nos entienda la— ya, mira, por ejemplo, este productor tiene facturas y tiene anticipos. Si tú te fijas, los anticipos ninguno corresponde a la facturación.

Speaker 02 [08:19:20]: Eso, por ejemplo, tú lo identificas como anticipo por el tipo de documento, ¿verdad?

Speaker 01 [08:20:10]: Sí, por el tipo de documento y porque al momento de uno ingresar el movimiento bancario tiene que poner si es egreso o ingreso, que es igual, se pueden equivocar. O sea, aquí también podría decir ingreso, la I, y estar con anticipo y el saldo negativo. Por ejemplo, acá hay un traspaso que para nosotros anticipos, pero tuvimos que hacer el movimiento manual porque quizás ese anticipo tuvimos que dividirlo en 2 y calzar una parte con una factura y la otra parte queda pendiente. Entonces ahí ya queda en traspaso, porque no hubo movimiento directo al banco.

Speaker 02 [08:27:01]: Al fin y al cabo, igual el tema de los traspasos hace como que existan este tipo de diferencias, más que nada por el cómo se están registrando actualmente, ¿verdad?

Speaker 01 [08:28:40]: Sí, o sea, bancariamente no nos hace ninguna diferencia, porque al final el mismo ingreso nosotros lo dividimos en 2.

Speaker 02 [08:30:40]: Vamos entonces a tener en consideración esto para armar el módulo de tal forma de que idealmente los registros vayan directamente en orden como deberían ser, para que no tengamos estos ingresos manuales.

Speaker 01 [08:32:40]: Mira, que te voy a dar un ejemplo de buscarse cómo para que no genere diferencia tipo de cambio. Ya, yo voy a pagar con Banco Chile, ya. Voy a poner costo. Creo que aquí está un poco más enredado.

Speaker 02 [08:36:11]: Lo bueno es que está todo grabado y después yo veo el vídeo y va surgiendo más dudas.

Speaker 01 [08:37:01]: Ya, mira, por ejemplo, el código financiero a nosotros nos ayuda a hacer el flujo de caja. Vale, ya. Entonces este, como es productor, es materia prima. Entonces nosotros, si después queremos saber cuánto gastamos en materia prima, Vemos el flujo de caja. Claro, supongamos que vamos a pagar esta factura, esta factura, y yo voy a tomar este anticipo. Pero yo, para que me tomen el anticipo, y acá lo modifico y le pongo que solo el anticipo voy a sacar 2 millones 718,836. Ya. Entonces, como estoy calzando en pesos, estoy usando el Banco Chile Peso, y el monto en pesos me queda en cero, pero en dólar tengo una diferencia, que es la diferencia que se me produce cuando yo ingreso la factura y me llega el dinero, o yo pago, que está acá, me genera una diferencia en dólar. Yo voy a guardarlo. Y acá me hace el asiento contable y no me calcula la diferencia en dólares, a diferencia del otro lado. No me la calcula, como que me la oculta.

Speaker 02 [08:50:00]: Sí, me indica que es porque los reportes no se actualizaron quizá en algún momento.

Speaker 01 [08:50:50]: Yo creo que es porque igual me explicaron que el módulo no estaba hecho para calzarlo.

Speaker 02 [08:51:51]: Claro, me imagino que lo ajustaron en su momento, pero la parte de repostería parece que no le hicieron el ajuste.

Speaker 01 [08:52:51]: Exacto. Mira, ahora lo voy a reversar. Buena reversa.

Speaker 02 [08:53:40]: Otra reversa.

Speaker 01 [08:53:51]: Otra reversa. Y vamos a usar el mismo proveedor, o sea, productor, perdón. Pero vamos a pagar en dólares. Entonces yo voy a tomar la misma factura y el mismo anticipo, y acá lo modifico en dólares. Menos 342,80. Ya me da el monto en dólar 0 y un monto de diferencia en pesos, ¿cierto? Sí. Ya yo lo grabo y acá sí debería calcularme la diferencia de tipo de cambio, que es el ajuste automático, y aparece como ajuste automático. Claro, esto está bien. Pero al hacerlo en pesos también debería calcularme la parte de dólar, y al final es el mismo efecto pero al revés, ¿no?

Speaker 02 [09:06:01]: Sí, sí.

Speaker 01 [09:06:11]: Entonces eso como que nosotros no nos explicamos por qué sí lo hacen cuando pagamos en dólar en pesos, pero no lo hace cuando lo hacemos en pesos en dólar, si se supone que tiene doble moneda.

Speaker 02 [09:07:51]: Bueno, igual esto lo tenemos en consideración ahora y se replica en todo aspecto de lo que vendría a ser estos comprobantes, así que Por eso no habría ningún problema, pero este sería el correcto, el borrar correcto.

Speaker 01 [09:11:10]: Y ahí estarían como los módulos completos. Igual yo creo que el de tesorería la vamos a tener que dar otra vuelta porque es uno de los módulos que nos importa que quede muy bien, porque la idea de acá es también sería que pudiéramos ver las nóminas de pago, lo que está próximo a vender, lo que tiene, no sé, un atraso de más de 90 días.

Speaker 02 [09:16:20]: Perfecto.

Speaker 01 [09:16:30]: Mira, en eso nos ayude más llevar un control de lo que nos deben pagar y lo que nosotros tenemos pendiente.

Speaker 02 [09:17:31]: Mira, para eso nosotros igual habíamos planificado el desarrollo para tener feedback de ustedes lo antes posible. Por ejemplo, nosotros tenemos ya una vista. De hecho, mira, va a compartir un poquito de pantalla yo para mostrarte que la idea es que también la próxima semana empiecen a revisar lo que vendría a ser el tablero donde tenemos el Trello. Y ahí nosotros vamos a subirla, el cómo vamos maqueteando. De momento solamente maqueta. Lo que vendría a ser la aplicación. Entonces aquí tenemos el tablero del Trello, y como lo habíamos visto en la reunión pasada, prácticamente cada una de estas tarjetitas que está acá son una pantalla de las que nosotros tenemos nuestro software, que ahora vamos a ver. Por ejemplo, el del panel principal. Entonces nosotros les dejamos la información aquí, más una pequeña descripción de lo que hace con la captura de pantalla. Más adelante les vamos a pasar directamente un link para que ustedes puedan acceder a esta maqueta y puedan también tomar capturas de pantalla, la vayan revisando. La vamos a dejar publicado como en un servidor de prueba. De momento lo tenemos local, así que estamos con capturas de pantalla, pero próximamente lo vamos a dejar para que puedan acceder. Y aquí tenemos lo que vendría a ser la primera parte de la maqueta, que ya tiene algo de funcional. Entonces Acá ya vamos implementando lo que vendría a ser cada uno de los módulos, y la idea tiene esta parte de acá que es modo demo y el modo real. El modo demo tiene información que está puesto solamente a modo de maquetación, y el modo real, el que se conecta a la base de datos. Ahora, como no tienen acceso directamente porque no lo hemos publicado de momento, las capturas de pantalla que nosotros les vamos a dejar va a ser solamente del modo demo. Que ya esté información de prueba solamente para que puedan visualizar. Y la idea es que, por ejemplo, ya para la próxima semana vamos a ir haciendo la construcción. Como ya les tenemos las capturas de pantalla y ya con estas reuniones ya sabemos los ajustes que tenemos que tener en lo básico, que vendría a ser como la cantidad de menús, la idea es que nosotros les dejemos ya en primera instancia el acceso a las capturas de pantalla y ustedes vayan discriminando: falta esto, hay que agregar esto, esto sobra, como a nivel bien general. Ya, entonces la idea también de que junto con los avisos, por ejemplo, si aquí en el panel operativo hay algún alcance, la idea es sacarle captura de pantalla. Y aquí tú también tienes acceso a este tablero, si gustas te puedo dejar el link. Aquí nos puedes dejar el comentario y le puedes pegar también la captura de pantalla junto con lo que necesitas que corrijamos, y Buenísimo. Por ejemplo, se entiende de que la disponibilidad de tiempo es acotada durante el día y quizás no vamos a coincidir en los tiempos. Entonces, mientras no estemos como en reunión y haya un poquito de disponibilidad, o por ejemplo a veces que necesitamos de que algún módulo tener el feedback de otra persona, lo vayan revisando por mientras desde acá y nos vayan retroalimentando con cualquier cosita que vayan pillando. Por ejemplo, las que tienen 2 capturas de pantalla es porque hay una opción que sale una ventanita, entonces a lo mejor Puede que nos digan, pues, sabes qué, de lo que vendría a ser los registros de empresas necesitamos que haya más información, algún contacto, algún número, y nosotros vamos nutriendo. Ya. Y bueno, de lo que vendría a ser la construcción actual de la aplicación, tenemos implementado en el modo real lo que vendría a ser la gestión de las empresas que se van agregando, el tema de los usuarios y los roles. Y entonces con este software la idea también que ustedes puedan ir agregando usuarios a medida de lo que vayan necesitando.

Speaker 01 [09:57:20]: Ya ahí podemos poner, por ejemplo, pinchar lo que quiere el usuario y no como que es que tan rígido como usuario digitador, usuario administrador.

Speaker 02 [09:58:41]: De hecho es más configurable y hay quizás, la idea es que nosotros le dejemos idealmente en primera instancia los roles ya listos, que ustedes no tengan que crear roles, pero esto da la posibilidad de también crear nuevos roles. Por ejemplo, aquí está el de digitador, y si uno va aquí te dice los permisos que tiene. Esta lista la vamos a implementar de mejor manera para que aquí salga un seleccionable y que estos nombres sean más específicos, ¿se entiende? Igual que el read es solamente leer y el write sería el que te permite editar. Entonces, por ejemplo, acá en el caso de que necesiten una persona que tenga un acceso mucho más limitado, que sea solamente visualizador, Podrían generar aquí un permiso nuevo para que acceda solamente a ciertas listas, y eso también limitaría los menús que aparecen acá. Ya, entonces aquí vendría a ser la parte de los roles, aquí vendría a ser el usuario. Por ejemplo, acá en el usuario yo le asigno el rol, y el rol es donde yo detallo qué permiso tiene.

Speaker 01 [10:08:20]: Buenísimo, porque igual yo ahora te traje 2 ejemplos de usuarios que tenemos adicionales al que tú ves ha visto ahora.

Speaker 02 [10:09:31]: Exacto. En ese caso, por ejemplo, lo que me mencionabas de que los digitadores a veces necesitaban tener acceso a información, pero que era peligroso que tuvieran acceso a escribir. Aquí perfectamente podrías configurarle, tanto si olvidó la contraseña, hay que hacer alguna actualización de correo, que a veces también pasa. Aquí también podrías decir de que ya esta persona, ponte tú, tenga el rol de digitador, o puede ser que a lo mejor tengan los roles segmentados. Ponte tú tengas los digitadores que puedan acceder a la página 1, 2, y puede que tengas, por ejemplo, no sé, por la secretaria que puede acceder al módulo 3 y 4. Toda una persona podrías darle el rol de secretaria y el rol de digitador para que pueda tener acceso a esos 2 módulos sin que tenga acceso, como por ejemplo el de administrador que tiene acceso a todo.

Speaker 01 [10:17:21]: Igual sería bueno que, por ejemplo, si yo pongo modo digitador, igual me aparecieran las pestañas a las cuales no tiene acceso en caso que le tenga que dar quizás un acceso en específico. Porque aquí, ¿qué pasa? Nosotros tenemos, como te contaba, tenemos dos rubros. Tenemos el rubro de exportaciones de servicios y tenemos el rubro agrícola. Claro, pero en el rubro agrícola igual está segmentado. Por ejemplo, tenemos una administrativa que tiene que ver a los contratistas.

Speaker 02 [10:22:41]: Me imagino que solo ella.

Speaker 01 [10:23:01]: Exacto, pero ella es digitadora, pero al final es solo de ese módulo.

Speaker 02 [10:23:41]: Ah, perfecto, esto calza perfecto con esa descripción. En ese caso, por ejemplo, lo primero que tú tendrías que hacer es el rol. Ahí, por ejemplo, dependiendo del nombre, y acá la idea es que te aparezca un listado con las pantallas y la opción de leer y escribir. De momento lo tenemos así porque es la forma en que nosotros podemos ver los comandos que vamos guardando, pero a ti después, al final, se te va a reflejar como una lista con todos los paneles. Por así decirlo, y aquí otras 2 listas que sea un check con lectura y un check con escritura.

Speaker 01 [10:29:11]: Perfecto. Entonces tú creas visualización, exacto.

Speaker 02 [10:30:00]: Entonces tú puedes crearle a ella, solamente a ella, un rol. Por ejemplo, este caso sería el rol prueba. Aquí como no me permite sin completar el campo, pero aquí te va a aparecer ese nuevo rol. Y al momento de que, por ejemplo, puede que sea una persona que ya trabajaba, puede que sea un cargo nuevo, ahí va a depender. Lo puedes editar si ya trabajaba y le asignas el rol que creamos, o puedes crear el usuario nuevo directamente con el rol.

Speaker 01 [10:33:50]: Ya, buenísimo.

Speaker 02 [10:34:01]: Entonces ahí segmentaríamos lo que vendría a ser los permisos para cada usuario y también restringiríamos el acceso a todos los datos para cada una de las personas que tengamos dentro del sistema. Entonces quizás como primera partida lo que podría ser bueno es cómo saber los roles que ustedes tienen actualmente, o si es que hace falta quizás dejar unos 2 o 3 roles para que ustedes los puedan ir configurando.

Speaker 01 [10:38:11]: Sí, yo creo que actualmente tenemos 3 roles como bien definidos y algunos mix.

Speaker 02 [10:39:10]: Que me imagino que los mix los tienen en un rol que no les corresponde, pero tienen que ir como jugando con eso.

Speaker 01 [10:40:11]: Sí, eso fue el problema que tuvimos en un momento con el usuario de Rodrigo, que es la persona que te estaba comentando el tema de contratista. Claro, porque él es el encargado de la agrícola contablemente. Que necesitaba tener acceso a más información que un digitador, pero no tanto acceso como a un administrador.

Speaker 02 [10:43:40]: Perfecto. Entonces con esto mitigamos todos esos casos de que hay personas que hay que tener ojo con lo que hacen. Con esto lo mitigáis, porque si necesita ver, vea, pero no pueda escribir.

Speaker 01 [10:45:20]: Claro.

Speaker 02 [10:45:30]: Perfecto. Mira, pasando un poquitito a las otras pantallas que tenemos, que igual sería bueno si es que hay alguna cosita que se nos vaya. Obviamente esto estaba pensado, de todas formas lo estamos ajustando a medida que hemos visto el software, entonces quizás hay pantallas que tú me vas a decir, oye, pero esto como que no aplica mucho a nuestro sistema, me avisas de inmediato y las vamos eliminando. Por ejemplo, aquí en los catálogos, el tema de las monedas, la idea todavía no está implementado, de hecho aquí aparece en la parte de abajo los indicadores del Banco Central, la idea es que acá en lo que vendría a ser monedas nosotros tengamos un botoncito que diga traer información del Banco Central. ¿Para qué? Para que tú puedas visualizar de manera independiente, sin interceder, lo que vendría a ser lo que aparece de los indicadores del Banco Central. Los puedas visualizar acá, pero donde tú tengas el control de dónde traerlo y dónde actualizarlo, o sea, acá. Y acá la idea es que tú puedas configurar si es que se hace de forma automática y a qué hora. Ya, entonces aquí sería como una visualización, y aquí sería como para ver los indicadores del Banco Central pensando en que hay alguna, siempre tenemos que pensar de que cuando son cosas de un sistema externo pueden haber errores, pueden haber errores del sistema externo. Entonces la idea de que sea configurable en esta parte donde ustedes ven los indicadores que tienen actualizados en su sistema, y aquí tengan como que vendría a ser lo que nosotros llamamos entre comillas integraciones, que este vendría a ser el Banco Central. Y vean en qué está actualmente el Banco Central, quizá que un botón de actualizar en caso de que la página no haya, no se haya recargado, hay algún error de internet. Por ahí tenemos como esa diferenciación. Tenemos, bueno, aquí vendría a ser todo lo que es configurar. ¿Te acuerdas que me habían mencionado que también tenían una parte donde configuraban las unidades de medida? Sí, este sería como el panel donde tenemos, podemos configurar qué unidades de medida se ocupan en el sistema. Y aquí tendríamos lo que vendría a ser el tema de los centros de costos. Si mal no me equivoco, por lo que me comentó el equipo de desarrollo, así sí aparece, se aparece el editar. Entonces, por ejemplo, acá sí está con poca información. Quizás a lo mejor aquí hace falta algún contacto del encargado del centro de costos. Podríamos ir agregando toda esa información, pero aquí la idea es que configuren los centros de costos que tienen actualmente. Igual lo que te comentaba siempre, si necesitan, si ya tienen datos y puedes como Extraerlos con una captura de pantalla. Si me los mandas, nosotros los dejamos del día 1 integrado en el sistema.

Speaker 01 [11:10:31]: O sea, lo que nosotros podemos mandarte ahora sería, bueno, igual lo voy a ver con Mario porque queríamos cambiar algunos centros de costo y elementos de costo.

Speaker 02 [11:12:00]: En ese caso, por ejemplo, nos podría mandar la lista de cómo lo quieren y nosotros lo integramos. Y bueno, esto siempre queda la posibilidad de editar del administrador. Entonces, si hay algún ajuste que se hizo durante el tiempo que no entregaron los centros de costo cuando tengan implementado el sistema lo van a poder editar sin problemas.

Speaker 01 [11:14:30]: Pero mira, ¿te parece que igual te mando lo actualizado por último? Después lo editamos.

Speaker 02 [11:15:10]: Sí, por supuesto.

Speaker 01 [11:15:20]: Ya, por supuesto.

Speaker 02 [11:15:51]: Y aquí tenemos, por ejemplo, los tipos de documentos que se manejan dentro de la organización, que también se pueden agregar e ir editando. La idea es que como que todo lo que sea parámetros esté dentro de lo que vendría a ser esta parte de catálogos. Y si es que se nos escapa alguna información también, que Deberíamos tener aquí un submenú, sería ideal. Por ejemplo, del módulo de contratistas también lo mismo está implementado, si no me equivoco, en el modo real. Así también está en el modo real. Esto ya está conectado con la base de datos, entonces yo podría crear un contratista, por ejemplo, vamos a crear uno de prueba y le colocamos prueba, no borrar. Y esto de momento está local, no está como en una base de datos. Ahí está, perfecto. Entonces aquí vendría a ser contratistas, sus tarifas y labores, todo bien configurable. La parte que vimos, idea de proformas, quizás está un poquitito desactualizada, que con la reunión de hoy la vamos a actualizar a lo que ustedes ya necesitan. Traspasos y cierres. Y eso va a grandes rasgos, los demás paneles no los vamos a revisar porque eso sí tengo entendido de que están solamente con el modo de prueba. Ya, entonces la idea es que durante estos días que nosotros nos llevamos todo esto de la reunión para seguir trabajando por debajo, yo creo que igual en la próxima semana, el martes, vamos a tener un reo en caso de que viernes y lunes salgan dudas. O si es que tienen algún caso específico también que nos quieran mostrar. Y ya el mismo martes planearíamos si es que el miércoles va a ser necesario o no, o el jueves. Igual yo tengo disponibilidad, como te dije, en caso de que haya alguno de esos casos que pasan una vez a las mil y lo podamos grabar para tenerlo de evidencia, me avisas por WhatsApp y hacemos reunión de inmediato. O en el caso de que, por ejemplo, sea algo muy acotado, también si tienes la posibilidad de grabarlo o solamente mandar capturas de pantalla de esos casos, también sería bueno. Ya, y bueno, la invitación ahora también sería que en caso de que tengas dudas me puedes ir consultando, puedes diciendo ahí al grupo de que vayamos nutriendo. Ahora, por ejemplo, hay capturas de pantalla que esto ya para la próxima semana me comprometo dejarlo actualizado con el feedback de esta reunión, para que desde el lunes o martes quizás nosotros demos el visto bueno de que con esta reunión de la semana ya la info está actualizado y replicado del software que tienen actualmente. Y ahí vayamos nutriendo lo que vendría a ser la parte visual. Y ya teniendo la parte visual con todo lo que ustedes necesitan, nos enfocamos directamente en lo que vendría a ser la lógica. Y en esa parte de la lógica, ahí quizás ya un poquitito más avanzado, va a ser cuando tengamos software quizás publicado. La idea es que en paralelo, si tienen que hacer un proceso, yo me pueda conectar con ustedes e ir haciéndolo también en este sistema para ir viendo el resultado.

Speaker 01 [11:46:31]: Ya, buenísimo. O sea, nosotros entre antes podamos ir haciendo las pruebas en el sistema, mejor.

Speaker 02 [11:47:41]: Perfecto, perfecto. La idea es que lleguemos a un punto que hagamos estas pruebas en paralelo lo antes posible, ya que con eso realmente en la planificación todo se ve bien, pero el momento de hacer la marcha blanca ahí es donde se ven los verdaderos problemas. Entonces nuestra idea es quizás, aunque sea un poquitito apurado, tener listo la marcha blanca, quizás no con todo el software listo, pero para ir probando con ejecuciones reales y tener el feedback que realmente sirve.

Speaker 01 [11:52:00]: Sí, de hecho, en la primera reunión, una de las primeras reuniones que tuvimos con Sergio, también vimos, tuvimos reunión con Cristian, que es el comercial de VoSocket.

Speaker 02 [11:54:00]: Eso sí, sí, sí.

Speaker 01 [11:54:11]: Entonces, entre ellos igual comentaron el tema de la implementación y del cómo del del match que va a hacer la página con GoSocket.

Speaker 02 [11:55:50]: De hecho, eso también te iba a preguntar, porque dentro de los pendientes que teníamos acá de nuestras preguntas, y nos surgieron estas dos. Bueno, el tema de las facturas afecto de extenso, creo que ese ejemplo no lo pudimos ver teniendo los dos, ¿verdad? Sí, creo que sí lo vimos, ¿cierto?

Speaker 01 [11:58:31]: Sí, sí lo vimos.

Speaker 02 [11:58:41]: Perfecto.

Speaker 01 [11:58:51]: Y lo que sí te comenté era que, por ejemplo, si yo ponía factura afecta y la orden de compra venía con exento, me daba una alerta.

Speaker 02 [12:00:20]: Eso es lo que nos quedaba también pendiente que teníamos acá, el tema de la integración con Gozo, que no sé si es que estás enterada de cómo funciona eso.

Speaker 01 [12:02:20]: Mira, estuve en la reunión, pero ellos hablaban entre ellos, yo no entendía nada de lo que hablaban.

Speaker 02 [12:03:10]: La idea entonces sería que tengamos una reunión con Cristian, me dijiste, ¿verdad?

Speaker 01 [12:03:50]: Sí, lo que pasa es que nosotros ahora vamos a firmar la propuesta que nos mandaron Y una vez que nosotros firmemos, nos van a agendar una reunión con el equipo de soporte que nos va a hacer el traspaso de Acepta a WhatsApp.

Speaker 02 [12:05:51]: Perfecto.

Speaker 01 [12:06:10]: Eso creo que en esa reunión sería importante que estuvieran ustedes ahí.

Speaker 02 [12:06:40]: Por ejemplo, esas reuniones, aproximadamente, ¿cuándo están? ¿Las tienen planificadas o todavía no hay fecha?

Speaker 01 [12:07:31]: Mira, si yo mando hoy día la propuesta, debería estar la próxima semana ya agendando una reunión con soporte, porque nosotros pedimos que la implementación de WhatsApp estuviera el 1 de septiembre. Entonces nuestra idea es tener todo listo, todo avanzado, terminar de facturar agosto con Acepta y en septiembre hacer el cambio definitivo a Osoquet. No tenemos en esos sistemas, no tenemos el mes de prueba porque una vez que nosotros demos de baja un sistema, al tiro se borra la base de datos de ese sistema.

Speaker 02 [12:13:11]: Ah, ok, entonces la idea es implementación a las finales. Mira, en ese caso lo que se me ocurre es que todavía no, si es posible retrasar esa reunión, sería bueno para que dejemos lo básico del ERP nuevo, y ya teniendo lo básico del ERP nuevo junto con las correcciones que vayamos teniendo de ustedes, ahí tengamos las reuniones con GoSocket para ir implementando junto con las correcciones.

Speaker 01 [12:17:00]: Ya, igual de todas maneras nosotros habíamos comentado que, porque le habíamos comentado a Sergio que quizás esta implementación iba a ser a 6 meses, pero igual creo que va a ser en menos plazo. Sí, sí, ya. Y con GoSocket queríamos partir sí o sí en en septiembre. ¿Cuál es la única limitante que tenemos? Que al final, o sea, no tenemos ninguna limitante si no está listo en paralelo con el ERP de AlmaWeb.

Speaker 02 [12:21:21]: Claro, es para poder liberar uno y poder tomar el otro.

Speaker 01 [12:21:50]: O sea, lo que pasa es que AlmaWeb y GoSocket son independientes, independientes, que van a estar conectados. Porque a nosotros lo que nos importa es que GoSocket nos deje listo para facturar. Pero ya si, por ejemplo, en 3 meses más está listo AlmaWeb para conectarlo con GoSocket, nosotros hacemos la pega de nuevo y punto. Si más que nada la idea de que GoSocket esté conectado con el ERP de AlmaWeb es que nos aparezca el libro de compras en línea y podamos contabilizar directo.

Speaker 02 [12:26:30]: Perfecto.

Speaker 01 [12:26:31]: Que era una de las cosas que habíamos comentado, pero de lo contrario igual nosotros podemos seguir contabilizando lo que vayamos haciendo en GoSocket en Agrosoft.

Speaker 02 [12:28:10]: No habría una limitancia entonces.

Speaker 01 [12:28:31]: No hay una limitancia. Lo que sí nos importa es que GoSocket nos cumpla y efectivamente nos traiga todos los documentos de aceptar GoSocket. Pero sería un tema de repente entre ellos.

Speaker 02 [12:30:40]: Claro, en ese caso voy a hablarlo bien con Sergio, porque como te digo, yo creo que lo mejor va a ser de que dejemos lo básico por último terminado bien, lo que vendría a ser la parte visual, que eso nos digan todo lo que necesitan, todo lo que haya que agregar y todo lo que haya que quitar. Y ya teniendo trabajo eso listo, partiendo con la lógica de las correcciones de la lógica, ahí sería bueno realizar la implementación. Voy a hablarlo bien con Sergio de todas formas para que lleguemos a un acuerdo en conjunto. Ya, perfecto. Y creo que de las otras dudas que teníamos parece que ya vimos todo. La proforma ya la vimos, ejemplo nota de crédito, la cuenta del digitador. Cuentas contables por tipo de movimiento de bodega. La bodega también revisamos. Factura en existencia también. Y mira, hay algo que me comentó el Sergio sobre los niveles de almacenamiento y el tema sobre las facturas parciales, pero eso me imagino que es más ligado a lo que vendría a ser GoSocket, ¿verdad?

Speaker 01 [12:40:51]: Mira, los niveles de almacenamiento se veía para el tema de insumos de bodega.

Speaker 02 [12:42:00]: Podríamos darle una revisada, Mari.

Speaker 01 [12:42:21]: ¿Te acordás que yo dije que ese módulo nosotros no lo usábamos? O sea, esa pestaña del sistema de bodega.

Speaker 02 [12:43:40]: Me acuerdo que lo vimos, me acuerdo que elegí aquí niveles de almacenamiento.

Speaker 01 [12:44:20]: De hecho, ni siquiera lo tenemos como parametrizado. Entonces acá nos aparecen todas las bodegas, pero nosotros no tenemos ningún nivel parametrizado porque en realidad no lo usamos. O sea, lo que ingresamos a la bodega sabemos dónde está, en qué bodega, y los movimientos que se hacen.

Speaker 02 [12:46:51]: De momento no hay una necesidad de tener todos los niveles. No, perfecto, perfecto. Me quedo con eso entonces. Y no sé si es que habrá algún otro ítem que se nos está escapando, Mari, de lo que yo tenía anotado pendiente.

Speaker 01 [12:49:20]: Lo único que sería, que sería la visualización de otro perfil. Por ejemplo, acá tú ves que tiene acceso a todo.

Speaker 02 [12:50:10]: Sigo, sigo. Mira, igual de todas formas, el tema de la visualización del perfil de digitador no es tan urgente, más que nada porque como vamos a tener el tema de permisología con los roles, va a ser configurable por ustedes.

Speaker 01 [12:52:40]: Mira, pero para que veáis la diferencia, porque ella tiene acceso a las empresas que ve.

Speaker 02 [12:53:30]: No estoy viendo tu pantalla.

Speaker 01 [12:53:41]: No todas. Ay, perdón, se me olvidó.

Speaker 02 [12:54:20]: No, está bien, si hay que resguardarla, sobre todo cuando uno está grabando. Muy bien. Y ahora con el internet todo se filtra y la furan. No, mejor.

Speaker 01 [12:56:00]: Y ahora sí, me metí al perfil de la persona que te había comentado y ella tiene acceso solamente a las empresas que ve. Ok, ya, por ejemplo, yo me meto a Santa Pilar y le aparece solo esta en el módulo.

Speaker 02 [12:58:10]: Mira, entonces el rol digitador con esto lo podemos ya dejar configurado con los permisos.

Speaker 01 [12:59:51]: Pero ella, por ejemplo, es digitadora de contratistas, por eso es muy distinto a, por ejemplo, la persona que yo tengo de analista. Mira, es el rol de la digitadora de contratistas y ella es analista y tiene acceso a más módulos, pero por ejemplo no tiene acceso a parametrización No tiene acceso al de gestión. Por ejemplo, aquí ella no debería tener acceso a parámetros, debería tener acceso solamente a procesos diarios, emisión de informes, y hasta ahí nomás, porque cierre de mes también lo hago yo.

Speaker 02 [13:07:30]: Perfecto.

Speaker 01 [13:08:01]: De insumos, por ejemplo, no tiene acceso a parametrización, pues tiene acceso al movimiento en sí de bodega y a los informes.

Speaker 02 [13:09:01]: Solo ver.

Speaker 01 [13:09:20]: Exacto. Y bueno, y meterse, pero un digitador no debería tener acceso a ingresar la información y a sacar los informes, nada más.

Speaker 02 [13:11:00]: Perfecto.

Speaker 01 [13:12:01]: Por ejemplo, acá tampoco tiene para parametrizar, que eso está bien.

Speaker 02 [13:12:50]: Perfecto.

Speaker 01 [13:14:10]: Esas serían como las principales diferencias.

Speaker 02 [13:14:41]: Entonces, en eso vamos a dejar esos roles listos, y en caso de que se nos escape una cosita, lo podemos ir viendo en la muestra y vamos haciendo los ajustes. Ya, creo que con eso estaríamos, no se nos escapa nada al parecer.

Speaker 01 [13:17:01]: Sí, creo que con eso estaríamos. Ya tendríamos reunión el martes.

Speaker 02 [13:17:40]: Sí, el martes tienes disponibilidad, ¿verdad? Sí, ya, perfecto. Entonces el martes hagamos la planificación de la semana, ¿te parece?

Speaker 01 [13:19:00]: El martes, sí, ya, ya.

Speaker 02 [13:19:40]: Y como te digo, bueno, te voy a dejar igual pasado el link del Trello. El lunes te voy a mandar un mensajito así como, oye, ya están las pantallas actualizadas del Trello. Más que nada como en caso de, por ejemplo, si tienen reuniones con cualquiera de los otros chicos que vayan a tener acceso al sistema, quizás las puedan revisar y ahí quizás tener un feedback interno. Cualquier cosita me van avisando.

Speaker 01 [13:22:51]: Ya, buenísimo.

Speaker 02 [13:23:10]: Eso, vos, Mari, quedamos al pendiente entonces hasta el martes.

Speaker 01 [13:23:50]: Estamos entonces, Carlos.

Speaker 02 [13:24:01]: Ya, pues que tengas muy buena tarde, que te vaya bien.

Speaker 01 [13:24:31]: Igual tú, chao, chao.
