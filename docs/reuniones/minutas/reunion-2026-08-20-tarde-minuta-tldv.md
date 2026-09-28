# Minuta automática tl;dv — 20/08/2026 (tarde)

**Fuente:** https://tldv.io/app/meetings/6a877e1e644c1a00131f8046  
**Título tl;dv:** Screen Recording 2026-08-20 174935  
**Video origen:** `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-20 174935.mp4`  
**Tamaño:** ~1,12 GB · **Duración aparente:** ~41 min (último timestamp 40:38)  
**MP4:** no versionar (gitignored `fuentes/videos/*.mp4`; esta grabación queda en Videos del usuario, igual que Reu6).  
**Transcripción verbatim:** [`transcripcion-2026-08-20-tarde-lupe-mario.md`](transcripcion-2026-08-20-tarde-lupe-mario.md) (llegó 21/08).  
**Minuta analizada:** [`../reunion-2026-08-20-tarde-lupe-mario.md`](../reunion-2026-08-20-tarde-lupe-mario.md)

> **Quién:** auto-minuta. Mario/Lupe = cliente operativo. No hay Agustín ni María Jesús / MJ. Francisca fue nombrada y no habló.

> **Corrección vs transcripción:** varios action items de tl;dv **sobrecomprometen**. «Aprobador individual» (00:27) lo ofreció Carlos y Mario pidió **probar** primero. «Editar fecha de vencimiento en nómina» (31:35) lo ofreció Carlos y Sergio/Mario/Lupe lo **descartaron** (aplazar compromiso interno, no mutar el DTE). Preferir la minuta analizada.

---

## 1. Elementos de acción

- Carlos implementar opción de seleccionar aprobador individual por usuario dentro eslabón 00:27
- Mario y equipo crear órdenes de compra ficticias para probar flujo aprobaciones 00:48
- Carlos agregar campo referencia cotización en pantalla emisión orden compra 06:35
- Carlos aumentar tamaño pantalla cartolas e implementar buscador 16:29
- Carlos agregar columna y filtro banco en flujo caja 23:57
- Carlos unificar pagos y anticipos con discriminación automática en ingreso 28:18
- Carlos agregar botones acciones para editar fecha vencimiento en nómina 31:35
- Carlos confirmar mañana disponibilidad nueva versión con correcciones 37:16
- Lupe confirmar por WhatsApp cuando error GoSocket esté resuelto 38:16
- Mario y equipo coordinar internamente horarios para reuniones martes y viernes 40:38

## 2. Flujo de aprobaciones

- Aprobación queda a elección del administrador del sistema 00:00
- Sistema permite configurar múltiples grupos con usuarios en más de uno 00:11
- Flujo aprobaciones es flexible pero requiere configuración adicional 00:20
- Aprobación puede ser opcional o restrictiva según configuración cadena 09:34
- Módulo aprobaciones muestra estado y envía notificaciones a aprobadores y emisores 08:34
- Flujo aprobaciones pasa solamente por compras, no por ventas 08:09

## 3. Proceso de compras y cotizaciones

- Documento inicial en flujo compra es orden compra, no cotización 02:57
- Otras áreas solicitan cotización y compras genera orden compra 05:48
- Referencia cotización en orden compra será informativa, no obligatoria 07:35
- Cotizaciones se reciben por correo o formato PDF, no se adjuntan 07:49

## 4. Gestión de facturas y aprobación de órdenes

- Factura sin orden compra aprobada debe destacarse para no contabilizar 11:41
- Factura no aprobada no pasa a pago ni se contabiliza 11:55
- Después 8 días sin aceptación, factura pasa automáticamente a aprobada 13:47
- Sistema registra trazabilidad de aceptación automática después 8 días 13:56

## 5. Módulo tesorería y cartolas

- Cartolas se importan desde Excel con posibilidad seleccionar qué se importa 18:41
- Cartola contiene ingresos, egresos y saldo de cuenta bancaria 25:01
- Importación cartola sirve para conciliación bancaria y flujo caja 25:20
- Saldo flujo caja se carga desde cartola con saldo inicial 24:52

## 6. Conciliación bancaria

- Cartola se usa para conciliación entre ingresos y documentos venta 22:01
- Asociación movimiento banco con factura se hace por monto y cliente 20:19
- Se necesita match entre factura venta y movimiento banco ingreso 22:07

## 7. Gestión de pagos y anticipos

- Pagos se unifican en un solo tipo con discriminación anticipo o total 28:01
- Pago total se asume automático si saldo es 100% de factura 28:23
- Anticipo se asume automático si saldo es inferior a factura 28:35
- Existen 3 tipos movimiento: pago total, anticipo y anticipo productores 29:22

## 8. Nómina de pagos

- Nómina visualiza documentos por semana según fecha vencimiento 30:48
- Nómina es solo visualización, no requiere carga manual de datos 30:53
- Puede editarse fecha pago de factura para moverla a otra semana 35:07
- Nómina muestra indicadores montos pagados, asignados, atrasados y adelantados 36:22
- Nómina es solo de pagos, no incluye recaudación 36:39

## 9. Integración GoSocket

- GoSocket se encarga informar aceptaciones y reclamos al servicio 12:46
- Aceptaciones y reclamos pasarán por integración GoSocket desde ERP 12:46
- Actualmente hay error de CAP o folio no disponible en pruebas 38:19
- Proveedor tiene retraso en entrega de folios para documentos 38:44

## 10. Anticipos y estado de cuenta

- Anticipos se registran en tesorería y visualizan en proveedor o cliente 39:00
- Anticipos se mostrarán en estado de cuenta con vista 360 cliente proveedor 39:15

## 11. Próximas reuniones

- Próxima reunión incluirá a María Jesús para coordinar temas adicionales 40:07
- Se realizarán 2 reuniones semanales los martes y viernes 40:33

## Notas manuales tl;dv

Aún no hay notas manuales.
