# Sesión Almahue 28/08/2026 — tesorería (MJ, Lupe, Fran, Mario)

**Tipo:** Demo / correcciones operativas de tesorería y contabilidad. **No sustituye Reu6** (MJ/Agustín de producto comercial/aprobaciones).  
**Fecha:** viernes 28/08/2026 (grabación local ~27/08 17:21; tl;dv `happenedAt` 28/08).  
**Participantes (audio):** María Jesús / MJ, Guadalupe / Lupe, Francisca / Fran (tesorería-contabilidad), Mario (entra ~40'). Lado Devint: Sergio + Carlos (voz de Carlos **no** quedó en la grabación).  
**Duración:** ~81 min (tl;dv duration ~4903 s).

| Fuente | Ubicación |
|---|---|
| Minuta personal Carlos (borrador) | Chat 28–31/08 + contraste PM |
| Transcripción tl;dv | [`fuentes/transcripcion-2026-08-28-tesoreria-mj-lupe.md`](fuentes/transcripcion-2026-08-28-tesoreria-mj-lupe.md) |
| tl;dv | https://tldv.io/app/meetings/6a91a445564eaa0013e057cd |
| Master ToDo / Trello | [`pm-barco-almahue-2026-08-31.md`](pm-barco-almahue-2026-08-31.md) §3 |

**Regla de autoridad:** MJ + Lupe/Mario/Fran = cliente operativo de **tesorería**. Pisán el plan 21/08 **solo en UX/flujo de cartola–TC–estado de cuenta–nómina** descritos aquí. **No** reabren D4/D11/D16 ni cadena OV.

Carlos/Sergio en sala = hipótesis / propuesta de UI, salvo donde MJ o Lupe confirman.

**Master de ejecución:** ToDos T1–T7 del pm-barco. Implementar **antes** que el resto del backlog histórico.

---

## 1. Resumen ejecutivo

1. **Anticipo productor + TC:** editable al crear y al calzar; montos de cartola/banco **inmutables**; solo cambia equivalencia USD / vista productor. Auditoría de quién cambió el TC.
2. **Cartola → contabilizar 1:1:** subir archivo y contabilizar cada movimiento **encima** de la cartola (contracuenta + destino doc/anticipo/traspaso/etc.). Cartola no “lista/archivada” con pendientes.
3. **Flujo de caja:** solo lectura; filtro por **moneda**; código financiero alimenta el flujo (tensión con R4-25 diferido).
4. **Triple moneda:** CLP/USD/yuan con TC Banco Central por fecha; excepción productor; carga histórica (Mario Excel ~19k); yuan hoy en Excel/Power BI.
5. **Nómina semanal de pagos:** título; aplazar año→mes→semana; totalizadores claros; ver semanas futuras; export.
6. **Estado de cuenta por RUT:** un RUT puede ser cliente y proveedor; pendiente/calzado; desplegable de con qué se calzó.

Cierre: tarjetas en línea; próxima reunión **jueves**.

---

## 2. Decisiones (cliente) vs demo vs hipótesis

### 2.1 Anticipo productor y tipo de cambio

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| TC manual al calzar anticipo↔factura | Si el anticipo tiene error, poder cambiar TC | Lupe ~12:40 | **Sí** |
| Anticipos productores en USD por contrato; a veces pagan CLP | Necesitan ver monto en USD manipulando TC | Lupe ~14:01 | **Sí** |
| TC editable una vez ingresado el anticipo (N anticipos / temporada) | Cada anticipo puede tener TC distinto | Lupe ~15:04 | **Sí** |
| Banco/cartola no se mueve | 10 millones en banco siguen 10 millones; cambia lo del productor | MJ ~54:37 | **Sí** |
| Registro de usuario en ediciones | Todo con registro de usuario | MJ ~18:52 | **Sí** |
| Campo “965” editable en pantalla de pago | Propuesta en demo | Sergio/Carlos | Hipótesis UI (encaja con pedido Lupe) |

### 2.2 Cartola y conciliación

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| Ideal: subir cartola y contabilizar cada movimiento | Factura, anticipo, etc. | MJ ~22:33 | **Sí** |
| Modal contracuenta + tipo destino | Proveedor/factura, anticipo, traspaso, sueldo… | MJ ~24:00 | **Sí** |
| Alternativa: cuenta + tipo doc + N° → calce en proveedores; si no existe → anticipo | Cruce al ingresar factura después | MJ ~26:13 | **Sí** |
| Contabilización 1 a 1 | Confirmado | MJ ~27:23 | **Sí** |
| Cartola con pendientes ≠ lista/archivada | Estados conciliado/pendiente; progreso 15/20 | MJ + Sergio | **Sí** |
| Agrandar modal detalle cartola | UX | Devint | **Sí** (sala) |
| Contrastar movimientos contables vs cartola | Lupe ~21:24; MJ desvía a contabilizar **desde** cartola | Lupe pregunta / MJ cierra | Decisión = modelo MJ |

### 2.3 Flujo de caja, monedas, código financiero

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| Flujo solo visualización (no editar/borrar) | | MJ/Mario | **Sí** |
| Filtro/eje por **moneda** (no por banco como total) | Totales suma bancos; moneda sí | MJ ~44–45 | **Sí** |
| Saldos reales por moneda por banco | Duda conversión global al TC del día → priorizar nativo | MJ ~48–50 | **Sí** (saldos nativos) |
| Código financiero en movimiento bancario → parametriza flujo | Como Agrosoft | MJ ~53 + demo ~57 | **Sí** (abre R4-25) |
| Triple moneda + BC diario; yuan hoy Excel/BI | Euro a futuro | MJ ~51–01:00 | **Sí** reportería |
| Carga histórica Excel (~19k) | Mario ofrece | Mario ~01:01 | Operativo |

### 2.4 Nómina y estado de cuenta

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| Título «nómina semanal de pagos» | | Lupe | **Sí** |
| Aplazar: año (default actual) → mes → semana | Facturas meses adelante | Lupe/MJ | **Sí** |
| Totalizadores semana vs mes claros | | Sala | **Sí** |
| Export periodo; ver semanas futuras | | Lupe | **Sí** |
| Tabs calendario desde–hasta / por año / por mes | Diseño Carlos | Carlos | **Propuesta** (no acuerdo cerrado) |
| Estado de cuenta por RUT unificado cliente+proveedor | | MJ/Lupe | **Sí** |
| Pendiente vs calzado; filtro histórico | | MJ | **Sí** |
| Desplegable: con qué anticipo/comprobante se calzó | | MJ ~01:19 | **Sí** |
| Seleccionar movimientos y ver total | Compensación | MJ | Bonus **Sí** |

### 2.5 Demo Agrosoft (contexto, no spec literal)

~27' pago proveedores + código financiero + asiento banco/proveedor.  
~30' calce anticipo+factura. Anticipo sin factura vía contabilidad.  
~57' comprobante diario: TC BC automático; selector moneda; no digitan USD a mano.

---

## 3. Contraste con plan 21/08 / código

| Pedido 28/08 | Plan / skill 21/08 | Lectura |
|---|---|---|
| Contabilizar desde cartola 1:1 con contracuenta elegida + doc | Asiento `CARTOLA:{id}` ya; contra fija vía `resolveCuentasCartola` | **Ampliar UX/API** (modal destino) |
| Pago = calce sin asiento PAGO | Ya | Sin cambio |
| Match automático | Diferido; calce manual | Confirmado manual |
| TC editable post-alta + al calzar + log | `tcManual` en create; `updatePago` permite `tcManual` pero sin log de auditoría | **Gap:** auditoría + UX calce |
| Código financiero obligatorio → flujo | R4-25 **diferido** | **Tensión** → preguntar jefe (P0?) |
| Triple moneda / yuan / BC | Flujo CLP/USD | **Nuevo** (fase 2 salvo que jefe diga P0) |
| Estado cuenta RUT dual + detalle calce | Kardex existe | **UX** |
| Nómina año/mes/semana | `semanaCompromiso` YYYY-MM-Sn | **UX** navegación/totalizadores |

---

## 4. Action items

### Devint

- Trello T1–T7 (orden T2 → T1 → T6 → T5 → T3 → T4).
- No codear “tabs calendario” como requisito cerrado.
- Pedir a MJ asiento de ejemplo si no llega.

### Almahue

- Mario: Excel histórico (~19k) cuando puedan.
- Validar tarjetas en línea durante la semana.
- Próxima reunión: **jueves**.

---

## 5. Speakers (aprox. en transcript)

| Label tl;dv | Lectura probable |
|---|---|
| Speaker 01 | MJ (y a veces sala Almahue) |
| Speaker 02 | Lupe / Mario según tramo |
| Speaker 00 | Sergio / eco Devint (y retornos) |

La voz de Carlos no está; sus notas personales + esta minuta cierran el lado Devint.
