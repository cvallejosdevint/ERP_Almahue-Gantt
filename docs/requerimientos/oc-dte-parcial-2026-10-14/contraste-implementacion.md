# Contraste de la implementacion: OC parcial, madre/hija y factura parcial

Fecha: 2026-10-14. Se leyo el codigo nuevo de Compras y del libro contra CU-01 a CU-11. La hija sigue naciendo al recepcionar el trozo. El vinculo y el sync no crean hija. No se emitio DTE ni se llamo al SII.

Conteo: 9 cumple, 2 parcial, 0 no cumple.

| CU | Juicio |
|---|---|
| CU-01 | parcial |
| CU-02 | cumple |
| CU-03 | parcial |
| CU-04 | cumple |
| CU-05 | cumple |
| CU-06 | cumple |
| CU-07 | cumple |
| CU-08 | cumple |
| CU-09 | cumple |
| CU-10 | cumple (fuera de este cambio) |
| CU-11 | cumple (fuera de este cambio) |

## CU-01. Parcial

La hija del trozo nace al guardar la recepcion confirmada de una madre, con numero `madre.1` y `madre.2`, estado `APROBADO`, cabecera de la madre y detalle digitado. Una factura menor que el saldo no marca `MONTO_NO_COINCIDE`. Si la factura calza con una hija aprobada que todavia no tiene factura, el vinculo la mueve a esa hija y no crea otra OC.

No cierra la madre sola cuando la segunda parcial completa cantidad y monto. La madre sigue en su neto y en `APROBADO`. Cerrarla, si lo recibido ya iguala el neto, es la rama de `solicitarCierreSaldoOc` que solo escribe `cerradaAt`.

- `compras.service.ts`: `createRecepcion`, `crearOcHijaDeRecepcion`, `recepcionEsTotalMadre`, `preferirHijaAprobadaSinFactura`, `vincularOcRegistroCompra`, `linkOrdenCompraFromReferencias`
- `libro-compras-factura-match.util.ts`: `calcularMatchFacturaOc`

## CU-02. Cumple

Recepcionar un trozo menor deja la `RecepcionOc` y, si la cuenta tiene par Facturas por recibir, el asiento con origen `RECEPCION:{id de la hija}:{recepcionId}` en la hija. La madre no pasa a `PENDIENTE_APROBACION` ni a `RECEPCIONADA` por ese trozo. Menor que el saldo no es alerta.

- `compras.service.ts`: `createRecepcion`, `updateRecepcion`, `planAsientoRecepcion`, `crearOcHijaDeRecepcion`
- `libro-compras-factura-match.util.ts`: `calcularMatchFacturaOc`

## CU-03. Parcial

Una sola recepcion que cubre el neto y agota las cantidades no crea hija: la recepcion y el asiento quedan en esa OC y pasa a `RECEPCIONADA`. El calce exacto del neto sigue `VALIDADA`.

No queda cerrada en el acto. Ni la recepcion total ni el registro de la factura escriben `cerradaAt`. Ese cierre sin hija solo ocurre si despues se llama `solicitarCierreSaldoOc` y lo recibido ya iguala el neto.

- `compras.service.ts`: `recepcionEsTotalMadre`, `createRecepcion`, `createRegistro`, `solicitarCierreSaldoOc`
- `libro-compras-factura-match.util.ts`: `calcularMatchFacturaOc`

## CU-04. Cumple

La hija de una sola linea copia cuenta y centro de esa linea de la madre. La madre no vuelve a la cadena por nacer esa hija. La segunda factura no anulada de una OC que ya es hija (`ocPadreId`) deja `OC_HIJA_YA_FACTURADA`. `OC_HIJA_PARCIAL` no sale por una factura menor que la madre: `buildMatchFacturaOcPatch` solo llama `assertFacturaCompletaOcHija` si hay `ocPadreId`, y ahi `OC_HIJA_PARCIAL` queda para una segunda factura cuando la hija ya esta cubierta y el monto no es su neto.

Elegir sola la linea cuando el codigo del proveedor no es el de Almahue sigue abierto, como lo dejo la sala. La recepcion calza por la descripcion que digita el usuario.

- `compras.service.ts`: `lineasConCuentaDeMadre`, `crearOcHijaDeRecepcion`, `buildMatchFacturaOcPatch`, `createRecepcion`
- `libro-compras-factura-match.util.ts`: `assertFacturaCompletaOcHija`, `calcularMatchFacturaOc`

## CU-05. Cumple

En la recepcion el usuario digita cantidades por linea. Al guardar un trozo confirmado de la madre nace la hija con esas lineas (una o varias) y el neto de lo digitado. La siguiente recepcion sin lineas propone el saldo: cantidad de la madre menos lo confirmado en la madre y en sus hijas. Digitar menos no es alerta. El exceso de cantidad o de monto se rechaza.

- `compras.service.ts`: `createRecepcion`, `updateRecepcion`, `saldoConfirmadoRecepcion`, `assertTopeRecepcion`, `crearOcHijaDeRecepcion`

## CU-06. Cumple

La hija nace `APROBADO`. No se llama `resolveCadenaAprobacion` ni se arma bandeja para ella. La madre no vuelve a aprobacion solo porque nace la hija. La cadena se vuelve a usar al modificar el monto de una OC `APROBADO`, al alza o a la baja.

- `compras.service.ts`: `crearOcHijaDeRecepcion`, `createRecepcion`, `updateOrden`

## CU-07. Cumple

No se guarda una recepcion por encima del saldo. El saldo de una madre suma las recepciones confirmadas de ella y de sus hijas no anuladas, asi que una madre que ya tuvo hijas no se infla por una recepcion de mas: no nace otra hija y el neto de la madre no cambia. `createRegistro` rechaza si la suma de facturas no anuladas supera el neto. El match de un monto por encima del neto sigue en `MONTO_NO_COINCIDE`.

Subir el monto de una OC `APROBADO` vuelve a `PENDIENTE_APROBACION` y rearma la cadena. Bajarlo tambien. No se crea otra OC.

- `compras.service.ts`: `assertTopeRecepcion`, `saldoConfirmadoRecepcion`, `createRecepcion`, `createRegistro`, `updateOrden`
- `libro-compras-factura-match.util.ts`: `calcularMatchFacturaOc`

## CU-08. Cumple

`solicitarCierreSaldoOc` achica la madre al neto ya recepcionado (madre mas hijas), la deja `PENDIENTE_APROBACION` y no crea hija por el faltante. Si la cadena tiene un paso, anula las filas anteriores no anuladas y deja la fila `PENDIENTE` del aprobador. Si lo recibido ya iguala el neto, solo marca `cerradaAt`. Sin recepcion confirmada el cierre no abre.

La baja de una madre que sigue `APROBADO`, aunque no tenga recepcion, vuelve a aprobacion por `updateOrden`. El boton del front dice "Achicar y enviar a aprobación" y el recibido suma madre e hijas.

- `compras.service.ts`: `solicitarCierreSaldoOc`, `updateOrden`, `scaleLineasCompraToNeto`
- `ComprasPages.tsx`: `recibidoConfirmadoOc`
- `compras-oc-helpers.ts`: `puedeSolicitarCierreSaldoOc`
- `CierreSaldoOcModal.tsx`

## CU-09. Cumple

El libro no crea OC ni hija. Si el XML no trae un numero que exista, el registro queda sin `ocId`. Asignar a mano escribe la OC elegida. Si esa OC es la madre y hay una hija aprobada sin factura cuyo neto calza, el vinculo pasa a la hija.

El listado manual ofrece OC sin `cerradaAt` y no anuladas, del proveedor, que todavia no tienen una factura no anulada por su neto. No ofrece cerradas ni anuladas. Sin `ocId` no se contabiliza.

- `asociar-oc-registro.util.ts`: `ordenesCompraCandidatasParaRegistro`
- `AsociarOcRegistroCompraModal.tsx`
- `compras.service.ts`: `vincularOcRegistroCompra`, `linkOrdenCompraFromReferencias`, `preferirHijaAprobadaSinFactura`, `assertOcParaRegistroCompra`
- `oc-estado.util.ts`: `ocPermiteAsociarFactura`, `ocNoAprobada`, `ocPermiteContabilizarOPagar` (factura de una OC que todavia esta en aprobacion: se asocia, se destaca, no se contabiliza, no nace hija)

## CU-10. Cumple, fuera de este cambio

La guia de insumos no se asocio a la OC y no se reimplemento. `createGuiaInsumoRecibida` no guarda `ocId`, no crea hija y no crea `RecepcionOc`. Mueve bodega con `ENTRADA_PROVEEDOR`. La factura de fin de mes, si despues se recepciona como trozo menor, nace hija por `createRecepcion` (CU-02), no por cada guia.

- `insumos.service.ts`: `createGuiaInsumoRecibida`, `precioGuiaDesdeOrden`

## CU-11. Cumple, fuera de este cambio

La proforma no se parte y no se reimplemento. No hay `ocPadreId` ni hija de una fraccion en Contratistas. Una factura puede juntar varias proformas. `solicitarCierreSaldoOc` no es el camino de la proforma.

- `contratistas.service.ts`: `updateProforma`, `marcarProformaDefinitiva`

## Correccion de este paso

El cierre ya achicaba la madre y no creaba hija por el faltante. Se dejo ese nacimiento como estaba. Se cerraron dos huecos que el contraste anterior marco CAMBIAR y el codigo nuevo todavia no hacia:

- Bajar el monto de una OC `APROBADO` vuelve a aprobacion, igual que subirlo. Un cambio solo de texto sigue aprobada.
- El cierre, cuando la cadena tiene un paso, escribe la fila de bandeja. Sin ese paso el estado sigue `PENDIENTE_APROBACION` y no hay fila, como antes.

La recepcion de mas sobre una madre que ya tiene hijas ya estaba rechazada. Se dejo un test que lo afirma.

Archivos corregidos:

- `ERP/erp_back/src/modules/compras/compras.service.ts`
- `ERP/erp_back/src/modules/compras/oc-parcial.compras.service.spec.ts`
- `ERP/erp_back/src/modules/compras/compras.service.spec.ts`

Pruebas corridas, solo el patron de estos casos, desde `ERP/erp_back` con `npx jest --runInBand`: 5 pasaron (baja, recepcion de mas con hija, cierre sin hija, cierre con fila de bandeja, edicion de solo texto) y la suba de monto que ya existia siguio pasando. No se corrio la suite entera.
