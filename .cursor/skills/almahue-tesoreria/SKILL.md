---
name: almahue-tesoreria
description: Cartolas, conciliación, pagos, estado de cuenta y aging; parsers banco Almahue. Use when working on tesorería, cartolas, conciliación or flujo de caja.
---

# Tesorería Almahue

Módulo **existe**. Contrato ciclo: `docs/erp-planificacion/agrosoft-levantamiento/plan-tesoreria-ciclo-completo-2026-08-21.md`. Tesorería **no crea** la deuda; solo la liquida.

## Cerrado 21/08 (ciclo)

- Asiento banco = movimiento de cartola (`origen CARTOLA:{id}`). Periodo ABIERTO.
- Pago/cobro = calce + CC + aging. **No** asiento `PAGO:{id}` (ni con cartola ni sin ella).
- Al contabilizar compra/venta: CC + aging (neto+IVA).
- Gate: no pagar OC no operable; no cobrar factura no `CONTABILIZADA`.
- Cartola: solo import con líneas; `usuarioCarga` = email de sesión.
- `updatePago`: no edita calce/monto/contraparte.
- Conciliación: resumen de cartolas (R4-19). No alta huérfana.
- Pagos unificados: `PAGO_TOTAL` | `ANTICIPO` | `ANTICIPO_PRODUCTOR` (flag `esProductor` + TC). `/tesoreria/anticipos` redirige.
- Nómina: `semanaCompromiso` (aplazar no muta DTE). R4-17 vencimiento queda en aging.
- Flujo caja: banco + CLP/USD + apertura inmutable.
- Menú: cartola → conciliación → flujo → pagos → nómina → estado de cuenta.

## No inventar / diferido

- **Cobranza R4-18** (compromisos, mail, tracking).
- **SMTP** / H9.
- Match automático cartola↔factura (RUT+monto): calce **manual** 1:1.
- Parsers Chile/Estado/Santander sin muestra MJ (**H13**). Queda Almahue-web + CSV/Excel genérico.
- Maestro Productor. Códigos financieros Agrosoft (R4-25).
- DTE real / SII live.

Rule: `erp-tesoreria`. Integridad UI↔Prisma: `docs/auditoria-integridad-secundaria.md`.
