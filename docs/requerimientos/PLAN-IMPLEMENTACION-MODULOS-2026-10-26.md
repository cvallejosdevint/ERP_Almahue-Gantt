# Plan de implementacion - solo apuntes reunion 26/10/2026

Fuente principal: `revision en cliente.txt` (lo que anotaste en sala). Orden del menu ERP (`Sidebar.tsx`).

Complemento acordado contigo (audio tarde o refinamiento UI): seccion **Aplicamos ademas** al final de Parametrizacion y Administracion.

Al cierre: **lo que no anotaste** (sale en transcripciones / minuta v2, fuera de alcance hasta que lo valides).

Referencias balances MJ (reportes): [`docs/reuniones/compartidos/mj-2026-10-26/`](../reuniones/compartidos/mj-2026-10-26/).

---

## 1. Administracion

| # | Lo que anotaste | Estado / criterio |
|---|---|---|
| A-1 | Al crear usuarios solo aparecia una empresa aunque el usuario tiene dos | **Hecho** 26/10 (selector por empresas asignadas). |

### Aplicamos ademas (no estaba en el txt; si aplicas)

| # | Tarea | Criterio |
|---|---|---|
| A-2 | **Historial de parametrizacion** (1.6): accion, antes/despues legible, fecha, usuario; sin metadatos tecnicos al operador | Piloto Contratistas, luego Parametrizacion |
| A-3 | **Solicitud apertura de periodo y reverso** (1.7): desde modulo origen con motivo; bandeja contabilidad/admin; link al asiento con Reversar | Flujo tarde 26/10 |

---

## 2. Parametrizacion

### De tus apuntes

| # | Lo que anotaste | Criterio de aceptacion |
|---|---|---|
| P-1 | Plan de cuentas: asociar **N** centros de costo, **N** elementos y **N** areas de negocio **por cuenta** (listas para asociar) | **Tres columnas** (CC / elemento / area) con agregar y quitar por cuenta; en OC y asientos solo se ofrecen los asociados |
| P-2 | En CC, elemento de costo y area de negocio: columna con **cantidad de cuentas** del plan asociadas | Contador + detalle al clic |
| P-3 | Bancos: mas de una **cuenta por banco**; indicar **moneda** de cada cuenta | Ver **P-3b** (refinamiento tuyo) |
| P-4 | Revisar **historial de parametrizaciones** (no funciona) | Mismo patron que A-2 en mantenedores de catalogo (**P-4** = 2.10) |
| P-5 | Boleta de honorarios: registro y recepcion; **no** emision; tipo documento en proveedor | Pendiente diseno; ver explicacion **2.9** abajo |
| P-6 | Nota de cobro = rendicion de gastos; compras + contabilidad; facturas electronicas | Pendiente diseno; ver **2.9** |
| P-7 | OPB embarcador paga facturas export/import; Almahue ingresa detalle; OPB como intermediario | Pendiente diseno; ver **2.9** |

### Aplicamos ademas (refinamiento UI)

| # | Tarea | Criterio |
|---|---|---|
| P-3b | **Cuentas bancarias para transferencias** (tu 2.5): por banco, varias filas; **numero de cuenta** + **tipo** (default **cuenta corriente**); moneda por cuenta (de tus apuntes) | Catalogo bancos usable en tesoreria/pagos |
| P-8 | **Matriz plan de cuentas - permisos/requisitos por cuenta** (tu 2.2, no es reimportar el plan): lista de cuentas con **scroll vertical fijo en nombres/codigos**; a la derecha, rejilla de permisos/atributos (CC, elemento, area, auxiliar, etc.) con **scroll vertical y horizontal** | Editar que exige cada cuenta sin perder de vista la fila de la cuenta |
| P-9 | **Planta / variedad** (2.7): sin planta en operacion; variedad opcional en maestro | Tarde 26/10; alinear contratistas y parametrizacion |

**Nota:** el **plan de cuentas ya cargado** en ERP cubre el maestro; el trabajo pendiente es **P-1, P-2, P-8** (vinculos y UI), no volver a importar 397 cuentas salvo que falten cuentas vs Agrosoft.

---

## 3. Contratistas

*No hay lineas en `revision en cliente.txt`.*

---

## 4. Ventas

*No hay lineas en tus apuntes.*

---

## 5. Compras

| # | Lo que anotaste | Criterio |
|---|---|---|
| C-1 | Orden en linea OC: **cuenta > centro de costo > elemento** | Bloquear CC/elemento sin cuenta |
| C-2 | Si CC o elemento no esta asociado al plan de la cuenta: opcion en lista para **solicitar al administrador** agregarlo | Workflow con motivo; no alta libre en OC |
| C-3 | CC/elemento **por linea** (varias lineas si hay varios CC/elementos en un mismo item conceptual) | Multiples lineas de detalle |
| C-4 | **Ver detalle** imitando visualizacion de **flujo de caja** (arbol / desglose) | Pantalla detalle OC, no solo PDF |

*Tus apuntes tambien mencionan honorarios / nota de cobro en compras (ver P-5, P-6, P-7).*

---

## 6. Insumos / Bodega

*No hay lineas en tus apuntes.*

---

## 7. Activo fijo

*No hay lineas en tus apuntes.*

---

## 8. Contabilidad

| # | Lo que anotaste | Criterio |
|---|---|---|
| K-1 | TC en pesos al contabilizar | Comportamiento al grabar asiento |
| K-2 | Cierre/apertura de mes con **motivo** | Obligatorio en periodos |
| K-3 | Identificador del asiento con **nomenclatura del tipo** (apertura, egresos, ingresos, proveedores, traspasos, ventas) | Visible en correlativo o codigo |
| K-4 | Detalle del asiento en **tres columnas**; regularizar botones **editar glosa** | UI comprobante |
| K-5 | Adjuntar **RC** en comprobante | Adjunto en registro |
| K-6 | Nuevo comprobante manual: pedir **tipo**; si viene de otro modulo, tipo **automatico** | Wizard nuevo asiento |
| K-7 | Validar carga historica con **Mario** | Proceso + plantilla |
| K-8 | Nuevo comprobante pasa directo a **contabilizado** al guardar | Estado al crear manual |
| K-9 | Si no hay TC del dia: ingreso **manual** y **notificar administrador** | Aviso + override controlado |
| K-10 | Presupuesto: **alerta por porcentaje** en totalizados | Config + UI presupuesto |
| K-11 | CC agrupados por **departamento** con **totalizados arriba** | Vista presupuesto/seguimiento |
| K-12 | Libro mayor / diario: filtro **mes y ano**; **Todos** = solo **ano en curso** | Reportes |
| K-13 | Libro mayor: ancho del selector **todas las cuentas** | UX |
| K-14 | Libro mayor: saldo **de un ano a otro** con su informacion | Arrastre de saldo |
| K-15 | Balance 8 columnas: enfoque **ano actual** (cuentas de resultado se traspasan de temporada) | Coherente con cierre |
| K-16 | Estado de resultados: filtro **solo ano en curso** | Reporte EERR |
| K-17 | Situacion financiera: puede traer **anos anteriores** | Reporte |
| K-18 | Utilidad del ejercicio sale del EERR y pasa a situacion financiera el **31/12** | Cierre anual |
| K-19 | Validar **resultado del ejercicio** y **resultado acumulado** en reporteria (MJ explico en reunion; Excel 26/10) | Cuadra con balances ene-2026 / dic-2025 en carpeta MJ |
| K-20 | **Carga masiva** comprobantes vista **Agrosoft** (campos opcionales/restrictivos segun cuenta) | Fail-closed; validar con Mario |

Tipos comprobante (apuntes): apertura, egresos, ingresos, proveedores, traspasos, ventas - **parcialmente en codigo** 26/10.

---

## 9. Tesoreria

*No hay lineas en tus apuntes* (cartola banco fue en audio, ver lista final).

---

## Avance en codigo (26/10 noche)

| Item | Estado |
|---|---|
| P-1 / P-8 | Vista **Matriz** en plan de cuentas; edicion con **3 columnas** con scroll |
| P-2 | Columna **Cuentas plan** en CC, elementos y areas |
| P-3b | **Cuentas para transferencias** en banco (numero, tipo default CTE, moneda) |
| P-4 / A-2 parcial | Historial plan: guardar cuenta registra cambio en importaciones/historial |
| C-2 | OC: opcion **Solicitar al administrador** en CC y elemento |
| A-3, C-4, K-* | Pendiente siguiente tanda |

Migracion local: `erp_back/prisma/migrations/20261026230000_banco_cuentas_solicitud_vinculo/`

## Orden sugerido de trabajo (solo lo que aplicas)

1. **Parametrizacion:** P-1, P-2, P-8 (plan + N:N + matriz scroll).
2. **Parametrizacion:** P-3b bancos; P-4 historial catalogos.
3. **Compras:** C-1 a C-4 (dependen de P-1).
4. **Contabilidad:** K-19 reporteria vs Excel MJ; K-12 a K-18; K-20 carga masiva; resto K-* segun prioridad operativa.
5. **Administracion:** A-3 apertura/reverso (habilita correcciones con periodo cerrado).
6. **P-5 a P-7:** cuando cierres diseno con MJ (ver explicacion 2.9).

---

## Explicacion de puntos que confundian (del plan anterior)

Eran items mezclados desde AGENTS, audio o minuta IA; **no** salen de tu txt salvo donde indico.

| Antes | Que era | Por que no aplica o que hacer |
|---|---|---|
| **1.2** Reglas OC sin OV | Decision de proyecto agosto (solo aprobacion compras) | Politica ya cerrada; no es pendiente del 26/10 |
| **1.3** Roles / quien aprueba OC elige cuenta | MJ `[27:27]`: hoy el aprobador solo ve monto; meta es que cada area impute bien **al armar la OC** | **Aclaracion**, no modulo nuevo: ya va por **linea** en wizard (`cuenta > CC > elemento`). Ver [`validacion-puntos-plan-2026-10-27.md`](validacion-puntos-plan-2026-10-27.md) |
| **1.4** Config correos | PIN de aprobaciones (SMTP) del backlog tecnico | **No salio el 26/10** en tus notas |
| **1.5** Plantilla PDF OC sin dimensiones | Agrosoft: hoja 1 al proveedor sin CC/elemento; hoja 2 contable `[50:24]`-`[53:30]` | **Fuera de alcance ERP por ahora** (proceso actual Agrosoft). En ERP: **C-4** pantalla. Ver validacion 1.5 |
| **2.1** Import 397 cuentas | Mail MJ = referencia; import Excel **ya en ERP** | Antes del cruce MJ: **panel/matriz permisos y N:N** (P-8); luego import Mario |
| **2.2** (plan anterior) Flags Agrosoft | Columnas PLT, CC, CF de la foto Agrosoft | Tu **2.2** es la **matriz con scroll** (P-8), no duplicar import |
| **2.6** Archivo temporada Comex | MJ `[26:34]`-`[27:19]`: cada temporada Comex/logistica manda mapeo area-CC-elemento para filtrar combos | Detalle en [`validacion-puntos-plan-2026-10-27.md`](validacion-puntos-plan-2026-10-27.md). Opcional post P-1 |
| **2.8** Factor honorarios (catalogo) | Reu4 + 22/10: % retencion SII; no en 26/10 (`[01:08:36]` boletas no vistas) | Parametrizacion; no es glosa. Ver validacion 2.8 |
| **2.9** OPB / nota cobro / honorarios | Apuntes consultor; **no** en audio 26/10 | Ver validacion 2.9; P-5 a P-7 en espera |

### 2.9 - Honorarios, nota de cobro y OPB (tus apuntes P-5 a P-7)

Resumen en lenguaje operativo:

1. **Boleta de honorarios:** el ERP **no emite** boletas al SII; solo **registra** las que llegan y su **recepcion** (como una compra de servicio). En **proveedor** debe quedar claro el **tipo de documento** honorarios para enrutar libro compras/contabilidad.

2. **Nota de cobro:** documento interno de **rendicion de gastos** (empleado o area rinde gastos). Debe poder ingresarse desde **contabilidad** y tambien desde **compras**; las facturas asociadas llegan en formato **electronico** (DTE/XML o registro manual segun acuerden).

3. **OPB (embarcador):** tercero que **paga** facturas de comercio exterior; envia a Almahue el **detalle** de lo pagado; Almahue **carga** esas facturas en el ERP y contabiliza el rol de OPB como **intermediario** (no es el proveedor final del gasto en todos los casos).

**Antes de implementar** conviene un diagrama corto con MJ: estados del documento, si genera OC, si va directo a libro compras, y que cuenta contable usa el puente OPB.

---

## Lo que NO anotaste (transcripcion 26/10 - no implementar hasta que lo pidas)

Temas fuertes en **audio tarde** (contratistas) y **manana** que no estan en `revision en cliente.txt`:

| Tema | Donde |
|---|---|
| Modulo **contratistas** completo (parametrizacion, ingreso diario, proforma, centralizacion, compras puente) | Tarde |
| **Actividad > labor** (asociar desde actividad) | Tarde |
| **Aprobacion en proforma**, no en cada ingreso diario | Tarde |
| Bloques cierre verde vs informativo en contratistas | Tarde |
| **Reverso en cascada** si hay meses posteriores cerrados | Tarde |
| **Edicion acotada** sin reverso (solo imputacion, sin factura) | Tarde |
| Apertura de un modulo **impacta** compras, ventas, insumos | Tarde |
| Debate carga masiva: rechazar lote entero vs lineas | Manana |
| Archivo temporada **Comex/logistica** (2.6) | Manana |
| **Cartola**: archivo debe ser descarga directa del banco | Manana |
| Factura **50% TI / 50% contabilidad** en una OC | Manana |
| Ejemplo presupuesto **VINs** confeccion vs arriendo | Manana |
| PDF OC **sin dimensiones** al proveedor (1.5) | Manana |
| **Notificaciones** desde listados (proforma borrador) | Tarde |

Minuta consolidada y timestamps: [`docs/reuniones/minutas/reunion-2026-10-26-presencial-v2.md`](../reuniones/minutas/reunion-2026-10-26-presencial-v2.md) anexos A y B.

---

## Referencias

- Apuntes: `C:\Users\c\Desktop\revision en cliente.txt`
- Menu ERP: `ERP/erp_front/src/app/Sidebar.tsx`
