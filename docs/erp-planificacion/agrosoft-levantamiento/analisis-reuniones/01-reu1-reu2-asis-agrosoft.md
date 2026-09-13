# Reu1 + Reu2 — as-is Agrosoft (desde transcripción)

> **Fuente primaria de este documento:** lectura íntegra de
> `fuentes/transcripcion.md` (Reu1) y `fuentes/transcripcion-reunion2.md` (Reu2).
> No se usó ninguna minuta como insumo salvo en la sección «Contraste con la minuta IA».
>
> **Nota de método — relojes de los transcripts.** Las marcas de tiempo de los
> transcripts **no** coinciden con el video/tl;dv. En Reu2 el reloj corre a **1/10**
> del tiempo real: verificado contra cuatro anclas de la minuta tl;dv
> (raw `06:47:51`→`40:47`, raw `11:10:31`→`01:07:03`, raw `12:30:40`→`01:15:04`,
> raw `13:14:41`→`01:19:28`). Por eso aquí se cita `[raw hh:mm:ss ≈ mm:ss real]`.
> Para **Reu1 no hay ancla de calibración** (no existe minuta ni la
> `matriz-trazabilidad.csv` que menciona la cabecera del archivo). Se citan las marcas
> **raw tal cual**; si aplicara el mismo factor ÷10 la reunión duraría ≈1 h 56 min, pero
> el comentario «Sí, estamos a la hora» aparece en raw `17:35:30` (≈1:45 bajo ese
> factor), así que **el factor no está confirmado para Reu1**.
>
> **Nota de método — diarización.** En Reu1 la diarización está rota: hay bloques
> atribuidos a `Speaker 01` que son claramente del cliente (p. ej. raw `14:51:20`
> describiendo los auxiliares contables) y bloques de `Speaker 00` que contienen
> interjecciones del proveedor («Exacto», «Ideal», «Sería perfecto») embebidas en el
> mismo párrafo. Cuando una frase de requisito puede ser de cualquiera de los dos, se
> marca explícitamente **[atribución dudosa]**.

---

## Ficha

### Reu1 — Demo Agrosoft, 21/07/2026

| Campo | Detalle |
|---|---|
| Archivo | `fuentes/transcripcion.md` (57.556 bytes) |
| Video | `c:\Users\c\Videos\Screen Recordings\Screen Recording 2026-07-21 120114.mp4` · tl;dv `6a60394d4959970013159ad2` |
| Participantes | **2 hablantes.** `Speaker 00` = **cliente**, quien comparte pantalla y opera Agrosoft con perfil de administrador; casi con certeza **María José (MJ)** — habla en tercera persona de «María Jesús» al describir el escenario de aprobación (raw `08:18:31`) y dice «yo tengo el perfil de administrador» (raw `02:51:40`). `Speaker 01` = **proveedor** (Carlos Vallejos). *No confirmado al 100% por la diarización rota.* |
| Mencionados sin estar presentes | **Juan Agustín** (jefe que aprueba OC), **Mario** (control de gestión, «vuelve en agosto») |
| Duración | Última marca raw `19:21:50`. Duración real **no determinada** (ver nota de método) |
| Temas | Login/multiempresa · Mano de obra (no usado) · Contratistas · Compras (OC, aprobación, recepción) · Registro de compra · Insumos/Bodega · Maquinaria (no usado) · Contabilidad (plan de cuentas, dimensiones, carga masiva) · Gestión (no usado) · Parámetros generales e indicadores Banco Central |
| Carácter | **Recorrido pantalla por pantalla del sistema en producción**, con incidencias reales demostradas en vivo (se crea la OC 5207 y se pide «vamos a ir anotándola para después eliminarla») |
| Minuta IA | **No existe** |

### Reu2 — Demo Agrosoft + AgroSmart, 23/07/2026

| Campo | Detalle |
|---|---|
| Archivo | `fuentes/transcripcion-reunion2.md` (70.606 bytes) |
| Video | `fuentes/videos/reunion2-2026-07-23.mp4` · tl;dv `6a624d3ff324400013c736cb` |
| Participantes | **3 hablantes.** `Speaker 00` = **Rodrigo** (cliente; «el encargado de la agrícola contablemente», raw `10:40:11`) — demuestra contratistas y AgroSmart. `Speaker 01` = **María José / «Mari»** (cliente) — Carlos la llama «Mari» en raw `12:42:00` y `13:23:10`; ella cierra con «Estamos entonces, Carlos». `Speaker 02` = **Carlos Vallejos** (proveedor) — «chicos, estoy grabando». |
| Mencionados sin estar presentes | **Sergio** (proveedor), **Agustín** (cliente, tiene las cartolas), **Mario** (centros/elementos de costo), **Cristian** (comercial de GoSocket) |
| Duración | **≈1 h 20 min 27 s** (raw `13:24:31` ÷10) |
| Temas | Contratistas end-to-end (tarifario → contrato → enrolamiento → control de producción → proforma → factura → asiento) · AgroSmart como referencia de UX · Libro de ventas · Tesorería (calce, anticipos, conciliación, cartola) · Maqueta del ERP nuevo, roles y permisos · Migración Acepta→GoSocket · Metodología y cronograma |
| Minuta IA | `fuentes/reunion2-minuta-tldv-2026-07-23.md` (1.175 bytes; 6 action items y **cero contenido temático**) |

---

## As-is Agrosoft

Estructura del producto según la propia demo: Agrosoft es un conjunto de módulos
(**mano de obra, contratistas, compras, insumos, maquinaria, contabilidad, gestión,
parámetros generales**) donde *contabilidad* actúa de núcleo: «aquí centraliza
contabilidad, proveedores, ventas, tesorería y activos fijos» (Reu1 raw `14:30:00`).
Cada módulo satélite tiene el mismo tríptico: **parametrización → procesos diarios →
traspaso contable + cierre de mes → informes**.

### 1. Acceso, multiempresa y temporada

- Se entra por un link externo a Agrosoft; usuario y clave. **Queda siempre en la
  última empresa trabajada** y hay un «cambio de empresa» que lista las empresas a las
  que el usuario tiene acceso (Reu1 raw `00:40`).
- Al cambiar de empresa pide **mes contable y mes de remuneración**; luego entra al
  módulo de AlmaWeb.
- Existe **cambio de temporada**, pero: *«nos dimos cuenta que en realidad el cambio de
  temporada en esta página no sirve mucho porque nosotros no usamos el módulo de
  gestión. Pero igual sería bueno implementarlo en el ERP nuevo.»* (Reu1 raw `00:40`).
- **15 usuarios contratados y se cobra por usuario adicional.** Consecuencia operativa:
  *«hay veces en que un usuario lo ocupan 2 personas»* → si dos personas comparten
  usuario y una cambia de empresa, la otra sigue trabajando en la empresa equivocada:
  *«si no se da cuenta, le permite seguir ingresando información en una empresa
  diferente.»* La sesión además caduca sola cada cierto tiempo (Reu1 raw `00:40`, `27:40`).
- **Fuga de contexto de empresa (aparece tres veces, en tres módulos distintos):**
  - Centros de costo: *«si yo estoy trabajando en ALM, me permite seleccionar centros de
    costos de otra empresa»* (Reu1 raw `01:54:10`).
  - Distribución de OC: *«yo estoy en Alem, pero yo podría poner Almaue, por ejemplo, o
    Santa Pilar y me deja»* (Reu1 raw `05:56:50` aprox., bloque de la OC).
  - Bodegas: *«me aparecen igual todas las bodegas de la otra empresa… si yo estoy en LM,
    debería ser sí o sí solamente LM»* (Reu1 raw `11:17:10`).

### 2. Mano de obra — **no lo usan**

Parametriza labor, actividades, horarios, previsiones, sistema de previsión de salud y
todo lo de liquidación. *«actualmente nosotros trabajamos con Book, entonces este módulo
para nosotros no es relevante»* (Reu1 raw `00:40`). **[transcripción dudosa: «Book» es
casi seguro «BUK», software chileno de remuneraciones; no está deletreado en la fuente.]**

Consecuencia de diseño: como **actividades y labores viven en mano de obra** y ese módulo
no se implementará, *«lo queremos parametrizar en lo que es en el módulo de
contratista»* (Reu1 raw `39:50`). Y: *«en un futuro no va a ser mano de obra, sino que va
a ser todo contratista»* (Reu1 raw `04:33:01`).

### 3. Contratistas

#### 3.1 Maestro y estructura de datos (Reu2 raw `36:51` ≈ `03:41`)

- **Maestro de contratistas**: nombre + RUT. *«esa es como la utilidad de este módulo»*.
- **Segunda base**: labores con actividades.
- La actividad es la agrupación general y la labor lo específico: *«tratamos de que la
  actividad sea como general y la labor sea más específica»* (Reu1 raw `01:13:01`).
  Ejemplo real: actividad **«armado de caja»** ← labor **«packing cereza»**; se muestra
  cómo anexar la labor **«pintar troncos»** (Reu1 raw `01:20:41`).
- Enrolamiento del contratista con «planilla de datos»; historial y **cambio de vigencia**
  (vigente / no vigente) para dejar de mostrarlo (Reu1 raw `01:07:10`).

#### 3.2 Tarifario — el dolor número uno

Campos: año, mes, código, contratista, labor, **unidad de control / unidad de medida**
(por formato o **a trato**), fecha desde–hasta, **centro de costo**, tarifa
(Reu1 raw `01:20:41`; Reu2 raw `50:51` ≈ `05:05`).

- **No hay listado.** *«si ingreso 2, la que ingresé primero no se me visualiza… queda
  siempre la duda si yo la ingresé o no la ingresé… no hay un listado, entonces no me
  permite revisar si tengo algún error»* (Reu1 raw `39:50`, `01:46:11`).
- Para agregar otra labor hay que limpiar el formulario y empezar de nuevo (Reu1
  raw `01:20:41`).
- Rodrigo lo reproduce en vivo con la labor «amarras laterales» a **36.500**: *«me borra
  los datos anteriores. Entonces yo para poder visualizarlo tengo que volver a entrar al
  módulo»* (Reu2 raw `01:00:00` ≈ `06:00`).
- La opción «buscar» existe **solo como informe**, no permite agregar ni modificar sobre
  el mismo tarifario (Reu1 raw `39:50`).
- **Cuestionamiento del propio concepto de tarifario** (Rodrigo, Reu2 raw `01:06:51`
  ≈ `06:41`): *«el tarifario es como bien complejo porque a veces los precios van
  cambiando… Se nos hace más fácil como colocarlo dentro del mismo proceso de inmediato
  en vez de hacer un tarifario antes de poder trabajar.»*

#### 3.3 Ciclo completo (Reu2, demostrado paso a paso)

1. **Ingreso de contratos** (raw `01:06:51` ≈ `06:41`): contratista, estado («siempre
   tiene que estar activo»), **tipo de contrato «mano de obra»**, fecha de emisión, fecha
   de inicio y término del trabajo (16 al 30 de junio), **faena** — *«tenemos hartas, pero
   al final siempre usamos que una faena agrícola, como un dato, un paso de más»* — y de
   nuevo la fecha de inicio. Genera **folio 179**, que el operador debe anotar a mano.
2. **Enrolamiento de personal**: nombre de la persona, fecha de inicio, activo, **jefe de
   cuadrilla**.
3. **Control de producción** — labores diarias. Hay que reingresar fecha, faena y jefe, y
   seleccionar los centros de costo uno a uno.
   - **Relación actividad↔labor invertida** (raw `01:36:40` ≈ `09:40`): *«tengo que
     saberme de memoria cuáles son las actividades… uno ingresa a la labor y después te
     pide la actividad, y no puede entrar a la labor si no se sabe la actividad. Entonces
     como que medio enredado.»* Ejemplo: «abrir carpas» está bajo la actividad «techos»,
     no bajo «diversas labores».
   - MJ (raw `01:43:21` ≈ `10:20`): *«si uno por ejemplo pincha la labor, te sale como a
     qué actividad está asociada, sino que te salen todas, y es innecesario.»*
   - **El precio viene del tarifario y no se puede editar aquí** (raw `01:45:51`
     ≈ `10:35`): *«de repente pasa que terminan de hacer los trabajos y después de que
     terminan de hacer los trabajos muchas veces se da el precio. Entonces no nos sirve
     para llevar un control diario sobre quién está yendo, cómo llevar asistencia… se nos
     haría más fácil ingresar diariamente, pero no podemos porque como no manejamos el
     precio todavía muchas veces.»*
4. **Emisión de proforma** (raw `01:56:40` ≈ `11:40`): se elige contratista (**nº 6, Gómez
   y Gómez**) y **folio 179**. El reporte se activa vía PDF y hay dos: **borrador** y
   **definitivo**.
   - *«si uno pone el definitivo, sí o sí se va a emitir como todo el proceso, como que no
     hay ningún filtro antes, como de si está seguro, como para validarlo, para poder
     revisar.»*
   - Contenido de la proforma: detalle + plantilla principal con faena, cantidad, precio
     total (**37.500** por una jornada), **neto, IVA, total**.
   - *«uno le va mandando estas cosas a los contratistas para que ellos después puedan
     hacer la facturación, según lo que nosotros tenemos informado.»* ← **la proforma es
     el documento que el mandante envía al contratista para que éste facture.**
   - Definitiva asigna folio (**155**); en borrador el folio de factura queda en 0.
5. **Asociación proforma↔factura** en *Proveedores › Procesos diarios*, con **tipo de
   compra = contratista** (raw `02:26:01` ≈ `14:36`).
   - **Limitación dura:** *«las proformas, nos deja hacer una proforma por mes. Entonces
     hay veces en las que se juntan 2 meses… necesitamos hacer dos proformas distintas
     para esa factura. Pero si hacemos las dos proformas, no nos deja asociarlas después
     dentro de este módulo.»*
   - **Workaround real:** se ingresa todo dentro de un mes y se lleva un **segundo
     registro fuera del sistema**: *«tenemos 2 registros al final, uno que lo lleva un
     poco más administrativamente… se abrió carpa en enero y en febrero, pero yo ingreso
     todo en febrero en el sistema porque se hace más sencillo»* (raw `02:40:31`
     ≈ `16:03`).
   - MJ pone el costo del workaround (raw `02:45:50` ≈ `16:35`): *«eso impide que haya un
     poco de gestión, porque si ven el comportamiento de… el costo de abrir carpas
     mensualizado, no se refleja la realidad.»*
6. **Emitir factura / cierre**: *«cada contrato tenga anexado solamente una factura, y no
   te deja cerrar el módulo hasta que todos los contratos están asociados a un
   documento»* (Reu1 raw `02:51:40`). En borrador se puede corregir el contratista; **en
   definitiva no**: *«si yo pongo definitiva, no me deja modificarlo… ahí tengo que
   reversar y tengo que modificar para atrás.»*

#### 3.4 Efecto contable de contratistas

- Al contabilizar la factura se reconoce el costo del trabajo y una subcuenta **«facturas
  por recibir contratistas»**; la factura entra *facturas por recibir contratistas contra
  el proveedor (contratista)* (Reu1 raw `02:51:40`).
- Rodrigo lo muestra al revés, desde la proforma (Reu2 raw `02:56:10` ≈ `17:37`): al
  cierre de mes se arma un asiento **«facturas de contratistas por recibir»** (con RUT del
  contratista y referencia a la proforma 155) **contra «costo por mano de obra
  contratista, o la cuenta que seleccionemos»**. Y: *«El efecto contable al final se arma
  siempre de todo contra mano de obra contratista, contra la suma de todas las proformas
  que estén dentro del mes.»*
- **Traspaso contable** del módulo (Reu1 raw `02:51:40`): pide **tasa de cambio**,
  «contabilizar» y genera el asiento, que luego se traspasa a contabilidad. En
  contratistas el proceso queda cerrado; **en contabilidad queda abierto** hasta que
  llegue la factura.
- **Cierre de mes**: el administrador cierra el mes e impide al digitador seguir
  ingresando. *«el perfil de digitador no tiene parametrización y no tiene… ni el traspaso
  contable ni el cierre de mes.»*

#### 3.5 AgroSmart — referencia de UX que el cliente pide replicar (Reu2)

Contexto (MJ, raw `22:41` ≈ `02:16` y raw `03:55:51` ≈ `23:35`): evaluaron migrar a
AgroSmart («una página especialista en productores… en el campo») **por el módulo de
contratistas**, pero *«tuvimos problemas en el módulo de contabilidad… nos duplicaba
registros, nos daba unas centralizaciones súper descuadradas, así que no confiamos en el
sistema y nos mantuvimos en AgroSoft.»* Siguen con acceso: *«aún no nos han eliminado»*,
y el material es **confidencial**.

Lo que hace bien AgroSmart, demostrado en vivo:

- **Ingreso múltiple de registros de mano de obra** (raw `03:03:10` ≈ `18:19`): empresa,
  fecha, **cuartel**, faena, **formato de pago (trato o jornada)**, unidad de pago (por
  kilos cosechados, bins, capachos…), jornadas y duración (20 jornadas × 8 h = 160 h),
  **valor unitario o valor jornada** (37.500), y suma automática del gasto.
- **Tarifario editable en línea**: *«uno podía ingresar el tarifario diario y lo podía
  editar también»* (MJ, raw `02:50:41` ≈ `17:04`).
- **Asignación de facturas** (raw `03:30:10` ≈ `21:01`): pantalla con **todas las labores
  ejecutadas aún no asociadas**; se elige una factura del proveedor (ej. factura 120 de
  *Sociedad Agrícola Guarachi*) y se van marcando labores; el sistema **descuenta del
  total hasta calzar** (2.550.000 − 825.000 …). Ejemplo de línea: 21/10, aplicación de
  herbicidas / control de maleza, 150.000 pagados por jornada.
- Debilidad demostrada: por una actualización en curso, el registro **no trae el maestro
  de contratistas**, solo «trabajador interno» (raw `03:03:10`).
- **Requisito que sale de aquí** (Rodrigo, raw `03:51:00` ≈ `23:06`): *«como nosotros
  trabajamos un poco al revés, nosotros hacemos la proforma primero… después de haber
  anotado todas las labores diarias, yo poder ver todas las labores que tengo anotadas y
  decir ya, esta, esta, esta, hago una proforma.»*
- **Magnitud del dolor actual** (raw `04:08:00` ≈ `24:48`): *«cuando empezamos a hacer las
  proformas de contratistas en AgroSoft la primera vez no alcanzamos a hacer una en todo
  un día de trabajo porque es muy largo el proceso, es muy engorroso.»*
- Decisión del proveedor (Carlos, raw `04:17:21` ≈ `25:44`): tomar de AgroSmart **solo
  esta parte**; el resto de la funcionalidad se basa en Agrosoft.

### 4. Compras

#### 4.1 Maestro de artículos duplicado

- El maestro existe **en Compras y en Insumos** y es el mismo: *«está como duplicado. O
  sea, es que al final, si yo lo creo arriba, igual me aparece abajo»* (Reu1 raw `04:54:20`).
- Compras mezcla **servicios** con **materiales/existencia**; «otros artículos» son
  **activos fijos**.
- Práctica del cliente: *«nosotros siempre cuando creamos insumos o artículos los creamos
  en el módulo de insumos»*, y preferencia explícita: *«yo como que prefiero que lo que es
  maestro de artículos quede en el módulo de insumos»* (Reu1 raw `10:54:01`).
- **No valida duplicados.** Demostrado en vivo con familia «materiales de embalaje»,
  subfamilia «materiales de embalaje separadores», artículo «bolsas», unidad: se crea dos
  veces con datos idénticos sin advertencia. *«lo puedo crear 20 veces y después cuando la
  persona quiere comprar bolsas, él va a poner bolsa y va a apretar cualquiera. Y si yo
  aprieto 10 distintas, cuando yo saqué el mayor de insumos me va a aparecer en 10 partes
  diferentes, mi stock.»*

#### 4.2 Solicitud de compra — **no la usan**

*«acá está el módulo de solicitud de compra, pero nosotros no lo usamos. Nosotros nos
vamos directo a realizar la orden de compra… como siempre hemos trabajado sin solicitud,
en realidad como que esto no debería ir.»* (Reu1 raw `05:56:50`).

#### 4.3 Orden de compra — campos y flujo

Campos demostrados (Reu1 raw `05:56:50`): sin solicitud · **departamento** (hoy son 2) ·
solicitante · fecha · **jefe que aprueba** (Juan Agustín) · proveedor · **tipo de pago
(contado / 15 días / 30 días)** · moneda (siempre pesos, a veces dólar) · observación ·
tipo de cambio · **tipo (servicio / existencia / activo fijo)** · artículo · cantidad ·
precio · distribución de costo · afecto/exento.

- **Tipo de cambio que no sirve:** *«acá me arroja el tipo de cambio, pero este tipo de
  cambio que me arroja después no me lo reconoce al momento de yo registrar la orden de
  compra. Se registra a la fecha en que yo recepciono la orden de compra.»*
- **Distribución de costo — tres modos:** *por hectárea*, *por grupo de centro de costo* o
  *directo*. Hoy usan **directo** (centro de costo + elemento de costo + monto). El modo
  por hectárea está descartado por rigidez: *«si queda mal ingresada una hectárea, queda
  eternamente mal parametrizado en la imputación del costo… si yo quisiera por hectárea y
  quiero que solo un cuartel no esté dentro de esa hectárea, no me deja editarlo para
  eliminar solo ese cuartel. Es como todo o nada.»*
- **Descuadre silencioso:** se distribuyen 1.010 contra un neto de 1.000 y el sistema deja
  agregar sin avisar; recién al guardar aparece *«distribución del centro de costo no
  cuadra con total neto»* y hay que rehacer todo. *«puedo poner más de una actividad,
  entonces al final no te va a decir en cuál tú tienes la diferencia.»*
- **Afecto/exento**: si es afecta calcula IVA y neto; si es exenta va todo a exento.
  *«esto influye mucho para cuando llega la factura, porque lo asimila al tiro… de que el
  documento que tengo que asociarlo tiene que ser exento.»*
- Al grabar se genera el número: **OC 5207**. Estado inicial **pendiente**.

#### 4.4 Visibilidad y búsqueda de OC — dolor grande

- *«en el caso de la persona que lo crea, lo puede visualizar acá. Si yo me meto y lo creó
  otra persona, a mí no me aparece en este módulo la que creó.»*
- **Informe de OC exige elegir el estado** entre **anulada, aprobada, cerrada,
  contabilizada, pendiente, recepcionada parcial, recepcionada total** (7 estados):
  *«Si yo no tengo idea, tengo que buscarla módulo por módulo.»*
- Buscar por **número** sí funciona con cualquier estado. Buscar por **proveedor** solo
  devuelve las contabilizadas: *«al final tampoco me sirve buscar por el proveedor… y
  además las ordena de la más antigua a la más reciente.»*
- **No hay informe de qué OC tiene tal proveedor** ni el proveedor aparece en el informe
  de OC contabilizadas.

#### 4.5 El orden real del proceso está invertido

Dato duro que contradice el flujo teórico (Reu1 raw `07:12:41`):
*«nosotros cuando creamos la orden de compra, como la creamos primero, o sea, se emite la
factura y después creamos la orden de compra, nosotros en la observación ponemos factura
tanto, no sé, servicio de reparación de activos.»* Y a continuación: *«Se supone que
primero va la orden de compra y después la factura. Lo que pasa es que igual actualmente
lo hace el departamento de contabilidad lo que es la creación de las órdenes de compra,
pero lo ideal es que después cada departamento se encargue de su creación de orden de
compra. Entonces igual necesitamos que los pasos sigan iguales de aprobación y
recepción.»*

#### 4.6 Aprobación de OC

- Módulo *Aprobación orden de compra*: el aprobador ve las OC asignadas a él; puede
  **aprobar o rechazar**. Se demuestra con la 5207 asignada a Juan Agustín (Reu1
  raw `08:18:31`).
- **No hay ninguna notificación**: *«si yo me meto en aprobación orden de compra me
  aparece, pero no me llega ningún correo, nada de que alguien me solicitó una orden de
  compra.»*
- Preferencia explícita por **badge**, no correo: *«O por último, aquí que aparezca un
  icono de pendientes, no sé, como un icono rojo… quizás no mucho el correo porque igual
  sería tedioso que a cada rato que estén ingresando órdenes de compra me vaya llegando un
  correo, pero sí al momento de meterme a la página y que me aparezca como un pendientes.»*
- El solicitante **no ve** cerrar / reactivar / aprobación / recepción; solo el informe.
  *«Estos 3 módulos quedarían solamente para las personas que tienen acceso a aprobar y
  anular.»*

#### 4.7 Recepción de OC → asiento

- Recepción pide **solo la fecha**. *«ahí es cuando se me reconoce con el tipo de cambio
  de la fecha que yo recepciono el gasto.»*
- **Problema estructural con productores** (Reu1 raw `08:47:00`): *«a veces el tipo de
  cambio es promedio. Entonces no existe una fecha exacta donde a mí me dé el tipo de
  cambio exacto del costo de la fruta. Entonces acá se me genera mucha diferencia entre lo
  que yo imputo contablemente y lo que yo pago, porque en el módulo de pago a mí me
  permite poner el tipo de cambio manual… yo lo pago al tipo de cambio que estoy
  negociando, pero en realidad yo estoy reconociendo mi costo al tipo de cambio de un día X.»*
- Asiento generado (comprobante **8310**, glosa «orden de compra de servicios, la 5207 del
  7 del 26»): **Mantención y reparación de activos (gasto) contra Facturas por recibir
  servicios**, expresado en peso y dólar.

#### 4.8 Registro de compra (Proveedores › Procesos diarios)

- Se elige proveedor y **tipo de compra** (existencia / activos fijos / servicios) para que
  aparezcan las OC disponibles.
- **Regla dura** (Reu1 raw `10:54:01`): *«Siempre que la orden de compra esté aprobada y
  recepcionada, ya sea insumo o servicio, me va a aparecer el registro de compra. Si está
  solamente en estado aprobada, no me aparece.»*
- Al doble clic sobre la OC trae cuenta «facturas por recibir servicios», auxiliar del
  proveedor, OC, monto y TC. **La cantidad nunca aparece.**
- **Bug de cruce de proveedor**: *«si yo pongo Sandoval y Fuentes y me coincide el monto de
  la orden de compra, me deja contabilizarlo cruzado.»*
- **Parche del tipo de cambio**: se puede editar el TC en el registro de compra (se muestra
  9,10 vs 9,33 — **[ambiguo: casi seguro 910 y 933 CLP/USD]**) pero *«se me modifica
  solamente la parte del proveedor, no la parte del costo… fue una solución parche que nos
  dieron… Pero no nos dieron una solución del tipo de cambio de recepción.»* Preferencia
  del cliente: *«quizás dejarlo como más rígido y no dejar modificar acá, sino tener que
  modificar directamente en la recepción.»*
- **OC exenta + factura afecta se contabiliza igual**, sin alerta. La discusión que sigue
  es matizada y **el cliente pide NO endurecerlo**: *«hay facturas que son afectas que
  traen montos exentos… y también hay facturas… de combustible, que traen el impuesto
  específico. Entonces creo que la orden de compra trae el módulo para dejarlo como afecto
  exento, pero en realidad no tiene mayor implicancia en el módulo de registro de compra
  porque si no quedaría como muy rígido y quizás impediría el ingreso de alguna factura.»*
  Práctica actual: *«las facturas que traen exento y afecto, nosotros tenemos que, para
  hacer la orden de compra, sumar el neto y el exento para poder ingresar el costo.»*
- Valida cuadratura del asiento y **exige glosa** antes de grabar.

### 5. Insumos / bodega

- Submódulos: maestro de artículos, **bodegas**, **nivel de almacenamiento**, ingrediente
  activo, unidad de medida, parámetro de contabilización, movimiento de bodega, informes,
  traspaso a contabilización, cierre de mes (Reu1 raw `10:54:01`).
- **No usan** ingrediente activo ni unidad de medida — pero: *«para lo que es el área
  agrícola sería bueno que tuviera los ingredientes activos y la unidad de medida, porque
  ellos lo podrían usar para el tema de las aplicaciones.»*
- **Nivel de almacenamiento: no lo usan.** *«Siempre son 3 niveles»* pero no está
  parametrizado. Ratificado en Reu2 (raw `12:44:20` ≈ `1:16:26`): *«ni siquiera lo tenemos
  como parametrizado… lo que ingresamos a la bodega sabemos dónde está, en qué bodega, y
  los movimientos que se hacen.»* Carlos cierra: *«De momento no hay una necesidad de tener
  todos los niveles.»*
- **Bodegas**: se crean por número (se demuestra crear la bodega 24 tras la 23). Bodega
  operativa nombrada: **Chamonate** — *«Siempre pongo Bodega Chamonate.»*
- **Parámetro de contabilización**: por **tipo de movimiento + familia + subfamilia** se
  define **cuenta al debe y cuenta al haber**. Ejemplo demostrado: entradas de bodega de
  «materiales de embalaje / separadores» → **existencia**; consumo/baja → **costo
  materiales de embalaje**.
- **Movimiento de bodega in situ**: se selecciona la OC y el tipo de movimiento (entrada
  desde proveedor / compra); el sistema muestra **saldo y total** (ejemplo real: compradas
  800, ingresadas 398 → estado **parcial**); proveedor automático desde la OC; bodega
  destino; observación; tipo de cambio de compra; artículo y cantidad. También hay
  **traspaso entre bodegas** y **devolución**.
- **Problema de valorización con notas de crédito** (Reu1 raw `12:17:30` aprox.): la bodega
  valoriza a **precio promedio ponderado**. Ejemplo dado: hay bolsas a 100; se compran
  1.000 a 110 → promedio 105. *«cuando yo tengo una nota de crédito que va directamente a
  una factura en específico, no me deja sacar esa cantidad por el precio de la factura, me
  la saca de bodega a precio promedio… a nosotros en contabilidad se nos genera una
  diferencia cuando llegan notas de crédito, ya sea para arriba o para abajo.»* Caso
  típico: se compró 1.000, llegaron 900, NC por 100.
- Mismo cierre que contratistas: traspaso a contabilización → contabilidad → cierre de mes.

### 6. Maquinaria — **no lo usan en ningún rubro**

*«se supone que el módulo de maquinaria es para el área agrícola, que tiene tractores,
tiene pulverizador… esto es para ver las mantenciones, ver el desgaste. Y para hacer el
prorrateo, por ejemplo, si yo tengo un tractor y lo ocupo en 5 cuarteles, hacer el desglose
por cuartel o por labor… este módulo sería como ya la necesidad de lo que queremos ver,
pero en sí no lo usamos en ningún rubro.»* (Reu1 raw `13:32:20`).

### 7. Contabilidad

#### 7.1 Plan de cuentas y dimensiones (Reu1 raw `14:30:00`–`14:38:00`)

- Se agrega / elimina / modifica el plan de cuentas. **Por cuenta se declara qué
  dimensiones exige**: centro de costo, área de negocio, especie, variedad, elemento de
  costo, nivel. *«todas las que son N son las que no se requieren.»*
- **Inactivación = marcar «no imputable»**: *«si no quiero que la utilicen, pongo no
  imputable y pongo guardar. Entonces nadie puede utilizar esa cuenta.»*
- Se parametriza qué se ve en **estado de resultados** y **estado de situación financiera**.

#### 7.2 Catálogos contables

- **Auxiliares**: tipos de auxiliares y cuentas auxiliares (personal contratado,
  instituciones de previsión).
- **Tipos de referencia** — los que se eligen en el libro de compras. Se crean con **código
  + descripción**; se menciona *«el 31 lo creé»* **[el 31 no corresponde a un tipo de DTE
  SII estándar; la transcripción no aclara si es un código interno]**. En otro módulo se
  declara si ese tipo lleva impuesto específico o exento.
- **Área de negocio**, **elemento de costo** (crear/modificar/eliminar en línea).
- **Código financiero** (Reu1 raw `15:19:10`): *«lo usamos netamente para el flujo de caja,
  para todo lo que tiene que ver con movimiento de banco y tesorería… dependiendo del
  código financiero se parametriza para que cuando yo saque el flujo de caja me aparezca si
  es ingreso cereza, si es ingreso de la exportación, si es venta de agroquímicos»*, o
  «venta exportación cereza» / «venta exportación nectarina». En Reu2 se ve en uso: para un
  productor el código financiero es **materia prima** (raw `08:37:01` ≈ `51:42`).
- **Tipos de comprobante** (6): apertura, egreso, ingreso, proveedores, traspaso, venta.
- **Tipos de impuestos**: IVA **19 %** y retenido **19 %** (dicho como «0,19 %»);
  **honorarios con factor actual + factor anterior + fecha desde**, para reflejar el
  aumento anual de la retención. **[Los porcentajes citados —«del 15 a 25» y «del 14 a 5»—
  están mal transcritos; probablemente 15,25 % y 14,5 %.]** Falta historial: *«El cómo,
  quién fue que modificó… sí, estaría bueno»*.

#### 7.3 El problema de las dimensiones libres (requisito de negocio importante)

Reu1 raw `15:19:10`: hoy artículo, centro de costo y elemento de costo *«podemos mezclarla
como nosotros queramos. La idea sería que se fueran asociando, porque así cada departamento
trabaja con sus centros de costos y sus artículos más rígidos.»* El síntoma concreto:
*«le preguntamos al jefe de área industrial: esta factura, ¿a qué va? Ya dice, no sé,
movimiento de envase, elemento de costo movimiento de envase. Después le preguntamos lo
mismo y dice ya centro de costo cereza, elemento de costo bodega. Entonces al final es el
mismo concepto y vamos cambiando el elemento de costo.»* Lo que piden: que el área
industrial, al usar los centros de costo de bodegas, solo pueda usar elementos de costo de
esa área (movimiento de envases, limpieza de envases, reparación de envases…).

#### 7.4 Elementos de costo sin inactivación

*«actualmente los elementos de costo nosotros los podemos modificar, editar o eliminar,
pero no nos deja anular el uso… obviamente sabemos que no lo podemos eliminar por la
información histórica, pero igual hay muchos elementos de costo que ya no se usan.
Entonces, cuando uno quiere seleccionar elementos de costo, te aparece el paño de
elementos de costo. Están los porque sí, los porque no, y los por si acaso.»*

#### 7.5 Exportación de informes

Se puede exportar a Word, PDF, PowerPoint y Excel. *«Siempre usamos Excel, pero nunca está
de más tener el PDF… Para nosotros Excel es sagrado.»* Además: *«eso fue una mejora que fue
implementada hace poco porque antes se podía sacar solo en PDF.»*

#### 7.6 Comprobantes y carga masiva (Reu1 raw `16:23:01`–`17:28:11`)

- Procesos diarios: comprobantes de **ingreso, egreso y traspaso** (proveedor y venta se
  hacen en sus propios módulos). El traspaso se usa para reclasificar centro de costo.
- **Carga masiva de comprobante contable** — funcionalidad reciente y muy valorada:
  *«Antes no teníamos esta opción, teníamos que digitar si eran 200 líneas, las 200
  líneas… Más cuando se te cerraba la sesión en el movimiento 180.»*
  - Archivo Excel *«especial que nos creó Agrosoft con campos específicos, con tipo de
    documento específico»*. Se sube, se pone glosa, valida y guarda.
  - **Validaciones que hace**: periodo contable de cada línea; diferencia debe/haber = 0
    **en peso y en dólar**; línea que trae centro de costo cuando la cuenta no lo requiere;
    línea a la que falta centro de costo, elemento de costo o área de negocio.
  - Uso principal: **centralización de remuneraciones** (que vienen de fuera del sistema).
  - Dolor: errores opacos. *«una celda se había cambiado de número a texto»* y costó
    encontrarlo; *«tengo que buscar un archivo que esté como listo para subir, para poder
    modificarlo recién y subirlo.»*
  - La **glosa** es la clave de búsqueda posterior («centralización de remuneraciones mes
    de junio»).

### 8. Ventas / libro de ventas (Reu2 raw `04:39:40` ≈ `27:58`)

- El módulo de ventas **es** el libro de ventas: ahí se ingresan los documentos emitidos.
- Campos: **tipo de documento**, número, **tipo de venta (contado / 15 días / 30 días)**,
  documento asociado si es **nota de débito o nota de crédito**, cliente (trae sus datos),
  número de despacho, teléfono, fax *(«lo demás no es necesario rellenarlo»)*, **módulo de
  venta** (ej. «Mercado Nacional»), **centro de costos**, **área de negocio**, cantidad,
  precio unitario.
- **«Guardar» vs «grabar»**: guardar es temporal, no genera registro contable y no aparece
  en reportes. Veredicto del cliente (raw `05:46:20` ≈ `34:38`): *«en este módulo al menos
  el guardar está de más porque en realidad no se ocupa… si comete el error de guardarlo,
  después yo quiero sacar un informe, me va a aparecer que el documento aún está pendiente
  de ingreso. Eso no tiene como mayor utilidad. Aquí sería solamente grabar, grabar y
  contabilizar.»*
- **Limitación central**: *«al momento de ingresar todos los datos, si yo la guardo y
  después la quiero reversar, no puedo solo editar lo que me equivoqué, tengo que ingresar
  el documento totalmente completo de nuevo»*, a diferencia de compras y contabilidad donde
  sí se edita la línea. *«No se puede modificar un RV reversado, ingresar todo de nuevo.»*
- **Cuándo aparece el error**: *«Puede ser en el mismo instante o puede ser cuando ya
  hacemos la revisión del mes.»*
- **Modelo de reversa que el cliente describe como correcto** (raw `05:39:21` ≈ `33:56`):
  *«el 472 queda con el original, que es el reversado. El 473 debería ser la reversa para
  que me quede cero en la contabilidad, y el 474 el nuevo registro.»* Lo único que falta es
  **reutilizar los datos del documento reversado**.
- **Bug de búsqueda demostrado en vivo**: el documento recién grabado no aparece al
  buscarlo, y cuando aparece muestra el cliente equivocado (Chamonate en vez de Sandoval y
  Fuente). Carlos deja constancia del número en la grabación para que puedan borrarlo.
- **Diagnóstico de aislamiento del módulo** (raw `06:30:51` ≈ `39:05`): *«estos módulos
  están súper conectados, pero el módulo de venta queda aparte, no tiene como esa
  interacción.»*

### 9. Tesorería (Reu2 raw `05:56:10` ≈ `35:37` en adelante)

Frase que enmarca todo el módulo (MJ): *«por el lado de tesorería, acá tenemos un tema
grande porque en este ERP no está hecho para conciliar. Ni para hacer los calces de lo que
es el pago y la factura. Entonces… nosotros lo hacemos, pero lo hacemos de una manera que
es como parche, y ahí se generan varias diferencias.»*

#### 9.1 Calce (pago a proveedores / cobro a clientes)

- Pantalla con las facturas por banco (Banco de Chile). Se pone fecha, banco, moneda del
  calce, número de movimiento, y se marcan los documentos. También se pueden ingresar
  movimientos directos (comisiones).
- **Bug**: *«me dejó guardar y no había pinchado nada… debería darme una advertencia que en
  realidad no estoy pinchando nada.»*
- Al grabar se hace el asiento de banco y la rebaja de la factura contra el comprobante del
  banco (ejemplo: 46.000 pesos).
- **Estado de cuenta**: documento pendiente muestra total y saldo; si se paga menos, el
  saldo queda actualizado (se demuestra dejando saldo 30).
- Reversa: genera **reversado + reversador** de forma automática. Requisito de MJ: *«que se
  refleje también de la misma forma en el otro módulo»* [el de ventas].

#### 9.2 Bug de doble moneda — asimétrico

Demostrado dos veces con el mismo productor y el mismo par factura+anticipo
(raw `08:37:01`–`09:06:11` ≈ `51:42`–`54:37`):

- Calce **en pesos** (anticipo 2.718.836): el monto en pesos queda en 0 pero queda una
  **diferencia en dólares** que el asiento **no calcula**. *«no me calcula la diferencia en
  dólares, a diferencia del otro lado. No me la calcula, como que me la oculta.»*
- Calce **en dólares** (−342,80): el monto en dólar queda 0 y el sistema **sí** genera la
  diferencia en pesos como **«ajuste automático»**. *«esto está bien.»*
- Conclusión del cliente: *«eso como que nosotros no nos explicamos por qué sí lo hacen
  cuando pagamos en dólar en pesos, pero no lo hace cuando lo hacemos en pesos en dólar, si
  se supone que tiene doble moneda.»*
- Hipótesis interna: *«me explicaron que el módulo no estaba hecho para calzarlo.»*

#### 9.3 Anticipos a productores

- *«nosotros acá igual trabajamos con mucho anticipo, entonces el anticipo tú sí o sí lo
  tienes que ingresar en el módulo de contabilidad»* (raw `08:06:50` ≈ `48:41`).
- En el estado de cuenta del productor conviven facturas y anticipos, y *«los anticipos
  ninguno corresponde a la facturación»*.
- Se identifican **por tipo de documento** y por la marca **ingreso/egreso (I/E)**, que es
  manual y por tanto propensa a error: *«aquí también podría decir ingreso, la I, y estar
  con anticipo y el saldo negativo.»*
- **Anticipo partido**: si un anticipo se divide para calzar parcialmente con una factura,
  queda registrado como **traspaso** porque no hubo movimiento directo de banco.

#### 9.4 Conciliación bancaria

- Hoy se **sube un Excel** con los movimientos de la cartola. Mejora que piden:
  *«subir el PDF que nos manda el banco»* (raw `06:43:01` ≈ `40:18`). Carlos pide que les
  envíen el Excel y el PDF tal como llegan del banco; MJ: *«Se lo tenemos que solicitar al
  Agustín.»*
- **La conciliación es manual** porque los identificadores no calzan: *«la cartola dice
  transferencia 20 y nosotros no respetamos el número de comprobante 20, ponemos el 1.
  Entonces no se te calzan los datos.»*
- Pantalla a dos columnas: izquierda los movimientos cargados de la cartola, derecha los de
  contabilidad. Hay que **marcar todos** y que los totales coincidan para poder grabar.
- **Sin navegación a la diferencia**: hay que buscar manualmente. Volumen real:
  *«tenemos 300 registros mensuales y tenemos que ir por fecha, por monto, e ir calzando de
  a poco.»*
- **Búsqueda de cartolas cargadas**: aparecen todas las históricas mezcladas
  (2024 junto a 2026); hay que buscar «muy minucioso».
- **Reversa de conciliación**: por empresa + mes, con opciones «todas / solo automáticas /
  solo manuales». **No existe desconciliar un movimiento suelto**: *«nos damos cuenta en la
  revisión que un pago no se fue a Santa Pilar y se fue a Los Palos… y queremos solamente
  modificar ese movimiento, tenemos que reversar todo el mes, modificar el movimiento,
  volver a conciliar y volver a revisar.»*
- **Dato importante para el diseño**: que un movimiento ya conciliado no se pueda editar en
  contabilidad **no es una queja**. Pregunta de Carlos y respuesta literal de MJ
  (raw `07:50:41` ≈ `47:04`): *«No es una limitación, eso está bien, eso está bien.»* Lo que
  falta es poder desconciliar granularmente.

#### 9.5 El rediseño que pide el cliente: contabilizar desde la cartola

Reu2 raw `07:23:01` ≈ `44:18` (MJ), es la propuesta más elaborada de toda la reunión:
*«lo ideal quizás acá sería que uno pudiera subir la cartola diaria o semanal y con la
misma cartola ir contabilizando. Claro, quizás pescar el movimiento y contabilizar… y ahí
aparezcan solamente los movimientos que no están contabilizados, porque ya estando en la
cartola son sí o sí los oficiales. Sería como más eficiente de esa forma y menos errores,
porque al final si está en la cartola, yo sí o sí tengo que contabilizar lo que está en la
cartola. Entonces, el momento de yo contabilizarlo sería ese movimiento conciliado al tiro.
Y si yo voy a ver los movimientos pendientes, me van a aparecer al tiro los que me faltan
por contabilizar. En cambio, acá lo hacemos al revés.»*

#### 9.6 Lo que tesorería debe entregar

Reu2 raw `09:11:10` ≈ `55:07` (MJ): *«el de tesorería la vamos a tener que dar otra vuelta
porque es uno de los módulos que nos importa que quede muy bien, porque la idea de acá es
también sería que pudiéramos ver las nóminas de pago, lo que está próximo a vender [sic —
casi seguro «vencer»], lo que tiene, no sé, un atraso de más de 90 días… en eso nos ayude
más llevar un control de lo que nos deben pagar y lo que nosotros tenemos pendiente.»*

### 10. Gestión — **no lo usan**

Reu1 raw `17:46:00`: *«el sistema de gestión tampoco lo usamos actualmente y por eso nació
la creación del departamento de Mario. De control de gestión y que él trabajara con los
Power BI directos de la base de Agrosoft… en sí la gestión que nos daba el sistema era muy
básica.»*

Lo que sí quieren en el ERP nuevo es **poco y rápido**: *«serían como gráficos rapiditos
de… desviación en el centro de costo, o ver la cantidad de costos versus las especies, pero
como algo más rápido en realidad»*, y *«si hay alguna desviación con el presupuesto»*. El
análisis de fondo sigue en el Power BI de Mario sobre AlmaWeb.

### 11. Parámetros generales e indicadores

- Se crean **empresas** (las que aparecen en el selector de login), **especie**,
  **variedad**, **fondos** (= los campos; *«no tiene mayor relevancia… lo ponen por sector»*),
  **tipo de terreno** (*«sí importa porque para el área agrícola»*), **centros de costo**
  (crear / modificar / cambiar vigencia) y **ubicación geográfica** (*«no impacta mucho»*
  pero se pide al crear proveedores).
- **Indicadores financieros** (Reu1 raw `17:46:00`–`19:05:21`):
  - Se toman automáticamente de la **página del Banco Central**, no del SII: *«se hace del
    Banco Central y no se hace la página del Servicio de Impuestos Internos, porque el
    servicio lo actualiza más tarde.»* Disponibles **a las 9 de la mañana**.
  - Es una mejora reciente. Antes era digitación manual diaria y el efecto era grave:
    *«se me olvidaba un día y la gente contabilizaba y no se daba cuenta que no tiene el
    tipo de cambio y se contabiliza igual… en pesos siempre me va a salir, porque en pesos
    me deja contabilizarlo, pero ya hay un registro que no me aparecen en dólares. Entonces,
    momento de sacar reportería en dólares, una información errónea.»*
  - **Bug de calendario**: *«los días domingo y los feriados no me trae el tipo de cambio.
    Entonces estos días yo lo tengo que digitar manual»*, y al digitarlo *«se me agrega
    solamente el dólar… si quisiera los otros datos, tendría que ponerlos manuales.»* Se
    señala en pantalla que falta el día 19.
  - Indicadores que **no** usan: UF, UTM, IPC *«no son indicadores que usemos directamente
    para ninguna reportería»* (incluso en mano de obra los agrícolas los digitan a mano).

### 12. Perfiles y permisos en Agrosoft (as-is)

- Solo existen dos perfiles de fábrica: **administrador** y **digitador**, y **los cambia
  el proveedor**, no el cliente: *«solamente lo podemos pedir al proveedor y es igual, nos
  ha traído problemas»* (Reu1 raw `01:58:21`).
- **Incidente real**: necesitaban un perfil intermedio; *«cuando pedimos el cambio de
  perfil, ellos cambiaron el perfil, pero también cambiaron todos los perfiles de los
  digitadores… se activaron varias pestañas que no se tenían que activar en otro usuario, y
  ahí nos generó un conflicto porque al final igual tienen información a la cual no
  deberían tener acceso, por ejemplo, a borrar, a modificar.»* En Reu2 se identifica a la
  persona afectada: **Rodrigo** (raw `10:40:11` ≈ `1:04:01`).
- Segmentación deseada: administrativo vs jefatura; la parametrización solo para jefatura.
- **Roles reales que describen (Reu2 raw `12:59:51` ≈ `1:17:59`):** 3 bien definidos más
  «algunos mix».
  - **Digitadora de contratistas**: solo ese módulo, y **solo las empresas que le
    corresponden** — *«ella tiene acceso solamente a las empresas que ve… yo me meto a Santa
    Pilar y le aparece solo esta en el módulo.»*
  - **Analista**: procesos diarios + emisión de informes. *«no tiene acceso a
    parametrización, no tiene acceso al de gestión… porque cierre de mes también lo hago
    yo.»* En insumos: movimiento de bodega e informes, sin parametrización.
  - **Administrador**: todo, incluido parametrización, traspaso contable y cierre de mes.
- **Estructura organizacional declarada** (raw `10:17:21` ≈ `1:01:44`): *«tenemos dos
  rubros. Tenemos el rubro de exportaciones de servicios y tenemos el rubro agrícola… pero
  en el rubro agrícola igual está segmentado.»*

### 13. Alcance declarado del proyecto (Reu1 raw `01:20:41`)

*«actualmente nosotros estamos haciendo un ERP para lo que es la exportadora y la de
servicio, pero nosotros también tenemos un partner que es agrícola. Entonces, en ese
sentido, este módulo igual va a tener que quedar como más específico para lo que es el área
agrícola que para lo que es el área industrial.»*

Y la síntesis del cliente sobre el objetivo del proyecto (Reu1 raw `02:51:40`):
**«si al final lo que nosotros queremos hacer es como un Agrosoft pero una versión 3.0.»**

---

## Requisitos del cliente

Convención: **quién** = cliente (MJ, Rodrigo, Agustín…) o proveedor (Carlos/Sergio).
Solo los de fila «cliente» son requisitos; los de proveedor son propuestas.
Timestamps de Reu1 son **raw** (reloj no calibrado); los de Reu2 son `raw ≈ real`.

| # | Requisito | Quién | Reunión / timestamp | Cita textual | Dato duro o preferencia |
|---|---|---|---|---|---|
| R-01 | Multimoneda **peso, dólar, yuan y euro** | Cliente (MJ) | Reu1 raw `02:51:40` | «lo ideal es para el módulo que estamos creando en que sea peso, dólar, yuan y euro como principales monedas» | **Dato duro** (lista cerrada de 4) |
| R-02 | Aislar el contexto de empresa en todos los selectores (centros de costo, bodegas, distribución) | Cliente (MJ) | Reu1 raw `01:54:10`, `11:17:10` | «si yo estoy en LM, debería ser sí o sí solamente LM» | **Dato duro** (bug reproducido en 3 pantallas) |
| R-03 | Alerta de artículo duplicado en el maestro | Cliente (MJ) | Reu1 raw `04:54:20` | «yo puse exactamente los mismos datos y aún así me dejó crearlo… me va a aparecer en 10 partes diferentes, mi stock» | **Dato duro** |
| R-04 | Un solo maestro de artículos, alojado en Insumos, separando servicios de existencias | Cliente (MJ) | Reu1 raw `04:54:20`, `10:54:01` | «yo como que prefiero que lo que es maestro de artículos quede en el módulo de insumos» | Preferencia bien fundada |
| R-05 | **No implementar solicitud de compra** | Cliente (MJ) | Reu1 raw `05:56:50` | «como siempre hemos trabajado sin solicitud, en realidad como que esto no debería ir» | **Dato duro de alcance** |
| R-06 | Mantener los pasos de **aprobación y recepción** de OC al descentralizar su creación por departamento | Cliente (MJ) | Reu1 raw `07:12:41` | «lo ideal es que después cada departamento se encargue de su creación de orden de compra. Entonces igual necesitamos que los pasos sigan iguales de aprobación y recepción» | **Dato duro** |
| R-07 | Aviso de pendientes de aprobación **como badge en la app, no por correo** | Cliente (MJ) | Reu1 raw `08:13:41` | «quizás no mucho el correo porque igual sería tedioso… pero sí al momento de meterme a la página y que me aparezca como un pendientes» | **Dato duro** (rechaza explícitamente el correo) |
| R-08 | Validar la distribución de costo **al agregar la línea**, indicando la línea descuadrada | Cliente (MJ) | Reu1 raw `05:56:50` | «por último que diga descuadrado, iba a saber al tiro que falta algo… al final no te va a decir en cuál tú tienes la diferencia» | **Dato duro** |
| R-09 | Distribución de centro de costo editable línea a línea (no «todo o nada» por hectárea) | Cliente (MJ) | Reu1 raw `05:56:50` | «si yo quisiera por hectárea y quiero que solo un cuartel no esté dentro de esa hectárea, no me deja editarlo… Es como todo o nada» | **Dato duro** |
| R-10 | Buscar OC sin conocer el estado, y por proveedor en cualquier estado | Cliente (MJ) | Reu1 raw `07:12:41` | «Si yo no tengo idea, tengo que buscarla módulo por módulo… tampoco me sirve buscar por el proveedor» | **Dato duro** |
| R-11 | Que el creador pueda ver el PDF de la OC al crearla | Cliente (MJ) **[atribución dudosa]** | Reu1 raw `07:12:41` | «Lo bueno sería que cuando uno la crea se abra como el PDF para visualizarla» | Preferencia |
| R-12 | TC del gasto editable **solo en recepción**, no en el registro de compra | Cliente (MJ) | Reu1 raw `09:56:51` | «quizás dejarlo como más rígido y no dejar modificar acá, sino tener que modificar directamente en la recepción» | Preferencia fundada |
| R-13 | **No** endurecer afecto/exento entre OC y factura | Cliente (MJ) | Reu1 raw `10:48:11` | «si no quedaría como muy rígido y quizás impediría el ingreso de alguna factura» | **Dato duro** (contra-requisito) |
| R-14 | NC de compra valorizada al precio de **su factura de origen**, no al promedio de bodega | Cliente (MJ) | Reu1 raw `12:17:30` aprox. | «No me deja sacar esa cantidad por el precio de la factura, me la saca de bodega a precio promedio» | **Dato duro** |
| R-15 | **Inactivar** (no borrar) elementos de costo y catálogos obsoletos | Cliente (MJ) | Reu1 raw `15:19:10` | «no nos deja anular el uso… Están los porque sí, los porque no, y los por si acaso» | **Dato duro** |
| R-16 | Asociar centro de costo ↔ elemento de costo ↔ artículo por área/departamento | Cliente (MJ) | Reu1 raw `15:19:10` | «La idea sería que se fueran asociando, porque así cada departamento trabaja con sus centros de costos y sus artículos más rígidos» | **Dato duro** con caso de uso |
| R-17 | **Exportar a Excel siempre** | Cliente (MJ) | Reu1 raw `15:19:10` | «Para nosotros Excel es sagrado» | **Dato duro** |
| R-18 | Carga masiva de comprobantes con validación por línea y mensajes de error accionables | Cliente (MJ) | Reu1 raw `16:44:11` | «me dice todo lo que tiene inconsistencia… tal línea no requiere centro de costo, o tal línea le falta centro de costo» | **Dato duro** (funcionalidad crítica hoy: centralización de remuneraciones) |
| R-19 | Historial de quién cambió los factores de impuesto | Cliente (MJ) **[atribución dudosa]** | Reu1 raw `16:20:11` | «No, sí, sería bueno tener un historial» | Preferencia |
| R-20 | Indicadores desde **Banco Central** con cobertura de **domingos y feriados** y todas las monedas | Cliente (MJ) | Reu1 raw `18:49:40` | «los días domingo y los feriados no me trae el tipo de cambio… se me agrega solamente el dólar que yo estoy ingresando» | **Dato duro** |
| R-21 | Gestión = pocos gráficos rápidos (desviación de centro de costo, costo por especie, vs presupuesto); el BI pesado queda en Power BI | Cliente (MJ) | Reu1 raw `17:46:00` | «serían como gráficos rapiditos… pero como algo más rápido en realidad» | **Dato duro de alcance** |
| R-22 | **No** implementar mano de obra / remuneraciones | Cliente (MJ) | Reu1 raw `00:40` | «actualmente nosotros trabajamos con Book, entonces este módulo para nosotros no es relevante» | **Dato duro de alcance** |
| R-23 | Actividades y labores deben administrarse **desde contratistas** | Cliente (MJ) | Reu1 raw `39:50`, `01:58:21` | «como no vamos a tener ese módulo, la idea es que se administre directamente de contratista» | **Dato duro** |
| R-24 | Listado visible del tarifario de contratistas, con edición sobre el mismo tarifario | Cliente (MJ, Rodrigo) | Reu1 raw `39:50`; Reu2 raw `01:00:00` ≈ `06:00` | «no hay un listado, entonces no me permite revisar si tengo algún error» | **Dato duro** |
| R-25 | Poder fijar el precio **dentro del proceso**, sin tarifario previo obligatorio | Cliente (Rodrigo) | Reu2 raw `01:06:51` ≈ `06:41` | «Se nos hace más fácil como colocarlo dentro del mismo proceso de inmediato en vez de hacer un tarifario antes de poder trabajar» | **Dato duro** |
| R-26 | Registrar **avance/asistencia diaria sin precio** definido | Cliente (Rodrigo) | Reu2 raw `01:45:51` ≈ `10:35` | «no nos sirve para llevar un control diario sobre quién está yendo, cómo llevar asistencia… no podemos porque como no manejamos el precio todavía» | **Dato duro** |
| R-27 | Al elegir labor, mostrar **solo** las actividades asociadas (y no exigir saber la actividad primero) | Cliente (MJ, Rodrigo) | Reu2 raw `01:36:40`–`01:43:21` ≈ `09:40`–`10:20` | «te salen todas, y es innecesario» | **Dato duro** |
| R-28 | **Proforma construida seleccionando labores diarias** ya registradas | Cliente (Rodrigo) | Reu2 raw `03:51:00` ≈ `23:06` | «poder ver todas las labores que tengo anotadas y decir ya, esta, esta, esta, hago una proforma» | **Dato duro** |
| R-29 | **N proformas → 1 factura**, y proformas que crucen el corte de mes | Cliente (Rodrigo, MJ) | Reu2 raw `02:26:01`–`02:45:50` ≈ `14:36`–`16:35` | «necesitamos hacer dos proformas distintas para esa factura. Pero si hacemos las dos proformas, no nos deja asociarlas» | **Dato duro** (hoy obliga a un registro paralelo fuera del sistema) |
| R-30 | Confirmación previa antes de emitir la proforma definitiva | Cliente (Rodrigo) + Carlos | Reu2 raw `01:56:40`–`02:04:21` ≈ `11:40`–`12:26` | «no hay ningún filtro antes, como de si está seguro, como para validarlo, para poder revisar» | **Dato duro** (dolor del cliente; la formulación de la solución es de Carlos) |
| R-31 | Libro de ventas: eliminar «guardar» temporal; dejar solo grabar y contabilizar | Cliente (MJ) | Reu2 raw `05:46:20` ≈ `34:38` | «Aquí sería solamente grabar, grabar y contabilizar» | **Dato duro** |
| R-32 | Reversa de venta que **reutilice los datos** del documento reversado (472 / 473 / 474) | Cliente (MJ) | Reu2 raw `05:39:21` ≈ `33:56` | «el 472 queda con el original… El 473 debería ser la reversa… y el 474 el nuevo registro» | **Dato duro** |
| R-33 | Módulo de ventas integrado con el resto (hoy queda aislado) | Cliente (MJ) | Reu2 raw `06:30:51` ≈ `39:05` | «estos módulos están súper conectados, pero el módulo de venta queda aparte» | **Dato duro** |
| R-34 | **Diferencia de cambio simétrica**: calcularla también cuando se calza en pesos una deuda en dólares | Cliente (MJ) | Reu2 raw `09:06:11` ≈ `54:37` | «no nos explicamos por qué sí lo hacen cuando pagamos en dólar en pesos, pero no lo hace cuando lo hacemos en pesos en dólar, si se supone que tiene doble moneda» | **Dato duro** |
| R-35 | **Contabilizar desde la cartola**; cartola diaria o semanal; el movimiento contabilizado queda conciliado en el acto | Cliente (MJ) | Reu2 raw `07:23:01` ≈ `44:18` | «subir la cartola diaria o semanal y con la misma cartola ir contabilizando… ese movimiento conciliado al tiro» | **Dato duro** — es el rediseño más explícito de la reunión |
| R-36 | Cargar la cartola desde el **PDF del banco** (hoy solo Excel armado a mano) | Cliente (MJ) | Reu2 raw `06:43:01` ≈ `40:18` | «era quizás una mejora que queríamos hacer, de subir el PDF que nos manda el banco» | **Dato duro** |
| R-37 | **Desconciliar un movimiento** sin reversar el mes completo | Cliente (MJ) | Reu2 raw `07:50:41` ≈ `47:04` | «tenemos que reversar todo el mes, modificar el movimiento, volver a conciliar y volver a revisar» | **Dato duro** |
| R-38 | Mantener el bloqueo de edición de movimientos ya conciliados | Cliente (MJ) | Reu2 raw `07:50:41` ≈ `47:04` | «No es una limitación, eso está bien, eso está bien» | **Dato duro** (confirmación de regla) |
| R-39 | **Nóminas de pago** y **aging con corte de 90 días** | Cliente (MJ) | Reu2 raw `09:11:10` ≈ `55:07` | «pudiéramos ver las nóminas de pago, lo que está próximo a vender [vencer], lo que tiene un atraso de más de 90 días» | **Dato duro** (el «90 días» es explícito) |
| R-40 | Soporte de **anticipos** a productores, incluida la división de un anticipo entre varias facturas | Cliente (MJ) | Reu2 raw `08:06:50`–`08:20:10` ≈ `48:41`–`50:01` | «nosotros acá igual trabajamos con mucho anticipo» | **Dato duro** |
| R-41 | Link directo desde la diferencia de conciliación al registro a corregir | Carlos (proveedor) → aceptado por MJ | Reu2 raw `07:04:41` ≈ `42:28` | Carlos: «Sería bueno que te dé el link directo»; MJ: «Exacto, sí, eso sería una mejora también» | Propuesta del proveedor **validada** por el cliente |
| R-42 | Roles configurables por el cliente, con checks de lectura/escritura por pantalla | Cliente (MJ) sobre propuesta de Carlos | Reu2 raw `09:57:20` ≈ `59:44` | «pinchar lo que quiere el usuario y no como que es tan rígido como usuario digitador, usuario administrador» | **Dato duro** |
| R-43 | En el editor de rol, **mostrar también las pantallas sin acceso** | Cliente (MJ) | Reu2 raw `10:17:21` ≈ `1:01:44` | «si yo pongo modo digitador, igual me aparecieran las pestañas a las cuales no tiene acceso en caso que le tenga que dar quizás un acceso en específico» | **Dato duro** |
| R-44 | Alcance de acceso **por empresa y por usuario** | Cliente (MJ) | Reu2 raw `12:56:00` ≈ `1:17:36` | «ella tiene acceso solamente a las empresas que ve» | **Dato duro** |
| R-45 | Integración GoSocket ⇒ **libro de compras en línea** para contabilizar directo | Cliente (MJ) | Reu2 raw `12:21:50` ≈ `1:14:11` | «la idea de que GoSocket esté conectado con el ERP de AlmaWeb es que nos aparezca el libro de compras en línea y podamos contabilizar directo» | **Dato duro** — es *el* objetivo declarado de la integración |
| R-46 | Implementar cambio de temporada aunque hoy no lo usen | Cliente (MJ) | Reu1 raw `00:40` | «igual sería bueno implementarlo en el ERP nuevo» | Preferencia / futuro |
| R-47 | Módulo de maquinaria (mantenciones, desgaste, prorrateo por cuartel/labor) | Cliente (MJ) | Reu1 raw `13:32:20` | «actualmente el maquinario no lo usamos en ninguno de los rubros… este módulo sería como ya la necesidad de lo que queremos ver» | Preferencia / futuro |
| R-48 | Ingredientes activos y unidades de medida en Insumos para el área agrícola | Cliente (MJ) | Reu1 raw `10:54:01` | «Sería bueno que tuviera los ingredientes activos y la unidad de medida, porque ellos lo podrían usar para el tema de las aplicaciones» | Preferencia / futuro |
| R-49 | Validar y revisar el ERP con los **encargados de cada área**, no solo con contabilidad | Cliente (MJ) | Reu1 raw `12:17:30` | «como llamar a los encargados de cada área para ver si se puede hacer alguna mejora o están conformes con lo que se está haciendo» | **Dato duro de proceso** |

---

## Reglas de negocio concretas

### Documentos, folios y numeración (todos observados en pantalla)

| Objeto | Valor real observado | Reunión |
|---|---|---|
| Orden de compra de servicio | **5207** (neto 1.000, IVA 190) | Reu1 |
| Comprobante de traspaso por recepción de OC | **8310**, glosa «orden de compra de servicios, la 5207 del 7 del 26» | Reu1 |
| Contrato de contratista (folio) | **179**, periodo 16→30 de junio, faena «faena agrícola» | Reu2 |
| Proforma de contratista definitiva | **155**; en borrador el folio de factura = **0** | Reu2 |
| Contratista | nº **6**, «Gómez y Gómez» | Reu2 |
| Comprobante de venta | **472** (original) → **473** (reversa) → **474** (nuevo) | Reu2 |
| Factura del proveedor en AgroSmart | **120**, Sociedad Agrícola Guarachi | Reu2 |
| Bodegas | existen hasta la **23**; se crea la **24**; bodega operativa «**Chamonate**» | Reu1 |

### Estados y catálogos cerrados

- **Estados de OC (7):** anulada · aprobada · cerrada · contabilizada · pendiente ·
  recepcionada parcial · recepcionada total.
- **Tipos de comprobante (6):** apertura · egreso · ingreso · proveedores · traspaso · venta.
- **Tipos de compra en registro de compra:** existencia · activos fijos · servicios ·
  contratista.
- **Modos de distribución de costo en OC (3):** directo (en uso) · por grupo de centro de
  costo · por hectárea (descartado por el cliente).
- **Plazos de pago:** contado · 15 días · 30 días (tanto en compras como en ventas).
- **Reversa de conciliación:** todas / solo automáticas / solo manuales.
- **Unidad de pago a contratistas:** por **jornada** o **a trato** (kilos cosechados, bins,
  capachos). Jornada estándar de **8 horas** (en AgroSmart).

### Cuentas y asientos nombrados

| Evento | Asiento |
|---|---|
| Recepción de OC de servicio | *Mantención y reparación de activos* (gasto) **contra** *Facturas por recibir servicios* |
| Recepción/OC de contratista | costo del trabajo **contra** *Facturas por recibir contratistas* |
| Cierre de mes de contratistas (desde proforma) | *Facturas de contratistas por recibir* (con RUT y referencia a proforma) **contra** *Costo por mano de obra contratista* |
| Entrada a bodega de «materiales de embalaje / separadores» | **Existencia** |
| Consumo/baja de esa subfamilia | **Costo materiales de embalaje** |
| Calce en dólares con diferencia | línea de **«ajuste automático»** por diferencia de cambio |

### Impuestos y factores

- **IVA 19 %**; **IVA retenido 19 %** (dicho literalmente como «0,19 %»).
- **Retención de honorarios**: parametrizada con *factor actual* + *factor anterior* +
  *fecha desde* la que aplica el nuevo factor. Los valores citados están mal transcritos
  («del 15 a 25» y «del 14 a 5»); **probablemente 15,25 % y 14,5 %, no verificable**.

### Monedas e indicadores

- Hoy: **peso y dólar**. Objetivo declarado: **peso, dólar, yuan y euro**.
- Fuente de indicadores: **Banco Central**, disponibles **a las 09:00**. Se descarta el SII
  por publicar más tarde.
- No usan UF, UTM ni IPC para reportería.
- Tipos de cambio observados en el registro de compra: **9,10** y **9,33**
  **[casi seguro 910 y 933 CLP/USD]**.

### Montos y volúmenes reales

- **15 usuarios** contratados en Agrosoft, con cobro por usuario adicional.
- **~300 movimientos de banco al mes** que se concilian a mano.
- Proforma demostrada: 1 jornada a **$37.500** (neto + IVA + total).
- Tarifa «amarras laterales»: **36.500**.
- AgroSmart: 20 jornadas × 8 h = **160 h**; factura de **2.550.000** de la que se asocian
  **825.000**; labor de aplicación de herbicidas / control de maleza a **150.000** por jornada.
- Anticipo de productor calzado: **2.718.836 CLP** / **−342,80 USD**.
- Pago de factura desde cartola: **46.000 CLP**; saldo remanente forzado: **30 CLP**.
- OC parcial: compradas **800**, ingresadas **398**.
- NC de compra: compró **1.000**, llegaron **900**, NC por **100**; bolsas en bodega a
  **100**, compra de 1.000 a **110** → promedio **105**.
- Departamentos que emiten OC hoy: **2**.
- Niveles de almacenamiento definidos por el sistema: **3** (no usados).
- Aging: corte de **90 días**.

### Sociedades, sistemas y personas nombradas

- **Sociedades / entidades**: AlmaWeb · ALM (transcrito también «Alem», «LM», «EME») ·
  Almahue (transcrito «Almaue») · Santa Pilar · Los Palos · Chamonate (aparece como bodega
  **y** como nombre de cliente) · Sandoval y Fuentes (proveedor/productor) · Sociedad
  Agrícola Guarachi (en AgroSmart) · Gómez y Gómez (contratista).
  **[Las siglas no están deletreadas en la transcripción; su mapeo a Almahue Export /
  Almahue Services / AlmaWeb no se puede confirmar desde estas dos fuentes.]**
- **Sistemas**: Agrosoft (actual) · AgroSmart (evaluado, con acceso vigente, confidencial) ·
  Power BI (control de gestión de Mario) · «Book» **[probablemente BUK]** para
  remuneraciones · **Acepta** (facturación electrónica actual) → **GoSocket** (destino).
- **Personas**: Agustín / «Juan Agustín» (aprueba OC, tiene las cartolas) · María José /
  «María Jesús» / «Mari» · Rodrigo (encargado contable de la agrícola) · Mario (control de
  gestión, vuelve en agosto) · Carlos Vallejos y Sergio (proveedor) · Cristian (comercial
  de GoSocket).

### Migración DTE (Reu2, raw `11:52:00`–`12:30:40` ≈ `1:11:12`–`1:15:04`)

- Migran de **Acepta a GoSocket**. Ya hubo reunión con **Cristian**, comercial de GoSocket;
  falta firmar la propuesta y agendar con soporte el traspaso.
- **Fecha objetivo: 1 de septiembre.** *«pedimos que la implementación de [GoSocket]
  estuviera el 1 de septiembre. Entonces nuestra idea es tener todo listo, todo avanzado,
  terminar de facturar agosto con Acepta y en septiembre hacer el cambio definitivo.»*
- **Riesgo declarado por el cliente**: *«no tenemos el mes de prueba porque una vez que
  nosotros demos de baja un sistema, al tiro se borra la base de datos de ese sistema.»*
- **Desacople explícito**: *«AlmaWeb y GoSocket son independientes… lo que nos importa es
  que GoSocket nos deje listo para facturar. Pero ya si en 3 meses más está listo AlmaWeb
  para conectarlo con GoSocket, nosotros hacemos la pega de nuevo y punto.»*
- **Objetivo de la integración**: libro de compras en línea + contabilización directa (R-45).
- **Requisito hacia GoSocket**: *«que GoSocket nos cumpla y efectivamente nos traiga todos
  los documentos de aceptar [Acepta].»*
- **Plazo global del ERP**: *«le habíamos comentado a Sergio que quizás esta implementación
  iba a ser a 6 meses, pero igual creo que va a ser en menos plazo.»*

---

## Decisiones cerradas vs temas abiertos

### Cerradas en estas dos reuniones

| Decisión | Quién la cierra | Referencia |
|---|---|---|
| **No** se implementa mano de obra / remuneraciones (siguen con «Book»/BUK) | Cliente | Reu1 raw `00:40` |
| Actividades y labores pasan a administrarse **desde contratistas** | Cliente | Reu1 raw `39:50` |
| **No** se implementa solicitud de compra | Cliente | Reu1 raw `05:56:50` |
| **No** se implementan niveles de almacenamiento | Cliente + Carlos | Reu2 raw `12:44:20` ≈ `1:16:26` |
| Distribución por hectárea queda descartada; se usa el modo directo | Cliente | Reu1 raw `05:56:50` |
| Módulo de gestión reducido a gráficos rápidos; el BI queda en Power BI | Cliente | Reu1 raw `17:46:00` |
| Afecto/exento entre OC y factura **no** se endurece | Cliente | Reu1 raw `10:48:11` |
| El bloqueo de edición post-conciliación se mantiene | Cliente | Reu2 raw `07:50:41` ≈ `47:04` |
| De AgroSmart se toma **solo** el flujo de mano de obra/asignación; el resto se basa en Agrosoft | Carlos, sin objeción del cliente | Reu2 raw `04:17:21` ≈ `25:44` |
| GoSocket va **independiente** del ERP, con fecha propia 1-sep | Cliente | Reu2 raw `12:21:50` ≈ `1:14:11` |
| Metodología: primero maqueta/pantallas en Trello, después lógica, después marcha blanca en paralelo | Carlos, aceptado por MJ | Reu2 raw `11:15:51`–`11:47:41` ≈ `1:07:35`–`1:10:47` |
| Los roles iniciales los deja configurados el proveedor (digitador, analista, administrador) y el cliente puede crear más | Carlos + MJ | Reu2 raw `13:14:41` ≈ `1:19:28` |

### Abiertas al cierre de Reu2

- **Cuándo se hace la reunión con soporte de GoSocket.** Carlos propone retrasarla hasta
  tener «lo básico del ERP»; MJ no se compromete y depende de la firma de la propuesta.
  Carlos: *«Voy a hablarlo bien con Sergio.»*
- **Cartolas del banco**: pendiente que Agustín entregue el Excel y el PDF.
- **Centros de costo y elementos de costo**: MJ va a mandar la lista, pero la van a cambiar
  con Mario. *«queríamos cambiar algunos centros de costo y elementos de costo»* → la lista
  actual es provisional.
- **Tesorería**: MJ pide explícitamente otra sesión. *«el de tesorería la vamos a tener que
  dar otra vuelta.»* (se materializa mucho después, en la sesión de tesorería de 28/08).
- **Modelo de tarifario de contratistas**: hay tres propuestas en tensión sin resolver —
  tarifario previo (Agrosoft), precio en línea dentro del proceso (Rodrigo, R-25) y proforma
  armada desde labores diarias (Rodrigo, R-28).
- **Notas de crédito con diferencia de precio promedio**: MJ se compromete en Reu1 a traer
  un caso real; en Reu2 no se muestra. Queda pendiente.
- **Perfil de digitador**: se ve solo parcialmente. Carlos: *«no es tan urgente, más que
  nada porque como vamos a tener el tema de permisología con los roles, va a ser
  configurable por ustedes.»*
- **Contacto del encargado por centro de costo**: propuesto por Carlos, sin respuesta del
  cliente.
- **Alcance del área agrícola**: se declara que el partner agrícola queda fuera del ERP
  (exportadora + servicios), pero **todo el módulo de contratistas que se levanta es
  agrícola** (faenas, cuarteles, labores de campo). Esta tensión no se resuelve.

---

## Contraste con la minuta IA

Se contrasta contra `fuentes/reunion2-minuta-tldv-2026-07-23.md`.
**Reu1 no tiene minuta**: todo el recorrido pantalla por pantalla de Agrosoft descrito
arriba —los 11 módulos, los bugs demostrados en vivo, los estados, las cuentas contables,
los 4 requisitos de alcance («no mano de obra», «no solicitud de compra», «no niveles»,
«gestión mínima»)— **nunca tuvo representación en la capa de minutas**.

### 1. La minuta de Reu2 no tiene contenido temático: es un stub roto

La minuta ocupa 1.175 bytes. Tiene 6 action items y luego un encabezado literal
**«## 2–16. Temas (resumen tl;dv)»** cuyo cuerpo completo es una remisión:

> *«Ver análisis canónico en `../reunion2-analisis-2026-07-23.md` (limitaciones AgroSoft
> contratistas, ventajas AgroSmart, ventas, tesorería, roles, cronograma, pendientes
> resueltos).»*

**Ese archivo no existe en el repositorio.** Verificado: las únicas dos referencias a
`reunion2-analisis` en todo `docs/` son la propia minuta y `fuentes/cadena-documental.md`;
no hay ningún fichero con ese nombre. Es decir, **los temas 2 a 16 de Reu2 (los 15 bloques
sustantivos de una reunión de 80 minutos) se colapsaron en una lista de siete sustantivos
que apunta a la nada.** Cualquier afirmación del tipo «Reu2 dice X» apoyada en la minuta es,
literalmente, no verificable.

La minuta además afirma: *«La transcripción completa se conserva en tl;dv y en el historial
de la sesión de análisis»* — cuando la transcripción **está en el propio repo**
(`fuentes/transcripcion-reunion2.md`, 70 KB). La minuta desvía al lector fuera del
repositorio hacia una fuente que ya estaba dentro.

### 2. Errores de atribución en los action items (3 de 6)

| Minuta dice | La transcripción dice | Gravedad |
|---|---|---|
| «**Agustín** enviar archivos Excel y PDF de cartola bancaria (40:48)» | **Agustín no está en la reunión.** Carlos pide los archivos y MJ responde *«Se lo tenemos que solicitar al Agustín»* (raw `06:47:51`). El compromiso es de MJ, no de Agustín; Agustín nunca se comprometió. | Media — convierte una petición de tercero en un compromiso de una persona ausente |
| «**Mario** enviar lista actualizada de centros de costo y elementos de costo (01:07:04)» | MJ dice *«lo voy a ver con Mario porque queríamos cambiar algunos centros de costo y elementos de costo»* y luego *«¿te parece que igual te mando lo actualizado por último?»* (raw `11:10:31`, `11:14:30`). **La que envía es MJ**; Mario ni siquiera está y en Reu1 se dijo que «vuelve en agosto». Además la minuta pierde el matiz crítico: **la lista va a cambiar**. | Media |
| «**Sergio** coordinar con GoSocket para reagendar reunión (01:15:04)» | **Sergio no está en la reunión.** Carlos dice *«Voy a hablarlo bien con Sergio de todas formas para que lleguemos a un acuerdo en conjunto»* (raw `12:30:40`). La acción es de **Carlos**, y su contenido es *consultar a Sergio*, no *coordinar con GoSocket*. | Media |

Los otros tres action items (actualizar capturas del Trello, configurar roles, enviar link
el lunes) sí están respaldados.

### 3. Lo que la transcripción tiene y la minuta perdió por completo

Ninguno de estos aparece ni en los action items ni en la línea de temas:

1. **El objetivo real de la integración GoSocket**: *«que nos aparezca el libro de compras
   en línea y podamos contabilizar directo»* (raw `12:21:50` ≈ `1:14:11`). La minuta
   menciona GoSocket solo como «reagendar reunión». Se perdió el **requisito funcional**.
2. **La fecha 1 de septiembre** y el riesgo de que **no hay mes de prueba** porque al dar de
   baja Acepta se borra su base de datos (raw `12:07:31` ≈ `1:12:45`).
3. **El bug de diferencia de cambio asimétrica** — demostrado dos veces en vivo, con montos
   (raw `08:37:01`–`09:06:11`). Es probablemente el hallazgo técnico más importante de la
   reunión y no deja rastro.
4. **La limitación «una proforma por mes» y el registro paralelo fuera del sistema**
   (raw `02:26:01`–`02:45:50`), con el diagnóstico de MJ de que **falsea el costo
   mensualizado**.
5. **El rediseño «contabilizar desde la cartola»** (raw `07:23:01` ≈ `44:18`), el párrafo
   más elaborado que dice el cliente en toda la reunión.
6. **Nóminas de pago y aging de 90 días** (raw `09:11:10` ≈ `55:07`).
7. **La imposibilidad de desconciliar un movimiento suelto** y, en el mismo pasaje, la
   confirmación de que el bloqueo de edición post-conciliación **está bien** (raw `07:50:41`).
8. **El modelo de reversa 472/473/474** del libro de ventas y el veredicto de que el botón
   «guardar» sobra (raw `05:39:21`, `05:46:20`).
9. **El scoping de acceso por empresa por usuario** (raw `12:56:00`) — distinto de los roles.
10. **El requisito de ver en el editor de rol también las pantallas sin acceso**
    (raw `10:17:21`).
11. **AgroSmart es confidencial y el acceso sigue vigente** («aún no nos han eliminado»),
    y **por qué fracasó**: duplicaba registros y descuadraba centralizaciones
    (raw `03:55:51`). La línea de la minuta dice «ventajas AgroSmart» y omite que el intento
    de migración **ya falló**.
12. **La métrica de esfuerzo**: una proforma de contratista tomaba más de un día completo de
    trabajo (raw `04:08:00`).
13. **Los requisitos de Rodrigo sobre el tarifario** (precio dentro del proceso, control
    diario sin precio, proforma desde labores). Rodrigo **no aparece en la minuta**, ni
    siquiera como participante, pese a que habla en aproximadamente la mitad de la reunión.

### 4. Lo que la minuta insinúa y la transcripción no respalda

- **«pendientes resueltos»**: en la transcripción, del listado de pendientes que repasa
  Carlos (raw `12:30:40` ≈ `1:15:04`) el ejemplo afecto/exento **no se vio en Reu2** —
  Carlos pregunta *«creo que ese ejemplo no lo pudimos ver teniendo los dos, ¿verdad?»* y MJ
  contesta que sí lo vieron, pero eso ocurrió en **Reu1**. Y el **perfil de digitador quedó
  a medias**, con Carlos diciendo *«no es tan urgente»*. Calificar los pendientes como
  «resueltos» es más optimista de lo que la transcripción sostiene.
- **«cronograma»**: la minuta lo lista como tema. Lo único que hay en la transcripción es
  la reunión del martes siguiente y la mención de MJ de que la implementación *«iba a ser a
  6 meses, pero igual creo que va a ser en menos plazo»*. No hay cronograma.

### 5. Las marcas de tiempo no son intercambiables

Los timestamps de la minuta son de tl;dv (tiempo real); los del transcript corren a **1/10**.
Un lector que cite «raw 12:30:40» pensando que es el minuto 12 de la reunión se equivoca por
un factor de 10 (es el minuto 75). Cualquier trazabilidad cruzada entre minuta, transcript y
capturas debe hacer la conversión ×10.

---

## Señales para QA

### Casos hoy marcados SKIP que estas transcripciones **justifican dejar en SKIP**

| Área | Justificación desde la transcripción |
|---|---|
| Solicitud de compra / requisición | *«nosotros no lo usamos… en realidad como que esto no debería ir»* (Reu1 raw `05:56:50`). No es alcance. |
| Niveles de almacenamiento en bodega | Confirmado dos veces: ni lo usan ni lo tienen parametrizado (Reu1 raw `11:17:10`; Reu2 raw `12:44:20`). |
| Mano de obra / remuneraciones / liquidaciones | Fuera de alcance; usan un sistema externo (Reu1 raw `00:40`). Solo debe migrar la **carga masiva de la centralización** como comprobante contable. |
| Módulo de maquinaria | No lo usan en ningún rubro; es deseo a futuro (Reu1 raw `13:32:20`). |
| Dashboards / BI extensos | El cliente pidió explícitamente **gráficos rápidos**; el análisis vive en Power BI (Reu1 raw `17:46:00`). |
| Ingrediente activo / unidad de medida agrícola | No usados hoy; mejora futura para el partner agrícola (Reu1 raw `10:54:01`). |
| Cambio de temporada | No lo usan; «sería bueno implementarlo» (Reu1 raw `00:40`). Prioridad baja, no bloqueante. |

### Casos que **NO deberían quedar SKIP/BLOCKED** — hay requisito explícito de cliente

| Caso | Señal |
|---|---|
| **Aislamiento por `empresaId` en todos los selectores** (centros de costo, bodegas, distribución de costo, elementos de costo) | Es el bug de Agrosoft que más veces reproducen (3 pantallas distintas). No es un caso teórico de seguridad: es un dolor operativo declarado. Debe ejercerse siempre. |
| **Exportación a Excel de cada informe** | «Para nosotros Excel es sagrado». Si hay casos de export en SKIP, deben ejercerse. |
| **Multimoneda CLP/USD/EUR/CNY** y **diferencia de cambio simétrica** | R-01 y R-34. En particular: calzar en **pesos** una deuda en **dólares** debe generar el ajuste, no solo el caso inverso. Es el bug exacto que el cliente demostró. |
| **Tipo de cambio en domingos y feriados** | El BC no publica; Agrosoft dejaba el día vacío y se contabilizaba sin TC. Caso de borde con impacto contable real. |
| **Aging con corte de 90 días y nóminas de pago** | Pedido literal de MJ (R-39). Si hay casos de aging en BLOCKED, el requisito existe. |
| **Anticipos a productores, incluido anticipo dividido entre varias facturas** | R-40; hoy en Agrosoft eso degrada a «traspaso» manual. |
| **N proformas de contratista → 1 factura, cruzando el corte de mes** | R-29. Es la limitación que obliga al cliente a llevar un registro paralelo fuera del sistema. Si el ERP replica «una proforma por mes», es una regresión, no una simplificación. |
| **Inactivar (no borrar) catálogos: elementos de costo, cuentas («no imputable»), centros de costo, contratistas («cambiar vigencia»)** | R-15. Agrosoft tiene el patrón para cuentas y contratistas pero no para elementos de costo, y eso duele. |
| **Alerta de duplicado en el maestro de artículos** | R-03, con consecuencia demostrada sobre el stock y el mayor de insumos. |
| **Validación de cuadratura de la distribución de centro de costo al agregar la línea** | R-08. El caso relevante es distribuir 1.010 contra un neto de 1.000 y esperar el error **en la línea**, no al guardar. |
| **Roles: mostrar pantallas sin acceso en el editor; acceso por empresa por usuario** | R-43 y R-44. |

### Divergencias deliberadas entre el as-is y el ERP nuevo que QA debe cubrir explícitamente

1. **Gate de recepción para registrar la factura.** En Agrosoft la regla es dura:
   *«Si está solamente en estado aprobada, no me aparece»* en el registro de compra
   (Reu1 raw `10:54:01`). El ERP nuevo permite asociar factura a OC no aprobada
   (destacándola con `ocNoAprobada`) y bloquea después. Es una divergencia **intencional y
   defendible** —encaja con el hecho de que el cliente crea la OC *después* de la
   factura— pero necesita casos de prueba que verifiquen que el bloqueo de contabilizar y
   pagar sí se aplica.
2. **La OC se crea después de la factura en la práctica** (Reu1 raw `07:12:41`). Los casos
   de prueba con este orden invertido son **realistas**, no artificiales. Deben existir.
3. **Aprobación de OC sin notificación por correo.** El cliente rechazó el correo y pidió un
   badge (R-07). Si hay casos BLOCKED por «H9 SMTP correo PIN externo», eso **no bloquea**
   el requisito de aprobación: el aviso pedido es in-app. Separar ambas cosas.
4. **Afecto/exento OC vs factura: no endurecer.** Si existe un caso de prueba que espera que
   el sistema rechace una factura afecta contra una OC exenta, **contradice al cliente**
   (R-13). Hay facturas afectas con montos exentos y combustible con impuesto específico.
5. **Cartola desde PDF del banco.** El ERP hoy es import-only con parser web. El caso «subir
   el PDF que manda el banco» (R-36) es un **gap de alcance real**, no un SKIP de entorno.
   Documentarlo como gap, no como caso no aplicable.
6. **Contabilizar desde la cartola** (R-35) está **alineado** con el diseño actual del ERP
   (asiento de banco anclado a `CARTOLA:{id}`). QA debe verificar la otra mitad del
   requisito: que la vista de pendientes muestre **solo los movimientos de cartola aún no
   contabilizados** y que contabilizar deje el movimiento conciliado en el acto.
7. **Desconciliar un movimiento suelto** (R-37) sin reversar el mes. Y su complemento
   (R-38): un movimiento **conciliado** no debe poder editarse. Ambos deben tener caso.
8. **GoSocket: recepción, no solo emisión.** El objetivo declarado del cliente es el **libro
   de compras en línea** (R-45). El estado actual del ERP cubre emisión DTE en tres modos.
   Si hay casos de recepción/libro de compras en BLOCKED, el motivo correcto es **alcance no
   construido**, no «falta GoSocket» ni «falta CAF». Es una distinción que cambia la
   priorización.
9. **Libro de ventas: reversa reutilizable** con la secuencia 472/473/474 y sin botón
   «guardar» temporal (R-31, R-32). Si el ERP no tiene reversa de venta, es gap.
10. **Nota de crédito de compra valorizada al precio de su factura de origen** (R-14), no al
    promedio ponderado de la bodega. Caso de prueba concreto: bodega con promedio 105, NC
    contra una factura de 110 → la salida debe ir a 110.

### Cautelas de interpretación para quien use este documento

- En Reu1 la diarización es poco fiable: varias frases del tipo «sería ideal» pueden ser del
  proveedor y no del cliente. Están marcadas **[atribución dudosa]** en la tabla de
  requisitos. **No cerrar un requisito solo con una de esas.**
- Términos mal transcritos que **no deben citarse literalmente** en documentación derivada:
  «Book» (→BUK), «VoSocket» / «Osoquet» / «Gozo» / «WhatsApp» (→GoSocket), «aceptar»
  (→Acepta), «la UEF» (→UF), «repartidería» (→reportería), «próximo a vender» (→vencer),
  «Almaue» (→Almahue), «María Jesús» (→María José), «16 y bins» y «Dan Plaza» (ilegibles).
- El **«tipo de referencia 31»** citado en Reu1 no corresponde a un código de DTE SII
  estándar (33/34/61/56). Puede ser un código interno de Agrosoft. **No usarlo como
  requisito de catálogo SII sin verificar** contra
  `catalogo-tipos-referencia-agrosoft.md`.
- Reu1 y Reu2 son de **julio 2026**. Cuando algo aquí choque con Reu6 o con las sesiones de
  agosto (20/08 tarde con Lupe y Mario, 28/08 tesorería), **gana lo más reciente**. Este
  documento sirve para saber **de dónde viene** un requisito y **qué duele hoy en Agrosoft**,
  no para reabrir decisiones ya cerradas.
