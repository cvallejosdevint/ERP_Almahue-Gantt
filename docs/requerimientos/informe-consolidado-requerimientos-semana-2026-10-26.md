# Informe Consolidado de Requerimientos y Validación en Código por Módulos
## Sesiones Presenciales y Remotas: Lunes 26, Martes 27 y Miércoles 28 de Octubre + Correo MJ 29/10/2026

**Proyecto:** ERP Almahue  
**Fecha de Actualización de Auditoría y Cierre Técnico:** 04 de Noviembre de 2026  
**Fuentes Primarias Analizadas:**
1. **Lunes 26/10:** Apuntes [`revision en cliente.txt`](file:///C:/Users/c/Desktop/revision%20en%20cliente.txt), [`transcripcion-2026-10-26-presencial.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-10-26-presencial.md) (AM, 01:24:40) y [`transcripcion-2026-10-26-presencial-tarde.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-10-26-presencial-tarde.md) (PM, 01:54:00). Detalle ampliado en [`14-informe-auditoria-lunes-2026-10-26.md`](file:///e:/source/repos/Almahue/docs/reuniones/analisis/14-informe-auditoria-lunes-2026-10-26.md).
2. **Martes 27/10:** [`transcripcion-2026-10-27-reunion.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-10-27-reunion.md) (AM, 01:18:10) y [`transcripcion-2026-10-27-reunion-tarde.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-10-27-reunion-tarde.md) (PM, 01:47:50).
3. **Miércoles 28/10:** [`transcripcion-2026-10-28-reunion.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-10-28-reunion.md) (Sesión Integral, 03:04:06).
4. **Requerimientos Extraordinarios Correo MJ (29/10/2026)** y **Cierre Técnico del 04/11/2026 en `erp_back` y `erp_front`**.

---

## 1. Resumen Ejecutivo y Matriz Global de Estado (Al 04/11/2026)

| Módulo Operativo | Total Puntos | Completo | Parcial | Faltante / Externo | % Completitud ERP |
|---|:---:|:---:|:---:|:---:|:---:|
| **1. Contabilidad, Plan de Cuentas y Reportes** | 12 | 12 | 0 | 0 | 100.0% |
| **2. Compras, Proveedores y Notas de Cobro** | 11 | 11 | 0 | 0 | 100.0% |
| **3. Contratistas Agrícolas** | 7 | 7 | 0 | 0 | 100.0% |
| **4. Insumos y Bodega** | 5 | 5 | 0 | 0 | 100.0% |
| **5. Activos Fijos** | 3 | 3 | 0 | 0 | 100.0% |
| **6. Tesorería, Bancos y Contrapartes** | 6 | 6 | 0 | 0 | 100.0% |
| **7. Comercial, Packing y Exportación (Comex)** | 4 | 3 | 0 | 1 *(Sistema externo)* | 100.0% *(en alcance ERP)* |
| **SUBTOTAL REUNIONES 26–28 OCTUBRE** | **48** | **47** | **0** | **1 *(Externo)*** | **97.9% (100% ERP)** |
| **8. Requerimientos Extraordinarios Correo MJ (29/10)** | 7 | 7 | 0 | 0 | 100.0% |
| **TOTAL GENERAL AUDITADO EN CÓDIGO** | **55** | **54** | **0** | **1 *(Externo)*** | **98.2% (100% ERP)** |

---

## 2. Detalle de Requerimientos Auditados por Módulo

### Módulo 1: Contabilidad, Plan de Cuentas y Reportes Financieros (12 Completos)

- **1.1 Selector Multi-Empresa al Crear Usuarios (A-1)** — `COMPLETO` ([`EmpresaSelector.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/components/layout/EmpresaSelector.tsx)).
- **1.2 Asociación N:N de Dimensiones por Cuenta (Plan de Cuentas) (P-1)** — `COMPLETO` ([`CuentaAsociadosPanel.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/CuentaAsociadosPanel.tsx), [`PlanCuentasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx)).
- **1.3 Matriz de Plan de Cuentas con Scroll Bidireccional (P-8)** — `COMPLETO` ([`PlanCuentasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx) + columnas `AUX` y `REF`).
- **1.4 Balance de 8 Columnas Acumulativo Anual (K-15)** — `COMPLETO` ([`Balance8ColumnasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/Balance8ColumnasPage.tsx)).
- **1.5 Estado de Resultados Mensual vs Situación Financiera al 31/12 (K-16, K-18, K-19)** — `COMPLETO` ([`EstadosFinancierosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/EstadosFinancierosPage.tsx), [`CierreAnualModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/CierreAnualModal.tsx)).
- **1.6 Carga Masiva Restrictiva Tipo Agrosoft (K-20)** — `COMPLETO`
  - **Evidencia:** Validación y persistencia atómica **todo-o-nada** (`this.prisma.$transaction`) en [`contabilidad.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contabilidad/contabilidad.service.ts#L1252-L1388) y botón **«Descargar plantilla Agrosoft (.xlsx)»** en [`AsientosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/AsientosPage.tsx#L454-L565).
- **1.7 Tipos de Comprobante Contable y Nomenclatura (K-3, K-6)** — `COMPLETO` ([`tipo-comprobante.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/tipo-comprobante.ts)).
- **1.8 Detalle de Asiento en 3 Columnas, Glosas y Adjuntos (K-4, K-5)** — `COMPLETO` ([`AsientosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/AsientosPage.tsx#L726-L896)).
- **1.9 Protocolo de Reversas y Comprobantes de Ajuste (A-3)** — `COMPLETO` ([`SolicitudesReversaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/SolicitudesReversaPage.tsx) y [`solicitud-reversa-edicion.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/solicitud-reversa-edicion.service.ts)).
- **1.10 Auditoría e Historial Distribuida por Módulo (A-2)** — `COMPLETO` ([`AuditoriaContabilidadPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/AuditoriaContabilidadPage.tsx), [`AuditoriaContratistasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/AuditoriaContratistasPage.tsx), [`AuditoriaInsumosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/AuditoriaInsumosPage.tsx), [`ActivoFijoHistorialPanel.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoHistorialPanel.tsx)).
- **1.11 Libro Mayor y Diario: Filtros de Periodo y Arrastre Interanual (K-12, K-13, K-14)** — `COMPLETO` ([`LibroDiarioMayorPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/LibroDiarioMayorPages.tsx), [`IndicadoresBcPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/pages/parametrizacion/IndicadoresBcPage.tsx)).
- **1.12 Presupuesto: Alertas Porcentuales y Agrupación por Departamento (K-10, K-11)** — `COMPLETO` ([`PresupuestosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/presupuestos/PresupuestosPage.tsx)).

---

### Módulo 2: Compras, Proveedores y Notas de Cobro (11 Completos)

- **2.1 Jerarquía en Cascada en Orden de Compra (C-1)** — `COMPLETO` ([`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx)).
- **2.2 Solicitud al Administrador de Dimensiones Faltantes (C-2)** — `COMPLETO` ([`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx)).
- **2.3 Múltiples Líneas de Imputación Contable en OC (C-3)** — `COMPLETO` ([`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx)).
- **2.4 Vista de Detalle de OC en Árbol Desplegable (C-4)** — `COMPLETO` ([`OcDesgloseContableTree.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OcDesgloseContableTree.tsx)).
- **2.5 Plantilla PDF Oficial al Proveedor sin Dimensiones Contables (C-5)** — `COMPLETO` ([`compras-oc-helpers.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/compras-oc-helpers.ts)).
- **2.6 Notas de Cobro — Gasto Directo (Asoex / Exentos) (P-6)** — `COMPLETO` ([`NotasCobroPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/NotasCobroPage.tsx)).
- **2.7 Notas de Cobro — Embarcadores y Carga Masiva Excel (P-7)** — `COMPLETO` ([`NotasCobroPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/NotasCobroPage.tsx), [`notas-cobro.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/compras/notas-cobro.service.ts)).
- **2.8 Flujo de Guardado y Anulación Autorizada con PIN en Notas de Cobro** — `COMPLETO` ([`NotasCobroPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/NotasCobroPage.tsx), [`notas-cobro.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/compras/notas-cobro.service.ts)).
- **2.9 Fecha de Vencimiento Automática (+30 días desde Emisión SII)** — `COMPLETO` ([`libro-compras-tipo.util.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/libro-compras-tipo.util.ts)).
- **2.10 Boletas de Honorarios: Tipos 1001/1002/1003 y Retención Anual (P-5)** — `COMPLETO` ([`RegistroBoletaHonorariosModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/RegistroBoletaHonorariosModal.tsx)).
- **2.11 Modal Universal de Factura PDF con Botón "Ir a Documento" y Columna Relacionados** — `COMPLETO` ([`VisorDocumentoPdfModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/components/trazabilidad/VisorDocumentoPdfModal.tsx)).

---

### Módulo 3: Contratistas Agrícolas (7 Completos)

- **3.1 Segregación Estricta de Roles: Abastecimiento vs Contabilidad** — `COMPLETO` ([`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx)).
- **3.2 Inversión de Jerarquía: Actividad $\rightarrow$ Labores (CTR-2)** — `COMPLETO` ([`AsociacionLaboresPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/AsociacionLaboresPage.tsx)).
- **3.3 Ingreso Diario Ágil y Aprobación en Proforma (CTR-3)** — `COMPLETO` ([`IngresoLaborDiarioMasivoPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/IngresoLaborDiarioMasivoPage.tsx), [`ProformasContratistaNivel1Page.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx)).
- **3.4 Pantalla de Cierre con Bloques de Resumen y Pendientes de Asociación (CTR-4)** — `COMPLETO` ([`TraspasoContratistasResumenPanel.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/TraspasoContratistasResumenPanel.tsx)).
- **3.5 Asiento de Cierre: Gasto Agrupado por CC y Auxiliar en Provisión (CTR-5)** — `COMPLETO` ([`contratistas.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/contratistas.service.ts)).
- **3.6 Protocolo de Reversa y Reapertura de Proforma en Período Abierto y Cerrado (CTR-6)** — `COMPLETO`
  - **Evidencia:** Selección de `1..N` proformas, Doble VºBº (Contratistas + Contabilidad), desbloqueo puntual de `assertPeriodoOperable`, edición de Labor/Cuartel/Cantidad/Precio en `ProformaItemsCentros`, actualización de Reportería en Árbol (`Labor → CC → Proforma`), snapshot **Antes / Después** en Auditoría y endpoint `POST contratistas/traspaso-cierre/:periodo/recentralizar` en [`contratistas.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/contratistas.service.ts) y [`solicitud-reversa-edicion.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/solicitud-reversa-edicion.service.ts).
- **3.7 Notificaciones desde Listados de Proformas (CTR-7)** — `COMPLETO` ([`ProformaNotificarModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformaNotificarModal.tsx)).

---

### Módulo 4: Insumos y Bodega (5 Completos)

- **4.1 Guías / Órdenes de Aplicación de Campo, Recetas y Producción Packing** — `COMPLETO`
  - **Evidencia:** [`OrdenesAplicacionPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesAplicacionPage.tsx) con validación obligatoria de `stock > 0`, Cadena de Aprobación de Insumos con PIN, rebaja física de stock, mantenedor de Recetas de Packing (1 a 1 y Excel) y Producción Mensual Packing.
- **4.2 Prohibición Estricta de Stock Negativo** — `COMPLETO` ([`StockMantenedorPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/StockMantenedorPage.tsx)).
- **4.3 Bodega por Empresa y Distribución en Maestro de Artículos** — `COMPLETO` ([`InsumoStockDistribucionPanel.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/InsumoStockDistribucionPanel.tsx)).
- **4.4 Ingreso Respaldado por Guía de Despacho Física y OC Hijas en Acordeón** — `COMPLETO` ([`GuiasInsumosRecibidasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx), [`OrdenesInsumosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesInsumosPage.tsx)).
- **4.5 Tipos de Movimientos de Bodega, Devolución con Guía Original y Cierre por Consumos** — `COMPLETO` ([`InsumosPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/InsumosPages.tsx), [`CierreBodegaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/CierreBodegaPage.tsx)).

---

### Módulo 5: Activos Fijos (3 Completos)

- **5.1 Nacimiento Obligatorio desde Orden de Compra (Mandato Agustín)** — `COMPLETO` (tipo `ACTIVO_FIJO` en [`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx), selector obligatorio de OC aprobada de origen en [`AltaActivoFijoDialog.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/AltaActivoFijoDialog.tsx) y pestaña `Activos fijos` en [`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx)).
- **5.2 Gráfico Consolidado General de Depreciación Mensual** — `COMPLETO` (`GraficoConsolidadoDepreciacionSection` en [`ActivoFijoPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoPages.tsx)).
- **5.3 Depreciación Mensual, Agrupación por Familia, Parametrización e Historial de Activos Fijos** — `COMPLETO` ([`ActivoFijoPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoPages.tsx), [`ActivoFijoHistorialPanel.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoHistorialPanel.tsx)).

---

### Módulo 6: Tesorería, Bancos y Contrapartes (6 Completos)

- **6.1 Parametrización Bancaria Multi-cuenta y Moneda (P-3b)** — `COMPLETO` ([`BancosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/pages/parametrizacion/BancosPage.tsx)).
- **6.2 Carga Periódica de Cartolas Bancarias sin Duplicados (TES-1)** — `COMPLETO` (deduplicación automática por llave compuesta `(fecha, monto, abs(monto), referencia || glosa)` en [`tesoreria.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/tesoreria/tesoreria.service.ts#L2012-L2155)).
- **6.3 Nómina Semanal de Pagos y Asignación de Compromisos** — `COMPLETO` ([`NominasAgingPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/NominasAgingPage.tsx)).
- **6.4 Filtro Diferenciador de Proveedores vs Productores** — `COMPLETO` ([`CuentasCorrientesPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CuentasCorrientesPage.tsx), [`CompromisosAnticiposPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CompromisosAnticiposPage.tsx), [`NominasAgingPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/NominasAgingPage.tsx#L656-L680)).
- **6.5 Gestión de Anticipos a Productores y Flujo de Caja Proyectado** — `COMPLETO` ([`AnticiposProductoresPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/AnticiposProductoresPage.tsx), [`FlujoCajaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/FlujoCajaPage.tsx)).
- **6.6 Estado de Cuenta Unificado por RUT y Compensación** — `COMPLETO` ([`CuentasCorrientesPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CuentasCorrientesPage.tsx)).

---

### Módulo 7: Comercial, Packing, Logística y Exportación (Comex) (3 Completos · 1 Sistema Externo)

- **7.1 Optimización de Contenedores y Pallets (Cajas Rojas vs Negras)** — `SISTEMA EXTERNO DE PACKING` (en el ERP se integraron las **Recetas de Packing** y la **Producción Mensual** para el consumo contable de materiales en [`OrdenesAplicacionPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesAplicacionPage.tsx)).
- **7.2 Importador Masivo de Planilla COMEX (`ACTUALIZABLE COMEX.xlsx`)** — `COMPLETO` ([`ComexImportPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/ComexImportPage.tsx)).
- **7.3 Prevalidación XML DTE, Código `<VlrCodigo>` y Selector de Unidad en OV** — `COMPLETO` ([`linea-detalle-dte.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/comercial/linea-detalle-dte.ts), [`canonical-builder.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/billing/canonical-builder.ts), [`DtePdfPreviewModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/DtePdfPreviewModal.tsx) y selector de unidad en [`ComercialPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/ComercialPages.tsx#L41-L73)).
- **7.4 Emisión de Guías de Despacho Electrónicas (Resolución 154)** — `COMPLETO` ([`GuiasDespachoPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/GuiasDespachoPage.tsx)).

---

### Módulo 8: Requerimientos Extraordinarios Incorporados (Correo María Jesús - 29/10/2026) (7 Completos)

- **E-1 (4.1) Compromisos de Anticipo en Flujo de Caja sin Asiento Contable (Punto 2 MJ)** — `COMPLETO` ([`CompromisosAnticiposPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CompromisosAnticiposPage.tsx)).
- **E-2 (4.2) Cálculo de Vencimientos Atado a Emisión Electrónica SII (Punto 3 MJ)** — `COMPLETO` ([`libro-compras-tipo.util.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/libro-compras-tipo.util.ts)).
- **E-3 (4.3) Facturas Bimoneda y Desglose de Aging con IVA al día 20 (F29) (Punto 4 MJ)** — `COMPLETO` ([`aging-sync.util.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/tesoreria/aging-sync.util.ts)).
- **E-4 (4.4) Importador Masivo de Planilla COMEX `ACTUALIZABLE COMEX.xlsx` (Punto 5 MJ)** — `COMPLETO` ([`ComexImportPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/ComexImportPage.tsx)).
- **E-5 (4.5) Columna 'Relacionados' con Badge Numérico (1-9, 9+) y Visor Universal de Documentos** — `COMPLETO` ([`VisorDocumentoPdfModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/components/trazabilidad/VisorDocumentoPdfModal.tsx)).
- **E-6 (4.6) Asociación Múltiple (N Proformas → 1 Factura) y Barra de Porcentaje de Cobertura** — `COMPLETO` ([`AsociarOcRegistroCompraModal.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx)).
- **E-7 (4.7) Filtro Rápido por Módulo, Doble Candado de Cierre y Reapertura por Excepción** — `COMPLETO` ([`SolicitudesReversaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/SolicitudesReversaPage.tsx), [`solicitud-reversa-edicion.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/solicitud-reversa-edicion.service.ts), [`contratistas.service.ts`](file:///e:/source/repos/Almahue/ERP/erp_back/src/modules/contratistas/contratistas.service.ts)).
