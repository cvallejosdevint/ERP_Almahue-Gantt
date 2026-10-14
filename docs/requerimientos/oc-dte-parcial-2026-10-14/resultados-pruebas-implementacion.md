# Resultados de pruebas: OC parcial madre/hija

Fecha: 2026-10-14. Corrida desde `ERP/erp_back` con `npx jest --runInBand`, en este orden. No se emitio DTE, no se llamo al SII, no se corrio `prisma migrate deploy` y no se escribio en la base. No se corrio la suite entera de `compras.service.spec` sin filtro. No hubo que corregir tests ni codigo: los tres comandos pasaron a la primera.

## Comandos

| # | Comando | Resultado |
|---|---|---|
| 1 | `npx jest --runInBand --testPathPattern="oc-parcial.compras.service.spec"` | 13 passed, 0 failed. Suite `oc-parcial.compras.service.spec.ts` en 6.7 s. |
| 2 | `npx jest --runInBand --testPathPattern="libro-compras-factura-match.util.spec"` | 14 passed, 0 failed. Suite `libro-compras-factura-match.util.spec.ts` en 5.2 s. |
| 3 | `npx jest --runInBand --testPathPattern="compras.service.spec" --testNamePattern="P1-10\|P0-3"` | 13 passed, 80 skipped, 0 failed. La suite `compras.service.spec.ts` paso los 13 del filtro (bloques `P0-3 createRecepcion`, `P0-3/P0-4 updateRecepcion`, `P1-10 recepcion parcial real` y `P1-10 matching de 3 vias`). `oc-parcial.compras.service.spec.ts` entro al patron de ruta y Jest la dejo skipped porque ninguno de sus nombres es `P1-10` ni `P0-3`. |

## Veredicto P-01 a P-10

Estos casos viven en el spec de OC parcial y en el de match de factura. El tercer comando no los ejecuta: su filtro es `P1-10` y `P0-3`, no `P-0`.

| Caso | Veredicto |
|---|---|
| P-01 | Paso. Dos recepciones de 50.000 crean hija `.1` y `.2` en `APROBADO` y la madre sigue en 100.000. La factura de 50.000 no marca `MONTO_NO_COINCIDE` ni crea hija. El vinculo la mueve a `.1`. En el match, 50.000 contra saldo 100.000 no es `MONTO_NO_COINCIDE`. |
| P-02 | Paso. La recepcion y el asiento `RECEPCION` quedan en la hija. La madre no vuelve a aprobacion. |
| P-03 | Paso. La recepcion por el neto completo no nace hija y la OC queda `RECEPCIONADA`. El calce exacto del neto sigue `VALIDADA`. |
| P-05 | Paso. La segunda factura sobre una hija ya facturada deja `OC_HIJA_YA_FACTURADA` y no nace otra hija. |
| P-07 | Paso. Recepcionar cajas y bolsas de menos nace la hija con ese neto y el saldo pendiente baja. |
| P-08 | Paso. La hija nace `APROBADO` sin armar la cadena. |
| P-09 | Paso. Recepcionar de mas se rechaza y la suma de facturas que supera el neto se rechaza. Bajar el monto de una madre `APROBADO` vuelve a aprobacion. Una madre con hijas no acepta una recepcion por encima del saldo. El exceso sobre el neto sigue en descalce. |
| P-10 | Paso. `solicitarCierreSaldoOc` achica la madre a lo recepcionado, la deja `PENDIENTE_APROBACION` y no crea hija del faltante. Con cadena, el cierre deja la fila pendiente. |

## Parciales que quedaron fuera de esta corrida

El contraste dejo abiertos dos parciales. Esta corrida no los implemento y los tests que pasaron no los cierran.

- CU-01. No cierra la madre sola cuando las dos parciales calzan. Con las dos recepciones de 50.000 la madre sigue en su neto de 100.000 y en `APROBADO`. Cerrarla, si lo recibido ya iguala el neto, sigue siendo la rama de `solicitarCierreSaldoOc` que solo escribe `cerradaAt`.
- CU-03. No escribe `cerradaAt` al recepcionar el neto completo. La recepcion total deja la OC en `RECEPCIONADA` y no nace hija. Ni esa recepcion ni el registro de la factura escriben `cerradaAt`. Ese cierre sin hija solo ocurre si despues se llama `solicitarCierreSaldoOc` y lo recibido ya iguala el neto.
