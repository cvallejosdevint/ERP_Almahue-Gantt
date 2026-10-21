# Reunion cliente 21/10/2026 - MJ, Fran y Lupe

**Tipo:** demo de avances (insumos, libro de guias, compras madre/hija, contratistas, activo fijo, usuarios) y pedidos del cliente sobre esos flujos.
**Fecha:** miercoles 21/10/2026. Grabacion `Screen Recording 2026-10-21 165353.mp4`, 00:53:06. Metadata de creacion 16:00:46 local. El nombre del archivo marca el cierre, ~16:53.
**Cliente en sala (requisito):** Maria Jesus / MJ (ASR: Mari / Marin), Fran, Lupe. Entran ~[07:02].
**No estuvo:** Mario. Carlos dice que Mario avisa que tampoco `[08:50]`. Sergio no esta en sala; Carlos lo nombra para planificar WhatsApp y para manana `[20:07]`, `[52:49]`.
**Devint:** Carlos (demo). Los primeros ~7 min son silencio / espera (VAD).

La transcripcion es ASR local (Whisper large-v3). No atribuye speaker. Los pedidos se marcan cuando MJ/Fran/Lupe corrigen o confirman. Lo que Carlos muestra sin cierre del cliente es hipotesis de implementacion.

| Fuente | Ubicacion |
|---|---|
| Transcripcion ASR | [`../transcripciones/transcripcion-2026-10-21-reunion-cliente.md`](../transcripciones/transcripcion-2026-10-21-reunion-cliente.md) |
| Whisper | `medios/whisper-local/2026-10-21-reunion/` (wav gitignored) |
| Video | `G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 14 - 2026-10-19 a 2026-10-25\2026-10-21 Reunion cliente - MJ, Fran y Lupe\` |

El ASR oye mal algunos nombres: Mari / Marin = MJ. AlmaWebExport / ALM Service = empresas de prueba. Idemorfis = Murphy.

---

## 1. Pedidos del cliente

### Guias de despacho (MJ)

1. Mientras sigan con **Acepta** (abastecimiento opera ahi en dualidad), tiene que existir **ingreso manual** de la guia, no solo lo que llega por GoSocket. `[17:56]`-`[19:12]`.
2. Adjuntar **N archivos** al tipeado (digitalizar el papel) o, como minimo, **subir un Excel** bajado de Acepta. `[18:23]`-`[18:49]`.
3. Pedir al cliente **una guia real de Acepta** para tomar los campos del formulario de ingreso manual. `[18:59]`-`[19:09]`.

### Ordenes madre / hija y facturas (MJ)

4. Las **hijas no quedan con saldo**. Se crean con la recepcion. Al asociarles la factura **mueren / quedan cerradas**. La unica que puede quedar con saldo es la **madre**. `[22:21]`-`[23:15]`.
5. Las hijas tienen que quedar **siempre 100% calzadas** con la facturacion. No hay diferencia ahi. `[28:00]`-`[28:13]`.
6. Las hijas **no se contabilizan en la orden**. Se contabilizan en el **cierre de bodega** (acumulacion mensual, un asiento de centralizacion). `[23:27]`-`[23:45]`, `[27:39]`-`[27:48]`.
7. Hay **dos asientos**: al recepcionar, existencia contra **facturas por recibir**; al calce, se elimina facturas por recibir y se reconoce el proveedor. `[23:49]`-`[24:06]`.

### Activo fijo (MJ)

8. El activo **ingresa directo** en su modulo. **No** nace de una orden de compra. `[30:39]`-`[30:54]`.
9. Va a **cuentas de activo**, no a insumos/bodega. El nexo es la **factura del libro de compras**. `[30:59]`-`[32:14]`.
10. El tipo de documento del alta queda **informativo** (sale de la factura elegida). `[32:47]`-`[32:57]`.
11. **No** se dan de alta activos desde documentos fisicos que no hayan llegado digitales. `[32:57]`-`[33:14]`.
12. **Centro de costo no va** en el alta. `[33:24]`-`[33:38]`.
13. Vida util en **meses**, no con selector de fechas. `[34:15]`-`[34:30]`.
14. **Vida util tributaria = la misma** que la vida util en meses. Sacar el campo duplicado. `[35:06]`-`[36:56]`.
15. Depreciacion **tributaria**. Al cerrar el mes tiene que verse el mes consumido. `[33:57]`-`[37:43]`.
16. **Correccion monetaria por IPC mensual** (indicador). Parametrizar el IPC; evaluar bajarlo automatico del SII. Historial de **valor neto mes a mes**, no de cambios del monto de compra. `[37:59]`-`[40:38]`.
17. En los totalizados, mostrar tambien el **IPC**. El traspaso genera **asiento**. `[40:38]`-`[41:05]`.

### Contratistas y cierre (MJ)

18. Al cierre / centralizacion entran las proformas **aprobadas y con factura**. Las demas (borrador, pendiente, ingresos fuera de proforma) son informativas y no van al asiento. `[41:22]`-`[42:09]`.
19. Cuenta preseleccionada **mano de obra contratista** + glosa editable, a cargo de jefatura. Replicar ese patron de cuenta + glosa en el **cierre de bodega** de insumos. `[42:36]`-`[43:19]`.

### Operacion

20. MJ quiere **crear usuarios en modo real** desde hoy. Carlos acepta y muestra roles, grupos y cadenas. `[44:36]`-`[48:44]`.
21. Montos y nodos de la cadena de aprobacion son **editables** (MJ lo confirma). `[50:48]`-`[51:36]`.
22. **Manana 22/10, 16:00**, misma sala: **tesoreria y contabilidad**. Sergio puede sumarse. `[43:48]`-`[52:49]`.
23. El cliente quiere **planificar** un dia con abastecimiento para un proceso completo, y otro dia de dudas. Carlos lo lleva a Sergio / WhatsApp. `[19:15]`-`[20:25]`.

---

## 2. Lo que Carlos mostro (no es requisito por si solo)

- Estilo visual, bandeja de notificaciones, reglas de aprobacion de **insumos**, familias/subfamilias ligadas a parametrizacion AF. `[09:26]`-`[10:26]`.
- Libro de guias: traer de GoSocket, acuse DTE, asociar a orden de insumo, match / hija / aviso si no calza. El acuse **no se pudo demostrar**: GoSocket lento (Pablo lo habia avisado). Prueba real ALM Service > AlmaWebExport. `[13:56]`-`[16:53]`.
- Columna de documentos asociados navegable (guia > orden > factura). `[20:41]`-`[21:37]`.
- Libro de compras: barra de cobertura en la madre; aviso si los items no calzan. En demo tardo en cargar. `[24:46]`-`[26:57]`.
- Quitar **contabilizar** de las ordenes para dejarlo en el cierre de bodega, segun el punto 6. `[27:39]`.
- Reporteria de contratistas: totalizados plegables, por semana, vista calendario, PDF, plantilla de logo/pie/colores. `[28:17]`-`[29:37]`.
- Maestro AF, traspaso/cierre y reporteria todavia con huecos (cuentas de maquinaria en confirmar traspaso). `[29:37]`-`[38:58]`.
- Limpieza que Carlos se lleva: borrar datos demo, dejar parametrizacion/admin, precargar centros y elementos, un grupo por concepto. `[45:35]`, `[48:52]`-`[50:41]`. Avisar actualizacion de prod. `[44:09]`.

---

## 3. Proximos

- 22/10 16:00: tesoreria + paso a contabilidad.
- Ingreso manual de guias + adjuntos / Excel Acepta mientras dure la dualidad.
- Cierre de bodega con los dos asientos (existencia / facturas por recibir / proveedor).
- Hijas siempre cerradas al 100% al facturar.
- AF: alta desde factura de compras, sin CC, correccion IPC, vida util unica en meses.
- Cuenta + glosa en cierre de bodega, igual que contratistas.
- Usuarios reales: MJ arranca; Carlos limpia demo.
