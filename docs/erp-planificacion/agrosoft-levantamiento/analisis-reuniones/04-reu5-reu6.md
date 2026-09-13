# Reu5 + Reu6 — análisis desde transcripción

> Elaborado leyendo **completas** las dos transcripciones verbatim, sin apoyarse en las minutas.
> Fuentes primarias:
> - [`../fuentes/transcripcion-reunion5.md`](../fuentes/transcripcion-reunion5.md)
> - [`../fuentes/transcripcion-reunion6.md`](../fuentes/transcripcion-reunion6.md)

---

## Ficha

### Reu5 — 03/08/2026

| Campo | Dato |
|---|---|
| Asistentes reales | **Speaker 00 = Carlos Vallejos** (presenta/demuestra) · **Speaker 01 = Sergio** (pide/valida) · **Speaker 02** = intervenciones muy cortas, probablemente el mismo Sergio partido por la diarización |
| **Cliente presente** | **NINGUNO.** No hay Agustín, MJ, Lupe, Mario ni Fran |
| Naturaleza | Revisión interna proveedor↔proveedor de ajustes pendientes de deploy |
| Duración real | **≈ 42–43 min** (ver nota de reloj) |

**Hallazgo de método nº1 — Reu5 no contiene ni un solo requisito de cliente.** Todo lo que se dice es proveedor. Cuando Carlos invoca al cliente lo hace **de oído y en pasado** («como lo dijo la María José», «ella había pedido», «según como lo solicitó la Mari»), es decir, testimonio de segunda mano sobre reuniones anteriores. Cualquier ítem que hoy se cite como «pedido en Reu5» es, en rigor, una **decisión de diseño de Devint**.

**Nota de reloj (importante).** Los timestamps del archivo de transcripción de Reu5 están **inflados ≈10×** respecto de los de tl;dv. Comprobación:

| Tema | tl;dv | Transcripción | Ratio |
|---|---|---|---|
| Clave de cuenta al cambiar PIN | 03:57 | `[39:01]` | 9,9 |
| Totalizados libro de compras | 10:35 | `[01:45:50]` | 10,0 |
| Cartolas bancarias pendientes | 40:36 | `[06:48:10]` | 10,1 |

En este documento cito el timestamp **tal cual aparece en la transcripción** y, cuando ayuda, agrego entre paréntesis el minuto real aproximado (`÷10`). El encabezado del propio archivo ya advertía «si el player del MP4 no calza, anclar y corregir como en Reu4»: **queda confirmado que no calza**.

### Reu6 — 06/08/2026

| Campo | Dato |
|---|---|
| Proveedor | **Carlos Vallejos** (presenta la demo) · **Sergio** (abre y modera) |
| Cliente | **Speaker 00 = Agustín** · **Speaker 01 = María Jesús (MJ)** · Mario y Lupe presentes pero **no hablan** en la transcripción (solo son nombrados: «Mario se pegó de nuevo» `[52:06]`, «Lupe, no caigas a esa factura» `[51:39]`, «Gracias, Mario» `[01:04:19]`) |
| Naturaleza | **Demo transversal de avance** con cliente presente. Es la primera de las dos que constituye fuente de requisitos |
| Duración | ≈ 1 h 06 min (timestamps consistentes, sin desfase) |
| Cierre | Los últimos ~2 min (`[01:04:36]`–`[01:06:08]`) son Carlos↔MJ a solas, tema agenda/personal |

**Advertencias de calidad de la transcripción de Reu6:**

- La diarización **mezcla turnos**. Ejemplo claro: `Speaker 00 [09:19]` contiene la pregunta de Agustín **y** la respuesta «Exactamente» que corresponde a Carlos.
- Hay fragmentos **claramente corruptos** que NO deben citarse como requisito: `[16:49]` «te hice ver la hora de contrapaso», `[17:15]` «si la pared que tú usas de vacaciones», `[17:27]` «pueden haber unos 50 niveles bajos», `[18:24]` «si viene con la quemadura», `[20:22]` «para que Nico se la juegue, pueden pasar por años», `[36:13]` «cuando le guste le enviamos los bancos».
- Nombres mal transcritos: MJ llama «Pablo» a Carlos en `[03:35]`; «Almaue», «Almagüe», «AlmaWeb» conviven; «la Siri»/«la SIDI»/«la Fran» parecen ser la misma persona (**Fran**).
- Reu5 tiene el mismo problema: «Demirel» `[01:45:50]` es un nombre de sistema no identificable con certeza.

---

## As-is Agrosoft

### Lo que Reu5 aporta sobre el as-is: **nada**

Reu5 **no muestra Agrosoft**. El sistema que Sergio comparte en pantalla y propone como referencia visual es **producto propio de Devint** («lo que vimos con Better Software» `[01:27:21]`, «te voy a compartir pantalla para que veas cómo lo hace hoy en día de Demirel» `[01:45:50]`). El dato «tenemos buenos [clientes] que emiten 22.000 documentos mensuales» `[03:55:31]` es de **la cartera de Sergio**, no de Almahue. No usar Reu5 como evidencia de as-is.

### Lo que Reu6 sí revela del as-is (dicho por el cliente)

| Tema | Quién | Timestamp | Cita |
|---|---|---|---|
| Plan de cuentas con atributos por cuenta | MJ | `[25:26]` | «actualmente nosotros por cuenta podemos determinar si está asociado a centro de costo, elemento de costo, área de negocio, XX» |
| Plan de cuentas incluye área de negocio con flag activo/inactivo | MJ | `[25:50]` | «en el plan de cuentas que le adjunté, arriba sale como toda el área de negocio que yo puedo pinchar y si está activo o inactivo» |
| Ya existe trazabilidad de creación/modificación de usuarios | MJ | `[34:59]` | «actualmente igual tenemos la trazabilidad de cuándo se hace una modificación o quién hace la creación de cada usuario. Yo creo que eso hay que mantenerlo» |
| Ya existe clave para reversar/eliminar en ciertos paneles | MJ | `[34:59]` | «hay paneles o restricciones que se necesita clave para poder reversar o eliminar» |
| Ventas se emiten hoy **fuera** del ERP, en el sistema de facturación | MJ | `[40:21]` | «cuando nosotros emitimos las ventas lo hacemos directamente en el sistema de facturación, pero ya sabemos lo que vamos a vender» |
| Hoy **no** se cotiza para vender | MJ | `[40:09]` | «a mi criterio las cotizaciones son para las compras» |
| Indicadores se actualizaban a las 9:00 | Carlos (reportando el as-is) | `[23:36]` | «Esto actualmente, por cómo lo utilizaban, se actualizaba a las 9 de la mañana» |
| Los datos bancarios de proveedores se buscan hoy en el correo | Agustín | `[31:51]` | «actualmente está consiguiéndose la cuenta, haciendo buscarla al correo» |
| Cuenta puente «gastos próxima temporada» + traspaso manual cuenta por cuenta | Agustín | `[28:04]`, `[29:04]` | «sale una cuenta que se llama gastos próxima temporada… la administración siempre se tiene que meter cuenta por cuenta y hacer el traspaso una por una, es un cacho» |
| Traslape de temporadas: se activan gastos de la temporada siguiente | Agustín | `[29:04]` | «nosotros por ejemplo aceptamos la temporada 25-26… y yo hoy día estoy pagando servicios de la temporada 26, 27 ya. Entonces obviamente para que no se me ensucie el resultado… la María Jesús agarra todos esos gastos y los activa» |
| Trabajan con stock en tránsito, pero solo en bodega | MJ | `[55:55]` | «nosotros trabajamos con stock en tránsito, pero netamente en la bodega. Pero lo que es venta tiene que estar en stock real» |
| Aprobaciones hoy funcionan por organigrama informal y **se saltan** | Agustín | `[14:52]`, `[20:22]` | «los materiales de hoy día, que por ejemplo yo le autorizo a José Tomás y José Tomás depende de Martín, pero no tiene ningún sentido… No me preguntéis por qué siempre apruebo yo esa cuestión» |
| Proveedor DTE histórico = **Acepta**; nuevo = **GoSocket** (contacto Pablo) | MJ | `[58:29]`, `[57:44]` | «me estoy comunicando con Acepta para hacer el tema de la carga masiva, que nos manden los documentos» |
| Cuentas corrientes en varias monedas por contraparte | Agustín | `[31:51]` | «igual ingresas varias cuentas, por ejemplo, la cuenta en dólares, la cuenta en pesos, la cuenta en pesos 2» |
| Riesgo real de fraude por cambio de cuentas bancarias | Agustín | `[33:07]` | «igual también hay estafas que cambian las cuentas y hartas cosas» |

---

## Requisitos del cliente

**Todos provienen de Reu6.** Reu5 no aporta requisitos de cliente (ver Ficha).

| # | Requisito | Quién | Timestamp | Cita textual | ¿Dato duro o preferencia? |
|---|---|---|---|---|---|
| R1 | Multi-empresa: el usuario se crea eligiendo a qué empresas ve | MJ | `[11:28]` | «cuando tú creas el usuario, elige a las empresas que puedan tener visualización» | **Dato duro** (describe el modelo acordado) |
| R2 | Súper admin ve todas las empresas | Agustín | `[09:19]` | «el súper admin imagino que puede ver toda la empresa y hay otros usuarios que a lo mejor ven cierta empresa, ¿no?» | Preferencia / verificación (fraseado como pregunta) |
| R3 | Se puede recortar acceso al asignar el rol al usuario | MJ | `[11:15]` | «igual cuando uno selecciona el rol le puede despinchar cierto acceso» | **Dato duro** |
| R4 | **Cadena de aprobación multi-nivel por monto** | Agustín | `[12:28]`, `[13:12]` | «¿Tú, por ejemplo, no puedes poner como una cadena de aprobación?» / «si Mario tiene, estoy inventando, la orden de compra es de 400 lucas y Mario tiene por 500, la aprobó… Si era por 10 millones, la va a tener que aprobar mi jefe» | **Dato duro** |
| R5 | El segundo nivel se activa **solo al exceder el límite**, no siempre | Agustín | `[13:42]` | «No, cuando pase el límite, porque obviamente es un monto porque está autorizado para ese monto» | **Dato duro** (corrige explícitamente a MJ, que había dicho «Claro, siempre» en `[13:41]`) |
| R6 | **El creador NO elige aprobador**: se asigna automático por jefatura | Agustín | `[13:50]`, `[14:52]` | «la persona que crea la orden de compra… automáticamente venga asociado a su jefatura» / «sí o sí ella no va a decidir para dónde se va la orden de compra» | **Dato duro** (con motivación anti-fraude explícita: «son amigas, pasó la cuestión y se arreglaron entre las dos» `[14:19]`) |
| R7 | Aprobación por **línea de mando** estricta | MJ | `[16:04]` | «si mi analista hace una orden de compra, solamente le aparezca yo como jefatura para aprobar, no que aparezca otra jefatura. Eso están pidiendo, que vaya en línea de mando… La Fran en este caso no le podría mandar una orden de compra a Mario, siempre tiene que ser a mí» | **Dato duro** |
| R8 | **Suplencia** cuando el aprobador de la línea no está | Agustín / MJ | `[16:41]` / `[16:48]` | Agustín: «si la persona que está en tu línea de aprobación no está, ¿qué pasa?» — MJ: «Pasa a la equipo de la siguiente» | **Dato duro** en la necesidad; **abierto** en el mecanismo (Agustín cierra con «habría que mirarlo… hay que solucionar un par de temas ahí») |
| R9 | Un usuario puede depender de **más de una** jefatura | Agustín | `[19:44]` | «hay casos que podría depender de más de uno y le podríamos dejar a más de una dependencia, y esa persona sí puede mandársela a 2 personas» | Preferencia (Carlos responde «Puede ser», no se cierra) |
| R10 | El aprobador intermedio **revisa aunque no pueda autorizar** («doble check») | Agustín | `[17:27]` | «la Fran le mandó una orden de compra a María Jesús, que María Jesús por el monto no le da, la va a aprobar, pero sin monto va a quedar todavía pendiente y me va a saltar a mí automáticamente hasta que yo pueda… querís que haya esa doble check. Sí» | **Dato duro** |
| R11 | Clientes y proveedores en **bases separadas**, con consulta unificada por RUT | MJ | `[23:06]` | «Yo prefiero que sea base de datos individualizada porque si quiero sacar un listado de proveedores no se me va a mezclar con clientes. Ahora, en la consulta del RUT quedamos que iba a tener el detalle de si tenía RUT como sociedad, estaba creado como proveedor, como cliente, como productor» | **Dato duro** (MJ **revierte** lo que Carlos acababa de proponer en `[22:44]`: «lo dejamos entonces para que sea una base de datos compartida») |
| R12 | Cuenta contable: **inactivar, no eliminar**, si tiene movimiento | Agustín | `[26:42]`, `[27:36]` | «Además que se inactiven, ¿no?… si lo inactiváis van a quedar todos los comprobantes, pero no lo podés utilizar más a cuenta» / «vamos a dejar entonces habilitada solamente la opción de deshabilitar» | **Dato duro** |
| R13 | Atributos por cuenta: CC / elemento de costo / área de negocio, agregables y quitables | MJ | `[25:26]` | «aquí nosotros también deberíamos tener la opción de poder agregarlo, quitarle características» | **Dato duro** |
| R14 | **Ficha única** de contraparte con bancos, contactos y direcciones | Agustín | `[35:45]`, `[33:04]` | «Quisiéramos una ficha, una pura ficha para todo. O sea, cuando me cree el cliente, que él tiene el frente, ponga los contactos, que pongan los datos bancarios, que dobla en la ficha de creación» / «Y n cuentas de banco» | **Dato duro** |
| R15 | **Registro de todos los cambios** en datos sensibles de la ficha | Agustín | `[34:52]` | «cualquier cosa que se cambie, nadie nunca fue. Entonces lo mejor es dejar siempre el registro» | **Dato duro** |
| R16 | Restringir por rol quién edita datos sensibles | Agustín | `[34:16]` | «¿No lo podías dar con clave para que no puedan editar? Sí, o que lo vea gerencia nomás, que lo pueda editar» | Preferencia (mecanismo no cerrado: ¿rol o clave?) |
| R17 | **Ficha de solicitud de alta** de contraparte, con respaldo de quién la pide | Agustín | `[36:13]` | «nosotros hacemos una ficha interna que… le llevamos todo el respaldo de quién está solicitando el proveedor al cliente… Entonces así ya lo creamos al lote, la luz después no anda buscando las cuentas por todos lados, va a estar todo consolidado la información» | **Dato duro** en la intención; frase parcialmente corrupta |
| R18 | Prospectos se guardan **directamente como clientes** | Agustín (citando a MJ) | `[31:01]` | «Por lo que me había dicho la Mari, los prospectos directamente como clientes, porque si lo creamos porque ya está la relación laboral» | **Dato duro** (de segunda mano: Agustín cita a MJ, MJ no lo confirma en la sala) |
| R19 | «Cotizaciones» del menú Ventas debe llamarse **Orden de venta** | MJ | `[40:21]` | «la cotización debería ser el orden de venta, debería llamarse el título» | **Dato duro** |
| R20 | La pantalla de cotización **pertenece al panel de Compras** | MJ | `[40:59]` | «Debe estar en el panel de compras» (confirma a Carlos `[40:56]`; Agustín ratifica en `[41:02]` y `[41:46]`) | **Dato duro** |
| R21 | Orden de venta con **dos tipos**: servicio o producto | Agustín | `[42:18]` | «cuando creas una nueva orden de venta… a ti te debiese dar 2 tipos de orden de venta, ¿cachai? O un servicio o un producto» | **Dato duro** |
| R22 | El producto de la OV viene del **maestro de bodega**, con bodega indicada | Agustín | `[42:34]` | «los productos debiesen venir linkeados a los productos que tú tienes en bodega, e incluso en qué bodega tú lo vas a trabajar» | **Dato duro** |
| R23 | No se pueden inventar descripciones fuera del maestro de productos | Agustín | `[38:25]` | «si tengo caja de 5 kilos granel creada por sistema, Mario, ¿no puede salir a vender cajas cerezas?» | **Dato duro** |
| R24 | Al facturar debe rebajar inventario y generar salida a cliente | Agustín | `[42:59]` | «cuando tú salgas a emitir el documento y tú vengas a buscar esta orden de venta, lo que tiene que hacer por el lado de insumos hacerte la salida del cliente y rebajarte el inventario» | **Dato duro** — pero **ver conflicto con R25** |
| R25 | El movimiento de inventario lo hace la **nota/orden de venta**, no la factura | MJ | `[45:44]` | «si estoy haciendo una nota de venta, o sea, claro, una nota venta, que se mueva inventario. Y si yo lo quiero asociar a la factura, que me traiga solamente la cantidad y el detalle del nombre» | **Dato duro** (MJ **corrige** a Agustín; queda como la definición final porque nadie la rebate) |
| R26 | Al facturar: **cantidad y descripción se conservan, el precio se edita** | MJ | `[46:58]`, `[47:14]` | «lo que a mí me importa es que se mantenga cantidad y descripción de lo que yo estoy vendiendo, pero no el monto, porque eso sí se puede modificar» / «sí o sí el precio habría que modificarlo» | **Dato duro** |
| R27 | El precio se edita **por línea de detalle**, no con recargo global | Sergio pregunta / MJ | `[47:28]` / `[47:49]` | Sergio: «¿tú modificas el monto por cada línea de detalle o le das un recargo global al documento? Por cada línea de detalle, al precio unitario, ¿cierto?» — MJ: «Sí» | Preferencia — **atención: Sergio se autorresponde y MJ solo asiente**; evidencia débil |
| R28 | Ventas solo con **stock positivo**; nada de stock negativo | MJ | `[55:39]` | «Ya, ok, stock positivo. Así obligamos que tengan que tener todo el día» | **Dato duro** |
| R29 | Producto en varias bodegas: ver stock por bodega y **sacar cantidades de cada una** | MJ | `[54:14]`, `[54:48]` | «habría que traer la bodega y ver el stock de cada bodega» / «Si yo elijo un producto que está en 3 bodegas, ¿yo puedo sacar cierta cantidad de cada bodega?» | **Dato duro** (Carlos: «Sí se puede» `[54:54]`; MJ: «Perfecto» `[55:03]`) |
| R30 | No vender por sobre el stock disponible | Agustín | `[55:27]` | «tampoco no puedo vender más que mi stock, o si no, cuando haga el movimiento de bodega te va a rebotar» | **Dato duro** |
| R31 | **No vender bajo el costo** | Agustín | `[49:16]` | «Lo que sí es clave, creo yo, Que no me dejara vender menos del costo» | **Dato duro** en la intención; **el mecanismo queda ambiguo** (ver Reglas de negocio) |
| R32 | Flete y recargos se modelan como **línea adicional** | MJ | `[57:06]` | «Ah, entiendo. Yo le habré que agregar una línea adicional nomás» | **Dato duro** |
| R33 | **No** manejan productos con impuestos adicionales | Agustín | `[57:19]` | Sergio: «Productos con impuestos adicionales no manejan.» — Agustín: «No, nosotros no» | **Dato duro** |
| R34 | Diseño de documentos configurable | Agustín | `[01:02:01]` | «Sí, qué buena esa» (reacción a la propuesta de Sergio en `[01:01:52]`) | **Preferencia** — la idea es del proveedor, no del cliente |
| R35 | SSO Microsoft / login sin contraseña | Agustín | `[04:24]`, `[05:52]` | «Especialmente por usar los mismos correos» / «cuando… hay un correo que expira o ya no se usa, al bloquear la cuenta en Microsoft como que se niega el acceso a cualquier plataforma» | **Preferencia** — Carlos lo baja explícitamente a nota: «vamos a dejarlo como nota ahí para futuro» `[05:47]` |
| R36 | Traspaso masivo de la cuenta «gastos próxima temporada» a cuentas de gasto | Agustín | `[28:04]`, `[29:04]` | «podríamos subir la cuenta de próxima temporada o crearle… una especie de activo de balance abierto por cuenta y después solamente el traspaso por cuenta» | Preferencia — **Agustín mismo lo desactiva**: «Pero no, está perfecto, no hay que hacer nada» `[29:04]` |
| R37 | Cargar **datos reales** en el ambiente publicado desde el día siguiente | MJ | `[01:00:14]`, `[01:00:35]` | «¿nosotros ya podríamos empezar a ingresar información real?» / «la idea es como ir viendo un proceso completo de una compra, un proceso completo de una venta» | **Dato duro** |
| R38 | Carga masiva histórica de DTE vía Acepta | MJ | `[58:29]` | «me estoy comunicando con Acepta para hacer el tema de la carga masiva, que nos manden los documentos» | **Dato duro** (tarea del cliente, no del ERP) |

---

## Reglas de negocio concretas

1. **Escalamiento por monto, no en cascada obligatoria.** Solo se sube de nivel si el monto **excede** la facultad del aprobador actual (R5, `[13:42]`). El nivel superior no participa si el inferior alcanza.
2. **Aprobador determinado por organigrama, no por elección del solicitante** (R6/R7). El motivo declarado es control de colusión, no ergonomía: `[14:19]` «como son amigas, pasó la cuestión y se arreglaron entre las dos».
3. **Doble check obligatorio**: el jefe directo aprueba aunque el monto lo exceda; su aprobación no cierra el flujo, lo escala (R10, `[17:27]`).
4. **Cuenta contable con movimientos: solo inactivar.** Eliminar únicamente si no tiene nada asociado (`[27:23]` Sergio: «la cuenta se podría eliminar siempre y cuando no tenga nada asociado»; `[27:36]` Agustín cierra: solo deshabilitar).
5. **Renombrar una cuenta propaga el nombre al histórico.** Carlos lo confirma (`[27:51]` «Exacto») ante la pregunta de Agustín `[27:36]`. Agustín lo había marcado como riesgo en `[27:11]`: «¿se modifican para atrás también o se modifican solamente desde ahí? Hay que revisar eso». **Queda abierto.**
6. **El documento que mueve inventario es la orden/nota de venta, no la factura** (R25). La factura hereda cantidad y descripción; el precio se sobrescribe porque debe llevar margen: `[46:25]` «la idea es, en la mayoría de los casos, tener un poco de utilidad de lo que estamos vendiendo. Entonces a llamar el mismo precio de la bodega. Por eso, cuando se sale de la bodega es un precio, pero cuando yo emita la factura tiene que asociarse solamente al movimiento de bodega, pero no al monto».
7. **En la factura no se editan producto ni cantidad, solo precio.** Sergio `[47:06]`: «y bueno, los productos, que eso no se editen, solamente el precio»; MJ `[47:14]`: «Lo otro yo lo dejaría tal cual, porque la cantidad igual es importante que vaya en el detalle de la venta».
8. **Stock de venta = stock real positivo.** El stock en tránsito existe pero es exclusivo de bodega y no habilita venta (R28, `[55:55]`).
9. **Precio de venta ≥ costo.** Regla pedida por Agustín. **La base de comparación que se discutió es el precio de compra del mantenedor de productos**, propuesta por Sergio `[49:38]`: «si el producto tiene un precio como costo, un precio de compra, digamos, Que vale 10 pesos, no se puede vender a menos de 10 pesos… eso sí lo podríamos dejar en el mantenedor de productos, asociarle el precio compra». **Nadie mencionó costo promedio.**
   **Ambigüedad no resuelta:** Carlos pregunta `[50:03]` «¿Eso sería estrictamente para todos los casos, hoy nunca existiría la posibilidad de que se venda a menor precio, verdad?» y MJ responde `[50:11]` «No, ahí ya sería merma». Esa respuesta admite **dos lecturas opuestas** y la transcripción no permite decidir:
   - (a) «No [nunca se puede], porque eso ya sería merma» → **regla dura sin excepción**, y la venta bajo costo se canaliza como proceso de merma aparte.
   - (b) «No [no es estricto]; en ese caso sería merma» → **excepción parametrizable** etiquetada como merma.
   Sergio y Carlos rematan con «Perfecto» / «Merma roja» `[50:14]`–`[50:16]`, sin desambiguar. **Esto requiere confirmación del cliente antes de cerrarlo en código.**
10. **Sin descuento/recargo SII a nivel de detalle ni global; el flete es una línea más** (R32/R33). Cabe notar que Sergio formula las tres preguntas y **se contesta él mismo «no»** en `[56:09]`; MJ solo interviene tras la explicación del flete.
11. **Permisos: lectura y escritura, escritura exige lectura.** Carlos `[09:37]`: «El de escritura siempre va a pedir de que se dé el de lectura por obvias razones».
12. **Variación de permisos por empresa se resuelve con un rol por empresa.** Carlos `[11:04]`. Es propuesta del proveedor; el cliente no la rechaza pero MJ agrega el matiz de recorte al asignar (R3).

---

## Decisiones cerradas vs temas abiertos

### Cerradas en la sala (cliente lo afirma y nadie lo rebate)

- Bases separadas cliente/proveedor + lookup unificado por RUT (R11).
- Ficha única con N bancos, N contactos, N direcciones (R14) y registro de cambios (R15).
- Cuenta contable: solo inactivar si tiene movimiento (R12).
- Atributos CC / elemento de costo / área de negocio por cuenta (R13).
- Renombrar «Cotizaciones» de Ventas a **Orden de venta** y mover la pantalla de cotización a **Compras** (R19/R20).
- OV tipo servicio o producto, producto ligado al maestro de bodega (R21/R22/R23).
- Inventario se mueve en la OV; factura conserva cantidad/descripción con precio editable (R25/R26).
- Stock positivo obligatorio, no vender sobre stock (R28/R30).
- Flete como línea adicional; sin impuestos adicionales (R32/R33).
- Cargar datos reales en el ambiente publicado (R37).

### Abiertas al cierre de Reu6

| Tema | Estado literal | Cita |
|---|---|---|
| **Diseño completo de la cadena de aprobación** | Devint entrega propuesta; **el cliente debe entregar el flujo** | Carlos `[18:56]`: «Vamos a generar una propuesta»; Carlos `[21:40]`: «Quedamos pendientes entonces a que nos den la definición bien de cómo podríamos hacer el flujo. Igual, de todas formas, voy a armar una propuesta por mientras»; Sergio `[21:28]`: «La idea es que ustedes definan el flujo» |
| Cruce de líneas jerárquicas (José Tomás → Martín vs → Agustín) | Sin resolver | MJ `[21:06]`: «Igual vamos a tener un problema de cruce de información porque ahí tenéis que poner que José Tomás te puede mandar a ti como gerente, le puede mandar a Martín, igual van a estar cruzadas las líneas de jerarquía»; Agustín `[21:15]`: «hay que revisarlo» |
| Suplencia: mecanismo concreto | Necesidad clara, diseño abierto | Agustín `[18:28]`: «habría que ver varias cosas de cómo pasa el tema de las dependencias cuando no está, hay que solucionar un par de temas ahí» |
| Aprobación de segundo dependiente: ¿opcional u obligatoria? | Abierto | Sergio `[20:03]`: «que sea configurable que si esa persona es opcional u obligatoria la aprobación»; Agustín `[20:11]`: «No, voy a ver, hay que vender un poco esa» |
| **Venta bajo costo: ¿regla dura o excepción por merma?** | **Ambiguo** | Ver Regla 9 |
| Renombrar cuenta: ¿propaga al histórico? | Abierto por decisión del cliente | Agustín `[27:11]`: «Hay que revisar eso» |
| Selector multi-bodega | Devint prepara propuesta | Sergio `[56:09]`: «nosotros le vamos a hacer, preparar una propuesta de cómo sería el tema de selección del producto y seleccionar la bodega y poder sacar desde las bodegas disponibles» |
| SSO Microsoft | **Nota para futuro**, no decisión | Carlos `[05:47]`: «vamos a dejarlo como nota ahí para futuro» |
| Cuáles son los «datos críticos» de los mantenedores | Pedido al cliente, sin respuesta en la sala | Sergio `[34:27]`: «Sería bueno que nos indiquen, por ejemplo, cuáles son los datos críticos por los mantenedores» |
| Credenciales GoSocket | Bloqueante de emisión | Carlos `[57:49]`: «al no tener las credenciales no pudimos realizar en el ambiente de pruebas. Entonces la misión de acá está con errores mientras no tengamos las credenciales»; MJ `[58:20]`: «el lunes tenemos la reunión de credenciales con Pablo» |
| Compras completo, contabilidad, tesorería, inventario | **No se demostraron** por falta de tiempo | Carlos `[58:45]` |

---

## Auditoría de la minuta Reu6

Referencia auditada: [`../reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md).

### Advertencia previa y crítica: hay **dos numeraciones D distintas en circulación**

Las decisiones «D4 / D11 / D16 / D17» que cita `AGENTS.md` **no significan lo mismo** que las D4/D11/D16/D17 de la minuta Reu6. El caso de D4 es directamente incompatible:

| Código | Minuta Reu6 | `AGENTS.md` |
|---|---|---|
| D4 | «Reglas de aprobación… pool de jefes por módulo/monto; **cadena secuencial automática**. Alcance: **Compras OC, Contratistas proformas, Comercial (reservado)**» | «cadena de aprobación **solo Compras (OC)**. Se **eliminó** la cadena de OV» |

Es decir, `AGENTS.md` usa el rótulo «D4» para afirmar **lo contrario** del alcance que fija la minuta que declara canónica. Esto no es un matiz: es un riesgo de trazabilidad de primer orden. Todo el que lea «D4» sin saber cuál de las dos fuentes se cita puede concluir cosas opuestas.

### Auditoría D1–D20

| # | Decisión de la minuta | Veredicto | Sustento / objeción |
|---|---|---|---|
| **D1** | Admin usuarios desde el ERP; multi-empresa por usuario | **RESPALDADA** | Carlos `[06:32]` («dentro de este panel se administrará la creación de los usuarios») + MJ `[11:28]` («cuando tú creas el usuario, elige a las empresas que puedan tener visualización») + Sergio `[06:07]` («la administración de los usuarios va a ser totalmente ustedes»). Cliente confirma |
| **D2** | Super admin ve todo y **puede aprobar cualquier pendiente con advertencia**; rol master no editable | **PARCIAL** | La primera mitad está en Reu6 (Agustín `[09:19]`). La segunda mitad —aprobar por otro con advertencia— **no existe en Reu6**: viene de Reu5 `[01:02:20]`, dicha por **Carlos a Sergio** sin cliente presente, y allí Carlos mismo dijo «Y estará bien eso, hay que consultarlo». «Rol master no editable en permisología» **no aparece en ninguna de las dos transcripciones** |
| **D3** | Permisos por rol, no por empresa; rol por empresa si hace falta | **RESPALDADA (origen proveedor)** | Carlos `[11:04]`. El cliente no la pide ni la rechaza. La minuta **omite el matiz de MJ** `[11:15]`: «igual cuando uno selecciona el rol le puede despinchar cierto acceso» |
| **D4** | Reglas de aprobación: pool por módulo/monto; cadena secuencial automática. **Alcance: OC, proformas y Comercial** | **PARCIAL, con el alcance NO RESPALDADO** | El pool y la cadena están respaldados (`[11:35]`, `[12:28]`). Pero el alcance de **tres módulos, y en particular «Comercial», es afirmación de Carlos** (`[11:35]`: «las órdenes de compra, los contratistas con sus proformas y la parte comercial. Son esos 3 aspectos que hemos considerado») — describe **lo ya construido**, no un pedido. **Ningún cliente pidió jamás aprobación de documentos comerciales en Reu6.** Además la minuta funde en una sola fila dos cosas distintas: el estado del prototipo (pool, 1 firma) y el requisito nuevo de Agustín (cadena). Ver también Reu5 `[04:11:40]`, donde Carlos reporta —de oído— que «como lo dijo la María José… ya actualmente no trabajaban con el sistema de aprobaciones» |
| **D4 según `AGENTS.md`** («solo Compras», cadena OV eliminada) | **NO RESPALDADA POR REU6** | Reu6 no dice esto en ninguna parte. Su origen real es la sesión del 20/08 tarde con Lupe y Mario. El **efecto neto sí es defendible** —el cliente nunca pidió aprobación de OV— pero **la cita está mal atribuida** |
| **D5** | Quitar checkbox «Aprobar con PIN» del rol; PIN ligado a designación en reglas | **PARCIAL — decisión de proveedor, no requisito** | Carlos `[09:37]`: «esta aprobación no corresponde a este menú, debería eliminarse, ya que esto era parte de una implementación antigua». Es una autocorrección de Devint. **Nadie del cliente opina.** Es además el **reverso de Reu5**, donde el PIN por rol se diseñó a pedido de Sergio (`[00:20]`: «en los roles se dejó la opción de aprobar con PIN, ya que dijeron que era por rol el tema de las aprobaciones»). La minuta la presenta como decisión de producto del cliente |
| **D6** | Cadena por montos + línea de mando/organigrama + suplencia vacaciones | **RESPALDADA** (la más sólida de la minuta) | R4–R10. Citas literales de Agustín `[12:28]`, `[13:42]`, `[13:50]`, `[14:52]`, `[16:41]`, `[17:27]` y de MJ `[16:04]`, `[16:48]`. **Objeción menor:** la minuta la lista como decisión cerrada; en la sala quedó como **propuesta pendiente de que el cliente entregue el flujo** (`[21:40]`) |
| **D7** | Bases separadas + consulta RUT unificada (sociedad/proveedor/cliente/productor) | **RESPALDADA (literal)** | MJ `[23:06]`, cita textual completa. Es de las pocas filas que reproduce fielmente el vocabulario del cliente |
| **D8** | Ficha única: bancos (N cuentas/monedas), contactos, direcciones despacho; trazabilidad | **RESPALDADA** | Agustín `[31:51]`, `[33:04]`, `[35:45]`; Sergio `[32:16]`, `[32:51]`; trazabilidad en `[34:52]` y MJ `[34:59]` |
| **D9** | Plan de cuentas: atributos CC/elemento/área según Excel MJ | **RESPALDADA (literal)** | MJ `[25:26]` y `[25:50]` |
| **D10** | Cuenta contable: no eliminar con movimiento; inactivar; revisar rename | **RESPALDADA** | `[26:33]`, `[26:42]`, `[27:23]`, `[27:36]`, `[27:51]`. La minuta acierta al dejar el rename como pendiente |
| **D11** | «Cotizaciones» en Ventas → renombrar/mover a **Orden de venta** | **RESPALDADA** (el enunciado de la minuta) | MJ `[40:09]`, `[40:21]`, `[40:59]`; Agustín `[41:02]`, `[41:46]`. Evidencia muy fuerte |
| **D11 según `AGENTS.md`** («no hay menú ni CRUD de Cotizaciones ni atajo cotiz→OC; redirect a `/compras/ordenes`») | **NO RESPALDADA — extensión posterior** | En Reu6 el cliente pide **reubicar**, no suprimir: MJ `[40:59]` «**Debe estar en el panel de compras**», Carlos `[40:56]` «este debería estar en el panel de compras». La eliminación del CRUD de cotizaciones **no se decide en Reu6**. Es una interpretación añadida más tarde |
| **D12** | OV: tipo producto (catálogo + bodega + stock) o servicio | **RESPALDADA** | Agustín `[42:18]`, `[42:34]`, `[38:25]`; Sergio recapitula en `[53:38]` |
| **D13** | Inventario se mueve en nota/orden de venta; factura con precio editable | **RESPALDADA** | MJ `[44:19]`, `[45:44]`, `[46:58]`, `[47:14]`. La minuta **omite** que Sergio ofreció hacerlo configurable (`[45:02]`) y que MJ optó por fijarlo. También omite que Agustín había dicho lo contrario en `[42:59]` |
| **D14** | Stock ventas solo positivo | **RESPALDADA** | MJ `[55:39]`, `[55:55]`. Pregunta detonada por Sergio `[55:32]` |
| **D15** | Multi-bodega: elegir bodegas y cantidades; no vender sobre stock | **RESPALDADA** | MJ `[54:02]`, `[54:14]`, `[54:48]`; Agustín `[55:27]`; Carlos `[54:54]`. Nota: quedó como propuesta a preparar (`[56:09]`) |
| **D16** | No vender bajo costo **(parametrizable; excepción = merma)**; precio mínimo = costo en mantenedor de producto | **PARCIAL — el paréntesis es interpretación de la minuta** | El requisito base sí está (Agustín `[49:16]`). Pero «parametrizable» **no lo pide nadie**: MJ dice `[49:27]` «no sé si se podrá parametrizar así» —una **duda**, no un pedido— y `[50:00]` «Si se puede, ideal». Y «excepción = merma» descansa entero en la respuesta ambigua `[50:11]` «No, ahí ya sería merma», que admite lectura opuesta (ver Regla 9). **La minuta resolvió una ambigüedad sin marcarla como tal.** Además la base de costo discutida fue el **precio de compra del mantenedor** (Sergio `[49:38]`); la minuta lo dice bien, pero el código usa `costoPromedio`, que nadie nombró |
| **D17** | Recargos/flete → línea adicional, no recargo SII en detalle; sin impuestos adicionales | **RESPALDADA en el flete, PARCIAL en lo global** | Flete como línea adicional: MJ `[57:06]` literal, respaldado. Impuestos adicionales: Agustín `[57:19]` «No, nosotros no», respaldado. **Pero «no descuento/recargo global» lo responde Sergio a sí mismo** (`[56:09]`: «Y a nivel global, descuento, recargo a nivel global, no.»); MJ ni siquiera había entendido la pregunta en ese momento (`[56:45]` «¿a qué te refieres con recargos de intereses?»). Evidencia débil para esa mitad. Contradice además Reu5 `[04:31:00]`, donde **Sergio pidió** «total en los descuentos recargos globales, descuento recargo a nivel de línea» |
| **D18** | Diseño de documentos configurable por cliente con preview | **RESPALDADA (origen proveedor)** | Sergio `[01:01:52]`, Carlos `[01:02:11]`; el cliente solo reacciona: Agustín `[01:02:01]` «Sí, qué buena esa». No es requisito del cliente |
| **D19** | SSO Microsoft (Entra): incorporar; **redirect + Tenant/Client ID de IT Almahue** | **PARCIAL, con detalle INVENTADO POR LA MINUTA** | El interés del cliente existe (`[04:24]`, `[05:52]`) y Sergio dice «sí lo podemos incorporar» `[04:38]`. Pero Carlos lo **degrada explícitamente**: `[05:47]` «vamos a dejarlo como nota ahí para futuro». La minuta lo asciende a decisión numerada. Y **«Entra», «redirect», «Tenant/Client ID», «IT Almahue» y «botón deshabilitado hasta credenciales `.env`» no se pronuncian en ninguna de las dos transcripciones**: son invención de la minuta |
| **D20** | Ambiente publicado con datos de prueba; pueden cargar datos reales en fase piloto | **RESPALDADA** | Carlos `[29:58]`, `[01:00:22]`; MJ `[01:00:14]`, `[01:00:35]`. «Fase piloto» es vocabulario de la minuta, no de la sala |

### Requisitos de la transcripción que la minuta Reu6 **omitió**

| Requisito | Cita | Gravedad |
|---|---|---|
| **R17 — Ficha de solicitud de alta de contraparte** con respaldo de quién la pide | Agustín `[36:13]`, insistido en `[35:45]` y `[36:05]` | **Alta.** Agustín lo repite tres veces y la minuta lo colapsa dentro de D8 (que es solo el mantenedor) |
| **R18 — Prospectos se guardan directamente como clientes** | Agustín `[31:01]` | Media. Es una decisión de modelo de datos que no quedó registrada |
| **R16 / MJ `[34:59]` — clave para reversar o eliminar** en paneles sensibles | MJ `[34:59]`, Agustín `[34:16]` | Media. La minuta lo reduce a «trazabilidad en datos críticos» |
| **R5 — el nivel superior se activa solo al exceder el límite** | Agustín `[13:42]`, corrigiendo a MJ | Media. D6 dice «escalamiento si monto excede facultad» pero no registra que MJ había dicho «siempre» y fue corregida |
| **R9 — dependencia múltiple** (un solicitante con dos jefaturas posibles) | Agustín `[19:44]` | Media |
| Parametrizar **hora de actualización** de indicadores BC + historial | Carlos `[23:36]` | Baja (origen proveedor) |
| Acción pendiente: **el cliente debe indicar cuáles son los «datos críticos»** | Sergio `[34:27]` | Media. No figura en los action items de Almahue |
| **La demo nunca cubrió** compras completo, contabilidad, tesorería ni inventario | Carlos `[58:45]` | Alta como contexto: la minuta lo menciona en «diferidos», pero conviene recordar que **no hay validación de cliente** sobre esos módulos en Reu6 |

---

## Contraste con la minuta IA de Reu5

Se contrastan [`../fuentes/reunion5-minuta-tldv-2026-08-03.md`](../fuentes/reunion5-minuta-tldv-2026-08-03.md) (tl;dv crudo) y [`../reunion5-minuta-2026-08-03.md`](../reunion5-minuta-2026-08-03.md) (canónica).

### Problema estructural

Ambas minutas presentan Reu5 como una lista de **requisitos**. No lo es: es una **conversación interna de Devint**. Ni la minuta tl;dv ni la canónica advierten en su cuerpo que **no había cliente en la sala**. La canónica sí lista correctamente «Participantes: Carlos (Devint), Sergio (Devint)», pero luego presenta los ítems como pedidos a cumplir con estado Hecho/Diferido, lo que en la práctica los convirtió en requisitos de proyecto.

### Errores concretos de la minuta tl;dv

| Ítem tl;dv | Qué dice la transcripción | Veredicto |
|---|---|---|
| «Configuración contable SAI **necesaria** para implementar GoSocket 37:20» | Carlos `[06:10:51]`: «esto ya fue **fantasmeo de la IA**. Que me dijo que según lo que necesitamos para implementar GoSocket había que tener una configuración contable del SAI… Como todavía no tenemos la documentación de GoSocket, **es puro fantaseo del aire**» | **INVERSIÓN TOTAL DE SENTIDO.** La transcripción dice que es una alucinación a descartar; la minuta lo registra como requisito |
| «Cotización convertible a **nota de crédito** o factura 29:03» | Carlos `[04:47:31]`: «se puede convertir a **nota** o convertir a factura» — en el contexto, nota de venta | **INVENTADO.** «Nota de crédito» no se dice; el salto semántico es grave en un contexto tributario |
| «**Sergio** implementar / agregar / hacer…» (16 de 18 action items) | Carlos es quien implementa; Sergio pide | Error de atribución. **El propio archivo tl;dv lo advierte en su encabezado**, y la minuta canónica lo corrige. Bien resuelto |
| «Descuentos y recargos aplicables a nivel global y de línea 27:26» | Correcto para Reu5 (Sergio `[04:31:00]`) | Correcto, pero **contradicho tres días después** por el cliente en Reu6 (D17). Reu6 gana: es posterior y es cliente |
| «Múltiples períodos pueden estar activos simultáneamente 34:24» | Sergio `[05:44:00]` lo pregunta y luego concluye `[05:53:51]` «por eso yo lo sacaría» | Registra la pregunta como si fuera una característica confirmada |
| Timestamps | Los de tl;dv son los correctos; los del archivo de transcripción están ×10 | El desfase no está señalado en ninguna minuta |

### Errores/riesgos de la minuta canónica de Reu5

| Fila | Objeción |
|---|---|
| «Ventas sin CC — **Hecho**» | En la transcripción esto es **una disputa sin resolver**. Sergio `[04:40:51]`: «la Ventas no van con centro de costo». Pero Carlos `[03:29:00]` recuerda lo contrario: «Ah, pero centro de costo igual **ella dijo que iba**», y `[03:30:40]`: «voy a preguntarle por interno porque tengo la duda y creo que ahí en esa parte de la reunión **se me cayó un poquitito la internet**». Sergio mismo admite `[03:32:20]`: «no sé si en la venta… **la cuenta mayor sí sé, pero por ejemplo centro no lo sé**». Cerrar esto como «Hecho» **cierra sobre la opinión de un proveedor que declaró no saber**, contra el recuerdo de lo que dijo MJ |
| «Cotiz→NP→Factura UI — **Hecho** (pestaña NP + convert conserva campos)» | Contradice frontalmente a `AGENTS.md`, que ordena «No restaurar cotiz→NP→factura». Dos documentos vigentes dicen lo opuesto |
| «CC por ítem OC — Hecho» | Correctamente respaldado: Carlos consulta y Sergio responde «Sí, es por ítem» `[01:10:50]`. Pero sigue siendo **decisión de proveedor**; el origen atribuido («hoy día viendo el vídeo, me surgió la duda si hacían referencia de que por ítem tendría que ir el centro de costo») es una inferencia de Carlos sobre una reunión previa |
| «Correo al cambiar PIN — Diferido / Password al cambiar PIN — Hecho» | Bien capturado. Es propuesta de Sergio `[39:01]`: «Al poner cambiar PIN, que te ingrese la clave de la cuenta» |
| Ausencia de advertencia | Ninguna de las dos minutas dice «Reu5 no tiene requisitos de cliente». Debería ser la primera línea |

---

## Señales para QA

### Casos que **deberían ejercerse** (hay requisito de cliente explícito y verificable)

| Caso | Fundamento | Nota de implementación observada |
|---|---|---|
| OV: no vender por sobre stock disponible | R30, `[55:27]` | Regla dura; ejercer |
| OV: stock negativo bloqueado | R28, `[55:39]` | Ejercer; no hay excepción pedida |
| OV: partir un producto entre varias bodegas | R29, `[54:48]` + «Sí se puede» de Carlos | El DTO de línea de OV tiene **un solo `bodegaId`**. El reparto solo es posible **por líneas separadas**. Ejercer explícitamente ese escenario y anotar si satisface el pedido |
| OV → factura: cantidad y descripción se conservan, precio editable, producto no editable | R26/R27, `[46:58]`, `[47:06]`, `[47:14]` | Ejercer los tres asertos por separado |
| Inventario se mueve con la OV, no con la factura | R25, `[45:44]` | Ejercer; hay una afirmación contraria de Agustín `[42:59]` que quedó sobrescrita por MJ |
| Cuenta contable con movimiento: DELETE → 409, inactivar sí | R12, `[27:36]` | Ejercer |
| Periodo: historial de quién abre/cierra + motivo obligatorio al reabrir | Reu5 Sergio `[05:53:51]` | Existe `PeriodoContableEvento` en el schema. Ejercer. **Origen proveedor**, pero es control de auditoría razonable |
| Ficha contraparte: N cuentas bancarias en distintas monedas, N contactos, N direcciones | R14, `[31:51]`, `[33:04]` | Existen `Cliente/ProveedorCuentaBancaria`, `…Contacto`, `…Direccion`. **No debe quedar SKIP** |
| Ficha: registro de cambios en datos sensibles | R15, `[34:52]` | Existen `ClienteCambio` y `ProveedorCambio`. Ejercer con un cambio de cuenta bancaria y de razón social |
| Cadena de aprobación: escalamiento **solo al exceder** el monto | R5, `[13:42]` | Verificar que el nivel superior **no** participe cuando el inferior alcanza |
| Cadena: el solicitante no elige aprobador; sale por jefatura | R6/R7, `[13:50]`, `[16:04]` | `Usuario.jefeId` existe en el schema y `approval-engine` lo usa (`byId.get(solicitanteId)?.jefeId`). Ejercer el caso negativo: Fran no puede enviar a Mario |
| Cadena: doble check del jefe directo aunque no alcance el monto | R10, `[17:27]` | Ejercer |
| Flete como línea adicional en OV/DTE | R32, `[57:06]` | Ejercer |
| Prospecto guardado directamente como cliente | R18, `[31:01]` | Existe `ProspectosPage` y modelo `prospecto`. Verificar el paso a cliente |

### Casos que **legítimamente pueden seguir SKIP/BLOCKED**

| Caso | Por qué |
|---|---|
| Aprobación de documentos **comerciales / cadena de OV** | **Ningún cliente la pidió jamás en Reu6.** La única mención (`[11:35]`) es Carlos describiendo el prototipo. El cierre de `AGENTS.md` es correcto en el fondo aunque cite mal la fuente. Mantener SKIP, y corregir la referencia: no viene de «D4 Reu6» |
| SSO Microsoft | Carlos lo degrada a nota para futuro (`[05:47]`). No es requisito duro. BLOCKED aceptable |
| Emisión DTE real contra SII | Bloqueada por credenciales GoSocket ya en Reu6 (`[57:49]`). BLOCKED legítimo |
| Import de cartola por file picker (`TES-CARTOLA-IMP`) | Reu5 `[06:48:10]`: «Esto todavía no lo he tocado. Esto está pendiente». No hay requisito de cliente en Reu5/Reu6 sobre cartolas. SKIP sin riesgo desde estas fuentes |
| Descuento/recargo **global** en el documento | El cliente dijo que no lo necesita (D17), así que **no es un requisito a probar**. El DTO de OV tiene `descuentoGlobalPct`; es capacidad extra, no un fallo |
| Impuestos adicionales | Agustín `[57:19]` «No, nosotros no». Fuera de alcance |
| Traspaso de gastos «próxima temporada» | Agustín se autodescartó: `[29:04]` «Pero no, está perfecto, no hay que hacer nada». Diferir sin culpa |

### Casos que **NO deben marcarse pass/fail** hasta confirmar con el cliente

| Caso | Ambigüedad |
|---|---|
| **Venta bajo costo** | Sin resolver si es regla dura o excepción por merma (Regla 9). Además, la base de costo discutida fue el **precio de compra del mantenedor** (Sergio `[49:38]`), mientras el código valida contra `costoPromedio` (`comercial.service.ts`: «No se puede vender … bajo costo»). **Nadie mencionó costo promedio en ninguna de las dos reuniones.** Un test que hoy pase puede estar validando una regla distinta a la pedida |
| Renombrar cuenta contable: ¿propaga al histórico? | Abierto por decisión de Agustín `[27:11]` |
| Existencia de menú/CRUD de Cotizaciones | El cliente pidió **moverlo a Compras**, no eliminarlo (`[40:59]`). Un test que verifique «no existe cotizaciones» está validando una interpretación posterior, no Reu6 |
| Ventas con o sin centro de costo | Disputa no resuelta en Reu5 entre Sergio y el recuerdo de Carlos sobre lo dicho por MJ. **No cerrado por cliente en ninguna transcripción** |

### Huecos funcionales detectados (requisito de cliente sin implementación aparente)

| Hueco | Requisito | Evidencia en código |
|---|---|---|
| **Ficha de solicitud de alta de contraparte** con respaldo del solicitante | R17, `[36:13]` | Sin coincidencias para `solicitudAlta` / flujo de alta en `erp_back/src`. **No implementado** |
| Clave/PIN para **reversar o eliminar** en mantenedores sensibles | R16 + MJ `[34:59]` | Sin coincidencias de `requierePin` / `verifyPin` fuera del dominio de aprobaciones. **Aparentemente no implementado** |
| Dependencia **múltiple** de jefaturas | R9, `[19:44]` | `Usuario.jefeId` es un único FK opcional. **Solo soporta una jefatura** |
| Hora parametrizable de sincronización de indicadores BC + historial de valores | Carlos `[23:36]` | `bc-sync.cron.ts` usa cron fijo `*/5 * * * *`; no hay parámetro de hora. **No implementado** (origen proveedor, prioridad baja) |
