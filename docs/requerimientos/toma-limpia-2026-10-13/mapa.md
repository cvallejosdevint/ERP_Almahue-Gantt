# Mapa de lo que pidio el cliente

El ERP que describen es el reemplazo de Agrosoft / AlmaWeb para la exportadora y la empresa de servicio, tambien usable por el partner agricola. En la primera reunion lo resumen como un Agrosoft mejorado, sobre todo en contratistas, y sin modulo de mano de obra (liquidan remuneraciones en Buk).

Trabajan varias empresas (Almahue, ALM, Santa Pilar, Los Palos). Un usuario entra solo a las que se le asignan. Lo que se digita en una no se ve en la otra.

## Modulos

| Modulo | Para que lo quieren | Documento que manda |
|---|---|---|
| Compras | Orden de compra, aprobacion, recepcion, libro de compras | Orden de compra |
| Contratistas | Ingreso del dia, proforma, factura del contratista | Proforma, y la factura que la calza |
| Ventas | Orden de venta, stock, factura nacional y de exportacion | Orden de venta, luego el DTE |
| Inventario | Bodega de ALM: insumos, guias, traspasos, devolucion | Guia para entrar material; factura para el gasto |
| Contabilidad | Plan, comprobantes, cierres por modulo | Comprobante en pesos y dolares, y yuan pedido el 01/10 |
| Tesoreria | Cartola, calce, nomina, flujo de caja, estado de cuenta | Movimiento de banco |
| Facturacion | Emitir en el ERP y que GoSocket hable con el SII | DTE (factura, nota de credito, nota de debito, guia) |
| Admin | Empresas, roles por pantalla, ficha de cliente y de proveedor, tipo de cambio | Parametrizacion aparte de la operacion |

Fuera de este mapa, y pedido igual: maquinaria agricola (tractor, pulverizador, prorrateo por cuartel) y graficos cortos de gerencia (costo por especie, desviacion contra presupuesto). No pidieron traer el Power BI de Mario al ERP.

## Evolucion que cambia el pedido

Estas frases chocan. La de la derecha es la mas nueva del cliente.

| Tema | Antes | Quedo |
|---|---|---|
| Cotizacion | 06/08, MJ [40:59]: la cotizacion debe estar en el panel de compras. 30/07: quieren pedir varias y elegir. | 20/08, Lupe [05:48]: a compras solo le piden la orden y ellos solo generan la orden. 23/09 [15:57]: la orden nace digitada y la cotizacion o el presupuesto va de adjunto. |
| A quien se aprueba | 20/08, Lupe [01:43]: la aprobacion es de compras, de servicio y de materiales. | 06/10, MJ [17:39]: el ingreso diario arma proformas y la proforma agrupada pasa por jefatura. La orden de compra sigue con su propia cadena. |
| Donde se pone la cuenta de la venta | 30/07: cuenta y centro de costo en la emision, por linea. | 10/09 [40:13]: se contabiliza desde el libro de ventas, sin volver a digitar el documento. La orden de venta no lleva la cuenta. |
| Area de negocio | 06/08: en cada cuenta se marca si usa area de negocio. | 01/10 [16:23]: no la ocupan ni para gestion. Piden vigente o anulado en los maestros, no borrarlos. |
| Facturador | Julio: GoSocket reemplaza a Acepta y el ideal es emitir en el ERP. | 15/09: MJ sigue frenada por el contrato y por YoFacturo. La carga historica de DTE se hace al final. |
| Banco en linea | Reu2: querian el PDF del banco. | 14/09 [50:33]: la primera puesta en marcha sigue por carga de cartola. El banco en linea queda despues. |
| Contabilidad electronica | 30/07: la suben al hacer la renta, con un contador externo. | La dejan como segunda etapa. Certificarse como software de mercado no es parte de este ERP. |

## Reglas que se repiten y no se cayeron

- Cada empresa ve solo sus centros de costo, bodegas y usuarios.
- La orden de compra no se contabiliza hasta estar aprobada. Si la factura llega antes, se destaca y no se paga.
- Sin reclamo en el plazo, la factura recibida queda aceptada. No hay rechazo automatico. El 14/09 el plazo es 8 dias y el 23/09 es 7. El 01/10 no lo corrigen.
- El neto y el IVA del proveedor pueden tener plazos distintos. Materiales: IVA al mes siguiente y neto a 60 dias. A 30 dias se paga la factura completa.
- No se vende producto nacional bajo el precio de bodega. La exportacion no tiene ese piso.
- El flete es una linea, no un recargo pegado al producto.
- La cartola es el movimiento oficial. No se edita. El flujo de caja sale del codigo financiero, agrupado por concepto.
- La nomina es de pagos. Mover la semana no cambia el vencimiento.
- Un RUT puede ser cliente y proveedor. El estado de cuenta los muestra juntos. Las fichas siguen separadas y, al crear, se copian los datos si el RUT ya existe en la otra.
- El tipo de cambio sale del Banco Central (dolar, y piden euro y yuan). Domingo y feriado se digita. UF, UTM e IPC no entran en la reporteria.
