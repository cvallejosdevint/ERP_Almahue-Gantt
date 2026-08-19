---
name: almahue-tesoreria
description: Cartolas, conciliación, pagos, estado de cuenta y aging; parsers banco Almahue. Use when working on tesorería, cartolas, conciliación or flujo de caja.
---

# Tesorería Almahue

Módulo **existe** en código (pagos, cartolas, conciliación, estado de cuenta, anticipos, aging, flujo de caja). Demo cliente **no** cerrada (Reu6 «siguiente reunión»).

## Hechos (Fase 1)

- Parsers en `erp_back` `modules/tesoreria/parsers` (p. ej. Almahue web); carga Excel **base**, formato banco fino pendiente de MJ.
- Códigos de flujo de caja: UI hay; códigos Agrosoft no auditados (R4-25 parcial).
- Estado de cuenta / aging ≠ cobranza.

## No inventar / diferido

- **Cobranza R4-18** (compromisos, mail, tracking): no hay; propuesta, no feature.
- **SMTP**: correo al cambiar PIN / reenvío mail diferido (infra).
- DTE real y emisión SII: no es tesorería; ver skill `almahue-billing-dte`.
- Productor no es maestro (lookup comercial).

Rule: `erp-tesoreria`. Integridad UI↔Prisma: `docs/auditoria-integridad-secundaria.md`. El as-is 14/08 está `{deprecado}`.
