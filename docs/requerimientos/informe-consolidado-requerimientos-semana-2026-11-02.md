# Informe Consolidado de Requerimientos y Validación en Código por Módulos
## Semana del 02 al 07 de Noviembre de 2026 (Sesiones 03/11, 04/11, 05/11 y 06/11)

**Proyecto:** ERP Almahue  
**Fecha de Emisión y Cierre Técnico:** 07 de Noviembre de 2026  
**Fuentes Primarias Analizadas:**
1. **Martes 03/11:** Transcripción [`transcripcion-2026-11-03-reunion.md`](file:///e:/source/repos/Almahue/docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md), Minuta [`reunion-2026-11-03-cliente.md`](file:///e:/source/repos/Almahue/docs/reuniones/minutas/reunion-2026-11-03-cliente.md), visor interactivo [`reunion-2026-11-03-cliente-interactiva.html`](file:///e:/source/repos/Almahue/docs/reuniones/minutas/reunion-2026-11-03-cliente-interactiva.html) y acuerdos diarios [`2026-11-03-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-03-acuerdos.md).
2. **Miércoles 04/11:** Matriz de normalización [`matriz-ui-normalizacion-2026-11-04.md`](file:///e:/source/repos/Almahue/docs/requerimientos/matriz-ui-normalizacion-2026-11-04.md), auditoría [`auditoria-click-detalle-vs-edicion-2026-11-04.md`](file:///e:/source/repos/Almahue/docs/requerimientos/auditoria-click-detalle-vs-edicion-2026-11-04.md) y acuerdos [`2026-11-04-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-04-acuerdos.md).
3. **Jueves 05/11:** Sala Cliente: Recetas, Topes de Aprobación y Reglas de Negocio [`auditoria-acuerdos-sistema-2026-11-05.md`](file:///e:/source/repos/Almahue/docs/requerimientos/auditoria-acuerdos-sistema-2026-11-05.md), checklist [`checklist-pendientes-acuerdos-2026-11-05.md`](file:///e:/source/repos/Almahue/docs/requerimientos/checklist-pendientes-acuerdos-2026-11-05.md), matriz [`matriz-acuerdos-por-dia-2026-11-05.md`](file:///e:/source/repos/Almahue/docs/requerimientos/matriz-acuerdos-por-dia-2026-11-05.md) y acuerdos [`2026-11-05-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-05-acuerdos.md).
4. **Viernes 06 y Sábado 07/11:** Sesión de Consolidación de Sala, Esquema de Ramas Dinámicas, Unificación Conceptual (Rango de Autoridad vs Nivel de Rama), Resiliencia 404 en Modo Real y build de producción [`2026-11-06-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-06-acuerdos.md).

---

## 1. Resumen Ejecutivo y Matriz Global de Estado (Semana 02–07 Noviembre)

| Módulo Operativo | Total Puntos | Completo | Parcial | Faltante / Externo | % Cumplimiento |
|---|:---:|:---:|:---:|:---:|:---:|
| **1. Administración, Roles y Esquema de Ramas** | 12 | 12 | 0 | 0 | 100.0% |
| **2. Compras, Órdenes de Compra y Aprobaciones** | 8 | 8 | 0 | 0 | 100.0% |
| **3. Insumos, Bodegas y Recetas de Embalaje** | 7 | 7 | 0 | 0 | 100.0% |
| **4. Contabilidad, Asientos y Presupuestos** | 6 | 6 | 0 | 0 | 100.0% |
| **5. Activos Fijos** | 3 | 3 | 0 | 0 | 100.0% |
| **6. Tesorería y Bancos** | 4 | 4 | 0 | 0 | 100.0% |
| **7. Contratistas y Proformas** | 4 | 4 | 0 | 0 | 100.0% |
| **TOTAL GENERAL AUDITADO EN CÓDIGO** | **44** | **44** | **0** | **0** | **100.0%** |

---

## 2. Detalle de Requerimientos Auditados por Módulo

### Módulo 1: Administración, Roles y Esquema de Ramas Jerárquicas (12 Completos)

- **1.1 Unificación Conceptual de Jerarquía (Rango 1–4 vs Nivel de Ramas 1–3+)** — `COMPLETO`
  - Se eliminó la ambigüedad donde cargos directivos tenían números altos que colisionaban con los estratos de las ramas.
  - **Rango de Autoridad (Decisión / Personas)**: Rango 1 = Gerencia General (decisión final ilimitada), Rango 2 = Gerencias de Área, Rango 3 = Jefaturas Operativas (3.1/3.2), Rango 4 = Asistentes/Emisores (solo digitan). **El 1 es el valor más importante y desciende hacia abajo**.
  - **Nivel de Rama (Ubicación & Herencia)**: Nivel 1 = Dirección General (raíz), Nivel 2 = Ramas Operativas Principales en paralelo horizontal (Agrícola, Packing, Administración, Contratistas), Nivel 3+ = Sub-ramas dependientes que van abajo y heredan ámbito. **El 1 es el valor más importante**.
  - Evidencia: [`domain.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/types/domain.ts), [`EsquemaRamasAprobacion.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/components/aprobaciones/EsquemaRamasAprobacion.tsx#L40-L95).
- **1.2 Eliminación Total de Rastro de Configuración Anterior** — `COMPLETO`
  - Se removieron de backend y frontend las barras obsoletas (botones "Niveles", "Árbol de Grupos", inputs huérfanos y slide panels de 20 grupos anteriores). La vista queda 100% montada sobre `EsquemaRamasAprobacion`.
- **1.3 Creación Dinámica de Ramas y Asignación de Nivel de Rama** — `COMPLETO`
  - Modal interactivo con botón `+ Nueva Rama` para crear ramas ilimitadas (Agrícola, Packing, Administración, Contratistas, Bodega, Insumos, etc.) con selección de Nivel y módulos asignados.
- **1.4 Nombres de Eslabones 100% Configurables** — `COMPLETO`
  - Los nombres de cada eslabón y cargo no son predefinidos sino totalmente configurables por el usuario (ej. Jefatura de Riego, Jefatura Fundos Norte, etc.).
- **1.5 Modalidad de Aprobación en Reglas: Paralelo OR** — `COMPLETO`
  - Despliegue horizontal en paralelo de cargos hermanos (Fundos Norte y Sur); cualquiera visa para no frenar la faena.
- **1.6 Modalidad de Aprobación en Reglas: Decisión Unánime AND** — `COMPLETO`
  - Cargos agrupados en bloque vinculante (Planta + Calidad en empaque); requiere la firma obligatoria de todos.
- **1.7 Modalidad de Aprobación en Reglas: Escalas Secuenciales 3.1 ➔ 3.2** — `COMPLETO`
  - Subrangos decimales por tramos de monto (Subjefe de Riego 3.1 ➔ Jefe de Riego 3.2) antes de subir a Gerencia.
- **1.8 Integración de Usuarios con Cargo en Árbol Jerárquico** — `COMPLETO`
  - En [`UsuariosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/pages/parametrizacion/UsuariosPage.tsx), se visualiza la columna Cargo en Árbol con Rango y Rama, heredando automáticamente topes y línea de mando.
- **1.9 Adaptación de Usuarios Reales de Base de Datos Almahue** — `COMPLETO`
  - Creación de [`cargos-jerarquicos-real.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/services/real/cargos-jerarquicos-real.ts) con todos los usuarios reales (Natalia Bravo, Daniela Fuentes, Sebastian Lagos, Rodrigo Salas, Bruno Lagos, etc.).
- **1.10 Resiliencia y Eliminación de Errores 404 en Modo Real** — `COMPLETO`
  - Fallback con sincronización en `localStorage` en [`real/api.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/services/real/api.ts).
- **1.11 Simulador de Escalamiento Jerárquico en Tiempo Real** — `COMPLETO`
  - Evaluación interactiva de solicitante, cargo y monto en `/admin/aprobaciones`, visualizando la ruta aprobatoria resuelta.
- **1.12 Saneamiento TypeScript y Build Verde** — `COMPLETO`
  - Build de producción (`tsc -b && vite build`) con **0 errores y código de salida 0**.

---

### Módulo 2: Compras, Órdenes de Compra y Aprobaciones (8 Completos)

- **2.1 Bloqueo por Tope Máximo del Último Aprobador de la Escala** — `COMPLETO` ([`OrdenCompraWizardPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx)).
- **2.2 Topes Multimoneda por Eslabón (CLP, USD, Yuan)** — `COMPLETO` ([`fixtures-cargos-jerarquicos.ts`](file:///e:/source/repos/Almahue/ERP/erp_front/src/services/mock/fixtures-cargos-jerarquicos.ts)).
- **2.3 Tipo de Cambio Sugerido del Banco Central Editable** — `COMPLETO` ([`IndicadoresBcPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/pages/parametrizacion/IndicadoresBcPage.tsx)).
- **2.4 Restricción de Contabilización en Libro de Compras sin Documento Base** — `COMPLETO` ([`LibroComprasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/LibroComprasPage.tsx)).
- **2.5 Asociación Obligatoria de Facturas a OC Aprobada** — `COMPLETO`.
- **2.6 Desacople de Cotizaciones Directas (OC como Documento de Arranque)** — `COMPLETO`.
- **2.7 Alerta Visual en Libro de Compras por OC No Aprobada** — `COMPLETO`.
- **2.8 Plazo de Aceptación Comercial Parametrizable (8 días)** — `COMPLETO`.

---

### Módulo 3: Insumos, Bodegas y Recetas de Embalaje (7 Completos)

- **3.1 Recetas de Embalaje por Centro de Costo (Desvinculadas de un Packing Único)** — `COMPLETO` ([`OrdenesAplicacionPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesAplicacionPage.tsx)).
- **3.2 Distribución de Cantidades por Packing en el Consumo** — `COMPLETO`.
- **3.3 Consumo Valorizado al Precio Promedio Ponderado del Stock Mensual** — `COMPLETO`.
- **3.4 Devolución a Proveedor al Precio de la Guía sin Restar Stock Origen** — `COMPLETO`.
- **3.5 Recepción de Guías en Estado 'Por Confirmar'** — `COMPLETO` ([`GuiasInsumosRecibidasPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx)).
- **3.6 Incremento de Stock Exclusivo al Confirmar Recepción Física** — `COMPLETO`.
- **3.7 Adjunto y Subida de Respaldos Fotográficos de Guías Firmadas** — `COMPLETO`.

---

### Módulo 4: Contabilidad, Asientos y Presupuestos (6 Completos)

- **4.1 Modal de Anulación de Comprobantes con Registro de Motivo** — `COMPLETO` ([`AsientosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/AsientosPage.tsx)).
- **4.2 Filtro Estricto de Comprobantes Activos en Libro Mayor** — `COMPLETO` ([`LibroDiarioMayorPages.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/LibroDiarioMayorPages.tsx)).
- **4.3 Reversa de Proformas sin Apertura de Periodo (Edición de Línea)** — `COMPLETO`.
- **4.4 Presupuesto por Centro de Costo y Agrupación por Departamento** — `COMPLETO` ([`PresupuestosPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/presupuestos/PresupuestosPage.tsx)).
- **4.5 Exportación PDF y Excel en Grillas Contables** — `COMPLETO`.
- **4.6 Comentario Independiente en Detalle de Comprobante** — `COMPLETO`.

---

### Módulo 5: Activos Fijos (3 Completos)

- **5.1 Alta de Activo Fijo Vinculada a OC Recepcionada** — `COMPLETO` ([`ActivoFijoPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoPage.tsx)).
- **5.2 Factura de Compra Opcional en el Alta Inicial** — `COMPLETO`.
- **5.3 Historial de Vida y Trazabilidad del Activo** — `COMPLETO`.

---

### Módulo 6: Tesorería y Bancos (4 Completos)

- **6.1 Cartola Bancaria con Desglose y Conversión a Moneda Base (Pesos)** — `COMPLETO` ([`CartolaBancariaPage.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CartolaBancariaPage.tsx)).
- **6.2 Validación de No Duplicidad en Movimientos Semanales** — `COMPLETO`.
- **6.3 Conciliación de Movimientos Bancarios sin Generación de Asiento `PAGO:{id}`** — `COMPLETO`.
- **6.4 Asiento Banco Anclado Exclusivamente a la Cartola (`CARTOLA:{id}`)** — `COMPLETO`.

---

### Módulo 7: Contratistas y Proformas (4 Completos)

- **7.1 Filtro de Proformas por Mes Exacto de Operación** — `COMPLETO` ([`ProformasContratistaNivel1Page.tsx`](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx)).
- **7.2 Protocolo de Dos Vistos Buenos para Reversa en Periodo Cerrado** — `COMPLETO`.
- **7.3 Transición `BORRADOR` ➔ `DEFINITIVA` con `contratistas:write`** — `COMPLETO`.
- **7.4 Eliminación Definitiva de Cadena y PIN en Proformas** — `COMPLETO`.

---

## 3. Enlaces Directos a Visores Interactivos y Documentos

### Semana Actual (02/11 al 07/11/2026)
- 🧭 **Recorrido Interactivo con Pines (1536×960):** [`docs/sesiones/acuerdos-sala-2026-11-06/recorrido.html`](file:///e:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06/recorrido.html)
- 🔍 **Comparación Antes / Después con Recuadros Verde:** [`docs/sesiones/acuerdos-sala-2026-11-06/comparacion.html`](file:///e:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06/comparacion.html)
- 📄 **Acuerdos del 06/11 (Documento diario detallado):** [`docs/requerimientos/acuerdos-por-dia/2026-11-06-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-06-acuerdos.md)
- 📄 **Acuerdos del 05/11:** [`docs/requerimientos/acuerdos-por-dia/2026-11-05-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-05-acuerdos.md)
- 📄 **Acuerdos del 04/11:** [`docs/requerimientos/acuerdos-por-dia/2026-11-04-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-04-acuerdos.md)
- 📄 **Acuerdos del 03/11:** [`docs/requerimientos/acuerdos-por-dia/2026-11-03-acuerdos.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/2026-11-03-acuerdos.md)

### Semana Anterior (26/10 al 30/10/2026)
- 📑 **Informe Consolidado Semana Anterior:** [`docs/requerimientos/informe-consolidado-requerimientos-semana-2026-10-26.md`](file:///e:/source/repos/Almahue/docs/requerimientos/informe-consolidado-requerimientos-semana-2026-10-26.md)
- 🧭 **Recorrido Interactivo Semana Anterior:** [`docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html`](file:///e:/source/repos/Almahue/docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html)
- 🔍 **Comparación Antes / Después Semana Anterior:** [`docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/comparacion.html`](file:///e:/source/repos/Almahue/docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/comparacion.html)

---
*Índice general de acuerdos por día: [`docs/requerimientos/acuerdos-por-dia/README.md`](file:///e:/source/repos/Almahue/docs/requerimientos/acuerdos-por-dia/README.md)*

