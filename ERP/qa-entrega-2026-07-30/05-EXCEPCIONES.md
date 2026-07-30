# Excepciones / casos borde — entrega

**Fecha:** 2026-07-30  
**Fuente:** [Excepciones](65d0927b-084b-4728-993e-5d2de4d5b51e)

## Hallazgo transversal

Suite TC01–TC41 = **100% happy path**. Casi ninguna excepción tiene TC dedicado aunque el backend a veces sí la implementa.

## Top 10 EX (prioridad entrega)

| # | ID | Sev | Descripción |
|---|---|---|---|
| 1 | EX-05 | BLOQ | Traspaso contratistas re-ejecutable → asientos duplicados |
| 2 | EX-25 | BLOQ | Anular movimiento bodega CONFIRMADO no revierte stock/par |
| 3 | EX-28 | ALTO | Cartola nunca llega a CERRADA (sin endpoint + sin guard) |
| 4 | EX-29 | ALTO | Calce pago duplicado posible (texto libre) |
| 5 | EX-18 | ALTO | Proforma sin flujo RECHAZADA |
| 6 | EX-16 | ALTO | Convertir cotización implementado pero **no probado** E2E |
| 7 | EX-04 | MEDIO | Traspaso no pasa periodo correcto a `createAsiento` |
| 8 | EX-20 | MEDIO | N proformas → 1 factura no probado con N>1 |
| 9 | EX-08 | MEDIO | `clienteId` no validado contra empresa operativa |
| 10 | EX-35 | MEDIO | Sin soft lock concurrente |

## Ya OK (implementados; falta TC de excepción)

Periodo cerrado en asiento/doc/centralización (EX-01…03), rechazo OC + solo jefe (EX-10/11), anular/editar cotización FACTURADO (EX-13/15), NC origen (EX-22/23), doble contabilizar cartola (EX-27), usuario inactivo (EX-32), folio duplicado P2002 (EX-34).

## Smoke manual mínimo pre-entrega

1. Traspaso contratistas dos veces → no debe duplicar asiento (EX-05)  
2. Anular movimiento CONFIRMADO → stock coherente (EX-25)  
3. Convertir 1 cotización con líneas → NP/Factura (EX-16)  
4. Rechazar OC + intentar aprobar como no-jefe (EX-10/11)  
5. 2 proformas → 1 factura (EX-20)  
6. Reintento calzar mismo TRX dos veces (EX-29)
