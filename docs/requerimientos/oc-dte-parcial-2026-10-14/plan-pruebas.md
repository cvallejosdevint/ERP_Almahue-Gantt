# Plan de pruebas: OC parcial, madre/hija y factura parcial

Fecha: 2026-10-14. Casos: `casos-de-uso.md` (CU-01 a CU-11). Encaje en el flujo actual: `plan-integracion.md`.

Este plan no se ejecuta aquí. No se emite DTE real, no se llama al SII y no se usa CAF. Cuando otro agente lo corra, la empresa es ALMAHUE EXPORT SPA, en local. La factura de proveedor entra por un registro manual del libro de compras o por un registro ya sincronizado. No se dispara emisión ni un evento a GoSocket para "ver qué pasa".

Cada caso se lee contra lo que dijeron Mario y Lupe en la sala. El cierre de saldo actual (`solicitarCierreSaldoOc`) no es el camino correcto de la parcial: ese resultado va en la columna de hoy para contrastar, y no acredita el caso.

## Cómo leer un resultado

Pasa solo la columna "Resultado esperado (sala)".

Estos hechos del código de hoy no son un pase:

- Dos facturas parciales quedan asociadas a la misma madre porque la suma no supera el neto (`createRegistro`).
- El match marca `MONTO_NO_COINCIDE` porque compara cada factura contra el neto completo. En la sala, una factura menor al saldo no es alerta (24/09): es el nacimiento de la hija.
- `solicitarCierreSaldoOc` crea una hija por el saldo no recibido, achica la madre y la devuelve a `PENDIENTE_APROBACION`. Esa hija es el documento al revés de CU-01 y de CU-08.
- `assertFacturaCompletaOcHija` alerta `OC_HIJA_PARCIAL` y `OC_HIJA_YA_FACTURADA` solo si la OC vinculada ya es hija (`ocPadreId`). Sobre la madre esas alertas no salen, y no reemplazan el caso.
- `createRecepcion` no crea hija. `vincularOcRegistroCompra` y el sync del XML (`linkOrdenCompraFromReferencias`) tampoco.

Fuera de este plan, porque la sala no lo pidió o lo dejó abierto:

- Servicios y activo fijo no tienen prohibida la hija. Esa prohibición está solo en el deck. No armar un caso que falle si un servicio se parte.
- "Una factura cubre varias hijas y no una hija en partes" es frase del deck. El caso de la sala es al revés en el origen: cada factura parcial crea su hija.
- No se elige sola la línea cuando el código del proveedor no es el de Almahue (P-15 lo deja explícito).
- No se baja la guía física como DTE código 52.

## Armado común de la madre

Salvo que el caso diga otra cosa:

1. OC en Compras, empresa ALMAHUE EXPORT SPA, estado final `APROBADO` (la cadena de la madre ya corrió).
2. Anotar número, neto, líneas, cuenta y centro de costo de cada línea.
3. No ejecutar `solicitarCierreSaldoOc` como paso de la parcial. Si se ejecuta, el resultado se anota solo en la columna de hoy.

La hija que pide la sala usa el número de la madre con sufijo `.1`, `.2` (en el ejemplo de la sala, 100.1 y 100.2). El correlativo nuevo `OC-AAAA-NNNN` es el comportamiento de hoy, no el esperado.

## Índice

| ID | CU | Qué se hace |
|---|---|---|
| P-01 | CU-01 | Dos DTE parciales seguidos de la misma madre |
| P-02 | CU-02 | Recepción de la parcial: nace la hija y solo ella se contabiliza |
| P-03 | CU-03 | Factura por el neto completo, sin hija |
| P-04 | CU-04 | Factura de una sola línea |
| P-05 | CU-04 | Segunda factura de la misma línea |
| P-06 | CU-04 | Factura de la otra línea completa la madre |
| P-07 | CU-05 | Digitar cantidades y al guardar nace la hija |
| P-08 | CU-06 | La hija no vuelve a aprobación |
| P-09 | CU-07 | Factura mayor que la OC |
| P-10 | CU-08 | Saldo que no va a llegar: se achica la madre |
| P-11 | CU-09 | Factura sin OC en el XML |
| P-12 | CU-09 | Factura de una OC que todavía está en aprobación |
| P-13 | CU-10 | Guías de bodega y una sola factura de fin de mes |
| P-14 | CU-11 | Proforma de contratistas: no se parte |
| P-15 | CU-04 | Dos líneas del mismo monto: el usuario elige la línea |
| P-16 | CU-07 | El aumento no alcanza el plazo: rechazar y pedir refacturación |

## P-01. Dos DTE parciales seguidos de la misma madre

- CU: CU-01. Al guardar cada recepción se apoya en CU-05. La hija queda aprobada por CU-06.
- Precondición: OC madre `APROBADO`, tipo servicio (factura directa, sin guía de bodega). Una línea, cantidad 10, neto 100.000. Es el ejemplo de la sala del 23/09 (OC 100 por 100.000 y 10 cajas), corrido como factura directa para no mezclarlo con las guías de P-13.
- Entrada: factura parcial neto 50.000 y cantidad 5, con referencia a la madre. Recepción: digitar 5 y guardar. Después, segunda factura neto 50.000 y cantidad 5, referencia a la misma madre. Recepción: digitar 5 y guardar.
- Hueco: no hay prueba de dos parciales seguidas. El único nacimiento de hija hoy es el cierre de saldo, y solo deja una hija activa.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue como OC de control, aprobada, sin asiento propio. Al calzar cantidad y monto con la segunda parcial, se cierra. | Sigue siendo la única OC. La primera recepción confirmada la pasa a `RECEPCIONADA`. No aparece 100.1 ni 100.2. |
| Hija | Al guardar la primera recepción nace la hija `.1` por 50.000 y cantidad 5, con la cabecera de la madre y el detalle recibido. Al guardar la segunda nace la hija `.2` por 50.000 y cantidad 5. Cada una queda aprobada, sin cadena. | No nace hija en el vínculo ni en la recepción. `vincularOcRegistroCompra` y el sync solo escriben `ocId` de la madre. `createRecepcion` deja `RecepcionOc` sobre la madre. |
| Contabilidad | Cada hija se contabiliza por su parcial. La madre no contabiliza. | Si la cuenta tiene par Facturas por recibir, el asiento cuelga de la madre: origen `RECEPCION:{id de la madre}:{recepcionId}`. La madre es el documento contable. |
| Alerta | Ninguna por ser menor al saldo. Menor es este caso. | Cada factura queda asociada a la madre (la suma 100.000 no supera el neto) y el match marca `MONTO_NO_COINCIDE` contra el neto completo. `OC_HIJA_PARCIAL` no sale: la madre no tiene `ocPadreId`. Con `ALERTA`, el libro no informa eventos a GoSocket. |
| Aprobación | Ninguna de las dos hijas entra a la bandeja ni pide PIN. La madre no vuelve a aprobación por estas dos parciales. | No hay hija que enviar. Si alguien pide el cierre de saldo después de la primera recepción, la madre vuelve a `PENDIENTE_APROBACION` y nace una sola hija `BORRADOR` por el saldo no recibido (50.000), con correlativo nuevo. La segunda llamada se rechaza porque ya hay una hija activa. |

## P-02. Se recepciona la parcial, nace la hija y solo la hija se contabiliza

- CU: CU-02.
- Precondición: otra OC madre `APROBADO`, factura directa. Ejemplo de la sala: cantidad 1.000, neto de esa cantidad. Cuenta de la línea con par Facturas por recibir, para poder ver el asiento.
- Entrada: una factura por cantidad 100 (monto de esas 100, menor que la madre). En la recepción, digitar 100 y guardar. No cargar una segunda factura en este caso.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Queda informativa, de control. No contabiliza. El 01/10 el cliente cierra con "Exacto": se contabilizan los hijos y la madre queda informativa; no se ve en un módulo que no sea insumos. | Pasa a `RECEPCIONADA`. Sigue siendo el documento de la recepción y del asiento. |
| Hija | Nace la hija 1 con la cabecera de la madre y el detalle de las 100. El saldo de la grande baja en esas 100. Una llegada posterior de 200 sería la hija 2; no hace falta correrla aquí si P-01 ya cubrió la segunda tanda. | `createRecepcion` confirma `RecepcionOc` sobre la madre. No hay `ocPadreId` nuevo. |
| Contabilidad | El asiento es solo el de la hija, por el monto de las 100. La madre queda en cero. | El asiento de la parcial sale con origen `RECEPCION:{id de la madre}:{recepcionId}` (debe gasto o existencia, haber Facturas por recibir), si la cuenta tiene ese par. Una factura posterior de esa OC debita esa Facturas por recibir y no vuelve a cargar el gasto. |
| Alerta | No hay alerta de "menor". | `MONTO_NO_COINCIDE` al asociar la factura de 100 contra el neto de las 1.000. |
| Aprobación | La hija queda aprobada. La madre sigue aprobada. | La madre no vuelve a la bandeja por esta recepción. |

## P-03. Factura por el neto completo, sin hija

- CU: CU-03.
- Precondición: OC madre `APROBADO`, tipo servicio, una línea, neto 80.000. Monto distinto del de P-01 para no reutilizar documentos.
- Entrada: una factura por 80.000, igual al neto, con referencia a la madre. Si se recepciona, la cantidad es el saldo completo.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Se cierra y se contabiliza en el acto. | Puede contabilizarse si está en estado que opera (`APROBADO`, `RECEPCIONADA`, `CONTABILIZADA`, `FACTURADO`). Si además se recepciona el total, `createRecepcion` confirma el saldo completo. |
| Hija | No nace hija. Este camino no es el de 100.1 y 100.2. | No nace hija por el vínculo ni por la recepción. Si después se pide cierre de saldo y lo recibido ya iguala el neto (tolerancia de 1 peso), `solicitarCierreSaldoOc` solo marca `cerradaAt` y no crea hija. |
| Contabilidad | Se contabiliza esa orden. | El asiento es el de la propia OC. En este calce, eso coincide con la sala. |
| Alerta | No aplica. El caso es el calce. | Match `VALIDADA` si moneda, monto y líneas calzan, con la tolerancia de 1 peso que usa el código. La entrada de la prueba es igualdad exacta, no un peso de diferencia. |
| Aprobación | No vuelve a la cadena. | No vuelve a `PENDIENTE_APROBACION` por este calce. |

## P-04. La factura cubre una sola línea de la madre

- CU: CU-04.
- Precondición: OC madre `APROBADO`, factura directa, dos líneas ya imputadas por quien creó la OC. Línea 1: cajas, cantidad 100, neto 40.000, cuenta C1, centro K1. Línea 2: bolsas, cantidad 50, neto 60.000, cuenta C2, centro K2. Neto de la madre: 100.000.
- Entrada: una factura de este mes por la línea 1, neto 40.000. En la recepción, digitar solo la cantidad de la línea 1 y guardar.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue abierta. Es la que manda: cuenta y centro de costo salen de la línea que dejó el usuario original. | Sigue siendo la única OC. Puede quedar `RECEPCIONADA` con una recepción de una sola línea. |
| Hija | Nace una hija con una sola línea (la 1), neto 40.000. Hereda C1 y K1. No hereda la línea 2. | La recepción puede guardar una sola línea, calzada por descripción, sin pasarse de la cantidad de esa línea. No nace hija de una línea. |
| Contabilidad | La hija se contabiliza con C1 y K1. Contabilidad no inventa la imputación. | El asiento de recepción, si sale, agrupa por cuenta y centro de costo de la línea, con origen en la madre. |
| Alerta | No hay alerta por traer solo la línea 1. | El match compara contra la OC completa y puede marcar `CANTIDAD_NO_COINCIDE` o `MONTO_NO_COINCIDE`. |
| Aprobación | La hija queda aprobada. La madre no vuelve a la cadena. | Sin hija y sin vuelta a la bandeja. |

Dejar esta madre abierta: P-06 la continúa. P-05 usa otra madre.

## P-05. Segunda factura de la misma línea

- CU: CU-04.
- Precondición: otra OC madre `APROBADO` con las mismas dos líneas de P-04 (C1/K1 por 40.000 y C2/K2 por 60.000). La línea 1 ya fue recepcionada en una hija por 40.000, o, si esa hija todavía no existe en el código, la línea 1 ya tiene una factura de 40.000 asociada. Preparar la segunda factura sobre esa misma línea 1.
- Entrada: segunda factura otra vez por la línea 1 (neto 40.000, o cualquier monto de esa misma línea). No usar la línea 2.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | No se completa. La línea 1 ya estaba tomada. | La OC madre sigue siendo el único destino del vínculo. |
| Hija | No nace otra hija de la línea 1. | No nace hija. La segunda factura se asocia a la madre si la suma no supera el neto 100.000. |
| Contabilidad | Esa segunda factura no se contabiliza como calce de la línea 1. | Puede quedar asociada. El asiento, si alguien fuerza la contabilización sobre la madre, no es un rechazo de "misma línea". |
| Alerta | Alerta o rechazo. La sala lo dice así: "no va a ser macho. Va a tener la alerta o la va a rechazar". | El match puede marcar `MONTO_NO_COINCIDE` porque no es el total de la madre. Eso no reconoce "segunda vez la misma línea". `OC_HIJA_YA_FACTURADA` no sale: la OC vinculada no es hija. |
| Aprobación | No se abre una modificación de la madre por este rechazo. | No hay vuelta a la cadena por esta segunda factura. |

`MONTO_NO_COINCIDE` no acredita este caso. Esa alerta también sale en P-01, donde la sala no quiere alerta.

## P-06. La otra línea completa la madre

- CU: CU-04. Continúa la madre de P-04 (línea 1 ya en su hija, línea 2 pendiente).
- Precondición: la madre de P-04 sigue abierta, con C2 y K2 en la línea 2.
- Entrada: factura por la línea 2, neto 60.000. Recepción: digitar solo la cantidad de la línea 2 y guardar.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Se completa. Sigue siendo la que manda la imputación. | La segunda factura se asocia a la misma madre si la suma no supera 100.000. No hay cierre por "líneas completas en hijas", porque no hay hijas. |
| Hija | Nace la hija de la línea 2, neto 60.000, con C2 y K2. | No nace hija. La recepción puede guardar la línea 2 por descripción. |
| Contabilidad | Esa hija se contabiliza con C2 y K2. | El asiento, si sale, sigue colgado de la madre. |
| Alerta | No hay alerta: la línea 2 todavía tenía saldo. | El match de cada factura parcial contra el neto completo puede seguir en `MONTO_NO_COINCIDE` o `CANTIDAD_NO_COINCIDE`. |
| Aprobación | La hija de la línea 2 queda aprobada sin cadena. | Sin hija nueva en la bandeja. |

## P-07. En la recepción se digitan las cantidades y al guardar nace la hija

- CU: CU-05.
- Precondición: OC madre `APROBADO`, factura directa, dos líneas. Cajas: cantidad 100, precio 1.000, neto 100.000. Bolsas: cantidad 50, precio 200, neto 10.000. Neto de la madre: 110.000. La factura referencia la madre. Si el XML no trajera la referencia, primero se asigna a mano (eso es P-11) y después se corre este caso.
- Entrada: factura parcial por 20 cajas y 10 bolsas, neto 22.000. Como el neto de la madre es mayor, se abre el detalle. El usuario digita 20 cajas y 10 bolsas (no el saldo completo) y guarda.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | No se vuelve a levantar el total (100 y 50). El saldo pendiente pasa a ser 80 cajas y 40 bolsas: cantidad original menos lo recepcionado en las hijas. | El saldo pendiente de la próxima recepción es la cantidad de la madre menos lo ya confirmado en `RecepcionOc`. La madre queda `RECEPCIONADA`. |
| Hija | Al guardar nace la hija con las dos líneas digitadas: 20 cajas y 10 bolsas, neto 22.000. Puede llevar más de una línea. Esto convive con P-04, donde la hija era de una línea porque la factura era de una línea. | No nace hija al guardar. Si el usuario manda líneas, se calzan por descripción y no pueden exceder lo ya confirmado más lo nuevo. Si no manda líneas, el sistema propone el saldo pendiente. |
| Contabilidad | Sigue CU-02: se contabiliza la hija, no la madre. | Asiento de recepción sobre la madre, si la cuenta tiene par Facturas por recibir. |
| Alerta | No hay alerta por digitar menos que el saldo. | `MONTO_NO_COINCIDE` en la factura de 22.000 contra 110.000. |
| Aprobación | La hija queda aprobada. | Sin hija en la bandeja. |

## P-08. La hija no vuelve a aprobación

- CU: CU-06.
- Precondición: OC madre `APROBADO`, tipo servicio, neto 100.000. La cadena de esa madre ya terminó.
- Entrada: una factura parcial menor, neto 30.000. Recepción de 30.000 y guardar. No pedir modificación de la madre.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue aprobada. No entra de nuevo a la bandeja. | Si solo se recepciona, pasa a `RECEPCIONADA` y no vuelve a `PENDIENTE_APROBACION`. |
| Hija | Se crea por 30.000 y queda aprobada, porque es parte de la madre que ya pasó la cadena. No recorre bandeja ni PIN. | `createRecepcion` no crea hija. El único nacimiento está en `solicitarCierreSaldoOc`: la hija de ese cierre queda `BORRADOR`, por el saldo no recibido (70.000), fuera de la bandeja hasta que alguien la envíe. |
| Contabilidad | Sin regla nueva en este caso. El asiento, si se mira, es el de P-02. | El asiento de la recepción cuelga de la madre. |
| Alerta | No hay alerta por ser menor. | `MONTO_NO_COINCIDE` en la factura de 30.000. |
| Aprobación | La cadena no corre para la hija. Vuelve a usarse solo si hay que editar el monto de la madre (P-09 al alza, P-10 a la baja). | Si se usa el cierre de saldo, la madre (el documento grande) vuelve a `PENDIENTE_APROBACION`. Es el documento al revés de este caso. `updateOrden` no deja editar una OC ya `RECEPCIONADA`, así que tampoco hay otro "solicitar modificaciones" de esa madre. |

## P-09. La factura trae más que la OC

- CU: CU-07. La vuelta a la cadena es la de CU-06 aplicada a la madre.
- Precondición: OC madre `APROBADO`. Ejemplo de la sala: quedó en 1.000 y la factura llega por 1.200. Usar neto 1.000.000 y cantidad 1.000. Dejar la escala de aprobación de ALMAHUE EXPORT SPA anotada (cortes de monto) antes de empezar.
- Entrada: factura por 1.200.000 y cantidad 1.200, con referencia a la madre. Intentar recepcionar esas 1.200. No guardar esa recepción. Después, el usuario pide modificar la madre al alza (no una OC nueva) para que la factura tenga espacio.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | No se recepciona de más. Queda pendiente de una modificación al alza, que es aprobación de la misma OC, no una OC nueva. Si el neto nuevo cruza un tramo de la escala (ejemplos dichos en la sala: de 1.000 a 10.000, o de 7.000 a 10.000), vuelve a la cadena de ese monto y quien pide explica el aumento. Para ver el cruce, repetir el mismo caso con un neto inicial bajo el corte vigente y una factura por encima de ese corte. | `createRecepcion` rechaza cantidad o monto por encima. Si la madre ya está `RECEPCIONADA`, `updateOrden` no la deja agrandar. No hay un pendiente de modificación distinto del cierre de saldo. |
| Hija | La parcial que no cabe queda en espera. No se aprueba ella. Se aprueba la modificación de la madre. No nace una hija por el exceso. | No hay hija del caso, así que no queda una hija "en el aire". El cierre de saldo, si hubiera recepción previa por menos, crearía hija por el faltante, no por este exceso. |
| Contabilidad | Mientras no calza, la factura no se contabiliza y los montos no coinciden. | `createRegistro` rechaza la asociación si la suma de facturas no anuladas supera el neto. Sin asiento de esa factura. |
| Alerta | El ERP marca en rojo que hay una factura que no cuadra con la OC. | Error al recepcionar o al asociar el exceso. No queda la marca roja dentro de un flujo de hija. |
| Aprobación | Vuelve la madre, no la factura. Si el trámite no alcanza el plazo en que el documento pasa solo, sigue P-16. | No hay bandeja de "modificación al alza" de una madre `RECEPCIONADA`. |

## P-10. Quedó saldo y no va a llegar: se achica la madre

- CU: CU-08. La aprobación de esa baja es CU-06.
- Precondición: OC madre que ya tiene recepcionado y facturado un trozo, con la hija de ese trozo según la sala. Neto original 100.000. Hija ya existente por 60.000. Quedan 40.000 que no van a llegar. No cargar otra factura.
- Entrada: el usuario pide cerrar porque el saldo no va a llegar. Es ausencia de factura, no un DTE nuevo.
- Variante, en otra OC: madre todavía `APROBADO`, sin recepción, y el usuario baja el monto. La sala pide aprobación también para menos.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Se modifica a la baja (queda en 60.000), pasa por aprobación y, al aprobar, se cierra saldada. | Con recepción `CONFIRMADA` y saldo mayor que 1 peso, `solicitarCierreSaldoOc` baja el neto de la madre a lo recibido, prorratea las líneas y la deja en `PENDIENTE_APROBACION`. |
| Hija | No nace una hija por los 40.000 que no van a llegar. La hija de los 60.000 ya recepcionados es lo que queda. | Nace una hija `BORRADOR` por los 40.000 no recibidos, correlativo nuevo `OC-AAAA-NNNN`, `ocPadreId` y `referenciaFolio` = número de la madre. Solo se permite una hija activa. La segunda llamada se rechaza. Si no hay recepción confirmada, el cierre ni siquiera abre. |
| Contabilidad | La sala no dicta un asiento de cierre. No se contabiliza un documento por el faltante. | No hay un asiento de cierre dicho en el flujo actual; el efecto observable es la hija `BORRADOR` y la madre achicada. |
| Alerta | No es alerta de factura. Es un cierre pedido por el usuario. | No marca `MONTO_NO_COINCIDE` por un DTE que no existe. El contraste está en el documento que nace. |
| Aprobación | La cadena es de la modificación de la madre, a la baja. En la variante sin recepción, la baja también vuelve a aprobación. | La madre vuelve a `PENDIENTE_APROBACION` por el cierre, y la hija del faltante queda `BORRADOR`. En la variante, `updateOrden` de una baja sobre una OC que sigue `APROBADO` no reabre la cadena: solo la subida pone `PENDIENTE_APROBACION`. |

Un pase de `solicitarCierreSaldoOc` (hija por el faltante) es un fallo de este caso.

## P-11. La factura llega sin OC en el XML

- CU: CU-09.
- Precondición: dos proveedores del maestro, en ALMAHUE EXPORT SPA. Proveedor A: sin OC abierta. Proveedor B: una OC madre `APROBADO`, neto 50.000, todavía sin factura asociada. Tener a mano otra OC del proveedor B que ya tenga factura, para comprobar que no sale en el listado.
- Entrada 1: factura del proveedor A, XML sin referencia de OC (registro manual o ya sincronizado, sin llamar al SII).
- Entrada 2: factura del proveedor B, XML sin referencia de OC, monto menor o igual; en este caso usar 50.000 para no abrir P-01 dentro del mismo paso. La asignación es a mano.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Entrada 1: no existe, y no se crea desde el libro. Quien pidió la compra la crea por el flujo normal, con su cadena, y avisa a quien contabiliza. Entrada 2: la OC abierta se asigna a mano. | Entrada 1: el registro queda sin `ocId`. Un número citado que no existe se guarda como texto, sin OC. Entrada 2: `vincularOcRegistroCompra` escribe la OC elegida en el registro. No crea OC. |
| Hija | No nace en este paso. Si después de asociar el monto fuera menor, el nacimiento sigue en P-02 y P-07. Con 50.000 iguales al neto, sigue P-03 y no nace hija. | El vínculo y el sync no crean hija. |
| Contabilidad | No se contabiliza hasta asociar OC o proforma. | Sin `ocId` no hay asiento. `assertOcParaRegistroCompra` exige OC en estado que opera para contabilizar. |
| Alerta | Dos alertas distintas. (1) Llegó la factura y no hay OC de ese proveedor. (2) Hay OC abierta, pero no venía referenciada, y hay que asignarla. El listado de la (2) muestra OC de ese proveedor abiertas y sin factura, no las ya asociadas. | Registro `EMITIDO` sin `ocId`. Aceptar o rechazar en GoSocket exige `ocId` y proveedor en el maestro; esta prueba no envía ese evento. Si el número de OC sí existe, hay aviso al generador (`resolveGeneradorOc`). |
| Aprobación | La OC nueva de la entrada 1 pasa por su cadena. Quien contabiliza no la salta. La entrada 2 no crea otra OC. | No se crea OC desde el libro, así que no hay cadena nueva por el registro. El cron de aceptación, a los ocho días, puede dar por aceptado el documento: eso no crea hija ni aprueba una OC. |

## P-12. Factura de una OC que todavía está en aprobación

- CU: CU-09, límite dicho el 14/09. No es un caso de hija.
- Precondición: OC en `PENDIENTE_APROBACION`, neto 40.000, mismo proveedor de la factura.
- Entrada: factura que referencia esa OC, neto 40.000. No rechazarla a mano. No aprobar la OC dentro de este caso.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue en aprobación. La factura no se rechaza sola y no se bloquea la aceptación del documento. Se destaca. | Se puede asociar. La UI marca `ocNoAprobada`. La OC sigue `PENDIENTE_APROBACION`. |
| Hija | No nace. | No nace. |
| Contabilidad | No se contabiliza mientras la OC no esté aprobada. | `assertOcParaRegistroCompra` no deja contabilizar fuera de `APROBADO`, `RECEPCIONADA`, `CONTABILIZADA`, `FACTURADO`. |
| Alerta | El documento queda destacado, en la misma familia que la factura sin OC. El 14/09 agregan que en la práctica sí llega factura de una OC todavía en aprobación, y que el 90% llega sin OC y queda pendiente de emitirla (la pendiente de emitir es la entrada 1 de P-11). | Destaque `ocNoAprobada`. A los ocho días, si nadie reclama, el cron puede aceptar el documento. Eso es aceptación del DTE, no creación de hija. |
| Aprobación | La OC sigue su cadena. El paso a los ocho días, si no se rechaza, es aceptación del documento. | El cron no manda la OC a `APROBADO`. |

## P-13. Insumos: varias guías en el mes y una factura al cierre

- CU: CU-10. Si la factura de cierre es menor que el saldo, el nacimiento de la hija es CU-02, disparado por esa factura y no por cada guía.
- Precondición: empresa con `recibeInsumosConGuia`. OC madre `APROBADO`, tipo insumos, 100 cajas a 1.000, neto 100.000. Bodega de insumos usable. Sin facturas previas de esta OC.
- Entrada: cuatro guías físicas de 10 cajas cada una, cargadas en insumos (no como DTE). Después, una factura de fin de mes por 40 cajas, neto 40.000, con referencia a la madre.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue siendo la referencia de la factura de fin de mes. Cada guía no se le asocia. | La guía no guarda `ocId`. La factura de 40.000, si se vincula, queda en esa madre. |
| Hija | Ninguna guía crea hija. La factura de 40.000 es menor que 100.000: al recepcionar contra esa factura nace una hija por 40.000 (40 cajas), no cuatro hijas. El cliente no dijo que la guía cree la hija. | `createGuiaInsumoRecibida` no crea hija ni recepción de OC. La factura vinculada tampoco crea hija. |
| Contabilidad | La bodega se actualiza con la guía. La sala no dicta el asiento de la guía. La asociación comercial con la OC es la factura, y el asiento de esa parcial es el de la hija (CU-02). | Cuatro movimientos `ENTRADA_PROVEEDOR` y cuatro guías en el listado. El precio de la guía puede leer una línea de OC `APROBADO` o `RECEPCIONADA` del mismo proveedor (`precioGuiaDesdeOrden`): eso no asocia la guía. El cierre de bodega centraliza movimientos y no es el asiento de la OC. Un `RecepcionOc` de compras, si alguien lo carga aparte, es otro documento. |
| Alerta | La sala no define una alerta para las cuatro guías. La factura de 40 sobre una madre de 100 no es alerta de "menor": es parcial (CU-02). | La factura de 40.000 asociada a la madre de 100.000 queda con alerta de monto (`MONTO_NO_COINCIDE`). `OC_HIJA_PARCIAL` no sale. |
| Aprobación | La guía no entra a la cadena. La hija de la factura de cierre, si nace, queda aprobada (CU-06). | Sin hija y sin bandeja nueva. |

No pedir a GoSocket las guías código 52. La sala dejó esa duda abierta.

## P-14. La proforma de contratistas no se parte

- CU: CU-11.
- Precondición: dos proformas de contratistas ya en el flujo de proforma (`DEFINITIVA` / enviadas al contratista, sin tratarlas como OC madre). Proforma X: 9.600. Proformas Y y Z: 4.000 y 5.600, suma 9.600. Ingreso diario de origen localizable en X.
- Entrada 1: factura del contratista por 5.600 contra la proforma X de 9.600. Es el ejemplo que María Jesús descartó.
- Entrada 2: otra factura por 9.600 que cubre Y y Z juntas.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | No hay OC madre. La entrada 2 calza una factura con N proformas. | La proforma puede apuntar a un `registroCompraId`. No se abre el flujo de OC madre. |
| Hija | No nace hija por la fracción 5.600, ni por cada proforma de la entrada 2. | No hay OC hija de una fracción de proforma. `solicitarCierreSaldoOc` no es el camino de la proforma. |
| Contabilidad | La sala no describe el asiento en este tramo. La asociación es proforma(s) aprobada(s) y enviada(s) contra la factura, en documentos recibidos. La entrada 1 no queda como parcial abierta. | Si una OC tuviera `referenciaTipo = PROFORMA_CONTRATISTA`, el asiento de compra usa la cuenta Facturas por recibir del tipo de contrato. Eso no parte la proforma. Anotar el asiento si aparece; no usarlo como prueba de hija. |
| Alerta | La entrada 1 no deja una parcial abierta. Se modifica la proforma X y el ingreso diario de origen, y esa modificación vuelve a aprobación. La entrada 2 calza y no alerta por "parcial". | No hay `OC_HIJA_PARCIAL` sobre una proforma. El plan de integración no describe una alerta de fracción; el fallo sería crear una hija o dejar la parcial abierta. |
| Aprobación | La proforma en disputa vuelve a aprobación. No es la bandeja de la hija de OC. La proforma no usa la cadena de OC para "aprobar el trozo". | La proforma pasa de `BORRADOR` a `DEFINITIVA` con permiso de contratistas, sin bandeja de cadena de OC. Contrastar si la modificación de X vuelve a aprobación: el caso de la sala lo pide. Hoy no hay hija que enviar a esa bandeja. |

## P-15. Dos líneas del mismo monto y código distinto: elige el usuario

- CU: CU-04, límite abierto el 23/09 y el 24/09. No es una regla de reconocimiento automático.
- Precondición: OC madre `APROBADO`, dos líneas con el mismo neto (20.000 y 20.000), cuentas y centros distintos (C1/K1 y C2/K2). El código de producto que trae la factura no es el código de Almahue en ninguna de las dos.
- Entrada: factura por 20.000, sin un código que designe la línea. Abrir la recepción y elegir la línea 2 a mano. Digitar la cantidad de esa línea y guardar.

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Sigue abierta. La imputación sale de la línea que el usuario eligió, no de un cálculo por monto igual. | Sigue siendo la única OC. |
| Hija | Si nace la hija de esta parcial, lleva la línea 2, con C2 y K2. El sistema no decide solo entre las dos líneas de 20.000. | No nace hija. La recepción calza por descripción cuando el usuario manda líneas. No hay regla automática por código de proveedor. |
| Contabilidad | La imputación de lo elegido es C2 y K2. | Si hay asiento de recepción, usa la línea que se haya guardado, colgado de la madre. |
| Alerta | No se exige una alerta nueva. El caso pasa si el usuario puede elegir y el sistema no asigna la línea por monto igual. Falla si la línea queda elegida sola. | Sin `OC_HIJA_PARCIAL`. El match de monto contra la madre completa puede alertar `MONTO_NO_COINCIDE`; eso no es el reconocimiento de la línea. |
| Aprobación | Sin cadena nueva. | Sin hija en la bandeja. |

Hasta un caso real de OC multi-línea, no se automatiza este reconocimiento. P-15 no se convierte en defecto por falta de matching automático.

## P-16. La modificación no alcanza el plazo: rechazar y pedir refacturación

- CU: CU-07, cierre del mismo caso cuando la aprobación de la madre no sale a tiempo.
- Precondición: el mismo descalce de P-09 (madre en 1.000, factura en 1.200) ya dejado pendiente, sin recepcionar de más y sin contabilizar. Anotar `aceptacionCompraPlazoDias` de la empresa (default 8 en el código). La sala habla de menos de siete días, porque después el documento pasa solo.
- Entrada: no aprobar la modificación de la madre dentro de ese plazo. No enviar evento a GoSocket ni al SII. Observar el estado del registro y de la OC cuando el plazo de aceptación se cumple (fecha del documento adelantada en el dato de prueba, o el criterio del cron, sin disparar un DTE nuevo).

| | Resultado esperado (sala) | Resultado que el código hace hoy |
|---|---|---|
| Madre | Conserva su saldo. No se agranda sola al vencer el plazo. | Sigue sin un camino de agrandar si ya está `RECEPCIONADA`. El vencimiento no modifica el neto. |
| Hija | No nace hija por el exceso ni por el plazo. | No nace hija. El cron no crea OC. |
| Contabilidad | La factura que no calza sigue sin contabilizarse. | Sigue sin asiento mientras la asociación del exceso esté rechazada o en alerta. |
| Alerta | Se rechaza y se pide que el proveedor refacture. La sala del 23/09 no dicta el código de reclamo GoSocket. | El cron de aceptación puede dar por aceptado el documento al cumplir `aceptacionCompraPlazoDias`. Eso es aceptación del DTE, no la refacturación que pide la sala. El reclamo GoSocket (evento 31, notas RCD / RFP / RFT) existe en `emitirGoSocketEventoRegistroCompra`; no usarlo como resultado esperado y no llamarlo en esta prueba. Con `ALERTA`, el libro no informa eventos. |
| Aprobación | La modificación de la madre que no alcanzó a aprobarse no autoriza el exceso. | El cron no aprueba la OC ni la modificación. |

## Orden sugerido cuando se ejecuten

1. P-11 y P-12. La factura sin OC, o con OC todavía en aprobación, no crea hija.
2. P-03. El total cierra sin hija, antes de mirar cualquier parcial.
3. P-13. En insumos la guía no es el disparador.
4. P-07, P-02 y P-01. Digitar, contabilizar la hija, y repetir con la segunda parcial.
5. P-08. Esa hija no entra a la bandeja.
6. P-04, P-05, P-06 y P-15. Líneas, segunda vez la misma línea, y elección manual.
7. P-09 y P-16. Exceso, modificación de la madre, plazo.
8. P-10 al final. Achicar la madre sin hija del faltante.
9. P-14 aparte. La proforma no entra en esta cadena.

## Qué anotar en el informe de ejecución

Por cada ID: número de la madre, neto, estado final de la madre, números de OC creadas en el paso (`ocPadreId`, estado, neto), asiento y su origen, `validacionFacturaEstado` y el motivo (`MONTO_NO_COINCIDE`, `OC_HIJA_PARCIAL`, `OC_HIJA_YA_FACTURADA`, `ocNoAprobada`), y si la madre o la hija aparecieron en la bandeja.

Si el único documento nuevo es una hija `BORRADOR` por el saldo no recibido, el caso de parcial (P-01, P-02, P-07) y el de cierre (P-10) quedan en fallo, aunque la función haya respondido 200.
