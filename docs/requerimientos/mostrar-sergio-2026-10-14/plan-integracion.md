# Plan de integración: qué mostrar el 14/10/2026

Fecha: 2026-10-14. Fuente de los casos: `casos-de-uso.md` (CU-1-01 a CU-5-03). Este documento dice en qué pantalla entra cada caso y qué se deja a la vista. No propone código. No reabre el mecanismo de factura parcial de `docs/requerimientos/oc-dte-parcial-2026-10-14/`.

Dos decisiones ya tomadas, que este plan respeta:

- La orden madre se muestra en Compras > Órdenes de compra, en el mismo listado, con el panel Madre / hijas. Eso pisa la frase de María Jesús del 01/10 ("la madre solo en insumos"). No hay una pantalla aparte en Insumos para ver la madre.
- La hija de una recepción parcial ya nace como el trozo recibido (`crearOcHijaDeRecepcion`). El cierre de saldo achica la madre y no crea hija por el faltante. No se vuelve al cierre viejo. En la demo no se aprieta ese botón y no se recorre el algoritmo de la factura parcial.

La interna del 13/10 arma el orden de la demo. Si una frase de Carlos o Sergio choca con el cliente, se muestra lo que pidió el cliente y se dice en voz alta que lo otro es revisión interna.

## Ancla: pantallas que ya existen

| Punto | Menú | Ruta |
|---|---|---|
| Venta contabilizada y comprobante | Ventas > Libro de ventas; Contabilidad > Comprobantes / asientos | `/comercial/libro`, `/contabilidad/asientos` |
| Compra con OC y cuenta | Compras > Libro de compras | `/compras/registro` |
| Balance y libro diario | Contabilidad > Balance de 8 columnas; Contabilidad > Libro diario; Contabilidad > Libro mayor | `/contabilidad/balance-8-columnas`, `/contabilidad/libro-diario`, `/contabilidad/mayor` |
| Contratista, ingreso y proforma | Contratistas > Listado; Ingreso diario; Proformas y facturas | `/contratistas`, `/contratistas/ingreso-diario`, `/contratistas/proformas` |
| Madre, hija y asignación de OC | Compras > Órdenes de compra; el mismo Libro de compras | `/compras/ordenes`, `/compras/registro` |
| Guía, aparte de la OC | Insumos / Bodega > Guías de insumos recibidas | `/insumos/guias-recibidas` |
| Proforma en el documento de compra | Libro de compras, modal Asociar | `/compras/registro` |
| Aviso sin OC | Libro de compras, modal Notificar | `/compras/registro` |
| Correo de la proforma | Contratistas > Proformas y facturas; Contratistas > Envío operativo | `/contratistas/proformas`, `/contratistas/envio-operativo` |
| Plantilla y servidor de correo | Administración > Configuración de correos | `/admin/configuracion-correos` |

No se abre Tesorería > Pagos. No se cierra un período en Contabilidad > Períodos contables. No se entra a Ventas > Emitir DTE.

## 1. Contabilización de compra, de venta, balance y libro diario

### CU-1-01. Contabilizar la venta y abrir el comprobante

- Requisito del cliente (María Jesús, Fran y Lupe, 01/10).
- Pantalla: Ventas > Libro de ventas, una factura que ya figure Contabilizada. Desde ahí, o directo, Contabilidad > Comprobantes / asientos: abrir el detalle y usar Imprimir. El mayor, si se quiere leer la glosa sin el comprobante, es Contabilidad > Libro mayor.
- Entra: un documento de venta ya emitido en datos de demo, con glosa, cuentas de las líneas, auxiliar y tipo de cambio si el documento no está en peso.
- Se ve: el comprobante con columnas de pesos, dólar y yuan (T dólar, debe/haber dólar, T yuan, debe/haber yuan), auxiliar, glosa de cabecera y glosa de línea. El PDF sale de Imprimir.
- No se hace: no emitir un DTE real, no pagar, no cerrar el mes, no enviar correo, no crear un asiento nuevo para que el comprobante "salga bien".

### CU-1-02. Contabilizar la compra desde la OC asociada

- Requisito del cliente (sala del 23/09; María Jesús lo confirma el 01/10). La hija que se contabiliza es la del trozo ya recepcionado. La madre queda de control en el listado de compras. No se la lleva a una pantalla de Insumos.
- Pantalla: Compras > Libro de compras, un recibido que ya tenga OC hija asociada. Si todavía está por contabilizar, el modal Contabilizar muestra el preview y se cierra con Cancelar. Si ya está contabilizada, se abre el comprobante en Contabilidad > Comprobantes / asientos. La cuenta y el centro de costo se miran en el preview (columna "De dónde sale" = Orden de compra) o en las líneas de Compras > Órdenes de compra.
- Entra: factura de compra ya cargada en el libro y OC hija con cuenta y centro en la línea.
- Se ve: OC, monto, glosa, líneas con cuenta, debe, haber, auxiliar y el origen de la cuenta. La madre no aparece como comprobante.
- No se hace: no emitir DTE real, no pagar, no cerrar el mes, no apretar Aceptar y contabilizar si eso crea un comprobante nuevo, no contabilizar la madre, no usar el origen Tipo de contrato como si fuera la cuenta de una proforma.

### CU-1-03. Balance y libro diario: el cliente no pidió afinarlos

- Ítem de la interna de Sergio. En Reu6 Agustín no pidió dejar estos reportes afinados.
- Pantalla: Contabilidad > Balance de 8 columnas y Contabilidad > Libro diario, solo si ya abren con datos de demo.
- Entra: los asientos que ya existen. No entra un asiento armado para la reunión.
- Se ve: el reporte como revisión interna. Se dice que el cliente no pidió afinarlo.
- No se hace: no cerrar el mes, no generar asientos para cuadrar el balance, no tratar la revisada como requisito.

## 2. Módulo contratistas: ingreso diario, proforma, y la proforma no se parte

### CU-2-01. Ficha del contratista e ingreso diario

- Requisito del cliente (María Jesús, 06/10).
- Pantalla: Contratistas > Listado para el alta. Contratistas > Ingreso diario para el detalle. Cuartel sale del centro de costo (Parametrización > Centros de costo). Faena, labor y sector salen de los catálogos que ya usa el ingreso; el mantenedor del módulo está en Parametrización > Contratista.
- Entra en la ficha: RUT, nombre, dirección, ciudad, comuna, e-mail y proveedor de facturación. El código correlativo (CTR-00001, distinto del RUT) y quién creó la ficha los muestra el listado; el formulario no pide el código a mano.
- Entra en el ingreso: fecha, contratista, cuartel, labor, actividad, tipo jornada o trato, cantidad, precio unitario, predio opcional, temporada, sector y faena. No hay campo de trabajador.
- Se ve: la ficha con código, RUT, nombre y creador, y el ingreso con su total. Los ingresos que todavía no están en una proforma quedan en el indicador Pendientes de proforma.
- No se hace: no pagar, no emitir DTE real, no enviar correo al contratista, no cargar un contrato (el cliente lo saltó el 06/10).

### CU-2-02. Armar la proforma con varios ingresos diarios

- Requisito del cliente (María Jesús, 06/10). El 23/09 la sala dejó el módulo en espera; el 06/10 ella cierra que la proforma no se convierte en OC.
- Pantalla: Contratistas > Proformas y facturas. Se elige contratista y período, y se marcan ingresos que todavía no están en otra proforma.
- Entra: contratista, período, moneda y N ingresos pendientes.
- Se ve: el total de los ingresos marcados. Esos ingresos dejan de estar disponibles para otra proforma. La que sigue el trámite de aprobación es la proforma (modal Solicitar aprobación de proforma, grupo de proformas). Si en la demo ya hay una definitiva, se muestra esa y no se pide autorización nueva.
- No se hace: no aprobar con PIN de un usuario real, no pagar, no emitir la factura del contratista, no apretar Generar OC. Ese botón está en el modal Asociar factura / generar OC de la misma pantalla y choca con el cliente; la asociación que se muestra es la del punto 4, en el libro.

### CU-2-03. La proforma no se parte en hija

- Requisito del cliente (María Jesús, 06/10). Sergio lo repite en la interna; manda la frase de ella.
- Pantalla: la misma, Contratistas > Proformas y facturas, una proforma por su total. La asociación entera se ve en el punto 4.
- Entra: la proforma completa. No entra un monto menor para partirla.
- Se ve: un solo documento, con su monto, sin hija.
- No se hace: no partir la proforma, no generar una hija, no emitir DTE real, no pagar. El mecanismo de OC madre e hija no se rediscute aquí.

## 3. Asignación de la orden de compra en el listado de Compras

El cruce de factura parcial (cantidades, sufijos, multi-ítem) no se recorre. Sigue en `docs/requerimientos/oc-dte-parcial-2026-10-14/`.

### CU-3-01. Asociar a mano la OC del proveedor en el libro de compras

- Requisito del cliente (Lupe en la sala del 23/09, con Mario).
- Pantalla: Compras > Libro de compras, modal Asociar, sobre un recibido cuyo XML no trae OC. Si no hay candidatas, el modal avisa y ofrece notificar: eso se abre en el punto 5 y no se envía.
- Entra: el registro ya sincronizado o cargado, y la OC que ya existe para ese proveedor.
- Se ve: el combo Orden de compra con candidatas abiertas (sin cierre, no anuladas, todavía no cubiertas por el neto de otra factura) filtradas por el nombre del proveedor. Al vincular, el libro guarda `ocId` y `ocNumero`. No nace una OC.
- No se hace: no aceptar ni rechazar el DTE en el SII, no emitir, no pagar, no contabilizar en esta pantalla si la OC todavía no está asociada, no crear la OC desde el libro.

### CU-3-02. Madre e hija visibles en Compras, con la madre solo informativa

- Requisito del cliente en lo contable: la hija se asocia y se contabiliza; la madre no es movimiento. Dónde se muestra la madre lo decidió el usuario para esta demo: Compras > Órdenes de compra, el mismo listado. No se arma una pantalla en Insumos.
- Pantalla: Compras > Órdenes de compra. La fila de la hija dice "Hija de #". El detalle abre el panel Madre / hijas: la hija apunta al número de la madre, y la madre lista hijas con número, estado y neto.
- Entra: una madre ya aprobada y una hija nacida de una recepción parcial del trozo (`crearOcHijaDeRecepcion`: número `madre.N`, estado APROBADO, neto del trozo, cuenta y centro copiados de la línea de la madre).
- Se ve: las dos en el mismo listado, distinguibles. La hija es la que el libro asocia. La madre queda como control, sin comprobante propio.
- No se hace: no mostrar la madre como movimiento contable, no llevarla a ventas ni a tesorería, no pagar, no cerrar el mes, no apretar Cierre de saldo, no recorrer el algoritmo de la factura parcial.

### CU-3-03. La OC se asocia a la factura, no a la guía

- Requisito del cliente (María Jesús, 01/10).
- Pantalla de la asociación: Compras > Libro de compras, la factura con la OC (en el ejemplo de ella, la madre de las cajas y la factura de fin de mes). Pantalla de la guía, solo para decir que es otra cosa: Insumos / Bodega > Guías de insumos recibidas.
- Entra: la factura del libro. La guía, si se abre, es una ya cargada. No se carga una nueva.
- Se ve: la OC colgada de la factura. La guía es el ingreso de material a bodega y no es el documento al que se asocia la OC.
- No se hace: no recepcionar stock real, no emitir guía, no pagar, no tratar la guía como el disparador de la hija.

## 4. Asignación de la proforma al documento de compra

### CU-4-01. Asociar una o varias proformas en el libro de compras

- Requisito del cliente (María Jesús, 06/10; la sala del 23/09 ya había dicho que se asocia a la factura y dejó el módulo en espera).
- Pantalla: Compras > Libro de compras, el mismo modal Asociar. El bloque Proforma aprobada lista proformas DEFINITIVA o ENVIADA_CONTRATISTA que todavía no tienen factura ni orden. Elegir proforma deja vacía la OC, y al revés. El aviso al guardar dice que no se creó una orden.
- Entra: un recibido del libro y una proforma que en la demo ya figure aprobada, por su total (CU-2-03).
- Se ve: número, contratista, monto y estado (Aprobada o Notificada). Una factura del cliente puede juntar varias proformas; el modal marca una por vez.
- No se hace: no emitir el DTE del contratista, no pagar, no enviar el correo, no parcializar la proforma, no pasar por Generar OC de Contratistas > Proformas y facturas.

### CU-4-02. La cuenta contable de la proforma no está dicha

- Ítem de la interna. Carlos pregunta y Sergio la deja para María Jesús. El cliente no la respondió en estas transcripciones.
- Pantalla: la asociación del CU-4-01, sin abrir Contabilizar sobre ese documento.
- Entra: el vínculo proforma > registro. No entra una cuenta.
- Se ve: la proforma colgada del documento. No se muestra una cuenta como si ya estuviera definida. La frase de la línea de la OC (CU-1-02) no se extiende a la proforma. El preview de compra puede rotular un origen Tipo de contrato: eso no se presenta como respuesta de María Jesús.
- No se hace: no inventar la cuenta, no contabilizar la proforma, no cerrar el mes, no pagar.

## 5. Correo de notificación interna

### CU-5-01. Aviso interno cuando la factura de compra no trae OC

- Requisito del cliente (sala del 23/09, con Lupe en el libro; el 01/10 el cliente confirma el aviso). Carlos dijo en esa reunión que el correo todavía no sale y que el aviso interno está maqueteado.
- Pantalla: Compras > Libro de compras, modal Notificar. Se abre desde Asociar cuando no hay OC disponible (Sí, notificar) o desde la acción de notificar del registro.
- Entra: un usuario registrado como destinatario, el texto ya armado (proveedor, folio y monto, sin OC) y el asunto. La casilla de enviar correo se deja apagada.
- Se ve: el destinatario, el texto y, si ya hubo un aviso de demo, el historial con quién avisó, a quién y la fecha. No se confirma el envío.
- No se hace: no enviar el correo, no crear la OC desde el libro, no pagar, no contabilizar esa factura.

### CU-5-02. Correo al contacto cuando la proforma ya está aprobada

- Requisito del cliente (María Jesús, 06/10: mail del contacto del contratista). Sergio, en la interna, lo llama notificación interna.
- Pantalla: Contratistas > Proformas y facturas, una proforma ya aprobada, con el contacto cargado en la ficha (el e-mail está en Contratistas > Listado). La acción está en el botón E-mail y en Contratistas > Envío operativo (período desde / hasta, casilla de correo). Se muestran y no se ejecutan.
- Entra: la proforma aprobada y el e-mail de la ficha. El agrupado que se puede señalar es el rango de período de Envío operativo.
- Se ve: la proforma, el contacto y la acción, sin dispararla.
- No se hace: no enviar el correo, no apretar E-mail, no apretar Notificar contratista (marca el estado), no marcar la casilla de Envío operativo, no emitir la factura, no pagar.

### CU-5-03. Venta: el cliente no pidió correo de notificación

- Ítem de la interna de Sergio.
- Pantalla, si se abre: Administración > Configuración de correos, plantilla VENTAS, dicha como configuración interna. En la misma pantalla están COMPRAS, PROFORMAS y los campos del servidor. No se graba nada.
- Entra: nada como requisito. Los correos que el cliente nombra en Reu6 son de acceso y de datos bancarios, no un aviso al emitir una venta.
- Se ve: que la plantilla existe. No se ve un envío.
- No se hace: no enviar correo de venta, no probar el SMTP contra una casilla real, no pedir las credenciales del correo de Mario.

## Lo que se dice y no se construye en la reunión

Sigue siendo interno, como cierra `casos-de-uso.md`: afinar balance y libro diario; correo de venta con plantilla e imágenes; una cuenta contable de la proforma; el nombre de estado "notificada a proveedor" armado después del corte de luz; una franja fija de tipo de cambio en todas las pantallas; partir la proforma en hija.

## Orden para mostrar los cinco puntos

1. Contabilización. Libro de ventas, una venta ya contabilizada, y el comprobante en Contabilidad > Comprobantes / asientos (detalle e imprimir). Después el libro de compras, un recibido ya asociado a la OC hija, y su comprobante si ya existe. La madre no se abre como asiento. Al cierre de este punto, una mirada a Balance de 8 columnas y Libro diario, dicha como revisión interna.
2. Contratistas. Listado (código, RUT, nombre, dirección, creador), Ingreso diario, y Proformas y facturas con una proforma entera. No se genera OC ni se parte la proforma.
3. Asignación de OC. Compras > Órdenes de compra: madre e hija en el mismo listado y panel Madre / hijas. Libro de compras: modal Asociar sobre un recibido sin referencia, eligiendo una candidata. No se crea la OC ahí. La guía de insumos se nombra, o se abre una ya cargada, para dejar claro que la OC va en la factura.
4. Asignación de proforma. El mismo modal Asociar, ahora el bloque de proforma aprobada, sobre un recibido de demo. Sin contabilizar y sin cuenta.
5. Correo. Modal Notificar del libro, con destinatario y texto, sin confirmar. Luego la proforma aprobada con el contacto y el botón de envío, sin ejecutarlo. Configuración de correos solo si preguntan por la venta: se dice que el cliente no lo pidió.

## Choques que el contraste tiene que mirar

El contraste lee el código. No vuelve al cierre viejo ni abre una pantalla de madre en Insumos. El análisis de `oc-dte-parcial-2026-10-14/contraste-codigo.md` describió un cierre que creaba la hija por el faltante; `implementacion-compras.md` ya dejó `crearOcHijaDeRecepcion` y un cierre que achica la madre. Este plan no rediscute ese algoritmo. Estos son los choques de la demo:

- El botón del detalle de la OC todavía dice "Cierre de saldo (recibido ...)". Dentro del modal, si hay saldo, el botón dice "Achicar y enviar a aprobación" y el texto dice que no se abre otra OC por el saldo que no va a llegar. El contraste comprueba que `solicitarCierreSaldoOc` baja el neto de la madre, la deja `PENDIENTE_APROBACION` y no crea hija. En la demo ese botón no se aprieta: manda la madre de nuevo a la cadena.
- La hija visible en el panel tiene que ser el trozo (`madre.N`, APROBADO, neto recepcionado, `ocPadreId`). Si el listado muestra una hija `BORRADOR` con correlativo `OC-AAAA-NNNN` por el faltante, es el cierre viejo y no se usa como ejemplo.
- Comprobante de venta: las columnas peso, dólar y yuan están en el detalle. El contraste mira, en un asiento de demo, si la glosa es el comentario (folio y descripción corta) repetida en cliente, IVA e ingreso; si el auxiliar es el RUT sin dígito verificador; si la cuenta de IVA débito no sale como caja; y si el nombre del dueño no aparece. Si el documento está en otra moneda y no hay tipo de cambio cargado, mira si usa el del día. No se fabrica un asiento para cumplir la frase.
- Preview de compra: el origen Orden de compra es el que corresponde a CU-1-02. Plan de cuentas y Tipo de contrato no se muestran como la regla de la proforma. CU-4-02 sigue sin cuenta dicha por el cliente.
- Ingreso diario: no hay trabajador, y eso calza con María Jesús. En el formulario leído no están forma de pago, unidad ni duración; faena y sector son opcionales; el cuartel es el centro de costo; hay labor, actividad y un supervisor opcional por ingreso. El contraste confirma si forma de pago, unidad y duración viven en otro control de esa pantalla o faltan. La aprobación que se muestra es la de la proforma, no la de cada ingreso.
- Contratistas > Proformas y facturas tiene el modal Asociar factura / generar OC. Si no hay registro elegido, el botón dice Generar OC y el texto manda al cierre de saldo cuando la factura no cubre el total. Eso choca con "la proforma no se convierte en OC" y con "la proforma no se parte". La demo no entra a ese modal. La asociación que vale es la del libro, cuyo aviso dice que no se creó una orden.
- El modal del libro marca una proforma o una OC, no las dos, y una proforma por acción. El cliente pidió varias proformas en una factura. El contraste mira si un segundo vínculo sobre el mismo registro suma o pisa el anterior.
- Las candidatas de OC salen de `ordenesCompraCandidatasParaRegistro`: abiertas, sin `cerradaAt`, no anuladas, no cubiertas por el neto, y filtradas por nombre de proveedor parecido. El contraste mira si una OC ya tomada por otra factura sigue en la lista, y si el filtro por nombre esconde una OC del mismo proveedor cuando la razón social no coincide con el texto de la factura.
- La guía de insumos es otra pantalla. `implementacion-libro.md` no la tocó y no le guardó `ocId`. El contraste lo confirma. La demo no carga una guía ni recepciona stock.
- Notificar arma destinatario, asunto y cuerpo, y tiene casilla de correo. El contraste mira si confirmar el aviso, aun con la casilla apagada, dispara SMTP. El historial (quién, a quién, fecha) es lo que el cliente pidió como rastro. No se crea la OC desde el libro.
- En la proforma, E-mail llama `enviarProformaEmailContratista` al hacer clic. Notificar contratista marca el estado. Envío operativo manda correo si la casilla está prendida. La demo no ejecuta ninguna de las tres. El contraste mira si Notificar contratista deja la proforma como enviada sin haber salido un correo.
- Administración > Configuración de correos tiene plantillas COMPRAS, VENTAS y PROFORMAS, y los datos del servidor. VENTAS es de la interna. No se graba, no se prueba el envío y no se piden credenciales.
