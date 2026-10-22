# Casos de uso - auditoria octubre 2026

Extraccion de lo que el cliente pidio en las salas de octubre 2026. Sirve para auditar el codigo. No es un diseno nuevo.

Este archivo no reescribe `docs/requerimientos/presentacion-2026-10-14/`. Ese paquete es indice. Si choca con una transcripcion, gana la transcripcion.

Empresa de lectura para la auditoria posterior: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`.

No se implemento codigo, no hubo commit, no se emitio DTE, no se pago, no se cerro el mes y no se corrio `prisma migrate deploy`.

## Como se leyo

Entra un caso si lo dice el cliente o si el cliente confirma la frase. Cliente en estas salas: Maria Jesus (MJ), Lupe, Fran / Lafran, Mario, Rodrigo. Carlos y Sergio son hipotesis. Pablo (GoSocket) no es cliente del ERP: su frase entra solo si Maria Jesus u otro cliente la confirma como pedido al ERP.

Si la voz no trae nombre, se dice y se usa quien estaba en la sala. No se inventa un caso para tapar un silencio.

Si dos salas de octubre dicen lo contrario, gana la mas reciente con cliente: 14/10 > 13/10 > 06/10 > 01/10. La frase anterior queda anotada.

Reu1 a Reu3 son el as-is de Agrosoft. Reu5 no cuenta. Si Reu6 y Reu4 chocan, gana Reu6. Una sala anterior a octubre solo se cita como apoyo, en archivo y minuto. No crea un caso por si sola.

El encabezado "No es fuente de requisitos" de las transcripciones del 01/10 y del 06/10 es una advertencia del pipeline Whisper. No descarta la sala. Un caso entra si lo dice el cliente.

### Salas que si son fuente

| Sala | Archivo | Quien esta |
|---|---|---|
| 01/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-01-reunion-cliente.md` | Desde [10:14]: Maria Jesus, Fran y Lupe. Mario no entro. Antes de [10:14] solo Carlos y Sergio. |
| 06/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md` | Pablo hasta que se va [09:27]. Despues Maria Jesus con Carlos y Sergio. Maria Jesus se corta cerca de [30:54]. |
| 13/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-13-gosocket-almahue.md` | Pablo, Carlos y Maria Jesus. |
| 14/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md` | Maria Jesus, Mario, Rodrigo y Lafran. Presentan Carlos y Sergio. |

### Salas de octubre que no aplican

- `docs/reuniones/transcripciones/transcripcion-2026-10-13-interna-carlos-sergio.md`. Solo Carlos y Sergio. Hablan de deploy, de QA y de que la proforma no cree una hija. No es fuente.
- `docs/reuniones/transcripciones/transcripcion-2026-10-14-jose-sergio.md`. Jose y Sergio, interno. Hablan de asociacion tecnica, tracking y botones. No es fuente.

## Indice

| Caso | Tema |
|---|---|
| CU-01 | Condiciones de pago del neto y del IVA, editables |
| CU-02 | Fichas de proveedor y cliente separadas, que conversan por RUT |
| CU-03 | Consulta por RUT con movimientos de proveedor y de cliente |
| CU-04 | Anular un elemento de costo sin borrar el historial |
| CU-05 | Historico del Banco Central, sin pisar documentos |
| CU-06 | Comprobante en peso, dolar y yuan |
| CU-07 | Auxiliar = RUT sin digito verificador |
| CU-08 | Glosa = comentario, repetida en cada linea |
| CU-09 | En la venta, la cuenta es IVA debito |
| CU-10 | Avisar a quien debe crear la OC que falta |
| CU-11 | OC madre de insumos, solo informativa |
| CU-12 | OC de servicio, uno a uno y con factura directa |
| CU-13 | La guia en bodega actualiza stock y nace la OC hija |
| CU-14 | Libro de guias solo en insumos |
| CU-15 | La factura de insumos se asocia a las OC hijas |
| CU-16 | Compras solo lista hijas ya recepcionadas |
| CU-17 | Quien ve la madre y quien ve la hija |
| CU-18 | El saldo de la madre se ve en insumos |
| CU-19 | Si la guia no cabe, se pide modificar la madre |
| CU-20 | La madre se edita una vez, para arriba o para abajo, con aprobacion |
| CU-21 | La madre la crea el jefe; la hija, el administrativo |
| CU-22 | Cadenas distintas para insumos y para servicios |
| CU-23 | Toda OC pasa por aprobacion, desde monto cero |
| CU-24 | Devolucion a proveedor solo en ALM |
| CU-25 | Nomina semanal, historico y banderas |
| CU-26 | Ficha de contratista con codigo correlativo |
| CU-27 | El flujo de contratista no tiene contrato |
| CU-28 | Ingreso diario de la labor |
| CU-29 | Mantenedores de cuartel y faena |
| CU-30 | Armar la proforma eligiendo ingresos |
| CU-31 | La que se aprueba es la proforma |
| CU-32 | La proforma no se factura parcial |
| CU-33 | Enviar la proforma al contratista |
| CU-34 | Editar la proforma aprobada; no editarla si ya hay factura |
| CU-35 | Ver proformas pendientes y aprobadas |
| CU-36 | El DTE se asocia en compras; el costo se imputa en contratistas |
| CU-37 | Cuenta mano de obra contratista |
| CU-38 | Centralizacion del mes en un asiento |
| CU-39 | Al asociar la factura, facturas por recibir contra proveedor |
| CU-40 | Precio estimativo en el trato, editable despues |
| CU-41 | El cierre de mes trabaja contra proformas |
| CU-42 | El correo de la OC es interno |
| CU-43 | PDF y Excel de los reportes contables |
| CU-44 | El pago del contratista es el de la factura asociada |

Total: 44 casos.

---

## Casos

### CU-01. Condiciones de pago del neto y del IVA, editables

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [18:32] y [18:37].
- Que pasa: en la ficha del proveedor el neto y el IVA tienen condicion de pago distinta. Los dias no vienen solo de una lista: ella tiene que poder poner, por ejemplo, 45 dias. Esa condicion despues se sugiere en los otros modulos, y ahi tambien se puede editar.
- Documento: ficha de proveedor. La sugerencia llega a la OC y a la factura.
- Que debe quedar: dos plazos independientes (neto e IVA), ingreso manual de dias, valor sugerido y no bloqueado en el documento que lo use.
- Salas de octubre: ninguna otra sala del mes lo repite ni lo contradice.
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [12:16] y [13:04], sala de Mario y Lupe. El maestro del proveedor trae las condiciones, incluido el plazo del IVA, y en la OC se pueden editar.

### CU-02. Fichas de proveedor y cliente separadas, que conversan por RUT

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [18:50], [19:26], [19:47], [20:21] y el cierre en [24:38] a [26:25].
- Que pasa: al principio pide una ficha general donde se marque proveedor, productor o cliente, porque si alguien es las dos cosas se usan los mismos datos. Despues de un corte de audio cierra otra cosa: no hace falta un formulario unico. La mayoria (habla de un 98 por ciento) es solo proveedor o solo cliente. Un proveedor si puede pasar a ser tambien cliente. Lo conveniente es dejar las fichas separadas y que conversen: si el RUT ya existe como proveedor, al crear el cliente el mismo RUT trae la informacion, para que el nombre no quede distinto. La creacion de proveedor o de cliente queda en una jefatura, por seguridad. Hoy la hace ella.
- Documento: ficha de proveedor y ficha de cliente.
- Que debe quedar: dos fichas, no una sola pantalla de alta. Al escribir un RUT que ya existe en la otra ficha, se copian los datos. Un mismo RUT puede quedar como proveedor y como cliente. La alta no es de un digitador cualquiera: es de jefatura.
- Salas de octubre: la frase de las [18:50] (ficha unica con un check) queda reemplazada por el cierre de la misma sala, [25:50]. Ninguna sala posterior de octubre vuelve al tema.
- Apoyo anterior: sin caso de octubre que lo repita. El productor como tercer tipo lo nombra solo en [19:26] y no lo cierra. Ver la lista de temas que no son caso.

### CU-03. Consulta por RUT con movimientos de proveedor y de cliente

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [27:09] a [27:21].
- Que pasa: si consulta un RUT en la reportabilidad, tienen que salir todos los movimientos de ese RUT, sea como proveedor o como cliente.
- Documento: consulta / reportabilidad por RUT. Toca documentos de compra y de venta de esa contraparte.
- Que debe quedar: una consulta del RUT no parte el historial en dos personas.
- Salas de octubre: ninguna otra.
- Apoyo anterior: no citado. Encaja con CU-02, que es la misma sala.

### CU-04. Anular un elemento de costo sin borrar el historial

- Quien: voz sin nombre. Sala del 01/10 con Maria Jesus, Fran y Lupe. Carlos muestra la edicion de un elemento de costo y la sala responde.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [17:14] a [17:45].
- Que pasa: el estado anulado deja el elemento no disponible para usarlo, y sigue visible. No se borra la historia.
- Documento: mantenedor de elemento de costo.
- Que debe quedar: vigente o anulado. Anulado no se ofrece para imputar y no desaparece del historial.
- Salas de octubre: ninguna otra. Carlos ofrece mas estados "si se necesita"; la sala no pide un tercer estado.
- Apoyo anterior: no citado para este mantenedor.

### CU-05. Historico del Banco Central, sin pisar documentos

- Quien: voz sin nombre de la sala del 01/10 (Maria Jesus, Fran y Lupe). Pregunta por el yuan y por si el historico transforma lo ya cargado. Acepta la respuesta de que no pisa los otros modulos.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [28:43] a [29:49].
- Que pasa: quieren traer el historico de indicadores (el ejemplo es el yuan) sin tener que cargar antes la base de Almahue. El historico es consulta. No reescribe el tipo de cambio ya usado en los demas modulos.
- Documento: monedas e indicadores del Banco Central. No es un asiento.
- Que debe quedar: carga de historico por moneda ya registrada y por rango de fechas, tomada del Banco Central. Los documentos ya grabados conservan su tipo de cambio.
- Salas de octubre: el 14/10 [56:51] Carlos muestra peso, dolar y yuan en el comprobante. Eso es CU-06, no una correccion de este caso.
- Apoyo anterior: `transcripcion-2026-08-28-tesoreria-mj-lupe.md`, Maria Jesus (speaker 01, el archivo no trae minuto en esas lineas): toda la contabilizacion en tres monedas y el tipo de cambio llamado al Banco Central. El reloj de esa transcripcion viene vacio; se cita el archivo.

### CU-06. Comprobante en peso, dolar y yuan

- Quien: voz sin nombre, criterio de contabilidad, en la sala del 01/10 con Maria Jesus, Fran y Lupe. El alcance lo da esa voz; Carlos solo confirma.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [32:41] a [33:38].
- Que pasa: aunque el movimiento venga en otra moneda, la contabilidad de ellos es siempre peso y dolar. Si nadie digita el tipo de cambio, hay que tomar el del dia en el Banco Central, porque el movimiento diario siempre tiene tipo de cambio. Ese valor se puede modificar cuando ingresan una factura o un caso puntual. Ademas piden el yuan en paralelo, como tercera columna. Vale para todos los casos.
- Documento: comprobante de asiento (el que estaban mirando era el de una venta contabilizada).
- Que debe quedar: tres columnas, peso, dolar y yuan, en el comprobante. Tipo de cambio del dia propuesto desde el Banco Central, editable al ingresar el documento.
- Salas de octubre: el 14/10 [56:51] Carlos dice que el comprobante muestra las monedas pedidas (peso, dolar y yuan). La sala no corrige el pedido del 01/10.
- Apoyo anterior: `transcripcion-2026-08-28-tesoreria-mj-lupe.md`, Maria Jesus, misma cita que CU-05. `transcripcion-2026-09-24-reunion-cliente.md` [22:33] y [31:48], sala de Lupe, Fran y Sigrid: registro en pesos, dolares y yuan.

### CU-07. Auxiliar = RUT sin digito verificador

- Quien: voz sin nombre de la sala del 01/10. Carlos pregunta que es el valor "aux" y la sala lo define.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [33:48] a [34:02].
- Que pasa: el auxiliar del comprobante es el RUT de la contraparte (en el ejemplo, el cliente), sin digito verificador.
- Documento: comprobante y mayor.
- Que debe quedar: auxiliar = RUT sin DV.
- Salas de octubre: ninguna otra lo contradice.
- Apoyo anterior: `transcripcion-2026-08-28-tesoreria-mj-lupe.md`, Maria Jesus, al distinguir la cuenta de proveedores por auxiliar y tipo de documento. Reloj vacio en ese archivo.

### CU-08. Glosa = comentario, repetida en cada linea

- Quien: voz sin nombre de la sala del 01/10. Revisa el comprobante que ellos habian enviado y el que arma el ERP.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [37:23] a [38:18], [38:39] y [39:36] a [40:16].
- Que pasa: la glosa que les sirve es la de abajo del comprobante de ejemplo: numero de factura y un poco de la descripcion, o sea el comentario que ingresan al documento. Con eso reconocen el asiento en la reportabilidad sin abrir el comprobante. Acuerdan dejar ese comentario, no una glosa larga que repita tipo, folio y tipo de cambio (eso ya esta al lado). El nombre del dueno que salia en el ejemplo no va. El mismo comentario tiene que repetirse en la linea de ingreso, en la de cliente y en la de IVA. En el mayor de cliente tiene que leerse a que movimiento corresponde.
- Documento: comprobante de venta y libro mayor.
- Que debe quedar: una glosa, la del comentario ingresado, copiada en todas las lineas del asiento. Sin el nombre del dueno. Sin rellenar la glosa con datos que ya van en otras columnas.
- Salas de octubre: ninguna otra vuelve a la glosa.
- Apoyo anterior: no se cita una frase anterior de octubre ni una de cliente que fije este texto. El comprobante de ejemplo lo habian mandado ellos; en la sala dicen que hay que revisarlo (`[36:00]` a `[37:23]`).

### CU-09. En la venta, la cuenta es IVA debito

- Quien: voz sin nombre de la sala del 01/10.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [38:52].
- Que pasa: en el comprobante de venta, la linea que salia como caja tiene que ser IVA debito.
- Documento: asiento de venta.
- Que debe quedar: la cuenta de IVA del asiento de venta es IVA debito, no caja.
- Salas de octubre: ninguna otra.
- Apoyo anterior: no citado.

### CU-10. Avisar a quien debe crear la OC que falta

- Quien: voz sin nombre de la sala del 01/10. Confirma el aviso que Carlos muestra en el libro de compras.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [46:12] a [46:55].
- Que pasa: si el documento recibido no trae la OC, ellos tienen que poder avisar a la persona que deberia crearla. Carlos enumera proveedor no creado, OC inexistente o OC con diferencia, destino elegible, aviso interno mientras el correo no este conectado, y que el aviso quede en la trazabilidad. La sala dice que si, que notificarian a quien crea la OC, y cierra con "buenisimo".
- Documento: factura recibida en el libro de compras.
- Que debe quedar: desde el documento sin OC (o sin proveedor, o con diferencia) se elige un usuario del sistema y se le envia el aviso. El aviso queda registrado en la trazabilidad de ese documento. No queda como pedido de esta sala el texto del correo ni el servidor SMTP: Carlos dice que el correo aun no esta conectado y la sala acepta el aviso interno.
- Salas de octubre: el 14/10 rearma el flujo de insumos (CU-13 a CU-20) y no deroga este aviso.
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [38:34], [42:12] y [45:06], Mario y Lupe. Lupe elige al usuario (ejemplo: Mario), le manda el aviso para que genere la OC, y quieren trazabilidad porque el otro puede decir que nunca le llego. [13:42]: si el proveedor no esta en el maestro, la factura queda en alerta para contabilidad y no se mueve hasta registrarlo.

### CU-11. OC madre de insumos, solo informativa

- Quien: voz sin nombre el 01/10 (sala Maria Jesus, Fran y Lupe). El 14/10 lo cierra Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [47:20] a [47:43]. `transcripcion-2026-10-14-presentacion.md` [29:09], [34:43], [45:49] y [46:58].
- Que pasa: la OC madre sirve para negociar con el proveedor de materiales. Es un dato informativo. No se contabiliza, no mueve el gasto y no se refleja en un modulo que no sea insumos. A compras, para asociar factura, van las hijas.
- Documento: OC madre de insumos.
- Que debe quedar: la madre no genera asiento y no aparece como documento asociable en el libro de compras. Vive en insumos.
- Salas de octubre: el 01/10 y el 14/10 dicen lo mismo. El 14/10 precisa que el flujo de madre e hija es solo insumos.
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [27:52] y [28:50], Mario y Lupe. La hija se contabiliza; la madre no.

### CU-12. OC de servicio, uno a uno y con factura directa

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [55:22] a [55:33]. `transcripcion-2026-10-14-presentacion.md` [52:18] a [52:35].
- Que pasa: guia solo en insumos. Lo demas entra con factura directa. Hay dos tipos de OC: insumos y servicios. La de servicio se aprueba y se recepciona, y es siempre una a una. La que llega por partes es la de insumos.
- Documento: OC de servicio. Factura recibida.
- Que debe quedar: una OC de servicio no se parte en madre e hijas ni espera guia. Una recepcion, una factura.
- Salas de octubre: el 01/10 dice que lo unico con guia es el insumo. El 14/10 pone el nombre "servicios" y la regla uno a uno. No se contradicen.
- Apoyo anterior: `transcripcion.md` (Reu1, as-is Agrosoft; los relojes de speaker pueden estar corridos), speaker 00 cerca de [08:51]: la OC de servicios, al recepcionarla, reconoce el gasto contra facturas por recibir servicios. Es el as-is, no el pedido de octubre.

### CU-13. La guia en bodega actualiza stock y nace la OC hija

- Quien: Maria Jesus.
- Archivo y minuto: pedido que manda, `transcripcion-2026-10-14-presentacion.md` [35:06] a [40:12], en especial [37:50], [38:21], [39:35] y [39:56].
- Que pasa: la OC hija de insumos siempre nace con la recepcion de la guia de despacho. Primero existe la OC madre. Cuando llega el despacho, en insumos se ingresa el material a bodega con esa guia, y esa misma guia genera la hija. Pueden llegar 10 guias en el mes y una sola factura. El ejemplo de ella: la madre son 100 cajas o 100.000 pesos, y un despacho de 10.000 tiene que quedar amarrado a la guia para que exista la hija. El saldo de la madre es parcial.
- Documento: guia de despacho recibida, movimiento de bodega, OC hija, OC madre.
- Que debe quedar: sin madre no hay guia asociable. Cada guia recepcionada en insumos actualiza la bodega y crea una hija de esa madre. Varias guias del mes pueden corresponder a una factura (la asociacion de la factura es CU-15, no de la guia).
- Salas de octubre, frase anterior que no manda: `transcripcion-2026-10-01-reunion-cliente.md` [55:49] a [56:45]. Ahi Maria Jesus dice que el material llega con guia, que la guia entra el material para que la bodega quede al dia, y que la asociacion con la OC la hace la factura de fin de mes, no la guia. El 14/10 gana: la guia si se asocia a la madre, porque de ahi nace la hija; la factura se asocia a las hijas, no a la madre. En el 01/10 [57:10] el control del jefe de abastecimiento es la guia fisica. En el 01/10 [57:35] ella dice que en el RCV del SII las guias no aparecen. Eso no queda convertido en un pedido de sincronizar la guia desde GoSocket (ver temas que no son caso).
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [32:37] y [34:04], y `transcripcion-2026-09-24-reunion-cliente.md` [27:13] a [28:15]. Ahi la hija nacía al asociar la factura parcial, digitando cantidades de la madre. El 14/10 mueve el nacimiento de la hija a la guia en bodega. Esas salas quedan como apoyo del problema (recepcion por partes), no como el mecanismo que manda.

### CU-14. Libro de guias solo en insumos

- Quien: Maria Jesus. Sergio propone un libro de guias aparte del libro de compras; ella fija donde vive.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [37:35] a [37:46], [38:05], [50:42] y [51:17] a [51:24].
- Que pasa: el libro de compras no es el lugar de la guia. El libro de guias, emitidas y recibidas en la propuesta de Sergio, queda en insumos bodega. Bodega tiene que poder ver las guias de despacho recibidas.
- Documento: libro de guias, modulo de insumos.
- Que debe quedar: guia visible y operable en insumos. El libro de compras no lista guias de despacho.
- Salas de octubre: el 01/10 no pide un libro de guias; pide la recepcion fisica en bodega (CU-13, frase anterior).
- Apoyo anterior: no hay un libro de guias pedido antes con este corte. Reu4, `transcripcion-reunion4.md` speaker 01 [12:48], as-is: en ALM los materiales se ven en bodega, con devoluciones, traspasos e ingreso de compra.

### CU-15. La factura de insumos se asocia a las OC hijas

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [36:23] a [36:47], [39:03] a [40:22] y [41:01].
- Que pasa: cuando llega la factura, las hijas ya existen porque nacieron con la guia. En el libro de compras ella asocia esas hijas a la factura. No asocia la guia. No quiere un calce "por monto": quiere el listado de lo que llego de ese proveedor. El ejemplo que ella acepta es Cartocor, factura 20, ver lo que hay de ese proveedor. Diez guias pueden ser cinco hijas contra una factura, y la madre puede seguir con saldo.
- Documento: factura recibida en libro de compras. OC hija.
- Que debe quedar: desde la factura se eligen N OC hijas del mismo proveedor, ya nacidas de una guia. No se elige la guia ni la madre. No basta un match solo por monto.
- Salas de octubre: corrige la demo de la misma sala, [26:35] a [30:07], donde Carlos y Sergio muestran la hija creandose al asociar una factura de monto menor en el libro de compras. Maria Jesus, mas adelante, dice que la hija nace con la guia en bodega. Manda esa frase posterior.
- Apoyo anterior: el mecanismo "la hija nace de la factura" esta en septiembre (cita de CU-13). No manda.

### CU-16. Compras solo lista hijas ya recepcionadas

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [49:56] a [50:05] y [55:16] a [55:24].
- Que pasa: en compras, para asociar, solo entran las que ya estan recepcionadas. Si hay mil OC que no estan aprobadas o no estan recepcionadas, en ese modulo no se ven: "es como que no existe". En compras no van las pendientes ni las que estan solo aprobadas. Tienen que estar listas para contabilizar.
- Documento: libro de compras, OC hija.
- Que debe quedar: el listado de asociacion de compras no muestra madres, ni OC sin recepcion, ni OC solo aprobadas.
- Salas de octubre: coherente con CU-11 y CU-15. No hay frase en contra.
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [39:09], Mario y Lupe: al asignar, no mostrar OC ya asociadas a otra factura, y si listar las de ese proveedor pendientes de asignacion.

### CU-17. Quien ve la madre y quien ve la hija

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [46:35] a [47:18] y [54:42] a [56:02].
- Que pasa: una voz de la sala (sin nombre; estan Maria Jesus, Mario, Rodrigo y Lafran) propone un modulo de OC madre aparte. Maria Jesus cierra el corte: insumos es un mundo aparte. Las madres no pasan al modulo de compras para asociarlas. Ahi solo van las hijas con guia. Hay gente con acceso solo a insumos, no a compras: el administrativo de abastecimiento tiene que ver sus OC. En insumos se ven la madre y la hija. En compras se ven las hijas. Las guias no se ven en el libro de compras.
- Documento: OC madre, OC hija, permisos de insumos y de compras.
- Que debe quedar: insumos muestra madre e hija. Compras muestra hijas listas para contabilizar (CU-16). Un usuario solo de insumos puede ver las OC de ese mundo. La madre no se mezcla en el libro de compras.
- Salas de octubre: el 01/10 [47:26] ya decia que la madre no se refleje fuera de insumos.
- Apoyo anterior: no citado como permiso. El contenido contable de la madre esta en CU-11.

### CU-18. El saldo de la madre se ve en insumos

- Quien: voz sin nombre pregunta si hay que mostrar cuanto falta para cerrar la madre. Maria Jesus responde.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [47:48] a [48:34].
- Que pasa: el pendiente de la madre se ve en insumos, no en compras. Quien calza la factura con la OC hija solo necesita que calcen. No entra a ver si llego material o si falta por llegar.
- Documento: OC madre en insumos. Factura en libro de compras.
- Que debe quedar: insumos muestra el saldo de la madre. El calce de la factura no exige ese saldo en pantalla.
- Salas de octubre: ninguna otra.
- Apoyo anterior: `transcripcion-2026-09-24-reunion-cliente.md` [28:01], Lupe, Fran y Sigrid: el saldo de la madre se rebaja con las hijas ya recepcionadas. El lugar (insumos, no compras) lo fija el 14/10.

### CU-19. Si la guia no cabe, se pide modificar la madre

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [41:27] a [41:35] y [49:39] a [49:56].
- Que pasa: el control es al recepcionar, no al calzar la factura. Si abastecimiento no puede recepcionar la guia porque no queda cupo en la madre, ahi pide que le modifiquen la OC. El usuario se va a encontrar el problema en la recepcion, cuando no haya espacio.
- Documento: guia de despacho, OC madre.
- Que debe quedar: la recepcion de la guia no puede pasar el saldo de la madre. El desborde se resuelve pidiendo la edicion de la madre (CU-20), antes de asociar la factura.
- Salas de octubre: ninguna otra.
- Apoyo anterior: `transcripcion-2026-09-24-reunion-cliente.md` [28:23] a [29:30]. Cuando la factura ya no cabe, el usuario pide modificar la madre.

### CU-20. La madre se edita una vez, para arriba o para abajo, con aprobacion

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [30:44] a [32:08] y [43:32] a [45:10].
- Que pasa: la madre se puede cambiar una sola vez, y ese cambio es el cierre: ya no va a llegar mas material, o hay que adicionar. No es para corregirla cada vez que aparece un error. Si hace falta otro cambio, se pide a contabilidad. Esa unica edicion pasa por aprobacion tanto si el monto baja como si sube. Una recepcion parcial normal no es esa edicion: si se negociaron 100 y van 50 entregadas, la madre sigue abierta y no vuelve a la cadena. El cierre hacia abajo es cuando ellos le dicen al proveedor que negociaron 100 cajas y solo necesitan 50, porque la compra nacio de una estimacion de fruta. Lo pide el usuario que pidio la madre. La aprobacion de ese cierre es para poder dar la madre por cerrada.
- Documento: OC madre.
- Que debe quedar: una edicion de cierre, para arriba o para abajo, que recorre la cadena. Sin cierre automatico al recibir una parte. Un segundo cambio no queda en la misma via: lo pide contabilidad. La hija no se aprueba de nuevo por el solo hecho de nacer (la madre ya estaba aprobada; ver CU-21).
- Salas de octubre, frase anterior que no manda: `transcripcion-2026-10-01-reunion-cliente.md` [47:52]. Carlos dice que si el monto de la OC sube, vuelve a la cadena. La sala contesta "si". No habla del monto que baja. El 14/10 Maria Jesus lo deja explicito: edicion para abajo o para arriba, con aprobacion. Dentro del 14/10, [32:03] y el cierre de [43:59] se leen juntos: la aprobacion es de la edicion de cierre, no de cada recepcion parcial.
- Apoyo anterior: `transcripcion-2026-09-23-dudas-cliente.md` [36:20] a [36:35]. Mario y Lupe: la edicion es una vez y, si el monto aumenta, pasa por la cadena "siempre y cuando cumpla con las condiciones". El 14/10 saca ese "siempre y cuando" para la edicion (ver CU-23). `transcripcion-2026-09-24-reunion-cliente.md` [21:21] a [22:22]: si se pasa o queda corto, la madre se edita y vuelve al flujo, "tanto para mas y para menos". [29:03]: la hija no recorre la cadena porque la madre ya estaba aprobada.

### CU-21. La madre la crea el jefe; la hija, el administrativo

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [41:07], [52:42] a [53:22].
- Que pasa: la madre se aprueba una vez, porque el real esta en las hijas. La crea el jefe. La hija la genera el administrativo de abastecimiento, en insumos, al recepcionar. En [37:50] dice que la hija "se apruebe con la guia": nace cuando llega el despacho, no con una segunda cadena.
- Documento: OC madre, OC hija, guia.
- Que debe quedar: alta de la madre restringida al jefe, con una aprobacion. Alta de la hija en la recepcion de la guia, por el administrativo de insumos, sin recorrer otra vez la cadena de la madre.
- Salas de octubre: el 01/10 no dice quien crea cada una.
- Apoyo anterior: `transcripcion-2026-09-24-reunion-cliente.md` [29:37] a [29:48], la hija queda aprobada porque es parte de la madre ya aprobada.

### CU-22. Cadenas distintas para insumos y para servicios

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [51:42] a [52:40].
- Que pasa: las reglas de aprobacion de OC tienen que separarse. Un flujo para insumos y otro para servicios. Carlos pregunta si ademas se marca en la escala quien puede generar la OC de insumos. Ella confirma los dos tipos y quien crea la madre y la hija (CU-21). No dice que un mismo grupo no pueda existir en los dos flujos: eso lo hablan Carlos y Sergio el 06/10, sin ella (ver temas que no son caso).
- Documento: reglas de aprobacion de OC.
- Que debe quedar: la cadena de una OC de insumos no es la misma pieza que la de una OC de servicio.
- Salas de octubre: el 06/10, despues del corte de Maria Jesus, Carlos y Sergio dicen que un grupo no puede servir a la vez para OC y para proforma. Ella no lo confirma. No entra en este caso. La proforma tiene su propia aprobacion en CU-31.
- Apoyo anterior: no citado para esta separacion de tipos.

### CU-23. Toda OC pasa por aprobacion, desde monto cero

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [32:29] a [33:48].
- Que pasa: ella estaba de vacaciones cuando se dejo la aprobacion automatica y no esta de acuerdo. Aunque sean 5 pesos, tiene que pasar por aprobacion. En Almahue llegan muchas facturas de 10.000 o 15.000 pesos, del orden de 300 al mes, y por eso se habia pensado un tramo automatico. El problema es que en ese tramo tambien caerian almuerzos o libreria, que no deberian aprobarse solos. Acepta que no exista un salto de la cadena y que el primer eslabon parta desde cero (el ejemplo de Carlos es Felipe desde 0 hasta 500.000: el nombre y el tope son ejemplo, no un monto pedido por ella). "Yo dejaria todo con aprobacion."
- Documento: OC, cadena de aprobacion.
- Que debe quedar: ninguna OC queda aprobada solo por estar bajo un monto. El primer aprobador cubre desde cero. Siguen pudiendo existir escalas por monto para saber quien firma, pero nadie se salta la cadena.
- Salas de octubre: no hay otra sala de octubre donde el cliente pida el tramo exento. La frase que ella rechaza es una decision tomada mientras estaba de vacaciones.
- Apoyo anterior, en contra de este caso y por eso no manda: `transcripcion-2026-09-24-reunion-cliente.md` [06:10] a [06:17], Lupe, Fran y Sigrid, sin Maria Jesus. Ahi se nombra "aprobacion automatica" como flujo normal si el monto ya no llega al gerente. La frase esta sucia. Maria Jesus el 14/10 la deja sin efecto. `transcripcion-2026-09-23-dudas-cliente.md` [36:35] condiciona la re-aprobacion a que el aumento "cumpla con las condiciones" de la cadena. El 14/10, para no saltarse la cadena, manda CU-23.

### CU-24. Devolucion a proveedor solo en ALM

- Quien: voz sin nombre de la sala del 01/10 (Maria Jesus, Fran y Lupe), respondiendo a Carlos.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [59:35] a [01:00:18].
- Que pasa: si se rechaza una factura y hay que devolver material, eso pasa, y solo en ALM. Es una devolucion a proveedor. En Almahue exportacion no hay reintegro de bodega: compran lo justo que venden, porque es fruta. Carlos propone configurarlo por empresa. La sala confirma el corte entre las dos empresas.
- Documento: movimiento de bodega, devolucion a proveedor.
- Que debe quedar: ALM puede devolver material al proveedor. Almahue exportacion no usa ese reintegro. La diferencia es por empresa, no un flujo unico para las dos.
- Salas de octubre: ninguna otra.
- Apoyo anterior: `transcripcion-reunion3.md` speaker 01 [07:37] y [07:47], as-is. La devolucion al proveedor se identifica como salida a proveedor. El reloj de esa transcripcion es el del speaker.

### CU-25. Nomina semanal, historico y banderas

- Quien: Lupe. Carlos le pregunta si queda aprobado y la sala dice que si. El atribuye el visto bueno a Lupe y nadie lo corrige.
- Archivo y minuto: `transcripcion-2026-10-01-reunion-cliente.md` [48:21] a [49:59].
- Que pasa: la nomina que habian visto con Lupe y Mario queda asi: periodo actual partido en semanas, con cuantos van pendientes y cuantos atrasados; historico por rango de fechas; banderas configurables (a los 7 dias atrasado, a los 30 critico, a los 90 otra bandera, y se puede agregar otra con color y nombre); filtro para ver solo pendientes o todos.
- Documento: nomina semanal de pago.
- Que debe quedar: esas dos vistas (actual e historico), los conteos, las banderas con umbral, nombre y color configurables, y el filtro de pendientes. Los dias 7, 30 y 90 son el ejemplo que ella aprueba como punto de partida, no un candado: el umbral se configura.
- Salas de octubre: ninguna otra lo toca.
- Apoyo anterior: `transcripcion-2026-08-28-tesoreria-mj-lupe.md`, Lupe y Maria Jesus, nomina semanal de pagos. Reloj vacio en ese archivo. `transcripcion-2026-09-23-dudas-cliente.md` [10:39], Mario y Lupe, como llegar a la nomina desde compras.

### CU-26. Ficha de contratista con codigo correlativo

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [14:13] a [14:48].
- Que pasa: hace falta ingresar la ficha del contratista. El codigo es un correlativo: si hay 10, el siguiente es el 11. No es el RUT. El codigo de proveedor si es el RUT. La ficha lleva codigo, RUT, nombre, direccion, y queda registrada la persona que la crea.
- Documento: ficha de contratista.
- Que debe quedar: maestro propio, codigo numerico correlativo, RUT, nombre, direccion y usuario de alta.
- Salas de octubre: el 14/10 [06:49] Carlos muestra una etiqueta cuando el RUT del contratista coincide con un proveedor. Ella no lo pide en el 06/10. No se eleva a caso (ver temas que no son caso).
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [36:51], as-is Agrosoft. El maestro pide nombre y RUT. El correlativo distinto del RUT es pedido de octubre, no del as-is.

### CU-27. El flujo de contratista no tiene contrato

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [12:23] a [13:03].
- Que pasa: el flujo que adelanta esta pensado en el area agricola, porque la exportadora tiene poco contratista. Se crea el contratista, se hacen los registros diarios, se emite la proforma, pasa a aprobacion, a facturacion y a pago. El contrato se salta: en Agrosoft es necesario y en AgroSmart no. Van a una fusion de los dos, y en este punto se quedan con AgroSmart.
- Documento: no hay documento contrato en el flujo.
- Que debe quedar: el ingreso diario no exige un contrato vigente ni un folio de contrato.
- Salas de octubre: ninguna sala posterior vuelve a pedir el contrato.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [01:06], as-is Agrosoft. Ahi el contrato si es un paso, y ellos lo viven como un paso de mas. El 06/10 pide no copiarlo.

### CU-28. Ingreso diario de la labor

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [14:51] a [16:36].
- Que pasa: el ingreso diario parte eligiendo empresa y temporada. El predio ella lo queria sacar o dejar no obligatorio: queda opcional para las dos empresas. Agricola lo necesita; ALM no. ALM necesita saber si es jornal o a trato. Mas adelante quieren crear mas empresas, y el funcionamiento tiene que ser transversal. El ingreso lleva fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duracion, valor unitario del trato o de la jornada, cantidad y total. El trabajador no es necesario.
- Documento: ingreso diario de contratistas.
- Que debe quedar: esos campos. Predio opcional. Sin trabajador obligatorio. Jornal o a trato como forma de pago. Sirve para ALM y para agricola, y no queda amarrado a una sola empresa.
- Salas de octubre: el 14/10 [06:03] Carlos muestra sector y faena como datos opcionales. El unico opcional que ella pide con esa palabra es el predio. Sector, cuartel y faena siguen siendo datos del ingreso (la faena, ademas, tiene mantenedor: CU-29).
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [03:03], as-is AgroSmart. Empresa, fecha, cuartel, faena, trato o jornada, y la unidad sale segun la forma de pago.

### CU-29. Mantenedores de cuartel y faena

- Quien: Maria Jesus. El 14/10 una voz sin nombre de la sala (Maria Jesus, Mario, Rodrigo y Lafran) confirma que al elegir la labor aparece la actividad.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [16:39] a [17:22]. `transcripcion-2026-10-14-presentacion.md` [16:24].
- Que pasa: cuartel y faena no se escriben a mano: tienen mantenedor. Tambien el contratista (eso ya es CU-26). Por el lado de ALM las faenas son puntuales: servicio administrativo, armado de cajas. El 14/10 la sala dice que la labor queda parametrizada y la actividad sale sola, y que eso les evita buscar a que labor correspondia.
- Documento: mantenedor de cuartel, mantenedor de faena / labor, ingreso diario.
- Que debe quedar: cuartel y faena se eligen de un mantenedor. Hay faenas de agricola y faenas puntuales de ALM. Al elegir la labor, la actividad queda determinada.
- Salas de octubre: el 06/10 pide el mantenedor. El 14/10 confirma labor y actividad automatica. No hay frase en contra.
- Apoyo anterior: `transcripcion.md` (Reu1, as-is; relojes pueden estar corridos), speaker 00 [39:50]. No van a tener el modulo de mano de obra, y la labor y la actividad hay que parametrizarlas en contratistas. `transcripcion-reunion2.md` speaker 00 [01:45]: en Agrosoft la actividad depende de acordarse en que faena esta, y el precio del tarifario no se puede tocar. El mantenedor de octubre responde a ese as-is.

### CU-30. Armar la proforma eligiendo ingresos

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [13:14] a [13:54], [17:26] a [17:45], [19:43] a [20:10] y [26:33] a [26:51]. `transcripcion-2026-10-14-presentacion.md` [12:50] a [13:07].
- Que pasa: la proforma no es una por factura. Son varios ingresos diarios. El ingreso diario es el detalle. Ella elige cuales van a una proforma: de 30 ingresos puede armar 2 o 3 proformas. Puede ser una proforma diaria, una semanal, o agrupar por rango de fecha o por labor. Al usarse en una proforma, ese ingreso ya no queda disponible para otra. En el mes un contratista puede tener varias proformas, y varias proformas se asocian a una factura. La proforma es "como la orden de compra" del contratista: no se convierte en una OC de compras.
- Documento: ingreso diario, proforma.
- Que debe quedar: seleccion multiple de ingresos de un contratista, total de lo seleccionado, y bloqueo del ingreso ya usado. Una proforma no se transforma en OC.
- Salas de octubre: el 14/10 ella repite que cinco ingresos se agrupan en una proforma. El 01/10 [54:12] Sergio deja abierta la duda de si la proforma se convierte en OC. El 06/10 la responde: es otro documento, asociable a la factura igual que la OC (CU-36).
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:26] y [03:51], as-is. Agrosoft deja una proforma por mes y no deja asociar dos proformas a una factura cuando el trabajo cruza de mes. Ellos quieren elegir las labores y armar la proforma. El 06/10 pide sacar ese limite.

### CU-31. La que se aprueba es la proforma

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [18:12] a [18:27] y, la frase que manda, [24:05]. `transcripcion-2026-10-14-presentacion.md` [13:08] y [11:09].
- Que pasa: primero dice que, al guardar, el ingreso diario se va a aprobacion de la jefatura. Sergio le muestra que asi cada monto chico pasaria solo y la proforma agrupada, que puede ser grande, no. Ella ofrece elegir cuantos ingresos se mandan a aprobacion y que ahi se genere la proforma. Despues cierra: esta proforma pasa a aprobacion y, ya aprobada, se hace el match con la factura. El 14/10 repite que la aprueba el jefe de campo, y que recien ahi se asume que la labor de esa semana si se hizo. El 14/10 [09:16] la sala dice "perfecto" al ver la cadena de la proforma por tramos de monto. Los montos de la demo (5.000 y 10.000) son del ejemplo de Carlos, no un piso pedido por ella.
- Documento: proforma. Cadena de aprobacion de proforma.
- Que debe quedar: la aprobacion interna es de la proforma, por la jefatura que definan (en la sala, el jefe de campo). El ingreso diario no queda aprobado uno a uno al guardarse.
- Salas de octubre: dentro del 06/10, [18:17] no manda; manda [24:05]. El 13/10 [08:40] y el 14/10 hablan de la proforma aprobada, no del ingreso aprobado suelto.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [01:56], as-is Agrosoft. La proforma pasa a definitiva sin un filtro previo de revision. El 06/10 pone ese filtro en la aprobacion de la proforma.

### CU-32. La proforma no se factura parcial

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [25:07] a [25:48] y [29:13] a [29:33].
- Que pasa: la proforma no queda parcializada con la facturacion. Ellos eligen las proformas del periodo, le mandan el detalle al contratista y el emite la factura. La factura recibida puede tomar N proformas. El contratista tiene que tener la proforma aprobada antes de facturar, porque es una negociacion. Si el precio o la jornada no calzan, y llegan a acuerdo, se modifica la proforma en cuestion, y se modifica el ingreso diario de origen. No se factura una parte de la proforma.
- Documento: proforma, ingreso diario, factura recibida.
- Que debe quedar: una proforma se asocia completa. Varias proformas caben en una factura. Una diferencia se corrige en el ingreso de origen, no dejando un saldo facturado a medias. La asociacion a la factura exige la proforma aprobada.
- Salas de octubre: el 13/10 no abre la parcializacion. El 14/10 no la contradice. No se copia a la proforma el modelo de OC hija (CU-13): ella lo dice para la OC de insumos, no para la proforma.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:26], as-is. Mas de una proforma para una factura. El rechazo de la parcial es de octubre.

### CU-33. Enviar la proforma al contratista

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [25:52] a [28:03] y [28:38] a [30:29]. `transcripcion-2026-10-14-presentacion.md` [19:22].
- Que pasa: la proforma se la pasan al contratista y con eso el emite la factura. Les sirve mandarlas por partes, por ejemplo el avance semanal. Hoy imprimen el documento del sistema y se lo pasan. Ella dice que estaria bien un correo al contacto, una vez aprobada. El envio ya lo toman como check del contratista, salvo que el reclame precio o jornada. No hay un segundo aprobador dentro del ERP que sea el contratista. Sergio plantea que una proforma ya informada no entre en el envio siguiente del mes; ella arranca esa respuesta con "si" y explica el modelo del envio. El 14/10, al ver "notificar a contratista" con correo, la sala dice "buenisimo".
- Documento: proforma aprobada. Correo al contacto del contratista.
- Que debe quedar: desde una proforma aprobada se puede enviar al contratista, con el documento, al mail del contacto. Queda constancia de cuales ya se enviaron, para no repetirlas en el cierre siguiente. El contratista no entra al ERP a aprobar. Si reclama, se edita el origen (CU-32 y CU-34).
- Salas de octubre: el 06/10 pide el envio. El 14/10 no lo corrige. Lo que no entra: el 06/10 [31:36] en adelante, ya sin Maria Jesus, Carlos y Sergio bautizan el estado "notificada a proveedor" y dicen que solo esas se listen en compras. El 13/10 ella lista en compras las aprobadas, no las notificadas (CU-36).
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:11], as-is. Le van mandando la proforma al contratista para que facture.

### CU-34. Editar la proforma aprobada; no editarla si ya hay factura

- Quien: Maria Jesus. La pregunta del 14/10 la hace una voz sin nombre de la sala; ella responde.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [30:33] a [30:45]. `transcripcion-2026-10-14-presentacion.md` [01:00:17] a [01:01:14].
- Que pasa: si la proforma ya paso la aprobacion interna y hay que editarla, vuelve a pasar por la cadena. El 14/10: si esta aprobada, la modificacion es con solicitud. Si ya esta asociada a una factura recibida, no se edita, porque va a estar facturada. La factura es el ultimo control para no quedar con una diferencia con el contratista.
- Documento: proforma, ingreso diario, factura recibida.
- Que debe quedar: proforma aprobada y aun no facturada se puede corregir solo volviendo a aprobacion. Proforma ya asociada a factura queda cerrada a la edicion.
- Salas de octubre: el 06/10 y el 14/10 dicen lo mismo. En [01:01:09] hay una frase sucia, "orden de credito"; no alcanza para pedir una nota de credito (ver temas que no son caso).
- Apoyo anterior: no citado.

### CU-35. Ver proformas pendientes y aprobadas

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-13-gosocket-almahue.md` [05:50].
- Que pasa: en el modulo de contratistas tienen que poder ver las proformas pendientes y las aprobadas. La asociacion del DTE no se hace ahi (CU-36).
- Documento: proforma.
- Que debe quedar: listado en contratistas con esos dos estados, distinguibles.
- Salas de octubre: el 14/10 [20:19] precisa, para el traspaso contable, que el listado de gasto son las aprobadas y que la pendiente es solo informativa. No borra este listado operativo.
- Apoyo anterior: no citado.

### CU-36. El DTE se asocia en compras; el costo se imputa en contratistas

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [24:32] a [24:41]. `transcripcion-2026-10-13-gosocket-almahue.md` [05:59] a [08:54].
- Que pasa: en documentos recibidos de compras se puede asociar una proforma o una OC. El 13/10 Carlos pregunta si la asociacion del DTE va en el libro de compras o en un submodulo de contratistas. Ella dice que la asociacion de la proforma con la factura se hace en compras. La imputacion del costo se hace en contratistas, y puede hacerse aunque la factura todavia no este asociada. Primero dice que la cuenta se asigna en los dos modulos; despues cierra que la cuenta se asigna y se edita solo en contratistas, y que a compras viaja el dato. En compras tienen que aparecer, para asociar, las proformas aprobadas contra las facturas que lleguen. No exige que la factura ya exista para reconocer el costo.
- Documento: factura recibida, proforma, OC.
- Que debe quedar: en el libro de compras el usuario elige proforma o OC. La cuenta no se edita ahi. El costo de la proforma aprobada puede quedar imputado antes del calce. El listado de asociacion muestra proformas aprobadas, no un subconjunto "solo notificadas".
- Salas de octubre: el 06/10 abre la asociacion proforma u OC. El 13/10 fija el lugar. El 14/10 no lo mueve de compras. La frase de Carlos y Sergio del 06/10 [31:56], sin ella, (solo las notificadas se listan en compras) no manda.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:26], as-is. Despues de la proforma, en proveedores se asocia la proforma a la factura, filtrando tipo de compra contratista.

### CU-37. Cuenta mano de obra contratista

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [10:41] a [14:16].
- Que pasa: la cuenta del contratista va a mano de obra contratista. El detalle se analiza por centro de costo, labor y actividad. Esas dos cosas (la cuenta y el centro de costo, en el ida y vuelta con Carlos) van en el ingreso diario. Despues precisa: en el ingreso diario se asocia la labor del trabajo, no una cuenta distinta por linea. En la proforma queda el detalle de lo hecho, por labor, centro de costo y monto, y todo eso va a la cuenta mano de obra contratista.
- Documento: ingreso diario, proforma.
- Que debe quedar: una cuenta de gasto, mano de obra contratista, para el modulo. El ingreso diario guarda labor, actividad y centro de costo. La proforma no pide una cuenta por linea.
- Salas de octubre: el 13/10 [06:30] habla de gasto o costo contra facturas por recibir en cada modulo, sin nombrar la cuenta. El 14/10 le pone el nombre. No hay frase en contra.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:56] y [03:03], as-is. Al cierre, facturas por recibir contratistas contra costo por mano de obra contratista, suma de las proformas del mes. `transcripcion.md` (Reu1), speaker 00 [02:51], el mismo par de cuentas.

### CU-38. Centralizacion del mes en un asiento

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-13-gosocket-almahue.md` [07:40] a [08:49]. `transcripcion-2026-10-14-presentacion.md` [11:19] a [15:30] y [20:10] a [20:28].
- Que pasa: al cerrar el mes se centraliza todo lo ingresado en el mes que este aprobado. Es un asiento, totalizado, no uno por proforma. Reconoce el costo del mes de la proforma aunque la factura llegue con fecha del mes siguiente: el gasto de octubre queda en octubre. El asiento es mano de obra contratista contra facturas por recibir contratista. El menu se llama "Traspaso contable y cierre de mes", uno solo, debajo de auditoria. Ahi informa que mes cierra y se traspasa a contabilidad. En ese listado van todas las proformas aprobadas de contratista. La que sigue pendiente de aprobacion es solo informativa y no entra al gasto.
- Documento: asiento de centralizacion. Proformas aprobadas del mes. Cierre de mes de contratistas.
- Que debe quedar: un cierre por mes, un asiento agrupado, solo proformas aprobadas, con el gasto en el mes de la proforma y no en el mes de la factura. Menu unico de traspaso y cierre.
- Salas de octubre: el 13/10 y el 14/10 dicen lo mismo. El 06/10 no habla del asiento.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [03:03], as-is. Un asiento del mes contra mano de obra contratista, suma de las proformas del mes.

### CU-39. Al asociar la factura, facturas por recibir contra proveedor

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-13-gosocket-almahue.md` [07:55] a [08:21]. `transcripcion-2026-10-14-presentacion.md` [14:27] a [14:42].
- Que pasa: cuando en compras asocia la proforma a la factura, el calce es facturas por recibir contratista contra el nombre del contratista. La factura queda facturas por recibir contra proveedor. Junto con el asiento de CU-38, el gasto queda contra el proveedor.
- Documento: factura recibida, asiento de compras.
- Que debe quedar: el asiento del calce no vuelve a reconocer el gasto. Saca facturas por recibir y deja al proveedor. La cuenta no se reescribe en compras (CU-36).
- Salas de octubre: el 13/10 y el 14/10 coinciden.
- Apoyo anterior: `transcripcion.md` (Reu1), speaker 00 [02:51], as-is. La factura entra a facturas por recibir contratistas contra el proveedor.

### CU-40. Precio estimativo en el trato, editable despues

- Quien: voz sin nombre de la sala del 14/10 (estan Maria Jesus, Mario, Rodrigo y Lafran; el tema es el ingreso agricola). Maria Jesus responde y fija la regla.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [59:15] a [01:00:17].
- Que pasa: preguntan si un ingreso diario puede guardarse con precio cero, porque en el trato el precio a veces se fija despues, cuando sale la fruta o al cierre de mes, y necesitan tener ya la cantidad de labores. Carlos dice que precio cero tira error. Maria Jesus no deja el cero como regla: se carga un precio estimativo y despues se edita. La edicion, dice, no tiene problema.
- Documento: ingreso diario a trato.
- Que debe quedar: se puede registrar la labor antes del precio definitivo, con un valor estimativo, y corregir ese valor mas adelante. El precio cero no queda habilitado por esta sala. Si la proforma de ese ingreso ya esta aprobada o facturada, la correccion sigue CU-34.
- Salas de octubre: el 06/10 pide el valor unitario en el ingreso y no habla del cero.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [01:45], as-is Agrosoft. El precio muchas veces se sabe despues del trabajo, y el tarifario no deja modificarlo, asi que no pueden llevar el control diario. El 14/10 responde con el estimativo editable, no con un tarifario cerrado.

### CU-41. El cierre de mes trabaja contra proformas

- Quien: Maria Jesus. La pregunta la hace una voz sin nombre de la sala del 14/10.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [01:01:15] a [01:02:53].
- Que pasa: le plantean 29 dias con proforma y un dia trabajado sin proforma. Ella dice que ese dia tiene que tener su propia proforma, solo de ese dia. El cierre trabaja contra proforma. Si no, el dia queda fuera y un mes queda con 29 y otro con 31. Si cerraron el mes y quedo una proforma pendiente, tienen que abrir el mes. Hay que evitar que pase. Pueden hacer muchas proformas (habla de 20) y esas se asocian a las facturas.
- Documento: ingreso diario, proforma, cierre de mes de contratistas.
- Que debe quedar: un dia con labor y sin proforma no entra al asiento del mes. El cierre no se lo lleva solo por existir el ingreso. Si el mes se cerro y queda una proforma pendiente, el mes se puede volver a abrir. No hay un tope de una proforma por mes (eso ya esta en CU-30).
- Salas de octubre: encaja con CU-38. No lo contradice.
- Apoyo anterior: `transcripcion-reunion2.md` speaker 00 [02:26], as-is. Agrosoft ata la proforma al mes de la factura. El 14/10 separa el mes del gasto (el de la proforma) del mes de la factura, y exige proforma para cada dia que se quiera cerrar.

### CU-42. El correo de la OC es interno

- Quien: voz sin nombre. Sala del 14/10 con Maria Jesus, Mario, Rodrigo y Lafran. Habla en primera persona de la empresa ("nosotros nos mandemos entre el departamento"), asi que no es Carlos.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [22:22] a [23:10] y [26:03].
- Que pasa: el correo de la OC de compra es informacion interna, entre el departamento. Carlos muestra plantilla, destinatario usuario del sistema, copia, correos externos separados por coma y adjuntos. La sala dice "ya" y, al ver el envio, "buenisimo". El destinatario pensado es un usuario del sistema. Un correo de alguien que no esta en la plataforma se agrega a mano y no toma el nombre del destinatario.
- Documento: OC. Correo interno.
- Que debe quedar: desde la OC se avisa a un usuario interno, con el documento. Se puede agregar copia y un correo externo escrito a mano. No queda pedido, en esta frase, un portal para el proveedor.
- Salas de octubre: no es el aviso de "falta la OC" (CU-10) ni el envio de la proforma al contratista (CU-33).
- Apoyo anterior: no citado.

### CU-43. PDF y Excel de los reportes contables

- Quien: voz sin nombre de la sala del 14/10. Sergio pregunta si les pueden pasar un formato PDF. La sala dice que de todo. Otra voz, tambien sin nombre, pide ver la descarga del estado de resultados.
- Archivo y minuto: `transcripcion-2026-10-14-presentacion.md` [57:42] a [58:37] y [58:54] a [59:07].
- Que pasa: piden formato PDF de todos los reportes que estaban en pantalla: libro diario, libro mayor, balance de ocho columnas y estado de resultados. El Excel exporta las columnas de la grilla. Sergio dice que el PDF lleva arriba los datos de la empresa, el nombre del reporte y el periodo. La sala responde "ya, perfecto". El estado de resultados, que en la demo no tenia descarga, queda pedido en Excel y en PDF.
- Documento: libro diario, libro mayor, balance de ocho columnas, estado de resultados.
- Que debe quedar: cada uno de esos cuatro se exporta a PDF y a Excel. El PDF identifica empresa, reporte y periodo. El Excel respeta las columnas de la grilla.
- Salas de octubre: el 01/10 mira el PDF del comprobante (CU-06 a CU-09). No pide ahi estos cuatro reportes.
- Apoyo anterior: no citado para el formato de estos reportes.

### CU-44. El pago del contratista es el de la factura asociada

- Quien: Maria Jesus.
- Archivo y minuto: `transcripcion-2026-10-06-gosocket-contratistas.md` [13:03] y [25:22].
- Que pasa: el recorrido que ella nombra termina en facturacion y pago. El contratista emite la factura a partir de las proformas. No describe una nomina, un anticipo ni un documento de pago distinto para el contratista.
- Documento: factura recibida ya asociada a la proforma. Pago de esa factura.
- Que debe quedar: despues del calce de CU-39, el pago es el pago de esa factura de proveedor. No hay un documento de pago propio del modulo de contratistas pedido en octubre.
- Salas de octubre: ninguna otra agrega un pago especial de contratistas.
- Apoyo anterior: no se cita un pago distinto en el as-is de la proforma. La nomina semanal de CU-25 es de tesoreria general, no un cierre de este modulo.

---

## Temas oidos que no son caso

### Salas que no son fuente

- `transcripcion-2026-10-13-interna-carlos-sergio.md`. No hay cliente. No se saco ningun caso, tampoco el de "la proforma no crea hija" ni el de deploy.
- `transcripcion-2026-10-14-jose-sergio.md`. Jose y Sergio. No se saco la asociacion manual por RUT, la sugerencia por monto ni el tracking que le pedian a Diego.

### Antes de que entre el cliente, 01/10

De [00:03] a [10:14] hablan Carlos y Sergio. Importar y exportar centros de costo, elementos y codigo financiero, la nomina y las monedas se muestran ahi sin cliente. Solo entra a caso lo que la sala confirma despues de [10:14].

### Demo o pedido que el cliente no formula

- Importar y exportar centros de costo, elementos de costo y codigo financiero. Carlos dice el 01/10 [14:23] que venia de Trello. En la sala el cliente no lo pide de nuevo.
- Area de negocio. El 01/10 [16:23] Maria Jesus dice que no la usan, ni como parametro ni para gestionar. Carlos ofrece importar y exportar y ella no lo pide. Deja abierto si Mario la quisiera; Mario no estaba. El 01/10 [30:55] Carlos agrega area de negocio al asiento de venta. Ella no lo pide. No es caso de octubre.
- Cuenta contable y centro de costo en el asiento de venta. Lo muestra Carlos el 01/10 [30:55]. El cliente no lo pide en esa sala. Lo que si pide del comprobante esta en CU-06, CU-07, CU-08 y CU-09.
- Historial de modificaciones de los mantenedores y mas estados ademas de vigente y anulado. Carlos lo ofrece el 01/10 [17:32]. La sala no pide otro estado.
- Moneda de pago en la ficha, dicha por Carlos antes de que entrara el cliente. Maria Jesus confirma dias de neto e IVA (CU-01), no una moneda de pago distinta.
- Etiqueta "tambien es proveedor" en la ficha del contratista. La muestra Carlos el 14/10 [06:49]. Ella pidio codigo, RUT, nombre, direccion y quien crea (CU-26). No pidio la etiqueta.
- Folio de la OC hija con el mismo numero y un guion (`-1`, `-2`). Es la demo de Carlos el 14/10 [27:50]. Ella no fija el formato.
- Vencimientos en el comprobante. Frase de Carlos el 14/10 [56:51]. El plazo editable esta en CU-01. Ella no pide la columna de vencimiento en esa pantalla.
- Cadena de OC "para que Mario deje de perderse". El 01/10 [50:22] Maria Jesus pide que se la muestren. No agrega una regla. La regla nueva de octubre es CU-23.
- Montos 5.000 y 10.000 de la cadena de proforma en la demo del 14/10 [08:32]. Ejemplo de Carlos. Ella no los fija.
- Nombre "Felipe" y tope 500.000. Ejemplo de Carlos el 14/10 [33:23]. Ella acepta que el primer eslabon parta de cero, no esos datos.
- Plan de pruebas de emision, tres o cuatro muestras por tipo de DTE, y representaciones graficas. Lo pide Pablo el 06/10 [06:17] y lo reitera el 13/10 [01:37]. Es trabajo de GoSocket con Carlos. Maria Jesus no lo confirma como pedido al ERP.
- Resolucion 154 de la guia de despacho, GetDocumentPDF y descarga de XML. Pablo pregunta el 13/10 [01:52]; Carlos dice que lo estan considerando. Maria Jesus no lo pide.
- Sincronizar la guia desde la API de GoSocket. Pablo el 06/10 [04:39] dice que la guia de despacho se puede obtener de lo recibido. Maria Jesus no lo confirma. El 01/10 [57:10] el control que ella describe es la guia fisica, y [57:38] recuerda que en el RCV del SII la guia no aparece. El pedido al ERP es el libro en insumos (CU-13 y CU-14), no la sincronizacion.
- Grupo de aprobacion que no pueda servir a la vez para OC y para proforma. Lo dicen Carlos y Sergio el 06/10 [37:20], despues de que se corto Maria Jesus. Ella no lo confirma. El 14/10 ven un selector y no dicen esa exclusividad.
- Estado "notificada" como condicion para listar la proforma en compras. Lo arman Carlos y Sergio el 06/10 [31:51], sin ella. El 13/10 [08:49] ella lista las aprobadas.
- Cierre semanal obligatorio de proformas. Lo conversan Carlos y Sergio el 06/10 [33:27], sin ella, como pregunta pendiente. Ella el 14/10 pide cierre de mes (CU-38). La semana le sirve para agrupar y enviar (CU-30 y CU-33), no como un cierre de sistema.
- Menu de traspaso que habia armado Diego. Lo miran Carlos y Sergio el 06/10 [32:41], sin ella. El menu que ella nombra el 14/10 es "Traspaso contable y cierre de mes" (CU-38).
- Productor como maestro. El 01/10 [19:26] Maria Jesus lo nombra junto con proveedor y cliente. El cierre de esa sala, [25:50], habla solo de fichas separadas de proveedor y cliente que conversan por RUT. No queda un maestro Productor.
- Nota de credito por diferencia de contratista. El 14/10 [01:01:09] se oye "orden de credito". La frase esta sucia. Lo que ella dice claro es que, ya facturado, no se edita (CU-34).
- Precio cero en el ingreso diario. Lo pregunta una voz de la sala el 14/10 [59:15]. Maria Jesus deja el precio estimativo editable (CU-40), no el cero.
- Aprobacion del ingreso diario al guardarlo. Ella lo dice el 06/10 [18:17] y lo corrige en la misma sala el [24:05] (CU-31).
- La hija que nace al asociar la factura en el libro de compras. Es la demo de Carlos y Sergio el 14/10 [29:50] y el mecanismo de septiembre. Maria Jesus, mas adelante en la misma sala, la hace nacer de la guia en bodega (CU-13).
- Contabilidad "de vuelta" en Trello, responsables por modulo, y el compromiso de ella de traer el flujo de contratistas el martes. El 01/10 [53:48] y [01:01:26]. Es organizacion de la sala. El flujo llego el 06/10 y de ahi salen los casos de contratistas.
- Rodrigo como posible usuario agricola. El 01/10 [01:03:02] ella dice que se van a apoyar en el por si el area agricola quiere usar la plataforma, y que es de otra empresa. No hay un requerimiento suyo en esa sala. Lo que el 14/10 queda pedido con el en la sala esta en CU-28, CU-29, CU-40 y CU-41.
- Acceso a Trello, visita de la semana del 26, y si se reunen el jueves siguiente. Cierre del 14/10 [01:03:54]. No es un caso del ERP.
- Contrato con GoSocket, Iofacturo, capacitacion del portal e induccion. Maria Jesus el 06/10 [09:04] ("si, por favor Pablo") y el 13/10 [03:24] y [04:19]. Es contrato y capacitacion del proveedor de facturacion, no un caso del ERP.
- Emision de prueba entre empresas y rechazos de folios de septiembre. Tramo de Pablo, Carlos y Sergio el 06/10 [02:21] a [08:52], antes del flujo de contratistas. Maria Jesus no pide un cambio al ERP ahi.

### Silencio

- El 01/10 Mario no esta. No se le atribuye un caso por lo que Carlos dice que Mario le mando.
- Donde el Whisper no pone nombre, el caso dice "voz sin nombre" y la sala. No se le puso nombre de Fran, Lafran, Rodrigo o Mario solo por el tema.
- No se creo un caso de area de negocio, de tarifario, de portal del contratista ni de guia electronica para llenar un hueco de la demo.
