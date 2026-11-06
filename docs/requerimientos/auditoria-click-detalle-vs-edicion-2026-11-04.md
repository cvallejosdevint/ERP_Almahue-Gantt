# Auditoria: click en lista = detalle (no edicion)

Fecha: 2026-11-04. Alcance: `ERP/erp_front` listados con ficha/CRUD.

**Avance 04/11 noche (barrido front):** P0 `MockListPage` (`viewFirst` default true, «Editar datos», `onToggleActiva`; sin icono Ver redundante). Monedas, Bancos, Plan cuentas (click=detalle), Roles (click=ficha), AF param, Contratista param, catalogos, Empresas, Usuarios, Clientes con toggle donde aplica. Tipografia `DataTable` unificada. Queda: Eliminar hard-delete en catalogos sin API delete; Indicadores BC N/A; algunos wizards HTML.

## Regla pedida

| Accion | Comportamiento esperado |
|---|---|
| Click en fila | Abre **detalle** (solo lectura) |
| Editar | Accion aparte: boton/icono **Editar datos** (no el click de la fila) |
| Parametrizacion (catalogos simples) | En Acciones: **1) Activar/Desactivar 2) Editar 3) Eliminar** |
| Modal detalle catalogo | Tamano estandar minimo (propuesta: `lg`) para fichas cortas C5 |

Pedidos relacionados: historial en documento (skill diseno); ficha densa Plan de cuentas (C4) sigue siendo excepcion de densidad, no de click=editar.

## Mecanismo actual (`MockListPage`)

Ya existe `viewFirst`:

- `viewFirst={true}`: click / "Ver ficha" abren modal en solo lectura; lapiz fuerza edicion; footer "Editar".
- **Default `viewFirst={false}`**: click abre **edicion directa** (`setIsEditing(forceEdit \|\| !viewFirst)`).

Hoy **solo** `ContratistasPages` (listado) usa `viewFirst={true}`.

Huecos del componente para Parametrizacion:

1. Default deberia ser `viewFirst={true}` (o forzarlo en todos los MockList de catalogos).
2. Texto footer: hoy dice `Editar`; pedido: **Editar datos**.
3. No hay accion de fila **Activar/Desactivar**: solo checkbox `activa` dentro del form.
4. Casi ningun catalogo pasa `onDelete` (no hay Eliminar en Acciones).
5. Tamano modal: default ya es `lg` (bien para C5); Parametrizacion rica (Plan cuentas) sigue custom.

## 1. Parametrizacion (menu Sidebar) - matriz

Leyenda: Det=click abre detalle; Ed=accion Editar; AD=activar/desactivar en Acciones; Del=eliminar en Acciones; OK / DEUDA / N/A.

| Pantalla | Ruta | Impl | Det | Ed | AD | Del | Notas |
|---|---|---|:---:|:---:|:---:|:---:|---|
| Monedas | `/catalogos/monedas` | Custom `pages/parametrizacion/MonedasPage` | DEUDA | DEUDA | OK | Parcial | Screenshot: solo desactivar + basura. Sin editar. Sin onRowClick. Modal solo alta. |
| Unidades de medida | `/catalogos/unidades` | MockList `CatalogosPages` | DEUDA | Parcial | DEUDA | DEUDA | Click = edicion. Activa solo en form. Sin onDelete. |
| Bancos | `/catalogos/bancos` | Custom `BancosPage` | DEUDA | OK (abre edit) | DEUDA | OK | Sin onRowClick. Activo solo checkbox en form. |
| Centros de costo | `/catalogos/centros-costo` | MockList | DEUDA | Parcial | DEUDA | DEUDA | Igual patron MockList default. |
| Elementos de costo | `/catalogos/elementos-costo` | MockList `ContabilidadPages` | DEUDA | Parcial | DEUDA | DEUDA | Vigencia ANULADO en form, no AD en fila. |
| Areas de negocio | `/catalogos/areas-negocio` | MockList | DEUDA | Parcial | DEUDA | DEUDA | |
| Conceptos | `/catalogos/conceptos-flujo` | MockList | DEUDA | Parcial | DEUDA | DEUDA | |
| Codigos financieros | `/catalogos/codigos-financieros` | MockList | DEUDA | Parcial | DEUDA | DEUDA | |
| Tipos de documento | `/catalogos/tipos-documento` | MockList | DEUDA | Parcial | DEUDA | DEUDA | |
| Plan de cuentas | `/catalogos/plan-cuentas` | Custom arbol | Parcial | OK (lapiz) | OK (fila) | OK | Click nodo = edicion (`openEdit`). Tiene deshabilitar/reactivar + borrar. Alinear: click = ficha lectura + Editar datos. |
| Factor de honorarios | `/catalogos/factor-honorarios` | MockList | DEUDA | Parcial | N/A | DEUDA | Factores por vigencia; AD tipico N/A. Click = edit. |
| Indicadores BC | `/catalogos/indicadores-bc` | Custom lista | N/A | N/A | N/A | N/A | Series/valores sync; no ficha CRUD tipica. Fuera del trio AD/Ed/Del. |
| Proveedores | `/catalogos/proveedores` | Custom ficha | OK | OK | Parcial | ? | Click = vista (`viewMode`). Editar aparte. Revisar AD en Acciones. |
| Productores | `/catalogos/productores` | Custom ficha | OK | OK | Parcial | ? | Click = vista. |
| Contratista (param) | `/catalogos/contratista` | Varios MockList | DEUDA | Parcial | DEUDA | DEUDA | Labores, sectores, faenas, actividades, UM: sin viewFirst ni onDelete. |
| Activo fijo (param) | `/catalogos/activo-fijo` | Varios MockList | DEUDA | Parcial | DEUDA | DEUDA | Familias/subfamilias/ubicaciones/tipos. |

**Conteo Parametrizacion (15 con CRUD tipico, excl. Indicadores BC):** 0 cumplen el trio completo + click detalle. Solo Proveedores/Productores cumplen click=detalle. Monedas es el ejemplo visible de AD+Del sin Editar ni detalle.

## 2. Resto del ERP - click detalle vs edicion

### Cumplen click = detalle (referencia)

| Area | Pantalla | Como |
|---|---|---|
| Contratistas | Listado | `viewFirst` + `onRowClick` detalle |
| Contratistas | Aprobaciones / Auditoria / Reporte dia | detalle modal |
| Comercial | OV, Libro ventas (docs), Clientes?* | OV preview; docs `setPreviewDoc` |
| Compras | OC listado, Recepciones, Notas cobro | `setDetalle` / preview |
| Contabilidad | Asientos, Auditoria | detalle; Editar aparte en asiento |
| Insumos | Movimientos, Guias, Ordenes, Auditoria | detalle |
| Tesoreria | Cartola, Conciliacion, CC | detalle |
| Catalogos | Proveedores, Productores | vista primero |
| Activo fijo | Maestro / movimientos | detalle |

\*Clientes/Prospectos via MockList **sin** `viewFirst` = deuda (click edita).

### Deuda: click abre edicion o no hay detalle

| Area | Pantalla / archivo | Problema |
|---|---|---|
| Comun | `MockListPage` default | `viewFirst=false` infecta todos los consumidores |
| Admin | Roles | `onRowClick={openEdit}` |
| Admin | Usuarios, Empresas | MockList sin viewFirst |
| Admin | Workflow aprobaciones | Editar en botones; click grupo selecciona (OK parcial) |
| Comercial | Clientes, Prospectos | MockList sin viewFirst |
| Contratistas | Ingreso diario, Proformas N1, Tarifas | MockList sin viewFirst (proformas listado real usa detalle aparte en otra ruta) |
| Tesoreria | Pagos (MockList), Anticipos | sin viewFirst; conciliacion si tiene detalle |
| Contabilidad | Honorarios (ya en param), Elementos | MockList |
| Presupuestos | PresupuestosPage | boton Editar; sin click detalle tipico |
| Bancos / Monedas custom | ver seccion 1 | |

### Listas solo consulta / sin ficha (N/A o baja prioridad)

Reporteria, Balance 8 col, Estados financieros, Flujo caja, Aging, Centralizacion masiva, Dashboard, Indicadores BC, Cierre bodega (operativo).

## 3. Plan de remediacion propuesto

### Fase P0 - base (desbloquea Parametrizacion y MockList)

1. `MockListPage`: default `viewFirst={true}`.
2. Footer lectura: boton **Editar datos** (no solo "Editar").
3. API opcional `onToggleActiva?: (row) => void` + icono Activar/Desactivar en Acciones (antes de Editar y Eliminar).
4. Documentar en skill `almahue-diseno`: click = detalle; Editar datos; Parametrizacion = AD + Editar + Eliminar; modal min `lg`.

### Fase P1 - Parametrizacion

1. Monedas custom: onRowClick detalle; Acciones = AD (ya) + Editar datos + Eliminar; modal detalle `lg` con Editar datos.
2. Bancos: igual (detalle click; AD en fila; no abrir edit al click).
3. Todos los MockList de catalogos/param: `viewFirst` (heredado del default) + cablear `onDelete` donde API exista + `onToggleActiva` donde haya `activa`/`activo`.
4. Plan de cuentas: click fila/nodo abre ficha lectura; lapiz / Editar datos edita.
5. Param Contratista + Activo fijo: mismos defaults.

### Fase P2 - resto MockList / Roles

Clientes, Prospectos, Usuarios, Empresas, Ingreso diario, Tarifas, Anticipos, Pagos MockList, Roles (`onRowClick` > detalle).

### Fase P3 - pulido

Tamano modal estandar documentado; checklist QA por pantalla Parametrizacion; actualizar esta matriz al cerrar cada fila.

## 4. Criterio de aceptacion (checklist QA)

Por cada pantalla Parametrizacion con CRUD:

- [ ] Click fila abre modal/panel **solo lectura** (campos disabled o ficha).
- [ ] Existe **Editar datos** (footer y/o Acciones) que habilita edicion.
- [ ] Acciones: Activar o Desactivar (si aplica), Editar, Eliminar - iconos distintos, tooltip AccionConNombre.
- [ ] Eliminar no se dispara desde el click de fila.
- [ ] Modal detalle catalogo simple no usa `wide` vacio; minimo usable `lg`.

Por otras listas con documento:

- [ ] Click = documento/detalle; edicion solo con accion explicita (salvo alta Nueva).

## 5. Fuera de alcance de esta auditoria

- Logica backend de soft-delete vs hard-delete.
- Ordenes de compra listado (skill: fuera hasta pedido).
- Indicadores BC como series (no trio AD/Ed/Del).
