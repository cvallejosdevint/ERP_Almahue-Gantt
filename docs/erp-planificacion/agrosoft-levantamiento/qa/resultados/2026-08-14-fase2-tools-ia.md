# Fase 2 — Tools de IA vs estado del proyecto

**Fecha:** 2026-08-14  
**Fuente de verdad:** `qa/resultados/2026-08-14-fase1-as-is-to-be.md` (Reu6 vs código).  
**No se leyeron transcripciones.** Carlos/Sergio = hipótesis.  
**No se editaron** skills, rules, agents ni `AGENTS.md`; solo propuestas.

Leyenda: **Vigente** · **Obsoleto** · **Parcial** · **Falta**.

---

## 1. Resumen ejecutivo (actualizar ya)

Los tools de **aprobaciones** (PIN en reglas, grupos/escalas, `workflows-admin` legacy, AdminConcepto re-login) y el **split D11** (cotización Compras vs OV Ventas) están alineados con Fase 1. El riesgo es otro: un agente puede **cerrar mal un ticket** o **vender mal la demo** porque faltan huecos explícitos.

**Actualizar ahora (prioridad demo / no deshacer Reu6):**

1. **`almahue-comercial-inventario` + `erp-comercial.mdc` + `almahue-architecture`** — no dicen que el wizard **Emitir** aún puede crear cotización/NP/OC; que **`pantallas-permisos`** sigue catalogando Cotizaciones en Ventas y no lista OV; que **`ventaBajoCosto` no tiene UI**; que lookup **no tiene productor**; que **no restaurar NP** (Reu5 «cotiz→NP→factura» superada).
2. **`AGENTS.md` + `almahue-erp-contexto`** — no apuntan al as-is 14/08; no advierten **aprobación comercial reservada**; no mencionan tesorería/DTE stub ni prod vs migrate `stock_ov_ficha`.
3. **`almahue-qa-local` / runner / reviewer** — solo plan de **aprobaciones**; no tratan OV/stock ni deudas Fase 1 como «deuda conocida».
4. **`almahue-erp-contexto/reference.md`** — `02-PROPUESTA-APROBACIONES-ORGANIGRAMA.md` (jefeId) se lee como diseño vigente; la fuente de verdad es grupos/escalas (`03-DISENO-…`).

**No urgente:** `almahue-core`, `almahue-reuniones`, `erp-backend`, `erp-prisma`, `almahue-security`, `almahue-aprobaciones` (salvo una línea: Comercial sin cadena).

---

## 2. Tabla por path

| Path | Estado | Hallazgo | Propuesta |
|---|---|---|---|
| `AGENTS.md` | **Parcial** | Stack, Reu6, skills, PIN, re-login: vigentes. **Falta:** puntero Fase 1; D4 comercial sin aprobación; D16 sin UI; D20 migrate prod; tesorería/DTE; `pantallas-permisos` desfasado. | Bloque «Huecos vigentes (no mentir en demo)» + link al md Fase 1. Ver §3. |
| `.cursor/skills/almahue-aprobaciones/SKILL.md` | **Vigente** (+ falta menor) | Modelo grupos/escalas, PIN en reglas, AdminConcepto, `workflows-admin` legacy: coincide D4–D6/D5. **Falta:** D4 Comercial (OV/factura) **sin** cadena; no venderlo en demo. | Añadir viñeta D4 comercial reservado. |
| `.cursor/skills/almahue-aprobaciones/reference.md` | **Vigente** | Seed S1–S6, PIN 4821, `seed:aprobaciones-f2`. Fuera de alcance comercial. | Sin cambio obligatorio. |
| `.cursor/skills/almahue-comercial-inventario/SKILL.md` | **Parcial** | Tabla D11 y stock/flete/lookup: vigentes. **Falta:** productor `false`; Emitir mezcla tipos; `ventaBajoCosto` sin UI; FLETE no unificado en emitir/cotización; no NP; `pantallas-permisos`; redirect `/comercial/cotizaciones`. **Obsoleto implícito:** «No implementar DTE» está bien (diferido), pero no avisa el **stub** `billing/`. | Reescribir sección «Huecos / no mentir» (§3). |
| `.cursor/skills/almahue-deploy/SKILL.md` | **Vigente** (+ falta) | Host, no overwrite `.env`, smoke 401 grupos. **Falta:** D20 — no asumir prod con OV/stock hasta migrate `20260813230000_stock_ov_ficha`. | Una línea en Migraciones. |
| `.cursor/skills/almahue-deploy/reference.md` | **Vigente** | Sync tar/scp, health 4010. | Sin cambio. |
| `.cursor/skills/almahue-erp-contexto/SKILL.md` | **Parcial** | Reu6, tenant, AdminConcepto, D11: vigentes. **Falta:** tesorería existe (demo no); DTE stub; pantallas-permisos; comercial sin aprobación. | Ampliar «Documentos» + huecos. |
| `.cursor/skills/almahue-erp-contexto/reference.md` | **Obsoleto** (parcial) | Texto: `02-PROPUESTA-APROBACIONES-ORGANIGRAMA.md` \| «Fase 1 (jefeId)» — **no** es fuente de verdad post grupos/escalas. Rutas omiten `/compras/cotizaciones` vs menú y no advierten Emitir. | Marcar 02 como histórico; 03 + skill aprobaciones como vigente; rutas + advertencias. |
| `.cursor/skills/almahue-modulo/SKILL.md` | **Vigente** (+ falta) | Orden Nest/front, `StockInsumoBodega`. **Falta:** al añadir pantalla, actualizar catálogo de permisos (hoy desfasado vs Sidebar) y no meter cotización en Ventas. | Viñeta pantallas + D11. |
| `.cursor/skills/almahue-qa-local/SKILL.md` | **Parcial** | Plan aprobaciones: vigente. **Falta:** alcance OV/cotización/tesorería; cruzar deudas Fase 1; no clasificar «comercial sin PIN» como bug. | Ampliar alcance + deudas conocidas. |
| `.cursor/rules/almahue-core.mdc` | **Vigente** | ES, tenant, no transcripciones, migrations. | Sin cambio. |
| `.cursor/rules/almahue-reuniones.mdc` | **Vigente** | Carlos/Sergio hipótesis; Reu6>Reu5>Reu4. **Falta menor:** D11 «ambos documentos» ya en código (13/08); no reabrir cotiz→NP. | Una línea D11/NP. |
| `.cursor/rules/erp-backend.mdc` | **Vigente** | Orden Nest; no mezclar workflows-admin. | Sin cambio. |
| `.cursor/rules/erp-frontend.mdc` | **Parcial** | Orden front, API real. **Falta:** menú vs `pantallas-permisos`; Emitir no es solo factura/NC. | Viñetas D11 + Emitir. |
| `.cursor/rules/erp-prisma.mdc` | **Vigente** (+ falta) | migrations, `grupoId`. **Falta:** `StockInsumoBodega`, `Empresa.ventaBajoCosto`, dimensiones cuenta. | Viñeta inventario/comercial al tocar schema. |
| `.cursor/rules/erp-comercial.mdc` | **Parcial** | D11 correcto. **Falta / riesgo:** no prohíbe NP; no Emitir; no UI `ventaBajoCosto`; no productor. | Completar como §3. |
| `.cursor/agents/almahue-architecture.md` | **Parcial** | Legacy workflows + D11 menú: vigentes. **Falta:** flaggear Emitir mezclado; catálogo pantallas vs Sidebar; no tratar workflows-admin como «arreglar a grupos» en el mismo PR sin pedido. | Checklist extra §3. |
| `.cursor/agents/almahue-db.md` | **Vigente** (+ falta) | Aprobaciones fase 2. **Falta:** tablas/stock OV, ficha, `cuenta_dimensiones` cuando el diff es comercial/contable. | Ampliar punto 3 condicional. |
| `.cursor/agents/almahue-normalization.md` | **Vigente** (+ falta) | Compras/Contratistas strings; un grupo por módulo. **Falta:** no inventar módulo de aprobación Comercial; alinear nombres de pantalla (OV vs Cotizaciones Ventas). | Viñeta D4 + pantallas. |
| `.cursor/agents/almahue-patterns.md` | **Vigente** | DTO, guards, Query, ProtectedRoute. | Opcional: `pantallas-permisos` vs ruta. |
| `.cursor/agents/almahue-qa-reviewer.md` | **Parcial** | Deuda Jorge/S5: vigente. **Falta:** deudas Fase 1 (Emitir, pantallas, ventaBajoCosto, DTE, comercial sin cadena). | Lista «no clasificar como defecto nuevo». |
| `.cursor/agents/almahue-qa-runner.md` | **Parcial** | Plan aprobaciones. **Falta:** si el usuario pide Fase 4 comercial, no ejecutar solo E/S/OC; no pegar PIN en reportes (ya dice JWT/passwords). | Alcance: si piden comercial, usar Fase 1 como checklist. |
| `.cursor/agents/almahue-security.md` | **Vigente** | PIN no en rol; AdminConcepto vs `admin:*`; tenant. | Sin cambio. |

### Citas de texto obsoleto o peligroso (por omisión)

| Texto / omisión | Dónde | Por qué |
|---|---|---|
| «Fase 1 (jefeId)» como uso de `02-PROPUESTA-…` | `almahue-erp-contexto/reference.md` | Fuente de verdad = grupos/escalas (`03-DISENO`), no jefeId. |
| Skill comercial sin «no restaurar NP / cotiz→NP→factura» | `almahue-comercial-inventario` | Reu5 decía «hecho»; Fase 1: **contradicción resuelta** — cotización → OC, no NP. |
| QA/AGENTS sin «Comercial sin cadena» | varios | D4 **parcial** a propósito; demo no cubre facturas. |
| Skill comercial: lookup «sociedad, clientes, proveedores» sin productor | comercial | D7 **parcial**: `productor: false`. |
| D16 en skill como si fuera parametrizable | comercial | Existe en BD; **sin UI admin**. |
| Nada sobre wizard Emitir | comercial, architecture, erp-comercial | Fase 1: **alta** — Emitir no atado a factura/NC desde OV. |

---

## 3. Parches sugeridos (copiar; no aplicados)

### 3.1 `AGENTS.md` — añadir tras «Flujo post-cambio»

```markdown
## Huecos vigentes (Fase 1, 2026-08-14)

Fuente: `docs/erp-planificacion/agrosoft-levantamiento/qa/resultados/2026-08-14-fase1-as-is-to-be.md`.

- **D4:** cadena de aprobación solo Compras (OC) y Contratistas (proformas). Comercial (OV/factura) **no** tiene cadena; no venderlo en demo.
- **D11:** Compras › Cotizaciones → OC. Ventas › Orden de venta → stock → factura. No restaurar cotiz→NP→factura. Redirect `/comercial/cotizaciones`. Catálogo `pantallas-permisos` puede seguir listando Cotizaciones bajo Ventas (desfasado vs Sidebar).
- **D16:** `Empresa.ventaBajoCosto` en API; **sin pantalla** para cambiarlo (default BLOQUEAR).
- **D7:** lookup RUT sin maestro **productor**.
- **Emitir documento:** el wizard no está restringido a factura/NC de OV (puede mezclar tipos de compra).
- **DTE:** stub `billing/`; GoSocket diferido. Tesorería **existe** en código (cartolas, conciliación, pagos); demo cliente no cerrada.
- **Prod:** no asumir migrate `stock_ov_ficha` / OV en `45.7.229.46` hasta deploy explícito.
```

### 3.2 `.cursor/skills/almahue-comercial-inventario/SKILL.md` — reemplazar «No implementar» y añadir huecos

```markdown
## Huecos (no «ya está»)

- Lookup RUT: sociedad + clientes + proveedores. **Productor no** es maestro (`productor: false`).
- `ventaBajoCosto` (`BLOQUEAR` \| `PERMITIR_MERMA`) en `Empresa` + validación OV; **no hay UI** de parámetro.
- Wizard **Emitir** (`/comercial/emitir`) no está atado solo a factura/NC desde OV; no ampliar tipos de compra ahí.
- FLETE: en OV como `tipoLinea`; cotización/emitir pueden no ofrecerlo igual. Canonical DTE no auditado (recargo SII).
- Permisos de pantalla: alinear catálogo con menú (OV en Ventas; Cotizaciones **no** en Ventas).
- Guías de despacho: hay API; menú Ventas **sin** UI de despacho.

## No implementar / no restaurar

- Traspaso gastos próxima temporada (Reu6 diferido).
- DTE GoSocket real sin credenciales (existe stub `modules/billing/`).
- **No** restaurar cotización → nota de pedido → factura (Reu5). Cotización Compras convierte a **OC**.
```

### 3.3 `.cursor/rules/erp-comercial.mdc` — reemplazo del cuerpo

```markdown
# Comercial Almahue

- Cotización (`COTIZACION`) = Compras, receptor proveedor, convierte a **OC** (no NP, no factura).
- Orden de venta (`ORDEN_VENTA`) = Ventas, receptor cliente, stock al **confirmar**, factura copia qty/desc (precio editable).
- No reutilizar `CotizacionesPage` para OV. No cotización de cliente en menú Ventas.
- No usar wizard Emitir para cotización/NP/OC.
- `ventaBajoCosto` es param de empresa en BD, no checkbox de rol; no inventar UI salvo pedido.
- Lookup: no asumir productor hasta que exista maestro.
```

### 3.4 `.cursor/skills/almahue-erp-contexto/SKILL.md` — añadir a «Documentos (Reu6)»

```markdown
## Huecos de producto (no greenfield)

- Tesorería y contabilidad: módulos en código; demo cliente pendiente.
- DTE: stub billing; no emisión SII.
- Aprobación: no cubre OV/factura.
- Skill comercial: `almahue-comercial-inventario`. As-is: `qa/resultados/2026-08-14-fase1-as-is-to-be.md`.
```

### 3.5 `.cursor/skills/almahue-erp-contexto/reference.md` — filas a corregir

```markdown
| `03-DISENO-GRUPOS-Y-ESCALAS-APROBACION.md` | Fuente de verdad aprobaciones (grupos/escalas) |
| `02-PROPUESTA-APROBACIONES-ORGANIGRAMA.md` | **Histórico** (jefeId / fase anterior). No implementar desde aquí. |
| `qa/resultados/2026-08-14-fase1-as-is-to-be.md` | As-is/to-be vigente vs código |

Rutas: `/compras/cotizaciones`, `/comercial/ordenes-venta`, `/comercial/emitir` (Emitir = riesgo de mezcla; no es el flujo OV canónico).
```

### 3.6 `.cursor/agents/almahue-architecture.md` — añadir puntos 6–7

```markdown
6. Flaggea wizard Emitir si crea COTIZACION/NP/OC o mezcla Compras con Ventas.
7. Flaggea desfase menú Sidebar vs catálogo de pantallas/permisos (Cotizaciones en Ventas, OV ausente, Prospectos huérfanos).
8. No trates `workflows-admin` como fuente de verdad ni lo «migres» en el mismo cambio de grupos/escalas salvo pedido explícito.
```

### 3.7 `.cursor/skills/almahue-aprobaciones/SKILL.md` — una viñeta bajo Modelo

```markdown
- Módulos con cadena: **Compras** y **Contratistas** únicamente. Comercial (OV/factura) **sin** aprobación (D4 reservado). Super admin puede aprobar pendientes de esos módulos (D2), no implica cadena comercial.
```

### 3.8 `.cursor/skills/almahue-qa-local/SKILL.md` + reviewer — deudas conocidas

```markdown
## Deuda conocida (Fase 1) — no FAIL de producto en QA de aprobaciones

- Comercial sin cadena de aprobación (D4).
- Emitir documento mezcla tipos.
- `pantallas-permisos` vs Sidebar (Cotizaciones/OV).
- `ventaBajoCosto` sin UI.
- DTE stub; productor ausente; workflows-admin legacy aún en API/UI.
- Prod puede no tener migrate stock/OV.

Si el pedido es QA comercial/inventario, usar la tabla D11–D17 de Fase 1, no solo PLAN-PRUEBAS-APROBACIONES.
```

**Deploy (opcional, una línea):** en `almahue-deploy/SKILL.md` Migraciones: «OV/stock/ficha: verificar migrate `20260813230000_stock_ov_ficha` en prod antes de demo de ventas.»

---

## 4. Skills / rules / agents que no existen y convendría crear

No creados en esta fase. Nombre + description de 1 línea (frontmatter):

| Nombre sugerido | Tipo | description |
|---|---|---|
| `almahue-tesoreria` | skill | Cartolas, conciliación, pagos, estado de cuenta y aging; parsers banco Almahue. Use when working on tesorería, cartolas, conciliación or flujo de caja. |
| `almahue-billing-dte` | skill | Stub GoSocket/canonical DTE; no emitir SII real sin credenciales. Use when touching billing/, canonical-builder, o emisión DTE. |
| `almahue-pantallas-permisos` | skill | Catálogo de pantallas vs Sidebar y `modulo:read/write`; OV vs Cotizaciones. Use when editing pantallas-permisos, roles, or menu routes. |
| `almahue-contabilidad` | skill | Plan de cuentas, dimensiones CC/elemento/área, inactivar vs borrar, periodos. Use when working on cuentas, asientos, or centralización. |
| `almahue-ficha-contraparte` | skill | Ficha única cliente/proveedor (bancos, contactos, despacho); productor aún no maestro. Use when editing FichaContraparte or lookup-rut. |
| `erp-tesoreria` | rule (glob tesorería) | No inventar cobranza R4-18 ni SMTP; parsers en `tesoreria/parsers`. |
| `almahue-comercial-qa` | agent | Ejecuta checklist D11–D17 / Emitir / stock bodega; no el plan solo de aprobaciones. |

**No crear** skill de «workflows-admin»: el vigente es grupos/escalas; el agent architecture ya debe flaggear legacy.

---

## 5. Fuera de alcance de esta fase

- Aplicar parches (queda para cuando lo pidas).
- Fase 3 (qué no mostrar al cliente) y Fase 4–5 (tests).
- Leer transcripciones.
