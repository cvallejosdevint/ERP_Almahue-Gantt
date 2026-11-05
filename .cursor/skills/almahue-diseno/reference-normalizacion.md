# Referencia - normalizacion visual

Matriz viva: [`docs/requerimientos/matriz-ui-normalizacion-2026-11-04.md`](../../../docs/requerimientos/matriz-ui-normalizacion-2026-11-04.md).

## Referencias visuales

| Rol | Pantalla | Que imitar / evitar |
|---|---|---|
| Bueno | Plan de cuentas > modal Detalle y edicion de cuenta | Tabs, grilla 2-3 cols llena, seccion requisitos, badge codigo en titulo, footer hint + ghost + primary |
| Malo | Editar Ingreso (`MockListPage`, 3 cols) | Tercera columna vacia, huecos grandes, pocos campos en modal wide |

## Pedidos cliente (export y regularizacion)

- 22/10: PDF y Excel en **todos** los modulos (`transcripcion-2026-10-22-reunion-cliente.md` [27:42]-[27:48]).
- 28/10: "Todo siempre PDF y Excel" + regularizar en **todas las paginas** (`transcripcion-2026-10-28-reunion.md` [58:40], [02:46:11]-[02:46:18]).
- 03/11: filtros en barra; estados vs contabilizacion; modal de detalle propio (no zigzag); color de estado coherente.

## Checklist al normalizar una pantalla

1. Shell = `PageHeader` (export outline, primario al final).
2. Totales = `CollapsibleLibroSection` + fila `KpiStatCard`.
3. Lista = `DataTable` (filtros en `filterBarExtra`, chips en `toolbarExtra`).
4. Modal: si >= 5 campos visibles usar densificacion Plan de cuentas; si < 4, max 2 columnas.
5. Estados = `Badge`. Acciones = `RowActions`.
6. Sin banners sky/amber/emerald ni `className` emerald en `Button`.
7. Export PDF/Excel disponible en listados (pedido transversal).
8. Actualizar deuda en la matriz si el archivo cambio de categoria.
