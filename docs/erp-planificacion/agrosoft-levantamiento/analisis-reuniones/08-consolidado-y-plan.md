# Consolidado del análisis de reuniones — 03/09/2026

Cierre de las 11 transcripciones (~450 KB) leídas íntegras, más el triage de los 40 SKIP y 1 BLOCKED de la corrida QA del 02/09.

## Veredicto en una línea

El código está sano —490 PASS y 0 FAIL— pero **la capa documental sobre la que se decidió el alcance no es confiable**, y por eso hay requisitos del cliente eliminados sin respaldo y requisitos nunca implementados que no tienen ni caso de prueba.

## Quién estaba en cada reunión

Este es el filtro que faltaba. Una decisión solo vale como requisito si había un cliente en la sala.

| Reunión | Cliente presente | Valor como requisito |
|---|---|---|
| Reu1 · 21/07 | MJ, Rodrigo | **Alto.** Recorrido de Agrosoft. **Nunca tuvo minuta** |
| Reu2 · 23/07 | MJ, Rodrigo | **Alto.** Recorrido de Agrosoft. Minuta = stub de 1 KB |
| Reu3 · 28/07 | MJ sola | Medio-alto |
| Reu4 · 30/07 | MJ sola (Sigrid asistió por Mario y no habló; Agustín y Mario de vacaciones) | Medio. **Sin validación de gerencia** |
| Reu5 · 03/08 | **ninguno** | **Nulo.** Interna Carlos ↔ Sergio |
| Reu6 · 06/08 | MJ, Agustín | Alto, pero **nunca demostró** compras completo, contabilidad, tesorería ni inventario |
| 19/08 · demo interno | ninguno | Nulo |
| 20/08 · mañana | ninguno (Sergio) | Nulo |
| 20/08 · tarde | Lupe, Mario | Alto en compras y tesorería operativa; **cero** en contratistas y ventas |
| 28/08 · tesorería | MJ, Lupe, Fran, Mario | **Alto.** Es el master ToDo vigente |

Consecuencia inmediata: **Reu5 no puede citarse como fuente de requisitos**, y sin embargo de ella salió la línea que originó toda la confusión sobre Config SII.

## Estado de las minutas

| Minuta | Problema |
|---|---|
| Reu1 | **No existe.** Once módulos recorridos sin representación documental |
| Reu2 (tl;dv) | **1.175 bytes.** Seis ítems y un encabezado «## 2–16. Temas» cuyo cuerpo remite a `reunion2-analisis-2026-07-23.md`, **archivo que no existe en el repositorio** (verificado). Tres de los seis compromisos están mal atribuidos, los tres a personas ausentes. Rodrigo no figura ni como participante pese a hablar la mitad de la reunión |
| Reu3 | Borra al hablante y convierte preguntas abiertas en hechos. Omite por completo el renombrado «Libro comercial → Libro de ventas» |
| Reu4 | Presenta como funcionalidad decidida una **objeción de Sergio**. Convierte tres preguntas del proveedor en requisitos del cliente. Se contradice sola sobre la clave de reversa |
| Reu5 | **Invierte el sentido** de la frase sobre GoSocket. Afirma «Cotiz→NP→Factura — Hecho», en contradicción directa con `AGENTS.md` |
| Reu6 | 12 decisiones respaldadas, 6 parciales, detalles inventados en D19 |
| 20/08 tarde | Marca «Aprobaciones solo compras — ¿Pedido cliente? Sí» sin anotar que fueron respuestas a preguntas cerradas, y **no advierte** que proformas y contratistas no se mencionaron |

Además, dos rótulos colisionan: **D14** significa «cartola Excel» en Reu4 y «stock solo positivo» en Reu6; **D4** significa «alcance incluye Comercial» en Reu6 y «solo Compras» en `AGENTS.md`.

## Hallazgos ordenados por impacto

### 1. Config SII: nadie la pidió, y el mito de GoSocket nació de un error de transcripción

En Reu4, Carlos (proveedor): *«tenemos este panel configurable del SII, que este **fue ideado por parte del equipo de desarrollo**, y no sabría si es que este le darían utilidad, porque recuerdo que **este no lo utilizaban ustedes**»*. MJ: *«No lo utilizábamos, pero sí hay una parte de configuración de las cuentas»*. Sergio objeta: *«si la cuenta la van a asociar a nivel de detalle, **no le vería mucho sentido como a nivel de tipo de documento**»*. MJ cierra con un *«quizá aquí se hace más fácil»* y Carlos concluye *«entonces lo conservamos»*.

La frase «asocia cuentas por tipo de documento» que la minuta presenta como requisito **es la objeción de Sergio**. Se decidió conservar el panel, nunca construirlo ni especificarlo.

Y el vínculo con GoSocket es un artefacto: la minuta tl;dv de Reu5 registra «configuración contable **SAI** necesaria para implementar GoSocket», cuando el verbatim de ese minuto habla de **PIN**, y Carlos calificó esa lectura de *«fantasmeo de la IA… puro fantaseo del aire»*. GoSocket no cubre, no necesita y no menciona jamás la contabilización interna.

### 2. La cadena de aprobación de proformas se eliminó sin ninguna base

MJ la pidió en Reu3 con motivación de control, incluyendo re-aprobación al editar y nombre del aprobador. El corte del 21/08 la eliminó apoyándose en la sesión del 20/08, donde **«proforma», «contratista», «labor» y «jornal» aparecen 0 veces** (recuento verificado sobre las tres transcripciones, contra 49 menciones de «aprobación» y 119 de «compra»).

### 3. D11: MJ pidió mover la cotización, el código la suprimió

MJ en Reu6 `[40:59]`: *«Debe estar en el panel de compras»*. Hoy `/compras/cotizaciones` redirige a órdenes. Existe una frase posterior de Lupe que apunta a no necesitarla, pero `AGENTS.md` establece que Lupe y Mario no pisan Reu6 cuando chocan; aquí chocan y se aplicó al revés.

### 4. El proceso de compras de Agrosoft corre al revés del diseñado

MJ en Reu1: *«como la creamos primero, o sea, se emite la factura y después creamos la orden de compra»*. Hoy la OC es un registro de gasto **a posteriori** que hace contabilidad, no un instrumento de autorización previa. Todo el diseño de cadena de aprobación previa asume lo contrario. No es necesariamente un error —puede ser la mejora buscada— pero **nadie lo declaró como cambio de proceso**, y explica por qué el cliente responde de forma ambigua cuando se le pregunta por aprobaciones.

### 5. El libro mayor es monomoneda

MJ el 28/08: «toda la contabilización de todo el sistema tenga las 3 conversiones». Verificado en el esquema: `Asiento.lineas` es `Json` con forma `[{ debe, haber, cuentaId?, glosa? }]`, sin tipo de cambio ni importe convertido, y `debe`/`haber` son `Decimal(18,2)`. Diario, mayor y balance no soportan las tres conversiones. Es el hueco funcional más grande y **no es de un día**.

### 6. D16 valida contra la magnitud equivocada

Lo discutido en Reu6 fue el **precio de compra del mantenedor**. El código valida contra `costoPromedio`, término que nadie pronunció nunca. La decisión figura como cerrada.

### 7. El objetivo declarado de GoSocket era recepción, no emisión

MJ en Reu2: *«la idea de que GoSocket esté conectado con el ERP de AlmaWeb es que nos aparezca el **libro de compras en línea** y podamos contabilizar directo»*. Si hay casos bloqueados por ese lado, el motivo correcto es alcance no construido, no «falta CAF».

## Correcciones que necesita `AGENTS.md`

| Afirmación actual | Corrección |
|---|---|
| «D4 … Migración `20260821120000_aprobaciones_solo_compras_drop_ov`» atribuido a Reu6 | El origen es 20/08 tarde. En Reu6, D4 dice lo contrario. La parte de **proformas** no tiene respaldo alguno |
| «D11 … no hay menú ni CRUD de Cotizaciones» | MJ pidió **moverlas al panel de Compras**, no suprimirlas |
| «Sin CAF/cert MJ el partner **REJECTED** (fail-closed)» | Ya no se reproduce: el 02/09 el sandbox encoló con folio oficial 58 y asiento. Hay que forzarla con un `BillerId` inválido |
| «D16 … no vender bajo `costoPromedio`» | Verificar contra el precio de compra del mantenedor, que es lo que se discutió |
| Prioridad «Reu6 > Reu5 > Reu4» | Reu5 **no tuvo cliente**. No puede pesar sobre Reu4, donde sí estaba MJ |

## Plan para hoy

### Bloque A — arreglar (bajo riesgo, alto retorno)

1. **Config SII a cuentas imputables** (`PROVEEDORES`, `CONTRATISTAS`, `IVA_CREDITO`, `BANCO`, y `VENTAS` con área o a una hoja sin dimensión). Es configuración de tenant, no código. Destraba de una vez el traspaso de contratistas, el haber de compras, la centralización y la emisión por la hoja de ventas, y elimina el fallback a CAJA.
2. **Corregir `AGENTS.md`** con la tabla de arriba. Sin código.
3. **Renombrar la pantalla** «Configuración contable (SII)» a algo que diga lo que hace, del tipo «Cuentas por tipo de documento». Mata la confusión de raíz.

### Bloque B — ejercer en QA (requiere levantar el stack, hoy caído)

Con Config SII corregido se pueden cerrar casos que quedaron en SKIP por entorno: `CNT-007` centralizar execute, `SIST-6-91` traspaso de contratistas, `SIST-9-22` emisión por la hoja de ventas sin caer en CAJA, y `SIST-3-72` compra con elemento de costo.

Además, ahora que el sandbox emite con folio, se puede cerrar el hueco P0 `INV-010` (nota de crédito contabilizada → `DEVOLUCION_NC`) y probar de verdad las reglas `CodRef` 1/2/3, que hoy solo tienen cobertura Jest.

### Bloque C — decisiones de alcance (requieren al usuario)

No las tomo yo: cambian el producto.

- ¿Se reabre la cadena de aprobación de proformas que pidió MJ?
- ¿Se restauran las cotizaciones en el panel de Compras?
- ¿D16 valida contra costo promedio o contra precio de compra?
- Triple moneda en el mayor: cuándo entra.

## Estado del entorno

La API (`localhost:3001`) y el front (`localhost:5174`) están **caídos**. Nada del Bloque B corre hasta levantarlos.
