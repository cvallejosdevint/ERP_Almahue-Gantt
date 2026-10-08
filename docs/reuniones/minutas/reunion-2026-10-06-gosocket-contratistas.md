# Reunion 06/10/2026 - GoSocket (Pablo) y contratistas (MJ)

**Tipo:** dos bloques en la misma grabacion. Primero GoSocket. Despues, con Pablo ya fuera, el modulo de contratistas.
**Fecha:** martes 06/10/2026. Grabacion `Screen Recording 2026-10-06 124123.mp4`, 00:40:49. Metadata de creacion 12:00 local. El nombre del archivo marca el cierre, ~12:41.
**En sala:** Pablo (GoSocket, sale ~[09:27]), Maria Jesus / MJ (cliente; se le corta la luz ~[34:54]), Carlos (demo), Sergio.
**Nombrados, no en sala:** Cristian (correo del contrato), Diego (va a implementar con la transcripcion; Sergio le arma el flujo de aprobaciones en la tarde, para el jueves).
**No es requisito:** lo que acuerdan Carlos y Sergio despues de que MJ se cae de la llamada. Sirve como hipotesis de implementacion.

| Fuente | Ubicacion |
|---|---|
| Transcripcion ASR | [`../transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md`](../transcripciones/transcripcion-2026-10-06-gosocket-contratistas.md) |
| Whisper | `medios/whisper-local/2026-10-06-reunion/` (wav gitignored) |
| Video | `G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 12 - 2026-10-05 a 2026-10-11\2026-10-06 GoSocket y contratistas - Pablo y MJ\` |

El ASR oye mal varios nombres: Consoque / CUA = GoSocket, controlista = contratista, performa = proforma, AgroCosa = GoSocket.

---

## Hitos

### GoSocket, con Pablo `[01:29]`-`[09:27]`

1. **Guias de despacho recibidas.** Antes de la factura el proveedor puede mandar una guia. Hay que poder bajarla desde el portal o la API de GoSocket y cruzarla con la guia fisica. Pablo confirma que en productivo de otra empresa las guias de despacho si aparecen en recibidos. Prueba pendiente: emitir una guia de una empresa a la otra y verla en recibidos. `[02:30]`-`[05:07]`.
2. **Facturas.** Ya probaron emitidas y recibidas. Corrigieron los duplicados. Pablo no ve un problema de emision y dice que van avanzados. `[05:07]`-`[05:49]`.
3. **Plan de pruebas para la representacion grafica.** Pablo pide una tabla por tipo de documento, con 3 o 4 muestras de cada uno. Cuando esten en GoSocket, el las revisa (rechazo o reparo) y despues, con MJ, la construccion del PDF. La factura 85 del 18/09 tiene un mensaje de error para abrir. `[05:46]`-`[08:49]`.
4. **Contrato e Iofacturo.** MJ mando un correo y Cristian no ha respondido. Pablo va a reenviar ese correo para activar al menos Iofacturo. `[07:52]`-`[09:06]`.

### Contratistas, con MJ `[11:25]`-`[31:00]`

5. **Flujo que MJ trae en un Word**, armado para el area agricola (la exportadora casi no usa contratista). Alta del contratista, registros diarios, sin contrato (en AgroSmart no hace falta; en Agrosoft si; van a una fusion de los dos), proforma, aprobacion, facturacion y pago. `[12:13]`-`[13:03]`.
6. **La proforma agrupa ingresos diarios.** No es una proforma por factura. Puede haber 10 proformas asociadas a una factura. Ejemplo de MJ: 30 ingresos del dia se pueden partir en 2 o 3 proformas. `[13:08]`-`[20:10]`.
7. **Ficha del contratista.** Codigo correlativo (el 11 si ya hay 10). No es el RUT, a diferencia del proveedor. Tambien RUT, nombre, direccion y quien lo creo. `[14:13]`-`[14:48]`.
8. **Ingreso diario: predio opcional.** Agricola lo necesita. ALM no: ahi basta jornal o a trato. El dato queda opcional para las dos empresas, y el funcionamiento tiene que servir si mas adelante hay mas empresas. `[14:51]`-`[16:02]`.
9. **Campos del ingreso.** Fecha, sector, cuartel, faena, forma de pago, unidad, contratista, duracion, valor unitario (trato o jornada), cantidad y total. El trabajador no va. Cuartel y faena con mantenedor, no texto libre. En ALM las labores son puntuales (servicio administrativo, armado de cajas). `[16:06]`-`[17:22]`.
10. **Quien pasa por aprobacion.** MJ dice primero que el ingreso diario, al guardarse, va a jefatura `[18:17]`. Al ver que los montos diarios son chicos y la proforma agrupada puede ser grande, queda que **la proforma** es la que entra al flujo. En la pantalla: se elige el contratista, se marcan N ingresos pendientes, se calcula el total, y esos ingresos dejan de estar disponibles. `[20:50]`-`[24:05]`.
11. **Factura recibida.** En compras, el documento recibido se asocia a una orden de compra o a proformas. La proforma no se factura parcial: el contratista emite por el total de las proformas que se le enviaron. Varias proformas pueden ir en una sola factura. `[24:30]`-`[25:37]`.
12. **Envio al contratista.** La proforma aprobada se le manda (semanal, segun el avance) para que facture. Si no reclama precio o jornada, se da por aceptada. Si hay diferencia, se edita el ingreso diario de origen y la proforma vuelve a pasar por aprobacion. `[25:52]`-`[29:49]`.
13. **Correo al contacto** cuando la proforma ya esta aprobada. Lo pide MJ. `[27:49]`-`[28:02]`.
14. **No reenviar.** Una proforma ya informada al contratista no entra en el envio siguiente del mes. `[28:18]`-`[28:30]`.
15. **Agrupar** los ingresos por rango de fecha o por labor. `[26:33]`-`[26:43]`.

### Despues del corte de luz (Carlos y Sergio; MJ no vuelve)

16. **Estado "notificada a proveedor".** No hace falta que el contratista apruebe dentro del sistema. Con el envio se marca, y solo esas proformas se listan para asociar en compras. `[31:36]`-`[32:08]`.
17. **Traspaso y cierre.** El submodulo que armo Diego podria agrupar proformas por semana o por mes y mostrar estados. El cierre semanal quedo por confirmar con MJ. `[32:41]`-`[34:38]`.
18. **Grupos de aprobacion separados.** Un grupo de proforma no sirve a la vez para orden de compra. Sergio lo deja armado en la tarde para que Diego avance, y le pasan la grabacion. `[36:47]`-`[39:35]`.
