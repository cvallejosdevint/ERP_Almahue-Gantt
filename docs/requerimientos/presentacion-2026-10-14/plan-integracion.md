# Plan de integracion - presentacion 2026-10-14

Fuente de los casos: `casos-de-uso.md` (CU-01 a CU-25), sala `transcripcion-2026-10-14-presentacion.md`. Este documento dice, por caso, por donde entra hoy, que deja el codigo hoy, que pide la sala y de que otros casos depende. No redefine pantallas y no propone un parche.

Contraste leido en el codigo del 15/10 (`ERP/erp_back`, `ERP/erp_front`). Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`, API `http://localhost:3001/api/v1`. No se emite DTE, no se paga, no se cierra el mes y no se corre migrate.

Lo que `casos-de-uso.md` dejo abierto (precio cero, edicion de la proforma aprobada sin factura, nota de credito, uno o dos menus, segunda modificacion de la madre, cabecera del PDF, monedas del comprobante, historial del rechazo, si la hija pasa por la cadena, varias lineas con centros distintos, canal de la guia, folio con guion, silencio del contratista, tipo de cambio en el cierre) no es caso y no se integra aqui.

## Ancla: por donde entra el flujo hoy

| Entrada | Donde esta | Que deja el codigo |
|---|---|---|
| Ingreso diario | Contratistas, `IngresoLaborDiarioPage` y `createIngresoLaborDiario` | Fila con fecha, contratista, centro de costo, labor, actividad, cantidad y precio. La actividad se elige en un combo filtrado por la labor. Sin `aprobadorId` queda `PENDIENTE`. |
| Proforma | Contratistas, `ProformasContratistaNivel1Page` y `createProforma` | Agrupa ingresos del mismo contratista y del mismo mes. El formulario pide contratista, periodo, moneda e ingresos. No pide cuenta de gasto. `cuentaGastoId` queda vacio si no viene. Los ingresos pasan a `ASOCIADO`. |
| Aprobacion de proforma | Contratistas, `marcarProformaDefinitiva` y `aprobarProformaDefinitiva` | Cadena del grupo de proformas. `bajo_umbral` lanza error. Al completar la cadena el estado es `DEFINITIVA`. No crea asiento. |
| Traspaso del mes | Menu Contratistas, item siguiente a Auditoria, rotulo "Traspaso contable y cierre de mes", ruta `/contratistas/traspaso`. Servicio `traspasoCierre` | Un asiento `TRASPASO-CTR:{periodo}`: debe `6-1-01-01-002`, haber `2-1-08-02-003`, debe partido por centro de costo. El periodo es el del encabezado. La pantalla no pide tipo de cambio. |
| Factura del contratista | `asociarFacturaProforma` | Con registro del libro, marca las proformas `FACTURADA` y no arma asiento. Sin registro, crea una OC `PROFORMA_CONTRATISTA`. El asiento de la factura, si despues se contabiliza el registro, es `planAsientoRegistroCompra`. |
| Orden de compra | Compras, `createOrden` y `updateOrden`. Cadena `resolveCadenaAprobacion` | Al enviar, el primer eslabon no se salta por monto chico. `bajo_umbral` lanza error. No hay tipo servicio ni insumos. |
| Recepcion de OC | Compras, `createRecepcion` y `updateRecepcion`. Hija en `crearOcHijaDeRecepcion` | Si el trozo es menor que la madre, nace hija `APROBADO` `{madre}.{n}`. El asiento de recepcion cuelga de la hija. La madre no pasa a `RECEPCIONADA`. |
| Vinculo de factura a OC | Libro de compras, `vincularOcRegistroCompra`. Sigue llamando a `splitOcMadreCreaHijaPorMontos` | Si el monto es menor que la madre, la factura queda en la madre, la madre baja su neto a ese monto y vuelve a `PENDIENTE_APROBACION`, y la hija es el saldo que no vino en la factura. |
| Cierre de saldo | Compras, `solicitarCierreSaldoOc`, modal en el listado de ordenes | Si lo recibido es menor, la madre baja a ese neto y vuelve a aprobacion. No abre hija por lo que no llega. |
| Guia de insumos | Insumos, `GuiasInsumosRecibidasPage` y `createGuiaInsumoRecibida` | Movimiento `ENTRADA_PROVEEDOR` y fila de guia. No pide madre. No crea hija. |
| Reportes | Contabilidad, libro diario, libro mayor, balance de 8 columnas, comprobantes, estado de resultados | Diario, mayor y balance exportan Excel y PDF. El comprobante abre la ventana de impresion. El estado de resultados no tiene Excel ni PDF. |

## CU-01. Al elegir la labor, la actividad sale sola

- Entra hoy: Contratistas > Ingreso diario. Al cambiar `laborId`, el front pide `getActividades(laborId)` y vacia `actividadId`. El alta es `createIngresoLaborDiario`, que exige el par en `laborActividad`.
- Deja el codigo: la actividad no se completa sola. El combo queda filtrado a las actividades parametrizadas de esa labor, y la persona tiene que elegir una. Si la labor no tiene ninguna, el combo queda vacio y el guardado rechaza el par.
- Pide la sala: en el ingreso diario se elige la labor y la actividad asociada aparece sola. El ingreso es el que usa el area agricola.
- Depende de: la parametrizacion labor-actividad que ya lee `getActividades`. El detalle que esa fila guarda lo usa CU-02. El agrupado de esas filas es CU-03.

## CU-02. El ingreso diario lleva el detalle; el gasto va a una sola cuenta

- Entra hoy: el ingreso (`centroCostoId`, `laborId`, `actividadId`) y la proforma (`createProforma`). El asiento del mes entra por `traspasoCierre` y `resolveCuentasCierreSala`.
- Deja el codigo: el formulario de la proforma no pide cuenta de gasto. `resolveCuentaGastoProforma` guarda null si no viene cuenta. El traspaso no usa `cuentaGastoId` ni la cuenta del tipo de contrato: debe `6-1-01-01-002` (o, si no esta ese codigo, una cuenta de gasto cuyo nombre es mano de obra contratista) y agrupa el debe solo por centro de costo. Labor y actividad quedan en el ingreso y no salen en la linea del asiento. El camino que genera OC desde la proforma (`buildLineasOrdenCompraDesdeIngresosProformas`) sigue pidiendo `cuentaGastoId` y rechaza la proforma si viene vacia.
- Pide la sala: centro de costo, labor y actividad quedan en el ingreso diario. La proforma no pide una cuenta distinta por linea. El gasto de esas lineas es la cuenta mano de obra contratista.
- Depende de: CU-01 (la fila del ingreso) y CU-03 (la proforma como agrupado). El asiento que usa la cuenta es CU-05 y CU-07.

## CU-03. Varios ingresos diarios arman una proforma

- Entra hoy: Nueva proforma en Contratistas > Proformas y facturas. El multicheck `ingresoIds` lista pendientes del contratista, del tipo operativo y del periodo. `createProforma` / `previewProforma` marcan esos ingresos `ASOCIADO`.
- Deja el codigo: se pueden tomar varios ingresos, o uno solo si se desmarcan los demas. El servidor rechaza un ingreso de otro contratista, de otro mes (`periodoDesdeFecha`) o que ya no este `PENDIENTE` o `PENDIENTE_APROBACION`. Al guardar, esos ingresos no quedan libres para otra proforma. Vienen todos marcados; hay que desmarcar para dejar un dia afuera.
- Pide la sala: la proforma es el agrupado de los ingresos diarios elegidos de ese contratista. Esos ingresos ya no quedan libres para otra proforma. No hace falta una proforma por dia, salvo el dia suelto de CU-25.
- Depende de: CU-01 y CU-02 (que el ingreso ya traiga labor, actividad y centro de costo). La aprobacion de ese agrupado es CU-04. El dia que no entra es CU-25.

## CU-04. La proforma la aprueba el jefe de campo

- Entra hoy: enviar la proforma en borrador (`marcarProformaDefinitiva`) y firmarla en Contratistas > Aprobaciones (`aprobarProformaDefinitiva`). La cadena sale de `resolverCadenaProforma`, modulo Contratistas, grupo de tipo `PROFORMA`.
- Deja el codigo: no hay un rol llamado jefe de campo. Aprueba el eslabon pendiente de esa escala. `bajo_umbral` lanza error y no deja la proforma definitiva sola. El tramo que pondria `DEFINITIVA` con motivo `bajo_umbral` sigue escrito en `marcarProformaDefinitiva`, y `resolverCadenaProforma` no lo alcanza: o devuelve cadena o lanza error. Al cerrar el ultimo paso el estado es `DEFINITIVA` y no hay asiento. El ingreso, si el alta no manda `aprobadorId`, queda `PENDIENTE` y no arma su propia cadena; si el alta manda aprobador, el ingreso si puede quedar `PENDIENTE_APROBACION`.
- Pide la sala: sin aprobacion del jefe de campo la proforma no queda lista para el traspaso. La aprobacion es de la proforma, no de cada ingreso suelto.
- Depende de: CU-03 (tiene que existir la proforma con ingresos). Quien entra al mes es CU-05 y CU-09. El aviso posterior es CU-10.

## CU-05. El asiento del mes es uno, al cierre, y suma las proformas aprobadas

- Entra hoy: Contratistas > Traspaso contable y cierre de mes, boton Traspasar y cerrar. El servicio es `traspasoCierre`. Aprobar (`aprobarProformaDefinitiva`) no llama a contabilidad.
- Deja el codigo: un asiento por periodo, origen `TRASPASO-CTR:{periodo}`, con las proformas `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA` de ese periodo. El debe va por centro de costo a `6-1-01-01-002` y el haber, en una sola linea, a `2-1-08-02-003`. Si el monto es 0, cierra el periodo sin asiento. Un segundo cierre del mismo periodo se rechaza. Reabrir existe (`reabrirCierreContratista`) y la sala no lo pidio. Aprobar una proforma no genera asiento.
- Pide la sala: aprobar una proforma no genera el asiento. Al cerrar el mes, las proformas aprobadas de ese mes salen en un asiento centralizado. No se contabiliza contratista por contratista.
- Depende de: CU-04 (aprobada), CU-02 y CU-07 (las dos cuentas), CU-08 (el menu) y CU-09 (la pendiente no entra). El mes del gasto es CU-06.

## CU-06. El gasto queda en el mes de la proforma

- Entra hoy: el periodo de la proforma, que el traspaso filtra (`periodo` del encabezado contra `proforma.periodo`). La factura entra despues por `asociarFacturaProforma` y no reescribe ese periodo.
- Deja el codigo: el asiento usa el periodo de la proforma, no la fecha del registro de compra. Una proforma de octubre entra al cierre de octubre aunque la factura se asocie en noviembre, y tambien entra si ya esta `FACTURADA`. El ingreso suelto, sin proforma, no se mueve de mes: CU-25.
- Pide la sala: el mes del gasto es el mes de la proforma aprobada. No se espera la fecha de la factura para reconocer ese gasto.
- Depende de: CU-05 (el asiento del cierre) y CU-03 (el periodo nace con la proforma). La segunda partida, cuando llega la factura, es CU-07.

## CU-07. Mano de obra contra facturas por recibir, y despues la factura contra el proveedor

- Entra hoy: la primera partida en `traspasoCierre` / `resolveCuentasCierreSala`. La segunda, si alguien contabiliza el registro, en `planAsientoRegistroCompra`. Asociar (`asociarFacturaProforma` con `registroCompraId`) no crea asiento: solo deja la proforma `FACTURADA`.
- Deja el codigo: el cierre debe `6-1-01-01-002` y haber `2-1-08-02-003` (si falta el codigo, busca por nombre "MANO DE OBRA CONTRATISTA" y "FACT X RECIBIR CONTRATISTAS"). No usa la cuenta del proveedor. Al contabilizar el registro, si la proforma quedo ligada por `registroCompraId`, `tipoContratoDeRegistro` toma el tipo y el debe es `tipo.cuentaHaber`, no el codigo `2-1-08-02-003` del cierre. El haber de esa factura es proveedores (`origen COMPRA:{factura}`). Si el haber del tipo no es la misma cuenta del cierre, las dos partidas no se encuentran. Si no hay tipo en la proforma ligada, el asiento de la factura puede ir a la cuenta de gasto de la OC y repetir el gasto. El otro camino de asociar, sin registro, crea una OC y tampoco publica esta segunda partida.
- Pide la sala: centralizar no usa la cuenta del proveedor. Asociar la factura recibida saca facturas por recibir y deja al proveedor. El gasto no se duplica.
- Depende de: CU-05 y CU-06 (el haber ya esta en el mes de la proforma) y CU-02 (una sola cuenta de gasto). La proforma facturada que ya no se edita es CU-24. Varias proformas en una factura es CU-25.

## CU-08. El cierre es un menu bajo auditoria

- Entra hoy: `Sidebar.tsx`, grupo Contratistas. Despues del item Auditoria (`/contratistas/auditoria`) esta Traspaso contable y cierre de mes (`/contratistas/traspaso`). La pagina es `TraspasoContratistasPage`.
- Deja el codigo: el rotulo del menu y el titulo de la pagina son "Traspaso contable y cierre de mes". Queda en el mismo menu, inmediatamente despues de Auditoria. No es un subitem de la pantalla de auditoria. El mes no se tipea en el formulario: se usa el periodo del encabezado del sitio (`usePeriodoScopeCodigo`). La pantalla muestra ese periodo y el boton cierra ese mes. No hay campo de tipo de cambio. Ejecutar pide `contratistas:transfer` y `contratistas:close`.
- Pide la sala: el cierre no es un boton suelto en cada proforma. Es el menu "Traspaso contable y cierre de mes", bajo auditoria, y el usuario dice que mes cierra.
- Depende de: CU-05 (lo que ese menu ejecuta) y CU-09 (el listado de esa pantalla). El tipo de cambio en esta pantalla no es caso: la sala del 14/10 no lo repitio.

## CU-09. Al traspaso entran todas las aprobadas; la pendiente no es gasto

- Entra hoy: la grilla de `TraspasoContratistasPage` (`delPeriodo`, todas las proformas cuyo periodo calza) y el filtro `elegibles` que arma el cuerpo de `traspasoCierre`.
- Deja el codigo: la grilla lista todas las del periodo, de todos los contratistas, incluida la `PENDIENTE_APROBACION` y el borrador. El asiento solo suma `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA`. La pendiente se ve y su columna Contabilidad no la marca como gasto. No es una fila por contratista: es una fila por proforma.
- Pide la sala: se listan todas las aprobadas. Una pendiente se puede ver, y no se contabiliza.
- Depende de: CU-04 (que exista el estado aprobado), CU-05 (el asiento) y CU-08 (la pantalla). La ya facturada sigue en el mismo mes por CU-06.

## CU-10. La proforma aprobada se puede avisar al contratista por correo

- Entra hoy: notificar desde la proforma (`notificarProforma`, `ProformaNotificarModal`) y el envio operativo (`enviarEmailsProformasContratista`, `EnvioOperativoContratistasPage`).
- Deja el codigo: notificar exige una proforma aprobada o ya notificada y un usuario del ERP de la empresa. El aviso interno queda siempre. El correo, si se marca, sale al email de ese usuario y puede adjuntar el PDF. Puede copiar el email del contratista (`copiarContratista`) y otras direcciones (`correoCopia`). El envio operativo, si se pide email, manda el PDF al correo de la ficha del contratista. Siguen siendo dos entradas. Sin `SMTP_HOST` el aviso interno queda y el correo no sale.
- Pide la sala: existe el aviso por correo al contratista, con el documento de la proforma. Unir o no los dos botones no quedo dicho.
- Depende de: CU-04 (la proforma tiene que estar aprobada para el aviso que el codigo exige). No depende del cierre: el aviso es anterior a CU-05.

## CU-11. El correo de la orden de compra es interno

- Entra hoy: Libro de compras, modal Notificar (`RegistroCompraNotificarModal`, `notificarRegistroCompra`). La plantilla es el concepto `COMPRAS`. No hay un envio propio en el alta de la orden.
- Deja el codigo: el destinatario es un usuario del ERP con acceso a la empresa. El aviso interno va a ese usuario. El correo opcional sale al email de su ficha y puede llevar PDF o XML del DTE si el registro tiene documento GoSocket. El modal sigue ofreciendo copia al remitente, copia a quien genero la orden y un campo de correos extra (`correoCopia`).
- Pide la sala: el destinatario previsto del correo de compras es un usuario interno del departamento. La pantalla para copiar a externos no la pidio el cliente en esta sala.
- Depende de: ninguno de contratistas. Es el aviso del documento de compras, distinto del aviso al contratista (CU-10). No cambia madre ni hija.

## CU-12. La madre es la negociacion; se contabiliza la hija

- Entra hoy: la OC en Compras (`createOrden`). La hija puede nacer en la recepcion de compras (`crearOcHijaDeRecepcion`) o al vincular una factura parcial (`splitOcMadreCreaHijaPorMontos`, llamado desde `vincularOcRegistroCompra`). Contabilizar el registro pasa por `assertRegistroContabilizableOcMadre` y `planAsientoRegistroCompra`.
- Deja el codigo: no hay un documento marcado "solo negociacion". `getOrdenes` devuelve madre e hija juntas. Una recepcion parcial contabiliza la hija (`RECEPCION:{hija}`) y no mueve la madre a `RECEPCIONADA`. Una recepcion por el total contabiliza la madre y la deja `RECEPCIONADA`. Al vincular una factura de menor monto, la factura queda asociada a la madre, no a una hija de lo recibido. Si la madre ya tiene hijas activas, contabilizar esa factura se rechaza y el mensaje pide la factura de la hija.
- Pide la sala: la madre no se contabiliza. La hija si puede contabilizarse. La madre no se asocia en el libro de compras como si fuera la orden que calza la factura.
- Depende de: CU-13 (de donde nace la hija) y CU-14 (que la factura tome hijas ya nacidas). La aprobacion de la madre es CU-19 y CU-20. El mundo insumos es CU-15 y CU-16.

## CU-13. La hija nace al recepcionar la guia en insumos

- Entra hoy: Insumos > Guias de insumos recibidas, `createGuiaInsumoRecibida`. La hija que el codigo si crea entra por Compras > Recepciones (`createRecepcion`) o por el vinculo del libro (`vincularOcRegistroCompra`).
- Deja el codigo: la guia pide numero fisico, proveedor, articulo, cantidad y bodega. Crea `ENTRADA_PROVEEDOR` y la fila de guia. No recibe `ocId`, no busca la madre y no crea hija. El precio sale de una orden aprobada del mismo proveedor, o del maestro, y no parte la orden. En compras, la hija de la recepcion es el trozo recibido (`APROBADO`, sin cadena nueva) y la hija del vinculo es el saldo no facturado, con la madre devuelta a aprobacion.
- Pide la sala: sin madre no hay donde asociar la guia. Al recepcionar la guia contra la madre, queda creada la hija por el parcial de esa guia. El libro de compras no crea la hija. Insumos es el unico modulo de este flujo.
- Depende de: CU-12 (la madre existe y no se contabiliza) y CU-18 (quien recepciona es el administrativo). El cupo para poder recepcionar es CU-20. La guia no se asocia en el libro: CU-14 y CU-15.

## CU-14. Varias guias del mes y una factura: en compras se asocian las hijas

- Entra hoy: Libro de compras, `vincularOcRegistroCompra` y el modal `AsociarOcRegistroCompraModal`. El listado de ordenes es `getOrdenes`.
- Deja el codigo: se elige una OC. Si el monto de la factura es menor que el neto de una madre sin hijas, `splitOcMadreCreaHijaPorMontos` corre igual: achica la madre al monto de la factura, la pone `PENDIENTE_APROBACION` y crea una hija por el saldo. La factura queda con el `ocId` de la madre. Si ya hay una hija, el vinculo exige elegir la hija cuyo neto coincida; no ofrece marcar varias hijas en una misma factura. `preferirHijaAprobadaSinFactura` solo corre al leer referencias de un XML (`linkOrdenCompraFromReferencias`) y, si el neto calza, mueve el vinculo a una hija ya aprobada y sin factura. No lista "lo que llego".
- Pide la sala: una factura puede tomar varias hijas del mismo proveedor, hijas que ya nacieron de las guias. El listado es lo que llego, no un calce solo por monto. La guia no es la linea que se asocia.
- Depende de: CU-13 (las hijas ya existen) y CU-12 (la madre no es la orden del libro). El libro no muestra la guia: CU-15.

## CU-15. Las guias se ven en insumos, no en el libro de compras

- Entra hoy: Insumos > Guias de insumos recibidas (`getGuiasInsumoRecibidas`). Compras > Libro de compras (`getRegistros`).
- Deja el codigo: insumos lista numero, proveedor, articulo, cantidad y bodega. No tiene libro de compras. El libro de compras lista registros de factura y asocia ordenes; no lista `guiaInsumoRecibida` para marcarla. La guia no guarda la madre ni la hija.
- Pide la sala: insumos tiene libro de guias y no tiene libro de compras. El libro de compras no lista la guia para asociarla. Cuando la hija ya esta y se asocia a la factura, recien pasa al libro de compras.
- Depende de: CU-13 (la guia es el alta en insumos) y CU-14 (en el libro se asocia la hija, no la guia).

## CU-16. Insumos ve madre e hija; compras solo ve la hija lista para contabilizar

- Entra hoy: Compras > Ordenes de compra (`getOrdenes`, `ComprasPages`) y el selector del libro. Insumos no tiene listado de ordenes: tiene maestro, bodegas, stock, movimientos, cierre de bodega y guias.
- Deja el codigo: el listado de compras trae madre e hija, en cualquier estado, y muestra "Hija de" cuando hay `ocPadreId`. Una madre aprobada y no recepcionada se puede abrir y, si esta aprobada, se puede elegir al asociar. Insumos no muestra la madre ni la hija. Quien solo tiene `insumos:read` no ve las ordenes en su modulo.
- Pide la sala: la madre no aparece para asociar en compras. La hija aparece en compras solo si ya fue recepcionada. Insumos muestra madre e hija. El perfil de insumos no depende de entrar a compras para ver lo suyo. Una orden pendiente o solo aprobada, si no esta recepcionada, en compras no existe.
- Depende de: CU-13 (la hija nace recepcionada en insumos), CU-15 (las guias viven ahi) y CU-18 (el administrativo de abastecimiento trabaja en insumos).

## CU-17. Servicio es una a una; insumos llega por partes

- Entra hoy: la misma OC de `createOrden`. No hay campo de tipo servicio o insumos. El departamento sale del grupo de aprobacion (`ocDepartamentoDesdeGrupo`). La particion la deciden `crearOcHijaDeRecepcion` y `splitOcMadreCreaHijaPorMontos` para toda madre sin `ocPadreId`.
- Deja el codigo: cualquier orden aprobada puede recepcionarse por un monto menor y nacer hija. No hay un flujo de aprobacion distinto por tipo. Una orden de servicio, si alguien la recepciona o la factura por menos del neto, sigue el mismo corte que un insumo.
- Pide la sala: el flujo de madre, guia e hija es solo insumos. La de servicio se aprueba, se recepciona y es siempre una a una. La regla de aprobacion se puede distinguir por esos dos tipos.
- Depende de: CU-12 y CU-13 (el corte es solo del insumo) y CU-19 (la cadena, que la sala acepto poder separar por tipo).

## CU-18. La madre la crea el jefe; la hija, el administrativo

- Entra hoy: crear la OC es Compras > Ordenes, `createOrden`, con permiso de compras y pertenencia a un grupo de aprobacion de Compras. La hija de recepcion la crea quien confirma la recepcion en compras. La hija del saldo la crea quien vincula la factura parcial. La guia la crea quien tiene insumos y la empresa con `recibeInsumosConGuia`.
- Deja el codigo: no hay un permiso "solo el jefe crea la madre" ni "solo el administrativo crea la hija". Cualquier usuario del grupo puede enviar la orden a la cadena. La guia no crea la hija, asi que el administrativo de insumos no genera la orden hija al recepcionar.
- Pide la sala: crear la madre no esta abierto a cualquiera del grupo. La crea el jefe. Crear la hija es del administrativo de insumos, en la recepcion de la guia, no un alta manual en compras.
- Depende de: CU-13 (el alta de la hija es la guia) y CU-19 (la madre, una vez creada por el jefe, entra a la cadena).

## CU-19. No hay monto que se salte la aprobacion

- Entra hoy: al enviar la OC (`createOrden` / `updateOrden` cuando `ocEnviaAprobacion`) y al enviar la proforma (`marcarProformaDefinitiva`). La cadena la arman `buildCadenaDesdeGrupo` y `buildCadenaAprobacion` en `approval-engine.ts`. Compras la aplica en `resolveCadenaAprobacion`. Contratistas, en `resolverCadenaProforma`.
- Deja el codigo: el primer eslabon ya no se salta por monto bajo. El corte `pasoExigidoPorMonto` solo corre cuando `chain.length > 0`, o sea en los eslabones siguientes. Un monto chico entra al primero. Los siguientes se omiten si el monto no alcanza el tope de ese nodo. Si la cadena queda vacia, el motivo puede seguir siendo `bajo_umbral` o `sin_cadena`, y los dos servicios lanzan error: no dejan el documento `APROBADO` ni `DEFINITIVA` por monto. Un borrador que no se envia no entra a la bandeja. Los topes de la escala siguen siendo los del mantenedor; esta sala no los fijo.
- Pide la sala: no hay tramo exento por monto. Toda orden entra a la cadena, desde el primer eslabon. Hasta un monto de 5 pesos pasa por aprobacion.
- Depende de: ninguno de madre o hija para la regla. La madre que se edita vuelve a usar esta misma cadena en CU-20. La proforma usa la misma regla de primer eslabon en CU-04.

## CU-20. Subir o bajar la madre vuelve a pasar por aprobacion

- Entra hoy: editar una OC `APROBADO` en `updateOrden`, y achicarla en `solicitarCierreSaldoOc`. El vinculo parcial tambien la devuelve a la cadena, dentro de `splitOcMadreCreaHijaPorMontos`.
- Deja el codigo: si el total de una `APROBADO` sube o baja, `montoCambia` rearma `resolveCadenaAprobacion` y el estado vuelve a `PENDIENTE_APROBACION`. `RECEPCIONADA`, `CONTABILIZADA` o `FACTURADO` no se editan. El tope de la recepcion de compras (`assertTopeRecepcion`) impide pasar el neto ya confirmado. La guia de insumos no mira ese cupo. Cada hija de recepcion nace `APROBADO` sin recorrer la bandeja. Al vincular una factura parcial, la madre igual vuelve a aprobacion, y ese control queda en el libro, no en la recepcion.
- Pide la sala: la aprobacion inicial de la madre no se repite en cada hija. Si la madre se edita, el monto nuevo recorre la cadena, baje o suba. Sin cupo, la guia no se recepciona hasta esa modificacion. El control del cupo es en la recepcion, no al vincular en compras.
- Depende de: CU-19 (la cadena desde el primer eslabon), CU-13 (la recepcion que tiene que respetar el cupo) y CU-21 (cerrar por menos es esta misma aprobacion, hecha en insumos).

## CU-21. Cerrar la madre por menos se hace en insumos

- Entra hoy: Compras > Ordenes de compra, `CierreSaldoOcModal` y `solicitarCierreSaldoOc`. Insumos no tiene esa accion.
- Deja el codigo: solo sobre la madre, y solo si hay recepcion `CONFIRMADA`. Si lo recibido es menor, el neto baja a lo recibido, no se crea hija por el saldo cortado, y la madre vuelve a `PENDIENTE_APROBACION` (CU-20). Si ya calza, solo marca `cerradaAt`. El vinculo del libro rechaza una madre con `cerradaAt`. La guia de insumos no lee `cerradaAt` ni el saldo de la madre. Despues de aprobar el neto achicado, una recepcion de compras que se pase del nuevo neto la frena `assertTopeRecepcion`.
- Pide la sala: cerrar por una estimacion menor es una accion de la madre en insumos, no en el listado de compras. La madre cerrada no sigue recibiendo guias por el saldo que se corto. La aprobacion de ese cierre es la de CU-20.
- Depende de: CU-20 (el monto nuevo recorre la cadena), CU-13 (dejar de recibir guias) y CU-22 (el pendiente que se esta cerrando se mira en insumos).

## CU-22. El pendiente de la madre se mira en insumos

- Entra hoy: el saldo de recepciones confirmadas esta en `saldoConfirmadoRecepcion`, usado por la recepcion de compras y por el cierre de saldo. El detalle de la orden en compras muestra lo recibido (`recibidoConfirmadoOc`). Insumos muestra stock de bodega, no el saldo de la madre.
- Deja el codigo: el libro, al asociar, compara el monto del registro con el neto de la OC (`calcularMatchOc`) y, si es parcial contra una madre, parte la orden. El pendiente de la madre es condicion de ese vinculo y del cierre, y se ve en compras. Insumos no muestra cuanto le falta a la madre.
- Pide la sala: el pendiente de la madre esta en insumos. Quien calza la factura con la orden solo necesita que calcen. El libro de compras no muestra ese saldo como condicion para asociar la hija con la factura.
- Depende de: CU-13 y CU-16 (insumos es donde vive la madre) y CU-14 (en el libro se asocian hijas ya nacidas, por lo que llego).

## CU-23. Los reportes contables salen en PDF, y el estado de resultados tambien en Excel

- Entra hoy: Contabilidad > Reportes y Comprobantes / asientos. Diario y mayor en `LibroDiarioMayorPages`, balance en `Balance8ColumnasPage`, comprobante en `AsientosPage` (`imprimirComprobante`), estado de resultados en `EstadosFinancierosPage` con `modo="resultado"` (`/contabilidad/estado-resultados`).
- Deja el codigo: libro diario, libro mayor y balance de 8 columnas tienen Exportar Excel/CSV (`exportRowsToExcel`) y Exportar PDF (`printReporteContable`, ventana de impresion). El comprobante tiene el boton Imprimir, que abre la misma ventana de impresion, y no tiene Excel. El estado de resultados muestra la grilla del periodo (codigo, cuenta, perdida, ganancia) y no tiene boton de Excel ni de PDF. La misma pagina, en situacion financiera, tampoco; la sala no nombro ese reporte.
- Pide la sala: comprobantes, libro diario, libro mayor, balance de ocho columnas y estado de resultados se exportan a PDF. El estado de resultados, ademas, se exporta a Excel. Los campos de cabecera que una voz de implementacion nombro no los pidio el cliente.
- Depende de: ninguno de contratistas ni de madre e hija. Lee los asientos que ya existan, entre ellos el de CU-05 si el mes se hubiera cerrado.

## CU-24. Con factura recibida, la proforma no se edita

- Entra hoy: `updateProforma`, `patchCentrosCostoProforma` y `updateIngresoLaborDiario`, desde la ficha de proformas y el ingreso diario.
- Deja el codigo: `updateProforma` solo acepta `BORRADOR`. Con `FACTURADA`, o con OC ya generada, no cambia numero, periodo, moneda ni ingresos. `patchCentrosCostoProforma` rechaza la proforma facturada o con orden. El ingreso `ASOCIADO` o `FACTURADO` tampoco se edita: el candado del ingreso corre desde que entro a la proforma, antes de la factura. La sala dejo abierto el caso de la proforma aprobada que todavia no tiene factura.
- Pide la sala: la proforma ya asociada a una factura recibida queda cerrada a edicion. No se le cambian ingresos diarios ni montos.
- Depende de: CU-07 y CU-25 (la asociacion que la deja `FACTURADA`). No depende del cierre: puede facturarse antes o despues de CU-05.

## CU-25. El dia sin proforma no se corre de mes, y una factura puede tomar varias

- Entra hoy: el ingreso conserva `fecha` y su mes (`periodoDesdeFecha`). El cierre no lo reasigna. La proforma solo acepta ingresos de su periodo. La factura de varias entra por `asociarFacturaProforma` (`proformaIds`).
- Deja el codigo: un ingreso `PENDIENTE` de un dia sigue en ese mes aunque se cierre el traspaso; no pasa a otro periodo ni se contabiliza. Se puede armar una proforma con un solo ingreso de ese mes. Una factura (registro del libro) puede llevar varias proformas del mismo contratista, moneda y tipo, y cada una pasa entera a `FACTURADA`. Si la suma supera el neto de la factura, se rechaza. Si es menor, la factura conserva saldo y las proformas quedan facturadas por completo: no hay facturacion parcial de lineas de una proforma. Sin registro, el otro camino crea una OC por el grupo y tambien las marca `FACTURADA`.
- Pide la sala: un ingreso no pasa de mes por el cierre. Para entrar al mes necesita su proforma, aunque sea de un solo dia. Una factura puede asociar varias proformas. La proforma no se deja facturada a medias.
- Depende de: CU-03 (elegir los ingresos, incluido un dia suelto), CU-05 (el cierre no se lleva lo que no tiene proforma), CU-06 (el gasto es el mes de la proforma) y CU-24 (una vez facturada, no se edita).
