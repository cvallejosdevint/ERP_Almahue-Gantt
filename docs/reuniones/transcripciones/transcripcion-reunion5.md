# Transcripción Reunión 5 (03/08/2026)

Fuente: pegada en chat Cursor · video `fuentes/videos/reunion5-2026-08-03.mp4`  
tl;dv: https://tldv.io/app/meetings/6a71065851275b0013b6f1d9  
Minuta canónica: [`../reunion5-minuta-2026-08-03.md`](../reunion5-minuta-2026-08-03.md)

**Speakers (aproximado):** Speaker 00 = Carlos · Speaker 01 = Sergio · Speaker 02 = (tercero / corta intervención)

> **Reloj:** timestamps tal como vinieron de tl;dv / pegado. Si el player del MP4 no calza, anclar y corregir como en Reu4.

---

Speaker 00 [00:20]: Ya los ajustes no se deployaron al server. Igual habían algunos que estaban con errores, entonces tiraba error al subirse, así que no se terminaron deployando. Los tengo local y de lo que solicitaron, primero lo que vendría a ser las aprobaciones con PIN, que es lo que tengo aquí anotadito para que no vaya perdiendo. Y bueno, aquí como se solicitó, en los roles se dejó la opción de aprobar con PIN, ya que dijeron que era por rol el tema de las aprobaciones. Así que dentro de la opción, en los que estén aquí van a tener habilitada la opción para el PIN.

Speaker 01 [06:41]: Y el PIN, por ejemplo, tiene que ser como un usuario. ¿Cómo sabes cuál es el que va a tener PIN?

Speaker 00 [08:21]: En este caso es para los roles, pues entonces uno crea los roles y aquí le agrega a los usuarios ese rol, y estos usuarios son los que tendrían el PIN.

Speaker 01 [10:10]: Ah, pero es el mismo PIN para todos.

Speaker 00 [10:31]: No, no, no, se activa, se habilita la opción de aprobar por PIN. No es un PIN para todos, es un PIN por cada usuario. Cada usuario puede restablecer su PIN, cambiarlo.

Speaker 01 [12:11]: Ah, no te entiendo. Bueno, derecha. ¿Podéis hacer un ejemplo?

Speaker 00 [12:51]: Sí, por supuesto. Mira, vamos entonces a crear un rol de ejemplo. Va a tener acceso a todo.

Speaker 01 [14:41]: Ah, ya, ya, un rol. Perfecto, ya te entendí.

Speaker 00 [15:11]: Yo como todavía no he creado el rol, todavía ni le asigno usuario, solamente le estoy dando los permisos. Y acá le doy la opción de que ese rol va a poder aprobar con PIN.

Speaker 01 [16:40]: Ya, perfecto.

Speaker 00 [16:50]: Entonces, por ejemplo, yo acá lo creo y después me voy a crear los usuarios.

Speaker 01 [17:31]: Cuando le asignes ese rol, exacto.

Speaker 00 [18:21]: Exacto, y ese lo habíamos puesto el rol ejemplo. Aquí uno selecciona la empresa a la que va a tener acceso esta persona, ya, buenísimo. La contraseña, que es obligatoria, bajarlo como demo123, sin vigencia, y va a ser un usuario activo. Entonces este tipo, cuando se loguee, va a poder aprobar con PIN. Y cómo se vería cuando él se inicie la sesión aquí en su versión. Y aquí también para la contraseña. Lo que sí, y ahí ya siento que hay que darle igual una pasada, porque ahora yo hago el cambio acá, por ejemplo, pongo el PIN nuevo y confirmo y lo cambio. Quizás la idea sería que esto tenga una confirmación por correo, porque igual la aprobación es algo sensible. Claro, cachai. Entonces, como que te mando un correo y que en el correo venga el link para acceder al cambio de PIN, como lo hacen casi todos los servicios.

Speaker 01 [28:50]: Es que en realidad, por ejemplo, si dejáis la trazabilidad y el usuario que lo hizo, sabemos que ese usuario sí registró el PIN y lo editó en línea prácticamente su PIN porque no se acordó, cachai, cuál le había configurado. Eso da igual porque no afecta a los demás.

Speaker 00 [31:30]: Yo más que nada lo decía porque, por ejemplo, en el caso de que no sepan, hay usuarios que tienen los PIN anotados como aquí en el escritorio, darte un ejemplo, ¿cachai? Sería fácil tenerlo o cambiárselo igual. Por ejemplo, si yo no me sé el PIN de, por ejemplo, este es tu usuario y yo no me sé tu PIN y quiero aprobar algo, yo me voy a tu perfil, le cambio el PIN y ya tengo tu nuevo PIN y puedo aprobar. No hay como algo de seguridad que por último llegue un correo que diga hoy está intentando cambiar tu PIN.

Speaker 01 [35:41]: O sea, pero si estáis trabajando con el usuario, ya es vulnerable la cuenta, ya está vulnerada.

Speaker 00 [36:40]: Claro, claro. Es más que nada para evitar el tema de que otra persona pueda utilizar tu computador directamente para probarse, ¿cachai? En caso de que fuiste al baño, el loco entró, cambió su contraseña, se aprobó, y tú no te enteraste hasta que fuiste a probar otra cosa y tenía otra clave.

Speaker 01 [39:01]: ¿Sabéis lo que podría hacer ahí? Al poner cambiar PIN, que te ingrese la clave de la cuenta.

Speaker 00 [40:01]: Ah, toda la razón. Que te confirme con la clave de la cuenta.

Speaker 01 [40:40]: Sí, porque si era el correo, vamos a ser más hueviados.

Speaker 00 [41:10]: Sí, hay que tener el servicio de envío de correo, toda la weá.

Speaker 01 [42:00]: Perfecto.

Speaker 00 [44:31]: Ya, entonces lo que vendría a ser ahora las aprobaciones. Por ejemplo, en este caso lo que vendría a ser las proformas, debería tener aquí alguna parte. Y por ejemplo, aquí al momento de aprobar te dice primero, porque aquí te va a listar las que están realizadas así como a nivel general, pero como estamos en el admin Aquí me va a decir que está solicitado a, y si yo como admin quiero aprobarlo, aquí va a decir esta aprobación no se solicitó a ti.

Speaker 01 [50:30]: O sea, el solicitado, ¿a dónde yo le asigno a quién se lo solicito?

Speaker 00 [51:20]: De los que están con el permiso para aprobar, se te despliega una lista de todas esas personas.

Speaker 01 [52:30]: ¿Podemos hacer un registro?

Speaker 00 [52:41]: Sí, por supuesto.

Speaker 01 [54:01]: Acuérdate que la proforma es como una factura en realidad, o esos campos eran lo que yo había dicho.

Speaker 00 [55:30]: Al menos acá estamos haciendo la proforma, entonces ahí vamos a hacerla. Y aquí me pide solamente de las personas que tienen permiso para aprobar proformas, me muestra la lista de estas personas pensando en que mi jefe de área podría ser Elena o podría ser, bueno, aquí está un cuadro, va a dar el nombre del usuario, ¿cachai? Y aquí esta proforma se le va a ir a esa persona para que me la apruebe. Y esas proformas se ven así al momento de recibirlas.

Speaker 01 [01:02:10]: Ok, te capto.

Speaker 00 [01:02:20]: Y en este caso, como estamos en el perfil de admin Me figuran igual todas las solicitudes, pero me muestra esa advertencia de que si la quiero aprobar, la estoy aprobando a nombre de otra persona. Y estará bien eso, hay que consultarlo, pero es súper fácil dejarlo de que solamente lo vea la persona que lo aprobó y no el administrador, o sea, la persona que se le solicitó, perdón. Sí, más que nada porque la agilidad que me da el perfil de admin, Sergio, que esto sí va a no tener que cambiar de perfil a cada rato.

Speaker 01 [01:07:41]: Ya, claro, también, sí, también.

Speaker 00 [01:08:30]: Pero si se necesita cambiar ese ajuste, lo sacamos rapidito, no hay problema.

Speaker 01 [01:09:11]: Ya, no, pero si te falta bien, porque así puede ser como un súper jefe. Igual va a decir ya, yo pruebo también.

Speaker 00 [01:10:50]: Sí, exactamente, este va a ser como el que no se le puede ir nada del sistema, porque si se le va algo puede dejarla cagada. Y esa aprobación, bueno, está en las proformas y también está en las compras. También funciona con el sistema de aprobación y PIN. También lo que vendría a ser la visualización, de hecho, acá si no me equivoco lo tengo en las proformas, que fue donde se solicitó Entonces eran las aprobaciones, está bien, las aprobaciones de compra, que uno puede ver el detalle de la orden de compra. Aquí viene la que se había solicitado que apareciera el centro de costo. Aquí tenía una duda, así, Sergio. Al momento de realizar órdenes de compra, ya, esto, el centro de costo va asociado por ítem, porque yo le dejé asociado a la orden de compra, pero después viendo, hoy día viendo el vídeo, me surgió la duda si hacían referencia de que por ítem tendría que ir el centro de costo. Sí, es por ítem. Perfecto, lo voy a dar 2 minutos.

Speaker 01 [01:25:40]: No sé si lograste ver el tema de expandir la pantalla de emisión de la 12, ¿te acuerdas que habéis dicho expandir la pantalla de la emisión?

Speaker 00 [01:27:01]: De que quedara más ancha, ¿verdad?

Speaker 01 [01:27:21]: Claro, la verdad, como lo decía estos panes de, ah bueno, ¿cómo se llama esto? Lo que vimos con Better Software, ahí está.

Speaker 00 [01:30:41]: No estoy perdido, Sergio. Aquí así referencia para anotarlo acá y revisarlo después.

Speaker 01 [01:31:41]: Habían dicho de la opción de expandir, quería como esa.

Speaker 00 [01:32:20]: Ah, las ventanas. Sí, la parte visual no lo había, no lo había visto, viejito. Lo voy a tener aquí anotado para dejar la posibilidad de tenerlo como ventana. Sí, porque en esa pestaña que estábamos viendo tenéis razón, estaba muy, muy comprimida.

Speaker 01 [01:34:51]: Claro, sí, no, pero está bien así porque hay goles que le gusta ver bien acotado por un tema de, pero por último no sé si un expandir que tome un tamaño más, al menos por ejemplo esta vista está justa, pero igual este monitor es grande, no sé cómo se verá en un monitor más pequeño, así que igual estaría bueno dejarlo redimensionable.

Speaker 00 [01:39:30]: Sí, porque no cacho cómo se verá un monitor más cuadrado, por así decirlo, porque este igual es como más panorámico la vista. Entonces, con las compras, entonces las órdenes de compra ya las vimos, y eso tiene que ir anotado. Por ítem, perfecto. El libro de compras, aquí me falta el totalizado porque aquí en el, sé que en el libro de venta habían pedido totalizado, pero aquí creo que igual habíamos dicho que quedaran así.

Speaker 01 [01:45:50]: La idea que todos los libros tengan totalizado. De igual forma, esperé que los totales sean como, puta, esa visualización sea como configurable, no sé si Claro, algo así. Pero por ejemplo, si tú lo quieres ocultar, pero sabes lo que ahí sería bueno, Carlos, que en realidad no sé cómo lo podemos hacer. A ver, te voy a compartir pantalla para que veas cómo lo hace hoy en día de Demirel. Que en realidad igual es útil. Está en el auto, hija. Tira la almohada que te voy a buscar. Tira la almohada que te voy a buscar. Ya después, dame un segundito, termino la reunión y voy. Ya verás, por ejemplo, aquí en mis libros Todos los documentos tienen esta misma hoja, que tiene su resumen, ¿cachai? Pero el resumen, si te das cuenta, es como una tablita por tipo de documento.

Speaker 00 [01:59:11]: Sí, está súper buena esa vista.

Speaker 01 [02:00:20]: Sí, voy a, por ejemplo, que esto se pueda ocultar, ¿cachai? Cómo minimizar, pues, de que quede el resumen arribita, una flechita, y esto se oculta.

Speaker 00 [02:02:50]: No sé, con el panel lateral, ¿cierto? Ese que se oculta así como si de la derecha para la izquierda, ¿verdad? Claro, sí, sí, algo así.

Speaker 01 [02:04:40]: ¿Por qué? Porque, por ejemplo, si el que estamos, que está compartiendo, ese es Ahora sí. Por ejemplo, ahí claro está bien el total porque es el IVA completo, pero quiero saber cuántas notas de crédito tengo. Claro, porque ese otro tema para los totales, si podía notar en alguna parte, por ejemplo, las boletas, las facturas, las boletas afectas. Las boletas exentas, las facturas afectas, las facturas exentas y las notas de débito se suman.

Speaker 00 [02:12:11]: Exentas y notas del débito, ¿cierto? Exentas, exentas, exentas, notas de crédito, notas de débito.

Speaker 01 [02:14:30]: Esos se suman a, como esas son parte de tu venta, y solo las notas de crédito son las que se restan.

Speaker 02 [02:16:20]: Vale. ¿Qué más?

Speaker 01 [02:20:20]: Lo que yo te había dicho, por ejemplo, donde dice facciones, el PDF que donde sale el número del documento, ahí, a eso te hace una vista preliminar. Ya, entonces ese PDF que tú tienes El otro, el botón de acciones, no es necesario porque lo tenía acá. Vale, la idea es que la visualización del Pero te voy a compartir pantalla también, un tema que yo bien dibujé. La sesión está aspirada. ¿Están viendo mi pantalla?

Speaker 00 [02:33:10]: Sí, sí, sí.

Speaker 01 [02:33:30]: Comercial, libro comercial.

Speaker 02 [02:34:21]: Está en el periodo de julio, 1 de julio.

Speaker 01 [02:36:10]: Por ejemplo, aquí yo visualizo, cierto, así el formato, ¿cachai? Datos de receptor con los totales abajo. Esto es una cotización, una orden de compra.

Speaker 00 [02:38:50]: Ya, va a sacarle captura de pantalla.

Speaker 01 [02:39:10]: Grabando, grabando.

Speaker 00 [02:39:20]: Vale, sí, porque me hace falta un documento tipo para no fantasmear. Carlos, de hecho, esta vista me gusta porque como lo tengo actual, si te das cuenta, habilita al tiro el panel de impresión del navegador.

Speaker 01 [02:44:11]: Claro, estaba por ejemplo ahí, no me podía imprimir. O descargar como PDF o cerrar.

Speaker 00 [02:45:10]: Sí, está buena esa.

Speaker 01 [02:45:21]: Igual la idea es mantener eso.

Speaker 00 [02:45:41]: Sí, sí.

Speaker 01 [02:45:50]: Por ejemplo, también envío correo. La idea es que puedas enviar correo, ya, a diferentes destinatarios.

Speaker 00 [02:47:00]: Pero en ese caso, como todavía no tenemos servidor, lo podría dejar como opción pero todavía no conectado.

Speaker 01 [02:47:51]: Claro, bacán. ¿Qué más? Por ejemplo, y a ese, bueno, acá este no va a ser como opción para ellos, pero acá yo puedo adjuntar archivos, ¿cachai? Asociarlo al documento. No sé si pasó a todos de nuevo. Y por ejemplo, aquí puedes como anular, ¿te acuerdas de lo que habíamos hablado? Sí. Lo que sí acá era el tema de las acciones. Por ejemplo, este es para registrar el pago, facturar el documento, perdón, este es para facturarlo, convertirlo en un DTE, este es para imprimir, que te levanta el PDF, ya, vale. Este es para enviar correo, este es para adjuntar y este anular. Entonces la idea es que reutilicemos un poquito estas acciones, te las voy a pasar ya. Para que las consideres y las implementes, pues, como lo busques.

Speaker 02 [03:03:31]: Vale, ya eso.

Speaker 01 [03:04:10]: Bueno, los filtros, la idea que también estén los libros, tengan filtros. No sé si le aplicaste filtros tú.

Speaker 00 [03:05:11]: Sí, tengo filtros. De hecho, ahí hay que reformular los filtros, y eso lo hizo igual la IA, porque hay algunos que siento que están de más y que la forma de cómo están hechos están medio feítos. Así que igual habría que darle una Una repasada, que quede más bonito estéticamente. Tienen, funcionan, pero siento que se ven feos.

Speaker 01 [03:08:00]: Ya, ok, bueno, igual te dejé pasado ahí como lo que tengo ahora en DeepSeek.

Speaker 00 [03:08:50]: Ya, vale, bacán.

Speaker 01 [03:09:31]: ¿Qué más? Eso de momento.

Speaker 00 [03:10:51]: Dale, va a cerrar este y este el deploy. Entonces ahora, bueno, con lo que vendría a ser el libro de ventas, se quitaron los accesos directos que tenían entre ellos. ¿Te acordás que estaba acá arriba?

Speaker 01 [03:13:51]: Se lo eliminé a los dos, los dejaste separados.

Speaker 00 [03:14:41]: Perfecto, exacto. Que me fijé de que, por ejemplo, al momento de generar una, por ejemplo, emitir un documento, ella había pedido la opción de dejar como borrador, pero no tenía un menú dentro de todo lo que vendrían a ser las vistas para ver los borradores como tal, ya que acá en el libro de ventas pidieron que aparecieran los que estaban contabilizados. Entonces los pendientes me estaban quedando ahí medio guachitos, los borradores, así que lo implementé acá en este menú como para poder ir viendo. Quedan en este caso como historial. Uno puede ver el documento como predefinido de ese, te aparece con la leyenda borrador igual para verlo como rápido. Y aquí puedes cargarlo para que se te cargue la opción acá. Y por ejemplo, si tú ya tenías uno en el borrador, modificaste algo y necesitas guardarlo pero confirmar, ya sea, no sé, algún ítem de estos de acá, si lo pones guardar como borrador se guarda toda información que actualizaste del borrador. Entonces siempre va a ir actualizándose en caso de que necesitas guardarlo y no finalizarlo, te lo permite el sistema. Ya, entonces, por ejemplo, acá vamos a ver este de carga. Aquí los ítems van con su centro de costo también, ¿verdad?

Speaker 01 [03:29:00]: Los ítems también. Ese es, pero es venta, pero ese va por la cuenta. Ah, pero centro de costo igual ella dijo que iba.

Speaker 00 [03:30:40]: No, voy a preguntarle por interno porque tengo la duda y creo que ahí en esa parte de la reunión se me cayó un poquitito la internet.

Speaker 01 [03:32:20]: Sí, no sé si en la venta, no sé si en la venta en sí, cuando tú estás vendiendo un producto tienes que asociarlo a un centro de costo. Porque la cuenta mayor sí sé, pero por ejemplo centro no lo sé.

Speaker 00 [03:34:51]: Vale, sí, porque quedé con esa confusión porque justo cuando estábamos hablando de esta parte de la emisión de documentos de la venta se me estaba cayendo un poquitito la net, así que iba a quedar como pendiente. Y está con sus cuentas contables, y aquí al darle siguiente Permite agregar referencias, observaciones, y acá también tenemos una previsualización del documento.

Speaker 01 [03:40:01]: Ya, perfecto.

Speaker 00 [03:40:20]: Y bueno, en caso de guardar como borrador, y se va actualizando la lista. Esta lista de borradores sí está asociada solamente al usuario. Yo no puedo ver los borradores de otras personas.

Speaker 01 [03:42:01]: Y antes, puedo ver una aparte de la emisión, no tengo ¿Por dónde? ¿Otro lado verla? ¿Como un libro de borradores?

Speaker 00 [03:43:31]: No, lo dejé solamente acá como menú rápido más que nada. Igual podría hacer un menú acá que sea borradores.

Speaker 01 [03:45:10]: O sea, igual, ¿sabes qué estaba pensando? En el libro de ventas. En el libro de ventas, ¿cuándo te lo—?

Speaker 00 [03:46:10]: Acá lo tengo, aquí, mira. Porque aquí, como habían pedido que solamente apareciera lo contable, no lo dejé así como visible como borrador como tal, pero igual en la reunión estaba puesto como borrador, se podían ver los borradores desde acá, pero como pidieron solamente ver lo contable, lo dejé ahí. Y por ejemplo, el tema de los periodos me pasó. Bueno, esto igual es por lo que te digo de no tener que andar cambiando tantas opciones, de que en algún momento quería ver lo que pasaba en los demás periodos y la habilité esta opción, porque si no te carga de este cliente lo que está en este periodo. Y ponte tú, necesitan revisar algo con agilidad de periodos anteriores, sacar alguna información, alguna captura de pantalla o ver un documento, le di esta opción que te permita ver los periodos anteriores. En este caso, justo hace como media horita limpié la base de datos, así que no tengo, no tengo otros periodos, tengo solamente el de agosto.

Speaker 01 [03:55:31]: Ah, ya, yo lo dejaría, o sea, está bueno, pero es peligroso. No, no, no, no, no, es por el tema de la cantidad de registro. Vale, eso se te va, se te puta. Bueno, no son 30.000, tenemos buenos que emiten 22.000 documentos mensuales, y si le ponía así todos los periodos, puta, eso se te va a pegar el navegador.

Speaker 00 [03:59:50]: Podría ser con paginación entonces, de que te muestre de a 15 para que no se te pegue el navegador, cosa que la consulta traiga los primeros 15, y si le dais siguiente recién busque los siguientes 15.

Speaker 01 [04:01:30]: O yo lo dejaría, por ejemplo, no todos los periodos del año, desde el año actual, o cómo sería.

Speaker 00 [04:02:41]: Y es literal todo de este cliente, ¿cachai?

Speaker 01 [04:03:50]: Y yo lo dejaría como anual nomás. Vale, vale, ya.

Speaker 00 [04:05:51]: Bueno, en el caso de que igual necesiten ver, si no sé, vos dices no, es que yo necesito de repente ver cosas de hace 3 años, podríamos dejar de que esta opción sea solamente máximo 1 año, pero que cuando se apliquen filtros de búsqueda avanzada ahí ya haga otra discriminación.

Speaker 01 [04:09:10]: Claro, por eso yo lo dejaría, por ejemplo, no sé, por los rangos de fecha, pero él va a sacar información de 1 año completo.

Speaker 02 [04:10:21]: Claro, ya, bacán.

Speaker 00 [04:11:40]: Un momentito, y ahora sí, entonces Bueno, las cotizaciones realmente no le di mucha vuelta porque habían quedado con el sistema de aprobación, como lo dijo la María José, que ya actualmente no trabajaban con el sistema de aprobaciones. Y le hablo, le implementé igual que el otro módulo la aprobación.

Speaker 01 [04:17:00]: Las cotizaciones son muy similares a la orden de compra.

Speaker 00 [04:17:31]: Sí, ahí lo tengo con detalle, el estado. Este lo voy a eliminar, sí, porque aquí no debería haber mantención de clientes.

Speaker 01 [04:19:10]: Sí, podría ser, podría ser igual, pero sí, sí, es bastante útil.

Speaker 00 [04:20:21]: O quizás cuando aquí uno, o no, así nomás, no está bien así.

Speaker 01 [04:21:20]: Lo que sí, en vez de que la palabra completa crear cliente, le dejaría por ejemplo un más, ¿cachai? Claro, y que ese más te levante otro modal con el formulario completo del material del cliente.

Speaker 00 [04:23:21]: Sí, porque está como, ocupa mucho, se nota mucho.

Speaker 01 [04:24:10]: Claro, o si lo podéis tirar, sabéis que donde queda filete, cuando aparece como en el lado derecho de la pantalla con un mini formulario, vale, vale, vale, para que no se levante un modal sobre otro modal, ¿me explico? Sí, sí, sí, sí.

Speaker 00 [04:27:20]: Y ahí también la otra información, si igual esto es como RUT y razón social, pero tiene más campos.

Speaker 01 [04:28:10]: Sí, por ejemplo, la dirección, comuna, ciudad, teléfono, correo. Exacto.

Speaker 00 [04:29:20]: Aquí deja agregar más líneas.

Speaker 01 [04:31:00]: Ahí abajo, abajo, me gustaría abajito donde dice neto calculado. Hay harta información en realidad que hay que agregar. En realidad te das cuenta cuando emitamos la factura. Ah, no, pero cuando trabajemos en la emisión de factura, te vas dando cuenta que falta hartos campos. Por ejemplo, el total neto, total exento, total IVA, total en los descuentos recargos globales, descuento recargo a nivel de línea, ¿cachai?

Speaker 00 [04:36:00]: Vale, igual aquí los dejo anotaditos con la transcripción también de la roca que estamos haciendo ahora. Lo aprovecho igual de implementar al tiro, cosa que después sea lo mínimo que falta.

Speaker 01 [04:37:41]: Claro, yo trabajaría así sobre la emisión de factura, vale. Después replicamos para la cotización y las órdenes de compra, vale.

Speaker 00 [04:40:01]: Al fin y al cabo, todo como se relaciona van a tener los mismos campos.

Speaker 01 [04:40:51]: En gran parte sí. Por ejemplo, la Ventas no van con centro de costo. Las órdenes de compra, las facturas recibidas sí deberían ir con centro de costo.

Speaker 00 [04:42:51]: Mira, aquí tengo como el menú de acciones más parecido al de allá.

Speaker 01 [04:46:00]: Ya, eso está bueno. Pero si las acciones tienen que ir toda la línea hacia la derecha, sí, pues tiene que estar acá. Eso, esos botoncitos están perfectos.

Speaker 00 [04:47:31]: Ya los voy a replicar, esto sí también tan bonito. Bueno, aquí en este caso, como estoy desde el perfil de admin, me permite emitir la cotización y todo, por eso tengo todas las opciones, o anularlas también. Entonces ahí cambia el estado emitido y se puede convertir a nota o convertir a factura, y una cotización imprimible. Aquí también voy a copiarme. De casualidad, ¿no tenía algún documento de cotización que me pueda copiar? Igual este está básico.

Speaker 01 [04:54:01]: No, pues, ¿qué demandé yo? Si ese en realidad lo que se va a cambiar arriba El que te envié dice orden de compra, cambia el título, no el título. Vale, hijito, genial.

Speaker 00 [04:57:10]: Mira, acá en el libro de estas hay que modificar esa parte de ahí. Ahí está la cotización, la que recién acabamos de aprobar. Este hay que eliminarlo. Sí, eso hay que eliminarlo.

Speaker 01 [04:59:41]: Eso se elimina, pero la idea es que el folio, donde dice folio, aparezca como que se entiende que un botón, ¿cachai?

Speaker 00 [05:00:50]: O colocarle quizás una lupita ahí.

Speaker 01 [05:01:40]: O por ejemplo, si la bonita que el PDF tiene un borde, un borde, vale, y que sea lo mismo así como aparezca dentro el folio. Entender que va a ser un botón. Lo de los borradores, ¿cómo lo podríamos dejar? Estaba pensando, por ejemplo, si pinchas borradores, que no sé si te los liste así, que en realidad no hay nunca tantos borradores, pero si yo soy súper usuario o administrador, si quisiera ver todos los borradores Los borradores.

Speaker 00 [05:07:50]: Por eso te decía, acá como lo dejé configurado, cada uno, el admin no puede ver los demás borradores, pues, ¿cachai? Podríamos hacer de que acá igual en la búsqueda avanzada te filtre que no sea igual a borrador, cosa de siempre verlo contabilizado y emitido, y en caso de que uno quiera ver los borradores, aquí verlos.

Speaker 01 [05:11:51]: No, pero en realidad, como decís tú, en realidad, puta, ¿para qué querías estar viendo borradores de otras personas?

Speaker 00 [05:12:51]: Sí, yo lo que pienso es que, por ejemplo, no sé en qué te sería útil, y esto es un caso muy rebuscado. Por ejemplo, tenía un trabajador que estaba haciendo uno, lo dejó borrador, se fue. Ahí recién como que el administrador tendría que ver qué estaba haciendo, cómo lo calculó, pero no tiene tanta ciencia porque igual el cálculo no va a cambiar porque otra persona lo revise.

Speaker 02 [05:16:40]: Claro, exacto.

Speaker 00 [05:16:51]: Entonces ese borrador que viva dentro del usuario y que nunca se, o sea, quizás quedaría como información basura, pero cada usuario cuando se meta va a ver ahí que tiene un numerito. Pues ya la gente, créeme que le da toque ver esas cosas. Claro, igual podríamos listar todos los borradores acá como para el admin por último. Así como aquí al admin, en vez de que le muestren sus borradores, de que solamente le muestre la lista de todos y el usuario, y quizás con filtros.

Speaker 01 [05:22:51]: Por filtros, sí, eso, eso. Pero en realidad, como decís tú, realmente van a trabajar con tantos borradores, un buen disperso. Claro, pero sí le agregaría un filtro. Eso para poder que el buen filtre. Y en realidad, si le dais ver, abre, ponele ver, ese te muestra el documento, ¿cachai? Ya, ok.

Speaker 00 [05:27:10]: Y cuando uno le da cargar, se te abre la interfaz de la emisión de documentos con los datos cargados. Ah, perfecto, ¿cachai? Entonces aquí yo finalizaría, y si es que yo lo finalizo, se me borra el borrador. Ya entiendo.

Speaker 01 [05:29:30]: Sí, está bien, bacán.

Speaker 00 [05:30:31]: Vamos entonces con, bueno, la parametrización. También se movieron todos los ítems según como lo solicitó la Mari. De esto realmente no había muchas correcciones, solamente pidieron ubicación de algunos ítems que quedaran acá. Ay, eso no lo borré. Productores todavía lo tenemos duplicado. Voy a sacarlo de compras porque la Mari dijo que lo dejáramos en parametrización nomás.

Speaker 01 [05:38:21]: No, no está aprobado. Están cobrando, están cobrando.

Speaker 00 [05:39:31]: Ya, ya vamos entonces ahora con contabilidad. ¿Por qué no aparecía este periodo si yo lo había borrado? Chan. Ahí sí me cambia el periodo. Eso no me funcionaba, el cambio de periodo desde acá.

Speaker 01 [05:44:00]: Ahí podéis tener más de un periodo activo, o sea, activo lo que hace referencia es en el que tú estás acá, ¿cachai?

Speaker 00 [05:45:51]: Y el estado es abierto, ¿vos cachai?

Speaker 01 [05:46:21]: Ya, a ver, cámbiata, el cambio de periodo. O sea, pero, ¿cuál es la ventaja de hacer eso?

Speaker 00 [05:48:00]: O más que nada para que uno vea aquí que está en ese mes, pues, ¿cachai? O sea, perdón, sí, en ese mes. Pero este de acá no tiene ni una ciencia, si uno lo tiene que manejar de acá.

Speaker 01 [05:49:50]: Claro, porque en realidad después tú vayas a trabajar sobre, en realidad, si lo cambias así, vaya a trabajar con información de quizás de un periodo que no No es el actual, o sea, yo ese no lo ocuparía porque se controla desde acá.

Speaker 00 [05:52:20]: Y por ejemplo, acá, si es que yo lo cambio, ese también me da. Pero mira, eso no se está haciendo, ahí debería actualizarse el activo.

Speaker 01 [05:53:51]: No, por eso yo lo sacaría. Vale, vale, pero sí tienes que tener trazabilidad de quién cierra el periodo, eso sí. Y quién lo abre, ¿me captáis? Y cuando es apertura de periodo, o lo reabre, debe dejar algún comentario.

Speaker 00 [05:58:30]: Entonces, en este caso, lo que me haría falta es que yo pueda aquí tener un ver para ver el historial del periodo, ¿cierto?

Speaker 01 [05:59:51]: Pero, ¿qué te refieres? ¿Qué historial pedíais?

Speaker 00 [06:00:20]: De quién lo abrió, quién lo cerró, porque no tengo historial. Claro, solamente lo puedo cerrar, abrir, pero no puedo consultar quién lo hizo. Eso me falta. Por ejemplo, este, si lo abro, me pregunta, debe también preguntar el motivo para abrir un periodo, ¿cierto? O los periodos no se deberían poder abrir.

Speaker 01 [06:05:30]: Perfecto.

Speaker 02 [06:05:40]: Sí, allá, perfecto.

Speaker 00 [06:06:20]: Y ahí eso iría con la trazabilidad del historial.

Speaker 02 [06:07:20]: Perfecto.

Speaker 00 [06:10:51]: Perdón. Entonces, ¿qué más hizo justo? Espera, que lo tengo aquí anotado. Se me abrieron un poquito las notas. Ya, la configuración del sí, esto ya fue fantasmeo de la IA. Que me dijo que según lo que necesitamos para implementar GoSocket había que tener una configuración contable del SAI. Por eso no lo eliminé. Como todavía no tenemos la documentación de GoSocket, es puro fantaseo del aire.

Speaker 02 [06:16:41]: Vale, usted el experto.

Speaker 00 [06:17:41]: Yo le hago caso a usted.

Speaker 02 [06:19:21]: Perfecto.

Speaker 00 [06:21:10]: Y aquí ya estaba esta parte en la que me faltaba revisar ahora, que es la parte de los comprobantes de asientos contables. Y lo que vendría a ser del módulo tesorería, que es el estado de cuentas, donde están los detalles. Aquí se pueden ver las facturas, que no sé por qué no me está mostrando esas facturas, y aquí me la está mostrando. Ahí tengo un problema. Esa factura no me la está reflejando y es la 88001. Y si yo le doy clic acá para verla, tampoco, pero sí me la realiza para buscar, ¿cachai? Algo está pasando ahí, debe ser por el borrado que hice delante de la base de datos, pero aquí irían asociados los documentos de del estado de cuenta. Y aquí, bueno, los filtros que habían pedido, de todos o solamente los pendientes. Ya, ok.

Speaker 01 [06:34:11]: Ese es el estado de cuenta de los clientes, ¿cierto? Que tenía que verla. Exacto, tiene que ser igual. Por ejemplo, es una, debería poner el tipo, o sea, el tipo movimiento, si es una venta o una compra.

Speaker 00 [06:40:30]: Aquí con el tema de la conciliación también se dejó los pendientes solamente, con la posibilidad de ver un resumen, el cual no me está cargando tampoco, deben ser los datos que se borraron.

Speaker 02 [06:46:00]: Las cartolas bancarias.

Speaker 00 [06:48:10]: Esto todavía no lo he tocado. Esto está pendiente. Y eso es lo que ha avanzado Sergio.

Speaker 02 [06:53:30]: Ya, contratista, anticipo, conciliación.

Speaker 01 [06:55:51]: Bueno, conciliación no está todavía, no, todavía no. Ok, ya, puta, yo creo que ya, bueno, ahora de esta reunión sacamos hartos ajustes. A ver si podemos estarnos para mañana a esta misma hora, ¿te parece? Sí, no hay problema. Ya, o sea, si los tenía antes, me avisáis, nos juntamos y vamos observando lo siguiente. Vale, ya, vacancito. Ya, Carlos, me voy a otro juego por la lluvia.

Speaker 00 [07:02:30]: Por la lluvia. Mañana, mañana no te dejará hablar, te va a dejar una nota así para que digáis sí o no. Ya, vale, ya, viejito. Ya, hablamos. Cuídense, que esté bien.

Speaker 01 [07:04:51]: Igual, chau, chau.
