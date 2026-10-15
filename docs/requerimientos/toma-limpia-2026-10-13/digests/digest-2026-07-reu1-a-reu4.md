# Digest Reu1 a Reu4 (21 al 30 de julio 2026)

Solo estas cuatro transcripciones. El as-is es Agrosoft / AlmaWeb, el sistema que el cliente muestra. El pedido es lo que quiere en el ERP nuevo.

Voces segun el propio archivo:

- Reu1 (`transcripcion.md`): Speaker 00 muestra Agrosoft en primera persona ("nosotros"). No dice su nombre. Speaker 01 responde corto. El archivo advierte que los relojes pueden estar corruptos; se citan igual, como aparecen.
- Reu2: Speaker 00 es Rodrigo (muestra contratistas y AgroSmart). Speaker 01 es Maria Jose / MJ (Carlos le dice Mari). Speaker 02 es Carlos.
- Reu3: el archivo rotula Speaker 00 = Carlos y Speaker 01 = Maria Jesus.
- Reu4: Speaker 00 = Carlos, Speaker 01 = Maria Jesus, Speaker 02 = Sergio. Sigrid esta en la sala por Mario y no tiene turnos rotulados. Agustin y Mario estan de vacaciones.

Si el texto no nombra a quien habla, Quien = no dicho.

---

## Admin

### ADM-01
- Enunciado: El cliente entra a Agrosoft con usuario y clave, y la sesion queda en la ultima empresa en la que trabajo. Desde ahi cambia de empresa y ve solo las empresas a las que tiene acceso.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [00:40]
- Cita: "al ingresar siempre nos queda en la ultima empresa que trabajamos, pero aca nosotros podemos hacer cambio de empresa."

### ADM-02
- Enunciado: El cliente puede cambiar temporada en la pagina de inicio, pero ese cambio no les sirve porque no usan el modulo de gestion. El sistema nuevo debe implementarlo igual.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [00:40]
- Cita: "el cambio de temporada en esta pagina no sirve mucho porque nosotros no usamos el modulo de gestion. Pero igual seria bueno implementarlo en el ERP nuevo."

### ADM-03
- Enunciado: Al cambiar de empresa el cliente elige el mes contable y el mes de remuneracion, acepta, y entra al modulo de AlmaWeb.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [00:40]
- Cita: "veo los meses que, en el mes que quiero trabajar, mes contable y de remuneracion, y pongo aceptar."

### ADM-04
- Enunciado: Hoy tienen 15 usuarios y cada usuario extra se cobra aparte. A veces dos personas comparten un usuario. La ultima sesion pisa la empresa y la otra persona sigue digitando en una empresa distinta.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [00:40]
- Cita: "hay veces en que un usuario lo ocupan 2 personas... le permite seguir ingresando informacion en una empresa diferente."

### ADM-05
- Enunciado: La sesion se cierra sola cada cierto tiempo. Si a una persona se le cerro y la otra sigue activa, a la primera le aparece que esta trabajando en otra empresa.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [27:40]
- Cita: "igual cada cierto tiempo se te cierra la sesion automatica, y pasa eso de que se le cierra la sesion y yo la tengo activa."

### ADM-06
- Enunciado: El proveedor solo tenia perfiles administrador y digitador. Al pedir un perfil intermedio, el cambio se aplico a todos los digitadores y se abrieron pestañas de borrar y modificar a quien no debia.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:58:21]
- Cita: "Cuando pedimos el cambio de perfil, ellos cambiaron el perfil, pero tambien cambiaron todos los perfiles de los digitadores."

### ADM-07
- Enunciado: La jefatura debe poder parametrizar. El administrativo no. El digitador ingresa datos y saca informes. Quien administra crea, elimina, modifica y cierra el mes, y con eso impide seguir digitando el mes cerrado.
- Modulo: admin
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:58:21] y [02:51:40]
- Cita: "la jefatura tienen permiso para tener el modulo de parametrizacion, pero no los administrativos."

### ADM-08
- Enunciado: El ERP debe dejar armar roles eligiendo pantallas, con lectura y escritura por separado, y no quedarse en el par rigido digitador / administrador.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [09:57:20]
- Cita: "podemos poner, por ejemplo, pinchar lo que quiere el usuario y no como que es que tan rigido como usuario digitador, usuario administrador."

### ADM-09
- Enunciado: Hoy hay 3 roles definidos y algunos mixtos. La digitadora de contratistas ve solo su modulo y solo sus empresas (en el ejemplo, solo Santa Pilar). La analista ve mas modulos, sin parametrizacion ni gestion, y el cierre de mes lo hace Maria Jose. En insumos el digitador mueve bodega y saca informes, no parametriza.
- Modulo: admin
- Clase: as-is
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [10:38:11], [12:56:00] y [13:08:01]
- Cita: "ella es digitadora, pero al final es solo de ese modulo."

### ADM-10
- Enunciado: Hay usuarios por empresa. Al crear un usuario hay que marcar a que empresas entra. Una persona puede entrar a una o a varias.
- Modulo: admin
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [02:32:01] y [02:33:21]
- Cita: "Yo creo que la creacion de usuario igual vamos a tener que seleccionar a que empresa pueden entrar."

### ADM-11
- Enunciado: En la revision de un movimiento debe verse el nombre de la persona que lo hizo, no el cargo ni el rol.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [01:01:00]
- Cita: "preferimos que aparezca el nombre de la persona que esta haciendo el trabajo, porque asi despues cuando revisamos sabemos quien hizo el movimiento."

### ADM-12
- Enunciado: Quedo dicho por el equipo que cada usuario tiene un solo rol. Si necesita permisos de dos perfiles, se crea un rol nuevo con esa mezcla. El cambio de rol se hace en el usuario.
- Modulo: admin
- Clase: decision
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion3.md, Speaker 00 [01:20:51]
- Cita: "el sistema actualmente esta hecho para que no te deje tener 2 roles, sino que en caso de que sea necesario se crea un rol con los permisos."

### ADM-13
- Enunciado: Hoy cada persona cambia su propia clave. Maria Jesus dice que estaria bien si el administrador pudiera ver la clave de otro. Carlos propone no mostrarla y solo dejar una clave temporal. No queda cerrado.
- Modulo: admin
- Clase: duda
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [01:50:11]
- Cita: "actualmente cada uno cambia su clave, pero si el administrador tiene permiso para visualizar la clave de otro usuario, Perfecto."

### ADM-14
- Enunciado: Todo lo que se crea o modifica (centro de costo, plan de cuentas, elemento de costo, tipo de documento, tipo de referencia, codigo financiero, indicadores, factores) debe vivir en parametrizacion. Quien no tenga ese acceso no ve esa pantalla, aunque tenga el modulo operativo.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [02:50:30] y [02:56:31]; transcripcion-reunion4.md, Speaker 01 [08:34:00]
- Cita: "yo lo que esta en catalogo yo lo dejaria todo lo que es creacion y modificacion ahi."

### ADM-15
- Enunciado: Cada usuario puede mostrar u ocultar columnas de una lista, y ese orden se guarda para el en otra sesion u otro computador. No cambia la vista de los demas ni los datos de la empresa.
- Modulo: admin
- Clase: ui
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion3.md, Speaker 00 [02:11:31]
- Cita: "cada usuario va a poder mostrar u ocultar columnas... no te va a afectar a la vista de otro usuario."

### ADM-16
- Enunciado: Al cambiar de empresa el sistema pregunta desde que periodo se mira, y el menu debe mostrar la empresa activa y el periodo.
- Modulo: admin
- Clase: ui
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion3.md, Speaker 00 [02:25:50]
- Cita: "cuando uno hace el cambio de empresa tambien te pregunta directamente desde que periodo quieres verlo."

### ADM-17
- Enunciado: Los indicadores se toman del Banco Central, no del SII, porque el Banco Central actualiza mas temprano. A las 9 de la manana ya estan. El cliente quiere dolar, euro y yuan como monedas principales, y poder agregar otra moneda despues. UF, UTM e IPC no los usan en la reporteria.
- Modulo: admin
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [17:46:00]
- Cita: "seria importante que claro aqui fuera dolar, euro y yuan... que nosotros vayamos seleccionando la moneda."

### ADM-18
- Enunciado: Domingo y feriado el Banco Central no trae tipo de cambio, y el cliente lo digita a mano. Si lo digita, solo queda el dolar; el resto hay que ponerlo tambien a mano. Si falta el tipo de cambio, hoy el sistema deja contabilizar en pesos y la reporteria en dolares sale mal.
- Modulo: admin
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [18:49:40]
- Cita: "los dias domingo y los feriados no me trae el tipo de cambio. Entonces, por ejemplo, estos dias yo lo tengo que digitar manual."

### ADM-19
- Enunciado: En parametros generales crean empresas, especie, variedad, fondos (campos), tipo de terreno, centros de costo y ubicacion. Fondos y ubicacion casi no impactan; el tipo de terreno si importa para el agricola. La ubicacion se pide al crear proveedores. El centro de costo se crea, se modifica y se le cambia la vigencia.
- Modulo: admin
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [17:46:00]
- Cita: "El tipo de terreno si importa porque para el area agricola, los centros de costo que los podemos aca cambiar vigencia."

### ADM-20
- Enunciado: Si se elimina un rol que todavia tiene usuarios, el sistema debe pedir a que rol quedan. Debe poder existir un rol temporal (ejemplo: vacaciones) y volver a asignar el rol anterior al eliminarlo.
- Modulo: admin
- Clase: ui
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion4.md, Speaker 00 [27:20]
- Cita: "cuando uno va a eliminar un rol, y si es que existe un usuario dentro de ese rol, cuando uno lo elimina te dice que rol quieres dejarle."

### ADM-21
- Enunciado: Cada empresa debe poder subir su logo a los documentos impresos, definir pie de pagina y columnas. Si no hay imagen, se usa el nombre de la empresa.
- Modulo: admin
- Clase: ui
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [44:09]
- Cita: "Pero por ejemplo, se puede subir la imagen?"

### ADM-22
- Enunciado: Los listados se trabajan en Excel. El PDF sirve de complemento. En Agrosoft tambien existia Word y PowerPoint, pero Excel es el formato que usan.
- Modulo: admin
- Clase: ui
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [15:19:10]; transcripcion-reunion4.md, Speaker 01 [15:06:10]
- Cita: "Para nosotros Excel es sagrado."

---

## Contratistas

### CTR-01
- Enunciado: Hoy no usan el modulo de mano de obra (liquidan con Book). Ahi se parametrizan labor, actividad, horario y prevision. Como el ERP nuevo no tendra mano de obra, actividad y labor deben parametrizarse en contratistas. A futuro el trabajo de campo sera contratista, no mano de obra propia.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [39:50] y [04:33:01]
- Cita: "como nosotros no vamos a tener el de mano de obra, lo queremos parametrizar en lo que es en el modulo de contratista."

### CTR-02
- Enunciado: Al ingresar tarifas, la linea anterior desaparece. No hay listado para revisar si quedo grabada o si hay error. La busqueda existe solo como informe, no para agregar o modificar tarifas del mismo tarifario. Para otra labor hay que limpiar y cargar de nuevo.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [39:50] y [01:46:11]
- Cita: "me deja agregar la otra, pero se me desaparece la primera... no hay un listado, entonces no me permite revisar si tengo algun error."

### CTR-03
- Enunciado: Primero se enrola al contratista (historial, agregar, y pasar de vigente a no vigente para que deje de aparecer). Despues se carga la tarifa: ano, mes, codigo y contratista.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:07:10]
- Cita: "aqui yo tengo la opcion de evitarlo, agregar o cambiar vigencia, de que quede de vigente a no vigente."

### CTR-04
- Enunciado: La labor va anexada a una actividad. La actividad se usa general y la labor especifica (ejemplo: actividad armado de caja, labor packing cereza). Deben poder anexar otra labor a una actividad, y esa parametrizacion tiene que verse en contratistas.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:13:01]
- Cita: "generalmente aca tratamos de que la actividad sea como general y la labor sea mas especifica."

### CTR-05
- Enunciado: La tarifa lleva unidad de control (como se mide; en campo), fechas desde-hasta, centro de costo y valor negociado. La unidad de control se puede crear en la misma pantalla.
- Modulo: contratistas
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:20:41]
- Cita: "Unidad de control, aca yo puedo poner por como lo voy a medir... centro de costo, a que lo voy a anexar, y la tarifa."

### CTR-06
- Enunciado: El ERP que estan armando es de la exportadora y de la empresa de servicio, pero el partner agricola tambien lo usara. El modulo de contratistas debe quedar mas especifico para el area agricola que para la industrial.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [01:20:41]
- Cita: "este modulo igual va a tener que quedar como mas especifico para lo que es el area agricola que para lo que es el area industrial."

### CTR-07
- Enunciado: Al centralizar, el cliente define las cuentas. Se reconoce el costo del trabajo contra facturas por recibir contratistas. Cuando llega la factura, se ingresa esa cuenta contra el contratista y queda amarrada a la proforma.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [02:51:40]
- Cita: "se me va a reconocer una subcuenta que es facturas por recibir contratistas... y ahi me queda anexada... la orden de compra con la factura."

### CTR-08
- Enunciado: Hoy "emitir factura" deja una sola factura por contrato y no cierra el modulo hasta asociar todos. En ALM hay pocos contratistas y, ya asociados, desaparecen de la pantalla. Para revisar hay que sacar el informe del mes.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [02:51:40]
- Cita: "cada contrato tenga anexado solamente una factura, y no te deja cerrar el modulo hasta que todos los contratos estan asociados a un documento."

### CTR-09
- Enunciado: En borrador se puede corregir, por ejemplo el contratista. En definitiva no se puede modificar: hay que reversar. El cliente dice que igual hay errores despues de dejarla definitiva.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [02:51:40]
- Cita: "si yo pongo borrador me deja modificar... Pero si yo pongo definitiva, no me deja modificarlo."

### CTR-10
- Enunciado: El traspaso contable pide la tasa de cambio, arma el asiento del mes y lo manda a contabilidad. En contratistas el proceso queda cerrado; en contabilidad sigue abierto como factura por recibir hasta ingresar la factura. El cierre de mes lo hace el administrador y bloquea al digitador.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [02:51:40]
- Cita: "en el modulo de contratista como que queda cerrado el proceso. Pero queda abierto en el modulo de contabilidad."

### CTR-11
- Enunciado: El proceso actual repite datos: tarifario por centro de costo, luego contrato (estado activo, tipo mano de obra, fechas, faena que siempre es agricola), folio que hay que anotar, enrolamiento (nombre, fecha, jefe de cuadrilla) y recien ahi el control de produccion diario. Si el tarifario esta mal, se vuelve al inicio.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [01:00:00] a [01:06:51]
- Cita: "armar el tarifario, por lo menos para nosotros, como un paso de mas. Se nos hace mas facil como colocarlo dentro del mismo proceso."

### CTR-12
- Enunciado: En el control diario el precio sale del tarifario y no se puede cambiar. Muchas veces el precio se acuerda cuando el trabajo ya termino, y un trabajo puede durar un mes. Por eso no les sirve para asistencia ni control diario.
- Modulo: contratistas
- Clase: as-is
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [01:45:51]
- Cita: "terminan de hacer los trabajos y despues de que terminan de hacer los trabajos muchas veces se da el precio."

### CTR-13
- Enunciado: Al elegir una labor deben listarse solo las actividades asociadas. Hoy hay que saberse de memoria la actividad, porque el sistema pide la labor y despues todas las actividades.
- Modulo: contratistas
- Clase: pedido
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion2.md, Speaker 02 [01:44:51]
- Cita: "Seria mucho mas practico que aparezcan las asociadas solamente."

### CTR-14
- Enunciado: La proforma se manda al contratista para que facture. Muestra faena, cantidad, precio, neto, IVA y total. Debe verse primero el borrador y despues confirmar la definitiva. Hoy la definitiva emite el folio sin un paso de revision.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [02:11:51] y Speaker 02 [02:04:21]
- Cita: "si uno pone el definitivo, si o si se va a emitir como todo el proceso, como que no hay ningun filtro."

### CTR-15
- Enunciado: Una factura puede juntar varias proformas, incluso de dos meses (fin de un mes y principio del otro). Agrosoft deja una proforma por mes y no permite asociar las dos. Hoy cargan todo en un solo mes y llevan el otro registro aparte, asi que el costo mensual no refleja el mes real.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [02:37:50]
- Cita: "se juntan 2 meses... necesitamos hacer dos proformas distintas para esa factura. Pero si hacemos las dos proformas, no nos deja asociarlas."

### CTR-16
- Enunciado: AgroSmart les gustaba para el dia a dia (tarifario diario editable, varias labores, asociar las que correspondan a una factura hasta calzar el monto) pero duplicaba registros y descuadraba la centralizacion. Se quedan en Agrosoft por la contabilidad. Del otro sistema quieren la operatoria simple, no su contabilidad.
- Modulo: contratistas
- Clase: decision
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [03:55:51] y [04:01:31]
- Cita: "nos duplicaba registros, nos daba unas centralizaciones super descuadradas, asi que no confiamos en el sistema y nos mantuvimos en AgroSoft."

### CTR-17
- Enunciado: El asiento de cierre suma las proformas del mes: facturas de contratistas por recibir (con proforma y RUT) contra costo de mano de obra contratista, o contra la cuenta que elijan.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [03:03:10]
- Cita: "se arma siempre de todo contra mano de obra contratista, contra la suma de todas las proformas que esten dentro del mes."

### CTR-18
- Enunciado: Quieren anotar las labores del dia (fecha, cuartel, faena, trato o jornada, unidad como kilo, bin o capacho, valor) y despues armar la proforma marcando esas lineas. La duracion en horas casi no les importa; si la usan, ponen 8.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Rodrigo
- Fuente: transcripcion-reunion2.md, Speaker 00 [03:51:00]
- Cita: "despues de haber anotado todas las labores diarias, yo poder ver todas las labores que tengo anotadas y decir ya, esta, esta, esta, hago una proforma."

### CTR-19
- Enunciado: Editar una proforma o un trabajo diario debe pedir autorizacion de un supervisor. Si ya estaba autorizada y se edita, debe autorizarla de nuevo la misma persona. Debe quedar el nombre de quien aprobo.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [03:37:00] y [03:45:40]
- Cita: "despues esa proforma hay que editarla. Al editarla, igual pedira una autorizacion de la persona que autorizo."

### CTR-20
- Enunciado: Deben poder marcar 3 o 4 proformas y asociarlas a una misma factura, filtrar pendientes y facturadas, y ordenar columnas.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [03:54:41] y [04:08:10]
- Cita: "uno pudiera pinchar varias proformas y poder facturarlas. Por ejemplo, que 3 o 4 proformas pertenezcan a una factura."

### CTR-21
- Enunciado: El traspaso no se hace contratista por contratista. La pantalla pide el mes a cerrar y el tipo de cambio, centraliza, y el sistema reconoce costo contra facturas por recibir contratistas.
- Modulo: contratistas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [04:26:30] y [04:28:21]
- Cita: "aqui solamente se centraliza la informacion, no se hace por contratista."

### CTR-22
- Enunciado: En AlmaWeb solo deben ofrecerse los centros de costo de AlmaWeb. Hoy cada empresa tiene los suyos con apellido (Administracion AlmaWeb, ALM, Santa Pilar, Los Palos). Los que parten con 1 son ALM, con 2 Almahue, con 3 Santa Pilar. Lo piden mas rigido para no imputar mal.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [01:05:09] y [01:14:39]
- Cita: "la idea es como que sea mas rigido que lo que tenemos actualmente para evitar el error de imputacion."

### CTR-23
- Enunciado: El centro de costo queda amarrado a la empresa activa. El mismo codigo (ejemplo 10100) puede repetirse en otra empresa sin agregar apellido. Sergio dice que la columna empresa en esa pantalla no hace falta.
- Modulo: contratistas
- Clase: decision
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-reunion4.md, Speaker 02 [01:38:20]
- Cita: "ese codigo, tu lo puedes utilizar en AlmaWeb o en la otra, la n empresa que tu tengas."

### CTR-24
- Enunciado: Una proforma aprobada no se edita ni se elimina: solo se asocia a la factura. Para reversar la aprobacion piden clave, como hoy, y esa opcion no le aparece al analista. Sergio propone que cada supervisor tenga su propia clave, no una clave compartida. Maria Jesus pide separar editar de modificar.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [02:36:29] y [02:59:10]
- Cita: "si esta aprobada deberia quedar solamente para asociar a la factura y en caso de poder reversar la aprobacion."

### CTR-25
- Enunciado: Al entrar debe verse que hay aprobaciones pendientes (icono o contador). No quieren un correo por cada orden, porque seria tedioso. La notificacion que se marca leida al hacer clic no reemplaza ese pendiente.
- Modulo: contratistas
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [07:12:41]
- Cita: "quizas no mucho el correo... pero si al momento de meterme a la pagina y que me aparezca como un pendientes."

### CTR-26
- Enunciado: Las reglas de aprobacion definen que modulo se aprueba y que personas aprueban (proformas y ordenes de compra). Si alguien aprueba en reemplazo de otro, debe salir una advertencia y quedar evidencia.
- Modulo: contratistas
- Clase: ui
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion4.md, Speaker 00 [44:29]
- Cita: "Mostrandole una advertencia de que esta aprobando a nombre de otra persona, si desea continuar. Y tambien va a quedar evidencia."

---

## Compras

### COM-01
- Enunciado: No usan solicitud de compra. Van directo a la orden y marcan "sin solicitud". En el ERP nuevo esa solicitud no deberia estar.
- Modulo: compras
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "nosotros nos vamos directo a realizar la orden de compra... como que esto no deberia ir."

### COM-02
- Enunciado: La orden lleva departamento (hoy son 2; la hace el administrativo), solicitante, fecha, jefe que aprueba (en el ejemplo, Juan Agustin), proveedor, plazo (contado, 15 o 30 dias), moneda (casi siempre pesos, tambien dolar) y observacion.
- Modulo: compras
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "seleccionamos el departamento... el jefe es la persona que me lo va a aprobar. A Juan Agustin."

### COM-03
- Enunciado: El tipo de cambio que muestra la orden al crearla no es el del gasto. El gasto toma el tipo de cambio de la fecha en que se recepciona.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "este tipo de cambio que me arroja despues no me lo reconoce... Se registra a la fecha en que yo recepciono la orden de compra."

### COM-04
- Enunciado: La imputacion puede ser por hectarea, por grupo de centros de costo o directa. La directa es la que usan: centro de costo, elemento de costo y monto. La hectarea la quieren usar, pero hoy es todo o nada: no pueden sacar un cuartel. Quieren ir agregando y distribuir.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "si yo quisiera por hectarea y quiero que solo un cuartel no este dentro de esa hectarea, no me deja editarlo."

### COM-05
- Enunciado: Estando en ALM, la orden deja elegir centro de costo y elemento de costo de otra empresa (Almahue, Santa Pilar). Eso es un error del sistema viejo.
- Modulo: compras
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "yo estoy en Alem, pero yo podria poner Almaue, por ejemplo, o Santa Pilar y me deja."

### COM-06
- Enunciado: Si la distribucion no cuadra con el neto, la alerta sale al final y hay que rehacer todo. Si hay varias lineas, no dice cual esta descuadrada. El cliente quiere el aviso al momento de agregar.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [05:56:50]
- Cita: "me dejo agregarlo por 1000, pero yo habia puesto 1010 y no me da una advertencia de que no esta cuadrado."

### COM-07
- Enunciado: La linea de la orden se marca con IVA o exenta, y eso condiciona el documento que despues se asocia. Tambien hay facturas mixtas (afecto mas exento) y combustible con impuesto especifico. El cliente plantea dos caminos y no cierra: o la orden no marca afecto/exento porque solo reconoce el neto, o una orden exenta no debe aceptar una factura afecta. Dejarlo rigido les impediria cargar esas facturas. Hoy suman neto y exento en la orden para entrar el costo.
- Modulo: compras
- Clase: duda
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [09:56:51]
- Cita: "habrian dos soluciones: o la orden de compra en realidad no se pone si afecto, exento... O aca... no me deberia poner dejar un documento afecto."

### COM-08
- Enunciado: Al crear la orden deberia abrirse el PDF. El creador la ve en su lista; otro usuario no ve la que creo un tercero. El informe obliga a elegir un estado (anulada, aprobada, cerrada, contabilizada, pendiente, recepcion parcial o total). Por numero aparece en cualquier estado. Por proveedor solo salen las contabilizadas, de la mas antigua a la mas nueva.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [07:12:41]
- Cita: "si yo aca pongo el numero, me aparece directa independiente de si esta contabilizada, pendiente, anulada."

### COM-09
- Enunciado: A veces la factura llega antes que la orden. En la observacion escriben el numero de factura. No tienen un informe que diga en que orden esta la factura de un proveedor. Cuando la orden ya esta contabilizada, el informe deberia decir el proveedor.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [07:12:41]
- Cita: "se emite la factura y despues creamos la orden de compra, nosotros en la observacion ponemos factura tanto."

### COM-10
- Enunciado: Hoy contabilidad crea las ordenes. Lo ideal es que cada departamento cree las suyas. Los pasos de aprobacion y de recepcion se mantienen.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [07:12:41]
- Cita: "lo ideal es que despues cada departamento se encargue de su creacion de orden de compra... los pasos sigan iguales de aprobacion y recepcion."

### COM-11
- Enunciado: La aprobacion muestra solo las ordenes asignadas a ese jefe. Puede aprobar o rechazar. Quien la emitio no ve aprobar, recepcionar, cerrar ni anular: solo informes. Esos pasos son de quien tiene permiso de aprobar y anular. El estado se consulta buscando la orden.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [08:18:31]
- Cita: "Estos 3 modulos quedarian solamente para las personas que tienen acceso a aprobar y y anular."

### COM-12
- Enunciado: Recepcionar es poner la fecha y reconocer el gasto a esa fecha. Con productores el tipo de cambio es promedio y no hay un dia exacto del costo de la fruta. En tesoreria el pago usa el tipo de cambio negociado, manual. Por eso el costo y el pago no coinciden. Quien recepciona a veces pone el dia del movimiento; otros ponen la fecha que quieren.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [08:18:31]
- Cita: "como trabajamos con productores, a veces el tipo de cambio es promedio. Entonces no existe una fecha exacta."

### COM-13
- Enunciado: Al recepcionar un servicio, el asiento es la cuenta de gasto (en el ejemplo, mantencion y reparacion) contra facturas por recibir servicios. El gasto ya quedo reconocido y la factura sigue pendiente. El asiento se ve en pesos y en dolares.
- Modulo: compras
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [08:51:50]
- Cita: "Mantencion y reparacion de activos en la cuenta del gasto contra facturas por recibir servicios."

### COM-14
- Enunciado: La factura de compra se ingresa en proveedores, registro de compra, eligiendo el tipo (existencia, activo fijo o servicio) para ver las ordenes listas. Si el monto coincide, el sistema dejo contabilizar la orden contra otro proveedor. El tipo de cambio de la factura se puede cambiar y solo mueve el lado del proveedor, no el costo. El cliente quiere cambiar el tipo de cambio en la recepcion, no en este registro. La cantidad de la orden no aparece; si el monto y el tipo de cambio. La glosa es obligatoria.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [09:06:20]
- Cita: "quizas dejarlo como mas rigido y no dejar modificar aca, sino tener que modificar directamente en la recepcion."

### COM-15
- Enunciado: La orden solo aparece para facturar si esta aprobada y recepcionada, sea insumo o servicio. Si esta solo aprobada, no aparece.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [10:54:01]
- Cita: "Siempre que la orden de compra este aprobada y recepcionada... me va a aparecer el registro de compra. Si esta solamente en estado aprobada, no me aparece."

### COM-16
- Enunciado: En la orden deben verse la cuenta contable, el centro de costo y el elemento de costo, porque ahi se imputa el costo. Tambien el neto y, si corresponde, el impuesto.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [05:40:40] y [05:47:31]
- Cita: "ahi falta la cuenta contable y el centro de costo... Adicionar el elemento de costo tambien."

### COM-17
- Enunciado: En el libro de compras, al ver una factura deben listarse las ordenes del mismo RUT, ya aprobadas y recepcionadas, para ir asociando. Borrador, anulada y emitida no son facturas. La carga de un Excel del SII (o de un tramo de fechas) no debe duplicar lo ya cargado: primero mostrar duplicados y recien ahi confirmar.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [06:10:51] y [06:47:40]; transcripcion-reunion4.md, Speaker 01 [03:26:29]
- Cita: "ver si ese proveedor tiene ordenes de compra asociada, y con eso ir seleccionando la orden de compra."

### COM-18
- Enunciado: El nombre "libro comercial" les significa libro de compras. En ventas la pantalla debe llamarse libro de ventas. La carga masiva aplica a los dos libros.
- Modulo: compras
- Clase: ui
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [06:22:20]
- Cita: "el libro comercial yo le pondria el libro de venta, porque para nosotros el libro comercial es el de compra."

### COM-19
- Enunciado: Hoy no trabajan con cotizaciones: el encargado compra y despues se aprueba lo comprado. Quieren implementarlas, del tipo de pedir varias cotizaciones y elegir. Mientras no este el flujo, dejar el registro, y si siguen como hoy, la cotizacion la da la jefatura y se aprueba.
- Modulo: compras
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [06:56:50]
- Cita: "actualmente no trabajamos con cotizaciones, pero lo ideal es implementarlo."

### COM-20
- Enunciado: Aprobar la orden lo hace el jefe del departamento que pidio el servicio o la existencia. Recepcionar lo hace contabilidad cuando el servicio se efectua, y puede ser el mismo mes o uno o dos meses despues. Ahi se reconoce el gasto.
- Modulo: compras
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [03:32:40]
- Cita: "la aprobacion la hace el jefe del departamento... Y la recepcion la hacemos nosotros en el momento que el servicio se efectua."

---

## Inventario

### INV-01
- Enunciado: El maestro de articulos esta duplicado entre compras e insumos. Ellos crean el insumo en insumos. Si lo crean de nuevo con la misma familia, subfamilia, nombre y unidad, el sistema no avisa y el stock del mayor queda partido. El sistema debe avisar que el articulo ya existe.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [04:54:20]
- Cita: "puse exactamente los mismos datos y aun asi me dejo crearlo. Entonces lo puedo crear 20 veces."

### INV-02
- Enunciado: Quieren que insumos reciba materiales de bodega y agroquimicos, no servicios. Los activos fijos hoy se crean en "otro articulo". El maestro de compras les mezcla servicio, material y existencia. Prefieren que el maestro quede en insumos: la orden administrativa es para servicios; material y agroquimico van por insumos.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [04:54:20] y [10:54:01]
- Cita: "si me hiciera una distincion entre que el sistema de insumos yo pueda ingresar solamente materiales de bodega o materiales agroquimicos, genial."

### INV-03
- Enunciado: En insumos usan maestro, bodegas y (poco) nivel de almacenamiento. El nivel seria la ubicacion interna, y en el sistema viejo son 3 niveles. No lo tienen parametrizado. En la reu2 queda que por ahora no hay necesidad. Falta confirmarlo con la persona de materiales.
- Modulo: inventario
- Clase: duda
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion.md, Speaker 00 [11:17:10]; transcripcion-reunion2.md, Speaker 01 [12:44:20]
- Cita: "nosotros no tenemos ningun nivel parametrizado porque en realidad no lo usamos."

### INV-04
- Enunciado: Ingrediente activo y unidad de medida no los usa la exportadora, porque no aplican desde este modulo. Para el area agricola si serian utiles, para las aplicaciones.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [10:54:01]
- Cita: "para lo que es el area agricola Seria bueno que tuviera los ingredientes activos y la unidad de medida."

### INV-05
- Enunciado: Al estar en una empresa, las bodegas que se crean y se ven deben ser solo de esa empresa. Hoy, en LM, aparecen bodegas de otra empresa y se puede crear una bodega que despues se ve en la otra.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [11:17:10]
- Cita: "si yo estoy en LM, deberia ser si o si solamente LM, porque puede pasar que yo por error ponga el MAWE."

### INV-06
- Enunciado: Cada tipo de movimiento de bodega se parametriza con familia, subfamilia, cuenta al debe y cuenta al haber. Ejemplo: la entrada de separadores va a existencia; el consumo va a costo de materiales de embalaje. Hay partidas complementarias que se agregan solas. El cliente se comprometio a pasar la cuenta de cada tipo de movimiento. Al cerrar el mes de bodega, eso se contabiliza.
- Modulo: inventario
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [12:17:30]
- Cita: "cuando entre a bodega los separadores se me van a ir a la cuenta, por ejemplo, existencia... el consumo, se me va a ir a la cuenta costo."

### INV-07
- Enunciado: La entrada por compra elige la orden y el tipo "entrada desde proveedor". Muestra saldo y total (ejemplo: compro 800 y lleva 398, por eso esta parcial). El proveedor sale de la orden. Se elige bodega, observacion, tipo de cambio de compra, articulo y cantidad. Tambien hay traspaso entre bodegas y devolucion, cambiando el tipo de movimiento.
- Modulo: inventario
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [12:17:30]
- Cita: "El saldo lo aclara lo que yo ya ingrese... yo compre 800 pero llevo ingresadas 398."

### INV-08
- Enunciado: La bodega valoriza a precio promedio. Si una nota de credito es por cantidad de una factura puntual, el sistema saca las unidades al promedio y no al precio de esa factura, y no deja elegir ni modificar. Eso descuadra la contabilidad. El cliente iba a traer un ejemplo.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [13:32:20]
- Cita: "No me deja sacar esa cantidad por el precio de la factura, me la saca de bodega a precio promedio."

### INV-09
- Enunciado: El maestro de articulos es la creacion: no llevan ahi el stock ni el costo promedio. Al crear el articulo (ejemplo bolsas) deben elegir la cuenta del consumo, para que la centralizacion de bodega sepa a donde va.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [07:10:40] y [07:17:01]
- Cita: "El stock no es necesario porque el maestro de articulo es la creacion. Ni el costo promedio."

### INV-10
- Enunciado: La devolucion a proveedor se identifica por el tipo de movimiento "salida proveedor". Debe poder salir con un tipo de cambio especifico, sin mover el precio promedio del resto de la bodega. Maria Jesus iba a mandar la lista de estados de movimiento.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [07:37:40] y [07:47:20]
- Cita: "la devolucion nosotros la identificamos por el tipo movimiento porque es salida proveedor."

### INV-11
- Enunciado: En movimientos debe poder elegirse la bodega, no solo buscar por el movimiento. Los despachos y las guias viven en bodega. El libro de ventas es el documento, no el despacho. Si emiten guia.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [07:31:10]; transcripcion-reunion4.md, Speaker 01 [03:47:49] y [03:52:10]
- Cita: "los despachos, deberian quedar solamente en el movimiento de bodega."

### INV-12
- Enunciado: ALM tiene el stock de materiales (compras, devoluciones, traspasos). AlmaWeb no mueve bodega: solo registra la factura de compra y la de venta. El stock de fruta esta en la pagina de packing, no en Agrosoft, y no esta decidido si eso se trae al ERP.
- Modulo: inventario
- Clase: as-is
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [08:15:29] y [12:48:19]
- Cita: "en AlmaWeb solamente ingresamos la factura como compra y venta."

### INV-13
- Enunciado: Las cajas de AlmaWeb no tienen stock de un mes a otro: es bodega de paso (vendo 100 y compre 100). El SII, para la devolucion de IVA exportador, pide con que factura se compro y que cantidad. Al cierre, ALM factura a AlmaWeb la cantidad real del mes y el stock queda en ALM. Piden cargar por Excel el seguimiento de cajas que hoy llevan en la pagina de AlmaWeb.
- Modulo: inventario
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [07:55:59] y [08:20:49]
- Cita: "no contamos un inventario fisico, un stock fisico. El inventario es como yo vendo 100 y compre 100."

### INV-14
- Enunciado: Sergio propone marcar el producto como inventariable o no, y que el ingreso de un inventariable suba stock, por si mas adelante mueven existencias. Maria Jesus no lo confirma: responde con la carga Excel de cajas.
- Modulo: inventario
- Clase: duda
- Voz: equipo
- Quien: Sergio
- Fuente: transcripcion-reunion4.md, Speaker 02 [08:17:09]
- Cita: "La idea es que los productos los marquen como inventariable o no, cierto?"

---

## Contabilidad

### CON-01
- Enunciado: Contabilidad centraliza contabilidad, proveedores, ventas, tesoreria y activos fijos. El plan de cuentas se agrega, modifica y elimina. Por cuenta se define si pide centro de costo, area de negocio, especie, variedad o elemento de costo. Si se marca no imputable, nadie la usa.
- Modulo: contabilidad
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [14:30:00]
- Cita: "si no quiero que la utilicen, pongo no imputable y pongo guardar. Entonces nadie puede utilizar esa cuenta."

### CON-02
- Enunciado: Con el plan armado, parametrizan que cuentas se ven en el estado de resultados y en el estado de situacion financiera.
- Modulo: contabilidad
- Clase: as-is
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [14:38:00]
- Cita: "podemos parametrizar lo que queremos visualizar en el estado de resultados y en el estado de situacion financiera."

### CON-03
- Enunciado: Existen auxiliares (personal, instituciones de prevision), tipos de referencia del libro de compras (ellos crearon el 31; codigo, descripcion, y si lleva impuesto especifico o exento), area de negocio y elemento de costo. Los tipos de comprobante a replicar son apertura, egreso, ingreso, proveedores, traspaso y venta. En el dia a dia usan ingreso, egreso y traspaso; proveedor y venta se hacen en su modulo.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [14:56:00] y [16:23:01]
- Cita: "Los tipos de comprobante, si es de apertura, si es de egreso, ingreso, proveedores, traspaso y venta. Aca seria replicar solamente."

### CON-04
- Enunciado: Hoy mezclan articulo, centro de costo y elemento de costo con libertad, y el mismo concepto cambia de elemento segun quien responde. Quieren amarrarlos por area: el industrial solo usa sus centros y sus elementos (ejemplo: movimiento, limpieza y reparacion de envases).
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [15:19:10]
- Cita: "La idea seria que se fueran asociando, porque asi cada departamento trabaja con sus centros de costos y sus articulos mas rigidos."

### CON-05
- Enunciado: El elemento de costo no se borra si tiene historia. Debe poder dejarse fuera de uso para que no salga en el selector. Hoy aparecen los vigentes, los viejos y los de reserva.
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [15:19:10]
- Cita: "no nos deja, por ejemplo, anular el uso... hay muchos elementos de costo que ya no se usan."

### CON-06
- Enunciado: El codigo financiero clasifica el movimiento de banco para el flujo de caja (ingreso cereza, exportacion, nectarina, venta de agroquimicos, materia prima de productor). Sirve para ver que linea da mas ingreso o mas costo. En el pago de tesoreria tambien se pide.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [15:19:10]; transcripcion-reunion4.md, Speaker 01 [11:19:50]
- Cita: "el codigo financiero lo usamos netamente para el flujo de caja, para todo lo que tiene que ver con movimiento de banco y tesoreria."

### CON-07
- Enunciado: El comprobante diario se digita o se carga masivo (lo usan en remuneraciones) con un archivo de campos fijos. Antes de guardar debe mostrar errores: periodo, centro de costo de mas o de menos, elemento, area de negocio, y diferencia debe/haber en pesos y dolares. La glosa es el texto con el que despues se busca el comprobante. El archivo a veces falla por una celda pasada a texto o por un error de conexion, y tienen que rescatar una copia limpia.
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [16:44:11]
- Cita: "subimos el archivo y nos arroja si tiene o no errores, y ahi guardamos y se contabiliza."

### CON-08
- Enunciado: IVA y retenido estan en 19%. El honorario tiene factor actual, factor anterior y fecha desde la que rige, porque sube ano a ano. Debe verse la historia (ejemplo: hasta febrero 15% y desde marzo 17%) y aplicarse el factor vigente segun la fecha. Quieren historial de quien lo modifico.
- Modulo: contabilidad
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [15:19:10]; transcripcion-reunion4.md, Speaker 01 [09:08:00]
- Cita: "si hubo un cambio en junio, yo pongo que desde junio sea, por ejemplo, un factor del 15 a 25, y de mayo hacia atras sea del 14 a 5."

### CON-09
- Enunciado: En la reu3, contabilizar el libro es elegir cuenta, centro de costo, glosa y cliente. El libro de ventas deberia llegar del SII / GoSocket (factura, nota de credito y nota de debito), con opcion de cargar Excel. En la reu4 ese dato contable se mueve a la emision, por linea, y el libro pasa a ser consulta de lo ya emitido.
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [05:00:51] y [05:04:51]
- Cita: "al contabilizar nosotros seleccionamos cuenta contable, centro de costos, le agregamos una glosa, seleccionamos el cliente."

### CON-10
- Enunciado: El plan de cuentas real lo mandan en Excel. Tiene niveles de clasificacion y de agrupacion, y trabajan con cinco niveles. Cada cuenta debe poder exigir o quitar centro de costo y el resto de dimensiones. La importacion debe calzar con ese formato.
- Modulo: contabilidad
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [08:11:21]; transcripcion-reunion4.md, Speaker 01 [15:21:19]
- Cita: "el plan de cuenta igual tiene niveles, que algunos son de clasificacion y los otros son de agrupacion."

### CON-11
- Enunciado: Abrir y cerrar mes no va en parametrizacion. Va en cada modulo que se cierra por separado: contabilidad, contratistas e insumos.
- Modulo: contabilidad
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [08:42:50]
- Cita: "en los periodos contables tendria que estar en el modulo de contabilidad, en el modulo de contratista y en el modulo de insumos."

### CON-12
- Enunciado: Usan el libro mayor (debe, haber, saldo) mas que el libro diario. Lo que se mostro se parece a un balance de 8 columnas. Falta un menu de balance alimentado por los movimientos del ano. Van a mandar mayor, balance y diario de ejemplo.
- Modulo: contabilidad
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [09:23:50] y Speaker 02 [09:26:19]
- Cita: "falta yo creo que el balance de 8 columnas... seria otro menu que seria el balance."

### CON-13
- Enunciado: Tienen contabilidad electronica, pero no mensual: se sube al hacer la renta. El sistema saca la informacion, el contador externo la pasa a XML, firma con el certificado del representante y la carga al SII. Hacerlo dentro del ERP, con el cruce a la cuenta del SII, queda como segunda etapa. Maria Jesus lo ve viable. Certificarse como software de mercado es un trabajo aparte, dicho por Sergio.
- Modulo: contabilidad
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [09:39:40] y [09:56:50]
- Cita: "nosotros tenemos contabilidad electronica, por eso se sube una vez que uno hace la renta, no nos hacen hacer la mensualizada."

### CON-14
- Enunciado: Hay una pantalla de cuentas del SII que ellos no usaban. Sergio no le ve sentido si la cuenta se asigna en el detalle del documento. Maria Jesus dice que en Agrosoft hay que parametrizar lo que se crea y que aqui podria ser mas claro. Carlos la deja como parametrizacion. No queda una regla de negocio cerrada.
- Modulo: contabilidad
- Clase: duda
- Voz: no-claro
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [08:58:09]
- Cita: "quiza aqui se hace mas facil el poder parametrizarlo y mas como mas entendible."

---

## Tesoreria

### TES-01
- Enunciado: Agrosoft no esta hecho para conciliar ni para calzar pago y factura. Lo hacen con un parche y se producen diferencias. El modulo de ventas no conversa con ese calce; proveedores y tesoreria si.
- Modulo: tesoreria
- Clase: as-is
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [05:56:10]
- Cita: "en este ERP no esta, no esta hecho para conciliar. Ni para hacer los calces de lo que es el pago y la factura."

### TES-02
- Enunciado: El sistema dejo grabar un pago sin marcar ninguna factura. Debe advertir y no grabar.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [06:12:40]
- Cita: "me dejo guardar y no habia pinchado nada... deberia darme una advertencia que en realidad no estoy pinchando nada."

### TES-03
- Enunciado: Al pagar, el asiento saca el banco y rebaja la factura. Si pagan menos, queda el saldo. Si el documento esta intacto, total y saldo son iguales. Al eliminar, el reversador se hace solo y deja en cero el par reversado / reversador. En pesos, el pago respeta el tipo de cambio del comprobante y no calcula diferencia.
- Modulo: tesoreria
- Clase: as-is
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [06:16:51] y [06:39:10]
- Cita: "se me hace el asiento contable de banco y en la rebaja de la factura... y page esta factura."

### TES-04
- Enunciado: Hoy suben un Excel de cartola y concilian a mano, porque el numero del banco no calza con el comprobante que ellos ponen (ponen 1). Deben marcar los dos lados y los totales tienen que ser iguales. Si hay diferencia, buscan a mano en la cartola y en contabilidad (unos 300 movimientos). Piden un enlace directo al registro. Tambien habian pedido el PDF del banco; en la reu4 dicen que el correo diario no llega y que cargaran el Excel que ya usan.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [06:43:01] y [06:51:00]
- Cita: "tenemos que subir un archivo Excel con los movimientos de la cartola bancaria... de subir el PDF que nos manda el banco."

### TES-05
- Enunciado: Quieren cargar la cartola del dia o de la semana y contabilizar desde ahi. Lo que esta en la cartola es el movimiento oficial y debe quedar conciliado al contabilizarlo. Lo pendiente es lo que falta por contabilizar. Hoy hacen al reves: contabilizan mirando el banco y suben la cartola a fin de mes. Subir varias cartolas en el mes las mezcla con el historico.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [07:23:01]; transcripcion-reunion4.md, Speaker 01 [10:28:59]
- Cita: "al contabilizar el movimiento en si de la cartola, deberia quedar contabilizado y conciliado."

### TES-06
- Enunciado: Conciliar bloquea la edicion en contabilidad, y eso lo dan por bueno. El problema es que no pueden desconciliar un solo movimiento: si el pago quedo en la empresa o el cliente equivocado, reversan el mes entero (todas, automaticas o manuales) y vuelven a conciliar. Piden corregir uno sin rehacer el mes.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [07:50:41]
- Cita: "tenemos que reversar todo el mes, modificar el movimiento, volver a conciliar y volver a revisar."

### TES-07
- Enunciado: Trabajan con muchos anticipos. El anticipo se ingresa en contabilidad, no en el calce, y se reconoce por el tipo de documento. A veces lo parten: una parte calza una factura y la otra queda pendiente, y ese resto queda como traspaso porque no hubo un segundo movimiento de banco. En el banco es un solo ingreso.
- Modulo: tesoreria
- Clase: as-is
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [08:20:10]
- Cita: "ese anticipo tuvimos que dividirlo en 2 y calzar una parte con una factura y la otra parte queda pendiente."

### TES-08
- Enunciado: Si calzan en pesos, el sistema deja diferencia en dolares y no la contabiliza. Si pagan en dolares, si calcula el ajuste en pesos. Con doble moneda debe calcular la diferencia en los dos sentidos. En el ejemplo, el codigo financiero del productor es materia prima.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [09:06:11]
- Cita: "al hacerlo en pesos tambien deberia calcularme la parte de dolar, y al final es el mismo efecto pero al reves."

### TES-09
- Enunciado: El tipo de cambio del pago sale por la fecha del movimiento y se puede editar. En facturas de productores el tipo de cambio es un promedio que no existe en el Banco Central, y lo digitan. Lo mismo pasa en proveedores y en materiales: el tipo de cambio del documento no es el de la factura.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [11:55:30]
- Cita: "las facturas de los productores tienen un tipo de cambio promedio, que muchas veces no existe el tipo de cambio como el Banco Central."

### TES-10
- Enunciado: Quieren nomina de lo que hay que pagar y de lo que hay que cobrar, con antiguedad (30 dias, 90 dias, mas de 90). En general la nomina es de pago. La cobranza de hoy es un informe llamado inventario balance: deuda por cliente o proveedor, y despues el detalle. Sergio propone seguimiento de compromisos, reenvio de la factura y registro de quien movio la fecha. Maria Jesus lo acepta.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [09:11:10]; transcripcion-reunion4.md, Speaker 01 [13:00:39] y [14:08:39]
- Cita: "pudieramos ver las nominas de pago, lo que esta proximo a vender, lo que tiene, no se, un atraso de mas de 90 dias."

### TES-11
- Enunciado: La fecha de vencimiento se pone al ingresar el documento y depende de la negociacion: 30 dias, 90 dias, 3 meses en materiales, 6 meses, o hasta un ano. Con GoSocket llegara la fecha que puso el proveedor. Ellos usan otra para pagar: cerca del 80% coincide con la real; materiales y productores van a plazo, y el productor se paga al liquidar la fruta. Poder editar esa fecha es ideal, y solo lo hace tesoreria. Maria Jesus solo mira.
- Modulo: tesoreria
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [13:11:29] y [13:45:50]
- Cita: "la persona que puede editar debiese ser solamente el encargado de tesoreria. Yo deberia poder solo visualizar."

### TES-12
- Enunciado: Hay RUT que es proveedor y cliente a la vez, y hay que compensar lo vendido con lo comprado. Hoy estan en dos modulos. Piden un estado de cuenta del RUT, con anticipos, compras y ventas, pagadas y pendientes, filtro todos o pendientes, y enlace al pago y a la factura. El reporte va en Excel y, en algunos casos, tambien en PDF.
- Modulo: tesoreria
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [14:42:00]
- Cita: "tenemos proveedores que tambien actuan como clientes, y que pasa, a veces tenemos que compensar lo que yo le vendi y lo que ellos me vendieron."

### TES-13
- Enunciado: La pantalla de conciliacion debe mostrar lo no conciliado y tambien poder ver lo ya conciliado. Arriba, un resumen de monto conciliado y pendiente; si se puede, tambien la cantidad. La cartola trae cargos y abonos.
- Modulo: tesoreria
- Clase: ui
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [14:14:40] y [14:19:39]
- Cita: "aqui igual seria bueno que quizas arriba tuviera como un resumen de los, como los saldos de conciliados y pendientes."

### TES-14
- Enunciado: ALM da anticipos a productores. AlmaWeb recibe anticipos de clientes. ALM concentra packing, materia prima y mano de obra, y entrega el producto terminado a AlmaWeb. AlmaWeb lo compra y lo exporta, y por eso no tiene inventario.
- Modulo: tesoreria
- Clase: dato
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [12:36:30] y [12:39:49]
- Cita: "a los productores nosotros les damos anticipo... por el lado de LM. Y por el lado de AlmaWeb son anticipos que recibimos de los clientes."

### TES-15
- Enunciado: La pantalla de pagos, como lugar donde la persona de cartola ingresa el pago, les parece bien. El numero que hoy ponen a mano (siempre 1) deberia ser el numero de la cartola. El asiento del ejemplo mueve banco y proveedor por el mismo monto, en pesos y en dolares.
- Modulo: tesoreria
- Clase: as-is
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [11:29:20] y [12:25:40]
- Cita: "como lo hacemos manual, siempre ponemos el 1, pero aqui deberia ir, por ejemplo, el numero de cartola."

---

## Ventas

### VEN-01
- Enunciado: Si se equivocan en el libro de ventas (cliente, centro de costo), al reversar no pueden corregir la linea: hay que escribir el documento de nuevo. En proveedores si editan la linea. Pasa al momento o en la revision del mes. No hay un dato que justifique bloquear la correccion. Quieren reutilizar los datos.
- Modulo: ventas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [04:39:40] y [05:29:10]
- Cita: "no puedo solo editar lo que me equivoque, tengo que ingresar el documento totalmente completo de nuevo."

### VEN-02
- Enunciado: Reversar deja dos asientos: el original y la contrapartida, para que la contabilidad de cero. El documento corregido lleva un numero nuevo (en el ejemplo, 472 original, 473 reversa, 474 nuevo). Al grabar de nuevo debe avisar que se estan usando datos de una reversa.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [05:35:00]
- Cita: "el 472 queda con el original, que es el reversado. El 473 deberia ser la reversa... y el 474 el nuevo registro."

### VEN-03
- Enunciado: Guardar la venta la deja temporal y no entra a contabilidad ni a los reportes; el informe la muestra pendiente. Grabar si contabiliza. El boton guardar, para ellos, sobra. El flujo es grabar y contabilizar.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [05:06:21] y [05:46:20]
- Cita: "si yo lo guardo, se me guarda pero no se me va al registro contable. Si yo lo grabo, se me va al registro contable."

### VEN-04
- Enunciado: La venta pide tipo de documento, numero, condicion (contado, 15 o 30 dias), referencia si es nota de credito o debito, y cliente. No usan numero de despacho, telefono ni fax. Tambien piden modulo de venta (ejemplo mercado nacional), centro de costo, area de negocio, cantidad y precio. En la demo el cliente guardado no fue el elegido.
- Modulo: ventas
- Clase: dato
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [04:56:31]
- Cita: "lo demas no es necesario rellenarlo: numero de despacho, telefono cliente, fax, nada."

### VEN-05
- Enunciado: El cliente lo crea contabilidad, no el vendedor, para no dejar la ficha abierta. No piden un maestro de vendedores ni un contacto de empresa en esa pantalla. Para crear basta giro, razon social, RUT y direccion. En el registro debe salir quien lo creo.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [05:15:40] y [05:23:11]
- Cita: "las personas que crean el cliente somos el area contable, ni siquiera el vendedor... por un tema de control."

### VEN-06
- Enunciado: Deben existir cliente nacional y cliente de exportacion. Hoy, para crear el de exportacion, piden un RUT en una pagina externa.
- Modulo: ventas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [07:07:40]
- Cita: "nosotros podemos crear clientes exportacion y clientes nacionales... hay que pedir un generador de RUT en una pagina."

### VEN-07
- Enunciado: El documento nuevo queda en borrador. Grabar y contabilizar lo emite hacia GoSocket y lo contabiliza. El folio lo entrega GoSocket. En el borrador, al pinchar el folio, debe verse el documento con marca de agua. Despues, el PDF timbrado. Cuenta contable y centro de costo van por linea, en la emision, y no se envian a GoSocket. Sergio agrega referencia, descuento y recargo; Maria Jesus no lo discute.
- Modulo: ventas
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [05:47:59] y [06:14:49]
- Cita: "ahi seria grabar y contabilizar, y ahi se emitiria el documento."

### VEN-08
- Enunciado: El libro de ventas muestra lo ya emitido y contabilizado, para cruzarlo con el SII (folio faltante, documento en la nube, error). No debe quedar ahi un documento anulado ni reversado. La reversa del libro sirve para corregir un dato contable (centro de costo o cuenta: de un huerto a otro, de exportacion a nacional) y volver a contabilizar. El documento tributario sigue existiendo. No se puede repetir el mismo folio. Monto y detalle de la factura no se modifican por esa via.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [05:07:09] y [06:27:30]
- Cita: "en el libro de ventas tiene que quedar todo siempre contabilizado. Lo que podemos hacer es modificar informacion, pero si o si la factura existe."

### VEN-09
- Enunciado: En el libro de ventas quieren descargar el libro, reenviar PDF y XML al correo del cliente, y un total por tipo de documento, como el RCV del SII, para cruzar rapido. El boton de emitir no va en el libro: quien emite y quien solo mira el libro pueden ser roles distintos.
- Modulo: ventas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [06:35:49] y [06:41:19]
- Cita: "aca en el libro de ventas podria estar la opcion de descargar libro nomas."

### VEN-10
- Enunciado: La factura de exportacion pide aduana, pais de destino, puerto, tipo de venta y condicion. Son codigos del SII, no el nombre del pais. Maria Jesus tiene un manual de como la ingresan y lo puede compartir. En Acepta, la nota de credito o debito de exportacion obliga a reescribir todo y deja asociar la factura a otro cliente. Piden la nota precargada desde la factura.
- Modulo: ventas
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [07:24:59] y [07:27:30]
- Cita: "en Acepta, si queremos emitir nota de credito y debito de exportacion, tenemos que volver a poner todos los datos."

### VEN-11
- Enunciado: La factura de exportacion se emite al mandar la fruta. La nota de credito o de debito se emite al liquidar, cuando se sabe quien gano o quien debe. Casi todas las facturas de exportacion llevan una u otra. La anulacion completa es poca; lo habitual es correccion de monto o aumento.
- Modulo: ventas
- Clase: regla
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [07:37:10]
- Cita: "todas las facturas si o si tienen asociada una nota de credito, una nota de debito, que se hace el momento de la liquidacion."

### VEN-12
- Enunciado: Si la reversa de una venta en el libro debe o no pasar por un administrador, Maria Jesus no lo cierra: dice que el digitador lo hace mas abierto.
- Modulo: ventas
- Clase: duda
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion3.md, Speaker 01 [04:43:01]
- Cita: "No se, que es un poco mas abierto porque se que hay el rol del digitador."

---

## Facturacion

### FAC-01
- Enunciado: GoSocket reemplaza a Acepta. Quieren facturar agosto en Acepta y cambiar el 1 de septiembre. Al dar de baja el sistema viejo se borra su base: no hay mes de prueba ahi. En esta reunion el audio tambien dice "WhatsApp" y "Osoquet" para ese mismo cambio. La reunion de traspaso con soporte debia agendarse al firmar la propuesta, y piden que el equipo del ERP este.
- Modulo: facturacion
- Clase: decision
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [12:07:31]
- Cita: "pedimos que la implementacion de WhatsApp estuviera el 1 de septiembre... facturar agosto con Acepta y en septiembre hacer el cambio definitivo a Osoquet."

### FAC-02
- Enunciado: GoSocket y el ERP son independientes y despues se conectan. Lo urgente es facturar. Si el ERP se conecta meses mas tarde, vuelven a hacer el traspaso. La conexion que les importa es el libro de compras en linea para contabilizar directo. Mientras tanto pueden seguir contabilizando en Agrosoft lo emitido en GoSocket. GoSocket debe traer los documentos que hoy estan en Acepta.
- Modulo: facturacion
- Clase: pedido
- Voz: cliente
- Quien: Maria Jose
- Fuente: transcripcion-reunion2.md, Speaker 01 [12:21:50]
- Cita: "la idea de que GoSocket este conectado con el ERP de AlmaWeb es que nos aparezca el libro de compras en linea y podamos contabilizar directo."

### FAC-03
- Enunciado: En la reu4 ya firmaron y llevaban una semana sin contacto. Si no hay conexion en septiembre, Maria Jesus posterga el cambio a la otra temporada, porque en septiembre se renueva Acepta. El cambio de facturador lo necesitan en agosto. Primero pueden emitir en el portal de GoSocket y, si el ERP aun no esta conectado, cargar el libro o los PDF que hoy bajan de Acepta.
- Modulo: facturacion
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [03:53:40] y [04:09:00]
- Cita: "necesitamos que sea agosto si o si el cambio de facturador."

### FAC-04
- Enunciado: El escenario que el cliente llama ideal es una sola plataforma: se emite en el ERP y GoSocket informa al SII por debajo. Antes de apagar Agrosoft quieren unos dos meses en paralelo, los mismos reportes en los dos sistemas, y un dia de prueba solo con el ERP. Sergio estima dos semanas de integracion una vez entregado el portal y la documentacion.
- Modulo: facturacion
- Clase: decision
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [04:17:10] y [04:22:20]
- Cita: "vamos a trabajar de manera espejo, o sea, deberiamos hacer el mismo reporte y aparecer la misma informacion."

### FAC-05
- Enunciado: La pantalla de GoSocket dentro del ERP no es un mantenedor. Es un paso intermedio. Lo que se administra es el libro, no ese panel.
- Modulo: facturacion
- Clase: decision
- Voz: equipo
- Quien: Carlos
- Fuente: transcripcion-reunion3.md, Speaker 00 [05:26:40]
- Cita: "GoSocket es un paso intermedio... esta pestana, si es que se conserva, va a ser como consulta."

---

## Otro

### OTR-01
- Enunciado: El modulo de maquinaria no lo usan en ningun rubro. Lo quieren para el agricola: tractor, pulverizador, mantenciones, desgaste, y prorrateo del uso entre cuarteles o labores.
- Modulo: otro
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [13:32:20]
- Cita: "si yo tengo un tractor y lo ocupo, no se, pues en 5 cuarteles, hacer el desglose por cuartel, por cuartel o por labor."

### OTR-02
- Enunciado: El modulo de gestion de Agrosoft no lo usan: era muy basico. Por eso existe el area de Mario, con Power BI directo a la base. Vuelve en agosto. En el ERP piden graficos cortos para contabilidad y gerencia: costo por especie, desviacion contra presupuesto, desviacion de centro de costo.
- Modulo: otro
- Clase: pedido
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [17:46:00]
- Cita: "graficos rapiditos de, no se, pues desviacion en el centro de costo, o ver, no se, la cantidad de costos versus las especies."

### OTR-03
- Enunciado: Contratistas no se cruza con los otros modulos. Solo se cruzaba con mano de obra, por actividad y labor.
- Modulo: otro
- Clase: regla
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [04:33:01]
- Cita: "de los otros modulos no se cruza ninguno con contratistas. Contratistas se cruza solamente con mano de obra."

### OTR-04
- Enunciado: Cada modulo tiene sus informes. La reporteria del ERP se arma cuando el modulo ya funciona, y el cliente dira que pantallas se exportan y en que formato. Van a mandar la reportabilidad actual, un informe de movimiento de bodega, el manual de factura de exportacion, el Excel de cajas, mayor, balance, diario y la cartola.
- Modulo: otro
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [15:11:00] y [12:11:30]
- Cita: "tendra que mandarte ya como la reportabilidad del sistema y ver cuales podemos mejorar como informe."

### OTR-05
- Enunciado: Si una pantalla del ERP queda demasiado parecida a Agrosoft, el cliente pide que el equipo proponga mejoras. Sergio pide que la contabilidad quede modular, para agregar despues otro modulo que genere asientos.
- Modulo: otro
- Clase: pedido
- Voz: cliente
- Quien: Maria Jesus
- Fuente: transcripcion-reunion4.md, Speaker 01 [04:29:29]
- Cita: "si hay alguna, no se, algun modulo que nosotros lo estemos viendo como muy basico o muy similar a AgroSoft, la idea es que igual nos puedan dar ideas como de mejora."

### OTR-06
- Enunciado: En la reu1 el cliente resume el encargo como un Agrosoft version 3.0, mejorando sobre todo contratistas, y sin mano de obra.
- Modulo: otro
- Clase: decision
- Voz: cliente
- Quien: no dicho
- Fuente: transcripcion.md, Speaker 00 [02:51:40]
- Cita: "lo que nosotros queremos hacer es como un Agrosoft pero una version 3.0."

---

## Contradicciones dentro de estos cuatro archivos

1. Alerta de IVA entre orden y factura. En la reu1 el cliente muestra que una orden exenta se contabilizo con un documento afecto y no salto alerta, porque el neto cuadraba (`transcripcion.md` [09:56:51]). En la reu2 dice que, si la factura era afecta y la orden venia exenta, si le daba una alerta (`transcripcion-reunion2.md` [11:58:51]).

2. Afecto o exento en la orden. En la misma reu1 el cliente dice que la marca condiciona el documento, y despues dice que la orden solo reconoce el neto y que dejarla rigida impediria facturas mixtas y combustible con impuesto especifico. Deja dos soluciones abiertas y no elige (`transcripcion.md` [07:02:20] y [09:56:51]).

3. Un usuario, varios roles. En la reu2 Carlos dice que una persona podria tener a la vez el rol de secretaria y el de digitador (`transcripcion-reunion2.md` [10:08:20]). En la reu3 dice que el sistema no permite dos roles y que la mezcla se crea como un rol nuevo (`transcripcion-reunion3.md` [01:20:51]).

4. Ver la clave de otro. Maria Jesus dice que hoy cada uno cambia su clave y que estaria bien si el administrador viera la clave de otro (`transcripcion-reunion3.md` [01:50:11]). Carlos responde que la clave no se muestra y que el administrador solo pone una temporal (`transcripcion-reunion3.md` [01:51:50]). Ella dice que entiende. No hay un "si" al cierre. La clave de la reu4 es otra: la clave para reversar una proforma, no la clave de ingreso.

5. Proforma definitiva y edicion. En la reu1, definitiva no se puede tocar y eso les duele porque hay errores (`transcripcion.md` [02:51:40]). En la reu3 piden que editar una proforma ya autorizada vuelva a pedir autorizacion (`transcripcion-reunion3.md` [03:45:40]). En la reu4, al ver que una aprobada todavia se editaba, piden dejarla sin edicion ni eliminacion, solo asociarla a la factura, y reversar la aprobacion con clave (`transcripcion-reunion4.md` [02:33:50] y [02:36:29]).

6. Donde se imputa la venta. En la reu3, cuenta, centro, glosa y cliente se eligen al contabilizar el libro (`transcripcion-reunion3.md` [05:00:51]). En la reu4, cuenta y centro van en la emision, por linea, y el libro de ventas solo muestra lo ya emitido y contabilizado (`transcripcion-reunion4.md` [06:04:20] a [06:27:30]).

7. Reversar o anular la factura de venta. Sergio propone un boton que anule y emita solo la nota de credito (`transcripcion-reunion4.md` [04:45:10] y [04:53:10]). Maria Jesus dice que en el libro no debe quedar un documento anulado ni reversado, porque se compara con el SII, y que la reversa es para corregir la imputacion contable (`transcripcion-reunion4.md` [05:00:40] y [05:19:39]). Despues distingue: la anulacion tributaria es la nota de credito; la reversa interna no borra la factura.

8. Centros de costo entre empresas. En la reu3 Maria Jesus pregunta si el centro de costo es transversal a todas las empresas (`transcripcion-reunion3.md` [02:19:41]). En la reu1 muestra que el sistema viejo deja elegir un centro de otra empresa y lo trata como error. En la reu4 dice que cada empresa tiene los suyos y pide ver solo los de la empresa activa. Sergio agrega que el mismo codigo puede repetirse en otra empresa (`transcripcion-reunion4.md` [01:14:39] y [01:38:20]).

9. Plazo de GoSocket. En la reu2 el cambio es el 1 de septiembre, facturando agosto en Acepta, y dicen que no los frena si el ERP todavia no esta conectado (`transcripcion-reunion2.md` [12:07:31] y [12:17:00]). En la reu4, si GoSocket no responde, postergarian a la otra temporada porque Acepta se renueva en septiembre, y a la vez dicen que el cambio de facturador tiene que ser en agosto (`transcripcion-reunion4.md` [03:53:40]). Tambien dicen que las dos plataformas deben funcionar separadas y, en la misma reunion, que lo ideal es una sola.

10. Conciliado se bloquea, pero quieren corregir uno. En la reu2 dicen que no poder editar un movimiento ya conciliado "esta bien", y enseguida dicen que reversar el mes entero para corregir un pago si es un problema (`transcripcion-reunion2.md` [07:50:41]). En la reu4 el diseño pasa a ser otro: contabilizar desde la cartola para que nazca conciliado, y la pantalla de conciliacion muestra lo pendiente (`transcripcion-reunion4.md` [10:36:09] y [14:14:40]).

11. Niveles de bodega. En la reu1 no los usan y dejan la duda para la persona de materiales (`transcripcion.md` [11:17:10]). En la reu2 Maria Jose dice que no estan parametrizados y Carlos cierra que por ahora no hay necesidad (`transcripcion-reunion2.md` [12:44:20] y [12:46:51]).

12. Cartola en PDF o en Excel. En la reu2 la mejora pedida es subir el PDF del banco (`transcripcion-reunion2.md` [06:43:01]). En la reu4 dicen que el PDF o el correo diario no llego a implementarse con el banco, y piden cargar el Excel de cartola que ya trabajan (`transcripcion-reunion4.md` [10:49:39]).
