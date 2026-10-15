# Diagramas

Salen de lo que el cliente describio, con la frase mas nueva cuando hubo dos versiones. Las flechas del diagrama son la sintaxis del grafico.

## Compra de materiales y servicios

```mermaid
flowchart TD
  adjunto["Cotizacion o presupuesto adjunto"]
  oc["Orden de compra digitada"]
  cadena["Cadena por monto en pesos"]
  rec["Recepcion o hija parcial"]
  libro["Libro de compras"]
  nomina["Nomina de pago"]
  adjunto --> oc
  oc --> cadena
  cadena -->|aprobada| rec
  cadena -->|rechazada| oc
  rec --> libro
  libro -->|OC aprobada y calce| nomina
  libro -->|OC aun no aprobada| espera["Destacada: no se contabiliza ni se paga"]
```

La orden grande es madre de control. Cada factura parcial abre las lineas y digita solo lo recepcionado. La hija no vuelve a la cadena. Si hay que subir o achicar la madre, la madre si vuelve a aprobacion.

Si el monto de la orden en dolares cambia de tramo, el tipo de cambio del dia la pasa a pesos y se compara en pesos.

## Contratistas (06/10)

```mermaid
flowchart TD
  dia["Ingreso diario: fecha, sector, cuartel, faena, jornal o trato"]
  grupo["Se agrupan ingresos en una proforma"]
  jefe["Aprobacion de jefatura"]
  envio["Se envia al contratista"]
  fac["Factura del contratista, sin parcializar"]
  dia --> grupo --> jefe --> envio
  envio -->|no reclama| fac
  envio -->|reclama precio o jornada| dia
  fac -->|una factura, varias proformas| pago["Contabilizar y pagar"]
```

Una proforma de 9600 no acepta una factura de 5600. Si el contratista reclama, se edita el ingreso de origen y la proforma vuelve a jefatura.

## Venta

```mermaid
flowchart TD
  ov["Orden de venta"]
  stock["Guardar valida stock y piso de precio nacional"]
  emitir["Emitir DTE"]
  gosocket["GoSocket informa al SII"]
  libro["Libro de ventas: cuenta y centro de costo por item"]
  ov --> stock --> emitir --> gosocket --> libro
```

Producto: solo articulos ya creados y bodega. Servicio: sin bodega. Exportacion: tipo de cambio del dia, libre respecto del precio de bodega. La nota de credito o debito de exportacion hereda el tipo de cambio de la factura de origen y nace precargada.

## Tesoreria

```mermaid
flowchart TD
  excel["Cartola Excel del banco"]
  mov["Cada movimiento"]
  egreso["Egresos contra la nomina de la semana"]
  ingreso["Ingresos de clientes, de a uno"]
  flujo["Flujo por concepto y codigo financiero"]
  bancos["Apertura por banco y por moneda"]
  excel --> mov
  mov --> egreso
  mov --> ingreso
  egreso --> flujo
  ingreso --> flujo
  mov --> bancos
```

El saldo de apertura no se borra. El flujo suma bancos y se informa en pesos. La vista por banco muestra la moneda de esa cuenta sin convertirla ahi.

## Lo que no entra en el primer dibujo

El cliente dejo fuera de la primera puesta en marcha el banco en linea, la contabilidad electronica al SII y la carga historica de documentos (al final de la implementacion). Maquinaria y graficos de gerencia los pidieron y no tienen flujo cerrado.
