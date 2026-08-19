---
name: almahue-contabilidad
description: Plan de cuentas, dimensiones CC/elemento/área, inactivar vs borrar, periodos. Use when working on cuentas, asientos, or centralización.
---

# Contabilidad Almahue

Módulo **existe** (asientos, periodos, centralización, plan de cuentas, balance 8 columnas). Demo cliente y «oficial SII» **no** cerrados.

## Hechos Reu6 (D9–D10)

- Dimensiones CC / elemento / área por cuenta (N:N + flags). Excel MJ = fuente de carga, no inventar Excel.
- No eliminar cuenta con movimiento: DELETE → 409; inactivar; rename usa maestro en diario/mayor.
- Wipe `replace` bloqueado si hay asientos.

## Diferido / no mezclar

- Contabilidad electrónica SII (Reu4 D13): config SII de cuentas; no certificación.
- DTE: HTTP a `billing-gateway` (skill `almahue-billing-dte`). Fail-closed si el partner rechaza: no asiento. Stub inline solo para demo. No SII live.
- Tesorería (cartolas, conciliación) es otro módulo; cobranza R4-18 y SMTP diferidos.
- Productor no es maestro de contraparte.

Integridad UI↔Prisma: `docs/auditoria-integridad-secundaria.md`. El as-is 14/08 está `{deprecado}`.
