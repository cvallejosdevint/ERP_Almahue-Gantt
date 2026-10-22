# Plan de pruebas - auditoria octubre 2026

Fecha de lectura: 2026-10-15. Casos: `casos-de-uso.md` (CU-01 a CU-44). Encaje de hoy: `plan-integracion.md`.

Este plan no se ejecuta aqui. No se implementa, no se hace commit, no se emite DTE, no se llama al SII, no se paga, no se cierra el mes y no se corre `prisma migrate deploy`.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`.

La factura de proveedor, cuando un caso la necesita, entra por un registro del libro de compras ya existente o por la carga manual. No se dispara emision ni un evento a GoSocket para ver que pasa. No se guarda, contabiliza ni paga un documento real solo para sacar una foto.

## Como se lee un resultado

Pasa solo la columna "Resultado esperado (sala)".

Un Jest en verde acredita el caso solo si lo que afirma ese spec es la columna de la sala. Si el spec afirma el atajo de hoy, el verde es la columna de hoy.

Estos hechos no son un pase:

- `catalogos.service.spec.ts`, "acepta 45 dias", solo cubre la ficha. No acredita el plazo editable en la OC ni en la factura (P-01 y P-45).
- `comercial.service.spec.ts`, "la glosa conserva el comentario", espera `FACTURA 8/2026 TC: 950.5 ...`. Esa frase es la columna de hoy de P-08.
- `oc-parcial.compras.service.spec.ts` pertenece a otro plan (parcial de septiembre, hija al recepcionar en compras). Sus titulos P-01 a P-10 no son estas pruebas. No se corre ese archivo como evidencia de CU-13: el 14/10 la hija nace con la guia en bodega.
- Saltar un eslabon porque el monto no llega a su tope es lo que hace `approval-engine` hoy. No acredita CU-23 (P-23 y P-54).
- `TipoContratoContratista` no es el contrato de Agrosoft. Que exista no acredita CU-27, y que el ingreso lo pida no es el folio que la sala rechazo.
- La etiqueta "tambien es proveedor" no la pidio la sala. No acredita CU-26.
- `POST /ingresos-labor-diario/:id/aprobar` no acredita CU-31. La frase del 06/10 [18:17] quedo corregida en [24:05].
- Exigir `ENVIADA_CONTRATISTA` para asociar no acredita CU-32 ni CU-36. La sala lista las aprobadas.
- Guardar precio cero no acredita CU-40. La sala dejo el estimativo.
- Un asiento de traspaso ya corrido, o un pago ya hecho, no se usa para forzar CU-38, CU-39, CU-41 ni CU-44.

## Que se corre

- Jest en `ERP/erp_back`, con el mock del spec. No pega a la API local para crear, contabilizar, pagar ni cerrar.
- Pantalla con Playwright (`plugin-playwright-playwright`), ventana completa, sin achicar el viewport. No el navegador interno de Cursor.
- Si la prueba necesita emitir DTE, pagar, cerrar el mes o `prisma migrate deploy`, es observacion de lectura: codigo o pantalla ya abierta. No se muta.

## Fuera de este plan

La sala de octubre no los pidio. No se arma una prueba para que fallen o para tapar un silencio.

- Importar y exportar centros de costo, elementos y codigo financiero.
- Area de negocio.
- Cuenta y centro de costo en el asiento de venta, fuera de lo que piden P-06 a P-09.
- Mas estados que vigente y anulado, y un historial de modificaciones del mantenedor.
- Moneda de pago en la ficha. Maria Jesus confirmo los dias (CU-01).
- Etiqueta "tambien es proveedor" en el contratista.
- Folio de la hija con guion (`-1`, `-2`). Ella no fijo el formato.
- Columna de vencimiento en el comprobante.
- Montos 5.000 y 10.000 de la demo de proforma, y el nombre Felipe con tope 500.000. El dato pedido es que el primer eslabon parta de cero.
- Plan de pruebas de emision de Pablo, resolucion 154, GetDocumentPDF, descarga de XML.
- Sincronizar la guia desde GoSocket. El control que ella describe es la guia en insumos.
- Un grupo que no pueda servir a la vez para OC y para proforma. Lo dijeron Carlos y Sergio sin ella.
- Estado "notificada" como condicion para listar la proforma en compras.
- Cierre semanal obligatorio. La semana le sirve para agrupar y enviar, no como cierre de sistema.
- Maestro Productor. El cierre del 01/10 habla de proveedor y cliente.
- Nota de credito por la frase sucia "orden de credito" del 14/10 [01:01:09].
- Precio cero como regla del ingreso.
- Aprobar el ingreso diario al guardarlo.
- Hija que nace al asociar la factura en el libro de compras. El 14/10 la hace nacer de la guia.
- Portal del proveedor, tarifario cerrado, contrato con GoSocket, emision de prueba entre empresas.
- Salas que no son fuente: `transcripcion-2026-10-13-interna-carlos-sergio.md` y `transcripcion-2026-10-14-jose-sergio.md`. Reu5 no cuenta.

## Indice

| ID | CU | Que cubre |
|---|---|---|
| P-01 | CU-01 | Dos plazos en la ficha, neto e IVA |
| P-02 | CU-02 | Dos fichas que se copian por RUT |
| P-03 | CU-03 | Consulta del RUT, proveedor y cliente juntos |
| P-04 | CU-04 | Anular elemento de costo sin borrarlo |
| P-05 | CU-05 | Historico del Banco Central |
| P-06 | CU-06 | Comprobante en peso, dolar y yuan |
| P-07 | CU-07 | Auxiliar = RUT sin digito verificador |
| P-08 | CU-08 | Glosa = comentario, en cada linea |
| P-09 | CU-09 | IVA debito en la venta |
| P-10 | CU-10 | Aviso a quien debe crear la OC |
| P-11 | CU-11 | Madre de insumos, solo informativa |
| P-12 | CU-12 | OC de servicio, una a una |
| P-13 | CU-13 | La guia en bodega nace la hija |
| P-14 | CU-14 | Libro de guias solo en insumos |
| P-15 | CU-15 | La factura se asocia a las hijas |
| P-16 | CU-16 | Compras lista hijas ya recepcionadas |
| P-17 | CU-17 | Quien ve la madre y quien ve la hija |
| P-18 | CU-18 | Saldo de la madre en insumos |
| P-19 | CU-19 | Guia que no cabe en la madre |
| P-20 | CU-20 | Una edicion de la madre, con aprobacion |
| P-21 | CU-21 | La madre la crea el jefe; la hija, el administrativo |
| P-22 | CU-22 | Cadenas distintas, insumos y servicios |
| P-23 | CU-23 | Toda OC se aprueba, desde cero |
| P-24 | CU-24 | Devolucion a proveedor solo en ALM |
| P-25 | CU-25 | Nomina semanal, historico y banderas |
| P-26 | CU-26 | Ficha de contratista, codigo correlativo |
| P-27 | CU-27 | El flujo no tiene contrato |
| P-28 | CU-28 | Ingreso diario de la labor |
| P-29 | CU-29 | Mantenedores de cuartel y faena |
| P-30 | CU-30 | Armar la proforma eligiendo ingresos |
| P-31 | CU-31 | Se aprueba la proforma |
| P-32 | CU-32 | La proforma no se factura parcial |
| P-33 | CU-33 | Enviar la proforma al contratista |
| P-34 | CU-34 | Editar la aprobada; no editarla si hay factura |
| P-35 | CU-35 | Ver pendientes y aprobadas |
| P-36 | CU-36 | El DTE se asocia en compras |
| P-37 | CU-37 | Cuenta mano de obra contratista |
| P-38 | CU-38 | Centralizacion del mes en un asiento |
| P-39 | CU-39 | Al asociar, facturas por recibir contra proveedor |
| P-40 | CU-40 | Precio estimativo, editable despues |
| P-41 | CU-41 | El cierre trabaja contra proformas |
| P-42 | CU-42 | El correo de la OC es interno |
| P-43 | CU-43 | PDF y Excel de los reportes |
| P-44 | CU-44 | El pago es el de la factura |
| P-45 | CU-01 | Dia libre en la OC y plazo en la factura |
| P-46 | CU-02 | El alta es de jefatura |
| P-47 | CU-05 | Un dia vacio no pisa documentos ya grabados |
| P-48 | CU-12 | La de servicio no admite parcial ni hija |
| P-49 | CU-13 | Sin madre, la guia no entra |
| P-50 | CU-15 | No se elige madre ni guia, ni solo el monto |
| P-51 | CU-16 | Una OC solo aprobada no se lista |
| P-52 | CU-20 | Una recepcion parcial no reabre la cadena |
| P-53 | CU-20 | El segundo cambio lo pide contabilidad |
| P-54 | CU-23 | Ningun eslabon se salta por monto |
| P-55 | CU-24 | Exportacion no devuelve; ALM si, sin mover stock |
| P-56 | CU-31 | Guardar el ingreso no lo aprueba |
| P-57 | CU-32 | Una parte de la proforma no se factura |
| P-58 | CU-34 | Con factura, la proforma no se edita |
| P-59 | CU-36 | Se listan las aprobadas, no solo las notificadas |
| P-60 | CU-40 | El precio cero no queda habilitado |
| P-61 | CU-41 | Un dia sin proforma no entra al asiento |

Un CU con limite se acredita si pasan la prueba alineada y sus limites. El verde de una sola no tapa el borde.

---

## P-01. Dos plazos en la ficha del proveedor

- CU: CU-01. Maria Jesus, 01/10 [18:32] y [18:37].
- Que se hace: Jest `catalogos.service.spec.ts` ("acepta 45 dias") como columna de hoy de la ficha. Playwright en Parametrizacion > Proveedores, `/catalogos/proveedores`, mira los dos campos y no guarda. El dia fuera de la lista, en la OC y en la factura, es P-45.
- Mutacion: no se graba el proveedor.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Ficha | Neto e IVA tienen plazo distinto. Los dias se pueden escribir, por ejemplo 45. No salen solo de una lista. | Guarda `condicionPagoDias` y `condicionIvaDia` (default 10). Acepta un entero manual, por ejemplo 45. |
| Uso | Ese valor se sugiere en los otros modulos y ahi tambien se puede editar. | La OC copia el neto. La factura del libro no tiene plazo propio. El vencimiento del IVA en aging sale de la ficha. |

Criterio de pase: solo la columna de la sala. El Jest de los 45 dias en la ficha no acredita la edicion en el documento.

## P-02. Dos fichas que conversan por RUT

- CU: CU-02. Maria Jesus, 01/10 [18:50] a [26:25]. Manda el cierre [25:50], no la ficha unica de [18:50].
- Que se hace: Playwright en `/catalogos/proveedores` y en Ventas > Clientes, `/comercial/clientes`. Al tipear un RUT que ya esta en la otra ficha, se mira si copia los datos. No se envia el alta. El corte de jefatura es P-46.
- Mutacion: no se crea proveedor ni cliente.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Alta | Dos fichas, no un formulario unico. Un mismo RUT puede ser proveedor y cliente. | Dos maestros, `Proveedor` y `Cliente`. El mismo RUT puede existir en los dos. No se fusionan. |
| Copia | Si el RUT ya existe en la otra ficha, trae la informacion para que el nombre no quede distinto. | `GET /contraparte-por-rut`. Si el alta esta vacia, copia razon social, giro, mail, telefono y direccion. |
| Quien | La creacion queda en una jefatura. | Pide `catalogos:write` o `compras:write` para proveedor, y `comercial:write` para cliente. |

Criterio de pase: solo la columna de la sala. Una copia de datos con el permiso de escritura no acredita la jefatura (P-46).

## P-03. Consulta por RUT con movimientos de proveedor y de cliente

- CU: CU-03. Maria Jesus, 01/10 [27:09] a [27:21]. Depende de CU-02.
- Que se hace: Jest `cuenta-corriente.service.spec.ts` ("fusiona cliente y proveedor del mismo RUT" y "listSaldos agrupa dual por RUT"). Playwright en Tesoreria > Estado de cuenta, `/tesoreria/cuentas-corrientes`, sobre un RUT que ya tenga ficha en los dos lados, si existe. No se crean movimientos.
- Mutacion: ninguna.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Consulta | Un RUT muestra todos sus movimientos, sea proveedor o cliente. El historial no se parte en dos personas. | El estado de cuenta junta los movimientos de cuenta corriente de las dos fichas y separa los saldos. |
| Alcance | Reportabilidad del RUT, documentos de compra y de venta de esa contraparte. | No abre un reporte de OC, facturas y ventas que no hayan pasado por la cuenta corriente. `GET /lookup-rut` solo dice el tipo de ficha. |

Criterio de pase: solo la columna de la sala. Juntar la cuenta corriente no acredita el resto de los movimientos si la sala pidio todos.

## P-04. Anular un elemento de costo sin borrar el historial

- CU: CU-04. Voz sin nombre, sala del 01/10 con Maria Jesus, Fran y Lupe, [17:14] a [17:45].
- Que se hace: Playwright en Parametrizacion > Elementos de costo, `/catalogos/elementos-costo`. Se mira un elemento ya anulado, si hay uno, y el combo de vigencia. No se anula uno vigente para la foto. Jest de lectura: el comprobante, el plan y la cartola no ofrecen el anulado.
- Mutacion: no se cambia la vigencia.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Estado | Vigente o anulado. No hay un tercer estado pedido. | Vigencia `VIGENTE` o `ANULADO`. El alta nace vigente. No hay un tercer estado. |
| Historial | Anulado sigue visible. No se borra la historia. | El listado sigue mostrando el anulado. |
| Uso | Anulado no se ofrece para imputar. | El comprobante, el plan de cuentas y la cartola no lo ofrecen. |

Criterio de pase: solo la columna de la sala.

## P-05. Historico del Banco Central, sin pisar documentos

- CU: CU-05. Voz sin nombre, sala del 01/10, [28:43] a [29:49]. El borde del dia vacio es P-47.
- Que se hace: Playwright en Parametrizacion > Indicadores BC, `/catalogos/indicadores-bc`. Se mira el rango y las monedas ya registradas (el ejemplo de la sala es el yuan). No se lanza la sincronizacion contra el Banco Central.
- Mutacion: no se escribe `IndicadorBc`.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Carga | Historico por moneda ya registrada y por rango, tomado del Banco Central, sin cargar antes una base propia. | `POST /parametrizacion/indicadores-bc/sincronizar` escribe filas (usd, eur, cny y un mapa). Tambien hay importacion CSV o Excel. |
| Documentos | Los documentos ya grabados conservan su tipo de cambio. El historico es consulta. | No recorre OC, facturas ni asientos para cambiarles la tasa guardada. El asiento en pesos no se reescribe. |

Criterio de pase: solo la columna de la sala. Poder sincronizar no acredita que un documento ya grabado conserve su tasa (P-47).

## P-06. Comprobante en peso, dolar y yuan

- CU: CU-06. Voz sin nombre, criterio de contabilidad, sala del 01/10 [32:41] a [33:38]. El 14/10 [56:51] la sala no corrige el pedido.
- Que se hace: observacion de lectura. Playwright en Contabilidad > Comprobantes, `/contabilidad/asientos`, sobre un comprobante de venta ya contabilizado, si la pantalla ya lo tiene. Jest `comercial.service.spec.ts` ("si el tipo de cambio viene vacio usa el dolar del dia" y "usa el tipo de cambio pedido") con mock. No se emite DTE y no se contabiliza un documento nuevo.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Columnas | El comprobante muestra peso, dolar y yuan. Vale para todos los casos, aunque el movimiento venga en otra moneda. | La pantalla y la impresion muestran debe y haber en las tres monedas. El yuan de un documento en pesos se calcula al ver el comprobante. No queda como tercera cifra guardada. |
| Tasa | Si nadie la digita, se toma la del dia en el Banco Central. Al ingresar la factura se puede modificar. | Si al contabilizar no viene tipo de cambio, toma el dolar de `IndicadorBc` de la fecha. El libro deja editarlo antes de contabilizar. |

Criterio de pase: solo la columna de la sala. Ver tres columnas en un comprobante ya abierto no acredita la tasa editable si esa edicion no esta.

## P-07. Auxiliar igual al RUT sin digito verificador

- CU: CU-07. Voz sin nombre, sala del 01/10 [33:48] a [34:02]. Depende de CU-06.
- Que se hace: observacion de lectura del mismo comprobante ya abierto de P-06, y del libro mayor `/contabilidad/mayor`. Jest de la linea de venta: `auxiliar` es el RUT del receptor sin puntos y sin DV. No se contabiliza nada nuevo.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Comprobante | El auxiliar es el RUT de la contraparte, sin digito verificador. | Cada linea del asiento de venta guarda ese RUT sin puntos y sin DV. |
| Mayor | En el mayor tambien se lee ese auxiliar. | El libro diario y el mayor no traen la columna. Muestran glosa, cuenta, debe y haber. |

Criterio de pase: solo la columna de la sala. El auxiliar en el comprobante no acredita el mayor.

## P-08. Glosa igual al comentario, repetida en cada linea

- CU: CU-08. Voz sin nombre, sala del 01/10 [37:23] a [40:16].
- Que se hace: Jest `comercial.service.spec.ts` ("la glosa conserva el comentario") como columna de hoy, no como pase. Playwright del comprobante ya abierto y del mayor, si hay un asiento con comentario. No se contabiliza un documento nuevo.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Texto | La glosa es el comentario ingresado al documento: numero de factura y un poco de la descripcion. Sin el nombre del dueno. Sin rellenar con tipo, folio y tipo de cambio, porque eso ya va al lado. | Si no se manda otra glosa, la cabecera queda `FACTURA mes/anio`, mas el tipo de cambio si hay, mas el comentario. El nombre del dueno no entra. |
| Lineas | El mismo comentario va en la linea de ingreso, en la de cliente y en la de IVA. En el mayor de cliente se lee a que movimiento corresponde. | Esa frase completa se copia en las tres lineas. El mayor muestra la glosa de la linea, o la de la cabecera si no hay. |

Criterio de pase: solo la columna de la sala. Un verde del spec que espera `FACTURA mes/anio TC:` es la columna de hoy.

## P-09. En la venta, la cuenta es IVA debito

- CU: CU-09. Voz sin nombre, sala del 01/10 [38:52].
- Que se hace: Jest `comercial.service.spec.ts` ("grabarDocumentoContabilizar genera linea de IVA a la cuenta fiscal correspondiente") con mock. Playwright del comprobante de venta ya abierto: la linea de IVA. No se emite y no se contabiliza uno nuevo.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Venta | La linea de IVA del comprobante de venta es IVA debito, no caja. | Si hay IVA, usa la cuenta `2-1-09-02-001`. Si el plan no la tiene, contabilizar se detiene. |
| Otros | La sala habla del comprobante de venta que estaban mirando. | En una nota de credito la cuenta es IVA credito. Un asiento viejo dejado en caja, con glosa IVA debito, se muestra como IVA debito y no se reescribe. |

Criterio de pase: solo la columna de la sala. Mostrar la glosa "IVA debito" sobre una cuenta caja no acredita el caso.

## P-10. Avisar a quien debe crear la OC que falta

- CU: CU-10. Voz sin nombre, sala del 01/10 [46:12] a [46:55]. Confirman el aviso del libro de compras.
- Que se hace: Jest `compras.service.spec.ts` ("con la casilla de correo apagada deja el aviso y no encola SMTP") como evidencia del aviso interno. Playwright en Compras > Libro de compras, `/compras/registro`, sobre un registro ya existente sin OC, si hay uno: se mira "Notificar usuario / correo" y la trazabilidad. No se envia el aviso, no se abre SMTP y no se llama a GoSocket.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cuando | Desde el documento sin OC, sin proveedor o con diferencia. | El modal se ofrece tambien cuando el documento no tiene OC. |
| Aviso | Se elige un usuario del sistema y el aviso queda en la trazabilidad. El texto del correo y el SMTP no son pedido de esta sala. | Se elige un usuario de la empresa. Queda aviso en la bandeja y una fila en `RegistroCompraNotificacionEvento`. Si SMTP no responde, el aviso interno igual queda. |

Criterio de pase: solo la columna de la sala. Un correo enviado no hace falta para el pase, y un evento a GoSocket no lo reemplaza.

## P-11. OC madre de insumos, solo informativa

- CU: CU-11. Voz sin nombre el 01/10 [47:20] a [47:43]. Maria Jesus lo cierra el 14/10 [29:09], [34:43], [45:49] y [46:58].
- Que se hace: Playwright en Insumos > Ordenes de insumos, `/insumos/ordenes`, y en el libro de compras. Se mira una madre ya existente, si hay una, con rol `MADRE`. No se crea una OC y no se contabiliza.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Madre | No genera asiento, no mueve el gasto y no aparece como documento asociable en el libro de compras. Vive en insumos. | No arma asiento al crearse. `GET /ordenes-compra` no la lista. `PATCH /registros-compra/:id/vincular-oc` la rechaza. Contabilizar un registro atado a la madre se detiene. Vive en `/insumos/ordenes` con rol `MADRE`. |
| Factura | A compras, para asociar, van las hijas. | La asociacion de hijas es P-15. |

Criterio de pase: solo la columna de la sala. Que la madre no tenga asiento al crearse no acredita que el libro no la ofrezca, si el libro la ofrece.

## P-12. OC de servicio, una a una, con factura directa

- CU: CU-12. Maria Jesus, 01/10 [55:22] a [55:33] y 14/10 [52:18] a [52:35]. El rechazo del parcial es P-48.
- Que se hace: Playwright en Compras > Ordenes de compra, `/compras/ordenes/nueva`, mira el tipo servicio como alta de esa pantalla. No se guarda la OC. La recepcion menor al neto no se confirma: es P-48, Jest de lectura.
- Mutacion: no se guarda la orden.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Tipo | Hay OC de insumos y OC de servicio. La de servicio no se parte en madre e hijas y no espera guia. | `tipo=SERVICIO` no acepta madre ni hija. La recepcion de insumos por `/compras/recepciones` esta cerrada para este caso. |
| Calce | Se aprueba, se recepciona y es siempre una a una. Una recepcion, una factura. | Confirmar la recepcion exige el neto completo. Asociar la factura admite una sola orden de servicio. |

Criterio de pase: solo la columna de la sala. Ver el tipo servicio en el alta no acredita el uno a uno (P-48).

## P-13. La guia en bodega actualiza stock y nace la hija

- CU: CU-13. Maria Jesus, 14/10 [35:06] a [40:12]. Gana sobre el 01/10 [55:49], donde la guia no se asociaba a la OC. Sin madre: P-49. Que no quepa: P-19.
- Que se hace: Jest `insumos.service.spec.ts` ("al recepcionar la guia contra la madre nace una hija APROBADA por el parcial") con mock, como evidencia de hoy. No se corre `oc-parcial.compras.service.spec.ts` para este caso. No se llama `POST /guias-despacho-recibidas/sincronizar`. Playwright en `/insumos/guias-recibidas` solo si ya hay guias, sin guardar una nueva.
- Mutacion: no se recepciona en la empresa. Si "Recibe insumos con guia" esta apagado, no se prende.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Nacimiento | Primero existe la madre. Cada guia recepcionada en insumos actualiza la bodega y crea una hija. El ejemplo: madre de 100 cajas o 100.000, un despacho de 10.000 amarrado a la guia. | Sin madre aprobada, del mismo proveedor y con el articulo en sus lineas, la guia no entra. Si entra, mueve stock con `ENTRADA_PROVEEDOR` y crea una hija `APROBADO`, numero de la madre mas un punto y un correlativo, sin cadena nueva. |
| Factura | Varias guias del mes pueden corresponder a una factura. Esa asociacion es CU-15, no de la guia. | La hija no nace al asociar la factura. El codigo tambien trae la guia DTE 52 y la deja pendiente de asociar. La sala no pidio ese inbox. |

Criterio de pase: solo la columna de la sala. Una hija creada al vincular la factura en el libro no acredita este caso.

## P-14. Libro de guias solo en insumos

- CU: CU-14. Maria Jesus, 14/10 [37:35] a [37:46], [38:05], [50:42] y [51:17] a [51:24].
- Que se hace: Playwright en `/insumos/guias-recibidas` y en Compras > Libro de compras, `/compras/registro`. Se mira si el libro de compras lista guias de despacho. Ventas > Libro de guias, `/comercial/guias-despacho`, es la guia emitida de ventas: se anota aparte, no se usa como el libro de este caso.
- Mutacion: no se sincroniza ni se guarda una guia.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Insumos | La guia, emitida o recibida en la propuesta que ella acepto ubicar, se ve y se opera en insumos bodega. | Las guias recibidas se listan en insumos (`GET /guias-insumo-recibidas` y `GET /guias-despacho-recibidas`). |
| Compras | El libro de compras no lista guias de despacho. | El sincronizado del libro salta el DTE 52 y no lo deja como factura. |

Criterio de pase: solo la columna de la sala. El libro de guias de ventas no acredita el de insumos.

## P-15. La factura de insumos se asocia a las OC hijas

- CU: CU-15. Maria Jesus, 14/10 [36:23] a [40:22] y [41:01]. Los rechazos de madre, guia y match solo por monto son P-50.
- Que se hace: Playwright en `/compras/registro`, sobre un registro ya existente, abre el modal de asociacion y no guarda el vinculo. No se contabiliza. No se llama a GoSocket.
- Mutacion: no se muta el registro.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Eleccion | Desde la factura se eligen N hijas del mismo proveedor, ya nacidas de una guia. El ejemplo que ella acepta: Cartocor, factura 20, ver lo que llego de ese proveedor. Diez guias pueden ser cinco hijas contra una factura, y la madre puede seguir con saldo. | `PATCH /registros-compra/:id/vincular-oc` acepta una o varias OC. Rechaza la madre y una hija de insumos sin guia. Exige el mismo proveedor. Varias hijas quedan en `RegistroCompraOrden`. |
| Monto | No basta un calce solo por monto. No se elige la guia ni la madre. | Compara el monto de la factura con la suma de las hijas y, si la diferencia pasa un peso, deja el registro en alerta. La seleccion es por orden. |

Criterio de pase: solo la columna de la sala. Una alerta de monto no acredita el listado de hijas.

## P-16. Compras solo lista hijas ya recepcionadas

- CU: CU-16. Maria Jesus, 14/10 [49:56] a [50:05] y [55:16] a [55:24]. La OC de servicio solo aprobada es P-51.
- Que se hace: Playwright del mismo modal de P-15, sin vincular. Se anota que tipos de OC aparecen. No se recepciona nada para poblar la lista.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Lista | En compras, para asociar, solo entran las ya recepcionadas. Las pendientes y las solo aprobadas no se ven: "es como que no existe". Tienen que estar listas para contabilizar. | `GET /ordenes-compra` trae OC de servicio e hijas de insumos que ya tienen guia. No trae madres ni hijas sin guia. |
| Servicio | La frase cubre lo que se asocia en ese modulo, no solo la hija de insumos. | Una OC de servicio aprobada y todavia no recepcionada si aparece y se puede asociar. |

Criterio de pase: solo la columna de la sala. Ocultar la madre no acredita el caso si una orden solo aprobada sigue en la lista (P-51).

## P-17. Quien ve la madre y quien ve la hija

- CU: CU-17. Maria Jesus, 14/10 [46:35] a [47:18] y [54:42] a [56:02].
- Que se hace: Playwright con la sesion de lectura de ALMAHUE EXPORT SPA, en `/insumos/ordenes` y en `/compras/ordenes`. No se crea un usuario. Si no hay una sesion ya abierta con solo `insumos:read`, el corte de ese usuario es lectura del guard en codigo.
- Mutacion: no se crea usuario ni permiso.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Insumos | Se ven la madre y la hija. Quien solo tiene insumos ve las OC de ese mundo. | `/insumos/ordenes` lista madre e hija con `insumos:read`. Un usuario con solo ese permiso no entra al libro de compras. |
| Compras | Se ven las hijas listas para contabilizar. Las madres no pasan a compras para asociarlas. Las guias no se ven en el libro de compras. | Compras lista servicio e hijas con guia, y no la madre. Las guias recibidas no estan en el libro. |

Criterio de pase: solo la columna de la sala. El listado de P-16 es parte de este corte: compras no muestra la madre.

## P-18. El saldo de la madre se ve en insumos

- CU: CU-18. Voz sin nombre pregunta; Maria Jesus responde, 14/10 [47:48] a [48:34].
- Que se hace: Playwright en `/insumos/ordenes` sobre una madre ya existente, campo pendiente. En el modal de la factura no se exige ese saldo. No se recepciona para mover el numero.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Insumos | El pendiente de la madre se ve en insumos, no en compras. | `GET /insumos/ordenes` trae `pendiente`: neto de la madre menos hijas no anuladas. La hija repite el pendiente de su madre. |
| Factura | Quien calza la factura con la hija solo necesita que calcen. No entra a ver si falta material. | El modal de asociacion no pide ni muestra ese saldo. Calza ordenes contra el monto del documento. |

Criterio de pase: solo la columna de la sala. Ver el pendiente en el modal de compras no es lo pedido, y no hace falta para el pase de la factura.

## P-19. Si la guia no cabe, se pide modificar la madre

- CU: CU-19. Maria Jesus, 14/10 [41:27] a [41:35] y [49:39] a [49:56].
- Que se hace: Jest `insumos.service.spec.ts` ("rechaza la guia si no cabe en el saldo o la madre esta cerrada, y no nace hija") con mock. No se guarda la guia en la empresa y no se edita la madre en este paso. La edicion es P-20.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Tope | La recepcion no puede pasar el saldo de la madre. El usuario se encuentra el problema ahi, no al calzar la factura. | `assertTopeRecepcion`: si la cantidad o el neto superan lo ya recibido mas lo nuevo, la guia no entra y no nace hija. El mensaje dice que no cabe en el saldo. |
| Salida | El desborde se resuelve pidiendo la edicion de la madre, antes de asociar la factura. | No modifica la madre sola. |

Criterio de pase: solo la columna de la sala. Rechazar el exceso al asociar la factura, sin haberlo frenado en la guia, no acredita el caso.

## P-20. La madre se edita una vez, para arriba o para abajo, con aprobacion

- CU: CU-20. Maria Jesus, 14/10 [30:44] a [32:08] y [43:32] a [45:10]. La parcial que no es edicion es P-52. El segundo cambio es P-53.
- Que se hace: lectura del servicio. `POST /insumos/ordenes/:id/cierre` y `PUT /ordenes-compra/:id` no se llaman contra la API. No se manda una madre a la bandeja para la foto.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Edicion | Una sola edicion de cierre, para arriba o para abajo, y recorre la cadena. Lo pide quien pidio la madre. Sirve para cerrarla: ya no llega mas, o hay que adicionar. | Bajar al recibido: si queda saldo, baja el neto y la madre vuelve a `PENDIENTE_APROBACION`. Si ya no queda saldo, solo marca el cierre y no rearma la cadena. Un cambio de total, para arriba o para abajo, tambien rearma la cadena. |
| Una vez | Si hace falta otro cambio, se pide a contabilidad. No es para corregir cada error. | No hay un segundo cambio reservado a contabilidad. Mientras vuelva a `APROBADO` y no tenga factura que la cierre, se puede volver a editar. Quien edita es el creador o un administrador de la OC. |

Criterio de pase: solo la columna de la sala. Un cierre que deja la madre en `PENDIENTE_APROBACION` no acredita el "una sola vez" ni el segundo cambio de contabilidad.

## P-21. La madre la crea el jefe; la hija, el administrativo

- CU: CU-21. Maria Jesus, 14/10 [41:07] y [52:42] a [53:22]. En [37:50] la hija "se apruebe con la guia".
- Que se hace: lectura de `POST /ordenes-compra` con tipo insumos y del alta de la hija en la recepcion (P-13). No se crea una madre y no se recepciona una guia.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Madre | La crea el jefe y se aprueba una vez. | Solo la crea el aprobador inicial de un grupo de OC de Compras activo. Si el usuario no es ese jefe, la API dice que la madre solo la crea el jefe del grupo. |
| Hija | La genera el administrativo de abastecimiento, en insumos, al recepcionar. No recorre otra vez la cadena. | La graba quien recepciona, con `insumos:write`. Queda `APROBADO` y no arma otra cadena. No hay un permiso que se llame administrativo de abastecimiento. |

Criterio de pase: solo la columna de la sala. Que la hija nazca aprobada no acredita que la madre quede restringida al jefe.

## P-22. Cadenas distintas para insumos y para servicios

- CU: CU-22. Maria Jesus, 14/10 [51:42] a [52:40]. No pidio que un grupo no pueda existir en los dos flujos.
- Que se hace: Playwright en Admin > Reglas de aprobacion, `/admin/aprobaciones`. Se mira si insumos y servicio son dos piezas. No se crea un grupo ni una escala.
- Mutacion: no se muta la configuracion.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| OC | La cadena de una OC de insumos no es la misma pieza que la de una OC de servicio. | Las dos resuelven modulo `Compras` y grupo tipo `OC`. `preview-cadena` no recibe el tipo de OC. |
| Proforma | La proforma tiene su aprobacion aparte (CU-31). Ella no confirmo la exclusividad de grupos. | Una proforma no puede tomar un grupo que no sea tipo `PROFORMA`. Un mismo usuario puede estar en un grupo de OC y en otro de proforma. |

Criterio de pase: solo la columna de la sala. Una cadena de proforma distinta de la de OC no acredita el corte insumos / servicios.

## P-23. Toda OC pasa por aprobacion, desde monto cero

- CU: CU-23. Maria Jesus, 14/10 [32:29] a [33:48]. El salto del eslabon siguiente es P-54.
- Que se hace: Jest `approval-engine.spec.ts` ("el primer eslabon aprueba aunque el monto este bajo su piso" y "Ana $800k entra al primer eslabon aunque este bajo su piso") como columna de hoy. No se envia una OC de 5 pesos a la bandeja de la empresa.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Monto | Aunque sean 5 pesos, pasa por aprobacion. El primer aprobador cubre desde cero. Los almuerzos o la libreria de 10.000 o 15.000 no se aprueban solos. | El primer eslabon entra aunque el monto sea chico. Si la escala devolveria la OC aprobada sola por monto, la API rechaza el envio. |
| Escala | Pueden existir escalas por monto para saber quien firma. Nadie se salta la cadena. Felipe y 500.000 son ejemplo de Carlos, no un tope pedido. | Del segundo eslabon en adelante, un tope que el monto no alcanza se salta. Un neto cero o negativo no entra al calculo: el envio queda pendiente y puede no crear fila de aprobador. |

Criterio de pase: solo la columna de la sala. Que el primer eslabon reciba un monto chico no acredita el caso si un eslabon posterior se omite (P-54).

## P-24. Devolucion a proveedor solo en ALM

- CU: CU-24. Voz sin nombre, sala del 01/10 [59:35] a [01:00:18]. El corte de las dos empresas, sin mover stock, es P-55.
- Que se hace: Playwright en Admin > Empresas, se lee el checkbox "Permite devolucion a proveedor" de ALMAHUE EXPORT SPA. No se cambia. Jest `insumos.service.spec.ts` ("rechaza devolucion a proveedor si la empresa no la permite") con mock.
- Mutacion: no se confirma `SALIDA_PROVEEDOR`, `DEVOLUCION` ni `DEVOLUCION_NC`.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Corte | ALM puede devolver material al proveedor. Almahue exportacion no usa ese reintegro. La diferencia es por empresa. | Esos tres tipos se rechazan si la empresa no tiene el flag. El default es apagado. No hay un nombre de empresa escrito en el codigo. |
| Stock | La salida, cuando la empresa la tiene, es el reintegro de bodega. | Si se confirma, baja el stock de la bodega de origen. Esta prueba no la confirma. |

Criterio de pase: solo la columna de la sala. Ver el checkbox no acredita las dos empresas (P-55).

## P-25. Nomina semanal, historico y banderas

- CU: CU-25. Lupe, 01/10 [48:21] a [49:59]. La sala dice que si.
- Que se hace: Playwright en Tesoreria > Nomina semanal, `/tesoreria/nominas`. Se miran la vista del periodo, el historico, el filtro y las banderas ya guardadas. No se graba un umbral nuevo en la empresa.
- Mutacion: no se hace `PUT /nomina-plazos`.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Vistas | Periodo actual partido en semanas, con pendientes y atrasados. Historico por rango de fechas. Filtro de solo pendientes o todos. | La vista del periodo parte el mes en semanas y cuenta pendientes. El historico filtra por rango de semanas. El filtro cambia entre pendientes y todos. |
| Banderas | Umbral, nombre y color configurables. 7, 30 y 90 son el ejemplo de partida, no un candado. Se puede agregar otra. | Viven en la empresa (`nominaEtiquetas`): dias, nombre y color, hasta ocho. El default de codigo es atrasada desde 1 dia, critico a los 30 y otra a los 90. Esos dias se pueden cambiar. |

Criterio de pase: solo la columna de la sala. El default 1 / 30 / 90 no es un fallo por no ser 7, y tampoco acredita el caso si el umbral no se puede configurar. Esta prueba no graba el cambio: la columna de hoy sale del codigo que ya deja editarlos.

## P-26. Ficha de contratista con codigo correlativo

- CU: CU-26. Maria Jesus, 06/10 [14:13] a [14:48].
- Que se hace: Playwright en Contratistas > Listado, `/contratistas`, mira codigo, RUT, nombre, direccion y quien crea, en una ficha ya abierta o en el alta sin enviar. No se graba un contratista.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Codigo | Correlativo numerico. Si hay 10, el siguiente es el 11. No es el RUT. El codigo de proveedor si es el RUT. | Codigo propio `CTR-` mas cinco digitos, distinto del RUT. El codigo de proveedor sigue siendo el RUT. |
| Ficha | Codigo, RUT, nombre, direccion y la persona que la crea. | Guarda RUT, razon social, direccion y `creadoPorId`. Tambien exige ciudad y comuna. Si el RUT ya es proveedor, deja `proveedorId` y muestra la etiqueta. La sala no pidio la etiqueta. |

Criterio de pase: solo la columna de la sala. La etiqueta "tambien es proveedor" no acredita la ficha. El prefijo `CTR-` se anota en la columna de hoy; el pase es el correlativo distinto del RUT y los datos que ella nombro.

## P-27. El flujo de contratista no tiene contrato

- CU: CU-27. Maria Jesus, 06/10 [12:23] a [13:03].
- Que se hace: Playwright en `/contratistas/ingreso-diario`. Se mira si el formulario pide un contrato o un folio de contrato. No se guarda el ingreso.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Contrato | El ingreso diario no exige un contrato vigente ni un folio de contrato. En este punto se quedan con AgroSmart, no con el paso de Agrosoft. | No hay pantalla ni modelo de contrato con folio. El ingreso no pide ese folio. |
| Otro dato | La sala no pidio un tipo contable. | Si pide `TipoContratoContratista` (cuentas de debe, haber y administracion). Si la empresa no tiene uno activo, el ingreso no se guarda. Ese tipo no es el contrato. |

Criterio de pase: solo la columna de la sala. Que no haya folio de contrato es el pase. Que exista el tipo contable no acredita el caso y no se lee como el contrato rechazado.

## P-28. Ingreso diario de la labor

- CU: CU-28. Maria Jesus, 06/10 [14:51] a [16:36]. El 14/10 [06:03] Carlos muestra sector y faena como opcionales; el unico opcional que ella nombra asi es el predio.
- Que se hace: Playwright en `/contratistas/ingreso-diario`, sin guardar. Se miran los campos. No se exige un trabajador.
- Mutacion: no se guarda el ingreso.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Campos | Fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duracion, valor unitario del trato o de la jornada, cantidad y total. Jornal o a trato. | Guarda fecha, contratista, centro de costo (la pantalla lo llama cuartel), labor, actividad, jornada o trato, unidad, cantidad, precio y total. |
| Opcional | Predio opcional. Agricola lo necesita; ALM no. Sin trabajador obligatorio. El mismo funcionamiento para las dos empresas, no amarrado a una sola. | Predio, temporada, sector y faena son opcionales. No hay trabajador. El registro es por empresa. Al guardar queda `PENDIENTE`. |

Criterio de pase: solo la columna de la sala. Dejar sector y faena vacios en la pantalla de hoy no acredita que dejen de ser datos del ingreso. El predio si puede ir vacio.

## P-29. Mantenedores de cuartel y faena

- CU: CU-29. Maria Jesus, 06/10 [16:39] a [17:22]. Voz sin nombre de la sala del 14/10 [16:24]: al elegir la labor aparece la actividad.
- Que se hace: Playwright en Parametrizacion > Contratista, `/catalogos/contratista`, y en el ingreso diario, sin guardar. Se mira si cuartel y faena se eligen, y si al elegir la labor la actividad queda determinada.
- Mutacion: no se crea labor, faena ni cuartel.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Mantenedor | Cuartel y faena no se escriben a mano. Hay faenas de agricola y faenas puntuales de ALM (servicio administrativo, armado de cajas). | Labor, actividad, sector y faena se eligen de mantenedor. No hay un mantenedor que se llame cuartel: el ingreso usa el centro de costo, etiqueta "Cuartel / centro de costo". Faena sigue atada a un sector. |
| Actividad | Al elegir la labor, la actividad queda determinada. | Si la labor tiene una sola actividad vinculada, se llena sola. Si tiene varias, hay que elegirla. |

Criterio de pase: solo la columna de la sala. Un centro de costo con la etiqueta "cuartel" se anota en la columna de hoy. El pase es que cuartel y faena se elijan de mantenedor y que la labor determine la actividad.

## P-30. Armar la proforma eligiendo ingresos

- CU: CU-30. Maria Jesus, 06/10 [13:14] a [20:10] y [26:33] a [26:51]. El 14/10 [12:50] a [13:07] repite que cinco ingresos se agrupan en una.
- Que se hace: Playwright en Contratistas > Proformas y facturas, `/contratistas/proformas`, sobre ingresos ya existentes, si los hay. No se arma una proforma nueva y no se asocia una factura.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Armado | Ella elige cuales van. De 30 ingresos puede armar 2 o 3 proformas. Puede ser diaria, semanal, o por rango de fecha o por labor. El total es lo seleccionado. | Se eligen varios ingresos del mismo contratista, del mismo periodo y del mismo tipo contable. El monto es la suma. En un mes caben varias. |
| Bloqueo | El ingreso usado ya no queda para otra proforma. La proforma no se convierte en una OC. | El ingreso pasa a `ASOCIADO` y no vuelve a ofrecerse. Una proforma no crea una OC. El alta de factura exige un registro que ya este en el libro. |

Criterio de pase: solo la columna de la sala. Una proforma creada desde el ingreso no acredita el caso si ese ingreso sigue disponible para otra, o si la proforma se vuelve OC.

## P-31. La que se aprueba es la proforma

- CU: CU-31. Maria Jesus, 06/10. Manda [24:05], no [18:17]. El 14/10 [13:08] y [11:09]: la aprueba el jefe de campo. El borde del ingreso al guardar es P-56.
- Que se hace: Jest `contratistas.service.spec.ts` ("BORRADOR a PENDIENTE_APROBACION al solicitar aprobacion" y "bajo el primer piso entra al primer eslabon y no queda DEFINITIVA sola") con mock. No se envia una proforma de la empresa a la bandeja. Los montos 5.000 y 10.000 no se usan como dato pedido.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Proforma | La aprobacion interna es de la proforma, por la jefatura (en la sala, el jefe de campo). Recien aprobada se asume que la labor de esa semana si se hizo. | La proforma en borrador arma la cadena de Contratistas y pasa a `PENDIENTE_APROBACION`. El primer eslabon no se salta por monto. Si no hay grupo de proformas, no se puede enviar. |
| Ingreso | El ingreso diario no queda aprobado uno a uno al guardarse. | El ingreso nuevo queda `PENDIENTE` y no entra a la bandeja. Sigue existiendo `POST /ingresos-labor-diario/:id/aprobar`. |

Criterio de pase: solo la columna de la sala. Ver la proforma en la bandeja no acredita el caso si el ingreso se aprueba al guardarse (P-56).

## P-32. La proforma no se factura parcial

- CU: CU-32. Maria Jesus, 06/10 [25:07] a [25:48] y [29:13] a [29:33]. La fraccion 5.600 de 9.600 es P-57.
- Que se hace: lectura de `POST /proformas-contratista/:id/factura`. No se asocia un registro de la empresa y no se contabiliza.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Completa | Una proforma se asocia completa. Varias proformas caben en una factura. No se factura una parte. | Cada proforma del grupo pasa entera a `FACTURADA` y sus ingresos a `FACTURADO`. Varias del mismo contratista, moneda y tipo caben mientras la suma no pase el neto del registro. No deja un saldo de una parte. |
| Estado | La asociacion exige la proforma aprobada. Una diferencia se corrige en el ingreso de origen. | Para asociar, tiene que estar `ENVIADA_CONTRATISTA` y sin reclamo abierto. Una `DEFINITIVA` todavia no enviada no entra. |

Criterio de pase: solo la columna de la sala. Asociar varias proformas enteras no acredita el caso si una fraccion tambien entra (P-57), ni si una aprobada sin envio queda fuera.

## P-33. Enviar la proforma al contratista

- CU: CU-33. Maria Jesus, 06/10 [25:52] a [30:29]. El 14/10 [19:22] la sala dice "buenisimo" al ver notificar con correo.
- Que se hace: Playwright en una proforma ya aprobada, si la lista ya la muestra. Se mira la accion de envio y la constancia. No se envia el correo y no se abre SMTP. El contratista no tiene bandeja: se lee en el codigo, no se le crea un usuario.
- Mutacion: no se llama `enviar-email` ni `enviar-contratista` contra la API.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Envio | Desde una proforma aprobada se envia al mail del contacto, con el documento. Queda constancia de cuales ya se enviaron, para no repetirlas en el cierre siguiente. | Notificar pasa de `DEFINITIVA` a `ENVIADA_CONTRATISTA` y guarda quien y cuando. El correo sale al mail de la ficha, plantilla `PROFORMAS`, y marca `emailContratistaAt`. Un envio operativo solo toma las ya notificadas que no esten en otro paquete. |
| Contratista | No entra al ERP a aprobar. Si reclama precio o jornada, se edita el origen. | No tiene usuario ni bandeja. El reclamo deja `reclamadaAt` y un motivo, sin cambiar el estado, y bloquea la factura hasta reenviar. |

Criterio de pase: solo la columna de la sala. Un estado "notificada" usado como filtro del libro de compras no es este caso: eso no lo confirmo ella (P-59).

## P-34. Editar la proforma aprobada; cerrarla si ya hay factura

- CU: CU-34. Maria Jesus, 06/10 [30:33] a [30:45] y 14/10 [01:00:17] a [01:01:14]. La proforma ya facturada es P-58.
- Que se hace: Jest `contratistas.service.spec.ts` ("reversa DEFINITIVA a BORRADOR con clave de reversa valida") con mock, como la via de hoy de una aprobada. No se reversa una proforma de la empresa.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Aprobada | Si ya paso la aprobacion interna y hay que editarla, vuelve a la cadena. La modificacion es con solicitud. | `PUT` solo acepta borrador. Una definitiva o enviada se puede devolver a borrador con la clave de reversa, y ahi hay que volver a pedir la cadena. |
| Facturada | Si ya esta asociada a una factura recibida, no se edita. | Una facturada no entra a la reversa ni al reclamo. |

Criterio de pase: solo la columna de la sala. Reversar una definitiva no acredita el cierre de la ya facturada (P-58). No se busca una nota de credito.

## P-35. Ver proformas pendientes y aprobadas

- CU: CU-35. Maria Jesus, 13/10 [05:50]. El 14/10 [20:19] el listado de gasto son las aprobadas; la pendiente es informativa. Eso no borra este listado.
- Que se hace: Playwright en `/contratistas/proformas`. Se miran los estados y el filtro. No se cambia una proforma. La asociacion del DTE no se hace en esta pantalla.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Lista | En contratistas se ven las pendientes y las aprobadas, distinguibles. | Cada fila trae estado: borrador, pendiente de aprobacion, definitiva, enviada, facturada o rechazada. |
| Filtro | Los dos conjuntos se pueden distinguir. | El filtro tiene todos, pendientes y facturadas. "Pendientes" junta borrador, pendiente de aprobacion, definitiva y enviada. No hay un filtro que se llame "aprobadas" y deje fuera el borrador. |

Criterio de pase: solo la columna de la sala. Un filtro llamado pendientes que mezcla aprobadas y sin aprobar no alcanza si los dos conjuntos no se distinguen.

## P-36. El DTE se asocia en compras; el costo se imputa en contratistas

- CU: CU-36. Maria Jesus, 06/10 [24:32] a [24:41] y 13/10 [05:59] a [08:54]. El listado de aprobadas, no solo notificadas, es P-59.
- Que se hace: Playwright en `/compras/registro` y en la proforma. Se mira donde se elige la proforma y si el libro edita la cuenta. No se asocia y no se contabiliza.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Lugar | En el libro de compras se elige proforma o OC. La cuenta no se edita ahi. El dato de la cuenta viaja desde contratistas. | La asociacion esta en la proforma: `POST /proformas-contratista/:id/factura`, eligiendo un registro (`GET /contratistas/registros-compra-asociables`). El libro no tiene selector de proforma y no edita la cuenta. |
| Costo | El costo de la proforma aprobada puede quedar imputado antes del calce. No exige que la factura ya exista. | El costo del mes lo arma el traspaso con la cuenta fija de mano de obra, aunque la factura no este asociada. `cuentaGastoId` se guarda en la proforma y el traspaso no la usa como debe. |

Criterio de pase: solo la columna de la sala. Asociar desde la proforma no acredita la eleccion en el libro de compras. Listar solo las enviadas no acredita el listado de aprobadas (P-59).

## P-37. Cuenta mano de obra contratista

- CU: CU-37. Maria Jesus, 14/10 [10:41] a [14:16].
- Que se hace: lectura de `resolveCuentasCierreSala` y del ingreso (P-28). Playwright del ingreso diario, sin guardar, para ver labor, actividad y centro de costo. No se traspasa el mes.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cuenta | Una cuenta de gasto, mano de obra contratista, para el modulo. La proforma no pide una cuenta por linea. | El debe del cierre es `6-1-01-01-002` o, si no esta el codigo, una cuenta de gasto cuyo nombre es mano de obra contratista. El haber es facturas por recibir contratistas, `2-1-08-02-003`. No pide una cuenta distinta por linea. |
| Detalle | El ingreso guarda labor, actividad y centro de costo. El detalle se analiza por centro de costo, labor y actividad. | El asiento agrupa por centro de costo. Labor y actividad quedan en el ingreso, no en una linea del asiento. |

Criterio de pase: solo la columna de la sala. Una cuenta por linea en la proforma no es el caso, y el codigo que no la pide no acredita el nombre de la cuenta si esa cuenta no es la del cierre.

## P-38. Centralizacion del mes en un asiento

- CU: CU-38. Maria Jesus, 13/10 [07:40] a [08:49] y 14/10 [11:19] a [15:30] y [20:10] a [20:28].
- Que se hace: observacion de lectura. Playwright en Contratistas > Traspaso contable y cierre de mes, `/contratistas/traspaso`, sin pulsar el cierre. Jest `contratistas.service.spec.ts` ("pasa periodo YYYY-MM a createAsiento" y "rechaza re-traspaso de periodo ya cerrado") con mock. No se hace `POST /contratistas/traspaso-cierre`.
- Mutacion: no se cierra el mes.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Menu | Un menu, "Traspaso contable y cierre de mes", debajo de auditoria. Ahi informa que mes cierra. | Esa ruta existe, debajo de Auditoria. `/contabilidad/centralizacion` redirige ahi. |
| Asiento | Un cierre por mes, un asiento agrupado, solo proformas aprobadas. El gasto queda en el mes de la proforma, aunque la factura llegue al mes siguiente. La pendiente de aprobacion es informativa y no entra al gasto. | Un cierre por empresa y periodo `aaaa-mm`. Toma `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA`. Deja fuera borrador, pendiente de aprobacion y rechazada. Un asiento, origen `TRASPASO-CTR:periodo`. El periodo es el de la proforma. Si ya esta cerrado, no lo vuelve a traspasar. |

Criterio de pase: solo la columna de la sala. Un asiento ya existente no se usa para cerrar otro mes. No correr el cierre no convierte el caso en pase: la columna de hoy se lee del codigo y del spec con mock.

## P-39. Al asociar la factura, facturas por recibir contra proveedor

- CU: CU-39. Maria Jesus, 13/10 [07:55] a [08:21] y 14/10 [14:27] a [14:42].
- Que se hace: observacion de lectura. Si ya hay un registro asociado a una proforma, se puede abrir `GET /registros-compra/:id/asiento-preview` sin guardar. Si no hay, se lee el servicio. No se hace `PUT` a contabilizado y no se llama a GoSocket.
- Mutacion: no se contabiliza.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Calce | Al asociar en compras, el asiento es facturas por recibir contratista contra el proveedor. No vuelve a reconocer el gasto. Junto con el asiento de CU-38, el gasto queda contra el proveedor. | Si la proforma ya apunta al registro y tiene tipo contable, el asiento es debe `2-1-08-02-003` y haber proveedores, mas el IVA si corresponde. No vuelve a cargar el gasto. En ese caso no exige una OC. |
| Cuenta | La cuenta no se reescribe en compras. | Sale del plan por codigo. El libro no la edita. |

Criterio de pase: solo la columna de la sala. Contabilizar el registro para ver el asiento no es esta prueba. Un preview que vuelva a debitar la mano de obra no pasa.

## P-40. Precio estimativo en el trato, editable despues

- CU: CU-40. Voz sin nombre pregunta el 14/10 [59:15]; Maria Jesus fija la regla hasta [01:00:17]. El cero es P-60.
- Que se hace: Playwright en el ingreso a trato, sin guardar. Se mira si el precio se puede cargar y si el formulario deja corregirlo en un ingreso pendiente ya existente, sin enviar el `PUT`.
- Mutacion: no se guarda el precio.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Estimativo | Se registra la labor antes del precio definitivo, con un valor estimativo, y despues se corrige. Ella dice que la edicion no tiene problema. | Si hay tarifa vigente, el precio sugerido es esa tarifa. Cambiarlo pide `contratistas:rate-override` y un motivo. El ingreso solo se edita mientras esta pendiente, o cuando la proforma enviada esta en reclamo. Una definitiva sin reclamo no deja corregir el precio. |
| Despues | Si la proforma de ese ingreso ya esta aprobada o facturada, la correccion sigue CU-34. | Esa via es el reclamo y la reversa, no una edicion directa de la facturada. |

Criterio de pase: solo la columna de la sala. Poder guardar un precio no acredita el caso si el cero tambien queda habilitado (P-60), ni si una aprobada sin factura no se puede corregir volviendo a aprobacion.

## P-41. El cierre de mes trabaja contra proformas

- CU: CU-41. Maria Jesus, 14/10 [01:01:15] a [01:02:53]. El dia sin proforma es P-61.
- Que se hace: observacion de lectura del mismo traspaso de P-38 y de `POST /contratistas/traspaso-cierre/:periodo/reabrir`. No se cierra el mes y no se reabre.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Proforma | Un dia con labor y sin proforma no entra al asiento. El cierre no se lo lleva solo por existir el ingreso. Ese dia tiene que tener su propia proforma. Pueden ser muchas (ella habla de 20) y se asocian a las facturas. | Un ingreso sin proforma no entra al asiento. No hay tope de una proforma por mes. |
| Reabrir | Si cerraron el mes y quedo una proforma pendiente, el mes se puede volver a abrir. | Reabrir anula el asiento del traspaso si el periodo contable no esta cerrado. Si el periodo contable sigue cerrado, pide abrirlo primero. Esta prueba no lo ejecuta. |

Criterio de pase: solo la columna de la sala. No se cierra ni se abre el mes para comprobarlo. La columna de hoy sale del codigo.

## P-42. El correo de la OC es interno

- CU: CU-42. Voz sin nombre, sala del 14/10 [22:22] a [23:10] y [26:03]. Habla en primera persona del departamento. No es CU-10 ni CU-33.
- Que se hace: Playwright en la OC, `/compras/ordenes`. Se busca la accion de avisar a un usuario interno, con copia y con un correo externo escrito a mano. No se envia nada.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Aviso | Desde la OC se avisa a un usuario del sistema, con el documento. Se puede agregar copia. Un correo de alguien que no esta en la plataforma se escribe a mano y no toma el nombre del destinatario. | No hay pantalla ni endpoint que envie la OC. La orden no tiene "notificar". |
| Alcance | No queda pedido un portal para el proveedor. | El correo que existe en compras es el del libro (CU-10), sobre la factura recibida. No adjunta la OC. No hay portal de proveedor. |

Criterio de pase: solo la columna de la sala. El aviso del libro de compras no acredita el correo de la OC.

## P-43. PDF y Excel de los reportes contables

- CU: CU-43. Voz sin nombre, sala del 14/10 [57:42] a [59:07]. Sergio pregunta por el PDF; la sala dice que de todo, y pide la descarga del estado de resultados.
- Que se hace: Playwright, ventana completa, en libro diario `/contabilidad/libro-diario`, libro mayor `/contabilidad/mayor`, balance de ocho columnas `/contabilidad/balance-8-columnas` y estado de resultados `/contabilidad/estado-resultados`. Se abren Excel y PDF de lo ya cargado. El PDF se lee por la ventana de impresion: empresa, nombre del reporte y periodo. No se cierra un mes para tener cifras.
- Mutacion: no se muta. Exportar el reporte no guarda un documento comercial.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cuatro | Libro diario, libro mayor, balance de ocho columnas y estado de resultados se exportan a PDF y a Excel. | Los cuatro tienen Excel y "Exportar PDF". |
| Formato | El PDF identifica empresa, reporte y periodo. El Excel respeta las columnas de la grilla. | El Excel exporta las columnas de la grilla. El PDF abre la ventana de impresion con razon social, RUT, domicilio si existe, nombre del reporte, periodo y la tabla. |

Criterio de pase: solo la columna de la sala. La situacion financiera usa la misma pagina y la sala no la pidio: no entra en el pase ni en el fallo.

## P-44. El pago del contratista es el de la factura asociada

- CU: CU-44. Maria Jesus, 06/10 [13:03] y [25:22].
- Que se hace: observacion de lectura. Playwright en Contratistas, se mira si hay un documento de pago propio. En Tesoreria > Pagos, `/tesoreria/pagos`, se lee que el pago es contra el registro de compra o el proveedor. No se hace `POST /pagos`.
- Mutacion: no se paga.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Pago | Despues del calce, el pago es el de esa factura de proveedor. El recorrido que ella nombra termina en facturacion y pago. | El saldo por pagar queda en la cuenta del proveedor y en el aging. El pago vive en tesoreria. |
| Modulo | No hay nomina, anticipo ni documento de pago distinto para el contratista. | No hay un pago dentro de contratistas. La nomina de CU-25 es la de tesoreria, para cualquier documento con vencimiento. |

Criterio de pase: solo la columna de la sala. No se registra un pago para comprobarlo. Ver que contratistas no tiene documento de pago propio, y que el pago de la factura esta en tesoreria, es la lectura de las dos columnas.

---

## Limites

Cada limite es un borde que la sala dijo. No reemplaza la prueba del CU. Un pase de la prueba alineada no tapa el limite.

## P-45. Dia libre en la OC y plazo editable en la factura

- CU: CU-01. El ejemplo de 45 dias es de Maria Jesus, 01/10 [18:37]. La condicion se sugiere y se puede editar en el documento. Apoyo 23/09 [12:16] y [13:04], Mario y Lupe: en la OC se pueden editar.
- Que se hace: Playwright en Compras > Ordenes de compra, `/compras/ordenes/nueva`, sin guardar. Se intenta un dia que no sea 30, 60 ni 90. En un registro del libro ya existente se mira si neto e IVA tienen plazo propio editable. No se guarda la OC ni el registro. No se contabiliza.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| OC | El plazo sugerido se puede cambiar. Un dia nuevo, por ejemplo 45, se puede ingresar. | El combo muestra 30, 60, 90 y el valor que ya trae el formulario. Un 45 de la ficha se puede elegir. En la OC no se tipea un dia nuevo. La API conserva el entero que reciba. |
| Factura | En la factura tambien se puede editar. Son dos plazos. | La factura del libro no tiene plazo propio. En aging, el IVA sale de `condicionIvaDia` del proveedor. |

Criterio de pase: solo la columna de la sala. Elegir el 45 que ya vino de la ficha no acredita tipear un dia nuevo, ni el plazo de la factura.

## P-46. El alta de proveedor y de cliente es de jefatura

- CU: CU-02. Maria Jesus, 01/10 [24:38] a [26:25]. Hoy la hace ella. No es de un digitador cualquiera.
- Que se hace: lectura del permiso de `POST /proveedores` y `POST /clientes`. Playwright no envia el alta. No se crea un usuario de prueba.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Quien | La creacion queda en una jefatura, por seguridad. | Proveedor: `catalogos:write` o `compras:write`. Cliente: `comercial:write`. No hay un corte de jefatura distinto de ese permiso. |

Criterio de pase: solo la columna de la sala. Un alta que copia el RUT con permiso de escritura no acredita la jefatura.

## P-47. Un dia que estaba vacio no reescribe el tipo de cambio ya guardado

- CU: CU-05. La sala acepta que el historico no pisa los otros modulos, 01/10 [28:43] a [29:49].
- Que se hace: observacion de lectura del comprobante y del servicio de indicadores. No se lanza la sincronizacion. No se abre un asiento para regrabarlo.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Documento | Un documento ya grabado conserva su tipo de cambio. | El asiento guardado en pesos no se reescribe. La pantalla del comprobante, al armar dolar y yuan, vuelve a leer la tasa de esa fecha si la linea no trae el monto en esa moneda. |
| Dia vacio | Llenar el historico no transforma lo ya cargado. | Llenar un dia que antes estaba vacio puede cambiar lo que se ve en esas columnas. |

Criterio de pase: solo la columna de la sala. No recorrer las tablas para hacer un update no acredita el caso si al abrir el comprobante la columna cambia.

## P-48. La OC de servicio no admite parcial ni hija

- CU: CU-12. Maria Jesus, 14/10 [52:18] a [52:35]: es siempre una a una. La que llega por partes es la de insumos.
- Que se hace: Jest de lectura de `POST /recepciones-oc` para una orden `SERVICIO` con cantidad menor al neto, con mock. No se confirma la recepcion en la empresa.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Parcial | Una OC de servicio no se recepciona por partes. Una recepcion, una factura. | Confirmar la recepcion exige el neto completo. No deja un parcial. |
| Hija | No se parte en madre e hijas y no espera guia. | No acepta madre ni hija. La recepcion de insumos por esa pantalla esta cerrada. |

Criterio de pase: solo la columna de la sala. Rechazar el parcial y ademas crear una hija seria fallo. Rechazar el parcial sin hija es la columna de hoy; el pase es que eso sea lo que queda.

## P-49. Sin madre, la guia no entra

- CU: CU-13. Maria Jesus, 14/10 [37:50] y [39:35]: primero existe la madre. Sin madre no hay guia asociable.
- Que se hace: Jest `insumos.service.spec.ts` ("sin madre no asocia la guia y no nace hija") con mock. No se digita una guia en la empresa y no se sincroniza GoSocket.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Guia | Sin madre no hay guia asociable. No actualiza la bodega y no nace hija. | Sin madre aprobada, del mismo proveedor y con el articulo en sus lineas, la guia no entra. |
| Inbox | La sala no pidio traer la guia desde GoSocket. | El codigo la trae y la deja pendiente hasta asociarla a la madre. Tambien se puede digitar sin ese inbox. El inbox no acredita el caso. |

Criterio de pase: solo la columna de la sala.

## P-50. No se elige la madre, ni la guia, ni un calce solo por monto

- CU: CU-15. Maria Jesus, 14/10 [36:23] a [36:47] y [39:03]. No quiere un calce "por monto". No asocia la guia. No asocia la madre.
- Que se hace: Playwright del modal de un registro ya existente, sin confirmar el vinculo. Se anota si la madre o la guia aparecen como elegibles. No se contabiliza y no se llama a GoSocket.
- Mutacion: no se guarda el vinculo.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Eleccion | Se eligen las hijas ya nacidas de una guia, del mismo proveedor. | Rechaza la madre, rechaza una hija de insumos sin guia y exige el mismo proveedor. |
| Monto | No basta que el monto coincida. | Si la diferencia pasa un peso, el registro queda en alerta. La seleccion sigue siendo por orden. La alerta de monto no reemplaza el listado. |

Criterio de pase: solo la columna de la sala. Una alerta `MONTO_NO_COINCIDE`, o el nombre que use el codigo, no acredita el caso.

## P-51. Una OC solo aprobada no se lista para asociar

- CU: CU-16. Maria Jesus, 14/10 [55:16] a [55:24]: en compras no van las pendientes ni las que estan solo aprobadas.
- Que se hace: Playwright del listado de asociacion, sin vincular. Se busca una OC de servicio en `APROBADO` que todavia no tenga recepcion, si ya existe en la empresa. No se aprueba ni se recepciona una orden para armar el dato.
- Mutacion: no se muta. Si no hay esa orden, la columna de hoy se lee del filtro de `GET /ordenes-compra`.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Lista | Una OC que esta solo aprobada no se ve en compras para asociar. Tiene que estar recepcionada, lista para contabilizar. | La hija de insumos sin guia no aparece. La OC de servicio aprobada y sin recepcion si aparece y se puede asociar. |

Criterio de pase: solo la columna de la sala. Ocultar madres e hijas sin guia no acredita este borde.

## P-52. Una recepcion parcial no reabre la cadena de la madre

- CU: CU-20. Maria Jesus, 14/10 [32:03] y [43:59]. Si se negociaron 100 y van 50 entregadas, la madre sigue abierta y no vuelve a la cadena. La hija no se aprueba de nuevo por nacer.
- Que se hace: lectura del servicio de recepcion de guia y de `POST /insumos/ordenes/:id/cierre`. No se recepciona el parcial en la empresa y no se pide el cierre.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Parcial | La recepcion parcial no es la edicion de cierre. La madre sigue abierta. | Una recepcion parcial no devuelve la madre a la cadena. La hija nace `APROBADO`. |
| Cadena | No vuelve a aprobacion por esas 50. | El cierre por lo ya recepcionado es otra accion. Si alguien lo pide y queda saldo, ahi si vuelve a `PENDIENTE_APROBACION`. Esta prueba no lo pide. |

Criterio de pase: solo la columna de la sala. Un cierre de saldo que manda la madre a la bandeja es la columna de la edicion (P-20), no un pase de este limite.

## P-53. El segundo cambio de la madre lo pide contabilidad

- CU: CU-20. Maria Jesus, 14/10 [30:44] a [31:20] y [43:32]. La madre se cambia una sola vez. Si hace falta otro cambio, se pide a contabilidad.
- Que se hace: lectura de `PUT /ordenes-compra/:id` cuando la madre ya tuvo un cierre (`cerradaAt`) o ya volvio a `APROBADO`. No se ejecuta el segundo `PUT` contra la API.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Segunda vez | No queda en la misma via. Lo pide contabilidad. | Si `cerradaAt` ya tiene fecha, el cierre por lo recepcionado se rechaza. Un cambio de total, hecho por el creador o por un administrador de la OC, rearma la cadena y borra la marca de cierre. |
| Quien | No es el mismo usuario repitiendo la edicion de la madre. | No hay un segundo cambio reservado a contabilidad. Mientras la madre vuelva a `APROBADO` y no tenga factura que la cierre, se puede volver a editar. |

Criterio de pase: solo la columna de la sala. Rechazar el segundo cierre por saldo no acredita el caso si un `PUT` del total sigue abierto para el creador.

## P-54. Ningun eslabon de la OC se salta por monto

- CU: CU-23. Maria Jesus, 14/10 [33:23] a [33:48]. Acepta que no exista un salto y que el primer eslabon parta desde cero.
- Que se hace: Jest `approval-engine.spec.ts`. Se leen los casos en que el monto queda bajo el piso del eslabon siguiente ("Ana $1.5M pide solo el primer escalon", "Pedro en el piso de B pide solo a B"). Esos verdes son la columna de hoy. No se envia una OC real.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cadena | El monto sirve para saber quien firma. Nadie se salta la cadena. | Del segundo eslabon en adelante, un tope que el monto no alcanza se salta. |
| Primero | El primero cubre desde cero. Un monto de 5 pesos no queda aprobado solo. | El primer eslabon entra aunque el monto sea chico. Eso, solo, no cubre este limite. |

Criterio de pase: solo la columna de la sala. Un spec en verde que omite al segundo aprobador es fallo de este limite.

## P-55. Exportacion no devuelve; ALM si. No se mueve stock

- CU: CU-24. Sala del 01/10 [59:35] a [01:00:18]. Carlos propone configurarlo por empresa y la sala confirma el corte.
- Que se hace: observacion de lectura. En ALMAHUE EXPORT SPA se lee el flag apagado y el Jest de rechazo, sin postear el movimiento. Si otra empresa del local ya tiene el flag prendido, se lee ese checkbox y no se confirma la salida. Si no hay esa empresa, no se prende el flag y no se crea la empresa.
- Mutacion: no se mueve stock y no se cambia el flag.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Exportacion | No usa el reintegro de bodega. Compran lo justo que venden. | Con el flag apagado, `SALIDA_PROVEEDOR`, `DEVOLUCION` y `DEVOLUCION_NC` se rechazan. |
| ALM | Puede devolver material al proveedor. | El codigo no nombra a ALM. La empresa que tenga el flag prendido puede confirmar la salida y bajar stock. Esta prueba no la confirma. |

Criterio de pase: solo la columna de la sala. El rechazo en exportacion no acredita el lado de ALM, y prender el flag para probarlo no es esta prueba.

## P-56. Guardar el ingreso diario no lo aprueba

- CU: CU-31. Maria Jesus, 06/10 [18:17], corregido en [24:05]. El 14/10 la aprobacion que ven es la de la proforma.
- Que se hace: Jest de lectura del alta de ingreso: queda `PENDIENTE` y no entra a `/contratistas/aprobaciones`. Se anota que `POST /ingresos-labor-diario/:id/aprobar` sigue existiendo. No se guarda un ingreso en la empresa y no se llama ese aprobar.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Guardar | El ingreso no queda aprobado uno a uno. La que entra a la jefatura es la proforma. | El ingreso nuevo queda `PENDIENTE` y no entra a la bandeja. |
| Atajo | La frase de aprobar al guardar no manda. | El endpoint de aprobar el ingreso sigue publicado. Un ingreso nuevo no queda en ese estado por el alta. |

Criterio de pase: solo la columna de la sala. Dejar el ingreso en `PENDIENTE` al guardar es la columna que la sala pide para este borde. El endpoint publicado no acredita una aprobacion del ingreso.

## P-57. Una parte de la proforma no se factura

- CU: CU-32. Maria Jesus, 06/10 [25:07] a [25:48]. El ejemplo que descarta: factura por una parte. Si el precio o la jornada no calzan, se modifica la proforma y el ingreso de origen. No queda un saldo a medias.
- Que se hace: lectura de `POST /proformas-contratista/:id/factura` con un neto de factura menor que la proforma (el ejemplo de la sala: 5.600 contra 9.600). No se asocia en la empresa. La otra entrada de la sala, varias proformas enteras en una factura, queda en P-32.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Fraccion | No se factura una parte de la proforma. No queda saldo facturado a medias. | No deja un saldo facturado de una parte de la misma proforma. La proforma pasa entera a `FACTURADA` o no entra. |
| Diferencia | Se corrige el ingreso de origen y esa proforma vuelve a su aprobacion si ya estaba aprobada (CU-34). | Si el precio no calza, el camino es el reclamo, que vuelve a editar el ingreso de origen cuando la proforma enviada esta en reclamo. |

Criterio de pase: solo la columna de la sala. Rechazar la fraccion y dejar la proforma a medias, o asociarla parcial, es fallo. Exigir que este enviada, y no solo aprobada, no acredita el caso.

## P-58. Proforma ya asociada a una factura: no se edita

- CU: CU-34. Maria Jesus, 14/10 [01:00:17] a [01:01:14]. La factura es el ultimo control. La frase "orden de credito" no entra.
- Que se hace: lectura de `PUT /proformas-contratista/:id`, `POST /proformas-contratista/:id/reversar` y `POST /proformas-contratista/:id/reclamo` sobre estado facturado. No se llama contra la API. No se busca una nota de credito.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cierre | Ya asociada a una factura recibida, no se edita. | Una facturada no entra a la reversa ni al reclamo. `PUT` solo acepta borrador. |
| Nota | No hay pedido de nota de credito en esta frase. | `reemitir` crea otra proforma en borrador y deja la anterior rechazada. No hay nota de credito en este flujo. Ese `reemitir` no acredita el caso. |

Criterio de pase: solo la columna de la sala. Poder reversar una definitiva sin factura es P-34, no este limite.

## P-59. En compras se listan las proformas aprobadas, no solo las notificadas

- CU: CU-36. Maria Jesus, 13/10 [08:49]. La frase de Carlos y Sergio del 06/10 [31:56], sin ella, no manda.
- Que se hace: lectura de `GET /contratistas/registros-compra-asociables` y del libro `/compras/registro`. No se asocia. Se compara una proforma `DEFINITIVA` (aprobada, no enviada) con una `ENVIADA_CONTRATISTA`, en el codigo, sin cambiarlas.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Lista | Para asociar aparecen las proformas aprobadas, contra las facturas que lleguen. | El codigo pide proformas enviadas al contratista, no solo aprobadas. Una `DEFINITIVA` todavia no enviada no entra. |
| Lugar | La eleccion es en compras. La cuenta no se edita ahi. | El vinculo se hace desde la proforma. El libro no tiene selector de proforma. |

Criterio de pase: solo la columna de la sala. Listar las enviadas no acredita el caso.

## P-60. El precio cero en el trato no queda habilitado

- CU: CU-40. Una voz de la sala del 14/10 [59:15] pregunta por el cero. Maria Jesus no lo deja: se carga un estimativo y despues se edita.
- Que se hace: Jest de lectura del alta de ingreso con precio cero, con mock. No se guarda un ingreso en cero en la empresa. El mensaje de la API, si dice que cero sirve para una asistencia pendiente de valorizar, es la columna de hoy.
- Mutacion: no se muta.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Cero | El precio cero no queda habilitado. | Si no hay tarifa, se puede guardar un precio, incluido cero. |
| Estimativo | El valor que entra es un estimativo, mayor que cero, y despues se corrige. | Un precio mayor que cero sin tarifa pide `contratistas:rate-override` y un motivo. |

Criterio de pase: solo la columna de la sala. Un alta en cero, aunque el mensaje hable de valorizar despues, no pasa.

## P-61. Un dia trabajado sin proforma no entra al asiento del mes

- CU: CU-41. Maria Jesus, 14/10 [01:01:15] a [01:02:53]. Si no, el dia queda fuera y un mes queda con 29 y otro con 31.
- Que se hace: observacion de lectura del armado del traspaso. No se hace `POST /contratistas/traspaso-cierre` y no se reabre un periodo.
- Mutacion: no se cierra el mes.

| | Resultado esperado (sala) | Resultado que el codigo hace hoy |
|---|---|---|
| Dia | Un ingreso con labor y sin proforma no entra al asiento. El cierre trabaja contra proforma. | Un ingreso sin proforma no entra al asiento. El cierre no lo arrastra por existir. |
| Pendiente | Una proforma que sigue pendiente de aprobacion tampoco entra al gasto. Si el mes se cerro con esa pendiente, el mes se puede volver a abrir. La reapertura no se ejecuta aqui. | El traspaso deja fuera borrador, pendiente de aprobacion y rechazada. Reabrir anula el asiento del traspaso solo si el periodo contable no esta cerrado. |

Criterio de pase: solo la columna de la sala. Un asiento que sume ingresos sueltos es fallo, aunque el menu se llame como en P-38.
