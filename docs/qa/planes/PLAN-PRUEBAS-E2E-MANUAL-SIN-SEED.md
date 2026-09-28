# Plan E2E manual sin seed (solo superadmin)

**Objetivo:** Validar el ERP creando **toda** la parametrización desde la UI, sin `prisma seed` ni `seed:aprobaciones-f2`. Solo debe existir el superusuario inicial.

**Entorno:** API `http://localhost:3001/api/v1` · Front `http://localhost:5174`

## Preparación BD

```bash
cd ERP/erp_back && npm run reset:superadmin
```

1. Reset BD local (conservar solo empresa base + `admin@almahue.local` si el bootstrap lo deja).
2. **No** ejecutar `npm run seed` ni scripts de aprobaciones fase 2.
3. Login único inicial: `admin@almahue.local` / `Admin123!`

## Convención de casos

Cada entidad: **mínimo 2 registros** (A y B) para probar listados, filtros y reglas.

| Prefijo | Uso |
|---------|-----|
| `EMP-A`, `EMP-B` | Empresas |
| `ROL-A`, `ROL-B` | Roles |
| `USR-A`, `USR-B` | Usuarios |
| `PROV-A`, `PROV-B` | Proveedores |
| `CC-A`, `CC-B` | Centros de costo |
| `GRP-A`, `GRP-B` | Grupos aprobación |
| `OC-A`, `OC-B` | Órdenes de compra |

---

## Fase 1 — Administración base

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-1.1 | Crear empresa **EMP-A** y **EMP-B** | Listado con 2+ empresas |
| E2E-1.2 | Crear rol **ROL-A** con Compras→Aprobaciones R/W + Compras→Órdenes R/W | Guardado OK |
| E2E-1.3 | Crear rol **ROL-B** solo Contratistas (sin Compras Aprobaciones) | Guardado OK |
| E2E-1.4 | Crear **USR-A** (ROL-A) y **USR-B** (ROL-B), PIN `4821` cada uno | Login individual OK |
| E2E-1.5 | Asignar AdminConcepto Compras a USR-A (opcional) | JWT re-login muestra módulo |

## Fase 2 — Parametrización

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-2.1 | Monedas: CLP + USD (2 registros) | Catálogo visible |
| E2E-2.2 | Unidades: UN + KG | OK |
| E2E-2.3 | Centros de costo **CC-A**, **CC-B** | OK |
| E2E-2.4 | Tipos documento (2) | OK |
| E2E-2.5 | Plan de cuentas mínimo (≥2 cuentas gasto) | OC puede asociar cuenta |
| E2E-2.6 | Proveedores **PROV-A**, **PROV-B** | OK en catálogo y OC |

## Fase 3 — Reglas de aprobación Compras

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-3.1 | Grupo **GRP-A**: USR-A solicitante, aprobador inicial con ROL-A | OK |
| E2E-3.2 | Grupo **GRP-B**: segundo equipo | OK |
| E2E-3.3 | Escala GRP-A: tope $500k → escala a USR-A | OK |
| E2E-3.4 | Intentar asignar **USR-B** (sin Compras→Aprobaciones) como aprobador | **Modal** APROBADOR_SIN_BANDEJA + botón editar usuario (admin) |
| E2E-3.5 | Corregir rol USR-B, reintentar | Guardado OK |
| E2E-3.6 | Suplencia vigente (2 casos) | OK |
| E2E-3.7 | Simulador monto $200k y $2M | Cadena coherente |

## Fase 4 — Flujo OC

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-4.1 | USR-A crea **OC-A** $200k EMITIDO | Pendiente asignada |
| E2E-4.2 | Aprobador ve bandeja `/compras/aprobaciones` sin `compras:read` completo si está en cadena | 200 API + UI |
| E2E-4.3 | Aprobar con PIN | OC APROBADO |
| E2E-4.4 | **OC-B** rechazada y re-solicitud | Nueva bandeja PENDIENTE |
| E2E-4.5 | Usuario sin asignación no ve OC ajena | Lista filtrada |

## Fase 5 — Contratistas (si aplica)

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-5.1 | Contratistas **CTR-A**, **CTR-B** | OK |
| E2E-5.2 | Labores/tarifas (2 c/u) | OK |
| E2E-5.3 | Grupo + escala Contratistas | Validación bandeja análoga |
| E2E-5.4 | Proforma → solicitar aprobación → resolver | Flujo completo |

## Fase 6 — Import/export reglas

| ID | Acción | Esperado |
|----|--------|----------|
| E2E-6.1 | Export módulo Compras | JSON version 1 |
| E2E-6.2 | Import con aprobador inválido | Modal error |
| E2E-6.3 | Import válido en módulo sin pendientes | OK |

---

## Criterios de éxito global

- [ ] Ningún dato operativo vino del seed (excepto superadmin/bootstrap).
- [ ] Validación `APROBADOR_SIN_BANDEJA` bloquea configuración inválida.
- [ ] Aprobador designado accede a bandeja y resuelve sin `compras:read` global.
- [ ] Mínimo 2 casos por entidad documentados en informe.

## Informe

Resultados en `qa/resultados/YYYY-MM-DD-e2e-manual.md` (plantilla igual a `2026-08-12.md`).

**Ejecutor:** agente `almahue-qa-runner` con este plan + browser MCP.
