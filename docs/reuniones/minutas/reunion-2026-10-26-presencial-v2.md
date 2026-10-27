# Reunion presencial Almahue - 26/10/2026 (minuta v2.0)

Documento consolidado para implementacion. Cruza dos audios de celular (manana reparado + tarde reparada con untrunc), Whisper `large-v3`, y apuntes del consultor (`revision en cliente.txt`).

| Fuente | Archivo | Duracion aprox. | Transcripcion |
|---|---|---|---|
| Manana | `26-10-2026 12.33.m4a` | 01:24:40 | [`transcripcion-2026-10-26-presencial.md`](../transcripciones/transcripcion-2026-10-26-presencial.md) |
| Tarde | `26-10-2026 15.20 REPARADO.m4a` | ~01:54 (untrunc) | [`transcripcion-2026-10-26-presencial-tarde.md`](../transcripciones/transcripcion-2026-10-26-presencial-tarde.md) |

**Sala:** Maria Jesus (MJ), equipo Almahue (demo: Carlos/Sergio). Cliente operativo (Fran, Lupe u otros) en tramos de tesoreria. ASR no separa hablantes: reglas de negocio atribuidas a **MJ** cuando el contenido coincide con Agrosoft o decision explicita.

**Prioridad de evidencia:** transcripcion > esta minuta > apuntes manuscritos.

---

## 1. Contabilidad y reportes

### 1.1 Resultado del ejercicio y situacion financiera (MJ, manana `[00:19]`-`[02:03]`)

- El **estado de resultados** de un mes (ej. enero) muestra **solo ese mes**.
- El **resultado del ejercicio** del ano anterior **pasa el 31/12** al **estado de situacion financiera** como **resultado acumulado**.
- En situacion financiera deben coexistir **resultado del ejercicio** y **resultado acumulado**; si falta uno, el cuadro no cierra.
- Pendiente en ERP: replicar en reporteria lo explicado en sala (tus apuntes: balance y EERR solo ano en curso; situacion financiera con anos anteriores; mayor con saldo entre anos; filtros mes/ano y **Todos** = solo ano actual; ancho del selector de cuentas en mayor).

### 1.2 Comprobantes y carga masiva (manana `[06:55]`-`[17:09]`)

- **Plantilla tipo Agrosoft** (restrictiva): correlativo (= lineas del comprobante), **tipo** (ej. traspaso desde contabilidad), fecha, periodo, TC, cuenta, dimensiones segun parametrizacion de la cuenta (planta, CC, area, auxiliar, referencia, vencimiento, montos CLP/USD, glosa).
- Si la cuenta exige CC (ej. packing) y falta, **no contabilizar** esa linea.
- Validaciones antes de grabar: periodo vs fecha; debe = haber en CLP y USD. Si falla, **no cargar el lote** (fail-closed); corregir archivo y reintentar.
- MJ prefiere **formato unico obligatorio** frente a Excel abierto (evita que operadores omitan CC). Carlos deja puerta a mapeo de columnas en configuracion a futuro, con campos obligatorios igualmente enforced.
- Configuracion persistente: vincular columna Excel (ej. periodo en columna P) a campo ERP; una vez definida, se reutiliza.
- MJ ofrece enviar archivos de carga y cruce con plan de cuentas; **validar carga historica con Mario** (apunte consultor).

### 1.3 Tipos de comprobante, correlativo y estado (apuntes consultor; parcial manana)

- Tipos origen: **apertura, egresos, ingresos, proveedores, traspasos, ventas**; nomenclatura en identificador; tipo manual al crear desde contabilidad; automatico si viene de otro modulo.
- **Nuevo comprobante en estado contabilizado** al guardar (apunte; no reforzado en transcripcion).
- Adjuntar **RC**, detalle en **tres columnas**, regularizar botones de glosa, motivo en cierre/apertura de periodo, TC manual + aviso a administrador si falta TC del dia (apuntes; ver contratistas tarde para flujo reverso/apertura).

### 1.4 Periodo, reverso y apertura (tarde `[01:07]`-`[01:17]` y siguientes)

- Cierre de mes contable: tras contabilizar, **cerrar periodo** para bloquear edicion.
- Para corregir: **reversar comprobante** en contabilidad, luego **abrir mes** (hoy analistas no reversan traspaso de cierre; lo hace contabilidad).
- **Solicitud de apertura** desde el modulo origen (proforma, factura con OC, etc.) con **motivo**; notificacion a contabilidad; bandeja de solicitudes de reverso; click lleva al **asiento** con boton **Reversar**; trazabilidad en el asiento (quien solicito, quien reverso).
- Abrir periodo en un modulo (ej. contratistas) **impacta compras, ventas, insumos** (bodega): definir reglas por modulo al liberar.
- Si proforma ya tiene **factura asociada**, hay que **reversar factura en compras/contabilidad** antes de editar proforma o ingresos diarios.
- **Edicion acotada** sin reverso total: si solo cambia imputacion no monetaria (labor, cuartel) y **sin factura asociada**, evaluar flujo de **solicitud de modificacion** (antes/despues) con aprobacion de jefatura; si hay factura o montos, flujo completo de reverso.
- Anulados/reversados: no deben distorsionar reportes operativos; mantener historial y observacion (motivo).

---

## 2. Parametrizacion y plan de cuentas

### 2.1 Dimensiones N:N por cuenta (manana `[22:15]`-`[25:59]`, aprobado)

- Por cuenta imputable: listas de **centros de costo**, **elementos de costo** y **areas de negocio** (agregar/quitar N).
- Al usar la cuenta en OC, asientos o carga, solo se ofrecen dimensiones ligadas.
- UI sugerida: tres columnas con agregar/quitar; contador en mantenedores de CC/elemento/area (**cantidad de cuentas** asociadas; detalle al clic). Vista maestra desde la **cuenta**; el contador inverso es apoyo.
- **Centro** mas transversal (ej. cerezas); **elemento** mas detalle por departamento/operacion (DUS, certificados). **No** fijar elemento a centro de forma rigida.
- Comex/logistica envian por temporada mapeo area / CC / elemento; al elegir logistica, solo elementos de logistica.
- **Planta** y **variedad**: no usan planta; variedad dejar en maestro por si acaso (tarde `[03:39]`-`[04:10]`). Lista de flags Agrosoft revisada en contratistas (TLT, especie, codigo financiero, etc.).

### 2.2 Historial de parametrizacion (tarde `[48:40]`-`[50:18]`; apunte consultor)

- **Historial por modulo** (piloto en contratistas): accion, **antes / despues** legible, fecha, usuario.
- Metadatos tecnicos de BD: solo para **soporte** (menu restringido o envio a soporte), no para usuario final.
- Replicar patron al resto de modulos (resuelve "historial de parametrizaciones no funciona" de tus apuntes).

### 2.3 Bancos (apunte consultor)

- Varias **cuentas por banco**, cada una con **moneda**. No aparece en transcripciones; mantener como requisito hasta validar con cliente.

### 2.4 Usuarios y empresas

- Selector **dos empresas** (apunte ok; corregido en ERP 26/10).

---

## 3. Presupuesto y responsabilidad por area (manana)

- Sin imputacion correcta (CC/elemento), el **presupuesto no sirve**.
- Meta operativa 2026: quien aprueba OC define **cuenta y elemento**, no solo monto (hoy muchas areas solo aprueban documento).
- Ejemplo VINs: confeccion vs arriendo mal imputado distorsiona seguimiento.
- **Alerta por porcentaje** en totalizados (apunte consultor; no dicho en audio).
- **CC agrupados por departamento** con totalizados arriba (apunte; no detallado en audio).

---

## 4. Orden de compra y compras (manana)

- Orden en linea: **cuenta contable** > **centro de costo** > **elemento**; sin cuenta, bloquear CC y elemento.
- Multiples imputaciones: **varias lineas** (misma cuenta, distinto CC/elemento) preferido por MJ; division por **monto** en casos excepcionales (software TI/contabilidad).
- Si CC/elemento no esta en lista de la cuenta: **solicitar al administrador** (motivo, usuario, cuenta); no agregar libre en OC.
- **Detalle** en ERP estilo **flujo de caja** / arbol (cuenta y desglose); MJ quiere ver CC en vista principal, no solo "segunda hoja".
- **PDF proveedor**: hoja oficial **sin** dimensiones contables; detalle contable solo en sistema; opcion export con detalle interno.
- Ideal: todo nace en **OC**; hoy a veces se corrige en factura.

### 4.1 Documentos no cubiertos en audio (apuntes)

- **Boleta de honorarios**: registro y recepcion; no emision; tipo en proveedor.
- **Nota de cobro**: rendicion de gastos; compras + contabilidad; facturas electronicas.
- **OPB / embarcador**: paga facturas export/import; Almahue ingresa detalle; OPB como intermediario.

---

## 5. Contratistas (tarde, bloque principal)

### 5.1 Parametrizacion y maestros

- Parametrizacion dentro del modulo; listado de contratistas en el mismo modulo.
- Maestros: labores (codigo/nombre), actividades, sectores, faenas, creditos.
- **Actividad manda**: una actividad tiene muchas labores; asociacion **desde actividad hacia labores** (invertir UI actual que asocia desde labor).

### 5.2 Ingreso diario y proformas

- **Ingreso diario**: contratista, CC, labor/actividad, predio opcional, temporada/sector/faena desde parametrizacion, horas x precio (jornada vs trato).
- **Cadena de aprobacion en proforma**, no en cada ingreso diario (ingreso diario diario es operacion frecuente; aprobar cada uno es lento).
- Vista de cierre: bloque que **entra al cierre** (borde verde) vs bloques **informativos** (proformas borrador / ingresos sin proforma).
- Proforma: agrupa muchos ingresos diarios; boton **seleccionar todos** del proveedor con cuidado en periodos largos (quincenal).
- **Origen/cadena** en proforma debe listar ingresos diarios asociados.
- Vincular contratista con **proveedor de compras** para asociar facturas.
- Listado proformas: **aprobadas** y **facturadas** visibles; lo que centraliza es lo del bloque verde.

### 5.3 Centralizacion y compras

- Al **aprobar proforma** se reconoce gasto (mano de obra contratista vs facturas por recibir contratistas).
- **Centralizar** genera **un asiento** con todas las proformas del periodo.
- En **libro compras**, factura del contratista cancela puente; gasto del mes ya reconocido en contratistas (factura puede caer mes siguiente).
- Editar ingreso diario en periodo cerrado: permisos como OC; resumen de ingresos sin proforma a fin de mes.

### 5.4 Traspaso contable, glosa y reportes

- Traspaso/cierre contratistas: cuentas configurables (guardar predeterminadas); **glosa** con plantillas y detalle editable.
- Reporte ingresos: totalizados arriba; drill-down a ingresos diarios; orden sugerido **proforma** luego **ingreso** (ingreso mas detallado).
- Notificaciones internas/correo desde listados (ej. proforma en borrador); componente unico de notificaciones en todo el ERP; limite anti-spam.

### 5.5 Permisos de edicion y factura en proforma

- No asociar factura a proforma si el flujo no corresponde (validacion; error ingreso vs aprobacion).
- Modificaciones de CC dentro del mes posibles sin esperar mes siguiente; errores graves via reverso.

---

## 6. Tesoreria (manana `[01:02]`-`[01:09]`)

- Cartola: formato debe ser **descarga directa del banco** (Lupe confirma).
- Limitaciones de acceso ejecutivo Banco Chile; evaluar servicios del banco vs operacion interna.

---

## 7. Anexo A - Puntos que NO anotaste (y si estan en las transcripciones)

Estos temas salen en audio y **no** estan (o estan muy incompletos) en `revision en cliente.txt`:

| # | Tema | Donde |
|---|---|---|
| A1 | **Modulo contratistas completo** (parametrizacion, ingreso diario, proforma, centralizacion, compras puente) | Tarde |
| A2 | **Actividad > labor** (asociacion al reves de la UI actual) | Tarde `[05:29]`-`[06:09]` |
| A3 | **Aprobacion en proforma**, no en ingreso diario | Tarde `[23:28]`-`[24:11]` |
| A4 | **Bloques cierre**: verde = al asiento; gris = informativo | Tarde `[24:54]`-`[51:36]` |
| A5 | **Historial parametrizacion** UX: antes/despues, sin metadatos al usuario; piloto contratistas | Tarde `[48:40]`-`[50:18]` |
| A6 | **Flujo solicitud apertura de mes + reverso** con notificaciones y link al asiento | Tarde `[01:10]`-`[01:15]` |
| A7 | **Apertura de periodo impacta todos los modulos** (compras, ventas, insumos) | Tarde `[01:23]`-`[01:24]` |
| A8 | **Cadena proforma > factura > reverso** para poder editar | Tarde `[01:24]`-`[01:29]` |
| A9 | **Solicitud de modificacion** con antes/despues y aprobacion (sin reverso si solo texto/imputacion menor y sin factura) | Tarde `[01:36]`-`[01:42]` |
| A10 | **Solicitud de reverso desde el documento** (proforma, factura/OC), no solo desde cierre periodo | Tarde `[01:33]`-`[01:35]` |
| A11 | **No reversar mes intermedio** si meses posteriores cerrados (reversar en cascada hasta el mes objetivo) | Tarde `[01:30]`-`[01:31]` |
| A12 | **Debates carga masiva**: fail-closed total vs reporte de lineas rechazadas; mapeo columnas Excel | Manana `[08:47]`-`[12:33]` |
| A13 | **Comex/logistica**: archivo temporada CC + elemento por area | Manana `[26:34]`-`[27:19]` |
| A14 | **Area de negocio** posiblemente mal cargada en Excel actual | Manana `[20:03]` |
| A15 | **Eliminar uso de planta**; variedad opcional | Tarde `[03:39]` |
| A16 | **Notificaciones** desde listados (proforma borrador) y limite de envios | Tarde `[51:54]`-`[53:26]` |
| A17 | **Reporte ingresos contratistas**: totalizados y drill-down; orden proforma / ingreso | Tarde `[53:40]`-`[59:44]` |
| A18 | **Glosa traspaso cierre** contratistas configurable | Tarde `[01:02:28]` |
| A19 | **Cartola**: confirmacion descarga directa banco | Manana tarde `[01:09:29]` |
| A20 | **Software 50% TI / 50% contabilidad** en una factura (lineas o montos) | Manana `[33:42]`-`[35:17]` |
| A21 | **VINs confeccion vs arriendo** (ejemplo presupuesto) | Manana `[28:19]`-`[28:48]` |

---

## 8. Anexo B - Lo que anotaste y no aparece en las transcripciones

Validar con MJ/Mario (puede ser otra conversacion, no grabada, o pendiente de tarde perdida en telefono):

- Boleta de honorarios y recepcion (sin emision).
- Nota de cobro / rendicion y OPB embarcador.
- Parametrizacion bancos (multi-cuenta y moneda).
- Comprobante **contabilizado** al crear manualmente.
- RC adjunto, detalle asiento **3 columnas**, botones glosa.
- Filtros libro mayor/diario/balance 8 columnas y reglas de ano (salvo resultado ejercicio, parcialmente en manana).
- Alerta presupuesto por **porcentaje**.
- CC por **departamento** con totalizados.

---

## 9. Siguiente paso sugerido (post-validacion)

1. MJ confirma Anexo B (honorarios, nota cobro, OPB, bancos).
2. Priorizar: plan N:N en prod, carga masiva Agrosoft, reporteria resultado ejercicio/acumulado, OC (orden + solicitud admin + detalle + PDF), contratistas (actividad-labor, aprobacion proforma, centralizacion, apertura/reverso).
3. Diagrama de flujo reverso/apertura multi-modulo (pedido explicito en tarde `[01:25:35]`).

**Plan de trabajo (solo apuntes consultor + items acordados):** [`../../requerimientos/PLAN-IMPLEMENTACION-MODULOS-2026-10-26.md`](../../requerimientos/PLAN-IMPLEMENTACION-MODULOS-2026-10-26.md). Balances MJ: [`../compartidos/mj-2026-10-26/`](../compartidos/mj-2026-10-26/).

---

## Referencias

- Contraste previo: [`../../requerimientos/contraste-minuta-revision-cliente-2026-10-26.md`](../../requerimientos/contraste-minuta-revision-cliente-2026-10-26.md) (actualizar tras esta v2).
- Minuta v1: [`reunion-2026-10-26-presencial.md`](reunion-2026-10-26-presencial.md)
