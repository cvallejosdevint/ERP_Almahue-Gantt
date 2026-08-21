# Sesión Almahue 20/08/2026 (tarde) — Lupe, Mario, Sergio, Carlos

**Tipo:** Demo / correcciones de producto (aprobaciones-compras + tesorería). **No es Reu7 canónica.**  
**Fecha:** jueves 20/08/2026 · grabación 17:49:35  
**Participantes:** Sergio (Devint), Guadalupe / Lupe (Almahue), Mario (Almahue), Carlos Vallejos (Devint).  
**Nombrados sin hablar:** Francisca (tesorería, ~17:13). **No estuvieron:** Agustín, María Jesús / MJ.  
**Duración:** ~41 min (último timestamp 40:58).

**No confundir** con la reunión **interna de la mañana** del mismo día (solo Carlos + Sergio, video `105836`): [`reunion-2026-08-20-contraste-sergio.md`](reunion-2026-08-20-contraste-sergio.md).

| Fuente | Ubicación |
|---|---|
| Minuta Carlos | [`fuentes/reunion-2026-08-20-tarde-minuta-carlos.md`](fuentes/reunion-2026-08-20-tarde-minuta-carlos.md) |
| Transcripción verbatim tl;dv | [`fuentes/transcripcion-2026-08-20-tarde-lupe-mario.md`](fuentes/transcripcion-2026-08-20-tarde-lupe-mario.md) |
| Minuta auto tl;dv | [`fuentes/reunion-2026-08-20-tarde-minuta-tldv.md`](fuentes/reunion-2026-08-20-tarde-minuta-tldv.md) |
| tl;dv | https://tldv.io/app/meetings/6a877e1e644c1a00131f8046 |
| Video | `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-20 174935.mp4` (~1,12 GB; no git) |

**Regla de autoridad:** Lupe y Mario son **cliente operativo**. **No sustituyen** Reu6 (MJ/Agustín) cuando chocan. Esta minuta **alimenta backlog y preguntas**; no se implementa a ciegas (pedido 21/08: documentar, no codear).

Carlos y Sergio en sala = hipótesis / propuesta de diseño, salvo donde Lupe o Mario confirman.

---

## 1. Resumen ejecutivo

Dos paquetes, ahora con atribución de speaker (transcripción tl;dv 21/08):

1. **Compras + aprobaciones.** Lupe/Mario: la cadena es **solo compras** (servicios y materiales). El documento que emite Compras es la **orden de compra**; la cotización llega de otras áreas (correo/PDF) y **no** vive hoy en Microsoft ni se anexa. Factura recibida con OC no aprobada = **destacar + no contabilizar + no pagar**. Aceptación comercial SII a **8 días**: Lupe elige **dejar pasar** (auto-aceptar con trazabilidad), no rechazo automático. Hoy rechazan a mano en el SII.
2. **Tesorería.** Reordenar menú (**cartola primero**). Cartola = insumo de **conciliación** (falta RUT; hoy Lupe matachea a mano cliente + monto). Flujo de caja **por banco**, **CLP vs USD** (4 bancos, ej. Banco de Chile). **Propuesta** de saldo de apertura. Unificar **Pagos** (pago total / anticipo / anticipo productor con tipo de cambio). **Nómina semanal de pagos** sobre vencimientos de documentos recibidos: aplazar **compromiso interno** sin mutar el DTE; KPIs; solo egresos.

Operativo: error CAF/folio GoSocket (MJ subió un doc, error, Pablo sin respuesta); cadencia **martes y viernes**; próxima con **María Jesús**. Mario se queda con OC ficticias para probar cadenas.

---

## 2. Qué pidió el cliente (Lupe / Mario) vs qué propuso Devint

Citas de la transcripción. Lo de Sergio/Carlos **no** se trata como requisito hasta que Lupe/Mario (o MJ) lo confirmen.

### 2.1 Compras y aprobaciones

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| Aprobaciones solo compras (servicios y materiales) | «Sí, servicio y materiales, siempre de las compras… solo de compras.» / «Por compras, sí, correcto.» | Lupe 01:33–01:43 · Mario 08:21 | **Sí** |
| Doc inicial = OC; cotiz llega de afuera | «Nos llegan las cotizaciones, pero al tiro se genera la orden de compra y de ahí pasa aprobación…» Otras áreas hacen el procedimiento; Compras **solo genera la OC**. | Lupe 02:21, 05:32–05:48 | **Sí** |
| Cotiz no se anexa hoy | «Actualmente en Microsoft eso no pasa… No lo tenemos con cotización ni tampoco se anexa.» | Mario 03:39–03:46 · Lupe 03:44 | Hecho operativo |
| Referencia cotización en OC (tipo, folio, fecha), no obligatoria, **sin adjunto** | Propuesta Sergio 06:09–07:50; Mario: «Finalmente en PDF». | Sergio propone · Mario describe canal | **Backlog UX** (Sergio lo da por corrección; cliente no lo pidió como adjunto) |
| OC aprobada para contabilizar | «Debería ser que estuviese aprobada la orden de compra para que se pueda contabilizar.» | Lupe 10:27 | **Sí** |
| Factura con OC no aprobada: destacar, no pago, no asiento | Sergio ofrece rechazo auto **o** destacar. Mario: «no pasa ni a pago ni tampoco se contabiliza.» | Mario 11:55 | **Sí** (destacar + bloqueo; **no** rechazo auto) |
| 8 días SII | Sergio: ¿auto-aceptar a los 8 o rechazar día 7–8? Lupe: **«La primera opción.»** Hoy no usan rechazo automático; entran al SII a mano. | Lupe 12:34, 13:43 | **Sí**: esperar 8 días → aceptación automática + bitácora |
| Elegir aprobador individual en el eslabón | Carlos ofrece «tercera opción» y dice que hay que conversar alcance. Mario: primero **probar** con OC ficticias. | Carlos 00:05 · Mario 00:44 | **No cerrado.** tl;dv lo listó como action; no es acuerdo. |
| Cadena 1-de-N vs todos | Configurable; Lupe pregunta si con 1 de 2 ya se contabiliza. Respuesta: depende de la regla del eslabón; la OC no queda aprobada hasta cumplir la regla. | Lupe 09:15–10:27 · Sergio 10:35 | Configuración, alineada a diseño de grupos |
| OC ficticias para probar | Mario 00:48, 36:55 | Mario / Almahue | Operativo |

### 2.2 Tesorería

| Tema | Qué se dijo | Quién | ¿Pedido cliente? |
|---|---|---|---|
| Cartola primero en el menú | Carlos ofrece reordenar ciclo lógico; no hay objeción. | Carlos 25:38 | **Sí** (minuta Carlos + sala) |
| Lista de cartolas + «ojito» a pantalla de detalle (filtros fecha/monto/id) | Sergio 17:19; Lupe: «Sí, sería ideal.» | Lupe 18:00 | **Sí** |
| Import **completa** (no cherry-pick de líneas) | Carlos recuerda pedido MJ de seleccionar movimientos. Lupe: «se ingresa completa.» El problema es **contabilizar**: cartola trae **nombre**, no **RUT**. | Lupe 19:05 | Import completa = práctica Lupe. Selectivo = hipótesis MJ, no reabrir aquí. |
| Match banco ↔ factura | Hoy: ingreso **manual**. Criterio: maestro cliente + movimiento banco + **monto** de factura. Anticipo de cliente debe ir a ficha y **rebajar saldo**. Cartola sirve **para conciliar**. | Lupe 19:37–23:19 | **Sí** el problema; **algoritmo abierto** (Sergio se lleva el análisis 22:47) |
| Flujo de caja por banco + CLP/USD | 4 bancos; ej. Banco de Chile pesos y dólares; ver caja de cada uno. | Lupe 23:34–24:02 | **Sí** |
| Saldo inicial / apertura | Cartola trae saldo de cuenta. Mario: «saldo de apertura… que no se mueva… cuadrarse con la cartola.» | Lupe 25:10 · Mario 25:53 | **Propuesta a diseñar** |
| Unificar anticipos y pagos | «que se unifique, que quede solo pagos» y al ingresar marcar anticipo vs pago total. Tercer tipo: **anticipo productor** (misma data, se **mueve el tipo de cambio**). Auto 100%/parcial: Lupe acepta **si** se mantiene productor. | Lupe 26:44–29:33 | **Sí** |
| Nómina semanal, solo pagos | Vencimientos de **documentos recibidos**; vista, no carga. «este viernes… qué tengo para este viernes.» No recaudación. | Lupe 30:13–31:04 · Sergio 36:35 | **Sí** |
| Aplazar sin mutar el DTE | Lupe: factura contabilizada **no** se modifica; quiere sacarla de esta semana y verla en 3 semanas. Mario: asignar **semana de pago**; marcar días vencidos; **fecha contable de vencimiento no se edita**. Sergio propuso fecha compromiso en contabilización; Lupe: **no mezclar** tesorería con contabilidad (~36:06). Acuerdan: desde la lista, correr **compromiso de pago** a otra semana. | Lupe 33:51 · Mario 34:23 · Sergio 35:00 | **Sí** (aplazamiento interno) |
| KPIs nómina | Pagados / asignados / atrasados / adelantados (montos por semana). | Mario 36:22 | **Sí** |
| Anticipos en estado de cuenta 360 | Lupe pregunta si se ven en proveedor/cliente. Sergio cita lo hablado con MJ. Lupe: «eso quería ver.» | Lupe 39:00 · Sergio 39:15 | Cliente operativo + citar MJ |
| CAF / folios | MJ subió un doc, error, escribió a Pablo, sin respuesta. Proveedor atrasado con folios. Avisan por WhatsApp. | Lupe 37:48–38:16 | Operativo H11 |

---

## 3. Contraste con Reu6 / código (sin implementar)

| Pedido 20/08 tarde | Reu6 / diseño vigente | Lectura |
|---|---|---|
| Aprobaciones **solo compras** | D4: cadena OC + proformas + **comercial reservado**. Piloto local `comercialRequiereAprobacion` **ON** (OV). Mañana 20/08 (Sergio): OV también controla venta. | **Choque.** Lupe/Mario son operativos; no apagar piloto OV sin **MJ**. |
| Documento inicial = **OC** | D11: Cotización **Compras** → OC borrador. | **Parcialmente alineado.** OC es el doc de compra. **No borrar** Cotizaciones hasta que MJ diga que cotiz no vive en el ERP. Sala: cotiz es recibida (PDF/mail); referencia en OC **informativa**. |
| Referencia cotización opcional en OC | No era campo obligatorio | **Backlog UX** bajo riesgo. |
| Factura recibida + OC no aprobada: destacar + bloquear contabilizar/pago | Reu4 libro compras + asociar OC; no hay semáforo + bloqueo | **Backlog** coherente con control de gasto. |
| Auto-aceptación a 8 días | No es la cadena PIN. En Chile es **aceptación comercial** del DTE recibido (~8 días) vía partner. | **No** auto-aprobar la **OC**. Es flujo **C** (factura recibida + GoSocket) + bitácora. H11: sin CAF no hay SII live. |
| Elegir aprobador individual | D6 / `03-DISENO-GRUPOS-Y-ESCALAS`: cadena por grupo/escala; no elegir persona ajena. | Carlos lo ofreció; Mario pidió **probar** primero. **No codear.** Preguntar MJ. |
| Tesorería UX (cartola primero, ojito, banco, CLP/USD) | Módulo existe; demo tesorería no cerrada en Reu6 | **Backlog UX.** No contradice minutas. |
| Match cartola ↔ documentos (RUT) | Conciliación existe; H13 Excel banco fino pendiente MJ | **Diseño abierto** (Sergio se lo llevó). No codear algoritmo. |
| Unificar pagos + anticipo productor (TC) | Pantallas separadas; productor **no es maestro** (flag lookup) | Unificar UI = backlog. Anticipo productor + TC = producto nuevo; **no** inventar maestro Productor. |
| Nómina semanal + aplazar interno | Cobranza R4-18 era **propuesta** (mail). Esto es **nómina de pagos** (egresos), no recaudación. | Backlog tesorería. |
| CAF / «CAP» / folio | H11 fail-closed | Hecho técnico. |

---

## 4. Tres flujos que no hay que mezclar

La minuta de Carlos («aprobar automáticamente facturas a 8 días») se lee fácil como auto-PIN de OC. En transcripción va junto a **GoSocket, SII, aceptaciones y reclamos**.

| Flujo | Documento | Quién | Efecto pedido en sala |
|---|---|---|---|
| A | Orden de compra | Grupos/escalas + PIN | Autoriza comprar. Hasta cumplir la regla del eslabón, la OC **no** está aprobada. |
| B | Factura de proveedor (recibida) referenciando OC | Si A no está cerrado → **destacar + no contabiliza + no paga** | Control. **No** rechazo automático (Lupe). |
| C | Aceptación comercial SII (~8 días) | Partner GoSocket; si nadie reclama, queda aceptada **con trazabilidad** | Tributario. Lupe: **esperar** los 8 días. **No** es el PIN de la OC. |

Implementar C como «la OC se aprueba sola a los 8 días» sería un error de producto.

---

## 5. Tesorería — pedidos y huecos de diseño

### 5.1 Menú / cartolas

- Orden lógico: **cartola → conciliación → flujo de caja → pagos → nómina**.
- Lista de importaciones + **ojito** a pantalla completa de detalle (buscador, fecha, monto, id movimiento). Sergio: no levantar un módulo extra.
- Import **completa** según Lupe. Selectivo de líneas = recuerdo de Carlos sobre MJ; no tratarlo como pedido de esta sala.
- Al contabilizar el movimiento: hoy se ve **nombre**; falta **RUT**.

### 5.2 Conciliación (propuesta, no algoritmo cerrado)

Pedido: match **ingreso banco ↔ factura de venta** y **egreso banco ↔ compra**. Práctica actual de Lupe: **cliente + movimiento + monto**, uno a uno; anticipo de cliente rebaja saldo en ficha. Cartola en sistema = para **conciliar**.

Sergio se llevó el análisis de cómo enlazar carga + conciliación (~22:47). No hay regla única acordada (¿folio?, ¿RUT+monto+fecha?, ¿sugerencia + confirmación humana?).

### 5.3 Flujo de caja

- Saldo **por banco** (caja en cada cuenta).
- Desglose **peso y dólar** por banco (4 bancos; ejemplo Banco de Chile).
- Cartola trae ingresos, egresos y **saldo de cuenta**. Lupe: hay saldo inicial y los movimientos mueven el flujo. Import sirve **conciliación y flujo**.
- **Saldo de apertura:** Mario pide un monto que **no se mueva** y se cuadre con cartola. No hay fórmula cerrada (¿primera cartola vs asiento de apertura vs ambos?).

### 5.4 Pagos unificados

Una sola vista **Pagos**. Al registrar egreso:

| Tipo | Criterio en sala |
|---|---|
| Pago total | Imputación = 100% de la factura (Sergio propone auto; Lupe acepta) |
| Anticipo | Monto &lt; factura; o selección explícita al ingresar |
| Anticipo productor | Misma información; se **manipula tipo de cambio**. Lupe: «sacar todo lo de productores.» |

Anticipos se ven además en ficha / estado de cuenta 360 (Sergio cita a MJ).

### 5.5 Nómina de pagos (no recaudación)

- Fuente: **vencimientos de documentos recibidos**.
- Granularidad: **semana** (no carga manual de filas).
- **Aplazar:** cambia **compromiso de pago interno** / semana asignada; **no** altera fecha de vencimiento del DTE ni el asiento.
- UI: destacar aplazadas y vencidas, filtros, días respecto del vencimiento original («lleva 10 vencidas»).
- KPIs arriba: pagados / asignados / atrasados / adelantados (montos por semana).
- No editar vencimiento contable desde acciones de fila (Carlos lo ofreció ~31:27; Sergio y Mario lo descartan).
- No agregar «fecha compromiso» en la contabilización si eso mezcla tesorería con contabilidad (Lupe 36:06). El aplazamiento vive **en la nómina**.

---

## 6. Action items (corregidos contra la transcripción)

tl;dv asignó de más. Lo que sigue cruza minuta Carlos + speakers.

| # | Acción | Dueño | ¿Producto ahora? |
|---|---|---|---|
| 1 | OC ficticias para probar cadenas | Mario / Almahue | Operativo |
| 2 | Campo referencia cotización (tipo, folio, fecha) opcional en OC, sin adjunto | Sergio lo comprometió en sala | Backlog UX bajo riesgo |
| 3 | Aprobador «individual en eslabón» | Carlos lo ofreció | **Diseño** vs D6; Mario pidió prueba primero; no codear hasta MJ |
| 4 | Semáforo factura recibida si OC no aprobada + bloqueo contabilizar/pago | Cliente (Mario/Lupe) | Backlog; alinear con libro compras |
| 5 | Aceptación 8 días + bitácora vía GoSocket (esperar, no rechazar auto) | Lupe eligió opción 1 | H11 + partner; **no** auto-PIN OC |
| 6 | Tesorería: cartola primero; lista + ojito a detalle; buscador/filtros | Lupe «ideal» + minuta Carlos | Backlog UX |
| 7 | Columna/filtro banco + CLP/USD; **propuesta** saldo de apertura | Lupe + Mario | Backlog + diseño saldo |
| 8 | Unificar pagos/anticipos + 3 tipos (productor = TC) | Lupe | Backlog; productor sin maestro |
| 9 | Nómina semanal, aplazar compromiso interno, KPIs | Lupe + Mario | Backlog tesorería; Carlos debe **proponer** (~36:49) |
| 10 | Análisis match cartola ↔ conciliación (ingreso/venta, egreso/compra) | Sergio se lo llevó | Diseño; no codear algoritmo |
| 11 | Confirmar «mañana» (21/08) versión demo (desfase prod; **sin** estas correcciones) | Carlos 37:10 | Operativo |
| 12 | WhatsApp cuando CAF/folios / error Pablo esté resuelto | Lupe | H11 |
| 13 | Ritmo mar/vie; invitar a MJ | Mario / Almahue | Agenda |

---

## 7. Preguntas para MJ / Agustín (próxima con María Jesús)

1. ¿Se **apaga** la cadena de **OV / comercial**, o solo se enfatiza compras en la demo y el piloto D4 sigue?
2. ¿El ERP **deja de persistir cotizaciones** de compras (solo PDF/mail) o se mantiene Cotizaciones → OC (D11) con referencia opcional?
3. Factura recibida sin OC / con OC no aprobada: ¿solo destacar, o **bloqueo duro** de contabilizar y de nómina? (Mario dijo ambos.)
4. Los 8 días: ¿aceptación comercial SII (GoSocket) tal cual Lupe (esperar), u otra regla interna?
5. ¿El eslabón permite **elegir persona del grupo** o sigue el grupo/escala? (Carlos lo ofreció; no cerrado.)
6. Import de cartola: ¿siempre completa (Lupe) o selectiva de líneas (recuerdo Carlos de MJ)?
7. Saldo inicial de flujo de caja: ¿primera cartola, saldo de apertura contable, o ambos?
8. Anticipo productor: ¿misma contraparte con flag `esProductor`, u otra entidad? ¿El 360 de estado de cuenta es el de MJ?
9. Nómina: ¿el compromiso de pago vive solo en tesorería, sin campo extra en el asiento? (Lupe no quiere mezclar.)

---

## 8. Qué no hacer con este documento

- No llamarlo **Reu7** ni ponerlo por encima de Reu6.
- No quitar Cotizaciones→OC ni apagar `comercialRequiereAprobacion` porque «la sala lo dijo».
- No implementar match bancario, nómina ni tres tipos de pago hasta el siguiente encargo de código.
- No tratar el video de la **mañana** (Sergio) como esta sesión: allí se **reabría** cotiz vs OC; aquí el cliente operativo dice **OC primero**. Sigue haciendo falta MJ para cerrar D11.
- No copiar el MP4 a git (~1,12 GB).

---

## 9. Video (registro)

Verificado en disco el 21/08/2026.

| Campo | Valor |
|---|---|
| Nombre | `Screen Recording 2026-08-20 174935.mp4` |
| Ruta | `C:\Users\c\Videos\Screen Recordings\` |
| Bytes | 1 120 825 537 (~1,12 GB) |
| Fecha archivo | 20/08/2026 17:49:35 |
| Git | No (`.gitignore` de `fuentes/videos/*.mp4`) |
| ASR | Transcripción **tl;dv** ya versionada en `fuentes/`. Whisper local no hace falta salvo contraste. |
