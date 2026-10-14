# Plan de pruebas: qué mostrar el 14/10/2026

Fecha: 2026-10-14. Cubre cada caso de `casos-de-uso.md` con una prueba que se puede ejecutar en la demo. La pantalla de cada caso está en `plan-integracion.md`. Este archivo no cambia código y no registra un pase: al escribirlo no se abrió el ERP, no se emitió un DTE, no se pagó, no se cerró el mes y no se envió correo.

Empresa: ALMAHUE EXPORT SPA. Periodo que se deja a la vista: 2026-10. Front local: `http://localhost:5174`, con un usuario que ya tenga Contabilidad, Compras, Ventas y Contratistas.

Datos que ya se conocen y se usan como ancla. Si al abrir la pantalla el número no está, se anota y no se fabrica otro documento:

| Dato | Uso en la prueba |
|---|---|
| Asiento 20260041, folio 92, OV 101606909139 | Venta ya contabilizada (CU-1-01) |
| Asiento 20260039, folio 61 | Comprobante ya existente del mismo periodo. Se abre para ver si es la compra de la hija. Si no lo es, no se usa como ejemplo de CU-1-02 |
| OC-2026-0016 madre, hija OC-2026-0017 | Listado de Compras y control de la madre (CU-1-02, CU-3-02) |
| Proforma e ingreso diario ya cargados | Los que muestre Contratistas. Este plan no les inventa número |

Dos tipos de prueba:

- Requisito: el cliente lo pidió. Si la pantalla no lo muestra, el código no cumple ese caso.
- Mostrar: Sergio o Carlos lo nombraron en la interna y el cliente no lo pidió. Se abre para decirlo en voz alta. No es un ítem a implementar.

## Índice

| ID | CU | Tipo | Qué se comprueba |
|---|---|---|---|
| P-1-01 | CU-1-01 | Requisito | Comprobante de la venta ya contabilizada: detalle, PDF, glosa, auxiliar, IVA débito |
| P-1-02 | CU-1-01 | Requisito | El mismo comprobante en peso, dólar y yuan |
| P-1-03 | CU-1-02 | Requisito | Compra contabilizada desde la hija; la madre no tiene asiento |
| P-1-04 | CU-1-03 | Mostrar | Balance de 8 columnas y libro diario, como revisión interna |
| P-2-01 | CU-2-01 | Requisito | Ficha del contratista e ingreso diario |
| P-2-02 | CU-2-02 | Requisito | Varios ingresos arman una proforma y dejan de estar libres |
| P-2-03 | CU-2-03 | Requisito | La proforma sigue entera: no nace una hija |
| P-3-01 | CU-3-01 | Requisito | En el libro se listan OC abiertas de ese proveedor |
| P-3-02 | CU-3-02 | Requisito | Madre e hija en el listado de Compras; la madre es informativa |
| P-3-03 | CU-3-03 | Requisito | La OC queda en la factura, no en la guía |
| P-4-01 | CU-4-01 | Requisito | Una o varias proformas en el documento de compra |
| P-4-02 | CU-4-02 | Mostrar | No hay cuenta de proforma dicha por el cliente |
| P-5-01 | CU-5-01 | Requisito | Aviso interno si la factura no trae OC, sin enviarlo |
| P-5-02 | CU-5-02 | Requisito | Pantalla de correo de la proforma, sin enviarlo |
| P-5-03 | CU-5-03 | Mostrar | Plantilla de correo de venta, dicha como configuración interna |

En todas: no emitir DTE, no pagar, no cerrar el mes, no enviar correo, no inventar la cuenta de la proforma, no apretar Cierre de saldo, no entrar a Ventas > Emitir DTE ni a Tesorería > Pagos ni a Contabilidad > Períodos contables. El cruce de factura parcial no se recorre.

## 1. Contabilización

### P-1-01. Comprobante de la venta ya contabilizada

Cubre CU-1-01. Requisito (María Jesús, Fran y Lupe, 01/10).

| Campo | Contenido |
|---|---|
| Precondición | ALMAHUE EXPORT SPA, periodo 2026-10. Existe la OV 101606909139, folio 92, asiento 20260041. No se crea otro asiento. |
| Qué se abre | Ventas > Libro de ventas (`/comercial/libro`). Se ubica el folio 92 y se lee el estado. Después Contabilidad > Comprobantes / asientos (`/contabilidad/asientos`), se abre el 20260041 y se usa Imprimir para ver el PDF. Si hace falta leer la glosa sin el comprobante: Contabilidad > Libro mayor (`/contabilidad/mayor`). |
| Resultado que pidió el cliente | El comprobante muestra el detalle del asiento y el PDF. La glosa del mayor es el comentario escrito (número de factura y una descripción corta), no el texto del ítem, y se repite en cliente, IVA e ingreso. El auxiliar es el RUT del cliente, en general sin dígito verificador. La cuenta que en un PDF anterior salió como caja se ve como IVA débito. El nombre del dueño no aparece. |
| Qué no se debe apretar | No emitir un DTE. No pagar. No cerrar el mes. No enviar correo. No crear un asiento nuevo para que el comprobante salga bien. No grabar cambios en el asiento. |
| Cómo se sabría hoy | En el detalle del 20260041 y en el PDF se anota la glosa de cabecera y la de las líneas de cliente, IVA e ingreso; el auxiliar; el nombre de la cuenta de IVA; y si aparece un nombre de dueño. En el mayor se lee si esa glosa se ve sin abrir el comprobante. Cumple si esas cuatro lecturas coinciden con la fila de resultado. No cumple si la glosa es el texto del ítem, si el auxiliar trae el dígito verificador, si el IVA figura como caja, o si el nombre del dueño está en el PDF. Resultado de esta redacción: no corrido. |

### P-1-02. Comprobante de venta en peso, dólar y yuan

Cubre CU-1-01. Requisito. El cliente pidió la contabilidad en peso y dólar aunque el documento esté en otra moneda, el tipo de cambio del día (Banco Central) si no ingresan uno, y el yuan como tercera columna en todos los casos.

| Campo | Contenido |
|---|---|
| Precondición | La misma de P-1-01: asiento 20260041, folio 92, OV 101606909139. No se carga un tipo de cambio nuevo. |
| Qué se abre | El detalle del asiento 20260041, ya abierto en P-1-01. Se leen las columnas de moneda y, en la cabecera del documento de venta, la moneda y el tipo de cambio guardado. |
| Resultado que pidió el cliente | Columnas de pesos, dólar y yuan: T dólar, debe/haber dólar, T yuan, debe/haber yuan, además del peso. Si el documento no está en peso y no hay tipo de cambio ingresado, el comprobante usa el del día. |
| Qué no se debe apretar | No fabricar un asiento en otra moneda. No tipear un tipo de cambio para la reunión. No emitir, no pagar, no cerrar el mes. La franja fija de tipo de cambio en todas las pantallas no se muestra como pedido: el cliente la pidió dentro del comprobante. |
| Cómo se sabría hoy | En el detalle del 20260041 se cuenta si están las tres monedas. Se anota la moneda del folio 92 y si el tipo de cambio visible es uno cargado o el del día. Cumple si las columnas de dólar y yuan están en ese comprobante. No cumple si solo está el peso, o si un documento en otra moneda quedó sin conversión y sin el tipo del día. Resultado de esta redacción: no corrido. |

### P-1-03. Compra desde la hija; la madre sin asiento

Cubre CU-1-02. Requisito (sala del 23/09; María Jesús el 01/10).

| Campo | Contenido |
|---|---|
| Precondición | ALMAHUE EXPORT SPA, periodo 2026-10. Madre OC-2026-0016 e hija OC-2026-0017. Asiento 20260039, folio 61, solo si al abrirlo es la compra de esa hija. Si el folio 61 es otra cosa, se busca en el libro un recibido que ya tenga la hija asociada y no se inventa el vínculo. |
| Qué se abre | Compras > Libro de compras (`/compras/registro`). Se abre el recibido asociado a la hija. Si ya está contabilizado, se abre su comprobante en Contabilidad > Comprobantes / asientos. Si sigue por contabilizar, se abre el modal Contabilizar, se lee el preview y se cierra con Cancelar. En Compras > Órdenes de compra se leen cuenta y centro de costo de la línea de la hija. Se busca el número de la madre entre los comprobantes. |
| Resultado que pidió el cliente | Lo que se contabiliza es la OC hija. Cada línea trae cuenta contable y centro de costo tomados de la línea de la OC. La madre no contabiliza: queda como control y no es un comprobante. |
| Qué no se debe apretar | No apretar Aceptar y contabilizar. No contabilizar la madre. No emitir DTE. No pagar. No cerrar el mes. No usar un origen Tipo de contrato como si fuera la cuenta de una proforma. |
| Cómo se sabría hoy | En el preview, la columna De dónde sale dice Orden de compra, y las líneas muestran cuenta, debe, haber y auxiliar. En comprobantes, el asiento de esa factura existe y no hay un asiento cuyo documento sea OC-2026-0016. Cumple si la hija es el origen del comprobante y la madre no aparece como asiento. No cumple si el comprobante nace de la madre, o si la cuenta del preview no sale de la línea de la OC. Resultado de esta redacción: no corrido. |

### P-1-04. Balance y libro diario, solo para mostrar

Cubre CU-1-03. Mostrar, no requisito. Lo nombró Sergio en la interna del 13/10. En estas transcripciones el cliente no pidió dejarlos afinados. En Reu6 Agustín no pidió ese reporte.

| Campo | Contenido |
|---|---|
| Precondición | Los asientos que ya existen, entre ellos 20260039 y 20260041 si están en el periodo. No entra un asiento armado para cuadrar. |
| Qué se abre | Contabilidad > Balance de 8 columnas (`/contabilidad/balance-8-columnas`) y Contabilidad > Libro diario (`/contabilidad/libro-diario`), periodo 2026-10. |
| Resultado que pidió el cliente | Ninguno. En la reunión se dice que es revisión interna. Si las pantallas abren con datos de demo, se dejan a la vista. |
| Qué no se debe apretar | No cerrar el mes. No generar asientos para cuadrar el balance. No tratar la revisada como requisito de negocio. |
| Cómo se sabría hoy | Las dos rutas abren y muestran filas del periodo, o no abren. Eso solo dice si se pueden mostrar. No hay criterio de negocio que marcar como cumplido o incumplido. Resultado de esta redacción: no corrido. |

## 2. Contratistas

### P-2-01. Ficha del contratista e ingreso diario

Cubre CU-2-01. Requisito (María Jesús, 06/10).

| Campo | Contenido |
|---|---|
| Precondición | ALMAHUE EXPORT SPA. El contratista y el ingreso diario que ya están en el listado. No se da de alta otro contratista ni se carga otro ingreso si con los existentes se puede leer la ficha y una fila. |
| Qué se abre | Contratistas > Listado (`/contratistas`): código, RUT, nombre, dirección y quién lo creó. Contratistas > Ingreso diario (`/contratistas/ingreso-diario`): una fila ya cargada y, si hace falta ver el origen de los catálogos, Parametrización > Centros de costo y Parametrización > Contratista, solo lectura. |
| Resultado que pidió el cliente | Código correlativo distinto del RUT. Ficha con RUT, nombre, dirección y creador. Ingreso con fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duración, valor unitario (trato o jornada), cantidad y total. El trabajador no va. El predio es opcional. Cuartel y faena salen de mantenedor. El ingreso es el detalle de la proforma. El contrato no se carga. |
| Qué no se debe apretar | No pagar. No emitir DTE. No enviar correo al contratista. No guardar un alta nueva. No cargar un contrato. |
| Cómo se sabría hoy | En el listado se anota si el código es correlativo (no el RUT) y si se ve el creador. En el ingreso se anota campo por campo la lista del resultado, y si existe un campo trabajador. El plan de integración ya dejó la duda de si forma de pago, unidad y duración están en otro control de esa pantalla: esta prueba lo mira ahí y no cierra esa duda por adelantado. Cumple si la ficha muestra código, RUT, nombre y creador, el ingreso muestra su total, no hay trabajador, y cuartel y faena no son texto libre. No cumple si el código es el RUT, si hay que tipear el trabajador, o si cuartel y faena son texto libre. Los campos que no aparezcan se listan como hueco, sin darlos por ausentes antes de abrir la pantalla. Resultado de esta redacción: no corrido. |

### P-2-02. Varios ingresos en una proforma

Cubre CU-2-02. Requisito (María Jesús, 06/10).

| Campo | Contenido |
|---|---|
| Precondición | Un contratista con ingresos diarios. Al menos una proforma ya armada con más de un ingreso, si el listado la tiene. No se pide PIN. |
| Qué se abre | Contratistas > Proformas y facturas (`/contratistas/proformas`). Se elige el contratista y el periodo. Se lee el total de la proforma ya armada y el indicador de ingresos pendientes de proforma. |
| Resultado que pidió el cliente | Se pueden marcar N ingresos que todavía no están en una proforma y ver el total. Esos ingresos dejan de estar disponibles para otra proforma. Los ingresos de un día se pueden repartir en 2 o 3 proformas. La que pasa por aprobación es la proforma, no cada ingreso. La proforma no se convierte en OC: queda en el módulo y se asocia a la factura. |
| Qué no se debe apretar | No aprobar con PIN de un usuario real. No pagar. No emitir la factura del contratista. No apretar Generar OC ni entrar al modal Asociar factura / generar OC. No guardar una proforma nueva si ya hay una de ejemplo. |
| Cómo se sabría hoy | En la proforma de ejemplo se cuenta cuántos ingresos la componen y si esos mismos ingresos siguen ofrecidos para otra. En pendientes de proforma se mira si un ingreso ya usado vuelve a salir. Se confirma que el trámite visible es el de la proforma. Cumple si los ingresos usados no se ofrecen de nuevo y la proforma no ofrece convertirse en OC en el camino que se muestra. No cumple si el mismo ingreso entra en dos proformas, o si la pantalla que se muestra para asociar es Generar OC. Resultado de esta redacción: no corrido. |

### P-2-03. La proforma no se parte

Cubre CU-2-03. Requisito (María Jesús, 06/10). El ingreso y la proforma se muestran enteros.

| Campo | Contenido |
|---|---|
| Precondición | La proforma de P-2-02, por su total. No se ingresa un monto menor. |
| Qué se abre | La misma pantalla, Contratistas > Proformas y facturas. Se abre el detalle de esa proforma y se busca si existe una hija, un sufijo o un saldo partido. |
| Resultado que pidió el cliente | Una proforma por su total, asociada entera a la factura. Si la factura viniera por menos, la proforma no se parcializa: el contratista factura el total de las proformas enviadas. Una factura puede tomar N proformas. No se crea una proforma hija. |
| Qué no se debe apretar | No partir la proforma. No generar una hija. No emitir DTE. No pagar. No apretar un cierre de saldo de la proforma. El mecanismo de OC madre e hija no se rediscute en esta prueba. |
| Cómo se sabría hoy | El detalle muestra un solo documento y un solo monto, sin fila hija. En el código, la ausencia de una proforma hija se puede contrastar después; esta prueba no da ese contraste por hecho. Cumple si en la pantalla no hay acción ni documento hijo. No cumple si aparece una proforma hija o un monto parcial como forma de asociarla. Resultado de esta redacción: no corrido. |

## 3. Asignación de la OC

### P-3-01. OC abiertas del proveedor en el libro

Cubre CU-3-01. Requisito (Lupe, sala del 23/09, con Mario).

| Campo | Contenido |
|---|---|
| Precondición | Un recibido del libro cuyo XML no trae OC, del mismo proveedor que una OC que siga abierta. Si ese ejemplo ya está asociado, se usa otro recibido sin OC, o se abre el modal solo para leer candidatas y se cancela. No se crea la OC. |
| Qué se abre | Compras > Libro de compras, modal Asociar. Se lee el aviso de que no viene asociada. Se abre el combo Orden de compra. |
| Resultado que pidió el cliente | Aviso de que no viene asociada. El combo lista solo OC de ese proveedor que sigan abiertas o pendientes de asignación, no las ya tomadas por otra factura. Si la OC existe, la persona del libro la asigna. Si no existe, no la crea: el aviso es P-5-01. |
| Qué no se debe apretar | No aceptar ni rechazar el DTE en el SII. No emitir. No pagar. No contabilizar si la OC todavía no está asociada. No crear la OC desde el libro. No confirmar el vínculo en esta pasada si eso escribiría `ocId` sobre un documento que no era el ejemplo ya asociado. |
| Cómo se sabría hoy | Se anota si el modal avisa la falta de OC y si el combo trae OC del proveedor todavía abiertas. Una OC ya tomada por otra factura no debería seguir en la lista. Una OC del mismo proveedor no debería desaparecer solo porque la razón social no coincide con el texto de la factura. Cumple si el combo filtra por proveedor y por saldo abierto, y si no nace una OC al mirar el modal. No cumple si entran OC de otro proveedor, OC ya cubiertas, o si el libro ofrece crear la orden. Guardar el vínculo queda para la demo, sobre el documento elegido, no para cerrar esta lectura. Resultado de esta redacción: no corrido. |

### P-3-02. Madre e hija en el listado de Compras

Cubre CU-3-02. Requisito en lo contable. Dónde se ve la madre: Compras > Órdenes de compra, el mismo listado, con el panel Madre / hijas.

| Campo | Contenido |
|---|---|
| Precondición | Madre OC-2026-0016 e hija OC-2026-0017. La hija que sirve de ejemplo es el trozo ya recepcionado: estado que se pueda asociar, neto de ese trozo, cuenta y centro copiados de la madre. |
| Qué se abre | Compras > Órdenes de compra (`/compras/ordenes`). Se buscan las dos filas. Se abre el detalle y el panel Madre / hijas. No se abre una pantalla de madre en Insumos. |
| Resultado que pidió el cliente | Las dos se distinguen en el listado. La madre se ve como dato informativo. La hija es la que se asocia al documento y la que se contabiliza. Al asociar, la hija trae cuenta y centro de costo de la madre; contabilidad no los vuelve a tipear. La madre no es un movimiento contable (eso se cruza con P-1-03). |
| Qué no se debe apretar | No mostrar la madre como comprobante. No llevarla a ventas ni a tesorería. No pagar. No cerrar el mes. No apretar Cierre de saldo. No recorrer la factura parcial. |
| Cómo se sabría hoy | En el listado, la fila de la hija dice de quién es hija y el panel de la madre lista a la hija con número, estado y neto. Se anota el número real: si la hija de OC-2026-0016 es OC-2026-0017 y está en estado asociable, sirve de ejemplo. Si la hija visible es un borrador con correlativo por el faltante, es el cierre viejo y no se usa como ejemplo. Cumple si madre e hija están en el mismo listado, se distinguen, y la madre no tiene comprobante. No cumple si la madre no aparece, si solo está en Insumos, o si el ejemplo mostrado es la hija del faltante. Resultado de esta redacción: no corrido. |

### P-3-03. La OC va en la factura, no en la guía

Cubre CU-3-03. Requisito (María Jesús, 01/10).

| Campo | Contenido |
|---|---|
| Precondición | La factura del libro que ya tenga OC (la hija de P-3-02, si el libro ya la asoció). La guía, solo si ya hay una cargada en Guías de insumos recibidas. No se carga una guía nueva. |
| Qué se abre | Compras > Libro de compras: la factura y el campo de OC. Después Insumos / Bodega > Guías de insumos recibidas (`/insumos/guias-recibidas`), una guía ya cargada, para ver que no es el documento de la OC. |
| Resultado que pidió el cliente | La guía aplica a insumos y entra el material a bodega. La OC se asocia a la factura, no a la guía. El ejemplo de María Jesús es la madre de las cajas, entregas semanales y la factura de fin de mes. |
| Qué no se debe apretar | No recepcionar stock. No emitir guía. No pagar. No tratar la guía como el disparador de la hija. |
| Cómo se sabría hoy | En la factura se lee el número de OC. En la guía se busca si tiene OC o un `ocId`. Cumple si la OC está en la factura y la guía no la guarda. No cumple si el vínculo de la OC está en la guía, o si la guía es la que dispara la hija. Resultado de esta redacción: no corrido. |

## 4. Proforma en el documento de compra

### P-4-01. Una o varias proformas en el libro

Cubre CU-4-01. Requisito (María Jesús, 06/10). Cada proforma entra entera (P-2-03).

| Campo | Contenido |
|---|---|
| Precondición | Un recibido del libro y una o más proformas que en Contratistas ya figuren aprobadas, por su total. No hace falta que el contratista apruebe dentro del sistema en esta pasada. |
| Qué se abre | Compras > Libro de compras, modal Asociar, bloque Proforma aprobada. Se leen número, contratista, monto y estado. Se mira si se puede elegir una segunda proforma sobre el mismo documento. No se entra a Generar OC de Contratistas. |
| Resultado que pidió el cliente | En el documento recibido se asocia una OC o una o más proformas. Pueden ir varias proformas en una factura (el ejemplo de ella: 10). La proforma entra entera. Al guardar no se crea una orden. Con el envío al contratista se da por aceptada la proforma, salvo reclamo de precio o jornada: en esta prueba solo se muestran proformas que ya figuren aprobadas. |
| Qué no se debe apretar | No emitir el DTE del contratista. No pagar. No enviar el correo. No parcializar la proforma. No pasar por Generar OC. No guardar un vínculo nuevo si el recibido de demo ya tiene la proforma de ejemplo: se lee y se cancela. |
| Cómo se sabría hoy | El bloque lista proformas aprobadas que todavía no tienen factura ni orden. Elegir proforma deja vacía la OC, y al revés. El aviso al guardar, si ya hubo una asociación de demo, dice que no se creó una orden. Para "varias": se mira si un segundo vínculo sobre el mismo registro suma o pisa el anterior. El modal, según el plan de integración, marca una proforma por acción. Cumple el caso de una si el libro asocia la proforma entera y no crea OC. Cumple el caso de varias solo si el mismo documento puede quedar con N proformas. No cumple si la única asociación está en Contratistas y genera una OC, o si la segunda proforma reemplaza a la primera. Resultado de esta redacción: no corrido. |

### P-4-02. Cuenta de la proforma, solo para mostrar que no está dicha

Cubre CU-4-02. Mostrar, no requisito. Carlos preguntó y Sergio la dejó para María Jesús. El cliente no la respondió en estas transcripciones.

| Campo | Contenido |
|---|---|
| Precondición | El vínculo de P-4-01, si ya existe en un recibido de demo. No entra una cuenta. |
| Qué se abre | El mismo modal Asociar, o el recibido que ya muestra la proforma. No se abre Contabilizar sobre ese documento. |
| Resultado que pidió el cliente | Ninguno sobre la cuenta. En compras normales la cuenta viene en la línea de la OC (P-1-03). Esa frase no se extiende a la proforma. |
| Qué no se debe apretar | No inventar la cuenta. No contabilizar la proforma. No cerrar el mes. No pagar. No presentar el origen Tipo de contrato como respuesta de María Jesús. |
| Cómo se sabría hoy | Se anota si el documento de la proforma muestra una cuenta y de dónde sale el rótulo. No hay un "cumple" de negocio: la prueba pasa como mostrar si nadie tipea una cuenta en la reunión. Falla como demo si se contabiliza la proforma o si se dice que la cuenta de la OC ya vale para la proforma. Resultado de esta redacción: no corrido. |

## 5. Correo

### P-5-01. Aviso interno si falta la OC

Cubre CU-5-01. Requisito (sala del 23/09, con Lupe en el libro; el 01/10 el cliente confirma el aviso).

| Campo | Contenido |
|---|---|
| Precondición | Un recibido sin OC (el de P-3-01). Un usuario ya registrado como destinatario. La casilla de enviar correo queda apagada. |
| Qué se abre | Compras > Libro de compras, modal Notificar. Se abre desde Asociar (Sí, notificar) cuando no hay OC, o desde la acción de notificar del registro. Se leen destinatario, asunto y cuerpo. Si ya hubo un aviso de demo, se lee el historial. No se confirma. |
| Resultado que pidió el cliente | El aviso dice que la factura de tal proveedor y tal monto está sin OC, para que esa persona la genere. Queda rastro de a quién se notificó y en qué fecha. El 01/10 el cliente acepta notificar a quien debe crear la OC (proveedor no creado, OC inexistente o con diferencia). En la demo se muestra la pantalla y el texto. Carlos dijo el 01/10 que el correo todavía no sale y que el aviso interno está maqueteado: se comprueba el texto, no se dispara. |
| Qué no se debe apretar | No enviar el correo. No confirmar el aviso, ni con la casilla apagada: hay que mirar antes si confirmar dispara SMTP. No crear la OC desde el libro. No pagar. No contabilizar esa factura. |
| Cómo se sabría hoy | Con la casilla apagada, el modal muestra destinatario, asunto y cuerpo con proveedor, folio y monto. El historial, si existe, muestra quién avisó, a quién y la fecha. Cumple como pantalla si esos datos están y no sale correo. No cumple si no hay a quién elegir, si el texto no nombra proveedor y monto, si no hay forma de ver el rastro, o si al confirmar con la casilla apagada igual sale SMTP. Esta prueba no confirma el modal. Resultado de esta redacción: no corrido. |

### P-5-02. Correo de la proforma, sin enviarlo

Cubre CU-5-02. Requisito (María Jesús, 06/10: mail del contacto del contratista).

| Campo | Contenido |
|---|---|
| Precondición | Una proforma ya aprobada y el e-mail cargado en la ficha del contratista (Contratistas > Listado). |
| Qué se abre | Contratistas > Proformas y facturas: la proforma, el contacto y el botón E-mail, sin ejecutarlo. Contratistas > Envío operativo (`/contratistas/envio-operativo`): periodo desde / hasta y la casilla de correo, sin marcarla. |
| Resultado que pidió el cliente | Con la proforma aprobada se puede mandar el detalle al contacto para que el contratista facture. Lo ya informado a mediados de mes no entra en el envío del cierre. El agrupado puede ser por rango de fecha o por labor. En esta prueba se muestra la acción. |
| Qué no se debe apretar | No enviar el correo. No apretar E-mail. No apretar Notificar contratista. No marcar la casilla de Envío operativo. No marcar como enviada una proforma que no se envió. No emitir la factura. No pagar. |
| Cómo se sabría hoy | Se ve la proforma aprobada, el e-mail de la ficha y las dos acciones de envío. Envío operativo muestra el rango de periodo. Cumple como pantalla si esas tres cosas se ven y ninguna se ejecuta. No cumple si E-mail dispara el envío al solo mostrarlo, o si Notificar contratista deja la proforma como enviada sin correo: por eso esos botones no se aprietan. El nombre de estado "notificada a proveedor" no se presenta como pedido del cliente. Resultado de esta redacción: no corrido. |

### P-5-03. Correo de venta, solo para mostrar

Cubre CU-5-03. Mostrar, no requisito. Lo nombró Sergio en la interna. El cliente pidió el aviso de compra sin OC (P-5-01) y el correo al contacto de la proforma (P-5-02). En Reu6 los correos que nombra el cliente son de acceso y de datos bancarios.

| Campo | Contenido |
|---|---|
| Precondición | Ninguna de negocio. Se abre solo si en la reunión preguntan por el correo de venta. |
| Qué se abre | Administración > Configuración de correos (`/admin/configuracion-correos`), plantilla VENTAS. En la misma pantalla están COMPRAS, PROFORMAS y los campos del servidor. No se graba nada. |
| Resultado que pidió el cliente | Ninguno. Se dice que es configuración interna. |
| Qué no se debe apretar | No enviar correo de venta. No probar el SMTP contra una casilla real. No pedir las credenciales del correo de Mario. No guardar la plantilla ni el servidor. |
| Cómo se sabría hoy | La plantilla VENTAS se ve o no se ve. Eso no es un requisito a cumplir. Falla como demo si se envía un correo o se graba la configuración. Resultado de esta redacción: no corrido. |

## Qué no se prueba como pedido

Sigue fuera de implementación, como cierran los casos de uso:

- Afinar el balance y el libro diario: P-1-04, prueba de mostrar.
- Correo de venta, plantilla con etiquetas e imágenes, y campos del servidor: P-5-03, prueba de mostrar.
- Una cuenta contable de la proforma: P-4-02, prueba de mostrar. No se usa la cuenta de la línea de la OC.
- El nombre de estado "notificada a proveedor" y su filtro de listado. María Jesús dijo que el envío da por aceptada la proforma salvo reclamo. El nombre lo armaron Carlos y Sergio después del corte de luz.
- Una franja fija de tipo de cambio en todas las pantallas. El tipo de cambio que se mira es el del comprobante (P-1-02).
- Partir la proforma en hija. P-2-03 comprueba que esa opción no se muestra.
