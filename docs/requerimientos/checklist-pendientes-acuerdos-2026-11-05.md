# Checklist: lo que queda por ver

Fecha: 2026-11-05  
Alcance: acuerdos 26-28/10 + 03/11 (sin CAF / SII live).

Reunion 05/11 ya transcrita. La minuta, la matriz de que dia pisa a otro y la auditoria de lo que falta estan en `docs/reuniones/minutas/reunion-2026-11-05-cliente.md`, `docs/requerimientos/matriz-acuerdos-por-dia-2026-11-05.md` y `docs/requerimientos/auditoria-acuerdos-sistema-2026-11-05.md`. Este checklist no marca como hechos los pedidos nuevos de hoy.

## Cerrado en este lote

- [x] ER solo periodo; ESF acumulado + resultado del ejercicio
- [x] Balance 8 columnas: rango 1-ene → periodo (UI + `desde`/`hasta` en API)
- [x] Asiento CONTABILIZADO inmutable (montos/cuentas/glosas) + `creadoPor*` / cuándo
- [x] OC: cuenta primero; CC y elemento bloqueados sin cuenta; 1 CC por línea
- [x] FAC multi-OC + insumos madre/hijas por guía + columna Contabilizado en Órdenes de insumos
- [x] Asociación PF solo desde Compras (código muerto de asociar FAC en Proformas eliminado)
- [x] Nota cobro embarcador + Asoex/gasto directo; sin Excel masiva; calce 1 a 1; vencimiento +1 mes
- [x] Contratistas: sin Teléfono 2 en ficha; labor alta con 4 dígitos; labor no reusable en otra actividad; tope 24 h en JORNADA; KPI horas
- [x] Mantenedor Packings (ficha tipo proveedor) + bodega al alta (`Packing` / migración `20261105190000`)
- [x] Receta packing (plantilla Almahue o por packing) + import CSV vía API
- [x] Producción mensual: packing + receta + cajas → movimientos `CONSUMO_PACKING` + stock
- [x] Cierre bodega: bloque packing desde movimientos / fallback `producciones-packing` API
- [x] Organigrama visual PDF MJ (`/admin/organigrama`): árbol `jefeId` + flujo analista > jefatura > área > GG

## Pendiente / a validar en QA

### Contabilidad
- [x] Parametrizar cuentas puente del Balance 8 (Admin > Empresas: resultado del ejercicio y acumulado; vacio conserva 2-4-04-02-004 / 2-4-04-02-001)
- [x] Carga masiva asientos: cuadratura USD dual (columnas debe/haber en moneda paralela)
- [x] Propagar `creadoPor*` en asientos automaticos de libro, cierre, cartola, centralizacion y revaluacion
- [x] Migración `20261105180000_asiento_creado_por` aplicada en local (`localhost:5433`, SQL directo + registro; no `migrate deploy` a ciegas)
- [x] Migración `20261105190000_packing_receta_produccion` aplicada en local (mismo criterio)
- [ ] Migraciones en prod / otros entornos (incluye `20261105200000_checklist_acuerdos_nov`)
- [x] Planta fuera del plan de cuentas (la UI ya no la ofrece y el alta/import la deja en falso)

### Compras / Libro SII
- [x] Auto-cuenta desde articulo maestro al armar linea OC (selector en el wizard y respaldo al guardar si la descripcion parte con el codigo)
- [ ] Contabilizado de hijas: QA de punta a punta (guia > hija > FAC > asiento > madre CONTABILIZADA)
- [x] Enum Prisma `ACTIVO_FIJO` en tipo OC alineado con el front (migracion `20261105200000`)
- [x] Periodo cerrado: no reabrir contable; el ajuste queda en Contabilidad > Reversas (2 VB)

### Contratistas
- [x] Migrar codigos de labor legacy (L01…) a 4 digitos sin romper tarifas (la tarifa sigue por id)
- [x] Periodicidad proforma quincenal (Mensual / Quincenal en el alta)
- [x] Filtro de proformas por mes exacto (un rango `2026-06/2026-07` no arrastra otros meses). Wizard de reversa: no ofrece la clave hasta conocer el periodo; abierto y cerrado muestran motivo y los dos vistos buenos; el texto de traspaso ya no pide reabrir el mes

### Insumos / packing
- [x] Demo mock packing/recetas/producción/OA + seed local EMP-EXPORT (`scripts/seed-packing-demo-local.ts`)
- [x] Modo demo: reseed al montar + periodo forzado `2026-08` (`AppSettingsProvider`); OA/Packings/Cierre/Notas/Asientos/ER/ESF/Balance8 sin toast «No se encontró»
- [x] Sesión antes/después `docs/sesiones/acuerdos-noche-packing-org-2026-11-05/` (comparacion + recorrido, capturas 1536x960)
- [x] API packings/recetas/producciones levantada (reinicio Nest + rutas 200)
- [x] Guia DTE 52 traspaso a bodega del packing (el destino solo lista bodegas del mantenedor)
- [ ] Stock negativo / OA PIN: retest operators
- [ ] QA punta a punta: alta packing → receta → producción → cierre mes

### Tesorería (Lupe, 28/10 `[02:15]`-`[02:25]`)
- [x] Carga semanal de cartola sin repetir movimientos ya importados del mismo banco (fecha + ingreso/egreso + monto + referencia o glosa)
- [x] Avisar si el archivo no es del periodo de la sesion y excluir el movimiento del mes anterior que viaja al final del archivo (`[02:17:23]`-`[02:18:01]`)
- [x] Partir un ingreso de cartola en 2 o 3 codigos financieros, en la moneda de origen, sin pasar el monto y avisando si queda saldo (`[02:23:57]`-`[02:25:36]`)
- [x] Nombre de la cuenta bancaria junto al numero, al cargar bancos (`[02:15:47]`)

### Insumos (28/10 `[01:38]`)
- [x] Devolucion a proveedor al precio de la guia o factura de origen, no al precio promedio de bodega

### Compras / Libro (03/11 PM `[55:50]`)
- [x] No mostrar Contabilizar si el documento no esta asociado a una OC o a una proforma

### Carga de asientos (MJ, 26/10 `[08:47]`)
- [x] Si falta un dato obligatorio, rechazar esa linea y entregar el reporte (no abortar el archivo entero)

### Fuera de alcance (dejar explícito)
- [ ] CAF / emisión SII live
- [ ] Cadena OC desde organigrama (jefaturas) en lugar de grupos/escalas - solo vista; motor sigue grupos+escalas
- [ ] SMTP PIN (H9)
- [ ] Packing operativo externo (cajas/pallets COMEX)

## Cómo probar rápido

1. Contabilidad › Estados financieros (resultado): sin toggle acumulado; solo mes.
2. Contabilidad › Balance 8: subtítulo 1 ene → periodo.
3. Contabilidad › Asientos: columna Quién/cuándo; editar glosa de CONTABILIZADO debe fallar.
4. Compras › Nueva OC: CC deshabilitado hasta cuenta.
5. Contratistas › Proformas: no hay Asociar factura; Libro de Compras sí.
6. Compras › Notas de cobro: solo selección manual; tipo Asoex / gasto directo.
7. Parametrización › Labores: alta con código `0101`; ficha contratista sin Teléfono 2.
8. Admin › Organigrama: árbol por jefe + diagrama ruta OC del PDF MJ.
9. Insumos › Packings: alta con RUT/razón social (crea bodega).
10. Insumos › Órdenes de aplicación › Recetas / Producción: packing obligatorio en producción; cierre ve consumo packing.
