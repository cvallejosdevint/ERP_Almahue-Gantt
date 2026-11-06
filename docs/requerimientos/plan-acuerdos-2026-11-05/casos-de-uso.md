# Casos de uso: acuerdos 21/10 a 05/11

Corte: 05/11/2026. Este paquete es la planificacion antes de codear. No implementa, no describe pantallas y no reemplaza el contraste con el codigo.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`. El corte de codigo es local, no produccion.

Fuente: las transcripciones. La matriz y la auditoria del 05/11 ubican el acuerdo y dicen que ya esta en local. Si chocan con la transcripcion, gana la transcripcion. Carlos y Sergio son hipotesis hasta que el cliente confirma. Si la voz no trae nombre, se dice locutor no rotulado y se usa la pista de la sala.

Pisos que se conservan. No hay un caso para construirlos de nuevo. Si un acuerdo los toca, el caso lo dice:

- La aprobacion con cadena es solo de la OC de compras. La orden de venta se confirma al guardar, sin cadena.
- La cotizacion es solo una referencia dentro de la OC. No hay cotizacion > OC.
- No se vende bajo el precio de compra del maestro.
- Merma no existe. El 05/11 la palabra salio al pedir cuentas de cierre. No hay caso de merma.
- El organigrama no es el motor de la cadena. Grupos y escalas si.

## Leyenda de estados

| Estado | Que significa |
|---|---|
| Completo | La regla vigente ya esta en codigo local. Regresion. No construir de nuevo. |
| Parcial | Una parte esta y otra no. Si hubo duda entre Completo y Parcial, quedo Parcial. |
| Faltante | No esta. |
| Pisado | Un dia posterior cambio la regla. No se construye la version vieja. |
| Espera | Falta archivo, listado o reunion. No se codea el hueco. |
| Fuera | Otro sistema, o emision que este corte no construye. |
| No hacer | La sala lo rechazo. |

## 1. Indice

Una fila por acuerdo de la matriz. CU-46, CU-64 y CU-65 no son fila propia: se citan desde la fila mas cercana. CU-66 no es acuerdo de la matriz y no tiene fila. Su abanico es CU-66.1 a CU-66.3. La columna Escenarios es el rango de cada caso citado.

| Dia | Acuerdo | Estado del acuerdo | Casos | Escenarios | Dia que lo pisa o precisa |
|---|---|---|---|---|---|
| 21/10 | Guia tipeada a mano mientras abastecimiento siga en Acepta, con archivos o Excel de Acepta | Parcial | CU-01 | CU-01.1 a CU-01.4 | 05/11 precisa (foto al confirmar) |
| 21/10 | Hijas sin saldo: nacen en la recepcion, mueren al facturar, 100% calzadas. Solo la madre puede tener saldo | Parcial | CU-02 | CU-02.1 a CU-02.4 | 03/11 precisa (ultima guia ajusta la madre) |
| 21/10 | Las hijas no se contabilizan en la orden. Asiento en el cierre de bodega | Parcial | CU-03, CU-65 | CU-03.1 a CU-03.4; CU-65.1 a CU-65.3 | - |
| 21/10 | Activo fijo entra directo al modulo y no nace de una OC | Pisado | CU-04 | CU-04.1 a CU-04.3 | 27/10 y 05/11 pisan el origen. Siguen vida util, sin centro de costo e IPC |
| 21/10 | Al cierre de contratistas entran solo proformas aprobadas y con factura. Cuenta de mano de obra y glosa | Parcial | CU-05 | CU-05.1 a CU-05.5 | 26/10 y 03/11 precisan |
| 22/10 | Asiento: ver glosa, editar comentario, anular, reversar, PDF, filtro de activos | Parcial | CU-06 | CU-06.1 a CU-06.6 | 05/11 precisa anular y el mayor |
| 22/10 | Factor de honorarios en parametrizacion. IPC actualizable | Faltante | CU-07 | CU-07.1 a CU-07.4 | - |
| 22/10 | Presupuesto por centro de costo, ejecucion anual, PDF | Faltante | CU-08 | CU-08.1 a CU-08.4 | - |
| 22/10 | Libros con filtro de fechas. El balance no cruza de un ano a otro | Parcial | CU-09 | CU-09.1 a CU-09.4 | 26/10 precisa ER, ESF y balance |
| 22/10 | Cartola: moneda y banco, ver en pesos, PDF, adjunto en el pago, contabilizar, semana | Parcial | CU-10 | CU-10.1 a CU-10.6 | 28/10 precisa la carga |
| 22/10 | Estado de cuenta por RUT a Excel, cliente, proveedor y productor | Faltante | CU-11 | CU-11.1 a CU-11.6 | - |
| 22/10 | Una ficha que una cliente, proveedor y productor, con listas separadas | Parcial | CU-12 | CU-12.1 a CU-12.4 | - |
| 26/10 | ER de un mes muestra solo ese mes. El 31/12 el resultado pasa a acumulado | Completo | CU-13 | CU-13.1 a CU-13.4 | - |
| 26/10 | Carga masiva: si falta un obligatorio se rechaza esa linea y hay reporte | Parcial | CU-14 | CU-14.1 a CU-14.4 | - |
| 26/10 | Cuenta con N centros, N elementos y N areas. El elemento no se amarra al centro | Parcial | CU-15 | CU-15.1 a CU-15.5 | - |
| 26/10 | OC: primero cuenta, despues centro, despues elemento. Una linea, un centro | Completo | CU-16 | CU-16.1 a CU-16.4 | - |
| 26/10 | PDF al proveedor sin dimensiones contables | Parcial | CU-17 | CU-17.1 a CU-17.4 | - |
| 26/10 | Cartola: Lupe baja el archivo del banco | Completo | CU-18 | CU-18.1 a CU-18.3 | 28/10 precisa la carga |
| 26/10 | La actividad manda. La aprobacion va en la proforma, no en cada ingreso diario | Parcial | CU-19 | CU-19.1 a CU-19.5 | - |
| 26/10 | Al cierre entra el bloque de proformas aprobadas. Borrador e ingresos sueltos quedan informativos | Parcial | CU-20 | CU-20.1 a CU-20.4 | 03/11 precisa factura del mes siguiente |
| 26/10 | Un asiento de centralizacion. En libro de compras la factura cancela el puente | Parcial | CU-21 | CU-21.1 a CU-21.5 | 27/10 precisa agrupacion y auxiliar |
| 26/10 | La solicitud de reverso sale del documento. No se reabre el mes para corregir | Parcial | CU-22 | CU-22.1 a CU-22.5 | 03/11 precisa. 05/11 pisa el asiento nuevo |
| 26/10 | Planta fuera. Historial de parametrizacion antes / despues, sin metadatos | Parcial | CU-23 | CU-23.1 a CU-23.4 | - |
| 27/10 | Reversa en mes abierto y ajuste en mes cerrado, con dos vistos buenos | Pisado | CU-24 | CU-24.1 a CU-24.3 | 05/11 pisa el asiento de ajuste |
| 27/10 | Jose Tomas arma y aprueba la proforma. Contabilidad calza monto y RUT | Parcial | CU-25 | CU-25.1 a CU-25.5 | - |
| 27/10 | El asiento de cierre agrupa el gasto por centro de costo. Facturas por recibir lleva auxiliar | Faltante | CU-26 | CU-26.1 a CU-26.4 | - |
| 27/10 | Balance de 8 columnas | Completo | CU-27 | CU-27.1 a CU-27.3 | - |
| 27/10 | Notas de cobro, embarcador y Asoex | Parcial | CU-28 | CU-28.1 a CU-28.5 | - |
| 27/10 | La OC puede ser de activo fijo | Parcial | CU-29 | CU-29.1 a CU-29.3 | 05/11 precisa: el maestro nace con la OC recepcionada |
| 27/10 | Boleta de honorarios: registro y recepcion, no emision | Faltante | CU-30 | CU-30.1 a CU-30.4 | - |
| 28/10 | La cartola del mes se carga varias veces y no duplica movimientos | Completo | CU-31 | CU-31.1 a CU-31.3 | - |
| 28/10 | Excluir la linea del mes anterior y avisar si el archivo no es del periodo | Completo | CU-32 | CU-32.1 a CU-32.3 | - |
| 28/10 | Partir un ingreso en 2 o 3 codigos financieros, en la moneda de origen | Completo | CU-33 | CU-33.1 a CU-33.4 | - |
| 28/10 | Nombre de la cuenta junto al numero | Completo | CU-34 | CU-34.1 a CU-34.3 | - |
| 28/10 | Devolucion al precio de la guia o factura, no al promedio | Parcial | CU-35 | CU-35.1 a CU-35.4 | 05/11 precisa que esa guia no pierde stock |
| 28/10 | Proyectado de tesoreria | Espera | CU-36 | CU-36.1 a CU-36.4 | 05/11 retoma, sin disenar |
| 03/11 | No reabrir el periodo desde Traspaso. La correccion sale de la proforma | Completo | CU-37 | CU-37.1 a CU-37.3 | - |
| 03/11 | Periodo abierto: motivo y dos vistos buenos. Periodo cerrado: no ofrecer la clave directa | Completo | CU-38 | CU-38.1 a CU-38.4 | 05/11 precisa que el resultado no es un asiento nuevo |
| 03/11 | Asiento de ajuste al cerrar la reversa | Pisado | CU-39 | CU-39.1 a CU-39.3 | 05/11 pisa |
| 03/11 | Grilla de proformas solo del periodo. Recuadro de factura solo si hay vinculo | Parcial | CU-40 | CU-40.1 a CU-40.4 | - |
| 03/11 | Factura de proforma 1 a 1. Aviso al calzar y aviso al creador si descuadra | Parcial | CU-41 | CU-41.1 a CU-41.6 | 05/11 precisa cobertura parcial |
| 03/11 | Libro de compras contra facturas por recibir. No mostrar Contabilizar si no hay OC ni proforma | Parcial | CU-42 | CU-42.1 a CU-42.4 | - |
| 03/11 | Hijas de insumos por guia. Solo la ultima guia ajusta la madre | Parcial | CU-43 | CU-43.1 a CU-43.5 | 05/11 precisa cobertura por cantidad |
| 03/11 | Quien tiene acceso al modulo puede entrar al grupo de aprobacion | Completo | CU-44 | CU-44.1 a CU-44.4 | 05/11 precisa: el acceso es el rol |
| 03/11 | Organigrama como vista, no como motor de la cadena | Completo | CU-45, CU-46 | CU-45.1 a CU-45.3; CU-46.1 a CU-46.4 | 05/11 confirma |
| 03/11 | En la recepcion no se calza por el codigo ni el nombre de la guia | Parcial | CU-47 | CU-47.1 a CU-47.4 | 05/11 precisa: se elige el articulo del maestro |
| 03/11 | AlmaWeb: numeros y permisos del portal | Fuera | CU-48 | CU-48.1 a CU-48.4 | - |
| 05/11 | Administradores por modulo se retiran. El acceso es el rol | Parcial | CU-49 | CU-49.1 a CU-49.5 | Precisa el 03/11 |
| 05/11 | Grupos iguales a areas, con topes distintos. Gerencia de area y gerencia general en cada grupo | Parcial | CU-50 | CU-50.1 a CU-50.4 | No pisa el motor. Pisa, el mismo dia, eliminar los grupos |
| 05/11 | Siempre firma la jefatura, despues gerencia de area, despues gerencia general | Parcial | CU-51 | CU-51.1 a CU-51.5 | Precisa la cadena. No vuelve a poner aprobacion en la OV |
| 05/11 | El ultimo eslabon tiene tope. Si la OC lo pasa, no entra a la cadena y hay mensaje | Faltante | CU-52 | CU-52.1 a CU-52.5 | Pisa "el ultimo aprueba hasta infinito" |
| 05/11 | Tope por CLP, USD y yuan. Propuesta del dia, editable y despues fija | Faltante | CU-53 | CU-53.1 a CU-53.5 | Precisa el tope en pesos. No lo borra |
| 05/11 | Receta de embalaje, no de un solo packing. El consumo reparte cantidades | Faltante | CU-54, CU-64 | CU-54.1 a CU-54.5; CU-64.1 a CU-64.5 | Pisa receta y produccion obligadas a un packing |
| 05/11 | Consumo a precio promedio del stock del mes. No FIFO por guia | Parcial | CU-55 | CU-55.1 a CU-55.4 | Precisa el 28/10. La devolucion sigue al precio de la guia |
| 05/11 | Devolucion: precio de la guia, documento nuevo, sin rebajar esa guia | Parcial | CU-56 | CU-56.1 a CU-56.5 | Precisa el 28/10 |
| 05/11 | Stock de recepcion solo al confirmar, con adjunto | Faltante | CU-57 | CU-57.1 a CU-57.4 | Precisa el 03/11 |
| 05/11 | Activo fijo solo con OC recepcionada de ese tipo | Faltante | CU-58 | CU-58.1 a CU-58.6 | Precisa el 27/10 |
| 05/11 | Correccion de proforma: editar la linea. Sin asiento nuevo. Reporte solo activos | Faltante | CU-59 | CU-59.1 a CU-59.5 | Pisa el asiento de ajuste del 03/11 |
| 05/11 | Anular asiento: la fila queda, no entra al mayor. Lo hace la jefatura, con motivo | Faltante | CU-60 | CU-60.1 a CU-60.5 | - |
| 05/11 | Organigrama con cuatro titulos, solo vista | Parcial | CU-61, CU-46 | CU-61.1 a CU-61.3; CU-46.1 a CU-46.4 | Precisa el 03/11 y el 05/11 temprano |
| 05/11 | CAF agotado, tesoreria con Lupe, reportes con cada jefatura | Fuera y Espera | CU-62, CU-36, CU-63 | CU-62.1 a CU-62.3; CU-36.1 a CU-36.4; CU-63.1 a CU-63.3 | No pisan acuerdos |

## 2. Casos

### CU-01. Ingreso manual de la guia mientras abastecimiento siga en Acepta

**Acuerdo.** 21/10. Mientras abastecimiento siga en Acepta, la guia se puede tipear a mano y se le adjuntan archivos o un Excel de Acepta.

**Estado.** Parcial. El 03/11 la sala ya habla del ingreso manual como camino existente. La auditoria no acredita los N archivos ni el Excel de Acepta. La foto al confirmar es CU-57.

**Quien.** Locutor no rotulado. Pista: pregunta operativa a Carlos, y dice que abastecimiento sigue en Acepta. Sala 21/10: Maria Jesus, Fran y Lupe. `transcripcion-2026-10-21-reunion-cliente.md` [17:56] a [18:51].

**Que pasa.** Si la guia no llega por GoSocket, el usuario la digita. Mientras dure la dualidad con Acepta, ese ingreso manual sigue. Al documento se le pueden asociar varios archivos, o subir un Excel descargado de Acepta.

**Documento o pantalla.** Guia de despacho recibida, ingreso manual.

**Quien puede.** La sala no nombro el permiso.

**Limites.** El ingreso manual dura mientras abastecimiento opere en Acepta. La sala pidio una guia real de Acepta para copiar campos [18:59]. Ese archivo no esta en este corte: no se inventan campos.

**Que debe quedar.** Una guia digitada, con sus adjuntos, usable en la recepcion igual que una guia que hubiera llegado por integracion.

**Documentacion antes de codear.** Pantalla de ingreso manual de guia. Mensaje si falta un campo que la guia real traiga, cuando ese archivo exista. Estado de la guia registrada, todavia sin stock hasta CU-57. Permiso: la sala no lo nombro. Dato: archivos o Excel asociados a la guia.

**Depende de.** Ninguno. La foto y el stock al confirmar son CU-57.

### Abanico

#### CU-01.1 Guia digitada con respaldo
- Condicion: La guia no llega por GoSocket y abastecimiento sigue en Acepta.
- Que pasa: Se tipea a mano y se le asocian archivos o un Excel de Acepta.
- Que queda: Guia registrada, usable en la recepcion, todavia sin stock.
- Rama: construir

#### CU-01.2 Registrada y sin stock
- Condicion: La guia se digito y todavia no se confirma la recepcion.
- Que pasa: No se mueve stock. Eso queda para confirmar, en CU-57.
- Que queda: Estado registrada, cantidad en bodega sin cambio.
- Rama: construir

#### CU-01.3 Campos de una guia real que no llego
- Condicion: No esta el archivo de guia real pedido el 21/10.
- Que pasa: No se inventan campos para el formulario.
- Que queda: Sin columnas nuevas sacadas de un archivo ausente.
- Rama: no construir

#### CU-01.4 Stock al tipear
- Condicion: Alguien suma bodega en el mismo acto de digitar.
- Que pasa: Ese acto no es este acuerdo. El stock sube al confirmar.
- Que queda: Nada de stock nuevo en el tipeo. Lo hace CU-57.
- Rama: no construir

### CU-02. La hija no queda con saldo

**Acuerdo.** 21/10. Las hijas nacen en la recepcion, mueren al facturar y quedan 100% calzadas. Solo la madre puede quedar con saldo.

**Estado.** Parcial. Hay codigo de madre. La auditoria deja abierto el recorrido guia > hija > factura > asiento > madre.

**Quien.** Locutor no rotulado. Pista: corrige el saldo de la hija. `transcripcion-2026-10-21-reunion-cliente.md` [22:21] a [23:10] y [28:00] a [28:07].

**Que pasa.** Llega una guia que no cubre la OC. Nace una hija con esa recepcion. La hija es la orden real: al asociarle la factura se cierra. No conserva saldo. La madre es la unica que puede seguir con saldo hasta que las llegadas la completen.

**Documento o pantalla.** OC madre e hija de insumos, en la recepcion y en el libro de compras.

**Quien puede.** La sala no nombro el permiso de crear la hija. La hija no vuelve a la cadena: la madre ya fue aprobada. Se conserva la cadena solo en la OC de compras.

**Limites.** Hija siempre 100% calzada con su factura. Saldo solo en la madre. El 03/11 precisa que solo la ultima guia ajusta la madre: CU-43.

**Que debe quedar.** Hija cerrada al facturar. Madre con el saldo que todavia no llego.

**Documentacion antes de codear.** Donde se ve madre e hija. Mensaje si se intenta dejar saldo en la hija. Estados: hija cerrada al facturar, madre abierta mientras haya saldo. Permiso no nombrado. Dato: vinculo madre, hija, guia y factura.

**Depende de.** Ninguno. Lo precisa CU-43.

### Abanico

#### CU-02.1 Hija que se cierra al facturar
- Condicion: La guia no cubre la OC y luego se le asocia la factura.
- Que pasa: Nace la hija con esa recepcion y, al facturar, queda 100% calzada.
- Que queda: Hija cerrada, sin saldo.
- Rama: construir

#### CU-02.2 Madre con lo que falta
- Condicion: Llegaron unas tandas y todavia no todas.
- Que pasa: Solo la madre conserva el saldo pendiente.
- Que queda: Madre abierta. Las hijas ya facturadas siguen cerradas.
- Rama: construir

#### CU-02.3 Saldo dejado en la hija
- Condicion: Se intenta guardar una hija con saldo despues de facturar.
- Que pasa: El sistema no la deja. Mensaje no nombrado por la sala.
- Que queda: La hija no queda abierta. El saldo, si existe, sigue en la madre.
- Rama: construir

#### CU-02.4 Hija que vuelve a la cadena
- Condicion: Se manda la hija a aprobacion como si fuera una OC nueva.
- Que pasa: No corresponde: la madre ya fue aprobada. La cadena sigue solo en la OC de compras.
- Que queda: Hija sin recorrido de cadena.
- Rama: no construir

### CU-03. La hija no se contabiliza en la orden

**Acuerdo.** 21/10. Las hijas no se contabilizan en la orden. El asiento va en el cierre de bodega. Al recepcionar: existencia contra facturas por recibir. Al calce: se reconoce al proveedor.

**Estado.** Parcial. Mismo hueco que CU-02: el recorrido contable de punta a punta no esta acreditado.

**Quien.** Locutor no rotulado. Pista: explica los dos asientos de bodega. `transcripcion-2026-10-21-reunion-cliente.md` [23:27] a [24:06].

**Que pasa.** Recepcionar acumula el mes. No hay boton de contabilizar en la orden hija. Al cierre de bodega hay dos momentos: existencia contra facturas por recibir, y al calce se saca facturas por recibir y se reconoce al proveedor.

**Documento o pantalla.** Cierre de bodega. La orden hija queda sin accion de contabilizar.

**Quien puede.** La sala no nombro quien cierra bodega.

**Limites.** No se contabiliza la hija en la orden. Las cuentas que falten en el cierre estan en espera: CU-65. Sin merma.

**Que debe quedar.** Asiento de recepcion y asiento de calce en el cierre, no en la OC hija.

**Documentacion antes de codear.** Pantalla de cierre de bodega. Mensaje si se intenta contabilizar la hija desde la orden. Estado de la hija: recepcionada o facturada, no "contabilizada en la orden". Permiso no nombrado. Dato: los dos asientos y su vinculo a la recepcion y al calce.

**Depende de.** CU-02. Las cuentas faltantes son CU-65.

### Abanico

#### CU-03.1 Asiento al recepcionar
- Condicion: Hay recepcion acumulada del mes y se cierra bodega.
- Que pasa: Existencia contra facturas por recibir, en el cierre, no en la orden.
- Que queda: Asiento de recepcion ligado a la recepcion.
- Rama: construir

#### CU-03.2 Asiento al calce
- Condicion: La factura calza lo recepcionado.
- Que pasa: Se saca facturas por recibir y se reconoce al proveedor.
- Que queda: Asiento de calce en el cierre.
- Rama: construir

#### CU-03.3 Contabilizar desde la hija
- Condicion: Alguien usa una accion de contabilizar en la orden hija.
- Que pasa: No guarda ese asiento ahi. Mensaje no nombrado por la sala.
- Que queda: Hija recepcionada o facturada, no contabilizada en la orden.
- Rama: construir

#### CU-03.4 Cuenta de merma en el cierre
- Condicion: Se agrega merma porque la palabra aparecio al mirar movimientos.
- Que pasa: Merma no existe. Las cuentas que falten esperan el listado, CU-65.
- Que queda: Sin cuenta de merma.
- Rama: no construir

### CU-04. Activo fijo que no nace de una OC

**Acuerdo.** 21/10. El activo entra directo al modulo y no nace de una OC. El nexo es la factura. Sin centro de costo. Vida util en meses, una sola, igual a la tributaria. Correccion monetaria por IPC.

**Estado.** Pisado. No construir. La regla que gana es CU-58.

**Quien.** Locutor no rotulado. Pista: corrige el alta que estaba en pantalla. `transcripcion-2026-10-21-reunion-cliente.md` [30:39] a [30:54], [33:28], [35:06] y [37:59] a [40:43].

**Que pasa.** Ese dia el cliente dijo que el bien no sale de una OC y que el nexo es la factura del libro de compras. El 27/10 Agustin, relatado en sala, pidio OC de activo. El 05/11 la sala dejo el maestro recien con la OC recepcionada.

**Documento o pantalla.** No se construye el alta directa sin OC.

**Quien puede.** No aplica al flujo viejo.

**Limites que siguen, y viven en CU-58.** Sin centro de costo en el alta. Vida util unica en meses, igual a la tributaria. IPC en el historial de valor neto. No se dan de alta bienes desde un papel que no llego digital [32:57] a [33:14].

**Que debe quedar.** Nada del origen "directo al modulo, sin OC".

**Documentacion antes de codear.** No exige documento del flujo viejo.

**Depende de.** CU-58.

### Abanico

#### CU-04.1 Alta directa sin OC
- Condicion: El bien entra al modulo sin orden de compra.
- Que pasa: Es el origen que el 27/10 y el 05/11 pisaron.
- Que queda: No queda esa alta. Gana CU-58.
- Rama: no construir. Gana CU-58

#### CU-04.2 Nexo solo con la factura
- Condicion: Se crea el maestro contra la factura, sin OC recepcionada.
- Que pasa: Ese nexo del 21/10 no se construye.
- Que queda: Sin maestro nacido de la factura sola. Gana CU-58.
- Rama: no construir. Gana CU-58

#### CU-04.3 Papel que no llego digital
- Condicion: Se da de alta un bien desde un documento fisico que no esta en el libro.
- Que pasa: El propio 21/10 dijo que no debiese. El alta vigente es la OC recepcionada.
- Que queda: Sin ese alta. Gana CU-58.
- Rama: no construir. Gana CU-58

### CU-05. Cierre de contratistas: aprobadas con factura, cuenta y glosa

**Acuerdo.** 21/10. Al cierre entran solo proformas aprobadas y con factura. Cuenta de mano de obra contratista, glosa editable a cargo de la jefatura. El mismo patron de cuenta y glosa en el cierre de bodega.

**Estado.** Parcial. El 26/10 y el 03/11 precisan que una proforma del mes puede facturarse al mes siguiente y quedar en facturas por recibir. La auditoria no acredita el asiento de ese cierre de punta a punta.

**Quien.** Locutor no rotulado. Carlos nombra la cuenta y la sala la confirma. `transcripcion-2026-10-21-reunion-cliente.md` [41:22] a [43:19].

**Que pasa.** El cierre lista lo que entra (aprobada y con factura ese dia) y deja informativo el borrador, lo pendiente y el ingreso fuera de proforma. La cuenta de mano de obra viene preseleccionada y la jefatura puede cambiarla, con glosa. Ese par cuenta + glosa se repite en el cierre de bodega.

**Documento o pantalla.** Traspaso y cierre de contratistas, y el mismo par en cierre de bodega.

**Quien puede.** La glosa y el cambio de cuenta quedan a cargo de la jefatura [43:02].

**Limites.** Lo que no esta aprobado o no tiene factura no entra al asiento, en la frase de ese dia. El 03/11 afloja la factura del mismo mes: CU-20 y CU-42. Se conserva que la OV no tiene cadena.

**Que debe quedar.** Un cierre que no meta borradores, con cuenta y glosa editables por la jefatura, y el mismo par en bodega.

**Documentacion antes de codear.** Que entra y que queda informativo. Mensaje si una proforma no cumple. Estado de la proforma que centraliza. Permiso de jefatura para cuenta y glosa. Dato: cuenta, glosa y lista de proformas del asiento.

**Depende de.** CU-20 y CU-21 precisan el bloque y el asiento.

### Abanico

#### CU-05.1 Aprobada con factura, cuenta y glosa
- Condicion: La proforma esta aprobada y con factura, en la lectura de ese dia.
- Que pasa: Entra al cierre. La cuenta de mano de obra viene preseleccionada.
- Que queda: Asiento con esa proforma, cuenta y glosa.
- Rama: construir

#### CU-05.2 Borrador, pendiente o ingreso suelto
- Condicion: La proforma no esta aprobada, o el ingreso no tiene proforma.
- Que pasa: No entra al asiento. Queda informativo. Mensaje no nombrado por la sala.
- Que queda: Fuera del asiento, visible como informativo.
- Rama: construir

#### CU-05.3 La jefatura cambia cuenta y glosa
- Condicion: La jefatura necesita otra cuenta o completa la glosa.
- Que pasa: Puede cambiar la cuenta preseleccionada y la glosa. El mismo par va al cierre de bodega.
- Que queda: Cuenta y glosa guardadas en contratistas y en bodega.
- Rama: construir

#### CU-05.4 Factura exigida del mismo mes
- Condicion: Se frena el gasto porque la factura cae al mes siguiente.
- Que pasa: Esa exigencia la aflojo el 03/11.
- Que queda: No se construye ese freno. Gana la precision de CU-20.
- Rama: no construir. Gana CU-20

#### CU-05.5 Cadena en la orden de venta
- Condicion: Se aprovecha el cierre para poner aprobacion en la OV.
- Que pasa: La OV se confirma al guardar. Este acuerdo no la toca.
- Que queda: OV sin cadena.
- Rama: no construir

### CU-06. Ver el asiento, comentar, anular, reversar y filtrar activos

**Acuerdo.** 22/10. Ver la glosa, editar un comentario, anular, reversar, PDF, y filtro de solo activos o todos.

**Estado.** Parcial. En local el asiento contabilizado no se edita en montos, cuentas ni glosa, y queda quien y cuando. Anular con motivo y el mayor solo con activos son CU-59 y CU-60. El PDF no quedo acreditado.

**Quien.** Locutor no rotulado. Pista: "cuando nosotros queramos descargar los asientos". Sala: Maria Jesus, Lupe y Fran. `transcripcion-2026-10-22-reunion-cliente.md` [06:29] a [08:21].

**Que pasa.** La glosa que se ve es la del comprobante. La sala pidio poder agregar un comentario editable bajo esa glosa. Al descargar, el defecto es solo activos; los reversados se consultan aparte. Tambien pidieron PDF [07:46].

**Documento o pantalla.** Contabilidad > comprobantes y asientos, y el libro mayor.

**Quien puede.** La sala no nombro el permiso el 22/10. El 05/11 la anulacion queda en la jefatura: CU-60.

**Limites.** No se usa el reverso para armar reportes. Editar montos de un asiento ya contabilizado sigue prohibido. Anular no borra: CU-60.

**Que debe quedar.** Glosa visible, comentario aparte, descarga por defecto de activos, y PDF si se construye la parte que falta.

**Documentacion antes de codear.** Diferencia entre glosa del comprobante y comentario. Mensaje si se intenta editar el monto. Estado activo / reversado / anulado. Permiso de anular: CU-60. Dato: comentario, y el filtro con el que se exporto.

**Depende de.** CU-60 para anular. CU-59 para que el mayor omita lo anulado.

### Abanico

#### CU-06.1 Glosa visible y comentario aparte
- Condicion: El comprobante ya tiene glosa.
- Que pasa: Se muestra esa glosa y se puede agregar un comentario debajo, sin reemplazarla.
- Que queda: Glosa del comprobante intacta, comentario guardado aparte.
- Rama: construir

#### CU-06.2 Descarga de activos, y reversados aparte
- Condicion: Se exportan asientos.
- Que pasa: El defecto es solo activos. Los reversados se consultan si se piden.
- Que queda: Archivo de activos, o de todos, segun el filtro.
- Rama: construir

#### CU-06.3 PDF del asiento
- Condicion: Se pide el comprobante en PDF, ademas de Excel.
- Que pasa: Se genera el PDF.
- Que queda: PDF del asiento que se esta viendo.
- Rama: construir

#### CU-06.4 Editar monto, cuenta o glosa ya contabilizados
- Condicion: El asiento ya esta contabilizado y se intenta cambiar monto, cuenta o glosa.
- Que pasa: No se guarda. En local ya queda quien y cuando. Mensaje no nombrado por la sala.
- Que queda: Asiento igual. El comentario de CU-06.1 no es esta edicion.
- Rama: regresion

#### CU-06.5 Anular borrando la fila
- Condicion: Anular se entiende como borrar el comprobante.
- Que pasa: No es este acuerdo. Anular deja la fila.
- Que queda: Sin borrado. Gana CU-60.
- Rama: no construir. Gana CU-60

#### CU-06.6 Reverso para armar reportes
- Condicion: Se reversa un asiento para alimentar un reporte.
- Que pasa: El caso dice que el reverso no se usa para eso.
- Que queda: Sin ese reverso.
- Rama: no construir

### CU-07. Factor de honorarios e IPC en parametrizacion

**Acuerdo.** 22/10. El factor de honorarios vive en parametrizacion. El IPC se actualiza y guarda historial.

**Estado.** Faltante. La auditoria no lo lista como hecho. La boleta de honorarios es CU-30.

**Quien.** Locutor no rotulado. La sala acepta mover el factor y guardar el IPC. `transcripcion-2026-10-22-reunion-cliente.md` [09:07] a [09:58].

**Que pasa.** El factor no es de uso diario: se actualiza cuando cambia la norma y se consulta. El IPC se carga como un valor nuevo y conserva el historial. El 05/11 no lo reabrio.

**Documento o pantalla.** Parametrizacion del factor y del IPC.

**Quien puede.** La sala no nombro el permiso. El 21/10 la glosa de cierre quedo en la jefatura; aqui no se repitio ese rol.

**Limites.** La sala no dijo la tasa ni la fecha de vigencia. No se inventan.

**Que debe quedar.** Factor consultable desde parametrizacion, e IPC con historial de valores.

**Documentacion antes de codear.** Donde se edita el factor y el IPC. Mensaje si se guarda un valor sin fecha. Estado: valor vigente e historial. Permiso no nombrado. Dato: valor, fecha y quien lo cargo.

**Depende de.** Ninguno. CU-30 es el documento de la boleta, no este parametro.

### Abanico

#### CU-07.1 Factor en parametrizacion
- Condicion: Hay que consultar o actualizar el factor de honorarios.
- Que pasa: Vive en parametrizacion. No es una pantalla de uso diario.
- Que queda: Factor vigente consultable.
- Rama: construir

#### CU-07.2 IPC nuevo con historial
- Condicion: Cambia el IPC.
- Que pasa: Se guarda un valor nuevo y el anterior permanece en el historial.
- Que queda: Valor vigente e historial.
- Rama: construir

#### CU-07.3 IPC sin fecha
- Condicion: Se intenta guardar un valor de IPC sin fecha.
- Que pasa: No se guarda. Mensaje no nombrado por la sala.
- Que queda: Sin valor huerfano en el historial.
- Rama: construir

#### CU-07.4 Tasa o vigencia inventadas
- Condicion: No hay tasa ni fecha dichas por la sala.
- Que pasa: No se fija un numero ni una vigencia de ley.
- Que queda: Sin parametro inventado.
- Rama: no construir

### CU-08. Presupuesto por centro de costo

**Acuerdo.** 22/10. Presupuesto por centro de costo, con ejecucion anual, y PDF.

**Estado.** Faltante. La matriz lo deja pendiente. La auditoria no lo muestra en local.

**Quien.** Locutor no rotulado. Confirma el PDF con "Si". `transcripcion-2026-10-22-reunion-cliente.md` [10:05] a [10:35].

**Que pasa.** Se ve cuanto del presupuesto del centro ya se ejecuto en el ano, y se puede imprimir a PDF. El 26/10 la sala retoma la responsabilidad del area sobre cuenta y elemento para que el presupuesto sirva [27:27] a [28:51]. No cerro una alerta de porcentaje: eso no esta dicho como regla en la transcripcion de esa manana.

**Documento o pantalla.** Presupuesto por centro de costo.

**Quien puede.** La sala no nombro el permiso.

**Limites.** La sala no dijo montos, monedas ni el periodo distinto del ano.

**Que debe quedar.** Ejecucion anual visible y exportable a PDF.

**Documentacion antes de codear.** Que muestra la ejecucion. Mensaje si el centro no tiene presupuesto. Estado del monto ejecutado contra el anual. Permiso no nombrado. Dato: centro, monto anual y lo ya imputado.

**Depende de.** CU-15 y CU-16, porque sin cuenta, centro y elemento el presupuesto no cuadra. No se construye antes de que esos existan; en local la OC ya pide cuenta y centro.

### Abanico

#### CU-08.1 Ejecucion anual
- Condicion: El centro tiene presupuesto del ano.
- Que pasa: Se ve cuanto ya se imputo en el ano.
- Que queda: Ejecucion anual del centro.
- Rama: construir

#### CU-08.2 PDF del presupuesto
- Condicion: Se pide imprimir esa vista.
- Que pasa: Sale en PDF.
- Que queda: PDF de la ejecucion del centro.
- Rama: construir

#### CU-08.3 Centro sin presupuesto
- Condicion: El centro no tiene monto anual.
- Que pasa: No se fabrica un presupuesto. Mensaje no nombrado por la sala.
- Que queda: Sin monto anual inventado.
- Rama: construir

#### CU-08.4 Alerta de porcentaje
- Condicion: Se agrega un aviso al llegar a un porcentaje del presupuesto.
- Que pasa: La manana del 26/10 no cerro esa alerta.
- Que queda: Sin alerta de porcentaje.
- Rama: no construir

### CU-09. Filtro de fechas en los libros

**Acuerdo.** 22/10. Libros con filtro de fechas. El balance no se saca de un ano a otro: ano actual o ano pasado.

**Estado.** Parcial. El 26/10 preciso el ER, el ESF y el balance, y eso esta en local (CU-13 y CU-27). El filtro de fechas del libro mayor no se volvio a acreditar el 05/11.

**Quien.** Locutor no rotulado. Pide rango de fecha y luego la observacion del balance. `transcripcion-2026-10-22-reunion-cliente.md` [11:51] a [12:06] y [16:08] a [16:47].

**Que pasa.** Mayor, balance, estado de resultados y situacion financiera se filtran por fechas, con calendario. El balance de 8 columnas no mezcla dos anos: de enero a diciembre del ano elegido, actual o pasado. La sala dijo que esa limitacion es de ese reporte.

**Documento o pantalla.** Libros de contabilidad.

**Quien puede.** La sala no nombro el permiso.

**Limites.** Balance de 8: no cruza del 1 de enero al 31 de diciembre de otro ano en el mismo informe. El 26/10 cambia el resto: el ER es de un mes, y el ESF puede mostrar anos anteriores. Esa precision gana. No se construye un ER anual por esta frase del 22/10.

**Que debe quedar.** Filtro de fechas en el mayor. El balance de 8 respeta el ano. ER y ESF siguen CU-13.

**Documentacion antes de codear.** Donde esta el calendario del mayor. Mensaje si el balance de 8 pide dos anos. Estado no aplica a un documento. Permiso no nombrado. Dato: desde y hasta del filtro.

**Depende de.** CU-13 y CU-27 para no rehacer ER, ESF y balance.

### Abanico

#### CU-09.1 Fechas en el mayor
- Condicion: Se consulta el libro mayor.
- Que pasa: El rango se elige con calendario, desde y hasta.
- Que queda: Mayor del rango pedido.
- Rama: construir

#### CU-09.2 Balance de un solo ano
- Condicion: El balance de 8 se pide del ano actual o del pasado.
- Que pasa: No mezcla dos anos. Va de enero a diciembre del ano elegido. Eso ya quedo con CU-27.
- Que queda: Balance de un ano.
- Rama: regresion

#### CU-09.3 Balance que cruza el ano
- Condicion: El mismo balance de 8 pide dias de dos anos.
- Que pasa: No se emite asi. Mensaje no nombrado por la sala.
- Que queda: Sin informe cruzado.
- Rama: regresion

#### CU-09.4 Estado de resultados anual por esta frase
- Condicion: Se arma un ER de varios meses porque el 22/10 hablo de filtros.
- Que pasa: El 26/10 dejo el ER de un mes.
- Que queda: ER sin ese armado. Gana CU-13.
- Rama: no construir. Gana CU-13

### CU-10. Cartola: moneda, banco, pesos, PDF, adjunto y semana

**Acuerdo.** 22/10. La cartola identifica moneda y banco, se puede ver en pesos, se exporta a PDF, el pago lleva adjunto, se contabiliza desde la cartola y el movimiento va a una semana.

**Estado.** Parcial. La carga, la semana y contabilizar desde la cartola se precisaron el 28/10 y parte quedo en local (CU-31 a CU-34). Ver en pesos, el PDF y el adjunto del pago no se reabrieron y la auditoria no los acredita.

**Quien.** Locutor no rotulado. Operacion de cartola; nombran a Lupe para el archivo y el PDF. `transcripcion-2026-10-22-reunion-cliente.md` [17:51] a [18:20], [20:48], [24:32] y [27:07] a [27:20]. El adjunto del pago quedo para cuando Lupe modele el modulo [28:50].

**Que pasa.** Cada tab es moneda y banco. Si el archivo no se reconoce solo, se asigna a mano. Los egresos se asignan a una semana del periodo y se contabilizan desde el movimiento. La sala pidio ver montos en pesos y exportar la cartola a PDF. El comprobante adjunto al pago no se cerro ese dia.

**Documento o pantalla.** Tesoreria > cartola, y el pago que nace del movimiento.

**Quien puede.** La sala no nombro el permiso. Lupe es quien opera la cartola.

**Limites.** La cartola manda [36:31]. No se duplica el diseño del 28/10. Se conserva el asiento de banco igual a la cartola, ya vigente, sin un asiento distinto de pago.

**Que debe quedar.** Moneda y banco identificables, semana de pago, y las tres piezas que faltan: vista en pesos, PDF y adjunto del pago cuando Lupe lo cierre. El adjunto no se inventa antes de esa reunion: CU-36 es otra espera. Aqui el adjunto quedo nombrado y sin diseno.

**Documentacion antes de codear.** Solo lo faltante: vista en pesos, PDF de la cartola, y si el pago guarda un archivo. Mensaje si moneda o banco no se reconocen. Estado contabilizado o pendiente del movimiento. Permiso no nombrado. Dato: banco, moneda, semana y archivo del pago.

**Depende de.** CU-31 a CU-34, que no se reconstruyen.

### Abanico

#### CU-10.1 Montos vistos en pesos
- Condicion: La cartola esta en moneda de origen y se pide verla en pesos.
- Que pasa: Los montos se muestran en pesos.
- Que queda: Vista en pesos, sin perder la moneda de origen.
- Rama: construir

#### CU-10.2 PDF de la cartola
- Condicion: Se exporta la cartola.
- Que pasa: Ademas del Excel, hay PDF.
- Que queda: PDF de lo que se esta viendo.
- Rama: construir

#### CU-10.3 Moneda o banco no reconocidos
- Condicion: El archivo no identifica solo la moneda o el banco.
- Que pasa: No se aborta: se asignan a mano.
- Que queda: Cartola con banco y moneda asignados. Mensaje no nombrado por la sala.
- Rama: construir

#### CU-10.4 Semana y contabilizar desde la cartola
- Condicion: El egreso se asigna a una semana y se contabiliza desde el movimiento.
- Que pasa: Eso ya quedo precisado el 28/10. No se reconstruye aqui.
- Que queda: Movimiento en su semana, estado contabilizado o pendiente.
- Rama: regresion

#### CU-10.5 Adjunto del pago disenado ahora
- Condicion: El pago llevaria un archivo, y Lupe no cerro como.
- Que pasa: El adjunto quedo nombrado y sin diseno. No se inventa el formulario.
- Que queda: Sin adjunto nuevo en este corte.
- Rama: no construir

#### CU-10.6 Asiento de pago distinto de la cartola
- Condicion: Se crea un asiento de pago aparte del movimiento de cartola.
- Que pasa: La cartola manda. El asiento de banco sigue siendo el de la cartola.
- Que queda: Sin asiento paralelo de pago.
- Rama: no construir

### CU-11. Estado de cuenta por RUT a Excel

**Acuerdo.** 22/10. Estado de cuenta por RUT, con anticipos y facturas, para cliente, proveedor y productor, exportado a Excel.

**Estado.** Faltante. No esta en lo que la auditoria da por hecho.

**Quien.** Locutor no rotulado, le habla a Carlos. Lupe confirma Excel cuando la nombran. `transcripcion-2026-10-22-reunion-cliente.md` [42:11] a [42:25] y [44:50] a [45:03].

**Que pasa.** Se busca un RUT y se ven anticipos, facturas y documentos. El filtro separa proveedor, productor y cliente, o combinaciones. La exportacion a Excel lleva el RUT y la razon social, y abajo los movimientos filtrados.

**Documento o pantalla.** Estado de cuenta en tesoreria.

**Quien puede.** La sala no nombro el permiso. Dijeron que contabilidad puede ver el conjunto y que el consulta de productor o proveedor es de tesoreria.

**Limites.** No es un pago ni una contabilizacion: es consulta. El maestro Productor sigue fuera: CU-12. El productor aqui es un rol del mismo RUT, no una entidad nueva.

**Que debe quedar.** Un Excel del RUT con los movimientos del filtro elegido.

**Documentacion antes de codear.** Filtros de rol. Mensaje si el RUT no tiene movimientos. Estado no aplica. Permiso no nombrado. Dato: RUT, rol de cada linea, anticipo o factura, y el folio.

**Depende de.** CU-12 para saber si el RUT es cliente, proveedor o productor.

### Abanico

#### CU-11.1 RUT con un rol, a Excel
- Condicion: Se consulta un RUT como cliente, proveedor o productor.
- Que pasa: Se ven anticipos, facturas y documentos de ese filtro, y se exportan.
- Que queda: Excel con RUT, razon social y los movimientos filtrados.
- Rama: construir

#### CU-11.2 Filtro combinado
- Condicion: El mismo RUT es mas de un rol y se eligen dos o los tres.
- Que pasa: La lista respeta la combinacion.
- Que queda: Excel solo con los roles marcados.
- Rama: construir

#### CU-11.3 RUT sin movimientos
- Condicion: El RUT existe y no tiene documentos.
- Que pasa: No se inventan lineas. Mensaje no nombrado por la sala.
- Que queda: Consulta vacia.
- Rama: construir

#### CU-11.4 Quien mira el conjunto y quien consulta
- Condicion: Contabilidad quiere el conjunto. La consulta de productor o proveedor es de tesoreria.
- Que pasa: Contabilidad ve el conjunto. La consulta de un rol queda en tesoreria.
- Que queda: Misma ficha de RUT, dos usos dichos por la sala.
- Rama: construir

#### CU-11.5 Pagar o contabilizar desde la consulta
- Condicion: Desde el estado de cuenta se registra un pago o un asiento.
- Que pasa: Este acuerdo es consulta, no pago ni contabilizacion.
- Que queda: Sin pago y sin asiento nacidos aqui.
- Rama: no construir

#### CU-11.6 Productor como entidad nueva
- Condicion: Se abre un maestro Productor para poder filtrar.
- Que pasa: El productor de este caso es un rol del mismo RUT.
- Que queda: Sin maestro nuevo. Sigue CU-12.
- Rama: no construir

### CU-12. Ficha unica y listas separadas

**Acuerdo.** 22/10. Una ficha une cliente, proveedor y productor. Las listas quedan separadas. Si es el mismo RUT, comparten el contacto.

**Estado.** Parcial. La ficha unica de cliente y proveedor se conserva. El maestro Productor sigue fuera. La auditoria del 05/11 no volvio a acreditar las listas separadas ni el aviso de doble rol.

**Quien.** Locutor no rotulado. Pista: no pueden sacar el listado de productores. `transcripcion-2026-10-22-reunion-cliente.md` [47:13] a [49:36].

**Que pasa.** Cliente, proveedor y productor se crean en listas distintas para no cruzar los informes. Si el RUT ya existe, se comparte nombre y contacto: un cambio en uno se ve en el otro. Hay RUT que son proveedor y productor a la vez, y eso se tiene que notar.

**Documento o pantalla.** Ficha de la contraparte, y las listas de proveedores y de productores.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se abre un maestro Productor como entidad nueva. El productor es rol del mismo RUT dentro de la ficha. Contablemente el tratamiento de proveedor y productor es el mismo; la separacion es de lista.

**Que debe quedar.** Listas separadas, ficha compartida por RUT, y marca cuando el RUT tiene mas de un rol.

**Documentacion antes de codear.** Que listas existen. Mensaje si se crea un RUT que ya esta en la otra lista. Estado no aplica. Permiso no nombrado. Dato: roles del RUT y el contacto compartido.

**Depende de.** Ninguno.

### Abanico

#### CU-12.1 Ficha de cliente y proveedor
- Condicion: El RUT ya es cliente o proveedor.
- Que pasa: Siguen en la ficha unica que ya esta.
- Que queda: Una ficha, sin duplicar el contacto.
- Rama: regresion

#### CU-12.2 Listas separadas y doble rol
- Condicion: Hace falta el listado de productores, o el RUT es proveedor y productor.
- Que pasa: Las listas no se cruzan. Si tiene los dos roles, se nota.
- Que queda: Lista de proveedores y lista de productores. Marca de doble rol.
- Rama: construir

#### CU-12.3 Mismo RUT, contacto compartido
- Condicion: Se modifica telefono o correo en una lista y el RUT existe en la otra.
- Que pasa: El cambio se ve en la otra. Mensaje no nombrado por la sala si se esta creando de nuevo.
- Que queda: Un contacto para el RUT.
- Rama: construir

#### CU-12.4 Maestro Productor aparte
- Condicion: Se crea una entidad Productor distinta de la ficha.
- Que pasa: La sala pidio listas, no un maestro nuevo.
- Que queda: Sin entidad Productor.
- Rama: no construir

### CU-13. Resultado del mes y acumulado al 31/12

**Acuerdo.** 26/10 manana. El estado de resultados de un mes muestra solo ese mes. El 31/12 el resultado del ejercicio pasa a resultado acumulado en el estado de situacion financiera.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado. Pista: muestra el informe de enero y el de diciembre. Sala presencial con Maria Jesus. `transcripcion-2026-10-26-presencial.md` [00:15], [01:06] y [01:31] a [02:03].

**Que pasa.** Enero muestra solo lo ingresado del 1 al 31 de enero. En situacion financiera se ven el resultado del ejercicio y el resultado acumulado. Lo que se saca el 31 de diciembre es el que pasa a acumulado.

**Documento o pantalla.** Contabilidad > estados financieros.

**Quien puede.** La sala no nombro el permiso.

**Limites.** Un ER no trae otros meses. El ESF si muestra ejercicio y acumulado. Esto pisa la lectura del 22/10 que trataba el ER como un libro mas con fechas libres: CU-09.

**Que debe quedar.** ER del mes, y ESF con las dos lineas de resultado.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca la pantalla, no se mezcla el mes del ER ni se esconde el acumulado.

**Depende de.** Ninguno.

### Abanico

#### CU-13.1 Resultado de un mes
- Condicion: Se pide el estado de resultados de enero.
- Que pasa: Muestra solo del 1 al 31 de ese mes.
- Que queda: ER del mes, sin otros meses.
- Rama: regresion

#### CU-13.2 Ejercicio y acumulado
- Condicion: Se abre el estado de situacion financiera.
- Que pasa: Se ven el resultado del ejercicio y el resultado acumulado.
- Que queda: Las dos lineas siguen visibles.
- Rama: regresion

#### CU-13.3 Paso del 31/12
- Condicion: Se cierra el 31 de diciembre.
- Que pasa: El resultado del ejercicio pasa a resultado acumulado.
- Que queda: Acumulado con ese traspaso. El ER de diciembre no se mezcla con enero.
- Rama: regresion

#### CU-13.4 ER que trae otro mes
- Condicion: Se pide un resultado que junte dos meses.
- Que pasa: Sigue mostrando solo el mes pedido. No se rearma un ER anual.
- Que queda: ER de un mes.
- Rama: regresion

### CU-14. Carga masiva: se rechaza la linea, no el archivo

**Acuerdo.** 26/10 manana. Si falta un obligatorio, se rechaza esa linea y hay reporte. No se aborta el archivo.

**Estado.** Parcial. La auditoria del 05/11 no lo acredito. El ejemplo de Agrosoft "si falla no carga nada" quedo por debajo de esta preferencia.

**Quien.** Locutor no rotulado. Pista: no quiere que una cuenta se grabe sin centro de costo. `transcripcion-2026-10-26-presencial.md` [08:56] a [09:12].

**Que pasa.** La plantilla obliga los campos de la cuenta. Si una linea viene sin periodo o sin un obligatorio, esa linea no entra y el reporte dice cuantas cargaron y cuantas no. El resto del archivo si carga.

**Documento o pantalla.** Carga masiva de comprobantes, y el reporte de rechazos.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se aborta el archivo entero por una linea mala. La sala no dijo el formato de columnas mas alla del ejemplo Agrosoft que estaban mirando. No se copia ese formato como ley si no lo cerraron campo por campo.

**Que debe quedar.** Lineas buenas cargadas, lineas malas fuera, y un reporte con el conteo.

**Documentacion antes de codear.** Que se considera obligatorio segun la cuenta. Mensaje por linea rechazada. Estado de la linea: cargada o rechazada. Permiso no nombrado. Dato: motivo del rechazo y numero de linea.

**Depende de.** CU-15, porque el obligatorio depende de lo que la cuenta pida.

### Abanico

#### CU-14.1 Linea buena dentro de un archivo mixto
- Condicion: El archivo trae lineas completas y lineas sin un obligatorio.
- Que pasa: Las completas cargan. El archivo no se aborta.
- Que queda: Lineas en estado cargada.
- Rama: construir

#### CU-14.2 Linea sin obligatorio
- Condicion: Falta el periodo o un dato que la cuenta pide, por ejemplo el centro.
- Que pasa: Esa linea no entra. El reporte dice cuantas cargaron y cuantas no.
- Que queda: Linea rechazada, con motivo y numero de linea.
- Rama: construir

#### CU-14.3 Si falla no carga nada
- Condicion: Una linea mala tira atras el archivo entero, como el ejemplo de Agrosoft.
- Que pasa: Esa preferencia quedo abajo. No se aborta el archivo.
- Que queda: Las lineas buenas siguen cargadas.
- Rama: no construir

#### CU-14.4 Formato Agrosoft como ley
- Condicion: Se copian las columnas del ejemplo que estaban mirando.
- Que pasa: La sala no cerro ese formato campo por campo.
- Que queda: Sin columnas tomadas de ese ejemplo.
- Rama: no construir

### CU-15. La cuenta acepta N centros, N elementos y N areas

**Acuerdo.** 26/10 manana. Una cuenta tiene N centros, N elementos y N areas. El elemento no queda amarrado al centro.

**Estado.** Parcial. La auditoria lo dejo "no auditado de nuevo". No se da por completo.

**Quien.** Locutor no rotulado. Maria Jesus esta en la sala y otro locutor cita lo que ella prefiere en la OC. `transcripcion-2026-10-26-presencial.md` [22:15] a [22:43], [25:25] y [30:18] a [30:41]. El contador de cuentas: [29:17] a [29:53].

**Que pasa.** Al parametrizar la cuenta se agregan y quitan centros, elementos y areas. Al usarla, solo se ofrecen los ligados. El centro es transversal (la especie la ocupan varias areas). El elemento es el detalle (DUS, certificado) y no se ata rigido a un centro: el mismo centro puede ir con mas de un elemento.

**Documento o pantalla.** Mantenedor de la cuenta, y los mantenedores de centro, elemento y area.

**Quien puede.** La sala no nombro el permiso del mantenedor. En la OC, si el centro no esta en la lista, se solicita al administrador con motivo: eso esta dicho en CU-16, no se agrega libre.

**Limites.** No ligar elemento a centro. En centro, elemento y area pidieron una columna con la cantidad de cuentas, y al clic el detalle [29:53].

**Que debe quedar.** La cuenta con sus tres listas, y el contador en el mantenedor inverso.

**Documentacion antes de codear.** Como se agregan los N. Mensaje si se usa uno que la cuenta no tiene. Estado no aplica. Permiso no nombrado. Dato: las asociaciones cuenta-centro, cuenta-elemento y cuenta-area.

**Depende de.** Ninguno.

### Abanico

#### CU-15.1 N centros, N elementos y N areas
- Condicion: Se parametriza una cuenta.
- Que pasa: Se agregan o quitan centros, elementos y areas. Al usarla, solo salen los ligados.
- Que queda: Tres listas de la cuenta.
- Rama: construir

#### CU-15.2 Mismo centro, otro elemento
- Condicion: Un centro transversal usa mas de un elemento, por ejemplo DUS y certificado.
- Que pasa: El elemento no queda amarrado a ese centro.
- Que queda: Centro y elemento elegidos por separado, dentro de las listas.
- Rama: construir

#### CU-15.3 Dimension que la cuenta no tiene
- Condicion: Se intenta usar un centro, elemento o area fuera de la lista.
- Que pasa: No se ofrece. Mensaje no nombrado por la sala. En la OC la solicitud al administrador es CU-16.
- Que queda: Sin asociacion libre.
- Rama: construir

#### CU-15.4 Contador en el mantenedor inverso
- Condicion: Se mira el centro, el elemento o el area.
- Que pasa: Una columna dice cuantas cuentas lo usan y, al clic, el detalle.
- Que queda: Contador y detalle de cuentas.
- Rama: construir

#### CU-15.5 Elemento atado al centro
- Condicion: Elegir el centro deja un solo elemento fijo.
- Que pasa: La sala dijo que no se amarra rigido.
- Que queda: Sin ese amarre.
- Rama: no construir

### CU-16. En la OC primero la cuenta, despues el centro y el elemento

**Acuerdo.** 26/10 manana. Primero cuenta, despues centro, despues elemento. Una linea, un centro. Sin cuenta, centro y elemento bloqueados.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado, y Maria Jesus citada por nombre para preferir varias lineas. `transcripcion-2026-10-26-presencial.md` [44:04] a [44:13] y [47:25] a [47:40].

**Que pasa.** En la linea de la OC se elige la cuenta. Recien ahi se habilitan centro y elemento, limitados a los de esa cuenta. Si la misma cuenta va a dos centros, son dos lineas, no un renglon con varios centros.

**Documento o pantalla.** Compras > nueva OC.

**Quien puede.** La sala no nombro un permiso distinto del de crear la OC. Si el centro o el elemento no estan en la cuenta, se solicita al administrador con motivo, usuario y cuenta [44:13] a [45:24]. No se agregan a mano en la OC.

**Limites.** Se conserva: cotizacion solo como referencia dentro de la OC, no vender bajo el precio de compra del maestro, y cadena solo de la OC de compras. Una linea, un centro.

**Que debe quedar.** Linea sin cuenta no imputa centro ni elemento. Dos centros son dos lineas.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca la OC, no se invierte el orden ni se deja elegir centro sin cuenta.

**Depende de.** CU-15 para la lista de la cuenta. La OC ya exige el orden en local.

### Abanico

#### CU-16.1 Cuenta, despues centro y elemento
- Condicion: Se carga una linea de OC.
- Que pasa: Sin cuenta, centro y elemento siguen bloqueados. Con cuenta, solo los de esa cuenta.
- Que queda: Linea con una cuenta y un centro.
- Rama: regresion

#### CU-16.2 Dos centros
- Condicion: La misma cuenta va a dos centros.
- Que pasa: Son dos lineas, no un renglon con varios centros.
- Que queda: Dos lineas.
- Rama: regresion

#### CU-16.3 Centro que no esta en la cuenta
- Condicion: El centro o el elemento no figuran en la lista.
- Que pasa: No se agregan a mano. Se solicitan al administrador con motivo, usuario y cuenta.
- Que queda: OC sin esa dimension hasta que exista en la cuenta.
- Rama: regresion

#### CU-16.4 Pisos de la OC
- Condicion: La linea serviria para pasar una cotizacion a OC, vender bajo el precio de compra o aprobar una OV.
- Que pasa: Esos tres no se reabren. La cotizacion sigue como referencia. La OV se confirma al guardar.
- Que queda: OC con el orden de siempre, sin esos tres caminos.
- Rama: regresion

### CU-17. PDF de la OC al proveedor sin dimensiones

**Acuerdo.** 26/10 manana. El PDF que va al proveedor no lleva centro ni elemento. El detalle contable se ve en el sistema.

**Estado.** Parcial. Sigue como deuda: la auditoria no acredito que el PDF actual oculte las dimensiones.

**Quien.** Locutor no rotulado. Pista: el centro no le sirve al proveedor. `transcripcion-2026-10-26-presencial.md` [51:11] a [53:32].

**Que pasa.** Hay una hoja oficial para enviar y facturar, sin dimensiones. En el ERP se ve la cuenta, el centro y el elemento. Pidieron que lo descargable por defecto sea esa primera hoja. Una exportacion con detalle queda para uso interno, si se usa.

**Documento o pantalla.** PDF de la OC, y la vista de la OC en el sistema.

**Quien puede.** La sala no nombro el permiso. Dijeron que cada departamento se encarga de su OC [53:16].

**Limites.** El proveedor no recibe centro, elemento ni cuenta como dato de la hoja oficial.

**Que debe quedar.** Un PDF oficial sin dimensiones, y el detalle solo dentro del ERP.

**Documentacion antes de codear.** Que campos van al PDF y cuales no. Mensaje no hace falta si la descarga simplemente omite las dimensiones. Estado de la OC no cambia por exportar. Permiso no nombrado. Dato: ninguno nuevo; se omite centro, elemento y cuenta en el archivo enviado.

**Depende de.** CU-16. No se reabre el orden de los campos.

### Abanico

#### CU-17.1 PDF oficial sin dimensiones
- Condicion: Se descarga la hoja que va al proveedor.
- Que pasa: No lleva centro, elemento ni cuenta.
- Que queda: PDF oficial sin esas dimensiones. El estado de la OC no cambia.
- Rama: construir

#### CU-17.2 Detalle solo en el ERP
- Condicion: Quien compra revisa la OC por dentro.
- Que pasa: Ahi si se ven cuenta, centro y elemento.
- Que queda: Detalle en el sistema, no en la hoja enviada.
- Rama: construir

#### CU-17.3 Export interno con detalle
- Condicion: Hace falta una copia interna con dimensiones.
- Que pasa: Puede existir, distinta de la hoja oficial.
- Que queda: Dos salidas: oficial sin dimensiones, interna con detalle.
- Rama: construir

#### CU-17.4 PDF al proveedor con dimensiones
- Condicion: La hoja que se envia trae centro, elemento o cuenta.
- Que pasa: Esa no es la hoja oficial. La descarga por defecto las omite. No hace falta un mensaje si simplemente no van.
- Que queda: Proveedor sin dimensiones contables.
- Rama: no construir

### CU-18. Lupe baja la cartola del banco

**Acuerdo.** 26/10 manana. La cartola que se carga es el archivo que Lupe descarga del banco.

**Estado.** Completo. Regresion. No construir de nuevo. La carga de ese archivo quedo en CU-31 a CU-34.

**Quien.** Locutor no rotulado. Preguntan si el formato que mando Lupe sale directo del banco. Respuesta: directo al banco. `transcripcion-2026-10-26-presencial.md` [01:09:22] a [01:09:29].

**Que pasa.** No se pidio una conexion en linea al banco. Lupe baja el Excel del banco y ese archivo es el que entra. El banco limita el acceso de ejecutivo; eso no se resuelve en el ERP.

**Documento o pantalla.** Carga de cartola.

**Quien puede.** Lupe opera la descarga. La sala no nombro un permiso de sistema distinto.

**Limites.** El archivo no se rearma a mano antes de subirlo. No hay conector al banco en este acuerdo.

**Que debe quedar.** La importacion sigue recibiendo el archivo del banco, con las reglas del 28/10.

**Documentacion antes de codear.** No exige documento nuevo. No se agrega una integracion bancaria por esta frase.

**Depende de.** CU-31 a CU-34.

### Abanico

#### CU-18.1 Archivo bajado del banco
- Condicion: Lupe descarga la cartola y se carga ese archivo.
- Que pasa: Entra el Excel del banco, no uno rearmado a mano.
- Que queda: Cartola importada con las reglas del 28/10.
- Rama: regresion

#### CU-18.2 Conector en linea al banco
- Condicion: Se abre una integracion porque el ejecutivo del banco da poco acceso.
- Que pasa: Este acuerdo no la pidio. El limite del banco no se resuelve en el ERP.
- Que queda: Sin conector.
- Rama: regresion

#### CU-18.3 Archivo editado antes de subir
- Condicion: Alguien rearma columnas y lo carga como si fuera la bajada.
- Que pasa: La sala dijo que el formato va directo del banco.
- Que queda: Sin un segundo formato casero como fuente.
- Rama: regresion

### CU-19. La actividad manda, y la aprobacion esta en la proforma

**Acuerdo.** 26/10 tarde. La actividad manda y tiene muchas labores. La aprobacion va en la proforma, no en cada ingreso diario.

**Estado.** Parcial. La auditoria no acredita la cadena de la proforma. Se conserva la cadena de la OC de compras y que la OV se confirma al guardar, sin cadena.

**Quien.** Locutor no rotulado. Pista: operacion de contratistas. `transcripcion-2026-10-26-presencial-tarde.md` [06:05] a [07:18] y [23:28].

**Que pasa.** Una actividad agrupa muchas labores. La labor se puede repetir en actividades; la actividad no se duplica. En el ingreso diario se elige la labor y la actividad sale sola, porque en terreno se conoce la labor y no siempre la actividad. La persona confirma la proforma. No se aprueba cada ingreso diario: son muchos y frenaria la operacion.

**Documento o pantalla.** Parametrizacion de actividades y labores. Ingreso diario. Proforma.

**Quien puede.** La sala dijo que la proforma la confirma la persona, no el ingreso. No nombro el permiso de sistema. Jose Tomas, como jefe de abastecimiento, arma y aprueba la proforma: CU-25.

**Limites.** No se crea una cadena para la orden de venta. No se aprueba el ingreso diario uno a uno. La cadena de la OC de compras se conserva.

**Que debe quedar.** Actividad con N labores, ingreso diario sin cadena, y la aprobacion en la proforma.

**Documentacion antes de codear.** Como se asocia labor a actividad. Mensaje si se intenta aprobar el ingreso diario. Estados del ingreso (editable antes de la proforma) y de la proforma. Permiso de confirmar la proforma: la sala no lo dejo en un codigo. Dato: actividad, labores y proforma que agrupa los ingresos.

**Depende de.** CU-25 para quien aprueba.

### Abanico

#### CU-19.1 Actividad con muchas labores
- Condicion: Se parametriza la actividad.
- Que pasa: Agrupa muchas labores. La labor puede repetirse. La actividad no se duplica.
- Que queda: Actividad unica, con sus labores.
- Rama: construir

#### CU-19.2 Ingreso diario sin aprobacion
- Condicion: En terreno se conoce la labor y se registra el dia.
- Que pasa: Se elige la labor y la actividad sale sola. No se aprueba ese ingreso. Mensaje no nombrado por la sala si se intenta.
- Que queda: Ingreso editable antes de entrar a una proforma. Sin cadena.
- Rama: construir

#### CU-19.3 La proforma se confirma
- Condicion: Los ingresos ya estan agrupados en una proforma.
- Que pasa: La confirma la persona. Quien la arma y aprueba, en abastecimiento, es CU-25.
- Que queda: Proforma confirmada. Ingresos diarios sin cadena propia.
- Rama: construir

#### CU-19.4 Aprobar cada ingreso
- Condicion: Cada ingreso diario recorre una aprobacion.
- Que pasa: La sala lo descarto: son muchos y frenan la operacion.
- Que queda: Ingreso sin cadena.
- Rama: no construir

#### CU-19.5 Cadena en la OV, u OC sin la suya
- Condicion: Se mueve la aprobacion a la orden de venta, o se le quita a la OC de compras.
- Que pasa: La OV se confirma al guardar. La cadena de la OC de compras se conserva.
- Que queda: OV sin cadena. OC de compras con la suya.
- Rama: no construir

### CU-20. Al cierre entra solo el bloque aprobado

**Acuerdo.** 26/10 tarde. Al cierre entra el bloque de proformas aprobadas. Borrador e ingresos sueltos quedan informativos.

**Estado.** Parcial. La grilla de proformas del periodo esta en local. El bloque que entra contra el informativo no quedo reacreditado. El 03/11 precisa la factura del mes siguiente.

**Quien.** Locutor no rotulado, mostrando la pantalla. La sala de contratistas lo recorre. `transcripcion-2026-10-26-presencial-tarde.md` [24:57] y [51:12] a [51:29].

**Que pasa.** Una zona entra al cierre. Otra muestra proformas en borrador o sin aprobacion, y los ingresos diarios sin proforma. Esas no generan asiento. Entran las aprobadas; ese dia tambien se dicen las que ya tienen factura.

**Documento o pantalla.** Cierre de contratistas.

**Quien puede.** La sala no nombro el permiso de centralizar.

**Limites.** Borrador e ingreso suelto no entran al asiento. El 03/11: puede haber proforma de un mes y factura del siguiente, contra facturas por recibir. No se exige la factura del mismo mes para reconocer el gasto.

**Que debe quedar.** El asiento solo con el bloque que entra. Lo otro visible y fuera del asiento.

**Documentacion antes de codear.** Que marca el bloque que entra. Mensaje si se intenta centralizar un borrador. Estados: entra / solo informativo. Permiso no nombrado. Dato: proformas incluidas en el asiento del periodo.

**Depende de.** CU-05 y CU-21.

### Abanico

#### CU-20.1 Bloque que entra
- Condicion: La proforma esta aprobada y corresponde al cierre.
- Que pasa: Entra al asiento. La grilla del periodo, ya en local, no se reconstruye.
- Que queda: Proforma dentro del asiento del periodo.
- Rama: construir

#### CU-20.2 Borrador e ingreso suelto
- Condicion: Hay proformas sin aprobacion, en borrador, o ingresos sin proforma.
- Que pasa: Se ven y no generan asiento. Mensaje no nombrado por la sala si se intenta centralizarlas.
- Que queda: Estado solo informativo.
- Rama: construir

#### CU-20.3 Factura al mes siguiente
- Condicion: La proforma es de un mes y la factura del siguiente.
- Que pasa: El gasto del mes se reconoce igual. Lo que falta queda en facturas por recibir.
- Que queda: Gasto del mes. Puente abierto hasta la factura.
- Rama: construir

#### CU-20.4 Exigir la factura del mismo mes
- Condicion: Sin factura del mismo mes la proforma aprobada no entra.
- Que pasa: El 03/11 dejo de exigirla para reconocer el gasto.
- Que queda: Sin ese freno.
- Rama: no construir

### CU-21. Un asiento de centralizacion, y la factura cancela el puente

**Acuerdo.** 26/10 tarde. Un asiento de centralizacion del periodo. En libro de compras la factura cancela el puente de facturas por recibir.

**Estado.** Parcial. La auditoria no acredita ese asiento unico ni el auxiliar. El 27/10 pide agrupar el gasto por centro y poner RUT en facturas por recibir: CU-26.

**Quien.** Locutor no rotulado. Pista: explica donde se reconoce el gasto. `transcripcion-2026-10-26-presencial-tarde.md` [01:24:52] a [01:27:26].

**Que pasa.** Al aprobar la proforma se reconoce mano de obra contratista contra facturas por recibir. Centralizar genera un asiento con las proformas del periodo. La factura, en compras, cancela el puente y reconoce al proveedor. Si la factura cae al mes siguiente, el gasto ya quedo en el mes y facturas por recibir muestra lo que falta.

**Documento o pantalla.** Cierre de contratistas y libro de compras.

**Quien puede.** La sala no nombro el permiso. Contabilidad calza la factura: CU-25.

**Limites.** No se duplica el gasto en los dos modulos. El gasto nace en contratistas. La factura no nace ahi.

**Que debe quedar.** Un asiento del periodo, y la factura del libro dejando el puente en cero cuando calza.

**Documentacion antes de codear.** Cuentas del asiento. Mensaje si la factura no tiene proforma u OC, que es CU-42. Estado del puente. Permiso no nombrado. Dato: proformas del asiento y factura que lo cancela.

**Depende de.** CU-20, CU-26 y CU-42.

### Abanico

#### CU-21.1 Un asiento del periodo
- Condicion: Se centralizan las proformas que entran.
- Que pasa: Nace un asiento: mano de obra contratista contra facturas por recibir.
- Que queda: Un asiento con las proformas del periodo.
- Rama: construir

#### CU-21.2 La factura cancela el puente
- Condicion: La factura calza en libro de compras.
- Que pasa: Facturas por recibir se va contra el proveedor.
- Que queda: Puente en cero cuando calza.
- Rama: construir

#### CU-21.3 Factura que aun no llega
- Condicion: La factura cae al mes siguiente.
- Que pasa: El gasto ya quedo. El puente muestra lo que falta.
- Que queda: Gasto del mes y puente abierto.
- Rama: construir

#### CU-21.4 Gasto reconocido otra vez en compras
- Condicion: El libro de compras vuelve a reconocer el gasto de la proforma.
- Que pasa: El gasto nace en contratistas. La factura no nace ahi.
- Que queda: Sin segundo gasto.
- Rama: no construir

#### CU-21.5 Un asiento por proforma
- Condicion: Centralizar abre un comprobante por cada proforma.
- Que pasa: La sala dijo un asiento con las proformas del periodo.
- Que queda: Sigue siendo un asiento.
- Rama: no construir

### CU-22. La correccion sale del documento, no de reabrir el mes

**Acuerdo.** 26/10 tarde. La solicitud de reverso sale del documento, no de reabrir el mes. La matriz agrega que no se reversa un mes intermedio si los posteriores estan cerrados.

**Estado.** Parcial. En local el periodo cerrado no se reabre y la correccion de la proforma abre motivo y dos vistos buenos. Falta que el resultado sea editar la linea: CU-59. No se construye una cascada de meses.

**Quien.** Locutor no rotulado. Pista: contabilidad y quien pide abrir un mes. `transcripcion-2026-10-26-presencial-tarde.md` [01:30:48] a [01:31:40] y [01:33:22] a [01:34:14].

**Que pasa.** El usuario pide la correccion desde la proforma o desde la factura, no desde un boton de reabrir el mes. Si la proforma tiene factura, primero se suelta la factura. La frase de "reversar todos los meses hasta mayo" es el sistema que usan hoy. La sala pregunta si esta bien y se inclina a corregir solo el mes del error, porque el gasto no corre al mes siguiente. No dejo cerrada una regla de cascada. No se construye esa cascada.

**Documento o pantalla.** Solicitud desde la proforma o la factura. No un reabrir mes.

**Quien puede.** La sala habla de notificacion a contabilidad y de quien abre. El permiso concreto de los dos vistos buenos queda en CU-38.

**Limites.** No se reabre el periodo. No se emite un asiento nuevo: eso lo pisa CU-59. No se reversa en cascada un mes intermedio.

**Que debe quedar.** La correccion nace en el documento. El mes permanece cerrado.

**Documentacion antes de codear.** Desde que documento se pide. Mensaje si el periodo esta cerrado y alguien busca la clave de reapertura. Estado de la solicitud. Permiso: CU-38. Dato: documento, motivo y quien pidio.

**Depende de.** CU-38 y CU-59. No depende de CU-24 ni de CU-39: esos no se construyen.

### Abanico

#### CU-22.1 Pedido desde el documento
- Condicion: Hay que corregir una proforma o una factura ya cerrada.
- Que pasa: La solicitud sale de ese documento. En local abre motivo y dos vistos buenos.
- Que queda: Solicitud con documento, motivo y quien pidio. Mes cerrado.
- Rama: regresion

#### CU-22.2 Reabrir el mes
- Condicion: Alguien busca la clave o un boton para reabrir el periodo.
- Que pasa: No se reabre. Mensaje no nombrado por la sala.
- Que queda: Periodo cerrado.
- Rama: regresion

#### CU-22.3 Cascada hasta el mes viejo
- Condicion: Para tocar mayo habria que reversar junio, julio y agosto.
- Que pasa: La sala no cerro esa cascada. Se inclino a corregir el mes del error.
- Que queda: Sin reversa en cascada.
- Rama: no construir

#### CU-22.4 Asiento nuevo de la correccion
- Condicion: La solicitud genera un comprobante de ajuste o de reversa.
- Que pasa: El 05/11 piso ese resultado.
- Que queda: Sin asiento nuevo. Gana CU-59.
- Rama: no construir. Gana CU-59

#### CU-22.5 Primero se suelta la factura
- Condicion: La proforma que se corrige ya tiene factura.
- Que pasa: Antes de corregir se suelta la factura.
- Que queda: Factura libre y correccion pedida desde la proforma.
- Rama: construir

### CU-23. Planta fuera, e historial antes / despues

**Acuerdo.** 26/10 tarde. Planta no se usa. El historial de parametrizacion muestra antes y despues, sin metadatos al usuario.

**Estado.** Parcial. Planta ya quedo fuera del plan de cuentas. El historial sigue como deuda de presentacion.

**Quien.** Locutor no rotulado. "Planta no la usamos." Sobre el historial, otro locutor dice que el metadato es muy tecnico. `transcripcion-2026-10-26-presencial-tarde.md` [03:39] y [49:04] a [49:34].

**Que pasa.** Planta no se pide al imputar. Variedad puede quedar en el maestro, pero no es este caso. Cuando se cambia un parametro, el usuario ve el valor anterior y el nuevo, la fecha y quien lo hizo. No ve nombres de campos de base.

**Documento o pantalla.** Plan de cuentas sin planta. Historial de un cambio de parametrizacion.

**Quien puede.** La sala no nombro el permiso.

**Limites.** Planta no vuelve al comprobante ni a la cuenta. El historial no muestra metadatos tecnicos.

**Que debe quedar.** Imputacion sin planta, e historial legible de antes y despues.

**Documentacion antes de codear.** Que cambio se historifica. Mensaje no hace falta si el historial simplemente omite el metadato. Estado del parametro vigente. Permiso no nombrado. Dato: valor anterior, valor nuevo, fecha y usuario.

**Depende de.** Ninguno.

### Abanico

#### CU-23.1 Imputar sin planta
- Condicion: Se usa una cuenta o un comprobante.
- Que pasa: Planta no se pide. Ya quedo fuera del plan.
- Que queda: Sin planta.
- Rama: regresion

#### CU-23.2 Historial antes y despues
- Condicion: Cambia un parametro.
- Que pasa: Se ve el valor anterior, el nuevo, la fecha y quien. No los nombres de campos de base.
- Que queda: Historial legible. Parametro vigente actualizado.
- Rama: construir

#### CU-23.3 Planta de vuelta
- Condicion: La imputacion vuelve a pedir planta.
- Que pasa: La sala dijo que no la usan.
- Que queda: Sin planta en la cuenta ni en el comprobante.
- Rama: no construir

#### CU-23.4 Metadatos al usuario
- Condicion: El historial muestra nombres tecnicos de la base.
- Que pasa: La sala los encontro demasiado tecnicos.
- Que queda: Historial sin metadatos.
- Rama: no construir

### CU-24. Ajuste en mes cerrado y reversa en mes abierto

**Acuerdo.** 27/10 manana. En mes abierto se reversa. En mes cerrado se hace un ajuste, con dos vistos buenos, sin reabrir el mes.

**Estado.** Pisado. No construir. La regla que gana es CU-59.

**Quien.** Locutor no rotulado. Pista: contabilidad de contratistas. Nombran a Jose Tomas. `transcripcion-2026-10-27-reunion.md` [58:44] a [01:00:28] y [01:06:09].

**Que pasa.** Ese dia, si el mes sigue abierto y no se centralizo, se suelta la factura y se edita. Si ya esta cerrado, hablaron de un comprobante de ajuste y tambien de modificar solo la linea con historial y dos aprobaciones (contratistas y contabilidad), sin abrir el mes. El 05/11 elimino el asiento nuevo. Los dos vistos buenos y el no reabrir siguen en CU-38.

**Documento o pantalla.** No se construye el asiento de ajuste ni el de reversa de esta correccion.

**Quien puede.** Los dos vistos buenos quedan en CU-38, no en un asiento nuevo.

**Limites.** No reabrir el mes. No nacer otro comprobante por esta correccion.

**Que debe quedar.** Nada del asiento de ajuste. La linea editada es CU-59.

**Documentacion antes de codear.** No exige documento del flujo viejo.

**Depende de.** CU-59.

### Abanico

#### CU-24.1 Comprobante de ajuste en mes cerrado
- Condicion: El mes ya esta cerrado y se corrige con un asiento de ajuste.
- Que pasa: El 05/11 elimino ese comprobante nuevo.
- Que queda: Sin asiento de ajuste. Gana CU-59.
- Rama: no construir. Gana CU-59

#### CU-24.2 Asiento de reversa de la correccion
- Condicion: En mes abierto o cerrado la correccion nace como reversa contable nueva.
- Que pasa: Tampoco se construye ese asiento.
- Que queda: Sin asiento de reversa. Gana CU-59.
- Rama: no construir. Gana CU-59

#### CU-24.3 Reabrir el mes para poder editar
- Condicion: Para corregir se abre el periodo.
- Que pasa: El no reabrir sigue, pero en CU-38, no como este flujo viejo.
- Que queda: Mes sin reapertura. Los dos vistos buenos viven en CU-38.
- Rama: no construir. Gana CU-59

### CU-25. Jose Tomas arma la proforma y contabilidad calza la factura

**Acuerdo.** 27/10 manana. Jose Tomas arma y aprueba la proforma. Contabilidad calza la factura por monto y RUT.

**Estado.** Parcial. El calce con aviso verde y el aviso al creador siguen abiertos en la auditoria: CU-41.

**Quien.** Locutor no rotulado. Nombra a Jose Tomas como jefe de abastecimiento. `transcripcion-2026-10-27-reunion.md` [47:10] a [48:13].

**Que pasa.** Jose Tomas emite la proforma de contratistas. Contabilidad revisa que el monto y el proveedor de la factura coincidan, y recien ahi asocia. Si hay que editar la proforma ya asociada, contabilidad suelta la factura. La proforma no pasa sola a editable: CU-38 y CU-59.

**Documento o pantalla.** Proforma de contratistas y asociacion en compras.

**Quien puede.** Jose Tomas: arma y aprueba la proforma. Contabilidad: calza monto y RUT. La sala no dio un codigo de permiso.

**Limites.** Contabilidad no rearma la proforma. No se asocia si monto o RUT no calzan, sin el aviso de CU-41.

**Que debe quedar.** Proforma aprobada por quien abastece, y factura asociada solo cuando monto y RUT calzan.

**Documentacion antes de codear.** Quien ve el boton de aprobar y quien ve el de asociar. Mensaje si monto o RUT no coinciden. Estados de la proforma y de la factura asociada. Permiso separado de abastecimiento y de contabilidad, sin codigo dicho. Dato: monto y RUT comparados.

**Depende de.** CU-19 y CU-41.

### Abanico

#### CU-25.1 Jose Tomas arma y aprueba
- Condicion: Hay ingresos de contratistas para cerrar en una proforma.
- Que pasa: Jose Tomas, jefe de abastecimiento, la emite y la aprueba.
- Que queda: Proforma aprobada por abastecimiento.
- Rama: construir

#### CU-25.2 Contabilidad calza monto y RUT
- Condicion: Llega la factura y monto y proveedor coinciden.
- Que pasa: Contabilidad asocia. No rearma la proforma.
- Que queda: Factura asociada.
- Rama: construir

#### CU-25.3 Monto o RUT distintos
- Condicion: La factura no coincide en monto o en RUT.
- Que pasa: No se asocia en silencio. El aviso es el de CU-41. Mensaje no nombrado por la sala en este caso.
- Que queda: Factura sin asociar. Proforma como estaba.
- Rama: construir

#### CU-25.4 Proforma asociada, se suelta la factura
- Condicion: Hay que editar una proforma que ya tiene factura.
- Que pasa: Contabilidad suelta la factura. La proforma no pasa sola a editable.
- Que queda: Factura suelta. La edicion sigue en CU-38 y CU-59.
- Rama: construir

#### CU-25.5 Contabilidad edita la proforma a sola
- Condicion: Contabilidad cambia la proforma ya asociada sin soltar la factura ni pasar por CU-38 y CU-59.
- Que pasa: No la rearma.
- Que queda: Proforma sin esa edicion directa.
- Rama: no construir

### CU-26. El cierre agrupa por centro, y facturas por recibir lleva RUT

**Acuerdo.** 27/10 manana. El asiento de cierre agrupa el gasto por centro de costo. Facturas por recibir lleva auxiliar (RUT).

**Estado.** Faltante. La matriz dice que no estaba en el corte anterior. La auditoria no lo da por hecho.

**Quien.** Locutor no rotulado. Explica el asiento de mano de obra. `transcripcion-2026-10-27-reunion.md` [56:11] a [57:16]. La minuta ubica el detalle de la grilla en [01:11:29] a [01:13:47]; en el archivo de la manana el tramo de auxiliar de la grilla no quedo en una frase tan cerrada como el asiento de [57:05]. Se usa [57:05] a [57:16]. El minuto fino de la grilla: minuto no ubicado si no coincide con esa frase.

**Que pasa.** Al centralizar, el gasto de mano de obra contratista queda contra facturas por recibir, y se puede ver que falta la factura de un contratista. La sala pidio ver ese gasto agrupado por centro, y el auxiliar del puente con el RUT del contratista.

**Documento o pantalla.** Asiento del cierre de contratistas.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se abre un asiento por cada proforma: es el asiento del periodo, con lineas agrupadas. El RUT es el auxiliar, no un texto suelto en la glosa.

**Que debe quedar.** Lineas de gasto por centro, y facturas por recibir con el RUT.

**Documentacion antes de codear.** Como se agrupa. Mensaje si una proforma del bloque no tiene centro. Estado del asiento del periodo. Permiso no nombrado. Dato: centro en la linea de gasto y RUT en el puente.

**Depende de.** CU-21.

### Abanico

#### CU-26.1 Gasto agrupado por centro
- Condicion: El cierre trae varias proformas con centros distintos.
- Que pasa: El asiento del periodo agrupa el gasto por centro. No abre un comprobante por proforma.
- Que queda: Lineas de gasto por centro.
- Rama: construir

#### CU-26.2 Auxiliar en el puente
- Condicion: Facturas por recibir muestra que falta la factura de un contratista.
- Que pasa: El puente lleva el RUT como auxiliar, no como texto suelto en la glosa.
- Que queda: RUT en el auxiliar del puente.
- Rama: construir

#### CU-26.3 Proforma del bloque sin centro
- Condicion: Una proforma que entra no tiene centro.
- Que pasa: No se inventa el centro. Mensaje no nombrado por la sala.
- Que queda: Esa linea no queda agrupada sin centro.
- Rama: construir

#### CU-26.4 Un asiento por cada proforma
- Condicion: Centralizar parte el cierre en un comprobante por proforma.
- Que pasa: La sala pidio el asiento del periodo, con lineas agrupadas.
- Que queda: Sigue un asiento.
- Rama: no construir

### CU-27. Balance de 8 columnas

**Acuerdo.** 27/10 tarde. Balance de 8 columnas.

**Estado.** Completo. Regresion. No construir de nuevo. El rango desde el 1 de enero hasta el periodo quedo en codigo local esta semana.

**Quien.** Locutor no rotulado. Recorre el informe. `transcripcion-2026-10-27-reunion-tarde.md` [05:05]. El desarrollo del informe en la minuta va de [04:20] a [09:20]. La frase "hay ocho columnas" esta en [05:05].

**Que pasa.** El balance de 8 se emite del ano en curso, desde el 1 de enero hasta el periodo elegido. No se rearma el ER del mes ni el ESF: esos son CU-13.

**Documento o pantalla.** Contabilidad > balance 8.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No cruza a otro ano dentro del mismo balance. Eso ya lo dijo el 22/10 para este reporte: CU-09.

**Que debe quedar.** El balance de 8 del 1 de enero al periodo.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca, no se cambia el rango.

**Depende de.** CU-09 solo como limite de ano. No se reconstruye.

### Abanico

#### CU-27.1 Del 1 de enero al periodo
- Condicion: Se emite el balance de 8 del ano en curso.
- Que pasa: Parte el 1 de enero y llega al periodo elegido.
- Que queda: Balance de 8 de ese rango.
- Rama: regresion

#### CU-27.2 Cruce a otro ano
- Condicion: El mismo balance pide otro ano.
- Que pasa: No se cambia el rango. Sigue el limite de CU-09.
- Que queda: Sin balance cruzado.
- Rama: regresion

#### CU-27.3 Rearmar ER o ESF aqui
- Condicion: Este informe se usa para rehacer el resultado del mes o la situacion financiera.
- Que pasa: Esos dos son CU-13. Este caso no los toca.
- Que queda: Balance de 8 solo.
- Rama: regresion

### CU-28. Nota de cobro del embarcador y de Asoex

**Acuerdo.** 27/10 tarde. Notas de cobro de embarcador y de Asoex.

**Estado.** Parcial. En local estan las notas una a una, sin carga Excel, y la auditoria dice que la sala posterior no lo piso. En esta transcripcion la sala tambien pidio poder ingresarlas por proveedores cuando son muchas. Eso no esta. Por eso no queda Completo.

**Quien.** Locutor no rotulado. Pista: explica OPB y Asoex. `transcripcion-2026-10-27-reunion-tarde.md` [15:35] a [18:14], [34:00] y [37:05] a [38:16].

**Que pasa.** Hay dos notas. La de gasto (Asoex) se ingresa como documento y reconoce gasto contra proveedor. La del embarcador (OPB) no es gasto nuevo: un tercero pago facturas que ya estan en el sistema, y la nota se calza con esas facturas, se rebaja la deuda de cada proveedor y se reconoce la deuda con el tercero. La nota se asocia a las facturas que trae. Hoy lo hacen con un Excel, a veces de cientos de filas al inicio de temporada, y dijeron que hacerlo en proveedores seria mejor porque el asiento del haber sale solo.

**Documento o pantalla.** Compras > notas de cobro.

**Quien puede.** La sala no nombro el permiso. Dijeron que compras y tesoreria se tocan en el pago al tercero.

**Limites.** Si no calza, no pasa [21:47] a [21:51]. No se contabiliza la nota del embarcador como un gasto duplicado. La sala no fijo un maximo de facturas por nota. El ejemplo de 400 filas es volumen, no un tope.

**Que debe quedar.** Nota de gasto directo, y nota de tercero calzada  con sus facturas. La carga masiva en proveedores queda como la parte faltante, no como un segundo documento.

**Documentacion antes de codear.** Los dos tipos de nota. Mensaje si una factura de la nota no existe o el total no cuadra. Estado calzada o pendiente. Permiso no nombrado. Dato: tercero, facturas asociadas y tipo (gasto o reembolso).

**Depende de.** Ninguno.

### Abanico

#### CU-28.1 Asoex, gasto directo
- Condicion: La nota cobra un gasto, una a una.
- Que pasa: Se ingresa como documento y reconoce gasto contra proveedor. Eso ya esta en local.
- Que queda: Nota de gasto. Estado calzada o pendiente segun corresponda.
- Rama: regresion

#### CU-28.2 Embarcador, facturas que un tercero pago
- Condicion: OPB pago facturas que ya estan en el sistema.
- Que pasa: La nota se calza con esas facturas, se rebaja cada proveedor y se reconoce la deuda con el tercero. Una a una, ya en local.
- Que queda: Nota de reembolso calzada, sin gasto duplicado.
- Rama: regresion

#### CU-28.3 No calza
- Condicion: Una factura de la nota no existe o el total no cuadra.
- Que pasa: No pasa. Mensaje no nombrado por la sala.
- Que queda: Nota sin contabilizar. Facturas como estaban.
- Rama: regresion

#### CU-28.4 Muchas filas por proveedores
- Condicion: La temporada trae muchas facturas y hoy las cargan por contabilidad.
- Que pasa: La sala pidio poder hacerlo en proveedores, porque el haber sale solo. Eso no esta.
- Que queda: Carga en proveedores, no un segundo tipo de nota.
- Rama: construir

#### CU-28.5 Embarcador contabilizado como gasto nuevo
- Condicion: La nota del tercero vuelve a reconocer el gasto de facturas ya ingresadas.
- Que pasa: Eso duplica el gasto. No es este acuerdo.
- Que queda: Sin gasto duplicado.
- Rama: no construir

### CU-29. La OC puede ser de activo fijo

**Acuerdo.** 27/10 tarde. La OC puede ser de activo fijo. Lo pidio Agustin, relatado en la sala.

**Estado.** Parcial. El tipo de OC existe como dato. El alta del maestro no sale todavia de la OC recepcionada: CU-58. No se construye el camino "activo sin OC" que ese dia tambien se nombro.

**Quien.** Locutor no rotulado. "Lo que si pidio Agustin". Agustin no esta nombrado como presente. `transcripcion-2026-10-27-reunion-tarde.md` [25:04] a [28:22].

**Que pasa.** El activo deja de entrar solo por contabilidad. La OC lleva tipo activo fijo. El bien se crea desde esa orden, no al tipear el tipo. En el mismo tramo hablaron de crear el activo sin OC y asociarlo despues. El 05/11 cerro esa puerta: CU-58.

**Documento o pantalla.** OC con tipo activo fijo. El maestro espera a CU-58.

**Quien puede.** La sala no nombro el permiso. La OC de compras sigue con su cadena.

**Limites.** No se crea el bien al marcar el tipo. No se crea sin OC. Se conservan, desde el 21/10, vida util unica en meses, sin centro de costo en el alta, e IPC: CU-58.

**Que debe quedar.** OC marcada como activo fijo, sin maestro todavia.

**Documentacion antes de codear.** El tipo en la OC. Mensaje si se intenta alta sin recepcion: CU-58. Estado de la OC. Permiso el de la OC. Dato: tipo activo fijo en la orden.

**Depende de.** CU-58 para el alta. CU-04 no se construye.

### Abanico

#### CU-29.1 OC de tipo activo fijo
- Condicion: Se crea la orden y se marca activo fijo.
- Que pasa: El tipo queda en la OC. El maestro no nace al marcar ni al guardar.
- Que queda: OC con el tipo, sin bien creado.
- Rama: regresion

#### CU-29.2 Alta al marcar el tipo o al guardar
- Condicion: Elegir activo fijo, o guardar la OC, crea el maestro.
- Que pasa: El 05/11 lo cerro.
- Que queda: Sin maestro en ese momento. Gana CU-58.
- Rama: no construir. Gana CU-58

#### CU-29.3 Activo sin OC
- Condicion: Se crea el bien y la OC se asocia despues, como se nombro el 27/10.
- Que pasa: El 05/11 cerro esa puerta.
- Que queda: Sin alta sin OC. Gana CU-58.
- Rama: no construir. Gana CU-58

### CU-30. Boleta de honorarios: se registra, no se emite

**Acuerdo.** 27/10 tarde. Boleta de honorarios de registro y recepcion, no de emision.

**Estado.** Faltante. La auditoria dice que no se cerro en este corte.

**Quien.** Locutor no rotulado. Hablan de notaria, retencion y de ingresar la boleta cuando alguien la rinde. `transcripcion-2026-10-27-reunion-tarde.md` [54:13] a [54:27] y [01:03:36] a [01:04:23].

**Que pasa.** La boleta llega de un tercero (notaria, abogado). Se registra cuando se rinde. Si nadie la rinde, no se ingresa, porque quedaria pendiente para siempre. No se emite desde el ERP. Mencionaron codigos con y sin retencion y despues dudaron de los numeros. Esos numeros no quedan como ley.

**Documento o pantalla.** Registro de boleta de honorarios recibida.

**Quien puede.** La sala no nombro el permiso. Dijeron que la ingresa contabilidad cuando hay rendicion.

**Limites.** No es emision. No se carga la que nadie rindio. El factor de la boleta es CU-07. La sala no cerro la tasa.

**Que debe quedar.** Una boleta recibida, asociada a quien la rindio, sin folio emitido por Almahue.

**Documentacion antes de codear.** Alta de boleta recibida. Mensaje si se intenta emitir. Estado pendiente de rendicion o ingresada. Permiso no nombrado. Dato: emisor, monto, si tiene retencion, y quien la rindio.

**Depende de.** CU-07 para el factor, no para existir el registro.

### Abanico

#### CU-30.1 Se registra cuando se rinde
- Condicion: Notaria o un abogado emitio la boleta y alguien la rinde.
- Que pasa: Contabilidad la ingresa como recibida. Puede ir con retencion o sin ella. El codigo numerico no queda de ley.
- Que queda: Boleta ingresada, asociada a quien la rindio, sin folio emitido por Almahue.
- Rama: construir

#### CU-30.2 Nadie la rinde
- Condicion: La boleta queda en el aire y nadie la rinde.
- Que pasa: No se ingresa: quedaria pendiente para siempre.
- Que queda: Estado pendiente de rendicion, sin documento cargado.
- Rama: construir

#### CU-30.3 Emitirla desde el ERP
- Condicion: Se intenta emitir la boleta de honorarios.
- Que pasa: Este acuerdo es recepcion, no emision. Mensaje no nombrado por la sala.
- Que queda: Sin folio de emision.
- Rama: no construir

#### CU-30.4 Codigos que la sala dudo
- Condicion: Se fijan 1001, 1002 o 1003 porque se nombraron y despues se dudaron.
- Que pasa: Esos numeros no quedan como ley. La tasa es CU-07.
- Que queda: Sin codigo ni tasa inventados.
- Rama: no construir

### CU-31. La cartola del mes no duplica al recargarla

**Acuerdo.** 28/10. La cartola del mes se carga varias veces y no puede duplicar movimientos.

**Estado.** Completo. Regresion. No construir de nuevo. La auditoria lo da por hecho: fecha, signo, monto y referencia o glosa.

**Quien.** Locutor no rotulado. Carlos plantea la duplicidad y la sala confirma que no se duplica. Pista: tesoreria con Lupe. `transcripcion-2026-10-28-reunion.md` [02:18:16] a [02:18:35].

**Que pasa.** La cartola se carga por semana y el archivo trae otra vez lo ya subido. El movimiento ya cargado no se crea de nuevo.

**Documento o pantalla.** Carga de cartola.

**Quien puede.** La sala no nombro el permiso. La opera Lupe: CU-18.

**Limites.** No se borra el movimiento ya contabilizado para "limpiar" el duplicado. Se omite el repetido.

**Que debe quedar.** Una sola fila por movimiento, aunque el archivo del mes se suba de nuevo.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca la carga, no se vuelven a insertar los movimientos ya reconocidos.

**Depende de.** CU-18.

### Abanico

#### CU-31.1 Segunda carga del mes
- Condicion: La cartola semanal trae otra vez un movimiento ya subido.
- Que pasa: No se crea de nuevo. Se reconoce por fecha, signo, monto y referencia o glosa.
- Que queda: Una sola fila.
- Rama: regresion

#### CU-31.2 Borrar para limpiar el duplicado
- Condicion: Se elimina el movimiento ya contabilizado porque el archivo lo repite.
- Que pasa: No se borra. Se omite el repetido.
- Que queda: El contabilizado sigue.
- Rama: regresion

#### CU-31.3 Insertar el repetido
- Condicion: La segunda carga agrega la misma fila.
- Que pasa: No se inserta.
- Que queda: Sigue una fila.
- Rama: regresion

### CU-32. Linea del mes anterior, y archivo de otro periodo

**Acuerdo.** 28/10. Se excluye la linea del mes anterior que viaja al final del archivo, y se avisa si el archivo no es del periodo.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado. Confirman "se excluye". `transcripcion-2026-10-28-reunion.md` [02:17:23] a [02:18:01].

**Que pasa.** Si el periodo abierto es octubre y el archivo es de junio, se avisa de inmediato. La ultima linea que corresponde al mes anterior no entra.

**Documento o pantalla.** Carga de cartola, aviso antes de guardar.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se carga en silencio un archivo de otro mes. La linea de arrastre del mes previo no genera movimiento.

**Que debe quedar.** Aviso de periodo, y esa linea fuera.

**Documentacion antes de codear.** No exige documento nuevo. El aviso de periodo no se quita.

**Depende de.** CU-31.

### Abanico

#### CU-32.1 Archivo de otro periodo
- Condicion: El periodo abierto no es el del archivo.
- Que pasa: Se avisa de inmediato, antes de guardar.
- Que queda: Sin carga silenciosa.
- Rama: regresion

#### CU-32.2 Linea del mes anterior
- Condicion: Al final del archivo viaja el movimiento del mes previo.
- Que pasa: No genera movimiento.
- Que queda: Esa linea fuera.
- Rama: regresion

#### CU-32.3 Carga silenciosa
- Condicion: El archivo de otro mes entra sin aviso, o la linea de arrastre entra.
- Que pasa: No es la regla que ya esta.
- Que queda: Aviso presente y linea de arrastre fuera.
- Rama: regresion

### CU-33. Partir un ingreso en dos o tres codigos

**Acuerdo.** 28/10. Un ingreso se parte en 2 o 3 codigos financieros, en la moneda de origen, sin pasar el monto.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado. Ejemplo cereza y nectarina. `transcripcion-2026-10-28-reunion.md` [02:23:57] a [02:25:36].

**Que pasa.** Un abono trae mas de un destino. Se agregan partes, cada una con su codigo financiero y su monto, en la misma moneda del movimiento (dolar con dolar, yuan con yuan). No se convierte. La suma no puede pasar el total, y no puede quedar un saldo sin asignar.

**Documento o pantalla.** Contabilizacion del ingreso en la cartola.

**Quien puede.** La sala no nombro el permiso.

**Limites.** Hasta tres partes: "hasta tres me han tocado" [02:25:26]. Moneda de origen. Suma igual al movimiento.

**Que debe quedar.** Un ingreso partido, cuadrado, sin conversion.

**Documentacion antes de codear.** No exige documento nuevo. No se agrega una cuarta parte ni una conversion por este caso.

**Depende de.** CU-31.

### Abanico

#### CU-33.1 Dos o tres partes, misma moneda
- Condicion: Un ingreso trae dos destinos, o tres.
- Que pasa: Se parte en codigos financieros, en la moneda de origen. La suma iguala el total.
- Que queda: Ingreso cuadrado, sin conversion.
- Rama: regresion

#### CU-33.2 Suma que se pasa o que deja saldo
- Condicion: Las partes superan el movimiento, o queda un resto sin codigo.
- Que pasa: No se guarda.
- Que queda: Sin partida descuadrada.
- Rama: regresion

#### CU-33.3 Convertir al partir
- Condicion: Dolares o yuanes se pasan a otra moneda para imputar.
- Que pasa: No se convierte. Dolar con dolar, yuan con yuan.
- Que queda: Partes en la moneda del movimiento.
- Rama: regresion

#### CU-33.4 Cuarta parte
- Condicion: El ingreso se abre en cuatro codigos.
- Que pasa: La sala dijo que le han tocado hasta tres.
- Que queda: Sin cuarta parte.
- Rama: regresion

### CU-34. Nombre de la cuenta junto al numero

**Acuerdo.** 28/10. El nombre de la cuenta se ve junto al numero.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado. Pide un nombre para distinguir cuentas del mismo banco. `transcripcion-2026-10-28-reunion.md` [02:15:47] a [02:16:34].

**Que pasa.** Al ver la cuenta bancaria aparece el numero y un nombre. La sala dijo que hoy hay una cuenta corriente por banco, y que la diferencia real es la moneda: peso, dolar o yuan.

**Documento o pantalla.** Cuenta bancaria en tesoreria.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se inventan mas cuentas por banco. El nombre es para leer el numero, no un segundo identificador contable.

**Que debe quedar.** Numero y nombre visibles.

**Documentacion antes de codear.** No exige documento nuevo.

**Depende de.** Ninguno.

### Abanico

#### CU-34.1 Numero y nombre
- Condicion: Se mira la cuenta bancaria.
- Que pasa: Se ve el numero y el nombre.
- Que queda: Los dos visibles.
- Rama: regresion

#### CU-34.2 El nombre como otra cuenta
- Condicion: El nombre se usa como segundo identificador contable, o se inventa otra cuenta corriente del mismo banco.
- Que pasa: La sala dijo una cuenta por banco. La diferencia dicha es la moneda: peso, dolar o yuan.
- Que queda: Nombre solo para leer el numero. Sin cuenta extra.
- Rama: regresion

#### CU-34.3 Solo el numero
- Condicion: La cuenta se muestra sin nombre.
- Que pasa: Deja de distinguirse.
- Que queda: El nombre sigue al lado.
- Rama: regresion

### CU-35. La devolucion usa el precio de la guia, no el promedio

**Acuerdo.** 28/10. La devolucion al proveedor se valoriza al precio de la guia o de la factura, no al promedio.

**Estado.** Parcial. El precio de la guia o factura ya se toma en la salida. Falta no rebajar el stock de esa guia, y el documento nuevo: CU-56.

**Quien.** Locutor no rotulado. Pista: bodega. Dicen que el consumo va a promedio y que la devolucion no puede. `transcripcion-2026-10-28-reunion.md` [01:37:45] a [01:38:42].

**Que pasa.** El consumo de bodega sigue a precio promedio. La devolucion busca la guia o la factura de llegada y usa ese precio, para que la nota de credito del proveedor calce. El 05/11 precisa que esa busqueda no mueve el stock de la guia.

**Documento o pantalla.** Salida por devolucion a proveedor, en insumos.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se valoriza la devolucion al promedio. El consumo no pasa a FIFO. La palabra merma salio en esa sala como tipo de movimiento del sistema actual [01:40:06]. No se crea merma.

**Que debe quedar.** Devolucion valorizada al precio de origen. El stock de la guia origen no se toca: CU-56.

**Documentacion antes de codear.** De que documento sale el precio. Mensaje si no hay guia ni factura de origen. Estado del documento de salida. Permiso no nombrado. Dato: guia o factura de origen y el precio copiado.

**Depende de.** CU-56 completa la mitad que falta. CU-55 deja el consumo en promedio.

### Abanico

#### CU-35.1 Precio de la guia o de la factura
- Condicion: Se devuelve mercaderia y se conoce la guia o la factura de llegada.
- Que pasa: La salida toma ese precio, no el promedio. Esa mitad ya esta.
- Que queda: Devolucion valorizada al precio de origen.
- Rama: regresion

#### CU-35.2 Sin guia ni factura de origen
- Condicion: No hay documento de llegada para copiar el precio.
- Que pasa: No se inventa el precio. Mensaje no nombrado por la sala.
- Que queda: Sin devolucion valorizada al promedio por este hueco.
- Rama: construir

#### CU-35.3 Devolucion al promedio, consumo a FIFO o merma
- Condicion: La devolucion usa el promedio, el consumo pasa a FIFO, o se abre un movimiento de merma.
- Que pasa: Ninguno de los tres es este acuerdo.
- Que queda: Devolucion fuera del promedio. Consumo en CU-55. Sin merma.
- Rama: no construir

#### CU-35.4 Rebajar el stock de esa guia
- Condicion: Copiar el precio tambien descuenta la existencia de la guia.
- Que pasa: El 05/11 dijo que esa guia no se mueve.
- Que queda: Guia sin rebaja. Gana CU-56.
- Rama: no construir. Gana CU-56

### CU-36. Proyectado de tesoreria

**Acuerdo.** 28/10, retomado el 05/11. Proyectado de tesoreria, comentario de Lupe.

**Estado.** Espera. Reunion con Lupe. No esta el diseno.

**Quien.** El 05/11 Maria Jesus recuerda el comentario de Lupe. Lupe no esta en esa sala. `transcripcion-2026-11-05-reunion.md` [02:42:01] a [02:42:47]. En la transcripcion del 28/10 no ubique la palabra proyectado: minuto no ubicado en ese archivo.

**Que pasa.** Lupe pidio, en un comentario, sumar un proyectado. El 05/11 se agenda para el lunes, con Lupe y Agustin. No dijeron columnas, horizonte ni de que saldos sale.

**Documento o pantalla.** Ninguno hasta esa reunion.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se disena el proyectado en este corte. No se paga ni se contabiliza nada para "ver como se veria".

**Que debe quedar.** El caso anotado, sin pantalla.

**Documentacion antes de codear.** No se documenta pantalla, mensaje, estado ni dato hasta la reunion con Lupe.

**Depende de.** Ninguno. No bloquea la cartola ya hecha.

### Abanico

#### CU-36.1 Pantalla de proyectado
- Condicion: Se adelanta el modulo antes de la reunion con Lupe.
- Que pasa: No hay columnas, horizonte ni saldos dichos. No se codea.
- Que queda: Sin pantalla.
- Rama: no construir

#### CU-36.2 Columnas u horizonte inventados
- Condicion: Se elige un diseno para no llegar vacios a la reunion.
- Que pasa: La sala no los dijo.
- Que queda: Sin diseno.
- Rama: no construir

#### CU-36.3 Pagar o contabilizar para verlo
- Condicion: Se registra un pago o un asiento para simular el proyectado.
- Que pasa: Este acuerdo lo prohibe.
- Que queda: Sin pago y sin asiento de prueba.
- Rama: no construir

#### CU-36.4 La cartola no se frena
- Condicion: La espera del proyectado bloquea la cartola que ya carga.
- Que pasa: El caso dice que no la bloquea.
- Que queda: Cartola del 28/10 como esta.
- Rama: regresion

### CU-37. No se reabre el periodo desde Traspaso

**Acuerdo.** 03/11. No reabrir el periodo desde Traspaso y cierre. La correccion sale de la proforma.

**Estado.** Completo. Regresion. No construir de nuevo.

**Quien.** Locutor no rotulado. Pista: trato interno de Devint ("cachaí"), de manana, sin cliente nombrado. La regla de no reabrir ya la habia dicho el cliente el 26/10 y el 27/10. `transcripcion-2026-11-03-reunion-am.md` [00:35] a [01:12].

**Que pasa.** El boton de reapertura del traspaso queda fuera. Para corregir se pide desde la proforma.

**Documento o pantalla.** Traspaso y cierre de contratistas, sin reapertura. La solicitud vive en la proforma.

**Quien puede.** La sala de esa manana no nombro un permiso nuevo. Sigue CU-38.

**Limites.** No se reabre el periodo. No se ofrece la clave ahi.

**Que debe quedar.** Traspaso cerrado sin boton de reabrir.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca Traspaso, el boton de reapertura no vuelve.

**Depende de.** CU-22 y CU-38.

### Abanico

#### CU-37.1 Traspaso sin reapertura
- Condicion: El cierre de contratistas ya centralizo.
- Que pasa: No hay boton para reabrir el periodo desde Traspaso.
- Que queda: Periodo cerrado en esa pantalla.
- Rama: regresion

#### CU-37.2 Correccion desde la proforma
- Condicion: Hay que corregir una proforma cerrada.
- Que pasa: Se pide desde la proforma, no desde el panel de cierre.
- Que queda: Solicitud en la proforma.
- Rama: regresion

#### CU-37.3 Clave o boton de vuelta
- Condicion: Traspaso vuelve a ofrecer reapertura.
- Que pasa: No vuelve.
- Que queda: Sin boton y sin clave ahi.
- Rama: regresion

### CU-38. Motivo y dos vistos buenos, sin la clave al tiro

**Acuerdo.** 03/11. Periodo abierto: wizard con motivo y dos vistos buenos. Periodo cerrado: no ofrecer la clave directa.

**Estado.** Completo. Regresion. No construir de nuevo. El 05/11 no lo abre: precisa que el resultado no es un asiento nuevo (CU-59).

**Quien.** Misma pista que CU-37: manana interna. El cliente ya habia pedido los dos checks el 27/10. `transcripcion-2026-11-03-reunion-am.md` [01:32] a [02:13].

**Que pasa.** Al pedir la correccion se escribe el motivo y se ven dos vistos buenos: jefatura de contratistas y contabilidad. En periodo cerrado no aparece la reversa habilitada ni la clave de apertura.

**Documento o pantalla.** Solicitud desde la proforma.

**Quien puede.** Jefatura de contratistas y contabilidad, los dos vistos buenos. La sala no dio codigos de permiso.

**Limites.** No se reabre el mes. No se muestra la clave. El resultado de la correccion ya no es un asiento: CU-59.

**Que debe quedar.** Solicitud con motivo y dos aprobaciones, en abierto y en cerrado, sin clave de reapertura.

**Documentacion antes de codear.** No exige documento nuevo del wizard. Si se toca, no se salta un visto bueno ni se muestra la clave.

**Depende de.** CU-59 solo para el efecto sobre el asiento. El wizard en si no se reconstruye.

### Abanico

#### CU-38.1 Motivo y dos vistos buenos
- Condicion: Se pide la correccion con el periodo abierto o cerrado.
- Que pasa: Hay motivo y dos vistos buenos: jefatura de contratistas y contabilidad.
- Que queda: Solicitud incompleta si falta uno de los dos.
- Rama: regresion

#### CU-38.2 Periodo cerrado sin clave
- Condicion: El periodo esta cerrado.
- Que pasa: No se ofrece la reversa habilitada ni la clave de apertura.
- Que queda: Mes cerrado. Solicitud igual, sin reapertura.
- Rama: regresion

#### CU-38.3 Un solo visto bueno
- Condicion: Aprueba solo contratistas, o solo contabilidad.
- Que pasa: No alcanza. Son los dos.
- Que queda: Sin correccion habilitada.
- Rama: regresion

#### CU-38.4 El resultado es un asiento nuevo
- Condicion: Despues de los dos vistos buenos nace un comprobante de ajuste.
- Que pasa: El 05/11 preciso que el resultado no es ese asiento.
- Que queda: Sin asiento nuevo. Gana CU-59.
- Rama: no construir. Gana CU-59

### CU-39. Asiento de ajuste al cerrar la reversa

**Acuerdo.** 03/11. Al cerrar la reversa se genera un asiento de ajuste. Hubo respuesta afirmativa en la sala.

**Estado.** Pisado. No construir. La regla que gana es CU-59.

**Quien.** Locutor no rotulado. Carlos pregunta si debe generar un asiento de ajuste y la sala responde que si. En la tarde estan Francisca y Lupe [00:35] del archivo PM. `transcripcion-2026-11-03-reunion-pm.md` [32:48]. Mas tarde el mismo dia tambien dijeron ajustar la linea [02:17:02] del archivo combinado; el 05/11 dejo esa segunda frase como la regla.

**Que pasa.** Ese tramo pidio un comprobante de ajuste despues de los dos vistos buenos. El 05/11 lo reemplazo por editar la linea existente, sin asiento nuevo.

**Documento o pantalla.** No se construye el asiento de ajuste de la proforma.

**Quien puede.** No aplica.

**Limites.** No hay asiento de reversa ni asiento de ajuste para esta correccion.

**Que debe quedar.** Nada de ese comprobante nuevo.

**Documentacion antes de codear.** No exige documento del flujo viejo.

**Depende de.** CU-59.

### Abanico

#### CU-39.1 Asiento de ajuste al cerrar
- Condicion: Los dos vistos buenos ya estan y se genera un comprobante de ajuste.
- Que pasa: El 05/11 lo reemplazo por editar la linea.
- Que queda: Sin ese comprobante. Gana CU-59.
- Rama: no construir. Gana CU-59

#### CU-39.2 Asiento de reversa de la proforma
- Condicion: Cerrar la reversa deja un asiento de reversa nuevo.
- Que pasa: Tampoco se construye.
- Que queda: Sin asiento de reversa. Gana CU-59.
- Rama: no construir. Gana CU-59

#### CU-39.3 Editar la linea dentro de este caso
- Condicion: Se aprovecha este acuerdo pisado para construir la linea editada.
- Que pasa: La linea editada no nace aqui.
- Que queda: Nada de este flujo viejo. Gana CU-59.
- Rama: no construir. Gana CU-59

### CU-40. Proformas del periodo, y factura solo si hay vinculo

**Acuerdo.** 03/11. La grilla muestra solo las proformas del periodo. El recuadro de factura aparece solo si hay vinculo.

**Estado.** Parcial. La grilla del mes esta en local. El recuadro condicional no quedo acreditado en la auditoria.

**Quien.** Locutor no rotulado, manana interna, al ver proformas del periodo anterior. `transcripcion-2026-11-03-reunion-am.md` [30:02]. El recuadro: la minuta lo ubica en [30:55]; en el archivo el tramo siguiente habla del motivo del periodo cerrado. Minuto del recuadro: minuto no ubicado con una frase propia. La tarde, con Fran y Lupe, pide ver la factura en el detalle de la proforma: `transcripcion-2026-11-03-reunion-pm.md` [19:09].

**Que pasa.** En el periodo abierto no se listan proformas de meses anteriores. Si la proforma no tiene factura, no se dibuja el bloque de factura. Si tiene, se ve el vinculo.

**Documento o pantalla.** Grilla y detalle de proformas.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No mezclar periodos en la grilla del mes. No mostrar una factura vacia.

**Que debe quedar.** Grilla del periodo, y factura visible solo con vinculo real.

**Documentacion antes de codear.** Cuando se muestra el recuadro. Mensaje no hace falta si simplemente no esta. Estado de la proforma del periodo. Permiso no nombrado. Dato: factura vinculada, o ninguna.

**Depende de.** Ninguno.

### Abanico

#### CU-40.1 Grilla del periodo
- Condicion: Se abre la grilla del mes.
- Que pasa: No lista proformas de meses anteriores. Eso ya esta.
- Que queda: Solo el periodo.
- Rama: regresion

#### CU-40.2 Con factura vinculada
- Condicion: La proforma tiene una factura asociada.
- Que pasa: Se ve el recuadro. Esta parte no quedo acreditada.
- Que queda: Vinculo visible.
- Rama: construir

#### CU-40.3 Sin factura
- Condicion: La proforma no tiene factura.
- Que pasa: No se dibuja el bloque. No se muestra una factura vacia.
- Que queda: Detalle sin recuadro de factura.
- Rama: construir

#### CU-40.4 Meses mezclados o factura vacia
- Condicion: La grilla trae otro periodo, o el recuadro aparece sin vinculo.
- Que pasa: No es la regla.
- Que queda: Grilla del periodo y recuadro solo con vinculo real.
- Rama: no construir

### CU-41. Una proforma con una factura, y avisos de calce

**Acuerdo.** 03/11. Factura de proforma 1 a 1. Aviso al calzar. Aviso al creador si descuadra. Correo al asociar.

**Estado.** Parcial. El boton Contabilizar ya se esconde sin OC ni proforma. Faltan la vista de cobertura, el aviso verde, el aviso al creador y el correo. El 05/11 agrega que la cobertura puede ser parcial.

**Quien.** Tarde, Francisca y Lupe en la sala. Locutor no rotulado en las frases. `transcripcion-2026-11-03-reunion-pm.md` [14:17] a [15:58], [17:45] a [18:26] y [19:19]. Precision del 05/11: Maria Jesus, `transcripcion-2026-11-05-reunion.md` [02:30:02] a [02:30:23].

**Que pasa.** Una proforma no se asocia a una segunda factura, ni una factura ya calzada se reutiliza. Si cuadra, el aviso es verde, no solo naranja cuando descuadra. Si no cuadra (neto contra bruto, o un dia fuera de rango), se avisa a quien creo la proforma, con acuse. Al asociar se manda aviso interno y correo. El 05/11 Maria Jesus dice que la factura no tiene que cubrir la proforma completa: puede quedar parcializada, y que eso ya lo tienen. No es un campo porcentaje. El porcentaje que recordaban era de la OC madre, y ella lo recuerda por cantidad, no por un campo.

**Documento o pantalla.** Asociacion proforma-factura, y el aviso en el libro.

**Quien puede.** Contabilidad asocia. El creador de la proforma recibe el descuadre. La sala no dio codigos.

**Limites.** No 1 factura para varias asociaciones de la misma proforma. No reutilizar factura calzada. Sin campo porcentaje. El correo no se reemplaza por el aviso interno: la auditoria dice que el SMTP del PIN sigue fuera, y este correo es otro envio, tambien pendiente.

**Que debe quedar.** Vinculo 1 a 1, cobertura que puede ser parcial, aviso verde o aviso al creador, y correo al asociar.

**Documentacion antes de codear.** Textos del aviso verde y del descuadre. Mensaje al creador. Estado asociada / descuadrada. Permiso de asociar no nombrado en codigo. Dato: proforma, factura, si calzo, y que el correo se intento.

**Depende de.** CU-25. El correo no depende de CU-62.

### Abanico

#### CU-41.1 Calza y cubre
- Condicion: Monto y periodo de la factura cubren la proforma.
- Que pasa: Aviso verde, aviso interno y correo. No queda solo el naranja del descuadre.
- Que queda: Estado asociada. Correo intentado.
- Rama: construir

#### CU-41.2 Cobertura parcial
- Condicion: La factura no cubre la proforma completa.
- Que pasa: Puede quedar parcializada. No hay campo porcentaje. Maria Jesus dijo que no va por porcentaje.
- Que queda: Vinculo 1 a 1 con cobertura parcial, por el monto que calzo, no por un porcentaje.
- Rama: construir

#### CU-41.3 Descuadre
- Condicion: No calza: neto contra bruto, o un dia fuera de rango.
- Que pasa: Se avisa a quien creo la proforma, con acuse.
- Que queda: Estado descuadrada. Creador avisado.
- Rama: construir

#### CU-41.4 Segunda factura o factura reutilizada
- Condicion: La proforma ya tiene factura, o la factura ya esta calzada con otra.
- Que pasa: No se asocia. Mensaje no nombrado por la sala.
- Que queda: Sigue el vinculo anterior. La factura usada no reaparece para otra.
- Rama: construir

#### CU-41.5 Quien asocia y quien recibe
- Condicion: Hay que asociar, o hay descuadre.
- Que pasa: Contabilidad asocia. El creador recibe el descuadre. No al reves.
- Que queda: Asociacion hecha por contabilidad. Aviso en el creador.
- Rama: construir

#### CU-41.6 Campo porcentaje, o correo reemplazado
- Condicion: Se guarda un porcentaje, o el aviso interno sustituye al correo.
- Que pasa: Ninguno de los dos. El correo sigue pedido aunque el SMTP del PIN sea otro envio.
- Que queda: Sin porcentaje. Correo ademas del aviso interno.
- Rama: no construir

### CU-42. Contabilizar la factura contra facturas por recibir

**Acuerdo.** 03/11. En libro de compras se contabiliza contra facturas por recibir. No se muestra Contabilizar si no hay OC ni proforma.

**Estado.** Parcial. El boton ya se esconde sin OC ni proforma. Faltan cobertura contra la proforma, vista por proveedor, y la etiqueta contabilizada o pendiente.

**Quien.** Locutor no rotulado. Pista: contabilidad, tarde con Fran y Lupe. `transcripcion-2026-11-03-reunion-pm.md` [26:06] a [27:00] y [01:07:18] del mismo archivo, donde dicen que al contabilizar se elige OC o proforma.

**Que pasa.** El cierre del modulo reconoce el gasto contra el puente. El libro, al contabilizar el DTE, mueve facturas por recibir contra el proveedor, mas IVA. La factura asociada queda bloqueada y no contabilizada hasta ese paso. La vista muestra si la cobertura con la proforma esta completa, filtra un proveedor, y marca contabilizada o pendiente.

**Documento o pantalla.** Libro de compras.

**Quien puede.** La sala no nombro el permiso. Es trabajo de contabilidad.

**Limites.** Sin OC ni proforma no hay boton Contabilizar. No se contabiliza la factura dentro del modulo de contratistas.

**Que debe quedar.** Boton solo con vinculo, asiento contra el puente, y la vista que falta: cobertura, proveedor y etiqueta.

**Documentacion antes de codear.** Cuando se oculta el boton. Mensaje si no hay vinculo. Estados contabilizada y pendiente. Permiso no nombrado. Dato: OC o proforma, cobertura y si ya hay asiento.

**Depende de.** CU-21 y CU-41.

### Abanico

#### CU-42.1 Con OC o con proforma
- Condicion: La factura del libro tiene OC o proforma.
- Que pasa: Contabilizar mueve facturas por recibir contra el proveedor, mas IVA. Hasta ese paso la factura asociada sigue bloqueada y no contabilizada.
- Que queda: Asiento del libro. Estado contabilizada cuando el asiento existe.
- Rama: construir

#### CU-42.2 Sin OC ni proforma
- Condicion: La factura no tiene OC ni proforma.
- Que pasa: No se muestra Contabilizar. Eso ya esta.
- Que queda: Sin boton. Sin asiento de esta factura.
- Rama: regresion

#### CU-42.3 Vista que falta
- Condicion: Se mira el libro para una proforma o un proveedor.
- Que pasa: Falta ver la cobertura, filtrar un proveedor y la etiqueta contabilizada o pendiente.
- Que queda: Esas tres piezas en la vista.
- Rama: construir

#### CU-42.4 Contabilizar en contratistas
- Condicion: La factura de la proforma se contabiliza dentro del modulo de contratistas.
- Que pasa: Ahi nace el gasto, no la factura.
- Que queda: Factura sin asiento nacido en contratistas.
- Rama: no construir

### CU-43. La hija nace por guia, y solo la ultima ajusta la madre

**Acuerdo.** 03/11. Hijas de insumos por guia. Solo la ultima guia de la compra ajusta la madre.

**Estado.** Parcial. Hay codigo de madre. Falta el recorrido completo. El 05/11 dice que la cobertura de la madre es por cantidad, no por un campo porcentaje.

**Quien.** Locutor no rotulado. Tarde con Fran y Lupe. `transcripcion-2026-11-03-reunion-pm.md` [19:42] a [21:32]. Cantidad, no porcentaje: Maria Jesus, `transcripcion-2026-11-05-reunion.md` [02:29:19].

**Que pasa.** Una guia que no cierra la madre genera una hija. Varias hijas pueden compartir una factura, o ir a facturas distintas. Solo la ultima guia de esa compra puede ajustar la madre. Si aun asi no cuadra, se emite otra OC madre. No hay un segundo ajuste sobre la misma madre.

**Documento o pantalla.** Recepcion de insumos y OC madre / hija.

**Quien puede.** La sala no nombro el permiso. La hija no recorre la cadena de la OC.

**Limites.** Un solo ajuste por madre, en la ultima guia. Cobertura por cantidad, sin campo porcentaje. La hija sigue sin saldo: CU-02.

**Que debe quedar.** Hijas por guia, madre ajustada una sola vez, al final.

**Documentacion antes de codear.** Cual guia es la ultima. Mensaje si una guia intermedia intenta ajustar la madre. Estados de madre e hija. Permiso no nombrado. Dato: guia de cada hija y cantidades que cubren la madre.

**Depende de.** CU-02 y CU-47.

### Abanico

#### CU-43.1 Hija por guia que no cierra
- Condicion: Llega una guia que no cubre la madre.
- Que pasa: Nace una hija. Varias hijas pueden compartir una factura o ir a facturas distintas.
- Que queda: Hija ligada a su guia, sin saldo.
- Rama: construir

#### CU-43.2 Ultima guia, por cantidad
- Condicion: Es la ultima guia de esa compra y las cantidades ajustan la madre.
- Que pasa: Solo esa guia ajusta la madre. La cobertura es por cantidad, no por un campo porcentaje.
- Que queda: Madre ajustada una vez.
- Rama: construir

#### CU-43.3 Guia intermedia que ajusta
- Condicion: Una guia que no es la ultima intenta ajustar la madre.
- Que pasa: No lo hace. Mensaje no nombrado por la sala.
- Que queda: Madre sin ese ajuste.
- Rama: construir

#### CU-43.4 No cuadra ni con la ultima
- Condicion: La ultima guia ajusta y aun asi no cuadra.
- Que pasa: Se emite otra OC madre. No hay un segundo ajuste sobre la misma.
- Que queda: Madre nueva. La anterior con un solo ajuste.
- Rama: construir

#### CU-43.5 Porcentaje, cadena o saldo en la hija
- Condicion: Se usa un campo porcentaje, la hija entra a la cadena, o la hija queda con saldo.
- Que pasa: Ninguno. El saldo de la hija lo prohibe CU-02.
- Que queda: Sin porcentaje, sin cadena de la hija y sin saldo en la hija.
- Rama: no construir

### CU-44. Quien tiene el modulo puede entrar al grupo

**Acuerdo.** 03/11. Los usuarios con acceso al modulo deben poder entrar al grupo de aprobacion.

**Estado.** Completo. Regresion. No construir de nuevo. Corregido en local. En el servidor de la demo del 05/11 el rol administrador no aparecia; ese servidor no es este corte.

**Quien.** Tarde. Alguien de la sala (pista: estaba creando usuarios de Fran, analista contable) no ve personas al armar el grupo. Fran y Lupe estan nombradas al inicio. `transcripcion-2026-11-03-reunion-pm.md` [01:36] a [05:22] y [07:21].

**Que pasa.** Al crear el grupo de la OC se listan los usuarios que ya tienen un rol con acceso a ese modulo. No se esconden. Una persona puede estar en el grupo de emision y no en el de aprobacion: la aprobacion es de la jefatura. El rol y el grupo no son la misma cosa.

**Documento o pantalla.** Reglas de aprobacion de la OC.

**Quien puede.** Quien parametriza los grupos. La sala no dio un codigo. El 05/11 saca de la operacion a los administradores por modulo: CU-49. Entrar al grupo sigue exigiendo rol con acceso al modulo.

**Limites.** No se lista gente sin acceso al modulo. No se confunde emision con aprobacion. Se conserva la cadena solo en la OC de compras.

**Que debe quedar.** El buscador del grupo muestra a quien tiene el rol del modulo.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca el buscador, no se vuelve a dejar vacio a quien si tiene acceso.

**Depende de.** CU-49 no lo deshace: cambia quien administra, no esta lista.

### Abanico

#### CU-44.1 Con acceso al modulo
- Condicion: La persona tiene rol con acceso al modulo de la OC.
- Que pasa: Aparece al armar el grupo. No se esconde.
- Que queda: Puede entrar al grupo que corresponda.
- Rama: regresion

#### CU-44.2 Sin acceso al modulo
- Condicion: El usuario no tiene rol de ese modulo.
- Que pasa: No se lista.
- Que queda: Fuera del buscador del grupo.
- Rama: regresion

#### CU-44.3 Emision no es aprobacion
- Condicion: Alguien debe crear la OC y no aprobarla. La aprobacion es de la jefatura.
- Que pasa: Puede estar en el grupo de emision y no en el de aprobacion.
- Que queda: Rol y grupo siguen siendo cosas distintas.
- Rama: regresion

#### CU-44.4 Buscador vacio o cadena de OV
- Condicion: Quien si tiene acceso no aparece, o este buscador arma la cadena de la OV.
- Que pasa: No vuelve el buscador vacio. La OV se confirma al guardar.
- Que queda: Lista de quien tiene acceso. OV sin cadena.
- Rama: regresion

### CU-45. El organigrama es una vista

**Acuerdo.** 03/11. Organigrama como vista, no como motor de la cadena. La matriz lo da por confirmado el 05/11.

**Estado.** Completo. Regresion. No construir de nuevo. En local el motor sigue siendo grupos y escalas, y el organigrama es un arbol.

**Quien.** En los archivos del 03/11 no aparece la palabra organigrama. Minuto de ese dia: minuto no ubicado. La confirmacion es del 05/11. Carlos propone no rehacer las aprobaciones contra el organigrama [02:37]. La sala deja la vista como informativa [01:17:18] a [01:17:21]. `transcripcion-2026-11-05-reunion.md`.

**Que pasa.** El arbol se arma con el jefe marcado en el usuario. Sirve para leer quien depende de quien. No elige aprobadores ni montos.

**Documento o pantalla.** Admin > organigrama, solo lectura de la estructura.

**Quien puede.** La sala no nombro el permiso de verlo.

**Limites.** No arma la cadena. No reemplaza grupos. La cadena desde el organigrama es CU-46 y no se hace. Los cuatro titulos son CU-61.

**Que debe quedar.** Vista informativa, y la cadena intacta en grupos y escalas.

**Documentacion antes de codear.** No exige documento nuevo. Si se toca el arbol, no se conecta a la escala.

**Depende de.** CU-46, como prohibicion. CU-50 conserva los grupos.

### Abanico

#### CU-45.1 Arbol de lectura
- Condicion: Se abre el organigrama.
- Que pasa: Se arma con el jefe marcado en el usuario. Sirve para ver quien depende de quien.
- Que queda: Vista informativa.
- Rama: regresion

#### CU-45.2 El arbol elige aprobador o monto
- Condicion: La escala de la OC sale del organigrama.
- Que pasa: No se conecta. Grupos y escalas siguen siendo el motor.
- Que queda: Cadena intacta. El vinculo prohibido es CU-46.
- Rama: regresion

#### CU-45.3 El arbol reemplaza los grupos
- Condicion: Se borra el grupo porque el arbol ya muestra la jefatura.
- Que pasa: No los reemplaza.
- Que queda: Grupos conservados.
- Rama: regresion

### CU-46. No armar la cadena de la OC desde el organigrama

**Acuerdo.** 03/11 y 05/11. La sala rechazo usar el organigrama como motor de la cadena.

**Estado.** No hacer.

**Quien.** Carlos lo ofrece y lo descarta el 05/11 [02:37] y [47:08]. Maria Jesus y Fran dejan la vista informativa y conservan los grupos [01:17:18] y [53:18]. `transcripcion-2026-11-05-reunion.md`.

**Que pasa.** No se lee el jefe del arbol para armar la escala, ni se copia el monto desde el organigrama. La OC sigue su grupo y su escala.

**Documento o pantalla.** Ninguno nuevo.

**Quien puede.** No aplica.

**Limites.** Grupos y escalas se conservan. La OV sigue sin cadena.

**Que debe quedar.** Cero vinculo de aprobacion entre el arbol y la OC.

**Documentacion antes de codear.** No se documenta una pantalla de "cadena segun organigrama".

**Depende de.** CU-45 y CU-50.

### Abanico

#### CU-46.1 Escala leida del jefe
- Condicion: El jefe marcado en el arbol arma la escala de la OC.
- Que pasa: La sala lo rechazo.
- Que queda: Sin esa lectura. La OC sigue en su grupo.
- Rama: no construir

#### CU-46.2 Monto copiado del organigrama
- Condicion: El tope sale del arbol.
- Que pasa: El arbol no define montos.
- Que queda: Sin monto traido del organigrama.
- Rama: no construir

#### CU-46.3 OV colgada del arbol
- Condicion: La orden de venta toma aprobadores del organigrama.
- Que pasa: La OV no tiene cadena.
- Que queda: OV sin cadena.
- Rama: no construir

#### CU-46.4 Grupo y escala que ya mandan
- Condicion: La OC se aprueba por su grupo.
- Que pasa: Eso se conserva. No se codea un vinculo nuevo.
- Que queda: Cadena donde ya esta.
- Rama: regresion

### CU-47. En la recepcion no se adivina el articulo por la guia

**Acuerdo.** 03/11. La matriz dice "calzar por codigo de articulo". La transcripcion dice otra cosa: no guiarse ni por el nombre ni por el codigo que viene en la guia.

**Estado.** Parcial. El calce por articulo sigue pedido. La forma la precisa el 05/11: se elige el articulo del maestro. No se construye un calce automatico por el codigo de la guia.

**Quien.** Locutor no rotulado. Tarde con Fran y Lupe. `transcripcion-2026-11-03-reunion-pm.md` [01:20:45] a [01:20:51].

**Que pasa.** Los codigos y los nombres de la guia no alcanzan, y el nombre en pantalla sale cortado. Quien recepciona indica el articulo. El 05/11 lo deja como eleccion del maestro, y recien ahi se confirma el stock: CU-57.

**Documento o pantalla.** Recepcion de la guia de insumos.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No hay match automatico por codigo o nombre de la guia. No se suma stock al solo registrar: CU-57.

**Que debe quedar.** Cada linea de la guia apuntando a un articulo elegido del maestro.

**Documentacion antes de codear.** Como se elige el articulo. Mensaje si la linea queda sin articulo. Estado de la linea recepcionada sin stock hasta confirmar. Permiso no nombrado. Dato: articulo del maestro elegido, distinto del texto de la guia.

**Depende de.** CU-57.

### Abanico

#### CU-47.1 Articulo elegido del maestro
- Condicion: Se recepciona una linea de guia.
- Que pasa: Quien recepciona indica el articulo del maestro. Codigo y nombre de la guia no alcanzan.
- Que queda: Linea apuntando al articulo elegido, distinto del texto de la guia.
- Rama: construir

#### CU-47.2 Linea sin articulo
- Condicion: La linea queda sin articulo del maestro.
- Que pasa: No sigue. Mensaje no nombrado por la sala.
- Que queda: Linea sin recepcion cerrada.
- Rama: construir

#### CU-47.3 Calce automatico
- Condicion: El sistema casa la linea por el codigo o por el nombre que trae la guia.
- Que pasa: La transcripcion dijo que no se guia por ninguno de los dos.
- Que queda: Sin match automatico.
- Rama: no construir

#### CU-47.4 Stock al elegir
- Condicion: Elegir el articulo suma bodega.
- Que pasa: El stock no sube al registrar ni al elegir. Sube al confirmar.
- Que queda: Linea recepcionada sin stock. Gana el momento CU-57.
- Rama: no construir. Gana CU-57

### CU-48. AlmaWeb

**Acuerdo.** 03/11. Numeros y permisos del portal AlmaWeb.

**Estado.** Fuera. Otro sistema.

**Quien.** Jose, de AlmaWeb, en la manana. Maria Jesus dejo dos pendientes, relatados ahi: numeros del portal, y permisos de usuarios administradores contra la carga de evidencias (Paola). `transcripcion-2026-11-03-reunion-am.md` [35:34] a [40:30].

**Que pasa.** No se construye en el ERP. Mario arma un documento de pendientes del portal. Lo ya resuelto no se duplica en ese archivo.

**Documento o pantalla.** Ninguno en el ERP.

**Quien puede.** No aplica.

**Limites.** No se mezclan usuarios ni permisos de AlmaWeb con los roles del ERP.

**Que debe quedar.** El caso anotado, fuera del repo.

**Documentacion antes de codear.** No se documenta pantalla del ERP.

**Depende de.** Ninguno.

### Abanico

#### CU-48.1 Numeros del portal
- Condicion: Maria Jesus dejo pendiente el tema de numeros en AlmaWeb.
- Que pasa: No se construye en el ERP.
- Que queda: Sin pantalla de numeros del portal.
- Rama: no construir

#### CU-48.2 Permisos de evidencias
- Condicion: El portal distingue administradores y la carga de evidencias de Paola.
- Que pasa: Se corrige en AlmaWeb, no en los roles del ERP.
- Que queda: Sin esos permisos mezclados aca.
- Rama: no construir

#### CU-48.3 Usuarios del portal dentro del ERP
- Condicion: Un usuario o un permiso de AlmaWeb se copia al rol del ERP.
- Que pasa: No se mezclan.
- Que queda: Roles del ERP sin esa copia.
- Rama: no construir

#### CU-48.4 Duplicar lo ya resuelto
- Condicion: El documento de pendientes de Mario repite un punto que ya esta resuelto.
- Que pasa: No se duplica en el ERP.
- Que queda: Sin ese retrabajo.
- Rama: no construir

### CU-49. El acceso es el rol, no un administrador por modulo

**Acuerdo.** 05/11. Los administradores por modulo se retiran de la operacion. El acceso queda en el rol.

**Estado.** Parcial. El rol ya define paginas. Sigue el mantenedor de administradores por modulo. Falta dejarlo fuera del flujo. No se le da poder de cadena.

**Quien.** Maria Jesus y Fran en la sala. Carlos resume y la sala asiente. `transcripcion-2026-11-05-reunion.md` [34:28], [35:26] y [01:11:42].

**Que pasa.** Lo que una persona lee o escribe lo pide la parametrizacion general, por rol y cargo. No lo decide la jefatura del area en el momento. La jefatura es un eslabon de la cadena, no un rol que borre parametros. Ve la auditoria de su modulo, no la de todos. Dos cuentas parametrizan y no operan el dia a dia: gerencia general y jefatura de contabilidad. La cuenta maestra no lleva nombre de persona.

**Documento o pantalla.** Roles. El mantenedor de administradores por modulo sale de la operacion.

**Quien puede.** Quien parametriza los roles. La sala no dio un codigo. La jefatura no administra parametros.

**Limites.** No vuelve el administrador por modulo a la cadena ni a la operacion diaria. Se conserva CU-44: para entrar a un grupo hace falta rol con acceso al modulo. La OV sigue sin cadena.

**Que debe quedar.** Acceso solo por rol. Mantenedor de administradores por modulo fuera del flujo.

**Documentacion antes de codear.** Que pantallas deja de ver la operacion. Mensaje no hace falta si el menu no lo muestra. Estado no aplica. Permiso: el rol, no el flag de administrador de modulo. Dato: ninguno nuevo; se deja de usar el flag como acceso.

**Depende de.** CU-44, que no se rompe.

### Abanico

#### CU-49.1 Leer y escribir por rol
- Condicion: Alguien debe ver o editar una pagina.
- Que pasa: Lo define el rol, en la parametrizacion general. Esa parte ya existe.
- Que queda: Acceso por rol.
- Rama: regresion

#### CU-49.2 Mantenedor fuera de la operacion
- Condicion: El mantenedor de administradores por modulo sigue en el flujo diario.
- Que pasa: Se saca. No se le da poder de cadena.
- Que queda: Operacion sin ese mantenedor.
- Rama: construir

#### CU-49.3 Jefatura que administra o ve todo
- Condicion: La jefatura del area otorga el acceso en el momento, borra parametros, o ve la auditoria de todos los modulos.
- Que pasa: No. La jefatura es eslabon de la cadena. Ve la auditoria de su modulo.
- Que queda: Sin ese poder. Auditoria solo del propio modulo.
- Rama: no construir

#### CU-49.4 Quienes parametrizan y no operan
- Condicion: Gerencia general y jefatura de contabilidad configuran.
- Que pasa: No operan el dia a dia. La cuenta maestra no lleva nombre de persona.
- Que queda: Dos cuentas de parametrizacion, sin nombre de persona en la maestra.
- Rama: construir

#### CU-49.5 Flag de administrador como cadena o como OV
- Condicion: El administrador por modulo aprueba, o este cambio pone cadena en la OV.
- Que pasa: Ni lo uno ni lo otro. Para entrar a un grupo sigue haciendo falta el rol del modulo, CU-44.
- Que queda: Flag sin poder de cadena. OV sin cadena.
- Rama: no construir

### CU-50. Los grupos son las areas

**Acuerdo.** 05/11. Grupos iguales a areas, con topes distintos. Gerencia de area y gerencia general en cada grupo.

**Estado.** Parcial. El motor de grupos se conserva y no se elimina. La auditoria no acredita que cada grupo tenga ya las dos gerencias y topes distintos. Los topes son CU-52 y CU-53.

**Quien.** Maria Jesus corrige a Carlos, que habia propuesto quitar los grupos. `transcripcion-2026-11-05-reunion.md` [45:52] y [52:59] a [53:37].

**Que pasa.** Abastecimiento, comercial, COMEX, recursos humanos y contabilidad compran, cada uno con su tope. El grupo es el area. En cada grupo se repiten la gerencia de area y la gerencia general. No se borra el esquema de grupos.

**Documento o pantalla.** Grupos de aprobacion de compras.

**Quien puede.** Quien parametriza. La sala nombro areas, no un permiso.

**Limites.** No se eliminan los grupos. No se arma esto desde el organigrama: CU-46. No se pone cadena en la OV. La cadena de la OC se conserva.

**Que debe quedar.** Un grupo por area de compra, con las dos gerencias repetidas, y tope propio (el monto es CU-53).

**Documentacion antes de codear.** Que el grupo es un area. Mensaje si se intenta aprobar una OC de un area sin grupo. Estado no aplica al grupo. Permiso no nombrado. Dato: area del grupo, y los usuarios de jefatura, gerencia de area y gerencia general.

**Depende de.** CU-51, CU-52 y CU-53. CU-46 prohibe el atajo del organigrama.

### Abanico

#### CU-50.1 Un grupo por area
- Condicion: Abastecimiento, comercial, COMEX, recursos humanos o contabilidad compran.
- Que pasa: El grupo es el area. En cada uno se repiten gerencia de area y gerencia general.
- Que queda: Grupo con jefatura del area y las dos gerencias.
- Rama: construir

#### CU-50.2 OC de un area sin grupo
- Condicion: El area compra y no tiene grupo.
- Que pasa: No entra a una cadena inventada. Mensaje no nombrado por la sala.
- Que queda: OC sin encolar a un grupo que no existe.
- Rama: construir

#### CU-50.3 Motor que ya existe
- Condicion: Los grupos siguen siendo el motor.
- Que pasa: No se reconstruye el motor. Falta acreditar las dos gerencias en cada grupo.
- Que queda: Grupos conservados.
- Rama: regresion

#### CU-50.4 Quitar grupos, usar el arbol, o encadenar la OV
- Condicion: Se eliminan los grupos, la cadena sale del organigrama, o la OV entra a este esquema.
- Que pasa: El mismo dia se piso eliminar los grupos. El arbol es CU-46. La OV no tiene cadena.
- Que queda: Grupos vivos. OV sin cadena. Arbol sin motor.
- Rama: no construir

### CU-51. Jefatura, gerencia de area y gerencia general

**Acuerdo.** 05/11. Siempre firma la jefatura, despues la gerencia de area, despues la gerencia general.

**Estado.** Parcial. Las escalas existen y son configurables. La auditoria no acredita este orden fijo de tres niveles.

**Quien.** Maria Jesus. `transcripcion-2026-11-05-reunion.md` [48:46] a [49:17] y [01:02:30].

**Que pasa.** Aunque el monto sea chico, pasa por la jefatura del area. Si supera el tope de esa jefatura, sigue a la gerencia de area y despues a la gerencia general. No se salta a la jefatura. Son tres niveles. La sala uso de ejemplo a Agustin en gerencia de area y a Nico en gerencia general. Esos nombres son los cargos de la conversacion, no una tabla cerrada de usuarios.

**Documento o pantalla.** Escala de la OC del grupo.

**Quien puede.** Jefatura del area, gerencia de area y gerencia general, en ese orden. La sala no dio codigos de permiso.

**Limites.** No se salta el primer eslabon. No se agrega la OV a esta cadena. El ultimo eslabon no aprueba infinito: CU-52.

**Que debe quedar.** Toda OC del grupo recorre jefatura y, si el monto lo pide, los dos niveles siguientes, hasta el tope del ultimo.

**Documentacion antes de codear.** Orden de los tres niveles. Mensaje si falta la jefatura del grupo. Estado de la OC en la cadena. Permiso: estar en el eslabon que corresponde. Dato: quien firmo cada nivel.

**Depende de.** CU-50. El tope de cada nivel es CU-53. El techo del ultimo es CU-52.

### Abanico

#### CU-51.1 Monto chico, igual la jefatura
- Condicion: La OC no supera el tope de la jefatura del area.
- Que pasa: Igual firma la jefatura. No se salta.
- Que queda: OC en la jefatura.
- Rama: construir

#### CU-51.2 Supera el tope de la jefatura
- Condicion: El monto supera el tope de esa jefatura.
- Que pasa: Sigue a gerencia de area y despues a gerencia general.
- Que queda: Tres niveles, en ese orden, hasta el tope del ultimo.
- Rama: construir

#### CU-51.3 Falta la jefatura
- Condicion: El grupo no tiene jefatura y la OC quiere saltar a gerencia.
- Que pasa: No se salta. Mensaje no nombrado por la sala.
- Que queda: OC sin avanzar al segundo nivel.
- Rama: construir

#### CU-51.4 Igual al tope de la jefatura
- Condicion: El monto es igual al tope de la jefatura, ni menor ni mayor.
- Que pasa: La sala dijo que sigue si supera. No dijo el borde igual.
- Que queda: Sin una regla nueva para el igual.
- Rama: complemento. Frase de la sala: Si supera el tope de esa jefatura, sigue a gerencia de area y despues a gerencia general.

#### CU-51.5 Saltar jefatura, infinito, o cadena en la OV
- Condicion: La OC salta a gerencia, el ultimo aprueba sin techo, o la OV usa estos tres niveles.
- Que pasa: No se salta. El techo del ultimo es CU-52. La OV no entra.
- Que queda: Orden jefatura, gerencia de area, gerencia general. OV sin cadena.
- Rama: no construir

### CU-52. El ultimo eslabon tiene techo

**Acuerdo.** 05/11. El ultimo eslabon tiene tope. Si la OC lo pasa, no entra a la cadena y hay mensaje.

**Estado.** Faltante. Hoy la cadena puede cerrar en el ultimo nodo sin ese bloqueo.

**Quien.** Maria Jesus. El ejemplo del monto lo conversan con Carlos. `transcripcion-2026-11-05-reunion.md` [01:03:04] a [01:05:02].

**Que pasa.** El techo frena un error de tipeo. Si la orden supera el tope del ultimo, no se encola. Se muestra que excede el monto de gerencia. Para un monto real por encima del techo, alguien sube el tope a mano y mientras tanto la orden no se aprueba. La sala uso de ejemplo 400 millones como tope de Nico y 4.000 millones como el caso que no debe entrar. Son ejemplos de la conversacion, no el parametro unico de la empresa.

**Documento o pantalla.** Envio de la OC a aprobacion.

**Quien puede.** Nadie aprueba esa OC hasta que el tope se ajuste. La sala no nombro quien edita el tope.

**Limites.** No entra a la cadena. No se aprueba "igual" con un aviso suave. El tope es por moneda: CU-53.

**Que debe quedar.** OC bloqueada, con mensaje, y sin fila en la bandeja.

**Documentacion antes de codear.** Texto del mensaje: excede el monto de gerencia. Estado de la OC: no encolada. Permiso de subir el tope: no nombrado. Dato: monto de la OC, moneda y tope del ultimo eslabon que la rechazo.

**Depende de.** CU-51 y CU-53.

### Abanico

#### CU-52.1 Bajo el tope del ultimo
- Condicion: La OC no supera el tope del ultimo eslabon.
- Que pasa: Puede entrar a la cadena.
- Que queda: OC encolada.
- Rama: construir

#### CU-52.2 Sobre el tope
- Condicion: La OC supera el tope del ultimo. El ejemplo de la sala fue 400 millones contra 4.000, y no es el parametro unico.
- Que pasa: No entra. Se muestra que excede el monto de gerencia. Mientras no suban el tope a mano, no se aprueba.
- Que queda: OC no encolada, sin fila en la bandeja.
- Rama: construir

#### CU-52.3 Igual al tope
- Condicion: El monto es igual al tope del ultimo.
- Que pasa: La sala dijo que no entra si lo supera. No dicto el igual.
- Que queda: Sin regla nueva para el igual.
- Rama: complemento. Frase de la sala: Si la orden supera el tope del ultimo, no se encola.

#### CU-52.4 Ultimo sin numero de tope
- Condicion: El ultimo eslabon no tiene un monto cargado.
- Que pasa: La sala dijo que el ultimo tiene tope y no dicto el numero del borde. No se sustituye por infinito.
- Que queda: Sin aprobacion hasta infinito por campo vacio.
- Rama: complemento. Frase de la sala: El ultimo eslabon tiene tope.

#### CU-52.5 Hasta infinito o aviso suave
- Condicion: El ultimo aprueba cualquier monto, o la OC entra igual y solo avisa.
- Que pasa: Esa idea quedo pisada el mismo dia.
- Que queda: Sin infinito y sin encolado por encima del tope.
- Rama: no construir

### CU-53. Tope por peso, dolar y yuan

**Acuerdo.** 05/11. El tope se carga en CLP, USD y yuan. Al tipear pesos, se propone el tipo de cambio del dia y se puede editar. Ese numero queda fijo.

**Estado.** Faltante. Hoy la escala tiene un monto. Faltan los tres y la propuesta del dia.

**Quien.** Maria Jesus pregunta si habra OC en yuanes, y cierra la multimoneda. `transcripcion-2026-11-05-reunion.md` [01:05:10] a [01:09:09].

**Que pasa.** La misma cadena sirve para las tres monedas. Cada eslabon tiene un tope por moneda. Si la OC se escribe en pesos, el sistema propone la conversion del dia (la sala dijo Banco Central) y deja cambiarla antes de guardar. Despues no se recalcula sola. El peso sigue siendo el monto de partida; no se borra.

**Documento o pantalla.** Tope del eslabon, y el monto de la OC.

**Quien puede.** Quien parametriza la escala. La sala no nombro el permiso.

**Limites.** Monedas dichas: CLP, USD y yuan. No se agrega otra. No se recalcula el tipo ya guardado. No hay un aprobador extra segun la moneda [01:08:14].

**Que debe quedar.** Tres topes por eslabon, y en la OC el tipo de cambio propuesto, editado y guardado.

**Documentacion antes de codear.** Donde se cargan los tres topes. Mensaje si falta el tope de la moneda de la OC. Estado no aplica al tope; la OC usa CU-52 si se pasa. Permiso no nombrado. Dato: tope CLP, tope USD, tope yuan, tipo propuesto, tipo guardado y fecha del dia en que se propuso.

**Depende de.** CU-52. El peso de la escala actual no se tira: es el punto de partida.

### Abanico

#### CU-53.1 Tres topes
- Condicion: Se parametriza un eslabon.
- Que pasa: Tiene tope en CLP, en USD y en yuan. El peso que ya existe no se borra: es el punto de partida.
- Que queda: Tres montos. El de pesos conserva el monto de partida.
- Rama: construir

#### CU-53.2 Propuesta del dia
- Condicion: La OC se escribe en pesos y el tope o el monto piden conversion.
- Que pasa: Se propone el tipo del dia, Banco Central, se puede editar y despues queda fijo.
- Que queda: Tipo propuesto, tipo guardado y fecha del dia.
- Rama: construir

#### CU-53.3 Falta el tope de esa moneda
- Condicion: La OC esta en una de las tres monedas y el eslabon no tiene ese tope.
- Que pasa: No se aprueba con el tope de otra moneda. Mensaje no nombrado por la sala.
- Que queda: OC sin usar un tope ajeno. Si ademas se pasa el ultimo, vale CU-52.
- Rama: construir

#### CU-53.4 Recalcular, otra moneda o aprobador extra
- Condicion: El tipo guardado se recalcula solo, se agrega una moneda, o aparece un aprobador segun la moneda.
- Que pasa: Ninguno. La misma cadena sirve para las tres.
- Que queda: Tipo fijo. Sin moneda nueva y sin eslabon extra.
- Rama: no construir

#### CU-53.5 Monto unico que ya esta
- Condicion: La escala de hoy tiene un solo monto.
- Que pasa: No se tira. Pasa a ser el tope en pesos.
- Que queda: Tope CLP de partida conservado.
- Rama: regresion

### CU-54. La receta es de embalaje, no de un packing

**Acuerdo.** 05/11. Receta de embalaje. En el consumo, cantidad por cada packing. Centro de costo en la receta.

**Estado.** Faltante. Hoy receta y produccion piden un packing. Eso queda pisado: no se conserva como obligacion.

**Quien.** Maria Jesus. `transcripcion-2026-11-05-reunion.md` [02:13:10] a [02:15:57] y [01:44:30] a [01:44:47].

**Que pasa.** La receta no se amarra a un solo packing. Queda al embalaje. En el consumo se indica cuanto uso cada packing de esa receta. El packing se muestra para saber quien consumio. El centro de costo va en la receta, no recien al consumir. Un centro tiene muchas recetas. La lista se filtra por centro. La crea la jefatura, sin cadena. El consumo si pasa por aprobacion. La sala no nombro cual cadena.

**Documento o pantalla.** Receta de embalaje y consumo de bodega.

**Quien puede.** Jefatura crea la receta, sin cadena. El consumo pasa por aprobacion. Permiso de sistema: no nombrado.

**Limites.** No se exige un packing para guardar la receta. No se suma en una sola unidad lo que la orden trae en litros y en kilos: eso es de la orden de aplicacion, CU-64. El precio del consumo es CU-55.

**Que debe quedar.** Receta sin packing obligatorio, con centro, y consumo con cantidad por packing.

**Documentacion antes de codear.** Receta y linea de consumo. Mensaje si el consumo no dice la cantidad del packing. Estado de la receta (creada por jefatura) y del consumo (pendiente de aprobacion). Permiso: jefatura para crear; la cadena del consumo no quedo nombrada. Dato: embalaje, centro de costo, packing y cantidad consumida.

**Depende de.** CU-55 para el precio. CU-64 espera el Excel y no bloquea los campos que la sala ya dijo.

### Abanico

#### CU-54.1 Receta de embalaje con centro
- Condicion: Se guarda una receta.
- Que pasa: No pide un packing. Lleva centro de costo. Un centro puede tener muchas, y la lista filtra por centro.
- Que queda: Receta creada, con centro y sin packing obligatorio.
- Rama: construir

#### CU-54.2 Consumo por packing
- Condicion: Se consume esa receta.
- Que pasa: Se indica cuanto uso cada packing. Si no dice la cantidad, no sigue. Mensaje no nombrado por la sala.
- Que queda: Consumo con packing y cantidad. El packing muestra quien consumio.
- Rama: construir

#### CU-54.3 Quien crea y quien consume
- Condicion: Hay que crear la receta, o registrar el consumo.
- Que pasa: La jefatura crea, sin cadena. Otra persona no. El consumo si pasa por aprobacion. La sala no nombro cual cadena.
- Que queda: Receta creada por la jefatura. Consumo pendiente de aprobacion.
- Rama: construir

#### CU-54.4 Packing obligatorio
- Condicion: La receta no se guarda si no tiene un packing.
- Que pasa: Eso es lo que este acuerdo pisa.
- Que queda: Receta guardada sin ese obligatorio.
- Rama: no construir

#### CU-54.5 Litros sumados con kilos
- Condicion: El consumo junta unidades distintas en un solo numero.
- Que pasa: No se suman. La unidad de la orden es CU-64.
- Que queda: Cantidades separadas por unidad.
- Rama: no construir

### CU-55. El consumo va al promedio del mes

**Acuerdo.** 05/11. Consumo a precio promedio del stock del mes. No se consume guia por guia ni de la mas antigua a la mas nueva.

**Estado.** Parcial. El consumo de receta ya usa el costo de bodega. Falta dejar explicito que es el promedio del stock del mes, y no ofrecer FIFO.

**Quien.** Maria Jesus. `transcripcion-2026-11-05-reunion.md` [01:46:17] a [01:51:08] y [01:59:06]. El tramo de no ir de la mas antigua a la mas nueva esta en la misma conversacion de precio; la minuta lo junta en [01:58:28] a [02:06:18].

**Que pasa.** Al consumir se toma el precio promedio de lo que hay en bodega ese mes, incluido el stock anterior. Sale de cantidad y costo de lo recibido. No se edita el precio a mano en el maestro para "inventar" el promedio: lo mueven las guias. El mes ya consumido no se reescribe si al mes siguiente cambia el promedio. La devolucion no usa este precio: CU-56.

**Documento o pantalla.** Consumo de bodega (receta, orden de aplicacion o ingreso manual).

**Quien puede.** La sala no nombro el permiso del consumo, salvo que pasa por aprobacion: CU-54.

**Limites.** No FIFO. No precio de una guia puntual para el consumo. No reescribir meses cerrados. Tres entradas al cierre, pedidas por Agustin via Maria Jesus: orden de aplicacion, receta e ingreso manual [04:19] a [04:25]. Las tres centralizan bodega.

**Que debe quedar.** Consumo del mes al promedio de ese stock, sin opcion de salir de la guia mas vieja a la mas nueva.

**Documentacion antes de codear.** De donde sale el promedio. Mensaje si alguien elige FIFO o una guia como costo del consumo. Estado del consumo del mes. Permiso: el de aprobacion de CU-54. Dato: cantidad, costo del stock del mes y el promedio guardado en ese consumo.

**Depende de.** CU-54. No cambia CU-35 ni CU-56.

### Abanico

#### CU-55.1 Costo de bodega que ya se usa
- Condicion: El consumo de receta valoriza hoy con el costo de bodega.
- Que pasa: Esa base no se tira.
- Que queda: Consumo sigue tomando costo de bodega.
- Rama: regresion

#### CU-55.2 Promedio del stock del mes
- Condicion: Se consume por receta, por orden de aplicacion o por ingreso manual.
- Que pasa: El precio es el promedio de lo que hay ese mes, stock anterior incluido. Sale de cantidad y costo recibido. Las tres entradas centralizan bodega.
- Que queda: Promedio del mes guardado en ese consumo.
- Rama: construir

#### CU-55.3 FIFO, guia puntual o precio escrito a mano
- Condicion: Se ofrece salir de la mas antigua a la mas nueva, tomar el precio de una guia, o editar el maestro para inventar el promedio.
- Que pasa: No. Mensaje no nombrado por la sala si alguien elige FIFO o una guia como costo.
- Que queda: Sin esas tres vias.
- Rama: no construir

#### CU-55.4 Reescribir el mes o devolver al promedio
- Condicion: Al mes siguiente cambia el promedio y se reescribe el mes ya consumido, o la devolucion usa este precio.
- Que pasa: El mes cerrado no se reescribe. La devolucion es CU-56.
- Que queda: Consumos viejos intactos. Devolucion fuera de este promedio.
- Rama: no construir

### CU-56. La devolucion no le saca stock a la guia

**Acuerdo.** 05/11. Devolucion al precio de la guia, en un documento nuevo, sin rebajar esa guia.

**Estado.** Parcial. El precio de origen ya se toma (CU-35). Falta no descontar la existencia de la guia, y el documento de salida distinto.

**Quien.** Maria Jesus. `transcripcion-2026-11-05-reunion.md` [02:07:46] a [02:08:12].

**Que pasa.** Se busca la guia solo para copiar el precio de llegada. El stock de esa guia no se mueve. La salida es un documento nuevo. Se puede devolver aunque esas unidades ya se hayan consumido. Si se devolviera al promedio, la nota de credito del proveedor no calza.

**Documento o pantalla.** Documento nuevo de devolucion a proveedor.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se rebaja la guia origen. No se usa el promedio. No FIFO. Sin merma.

**Que debe quedar.** Devolucion nueva, valorizada al precio de la guia, con el stock de esa guia igual que antes.

**Documentacion antes de codear.** Documento de salida. Mensaje si no se encuentra la guia para el precio. Estado del documento nuevo, y la guia origen sin cambio de stock. Permiso no nombrado. Dato: guia consultada, precio copiado, y que no se desconto cantidad de esa guia.

**Depende de.** CU-35. No depende de CU-55 mas que para no mezclar los dos precios.

### Abanico

#### CU-56.1 Documento nuevo al precio de la guia
- Condicion: Se devuelve al proveedor y se busca la guia de llegada.
- Que pasa: Se copia el precio. El stock de esa guia no se mueve. La salida es un documento nuevo.
- Que queda: Devolucion nueva. Guia origen con la misma existencia.
- Rama: construir

#### CU-56.2 Unidades ya consumidas
- Condicion: Esas unidades ya salieron de bodega.
- Que pasa: Igual se puede devolver, al precio de la guia, sin rebajarla.
- Que queda: Documento nuevo. Guia sin rebaja.
- Rama: construir

#### CU-56.3 No hay guia para el precio
- Condicion: No se encuentra la guia de llegada.
- Que pasa: No se inventa el precio. Mensaje no nombrado por la sala.
- Que queda: Sin devolucion valorizada.
- Rama: construir

#### CU-56.4 Precio de origen que ya se toma
- Condicion: La salida ya puede tomar el precio de la guia o de la factura.
- Que pasa: Esa mitad no se reconstruye. Este caso agrega el documento nuevo y la no rebaja.
- Que queda: Precio de origen conservado.
- Rama: regresion

#### CU-56.5 Rebaja, promedio, FIFO o merma
- Condicion: Se descuenta la guia, se usa el promedio, se sale por FIFO o se registra merma.
- Que pasa: Ninguno.
- Que queda: Guia intacta. Sin promedio, sin FIFO y sin merma.
- Rama: no construir

### CU-57. El stock sube al confirmar, y la guia lleva adjunto

**Acuerdo.** 05/11. El stock de la recepcion sube al confirmar, no al registrar. Adjunto (foto) en la guia.

**Estado.** Faltante. La guia 52 en local exige bodega de packing. Falta confirmar antes de sumar, y el respaldo.

**Quien.** Maria Jesus acepta el adjunto. El momento del stock lo cierran en el mismo tramo. `transcripcion-2026-11-05-reunion.md` [02:10:19] y [02:10:29] a [02:10:50].

**Que pasa.** Registrar la guia no suma bodega. Al confirmar la recepcion, con el articulo del maestro ya elegido (CU-47), recien sube el stock. En la guia recibida se adjuntan fotos o documentos de como llego el packing.

**Documento o pantalla.** Recepcion de guia de insumos.

**Quien puede.** La sala no nombro el permiso de confirmar.

**Limites.** No hay stock en el alta de la guia. El adjunto no reemplaza el Excel de Acepta de CU-01: se suman. Mientras Acepta siga, el tipeo manual sigue.

**Que debe quedar.** Guia registrada con stock en cero hasta confirmar, y con archivo de respaldo.

**Documentacion antes de codear.** Boton confirmar distinto de registrar. Mensaje si se confirma sin articulo del maestro. Estados registrada y confirmada. Permiso no nombrado. Dato: fecha de confirmacion, articulo, cantidad que entro al stock, y el archivo.

**Depende de.** CU-01 y CU-47.

### Abanico

#### CU-57.1 Registrar no suma
- Condicion: La guia se registra y el articulo del maestro ya esta elegido.
- Que pasa: El stock sigue en cero.
- Que queda: Estado registrada.
- Rama: construir

#### CU-57.2 Confirmar suma
- Condicion: Se confirma la recepcion, con articulo del maestro.
- Que pasa: Recien ahi sube el stock. Puede llevar foto o documento de como llego, ademas del Excel de Acepta de CU-01.
- Que queda: Estado confirmada, con cantidad, fecha y archivo.
- Rama: construir

#### CU-57.3 Confirmar sin articulo
- Condicion: Se confirma una linea sin articulo del maestro.
- Que pasa: No suma. Mensaje no nombrado por la sala.
- Que queda: Sigue sin stock.
- Rama: construir

#### CU-57.4 Stock al registrar
- Condicion: Registrar la guia, o solo adjuntar la foto, aumenta la bodega.
- Que pasa: No es el momento dicho.
- Que queda: Stock sin cambio hasta confirmar.
- Rama: no construir

### CU-58. El maestro de activo fijo nace de la OC recepcionada

**Acuerdo.** 05/11. Activo fijo solo si la OC de ese tipo esta recepcionada. Aviso si no tiene factura. Estados recepcionado y facturado.

**Estado.** Faltante. El tipo en la OC existe (CU-29). Falta el selector de OC recepcionadas y el alta ahi.

**Quien.** Maria Jesus relata lo que Agustin pidio, y cierra el momento del alta. `transcripcion-2026-11-05-reunion.md` [02:19:12] a [02:26:01]. El grafico mensual de depreciacion quedo bien [02:18:10].

**Que pasa.** Todo nace en la OC tipo activo fijo. No se crea el maestro al elegir el tipo, ni antes de la orden, ni directo contra la factura sola. El maestro se crea cuando la OC esta recepcionada: llego el producto. La factura puede llegar despues. El alta lista solo OC recepcionadas de ese tipo y avisa si todavia no tienen factura. En el libro de compras, al asociar la factura, se ve el activo. Al cierre viajan la cuenta al debe, la cuenta al haber y la depreciacion. No pidieron otro campo.

**Documento o pantalla.** Alta de activo fijo desde OC recepcionada, y el vinculo en el libro de compras.

**Quien puede.** La sala no nombro el permiso. La OC sigue su cadena de compras.

**Limites.** No alta sin OC. No alta al guardar la OC. No alta solo con la factura. Se conservan del 21/10: sin centro de costo en el alta, vida util unica en meses igual a la tributaria, correccion por IPC. No se vende esto como insumo ni entra a bodega de insumos.

**Que debe quedar.** Bien creado desde una OC recepcionada, con aviso si falta factura, y visible en el libro cuando la factura se asocie.

**Documentacion antes de codear.** Lista de OC elegibles. Mensaje si la OC no esta recepcionada, y aviso si no tiene factura. Estados recepcionado y facturado. Permiso no nombrado. Dato: OC, estado de recepcion, factura si ya llego, vida util en meses e IPC. Sin centro de costo.

**Depende de.** CU-29. No depende de CU-04: ese origen no se construye.

### Abanico

#### CU-58.1 OC recepcionada con factura
- Condicion: La OC es de activo fijo, esta recepcionada y ya tiene factura.
- Que pasa: El alta la ofrece y crea el maestro. En el libro se ve el activo al asociar la factura.
- Que queda: Bien en estado facturado, ligado a la OC y a la factura.
- Rama: construir

#### CU-58.2 Recepcionada sin factura
- Condicion: Llego el producto y la factura no.
- Que pasa: Igual se puede crear. Avisa que todavia no tiene factura.
- Que queda: Bien en estado recepcionado, con el aviso.
- Rama: construir

#### CU-58.3 OC que no esta recepcionada
- Condicion: Se intenta el alta con una OC de activo fijo no recepcionada.
- Que pasa: No esta en la lista. Mensaje no nombrado por la sala.
- Que queda: Sin maestro.
- Rama: construir

#### CU-58.4 Vida util, sin centro, IPC y cierre
- Condicion: El bien se da de alta o se cierra el mes.
- Que pasa: Sin centro de costo. Vida util unica en meses, igual a la tributaria. IPC en el valor neto. Al cierre viajan debe, haber y depreciacion. No pidieron otro campo. El grafico mensual ya quedo bien.
- Que queda: Maestro con esos datos. Cierre con las tres piezas. Grafico como esta.
- Rama: construir

#### CU-58.5 Alta fuera de la OC recepcionada
- Condicion: Se crea al elegir el tipo, al guardar la OC, sin OC, solo con la factura, desde papel no digital, con centro de costo, o como insumo de bodega.
- Que pasa: Ninguna de esas puertas.
- Que queda: Sin ese maestro. El tipo en la OC sigue siendo CU-29.
- Rama: no construir

#### CU-58.6 Grafico que ya esta
- Condicion: Se vuelve a construir el grafico mensual de depreciacion.
- Que pasa: La sala dijo que esta bien.
- Que queda: Grafico sin rehacerse.
- Rama: regresion

### CU-59. Corregir la proforma edita la linea

**Acuerdo.** 05/11. La correccion edita la linea. No nace un asiento de ajuste ni uno de reversa. El mayor muestra solo activos.

**Estado.** Faltante. Hay solicitud, dos vistos buenos y protocolo. Sigue el discurso del asiento nuevo. Hay que sacarlo.

**Quien.** Maria Jesus y Fran. Carlos resume y la sala confirma. `transcripcion-2026-11-05-reunion.md` [05:55] a [06:39] y [02:33:28] a [02:33:34].

**Que pasa.** No se reabre el mes. La correccion se guarda en la linea del asiento que ya existe. Queda auditoria de quien, cuando, quien aprobo y como quedo. El libro mayor muestra solo comprobantes activos. Lo anulado y lo pendiente no entran. Si la proforma tenia factura, se desasocia, se corrige y se vuelve a asociar la factura que quedo libre [02:33:06].

**Documento o pantalla.** Linea del asiento de la proforma, y el libro mayor.

**Quien puede.** Los dos vistos buenos de CU-38. La sala no cambio ese par.

**Limites.** No se reabre el periodo. No hay asiento de reversa ni de ajuste. No se editan a mano los montos de un asiento por fuera de esta correccion aprobada: la inmutabilidad del asiento contabilizado sigue, y esta correccion es el acto aprobado, no una edicion libre. Anular es otro acto: CU-60.

**Que debe quedar.** La misma linea con el valor nuevo, historial de la correccion, y el mayor sin esa linea si quedo anulada o pendiente.

**Documentacion antes de codear.** Que se ve en la linea antes y despues. Mensaje si se intenta generar otro comprobante. Estado de la linea corregida. Permiso: los dos vistos buenos. Dato: valor anterior, valor nuevo, motivo, quien pidio y quien aprobo.

**Depende de.** CU-38. Reemplaza a CU-24 y CU-39. No se construyen esos.

### Abanico

#### CU-59.1 Se edita la linea
- Condicion: La correccion tiene motivo y los dos vistos buenos de CU-38.
- Que pasa: Se guarda en la linea del asiento que ya existe. Queda quien, cuando, quien aprobo y como quedo.
- Que queda: La misma linea con el valor nuevo y el historial.
- Rama: construir

#### CU-59.2 Tenia factura
- Condicion: La proforma corregida tenia factura.
- Que pasa: Se desasocia, se corrige la linea y se vuelve a asociar la factura que quedo libre.
- Que queda: Factura reasociada. Linea corregida.
- Rama: construir

#### CU-59.3 Mayor solo con activos
- Condicion: Se consulta el libro mayor.
- Que pasa: Entran solo comprobantes activos. Lo anulado y lo pendiente no.
- Que queda: Mayor sin anulados ni pendientes.
- Rama: construir

#### CU-59.4 Otro comprobante o el mes reabierto
- Condicion: Nace un asiento de ajuste, uno de reversa, se reabre el periodo, o se edita el monto sin esta correccion aprobada.
- Que pasa: No. Mensaje no nombrado por la sala si se intenta otro comprobante.
- Que queda: Sin asiento nuevo y sin mes reabierto. Montos contabilizados sin edicion libre.
- Rama: no construir

#### CU-59.5 Anular para corregir el monto
- Condicion: Se anula la fila en vez de editar la linea.
- Que pasa: Anular es otro acto.
- Que queda: Linea no anulada por esta correccion. Gana el acto CU-60 si lo que se quiere es anular.
- Rama: no construir. Gana CU-60 cuando el acto es anular

### CU-60. Anular el asiento no lo borra

**Acuerdo.** 05/11. Anular deja la fila, con motivo. No entra al mayor. Lo hace la jefatura, o un analista lo solicita y la jefatura aprueba. Sin tope de monto.

**Estado.** Faltante. No hay anulacion con solicitud a la jefatura.

**Quien.** Maria Jesus y Fran. `transcripcion-2026-11-05-reunion.md` [02:34:07] a [02:40:16].

**Que pasa.** Anular no desaparece la fila de la base. La jefatura anula con motivo. Otra persona puede solicitarlo y la jefatura lo aprueba. No es una cadena por monto. Editar y anular son dos acciones. El asiento manual sigue existiendo para ajustes y reclasificaciones que no nacen de un modulo. El mayor de CU-59 omite lo anulado.

**Documento o pantalla.** Comprobante de asiento, accion anular, y solicitud a la jefatura.

**Quien puede.** Jefatura de contabilidad anula. Un analista solo solicita. La sala lo dijo asi [02:40:16]: lo aprueba la jefatura, independiente del monto.

**Limites.** No se borra la fila. No hay tope ni cadena de montos para anular. No se usa anular para cambiar un monto: eso es la correccion de CU-59 o un asiento manual nuevo, no esta accion.

**Que debe quedar.** Fila anulada, con motivo, fuera del mayor, visible para auditoria.

**Documentacion antes de codear.** Diferencia entre editar y anular. Mensaje de motivo obligatorio. Estado anulado. Permiso de jefatura, y solicitud si no lo es. Dato: motivo, quien solicito, quien anulo y cuando.

**Depende de.** CU-59 para el filtro del mayor. No reemplaza la inmutabilidad del monto contabilizado.

### Abanico

#### CU-60.1 La jefatura anula
- Condicion: La jefatura de contabilidad anula, con motivo, sea cual sea el monto.
- Que pasa: La fila queda. No entra al mayor. Sin motivo no sigue. Mensaje no nombrado por la sala.
- Que queda: Estado anulado, con motivo, quien y cuando. Visible para auditoria.
- Rama: construir

#### CU-60.2 El analista solicita
- Condicion: Quien no es jefatura quiere anular.
- Que pasa: Solo solicita. La jefatura aprueba. No hay tope ni cadena de montos.
- Que queda: Solicitud pendiente hasta la jefatura. Despues, fila anulada.
- Rama: construir

#### CU-60.3 Asiento manual que no nace de un modulo
- Condicion: Hace falta un ajuste o una reclasificacion que no sale de un modulo.
- Que pasa: El asiento manual sigue existiendo. No se usa la anulacion para cambiar un monto.
- Que queda: Asiento manual disponible. Anular no lo reemplaza.
- Rama: regresion

#### CU-60.4 Borrar, anular sin jefatura, o encadenar por monto
- Condicion: Desaparece la fila, el analista anula solo, o el monto arma una cadena.
- Que pasa: Ninguno. La sala dijo que lo aprueba la jefatura, independiente del monto.
- Que queda: Fila presente. Sin cadena de montos.
- Rama: no construir

#### CU-60.5 Anular para cambiar el monto
- Condicion: Se anula porque el monto esta mal y no se quiere la correccion de la linea ni un asiento manual.
- Que pasa: Editar y anular son dos acciones.
- Que queda: Monto sin cambio por esta via. El cambio de linea es CU-59.
- Rama: no construir

### CU-61. Organigrama con cuatro titulos

**Acuerdo.** 05/11. El organigrama muestra gerencia general, gerencia de area, jefatura y analista. Solo vista.

**Estado.** Parcial. La vista existe (CU-45). La auditoria no acredita esos cuatro titulos.

**Quien.** Fran pide los titulos. Maria Jesus confirma que es informativo. `transcripcion-2026-11-05-reunion.md` [01:13:24] a [01:13:32] y [01:17:18] a [01:17:21].

**Que pasa.** El arbol se nutre del jefe marcado en el usuario. Los titulos son esos cuatro. No define montos ni la cadena. Las reglas de aprobacion siguen en la escala.

**Documento o pantalla.** Organigrama de lectura.

**Quien puede.** La sala no nombro el permiso de verlo.

**Limites.** Solo vista. No se rehacen las aprobaciones contra el arbol: CU-46. No se esconden los grupos.

**Que debe quedar.** Arbol con los cuatro titulos, sin efecto en la OC.

**Documentacion antes de codear.** Los cuatro titulos. Mensaje no hace falta. Estado no aplica. Permiso no nombrado. Dato: cargo del usuario que alimenta el arbol. Sin monto.

**Depende de.** CU-45 y CU-46.

### Abanico

#### CU-61.1 Vista que ya existe
- Condicion: Se abre el organigrama.
- Que pasa: Sigue siendo lectura. No se reconstruye el arbol.
- Que queda: Vista informativa.
- Rama: regresion

#### CU-61.2 Cuatro titulos
- Condicion: El arbol se nutre del jefe marcado en el usuario.
- Que pasa: Muestra gerencia general, gerencia de area, jefatura y analista. Sin monto.
- Que queda: Esos cuatro titulos, sin efecto en la OC.
- Rama: construir

#### CU-61.3 El arbol aprueba o esconde los grupos
- Condicion: Los titulos definen la escala, o se ocultan los grupos porque el arbol ya esta.
- Que pasa: No. La cadena desde el arbol es CU-46.
- Que queda: Arbol sin monto y sin cadena. Grupos visibles.
- Rama: no construir

### CU-62. CAF y emision en GoSocket productivo

**Acuerdo.** 05/11. Se acabaron los CAF. La emision productiva queda pendiente.

**Estado.** Fuera.

**Quien.** Carlos informa. Maria Jesus y Fran estan en la sala. `transcripcion-2026-11-05-reunion.md` [02:27:09] a [02:27:31].

**Que pasa.** En el ambiente productivo de GoSocket no quedan CAF. Carlos habla con Pablo. Quieren, la proxima semana, recibir DTE en el libro de compras. Este corte no emite al SII live ni pide folios.

**Documento o pantalla.** Ninguno de emision.

**Quien puede.** No aplica.

**Limites.** No se emite DTE real. No se compra CAF desde el ERP en este paquete.

**Que debe quedar.** El caso anotado, fuera de construccion.

**Documentacion antes de codear.** No se documenta pantalla de emision productiva.

**Depende de.** Ninguno.

### Abanico

#### CU-62.1 Emitir al SII
- Condicion: Se emite un DTE en GoSocket productivo.
- Que pasa: No quedan CAF. Este corte no emite.
- Que queda: Sin emision.
- Rama: no construir

#### CU-62.2 Pedir folios desde el ERP
- Condicion: El ERP compra o pide CAF.
- Que pasa: Carlos habla con Pablo. No se construye aqui.
- Que queda: Sin pedido de folios.
- Rama: no construir

#### CU-62.3 Recibir DTE esta semana como si el corte lo incluyera
- Condicion: Se adelanta la recepcion productiva para cerrar un modulo en este paquete.
- Que pasa: La sala lo dejo para la proxima semana, fuera de esta construccion.
- Que queda: Sin esa emision ni esa recepcion productiva en este corte.
- Rama: no construir

### CU-63. Reportes por jefatura

**Acuerdo.** 05/11. Los reportes de cada modulo se ven con la jefatura de ese departamento, cuando el modulo este cerrado.

**Estado.** Espera.

**Quien.** Maria Jesus. `transcripcion-2026-11-05-reunion.md` [02:28:02] a [02:28:46].

**Que pasa.** No se arma el paquete de reportes en esta planificacion. Cuando un modulo funcione, hay una reunion con la jefatura del area. Maria Jesus quiere ver lo que piden ellos, no solo lo que ella ve.

**Documento o pantalla.** Ninguno hasta esa reunion.

**Quien puede.** La jefatura del modulo, en la reunion. No hay permiso de sistema dicho.

**Limites.** No se adelanta un reporte "por si acaso".

**Que debe quedar.** El caso anotado, sin pantallas de reporte nuevas.

**Documentacion antes de codear.** No se documenta reporte hasta que el modulo este cerrado y la jefatura diga que quiere ver.

**Depende de.** Ninguno de este paquete. No bloquea los casos a construir.

### Abanico

#### CU-63.1 Reportes antes de cerrar el modulo
- Condicion: El modulo todavia no funciona y se arma su reporteria.
- Que pasa: No se codea.
- Que queda: Sin reportes nuevos.
- Rama: no construir

#### CU-63.2 Reporte sin la jefatura
- Condicion: Se disena lo que Maria Jesus ve, sin preguntar a la jefatura del area.
- Que pasa: Ella quiere ver lo que pidan ellos, cuando el modulo este cerrado.
- Que queda: Sin ese paquete adelantado.
- Rama: no construir

#### CU-63.3 La reunion como pantalla
- Condicion: La reunion con la jefatura se convierte en un modulo de reportes.
- Que pasa: Es una reunion, no una pantalla de este corte.
- Que queda: Sin pantallas de reporte nuevas.
- Rama: no construir

### CU-64. Excel de receta y orden de aplicacion real

**Acuerdo.** 05/11. El cliente envia el Excel de recetas y una orden de aplicacion real. Mientras tanto quedan los campos que la sala si dijo.

**Estado.** Espera de archivo. No se inventan columnas que el archivo traiga y la sala no nombro.

**Quien.** Maria Jesus. El Excel falta desde el inicio de la sala [05:02]. La orden la piden y dicen que la van a solicitar a abastecimiento agricola [01:36:47] y [01:38:45]. `transcripcion-2026-11-05-reunion.md`.

**Que pasa.** La carga automatica convive con el tipeo cuando llegue el formato. No llega en este corte. Lo que si quedo dicho, y se puede documentar sin el archivo:

- Orden de aplicacion con mas de una linea [01:35:48].
- Dosis por hectarea, que calcula la cantidad. Ejemplo de la sala: 2,5 litros por hectarea [01:34:45]. Es un ejemplo, no una dosis fija.
- Unidad de cada insumo. No se suman litros con kilos [01:36:19] a [01:36:29].
- El centro de costo es de la orden, no de cada linea. Es el cuartel [01:37:47] a [01:37:51].
- Elemento de costo: lo nombraron [01:38:30] y no cerraron si va en la orden o en la linea. No se elige uno de los dos.
- Carlos pregunto si la orden pasa por la cadena de insumos [01:39:14]. En el tramo siguiente no hay un si del cliente. No queda como regla.

**Documento o pantalla.** Ninguna carga hasta el archivo. Los campos de arriba se documentan para la orden manual, que es la tercera entrada al cierre junto con la receta (CU-54).

**Quien puede.** La sala no nombro quien crea la orden de aplicacion.

**Limites.** Sin el Excel no hay carga masiva. Sin la orden real no se agregan campos. El elemento de costo queda sin lugar hasta que abastecimiento responda.

**Que debe quedar.** El caso en espera, y la lista de campos ya dichos para no perderlos.

**Documentacion antes de codear.** No se documenta la carga. Para la orden manual, solo los campos cerrados: varias lineas, unidad, dosis por hectarea y centro de costo de la orden. El elemento de costo se anota como pregunta abierta, no como campo.

**Depende de.** CU-54 y CU-55 para no contradecir receta y precio. El archivo no bloquea esos dos.

### Abanico

#### CU-64.1 Carga del Excel que no llego
- Condicion: Se implementa la carga automatica de recetas.
- Que pasa: El archivo no esta. No se codea.
- Que queda: Sin carga masiva.
- Rama: no construir

#### CU-64.2 Columnas que el archivo traeria
- Condicion: Se agregan campos que la sala no nombro, a la espera del Excel o de la orden real.
- Que pasa: No se inventan.
- Que queda: Sin esas columnas.
- Rama: no construir

#### CU-64.3 Orden manual con lo ya dicho
- Condicion: Se codea la orden de aplicacion solo con lo conversado, antes del documento real.
- Que pasa: Los campos quedan anotados y no se construyen en este corte: varias lineas, unidad, dosis por hectarea y centro de costo de la orden. El 2,5 litros es ejemplo, no dosis fija.
- Que queda: Caso en espera. Sin pantalla nueva.
- Rama: no construir

#### CU-64.4 Elemento de costo ubicado por nosotros
- Condicion: El elemento va en la orden, o va en la linea, porque alguien lo elige.
- Que pasa: La sala lo nombro y no cerro el lugar.
- Que queda: Sin elemento de costo ubicado.
- Rama: no construir

#### CU-64.5 Cadena de insumos o unidades sumadas
- Condicion: La orden pasa por la cadena de insumos, el centro va por linea, o se suman litros con kilos.
- Que pasa: La cadena no tuvo un si del cliente. El centro es de la orden. Las unidades no se suman.
- Que queda: Sin cadena, sin centro por linea y sin suma de unidades distintas.
- Rama: no construir

### CU-65. Cuentas que faltan en el cierre de bodega

**Acuerdo.** 05/11. Falta el listado de cuentas del cierre de bodega.

**Estado.** Espera del listado. Sin merma.

**Quien.** Locutor no rotulado. Pista: miran el mapeo del cierre con Maria Jesus y Fran. `transcripcion-2026-11-05-reunion.md` [02:16:45] a [02:16:55].

**Que pasa.** Al mirar entradas y salidas, alguien pregunta si faltaria merma y la respuesta es que faltan algunas cuentas. Piden que manden el detalle. La palabra merma no abre un concepto: merma no existe. No hay caso de merma. Hasta que llegue el listado no se agregan cuentas.

**Documento o pantalla.** Ninguno nuevo.

**Quien puede.** La sala no nombro el permiso.

**Limites.** No se implementa merma. No se inventa el plan de cuentas del cierre.

**Que debe quedar.** El caso anotado. El cierre que ya existe no gana una cuenta nueva por esta frase.

**Documentacion antes de codear.** No se documenta cuenta, mensaje ni asiento hasta el listado.

**Depende de.** CU-03, que ya tiene los dos asientos dichos el 21/10. Este caso no los reemplaza.

### Abanico

#### CU-65.1 Cuentas nuevas sin listado
- Condicion: Se completan las cuentas del cierre de bodega antes de que manden el detalle.
- Que pasa: No se agregan.
- Que queda: Cierre sin cuentas nuevas.
- Rama: no construir

#### CU-65.2 Merma
- Condicion: La palabra merma, dicha al mirar el mapeo, abre una cuenta.
- Que pasa: Merma no existe.
- Que queda: Sin cuenta de merma.
- Rama: no construir

#### CU-65.3 Reemplazar los dos asientos
- Condicion: El listado pendiente sustituye el asiento de recepcion y el de calce.
- Que pasa: Esos dos ya estan dichos en CU-03. Este caso no los reemplaza.
- Que queda: CU-03 intacto hasta que llegue el listado.
- Rama: no construir

### CU-66. Packing COMEX externo

**Acuerdo.** Packing de cajas y pallets de COMEX, fuera del ERP.

**Estado.** Fuera.

**Quien.** En las transcripciones de este corte (21/10 a 05/11) no ubique un pedido del cliente de construir ese packing externo. Minuto no ubicado. La auditoria lo deja diferido y fuera. No se inventa el flujo para tapar ese silencio.

**Que pasa.** No se construye en el ERP el packing de cajas y pallets de COMEX.

**Documento o pantalla.** Ninguno.

**Quien puede.** No aplica.

**Limites.** No se confunde con la receta de embalaje de CU-54 ni con el packing que el consumo muestra para saber quien consumio.

**Que debe quedar.** El caso anotado, fuera.

**Documentacion antes de codear.** No se documenta pantalla.

**Depende de.** Ninguno.

### Abanico

#### CU-66.1 Packing de cajas y pallets
- Condicion: Se construye en el ERP el packing externo de COMEX.
- Que pasa: En este corte no hay pedido ubicado. No se inventa el flujo.
- Que queda: Sin ese modulo.
- Rama: no construir

#### CU-66.2 Confundido con la receta
- Condicion: La receta de embalaje de CU-54 se trata como el packing de COMEX.
- Que pasa: Son cosas distintas. La receta si es de este ERP.
- Que queda: Receta sin convertirse en COMEX.
- Rama: no construir

#### CU-66.3 Confundido con el packing del consumo
- Condicion: El packing que el consumo muestra, para saber quien consumio, se vuelve el packing externo.
- Que pasa: Ese packing es el de CU-54, no este.
- Que queda: Consumo sin heredar un modulo COMEX.
- Rama: no construir

## 3. Recuento de escenarios

275 escenarios.

- construir: 108
- regresion: 65
- no construir: 99
- complemento: 3

## 4. Abanicos con menos de 3 escenarios

Ninguno. Cada caso abrio al menos tres ramas con lo que su propio texto ya decia. No se agrego una tercera de relleno.
