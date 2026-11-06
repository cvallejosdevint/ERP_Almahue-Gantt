# Checklist de Pendientes, Conectores Inter-Módulos y Definiciones Post-Review
## Reunión de Revisión de Cambios con Cliente — Martes 03 de Noviembre de 2026 (AM + PM)

**Proyecto:** ERP Almahue  
**Fecha de Emisión y Cierre Técnico:** 04 de Noviembre de 2026  
**Estado de Implementación:** **14 / 14 ítems implementados (`100% COMPLETO`)**  
**Fuentes Primarias Analizadas:**
- **Grabaciones en `Screen Recordings`:**
  - Sesión AM (`Screen Recording 2026-11-03 115116.mp4` — `00:42:16`)
  - Sesión PM (`Screen Recording 2026-11-03 173934.mp4` — `02:38:24`)
- **Transcripción Primaria (Whisper `large-v3`):** [`transcripcion-2026-11-03-reunion.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md) ([`AM`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-am.md) y [`PM`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-pm.md))
- **Minuta Índice:** [`reunion-2026-11-03-cliente.md`](file:///e:/source/repos/Almahue/docs/reuniones/minutas/reunion-2026-11-03-cliente.md)
- **Participantes:** Cliente Almahue (**María José / MJ**, **Francisca / Fran**, **Lupe**, **Mario** `[desde PM 01:38:03]`) · Consultoría Devint (**Carlos**, **Sergio**).

> [!IMPORTANT]
> **Criterio de Contraste (`AGENTS.md`):** Todas las definiciones de este documento distinguen la voz mandataria del cliente (**MJ, Francisca, Mario, Lupe**) respecto de las hipótesis mostradas por Carlos/Sergio durante la demo, y documentan la implementación completa de todos los conectores entre módulos en `erp_back` y `erp_front`.

---

## 1. Definiciones del Cliente Post-Review (03/11/2026)

Tras revisar en vivo los cambios desarrollados a partir de las sesiones presenciales de la semana pasada (26–28 de octubre), el cliente estableció las siguientes **definiciones definitivas de operación y arquitectura entre módulos**:

### 1.1. Contratistas ↔ Libro de Compras ↔ Contabilidad
1. **Dirección única de asociación Factura ↔ Proforma(s) (Siempre desde Libro de Compras):**
   - **Definición de MJ (`PM [24:24–25:23]`, `[01:07:18]`, `[01:09:12]`, `[01:10:20]`, `[02:14:37–02:14:48]`):** La asociación de la factura recibida por GoSocket con una o más proformas **NO se realiza en el módulo de Contratistas**, sino **exclusivamente en `Compras › Libro de Compras`**.
   - **Aplicado en UI:** Se eliminó el botón *"Asociar factura"* en `Contratistas › Proformas` ([`ProformasContratistaNivel1Page.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx)) y *"Generar OC"* en [`ContratistasPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ContratistasPages.tsx). Al asociar la factura en el Libro de Compras, el folio de la factura se refleja automáticamente en la columna de `Contratistas › Proformas`.
2. **Dos pasos contables desacoplados (Cierre de Módulo vs Contabilización DTE):**
   - **Paso 1 — Traspaso y Cierre Mensual de Contratistas (`PM [23:52]`, `[01:03:05–01:04:40]`, `[02:14:27]`):**
     - **Regla MJ (`[01:03:15–01:03:33]`, `[02:14:27]`):** Al cierre mensual de Contratistas entran **TODAS las proformas aprobadas del período** (`DEFINITIVA`, `ENVIADA_CONTRATISTA`, `FACTURADA`), **tengan o no factura asociada todavía**, ya que el objetivo del cierre de módulo es reconocer el gasto del mes.
     - **Asiento Paso 1:** **Debe** = `6-1-01-01-002 · Mano de Obra Contratistas` **agrupado por Centro de Costo** vs **Haber** = `2-1-08-02-003 · Facturas por Recibir Contratistas` **abierto por Auxiliar RUT de cada contratista** (`PM [23:52]`, `[58:53]`).
     - En la pantalla de Traspaso y Cierre se muestra la tarjeta **"Pendientes de asociación"** (`aprobada(s) sin factura en Compras`) (`PM [01:10:49–01:10:59]`) y el desglose en árbol **Labor → Centro de Costo → Proforma**.
   - **Paso 2 — Contabilización de Factura en Libro de Compras (`PM [24:24–25:23]`, `[58:53–59:02]`):**
     - En el Libro de Compras se asocia el DTE a la(s) proforma(s) aprobada(s) exigiendo **cobertura 100% exacta del neto** (`Math.abs(montoSeleccionado - netoFactura) < 1`) y habilitando el botón **«Notificar diferencia al creador de la proforma»** cuando hay descuadre.
     - Al pulsar **"Contabilizar"** en el Libro de Compras, se genera el asiento que netea la provisión: **Debe** = `Facturas por Recibir Contratistas` (`2-1-08-02-003`, neto) + `IVA Crédito Fiscal` vs **Haber** = `Proveedores Nacionales` (`2-1-01-01-001`, bruto) con Auxiliar RUT.
3. **Cierre de Módulo vs Cierre Contable y Efecto del Doble VºBº en Período Cerrado:**
   - **Sin botón masivo "Reabrir" (`AM [00:50]`, `PM [28:13]`, `[30:35–31:06]`):** Ningún módulo cerrado se reabre masivamente; toda excepción nace seleccionando **una o varias proformas específicas** (`PM [02:21:56]`) con **Motivo + PIN**.
   - **Doble Visto Bueno (`PM [31:48–33:22]`, `[02:19:03–02:19:48]`):** Requiere aprobación con PIN de **1º Jefatura/Admin de Contratistas** y **2º Contabilidad** (en `/contabilidad/reversas`).
   - **Definición de MJ sobre el efecto post-doble VºBº cuando el período contable está cerrado (`PM [02:20:32–02:26:42]`):** Cuando el período contable ya está cerrado, la modificación autorizada sobre la proforma (ej. corregir labor, cuartel o cantidades) **actualiza la Reportería de Gestión de Contratistas (vista tabla y vista árbol Labor → CC → Proforma) y deja la trazabilidad Antes/Después en el Log de Auditoría y en Solicitudes de Reversa**, sin alterar ni reabrir el asiento contable histórico ya cerrado.

### 1.2. Insumos / Bodega ↔ Compras (OC Madre / Hijas / Guías) ↔ Contabilidad
1. **Separación conceptual: Recepción de Compras (Existencia) ≠ Cierre Mensual de Bodega (Consumo) (`PM [01:31:16–01:49:42]`):**
   - La recepción de guías de compra alimenta la **Existencia (activo en bodega)**. El **Cierre de Bodega mensual** contabiliza **lo CONSUMIDO en el mes** contra las cuentas de gasto/costo.
2. **Dos flujos de Consumo que alimentan el Cierre de Bodega:**
   - **Flujo A — Agrícola / Campo (`Órdenes de Aplicación`, `PM [02:06:20–02:11:36]`):**
     - Rebaja stock de agroquímicos/fertilizantes de la bodega agrícola validando **stock disponible > 0**, pasando por **Cadena de Aprobación de Insumos** con PIN e imputando en el Cierre de Bodega contra **"Consumo de materiales"**.
   - **Flujo B — Exportadora / Packing (`Traspaso entre Bodegas DTE 52` + `Recetas` + `Producción Mensual`, `PM [01:38:03–01:57:27]`):**
     - Los materiales de embalaje se envían a *Bodega Packing* mediante un **Traspaso entre Bodegas** que emite una **Guía de Despacho electrónica (DTE 52 traslado interno, no venta)** desde `Insumos › Libro de Guías (pestaña Guías Emitidas)`.
     - El mantenedor de **Recetas de Packing** (1 a 1 y plantilla Excel) y la pestaña **Producción Mensual Packing** calculan el consumo total de materiales por cajas producidas, rebajando el stock de *Bodega Packing* e imputando en el Cierre de Bodega contra **"Materiales de exportación"**.

---

## 2. Estado de Conectores entre Módulos (`100% Operativos`)

| # | Conector Inter-Módulos | Estado en Código (`erp_back` / `erp_front`) | Implementación Aplicada |
|---|---|---|---|
| **C-1** | **Proformas (`Contratistas`) ↔ Asociar Factura (`Libro de Compras`)** | **COMPLETO** | Eliminado botón *"Asociar factura"* en Contratistas; exigida cobertura **100% exacta** (`Math.abs(montoSeleccionado - netoFactura) < 1`) y botón **"Notificar diferencia al creador de la proforma"** en [`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx). |
| **C-2** | **Traspaso/Cierre (`Contratistas`) ↔ Provisión `2-1-08-02-003` (`Contabilidad`) ↔ Neteo (`Libro de Compras`)** | **COMPLETO** | Corregido `getCierreTraspaso` en [`contratistas.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/contratistas.service.ts) para usar `ESTADOS_PROFORMA_TRASPASO`; agregada tarjeta **"Pendientes de asociación"**, nombres completos de cuentas y vista en árbol (**Labor → CC → Proforma**) en [`ContratistasPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ContratistasPages.tsx) y [`ReporteContratistasIngresoPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ReporteContratistasIngresoPage.tsx). |
| **C-3** | **Reversa de Proformas (`Contratistas`) ↔ Bandeja Doble VºBº (`Contabilidad`) ↔ Reportería y Auditoría** | **COMPLETO** | Selección de `1..N` proformas (`proformaIds`), desbloqueo puntual en `assertPeriodoOperable`, edición de Labor/Cuartel/Cantidad/Precio en `ProformaItemsCentros`, snapshot **Antes / Después** en [`solicitud-reversa-edicion.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/solicitud-reversa-edicion.service.ts) y [`SolicitudesReversaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/SolicitudesReversaPage.tsx) sin alterar el asiento contable cerrado. |
| **C-4** | **OC Madre (`Insumos`) ↔ Recepción Guía (`Libro de Guías`) ↔ OC Hijas (`.1`, `.2`) ↔ `Libro de Compras`** | **COMPLETO** | Filtro exclusivo `tipo: 'INSUMOS'` en [`insumos.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/insumos/insumos.service.ts); selección múltiple con checkboxes de N OC Hijas en [`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx); acordeón desplegable de OC Hijas y columnas separadas **Estado Aprobación** / **Estado Recepción** en [`OrdenesInsumosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesInsumosPage.tsx). |
| **C-5** | **Consumo Campo (`Órdenes de Aplicación`) + Consumo Packing (`Traspaso DTE 52` + `Recetas` + `Producción`) ↔ `Cierre de Bodega`** | **COMPLETO** | Implementado centro de 3 pestañas en [`OrdenesAplicacionPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesAplicacionPage.tsx), pestaña `Guías Emitidas (DTE 52)` en [`GuiasInsumosRecibidasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx) y Cierre de Bodega por Consumos + Parametrización en [`CierreBodegaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/CierreBodegaPage.tsx). |
| **C-6** | **Compra de Activo Fijo (`OC` / `Activo Fijo`) ↔ `Libro de Compras`** | **COMPLETO** | Tipo `ACTIVO_FIJO` en [`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx), vínculo en [`AltaActivoFijoDialog.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/AltaActivoFijoDialog.tsx), pestaña **"Activos fijos"** en [`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx) y pestaña **Parametrización** en [`ActivoFijoPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoPages.tsx). |
| **C-7** | **Perfiles de Usuario (`Usuarios`) ↔ Grupos y Escalas (`Reglas de Aprobación`)** | **COMPLETO** | Eliminado filtro restrictivo por rol en [`WorkflowAprobacionesPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/admin/WorkflowAprobacionesPage.tsx) mostrando **Rol + Grupo actual**, y validación de secuencia estricta + **Suplencia activa** en [`workflowAprobacion.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/lib/workflowAprobacion.ts). |

---

## 3. Checklist Detallado — Reunión 03/11/2026 (`14 / 14 Completados`)

### Bloque 1: Contratistas, Proformas y Cierre/Reversa
- [x] **CHK-01 [P0] Eliminar botón "Asociar factura" / "Generar OC" en `Contratistas › Proformas`** (`PM [01:10:20]`, `[02:14:37]`) — **COMPLETO**
- [x] **CHK-02 [P0] Proformas: Iniciar filtro de período en "Todos" y mostrar `—` en envío si la proforma aún no está aprobada** (`AM [05:49–08:30]`, `PM [11:46]`, `[50:42]`) — **COMPLETO**
- [x] **CHK-03 [P0] Traspaso y Cierre de Contratistas: Incluir todas las proformas aprobadas, tarjeta "Pendientes de asociación", nombre de cuenta contable y vista en árbol (Labor → CC → Proforma)** (`PM [22:28]`, `[39:07–41:46]`, `[01:03:15]`, `[01:10:49]`, `[02:14:27]`) — **COMPLETO**
- [x] **CHK-04 [P0] Reapertura / Reversa de Proformas en Período Cerrado vs Abierto (Doble VºBº, multi-proforma, edición de Labor/Cuartel/Cantidad, Reportería Árbol y Auditoría Antes/Después sin alterar asiento cerrado)** (`AM [00:35–03:46]`, `PM [27:36–38:06]`, `[02:15:12–02:26:42]`) — **COMPLETO**

### Bloque 2: Compras y Libro de Compras
- [x] **CHK-05 [P0] Modal "Asociar factura" en Libro de Compras: Quitar pestaña "Guías recibidas", agregar pestaña "Activos fijos", exigir cobertura 100% en Proformas y permitir múltiples OC Hijas con checkboxes** (`PM [16:50]`, `[20:11–20:46]`, `[25:47]`, `[01:06:17–01:08:18]`, `[02:02:32–02:04:24]`) — **COMPLETO**
- [x] **CHK-06 [P1] Libro de Compras: Doble etiqueta en documento asociado (`Proforma/OC` + `Contabilizada / Pendiente contabilizar`) y botón de notificación de diferencia al creador de la proforma** (`PM [14:17–15:58]`, `[26:06–27:00]`) — **COMPLETO**

### Bloque 3: Insumos, Bodega, Packing y Guías
- [x] **CHK-07 [P0] Recepción de Guías en Insumos: Filtrar solo OCs `INSUMOS`, eliminar botón "Crear producto" y abrir "Pedir creación" en un modal independiente** (`PM [01:17:55–01:20:27]`) — **COMPLETO**
- [x] **CHK-08 [P1] Ingreso Manual de Guía en Insumos: Selector de Proveedor con búsqueda por RUT y campos de Tipo de Despacho / Traslado** (`PM [01:14:39–01:15:36]`) — **COMPLETO**
- [x] **CHK-09 [P1] Grilla `Órdenes de Insumos`: Desplegar OC Hijas (`.1`, `.2`) en acordeón bajo la OC Madre y separar columnas "Estado Aprobación" y "Estado Recepción"** (`PM [01:23:43–01:30:54]`) — **COMPLETO**
- [x] **CHK-10 [P1] Implementar `Órdenes de Aplicación` (Consumo Agrícola) con validación de stock > 0 y Cadena de Aprobación de Insumos** (`PM [01:34:01–01:36:14]`, `[02:06:20–02:09:34]`) — **COMPLETO**
- [x] **CHK-11 [P1] Flujo Packing en Insumos: `Libro de Guías` con 2 pestañas (`Guías Recibidas` / `Guías Emitidas` DTE 52 por traspaso a Bodega Packing), Mantenedor de `Recetas` (1 a 1 y Excel) y `Producción Mensual`** (`PM [01:38:03–02:01:09]`) — **COMPLETO**
- [x] **CHK-12 [P1] Cierre Mensual de Bodega centrado en Consumos (Aplicación Campo + Producción Packing), eliminación de botón "Reabrir cierre de bodega" y pestaña "Parametrización" por módulo (Contratistas, Insumos, Activo Fijo)** (`PM [01:31:16–01:36:14]`, `[02:10:00–02:13:30]`) — **COMPLETO**

### Bloque 4: Administración, Reglas de Aprobación y Usuarios
- [x] **CHK-13 [P0] Reglas de Aprobación: Permitir agregar cualquier perfil de usuario a un Grupo y mostrar Rol + Grupo actual en el listado** (`PM [01:24–07:47]`) — **COMPLETO**
- [x] **CHK-14 [P1] Bandejas de Aprobación: Garantizar bloqueo estricto de secuencia (escalón superior no aprueba antes que el inferior) y salto automático por Suplencia de vacaciones** (`PM [52:30–54:28]`) — **COMPLETO**
