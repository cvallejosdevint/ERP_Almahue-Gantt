# Resultados QA

Los **informes de corrida** (`YYYY-MM-DD-*.md`, `*.json`) viven **solo en disco local** — no se versionan en git (ver `.gitignore`).

## Estado actual (referencia local, 2026-08-15)

| Oleada | Veredicto |
|---|---|
| A | `LISTO_OLA_B` |
| B | `LISTO_OLA_C` |
| C | `PIPELINE_LOCAL_CERRADO` |
| Prod | **No-Go** — E2E-008 / H14 pendiente |

Últimos informes generados en esta carpeta (local): `integral-erp-ola-*`, `revision-ola-*`, `veredicto-*`, `analisis-jefe-proyecto-implementacion.md`.

## Planes (sí en git)

- [`../PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`](../PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md)
- [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md)
- [`../PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md`](../PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md)

## Nuevas corridas

Usar [PLANTILLA.md](PLANTILLA.md). Sin JWT en markdown. Dumps con tokens: `*-raw.md` (gitignored).

Histórico Reu4: [`../historico-reu4/`](../historico-reu4/)
