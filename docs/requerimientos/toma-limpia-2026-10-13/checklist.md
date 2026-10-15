# Checklist: pedido vigente contra el codigo

Fecha del contraste: 13/10/2026. El pedido es el de la transcripcion mas nueva. El estado sale del schema Prisma y de los servicios en `ERP/erp_back`, no de un documento previo.

| Estado | Significado |
|---|---|
| hecho | El modelo y el servicio cubren el pedido |
| a medias | Hay una parte y falta la que el cliente nombro |
| falta | No esta en el codigo |
| diferido | El propio cliente lo dejo para despues |

## Compras

| Pedido | Estado | En el codigo |
|---|---|---|
| La orden de compra es el documento de arranque. No hay solicitud de compra. La cotizacion no es un mantenedor: queda como tipo, folio y fecha. | hecho | `OrdenCompra.referenciaTipo/Folio/Fecha`. Las rutas de cotizaciones redirigen a ordenes. No hay modelo de solicitud. |
| Pedir varias cotizaciones y elegir (30/07). | a medias | No hay comparador. Quedo el adjunto de la frase del 23/09. |
| Cadena por monto, en pesos aunque la orden este en dolares. Rechazo devuelve al mismo documento y se recorre de nuevo. Historial y motivo. | hecho | `AprobacionOc`, `motivoRechazo`, grupos y escalas. |
| Factura de una orden aun no aprobada: se recibe, se destaca, no se contabiliza ni se paga. | hecho | `ocNoAprobada` en `compras.service.ts`. |
| Sin reclamo en el plazo, la factura queda aceptada. No hay rechazo automatico. | a medias | El codigo usa 8 dias (`aceptacionCompraPlazoDias`). El 14/09 dijeron 8 y el 23/09 dijeron 7. El 01/10 nadie corrigio el 7. |
| Orden madre y facturas parciales como hijas. La hija no se aprueba. El 01/10 la madre queda solo como dato de insumos y no se muestra en los otros modulos. | a medias | Existen `ocPadreId` y `ocHijas`. El schema dice que las hijas no se facturan en partes. No hay un corte que esconda la madre fuera de insumos. |
| Plazo del neto y plazo del IVA por separado, heredados del proveedor y editables. | hecho | `condicionPagoDias` y `condicionIvaDia` en `Proveedor`. |
| Aviso si el RUT de la factura no esta en el maestro, sin rechazarla al tiro. Aviso a quien debe crear la orden, con correo. | a medias | Hay asociacion manual al libro. No aparecio un aviso de "RUT observado" ni lista de vigilancia por proveedor. |
| Carga manual de factura con PDF cuando el XML no llega a GoSocket. | a medias | El libro de compras existe. No confirme en esta pasada una carga solo-PDF separada de la sincronizacion. |
| Varios archivos de respaldo en la compra y en la venta (cotizacion, presupuesto, contrato). El 24/09, en el mismo tramo, primero dijeron que ventas no llevaba adjuntos y despues corrigieron: compras y ventas, mas de un archivo. | falta | La orden guarda tipo, folio y fecha. No hay campo de archivos en `OrdenCompra` ni en el documento de venta. |

## Contratistas

| Pedido | Estado | En el codigo |
|---|---|---|
| Sin modulo de mano de obra. Labor y actividad viven en contratistas. | hecho | Modelos `Labor`, `Actividad`, `LaborActividad`. No hay modulo de remuneraciones. |
| Ingreso diario con jornal o trato, y proforma que agrupa varios ingresos. | hecho | `IngresoLaborDiario`, `TipoJornadaLabor` JORNADA/TRATO, `ProformaContratista`. |
| La proforma pasa por jefatura (06/10). | hecho | Estado `PENDIENTE_APROBACION` y campos de cadena en la proforma. |
| Una factura calza varias proformas y no se parcializa. | hecho | `FacturaContratista.proformasGrupoIds`. |
| Ficha con codigo secuencial, distinto del RUT de proveedor. | a medias | `Contratista` existe y se relaciona con `Proveedor`. No revise si el codigo es un correlativo propio y no el RUT. |
| Predio opcional, sector, cuartel y faena de mantenedor. Estado "enviado al contratista" para no reenviarla. | falta | El ingreso diario tiene centro de costo, labor y actividad. En el schema no estan predio, cuartel, sector ni un estado de envio. |
| Correo al contacto cuando la proforma ya esta aprobada. | falta | No hay marca de envio en el modulo de contratistas. |

## Ventas y facturacion

| Pedido | Estado | En el codigo |
|---|---|---|
| El documento se llama orden de venta. Guardar valida stock. Facturar va en Emitir, no en la orden. | hecho | `comercial.service.ts`. No hay cadena de aprobacion de OV. |
| No vender bajo el precio de bodega en nacional. Exportacion sin ese piso. | hecho | Piso en la venta; comentario en linea 1160: exportacion no aplica piso. |
| Flete como linea. Producto con bodega; servicio sin bodega. | hecho | Tipo de linea y bodega en la orden de venta. |
| Cuenta y centro de costo al contabilizar el libro de ventas, no en la orden. | hecho | El DTE queda por contabilizar y la cuenta se asigna en el libro. |
| Factura de exportacion: tipo de cambio del dia, un solo tipo para toda la factura, campos de aduana, puerto filtrado por pais, via maritima o aerea. | a medias | Hay indicador `EXPORTACION` y tipo de cambio. No confirme en esta pasada el filtro de puertos ni la via de transporte. |
| Nota de credito o debito precargada desde la factura, con el tipo de cambio de origen. | a medias | Hay emision de NC/ND. El precargado de exportacion hay que probarlo en pantalla. |
| Emitir en el ERP y que GoSocket informe al SII. Folio, PDF y tracking dentro del ERP. | a medias | El cliente HTTP a billing-gateway esta. YoFacturo y el contrato seguian bloqueados el 15/09. |
| Correo al cliente con PDF o XML, y otro correo interno de aprobacion, desde la casilla de contabilidad. | a medias | Hay plantillas y SMTP. El envio automatico al emitir no quedo cerrado como flujo unico. |

## Inventario

| Pedido | Estado | En el codigo |
|---|---|---|
| Stock por bodega y por empresa. Salida al vender. Entrada desde la orden. | hecho | `StockInsumoBodega`, `MovimientoBodega`, `Bodega`. |
| El insumo entra con guia. La factura de fin de mes se asocia a la orden. Devolucion a proveedor solo en ALM. | a medias | Existe `GuiaInsumoRecibida`. La devolucion con el precio de esa factura, y no el promedio, hay que confirmarla en el movimiento. |
| Avisar si el articulo ya existe, para no partir el stock. | falta | No lo busque como regla de alta duplicada en esta pasada. El maestro de insumo existe. |
| Precio promedio solo informativo. El movimiento se valoriza al precio de la orden con la que entro. | a medias | Hay costo y precio de compra en el insumo. La valorizacion del movimiento al precio de esa orden no quedo demostrada aqui. |
| Seguimiento de cajas de exportacion por Excel, para la devolucion de IVA. | falta | No hay un modulo de cajas. |

## Contabilidad

| Pedido | Estado | En el codigo |
|---|---|---|
| Plan con subniveles. Cuenta con movimientos se inactiva, no se borra. | hecho | `CuentaContable` y relaciones a centro, elemento y area. |
| Comprobante en pesos y dolares, y yuan como tercera columna en todos los casos (01/10). | a medias | Indicadores BC tienen `cny`. La cartola acepta CNY. El asiento guarda el detalle en JSON y la contabilidad conoce CNY. No hay tres columnas fijas en el modelo `Asiento`. |
| Tipo de cambio del Banco Central, con digitacion en feriado. | hecho | `IndicadorBc` y monedas con `codigoSerieBCCH`. |
| Auxiliar = RUT sin digito verificador. Glosa repetida en todas las lineas, con numero de factura. | a medias | El auxiliar y la glosa existen como dato. No confirme el formato exacto del 01/10. |
| Area de negocio fuera de uso (01/10). | a medias | Sigue en el plan (`CuentaAreaNegocio`). El cliente dijo que no la ocupan. |
| Cierre por modulo, no un solo cierre global. | hecho | Periodos de contabilidad y de contratistas. |
| Libro mayor, balance de 8 columnas y diario como los que mandaron de ejemplo. | a medias | Hay centralizacion. No contraste los tres informes contra los Excel de Maria Jose. |
| Contabilidad electronica al SII. | diferido | El 30/07 la dejaron en segunda etapa, con contador externo. |
| Carga historica desde Agrosoft (del orden de 19.000 movimientos) y DTE de un ano. | falta | Es migracion de datos, no una pantalla cerrada. El historial de Acepta no quedo respaldado. |

## Tesoreria

| Pedido | Estado | En el codigo |
|---|---|---|
| Cartola por carga. Cada movimiento se contabiliza. Lo pendiente es lo no contabilizado. | hecho | `CartolaBancaria`, `MovimientoCartola`. |
| Desconciliar un movimiento sin reversar el mes. | hecho | `POST movimientos-conciliacion/:id/desconciliar`. |
| Nomina semanal de pagos. Mover la semana no cambia el vencimiento. Egresos calzan contra la nomina. Ingresos, de a uno. | hecho | Nomina y `DocumentoAging`. |
| Tres tipos de pago: total, anticipo y anticipo productor, con tipo de cambio editable y registro. | hecho | `Pago` y `AnticipoProductor`, `PagoTcEvento`. |
| Flujo por concepto y codigo financiero, en pesos. Apertura que no se borra, por banco y moneda. | hecho | `ConceptoFlujo`, `CodigoFinanciero`, `MovimientoCaja.esApertura`. |
| Estado de cuenta del RUT, aunque sea cliente y proveedor, con anticipos restados. | hecho | Cuenta corriente y ficha cruzada por RUT. |
| Banco en linea. | diferido | El 14/09 lo dejaron para despues de la puesta en marcha. |
| Mantenedor de plazos de atraso, con critico configurable (30 y 90). | a medias | Hay `nominaDiasCritico` por empresa y por proveedor. Falta ver si la pantalla tiene los dos filtros rapidos que pidio Lupe. |

## Admin

| Pedido | Estado | En el codigo |
|---|---|---|
| Empresas aisladas. Roles con lectura y escritura por pantalla. El nombre de quien hizo el movimiento, no el cargo. | hecho | `UsuarioEmpresa`, `Rol`, auditoria en varios modelos. |
| Ingreso con Microsoft, sin clave, con los mismos correos. | a medias | `POST /auth/microsoft` existe. Queda prendido solo si hay tenant y client id. |
| Fichas separadas de cliente y de proveedor, con bancos, contactos y despacho. Al escribir el RUT, copiar si ya existe en la otra. | hecho | `Cliente` y `Proveedor` con cuentas, contactos y direcciones. Flag `esProductor`. No hay maestro Productor. |
| Alta de cliente o proveedor solo por jefatura. | a medias | Hay permisos por pantalla. No confirme que el formulario este partido en un solo perfil. |
| Temporada en el ingreso, como en Agrosoft. | falta | No hay un cambio de temporada en la sesion. |
| Maquinaria agricola y graficos de gerencia. | falta | No hay modulo. |
| Logo y pie por empresa en los impresos. Excel como salida principal de los listados. | a medias | Hay preferencia de tablas. No confirme logo y pie en todos los impresos. |

## Lo que falta, en una lista corta

1. Predio, cuartel, sector y el estado "enviado al contratista" en el ingreso y la proforma.
2. Correo al contratista cuando la proforma queda aprobada.
3. Varios archivos de respaldo en la compra y en la venta. La orden solo guarda tipo, folio y fecha. El comparador de varias cotizaciones de julio no tiene pantalla.
4. Yuan como tercera columna del comprobante, no solo como moneda de cartola y tipo de cambio. El plazo de aceptacion en codigo es 8 dias; el 23/09 dijeron 7.
5. Alertas de vigilancia por proveedor (campana y correo, sin lista negra automatica).
6. Seguimiento de cajas para la devolucion de IVA exportador.
7. Maquinaria y graficos de gerencia.
8. Carga historica de Agrosoft y de los DTE que Acepta no dejo.
9. Temporada al entrar, como en el sistema viejo.

Diferido por ellos, no por nosotros: banco en linea y contabilidad electronica al SII. Bloqueado afuera el 15/09: contrato GoSocket y YoFacturo.
