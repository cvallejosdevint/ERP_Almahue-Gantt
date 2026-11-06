# Auditoría UI front (2026-11-05)

Criterio: skill `almahue-diseno` + matriz `matriz-ui-normalizacion-2026-11-04.md` + reglas de sesión (click=detalle, «Editar datos», Activar/Desactivar, Eliminar admin+inactivo en parametrización).

## Error Vite (validado y corregido)

`[plugin:vite:oxc] Expected ',' or ')' but found 'export'` en `ERP/erp_front/src/services/real/api.ts`.

Causa: el script que insertó `delete*` cortó firmas de `update*` (p. ej. `updateCentroCosto`, `updateUnidad`, `updateAreaNegocio`, AF subfamilia/ubicación, etc.).

Estado: **reparado**. `tsc --noEmit` OK.

## Lote normalización visual (05/11 noche)

Aplicado sobre la deuda listada abajo (listado OC Compras sigue fuera de alcance por skill).

| Tema | Qué se hizo |
|---|---|
| «Editar» > «Editar datos» | OV, Compras (OC acciones), Ficha proveedores |
| Banners amber/sky/emerald | Reemplazados por `PageAviso` (C9: texto muted / danger + botón opcional) en Libro compras/ventas, Emitir, Plan cuentas, TC BC, Contratistas, GoSocket, Contabilizar, Borradores, Comex, Usuarios, Workflow, periodos, etc. |
| Export | `enableExport` en bandeja Aprobaciones OC. MockList ya trae `enableExport=true` por defecto (Empresas/Usuarios/tarifas/anticipos/AF no eran deuda real). |
| Tablas HTML densas | thead `text-xs font-medium uppercase tracking-wide`; códigos/folios `font-mono text-sm` en Asientos / Emitir / Comercial carga masiva / Compras detalle |
| Estado SII / borradores | Pastillas custom > `Badge` |

Componente nuevo: `ERP/erp_front/src/components/common/PageAviso.tsx`.

## Lote OC / fuera-de-alcance previo (05/11 noche+1)

Pedido explícito: normalizar lo que la skill dejaba fuera.

| Área | Cambio |
|---|---|
| Listado OC / insumos | Tipografía `text-sm`/`text-xs`; Imprimir `outline`; detalle footer «Editar datos»; alertas `Badge`; cobertura con accent (no amber) |
| Desglose C-4 | Tokens surface/border; sin slate/blue/emerald/amber |
| Wizard OC | Badge `!` sin `text-[10px]` custom |
| Notas de cobro | `PageAviso` danger; botones `danger` sin rose custom; tipografía lista |
| Emitir (HTML residual) | avisos muted; borrador con `PageAviso`; monospace `text-sm` |

Skill `almahue-diseno` actualizada: OC ya no queda fuera.

Residual menor: indicador `!` de parámetros faltantes del menú; colores de montos en Presupuestos; wizards densos siguen en HTML (tipografía alineada, no reescritos a DataTable).

## Conteo previo (73 archivos `*Page*` / `*Pages*`)

| Métrica | Antes | Después (features) |
|---|---:|---|
| Banner / `*-50` custom de ayuda | 21 | ~0 en pantallas de deuda (quedan `!` y progress en Compras) |
| Label «Editar» (no «Editar datos») | 3 | 0 |
| Lista MockList «sin export» | 8 | 0 (default MockList) |
| HTML tipografía suelta | 14 | alineada en densas tocadas; wizards intactos |

## Qué sí está normalizado

- Parametrización / catálogos MockList: viewFirst, «Editar datos», Activar/Desactivar, Eliminar (admin + desactivado).
- Plan de cuentas: detalle + Editar datos + deshabilitar; borrar solo admin/inactiva.
- FormGrid / densidad en MockList (lote 04/11).
- Tipografía listas (códigos mono, texto sm).
- Avisos C9 sin cajas de color en libros, Emitir, contratistas y modales de compra tocados.

## Lote layout ficha + historial (05/11)

Problema real en Contratistas (no el aviso muted): `formExtra` en **sidebar** dejaba la ficha a la izquierda y un recuadro blanco a la derecha (historial/aviso).

| Cambio | Detalle |
|---|---|
| `MockListPage` | `formExtraPlacement` default `below`; `detailFooterExtra` para Historial en footer del detalle |
| Contratistas | Historial de vigencia en modal propio (footer + Acciones); aviso RUT en `afterField` |
| Insumos | `formExtraPlacement="sidebar"` explicito (stock denso) |
| Skill | Historial fuera de ficha; sidebar solo si panel util |

## Deuda residual

1. Maestro insumos: sin Activar/Desactivar de catálogo (solo inventariable) - funcional, no solo visual.
2. Componentes compartidos (ApprovalChainVisual, timelines) con tintes de estado de cadena.
3. HTML de wizards densos: tipografía alineada; no convertidos a DataTable (flujo de documento).
4. Activo fijo: `ActivoFijoHistorialPanel` es serie de depreciacion (simulacion), no auditoria de cambios - distinto del caso contratista.

## Veredicto

Listado/detalle/wizard OC y Notas de cobro entran al mismo patrón visual. Parametrización + libros + OC quedan normalizados en código local. Wizards siguen en HTML denso a propósito.
