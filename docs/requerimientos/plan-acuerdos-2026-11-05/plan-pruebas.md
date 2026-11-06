# Plan de pruebas: acuerdos 21/10 a 05/11

Corte: 05/11/2026. Este archivo no se ejecuta. Una prueba por escenario del abanico de `casos-de-uso.md`.

Empresa: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`. No se entregan credenciales.

Pasa solo la columna Resultado que pasa, que es el Que queda de la sala. Lo que el codigo ya hace no acredita una rama construir ni una rama complemento. Regresion pasa si eso sigue cumpliendose y no se reconstruye. No construir pasa si ese camino no se implementa. Si el escenario dice que gana otro CU, la fila lo nombra.

La factura de proveedor, cuando el escenario la usa, entra por un registro del libro ya existente o por carga manual. No se emite DTE y no se dispara un evento a GoSocket. No se paga y no se cierra el mes.

## Recuento

- Pruebas: 275.
- Construir: 108.
- Complemento: 3.
- Regresion: 65.
- No construir: 99.
- Suma: 108 + 3 + 65 + 99 = 275.

## Pruebas

### CU-01. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-01.1 Guia digitada con respaldo | construir | La guia no llega por GoSocket y abastecimiento sigue en Acepta. | Guia registrada, usable en la recepcion, todavia sin stock. |
| CU-01.2 Registrada y sin stock | construir | La guia se digito y todavia no se confirma la recepcion. | Estado registrada, cantidad en bodega sin cambio. |
| CU-01.3 Campos de una guia real que no llego | no construir | No esta el archivo de guia real pedido el 21/10. | Sin columnas nuevas sacadas de un archivo ausente. |
| CU-01.4 Stock al tipear | no construir | Alguien suma bodega en el mismo acto de digitar. | Nada de stock nuevo en el tipeo. Lo hace CU-57. |

### CU-02. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-02.1 Hija que se cierra al facturar | construir | La guia no cubre la OC y luego se le asocia la factura. | Hija cerrada, sin saldo. |
| CU-02.2 Madre con lo que falta | construir | Llegaron unas tandas y todavia no todas. | Madre abierta. Las hijas ya facturadas siguen cerradas. |
| CU-02.3 Saldo dejado en la hija | construir | Se intenta guardar una hija con saldo despues de facturar. | La hija no queda abierta. El saldo, si existe, sigue en la madre. |
| CU-02.4 Hija que vuelve a la cadena | no construir | Se manda la hija a aprobacion como si fuera una OC nueva. | Hija sin recorrido de cadena. |

### CU-03. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-03.1 Asiento al recepcionar | construir | Hay recepcion acumulada del mes y se cierra bodega. | Asiento de recepcion ligado a la recepcion. |
| CU-03.2 Asiento al calce | construir | La factura calza lo recepcionado. | Asiento de calce en el cierre. |
| CU-03.3 Contabilizar desde la hija | construir | Alguien usa una accion de contabilizar en la orden hija. | Hija recepcionada o facturada, no contabilizada en la orden. |
| CU-03.4 Cuenta de merma en el cierre | no construir | Se agrega merma porque la palabra aparecio al mirar movimientos. | Sin cuenta de merma. |

### CU-04. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-04.1 Alta directa sin OC | no construir | El bien entra al modulo sin orden de compra. | No queda esa alta. Gana CU-58. |
| CU-04.2 Nexo solo con la factura | no construir | Se crea el maestro contra la factura, sin OC recepcionada. | Sin maestro nacido de la factura sola. Gana CU-58. |
| CU-04.3 Papel que no llego digital | no construir | Se da de alta un bien desde un documento fisico que no esta en el libro. | Sin ese alta. Gana CU-58. |

### CU-05. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-05.1 Aprobada con factura, cuenta y glosa | construir | La proforma esta aprobada y con factura, en la lectura de ese dia. | Asiento con esa proforma, cuenta y glosa. |
| CU-05.2 Borrador, pendiente o ingreso suelto | construir | La proforma no esta aprobada, o el ingreso no tiene proforma. | Fuera del asiento, visible como informativo. |
| CU-05.3 La jefatura cambia cuenta y glosa | construir | La jefatura necesita otra cuenta o completa la glosa. | Cuenta y glosa guardadas en contratistas y en bodega. |
| CU-05.4 Factura exigida del mismo mes | no construir | Se frena el gasto porque la factura cae al mes siguiente. | No se construye ese freno. Gana la precision de CU-20. |
| CU-05.5 Cadena en la orden de venta | no construir | Se aprovecha el cierre para poner aprobacion en la OV. | OV sin cadena. |

### CU-06. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-06.1 Glosa visible y comentario aparte | construir | El comprobante ya tiene glosa. | Glosa del comprobante intacta, comentario guardado aparte. |
| CU-06.2 Descarga de activos, y reversados aparte | construir | Se exportan asientos. | Archivo de activos, o de todos, segun el filtro. |
| CU-06.3 PDF del asiento | construir | Se pide el comprobante en PDF, ademas de Excel. | PDF del asiento que se esta viendo. |
| CU-06.4 Editar monto, cuenta o glosa ya contabilizados | regresion | El asiento ya esta contabilizado y se intenta cambiar monto, cuenta o glosa. | Asiento igual. El comentario de CU-06.1 no es esta edicion. |
| CU-06.5 Anular borrando la fila | no construir | Anular se entiende como borrar el comprobante. | Sin borrado. Gana CU-60. |
| CU-06.6 Reverso para armar reportes | no construir | Se reversa un asiento para alimentar un reporte. | Sin ese reverso. |

### CU-07. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-07.1 Factor en parametrizacion | construir | Hay que consultar o actualizar el factor de honorarios. | Factor vigente consultable. |
| CU-07.2 IPC nuevo con historial | construir | Cambia el IPC. | Valor vigente e historial. |
| CU-07.3 IPC sin fecha | construir | Se intenta guardar un valor de IPC sin fecha. | Sin valor huerfano en el historial. |
| CU-07.4 Tasa o vigencia inventadas | no construir | No hay tasa ni fecha dichas por la sala. | Sin parametro inventado. |

### CU-08. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-08.1 Ejecucion anual | construir | El centro tiene presupuesto del ano. | Ejecucion anual del centro. |
| CU-08.2 PDF del presupuesto | construir | Se pide imprimir esa vista. | PDF de la ejecucion del centro. |
| CU-08.3 Centro sin presupuesto | construir | El centro no tiene monto anual. | Sin monto anual inventado. |
| CU-08.4 Alerta de porcentaje | no construir | Se agrega un aviso al llegar a un porcentaje del presupuesto. | Sin alerta de porcentaje. |

### CU-09. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-09.1 Fechas en el mayor | construir | Se consulta el libro mayor. | Mayor del rango pedido. |
| CU-09.2 Balance de un solo ano | regresion | El balance de 8 se pide del ano actual o del pasado. | Balance de un ano. |
| CU-09.3 Balance que cruza el ano | regresion | El mismo balance de 8 pide dias de dos anos. | Sin informe cruzado. |
| CU-09.4 Estado de resultados anual por esta frase | no construir | Se arma un ER de varios meses porque el 22/10 hablo de filtros. | ER sin ese armado. Gana CU-13. |

### CU-10. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-10.1 Montos vistos en pesos | construir | La cartola esta en moneda de origen y se pide verla en pesos. | Vista en pesos, sin perder la moneda de origen. |
| CU-10.2 PDF de la cartola | construir | Se exporta la cartola. | PDF de lo que se esta viendo. |
| CU-10.3 Moneda o banco no reconocidos | construir | El archivo no identifica solo la moneda o el banco. | Cartola con banco y moneda asignados. Mensaje no nombrado por la sala. |
| CU-10.4 Semana y contabilizar desde la cartola | regresion | El egreso se asigna a una semana y se contabiliza desde el movimiento. | Movimiento en su semana, estado contabilizado o pendiente. |
| CU-10.5 Adjunto del pago disenado ahora | no construir | El pago llevaria un archivo, y Lupe no cerro como. | Sin adjunto nuevo en este corte. |
| CU-10.6 Asiento de pago distinto de la cartola | no construir | Se crea un asiento de pago aparte del movimiento de cartola. | Sin asiento paralelo de pago. |

### CU-11. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-11.1 RUT con un rol, a Excel | construir | Se consulta un RUT como cliente, proveedor o productor. | Excel con RUT, razon social y los movimientos filtrados. |
| CU-11.2 Filtro combinado | construir | El mismo RUT es mas de un rol y se eligen dos o los tres. | Excel solo con los roles marcados. |
| CU-11.3 RUT sin movimientos | construir | El RUT existe y no tiene documentos. | Consulta vacia. |
| CU-11.4 Quien mira el conjunto y quien consulta | construir | Contabilidad quiere el conjunto. La consulta de productor o proveedor es de tesoreria. | Misma ficha de RUT, dos usos dichos por la sala. |
| CU-11.5 Pagar o contabilizar desde la consulta | no construir | Desde el estado de cuenta se registra un pago o un asiento. | Sin pago y sin asiento nacidos aqui. |
| CU-11.6 Productor como entidad nueva | no construir | Se abre un maestro Productor para poder filtrar. | Sin maestro nuevo. Sigue CU-12. |

### CU-12. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-12.1 Ficha de cliente y proveedor | regresion | El RUT ya es cliente o proveedor. | Una ficha, sin duplicar el contacto. |
| CU-12.2 Listas separadas y doble rol | construir | Hace falta el listado de productores, o el RUT es proveedor y productor. | Lista de proveedores y lista de productores. Marca de doble rol. |
| CU-12.3 Mismo RUT, contacto compartido | construir | Se modifica telefono o correo en una lista y el RUT existe en la otra. | Un contacto para el RUT. |
| CU-12.4 Maestro Productor aparte | no construir | Se crea una entidad Productor distinta de la ficha. | Sin entidad Productor. |

### CU-13. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-13.1 Resultado de un mes | regresion | Se pide el estado de resultados de enero. | ER del mes, sin otros meses. |
| CU-13.2 Ejercicio y acumulado | regresion | Se abre el estado de situacion financiera. | Las dos lineas siguen visibles. |
| CU-13.3 Paso del 31/12 | regresion | Se cierra el 31 de diciembre. | Acumulado con ese traspaso. El ER de diciembre no se mezcla con enero. |
| CU-13.4 ER que trae otro mes | regresion | Se pide un resultado que junte dos meses. | ER de un mes. |

### CU-14. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-14.1 Linea buena dentro de un archivo mixto | construir | El archivo trae lineas completas y lineas sin un obligatorio. | Lineas en estado cargada. |
| CU-14.2 Linea sin obligatorio | construir | Falta el periodo o un dato que la cuenta pide, por ejemplo el centro. | Linea rechazada, con motivo y numero de linea. |
| CU-14.3 Si falla no carga nada | no construir | Una linea mala tira atras el archivo entero, como el ejemplo de Agrosoft. | Las lineas buenas siguen cargadas. |
| CU-14.4 Formato Agrosoft como ley | no construir | Se copian las columnas del ejemplo que estaban mirando. | Sin columnas tomadas de ese ejemplo. |

### CU-15. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-15.1 N centros, N elementos y N areas | construir | Se parametriza una cuenta. | Tres listas de la cuenta. |
| CU-15.2 Mismo centro, otro elemento | construir | Un centro transversal usa mas de un elemento, por ejemplo DUS y certificado. | Centro y elemento elegidos por separado, dentro de las listas. |
| CU-15.3 Dimension que la cuenta no tiene | construir | Se intenta usar un centro, elemento o area fuera de la lista. | Sin asociacion libre. |
| CU-15.4 Contador en el mantenedor inverso | construir | Se mira el centro, el elemento o el area. | Contador y detalle de cuentas. |
| CU-15.5 Elemento atado al centro | no construir | Elegir el centro deja un solo elemento fijo. | Sin ese amarre. |

### CU-16. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-16.1 Cuenta, despues centro y elemento | regresion | Se carga una linea de OC. | Linea con una cuenta y un centro. |
| CU-16.2 Dos centros | regresion | La misma cuenta va a dos centros. | Dos lineas. |
| CU-16.3 Centro que no esta en la cuenta | regresion | El centro o el elemento no figuran en la lista. | OC sin esa dimension hasta que exista en la cuenta. |
| CU-16.4 Pisos de la OC | regresion | La linea serviria para pasar una cotizacion a OC, vender bajo el precio de compra o aprobar una OV. | OC con el orden de siempre, sin esos tres caminos. |

### CU-17. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-17.1 PDF oficial sin dimensiones | construir | Se descarga la hoja que va al proveedor. | PDF oficial sin esas dimensiones. El estado de la OC no cambia. |
| CU-17.2 Detalle solo en el ERP | construir | Quien compra revisa la OC por dentro. | Detalle en el sistema, no en la hoja enviada. |
| CU-17.3 Export interno con detalle | construir | Hace falta una copia interna con dimensiones. | Dos salidas: oficial sin dimensiones, interna con detalle. |
| CU-17.4 PDF al proveedor con dimensiones | no construir | La hoja que se envia trae centro, elemento o cuenta. | Proveedor sin dimensiones contables. |

### CU-18. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-18.1 Archivo bajado del banco | regresion | Lupe descarga la cartola y se carga ese archivo. | Cartola importada con las reglas del 28/10. |
| CU-18.2 Conector en linea al banco | regresion | Se abre una integracion porque el ejecutivo del banco da poco acceso. | Sin conector. |
| CU-18.3 Archivo editado antes de subir | regresion | Alguien rearma columnas y lo carga como si fuera la bajada. | Sin un segundo formato casero como fuente. |

### CU-19. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-19.1 Actividad con muchas labores | construir | Se parametriza la actividad. | Actividad unica, con sus labores. |
| CU-19.2 Ingreso diario sin aprobacion | construir | En terreno se conoce la labor y se registra el dia. | Ingreso editable antes de entrar a una proforma. Sin cadena. |
| CU-19.3 La proforma se confirma | construir | Los ingresos ya estan agrupados en una proforma. | Proforma confirmada. Ingresos diarios sin cadena propia. |
| CU-19.4 Aprobar cada ingreso | no construir | Cada ingreso diario recorre una aprobacion. | Ingreso sin cadena. |
| CU-19.5 Cadena en la OV, u OC sin la suya | no construir | Se mueve la aprobacion a la orden de venta, o se le quita a la OC de compras. | OV sin cadena. OC de compras con la suya. |

### CU-20. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-20.1 Bloque que entra | construir | La proforma esta aprobada y corresponde al cierre. | Proforma dentro del asiento del periodo. |
| CU-20.2 Borrador e ingreso suelto | construir | Hay proformas sin aprobacion, en borrador, o ingresos sin proforma. | Estado solo informativo. |
| CU-20.3 Factura al mes siguiente | construir | La proforma es de un mes y la factura del siguiente. | Gasto del mes. Puente abierto hasta la factura. |
| CU-20.4 Exigir la factura del mismo mes | no construir | Sin factura del mismo mes la proforma aprobada no entra. | Sin ese freno. |

### CU-21. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-21.1 Un asiento del periodo | construir | Se centralizan las proformas que entran. | Un asiento con las proformas del periodo. |
| CU-21.2 La factura cancela el puente | construir | La factura calza en libro de compras. | Puente en cero cuando calza. |
| CU-21.3 Factura que aun no llega | construir | La factura cae al mes siguiente. | Gasto del mes y puente abierto. |
| CU-21.4 Gasto reconocido otra vez en compras | no construir | El libro de compras vuelve a reconocer el gasto de la proforma. | Sin segundo gasto. |
| CU-21.5 Un asiento por proforma | no construir | Centralizar abre un comprobante por cada proforma. | Sigue siendo un asiento. |

### CU-22. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-22.1 Pedido desde el documento | regresion | Hay que corregir una proforma o una factura ya cerrada. | Solicitud con documento, motivo y quien pidio. Mes cerrado. |
| CU-22.2 Reabrir el mes | regresion | Alguien busca la clave o un boton para reabrir el periodo. | Periodo cerrado. |
| CU-22.3 Cascada hasta el mes viejo | no construir | Para tocar mayo habria que reversar junio, julio y agosto. | Sin reversa en cascada. |
| CU-22.4 Asiento nuevo de la correccion | no construir | La solicitud genera un comprobante de ajuste o de reversa. | Sin asiento nuevo. Gana CU-59. |
| CU-22.5 Primero se suelta la factura | construir | La proforma que se corrige ya tiene factura. | Factura libre y correccion pedida desde la proforma. |

### CU-23. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-23.1 Imputar sin planta | regresion | Se usa una cuenta o un comprobante. | Sin planta. |
| CU-23.2 Historial antes y despues | construir | Cambia un parametro. | Historial legible. Parametro vigente actualizado. |
| CU-23.3 Planta de vuelta | no construir | La imputacion vuelve a pedir planta. | Sin planta en la cuenta ni en el comprobante. |
| CU-23.4 Metadatos al usuario | no construir | El historial muestra nombres tecnicos de la base. | Historial sin metadatos. |

### CU-24. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-24.1 Comprobante de ajuste en mes cerrado | no construir | El mes ya esta cerrado y se corrige con un asiento de ajuste. | Sin asiento de ajuste. Gana CU-59. |
| CU-24.2 Asiento de reversa de la correccion | no construir | En mes abierto o cerrado la correccion nace como reversa contable nueva. | Sin asiento de reversa. Gana CU-59. |
| CU-24.3 Reabrir el mes para poder editar | no construir | Para corregir se abre el periodo. | Mes sin reapertura. Los dos vistos buenos viven en CU-38. Gana CU-59. |

### CU-25. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-25.1 Jose Tomas arma y aprueba | construir | Hay ingresos de contratistas para cerrar en una proforma. | Proforma aprobada por abastecimiento. |
| CU-25.2 Contabilidad calza monto y RUT | construir | Llega la factura y monto y proveedor coinciden. | Factura asociada. |
| CU-25.3 Monto o RUT distintos | construir | La factura no coincide en monto o en RUT. | Factura sin asociar. Proforma como estaba. |
| CU-25.4 Proforma asociada, se suelta la factura | construir | Hay que editar una proforma que ya tiene factura. | Factura suelta. La edicion sigue en CU-38 y CU-59. |
| CU-25.5 Contabilidad edita la proforma a sola | no construir | Contabilidad cambia la proforma ya asociada sin soltar la factura ni pasar por CU-38 y CU-59. | Proforma sin esa edicion directa. |

### CU-26. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-26.1 Gasto agrupado por centro | construir | El cierre trae varias proformas con centros distintos. | Lineas de gasto por centro. |
| CU-26.2 Auxiliar en el puente | construir | Facturas por recibir muestra que falta la factura de un contratista. | RUT en el auxiliar del puente. |
| CU-26.3 Proforma del bloque sin centro | construir | Una proforma que entra no tiene centro. | Esa linea no queda agrupada sin centro. |
| CU-26.4 Un asiento por cada proforma | no construir | Centralizar parte el cierre en un comprobante por proforma. | Sigue un asiento. |

### CU-27. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-27.1 Del 1 de enero al periodo | regresion | Se emite el balance de 8 del ano en curso. | Balance de 8 de ese rango. |
| CU-27.2 Cruce a otro ano | regresion | El mismo balance pide otro ano. | Sin balance cruzado. |
| CU-27.3 Rearmar ER o ESF aqui | regresion | Este informe se usa para rehacer el resultado del mes o la situacion financiera. | Balance de 8 solo. |

### CU-28. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-28.1 Asoex, gasto directo | regresion | La nota cobra un gasto, una a una. | Nota de gasto. Estado calzada o pendiente segun corresponda. |
| CU-28.2 Embarcador, facturas que un tercero pago | regresion | OPB pago facturas que ya estan en el sistema. | Nota de reembolso calzada, sin gasto duplicado. |
| CU-28.3 No calza | regresion | Una factura de la nota no existe o el total no cuadra. | Nota sin contabilizar. Facturas como estaban. |
| CU-28.4 Muchas filas por proveedores | construir | La temporada trae muchas facturas y hoy las cargan por contabilidad. | Carga en proveedores, no un segundo tipo de nota. |
| CU-28.5 Embarcador contabilizado como gasto nuevo | no construir | La nota del tercero vuelve a reconocer el gasto de facturas ya ingresadas. | Sin gasto duplicado. |

### CU-29. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-29.1 OC de tipo activo fijo | regresion | Se crea la orden y se marca activo fijo. | OC con el tipo, sin bien creado. |
| CU-29.2 Alta al marcar el tipo o al guardar | no construir | Elegir activo fijo, o guardar la OC, crea el maestro. | Sin maestro en ese momento. Gana CU-58. |
| CU-29.3 Activo sin OC | no construir | Se crea el bien y la OC se asocia despues, como se nombro el 27/10. | Sin alta sin OC. Gana CU-58. |

### CU-30. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-30.1 Se registra cuando se rinde | construir | Notaria o un abogado emitio la boleta y alguien la rinde. | Boleta ingresada, asociada a quien la rindio, sin folio emitido por Almahue. |
| CU-30.2 Nadie la rinde | construir | La boleta queda en el aire y nadie la rinde. | Estado pendiente de rendicion, sin documento cargado. |
| CU-30.3 Emitirla desde el ERP | no construir | Se intenta emitir la boleta de honorarios. | Sin folio de emision. |
| CU-30.4 Codigos que la sala dudo | no construir | Se fijan 1001, 1002 o 1003 porque se nombraron y despues se dudaron. | Sin codigo ni tasa inventados. |

### CU-31. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-31.1 Segunda carga del mes | regresion | La cartola semanal trae otra vez un movimiento ya subido. | Una sola fila. |
| CU-31.2 Borrar para limpiar el duplicado | regresion | Se elimina el movimiento ya contabilizado porque el archivo lo repite. | El contabilizado sigue. |
| CU-31.3 Insertar el repetido | regresion | La segunda carga agrega la misma fila. | Sigue una fila. |

### CU-32. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-32.1 Archivo de otro periodo | regresion | El periodo abierto no es el del archivo. | Sin carga silenciosa. |
| CU-32.2 Linea del mes anterior | regresion | Al final del archivo viaja el movimiento del mes previo. | Esa linea fuera. |
| CU-32.3 Carga silenciosa | regresion | El archivo de otro mes entra sin aviso, o la linea de arrastre entra. | Aviso presente y linea de arrastre fuera. |

### CU-33. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-33.1 Dos o tres partes, misma moneda | regresion | Un ingreso trae dos destinos, o tres. | Ingreso cuadrado, sin conversion. |
| CU-33.2 Suma que se pasa o que deja saldo | regresion | Las partes superan el movimiento, o queda un resto sin codigo. | Sin partida descuadrada. |
| CU-33.3 Convertir al partir | regresion | Dolares o yuanes se pasan a otra moneda para imputar. | Partes en la moneda del movimiento. |
| CU-33.4 Cuarta parte | regresion | El ingreso se abre en cuatro codigos. | Sin cuarta parte. |

### CU-34. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-34.1 Numero y nombre | regresion | Se mira la cuenta bancaria. | Los dos visibles. |
| CU-34.2 El nombre como otra cuenta | regresion | El nombre se usa como segundo identificador contable, o se inventa otra cuenta corriente del mismo banco. | Nombre solo para leer el numero. Sin cuenta extra. |
| CU-34.3 Solo el numero | regresion | La cuenta se muestra sin nombre. | El nombre sigue al lado. |

### CU-35. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-35.1 Precio de la guia o de la factura | regresion | Se devuelve mercaderia y se conoce la guia o la factura de llegada. | Devolucion valorizada al precio de origen. |
| CU-35.2 Sin guia ni factura de origen | construir | No hay documento de llegada para copiar el precio. | Sin devolucion valorizada al promedio por este hueco. |
| CU-35.3 Devolucion al promedio, consumo a FIFO o merma | no construir | La devolucion usa el promedio, el consumo pasa a FIFO, o se abre un movimiento de merma. | Devolucion fuera del promedio. Consumo en CU-55. Sin merma. |
| CU-35.4 Rebajar el stock de esa guia | no construir | Copiar el precio tambien descuenta la existencia de la guia. | Guia sin rebaja. Gana CU-56. |

### CU-36. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-36.1 Pantalla de proyectado | no construir | Se adelanta el modulo antes de la reunion con Lupe. | Sin pantalla. |
| CU-36.2 Columnas u horizonte inventados | no construir | Se elige un diseno para no llegar vacios a la reunion. | Sin diseno. |
| CU-36.3 Pagar o contabilizar para verlo | no construir | Se registra un pago o un asiento para simular el proyectado. | Sin pago y sin asiento de prueba. |
| CU-36.4 La cartola no se frena | regresion | La espera del proyectado bloquea la cartola que ya carga. | Cartola del 28/10 como esta. |

### CU-37. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-37.1 Traspaso sin reapertura | regresion | El cierre de contratistas ya centralizo. | Periodo cerrado en esa pantalla. |
| CU-37.2 Correccion desde la proforma | regresion | Hay que corregir una proforma cerrada. | Solicitud en la proforma. |
| CU-37.3 Clave o boton de vuelta | regresion | Traspaso vuelve a ofrecer reapertura. | Sin boton y sin clave ahi. |

### CU-38. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-38.1 Motivo y dos vistos buenos | regresion | Se pide la correccion con el periodo abierto o cerrado. | Solicitud incompleta si falta uno de los dos. |
| CU-38.2 Periodo cerrado sin clave | regresion | El periodo esta cerrado. | Mes cerrado. Solicitud igual, sin reapertura. |
| CU-38.3 Un solo visto bueno | regresion | Aprueba solo contratistas, o solo contabilidad. | Sin correccion habilitada. |
| CU-38.4 El resultado es un asiento nuevo | no construir | Despues de los dos vistos buenos nace un comprobante de ajuste. | Sin asiento nuevo. Gana CU-59. |

### CU-39. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-39.1 Asiento de ajuste al cerrar | no construir | Los dos vistos buenos ya estan y se genera un comprobante de ajuste. | Sin ese comprobante. Gana CU-59. |
| CU-39.2 Asiento de reversa de la proforma | no construir | Cerrar la reversa deja un asiento de reversa nuevo. | Sin asiento de reversa. Gana CU-59. |
| CU-39.3 Editar la linea dentro de este caso | no construir | Se aprovecha este acuerdo pisado para construir la linea editada. | Nada de este flujo viejo. Gana CU-59. |

### CU-40. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-40.1 Grilla del periodo | regresion | Se abre la grilla del mes. | Solo el periodo. |
| CU-40.2 Con factura vinculada | construir | La proforma tiene una factura asociada. | Vinculo visible. |
| CU-40.3 Sin factura | construir | La proforma no tiene factura. | Detalle sin recuadro de factura. |
| CU-40.4 Meses mezclados o factura vacia | no construir | La grilla trae otro periodo, o el recuadro aparece sin vinculo. | Grilla del periodo y recuadro solo con vinculo real. |

### CU-41. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-41.1 Calza y cubre | construir | Monto y periodo de la factura cubren la proforma. | Estado asociada. Correo intentado. |
| CU-41.2 Cobertura parcial | construir | La factura no cubre la proforma completa. | Vinculo 1 a 1 con cobertura parcial, por el monto que calzo, no por un porcentaje. |
| CU-41.3 Descuadre | construir | No calza: neto contra bruto, o un dia fuera de rango. | Estado descuadrada. Creador avisado. |
| CU-41.4 Segunda factura o factura reutilizada | construir | La proforma ya tiene factura, o la factura ya esta calzada con otra. | Sigue el vinculo anterior. La factura usada no reaparece para otra. |
| CU-41.5 Quien asocia y quien recibe | construir | Hay que asociar, o hay descuadre. | Asociacion hecha por contabilidad. Aviso en el creador. |
| CU-41.6 Campo porcentaje, o correo reemplazado | no construir | Se guarda un porcentaje, o el aviso interno sustituye al correo. | Sin porcentaje. Correo ademas del aviso interno. |

### CU-42. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-42.1 Con OC o con proforma | construir | La factura del libro tiene OC o proforma. | Asiento del libro. Estado contabilizada cuando el asiento existe. |
| CU-42.2 Sin OC ni proforma | regresion | La factura no tiene OC ni proforma. | Sin boton. Sin asiento de esta factura. |
| CU-42.3 Vista que falta | construir | Se mira el libro para una proforma o un proveedor. | Esas tres piezas en la vista. |
| CU-42.4 Contabilizar en contratistas | no construir | La factura de la proforma se contabiliza dentro del modulo de contratistas. | Factura sin asiento nacido en contratistas. |

### CU-43. Ola C

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-43.1 Hija por guia que no cierra | construir | Llega una guia que no cubre la madre. | Hija ligada a su guia, sin saldo. |
| CU-43.2 Ultima guia, por cantidad | construir | Es la ultima guia de esa compra y las cantidades ajustan la madre. | Madre ajustada una vez. |
| CU-43.3 Guia intermedia que ajusta | construir | Una guia que no es la ultima intenta ajustar la madre. | Madre sin ese ajuste. |
| CU-43.4 No cuadra ni con la ultima | construir | La ultima guia ajusta y aun asi no cuadra. | Madre nueva. La anterior con un solo ajuste. |
| CU-43.5 Porcentaje, cadena o saldo en la hija | no construir | Se usa un campo porcentaje, la hija entra a la cadena, o la hija queda con saldo. | Sin porcentaje, sin cadena de la hija y sin saldo en la hija. |

### CU-44. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-44.1 Con acceso al modulo | regresion | La persona tiene rol con acceso al modulo de la OC. | Puede entrar al grupo que corresponda. |
| CU-44.2 Sin acceso al modulo | regresion | El usuario no tiene rol de ese modulo. | Fuera del buscador del grupo. |
| CU-44.3 Emision no es aprobacion | regresion | Alguien debe crear la OC y no aprobarla. La aprobacion es de la jefatura. | Rol y grupo siguen siendo cosas distintas. |
| CU-44.4 Buscador vacio o cadena de OV | regresion | Quien si tiene acceso no aparece, o este buscador arma la cadena de la OV. | Lista de quien tiene acceso. OV sin cadena. |

### CU-45. Ola D

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-45.1 Arbol de lectura | regresion | Se abre el organigrama. | Vista informativa. |
| CU-45.2 El arbol elige aprobador o monto | regresion | La escala de la OC sale del organigrama. | Cadena intacta. El vinculo prohibido es CU-46. |
| CU-45.3 El arbol reemplaza los grupos | regresion | Se borra el grupo porque el arbol ya muestra la jefatura. | Grupos conservados. |

### CU-46. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-46.1 Escala leida del jefe | no construir | El jefe marcado en el arbol arma la escala de la OC. | Sin esa lectura. La OC sigue en su grupo. |
| CU-46.2 Monto copiado del organigrama | no construir | El tope sale del arbol. | Sin monto traido del organigrama. |
| CU-46.3 OV colgada del arbol | no construir | La orden de venta toma aprobadores del organigrama. | OV sin cadena. |
| CU-46.4 Grupo y escala que ya mandan | regresion | La OC se aprueba por su grupo. | Cadena donde ya esta. |

### CU-47. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-47.1 Articulo elegido del maestro | construir | Se recepciona una linea de guia. | Linea apuntando al articulo elegido, distinto del texto de la guia. |
| CU-47.2 Linea sin articulo | construir | La linea queda sin articulo del maestro. | Linea sin recepcion cerrada. |
| CU-47.3 Calce automatico | no construir | El sistema casa la linea por el codigo o por el nombre que trae la guia. | Sin match automatico. |
| CU-47.4 Stock al elegir | no construir | Elegir el articulo suma bodega. | Linea recepcionada sin stock. Gana el momento CU-57. |

### CU-48. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-48.1 Numeros del portal | no construir | Maria Jesus dejo pendiente el tema de numeros en AlmaWeb. | Sin pantalla de numeros del portal. |
| CU-48.2 Permisos de evidencias | no construir | El portal distingue administradores y la carga de evidencias de Paola. | Sin esos permisos mezclados aca. |
| CU-48.3 Usuarios del portal dentro del ERP | no construir | Un usuario o un permiso de AlmaWeb se copia al rol del ERP. | Roles del ERP sin esa copia. |
| CU-48.4 Duplicar lo ya resuelto | no construir | El documento de pendientes de Mario repite un punto que ya esta resuelto. | Sin ese retrabajo. |

### CU-49. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-49.1 Leer y escribir por rol | regresion | Alguien debe ver o editar una pagina. | Acceso por rol. |
| CU-49.2 Mantenedor fuera de la operacion | construir | El mantenedor de administradores por modulo sigue en el flujo diario. | Operacion sin ese mantenedor. |
| CU-49.3 Jefatura que administra o ve todo | no construir | La jefatura del area otorga el acceso en el momento, borra parametros, o ve la auditoria de todos los modulos. | Sin ese poder. Auditoria solo del propio modulo. |
| CU-49.4 Quienes parametrizan y no operan | construir | Gerencia general y jefatura de contabilidad configuran. | Dos cuentas de parametrizacion, sin nombre de persona en la maestra. |
| CU-49.5 Flag de administrador como cadena o como OV | no construir | El administrador por modulo aprueba, o este cambio pone cadena en la OV. | Flag sin poder de cadena. OV sin cadena. |

### CU-50. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-50.1 Un grupo por area | construir | Abastecimiento, comercial, COMEX, recursos humanos o contabilidad compran. | Grupo con jefatura del area y las dos gerencias. |
| CU-50.2 OC de un area sin grupo | construir | El area compra y no tiene grupo. | OC sin encolar a un grupo que no existe. |
| CU-50.3 Motor que ya existe | regresion | Los grupos siguen siendo el motor. | Grupos conservados. |
| CU-50.4 Quitar grupos, usar el arbol, o encadenar la OV | no construir | Se eliminan los grupos, la cadena sale del organigrama, o la OV entra a este esquema. | Grupos vivos. OV sin cadena. Arbol sin motor. |

### CU-51. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-51.1 Monto chico, igual la jefatura | construir | La OC no supera el tope de la jefatura del area. | OC en la jefatura. |
| CU-51.2 Supera el tope de la jefatura | construir | El monto supera el tope de esa jefatura. | Tres niveles, en ese orden, hasta el tope del ultimo. |
| CU-51.3 Falta la jefatura | construir | El grupo no tiene jefatura y la OC quiere saltar a gerencia. | OC sin avanzar al segundo nivel. |
| CU-51.4 Igual al tope de la jefatura | complemento | El monto es igual al tope de la jefatura, ni menor ni mayor. | Sin una regla nueva para el igual. |
| CU-51.5 Saltar jefatura, infinito, o cadena en la OV | no construir | La OC salta a gerencia, el ultimo aprueba sin techo, o la OV usa estos tres niveles. | Orden jefatura, gerencia de area, gerencia general. OV sin cadena. |

### CU-52. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-52.1 Bajo el tope del ultimo | construir | La OC no supera el tope del ultimo eslabon. | OC encolada. |
| CU-52.2 Sobre el tope | construir | La OC supera el tope del ultimo. El ejemplo de la sala fue 400 millones contra 4.000, y no es el parametro unico. | OC no encolada, sin fila en la bandeja. |
| CU-52.3 Igual al tope | complemento | El monto es igual al tope del ultimo. | Sin regla nueva para el igual. |
| CU-52.4 Ultimo sin numero de tope | complemento | El ultimo eslabon no tiene un monto cargado. | Sin aprobacion hasta infinito por campo vacio. |
| CU-52.5 Hasta infinito o aviso suave | no construir | El ultimo aprueba cualquier monto, o la OC entra igual y solo avisa. | Sin infinito y sin encolado por encima del tope. |

### CU-53. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-53.1 Tres topes | construir | Se parametriza un eslabon. | Tres montos. El de pesos conserva el monto de partida. |
| CU-53.2 Propuesta del dia | construir | La OC se escribe en pesos y el tope o el monto piden conversion. | Tipo propuesto, tipo guardado y fecha del dia. |
| CU-53.3 Falta el tope de esa moneda | construir | La OC esta en una de las tres monedas y el eslabon no tiene ese tope. | OC sin usar un tope ajeno. Si ademas se pasa el ultimo, vale CU-52. |
| CU-53.4 Recalcular, otra moneda o aprobador extra | no construir | El tipo guardado se recalcula solo, se agrega una moneda, o aparece un aprobador segun la moneda. | Tipo fijo. Sin moneda nueva y sin eslabon extra. |
| CU-53.5 Monto unico que ya esta | regresion | La escala de hoy tiene un solo monto. | Tope CLP de partida conservado. |

### CU-54. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-54.1 Receta de embalaje con centro | construir | Se guarda una receta. | Receta creada, con centro y sin packing obligatorio. |
| CU-54.2 Consumo por packing | construir | Se consume esa receta. | Consumo con packing y cantidad. El packing muestra quien consumio. |
| CU-54.3 Quien crea y quien consume | construir | Hay que crear la receta, o registrar el consumo. | Receta creada por la jefatura. Consumo pendiente de aprobacion. |
| CU-54.4 Packing obligatorio | no construir | La receta no se guarda si no tiene un packing. | Receta guardada sin ese obligatorio. |
| CU-54.5 Litros sumados con kilos | no construir | El consumo junta unidades distintas en un solo numero. | Cantidades separadas por unidad. |

### CU-55. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-55.1 Costo de bodega que ya se usa | regresion | El consumo de receta valoriza hoy con el costo de bodega. | Consumo sigue tomando costo de bodega. |
| CU-55.2 Promedio del stock del mes | construir | Se consume por receta, por orden de aplicacion o por ingreso manual. | Promedio del mes guardado en ese consumo. |
| CU-55.3 FIFO, guia puntual o precio escrito a mano | no construir | Se ofrece salir de la mas antigua a la mas nueva, tomar el precio de una guia, o editar el maestro para inventar el promedio. | Sin esas tres vias. |
| CU-55.4 Reescribir el mes o devolver al promedio | no construir | Al mes siguiente cambia el promedio y se reescribe el mes ya consumido, o la devolucion usa este precio. | Consumos viejos intactos. Devolucion fuera de este promedio. |

### CU-56. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-56.1 Documento nuevo al precio de la guia | construir | Se devuelve al proveedor y se busca la guia de llegada. | Devolucion nueva. Guia origen con la misma existencia. |
| CU-56.2 Unidades ya consumidas | construir | Esas unidades ya salieron de bodega. | Documento nuevo. Guia sin rebaja. |
| CU-56.3 No hay guia para el precio | construir | No se encuentra la guia de llegada. | Sin devolucion valorizada. |
| CU-56.4 Precio de origen que ya se toma | regresion | La salida ya puede tomar el precio de la guia o de la factura. | Precio de origen conservado. |
| CU-56.5 Rebaja, promedio, FIFO o merma | no construir | Se descuenta la guia, se usa el promedio, se sale por FIFO o se registra merma. | Guia intacta. Sin promedio, sin FIFO y sin merma. |

### CU-57. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-57.1 Registrar no suma | construir | La guia se registra y el articulo del maestro ya esta elegido. | Estado registrada. |
| CU-57.2 Confirmar suma | construir | Se confirma la recepcion, con articulo del maestro. | Estado confirmada, con cantidad, fecha y archivo. |
| CU-57.3 Confirmar sin articulo | construir | Se confirma una linea sin articulo del maestro. | Sigue sin stock. |
| CU-57.4 Stock al registrar | no construir | Registrar la guia, o solo adjuntar la foto, aumenta la bodega. | Stock sin cambio hasta confirmar. |

### CU-58. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-58.1 OC recepcionada con factura | construir | La OC es de activo fijo, esta recepcionada y ya tiene factura. | Bien en estado facturado, ligado a la OC y a la factura. |
| CU-58.2 Recepcionada sin factura | construir | Llego el producto y la factura no. | Bien en estado recepcionado, con el aviso. |
| CU-58.3 OC que no esta recepcionada | construir | Se intenta el alta con una OC de activo fijo no recepcionada. | Sin maestro. |
| CU-58.4 Vida util, sin centro, IPC y cierre | construir | El bien se da de alta o se cierra el mes. | Maestro con esos datos. Cierre con las tres piezas. Grafico como esta. |
| CU-58.5 Alta fuera de la OC recepcionada | no construir | Se crea al elegir el tipo, al guardar la OC, sin OC, solo con la factura, desde papel no digital, con centro de costo, o como insumo de bodega. | Sin ese maestro. El tipo en la OC sigue siendo CU-29. |
| CU-58.6 Grafico que ya esta | regresion | Se vuelve a construir el grafico mensual de depreciacion. | Grafico sin rehacerse. |

### CU-59. Ola A

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-59.1 Se edita la linea | construir | La correccion tiene motivo y los dos vistos buenos de CU-38. | La misma linea con el valor nuevo y el historial. |
| CU-59.2 Tenia factura | construir | La proforma corregida tenia factura. | Factura reasociada. Linea corregida. |
| CU-59.3 Mayor solo con activos | construir | Se consulta el libro mayor. | Mayor sin anulados ni pendientes. |
| CU-59.4 Otro comprobante o el mes reabierto | no construir | Nace un asiento de ajuste, uno de reversa, se reabre el periodo, o se edita el monto sin esta correccion aprobada. | Sin asiento nuevo y sin mes reabierto. Montos contabilizados sin edicion libre. |
| CU-59.5 Anular para corregir el monto | no construir | Se anula la fila en vez de editar la linea. | Linea no anulada por esta correccion. Gana el acto CU-60 si lo que se quiere es anular. |

### CU-60. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-60.1 La jefatura anula | construir | La jefatura de contabilidad anula, con motivo, sea cual sea el monto. | Estado anulado, con motivo, quien y cuando. Visible para auditoria. |
| CU-60.2 El analista solicita | construir | Quien no es jefatura quiere anular. | Solicitud pendiente hasta la jefatura. Despues, fila anulada. |
| CU-60.3 Asiento manual que no nace de un modulo | regresion | Hace falta un ajuste o una reclasificacion que no sale de un modulo. | Asiento manual disponible. Anular no lo reemplaza. |
| CU-60.4 Borrar, anular sin jefatura, o encadenar por monto | no construir | Desaparece la fila, el analista anula solo, o el monto arma una cadena. | Fila presente. Sin cadena de montos. |
| CU-60.5 Anular para cambiar el monto | no construir | Se anula porque el monto esta mal y no se quiere la correccion de la linea ni un asiento manual. | Monto sin cambio por esta via. El cambio de linea es CU-59. |

### CU-61. Ola B

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-61.1 Vista que ya existe | regresion | Se abre el organigrama. | Vista informativa. |
| CU-61.2 Cuatro titulos | construir | El arbol se nutre del jefe marcado en el usuario. | Esos cuatro titulos, sin efecto en la OC. |
| CU-61.3 El arbol aprueba o esconde los grupos | no construir | Los titulos definen la escala, o se ocultan los grupos porque el arbol ya esta. | Arbol sin monto y sin cadena. Grupos visibles. |

### CU-62. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-62.1 Emitir al SII | no construir | Se emite un DTE en GoSocket productivo. | Sin emision. |
| CU-62.2 Pedir folios desde el ERP | no construir | El ERP compra o pide CAF. | Sin pedido de folios. |
| CU-62.3 Recibir DTE esta semana como si el corte lo incluyera | no construir | Se adelanta la recepcion productiva para cerrar un modulo en este paquete. | Sin esa emision ni esa recepcion productiva en este corte. |

### CU-63. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-63.1 Reportes antes de cerrar el modulo | no construir | El modulo todavia no funciona y se arma su reporteria. | Sin reportes nuevos. |
| CU-63.2 Reporte sin la jefatura | no construir | Se disena lo que Maria Jesus ve, sin preguntar a la jefatura del area. | Sin ese paquete adelantado. |
| CU-63.3 La reunion como pantalla | no construir | La reunion con la jefatura se convierte en un modulo de reportes. | Sin pantallas de reporte nuevas. |

### CU-64. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-64.1 Carga del Excel que no llego | no construir | Se implementa la carga automatica de recetas. | Sin carga masiva. |
| CU-64.2 Columnas que el archivo traeria | no construir | Se agregan campos que la sala no nombro, a la espera del Excel o de la orden real. | Sin esas columnas. |
| CU-64.3 Orden manual con lo ya dicho | no construir | Se codea la orden de aplicacion solo con lo conversado, antes del documento real. | Caso en espera. Sin pantalla nueva. |
| CU-64.4 Elemento de costo ubicado por nosotros | no construir | El elemento va en la orden, o va en la linea, porque alguien lo elige. | Sin elemento de costo ubicado. |
| CU-64.5 Cadena de insumos o unidades sumadas | no construir | La orden pasa por la cadena de insumos, el centro va por linea, o se suman litros con kilos. | Sin cadena, sin centro por linea y sin suma de unidades distintas. |

### CU-65. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-65.1 Cuentas nuevas sin listado | no construir | Se completan las cuentas del cierre de bodega antes de que manden el detalle. | Cierre sin cuentas nuevas. |
| CU-65.2 Merma | no construir | La palabra merma, dicha al mirar el mapeo, abre una cuenta. | Sin cuenta de merma. |
| CU-65.3 Reemplazar los dos asientos | no construir | El listado pendiente sustituye el asiento de recepcion y el de calce. | CU-03 intacto hasta que llegue el listado. |

### CU-66. Fuera

| Escenario | Rama | Que se comprueba | Resultado que pasa |
|---|---|---|---|
| CU-66.1 Packing de cajas y pallets | no construir | Se construye en el ERP el packing externo de COMEX. | Sin ese modulo. |
| CU-66.2 Confundido con la receta | no construir | La receta de embalaje de CU-54 se trata como el packing de COMEX. | Receta sin convertirse en COMEX. |
| CU-66.3 Confundido con el packing del consumo | no construir | El packing que el consumo muestra, para saber quien consumio, se vuelve el packing externo. | Consumo sin heredar un modulo COMEX. |
