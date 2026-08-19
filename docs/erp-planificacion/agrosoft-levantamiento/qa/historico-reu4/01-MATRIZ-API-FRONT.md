> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# Matriz conexión Front (modo real) → API local

Fecha: 2026-07-31  
Base: `http://127.0.0.1:5174/api/v1` → proxy → `http://localhost:3001`

## Barrido GET (paths usados por `erp_front/src/services/real/api.ts`)

Se extrajeron los path estáticos `http.get('...')` del cliente real y se consultaron autenticados (Bearer admin + `X-Empresa-Id`).

**Resultado: 0 faltantes / 0 errores 404-5xx en paths estáticos del cliente real.**

### Muestra Reu4 / core (todas HTTP 200 vía proxy)

| Método | Path | Notas |
|--------|------|--------|
| GET | `health` | `service=erp_back`, `db=ok` |
| GET | `auth/me` | sesión local |
| GET | `empresas` / `usuarios` / `roles` | admin |
| GET | `centros-costo` | R4-03 |
| GET | `indicadores-bc` | R4-13 |
| GET | `balance-8-columnas?periodo=2026-07` | R4-15 |
| GET | `libro-comercial` / `documentos` | R4-07/09 |
| GET | `ordenes-compra` / `registros-compra` / `recepciones-oc` | R4-05 |
| GET | `proformas-contratista` | R4-04 |
| POST | `auth/clave-reversa` | R4-04 (probado aparte) |
| GET | `cuentas-corrientes` | R4-17 rename UI |
| GET | `documentos-aging` | R4-19 |
| GET | `cartolas-bancarias` / `conciliaciones` / `pagos` | tesorería |
| GET | `dashboard/kpis` / `dashboard/notificaciones` / `dashboard/tendencia` | panel |

### Nota sobre “stubs”

`src/services/real/stub.ts` existe como legado; el modo real usa `src/services/real/api.ts` (HTTP Nest). En dev, sin preferencia, el toggle arranca en demo; hay que dejar **Modo real** para forzar API.

## Conclusión

Front local en MODO REAL está cableado al Nest local por proxy Vite. No hay indicios de llamadas a un host publicado en esta sesión.
