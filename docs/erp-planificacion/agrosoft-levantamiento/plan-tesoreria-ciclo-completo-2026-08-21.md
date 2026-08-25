# Contrato — tesorería ciclo completo (21/08)

Tesorería **no crea** la deuda. Solo la liquida. Si el documento de origen está mal (OC no aprobada, factura no contabilizada), el pago miente.

Fuentes: Reu4 (D14/D15, R4-16…R4-25) + Lupe/Mario 20/08 tarde. Reu6 no cerró demo de tesorería. **No** pisa Reu6. Carlos/Sergio en demo = hipótesis.

## Decisión F0 — asiento banco vs pago

| Hecho | Dónde vive |
|---|---|
| Asiento banco | Movimiento de cartola (`origen CARTOLA:{id}`). Periodo ABIERTO. |
| Pago / cobro | Calce operativo: `Pago` + cuenta corriente + aging. |
| Pago **con** cartola | 1:1 `movimientoCartolaId`. No segundo asiento. |
| Pago **sin** cartola | **Permitido** (se registra desde el libro antes de subir el Excel). Actualiza CC y aging. **No** crea asiento `PAGO:{id}`. El mayor se mueve cuando se calza la TRX y se contabiliza. |

No las dos cosas a la vez: nunca asiento de pago **y** asiento de la misma TRX.

## Gates (antes de tesorería)

- OC: asociar factura a OC no aprobada = destacar. Contabilizar o pagar = solo `APROBADO` / `RECEPCIONADA` / `CONTABILIZADA` / `FACTURADO`.
- OV: sin cadena. Confirmar stock → emitir. D16: no vender bajo `costoPromedio`.
- Libro ventas: registrar cobro solo si factura `CONTABILIZADA`.
- Recepción OC no mueve stock. Productor ≠ maestro (`esProductor`).
- Aceptación 8 días = bitácora comercial; no aprueba OC ni habilita pago.

## Qué es cada pantalla

| Pantalla | Rol |
|---|---|
| Cartolas | Insumo de conciliación. Import **completa**. Contabilizar TRX = asiento banco. Calzar egreso/ingreso a pago/cobro. |
| Conciliación | Resumen R4-19 (pendientes / conciliados). No alta huérfana. No matching automático. |
| Flujo de caja | Saldo por banco y moneda (CLP/USD). Apertura inmutable. No catálogo Agrosoft (R4-25 diferido). |
| Pagos | Una vista: `PAGO_TOTAL` / `ANTICIPO` / `ANTICIPO_PRODUCTOR`. |
| Nómina | Aging `POR_PAGAR` por **semana de compromiso**. Aplazar no muta DTE/asiento. ≠ cobranza R4-18. R4-17 (editar vencimiento) vive en aging, rol tesorería. |
| Estado de cuenta | Kardex por tercero. Links por id, no heurística de texto. |

## Diferido (no reabrir)

Cobranza R4-18, SMTP/H9, algoritmo match RUT+monto (Sergio), parsers banco finos (H13), maestro Productor, códigos R4-25, DTE/SII live.
