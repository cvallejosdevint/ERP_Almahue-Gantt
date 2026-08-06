# Minuta tl;dv — Reunión 5 (03/08/2026)

Fuente: https://tldv.io/app/meetings/6a71065851275b0013b6f1d9  
Título tl;dv: Screen Recording 2026-08-03 164322  
Video: `fuentes/videos/reunion5-2026-08-03.mp4`  
Origen: `c:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-03 164322.mp4`  
Estado vs código: [`../reunion5-minuta-2026-08-03.md`](../reunion5-minuta-2026-08-03.md)  
Transcripción: [`transcripcion-reunion5.md`](./transcripcion-reunion5.md)

> **Nota:** tl;dv atribuyó los action items a “Sergio implementar…”. En la sala, **Carlos** presenta/implementa y **Sergio** pide/valida. La minuta canónica corrige el “quién”.

## 1. Elementos de Acción

- Sergio implementar confirmación por correo para cambios de PIN sensibles 02:32
- Sergio agregar validación de contraseña de cuenta al cambiar PIN 03:57
- Sergio asociar centro de costo por ítem en órdenes de compra 08:28
- Sergio hacer pantalla de emisión redimensionable y expandible 09:19
- Sergio agregar totalizados al libro de compras 10:35
- Sergio implementar panel lateral colapsable para resumen de documentos 12:08
- Sergio reformular filtros de libros para mejorar estética visual 18:32
- Sergio implementar paginación en vista de periodos para evitar congelamiento 23:59
- Sergio limitar vista de periodos a máximo un año actual 24:23
- Sergio replicar menú de acciones similar al de Better Software 28:18
- Sergio hacer folio en libro de cotizaciones clickeable como botón 29:59
- Sergio agregar filtro de usuario para vista de borradores en admin 32:03
- Sergio agregar historial de apertura y cierre de periodos contables 35:51
- Sergio solicitar motivo al abrir periodos contables cerrados 36:16
- Sergio revisar problema de factura 88001 no reflejada en estado de cuenta 38:45
- Sergio agregar tipo de movimiento en estado de cuenta de clientes 39:35
- Sergio trabajar en módulo de cartolas bancarias 40:36
- Reunirse mañana a la misma hora para revisar ajustes implementados 41:49

## 2. Aprobaciones con PIN

- Sistema de aprobaciones con PIN habilitado por rol de usuario 00:24
- Cada usuario tiene PIN individual que puede cambiar y restablecer 01:07
- Rol ejemplo creado con permiso para aprobar con PIN 01:36
- Usuario demo123 asignado al rol ejemplo para pruebas de aprobación 02:01
- Riesgo de seguridad si usuario deja computador desbloqueado durante ausencia 03:41

## 3. Sistema de Aprobaciones de Documentos

- Proformas y compras funcionan con sistema de aprobación y PIN 07:17
- Solicitante selecciona aprobador de lista de personas con permiso 05:08
- Admin ve todas solicitudes pero recibe advertencia al aprobar por otro 06:14
- Perfil admin permite agilidad sin cambiar de perfil constantemente 06:37

## 4. Órdenes de Compra

- Centro de costo va asociado por ítem en órdenes de compra 08:02
- Visualización de orden de compra muestra detalle con centro de costo 07:29

## 5. Libros Contables

- Libro de compras requiere totalizados como en libro de ventas 10:19
- Resumen de documentos por tipo muestra boletas, facturas y notas 11:43
- Notas de crédito se restan mientras notas de débito se suman 13:27
- Botón de acciones en PDF permite vista preliminar de documento 14:02
- Funcionalidad de envío de correo disponible pero sin servidor conectado 16:42
- Opción de adjuntar archivos asociados al documento implementada 16:50
- Acciones incluyen registrar pago, facturar, imprimir, enviar y anular 17:17
- Filtros de libros funcionan pero necesitan mejora estética visual 18:32

## 6. Libro de Ventas

- Accesos directos entre libros de compra y venta eliminados 19:09
- Opción de guardar como borrador implementada para documentos incompletos 19:30
- Borradores aparecen en menú rápido con leyenda de estado 20:05
- Guardar como borrador actualiza información sin finalizar documento 20:17
- Borradores asociados solo al usuario que los crea 22:06
- Libro de ventas muestra solo documentos contabilizados sin borradores 22:39
- Opción de ver periodos anteriores habilitada para agilidad de búsqueda 22:57
- Vista de periodos múltiples puede congelar navegador con muchos registros 23:46
- Búsqueda avanzada permite filtrar por rango de fechas específico 24:36

## 7. Cotizaciones

- Cotizaciones implementadas con sistema de aprobación como otros módulos 25:34
- Cotizaciones similares a órdenes de compra en estructura 25:42
- Mantención de clientes debe eliminarse del módulo de cotizaciones 25:48
- Botón crear cliente reemplazado por ícono más para formulario modal 26:08
- Mini formulario cliente aparece en panel lateral derecho sin modal superpuesto 26:25
- Campos de cliente incluyen RUT, razón social, dirección, teléfono, correo 26:49
- Cotización convertible a nota de crédito o factura 29:03
- Cotización imprimible con vista preliminar en PDF 29:03

## 8. Emisión de Facturas

- Emisión de factura requiere campos de neto, exento, IVA y descuentos 27:26
- Descuentos y recargos aplicables a nivel global y de línea 27:26
- Campos de factura se replicarán a cotización y órdenes de compra 27:51
- Ventas no incluyen centro de costo a diferencia de compras 28:07
- Facturas recibidas deben incluir centro de costo como compras 28:11

## 9. Parametrización

- Ítems de parametrización reorganizados según solicitud de María 33:07
- Productores duplicado en compras debe eliminarse 33:23

## 10. Contabilidad

- Cambio de período desde contabilidad no funciona correctamente 34:14
- Múltiples períodos pueden estar activos simultáneamente 34:24
- Período activo indica en cuál mes se está trabajando actualmente 34:48
- Cambio de período desde contabilidad no tiene utilidad práctica 35:24
- Trazabilidad requerida para quién abre y cierra períodos contables 35:27
- Configuración contable SAI necesaria para implementar GoSocket 37:20

## 11. Tesorería

- Estado de cuentas muestra detalles de facturas de clientes 38:20
- Filtros de estado de cuenta permiten ver todos o solo pendientes 39:15
- Estado de cuenta de clientes debe mostrar tipo de movimiento 39:35
- Conciliación bancaria muestra solo pendientes con resumen disponible 40:03
- Cartolas bancarias aún no han sido implementadas 40:49

## Notas manual

Aún no hay notas manuales
