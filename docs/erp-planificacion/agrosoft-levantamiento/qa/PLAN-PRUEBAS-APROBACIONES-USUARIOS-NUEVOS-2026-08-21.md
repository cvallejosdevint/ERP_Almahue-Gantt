# Plan de pruebas — Aprobaciones Compras (usuarios nuevos + notificaciones)

**Fecha:** 2026-08-21  
**Ámbito:** local. Solo **Compras (OC)**.  
**Skills:** `almahue-qa-local`, `almahue-aprobaciones`.  
**Ejecutor / revisor:** `almahue-qa-runner` → `almahue-qa-reviewer`.  
**No es** el plan clásico S1–S6 (`seed:aprobaciones-f2`). No es el corte D11 de cotizaciones.

Complementa: `PLAN-PRUEBAS-APROBACIONES.md` (fase 2 seed) y `plan-eliminar-modulo-cotizaciones-2026-08-21.md`.

---

## Objetivo

Validar el ciclo operativo que el QA del 21/08 (sin módulo Cotizaciones) **no recorrió**:

1. Crear **usuarios nuevos** (no seed Luis/María/Laura).
2. Incluirlos en reglas Compras: miembros, aprobadores individuales (`SIMPLE`), nodos `AND` y `OR`.
3. Emitir OC con **referencia de cotización externa** (tipo/folio/fecha; sin PDF; sin menú Cotizaciones).
4. Aprobar, rechazar, reenviar; campana **in-app** al aprobador y al solicitante.
5. Huecos habituales: PIN malo, bandeja ajena, borrador vs enviar, auto-aprobación, override admin, tenant.

---

## No hacer

- Reset BD (`reset:superadmin`, `npm run seed`, `seed:qa-desde-cero`, `seed:aprobaciones-f2`, `migrate deploy` a ciegas). Tesorería de la misma instancia **no se toca**.
- Reabrir cadena OV ni PIN de proforma.
- SMTP / correo PIN (**SKIP H9**).
- Restaurar menú/CRUD Cotizaciones.
- Copiar JWT ni passwords al informe (salvo que el email de login sea evidencia de *quién* actuó).

---

## Entorno

| Pieza | Valor |
|---|---|
| Front | `http://localhost:5174` |
| API | `http://localhost:3001/api/v1` |
| Health | `GET /health` → `status: ok`, `db: ok` |
| Empresa | La activa en local (último QA: **EMP-EXPORT** / ALMAHUE EXPORT SPA). No mezclar OC con EMP-SERVICES. |
| Prefijo | Usuarios, roles y grupos: `QA-APR-2108-*` |
| Demo UI | **MODO REAL** (off) |
| PIN aprobadores | `4821` |
| Password operadores | `demo123` |
| Admin | `admin@almahue.local` / `Admin123!` — parametriza; **no** cierra cadenas salvo caso ADM |

Si health o front caen: arrancar Postgres `:5433`, Nest, Vite. No SKIP de UI por puertos sin intentar arranque.

---

## Matriz de usuarios (crear por Admin › Usuarios)

Password `demo123`. Aprobadores: PIN `4821`. Re-login de cada operador **después** de asignarlo a grupo/escala (`bandejaModulos` en JWT).

| Id | Nombre sugerido | Email | Rol en el ciclo | Pantallas / permisos |
|---|---|---|---|---|
| SOL | QA Solicitante | `qa.sol.apr2108@almahue.cl` | Solicita OC | Compras › Órdenes **write**. **Sin** bandeja Aprobaciones. |
| AP-S | QA Aprobador N1 | `qa.aps.apr2108@almahue.cl` | SIMPLE N1 tope **$500.000** | Compras › Aprobaciones + PIN |
| AP-N2 | QA Aprobador N2 | `qa.apn2.apr2108@almahue.cl` | SIMPLE N2 **sin tope** | Igual |
| AP-AND-1 | QA And Uno | `qa.and1.apr2108@almahue.cl` | Nodo AND | Igual |
| AP-AND-2 | QA And Dos | `qa.and2.apr2108@almahue.cl` | Nodo AND | Igual |
| AP-OR-1 | QA Or Uno | `qa.or1.apr2108@almahue.cl` | Nodo OR | Igual |
| AP-OR-2 | QA Or Dos | `qa.or2.apr2108@almahue.cl` | Nodo OR | Igual |
| SIN-BAN | QA Sin Bandeja | `qa.sinban.apr2108@almahue.cl` | Solo OC write, **sin** pantalla Aprobaciones | Para V1 |

Roles mínimos (crear si no existen, prefijo `QA-APR-2108`):

- **ROL-SOL:** Compras › Órdenes read/write; catálogos/proveedores read si el wizard lo exige.
- **ROL-AP:** igual + Compras › **Aprobaciones** (para que `validar-bandeja` no bloquee).

Admin **no** es miembro ni nodo de estos grupos.

---

## Grupos y escalas (Admin › Reglas de aprobación)

Módulo **solo Compras**. Simular **antes** de emitir cada familia de OC.

| Grupo | Miembros | Aprobador inicial | Escala |
|---|---|---|---|
| `GRP-QA-APR-SIMPLE` | SOL, AP-S (jefa: miembro + inicial) | AP-S | AP-S tope $500.000 `SIMPLE` → escala AP-N2 sin tope `SIMPLE` |
| `GRP-QA-APR-AND` | SOL-AND (usar SOL si un usuario = un grupo Compras; **si el unique lo impide**, crear `SOL-AND` con el mismo ROL-SOL: `qa.soland.apr2108@almahue.cl`) | AP-AND-1 | Nodo `AND` con AP-AND-1 + AP-AND-2 (ambos; sin tope o tope alto) |
| `GRP-QA-APR-OR` | `SOL-OR` `qa.solor.apr2108@almahue.cl` si hace falta | AP-OR-1 | Nodo `OR` con AP-OR-1 + AP-OR-2 |

**Restricción de producto:** un usuario = **un grupo por módulo**. No pongas a SOL en SIMPLE y AND a la vez. Crea solicitantes extra (`SOL-AND`, `SOL-OR`) si la UI lo exige.

Simulador (casos SETUP-SIM):

| ID | Solicitante | Monto | Esperado |
|---|---|---|---|
| SIM-S | SOL | 200.000 | Cadena AP-S |
| SIM-ESC | SOL | 800.000 | AP-S → AP-N2 |
| SIM-AUTO | AP-S (jefa solicita) | 200.000 | **No** auto-aprobación; escala a AP-N2 |
| SIM-AND | SOL-AND | 300.000 | Paso AND (AP-AND-1 y AP-AND-2) |
| SIM-OR | SOL-OR | 300.000 | Paso OR (AP-OR-1 o AP-OR-2) |

---

## Casos

### A. Entorno

| ID | Caso | Esperado |
|---|---|---|
| E1 | Health API + front | 200, `db=ok`; front 200 |
| E2 | Login admin | Sesión `*`; empresa EMP-EXPORT (o la activa) |
| E3 | `GET /grupos-aprobacion` sin token | **401** |

### B. Setup (usuarios + reglas)

| ID | Caso | Esperado |
|---|---|---|
| U1 | Crear roles + 7–9 usuarios | Login individual OK |
| U2 | Grupos/escalas SIMPLE, AND, OR | Guardado; Admin no figura |
| V1 | Poner SIN-BAN como aprobador en escala | Modal / API `APROBADOR_SIN_BANDEJA`; no guardar |
| SIM-* | Simulador Admin | Tabla de arriba |

### C. OC + cotización externa

Todas las OC de este plan: wizard con `referenciaTipo=COTIZACION`, folio `COT-QA-APR-2108-*`, fecha `2026-08-20`. Sin adjunto. Sin menú Cotizaciones.

| ID | Actor | Caso | Esperado |
|---|---|---|---|
| OC-BOR | SOL | Guardar **borrador** $200k + referencia | `BORRADOR`; **no** aparece en bandeja AP-S |
| OC-ENV | SOL | **Enviar a aprobación** $200k + referencia | `PENDIENTE_APROBACION`; correlativo `OC-AAAA-NNNN`; cadena AP-S |

### D. Aprobar / rechazar

| ID | Actor | Caso | Esperado |
|---|---|---|---|
| PIN-BAD | AP-S | PIN incorrecto sobre OC-ENV | No aprueba; OC sigue pendiente |
| APR-S | AP-S | PIN `4821` monto ≤ $500k | OC `APROBADO` |
| APR-ESC | SOL + AP-S + AP-N2 | OC $800k + referencia | Tras PIN N1 queda pendiente N2; segundo PIN → `APROBADO` |
| APR-AND | AP-AND-1 luego AP-AND-2 | Un solo PIN **no** cierra | Ambos → `APROBADO` |
| APR-OR | AP-OR-1 | Un PIN cierra el paso | AP-OR-2 **ya no** ve esa pendiente |
| RECH-N1 | AP-S | Rechaza OC nueva $200k | OC `RECHAZADO`; SOL ve motivo |
| RECH-AND | Un AND rechaza | Evidenciar comportamiento real | No debe quedar `APROBADO` con un solo rechazo |
| REA | SOL | Reenviar la OC de RECH-N1 | Nueva pendiente + campana al aprobador |
| ISO | AP-OR-1 (u otro) | Bandeja con OC de SIMPLE ajena | No ve la pendiente de AP-S |
| ADM | Admin | Override 1 OC pendiente (opcional) | Puede aprobar/rechazar sin estar en escala |
| AUTO | AP-S | Jefa emite OC $200k | Cadena salta auto-aprobación (va a AP-N2) |
| KPI | AP-S | Panel operativo | `ocPorAprobar` refleja **sus** pendientes |

### E. Notificaciones in-app (campana)

Login del destinatario. Topbar + `GET dashboard/notificaciones` (no pegar JWT). SMTP = **SKIP H9** (caso N-SMTP).

| ID | Evento | Aprobador | Solicitante |
|---|---|---|---|
| N-SOL | Tras OC-ENV | `OC_PENDIENTE` (título OC + pendiente) | **Medir:** ¿hay campana «enviada»? Si no, **FAIL/gap nuevo**, no H9 |
| N-APR | Tras APR-S (cierre) | Pendiente `oc-pend:*` marcada leída / desaparece | `OC_RESULTADO` aprobada |
| N-RECH | Tras RECH-N1 | Pendiente marcada leída | `OC_RESULTADO` rechazada |
| N-ESC | Tras PIN N1 en APR-ESC | Campana al **AP-N2** (`requiere tu aprobación` / escalada) | Sin cierre aún |
| N-AND | Tras enviar AND | Campana a **ambos** AND (medir; si solo uno, gap) | Igual que N-SOL |

---

## Criterios

- **PASS** si esperado se cumple y hay evidencia (folio OC, estado, usuario, tipo de notificación).
- **FAIL** si no, y no está en gaps conocidos (H9 SMTP, D4 OV, P0-1 asiento, recepción OC no mueve stock).
- **BLOCKED** si el entorno impide el caso (API/front caídos **después** de intentar arranque; unique de grupo que impida AND/OR — documentar workaround `SOL-AND` / `SOL-OR`).
- **SKIP H9** solo para correo SMTP.

Informe: `qa/resultados/2026-08-21-aprobaciones-usuarios-nuevos.md` (plantilla `resultados/PLANTILLA.md`). Sin JWT.

## Retest mínimo si el runner no alcanza todo

Prioridad: U1–U2, OC-ENV, APR-S, APR-AND, APR-OR, RECH-N1, N-SOL, N-APR. El resto no es SKIP por tiempo: es cobertura pendiente explícita en el informe.
