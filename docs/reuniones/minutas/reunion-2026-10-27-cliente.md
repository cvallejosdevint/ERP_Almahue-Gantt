# Reunión Presencial Almahue — 27/10/2026 (Minuta Consolidada AM y PM)

Documento consolidado para desarrollo e implementación basado en las dos sesiones de trabajo de sala del 27 de octubre de 2026 (Mañana y Tarde), procesadas con Whisper `large-v3` en CUDA float16 y normalización de léxico ERP.

| Sesión | Fuente Audio | Duración | Transcripción | Minuta Detallada |
|---|---|---|---|---|
| **Sesión AM (Mañana)** | `27-10-2026 12.11 (1).m4a` | 01:18:10 | [`transcripcion-2026-10-27-reunion.md`](../transcripciones/transcripcion-2026-10-27-reunion.md) | [`reunion-2026-10-27-am-cliente.md`](reunion-2026-10-27-am-cliente.md) |
| **Sesión PM (Tarde)** | `27-10-2026 15.24.m4a` | 01:47:50 | [`transcripcion-2026-10-27-reunion-tarde.md`](../transcripciones/transcripcion-2026-10-27-reunion-tarde.md) | [`reunion-2026-10-27-pm-cliente.md`](reunion-2026-10-27-pm-cliente.md) |

**Participantes:**  
* **Almahue:** María Jesús (MJ), Fran, Lupe, Mario. Actor clave del flujo de compras/contratos: José Tomás.
* **Devint (ERP):** Carlos, Sergio.

---

# PARTE I: SESIÓN AM (MAÑANA / MEDIODÍA)

## 1. Facturación Electrónica (DTE) y Guías de Despacho `[00:00 - 01:05]`
* **GoSocket y esquema DTE:** Los proveedores tradicionales validan contra esquema XSD antes del envío al SII; GoSocket transmite sin filtro previo y el rechazo ocurre en el SII, alargando el reproceso.
* **Guías de despacho:** Se evaluará en las próximas semanas la emisión directa desde el ERP con campos agrícolas específicos.

## 2. Plan de Cuentas en Servidor de Pruebas `[01:03 - 02:15]`
* El equipo Almahue aprueba la simpleza visual y operatividad del nuevo diseño del plan de cuentas en el servidor nuevo de pruebas.

## 3. Contratistas: Roles, Centralización y Asiento de Cierre `[44:20 - 48:09, 56:11 - 57:40, 01:11:15 - 01:13:50]`
* **Roles:** José Tomás (Jefe Abastecimiento) administra contratos, emite y aprueba la proforma. Contabilidad (Fran / Lupe / Mario) calza la factura de compra recibida verificando RUT y monto.
* **Mecánica Contable del Cierre de Contratistas:**
  1. *Cierre de Contratistas (Devengo del gasto):*  
     $$\text{Debe: Gasto Mano de Obra (agrupado por Centro de Costo)} \quad/\quad \text{Haber: Facturas por Recibir Contratistas (con Auxiliar)}$$
  2. *Factura en Libro de Compras (Extinción de provisión):*  
     $$\text{Debe: Facturas por Recibir Contratistas} \quad+\quad \text{Debe: IVA Crédito Fiscal} \quad/\quad \text{Haber: Proveedores por Pagar}$$
* **Requerimientos de Grilla:** El asiento agrupa por Centro de Costo en cuentas de gasto, pero exige registrar el **Auxiliar (RUT Proveedor)** en *Facturas por Recibir Contratistas* para el análisis de cuentas corrientes.

## 4. Reversas en Mes Abierto vs Ajustes en Mes Cerrado `[48:10 - 56:45, 58:00 - 01:06:40]`
* **Mes Abierto (No Centralizado):**  
  Contabilidad desvincula factura $\rightarrow$ Proforma pasa a estado **`REVERSADA`** (distinguible de `PENDIENTE`) $\rightarrow$ José Tomás o Admin Concepto con PIN habilita edición $\rightarrow$ Vuelve a pasar por el flujo de aprobación $\rightarrow$ Re-calce con factura.
* **Mes Cerrado (Centralizado):**  
  **NO reabrir ni desarmar la centralización completa** del mes para no ensuciar mayores. Se emite un **Comprobante de Ajuste puntual** (Ajuste/Traspaso) con **doble aprobación** (Abastecimiento + Contabilidad) e historial visible en la línea.

---

# PARTE II: SESIÓN PM (TARDE)

## 5. Auditoría e Historial por Módulo `[00:00 - 02:40]`
* Auditoría descentralizada por módulo (Contratistas, Insumos/Bodega, Activo Fijo, Contabilidad).
* Visibilidad restringida a Jefatura de Área y Contabilidad.
* En Insumos y Bodega los ajustes son mínimos al sustentarse en órdenes de consumo automáticas de packings y guías de recepción físicas.

## 6. Balance de 8 Columnas `[04:20 - 09:20]`
* Cadena de reportería: Libro Diario $\rightarrow$ Libro Mayor $\rightarrow$ Balance 8 Columnas $\rightarrow$ Estados Financieros.
* Cuadre de 8 columnas: Sumas (Debe/Haber), Saldos (Deudor/Acreedor), Inventario (Activo/Pasivo) y Resultados (Pérdida/Ganancia).
* Diferencia Ganancia - Pérdida = Resultado del Ejercicio (cuadra con Activo - Pasivo). Periodo acumulado 1 de enero a la fecha de corte.

## 7. Notas de Cobro: Embarcadores (OPB) y Asoex `[15:17 - 23:00, 29:30 - 43:00, 45:30 - 54:00]`
* **Caso 1: Embarcadores (OPB) - Facturas pagadas por cuenta de Almahue (98% de notas de cobro):**  
  El embarcador paga facturas de terceros a nombre de Almahue y emite una Nota de Cobro con planilla Excel adjunta.  
  - *Efecto contable:* Saldar las facturas de proveedores originales y reconocer la deuda contra OPB:  
    $$\text{Debe: Proveedores por Pagar (Proveedor original de cada factura)} \quad/\quad \text{Haber: Proveedores por Pagar (OPB - Nota de Cobro)}$$  
  - Las facturas originales quedan bloqueadas contra pago directo en Tesorería.  
  - En Compras: crear pantalla de Notas de Cobro que permite carga masiva de Excel con prevalidación estricta (verificar existencia de facturas y cuadre 100% de montos).
* **Caso 2: Asoex - Gasto Directo (2% de notas de cobro):**  
  Gasto directo exento por comisión de exportación. Ingreso directo por módulo de Proveedores:  
  $$\text{Debe: Gasto Comisión Comité / Exportación} \quad/\quad \text{Haber: Proveedores por Pagar (Asoex)}$$

## 8. Activos Fijos y Órdenes de Compra (Requisito de Agustín) `[24:00 - 28:50]`
* **Instrucción de Agustín:** Toda compra de activo fijo debe nacer desde una **Orden de Compra (OC)**.
* Agregar tipo de compra **Activo Fijo** en el formulario de OC de Compras.
* Vincular la ficha del activo fijo con la OC aprobada/recepcionada.
* **Gráfica de depreciación:** Reemplazar el gráfico individual por un **gráfico consolidado mensual general** de depreciación de todos los activos (depreciación lineal fija).

## 9. Boletas de Honorarios: Códigos y Reglas de Notaría `[54:10 - 59:15, 01:01:30 - 01:06:30]`
* Códigos SII: **1001** (Electrónica con retención), **1002** (Exenta), **1003** (Retención 3% préstamo solidario).
* **Gastos Notariales / Legales (Dolores / Trinidad):** Solo se ingresan al ERP si cuentan con **Rendición de Gastos formal con comprobante de pago efectivo**. Las boletas sin rendir no se contabilizan para evitar pasivos ficticios.

## 10. Tesorería y Cartolas Bancarias `[01:09:20 - 01:11:40]`
* Mostrar el número de cuenta corriente en el mantenedor bancario y reportería de pagos.
* El importador de cartolas debe **discriminar movimientos preexistentes** para permitir cargas periódicas o diarias sin duplicar registros.

---

# PARTE III: CALENDARIO OPERATIVO Y PRÓXIMOS HITOS `[01:12:00 - 01:15:40]`

1. **Hito de Temporada Alta:** El volumen operativo fuerte inicia la **última semana de noviembre** (cosecha y embalaje).
2. **Prueba de Fuego en Modo Espejo:** Operación paralela del ERP durante el primer mes de temporada alta.
3. **Compromiso de Datos:** Contabilidad (Mario) debe entregar la base de movimientos contables del año 2026 para carga inicial en el ERP.
4. **Jornada de Pruebas Integrales:** Sesión presencial de **medio día completo** para validar el flujo punta a punta (ingreso diario $\rightarrow$ proforma $\rightarrow$ centralización $\rightarrow$ factura libro compras $\rightarrow$ pago $\rightarrow$ balance).
