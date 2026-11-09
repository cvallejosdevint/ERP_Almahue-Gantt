# Propuestas de nómina - 23 y 24/09/2026

Fuente de las tres propuestas: transcripción del 23/09 (Mario y Lupe) y recorrido del 24/09 (Lupe, Fran y Sigrid). No cierran formato de pantalla más allá de lo que Lupe describió. No están implementadas.

El HTML de antes y después queda para cuando se pida. El modelo es `docs/sesiones/parametrizacion-ajustes-2026-09-24/comparacion.html`.

## Qué hay hoy

En Nómina semanal el combo es año, mes y semana. Pendientes y Todos filtran dentro de esa semana. Se puede mirar semanas futuras y exportar la semana elegida. El estado Crítico aparece si el atraso pasa de 90 días, fijo en código (`aging-sync.util.ts`). No hay mantenedor de plazos ni plazo distinto por proveedor.

## P1 - Ver pendientes de todas las semanas

Lupe, 23/09 `[51:35]` y `[51:38]`: sí. Revisa hacia adelante y trabaja por semana. Si esta semana queda algo de agosto, tiene que verlo. Pidió una vista de pendientes de todos los periodos, aparte de los filtros de la semana (`[51:43]`, `[52:01]`). La semana funciona como un hasta (`[52:06]`). El desde-hasta le sirve también para exportar (`[52:11]`).

Antes: el filtro Pendientes solo muestra la semana elegida del periodo del encabezado.

Después, propuesto:

- Una entrada aparte, en la misma nómina: pendientes de todos los periodos, hasta la semana en curso.
- Un desde-hasta opcional, para acotar y para el export de esa selección.
- No mezcla empresas. Lupe lo dijo el `[56:25]`: trabajando por empresa, mira una por una.

No pisa el aplazar ni el título de la tarjeta del 28/08. Agrega una vista.

## P2 - Cómo se ve esa ayuda

Lupe, `[54:38]` y `[55:38]`: arriba, una ayuda memoria de lo pendiente hacia atrás, de esta semana y de la siguiente. En su Excel filtra año, semana y fecha de pago, desfiltra y ve todas las semanas con información, marca la semana en curso (en el ejemplo, la 39) y lo que viene después. Al entrar a una semana ve qué hay que pagar. Totales por moneda. Sergio ofreció un calendario tipo Google (`[57:03]`) y dejó el dibujo como propuesta (`[57:24]`), porque muchas semanas en una tabla pueden no ser cómodas. Lupe no eligió el dibujo. Sí cerró la lógica.

Antes: no hay franja de semanas. Hay que cambiar el combo para ver otra.

Después, propuesto:

- Franja sobre la grilla. Cada celda es una semana con número de pendientes.
- Tres marcas fijas: semana anterior, semana en curso, semana siguiente.
- El resto se recorre (semanas con datos hacia atrás y hacia adelante), sin exigir ver el año entero de una vez.
- Clic en una celda abre esa semana, la misma grilla de hoy.
- Al lado, total de la semana en cada moneda. Sin columna de otra empresa.

El calendario completo no entra en esta propuesta. Si más adelante lo piden, reemplaza la franja, no la lógica.

## P3 - Aviso de crítico, días configurables

Lupe, `[58:43]` y `[58:55]`: sí al aviso extra, con otro color. Los días de crítico pueden cambiar, y pueden ser distintos según el proveedor. Quedó un mantenedor en tesorería, dentro de la nómina, con plazos y filtros rápidos, por ejemplo 30 y 90 (`[59:28]` a `[59:54]`). No se habló de apagar Atrasada y Crítico al pagar.

Antes: Crítico si el atraso es mayor a 90, igual para todos. En la reunión se mostró como si partiera a los 30. El código no tiene ese 30.

Después, propuesto:

- Mantenedor en Tesorería, arriba en Nómina semanal, no en Parametrización.
- Un plazo general de crítico, en días. Mientras no lo configuren, el valor inicial es 30, que es el que se conversó, no el 90 del código.
- Si un proveedor tiene su propio número, ese manda solo para sus documentos. Si no, vale el general.
- La fila crítica usa otro color, distinto de atrasada.
- Filtros rápidos para los umbrales que dejen cargados (el ejemplo de la sala fue 30 y 90).
- Al pagar, esta propuesta no cambia el estado. Eso no se acordó.

## Ramas carlos-dev y billing-gateway

Nada de P1, P2 ni P3 está escrito en código, así que no hay un commit pendiente de estas propuestas.

| Repo | Rama | Frente a origin | Qué hay sin commit |
|---|---|---|---|
| erp_back | carlos-dev | al día | `admin.service.spec.ts` solo cambia fin de línea. `scripts/seed-contratistas-datos-locales.mjs` está sin seguimiento: es semilla local, no va en este hilo. |
| erp_front | carlos-dev | al día | limpio |
| billing-gateway | master | al día | no existe rama carlos-dev. En `scripts/` hay tres archivos `qa-tmp-*.mjs` sin seguimiento. Son de inspección, no de estas propuestas. |

## Fuentes adjuntas - no implementar

No llegó un archivo aparte de GoSocket en este mensaje. GoSocket aparece dentro del diagrama de Mario: la factura puede entrar por ahí, y el reclamo vuelve a GoSocket.

### Mario - Compras_Almahue_Flujo.pptx (v1.2, septiembre 2026)

WhatsApp del 29/09: al crear la OC se elige tipo de compra (servicios, insumos, activo fijo). Las OC hijas, hoy, solo en insumos. En activo fijo y en servicios no hay recepción parcial.

El deck dice, en la portada, «asientos por definir». La diapositiva de registro contable y paso a pago está marcada pendiente.

Lo que sí toca tesorería, y queda anotado sin construir:

- Cada factura validada genera dos líneas por pagar: NETO (fecha de factura más los días de pago) e IVA (día 10 del mes siguiente). OC exenta: solo NETO.
- Esas líneas son lo que la nómina debería comprometer. Hoy la nómina trata el documento como una sola fecha de vencimiento.
- Tesorería es quien marca la línea como pagada.
- Recepción con factura no pasa por «facturas por recibir». Recepción con guía sí deja la factura pendiente.
- El tipo de cambio del registro de la factura (CLP, USD, yuan, y un TC generado para que la moneda de la OC cuadre) está descrito. La diapositiva 7 dice que por ahora no se valida el tipo de cambio. No cierra la tarjeta de triple moneda: los asientos siguen por definir.

Compras (OC hija, aprobación, alertas) no se detalla aquí. No es tesorería.

### Lupe - asiento de compra y asiento de tesorería

Sergio se lo pidió por Teams. Lupe respondió con una planilla. Los montos cierran: 1.906.962 + 362.324 = 2.269.286.

1. Nota «Ingreso OC». Debe Gasto combustible 1.906.962. Haber Facturas por recibir 1.906.962.
2. Nota «Ingreso factura». Debe Facturas por recibir 1.906.962. Debe IVA crédito 362.324. Haber Proveedor 2.269.286.
3. Nota «Pago de factura». En la captura se leen Banco y Anticipo proveedor, por 2.269.286. Es el asiento de tesorería que pidió Sergio.

Ese tercer asiento sí afecta tesorería. Hoy el pago no genera un asiento `PAGO`. El asiento de banco es el de la cartola (`CARTOLA`). La muestra de Lupe mueve banco contra anticipo proveedor al pagar la factura. Mario, en el mismo deck, deja los asientos por definir. No se cambia código con esta captura. Hay que confirmar con Lupe el debe y el haber de esa tercera nota antes de tratarla como regla: la imagen es chica y el lado de cada cuenta no se lee con la misma claridad que las dos primeras.

## Hecho el 29/09

P1, P2 y P3 quedaron en la nómina (back y front). Comparación: [nomina-antes-despues-2026-09-29/comparacion.html](nomina-antes-despues-2026-09-29/comparacion.html). Las dos líneas NETO/IVA de Mario y el tercer asiento de Lupe siguen sin implementarse.
