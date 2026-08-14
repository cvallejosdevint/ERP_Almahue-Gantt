# Presentación demo Almahue ERP — guion + FAQ por pantalla

**Fecha:** 2026-08-06  
**Audiencia:** María Jesús / equipo Almahue (demo / visualización)  
**Alcance de esta presentación:** 100 % del flujo de negocio **excepto** Bodega / Insumos / Inventario y derivados (acordado: no mostrar en esta sesión).  
**Incluye obligatoriamente:** aprobaciones (reglas, bandejas OC y proformas, PIN).  
**Ambiente sugerido:** Modo real · periodo **2026-08** (o el ABIERTO vigente) · empresa Almahue SpA  
**Acceso demo:** `admin@almahue.local` / `Admin123!` · PIN aprobación seed: `4821` (si aplica al usuario)

---

# PARTE A — Guion de presentación (speech)

> Leer en voz alta siguiendo el orden. Cada bloque = una “escena” en pantalla.  
> Entre corchetes `[...]` = acción a hacer en el sistema.

### Convención GoSocket (leer cuando haya **negrita de emisión**)

En este speech, todo lo marcado en **negrita** que toque emisión / DTE / facturación electrónica es un punto donde, en producción, el ERP hablaría con **GoSocket** (vía billing-gateway).

**Frase sugerida (decir en voz alta en esos puntos):**  
*«Esto que estamos viendo son datos de prueba que estamos generando nosotros, **sin conexión a GoSocket**. Cuando tengamos las credenciales de GoSocket, podremos usar su ambiente de pruebas e implementarlo en el ERP.»*

Hoy el partner activo es el **stub** (simulación local): folio/auditoría de prueba, badge “Stub · no SII”. La UI no cambia al pasar a sandbox/live GoSocket; solo el registry / ApiKeys.

---

## 0. Apertura (2 min)

Buenos días. Hoy recorremos el **ERP Almahue** de punta a punta: desde la parametrización hasta la emisión, las compras con aprobación, contratistas, contabilidad y tesorería.

Tres ideas de ancla:

1. **Una sola interfaz de trabajo** — el usuario opera siempre en el ERP; lo que ocurre “abajo” (**facturador electrónico / GoSocket**) es transparente.
2. **Periodo contable abierto** — nada se contabiliza si el mes no está abierto.
3. **Aprobaciones con responsable y PIN** — OC y proformas no “pasan solas”: hay regla, jefe elegido y, si el rol lo exige, PIN de 4 dígitos.

En esta sesión **no** revisamos bodega ni inventario (queda fuera del alcance de hoy).  
Aclaración temprana: **hoy no hay conexión real a GoSocket**; lo que se ve de facturación electrónica es stub / datos de prueba nuestros.

`[Login → confirmar periodo ABIERTO → empresa Almahue SpA]`

---

## 1. Panel operativo (1 min)

`[/]`

Esta es la **home operativa**: KPIs y colas.

- OC por aprobar  
- Proformas pendientes  
- Facturas por recibir  
- Indicador TC (USD)

Sirve para que jefatura entre y vea **qué espera su firma**, sin buscar módulo por módulo.

---

## 2. Administración — quién puede qué (3–4 min)

### 2.1 Empresas
`[/admin/empresas]`  
Multi-empresa: RUT, razón social, giro, activa. El resto del sistema trabaja siempre con la **empresa activa** del header.

### 2.2 Plantilla documentos
`[/admin/plantilla-documentos]`  
Branding de PDF internos (logo, colores, pie, marca de agua). **No es el PDF timbrado SII / GoSocket**; es la representación gráfica del ERP.

### 2.3 Usuarios y roles
`[/admin/usuarios]` · `[/admin/roles]`  
- Usuario: nombre, email, rol, empresas de acceso, vigencia, activo (login = email; username interno automático).  
- Rol: matriz Lectura/Escritura por pantalla + flag **“Aprobar con PIN”**.

Mensaje clave: *el PIN no se configura aquí; se registra en el perfil del usuario.*

### 2.4 Reglas de aprobación ⭐
`[/admin/aprobaciones]`  

Aquí se define **quién puede aprobar qué**:

- Módulo: Compras (OC) o Contratistas (proformas)  
- Rango de monto (mín / máx)  
- Jefes elegibles  

Sin regla activa y jefes, el flujo de solicitud de aprobación no tiene a quién pedir.

### 2.5 Perfil — PIN
`[/perfil]`  
El aprobador registra su **PIN de 4 dígitos** (con contraseña de cuenta). Ese PIN se pide en las bandejas de OC y proformas.

---

## 3. Parametrización — “el sistema habla el idioma Almahue” (4 min)

Recorrido rápido (mostrar listados, no crear todos):

| Pantalla | Para qué |
|---|---|
| Monedas | Códigos CLP/USD/… (sync Banco Central **no** está aquí) |
| Unidades | UM de ítems |
| Centros de costo | Cuarteles / CC de imputación |
| Tipos de documento | Catálogo por módulo |
| Plan de cuentas | Árbol contable (imputables) |
| Elementos de costo | Clasificación de gasto |
| Indicadores BC | Series TC + sync Banco Central |
| Proveedores | Maestro compras |

Mensaje: *sin esto, las pantallas de negocio no tienen combos ni cuentas para asentar.*

---

## 4. Flujo de ventas — de cotizar a cobrar (8–10 min)

### 4.1 Clientes / prospectos
`[/comercial/clientes]` · `[/comercial/prospectos]`  
Maestro comercial y leads. El cliente alimenta RUT/razón en emisión.

### 4.2 Cotizaciones / NP (misma pantalla)
`[/comercial/cotizaciones]` — menú **Ventas › Cotizaciones / NP**

No hay menú separado de NP: viven en **esta misma ruta**, con dos pestañas.

[Abrir Ventas › Cotizaciones / NP]

1. Pestaña **Cotizaciones** — alta / emitir / anular. (Documento interno ERP; **aún no es DTE GoSocket**.)  
2. Acción **Nota de pedido** (o **Facturar directo** ← **aquí sí iría GoSocket** al generar factura electrónica).  
3. Cambiar a pestaña **Notas de pedido** — ahí quedan las NP listas para **Facturar** ← **emisión DTE vía GoSocket**.  
4. Cadena trazada con `folioOrigen` (Cotiz → NP → Factura).

Mensaje clave: *«Cotización y NP son el mismo mantenedor; el menú lo dice para no buscar un ítem fantasma.»*  
Al **Facturar** (desde cotiz o NP): decir la **frase GoSocket** (datos de prueba / sin conexión real todavía).

### 4.3 Emitir documento (wizard) ⭐
`[/comercial/emitir]`  

Tres pasos:

1. **Datos generales y receptor** — tipo (**Factura / NC** / …), forma de pago, fechas, indicador (Venta / Exento / **Exportación**), receptor.  
2. **Ítems** — descripción, cantidad, precio, descuento, **cuenta contable** (en ventas no se pide CC por línea; CC es más de compras).  
3. **Referencias y COMEX** — si es exportación: moneda, TC, país, puertos, FOB/CIF, bultos, etc. (manual COMEX → **payload DTE 110/112 hacia GoSocket**).

Acciones: borrador · preview · **Emitir / Grabar y contabilizar** ← **punto GoSocket** (emisión electrónica + auditoría partner).

Al pulsar **Emitir / Grabar y contabilizar**: decir la **frase GoSocket**.  
Hoy el ERP genera asiento contable y, vía *billing-gateway*, pasa por el **partner stub** (folio/auditoría simulada, **no** es DTE SII oficial). Eso demuestra el intermediario; con ApiKeys se cambia el registry a **GoSocket** (sandbox → live) **sin cambiar la UI**.

### 4.4 Libro de ventas
`[/comercial/libro]`  
Documentos del periodo: folio, tipo, RUT, neto, estado (`CONTABILIZADA`, **badge “Stub · no SII”** si la emisión fue por partner de prueba).  
Desde aquí: vista previa, **registrar pago** → Tesorería, reverso contable, **emitir NC** ← **otra interacción GoSocket**.

Al mostrar el badge stub / folio de prueba: decir la **frase GoSocket**.

### 4.5 Corrección
- **Reverso contable** = corregir imputación (cuenta); **no** anula el DTE en SII/GoSocket.  
- **Nota de crédito** = corrección tributaria / anulación de monto ← **emisión DTE vía GoSocket**.

`[Emitir una factura corta → decir frase GoSocket → verla en Libro (badge stub) → opcional: puente a pago]`

---

## 5. Flujo de compras — OC con aprobación PIN (8–10 min) ⭐

### 5.1 Orden de compra
`[/compras/ordenes]`  
Alta OC: proveedor, solicitante, **jefe aprobador**, moneda, neto, cuenta/CC/elemento, ítems, distribución CC.  
Estado típico: BORRADOR → **EMITIDO** (entra a bandeja).

### 5.2 Aprobación de OC
`[/compras/aprobaciones]`  
Bandeja del jefe: Solo pendientes · Ver · **Aprobar / Rechazar**.  
Si el rol exige PIN → modal de 4 dígitos.  
Resultado: APROBADO o RECHAZADO (con “resuelto por”).

### 5.3 Recepción
`[/compras/recepciones]`  
Post-aprobación: fecha recepción, TC, monto → CONFIRMADA.

### 5.4 Libro de compras
`[/compras/registro]`  
Factura de **proveedor** vs OC (match afecto/exento). Contabiliza y puede **Registrar pago**.  
(Registro de compra = documento del proveedor; **no** es emisión GoSocket de Almahue. Eventual **recepción/consulta DTE** de compra sería otro enganche futuro con el partner.)

`[Mostrar OC emitida → cambiar a usuario jefe o usar admin → aprobar con PIN → recepción → factura compra]`

---

## 6. Flujo contratistas — labor → proforma → factura N:1 (8 min) ⭐

1. **Contratistas** — maestro.  
2. **Tarifas** — labor / actividad / CC / precio / vigencia.  
3. **Ingreso diario** — digitar jornada/trato del día.  
4. **Asociación** — vincular ingresos a una proforma.  
5. **Proformas** — borrador → **Solicitar aprobación** (elige jefe según reglas) → bandeja.  
6. **Aprobaciones proforma** `[/contratistas/aprobaciones]` — Aprobar/Rechazar + PIN.  
7. Estado **DEFINITIVA** → asociar **factura** (N proformas : 1 factura).  
   (Factura de contratista = documento de **proveedor de MO**; hoy es registro operativo. **Si mañana se emite/recepciona DTE aquí, sería GoSocket** — por ahora no marcar como emisión Almahue.)
8. **Traspaso y cierre** — genera asiento de mano de obra / cierre del mes (TC, glosa).

Mensaje: *misma mecánica de aprobación que compras (regla + jefe + PIN), otro módulo.*

---

## 7. Contabilidad — el mes manda (5–6 min)

1. **Períodos** — abrir / cerrar / reabrir (+ motivo). Header muestra mes activo.  
2. **Config SII (cuentas)** — mapeo tipo documento → cuenta (ventas, clientes, IVA, etc.). **No es GoSocket**; es **cuenta contable** del ERP.  
3. **Asientos** — manuales + los generados por ventas/compras/contratistas.  
4. **Centralización** — lote de orígenes pendientes.  
5. **Libro diario / Mayor / Balance 8 columnas / Resumen** — reportería del periodo.  
6. **Honorarios / Presupuestos** — factores y presupuesto vs real (mencionar breve).

`[Mostrar periodo ABIERTO → un asiento generado por la factura demo (asiento ERP; la emisión DTE fue stub/GoSocket) → Diario o Mayor]`

---

## 8. Tesorería — caja y bancos (5–6 min)

1. **Flujo de caja** — ingresos/egresos operativos.  
2. **Cartolas** — import Excel/CSV/PDF (parser multi-hoja Almahue/bancos). Preview → importar → movimientos.  
3. **Pagos** — desde libros o alta manual; calce de documentos; TC si aplica.  
4. **Anticipos productores** — ANT/TRA + calce parcial.  
5. **Nóminas / aging** — cartera vencida, días de atraso.  
6. **Conciliación** — cartola ↔ movimientos/asientos.  
7. **Estado de cuenta** — saldos cliente / proveedor / productor con links a docs.

`[Abrir cartolas o un pago puente desde libro de ventas]`

---

## 9. Cierre del speech (2 min)

Recap del circuito:

```
Parametrización + Admin (roles, reglas, PIN)
        ↓
Ventas (Cotizaciones/NP → emitir → libro → pago)
Compras (OC → aprobación PIN → recepción → factura → pago)
Contratistas (labor → proforma → aprobación PIN → factura → traspaso)
        ↓
Contabilidad (periodo, asientos, libros)
Tesorería (cartola, pagos, conciliación, C/C)
```

Fuera de alcance hoy: **bodega / inventario**.  

**GoSocket — cierre explícito:** el ERP ya deja el enganche vía **billing-gateway**. En esta demo el partner es **stub** (pruebas nuestras, **sin credenciales GoSocket**). Con ApiKeys del ambiente de pruebas GoSocket se cambia el registry a sandbox/live **sin cambiar la UI**. Repetir si hace falta: *«lo que vieron de facturación electrónica son datos de prueba generados por nosotros; con credenciales usamos el ambiente de pruebas de GoSocket y lo implementamos en el ERP.»*

### Mapa rápido — puntos **GoSocket** del speech

| Momento | Acción en UI |
|---|---|
| Cotizaciones / NP | **Facturar** / **Facturar directo** |
| Emitir documento | **Emitir / Grabar y contabilizar** (Factura, NC, export) |
| COMEX / exportación | Datos DTE 110/112 al emitir |
| Libro de ventas | Badge **Stub · no SII** / folio de prueba |
| Corrección | **Nota de crédito** (emisión) |

No son GoSocket (aclarar si preguntan): plantilla PDF ERP, Config SII (cuentas), reverso contable, OC/compras, proformas contratista, cotización/NP como docs internos.

Preguntas → usamos la **Parte B (FAQ)** ordenada por pantalla.

---

# PARTE B — FAQ por módulo / página

> Uso en vivo: buscar por ruta o nombre de pantalla.  
> **Principal** = qué decir primero. **Secundario** = si profundizan.  
> Bodega/Insumos omitidos a propósito.

---

## B.0 Acceso y marco

### Login — `/login`

| Campo / elemento | Principal | Secundario |
|---|---|---|
| Email | Identificador de usuario | Debe existir y estar **activo**; multi-empresa se resuelve tras login |
| Contraseña | Credencial de acceso | En demo: `Admin123!` (modo real) |
| Modo real / demo | Real = API/BD; Demo = datos mock locales | No confundir “Demo Mode” del front con partner stub de facturación |

### Header global

| Elemento | Principal | Secundario |
|---|---|---|
| Periodo contable | Mes sobre el que se opera y contabiliza | Debe estar **ABIERTO** para asentar |
| Empresa | Tenant activo | Filtra casi todos los maestros y documentos |
| Notificaciones | Avisos de pendientes (OC/proformas) | Depende de datos y permisos |
| Usuario | Acceso a perfil / cerrar sesión | Rol y permisos vienen del login |

### Panel operativo — `/`

| Elemento | Principal | Secundario |
|---|---|---|
| KPI OC por aprobar | Cola de compras | Enlace típico a `/compras/aprobaciones` |
| KPI Proformas | Cola contratistas | `/contratistas/aprobaciones` |
| TC USD | Referencia de mercado | Serie Indicadores BC / Banco Central |
| Tablas pendientes | Detalle de lo que espera firma | Mismo origen que bandejas de aprobación |

### Mi perfil — `/perfil`

| Campo | Principal | Secundario |
|---|---|---|
| Nombre / Rol / Empresa | Identidad | Rol puede tener vigencia |
| Correo | Login (email + clave) | Recuperación de clave (si SMTP) |
| Cambiar contraseña | Seguridad de cuenta | Independiente del PIN |
| PIN (4) + confirmar + password | Autoriza aprobaciones | Solo si el **rol** tiene “Aprobar con PIN”; se valida en bandejas |

---

## B.1 Administración

### Empresas — `/admin/empresas`

| Campo | Principal | Secundario |
|---|---|---|
| RUT | Identidad tributaria empresa | Único en el sistema |
| Razón social | Nombre legal | Sale en PDFs y emisión |
| Giro | Actividad | Plantillas / DTE futuro |
| Activa | Si se puede operar | Inactiva no debería usarse en header |

### Plantilla documentos — `/admin/plantilla-documentos`

| Campo | Principal | Secundario |
|---|---|---|
| Dirección / Comuna / Ciudad / Tel / Email | Pie y membrete | Datos de contacto empresa |
| Colores / tipografía / tabla | Look del PDF ERP | No es timbre SII |
| Logo / sello URL | Imágenes de marca | Data-URL o URL pública |
| Watermark / pie / términos / datos pago | Textos legales internos | Watermark “BORRADOR” vs stub facturación son cosas distintas |

### Usuarios — `/admin/usuarios`

| Campo | Principal | Secundario |
|---|---|---|
| Nombre, Email | Identidad y login (email) | Username interno auto (sin UI) |
| Rol | Perfil de permisos | Define R/W y si pide PIN |
| Empresas (acceso) | Multi-tenant | Header solo muestra empresas permitidas |
| Contraseña | Alta / reset | Políticas internas |
| Vigencia rol desde/hasta | Temporalidad del rol | Login muestra aviso específico si expiró / aún no vigente |
| Activo | Puede o no iniciar sesión | Login rechaza inactivos |

### Roles y permisos — `/admin/roles`

| Campo | Principal | Secundario |
|---|---|---|
| Nombre del rol | Etiqueta (Admin, Jefe, …) | Asignable a usuarios |
| Aprobar con PIN | Si las bandejas exigen PIN | El PIN vive en el perfil del usuario |
| Matriz Lectura / Escritura | Qué pantallas ve / edita | Códigos de permiso (`comercial:write`, etc.) en API |

### Reglas de aprobación — `/admin/aprobaciones` ⭐

| Campo | Principal | Secundario |
|---|---|---|
| Nombre | Nombre de la regla | Solo organización |
| Módulo | Compras OC **o** Contratistas proformas | Comercial reservado / no activo en UI actual |
| Activo | Si aplica | Reglas inactivas no aparecen en solicitud |
| Monto mín / máx | Tramo de la operación | El monto de la OC/proforma debe caer en el rango |
| Jefes elegibles | Quiénes salen en el combo “aprobar con” | Deben ser usuarios con permiso de aprobación |

---

## B.2 Parametrización

### Monedas — `/catalogos/monedas`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre / Símbolo | Identidad de moneda | Usado en OC, pagos, COMEX |
| Activa | Disponible en combos | |
| (Sync BC) | No aquí | Va en `/catalogos/indicadores-bc` |

### Unidades — `/catalogos/unidades`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre / Activa | UM de ítems y tarifas | Ej. HR, HA, UN |

### Centros de costo — `/catalogos/centros-costo`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre | Imputación de gasto/producción | En compras y labores es crítico |
| Contacto / vigencia / Activa | Gobernanza | |

### Tipos de documento — `/catalogos/tipos-documento`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre / Módulo / Activo | Catálogo genérico | No confundir con tipo DTE 33/110 |

### Plan de cuentas — `/catalogos/plan-cuentas`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre / Tipo / Padre | Estructura contable | Solo cuentas **imputables** en asientos |
| Carga masiva | Import Excel | Preview antes de confirmar |

### Elementos de costo — `/catalogos/elementos-costo`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Nombre / Depto / Vigencia | Clasificación de gasto | Se usa en OC |

### Indicadores BC — `/catalogos/indicadores-bc`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha, USD, EUR, … | Series de tipo de cambio | Fuente Banco Central; feriados marcados |

### Proveedores — `/catalogos/proveedores`

| Campo | Principal | Secundario |
|---|---|---|
| RUT / Razón / Giro / Contacto / Email / Tel / Activa | Maestro de compras | Alimenta OC y libro de compras |

---

## B.3 Ventas

### Clientes — `/comercial/clientes`

| Campo | Principal | Secundario |
|---|---|---|
| RUT / Razón social | Identidad comercial | Puede precargar emisión |
| Línea de crédito / Vendedor / Activo | Control comercial | |
| tipoCliente / giro (si visible) | Exportación / nacional | Ligado a COMEX |

### Prospectos — `/comercial/prospectos`

| Campo | Principal | Secundario |
|---|---|---|
| Lead / Contacto / Origen / Estado / Fecha | Pipeline liviano | No genera asiento |

### Cotizaciones / NP — `/comercial/cotizaciones`

Menú UI: **Ventas › Cotizaciones / NP** (no existe entrada aparte “Notas de pedido”).

| Campo | Principal | Secundario |
|---|---|---|
| Pestañas Cotizaciones / Notas de pedido | Un solo listado, dos vistas | Misma URL |
| Folio / Fecha / Cliente / Neto / Estado | Documento comercial pre-factura | Estados: BORRADOR, EMITIDO, ANULADO, … |
| Convertir a NP / Factura | Cadena comercial | Conserva origen (`folioOrigen`) |
| Lineas | Detalle de costos | Mismas ideas que emitir |

### Emitir documento — `/comercial/emitir` ⭐

| Campo | Principal | Secundario |
|---|---|---|
| Tipo documento | Factura, NC, Cotización, NP, OC* | OC comercial del wizard no reemplaza Compras › OC |
| Forma de pago | Crédito / Contado / Transferencia | Va al documento y resumen |
| Folio | Correlativo interno ERP | **No** es folio CAF SII hasta partner real |
| Fecha emisión / vencimiento | Contable y cobranza | Debe caer en periodo operable |
| Indicador de venta | VENTA / SERVICIO / EXENTO / **EXPORTACION** | Define IVA y bloque COMEX |
| Factura origen (NC) | Documento a anular/corregir | Valida saldo disponible |
| Cliente / RUT / Razón / Giro / Dirección / Comuna / Ciudad | Receptor | Export: RUT extranjero tip. `55.555.555-5` |
| Ítems: descripción, cant, P.U., desc %, cuenta | Detalle y neto | Cuenta alimenta asiento |
| Descuento global % | Sobre subtotal | |
| Tipo / Folio referencia | 801 OC, 802 NP, 110 export, HES | Distinto de folioOrigen NC |
| COMEX: moneda, TC, país, puertos, cláusula, vía, modalidad, ind. traslado, bulto tipo/cant/marca, montos otra moneda | Datos DTE 110/112 | Manual MJ; no van a GoSocket aún en stub |
| Observaciones | Texto libre | Condiciones de pago / despacho |
| Billing stub (post-emisión) | Partner de pruebas | Badge “Stub · no SII”; PDF watermark |

### Libro de ventas — `/comercial/libro`

| Campo / acción | Principal | Secundario |
|---|---|---|
| Folio / Tipo / RUT / Razón / Fecha / Neto / Estado | Consulta del periodo | Filtro periodo header |
| Origen / cadena | Cotiz→NP→Factura / NC | |
| Stub · no SII | Emisión vía partner stub | No es DTE oficial |
| Registrar pago | Abre Tesorería con contexto | Bridge UI |
| Reverso contable | Corrige asiento | No anula fiscal |
| Grabar y contabilizar | Desde borrador/pendiente | Exige periodo abierto + cuenta |
| Cuenta / CC / Glosa (modal) | Imputación | Ventas: CC suele no aplicarse |

---

## B.4 Compras (con aprobaciones)

### Órdenes de compra — `/compras/ordenes` ⭐

| Campo | Principal | Secundario |
|---|---|---|
| Nº OC / Fecha | Identidad | Folio único por empresa |
| Proveedor | Maestro proveedores | |
| Solicitante | Quién pide | Usuario actual o elegido |
| **Jefe aprobador** | A quién se solicita firma | Sale de **Reglas de aprobación** |
| Depto / Moneda / Neto / Afecto-Exento | Condiciones económicas | Monto entra al tramo de la regla |
| Cuenta / CC cabecera / Elemento costo | Imputación | |
| Ítems + distribución CC | Detalle y reparto | |
| Estado | BORRADOR → EMITIDO → APROBADO/RECHAZADO → RECEPCIONADA | |

### Aprobación de OC — `/compras/aprobaciones` ⭐

| Campo / acción | Principal | Secundario |
|---|---|---|
| Filtro Solo pendientes | Cola del jefe | |
| OC / Proveedor / Solicitante / Solicitado a / Monto / Fecha / Estado | Qué aprobar | “Solicitado a” = jefe |
| Aprobar / Rechazar | Cierra la solicitud | |
| **PIN** | Confirma identidad del aprobador | Solo si rol tiene flag PIN; PIN del perfil |
| Resuelto por | Auditoría | Quién firmó |

### Recepción de OC — `/compras/recepciones`

| Campo | Principal | Secundario |
|---|---|---|
| Nº OC / Fecha recepción / TC / Moneda / Monto | Confirma llegada de mercadería/servicio | Post-APROBADO |
| Estado CONFIRMADA | Habilita factura compra | |

### Libro de compras — `/compras/registro`

| Campo | Principal | Secundario |
|---|---|---|
| Nº OC / Nº factura / Proveedores / Monto / Afecto | Factura proveedor vs OC | Alerta si afecto no calza |
| Ítems | Detalle factura | |
| Match | Calidad del calce OC | |
| Registrar pago | → Tesorería | |
| Contabilizar | Asiento de compra | Periodo abierto |

---

## B.5 Contratistas (con aprobaciones)

### Contratistas — `/contratistas`

| Campo | Principal | Secundario |
|---|---|---|
| RUT / Razón / Especialidad / Vigente / Hasta | Maestro prestadores | |

### Tarifas — `/contratistas/tarifas`

| Campo | Principal | Secundario |
|---|---|---|
| Contratista / Labor / Actividad / Tarifa / UM / CC / Vigencias | Precio de referencia del día | Ingreso diario puede sobrescribir precio |

### Ingreso diario — `/contratistas/ingreso-diario`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha / Contratista / CC / Labor / Actividad / Tipo jornada / Cantidad | Captura productiva | Precio/monto calculados |
| Estado | PENDIENTE → ASOCIADO → FACTURADO | |

### Asociación labores — `/contratistas/asociacion`

| Campo | Principal | Secundario |
|---|---|---|
| Selección de ingresos + Proforma destino | Arma el contenido de la proforma | Calce de montos |

### Proformas y facturas — `/contratistas/proformas` ⭐

| Campo / acción | Principal | Secundario |
|---|---|---|
| Número / Contratista / Periodo / Neto | Cabecera proforma | |
| Solicitar aprobación | Pasa a PENDIENTE_APROBACION | Elige jefe según reglas |
| Solicitante / Solicitado a / Resuelto por | Trazabilidad | |
| Aprobar / Rechazar / Definitiva | Cierra flujo | Puede pedir PIN |
| Factura N:1 | Varias proformas → una factura | Número y fecha factura |
| Reverso | Deshace definitiva | PIN/clave según config |
| Estado | BORRADOR → PENDIENTE → DEFINITIVA → FACTURADA | |

### Aprobación de proformas — `/contratistas/aprobaciones` ⭐

| Campo | Principal | Secundario |
|---|---|---|
| Misma lógica que OC | Bandeja + PIN | Módulo Contratistas en reglas |

### Traspaso y cierre — `/contratistas/traspaso`

| Campo | Principal | Secundario |
|---|---|---|
| Periodo / TC / Moneda TC / Glosa | Genera asiento de cierre MO | Va a Contabilidad |
| Resumen por periodo | Proformas, montos, asiento | |

---

## B.6 Contabilidad

### Períodos — `/contabilidad/periodos`

| Campo | Principal | Secundario |
|---|---|---|
| Código aaaa-mm | Identidad del mes | Header usa este periodo |
| Estado ABIERTO/CERRADO | Gobierna si se puede contabilizar | |
| Reabrir + motivo | Excepción controlada | Queda auditado |

### Config contable SII — `/contabilidad/config-sii`

| Campo | Principal | Secundario |
|---|---|---|
| Tipo documento SII → Cuenta / lado | Defaults de asiento | **No** es GoSocket; solo cuentas ERP |

### Asientos — `/contabilidad/asientos`

| Campo | Principal | Secundario |
|---|---|---|
| Número / Periodo / Fecha / Tipo / Estado / Glosa | Comprobante | Pueden ser manuales o generados |
| Líneas Debe / Haber / Cuenta | Partida doble | Debe = Haber |
| Contabilizar / Anular / Carga masiva | Ciclo de vida | Periodo abierto |

### Centralización — `/contabilidad/centralizacion`

| Campo | Principal | Secundario |
|---|---|---|
| Periodo / TC | Contabiliza orígenes en lote | Preview antes de ejecutar |
| Origen / Ref / Glosa / Monto | Qué se centraliza | Ventas, compras, etc. |

### Honorarios — `/contabilidad/honorarios`

| Campo | Principal | Secundario |
|---|---|---|
| Factor anterior/nuevo / vigencias | Retenciones | |

### Presupuestos — `/presupuestos`

| Campo | Principal | Secundario |
|---|---|---|
| Año / CC / Presupuestado / Ejecutado / Estado | Control vs real | |

### Libro diario — `/contabilidad/libro-diario`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha / Asiento / Cuenta / Glosa / Debe / Haber | Cronológico del periodo | Export |

### Libro mayor — `/contabilidad/mayor`

| Campo | Principal | Secundario |
|---|---|---|
| Cuenta / Debe / Haber / Saldos | Por cuenta | Filtro cuenta |

### Balance 8 columnas — `/contabilidad/balance-8-columnas`

| Campo | Principal | Secundario |
|---|---|---|
| Código / Cuenta / Sumas / Saldos / Inventario / Resultado | Balance clásico | Formato pedido por Conta |

### Reportes / resumen — `/contabilidad/reportes`

| Campo | Principal | Secundario |
|---|---|---|
| Reporte / Periodo / Estado | Descarga de reportes | |

---

## B.7 Tesorería

### Flujo de caja — `/tesoreria/flujo-caja`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha / Concepto / Ingreso / Egreso / Saldo | Vista operativa de caja | |

### Cartolas — `/tesoreria/cartolas`

| Campo | Principal | Secundario |
|---|---|---|
| Banco / Cuenta / Mes / Periodo / Archivo / Formato | Cabecera de carga | Parser multi-hoja (Almahue web / bancos) |
| Movimientos / Pendientes / Total / Estado | Resultado import | Contabilizar o crear pago desde movimiento |
| Import Excel/CSV/PDF | Entrada bancaria | Preview antes de confirmar |

### Pagos — `/tesoreria/pagos`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha / Beneficiario / Monto / Medio | Egreso | Bridge desde libros |
| Moneda pago/factura / TC / Dif. TC | Multi-moneda | |
| Documentos a calzar | Qué factura/OC cierra | |
| Estado | Ciclo del pago | |

### Anticipos productores — `/tesoreria/anticipos`

| Campo | Principal | Secundario |
|---|---|---|
| Fecha / Productor / RUT / Banco / Forma / Códigos / Montos / TC / Glosa | Anticipo | Tipos ANT/TRA |
| Calce parcial | Imputa a facturas luego | |

### Nóminas / aging — `/tesoreria/nominas`

| Campo | Principal | Secundario |
|---|---|---|
| Documento / Contraparte / Emisión / Vencimiento / Saldo / Días atraso / Estado | Cartera vencida | Editar vencimiento |

### Conciliación — `/tesoreria/conciliacion`

| Campo | Principal | Secundario |
|---|---|---|
| Banco / Periodo / Movimientos / Diferencia / Asiento / Cartola / Estado | Cuadra banco vs libros | Conciliar / desconciliar |

### Estado de cuenta — `/tesoreria/cuentas-corrientes`

| Campo | Principal | Secundario |
|---|---|---|
| Tipo tercero / Debe / Haber / Saldo / Movs | Kardex C/C | Links a factura, pago, cartola |
| Ajuste manual | Debe/Haber + glosa | Uso excepcional |

---

## B.8 Preguntas frecuentes transversales (atajos)

| Pregunta probable | Respuesta corta |
|---|---|
| ¿Por qué no contabiliza? | Periodo cerrado, falta cuenta, o sin permiso write |
| ¿Dónde está el PIN? | Perfil del usuario; el rol solo activa la exigencia |
| ¿Dónde están las notas de pedido? | Ventas › **Cotizaciones / NP** (pestaña); no hay menú aparte |
| ¿Quién aprueba? | Reglas de aprobación → jefes elegibles → bandeja |
| ¿Folio = folio SII? | Hoy folio **interno** ERP; oficial SII cuando partner GoSocket esté en live/sandbox |
| ¿Qué es Stub? | Facturador de **pruebas** en billing-gateway; se reemplaza por GoSocket en registry |
| ¿Reverso = NC? | No. Reverso = contabilidad; NC = documento tributario |
| ¿Por qué no vemos bodega? | Fuera de alcance de esta presentación (acuerdo MJ) |
| ¿Dónde pago una factura? | Libro ventas/compras → Registrar pago → Tesorería › Pagos |
| ¿Exportación? | Indicador EXPORTACION + bloque COMEX; RUT extranjero tip. 55.555.555-5 |

---

## Anexo — Orden sugerido de pantallas (checklist demo)

1. Login + periodo  
2. Panel  
3. Roles (PIN) + Reglas de aprobación + Perfil PIN  
4. Parametrización (flash) — monedas **sin** sync BC; sync en **Indicadores BC**  
5. Ventas › Cotizaciones / NP → **Facturar / Emitir** (**GoSocket**/stub) → Libro → (pago)  
6. OC → Aprobación PIN → Recepción → Libro compras  
7. Ingreso labor → Proforma → Aprobación PIN → Factura → Traspaso  
8. Periodo / Asiento / Diario  
9. Cartola o Pagos / Estado de cuenta  
10. Cierre + Q&A con Parte B  

### Cobertura seed (EMP-1 · 2026-08) — validado

| Área | Qué hay en BD |
|---|---|
| Auth | Admin con PIN `4821`; login = email |
| Workflows | Compras + Contratistas (jefes U-1, U-6) |
| Periodos | 2026-08 ABIERTO · 2026-07 CERRADO |
| Cotizaciones | BORRADOR, EMITIDO, APROBADO (convertida), ANULADO |
| NP | BORRADOR + EMITIDO (con `folioOrigen`) |
| Libro ventas | Facturas CONTABILIZADA (stub), EMITIDO, EXPORTACION, NC |
| OC | BORRADOR, EMITIDO+PENDIENTE, APROBADO, RECHAZADO, RECEPCIONADA |
| Aprob. OC | PENDIENTE / APROBADA / RECHAZADA |
| Recepciones | BORRADOR + CONFIRMADA |
| Libro compras | ≥4 CONTABILIZADA (incluye casos N OC → 1 factura) |
| Proformas | BORRADOR, PENDIENTE_APROBACION, DEFINITIVA, FACTURADA, RECHAZADA |
| Ingresos labor | PENDIENTE, ASOCIADO, FACTURADO |
| Asientos | CONTABILIZADO (venta/compra/MO) + BORRADOR manual |
| Tesorería | Pagos, cartola, caja, anticipo, cuenta corriente |
| Prospectos / clientes | 3 prospectos · 2 clientes EMP-1 |

*Tras `prisma db seed`, las 28 rutas del checklist cargan con h1 y rastro de datos seed (smoke UI).*

---

*Documento generado para la demo de visualización Almahue ERP. Actualizar si cambian rutas o campos de UI.*
