> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# QA interactivo — Aprobaciones + permisos por rol

Fecha: 2026-07-31 · Stack: `127.0.0.1:5174` → proxy → Nest `:3001` · **MODO REAL**

## Usuarios creados (API admin)

| Usuario | Email | Pass | Rol | Permisos clave |
|---------|-------|------|-----|----------------|
| QA Aprobador | `qa.aprobador@almahue.local` | `QaTest123!` · PIN `4821` | ROL-9 QA Aprobador | `compras:write`, `compras:aprobar-all`, `contratistas:write`, `proformas:aprobar` · **aprobarConPin** |
| QA Solicitante | `qa.solicitante@almahue.local` | `QaTest123!` | ROL-10 QA Solicitante | `compras:write`, `contratistas:write` (**sin** aprobar) |
| QA Lectura | `qa.lectura@almahue.local` | `QaTest123!` | ROL-11 QA Solo lectura | solo `*:read` |
| Digitador (seed) | `jsanchez@almahue.cl` | `demo123` | ROL-3 | solo `contratistas:*` |

Workflows actualizados: Compras y Contratistas incluyen `U-16` (QA Aprobador) + `U-1`.

Credenciales también en `qa-users.json`.

---

## Módulos con cola de aprobación

| Módulo | Solicitar | Aprobar / Rechazar | Comercial |
|--------|-----------|--------------------|-----------|
| **Compras (OC)** | Crear/actualizar OC `EMITIDO` con `aprobadorId` | `PUT ordenes-compra/:id` `estado=APROBADO\|RECHAZADO` | — |
| **Contratistas (proformas)** | `POST …/solicitar-aprobacion` | `POST …/definitiva` / `…/rechazar` | — |
| **Comercial** | Sin cola | Sin cola | Solo regla “reservado” en Admin |

---

## Resultados API (flujos interactivos)

### Compras / OC — PASS

1. Solicitante crea `OC-QA-*` EMITIDO con proveedor maestro + `aprobadorId=U-16` → **201**
2. Solicitante intenta aprobar → **403** _“Solo el jefe aprobador asignado…”_
3. Lectura intenta aprobar → **403**
4. Aprobador ve bandeja `GET aprobaciones-oc` con la OC → **200**
5. Aprobador aprueba → estado **APROBADO**
6. Aprobador rechaza otra OC → **RECHAZADO**

### Contratistas / Proformas — PASS

1. Solicitante crea borrador → pide aprobación a U-16 → **PENDIENTE_APROBACION**
2. Solicitante / Digitador `POST …/definitiva` → **403** _supervisor de regla_
3. Aprobador aprueba → **DEFINITIVA** (`aprobadoPorId=U-16`)
4. Aprobador rechaza otra → **RECHAZADA**

### RBAC API — PASS

| Caso | Esperado | Resultado |
|------|----------|-----------|
| Lectura crea OC | 403 | 403 |
| Lectura admin/usuarios y roles | 403 | 403 |
| Lectura lista OC | 200 | 200 |
| Digitador lista OC | 403 | 403 |
| Solicitante admin/usuarios | 403 | 403 |

Detalle JSON: `02-RBAC-APROBACIONES-API.json`.

---

## Resultados UI (MODO REAL)

| Rol | Menú Administración | Proformas pendientes | OC Aprobaciones | Notas |
|-----|---------------------|----------------------|-----------------|-------|
| **QA Lectura** | Oculto | — | Ve botones Aprobar/Rechazar | API bloquea aprobación (OC queda EMITIDO). `/admin/usuarios` redirige a `/` |
| **QA Solicitante** | Oculto | **Sin** botones Aprobar | Puede operar compras/write | UI proformas respeta `canResolverProformaPendiente` |
| **QA Aprobador** | Oculto (sin `admin:read`) | **Con** Aprobar/Rechazar | Puede aprobar | Captura: `UI-aprobador-proformas.png` |
| **Digitador** | Oculto | Módulo contratistas OK | Ruta `/compras/*` **accesible en UI** | API `ordenes-compra` → **403** (menú/ruta demasiado permisivos) |

### Hallazgos UI (gaps)

1. **Bandeja OC** muestra Aprobar/Rechazar a quien tiene `compras:read`, sin filtrar si es el jefe; el **backend sí aplica** la regla.
2. **`App.tsx` ProtectedRoute** agrupa compras/catálogos/contab bajo `anyOf` que incluye `contratistas:read` → digitador ve pantallas de compras aunque la API deniegue datos.
3. El menú lateral **no oculta** Compras/Contabilidad/etc. por permiso de módulo (solo oculta Administración sin `admin:read`).
4. Proformas: la UI **sí** oculta Aprobar al solicitante (mejor que OC).

---

## Conclusión

- Flujos de **solicitud + aprobación/rechazo** en los dos módulos activos (OC y proformas) funcionan de punta a punta en local con usuarios QA.
- Los **permisos se aplican de verdad en API** (403 correctos).
- En UI: Administración y botones de proforma están bien; OC y menú global tienen **fugas visuales** (botones/rutas visibles) aunque la API sigue siendo la fuente de verdad.
