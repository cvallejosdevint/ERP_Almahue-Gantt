# Resultados de pruebas: OC parcial, madre/hija y factura parcial

Fecha: 2026-10-14. Lectura: `plan-pruebas.md` (P-01 a P-16), `contraste-codigo.md`, `casos-de-uso.md`.

No se levanto el ERP. No se crearon OC en la base. No se pago ni se contabilizo ningun documento real. No se emitio DTE, no se llamo al SII y no se corrio `prisma migrate deploy`.

El veredicto de cada caso es contra lo que pidieron Mario y Lupe (y Maria Jesus en P-14). Un pase de `solicitarCierreSaldoOc` no acredita la parcial.

## 1. Comandos

Directorio: `E:\source\repos\Almahue\ERP\erp_back`. Runner: Jest (`npm test` es `jest --runInBand`).

### 1.1. Los dos specs, archivo completo

```
npx jest --runInBand --testPathPattern="libro-compras-factura-match.util.spec|compras.service.spec"
```

Resultado: fallo el conjunto. El spec de match paso. El spec de compras fallo por 13 tests que no son este tema (asiento sin cuenta, y el inbox GoSocket: `libroComprasSyncMeta` no esta en el mock, y aceptar o rechazar exige proveedor en el maestro).

```
Test Suites: 1 failed, 1 passed, 2 total
Tests:       13 failed, 70 passed, 83 total
Snapshots:   0 total
Time:        34.477 s
```

`libro-compras-factura-match.util.spec.ts`: PASS.

Esos 13 fallos no cambian el veredicto de P-01 a P-16. No se corrigio el spec.

### 1.2. Bloques que tocan este tema

```
npx jest --runInBand --testPathPattern="libro-compras-factura-match.util.spec" --verbose
npx jest --runInBand --testPathPattern="compras.service.spec" --testNamePattern="P1-10" --verbose
```

Match, 6 tests, todos pasaron:

```
PASS src/modules/compras/libro-compras-factura-match.util.spec.ts
Test Suites: 1 passed, 1 total
Tests:       6 passed, 6 total
Time:        5.482 s
```

Incluye `assertFacturaCompletaOcHija`: "rechaza segunda factura" (`100, 100, 1`) y "rechaza parcial" (`100, 50, 0`). Los dos solo comprueban `ok === false`. No nombran `OC_HIJA_YA_FACTURADA` ni `OC_HIJA_PARCIAL`. Esos textos los devuelve la funcion: previos mayor que 0, y monto distinto del neto de la OC que ya es hija. El spec no pasa por `ocPadreId`. Sobre la madre esas alertas no salen.

Recepcion parcial P1-10, 5 tests, todos pasaron (el resto del archivo quedo skipped por el filtro):

```
PASS src/modules/compras/compras.service.spec.ts
Test Suites: 1 passed, 1 total
Tests:       72 skipped, 5 passed, 77 total
Time:        6.9 s
```

- `P1-10 recepción parcial real`: acepta 40 de 100, rechaza 70 ya confirmados mas 40, y sin lineas recepciona el saldo pendiente (40). No crea `ordenCompra` ni `ocPadreId`.
- `P1-10 matching de 3 vías en createRegistro`: factura 800 contra recepcion 500 deja `matchOk` false y `matchDiff` 300. Si ambos son 800, `matchOk` true. No compara contra el neto completo de la madre y no crea hija.

### 1.3. Cierre de saldo / hija

Busqueda en `ERP/erp_back` de `solicitarCierreSaldoOc`, "cierre de saldo" y `cierreSaldo` en `*.spec.ts`: sin coincidencias.

No ejecutado. No hay spec de `solicitarCierreSaldoOc` ni de las hijas 100.1 y 100.2.

## 2. P-01 a P-16

Ninguno de estos 16 se corrio contra la base. La columna de hoy sale del codigo ya leido en `contraste-codigo.md`, mas lo que los specs de arriba si confirman (cantidades sobre la misma OC, match de 3 vias, y la alerta de una hija que ya existe).

| ID | Resultado que pidio el cliente | Resultado del codigo actual | Veredicto |
|---|---|---|---|
| P-01 | Dos recepciones seguidas de la misma madre (50.000 y cantidad 5, dos veces) nacen la hija `.1` y la hija `.2`, aprobadas, sin alerta por ser menor y sin bandeja. La madre sigue de control y se cierra al calzar. | Las dos facturas quedan en la madre si la suma no supera 100.000. Cada match puede marcar `MONTO_NO_COINCIDE`. La primera recepcion confirmada deja la madre `RECEPCIONADA`. No hay `.1` ni `.2`. `OC_HIJA_PARCIAL` no sale. | no cumple |
| P-02 | Recepcionar 100 de 1.000 nace la hija 1. El asiento es solo de esa hija. La madre no contabiliza y no vuelve a la bandeja. Menor no es alerta. | `RecepcionOc` sobre la madre, estado `RECEPCIONADA`. Si la cuenta tiene par Facturas por recibir, el origen es `RECEPCION:{id de la madre}:{recepcionId}`. La factura de 100 contra el neto de 1.000 queda `MONTO_NO_COINCIDE`. No hay `ocPadreId` nuevo. | no cumple |
| P-03 | Factura igual al neto: se cierra y se contabiliza esa orden. No nace hija. No vuelve a la cadena. | El vinculo y la recepcion no crean hija. Match `VALIDADA` si moneda, monto y lineas calzan (tolerancia 1). El asiento es el de esa OC. `createRegistro` no escribe `cerradaAt`. | parcial |
| P-04 | Hija de una sola linea, neto 40.000, hereda cuenta C1 y centro K1. La madre sigue abierta. Sin alerta por traer solo esa linea. | `createRecepcion` puede guardar esa linea, calzada por descripcion. El asiento, si sale, agrupa por esa cuenta y ese centro, colgado de la madre. No nace hija. El match contra la OC completa puede marcar `CANTIDAD_NO_COINCIDE` o `MONTO_NO_COINCIDE`. | no cumple |
| P-05 | Segunda factura de la misma linea: alerta o rechazo. No nace otra hija. No se contabiliza como calce. No se modifica la madre. | La segunda factura se asocia a la madre si la suma no supera el neto. No hay rechazo de "misma linea". `OC_HIJA_YA_FACTURADA` no sale: la OC vinculada no es hija. `MONTO_NO_COINCIDE` no acredita este caso. | no cumple |
| P-06 | La factura de la otra linea nace una hija con C2 y K2 y completa la madre. Sin alerta. Hija aprobada sin cadena. | La segunda factura se asocia a la misma madre. La recepcion puede guardar la linea 2 por descripcion. No hay hijas ni cierre por lineas completas. | no cumple |
| P-07 | Al guardar 20 cajas y 10 bolsas nace la hija con esas dos lineas (neto 22.000), aprobada. El saldo pasa a 80 y 40. Sin alerta por digitar menos. | El pendiente de la proxima recepcion es la cantidad de la madre menos lo confirmado en `RecepcionOc`. Eso si lo cubre el spec P1-10. No nace hija. La factura de 22.000 contra 110.000 puede quedar `MONTO_NO_COINCIDE`. | parcial |
| P-08 | La hija de 30.000 queda aprobada, sin bandeja ni PIN. La madre sigue aprobada. La cadena vuelve solo si hay que editar el monto de la madre. | La recepcion no crea hija y pasa la madre a `RECEPCIONADA`. El cierre de saldo, si se usa, devuelve la madre a `PENDIENTE_APROBACION` y crea una hija `BORRADOR` por el faltante (70.000). `updateOrden` no edita una OC `RECEPCIONADA`. | no cumple |
| P-09 | No se guarda la recepcion de mas. La factura queda en rojo, sin contabilizar. Se modifica la misma madre al alza y, si cruza tramo, vuelve a la cadena. No nace hija por el exceso. | `createRecepcion` rechaza cantidad o monto por encima. `createRegistro` rechaza si la suma supera el neto. `vincularOcRegistroCompra` y el sync no aplican ese tope. Si la madre ya esta `RECEPCIONADA`, `updateOrden` no la agranda. | parcial |
| P-10 | La madre baja a lo recibido (ejemplo 60.000), pasa por aprobacion y se cierra. No nace hija por los 40.000 que no llegan. La baja sin recepcion tambien vuelve a aprobacion. | Con recepcion confirmada y saldo mayor a 1, `solicitarCierreSaldoOc` achica la madre y crea una hija `BORRADOR` por el faltante, correlativo nuevo. Sin recepcion confirmada el cierre no abre. Una baja con `updateOrden` sobre una OC `APROBADO` no reabre la cadena. Este cierre no tiene spec: no ejecutado como prueba, y como comportamiento es el documento al reves. | no cumple |
| P-11 | Sin OC del proveedor no se crea desde el libro. Con OC abierta sin referencia se asigna a mano. El listado son OC abiertas y sin factura. No nace hija. No se contabiliza sin OC. | El sync deja el registro `EMITIDO` sin `ocId` si el numero no existe. El vinculo escribe la OC elegida y no crea otra. Sin `ocId` no hay asiento. El listado de candidatas incluye OC ya facturadas y cerradas. No hay dos alertas distintas. | parcial |
| P-12 | Se asocia la factura de una OC `PENDIENTE_APROBACION`. No se rechaza sola. Se destaca. No se contabiliza. No nace hija. La OC sigue su cadena. A los ocho dias, si pasa algo, es aceptacion del documento. | Se puede asociar. La UI marca `ocNoAprobada`. No se contabiliza. No nace hija. El cron puede poner `ACEPTADA_PLAZO` y no pasa la OC a `APROBADO`. | cumple |
| P-13 | Cuatro guias no se asocian a la OC ni crean hija. La factura de 40.000 sobre 100.000, al recepcionar, nace una hija por 40, aprobada. La bodega se mueve con la guia. | `createGuiaInsumoRecibida` no guarda `ocId` ni crea hija. La factura de 40.000 vinculada a la madre queda con `MONTO_NO_COINCIDE` y sin hija. | parcial |
| P-14 | La proforma no se parte. La factura de 5.600 no deja una parcial de la proforma de 9.600: se modifica la proforma y vuelve a aprobacion. La factura de 9.600 puede cubrir dos proformas. | No hay OC hija. El vinculo rechaza si la suma de proformas supera el neto de la factura. `updateProforma` solo edita `BORRADOR`. No es la bandeja de OC. | parcial |
| P-15 | El sistema no elige solo entre dos lineas del mismo monto. El usuario digita la linea 2 y la imputacion es C2 y K2. | No hay regla por codigo de proveedor ni por monto igual. `createRecepcion` calza por la descripcion que manda el usuario. No nace hija. | parcial |
| P-16 | Al vencer el plazo la madre conserva el saldo, no se agranda sola y no nace hija. La factura que no calza sigue sin contabilizarse. Se rechaza y se pide refacturacion. | El vencimiento no modifica el neto y no crea hija. El cron puede dejar `ACEPTADA_PLAZO`: eso es aceptacion del documento, no la refacturacion de la sala. | parcial |

Conteo contra la sala: 1 cumple (P-12), 7 no cumple (P-01, P-02, P-04, P-05, P-06, P-08, P-10), 8 parcial (P-03, P-07, P-09, P-11, P-13, P-14, P-15, P-16).

## 3. Cierre

El comportamiento actual no implementa la hija por el trozo facturado. Las pruebas existentes que pasen solo confirman el cierre de saldo y las alertas de hija ya existente.
