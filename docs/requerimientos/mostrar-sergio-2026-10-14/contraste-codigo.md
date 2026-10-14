# Contraste de código: qué mostrar el 14/10/2026

Fecha: 2026-10-14. Fuentes: `casos-de-uso.md`, `plan-integracion.md`, `plan-pruebas.md`. Este archivo lee el código de `ERP/erp_back` y `ERP/erp_front`. No abre el ERP, no emite DTE, no paga, no cierra el mes y no envía correo.

Conteo de las 15 pruebas: **8 cumple**, **4 parcial**, **0 no cumple**, **3 solo mostrar**.

La orden madre sigue en Compras > Órdenes de compra. La hija de una recepción parcial sigue siendo el trozo recibido (`crearOcHijaDeRecepcion`). El cierre de saldo achica la madre y no crea hija por el faltante (`solicitarCierreSaldoOc`). Esas dos funciones no se reabrieron.

## Veredicto de las pruebas

| Prueba | Veredicto | Dónde |
|---|---|---|
| P-1-01 | cumple | `glosaAsientoVenta`, `rutSinDigito` y `buildAsientoVentasLineas` en `comercial.service.ts`. Pantalla: `AsientosPage`, `glosaVisible` y `cuentaEnComprobante` en `comprobante-vista.ts`. |
| P-1-02 | cumple | Columnas en `AsientosPage`. Conversión: `montosLinea` y `tasasDelDia` en `comprobante-vista.ts`. Si no hay tipo cargado: `tipoCambioDelDia` dentro de `grabarDocumentoContabilizar`. |
| P-1-03 | parcial | La madre no arma comprobante. La cuenta de la factura sale de la primera línea con imputación (`dimsDesdeLineasOc`), no de cada línea. Si ya hay recepción, el debe del preview dice Plan de cuentas (`cuentaHaberRecepcion`). |
| P-1-04 | solo mostrar | Rutas `/contabilidad/balance-8-columnas` (`Balance8ColumnasPage`) y `/contabilidad/libro-diario` (`LibroDiarioPage`). |
| P-2-01 | parcial | Ficha y catálogos están. En el ingreso faltan forma de pago y duración. La unidad se ve en la grilla, no como campo del formulario. |
| P-2-02 | parcial | `createProforma` marca los ingresos y no los vuelve a ofrecer. La misma pantalla de proformas sigue ofreciendo Generar OC. |
| P-2-03 | cumple | No hay proforma hija. `asociarFacturaProforma` cuelga la proforma entera. `reemitirProforma` copia el mismo monto y deja la anterior rechazada. |
| P-3-01 | cumple | `ordenesCompraCandidatasParaRegistro` en `asociar-oc-registro.util.ts`. El vínculo es `vincularOcRegistroCompra`. |
| P-3-02 | cumple | Listado y panel en `ComprasPages.tsx`. Hija: `crearOcHijaDeRecepcion`. Cierre: `solicitarCierreSaldoOc`. |
| P-3-03 | cumple | La OC queda en `RegistroCompra.ocId` (`vincularOcRegistroCompra`). `GuiaInsumoRecibida` no tiene `ocId`. `createGuiaInsumoRecibida` no la guarda. |
| P-4-01 | cumple | `asociarFacturaProforma` suma proformas al mismo registro y, con `registroCompraId`, no pide cuenta. El modal del libro marca una por vez. |
| P-4-02 | solo mostrar | La asociación no escribe cuenta. `planAsientoRegistroCompra` puede rotular Tipo de contrato si alguien abre Contabilizar: eso no se usa como respuesta. |
| P-5-01 | cumple | Modal `RegistroCompraNotificarModal`. Texto: `mensajeNotificacionSinOcDisponible`. Envío solo si `enviarCorreo` es true, en `notificarRegistroCompra`. |
| P-5-02 | parcial | Se ven la proforma, el e-mail y las acciones. `marcarProformaEnviadaContratista` deja la proforma notificada sin correo. |
| P-5-03 | solo mostrar | Plantilla VENTAS en `ConfiguracionSmtpPage` (`/admin/configuracion-correos`). |

## 1. Contabilización

### CU-1-01. Comprobante de venta

| Pieza | Veredicto | Por qué |
|---|---|---|
| `grabarDocumentoContabilizar` | CONSERVAR | Arma el asiento de una venta ya emitida. No se crea un asiento nuevo para la reunión. |
| `glosaAsientoVenta` | CONSERVAR | La glosa es `FACTURA mes/año`, el tipo de cambio si hay, y el comentario (`observaciones`). No usa el texto del ítem. |
| `buildAsientoVentasLineas` | CONSERVAR | Esa glosa se repite en cliente, IVA e ingreso. El auxiliar es `rutSinDigito` (cuerpo del RUT, sin dígito verificador). La cuenta de IVA es `CODIGO_IVA_DEBITO` (`2-1-09-02-001`), no caja. |
| `cuentaEnComprobante` | CONSERVAR | Si un asiento viejo dejó el IVA en la cuenta caja y la glosa dice IVA débito, la pantalla lo muestra como IVA débito. No reescribe el asiento. |
| `glosaVisible` | CONSERVAR | En el detalle y en el PDF se lee la glosa de cabecera. El mayor (`MayorPage`, `/contabilidad/mayor`) muestra la glosa de la línea, que en este camino es la misma. |
| Nombre del dueño en el comprobante | NO USAR | `comprobante-print.ts` y `AsientosPage` no imprimen un dueño. |
| Asiento 20260041 | NO USAR como prueba corrida | El código cumple el armado. Este contraste no abrió ese número. |

P-1-01: cumple.

### CU-1-02. Compra desde la hija

| Pieza | Veredicto | Por qué |
|---|---|---|
| `previewAsientoRegistroCompra` y `planAsientoRegistroCompra` | CONSERVAR el camino sin recepción previa | Sin asiento `RECEPCION:{ocId}`, el gasto usa la cuenta de la OC (`resolveCuentasAsientoCompra`, origen `OC`). La etiqueta del modal es Orden de compra (`RegistroCompraContabilizarModal`). |
| `dimsDesdeLineasOc` | CAMBIAR no, en esta demo | Toma la primera línea que tenga cuenta o centro. No arma una línea de comprobante por cada línea de la OC. Por eso P-1-03 queda parcial. No se parte el asiento en esta pasada: la demo no aprieta Aceptar y contabilizar. |
| `cuentaHaberRecepcion` | NO USAR como la regla de la proforma | Si la hija ya tiene recepción contabilizada, el debe de la factura es Facturas por recibir y el origen sale Plan de cuentas. La cuenta de gasto ya se usó en la recepción, copiada de la línea de la madre. |
| `crearOcHijaDeRecepcion` | CONSERVAR | Número `madre.N`, estado `APROBADO`, neto del trozo, cuenta y centro de la madre. El asiento de esa recepción, si nace, usa `RECEPCION:{id de la hija}`. |
| Comprobante de la madre | NO USAR | `solicitarCierreSaldoOc` no crea asiento. El origen de la factura es `COMPRA:{factura}`, no el número de la madre. |

P-1-03: parcial. La hija es el documento que se asocia y la madre no es un comprobante. El preview no repite cuenta y centro en cada línea de la OC, y con recepción previa no dice Orden de compra.

### CU-1-03. Balance y libro diario

| Pieza | Veredicto | Por qué |
|---|---|---|
| `Balance8ColumnasPage` y `LibroDiarioPage` | CONSERVAR para mostrar | Las rutas existen. No se generan asientos para cuadrar. |

P-1-04: solo mostrar.

## 2. Contratistas

### CU-2-01. Ficha e ingreso diario

| Pieza | Veredicto | Por qué |
|---|---|---|
| `Contratista.codigo` y `allocateNextContratistaCodigo` | CONSERVAR | Correlativo `CTR-00001`, distinto del RUT. El formulario no pide el código a mano. |
| `creadoPorNombre` | CONSERVAR | La ficha guarda quién la creó. |
| `IngresoLaborDiarioPage` | CONSERVAR lo que ya tiene | Fecha, contratista, cuartel (centro de costo), labor, actividad, jornada o trato, cantidad, precio, predio opcional, temporada, sector y faena de catálogo. No hay trabajador. El indicador Pendientes de proforma cuenta estado `PENDIENTE`. |
| Forma de pago y duración | NO USAR como si ya estuvieran | No están en el modelo `IngresoLaborDiario` ni en el formulario. `tipoPago` vive en la ficha del contratista, no en el ingreso. No se agregan columnas: haría falta una migración y esta pasada no la corre. |
| `unidad` | CONSERVAR en la grilla | El modelo la tiene. La columna Tarifa aplicada muestra precio y unidad. El formulario del ingreso no pide la unidad: sale de la tarifa. |

P-2-01: parcial. Código, RUT, nombre, creador, total, sin trabajador, y cuartel y faena de mantenedor están. Faltan forma de pago y duración en el ingreso.

### CU-2-02. Varios ingresos en una proforma

| Pieza | Veredicto | Por qué |
|---|---|---|
| `createProforma` | CONSERVAR | El monto es la suma de los ingresos. Los deja `ASOCIADO` con `proformaId`. Otro alta solo toma `PENDIENTE` o `PENDIENTE_APROBACION`. |
| Aprobación de la proforma | CONSERVAR | `marcarProformaDefinitiva` pide la cadena de la proforma, no de cada ingreso. El supervisor del ingreso es opcional. |
| Modal Asociar factura / generar OC en `ProformasContratistaNivel1Page` | NO USAR en la demo | Si no hay registro, el botón dice Generar OC y el texto manda al cierre de saldo de Compras. Eso choca con "la proforma no se convierte en OC". La ruta `/contratistas/proformas` es esta pantalla. La asociación que se muestra es la del libro. |

P-2-02: parcial. Los ingresos usados no vuelven a ofrecerse. La pantalla sigue ofreciendo generar una OC.

### CU-2-03. La proforma no se parte

| Pieza | Veredicto | Por qué |
|---|---|---|
| Modelo `ProformaContratista` | CONSERVAR | No tiene padre ni hija. |
| `asociarFacturaProforma` con `registroCompraId` | CONSERVAR | Escribe `registroCompraId` y estado `FACTURADA` sobre la proforma completa. Si la suma supera el neto de la factura, rechaza. No achica el monto ni crea otra proforma. |
| `reemitirProforma` | NO USAR como parcial | Crea otra proforma con el mismo `montoNeto` y deja la anterior `RECHAZADA`. No es una hija por el faltante. |
| Rama sin `registroCompraId` (generar OC) | NO USAR en la demo | Crea una OC por el total de las proformas. No parte la proforma. |

P-2-03: cumple.

## 3. Asignación de la OC

### CU-3-01. OC del proveedor en el libro

| Pieza | Veredicto | Por qué |
|---|---|---|
| `ordenesCompraCandidatasParaRegistro` | CONSERVAR, con el filtro por id | Saca anuladas, con `cerradaAt`, y las ya cubiertas por el neto de otra factura. Si el registro y la OC tienen `proveedorId`, compara ese id: una razón social distinta no esconde la OC del mismo proveedor. Si falta el id, sigue el texto parecido. |
| `vincularOcRegistroCompra` | CONSERVAR | Escribe `ocId` y `ocNumero` en el registro que ya existe. No crea OC. |
| Aviso sin candidatas | CONSERVAR | El modal ofrece Sí, notificar. Eso abre P-5-01 y no envía solo por abrirlo. |

P-3-01: cumple.

### CU-3-02. Madre e hija en Compras

| Pieza | Veredicto | Por qué |
|---|---|---|
| Columna "Hija de #" y panel "Madre / hijas" en `ComprasPages.tsx` | CONSERVAR | La madre se ve en el listado de Compras. No hay pantalla de madre en Insumos. |
| `crearOcHijaDeRecepcion` | CONSERVAR | Es el nacimiento del trozo. No se cambia. |
| `solicitarCierreSaldoOc` | CONSERVAR | Baja el neto de la madre a lo recepcionado, la deja `PENDIENTE_APROBACION` y no crea hija. En la demo no se aprieta. El botón del detalle sigue diciendo Cierre de saldo. |
| Frase de María Jesús "la madre solo en insumos" | NO USAR | El usuario ya decidió el listado de Compras. |

P-3-02: cumple. El ejemplo OC-2026-0016 / OC-2026-0017 no se abrió en esta lectura. Sirve si la hija es `madre.N`, `APROBADO` y neto del trozo. Una hija `BORRADOR` con correlativo `OC-AAAA-NNNN` sería el cierre viejo y no se usa.

### CU-3-03. La OC va en la factura, no en la guía

| Pieza | Veredicto | Por qué |
|---|---|---|
| `vincularOcRegistroCompra` y `linkOrdenCompraFromReferencias` | CONSERVAR | La OC queda en el registro de compra (la factura del libro). |
| `createGuiaInsumoRecibida` y `precioGuiaDesdeOrden` | CONSERVAR | La guía mueve stock. Puede leer un precio de una OC del mismo proveedor. No guarda `ocId` y no crea la hija. |
| Modelo `GuiaInsumoRecibida` | CONSERVAR | Sin `ocId`. |

P-3-03: cumple.

## 4. Proforma en el documento de compra

### CU-4-01. Una o varias proformas

| Pieza | Veredicto | Por qué |
|---|---|---|
| `AsociarOcRegistroCompraModal` | CONSERVAR | Lista proformas `DEFINITIVA` o `ENVIADA_CONTRATISTA` sin factura ni orden. Elegir proforma vacía la OC del formulario, y al revés. El aviso al guardar dice que no se creó una orden (`doVincularProforma`). |
| `asociarFacturaProforma` | CONSERVAR | Un segundo llamado sobre el mismo registro suma: no borra el `registroCompraId` anterior. Exige el mismo contratista, moneda y tipo. No exige cuenta contable cuando viene `registroCompraId`. |
| Una proforma por acción en el modal | CONSERVAR | El radio marca una. La siguiente, si cabe en el neto, se agrega. No hace falta una pantalla nueva. |
| Generar OC desde Contratistas | NO USAR | No es el vínculo del libro. |

P-4-01: cumple.

### CU-4-02. Cuenta de la proforma

| Pieza | Veredicto | Por qué |
|---|---|---|
| Cuenta al asociar | NO USAR | El camino con `registroCompraId` no la pide ni la inventa. |
| Origen Tipo de contrato en `planAsientoRegistroCompra` | NO USAR como respuesta de María Jesús | Si la proforma tiene `tipoContratoId` y alguien abre Contabilizar, el preview puede decir Tipo de contrato. La demo no abre ese modal. |

P-4-02: solo mostrar.

## 5. Correo

### CU-5-01. Aviso si la factura no trae OC

| Pieza | Veredicto | Por qué |
|---|---|---|
| `RegistroCompraNotificarModal` | CONSERVAR, casilla apagada | Elige usuario, asunto y cuerpo. La casilla de correo arranca apagada y ya no se prende sola cuando hay SMTP. Confirmar con la casilla apagada no llama a `queueEmailUseCase`. |
| `mensajeNotificacionSinOcDisponible` | CONSERVAR | El texto nombra factura, proveedor y monto, y dice que está sin orden de compra. |
| `notificarRegistroCompra` | CONSERVAR | El correo sale solo con `enviarCorreo === true`. Siempre deja el aviso en el ERP y una fila en `RegistroCompraNotificacionEvento`. |
| `NotificacionTimeline` | CONSERVAR | Muestra fecha, quién avisó y a quién. |
| Crear la OC desde el libro | NO USAR | El modal no la crea. |

P-5-01: cumple. En la demo no se aprieta Enviar.

### CU-5-02. Correo de la proforma

| Pieza | Veredicto | Por qué |
|---|---|---|
| Botón E-mail y `enviarProformaEmailContratista` | CONSERVAR para mostrar | Envía solo al hacer clic. Mostrarlo no dispara el correo. |
| `marcarProformaEnviadaContratista` (Notificar contratista) | NO USAR en la demo | Pasa a `ENVIADA_CONTRATISTA` sin SMTP. |
| `EnvioOperativoContratistasPage` | CONSERVAR para mostrar | Tiene periodo desde / hasta. El correo sale si se marca la casilla. No se marca. |
| Estado "notificada a proveedor" armado después del corte de luz | NO USAR como pedido del cliente | El nombre no se presenta como requisito. |

P-5-02: parcial. La pantalla está. Notificar contratista marca el envío sin que haya salido un correo.

### CU-5-03. Correo de venta

| Pieza | Veredicto | Por qué |
|---|---|---|
| Plantilla VENTAS en `ConfiguracionSmtpPage` | CONSERVAR para mostrar | También están COMPRAS, PROFORMAS y el servidor. No se graba ni se prueba el SMTP. |

P-5-03: solo mostrar.

## Correcciones de esta lectura

El aviso sin OC podía salir por correo al confirmar, porque el modal prendía la casilla cuando el SMTP estaba configurado. Quedó apagada. El texto del aviso ahora incluye el monto. El combo de OC del libro ya no esconde una orden del mismo `proveedorId` solo porque la razón social no coincide.

Archivos:

- `ERP/erp_front/src/features/compras/RegistroCompraNotificarModal.tsx`
- `ERP/erp_front/src/features/compras/asociar-oc-registro.util.ts`
- `ERP/erp_front/src/features/compras/asociar-oc-registro.util.node.spec.ts`
- `ERP/erp_back/src/modules/compras/compras.service.spec.ts`

Pruebas corridas, solo esos archivos: el test de `notificarRegistroCompra` con la casilla apagada (`npx jest --runInBand`, filtro de ese caso) y `asociar-oc-registro.util.node.spec.ts`. No se corrió la suite entera.
