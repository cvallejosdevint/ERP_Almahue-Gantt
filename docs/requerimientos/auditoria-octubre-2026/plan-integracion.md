# Plan de integracion - auditoria octubre 2026

Describe por donde entra hoy cada caso de `casos-de-uso.md` y que deja el codigo de octubre. No redisena pantallas y no propone un parche. No repite `docs/requerimientos/presentacion-2026-10-14/plan-integracion.md`: la guia de insumos, la madre y la hija, el reclamo de la proforma y el asiento al contabilizar ya estan en el codigo.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`.

La transcripcion manda. La minuta es indice. Carlos y Sergio no crean un caso. Reu1 a Reu3 son el as-is de Agrosoft. Reu5 no cuenta.

No se implemento codigo, no hubo commit, no se emitio DTE, no se pago, no se cerro el mes y no se corrio `prisma migrate deploy`.

## Como leer cada caso

- Entra hoy: ruta de pantalla y endpoint. El prefijo de la API es `/api/v1`.
- Deja hoy: lo que el codigo persiste o rechaza.
- Pide la sala: el cierre del caso, sin agregar un silencio.
- Depende de: otros CU. Si no depende de ninguno, se dice.

---

## Casos

### CU-01. Condiciones de pago del neto y del IVA, editables

- Entra hoy: Parametrizacion > Proveedores, `/catalogos/proveedores`. Alta y edicion en `POST /proveedores` y `PUT /proveedores/:id` (`catalogos`). La OC toma el neto en Compras > Ordenes de compra, `/compras/ordenes/nueva`, `POST /ordenes-compra`. El vencimiento del IVA se calcula al leer la nomina, `GET /documentos-aging` (`tesoreria`).
- Deja hoy: la ficha guarda dos enteros, `condicionPagoDias` (neto) y `condicionIvaDia` (IVA, default 10). Acepta un entero manual, por ejemplo 45. La OC solo tiene `condicionPagoDias`. Al elegir proveedor, el wizard copia el neto de la ficha. El combo muestra 30, 60, 90 y el valor que ya trae el formulario, asi que un 45 de la ficha se puede elegir, pero en la OC no se tipea un dia nuevo. La API de la OC conserva el entero que reciba. La factura del libro no tiene plazo propio. En aging, el vencimiento del IVA sale de `condicionIvaDia` del proveedor, no de un campo editable del documento.
- Pide la sala: dos plazos independientes, dias manuales, valor sugerido y editable en la OC y en la factura.
- Depende de: ninguno. La nomina que muestra el atraso es CU-25.

### CU-02. Fichas de proveedor y cliente separadas, que conversan por RUT

- Entra hoy: proveedor en `/catalogos/proveedores` (`POST /proveedores`). Cliente en Ventas > Clientes, `/comercial/clientes` (`POST /clientes`). Al tipear el RUT, las dos pantallas llaman `GET /contraparte-por-rut`.
- Deja hoy: son dos maestros, `Proveedor` y `Cliente`, con RUT unico dentro de cada uno. El mismo RUT puede existir en los dos. Si el RUT ya esta en la otra ficha, y el alta esta vacia, se copian razon social, giro, mail, telefono y direccion. No se fusionan en un solo registro. El alta de proveedor pide `catalogos:write` o `compras:write`. El alta de cliente pide `comercial:write`. No hay un corte de jefatura distinto de ese permiso.
- Pide la sala: dos fichas, copia al encontrar el RUT en la otra, un mismo RUT en las dos, y el alta en una jefatura.
- Depende de: ninguno. La consulta unificada del RUT es CU-03.

### CU-03. Consulta por RUT con movimientos de proveedor y de cliente

- Entra hoy: Tesoreria > Estado de cuenta, `/tesoreria/cuentas-corrientes`. El detalle llama `GET /cuentas-corrientes/por-rut`. El listado agrupa por RUT en `GET /cuentas-corrientes`.
- Deja hoy: si el RUT existe como cliente y como proveedor, el estado de cuenta junta los movimientos de cuenta corriente de las dos fichas y separa saldo de cliente y saldo de proveedor. No abre un reporte que liste OC, facturas y ventas que nunca hayan pasado por la cuenta corriente. `GET /lookup-rut` solo dice si el RUT es sociedad, cliente o proveedor. No trae movimientos.
- Pide la sala: consultar un RUT y ver todos sus movimientos, sea proveedor o cliente, sin partir el historial.
- Depende de: CU-02.

### CU-04. Anular un elemento de costo sin borrar el historial

- Entra hoy: Parametrizacion > Elementos de costo, `/catalogos/elementos-costo`. `GET /elementos-costo`, `POST /elementos-costo`, `PUT /elementos-costo/:id`.
- Deja hoy: vigencia `VIGENTE` o `ANULADO`. El alta nace vigente. El listado sigue mostrando el anulado. El comprobante, el plan de cuentas y la cartola no ofrecen el anulado para imputar. No hay un tercer estado.
- Pide la sala: vigente o anulado. Anulado no se imputa y no desaparece.
- Depende de: ninguno.

### CU-05. Historico del Banco Central, sin pisar documentos

- Entra hoy: Parametrizacion > Indicadores BC, `/catalogos/indicadores-bc`. `POST /parametrizacion/indicadores-bc/sincronizar` con rango de fechas, y la importacion CSV o Excel. Tambien `POST /sync-indicadores-bc`.
- Deja hoy: escribe filas de `IndicadorBc` (usd, eur, cny, y un mapa de otras monedas). No recorre OC, facturas ni asientos para cambiarles el tipo de cambio guardado. La pantalla del comprobante, al armar las columnas dolar y yuan, vuelve a leer la tasa de esa fecha si la linea no trae el monto en esa moneda. Llenar un dia que antes estaba vacio puede cambiar lo que se ve en esas columnas. El asiento guardado en pesos no se reescribe.
- Pide la sala: historico por moneda ya registrada y por rango, tomado del Banco Central, sin reescribir el tipo de cambio de los documentos ya grabados.
- Depende de: ninguno. Las columnas del comprobante son CU-06.

### CU-06. Comprobante en peso, dolar y yuan

- Entra hoy: el asiento de venta nace al contabilizar en Ventas > Libro de ventas, `/comercial/libro`, `POST /documentos/:id/contabilizar`. El comprobante se ve en Contabilidad > Comprobantes / asientos, `/contabilidad/asientos`.
- Deja hoy: la pantalla y la impresion del comprobante muestran debe y haber en pesos, en dolar y en yuan, con la tasa del dia. Si al contabilizar no viene tipo de cambio, el servicio toma el dolar de `IndicadorBc` de la fecha del documento. El libro deja editar ese tipo de cambio antes de contabilizar. La linea guarda pesos y, si hay moneda extranjera, un monto en esa moneda (dolar, o la moneda del documento). El yuan de un documento en pesos se calcula al ver el comprobante, no queda como tercera cifra guardada en el asiento.
- Pide la sala: tres columnas, peso, dolar y yuan, en el comprobante. Tipo de cambio del dia, propuesto desde el Banco Central y editable al ingresar el documento.
- Depende de: CU-05.

### CU-07. Auxiliar = RUT sin digito verificador

- Entra hoy: el mismo contabilizar de CU-06. El auxiliar se ve en el comprobante (`/contabilidad/asientos`) y en su impresion.
- Deja hoy: cada linea del asiento de venta guarda `auxiliar` con el RUT del receptor sin puntos y sin digito verificador. El libro diario y el mayor no traen esa columna: muestran glosa, cuenta, debe y haber.
- Pide la sala: auxiliar igual al RUT sin DV, en el comprobante y en el mayor.
- Depende de: CU-06.

### CU-08. Glosa = comentario, repetida en cada linea

- Entra hoy: el comentario del documento esta en `observaciones`. Al contabilizar, `POST /documentos/:id/contabilizar`. Se lee en el comprobante y en Libro diario y Libro mayor, `/contabilidad/libro-diario` y `/contabilidad/mayor`.
- Deja hoy: si no se manda otra glosa, la cabecera queda `FACTURA mes/anio`, mas el tipo de cambio si hay, mas el comentario. Esa frase completa se copia en la linea de cliente, en la de ingreso y en la de IVA. El mayor muestra la glosa de la linea, y si no hay, la de la cabecera. El nombre del dueno no entra en esa frase. La glosa por defecto si repite tipo y tipo de cambio, que la sala queria dejar fuera porque ya van en otras columnas.
- Pide la sala: una glosa, la del comentario ingresado, copiada en todas las lineas. Sin el nombre del dueno y sin rellenar la glosa con datos que ya van al lado.
- Depende de: CU-06.

### CU-09. En la venta, la cuenta es IVA debito

- Entra hoy: el mismo contabilizar de CU-06. La cuenta la resuelve el plan por codigo `2-1-09-02-001`.
- Deja hoy: si hay IVA, la linea usa esa cuenta. Si el plan no la tiene, contabilizar se detiene. En una nota de credito la cuenta es IVA credito. Si un asiento viejo dejo la linea de IVA en la cuenta caja y la glosa dice IVA debito, el comprobante la muestra como IVA debito y no reescribe el asiento.
- Pide la sala: en el comprobante de venta, la linea de IVA es IVA debito, no caja.
- Depende de: CU-06.

### CU-10. Avisar a quien debe crear la OC que falta

- Entra hoy: Compras > Libro de compras, `/compras/registro`. Accion "Notificar usuario / correo". `GET /registros-compra/destinatarios-notificacion`, `POST /registros-compra/:id/notificar`, `GET /registros-compra/:id/trazabilidad-notificaciones`.
- Deja hoy: se elige un usuario de la empresa. Queda un aviso en la bandeja y una fila en `RegistroCompraNotificacionEvento`. El correo es opcional: si SMTP responde, se envia; si no, el aviso interno igual queda. El modal se ofrece tambien cuando el documento no tiene OC.
- Pide la sala: desde el documento sin OC, sin proveedor o con diferencia, avisar a un usuario del sistema y dejar el aviso en la trazabilidad. El texto del correo y el SMTP no son pedido de esta sala.
- Depende de: ninguno. El correo de la OC misma es CU-42. El de la proforma es CU-33.

### CU-11. OC madre de insumos, solo informativa

- Entra hoy: la madre se crea en Compras > Ordenes de compra eligiendo tipo insumos, `POST /ordenes-compra` con `tipo=INSUMOS`. Se mira en Insumos > Ordenes de insumos, `/insumos/ordenes`, `GET /insumos/ordenes`.
- Deja hoy: la madre no arma asiento al crearse. `GET /ordenes-compra` no la lista. `PATCH /registros-compra/:id/vincular-oc` la rechaza. Contabilizar un registro atado a la madre se detiene con el texto de que la madre no se contabiliza. Vive en el listado de insumos, con rol `MADRE`.
- Pide la sala: la madre no genera asiento y no es documento asociable en el libro de compras. Vive en insumos.
- Depende de: CU-13 para que existan hijas. CU-21 para quien la crea.

### CU-12. OC de servicio, uno a uno y con factura directa

- Entra hoy: la OC de servicio es el default de `/compras/ordenes/nueva`, `POST /ordenes-compra` con `tipo=SERVICIO`. La recepcion esta en Compras > Recepciones, `/compras/recepciones`, `POST /recepciones-oc`. La factura entra por el libro, `PATCH /registros-compra/:id/vincular-oc`.
- Deja hoy: una OC de servicio no acepta madre ni hija. La recepcion de insumos por esta pantalla esta cerrada. Confirmar la recepcion exige el neto completo de la orden: no deja un parcial. Si la cuenta de la linea tiene par de facturas por recibir, la recepcion confirmada deja el asiento de gasto o existencia contra esa cuenta. Asociar la factura admite una sola orden de servicio. Varias hijas de insumos no se mezclan con una de servicio.
- Pide la sala: la OC de servicio no se parte y no espera guia. Una recepcion, una factura.
- Depende de: CU-23 para la aprobacion. La guia de insumos es CU-13 y no aplica a este tipo.

### CU-13. La guia en bodega actualiza stock y nace la OC hija

- Entra hoy: Insumos > Guias de insumos recibidas, `/insumos/guias-recibidas`. Dos entradas. La guia digitada: `POST /guias-insumo-recibidas`. La guia llegada de GoSocket (DTE 52): `POST /guias-despacho-recibidas/sincronizar` y despues `POST /guias-despacho-recibidas/:id/asociar`. El libro de compras, al sincronizar, no crea un registro si el DTE es 52: la deja en esa misma bandeja.
- Deja hoy: sin madre aprobada, del mismo proveedor y con el articulo en sus lineas, la guia no entra. Si la cantidad o el neto pasan el saldo, se rechaza. Si entra, mueve stock con `ENTRADA_PROVEEDOR` y crea una hija `APROBADO`, numero de la madre mas un punto y un correlativo, sin cadena nueva. Varias guias dejan varias hijas. La hija no nace al asociar la factura. La sala no pidio traer la guia desde GoSocket: el codigo igual la trae y la deja pendiente hasta asociarla a la madre. Tambien se puede digitar la guia sin ese inbox.
- Pide la sala: sin madre no hay guia asociable. Cada guia recepcionada en insumos actualiza la bodega y crea una hija. Varias guias del mes pueden ir a una factura, y eso es CU-15.
- Depende de: CU-11 y CU-21. El tope es CU-19. La empresa tiene que tener prendido "Recibe insumos con guia" en Admin > Empresas.

### CU-14. Libro de guias solo en insumos

- Entra hoy: `/insumos/guias-recibidas`, `GET /guias-insumo-recibidas` y `GET /guias-despacho-recibidas`. El libro de compras es `/compras/registro`.
- Deja hoy: las guias recibidas se listan en insumos. El sincronizado del libro de compras salta el DTE 52 y no lo deja como factura. Ventas > Libro de guias, `/comercial/guias-despacho`, es la guia emitida de ventas, otro documento.
- Pide la sala: la guia se ve y se opera en insumos. El libro de compras no lista guias de despacho.
- Depende de: CU-13.

### CU-15. La factura de insumos se asocia a las OC hijas

- Entra hoy: Compras > Libro de compras, `/compras/registro`. `PATCH /registros-compra/:id/vincular-oc` acepta una o varias OC. El asiento nace al pasar el registro a contabilizado, `PUT /registros-compra/:id`.
- Deja hoy: rechaza la madre, rechaza una hija de insumos que no tenga guia, y exige el mismo proveedor. Varias hijas quedan en `RegistroCompraOrden`. Compara el monto de la factura con la suma de las hijas y, si la diferencia pasa un peso, deja el registro en alerta. La seleccion es por orden, no por un calce solo de monto. Como la guia no dejo asiento de recepcion, al contabilizar esa factura el asiento usa la cuenta de gasto del registro contra el proveedor. No arrastra un haber de facturas por recibir de una recepcion que no existe.
- Pide la sala: desde la factura se eligen N hijas del mismo proveedor, ya nacidas de una guia. No se elige la guia ni la madre. No basta un match solo por monto.
- Depende de: CU-13 y CU-16.

### CU-16. Compras solo lista hijas ya recepcionadas

- Entra hoy: el listado de ordenes de compras es `GET /ordenes-compra`, pantalla `/compras/ordenes`. La asociacion usa el mismo conjunto en el modal del libro.
- Deja hoy: ese listado trae las OC de servicio y las hijas de insumos que ya tienen guia. No trae madres ni hijas sin guia. Al asociar, la hija tiene que estar aprobada o posterior, y la de insumos tiene que tener guia. Una OC de servicio aprobada y todavia no recepcionada si aparece en compras y se puede asociar: el filtro de "ya recepcionada" no la cubre.
- Pide la sala: el listado de asociacion no muestra madres, ni OC sin recepcion, ni OC solo aprobadas.
- Depende de: CU-11, CU-13 y CU-15.

### CU-17. Quien ve la madre y quien ve la hija

- Entra hoy: insumos en `/insumos/ordenes` (`insumos:read`). Compras en `/compras/ordenes` (`compras:read`). Las guias, en `/insumos/guias-recibidas`.
- Deja hoy: insumos lista madre e hija. Compras lista servicio e hijas con guia, y no la madre. Un usuario con solo `insumos:read` entra a las ordenes de ese mundo y no al libro de compras. Las guias recibidas no estan en el libro de compras.
- Pide la sala: insumos muestra madre e hija. Compras muestra hijas listas para contabilizar. Quien solo tiene insumos ve las OC de ese mundo. La madre no se mezcla en el libro.
- Depende de: CU-11 y CU-16.

### CU-18. El saldo de la madre se ve en insumos

- Entra hoy: `/insumos/ordenes`, `GET /insumos/ordenes`. El campo es `pendiente`.
- Deja hoy: el pendiente de la madre es su neto menos la suma de las hijas no anuladas. La hija repite el pendiente de su madre. El modal de asociacion de la factura no pide ni muestra ese saldo: calza ordenes contra el monto del documento.
- Pide la sala: el saldo de la madre se ve en insumos. El calce de la factura no exige ese saldo en pantalla.
- Depende de: CU-13 y CU-17.

### CU-19. Si la guia no cabe, se pide modificar la madre

- Entra hoy: al asociar la guia, `POST /guias-insumo-recibidas` o `POST /guias-despacho-recibidas/:id/asociar`. El tope esta en `assertTopeRecepcion`.
- Deja hoy: si la cantidad de una linea o el neto superan lo ya recibido mas lo nuevo, la guia no entra a bodega y no nace hija. El mensaje dice que la guia no cabe en el saldo de la madre. No modifica la madre sola. La edicion de esa madre es CU-20.
- Pide la sala: la recepcion no puede pasar el saldo. El desborde se resuelve pidiendo la edicion de la madre, antes de asociar la factura.
- Depende de: CU-13 y CU-20.

### CU-20. La madre se edita una vez, para arriba o para abajo, con aprobacion

- Entra hoy: bajar al recibido, en Insumos > Ordenes de insumos, `POST /insumos/ordenes/:id/cierre`. Subir o bajar el total en general, `PUT /ordenes-compra/:id` mientras la madre sigue `APROBADO`.
- Deja hoy: una recepcion parcial no devuelve la madre a la cadena. La hija nace aprobada. El cierre por lo ya recepcionado lo pide quien creo la madre, una vez: si `cerradaAt` ya tiene fecha, se rechaza. Si queda saldo, baja el neto a lo recibido y la madre vuelve a `PENDIENTE_APROBACION`. Si ya no queda saldo, solo marca el cierre y no rearma la cadena. Un cambio de total, para arriba o para abajo, hecho por el creador o por un administrador de la OC, tambien rearma la cadena y borra la marca de cierre. No hay un segundo cambio reservado a contabilidad: mientras la madre vuelva a `APROBADO` y no tenga factura que la cierre, se puede volver a editar.
- Pide la sala: una sola edicion de cierre, para arriba o para abajo, con cadena. Sin cierre automatico al recibir una parte. Un segundo cambio lo pide contabilidad. La hija no se aprueba de nuevo por nacer.
- Depende de: CU-11, CU-19 y CU-23.

### CU-21. La madre la crea el jefe; la hija, el administrativo

- Entra hoy: la madre, `POST /ordenes-compra` con tipo insumos. La hija, al recepcionar la guia (CU-13), con `insumos:write`.
- Deja hoy: la madre solo la crea el aprobador inicial de un grupo de OC de Compras activo. Si el usuario no es ese jefe, la API responde que la madre solo la crea el jefe del grupo. La hija la graba el usuario que recepciona, queda `APROBADO` y no arma otra cadena. No hay un permiso distinto que se llame "administrativo de abastecimiento": entra quien tenga escritura de insumos.
- Pide la sala: alta de la madre restringida al jefe, con una aprobacion. Alta de la hija en la recepcion, por el administrativo de insumos, sin recorrer otra vez la cadena.
- Depende de: CU-13, CU-20 y CU-23.

### CU-22. Cadenas distintas para insumos y para servicios

- Entra hoy: Admin > Reglas de aprobacion, `/admin/aprobaciones`. La OC, de los dos tipos, resuelve la cadena con modulo `Compras` y grupo tipo `OC`. La proforma usa modulo `Contratistas` y grupo tipo `PROFORMA`.
- Deja hoy: insumos y servicio comparten la misma pieza de Compras. `preview-cadena` no recibe el tipo de OC. Una proforma no puede tomar un grupo cuyo tipo no sea `PROFORMA`. Un mismo usuario puede estar en un grupo de OC y en otro de proforma. No hay una cadena de insumos distinta de la de servicios.
- Pide la sala: la cadena de una OC de insumos no es la misma pieza que la de una OC de servicio. No pidio que un grupo no pueda existir en los dos flujos.
- Depende de: CU-12 y CU-21. La aprobacion de la proforma es CU-31.

### CU-23. Toda OC pasa por aprobacion, desde monto cero

- Entra hoy: al enviar la OC a aprobacion, `POST /ordenes-compra` o `PUT /ordenes-compra/:id` con estado de envio. La cadena la arma `approval-engine` para modulo Compras. La bandeja es `/compras/aprobaciones`.
- Deja hoy: el primer eslabon entra aunque el monto sea chico. Del segundo en adelante, un tope que el monto no alcanza se salta. Si la escala devolveria la OC aprobada sola por monto, la API rechaza el envio y no la deja aprobada. Un borrador sigue sin cadena hasta que se envia. Un neto cero o negativo no entra al calculo de la escala: el envio queda marcado como pendiente y puede no crear fila de aprobador.
- Pide la sala: ninguna OC queda aprobada solo por estar bajo un monto. El primer aprobador cubre desde cero. Puede haber escalas por monto para saber quien firma, sin saltarse la cadena.
- Depende de: ninguno. La edicion que vuelve a la cadena es CU-20.

### CU-24. Devolucion a proveedor solo en ALM

- Entra hoy: Insumos > Movimientos, `/insumos/movimientos`, `POST /movimientos-bodega`. El corte por empresa esta en Admin > Empresas, checkbox "Permite devolucion a proveedor".
- Deja hoy: `SALIDA_PROVEEDOR`, `DEVOLUCION` y `DEVOLUCION_NC` se rechazan si la empresa no tiene el flag. El default es apagado. No hay un nombre de empresa escrito en el codigo: ALM lo prende y exportacion lo deja apagado. La salida a proveedor, si se confirma, baja el stock de la bodega de origen.
- Pide la sala: ALM puede devolver material al proveedor. Almahue exportacion no usa ese reintegro. La diferencia es por empresa.
- Depende de: ninguno.

### CU-25. Nomina semanal, historico y banderas

- Entra hoy: Tesoreria > Nomina semanal, `/tesoreria/nominas`. Documentos en `GET /documentos-aging`. Banderas en `GET /nomina-plazos` y `PUT /nomina-plazos`.
- Deja hoy: la vista del periodo parte el mes en semanas y cuenta pendientes. La vista historico filtra por rango de semanas. El filtro cambia entre pendientes y todos. Las banderas viven en la empresa (`nominaEtiquetas`): dias, nombre y color, hasta ocho. El default de codigo es atrasada desde 1 dia, critico a los 30 y otra a los 90. Esos dias se pueden cambiar. Un proveedor puede traer su propio umbral critico.
- Pide la sala: vista actual por semanas e historico por fechas, conteos, banderas con umbral, nombre y color, y filtro de pendientes. Los dias 7, 30 y 90 son el ejemplo de partida, no un candado.
- Depende de: ninguno. El plazo del IVA que usa el aging sale de CU-01.

### CU-26. Ficha de contratista con codigo correlativo

- Entra hoy: Contratistas > Listado, `/contratistas`. `POST /contratistas` y `PUT /contratistas/:id`.
- Deja hoy: codigo propio `CTR-` mas un correlativo de cinco digitos, distinto del RUT. Guarda RUT, razon social, direccion, y `creadoPorId` con el nombre de quien la crea. Tambien exige ciudad y comuna. Si el RUT ya es proveedor, deja `proveedorId`. La etiqueta "tambien es proveedor" la muestra el alta cuando el RUT coincide. La sala no la pidio como dato de la ficha. El codigo de proveedor sigue siendo el RUT, en el maestro de CU-02.
- Pide la sala: maestro propio, codigo numerico correlativo, RUT, nombre, direccion y usuario de alta.
- Depende de: ninguno.

### CU-27. El flujo de contratista no tiene contrato

- Entra hoy: el ingreso diario, `/contratistas/ingreso-diario`, `POST /ingresos-labor-diario`. No hay pantalla ni modelo de contrato con folio.
- Deja hoy: el ingreso no pide un contrato vigente ni un folio de contrato. Si pide un tipo contable operativo (`TipoContratoContratista`): cuentas de debe, haber y administracion. Si la empresa no tiene uno activo, el ingreso no se guarda. Ese tipo no es el contrato de Agrosoft. El cierre del mes lo usa para saber que la proforma tiene tipo, no para exigir un documento de contrato.
- Pide la sala: el ingreso diario no exige un contrato vigente ni un folio de contrato.
- Depende de: CU-26 y CU-28.

### CU-28. Ingreso diario de la labor

- Entra hoy: `/contratistas/ingreso-diario`, `POST /ingresos-labor-diario` y `PUT /ingresos-labor-diario/:id`. El masivo redirige a la misma ruta.
- Deja hoy: guarda fecha, contratista, centro de costo (la pantalla lo llama cuartel), labor, actividad, jornada o trato, unidad, cantidad, precio y total. Predio, temporada, sector y faena son opcionales. No hay trabajador. El registro es por empresa, asi que sirve para ALM y para agricola. Al guardar queda `PENDIENTE`. No queda aprobado uno a uno.
- Pide la sala: esos campos, predio opcional, sin trabajador obligatorio, jornal o trato, y el mismo funcionamiento para las dos empresas. Sector, cuartel y faena son datos del ingreso. El unico opcional que la sala nombro asi es el predio.
- Depende de: CU-26, CU-27 y CU-29. El precio estimativo es CU-40.

### CU-29. Mantenedores de cuartel y faena

- Entra hoy: Parametrizacion > Contratista, `/catalogos/contratista`. Labores y actividades: `GET/POST/PUT /labores` y `/actividades`, vinculo `POST /labor-actividad`. Sector y faena: `/sectores-contratista` y `/faenas-contratista`. El cuartel del ingreso es el centro de costo, `/catalogos/centros-costo`.
- Deja hoy: labor, actividad, sector y faena se eligen de mantenedor. No hay un mantenedor que se llame cuartel: el ingreso usa el centro de costo y la etiqueta dice "Cuartel / centro de costo". Al elegir la labor, si esa labor tiene una sola actividad vinculada, la actividad se llena sola. Si tiene varias, hay que elegirla. Faena sigue atada a un sector.
- Pide la sala: cuartel y faena se eligen de un mantenedor. Hay faenas de agricola y faenas puntuales de ALM. Al elegir la labor, la actividad queda determinada.
- Depende de: CU-28.

### CU-30. Armar la proforma eligiendo ingresos

- Entra hoy: Contratistas > Proformas y facturas, `/contratistas/proformas`. `POST /proformas-contratista` y `POST /ingresos-labor-diario/asociar`.
- Deja hoy: se eligen varios ingresos del mismo contratista, del mismo periodo y del mismo tipo contable. El monto de la proforma es la suma. El ingreso pasa a `ASOCIADO` y no vuelve a ofrecerse. Una proforma no crea una OC: el alta de factura exige un registro que ya este en el libro de compras. En un mes caben varias proformas.
- Pide la sala: seleccion multiple, total de lo elegido, bloqueo del ingreso ya usado, y que la proforma no se transforme en OC.
- Depende de: CU-28. La aprobacion es CU-31. La factura de varias proformas es CU-32.

### CU-31. La que se aprueba es la proforma

- Entra hoy: en la proforma en borrador, `POST /proformas-contratista/:id/definitiva`. La firma esta en Contratistas > Aprobaciones, `/contratistas/aprobaciones`, `POST /proformas-contratista/:id/aprobar`.
- Deja hoy: el ingreso nuevo queda `PENDIENTE` y no entra a la bandeja. La proforma en borrador arma la cadena del modulo Contratistas y pasa a `PENDIENTE_APROBACION`. El primer eslabon no se salta por monto. Si no hay grupo de proformas, no se puede enviar. Sigue existiendo `POST /ingresos-labor-diario/:id/aprobar`, pero un ingreso nuevo no queda en ese estado. Los montos de la escala son los que configure la empresa, no los 5.000 y 10.000 de la demo.
- Pide la sala: la aprobacion interna es de la proforma, por la jefatura (en la sala, el jefe de campo). El ingreso no queda aprobado al guardarse.
- Depende de: CU-30. La cadena no es la de la OC (CU-22).

### CU-32. La proforma no se factura parcial

- Entra hoy: desde la proforma, `POST /proformas-contratista/:id/factura`, con `registroCompraId` y una lista de proformas.
- Deja hoy: cada proforma del grupo pasa entera a `FACTURADA` y sus ingresos a `FACTURADO`. Varias proformas del mismo contratista, moneda y tipo caben en una factura, mientras la suma no pase el neto del registro. No deja un saldo facturado de una parte de la misma proforma. Para asociar, la proforma tiene que estar `ENVIADA_CONTRATISTA` y sin reclamo abierto. Una `DEFINITIVA` todavia no enviada no entra. Si el precio no calza, el camino del codigo es el reclamo (CU-34), que vuelve a editar el ingreso de origen.
- Pide la sala: la proforma se asocia completa. Varias caben en una factura. Una diferencia se corrige en el ingreso de origen. La asociacion exige la proforma aprobada.
- Depende de: CU-31 y CU-33. No copia el modelo de hija de CU-13.

### CU-33. Enviar la proforma al contratista

- Entra hoy: en la proforma aprobada, `POST /proformas-contratista/:id/enviar-contratista` y `POST /proformas-contratista/:id/enviar-email`. El reclamo es `POST /proformas-contratista/:id/reclamo`. Hay tambien un paquete `POST /contratistas/envios-operativos`.
- Deja hoy: notificar pasa la proforma de `DEFINITIVA` a `ENVIADA_CONTRATISTA` y guarda quien y cuando. El correo sale al mail de la ficha del contratista, con la plantilla `PROFORMAS`, y marca `emailContratistaAt`. El contratista no tiene usuario ni bandeja. El reclamo deja `reclamadaAt` y un motivo, sin cambiar el estado, y bloquea la factura hasta reenviar. Un envio operativo solo toma proformas ya notificadas que no esten en otro paquete. No es un cierre semanal del sistema.
- Pide la sala: desde una proforma aprobada, enviarla al mail del contacto, con constancia de cuales ya se enviaron. El contratista no aprueba dentro del ERP. Si reclama, se edita el origen.
- Depende de: CU-31. La edicion del reclamo es CU-34. El listado de compras no exige este envio: CU-36 pide las aprobadas.

### CU-34. Editar la proforma aprobada; no editarla si ya hay factura

- Entra hoy: editar datos, `PUT /proformas-contratista/:id`. Volver atras, `POST /proformas-contratista/:id/reversar`. Reclamo y correccion del ingreso, `POST /proformas-contratista/:id/reclamo` y `PUT /ingresos-labor-diario/:id`.
- Deja hoy: `PUT` solo acepta borrador. Una definitiva o enviada se puede devolver a borrador con la clave de reversa, y ahi hay que volver a pedir la cadena. Una facturada no entra a la reversa ni al reclamo. El ingreso asociado solo se edita si la proforma enviada esta en reclamo. Al guardar ese ingreso, el monto de la proforma se recalcula. `reemitir` crea otra proforma en borrador y deja la anterior rechazada. La frase sucia "orden de credito" no tiene nota de credito en este flujo.
- Pide la sala: aprobada y aun no facturada se corrige volviendo a aprobacion. Ya asociada a una factura, queda cerrada a la edicion.
- Depende de: CU-31, CU-32 y CU-33.

### CU-35. Ver proformas pendientes y aprobadas

- Entra hoy: `/contratistas/proformas`, `GET /proformas-contratista`.
- Deja hoy: cada fila trae su estado: borrador, pendiente de aprobacion, definitiva, enviada, facturada o rechazada. El filtro de pantalla tiene todos, pendientes y facturadas. "Pendientes" junta borrador, pendiente de aprobacion, definitiva y enviada. No hay un filtro que se llame "aprobadas" y deje fuera el borrador. La pendiente de aprobacion sigue en el listado. El traspaso contable no la lleva al gasto (CU-38).
- Pide la sala: en contratistas, ver pendientes y aprobadas, distinguibles. La asociacion del DTE no se hace en este listado como lugar de compras: eso es CU-36.
- Depende de: CU-31.

### CU-36. El DTE se asocia en compras; el costo se imputa en contratistas

- Entra hoy: la asociacion esta en la proforma, `POST /proformas-contratista/:id/factura`, eligiendo un registro del libro (`GET /contratistas/registros-compra-asociables`). La cuenta de la proforma se guarda en el alta, `cuentaGastoId`. El libro de compras no tiene un selector de proforma.
- Deja hoy: el vinculo queda en la proforma (`registroCompraId`), no como una eleccion hecha desde la fila de la factura. El libro no edita la cuenta de la proforma. El costo del mes lo arma el traspaso (CU-38) con la cuenta fija de mano de obra, aunque la factura todavia no este asociada. `cuentaGastoId` se guarda en la proforma y el traspaso no la usa como debe. Para listar en la asociacion, el codigo pide proformas enviadas al contratista, no solo aprobadas.
- Pide la sala: en el libro de compras se elige proforma o OC. La cuenta no se edita ahi. El costo de la proforma aprobada puede quedar imputado antes del calce. El listado de asociacion muestra proformas aprobadas, no solo las notificadas.
- Depende de: CU-31, CU-32 y CU-37. La OC del mismo libro es CU-15.

### CU-37. Cuenta mano de obra contratista

- Entra hoy: el ingreso guarda labor, actividad y centro de costo (CU-28). La cuenta del asiento de cierre la resuelve `resolveCuentasCierreSala` al traspasar, `POST /contratistas/traspaso-cierre`.
- Deja hoy: el debe del cierre es la cuenta `6-1-01-01-002` o, si no esta el codigo, una cuenta de gasto cuyo nombre es mano de obra contratista. El haber es facturas por recibir contratistas, `2-1-08-02-003`. El asiento agrupa por centro de costo. No pide una cuenta distinta por linea de la proforma. La labor y la actividad quedan en el ingreso, no en una linea del asiento.
- Pide la sala: una cuenta de gasto, mano de obra contratista. El ingreso guarda labor, actividad y centro de costo. La proforma no pide una cuenta por linea.
- Depende de: CU-28 y CU-29. El asiento del mes es CU-38.

### CU-38. Centralizacion del mes en un asiento

- Entra hoy: Contratistas > Traspaso contable y cierre de mes, debajo de Auditoria, `/contratistas/traspaso`. `GET /contratistas/traspaso-cierre` y `POST /contratistas/traspaso-cierre`. `/contabilidad/centralizacion` redirige a esa ruta.
- Deja hoy: un cierre por empresa y periodo `aaaa-mm`. Toma proformas `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA` de ese periodo. Deja fuera borrador, pendiente de aprobacion y rechazada. Arma un solo asiento, origen `TRASPASO-CTR:periodo`, debe mano de obra por centro de costo y haber facturas por recibir contratista. El periodo del asiento es el de la proforma, no la fecha de la factura. Si el periodo ya esta cerrado, no lo vuelve a traspasar.
- Pide la sala: un cierre por mes, un asiento agrupado, solo proformas aprobadas, gasto en el mes de la proforma, menu unico de traspaso y cierre.
- Depende de: CU-31, CU-35 y CU-37. Abrir el mes es CU-41.

### CU-39. Al asociar la factura, facturas por recibir contra proveedor

- Entra hoy: primero el vinculo de CU-36. El asiento del calce nace al contabilizar el registro, `PUT /registros-compra/:id` con estado contabilizado. La vista previa es `GET /registros-compra/:id/asiento-preview`.
- Deja hoy: si la proforma ya apunta a ese registro y tiene tipo contable, el asiento es debe facturas por recibir contratistas (`2-1-08-02-003`) y haber proveedores, mas el IVA si corresponde. No vuelve a reconocer el gasto. En ese caso no exige una OC para contabilizar. La cuenta no se reescribe en el libro: sale del plan por codigo. El gasto previo es el asiento de CU-38.
- Pide la sala: el calce saca facturas por recibir y deja al proveedor. No vuelve a reconocer el gasto. La cuenta no se edita en compras.
- Depende de: CU-36 y CU-38.

### CU-40. Precio estimativo en el trato, editable despues

- Entra hoy: el precio va en el ingreso, `POST /ingresos-labor-diario` y `PUT /ingresos-labor-diario/:id`.
- Deja hoy: si hay tarifa vigente, el precio sugerido es esa tarifa. Cambiarlo pide el permiso `contratistas:rate-override` y un motivo. Si no hay tarifa, se puede guardar un precio, incluido cero: el mensaje de la API dice que cero sirve para una asistencia pendiente de valorizar. Un precio mayor que cero sin tarifa tambien pide el permiso de override. El ingreso solo se edita mientras esta pendiente, o cuando la proforma enviada esta en reclamo. Una proforma definitiva, sin reclamo, no deja corregir el precio del ingreso.
- Pide la sala: registrar la labor con un valor estimativo y corregirlo despues. El precio cero no queda habilitado por la sala. Si la proforma ya esta aprobada o facturada, la correccion sigue CU-34.
- Depende de: CU-28 y CU-34.

### CU-41. El cierre de mes trabaja contra proformas

- Entra hoy: el mismo traspaso de CU-38. Reabrir: `POST /contratistas/traspaso-cierre/:periodo/reabrir`.
- Deja hoy: un ingreso sin proforma no entra al asiento. El cierre no lo arrastra por existir. Reabrir anula el asiento del traspaso si el periodo contable no esta cerrado. Si el periodo contable sigue cerrado, pide abrirlo primero. No hay tope de una proforma por mes: CU-30 ya deja varias.
- Pide la sala: un dia con labor y sin proforma no entra al asiento. Si el mes se cerro y queda una proforma pendiente, el mes se puede volver a abrir.
- Depende de: CU-30 y CU-38.

### CU-42. El correo de la OC es interno

- Entra hoy: no hay pantalla ni endpoint que envie la OC a un usuario. La orden no tiene "notificar".
- Deja hoy: el correo que existe en compras es el del libro de compras (CU-10), plantilla `COMPRAS`, sobre la factura recibida, con destinatario usuario del sistema y copia. No adjunta la OC ni la manda desde `/compras/ordenes`. No hay portal de proveedor.
- Pide la sala: desde la OC, avisar a un usuario interno con el documento, con copia y con un correo externo escrito a mano.
- Depende de: ninguno. No es CU-10 ni CU-33.

### CU-43. PDF y Excel de los reportes contables

- Entra hoy: Libro diario `/contabilidad/libro-diario` (`GET /libro-diario`). Libro mayor `/contabilidad/mayor` (`GET /mayor`). Balance de ocho columnas `/contabilidad/balance-8-columnas` (`GET /balance-8-columnas`). Estado de resultados `/contabilidad/estado-resultados`. Los cuatro tienen Excel y "Exportar PDF".
- Deja hoy: el Excel exporta las columnas de la grilla. El PDF abre una ventana de impresion del navegador con razon social, RUT, domicilio si existe, nombre del reporte y periodo, y la tabla de la grilla. El estado de resultados tiene las dos descargas. La situacion financiera, que la sala no pidio, usa la misma pagina con otro modo.
- Pide la sala: esos cuatro en PDF y en Excel. El PDF identifica empresa, reporte y periodo. El Excel respeta las columnas de la grilla.
- Depende de: ninguno. El PDF del comprobante de venta es CU-06 a CU-09, no este caso.

### CU-44. El pago del contratista es el de la factura asociada

- Entra hoy: no hay un pago dentro de contratistas. El pago de la factura es Tesoreria > Pagos, `/tesoreria/pagos`, `POST /pagos`, contra el registro de compra o el proveedor.
- Deja hoy: despues del calce de CU-39, el saldo por pagar queda en la cuenta del proveedor y en el aging. No hay nomina, anticipo ni documento de pago propio del modulo de contratistas. La nomina de CU-25 es la de tesoreria, para cualquier documento con vencimiento.
- Pide la sala: el pago es el de esa factura de proveedor. No hay un documento de pago propio de contratistas.
- Depende de: CU-39. La nomina general es CU-25 y no cierra este modulo.

---

## Modulos que toca

Carpetas Nest en `ERP/erp_back/src/modules`:

- `catalogos`: ficha de proveedor, plazos, copia por RUT.
- `comercial`: ficha de cliente, lookup de RUT, asiento de venta al contabilizar.
- `contabilidad`: elemento de costo, comprobante, libro diario, mayor, balance y estado de resultados.
- `parametrizacion/indicadores-bc`: historico del Banco Central.
- `compras`: OC, cadena, libro, aviso, asociacion de hijas y asiento de la factura.
- `aprobaciones`: escala de OC y de proforma.
- `insumos`: guia, stock, madre, hija, saldo y devolucion a proveedor.
- `contratistas`: ficha, ingreso, proforma, reclamo, traspaso y reapertura.
- `tesoreria`: estado de cuenta por RUT, nomina, aging y pago de la factura.
- `admin`: flags de la empresa y plantillas de correo.
- `notificaciones`: aviso interno de OC pendiente y de factura sin OC.

Carpetas React:

- `ERP/erp_front/src/features/catalogos`
- `ERP/erp_front/src/features/comercial`
- `ERP/erp_front/src/features/contabilidad`
- `ERP/erp_front/src/features/compras`
- `ERP/erp_front/src/features/insumos`
- `ERP/erp_front/src/features/contratistas`
- `ERP/erp_front/src/features/tesoreria`
- `ERP/erp_front/src/features/admin`
- `ERP/erp_front/src/pages/parametrizacion`
- `ERP/erp_front/src/app` (rutas y menu)
