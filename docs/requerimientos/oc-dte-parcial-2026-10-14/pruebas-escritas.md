# Pruebas escritas: OC parcial madre/hija

Fecha: 2026-10-14. Cubren el comportamiento nuevo de `implementacion-compras.md` e `implementacion-libro.md`. No emiten DTE, no llaman al SII y no escriben en la base.

## Comando

Desde `ERP/erp_back`:

```
npx jest --runInBand --testPathPattern="libro-compras-factura-match.util.spec|compras.service.spec" --testNamePattern="P-0|OC parcial|factura menor|OC_HIJA"
```

Resultado de esta corrida: 15 passed, 0 failed. De esos, 14 son tests nuevos. El que ya existía y el filtro también tomó es `factura menor que el saldo no es descalce`. Ningún test nuevo quedó en rojo.

## Tests nuevos

Archivo `ERP/erp_back/src/modules/compras/oc-parcial.compras.service.spec.ts` (el nombre entra en el filtro `compras.service.spec`):

| Test | Resultado |
|---|---|
| P-01 dos recepciones de 50.000 crean hija .1 y .2 APROBADO y la madre sigue en 100.000 | Pasó |
| P-01 registrar factura de 50.000 no marca MONTO_NO_COINCIDE ni crea hija | Pasó |
| P-01 vínculo mueve la factura de 50.000 a la hija .1 y no crea .2 | Pasó |
| P-02 la recepción y el asiento RECEPCION quedan en la hija y la madre no vuelve a aprobación | Pasó |
| P-03 recepción por el neto completo no nace hija y la OC queda RECEPCIONADA | Pasó |
| P-05 segunda factura sobre una hija ya facturada alerta OC_HIJA_YA_FACTURADA y no nace otra hija | Pasó |
| P-07 recepcionar cajas y bolsas de menos nace la hija con ese neto y el saldo pendiente baja | Pasó |
| P-08 la hija nace APROBADO sin armar la cadena de aprobación | Pasó |
| P-09 recepcionar de más se rechaza y la suma de facturas que supera el neto se rechaza | Pasó |
| P-10 solicitarCierreSaldoOc achica la madre a lo recepcionado, la deja PENDIENTE_APROBACION y no crea hija del faltante | Pasó |

Archivo `ERP/erp_back/src/modules/compras/libro-compras-factura-match.util.spec.ts`:

| Test | Resultado |
|---|---|
| P-01 factura de 50.000 contra saldo de 100.000 no es MONTO_NO_COINCIDE | Pasó |
| P-03 calce exacto del neto sigue VALIDADA | Pasó |
| P-09 exceso sobre el neto sigue en descalce | Pasó |
| P-05 segunda factura no anulada alerta OC_HIJA_YA_FACTURADA | Pasó |

## Qué afirma cada caso

- P-01 / CU-01. Dos recepciones confirmadas de 50.000 sobre una madre de 100.000 crean `OC-100.1` y `OC-100.2`, ambas `APROBADO`. La madre no se actualiza (sigue en 100.000 y `APROBADO`). Registrar la factura de 50.000 deja `PENDIENTE` sin `MONTO_NO_COINCIDE` y no crea hija. Si ya existe la hija .1 de 50.000 sin factura, vincular esa factura la mueve a `.1` con match `VALIDADA` y no crea `.2`.
- P-02 / CU-02. La `RecepcionOc` y el origen del asiento `RECEPCION:{id de la hija}:{recepcionId}` quedan en la hija. La madre no pasa a `PENDIENTE_APROBACION`.
- P-03 / CU-03. Recepción por el neto 80.000 no llama a `ordenCompra.create`. La OC queda `RECEPCIONADA`. El calce exacto del neto sigue `VALIDADA`.
- P-05 / CU-04. Vincular una segunda factura a una hija que ya tiene una factura no anulada deja `ALERTA` con `OC_HIJA_YA_FACTURADA`. No nace otra hija. `assertFacturaCompletaOcHija` devuelve el mismo motivo.
- P-07 / CU-05. Recepcionar 20 cajas y 10 bolsas nace la hija `.1` con esas líneas, cuentas y centros de la madre, neto 22.000. La recepción siguiente sin líneas propone el saldo: 80 cajas y 40 bolsas, monto 88.000.
- P-08 / CU-06. La hija de 30.000 nace `APROBADO`. No se llama `resolveCadenaAprobacion` ni se consulta la escala.
- P-09 / CU-07. Recepcionar 1.200 sobre 1.000 lanza `BadRequestException` y no guarda recepción ni hija. Asociar una factura de 1.200.000 sobre un neto de 1.000.000 también se rechaza. En el match, el exceso sigue en `MONTO_NO_COINCIDE`.
- P-10 / CU-08. Con 60.000 ya recepcionados sobre 100.000, `solicitarCierreSaldoOc` deja la madre en neto 60.000 y `PENDIENTE_APROBACION`. No crea una hija por los 40.000 que no van a llegar.

Los tests de tope de cantidad P1-10 que ya estaban en `compras.service.spec.ts` no se modificaron. El filtro de esta corrida no los ejecuta (su nombre es `P1-10`, no `P-0`).
