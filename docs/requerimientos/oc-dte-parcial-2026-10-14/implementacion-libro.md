# Implementacion libro: factura parcial sobre OC madre/hija

Fecha: 2026-10-14. Paso de libro de compras. No toca el dominio de compras (la hija sigue naciendo en la recepción), las proformas, las guías de insumos ni el cron de aceptación de 8 días. No hay migración. No se emite DTE ni se llama al SII.

## Funciones

| Funcion | Que hace ahora | CU |
|---|---|---|
| `calcularMatchFacturaOc` | Si la factura es menor que el neto de la OC y no supera el saldo (neto menos facturas no anuladas ya asociadas, tolerancia 1), no marca `MONTO_NO_COINCIDE` ni `CANTIDAD_NO_COINCIDE`. El estado queda `PENDIENTE`, no `ALERTA`. El calce del neto completo (tolerancia 1) sigue `VALIDADA`. El monto por encima del neto sigue `MONTO_NO_COINCIDE`. | CU-01, CU-02, CU-03, CU-07 |
| `assertFacturaCompletaOcHija` | Sigue corriendo solo si la OC vinculada ya es hija (`ocPadreId`). Una segunda factura no anulada deja `OC_HIJA_YA_FACTURADA`. El primer trozo, aunque el monto no sea el neto de la hija, no alerta. `OC_HIJA_PARCIAL` queda solo para esa segunda factura cuando la hija ya está cubierta por completo y el monto no es su neto. No se usa como alerta de "factura menor que la madre". | CU-04, CU-01, CU-02 |
| `buildMatchFacturaOcPatch` | Pasa a las dos funciones la suma y la cantidad de facturas no anuladas de esa OC (por `ocId` o `ocNumero`), sin contar el registro actual. Filtra por `empresaId`. | CU-01, CU-02, CU-04 |
| `preferirHijaAprobadaSinFactura` | Si el vinculo apunta a la madre y existe una hija `APROBADO` cuyo neto calza con la factura (tolerancia 1) y esa hija no tiene factura no anulada, devuelve la hija. Si no hay, devuelve la madre. No crea OC. | CU-01, CU-09 |
| `vincularOcRegistroCompra` | Sigue sin crear OC ni hija. Si el usuario elige la madre y hay hija que calza, escribe `ocId` y `ocNumero` de esa hija. Si no, el vinculo queda en la madre. | CU-09, CU-02 |
| `linkOrdenCompraFromReferencias` | Sigue sin crear OC ni hija. El sync aplica el mismo traslado a la hija que calza, y al completar un registro sin `ocId` guarda el numero de esa hija. | CU-09, CU-01 |
| `ordenesCompraCandidatasParaRegistro` | El listado manual ofrece OC abiertas (`sin cerradaAt`), no anuladas, que todavia no tienen una factura no anulada por su neto. Incluye madres con saldo e hijas sin facturar. No ofrece anuladas ni cerradas ya cubiertas. | CU-09 |
| `createRegistro` | Sin cambio de puerta: si la suma de facturas no anuladas supera el neto de la OC, rechaza. No nace hija ahi. | CU-03, CU-07 |

Proformas (CU-11), guias de insumos (CU-10) y `runAceptacionCompraAutoIfDue` no se modificaron.

## Ejemplo

Madre de 100.000 en `APROBADO`. Una recepcion confirmada de 50.000 ya dejo la hija `numero.1` en `APROBADO`, neto 50.000, sin factura. Llegan dos facturas de 50.000.

- La que se vincula mientras `.1` sigue sin factura no anulada se mueve a esa hija (`ocId` y `ocNumero` de `.1`). El match contra el neto de la hija es calce exacto: `VALIDADA`. No nace otra OC.
- La otra, vinculada cuando `.1` ya tiene esa factura, no encuentra hija libre con neto 50.000. Queda en la madre. 50.000 es menor que 100.000 y cabe en el saldo de la madre, así que no sale `MONTO_NO_COINCIDE` ni `CANTIDAD_NO_COINCIDE`. No nace `.2`: la hija del segundo trozo aparece al recepcionar, no al vincular.
