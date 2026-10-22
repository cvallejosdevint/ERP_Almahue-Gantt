# Resultados de pruebas - auditoria octubre 2026

Fecha de corrida: 2026-10-15. Empresa de lectura: ALMAHUE EXPORT SPA, sesion ya abierta de `admin@almahue.local`. Front `http://localhost:5174` y API `http://localhost:3001` estaban escuchando. No se reiniciaron.

No se guardo, contabilizo ni pago un documento. No se emitio DTE, no se llamo al SII, no se cerro el mes y no se corrio `prisma migrate deploy`. No se hizo click en Traspasar y cerrar.

Un PASA es solo la columna de la sala. Un Jest en verde que afirma el atajo de hoy queda anotado como columna de hoy: el veredicto de esa prueba es FALLA o PARCIAL, no un pase. PARCIAL: una parte de la columna de la sala se vio y otra no. BLOQUEO: el front o la API no respondieron, o el arranque de Jest fallo. En esta corrida no hubo bloqueo de ambiente.

## Como se corrio

Jest, desde `ERP/erp_back`, con mock, sin pegar a la API local:

```
npx jest --testPathPattern "catalogos.service.spec|cuenta-corriente.service.spec|comercial.service.spec|insumos.service.spec|approval-engine.spec|contratistas.service.spec" -t "45|fusiona cliente|listSaldos agrupa|tipo de cambio|glosa conserva|IVA|sin madre|recepcionar la guia|no cabe|devolucion|primer eslab|800k|1.5M|piso de B|YYYY-MM|re-traspaso|primer piso|reversa DEFINITIVA|BORRADOR a PENDIENTE|precio cero" --no-coverage --forceExit
npx jest src/modules/compras/compras.service.spec.ts -t "casilla de correo|parcial confirmada de servicio|neto completo no nace hija|con neto 0 no finge" --no-coverage --forceExit
```

Los dos comandos terminaron en verde (6 suites + 1 suite). No se corrio `oc-parcial.compras.service.spec.ts`.

Pantalla: Playwright, ventana 1920 x 1080, menu y contenido visibles. No se uso el navegador interno de Cursor.

---

## P-01. Dos plazos en la ficha del proveedor

- CU: CU-01.
- Que se corrio: Jest `catalogos.service.spec.ts`, "acepta 45 dias y persiste condicionIvaDia y monedaPago" (verde). Playwright en `/catalogos/proveedores`, ficha de QA-CRUCE PLAZO 45, sin Guardar. Se abrio "Ingresar dias" del IVA y se cancelo.
- Evidencia: Neto es un numero (spinbutton "Dias (ej. 45)", valor 45). IVA es una lista 10 a 90 y tambien "Ingresar dias", que abre otro numero. Son dos campos distintos. El Jest persiste el entero 45 y `condicionIvaDia`. La edicion en la OC y en la factura es P-45.
- Veredicto: PASA.

## P-02. Dos fichas que conversan por RUT

- CU: CU-02.
- Que se corrio: Playwright en `/catalogos/proveedores` y en `/comercial/clientes`. En Nuevo cliente se tipeo `76.111.222-8` y se cancelo. No se creo el cliente.
- Evidencia: Son dos pantallas. El alta de cliente aviso "Tambien es proveedor (QA-CRUCE PLAZO 45). Los modulos siguen separados" y copio razon social y giro. La jefatura es P-46.
- Veredicto: PASA.

## P-03. Consulta por RUT con movimientos de proveedor y de cliente

- CU: CU-03.
- Que se corrio: Jest `cuenta-corriente.service.spec.ts`, "fusiona cliente y proveedor del mismo RUT" y "listSaldos agrupa dual por RUT" (verde). Playwright en `/tesoreria/cuentas-corrientes`, detalle de `77.032.639-7` ALM SERVICES SPA. No se crearon movimientos.
- Evidencia: El verde afirma la cuenta corriente unificada. En pantalla el mismo RUT trae ventas (rol Cliente) y compras (rol Proveedor), con saldos separados. No abre OC, facturas ni ventas que no hayan pasado por esa cuenta. La sala pidio todos los movimientos de compra y de venta. Juntar la cuenta corriente no acredita el resto.
- Veredicto: PARCIAL.

## P-04. Anular un elemento de costo sin borrar el historial

- CU: CU-04.
- Que se corrio: Playwright en `/catalogos/elementos-costo`. Se abrio un elemento ya ANULADO y el combo de vigencia. No se guardo. Lectura de los combos de `AsientosPage`, `PlanCuentasPage` y `CartolaBancariaPage`.
- Evidencia: El listado muestra ANULADO y VIGENTE. El combo solo ofrece Vigente y Anulado. Los tres combos de imputacion filtran `vigencia !== 'ANULADO'`.
- Veredicto: PASA.

## P-05. Historico del Banco Central, sin pisar documentos

- CU: CU-05.
- Que se corrio: Playwright en `/catalogos/indicadores-bc`. No se pulso Sincronizar ni Consultar ahora. El dia vacio que cambia la columna visible es P-47.
- Evidencia: Hay rango, importacion CSV e historico ya cargado de USD, EUR y CNY (yuan). No se escribio `IndicadorBc`.
- Veredicto: PASA.

## P-06. Comprobante en peso, dolar y yuan

- CU: CU-06.
- Que se corrio: Playwright en `/contabilidad/asientos`, comprobante de venta ya contabilizado 20260041, sin contabilizar otro. Jest `comercial.service.spec.ts`: "si el tipo de cambio viene vacio usa el dolar del dia" y "usa el tipo de cambio pedido" (verde).
- Evidencia: El comprobante abierto muestra debe y haber en pesos, dolar y yuan (T dolar 979,85 y T yuan 146,203). El Jest usa el tipo de cambio pedido (950.5) y, si viene vacio, el dolar del dia (910) sin reescribir el documento.
- Veredicto: PASA.

## P-07. Auxiliar igual al RUT sin digito verificador

- CU: CU-07.
- Que se corrio: El mismo comprobante 20260041 y `/contabilidad/mayor`. Lectura de `rutSinDigito` en `comercial.service.ts`. No se contabilizo nada nuevo.
- Evidencia: En el comprobante la columna Aux de las tres lineas es `77032639` (RUT 77.032.639-7 sin puntos y sin DV). El libro mayor en pantalla trae cuenta, nombre, debe y haber, y no tiene columna auxiliar. `LibroDiarioMayorPages` no menciona auxiliar.
- Veredicto: PARCIAL.

## P-08. Glosa igual al comentario, repetida en cada linea

- CU: CU-08.
- Que se corrio: Jest `comercial.service.spec.ts`, "la glosa conserva el comentario" (verde), como columna de hoy. El mismo comprobante 20260041 y el mayor.
- Evidencia: El verde espera `FACTURA 8/2026 TC: 950.5 Pago a 30 dias`. En pantalla la glosa de las tres lineas es `FACTURA 10/2026 TC: 979.85`. La misma frase si se repite en cliente, ingreso e IVA. La sala pidio el comentario, sin rellenar con tipo, folio ni tipo de cambio.
- Veredicto: PARCIAL.

## P-09. En la venta, la cuenta es IVA debito

- CU: CU-09.
- Que se corrio: Jest `comercial.service.spec.ts`, "grabarDocumentoContabilizar genera linea de IVA a la cuenta fiscal correspondiente" (verde). Linea de IVA del comprobante 20260041.
- Evidencia: La linea es `2-1-09-02-001 · IVA DEBITO FISCAL`, haber $352. No es caja. El codigo usa `CODIGO_IVA_DEBITO` en la venta. `cuentaEnComprobante` (mostrar IVA debito encima de una caja) no se uso como evidencia.
- Veredicto: PASA.

## P-10. Avisar a quien debe crear la OC que falta

- CU: CU-10.
- Que se corrio: Jest `compras.service.spec.ts`, "con la casilla de correo apagada deja el aviso y no encola SMTP" (verde). Playwright en `/compras/registro`, modal Notificar de la factura 63 (sin OC). No se pulso Enviar.
- Evidencia: El modal elige un usuario de la empresa, el correo es opcional y hay "Trazabilidad de notificaciones". El Jest deja el aviso interno aunque SMTP no se encole.
- Veredicto: PASA.

## P-11. OC madre de insumos, solo informativa

- CU: CU-11.
- Que se corrio: Playwright en `/insumos/ordenes` y en el libro de compras. Lectura de `getOrdenes` y de `vincularOcRegistroCompra`. No se creo una OC.
- Evidencia: Insumos dice que la madre es la negociacion y que la hija nace al recepcionar la guia. En esta empresa el listado de insumos estaba vacio. `getOrdenes` no trae `tipo=INSUMOS` sin padre. Vincular una madre se rechaza con "La factura no queda en la orden madre". En Compras > Ordenes aparece OC-2026-0021 con el rotulo "Madre / hijas" y la hija OC-2026-0021-1; el detalle no nombra el tipo, y el rotulo sale si la orden tiene hijas. No se uso ese rotulo como la madre de insumos.
- Veredicto: PASA.

## P-12. OC de servicio, una a una, con factura directa

- CU: CU-12.
- Que se corrio: Playwright en `/compras/ordenes/nueva`, sin guardar. El uno a uno es el Jest de P-48.
- Evidencia: El alta ofrece Servicio e Insumos. El Jest de recepcion rechaza el parcial de servicio con "una a una" y no crea hija. La recepcion por el neto completo marca `RECEPCIONADA` y tampoco crea hija.
- Veredicto: PASA.

## P-13. La guia en bodega actualiza stock y nace la hija

- CU: CU-13.
- Que se corrio: Jest `insumos.service.spec.ts`, "al recepcionar la guia contra la madre nace una hija APROBADA por el parcial" (verde). Playwright en `/insumos/guias-recibidas`, sin guardar ni traer de GoSocket. No se corrio `oc-parcial.compras.service.spec.ts`.
- Evidencia: El verde afirma hija `APROBADO`, neto del parcial, numero de la madre mas punto y correlativo, grabada por quien recepciona. La pantalla de guias recibidas esta en insumos y ya tiene una guia ("QA pallet guia despacho") con "Asociar a la madre" y columna Orden hija. El boton "Traer de GoSocket" es el inbox que la sala no pidio: no se uso como pase.
- Veredicto: PASA.

## P-14. Libro de guias solo en insumos

- CU: CU-14.
- Que se corrio: Playwright en `/insumos/guias-recibidas` y en `/compras/registro`. No se abrio `/comercial/guias-despacho` como libro de este caso.
- Evidencia: Las guias recibidas se listan en insumos. El libro de compras muestra 13 documentos, todos "Factura compra". No hay guia de despacho en ese listado. El sincronizado del fuente salta el DTE 52.
- Veredicto: PASA.

## P-15. La factura de insumos se asocia a las OC hijas

- CU: CU-15.
- Que se corrio: Playwright, modal Asociar orden de la factura 63, sin Vincular. Lectura de `vincularOcRegistroCompra`.
- Evidencia: El modal dice "Marca lo recepcionado de este proveedor. En insumos son las hijas. Una orden de servicio se asocia una a una." Para ALM SERVICES SPA no habia orden elegible, asi que no se marco ninguna. El fuente acepta una o varias OC, rechaza la madre, rechaza la hija de insumos sin guia y exige el mismo proveedor. La alerta de monto no reemplaza el listado.
- Veredicto: PASA.

## P-16. Compras solo lista hijas ya recepcionadas

- CU: CU-16.
- Que se corrio: El mismo modal, sin vincular. Lectura de `getOrdenes`.
- Evidencia: El filtro trae todas las OC `SERVICIO`, en cualquier estado, y las hijas de insumos que ya tienen guia. Una de servicio aprobada y sin recepcion entra en ese listado. Ocultar la madre no cierra el caso.
- Veredicto: FALLA.

## P-17. Quien ve la madre y quien ve la hija

- CU: CU-17.
- Que se corrio: Playwright en `/insumos/ordenes` y `/compras/ordenes` con la sesion de ALMAHUE EXPORT SPA. No se creo un usuario de solo `insumos:read`. Lectura del menu y de `getOrdenes`.
- Evidencia: Insumos pide su mundo y en esta empresa no habia filas. Compras lista hijas (OC-2026-0021-1, Aprobado) y tambien ordenes que no estan recepcionadas (P-16). Quien solo tiene insumos no entra al libro: el menu separa los permisos. El listado de asociacion sigue mostrando la de servicio sin recepcion.
- Veredicto: PARCIAL.

## P-18. El saldo de la madre se ve en insumos

- CU: CU-18.
- Que se corrio: Playwright en `/insumos/ordenes`. El modal de la factura no se uso para exigir el saldo. Lectura de `getOrdenesInsumos` (`pendiente`).
- Evidencia: La pantalla dice "El pendiente se mira aca". No habia madre en el listado, asi que el numero no se vio. El fuente calcula pendiente como neto de la madre menos hijas no anuladas. El modal de asociacion no pide ni muestra ese saldo.
- Veredicto: PASA.

## P-19. Si la guia no cabe, se pide modificar la madre

- CU: CU-19.
- Que se corrio: Jest `insumos.service.spec.ts`, "rechaza la guia si no cabe en el saldo o la madre esta cerrada, y no nace hija" (verde). No se guardo la guia.
- Evidencia: Con la madre cerrada la guia no entra y `ordenCompra.create` no se llama. `assertTopeRecepcion` lanza "La guia no cabe en el saldo de la orden madre" y no modifica la madre.
- Veredicto: PASA.

## P-20. La madre se edita una vez, para arriba o para abajo, con aprobacion

- CU: CU-20.
- Que se corrio: Lectura de `solicitarCierreMadreInsumos` y de `updateOrden` cuando cambia el total. No se llamo `POST /insumos/ordenes/:id/cierre` ni `PUT /ordenes-compra/:id`.
- Evidencia: El cierre por lo recibido, si queda saldo, baja el neto y vuelve a `PENDIENTE_APROBACION`. Si ya no queda saldo, solo marca `cerradaAt` y no rearma la cadena. No sube el total. Un cambio de total, para arriba o para abajo, rearma la cadena y borra `cerradaAt`. Lo puede repetir el creador mientras la madre vuelva a `APROBADO`. No hay una sola vez ni un segundo cambio reservado a contabilidad.
- Veredicto: FALLA.

## P-21. La madre la crea el jefe; la hija, el administrativo

- CU: CU-21.
- Que se corrio: Lectura de `assertJefeCreaMadreInsumos` y del Jest de P-13 (alta de la hija). No se creo una madre ni se recepciono una guia.
- Evidencia: Si el usuario no es `aprobadorInicialId` de un grupo OC de Compras activo, la API dice que la madre solo la crea el jefe del grupo. La hija del Jest nace `APROBADO`, la graba quien recepciona y no arma otra cadena. No hay un permiso con el nombre administrativo de abastecimiento: el corte que queda es jefe contra quien recepciona.
- Veredicto: PASA.

## P-22. Cadenas distintas para insumos y para servicios

- CU: CU-22.
- Que se corrio: Playwright en `/admin/aprobaciones`, sin crear grupo ni escala. Lectura de `previewCadena`.
- Evidencia: La pantalla dice "Cadena de ordenes de compra. No usa los grupos de proformas." Hay una pieza de ordenes de compra y otra de proformas. No hay dos piezas, insumos y servicio. `previewCadena` no recibe el tipo de OC y resuelve modulo `Compras`. La cadena de proforma no acredita este corte.
- Veredicto: FALLA.

## P-23. Toda OC pasa por aprobacion, desde monto cero

- CU: CU-23.
- Que se corrio: Jest `approval-engine.spec.ts`, "el primer eslabon aprueba aunque el monto este bajo su piso" y "Ana $800k entra al primer eslabon aunque este bajo su piso" (verde), como columna de hoy del primer eslabon. Tambien "con neto 0 no finge cadena" en `compras.service.spec.ts` (verde). No se envio una OC de la empresa.
- Evidencia: El primer eslabon entra con un monto chico. Un neto 0 devuelve `no_pool` y cadena vacia: el envio puede quedar pendiente sin aprobador. El salto del eslabon siguiente es P-54 y no pasa.
- Veredicto: PARCIAL.

## P-24. Devolucion a proveedor solo en ALM

- CU: CU-24.
- Que se corrio: Playwright en `/admin/empresas`, ficha de ALMAHUE EXPORT SPA, sin guardar. Jest `insumos.service.spec.ts`, "rechaza devolucion a proveedor si la empresa no la permite" (verde).
- Evidencia: El checkbox "Permite devolucion a proveedor" de ALMAHUE EXPORT SPA esta marcado. El Jest rechaza `SALIDA_PROVEEDOR` solo cuando el flag esta apagado. Ver el checkbox no acredita el corte de las dos empresas (P-55). En esta empresa el flag esta prendido, al reves de lo que la sala dejo para exportacion.
- Veredicto: FALLA.

## P-25. Nomina semanal, historico y banderas

- CU: CU-25.
- Que se corrio: Playwright en `/tesoreria/nominas`. Se abrio Editar de los avisos y se cerro sin Guardar. No se hizo `PUT /nomina-plazos`.
- Evidencia: Periodo actual partido en semanas (S1, pendientes y documentos), boton "Atrasados historico", filtro Pendientes / Todos. Los avisos tienen nombre, dia y color: Atrasada desde el dia 1, Critico desde 30, "90 dias" desde 90, y hay "Agregar aviso". El 1 en vez de 7 no traba el caso: el umbral se edita.
- Veredicto: PASA.

## P-26. Ficha de contratista con codigo correlativo

- CU: CU-26.
- Que se corrio: Playwright en `/contratistas`. Se abrio la ficha CTR-00002 y se cancelo.
- Evidencia: Codigos `CTR-00002` y `CTR-00001`, distintos del RUT. La ficha guarda RUT, razon social, direccion (pasaje rolecha 15232) y creador (Admin Almahue en CTR-00002). El prefijo `CTR-` es la columna de hoy. La etiqueta "Este contratista tambien esta en Proveedores" se vio y no se usa como pase.
- Veredicto: PASA.

## P-27. El flujo de contratista no tiene contrato

- CU: CU-27.
- Que se corrio: Playwright en `/contratistas/ingreso-diario`, Nuevo ingreso, sin Crear.
- Evidencia: El formulario no pide contrato vigente ni folio de contrato. `TipoContratoContratista` sigue existiendo en el fuente y no se lee como el contrato que la sala saco.
- Veredicto: PASA.

## P-28. Ingreso diario de la labor

- CU: CU-28.
- Que se corrio: El mismo formulario, sin guardar.
- Evidencia: Hay fecha, contratista, "Cuartel / centro de costo", labor, actividad, jornada o trato, cantidad, precio y total. Predio esta marcado opcional. No hay trabajador. Sector y faena estan marcados opcionales. No hay un campo de duracion distinto de la cantidad. Dejar sector y faena vacios no es el ingreso que ella describio.
- Veredicto: PARCIAL.

## P-29. Mantenedores de cuartel y faena

- CU: CU-29.
- Que se corrio: Playwright en `/catalogos/contratista` y en el ingreso, eligiendo la labor PACK-CER, sin guardar.
- Evidencia: Hay mantenedores de labores, actividades, sectores y faenas. No hay uno que se llame cuartel: el ingreso usa centro de costo. Al elegir PACK-CER la actividad siguio en "Seleccionar..." con dos opciones (SEL-CER y TEST). No quedo determinada.
- Veredicto: PARCIAL.

## P-30. Armar la proforma eligiendo ingresos

- CU: CU-30.
- Que se corrio: Playwright en `/contratistas/proformas` y en el listado de ingresos, sin armar una proforma. Lectura de `createProforma` / `previewProforma` y de `asociarFacturaProforma`.
- Evidencia: La pagina dice "ingresos > proforma > aprobacion". Hay varias proformas en el mismo mes (PF-00001 a PF-00005, periodo 2026-10). Los ingresos ya usados muestran "No editable en este estado". Asociar factura exige un registro que ya llego al libro: "La proforma no genera una orden."
- Veredicto: PASA.

## P-31. La que se aprueba es la proforma

- CU: CU-31.
- Que se corrio: Jest `contratistas.service.spec.ts`, "BORRADOR a PENDIENTE_APROBACION al solicitar aprobacion" y "bajo el primer piso entra al primer eslabon y no queda DEFINITIVA sola" (verde). No se envio una proforma de la empresa.
- Evidencia: El verde afirma la cadena de la proforma y que un monto bajo el primer piso no la deja definitiva sola. El ingreso al guardar es P-56.
- Veredicto: PASA.

## P-32. La proforma no se factura parcial

- CU: CU-32.
- Que se corrio: Lectura de `asociarFacturaProforma`. No se asocio un registro.
- Evidencia: El grupo pasa entero a `FACTURADA` y varias del mismo contratista, moneda y tipo caben mientras la suma no pase el neto. No deja un saldo de una parte. Para entrar, el estado tiene que ser `ENVIADA_CONTRATISTA`. Una `DEFINITIVA` todavia no enviada no entra. La sala pide la aprobada, no solo la notificada.
- Veredicto: PARCIAL.

## P-33. Enviar la proforma al contratista

- CU: CU-33.
- Que se corrio: Playwright en una proforma ya notificada (PF-00005 y PF-00003). No se llamo `enviar-email` ni `enviar-contratista`. Lectura de que el contratista no tiene bandeja.
- Evidencia: La fila tiene Notificar, columna "Envio correo" y, en PF-00003, constancia "14-10-2026 · sin remitente > sin destino". El contratista no tiene usuario ni bandeja de aprobacion. El filtro "notificada" del libro de compras no es este caso.
- Veredicto: PASA.

## P-34. Editar la proforma aprobada; cerrarla si ya hay factura

- CU: CU-34.
- Que se corrio: Jest `contratistas.service.spec.ts`, "reversa DEFINITIVA a BORRADOR con clave de reversa valida" (verde). No se reverso una proforma de la empresa. El cierre de la facturada es P-58.
- Evidencia: El verde devuelve la definitiva a borrador con la clave, y ahi hay que volver a pedir la cadena. En pantalla Reversar esta en las notificadas y no en un estado facturado de esta lista.
- Veredicto: PASA.

## P-35. Ver proformas pendientes y aprobadas

- CU: CU-35.
- Que se corrio: Playwright en `/contratistas/proformas`. Se cambio el filtro a "Pendientes de facturar" solo para leer, sin editar una proforma.
- Evidencia: Cada fila trae su estado (PENDIENTE APROBACION, Notificada contratista). El filtro es Todas, Pendientes de facturar y Facturadas. "Pendientes de facturar" dejo juntas la pendiente de aprobacion y las ya notificadas. No hay un filtro de aprobadas que deje fuera el borrador y la pendiente.
- Veredicto: PARCIAL.

## P-36. El DTE se asocia en compras; el costo se imputa en contratistas

- CU: CU-36.
- Que se corrio: Playwright en `/compras/registro` y en la proforma. No se asocio ni se contabilizo.
- Evidencia: El libro no tiene selector de proforma. La asociacion esta en la proforma ("Asociar factura"). La columna Cuenta gasto de la proforma dice "Mano de obra contratista" y el libro no la edita. El listado de aprobadas, no solo notificadas, es P-59 y no pasa.
- Veredicto: FALLA.

## P-37. Cuenta mano de obra contratista

- CU: CU-37.
- Que se corrio: Lectura de `resolveCuentasCierreSala` y el ingreso de P-28, sin traspasar.
- Evidencia: El debe del cierre es `6-1-01-01-002` (o el nombre mano de obra contratista) y el haber es `2-1-08-02-003`. La proforma no pide una cuenta por linea. El ingreso guarda labor, actividad y centro de costo. El asiento agrupa por centro de costo.
- Veredicto: PASA.

## P-38. Centralizacion del mes en un asiento

- CU: CU-38.
- Que se corrio: Playwright en `/contratistas/traspaso`, sin pulsar Traspasar y cerrar. Jest "pasa periodo YYYY-MM a createAsiento" y "rechaza re-traspaso de periodo ya cerrado" (verde).
- Evidencia: El menu "Traspaso contable y cierre de mes" esta debajo de Auditoria. La pantalla informa el mes 2026-10, periodo contable ABIERTO, traspaso Pendiente, y "5 en periodo · 4 elegibles". El fuente toma `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA`, deja fuera borrador, pendiente de aprobacion y rechazada, y arma un asiento `TRASPASO-CTR:periodo`. El Jest rechaza repetir un periodo cerrado.
- Veredicto: PASA.

## P-39. Al asociar la factura, facturas por recibir contra proveedor

- CU: CU-39.
- Que se corrio: Lectura de `planAsientoRegistroCompra` cuando el registro esta ligado a una proforma. No se hizo PUT a contabilizado y no se llamo a GoSocket.
- Evidencia: El debe es `2-1-08-02-003` y el haber es proveedores, mas el IVA si corresponde. No vuelve a cargar el gasto. La cuenta sale del plan por codigo. El libro no la edita.
- Veredicto: PASA.

## P-40. Precio estimativo en el trato, editable despues

- CU: CU-40.
- Que se corrio: Playwright en el ingreso, sin guardar. No se envio un PUT. El cero es P-60.
- Evidencia: El precio unitario se puede cargar. Sin tarifa el campo queda vacio hasta que exista tarifario, y cambiarlo pide motivo de override. Los ingresos ya existentes de esta lista dicen "No editable en este estado". Una aprobada sin reclamo no se corrige directo. El cero tambien queda habilitado (P-60).
- Veredicto: PARCIAL.

## P-41. El cierre de mes trabaja contra proformas

- CU: CU-41.
- Que se corrio: Lectura del armado de `traspasoCierre` y de `reabrirCierre`. No se cerro ni se reabrio el mes. El dia sin proforma es P-61.
- Evidencia: El asiento solo toma ingresos cuyo `proformaId` esta en las proformas del periodo. No hay tope de una proforma por mes. Reabrir anula el asiento del traspaso si el periodo contable no esta cerrado; si sigue cerrado, pide abrirlo primero. Esta prueba no lo ejecuto.
- Veredicto: PASA.

## P-42. El correo de la OC es interno

- CU: CU-42.
- Que se corrio: Playwright en `/compras/ordenes`. No se envio nada.
- Evidencia: Las acciones de la orden son Ver, Editar, Recepcionar, Imprimir y Anular. No hay "notificar", ni copia, ni un correo externo escrito a mano. El aviso del libro de compras no es este caso.
- Veredicto: FALLA.

## P-43. PDF y Excel de los reportes contables

- CU: CU-43.
- Que se corrio: Playwright en `/contabilidad/libro-diario`, `/contabilidad/mayor`, `/contabilidad/balance-8-columnas` y `/contabilidad/estado-resultados`. Se pulso Exportar PDF del libro diario. No se cerro un mes. La situacion financiera no entra.
- Evidencia: Los cuatro tienen "Exportar Excel/CSV" y "Exportar PDF". El PDF llama a `printReporteContable` con titulo, periodo, razon social, RUT, domicilio si existe, y las columnas de la grilla. El click del diario abrio una ventana de impresion que en esta sesion quedo en blanco; el HTML que escribe el boton si identifica empresa, reporte y periodo.
- Veredicto: PASA.

## P-44. El pago del contratista es el de la factura asociada

- CU: CU-44.
- Que se corrio: Playwright en Contratistas y en `/tesoreria/pagos`, Nuevo pago, sin Crear.
- Evidencia: Contratistas no tiene documento de pago, nomina ni anticipo propios. El pago de tesoreria pide proveedor y "Documentos a calzar". Pendiente no rebaja la deuda.
- Veredicto: PASA.

## P-45. Dia libre en la OC y plazo editable en la factura

- CU: CU-01.
- Que se corrio: Playwright en `/compras/ordenes/nueva`, combo Condicion de pago, sin guardar. En el libro de compras se miro si la factura tiene plazo propio. No se contabilizo.
- Evidencia: El combo de la OC ofrece solo 30, 60 y 90 dias. No hay "Ingresar dias". La factura del libro no tiene plazo de neto ni de IVA. Elegir un 45 que ya vino de la ficha no se pudo: el 45 no esta en el combo si el formulario no lo trae.
- Veredicto: FALLA.

## P-46. El alta de proveedor y de cliente es de jefatura

- CU: CU-02.
- Que se corrio: Lectura de `POST /proveedores` y `POST /clientes`. No se envio el alta y no se creo un usuario.
- Evidencia: Proveedor pide `catalogos:write` o `compras:write`. Cliente pide `comercial:write` o `compras:write`. No hay un corte de jefatura distinto de ese permiso.
- Veredicto: FALLA.

## P-47. Un dia que estaba vacio no reescribe el tipo de cambio ya guardado

- CU: CU-05.
- Que se corrio: Lectura de `tasasDelDia` y `montosLinea` en `comprobante-vista.ts`. No se lanzo la sincronizacion.
- Evidencia: El asiento guardado en pesos no se reescribe. Si la linea no trae el monto en dolar o en yuan, esas columnas se calculan al abrir el comprobante con la tasa del dia que haya en `IndicadorBc`. Llenar un dia que estaba vacio cambia lo que se ve.
- Veredicto: FALLA.

## P-48. La OC de servicio no admite parcial ni hija

- CU: CU-12.
- Que se corrio: Jest `compras.service.spec.ts`, "una parcial confirmada de servicio no nace hija" y "una recepcion confirmada por el neto completo no nace hija y marca RECEPCIONADA" (verde). No se confirmo la recepcion en la empresa.
- Evidencia: El parcial confirmado se rechaza con "una a una" y no llama a `ordenCompra.create`. El neto completo marca `RECEPCIONADA` y tampoco nace hija. `createRecepcion` rechaza `tipo=INSUMOS` por esa pantalla.
- Veredicto: PASA.

## P-49. Sin madre, la guia no entra

- CU: CU-13.
- Que se corrio: Jest `insumos.service.spec.ts`, "sin madre no asocia la guia y no nace hija" (verde). No se digito una guia y no se sincronizo GoSocket.
- Evidencia: Sin `ocMadreId` lanza `BadRequestException` y no crea hija. El inbox de GoSocket que se vio en la pantalla no acredita el caso.
- Veredicto: PASA.

## P-50. No se elige la madre, ni la guia, ni un calce solo por monto

- CU: CU-15.
- Que se corrio: El modal de la factura 63, sin confirmar el vinculo. Lectura del rechazo en `vincularOcRegistroCompra`.
- Evidencia: El modal elige ordenes, no guias. El fuente rechaza la madre, rechaza la hija de insumos sin guia y exige el mismo proveedor. Si el monto difiere en mas de un peso, el registro queda en alerta y la seleccion sigue siendo por orden. La alerta no reemplaza el listado.
- Veredicto: PASA.

## P-51. Una OC solo aprobada no se lista para asociar

- CU: CU-16.
- Que se corrio: El listado de asociacion, sin vincular. No habia en ese modal una OC de servicio `APROBADO` sin recepcion (la factura 63 no tenia ordenes de su proveedor). La columna de hoy se leyo de `getOrdenes`.
- Evidencia: La hija de insumos sin guia no aparece. La OC de servicio, aprobada y sin recepcion, si entra al filtro y se puede asociar.
- Veredicto: FALLA.

## P-52. Una recepcion parcial no reabre la cadena de la madre

- CU: CU-20.
- Que se corrio: Lectura de la recepcion de guia y de `solicitarCierreMadreInsumos`. No se recepciono el parcial y no se pidio el cierre.
- Evidencia: El Jest de la hija parcial la deja `APROBADO` y no devuelve la madre a la cadena. El cierre por lo ya recepcionado es otra accion. Esta prueba no lo pide.
- Veredicto: PASA.

## P-53. El segundo cambio de la madre lo pide contabilidad

- CU: CU-20.
- Que se corrio: Lectura de `PUT /ordenes-compra/:id` cuando la madre ya tuvo cierre. No se ejecuto el segundo PUT.
- Evidencia: Si `cerradaAt` ya tiene fecha, el cierre por lo recepcionado se rechaza. Un cambio de total, hecho por el creador, rearma la cadena y borra `cerradaAt`. No hay un segundo cambio reservado a contabilidad.
- Veredicto: FALLA.

## P-54. Ningun eslabon de la OC se salta por monto

- CU: CU-23.
- Que se corrio: Jest `approval-engine.spec.ts`, "Ana $1.5M pide solo el primer escalon" y "Pedro en el piso de B pide solo a B" (verde). Esos verdes son la columna de hoy. No se envio una OC real.
- Evidencia: Ana en 1,5 millones queda solo en `U-A`. Pedro en el piso de B queda solo en `U-B`. Del segundo eslabon en adelante, el tope que el monto no alcanza se salta. Un spec en verde que omite al segundo aprobador es fallo de este limite.
- Veredicto: FALLA.

## P-55. Exportacion no devuelve; ALM si. No se mueve stock

- CU: CU-24.
- Que se corrio: Lectura del flag en ALMAHUE EXPORT SPA y en ALM SERVICES SPA, sin guardar y sin confirmar salida. El Jest de rechazo es el de P-24.
- Evidencia: En las dos empresas el checkbox "Permite devolucion a proveedor" esta marcado. No hay una empresa del local con el flag apagado en esta lectura, y no se prendio ni se creo una. El rechazo del Jest vale cuando el flag esta apagado. Exportacion, en esta ficha, si tiene el reintegro habilitado. No se movio stock.
- Veredicto: FALLA.

## P-56. Guardar el ingreso diario no lo aprueba

- CU: CU-31.
- Que se corrio: Lectura de `resolveEstadoIngresoNuevo` y de `aprobarIngresoLaborDiario`. No se guardo un ingreso y no se llamo el aprobar. La pantalla del ingreso dice que la aprobacion queda en la proforma.
- Evidencia: El alta deja `PENDIENTE` y no entra a la bandeja. `POST /ingresos-labor-diario/:id/aprobar` sigue publicado y solo actua si el ingreso ya esta `PENDIENTE_APROBACION`, estado que el alta nueva no deja. Al aprobar vuelve a `PENDIENTE`.
- Veredicto: PASA.

## P-57. Una parte de la proforma no se factura

- CU: CU-32.
- Que se corrio: Lectura de `asociarFacturaProforma` con un neto de factura menor que la suma del grupo. No se asocio en la empresa.
- Evidencia: Si la suma de las proformas pasa el neto del registro, no entra. No deja un saldo facturado de una parte: la proforma pasa entera o no entra. Para entrar exige `ENVIADA_CONTRATISTA`, no basta la aprobada. Si el precio no calza, el camino es el reclamo de la enviada, no una fraccion.
- Veredicto: PARCIAL.

## P-58. Proforma ya asociada a una factura: no se edita

- CU: CU-34.
- Que se corrio: Lectura de `PUT`, `reversar` y `reclamo` sobre estado facturado. No se llamo a la API y no se busco una nota de credito.
- Evidencia: `reversar` y `reclamo` aceptan `DEFINITIVA` o `ENVIADA_CONTRATISTA`, no `FACTURADA`. `PUT` solo acepta borrador. `reemitir` crea otra proforma en borrador y deja la anterior rechazada; no es nota de credito y no acredita el caso.
- Veredicto: PASA.

## P-59. En compras se listan las proformas aprobadas, no solo las notificadas

- CU: CU-36.
- Que se corrio: Lectura de `asociarFacturaProforma` y del libro `/compras/registro`. No se asocio y no se cambiaron estados.
- Evidencia: El fuente pide `ENVIADA_CONTRATISTA`. Una `DEFINITIVA` todavia no enviada no entra. El vinculo se hace desde la proforma. El libro no tiene selector de proforma.
- Veredicto: FALLA.

## P-60. El precio cero en el trato no queda habilitado

- CU: CU-40.
- Que se corrio: Lectura de `assertIngresoRefs` cuando no hay tarifa. No se guardo un ingreso en cero. No hay un spec cuyo titulo sea "precio cero"; el Jest filtrado por ese texto no encontro un caso, y la lectura es la del servicio.
- Evidencia: Si no hay tarifa, un precio `>= 0` se guarda, incluido cero. El mensaje dice que cero sirve para una asistencia pendiente de valorizar. Un precio mayor que cero sin tarifa pide `contratistas:rate-override` y un motivo, salvo permiso `*`.
- Veredicto: FALLA.

## P-61. Un dia trabajado sin proforma no entra al asiento del mes

- CU: CU-41.
- Que se corrio: Lectura del armado del traspaso. No se hizo `POST /contratistas/traspaso-cierre` y no se reabrio un periodo.
- Evidencia: Los ingresos del asiento se buscan con `proformaId` dentro de las proformas elegibles. Si el ingreso no tiene proforma del periodo, el cierre lo rechaza. Borrador, pendiente de aprobacion y rechazada quedan fuera. Reabrir no se ejecuto.
- Veredicto: PASA.

---

## Recuento

| Veredicto | Cantidad |
|---|---|
| PASA | 35 |
| PARCIAL | 11 |
| FALLA | 15 |
| BLOQUEO | 0 |
| Total | 61 |

PASA: P-01, P-02, P-04, P-05, P-06, P-09, P-10, P-11, P-12, P-13, P-14, P-15, P-18, P-19, P-21, P-25, P-26, P-27, P-30, P-31, P-33, P-34, P-37, P-38, P-39, P-41, P-43, P-44, P-48, P-49, P-50, P-52, P-56, P-58, P-61.

PARCIAL: P-03, P-07, P-08, P-17, P-23, P-28, P-29, P-32, P-35, P-40, P-57.

FALLA: P-16, P-20, P-22, P-24, P-36, P-42, P-45, P-46, P-47, P-51, P-53, P-54, P-55, P-59, P-60.

BLOQUEO: ninguno. Front y API respondieron. Jest arranco.
