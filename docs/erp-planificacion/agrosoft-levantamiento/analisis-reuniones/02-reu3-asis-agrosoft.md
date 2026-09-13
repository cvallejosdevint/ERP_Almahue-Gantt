# Reu3 — as-is Agrosoft (desde transcripción)

> Fuente primaria: [`fuentes/transcripcion-reunion3.md`](../fuentes/transcripcion-reunion3.md) (52.611 bytes, leída íntegra).
> Contraste: [`fuentes/reunion3-minuta-tldv-2026-07-28.md`](../fuentes/reunion3-minuta-tldv-2026-07-28.md).
> Video: `fuentes/videos/reunion3-2026-07-28.mp4` · tl;dv: `6a68f05340ebfe00135d54a8`.

## Aviso metodológico previo (léelo antes de citar timestamps)

> Convención unificada del proyecto en [`00-metodologia-y-timestamps.md`](00-metodologia-y-timestamps.md): leer la marca como `h:mm:ss` y **dividir por 10**. Da el mismo tiempo real que el `×6` usado abajo (difieren en menos de 6 s) y está verificada contra un ancla independiente de Reu4.

**Los timestamps de la transcripción NO son tiempo real de reunión.** El formato de la transcripción es
`[(mm:)ss:cc]` sobre una línea de tiempo comprimida ~**6×** respecto de la grabación. La minuta tl;dv sí usa
tiempo real. Verifiqué la conversión `real ≈ transcripción × 6` con más de 15 anclas cruzadas, p. ej.:

| Transcripción | ×6 | Minuta tl;dv (tiempo real) | Ancla |
|---|---|---|---|
| `[01:50:11]` | 11:01 | `11:11` | contraseña sin visualizar |
| `[02:32:01]` | 15:12 | `15:13` | «Tenemos usuarios por empresa» |
| `[02:45:40]` | 16:32 | `16:34` | enviar listado de centros de costo |
| `[05:00:51]` | 30:03 | `30:06` | contabilizar: cuenta, CC, glosa, cliente |
| `[05:40:40]` | 34:02 | `34:04` | cuenta contable y CC en OC |
| `[06:09:40]` | 36:56 | `36:58` | botón carga masiva |
| `[07:47:20]` | 46:43 | `46:44` | devolución = salida proveedor |
| `[08:11:21]` | 49:07 | `49:09` | niveles del plan de cuentas |

En este documento cito **`[T mm:ss:cc ≈ real mm:ss]`**: primero el sello literal del archivo de transcripción,
luego el equivalente en la línea de tiempo real (la que usa la minuta y la que verá quien abra el video).

**Segundo aviso, aún más importante: Reu3 NO es un recorrido de Agrosoft.** Reu3 es una **demo pantalla por
pantalla del ERP nuevo** (el mockup publicado en el servidor de pruebas), y el cliente va comentando. El as-is de
Agrosoft aparece **de forma indirecta**, en frases del tipo «actualmente nosotros…» / «nosotros identificamos…».
El recorrido explícito de Agrosoft fue Reu1–Reu2 (la propia transcripción lo dice: *«nos basamos en las capturas
de pantalla de AgroSmart en la segunda reunión»*). He extraído igualmente **todo** el as-is deducible, marcando
qué es afirmación directa del cliente sobre su sistema actual y qué es inferencia.

---

## Ficha

| Campo | Valor |
|---|---|
| Fecha | 28/07/2026 (la transcripción lo confirma: *«hoy estamos a 28»*, `[T 04:48:11 ≈ 28:49]`) |
| Duración real | ≈ **58 min** (último turno `[T 09:37:01 ≈ 57:42]`) |
| Participantes | **Solo dos voces.** Speaker 00 = **Carlos Vallejos** (proveedor) · Speaker 01 = cliente, area contable |
| Ausentes | No hay intervención de Agustín, Lupe, Mario, Fran ni Sergio en toda la reunión |
| Temas | Método de tablero Trello · acceso al servidor de pruebas · usuarios/roles · catálogo-parametrización · contratistas/proformas · traspaso y cierre · libro comercial (ventas) · clientes · GoSocket · compras/OC/recepciones/registro de facturas · insumos y bodega · contabilidad (plan de cuentas, indicadores BC, asientos) · reportería · agenda |

**Sobre la identidad del Speaker 01 (ambigüedad real, no la resuelvo por mi cuenta):** la cabecera del archivo
dice «Speaker 01 = María Jesús». Carlos la llama **«Mari»** cinco veces, y una vez **«Marino»**
(`[T 07:16:41]`) y una vez **«Mario»** (`[T 09:27:01]`, *«¿Hasta qué horas más o menos tienes, Dispo Mario?»`),
que son casi con certeza errores de ASR sobre «Mari». El contexto del proyecto identifica a la contraparte
contable como **María José (MJ)**. En este documento la trato como **MJ (cliente)**, pero la transcripción por sí
sola no permite cerrar si es «María Jesús» o «María José».

**Convención de este documento:** MJ = **cliente → requisito**. Carlos = **proveedor → propuesta/hipótesis**.

---

## As-is Agrosoft

Ordenado por módulo. Marco cada punto como **[AS-IS directo]** (MJ describe su sistema/proceso actual),
**[AS-IS inferido]** (se deduce, pero no está dicho literalmente) o **[Agrosoft copiado al ERP]** (el ERP nuevo
replica una pantalla de Agrosoft capturada en Reu2).

### 0. La demo del ERP nuevo se construyó copiando Agrosoft

`[T 03:07:50 ≈ 18:45]` MJ: **«eso sería como el modelo que sacamos de AgroSmart»**.
`[T 03:08:21 ≈ 18:50]` Carlos: *«esto nos basamos en lo que sacamos, las capturas de pantalla de AgroSmart en la
segunda reunión, para poder ejecutarlo. Teníamos otra vista, pero realmente, como ya tenían ese sistema y les
parecía cómodo, nos reconstruimos, nos basamos en ese directamente.»*
`[T 04:05:11 ≈ 24:31]` Carlos: *«Como igual nos basamos en la otra, se basó prácticamente uno a uno.»*

→ **Consecuencia práctica:** las pantallas de proformas / asociaciones laborales / tarifas de labores del ERP son
un calco 1:1 de Agrosoft. **[Agrosoft copiado al ERP]**

*Nota léxica:* la transcripción escribe siempre **«AgroSmart»**; es casi seguro un error de ASR por **«Agrosoft»**.

### 1. Usuarios, roles y multiempresa

- **[AS-IS directo]** `[T 01:01:00 ≈ 06:06]` MJ: *«nosotros sabemos que hay **roles administrativos y
  digitadores**, pero en realidad nosotros preferimos que aparezca el nombre de la persona que está haciendo el
  trabajo, porque así después cuando revisamos sabemos quién hizo el movimiento y no como el cargo.»*
  → Hoy existen al menos dos roles: **administrativo** y **digitador**. El dolor: la trazabilidad muestra cargo, no persona.
- **[AS-IS directo]** `[T 02:32:01 ≈ 15:12]` MJ: **«Tenemos usuarios por empresa.»**
  `[T 02:33:21 ≈ 15:20]`: *«la creación de usuario igual vamos a tener que seleccionar a qué empresa pueden entrar»*.
  `[T 02:37:11 ≈ 15:43]`: confirma que hay usuarios con acceso a **una o varias** empresas.
- **[AS-IS directo]** `[T 01:50:11 ≈ 11:01]` MJ: **«actualmente cada uno cambia su clave»**, y pide que además el
  administrador pueda **visualizar** la clave de otro usuario. Carlos lo **rechaza** (`[T 01:51:50 ≈ 11:11]`:
  *«ver la contraseña como tal no damos la opción, pero sugerimos siempre que exista la opción de cambiarla sin
  ver»*, con contraseña temporal). MJ: *«Ya, entiendo.»* → **Requisito del cliente denegado por el proveedor.**
- **[AS-IS inferido]** `[T 01:20:01 ≈ 07:20]` MJ: *«si yo hago un registro, aparece mi usuario, no sale mi rol»* —
  describe cómo espera/ve la trazabilidad.
- **[AS-IS inferido]** `[T 01:16:51 ≈ 07:39]` Carlos: *«hay traspaso de rol»* (recogiendo lo que MJ describe) →
  en Agrosoft la gente cambia de rol y hay que administrarlo.

### 2. Catálogo = «parametrización» (el nombre que usa el cliente)

- **[AS-IS directo]** `[T 02:48:20 ≈ 17:00]` MJ: *«en catálogo, y te puse que fuera **parametrización**, cosa de
  que sepamos que ahí se hace todo lo que es la parametrización del sistema.»*
- **[AS-IS directo]** `[T 02:50:30 ≈ 17:03]` MJ enumera qué contiene la parametrización de Agrosoft:
  **«el centro de costo, el plan de cuentas, los elementos de costo, los tipos de documentos, los tipos de
  referencia. Los códigos financieros.»**
  Reiterado en `[T 08:48:51 ≈ 52:53]`: *«el plan de cuentas, elementos de costos, centros de costos, los códigos
  financieros»*, y en `[T 08:44:21 ≈ 52:26]` añade **«los factores»** (por «factores de honorarios», mencionado
  por Carlos en `[T 08:19:31 ≈ 49:56]`).
- **[AS-IS directo]** `[T 02:56:31 ≈ 17:39]` MJ, sobre segregación de acceso: *«yo lo que está en catálogo yo lo
  dejaría todo lo que es creación y modificación ahí, cosa de que los usuarios cuando tengan acceso al catálogo
  sepan, sean los únicos que puedan modificar, agregar, eliminar, y el resto, independiente le activemos un
  módulo, no le aparezca el módulo de parametrización.»*
- **[AS-IS inferido]** `[T 02:45:40 ≈ 16:32]` MJ ya envió un **listado de centros de costo** en Excel;
  `[T 08:08:21 ≈ 48:50]` confirma haber cargado tres Excel al tablero: **plan de cuentas, centros de costo y
  elementos de costo**.
- **Dolor concreto: Agrosoft no la deja exportar.** `[T 11:40 ≈ 01:10]` MJ: **«yo en un comentario te puse como 7
  pantallazos porque no me dejaba bajar el Excel del sistema»**, hablando de la pantalla de **tipos de documento**
  (Carlos lo confirma en `[T 12:31 ≈ 01:15]`: *«creo que era este de acá, y de hecho el tipo de documento»*).
  *Ambigüedad honesta:* la frase «el sistema» no está desambiguada; por el contexto (ella captura pantallas de su
  sistema para que el proveedor lo replique) lo más probable es que sea **Agrosoft**, pero no es explícito.

### 3. Contratistas: ingresos diarios, proformas, asociaciones laborales, tarifas

Pantallas del ERP calcadas de Agrosoft `[T 02:59:30 – 03:20:21 ≈ 17:57 – 20:01]`:

- **Ingresos diarios** / **Proformas**: al hacer clic muestran información + **estado**: *asociado*, *facturado*
  o *pendiente*.
- **Asociaciones laborales**: columnas **contratista, labor, actividad, monto, estado**; con marcado (check) que
  habilita acciones.
- **Tarifas de las labores**: desde ahí se ven las proformas; **las acciones disponibles dependen del estado**, y
  **si ya está facturada no hay acción**.
- Flujo de proforma `[T 03:21:51 ≈ 20:11]` (descrito por Carlos replicando Agrosoft):
  - proforma **definitiva** → al hacer clic pide **número de factura, fecha, y si se quieren incluir otras proformas**;
  - proforma **borrador** → pregunta si pasar a **definitiva**; permite **editar** y **borrar**;
  - acción **asociar facturas**.
- **[AS-IS directo]** `[T 03:54:41 ≈ 23:28]` MJ: **«que uno pudiera pinchar varias proformas y poder facturarlas.
  Por ejemplo, que **3 o 4 proformas** pertenezcan a una factura.»**
- **[AS-IS directo]** `[T 03:20:21 ≈ 20:01]` MJ: *«¿aquí va a estar parametrizado con **GoSocket** que nosotros
  podamos seleccionar si nos llegaron facturas de ese proveedor?»* → hoy la recepción de facturas de proveedor
  pasa por GoSocket.
- **Dolor de control** `[T 03:37:00 ≈ 22:12]` MJ: *«Yo aquí en el modo de editar una proforma o un trabajo diario
  pediría aprobación de algún supervisor, algo así. Porque si no va a quedar **muy abierto a que modifiquemos
  demasiado el día a día**.»* → Lectura razonable: en Agrosoft la edición del día a día **no tiene control**.

### 4. Traspaso contable y cierre de mes

Este es el bloque as-is más nítido de toda la reunión.

- `[T 04:25:21 ≈ 26:31]` MJ: *«sería el **traspaso contable y cierre de mes**.»*
- `[T 04:26:30 ≈ 26:39]` MJ: *«aquí yo creo que va a quedar una modificación porque **aquí solamente se
  centraliza la información, no se hace por contratista**.»*
- `[T 04:28:21 ≈ 26:50]` MJ: *«acá solamente nosotros necesitamos, nos aparece **qué mes queremos cerrar, tipo de
  cambio**. Y centralizamos, y ahí internamente el sistema hace todo lo que es **reconocimiento del costo versus
  facturas por recibir contratistas**.»*
- `[T 04:32:41 ≈ 27:16]` Carlos la marca como pantalla crítica: *«está como una de las que tendríamos que tener
  más cuidado»*.

→ **Entradas del cierre: mes + tipo de cambio. Salida: centralización global (no por contratista) que reconoce
costo contra la cuenta de «facturas por recibir contratistas» (provisión).**

### 5. Ventas — «libro comercial» (que para el cliente se llama distinto)

- **[AS-IS directo] Nomenclatura invertida** `[T 06:22:20 ≈ 38:13]` MJ: *«ahí por ejemplo el libro comercial yo le
  pondría el **libro de venta**, porque **para nosotros el libro comercial es el de compra**.»*
  `[T 06:25:10 ≈ 38:31]`: *«Y en el que sea compras, que sea el libro de compras.»* → **decisión de renombrado.**
- **[AS-IS directo]** `[T 05:04:51 ≈ 30:29]` MJ: *«en la venta debería estar solamente el libro de venta, ya sea
  con **nota de crédito o débito, factura**, y eso debería cargarse directamente del **servicio Impuestos
  Internos**»*. La transcripción añade *«de Vozaker»*, palabra **ininteligible/garbleada**; podría ser «de
  GoSocket» pero **no lo doy por cierto**.
- **[AS-IS directo] Contabilizar el libro** `[T 05:00:51 ≈ 30:03]` MJ: *«nos faltaría poder hacer la acción real
  de contabilizar, porque al contabilizar nosotros seleccionamos **cuenta contable, centro de costos, le
  agregamos una glosa, seleccionamos el cliente**. Es solamente como **cargar el libro y contabilizar**.»*
- **[AS-IS directo] Carga masiva Excel SII, hoy ya existe** `[T 06:08:40 ≈ 36:52]` MJ: **«actualmente nosotros
  podemos subir un Excel al sistema y contabilizarlo»**. `[T 06:00:51 ≈ 36:03]`: *«en el libro comercial, que
  sería el libro de ventas, yo puedo cargar, por ejemplo, el archivo Excel del Servicio de Impuestos Internos.»*
- **[AS-IS directo] Deduplicación por solape de periodos** `[T 06:10:51 ≈ 37:03]` MJ: *«si subimos por ejemplo la
  primera semana de agosto lo que llegó **del 1 al 7**, y si subimos el 14, **del 1 al 14**, no haga como la
  distinción de lo que ya está duplicado»* (es decir: **que detecte y no duplique**).
  `[T 06:21:50 ≈ 38:11]` MJ confirma que la carga masiva aplica a **libro de compra y libro de venta**.
- **Reversa** `[T 04:38 ≈ 27:48]` (bloque de Carlos): documento aprobado → **reversar** → vuelve a **borrador**,
  queda el **dato del origen**, y al re-contabilizar aparece la advertencia *«este documento viene de una
  reversa»*. Carlos pregunta si la reversa debe pasar por aprobación de administrador y MJ responde
  `[T 04:43:01 ≈ 28:18]`: *«No sé, que es un poco más abierto porque sé que hay el rol del digitador»* →
  **queda abierto.**
- **[AS-IS directo] Asociar factura de compra a OC** `[T 04:47:01 ≈ 28:42]` MJ: *«si este es el libro de compras,
  lo ideal sería que yo, por ejemplo, en acción pueda **asociarlo a una orden de compra del sistema**.»*

### 6. Clientes y vendedores

- **[AS-IS directo] Quién crea al cliente** `[T 05:15:40 ≈ 31:34]` MJ: *«actualmente las personas que crean el
  cliente **somos el área contable, ni siquiera el vendedor**. Ellos nos solicitan a nosotros poder crear por un
  tema de control.»* `[T 05:17:41 ≈ 31:46]`: *«si dejamos a destajo que ellos creen, **pueden crear, falsificar
  documentos**.»* → control antifraude explícito.
- **[AS-IS directo] No existe maestro de vendedores** `[T 05:24:51 ≈ 32:29]` Carlos: *«falta también que tengamos
  un módulo de registro de los vendedores, eso no lo tenemos»* → `[T 05:26:00 ≈ 32:36]` MJ: **«Claro, o sea que no
  tenemos vendedores.»** → `[T 05:26:40 ≈ 32:40]` Carlos cierra: *«Va a ser **el usuario** entonces que
  prácticamente está aquí en el sistema el que lo cree, y **es el que debería aparecer en el registro**.»*
  **Decisión cerrada: sin entidad Vendedor; se registra el usuario creador.**
- **[AS-IS directo] Campos de creación** `[T 05:23:11 ≈ 32:19]` MJ: *«lo que necesitamos para crear un vendedor es
  el **giro, la razón social, el RUT. Dirección** y eso.»* *(Dice «vendedor» pero el hilo es la creación de
  clientes; la palabra es ambigua en la transcripción — lo marco como tal.)*
- Carlos propone un campo «contacto de la empresa» opcional; MJ lo descarta `[T 05:19:11 ≈ 31:55]`:
  *«debería aparecer como el que crea nomás.»*

### 7. Compras: OC, aprobaciones, recepciones, registro de facturas

- **Estados de OC** `[T ≈ 33:35]` (Carlos, describiendo el mockup): *«aprobado, emitido, **reaccionado**,
  contabilizado y borrador»*. **«Reaccionado» no es una palabra de negocio**: es casi seguro un error de ASR por
  *recepcionado* o *reversado*. **No lo resuelvo.**
- **[AS-IS directo] Campos faltantes en la OC** `[T 05:40:40 ≈ 34:02]` MJ: *«Proveedor, departamento, bueno, ahí
  falta la **cuenta contable** y el **centro de costo**, que al final es la orden de compra la que ha imputado el
  costo. Adicionar el **elemento de costo** también.»*
  → **La OC es el documento que imputa el costo** (cuenta contable + CC + elemento de costo + departamento).
- **[AS-IS directo] Totales de la OC** `[T 05:47:31 ≈ 34:44]` MJ: *«en la orden de compra aparece el **neto** y si
  tiene impuestos, el **impuesto**.»* Carlos admite `[T 05:50:20 ≈ 35:01]`: *«El tema del impuesto no estaba bien
  aplicado.»*
- **Recepciones** `[T 06:37:01 ≈ 39:42]` MJ: *«**Editar el tipo de cambio**, ¿cierto?»* → Carlos
  `[T 06:37:30 ≈ 39:45]`: *«ese se debería reflejar en **todos los módulos** al momento de realizar el cambio»*.
- **[AS-IS directo] Registro de compra ↔ OC por RUT** `[T 06:47:40 ≈ 40:46]` MJ: *«lo ideal sería que nosotros
  pudiéramos **seleccionar la factura y ver qué órdenes de compra están asociadas al RUT del proveedor**.»*
  `[T 06:56:40 ≈ 41:40]`: *«si vamos a hacer la carga del libro de compras y nos va a salir toda la información
  del proveedor, ver si ese proveedor tiene órdenes de compra asociada, y con eso ir seleccionando la orden de
  compra que se vaya contabilizando.»*
  Ejemplo concreto `[T 07:00:50 ≈ 42:05]`: **«si esa factura es la 77, que diga orden de compra 4.»**

### 8. Insumos y bodega

- **[AS-IS directo] El maestro de artículos NO lleva stock ni costo** `[T 07:10:40 ≈ 43:04]` MJ: **«El stock no es
  necesario porque el maestro de artículo es la creación. Ni el costo promedio.»**
  → stock y costo promedio se ven **en bodegas**, no en el maestro (`[T 07:13:51 ≈ 43:23]` Carlos: *«Aquí en las
  bodegas donde se debería poder ver, ¿verdad?»* → MJ: *«Sí»*).
- **[AS-IS directo] Cuenta contable de consumo en el artículo** `[T 07:15:20 ≈ 43:32]` MJ: *«en el maestro de
  artículos también deberíamos poder seleccionar **a qué se va a contabilizar. Cuando se centralice**.»*
  `[T 07:17:01 ≈ 43:42]`, con ejemplo textual: *«Si yo creo un artículo, por ejemplo, no sé, **bolsas**, yo voy a
  pedir que se vaya a la cuenta contable que es **costo materiales de embalaje**. Entonces, una vez que la bodega
  centralice, ahí por indicación se sabe a qué cuenta contable se debe ir cada consumo.»*
- **Bodegas**: registro simple, **código + nombre** `[T 07:21:51 ≈ 44:09]`.
- **[AS-IS directo] Se navega por bodega, no por movimiento** `[T 07:31:10 ≈ 45:07]` MJ: *«de poder seleccionar la
  bodega, porque **a veces uno quiere buscar por bodega y no por movimiento**.»*
  (El equipo de desarrollo había dicho que bastaba el filtro avanzado; **Carlos también discrepa**:
  `[T 07:25 ≈ 44:35]` *«Lo que yo creo que no, porque uno igual debería poder tener una vista rápida de las bodegas»*.)
- **[AS-IS directo] Devolución a proveedor** `[T 07:47:20 ≈ 46:44]` MJ: **«la devolución nosotros la identificamos
  por el tipo movimiento porque es **salida proveedor**.»**
  Antes, `[T 07:37:40 ≈ 45:46]` MJ había preguntado: *«¿qué pasa cuando ya tengamos una devolución de proveedor?
  Y que tenga que salir con un tipo de cambio específico, ¿se va a poder hacer?»* → **devolución con tipo de
  cambio propio.** Carlos responde con la preocupación de **no afectar el precio promedio** `[T 07:40:30 ≈ 46:03]`
  y detecta que **no hay botón de devolución ni control de estados** en el mockup.
- **[AS-IS directo] Existen estados de movimiento propios** `[T 07:55:40 ≈ 47:34]` MJ: *«ahí te voy a mandar el
  **estado de movimiento de la bodega**»* → hay un catálogo de estados en Agrosoft que aún no está en el ERP.

### 9. Contabilidad

- **[AS-IS directo] El plan de cuentas del mockup no se parece al real** `[T 08:03:10 ≈ 48:19]` MJ: *«igual te
  mando el plan de cuenta actual porque **no tiene mucho que ver con lo que está ahí escrito**.»*
- **[AS-IS directo] Niveles y parametrización por cuenta** `[T 08:11:21 ≈ 49:07]` MJ: *«el plan de cuenta igual
  tiene **niveles**, que algunos son de **clasificación** y los otros son de **agrupación**. Entonces igual,
  cuando tú abras el Excel, te va a salir el nivel y te va a salir todo lo que pide cada cuenta contable
  dependiendo de lo que nosotros parametricemos. Entonces la idea es que se mantenga esa opción de poder, **si
  nosotros queremos una cuenta contable, agregarle centro de costo, que vaya. Si la queremos quitar,
  quitársela**.»*
  → **Cada cuenta define qué dimensiones exige.** Esto es la semilla del modelo de dimensiones (CC / elemento / área).
- **Indicadores Banco Central** `[T ≈ 51:04]` (propuesta de Carlos, no as-is): sincronización automática **a las
  9:00 AM**, botón de actualización **manual** por si el servicio externo cae, e **historial** de última
  sincronización. Carlos ofrece fusionar el módulo de indicadores con el de monedas.
- **Asientos — carga masiva** `[T 08:50:11 ≈ 53:01]` (Carlos): subir documento → **analizar** → mostrar lo
  extraído → permitir descartar duplicados → cargar. Detecta que **falta la carga unitaria/edición manual**.
- **Reportería** `[T ≈ 54:14]` Carlos: en standby; *«la idea es que **cada uno de los módulos tenga su
  reportería**»* (recogiendo un pedido previo del cliente).

### 10. Método de trabajo y entorno (contexto, no as-is de Agrosoft)

- Tablero Trello con columnas: *«En Kua al Mawe»* (casi seguro **«En QA AlmaWeb»**, ASR dudoso) → el cliente
  revisa → **rechazado** (con comentario) o **aprobado** `[T 00:00 – 00:17 ≈ 00:00 – 00:02]`.
- Servidor de pruebas por **IP**, no definitiva; usuario semilla **`admin@almawe.cl`** (correo falso temporal)
  `[T 23:01 ≈ 02:18]`.
- El servidor publicado va **con días de desfase** respecto al desarrollo local.
- **Modo demo vs modo real**: el toggle existía ya en Reu3. Carlos `[T 23:01 ≈ 02:20]`: *«en el modo real, si
  aparece información, está funcionando el módulo y se puede probar»*; el modo demo es **solo visual**.
- Estado de avance declarado: *«el de administración está completo, pero el de catálogo y contratista hay algunas
  cositas que sí y otras que no»*.
- La misma IP sirve **otro proyecto, «FreshLink», con AlmaWeb** `[T 08:50:11 ≈ 53:40]`.
- Compromiso: funcional **antes de agosto, ojalá el viernes** `[T 04:48:11 ≈ 28:55]`; próxima reunión **jueves PM**
  (MJ no está disponible el viernes; disponible **hasta las 18:00**) `[T 09:25:30 ≈ 55:35]`.

---

## Requisitos del cliente

Solo entradas donde habla **MJ (cliente)**. «Dato duro» = hecho verificable de su operación o número/nombre
concreto. «Preferencia» = deseo de UX o pedido sin respaldo operativo explícito.

| # | Requisito | Quién | Timestamp (T ≈ real) | Cita textual | Tipo |
|---|---|---|---|---|---|
| R1 | En los registros/movimientos debe verse el **nombre de la persona**, no el cargo | MJ | `01:01:00 ≈ 06:06` | «preferimos que aparezca el nombre de la persona que está haciendo el trabajo… sabemos quién hizo el movimiento y no como el cargo» | Dato duro |
| R2 | **Usuarios por empresa**; al crear el usuario se selecciona a qué empresa(s) accede (una o varias) | MJ | `02:32:01 ≈ 15:12` | «Tenemos usuarios por empresa» / «vamos a tener que seleccionar a qué empresa pueden entrar» | Dato duro |
| R3 | El administrador debería poder **ver** la clave de otro usuario *(denegado por el proveedor)* | MJ | `01:50:11 ≈ 11:01` | «actualmente cada uno cambia su clave, pero si el administrador tiene permiso para visualizar la clave de otro usuario, perfecto» | Preferencia |
| R4 | El módulo Catálogo debe llamarse/funcionar como **Parametrización** y contener: centro de costo, plan de cuentas, elementos de costo, tipos de documentos, **tipos de referencia**, **códigos financieros** (+ factores) | MJ | `02:48:20 ≈ 17:00` y `02:50:30 ≈ 17:03` | «te puse que fuera parametrización… ahí deberían estar el centro de costo, el plan de cuentas, los elementos de costo, los tipos de documentos, los tipos de referencia. Los códigos financieros» | Dato duro |
| R5 | Toda **creación/modificación/eliminación** de maestros vive en Parametrización; a quien no tenga el permiso **no debe aparecerle el módulo** | MJ | `02:56:31 ≈ 17:39` | «sean los únicos que puedan modificar, agregar, eliminar… no le aparezca el módulo de parametrización» | Dato duro |
| R6 | **Aprobación de supervisor** al crear/editar proforma o trabajo diario; y **re-aprobación al editar** algo ya autorizado | MJ | `03:37:00 ≈ 22:12` y `03:45:40 ≈ 22:34` | «pediría aprobación de algún supervisor… Porque si no va a quedar muy abierto a que modifiquemos demasiado el día a día» / «ya ingreso una proforma diaria y alguien la autoriza, y después esa proforma hay que editarla. Al editarla, igual pedirá una autorización de la persona que autorizó» | Dato duro |
| R7 | **Selección múltiple de proformas → una factura** (3 o 4 proformas por factura), con el check junto al **estado** | MJ | `03:54:41 ≈ 23:28` y `03:59:41 ≈ 23:58` | «que uno pudiera pinchar varias proformas y poder facturarlas… que 3 o 4 proformas pertenezcan a una factura» | Dato duro |
| R8 | Filtro por **estado** en proformas (solo facturadas / solo pendientes) | MJ | `04:08:10 ≈ 24:49` | «quizá en estado también poder seleccionar si queremos ver solo las facturadas, solo las pendientes» | Preferencia |
| R9 | **Cierre de mes**: pedir **mes + tipo de cambio**, centralizar **global (no por contratista)** y reconocer **costo vs facturas por recibir contratistas** | MJ | `04:26:30 ≈ 26:39` y `04:28:21 ≈ 26:50` | «solamente se centraliza la información, no se hace por contratista» / «nos aparece qué mes queremos cerrar, tipo de cambio… reconocimiento del costo versus facturas por recibir contratistas» | Dato duro |
| R10 | **Contabilizar desde el libro**: seleccionar cuenta contable, centro de costos, glosa y cliente | MJ | `05:00:51 ≈ 30:03` | «al contabilizar nosotros seleccionamos cuenta contable, centro de costos, le agregamos una glosa, seleccionamos el cliente» | Dato duro |
| R11 | En el libro de compras, **asociar la factura a una OC del sistema** desde la columna de acción | MJ | `04:47:01 ≈ 28:42` | «en acción pueda asociarlo a una orden de compra del sistema» | Dato duro |
| R12 | Libro de ventas alimentado desde el **Excel del SII**; solo factura, **NC** y **ND** | MJ | `05:04:51 ≈ 30:29` y `06:00:51 ≈ 36:03` | «ya sea con nota de crédito o débito, factura, y eso debería cargarse directamente del servicio Impuestos Internos» | Dato duro |
| R13 | **Carga masiva** en libro de ventas **y** libro de compras, con **detección de duplicados** por solape de periodos | MJ | `06:08:40 ≈ 36:52`, `06:10:51 ≈ 37:03`, `06:21:50 ≈ 38:11` | «actualmente nosotros podemos subir un Excel al sistema y contabilizarlo» / «si subimos… del 1 al 7, y si subimos el 14, del 1 al 14, no haga como la distinción de lo que ya está duplicado» | Dato duro |
| R14 | **Renombrar**: «Libro comercial» → **Libro de ventas**; el de compras → **Libro de compras** | MJ | `06:22:20 ≈ 38:13` | «para nosotros el libro comercial es el de compra» | Dato duro |
| R15 | El **cliente lo crea el área contable**, no el vendedor (control antifraude); el registro guarda **el usuario creador** | MJ | `05:15:40 ≈ 31:34` y `05:19:11 ≈ 31:55` | «las personas que crean el cliente somos el área contable, ni siquiera el vendedor… si dejamos a destajo que ellos creen, pueden crear, falsificar documentos» / «debería aparecer como el que crea nomás» | Dato duro |
| R16 | **No existe maestro de vendedores** | MJ | `05:26:00 ≈ 32:36` | «Claro, o sea que no tenemos vendedores» | Dato duro |
| R17 | Campos de creación de contraparte: **giro, razón social, RUT, dirección** | MJ | `05:23:11 ≈ 32:19` | «lo que necesitamos para crear un vendedor es el giro, la razón social, el RUT. Dirección y eso» | Dato duro (con ambigüedad «vendedor»/«cliente») |
| R18 | La **OC** debe llevar **proveedor, departamento, cuenta contable, centro de costo, elemento de costo** (es el documento que imputa el costo) | MJ | `05:40:40 ≈ 34:02` | «ahí falta la cuenta contable y el centro de costo, que al final es la orden de compra la que ha imputado el costo. Adicionar el elemento de costo también» | Dato duro |
| R19 | La OC muestra **neto** y, si aplica, **impuesto** | MJ | `05:47:31 ≈ 34:44` | «en la orden de compra aparece el neto y si tiene impuestos, el impuesto» | Dato duro |
| R20 | En recepciones, poder **editar el tipo de cambio** | MJ | `06:37:01 ≈ 39:42` | «Editar el tipo de cambio, ¿cierto?» | Dato duro |
| R21 | Al cargar el libro de compras, ver las **OC del proveedor por RUT** y elegir cuál se contabiliza (ej. factura 77 → OC 4) | MJ | `06:47:40 ≈ 40:46`, `07:00:50 ≈ 42:05` | «seleccionar la factura y ver qué órdenes de compra están asociadas al RUT del proveedor» / «si esa factura es la 77, que diga orden de compra 4» | Dato duro |
| R22 | El **maestro de artículos NO lleva stock ni costo promedio** | MJ | `07:10:40 ≈ 43:04` | «El stock no es necesario porque el maestro de artículo es la creación. Ni el costo promedio» | Dato duro |
| R23 | El artículo define **la cuenta contable de consumo** que se usa al centralizar | MJ | `07:17:01 ≈ 43:42` | «si yo creo un artículo, por ejemplo, bolsas, yo voy a pedir que se vaya a la cuenta contable que es costo materiales de embalaje… ahí por indicación se sabe a qué cuenta contable se debe ir cada consumo» | Dato duro |
| R24 | **Selector de bodega** en movimientos (no solo filtro avanzado) | MJ | `07:31:10 ≈ 45:07` | «a veces uno quiere buscar por bodega y no por movimiento» | Dato duro |
| R25 | **Devolución a proveedor** con **tipo de cambio específico**, identificada por tipo de movimiento **salida proveedor** | MJ | `07:37:40 ≈ 45:46` y `07:47:20 ≈ 46:44` | «¿qué pasa cuando ya tengamos una devolución de proveedor? Y que tenga que salir con un tipo de cambio específico, ¿se va a poder hacer?» / «la devolución nosotros la identificamos por el tipo movimiento porque es salida proveedor» | Dato duro |
| R26 | El **plan de cuentas** tiene **niveles** (clasificación / agrupación) y **cada cuenta parametriza si exige centro de costo** | MJ | `08:11:21 ≈ 49:07` | «tiene niveles, que algunos son de clasificación y los otros son de agrupación… si nosotros queremos una cuenta contable, agregarle centro de costo, que vaya. Si la queremos quitar, quitársela» | Dato duro |
| R27 | Los módulos operativos solo **aplican** información; mantención y modificación viven en Parametrización | MJ | `08:44:21 ≈ 52:26` | «Todo lo que sea modificación y mantención que queden en la parametrización. Y que en los módulos, que solamente en la aplicación de la información» | Dato duro |
| R28 | Cargar los **centros de costo** que envió, precargados desde el día 1 | MJ | `02:45:40 ≈ 16:32` | «te mandé un listado de centros de costo… No sé si se podrán cargar» | Dato duro |
| R29 | Paginación más fina (de 5 en 5) | MJ | (dentro del bloque `04:09:11 ≈ 24:55`, respuesta a Carlos) | Carlos: «lo dejamos como 5, 15 y todos, pero igual se puede dejar una paginación un poquitito más amplia en caso de que quieran de 5 a 5» | Preferencia |

---

## Reglas de negocio concretas

Todo lo cuantificable/nominal que aparece en la transcripción. **No hay en Reu3 ningún código de cuenta
contable, ningún código de tipo de documento SII, ningún nombre de bodega, ningún porcentaje, ninguna moneda
nombrada ni ningún plazo en días.** Es importante decirlo: esos datos quedaron en los **Excel adjuntos al Trello**
(plan de cuentas, centros de costo, elementos de costo) y en un envío pendiente (estados de movimiento de bodega).

| Categoría | Valor concreto | Fuente |
|---|---|---|
| Roles as-is | **administrativo**, **digitador** | MJ `01:01:00 ≈ 06:06` |
| Rol propuesto | **vendedor** (ejemplo inventado por Carlos, con acceso solo a Catálogo › Monedas) | Carlos `01:20:51 ≈ 07:25` |
| Rol propuesto | **aprobación de proformas** | Carlos `03:40:30 ≈ 22:03` |
| Rol propuesto | **cambio de clave** (permiso granular) | Carlos `01:20:51 ≈ 10:38` |
| Regla de roles | **Un usuario = un solo rol.** Si se necesitan dos, se crea un rol combinado | Carlos `01:20:51 ≈ 09:00` |
| Contraseñas | El admin **no ve** la contraseña; solo puede **resetear** con una temporal | Carlos `01:51:50 ≈ 11:11` |
| Multiempresa | Usuarios **por empresa**, con acceso a **una o varias**; el selector de empresa pide también **periodo** | MJ `02:32:01 ≈ 15:12`; Carlos `02:25:50 ≈ 14:32` |
| Parametrización | 7 maestros: centro de costo · plan de cuentas · elementos de costo · **tipos de documentos** · **tipos de referencia** · **códigos financieros** · **factores (de honorarios)** | MJ `02:50:30 ≈ 17:03`, `08:48:51 ≈ 52:53`; Carlos `08:19:31 ≈ 49:56` |
| Proformas | Estados: **asociado / facturado / pendiente**; **borrador → definitiva**; si está **facturada, sin acciones** | Carlos `02:59:30 – 03:21:51 ≈ 17:57 – 20:11` |
| Proformas → factura | **3 o 4 proformas por factura** (agrupación N:1) | MJ `03:54:41 ≈ 23:28` |
| Asociaciones laborales | Columnas: **contratista, labor, actividad, monto, estado** | Carlos `03:08:21 ≈ 18:50` |
| Cierre de mes | Entradas: **mes** + **tipo de cambio**. Centralización **global**, no por contratista. Reconoce **costo vs «facturas por recibir contratistas»** | MJ `04:28:21 ≈ 26:50` |
| Contabilizar libro | 4 datos: **cuenta contable, centro de costo, glosa, cliente** | MJ `05:00:51 ≈ 30:03` |
| Libro de ventas | Tipos: **factura, nota de crédito, nota de débito**. Origen: **Excel del SII** | MJ `05:04:51 ≈ 30:29` |
| Nomenclatura cliente | Para Almahue, **«libro comercial» = libro de compras**. Renombrar el de ventas a **«Libro de ventas»** | MJ `06:22:20 ≈ 38:13` |
| Dedup carga masiva | Escenario declarado: cargar **01–07 de agosto**, luego **01–14 de agosto** → no duplicar el solape | MJ `06:10:51 ≈ 37:03` |
| Estados de OC (mockup) | **aprobado · emitido · «reaccionado» (sic) · contabilizado · borrador** | Carlos `≈ 33:35` |
| Imputación de costo | La **OC** imputa: **cuenta contable + centro de costo + elemento de costo + departamento** | MJ `05:40:40 ≈ 34:02` |
| Montos OC | **Neto** + **impuesto** (si aplica) | MJ `05:47:31 ≈ 34:44` |
| Tipo de cambio | Editable en **recepciones**, y el cambio debe **propagarse a todos los módulos** | Carlos `06:37:30 ≈ 39:45` |
| Ejemplo de trazabilidad compra | **Factura 77 → Orden de compra 4** | MJ `07:00:50 ≈ 42:05` |
| Maestro de artículos | **Sin stock, sin costo promedio.** Con **familia** y **cuenta contable de consumo** | MJ `07:10:40 ≈ 43:04`, `07:17:01 ≈ 43:42` |
| Ejemplo de cuenta | Artículo **«bolsas»** → cuenta **«costo materiales de embalaje»** | MJ `07:17:01 ≈ 43:42` |
| Bodegas | Campos mínimos: **código + nombre** | Carlos `07:21:51 ≈ 44:09` |
| Devolución proveedor | Tipo de movimiento **SALIDA PROVEEDOR**, con **tipo de cambio propio**, cuidando el **precio promedio** | MJ `07:47:20 ≈ 46:44`; Carlos `07:40:30 ≈ 46:03` |
| Plan de cuentas | Tiene **niveles**: de **clasificación** y de **agrupación**. Cada cuenta parametriza si **exige centro de costo** | MJ `08:11:21 ≈ 49:07` |
| Indicadores BC | Sincronización automática **a las 09:00**; fallback manual; historial de última sincronización | Carlos `≈ 51:04` |
| Paginación | **5 / 15 / todos** (cliente pide también de 5 en 5) | Carlos `04:09:11 ≈ 25:24` |
| Formatos de exportación | **Excel y PDF** (a definir por pantalla — el cliente aún no respondió) | Carlos `04:09:11 ≈ 25:35` |
| Entorno | Servidor de pruebas por **IP**; usuario semilla **`admin@almawe.cl`**; contraseña de ejemplo **`demo123!`** | Carlos `23:01 ≈ 02:18`, `01:09:40 ≈ 06:40` |
| Otro proyecto en la misma IP | **FreshLink** (con AlmaWeb) | Carlos `08:50:11 ≈ 53:40` |
| Sociedades | **Ninguna nombrada explícitamente.** «El MAU» (`02:24:20 ≈ 14:25`) y «LM» son ASR dudoso, probablemente «Almahue» y otra sigla. **No lo doy por bueno.** | — |

---

## Decisiones cerradas vs temas abiertos

### Cerradas en la reunión

| Decisión | Quién cierra | Timestamp |
|---|---|---|
| **No habrá maestro de Vendedores**; se registra el usuario creador del cliente | MJ acepta, Carlos formula | `05:26:00 – 05:26:40 ≈ 32:36` |
| **No se agrega campo «contacto de la empresa»** en el panel de clientes | MJ lo descarta | `05:20:30 ≈ 31:59` |
| **Renombrar** Libro comercial → **Libro de ventas**; y el otro → **Libro de compras** | MJ | `06:22:20 ≈ 38:13` |
| **Maestro de artículos sin stock ni costo promedio** | MJ | `07:10:40 ≈ 43:04` |
| El **catálogo pasa a llamarse/comportarse como Parametrización** y absorbe plan de cuentas, elementos de costo, centros de costo, códigos financieros y factores | MJ pide, Carlos acepta: *«vamos a hacer ese traslado de los paneles»* | `08:44:21 – 08:50:11 ≈ 52:26 – 53:01` |
| **Al editar una proforma ya aprobada se vuelve a pedir autorización** | Carlos plantea, MJ: *«Sí, perfecto»* | `03:47:40 – 03:48:21 ≈ 22:46` |
| **Debe registrarse el nombre de quien aprobó** | Carlos plantea, MJ: *«Sí, perfecto»* | `03:50:21 ≈ 23:02` |
| **Selección múltiple de proformas** con check junto al **estado** | MJ elige la ubicación | `03:59:41 ≈ 23:58` |
| **El administrador no verá contraseñas**; solo reset | Carlos impone, MJ: *«Ya, entiendo»* | `01:51:50 – 01:56:31 ≈ 11:11 – 11:44` |
| **Un usuario = un rol** | Carlos (limitación del sistema) | `01:20:51 ≈ 09:00` |
| **El panel GoSocket no es administrable**: será solo consulta *«si es que se conserva»* | Carlos (corrige un malentendido del equipo) | `05:26:40 ≈ 32:41` |
| Próxima reunión: **jueves PM**, hora a confirmar la misma mañana | ambos | `09:25:30 ≈ 55:35` |

### Abiertos al cierre de Reu3

| Tema abierto | Estado literal | Timestamp |
|---|---|---|
| **¿La reversa de un documento requiere aprobación de administrador?** | MJ: *«No sé, que es un poco más abierto porque sé que hay el rol del digitador»* — **sin respuesta** | `04:43:01 ≈ 28:18` |
| **¿Los centros de costo son transversales a todas las empresas?** | MJ lo **pregunta** y Carlos responde sobre otra cosa (columnas). **Nunca se contesta.** | `02:19:41 ≈ 13:56` |
| **Qué pantallas necesitan exportar y en qué formato (Excel/PDF)** | Carlos lo pide como tarea; MJ no responde en la reunión | `04:09:11 ≈ 26:06` |
| **Plan de cuentas real** | MJ debe enviarlo: el del mockup *«no tiene mucho que ver»* | `08:03:10 ≈ 48:19` |
| **Estados de movimiento de bodega** | MJ debe enviar el catálogo | `07:55:40 ≈ 47:34` |
| **¿Fusionar el módulo de Indicadores con el de Monedas?** | Carlos lo ofrece; sin decisión | `≈ 51:52` |
| **Tratamiento del impuesto en la OC** | Carlos: *«no estaba bien aplicado, pero ahí tendría que consultarlo directamente con los chicos»* | `05:50:20 ≈ 35:01` |
| **Reportería** | Explícitamente **en standby** hasta cerrar la lógica; luego una pestaña por módulo | `≈ 54:14` |
| **Pantalla de Traspaso y cierre** | Carlos: *«te voy a informar por privado… está como una de las que tendríamos que tener más cuidado»* → **el detalle se acordó fuera de la reunión y no está en ningún registro** | `04:32:41 ≈ 27:16` |

---

## Contraste con la minuta IA

Comparado contra [`fuentes/reunion3-minuta-tldv-2026-07-28.md`](../fuentes/reunion3-minuta-tldv-2026-07-28.md).

Balance general: la minuta es un **índice de timestamps notablemente preciso** (verifiqué la conversión ×6 con
más de 15 anclas y todas caen dentro de ±20 s). Como **fuente de requisitos es peligrosa** por dos vicios
sistemáticos: (a) **borra al hablante**, de modo que una propuesta del proveedor y un requisito del cliente
quedan indistinguibles; (b) **convierte preguntas abiertas en hechos afirmados**.

### A. Lo que la minuta afirma y la transcripción NO respalda

| # | Afirmación de la minuta | Lo que dice realmente la transcripción | Gravedad |
|---|---|---|---|
| A1 | *«Centros de costo son **transversales a todas las empresas** en el sistema 13:59»* (§3) | `[T 02:19:41 ≈ 13:56]` MJ **pregunta**: *«pero por ejemplo, acá los centros de costo va a ser transversal en todas las empresas»*. Carlos responde sobre el mostrar/ocultar columnas y **nunca contesta la pregunta**. La minuta convierte una **duda sin resolver** en una **regla de diseño multiempresa**. | **Grave** |
| A2 | *«Devolución genera **dos movimientos** con tipo específico para control de precio promedio 46:34»* (§7) | `[T 07:40:30 ≈ 46:03]` es **Carlos preguntando**: *«si hay una devolución, ¿se generan 2 movimientos como con la reserva?»*. MJ responde `[T 07:47:20]` con algo **distinto**: *«la devolución nosotros la identificamos por el tipo movimiento porque es salida proveedor»* — habla de **tipo de movimiento**, no de dos asientos de inventario. La minuta ascendió una hipótesis del proveedor a especificación. | **Grave** |
| A3 | *«**Vendedor asignado aparece en panel de clientes** para identificación 30:54»* (§5) | Ese timestamp es Carlos **observando el mockup** y proponiendo añadir un contacto. El hilo **termina en la conclusión contraria** (`≈ 32:36`): **no existen vendedores** y lo que debe quedar registrado es **el usuario creador**. La minuta congela el estado intermedio y **pierde la decisión**. | **Grave** |
| A4 | *«Usuarios pueden cambiar contraseña desde su perfil con opción de administrador 09:53»* (§2) | Carlos dice lo **opuesto** sobre el estado actual: *«los usuarios **no tienen** directamente la posibilidad de cambiar la contraseña de momento»*, y que el equipo *«estábamos **esperando que nos confirmen**»*. Es una **opción en evaluación**, no una funcionalidad. | Media |
| A5 | *«**Modelo de proformas** se basa en capturas de **AgroSmart**»* (§4) | Correcto en el fondo, pero la minuta **propaga el error de ASR**: el sistema del cliente es **Agrosoft**. Cualquier búsqueda documental por «AgroSmart» falla. | Menor pero contaminante |
| A6 | *«**Movimientos de bodega incluyen filtros avanzados** por bodega y tipo de movimiento 44:26»* (§7) | Presentado como característica existente. En realidad ese pasaje es Carlos **reportando que el equipo de desarrollo se negó** a poner un selector de bodega, y **tanto él como MJ discrepan** y piden el selector. La minuta invierte el sentido del pasaje. | Media |
| A7 | *«Configuración de columnas se guarda por sesión y usuario en diferentes computadores 13:47»* (§3) | Es una **feature que Carlos vende**, no un requisito del cliente. La minuta la mezcla en la misma lista que los requisitos. | Menor |
| A8 | *«Estados de órdenes de compra incluyen aprobado, emitido, **reaccionado**, contabilizado y borrador»* (§6) | Reproduce el término **«reaccionado»** sin marcarlo. No es una palabra de negocio: es ASR sobre *recepcionado* o *reversado*. Un implementador podría crear literalmente ese estado. | Media |
| A9 | *«Usuario enviar **plan de cuentas**, elementos de costo y centros de costo actualizados **16:34**»* (§1) | En `16:34` MJ solo menciona **centros de costo**. El compromiso sobre el **plan de cuentas real** ocurre en `≈ 48:19`. Timestamp mal atribuido. | Menor |

### B. Lo que la transcripción trae y la minuta perdió

| # | Contenido ausente en la minuta | Timestamp | Por qué importa |
|---|---|---|---|
| B1 | **Renombrado Libro comercial → Libro de ventas**, porque *«para nosotros el libro comercial es el de compra»* | `06:22:20 ≈ 38:13` | Es una **decisión de nomenclatura del cliente** que afecta menú, rutas y reportes. La minuta **no la menciona en absoluto**. Es la omisión más costosa. |
| B2 | **El maestro de artículos NO debe llevar stock ni costo promedio** | `07:10:40 ≈ 43:04` | Requisito **negativo** explícito del cliente. Los requisitos negativos son justo los que una minuta por bullets pierde, y son los que generan retrabajo. |
| B3 | **No existe maestro de Vendedores** (ver A3) | `05:26:00 ≈ 32:36` | Evita construir un módulo entero que el cliente no tiene ni quiere. |
| B4 | **El plan de cuentas del mockup «no tiene mucho que ver»** con el real | `08:03:10 ≈ 48:19` | Señal de que todo lo mostrado en Contabilidad era placeholder. |
| B5 | **Ejemplo concreto: factura 77 → OC 4**; y la vinculación **por RUT del proveedor** | `07:00:50 ≈ 42:05`, `06:56:40 ≈ 41:40` | La minuta dice «botón de seleccionar factura para ver órdenes de compra asociadas» pero **pierde la clave de cruce (RUT)** y el ejemplo. |
| B6 | **Ejemplo de imputación: artículo «bolsas» → cuenta «costo materiales de embalaje»** | `07:17:01 ≈ 43:42` | Único ejemplo nominal de cuenta contable en toda la reunión. |
| B7 | **La reversa con aprobación quedó ABIERTA** («No sé…») | `04:43:01 ≈ 28:18` | La minuta lista la reversa como funcionalidad sin señalar que el control quedó sin definir. |
| B8 | **Aclaración de GoSocket: el panel fue un malentendido del equipo de desarrollo**; será solo consulta *«si es que se conserva»* | `05:26:40 ≈ 32:41` | La minuta dice solo «GoSocket es proceso intermediario». Pierde que **la pestaña podría desaparecer**. |
| B9 | **Agrosoft no la deja exportar Excel** → tuvo que mandar 7 pantallazos | `11:40 ≈ 01:10` | Dolor operativo directo del sistema actual; motiva el requisito de exportar Excel/PDF. |
| B10 | El cliente pide **«tipos de referencia»** dentro de parametrización | `02:50:30 ≈ 17:03` | La minuta enumera la parametrización pero **omite «tipos de referencia» y «códigos financieros»** en §3 (los códigos financieros solo aparecen en un ítem de acción de §1). |
| B11 | **Segregación de visibilidad**: a quien no tenga permiso **no debe aparecerle el módulo** de parametrización | `02:56:31 ≈ 17:39` | Requisito de RBAC de visibilidad de menú, no solo de permiso de escritura. |
| B12 | **El cambio de tipo de cambio en recepciones debe reflejarse en TODOS los módulos** | `06:37:30 ≈ 39:45` | La minuta solo dice «agregar botón de editar tipo de cambio en recepciones». Pierde el efecto en cascada. |
| B13 | **Motivación antifraude** de que solo contabilidad cree clientes: *«pueden crear, falsificar documentos»* | `05:17:41 ≈ 31:46` | La minuta dice «para evitar falsificación» pero pierde que el pedido viene de los **vendedores** y que contabilidad lo **niega deliberadamente**. |
| B14 | **Carlos derivó el diseño de Traspaso/Cierre a un canal privado** | `04:32:41 ≈ 27:16` | Hay una conversación de diseño de la pantalla más crítica **fuera de todo registro**. |
| B15 | **La misma IP sirve otro proyecto, FreshLink/AlmaWeb** | `08:50:11 ≈ 53:40` | Contexto de entorno; explica confusiones de acceso. |
| B16 | Compromiso de fecha: **funcional antes de agosto, ojalá el viernes** (dicho el 28/07) | `04:48:11 ≈ 28:55` | La minuta lo tiene (`29:14`) pero sin el «hoy estamos a 28» que lo fecha. |
| B17 | **Los timestamps de la transcripción están comprimidos ×6** | — | Sin esto, cualquiera que intente cruzar transcripción y minuta concluye que una de las dos está mal. |

### C. Advertencia transversal sobre la minuta

De los **38 ítems de acción** de la §1, **todos** están atribuidos genéricamente a *«Equipo de desarrollo»* o
*«Usuario»*. La minuta **nunca dice quién pidió qué**. Aplicada la regla del proyecto (cliente = requisito,
proveedor = propuesta), esto significa que **la §1 completa no es utilizable para decidir alcance**. Por ejemplo,
«crear rol específico para aprobación de proformas» **lo propone Carlos**, mientras que «implementar aprobación
de proformas por supervisor en edición» **lo exige MJ** — son cosas de peso muy distinto y la minuta las presenta
como equivalentes.

---

## Señales para QA

Reu3 aporta evidencia de **cliente** (MJ) para varios casos que hoy pueden estar marcados SKIP/BLOCKED. Ojo:
**Reu3 es del 28/07/2026 y es anterior a Reu4, Reu5, Reu6 y a la sesión del 20/08**. Según la jerarquía de
`AGENTS.md` (Reu6 → Reu5 → Reu4), **nada de aquí revierte por sí solo una decisión posterior**. Lo que sí hace es
demostrar que **el requisito existió y tuvo origen en el cliente**, de modo que si hoy está apagado debe haber una
decisión posterior **explícita** que lo apague — y no un simple olvido.

### Debería ejercerse (evidencia de cliente, sin señal de que se haya revocado)

| Caso | Evidencia | Nota |
|---|---|---|
| **Selección múltiple de proformas → una sola factura (3–4 por factura)** | MJ `03:54:41 ≈ 23:28` | Requisito de cliente, dato duro. No aparece en la lista de «cerrado en código local» de `AGENTS.md`. **Verificar si el ERP lo soporta**; si el caso está SKIP, no hay base para saltarlo. |
| **Carga masiva Excel SII en libro de compras y libro de ventas, con detección de duplicados por solape** | MJ `06:08:40 ≈ 36:52`, `06:10:51 ≈ 37:03` | Es **as-is funcionando hoy en Agrosoft**: perderlo es una regresión frente al sistema que se reemplaza. Existe `erp_front/src/lib/libroVentasCsv.ts`, pero **el caso crítico es el dedup del solape 01–07 / 01–14**. Ejercer con dos archivos solapados. |
| **Registro de compra: ver las OC del proveedor por RUT y elegir cuál contabilizar** | MJ `06:47:40 ≈ 40:46`, `07:00:50 ≈ 42:05` | Complementa la deuda ya conocida de «asociar factura a OC no aprobada». El **cruce por RUT** es la parte concreta a probar. |
| **Cierre de mes: pedir mes + tipo de cambio; centralizar global (no por contratista); reconocer costo vs «facturas por recibir contratistas»** | MJ `04:28:21 ≈ 26:50` | Regla contable dura. Si hay casos BLOCKED por «no está definido el cierre», **sí está definido**: entradas y salida están en la transcripción. |
| **Maestro de artículos sin stock ni costo promedio** | MJ `07:10:40 ≈ 43:04` | Es un **caso negativo**: verificar que el maestro **no** exponga esos campos. El código sí tiene `costoPromedio` en `insumos.service.ts`, `stock-bodega.util.ts` y `EmitirDocumentoPage.tsx`; hay que distinguir **cálculo por bodega** (correcto) de **campo en el maestro** (que el cliente rechazó). |
| **Artículo → cuenta contable de consumo aplicada al centralizar** | MJ `07:17:01 ≈ 43:42` | Cadena completa: artículo «bolsas» → consumo → asiento a «costo materiales de embalaje». Si el caso está SKIP por «falta parametrización», el requisito está claro. |
| **Devolución a proveedor: tipo de movimiento SALIDA PROVEEDOR con tipo de cambio propio, sin distorsionar el costo promedio** | MJ `07:37:40 ≈ 45:46`, `07:47:20 ≈ 46:44` | `AGENTS.md` ya registra `ENTRADA_PROVEEDOR`; **falta comprobar la salida/devolución y su efecto en el costo promedio**. Alta prioridad: es una regla contable, no cosmética. |
| **Editar tipo de cambio en recepciones y verificar propagación a todos los módulos** | Carlos `06:37:30 ≈ 39:45` (propuesta aceptada sobre pedido de MJ) | El pedido de editar es del cliente; **la propagación es propuesta del proveedor**: probar, pero no tratar la propagación como requisito duro. |
| **Cada cuenta contable parametriza si exige centro de costo (y niveles clasificación/agrupación)** | MJ `08:11:21 ≈ 49:07` | Se conecta con la deuda P0-1 conocida («asiento de libro sin cuenta imputable»). El cliente **ya definió** que la exigencia de CC es **por cuenta**. |
| **Usuarios por empresa con selección múltiple de empresas** | MJ `02:32:01 ≈ 15:12` | Cruzar con el aislamiento por `empresaId`: el requisito es **usuario → N empresas**, no usuario global. |
| **En movimientos y registros mostrar el nombre del usuario, no el rol** | MJ `01:01:00 ≈ 06:06` | Requisito de auditoría barato de verificar y fácil de haber perdido. |
| **Cliente creado solo por área contable; se registra el usuario creador; sin maestro de Vendedores** | MJ `05:15:40 ≈ 31:34`, `05:26:00 ≈ 32:36` | Cruza con la ficha única cliente/proveedor. **No** construir Vendedor. |
| **Tipos de referencia y códigos financieros disponibles en Parametrización** | MJ `02:50:30 ≈ 17:03` | Ambos existen en el repo (`seed-tipos-referencia.ts`, `CodigosFinancierosPage.tsx`, `seed-codigos-financieros-reu.ts`); verificar que estén **bajo Parametrización** y con el RBAC de B11. |

### Probablemente NO deba ejercerse tal cual (revisar antes)

| Caso | Motivo |
|---|---|
| **Aprobación de proformas por supervisor + re-aprobación al editar + nombre del aprobador** | MJ lo pidió con claridad (`03:37:00 ≈ 22:12`, `03:45:40 ≈ 22:34`, `03:50:21 ≈ 23:02`) y es un **dato duro con motivación de control**. Pero `AGENTS.md` registra como cerrado que las proformas van `BORRADOR → DEFINITIVA` con `contratistas:write`, **sin bandeja ni PIN**. **Acción sugerida: no lo ejercites a ciegas, pero tampoco lo cierres como «nunca se pidió».** Hay que localizar en Reu6 o en la sesión del 20/08 tarde la decisión que lo revoca; si no aparece, es un requisito de cliente perdido, no una funcionalidad de más. |
| **Centros de costo transversales entre empresas** | La minuta lo afirma, pero **es una pregunta sin respuesta** (A1). Cualquier caso de prueba que asuma transversalidad se apoya en una alucinación de la minuta. **Debe quedar BLOCKED hasta preguntarle al cliente.** |
| **Reversa con aprobación de administrador** | Abierto explícitamente (`04:43:01 ≈ 28:18`). Correcto mantenerlo SKIP con la razón «pendiente de definición del cliente». |
| **Devolución genera dos movimientos** | Es hipótesis del proveedor (A2), no confirmada. No escribir el caso con esa aserción. |
| **Estado de OC «reaccionado»** | ASR corrupto (A8). No crear ni probar ese estado. |
| **Panel administrable de GoSocket** | Carlos lo declaró un **malentendido del equipo** y dijo *«si es que se conserva»* (`05:26:40 ≈ 32:41`). Casos que traten GoSocket como pantalla administrable están mal fundados. |
| **Administrador ve contraseñas** | Pedido por MJ pero **denegado por el proveedor y aceptado por MJ** (`01:56:31 ≈ 11:44`). No es requisito. |

### Datos que faltan y que bloquean casos legítimamente

Estos quedaron **pendientes de envío por el cliente** en Reu3; si no llegaron, los casos que dependan de ellos
están BLOCKED con razón:

1. **Plan de cuentas real** (`08:03:10 ≈ 48:19`) — el del mockup era placeholder.
2. **Catálogo de estados de movimiento de bodega** (`07:55:40 ≈ 47:34`).
3. **Definición por pantalla de qué exportar y en qué formato** (`04:09:11 ≈ 26:06`).
4. **Detalle de la pantalla de Traspaso y cierre**, que Carlos derivó a **canal privado** (`04:32:41 ≈ 27:16`) y
   por tanto **no consta en ninguna fuente auditable**.

---

## Anexo — términos dudosos por ASR

No los resuelvo; los dejo marcados para que nadie los tome como literales.

| En la transcripción | Lectura probable | Confianza |
|---|---|---|
| «AgroSmart» | **Agrosoft** | Alta |
| «En Kua al Mawe» / «al MAWE» | **En QA AlmaWeb** / **AlmaWeb** | Media-alta |
| «el MAU» (`02:24:20`) | **Almahue** | Media |
| «LM» (`02:24:20`) | Otra sociedad, sin identificar | Baja |
| «reaccionado» (estado de OC) | **recepcionado** o **reversado** | Media |
| «del servicio Impuestos Internos **de Vozaker**» (`05:04:51`) | ¿**GoSocket**? | **Baja — no usar** |
| «Marino» (`07:16:41`), «Mario» (`09:27:01`) | **Mari** (María José / María Jesús) | Alta |
| «en el **tráiler** captura de pantalla» (`02:11:31`) | **en el Trello** | Media-alta |
| «Estas son las compras de la tienda» (`05:12:31`) | Frase inconexa, **ininteligible en contexto** | — |
| «Y ya tenemos el hito» (`03:50:21`) | Sin sentido claro en contexto | — |
