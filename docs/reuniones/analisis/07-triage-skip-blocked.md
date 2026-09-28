# Triage de los 40 SKIP + 1 BLOCKED — QA sistema completo 02/09

**Origen:** `qa/resultados/2026-09-02-sist-review.md` (490 PASS · 0 FAIL · 1 BLOCKED · 40 SKIP · 535 casos).
**Propósito:** decidir cuáles de esos casos **debieron ejercerse** y hoy son un hueco real, contrastando el motivo del SKIP contra lo que el cliente dijo **en la transcripción** (no en la minuta IA).

## Por qué re-auditar los SKIP

Buena parte de los SKIP se justifican con una **etiqueta** (`D11`, `D14`, `D16`, `H10`, `H13`, `R4-18`, `DK-G4`…) que no vive en la transcripción: vive en las minutas generadas por IA. Si la etiqueta está mal, el SKIP hereda el error y un requisito real del cliente queda sin probar y sin implementar.

**Prueba de que el riesgo es real — el código `D14` significa dos cosas distintas:**

| Documento | Qué dice D14 |
|---|---|
| `reunion4-minuta-2026-07-30.md` L43 | «Cartola: carga Excel banco → contabilizar = calzar/conciliar; cargos y abonos» |
| `reunion6-minuta-2026-08-06.md` L43 | «Stock ventas **solo positivo** (real, no tránsito de venta)» |

QA marcó `INV-014` como SKIP citando «D14 tránsito venta — no modelado», usando la acepción de Reu6. Si el D14 que importaba era el de Reu4 (cartola Excel), el caso quedó sin cubrir por una colisión de nomenclatura, no por una decisión de negocio.

## Inventario completo

Leyenda de la columna **Tipo**:
- **admin** — el caso se cubrió en otra ola o con otro ID. No es hueco. Cero acción.
- **externo** — depende de un tercero (SII, SMTP, portal GoSocket, deploy a producción). No se puede cerrar en escritorio.
- **entorno** — se puede ejercer, no se hizo por estado de la base o de la corrida.
- **auditar** — el SKIP se apoya en una etiqueta de minuta IA. Requiere veredicto contra transcripción.

### Ola 1 — admin y RBAC (13)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| SMK-004 | Aislamiento holding cubierto por SIST-1-12 / RBAC-001 | admin | — |
| SMK-006 | Stock cereza es Ola 4 | admin | — |
| SMK-008 | `npm test` fuera de alcance de negocio | admin | — |
| ADM-004 | Plan Ola 1: no crear sociedad extra | entorno | _pendiente_ |
| ADM-005 | No se reasignó operador holding a 2 empresas | entorno | _pendiente_ |
| ADM-007 | No se editó rol seed (PIN en rol) | entorno | _pendiente_ |
| ADM-015 | Modal `APROBADOR_SIN_BANDEJA` exige mutar escala | entorno | _pendiente_ |
| ADM-019 | D4: cadena OV eliminada; combo módulo solo Compras | auditar | **⚠ atribución falsa** — ver «El caso D4» |
| ADM-020 | DK-D19: SSO Microsoft `enabled=false` | auditar | **SKIP correcto, requisito inexistente** — Carlos degradó el SSO a «nota para futuro»; «Entra», «redirect», «Tenant/Client ID» y `.env` **no se pronuncian jamás** en Reu6, los inventó la minuta |
| ADM-021 | Aprobar OC ajena es Ola 3 | admin | — |
| ADM-022 | No se mutó AdminConcepto; sin re-login JWT | entorno | _pendiente_ |
| RBAC-008 | DK-G8: `GET /workflows-admin` 200 n=0, legacy vivo | auditar | _pendiente_ |
| RBAC-009 | H9 SMTP correo PIN | externo | — |
| RBAC-014 | D4: `GET /aprobaciones-ov` 404, bandeja eliminada | auditar | **⚠ atribución falsa** — ver «El caso D4» |

### Ola 2 — parametrización y fichas (2)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| FIC-009 | Consolidado → VEN-029 | admin | — |
| FIC-010 | Consolidado → VEN-031 | admin | — |

### Ola 3 — compras (3)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| CMP-002 | D11: no existe convertir cotización → OC | auditar | **⚠ contradice a MJ** — ver «El caso D11» |
| CMP-003 | D11: no existe convertir cotización → factura | auditar | **⚠ contradice a MJ** — ver «El caso D11» |
| CMP-024 | H10 comparador de 3 cotizaciones — no es proceso actual | auditar | _pendiente_ |

### Ola 4 — inventario (4)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| INV-009 | Coherencia stock post-OV = VEN-007 (Ola 5) | admin | — |
| INV-010 | H7 e2e exige NC de ventas contabilizada | entorno | _pendiente_ — el reviewer lo marca **hueco P0** |
| INV-014 | D14 tránsito de venta — no modelado | auditar | _pendiente_ — colisión D14 Reu4 vs Reu6 |
| INV-015 | Carga masiva Excel movimientos bodega AlmaWeb — integración externa | auditar | _pendiente_ — tl;dv Reu4 lo lista como pedido (50:40) |

### Ola 5 — ventas (1)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| BIL-007 | SII live / CAF = Ola 9 | externo | — |

### Ola 6 — contratistas (4)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| CTR-012 | Eliminado v2 → ADM-012 S6. Cadena CTR no aplica | auditar | **⚠ Reu3 R6** — MJ pidió aprobación de supervisor en proformas |
| CTR-014 | DK-G5 narrativa traspaso ≠ gastos de temporada | auditar | ⚠ El diseño de Traspaso/Cierre se movió a un canal privado (Reu3 B14): no hay fuente auditable |
| CTR-018 | DK-G4 ingreso diario demo profundo | auditar | **⚠ Reu3 R6** — MJ pidió aprobación de supervisor también en el trabajo diario |
| CTR-020 | Re-solicitar tras rechazo: no hay cadena | auditar | **⚠ Reu3 R6** — ver recuadro abajo |

> **Conflicto abierto en contratistas.** `AGENTS.md` da por cerrado que las proformas van `BORRADOR → DEFINITIVA` **sin cadena ni PIN**, y los cuatro SKIP de arriba se apoyan en eso. Pero Reu3 registra a MJ pidiéndolo de forma explícita y con motivación de control:
>
> - `[T 03:37:00 ≈ 22:12]` MJ: *«pediría aprobación de algún supervisor… Porque si no va a quedar muy abierto a que modifiquemos demasiado el día a día»*
> - `[T 03:45:40 ≈ 22:34]` MJ: *«ya ingreso una proforma diaria y alguien la autoriza, y después esa proforma hay que editarla. Al editarla, igual pedirá una autorización de la persona que autorizó»*
> - `[T 03:50:21 ≈ 23:02]` MJ acepta que se registre **el nombre de quien aprobó**.
>
> El corte del 21/08 eliminó esa cadena. Antes de cerrar estos SKIP como «nunca se pidió» hay que exhibir la decisión posterior que revoca a MJ; si no existe, es un requisito perdido, no un caso fuera de alcance. Lo verifica el análisis de las sesiones del 20/08.

### Ola 7 — contabilidad (2)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| CNT-007 | Centralizar execute mutaría Olas 3/5/6 + haber SII padre no imputable | entorno | _pendiente_ — se destraba con Config SII |
| CNT-D13 | Contabilidad electrónica SII (Reu4 D13), no certificación | auditar | _pendiente_ — el cliente lo difirió explícitamente |

### Ola 8 — tesorería (6)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| T4-3 | No se re-importó histórico Banco Central | admin | — |
| TES-004 | H13 Excel banco fino (Chile / Estado / Santander); se usó CSV genérico | auditar | _pendiente_ — tl;dv Reu4 lo lista como pedido (01:05:10) |
| R4-18 | Cobranza — diferido | auditar | _pendiente_ — el cliente pidió una **propuesta**, no el módulo |
| SMTP | H9 correo PIN | externo | — |
| Match auto | Match automático cartola ↔ factura; se hizo calce manual 1:1 | auditar | **⚠ es el cuello de botella real de Lupe** — ver abajo |
| TES-CARTOLA-IMP | File picker de UI no automatizable; import por API sí cubierto | admin | — |

### Ola 9 — DTE y end-to-end (5 SKIP + 1 BLOCKED)

| ID | Motivo declarado | Tipo | Veredicto vs transcripción |
|---|---|---|---|
| BIL-005 | `BILLING_GATEWAY_ENABLED=false` no aplica; no se tocó `.env` | entorno | _pendiente_ |
| BIL-006 | Print HTML local; artifacts del partner en SIST-9-30 | admin | — |
| BIL-007 | SII live / CAF portal. Folio 58 es sandbox | externo | — |
| BIL-008 | Consolidado VEN-026 Ola 5 (guía GD-SIST5-01) | admin | — |
| E2E-007 | Greenfield / seed, fuera de corrida | entorno | _pendiente_ |
| **E2E-008** | **BLOCKED** — producción `45.7.229.46`, hueco H14: no se tocó prod | externo | _pendiente_ |

## El único BLOCKED

`E2E-008` no es un defecto: es el recorrido end-to-end **en producción**, y no se ejecutó porque `AGENTS.md` prohíbe asumir que el `migrate` de stock/OV/`piloto_on` ya corrió en `45.7.229.46` (hueco H14). Se destraba con un deploy explícito, no con código. Es decisión de negocio, no de ingeniería.

## Los tres casos que sostienen 9 SKIP

### El caso D4 — el rótulo significa cosas opuestas

`AGENTS.md` cierra «D4: aprobaciones **solo Compras**, cadena OV eliminada» y lo atribuye a Reu6. Pero en la minuta de Reu6, **D4 dice lo contrario**: «alcance OC + proformas + **Comercial**». Mismo rótulo, sentido invertido.

El origen real del corte es la sesión del **20/08 tarde**, y ahí el respaldo se parte en dos.

**Órdenes de venta → sí hay respaldo, con reservas serias.** Lupe `[01:43]`: *«Sí, servicio y materiales, siempre de las compras, de la, solo de compras»*. Mario `[08:21]`: *«Por compras, sí, correcto»*, respondiendo a «me confirman que el flujo de aprobaciones pasa solamente por compras». Las reservas: ambas son respuestas a **preguntas cerradas e inductivas** de Sergio; describen el as-is de Almahue, no un mandato sobre el ERP; el módulo de Ventas **nunca se abrió** en esa sesión; MJ y Agustín estaban ausentes. Y esa misma mañana el proveedor había concluido lo opuesto — `[17:22]` *«Dejarlo, dejarlo como por montos, pero en momentos más extremos»*, con la acción `[17:18]` *«preguntémoslo por montos»* que **nunca se preguntó** en la tarde. El único monto citado en toda la tanda, del orden de $500.000, quedó enterrado.

**Proformas y contratistas → sin ninguna base.** Recuento literal sobre las tres transcripciones del 19 y 20 de agosto:

| Palabra | 19/08 | 20/08 mañana | 20/08 tarde | Total |
|---|---:|---:|---:|---:|
| proforma | 0 | 0 | 0 | **0** |
| contratista | 0 | 0 | 0 | **0** |
| labor | 0 | 0 | 0 | **0** |
| jornal | 0 | 0 | 0 | **0** |
| cotización | 1 | 37 | 32 | 70 |
| aprobación | 3 | 29 | 17 | 49 |
| compra | 31 | 38 | 50 | 119 |

El tema se habló mucho —49 menciones de «aprobación»— pero **nunca sobre contratistas**. La eliminación se dedujo de una frase cuyo universo era «ventas contra compras», y deshace un pedido de MJ en Reu3 sin una sola mención del asunto. Los cuatro SKIP `CTR-012/014/018/020` cuelgan de ahí.

### El caso D11 — MJ pidió mover, el código suprimió

`AGENTS.md` cierra «no hay menú ni CRUD de Cotizaciones» con redirect de `/compras/cotizaciones` a órdenes. Lo que MJ dijo en Reu6 es lo contrario:

> MJ `[40:09]`: *«a mi criterio las cotizaciones son para las compras. Ahora, si queremos hacer una orden de venta, es distinto.»*
> MJ `[40:21]`: *«nosotros no hacemos cotizaciones para hacer ventas porque la cotización debería ser el orden de venta, debería llamarse el título.»*
> Carlos `[40:56]`: *«este debería estar en el panel de compras.»* — MJ `[40:59]`: *«Debe estar en el panel de compras.»*

El pedido es **mover** la cotización al panel de Compras y **renombrar** el documento de ventas a «orden de venta». Nadie pidió eliminarla. Existe una frase posterior de Lupe el 20/08 `[05:48]` —*«nosotros solamente nos piden la orden de compra y nosotros solo generamos la orden de compra»*— pero el propio `AGENTS.md` establece que Lupe y Mario **no pisan Reu6 cuando chocan**. Aquí chocan, y se aplicó la regla al revés.

### El caso Reu5 — no había cliente en la sala

Reu5 es una conversación interna Carlos ↔ Sergio. **Ningún cliente estuvo presente.** Todo lo que hoy se cita como «pedido en Reu5» es decisión de diseño del proveedor; cuando Carlos invoca a MJ, lo hace de oído y en pasado. Ninguna minuta lo advierte. Dos consecuencias directas:

- La minuta tl;dv registra «configuración contable SII necesaria para GoSocket» **como requisito**, cuando Carlos dijo textualmente que eso era *«fantasmeo de la IA… puro fantaseo del aire»*. Es una inversión total de sentido, y es el origen de la confusión sobre para qué sirve la pantalla Config SII.
- La minuta canónica de Reu5 afirma «Cotiz→NP→Factura — Hecho», mientras `AGENTS.md` ordena «no restaurar cotiz→NP→factura». Dos documentos vigentes en contradicción directa.

## Huecos que ni siquiera figuran como SKIP

Más grave que un SKIP mal justificado es un requisito del cliente que **no tiene caso de prueba en absoluto**. Los 535 casos de la corrida no lo detectan porque el plan se construyó desde las minutas. Primera tanda, desde Reu3:

| Requisito | Quién y cuándo | ¿Hay caso QA? |
|---|---|---|
| Agrupar **3 o 4 proformas en una factura** con selección múltiple | MJ `[T 03:54:41 ≈ 23:28]` | La Ola 6 facturó N:1, pero no hay caso que fije el requisito |
| Al contabilizar el libro de compras, **ver las OC del proveedor por RUT** (ejemplo textual: factura 77 → OC 4) | MJ `[T ≈ 36:52]` | No |
| **Devolución a proveedor** como `SALIDA_PROVEEDOR` con **tipo de cambio propio**, sin distorsionar el costo promedio | MJ | No. La Ola 4 clasificó el par `SALIDA_PROVEEDOR` como «diseño» |
| **Cada cuenta contable parametriza si exige centro de costo** | MJ | No. Conecta directo con P0-1 y con el 400 «exige elemento» de la Ola 3 |
| Renombrar **Libro comercial → Libro de ventas** (para el cliente «libro comercial» es el de **compra**) | MJ `[T 06:22:20 ≈ 38:13]` | No. La minuta IA de Reu3 **omitió** este ítem por completo |
| Importar el **Excel del SII** de compras y ventas con **dedup por solape** (cargar 01–07 y luego 01–14 sin duplicar) | MJ `[T ≈ 36:52]`, es lo que ya hacen hoy en Agrosoft | No |
| **No existe maestro de Vendedores**; el cliente se crea **solo desde el área contable** porque los vendedores *«pueden crear, falsificar documentos»* | MJ `[T ≈ 32:36]` | No |

Segunda tanda, desde Reu6 y desde la sesión del 20/08 tarde:

| Requisito | Quién y cuándo | Estado |
|---|---|---|
| **RUT de la contraparte en la cartola.** Hoy *«solo aparece el nombre, no me aparece el RUT»* y por eso calza a mano | Lupe `[19:05]` 20/08 | Hueco real. `MovimientoCartola` asocia proveedor/cliente por FK manual |
| **Motor de sugerencia de calce** cartola ↔ factura (hoy criterio maestro-cliente + movimiento + monto, uno a uno) | Lupe 20/08 | Hueco real. Los endpoints de conciliación son alta y desconciliación manual. Es el SKIP «Match auto» |
| **Ficha de solicitud de alta de contraparte**, con respaldo de quién la pide | Agustín, lo repite 3 veces, `[36:13]` Reu6 | Sin rastro en el backend. La minuta lo colapsó dentro de D8 |
| **Clave para reversar o eliminar** en mantenedores sensibles | MJ `[34:59]` Reu6 | El PIN existe solo para aprobaciones |
| **Dependencia múltiple de jefaturas** | `[19:44]` Reu6 | `Usuario.jefeId` admite una sola |
| ~~Hora parametrizable de indicadores Banco Central~~ | `[23:36]` Reu6 | **Ya implementado, verificado en código.** `SyncBcMeta` tiene `autoSync`, `horarios` múltiples, `frecuenciaMinutos`, `ventanaInicio/Fin`, `diasHabiles`, `lastCronSlot` y `failStreak`. El `@Cron('*/5 * * * *')` de `bc-sync.cron.ts` es solo el tic del planificador, que delega en `runScheduledBcSyncIfDue()` |
| **Triple moneda en el libro mayor** | MJ 28/08: «toda la contabilización de todo el sistema tenga las 3 conversiones» | **Hueco confirmado en código.** `Asiento.lineas` es `Json` con forma `[{ debe, haber, cuentaId?, glosa? }]`: sin tipo de cambio ni importe convertido. `debe`/`haber` son `Decimal(18,2)` monomoneda. Diario, mayor y balance no soportan las 3 conversiones |
| **Migración del histórico de Agrosoft** (~19.000 registros con TC, código financiero y cuenta) | MJ 28/08 | Sin importador y sin alcance definido. El TC histórico de yuan no existe ni en Agrosoft |
| **Bitácora transversal de usuario** | MJ 28/08: «todo lo que se haga en el sistema quede con registro de usuario» | Solo existe para el tipo de cambio de pagos |
| ~~**D16 valida contra la base de costo equivocada**~~ | Sergio `[49:38]` Reu6 | **Corregido 03/09.** Lo discutido era el **precio de compra del mantenedor**; el código validaba contra `costoPromedio`, término que nadie pronunció. Ahora el piso es `Insumo.precioCompra` con caída a `costoPromedio` mientras el maestro no lo tenga cargado |

## Config SII: el problema no eran las cuentas padre

Diagnóstico ejecutado el 03/09 contra la base local con `ERP/erp_back/scripts/config-sii-diag.mjs`. El SKIP hablaba de «cuentas no imputables», pero el plan real de EMP-EXPORT (398 cuentas importadas de Agrosoft) reveló algo distinto: **los mapeos apuntaban a cuentas sin relación semántica con la clave**. El seed los asignó por posición de código, y los códigos del plan real significan otra cosa que los del plan de juguete de EMP-SERVICES.

| Clave | Apuntaba a | Corregida a |
|---|---|---|
| `PROVEEDORES` | `2-1-01-01` OBLIGACIONES CON BANCOS CP (padre) | `2-1-04-01-001` PROVEEDORES |
| `IVA_CREDITO` | `1-1-03-01` VALORES NEGOCIABLES (padre) | `1-1-09-01-001` IVA CREDITO FISCAL |
| `IVA_DEBITO` | `2-1-03-01` (cuenta de seed ajena al plan Agrosoft) | `2-1-09-02-001` IVA DEBITO FISCAL |
| `BANCO` | no existía; el haber de cartola caía en CAJA | `1-1-01-02-001` BANCO CHILE $ |

Aplicado por API (`PUT /config-contable-sii`), que valida imputabilidad por su cuenta. Quedan 5 de 7 claves OK. Corregir por subárbol —la heurística del script SQL que se descartó— habría producido disparates: para `CONTRATISTAS` proponía «VENTA GANADO» y para `IVA_CREDITO`, «MUTUOS».

### Lo que no se podía arreglar por configuración — cerrado el 03/09

`CONTRATISTAS`, `VENTAS` y `COMPRAS` no tenían destino válido, y el motivo era el requisito de MJ que figura arriba como hueco sin caso QA: **en el plan real, toda cuenta de costo o de ingreso exige centro de costo**, y casi todas exigen además área o elemento. `ConfigContableSii.centroCostoId` existía y no lo leía nadie; las columnas de área y elemento ni siquiera existían.

El cierre no fue elegir otra cuenta, sino que el mapeo cargue las dimensiones y los generadores las arrastren:

- Migración `20260903150000_config_sii_dimensiones`: `areaNegocioId` y `elementoCostoId` en `ConfigContableSii`.
- `config-sii-dimensiones.util.ts`: tipo `DimensionesAsiento` y los helpers `dimensionesDeConfigSii` / `combinarDimensiones`.
- Los cuatro generadores propagan la dimensión del mapeo a cada línea: `comercial.service.ts` (VENTAS e IVA, incluida la reversa), `compras.service.ts` (combinando con la dimensión que traiga la OC, que tiene prioridad), `contratistas.service.ts` (`TRASPASO-CTR`) y `tesoreria.service.ts` (asiento de cartola).
- `putConfigContableSii` rechaza guardar un mapeo cuya cuenta exige una dimensión que no viene, y verifica que la dimensión exista en la empresa. Antes el error salía recién al contabilizar, y era opaco.
- La pantalla «Cuentas por tipo de documento» muestra un selector por cada dimensión que la cuenta elegida exige, y la tabla inferior resume las dimensiones guardadas.

### El seed nacía mal

El origen del mapeo roto de `CONTRATISTAS` estaba en `prisma/seed.ts`: resolvía la cuenta con `pick('6-1-01-01', …)`, un código de **nodo padre** que nunca aparece entre las imputables, y el fallback silencioso `cuentas[0]` la dejaba en cualquier parte — en EMP-EXPORT terminó en `5-1-01-01` VENTAS DE EXPLOTACIÓN, una cuenta de **ingresos** y encima no imputable: el traspaso de contratistas se anotaba como si fuera una venta. Ahora el seed resuelve por semántica (nombre y tipo), prefiere entre los candidatos el que **no** exige dimensiones, siembra las que sí hagan falta y avisa por consola si alguna queda sin completar.

Estado local tras la corrección (`scripts/config-sii-estado.mjs`): las 7 claves de EMP-EXPORT y las 6 de EMP-SERVICES en OK. `CONTRATISTAS` quedó en `6-1-01-01-002` MANO DE OBRA CONTRATISTA con CC 15100, y `VENTAS` en `5-1-01-01-001` con CC 15100 + área PACK.

### Efecto colateral encontrado: Insumos caído

Al revisar el log del backend apareció un `500` en `GET /api/v1/insumos`: *«The column (not available) does not exist»*. La columna `precioCompra` del cambio D16 estaba en el schema y en el cliente Prisma generado, pero no en la base local, porque `erp._prisma_migrations` está vacía y `migrate deploy` no se puede correr (H14). Se aplicó el DDL a mano con `scripts/apply-migraciones-pendientes.mjs`, que es idempotente y agrupa las dos migraciones del día. Insumos responde de nuevo.
