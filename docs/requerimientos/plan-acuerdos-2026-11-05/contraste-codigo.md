# Contraste de codigo: acuerdos 21/10 a 05/11

Corte: 05/11/2026. Fuentes: `casos-de-uso.md`, `plan-integracion.md`, `plan-pruebas.md`. Este archivo dice que hace hoy cada pieza abierta y que tendria que hacer para el caso vigente. No es un diseno. No propone un parche.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Se leyo codigo de `ERP/erp_back` y `ERP/erp_front`. Produccion no se toco.

Si la pieza no se abrio, el veredicto es `NO REVISADO`. Un Completo de la ola D entra solo cuando una ola anterior toca el mismo archivo y la funcion se leyo. CU-13 queda fuera: su pantalla no esta en un archivo que una ola anterior nombre. CU-04, CU-24 y CU-39 no se construyen. Si el codigo todavia ofrece ese camino, la fila apunta al caso que gana (CU-58 o CU-59).

## 1. Veredicto por pieza

| Pieza | CU | Que hace hoy | Que tendria que hacer | Veredicto |
|---|---|---|---|---|
| `insumos.service.ts` `crearGuiaManual` | CU-01 | Da de alta `GuiaDespachoRecibida` con id `MANUAL:`, estado `PENDIENTE`, lineas digitadas y una lista `adjuntos`. No mueve stock. | Seguir igual: guia digitada, con los archivos que se le adjunten, recepcionable despues como cualquier guia pendiente. | CONSERVAR |
| `insumos.service.ts` `createGuiaInsumoRecibida` | CU-57 | Exige insumo, linea de la madre y bodega. Crea el movimiento `ENTRADA_PROVEEDOR` en `CONFIRMADO` y llama `applyTipoToStock` en el mismo paso. `GuiaInsumoRecibida` se graba sin adjuntos ni fecha de confirmacion. | Dejar el stock en cero hasta un confirmar distinto del alta, con el articulo ya elegido, y guardar foto o archivo en la guia fisica. | CAMBIAR |
| `insumos.service.ts` `asociarGuiaDespacho` | CU-47, CU-57 | Si la linea no trae `insumoId`, busca por codigo o nombre (`insumoDeLineaGuia`) y puede crear un articulo nuevo. Al guardar crea el movimiento `CONFIRMADO` y suma bodega. | Cada linea tiene que apuntar a un articulo elegido del maestro. El stock sube recien al confirmar. | CAMBIAR |
| `guia-despacho-gosocket.util.ts` `insumoDeLineaGuia` | CU-47 | Calza la linea de la guia con un insumo por codigo igual o por nombre contenido. | No se usa en la recepcion. El caso que gana es elegir el articulo del maestro (CU-47). | NO USAR PARA ESTE CASO |
| `insumos.service.ts` `naceHijaPorGuia` | CU-02, CU-43 | Si la madre ya tiene hijas, toda guia nueva nace otra hija. Si la guia completa la orden, no nace hija y la madre pasa a `RECEPCIONADA`. No hay marca de ultima guia ni un ajuste de cantidades de la madre. | Hija por cada guia. Un solo ajuste de la madre, en la ultima guia, por cantidad. | CAMBIAR |
| `oc-madre-hija.util.ts` `crearOcHijaDeRecepcion` | CU-02, CU-43 | Crea la hija `APROBADO`, numero `madre.n`, neto igual al trozo, `ocPadreId` y `referenciaTipo = OC_PADRE`. No la manda a la cadena. | Seguir igual: la hija nace aprobada, por el trozo, colgada de la madre. | CONSERVAR |
| `oc-madre-hija.util.ts` `assertCalceFacturaHija` | CU-02 | Si el monto no calza (tolerancia 1), rechaza con el texto de calce al 100%. | Seguir igual: la hija no se cierra si la factura no calza. | CONSERVAR |
| `compras.service.ts` `vincularOcRegistroCompra` | CU-02 | No asocia la factura a la madre de insumos. Exige hija con guia. Si el monto calza, escribe `cerradaAt` en la hija con motivo de factura. Una misma factura puede cerrar varias hijas si la suma calza. | Seguir igual en el cierre de la hija al facturar y en dejar el saldo de control en la madre. | CONSERVAR |
| `insumos.service.ts` `getOrdenesInsumos` | CU-02 | Marca `MADRE`, `HIJA` o `NORMAL` y calcula el pendiente de la madre como neto menos la suma de hijas. | Seguir igual: el saldo visible queda en la madre. | CONSERVAR |
| `insumos.service.ts` `resolverPrecioFactura` | CU-35 | En `DEVOLUCION`, `DEVOLUCION_NC` y `SALIDA_PROVEEDOR` exige folio y toma el precio de la factura o de la entrada de origen. Si no hay precio, rechaza. No usa el costo promedio. | Seguir igual para el precio de la devolucion. | CONSERVAR |
| `insumos.service.ts` `applyTipoToStock` | CU-56 | `DEVOLUCION` y `DEVOLUCION_NC` suman stock. `SALIDA_PROVEEDOR` lo resta. | El documento de devolucion no le saca existencia a la guia de origen, aunque esas unidades ya se hayan consumido. | CAMBIAR |
| `insumos.service.ts` `createMovimiento` | CU-35, CU-56 | Pide el precio de origen en la devolucion, graba el movimiento y, si queda `CONFIRMADO`, mueve stock. Puede armar un par `SALIDA_PROVEEDOR` / `DEVOLUCION` con `parId`. | Conservar el precio de la guia y dejar un documento nuevo que no rebaje esa guia. | CAMBIAR |
| `approval-engine.ts` `eslabonCubreMonto` | CU-52 | Si `montoMax` es null, cualquier monto cierra en ese eslabon. | El ultimo eslabon tiene techo. Si la OC lo pasa, no cierra ahi. | CAMBIAR |
| `approval-engine.ts` `buildCadenaDesdeGrupo` | CU-51, CU-52 | Recorre los nodos que el grupo tenga. El primero entra desde monto 0. Un `montoMax` null corta la cadena. Salta al solicitante y al mantenedor. No hay tres cargos fijos. | Siempre jefatura, despues gerencia de area y despues gerencia general, sin saltar el primero. El ultimo tiene techo. | CAMBIAR |
| `approval-engine.ts` `resolveCadenaCompleta` | CU-45, CU-51 | Si hay grupos activos, usa la escala del grupo. Si no, llama `buildCadenaAprobacion`, que sube por `jefeId`. | La cadena sale solo del grupo. El organigrama no arma la OC. | CAMBIAR |
| `approval-engine.ts` `buildCadenaAprobacion` | CU-46 | Parte del `jefeId` del solicitante y sube la linea de mando. | No se usa para la OC. El caso que gana es el grupo y la escala (CU-50). El arbol queda como vista (CU-45). | NO USAR PARA ESTE CASO |
| `compras.service.ts` `resolveCadenaAprobacion` | CU-52 | Si no hay cadena, responde que hay que configurar la escala. Si el ultimo nodo no tiene tope, la OC entra a la bandeja. No hay mensaje de monto de gerencia. | Si la OC pasa el tope del ultimo, no se encola y el mensaje dice que excede el monto de gerencia. | CAMBIAR |
| `compras.service.ts` `resolveNetoClpParaCadena` | CU-53 | Pasa USD o yuan a CLP con `IndicadorBc` del dia y compara un solo numero. Si no hay tipo, deja el neto en la moneda original. No guarda en la OC un tipo propuesto y despues fijo. | Tope en CLP, USD y yuan. Al tipear pesos, un tipo del dia editable que despues queda fijo en la OC. | CAMBIAR |
| `schema.prisma` `GrupoAprobacion` | CU-50 | Grupo por `modulo` y `nombre`, con miembros y aprobador inicial. `UsuarioGrupoAprobacion.esJefe` es un flag. No hay area del grupo ni cargo del miembro. | Un grupo por area que compra, con jefatura, gerencia de area y gerencia general, y tope propio. | CAMBIAR |
| `schema.prisma` `NodoEscalaAprobacion.montoMax` | CU-53 | Un solo monto por eslabon. | Tres topes: CLP, USD y yuan. El `montoMax` actual es el punto de partida. | CAMBIAR |
| `packing.service.ts` `createReceta` | CU-54 | Guarda la receta con `packingId` opcional y `cantidadPorCaja`. No tiene centro de costo. | Receta de embalaje con centro de costo, sin packing obligatorio, y cantidad por packing. La crea la jefatura, sin cadena. | CAMBIAR |
| `packing.service.ts` `createProduccion` | CU-54, CU-55 | Exige packing, receta y cajas. El costo sale de `costoUnitario` de la linea o de `Insumo.costoPromedio` en el momento. Descuenta stock con `SALIDA_VENTA` confirmada. | El consumo no queda atado a un solo packing. El precio es el promedio del stock del mes, con saldo anterior, sin FIFO y sin reescribir un mes ya consumido. El consumo pasa por aprobacion. | CAMBIAR |
| `activo-fijo.service.ts` `crearActivo` | CU-58 | Crea el bien contra una factura del libro (`registroCompraId` o folio). Pide `vidaUtilMeses`. El alta leida no exige OC recepcionada ni escribe `ordenCompraId`. El modelo todavia tiene `centroCostoId` y `vidaUtilTributariaAnios`. El camino "directo, con la factura y sin OC" es el que CU-04 ya no manda. | Crearlo solo desde una OC tipo activo fijo ya recepcionada. Avisar si falta factura. Sin centro de costo en el alta. Una sola vida util, en meses. | CAMBIAR |
| `compras.service.ts` `createOrden` | CU-29 | Acepta `tipo` `ACTIVO_FIJO` y lo graba. No crea `ActivoFijo`. | Seguir igual: la OC queda marcada y el maestro espera la recepcion. | CONSERVAR |
| `OrdenCompraWizardPage.tsx` | CU-16, CU-29 | El combo tiene Activo fijo. En la linea, centro y elemento siguen deshabilitados hasta elegir cuenta, y al cambiar la cuenta se vacian. | Seguir igual: primero la cuenta, y el tipo activo fijo no crea el bien. | CONSERVAR |
| `solicitud-reversa-edicion.service.ts` `recentralizarPeriodo` | CU-59 | Cierra solicitudes `APROBADA_REAPERTURA` y guarda en `reCierre` un texto de asiento, sin crear comprobante y sin reescribir `Asiento.lineas`. | Guardar el valor nuevo en la linea que ya existe, con historial, sin asiento de ajuste ni de reversa. | CAMBIAR |
| `contabilidad.service.ts` `updateAsiento` | CU-59 | Un asiento `CONTABILIZADO` no se edita. La unica salida es `aplicarAnulacionConReverso`. El mensaje dice que se anule o que se cree un asiento de ajuste nuevo. Ese ajuste es el camino pisado (CU-24 y CU-39). | La correccion de la proforma edita la linea existente. No nace otro comprobante. | CAMBIAR |
| `activo-fijo.service.ts` `upsertIpc` | CU-07 | Guarda un valor por `periodoYm` en `ActivoFijoIpc`. El mismo mes se pisa. Vive en activo fijo, no en el mantenedor del factor. | IPC consultable en parametrizacion, con historial de valores que no se borre al cargar uno nuevo. | CAMBIAR |
| `contabilidad.service.ts` `createFactorHonorario` | CU-07 | Guarda factor anterior, factor nuevo, vigencia y usuario. | Seguir igual para el factor. El IPC es la otra pieza. | CONSERVAR |
| `LibroDiarioMayorPages.tsx` | CU-09 | Tiene desde y hasta. Pide un mayor por mes y, en el cliente, deja solo los movimientos del rango. | Seguir igual para el filtro de fechas del mayor. El balance de 8 y el ER no se rehacen aqui. | CONSERVAR |
| `contabilidad.service.ts` `getMayor` | CU-59, CU-60 | El mayor es de un periodo `aaaa-mm`. `asientosParaReporte` deja el asiento `ANULADO` si existe su reversa, para que el par sume cero. | El mayor muestra solo activos. Lo anulado queda en la fila y no entra. | CAMBIAR |
| `CartolaBancariaPage.tsx` | CU-10 | La carga es el archivo del banco. Hay banco, moneda y adjuntos en el movimiento. El combo PDF filtra el formato de importacion. No hay una vista en pesos ni una exportacion PDF de la cartola. | Vista en pesos y PDF de la cartola. El adjunto del pago ya tiene donde guardarse (`Pago.adjuntos`). | CAMBIAR |
| `FichaContraparteModal.tsx` | CU-12 | El modal es `cliente` o `proveedor`. El productor es el check `esProductor` de esa ficha. No copia contacto al otro maestro cuando el RUT ya existe. | Listas separadas, contacto compartido si el RUT es el mismo, y marca de mas de un rol. Sin maestro Productor. | CAMBIAR |
| `contabilidad.service.ts` `syncCuentaVinculos` | CU-15 | Reemplaza las tres listas de la cuenta: centros, elementos y areas. No hay vinculo elemento-centro. | Seguir igual en las tres listas. El contador al clic del mantenedor inverso no se abrio. | CONSERVAR |
| `ComprasPages.tsx` `printOc` | CU-17 | La hoja agrega el centro al texto de la linea y puede listar la distribucion de centros en la observacion. | La hoja que va al proveedor, sin centro, sin elemento y sin cuenta. | CAMBIAR |
| `historial.service.ts` `anotar` y `listar` | CU-23 | Guarda titulo, detalle, usuario y fecha. `listar` solo abre orden de compra, documento y guia. No hay valor anterior ni valor nuevo. | Historial de parametrizacion con valor anterior, valor nuevo, fecha y quien, sin nombres de campos. | CAMBIAR |
| `schema.prisma` `CuentaContable.requierePlanta` y `catalog-excel-plantilla.ts` | CU-23 | El flag sigue en la cuenta, con default falso. La plantilla Excel todavia exporta la columna PLANTA. | Imputar sin planta. La columna no vuelve a la plantilla ni al comprobante. | CAMBIAR |
| `notas-cobro.service.ts` altas `GASTO_DIRECTO` y `EMBARCADOR` | CU-28 | Hay nota de gasto con cuenta y lineas, y nota de embarcador con facturas asociadas. Si la factura ya esta en otra nota, la rechaza. | Seguir igual en los dos tipos. La carga de muchas filas es la otra pieza. | CONSERVAR |
| `notas-cobro.service.ts` `prevalidarExcel` | CU-28 | Recorre filas y separa facturas encontradas y no encontradas. No crea la nota ni reparte el asiento por proveedor. | La carga de muchas filas, por proveedores, cuando la nota del tercero trae cientos de facturas. | CAMBIAR |
| `ProformasContratistaNivel1Page.tsx` | CU-40 | La grilla filtra por el periodo del banner, salvo el modo todo. La columna de relacionados arma la fila Factura solo si hay folio o `registroCompraId`. | Seguir igual: periodo de la grilla, y factura solo cuando hay vinculo. | CONSERVAR |
| `insumos.service.ts` `esJefeArea`, `AdminConceptoPanel.tsx`, `Sidebar.tsx` | CU-49 | Sigue el mantenedor de administradores por modulo. `esJefe` de Insumos filtra entradas del menu. | Sacar ese mantenedor de la operacion. El acceso queda en el rol. | CAMBIAR |
| `contabilidad.service.ts` `anularAsiento` y `aplicarAnulacionConReverso` | CU-60 | Marca `ANULADO` y crea otro comprobante de reverso. El motivo va a la glosa del reverso. No hay solicitante ni jefatura. | La fila queda, con motivo, fuera del mayor. Lo hace la jefatura, o un analista solicita y la jefatura aprueba. Sin reverso. | CAMBIAR |
| `OrganigramaPage.tsx` | CU-45, CU-61 | Arma el arbol con `Usuario.jefeId`. Pinta los cuatro titulos segun la profundidad. En la tarjeta muestra `montoMaxAprobacion`. No llama al motor de la cadena. | Los cuatro titulos, solo como vista, sin montos y sin efecto en la OC. | CAMBIAR |
| `insumos.service.ts` `asientoExistenciaVsFxr` | CU-03 | Al asociar la guia arma existencia contra facturas por recibir y lo cuelga del movimiento (`GUIA-FXR`). | Ese asiento va en el cierre de bodega, no al recepcionar. | CAMBIAR |
| `insumos.service.ts` `cerrarBodega` | CU-03 | Arma `CIERRE-BODEGA:{periodo}` con las cuentas del tipo de movimiento. Deja fuera los movimientos que ya tienen `asientoRecepcionId`. Despues llama el calce de facturas. La glosa del dto se guarda. | Los dos momentos (existencia contra facturas por recibir, y el calce al proveedor) viven en este cierre. La orden hija no se contabiliza aparte. | CAMBIAR |
| `compras.service.ts` `contabilizarFacturasCierreBodega` | CU-03 | Al cerrar bodega contabiliza facturas no anuladas ni contabilizadas ligadas a hijas de insumos. La consulta leida no filtra por el periodo. | El calce del periodo, en el cierre, reconociendo al proveedor y sacando facturas por recibir. | CAMBIAR |
| `compras.service.ts` `contabilizarMadreInsumos` | CU-03 | Boton de la madre: si el cuadre habilita, contabiliza las facturas y pasa madre e hijas a `CONTABILIZADA`. | No hay accion de contabilizar en la orden hija. El asiento queda en el cierre de bodega. | CAMBIAR |
| `oc-madre-hija.util.ts` `evaluarCuadreMadreInsumos` | CU-02, CU-03 | Habilita ese boton solo si cada hija tiene guia y factura aceptada y la suma de hijas y de facturas cuadra con el neto de la madre. | La madre puede seguir con saldo. La hija no se contabiliza en la orden. | CAMBIAR |
| `contratistas.service.ts` `traspasoCierre` | CU-05, CU-20, CU-21, CU-26 | Toma proformas `DEFINITIVA`, `ENVIADA_CONTRATISTA` y `FACTURADA` del periodo. Un asiento `TRASPASO-CTR:{periodo}`. El debe agrupa por `centroCostoId`. El haber lleva `auxiliar` con el RUT. Glosa y cuentas salen del dto. | Seguir igual: bloque aprobado, un asiento del periodo, gasto por centro y RUT en el puente. Borrador e ingreso suelto no entran. | CONSERVAR |
| `contabilidad.service.ts` `getAsientos` | CU-06 | `soloActivos=true` omite `ANULADO`. Sin el parametro trae todos. No hay comentario distinto de la glosa ni PDF. | Descarga por defecto de activos, glosa visible y un comentario aparte. El PDF del comprobante no tiene funcion abierta. | CAMBIAR |
| `contabilidad.service.ts` `updateGlosaAsiento` | CU-06 | Cambia la glosa solo si el asiento no esta contabilizado ni anulado. | La glosa del comprobante se ve. El comentario editable es otro dato y no reescribe el monto. | CAMBIAR |
| `contabilidad.service.ts` `createPresupuesto` | CU-08 | Guarda anio, centro en texto, monto presupuestado y monto ejecutado digitado. | Ver la ejecucion anual del centro, calculada desde lo imputado, e imprimirla. | CAMBIAR |
| `CuentasCorrientesPage.tsx` | CU-11 | Consulta por RUT, filtra Todos / Proveedor / Productor / Cliente y exporta a Excel las filas filtradas, con rol y folio. El nombre del archivo lleva el RUT. | Seguir igual: Excel del RUT con los movimientos del filtro. | CONSERVAR |
| `contabilidad.service.ts` `bulkCreateAsientos` | CU-14 | Valida linea por linea, devuelve errores y graba las validas en una transaccion. Si la transaccion falla, `created` queda en 0 y no queda ninguna. | Las lineas buenas quedan cargadas, las malas fuera, y el reporte trae el conteo aunque una linea falle. | CAMBIAR |
| `contratistas.service.ts` envio de la proforma a `PENDIENTE_APROBACION` | CU-19 | La proforma entra a su cadena de contratistas. La OV no pasa por esta funcion. | Seguir igual: la aprobacion queda en la proforma. | CONSERVAR |
| `contratistas.service.ts` `INGRESO_ESTADOS_PARA_PROFORMA` | CU-19 | El ingreso diario admite `PENDIENTE_APROBACION`. | El ingreso diario no se aprueba uno a uno. La aprobacion queda en la proforma. | CAMBIAR |
| `compras.service.ts` `assertOcParaRegistroCompra` | CU-42 | Sin OC en estado que opera no contabiliza, salvo que el registro tenga tipo de contrato o proforma asociada. | Seguir igual en la puerta: sin OC ni proforma no hay asiento. La cobertura y el filtro de la pantalla no se abrieron. | CONSERVAR |
| `RegistroBoletaHonorariosModal.tsx` | CU-30 | Graba un `RegistroCompra` con `tipoDte` HONORARIOS y un folio digitado. No emite. En el tipo 1002 exige numero de rendicion. El adjunto que manda es el nombre del archivo, no el contenido. No usa `FactorHonorario`. | Boleta recibida, asociada a quien la rindio, sin folio emitido por Almahue. No se ingresa la que nadie rindio. | CAMBIAR |
| `schema.prisma` `ProformaRegistroCompra` y `facturaNumeroRef` | CU-41 | Una proforma puede quedar en varias facturas y una factura puede agrupar proformas. El comentario del modelo dice N:N. | Vinculo 1 a 1. La cobertura puede ser parcial, sin campo porcentaje. | CAMBIAR |
| `tesoreria.service.ts` `importarCartola` | CU-18, CU-31 | Recibe las lineas del archivo. Omite el movimiento ya cargado con la llave fecha, signo, monto y referencia o glosa. No abre una conexion al banco. | Seguir igual: el archivo que baja Lupe, sin duplicar. | CONSERVAR |
| `cartola-periodo.util.ts` `filtrarLineasAlMesSesion` | CU-32 | Deja solo las fechas del mes de la sesion. Si hay lineas de otro mes, avisa y dice cuantas excluyo. | Seguir igual: aviso de periodo y la linea del mes anterior fuera. | CONSERVAR |
| `tesoreria.service.ts` `contabilizarMovimientoCartola` | CU-33 | Parte el ingreso en 2 o 3 codigos, en la moneda de la cartola, y rechaza si la suma pasa el monto. Si falta saldo, igual contabiliza y devuelve `avisoSaldo`. Una cuarta parte se corta con `slice` y no se rechaza. | Hasta tres partes, suma igual al movimiento, sin saldo sin asignar y sin una cuarta parte. | CAMBIAR |
| `schema.prisma` `BancoCuenta` | CU-34 | Tiene `numero` y `nombre`. El comentario del campo dice que el nombre va junto al numero. | Seguir igual en el dato. La pantalla que lo muestra no se abrio en este pase. | CONSERVAR |
| `contratistas.service.ts` `assertPeriodoOperable` | CU-37 | Si el cierre de contratistas o el periodo contable esta cerrado, responde conflicto. No reabre el periodo. | Seguir igual: Traspaso no reabre el mes. | CONSERVAR |
| `contabilidad.service.ts` `getBalance8Columnas` | CU-27 | Pide un periodo. El resultado arranca en enero de ese ano (`saldosInicialesEjercicio`). El inventario arrastra el saldo anterior a ese periodo. | Seguir igual: un balance del ano, de enero al periodo elegido. | CONSERVAR |
| `GuiasInsumosRecibidasPage.tsx` | CU-01, CU-47, CU-57 | No se abrio. | - | NO REVISADO |
| `MovimientosBodegaPage.tsx` | CU-35, CU-56 | No se abrio. | - | NO REVISADO |
| `CierreBodegaPage.tsx` | CU-03, CU-05 | No se abrio. | - | NO REVISADO |
| `OrdenesAplicacionPage.tsx` | CU-54, CU-55 | No se abrio. | - | NO REVISADO |
| `WorkflowAprobacionesPage.tsx` | CU-44, CU-50, CU-51, CU-52, CU-53 | No se abrio. El motor si. | - | NO REVISADO |
| Pagina `/presupuestos` | CU-08 | No se abrio. El alta del back si. | - | NO REVISADO |
| Pantalla `/compras/registro` (cobertura, filtro y etiqueta) | CU-42 | No se abrio. La puerta `assertOcParaRegistroCompra` si. | - | NO REVISADO |
| `ProformaReversaProtocoloPanel` y el origen de `requiereSolicitud` | CU-38 | En la grilla, si no exige solicitud o la edicion ya esta habilitada, el modal pide la clave. No se abrio quien decide eso cuando el periodo esta cerrado. | - | NO REVISADO |
| `LaborActividad` y el mantenedor de actividad | CU-19 | No se abrio. La cadena de la proforma si. | - | NO REVISADO |
| Aviso de calce y acuse al creador (`ProformaNotificacionEvento`) | CU-41 | No se abrio. El vinculo N:N si. | - | NO REVISADO |

## 2. Recuento

| Veredicto | Filas |
|---|---|
| CONSERVAR | 22 |
| CAMBIAR | 41 |
| NO USAR PARA ESTE CASO | 2 |
| NO REVISADO | 10 |
| Total | 75 |

## 3. Por donde empezar

Solo piezas `CAMBIAR` de las olas A, B y C. No es una tarea.

### Ola A

- `createGuiaInsumoRecibida` - CU-57
- `asociarGuiaDespacho` - CU-47, CU-57
- `naceHijaPorGuia` - CU-02, CU-43
- `applyTipoToStock` - CU-56
- `createMovimiento` - CU-35, CU-56
- `eslabonCubreMonto` - CU-52
- `buildCadenaDesdeGrupo` - CU-51, CU-52
- `resolveCadenaCompleta` - CU-45, CU-51
- `resolveCadenaAprobacion` - CU-52
- `resolveNetoClpParaCadena` - CU-53
- `GrupoAprobacion` - CU-50
- `NodoEscalaAprobacion.montoMax` - CU-53
- `createReceta` - CU-54
- `createProduccion` - CU-54, CU-55
- `crearActivo` - CU-58
- `recentralizarPeriodo` - CU-59
- `updateAsiento` - CU-59
- `getMayor` - CU-59, CU-60

### Ola B

- `upsertIpc` - CU-07
- `CartolaBancariaPage` - CU-10
- `FichaContraparteModal` - CU-12
- `printOc` - CU-17
- `historial.service` `anotar` / `listar` - CU-23
- `CuentaContable.requierePlanta` y la plantilla Excel - CU-23
- `prevalidarExcel` - CU-28
- `evaluarCuadreMadreInsumos` - CU-02, CU-03
- `esJefeArea` y `AdminConceptoPanel` - CU-49
- `anularAsiento` - CU-60
- `OrganigramaPage` - CU-45, CU-61

### Ola C

- `asientoExistenciaVsFxr` - CU-03
- `cerrarBodega` - CU-03
- `contabilizarFacturasCierreBodega` - CU-03
- `contabilizarMadreInsumos` - CU-03
- `getAsientos` - CU-06
- `updateGlosaAsiento` - CU-06
- `createPresupuesto` - CU-08
- `bulkCreateAsientos` - CU-14
- `INGRESO_ESTADOS_PARA_PROFORMA` - CU-19
- `RegistroBoletaHonorariosModal` - CU-30
- `ProformaRegistroCompra` - CU-41

`contabilizarMovimientoCartola` (CU-33) tambien quedo `CAMBIAR`. Es ola D, el mismo archivo que la cartola, y no entra en esta lista.
