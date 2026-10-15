# Validación: pedido de las reuniones contra el código

Fecha: 13/10/2026. Se leyeron las 30 transcripciones de `docs/reuniones/transcripciones/`, de la del 21/07 a las dos del 13/10. `transcripcion-2026-08-20-reunion-sergio-limpia.md` no es otra reunión: es el resumen de la mañana con Sergio.

No se usaron skills, reglas ni minutas para decidir qué cuenta como pedido. Si dos reuniones chocan, queda la frase más nueva. El estado sale del código de `ERP/erp_back` y `ERP/erp_front` (modelos, servicios y pantallas), no de un documento previo. No es una prueba cliqueada de cada pantalla.

## Respuesta

No está implementado todo lo que se pidió.

El flujo diario de orden de compra, cadena, libro de compras, orden de venta, emisión, libro de ventas, cartola, nómina y proforma con aprobación sí está en el código. Lo que sigue afuera, o a medias, es concreto: archivos de respaldo, carga manual con PDF, predio y cuartel, la asociación de la proforma en el libro de compras, el yuan guardado como columna propia, la guía bajo la resolución 154, las cajas de exportación, la maquinaria y los gráficos de gerencia.

## Lo que una reunión posterior dejó atrás

Estas frases se dijeron y después se corrigieron. No se cuentan como falta.

- Cotización como documento del sistema (06/08). El 20/08 Lupe cierra que solo se genera la orden. El 23/09 y el 24/09 la cotización, el presupuesto y el contrato pasan a ser archivos, en compras y en ventas.
- Comparar tres cotizaciones y elegir (30/07 y 06/08). Queda reemplazado por ese respaldo en la orden.
- Cadena de aprobación de la orden de venta. El 14/09 queda solo compras. La orden de venta, al guardar, valida stock.
- La proforma convertida en orden de compra (dicho en internas del 21/09 y preguntado el 01/10). El 06/10 y el 13/10 María José asocia la proforma a la factura en Compras. No pide generar otra orden.
- Banco en línea y contabilidad electrónica al SII. Ellos mismos lo dejaron para después.
- Área de negocio como parámetro de gestión. El 01/10 María José dice que no la usan. El mantenedor sigue en el sistema.

## Compras

| Pedido vigente | Dónde | En el código |
|---|---|---|
| La orden es el documento de arranque. No hay solicitud ni mantenedor de cotizaciones. | 21/07 y 20/08, Lupe | Implementado. Las rutas de cotizaciones redirigen a órdenes. No hay modelo de solicitud. |
| En la orden, tipo, folio y fecha de la cotización, y además varios archivos (cotización, presupuesto, contrato) en compra y en venta. | 20/08 la referencia; 24/09 Mario pide N archivos | Parcial. `OrdenCompra.referenciaTipo`, `referenciaFolio` y `referenciaFecha`. La pantalla dice que no se adjunta archivo. No hay campo de archivos en la orden ni en la venta. |
| Cadena por monto en pesos, rechazo con motivo al mismo documento, historial, PIN. | 24/09 Mario y Carlos | Implementado. `resolveNetoClpParaCadena`, `AprobacionOc`, `motivoRechazo`. |
| Factura de una orden aún no aprobada: se destaca, no se contabiliza ni se paga. Sin lista negra. | 20/08 Mario; 14/09 María José | Implementado. `ocNoAprobada` y `ocPermiteContabilizarOPagar`. |
| Sin reclamo, a los días la factura queda aceptada sola. El 14/09 dicen 8. El 23/09 Lupe y Mario dicen 7. | 14/09 y 23/09 | Parcial. `aceptacionCompraPlazoDias` nace en 8. El cron `AceptacionCompraCron` pasa a `ACEPTADA_PLAZO`. Nadie volvió a fijar el 7. |
| Orden madre de control e hijas por la cantidad recepcionada. La hija no se aprueba. La madre, si cambia de monto, sí. El 01/10 la madre es solo dato de insumos y no se ve en los otros módulos. | 23/09, 24/09 y 01/10 María José | Parcial. Existen `ocPadreId` y la hija nace en `BORRADOR`. Al cerrar saldo, la madre vuelve a `PENDIENTE_APROBACION`. No hay un corte que impida mandar la hija a la cadena, ni uno que esconda la madre fuera de insumos. |
| Neto e IVA con plazos distintos, heredados del proveedor y editables (30, 60, 90 o un número, por ejemplo 45). | 24/09 y 01/10 | Parcial. En el proveedor están `condicionPagoDias` y `condicionIvaDia`. En la orden solo viaja `condicionPagoDias`. |
| Monedas peso, dólar y yuan. Si la factura no calza con la orden en dólares, el tipo de cambio se ajusta para que calce. | 24/09 Mario | Parcial. El catálogo tiene CNY. El calce usa el tipo observado de la fecha de la orden (`resolveTcObservadoParaOc`). La orden no guarda un tipo de cambio propio. |
| Si el XML no llega, cargar la factura a mano y subir el PDF. | 24/09 Mario | No está. El alta manual no recibe archivo. El PDF se baja de GoSocket. |
| RUT que no está en el maestro: alerta a contabilidad, la factura sigue, y se avisa a quien debe crear la orden, con traza. | 23/09 y 01/10 | Parcial. Si no hay proveedor, el registro queda y la pantalla marca «Sin proveedor». El correo es un aviso manual, no sale solo al detectar el RUT. |
| Factura al contado tratada como ya pagada. | 14/09, en el relato de contado sin vencimiento | No apareció una regla que marque esa factura de compra como pagada. |
| Libro: pendiente, aceptado y reclamado. Aceptar y reclamar en el ERP. Sincronizar con GoSocket. | 14/09 | Implementado. `AceptacionCompraEstado`, aceptar y rechazar contra GoSocket, cron de sincronización. |
| Al asociar, solo órdenes del RUT y con saldo pendiente. Cuenta y centro de costo salen de la línea. | 23/09 y 01/10 | Implementado en la asociación a orden. La proforma no está en ese selector: ver Contratistas. |

## Contratistas

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Sin módulo de mano de obra. Labor y actividad en contratistas. | 21/07 | Implementado. `Labor`, `Actividad`, `IngresoLaborDiario`. No hay módulo de remuneraciones. |
| Ficha con código correlativo distinto del RUT, más RUT, nombre y dirección. | 06/10 María José | Implementado. El alta usa `CTR-{empresa}-{n}` y el RUT va aparte. |
| Ingreso diario: jornal o trato, fecha, cantidad y valor. El trabajador no va. Cuartel y faena salen de mantenedor. Predio opcional. Sector. | 06/10 María José. El Word del mismo día, en la imagen, muestra empresa, temporada, predio, sector, cuartel y faena. El párrafo «Se registra» no nombra predio ni sector. | Parcial, con el código de Diego ya en `carlos-dev` (`9df72b6` / `3c4f66e`, integrados en `d350806` y `6189d49`). Hay `predio` y `temporada` como texto, y mantenedores `SectorContratista` y `FaenaContratista`. El cuartel de la imagen es un combo propio; en el ingreso el campo obligatorio se llama «Cuartel / centro de costo» y guarda `CentroCosto`. No hay trabajador. |
| Varios ingresos arman una proforma. Una factura calza varias proformas. No se parcializa. No hay proforma hija. | 06/10 María José; el 13/10 por la mañana el equipo repite que no hay hija | Implementado el calce. `asociarFacturaProforma` exige estado `DEFINITIVA`, suma los netos y rechaza si el monto no calza. No existe `proformaPadreId`. Una proforma no acepta ingresos de otro mes (`periodoDesdeFecha`). |
| La proforma pasa por jefatura. Aprobada, no se edita. Si hay diferencia, se corrige el ingreso y vuelve a jefatura. | 06/10 María José | Implementado. `PENDIENTE_APROBACION`, grupo tipo `PROFORMA`. En borrador se edita. `reversarProforma` la devuelve. |
| Al aprobar, correo al contacto. Lo ya enviado no se reenvía. | 06/10 María José, «sería bueno». Ni el texto ni las imágenes del Word exigen un estado previo. | Parcial, y más estricto que el pedido. Diego dejó `ENVIADA_CONTRATISTA`. `asociarFacturaProforma` rechaza la proforma si no está en ese estado. El correo al contacto no sale solo al aprobar. |
| La cuenta de costo se asigna solo en contratistas, aunque la factura no esté asociada. Al cerrar el mes: costo contra facturas por recibir. | 13/10 mediodía, María José | Parcial. El tipo de contrato tiene `cuentaDebeId` y `cuentaHaberId`. `traspasoCierre` arma el asiento. La cuenta no se edita en el libro de compras. |
| En el libro de compras se elige orden o proforma. El calce de la proforma es facturas por recibir contra el nombre del contratista. En compras se listan solo las aprobadas. | 13/10 mediodía, María José | No está en ese lugar. El libro de compras no ofrece proformas. La asociación vive en Contratistas (`Asociar factura / generar OC`) y, si no se indica un registro, `asociarFacturaProforma` crea una orden con `referenciaTipo: PROFORMA_CONTRATISTA`. Eso es el camino que ella no pidió el 13/10. |

## Ventas y documentos emitidos

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Orden de venta. Guardar valida stock y vuelve al listado. Facturar solo en Emitir. Sin cadena. | 03/09 y 20/08 | Implementado. `confirmarDocumento` deja `CONFIRMADA`. No hay `AprobacionOv`. |
| Nacional: no vender bajo el monto de bodega. Exportación: sin ese piso. | 10/09 | Implementado. El piso usa `precioCompra` o `costoPromedio`. Exportación no lo aplica. |
| Flete como línea. Producto con bodega. Servicio sin bodega. No pasar el stock de cada bodega. | 06/08 y reuniones de ventas | Implementado. `FLETE` y `SERVICIO` no mueven stock. Hay reparto `splits` por bodega. No hay un stock marcado en tránsito. |
| Cuenta y centro de costo al contabilizar el libro, por ítem. Reversar no anula el DTE. | 07/09 | Implementado en el libro. `reversarDocumento` deja el documento emitido. La API todavía acepta imputación sobre el documento. |
| Factura de exportación: aduana, país, puerto de ese país, vía, un tipo de cambio del día editable y monto en pesos. | 10/09 | Implementado. `puertosDesembarquePorPais` y `tcBcchSugerido`. |
| Nota de crédito o débito de exportación precargada. En corrección de monto el tipo de cambio se puede editar. En anulación se copia. | 10/09 | Implementado. `inheritComexFromOrigen`. El tipo se edita si el código de referencia es 3. |
| Ver PDF y XML en el ERP. Correo al cliente distinto del interno, desde la casilla de contabilidad. | 03/09 y 10/09 | Parcial. Hay descarga de PDF y XML vía billing-gateway. El correo al cliente existe. El remitente es `SMTP_FROM`, no una casilla de contabilidad aparte. |
| Guía de despacho en el alcance. Resolución 154. | 13/10, el consultor pregunta y el equipo dice que sigue pendiente | Parcial. Se emite guía (tipo 52). No hay campos de la resolución 154. |
| Quien emite y quien solo mira el libro pueden ser pantallas distintas. | 07/09 | Implementado. Pantallas separadas en el catálogo de permisos. |

## Inventario

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Un maestro. Avisar si el artículo ya existe. Bodegas de la empresa activa. | 21/07 | Implementado el aviso por código (`Ya existe un insumo con ese código`) y el filtro por empresa. |
| El insumo entra con guía. La recepción de la orden no es la que mueve la bodega. La factura de fin de mes se asocia a la orden. | 01/10 María José | Implementado. `GuiaInsumoRecibida` genera `ENTRADA_PROVEEDOR`. `createRecepcion` no llama al movimiento de stock. |
| El promedio es informativo. El movimiento se valoriza al precio de la orden con la que entró. La devolución al proveedor, solo en ALM, sale al precio de esa factura. | 10/09 y 01/10 | Parcial. Hay precio de compra y promedio. La guía usa el precio del maestro. La devolución se habilita por empresa, no queda fija a ALM, y el precio lo trae el movimiento, no la factura de origen. |
| Cada tipo de movimiento lleva cuenta al debe y al haber. El cierre de bodega es aparte del de contabilidad. | 21/07 | No está. `TipoMovimientoBodega` no tiene esas cuentas. No hay cierre de bodega. La centralización dice que bodega no entra hasta parametrizar. |
| Carga Excel del seguimiento de cajas para la devolución de IVA. En Almahue no hay reintegro de insumos. | 30/07 y 01/10 | No está. No hay módulo de cajas. |

## Contabilidad

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Plan con subniveles. Cuenta con movimientos se inactiva. Si no tiene nada, se puede eliminar. El elemento anulado queda visible. | 21/07 y 01/10 | Parcial. Hay jerarquía e inactivar. `deleteCuenta` rechaza siempre, también si la cuenta no tiene movimientos. El elemento tiene vigente y anulado. |
| Comprobante siempre en pesos y dólares, y el yuan como tercera columna en todos los casos. Tipo de cambio del Banco Central, editable, y a mano en feriado. | 01/10 | Implementado en la vista. `AsientosPage` y la impresión muestran debe y haber en pesos, dólar y yuan. Si la línea no está en yuan, ese monto se calcula al abrir con el tipo del día. El asiento guarda el detalle en JSON, no tres columnas fijas. UF, UTM e IPC no van en esas columnas. |
| Auxiliar = RUT sin dígito verificador. La glosa (comentario, número de factura, descripción corta) se repite en todas las líneas. La cuenta de IVA de la venta es IVA débito. No va el nombre del dueño. | 01/10 | Parcial. `rutSinDigito` y la glosa del comprobante se repiten (`glosaVisible`). La glosa de la venta sigue armada con tipo, folio y tipo de cambio, no solo con el comentario que pidieron. IVA débito está en la centralización. La impresión usa la razón social. |
| Cierre de mes por módulo, no uno solo. | 21/07 y 22/09 | Parcial. Hay cierre contable y traspaso de contratistas. No hay cierre de insumos. |
| Libro mayor, libro diario y balance de ocho columnas. | pedido de los informes de María José | Implementado. Rutas `libro-diario`, mayor y `balance-8-columnas`. |
| Honorario con factor vigente por fecha e historial. | reuniones de contabilidad | Implementado. `FactorHonorario`. |
| Carga histórica de Agrosoft y de los DTE que se perdieron al cambiar de facturador. | 30/07 y la reunión de QA con GoSocket | No está. No hay importación masiva de asientos. |

## Tesorería

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Cartola por carga, en un rango de fechas. El movimiento del banco no se edita. Cada línea se contabiliza. Pendiente es lo no contabilizado. | 14/09 | Implementado. También acepta CSV y PDF, no solo Excel. |
| Desconciliar sin reversar el mes. | 14/09 | Implementado. `desconciliarMovimiento`. |
| Egresos contra la nómina de la semana. La suma tiene que calzar. Mover la semana no cambia el vencimiento. Ingresos, de a uno. | 14/09 María José; el 23/09 Lupe confirma la asociación masiva de egresos | Parcial. `aplazarNominaLote` solo mueve `semanaCompromiso`. Si la suma no calza, avisa y igual asocia. |
| Pago total, anticipo y anticipo productor. En el productor el tipo de cambio se digita y queda registro. La diferencia se calcula. El monto de la cartola no se toca. | 28/08 y 14/09 | Implementado. `Pago`, `AnticipoProductor`, `PagoTcEvento`. El asiento de banco es `CARTOLA:{id}`. El pago no genera otro asiento. |
| Flujo por concepto y código financiero, en pesos. Apertura que no se borra. Otra vista: saldo de cada banco en cada moneda. | 14/09 | Implementado. `getFlujoCaja`, `esApertura`, `getSaldosBancos`. |
| Estado de cuenta del RUT, aunque sea cliente y proveedor, con antigüedad. Plazos críticos configurables, con atajos de 30 y 90 días. | 24/09 y 23/09 Lupe | Implementado. `getEstadoCuentaPorRut` y `nominaDiasCritico`. |
| Banco en línea. | 14/09 Mario | Diferido por ellos. No hay integración. Hay parsers de archivo (Chile, Santander y otros). |

## Administración

| Pedido vigente | Dónde | En el código |
|---|---|---|
| Cada usuario entra solo a sus empresas. Lo de una no se ve en la otra. Centros de costo y bodegas por empresa. | 21/07 | Implementado. `UsuarioEmpresa` y `assertTenantAccess`. |
| Roles por pantalla, con lectura y escritura separadas. En la revisión se ve el nombre de la persona. | 21/07 y 24/09 | Implementado el permiso por pantalla. El nombre queda en bitácoras puntuales (pagos, vencimiento, proforma), no en un registro único de toda acción. |
| Ingreso con Microsoft, además de usuario y clave. | pedido de usar los mismos correos | Parcial. `loginMicrosoft` existe. Queda prendido con `MICROSOFT_AUTH_ENABLED`, `MICROSOFT_TENANT_ID` y `MICROSOFT_CLIENT_ID`. |
| Fichas separadas de cliente y de proveedor. Al escribir el RUT se copian los datos si ya existe en la otra. Consulta: sociedad, cliente, proveedor o productor. No hay un tercer maestro de productor. El alta la hace jefatura. | 01/10 María José | Parcial. Las fichas, la copia por RUT y el flag `esProductor` están. No hay modelo Productor. Crear cliente o proveedor pide permiso de escritura del módulo, no un perfil de jefatura aparte. |
| Maestros en vigente o anulado, sin borrar la historia. | 01/10 | Parcial. Cliente, proveedor, centro y bodega se inactivan y guardan cambios. Algún maestro, como el presupuesto, sí se borra. |
| Indicadores del Banco Central. Logo y pie por empresa. Listados a Excel. | 10/09 y reuniones de impresión | Parcial. Indicadores y plantilla con logo están. Excel sale en plan, centros y códigos, no en todos los listados. |
| Al entrar, elegir temporada, como en el sistema anterior. | pedido del cambio de temporada | Implementado. Después del login, `AppSettingsProvider` abre el modal de temporada y mes si esa sesión todavía no la confirmó. |
| Maquinaria (uso y prorrateo por cuartel) y gráficos de gerencia (costo por especie, desviación contra presupuesto y contra centro de costo). | 21/07, dicho como algo a futuro | No está. |

## GoSocket

Emitir desde el ERP y recibir folio, PDF y XML está en el cliente de billing-gateway. El 13/10 María José dice que Cristian ya contestó y que el contrato se ve con legal. La inducción a Iofacturo espera esa firma. El plan de pruebas lo estiman para el jueves o el viernes: es un entregable, no una pantalla. Recuperar el historial perdido al salir del facturador anterior no tiene carga en el sistema.

## Lo que no está, en corto

1. Varios archivos de respaldo en la compra y en la venta.
2. Carga manual de una factura de compra con su PDF cuando el XML no llega.
3. Cuartel como mantenedor propio. Predio, temporada, sector y faena ya están, con el código de Diego del 13/10. El cuartel sigue siendo el centro de costo.
4. Asociar la proforma en el libro de compras, eligiendo orden o proforma, sin generar una orden desde Contratistas.
5. Correo automático al contacto cuando la proforma queda aprobada, y una marca de ya enviada.
6. Yuan guardado como tercera columna del asiento. Hoy la pantalla lo muestra y, si la línea no es en yuan, lo calcula al abrir.
7. Guía de despacho con la resolución 154.
8. Cuentas al debe y al haber por tipo de movimiento de bodega, y un cierre de bodega distinto del contable.
9. Seguimiento de cajas por Excel.
10. Borrar una cuenta que no tiene movimientos. Hoy ninguna cuenta se elimina.
11. Devolución a proveedor valorizada al precio de esa factura, limitada a ALM.
12. Plazo de aceptación en 7 días. El código nace en 8 y acepta solo al vencer.
13. Maquinaria y gráficos de gerencia.
14. Carga histórica de Agrosoft y de los DTE perdidos.

Diferido por ellos: banco en línea y contabilidad electrónica al SII. Fuera del código, a la espera del contrato: Iofacturo.
