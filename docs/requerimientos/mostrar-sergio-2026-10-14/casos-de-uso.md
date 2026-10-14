# Casos de uso para mostrar el 14/10/2026

Alcance de la demo que Sergio nombró en la interna del 13/10. La interna es hipótesis de qué mostrar. Si una frase de Carlos o Sergio choca con el cliente, gana el cliente. No se reabre aquí el mecanismo de factura parcial: eso está en `docs/requerimientos/oc-dte-parcial-2026-10-14/`.

## Reuniones leídas y quién era cliente

| Reunión | Archivo | Cliente en sala |
|---|---|---|
| Interna 13/10, Carlos y Sergio | `docs/reuniones/transcripciones/transcripcion-2026-10-13-interna-carlos-sergio.md` | Nadie. Hipótesis de alcance, no requisito. |
| Dudas 23/09 | `docs/reuniones/transcripciones/transcripcion-2026-09-23-dudas-cliente.md` | Mario y Lupe. Agustín no estuvo. María Jesús estaba de vacaciones. El ASR no rotula al hablante. |
| Cliente 24/09 | `docs/reuniones/transcripciones/transcripcion-2026-09-24-reunion-cliente.md` | Lupe, Fran y Sigrid. El ASR nombra a Mario al presentar el flujo y no rotula línea a línea. |
| Cliente 01/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-01-reunion-cliente.md` | María Jesús, Fran y Lupe, desde [09:54]. Mario no entró. Hasta [09:54] hablan solo Carlos y Sergio: eso no es requisito. El encabezado del archivo pide contrastar; se usa la frase del cliente en sala. |
| GoSocket y contratistas 06/10 | `docs/reuniones/transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md` | María Jesús. Pablo (GoSocket) sale cerca de [09:27]. Desde el corte de luz, cerca de [30:55], hablan solo Carlos y Sergio: eso no es requisito. |
| Reu6, 06/08 | `docs/reuniones/transcripciones/transcripcion-reunion6.md` | Agustín (Speaker 00) y María José (Speaker 01). |

Reu5 no se usó. Las minutas no se citan como requisito.

Lo que Sergio pidió mostrar, en la interna: contabilización de compra y de venta, con una revisada al balance y al diario [08:52] y [10:20]; módulo contratista de Diego, y que la proforma no cree hija [01:34]; asignación de OC de José [10:26]; asignación de proforma [10:31]; notificación interna por correo [03:44] y [10:31]. La cuenta de la proforma quedó como pregunta para María Jesús [02:24].

## 1. Contabilización de compra, de venta, balance y libro diario

### CU-1-01. Contabilizar la venta y abrir el comprobante

- Quién: María Jesús (cliente; el ASR no pone el nombre, el alcance es al comprobante que muestra Carlos). Fran y Lupe están en sala.
- Dónde: `transcripcion-2026-10-01-reunion-cliente.md`, [32:37] a [40:16].
- Mostrar hoy: una venta ya contabilizada en datos de demo. Abrir Contabilidad > comprobantes, ver el detalle del asiento y el PDF. La contabilidad va en peso y dólar aunque el documento esté en otra moneda [32:41]. Si no ingresan tipo de cambio, usar el del día (Banco Central) [32:50]. El yuan va como tercera columna, en todos los casos [33:22]. El auxiliar es el RUT del cliente, en general sin dígito verificador [33:44]. La glosa del mayor es el comentario que ellos escriben (número de factura y una descripción corta), no el texto del ítem [37:23]. Esa glosa se repite en cliente, IVA e ingreso, para leer el mayor sin abrir el comprobante [39:36]. La cuenta que en el PDF salió como caja tiene que verse como IVA débito [38:48]. El nombre del dueño no va [38:39].
- No hacer en la demo: no emitir un DTE real, no pagar, no cerrar el mes, no enviar correo.

### CU-1-02. Contabilizar la compra desde la OC asociada

- Quién: cliente en sala del 23/09 (Mario y Lupe; el ASR no rotula). María Jesús lo confirma el 01/10.
- Dónde: `transcripcion-2026-09-23-dudas-cliente.md`, [24:45] a [25:36] y [28:50] a [29:05]. `transcripcion-2026-10-01-reunion-cliente.md`, [47:20] a [47:43].
- Mostrar hoy: en el libro de compras, un documento recibido que ya tiene OC asociada, con cuenta contable y centro de costo tomados de la línea de la OC. Cada línea de la venta, en el ejemplo que citan, también lleva cuenta y centro de costo; en compra piden lo mismo por línea de la OC [24:45], [25:22]. Lo que se contabiliza es la OC hija. La madre no contabiliza: queda como control [28:50]. María Jesús: la madre es un dato informativo y no se refleja fuera de insumos; los hijos son los que se contabilizan [47:20].
- No hacer en la demo: no emitir DTE real, no pagar, no cerrar el mes, no contabilizar la madre, no inventar la cuenta de una proforma (eso es el punto 4).

### CU-1-03. Balance y libro diario: el cliente no pidió afinarlos

- Quién: Sergio, en la interna, sin cliente. Agustín, en Reu6, habla de otra cosa.
- Dónde: `transcripcion-2026-10-13-interna-carlos-sergio.md`, [08:52] a [08:59] y [10:20]. `transcripcion-reunion6.md`, Agustín [28:04] y [01:03:17].
- Mostrar hoy: si el balance y el libro diario ya abren con datos de demo, se pueden dejar a la vista como revisión interna. No hay frase del cliente, en las reuniones de esta lista, que pida dejarlos afinados. En Reu6 Agustín describe una cuenta de gastos de próxima temporada y un traspaso, y cierra con que no hay que hacer nada [29:04]. Su frase de [01:03:17] ("llegaron a los balances") es un comentario de cuánto avanzó la demo, no un pedido del reporte.
- No hacer en la demo: no cerrar el mes, no generar asientos nuevos para "cuadrar" el balance, no tratar esa revisada como requisito de negocio.

## 2. Módulo contratistas: ingreso diario, proforma, y la proforma no se parte

### CU-2-01. Ficha del contratista e ingreso diario

- Quién: María Jesús.
- Dónde: `transcripcion-2026-10-06-gosocket-contratistas.md`, [12:37] a [17:45].
- Mostrar hoy: alta del contratista con código correlativo (si hay 10, el siguiente es 11; no es el RUT), RUT, nombre, dirección y quién lo creó [14:13]. Ingreso diario con fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duración, valor unitario (trato o jornada), cantidad y total. El trabajador no va [16:06]. Predio opcional (agrícola lo usa, ALM no) [14:51]. Cuartel y faena salen de mantenedor, no de texto libre [16:55]. El ingreso diario es el detalle de la proforma [17:39]. El contrato se salta: AgroSmart no lo exige y van a una fusión con Agrosoft [12:37].
- No hacer en la demo: no pagar, no emitir DTE real, no enviar correo al contratista.

### CU-2-02. Armar la proforma con varios ingresos diarios

- Quién: María Jesús.
- Dónde: el mismo archivo, [13:14] a [13:54], [19:43] a [20:10] y [23:18] a [24:05].
- Mostrar hoy: elegir el contratista, listar sus ingresos diarios que todavía no están en una proforma, marcar N (por ejemplo 5 de 10) y ver el total. Esos ingresos dejan de estar disponibles para otra proforma [23:35]. 30 ingresos del día se pueden repartir en 2 o 3 proformas [19:54]. La proforma es como la orden de compra de este módulo [17:26]. La que pasa por aprobación es la proforma, no cada ingreso chico por separado [20:50] a [24:05]. En el 23/09 alguien de la sala creyó que la proforma se traspasaba a una OC [21:31]; en la misma reunión se corrige: la proforma queda en el módulo y se asocia a la factura [21:43] a [22:37], y piden dejar el módulo en espera [22:48]. El 01/10 la duda sigue abierta [54:12]. El 06/10 María Jesús la cierra: no se convierte en OC, se asocia a la factura.
- No hacer en la demo: no aprobar con PIN de un usuario real, no pagar, no emitir la factura del contratista.

### CU-2-03. La proforma no se parte en hija

- Quién: María Jesús. Sergio lo repite en la interna; la frase que manda es la de ella.
- Dónde: `transcripcion-2026-10-06-gosocket-contratistas.md`, [25:07] a [25:33]. Interna: `transcripcion-2026-10-13-interna-carlos-sergio.md`, [01:34] a [01:42].
- Mostrar hoy: una proforma por su total, asociada entera a la factura. Si el ejemplo es 9.600 y la factura viniera por 5.600, la proforma no se parcializa: el contratista factura el total de las proformas que se le enviaron. Una factura puede tomar N proformas [25:30]. A diferencia de la OC, no se crea una proforma hija.
- No hacer en la demo: no partir la proforma, no generar una hija, no emitir DTE real, no pagar. El mecanismo de OC madre e hija no se rediscute aquí.

## 3. Asignación de la orden de compra en el listado de Compras

Cómo se muestra y se asocia. El cruce de factura parcial (cantidades, hijas 100.1, multi-ítem) no se reabre: está en `docs/requerimientos/oc-dte-parcial-2026-10-14/`.

### CU-3-01. Asociar a mano la OC del proveedor en el libro de compras

- Quién: Lupe, nombrada en la sala. Mario está. El ASR no rotula cada frase.
- Dónde: `transcripcion-2026-09-23-dudas-cliente.md`, [38:48] a [40:17] y [42:00] a [42:06].
- Mostrar hoy: en el libro de compras, un recibido cuyo XML no trae OC. Aviso de que no viene asociada. Al asignar, listar solo OC de ese proveedor que sigan abiertas o pendientes de asignación, no las ya tomadas por otra factura [39:54], [40:12]. Si la OC ya existe, la persona del libro la asigna. Si no existe, no la crea ella: avisa a quien pidió el servicio (eso es el punto 5).
- No hacer en la demo: no aceptar ni rechazar el DTE en el SII, no emitir, no pagar, no contabilizar en esta pantalla si la OC todavía no está asociada.

### CU-3-02. Madre e hija visibles en Compras, con la madre solo informativa

- Quién: María Jesús el 01/10. En el 24/09 el cliente en sala (ASR sin nombre) dice que la madre es la que manda y que la cuenta y el centro de costo ya vienen declarados.
- Dónde: `transcripcion-2026-10-01-reunion-cliente.md`, [47:07] a [47:43]. `transcripcion-2026-09-24-reunion-cliente.md`, [15:37] a [15:43].
- Mostrar hoy: en el listado de Compras, la OC madre y la OC hija, distinguibles. La madre se ve como dato informativo. La hija es la que se asocia al documento y la que se contabiliza. La madre no se replica en módulos que no sean insumos [47:20]. Al asociar, la hija hereda cuenta y centro de costo de la madre; contabilidad no los vuelve a tipear [15:37].
- No hacer en la demo: no mostrar la madre como movimiento contable, no llevarla a ventas ni a tesorería, no pagar, no cerrar el mes. No recorrer el algoritmo de la factura parcial.

### CU-3-03. La OC se asocia a la factura, no a la guía

- Quién: María Jesús.
- Dónde: `transcripcion-2026-10-01-reunion-cliente.md`, [55:22] a [56:45].
- Mostrar hoy: la guía aplica solo a insumos y sirve para entrar el material a bodega. La OC (el ejemplo de ella: madre de 100 cajas, entregas semanales, factura de fin de mes) se asocia a esa factura, no a la guía.
- No hacer en la demo: no recepcionar stock real, no emitir guía, no pagar.

## 4. Asignación de la proforma al documento de compra

### CU-4-01. Asociar una o varias proformas en el libro de compras

- Quién: María Jesús. En el 23/09 la sala ya había dicho que sí, y dejó el módulo en espera.
- Dónde: `transcripcion-2026-10-06-gosocket-contratistas.md`, [13:52] a [13:54], [24:32] a [24:41], [25:30] a [25:33] y [30:10] a [30:25]. `transcripcion-2026-09-23-dudas-cliente.md`, [22:26] a [22:48].
- Mostrar hoy: en documentos recibidos del libro de compras, asociar una OC o una o más proformas al mismo documento. Pueden ir 10 proformas en una factura [13:54]. La proforma entra entera (CU-2-03). María Jesús: con el envío al contratista dan por aceptada la proforma, salvo que él reclame precio o jornada [30:16]. Mostrar la asociación sobre proformas que en la demo ya figuren aprobadas. No hace falta que el contratista apruebe dentro del sistema.
- No hacer en la demo: no emitir el DTE del contratista, no pagar, no enviar el correo, no parcializar la proforma.

### CU-4-02. La cuenta contable de la proforma no está dicha

- Quién: Carlos pregunta y Sergio la deja para María Jesús. El cliente no la respondió en estas transcripciones.
- Dónde: `transcripcion-2026-10-13-interna-carlos-sergio.md`, [02:14] a [02:41], [06:30] y [09:35].
- Mostrar hoy: la asociación de la proforma al documento del libro, sin una cuenta puesta como si ya estuviera definida. En compras normales el cliente sí dijo que la cuenta viene en la línea de la OC (CU-1-02). Esa frase no se extiende a la proforma.
- No hacer en la demo: no inventar la cuenta, no contabilizar la proforma, no cerrar el mes, no pagar.

## 5. Correo de notificación interna

### CU-5-01. Aviso interno cuando la factura de compra no trae OC

- Quién: cliente en sala del 23/09, con Lupe como quien revisa el libro. El 01/10 el cliente confirma el mismo aviso.
- Dónde: `transcripcion-2026-09-23-dudas-cliente.md`, [38:34] a [38:48] y [42:12] a [45:34]. `transcripcion-2026-10-01-reunion-cliente.md`, [45:47] a [46:39].
- Mostrar hoy: desde el libro de compras, elegir un usuario registrado y dejar armado el aviso de que la factura de tal proveedor y tal monto está sin OC, para que esa persona la genere [43:25]. Tiene que quedar rastro de a quién se notificó y en qué fecha, porque si no el otro puede decir que nunca le llegó [45:06]. El 01/10 el cliente acepta notificar a quien debe crear la OC (proveedor no creado, OC inexistente o con diferencia) [46:12]. Carlos dice en esa misma reunión que el correo todavía no sale y que el aviso interno está maqueteado [46:25]. En la demo se muestra esa pantalla y el texto, sin dispararlo.
- No hacer en la demo: no enviar el correo, no crear la OC desde el libro saltándose a quien la pide, no pagar, no contabilizar esa factura.

### CU-5-02. Correo al contacto cuando la proforma ya está aprobada

- Quién: María Jesús. Sergio, en la interna, lo llama notificación interna [10:31]. Ella habla del mail del contacto del contratista.
- Dónde: `transcripcion-2026-10-06-gosocket-contratistas.md`, [25:52] a [28:30].
- Mostrar hoy: una proforma aprobada, el contacto cargado y la acción de envío, sin ejecutarla. Sirve para mandar el detalle y que el contratista facture [25:57]. Lo que ya se informó a mediados de mes no entra en el envío del cierre [28:18]. El agrupado puede ser por rango de fecha o por labor [26:33].
- No hacer en la demo: no enviar el correo, no marcar como enviada una proforma que no se envió, no emitir la factura, no pagar.

### CU-5-03. Venta: el cliente no pidió correo de notificación

- Quién: Sergio, sin cliente.
- Dónde: `transcripcion-2026-10-13-interna-carlos-sergio.md`, [03:44] a [04:33].
- Mostrar hoy: nada como requisito. Si la pantalla de plantilla ya existe, se puede abrir y decir que es configuración interna. En Reu6 los correos que nombra el cliente son de acceso (Microsoft) y de buscar datos bancarios, no un aviso al emitir una venta (`transcripcion-reunion6.md`, [04:24] y [31:51]).
- No hacer en la demo: no enviar correo de venta, no probar el SMTP contra una casilla real, no pedir en la reunión las credenciales del correo de Mario.

## Lo que la interna pide mostrar y el cliente no pidió

No implementarlo como requisito.

- Dejar afinados el balance y el libro diario. Lo dice Sergio [08:52]. En estas transcripciones el cliente no lo pide.
- Correo de venta, plantilla con etiquetas e imágenes, y campos para configurar el servidor. Lo dice Sergio [03:44] a [04:55]. El cliente pidió aviso en compra sin OC (CU-5-01) y correo al contacto de la proforma (CU-5-02). No pidió el de venta.
- Una cuenta contable para la proforma. Quedó como pregunta a María Jesús [02:24]. No usar la cuenta de la línea de la OC como si ella la hubiera confirmado para la proforma.
- Un estado con el nombre "notificada a proveedor" definido después de que María Jesús se queda sin luz [31:36] del 06/10. Ella sí dijo que el envío da por aceptada la proforma salvo reclamo [30:16]. El nombre del estado y el filtro de listado los arman Carlos y Sergio solos.
- El tipo de cambio siempre visible arriba, como en Detemite. Lo propone Carlos en la interna [09:09]. María Jesús pidió el tipo de cambio del día dentro del comprobante (CU-1-01), no una franja fija en todas las pantallas.
- Partir la proforma en hija. Sergio pide lo contrario [01:34], y María Jesús también [25:14]. No mostrarlo como opción.
