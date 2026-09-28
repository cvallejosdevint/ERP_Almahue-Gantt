# Tesorería 28/08 + GoSocket — análisis desde transcripción

**Regla de fuente aplicada:** manda la transcripción verbatim de `fuentes/`. Las minutas generadas por IA solo sirven de índice. Cliente (MJ, Lupe, Fran, Mario, Agustín) = **requisito**. Devint (Carlos, Sergio) = **propuesta**. Pablo Rodriguez / GoSocket = **tercero**.

**Advertencia de citación — léela antes de usar los timestamps:**

| Fuente | ¿Verbatim? | ¿Timestamps? | Cómo cito aquí |
|---|---|---|---|
| `fuentes/transcripcion-2026-08-28-tesoreria-mj-lupe.md` | Sí | **No.** Los 224 segmentos vienen con marca vacía `[]` | Por **línea de archivo** (`L###`). No inventé minutos |
| `fuentes/transcripcion-reunion-gosocket-qa.md` | Sí | Sí, `[MM:SS]` | Timestamp real |
| `reunion-2026-09-01-gosocket-kickoff.md` | No, minuta Devint de la mesa API | No | Como **secundaria** (`K-n`), marcada |
| `reunion-gosocket-minuta-2026-08.md` | No, minuta derivada del verbatim | No | Solo cuando el verbatim la respalda |

**Segunda advertencia — diarización del 28/08.** La cabecera del archivo lo dice: «La voz de Carlos no quedó en el audio; speakers son del lado Almahue + eco Devint». Los hablantes están anonimizados (`Speaker 00/01/02`) y el reparto **se cruza en varios tramos**. Mi lectura por contenido y contexto:

- **Speaker 01 = María Jesús (MJ)** — cliente, jefa de contabilidad; es quien comparte pantalla de Agrosoft.
- **Speaker 02 = Lupe (Guadalupe)** — cliente, tesorería; habla de anticipos a productores y nómina.
- **Speaker 00 = Sergio (Devint)** — proveedor; además narra y repite en voz alta lo que Carlos hace en pantalla.

Casos donde la etiqueta está claramente mal y **no** debe usarse para atribuir requisitos: L270–L272 aparece como Speaker 00 pero el contenido es de MJ («no tiene sentido que lo veáis por banco»); L112 de Speaker 02 trae basura de ASR («los movimientos de nosotros contra Iglesia»). Marco cada cita afectada. **Fran no tiene ninguna intervención identificable**; MJ solo la menciona como presente (L36).

---

## Ficha (una por sesión)

### S1 — Tesorería 28/08/2026 (verbatim, sin timestamps)

| Campo | Valor |
|---|---|
| Archivo | `fuentes/transcripcion-2026-08-28-tesoreria-mj-lupe.md` (224 segmentos, 458 líneas) |
| Origen | tl;dv `6a91a445564eaa0013e057cd` — grabación 2026-08-27 17:21 |
| Cliente presente | María Jesús (todo), Lupe (todo), Fran (presente, sin intervención identificable), Mario (llega tarde, L230; se va antes, L316) |
| Devint | Sergio (voz), Carlos (comparte pantalla, **sin audio en la grabación**) |
| Formato | Devint muestra el ERP nuevo; MJ comparte **Agrosoft** en pantalla para explicar el as-is |
| Cierre | Sergio: «todo lo que se va a avanzar, lo que los ajustes que nos mencionaron acá, se va a crear como tarjeta para que ustedes también las puedan ir validando en línea durante la semana» (L452). Próxima sesión: jueves siguiente |
| Peso | Es la sesión **más reciente con el cliente sobre tesorería** y funciona como ToDo maestro del módulo |

### S2 — GoSocket QA onboarding (verbatim, con timestamps)

| Campo | Valor |
|---|---|
| Archivo | `fuentes/transcripcion-reunion-gosocket-qa.md` (~30 min) |
| Fecha | agosto 2026, post-Reu6; transcripción entregada 19/08. **Fecha exacta no confirmada en la fuente** |
| GoSocket | Pablo Rodriguez (consultor Chile) |
| Cliente | María Jesús, Mario |
| Devint | Carlos Vallejos |
| Mencionados | Cristian (contrato), Sergio, Nico (representante legal / certificado) |
| Contenido | Portal sandbox, enrolamiento, certificado, CAF/folios, API keys, lectura de errores, PDF |
| Nota ASR | «Cuba» = **QA**; «CUAA» = **CAF**; «IOFaktura / Yo Facturo / IO Facturo» = **IOFactura** |

### S3 — Kickoff GoSocket 01/09/2026 (minuta Devint, **no verbatim**)

| Campo | Valor |
|---|---|
| Archivo | `reunion-2026-09-01-gosocket-kickoff.md` |
| Tipo | Mesa API GoSocket 14213, ~38 min, ~16:00 UTC |
| Participantes | Pablo Rodriguez (GoSocket), Carlos, Sergio; invitados Mario, Vanessa Adams, Cristian Zúñiga. **MJ no se conectó** (estaba en el contrato) |
| Contenido | Campos obligatorios del canónico, `BillerId`, `DefaultCertificate`, resolución SII (CAE), lectura de la respuesta API |
| Salvedad | Es minuta, no transcripción. La uso para datos operativos concretos y la marco `K-n`. **Sin cliente presente** → nada de aquí es requisito de cliente |

### S4 — Minuta onboarding GoSocket agosto (derivada de S2)

| Campo | Valor |
|---|---|
| Archivo | `reunion-gosocket-minuta-2026-08.md` |
| Tipo | Minuta estructurada del mismo evento que S2 (`GOS-1`…`GOS-17`) |
| Uso | Índice. Verifiqué que `GOS-1` a `GOS-17` **sí** están respaldados por el verbatim S2. Su addendum 19/08 no viene de la llamada: es estado de código |

---

## Tesorería: cómo trabaja hoy MJ / Lupe

Todo este bloque sale de que MJ compartió Agrosoft en pantalla (L158 en adelante). Es el **as-is**, no el pedido.

**Cartola bancaria.** Hoy la cartola se **digita a mano** en Agrosoft, y por eso MJ quiere invertir el flujo: «no tendríamos que estar ingresando además la cartola manualmente, sino que cargaríamos el archivo del banco y ahí cada movimiento le iríamos contabilizando encima de la cartola» (MJ, L194).

**Bancos y monedas.** «Trabajamos con 2, pero cada banco tiene dólar y peso, y hay uno que tiene yuan. Son 3 bancos, 4» (MJ, L212). O sea: dos instituciones, cuatro cuentas por combinación banco+moneda. Lupe: «necesito saber qué saldo tiene la cuenta dólar. Lo mismo con la de yuan, porque también trabajamos con el banco en yuan. Y en peso» (L254).

**Pago a proveedores (Agrosoft).** MJ demuestra el circuito: entra a pago de proveedores, elige el documento pendiente, indica banco, y «aquí pongo el código financiero para que después se me vaya el flujo de caja… Y yo lo contabilizo. Se me genera el egreso al estar en el módulo de tesorería y se me hace el asiento contable de que disminuye el banco y disminuye el proveedor» (L162). El comprobante «se hace automático si yo ingreso directamente en el módulo de tesorería» (L166).

**Plan de cuentas de proveedores.** Ante la pregunta de Sergio sobre si cada proveedor tiene cuenta propia: «No, es la cuenta de proveedores, que es la 21040001. Lo que se diferencia es el auxiliar y el tipo de documento nomás» (MJ, L172). Cuenta única + auxiliar + tipo de documento.

**Anticipos.** Si la factura no está ingresada, hoy el anticipo **no** se registra en tesorería: «ahí yo tengo que ingresarlo por el módulo de contabilidad y ponerlo como un anticipo al proveedor… acá pongo la cuenta banco disminuyendo el haber y el anticipo aumentando al debe» (MJ, L174 y L184). Ese doble ingreso (anticipo por un lado, comprobante por otro) es justamente lo que quieren eliminar: Sergio lo resume «no tendría que estar registrando anticipo y comprobante por separado» (L192) y MJ lo confirma.

**Anticipos a productores — el caso duro.** Lupe: «los anticipos de los productores siempre se trabaja en dólar, ya, porque así es su contrato. Pero yo igual hay veces en que les pago en pesos, pero tengo que ver reflejado el monto en dólar, y ahí es donde yo manipulo el tipo de cambio» (L68). El calce llega meses después: «va a llegar un momento en que ellos me van a facturar y debo calzar» (L72). Y a los productores «al final se liquidan al final de la temporada» (MJ, L178).

**Conciliación bancaria.** Concepto de MJ, importante porque redefine la pantalla: la cartola sola **no** concilia nada útil, «solamente concilia la cuenta banco… porque obviamente la cartola no tiene la asignación de qué, si es pago a facturas y anticipos y traspaso, préstamo, nada» (L142). Su definición operativa de mes conciliado: «al estar toda la cartola contabilizada, se da por conciliado el mes» (L190).

**Flujo de caja.** Se alimenta del **código financiero**, no de una parametrización aparte: «actualmente nosotros en el código financiero alimentamos el flujo de caja. Cuando nosotros hacemos cualquier movimiento bancario, uno de los requisitos es ingresar el código financiero, y con el código financiero nosotros parametrizamos el flujo de caja» (MJ, L316).

**Tipo de cambio.** Agrosoft ya llama al Banco Central: «esto es la llamada del Banco Central que hacen de este sistema. Entonces, por ejemplo, todas las mañanas se actualiza esto» (MJ, L352). Pero el sistema trae UF/UTM/IPC, que a MJ no le sirven: «yo no ocupo la UF, la UTM, el IPC. Entonces, al final, para mí son datos vacíos. A mí lo que me importa es el tipo de cambio dólar, y en este caso yuan, y en un futuro también va a ser euro» (L352).

**La tercera moneda vive en Excel.** «Actualmente la controlamos en un Excel, un Power BI, pero la idea es que toda la información salga del sistema. Por eso este ERP nos quedó limitado, porque nosotros acá nos dijeron que no podíamos tener triple moneda» (MJ, L344). «Este ERP» = **Agrosoft**. Y el histórico está incompleto: «Nosotros actualmente tenemos el tipo de cambio peso y dólar, lo que no tenemos yuanes» (L330).

**Nómina de pagos.** Lupe trabaja por semana pero necesita mirar lejos: «yo tengo facturas que se pagan, suponte, estamos ahora en agosto y se pagan en diciembre… sobre todo con las facturas de materiales, que con ellas tenemos un crédito de hartos meses» (L380). Y el vencimiento del documento no le basta: «me va a aparecer en 6 meses, pero la fecha no corresponde. Por eso necesito ver las otras semanas» (L388).

**Estado de cuenta.** Hoy es un trabajo manual de cruce: «tenemos casos de que hay RUT que son cliente y proveedor. Entonces, cuando queremos compensar las cuentas, nos complica un poco porque tenemos que ir al módulo de clientes, ver qué movimientos tienen clientes, ir al módulo de proveedores y ver para dónde tenemos que hacer la compensación» (MJ, L426). Y el reporte de calces existe pero es malo: «te aparece el comprobante en un lado, después te aparece con qué se calzó en otro lado. Entonces al final igual es un seguimiento muy arcaico» (L450).

**Migración.** Devint pide la data histórica; MJ ofrece la sábana de Agrosoft, «como unos 19.000» registros en Excel, «viene con todo lo que está diciendo la gestión, el código financiero, la cuenta contable que están usando. Comprobante, más bien el tipo cambio» (L360 — segmento con diarización cruzada, la oferta es del lado Almahue).

---

## Requisitos del cliente en tesorería

Columna «¿parece implementado?» contrastada contra `qa/resultados/2026-09-02-tesoreria-t1-t6.md` (40 PASS / 0 FAIL / 3 BLOCKED / 5 SKIP) y contra el schema Prisma. No re-ejecuté QA.

| # | Requisito | Quién | Ref | Cita textual | ¿Dato duro o preferencia? | ¿Parece implementado? |
|---|---|---|---|---|---|---|
| T-01 | Subir la cartola del banco y **contabilizar cada movimiento encima de la cartola** | MJ (cliente) | L124 | «lo ideal sería que nosotros podamos subir la cartola y que cada movimiento de la cartola lo podamos contabilizar» | **Dato duro** — redefine el módulo | **Sí.** T2-2 PASS: asiento origen `CARTOLA:{movId}` |
| T-02 | Contabilización **1 a 1**, sin lotes | MJ (cliente) | L154 | «Sí, contabilización uno a uno» | Dato duro | **Sí.** T2-2 PASS «1:1 dos líneas»; T2-5 rechaza el segundo intento |
| T-03 | Al contabilizar: elegir **contracuenta** y si el banco va al debe o al haber | MJ (cliente) | L134 | «asignarlo a lo que es si se mueve al debe o al haber, por el lado del banco. Y ahí se podría desplegar quizá una ventanilla donde uno pueda poner a la cuenta contable que lo va a cargar… que sea la contracuenta del asiento» | Dato duro | **Sí.** T2-2 PASS: Ingreso = debe banco, Egreso = haber banco |
| T-04 | Identificar el destino por **tipo + número de documento**, y que calce solo contra el módulo de proveedores | MJ (cliente) | L146 | «poner como la cuenta contable, tipo de documento, el número de documento… por ejemplo, 33, y la factura 1, de tal proveedor se va igual a calzar internamente en el módulo de proveedores» | Dato duro | **Sí.** T2-3 PASS: `lookup-documento?folio=…&sentido=…` |
| T-05 | Si el documento **no existe**, el movimiento va como anticipo y calza después, al ingresar la factura | MJ (cliente) | L148, L150 | «Y ahí, si no existe el documento… tiene que ir anticipo» / «después se ingresa la factura, igual se va a calzar en el momento que nosotros ingresemos la factura» | Dato duro | **Sí.** T2-4 PASS: «Si no hay documento, elige Anticipo» |
| T-06 | La cartola **no queda lista** hasta estar 100% contabilizada | MJ (cliente) | L218 | «mientras la cartola no esté completamente contabilizada, no te va a aparecer como lista… Te va a aparecer siempre pendiente» | Dato duro | **Sí.** TES-CART-6 PASS: cerrar con pendientes → HTTP 400 |
| T-07 | Conciliación = filtrar los movimientos que faltan por contabilizar | MJ (cliente) | L222 | «si queremos filtrar, por ejemplo, por los pendientes, vamos a ver al tiro cuáles son los movimientos que faltan por contabilizar» | Dato duro | **Sí.** TES-CON-1 PASS: CONCILIADOS 3 / PENDIENTES 69 |
| T-08 | **TC editable** en anticipo de productor, tantas veces como haga falta | Lupe (cliente) | L76 | «yo necesito que quede, una vez que yo ingrese el anticipo de productor, poder modificar el tipo de cambio… voy a tener como 10 anticipos en temporada y van a ser todos con diferente tipo cambio que yo les voy a dar» | **Dato duro** | **Sí.** T1-5 PASS: PUT TC 980, monto intacto |
| T-09 | Editar el TC **no** mueve el saldo del banco ni el monto | MJ (cliente) | L322 | «Del banco nunca se va a mover, no va a influir el tipo de cambio… Lo único que te cambia es lo que le aparece al productor para poder calzar en el día de mañana con una factura en la liquidación» | **Dato duro** — regla contable | **Sí.** T1-5 PASS: monto 15000 intacto; editar monto → 400 |
| T-10 | Toda edición con **registro de usuario** | MJ (cliente) | L104 | «yo dejaría que todo quedara con registro, todo lo que se haga en el sistema quede con registro de usuario» | Dato duro en TC; **preferencia amplia** en «todo» | **Parcial.** T1-4 PASS: `/pagos/:id/tc-eventos` con usuario. **No hay bitácora transversal**: no existe modelo de auditoría global en el schema |
| T-11 | TC del día automático, del **Banco Central**, para que todo quede en triple moneda | MJ (cliente) | L316 | «necesitábamos que el sistema llamara los tipos de cambio al Banco Central, porque la idea es que todos los movimientos queden en triple moneda… ahora nos urge la triple moneda» | **Dato duro** y marcado urgente | **Parcial — ver hueco G-1.** `IndicadorBc` tiene `usd/eur/cny` y `origenSync: manual\|auto`, pero **no hay ningún `@Cron` ni `ScheduleModule` en el backend**. T4-3 PASS es **import manual** CSV/Excel |
| T-12 | Que **toda** la contabilidad se pueda ver en las 3 monedas al TC de su fecha | MJ (cliente) | L314 | «la idea es que toda la contabilización de todo el sistema tenga las 3 conversiones… el mismo movimiento que está en pesos yo lo puedo ver en dólar al tipo de cambio del 27 de agosto y lo puedo ver en yuanes al tipo de cambio del 27 de agosto» | **Dato duro** | **No, a nivel de asiento — ver hueco G-2.** `Asiento.lineas` es JSON `[{debe, haber, cuentaId?, glosa?}]`: sin TC ni monto en otra moneda. La triple moneda vive en `Pago` y en flujo de caja, no en el mayor |
| T-13 | 95% de la contabilidad con TC histórico de la fecha; solo el productor se edita | MJ (cliente) | L324 | «el 95% de la contabilidad va a quedar con el tipo de cambio histórico de la fecha en que se realizó. Lo único que se va a poder modificar, el tema de los productores» | Dato duro | **Sí.** T4-2 PASS: no productor toma BC; `ANTICIPO_PRODUCTOR` con `tcManual=777` no se pisa |
| T-14 | Fecha no hábil → usar TC anterior | MJ (cliente), implícito en el diario | L326 | «todos los movimientos, si se está llamando del tipo de cambio del Banco Central diario, si nosotros ingresamos un movimiento el lunes, queda el tipo de cambio del banco del lunes» | Dato duro | **Sí.** T4-1 PASS: domingo 2026-06-14 usa hábil anterior |
| T-15 | Flujo de caja filtrado **por moneda, no por banco** | MJ (cliente) | L266 | «el flujo de caja lo que quieren filtrar es si el movimiento se hizo en dólar o se hizo en peso. Pero no si se hizo por qué banco, porque el flujo de caja al final es la suma de todos los bancos» | Dato duro | **Sí.** T3-1 PASS: chips Todas / CLP / USD / Yuan |
| T-16 | Saldos **por banco y por moneda**, sin conversión forzada | MJ (cliente) | L302 | «lo que habría que hacer es dejar los saldos, pero por tipo de moneda. Claro, que el Banco Chile en pesos tenga su saldo, en dólares su saldo, y en yuanes su saldo» | Dato duro | **Sí.** `MovimientoCaja` indexa `[empresaId, banco, moneda]`; T3-4 PASS: equivalente CLP **OFF** por defecto |
| T-17 | Flujo de caja es **solo lectura**: no se edita ni se borra | MJ (cliente) | L258 | «No, porque el flujo de caja es directamente los movimientos del banco» | Dato duro | **Sí.** T3-1 PASS «Solo visualización»; T3-3 PASS: PUT apertura → 400 |
| T-18 | Saldo de apertura por banco/moneda | Mario (cliente), vía MJ | L244–L254 | Mario pregunta por el saldo; Lupe: «necesito saber qué saldo tiene la cuenta dólar. Lo mismo con la de yuan» | Dato duro | **Sí.** TES-CAJ-1 PASS: apertura inmutable, una por banco+moneda |
| T-19 | Nómina: renombrar a **«Nómina semanal de pagos»** | Lupe (cliente) | L392 | «eso ahí de egresos podría decir nómina semanal de pagos nomás» | Dato duro (literal) | **Sí.** T5-1 PASS: H1 exacto |
| T-20 | Poder navegar a semanas futuras, por año y mes | Lupe (cliente) | L388, L398 | «me va a aparecer en 6 meses, pero la fecha no corresponde. Por eso necesito ver las otras semanas» / «así por mes, y ahí yo selecciono la semana» | Dato duro | **Sí.** T5-1 PASS: Año → Mes → Semana (S1–S5 futuras) |
| T-21 | Exportar la nómina del periodo | Lupe (cliente) | L396 | «yo voy a poder exportar solo lo que, lo de la semana, no, del periodo» | Dato duro | **Sí.** T5-3 PASS: CSV y Excel |
| T-22 | Aplazar un pago a otra semana | Lupe (cliente) | L378–L380 | Sergio propone mover a otra semana; Lupe: «Sí, se ocurre» | Dato duro (confirmado por cliente) | **Implementado, no probado.** T5-4 **BLOCKED**: no hay documentos POR_PAGAR por la deuda P0-1 |
| T-23 | Estado de cuenta **por RUT**, sin eje cliente/proveedor | MJ (cliente) | L420 | «el estado de cuenta debería hacer el filtro de lo que nosotros queramos buscar… pusiéramos LM y nos saliera si tiene anticipos, si tiene pagos, está como cliente, como proveedor» | **Dato duro** | **Sí.** T6-1 PASS: «Kardex unificado por RUT», filtro Todos\|Pendientes |
| T-24 | Quitar el detalle de abajo; el detalle sale al filtrar el RUT | MJ (cliente) | L430 | «en esta vista yo eliminaría el detalle que está abajo y solamente dejaría para poder filtrar el RUT que quiero ver» | Dato duro | **Sí.** T6-2 PASS |
| T-25 | Un mismo RUT cliente **y** proveedor, para compensar | MJ (cliente) | L426 | «tenemos casos de que hay RUT que son cliente y proveedor… tenemos que ir al módulo de clientes… ir al módulo de proveedores» | **Dato duro** | **Implementado, no probado.** T6-3 PASS pero con `dual=false`: **no existe en EMP-EXPORT un RUT que sea ambos**. Falta el dato, no el código |
| T-26 | Filtro Pendientes / Histórico | MJ (cliente) | L442 | «debiese aparecer solamente si yo quiero poner como, no sé, consulta histórica o solo pendientes» | Dato duro | **Sí.** T6-2 PASS |
| T-27 | Abrir una factura calzada y ver **con qué** se calzó | MJ (cliente) | L444 | «si la factura está, aparece calzada, yo pueda apretar la factura y ahí se me despliegue la ventanilla de con qué anticipo se calzó o en qué comprobante se calzó» | Dato duro; motivo: «un seguimiento muy arcaico» (L450) | **Parcial.** T6-2 PASS pero anota «Calces en API (`calces[]` tipo PAGO)» — el despliegue inline en UI no está evidenciado. **Verificar** |
| T-28 | Migrar histórico de Agrosoft (~19.000 registros) con TC, código financiero y cuenta | MJ (cliente) ofrece; Devint pide | L358–L360 | «viene con todo lo que está diciendo la gestión, el código financiero, la cuenta contable que están usando. Comprobante, más bien el tipo cambio» | Dato duro; **alcance abierto** (Sergio menciona «desde 5 años… la información del 2019», L328) | **No — hueco G-3.** No hay importador de histórico contable. El TC histórico de **yuan no existe ni en Agrosoft** (L330) |

### Huecos que destaco

- **G-1 — no hay sync automático con el Banco Central.** MJ dijo «nos urge» (L316) y describió que Agrosoft ya lo hace todas las mañanas (L352). El ERP tiene el campo `origenSync: manual | auto` en `IndicadorBc`, pero cero jobs programados en el backend. Hoy alguien tiene que importar el CSV a mano. **Es una regresión funcional respecto de Agrosoft.**
- **G-2 — la triple moneda no llega al asiento contable.** T-12 pide que *cualquier* movimiento se lea en las 3 monedas. Está resuelto en pagos y en flujo de caja, pero `Asiento.lineas` no guarda TC ni importe convertido, así que libro diario, mayor y balance siguen siendo monomoneda. Es el requisito de tesorería del 28/08 con mayor distancia entre lo pedido y lo construido.
- **G-3 — migración histórica sin diseño.** MJ ofreció la sábana; no hay importador, ni definición de alcance (¿2019? ¿5 años?), ni TC yuan histórico de dónde sacarlo.
- **G-4 — bitácora transversal.** T-10 pedía registro de usuario para «todo lo que se haga en el sistema». Existe solo para TC de pagos.
- **G-5 — códigos financieros.** El flujo de caja se alimenta de ellos (L316) y QA anotó que el combo no muestra el catálogo Reu porque llega con `activa=null`. Es dato + filtro de UI, no diseño.

---

## Frontera ERP ↔ GoSocket

Tabla construida **solo** con lo dicho por Pablo (GoSocket) en S2 verbatim, más los datos operativos de S3 (minuta, marcados). Nada aquí es inferencia mía salvo donde lo digo.

| # | Responsabilidad | ¿ERP o GoSocket? | Evidencia |
|---|---|---|---|
| F-01 | **Solicitar los folios al SII** y obtener el archivo CAF | **Almahue (MJ)** — ni ERP ni GoSocket | Pablo [26:58]: «acá en el servicio Impuesto Interno, en la opción de CUAA \[CAF], cierto, está la opción de solicitar folios… te van a entregar un archivo CAF» |
| F-02 | **Cargar el CAF en el portal** GoSocket | **Almahue (MJ)**, manual en QA | Pablo [26:58]: «María, necesitamos cargar los CAF… Inbox… gestión de folios… Tú lo arrastras a este lugar… y con eso le das a cargar» |
| F-03 | Recarga de folios cuando se agotan | **Almahue (MJ)**, avisada por Devint | Pablo [28:31]: «Si en algún momento, Carlos, el API te entrega como mensaje de error de que no existe el rango de folio o el rango de números, es porque le falta folio y lo tienes que ver con María para que te cargue nuevos folios» |
| F-04 | Folios **en producción** | **GoSocket, automáticos** | Pablo [07:35]: «Recuerden que en QA, por el tema de los folios, María, como dan muy poquitos, lo ideal es que los carguemos manual. Ya en productivo serán automáticos» |
| F-05 | **Asignar el folio** al documento emitido | **GoSocket** | S3 `K-4` (minuta): Pablo quitó el `BillerId` y «el asignador de folio no encuentra rango CAF» → `GlobalDocumentId` 0 |
| F-06 | **Cargar el certificado digital** | **Almahue (MJ)** en el portal | Pablo [24:16]: «Acá tienen que cargar el certificado digital del representante legal o de la persona que va a firmar los documentos» |
| F-07 | Que el certificado tenga **permiso de firma en el SII** | **Almahue (MJ)** | Pablo [24:16]: «El certificado que esté agregado acá también tiene que estar como usuario en el servicio Impuesto Interno con el permiso de firma. Bien, sin eso el servicio nos va a indicar de que el usuario no tiene permisos para emitir» |
| F-08 | Distinción certificado de RL vs certificado firmante | **Almahue** decide | Pablo [25:29]: «el certificado digital del representante legal nosotros lo necesitamos solamente para modificar la información de la empresa… más que nada tiene que ser el certificado de un usuario firmante». Y [26:12]: «el certificado digital del representante legal es, no precisamente tiene los permisos de firma, ojo con eso» |
| F-09 | **Firmar** el DTE | **GoSocket**, con el certificado cargado | Se deduce de F-06/F-07 + S3: «TED `RR`/`MNT`/`IT1` se arman solos si eso va lleno». **Pablo no lo enuncia literalmente**; lo marco como inferencia sólida, no cita |
| F-10 | **Armar el XML final** conforme al XSD del SII | **GoSocket**, por XSLT | Pablo [07:35]: «El proceso de la API es que ustedes envían el request, este request se transforma por medio de un XSLT, de un mapeo» |
| F-11 | **Contenido del request** (canónico): Acteco, resolución, RUT y razón social del receptor, montos, detalle | **ERP** | S3 «Campos que el servicio pidió»: fecha y número de resolución, dirección de origen, razón social del receptor, RUT del receptor, monto total, monto de ítem |
| F-12 | **Número y fecha de resolución SII** (CAE) | **ERP los envía**; el dato lo aporta Almahue | Pablo [07:35]: «un error de carátula generalmente se ocasiona cuando no se informa correctamente la resolución, el número de resolución y la fecha de resolución en los documentos que están emitiendo». S3 `K-3` los hace obligatorios y da los valores |
| F-13 | `BillerId` por sociedad | **ERP** (`Empresa.gosocketBillerId`, Admin › Empresas) | S3 `K-1`: «BillerId por sociedad: Admin › Empresas (no en el gateway)» |
| F-14 | **Enviar el DTE al SII** | **GoSocket** | Pablo [24:16] habla de que «el servicio nos va a indicar» el rechazo; el manual API expone `SendDocumentToAuthority`. Cita directa de envío no aparece en S2; **el rol de emisor ante el SII es de GoSocket en toda la conversación** |
| F-15 | **Acuse / estado / motivo de rechazo** | **GoSocket** lo publica; el ERP lo consulta | Pablo [07:35]: «en la parte de abajo, que es lo que más nos importa, tenemos las notas. Y acá es donde se ven los errores» |
| F-16 | Diagnóstico mapeo vs request | **GoSocket** entrega ambos artefactos | Pablo [07:35]: «tenemos descargar el XML en el cual se construyó nuestro documento, y en el archivo de integración tenemos el documento que ustedes enviaron sin procesar, o sea en crudo. Bien, entonces así nosotros determinamos si es que este error se generó después del mapeo o es la información que ustedes nos enviaron» |
| F-17 | **PDF / representación gráfica** | **GoSocket** | Pablo [07:35]: «tenemos acá la opción del PDF… pueden descargar el PDF con la representación actual que está cargada». S3: «PDF API = `Get Download Document PDF` en base64, plantilla estándar» |
| F-18 | Cambiar la plantilla del PDF sin reemitir | **GoSocket** | Pablo [07:35]: «no es necesario volver a emitir un documento, sino que pueden irse a un documento antiguo y aquí en el combo box está la opción de regenerar PDF» |
| F-19 | **Ambiente QA**: crear y entregar credenciales | **GoSocket** | Pablo [04:49]: «para Cuba \[QA] no es necesario el contrato. Yo ahora voy a crear el ambiente para que ustedes puedan, en este caso, ya emitir los documentos. Así que saliendo de la reunión les mando las credenciales» |
| F-20 | **API keys QA** | **Devint** las genera (hasta 10) | Pablo [26:58]: «Solamente es colocar básica authentication y confirmar… Para QA tienen límite de 10» |
| F-21 | **API key productiva** | **GoSocket la entrega** (una) | Pablo [26:58]: «Para el productivo ya es necesario avisarnos porque ya en el productivo se entrega por lo generalmente una, bien, y se las entrego yo» |
| F-22 | Altas de usuarios del portal en producción | **Almahue (MJ)** | Pablo [17:49]: «Este proceso en productivo, María, lo más probable es que solamente usted tenga el acceso a agregar gente. Yo solamente le agrego a usted y ahí usted administra» |
| F-23 | Validar en el portal lo emitido por API | **Devint (obligatorio)** | Pablo [05:43]: «es súper importante que ustedes se integren también a la plataforma porque así pueden ver in situ cuáles son los errores que están generando los documentos» |
| F-24 | Interpretar la respuesta: HTTP 200 ≠ emitido | **ERP** | S3 `K-4`: «Guardar `GlobalDocumentId` para consultas posteriores. HTTP 200 ≠ éxito. Si el GID viene en **0**, responder negativo al usuario» |
| F-25 | Contrato comercial / IOFactura | **Almahue + GoSocket comercial** (Cristian) | Pablo [03:20]: «una vez que me informen que el contrato ya está firmado, les aviso para que podamos habilitar IO Facturo». MJ [01:11]: «nosotros no tenemos ningún problema en que nos manden el contrato y firmarlo» |
| F-26 | Recuperar historial DTE de AlmaWeb/Acepta (~1000–1200 docs) | **Diferido**, Almahue + GoSocket | Pablo [03:20]: «el servicio te deja descargar de 20 documentos máximo… es una tarea enorme. Mira, si gustas podemos verlo en otra reunión» |
| F-27 | **Contabilización interna del DTE** | **ERP, exclusivamente** | Ver sección siguiente |

### Sandbox vs producción — resumen operativo

| Aspecto | QA / sandbox | Producción |
|---|---|---|
| Contrato | **No requerido** (Pablo [04:49]) | Requerido para IOFactura (Pablo [03:20]) |
| Folios | Carga **manual** del CAF por MJ (Pablo [07:35]) | **Automáticos** (Pablo [07:35]) |
| API keys | Hasta 10, autoservicio (Pablo [26:58]) | Una, la entrega Pablo (Pablo [26:58]) |
| Usuarios del portal | Los agrega Pablo por invitación | Los administra MJ (Pablo [17:49]) |
| URL | `sandbox2` — la del correo falla (Carlos [21:10]) | No tratada en estas fuentes |
| Rendimiento | «hay que tener paciencia igual con el ambiente… tiene menos recursos que el de Productivo» (Pablo [07:35]) | — |
| Resolución SII (CAE) | Valores QA en S3 `K-3` | «Cambian en productivo» (S3 `K-3`) |

---

## Qué NO cubre GoSocket

**Confirmado por ausencia total en las fuentes, y desmentido explícitamente por el código.**

Revisé completos los dos verbatims de GoSocket y las dos minutas. **En ninguno aparece, ni una vez, el plan de cuentas, la cuenta contable, el asiento, la centralización ni el mapeo de tipo de documento a cuenta.** El vocabulario de Pablo es íntegramente de emisión: folios, CAF, certificado, firma, XSLT, XSD, nodos, carátula, resolución, PDF, notas, API key. Lo más cerca que llega a contabilidad es F-16, y ahí «mapeo» significa **XSLT request → XML SII**, no cuenta contable:

> Pablo [07:35]: «este request se transforma por medio de un XSLT, de un mapeo»

Del otro lado, la única mención a cuentas contables por tipo de documento en toda la sesión de tesorería es de **MJ describiendo Agrosoft**, sin GoSocket en la frase:

> MJ, L172: «es la cuenta de proveedores, que es la 21040001. Lo que se diferencia es el auxiliar y el tipo de documento nomás»

### De dónde salió la confusión

La rastreé. Viene de **una sola línea de una minuta generada por IA**, que además trae un error de ASR:

> `fuentes/reunion5-minuta-tldv-2026-08-03.md` L107: «Configuración contable **SAI** necesaria para implementar GoSocket 37:20»

Dos problemas. Uno: «SAI» es ruido de ASR, no una sigla. Dos: el verbatim de Reu5 **no respalda esa frase en ese minuto** — `transcripcion-reunion5.md` en 35:41–39:01 está hablando de PIN y contraseñas, no de GoSocket. La minuta comprime horas de reunión y su reloj no alinea con el del verbatim. **Esa línea no es evidencia de nada.**

### Qué es realmente la pantalla «Configuración contable (SII)»

Es una tabla interna de imputación contable. `ERP/erp_front/src/features/contabilidad/ConfigContableSiiPage.tsx` sobre el modelo `ConfigContableSii`:

```
tipoDocumentoSii  →  cuentaContableId  +  lado (DEBE|HABER)  +  centroCostoId?  +  activa
```

Y las claves que guarda **no son solo códigos SII**. En el seed conviven dos familias:

| Familia | Ejemplos del seed | Qué es |
|---|---|---|
| Códigos SII | `33` factura electrónica venta → cuenta ingreso HABER; `34`; `61` nota de crédito → DEBE; `46` factura compra | Tipo de DTE |
| Roles contables | `VENTAS`, `CLIENTES`, `PROVEEDORES`, `CONTRATISTAS`, `IVA_DEBITO`, `IVA_CREDITO` | Rol en el asiento |

El comentario del schema lo dice: «Código SII o **clave interna** (33, 34, FACTURA_COMPRA, IVA_DEBITO, …)». Lo consume `contabilidad.service.ts` en `resolveCuentaPair()` para la centralización, y el flujo de contabilizar para armar el asiento. **Nada de esto viaja a GoSocket.** El nombre «SII» describe el *origen de la clave*, no una integración; es exactamente lo que alimenta la confusión.

**Veredicto:** la pantalla es 100% ERP. GoSocket no la cubre, no la necesita y no la conoce. Renombrarla —por ejemplo «Imputación contable por tipo de documento»— eliminaría el malentendido de raíz.

---

## Reglas de negocio concretas

**Tesorería (cliente, 28/08):**

1. El movimiento de cartola es la **unidad de trabajo**: se contabiliza 1:1 y ahí mismo se dice contra qué (T-01, T-02).
2. Ingreso → banco al **debe**; egreso → banco al **haber**; la contracuenta la elige el usuario (T-03).
3. Cartola con movimientos pendientes **no se cierra**. Mes conciliado = cartola íntegramente contabilizada (T-06, MJ L190).
4. Sin documento identificable, el movimiento va como **anticipo**; el calce ocurre después, cuando entre la factura (T-05).
5. Anticipo de productor: siempre razona en dólares porque «así es su contrato» (Lupe L68), aunque el pago salga en pesos.
6. Editar el TC **nunca** mueve el monto ni el saldo bancario; solo cambia lo que el productor ve para liquidar (T-09, MJ L322).
7. TC por defecto = Banco Central de la fecha del movimiento; si no es hábil, el hábil anterior. Solo productores admiten TC negociado (T-13, T-14).
8. Flujo de caja: **solo lectura**, alimentado por movimientos contabilizados, clasificado por **código financiero**, filtrable por moneda (T-15, T-17, MJ L316).
9. Saldo de apertura: uno por banco+moneda, **inmutable** (T-18).
10. Saldos nunca se convierten sin que el usuario lo pida (T-16, y MJ descarta la conversión automática en L300–L302 porque «el usuario puede registrar cualquier tipo de cambio y no va a ser un valor real»).
11. Nómina por **semana de compromiso**, no por vencimiento del DTE: el crédito de materiales a 6 meses hace que la fecha del documento no sirva (T-20, Lupe L388).
12. Estado de cuenta se consulta **por RUT**, no por rol; un RUT puede ser cliente y proveedor a la vez y hay que poder compensar (T-23, T-25).

**DTE / GoSocket (tercero):**

13. Sin certificado cargado, los documentos salen **rechazados**: «antes de que Carlos emita documentos hacia el portal de pruebas, el certificado ya tiene que estar cargado, porque si no, nos van a salir como rechazado» (Pablo [26:12]).
14. Sin CAF cargado, la API responde que **no existe el rango de folio** (Pablo [28:31]).
15. Resolución SII mal informada → **error de carátula** (Pablo [07:35]).
16. Emitir con **fecha del día**, «para que no se les pierda en el mismo filtro»; buscar con «últimos 3 meses» (Pablo [07:35]).
17. `HTTP 200` no significa emitido: hay que mirar `Success` y sobre todo `GlobalDocumentId`; en 0, responder negativo al usuario (S3 `K-4`).
18. Razón social del emisor: 100 alfanuméricos, **GoSocket no trunca**, rechaza (S3, minuta).
19. `CodRef` en nota de crédito: solo `1` anula, `2` corrige texto, `3` corrige montos; el texto «anular» no sirve (S3, minuta).
20. Campos personalizados: ilimitados, no validados, y **se sacan del XML que va al SII**; sirven solo para la representación gráfica (S3, minuta).
21. Orden del XSD: `Acteco` (6 dígitos) antes de `DirOrigen`; `RUTRecep` antes de `RznSocRecep` (S3, minuta).

---

## Decisiones cerradas vs abiertas / bloqueos pendientes

### Cerradas por el cliente el 28/08

| Decisión | Quién | Ref |
|---|---|---|
| El trabajo diario de tesorería se hace **sobre la cartola**, no en pantallas sueltas | MJ | L124, L194 |
| Contabilización 1:1, sin proceso batch | MJ | L154 |
| Conciliación = estado derivado de la cartola, no un módulo con alta propia | MJ | L142, L190 |
| Solo el anticipo de productor tiene TC editable | MJ | L324 |
| Flujo de caja por moneda; el banco no es eje de análisis | MJ | L266 |
| Flujo de caja no editable | MJ | L258 |
| Nómina se llama «Nómina semanal de pagos» | Lupe | L392 |
| Estado de cuenta unificado por RUT | MJ | L420, L430 |

### Cerradas por GoSocket (tercero)

QA sin contrato (Pablo [04:49]) · folios manuales en QA y automáticos en producción (Pablo [07:35]) · certificado y CAF los carga MJ (Pablo [24:16], [26:58]) · API key productiva la entrega Pablo (Pablo [26:58]) · portal obligatorio para los testers (Pablo [05:43]).

### Abiertas

| # | Tema | Por qué sigue abierta | Quién destraba |
|---|---|---|---|
| A-1 | **Sync automático BC** | MJ dijo «nos urge» (L316) y hoy no hay job. No se acordó frecuencia ni fuente técnica | Devint (implementar); MJ ya definió el qué |
| A-2 | **Triple moneda en el mayor** | T-12 pide las 3 conversiones en toda la contabilidad; el asiento no las modela | Devint diseña; MJ valida alcance |
| A-3 | **Alcance de la migración histórica** | Sergio menciona «desde 5 años… la información del 2019» (L328), MJ no lo confirma. La sábana de ~19.000 registros quedó en «se los puedo mandar» (L360) | MJ envía Excel; Devint define importador |
| A-4 | **TC histórico de yuan** | «Nosotros actualmente tenemos el tipo de cambio peso y dólar, lo que no tenemos yuanes» (MJ L330). No hay fuente acordada | MJ / Devint |
| A-5 | **Alcance real de «todo con registro de usuario»** | MJ lo dijo en general (L104); solo se implementó para TC | Devint acota y propone |
| A-6 | **Contrato GoSocket / IOFactura** | Cristian no respondía al inicio; Pablo anunció borrador ese día (Pablo [20:11]) | Cristian → MJ/Mario firman → Pablo habilita |
| A-7 | **CAF y certificado productivos** | Nunca se declararon cargados en estas fuentes | MJ |
| A-8 | **Documento de validaciones GoSocket** | S3 `K-5`: «Pablo reenvía a Carlos el documento de validaciones (largos, obligatoriedad 1/2/3). Pendiente de correo» | Pablo |
| A-9 | **Representación gráfica a medida** | S3: «Pablo necesita spool válido (Sergio: próxima semana)» | Sergio → Pablo |
| A-10 | **Recuperación histórico AlmaWeb/Acepta** | Diferido a reunión aparte (Pablo [03:20]) | MJ + Pablo |
| A-11 | **Sets exportación y boletas** | S3: «Boletas: otro esquema»; exportación «después del set básico» | Devint + Pablo |

### Bloqueos que hoy frenan QA de tesorería

| Bloqueo | Efecto | Naturaleza |
|---|---|---|
| **P0-1** — Config SII `PROVEEDORES` apunta a `2-1-01-01`, cuenta marcada `noImputable=true` | Contabilizar factura de compra devuelve 400 → no hay aging POR_PAGAR → TES-PRE-2, TES-NOM-1 y T5-4 quedan **BLOCKED** | **Dato, no código.** Se arregla apuntando a una hoja imputable |
| Config SII `VENTAS` `5-1-01-01-001` exige área de negocio | En la ola 9 obligó a contabilizar contra CAJA | Dato / parametrización |
| Códigos financieros del catálogo Reu con `activa=null` | El combo de la UI no los ofrece; la API sí los acepta | Dato + filtro UI (`activa !== false`) |
| Sin RUT que sea cliente y proveedor en EMP-EXPORT | T6-3 no ejerce el caso dual que MJ describió (L426) | Dato de prueba |

Los tres BLOCKED de tesorería son **el mismo P0-1**, y P0-1 es un dato mal apuntado en la propia pantalla «Configuración contable (SII)». Vale la pena subrayarlo: la pantalla que se sospechaba redundante con GoSocket es hoy la que **bloquea el retest de tesorería**.

---

## Señales para QA

### Los SKIP/BLOCKED de DTE, uno por uno

| Caso | Estado 02/09 | Motivo declarado | Veredicto | Argumento |
|---|---|---|---|---|
| **BIL-007** — emisión real al SII | SKIP | «SII live / CAF portal. Sandbox ≠ live. Folio 58 es sandbox» | **Sigue bloqueado. Externo.** No ejercer | El SII live depende de la cadena F-25 → F-06 → F-02: contrato firmado, certificado con permiso de firma, CAF productivo. Todo eso es de MJ y Cristian, no de Devint. Pablo [26:12] es taxativo: sin certificado, «nos van a salir como rechazado». Además `H14`: no se ha desplegado a `45.7.229.46` |
| **BIL-004** — nota de crédito | PASS con matiz | «`GET documentos?tipo=NC` 200 n=0. Mapeo NC en Jest. No se creó NC» | **Debería ejercerse ya.** No lo bloquea nada externo | El sandbox está emitiendo (folio 58 PENDING). Y S3 aportó la regla dura que hoy **no está probada end-to-end**: `CodRef` solo admite 1/2/3, «Texto "anular" no sirve». Un canónico de NC con `CodRef` mal puesto se rechaza en GoSocket, no en el ERP. Hoy solo hay cobertura Jest de mapeo |
| **«REJECTED sin CAF»** | «no ocurrió» | «Sandbox encoló PENDING + folio 58. Fail-closed REJECTED queda como escenario no ejercido» | **El supuesto cambió. Hay que reencuadrarlo** | Ver abajo |
| **BIL-005** — modo `ENABLED=false` | SKIP | «no aplica (entorno HTTP). No se cambió `.env`» | **Ejercitable.** Entorno, no externo | Es un flag local. Cubre el modo «contabiliza sin partner» que AGENTS declara vigente |
| **BIL-006** — print HTML local | SKIP | R4-08 | **Sin urgencia** | Los artefactos del partner ya se validaron en SIST-9-30 (PDF 52.793 B real, XML `EnvioDTE` ~8 KB). Y la representación gráfica definitiva es de GoSocket (F-17), pendiente del spool de Sergio (A-9) |
| **BIL-008** — consolidado VEN-026 | SKIP | Cubierto en ola 5 | Administrativo. Cero acción | — |
| **E2E-008** — producción | BLOCKED | H14, no se tocó `45.7.229.46` | **Sigue bloqueado. Externo** | Requiere decisión de deploy |

### El cambio que nadie registró como cambio

`AGENTS.md` sigue afirmando que, sin CAF y certificado de MJ, el partner responde **REJECTED** en fail-closed y no se genera asiento. **Eso ya no es lo que pasa.** El 02/09, en sandbox GoSocket con `BILLING_GATEWAY_ENABLED=true` y `BILLING_STUB_INLINE=false`:

> `2026-09-02-sist-ola9-dte-e2e.md`: «Resultado **PENDING**… Folio oficial **58**… Asiento **20260012**… No es el camino REJECTED-sin-CAF: el sandbox **encoló** el DTE»

Que GoSocket haya asignado **folio oficial 58** significa que el asignador **sí encontró rango CAF** en sandbox (contrastar con S3 `K-4`: sin `BillerId`, el asignador no encuentra rango y devuelve GID 0). Consecuencias para QA:

1. **La rama fail-closed REJECTED ya no se reproduce sola.** Si se quiere seguir cubriendo, hay que forzarla —por ejemplo con un `BillerId` inválido, que es exactamente cómo Pablo la provocó en la mesa del 01/09. Dejarla como «escenario no ejercido» es aceptar un agujero en el manejo de errores.
2. **Hay que verificar `GlobalDocumentId`, no solo el HTTP.** S3 `K-4` es explícito: 200 no es éxito, y GID 0 debe reportarse como negativo al usuario. QA registró `folioOficial=58` y `Authority sandbox 0`; **no dejó constancia de haber validado el comportamiento ante GID 0**. Es un caso de prueba faltante y es barato.
3. **Actualizar AGENTS.md.** Mantener «GoSocket REJECTED por falta de CAF» como estado vigente induce a marcar SKIP por un bloqueo que en sandbox ya no existe.

### Qué probaría ahora, en orden

1. **Arreglar el dato P0-1** — apuntar Config SII `PROVEEDORES` a una hoja imputable. Desbloquea de un golpe TES-PRE-2, TES-NOM-1 y T5-4, y con T5-4 se cierra T-22 (aplazar sin mutar el DTE), que es requisito directo de Lupe.
2. **Emitir una NC de verdad en sandbox** con `CodRef` 1, 2 y 3, y una cuarta con valor inválido para confirmar el rechazo. Cubre BIL-004 real y la regla 19.
3. **Forzar GID 0** con `BillerId` inválido y comprobar que el ERP responde negativo al usuario (S3 `K-4`).
4. **Sembrar un RUT cliente+proveedor** en EMP-EXPORT y reejecutar T6-3 con `dual=true`. Es el caso que MJ describió como su dolor de compensación (L426) y hoy no se ha ejercido nunca.
5. **Contabilizar una venta con cuenta VENTAS + área**, para dejar de usar CAJA como atajo (ya está en el retest sugerido de la ola 9).
6. **Levantar A-1 y A-2 como huecos de producto**, no como casos de QA: no hay nada que probar hasta que exista el job del Banco Central y la conversión en el asiento.

**No tocar hasta que MJ y Cristian avancen:** BIL-007 y E2E-008. Ningún cambio de código los destraba.

---

## Trazabilidad

| Archivo leído | Cómo se usó |
|---|---|
| `fuentes/transcripcion-2026-08-28-tesoreria-mj-lupe.md` | Completo (458 L). Base de todo el bloque de tesorería |
| `fuentes/transcripcion-reunion-gosocket-qa.md` | Completo. Base de la frontera ERP↔GoSocket |
| `reunion-2026-09-01-gosocket-kickoff.md` | Completo. Secundario (`K-n`), sin cliente presente |
| `reunion-gosocket-minuta-2026-08.md` | Completo. Solo verificación de `GOS-1`…`GOS-17` contra el verbatim |
| `fuentes/reunion5-minuta-tldv-2026-08-03.md` L107 | Origen rastreado del mito «Configuración contable SII ↔ GoSocket» |
| `qa/resultados/2026-09-02-tesoreria-t1-t6.md` | Columna «¿parece implementado?» de T-01…T-28 |
| `qa/resultados/2026-09-02-sist-ola9-dte-e2e.md` | Estado real de DTE y de los SKIP/BLOCKED |
| `ERP/erp_back/prisma/schema.prisma`, `contabilidad.service.ts`, `ConfigContableSiiPage.tsx`, `prisma/seed*.ts` | Qué es realmente «Configuración contable (SII)»; huecos G-1, G-2, G-4 |
