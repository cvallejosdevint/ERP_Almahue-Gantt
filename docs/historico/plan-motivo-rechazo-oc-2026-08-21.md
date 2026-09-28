# Contrato — motivo de rechazo en OC (21/08)

**PM.** Hoy **no existe** campo motivo al rechazar una OC. El modal de bandeja pide PIN y confirma; `OrdenCompra` / `AprobacionOc` no tienen `motivoRechazo`. La campana dice «Tu solicitud fue rechazada» sin texto. QA RECH-N1: «API sin campo motivo libre».

Incluirlo. Solo Compras. Tenant `empresaId`. No tesorería. No cadena OV.

## Lo que viene

| Dónde | Comportamiento |
|---|---|
| Bandeja rechazar | Textarea **obligatorio** «Motivo del rechazo» (mín. 5 caracteres, trim). PIN se mantiene. |
| Persistencia | `OrdenCompra.motivoRechazo` + copia en la fila `AprobacionOc` que rechazó (`motivoRechazo`). |
| Solicitante | Detalle OC (Órdenes) y timeline: estado Rechazado + motivo + quién rechazó. Campana `OC_RESULTADO` incluye el motivo en `detalle`. |
| Reenviar | Al volver a `PENDIENTE_APROBACION` / wizard, **limpiar** `motivoRechazo` (no arrastrar el anterior). |

## API

`UpsertOrdenCompraDto.motivoRechazo` opcional en general; **requerido** si `estado=RECHAZADO` (400 si falta o < 5). No aceptar rechazo sin motivo.

`mapOc` y `getAprobaciones` devuelven `motivoRechazo`.

Migración Prisma `prisma/migrations/` IF NOT EXISTS. No `migrate deploy` a ciegas. No dropear enums.

## Tests + QA

Jest: rechazo sin motivo → 400; con motivo → persiste y campana lo incluye; reenviar limpia.

QA (usuarios `QA-APR-2108`, EMP-EXPORT, no reset): AP-S rechaza OC de SOL con texto visible; SOL abre la OC y ve el motivo; campana lo muestra. Informe `qa/resultados/2026-08-21-motivo-rechazo-oc.md`.
