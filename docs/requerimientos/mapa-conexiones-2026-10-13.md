# Mapa de necesidades y conexiones

Fecha: 13/10/2026. Lo que el cliente pidió sale de las transcripciones, del Word de contratistas y del deck de compras de Mario. Si chocan, gana la frase más nueva. El Word y el deck no pisan lo que María José cerró el 6/10 y el 13/10 al mediodía.

Cada fila de «comprobado» tiene un test que corrió y afirmó ese dato. Si el test no compiló o no mira el campo, queda como no comprobado: no se cuenta como hecho ni como falta. Lo que está en «falta» es porque el código hace otra cosa, y una prueba en verde lo afirma o el fuente no tiene el lector que el cliente nombró.

Revalidación después de aplicar las migraciones de contratistas y de regenerar el cliente Prisma (`prisma generate`, cliente 7.10.0). El cliente generado ya conoce `predio`, `sectorContratista`, `faenaContratista` y `ENVIADA_CONTRATISTA`.

Corridas, en `ERP/erp_back`:

- Contratistas, de nuevo: 3 suites, 29 tests, todos en verde. Incluye `contratistas.service.spec.ts`, que antes no compilaba.
- Contabilidad, de nuevo y en el mismo cliente: `contabilidad.service.spec.ts`, 22 tests en verde.
- Compras, de la pasada anterior: 86 en verde, 10 en rojo. Los 10 rojos son el sync y el aceptar/rechazar contra GoSocket: el mock no tiene `libroComprasSyncMeta` y aceptar exige proveedor antes de llamar al partner.
- Ventas e insumos, de la pasada anterior: 90 en verde. `stock-reserva.spec.ts` no compiló (propiedad duplicada).
- Tesorería, de la pasada anterior: 111 en verde.

## Cómo debería comunicarse

Esto es lo que quedó aprobado, no el diagrama viejo del Word ni la tapa del deck.

1. Contratistas. El ingreso diario arma la proforma. La proforma pasa por jefatura. Al cerrar el mes, aunque la factura no esté asociada, el asiento es costo de contratistas contra facturas por recibir. La cuenta de ese costo se elige solo ahí.
2. Compras. El libro recibe el DTE. La persona elige una orden de compra aprobada o una proforma aprobada. No se crea otra orden. Al calzar la proforma, el asiento es facturas por recibir contra el nombre del contratista. Una factura de una orden aún no aprobada se destaca y no se contabiliza ni se paga.
3. Insumos. La guía física mueve la bodega. La recepción de la orden no mueve stock. La factura de fin de mes se asocia a la orden. El promedio es informativo. El movimiento vale el precio de la orden con la que entró.
4. Ventas. Guardar la orden valida stock y la deja confirmada. Facturar es otro paso. La cuenta y el centro de costo se asignan al contabilizar el libro, no en la orden. El asiento de la venta entra al mayor.
5. Tesorería. La factura de compra ya contabilizada entra a la nómina. Los egresos de la cartola calzan con esa nómina y la suma tiene que coincidir. El asiento de banco es el de la cartola. El pago no genera otro asiento. El flujo se informa en pesos.

## Cómo se hace ahora

| Tramo | Lo que el cliente espera | Lo que hace el código | Prueba |
|---|---|---|---|
| Proforma a compras | En el libro se elige orden o proforma aprobada. No nace otra orden. | `asociarFacturaProforma` vive en contratistas. Sin registro de compra llama a `createOrden` con `referenciaTipo: PROFORMA_CONTRATISTA`. En `features/compras` no aparece la palabra proforma. | En verde. El `it` «genera una sola OC en Compras» afirma neto 150, una sola orden, `ordenCompraId` y las dos proformas en `FACTURADA`. El fixture parte en `ENVIADA_CONTRATISTA`. |
| Antes de asociar | Basta que esté aprobada. El correo al contacto era un «sería bueno». | Exige estado `ENVIADA_CONTRATISTA`. Si no, rechaza. | El test en verde usa ese estado como dato de entrada. No hay un `it` que pruebe el rechazo de una proforma solo `DEFINITIVA`. El rechazo sigue en el fuente. |
| Cierre de contratistas | Costo contra facturas por recibir, aunque no haya factura. | `traspasoCierre` arma debe a la cuenta del tipo de contrato y haber a su cuenta de facturas por recibir. Guarda `asientoId` en el periodo. | En verde. Con una proforma `DEFINITIVA` y sin factura, el asiento es debe 200 en `CTA-GASTO` y haber 200 en la cuenta haber del tipo. Origen `TRASPASO-CTR:2026-07`. |
| Al asociar la factura del contratista | Facturas por recibir contra el nombre del contratista. | Si se pasa un `registroCompraId`, solo sella la proforma. No arma ese asiento. El asiento de la compra, si la orden ya dice `PROFORMA_CONTRATISTA`, usa la cuenta haber del tipo y la glosa «Proveedores». | No hay `it` de la rama con registro. El test que pasó es el que genera la orden, no el calce contra el nombre. |
| Corregir una proforma ya armada | Se edita el ingreso de origen y vuelve a jefatura. | `reversarProforma` deja la proforma en borrador. El ingreso sigue `ASOCIADO` y `updateIngresoLaborDiario` no edita ese estado. | En verde el `it` de reversa: solo espera `BORRADOR`. No llama a actualizar el ingreso. |
| Recepción de insumos | La guía mueve stock. La recepción de la orden no. | `createRecepcion` escribe `recepcionOc` y puede dejar la orden `RECEPCIONADA`. No llama a stock. La guía, en el fuente, llama a `createMovimiento` `ENTRADA_PROVEEDOR`. | Recepción que marca `RECEPCIONADA`: en verde. Camino feliz de la guía: sin spec. |
| Orden de venta a bodega | Guardar rebaja la bodega elegida. | `confirmarOrdenVenta` deja `CONFIRMADA` y crea `SALIDA_VENTA`. | «confirma OV y crea SALIDA_VENTA» en verde. No afirma bodega ni cantidad. |
| Venta a contabilidad | La cuenta se pone en el libro y el asiento la usa. | `grabarDocumentoContabilizar` arma el haber por ítem con la cuenta y el centro de la línea, más IVA débito. | Tres `it` en verde (centro, IVA, glosa). |
| Compra a contabilidad | Cuenta y centro de cada línea, neto e IVA aparte. | El asiento de la compra es una línea de gasto y una de proveedores, por el neto. No hay línea de IVA. El centro se exige en las líneas, pero el asiento no reparte una línea por cada ítem. | «P0-1 createRegistro CONTABILIZADA» en verde: dos líneas, neto 1000. |
| Compra a tesorería | No se paga si la orden no está aprobada. Nómina con suma exacta. | Contabilizar una orden en borrador se rechaza. El pago, en el fuente, también mira el estado de la orden. Asociar la nómina avisa si no calza y graba igual. | Rechazo al contabilizar borrador: en verde. La suma de la nómina: el `it` no prueba el descalce. El fuente asocia igual. |
| Cartola a contabilidad | Un asiento por línea de cartola. El pago no crea otro. | `contabilizarMovimientoCartola` escribe origen `CARTOLA:{id}`. `createPago` no llama a `createAsiento`. | Asiento de 3 líneas y «calzar-productor no toca monto de cartola»: en verde. |
| Anticipo productor | El tipo de cambio se digita y queda registro. | El alta real es `Pago` tipo `ANTICIPO_PRODUCTOR` más `pagoTcEvento`. La pantalla de anticipos lee la tabla `anticipoProductor`. En el backend no hay `anticipoProductor.create`. `createAnticipo` responde 400. | El `it` del pago productor está en verde. La pantalla y la tabla no tienen test de ida y vuelta. |

## Checklist de lo que falta

Cada ítem es un pedido vigente que el código no cumple. Al lado, la prueba o el sitio del fuente.

### Contratistas con compras

1. Asociar la proforma en el libro de compras, eligiendo orden o proforma, sin generar una orden. El test en verde afirma lo contrario: una orden, neto 150, dos proformas facturadas.
2. Que en compras aparezcan las proformas aprobadas, no solo las marcadas como notificadas. El test en verde entra con `ENVIADA_CONTRATISTA`. El fuente rechaza otro estado.
3. Al asociar, asiento facturas por recibir contra el nombre del contratista. La rama con `registroCompraId` no tiene test y no crea asiento. La glosa del haber de la compra dice «Proveedores». El cierre de mes, en cambio, sí quedó en verde: costo contra la cuenta haber, sin factura asociada.
4. Corregir el ingreso después de armar la proforma. El test de reversa en verde solo deja la proforma en borrador.
5. La proforma pasa por jefatura. El test «bajo el primer piso queda DEFINITIVA sin aprobador pendiente» está en verde. Ella no aprobó esa excepción.

### Compras, según el deck y las correcciones posteriores

6. Varios archivos en la compra y en la venta. La orden no tiene campo de adjuntos. El wizard dice que no se adjunta archivo.
7. Carga manual de la factura con PDF. No hay carga de archivo. El PDF del libro se baja de GoSocket.
8. Tipo de cambio generado, guardado, para que los dólares o yuanes de la factura calcen con la orden. La orden no tiene columna de tipo de cambio. El calce usa el tipo observado de la fecha. `RecepcionOc.tcAplicado` sí se guarda en la recepción. Los tests de `calcularMatchFacturaOc` están en verde y no afirman un tipo guardado en la orden.
9. Plazo del IVA distinto del neto, en la orden y en el vencimiento. `condicionIvaDia` está en el proveedor. La orden y el aging usan solo `condicionPagoDias`.
10. Línea de neto y línea de IVA por cada orden hija. El asiento de compra que pasó el test es neto contra proveedores, sin IVA.
11. La hija de insumos nace autorizada y no entra a la cadena. La madre no se muestra fuera de insumos. `solicitarCierreSaldoOc` crea la hija en `BORRADOR`, no filtra por tipo insumos, y la madre vuelve a `PENDIENTE_APROBACION` y sigue en el listado. No hay spec de ese método.
12. Plazo de aceptación en 7 días. El default de `aceptacionCompraPlazoDias` es 8. El cron usa `?? 8`.

### Inventario

13. El promedio es solo informativo. El test «actualiza stock/CPP al confirmar un borrador de ENTRADA_PROVEEDOR» pasa y deja `costoPromedio` cerca de 433. El movimiento sí cambia el promedio.
14. La devolución al proveedor, solo en ALM, al precio de esa factura. El código mira el flag `permiteDevolucionProveedor` y el precio del movimiento. El test de devolución en verde usa el precio del DTO (500), no el de una factura, y no nombra ALM.
15. Cuenta al debe y al haber por tipo de movimiento de bodega. `createMovimiento` no escribe esas cuentas.
16. Cierre de bodega distinto del cierre contable. No hay ese cierre.
17. Excel de seguimiento de cajas. No hay módulo.

### Ventas

18. La cuenta y el centro de costo no van en la orden de venta. El test «actualiza cuenta y CC en OV confirmada» pasa y los escribe en el documento. Al contabilizar, el asiento sí los toma de la línea: eso está en verde y sí cumple el libro.
19. Guía de despacho con la resolución 154. Se emite guía. No hay campos de esa resolución.
20. Flete como línea y stock en tránsito que no alcance para vender. No hay test de flete. En el fuente no aparece un stock en tránsito.

### Contabilidad y tesorería

21. Borrar una cuenta que no tiene movimientos. `deleteCuenta` lanza 409 siempre. El test «rechaza hard-delete de cuenta» pasa con el impacto en cero y espera ese 409. Inactivar no tiene `it`.
22. La glosa lleva el número de factura y se repite. El test de venta en verde fija `FACTURA 8/2026 TC: 950.5 Pago a 30 dias`. El folio no entra. En la compra, las líneas dicen «Gasto/compra» y «Proveedores», no la glosa de la cabecera.
23. Auxiliar de la compra igual al RUT sin dígito. La venta lo escribe. El asiento de compra no escribe `auxiliar`. El mayor, al armar el libro, no conserva ese campo. El comprobante sí lo pinta si viene en la línea.
24. Los egresos elegidos tienen que calzar con la nómina. `asociarNominaCartola` avisa y asocia igual. El test en verde no cubre el descalce.
25. El flujo de caja en pesos, sumando los bancos. El test «GET flujo-caja» pasa y deja el dólar en 50, sin convertirlo.
26. La pantalla de anticipos productores no escribe la tabla que lee. `createAnticipo` responde 400. El anticipo que sí se guarda es un `Pago`. El estado de cuenta también consulta `anticipoProductor` para el calce: lee una tabla sin alta.

### GoSocket y lo que ellos dejaron para después

27. Los 10 tests de sync y de aceptar/rechazar en el libro de compras están en rojo por el mock, no porque se haya ejecutado el partner. No queda comprobado que el documento sincronizado guarde `ocId` y `aceptacionEstado`.
28. Iofacturo y el plan de pruebas siguen fuera del código, a la espera del contrato. No es una pantalla faltante de esta pasada.
29. Banco en línea y contabilidad electrónica al SII los dejaron ellos para después. No hay código y no se listan como falta.

## Lo que sí quedó comprobado

- Cadena de la orden en pesos y rechazo con motivo en el mismo documento. Tres tests en verde, incluido 200 USD por 965.71 dentro de la escala.
- Factura de una orden en borrador: se asocia, `ocNoAprobada` queda verdadero, y contabilizarla se rechaza.
- Orden de venta a `CONFIRMADA` sin cadena. Piso de precio en nacional y exportación sin piso.
- Emitir guarda `folioOficial`. El PDF se pide al gateway y no se vuelve a emitir.
- Asiento de venta con centro de costo por ítem e IVA débito.
- Cartola por carga, doble contabilización rechazada, mover la semana sin tocar el vencimiento, nómina solo en egresos, pago productor con evento de tipo de cambio, diferencia de cambio en el asiento de la cartola, y el calce que no altera el monto del banco.
- El pago no crea asiento. Lo crea la línea de cartola, origen `CARTOLA:`.
- Estado de cuenta del mismo RUT como cliente y como proveedor, con un pago total. El anticipo en esa vista no quedó en el test.
- Cierre de contratistas sin factura asociada: asiento debe gasto y haber facturas por recibir, origen `TRASPASO-CTR`, guardado en el periodo. Una proforma en borrador, y dos ingresos asociados a una proforma.
- Varias proformas quedan en una sola orden de compra. Eso está en verde y es justo lo que el 13/10 no pidió.

## Lo que sigue sin prueba

El cliente Prisma ya está al día. Ningún `it` de contratistas afirma que el ingreso guarde predio, temporada, sector o faena, ni que una proforma solo `DEFINITIVA` sea rechazada al asociar.

Tampoco corrió un spec del camino feliz de la guía de insumos, de `solicitarCierreSaldoOc`, de borrar una apertura de caja, de los saldos por banco y moneda, ni del mayor leyendo un asiento `COMPRA:` o `DOC:` de punta a punta. Esos tramos no se marcan como hechos.
