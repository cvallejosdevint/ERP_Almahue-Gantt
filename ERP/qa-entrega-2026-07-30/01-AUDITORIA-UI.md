# Auditoría UI — pantallas (subagente UX)

**Fecha:** 2026-07-30  
**Fuente:** rutas `App.tsx` + `features/**` vs reglas de `00-PROMPT-MAESTRO.md`

## Bloqueantes / altos pre-entrega

| ID | Severidad | Hallazgo |
|---|---|---|
| UI-01 | BLOQUEANTE | Cerrar período contable **sin confirmación** |
| UI-02 | ALTA | `EmitirDocumentoPage` huérfana (no en rutas) |
| UI-03 | ALTA | Anular asiento solo vía combo estado, sin confirmación dedicada |
| UI-04 | ALTA | Libro compras: solo Ver (sin editar/anular) |
| UI-05 | ALTA | Sin “Anular OC” post-aprobación |
| UI-06 | ALTA | Flujo de caja: solo Crear |

## Transversales

- G1: `window.confirm` en varias pantallas (vs Modal de marca)
- G2: muchos maestros sin baja/desactivar en fila
- G3: `ProtectedRoute` too broad (permisos cruzados)
- G4: rutas duplicadas (`/insumos/catalogo`, `/tesoreria/aging`)
- G5: páginas huérfanas (Presupuestos, Reporte ejecutivo, Workflow, EmitirDocumento)

## Lista priorizada (15)

Ver respuesta del subagente UX en sesión; top 6 = UI-01…UI-06 arriba.

Detalle completo: chat agente UI (tabla por ruta).
