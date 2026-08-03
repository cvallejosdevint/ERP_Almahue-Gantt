# Reunión 4 — Minuta y plan accionable (30/07/2026)

**Fecha calendario:** jueves 30/07/2026  
**Próxima demo / PM:** **próximo jueves** (con Agustín y Mario de vuelta)  
**Objetivo:** demo ERP real (modo Demo OFF) + feedback cliente/Sergio sobre módulos admin → tesorería  
**Participantes:** Carlos (Devint), María Jesús (Almahue), Sergio (Devint), Sigrid (por Mario)

| Fuente | Ubicación |
|---|---|
| tl;dv | https://tldv.io/app/meetings/6a6c199a423056001311d7a6 |
| Video local (gitignored) | [`fuentes/videos/reunion4-2026-07-30.mp4`](fuentes/videos/reunion4-2026-07-30.mp4) |
| Video origen | `e:\grabaciones\Screen Recording 2026-07-30 180246.mp4` |
| Minuta cruda tl;dv | [`fuentes/reunion4-minuta-tldv-2026-07-30.md`](fuentes/reunion4-minuta-tldv-2026-07-30.md) |
| Transcripción | [`fuentes/transcripcion-reunion4.md`](fuentes/transcripcion-reunion4.md) |

---

## 1. Resumen ejecutivo

Demo en **modo real** del ERP con módulos conectados. Se recorrió Administración, Contratistas (proformas/aprobación), Compras, Ventas/Libro de ventas, Cotizaciones/Clientes, Bodega, Contabilidad y Tesorería. Quedaron decisiones fuertes de producto (libro ventas = solo emitidos/contabilizados; proforma aprobada sin edición; CC → Estado de cuenta; centros de costo por empresa sin columna empresa) y una lista larga de action items Dev para la reu del próximo jueves.

**GoSocket:** MJ aprieta el lunes; Sergio manda correo. Emisión portal primero; integración ERP ~2 semanas post documentación. Marcha blanca espejo Agrosoft ~2 meses.

---

## 2. Decisiones de producto

| # | Decisión | Implicancia |
|---|---|---|
| D1 | Centros de costo **por empresa seleccionada**; **sin columna empresa** en el mantenedor | Scope por empresa del topbar; código reutilizable entre empresas |
| D2 | Proforma **aprobada**: sin edición ni eliminación; solo **asociar factura**; reversa con clave | Bloquear edit post-aprobación |
| D3 | Clave de reversa/rechazo **por usuario** (no compartida por perfil) | Cada supervisor registra su clave |
| D4 | OC enlazadas a factura: solo **aprobadas y recepcionadas** (procesos distintos) | Filtro en libro compras / asociación |
| D5 | **Despachos / guías** → movimiento bodega / inventario; **no** libro ventas | Libro ventas = documentos tributarios |
| D6 | Libro ventas: solo docs **emitidos y contabilizados**; sin anulados; reversa = modificación **contable** (CC/cuenta) | Acciones: reverso contable + re-contabilizar; NC para anulación SII |
| D7 | Emisión: borrador → grabar/contabilizar emite; folio abre representación gráfica (marca agua borrador) | Cuenta + CC en **detalle de emisión**, no en libro |
| D8 | Quitar botón **Emitir documento** del libro de ventas | Emisión en pantalla dedicada; libro = consulta + descarga + reenvío |
| D9 | Cotizaciones: dejar página de registro hasta definir flujo/aprobación | No bloquear; flujo ideal con aprobación |
| D10 | Productos **inventariable / no**; AlmaWeb = bodega de paso (sin stock físico mes a mes) | NC inventariable → reingreso bodega |
| D11 | Plan cuentas, indicadores, elementos/centros → **Parametrización**; **periodos** quedan en Contabilidad (y cierres por módulo) | Menú + permisos |
| D12 | Panel SII config: conservar para parametrizar cuentas | Útil aunque Agrosoft no lo tenía igual |
| D13 | Contabilidad electrónica / certificación SII = **segunda etapa** | Diferido |
| D14 | Cartola: carga Excel banco → contabilizar = calzar/conciliar; cargos y abonos | Depende Excel tipo de MJ |
| D15 | Edición fecha vencimiento en nóminas: solo rol **encargado tesorería** | Resto solo lectura |
| D16 | Renombrar **Cuentas corrientes → Estado de cuenta** (por RUT; compras+ventas; compensación) | Menú + copy |
| D17 | Plan de cuentas: **5 niveles**; import ajustar al Excel del cliente | Importación |

---

## 3. Action items — Externos (no Dev)

| Quién | Acción | ts |
|---|---|---|
| Carlos | Agendar reu próximo jueves con Agustín y Mario | 01:33:31 |
| María Jesús | Compartir correo de Agustín en el grupo | 01:33:42 |
| Sergio | Correo lunes a GoSocket (conexión septiembre / cambio agosto) | 24:08 |
| María Jesús | Compartir: manual facturación exportación, inventario Excel AlmaWeb, libro mayor, balance, diario, cartolas | 01:13:45 |
| María Jesús | Plan de cuentas Excel para importación | 01:32:01 |
| María Jesús | Informe movimiento bodega por tipo documento | 01:31:51 |

---

## 4. Action items — Dev (R4-XX)

| ID | Acción | Módulo / ruta | ts | Prioridad |
|---|---|---|---|---|
| R4-01 | Búsqueda de rol en módulo Roles | `/admin/roles` | 02:49 | Jueves |
| R4-02 | Selector de pantallas en Roles (parcial/completo por módulo) | `/admin/roles` | 04:05 | Jueves |
| R4-03 | Eliminar columna empresa en mantenedor centros de costo | `/catalogos/centros-costo` | 09:03 | Jueves |
| R4-04 | Proforma aprobada: bloquear edición; solo asociar factura; reversa con clave por usuario | `/contratistas/proformas` | 16:08 | Jueves |
| R4-05 | Libro compras: OC asociadas solo aprobadas + recepcionadas | `/compras/registro` | 21:40 | Jueves |
| R4-06 | Cuenta contable + centro costo en **detalle** emisión ventas | Emitir documento | 38:14 | Jueves |
| R4-07 | Eliminar botón Emitir documento del libro de ventas | `/comercial/libro` | 40:24 | Jueves |
| R4-08 | Reenvío PDF/XML desde libro de ventas | Libro ventas | 39:41 | Post / con GoSocket |
| R4-09 | Totalizado cabecera libro ventas (tipo RCV SII) | Libro ventas | 40:48 | Jueves |
| R4-10 | Folio → representación gráfica (+ marca agua borrador) | Emisión / libro | 35:47 | Post |
| R4-11 | Carga masiva Excel movimientos bodega AlmaWeb | `/insumos/movimientos` | 50:40 | Depende Excel MJ |
| R4-12 | Flag inventariable + stock automático / reingreso por NC | Insumos | 50:27 | Post |
| R4-13 | Mover plan de cuentas (y afines) a Parametrización | Sidebar / catálogos | 52:00 | Jueves |
| R4-14 | Factor honorario: historial % / vigencia por periodo | Contabilidad / indicadores | 55:19 | Post |
| R4-15 | Menú **Balance de 8 columnas** | Contabilidad › Reportes | 57:15 | Jueves |
| R4-16 | Carga Excel cartolas bancarias (estructura tipo) | `/tesoreria/cartolas` | 01:05:10 | Depende Excel MJ |
| R4-17 | Edición fecha vencimiento en nóminas por rol tesorería | `/tesoreria/nominas` | 01:22:35 | Jueves |
| R4-18 | Propuesta módulo cobranza con trazabilidad (compromisos, mail, tracking) | Tesorería / nuevo | 01:24:32 | Propuesta (no código) |
| R4-19 | Conciliación: default pendientes + resumen cantidad/monto conciliados vs pendientes | `/tesoreria/conciliacion` | 01:26:33 | Jueves |
| R4-20 | Renombrar Cuentas corrientes → **Estado de cuenta** | Sidebar + página | 01:29:47 | Jueves |
| R4-21 | Filtro Todos / Pendientes en estado de cuenta | Estado de cuenta | 01:30:19 | Jueves |
| R4-22 | Linkear visualización pago y factura desde estado de cuenta | Estado de cuenta | 01:30:57 | Jueves |
| R4-23 | Ajustar import plan de cuentas al formato Excel cliente (5 niveles) | Plan cuentas | 01:32:25 | Depende Excel |
| R4-24 | Impresión OC: recalcular / detalle completo | `/compras/ordenes` | 19:42 | Post |
| R4-25 | Mantenedor códigos financieros (flujo caja) — gap visto en Agrosoft | Tesorería / Param | 11:25 | Post |

---

## 5. Temas por módulo (síntesis)

### Administración
Roles con usuarios asociados + salto a usuarios; eliminación con reasignación obligatoria; roles temporales; plantilla documentos (logo/pie); reglas de aprobación multi-módulo.

### Contratistas
CC filtrados por empresa; tarifas (contratista/labor/unidad/CC/vigencia); proformas con solicitar/aprobar/rechazar y aprobación cruzada con advertencia; inbox/notificaciones.

### Compras
Proveedores + aprobación OC; estados anulado/aprobado/emitido; libro compras por factura; aprobación ≠ recepción.

### Ventas / Libro ventas
Sin despachos en libro; GoSocket timeline; emisión desde ERP (transparente a GoSocket); libro = emitidos/contabilizados; reenvío PDF/XML; totalizado; descarga libro.

### Cotizaciones / Clientes
Cotizaciones en registro hasta flujo; clientes exportación (RUT externo) + aduana/país/puertos SII; NC exportación precargada (corrección monto frecuente).

### Bodega
ALM = stock materiales; AlmaWeb = paso; inventariable; carga Excel cajas; NC → reingreso.

### Contabilidad
Param vs periodos; config SII; BC + factores honorario; diario/mayor; balance 8 col; contabilidad electrónica diferida.

### Tesorería
Flujo caja, cartolas, pagos, anticipos (ALM da a productores / AlmaWeb recibe de clientes); nóminas aging; conciliación; estado de cuenta.

### Estructura
ALM = packing/MP/MO → producto a AlmaWeb; stock fruta packing aparte.

---

## 6. Materiales pendientes cliente (MJ)

1. Manual facturación exportación  
2. Inventario Excel AlmaWeb  
3. Libro mayor / balance / libro diario (ejemplos)  
4. Excel cartolas bancarias (+ ejemplo calce vs factura/asiento)  
5. Plan de cuentas Excel (5 niveles)  
6. Informe movimiento bodega por tipo documento  

---

## 7. Slice sugerido próximo jueves

1. R4-03, R4-01/02 (CC + roles)  
2. R4-04 (proforma lock)  
3. R4-06, R4-07, R4-09 (ventas)  
4. R4-13, R4-15 (param + balance)  
5. R4-17, R4-19, R4-20–22 (tesorería UI)  
6. R4-18 como **documento propuesta** (no feature completa)  
7. R4-11 / R4-16 / R4-23 cuando lleguen Excels  

**Diferir:** GoSocket keys/integración, R4-08/10 sin PDF real, contabilidad electrónica, cobranza full.
