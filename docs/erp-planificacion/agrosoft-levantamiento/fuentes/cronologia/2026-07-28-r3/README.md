# 2026-07-28 — R3 (demo **ERP nuevo**, no Agrosoft)

- Video: `fuentes/videos/reunion3-2026-07-28.mp4` (~1,7 GB, **57:48**)
- Transcripción: `fuentes/transcripcion-reunion3.md` (reloj ×10) · Whisper: `whisper-local/reu3/`
- Meet: **ERP Almahue - Avances**. Carlos presenta; **MJ** en sala (requisito)
- URL demo: `http://45.7.229.46/almahue-erp` (mismo host que Freshlink: **no** entrar solo la IP)
- Esto es **walkthrough del prototipo** + feedback MJ. No es AS-IS Agrosoft (eso fue R1–R2)

## 00:00–05:00 — Trello + login

| t | Pantalla | Qué se ve / pide |
|---|---|---|
| 00:20 | Trello **Almahue ERP** 28/07 11:03 | Columnas: En desarrollo / En QA Devint / **En QA Almahue** / Rechazado / Aprobado. Cards R1 (21/07) y R2 (23/07). Rechazados: Roles, Monedas, Tipos de documento |
| 02:40–03:40 | Credenciales en Trello → login → **panel operativo** `45.7.229.46` | Toggle **MODO REAL** vs **MODO DEMO**. Admin, periodo T 2026 / julio, empresa Almahue SpA. KPIs en 0; proformas mock en el panel |
| 05:00 | Dark mode + «AGROSOFT 3.0» en sidebar | Admin «completo»; catálogo y contratistas a medias. Demo = relleno; Real = BD |

MJ: en movimientos quiere **nombre de persona**, no el cargo.

## 05:30–16:00 — admin, usuarios, catálogo

| t | Pantalla | Feedback MJ |
|---|---|---|
| 05:40 | **Contratistas › Listado** (modo real): 3 RUTs mock, especialidad, vigencia | Listado «listo» |
| 07:20 | **Admin › Usuarios** + modal: Carlos, roles Admin / Analista / Contador / **Digitador contratistas** | Un usuario = **un rol**. Si hace falta mezclar, se crea un rol nuevo. Contraseña: cada uno cambia la suya; admin **resetea** sin verla |
| 13:20 | Catálogo UM: ocultar columnas por usuario | Preferencia de columnas **por usuario**, no por empresa |
| 14:31 | Cambio empresa + periodo | **Usuarios por empresa** (uno o varios). Check de empresas en el alta |
| 16:40 | Centros de costo (demo, Almahue Logística): ADM/PACK/CAMPO/LOG/FIN | MJ mandó **listado Excel** para precargar. Catálogo = **parametrización** (CC, plan de cuentas, elementos, tipos doc/ref, códigos financieros). Quien tiene catálogo es el único que crea/edita; el resto no ve param |

## 18:00–28:00 — contratistas (copia AgroSmart)

| t | Pantalla | Feedback MJ |
|---|---|---|
| 19:20 | **Asociación labores → proforma/factura**: check, monto $152.000, calce, labores uva/ciruela | Modelo de R2 AgroSmart. GoSocket: elegir facturas **del proveedor**. Definitiva pide nro/fecha factura + otras proformas. Borrador → definitiva. Editar trabajo/proforma = **aprobación supervisor**; re-editar = otra autorización; guardar **quién aprobó** |
| 23:30 | (lista proformas) | **Varias proformas → una factura** (check + acciones masivas). Filtro facturada/pendiente |
| 27:00 | **Traspaso y cierre**: $ facturas por recibir vs costo MO; tasas CLP/USD/CNY/EUR; notepad de Carlos | MJ: **no es por contratista**. Solo mes + tipo de cambio y centraliza costo vs facturas por recibir. Notepad 27/07: mismos puntos |

## 28:00–42:00 — ventas, clientes, compras

| t | Pantalla | Feedback MJ |
|---|---|---|
| 28:20 | **Ventas › Libro comercial**: folios COT/NC/FAC, estados, **Grabar y contabilizar** / Reversar, cadena 473/474 | **Renombrar a Libro de ventas**. Contabilizar de verdad = cuenta + CC + glosa + cliente. Nutrición: **Excel SII** (carga 1–7 y luego 1–14 **sin duplicar**). NC/ND/factura. GoSocket es **consulta**, no panel admin (malentendido del equipo) |
| 31:20 | Clientes (vendedor asignado) | Crea **conta**, no el vendedor (control / no falsificar). Campos: giro, RS, RUT, dirección. No hay módulo vendedores; el «creador» = usuario del sistema |
| 33:40 | **Compras › OC**: OC-2026-104… estados APROBADO/EMITIDO/RECEPCIONADA/CONTABILIZADA/BORRADOR; AFECTO/EXENTO/MIXTO | Falta **cuenta, CC, elemento**. Neto + impuesto. Advertencia de pendientes debe **filtrar no aprobadas**. Libro de compras (no «comercial») |
| 40:30 | Registro facturas | Carga masiva: factura → **OCs de ese RUT**; en la fila «factura 77 / OC 4» |

## 42:00–fin — insumos, conta, indicadores

| t | Pantalla | Feedback MJ |
|---|---|---|
| 42:30 | **Maestro artículos**: familias agroquímico/envase, **stock y costo promedio** visibles | Maestro = creación. **Ni stock ni costo promedio** acá. Sí: **cuenta** al centralizar (ej. bolsas → costo materiales embalaje). Stock en bodegas |
| audio ~45 | Movimientos | Filtro **por bodega** (no solo por movimiento). Devolución = tipo **salida proveedor** + TC específico (R2: no a promedio). MJ manda tipos de movimiento |
| ~48 | Plan de cuentas (mock) | Excel real: **niveles** clasificación vs agrupación; flags CC/elemento por cuenta (on/off) |
| ~52 | Indicadores BC | Sync 9:00 + **manual** si el BC cae + historial. Param (plan, elementos, factores, códigos fin.) **en catálogo**; los módulos solo aplican |
| 55+ | Trello de nuevo | MJ entra al sitio. Queda **jueves PM** (R4 30/07). Tarea: QA columna Almahue (aprobar / rechazar = falta ajuste) |

## Qué **no** tratar como requisito cerrado

- Menú **GoSocket / DTE** como CRUD: Carlos lo desautoriza en esta misma reunión.
- Libro comercial con **cotizaciones** en el mock: MJ pide libro de **venta** (factura/NC/ND) alimentado por SII.
- Un usuario = un rol: es diseño de esa fecha; contrastar código actual (`*` / AdminConcepto).
- Folios `OC-2026-NNN` en el mock vs folio numérico Agrosoft (5207) de R1.

## Hallazgos visuales

- Host ya es **prod IP** `45.7.229.46` el 28/07 (muestra).
- Toggle **MODO REAL / DEMO** ya en UI.
- Sidebar etiqueta **AGROSOFT 3.0**.
- Notepad `reunion sergio 27-07.txt` (interna previa): roles×empresa, param en catálogo, multi-proforma, cierre centralizado.
