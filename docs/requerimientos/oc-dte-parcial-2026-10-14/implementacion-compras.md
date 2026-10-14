# Implementacion compras: OC parcial madre/hija

Fecha: 2026-10-14. Paso de dominio en Compras. No toca el libro de compras, el vinculo de DTE, el sync de GoSocket, las proformas ni las guias de insumos. No hay migracion: se usa `ocPadreId` que ya estaba en el modelo.

## Funciones

| Funcion | Que hace ahora | CU |
|---|---|---|
| `createRecepcion` | Si la OC ya es hija, la recepcion sigue en esa hija. Si es madre y la recepcion confirmada cubre el neto de una sola vez (tolerancia 1 peso y cantidades que agotan el saldo, sin un trozo previo), no nace hija: la recepcion y el asiento quedan en esa OC y pasa a `RECEPCIONADA`. Si es madre y el trozo es menor, nace la hija aprobada y la recepcion se cuelga de la hija. Un borrador no nace hija. | CU-01, CU-02, CU-03, CU-04, CU-05, CU-06. Los topes de cantidad y monto se conservan (CU-07). |
| `updateRecepcion` (confirmar borrador) | El mismo corte que `createRecepcion`. Confirmar el total deja la OC `RECEPCIONADA`. Confirmar un trozo de la madre mueve la recepcion a la hija nueva y no cambia el estado de la madre. | CU-02, CU-03, CU-05, CU-06 |
| `crearOcHijaDeRecepcion` | Arma la hija: `ocPadreId` de la madre, `referenciaTipo = OC_PADRE`, `referenciaFolio` = numero de la madre, numero `madre.(hijas no anuladas + 1)`, estado `APROBADO`, neto del trozo, lineas digitadas con la cuenta y el centro de la linea madre. Sin bandeja, sin PIN, sin `allocateOcNumero`. | CU-01, CU-02, CU-04, CU-05, CU-06 |
| `saldoConfirmadoRecepcion` | Suma recepciones `CONFIRMADA` de la madre y de sus hijas no anuladas. En una hija, solo las de esa hija. Filtra por `empresaId`. | CU-02, CU-05, CU-08 |
| `assertTopeRecepcion` | Rechaza cantidad o monto por encima del saldo. Los borradores no entran en la suma. | CU-05, CU-07 |
| `recepcionEsTotalMadre` | Decide el camino sin hija (CU-03). Si ya hay un trozo confirmado, el resto sigue naciendo hija (`.2`). | CU-03, CU-01 |
| `lineasConCuentaDeMadre` | Copia cuenta y centro de costo de la linea de la madre. No usa `scaleLineasCompraToNeto`. | CU-04, CU-05 |
| `solicitarCierreSaldoOc` | Achica la madre al neto ya recepcionado (madre mas hijas) y la deja `PENDIENTE_APROBACION` con la cadena del monto nuevo. No crea hija por el faltante. Si lo recibido ya iguala el neto (tolerancia 1), solo marca `cerradaAt`. Sin recepcion confirmada, el cierre no abre. | CU-08, CU-03 (rama de cierre sin hija) |
| `scaleLineasCompraToNeto` | Sigue usandose solo para que las lineas de la madre cuadren con el neto achicado en el cierre. No prorratea un faltante ni arma una hija. | CU-08 |

El asiento de una parcial, si la cuenta tiene par Facturas por recibir, queda con origen `RECEPCION:{id de la hija}:{recepcionId}`. La madre no se contabiliza y no vuelve a `PENDIENTE_APROBACION` por nacer la hija.

## Pantalla

El boton del cierre decia que creaba una OC hija por el saldo. Ahora dice "Achicar y enviar a aprobación". El recibido del boton suma las recepciones confirmadas de la madre y de sus hijas. El cierre se puede pedir aunque ya existan hijas de trozos.

## Ejemplo

Madre de 100.000 con una recepcion confirmada de 50.000:

- La madre sigue en 100.000 y en `APROBADO`. No baja el neto, no pasa a recepcionada y no entra a la bandeja.
- Nace la hija `numero-de-la-madre.1`, `APROBADO`, neto 50.000, con el detalle digitado.
- La `RecepcionOc` confirmada y su asiento cuelgan de esa hija.
- El saldo de control es 50.000 (madre menos lo ya recepcionado en hijas).
