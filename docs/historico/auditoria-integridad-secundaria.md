# Auditoría de integridad secundaria (UI vs Prisma)

**Alcance:** Tesorería, Contabilidad (profunda), Contratistas (proformas) y Workflows-Admin legado.  
**Cruce:** `ERP/erp_front` ↔ `ERP/erp_back/prisma/schema.prisma` (y DTOs/servicios solo para confirmar qué llega a persistir).  
**Fecha:** 2026-08-16.  
**Complemento de:** `docs/auditoria-integridad-datos.md` (Comercial / Compras / Insumos).

**No se modificó código.** Este documento es hallazgos + plan de refactor.

Tenant: toda fila de negocio lleva `empresaId`. Schema PostgreSQL `erp`.  
Instrucción vigente: **no inventar UI de maestro Productor**.

---

## 0. Mapa de persistencia (lo que sí conecta)

| UI | Modelo / campos | Notas |
|---|---|---|
| Tesorería › Flujo de caja | `MovimientoCaja`: fecha, concepto, ingreso, egreso; `saldo` recalculado en API | Formulario de `TesoreriaPages.FlujoCajaPage` pega a create/update |
| Tesorería › Pagos | `Pago`: fecha, beneficiario, monto, medio, estado, monedas, TC, `documentosCalce`, `movimientoCartolaId` (query `?movId=` desde cartola) | Calce 1:1 con `MovimientoCartola` si viene el id |
| Tesorería › Cartolas (import Excel/PDF) | `CartolaBancaria` + `MovimientoCartola` (líneas del parser) | Camino serio: `preview` + `import-archivo` |
| Tesorería › Cartolas › contabilizar | `MovimientoCartola.estadoContable`, `asientoId`/`asientoNumero` + `Asiento` origen `CARTOLA:{id}` | Requiere servicio de contabilización y periodo abierto |
| Tesorería › Anticipos | `AnticipoProductor` cabecera (textos + montos) y calce (`montoCalzado`, `documentosCalce`) | **Sin FK** a cliente/proveedor |
| Tesorería › Cuentas corrientes | `CuentaCorrienteMovimiento` (listado + ajuste) | `terceroTipo` incluye `PRODUCTOR` |
| Tesorería › Aging | `DocumentoAging` vía sync; UI edita `fechaVencimiento` | Alta no es formulario libre |
| Contabilidad › Plan de cuentas | `CuentaContable` + N:N `CuentaCentroCosto` / `CuentaElementoCosto` / áreas | Flags `requiereCc` / `requiereArea` / `requiereElemento` / `requiereEspecie` |
| Contabilidad › Asientos | `Asiento` (numero, periodo, fecha, tipo, glosa, estado, `lineas` JSON) | Cuadre debe=haber; periodo ABIERTO si CONTABILIZADO |
| Contabilidad › Periodos | `PeriodoContable` + `PeriodoContableEvento` (cierre/reapertura) | Alta por código `aaaa-mm` |
| Contabilidad › Config SII | `ConfigContableSii` | Mapeo tipo DTE → cuenta; no es certificación SII |
| Contabilidad › Honorarios | `FactorHonorario` | Factor anterior/nuevo + vigencia |
| Contabilidad › Elementos de costo | `ElementoCosto` | Código, nombre, depto, vigencia |
| Contabilidad › Centralización | Asientos de origen ventas/compras/contratistas/bodega | Preview + ejecutar |
| Contratistas › ficha / tarifas | `Contratista`, `TarifaContratista` | Id interno `CTR-{empresaId}-{n}` |
| Contratistas › labor diario | `IngresoLaborDiario` (FKs contratista, CC, labor, actividad) | Monto = cantidad × PU en API |
| Contratistas › proformas | `ProformaContratista` (numero, contratistaId, periodo, montoNeto, moneda) | Cadena se llena al **solicitar**, no en el alta |
| Contratistas › asociación labores | `IngresoLaborDiario.proformaId` | Calce de monto en UI |
| Contratistas › factura / traspaso | `FacturaContratista`, `PeriodoCierreContratista` | Acciones, no mantenedor completo |
| Admin › Aprobaciones | `GrupoAprobacion`, `NodoEscalaAprobacion`, `DelegacionAprobacion` | Fuente Reu6 |
| Admin › Aprobaciones (bloque legado) | `WorkflowConfig` (`workflows-admin`) | Sigue CRUD en la misma pantalla |
| `/workflow` | — | Redirect a `/compras/aprobaciones` (página retirada) |

---

## 1. Cables sueltos (UI que no guarda bien, o guarda otra cosa)

### Tesorería

| # | Pantalla | Campo / acción UI | Qué pasa en Prisma | Riesgo |
|---|---|---|---|---|
| T1 | Cartolas › «Nueva cartola» (formulario MockList) | Banco, periodo, nombre archivo, **Nº movimientos**, **monto total** | `createCartola` persiste **cabecera**. El front **no envía `lineas`**. Quedan `movimientos`/`montoTotal` numéricos **sin** filas `MovimientoCartola` | Cabecera huérfana: no hay nada que contabilizar ni calzar. El camino correcto es **importar archivo** |
| T2 | Cartolas › alta manual | `usuarioCarga: 'demo'` hardcodeado | Se escribe siempre `'demo'` en `CartolaBancaria.usuarioCarga` | Auditoría de carga falsa en API real |
| T3 | Pagos | Beneficiario (texto libre) | `proveedorId` solo se rellena si el texto **coincide exacto** (insensitive) con `Proveedor.razonSocial`, o si el DTO trae `proveedorId` (el form **no** lo envía) | Pago desligado del maestro; homónimos |
| T4 | Pagos › documentos a calzar | Texto obligatorio (`FAC-8801` o `Cartola TRX-…`) | `Pago.documentosCalce` es `String?`, **no FK** a aging, factura ni OC | Calce narrativo; aging no se actualiza salvo `applyPagoToAging` por heurística de texto |
| T5 | Pagos desde cartola | Query `movId` | Sí persiste `movimientoCartolaId` + marca `MovimientoCartola.pagoId` | OK **solo** si se entra por el link de cartola. Alta «Nuevo pago» no calza TRX |
| T6 | Conciliación › «Nueva conciliación» | Banco, periodo, **cantidad de movimientos**, asiento opcional | Crea `Conciliacion` con `conciliados=0`, **sin `cartolaId`**, **sin** `MovimientoConciliacion` | KPI y detalle viven de otra tabla vacía. El trabajo real está en cartolas |
| T7 | Conciliación › asiento | `asientoNumero` texto | No valida existencia de `Asiento`; `asientoId` queda null | Referencia rota |
| T8 | Flujo de caja | `saldo` en grilla | Lo recalcula el backend; el mock de demo inventa un saldo | En API real está bien; no usar demo como evidencia |
| T9 | Cuentas corrientes › links «Ver pago/factura» | Heurística por `documentoRef` (`Cartola TRX…`, `PAG-…`) | `CuentaCorrienteMovimiento` **no** tiene `pagoId` / `documentoComercialId` en Prisma | Deep-link frágil; comentario en front: «si el backend lo expone más adelante» |
| T10 | Anticipos | Productor / RUT libres | Ver sección 3: CC usa `terceroId = rut \|\| productor` (string) | Libro de productores partido o fusionado sin maestro |

### Contabilidad

| # | Pantalla | Campo / acción UI | Qué pasa en Prisma | Riesgo |
|---|---|---|---|---|
| C1 | Asientos (línea) | Centro de costo (select) | Va en JSON `Asiento.lineas[].centroCostoId` **si** se elige. Si la cuenta tiene `requiereCc` y el usuario deja vacío, el API **rechaza** (correcto). No hay tabla de líneas: no hay FK relacional | Mayor por JSON; no se puede join SQL a `CentroCosto` |
| C2 | Asientos (línea) | **No hay** select de área ni de elemento | `contabilizar.service` **exige** `areaNegocioId` / `elementoCostoId` si la cuenta tiene `requiereArea` / `requiereElemento` | Imputación imposible desde UI para esas cuentas (409/400). Flags del plan vs formulario desalineados |
| C3 | Asientos (línea) | Moneda + tipo de cambio | DTO sí acepta `moneda`/`tipoCambio`; se guardan **dentro del JSON**. No hay columnas Prisma ni conversión a CLP en el mayor | TC «de adorno»: el debe/haber se guardan como montos ya digitados, no convertidos |
| C4 | Plan de cuentas | `requiereEspecie` | Flag en `CuentaContable`. **Ninguna** línea de asiento tiene especie | Flag sin efecto operativo |
| C5 | Honorarios | Campo «Usuario» texto | `FactorHonorario.usuario` es `String`, no FK a `Usuario` | Cualquiera escribe un nombre; no hay rastro de `userId` |
| C6 | Periodos › crear | Solo `codigo` (+ activo) | `anio`/`mes`/`fechaDesde`/`fechaHasta` los deriva el API. El DTO permite fechas explícitas; la UI no las manda | Aceptable si el backend cubre el mes calendario; no se puede abrir un periodo de temporada no-calendario desde UI |

### Contratistas / proformas

| # | Pantalla | Campo / acción UI | Qué pasa en Prisma | Riesgo |
|---|---|---|---|---|
| P1 | Proforma (alta) | numero, contratista, periodo, montoNeto, moneda | Persiste BORRADOR. **No** pide labores | Proforma sin `IngresoLaborDiario` hasta Asociación. Monto de cabecera puede no coincidir con labores |
| P2 | Proforma › solicitar aprobación | Botón (no campos de cadena) | Motor mezcla **`WorkflowConfig` legado** (pool `aprobadorIds` por monto) **y** grupos/escalas Reu6 | Dos verdades: una regla de monto en `workflows-admin` y otra cadena en grupos. Incumple «no mezclar» |
| P3 | Front contratistas | `getWorkflows` + `matchWorkflow` | Lectura del pool legado en UI para habilitar botones | La pantalla de negocio sigue acoplada al legado aunque Admin tenga grupos |
| P4 | Asociación labores | Calce `prf.monto` vs suma labores | Dominio: `ProformaContratista.montoNeto`. Si el mapper del API no expone `monto`, el calce UI puede usar `undefined` | Verificar mapper; no inventar campo `monto` en Prisma |
| P5 | Id contratista | No se captura | `id` = `CTR-{empresaId}-{count+1}` | Colisión posible si dos altas concurrentes (count no es secuencia) |

### Workflows-Admin legado

| # | Pantalla | Campo / acción UI | Qué pasa en Prisma | Riesgo |
|---|---|---|---|---|
| W1 | `/admin/aprobaciones` | Formulario de «regla» (nombre, módulo, montoMin/Max, **aprobadorIds**, activo) | Sigue `createWorkflowAdmin` / `updateWorkflowAdmin` → `WorkflowConfig` | Convive con `GrupoAprobacion` en la **misma** página. Operadores pueden creer que esa regla **es** la cadena |
| W2 | Mismo formulario | `WorkflowConfig.aprobadores` (`Int`, default 1) | Comentario Prisma: legado Reu4 «1 firma». La UI manda **lista de ids**, no el entero | Columna `aprobadores` no refleja la cadena Reu6; queda desfasada |
| W3 | `/workflow` | — | Solo `Navigate` a bandeja OC | No hay persistencia; no es cable suelto de datos |

---

## 2. Campos huérfanos (Prisma obligatorio o relevante sin captura UI)

Campos `id` / `empresaId` / timestamps se omiten (sistema).

### Tesorería

| # | Modelo.campo | Obligatorio | UI | Comentario |
|---|---|---|---|---|
| H-T1 | `Pago.proveedorId` | no | No hay select de proveedor | Huérfano de captura; lookup solo por nombre |
| H-T2 | `MovimientoCartola` (fecha, referencia, glosa, monto, tipo) | sí (por línea) | Alta manual de cartola **no** captura líneas | Solo import/parser |
| H-T3 | `MovimientoCartola.asientoId` | no | No se elige a mano | Lo llena «Contabilizar» |
| H-T4 | `Conciliacion.cartolaId` | no | Formulario no lo pide | Conciliación desconectada de cartola |
| H-T5 | `MovimientoConciliacion` (todas las columnas de línea) | sí al existir | No hay alta de movimiento; solo desconciliar | Tabla para un flujo que la UI de «nueva conciliación» no alimenta |
| H-T6 | `DocumentoAging.documentoComercialId` / `registroCompraId` | no | Solo sync | Correcto si el sync los llena; no hay alta UI |
| H-T7 | `DocumentoAging.vencimientoHistorial` | no | No se muestra | API puede escribir JSON al patch de vencimiento |
| H-T8 | `AnticipoProductor.saldo` | sí | Calculado (monto − calzado) | No debe ser editable; OK |
| H-T9 | `CuentaCorrienteMovimiento.origen` | no | Ajuste manda `AJUSTE`; anticipo manda `ANTICIPO` | Alta libre de CC no existe (bien) |

### Contabilidad

| # | Modelo.campo | Obligatorio | UI | Comentario |
|---|---|---|---|---|
| H-C1 | Línea asiento `areaNegocioId` / `elementoCostoId` | condicional (`requiere*`) | **Ausentes** en `AsientosPage` | Bloquean contabilizar cuentas con flags D9 |
| H-C2 | `CuentaContable.requiereEspecie` | flag | Plan sí; asiento no | Dimensión especie no modelada en `lineas` |
| H-C3 | `Asiento.lineas` como tabla relacional | — | JSON | Diseño actual; mayor/diario leen JSON |
| H-C4 | `PeriodoContable.fechaDesde` / `fechaHasta` / `anio` / `mes` | sí | Solo `codigo` | Derivados; OK si el API es la fuente |
| H-C5 | `PeriodoContableEvento` | sí al cerrar | Historial de solo lectura | OK |
| H-C6 | `ConfigContableSii` | por tipo SII | Hay pantalla | Certificación electrónica **fuera** (skill contabilidad) |

### Contratistas

| # | Modelo.campo | Obligatorio | UI | Comentario |
|---|---|---|---|---|
| H-P1 | `ProformaContratista.aprobadorId`, `aprobacionCadenaIds`, paso actual | no en alta | Se llenan al solicitar | No exponer como campos de alta (el solicitante no elige jefe) |
| H-P2 | `ProformaContratista.creadoPorId` | no | API desde JWT | OK |
| H-P3 | `FacturaContratista` (fecha, montoNeto, `proformasGrupoIds`) | sí al facturar | Acción «asociar factura», no form completo | Revisar si fecha/monto se piden o se copian de proforma |
| H-P4 | `IngresoLaborDiario.monto` / `estado` / `facturaNumero` | sí / default | Monto calculado; estado al asociar | OK |
| H-P5 | `PeriodoCierreContratista.asientoId`, `tipoCambio`, `proformaIds` | mixto | Traspaso de cierre | TC del periodo (D9) sí hay campo en centralización/traspaso; no duplicar por contratista |
| H-P6 | `Contratista.id` | sí, sin `@default` | Generado en servicio | No hay secuencia DB |

### Workflow legado

| # | Modelo.campo | Obligatorio | UI | Comentario |
|---|---|---|---|---|
| H-W1 | `WorkflowConfig.aprobadores` (Int) | default 1 | No se edita el entero; se editan `aprobadorIds` | Columna legado |
| H-W2 | Cadena Reu6 (`GrupoAprobacion`, nodos) | sí para piloto | Sí hay UI (grupos/escalas/simulador) | No huérfano; el problema es **doble modelo** (W1) |

---

## 3. Estado de «Productor-maestro»

### Qué hay hoy (no hay tabla `Productor`)

1. **Flag en maestros existentes**  
   - `Cliente.esProductor` (default `false`) — comentario Prisma D7.  
   - `Proveedor.esProductor` (default `false`).  
   - UI: checkbox en clientes (`ComercialPages`), ficha (`FichaContraparteModal`) y proveedores (`FichaProveedoresPage`). **No** hay menú «Productores».

2. **Lookup RUT** (`GET` comercial lookup)  
   Busca sociedad + clientes + proveedores. Devuelve `productor: Boolean(esProductor)` y un array `productores` que es **la unión filtrada** de esos mismos registros. **No** crea ni lee un maestro aparte.

3. **Tesorería › Anticipos productores**  
   Modelo `AnticipoProductor`: `productor` (**String obligatorio**), `rut` opcional, banco/forma/código/tipo docto, montos, calce. **Cero FK** a `Cliente` o `Proveedor`.

4. **Cuenta corriente**  
   Enum de aplicación `CLIENTE | PROVEEDOR | PRODUCTOR`. Al crear un anticipo, el servicio registra movimiento con:
   - `terceroTipo: 'PRODUCTOR'`
   - `terceroId: row.rut || row.productor` (RUT si hay, **si no el nombre libre**)
   - `terceroNombre: row.productor`

5. **Cuentas corrientes (UI)**  
   Filtro «productor» y subtítulo que habla de cliente/proveedor/productor. Los saldos PRODUCTOR **no** se agregan desde el flag `esProductor` del maestro: salen de movimientos cuyo `terceroTipo` ya es PRODUCTOR (anticipos/ajustes).

### Riesgo referencial (Anticipo × Tesorería × maestros)

| Riesgo | Detalle | Severidad |
|---|---|---|
| R-P1 | Anticipo no apunta a `Cliente`/`Proveedor`. Un mismo productor en ficha (`esProductor=true`) y en anticipo (texto) **no se cruzan** | Alta para aging/CC unificado |
| R-P2 | `terceroId` inestable: sin RUT = nombre; con RUT = RUT. Editar el RUT después **no** reagrupa historial. Dos anticipos «AGRICOLA X» sin RUT = misma cuenta; dos RUTs distintos del mismo holding = dos cuentas | Alta |
| R-P3 | Lookup puede marcar productor en **cliente y proveedor a la vez** (mismo RUT en ambas tablas). Anticipo no elige cuál. Pagos calzan contra `Proveedor` por razón social, no contra flag productor | Media |
| R-P4 | Inventar pantalla maestro Productor **rompería** D7/ficha y la skill: productor sigue siendo **atributo**. El hueco es de **integridad de tesorería**, no de un CRUD nuevo | — (restricción de diseño) |
| R-P5 | Modo demo (`fixtures-almahue-demo`) muestra anticipos con nombres que pueden no existir como cliente/proveedor | No usar demo como evidencia |

**Conclusión:** el producto trata al productor como **flag D7** en contraparte. Tesorería trata al productor como **texto de giro**. Mientras no haya pedido de maestro, el plan no es crear UI: es **atar** anticipo/CC a un `clienteId` y/o `proveedorId` existente (o exigir RUT que ya esté en uno de los dos maestros) **sin** nuevo tipo de ficha.

---

## 4. Plan de refactorización (solo propuesta)

Orden sugerido. No implementar hasta que se pida.

1. **Cartola: una puerta de entrada**  
   Quitar o deshabilitar el alta MockList sin `lineas`. Cabecera solo vía import. `usuarioCarga` = usuario JWT, no `'demo'`. Si se necesita carga manual, formulario de **líneas** (`fecha`, `referencia`, `glosa`, `monto`, `tipo`) que persista `MovimientoCartola`.

2. **Pago: FK de contraparte**  
   Select de `Proveedor` (y, si el beneficiario es productor-flag, el mismo maestro con `esProductor`). Enviar `proveedorId`. Dejar `beneficiario` denormalizado de lectura. `documentosCalce`: o bien ids de `DocumentoAging` / registro compra, o texto explícitamente «comentario» en UI.

3. **Conciliación**  
   O se genera desde una `cartolaId` (crear `MovimientoConciliacion` desde `MovimientoCartola`), o se retira «Nueva conciliación» y se deja la pantalla como **tablero** de cartolas. No persistir conteos inventados.

4. **Asiento vs dimensiones D9**  
   En cada línea: CC (ya hay), **área** y **elemento** si la cuenta lo exige. No capturar especie hasta que Prisma tenga el campo en el JSON/DTO (hoy `requiereEspecie` es muerto). Decidir si moneda/TC convierten a CLP o se documentan como metadato.

5. **Proforma**  
   Alta: o exigir asociación de labores en el mismo flujo, o recalcular `montoNeto` desde ingresos. **Solicitar aprobación:** dejar de leer `WorkflowConfig` como condición de negocio; solo grupos/escalas (pool legado = lista opcional de quién *puede* estar en un grupo, no la cadena).

6. **Workflows-admin**  
   En `/admin/aprobaciones`: ocultar CRUD de `WorkflowConfig` o marcarlo «solo pool de usuarios / no cadena». Dejar de escribir `aprobadores` Int. Motor de proformas: `hasGruposActivos` suficiente; no `match` por montoMin/Max del legado.

7. **Productor (sin UI nueva)**  
   - Al guardar anticipo: si hay RUT, resolver `Cliente` o `Proveedor` del tenant con ese RUT (y preferir `esProductor=true`). Guardar el id en columnas nuevas **opcionales** (`clienteId` / `proveedorId`) *cuando se autorice migración*; hasta entonces, **exigir RUT** y usar siempre RUT normalizado como `terceroId` de CC.  
   - No crear tabla `Productor`.  
   - Ajuste CC tipo PRODUCTOR: mismo criterio de id que el anticipo.

8. **QA**  
   Casos: import cartola → contabilizar → pago con `movId`; conciliación vacía no debe parecer mes cerrado; asiento con cuenta `requiereArea`; proforma BORRADOR → solicitar con solo grupos; anticipo sin RUT vs con RUT y flag en ficha; AdminConcepto re-login.

9. **Fuera de este plan**  
   Cobranza R4-18, SMTP, DTE real/GoSocket, certificación SII, maestro productor.

---

## 5. Relación con la auditoría principal

La auditoría de Comercial/Compras/Insumos dejó estos módulos fuera a propósito. Hallazgos de inventario/flete/DTE **no** se repiten aquí.  
Productor en Comercial (checkbox + lookup) **sí** es el único ancla válida; tesorería aún no la usa.
