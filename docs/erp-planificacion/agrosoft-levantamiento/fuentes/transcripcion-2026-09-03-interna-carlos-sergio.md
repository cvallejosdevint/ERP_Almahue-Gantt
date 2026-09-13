# Transcripción bruta (faster-whisper local medium, ES)

Fuente: `Screen Recording 2026-09-03 110956.mp4` (27:41). VAD activo, `beam_size=5`.
Participantes: **Carlos** (desarrollo) y **Sergio** (proveedor). **No hubo cliente en la sala.**

Igual que Reu5: es una revisión interna. Lo que aquí se acuerda son decisiones de
diseño del proveedor, no requisitos del cliente. En `[07:47]` ellos mismos dejan
abierta la pregunta de fondo — «validémoslo con ellos mejor en la reunión».

Alcance que Sergio fija para la demo, `[24:56]`: *«que la presentación del día se
enfoque solamente en órdenes de venta, la facturación, integración con GoSocket,
visualización del PDF y el tracking. Nada más que eso.»*

---

[00:38] Carlos
[00:39] ¿Cómo estáis Sergio?
[00:40] ¿Y tú?
[00:41] Bien, bien
[00:42] Que bueno
[00:45] Vamos, vamos a la revisión
[00:50] Vamos a ver
[00:51] Venga
[00:52] Se ve cierto
[00:58] ¿Tú viejas?
[00:59] Ahí está la doña
[01:02] Le dieron un mes más de licencia
[01:04] Así que tiene que seguir yendo a quine
[01:06] Chucho
[01:07] ¿Qué tiene?
[01:08] Le sacaron la rodilla
[01:10] Y le pusieron una prótesis
[01:12] Oh
[01:14] Ya llevaba un mes
[01:16] Pues ahora le dieron otro mes más
[01:18] De reposo
[01:19] Ah, bien
[01:21] Pero está bien, sí está bien
[01:23] Igual me imagino que es por lo demandante que era su trabajo
[01:26] Igual que le dieron el mes de reposo para que se recupere bien
[01:28] ¿Con qué trabaja?
[01:30] Trabaja en la parte de cultura de la municipalidad de San Bernardo
[01:34] Específico en la Casa de la Cultura
[01:36] Y tiene que gestionar eventos, todas las cuestiones
[01:39] Andar viendo, de repente tiene que andar caminando de la Muni
[01:42] Para la Casa de la Cultura, después a Diteco, entonces
[01:45] Tiene que caminar caliente
[01:47] Ah, chucho
[01:49] Chucho
[01:50] Me das uno más, ¿cierto?
[01:55] Se ve, ¿cierto?
[01:56] Sí
[01:57] Veo
[01:58] Ya, entonces, esto si te das cuenta está en lo publicado
[02:04] Está corriendo en local
[02:06] Ya, estoy bien, sigo
[02:14] Entonces, vamos a elegir un cliente
[02:17] Aquí ya eliminé esos campos que estaban de más
[02:19] De hecho la vista se acortó bastante, queda bien bonita
[02:22] Los indicadores, el de venta
[02:26] Forma de pago de crédito, la fecha de emisión
[02:29] Fecha de vencimiento
[02:30] Este campo yo creo que no aplica así, la verdad
[02:33] Tengo la duda si es que va con fecha de vencimiento
[02:35] Sí
[02:36] Sí, sí, sí
[02:37] La fecha de vencimiento es importante para los documentos
[02:39] Tanto emitidos como recibidos
[02:41] Tiene que ir si o si, ¿cierto?
[02:43] No es obligatorio
[02:45] Ay
[02:46] No es obligatorio
[02:47] Pero sí es importante y yo creo que gran parte lo ocupa
[02:50] Vale, vale, vale
[02:51] Entonces lo vamos a dejar ahí
[02:54] Aquí tenemos la vista
[02:56] Para los detalles del item
[02:57] Si te das cuenta que ya lo dejé más comprimido
[03:00] Para que sea más agradable a la vista
[03:02] Vamos a agregar
[03:04] Uno item más
[03:06] Y éste se queda fijo para todo el usuario de la info
[03:10] Con el descuento global
[03:12] El neto que también está acá y ya no aparece abajo
[03:16] Oye
[03:17] ¿Qué pasa la montaje Carlos?
[03:19] Porque si te das cuenta
[03:21] De cierto modo como que igual ocupa harto espacio
[03:24] Por ejemplo ahí ya tení en la pantalla completa
[03:27] Tení solo cuatro items
[03:29] Se podría agregar cuando te le pones a agregar item
[03:32] Que no que se agregue como una caruga completa
[03:34] Sino que se agregue un campo debajo por ejemplo de ese tipo
[03:38] Cachay como que se vaya construyendo una grilla
[03:40] No sé si me explico
[03:41] Ah sí, sí, sí
[03:43] De hecho me parece muy buena idea
[03:45] Lo voy a implementar
[03:47] Ya buena, buenísimo
[03:48] Cachay
[03:51] Todavía no agregábamos item a otras bodegas
[03:53] Puta la de cera
[03:54] Pero lo mismo
[03:56] Acá por ejemplo si existiera más por este item
[03:59] Podría agregar más bodega
[04:01] De hecho a ver si en el modo demo
[04:03] ¿Se puede visualizar mejor?
[04:05] Voy a dejarlo para la reunión de la tarde que aparezca
[04:08] ¿El cliente no tiene dirección fiscal?
[04:10] Ya
[04:12] Ah y eso es lo otro
[04:13] En cuanto a los clientes, al maestro de clientes
[04:17] Por lo que había solicitado Kozoke
[04:20] Tuve que agregarle obligatorio la dirección fiscal, la comuna, ciudad
[04:24] Sí, eso es obligatorio
[04:26] Muy bien
[04:27] Me di cuenta ahí en los testing
[04:30] Entonces creo que este sí funciona
[04:35] Bueno
[04:37] Vamos a omitir el tema de las bodegas
[04:40] Porque no me lo está tomando bien el modo demo
[04:42] Lo voy a corregir
[04:44] No, pero si querías
[04:46] Vamos con este que tiene que estar una pura bodega no más
[04:50] Ya
[04:52] Porque acá te quería mostrar cómo lo dejé
[04:55] Al momento de que tenga más bodegas
[04:57] Igual lo dejé para que se vea más comprimido
[04:59] Ocupa menos el espacio cuando son más de una bodega
[05:04] Entonces el siguiente
[05:06] Aquí podríamos colocar una referencia
[05:14] Como firmamos el stock
[05:16] Se hace la
[05:19] Así como reserva del stock
[05:21] Y aquí podría facturarlo directamente
[05:23] Entonces
[05:27] Parece factura cargada
[05:30] Oye, pero ¿por qué le poní siguiente ahí?
[05:33] Sí, aquí tengo un error del wizard
[05:35] Porque aquí debería salirme la emisión del documento directo con facturar
[05:39] Sí, no
[05:40] Claro, pero ahí no me diría pasar
[05:43] Para que se pase el flujo real de ello
[05:46] Entonces la orden de venta tú la estás guardando
[05:49] Aquí ve si te das cuenta
[05:51] Cambió al wizard al emitir DT
[05:53] Pero lo hizo automático
[05:54] En vez de hacerle clic acá y darle facturar
[05:56] Se hace como automático esa vista
[05:58] Voy a hacer lo que se pase a esta página no más
[06:00] No, no, no, no
[06:01] O sea, yo ahí mira
[06:03] Tú estás en órdenes de venta
[06:04] Vamos a emitir una
[06:05] Tú vuelve a órdenes de venta
[06:07] Cuando estés acá
[06:08] Una nueva orden de venta
[06:10] Cuando tú la crees
[06:11] Ahí le das no sé cómo
[06:13] Guardar
[06:14] Ahí no sé por qué
[06:15] Ahí debería ser
[06:16] Por qué confirmar esto?
[06:17] Debería como guardar simplemente
[06:21] Lo había hecho así para que en caso de que alguien
[06:24] O dos personas estén haciendo la venta
[06:26] Primero confirmen el stock y después vendan
[06:29] No, pero es que eso
[06:30] Por ejemplo
[06:31] Cuando ahí en el botón guardar
[06:36] Obviamente le va a validar
[06:38] Va a hacer la validación ahí
[06:40] Antes de insertar el movimiento
[06:42] Debería preguntar si hay stock
[06:44] Si no hay stock
[06:45] Claro, ahí te debería tirar alerta
[06:47] Vale
[06:49] Entonces ahí lo que debería hacer es guardar
[06:52] Guardar documentos
[06:53] La orden de venta le da a guardar
[06:55] Y te debería devolver a andate al libro
[06:57] Ahí
[06:58] Ahí debería devolver
[06:59] ¿Caché?
[07:01] Y de que aparezca el registro ahí
[07:03] Que creaste
[07:04] El nuevo
[07:05] ¿Me explico?
[07:06] Vale y lo estaba dejando acá
[07:08] No, no
[07:09] No porque en cierto modo es como que
[07:12] Porque puede ser que ellos tengan separado
[07:14] El flujo o el proceso de
[07:16] Ordenes de venta
[07:17] ¿Caché?
[07:18] Emite órdenes de venta
[07:19] Y no necesariamente tenéis que irte al libro
[07:21] A emitir de ve
[07:22] Porque tenéis que esperar el flujo de aprobaciones
[07:24] ¿Caché?
[07:26] Entonces a lo mejor es esta persona
[07:28] O el usuario se va a poner
[07:30] Es que
[07:31] Por lo que habían dicho
[07:32] En lo que estábamos en la reunión con Mario Lu
[07:34] Ah, eso lo compra
[07:35] Eso lo compra las aprobaciones
[07:38] Ya
[07:39] Ya pero
[07:41] Yo lo tiraría
[07:42] No sé, no sé si
[07:43] Es que en realidad
[07:44] Emite ir directo
[07:45] ¿Caché?
[07:47] Puta, validémoslo con ellos mejor en la reunión
[07:49] Dale
[07:50] Validémoslo con ellos
[07:51] ¿Cuál es lo más cómodo?
[07:52] Si a lo mejor
[07:53] Yo estoy equivocado
[07:54] Que tiene que hacerse
[07:55] Directo desde la orden de venta
[07:57] Y emitir la factura y todo eso
[07:59] O
[08:00] Que vaya por parte
[08:02] Vale
[08:05] Y emitir la factura
[08:12] ¿Cómo?
[08:13] ¿Crees que lo he dejado?
[08:19] No me la guardo
[08:20] ¿Qué está pasando?
[08:22] ¿Por qué no está con la fecha de hoy?
[08:25] Por Carlos de Tamadora
[08:27] No
[08:28] Un par de horas
[08:29] Ya, cantidad de madera ya
[08:39] Siguiente
[08:40] Ya, sin referencia, confirma el stock
[08:51] Va a duplicar la página para no perder esto
[08:53] Ajá
[08:55] Ahorita va a poner
[08:56] ¿Por qué le hizo con fecha de ayer la hueá?
[09:02] Ya, pero no es un pay call
[09:04] ¿Y la hay confirmar?
[09:08] Bueno
[09:09] Ahí quedaría registrada en la página de emitir
[09:12] ¿Sí?
[09:13] Entonces
[09:14] Si yo le voy a facturar de ahí
[09:16] O de acá
[09:17] Debería hacer lo mismo
[09:18] Y tirar a GoSocket
[09:19] Lo que decí, vamos a abrir GoSocket antes
[09:23] Para ver los registros
[09:24] Esto que tengo las claves acá
[09:42] Estamos en Alma Wexport
[10:24] Alma Wexport si estamos bien
[10:43] Cambiar el estado que hice
[10:45] Por enviar la entidad tributaria
[10:47] Del 3 de el 9
[10:51] Esto es la prueba que estaba haciendo en la mañana
[10:53] Sí, por eso está en ese estado
[10:55] Esto es donde llegan las emisiones
[10:57] ¿Cachai?
[10:58] Es una prueba que estaba haciendo en la mañana
[11:00] No está revisado por el sí
[11:03] Pero por ejemplo así quedaría cuando ya está valida
[11:05] Que esta es la prueba que hice ayer
[11:06] Así aparece como harto rato
[11:08] Y después te aparece si es rechazo
[11:10] O si está aprobado
[11:12] Se ve margaleta así la cuestión
[11:15] Entonces ahora
[11:16] Mientras se vaya a GoSocket
[11:18] Sí, sí
[11:20] Entonces vamos a darle aquí a facturar
[11:24] Y aquí aparece la parte de emisión de documento
[11:27] No
[11:28] Está como el hoyo, hay que corregirlo rápido
[11:30] Siguiente, aquí me hace como revisar
[11:33] Sí, esto es parte del proceso de aprobación
[11:35] Y aquí recién va la emisión de documento
[11:37] No, está mal eso
[11:40] Si, si
[11:41] Y eso, eso, eso
[11:44] Por ejemplo, documento tributario
[11:46] Y ahí se emitió
[11:48] Ya, ya está, ahora abre el PDF
[11:50] ¿Podría abrir el PDF?
[11:51] ¿Este de acá?
[11:52] Sí
[11:54] O sea, aquí lo descargo
[11:55] Y eso también tengo una duda
[11:56] Porque aquí se descarga con la representación gráfica de GoSocket
[12:00] ¿Cachai? Mira, de hecho
[12:02] Sí, está bien
[12:03] Está bien
[12:06] Y aquí también tengo para descargar el LKML
[12:08] Pero eso es como más para mí
[12:10] No, está bien también el LKML
[12:12] Eso está perfecto
[12:14] Y ahí llega, si te das cuenta
[12:16] Comercial package
[12:17] Le habíamos tirado una cuestión que costaba 500 pesos
[12:19] Sí, 500 pesos, ahí está
[12:26] Y GoSocket
[12:28] Vale, lo cerré
[12:29] Espérate, voy a dejar esta cuestión
[12:38] No me ocupé tanto espacio
[12:40] Porque la vista de la cosa que graba
[12:42] Me molesta
[12:45] Entonces ya ahora lo voy a buscar
[12:49] Ah, y por ejemplo tengo este botón
[12:51] Como te digo, se demora caleta
[12:53] Que aquí podéis ver, podéis actualizar
[12:55] Por ejemplo aquí
[12:57] Está igual el webhook
[12:59] Pero es lento
[13:01] Es lenta la respuesta
[13:02] Entonces aquí lo podéis forzar
[13:03] Para ver si es que se actualizó o no
[13:05] También acá en GoSocket
[13:06] Ve y ahí llegó el segundo
[13:07] Ok
[13:12] Mira acá, si nos vamos a Anforium
[13:15] Perdón que estoy tomando el sello
[13:18] Se va a abrir la pestaña de ahí
[13:20] Con los detalles
[13:21] No, pero eso GoSocket a mí me da igual
[13:25] No quiero darle poco a ellos
[13:27] En la presentación
[13:28] Pero me interesa que en el RP
[13:30] Este funcionando el flujo de emisión
[13:32] De perfect
[13:33] Y acá por ejemplo el tema de
[13:35] Descargar el pdf
[13:37] En sí tiene que ser como
[13:39] Tenés que, así lo tengo que hacer
[13:41] Carlos
[13:42] Que cuando el buen pinche
[13:44] Ver pdf, no descargarlo, ojo
[13:46] No descargarlo
[13:47] Ver el pdf, ver el documento
[13:49] Obviamente haga la pega de ir a descargarlo
[13:52] Que es cierto
[13:53] Y te lo cargue en la base de datos
[13:55] Esa descarga
[13:57] Como tener una previsualización
[13:58] Y la opción de descargar
[13:59] Como lo teníamos en el otro, ¿Cierto?
[14:01] No, o sea, yo ahí lo que haría
[14:07] Levanto el pdf nomás
[14:08] Y ahí quieren si lo descargan
[14:10] O no sé
[14:11] Eso te estoy diciendo
[14:13] Cuando le di acá
[14:15] En vez de descargar
[14:16] Que se te previsualice el pdf
[14:18] Y la opción de descargarlo
[14:20] Eso ya, sí
[14:22] Ahí se entiende bien
[14:23] Eso es lo que me
[14:24] Eso, pero para el usuario
[14:26] Que el usuario sea transparente
[14:27] Y que bueno
[14:28] No sé, voy a descargarlo
[14:29] A costo
[14:30] Que no
[14:31] ¿Cacháis?
[14:32] Que como que
[14:33] Esto es todo, todo, todo del RP
[14:35] Ah, sí, sí, sí
[14:36] Eso más que nada
[14:37] Como para mostrarte que
[14:38] Está llegando la info
[14:39] No, no, no
[14:40] Sí, sí
[14:41] Es igual
[14:42] Tenemos que hacerlo dentro
[14:43] De la demostración del día
[14:44] Pero lo que voy yo que
[14:47] En sí
[14:48] Los botones
[14:49] Es un llamado a la opción
[14:50] De visualizar nomás
[14:51] ¿Cacháis?
[14:52] Visualizar pdf
[14:53] No va a ser el descargar
[14:54] Esto ya no sale entonces
[14:55] Claro
[14:56] Ese tienes que cambiarlo
[14:57] Por el del pdf de
[15:00] De GoSocke
[15:01] ¿Me explico?
[15:02] Sí, sí
[15:07] Y bueno, tengo que corregir
[15:08] El wizard
[15:09] Porque
[15:10] Todavía tiene rastros
[15:11] Del sistema de aprobación
[15:13] Voy a
[15:14] Voy a corregirlo para que quede
[15:15] Como
[15:16] Más simplificado
[15:17] Porque tiene como
[15:18] 6 veces que pasar esa página
[15:19] Siguiente
[15:24] Ya
[15:26] Eso
[15:27] Mira, yo tengo un lefoco a esto
[15:29] Trata de dejarlo
[15:30] Puta, juntémonos antes
[15:31] Pero tiene que estar
[15:32] Un buen
[15:33] Está funcionando filete
[15:34] Para la red
[15:35] Para que
[15:36] Desfoqueamos la reunión
[15:37] Sobre
[15:38] Esto no va
[15:39] ¿Cacháis?
[15:40] La orden de venta
[15:41] Que funcione bien
[15:42] Yo como te digo
[15:43] Puta, si voy a dejar
[15:45] En la orden de venta
[15:46] Guardar
[15:47] Eso de que emitir
[15:48] Facturar detallar
[15:49] No, no lo pondría
[15:50] Claro, sería
[15:51] Sería pasar como
[15:52] Una vez por acá
[15:53] Darle guardar
[15:54] Y de acá darle facturar
[15:55] Exacto
[15:56] Sí, sí, te entendi
[15:57] Porque está demasiado
[15:58] Con muchos pasos
[15:59] En la red
[16:00] Sí
[16:01] Porque podía hacer
[16:02] Las dos cosas
[16:03] En dos lados
[16:04] No, pues la idea
[16:05] Es que sea un orden
[16:06] Sí, sí, sí
[16:07] Y bueno
[16:08] Si ellos después
[16:09] Nos dicen
[16:10] No, es que yo quiero
[16:11] Al momento de guardar
[16:12] La orden de venta
[16:13] Tiro facturar
[16:14] Ya, bueno
[16:15] Ya lo vemos
[16:16] Pero
[16:17] La idea es que sea un
[16:18] Con un orden
[16:19] Vale, vale
[16:21] Igual
[16:22] Por las
[16:23] Correcciones
[16:24] De la semana pasada
[16:25] Yo voy a decir
[16:26] Que se dio foco
[16:27] A como
[16:28] Estábamos ya
[16:29] Con un Go Soccer
[16:30] A eso
[16:31] Y que la próxima semana
[16:32] Vamos a presentar
[16:33] Los avances de lo que
[16:34] Habían solicitado
[16:36] El módulo de sorería
[16:37] Que cualquier
[16:38] Claro
[16:39] Claro
[16:40] Por eso
[16:41] Pero aquí
[16:42] Lo digo
[16:43] Mata esto
[16:44] Porque aquí
[16:45] Te falta también
[16:46] Armonar
[16:47] Vale
[16:48] Enviéndote el
[16:49] Crédito
[16:50] ¿Caché?
[16:51] Vale
[16:52] Y tenéis que
[16:53] Por ejemplo
[16:54] La visualizar
[16:55] PDF
[16:56] Descargar
[16:57] Lqml
[16:58] Ya lo tienes o no?
[17:00] Sí, sí
[17:01] ¿Por qué lo tienes?
[17:02] Te aparece acá
[17:03] El estado
[17:04] Pero el estado
[17:05] Del Go Soccer
[17:06] ¿Cómo lo actualiza el estado?
[17:07] Acá
[17:10] Y pero
[17:11] ¿Está consumiendo
[17:12] El servicio de ahí?
[17:13] Sí
[17:14] Si de hecho
[17:15] Acá todo esto
[17:16] Pero si te das cuenta
[17:17] Este que el folio 56
[17:18] Dice que
[17:19] Folio 6 y 56
[17:20] Este ya está listo
[17:21] Si te vas a ver acá
[17:23] Oye pero
[17:24] No te asignan
[17:25] ¿Tiro el folio de ello?
[17:26] No, pues que
[17:27] Este
[17:28] Este sistema de
[17:29] Sandbox que tienen
[17:30] Como de pruebas
[17:31] Se demora caleta
[17:32] Y el folio si lo asignan
[17:33] Para números
[17:35] Y ese folio
[17:36] ¿Por qué no lo rescatas tú?
[17:37] Lo voy a rescatar
[17:38] Lo que pasa es que
[17:39] Lo tenía así
[17:40] Para que esa
[17:41] Esa parte te reflejara
[17:42] Solamente como el estado pendiente
[17:43] No más
[17:44] Pero lo voy a dejar acá
[17:45] Como
[17:46] Como ítem
[17:47] No porque
[17:48] En cierto modo
[17:49] Ese folio
[17:50] Ojo ahí
[17:51] Carlos
[17:52] El folio que te están devolviendo
[17:53] Por ejemplo
[17:54] El folio si 56
[17:55] Es el folio que tienes que poner
[17:56] La misma en la primera columna
[17:57] De esa tabla
[17:58] Vale
[18:00] ¿Me cacháis?
[18:01] Y esto que se está dejando aquí
[18:04] Mierda
[18:05] Entonces
[18:06] Eso tenéis que
[18:07] Eso tenéis que cambiar
[18:09] Yo lo que yo te decía
[18:10] ¿Es un link a eso?
[18:11] Si es un link
[18:12] Ya pues
[18:13] Eso está muy bien
[18:14] Está muy bien
[18:15] Que lo mismo
[18:16] Pero poner el folio
[18:17] Del
[18:18] Del
[18:19] De estos muchachos
[18:20] Incluso ahí
[18:21] Si podéis cambiar
[18:22] Por ejemplo
[18:23] El ojito
[18:24] El botón del ojito
[18:25] Dejarlo allá
[18:26] Cacháis
[18:27] Como parte del link
[18:28] No sé cómo podréis
[18:29] A lo mejor podréis
[18:30] Crearte un botón
[18:31] Que se convierta
[18:32] Con un botoncito
[18:33] Adentro que aparezca
[18:34] El folio
[18:35] Mirá
[18:36] Entonces
[18:38] Demítenme el demo
[18:39] Que te pasé yo
[18:43] Andate
[18:44] He contado mis libros
[18:45] El libro de ventas
[18:46] Viste ahí
[18:49] Aparece el folio
[18:57] Folio es un botón
[18:58] Abajito
[18:59] El folio es un botón
[19:00] Y si tú pinchaste
[19:01] Habrá el pdf
[19:02] Vale
[19:03] Eso mismo
[19:04] Y en el otro lado
[19:05] En el otro lado
[19:06] En el almahue
[19:07] En el almahue
[19:08] Sácase
[19:09] Ese botón
[19:12] De ojito ahí
[19:13] Cacháis
[19:14] Vale
[19:15] Y si te das cuenta
[19:17] También
[19:18] Detémite
[19:19] Mira
[19:21] Al primer botoncito
[19:22] El check verde
[19:23] Que está ahí
[19:24] Ese
[19:26] Si tú lo pinchas
[19:27] Te muestra el tracking
[19:28] Del documento
[19:29] Cacháis
[19:30] Ahí eso igual
[19:31] Tenís que agregarlo
[19:32] Tenís que agregar un tracking
[19:33] De que cuando fue emitido
[19:34] La fecha y hora
[19:35] Que fue emitido
[19:36] Que el flujo de acá
[19:37] Por qué usuario
[19:38] Mmm
[19:39] Por qué usuario
[19:40] Fue emitido
[19:41] Todo eso
[19:42] En ese ojito
[19:43] Lo reemplazaría
[19:44] Para que te levanta
[19:45] El tracking
[19:46] Cacháis
[19:50] Vale
[19:51] ¿Qué otros datos
[19:52] Podrían ir dentro del tracking?
[19:55] Mmm
[19:56] Por ejemplo
[19:57] También hay que
[19:58] Eso lo tenemos que considerar
[19:59] Cuando fue enviado
[20:00] Hay que mandar correo
[20:01] Al
[20:02] A la casilla del cliente
[20:03] Cacháis
[20:04] Enviar
[20:06] No, no caché
[20:07] Mira
[20:08] Tú cuando emites una factura
[20:09] Tú tú eres el administrador de clientes
[20:11] Tienes
[20:12] Ándate al administrador de clientes
[20:13] Los maestros
[20:14] Ya tú tienes esos dos
[20:16] Edítalos
[20:17] Edita uno
[20:18] Ya
[20:22] Por ejemplo
[20:23] Aquí tenís
[20:24] Te falta el campo correo
[20:26] Vale
[20:28] Te falta el campo correo
[20:29] El correo
[20:30] Y cuando tú agregues un correo
[20:31] A ese cliente
[20:32] Incluso yo le dejaría
[20:35] Por ejemplo
[20:36] Dejaría así
[20:37] Los datos del cliente
[20:39] Dentro de los
[20:40] Como los datos generales
[20:41] Que serían estos
[20:42] Después podría un dato
[20:43] De contacto
[20:44] Ya
[20:45] Contacto
[20:46] Que ese puede ser
[20:47] No sé
[20:48] Por una persona
[20:49] Y un correo
[20:50] Nombre de persona
[20:51] Y correo
[20:52] Ya
[20:53] Carlos
[20:54] Sí te escucho
[20:55] Te escucho
[20:57] Ya entonces
[20:58] Un nombre de
[21:00] Una pestañita
[21:01] Esto sea como general
[21:02] Otra pestañita
[21:03] Que sea de contacto
[21:04] Cacháis
[21:05] Vale
[21:06] Que sea de contacto
[21:07] Cacháis
[21:08] O
[21:09] Voy a hacerla más simple
[21:10] Después lo vemos en tips
[21:11] Y mejor
[21:12] Deja
[21:13] Así como
[21:14] Aquí agregarle
[21:15] El campo correo
[21:16] Ya
[21:17] Si el cliente
[21:18] Tiene un correo
[21:19] Registrado en su mantenedor
[21:20] Cuando imitas
[21:21] Una orden de venta
[21:22] Tienes que informar
[21:23] Esa orden de venta
[21:24] Al correo
[21:25] Al cliente
[21:26] Cacháis
[21:27] Que le pregunte
[21:28] Y después
[21:29] Cuando tú factures
[21:30] Cuando la factura
[21:31] Ha sido así
[21:32] Tienes que mandar
[21:33] El correo
[21:34] Al cliente
[21:35] Vale
[21:37] Y ahí por ejemplo
[21:40] Me imagino que
[21:41] En el tracking
[21:42] Debería salir de que
[21:43] Se envió el correo
[21:44] A la casilla tanto
[21:45] Claro
[21:46] Vale, vale, vale
[21:48] Y eso por ejemplo
[21:49] Entonces para enviarlo
[21:50] Cuando yo esté acá
[21:51] Eh
[21:52] Perdón
[21:53] Acá
[21:55] Sería como
[21:56] Un botón de enviar
[21:57] Es que cuando tú lo imites
[22:00] Tienes que mandarse de una
[22:02] Automáticamente
[22:03] Automáticamente
[22:04] Y acá también podrías
[22:05] Como reenviar
[22:06] Cacháis
[22:07] Vale
[22:08] Vale, vale, vale
[22:09] Bueno
[22:10] Igual eso va a quedar como
[22:11] Eh
[22:12] Porque todavía no tenemos
[22:13] Servicios de envío de correo
[22:14] Lo dejaría como opción
[22:15] No más
[22:17] Pero no funcionaría
[22:18] Claro
[22:19] Pero ahí tenéis que
[22:20] Dentro de la administración
[22:21] Tenéis que dejar
[22:22] Para que ellos puedan
[22:23] Configurar su
[22:24] SBTP
[22:25] Y todo
[22:26] Un servidor de correo
[22:27] Vale
[22:28] Cacháis
[22:30] Sí, sí, sí
[22:31] Entonces
[22:32] Eso
[22:35] Ya
[22:36] Simplificar
[22:37] La orden de venta
[22:38] De que
[22:39] El botón de facturar
[22:40] Solamente
[22:41] Sea en emitir
[22:42] Y en el otro
[22:43] Y
[22:44] Sí
[22:45] Sí
[22:46] Y no
[22:47] Y no alertito
[22:48] Por cada paso que hace
[22:49] De esos
[22:50] Verdecitos
[22:51] Sino que alertad
[22:52] Ya cuando está emitido
[22:53] No más
[22:54] El documento va
[22:55] Vale
[22:56] La alerta
[22:57] De arriba
[22:58] Sí
[22:59] Sí, sí, sí
[23:00] Vale
[23:01] Ya
[23:03] Eh
[23:04] ¿Qué otra cosita
[23:05] No se me escapa nada
[23:06] Cierto
[23:07] Bueno el folio
[23:08] Recuerda el folio
[23:09] El ojito
[23:10] Que ya
[23:11] El ojito tiene que verla
[23:12] Igual que implementar
[23:13] El
[23:14] Si está
[23:15] Pero el folio pendiente
[23:16] No debería ya tener
[23:17] Folio pendiente
[23:18] Porque gozo que te entrega
[23:19] Folio de una
[23:20] Claro
[23:21] El estado del pendiente
[23:22] Realmente
[23:23] La revisión del CI
[23:24] Sí
[23:25] Exacto
[23:26] Entonces todo ese tracking
[23:27] Tiene que agregarlo
[23:28] Dentro del ojito
[23:29] Pero el folio tiene que aparecer
[23:30] Allá como un botón
[23:31] Y poder abrirlo desde ahí
[23:32] Vale, vale
[23:33] Oye Sergio
[23:34] Otra cosa que te quería
[23:35] Consultar
[23:36] Que igual siento que
[23:37] Uno
[23:38] Me falta caleta
[23:39] Por hacer
[23:40] Me falta mucho por hacer
[23:41] Y dos
[23:42] Si le mareamos
[23:43] Si te das cuenta
[23:44] Me meto a una reunión
[23:45] Entiendo algo
[23:46] Y deja no
[23:47] Te gustamos videos
[23:48] Estaba la cuestión
[23:49] Pero
[23:50] Como que no
[23:51] Lo estoy aplicando bien
[23:52] Entonces
[23:53] No sé si es que
[23:54] Este fin de semana
[23:55] Nos podríamos conectar
[23:56] A hacer una maratón
[23:57] Algo porque
[23:58] Y también para
[23:59] Calmarme la ansiedad
[24:00] Porque estoy durmiendo
[24:01] Menos que la chucha
[24:02] Oye
[24:03] Sí
[24:04] Tienen ningún problema
[24:05] El coordineo
[24:06] Hoy el fin de semana
[24:07] Yo voy a estar
[24:08] En la casa
[24:09] Entonces
[24:10] Puta
[24:11] No sé
[24:12] No sé
[24:13] El tema del fin de semana
[24:14] Tenté con la hija
[24:15] Me acomodo
[24:16] Si necesite que
[24:17] Me conecto
[24:18] Una la mañana
[24:19] Lo hago
[24:20] Pero necesito
[24:21] Uno
[24:22] Terminar esta guay
[24:23] Y dos
[24:24] Porque de verdad
[24:25] Psicológicamente
[24:26] No me tengo ni una fe
[24:27] Como que cada día
[24:28] Que pasa
[24:29] No me creo nada
[24:30] No lo hago presencial
[24:31] Ni lo digo ni nada
[24:32] Porque mientras más lo digo
[24:33] Más lo creo
[24:34] Pero necesito tener calma
[24:35] Mental de esta weá
[24:36] De que va a
[24:37] Funcionar
[24:38] No sé
[24:39] Hay que tener la integración
[24:40] pero no no piñisqui por muchos lados entonces ahora por ejemplo ya tenéis claro lo que hay que hacer
[24:48] para esta presentación enfócate en eso no en los futuros vamos alíneate para que la
[24:56] presentación del día se enfoque solamente es ordenes de venta la facturación integración
[25:00] con go socket visualización del pdf el tracking nada más que eso vale ya entonces y eso
[25:08] dejando una tarjeta en la reunión y lo dejáis para que entregan reunión tanto y para que la
[25:13] revisen ellos vale ya vale pero nos juntamos pero vamos a punto específico no veamos el
[25:24] mundo completo sino que me dice que es el que necesito de estado como va a esto tenemos
[25:30] que llegar perfecto matamos a mí si dura 10 minutos 20 minutos la matamos tú te vas
[25:34] a enfocar a eso full full full ya lo tengo listo nos juntamos revisamos y toque ya otro
[25:40] punto oye necesito de esto como ese punto pero no no no nos mareamos porque esto va a un mundo
[25:48] igual complejo entonces absorberlo todo de una va a ser imposible sí sí está acuático entonces
[25:57] por parte nos ataquemos punto específico vale ya vale y hablamos chau
