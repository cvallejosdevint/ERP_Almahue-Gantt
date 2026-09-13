# 2026-07-30 — R4 (demo **ERP nuevo** + Agrosoft tesorería)

- Video: `fuentes/videos/reunion4-2026-07-30.mp4` (**1h33:53**)
- Transcripción: `fuentes/transcripcion-reunion4.md` (desfase documentado **−5:51**; ancla «aceptar invitación» = 00:40)
- Whisper: `fuentes/whisper-local/reu4/` · tl;dv [6a6c199a…](https://tldv.io/app/meetings/6a6c199a423056001311d7a6)
- Meet: **ERP Almahue - Avances**. Carlos comparte `localhost:5173`. **MJ** (requisito). **Sigrid** en lugar de Mario. **Sergio** entra ~min 8 (audio)
- Material MJ del mismo día: `fuentes/mj-compartidos-2026-07-30/` (mayor, diario, inventario, cartola, NC/COMEX)
- Esto es **walkthrough del prototipo** (modo real, julio 2026) + feedback MJ. El tramo tesorería ~69:30 **MJ comparte Agrosoft** (pago proveedores ALM)

Hitos en `hitos/` (reloj = minuto del MP4). El still `13m00-proforma-aprobar` cayó en **login** (cambio de usuario para el flujo Elena); el pedido de «proforma aprobada no se edita» está en audio, no en ese JPEG.

## Sala

| Quién | Rol en esta toma |
|---|---|
| Carlos | Demo ERP local |
| MJ | Cliente / requisito |
| Sigrid | En lugar de Mario (Meet dice Mario) |
| Sergio | Entra a mitad; diseña tenant/CC y DTE |

## 00:00–08:00 — admin: roles, plantilla, reglas

| t | Pantalla | Qué se ve / pide |
|---|---|---|
| 02:50 | Admin › Roles · modal **Editar rol** Administrador | Columna **usuarios del rol** (Admin + `cvallejoss@devint.cl`). Checks lectura/escritura por pantalla (47). Roles: Administrador, Analista, Aprobación proformas, Aprobador OC demo, Compras demo, Contador, Digitador contratistas |
| audio | (mismo módulo) | MJ: el rol **no queda rígido** (borrar / agregar funciones). Al borrar rol con gente: **reasignar** (no dejar sin rol). Carlos: rol temporal **vacaciones digitador** |
| ~04:30 | Plantilla documentos | Logo **por empresa**; pie; si no hay imagen, nombre de empresa. MJ: ¿se puede subir imagen? Sí |
| 05:25 | **Reglas de aprobación** | Copy de esa build: «un solo jefe» al crear OC o pedir proforma. Filas demo: OC estándar, aprobadora proformas. Módulos Comercial / Compras / Contratistas. Rango 0–999.999.999. Jefes: AADMIN, LJEFE, ESUPER |
| 06:50–08:20 | Contratistas › **Ingreso diario** + modal Nuevo ingreso | Fecha 30/07, contratista, **CC/cuartel**, labor, actividad, tipo Jornada. Lista: Servicios Agrícolas del Valle, PENDIENTE |

## 08:00–19:00 — CC por tenant, tarifas, proforma

| t | Pantalla | Feedback MJ / Sergio |
|---|---|---|
| 08:20 | Ingreso diario (modal CC) | MJ: en AlmaWeb **solo CC de esa empresa** (más rígido que Agrosoft; evita imputación cruzada). Dijo «AlmaWeb → CC de Almahue» en el audio: el pedido es **filtrar por empresa activa** |
| 09:40 | Mantenedor CC | Sergio: **no hace falta columna empresa**. Lo que se crea queda del tenant del combo de arriba («Almahue SpA»). Código **`10100` reusable** por tenant; **sin apellido** ALM/AlmaWeb/Santa Pilar |
| 12:20 | Tarifas / labores | Contratista + labor + UM + CC + vigencias |
| 13:00 | **Login** (InPrivate) | Cambio de sesión para mostrar bandeja (no es la grilla de proformas) |
| 14:00 | (reglas / Elena) | Admin puede aprobar «en nombre de» con advertencia (Carlos). **MJ+Sergio: proforma aprobada no se edita**; reversa con **clave**. Hoy la clave es **de perfil** (analista no la ve). Sergio: **clave por usuario** para no rotar una sola clave de todos los supervisores |

## 19:00–28:00 — compras y libro

| t | Pantalla | Feedback |
|---|---|---|
| 19:15 | `catalogos/proveedores` (sidebar Compras también) | Mock: Agro Insumos Sur, Packaging Chile. Menú: OC, Aprobaciones, Recepciones, Libro de compras |
| 20:25 | **Libro de compras** | Una fila `OC-2026-001` / `FACT-FIX30-001-EDIT`, match OK, estado **ANULADO**. Botones Carga masiva + Registrar factura |
| audio | (libro vs OC) | MJ: en el detalle de OC no mezclar borrador/anulada/emitida con el universo de facturas. Sergio: factura **solo a OC aprobadas y recepcionadas**. MJ: **dos procesos** — aprobación = jefe depto (para emitir/hacer el servicio); recepción = conta, **puede ser meses después** (ahí se reconoce el gasto) |

## 23:00–48:00 — libro ventas, emitir, GoSocket, AlmaWeb

| t | Pantalla | Feedback |
|---|---|---|
| 23:00 | `/comercial/libro` pestañas Ventas / Compras / **Despachos** | Folios mock COT/NP/FACTURA; Reversar; **Grabar y contabilizar** en borrador. Sergio: despachos = **movimiento bodega**, no libro ventas. Guías **sí se emiten** |
| 28:50 | mismo libro + toast cadena asientos | NC `NC-5463-REV-*`, estados CONTABILIZADA / ANULADO / BORRADOR + **Emitir DTE**. MJ: libro ventas **no debe tener anulado** ante SII; reversa = solo imputación (CC/cuenta). Folio único (no dos «300»). NC para anular ante el SII |
| audio | Emitir vs libro | MJ duda: ¿facturan en GoSocket o en el ERP? Sergio: **ERP**; GoSocket transparente. Folio lo da GoSocket. Preview PDF **borrador** (botón en folio) → PDF timbrado al grabar. Cuenta + CC **en emisión** (no viajan a GoSocket). Libro = **ya emitido + contabilizado** (cruce SII / huecos de folio) |
| 36:00 | libro otra vez (wizard no en el still) | El JPEG no muestra el wizard; el audio sí (receptor, ítems, CC por línea) |
| 44:10 | **Clientes** (sidebar sigue diciendo GoSocket / DTE) | Smoke + Exportadora Frutas del Sur. MJ: GoSocket comercial **lento**; contrato **Acepta se renueva septiembre**; quieren cambio de facturador **en agosto**. Marcha blanca espejo Agrosoft↔ERP |
| 48:30 | Clientes de nuevo (hito mal rotulado «insumos») | ALM: stock en **Insumos › bodega**. AlmaWeb: cajas = **bodega de paso**, sin stock mes a mes (IVA exportador: archivo compra/cantidad). Producto **inventariable sí/no**. Carga masiva Excel desde AlmaWeb (pendiente MJ) |

## 48:00–62:00 — param, cierre de mes, SII, honorarios

| t | Pantalla | Feedback |
|---|---|---|
| audio | Param vs conta | MJ: indicadores, plan, CC, elementos → **Parametrización**. **Cierre/apertura de mes por módulo** (conta, contratistas, insumos) — no un solo switch. Periodos operativos **no** se esconden en param |
| 53:50 | Contabilidad › **Configuración contable (SII)** | Mapeo BODEGA/CLIENTES/IVA/tipos 33/34/46/61 → cuentas `1-1-…` / `5-1-…`. Carlos: lo inventó el equipo. MJ: en Agrosoft también hay param por módulo; útil. Sergio: si la cuenta va **por línea**, el default por tipo SII aporta poco |
| audio | Honorarios | % retención con **vigencia por periodo** (ej. 15% hasta feb, 17% desde mar) según fecha del asiento |
| audio | Mayor / balance | MJ trabaja **mayor**, poco el diario. Sergio: falta **balance 8 columnas** aparte. MJ manda ejemplos (carpeta `mj-compartidos-2026-07-30`). Contabilidad electrónica = anual (renta), no mensual |

## 62:00–fin — tesorería (ERP mock + Agrosoft)

| t | Pantalla | Feedback |
|---|---|---|
| 62:00 | Tesorería (menú) | Flujo caja vacío; pagos/anticipos mock |
| 65:00 | `/tesoreria/cartolas` | Copy: CSV/Excel (fecha, glosa, monto) y PDF heurístico. Una carga `cartola-julio.xlsx`, Banco Estado 012, **Cerrada**, $980.000, Trabajar |
| audio | (MJ) | Bajar Excel del banco → cargar → **seleccionar movimiento e imputar** (queda calzado). Contabilizar el movimiento de cartola = **contabilizado y conciliado**. Venta/compra dólar. Si hay factura, enlazar. PDF diario del banco lo intentaron y no; se quedan en Excel |
| 69:30 | **Agrosoft 3.0.2** ALM `mjrodriguez` · Tesorería › **Pago a proveedores** | Banco `110102001` Chile $, TRANS, código fin. 3008 SERVICIOS, glosa `PAGO F/27777516 PRUEBA`. Proveedor Alarcón. Facturas tipo 33 (28815) a pagar ~49.900. MJ: n° de **transacción de cartola** (hoy ponen 1 a mano; debería ir p.ej. 5200156) → asiento banco vs proveedor, CLP y USD al TC del día |
| 74:30 / 82:10 | tesorería / cierre Meet | MJ comparte: manual facturación/exportación, inventario AlmaWeb, mayor, balance, diario, Excel cartolas. Anticipos: **ALM da** a productores; **AlmaWeb recibe** de clientes. ALM = packing/MO/PT hacia AlmaWeb; AlmaWeb compra y exporta (**sin inventario ni bodega**). Próximo jueves con Agustín y Mario (vuelven de vacaciones) |

## Qué **no** tratar como requisito cerrado (esta toma)

- Copy de reglas «**un solo jefe**» vs cadena/grupos posteriores (Reu6 / 20/08 / código actual solo OC).
- Libro ventas con **cotizaciones y NP** en el mock: MJ pide libro = emitido SII.
- Menú **GoSocket / DTE** como pantalla de negocio (ya desautorizado en R3).
- Folios `OC-2026-001` / `FACT-FIX30-*` = prototipo.
- Mapeo SII a **CAJA** en el still = basura de demo, no el plan real.
- Hitos `48m30-insumos` y `44m10-gosocket` son la **misma familia de pantalla** (clientes); el audio de insumos/AlmaWeb no coincide con el JPEG.

## Hallazgos visuales

- Demo en **localhost:5173**, no en `45.7.229.46` (R3 sí fue prod IP).
- Toggle **MODO REAL**; periodo julio 2026; empresa Almahue SpA.
- Sidebar **AGROSOFT 3.0** + Contratistas con **Aprobaciones**.
- ~69:30 es la evidencia AS-IS de **pago + n° cartola** en Agrosoft (ALM).
