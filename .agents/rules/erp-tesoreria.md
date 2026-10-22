---
description: No inventar cobranza R4-18 ni SMTP; parsers en tesoreria/parsers.
globs: ERP/erp_back/src/modules/tesoreria/**/*.ts,ERP/erp_front/src/features/tesoreria/**/*.{ts,tsx}
alwaysApply: false
---

# Tesorería Almahue

- Parsers de cartola en `tesoreria/parsers` (p. ej. Almahue web). No duplicar parsers en otros módulos.
- No inventar **cobranza R4-18** (compromisos, mail, tracking): solo estado de cuenta / aging.
- No inventar **SMTP** (reenvío mail, aviso PIN): diferido infra.
- Flujo de caja existe; no asumir códigos Agrosoft auditados.
- DTE / GoSocket no es tesorería. Productor no es maestro.
