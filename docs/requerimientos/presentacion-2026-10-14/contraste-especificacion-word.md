# Contraste con el Word del otro modelo

Fecha de la revisión: 15/10/2026. Empresa de la captura: ALMAHUE EXPORT SPA, modo real, periodo 2026-10.

Documento contrastado: `Especificacion para desarrollo - Presentacion cliente 14 10 2026 (16 00).docx`. La sala manda cuando el Word y la transcripción `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md` no dicen lo mismo. El md del repo `especificacion-desarrollo.md` es el mismo texto, salvo dos frases que el Word agregó y que se anotan abajo.

No se ejecutó el cierre, no se vinculó una factura, no se emitió un DTE y no se pagó nada.

## Dos frases que el Word agrega

1. En el cierre de contratistas pide un historial de aperturas y cierres con el usuario. Esa frase no está en el md del repo. En la base ya existe `PeriodoCierreContratistaEvento` (`accion`, `usuarioId`, `usuarioNombre`) y el cierre guarda `cerradoPorId` / `cerradoPorNombre`. La captura no bajó hasta ese listado.
2. En el trato dice que el precio puede ser 0, o que se ingrese sin precio y se marque. La sección "Fuera de alcance" del mismo Word dice que el precio 0 sigue abierto, sin un sí del cliente. La transcripción tampoco lo cierra. El código ya acepta 0 cuando no hay tarifario (`contratistas.service.ts`, mensaje "puede ser 0 para asistencia/avance pendiente de valorizar"). No se toma la frase del cuerpo del Word como pedido nuevo.

## Contratistas

La cuenta del gasto sigue eligiéndose en la proforma (`cuentaGastoId`). El cierre arma el debe con esa cuenta, o con la del tipo de contrato, y el haber con la cuenta haber del tipo. La glosa dice "Facturas por recibir" más el nombre del tipo. No está fija la cuenta "mano de obra contratista".

`asociarFacturaProforma` deja la proforma en camino a Compras y crea una orden de compra. No arma el asiento que pasa facturas por recibir a proveedor cuando llega la factura.

La pantalla ya se llama "Traspaso contable y cierre de mes". El menú dice "Traspaso y cierre" y está arriba de Auditoría. La tarjeta "A traspasar" suma DEFINITIVA y FACTURADA. El tipo de cambio del periodo sigue en el formulario. Las proformas pendientes se listan en la grilla del periodo.

Un día sin proforma no salta de mes en el ingreso. Si el mes de contratistas ya está cerrado, el modelo de eventos permite reabrirlo. Eso no se probó en pantalla.

## Insumos y libro de compras

La guía recibida en insumos (`createGuiaInsumoRecibida`) no crea una OC hija. La hija nace en el libro, dentro de `vincularOcRegistroCompra`, con `splitOcMadreCreaHijaPorMontos`: si el neto de la factura es menor que el de la madre, la madre baja al monto de la factura, vuelve a `PENDIENTE_APROBACION` y la hija queda `APROBADO` con el saldo. La factura queda en la madre. `assertRegistroContabilizableOcMadre` impide contabilizar una madre que tiene hijas activas.

Eso es el camino contrario al de la sala. En la sala la madre es informativa y no se contabiliza, la hija nace al recepcionar la guía en insumos, varias guías del mes pueden ir a una factura, y el libro asocia las hijas de ese proveedor. Solo las hijas se contabilizan.

`solicitarCierreSaldoOc` baja la madre a lo recibido y la deja `PENDIENTE_APROBACION`. No crea la hija del saldo y vive en Compras, no en insumos. Se puede repetir mientras haya diferencia. La sala pidió un solo ajuste al cierre, hacia arriba o hacia abajo, pedido desde insumos por quien creó la madre, y con aprobación.

`bajo_umbral` sigue en `approval-engine.ts`. Un monto chico puede saltarse la cadena. La sala dijo que hasta 5 pesos pasa por la cadena y que el primer tramo parte en 0.

Las listas de Compras e Insumos siguen mezclando madre e hija. No hay marca de quién del grupo puede crear la madre.

## Estado de resultados

`EstadosFinancierosPage` no tiene botones de Excel ni de PDF. La captura del 13/10 (`docs/sesiones/contabilidad-estados-2026-10-13/despues-estado-resultados.png`, 1536x960) muestra la misma pantalla sin exportar. Por eso no hay par antes / después de esa pantalla.

## Qué sí cambió en pantalla

El único par con antes de 1536x960 es el traspaso de contratistas. El antes es el del 13/10, cuando la pantalla estaba en Contabilidad. El después es el de hoy. Comparación y recorrido: `docs/sesiones/presentacion-validacion-2026-10-15/`.
