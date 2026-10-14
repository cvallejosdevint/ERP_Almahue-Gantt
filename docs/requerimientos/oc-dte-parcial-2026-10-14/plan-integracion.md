# Plan de integración: OC parcial, madre/hija y factura parcial

Fecha: 2026-10-14. Fuente de los casos: `casos-de-uso.md` (CU-01 a CU-11). Este documento dice dónde encaja cada caso en el flujo que el ERP ya tiene. No redefine pantallas ni propone código.

Empresa de prueba: ALMAHUE EXPORT SPA. No se emite DTE real ni se llama al SII. El DTE de proveedor entra por el libro de compras ya sincronizado (billing-gateway / GoSocket) o por un registro manual de ese libro.

## Ancla: qué hace el flujo hoy

Tres entradas de documento, y ninguna crea la hija del caso de la sala.

| Entrada | Dónde está | Qué deja |
|---|---|---|
| DTE de proveedor | Libro de compras. El sync (`linkOrdenCompraFromReferencias`, referencias del XML) y el vínculo manual (`vincularOcRegistroCompra`) escriben `ocId` / `ocNumero` en el registro. `createRegistro` hace lo mismo si el usuario carga la factura a mano. | La factura queda asociada a la OC que ya existe. No nace OC. |
| Recepción manual | Compras, `createRecepcion`. Exige OC `APROBADO` o `RECEPCIONADA`. Permite cantidades menores al saldo de cada línea (calce por descripción). Al confirmar pasa la OC a `RECEPCIONADA` y, si la cuenta de la línea es gasto o existencia con par Facturas por recibir (FxR), arma el asiento `RECEPCION:{ocId}:{recepcionId}`. | Movimiento de recepción sobre la misma OC. No nace hija. |
| Cierre de saldo | Compras, `solicitarCierreSaldoOc`. Solo sobre la madre, y solo si hay recepción `CONFIRMADA` y no hay otra hija activa. | La madre baja su neto a lo recibido y vuelve a `PENDIENTE_APROBACION`. La hija nace en `BORRADOR` por el saldo no recibido, con correlativo nuevo `OC-AAAA-NNNN` (`allocateOcNumero`), `ocPadreId` y `referenciaFolio` = número de la madre. No usa el sufijo 100.1. |

`assertFacturaCompletaOcHija` corre dentro de `buildMatchFacturaOcPatch` solo cuando la OC vinculada ya tiene `ocPadreId`. No crea nada. Si esa hija ya tiene otro registro no anulado, motivo `OC_HIJA_YA_FACTURADA`. Si el monto de la factura no es el neto de la hija, motivo `OC_HIJA_PARCIAL`. Esas alertas dejan `validacionFacturaEstado = ALERTA`. Con `ALERTA`, el libro no informa eventos a GoSocket.

Contabilizar una factura (`createRegistro` / `updateRegistro` a `CONTABILIZADA`) exige OC en estado que opera (`APROBADO`, `RECEPCIONADA`, `CONTABILIZADA`, `FACTURADO`): `assertOcParaRegistroCompra`. Asociar se permite también con OC aún no aprobada; la UI marca `ocNoAprobada`. El asiento de la factura, si ya hubo asiento de recepción de esa OC, debita la FxR de esa recepción y no vuelve a cargar el gasto. Si no hubo recepción contabilizada, debita la cuenta de la OC (cabecera o primera imputación de línea) contra proveedores e IVA.

La guía de insumos (`createGuiaInsumoRecibida`) es otra entrada: mueve stock `ENTRADA_PROVEEDOR` y lista la guía. No guarda `ocId`. Solo lee precio de líneas de OC `APROBADO` o `RECEPCIONADA` del mismo proveedor. El cierre de bodega centraliza movimientos; no es el asiento de la OC.

## CU-01. El proveedor factura en partes una OC grande

- Origen: DTE de proveedor, parcial, que en el ejemplo de la sala referencia la OC 100. Entra por libro de compras (sync de referencias o `vincularOcRegistroCompra`). No entra por el cierre de saldo.
- Módulo: compras (la madre ya aprobada, y las hijas que todavía no existen) y libro de compras (dos registros pueden quedar los dos asociados a la misma madre: `createRegistro` solo rechaza cuando la suma supera el neto). Contabilidad no tiene todavía un asiento por hija.
- Entra: madre aprobada por el total (ejemplo: 100.000 y 10 cajas) y una factura por una parte (50% ahora, 50% después).
- Sale hoy: las dos facturas colgadas de la madre, con alerta `MONTO_NO_COINCIDE` porque el match compara cada factura contra el neto completo. No salen 100.1 ni 100.2.
- Sale en el caso: madre de control, hija 100.1 por el monto de la primera factura, hija 100.2 por el resto. Si cantidad y monto calzan al final, la madre se cierra.
- Depende de CU-02 y CU-05 para que cada factura nazca como hija, y de CU-03 para no abrir hija cuando la factura trae el total. El descalce no es de este caso: sigue en CU-07 y CU-08.
- La alerta de "parcial" que hoy dispara `assertFacturaCompletaOcHija` no aplica aquí: la madre todavía no es hija.

## CU-02. Se recepciona la parcial, nace la hija y solo la hija se contabiliza

- Origen: recepción manual de una factura de monto menor que la OC. La factura puede haber llegado antes por el libro; la hija, en el caso, nace con el movimiento y el monto recepcionado.
- Módulo: compras (`createRecepcion`) y contabilidad (asiento de recepción y, después, asiento del registro de compra). Aprobaciones no intervienen en la hija (eso lo fija CU-06).
- Entra: madre ya aprobada. Ejemplo: mil cajas y factura por cien. El usuario recepciona cien.
- Sale hoy: una `RecepcionOc` confirmada sobre la madre, la madre en `RECEPCIONADA`, y el asiento de esa parcial con origen `RECEPCION:{id de la madre}:...` (debe gasto o existencia, haber FxR), si la cuenta tiene par FxR. La madre sigue siendo el documento contable. No hay hija.
- Sale en el caso: hija 1 con la cabecera de la madre y el detalle de lo recibido. El asiento es solo de esa parcial. La madre no contabiliza: queda informativa. El cliente lo cerró el 01/10 con "Exacto": la madre no se ve en un módulo que no sea insumos. Cuando llegan 200 más, hija 2, y el saldo de la grande baja. Menor que el saldo no es alerta: es este caso (24/09).
- Depende de CU-05 (el usuario digita cantidades y al guardar nace la hija) y de CU-06 (esa hija queda aprobada sin cadena). En insumos el disparador lo cambia CU-10: la guía no es esta recepción.
- Choque de asiento: hoy la recepción ya contabiliza la parcial, pero la cuelga de la madre. El caso pide el mismo monto en la hija y cero en la madre. La factura posterior, si la recepción ya posteó FxR, hoy debita esa FxR (`cuentaHaberRecepcion`) en vez de repetir el gasto.

## CU-03. Monto igual al de la OC: se cierra y se contabiliza, sin armar parcial

- Origen: DTE de proveedor por el total de la OC (libro de compras, sync o vínculo manual, o `createRegistro`).
- Módulo: libro de compras (match y contabilización) y compras (la misma OC, sin hija). Si además se recepciona el total, `createRecepcion` confirma el saldo completo.
- Entra: factura cuyo monto es el neto de la OC.
- Sale hoy: match `VALIDADA` si moneda, monto y líneas calzan (tolerancia 1 peso). Contabilizar exige OC que opera. `solicitarCierreSaldoOc`, si lo recibido ya iguala el neto (tolerancia 1), solo marca `cerradaAt` y no crea hija.
- Sale en el caso: la orden se cierra y se contabiliza. No nace hija. El 24/09 lo separan del camino 100.1 / 100.2.
- Debe evaluarse antes de CU-01 y CU-02. Si el monto iguala, no se abre el flujo de hija.
- No usa el cierre de saldo como generador de documento. El cierre actual, en este calce, ya se parece al caso: cierra y no crea hija. El asiento sigue siendo el de la propia OC, que en este caso es lo que la sala pide.

## CU-04. La madre tiene varias líneas y la factura cubre una sola

- Origen: DTE parcial asociado a una línea de la madre. Entra por libro de compras y, para armar el detalle, por la recepción de CU-05.
- Módulo: compras (líneas de la OC: cada una trae cuenta y centro de costo) y contabilidad (el asiento de la hija usa esa imputación). Libro de compras compara líneas con `CANTIDAD_NO_COINCIDE` cuando la cantidad de líneas o los totales no coinciden con la OC completa.
- Entra: madre con dos o tres líneas, ya imputadas por quien la creó. Factura de este mes por la primera línea.
- Sale hoy: la recepción parcial sí puede guardar una sola línea, calzada por descripción, sin pasarse de la cantidad de esa línea. El asiento de recepción agrupa por cuenta y centro de costo de la línea. No nace una hija de una línea. Una segunda factura de la misma madre se acepta mientras la suma no supere el neto; el match igual alerta porque no es el total.
- Sale en el caso: hija con una sola línea, cuenta y centro de costo heredados de esa línea de la madre. La madre sigue abierta y es la que manda: contabilidad no inventa la imputación. Si la segunda factura repite la línea 1, alerta o rechazo. Si llega por la línea 2, completa la madre con la imputación de la línea 2.
- Depende de CU-02 y CU-05. CU-05 admite hija de más de una línea (cajas y bolsas en la misma factura); CU-04 es el caso en que la factura trae una sola línea. Los dos quedan dichos.
- No se automatiza el reconocimiento de la línea cuando el código del proveedor no es el de Almahue, ni cuando dos líneas valen lo mismo. La sala lo dejó abierto el 23/09 y el 24/09: piden un caso real. Hasta ese caso, el usuario elige la línea en la digitación de CU-05.

## CU-05. En la recepción el usuario digita las cantidades por línea y al guardar nace la hija

- Origen: factura parcial que referencia la madre. Si el XML no trae la referencia, el usuario la asigna antes (CU-09). Si el neto de la madre es mayor que el de la factura, se abre el detalle para digitar cantidades. Eso es recepción manual, no el sync del DTE.
- Módulo: compras, `createRecepcion`. El comportamiento de cantidades ya está: si el usuario manda líneas, se calzan por descripción y no pueden exceder lo ya confirmado más lo nuevo; si no manda líneas, el sistema propone el saldo pendiente (cantidad de la OC menos lo ya confirmado).
- Entra: madre con códigos distintos (ejemplo: 100 cajas y bolsas) y factura por 20 cajas y 10 bolsas. El usuario digita solo esas cantidades.
- Sale hoy: `RecepcionOc` sobre la madre, madre `RECEPCIONADA`, asiento de recepción si corresponde. El saldo pendiente de la próxima recepción es la cantidad de la madre menos lo confirmado. No nace hija al guardar.
- Sale en el caso: al guardar, hija con esas cantidades y ese detalle (puede ser más de una línea). El saldo de la madre pasa a ser la cantidad original menos lo ya recepcionado en las hijas. No se vuelve a levantar el total de la madre.
- La contabilización de esa hija sigue CU-02. Si la última factura no cabe en el saldo, no se fuerza: pasa a CU-07.
- Dependencia con CU-10: en insumos este disparador no es la guía. La guía física no guarda la recepción de OC ni crea hija. El modal de cantidades, para el insumo, queda del lado de la factura de fin de mes, no de cada guía semanal.

## CU-06. La hija no vuelve a aprobación; la madre sí, cuando hay que modificarla

- Origen: la misma factura parcial menor que la madre (CU-02 / CU-05). No es un documento distinto.
- Módulo: aprobaciones de OC, sobre la madre. La cadena (`resolveCadenaAprobacion`, bandeja, PIN) ya existe para crear la OC y para dos ediciones: `updateOrden` de una OC `APROBADO` cuyo monto sube, y `solicitarCierreSaldoOc`.
- Entra: hija recién creada por una parcial, y madre que ya está aprobada.
- Sale hoy, si alguien usa el cierre de saldo: la madre (el documento grande) vuelve a `PENDIENTE_APROBACION` y la hija del saldo queda en `BORRADOR`, fuera de la bandeja hasta que alguien la envíe. Es el documento al revés del caso.
- Sale en el caso: la hija se crea y queda aprobada, porque es parte de la madre que ya pasó la cadena. No recorre bandeja ni PIN. La madre sigue aprobada. La cadena se vuelve a usar solo si hay que editar el monto de la madre (CU-07 al alza, CU-08 a la baja).
- `updateOrden` no deja editar una OC `RECEPCIONADA`. Como la primera recepción confirmada ya deja la madre en `RECEPCIONADA`, hoy no hay camino de "solicitar modificaciones" de esa madre salvo el cierre de saldo. CU-07 y CU-08 necesitan ese camino sobre la madre, sin convertir la hija en borrador.
- Una baja de monto sobre una OC que sigue `APROBADO` (todavía sin recepción) hoy no reabre la cadena: solo la subida pone `PENDIENTE_APROBACION`. CU-08 pide aprobación también a la baja.

## CU-07. La factura trae más que la OC

- Origen: DTE (y la recepción asociada) por encima del saldo. Entra al libro y se intenta recepcionar. No se guarda esa recepción de más.
- Módulo: compras (`createRecepcion` ya rechaza cantidad o monto por encima de la OC), libro de compras (`createRegistro` rechaza si la suma de facturas no anuladas supera el neto) y aprobaciones (modificación de la madre).
- Entra: hijas que ya consumieron saldo, y una última factura por más monto y más cajas (ejemplo: OC en mil, factura por mil doscientas).
- Sale hoy: error al recepcionar o al asociar el exceso. No queda un pendiente "en el aire" marcado en rojo dentro del flujo de hija, porque la hija del caso no existe. La madre `RECEPCIONADA` no se puede agrandar con `updateOrden`.
- Sale en el caso: la factura que no cabe queda pendiente, sin recepcionar de más y sin contabilizar. Alerta en rojo de factura que no cuadra con la OC. El usuario pide modificar la madre al alza (no una OC nueva). Si el monto nuevo cruza tramo de la cadena, vuelve a aprobación y quien pide explica el aumento. Si el trámite no alcanza el plazo en que el documento pasa solo (la sala habla de menos de siete días), se rechaza y se pide refacturación.
- El plazo de aceptación comercial del DTE ya está en el libro (`aceptacionCompraPlazoDias`, default 8) y en los eventos GoSocket. Ese plazo es aceptación del documento, no creación de hija ni aprobación de la OC. El reclamo GoSocket (evento 31, notas RCD / RFP / RFT) existe en `emitirGoSocketEventoRegistroCompra`; la sala del 23/09 no dicta ese código, dice rechazar y pedir que refacturen.
- Depende de CU-05 (saldo consumido por hijas) y de CU-06 (se aprueba la modificación de la madre, no la hija que no cupo). Mientras no calza, no hay asiento de esa factura.

## CU-08. Quedó saldo y no va a llegar otra factura: se achica la madre y se cierra

- Origen: ausencia de factura. Lo dispara el usuario, no un DTE ni una recepción.
- Módulo: compras y aprobaciones. El único cierre con saldo que existe es `solicitarCierreSaldoOc`.
- Entra: madre con recepciones confirmadas por menos que el neto, y la decisión de que no vendrá otra factura.
- Sale hoy: si el saldo es mayor que 1, la madre baja al neto recibido, sus líneas se prorratean a ese neto, vuelve a `PENDIENTE_APROBACION`, y nace una hija `BORRADOR` por el saldo no recibido. Solo se permite una hija activa. Si no hay recepción confirmada, el cierre ni siquiera abre.
- Sale en el caso: la madre se modifica a la baja, pasa por aprobación y se cierra saldada. No nace una hija por el saldo que no va a llegar. Las hijas ya recepcionadas (las del trozo facturado, CU-02) son lo que queda. No hay asiento de cierre dicho en la sala. No es alerta de factura.
- Este es el choque principal con el cierre actual. El caso de la sala y `solicitarCierreSaldoOc` no nombran el mismo documento: ver el cierre de este plan.
- Depende de CU-06 (la cadena es de la modificación de la madre) y de que CU-02 ya haya dejado las hijas de lo recibido. Sirve para más y para menos; el "más" es CU-07.

## CU-09. La factura llega sin referencia de OC

- Origen: DTE de proveedor vía billing-gateway / GoSocket, XML sin referencia de OC, o con un número que no existe en compras. El sync igual crea el registro (`estado EMITIDO`) y, si no hay calce, deja `ocId` vacío. El número citado que no existe se guarda como texto, sin OC.
- Módulo: libro de compras (`vincularOcRegistroCompra` para asignar a mano; `assertOcParaRegistroCompra` para no contabilizar sin OC). Compras solo entra cuando quien pidió la compra crea la OC por el flujo normal. Aprobaciones de esa OC nueva no se saltan.
- Entra: factura sin OC en el XML. No es, por sí sola, una parcial.
- Sale hoy: registro sin `ocId`, sin asiento. Aceptar o rechazar en GoSocket exige `ocId` y proveedor en el maestro. Hay aviso al generador de la OC cuando el número sí existe (`resolveGeneradorOc`). Asociar una OC no aprobada se permite y se destaca (`ocNoAprobada`). A los ocho días, si nadie reclama, el cron de aceptación puede dar por aceptado el documento: eso no crea hija.
- Sale en el caso: dos alertas distintas. (1) Llegó la factura y no hay OC de ese proveedor: Lupe no la crea desde el libro; se comunica con quien la pidió, esa persona crea la OC y avisa para contabilizar. (2) Hay OC abierta, pero no venía referenciada: se asigna a mano. El listado de candidatos son OC de ese proveedor abiertas y todavía sin factura, no las ya asociadas.
- No se automatiza: crear la OC desde el libro, ni nacer una hija en este paso, ni contabilizar antes de asociar OC o proforma. Si después de asociar el monto es menor, siguen CU-02 y CU-05. Si es igual, CU-03.
- El 14/09 agrega el mismo borde, sin hablar de hija: en la práctica llega factura de una OC que aún está en aprobación; no se rechaza sola; se destaca. El 90% sin OC queda pendiente de emitir la OC.

## CU-10. Insumos: varias guías en el mes y una factura al cierre, asociada a la OC

- Origen: guías físicas, cargadas a mano en insumos. No son un DTE de GoSocket en lo que dijo el cliente. La factura de fin de mes sí es DTE y entra por el libro de compras, referenciando la madre.
- Módulo: insumos (`createGuiaInsumoRecibida`, listado `getGuiasInsumoRecibidas`, movimiento `ENTRADA_PROVEEDOR`). La empresa tiene que tener `recibeInsumosConGuia`. Compras y libro entran solo con la factura de cierre. El precio de la guía puede salir de una línea de OC del proveedor (`precioGuiaDesdeOrden`); eso no asocia la guía a la OC.
- Entra: madre por 100 cajas; cuatro guías de 10 en el mes; al cierre, factura por 40.
- Sale hoy: cuatro movimientos de bodega y cuatro guías listadas, sin `ocId` y sin hija. La factura de 40, si se vincula a la madre de 100, queda asociada a esa madre con alerta de monto. La bodega se entera por la guía; el asiento de existencia de la OC, si alguien recepciona en compras, es otro documento (`RecepcionOc`).
- Sale en el caso: la guía no se asocia a la OC. La OC de las 100 sigue siendo la referencia de la factura de fin de mes. El cliente no dice que cada guía cree una hija. La bodega queda al día con la guía. La asociación comercial es la factura.
- Cambia el disparador de CU-05 en insumos. CU-05 hace nacer la hija al guardar la recepción de la OC. En insumos esa recepción no es la guía: la guía solo ingresa material. La digitación de cantidades y el nacimiento de la hija, si la factura de cierre es menor que el saldo, ocurren cuando llega esa factura (CU-02), no cuando se guarda cada guía. Lo que no es insumo sigue con factura directa, sin este desvío.
- No se automatiza traer la guía como DTE código 52. La sala duda si GoSocket traerá guías recibidas; no quedó regla. La devolución si se rechaza la factura se nombra solo para la sociedad con insumos (ALM). No se arma en este plan un rechazo automático de stock.
- El deck (guía asociada a la OC, "factura pendiente", una factura que cubre varias hijas) pierde contra esta transcripción del 01/10.

## CU-11. La proforma de contratistas no se factura parcial

- Origen: factura del contratista por el total de las proformas que se le enviaron en el mes. Entra a documentos recibidos. No entra al flujo madre/hija.
- Módulo: contratistas (proforma `BORRADOR` a `DEFINITIVA`, sin bandeja de cadena de OC). El asiento de compra, si la OC tiene `referenciaTipo = PROFORMA_CONTRATISTA`, usa la cuenta Facturas por recibir del tipo de contrato, no el par FxR de una recepción de insumos.
- Entra: N proformas del mes y una factura que tiene que calzar con ese total.
- Sale hoy: la proforma puede apuntar a un `registroCompraId`. No hay OC hija de una fracción de proforma.
- Sale en el caso: no hay madre ni hija. Si no calza, se modifica la proforma (y el ingreso diario de origen) y vuelve a aprobación. No queda una parcial abierta.
- No se automatiza con CU-01 a CU-08. María Jesús descartó el ejemplo (proforma 9.600 y factura 5.600).

## Dependencias

```
CU-09 asociar OC (sin crear hija)
    > CU-03 si el monto iguala el saldo: cerrar y contabilizar, sin hija
    > CU-02 / CU-05 si el monto es menor: digitar cantidades y nacer hija del trozo
        > CU-06 esa hija queda aprobada; la cadena queda para editar la madre
        > CU-01 se repite el ciclo (100.1, después 100.2) hasta calzar
        > CU-04 si la factura es de una línea: la hija hereda cuenta y centro de costo
        > CU-07 si la última no cabe: no recepcionar; modificar la madre al alza
CU-10 en insumos: la guía no dispara CU-05; la factura de fin de mes sí
CU-08 cuando no vendrá otra factura: achicar la madre, aprobar, cerrar, sin hija del saldo
CU-11 no entra a esta cadena
```

CU-04 no bloquea a CU-01: una hija puede ser de una línea o de varias, según lo que el usuario digite. El límite abierto de CU-04 (código del proveedor) no se resuelve con otro caso.

## Qué no se automatiza

- CU-11: la proforma no se parcializa ni genera hija. Una factura puede juntar N proformas; si no calza, se edita la proforma.
- CU-09: desde el libro no se crea la OC, no se crea la hija y no se contabiliza mientras no haya OC o proforma asociada. La asignación es manual. Quien pide la compra crea la OC y pasa por su cadena.
- CU-04: no se elige sola la línea cuando el código del proveedor no es el de Almahue, ni cuando dos líneas tienen el mismo monto.
- CU-10: no se baja la guía física como DTE ni se asocia cada guía a la OC.
- Servicios y activo fijo: el deck les prohíbe la hija. La sala no lo dice. No se agrega esa prohibición desde el deck.
- "Una factura cubre varias hijas, pero no una hija en partes": frase del deck, no de la transcripción. El caso es al revés en el origen: cada factura parcial crea su hija (CU-01), y una hija de una línea no acepta una segunda factura de esa misma línea (CU-04).
- No se emite DTE de venta ni se llama al SII para probar esto. ALMAHUE EXPORT SPA se usa con documentos de compra ya recibidos o con registro manual del libro.

## Dónde el caso de la sala choca con el cierre de saldo actual

`solicitarCierreSaldoOc` es el único lugar donde hoy nace una hija. El caso de la sala usa la hija para otra cosa.

| | Caso de la sala | Cierre de saldo actual |
|---|---|---|
| Qué es la hija | El trozo recepcionado y facturado (100.1, 100.2) | El saldo que no se recibió |
| Qué le pasa a la madre | Sigue de control, aprobada, sin asiento. Se cierra cuando calza o cuando el usuario la achica | Baja el neto a lo recibido y vuelve a `PENDIENTE_APROBACION` |
| Cuántas hijas | Una por factura parcial | Una sola activa; la segunda llamada se rechaza |
| Número | Sufijo de la madre (100.1) | Correlativo nuevo `OC-AAAA-NNNN` |
| Estado de la hija | Aprobada, sin cadena (CU-06) | `BORRADOR` |
| Cuándo nace | Al guardar la recepción del trozo (CU-05), o con la factura de fin de mes en insumos (CU-10) | Al pedir cierre, y solo si ya hay recepción confirmada |
| Saldo que no va a llegar (CU-08) | Se achica la madre, se aprueba y se cierra. No hay hija de ese saldo | La hija es precisamente ese saldo |
| Recepción | No crea hija | Sigue sin crear hija; el cierre es otro paso |

Otros choques del mismo circuito, fuera de esa función:

- La recepción confirmada ya contabiliza la parcial en la madre (asiento `RECEPCION:{madre}`) y la deja `RECEPCIONADA`. El caso contabiliza la hija y deja la madre sin asiento.
- `updateOrden` no edita una OC `RECEPCIONADA`, así que CU-07 (agrandar) y CU-08 (achicar) no tienen hoy un "solicitar modificaciones" distinto del cierre de saldo.
- Una baja de monto en OC todavía `APROBADO` no reabre la cadena. CU-08 pide aprobación también para menos.
- Dos DTE parciales pueden vincularse a la madre. El match los alerta (`MONTO_NO_COINCIDE`) y GoSocket no acepta con `ALERTA`. `OC_HIJA_PARCIAL` no sale en ese caso: la madre no tiene `ocPadreId`.
- La guía de insumos no es `createRecepcion`. Tratar la guía como el disparador de CU-05 contradice CU-10.

## Orden de integración propuesto

1. CU-09. Dejar la puerta como está: el DTE sin referencia se asigna a mano y no crea OC ni hija. Los casos siguientes solo corren después de esa asociación.
2. CU-03. Si la factura iguala el saldo, cerrar y contabilizar esa OC, sin hija. Así el caso fácil no cae en el flujo parcial.
3. CU-10. Fijar el disparador en insumos antes de cablear la hija: la guía mueve bodega; la factura de fin de mes es la que se asocia a la madre.
4. CU-05, CU-02 y CU-01, juntos. Al guardar la recepción del trozo (o, en insumos, al recepcionar contra la factura de cierre) nace la hija por ese monto, hereda la cabecera, y el asiento es de la hija. La madre queda de control. Se repite por cada factura parcial.
5. CU-06. Esa hija no entra a la bandeja. La cadena queda reservada a la modificación de la madre.
6. CU-04. La hija de una línea hereda cuenta y centro de costo. La segunda factura de la misma línea alerta o se rechaza. Sin reconocimiento automático de código ajeno.
7. CU-07. La factura que se pasa no se recepciona. Queda la alerta, se agranda la madre y vuelve a la cadena del monto nuevo. Si no alcanza el plazo de aceptación, rechazar y pedir refacturación.
8. CU-08 al final. Achicar y cerrar la madre con aprobación, sin hija del saldo que no llega. No reutilizar `solicitarCierreSaldoOc` tal como está: esa función crea la hija al revés.
9. CU-11 no se integra a este orden.
