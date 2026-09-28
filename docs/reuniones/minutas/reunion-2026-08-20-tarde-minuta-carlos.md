# Minuta manual — Carlos Vallejos — 20/08/2026 (tarde)

**Origen:** texto pegado por Carlos el 21/08/2026. No es transcripción verbatim.  
**Sesión:** demo/revisión ERP con Almahue (Lupe, Mario) + Devint (Sergio, Carlos).  
**Transcripción:** [`transcripcion-2026-08-20-tarde-lupe-mario.md`](transcripcion-2026-08-20-tarde-lupe-mario.md)  
**Minuta analizada:** [`../reunion-2026-08-20-tarde-lupe-mario.md`](../reunion-2026-08-20-tarde-lupe-mario.md)

---

## Correcciones módulo aprobaciones y compras

- se debe dejar el sistema de aprobaciones solo para compra (servicios y materiales)
- el documento inicial es una orden de compra
- cuando una OC no está aprobada, en caso que reciban una factura referenciando esta OC, se debe destacar la factura referenciada; aún no se puede contabilizar porque la OC no ha sido aprobada
- aprobar automáticamente en caso de las facturas que hayan pasado 8 días

## Correcciones módulo de tesorería

- se debe reestructurar el orden del dashboard para una manera más lógica (cartola va primero)
- cartolas, ¿cómo queda contabilizado? ya que solo aparece el nombre, más no el RUT del proveedor o cliente (hay que ver la forma de asociar la carga y conciliación bancaria, para los ingresos vs documentos de venta, ¿cómo podemos hacer match entre factura e ingresos? y para las compras vs los egresos?)
- flujo de caja: el saldo se debería poder ver por banco (para saber el monto en caja en cada banco) y debería tener la diferencia en peso y dólar de cada banco. el flujo de caja tiene un saldo inicial, por lo que se debe proponer cómo dejar el saldo inicial
- se debe unificar la vista de anticipos y pagos (solo pagos), por lo que al momento de realizar un movimiento egreso, se debe identificar cuándo es anticipo y cuándo es pago de factura; también debe existir un tercer tipo, que es el anticipo productor, donde la diferenciación es que se manipula el tipo de cambio

## Nóminas

- se trabaja con los vencimientos de los documentos recibidos; esta nómina se trabaja de forma semanal
- también se debe poder retrasar la fecha de vencimiento (como compromiso de pago), pero a nivel interno: no se debe modificar los documentos directamente; debe ser una forma de «aplazar» e identificar (destacar en lista y agregar filtros) las nóminas que se aplazaron, mostrando sus días de vencimiento que han recurrido
- falta tener contadores o visualizadores de indicadores (montos pagados por semana, asignados, atrasados, adelantados, etc.)
