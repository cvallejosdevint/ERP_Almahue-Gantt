# Auditoria: lo que el sistema tiene y lo que el cliente pidio

Corte: 05/11/2026, despues de transcribir la reunion de hoy.  
Las tres semanas (21/10 a 05/11) estan en la matriz, con las dos grabaciones del 26, las dos del 27 y la unica del 28. El 21/10 y el 22/10 tambien entran. El clip del 30/10 no es reunion.  
No es un plan de implementacion. Dice que ya esta en el codigo local y que la sala pidio y todavia no esta.

La sala de hoy miro un servidor que no traia los cambios de esta semana. Carlos lo dijo al mostrar ordenes de aplicacion y recetas como maqueta `[01:20:31]`. En local esas pantallas ya tienen API. Abajo se separa "esta en local" de "la sala lo vio viejo".

## Esta en local y la sala no lo piso

| Pedido | Donde quedo |
|---|---|
| ER solo del mes. ESF con resultado del ejercicio y acumulado | Contabilidad > Estados financieros. Cuentas puente en Admin > Empresas |
| Balance 8 desde el 1 de enero hasta el periodo | Contabilidad > Balance 8 |
| Asiento contabilizado no se edita en montos, cuentas ni glosa. Queda quien y cuando | Contabilidad > Asientos |
| OC: cuenta, despues centro y elemento. Sin cuenta, esos campos no se eligen | Compras > Nueva OC |
| Notas de cobro de embarcador y Asoex, una a una, sin carga Excel | Compras > Notas de cobro |
| Cartola semanal sin repetir el mismo movimiento. Aviso si el archivo no es del mes. Ingreso partido en 2 o 3 codigos. Nombre de la cuenta | Tesoreria |
| Devolucion valorizada al precio de la guia o factura, no al promedio | Insumos. El 05/11 precisa que esa guia no pierde stock: falta esa mitad |
| Periodo contable cerrado no se reabre. La correccion de la proforma abre motivo y dos vistos buenos, no la clave al tiro | Contabilidad > Periodos y Contratistas > Proformas |
| Proformas del mes, no las del mes anterior, en la grilla | Contratistas > Proformas |
| Tipo de OC activo fijo existe como dato | Compras. Falta el alta del maestro recien con la OC recepcionada |
| Grupos y escalas siguen siendo el motor. El organigrama es un arbol | Admin > Aprobaciones y Admin > Organigrama. La sala de hoy lo confirmo |
| Packing como ficha, receta, produccion y consumo en el cierre de bodega | Insumos. La sala lo vio como dibujo. El diseno de "una receta, un packing" quedo pisado hoy |
| Usuarios con rol de administrador del modulo pueden entrar a un grupo, y se puede agregar un nivel despues del ultimo | Corregido en local. En la demo del servidor no estaba `[57:59]`, `[58:39]` |

Migraciones de esta semana (`20261105180000`, `20261105190000`, `20261105200000`) estan aplicadas en la base local. Produccion no queda acreditada en este corte.

## Lo pidio el cliente y falta

### Cambia lo que ya esta construido

| Pedido (05/11, MJ o Fran) | Que hace hoy el local | Que falta |
|---|---|---|
| La correccion de la proforma edita la linea. No nace un asiento de ajuste ni uno de reversa. El mayor muestra solo activos | Hay solicitud, dos vistos buenos y protocolo. El asiento de ajuste sigue en el discurso del 03/11 | Editar la linea del asiento existente. Sacar el asiento nuevo de esa correccion. Filtrar anulados del libro mayor |
| Anular un asiento: la fila queda, con motivo. Lo hace la jefatura, o un analista lo solicita y la jefatura aprueba. No es una cadena por monto | Contabilizado no se edita. No hay anulacion con solicitud a la jefatura | Estado anulado, motivo, permiso de jefatura, y que el mayor lo omita |
| Receta de embalaje. En el consumo, cantidad por cada packing. Centro de costo en la receta | Receta y produccion piden un packing | Soltar el packing obligatorio de la receta. Repartir el consumo. Guardar el centro en la receta y filtrar por el |
| Ultimo aprobador con tope. Si la OC lo supera, no entra a la cadena y se avisa | La cadena cierra en el ultimo nodo. Un monto por encima puede seguir o quedar sin techo | Tope obligatorio del ultimo eslabon y bloqueo con mensaje antes de encolar |
| Tope por CLP, USD y yuan. Al tipear pesos, proponer el tipo de cambio del dia y dejar editarlo. No recalcular despues | Un monto en la escala | Tres montos por eslabon, propuesta del dia, valor guardado |
| Activo fijo solo si la OC de ese tipo esta recepcionada. Aviso si no tiene factura. Estados recepcionado y facturado | Existe el tipo en la OC. El maestro no sale de esa OC recepcionada | Selector de OC recepcionadas, alta del maestro ahi, vinculo en el libro de compras |
| Devolucion: precio de la guia, documento nuevo, sin rebajar esa guia. Consumo a precio promedio del stock, sin FIFO | La salida por devolucion toma el precio de la factura o de la entrada. El consumo de receta usa el costo de bodega | No descontar la existencia de la guia origen. No ofrecer "de la mas antigua a la mas nueva" |
| Stock de la guia al confirmar la recepcion, no al registrarla. Adjunto (foto) en la guia | La guia 52 exige bodega de packing. El calce por articulo esta pedido desde el 03/11 | Confirmar antes de sumar stock. Adjuntar respaldo |
| Sacar administradores por modulo de la operacion. El acceso queda en el rol | Sigue el mantenedor de administradores por modulo | Ocultarlo o dejarlo fuera del flujo. No darle poder de cadena |

### Pedido antes y todavia abierto

| Pedido | Dia | Nota |
|---|---|---|
| Excel de recetas y una orden de aplicacion real para copiar los campos | 05/11, y el manual quedo a la espera del archivo | Lo tiene que mandar el cliente. La orden de aplicacion de hoy pide ademas varias lineas, unidad y elemento de costo |
| Cuentas que faltan en el cierre de bodega | 05/11 `[02:16:45]` | Mandan el listado. La palabra merma no se implementa: no es concepto del negocio |
| Contabilizado de hijas de punta a punta (guia > hija > factura > asiento > madre) | 03/11 | Hay codigo de madre. Falta el recorrido completo, no un check de memoria |
| Libro de compras: cobertura contra la proforma, vista por proveedor, etiqueta contabilizada o pendiente, aviso verde al calzar y aviso al creador si descuadra | 03/11 | El boton Contabilizar ya se esconde si no hay OC ni proforma. Falta el resto de esa vista |
| Correo al asociar proforma y factura | 03/11 | El envio SMTP del PIN sigue fuera. El aviso interno no reemplaza el correo |
| Proyectado de tesoreria con Lupe | 28/10, retomado el 05/11 | Reunion el lunes. No esta el modulo |
| Reportes que pide cada jefatura | 05/11 | Cuando el modulo este cerrado, no antes |
| CAF y emision en GoSocket productivo | 05/11 `[02:27:09]` | Se acabaron los CAF. Fuera de este corte. Hablar con Pablo |
| Boleta de honorarios (registro, no emision) | 27/10 | No se cerro en este corte |
| PDF de OC al proveedor sin dimensiones contables | 26/10 | No reabierto hoy. Sigue como deuda si el PDF actual las muestra |
| Cuenta con N centros, N elementos y N areas, y contador de cuentas en el mantenedor | 26/10 | No auditado de nuevo hoy |
| Cadena OC armada desde el organigrama | hipotesis de demo | La sala la rechazo dos veces (03/11 y 05/11). No se hace |
| Packing externo de cajas y pallets COMEX | diferido | Sigue fuera |
| AlmaWeb: numeros y permisos del portal | 03/11 | Otro sistema |

## Lo que no hay que rehacer

- Aprobacion solo en la OC de compras. La orden de venta se confirma al guardar.
- Cotizacion solo como referencia dentro de la OC.
- No vender bajo el precio de compra del maestro.
- Cartola que no duplica al recargarla en el mes.
- Grupos por area, con gerencia repetida en cada uno. El organigrama no los reemplaza.
- Precio de devolucion distinto del precio promedio de consumo.

## Recorrido de lo ya aplicado

Las pantallas tocadas desde el 27/10 hasta el 04/11 (organigrama, packings, orden de aplicacion, asientos, balance, resultado, situacion financiera, notas de cobro, cierre de bodega) estan en un solo antes / despues:

- [`docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/comparacion.html`](../sesiones/revision-semana-2026-10-27-a-2026-11-05/comparacion.html)
- [`docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html`](../sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html)

Esas fotos son el sistema en modo demo, periodo 2026-08, a 1536x960. No incluyen lo pedido hoy en la seccion "cambia lo que ya esta construido": eso todavia no esta en pantalla.
