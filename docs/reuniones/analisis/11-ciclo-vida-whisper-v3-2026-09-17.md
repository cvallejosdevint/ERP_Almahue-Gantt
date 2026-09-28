# Ciclo de vida del software — transcripciones Whisper large-v3

**Corte:** 17/09/2026.  
**Fuente primaria:** transcripciones en `fuentes/transcripcion*.md` (lote Whisper `large-v3` + las ya limpias de Reu1–Reu6). Las minutas IA son índice, no evidencia.  
**Lista fina del lunes 14:** [`12-acuerdos-lunes-14-y-codigo.md`](12-acuerdos-lunes-14-y-codigo.md).

Este archivo **no borra** lo dicho en una reunión anterior. Cada semana deja su capa intacta; la columna «Vigente al 14/09» y la tabla de obsolescencia dicen qué se pisó después.

---

## 0. Método

| Regla | Aplicación |
|---|---|
| Quién habla | Cliente (Agustín, MJ / María José / María Jesús, Lupe, Mario, Fran, Rodrigo) = **requisito**. Carlos / Sergio = **hipótesis**. Pablo GoSocket = **tercero**. |
| Reu5 (03/08) | **Nulo.** Sin cliente. No pisa nada. |
| Reloj Reu1–Reu5 | Marca de transcripción ÷ 10 ≈ tiempo real. Reu6 y agosto–septiembre: reloj real. |
| Whisper `reu6/` | El MP4 mapeado **no** es la Reu6 ERP (es otro Meet). Usar `fuentes/transcripcion-reunion6.md`. |
| Tesorería 28/08 | ASR en `whisper-local/2026-08-27-tesoreria-ui/` (grabación 27/08, sesión de tesorería). |
| 14/09 | Cliente = `transcripcion-2026-09-14-demo-avances.md`. Las tres internas del mismo día **no** son requisito. |
| Cortes del dueño 03/09 | D4 solo OC y D11 cotización suprimida: ratificados. Lupe/Mario no pisan Reu6 **salvo** esa ratificación. |
| ASR | Whisper no diariza bien. «Chipas» = Chipax; «CUA» = columna Trello Devint; «MAU» = tablero Almahue; «Star» en conciliación ≈ sync banco; «ACRI» = año siguiente. |

Cadena de autoridad: transcripción con cliente > Reu6 > Reu4 > Reu3 > Reu1–2 (as-is). Interna proveedor nunca gana a un verbatim de cliente.

Documentos previos de esta carpeta (`01`–`10`) siguen siendo el detalle por reunión. Aquí se **disecciona** esa materia prima en procesos de ciclo de vida y se recorre **semana a semana** hasta el 14/09.

---

## 1. Inventario de sesiones (ERP) usadas en este corte

| Semana | Fecha | Id | Cliente en sala | Valor req. | Transcripción |
|---|---|---|---|---|---|
| 13/07 | 13/07 | Kickoff | Mario (Gantt/Trello) | Alcance proyecto, no Agrosoft | inventario `fuentes/cronologia/` |
| 21–23/07 | 21/07 | Reu1 | MJ, Rodrigo | **Alto · as-is Agrosoft** | `transcripcion.md` |
| | 23/07 | Reu2 | MJ, Rodrigo | **Alto · as-is** | `transcripcion-reunion2.md` |
| 28–30/07 | 28/07 | Reu3 | MJ | Medio-alto · demo ERP nuevo | `transcripcion-reunion3.md` |
| | 30/07 | Reu4 | MJ | Medio (sin gerencia) | `transcripcion-reunion4.md` |
| 03–06/08 | 03/08 | Reu5 | **nadie** | **Nulo** | `transcripcion-reunion5.md` |
| | 04–05/08 | GoSocket | Pablo ± MJ | Técnico emisión | `whisper-local/2026-08-04-gosocket/` + `2026-08-05-gosocket-interna/` |
| | 06/08 | Reu6 | MJ, Agustín | **Alto** | `transcripcion-reunion6.md` |
| 13/08 | 13/08 | Kickoff GS | Pablo | Técnico | `whisper-local/2026-08-13-kickoff-gosocket/` |
| 19–20/08 | 19/08 | Demo interno | nadie | Nulo | `transcripcion-2026-08-19-demo-interno.md` |
| | 20/08 AM | Sergio | nadie | Nulo (agenda de preguntas) | `transcripcion-2026-08-20-reunion-sergio.md` |
| | 20/08 PM | Lupe, Mario | **Alto operativo** compras/teso | `transcripcion-2026-08-20-tarde-lupe-mario.md` |
| 25–28/08 | 25/08 | Interna ERP | nadie | Nulo | `whisper-local/2026-08-25-erp-interna/` |
| | 28/08 | Tesorería | MJ, Lupe, Fran, Mario | **Alto tesorería** | `transcripcion-2026-08-28-tesoreria-mj-lupe.md` |
| 01–03/09 | 01/09 | Kickoff GS API | Pablo (sin MJ) | Técnico | minuta kickoff |
| | 01/09 | Sergio | nadie | Hipótesis | `whisper-local/sergio-2026-09-01/` |
| | 03/09 | Interna + **R dueño** | — | Cortes D4/D11 | `transcripcion-2026-09-03-interna-carlos-sergio.md` + `AGENTS.md` |
| 07–10/09 | 07/09 | Interna | nadie | Hipótesis NC/cuentas | `transcripcion-2026-09-07-interna-carlos-sergio.md` |
| | 08/09 | MJ + GoSocket | MJ, Pablo | Alto ventas locales | recap + `2026-09-08-seguimiento-gosocket/` |
| | 10/09 | Demo cliente | cliente | Alto DTE/OV | `transcripcion-2026-09-10-demo-cliente.md` |
| | 10/09 | Interna | nadie | Nulo | `transcripcion-2026-09-10-interna-carlos-sergio.md` |
| 14/09 | 14/09 AM/mediodía | Internas | nadie | Nulo | `transcripcion-2026-09-14-interna-manana.md` / `…-mediodia.md` |
| | **14/09 tarde** | **Demo avances** | **Mario; MJ/Lupe invitadas** | **Alto. Lista fina.** | `transcripcion-2026-09-14-demo-avances.md` |
| | 14/09 noche | Interna tesorería | nadie | Diseño proveedor (coda) | `transcripcion-2026-09-14-interna-tesoreria.md` |

---

## 2. Disección por proceso del ciclo de vida

### 2.1 Toma de requisitos

Cómo se levantó (no es un BRD clásico):

1. **Recorrido as-is** (Reu1–Reu2): MJ/Rodrigo comparten Agrosoft, módulo por módulo. Es la única foto completa del sistema que el cliente usa hoy.
2. **Demo to-be** (Reu3 en adelante): el proveedor muestra el ERP nuevo (a menudo calco de Agrosoft) y el cliente corrige en voz.
3. **Pregunta cerrada** (20/08 tarde, parte de 14/09): Sergio/Carlos preguntan «¿cierto?» y el cliente dice sí. Vale como **confirmación**, no como pedido espontáneo. Se marca.
4. **Sesión de dominio** (28/08 tesorería, 08–10/09 DTE): un módulo a fondo. El 14/09 pide **repetir ese formato** (lunes contabilidad, martes tesorería).
5. **Tablero Trello** (Reu3 método; 14/09 asignación por persona/módulo). Las tarjetas no sustituyen la transcripción.
6. **Ratificación del dueño** (03/09): única vez en que un corte de código que choca con Reu6 queda firme (D4, D11).

Lo que **no** es toma de requisitos: Reu5, internas Carlos↔Sergio, minutas tl;dv, afirmaciones en demo del tipo «ya está».

Entregable de esta fase al 14/09: lista fina en el documento `12`, no un SRS aparte.

### 2.2 As-is — Agrosoft (lo que el cliente hace hoy)

Fuente: Reu1–Reu2 (recorrido), más frases «actualmente…» en Reu3, Reu4, Reu6, 20/08 y 28/08.

| Proceso | Cómo trabaja hoy | Dicho por | Dónde |
|---|---|---|---|
| Acceso | Link externo, última empresa, mes contable + mes remuneración. 15 usuarios; a veces 2 personas / 1 usuario → fugas de empresa. | MJ | Reu1 |
| Compras | En Agrosoft a menudo **primero la factura, después la OC**. Aprobación por organigrama informal (Agustín se salta niveles). Recepción de mercadería ≠ movimiento de stock. | MJ, Agustín, Lupe | Reu1, Reu6, 20/08 |
| Cotización | Cotizar es de **compras**, no de ventas. «Hoy no se cotiza para vender.» | MJ | Reu6 `[40:09]` |
| Ventas | Se emiten **fuera** del ERP, en el facturador (Acepta → GoSocket). Libro de ventas = DTE ya emitidos. | MJ | Reu6 `[40:21]`, Reu2 |
| Contratistas | Tarifario → contrato → enrolamiento → labores → **N proformas → 1 factura** → asiento. | Rodrigo, MJ | Reu2, Reu3 |
| Tesorería | Pago: banco + **código financiero** + RUT + factura + n° cartola (hoy digitado, a menudo «1»). Asiento banco vs CxP en peso y dólar. Cartola: Excel del banco, **no** correo diario. Nómina de pago **semanal** (Lupe). | MJ, Lupe | Reu4, 20/08, 28/08 |
| Flujo de caja | Se arma con códigos financieros al pagar. MJ: ver gasto **por moneda**, no por banco. Lupe: saldo **por banco y moneda**. | MJ, Lupe | 28/08 |
| Contabilidad | Plan 5 niveles; CC / elemento / área por cuenta. Mayor es el reporte de trabajo; diario casi no. Contabilidad electrónica **anual** (renta). Factores honorario escalonados. Cierres **por módulo**. | MJ | Reu4, Reu6 |
| Dimensiones | Área de negocio con activo/inactivo. «Gastos próxima temporada» + traspaso manual. | MJ, Agustín | Reu6 |
| Estado de cuenta | Informe «inventario balance»; cobranza «arcaica». | MJ | Reu4 |
| Bancos | Varias cuentas por contraparte y moneda. Riesgo de fraude por cambio de cuenta. Datos bancarios se buscan en el correo. | Agustín | Reu6 |
| Bodega | Stock en tránsito **solo bodega**. Venta exige stock real. | MJ | Reu6 `[55:55]` |
| Reversas | Clave de reversa **por perfil**; el analista no la ve. | MJ | Reu4 |
| GoSocket vs Acepta | Objetivo declarado: **libro de compras en línea** y contabilizar directo. Contrato Acepta se acababa en septiembre. | MJ | Reu2, Reu4 |

### 2.3 To-be — ERP Almahue (lo que se acordó construir)

Estado **vigente al 14/09**, ya con pisos aplicados. El detalle de quién pisó a quién está en §4.

| Proceso | To-be vigente | Origen que manda |
|---|---|---|
| Tenant | Todo filtrado por `empresaId`. Periodo contable en header. | Reu1 fuga de contexto + convención de código |
| Compras | Arranque = **OC** correlativo. Cadena PIN **solo OC**. Factura a OC no aprobada: **asociar y destacar**, no rechazar. Sin OC (90 % real): destacar, queda pendiente, a los 8 días auto-acepta. No contabilizar ni pagar hasta OC `APROBADO`. | Reu6 + 20/08 + R 03/09 + **14/09 Mario/MJ** |
| Cotización | Sin CRUD. Referencia tipo/folio/fecha en la OC. | R 03/09 (MJ Reu6 pedía moverla a Compras) |
| Ventas | OV → Guardar valida stock → `CONFIRMADA` → Emitir DTE. Sin bandeja OV. Libro = DTE; `EMITIDO` = por contabilizar (cuenta + CC **por ítem**). | 20/08 + R 03/09 + 08–10/09 |
| D16 | No vender bajo **precio de compra** del maestro; caída a `costoPromedio`. | Reu6 MJ `[50:00]` |
| NC/ND | CodRef 1/2/3 amarrada a factura origen; TC de origen. Confirmación al emitir. | 08–10/09 |
| Contratistas | N proformas → 1 factura. `BORRADOR` → `DEFINITIVA` con `contratistas:write`. **Sin** bandeja PIN. | Reu3 cortado 21/08 + R 03/09 |
| Tesorería cartola | Import Excel/CSV/PDF. Contabilizar **1:1** el movimiento (ingresos sí; egresos en discusión con nómina). Conciliación = **vista**. Lookup factura (match RUT+monto). Saldos **banco × moneda** en cartolas. | 28/08 + **14/09** |
| Tesorería nómina | Semana de compromiso (`YYYY-MM-Sn`). Aplazar. No muta DTE. El 14/09: asociar egresos de cartola a una nómina que **calce**; MJ quiere **contabilizar con la nómina** en egresos (asiento puente: propuesto, no cerrado). | 28/08 + **14/09** |
| Flujo de caja | Lectura. Totalizado **por moneda** (independiente del banco). Filas = **concepto + código financiero**. Excel de Mario como formato. | 28/08 + **14/09** |
| Estado de cuenta | Por RUT, menú Tesorería, corte mes contable. | Reu4 rename + 28/08 T6 |
| Chipax / sync banco | **Diferido** (Mario: echar a andar import; automatizar el año siguiente). | **14/09** `[50:29]` |
| GoSocket | Emisión vía gateway (CAF/cert Almahue). Contabilización = solo ERP. Recepción → libro compras: **sigue pendiente**; el 14/09 la reabre como aceptar/reclamar en el ERP. | Reu2 vs onboarding ago–sep + **14/09** |
| Alertas RUT | Watchlist de RUT (disputa / objetado SII): campana + correo a N usuarios, **no** auto-rechazo. | **14/09** `[26:36]`–`[33:32]` |
| Triple moneda | Pedido MJ 28/08: 3 conversiones en **toda** contabilización. **Sigue pendiente** en mayor. | 28/08 |
| Reuniones | Por módulo, con responsable de tarjetas. Tesorería no se pasa a Lupe hasta corregir (salvo nómina semanal). | **14/09** |

### 2.4 Análisis y diseño (decisiones de alcance)

Decisiones que **cambian el producto** y no son un bug:

| Código | Decisión | Tipo |
|---|---|---|
| D4 | Cadena de aprobación solo Compras (OC). OV sin bandeja. | Corte dueño 03/09 |
| D11 | Cotización suprimida como documento; no restaurar cotiz→NP→factura | Corte dueño 03/09 |
| D16 | Piso = precio compra maestro | Reu6 cliente |
| D17 | Flete = `tipoLinea` en OV | Reu6; canonical SII no auditado |
| T1–T6 | Tesorería ciclo 21/08 y UI 28/08: cartola, conciliación vista, flujo, nómina, CC, pagos sin `PAGO:{id}` | 21/08 código + 28/08 cliente |
| Config SII | Panel interno ERP (cuentas por tipo). **No** es requisito de GoSocket | Reu4; mito Reu5 anulado |
| Proformas PIN | Eliminado, no oculto | Código 21/08; 0 menciones 19–20/08 |

Huecos de diseño **abiertos** al 14/09: asiento puente de nómina; rango fechas cartola; alerta RUT; recepción GoSocket; triple moneda en asientos; restaurar o no cotizaciones (cerrado por dueño).

### 2.5 Implementación (dónde vive en código)

No es un inventario de archivos. Es el puente ciclo de vida → repo:

| Dominio | Back | Front |
|---|---|---|
| Tenant / periodo | `empresaId` en servicios Nest; JWT | `useEmpresaScopeId`, `usePeriodoScopeCodigo`, header periodo |
| OC + cadena | `compras.service.ts`, `approval-engine.ts`, `oc-estado.util.ts` | `ComprasPages.tsx`, `/compras/aprobaciones` |
| OV + Emitir | `comercial.service.ts`, `ov-estado.util.ts` | `EmitirDocumentoPage.tsx` (`mostrarCuenta={false}`), Libro ventas |
| Tesorería | `tesoreria.service.ts` (`getSaldosBancos`, `asociarNominaCartola`, `lookupDocumentoCartola`, `flujo-caja`) | `CartolaBancariaPage`, `FlujoCajaPage`, `NominasAgingPage`, `CuentasCorrientesPage` |
| Concepto flujo | `ConceptoFlujo` + `catalogos` `conceptos-flujo` | `/catalogos/conceptos-flujo` |
| DTE partner | `billing-gateway` (otro repo) | Emitir; stub vs HTTP |

Validación archivo a archivo del 14/09: documento `12`.

### 2.6 Validación (QA, demo, tablero)

- QA local: skill `almahue-qa-local`; planes en `qa/`. No reabrir casos PASS como regresión sin evidencia.
- Demos con cliente: Reu3, Reu4, Reu6, 20/08 PM, 28/08, 10/09, **14/09**.
- 14/09: las tarjetas de **compras no se pasan** hasta ajustes de aprobación/reclamo; tesorería vuelve a columna Devint salvo nómina semanal para Lupe.
- Demo mode (`EMP-1`, periodo `2026-08`): no es requisito de cliente; es fixture para no mostrar pantallas vacías.

### 2.7 Entrega / operación

- Prod `45.7.229.46`: **H14** vigente — no asumir migrate de stock/OV/`piloto_on` hasta deploy explícito.
- 14/09 mediodía: interna sobre movimientos de bodega **en prod**. No genera requisitos nuevos.
- Operación acordada: reuniones semanales **por módulo** + WhatsApp para coordinar.

---

## 3. Acuerdos por semana (capa intacta + qué quedó obsoleto)

Leyenda **Vigente al 14/09:** Sí / No (pisado) / Parcial / Nulo (nunca fue requisito).

### Semana 13/07 — kickoff proyecto

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| K13-1 | Proyecto ERP con Gantt ~6 meses y tablero Trello | Mario + Devint | Sí (método). El 14/09 **formaliza** responsables por módulo |

### Semana 21–23/07 — Reu1 + Reu2 (as-is)

| Id | Acuerdo / hallazgo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| R1-01 | Recorrer Agrosoft como referencia funcional | MJ | Sí. Reu1–3 son as-is, no ruido |
| R1-02 | En Agrosoft a menudo factura **antes** que OC | MJ | **As-is vigente.** El to-be «OC primero» se **suavizó** el 14/09 (destacar, no rechazar) |
| R1-03 | Multiempresa + mes contable al entrar | MJ | Sí (periodo header) |
| R1-04 | Contratistas: N proformas → 1 factura | Rodrigo | Sí el proceso; **No** la cadena PIN (cortada) |
| R2-01 | GoSocket para **libro de compras en línea** y contabilizar directo | MJ | **Parcial.** Emisión construida; recepción **pendiente**. El 14/09 la reabre (aceptar/reclamar en ERP) |
| R2-02 | Libro de ventas = documentos emitidos, no ensuciar con borradores | MJ | Sí (P0-4: borradores en Emitir) |
| R2-03 | Tesorería: calce, anticipos, cartola, conciliación | MJ/Rodrigo | Sí, detallado 28/08 y 14/09 |
| R2-04 | Reversa reutilizable | MJ | **Parcial** (API sí, UX Libro incompleta) |

### Semana 28–30/07 — Reu3 + Reu4 (primer to-be)

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| R3-01 | Tablero Trello como método de avance | MJ/Carlos | Sí; 14/09 asigna personas |
| R3-02 | Proformas con aprobación / re-aprobación al editar | MJ | **No.** Cortado 21/08 + R 03/09 |
| R3-03 | Libro comercial → Libro de ventas (nombre) | MJ | Sí |
| R3-04 | Carga masiva SII + dedup | MJ | **Parcial** (CSV/folio) |
| R3-05 | Cuenta y CC al contabilizar (no solo cabecera) | MJ | Sí en Libro ventas 08–10/09 |
| R4-01 | Conservar panel de cuentas por tipo documento (Config «SII») | MJ tibio + Carlos | Sí como panel **ERP**. No es GoSocket |
| R4-02 | Cartola: cargar Excel del banco (no correo diario) | MJ | Sí. Chipax **no** lo pisa (14/09 lo aplaza) |
| R4-03 | Estado de cuenta (rename de cuentas corrientes) | MJ | Sí, solo menú Tesorería |
| R4-04 | Imputar al emitir / pagar con código financiero | MJ demo Agrosoft | **Parcial.** Código financiero **sí** (flujo). Cuenta de venta: **solo al contabilizar** (piso 08/09) |
| R4-05 | Plan de cuentas 5 niveles + dimensiones | MJ | Sí |
| R4-06 | Clave de reversa por perfil | MJ | Sí (clave reversa; PIN aparte) |
| R4-07 | Cambio facturador Acepta→GoSocket en agosto | MJ | Sí (emisión). Recepción pendiente |

**Obsoletos esta semana:** ninguno interno. Reu4 no tiene gerencia: lo que pida solo MJ puede ser precisado después por Agustín/Mario.

### Semana 03–06/08 — Reu5 nula + Reu6

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| R5-* | Cotiz→NP→factura, Config SII «necesaria para GoSocket», etc. | Solo proveedor / minuta IA | **Nulo.** No entrar |
| R6-D4 | Cadena: en sala se habla de **OC**; la minuta mete Comercial/proformas | Minuta vs verbatim | Ver piso 20/08 + R 03/09 → **solo OC** |
| R6-D11 | MJ: la cotización **debe estar en el panel de compras** `[40:59]` | MJ | **No como CRUD.** R 03/09 suprime. **No reabrir** sin dueño |
| R6-D16 | No vender bajo precio de compra del **maestro** | MJ «si se puede, ideal» | Sí |
| R6-01 | Trazabilidad usuario + clave para reversar | MJ | Sí |
| R6-02 | Ventas se saben antes; se emiten en facturador | MJ | Sí (OV → Emitir) |
| R6-03 | Ficha banco de contraparte en el ERP (no buscar en el correo) | Agustín | Sí (ficha) |
| R6-04 | Área de negocio / gastos próxima temporada | Agustín, MJ | Parcial (dimensiones sí; puente temporada no cerrado) |
| R6-05 | Stock tránsito solo bodega; venta con stock real | MJ | Sí (D14 Reu6 ≠ D14 Reu4) |
| R6-D17 | Flete como línea | sala | Sí `tipoLinea`; recargo SII no auditado |

**Obsoletos al salir de la semana:** nada de Reu6 cliente. La minuta D4 «OC+proformas+Comercial» ya era un error documental.

### Semana 13/08 — GoSocket kickoff técnico

Acuerdos de **emisión** (CAF, certificado, API). No pisan Reu2 recepción. No son requisitos de MJ.

### Semana 19–20/08 — operativa Lupe/Mario

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| A20-01 | «Nosotros solamente nos piden la OC y nosotros solo generamos la OC» | Lupe `[05:48]` | Sí como operación. Cotiz CRUD cortada por R 03/09 |
| A20-02 | ¿Aprobación de OV? Respuesta a pregunta **cerrada** Lupe/Mario | Confirmación, no pedido | **Solo OC** por R 03/09. No usar 20/08 para apagar Reu6 **sin** esa R |
| A20-03 | Flujo de caja **por banco** (Lupe) | Lupe | **No.** MJ 28/08 + 14/09: flujo por **moneda**; banco en **cartola** |
| A20-04 | Nómina semanal de pago; cartola Excel; anticipos | Lupe | Sí |
| A20-05 | Proformas / contratistas | — | **No se hablaron** (0 menciones). No sirve para cortar Reu3; el corte lo hizo el dueño 03/09 |

**Obsoletos:** cadena OV que el código aún mostraba el 19/08 (demo interno) — se **eliminó** el 21/08, no se ocultó.

### Semana 25–28/08 — tesorería (master ToDo del módulo)

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| A28-01 | Cargar archivo banco y contabilizar **encima** de la cartola (no digitar) | MJ | Sí |
| A28-02 | Flujo de caja **por moneda** («no tiene sentido por banco») | MJ | Sí. 14/09 lo **confirma** y manda banco a cartolas |
| A28-03 | Saldo por banco y moneda (Lupe necesita ver dólar/yuan/peso) | Lupe | Sí, **en cartolas** (14/09) |
| A28-04 | Triple conversión en toda contabilización | MJ | **Pendiente** (mayor monomoneda). El 14 **no** lo cierra |
| A28-05 | Nómina = semana de compromiso | Lupe/MJ | Sí |
| A28-06 | Conciliar / contabilizar 1:1 en cartola | sala | **Parcial.** 14/09: ingresos 1:1; egresos MJ quiere **nómina** |
| A28-07 | Código financiero alimenta el flujo | MJ Agrosoft | Sí |
| A28-08 | Estado de cuenta por RUT | MJ | Sí |

### Semana 01–03/09 — partner + cortes dueño

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| R03-D4 | Aprobaciones **solo OC**. OV Guardar → `CONFIRMADA` | Dueño | Sí. 14/09 no reabre OV |
| R03-D11 | Cotización suprimida | Dueño | Sí. 14/09 no reabre |
| GS-01 | Emisión sandbox GoSocket (folio, XML) | Pablo/Carlos | Sí técnico |
| GS-02 | Contabilización no la hace GoSocket | diseño | Sí |

### Semana 07–10/09 — DTE / Libro ventas

| Id | Acuerdo intacto | Quién | Vigente al 14/09 |
|---|---|---|---|
| A10-01 | Cuenta + CC **por ítem** al contabilizar. Emitir **sin** cuenta | MJ 08/09 | Sí. 14/09 no lo toca |
| A10-02 | NC CodRef 1/2/3 + TC de factura origen | MJ/Pablo | Sí |
| A10-03 | Historial factura ↔ NC/ND | cliente | Sí |
| A10-04 | Exportación DTE: set con Pablo **pendiente** | 10/09 | Pendiente |
| A10-05 | Recepción compras GoSocket | Reu2 vivo | Pendiente; **14/09 lo agenda** (aceptar/reclamar) |

Ver también `09-acuerdos-definitivos-2026-09-10.md` (corte anterior a esta semana).

### Semana 14/09 — lista fina (detalle en documento 12)

Gobernanza: tarjetas por módulo; compras no se pasan; tesorería vuelve a CUA salvo nómina; reuniones semanales por módulo.

Compras/DTE recibido: destacar OC no aprobada **y** sin OC; no auto-rechazo; 8 días; alerta RUT (campana+correo).

Tesorería: Chipax año siguiente; cartola con fechas (rollback intra-reunión); conciliación vista; lookup factura; asociar egresos↔nómina que calce; flujo totalizado moneda + concepto/código; saldos banco en cartolas.

Interna tesorería 14/09 noche (Sergio): maestro concepto + asociar nómina en egresos — **diseño proveedor** alineado con lo que Mario/MJ acababan de pedir; no crea requisitos extra.

**Obsoleto dentro de la misma reunión 14/09:** «excluir movimiento del mes anterior» `[47:17]` → rollback `[48:12]` «como control interno lo vamos a eliminar y que sí se pueda leer la fecha del mes anterior». Queda: cargar lo que venga + **rango desde–hasta** para subida semanal.

---

## 4. Cadena de obsolescencia (quién pisa a quién)

| Tema | Acuerdo original | Lo pisa | Queda vigente el 14/09 |
|---|---|---|---|
| Aprobaciones OV / Comercial | Minuta Reu6 D4: OC+proformas+Comercial | 20/08 pregunta cerrada **no basta**; **R 03/09 sí** | Solo OC. OV: Guardar → `CONFIRMADA` |
| Proformas con PIN | Reu3 MJ | Código 21/08 + R 03/09 | `BORRADOR`→`DEFINITIVA` con permiso write |
| Cotización | Reu6 MJ: **mover a Compras** | Lupe 20/08 + R 03/09 | Sin CRUD; ref. en OC |
| Cuenta en venta | Reu4 imputar al emitir | MJ 08/09 | Solo al contabilizar Libro, CC por ítem |
| Eje flujo caja | Lupe 20/08: por banco | MJ 28/08: por moneda; 14/09 confirma | Flujo = moneda + concepto/código. Banco = cartola |
| 1:1 cartola | 28/08 contabilizar cada línea | 14/09 MJ: egresos con **nómina** | Ingresos 1:1. Egresos: asociar a nómina (hecho) + puente contable (**abierto**) |
| Sync banco | Hipótesis Chipax/Fintox | Mario 14/09: no ahora | Import Excel. Automatizar «ACRI» próximo año |
| Fecha cartola mes anterior | 14/09 `[47:17]` excluir | 14/09 `[48:12]` rollback | Incluir; rango desde–hasta (front **no** lo tiene) |
| GoSocket | Reu2 = recepción compras | Onboarding = emisión | **Ambos.** Emisión sí. Recepción pendiente; 14/09 la pide en el ERP |
| Config SII ↔ GoSocket | Minuta Reu5 | Verbatim Reu5 = PIN, no SAI | Panel ERP interno. GoSocket no lo usa |
| Cotiz→NP→factura | Minuta Reu5 | Nunca hubo cliente | No entra |
| OC rígida antes de factura | To-be implícito Reu3–Reu6 | Mario 14/09: «en teoría no, en la práctica sí» | Destacar, no rechazar. 8 días |

Reu5 **no pisa nada**.

---

## 5. Mapa as-is → to-be por proceso (resumen ejecutivo)

```
Agrosoft (Reu1–2)          Decisión de alcance              ERP al 14/09
─────────────────          ──────────────────              ────────────
Factura → OC a posteriori  OC primero + cadena     →      OC + destacar si factura llega antes
Cotizar en compras         MJ: mover / dueño: quitar →    Ref. en OC, sin menú
Ventas en Acepta           OV + GoSocket emisión   →      OV CONFIRMADA → Emitir → Libro
Proforma con control MJ    Corte PIN 21/08         →      Definitiva sin bandeja
Cartola digitada           Excel 28/08; Chipax no  →      Import; 1:1; lookup; nómina en egresos
Flujo por código al pagar  Moneda 28/08 + Excel 14 →      Flujo Excel-like; saldos en cartola
Mayor con 3 conversiones   Pedido 28/08            →      Pendiente (asiento JSON monomoneda)
Libro compras Acepta       GoSocket recepción      →      Pendiente + alerta RUT / 8 días
```

---

## 6. Qué validar ahora

El documento hermano [`12-acuerdos-lunes-14-y-codigo.md`](12-acuerdos-lunes-14-y-codigo.md) toma **solo** los acuerdos del lunes 14 (más el stock vigente que esa reunión no reabrió) y marca cada uno **CUMPLE / PARCIAL / PENDIENTE** en back y front.

Huecos que el ciclo de vida deja explícitos para no reabrirlos como «ya está»:

1. Alerta parametrizable por RUT (campana + correo).
2. Rango de fechas desde–hasta al cargar cartola.
3. Asiento puente / contabilizar egresos **con la nómina**.
4. Destacar en UI las facturas **sin** OC (hoy el alta exige OC).
5. Triple moneda en el mayor.
6. Recepción GoSocket → aceptar/reclamar en el ERP (objetivo Reu2).
7. SMTP (H9) — no se habló el 14; sigue pendiente de infraestructura.
