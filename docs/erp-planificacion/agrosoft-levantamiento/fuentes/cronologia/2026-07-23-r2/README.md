# 2026-07-23 — R2 (Agrosoft contratistas + AgroSmart + ventas + tesorería)

- Video: `fuentes/videos/reunion2-2026-07-23.mp4` (~2,6 GB, **1h21**)
- Transcripción: `fuentes/transcripcion-reunion2.md` (reloj ×10) · Whisper real: `whisper-local/reu2/`
- Meet: **Demo Almahue ERP**. Presentan **Rodrigo Olguín** (`ROLGUIN` / Informática Santa Petra) y después **MJ** (`javillela` / `MGAJARDO`)
- Empresa de la demo Rodrigo: **Agrícola Santa Pilar**. MJ vuelve a **ALM SERVICES SPA**

Cliente en sala = requisito. Carlos/Sergio = hipótesis. AgroSmart = referencia de UX, **no** sistema a clonar (conta falló).

## 00:00–03:00 — setup

Rodrigo entra a compartir. MJ: limitaciones tarifario/factura; quieren ver **proceso completo proforma→factura** y comparar **AgroSmart** (campo/productores).

## 03:45–17:00 — flujo contratista Agrosoft (Santa Pilar)

| t Whisper | Pantalla | Qué importa |
|---|---|---|
| 03:50 | Home Agrosoft, menú contratistas expandido, user **ROLGUIN** | Maestro + labores/actividades son **bases distintas** |
| 05:20 | Tarifario + lookup 19 contratistas | Año/mes 06/2026 |
| 06:20 | Tarifas **Gómez & Gómez** (cod 6): 4 líneas labor 10, U.control 20, CC 50306xx, **37.500**, 01/06–23/07 | Agregar otra labor **borra** las anteriores; hay que reabrir el módulo |
| 07:50 | **Contratos**: cod 6, RUT `77.439.797-3`, tipo 1, 16–30/06, faena 300 | Folio **179** (audio; hay que anotarlo). Faena agrícola = paso de más |
| 08:30–09:20 | Enrolamiento → **Control de producción** Gómez, fecha 16/06 | Labor diaria. Actividad/labor **al revés** (hay que saberse la actividad de memoria). Precio **bloqueado** por tarifario; a veces el precio se negocia **después** del trabajo |
| **12:10** | **Emisión proforma**: contratista 6–6, **por folio 179**, **Borrador** | Definitiva emite **sin confirmación** |
| **13:20** | SSRS **Anexo** folio factura **0**, labor **15 ABRIR CARPAS**, CC cereza Santina, 1 jornada × 37.500 | |
| **14:10** | PDF **FACTURA PROFORMA MANO DE OBRA / BORRADOR**: «favor emitir factura…» a Santa Pilar RUT `76.137.120-7` | Se lo mandan al contratista para que facture. Definitiva = folio **155** |
| **15:05** | Conta › Proveedores › Registro compras › ayuda OC: tipo **CONTRATISTAS**, correlativos **154** (2.287.500) y **155** (37.500) | Tipo compra **6 Contratistas**. **Una proforma por mes**; dos meses en una factura **no se pueden asociar**. En la práctica meten todo en el mes de la factura → **gestión mensual mentira** |
| 17:00 | Registro con OC/proforma **155**, cta `210802003`, 37.500 | Cierre de mes: asiento facturas por recibir vs MO contratista (todas las proformas del mes) |

## 16:50–26:00 — AgroSmart (`app.agrosmart.cl`)

Referencia de lo que **quisieron** para contratistas. Conta de AgroSmart **duplicaba / descuadraba**; se quedaron en Agrosoft.

| t | Pantalla | Qué importa |
|---|---|---|
| 18:50 | **Registro múltiple mano de obra**: empresa, predio, fecha, sector, cuartel, faena, forma/unidad de pago, +fila | Tarifario **diario y editable**. En la demo el maestro de contratistas **no sincronizaba** (updates); caía a trabajador interno |
| 21:30 | **Asociar factura**: empresa Santa Pilar, proveedor, rango fechas | Labores sueltas → se van tildando contra una factura existente y **resta el saldo**. MJ/Rodrigo: ellos trabajan **al revés** (proforma primero); igual quieren armar proforma **eligiendo labores ya anotadas** |

Extraer de AgroSmart: **menos pestañas + asociar labores a un documento**. Lo demás (conta, reportes) = Agrosoft + Power BI.

## 26:30–35:00 — ventas (MJ, ALM)

Pendiente de R1. Form **Registro de ventas** (más campos que compras).

| t | Pantalla | Qué importa |
|---|---|---|
| 28:10 | Registro ventas vacío: Reversar, **Grabar/Contab.**, XML, guía, COMEX (embarque, cláusula) | **Guardar** = temporal, **no** sale en informes (queda «pendiente»). Útil solo **Grabar y contabilizar** |
| 30:40 | Doc **33**, nro 10, cliente Sandoval, 30 días + modal **códigos de venta**: 1 exportación `510101004`, 2 nacional `510101001`, 3 otros, 4 fruta comercial, 17 guías, 18 rebate | Muchos campos (fax, despacho) **no se usan** |
| ~32 | Reversa: no edita línea (a diferencia de proveedores). Cadena **472** orig / **473** reversa / **474** nuevo | Búsqueda de cliente falló (eligió Sandoval, apareció Chamonate) |

## 35:30–~55:00 — tesorería (MJ)

«Este ERP **no está hecho para conciliar ni calzar** pago↔factura; es parche.»

| t | Pantalla | Qué importa |
|---|---|---|
| 36:50 | **Pago a proveedores**: Banco Chile $, TRANS, radio peso/dólar, docs pendientes | Se puede **grabar sin tildar** factura. Calce peso no genera ΔTC en USD; calce **dólar sí** arma ajuste automático |
| 40:30 | Lookup comprobantes: EGRESOS/VENTAS **REVERSADO** vs ACTUALIZADO | Reversa deja par reversado/reversador |
| **42:00** | Tesorería › Conciliaciones › **Conciliación manual**: periodo 06/2026, banco `110102006` **BANCO CHILE YUAN**, dos grillas Cartola vs Contabilidad | Import **solo Excel**. Quieren **PDF banco**. Match **manual** (300 líneas). Cartola debería ser la verdad; hoy contabilizan primero y suben cartola a fin de mes. Varias cartolas/mes = lío para borrar |
| audio ~47 | Reversa conciliación: **todo el mes** (auto/manual/todas); no una línea. Error de empresa (Santa Pilar vs Los Palos) = rehacer el mes | Anticipos productores: tipo doc + egreso/ingreso; a veces **traspaso** para partir un anticipo. Código financiero = flujo (materia prima) |

Nóminas / aging 90 días: MJ pide **otra vuelta** a tesorería.

## 1:16–1:20 — insumos niveles + perfil

| t | Pantalla | Qué importa |
|---|---|---|
| ~1:16 | (still Meet; audio sí) | **Niveles de bodega no se usan** |
| 1:17:50 | Login **MGAJARDO / María José**, Santa Pilar: menú solo **Contratistas + Insumos** | Digitador contratista ≠ analista (analista: procesos diarios + informes; **sin** param, **sin** cierre, insumos solo informe). Cierre de mes = MJ |

Cierre: martes siguiente (R3 28/07). Trello de pantallas.

## Hallazgos que el video fija

- Folio contrato **179** → proforma borrador folio factura **0** → definitiva **155** → registro compra tipo **6** correlativo 155, 37.500, cta `210802003`.
- Empresa demo campo: **Santa Pilar**; conta/tesorería: **ALM**.
- Banco **Yuan** ya existe en conciliación (`110102006`).
- AgroSmart URL real: `app.agrosmart.cl` (asociar factura, registro múltiple).
