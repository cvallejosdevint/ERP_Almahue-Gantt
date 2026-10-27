# Validacion de puntos dudosos (post reunion 26/10)

Fuentes: transcripciones `transcripcion-2026-10-26-presencial.md`, `transcripcion.md` (as-is Agrosoft), codigo ERP, apuntes consultor.

---

## 1.3 - Aprobacion OC y cuenta / elemento

**Tu lectura:** fue aclaracion, no un modulo nuevo; la imputacion ya va **por linea** en la OC.

**Evidencia reunion manana `[27:27]`-`[27:27]` (MJ):** hoy los jefes **solo aprueban el documento** (monto), no eligen cuenta ni elemento; la meta 2026 es que **cada area se haga cargo** de su imputacion para que el presupuesto cuadre.

**Evidencia ERP:** en `OrdenCompraWizardPage` cada linea tiene `cuentaContableId`, `centroCostoId`, `elementoCostoId` (orden cuenta > CC > elemento). Eso cubre **quien arma la OC**.

**Conclusion:** No hace falta un flujo aparte de "solicitud de imputacion en aprobacion" si la operacion acordada es: **quien crea/edita la OC** (o quien completa antes de enviar) define cuenta/CC/elemento por linea. El comentario de MJ apunta a **cambio cultural + que la bandeja muestre esas dimensiones** al aprobar, no a un formulario nuevo en Administracion. Opcional futuro: en bandeja aprobacion mostrar resumen CC/elemento por linea (sin editar si no se pidio).

---

## 1.5 - PDF / reporte al proveedor sin dimensiones

**Tu lectura:** es del **sistema actual (Agrosoft)**, no urgente en el ERP nuevo.

**Evidencia 26/10 manana `[50:24]`-`[53:30]`:** MJ describe la OC en Agrosoft con **dos hojas**: la primera es la orden "oficial" para el proveedor (**sin** centro de costo ni elemento, "no tiene sentido para el proveedor"); la segunda hoja trae el **detalle contable** (CC, elemento). Piden exportar PDF solo la primera hoja; el detalle queda en el sistema.

**Proceso as-is Agrosoft (Reu1 `transcripcion.md` ~`07:12`):** al crear OC se genera numero; el usuario revisa en pantalla; existe **informe orden de compra** y visualizacion tipo PDF al crear (deseo de mejora: que se abra al crear).

**En nuestro ERP:** no hay aun plantilla dual hoja1/hoja2 como Agrosoft. Tu apunte **C-4** (ver detalle estilo flujo de caja **en pantalla**) es el equivalente interno; **1.5 queda fuera de alcance** hasta que pidan paridad de impresion/envio a proveedor.

---

## 2.1 - Import plan vs matriz de permisos

**Tu lectura:** el import Excel **ya existe**; antes del cruce con archivos MJ falta el **panel lateral / slide** con permisos y listas N:N por cuenta (tus notas).

**Codigo:** `PlanCuentasPage` tiene carga masiva Excel + edicion por cuenta; se agrego vista **Matriz** y tres columnas con scroll en el modal. Falta refinamiento UX tipo **panel fijo a la derecha** al navegar la lista (tu "slide hacia el lado") si la matriz actual no alcanza.

**Orden:** parametrizar vinculos (P-1/P-8) > validar con MJ > import/cruce masivo (K-20 / Mario).

---

## 2.6 - Archivo temporada Comex / logistica

**Contexto conversacion (manana `[26:34]`-`[27:19]`):**

- Comex y logistica **cada temporada** envian un mapeo: que **area** corresponde, que **centro de costo** usan, que **elementos de costo** aplican.
- Ejemplo: si eliges **logistica**, el combo de elementos muestra solo los de logistica, no los de Comex (evita mezclar departamentos).
- Relacionado: cerezas vs otras frutas, centros mas generales en Comex y elementos mas detallados (DUS, certificados, etc.) `[22:23]`-`[30:36]`.

**No es** un import masivo del plan entero; es **carga estacional** que alimenta las listas N:N o filtros por area. **Opcional** despues de P-1.

---

## 2.8 - Factor de honorarios

**No se hablo el 26/10** (cierre manana `[01:08:36]`: "boleta de honorarios no lo vimos").

**Contexto previo:**

- Reu4 `transcripcion-reunion4.md` ~`09:00`-`09:05`: pantalla **factores de honorario** en parametrizacion; MJ explica que es el **% de retencion** que el SII va subiendo hacia 20%.
- Reunion cliente 22/10: MJ sugiere mover factor de honorarios a **Parametrizacion** (no modulo contabilidad suelto).

**No es glosa de asiento** en si; es **tabla maestra de porcentaje** usada al contabilizar/registrar boletas de honorarios. Competencia tipica: SAP B1 retencion prestadores, Defontana libro honorarios, Softland % actualizable por periodo. **Pendiente:** ubicar en Parametrizacion > Factor honorarios + flujo P-5 cuando retomen boletas.

---

## 2.9 - Honorarios, nota de cobro, OPB

**26/10:** honorarios **no se trataron** en sala (`[01:08:36]`). Lo de tus apuntes viene de **otras conversaciones** o operacion diaria, no de esa grabacion.

| Tema | Donde buscar mas contexto |
|---|---|
| Boleta honorarios | Apuntes consultor; Reu4 factor %; fin reunion 26/10 pendiente |
| Nota de cobro / rendicion | Solo apuntes consultor; no en transcripcion 26/10 |
| OPB embarcador | Solo apuntes consultor; Comex/export en Reu1 y 26/10 habla de **areas y OC**, no OPB por nombre |

**Implementacion:** mantener **P-5 a P-7 en espera**; proxima sesion con MJ/Mario: un ejemplo real (pantalla Agrosoft o papel) por cada documento.

---

## Referencia rapida PDF OC (1.5)

| Sistema | Donde | Que pasa |
|---|---|---|
| Agrosoft | Modulo compras > orden de compra > export / informe | Hoja 1 proveedor; hoja 2 dimensiones (26/10 MJ) |
| ERP Almahue (hoy) | Compras > OC wizard + listado | Sin PDF dual; detalle en lineas y (futuro) C-4 en pantalla |
