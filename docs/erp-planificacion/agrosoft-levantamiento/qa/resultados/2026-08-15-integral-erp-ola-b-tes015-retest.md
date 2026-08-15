# Retest TES-015 — Ola B integral

**Fecha:** 2026-08-15  
**Entorno:** local  
**Ejecutor:** almahue-qa-runner  
**API:** `http://localhost:3001/api/v1`  
**Front:** no requerido (caso API)  
**Fix bajo prueba:** `parseEstadoGenerico` en `tesoreria.service.ts`  
**Contexto:** FAIL previo en Ola B (`POST /pagos` → 500 con `estado: PENDIENTE`)

No incluir JWT ni passwords.

## Precondiciones

| Pieza | Resultado |
|---|---|
| `GET /health` | **200** — `status: ok`, `db: ok` |
| API `erp_back` | `npm run start:dev` en watch; reinicio automático ~18:47 (código compilado) |
| Actor | `admin@almahue.local` — permisos `*` (`tesoreria:write` implícito) |

## Conteo

| PASS | FAIL | BLOCKED | Total |
|---|---|---|---|
| 3 | 0 | 0 | 3 |

## Casos

| ID | Resultado | Evidencia |
|---|---|---|
| E1 | PASS | `GET /health` → 200, `db: ok` |
| TES-015 | **PASS** | `POST /pagos` body `{fecha:"2026-08-15", beneficiario:"Proveedor QA TES-015", medio:"TRANSFERENCIA", estado:"PENDIENTE", monto:150000}` → **201** — respuesta incluye `id`, `estado:"PENDIENTE"`, `monto:150000` |
| TES-015-B | **PASS** | `POST /pagos` mismo payload con `estado:"CONFIRMADO"` → **400** `Bad Request` — mensaje: `estado inválido: CONFIRMADO. Valores permitidos: ACTIVO, INACTIVO, PENDIENTE, BORRADOR` (no 500) |

## Comparación con Ola B

| Aspecto | Ola B (antes) | Retest |
|---|---|---|
| `estado: PENDIENTE` | **500** Internal Server Error | **201** Created |
| `estado: CONFIRMADO` | no probado | **400** Bad Request (validación explícita) |

## Defectos vs deuda

| ID | Clasificación | Nota |
|---|---|---|
| TES-015 | **cerrado** | Defecto P1 resuelto — `parseEstadoGenerico` acepta `PENDIENTE` y rechaza estados fuera del set con 400 |

## Retest sugerido

- Incorporar **TES-015** al script `run-ola-b-integral.mjs` con payload mínimo y variante `CONFIRMADO` → 400.
- Tras merge: retest **E2E-005** (showcase centralización + tesorería) según plan §9.

## Resumen para revisor

- **Veredicto retest:** **PASS** — único FAIL P1 de Ola B (`TES-015`) cerrado.
- **FAIL abiertos:** 0
- **BLOCKED:** 0
- Gate Ola B: pendiente addendum revisor tras reconciliar JSON/script.
