# Contrato — eliminar módulo Cotizaciones (21/08/2026, tarde)

**PM.** Complementa `plan-aprobaciones-solo-compras-2026-08-21.md`.  
La cotización del proveedor **no es un documento del ERP**: es un dato de referencia en la OC (tipo, folio, fecha). **Eliminar, no ocultar.**

Sidebar actual **ya no lista** Cotizaciones (solo redirect de URL vieja). Aun así el módulo vive: `convertirCotizacionAOc`, tipo `COTIZACION` en `DocumentoComercial`, filtro en Libro ventas, plantilla preview, fixtures.

## Lo que viene / lo que va

| | Se va | Se queda |
|---|---|---|
| Menú / rutas | Página de listado/alta de cotizaciones. Atajo «convertir a OC». | Redirect `/compras/cotizaciones` y `/comercial/cotizaciones` → `/compras/ordenes` (bookmarks). |
| Flujo | Cotiz persistida → aprobar cotiz → generar OC | OC wizard: referencia opcional. Cadena PIN solo OC. |
| API | `convertirCotizacionAOc`; crear/editar `tipo=COTIZACION`; convertir COTIZACION→OC | `DocumentoComercial` para OV, FACTURA, NC, ND, GUIA. Enum PG `COTIZACION` **no se dropea**. |
| Libro ventas | Filtro/opción «Cotización» (no es DTE de venta) | FACTURA / NC / ND / GUIA |
| Plantilla | Preview cuyo título es «Cotización» como doc de Compras | Preview con OC o FACTURA (misma plantilla de papel) |
| Referencia OC | — | `referenciaTipo` / `referenciaFolio` / `referenciaFecha` en wizard |

## Flujo objetivo

```
Proveedor envía PDF/correo (fuera del ERP)
  → Compras › Orden de compra (opcional: tipo COTIZACION + folio + fecha)
  → Borrador | Enviar a aprobación → PIN → APROBADO
  → Recepción / Libro (factura puede llegar antes; destacar si OC no aprobada)
```

## No hacer

- Adjuntar PDF.
- Restaurar cotiz→NP→factura.
- Borrar enum PostgreSQL `COTIZACION` (histórico).
- Quitar campos de referencia en la OC.
- Tesorería.
