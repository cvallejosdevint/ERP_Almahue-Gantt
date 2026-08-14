# 08 — Datos limpios + creación OC desde front

Fecha: 2026-07-31

## Qué significaba la captura (`OC-2026-001`)

| Campo | Valor | ¿Correcto? |
|-------|-------|------------|
| Estado OC | `EMITIDO` | Sí — documento emitido esperando firma |
| Estado aprobación | `PENDIENTE` | Sí — bandeja del jefe |
| Jefe | vacío (`—`) | **No** — basura de seed/legacy |

`EMITIDO` + bandeja `PENDIENTE` **es el flujo normal**. El problema de esa fila era **sin jefe asignado**.

## Limpieza BD

Script: `erp_back/scripts/audit-and-reset-flujo-oc.ts`

Borrado (empresa Almahue): registros-compra, recepciones, aprobaciones-oc, ordenes-compra (13 OC viejas, incl. `OC-2026-001` y `OC-FIX30-001`).

## Set sembrado (coherente)

| Nº | OC | Bandeja | Jefe | Uso |
|----|----|---------|------|-----|
| `OC-QA-PEND-001` | EMITIDO | PENDIENTE | QA Aprobador | Aprobar/rechazar |
| `OC-QA-OK-002` | APROBADO | APROBADA | QA Aprobador | Recepción / libro |
| `OC-QA-RECH-003` | RECHAZADO | RECHAZADA | QA Aprobador | Editar/anular |
| `OC-QA-ANUL-004` | ANULADO | ANULADA | QA Aprobador | Caso cerrado post-fix |

## Test front (MODO REAL)

1. Login `qa.solicitante@almahue.local` / `QaTest123!`
2. Compras → Órdenes → **Nueva OC** → `OC-FRONT-001`
   - Proveedor Agro Insumos Sur, jefe **QA Aprobador**, ítem urea 25×$12.000, CC DAGGEN, neto $300.000
3. Resultado BD: `EMITIDO` + bandeja `PENDIENTE` + jefe QA Aprobador
4. Login `qa.aprobador@almahue.local` → bandeja pendientes: `OC-FRONT-001` + `OC-QA-PEND-001` con **Aprobar/Rechazar**

### Ajuste de producto

Alta nueva OC desde front ahora guarda `estado: EMITIDO` (antes `BORRADOR`) para entrar limpio a bandeja con jefe.

## Cómo repetir

```bash
cd ERP/erp_back
npx ts-node -r tsconfig-paths/register scripts/audit-and-reset-flujo-oc.ts
```
