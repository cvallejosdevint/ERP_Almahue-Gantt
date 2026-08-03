# Minuta tl;dv — Reunión 3 (28/07/2026)

Fuente: https://tldv.io/app/meetings/6a68f05340ebfe00135d54a8  
Video: `fuentes/videos/reunion3-2026-07-28.mp4`  
Origen: `e:\grabaciones\Screen Recording 2026-07-28 120034.mp4`  
Transcripción: [`transcripcion-reunion3.md`](./transcripcion-reunion3.md)

> Archivo histórico. Para planificar el sprint actual usar [`../reunion4-minuta-2026-07-30.md`](../reunion4-minuta-2026-07-30.md) (si chocan, gana Reu4).

## 1. Elementos de Acción

- Equipo de desarrollo implementar vista de roles con listado de usuarios asignados a cada rol 07:48
- Equipo de desarrollo agregar campo de empresa en creación de usuarios para seleccionar acceso 15:21
- Equipo de desarrollo implementar botón de carga masiva en libro comercial y libro de compras 36:58
- Equipo de desarrollo agregar campos de cuenta contable y centro de costo en órdenes de compra 34:04
- Equipo de desarrollo implementar botón de devolución con estados en movimientos de bodega 46:09
- Equipo de desarrollo trasladar plan de cuentas, elementos de costo y códigos financieros a parametrización 53:02
- Equipo de desarrollo agregar selector deslizable de bodegas en módulo de movimientos 45:17
- Equipo de desarrollo implementar selección múltiple de proformas para facturación conjunta 24:42
- Equipo de desarrollo agregar opción de arrastrar columnas en tablas de proformas 24:08
- Equipo de desarrollo implementar aprobación de proformas por supervisor en edición 22:48
- Equipo de desarrollo agregar nombre de aprobador en proformas autorizadas 23:03
- Equipo de desarrollo implementar botones de exportar en formatos Excel y PDF por pantalla 25:35
- Equipo de desarrollo agregar campo de elemento de costo en órdenes de compra 34:18
- Equipo de desarrollo implementar filtro automático de aprobaciones pendientes 35:13
- Equipo de desarrollo agregar botón de editar tipo de cambio en recepciones 39:43
- Equipo de desarrollo implementar vista de previsualización de facturas en registro de compras 40:08
- Equipo de desarrollo agregar botón de seleccionar factura para ver órdenes de compra asociadas 41:18
- Equipo de desarrollo implementar detección de duplicados en carga masiva de libros 37:06
- Equipo de desarrollo crear rol específico para aprobación de proformas 22:04
- Equipo de desarrollo implementar botón de análisis en carga masiva de asientos contables 53:27
- Equipo de desarrollo agregar opción de edición unitaria en carga masiva de asientos 53:52
- Usuario revisar pantallas en columna "En Kua al Mawe" y mover a aprobado o rechazado 57:02
- Usuario enviar feedback de pantallas que requieren exportación en Excel o PDF 26:06
- Usuario enviar plan de cuentas, elementos de costo y centros de costo actualizados 16:34
- Usuario enviar estado de movimiento de bodega para implementación 47:34
- Equipo de desarrollo confirmar disponibilidad del servidor publicado para jueves 56:48

## 2. Gestión de Usuarios y Roles

- Administrador puede cambiar contraseña de usuarios sin visualizarla por seguridad 11:11
- Sistema permite crear roles personalizados con permisos específicos según necesidades 08:22
- Usuarios no pueden tener múltiples roles simultáneamente, se crea rol combinado 09:00
- Cambio de rol de usuario se refleja automáticamente en permisos del panel izquierdo 09:36
- Usuarios pueden cambiar contraseña desde su perfil con opción de administrador 09:53
- Rol específico puede permitir cambio de clave a otros usuarios como permiso granular 10:38

## 3. Módulo de Catálogo y Parametrización

- Unidades de medida contienen campos básicos con estados activo e inactivo 12:58
- Usuarios pueden mostrar u ocultar columnas sin afectar vista de otros usuarios 13:18
- Configuración de columnas se guarda por sesión y usuario en diferentes computadores 13:47
- Centros de costo son transversales a todas las empresas en el sistema 13:59
- Información precargada de centros de costo se carga directamente en base de datos 16:41
- Parametrización incluye centro de costo, plan de cuentas, elementos de costo y tipos de documentos 17:03
- Acceso a catálogo permite solo a usuarios autorizados crear, modificar y eliminar datos 17:40

## 4. Módulo de Contratistas y Proformas

- Ingresos diarios muestran información de proformas con estados facturado o pendiente 18:28
- Modelo de proformas se basa en capturas de AgroSmart de reunión anterior 18:51
- Asociaciones laborales muestran contratista, labor, actividad, monto y estado 19:15
- Proformas en estado definitivo consultan número de factura, fecha e inclusión de otras 20:31
- Proformas en borrador pueden convertirse a definitivas o eliminarse 20:50
- GoSocket es proceso intermediario para gestión de facturas de proveedores 20:21

## 5. Módulo de Ventas

- Libro comercial integra estados y acciones con opción de reversa a borrador 27:47
- Reversa de documento genera advertencia de origen y opción de grabar y contabilizar 27:59
- Libro de venta se carga desde archivo Excel del Servicio de Impuestos Internos 36:06
- Contabilización requiere seleccionar cuenta contable, centro de costos, glosa y cliente 30:06
- Clientes se crean por área contable para evitar falsificación de documentos 31:41
- Vendedor asignado aparece en panel de clientes para identificación 30:54

## 6. Módulo de Compras

- Estados de órdenes de compra incluyen aprobado, emitido, reaccionado, contabilizado y borrador 33:35
- Orden de compra contiene neto e impuesto si aplica 34:46
- Advertencia de aprobaciones pendientes filtra automáticamente órdenes no aprobadas 35:13
- Registro de compras permite carga masiva de facturas con detección de duplicados 37:06
- Carga masiva muestra información extraída antes de confirmar para validación 53:27

## 7. Módulo de Insumos y Bodega

- Maestro de artículos registra cada artículo con familia y datos asociados 42:35
- Artículos se contabilizan a cuenta específica indicada en maestro al centralizar 43:58
- Bodegas contienen código y nombre para identificación en sistema 44:12
- Movimientos de bodega incluyen filtros avanzados por bodega y tipo de movimiento 44:26
- Devolución de proveedor se identifica por tipo de movimiento salida proveedor 46:44
- Devolución genera dos movimientos con tipo específico para control de precio promedio 46:34

## 8. Módulo de Contabilidad

- Plan de cuentas contiene niveles de clasificación y agrupación según parametrización 49:09
- Cuentas contables pueden tener centro de costo agregado o removido según necesidad 49:26
- Asientos contables se cargan masivamente desde documento con análisis previo 53:27
- Reportería se implementará por módulo una vez completada la lógica funcional 54:14

## 9. Configuración del Sistema

- Página web utiliza dirección IP temporal para servidor de prueba, cambiará después 02:45
- Credenciales de acceso usan correo admin@almawe.cl temporal, será real después 02:22
- Modo demo contiene datos visuales sin conexión a base de datos 05:31
- Modo real muestra información conectada a base de datos y funcional 05:42
- Botón de cambio de empresa permite seleccionar período de visualización 14:39
- Usuarios son por empresa, pueden acceder a una o varias empresas 15:13

## 10. Indicadores y Monedas

- Indicadores del Banco Central se sincronizan automáticamente a las 9 de la mañana 51:04
- Cambio de moneda puede realizarse manualmente si sistema externo no está disponible 51:04
- Historial de cambios muestra cuándo fue última sincronización de indicadores 51:04
- Módulo de monedas permite actualización manual independiente de sincronización automática 51:52

## 11. Traspaso Contable y Cierre de Mes

- Traspaso contable centraliza información sin hacer por contratista individual 26:39
- Cierre de mes requiere seleccionar mes y tipo de cambio para centralización 26:51
- Sistema realiza automáticamente reconocimiento de costo versus facturas por recibir 26:59

## 12. Funcionalidades de Interfaz

- Ordenamiento de columnas permite ascendente o descendente por nombre o estado 24:56
- Filtros de estado permiten ver solo facturadas, pendientes u otros estados específicos 24:56
- Paginación configurable muestra 5, 15 o todos los resultados por página 25:24
- Modo oscuro disponible para reducir fatiga visual en pantalla blanca 03:20

## 13. Próximas Reuniones y Cronograma

- Reunión de seguimiento programada para jueves en horario PM a confirmar 56:36
- Objetivo tener funcional todos los módulos antes de agosto, idealmente viernes 29:14
- Próxima reunión incluirá ejecución detallada de todos los módulos con validación 29:20

## Notas manuales

Aún no hay notas manuales
