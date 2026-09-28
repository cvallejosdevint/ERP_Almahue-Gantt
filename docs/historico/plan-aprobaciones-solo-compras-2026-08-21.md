# Contrato de flujo — aprobaciones solo Compras (21/08/2026)

**Para subagentes.** No es Reu7. Fuentes: minuta Carlos + transcripción 20/08 tarde. Auto-minuta tl;dv **no** cuenta.

Pisa a propósito Reu6 D4 (piloto OV) y Reu4 PIN de proforma: el cliente operativo pidió cadena **solo compras** (servicios y materiales) y Carlos pidió **eliminar, no ocultar**.

Tesorería (cartola, flujo de caja, pagos unificados, nómina) queda **fuera**.

---

## Lo que viene / lo que va

| Módulo | Se va | Se queda / se repara |
|---|---|---|
| **Ventas (OV)** | Cadena, bandeja `/comercial/aprobaciones`, grupos `Comercial`, flags `comercialRequiereAprobacion` / `comercialAprobacionDesde`, PIN de OV, estado intermedio `AUTORIZADA` ligado a la cadena, reserva de stock en el último OK de aprobación, pestaña Comercial en Admin › Aprobaciones, seed `GRP-COMERCIAL-*` | OV → confirmar (stock) → factura. Sin bandeja ni PIN. |
| **Contratistas (proforma)** | Solicitar/aprobar/rechazar con PIN, bandeja `/contratistas/aprobaciones`, grupos `Contratistas`, pestaña Admin, seed `GRP-CONTRATISTAS-*` | Labores → proforma `BORRADOR` → `DEFINITIVA` (write + lock) → asociar factura |
| **Compras (OC)** | Cotización como documento/módulo (menú, CRUD, convertir→OC) | Cadena grupos/PIN **solo Compras**. Wizard: borrador vs enviar a aprobación. Cotización = referencia opcional (tipo, folio, fecha; sin adjunto ni listado). Ver `plan-eliminar-modulo-cotizaciones-2026-08-21.md`. |
| **Libro compras** | Rechazar el alta si la OC no está recepcionada | Alta permitida con OC no aprobada (**destacar**). No contabilizar ni pagar hasta OC `APROBADO` (o posterior). Aceptación comercial a N días (Admin, default 8) + bitácora. No es auto-PIN de la OC. |

## Flujos objetivo

```
Compras:  [ref cotiz opcional] → OC (BORRADOR | PENDIENTE_APROBACION) → PIN cadena → APROBADO
           Factura recibida (puede llegar antes) → destacar si OC no APROBADO → no asiento / no pago
           A N días sin reclamo → aceptación automática (bitácora ERP; no SII live)

Ventas:   OV BORRADOR → confirmar (SALIDA_VENTA) → APROBADO → Emitir factura

CTR:      Proforma BORRADOR → DEFINITIVA → asociar factura
```

## No hacer

- Auto-aprobar la OC con el plazo de 8 días.
- Ocultar menús dejando código muerto de cadena OV/proforma.
- Inventar cadena nueva de contratistas.
- Adjuntar PDF de cotización.
- Tesorería de la misma reunión.
- GoSocket/SII en vivo (H11).
