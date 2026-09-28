# Plan de pruebas — Aprobaciones fase 2

**Ámbito:** local (front + API). Prod solo smoke si se pide aparte.  
**Skills:** `almahue-qa-local`, `almahue-aprobaciones`.  
**Ejecutor / revisor:** subagentes `almahue-qa-runner` y `almahue-qa-reviewer`.

## Precondiciones

| Pieza | Valor |
|---|---|
| Front | `http://localhost:5174` |
| API | `http://localhost:3001/api/v1` |
| Health | `GET /health` → `status: ok`, `db: ok` |
| Datos | seed + `seed:aprobaciones-f2` |
| Sesión UI | `localStorage['erp.session']` |
| AdminConcepto | **re-login** antes de grupos |

Si health o seed fallan → todos los casos **BLOCKED**.

## Credenciales demo

| Usuario | Email | Password | Uso |
|---|---|---|---|
| Admin | `admin@almahue.local` | `Admin123!` | Simulador, admin total |
| Claudia | `cvargas@almahue.cl` | `demo123` | AdminConcepto Compras |
| Ricardo | `rmunoz@almahue.cl` | `demo123` | AdminConcepto Contratistas |
| Luis | `lherrera@almahue.cl` | `demo123` | Alta OC |
| Jorge | `jsanchez@almahue.cl` | `demo123` | Cadena / bandeja runtime + PIN |
| María | `mgonzalez@almahue.cl` | `demo123` | Bandeja con `compras:read` |
| PIN | — | `4821` | Pool aprobadores |

No copiar JWT a informes.

## A. Entorno

| ID | Caso | Esperado |
|---|---|---|
| E1 | Health API | 200, db ok |
| E2 | Login admin | token + `permisos: ["*"]` |
| E3 | `GET /grupos-aprobacion` sin token | **401** (no 404) |

## B. Simulador (admin, `/admin/aprobaciones`)

| ID | Solicitante | Monto | Grupo / módulo | Esperado |
|---|---|---|---|---|
| S1 | Luis Herrera | 200.000 | GRP-COMPRAS-1 | Jorge (suplente María) |
| S2 | Diego | 500.000 | GRP-COMPRAS-2 | Pablo Núñez |
| S3 | María | 100.000 | GRP-COMPRAS-1 | Jorge (sin auto-aprobación) |
| S4 | Bruno | 800.000 | GRP-COMPRAS-6 AND | Laura + co-aprobador |
| S5 | Luis | 3.000.000 | GRP-COMPRAS-1 | Jorge → Claudia |
| S6 | Diego | 400.000 | Contratistas | Pablo Núñez |

API: `POST /aprobaciones/simular` con Bearer admin.

## C. AdminConcepto

| ID | Actor | Caso | Esperado |
|---|---|---|---|
| AC1 | Claudia | Login + `/admin/aprobaciones` | UI reglas; sidebar sin Usuarios |
| AC2 | Claudia | `GET /grupos-aprobacion` | 200, 12 Compras, 0 Contratistas |
| AC3 | Claudia | `GET /usuarios` | 403 |
| AC4 | Ricardo | Grupos | 8 Contratistas, 0 Compras |
| AC5 | Claudia | Combo módulo | Solo Compras |

## D. Flujo OC (operativo)

| ID | Actor | Caso | Esperado | Nota |
|---|---|---|---|---|
| OC1 | Luis | Nueva OC y enviar | Entra a cadena | Validar Nº OC en form |
| OC2 | Jorge | `/compras/aprobaciones` | Ver pendiente asignada | 200 API; ruta `bandejaModulo` |
| OC3 | Jorge | Aprobar con PIN 4821 | Avanza | PUT sin `compras:write` global |
| V1 | Admin | Guardar escala con aprobador sin Compras→Aprobaciones | Modal `APROBADOR_SIN_BANDEJA` | API `validar-bandeja` + save |
| OC4 | María | Bandeja | Pendientes según reglas | |

## E. Regresión mínima

| ID | Caso | Esperado |
|---|---|---|
| R1 | Login María dashboard | Notificaciones sin 500 |
| R2 | Build front | `npx tsc -b` y `npx vite build` OK |

## Criterios

- **PASS** si esperado se cumple.
- **FAIL** si no, y no está en gaps.
- **BLOCKED** si entorno impide el caso.
- OC2 resuelto: bandeja runtime + `bandejaModulos` en sesión (re-login tras cambios de reglas).

Plantilla: [`resultados/PLANTILLA.md`](resultados/PLANTILLA.md).
