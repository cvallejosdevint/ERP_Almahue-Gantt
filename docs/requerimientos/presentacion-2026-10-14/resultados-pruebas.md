# Resultados de pruebas - presentacion 2026-10-14

Plan: `plan-pruebas.md` (P-01 a P-25). Contraste: `contraste-codigo.md`. Sala: `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md`.

Corrida del 15/10, local, empresa ALMAHUE EXPORT SPA. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`. Health de la API: 200, `db: ok`. Front: 200. Modo real: `localStorage almahue-erp-demo-mode = "false"`. Sesion `admin@almahue.local`, periodo de trabajo 2026-10. Pantalla con Playwright, ventana 1536x960, escala css.

No se emitio DTE, no se llamo al SII ni a GoSocket, no se pago, no se cerro el mes, no se reabrio un periodo y no se corrio `prisma migrate deploy`. No se pulso Traspasar y cerrar, no se ejecuto `solicitarCierreSaldoOc` y no se confirmo un vinculo. No se guardo un ingreso, una proforma, una guia ni una orden. No se envio correo.

Pasa solo el resultado esperado de la sala. Un verde de Jest que afirma el atajo de hoy queda anotado como resultado de hoy y no acredita el caso. Los limites del plan no se numeraron y no se convirtieron en prueba.

Jest, desde `ERP/erp_back`:

`npx jest --runInBand --no-coverage src/modules/aprobaciones/approval-engine.spec.ts src/modules/contratistas/contratistas.service.spec.ts src/modules/compras/oc-parcial.compras.service.spec.ts src/modules/insumos/precio-guia-oc.util.spec.ts src/modules/insumos/insumos.service.spec.ts`

Salida: 2 suites fallidas, 3 suites en verde, 2 tests fallidos, 73 en verde, 75 en total. El codigo de salida no es el veredicto.

## Recuento

| Resultado | Pruebas |
|---|---|
| Pasa | 10 |
| Falla | 15 |
| Bloqueo | 0 |

## P-01. Al elegir la labor, la actividad sale sola

- Resultado: falla
- Evidencia: pantalla Contratistas > Ingreso diario, boton Nuevo ingreso, sin pulsar Crear. Labor PACK-CER - Packing cereza export. El combo Actividad (filtrada por labor) quedo en Seleccionar. Al abrirlo aparecen SEL-CER - Seleccion y embalaje cereza y TEST - test. `IngresoLaborDiarioPage.tsx`, `onFieldChange` de `laborId`, deja `actividadId` vacio.
- Frase: se elige la labor y la actividad no queda puesta; hay que buscarla en el combo.

## P-02. El ingreso diario lleva el detalle y el gasto va a una sola cuenta

- Resultado: pasa
- Evidencia: el mismo formulario de ingreso pide Cuartel / centro de costo, Labor y Actividad. Nueva proforma pide contratista, periodo, moneda e ingresos pendientes; no hay campo de cuenta. La grilla de proformas muestra la columna Cuenta gasto con el texto fijo Mano de obra contratista (PF-00001 a PF-00005). `resolveCuentasCierreSala` debe `6-1-01-01-002` (o el nombre mano de obra contratista) y `traspasoCierre` glosa esa linea. El camino que arma una OC y exige `cuentaGastoId` no se uso como pase.
- Frase: el detalle esta en el ingreso, la proforma no pide cuenta por linea, y el gasto del traspaso es mano de obra contratista.

## P-03. Varios ingresos diarios arman una proforma

- Resultado: pasa
- Evidencia: Nueva proforma, sin pulsar Crear. El campo es Ingresos pendientes, tipo multicheck, `autoSelectAll: true`, y el hint dice que los pendientes compatibles vienen marcados y se pueden desmarcar. En 2026-10, ALM SERVICES SPA y Cuadrillas Packing Export Ltda no tenian ingresos pendientes, asi que la lista salio vacia. `previewProforma` y `createProforma` aceptan uno o varios, rechazan otro contratista, otro mes (`periodoDesdeFecha`) o un ingreso que ya no esta `PENDIENTE` o `PENDIENTE_APROBACION`, y al guardar los pasan a `ASOCIADO`.
- Frase: varios ingresos del mismo contratista y del mismo mes pueden quedar en una proforma y dejan de estar libres.

## P-04. La proforma la aprueba el jefe de campo

- Resultado: falla
- Evidencia: Contratistas > Aprobaciones, sin firmar. Titulo Aprobaciones de contratistas. Texto: pendientes del grupo de Contratistas. PF-00004, Cuadrillas Packing Export Ltda, solicitado a Bruno Lagos, cadena 0/2. No hay un rol jefe de campo en el fuente. `resolverCadenaProforma` aprueba el eslabon del grupo de tipo `PROFORMA`. `aprobarProformaDefinitiva` dice que la aprueba el eslabon pendiente. Jest `contratistas.service.spec.ts`, caso "bajo el primer piso queda DEFINITIVA sin aprobador pendiente", fallo: el servicio dejo `PENDIENTE_APROBACION` con aprobador U-SUP, no `DEFINITIVA` sola. `resolveEstadoIngresoNuevo`, si el alta manda `aprobadorId`, puede dejar el ingreso en `PENDIENTE_APROBACION`.
- Frase: quien aprueba es el eslabon del grupo, no un jefe de campo, y el ingreso suelto todavia puede armar cadena.

## P-05. El asiento del mes es uno, al cierre, y suma las proformas aprobadas

- Resultado: pasa
- Evidencia: `/contratistas/traspaso`, sin pulsar Traspasar y cerrar. El texto dice que toma las aprobadas del mes, de todos los contratistas, y que se incluiran 4 proformas por $44.800. `aprobarProformaDefinitiva` deja `DEFINITIVA` y no llama a contabilidad. `traspasoCierre` arma un asiento, origen `TRASPASO-CTR:{periodo}`, con `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA` de ese periodo. Un segundo cierre del mismo periodo se rechaza. El cierre en cero sin asiento no se uso como pase.
- Frase: aprobar no genera asiento, y el cierre del mes junta las aprobadas de ese mes en un solo asiento.

## P-06. El gasto queda en el mes de la proforma

- Resultado: pasa
- Evidencia: `traspasoCierre` filtra `proforma.periodo`, no la fecha del registro de compra. No se cerro el mes y no se asocio una factura. Una proforma de octubre entra al cierre de octubre aunque la factura se asocie despues, y tambien si ya esta `FACTURADA`.
- Frase: el mes del gasto es el mes de la proforma, no la fecha de la factura.

## P-07. Mano de obra contra facturas por recibir, y despues la factura contra el proveedor

- Resultado: falla
- Evidencia: `resolveCuentasCierreSala` debe mano de obra y haber `2-1-08-02-003` (o el nombre de facturas por recibir). No se contabilizo ni se cargo un registro. `planAsientoRegistroCompra`, si la proforma quedo ligada y hay tipo, pone el debe en `tipo.cuentaHaber`, no en el codigo del haber del cierre, y el haber en proveedores (`COMPRA:{factura}`). Si no hay tipo, el asiento puede ir a la cuenta de gasto de la OC. `asociarFacturaProforma` sin `registroCompraId` crea una OC `PROFORMA_CONTRATISTA` y marca `FACTURADA`. Ese camino no se uso como pase.
- Frase: el cierre es la primera partida de la sala, y la factura recibida no saca esa misma cuenta de facturas por recibir.

## P-08. El cierre es un menu bajo auditoria

- Resultado: falla
- Evidencia: menu Contratistas, en este orden: Listado, Ingreso diario, Proformas y facturas, Aprobaciones, Reporte ingresos, Auditoria, Traspaso contable y cierre de mes. La pagina `/contratistas/traspaso` tiene ese titulo. No es un boton de la fila de proforma (ahi estan Items, PDF, Notificar, Facturar, Reversar, Reemitir). El periodo que cierra es el del encabezado, 2026-10. No hay campo de mes en el formulario. El boton Traspasar y cerrar cierra ese periodo. El historico dice que un clic cambia el periodo de trabajo del sitio.
- Frase: el menu tiene el nombre y queda debajo de Auditoria, y en esa pantalla el usuario no informa el mes que cierra.

## P-09. Al traspaso entran todas las aprobadas y la pendiente no es gasto

- Resultado: pasa
- Evidencia: la misma pantalla, sin cerrar. Grilla de 2026-10: 5 proformas, 4 elegibles. PF-00005, PF-00003, PF-00002 y PF-00001 estan `ENVIADA CONTRATISTA` (dos contratistas). PF-00004 esta `PENDIENTE APROBACION` y se ve en la misma grilla. El texto dice que las pendientes se ven y no entran al asiento. `elegibles` suma solo `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA`. Es una fila por proforma.
- Frase: estan las aprobadas de todos los contratistas, una fila por proforma, y la pendiente se ve y queda fuera del asiento.

## P-10. La proforma aprobada se puede avisar al contratista por correo

- Resultado: pasa
- Evidencia: modal Notificar de una proforma ya notificada, sin pulsar Enviar. El destinatario de ese modal es Usuario destino, un usuario del ERP. La copia al contratista solo aparece si se marca el correo. Esa entrada no acredita. `/contratistas/envio-operativo` redirige a `/contratistas/proformas`. `createEnvioOperativoContratista`, si `enviarEmail`, llama a `enviarEmailsProformasContratista`: el `to` es el email de la ficha del contratista y el mensaje adjunta `proforma-{numero}.pdf` con el detalle de ingresos. No se envio, asi que la falta de SMTP no se trato como bloqueo. Que sigan dos entradas no se falla.
- Frase: con la proforma lista, el envio operativo deja al contratista como destinatario y el mensaje lleva el documento.

## P-11. El correo de la orden de compra es interno

- Resultado: pasa
- Evidencia: Libro de compras, factura #62, boton Notificar usuario / correo, sin pulsar Enviar. Campos: Usuario destino y Enviar tambien por correo electronico. El correo destino del modal se carga con el email de ese usuario. El fuente ofrece copia al que envia, copia a quien genero la orden y copia adicional. No se abrio el PDF ni el XML de GoSocket. No se sincronizo.
- Frase: el destinatario previsto del correo de compras es un usuario interno del ERP.

## P-12. La madre es la negociacion y se contabiliza la hija

- Resultado: falla
- Evidencia: Compras > Ordenes de compra, sin recepcionar ni vincular ni contabilizar. El listado trae juntas `#OC-2026-0021` (pendiente de aprobacion) y `#OC-2026-0021-1` (hija, aprobada). `assertRegistroContabilizableOcMadre` solo rechaza la madre si ya tiene hijas activas. Si no tiene hijas, no frena. Jest `oc-parcial.compras.service.spec.ts` dejo en verde "recepcion por el neto completo no nace hija y la OC queda RECEPCIONADA". `splitOcMadreCreaHijaPorMontos` deja la factura en la madre. Esos verdes afirman el atajo y no acreditan. Un test de ese archivo fallo al asignar folio hija (`No se pudo asignar folio hija para OC-100`); tampoco acredita.
- Frase: la madre se puede contabilizar y el libro puede dejar la factura en la madre.

## P-13. La hija nace al recepcionar la guia en insumos

- Resultado: falla
- Evidencia: Insumos > Guias de insumos recibidas. La pagina cargo: "Esta empresa no recibe insumos con guia." No se guardo una guia. El alta de `GuiasInsumosRecibidasPage` pide numero de guia fisica, proveedor, articulo, cantidad y bodega. `createGuiaInsumoRecibida` crea `ENTRADA_PROVEEDOR` y la fila de guia. No recibe la orden madre y no crea hija. `precioGuiaDesdeOrden` solo toma un precio. La hija que el codigo crea entra por Compras > Recepciones o por `splitOcMadreCreaHijaPorMontos`. Esos caminos no acreditan.
- Frase: la guia de insumos no se recepciona contra la madre y de ese parcial no nace la hija.

## P-14. Varias guias del mes y una factura: en compras se asocian las hijas

- Resultado: falla
- Evidencia: Libro de compras, factura #63, boton Asociar orden, sin pulsar Vincular OC. El formulario tiene un solo campo Orden de compra y el boton Vincular OC. El texto del modal dice que se elige una orden aprobada del mismo proveedor. Si el monto es parcial contra una madre, al vincular el neto de la madre queda en el monto del documento y se crea una hija por el saldo. No hay marcas de varias hijas. `preferirHijaAprobadaSinFactura` solo corre al leer un XML y no se uso.
- Frase: el libro elige una orden, y no deja marcar varias hijas ya nacidas de lo recepcionado.

## P-15. Las guias se ven en insumos, no en el libro de compras

- Resultado: pasa
- Evidencia: la ruta de guias es `/insumos/guias-recibidas`, titulo Guías de insumos recibidas, bajo Insumos / Bodega. El menu de insumos no tiene libro de compras. El Libro de compras lista facturas (tipo, razon social, OC, match) y no ofrece la guia como linea para asociar. Que la guia no guarde la madre es P-13.
- Frase: las guias estan en insumos, insumos no tiene libro de compras, y el libro de compras no asocia la guia.

## P-16. Insumos ve madre e hija y compras solo ve la hija lista para contabilizar

- Resultado: falla
- Evidencia: el listado de compras trae madre e hija en borrador, pendiente y aprobado, y muestra "Hija de" cuando hay padre. Una madre pendiente se abre en el mismo listado. El menu Insumos / Bodega tiene maestro, bodegas, stock, movimientos, cierre de bodega y guias. No tiene listado de ordenes. No se asocio ni se recepciono.
- Frase: compras muestra madre e hija en cualquier estado, e insumos no muestra ninguna de las dos.

## P-17. Servicio es una a una e insumos llega por partes

- Resultado: falla
- Evidencia: `/compras/ordenes/nueva`, sin Guardar borrador y sin Enviar a aprobacion. Campos: proveedor, condicion de pago, fecha, moneda, afecto / exento y Departamento. No hay tipo servicio ni tipo insumos. El departamento sale del grupo (`ocDepartamentoDesdeGrupo`). Cualquier orden aprobada puede partirse en la recepcion de compras o en el vinculo del libro.
- Frase: no hay dos flujos; servicio e insumos siguen el mismo corte.

## P-18. La madre la crea el jefe y la hija, el administrativo

- Resultado: falla
- Evidencia: el mismo alta, sin crear la orden. `createOrden` pide permiso de compras y pertenencia a un grupo de aprobacion de Compras. El texto de la pantalla dice que solo Enviar a aprobacion pide firma. No hay un permiso de jefe para la madre ni de administrativo de insumos para la hija. La guia la crea quien tiene insumos, y esa guia no crea la hija. La hija de recepcion y la del saldo las crean quien confirma la recepcion en compras o quien vincula la factura.
- Frase: la madre la puede crear cualquier usuario del grupo, y la hija no nace cuando el administrativo recepciona la guia.

## P-19. No hay monto que se salte la aprobacion

- Resultado: falla
- Evidencia: no se envio una orden a la bandeja. `buildCadenaAprobacion` y `buildCadenaDesdeGrupo`: `pasoExigidoPorMonto` solo corre si `chain.length > 0`. El primer eslabon entra con un monto chico. Del segundo en adelante, si el monto no alcanza el tope, el eslabon se omite. Jest `approval-engine.spec.ts` en verde: "incluye al jefe cuando el monto alcanza su piso y no al siguiente" espera solo `U-MARIO`; "sobre el piso del siguiente incluye ambos escalones" espera `U-MARIO` y `U-AGUS`. Ese verde afirma el tramo que se salta y no acredita. `bajo_umbral` lanza error y no deja la orden `APROBADO` sola: eso tampoco acredita mientras los eslabones de arriba se omitan.
- Frase: una orden chica entra al primer eslabon y los siguientes se omiten si el monto no alcanza el tope.

## P-20. Subir o bajar la madre vuelve a pasar por aprobacion

- Resultado: falla
- Evidencia: no se edito una orden ni se recepciono. `updateOrden`: si el total de una `APROBADO` sube o baja, `montoCambia` la deja en `PENDIENTE_APROBACION`. `RECEPCIONADA`, `CONTABILIZADA` y `FACTURADO` no se editan. La guia de insumos no lee el cupo ni `cerradaAt`. `assertTopeRecepcion` frena la recepcion de compras y no la guia. Devolver la madre a la cadena al vincular la factura no se uso como pase.
- Frase: subir o bajar la madre vuelve a la cadena, y la guia se puede recepcionar igual aunque no haya cupo.

## P-21. Cerrar la madre por menos se hace en insumos

- Resultado: falla
- Evidencia: el menu de insumos no tiene la accion de cerrar la madre. Tiene Cierre de bodega, que es otro cierre. `CierreSaldoOcModal` esta en Compras > Ordenes de compra (`ComprasPages.tsx`). No se ejecuto `solicitarCierreSaldoOc`. Jest `oc-parcial.compras.service.spec.ts` dejo en verde el cierre que achica la madre en compras y la deja `PENDIENTE_APROBACION`. Ese verde es el listado de compras y no acredita. La guia no lee la madre cerrada.
- Frase: cerrar por menos esta en el listado de compras, no en insumos, y la guia no deja de recibir el saldo cortado.

## P-22. El pendiente de la madre se mira en insumos

- Resultado: falla
- Evidencia: no se vinculo. En el libro, la factura #62 muestra "Saldo · hija OC-2026-0021-1" y una diferencia de $20.000. `calcularMatchOc` compara el monto del registro con el neto de la orden y, si es parcial contra una madre, dispara el corte. El menu de insumos muestra stock por bodega, no el saldo de la madre. El detalle de lo recibido vive en la orden de compras.
- Frase: el pendiente de la madre se ve en compras y el libro lo usa para partir la orden, no en insumos.

## P-23. Los reportes contables salen en PDF y el estado de resultados tambien en Excel

- Resultado: falla
- Evidencia: sin cerrar el mes y sin pulsar las exportaciones. Libro diario, libro mayor y balance de 8 columnas muestran Exportar Excel/CSV y Exportar PDF. El comprobante, en el detalle del asiento, tiene Imprimir (`imprimirComprobante`, ventana de impresion) y no Excel. Estado de resultados (`/contabilidad/estado-resultados`) muestra la grilla y no tiene boton de Excel ni de PDF. Excel y PDF de diario, mayor y balance no cubren el estado de resultados.
- Frase: cuatro reportes tienen salida, y el estado de resultados no exporta a PDF ni a Excel.

## P-24. Con factura recibida, la proforma no se edita

- Resultado: pasa
- Evidencia: en la grilla de proformas de 2026-10 no hay una `FACTURADA` (hay notificadas y una pendiente). No se guardo ni se edito un ingreso. `updateProforma` solo acepta `BORRADOR` y rechaza cambiar numero, periodo, moneda o ingresos en otro estado. `patchCentrosCostoProforma` rechaza la `FACTURADA` o la que ya tiene orden. `updateIngresoLaborDiario` solo edita `PENDIENTE` o `PENDIENTE_APROBACION`. El candado desde `ASOCIADO`, antes de la factura, quedo fuera de esta prueba.
- Frase: la proforma `FACTURADA` no cambia ingresos ni montos.

## P-25. El dia sin proforma no se corre de mes, y una factura puede tomar varias

- Resultado: pasa
- Evidencia: no se cerro el mes, no se asocio y no se uso el camino sin registro. `traspasoCierre` no reasigna ni contabiliza un ingreso sin proforma. `createProforma` acepta un solo ingreso de ese mes. `asociarFacturaProforma` con `registroCompraId` toma varias proformas del mismo contratista, moneda y tipo, y cada una pasa entera a `FACTURADA`. Si la suma supera el neto, rechaza. Si es menor, la factura conserva saldo y no deja una proforma facturada por una parte de sus lineas. Crear una OC y marcar `FACTURADA` sin registro no acredita.
- Frase: el dia suelto no cambia de mes, puede armar su proforma de un dia, y un registro del libro toma varias proformas enteras.
