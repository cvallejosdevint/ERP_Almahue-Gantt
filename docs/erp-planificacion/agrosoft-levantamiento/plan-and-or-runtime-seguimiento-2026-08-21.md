# Contrato — AND/OR runtime + seguimiento visual (21/08)

**PM.** Corrige FAILs del QA `2026-08-21-aprobaciones-usuarios-nuevos.md`. Solo Compras (OC). Tenant `empresaId`. No tesorería. No cadena OV.

QA: usuarios `QA-APR-2108-*` en EMP-EXPORT, PIN `4821`.

## Lo que viene / lo que va

| | Se va | Se queda |
|---|---|---|
| Runtime AND | Un PIN del principal cierra el paso | Ambos (todos) deben PIN; OC sigue `PENDIENTE_APROBACION` hasta el último |
| Runtime OR | Extra no ve bandeja | Ambos ven pendiente; **un** PIN cierra; el otro queda omitido (gris) |
| Cadena persistida | Solo `aprobacionCadenaIds: string[]` (pierde logica/co-aprobadores) | Snapshot de pasos con logica + estado por persona |
| Campana enviar | Solo `aprobadorId` principal | Todos los pendientes del paso; **solicitante** recibe aviso de «enviada» |
| V1 bandeja | `compras:write` / `compras:read` cuentan como bandeja | Solo pantalla **Compras → Aprobaciones** (o `*`). Admin `*` sigue OK |

## Snapshot de cadena (persistir en OC)

JSON en `OrdenCompra` (campo nuevo, p.ej. `aprobacionCadena`). `aprobacionCadenaIds` se mantiene (ids del primer miembro de cada paso, compat).

```ts
type PasoCadena = {
  logica: 'SIMPLE' | 'AND' | 'OR';
  aprobadores: { id: string; nombre: string; estado: 'PENDIENTE' | 'APROBADA' | 'RECHAZADA' | 'OMITIDA' }[];
};
```

Bandeja: **una fila `AprobacionOc` por integrante del paso actual** (`logica` en la fila). `getAprobaciones` por `aprobadorId = user.sub` ya sirve si hay N filas.

Enum `EstadoAprobacionOc`: añadir `OMITIDA` (OR: el que no firmó cuando el otro sí).

## Reglas de resolución (PIN)

- Asignado = hay fila PENDIENTE con `aprobadorId = user.sub` (o admin override).
- **AND:** marcar esa fila APROBADA. Si quedan PENDIENTE en el mismo `pasoOrden` → no escalar, OC sigue pendiente. Si no quedan → escalar o APROBADO.
- **AND rechazo:** una RECHAZADA cierra la OC en RECHAZADO; otras PENDIENTE del paso → OMITIDA o RECHAZADA (documentar); no APROBADO.
- **OR:** una APROBADA cierra el paso; hermanas PENDIENTE → **OMITIDA**; escalar o APROBADO.
- **OR rechazo:** si aún hay otro PENDIENTE, el paso no cierra (el otro puede aprobar). Si todos rechazaron → OC RECHAZADO.
- Campana: al abrir paso, upsert `OC_PENDIENTE` a **cada** pendiente. Al cerrar OC, `OC_RESULTADO` al `creadoPorId`. Al **enviar**, también campana al solicitante (`OC_ENVIADA` o `OC_RESULTADO` claro: «OC X enviada a aprobación»).
- PIN: extras AND/OR ya están en `nodo.aprobadores`; deben poder configurar y usar PIN.

## Visual seguimiento

`ApprovalChainTimeline` / `buildApprovalTimelineSteps` en listado OC, detalle y bandeja.

Por cada paso:

- **AND:** cada integrante con estado (espera / aprobó / rechazó). Badge AND.
- **OR:** ambos en espera al inicio; si uno aprueba: ese en verde «aprobó», el otro **gris omitido** «no requirió firma»; continuar cadena.
- Pasos futuros: integrantes visibles, estado pendiente (no actuales).
- Compacto: `1/2 AND` o `OR · Nombre`.

No mezclar con `workflows-admin`.

## Tests

- Jest: AND dos PIN; un PIN no cierra; OR un PIN omite al otro; rechazo AND; V1 SIN-BAN con `compras:write` sin pantalla Aprobaciones → `APROBADOR_SIN_BANDEJA`; campana solicitante al enviar.
- No dropear enum PG `COTIZACION`.

## QA retest (después)

APR-AND, N-AND, APR-OR (extra ve pendiente **antes**), N-SOL, V1. Usuarios QA-APR-2108 ya existen; no reset BD.
