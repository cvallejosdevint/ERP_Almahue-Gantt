# Reunión interna supervisor ↔ Carlos — Replanificación post Reu 3

**Fecha:** martes 28/07/2026 ~15:36  
**Participantes:** Supervisor, Carlos  
**Demo cliente:** jueves 30/07/2026 (tarde)  
**Reunión follow-up:** miércoles 29/07 — revisar plan de cuentas / contabilidad  

| Fuente | Ubicación / estado |
|---|---|
| tl;dv | https://tldv.io/app/meetings/6a6905066efaa60013c8a251 — **temporalmente no disponible** (error app) |
| Video local | `e:\grabaciones\Screen Recording 2026-07-28 153620.mp4` (existe; no transcript automático en esta pasada) |
| Minuta Reu 3 cliente | [`reunion3-minuta-2026-07-28.md`](reunion3-minuta-2026-07-28.md) |
| Canvas backlog Reu 3 | `canvases/reunion3-backlog-2026-07-28.canvas.tsx` |
| Canvas sprint plan cuentas | `canvases/plan-cuentas-sprint-jueves.canvas.tsx` |
| Excel + UI ref (28/07) | [`fuentes/parametrizacion-2026-07-28/`](fuentes/parametrizacion-2026-07-28/README.md) — plan/elementos/centros + decisión código `X-X-XX-XX` |

---

## 1. Veredicto — cómo cambia el Top 8 de Reu 3

La Reu 3 priorizaba un slice admin + libros + OC + proformas + **mover** plan cuentas a Parametrización. Gran parte de ese Top 8 ya está marcado como hecho en código (roles, multi-empresa, libros/carga, move menú, OC cuenta/CC/elemento, proformas, filtro aprobaciones).

La reunión interna **pivota el foco restante hasta el jueves**:

| Antes (Top 8 Reu 3) | Ahora (hasta demo jueves) |
|---|---|
| Amplio: admin + libros + OC + proformas + move menú plan cuentas | **FOCO ÚNICO de producto demo:** plan de cuentas **jerárquico** (árbol) + edición + carga masiva real |
| Plan cuentas = relocación de menú (R3-06) | Plan cuentas = **modelo + API + UI árbol + seed Excel** |
| Comprobantes / asientos = post-jueves (R3-17) | Comprobantes suben a **slice jueves** (número, período, fecha, tipo, líneas con búsqueda cuenta, estados) |
| Cotizaciones/OC formato dinámico no estaba en Top 8 | Si cliente no entrega assets → Carlos **propone** formato (no bloquea demo core) |

**Implicancia:** el Top 8 Reu 3 deja de ser la cola de trabajo de Carlos esta semana. Lo ya cableado se **consolida con redeploy**; lo pendiente de Reu 3 que no sea plan cuentas/comprobantes/periodos **se aplaza**.

---

## 2. Decisiones (internas)

| # | Decisión | Implicancia |
|---|---|---|
| I1 | **FOCO** = plan de cuentas jerárquico: árbol tipo `1000 → 11/12 → 1101/1102/1201…`, código, categoría (activo/pasivo/patrimonio/ingreso), padre, editar + carga masiva | Schema + API + UI; seed desde Excel cliente |
| I2 | Timeline Carlos: **mar–mié back**, **mié front**, **jue testing**, **jue tarde demo** | Capacidad 100% en este slice |
| I3 | Comprobantes (asientos): número, período, fecha, tipo, líneas con búsqueda de cuenta; estados contabilizado / pendiente / anulado | Ampliar modelo/UI asientos; no solo toast carga masiva |
| I4 | Períodos contables afectan ventas/facturas | Hoy solo `localStorage`; hay que conectar a flujos documento |
| I5 | Cotizaciones/OC formato dinámico (logo, sello agua, columnas): si cliente no entrega antes del jueves → Carlos hace propuesta | No bloquea demo plan cuentas |
| I6 | Reunión miércoles: revisar plan cuentas / contabilidad con supervisor | Checkpoint mid-sprint |

---

## 3. Timeline día a día (mar → jue)

### Martes 28/07 (hoy, resto del día) — Backend
- Extender Prisma `CuentaContable`: `padreId`, nivel opcional; categoría = `tipo` existente.
- Migración + `PATCH/PUT` update cuenta; endpoint carga masiva (upsert por código).
- Seed/import script preparado para Excel (cuando llegue).
- Empezar campos faltantes en `Asiento` / comprobante: `periodo`, `tipo` (si aplica), estados alineados (pendiente ≈ borrador).

### Miércoles 29/07 — Backend cierre + Front
- **AM / early:** cerrar API árbol (list flat + children, o tree endpoint), validaciones padre/código.
- **Reunión supervisor:** alinear árbol y reglas (cuentas no imputables = nodos padre).
- **PM Front:** UI árbol expandible en `/catalogos/plan-cuentas` (breadcrumbs Parametrización); form con padre + categoría; edición real (no solo create); botón carga masiva wired.
- Comprobantes UI: cabecera (nº, período, fecha, tipo) + líneas N con búsqueda de cuenta; badges estados.

### Jueves 30/07 — Testing + Demo
- **AM:** testing integrado (crear árbol, editar, carga masiva, asiento con búsqueda cuenta, período en ventas si alcanza).
- Redeploy / smoke en servidor publicado (**R3-18** sigue bloqueante).
- **PM:** demo cliente — protagonistas: plan cuentas jerárquico + comprobantes; resto Top 8 como “ya entregado / consolidado” si redeploy OK.

### Post-jueves / próxima semana
- Ítems Reu 3 aplazados (bodega estados, drag columnas, export, preview factura, etc.).
- Formato cotización/OC (propuesta o assets cliente).

---

## 4. Qué SE APLAZA del Top 8 / backlog Reu 3 vs qué SIGUE

### Sigue en ventana jueves (nuevo núcleo)

| ID | Ítem | Notas |
|---|---|---|
| **PC-01** | Plan cuentas jerárquico (árbol, padre, categoría) | Reemplaza el alcance superficial de R3-06 |
| **PC-02** | Editar cuenta + carga masiva real | Gap actual: solo `POST` create; UI flat |
| **PC-03** | Comprobantes/asientos enriquecidos | Sube R3-17 + requisitos supervisor |
| **PC-04** | Período contable impacta ventas/facturas | Extiende selector localStorage → reglas |
| **R3-18** | Servidor publicado + redeploy | Sigue bloqueante demo |
| *(consolidación)* | Top 8 ya hecho en código | Mostrar en demo si deploy OK; no invertir más días |

### Se aplaza (explícito)

| Origen | Ítem | Motivo |
|---|---|---|
| R3-05 | Devolución + estados bodega | Bloqueado datos cliente + fuera de foco |
| R3-07 | Selector deslizable bodegas | Post |
| R3-09 | Drag columnas proformas | Post (reorder ←/→ alcanza) |
| R3-11 | Export Excel/PDF genérico | Espera feedback pantallas |
| R3-13–15 | TC recepciones, preview factura, OCs por RUT | Post |
| R3-16 polish | Rol aprobación (seed ya existe) | No más scope esta semana |
| Nuevo | Cotización/OC formato dinámico full | Solo propuesta si no hay assets |
| Top 8 residual | Pulido / edge cases admin-libros-OC-proformas | Solo bugs bloqueantes demo |

---

## 5. Dependencias

| Dependencia | Estado (28/07 tarde) | Bloquea |
|---|---|---|
| Excel plan de cuentas (cliente/supervisor: “hoy subieron”) | **No encontrado** en `docs/erp-planificacion`, repo Almahue ni Downloads recientes (últimos 14 días). **Dependencia abierta.** | Seed real / validación árbol vs negocio |
| Excel elementos de costo / CC | Mismo estado | Parametrización datos reales |
| Assets cotización/OC (logo, sello agua, columnas) | Pendiente cliente | Formato dinámico; si no llega → propuesta Carlos |
| Estados movimiento bodega | Pendiente (Reu 3) | R3-05 (aplazado) |
| Feedback Trello En Kua al Mawe | Pendiente | Cierre scope UI |
| Servidor publicado | Pendiente confirmación | Demo jueves |

**Acción:** pedir al supervisor el archivo Excel (ruta Drive/Trello/correo) o copiarlo a `docs/erp-planificacion/agrosoft-levantamiento/fuentes/`.

---

## 6. Riesgos

| Riesgo | Severidad | Mitigación |
|---|---|---|
| Excel no llega / no localizable | Alta | Árbol demo con seed sintético jerárquico (1000→11→1101…); marcar datos como ejemplo |
| Scope árbol + comprobantes + períodos en ~2 días | Alta | Miércoles checkpoint; períodos en ventas = slice mínimo o stub si no alcanza |
| tldv caído → matices perdidos | Media | Video local disponible; validar con supervisor miércoles |
| Edit cuenta en front llama solo create | Alta | Backend `PATCH` + front `onSave` con `editingId` |
| Período solo en localStorage | Media | Documentar límite en demo; cablear validación en emisión documentos si hay tiempo |
| Redeploy incompleto | Alta | Checklist smoke jueves AM antes de demo |

---

## 7. Snapshot técnico (gaps vs pedido supervisor)

Ver detalle en sección C del plan de implementación / canvas. Resumen:

| Capacidad pedida | Estado repo |
|---|---|
| Árbol padre→hijo | **Gap:** `CuentaContable` flat, sin `padreId` |
| Categoría activo/pasivo/… | **OK parcial:** enum `TipoCuentaContable` (+ GASTO) |
| Editar | **Gap API:** solo `POST /cuentas`; MockListPage edita en UI pero persiste como create |
| Carga masiva | **Gap:** no hay endpoint; asientos = toast |
| UI árbol en Parametrización | **Parcial:** ruta `/catalogos/plan-cuentas` OK; breadcrumbs aún “Contabilidad”; lista flat |
| Comprobantes (nº, período, tipo, N líneas, búsqueda) | **Parcial:** `Asiento` con numero/fecha/estado/lineas JSON; form 2 cuentas; sin período/tipo en modelo |
| Períodos → ventas/facturas | **Gap:** settings front only |

---

## 8. Plan de implementación (sin codear aún)

Ver sección D abajo y canvas `plan-cuentas-sprint-jueves.canvas.tsx`.

### D1 — Martes/miércoles (back) — archivos

1. `ERP/erp_back/prisma/schema.prisma` — `padreId`, relación self; opcional `nivel`; Asiento: `periodo`, `tipo`/`tipoComprobante`.
2. Migración Prisma nueva bajo `prisma/migrations/`.
3. `src/modules/contabilidad/dto/contabilidad.dto.ts` — padreId, bulk DTO, update DTO, campos comprobante.
4. `contabilidad.service.ts` / `contabilidad.controller.ts` — `PATCH cuentas/:id`, `POST cuentas/carga-masiva`, list ordenado / tree helper.
5. `contabilizar.service.ts` — período + estado pendiente; búsqueda cuenta en create.
6. `prisma/seed.ts` — árbol ejemplo o import Excel.
7. Script opcional `scripts/import-plan-cuentas.js` (o similar).

### D2 — Miércoles (front) — archivos

1. `src/types/domain.ts` — `padreId`, `hijos?`, campos asiento.
2. `src/services/real/api.ts` (+ mock/demo-store/api.ts) — update + bulk cuentas.
3. `src/features/contabilidad/ContabilidadPages.tsx` (`PlanCuentasPage`, `AsientosPage`) — árbol, breadcrumbs Parametrización, carga masiva, líneas dinámicas + search.
4. `src/App.tsx` / `Sidebar.tsx` — ya en catálogos; verificar copy.
5. `PeriodoContableSelector` / emisión comercial — validar período abierto al facturar (mínimo viable).

### D3 — Jueves

- Tests smoke manual + e2e puntual si existe harness.
- Deploy + demo script: crear cuenta hija → editar → carga masiva → comprobante con búsqueda → (si hay) bloquear venta fuera de período.

---

## 9. Entregables de esta pasada

| Entregable | Path |
|---|---|
| Esta minuta | `docs/erp-planificacion/agrosoft-levantamiento/reunion-interna-supervisor-2026-07-28.md` |
| Canvas sprint | `C:\Users\c\.cursor\projects\e-source-repos-Almahue\canvases\plan-cuentas-sprint-jueves.canvas.tsx` |
| Minuta Reu 3 (referencia) | `docs/erp-planificacion/agrosoft-levantamiento/reunion3-minuta-2026-07-28.md` |

**No se implementó código** en esta pasada (solo planificación).
