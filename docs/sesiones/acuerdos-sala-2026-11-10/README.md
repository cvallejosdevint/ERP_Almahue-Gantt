# Avance acuerdos sala 10/11/2026

Minuta: [`docs/reuniones/minutas/reunion-2026-11-10-cliente.md`](../../reuniones/minutas/reunion-2026-11-10-cliente.md)

## Entregables

| Archivo | Uso |
|---|---|
| [`comparacion.html`](comparacion.html) | Antes / despues con NUEVO |
| [`recorrido.html`](recorrido.html) | Pins sobre controles nuevos |

## Implementado (todos los acuerdos del dia)

| ID | Acuerdo | Touch |
|---|---|---|
| A1 | Vista simple / detalle + zoom | `EsquemaRamasAprobacion.tsx` |
| A2 | Topes CLP/USD/CNY al editar usuario | `UsuariosPage.tsx` |
| A3 | Color por rango 1-9 | `lib/rango-colores.ts` |
| A4 | Colores reutilizados en cadena OC | `ApprovalChainVisual` + `approval-engine` (`rango`) |
| A5 | Sync organigrama <> usuarios | `syncUsuarioCargosMiembro` + miembros M:N |
| A6 | Usuario en dos jefaturas | `cargosAsignados` / `cargoIdsExtra` API + UI |
| A7 | VºBº reversa en edit rama | `vbReversaUsuarioId` |
| A8 | Dos VºBº desde ramas distintas | `solicitud-reversa-edicion` resuelve por rama |
| A9 | Contratistas sin gerencia (rango 1) | validacion al crear/editar cargo |
| A10 | Basta un aprobador del tope (OR) | badge «OR · basta uno» + default OR |
| P5 | Auto-ejecutar reversa al 2º VºBº (sin PIN solicitante) | `aprobarVbContabilidadSolicitud` > `reversarProforma` (**Listo** 11/11) |
| P6 | Mantenedor Temporadas | schema + catalogos + `/catalogos/temporadas` |
| P7 | OC servicio: RECEPCIONADA + asiento recepcion; no centraliza | `oc-estado.util` + `planAsientoRecepcion` + omit en centralizacion (**Listo** 11/11) |

## Respaldo previo

- `erp_back` `703c8cf` chore: respaldo WIP pre acuerdos sala 10/11
- `erp_front` `c9d3a79` chore: respaldo WIP front pre acuerdos sala 10/11

## Migraciones locales

- `20261110230000_rama_vb_reversa_usuario`
- `20261110234500_temporadas` (aplicar con `prisma db execute` si `_prisma_migrations` esta vacia)
