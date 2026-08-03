# Minuta tl;dv — Reunión 4 (30/07/2026)

Fuente: https://tldv.io/app/meetings/6a6c199a423056001311d7a6  
Video: `fuentes/videos/reunion4-2026-07-30.mp4`  
Origen: `e:\grabaciones\Screen Recording 2026-07-30 180246.mp4`  
Minuta canónica: [`../reunion4-minuta-2026-07-30.md`](../reunion4-minuta-2026-07-30.md)  
Transcripción: [`transcripcion-reunion4.md`](./transcripcion-reunion4.md)

## 1. Elementos de Acción

- Carlos agendar reunión para próximo jueves con Agustín y Mario 01:33:31
- María Jesús compartir correo de Agustín en grupo para agenda 01:33:42
- Sergio enviar correo el lunes a GoSocket para confirmar conexión en septiembre 24:08
- María Jesús compartir manual facturación exportación, inventario Excel, libro mayor, balance, diario y cartolas 01:13:45
- María Jesús compartir plan de cuentas en formato Excel para importación 01:32:01
- Equipo desarrollo ajustar formato plan de cuentas para importación 01:32:25
- Equipo desarrollo eliminar columna empresa en mantener centro de costos 09:03
- Equipo desarrollo agregar búsqueda de rol en módulo de roles 02:49
- Equipo desarrollo implementar selector de pantallas en módulo de roles 04:05
- Equipo desarrollo agregar campos cuenta contable y centro costo en detalle ventas 38:14
- Equipo desarrollo eliminar botón emitir documento del libro de ventas 40:24
- Equipo desarrollo agregar opción reenvío PDF y XML en libro de ventas 39:41
- Equipo desarrollo agregar totalizado de facturas en cabecera libro ventas 40:48
- Equipo desarrollo implementar carga masiva Excel para movimientos bodega AlmaWeb 50:40
- Equipo desarrollo mover plan de cuentas a módulo parametrización 52:00
- Equipo desarrollo agregar contador porcentaje en factor honorario 55:19
- Equipo desarrollo agregar balance de ocho columnas en contabilidad 57:15
- Equipo desarrollo implementar carga Excel cartolas bancarias 01:05:10
- Equipo desarrollo agregar edición fecha vencimiento en nóminas por rol 01:22:35
- Equipo desarrollo crear propuesta módulo cobranza con trazabilidad 01:24:32
- Equipo desarrollo agregar resumen saldos conciliados y pendientes 01:26:33
- Equipo desarrollo renombrar cuentas corrientes a estado de cuenta 01:29:47
- Equipo desarrollo agregar filtro pendientes en estado de cuenta 01:30:19
- Equipo desarrollo linkear visualización pago y factura en estado de cuenta 01:30:57
- María Jesús enviar informe movimiento bodega por tipo documento 01:31:51

## 2. Módulo de Administración

- Roles mantienen usuarios asociados con opción cambio directo desde pantalla 02:40
- Sistema previene usuarios sin rol al eliminar rol con advertencia 03:20
- Roles temporales como vacaciones se pueden crear y eliminar automáticamente 04:18
- Planilla documentos permite configurar logo y pie página por empresa 04:40
- Reglas aprobación definen quiénes aprueban proformas y órdenes compra 05:23
- Múltiples aprobadores pueden definirse por módulo con cantidad usuarios 06:01

## 3. Módulo de Contratistas

- Centros costos se filtran por empresa seleccionada en sistema 08:21
- Código centro costo puede reutilizarse en diferentes empresas 10:26
- Servicios Agrícolas Valle es centro costo pendiente con labores asociadas 11:35
- Tarifas configurables incluyen contratista, labor, unidad, centro costo y vigencias 12:10
- Proformas muestran flujo completo con botones aprobar y rechazar 12:30
- Usuario solicita aprobación proforma con estado pendiente de aprobación 12:42
- Proforma aprobada permite edición antes asociar factura 15:32
- Proforma aprobada debe quedar sin edición excepto para asociar factura 16:08
- Reversión aprobación requiere clave por perfil de usuario 16:14
- Cada usuario debe registrar clave individual para reversas y rechazos 17:52

## 4. Módulo de Compras

- Proveedores listados con módulo aprobación similar a contratistas 19:16
- Órdenes compra pueden estar anuladas, aprobadas o emitidas 19:31
- Impresión orden compra muestra detalle parcial y requiere recalcular 19:42
- Libro compras muestra órdenes compra asociadas por factura 20:47
- Órdenes compra enlazadas solo deben ser aprobadas y recepcionadas 21:40
- Aprobación y recepción son procesos distintos en órdenes compra 21:52

## 5. Módulo de Ventas

- Despachos deben quedar solo en movimiento bodega, no libro ventas 23:22
- Empresa emite guía de despacho migrada a módulo inventario 23:51
- GoSocket requiere confirmación de conexión para cambio facturador en agosto 24:29
- Comercial GoSocket ha sido lento en proceso de propuestas 24:53
- Emisión directa GoSocket desde portal será primera etapa 25:13
- Integración GoSocket con sistema requiere dos semanas después documentación 25:59
- Prueba paralela con Agrosoft y nueva plataforma durará dos meses 26:21
- Marcha blanca replicará información en ERP para verificación con Agrosoft 26:28

## 6. Libro de Ventas

- Factura electrónica no se anula sin nota crédito en SII 29:13
- Reversión factura requiere motivo anulación, corrección monto o texto 29:22
- Nota crédito se emite automáticamente con motivo anulación masiva 30:22
- Libro ventas debe quedar siempre contabilizado sin documentos anulados 31:19
- Modificación contable permite cambiar centro costo e imputación 31:33
- Documento nuevo queda en estado borrador antes contabilizar 35:20
- Representación gráfica documento debe mostrar marca agua borrador 36:22
- Folio número documento debe ser botón para abrir representación gráfica 35:47
- Libro ventas debe mostrar solo documentos emitidos y contabilizados 39:36
- Descarga libro ventas disponible como opción en acciones 40:43

## 7. Cotizaciones y Clientes

- Cotizaciones actualmente no se trabajan pero ideal implementarlas 42:17
- Cotizaciones deberían pasar por proceso aprobación departamental 42:12
- Página cotizaciones registra cotizaciones hasta definir flujo 42:43
- Clientes exportación requieren generador RUT de página externa 43:36
- Factura exportación requiere información aduana y país destino 43:52
- Códigos puertos y país destino son estándares SII en XML 44:35
- Nota crédito exportación precargada con datos factura original 45:45
- Nota crédito anulación completa no requiere rellenar datos 45:57
- Nota crédito exportación por corrección monto es más frecuente 46:19
- Todas facturas exportación llevan asociada nota crédito o débito 46:28

## 8. Inventario y Bodega

- Inventario ALM concentra existencias en módulo bodega insumos 48:11
- Inventario AlmaWeb cajas no maneja stock físico, es bodega paso 48:27
- Productos deben marcarse como inventariables o no inventariables 50:27
- Ingreso mercadería inventariable aumenta stock automáticamente 50:32
- Movimientos caja AlmaWeb se cargan desde página externa 50:46
- Nota crédito debe generar reingreso producto a bodega 48:00
- Devolución producto inventariable requiere movimiento bodega registrado 49:35

## 9. Módulo de Contabilidad

- Plan cuentas, indicadores y elementos costo van a parametrización 52:00
- Periodos contables se mantienen en módulo contabilidad 53:35
- Panel SII configurable asocia cuentas por tipo documento 54:08
- Información Banco Central se trae automáticamente al sistema 54:47
- Factor honorario se actualiza hasta llegar retención veinte por ciento 55:10
- Libro diario y mayor incluyen faltantes solicitados por Sergio 56:22
- Libro mayor muestra debe, haber y saldo por cuenta 56:59
- Contabilidad electrónica se sube una vez renta anual 58:34
- Contador externo tributario sube contabilidad electrónica en XML 59:13
- Contabilidad electrónica podría implementarse automáticamente en futuro 59:59
- Certificación contabilidad electrónica requiere trabajo con SII 01:00:27

## 10. Módulo de Tesorería

- Flujo caja carga fecha, concepto ingreso y egreso con cartolas 01:01:46
- Cartola permite contabilización con opción editar o eliminar 01:02:18
- Pagos menú muestra activos y pendientes en tesorería 01:02:31
- Cartola bancaria puede cargarse desde Excel del banco 01:02:52
- Conciliación bancaria enlaza movimientos banco con contabilidad 01:04:00
- Cartola trae cargos y abonos para conciliación completa 01:04:53
- Carga Excel cartolas requiere estructura tipo para procesar 01:05:22
- Banco no envía correo diario, se descarga Excel manualmente 01:05:52
- Procesos diarios proveedores y clientes generan asientos contables 01:07:07
- Pago factura genera asiento banco menos proveedor 01:09:47
- Tipo cambio se trae automático por fecha movimiento banco 01:10:09
- Tipo cambio se puede editar manualmente en tesorería 01:10:19
- Facturas productores tienen tipo cambio promedio diferente 01:12:21
- Facturas materiales requieren tipo cambio diferente al factura 01:12:46

## 11. Nóminas y Cobranza

- Nóminas muestran documentos pendientes con antigüedad histórica 01:18:39
- Fecha vencimiento documento se registra al ingresar factura 01:20:25
- GoSocket entrega documentos recibidos con fecha vencimiento proveedor 01:21:11
- Ochenta por ciento facturas vencen en fecha real 01:21:38
- Facturas productores se pagan después liquidación fruta 01:21:38
- Facturas materiales vencimiento depende negociación encargado bodega 01:21:59
- Encargado tesorería edita fecha vencimiento, otros solo visualizan 01:23:23
- Gestión cobranza actual es arcaica con informe inventario balance 01:23:58
- Proveedores actúan como clientes requiriendo compensación de deudas 01:28:56

## 12. Conciliación y Estado de Cuenta

- Conciliación muestra movimientos banco y contabilidad pendientes 01:26:04
- Conciliación filtra por defecto pendientes a conciliar 01:26:21
- Resumen conciliación muestra cantidad y monto conciliados pendientes 01:26:41
- Estado cuenta muestra saldo detalle por cliente proveedor productor 01:28:49
- Estado cuenta permite buscar RUT con información compras ventas 01:29:57
- Reporte estado cuenta genera Excel e PDF según necesidad 01:31:13

## 13. Estructura Empresarial

- ALM empresa servicios concentra packing materia prima mano obra 01:16:34
- AlmaWeb compra y exporta producto terminado de ALM 01:16:46
- Movimiento bodega ALM concentra stock materiales e insumos 01:17:08
- Stock fruta ALM se maneja en página conectada con packing 01:17:11
- Plan cuentas trabaja con cinco niveles de clasificación 01:32:43

## Notas manuales

Aún no hay notas manuales
