# Transcripción Reunión 6 — Avances ERP (06/08/2026)

**Fuente:** transcripción reunión avances (Teams/Meet + grabación local)  
**Video:** grabaciones usuario Cursor (no versionado en git)  
**Minuta canónica:** [`../reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md)

**Speakers (aproximado):**

| Etiqueta | Persona |
|---|---|
| Carlos Vallejos | Carlos Vallejos (Devint) — presentación demo |
| sergio | Sergio (Devint) |
| Speaker 00 | Agustín (Almahue) |
| Speaker 01 | María Jesús (Almahue) |
| Speaker 00 [02:20] | Equipo Almahue (confirmación audio) |

> Timestamps tal como vinieron de la transcripción automática.

---

Speaker 00 [00:01]: Eso, ¿lo veo bien?

sergio [00:05]: Sí, se ve impecable. ¿Según eso murió?

Speaker 00 [00:44]: Sí, nada más uno. Murió cerca de la siglo 80.

sergio [00:49]: Ok. Carlos, si quieres puedes compartir mientras pantalla del login. Voy de inmediato.

Speaker 00 [02:20]: Ya, Sergio, estamos perfectos.

sergio [02:29]: Muy buenas tardes a todos, espero que estén todos muy bien. Ahora estamos en otro proyecto, vamos a mostrar el avance del proyecto RP Almagüe. En este caso va a presentar Carlos. Obviamente, ya como todos bien saben, hay un avance que ha estado trabajando Carlos en conjunto con María Jesús. Ya se han definido varias cositas y hemos ya tenido reuniones con el nuevo proveedor de facturación electrónica que usó, que ya tenemos la documentación para iniciar la integración. Que también se está trabajando en ello. Esperamos ya tener noticias la próxima semana. Bueno, y Carlos les va a presentar el avance de todo lo que es la interfaz. Ya está gran parte avanzado, también lo que es conexión a base de datos, pero ya vienen ya como afinar algunos temas de reportería, cálculo y ese tipo de cosas. Así que, Carlos, te doy el pase.

Carlos Vallejos [03:29]: Muchas gracias, Sergio. Buenas tardes a todos, espero que se encuentren bien. Me confirman si es que se ve bien la pantalla.

Speaker 01 [03:35]: Se ve bien, Pablo.

Carlos Vallejos [03:37]: Perfecto. Vamos entonces a partir, vamos a hacer el inicio de sesión. Como bien lo dijo Sergio, se han definido hartas cosas a lo largo de las semanas, por lo que vamos a hacer una pincelada dentro de lo posible a todos los módulos y las pantallas que tenemos actualmente. E idealmente, si es que tienen alguna duda o consulta, no hay ningún problema en que puedan interrumpir para que vayamos dejando todo bien definido. Le informo también que esta llamada en este momento está siendo grabada para tenerlo a modo de referencia a futuro.

Speaker 00 [04:08]: Dígame.

Carlos Vallejos [04:11]: Con Microsoft tendríamos que evaluarlo, tendríamos que evaluarlo. De momento no lo tendríamos dentro de lo que era la definición.

Speaker 00 [04:24]: Especialmente por usar los mismos correos. ¿Y qué pasa si tenemos, por ejemplo, tenemos otra implementación de desarrollo y le mostraste a los desarrolladores el ingreso con la clave y todo lo demás?

sergio [04:38]: Sí, sí, sí lo podemos incorporar el Authenticator de Microsoft. Esa era una duda que en realidad yo tenía porque, bueno, se puede hacer con Facebook, Instagram o Google, que es de Gmail, o Microsoft. Pero sí lo podemos incorporar, esa autenticación. No escucho muy bien, Carlos.

Speaker 01 [05:09]: Yo me hice un usuario en la página y yo puse el correo de AlmaWeb y me pescó perfectamente.

Carlos Vallejos [05:15]: Sí, está implementado para que se puedan crear con cualquier correo, pero no está hecha la conexión como tal a Microsoft en sí.

sergio [05:25]: Sí, lo que se refiere a Carlos, lo que se refiere, claro, no sé si han visto algunos inicios de sesión que aparece el icono de Microsoft bajito, la de Google, y que en realidad no ingresan contraseña, sino que seleccionan su cuenta que ya está logueada en el navegador, y ahí desde ahí se inicia sesión automático sin ingresar contraseña. ¿Me explico?

Carlos Vallejos [05:47]: Sí, vamos a dejarlo como nota ahí para futuro.

Speaker 00 [05:52]: En mi caso, principalmente cuando, no sé, hay un correo que expira o ya no se usa, al bloquear la cuenta en Microsoft como que se niega el acceso a cualquier plataforma que esté en el móvil.

sergio [06:07]: Claro, ahí la administración de los usuarios va a ser Totalmente ustedes, ustedes van a decidir qué usuario se mantiene activo, uno nuevo, o dar de baja, ustedes lo van a administrar.

Carlos Vallejos [06:32]: Pasando entonces a eso y también viéndolo en base a la duda que acaba de surgir, dentro de lo que se tenía estipulado es que dentro de este panel se administrará la creación de los usuarios, que lo más probable es que así es como lo hizo María Jesús con su usuario. Este ambiente que tenemos actualmente, que estamos viendo, un ambiente que está aparte de la página pública, por eso quizás no ves tu usuario acá, pero este es el panel que teníamos predeterminado para la creación del usuario. Ahora con esto vamos a surgir una modificación, pero la administración de usuarios también terminaría viéndose desde acá.

Speaker 01 [07:08]: Exactamente.

sergio [07:09]: Exactamente.

Carlos Vallejos [07:10]: Entonces, como pueden ver en este panel de administración, dentro de lo que vendría a ser los usuarios, al momento de realizar la creación, aquí nos figura también a qué empresa pertenecen, porque dentro de acá podemos hacer la creación de las diferentes empresas que va a tener el ERP para las diferentes administraciones que tengan. Y lo importante de esto es que se tiene que tener en consideración que en la empresa donde estamos ubicados actualmente es la que predomina en el menú de acá.

Speaker 00 [07:41]: No hay problema.

Carlos Vallejos [08:25]: Perfecto. Entonces, partiendo de lo que vendría a ser la creación de las empresas, se crean desde el panel de administración empresas, y eso es la que va a mandar dentro de lo que vendría a ser donde estamos trabajando actualmente. Aquí también podemos ver lo que vendría a ser los periodos, donde el sistema siempre va a mostrar acá en qué cliente, perdón, en qué empresa están trabajando y bajo qué periodo, y también el estado del periodo. Exactamente. Eso qué quiere decir, que si ustedes están viendo, por ejemplo, en este caso estuvieran dentro de su computador viendo el usuario Almaue SPA y yo estuviera viendo el Almaue Logística Ltda, no va a coincidir ni va a actualizarse lo que yo esté viendo versus lo suyo. Van a ser administraciones totalmente diferentes, por ende el que yo cambie de acá no tendría incidencia en otro usuario.

Speaker 00 [09:19]: Oye, y otra consulta, el usuario al final, no sé, el súper admin imagino que puede ver toda la empresa y hay otros usuarios que a lo mejor ven cierta empresa, ¿no? Exactamente.

Carlos Vallejos [09:37]: De hecho, acá en la creación de usuario es donde uno define la empresa a las cuales usuarios va a poder tener acceso, junto también con la administración de la contraseña, que eso ya, como les digo, tendría que modificarse con el tema de Microsoft. Pero la administración vendría a ser lo mismo, y aquí también se reflejaría el estado de la cuenta. Ahora, lo que va de la mano con eso Serían los roles y permisos. Acá visualmente hay un pequeño fix que tenemos que hacer todavía, ya que esta aprobación no corresponde a este menú, debería eliminarse, ya que esto era parte de una implementación antigua. Pero esto no hay que considerarlo, más rato les voy a explicar por qué. Volviendo a lo que vendría a ser las creaciones de roles, aquí tenemos unos roles predeterminados que nos entregó María Jesús para que nosotros pudiéramos trabajar por mientras. Y como pueden ver, se pueden crear más roles donde aquí podemos usar el nombre del rol, podemos darle los diferentes permisos dentro de lo que vendría a ser la página, que se ven reflejados por panel del dashboard de la izquierda. Entonces acá podemos realizar habilitación de permisos de lectura y habilitación de permisos de escritura. El de escritura siempre va a pedir de que se dé el de lectura por obvias razones. Y también se puede seleccionar rápidamente para dar permisos por panel.

Speaker 00 [11:00]: Oye, ¿y cómo nacen los permisos por empresa?

Carlos Vallejos [11:04]: En este caso, como se va gestionando por rol, en caso de que necesiten tener definiciones por empresa, la idea sería que se vaya creando un rol por empresa y se vaya asignando a la persona.

Speaker 01 [11:15]: De todas maneras, igual cuando uno selecciona el rol le puede despinchar cierto acceso.

Speaker 00 [11:23]: Exactamente.

Speaker 01 [11:28]: Sí, cuando tú creas el usuario, elige a las empresas que puedan tener visualización.

Carlos Vallejos [11:35]: Y por último, la que sería de las parametrizaciones de este panel de administración son las aprobaciones, donde podemos crear reglas. Y aquí es donde se define cuáles son las personas que van a aparecer disponibles para solicitar las aprobaciones de lo que vendría a ser la parte de las órdenes de compra, los contratistas con sus proformas y la parte comercial. Son esos 3 aspectos que hemos considerado para la solicitud de aprobaciones dentro del sistema. Aquí, como podemos ver, podemos dejar la regla si está activa o no, más que nada para control, controlar los montos que se aprueban por cada una de las reglas de aprobación. Y también, en este caso, por ejemplo, si tienen más de un rol que pueda aprobar órdenes de compra. Aquí pueden seleccionar de los usuarios que se encuentran activos en el sistema varias personas para que puedan aprobar en ese aspecto.

Speaker 00 [12:26]: Oye, Carlos, te puse una pregunta.

Carlos Vallejos [12:28]: Dígame.

Speaker 00 [12:28]: Pensando en un futuro y pensando en otras estructuras de empresa, obviamente la idea es que sea medio genérico, pero sí que funcione más para más ámbitos. ¿Tú, por ejemplo, no puedes poner como una cadena de aprobación? Cachai, porque por ejemplo estoy inventando, ya la Siri trabaja con Mario y Mario trabaja conmigo, que alegremente yo tengo un jefe, cachai. Entonces a lo mejor la Siri va a generar una orden de compra y se la va a mandar a Mario, Mario la va a aprobar pero no tiene la capacidad de poder autorizar por el monto y me tiene que saltar a mí claramente.

sergio [13:00]: Agustín, para entender, tú te refieres como a niveles de aprobación, por ejemplo, no sé, defino la orden de compra, tiene el primer nivel, va a pasar por Mario. Un segundo nivel por Juanito, así, claro.

Speaker 00 [13:12]: Ya te entiendo. O sea, si Mario tiene, estoy inventando, la orden de compra es de 400 lucas y Mario tiene por 500, la aprobó, puede estar autorizado, ¿cachai? Pero si era por 1 millón y Mario, obviamente yo voy a ver la aprobación de Mario, yo lo voy a mirar y la voy a aprobar yo, ¿cachai? Si era por 10 millones, la va a tener que aprobar mi jefe, no tiene que pasar por todos nosotros, ¿cachai?

sergio [13:32]: Ya, pero ese segundo nivel ¿Se activaría siempre y cuando pasa los límites?

Speaker 01 [13:41]: Claro, siempre.

Speaker 00 [13:42]: No, cuando pase el límite, porque obviamente es un monto porque está autorizado para ese monto.

sergio [13:48]: Ya, ok, sí, sí, sí, te entendí perfecto.

Speaker 00 [13:50]: Y lo otro, que la persona que crea la orden de compra, no sé cómo se puede hacer eso, pero automáticamente venga asociado a su jefatura, ¿cachai? Por cosas que la SIDI no voy a mandarlo a aprobar porque con gente de la otra área, porque sabe que puede interesarle más y son amigos.

Carlos Vallejos [14:09]: En ese caso tendríamos que tener un control de jefatura igual.

sergio [14:18]: O no te escuché muy bien, Agustín.

Speaker 00 [14:19]: Como un control de dependencia. Sí, porque claro, ¿qué pasa? O sea, no quiero ser mal pensado, pero en muchas instituciones, pues bueno, no sé, terminó de la sede y quiere hacer la cuestión y sabe que Mario a lo mejor no tiene la capacidad de autorizárselo y se lo va a mandar a la Lube, que puede autorizar todo un millón y Mario hasta 500. Y como son amigas, pasó la cuestión y se arreglaron entre las dos.

Carlos Vallejos [14:40]: Sí, sí, podemos implementarlo, podemos implementarlo por niveles que dependan del monto. De tal monto a tal monto aprueba tal persona, y de tal monto a tal monto tiene que pasar por una segunda aprobación.

Speaker 00 [14:52]: Y por persona, claro. Entonces, obviamente, cuando esa persona cree la orden de compra, sí o sí ella no va a decidir para dónde se va la orden de compra. O sea, la orden de compra automáticamente se tiene que aprobar por ella. Es lo que, por ejemplo, los materiales de hoy día, que por ejemplo yo le autorizo a José Tomás y José Tomás depende de Martín, pero no tiene ningún sentido. O sea, yo voy a revisar la cuestión, pero yo no soy el que aprueba. No me preguntéis por qué siempre apruebo yo esa cuestión, pero por rigores, por organigrama, por dependencia, de ahí se pasa a Martín. Y si Martín no es capaz, Martín debería darle el visto bueno muy o menos por su monto y que le pase al gerente final hasta que alguien pueda aprobar la cuestión.

sergio [15:28]: Sí, te entiendo.

Speaker 00 [15:31]: Digo, porque yo la he hecho, trampa hecha. Entonces yo creo que Alejandro es el tipo que usted hoy día que estamos desarrollando, a que después empiezan a saltar y es tarde. Yo soy súper mal pensado a las cosas, pero no, mejor no.

sergio [15:43]: Está bien, está bien. Sí, la idea es que todo lo que se vaya desarrollando sea como administrado por ustedes. Ustedes definan, por ejemplo, quiénes van a ser los usuarios, cuáles son los niveles, cuáles son los máximos. Es decir, si excede el máximo, ¿qué usuario va a tener que aprobar o qué entra al juego? Todo eso se ha administrado por ustedes.

Speaker 01 [16:04]: Lo que pasa es que acá es algo más que el monto de aprobación. Es, por ejemplo, si mi analista hace una orden de compra, solamente le aparezca yo como jefatura para aprobar, no que aparezca otra jefatura. Eso están pidiendo, que vaya en línea de mando. Claro, por ejemplo, porque con Mario podemos tener el mismo monto de aprobación por ser jefatura, pero La Fran en este caso no le podría mandar una orden de compra a Mario, siempre tiene que ser a mí.

Speaker 00 [16:32]: Con Mario, a ver, eso pasó y pasó pago y corrió todo el flujo.

Speaker 01 [16:37]: Y quizás por línea de mando.

Speaker 00 [16:41]: Ahora, por ejemplo, ya la pregunta interna: si la persona que está en tu línea de aprobación no está, ¿qué pasa?

Speaker 01 [16:48]: Pasa a la equipo de la siguiente.

Speaker 00 [16:49]: Pero, ¿cómo vas a ver el sistema? No, porque si, por ejemplo, En rigor, yo también te hice lo que haría tuyo, también te hice ver la hora de contrapaso. O no sé, estoy inventando, habría que mirarlo. Por ejemplo, si la pared que tú usas de vacaciones, hay que meterle un poco a esa, pero esa es la idea.

sergio [17:15]: O sea, ya como lo que veo en realidad un poquito es como A nivel de usuario, definirle los niveles y la dependencia.

Speaker 00 [17:27]: Claro, claro, pero la dependencia siempre. Entonces, si la, por ejemplo, la Fran le mandó una orden de compra a María Jesús, que María Jesús por el monto no le da, la va a aprobar, pero sin monto va a quedar todavía pendiente y me va a saltar a mí automáticamente hasta que yo pueda. Si no puedo, me va a pasar a mi jefe, y así hasta que alguno pueda autorizarlo por el monto. Pues tú siempre, por ejemplo, querís que haya esa doble check. Sí, vos. Entonces, ¿qué pasa? Que cuando llegue la cuestión de la orden de compra a la SIDI, yo voy a decir, tú la miraste, vos. Entonces, no me llega una orden de compra directamente a la SIDI y yo voy a decir, ¿quién es esto? Entonces, ¿qué pasa? Que si tú te vas a ir a una empresa, pueden haber unos 50 niveles bajos, vos. Entonces, te va a llegar uno directo, ¿cachai? Y después va a decir, ¿qué chinga es esto? Entonces, debes tener una planta. Y te metía la planta, no sé, a lo mejor la persona que trabaja en postería hizo un antecopio y me saltó a mí directamente, y decía, ¿qué está jugando? Pero con todo el respeto, estoy medio desesperado.

sergio [18:24]: No hay problema, no hay problema.

Speaker 00 [18:28]: Entonces iba a decir, ¿quién es? Pero obviamente que si viene con la quemadura, que no diga, ah, cacho es Mario. Si Mario me lo revisó porque alguien que trabaja con él para abajo y que lo va a utilizar. Pero sí habría que ver varias cosas de cómo pasa el tema de las dependencias cuando no está, hay que solucionar un par de temas ahí, pero hay que meterle un poco a eso, pero sería bueno.

sergio [18:51]: Sí, pero se entendió la idea.

Speaker 00 [18:53]: Sí, puta, me van a invitar más a las reuniones.

Carlos Vallejos [18:56]: Vamos a generar una propuesta, se entendió. Yo creo que ya teniendo una propuesta más visual y concreta podríamos tener más correcciones, pero se entendió de que necesitan de que haya el traspaso tanto de lo que vendría a ser de responsabilidades, pensando en las vacaciones, una persona no pueda estar disponible. Y también tener niveles, que una persona tenga, no es tanto por los montos, sino de que tenga que pasar por aprobación también de una jefatura de la jefatura, ¿verdad?

Speaker 00 [19:23]: Claro, por el monto, claro.

Carlos Vallejos [19:24]: Perfecto.

Speaker 00 [19:25]: Y con dependencia, claro. Por eso digo, no cualquiera le puede mandar una orden de compra a cualquiera, ¿cachai?

Carlos Vallejos [19:30]: En ese caso me imagino que al momento de crear el usuario sería bueno identificar a qué área pertenece y en la jefatura, y ahí podríamos tener como ese Claro, tenemos que crearlo por organigrama, va a ir haciendo las dependencias abajo. Exacto.

Speaker 00 [19:44]: Y por ejemplo, hay casos que podría depender de más de uno y le podríamos dejar a más de una dependencia, y esa persona sí puede mandársela a 2 personas. En el caso, por ejemplo, la Lupe o de la Fran, que muchas veces hace lo de compra, le voy a poner, inventando el nombre, pero le podría poner más de un cliente, así que va a estar ayudando a varias áreas.

Carlos Vallejos [20:01]: Puede ser.

sergio [20:03]: Claro, pero ahí también que sea configurable que si esa persona es opcional u obligatoria la aprobación de su Claro, claro, claro.

Speaker 00 [20:11]: No, voy a ver, hay que vender un poco esa.

Carlos Vallejos [20:14]: Perfecto, ahogar. Entonces, dentro de los pendientes, llegar con una propuesta que abarque todo lo que necesitan.

Speaker 00 [20:22]: Un segundo, un segundo, para explicar acá a los chiquillos. Cachai, a lo mejor José se la manda a Martín y Martín por facultades, pero no le vale el monto. Y para que Nico se la juegue, pueden pasar por años. Entonces probablemente Martín me lo pueda mandar a mí.

Speaker 01 [20:40]: Bueno, la idea, Agustín, también es que empecemos a acostumbrar los departamentos a que cumplan con sus funciones.

Speaker 00 [20:47]: No, no, por eso digo, entonces José Tomás que se la manda a Martín, y probablemente Martín por monto, porque la factura más chica de José Tomás son de 500 palos.

Speaker 01 [20:55]: Pero es que igual, como Martín es gerente, va a tener los mismos montos que tú, pues, si son en la misma línea.

Speaker 00 [21:00]: No sé, pero lo dudo.

Speaker 01 [21:06]: Igual vamos a tener un problema de cruce de información porque ahí tenéis que poner que José Tomás te puede mandar a ti como gerente, le puede mandar a Martín, igual van a estar cruzadas las líneas de jerarquía.

Speaker 00 [21:15]: No, pero Martín se lo va a poder mandar a Nico o a mí, no sé, hay que revisarlo, pero obviamente por un tema de responsabilidades Martín va a tener el mismo monto de prácticas que yo.

sergio [21:28]: La idea es que ustedes definan el flujo y después, bueno, se plasma a los usuarios de cómo tienen que utilizar y cuál va a ser el flujo final.

Carlos Vallejos [21:40]: Quedamos pendientes entonces a que nos den la definición bien de cómo podríamos hacer el flujo. Igual, de todas formas, voy a armar una propuesta por mientras. Volviendo a lo que vendría a ser el ERP, ahora vamos a pasar por la parte de la parametrización, que es donde se configura todo lo que va a tener instalado interacción dentro de la plataforma. Esta parte ya un poco más rápida, lo que vendría a ser este menú, ya que como pueden ver aquí en la parametrización de monedas se ingresan las monedas que tengan en el sistema. Lo mismo con las unidades de medida, los centros de costos, que aquí tenemos unos de prueba, los tipos de documentos que están en el sistema, los elementos de costo Y lo que vendría a ser proveedores. Si se dieron cuenta, me salté estas dos páginas.

Speaker 00 [22:30]: ¿Proveedores y clientes son aparte? No es la misma base de datos.

Carlos Vallejos [22:44]: Si gustan, podríamos tenerlos así de que tengan cruces entre ellos. De momento los teníamos separados porque no sabíamos si es que existía la posibilidad de que la misma persona fuera cliente con algún nombre similar más que nada como para evitar esa duplicidad. Perfecto, lo dejamos entonces para que sea una base de datos compartida.

Speaker 01 [23:06]: Yo prefiero que sea base de datos individualizada porque si quiero sacar un listado de proveedores no se me va a mezclar con clientes. Ahora, en la consulta del RUT quedamos que iba a tener el detalle de si tenía RUT como sociedad, estaba creado como proveedor, como cliente, como productor. Sí, que en la consulta va a estar todo por RUT, pero en la base de datos como proveedor y como cliente por separado.

Speaker 00 [23:34]: Perfecto.

Carlos Vallejos [23:36]: Aquí tendríamos el panel con los indicadores del Banco Central, que aquí falta hacer la configuración para dejar el periodo que va a ir actualizándose esto, porque no habían dicho. Esto actualmente, por cómo lo utilizaban, se actualizaba a las 9 de la mañana. La idea es que aquí tenga la parametrización de, en caso de que quieran seleccionar la hora, y también tener un historial de estos campos que va trayendo desde el Banco Central hacia el ERP de manera automática. Y finalmente, lo que vendría a ser el plan de cuentas. Acá ya tenemos cargado el que nos entregó María Jesús Centrello, con cada uno de sus niveles de detalle, y también con la posibilidad de agregar más en cada uno de ellos. Excelente, excelente. Por ejemplo, acá vamos a crear uno de prueba, categoría 7.

Speaker 00 [24:27]: ¿Creen que le pega contabilidad aquí o no?

Speaker 01 [24:31]: ¿Qué, Carlos?

Carlos Vallejos [24:32]: ¿Cómo, perdón?

Speaker 00 [24:33]: ¿Quién le pega contabilidad acá?

Carlos Vallejos [24:35]: Sergio, el máster de contabilidad.

sergio [24:38]: Tenemos nuestro contador interno, pero nosotros todos los desarrollos relacionados a contabilidad pasan por la revisión de nuestro contador.

Carlos Vallejos [24:49]: Bueno, y aquí se pueden agregar más subniveles dependiendo de la necesidad, y también está la posibilidad de editarlos junto con la eliminación.

Speaker 01 [25:00]: ¿Podría mostrar cómo se crea una cuenta contable? Porque ahí tú creaste una clasificación de que sería el nivel 1, pero yo quiero ver cómo se crea el nivel 5.

sergio [25:15]: Ahí sería a nivel de caja, debería crear uno, ¿cierto?

Carlos Vallejos [25:18]: Exacto, y se hereda también el código que viene desde arriba.

Speaker 01 [25:26]: Ya, yo tengo una duda, porque actualmente nosotros por cuenta podemos determinar si está asociado a centro de costo, elemento de costo, área de negocio, XX. Entonces aquí nosotros también deberíamos tener la opción de poder agregarlo, quitarle características.

Carlos Vallejos [25:45]: Perfecto.

sergio [25:47]: Y eso, y esa información, María Jesús, ¿la tiene a mano?

Speaker 01 [25:50]: Y de hecho, en el plan de cuentas que le adjunté, arriba sale como toda el área de negocio que yo puedo pinchar y si está activo o inactivo.

Carlos Vallejos [26:00]: Ok, vamos a escribir entonces esa información.

Speaker 00 [26:12]: Carlos, una pregunta de funcionamiento. ¿Qué pasa si tú tienes un plan de cuentas y veo que tenés el basurero y eliminás una cuenta? ¿Qué pasa con toda la información que hay para atrás? Estoy diciendo para que no exista un error administrativo, que se pueda borrar la cuenta y se volvió a crear y se borró la información.

sergio [26:33]: Ahí, bueno, buena pregunta, Agustín. Ahí tenemos que Bueno, lo sano es que no se pueda eliminar si tiene movimiento asociado, comprobante.

Speaker 00 [26:42]: Además que se inactiven, ¿no?

sergio [26:44]: Claro, pero ahí todo eso, esos asientos, ¿a qué cuenta lo asociaría, hermano? ¿Cómo lo dejarían ahí?

Speaker 00 [26:54]: Por eso, entonces, si lo inactiváis, no lo podéis usar nomás, pero va a seguir ahí hasta que—

sergio [26:58]: Ah, claro, todos los comprobantes. Ya te entiendo.

Speaker 00 [27:01]: ¿Me cachai? Si lo inactiváis van a quedar todos los comprobantes, pero no lo podés utilizar más a cuenta.

sergio [27:07]: Claro, no lo podés utilizar, generar más asientos asociados a esa cuenta.

Speaker 00 [27:11]: Y lo mismo que si lo modificamos, si lo modificamos, ¿se modifican para atrás también o se modifican solamente desde ahí? ¿Hay que revisar eso?

sergio [27:18]: Sí, buena acotación.

Speaker 00 [27:20]: Son cagazos típicos.

sergio [27:23]: O sea, en realidad la cuenta se podría eliminar siempre y cuando no tenga nada asociado. Claro, no había problema. Eliminar o editar.

Speaker 00 [27:36]: Perfecto, vamos a dejar entonces habilitada solamente la opción de deshabilitar, porque en rigor si cambia el nombre se va a cambiar para atrás el nombre, ¿no?

Carlos Vallejos [27:51]: Exacto.

Speaker 00 [27:57]: Hoy está filé de esa cuestión, se me ocurrieron miles de cosas.

Carlos Vallejos [28:02]: Todo feedback es bien recibido.

Speaker 00 [28:04]: Es que sabéis que nos pasa harto ahí en la administración, me vuelvo a regir, cachai, que a nosotros de repente se nos empiezan a traslapar las temporadas ya, y obviamente queremos hacer ejercicio, y muchos gastos de estos de que tenemos de la próxima temporada que ya lo tenemos en esta Solamente, ¿cachai? Nosotros las empezamos a activar, que la administración tiene una cuenta solamente, ¿cachai? Que sale una cuenta que se llama gastos próxima temporada. Pero claro, de esta forma podríamos subir la cuenta de próxima temporada o crearle, no sé, alguna como un tipo, una especie de activo de balance abierto por cuenta y después solamente el traspaso por cuenta. Entonces después la administración siempre se tiene que meter cuenta por cuenta y hacer el traspaso una por una, es un cacho más o menos.

sergio [28:45]: Ah, ya te entiendo.

Speaker 00 [28:47]: Está hecho, parece muy buena estas cosas, que está bueno.

sergio [28:51]: Ah, sería un traspaso. Entonces claro, ahí podríamos agregar, no sé si es como el botoncito actualizar, que seleccionen la cuenta y la cuenta destino. ¿A eso te refieres tú?

Speaker 00 [29:04]: Sí, sí, que ofrece manual que hacemos, porque por eso te digo, nosotros por ejemplo aceptamos la temporada 25-26, ¿cachai? Y yo hoy día estoy pagando servicios de la temporada 26, 27 ya. Entonces obviamente para que no se me ensucie el resultado, ¿qué hace la María Jesús? Agarra todos esos gastos y los activa, ¿cachai? Pero los pone en una cuenta que se llama gastos próxima temporada, una cuestión así. Pero hay veces que se le dan un saco y después tiene que, cuando pasamos a la temporada baja, y los lleva al gasto del activo del gasto, ¿cachai? Entonces por eso es muy buena la discusión para poder después llevarlos segregados, todo ya abierto, sobre todo para el presupuesto de mayo. Pero no, está perfecto, no hay que hacer nada.

sergio [29:44]: Bueno, la idea es que ustedes también, bueno, esto no sé, no está el local de momento, Carlos, ¿cierto? Bueno, le vamos a entregar los accesos para que ustedes también vayan ahí cachureando la plataforma y dándole el feedback.

Carlos Vallejos [29:58]: De hecho, para el día de mañana va a quedar esta actualización en el publicado para que puedan acceder y revisar, y como va a estar conectado a una base de datos de prueba, van a poder ingresar datos eliminar sin ningún tipo de problemas para que empiecen a probar la plataforma. Nada de esto va, son como datos reales de por sí, más allá de la estructura que tenemos acá del plan de cuentas que nos entregó la marca. Vamos entonces con lo que vendría a ser el flujo de las ventas. Esto parte con la creación de lo que vendría a ser los prospectos de clientes, donde me imagino que esto también la idea sería que quede enlazado directamente con clientes. Teníamos igual esta base de datos separadas Y aquí me surgía la duda si es que los prospectos de clientes, su razón de ser es solamente de registros para después dejarlos como clientes, porque aquí podríamos dejar la posibilidad de guardarlo directamente como clientes, o si los dejamos en la misma base de datos con una etiqueta de cliente o prospecto.

Speaker 00 [31:01]: Por lo que me había dicho la Mari, los prospectos directamente como clientes, porque si lo creamos porque ya está la relación laboral Sí, oye, es que insólito me da cuando uno crea cliente, tú ves ficha cliente, deberíamos poder editarlo.

Carlos Vallejos [31:22]: Sí, se pueden editar los clientes.

Speaker 00 [31:23]: Y esa cuestión, podríamos quedar activos sus datos bancarios, todo el tema que después traiga con tesorería.

Carlos Vallejos [31:30]: Sí, podríamos dejarlo acá como registro por cada cliente.

Speaker 01 [31:33]: En ese caso sería el proveedor.

Speaker 00 [31:37]: Perdón, en el proveedor, en el proveedor, en el proveedor. Igual les queda al mes, obviamente hay que volverle nota al cliente, pero ambos dos. Entonces cuando hagamos una cuenta de cliente o de proveedor, tiene que venir los datos bancarios.

Carlos Vallejos [31:50]: Perfecto.

Speaker 00 [31:51]: Sí, porque actualmente está consiguiéndose la cuenta, haciendo buscarla al correo. Entonces cuando creamos un cliente, un proveedor, que te pida, igual ingresas varias cuentas, por ejemplo, la cuenta en dólares, la cuenta en pesos, la cuenta en pesos 2.

Carlos Vallejos [32:07]: Sí, sí, sí, podemos incluir esos datos también parte del registro. Los dejaríamos acá abajo como datos bancarios para tenerlo como datos opcionales.

sergio [32:16]: De todas formas, disculpa, el tema de las direcciones de despacho o datos de contacto, ¿también lo incorporarían acá?

Speaker 00 [32:25]: También, porque yo haría una cosa fija. Sí, yo haría todo junto porque cachai que al final cuando lo obtuvo, ¿crees, Sergio Carlos? Pediste con nosotros mismos, vamos a hacer una ficha y la posibilidad de que tenga un problema nuevo, pues para que lleve la ficha al problema.

sergio [32:51]: Entonces ahí podríamos, ahí podríamos, Carlos, agregar dos pestañitas, una que sea los datos bancarios, otro de despacho y de contacto. Porque bueno, un cliente puede tener, o proveedor puede tener, n contactos y n direcciones también.

Speaker 00 [33:04]: Y n cuentas de banco.

sergio [33:05]: Claro, perfecto.

Speaker 00 [33:07]: Y de las diferentes monedas. Pero yo haría una ficha al final, Sergio Carlos, haría una ficha cuando tú tienes el cliente, cosas que no estemos acá todo el rato editándolo, cosas que no aparezca el cliente porque sería una forma, ahora al lado en otra, ¿cachai? Y al final dices, este es el proveedor, este es el proveedor, y nadie más le metió mano, ¿cachai? Porque igual también hay estafas que cambian las cuentas y hartas cosas.

sergio [33:31]: Entiendo. Claro, así obviamente todos los otros módulos, por ejemplo, cuando trabaje con los clientes, van a trabajar con la ficha, los datos de este módulo, de este administrador.

Speaker 00 [33:42]: Claro, la idea es que esto sería después para buscar de ese mismo dato también para pagar.

sergio [33:47]: Claro, ahí por ejemplo es una problemática que varios, varios software no tienen cubierta. Ustedes quieren incorporar trazabilidad en las ediciones de algunos mantenedores o registros como delicados. Por ejemplo, ¿qué pasa? Que el cliente, no sé, el cliente Juanito le cambiaron la razón social. ¿Quién fue? ¿Qué usuario fue? ¿Cuándo fue?

Speaker 00 [34:12]: ¿Por qué fue?

sergio [34:15]: ¿Cómo?

Speaker 00 [34:16]: ¿No lo podías dar con clave para que no puedan editar? Sí, o que lo vea gerencia nomás, que lo pueda editar.

sergio [34:27]: Claro, eso va a ser parte del rol, el rol que le asignen al usuario. Sería bueno que nos indiquen, por ejemplo, cuáles son los datos críticos por los mantenedores. ¿Cómo?

Speaker 00 [34:43]: A lo que le puedes poner el registro, ponle.

sergio [34:51]: Ya, ok.

Speaker 00 [34:52]: O sea, cualquier cosa que se cambie, nadie nunca fue. Entonces lo mejor es dejar siempre el registro.

Speaker 01 [34:59]: O sea, actualmente igual tenemos la trazabilidad de cuándo se hace una modificación o quién hace la creación de cada usuario. Yo creo que eso hay que mantenerlo. También que no todos los usuarios puedan crear y editar, eso ya lo habíamos hablado con Carlos, que hay paneles o restricciones que se necesita clave para poder reversar o eliminar.

Carlos Vallejos [35:20]: También hay permisología de lectura y escritura, entonces dependiendo también del módulo del permiso que se le dé, solamente va a poder leer datos o escribir. También está la posibilidad de no dejarle acceso al panel.

Speaker 00 [35:45]: Oye, me dice, sí, recién antes no estaba escuchando, parece que está ahí lo que le decía a los chiquillos. Quisiéramos una ficha, una pura ficha para todo. O sea, cuando me cree el cliente, que él tiene el frente, ponga los contactos, que pongan los datos bancarios, que dobla en la ficha de creación.

Speaker 01 [36:02]: Tú dices alguien que solicite crear el proveedor, el cliente.

Speaker 00 [36:05]: Claro, y cuando nosotros creemos acá, creemos todo de una, ¿me cachai? En un puro lugar.

Speaker 01 [36:10]: No te entiendo, pero que la persona que solicita mande la ficha.

Speaker 00 [36:13]: Sí, nosotros hacemos una ficha interna que cuando le guste le enviamos los bancos, le llevamos todo el respaldo de quién está solicitando el proveedor al cliente. Exacto, o sea, nosotros también por los requisitos, una ficha de cliente, igual como cuando nos piden a nosotros, yo puedo mandar todo que quiero como cliente y proveedor. Entonces así ya lo creamos al lote, la luz después no anda buscando las cuentas por todos lados, va a estar todo consolidado la información.

Carlos Vallejos [36:42]: Vamos a continuar revisando los otros paneles. Vamos a ir ahora a lo que vendría a ser el menú de las cotizaciones. Aquí es donde predomina el aprobador, que se tiene que configurar Yo creo que en base a lo que estamos hablando en esta reunión va a pasar por una rectificación de cómo está funcionando actualmente para que coincida con lo que están solicitando. Pero en sí, como lo vimos dentro de la administración, las personas que aparezcan en las reglas de aprobación de cotizaciones son las que pueden realizar. En este caso, como yo estoy en el de admin, el admin puede ver todo lo que vendría a ser las aprobaciones como tal, todo el historial. Acá, por ejemplo, es el menú de la creación de la cotización como tal, donde se pueden agregar los ítems, precio unitario, cantidad, se puede dejar directamente el estado. Y en caso de que hay un cliente que no esté creado, aquí también se podía crear directamente. Aquí, como lo hablamos recién, faltaría también la opción de agregar los datos opcionales bancarios para completar la ficha según lo que acaban de solicitar. Y aquí podemos ver lo que vendría a ser una cotización ya aprobada. Así sería finalmente.

Speaker 00 [38:12]: Te hago una pregunta, Carlos.

Carlos Vallejos [38:14]: Dígame.

Speaker 00 [38:14]: Esto va a estar asociado después a la facturación, o sea, por ejemplo, yo tengo la cotización y después yo le voy a poner facturar la misma cotización y se va a facturar la misma cotización.

Carlos Vallejos [38:21]: Exactamente.

Speaker 00 [38:23]: Ya, oye, ¿te puedo hacer una pregunta?

Carlos Vallejos [38:24]: Dígame.

Speaker 00 [38:25]: Es que tú te devuelves para atrás un poquito y ponerle nueva. Y ahí sale, por ejemplo, servicio, producto. Si la idea es que cuando tú salgas a buscar los productos, o arriba te ponga preguntas, sean de tus servicios o productos, tú salgas a buscar productos que te marquen los mismos códigos que tienen los productos creados por sistema, ¿cachai? O sea que, por ejemplo, si tengo caja de 5 kilos granel creada por sistema, Mario, ¿no puede salir a vender cajas cerezas?

Carlos Vallejos [38:55]: Vamos a hacer la conexión con esa base de datos.

Speaker 01 [38:58]: Claro, porque cuando hay, chiquillo, bueno, cotizaciones pero de ventas. Nosotros vamos a ingresar cotizaciones de venta, se supone que las cotizaciones son para las compras.

Speaker 00 [39:12]: No sé dónde está el pan, amigo.

Speaker 01 [39:15]: Aquí estamos en cliente, estamos en cliente, por eso es que eso es lo que me parece raro, porque cuando uno cotiza es para hacer una compra.

sergio [39:24]: Pero sí, pero ahí no se emitiría una orden de compra, o se cotiza y después se emite la orden de compra y luego la recepción de la factura.

Speaker 01 [39:37]: Es que por eso me parece raro que esté en ventas, porque cuando uno vende no hace una cotización para vender.

Speaker 00 [39:43]: Sí, es que, pero María Jesús, perdón, pero de repente muchas veces tenemos que hacer proformas para poder vender facturas. Aló, parece que es el aló.

Speaker 01 [40:00]: No se escucha, se escucha.

Speaker 00 [40:06]: A mí sí, es que de repente se nos pierde.

Speaker 01 [40:09]: No, no, para nada. Pero lo que pasa es que a mi criterio las cotizaciones son para las compras. Ahora, si queremos hacer una orden de venta, es distinto.

Speaker 00 [40:18]: Ah, bueno, hay que cambiarle el nombre.

Speaker 01 [40:21]: Claro, porque se supone que cuando nosotros emitimos las ventas lo hacemos directamente en el sistema de facturación, pero ya sabemos lo que vamos a vender. Ahora, si esto va a estar linkeado a algún stock, ejemplo de AlmaWeb, que estemos vendiendo caja en sí, te creo que puede hacer como linkeado a lo que hay en bodega, pero en realidad nosotros no hacemos cotizaciones para hacer ventas porque la cotización debería ser el orden de venta, debería llamarse el título.

Speaker 00 [40:50]: Porque después, cuando tú emitas el documento, Carlos, vas a ir a buscar la orden de venta, la cotización, como la tienen puesto, ¿verdad?

Carlos Vallejos [40:56]: Sí, sí, sí, este debería estar en el panel de compras.

Speaker 00 [40:59]: Procesadores.

Speaker 01 [40:59]: Debe estar en el panel de compras.

Carlos Vallejos [41:01]: Sí, efectivamente.

Speaker 00 [41:02]: Entonces, justamente, entonces, como dice la María Jesús, se dice llamar orden de venta.

Speaker 01 [41:13]: No sé, yo lo escucho.

Carlos Vallejos [41:18]: No sabemos si es que está pensando, le damos espacio para hablar. No, igual hay que decirlo, ahí cuando estar un poquitito lejos se escucha un poquitito despacio. Entonces cuando uno habla no sabemos si es que lo estamos interrumpiendo. Entonces por eso como que quizás a María José le pasa lo mismo.

Speaker 01 [41:40]: Ustedes escuchan muy lejos.

Speaker 00 [41:43]: Y ahí me escucho mejor.

Carlos Vallejos [41:44]: Sí, mucho mejor.

Speaker 00 [41:46]: Ya, oye, mira, como dice la madre de Jesús, efectivamente dice llamarse orden de venta.

Carlos Vallejos [41:50]: Sí, están en el panel de compra, efectivamente.

Speaker 00 [41:52]: Sí, exacto. No, por el de compra, orden de compra está bien, pues este orden de venta. Ya, porque por la orden de venta, y él se la puede quitar 200, 300 y facturarla. A ver, es que eso tiene razón. Después le podemos cambiar ese título, Carlos.

Carlos Vallejos [42:16]: Sí, por supuesto.

Speaker 00 [42:18]: Ya, mira, y tú cuando creas una nueva orden de venta, a ti justamente cuando ponís el folletero automático y ponís el cliente, a ti te debiese dar 2 tipos de orden de venta, ¿cachai? O un servicio o un producto.

Carlos Vallejos [42:32]: Perfecto.

Speaker 00 [42:34]: Ya, y los productos debiesen venir linkeados a los productos que tú tienes en bodega, e incluso en qué bodega tú lo vas a trabajar, porque cuando después tú factures, verdad, no ahora, pero cuando tú factures te tiene que hacer la salida cliente y hacerte la rebaja, ¿me cachai? O de inventario.

sergio [42:49]: Entonces van a manejar inventario, eso es lo que yo le había consultado.

Speaker 00 [42:53]: Entonces mira, por ejemplo, tenía hoy día, tenía un 46%, ¿verdad?

Carlos Vallejos [42:58]: Exacto.

Speaker 00 [42:59]: Entonces, por ejemplo, tú vas a ir hoy día y vas a emitir una orden de venta, ¿verdad? Y le voy a poner insumos, perdón, perdón, le voy a poner, ponle nuevo, que se la voy a poner ya al cliente, cualquier cliente. Y tú vas a pinchar que va a ser, por ejemplo, que va a ser un producto, ¿cachai? Y le voy a buscar los productos que queréis facturar y le voy a poner URI al 46%, cantidad de la bodega que lo vaya a vender, precio unitario, descuento, pam, crear, ¿cachai? Y cuando tú salgas a emitir el documento y tú vengas a buscar esta orden de venta, lo que tiene que hacer por el lado de insumos hacerte la salida del cliente y rebajarte el inventario. ¿Me cachai?

sergio [43:40]: Claro. Oye, Agustín, ahí tengo una consulta. Por lo que yo he visto, ahí tienen, trabajan como dos modalidades del tema del inventario, que puede ser, por ejemplo, en la nota de venta, cierto, que te baje el inventario O posiblemente que te lo trabaje sobre la factura. Cuando tú factures la nota de venta, que eso quiere decir que ya se vendió, ahí recién te mueve el inventario. ¿Quieren que eso sea configurable por ustedes? Por ejemplo, decir ya la nota de venta mueve inventario sí o no. O bueno, en realidad tiene que ser uno o el otro porque los dos no pueden mover el inventario.

Speaker 01 [44:19]: Sergio, yo creo que es mejor que quede como un registro de que efectivamente hubo un movimiento de bodega independiente de esa factura, no. Cosa que nosotros mensualmente podamos ver si faltan.

sergio [44:30]: No, no, no, no, no, sí, sí, te entiendo, María Jesús, que obviamente el documento que mueve el inventario tiene que hacer el movimiento de inventario, cierto, la rebaja de stock. Pero lo que voy yo, que nosotros perdimos, Carlos, ¿puede mostrar el login?

Carlos Vallejos [44:51]: Mi nombre es Carlos Vallejos.

Speaker 01 [44:56]: Habíamos avanzado a otro módulo, Agustín.

sergio [45:02]: Lo que yo les decía, bueno, María Jesús, que yo entiendo que cada vez que se mueva el inventario de una nota de venta o factura se tiene que dejar una trazabilidad, cierto, desde qué bodega, cuál fue el artículo que se movió, cuánto fue la cantidad, qué el usuario, todo eso. Pero lo que voy yo, que si prefieren que dejemos como administrable, que ustedes decidan qué documento va a mover el stock, Si ya sea la nota de venta o la factura, me explico, ¿no?

Speaker 00 [45:32]: Porque puede ser que la rebaja te la haga con la nota de venta o que te la haga con la factura, el tomar la definición. Claro, para que ustedes lo consideren, que cuando se emita la factura, que le rebaje inventario, o cuando emita la nota de venta, que se le—

Speaker 01 [45:44]: Lo que pasa es que por el módulo de venta funciona un poquito diferente, porque la venta en sí no va a ser el mismo precio que tengo en bodega. Entonces, para mí son movimientos distintos. Yo siempre dejaría, si estoy haciendo una nota de venta, o sea, claro, una nota venta, que se mueva inventario. Y si yo lo quiero asociar a la factura, que me traiga solamente la cantidad y el detalle del nombre, porque al final el monto puede que siempre sea mayor para tener la utilidad.

sergio [46:15]: O sea, cuando ustedes facturen la nota de venta en sí, no es que todo lo que está en la nota de venta se convierta factura, sino que ustedes pueden emitir una venta.

Speaker 01 [46:25]: La idea es, en la mayoría de los casos, tener un poco de utilidad de lo que estamos vendiendo. Entonces a llamar el mismo precio de la bodega. Por eso, cuando se sale de la bodega es un precio, pero cuando yo emita la factura tiene que asociarse solamente al movimiento de bodega, pero no al monto.

sergio [46:42]: Ya te entiendo. Entonces, en ese caso, cuando tengan la nota de venta, cuando le den facturar esa nota de venta, en realidad lo que va a hacer, o lo que debería hacer, es precargar toda la información de la nota de venta en la emisión de la factura para que ustedes puedan editar esos precios.

Speaker 01 [46:58]: Exacto, o sea, lo que a mí me importa es que se mantenga cantidad y descripción de lo que yo estoy vendiendo, pero no el monto, porque eso sí se puede modificar.

sergio [47:06]: Ya, ok, o sea, y cantidad, y bueno, los productos, que eso no se editen, solamente el precio.

Speaker 01 [47:14]: O sea, por lo que nosotros hemos vendido, yo dejaría que se mantuviera lo que está en bodega, pero sí o sí el precio habría que modificarlo. Lo otro yo lo dejaría tal cual, porque la cantidad igual es importante que vaya en el detalle de la venta.

sergio [47:28]: Oye, ahí María Jesús, por ejemplo, cuando tú facturas la nota de venta, ¿tú modificas el monto por cada línea de detalle o le das un recargo global al documento? Por cada línea de detalle, al precio unitario, ¿cierto?

Speaker 01 [47:49]: Sí, Mario, ¿no escuchan?

Speaker 00 [47:53]: Sí, espera, que estaba justo, se está diciendo que actualice la página. Un segundo.

sergio [48:00]: Ya, sí, sí. Bueno, eso.

Speaker 01 [48:06]: Muchas gracias.

Carlos Vallejos [48:15]: Ahora sí, ahora se ve como más HD, más ampliado.

Speaker 00 [48:21]: Ahí le puse un apretar y le quedó la perilla. Tiro el internet para que llegue nomás.

Speaker 01 [48:26]: Le quitaron a Chamonate. De ahí sé que se ven bien, al menos. Ya, entonces, viendo el tema de la orden de venta, un segundito.

Speaker 00 [49:01]: Y ahora sí, ahora sí, perdón.

Speaker 01 [49:06]: Ya estábamos viendo el tema de la nota de venta, la orden de venta, y llamara la cantidad y el producto, pero el precio fuera modificable al momento de facturar.

Speaker 00 [49:16]: Lógico, lógico. Lo que sí es clave, creo yo, Que no me dejara vender menos del costo.

Speaker 01 [49:27]: O sea, claro, sería un filtro que vamos a manejar que venda, pero sí, no sé si se podrá parametrizar así.

sergio [49:38]: O sea, si el producto tiene un precio como costo, un precio de compra, digamos, Que vale 10 pesos, no se puede vender a menos de 10 pesos. Claro, eso sí lo podríamos dejar en el mantenedor de productos, asociarle el precio compra, y en la venta que no, que te limite, porque no sea un monto inferior.

Speaker 01 [50:00]: Si se puede, ideal.

Carlos Vallejos [50:03]: Eso sería estrictamente para todos los casos, hoy nunca existiría la posibilidad de que se venda a menor precio, ¿verdad?

Speaker 01 [50:11]: No, ahí ya sería merma.

sergio [50:14]: Perfecto.

Carlos Vallejos [50:16]: Merma roja.

sergio [50:17]: Tengo otra consulta. En la emisión, por ejemplo, puede abrir, pensemos que se está emitiendo la nota de venta, ¿cierto? ¿Puede abrir una, buscarlo? Oh, tenemos problemas de internet nosotros.

Speaker 01 [50:35]: Le bajaron el internet.

Speaker 00 [50:36]: ¿Le bajaron la billetera?

Carlos Vallejos [50:38]: Sí, creo que será justo el último que se estaba trabajando en el local.

sergio [50:41]: Déjame ver si es que sí, este quedó con la admisión de la nota de venta, la cotización en realidad era que tú tienes. Ahí, por ejemplo, se entiende lo que decía Agustín, que se marque si es servicio, producto. Si es producto, se tiene que ir a buscar al mantenedor de productos. Exacto. Claro, ese producto puede estar, ese producto puede estar en más de una bodega.

Carlos Vallejos [51:23]: Así que siguen con problemas los chicos todavía.

Speaker 00 [51:26]: Deme un segundo que estoy aprendiendo.

Speaker 01 [51:39]: Lupe, no caigas a esa factura.

Speaker 00 [51:42]: Ya, vale, ya hice. Vale, quiere la perilla, Hugo. Bájale a los acuarios y nos ponen a fondo. Ya, vale, ya.

sergio [51:57]: Ahora sí, ahí se lo arreglaron.

Speaker 00 [52:00]: Es que tenemos un proveedor local, entonces uno lo llama y es fácil que gire las perillas.

Speaker 01 [52:03]: Excelente.

sergio [52:06]: Ya, bueno, aparece que se pegó de nuevo. Mira, Mario, Mario está pegado.

Speaker 01 [52:16]: Mario se pegó de nuevo.

sergio [52:19]: No sé si quieren dejar, pueden dejar de compartir la cámara.

Speaker 00 [52:22]: Voy a intentar eso, cerrarla, apagar la cámara, a ver si mejora. ¿Tengo que cambiar algo acá o no?

Speaker 01 [52:39]: ¿Y si volví a entrar?

Speaker 00 [52:42]: Bien, en todo caso, un segundo, un segundito.

Speaker 01 [52:50]: ¿Se fueron del modo?

sergio [52:53]: No le gustó el sistema.

Speaker 01 [52:56]: No, menos mal hoy día no estaba con ellos.

Carlos Vallejos [53:01]: Mari, representante de Almaue.

Speaker 01 [53:08]: La idea de aquí en esta palanilla es que se alimente directamente del inventario.

sergio [53:16]: Claro, ¿cuál es la idea? Mira, eso es lo que les quería preguntar.

Speaker 00 [53:20]: Por ejemplo, solicitar Y ahora sí que nos subieron la historia de respaldo. Ahora sí, con la cámara apagada.

sergio [53:38]: Ok, bueno, ahí se entendió perfecto lo que es el tema de seleccionar si va a ser un servicio o un producto, ¿cierto? Si es servicio, no va a listar nada, no va a estar enlazado al mantenedor de productos. Si es producto, debería listar solo los productos ya creados. Pero mi duda iba si el producto puede estar más en más de una bodega.

Speaker 01 [54:02]: Sí, puede estar en más de una bodega.

sergio [54:04]: Ya, entonces ahí, por ejemplo, si yo selecciono un producto que está en más de una bodega, debería yo también poder seleccionar a qué bodega voy a mover ese producto.

Speaker 01 [54:14]: Exacto, claro, habría que traer la bodega y ver el stock de cada bodega.

sergio [54:20]: Claro, ya te entiendo.

Carlos Vallejos [54:22]: Sí, por bodega, sí.

Speaker 00 [54:24]: ¿Y eso sirve como una base auxiliar? ¿O para que no te aparezcan varias veces el producto? ¿Cómo? ¿Y eso te pega como una base auxiliar para que no te aparezca varias veces el producto?

sergio [54:35]: No, no, o sea, el producto va a aparecer una sola vez, pero yo cuando selecciono el producto te liste las bodegas donde está ese producto. No es que se duplique.

Speaker 00 [54:43]: Consulta, Sergio, de los 2 o 3 bodegas que podéis meter, de 2 o 3 bodegas.

Speaker 01 [54:48]: Eso mismo. Si yo elijo un producto que está en 3 bodegas, ¿yo puedo sacar cierta cantidad de cada bodega?

Carlos Vallejos [54:54]: Tendríamos que parametrizarlo para que muestre una bodega o varias y la cantidad que quieren de cada una de esas bodegas. Sí se puede.

Speaker 01 [55:03]: Perfecto.

Speaker 00 [55:04]: Claro, por eso te decía, para que no aparezca cada vez, déjalo en una base auxiliar para que después te quede el respaldo por acá.

Carlos Vallejos [55:09]: En ese caso me imagino que sería bueno seleccionar en la misma lista del producto que diga la cantidad al momento de desplegarlo, y también podría tener quizás las iniciales de la bodega donde se encuentra, y al momento de desplegarlo mostrar la cantidad que tiene por cada una de las bodegas. Y seleccionar las que quieren.

Speaker 00 [55:27]: Claro, porque tampoco no puedo vender más que mi stock, o si no, cuando haga el movimiento de bodega te va a rebotar.

Carlos Vallejos [55:31]: Exacto.

sergio [55:32]: Ya, esa es otra pregunta. ¿Van a trabajar solamente con stock positivo? Porque hay casos que trabajan con stock negativo.

Speaker 01 [55:39]: Ya, ok, stock positivo. Así obligamos que tengan que tener todo el día.

sergio [55:44]: Ya, hay algunas empresas que trabajan como con stock en tránsito, que les va a llegar, que hagan la pega o el despacho.

Speaker 01 [55:55]: Sí, lo que pasa es que nosotros trabajamos con stock en tránsito, pero netamente en la bodega. Pero lo que es venta tiene que estar en stock real, ya, porque si no nos queda un enredo entre lo que tenía que llegar, lo que se vendió, lo que nunca llegó.

sergio [56:09]: Ya, mira, nosotros le vamos a hacer, preparar una propuesta de cómo sería el tema de selección del producto y seleccionar la bodega y poder sacar desde las bodegas disponibles que Ya, ok. Otra consulta: recargos a nivel de detalle, ¿no trabaja? Recargos a nivel de detalle, no. Y a nivel global, descuento, recargo a nivel global, no.

Speaker 01 [56:45]: Pero, ¿a qué te refieres con recargos de intereses?

sergio [56:50]: Claro, pues que el formato de la factura electrónica, por ejemplo, te permite a nivel de detalle, por ejemplo, tú tienes un precio, una cantidad, ¿cierto? Pero a esa línea de detalle yo le puedo agregar un recargo que, por ejemplo, puede ser el flete, ¿entiendes?

Speaker 00 [57:05]: Como un servicio flete, Marco.

Speaker 01 [57:06]: Ah, entiendo. Yo le habré que agregar una línea adicional nomás.

sergio [57:10]: Como una línea adicional, claro.

Speaker 01 [57:11]: Claro.

sergio [57:12]: Por eso lo preguntaba. ¿Qué más? Productos con impuestos adicionales no manejan.

Speaker 00 [57:19]: No, nosotros no.

Carlos Vallejos [57:34]: Consulta, ¿de casualidad de la parte de GoSocket les entregaron las credenciales de la API?

Speaker 01 [57:44]: No, tuvimos que cancelar la reunión que teníamos hoy y la reagendamos para el lunes.

Carlos Vallejos [57:49]: Perfecto. Sí, perfecto, porque la parte de la emisión de los documentos como tal la estábamos con la documentación que nos entregaron en esta prueba, ya la teníamos maqueteada. Pero al no tener las credenciales no pudimos realizar en el ambiente de pruebas. Entonces la misión de acá está con errores mientras no tengamos las credenciales.

Speaker 01 [58:20]: Ya el lunes tenemos la reunión de credenciales con Pablo y debería, que me dijo que debería quedar listo el mismo lunes.

sergio [58:27]: Perfecto.

Speaker 01 [58:29]: Y me estoy comunicando con Acepta para hacer el tema de la carga masiva, que nos manden los documentos. Lo habíamos hablado en reunión.

Carlos Vallejos [58:45]: Perfecto. Bueno, revisemos dentro de lo que resta del tiempo, que sería el tema del módulo de compás. Creo que nos falta irle contabilidad y tesorería. O no sé si es que por el tema del tiempo gustarían que agendáramos una reunión, porque igual con las correcciones que tenemos ya podríamos trabajar en la solicitud de asociar con el correo electrónico de Microsoft las bodegas. Podríamos ya tener un avance para la próxima reunión y revisar de pasada también lo que vendrían a ser los demás módulos ya con GoSocket integrado para poder realizar la muestra de la emisión de los documentos.

Speaker 01 [59:35]: Por mi lado, igual sería bueno que los chiquillos también se metieran a la página para ver si queremos hacer mejoras en los módulos siguientes.

Carlos Vallejos [59:42]: Sí, de hecho, como informé, el día de mañana esto va a quedar publicado y les vamos a ingresar con las mismas credenciales para que puedan explorar. También, bueno, está el modo demo con información cargada, pero en el servidor real todavía no hay información de prueba como en este. Vamos a tener sí cargado lo que vendría a ser las parametrizaciones, que esas sí las podemos realizar de carga para que ya puedan revisar en el sistema, y también la actualización de las tarjetas de tráiler con esta reforma que le hicimos en las últimas reuniones que falta.

Speaker 01 [01:00:14]: Carlos, consulta, si mañana queda publicada la página oficial de AlmaWeb, ¿nosotros ya podríamos empezar a ingresar información real?

Carlos Vallejos [01:00:22]: Pueden, pero la idea es que en esta primera instancia se genere sabiendo de que va a ser información de muestra todavía, pero estaría habilitado totalmente para que puedan ingresar datos reales.

Speaker 01 [01:00:35]: Claro, la idea es como ir viendo un proceso completo de una compra, un proceso completo de una venta, porque ahí también nos van a surgir a nosotros ideas o dudas de lo que estamos haciendo en el módulo. Sí, sí, entonces esa es la idea.

Carlos Vallejos [01:00:47]: Sí, sí, de hecho mañana, como te digo, teniendo, bueno, las credenciales de GoSocket, hasta que no las tengamos, el tema de la emisión Teníamos preparado un, por así decirlo entre comillas, documento de muestras para que lo pueda tener. Voy a ver si es que podemos dejar habilitado para que mientras no tengamos de GoSocket saque igual de todas formas con datos falsos, pero para que puedan por mientras utilizar el sistema, lo vayan revisando y todo el feedback que vayan teniendo de la revisión nos la vayan dando.

Speaker 00 [01:01:21]: Perfecto.

Speaker 01 [01:01:22]: Sí, podemos crear usuario y verlo. Los parámetros, todo eso.

sergio [01:01:28]: Genial. Carlos, no sé si lograste levantar para que puedan ver cómo la cotización, el diseño.

Carlos Vallejos [01:01:35]: Tenemos para solamente la muestra de la planilla. Lo que pasa es que como estábamos en este ambiente de desarrollo, crear el conector de GoSocket, Sergio, no está, no está disponible en este momento.

sergio [01:01:52]: La idea es que, como pueden ver acá, se pueda administrar usted el diseño de sus órdenes de compra. ¿Cómo?

Speaker 00 [01:02:01]: Sí, qué buena esa.

sergio [01:02:04]: La idea es que lo pueden ustedes diseñar y agregar información que necesiten.

Carlos Vallejos [01:02:11]: También adicional agregar de que va por cliente, así que cada modificación que haga se va cambiando cada uno de los clientes. Pueden modificarle los colores, el contenido. Y aquí pueden tener una preview de cómo quedaría este, en este caso, una cotización de demo con datos fantasmas.

Speaker 00 [01:02:28]: Perfecto, súper genial.

sergio [01:02:34]: Entonces, Mario, ¿para cuándo agenda la próxima reunión? ¿Este mismo día, misma hora, te parece?

Speaker 00 [01:02:44]: Yo creo que sí, una semana mismo horario, mismo lugar, ¿o no, María Jesús? Sí, vamos a dejar bloqueado este horario para esto.

Carlos Vallejos [01:02:56]: Perfecto, entonces ahí genero yo la reunión, Sergio.

Speaker 00 [01:03:02]: General Carlos, oye, muy buenas tardes.

sergio [01:03:09]: Eso, no sé qué les pareció el avance. Bueno, María Jesús, ha sido un trabajo bastante, Carla y María Jesús, constante, así que No sé qué les pareció a ustedes.

Speaker 00 [01:03:17]: Bueno, yo creo que llegaron a los balances. No habrán avanzado mucho.

Carlos Vallejos [01:03:27]: Qué bueno.

sergio [01:03:28]: Sí, sí, la verdad que hay otras pantallas que ya están también bien avanzadas, pero por tema de tiempo, vamos por parte, vamos por parte.

Speaker 00 [01:03:38]: Pero está quedando filete. Qué bueno, qué bueno que le guste. Lo que habíamos hablado de hacer, más o menos los próximos pasos, este, vamos a diseñar. Yo los dejo, muchachos, nos vemos.

Carlos Vallejos [01:03:49]: Que estén muy bien.

Speaker 00 [01:03:51]: Lo que habíamos hablado el otro día, el martes, vamos a diseñar antes de empezar la temporada, y ahí vamos a hacer las reuniones presenciales.

sergio [01:04:02]: Sí, ahí vamos a hacer la prueba de fuego. La idea es que nosotros ya cuando pasemos prácticamente todo el Y ya estemos listos para pasar a producción. Ese proceso vamos a estar allá con usted acompañando.

Speaker 00 [01:04:16]: Ya, súper.

sergio [01:04:19]: Ya pues, muchas gracias a todos por su tiempo. Gracias, Carlos, por la presentación. Gracias, María Jesús. Gracias, Mario.

Carlos Vallejos [01:04:25]: Gracias, chiquillos. Cuídense, que estén muy bien.

sergio [01:04:28]: Chao, chao.

Speaker 01 [01:04:36]: ¿Se fueron todos?

Carlos Vallejos [01:04:37]: Sí.

Speaker 01 [01:04:38]: Y entonces quedamos para el jueves.

Carlos Vallejos [01:04:41]: Sí, Mari, quedamos para el jueves. Yo creo que igual en la semanita te voy a estar molestando y para que hagamos quizá una mini review para mostrarte el inicio de sesión, ver si es que hay algún tipo de problema. No va a ser más de 5 o 10 minutos, y más que nada como una entrega formal de las credenciales con el nuevo diseño. Y ahí ya vendría, voy a terminar primero lo que es el sistema, te paso las credenciales y mañana voy a estar actualizando el Trello para que vayamos documentando ahí lo nuevo.

Speaker 01 [01:05:08]: Ya, oye Carlos, ¿podría ser esa reunión el lunes?

Carlos Vallejos [01:05:12]: Sí, sí, de hecho si gustas el mismo lunes como lo hicimos el otro día vamos coordinando porque no va a ser más de 5 minutos, Mari.

Speaker 01 [01:05:18]: Ya, ningún problema porque el martes no voy a estar presente ni en la oficina ni teletrabajo.

Carlos Vallejos [01:05:23]: Ah, te vamos a echar de menos, ¿para dónde vais?

Speaker 01 [01:05:25]: No, me tengo que operar.

Carlos Vallejos [01:05:27]: ¿En serio?

Speaker 01 [01:05:28]: Y de hecho, después de tener licencia, pero igual me voy a conectar a las reuniones.

Carlos Vallejos [01:05:32]: No, me vas a abandonar, Mari.

Speaker 01 [01:05:33]: No, no, sí, con el proyecto estamos full.

Carlos Vallejos [01:05:35]: Todas hacen lo mismo.

Speaker 01 [01:05:39]: No, Agustín, realmente no es lo mismo.

Carlos Vallejos [01:05:43]: Ya, mira, en ese caso, si tienes alguna preferencia de tiempo, cualquier cosita, o si va a dejar algún reemplazo, ningún problema, igual yo te puedo ir reportando.

Speaker 01 [01:05:52]: Prefiero que tengamos la reunión nosotros como para ver los avances y las credenciales. Ya. Y el jueves igual me voy a conectar a la reunión.

Carlos Vallejos [01:06:00]: Ya, ningún problema. Ya, pues, Mari, quedamos en eso entonces.

Speaker 01 [01:06:05]: Ya, Carlos, que estés bien.

Carlos Vallejos [01:06:07]: Cuídese, hasta luego.

Speaker 01 [01:06:08]: Igual, chao.
