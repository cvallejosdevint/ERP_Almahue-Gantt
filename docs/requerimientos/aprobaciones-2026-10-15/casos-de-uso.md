# Casos de uso: primer eslabon y aprobaciones de insumos

Fecha de lectura: 2026-10-16. Fuente primaria: la transcripcion. No hay transcripcion del 15/10. La sala con cliente es la del 14/10.

Las notas del usuario filtran el alcance. No reemplazan la voz. Si una frase esta solo ahi, no entra como caso: queda en la seccion 3.

Este paquete es solo aprobaciones, en dos partes:

1. El primer eslabon parte desde cero hasta el monto configurado, y el siguiente sigue desde ahi. No hay aprobacion automatica por monto bajo.
2. Cadena del modulo de insumos para la OC madre y la OC hija. Se marca al jefe que genera la madre. La madre pasa por esa cadena. La hija no.

No hay casos de proformas, contabilidad, libro de compras, reportes ni estado de resultados. Esas frases, cuando el cliente las dice, quedan en la seccion 4.

Carlos y Sergio son hipotesis. Un caso entra si lo dice el cliente (Agustin, Maria Jesus, Lupe, Mario, Rodrigo, Fran) o si el cliente confirma la frase. Whisper no rotula al locutor. Donde no hay nombre, se dice y se usa la pista de la sala.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`, API `http://localhost:3001/api/v1`.

## 1. Reuniones leidas

| Reunion | Archivo | Cliente en la sala | Que se busco |
|---|---|---|---|
| 2026-10-14 presentacion | `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md` | Maria Jesus, Mario, Rodrigo y Fran. Ella los nombra en [02:21]. Agustin y Lupe no estan. | Sala completa. La cadena esta en [30:44] a [33:51] y el flujo de insumos en [51:42] a [53:22]. |
| 2026-10-01 | `docs/reuniones/transcripciones/transcripcion-2026-10-01-reunion-cliente.md` | Maria Jesus, Fran y Lupe. Mario aviso que estaria y al inicio estaba en otra reunion. | Madre/hija [47:07] a [48:05], cadena [50:22] a [52:48], jefe de abastecimiento [57:10]. |
| 2026-10-06 GoSocket y contratistas | `docs/reuniones/transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md` | Maria Jesus. Pablo es de GoSocket. | Aprobacion y madre. El tramo es de proforma. No entra. |
| 2026-09-24 | `docs/reuniones/transcripciones/transcripcion-2026-09-24-reunion-cliente.md` | Lupe, Fran y Sigrid. | Solo el antecedente que Maria Jesus revoca: [04:24] y [06:11]. No se abre caso. |

No aplican:

- `transcripcion-2026-10-13-interna-carlos-sergio.md`. Carlos y Sergio. No hay cliente. No habla de cadena, eslabon, jefe ni madre.
- `transcripcion-2026-10-14-jose-sergio.md`. Jose y Sergio. No hay cliente. En [08:56] a [09:05] el equipo dice "dijeron que deberia pasar la madre". Es hipotesis. No se usa.
- `transcripcion-2026-10-13-gosocket-almahue.md`. Maria Jesus esta (la nombran en [03:13] y [03:43]). Habla de proformas aprobadas y de asociarlas. No confirma una frase de cadena, de primer eslabon, de jefe ni de madre/hija.

## 2. Casos

### CU-01. No hay aprobacion automatica: el primer eslabon parte desde cero y el siguiente sigue desde ahi

- Quien: Maria Jesus. La voz no esta rotulada. La pista es [32:29]: "yo estaba de vacaciones y no estoy de acuerdo". El mismo "yo dejaria" cierra en [33:38].
- Donde: `transcripcion-2026-10-14-presentacion.md` [32:29], [32:39], [32:52], [33:38] y [33:48]. El equipo propone la forma en [32:45] y [33:23]. Ella responde "Si, yo lo haria asi, yo dejaria todo con aprobacion" y "Exacto".
- Que pasa: ella rechaza la aprobacion automatica por monto. Dice que hasta 5 pesos tiene que pasar por aprobacion. En Almahue reciben muchas facturas de 10.000 o 15.000 (la transcripcion dice AlmaWeb), del orden de 300 en el mes. Un automatico solo por monto tambien dejaria pasar almuerzo o libreria. El equipo propone que no exista un "no pasa por la cadena", que las aprobaciones sean "desde" y que el primer eslabon apruebe desde cero hasta su monto. El ejemplo del equipo es Felipe desde cero hasta 500.000. Ella acepta esa forma. No fija el nombre ni el 500.000.
- Documento: la cadena de aprobacion. En el tramo el ejemplo son esas facturas y la edicion de monto de la orden de compra. No nombra un modulo distinto para la regla.
- Que debe quedar: no hay tramo que se apruebe solo. El primer integrante cubre desde cero hasta el monto configurado para el. Un documento de 5 pesos entra a ese primer eslabon. El eslabon siguiente cubre desde ese monto hacia el suyo: no queda un hueco en el que el documento se apruebe solo. Un monto que cabe en el primer tramo no recorre los eslabones de arriba. Ella acepto un primer tramo "desde cero hasta" un tope, no que todos firmen lo chico. Los topes los configura la empresa.
- Alcance de "todas": ella dijo "todo con aprobacion" sobre la cadena, no modulo por modulo. La misma regla vale para la cadena de insumos de CU-04. Este paquete no abre un caso de proforma.
- Antecedente que ella revoca: el 24/09, con Lupe, Fran y Sigrid, se hablo de un tramo menor que "pasa una version automatica" (`transcripcion-2026-09-24-reunion-cliente.md` [04:24] y [06:11]). La voz de ese tramo no trae nombre. El 14/10 ella dice que esa decision se tomo en sus vacaciones y no esta de acuerdo. Gana el 14/10.

### CU-02. La edicion del monto, para abajo o para arriba, pasa por aprobacion

- Quien: Maria Jesus. La voz de [32:03] no esta rotulada. Es el mismo "yo dejaria" de CU-01, dos minutos antes de identificarse por las vacaciones.
- Donde: `transcripcion-2026-10-14-presentacion.md` [31:36] a [32:08]. Antes, el 01/10, el equipo dice que si el monto aumenta la orden vuelve a la linea y el cliente responde "Si" (`transcripcion-2026-10-01-reunion-cliente.md` [47:52] a [48:05]).
- Que pasa: el equipo tenia entendido que bajar el monto se modifica y no pasa por aprobaciones, y que subir, si cae en una cadena, recorre la cadena. Ella dice: "yo dejaria edicion, sea para abajo o para arriba, con aprobacion". El equipo cierra con "Perfecto". El "Si" del 01/10 confirma solo la subida. El 14/10 agrega la bajada y descarta el salto.
- Documento: orden de compra madre. El tramo viene de la edicion de esa orden ([30:44] en adelante). La frase de ella es "edicion", no una lista de otros documentos.
- Que debe quedar: una edicion del monto de la madre, menor o mayor, pide aprobacion. No queda un atajo para el monto inferior. El momento de esa edicion es el de CU-03. Una recepcion parcial, con la madre todavia abierta, no es esta edicion.

### CU-03. La madre se edita una sola vez, al cerrarla, y esa edicion pide la aprobacion

- Quien: cliente. Locutor no rotulado. En [31:31] otro locutor dice "como ella le dice". La unica mujer nombrada del lado cliente es Maria Jesus (estan ella, Mario, Rodrigo y Fran). En [44:30] el mismo lado operativo cuenta la negociacion de abastecimiento.
- Donde: `transcripcion-2026-10-14-presentacion.md` [30:44] a [31:36], [43:59] y [44:30] a [45:09].
- Que pasa: la madre se puede editar una sola vez, cuando se cierra. No cada vez que aparece un error. Si hace falta otro cambio, se pide a contabilidad. Esa unica chance igual pide la solicitud de aprobacion: [31:31] dice "solicito de adicion, como ella le dice", y CU-02 ya dejo la edicion con aprobacion. El sentido de ver la aprobacion es poder dar la madre por cerrada [43:59]. El caso de monto menor es la renegociacion: estimaron fruta, negociaron 100 cajas y al final necesitan 50; ahi cierran [44:30] a [44:48]. El equipo pregunta si con monto menor se puede cerrar en cualquier momento y el cliente dice "Exacto" [45:09].
- Documento: orden de compra madre.
- Que debe quedar: una sola edicion, en el cierre, para dejar el monto en el que se cierra (menor o mayor, CU-02), y esa edicion entra a la cadena. No se reabre en cada correccion.
- Limite, mismo tramo, sin caso aparte: si solo llego una parte y la madre sigue abierta, esa diferencia no es la edicion y no vuelve a la cadena. En [43:55] un locutor no rotulado dice que ese caso "no deberia ir a aprobacion". En [44:06] el equipo lo entiende: la orden sigue abierta porque recibieron la mitad. [45:10] ("pedir el municipal") no se entiende y no arma caso.

### CU-04. Insumos tiene su flujo de aprobacion, distinto del de servicios

- Quien: cliente. Locutor no rotulado. Responde al equipo en las reglas de aprobacion. En la sala estan Maria Jesus, Mario, Rodrigo y Fran.
- Donde: `transcripcion-2026-10-14-presentacion.md` [51:42] a [52:40]. El equipo pregunta si las reglas de orden de compra hay que separarlas para insumos. El cliente dice el otro tipo: "Servicios" [52:18].
- Que pasa: la orden de servicio es aprobacion y recepcion, y siempre es una a una. La de insumos es la que llega por partes [52:21] a [52:27]. El equipo dice que habria que agregar un tipo de flujo. El cliente dice "Si" [52:40]. El rotulo que sigue, "De servicio o de insumos", cae en el mismo intercambio.
- Documento: la cadena de la orden de compra de insumos, separada de la de servicios.
- Que debe quedar: dos flujos. El de insumos no es el de servicios. La cadena de insumos usa la regla de CU-01: su primer eslabon parte desde cero.
- La pantalla: el equipo esta en las reglas de aprobacion, la misma que el 01/10 mostro con grupos, integrantes, escalas y simulador (`transcripcion-2026-10-01-reunion-cliente.md` [50:55] a [51:46]). El cliente no dice "tab", "arbol" ni "Administracion". Esos nombres quedan en la seccion 3.

### CU-05. Se marca al jefe: la madre pasa por la cadena de insumos y la hija no

- Quien: cliente. Locutor no rotulado. Confirma lo que el equipo dice que le contaron. Pista: el mismo intercambio de CU-04.
- Donde: `transcripcion-2026-10-14-presentacion.md` [52:42] a [53:15], y el para que de la madre en [41:07]. La hija "se apruebe con la guia" en [37:50] a [37:56].
- Que pasa: el equipo dice que le contaron que el jefe genera la orden de compra, y el cliente dice "Si" [52:50]. El equipo propone identificar quien es el jefe dentro de los integrantes, para que esa persona tenga el menu. El cliente cierra: "La madre es el jefe. Y la hija la va a generar el administrativo" [53:15]. Antes, el mismo lado dice que la madre solo deberia necesitar una vez aprobacion, porque con las hijas tienen el real [41:07]. La hija nace cuando llega el despacho y queda con la guia [37:50] a [37:56]. El administrativo la genera al recepcionar, en insumos [52:59] a [53:07].
- Documento: orden de compra madre de insumos, y la hija que nace de su recepcion.
- Que debe quedar: en el grupo de insumos se marca un integrante como jefe. Solo ese jefe puede generar la madre. La madre entra una vez a la cadena de CU-04. La hija no entra a esa cadena: la genera el administrativo con la guia. La madre vive en insumos. El 01/10 el cliente ya dijo que la madre es informativa y no se ve fuera de insumos, y el equipo lo repitio; el cliente cerro con "Exacto" (`transcripcion-2026-10-01-reunion-cliente.md` [47:20] a [47:43]). El 14/10 lo repite: "solo insumo" [47:18] y "el de insumo es un mundo aparte" [46:58].
- El 01/10 [57:10] "jefe de abastecimiento" es quien controla la guia fisica. No es esta marca del grupo.

## 3. Pedido anotado sin voz del cliente

Estas frases estan en las notas y el cliente no las dice. No son casos. La regla que si dijo esta en el CU indicado.

- "desde monto $1". Ella dijo "desde cero" y "5 pesos" [32:39] y [33:23], y acepto esa forma [33:38]. El $1 no es otro piso. Queda en CU-01.
- "en Administracion > Aprobaciones, un tab nuevo llamado Insumos, con su arbol". El cliente dijo "Si" a un flujo aparte de servicio o de insumos [52:40], mirando las reglas de aprobacion. No dijo tab, arbol ni Administracion. El flujo aparte es CU-04.
- "jefe de insumos" y "jefe de bodega". El cliente dijo "el jefe" y "La madre es el jefe" [52:50] y [53:15]. No uso esos dos titulos. La marca es CU-05.
- "submenu de creacion de OC insumos para el jefe de bodega". El equipo dijo que el jefe marcado entra a ese menu [52:51] y que hay que tocar los submodulos de insumos bodega [54:15]. El cliente confirmo que la madre la hace el jefe. No dijo submenu ni jefe de bodega. Quien crea la madre es CU-05.

## 4. Dicho en la sala y fuera de este paquete

El cliente lo dice. El usuario lo dejo fuera. No hay caso.

- Proformas, centralizacion, cierre de mes y contratistas: [07:59] a [20:28] y [59:10] a [01:03:01]. El 06/10 la aprobacion que se conversa es la de la proforma, y en [37:20] a [37:34] se pide grupo de proforma separado del de orden de compra. No es la cadena de insumos.
- Guia, libro de compras y contabilizacion de la hija: [34:30] a [41:05] y [49:20] a [51:41]. De ahi solo se uso, en CU-05, que la hija nace con la guia y que la madre se aprueba una vez.
- Quien ve la madre y quien ve la hija: [54:23] a [55:58]. Compras ve la hija; insumos ve madre e hija. No es la cadena.
- Reportes PDF y estado de resultados: [56:26] a [59:07].
