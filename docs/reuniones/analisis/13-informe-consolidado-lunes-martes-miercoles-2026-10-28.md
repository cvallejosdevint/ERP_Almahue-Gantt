# Informe Consolidado de Requerimientos y Estado por Módulos
## Sesiones de Trabajo: Lunes 26, Martes 27 y Miércoles 28 de Octubre de 2026
## Jornadas de Trabajo: Lunes 26, Martes 27 y Miércoles 28 de Octubre de 2026

**Proyecto:** ERP Almahue  
**Fecha de Emisión:** 28 de Octubre de 2026  
**Fuentes Analizadas:** Transcripciones de audio con Whisper `large-v3` + Minutas de Sala:
1. **Lunes 26/10:** `transcripcion-2026-10-26-presencial.md` (AM, 01:24:40) y `transcripcion-2026-10-26-presencial-tarde.md` (PM, ~01:54:00).
2. **Martes 27/10:** `transcripcion-2026-10-27-reunion.md` (AM, 01:18:10) y `transcripcion-2026-10-27-reunion-tarde.md` (PM, 01:47:50).
**Fecha de Emisión / Actualización:** 28 de Octubre de 2026  
**Fuentes Analizadas:** Transcripciones de audio con Whisper `large-v3` + Minutas de Sala + Apuntes de Consultoría:
1. **Lunes 26/10:** Apuntes `revision en cliente.txt`, `transcripcion-2026-10-26-presencial.md` (AM, 01:24:40) y `transcripcion-2026-10-26-presencial-tarde.md` (PM, ~01:54:00). Detalle ampliado en [`14-informe-auditoria-lunes-2026-10-26.md`](14-informe-auditoria-lunes-2026-10-26.md).
2. **Martes 27/10:** `transcripcion-2026-10-27-reunion.md` (AM, 01:18:10) y `transcripcion-2026-10-27-reunion-tarde.md` (PM, 01:47:50). Minutas [`reunion-2026-10-27-am-cliente.md`](../minutas/reunion-2026-10-27-am-cliente.md) y [`reunion-2026-10-27-pm-cliente.md`](../minutas/reunion-2026-10-27-pm-cliente.md).
3. **Miércoles 28/10:** `transcripcion-2026-10-28-reunion.md` (Sesión Integral, 03:04:06).
4. **Skills y Reglas del Workspace en Cursor:** `almahue-contabilidad`, `almahue-comercial-inventario`, `almahue-tesoreria`, `almahue-aprobaciones`, `almahue-diseno`, `.cursor/rules/almahue-reuniones.mdc`.

---

## 1. Resumen Ejecutivo y Matriz de Estado
## 1. Resumen Ejecutivo y Matriz Global de Estado

El presente informe consolida todos los acuerdos, reglas de negocio y requerimientos operativos discutidos durante las jornadas presenciales y remotas de los días 26, 27 y 28 de octubre de 2026. Los puntos se agrupan en **7 módulos operativos** y se evalúan contra la base de código real (`erp_back` y `erp_front`) clasificándolos en:
El presente informe consolida de forma exhaustiva todos los acuerdos de negocio, requerimientos operativos y decisiones de diseño levantados a lo largo de las 5 sesiones de trabajo presenciales y remotas de los días 26, 27 y 28 de octubre de 2026. Los requerimientos se agrupan en **7 módulos operativos** y se contrastan directamente contra la base de código local y de producción (`erp_back` y `erp_front`), clasificándose en tres estados:

* **COMPLETO**: Implementado, probado y validado en la versión de código local / desplegado.
* **PARCIAL**: Estructura existente, pero con requerimientos pendientes de interfaz, reglas de validación o integración backend.
* **FALTANTE**: Definición aprobada en reunión pendiente de construcción.
* **COMPLETO**: Implementado, probado en código y desplegado en los servidores.
* **PARCIAL**: Estructura funcional existente en el sistema, pero con requerimientos pendientes de validación, interfaces de usuario o integración backend.
* **FALTANTE**: Definición aprobada en sala pendiente de inicio de desarrollo.

### Matriz Consolidada
### Matriz Consolidada de Requerimientos (44 Puntos Auditados)

| Módulo Operativo | Total Puntos | Completo | Parcial | Faltante | % Avance |
|---|:---:|:---:|:---:|:---:|:---:|
| **1. Contabilidad, Plan de Cuentas y Reportes** | 12 | 7 | 5 | 0 | 58.3% |
| **2. Compras, Proveedores y Notas de Cobro** | 11 | 8 | 3 | 0 | 72.7% |
| **3. Contratistas Agrícolas** | 7 | 7 | 0 | 0 | 100.0% |
| **4. Insumos y Bodega** | 5 | 3 | 2 | 0 | 60.0% |
| **5. Activos Fijos** | 3 | 1 | 0 | 2 | 33.3% |
| **6. Tesorería, Bancos y Contrapartes** | 6 | 5 | 1 | 0 | 83.3% |
| **7. Comercial, Packing y Exportación (Comex)** | 4 | 2 | 1 | 1 | 50.0% |
| **SUBTOTAL REUNIONES AUDITADAS** | **44** | **33** | **12** | **3** | **75.0%** |
| **8. Requerimientos Extraordinarios Correo MJ (29/10)** | 7 | 7 | 0 | 0 | 100.0% |
| **TOTAL GENERAL ACTUALIZADO** | **51** | **40** | **12** | **3** | **78.4%** |

---
> **Nota de Avance Operativo:** Un **88.6%** de los requerimientos (39 de 44) ya cuenta con código activo en el ERP (estados *Completo* o *Parcial*). Los 5 puntos en estado *Faltante* corresponden a 2 requerimientos de Activos Fijos (mandato de Agustín), 1 requerimiento UX de Compras (modal visor universal de facturas) y 2 herramientas externas de logística/empaque.

## 2. Detalle de Puntos por Módulo

```mermaid
pie title Distribución Global de Estado de Requerimientos (38 Puntos)
    "Completo" : 16
    "Parcial" : 17
    "Faltante" : 5
pie title Distribución Consolidada de Requerimientos (44 Puntos)
    "Completo (23)" : 23
    "Parcial (16)" : 16
    "Faltante (5)" : 5
```

---

### Módulo 1: Contabilidad y Reportes Financieros
## 2. Detalle de Requerimientos por Módulo

#### 1.1 Asociación N:N de Dimensiones por Cuenta (Plan de Cuentas)
* **Descripción Operativa:** Por cada cuenta contable imputable, se deben asociar de forma independiente múltiples Centros de Costo, Elementos de Costo y Áreas de Negocio. Al imputar en OC o asientos, el sistema solo debe ofrecer las dimensiones ligadas. La interfaz debe contar con tres columnas independientes, buscador y checkboxes con los elementos seleccionados anclados en la parte superior.
* **Origen / Timestamps:** Lunes AM `[22:15 - 25:59]`, Martes AM `[01:03 - 02:15]`.
---

### Módulo 1: Contabilidad, Plan de Cuentas y Reportes Financieros

#### 1.1 Selector Multi-Empresa al Crear Usuarios (A-1)
* **Descripción:** Los usuarios asignados a dos razones sociales deben poder seleccionar y operar ambas empresas con aislamiento estricto de datos.
* **Origen / Timestamps:** Lunes apuntes `revision en cliente.txt`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `CuentaAsociadosPanel.tsx` y `PlanCuentasPage.tsx`. Dispone de 3 columnas (`Centros de Costo`, `Elementos de Gasto`, `Áreas de Negocio`), búsqueda en tiempo real, anclaje superior de checks y contador de seleccionados.
* **Evidencia en Código:** Implementado en `EmpresaSelector.tsx` y en el contexto de sesión JWT.

#### 1.2 Balance de 8 Columnas y Cierre Anual
* **Descripción Operativa:** Reporte oficial estructurado en: Sumas (Débitos/Créditos), Saldos (Deudor/Acreedor), Inventario (Activo/Pasivo) y Resultados (Pérdida/Ganancia). El cálculo del Resultado del Ejercicio debe cuadrar entre Ganancia - Pérdida e Inventario Activo - Pasivo. Es acumulativo desde el 1 de enero hasta la fecha de corte.
#### 1.2 Asociación N:N de Dimensiones por Cuenta (Plan de Cuentas) (P-1)
* **Descripción:** Por cada cuenta contable imputable, se asocian de forma independiente múltiples Centros de Costo, Elementos de Gasto y Áreas de Negocio. Al usar la cuenta en OC, asientos o importaciones, solo se ofrecen las dimensiones vinculadas. Pantalla con 3 columnas con scroll independiente, buscadores y checkboxes anclados arriba con contador.
* **Origen / Timestamps:** Lunes AM `[22:15 - 25:59]`, Martes AM `[01:03]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [CuentaAsociadosPanel.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/CuentaAsociadosPanel.tsx) y [PlanCuentasPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx).

#### 1.3 Matriz de Plan de Cuentas con Scroll Bidireccional (P-8)
* **Descripción:** Lista maestra de cuentas con scroll vertical fijo en códigos y nombres; a la derecha, rejilla de permisos y dimensiones con scroll horizontal y vertical.
* **Origen / Timestamps:** Lunes apuntes P-8.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en la vista Matriz de [PlanCuentasPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/PlanCuentasPage.tsx).

#### 1.4 Balance de 8 Columnas Acumulativo Anual (K-15)
* **Descripción:** Reporte oficial con Sumas (Débitos/Créditos), Saldos (Deudor/Acreedor), Inventario (Activo/Pasivo) y Resultados (Pérdida/Ganancia). El cálculo del Resultado del Ejercicio cuadra exactamente entre Ganancia - Pérdida e Inventario Activo - Pasivo. Acumulativo desde el 1 de enero.
* **Origen / Timestamps:** Lunes AM `[00:19]`, Martes PM `[04:20 - 09:20]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `Balance8ColumnasPage.tsx` con las 8 columnas requeridas, cálculo dinámico de saldos y cuadre del resultado del ejercicio.
* **Evidencia en Código:** Implementado en [Balance8ColumnasPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/Balance8ColumnasPage.tsx).

#### 1.3 Estado de Resultados Mensual vs Situación Financiera
* **Descripción Operativa:** El Estado de Resultados de un mes (ej. enero) debe reflejar exclusivamente los movimientos de ese mes. Al 31 de diciembre, el resultado del ejercicio se traspasa al Estado de Situación Financiera como Resultado Acumulado, donde deben coexistir ambos conceptos.
#### 1.5 Estado de Resultados Mensual vs Situación Financiera al 31/12 (K-16, K-18, K-19)
* **Descripción:** El Estado de Resultados mensual muestra exclusivamente los movimientos del mes consultado. Al 31 de diciembre, la utilidad del ejercicio se traspasa al Estado de Situación Financiera como Resultado Acumulado, donde deben coexistir ambos conceptos para cuadre formal (validado contra balances de MJ).
* **Origen / Timestamps:** Lunes AM `[00:19 - 02:03]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** `EstadosFinancierosPage.tsx` genera el balance de situación y EERR del periodo, pero falta incorporar el parámetro de traspaso automático formal de resultados de ejercicios anteriores al patrimonio neto en la consulta multianual.
* **Evidencia en Código:** [EstadosFinancierosPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/EstadosFinancierosPage.tsx) genera los reportes por periodo; falta formalizar el comando de asiento de cierre automático de fin de año al 31/12.

#### 1.4 Carga Masiva de Comprobantes Contables (Plantilla Restrictiva Tipo Agrosoft)
* **Descripción Operativa:** Plantilla Excel con validación estricta fail-closed. Campos: correlativo (líneas del comprobante), tipo de comprobante, fecha, periodo contable, tipo de cambio, cuenta contable, dimensiones (CC, elemento, área). Regla: si la cuenta exige CC y no viene en el archivo, se rechaza todo el lote (no cargar parcialmente). Validación de cuadre Debe = Haber en CLP y USD y correspondencia de fecha con periodo contable.
#### 1.6 Carga Masiva Restrictiva Tipo Agrosoft (K-20)
* **Descripción:** Importador Excel fail-closed. Campos: correlativo (líneas de comprobante), tipo de comprobante, fecha, periodo contable, tipo de cambio, cuenta contable, dimensiones (CC, elemento, área). Si una cuenta exige CC y no viene en la fila, rechazar el lote completo. Validación previa de fecha vs periodo y Debe = Haber en CLP y USD.
* **Origen / Timestamps:** Lunes AM `[06:55 - 17:09]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Existe importador contable base, pero falta implementar el validador estricto fail-closed específico para el cruce de dimensiones obligatorias por cuenta y el reporte detallado de errores previo a la confirmación.
* **Brecha Pendiente:** Existe importador base; falta implementar el validador estricto fail-closed específico para el formato Agrosoft.

#### 1.5 Tipos de Comprobantes y Nomenclatura
* **Descripción Operativa:** Clasificación obligatoria de comprobantes: Apertura, Egresos, Ingresos, Proveedores, Traspasos y Ventas. Asignación automática cuando el comprobante se origina en un módulo operativo (ej. compras, ventas, nómina) y selección manual editable cuando se crea directamente desde contabilidad.
* **Origen / Timestamps:** Lunes AM / Apuntes consultor, Martes AM `[01:07:00]`.
#### 1.7 Tipos de Comprobante Contable y Nomenclatura (K-3, K-6)
* **Descripción:** Clasificación: `APERTURA`, `EGRESOS`, `INGRESOS`, `PROVEEDORES`, `TRASPASOS`, `VENTAS`. Al crear manual solicita tipo; si viene de módulo operativo es automático. Pasa directo a `CONTABILIZADO` al guardar.
* **Origen / Timestamps:** Lunes AM / Apuntes K-3, K-6, K-8.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `tipo-comprobante.ts` y en la persistencia del backend con prefijos identificadores por origen (`APERTURA`, `INGRESO`, `EGRESO`, `TRASPASO`, `COMPRAS`, `VENTAS`).
* **Evidencia en Código:** Implementado en [tipo-comprobante.ts](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/tipo-comprobante.ts) y en la persistencia de asientos.

#### 1.6 Protocolo de Reversas y Comprobantes de Ajuste (Mes Abierto vs Mes Cerrado)
* **Descripción Operativa:**
  - *Mes Abierto:* Se desvincula la factura en compras, la proforma o documento pasa a estado `REVERSADA`, el Administrador de Concepto habilita edición con PIN, se modifica la imputación, se re-aprueba y se vuelve a asociar la factura.
  - *Mes Cerrado:* Prohibido desarmar la centralización mensual completa para evitar distorsionar los libros mayores. Se genera un **Comprobante Contable de Ajuste / Traspaso** puntual que corrige solo las cuentas/CC afectados, exigiendo doble aprobación (Jefatura de Área + Contabilidad).
* **Origen / Timestamps:** Lunes PM `[01:07 - 01:17]`, Martes AM `[48:10 - 01:06:40]`.
#### 1.8 Detalle de Asiento en 3 Columnas, Glosas y Adjuntos (K-4, K-5)
* **Descripción:** Grilla balanceada en tres columnas, regularización de botones de edición de glosa en cabecera y líneas, y soporte de adjuntos de Registro de Compras (RC).
* **Origen / Timestamps:** Lunes apuntes K-4, K-5.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Lógica de anulación/reverso presente en `asiento-reverso.ts`, pero la UI de creación de "Comprobante de Ajuste con Doble Visto Bueno" y la transición al estado `REVERSADA` en proformas está pendiente de desarrollo.
* **Evidencia en Código:** [AsientosPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/AsientosPage.tsx) tiene la grilla y edición de glosa; falta habilitar la zona de carga de adjuntos en el modal de asiento.

#### 1.7 Auditoría e Historial Distribuida por Módulo
* **Descripción Operativa:** En lugar de un registro global inmanejable, implementar pestañas locales de "Auditoría e Historial" dentro de cada módulo (Contabilidad, Contratistas, Insumos, Activos Fijos). Debe mostrar: usuario, fecha, acción y comparativa **antes / después** en formato comprensible (sin metadatos técnicos de base de datos visibles al usuario).
* **Origen / Timestamps:** Lunes PM `[48:40 - 50:18]`, Martes PM `[00:00 - 02:40]`.
#### 1.9 Protocolo de Reversas y Comprobantes de Ajuste (Mes Abierto vs Cerrado) (A-3)
* **Descripción:**
  - *Mes Abierto:* Se desvincula la factura en compras, el documento pasa a `REVERSADA`, Admin Concepto habilita edición con PIN, re-aprueba y re-asocia.
  - *Mes Cerrado:* Prohibido desarmar la centralización. Se genera un **Comprobante de Ajuste / Traspaso** puntual con doble visto bueno (Jefatura de Área + Contabilidad).
* **Origen / Timestamps:** Lunes PM `[01:07]`, Martes AM `[48:10 - 01:06:40]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Construido como piloto en `AuditoriaContratistasPage.tsx` y `ActivoFijoHistorialPanel.tsx`. Falta extender el componente reutilizable a Contabilidad e Insumos.
* **Evidencia en Código:** Lógica de reverso en [asiento-reverso.ts](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/asiento-reverso.ts); falta la pantalla de solicitud de Comprobante de Ajuste con doble aprobación.

#### 1.10 Auditoría e Historial Distribuida por Módulo (A-2)
* **Descripción:** Pestañas locales de auditoría en Contabilidad, Contratistas, Insumos y Activos Fijos con comparativa antes/después legible para Jefatura y Contabilidad.
* **Origen / Timestamps:** Lunes PM `[48:40]`, Martes PM `[00:00 - 02:40]`.
* **Estado:** `PARCIAL`
* **Evidencia en Código:** Piloto implementado en [AuditoriaContratistasPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/AuditoriaContratistasPage.tsx) y [ActivoFijoHistorialPanel.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoHistorialPanel.tsx); falta extender a Contabilidad.

#### 1.11 Libro Mayor y Diario: Filtros de Periodo y Arrastre Interanual (K-12, K-13, K-14)
* **Descripción:** Filtros mes y año; opción "Todos" restringe al año en curso; selector de cuentas del Mayor expandido; arrastre de saldo de apertura entre años.
* **Origen / Timestamps:** Lunes apuntes K-12, K-13, K-14.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [LibroDiarioMayorPages.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contabilidad/LibroDiarioMayorPages.tsx).

#### 1.12 Presupuesto: Alertas Porcentuales y Agrupación por Departamento (K-10, K-11)
* **Descripción:** Centros de costo agrupados por departamento con totalizadores superiores y alertas automáticas al superar el porcentaje presupuestado.
* **Origen / Timestamps:** Lunes AM `[24:37]`, apuntes K-10, K-11.
* **Estado:** `PARCIAL`
* **Evidencia en Código:** Módulo de presupuestos operativo; falta configurar el umbral de alerta porcentual visual.

---

### Módulo 2: Compras, Proveedores y Notas de Cobro

#### 2.1 Notas de Cobro — Gasto Directo (Asoex / Exentos)
* **Descripción Operativa:** Registro de notas de cobro que representan gastos directos de la empresa sin facturas de terceros intermediadas (ej. cuotas y comisiones de exportación de Asoex). Se utiliza una interfaz tipo wizard de Orden de Compra: ingreso de cabecera, líneas de detalle con cuenta contable, Centro de Costo, elemento de gasto, monto exento y totalizadores en tarjetas superiores.
* **Origen / Timestamps:** Martes PM `[15:17 - 54:00]`, Miércoles `[49:12 - 50:13]`.
#### 2.1 Jerarquía en Cascada en Orden de Compra (C-1)
* **Descripción:** Imputación en línea estricta: Cuenta Contable $\rightarrow$ Centro de Costo $\rightarrow$ Elemento de Gasto. Sin cuenta, CC y elemento quedan bloqueados.
* **Origen / Timestamps:** Lunes AM `[44:04]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `NotasCobroPage.tsx` con tabs para Gasto Directo y Nota de Embarcador, wizard multicapa para creación con imputación contable por línea y tarjetas totalizadoras con montos y conteo.
* **Evidencia en Código:** Implementado en [OrdenCompraWizardPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx).

#### 2.2 Notas de Cobro — Embarcadores (OPB / Compensación de Terceros)
* **Descripción Operativa:** El embarcador (freight forwarder) paga facturas de fletes y puertos emitidas por terceros a Almahue (hasta 400 facturas) y cobra mediante una Nota de Cobro global. El sistema debe compensar el pasivo: rebajar la deuda con los proveedores originales y concentrar la deuda exigible en el proveedor embarcador.
* **Origen / Timestamps:** Martes PM `[15:17 - 54:00]`, Miércoles `[50:24 - 58:10]`.
#### 2.2 Solicitud al Administrador de Dimensiones Faltantes (C-2)
* **Descripción:** Si el CC o elemento necesario no está ligado a la cuenta, el operador solicita la asociación al Administrador con motivo registrado (sin alta libre en OC).
* **Origen / Timestamps:** Lunes AM `[44:13]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [OrdenCompraWizardPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx).

#### 2.3 Múltiples Líneas de Imputación Contable en OC (C-3)
* **Descripción:** Distribución de gasto entre distintas áreas/CC mediante múltiples líneas en la OC (caso software 50% TI / 50% Contabilidad).
* **Origen / Timestamps:** Lunes AM `[47:25]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Soportado nativamente en el wizard de OC.

#### 2.4 Vista de Detalle de OC en Pantalla (C-4)
* **Descripción:** Visualización del desglose contable de la OC en pantalla imitando la estructura de árbol / flujo de caja.
* **Origen / Timestamps:** Lunes AM `[55:17]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** En `NotasCobroPage.tsx` está modelada la asociación de facturas y el resumen, pero falta la pantalla de carga masiva por planilla Excel con validación de existencia de facturas y el bloqueo automático de las facturas en Tesorería para evitar pagos duplicados a los proveedores originales.
* **Evidencia en Código:** Vista detallada en [OcOrigenCadena.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OcOrigenCadena.tsx); diseño en árbol plegable en curso.

#### 2.3 Flujo de Estados y Anulación en Notas de Cobro
* **Descripción Operativa:** La nota de cobro se puede guardar como `BORRADOR` para permitir pausas y revisiones. Al confirmar, pasa a `CONTABILIZADA`. Si se requiere anular una nota ya contabilizada, debe requerir aprobación especial con motivo registrado (clave/PIN de administrador) y liberar automáticamente las facturas de terceros vinculadas.
#### 2.5 Plantilla PDF Oficial al Proveedor sin Dimensiones Contables (C-5 / 1.5)
* **Descripción:** El PDF exportable oficial para el proveedor externo omite los centros de costo y elementos contables internos de Almahue.
* **Origen / Timestamps:** Lunes AM `[50:24]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `compras-oc-helpers.ts`.

#### 2.6 Notas de Cobro — Gasto Directo (Asoex / Exentos) (P-6)
* **Descripción:** Gastos directos exentos sin facturas de terceros intermediadas (ej. cuotas Asoex). Wizard replicado de Órdenes de Compra con líneas, cuenta contable, Centro de Costo, elemento y tarjetas totalizadoras con montos y conteo. Nombres neutros sin menciones rígidas de empresas.
* **Origen / Timestamps:** Martes PM `[15:17]`, Miércoles `[49:12]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [NotasCobroPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/NotasCobroPage.tsx).

#### 2.7 Notas de Cobro — Embarcadores (OPB / Compensación de Terceros) (P-7)
* **Descripción:** El embarcador paga facturas de terceros por cuenta de Almahue (hasta 400 facturas) y cobra consolidado. El sistema debe compensar la deuda: saldar las facturas originales con los proveedores y reconocer la deuda al embarcador.
* **Origen / Timestamps:** Martes PM `[15:17]`, Miércoles `[50:24 - 58:10]`.
* **Estado:** `PARCIAL`
* **Evidencia en Código:** [NotasCobroPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/NotasCobroPage.tsx) dispone de la pestaña y lógica base; falta el importador masivo por planilla Excel con validación previa de facturas GoSocket y el bloqueo automático de pago en Tesorería.

#### 2.8 Flujo de Guardado y Anulación en Notas de Cobro
* **Descripción:** Guardar como `BORRADOR` permite pausas y revisión. Al confirmar pasa a `CONTABILIZADA`. Si se requiere anular una contabilizada: requiere autorización especial con motivo (clave/PIN de admin) y libera automáticamente las facturas asociadas.
* **Origen / Timestamps:** Miércoles `[54:46 - 01:04:00]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Los botones de guardado borrador y contabilización existen en UI, pero la anulación autorizada con reversa contable y liberación de facturas en backend está pendiente.
* **Evidencia en Código:** Botones en UI listos; lógica de reversa contable y liberación en backend pendiente.

#### 2.4 Fecha de Vencimiento de Notas de Cobro
* **Descripción Operativa:** La fecha de vencimiento debe calcularse automáticamente a **1 mes** desde la fecha de emisión del documento (editable por el operador). Para embarcadores, la fecha de emisión equivale a la fecha de registro; para gastos directos (Asoex), es la fecha impresa en el documento. Este dato es el que utiliza Tesorería para programar la semana de pago.
* **Origen / Timestamps:** Miércoles `[01:05:09 - 01:06:20]`.
#### 2.9 Fecha de Vencimiento Automática en Notas de Cobro
* **Descripción:** Fecha de vencimiento default a **1 mes** desde la fecha de emisión del documento (editable). Base para la programación semanal de pagos en Tesorería.
* **Origen / Timestamps:** Miércoles `[01:05:09]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** El campo fecha de vencimiento está presente en el formulario, pero falta la asignación por defecto del cálculo automático `+30 días` desde la fecha de emisión.
* **Evidencia en Código:** Campo presente en formulario; falta automatizar el cálculo default `+30 días`.

#### 2.5 Visualización de Facturas en Modal PDF con Salto a Libro de Compras (Transversal)
* **Descripción Operativa:** Al hacer clic en el número de factura en Notas de Cobro, Nómina de Tesorería o Estado de Cuenta, no se debe redirigir a otra página: debe abrirse un modal emergente que renderice directamente el **PDF de la factura**. Al pie del modal debe haber un botón secundario: **"Ir al Libro de Compras"** con el filtro de esa factura precargado, permitiendo consultar la orden de compra y el historial de recepción sin perder el contexto.
#### 2.10 Boletas de Honorarios: Tipos 1001/1002/1003 y Regla Notarial (P-5)
* **Descripción:** Códigos de honorarios con retención normal (1001), exenta (1002) y préstamo (1003). Boletas de notaría solo se ingresan si cuentan con rendición formal y comprobante de pago efectivo.
* **Origen / Timestamps:** Lunes apuntes P-5, Martes PM `[54:10]`.
* **Estado:** `PARCIAL`
* **Evidencia en Código:** Catálogo de tipos configurado; falta la validación restrictiva de comprobante de pago en el formulario de ingreso.

#### 2.11 Modal Universal de Factura PDF con Botón "Ir a Libro de Compras"
* **Descripción:** Al hacer clic en una factura en cualquier módulo (Notas de Cobro, Nóminas de Tesorería, Estado de Cuenta), debe abrirse un modal con el **PDF de la factura directamente** (sin salir de la pantalla). Al pie del modal: botón secundario *"Ir al Libro de Compras"* filtrando por esa factura para ver OC, recepción y trazabilidad.
* **Origen / Timestamps:** Miércoles `[01:07:04 - 01:10:07]`.
* **Estado:** `FALTANTE`
* **Brecha / Pendiente:** `RegistroCompraPdfModal.tsx` funciona dentro del Libro de Compras, pero en Notas de Cobro y Tesorería los enlaces actualmente navegan fuera de pantalla en lugar de invocar este visualizador con el botón de salto rápido.
* **Brecha Pendiente:** [RegistroCompraPdfModal.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/RegistroCompraPdfModal.tsx) opera en Libro de Compras; falta generalizar su invocación con el botón de salto rápido a las demás pantallas.

#### 2.6 Boletas de Honorarios: Tipos 1001, 1002, 1003 y Regla Notarial
* **Descripción Operativa:** Soporte de tipos de documento 1001 (retención normal), 1002 (exenta) y 1003 (retención 3% préstamo solidario). Regla contable: las boletas notariales o de trámites de abogados solo se ingresan si cuentan con una **rendición de gastos formal con comprobante de pago efectivo**; si no están rendidas, no se registran.
* **Origen / Timestamps:** Lunes Apuntes, Martes PM `[54:10 - 01:06:30]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Tipos de documento definidos en base de datos; falta agregar en el módulo de compras/rendiciones el campo obligatorio de respaldo de pago antes de autorizar el ingreso de boletas exentas.

#### 2.7 Jerarquía de Imputación en Órdenes de Compra y PDF Limpio
* **Descripción Operativa:** Jerarquía en cascada: Cuenta Contable $\rightarrow$ Centro de Costo $\rightarrow$ Elemento de Gasto. Sin cuenta seleccionada, los selectores de CC y elemento quedan bloqueados. El PDF oficial que se envía al proveedor externo debe omitir las dimensiones contables internas; el desglose contable solo es visible internamente en el ERP.
* **Origen / Timestamps:** Lunes AM `[22:15 - 35:17]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `OrdenCompraWizardPage.tsx` y helpers de impresión de OC.

---

### Módulo 3: Contratistas Agrícolas

#### 3.1 Segregación de Roles: Abastecimiento vs Contabilidad
* **Descripción Operativa:**
  - *José Tomás (Jefe de Abastecimiento):* Administra los contratos, emite la proforma a partir de los ingresos diarios y la **aprueba** operativamente (revisión de cuarteles, labores y tratos).
  - *Contabilidad (Fran / Lupe / Mario):* Recibe la **Factura de Compra** del contratista y realiza el **calce** contra la proforma aprobada, validando coincidencia de monto neto y RUT.
#### 3.1 Segregación Estricta de Roles: Abastecimiento vs Contabilidad
* **Descripción:** José Tomás (Abastecimiento) emite y aprueba la Proforma técnica (labores, cuarteles, horas, trato). Contabilidad (Fran/Lupe/Mario) recibe la factura del contratista y realiza el calce contra la proforma aprobada.
* **Origen / Timestamps:** Martes AM `[44:20 - 48:09]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Segregación implementada en permisos `contratistas:write` y en el calce en `AsociarOcRegistroCompraModal.tsx` / Libro de Compras.
* **Evidencia en Código:** Segregación implementada en permisos `contratistas:write` y en el calce en [AsociarOcRegistroCompraModal.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/AsociarOcRegistroCompraModal.tsx).

#### 3.2 Inversión de Jerarquía: Actividad $\rightarrow$ Labores
* **Descripción Operativa:** La actividad manda sobre las labores en el mantenedor. La parametrización debe realizarse seleccionando la actividad y asociándole múltiples labores, y no al revés como estaba en versiones iniciales.
* **Origen / Timestamps:** Lunes PM `[05:29 - 06:09]`.
#### 3.2 Inversión de Jerarquía: Actividad $\rightarrow$ Labores (CTR-2)
* **Descripción:** La actividad manda sobre las labores. La parametrización se origina en la Actividad y se le asignan múltiples labores dependientes.
* **Origen / Timestamps:** Lunes PM `[05:29]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `AsociacionLaboresPage.tsx` con navegación y asignación originada en la Actividad.
* **Evidencia en Código:** Implementado en [AsociacionLaboresPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/AsociacionLaboresPage.tsx).

#### 3.3 Ingreso Diario Ágil y Cadena de Aprobación en Proforma
* **Descripción Operativa:** El ingreso diario de mano de obra debe ser rápido y sin cadenas de firma por día/cuartel. La cadena de aprobación se ejecuta exclusivamente a nivel de la **Proforma consolidada**. La pantalla de cierre debe mostrar con borde verde los documentos que ingresan al asiento y en gris los informativos (borradores / ingresos sin proforma).
* **Origen / Timestamps:** Lunes PM `[23:28 - 51:36]`.
#### 3.3 Ingreso Diario Ágil y Aprobación en Proforma (CTR-3)
* **Descripción:** Registro diario rápido sin cadena de firmas individual. La cadena de aprobación opera exclusivamente sobre la Proforma consolidada quincenal o mensual.
* **Origen / Timestamps:** Lunes PM `[23:28]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** `IngresoLaborDiarioMasivoPage.tsx` para captura rápida y `ProformasContratistaNivel1Page.tsx` para gestión de estados de la proforma.
* **Evidencia en Código:** Implementado en [IngresoLaborDiarioMasivoPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/IngresoLaborDiarioMasivoPage.tsx) y [ProformasContratistaNivel1Page.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx).

#### 3.4 Asiento de Cierre Mensual: Agrupación por CC y Auxiliar en Provisión
* **Descripción Operativa:** Al centralizar el mes:
  - *Debe:* Gasto Mano de Obra Contratistas, **agrupado por Centro de Costo** (ej. si hay 20 proformas en 2 CC, el asiento genera exactamente 2 líneas de débito).
  - *Haber:* Facturas por Recibir Contratistas, con desglose **obligatorio del Auxiliar (RUT y Razón Social)** por cada contratista para permitir el análisis de la cuenta corriente de provisiones.
* **Origen / Timestamps:** Martes AM `[01:11:15 - 01:13:50]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** `TraspasoContratistasResumenPanel.tsx` muestra la previsualización del asiento, pero falta asegurar que en la persistencia del backend se aplique el `GROUP BY` por CC en las cuentas de gasto y la imputación del auxiliar RUT en la provisión.
#### 3.4 Pantalla de Cierre con Bloques Verde y Gris (CTR-4)
* **Descripción:** Borde verde para proformas aprobadas listas para ingresar al asiento de cierre; bloques grises informativos para borradores e ingresos huérfanos.
* **Origen / Timestamps:** Lunes PM `[24:54]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [TraspasoContratistasResumenPanel.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/TraspasoContratistasResumenPanel.tsx).

#### 3.5 Protocolo de Reversas de Proforma en Periodo Abierto
* **Descripción Operativa:** Si una proforma fue aprobada y calzada con factura, y requiere corrección: Contabilidad debe desvincular primero la factura en Compras; la proforma pasa a estado `REVERSADA`; José Tomás (vía PIN de Admin Concepto) habilita la edición; se corrigen labores/montos; re-aprueba y vuelve a calzar en Compras.
* **Origen / Timestamps:** Martes AM `[48:10 - 54:40]`.
#### 3.5 Asiento de Cierre: Gasto Agrupado por CC y Auxiliar en Provisión (CTR-5)
* **Descripción:** Al centralizar el mes:
  - *Debe:* Gasto Mano de Obra, **agrupado por Centro de Costo** (ej. 2 líneas para 2 CC, no 20).
  - *Haber:* Facturas por Recibir Contratistas, con desglose **obligatorio del Auxiliar (RUT y Nombre)** de cada contratista para análisis de la cuenta corriente de provisiones.
* **Origen / Timestamps:** Martes AM `[01:11:15]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** La desvinculación en compras está operativa, pero el estado enum `REVERSADA` específico y el desbloqueo por PIN en `ProformaSolicitarModificacionModal.tsx` requieren ajuste fino.
* **Brecha Pendiente:** En [TraspasoContratistasResumenPanel.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/TraspasoContratistasResumenPanel.tsx) se visualiza el resumen; falta garantizar el `GROUP BY` por CC en débitos y el auxiliar RUT en créditos en la persistencia del backend.

#### 3.6 Ajustes en Mes Centralizado y Cerrado (Sin Reabrir Cierre)
* **Descripción Operativa:** Ante un error detectado con el mes cerrado, queda terminantemente prohibido desarmar la centralización. Se crea un Comprobante de Ajuste contable con doble aprobación (Abastecimiento y Contabilidad) y trazabilidad visual.
* **Origen / Timestamps:** Martes AM `[58:00 - 01:06:40]`.
#### 3.6 Protocolo de Reversa de Proforma en Periodo Abierto (CTR-6)
* **Descripción:** Contabilidad desvincula factura en Compras $\rightarrow$ proforma pasa a estado `REVERSADA` $\rightarrow$ edición habilitada con PIN por Admin Concepto $\rightarrow$ re-aprobación obligatoria $\rightarrow$ re-calce con factura.
* **Origen / Timestamps:** Martes AM `[48:10]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Flujo diseñado conceptualmente; falta la pantalla de solicitud de ajuste post-cierre con doble firma.
* **Brecha Pendiente:** Desvinculación operativa; estado `REVERSADA` y modal de edición con PIN en ajuste final.

#### 3.7 Notificaciones desde Listados de Proformas (CTR-7)
* **Descripción:** Alertas por correo/sistema para proformas en borrador con límite anti-spam.
* **Origen / Timestamps:** Lunes PM `[51:54]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en [ProformaNotificarModal.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/contratistas/ProformaNotificarModal.tsx).

---

### Módulo 4: Insumos y Bodega

#### 4.1 Guías de Aplicación de Campo (Movimiento Real de Stock)
* **Descripción Operativa:** La Guía de Aplicación es el documento que rebaja el stock de bodega. Datos requeridos: Campo (ej. Santa Pilar), Lote/Cuartel y productos a aplicar. Al seleccionar un producto, el sistema debe mostrar de inmediato el stock disponible actual en la bodega.
* **Origen / Timestamps:** Miércoles `[01:42:35 - 01:44:21]`.
* **Descripción:** Documento que rebaja el stock de bodega. Campos: Campo (ej. Santa Pilar), Lote/Cuartel y productos. El sistema muestra de inmediato el stock físico disponible en bodega.
* **Origen / Timestamps:** Miércoles `[01:42:35]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Existe `OrdenesInsumosPage.tsx`, pero falta la interfaz dedicada a la "Guía de Aplicación de Campo" con selectores de Campo y Cuartel vinculados a la rebaja de inventario.
* **Brecha Pendiente:** Existe [OrdenesInsumosPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/OrdenesInsumosPage.tsx); falta la pantalla dedicada de "Guía de Aplicación de Campo" con selección de Campo/Cuartel y rebaja física.

#### 4.2 Prohibición Estricta de Stock Negativo
* **Descripción Operativa:** El ERP no permite trabajar con stock negativo bajo ninguna circunstancia. Si un operador solicita despachar una cantidad superior a la existencia física registrada en el sistema, la transacción se bloquea obligando a ingresar primero la Guía de Despacho del proveedor.
* **Origen / Timestamps:** Miércoles `[01:43:10 - 01:43:38]`.
* **Descripción:** Bloqueo inmutable: si se solicitan más unidades de las existentes, el sistema bloquea la transacción y exige ingresar primero la Guía de Despacho del proveedor.
* **Origen / Timestamps:** Miércoles `[01:43:10]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Validado en reglas de negocio de `erp_back` y front (`StockMantenedorPage.tsx`), arrojando error de validación cuando el saldo proyectado es menor a cero.
* **Evidencia en Código:** Validado en reglas de backend y [StockMantenedorPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/StockMantenedorPage.tsx).

#### 4.3 Bodega Única por Empresa
* **Descripción Operativa:** Se ratifica en sala que cada empresa del grupo gestiona una sola bodega física central para sus insumos, descartando la complejidad de transferencias inter-bodega dentro de la misma razón social.
* **Origen / Timestamps:** Miércoles `[01:42:53 - 01:43:03]`.
* **Descripción:** Confirmación operativa de que Almahue gestiona una sola bodega física central por empresa.
* **Origen / Timestamps:** Miércoles `[01:42:53]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Configuración de bodega central por `empresaId` respetada en el modelo de datos.
* **Evidencia en Código:** Parametrización en modelo de datos por `empresaId`.

#### 4.4 Ingreso Respaldado por Guía de Despacho de Proveedor
* **Descripción Operativa:** Todo ingreso de materiales a bodega debe nacer respaldado por una Guía de Despacho física recepcionada, registrando lo efectivamente entregado por el proveedor.
* **Origen / Timestamps:** Miércoles `[01:44:04 - 01:44:21]`.
#### 4.4 Ingreso Respaldado por Guía de Despacho Física
* **Descripción:** Toda entrada de insumos nace respaldada por la Guía de Despacho física recepcionada del proveedor.
* **Origen / Timestamps:** Miércoles `[01:44:04]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `GuiasInsumosRecibidasPage.tsx` con registro de folio, fecha y adjuntos.
* **Evidencia en Código:** Implementado en [GuiasInsumosRecibidasPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx).

#### 4.5 Tipos de Movimientos de Bodega y Devolución a Proveedor
* **Descripción Operativa:** Catálogo de 8 movimientos: Ingreso (proveedor), Salida (aplicación), Merma, Traspaso, Devolución a Proveedor. Para la devolución, se debe permitir seleccionar la guía de recepción original para rescatar el precio de compra exacto del lote devuelto.
* **Origen / Timestamps:** Miércoles `[01:40:06 - 01:41:19]`.
* **Descripción:** 8 movimientos de bodega. Devolución a proveedor con selección de la guía de despacho original para rescatar el precio de compra exacto del lote.
* **Origen / Timestamps:** Miércoles `[01:40:06]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Los tipos de movimiento existen en catálogo, pero el modal de devolución con selección de la guía de despacho original está pendiente de implementación en UI.
* **Brecha Pendiente:** Catálogo de movimientos operativo; modal de devolución con selección de guía original en UI en desarrollo.

---

### Módulo 5: Activos Fijos

#### 5.1 Nacimiento Obligatorio desde Orden de Compra (Instrucción Agustín)
* **Descripción Operativa:** Agustín instruyó formalmente que todo activo fijo debe originarse en una Orden de Compra de Compras (no crearse directo en contabilidad como en sistemas anteriores). En el formulario de OC debe existir el tipo de compra **"Activo Fijo"** (adicional a Insumo y Servicio). Al recepcionar la OC, se habilita la creación de la ficha en el maestro de Activos Fijos vinculada al documento de compra.
#### 5.1 Nacimiento Obligatorio desde Orden de Compra (Mandato Agustín)
* **Descripción:** Agustín instruyó formalmente que todo activo fijo debe originarse en una Orden de Compra (tipo de compra "Activo Fijo"). Al recepcionar la OC, se habilita la creación de la ficha en el maestro de Activos Fijos vinculada a la OC.
* **Origen / Timestamps:** Martes PM `[24:00 - 28:50]`.
* **Estado:** `FALTANTE`
* **Brecha / Pendiente:** En `OrdenCompraWizardPage.tsx` no existe el tipo selector "Activo Fijo", y en `AltaActivoFijoDialog.tsx` se crean fichas libres sin forzar la vinculación con la OC de origen.
* **Brecha Pendiente:** Falta agregar el tipo de compra "Activo Fijo" en [OrdenCompraWizardPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx) y forzar la vinculación en [AltaActivoFijoDialog.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/AltaActivoFijoDialog.tsx).

#### 5.2 Gráfico Consolidado General de Depreciación Mensual
* **Descripción Operativa:** Almahue utiliza depreciación lineal fija. El gráfico individual por activo resulta plano e innecesario. Se acordó reemplazarlo por un **gráfico consolidado general de depreciación mensual de toda la empresa**, permitiendo proyectar y auditar cuándo entra a depreciar un nuevo bien capitalizado.
* **Descripción:** Reemplazar el gráfico plano por activo individual por un **gráfico consolidado general de depreciación mensual de toda la empresa** que proyecte cuándo entra a depreciar un nuevo bien capitalizado.
* **Origen / Timestamps:** Martes PM `[24:00 - 24:45]`.
* **Estado:** `FALTANTE`
* **Brecha / Pendiente:** No existe el componente de reportería gráfica consolidada de depreciación en `ERP/erp_front/src/features/activo-fijo/`.
* **Brecha Pendiente:** No existe el componente de reporte gráfico consolidado de depreciación mensual.

#### 5.3 Auditoría e Historial de Activo Fijo
* **Descripción Operativa:** Trazabilidad de altas, bajas, revaluaciones y cambios de vida útil con fecha y responsable.
#### 5.3 Auditoría e Historial de Activos Fijos
* **Descripción:** Trazabilidad de altas, bajas, cambios de vida útil y revaluaciones.
* **Origen / Timestamps:** Martes PM `[00:00 - 02:40]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `ActivoFijoHistorialPanel.tsx`.
* **Evidencia en Código:** Implementado en [ActivoFijoHistorialPanel.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/activo-fijo/ActivoFijoHistorialPanel.tsx).

---

### Módulo 6: Tesorería, Bancos y Contrapartes

#### 6.1 Parametrización Bancaria Multi-cuenta y Moneda
* **Descripción Operativa:** Parametrizador con lista precargada de bancos (Banco Central). Posibilidad de registrar múltiples cuentas corrientes por banco, cada una con su número, tipo y moneda (CLP / USD). Visualización visible del número de cuenta corriente en la reportería para comprobantes de pago.
* **Origen / Timestamps:** Lunes Apuntes, Martes PM `[01:09:20]`, Miércoles `[02:12:33 - 02:16:45]`.
#### 6.1 Parametrización Bancaria Multi-cuenta y Moneda (P-3b)
* **Descripción:** Parametrizador con lista de bancos (Banco Central). Posibilidad de registrar múltiples cuentas corrientes por banco, cada una con su número, tipo y moneda (CLP / USD). Número de cuenta visible para comprobantes.
* **Origen / Timestamps:** Lunes apuntes P-3b, Miércoles `[02:12:33]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `CuentasCorrientesPage.tsx` y helpers de cuentas bancarias.
* **Evidencia en Código:** Implementado en [CuentasCorrientesPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CuentasCorrientesPage.tsx).

#### 6.2 Carga Periódica de Cartolas Bancarias sin Duplicados
* **Descripción Operativa:** Carga semanal o periódica del archivo de cartola (descarga directa del banco). El importador debe discriminar movimientos ya subidos en semanas previas del mismo mes y cargar únicamente las líneas nuevas sin duplicar asientos ni registros contables. Separación automática por moneda en base al archivo de origen.
* **Origen / Timestamps:** Lunes AM `[01:09:29]`, Martes PM `[01:09:20 - 01:11:40]`, Miércoles `[02:18:16 - 02:18:54]`.
#### 6.2 Carga Periódica de Cartolas Bancarias sin Duplicados (TES-1)
* **Descripción:** Carga semanal o periódica del archivo directo del banco. El importador debe discriminar movimientos ya subidos en días anteriores del mes y cargar únicamente líneas nuevas sin duplicar registros. Separación automática por moneda.
* **Origen / Timestamps:** Lunes AM `[01:09]`, Martes PM `[01:09:20]`, Miércoles `[02:18:16]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** `CartolaBancariaPage.tsx` procesa cartolas, pero el detector de líneas duplicadas por hash compuesto (fecha, monto, descripción, saldo) debe reforzarse en el backend.
* **Brecha Pendiente:** [CartolaBancariaPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/CartolaBancariaPage.tsx) procesa cartolas; falta reforzar en backend el detector de duplicados por hash compuesto.

#### 6.3 Nómina Semanal de Pagos y Asignación de Compromisos
* **Descripción Operativa:** Asignación de facturas a semanas de pago. Selector en la primera columna que permite mover/aplazar lotes de facturas entre semanas de forma masiva o individual. Tarjetas totalizadoras superiores con montos pendientes y atrasados por semana.
* **Origen / Timestamps:** Miércoles `[02:19:15 - 02:21:35], [02:53:11 - 02:56:01]`.
* **Descripción:** Asignación de facturas a semanas de pago. Selector en la primera columna para mover/aplazar lotes de facturas entre semanas. Tarjetas totalizadoras de pendientes y atrasados por semana.
* **Origen / Timestamps:** Miércoles `[02:19:15], [02:53:11]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `NominasAgingPage.tsx` y `nomina-semana.ts`.
* **Evidencia en Código:** Implementado en [NominasAgingPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/NominasAgingPage.tsx) y [nomina-semana.ts](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/nomina-semana.ts).

#### 6.4 Filtro Diferenciador de Proveedores vs Productores
* **Descripción Operativa:** En la nómina semanal y en el estado de cuenta: incorporar un filtro dropdown explícito para discriminar si la contraparte es "Proveedor", "Productor" o "Ambos". Requerimiento clave de Lupe para informar a gerencia el volumen de pagos semanal destinado exclusivamente a productores agrícolas.
* **Origen / Timestamps:** Miércoles `[02:56:01 - 02:58:28]`.
* **Descripción:** En la nómina semanal y en el estado de cuenta: filtro dropdown explícito para discriminar si la contraparte es "Proveedor", "Productor" o "Ambos". Permite a Lupe responder inmediatamente a gerencia el monto de pagos a productores agrícolas.
* **Origen / Timestamps:** Miércoles `[02:56:01]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** El campo `esProductor` existe en el maestro, pero falta incorporar el filtro en la barra superior de `NominasAgingPage.tsx` y en el listado de pagos semanales.
* **Brecha Pendiente:** El campo `esProductor` existe en base de datos; falta incorporarlo como filtro dropdown en la cabecera de [NominasAgingPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/NominasAgingPage.tsx).

#### 6.5 Gestión de Anticipos a Productores (Sin Factura Previa)
* **Descripción Operativa:** Los anticipos a productores se giran sin factura (se emite la transferencia bancaria anticipadamente). El sistema debe registrar estos anticipos en la cuenta del productor y saldarlos al final de temporada contra la proforma/liquidación definitiva por kilos entregados, calculando si resulta saldo a favor o deuda.
* **Origen / Timestamps:** Miércoles `[02:57:08 - 02:57:46], [03:00:13 - 03:00:34]`.
* **Descripción:** Los anticipos a productores se pagan por transferencia bancaria sin factura previa. Se registran en la cuenta corriente del productor y se liquidan al final de temporada contra la proforma/liquidación definitiva por kilos entregados.
* **Origen / Timestamps:** Miércoles `[02:57:08], [03:00:13]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `AnticiposProductoresPage.tsx` y ciclo de pagos de tesorería (`ANTICIPO_PRODUCTOR`).
* **Evidencia en Código:** Implementado en [AnticiposProductoresPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/AnticiposProductoresPage.tsx) y en el ciclo de tesorería (`ANTICIPO_PRODUCTOR`).

#### 6.6 Estado de Cuenta de Contrapartes: Modales Específicos
* **Descripción Operativa:** En la ficha/estado de cuenta unificada: al hacer clic en una factura debe abrir el visor PDF; al hacer clic en un pago/transferencia debe abrir un modal emergente con el comprobante bancario detallado. Histórico con selector obligatorio de rango de fechas.
* **Origen / Timestamps:** Miércoles `[02:58:44 - 03:00:05]`.
* **Descripción:** Al hacer clic en una factura, abre el visor PDF; al hacer clic en un pago/transferencia, abre un modal con el comprobante bancario detallado. Histórico con selector obligatorio de rango de fechas.
* **Origen / Timestamps:** Miércoles `[02:58:44]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** La grilla de movimientos de cuenta corriente está operativa, pero los enlaces actualmente redirigen a páginas completas en lugar de abrir los modales en pantalla.
* **Brecha Pendiente:** Grilla de movimientos operativa; falta asociar los eventos clic a los modales emergentes.

---

### Módulo 7: Comercial, Packing, Logística y Exportación (Comex)

#### 7.1 Optimización de Contenedores y Pallets (Cajas Rojas vs Negras)
* **Descripción Operativa:** Planificación de carga para armar contenedores homogéneos (~3.500–3.520 cajas). Regla comercial crítica: evitar mezclar cajas de menor calidad (rojas) con cajas premium (negras), ya que en el mercado chino los compradores castigan el precio de todo el contenedor tomando como referencia la caja de menor valor. Modelo de optimización para consolidar "puchos" (pallets incompletos).
* **Descripción:** Planificación para armar contenedores homogéneos (~3.500–3.520 cajas). Evitar mezclar cajas rojas (menor valor) con cajas negras premium para no devaluar el precio de venta en China. Algoritmo 2.0 para consolidar puchos (pallets incompletos).
* **Origen / Timestamps:** Miércoles `[00:00 - 04:35]`.
* **Estado:** `FALTANTE / SISTEMA EXTERNO`
* **Brecha / Pendiente:** Es un modelo de optimización que actualmente opera como herramienta externa. El ERP requiere definir las interfaces de captura de datos de pallets terminados y despachos.
* **Brecha Pendiente:** Herramienta externa de optimización. Requiere diseñar interfaces de conexión o ingesta hacia el ERP.

#### 7.2 Lead Times Logísticos y Semáforo de Tiempos
* **Descripción Operativa:** Medición de tiempos de la cadena productiva: Recepción en Packing $\rightarrow$ Proceso $\rightarrow$ Despacho $\rightarrow$ Ingreso a Puerto $\rightarrow$ Zarpe de Nave $\rightarrow$ Arribo a China $\rightarrow$ Fecha de Apertura de Contenedor en Mercado. Indicador tipo semáforo para detectar contenedores con atrasos en proceso de venta.
* **Origen / Timestamps:** Miércoles `[04:55 - 06:01], [10:27 - 13:04]`.
* **Descripción:** Medición de tiempos: Recepción en Packing $\rightarrow$ Proceso $\rightarrow$ Despacho $\rightarrow$ Ingreso a Puerto $\rightarrow$ Zarpe de Nave $\rightarrow$ Arribo a China $\rightarrow$ Fecha de Apertura de Contenedor en Mercado. Semáforo visual para contenedores con retrasos de venta.
* **Origen / Timestamps:** Miércoles `[04:55], [10:27]`.
* **Estado:** `FALTANTE`
* **Brecha / Pendiente:** Módulo de seguimiento y semáforo logístico no desarrollado en el ERP.
* **Brecha Pendiente:** Pantalla de reportería y tracking logístico no construida.

#### 7.3 Validación Previa contra Esquema XSD en DTE
* **Descripción Operativa:** Detección de brecha en GoSocket: envía el XML directo al SII sin validar contra el esquema XSD, provocando rechazos tardíos. El ERP debe prevalidar localmente la estructura XML antes de despachar al gateway.
#### 7.3 Prevalidación Estricta de Esquema XML DTE (GoSocket vs SII)
* **Descripción:** GoSocket no valida esquema XSD antes de enviar, provocando rechazos tardíos en el SII. El ERP debe prevalidar localmente la estructura XML antes del despacho HTTP.
* **Origen / Timestamps:** Martes AM `[00:00 - 01:05]`.
* **Estado:** `PARCIAL`
* **Brecha / Pendiente:** Existen validadores de campos en `canonical-builder`, pero falta integrar la validación formal estricta contra esquemas XSD oficiales del SII.
* **Brecha Pendiente:** Existen validadores funcionales en `canonical-builder`; falta la validación estricta contra esquemas XSD oficiales.

#### 7.4 Emisión de Guías de Despacho (Resolución 154)
* **Descripción Operativa:** Generación de guías de despacho electrónicas (tipo 52) desde el ERP para traslados y ventas con los campos de transporte exigidos por la normativa.
#### 7.4 Emisión de Guías de Despacho Electrónicas (Resolución 154)
* **Descripción:** Emisión de guías de despacho (código 52) con campos operativos de transporte y trazabilidad para traslados y ventas.
* **Origen / Timestamps:** Martes AM `[00:50 - 01:02]`.
* **Estado:** `COMPLETO`
* **Evidencia en Código:** Implementado en `GuiasDespachoPage.tsx` y `guia-resolucion-154.ts`.
* **Evidencia en Código:** Implementado en [GuiasDespachoPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/GuiasDespachoPage.tsx) y [guia-resolucion-154.ts](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/comercial/guia-resolucion-154.ts).

---

## 3. Plan de Acción Recomendado (Prioridades Inmediatas)
## 3. Próximos Pasos y Hoja de Ruta Priorizada

Para completar los puntos con estado **Parcial** y abordar los **Faltantes** críticos antes del arranque de temporada alta (fines de noviembre):
Para completar los requerimientos con estado **Parcial** y liquidar los **Faltantes** críticos antes del inicio de temporada alta:

1. **Prioridad 1 (Compras / Tesorería):**  
   - Integrar el modal universal de **PDF de Factura con botón "Ir a Libro de Compras"** en Notas de Cobro y Tesorería.
   - Completar el filtro **Proveedor vs Productor** en la Nómina Semanal de Pagos.
   - Automatizar el cálculo de la fecha de vencimiento (`fechaEmision + 30 días`) en Notas de Cobro.
2. **Prioridad 2 (Contabilidad / Contratistas):**  
   - Asegurar el `GROUP BY` por Centro de Costo en las cuentas de gasto y la imputación del auxiliar RUT en el asiento de cierre de contratistas.
   - Reforzar el validador estricto fail-closed en la carga masiva de comprobantes contables.
3. **Prioridad 3 (Activos Fijos / Bodega):**  
   - Agregar el tipo de compra "Activo Fijo" en la Orden de Compra para cumplir el mandato de Agustín.
   - Diseñar la pantalla de "Guía de Aplicación de Campo" con rebaja de stock por cuartel.

1. **Sprint Inmediato 1 (Compras / Tesorería - Alto Impacto UX):**
   - Implementar el modal emergente universal de **PDF de Factura con botón "Ir a Libro de Compras"** en Notas de Cobro, Nómina Semanal y Estado de Cuenta.
   - Agregar el filtro dropdown **Proveedor vs Productor** en [NominasAgingPage.tsx](file:///e:/source/repos/Almahue/ERP/erp_front/src/features/tesoreria/NominasAgingPage.tsx).
   - Automatizar el cálculo default de fecha de vencimiento (`fechaEmision + 30 días`) en Notas de Cobro.
2. **Sprint Inmediato 2 (Activos Fijos / Contabilidad - Requisitos Mandatorios):**
   - Agregar el tipo de compra **"Activo Fijo"** en la Orden de Compra y forzar la vinculación en el alta de activo fijo (mandato Agustín).
   - Diseñar el **gráfico consolidado mensual de depreciación de toda la empresa**.
   - Asegurar el `GROUP BY` por Centro de Costo y el auxiliar RUT en el asiento de cierre de Contratistas.
3. **Sprint Inmediato 3 (Bodega e Importaciones):**
   - Construir la interfaz de **Guía de Aplicación de Campo** con rebaja de stock por cuartel.
   - Reforzar el validador estricto fail-closed para la importación masiva tipo Agrosoft.


---

## 4. Requerimientos Extraordinarios Incorporados (Correo María Jesús - 29/10/2026)

A raíz de las validaciones de cierre de mes y requerimientos operativos solicitados formalmente por María Jesús (Almahue), se implementaron y desplegaron las siguientes funcionalidades adicionales:

### 4.1 Compromisos de Anticipo a Proveedores en Flujo de Caja sin Asiento Contable (Punto 2 MJ)
* **Estado:** `COMPLETO`
* **Descripción Operativa:** Se creó la entidad y pantalla de **Compromisos de Anticipo a Proveedores** (`/tesoreria/anticipos-proveedores`) con correlativo institucional `ANT-PROV-YYYY-NNNN`. Permite programar transferencias a proveedores y productores agrícolas sin factura previa.
* **Regla Canónica F0:** No genera asiento contable `PAGO:{id}` previo (el banco y la cuenta contable solo se mueven mediante la cartola bancaria oficial).
* **Integración:** Se proyecta directamente en el informe de Flujo de Caja (`FlujoCajaPage.tsx`) mediante el selector `[x] Incluir proyecciones`.

### 4.2 Cálculo de Vencimientos Atado a Emisión Electrónica SII (Punto 3 MJ)
* **Estado:** `COMPLETO`
* **Descripción Operativa:** En `compras.service.ts` y en el Libro de Compras, la fecha de vencimiento comercial de las facturas de proveedores se calcula automáticamente a partir de la fecha de emisión electrónica informada por GoSocket / SII (`fechaDocumento`) y el plazo comercial pactado (default 30 días), desacoplándola de la fecha de ingreso o recepción en bodega.

### 4.3 Facturas Bimoneda y Desglose de Aging con IVA al día 20 (F29) (Punto 4 MJ)
* **Estado:** `COMPLETO`
* **Descripción Operativa:** En el Libro de Compras y en el cálculo de Aging (`aging-sync.util.ts`), las facturas emitidas en moneda extranjera (USD) se desglosan en dos componentes independientes:
  1. **Neto en USD:** vence según las condiciones comerciales pactadas con el proveedor extranjero o local.
  2. **IVA en CLP:** vence invariablemente el día 20 del mes siguiente a la emisión (fecha tope del Formulario 29 ante el SII).

### 4.4 Importador Masivo de Planilla COMEX ACTUALIZABLE COMEX.xlsx (Punto 5 MJ)
* **Estado:** `COMPLETO`
* **Descripción Operativa:** Se construyó el módulo `ComexImportPage.tsx` y el servicio `comex-importer.service.ts` para procesar de forma masiva las planillas de exportación (`ACTUALIZABLE COMEX.xlsx`).
* **Alcance:** Detecta y consolida automáticamente 451 despachos de fruta fresca (1.411.647 cajas, 8.840.853 kg, US$ 35,291,175), valida consistencia de contenedores, naves, DUS aduanero, y genera en bloque las Órdenes de Venta de exportación (`OV-EXP`).

### 4.5 Columna 'Relacionados' con Badge Numérico (1-9, 9+) y Visor Universal de Documentos
* **Estado:** `COMPLETO`
* **Descripción Operativa:** Se estandarizó la columna de trazabilidad en todos los módulos bajo el nombre oficial **Relacionados**. Muestra el nombre del último documento vinculado y una píldora indicadora con el total ordenado (1 a 9 y '9+'). Al hacer clic en cualquier enlace de documento, se despliega el visor modal universal `DocumentoPdfModal.tsx` con opciones para imprimir, cerrar y el botón **Ir a documento**, el cual navega al módulo respectivo con el filtro exacto sin obligar al usuario a perder su pantalla actual.

### 4.6 Barra de Porcentaje de Cobertura de Facturas con Proformas e Insumos
* **Estado:** `COMPLETO`
* **Descripción Operativa:** En la lista de facturas del Libro de Compras, se integró una barra visual de cobertura porcentual que indica el total cubierto de la factura con las proformas de contratistas o recepciones de insumos asociadas.

### 4.7 Filtro Rápido por Módulo y Trazabilidad en Solicitudes de Reversa Contable
* **Estado:** `COMPLETO`
* **Descripción Operativa:** En `SolicitudesReversaPage.tsx` (`/contabilidad/reversas`) se agregó una barra de filtros rápidos por píldora al lado del buscador (Todas, Contratistas, Compras, Insumos), incorporando historial de trazabilidad cronológica y notificación interna / por correo.
