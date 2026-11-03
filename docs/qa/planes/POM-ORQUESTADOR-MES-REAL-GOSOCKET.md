# POM orquestador: mes contable real (front + GoSocket)

Estado: **encargo activo** (nov 2026). Octubre 2026 en QA manual paralelo (otro agente).

## Problema que corrige

- Vinculos **FAC-CTR-*** manuales en proformas **no** son DTE GoSocket; el visor sin PDF no hace fidedigno octubre como mes cerrado interempresa.
- Scripts API-only (ene/feb DTE, cierres CTR+bodega) prueban backend pero **no** sustituyen el plan integral front + sync + PDF.

## Regla de fidelidad

| Evidencia valida | No cuenta como mes real |
|------------------|-------------------------|
| DTE `EMITIDO`/`PENDING` con `billingEmissionId` + GID GoSocket | Factura texto FAC-CTR en proforma |
| PDF compra/venta vía `GET .../dte/pdf` (gateway) | HTML fallback visor (solo demo) |
| Libro compras fila con `gosocket.globalDocumentId` | Registro manual sin sync |
| Playwright accion desde menu ERP (1536x960, pagina completa) | Solo POST API sin UI |

## Pre-requisitos entorno (checklist PM)

1. PostgreSQL local (`DATABASE_URL`, tipico `:5433`) **arriba**.
2. `billing-gateway` en `:3040`, `BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=false`.
3. Credenciales sandbox GoSocket en gateway (`GOSOCKET_API_USER_ALMAHUE_*`).
4. `Empresa.gosocketBillerId` + resolucion + acteco en **EXPORT** y **SERVICES**.
5. Migraciones Prisma aplicadas (incl. `SolicitudReversaEdicion` si aplica reversa cerrada).

## Arquitectura POM

```
ERP/.qa-tmp/pom/
  config.mjs           # URLs, empresas, periodo objetivo
  pages/               # Page objects por modulo
  flows/               # Secuencias de negocio (emitir, sync, contabilizar, cierre)
  orchestrator.mjs     # PM: fases, evidencias, gates
  evidence/            # capturas + json estado (gitignore ok)
```

Referencias: `PLAN-MES-CONTABLE-COMPLETO-INTEREMPRESA.md`, skill `almahue-billing-dte`, `almahue-qa-local`, `emit-ene-feb-interempresa.mjs` (solo emision, no mes completo).

## Fases PM (orden obligatorio)

1. **Gate entorno** - health API, gateway, una emision smoke 33 SERVICES > EXPORT.
2. **Maestros** - tenant EXPORT/SERVICES, periodo abierto oct-2026 (o mes piloto acordado).
3. **Comercial** - OV EXPORT, emitir 33/52 real, sync estado si PENDING.
4. **Compras receptor** - sync GoSocket, acuse, contabilizar, PDF visor OK.
5. **Contratistas** - ingreso, proforma, factura = registro **sync** (no FAC-CTR manual).
6. **Insumos** - movimiento, guias recibidas sync, cierre bodega.
7. **Tesoreria** - cartola import, calce (sin pagar solo por foto).
8. **Contabilidad** - libros, cierre periodo contable.
9. **Contratistas cierre** - traspaso + evidencia asiento.
10. **Informe** - matriz modulo/submodulo PASS/FAIL/SKIP + enlaces capturas.

## Criterio de cierre de fase

- PM no avanza si falta evidencia (`evidence/<fase>-*.png` + `state.json` con folio/GID/asiento).
- FAIL producto: issue en `docs/qa/resultados/` sin parchear codigo salvo bloqueo entorno (regla usuario oct QA).

## Subagente PM

Prompt fijo en `.qa-tmp/pom/PM-PROMPT.md`. Modelo recomendado: razonamiento alto + Playwright MCP (no viewport chico).
