> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md) + código. Motivo: levantamiento Reu1 pantalla a pantalla; no spec ERP actual.

# Módulo: Insumos y Bodega

Compras de **materiales / agroquímicos** viven aquí. Maestro de artículos unificado aquí (**DEC-07**), no duplicado con Compras.

## Pantalla: Maestro de artículos

- **Timestamp:** 30:20–34:00
- **Captura:** `../pantallas-legacy/11-maestro-articulos.png`
- **Etiqueta:** REQ

### As-Is
- Se puede crear el mismo artículo N veces (familia+subfamilia+descripción) sin alerta → stock fragmentado.
- Maestro aparece también en Compras.

### To-Be
- [REQ] Unicidad Familia + Subfamilia + Descripción.
- [REQ] Un solo maestro (Insumos); Compras solo consume servicios o referencia.
- [REQ] Familias/subfamilias administrables (integrado, no tarjeta separada inventada).
- [OPT] Ingredientes activos / UM relevantes para agrícola (mejora mencionada).

---

## Pantalla: Bodegas

- **Timestamp:** 01:08:04–01:10:17
- **Captura:** `../pantallas-legacy/12-bodegas.png`
- **Etiqueta:** REQ

### To-Be
- [REQ] Listar/crear bodegas solo de empresa activa.
- [REQ] Código único por empresa.

---

## Niveles de almacenamiento

- **Timestamp:** 01:10:29–01:11:32
- **Etiqueta:** OUT/PEND-03 — no se usan; validar con materiales antes de construir.

---

## Parametrización contabilización + movimientos complementarios

- **Timestamp:** 01:11:32–01:15:37
- **Etiqueta:** REQ

### To-Be
- [REQ] Por tipo de movimiento + familia/subfamilia → cuentas debe/haber.
- [REQ] Replicar **movimientos complementarios automáticos**.

---

## Movimientos de bodega

- **Timestamp:** 01:16:57–01:23:03
- **Etiqueta:** REQ

### Tipos
Entrada desde proveedor (parcial OK), cambio entre bodegas, devolución/NC.

### NC / devolución (crítico)
- **Captura:** `../pantallas-legacy/13-nc-devolucion.png` @ 01:20:20
- [REQ] Poder vincular NC a **factura específica** y sacar stock al **precio de esa factura**, no al promedio de bodega.
- **No** pedir FIFO/LIFO (no solicitado).

### Cierre
Traspaso contable + cierre de mes análogo a contratistas.
