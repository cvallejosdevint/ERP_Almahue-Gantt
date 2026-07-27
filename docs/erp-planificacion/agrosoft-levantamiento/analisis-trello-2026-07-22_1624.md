# Análisis tablero Trello — backup 22/07/2026 16:24

**Respaldo:** `backups/trello-wixKcrP0-2026-07-22_1624.json`  
**Tablero:** [Almahue ERP](https://trello.com/b/wixKcrP0/almahue-erp)  
**Cards abiertas:** 36 · **Total (incl. archivadas):** 69

---

## Estado general post-ajustes manuales

| Área | Estado |
|---|---|
| Mocks Gantt F1 (#1–#26) | Restaurados con capturas `docs/trello-capturas-erp-mock/` |
| 9 tarjetas nuevas Reunión 1 | En **En desarrollo**, etiquetas MockUp + Solicitudes reunión 1 + Fuera Gantt F1 |
| Tarjeta índice | **Reunión 1 - Registro demo (22/07/2026)** en En QA Almahue |
| Video reunión | Eliminado de cards (uso interno Devint) |

---

## Tarjetas nuevas — capturas (post-corrección)

| # | Tarjeta | Captura(s) | Fuente |
|---|---|---|---|
| 60 | Tarifas de contratista | `03-tarifas-contratista.png` | legacy demo |
| 61 | Proformas y facturas | `16-proformas-contratista.png` | **captura ERP mock** (nueva) |
| 62 | Traspaso / cierre mes | `17-traspaso-cierre-contratistas.png` | **captura ERP mock** (nueva) |
| 63 | OC servicios | `06-orden-compra.png`, `07-distribucion-cc.png` | legacy |
| 64 | Recepción OC | `09-recepcion-oc.png` | legacy |
| 65 | Registro compra | `10-registro-compra.png` | legacy |
| 66 | Bodegas | `12-bodegas.png` | legacy |
| 67 | Movimientos / NC | `13-nc-devolucion.png` | legacy |
| 68 | Indicadores BC | `15-indicadores-bc.png` | legacy |

**Acción aplicada:** Proformas y Traspaso no tenían PNG legacy de la demo Agrosoft; se generaron desde `erp_front` (modo demo, `:5174`) y se subieron a Trello.

---

## Backend vs front (ERP)

| Tarjeta | Back `erp_back` | Front `erp_front` |
|---|---|---|
| Tarifas (C-03) | **REAL** — Prisma + API | **REAL** — CRUD con `onSave` |
| Proformas (C-06) | ❌ | Mock UI `/contratistas/proformas` |
| Traspaso (C-07) | ❌ | Mock UI `/contratistas/traspaso` |
| OC (P-01) | ❌ | Mock `/compras/ordenes` |
| Recepción (P-07) | ❌ | Mock `/compras/recepciones` |
| Registro (P-08) | ❌ | Mock `/compras/registro` |
| Bodegas (I-01) | ❌ | Mock `/insumos/bodegas` |
| Movimientos (I-04/I-05) | ❌ | Mock `/insumos/movimientos` |
| Indicadores BC (K-05) | ❌ | Mock `/contabilidad/indicadores-bc` |

---

## Orden de implementación recomendado

1. **Sprint A — Contratistas:** C-06 Proformas → C-07 Traspaso/cierre  
2. **Sprint B — Compras:** P-01 OC → P-06 Aprobación → P-07 Recepción → P-08 Registro  
3. **Sprint C — Insumos:** P-02 Maestro (prerrequisito) → I-01 Bodegas → I-03 Param → I-04/I-05 Movimientos  
4. **Sprint D — Contabilidad transversal:** K-05 Indicadores BC (en paralelo con B, consumido por recepción)

Detalle técnico: **`implementacion-tarjetas-nuevas-reunion1.md`**

---

## Scripts útiles

| Script | Uso |
|---|---|
| `analizar-backup-trello.py` | Adjuntos faltantes por card |
| `adjuntar-capturas-nuevas-trello.py` | Subir PNG legacy a Trello |
| `trello-qa-screenshots/capture-tarjetas-nuevas-erp.mjs` | Regenerar capturas desde erp_front |
