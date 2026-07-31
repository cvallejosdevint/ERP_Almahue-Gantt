# 10 — AS-IS / TO-BE operativo

Fecha: 2026-07-31 (actualizado oleada alto/medio impacto)  
Canvas: `operativo-as-is-to-be.canvas.tsx` (abrir junto al chat)

## Veredicto

| Alcance | ¿Operativo? | Nota |
|---------|-------------|------|
| **Piloto interno** (QA/Admin, MODO REAL, sin SII live) | **SÍ** | Flujos core + oleada alto/medio cerrada |
| **Producción temporada / DTE real** | **NO todavía** | Integración DTE diferida (sin proveedor hasta docs); inventariable/AlmaWeb; Excel MJ |

## Cotizaciones (D9)

**Sin cambio de flujo.** Se mantiene registro/aprobación actual. Preguntar a Sergio qué acordaron cuando se cortó la llamada (mute ~07:01).

## Resumen conteos

| Estado | Cant. |
|--------|------:|
| OK | 13 |
| Parcial | 4 |
| Gap | 1 |
| Diferido | 2 |

## Matriz (síntesis)

| ID | Área | TO-BE | AS-IS | Estado | Piloto | Prod |
|----|------|-------|-------|--------|:------:|:----:|
| INF-01 | Infra | Stack estable MODO REAL | 54/54 GET; 0 gaps front↔Nest | OK | Sí | Sí |
| RBAC-01 | Permisos | Mutaciones por rol; solo jefe aprueba | Smoke 5 roles + 403 API | OK | Sí | Sí |
| RBAC-02 | Matriz pantallas | permisosPantalla en roles | Script `seed-permisos-pantalla.ts` | OK | Sí | Sí |
| WF-01 | Reglas | Jefes por módulo/monto | Reglas Compras/Contratistas OK | OK | Sí | Sí |
| OC-01 | Flujo OC | Emitir→bandeja→resolver | Front + bandeja + anular→ANULADA | OK | Sí | Sí |
| OC-02 | Re-solicitud rechazada | Nueva pendiente limpia | updateOrden recrea bandeja PENDIENTE | OK | Sí | Sí |
| OC-03 | OC→recepción→factura | Solo elegibles en libro | Seed `OC-QA-REC-005` + registro | OK | Sí | Sí |
| PF-01 | Proformas | Aprobar/lock/factura/reversa | Validado | OK | Sí | Sí |
| VEN-01 | Ventas/DTE | Emisión + PDF/XML SII | Libro: folio→print + reenvío si trackId | OK | Sí | Parcial |
| VEN-02 | Cotizaciones | Definir flujo | Sin cambio; pendiente Sergio | Parcial | — | — |
| CON-01 | Contabilidad | Periodos/asientos/plan | Base OK; factor honorario vigente | OK | Sí | Parcial |
| TES-01 | Tesorería | Cartola/calce/aging | Aging con historial vencimiento | OK | Sí | Parcial |
| INS-01 | Insumos | Inventariable + AlmaWeb | Solo movimientos; soft bodega catálogo | Gap | — | Sí |
| GS-01 | DTE proveedor | Integración oficial | **Removido del código** hasta documentación | Diferido | — | — |
| DATA-01 | Datos | Maestros coherentes | Audit BD + seed E2E OC | OK | Sí | Sí |
| EXP-01 | Exportación | Cliente/aduana | Sin UI | Diferido | — | — |
| COB-01 | Cobranza | Módulo R4-18 | Solo propuesta | Diferido | — | — |
| AUD-01 | Audit vencimiento | Quién/cuándo | Historial JSON + columna UI | OK | Sí | Sí |
| ROL-01 | Roles temporales | vigenciaDesde/Hasta | Login/refresh/perfil + UI Usuarios | OK | Sí | Sí |
| PIN-01 | PIN aprobación | 4 dígitos por rol; perfil + al aprobar/rechazar | `Rol.aprobarConPin` + hash usuario; OC/proformas | OK | Sí | Sí |

## Oleada alto/medio (esta entrega)

| Ítem | Estado |
|------|--------|
| OC-02 re-solicitud RECHAZADO→EMITIDO + bandeja | Hecho |
| permisosPantalla roles | Script seed |
| Seed E2E OC→recepción→registro + bodega | Hecho en `audit-and-reset-flujo-oc.ts` |
| R4-24 print OC con líneas | Hecho |
| R4-10 folio libro → preview + watermark BORRADOR | Hecho |
| R4-14 factor honorario vigente | Hecho (API + UI) |
| Audit vencimiento aging | Hecho |
| Integración DTE / GoSocket | **Removida** del código hasta docs oficiales |
| Roles temporales MVP | Hecho |
| PIN 4 dígitos aprobación (Sergio) | Hecho (flag rol + perfil + OC/proformas) |
| Cotizaciones | **Sin tocar** (pregunta Sergio) |

## Go-live recomendado

### Ahora — piloto
1. Usuarios QA + Admin en MODO REAL.
2. Sembrar pantallas: `npx ts-node -r tsconfig-paths/register scripts/seed-permisos-pantalla.ts`
3. Reset OC E2E: `npx ts-node -r tsconfig-paths/register scripts/audit-and-reset-flujo-oc.ts`
4. Ejercer: OC (reabrir rechazada), recepción, libro ventas (folio/PDF), aging, factores, roles temporales.

### Antes de producción
1. Documentación oficial DTE + reintegrar proveedor cuando exista.
2. Inventariable + carga Excel AlmaWeb (MJ).
3. Cartola Excel tipo MJ + plan cuentas Excel cliente.
4. Cerrar decisión cotizaciones con Sergio.

## Evidencia

- [`06-MATRIZ-CUMPLIMIENTO-REU4.md`](./06-MATRIZ-CUMPLIMIENTO-REU4.md)
- [`07-FLUJO-COMPLETO.md`](./07-FLUJO-COMPLETO.md)
- [`08-DATOS-FLUJO-OC.md`](./08-DATOS-FLUJO-OC.md)
- [`09-AUDITORIA-BD.md`](./09-AUDITORIA-BD.md)
