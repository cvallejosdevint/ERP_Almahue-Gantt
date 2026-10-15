# Mapa de las transcripciones contra el software

Fecha: 13/10/2026, después de las migraciones de contratistas. El pedido sale de las transcripciones. Si dos frases chocan, queda la más nueva. El Word de contratistas y el deck de Mario entran solo donde la sala no los corrigió.

Marca de cada tramo:

| Marca | Significado |
|---|---|
| Conectado | El módulo que sigue lee el dato que el anterior guardó. Hay prueba en verde o un lector en el fuente. |
| Parcial | El dato viaja, pero no por el camino o con el campo que el cliente cerró. |
| Deuda | El cliente lo pidió y el siguiente módulo no lo recibe, o el software hace el paso al revés. |

No está limpio. Hay tramos conectados y quedan deudas entre contratistas, compras, insumos y tesorería.

## El recorrido que el cliente cerró

1. Contratistas. Ingreso, proforma, jefatura. Al cerrar el mes, costo contra facturas por recibir, aunque la factura no esté asociada. La cuenta de costo se elige solo ahí.
2. Compras. El libro recibe el DTE. Se elige una orden aprobada o una proforma aprobada. No nace otra orden. Al calzar la proforma, facturas por recibir contra el nombre del contratista. Una factura de una orden sin aprobar se destaca y no se contabiliza ni se paga.
3. Insumos. La guía mueve la bodega. La recepción de la orden no. La factura de fin de mes se asocia a la orden. El promedio es informativo.
4. Ventas. Guardar valida stock y deja la orden confirmada. Facturar es otro paso. La cuenta se asigna al contabilizar el libro. El asiento entra al mayor.
5. Tesorería. La factura ya contabilizada entra a la nómina. Los egresos de la cartola calzan con esa nómina y la suma tiene que coincidir. El asiento de banco es el de la cartola. El flujo se informa en pesos.

## Qué hace el software en cada módulo

### Compras

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| La orden es el documento. La cotización es tipo, folio y fecha. | Lo guarda en la orden. Las rutas de cotizaciones redirigen a órdenes. | Conectado consigo mismo. |
| Varios archivos en la compra y en la venta (24/09). | No hay campo de archivos. El wizard dice que no se adjunta. | Deuda. El archivo no llega a ningún módulo. |
| Cadena por monto en pesos. Rechazo con motivo, mismo documento. | Lo hace. Tests en verde, incluido un monto en dólares convertido. | Conectado: la orden escribe `AprobacionOc` y la bandeja lo lee. |
| Factura de una orden sin aprobar: se destaca, no se contabiliza ni se paga. | Se asocia y marca `ocNoAprobada`. Contabilizar un borrador se rechaza. | Conectado con contabilidad en ese gate. El pago, en el fuente, mira el mismo estado. Ese `it` de tesorería no corrió. |
| Plazo de aceptación: 8 días el 14/09, 7 el 23/09. | El default es 8. Un cron pasa a aceptada al vencer. | Parcial. Nadie volvió a fijar el 7. |
| Madre solo de insumos, hija sin nueva aprobación, madre invisible fuera de insumos (01/10). | La hija nace en borrador. La madre sigue en el listado y, al cerrar saldo, vuelve a aprobación. No filtra por insumos. | Deuda con insumos y con el listado de compras. |
| Neto e IVA con plazos distintos. Tipo de cambio guardado para calzar dólares o yuanes. | El IVA a día 10 está en el proveedor. La orden y el aging usan solo los días del neto. La orden no guarda tipo de cambio. | Parcial hacia tesorería: viaja un solo vencimiento. |
| Carga manual con PDF. | El alta manual no recibe archivo. El PDF se baja de GoSocket. | Deuda. |
| En el libro se elige orden o proforma (13/10). | El libro solo elige órdenes. | Deuda. Ver el tramo de contratistas. |

### Contratistas

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| Sin contrato. Ficha con código distinto del RUT. | No hay contrato. El código es `CTR-` más un correlativo. | Conectado en la ficha. |
| Ingreso con predio opcional, sector, faena y cuartel de mantenedor. | Predio, temporada, sector y faena existen. El cuartel obligatorio es el centro de costo. | Parcial. Ningún test afirma que el ingreso guarde predio, sector o faena. |
| La proforma, no cada fila, pasa por jefatura. | Hay cadena. Si el monto no llega al primer piso, queda definitiva sin aprobador. Test en verde. | Deuda contra lo que ella dijo el 6/10. |
| Una factura calza varias proformas. No se parcializa. No hay proforma hija. | Varias proformas suman el neto y, si no calza, rechaza. Test en verde. | Conectado entre proformas. |
| Cierre de mes: costo contra facturas por recibir, aunque no haya factura. | `traspasoCierre` lo arma. Test en verde con una proforma definitiva y sin factura. El asiento queda en el periodo. | Conectado con contabilidad. |
| Corregir vuelve al ingreso y a jefatura. | Reversar deja la proforma en borrador. El ingreso sigue asociado. Test en verde, y no toca el ingreso. | Deuda interna del módulo. |
| Asociación del DTE en compras, solo proformas aprobadas (13/10). | La asociación está en contratistas y exige `ENVIADA_CONTRATISTA`. Sin registro de compra crea una orden. Test en verde: neto 150, una orden, dos proformas facturadas. | Deuda. El camino real es contratistas > orden > compras. |
| Al calzar: facturas por recibir contra el nombre del contratista. | Si esa orden se contabiliza, compras lee la proforma ligada y arma debe «Facturas por recibir contratistas» y haber «Proveedores». | Parcial. Compras sí lee la proforma, pero solo porque la orden ya trae `referenciaTipo: PROFORMA_CONTRATISTA`. El haber no es el nombre del contratista. |

### Ventas

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| Guardar valida stock y deja la orden confirmada. Facturar va en Emitir. Sin cadena. | Lo hace. Tests en verde. | Conectado con insumos: confirma y crea `SALIDA_VENTA`. El test no afirma bodega ni cantidad. |
| Nacional no vende bajo el precio de bodega. Exportación sin ese piso. | Tests en verde. | Conectado con el maestro de insumos (`precioCompra` o `costoPromedio`). |
| Cuenta y centro al contabilizar el libro, no en la orden. | El asiento de la venta sí los toma de la línea. Test en verde, con IVA débito. Otro test en verde también los escribe en la orden confirmada. | Parcial. Contabilidad los recibe. La orden no debería guardarlos. |
| Folio, PDF y XML en el ERP. | El folio se guarda en el documento. El PDF se pide al gateway. | Conectado con billing-gateway. |
| Guía de despacho. Resolución 154, pendiente en la sala del 13/10. | Se emite guía. No hay campos de la 154. | Deuda de campos, no de emisión. |

### Inventario

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| La guía mueve stock. La recepción de la orden no. | La recepción escribe `recepcionOc` y puede dejar la orden recepcionada. No llama a stock. Test en verde. La guía, en el fuente, llama a `ENTRADA_PROVEEDOR`. | Parcial. Compras y bodega no comparten el mismo acto. El camino feliz de la guía no tiene spec. |
| El promedio es informativo. El movimiento vale el precio de la orden. | Confirmar una entrada recalcula `costoPromedio`. Test en verde. La guía usa el precio del maestro, no el de la orden. | Deuda. Insumos no lee el precio de la orden de entrada. |
| Devolución a proveedor solo en ALM, al precio de esa factura. | Mira un flag de la empresa y el precio del movimiento. | Deuda. No lee la factura ni fija ALM. |
| Cuenta al debe y al haber por tipo de movimiento. Cierre de bodega. Excel de cajas. | No están. | Deuda. Esos movimientos no llegan a contabilidad por ese camino. |

### Contabilidad

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| Asiento de venta y de compra visibles en el mayor. | Los dos llaman a `createAsiento`. El mayor lee la tabla `Asiento`. | Parcial. No hay un test que meta un origen `COMPRA:` o `DOC:` en el mayor. |
| Pesos, dólar y yuan en el comprobante. Auxiliar = RUT sin dígito. Glosa con el número de factura. | La vista muestra las tres columnas. La venta escribe el auxiliar. La glosa de venta en verde no lleva el folio. La compra no escribe auxiliar y sus líneas dicen «Proveedores». | Parcial hacia el comprobante. |
| Cuenta sin movimientos se puede borrar. Con movimientos, se inactiva. | `deleteCuenta` rechaza siempre. Test en verde, con el impacto en cero. | Deuda contra el 01/10. |
| Cierre por módulo. | Hay cierre contable y traspaso de contratistas. No hay cierre de insumos. | Parcial. |

### Tesorería

| Pedido vigente | El software hoy | Con quién habla |
|---|---|---|
| Cartola por carga. Cada línea se contabiliza. Desconciliar no reversa el mes. | Tests en verde. El asiento nace con origen `CARTOLA:`. | Conectado con contabilidad. |
| Mover la semana no cambia el vencimiento. Ingresos de a uno. | Tests en verde. | Conectado con el aging del documento. |
| Egresos que calzan en monto con la nómina. | Avisa si no calza y asocia igual. | Deuda. El dato viaja aunque la suma no cierre. |
| Pago total, anticipo y anticipo productor, con tipo de cambio registrado. El pago no crea asiento. | El pago `ANTICIPO_PRODUCTOR` y su evento de tipo de cambio están en verde. `createPago` no crea asiento. | Conectado con la cartola. |
| La pantalla de anticipos productores. | Lee la tabla `anticipoProductor`. El alta de esa tabla responde 400. El anticipo real está en `Pago`. | Deuda. La pantalla y el pago no se hablan. |
| Flujo en pesos, sumando bancos. Saldos por banco y moneda sin convertir. | El test del flujo deja el dólar en 50, sin pasarlo a pesos. | Deuda del informe en pesos. El agrupamiento por concepto sí está. |
| Estado de cuenta del RUT, cliente y proveedor a la vez. | Test en verde con un pago total. | Conectado. El anticipo de esa vista lee la tabla que nadie escribe. |
| Banco en línea. | No hay integración. | No es deuda. Ellos lo dejaron para después. |

### Administración y GoSocket

Empresas separadas, roles por pantalla, fichas de cliente y proveedor que se copian por RUT, indicadores del Banco Central y temporada al entrar están en el software. El ingreso con Microsoft existe y queda prendido solo si hay tenant y client id. Maquinaria y gráficos de gerencia no están.

Emitir y bajar PDF/XML habla con billing-gateway. Iofacturo espera el contrato. Los 10 tests de sincronizar y aceptar compras contra GoSocket están en rojo por el mock, no porque se haya llamado al partner. Ese tramo no queda demostrado.

## Comunicación entre módulos

| De | A | Qué debería viajar | Qué viaja hoy |
|---|---|---|---|
| Contratistas | Contabilidad | Costo contra facturas por recibir al cerrar el mes | Conectado. Test en verde. |
| Contratistas | Compras | Proformas aprobadas para elegirlas en el libro, sin crear orden | Deuda. Contratistas crea la orden. Compras no lista proformas. |
| Compras | Contratistas | Al contabilizar esa orden, leer la cuenta de facturas por recibir | Parcial. Sí lee la proforma ligada a la orden y usa esa cuenta al debe. El haber es «Proveedores». |
| Compras | Contabilidad | Asiento por líneas, neto e IVA | Parcial. Viaja un asiento de neto contra proveedores. |
| Compras | Tesorería | Documento contabilizado, dos vencimientos, y no pagar si la orden no está aprobada | Parcial. Viaja un vencimiento. El gate de no contabilizar borrador está en verde. |
| Compras | Insumos | La recepción no mueve stock. La guía sí, al precio de la orden | Parcial. La recepción no mueve stock. La guía no lee el precio de la orden. |
| Insumos | Ventas | Stock por bodega para poder confirmar | Conectado. Confirmar crea la salida. |
| Ventas | Contabilidad | Cuenta y centro por ítem, IVA débito | Conectado. Tests en verde. |
| Ventas | Billing | Folio, PDF, XML | Conectado en folio y descarga. |
| Tesorería | Contabilidad | Asiento de la cartola, no uno por pago | Conectado. Tests en verde. |
| Tesorería | Pantalla de anticipos | El mismo anticipo productor | Deuda. Pantalla y pago usan tablas distintas. |

## Deudas que siguen abiertas

1. La proforma no se elige en el libro de compras. Se convierte en orden desde contratistas, y solo si ya fue notificada.
2. Al contabilizar esa compra, el haber no queda a nombre del contratista.
3. Reversar la proforma no devuelve el ingreso.
4. La proforma de monto bajo se aprueba sola.
5. La orden madre sigue visible y la hija nace en borrador, sin corte de insumos.
6. Un solo vencimiento. Sin archivos. Sin PDF de carga manual. Plazo de aceptación en 8, no en 7.
7. El promedio de bodega se recalcula. La devolución no sale al precio de la factura.
8. La cuenta se puede escribir en la orden de venta. Una cuenta vacía no se puede borrar.
9. La nómina asocia aunque la suma no calce. El flujo no pasa todo a pesos.
10. La pantalla de anticipos productores no escribe lo que lee.

Cerrado por ellos, no como deuda de esta pasada: banco en línea y contabilidad electrónica al SII.
