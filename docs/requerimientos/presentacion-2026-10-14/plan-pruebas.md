# Plan de pruebas - presentacion 2026-10-14

Casos: `casos-de-uso.md` (CU-01 a CU-25). Encaje de hoy: `plan-integracion.md`. Sala: `docs/reuniones/transcripciones/transcripcion-2026-10-14-presentacion.md`.

Este plan no se ejecuta en esta redaccion. No se implementa codigo y no se hace commit.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`.

Quien lo corra despues no emite DTE, no llama al SII, no paga, no cierra el mes, no reabre un periodo y no corre `prisma migrate deploy`. No pulsa Traspasar y cerrar, no ejecuta `solicitarCierreSaldoOc` y no confirma un vinculo que parta una orden.

La factura de proveedor, cuando un caso la nombra, entra por un registro del libro de compras ya existente o por carga manual. No se dispara emision ni un evento a GoSocket. En la corrida no se carga un registro nuevo, no se contabiliza y no se vincula: se abre el que ya este, o se lee el servicio si no hay ninguno.

Hay 25 pruebas, P-01 a P-25. Una por caso. Los limites no se numeran y no se convierten en P-26.

## Como se lee un resultado

Pasa solo la columna Resultado esperado (sala).

El codigo de salida de un spec no es el veredicto. Un verde que afirma el atajo de hoy se anota en Resultado de hoy. Ese verde no acredita el caso.

Si la pantalla no carga o el stack no responde, el resultado es bloqueo de ambiente. No se cierra el mes, no se emite y no se migra para fabricar el dato.

Atajos del codigo actual que no acreditan el caso:

- El combo de actividad filtrado por la labor, con la actividad vacia, no es "sale sola" (P-01).
- Armar una OC desde la proforma y exigir `cuentaGastoId` no es el gasto de la sala (P-02).
- Una hija nacida en Compras > Recepciones, o al vincular la factura, no es la hija que nace de la guia en insumos (P-12, P-13, P-14).
- `splitOcMadreCreaHijaPorMontos`: la factura queda en la madre y la hija es el saldo no facturado. Es el corte al reves (P-14, P-20).
- `preferirHijaAprobadaSinFactura`, al leer un XML, no es el listado de lo que llego (P-14).
- `solicitarCierreSaldoOc` en el listado de compras no es el cierre de la madre en insumos (P-21).
- Entrar solo al primer eslabon, y omitir los siguientes porque el monto no alcanza el tope, deja un tramo exento (P-19).
- Excel y PDF de diario, mayor y balance no cubren el estado de resultados (P-23).
- Asociar la proforma sin registro, creando una OC, no es la factura recibida (P-07, P-25).
- Copiar al contratista, o a correos extra, no es el aviso al contratista ni convierte el correo de compras en un aviso al proveedor (P-10, P-11).
- Una guia que mueve stock y no pide la madre no hace nacer la hija (P-13).

## Limites

Lo que `casos-de-uso.md` dejo abierto no es prueba. Un pase de P-01 a P-25 no los cierra. No se inventa un caso para taparlos.

- Precio cero en el ingreso diario. Preguntaron si se puede guardar sin precio. Nadie cerro que se permita. Sigue abierto.
- Editar ingresos cuando la proforma esta aprobada y todavia no tiene factura. Lo que si quedo cerrado es la ya facturada: P-24.
- La frase que suena a nota de credito si hay diferencia antes de la factura. No se entiende y nadie la cerro.
- Si "Traspaso contable y cierre de mes" es un menu o dos. El nombre y el lugar si quedaron: P-08.
- Una segunda modificacion de la madre y una sola chance de cambio. Lo dijo una voz sin nombre. Maria Jesus no lo repitio. Lo cerrado es P-20 y P-21.
- Cabecera del PDF con empresa, nombre del reporte y periodo. Lo dijo quien implementa. El cliente pidio el formato: P-23.
- Peso, dolar, yuan y vencimientos en el comprobante. En esta sala nadie los volvio a cerrar.
- Historial de por que se rechazo una orden. En esta transcripcion no esta. El 24/09 quedo en "podriamos".
- Si la hija pasa o no por la cadena. El 14/10 no se repitio esa frase. Lo cerrado de la madre es P-20.
- Varias lineas de la madre con centros de costo distintos, y el reparto de una factura parcial. Esta sala no lo cerro.
- Si la guia de la recepcion es la fisica o la que viene por GoSocket, codigo 52. Esta sala hablo de la guia en bodega y no distinguio el canal. No se dispara un evento a GoSocket para verlo.
- Folio de la hija con guion 1, guion 2. Lo mostro el equipo. El cliente no lo cerro.
- El silencio del contratista como si hubiera aprobado la proforma. El 14/10 no se repitio. El aviso por correo si quedo: P-10.
- Tipo de cambio en la pantalla de cierre. Lo pidio el cliente en Reu3 y el 14/10 no lo repitio. La pantalla de hoy no lo pide. No se arma prueba.

## Indice

| ID | CU | Que se hace |
|---|---|---|
| P-01 | CU-01 | Elegir la labor en el ingreso diario y ver si la actividad queda puesta |
| P-02 | CU-02 | Ver el detalle del ingreso y la cuenta unica del gasto |
| P-03 | CU-03 | Agrupar varios ingresos diarios en una proforma |
| P-04 | CU-04 | Aprobar la proforma como jefe de campo |
| P-05 | CU-05 | Ver el asiento unico del mes, sin contabilizar al aprobar |
| P-06 | CU-06 | Ver que el gasto queda en el mes de la proforma |
| P-07 | CU-07 | Ver las dos partidas: cierre, y factura contra el proveedor |
| P-08 | CU-08 | Ver el menu de cierre bajo auditoria y donde se dice el mes |
| P-09 | CU-09 | Ver el listado del traspaso y que la pendiente no es gasto |
| P-10 | CU-10 | Ver el aviso por correo al contratista, con el documento |
| P-11 | CU-11 | Ver que el correo de compras sale a un usuario interno |
| P-12 | CU-12 | Ver que la madre no se contabiliza y no calza la factura |
| P-13 | CU-13 | Ver si la guia de insumos, contra la madre, hace nacer la hija |
| P-14 | CU-14 | Ver si una factura puede tomar varias hijas ya nacidas |
| P-15 | CU-15 | Ver las guias en insumos y no en el libro de compras |
| P-16 | CU-16 | Ver madre e hija en insumos, y en compras solo la hija recepcionada |
| P-17 | CU-17 | Ver si servicio e insumos tienen flujos distintos |
| P-18 | CU-18 | Ver quien puede crear la madre y quien hace nacer la hija |
| P-19 | CU-19 | Ver si una orden de 5 pesos entra a la cadena, sin tramo exento |
| P-20 | CU-20 | Ver la edicion de la madre, al alza o a la baja, y el cupo de la guia |
| P-21 | CU-21 | Ver donde se cierra la madre cuando llego menos |
| P-22 | CU-22 | Ver donde se mira el pendiente de la madre |
| P-23 | CU-23 | Ver PDF de los reportes de la muestra, y Excel del estado de resultados |
| P-24 | CU-24 | Ver que la proforma ya facturada no se edita |
| P-25 | CU-25 | Ver el dia suelto y una factura con varias proformas enteras |

## P-01. Al elegir la labor, la actividad sale sola

- Id: P-01
- CU: CU-01
- Que se hace: en ALMAHUE EXPORT SPA, abrir Contratistas > Ingreso diario. Elegir una labor que ya tenga actividad parametrizada. No guardar el ingreso.
- Resultado de hoy: al cambiar la labor, el front pide las actividades de esa labor y vacia la actividad. La persona tiene que elegir una en el combo. Si la labor no tiene ninguna, el combo queda vacio y el guardado rechaza el par.
- Resultado esperado (sala): se elige la labor y la actividad asociada aparece sola. El ingreso es el que usa el area agricola.
- Cuando pasa: la actividad queda puesta al elegir la labor, sin buscarla a mano.
- No acredita: el combo filtrado, con la actividad vacia.

## P-02. El ingreso diario lleva el detalle y el gasto va a una sola cuenta

- Id: P-02
- CU: CU-02. El asiento que usa la cuenta se lee en P-05 y P-07. Aqui se mira donde vive el detalle y cual es la cuenta.
- Que se hace: abrir el ingreso diario y Nueva proforma en Contratistas > Proformas y facturas. Ver si el ingreso guarda centro de costo, labor y actividad, y si la proforma pide una cuenta de gasto por linea. No guardar. No pulsar el traspaso. La cuenta del gasto se lee en `traspasoCierre` / `resolveCuentasCierreSala`, sin ejecutarlo.
- Resultado de hoy: el formulario de la proforma no pide cuenta de gasto. Si no viene cuenta, queda vacia. El traspaso no usa esa cuenta ni la cuenta del tipo de contrato: el debe es `6-1-01-01-002` o, si no esta ese codigo, una cuenta de gasto cuyo nombre es mano de obra contratista, y agrupa el debe solo por centro de costo. Labor y actividad quedan en el ingreso y no salen en la linea del asiento. El camino que arma una OC desde la proforma sigue pidiendo `cuentaGastoId` y rechaza la proforma si viene vacia.
- Resultado esperado (sala): centro de costo, labor y actividad quedan en el ingreso diario. La proforma no pide una cuenta distinta por linea. El gasto de esas lineas es la cuenta mano de obra contratista.
- Cuando pasa: el detalle esta en el ingreso, la proforma no pide cuenta por linea, y el gasto del traspaso es mano de obra contratista.
- No acredita: el camino de la OC que exige `cuentaGastoId`. La sala no manda el gasto por esa orden.

## P-03. Varios ingresos diarios arman una proforma

- Id: P-03
- CU: CU-03. El dia que no entra es P-25.
- Que se hace: abrir Nueva proforma. Ver el multicheck de ingresos del contratista, del tipo operativo y del periodo. No guardar una proforma nueva. Leer que `createProforma` marca los elegidos `ASOCIADO` y rechaza otro contratista, otro mes, o un ingreso que ya no esta pendiente.
- Resultado de hoy: se pueden tomar varios ingresos, o uno solo si se desmarcan los demas. Al guardar, esos ingresos no quedan libres para otra proforma. Vienen todos marcados.
- Resultado esperado (sala): la proforma es el agrupado de los ingresos diarios elegidos de ese contratista. Esos ingresos ya no quedan libres para otra proforma. No hace falta una proforma por dia, salvo el dia suelto de P-25.
- Cuando pasa: varios ingresos del mismo contratista y del mismo mes quedan en una proforma y dejan de estar libres.
- No acredita: exigir una proforma por cada dia. Que vengan todos marcados es lo de hoy; se puede dejar un dia afuera al desmarcarlo.

## P-04. La proforma la aprueba el jefe de campo

- Id: P-04
- CU: CU-04. Quien entra al mes es P-05 y P-09.
- Que se hace: abrir una proforma en borrador y Contratistas > Aprobaciones. Ver quien es el eslabon que la deja lista para el traspaso. No firmar. No enviar una proforma real a la bandeja. Leer `resolverCadenaProforma` y `aprobarProformaDefinitiva` sin ejecutarlos.
- Resultado de hoy: no hay un rol llamado jefe de campo. Aprueba el eslabon pendiente de la escala de proformas. `bajo_umbral` lanza error y no deja la proforma definitiva sola. Al cerrar el ultimo paso el estado es `DEFINITIVA` y no hay asiento. El ingreso, si el alta no manda aprobador, queda `PENDIENTE` y no arma cadena. Si el alta manda aprobador, el ingreso puede quedar `PENDIENTE_APROBACION`.
- Resultado esperado (sala): sin aprobacion del jefe de campo la proforma no queda lista para el traspaso. La aprobacion es de la proforma, no de cada ingreso suelto.
- Cuando pasa: quien aprueba es el jefe de campo, la proforma sin esa firma no entra al traspaso, y el ingreso suelto no arma su propia cadena.
- No acredita: una escala generica sin el rol jefe de campo. Que `bajo_umbral` lance error no nombra a ese jefe.

## P-05. El asiento del mes es uno, al cierre, y suma las proformas aprobadas

- Id: P-05
- CU: CU-05. Depende de la cuenta de P-02 y de la lista de P-09.
- Que se hace: abrir Contratistas > Traspaso contable y cierre de mes (`/contratistas/traspaso`). No pulsar Traspasar y cerrar. No reabrir. Si ya existe un asiento `TRASPASO-CTR:{periodo}`, leerlo en Contabilidad > Asientos. Si no existe, leer `traspasoCierre` y `aprobarProformaDefinitiva` sin ejecutarlos.
- Resultado de hoy: aprobar una proforma no llama a contabilidad. Al cerrar el periodo hay un asiento, origen `TRASPASO-CTR:{periodo}`, con las proformas `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA` de ese periodo. El debe va por centro de costo a `6-1-01-01-002` y el haber, en una sola linea, a `2-1-08-02-003`. Si el monto es 0, cierra el periodo sin asiento. Un segundo cierre del mismo periodo se rechaza. Reabrir existe y la sala no lo pidio.
- Resultado esperado (sala): aprobar una proforma no genera el asiento. Al cerrar el mes, las proformas aprobadas de ese mes salen en un asiento centralizado. No se contabiliza contratista por contratista.
- Cuando pasa: no hay asiento al aprobar, y el cierre del mes deja un solo asiento con las aprobadas de ese mes.
- No acredita: un asiento por cada proforma, o uno por contratista. Cerrar en cero sin asiento no esta dicho por la sala: no se usa como pase ni como caso nuevo. Incluir la ya enviada o la ya facturada en el asiento del mes de la proforma es P-06, no un atajo.

## P-06. El gasto queda en el mes de la proforma

- Id: P-06
- CU: CU-06
- Que se hace: leer el filtro de `traspasoCierre` (periodo del encabezado contra `proforma.periodo`) y `asociarFacturaProforma`. No cerrar el mes. No asociar una factura nueva. Si ya hay una proforma de un mes y un registro de compra de otro mes, solo leer las fechas.
- Resultado de hoy: el asiento usa el periodo de la proforma, no la fecha del registro de compra. Una proforma de octubre entra al cierre de octubre aunque la factura se asocie en noviembre, y tambien entra si ya esta `FACTURADA`. El ingreso suelto, sin proforma, no se mueve de mes: P-25.
- Resultado esperado (sala): el mes del gasto es el mes de la proforma aprobada. No se espera la fecha de la factura para reconocer ese gasto.
- Cuando pasa: el gasto de octubre se reconoce en octubre aunque la factura tenga fecha de noviembre.
- No acredita: usar la fecha del registro de compra como mes del gasto.

## P-07. Mano de obra contra facturas por recibir, y despues la factura contra el proveedor

- Id: P-07
- CU: CU-07. La proforma que queda cerrada al facturar es P-24. Varias proformas en una factura es P-25.
- Que se hace: leer `resolveCuentasCierreSala` y `planAsientoRegistroCompra` sin contabilizar. Si ya existe un asiento `TRASPASO-CTR:{periodo}` y un asiento `COMPRA:{factura}` de una proforma ligada por `registroCompraId`, leer las cuentas. No emitir. No cargar un registro nuevo. No pagar. No disparar GoSocket. No usar el camino que crea una OC.
- Resultado de hoy: el cierre debe `6-1-01-01-002` y haber `2-1-08-02-003` (si falta el codigo, busca por nombre "MANO DE OBRA CONTRATISTA" y "FACT X RECIBIR CONTRATISTAS"). No usa la cuenta del proveedor. Asociar con `registroCompraId` no crea asiento: deja la proforma `FACTURADA`. Al contabilizar ese registro, si la proforma quedo ligada, el debe es `tipo.cuentaHaber`, no el codigo `2-1-08-02-003` del cierre, y el haber es proveedores. Si el haber del tipo no es la misma cuenta del cierre, las dos partidas no se encuentran. Si no hay tipo en la proforma ligada, el asiento de la factura puede ir a la cuenta de gasto de la OC y repetir el gasto. Asociar sin registro crea una OC y no publica esta segunda partida.
- Resultado esperado (sala): centralizar no usa la cuenta del proveedor. Asociar la factura recibida saca facturas por recibir y deja al proveedor. El gasto no se duplica.
- Cuando pasa: el cierre es mano de obra contra facturas por recibir, y la factura recibida deja facturas por recibir contra el proveedor, sin un segundo gasto.
- No acredita: el debe `tipo.cuentaHaber` cuando no es la cuenta del haber del cierre. No acredita repetir el gasto por la cuenta de la OC. No acredita crear una OC al asociar sin registro.

## P-08. El cierre es un menu bajo auditoria

- Id: P-08
- CU: CU-08
- Que se hace: en el menu Contratistas, comparar Auditoria (`/contratistas/auditoria`) con Traspaso contable y cierre de mes (`/contratistas/traspaso`). Ver el rotulo, si cuelga de cada proforma, y donde se informa el mes. No pulsar el cierre. No buscar un campo de tipo de cambio: no es caso.
- Resultado de hoy: el rotulo del menu y el titulo de la pagina son "Traspaso contable y cierre de mes". Queda en el mismo menu, inmediatamente despues de Auditoria. No es un subitem de la pantalla de auditoria. El mes no se tipea en el formulario: se usa el periodo del encabezado del sitio. La pantalla muestra ese periodo y el boton cierra ese mes. Ejecutar pide `contratistas:transfer` y `contratistas:close`.
- Resultado esperado (sala): el cierre no es un boton suelto en cada proforma. Es el menu "Traspaso contable y cierre de mes", bajo auditoria, y el usuario dice que mes cierra.
- Cuando pasa: el item tiene ese nombre, esta en Contratistas debajo de Auditoria, no es un boton de la proforma, y en esa pantalla el usuario informa el mes que cierra.
- No acredita: el titulo de la pagina, igual al nombre, si el item del menu no es ese. No acredita heredar el periodo del encabezado sin decir el mes en esa pantalla.

## P-09. Al traspaso entran todas las aprobadas y la pendiente no es gasto

- Id: P-09
- CU: CU-09
- Que se hace: abrir `/contratistas/traspaso` en un periodo que tenga proformas de mas de un contratista y de mas de un estado, si ya existen. No pulsar el cierre. Leer el filtro `elegibles` de `traspasoCierre`.
- Resultado de hoy: la grilla lista todas las del periodo, de todos los contratistas, incluida la `PENDIENTE_APROBACION` y el borrador. El asiento solo suma `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA`. La pendiente se ve y su columna Contabilidad no la marca como gasto. Es una fila por proforma, no una fila por contratista.
- Resultado esperado (sala): se listan todas las aprobadas. Una pendiente se puede ver, y no se contabiliza.
- Cuando pasa: estan las aprobadas de todos los contratistas, una fila por proforma, y la pendiente se ve y queda fuera del asiento.
- No acredita: una fila por contratista, ni contabilizar la pendiente. Ver el borrador en la misma grilla es lo de hoy: no acredita por si solo, y no anula el caso si las aprobadas estan y la pendiente queda fuera del gasto.

## P-10. La proforma aprobada se puede avisar al contratista por correo

- Id: P-10
- CU: CU-10
- Que se hace: abrir el aviso de una proforma ya aprobada (`ProformaNotificarModal`) y la pantalla de envio operativo. Leer a quien sale el correo y si adjunta el PDF. No enviar el correo. No unir botones.
- Resultado de hoy: notificar exige una proforma aprobada o ya notificada y un usuario del ERP de la empresa. El aviso interno queda siempre. El correo, si se marca, sale al email de ese usuario y puede adjuntar el PDF. Puede copiar el email del contratista y otras direcciones. El envio operativo, si se pide email, manda el PDF al correo de la ficha del contratista. Siguen siendo dos entradas. Sin `SMTP_HOST` el aviso interno queda y el correo no sale.
- Resultado esperado (sala): existe el aviso por correo al contratista, con el documento de la proforma. Unir o no los dos botones no quedo dicho.
- Cuando pasa: con la proforma aprobada, el contratista es el destinatario del correo y el mensaje lleva el documento.
- No acredita: el modal cuyo destinatario es un usuario interno y el contratista entra solo si se marca la copia. Que sigan dos entradas no se falla: la sala no lo dijo. Sin SMTP, si el destinatario del codigo es el correo de la ficha, es bloqueo de ambiente.

## P-11. El correo de la orden de compra es interno

- Id: P-11
- CU: CU-11
- Que se hace: en el Libro de compras, abrir el modal Notificar de un registro ya existente. Leer el destinatario y los campos de copia. No enviar. No sincronizar. No disparar un evento a GoSocket. No usar el PDF ni el XML de un DTE de GoSocket como prueba.
- Resultado de hoy: el destinatario es un usuario del ERP con acceso a la empresa. El aviso interno va a ese usuario. El correo opcional sale al email de su ficha y puede llevar PDF o XML del DTE si el registro tiene documento GoSocket. El modal ofrece copia al remitente, copia a quien genero la orden y un campo de correos extra.
- Resultado esperado (sala): el destinatario previsto del correo de compras es un usuario interno del departamento. La pantalla para copiar a externos no la pidio el cliente en esta sala.
- Cuando pasa: el destinatario previsto es un usuario interno del departamento.
- No acredita: mandar el correo al proveedor. Los campos de copia a externos y el adjunto GoSocket son lo de hoy: ofrecerlos no es un pedido de la sala y no reemplaza al destinatario interno.

## P-12. La madre es la negociacion y se contabiliza la hija

- Id: P-12
- CU: CU-12. De donde nace la hija es P-13. La factura que toma hijas es P-14.
- Que se hace: abrir Compras > Ordenes de compra y, si ya hay asientos, Contabilidad > Asientos. No recepcionar. No vincular. No contabilizar. Leer `assertRegistroContabilizableOcMadre`, `crearOcHijaDeRecepcion` y `splitOcMadreCreaHijaPorMontos` sin ejecutarlos.
- Resultado de hoy: no hay un documento marcado solo negociacion. El listado devuelve madre e hija juntas. Una recepcion parcial contabiliza la hija (`RECEPCION:{hija}`) y no mueve la madre a `RECEPCIONADA`. Una recepcion por el total contabiliza la madre y la deja `RECEPCIONADA`. Al vincular una factura de menor monto, la factura queda asociada a la madre, no a una hija de lo recibido. Si la madre ya tiene hijas activas, contabilizar esa factura se rechaza y el mensaje pide la factura de la hija.
- Resultado esperado (sala): la madre no se contabiliza. La hija si puede contabilizarse. La madre no se asocia en el libro de compras como si fuera la orden que calza la factura.
- Cuando pasa: la madre no tiene asiento, la hija si puede tenerlo, y el libro no deja la factura en la madre.
- No acredita: la recepcion total que contabiliza la madre. No acredita el vinculo que deja la factura en la madre. No acredita la hija de la recepcion de compras: la hija de la sala nace en insumos (P-13).

## P-13. La hija nace al recepcionar la guia en insumos

- Id: P-13
- CU: CU-13
- Que se hace: abrir Insumos > Guias de insumos recibidas y el formulario de alta. Ver si pide la orden madre y si al guardar nacería una hija. No guardar la guia. No recepcionar en Compras. No vincular en el libro.
- Resultado de hoy: la guia pide numero fisico, proveedor, articulo, cantidad y bodega. Crea un movimiento `ENTRADA_PROVEEDOR` y la fila de guia. No recibe la orden, no busca la madre y no crea hija. El precio sale de una orden aprobada del mismo proveedor, o del maestro, y no parte la orden. La hija que el codigo si crea entra por Compras > Recepciones (trozo recibido, `APROBADO`, sin cadena nueva) o por el vinculo del libro (saldo no facturado, madre devuelta a aprobacion).
- Resultado esperado (sala): sin madre no hay donde asociar la guia. Al recepcionar la guia contra la madre, queda creada la hija por el parcial de esa guia. El libro de compras no crea la hija. Insumos es el unico modulo de este flujo.
- Cuando pasa: la guia se recepciona contra la madre y de ese parcial nace la hija, en insumos.
- No acredita: una guia que solo mueve stock. No acredita la hija de `createRecepcion`. No acredita la hija de `splitOcMadreCreaHijaPorMontos`.

## P-14. Varias guias del mes y una factura: en compras se asocian las hijas

- Id: P-14
- CU: CU-14. Las hijas ya existen por P-13.
- Que se hace: en el Libro de compras, abrir el modal de asociar orden de un registro ya existente. Ver si el listado es lo que llego de ese proveedor y si se pueden marcar varias hijas. No confirmar el vinculo. No emitir. No leer un XML de GoSocket para forzar el calce. No cargar un registro nuevo.
- Resultado de hoy: se elige una OC. Si el monto de la factura es menor que el neto de una madre sin hijas, el corte achica la madre al monto de la factura, la pone `PENDIENTE_APROBACION` y crea una hija por el saldo. La factura queda con la madre. Si ya hay una hija, el vinculo exige elegir la hija cuyo neto coincida. No ofrece marcar varias hijas en una misma factura. `preferirHijaAprobadaSinFactura` solo corre al leer referencias de un XML y, si el neto calza, mueve el vinculo a una hija ya aprobada y sin factura. No lista lo que llego.
- Resultado esperado (sala): una factura puede tomar varias hijas del mismo proveedor, hijas que ya nacieron de las guias. El listado es lo que llego, no un calce solo por monto. La guia no es la linea que se asocia.
- Cuando pasa: en el libro se marcan varias hijas ya nacidas, del mismo proveedor, contra una factura, y el listado es lo recepcionado.
- No acredita: elegir una sola OC. No acredita el corte que deja la factura en la madre y crea la hija por el saldo. No acredita calzar una hija por el neto al leer un XML.

## P-15. Las guias se ven en insumos, no en el libro de compras

- Id: P-15
- CU: CU-15
- Que se hace: abrir Insumos > Guias de insumos recibidas y el Libro de compras. Ver si insumos tiene libro de compras y si el libro de compras lista la guia para asociarla. No cargar una guia. No vincular.
- Resultado de hoy: insumos lista numero, proveedor, articulo, cantidad y bodega. No tiene libro de compras. El libro de compras lista registros de factura y asocia ordenes. No lista la guia para marcarla. La guia no guarda la madre ni la hija.
- Resultado esperado (sala): insumos tiene libro de guias y no tiene libro de compras. El libro de compras no lista la guia para asociarla. Cuando la hija ya esta y se asocia a la factura, recien pasa al libro de compras.
- Cuando pasa: las guias se ven en insumos, insumos no tiene libro de compras, y el libro de compras no ofrece la guia como linea para asociar.
- No acredita: que la guia no guarde la madre. Eso es P-13. Este caso es donde se ve la guia.

## P-16. Insumos ve madre e hija y compras solo ve la hija lista para contabilizar

- Id: P-16
- CU: CU-16
- Que se hace: abrir Compras > Ordenes de compra y el selector de orden del libro. Abrir el menu de Insumos con un perfil que solo tenga insumos, si ya existe en la empresa, o leer que insumos no tiene listado de ordenes. No asociar. No recepcionar.
- Resultado de hoy: el listado de compras trae madre e hija, en cualquier estado, y muestra "Hija de" cuando hay padre. Una madre aprobada y no recepcionada se puede abrir y, si esta aprobada, se puede elegir al asociar. Insumos no muestra la madre ni la hija. Quien solo tiene lectura de insumos no ve las ordenes en su modulo.
- Resultado esperado (sala): la madre no aparece para asociar en compras. La hija aparece en compras solo si ya fue recepcionada. Insumos muestra madre e hija. El perfil de insumos no depende de entrar a compras para ver lo suyo. Una orden pendiente o solo aprobada, si no esta recepcionada, en compras no existe.
- Cuando pasa: insumos muestra la madre y la hija, y compras, para asociar, solo muestra la hija ya recepcionada.
- No acredita: el listado de compras con madre e hija en cualquier estado. No acredita que el administrativo de abastecimiento tenga que entrar a compras para ver sus ordenes.

## P-17. Servicio es una a una e insumos llega por partes

- Id: P-17
- CU: CU-17
- Que se hace: abrir el alta de una orden de compra. Ver si hay tipo servicio e insumos, y si la cadena se puede armar distinta por ese tipo. No guardar la orden. No recepcionar. No facturar por menos para ver si nace hija.
- Resultado de hoy: no hay campo de tipo servicio o insumos. El departamento sale del grupo de aprobacion. Cualquier orden aprobada puede recepcionarse por un monto menor y nacer hija. Una orden de servicio, si alguien la recepciona o la factura por menos del neto, sigue el mismo corte que un insumo.
- Resultado esperado (sala): el flujo de madre, guia e hija es solo insumos. La de servicio se aprueba, se recepciona y es siempre una a una. La regla de aprobacion se puede distinguir por esos dos tipos.
- Cuando pasa: solo la de insumos se parte en madre, guia e hija, y la de servicio no nace hijas.
- No acredita: el mismo corte para cualquier orden, sin tipo.

## P-18. La madre la crea el jefe y la hija, el administrativo

- Id: P-18
- CU: CU-18. El alta de la hija es la guia de P-13.
- Que se hace: ver quien puede abrir el alta de orden en Compras > Ordenes, y quien puede recepcionar una guia en insumos. No crear la orden. No guardar la guia. Leer si existe un permiso de jefe para la madre y de administrativo de insumos para la hija.
- Resultado de hoy: crear la orden pide permiso de compras y pertenencia a un grupo de aprobacion de Compras. No hay un permiso "solo el jefe crea la madre" ni "solo el administrativo crea la hija". Cualquier usuario del grupo puede enviar la orden a la cadena. La hija de recepcion la crea quien confirma la recepcion en compras. La hija del saldo la crea quien vincula la factura parcial. La guia la crea quien tiene insumos, y esa guia no crea la hija.
- Resultado esperado (sala): crear la madre no esta abierto a cualquiera del grupo. La crea el jefe. Crear la hija es del administrativo de insumos, en la recepcion de la guia, no un alta manual en compras.
- Cuando pasa: la madre solo la crea el jefe, y la hija nace cuando el administrativo recepciona la guia en insumos.
- No acredita: que cualquier usuario del grupo envie la orden. No acredita la hija creada al confirmar una recepcion de compras o al vincular la factura.

## P-19. No hay monto que se salte la aprobacion

- Id: P-19
- CU: CU-19. La misma regla de primer eslabon en la proforma se mira en P-04. Aqui el documento es la orden de compra.
- Que se hace: leer la cadena que armarian `resolveCadenaAprobacion` y `buildCadenaAprobacion` para una orden de 5 pesos, sin enviarla. Anotar si el primer eslabon entra y si un eslabon siguiente se omite por tope. No enviar una orden real a la bandeja. No usar como prueba los topes de ejemplo de la demo (5.000, 10.000, un primer tramo hasta 500.000): esta sala no los fijo.
- Resultado de hoy: el primer eslabon no se salta por monto bajo. El corte por monto solo corre en los eslabones siguientes. Un monto chico entra al primero. Los siguientes se omiten si el monto no alcanza el tope de ese nodo. Si la cadena queda vacia, el motivo puede ser `bajo_umbral` o `sin_cadena`, y el servicio lanza error: no deja la orden `APROBADO` por monto. Un borrador que no se envia no entra a la bandeja. Los topes siguen siendo los del mantenedor.
- Resultado esperado (sala): no hay tramo exento por monto. Toda orden entra a la cadena, desde el primer eslabon. Hasta un monto de 5 pesos pasa por aprobacion.
- Cuando pasa: una orden de 5 pesos entra a la cadena desde el primer eslabon y no queda aprobada sola por el monto, y ningun eslabon se omite por un tope.
- No acredita: entrar solo al primer eslabon y saltar los siguientes porque el monto no alcanza. Eso es un tramo exento. No acredita un verde de "el monto chico ya no se aprueba solo" si los eslabones de arriba se omiten.

## P-20. Subir o bajar la madre vuelve a pasar por aprobacion

- Id: P-20
- CU: CU-20. Cerrar por menos, hecho en insumos, es P-21. La recepcion que tiene que respetar el cupo es P-13.
- Que se hace: leer `updateOrden` sobre una madre `APROBADO`, `assertTopeRecepcion` y si la guia de insumos mira el cupo de la madre. No editar una orden real. No recepcionar. No vincular una factura parcial.
- Resultado de hoy: si el total de una `APROBADO` sube o baja, el estado vuelve a `PENDIENTE_APROBACION`. `RECEPCIONADA`, `CONTABILIZADA` o `FACTURADO` no se editan. El tope de la recepcion de compras impide pasar el neto ya confirmado. La guia de insumos no mira ese cupo. Cada hija de recepcion de compras nace `APROBADO` sin recorrer la bandeja. Al vincular una factura parcial, la madre vuelve a aprobacion, y ese control queda en el libro, no en la recepcion.
- Resultado esperado (sala): la aprobacion inicial de la madre no se repite en cada hija. Si la madre se edita, el monto nuevo recorre la cadena, baje o suba. Sin cupo, la guia no se recepciona hasta esa modificacion. El control del cupo es en la recepcion, no al vincular en compras.
- Cuando pasa: subir o bajar la madre la devuelve a la cadena, la hija no repite esa aprobacion, y la guia no se recepciona si no hay cupo.
- No acredita: `updateOrden` solo, si la guia no mira el cupo. No acredita devolver la madre a la cadena al vincular la factura en el libro. Ese control, en la sala, es de la recepcion.

## P-21. Cerrar la madre por menos se hace en insumos

- Id: P-21
- CU: CU-21. La aprobacion de esa baja es P-20.
- Que se hace: ver si Insumos tiene la accion de cerrar la madre por una estimacion menor, y si Compras > Ordenes de compra tiene `CierreSaldoOcModal`. No ejecutar `solicitarCierreSaldoOc`. No recepcionar una guia contra una madre cerrada.
- Resultado de hoy: el cierre esta en el listado de ordenes de compra. Insumos no tiene esa accion. Solo corre sobre la madre, y solo si hay recepcion confirmada. Si lo recibido es menor, el neto baja a lo recibido, no se crea hija por el saldo cortado, y la madre vuelve a `PENDIENTE_APROBACION`. Si ya calza, solo marca el cierre. El libro rechaza una madre ya cerrada. La guia de insumos no lee ese cierre ni el saldo de la madre. Despues de aprobar el neto achicado, una recepcion de compras que se pase del nuevo neto la frena el tope de compras.
- Resultado esperado (sala): cerrar por una estimacion menor es una accion de la madre en insumos, no en el listado de compras. La madre cerrada no sigue recibiendo guias por el saldo que se corto. La aprobacion de ese cierre es la de P-20.
- Cuando pasa: el cierre por menos se pide en insumos, la baja recorre la cadena, y la madre cerrada no recibe guias por el saldo cortado.
- No acredita: el modal del listado de compras. No acredita el tope de la recepcion de compras si la guia de insumos no lee la madre cerrada.

## P-22. El pendiente de la madre se mira en insumos

- Id: P-22
- CU: CU-22
- Que se hace: abrir el detalle de una madre en compras, si ya existe, y las pantallas de insumos (stock, movimientos, guias). Ver donde aparece cuanto le falta a la madre, y si el libro usa ese saldo para asociar. No vincular.
- Resultado de hoy: el saldo de recepciones confirmadas se usa en la recepcion de compras y en el cierre de saldo. El detalle de la orden en compras muestra lo recibido. Insumos muestra stock de bodega, no el saldo de la madre. El libro, al asociar, compara el monto del registro con el neto de la orden y, si es parcial contra una madre, parte la orden. El pendiente de la madre es condicion de ese vinculo y del cierre, y se ve en compras.
- Resultado esperado (sala): el pendiente de la madre esta en insumos. Quien calza la factura con la orden solo necesita que calcen. El libro de compras no muestra ese saldo como condicion para asociar la hija con la factura.
- Cuando pasa: cuanto le falta a la madre se ve en insumos, y el libro asocia la hija sin usar el saldo de la madre como condicion.
- No acredita: ver lo recibido en el detalle de compras. No acredita partir la madre en el libro porque el monto no calza.

## P-23. Los reportes contables salen en PDF y el estado de resultados tambien en Excel

- Id: P-23
- CU: CU-23. No depende del cierre. Si el mes no esta cerrado, los botones se miran con el periodo en pantalla. No se cierra el mes para llenar la grilla.
- Que se hace: abrir comprobantes, libro diario, libro mayor, balance de ocho columnas y estado de resultados (`/contabilidad/estado-resultados`). Ver Exportar PDF y Exportar Excel en cada uno. No exigir cabecera de empresa, nombre del reporte y periodo: el cliente no la pidio. No probar situacion financiera: la sala no la nombro.
- Resultado de hoy: libro diario, libro mayor y balance de ocho columnas exportan Excel y PDF. El PDF es la ventana de impresion. El comprobante tiene Imprimir, la misma ventana, y no tiene Excel. El estado de resultados muestra la grilla del periodo (codigo, cuenta, perdida, ganancia) y no tiene boton de Excel ni de PDF.
- Resultado esperado (sala): comprobantes, libro diario, libro mayor, balance de ocho columnas y estado de resultados se exportan a PDF. El estado de resultados, ademas, se exporta a Excel.
- Cuando pasa: los cinco tienen PDF, y el estado de resultados tiene ademas Excel.
- No acredita: Excel y PDF de diario, mayor y balance, si el estado de resultados no exporta. La ventana de impresion del comprobante no cubre el estado de resultados.

## P-24. Con factura recibida, la proforma no se edita

- Id: P-24
- CU: CU-24. La asociacion que la deja facturada es P-07 y P-25.
- Que se hace: abrir una proforma `FACTURADA`, si ya existe, e intentar ver si el formulario deja cambiar numero, periodo, moneda, ingresos o centros de costo. No guardar. No editar un ingreso. Si no hay una facturada, leer `updateProforma`, `patchCentrosCostoProforma` y `updateIngresoLaborDiario` sin ejecutarlos. La proforma aprobada que todavia no tiene factura quedo abierta: no es esta prueba.
- Resultado de hoy: `updateProforma` solo acepta borrador. Con `FACTURADA`, o con OC ya generada, no cambia numero, periodo, moneda ni ingresos. El parche de centros rechaza la proforma facturada o con orden. El ingreso `ASOCIADO` o `FACTURADO` tampoco se edita: el candado del ingreso corre desde que entro a la proforma, antes de la factura.
- Resultado esperado (sala): la proforma ya asociada a una factura recibida queda cerrada a edicion. No se le cambian ingresos diarios ni montos.
- Cuando pasa: la proforma `FACTURADA` no cambia ingresos ni montos.
- No acredita: el candado del ingreso desde que quedo `ASOCIADO`, antes de la factura. Ese tramo quedo abierto. Tampoco anula este caso, porque la facturada de hoy si queda cerrada.

## P-25. El dia sin proforma no se corre de mes, y una factura puede tomar varias

- Id: P-25
- CU: CU-25
- Que se hace: leer la fecha y el periodo de un ingreso `PENDIENTE`, y que el cierre no lo reasigna. Ver si una proforma acepta un solo ingreso de su mes. Leer `asociarFacturaProforma` con varias proformas del mismo contratista, sobre un registro del libro ya existente. No cerrar el mes. No asociar en esta corrida. No emitir. No usar el camino sin registro.
- Resultado de hoy: un ingreso pendiente de un dia sigue en ese mes aunque se cierre el traspaso. No pasa a otro periodo y no se contabiliza. Se puede armar una proforma con un solo ingreso de ese mes. Una factura, como registro del libro, puede llevar varias proformas del mismo contratista, moneda y tipo, y cada una pasa entera a `FACTURADA`. Si la suma supera el neto de la factura, se rechaza. Si es menor, la factura conserva saldo y las proformas quedan facturadas por completo: no hay facturacion parcial de lineas de una proforma. Sin registro, el otro camino crea una OC por el grupo y tambien las marca `FACTURADA`.
- Resultado esperado (sala): un ingreso no pasa de mes por el cierre. Para entrar al mes necesita su proforma, aunque sea de un solo dia. Una factura puede asociar varias proformas. La proforma no se deja facturada a medias.
- Cuando pasa: el dia suelto no cambia de mes, puede armar su proforma de un dia, y un registro del libro toma varias proformas enteras.
- No acredita: crear una OC y marcar las proformas `FACTURADA` sin registro del libro. La factura de la sala es la recibida. No acredita dejar una proforma facturada por una parte de sus lineas.
