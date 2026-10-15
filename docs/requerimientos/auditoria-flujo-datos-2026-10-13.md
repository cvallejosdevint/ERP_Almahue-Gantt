# Auditoría: datos entre módulos contra lo que pidió el cliente

Fecha: 13/10/2026. Auditoría nueva: no parte del mapa anterior. Tres revisiones en paralelo leyeron `ERP/erp_back` y `ERP/erp_front`:

- Inventario de cada cruce de datos entre módulos: quién escribe, quién lee, y qué campos se escriben y nadie lee.
- Búsqueda de datos que el cliente descartó en las reuniones y que el software todavía guarda o exige.
- Verificación escéptica de los 16 hallazgos del mapa anterior. Ninguno quedó refutado: 12 se confirman tal cual y 4 con matices.

Lo que el cliente cerró sale de las transcripciones (la frase más nueva gana), del Word de contratistas y del deck de Mario, donde la sala no los corrigió. Cada punto lleva archivo y línea. Rutas relativas a `ERP/erp_back/src/modules/`, salvo indicación.

## Veredicto

Hay conexiones que faltan, datos que viajan con valores que no cuadran entre un módulo y otro, y datos que el cliente descartó y que todavía bloquean flujos.

Lo más grave no es un dato faltante. Son tres cifras que no cuadran:

1. Compras registra el asiento por el neto y la cuenta corriente por el bruto.
2. Tesorería paga contra el neto.
3. Las notas de crédito suman a lo que se cobra.

## 1. Datos que viajan con valores distintos

Cada módulo guarda su parte, pero el número que pasa de uno a otro no es el mismo.

| Tramo | Qué pasa | Efecto | Evidencia |
|---|---|---|---|
| Compras > Contabilidad y Tesorería | El asiento de la compra acredita Proveedores por el **neto**, sin línea de IVA crédito. Al contabilizar, la cuenta corriente y el aging cargan neto por 1,19. | El mayor de Proveedores no calza con el estado de cuenta ni con la nómina. | `compras/compras.service.ts:250-254` (`totalCompraParaTesoreria`), `:860` (haber por `opts.monto`), `:2646`, `:2657` |
| Tesorería > Cuenta corriente | Al pagar desde la cartola, abona la cuenta corriente con el monto del registro de compra, que es el neto. | El saldo del proveedor no llega a cero después de pagar la factura completa. | `tesoreria/tesoreria.service.ts:2310`, `:1822-1852` |
| Ventas > Aging | La nota de crédito entra al aging como `POR_COBRAR` con monto positivo. `syncDocumentosAging` repite lo mismo. | Una nota de crédito aumenta lo que el cliente debe. | `tesoreria/aging-sync.util.ts:64-65`, `:78`; `tesoreria.service.ts:2772`, `:2838` |
| Tesorería > Aging | El pago busca el documento solo por número, sin mirar si es por cobrar o por pagar. | Una factura de compra y una de venta con el mismo número se cruzan. | `tesoreria.service.ts:1173-1179`, `:1221-1228` |
| Compras > Contabilidad | El asiento de compra no lleva fecha ni periodo: toma la de hoy, no la del documento. El aging usa la fecha de creación del registro, no la de la factura. | Una factura de septiembre contabilizada en octubre queda en octubre. | `compras.service.ts:869-886`, `:2522-2528` |

## 2. Conexiones que faltan

| De | A | Qué pidió el cliente | Qué falta | Evidencia |
|---|---|---|---|---|
| Contratistas | Compras | 13/10: en el libro se elige la orden o la proforma aprobada, sin crear otra orden. | Compras no lista proformas. La asociación vive en Contratistas y crea una orden. | `contratistas/contratistas.service.ts:2606-2627`; búsqueda de `proforma` en `erp_front/src/features/compras`: 0 coincidencias |
| Contratistas | Compras (cadena) | La proforma ya pasó por jefatura en Contratistas (6/10). | La orden generada nace `EMITIDO`, y `ocEnviaAprobacion` lo trata como «enviar a aprobación»: la proforma se aprueba dos veces. Si el usuario de Contratistas no está en un grupo de Compras, la cadena falla con `sin_grupo` y la orden no se crea. | `compras.service.ts:147-150`; `contratistas.service.ts:2616`; `compras.service.ts:1241-1244` |
| Contratistas | Compras (cuenta) | Al calzar: facturas por recibir contra el **nombre del contratista**. | Compras lee la proforma solo si la orden trae `referenciaTipo: PROFORMA_CONTRATISTA`. El haber va a la cuenta Proveedores con glosa «Proveedores», sin auxiliar. Si se asocia por la rama del registro de compra, Compras no se entera: usa la cuenta normal. | `compras.service.ts:783-822`; `contratistas.service.ts:2503-2554` |
| Contratistas | Compras | La orden y su vínculo con la proforma deben quedar juntos. | `createOrden` corre fuera de la transacción que enlaza la proforma. Si el enlace falla, queda una orden huérfana. | `contratistas.service.ts:2606-2647` |
| Compras (cierre de saldo) | Aprobaciones | La madre, si cambia el monto, vuelve a la cadena (24/09). | La madre pasa a `PENDIENTE_APROBACION` sin crear filas en `AprobacionOc`. La bandeja lee esas filas y aprobar responde «No hay aprobación pendiente». La madre queda trabada. | `compras.service.ts:3961`, `:558`, `:1594-1598`, `:1908` |
| Compras | Insumos | La guía entra al precio de la orden (10/09). La factura de fin de mes se asocia a la orden (01/10). | Las líneas de la orden no llevan `insumoId`. La guía no conoce la orden y toma el precio del maestro. Compras e insumos no comparten ningún dato. | Búsqueda de `insumoId` en `compras/`: 0 coincidencias; `insumos/insumos.service.ts:709-710` |
| Compras | Tesorería | Neto e IVA con vencimientos distintos (24/09). | El aging usa un solo vencimiento, el del neto. `Proveedor.condicionIvaDia` no viaja. | `tesoreria/aging-sync.util.ts:116` |
| Ventas (reverso) | Tesorería | Reversar corrige la imputación sin anular el DTE. | El movimiento de cuenta corriente del reverso se graba sin `documentoComercialId`. El aging no se toca y sigue vivo. | `comercial/comercial.service.ts:2692-2725` |
| Tesorería (anular pago) | Cuenta corriente y aging | - | Pasar un pago a anulado no revierte la cuenta corriente ni el `montoPagado` del aging. No hay otro camino de anulación. | `tesoreria.service.ts:1284-1371` |
| Contabilidad (anular asiento) | Compras, Ventas, Contratistas | - | Anular un asiento no avisa al documento de origen: el registro de compra, la venta y el cierre de contratistas siguen contabilizados con un asiento anulado. Solo se protege el origen `CARTOLA:`. | `contabilidad/contabilidad.service.ts:800-839` |
| Contratistas | Corrección | Si hay diferencia, se corrige el ingreso y vuelve a jefatura (6/10). | Reversar deja la proforma en borrador. El ingreso sigue asociado y no se edita. Solo se libera si se borra la proforma. | `contratistas.service.ts:2721-2731`, `:3058`, `:2686-2700` |
| Admin (traspaso de aprobador) | Compras y Contratistas | - | Cambia `aprobacionCadenaIds`, pero no el JSON `aprobacionCadena`, que es el que Compras lee primero. Las proformas pendientes no se traspasan. | `admin/admin.service.ts:1801-1870`; `aprobaciones/aprobacion-cadena.util.ts:84-90` |
| Contabilidad (vista previa del cierre) | Contratistas | - | La vista previa cuenta proformas `DEFINITIVA` y `FACTURADA`. La ejecución incluye además `ENVIADA_CONTRATISTA`. Muestran montos distintos. | `contabilidad.service.ts:2244-2251`; `contratistas.service.ts:3438` |
| Dashboard | Contratistas | - | El indicador «facturas por recibir» solo cuenta `DEFINITIVA` y deja fuera las notificadas, que son justamente las que esperan factura. | `dashboard/dashboard.service.ts:45-63` |

## 3. Datos que sobran

El cliente los descartó en las reuniones y el software todavía los guarda. Van primero los que además condicionan un flujo.

### Sobran y bloquean

| Dato | Qué dijo el cliente | Qué bloquea | Evidencia |
|---|---|---|---|
| Área de negocio (`AreaNegocio`, `CuentaAreaNegocio`, `requiereArea`) | 01/10, María José: no se usa, ni para gestión. | Todo asiento exige el área si la cuenta tiene `requiereArea`. Compras también la exige, pero ningún llamador la manda. Basta una cuenta marcada para que una compra no se pueda contabilizar. | `contabilidad/contabilizar.service.ts:194-201`; `compras.service.ts:733-736`, `:910-918` |
| Estado `ENVIADA_CONTRATISTA` | 6/10: el correo al contacto «sería bueno». 13/10: en compras, las aprobadas. | Asociar la factura exige ese estado. | `contratistas.service.ts:2475-2480` |
| Orden que crea `asociarFacturaProforma` | 13/10: no nace otra orden. | Es el único camino por el que Compras toma la cuenta del tipo de contrato, y además repite la aprobación. | `contratistas.service.ts:2606-2627`; `compras.service.ts:783` |
| `WorkflowConfig` (motor de aprobación anterior) | Hoy mandan grupos y escalas. | No tiene pantalla, pero sus filas todavía arman el grupo de aprobadores de la orden y deciden si se exige PIN. La consulta del PIN no filtra por empresa. | `compras.service.ts:1165-1186`; `ERP/erp_back/src/auth/pin-aprobacion.ts:40-47` |

### Sobran sin bloquear

| Dato | Qué dijo el cliente | Dónde vive | Evidencia |
|---|---|---|---|
| Cuenta y centro de costo en la cabecera de la orden de venta | 07/09: se asignan al contabilizar el libro, por ítem. | Se guardan al crear la venta. Emitir copia en silencio la cuenta del maestro a cada ítem. Al contabilizar solo se usan si el libro no manda líneas. | `comercial.service.ts:2549-2550`, `:2885-2907`; `erp_front/src/features/comercial/EmitirDocumentoPage.tsx:1624-1625` |
| Supervisor y aprobación por ingreso diario (`aprobadorId`, `aprobadoPor*`, `aprobadaAt`) | 6/10: se aprueba la proforma, no cada fila. | Combo «Supervisor (aprobación)» y botón Aprobar en el ingreso y en el masivo. No bloquea la proforma. | `contratistas.service.ts:2939-3153`; `erp_front/src/features/contratistas/IngresoLaborDiarioPage.tsx:172-173` |
| Envío operativo (`EnvioOperativoContratista`) | El correo es opcional. | Pantalla y menú propios. | `contratistas.service.ts:2267-2339`; `erp_front/src/app/Sidebar.tsx:96` |
| `reemitirProforma` | 13/10: no hay proforma hija. | Crea una proforma nueva y marca la original como `RECHAZADA`, aunque nadie la rechazó. No es una hija formal, pero el resultado se parece. Hay que confirmarlo con María José. | `contratistas.service.ts:2745-2813` |

### Muertos: definidos o escritos y nadie los usa

| Dato | Evidencia |
|---|---|
| `PATCH documentos/:id/imputacion`. Escribe la cuenta en la orden de venta y ninguna pantalla lo llama. | `comercial/comercial.controller.ts:257-266` |
| `ReservaStock` y `crearReservasOv`. No tienen llamador. Consumir, liberar y la columna «reservado» trabajan sobre cero filas. | `insumos/stock-bodega.util.ts:169-255` |
| `AnticipoProductor`. Solo lo llena el seed de demo. La pantalla no tiene ruta. La cuenta corriente todavía lee esa tabla para el calce, además de `Pago`. | `tesoreria.service.ts:3024-3038`; `tesoreria/cuenta-corriente.service.ts:317-325`; `prisma/seed-demo-showcase.ts:829` |
| `FacturaContratista`. Nadie hace `create`. | `contratistas.service.ts:151`, `:282` |
| Ramas de ventas, compras y bodega de `runCentralizacion`. Son inalcanzables: solo se ejecuta contratistas. | `contabilidad.service.ts:2030-2035` |
| `MovimientoBodega.centralizadoAsiento*`. Se lee y nadie lo escribe. | `contabilidad.service.ts:2304` |
| `PasoAprobacionDetalle`. Está en el schema y no aparece en el código. | `prisma/schema.prisma:2573` |
| Estado `AUTORIZADA` de la venta y tipos `COTIZACION` / `NP`. Quedan en los enums y nadie los asigna. | `prisma/schema.prisma:801-817`, `:1001-1011` |
| `Contratista.especialidad`, `representanteLegal`, `rutRepresentante`, `tipoPago`. Ninguna pantalla los muestra. | `contratistas.service.ts:960-969` |
| `billingPartner`, `billingConnectionMode`, `billingGlobalDocumentId`, `gosocketCountryDocumentId`. Se guardan y ninguna pantalla los lee. Sirven para soporte; no estorban. | `comercial.service.ts:136-151`; `compras.service.ts:2845-2853` |
| `Moneda.focoReporteria`. Se muestra como Sí/No y ningún informe lo usa. | `catalogos/catalogos.service.ts:152`, `:177` |

## 4. Lo que viaja bien y es necesario

- Cadena de la orden: escribe `AprobacionOc` y la bandeja la lee. El monto se pasa a pesos antes de elegir el tramo.
- Factura de una orden sin aprobar: se asocia, se destaca y no se contabiliza ni se paga. Tesorería mira el mismo estado antes de pagar.
- Referencia de la cotización (tipo, folio y fecha) dentro de la orden.
- Venta a insumos: confirmar crea `SALIDA_VENTA` y rebaja la bodega. La recepción de la orden no mueve stock.
- Venta a contabilidad: el asiento usa la cuenta y el centro de cada ítem del libro, más el IVA débito.
- Venta a billing: folio guardado. PDF y XML se piden al gateway sin volver a emitir.
- Contratistas a contabilidad: cierre de mes, costo contra facturas por recibir, con el asiento guardado en el periodo.
- Tesorería a contabilidad: el asiento de banco es el de la cartola. El pago no crea otro.
- Pago `ANTICIPO_PRODUCTOR` con tipo de cambio digitado y bitácora en `PagoTcEvento`.
- `TipoContratoContratista` con sus cuentas: el nombre confunde, pero es el lugar donde vive la cuenta de costo que pidió María José.
- Datos que el cliente pidió no tener y el software no tiene: solicitud de compra, maestro de cotizaciones, contrato de contratistas, trabajador, niveles dentro de la bodega, stock de fruta, reintegro de insumos, maestro de productor y banco en línea.

## Orden sugerido

1. Cuadrar el IVA de compras entre el asiento, la cuenta corriente y el pago. Corregir el signo de la nota de crédito y el cruce por número sin tipo.
2. Mover la asociación de la proforma al libro de compras, sin crear orden y sin `ENVIADA_CONTRATISTA` como requisito. Llevar el haber a nombre del contratista.
3. Destrabar la orden madre después del cierre de saldo.
4. Revertir cuenta corriente y aging al anular un pago o reversar una venta. Avisar al documento cuando se anula su asiento.
5. Quitar el área de negocio como requisito y retirar `WorkflowConfig` del cálculo de aprobadores y del PIN.
6. Limpiar lo muerto: reservas, `AnticipoProductor`, `FacturaContratista`, ramas inalcanzables de la centralización, imputación de la orden de venta.
