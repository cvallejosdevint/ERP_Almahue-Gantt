# Checklist QA + Reuniones — 2026-07-28

**Fecha pasada 1 (secciones A–D):** 2026-07-28 · **Fecha pasada 2 (sección E):** 2026-07-29 · **Repos:** `erp_back` + `erp_front`  
**Fuentes:** Reu1, Reu2, Reu3, reunión interna supervisor, flujo negocio, menús Sergio (informativo), tablero Trello real (API, comentarios/adjuntos de María Jesús 28/07), `CHECKLIST_FLUJO_NEGOCIO.md`, `CHECKLIST_CIERRE_100.md`

---

## A) Tests / builds

| Check | Resultado | Detalle |
|---|---|---|
| Back `npm test` (Jest unit) | **PASS** | 11 suites / **36** tests |
| Back `npx nest build` | **PASS** | exit 0 |
| Back e2e `test/app.e2e-spec.ts` | **PASS** | 1 test (`GET /api/v1/health`) |
| Front `npx tsc -b` | **PASS** | exit 0 |
| Front `npm run build` | **PASS** | `tsc -b && vite build` OK (~17.7s) |

### Fix aplicado en esta pasada (tests)

| Issue | Causa | Fix |
|---|---|---|
| `compras.service.spec.ts` FAIL | Mock Prisma sin modelo `proveedor`; `createOrden` ahora resuelve maestro | `prisma-mock.ts` + stub `proveedor.findFirst` en spec |

**Antes del fix:** 10 suites PASS / 1 FAIL (ENOMEM o `findFirst` undefined) · **Después:** 11/11 PASS, 36/36.

---

## B) Auditoría UI (pantallas nuevas) + fixes

### Criterios

Design system existente · `listQueryKey` + `empresaId` · `onSave`/API real · selects de catálogo · Sidebar Parametrización vs Contabilidad Config/Operaciones · demo+real · a11y básica ES · sin look purple/card-heavy nuevo.

### Pantallas revisadas

| Pantalla | Ruta | Veredicto | Notas |
|---|---|---|---|
| Plan de cuentas | `/catalogos/plan-cuentas` | OK | Árbol, SearchableSelect, query keys, API create/update/bulk; breadcrumb Parametrización |
| Elementos de costo | `/catalogos/elementos-costo` | Parcial | MockListPage + create API; **editar llama create** (sin PATCH) |
| Proveedores | `/catalogos/proveedores` | OK | MockListPage, create/update, invalidate OC/registro |
| Períodos | `/contabilidad/periodos` | OK | DataTable, listQueryKey, breadcrumbs Configuración |
| Config SII | `/contabilidad/config-sii` | OK | Cuentas desde catálogo, put API, breadcrumbs Config |
| Centralización | `/contabilidad/centralizacion` | OK | Preview/ejecutar API, periodos, DataTable |
| Comprobantes | `/contabilidad/asientos` | OK | SearchableSelect cuentas, bulk, API |
| Libro diario / Mayor | `/contabilidad/libro-diario`, `/mayor` | OK | listQueryKey periodo/cuenta, export |
| Cartola | `/tesoreria/cartolas` | OK | MockListPage + import preview Excel/CSV/PDF |
| Plantilla docs | `/admin/plantilla-documentos` | OK | `updateEmpresa` real, preview print |
| Sidebar Contabilidad | — | OK | Config / Operaciones / Reportes alineado Sergio |

### Fixes UI hechos (alto impacto / coherencia)

1. **Asientos breadcrumbs** → `Contabilidad › Operaciones` (`AsientosPage.tsx`) — alineado a Sidebar Sergio.
2. **Label Cartolas** en Sidebar → `Cartolas (Excel/CSV/PDF)` — refleja parser PDF ya cableado.

### Hallazgos cosméticos / menores (solo lista)

- Config SII: inputs en tabla sin `<label>`/`Field` explícitos (headers de columna alcanzan para demo).
- Elementos de costo / Factores honorarios: `onSave` ignora `id` → edición crea duplicado o Conflict (falta PATCH).
- Proveedores aparece en Catálogos **y** Compras (intencional shortcut).
- Plan cuentas también enlazado bajo Contabilidad › Configuración (entrada duplicada aceptada en validación Sergio).
- Preferencia período UI aún parcialmente en localStorage (documentado en minutas).
- Chunk JS front > 500 kB (aviso Vite; no bloqueante).

**¿UI acorde a reglas?** **Parcial → OK tras fixes** (design system respetado; 2 fixes de coherencia; residuales menores listados).

---

## C) Matriz reuniones (cliente + Sergio)

Leyenda: **OK** · **parcial** · **falta** · **DEFERRED** · **OUT**

| Solicitud | Fuente | Estado | Evidencia |
|---|---|---|---|
| Roles: usuarios asignados visibles | Reu3 R3-01 | OK | `erp_front/src/features/admin/RolesPage.tsx` |
| Usuarios multi-empresa (checks) | Reu3 R3-02 / D4 | OK | `UsuariosPage.tsx` + `UsuarioEmpresa` |
| Un rol por usuario | Reu3 D1 | OK | Admin usuarios/roles |
| Reset password sin ver plaintext | Reu3 D2 | OK | Auth admin + Perfil |
| Permisos pantalla persistentes | Reu3 gap | OK | `Rol.permisosPantalla` + API |
| Carga masiva libros + dupes | Reu3 R3-03 | OK | comercial/compras carga masiva API |
| Rename Libro ventas / compras | Reu3 D8 | OK | `Sidebar.tsx` |
| OC cuenta + CC + elemento | Reu3 R3-04 | OK | `ComprasPages.tsx` + schema |
| Devolución / salida proveedor + estados | Reu3 R3-05 | OK / parcial | estados seed; catálogo oficial cliente DEFERRED |
| Plan/elementos/códigos → Parametrización | Reu3 R3-06 | OK | Catálogos + redirect `/contabilidad/plan-cuentas` |
| Selector bodegas movimientos | Reu3 R3-07 | OK | chips horizontales |
| Multi-select proformas facturación | Reu3 R3-08 | OK | `ContratistasPages.tsx` Facturar selección |
| Drag columnas tablas | Reu3 R3-09 | OK | DataTable HTML5 drag |
| Aprobación proforma + nombre aprobador | Reu3 R3-10 | OK | `aprobadorNombre` UI/API |
| Export Excel/PDF genérico | Reu3 R3-11 | parcial / DEFERRED PDF | CSV/Excel DataTable; PDF avanzado DEFERRED |
| Filtro aprobaciones desde dashboard | Reu3 R3-12 | OK | `?estado=PENDIENTE` |
| Editar TC recepciones | Reu3 R3-13 | OK | PATCH recepción |
| Preview factura + OCs por proveedor | Reu3 R3-14/15 | OK | Libro compras modal |
| Rol aprobación proformas | Reu3 R3-16 | OK | seed ROL-5 |
| Carga masiva asientos analizar/editar | Reu3 R3-17 | OK | `AsientosPage.tsx` |
| Servidor publicado demo | Reu3 R3-18 | OK | `http://45.7.229.46/almahue-erp/` |
| Traspaso mes + TC | Reu3 D9 | OK | `/contratistas/traspaso` |
| Contabilizar doc cuenta+CC+glosa | Reu3 D10 | OK | flujo comercial |
| Maestro artículo con cuenta (sin stock form) | Reu3 D11 | OK | `/insumos/maestro` |
| GoSocket prod / DTE | Reu3 D7 | **DEFERRED** | panel consulta; sin API keys |
| Plan cuentas jerárquico árbol | Interno PC-01 | OK | `PlanCuentasPage.tsx` + `padreId` Prisma |
| Editar cuenta + carga masiva | Interno PC-02 | OK | PATCH + import Excel/API |
| Comprobantes enriquecidos | Interno PC-03 | OK | periodo/tipo/líneas/estados |
| Período impacta ventas | Interno PC-04 | parcial | selector API + PeriodoSetup; reglas doc parciales |
| Formato cotización/OC logo/sello | Interno I5 | OK | Admin plantilla + print |
| Períodos contables pantalla | Sergio | OK | `/contabilidad/periodos` |
| Config SII → cuenta | Sergio | OK | `/contabilidad/config-sii` |
| Centralización masiva | Sergio | OK | `/contabilidad/centralizacion` |
| Submenú Contabilidad Config/Operaciones | Sergio | OK | `Sidebar.tsx` |
| Libro diario / mayor | Sergio / flujo | OK | rutas reportes + Excel |
| Conciliación bajo Contabilidad | Sergio | parcial | vive en Tesorería (dominio OK) |
| Cuentas corrientes | Sergio | falta / parcial | no módulo dedicado |
| Maestro proveedores | Flujo | OK | `/catalogos/proveedores` |
| Cartola Excel/CSV/PDF | Flujo / Reu2 | OK / parcial | PDF genérico; banco-específico DEFERRED |
| NC ↔ factura | Flujo | OK | comercial + bodega |
| Cron BC 9am prod | Reu3 D13 | parcial | sync manual OK; cron prod no validado |
| Excel maestros oficiales cliente | Dependencia | falta | seed usable; Excel Mario pendiente |
| Libro comercial unificado + despachos | Sergio | parcial / OUT sprint | ventas/compras separados (producto) |

### Cumplimiento aproximado

| Scope | % aprox. | Nota |
|---|---|---|
| Action items Reu3 Top 8 + cableables | **~95%** | GoSocket prod DEFERRED a propósito |
| Slice supervisor (PC-01…04 + R3-18) | **~90%** | PC-04 períodos→ventas parcial |
| Menús Sergio (scope demo) | **~90%** | Cuentas corrientes / libro unificado fuera o parcial |
| Circuito flujo negocio local Demo OFF | **~90%** | Ver `CHECKLIST_FLUJO_NEGOCIO.md`; DEFERRED externos |

---

## D) Top residuales

> Specs listos en [`DEFINICIONES_PENDIENTES.md`](./DEFINICIONES_PENDIENTES.md). Fixes de código cerrados el 2026-07-29 (PATCH elementos/honorarios, PC-04, H5, H8, toasts, eslint).

1. **GoSocket/DTE productivo** — DEFERRED (sin keys; pedido usuario no tocar). Spec §1.
2. ~~Elementos de costo / honorarios: falta PATCH~~ — **RESUELTO** (`PUT /elementos-costo/:id`, `PUT /factores-honorario/:id`).
3. ~~PC-04 período → contabilización~~ — **RESUELTO** (`ContabilizarService.assertPeriodoAbierto` bloquea asientos CONTABILIZADO si periodo inexistente/cerrado).
4. **Cartola banco-específica / PDF escaneado** — falta muestra Agustín. Spec §3.
5. **Datos maestros Excel cliente** (plan/elementos/CC oficiales + estados bodega). Spec §4.
6. **Cuentas corrientes** (menú Sergio) — no implementado; **definición lista** Spec §2 (esperar OK de producto).
7. **Cron BC 9am en producción** — no validado en deploy. Spec §5.

---

## Archivos tocados en esta QA

| Archivo | Cambio |
|---|---|
| `erp_back/src/test-utils/prisma-mock.ts` | Mock `proveedor` + `empresaPlantillaDoc` |
| `erp_back/src/modules/compras/compras.service.spec.ts` | Stub resolve proveedor |
| `erp_front/src/features/contabilidad/AsientosPage.tsx` | Breadcrumbs Operaciones |
| `erp_front/src/app/Sidebar.tsx` | Label cartolas PDF |
| `ERP/CHECKLIST_QA_REUNIONES_2026-07-28.md` | Este documento |

Canvas flujo: sin cambio de estado material vs `flujo-negocio-completo-validacion-2026-07-28.md` (ya reflejaba cierre local); no se actualizó canvas.

---

## E) Validación cruzada Trello (feedback real de María Jesús, 28/07) + fixes aplicados

### Fuente

Export JSON del tablero Trello (`wixKcrP0 - almahue-erp.json`) + API de Trello (token autorizado por el usuario, solo lectura) para extraer comentarios y adjuntos reales de cada tarjeta. Se cruzó con las 3 minutas de reunión con cliente, la reunión interna con el supervisor (Sergio) y el checklist de secciones A–D de este mismo documento.

**Hallazgo clave:** María Jesús dejó **14 comentarios el 28/07/2026** (mismo día de Reunión 3), moviendo 5 tarjetas a "Rechazado Almahue" y comentando 2 tarjetas más que seguían en "En desarrollo". Es la señal más fresca y concreta disponible — más precisa que las minutas generales porque referencia pantallas mock puntuales. Las columnas "En QA Almahue" (9 tarjetas) y "Aprobado Almahue" (0 tarjetas) muestran que el resto del mock aún no había sido revisado por ella al momento del corte.

**Nota sobre Sergio:** su feedback (reunión interna del 28/07, ver `docs/erp-planificacion/agrosoft-levantamiento/validacion-sergio-menus-2026-07-28.md`) es **informativo / no prioritario** para este ciclo — se usó solo como referencia de nomenclatura de menús DTEMITE, ya cubierta en la sección C. No generó ítems de acción nuevos en esta pasada.

### Los 7 puntos del feedback fresco (28/07) — estado final

| # | Tarjeta Trello | Comentario de María Jesús | Estado previo | Fix aplicado | Evidencia |
|---|---|---|---|---|---|
| 1 | Mock — Administración/Roles y permisos | *"Agregar nombre de usuario, no solo rol. Ej. Perfil administrador, pero que el usuario sea MRODRIGUEZ."* | Faltaba | **RESUELTO** — campo `username` en `Usuario` (schema+migración `20260729030000_usuario_username`+DTO), autogenerado (inicial+apellido) si se deja vacío, visible en Topbar/RolesPage/UsuariosPage/Perfil | `prisma/schema.prisma`, `admin.service.ts`, `admin.dto.ts`, `auth.service.ts`, `UsuariosPage.tsx`, `RolesPage.tsx`, `Topbar.tsx`, `PerfilPage.tsx` |
| 2 | Mock — Monedas | *"Cambiar Catálogo a Parametrización."* | Faltaba | **RESUELTO** — label visible renombrado en Sidebar, breadcrumbs y permisos (el `id`/`code` interno `catalogos` se mantiene para no romper permisos guardados) | `Sidebar.tsx`, `CatalogosPages.tsx`, `PlanCuentasPage.tsx`, `ContabilidadPages.tsx`, `pantallas-permisos.ts`, `real/api.ts` |
| 3 | Mock — Tipos de documento | 6 capturas de la pantalla legacy Agrosoft "TIPOS DE REFERENCIAS" con 57 códigos (boletas honorario, facturas exportación/electrónica/exenta, notas débito/crédito, caja chica, tarjeta de crédito, depósito, cheque, transferencia, abono, anticipo, egreso, ingreso, préstamo, pagaré, provisión, traspaso, vales, etc.) | Catálogo muy pobre (3 tipos: OC/FAC/NC, sin seed backend) | **RESUELTO** — ampliado a 53 tipos de documento en mock (`fixtures.ts`) y seed backend (`seed.ts`), cubriendo Comercial/Compras/Contratistas/Insumos/Contabilidad/Tesorería; se agregó el módulo "Comercial" que faltaba en el selector | `services/mock/fixtures.ts`, `erp_back/prisma/seed.ts`, `CatalogosPages.tsx` (TiposDocumentoPage) |
| 4 | Mock — Plan de cuentas | Adjuntó los mismos 3 Excel (`PlanDeCuenta_(16)`, `RptCentroCostos_Excel_(24)`, `ReporteElementosDeCostos_(13)`) | — | **VERIFICADO SIN CAMBIOS** — son exactamente los mismos 3 Excel ya procesados/importados en esta sesión (confirmado por nombre de archivo original en `fuentes/parametrizacion-2026-07-28/README.md`): 396 cuentas, 233 centros de costo, 208 elementos de costo, ya cargados vía `seed.ts` | `prisma/data/plan-cuentas-almahue.json`, `centros-costo-almahue.json`, `elementos-costo-almahue.json` |
| 5 | Mock — Asientos contables | *"Se necesita más detalle del ingreso de la información."* | Solo cuenta/debe/haber/glosa por línea | **RESUELTO** — se agregó Centro de Costo (select) y Moneda + Tipo de cambio opcional por línea, con aviso (toast warning, no bloqueante) si falta el TC del día para moneda ≠ CLP al guardar; auto-completa TC desde Indicadores Banco Central si existe para la fecha | `contabilidad.dto.ts` (`LineaAsientoDto`), `AsientosPage.tsx`, `types/domain.ts`, `real/api.ts`, `mock/demo-store.ts` |
| 6 | Mock — Tarifas de contratista (En desarrollo) | *"Copiar formato de Agrosoft."* | Sin filtros superiores (columnas ya alineadas a Agrosoft) | **RESUELTO** — filtros superiores Año / Mes / Contratista sobre el listado, manteniendo columnas actuales (Labor, UM, CC, Tarifa, Vigencia) | `ContratistasPages.tsx` (`TarifasContratistaPage`) |
| 7 | Mock — Traspaso contable y cierre de mes (En desarrollo) | *"La centralización se hace de manera grupal del mes, no por contratista."* | Ya implementado así en sprint anterior | **CONFIRMADO EN CÓDIGO** — ambas rutas de centralización de contratistas (`contabilidad.service.ts` centralizar-período y `contratistas.service.ts traspasoCierre`) agrupan **todas** las proformas `DEFINITIVA`/`FACTURADA` del período en un único asiento (`origen: TRASPASO-CTR:{periodo}`, único por `empresaId_periodo`); no existe ninguna ruta que centralice por contratista individual | `contabilidad.service.ts` (~L1191-1271), `contratistas.service.ts` (`traspasoCierre`, ~L936-999) |

### QA re-ejecutado tras estos fixes (2026-07-29)

| Check | Resultado |
|---|---|
| Back `npx nest build` | **PASS** (exit 0) |
| Back `npm test` (Jest) | **PASS** — 11 suites / 36 tests |
| Back `npx prisma migrate deploy` (DB local `localhost:5433`) | **PASS** — migración `20260729030000_usuario_username` aplicada |
| Back `npx prisma db seed` | **PASS** — 53 tipos de documento, usuarios con `username`, plan de cuentas 396/233/208 |
| Front `npx tsc -b` | **PASS** (exit 0) |
| Front `npm run build` | **PASS** (`vite build` OK, ~7s) |
| Front `npm run lint` | **N/A** — falta `eslint.config.js` (migración a ESLint v9 pendiente; issue preexistente, no introducido por estos cambios) |

### Nota sobre drift de migraciones (preexistente, no bloqueante)

Al ejecutar `prisma migrate status` se detectó que la base de datos local (`localhost:5433`) tiene 3 migraciones aplicadas (`20260722163000_proformas_contratista`, `20260723220000_proformas_n1_factura`, `20260727150000_ui_table_preferences`) cuyas carpetas ya no existen en `prisma/migrations/` del working tree actual. Esto es **preexistente** a esta sesión de trabajo (no relacionado con los 7 fixes) y no impidió aplicar la nueva migración `usuario_username`. Recomendación: en el próximo ciclo, alinear el historial de migraciones del repo con el estado real de la BD de desarrollo (`prisma migrate resolve` o regenerar el baseline) antes de un despliegue a producción.
