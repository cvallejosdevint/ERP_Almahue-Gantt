# Transcripción — Reunión GoSocket QA

**Fecha de transcripción entregada:** 19/08/2026  
**Fecha de reunión:** agosto 2026, post-Reu6; fecha exacta no confirmada  
**Tipo:** Onboarding GoSocket QA / portal sandbox / credenciales API  
**Participantes:** Pablo Rodriguez (GoSocket Chile, consultor), Maria Jesus Rodriguez / María Jesús (Almahue), Carlos Vallejos (Devint), Mario Andres Ubillo Labrin (Almahue)  
**Mencionados:** Cristian (contrato/factura GoSocket), Sergio (Devint), Nico (representante legal / certificado)

> Fuente entregada por usuario el 19/08/2026. Se conserva contenido, hablantes y timestamps. Se corrigen solo espaciados mínimos para legibilidad; no se incorporan secretos.

---

Pablo Rodriguez [00:08]: María, lo dejo como obligatorio, ¿cierto? Sí, por favor. Ahí envié la actualización. Bien, vamos a ver. María, consulta, ¿aún no han podido avanzar con el tema del contrato?

Maria Jesus Rodriguez [00:52]: La verdad es que Cristian no nos ha respondido nada sobre el contrato. Yo ya le mandé la consulta y le pregunté por la factura, que teníamos una diferencia, que me la aclaró, y le pregunté por el contrato, no me ha respondido nada.

Pablo Rodriguez [01:07]: Ya le había dejado el aviso, pero igual voy a tener que presionarlo más.

Maria Jesus Rodriguez [01:11]: O sea, en el caso de que ustedes quieran salir en agosto con IOFaktura, que sería lo ideal, pero sí, o sea, nosotros no tenemos ningún problema en que nos manden el contrato y firmarlo si ya está todo aprobado por parte de Diferencias.

Pablo Rodriguez [01:23]: Ya, vamos a ver.

Maria Jesus Rodriguez [01:30]: Lo que sí vamos a tener un poco de desfase en la carga de documentos porque no están haciendo bastante difícil por el lado de aceptar la entrega de información.

Pablo Rodriguez [01:39]: Sí, lo que comentábamos esta semana también, sí suele pasar, es normal que pase eso, la verdad. Pero mira, no te preocupes. De gran manera por eso, porque igual podemos avanzar con lo demás mientras y la carga la podemos hacer finalizando ya el proceso de implementación.

Mario Andres Ubillo Labrin [01:59]: Bien, bien.

Pablo Rodriguez [02:04]: ¿Y cuántos documentos son?

Maria Jesus Rodriguez [02:05]: Una vez tú me comentaste, yo creo que por el lado de AlmaWeb no son tantos porque alcanzamos a estar un año con ellos, debiesen ser alrededor de unos 1000, 1200.

Pablo Rodriguez [02:17]: No son muchos para descargarlos del servicio.

Maria Jesus Rodriguez [02:20]: Sí, no hay por el lado de ADAS. Lo que pasa es que por el lado del servicio, por tener Acepta, no nos queda el respaldo en el servicio.

Pablo Rodriguez [02:32]: No, no hay, claro, tienes que solicitarlo.

Maria Jesus Rodriguez [02:35]: Sí, de hecho nosotros perdimos el historial de AlmaWeb por lo mismo, porque hicimos el cambio a Acepta y no nos confirmaron que había quedado bien cargado a la base. Y una vez que hicimos el cambio y aceptamos todo, nos dijeron como que teníamos problemas y perdimos el historial completo. Menos mal teníamos todo impreso.

Pablo Rodriguez [02:58]: Sí, o sea, igual se puede descargar del servicio esa información, pero es más complejo por siendo tantos documentos, es una tarea bastante compleja.

Maria Jesus Rodriguez [03:09]: Porque más encima del servicio, igual me interesaría saber la forma porque por el lado del mago igual dimos perdido el historial y yo prefiero recuperarlo.

Pablo Rodriguez [03:20]: Sí, lo que pasa es que el servicio te deja descargar de 20 documentos máximo. Entonces se puede descargar el archivo de respaldo, pero es una tarea estar 20 por 20, es una tarea enorme. Mira, si gustas podemos verlo en otra reunión, bien, podemos verlo en otra reunión para ver si es que hay alguna posibilidad de hacer algo. Yo te apoyo, bien, yo te apoyo con él. En la misma llamada. Bien, bueno, ahí le mandé la consulta a Cristian para que nos dé información del contrato. Bien, yo actualmente estoy trabajando aún en las representaciones gráficas, bien, pero es algo que finalmente se puede hacer bastante rápido. Entonces, una vez que me informen que el contrato ya está firmado, les aviso para que podamos habilitar IO Facturo. Bien. Y bueno, respecto al tema de la implementación por API, ¿tienen alguna, algún avance, alguna duda respecto a la integración?

Maria Jesus Rodriguez [04:24]: Ahí te dejo con los expertos, Carlos y Sergio.

Carlos Vallejos [04:26]: No hay problema, no hay problema. Estábamos revisando y en sí con la documentación que nos entregaron hemos podido adelantar harto trabajo. Ya tenemos aproximadamente la estructura de cómo vamos a enviar la información mediante la API, cómo la estamos armando. Lo que sí tenía la duda es si es que por esto del contrato todavía no tenemos las credenciales para generar en el ambiente de Cuba, ¿verdad?

Pablo Rodriguez [04:49]: Sí, eso mismo le iba a comentar. No, para Cuba no es necesario el contrato. Yo ahora voy a crear el ambiente para que ustedes puedan, en este caso, ya emitir los documentos. Así que saliendo de la reunión les mando las credenciales y para que ustedes se puedan conectar. Bien, ahora necesito que uno de los testers, lo ideal es que sepa manejar también el portal, porque ahí es donde va a estar concentrada, concentrado la mayor parte de los documentos y las validaciones que van a tener que hacer van a estar en este sector. Entonces, si se pueden, pueden ingresar a la empresa más que nada.

Carlos Vallejos [05:33]: Perfecto, perfecto. Tendríamos que definir, porque me imagino que es más que nada como para mientras nosotros realizamos las gestiones desde el API poder comprobar desde el sitio que todo quedó correcto, ¿verdad?

Pablo Rodriguez [05:43]: Claro, desde el mismo sitio. Voy a asignarme las empresas, ahí vemos con cuál vamos a trabajar. Lo ideal es que sea con ambas, bien, para validar la integración de los datos. Pero es súper importante que ustedes se integren también a la plataforma porque así pueden ver in situ cuáles son los errores que están generando los documentos en el caso de que tengan alguno. Perfecto. Denme un segundito, estoy asignando la empresa y les comparto pantalla para que vayamos revisando.

Carlos Vallejos [06:15]: No hay problema. Voy a aprovechar de dejar grabando desde ahora para que tengamos el respaldo del compartir pantalla.

Pablo Rodriguez [07:27]: Coméntenme si se ve la pantalla.

Maria Jesus Rodriguez [07:32]: Sí se ve la pantalla, se ve en blanco.

Pablo Rodriguez [07:35]: Ya, sí, estaba cargando. Ya vamos a ingresar a cualquiera de los routes. Por ejemplo, al Mago Exportación S.A. Y este es el portal. Bien, lo primero, tienen que registrarse, tienen que registrarse en el ambiente. Este mismo, este mismo link les va a servir, se lo voy a dejar en el mismo chat. Solamente es ingresar. Una vez que ya hayan ingresado, me confirman para yo poder, en este caso, agregarlos a la empresa. Bien, y una vez que estén acá, este es el portal de GoSocket. Es muy simple utilizarlo. Acá en el inbox tenemos la gestión de los folios, ¿cierto? Recuerden que en QA, por el tema de los folios, María, como dan muy poquitos, lo ideal es que los carguemos manual. Ya en productivo serán automáticos, pero de alguna manera igual tenemos que, como tenemos que trabajar acá Tenemos que sí o sí tener folios. Entonces, en la opción de emitidos, hay que tener paciencia igual con el ambiente de ECUA, tiene menos recursos que el de Productivo, bastante menos. Tenemos este filtro de documentos, bien. Entonces ustedes, una vez que emiten el documento, lo ideal es que lo emitan con la fecha del día, bien, para que no se les pierda en el mismo filtro. Y tienen la opción acá de fecha de emisión del documento. Acá solamente seleccionan últimos 3 meses y la opción de buscar, y con eso ya les va a mostrar en este caso todos los documentos que han emitido. Bien, acá no tenemos ningún ejemplo para que lo podamos ver, pero voy a ir a otra empresa, buscar otra empresa para que vean cómo, cómo se ven los documentos bien y dónde consultar el tipo de errores que tiene. Bien. Inbox. Vamos a emitido nuevamente. Y acá, por ejemplo, tenemos documentos que son creados desde el día. Bien, si se fijan, primero tenemos un pequeño icono que ya nos está indicando, nos está diciendo del estado del documento. Bien, y tenemos otro más abajo que dice rechazado. Bien, yo acá les recomiendo que presionen el Control y al ingresar al documento tienen que presionar el folio o cualquier sección de esta parte del documento. Por ejemplo, esta factura electrónica que está rechazada la vamos a revisar. Bien. Ya acá tenemos el detalle del documento. Bien, no es el XML como tal, pero es mayormente el detalle donde podemos ver los datos que estamos entregando, tanto en el detalle, la referencia del documento, la información del emisor y el receptor. Bien, y en la parte de abajo, que es lo que más nos importa, tenemos las notas. Y acá es donde se ven los errores. Bien. Por ejemplo, este documento tiene un error que es rechazado por error de carátula. Cuando hay un error que ustedes no lo conocen realmente o no o no tienen cómo identificarlo, lo ideal es que me lo consulten, bien. Pero por ejemplo, un error de carátula generalmente se ocasiona cuando no se informa correctamente la resolución, el número de resolución y la fecha de resolución en los documentos que están emitiendo, bien. Entonces, cuando vean este tipo de errores, me lo pueden mandar por correo electrónico y yo les voy a responder a qué se debe y qué es lo que deben corregir, bien. Acá en este apartado tenemos varias cosas importantes que no les van a servir para poder avanzar con el proyecto. Por ejemplo, la descarga del XML. El proceso de la API es que ustedes envían el request, este request se transforma por medio de un XSLT, de un mapeo. Bien, entonces acá nosotros tenemos dos opciones: tenemos descargar el XML en el cual se construyó nuestro documento, y en el archivo de integración tenemos el documento que ustedes enviaron sin procesar, o sea en crudo. Bien, entonces así nosotros determinamos si es que este error se generó después del mapeo o es la información que ustedes nos enviaron al portal. Bien, también tenemos acá la opción del PDF, cierto. Esto es súper importante porque pueden descargar el PDF con la representación actual que está cargada, y si piden un cambio, por ejemplo, yo cargo la representación gráfica no es necesario volver a emitir un documento, sino que pueden irse a un documento antiguo y aquí en el combo box está la opción de regenerar PDF. Lo que hace esta opción es tomar la representación gráfica antigua, eliminarla y tomar la nueva que yo he cargado. Bien, entonces no es necesario siempre que hay un ajuste en las representaciones gráficas, no es necesario reemitir, sino que simplemente regenerarlo. Bien, bueno, y eso en mayor detalle, eso es el portal. Es una herramienta bastante simple de utilizar y con esto es importante que ustedes puedan trabajar con esto porque da mayor certeza del error que le está generando. Incluso muchas veces aquí los errores de esquema, que son los más comunes, aquí informa cuál es el nodo que tiene problemas y qué es lo que está ocurriendo con ese nodo. Bien, ¿alguna duda o consulta por el momento? Por mi parte no, por mi parte tampoco. Ya, yo los puedo agregar al ambiente, yo los puedo agregar al ambiente directamente, pero es más complejo. Lo que podríamos hacer es que ustedes se enrolen, bien, tienen que hacerlo en el link, y una vez que se enrolen me avisan y yo lo agrego a todos al portal, al portal de pruebas.

Carlos Vallejos [13:34]: Lo hacemos de inmediato.

Pablo Rodriguez [13:36]: Si gustan, pueden hacerlo de inmediato, no demora mucho hacerlo.

Carlos Vallejos [13:41]: ¿Hay algún límite, por ejemplo, con el dominio con el cual nos registremos, o no es necesario que sean del mismo dominio?

Pablo Rodriguez [13:48]: No es necesario que sean del mismo dominio, más que nada por correo.

Carlos Vallejos [13:52]: Voy a registrarme de inmediato.

Pablo Rodriguez [13:57]: Si tienen algún incidente, me comentan.

Carlos Vallejos [14:18]: Al menos al ingresar al link me aparece el login más no registro como tal.

Pablo Rodriguez [14:26]: No aparece registrarse, la opción registrarse no aparece, solamente correo y contraseña. Ya, vamos a validar. Ese es un cambio que creo que estaban haciendo porque quieren juntar. Ya, ok, ya. Entonces vamos a ingresar al siguiente link. Eso significa que unificaron las bases de datos, así que vamos a ingresar al link que yo les acabo de dejar, www.osec.net www.gozake.net.

Maria Jesus Rodriguez [15:19]: Me sale lo mismo, no me deja registrarme.

Carlos Vallejos [15:23]: A ver si aparece la misma página.

Pablo Rodriguez [15:35]: Ya, quizás por algún motivo deshabilitaron momentáneamente el registro. Ya, los correos electrónicos son los que, con los cuales ustedes están actualmente, ¿cierto?

Carlos Vallejos [15:44]: Sí.

Pablo Rodriguez [15:45]: Vamos a intentar hacer algo, los voy a agregar directamente y les debería llegar un correo de que yo los agregué, por ende realicen el proceso de de registro. Voy primero con María.

Carlos Vallejos [15:58]: Ahí dejé en el chat mi email que se agregó con usuario temporal aquí en la reunión.

Pablo Rodriguez [16:10]: Ya hagamos la prueba. Primero lo voy a hacer con AlmaWeb y voy a agregar a María y Carlos.

Maria Jesus Rodriguez [16:16]: Y Mario, por favor.

Mario Andres Ubillo Labrin [16:18]: Ya.

Pablo Rodriguez [16:20]: Sí, amigo, te mando igual el correo por chat. Sí, sí, perfecto. ¿Puedes validar, María, si es que te llegó un correo? Dependiendo la casilla, igual puede demorar.

Maria Jesus Rodriguez [17:17]: Voy a actualizar la casilla, aún no me ha llegado nada.

Pablo Rodriguez [17:22]: Le agregué a Carlos, mi amigo. Ya, coméntanos qué es lo que dice, por favor.

Maria Jesus Rodriguez [17:30]: Dice, estimada María Jesús, ahora usted puede acceder desde GoSocket a los documentos tributarios electrónicos de AlmaWeb por SPA. Siga estos pasos para registrarse y activar su cuenta. Ya, perfecto.

Pablo Rodriguez [17:41]: Ahí debería haber un link.

Maria Jesus Rodriguez [17:45]: Sí, me arrojó un link y me mandó un correo de contraseña.

Pablo Rodriguez [17:49]: Sí, esos son los datos como para poder iniciar por el momento. Este proceso en productivo, María, lo más probable es que solamente usted tenga el acceso a agregar gente. Yo solamente le agrego a usted y ahí usted administra para todas las demás personas que quiere ingresar.

Mario Andres Ubillo Labrin [18:13]: Bien, bien.

Carlos Vallejos [18:17]: Aquí recién me llegó el mail.

Maria Jesus Rodriguez [18:21]: No me deja entrar.

Mario Andres Ubillo Labrin [18:24]: A ver, ahí sí.

Maria Jesus Rodriguez [18:42]: Si coloco entrar, me manda a la página principal como de volver a entrar de nuevo.

Pablo Rodriguez [18:50]: ¿Puede mostrarme pantalla?

Maria Jesus Rodriguez [18:56]: Voy a compartir la pantalla.

Pablo Rodriguez [19:06]: Ya, ya tiene que ingresar, pero el link al sandbox se ve ahí. Sí, ahí se ve.

Maria Jesus Rodriguez [19:21]: Mira, pongo ingresar. Con los datos que me mandaste y pongo entrar. Me manda de nuevo esta pantalla.

Pablo Rodriguez [19:37]: Coloca ahí la opción de login. Ese es el productivo, intenta ingresar ahí.

Maria Jesus Rodriguez [19:48]: Arriba me aparece error y me manda a la pantalla de WhatsApp que tengo.

Pablo Rodriguez [19:51]: Ya vamos a hacer lo siguiente, coloque la opción de login y vamos a solicitar una, olvidó su contraseña.

Mario Andres Ubillo Labrin [20:03]: Perfecto.

Pablo Rodriguez [20:11]: Ahí María me está comentando, Cristian, que les va a mandar hoy día el borrador para que lo puedan revisar.

Mario Andres Ubillo Labrin [20:25]: Buenísimo.

Pablo Rodriguez [20:29]: Ya, ahí va a llegar un correo para poder hacer el cambio de contraseña. Antes de colocar las contraseñas, lo ideal es que lo coloquemos en un Notepad.

Mario Andres Ubillo Labrin [21:00]: Todavía no me ha llegado el correo.

Pablo Rodriguez [21:07]: Carlos, ¿tú pudiste ingresar o aún no?

Carlos Vallejos [21:10]: Pude, me estaba pasando lo mismo y al parecer es por la URL. Me fijé que estaba entrando en la que viene en el correo, que no me funcionaba, pero la que está en el chat, que es sandbox 2, esa me funcionó.

Pablo Rodriguez [21:26]: ¿Esa te funcionó?

Carlos Vallejos [21:27]: Sí, esa me funcionó. La que viene en el mismo correo no me funcionó.

Pablo Rodriguez [21:35]: Ya, sí, puede ser un tema de bloqueo, pero ahora haciendo el cambio de contraseña María debería poder ingresar, se debería poder ingresar sin problema. Creo que ahí pudiste entrar, María. Ya, yo lo estoy agregando. Mira, si te fijas arriba Ahí coloca aceptar, cierra todo. Arriba tienes el nombre de la empresa, Almago Export S.p.A. Ya, ya ahí están las dos empresas. Me falta agregar a Carlos a la otra empresa. Cuando yo te agregue, Carlos, tienes que reiniciar sesión. Tío, también soy solamente con alma, güey. También logré entrar.

Mario Andres Ubillo Labrin [22:44]: Falta Mario.

Pablo Rodriguez [23:09]: Ya ahí están agregados los 3. Mario y Carlos, por favor, ahí reinicien la sesión. Cerrar sesión del mismo botón de donde aparece su nombre, dice cerrar sesión y volver a ingresar. Y aquí les voy a explicar lo más importante, que es el cómo obtener las APIs, bien, la API de QA. Avísenme cuando puedan ingresar.

Carlos Vallejos [23:57]: Ingresar. Y ahora sale las dos.

Pablo Rodriguez [24:02]: Ya vamos a hacerlo con el Mago Export. Bien, lo va a hacer María ya que está compartiendo. Ahí, María, selecciona tu nombre y dice configuraciones.

Mario Andres Ubillo Labrin [24:15]: Bien.

Pablo Rodriguez [24:16]: Vamos a ingresar en configuraciones. Ya, aquí es muy importante, María, en la opción de certificados. Ingresa a esa opción, por favor. Acá tienen que cargar el certificado digital del representante legal o de la persona que va a firmar los documentos. Ya, bien. Aquí se tiene que hacer un match. El certificado que esté agregado acá también tiene que estar como usuario en el servicio Impuesto Interno con el permiso de firma. Bien, sin eso el servicio nos va a indicar de que el usuario no tiene permisos para emitir. Bien, bien, eso por parte tuya.

Maria Jesus Rodriguez [24:55]: Y lo otro, en la opción de consultas, ¿te acuerdas que la reunión pasada vimos el tema de anular los folios emitidos en modo prueba? Ya, yo te comentaba que la idea era que el Mawi LM quedara con el representante legal, Nico. Pero a mí me dejó eliminar los folios con el certificado digital de Don Pablo, que es el otro representante legal. ¿Eso se puede modificar en el servicio?

Pablo Rodriguez [25:23]: Sí, pero creo que se demora muchísimo.

Maria Jesus Rodriguez [25:26]: Entonces aquí tendría que subir los 2 certificados.

Pablo Rodriguez [25:29]: No es necesario. O sea, lo que pasa es que el certificado digital del representante legal nosotros lo necesitamos solamente para modificar la información del de la empresa. Por ejemplo, la escasez de intercambio, que es información crítica para el negocio. Bien, pero esto principalmente, este certificado no es necesario, el del representante legal puede ser el tuyo, por ejemplo, pero que tenga permisos de firma en el servicio. Puede ser cualquier otro certificado, más que nada tiene que ser el certificado de un usuario firmante.

Mario Andres Ubillo Labrin [26:00]: Ya.

Maria Jesus Rodriguez [26:03]: Me acuerdo que cambiamos las casillas de usuario con el de Nico, así que creo que se puede firmar con los dos.

Pablo Rodriguez [26:12]: Sí, hay igual, de todas formas, el certificado digital del representante legal es, no precisamente tienen los permisos de firma, ojo con eso, puede que no los tenga también. O sea, tienen que ingresar en el apartado de usuarios y ver que él esté. Yo lo que recuerdo, que lo que vimos sí estaban, así que no deberían tener problemas para firmar. Así que antes de que Carlos emita documentos hacia el portal de pruebas, el certificado ya tiene que estar cargado, porque si no, nos van a salir como rechazado. Bien, bien, eso por parte tuya. Bien, por parte de los chicos, de Carlos, en la opción, ve a la opción que dice API keys, por favor.

Carlos Vallejos [26:53]: Perfecto, aquí ya estoy.

Pablo Rodriguez [26:58]: Ya, ahora en donde dice agregar API key, presiónalo, María, para que lo veamos. Solamente es colocar básica authentication y confirmar. Con eso ya van a tener API key. Para QA tienen límite de 10, 10 API keys, bien, utilizables para que puedan en este caso hacer uso. Para el productivo ya es necesario avisarnos porque ya en el productivo se entrega por lo generalmente una, bien, y se las entrego yo, bien. Así que ya con eso pueden en este caso hacer la emisión de los documentos, bien, bien. Ahora, María, necesitamos cargar los CAF. Para eso vamos a ir a la opción que dice Inbox a la izquierda. Y vamos a ir a la opción que dice gestión de folios. Ya acá en el servicio Impuesto Interno, en la opción de CUAA, cierto, está la opción de solicitar folios. Es muy sencillo, solicitar los folios y te van a entregar un archivo CAF. Tú lo arrastras a este lugar o elegir archivo, y con eso le das a cargar. Y eso es todo, con eso ya se cargan los folios para que puedan operar.

Maria Jesus Rodriguez [28:26]: Son los mismos pasos que hicimos para eliminar los folios solicitados, ¿cierto?

Pablo Rodriguez [28:31]: Sí, donde tú estabas en la opción de eliminar los folios, 2 más arriba dice solicitar folio, y los puedes cargar en este apartado. Si en algún momento, Carlos, el API te entrega como mensaje de error de que no existe el rango de folio o el rango de números, es porque le falta folio y lo tienes que ver con María para que te cargue nuevos folios.

Carlos Vallejos [28:54]: Perfecto.

Pablo Rodriguez [28:58]: Bien, así que bueno, eso más que nada el tema de la, de Yo Facturo, María. Eso sí, la carga de folios es en otra parte, así que eso con su momento lo veremos ya entre los dos. Bien, así que bueno, ¿tienen alguna duda, consulta hasta el momento?

Maria Jesus Rodriguez [29:18]: Por mi parte, hasta el momento no.

Pablo Rodriguez [29:20]: Está bastante simple, es bastante simple e intuitivo ocupar el portal. Bien, así que si necesitan probar cosas en el portal, ahí están a libertad de hacer lo que gusten con él. Bien, así que bueno, eso más que nada. Me comentó Cristian, como te decía, María, que ya les van a enviar el borrador, me va a copiar a mí, así que yo también voy a estar al tanto de eso. Y una vez que ya tengamos firmado eso, podemos ver el tema de IO Factura entre los dos.

Maria Jesus Rodriguez [29:48]: Ya, buenísimo.

Pablo Rodriguez [29:50]: Bien, así que eso, eso, chicos, por el momento. ¿Hay algún otro punto que tengan que revisar? ¿Algo más adicional?

Carlos Vallejos [29:58]: De momento no. Lo que sí, Pablo, ¿no habría problema en caso de cualquier cosita mandarte un correo para dudas, verdad?

Pablo Rodriguez [30:04]: No, no hay problema. De hecho, si me quieren hablar por Teams también lo pueden hacer. Bien, así lo vemos mucho más rápido el tema. Perfecto, perfecto. Bien, así que bueno, eso, chicos, por el momento estamos en contacto. Cualquier cosita ahí me pueden contactar. Y bueno, ojalá les vaya bien con las pruebas también.

Carlos Vallejos [30:25]: Perfecto, muchas gracias. Y entonces cualquier cosita estaríamos en contacto.

Pablo Rodriguez [30:28]: Sí, no hay problema, ahí voy a estar atento. Bien, gracias, Pablo. Un gusto, que estén muy bien.

Carlos Vallejos [30:35]: Chau, gracias.

Pablo Rodriguez [30:35]: Hasta luego, chau, chau, chau, chau.

Carlos Vallejos [30:37]: Que estén muy bien.
