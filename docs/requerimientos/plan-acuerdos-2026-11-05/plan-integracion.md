# Plan de integracion: acuerdos 21/10 a 05/11

Corte: 05/11/2026. Fuente de los casos: `casos-de-uso.md` (CU-01 a CU-66). Este plan dice por donde entra cada caso en el codigo local de hoy y de que otro caso depende. No es una lista de tareas, no redisena pantallas y no propone un parche.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`. El corte es el codigo de este repo. Produccion no se acredita.

Tenant: todo lo que se nombra filtra por `empresaId`. La cadena de la OC entra por grupos y escalas (`ERP/erp_back/src/modules/aprobaciones/approval-engine.ts`, pantalla `/admin/aprobaciones`). No se usa `workflows-admin`. La ruta front `workflow/*` redirige al inicio. La aprobacion con cadena sigue solo en la OC de compras. La orden de venta se confirma al guardar, sin cadena. La cotizacion es referencia dentro de la OC. Merma no existe. El organigrama no arma la cadena.

## 1. Mapa de modulos

Solo modulos que ya existen, o una extension dentro de uno que ya existe. Si el caso no cabe, la fila dice `hueco`.

| Modulo | Casos que lo tocan | Back | Front |
|---|---|---|---|
| Insumos | CU-01, CU-02, CU-03, CU-35, CU-43, CU-47, CU-54, CU-55, CU-56, CU-57. CU-64 y CU-65 no se integran y se nombran aqui para no abrir otro modulo | `ERP/erp_back/src/modules/insumos/insumos.service.ts`, `packing.service.ts`, `insumos.controller.ts` | `/insumos/guias-recibidas` (`GuiasInsumosRecibidasPage.tsx`), `/insumos/movimientos` (`MovimientosBodegaPage.tsx`), `/insumos/cierre` (`CierreBodegaPage.tsx`), `/insumos/ordenes-aplicacion` (`OrdenesAplicacionPage.tsx`), `/insumos/ordenes` |
| Compras | CU-16, CU-17, CU-28, CU-29, CU-30, CU-42 | `ERP/erp_back/src/modules/compras/compras.service.ts`, `compras.controller.ts`, `notas-cobro.service.ts`, `oc-estado.util.ts` | `/compras/ordenes` y `/compras/ordenes/nueva` (`ComprasPages.tsx`, `OrdenCompraWizardPage.tsx`), `/compras/registro` (libro), `/compras/notas-cobro` (`NotasCobroPage.tsx`), modal `RegistroBoletaHonorariosModal.tsx` |
| Contratistas | CU-05, CU-19, CU-20, CU-21, CU-22, CU-25, CU-26, CU-37, CU-38, CU-40, CU-41 | `ERP/erp_back/src/modules/contratistas/contratistas.service.ts`, `solicitud-reversa-edicion.service.ts` | `/contratistas/proformas`, `/contratistas/traspaso`, `/contratistas/ingreso-diario`, `/catalogos/contratista` |
| Contabilidad | CU-06, CU-07, CU-08, CU-09, CU-13, CU-14, CU-15, CU-23, CU-27, CU-59, CU-60 | `ERP/erp_back/src/modules/contabilidad/contabilidad.service.ts`, `contabilidad.controller.ts` | `/contabilidad/asientos`, `/contabilidad/mayor`, `/contabilidad/balance-8-columnas`, `/contabilidad/estado-resultados`, `/contabilidad/situacion-financiera`, `/catalogos/plan-cuentas`, `/presupuestos`, `/catalogos/factor-honorarios` |
| Tesoreria | CU-10, CU-11, CU-18, CU-31, CU-32, CU-33, CU-34. CU-36 no se integra | `ERP/erp_back/src/modules/tesoreria/tesoreria.service.ts`, `tesoreria.controller.ts` | `/tesoreria/cartolas`, `/tesoreria/cuentas-corrientes`, `/tesoreria/pagos` |
| Activo fijo | CU-29, CU-58. CU-04 no se integra | `ERP/erp_back/src/modules/activo-fijo/activo-fijo.service.ts`, `activo-fijo.controller.ts` | `/activo-fijo/ingreso`, `/activo-fijo/maestro`, `/catalogos/activo-fijo` |
| Aprobaciones (grupos y escalas) | CU-44, CU-49, CU-50, CU-51, CU-52, CU-53. CU-46 no se integra | `ERP/erp_back/src/modules/aprobaciones/approval-engine.ts`. Grupos en el modulo admin | `/admin/aprobaciones` (`WorkflowAprobacionesPage.tsx`), `/admin/administradores`, `/compras/aprobaciones` |
| Admin | CU-45, CU-49, CU-61 | Usuario.`jefeId` en `schema.prisma`. Roles en admin | `/admin/organigrama` (`OrganigramaPage.tsx`), `/admin/roles`, `/admin/administradores` |
| Ficha de contraparte | CU-12, CU-11 | `Proveedor`, `Cliente` y flag `esProductor` en `schema.prisma`. Catalogos | `/catalogos/proveedores`, `/catalogos/productores`, `/comercial/clientes`, `FichaContraparteModal.tsx` |
| hueco | CU-36 proyectado, CU-48 AlmaWeb, CU-63 reportes por jefatura, CU-66 packing de cajas COMEX | Punto de entrada no ubicado para esos cuatro terminos. `reporteria` existe y no es el paquete de CU-63. El `Packing` de insumos no es el packing COMEX | La ruta `reportes/*` redirige a `/`. No hay pantalla de proyectado, de AlmaWeb ni de packing COMEX |

## 2. Orden de integracion

Fuera de las olas, porque no se codea: CU-04, CU-24, CU-39, CU-36, CU-46, CU-48, CU-62, CU-63, CU-64, CU-65, CU-66.

Una ola solo pide casos de una ola anterior, de la misma ola, o un Completo. La ola D no se construye: un Completo ya esta en el codigo y no cuenta como requisito pendiente. Si dos casos se citan en circulo, quedan en la misma ola.

### Ola A

Casos: CU-01, CU-29, CU-35, CU-47, CU-50, CU-51, CU-52, CU-53, CU-54, CU-56, CU-57, CU-58, CU-59.

Van juntos porque los circulos de la sala no se pueden partir, y ninguno de estos casos pide a la ola B ni a la C:

- CU-47 y CU-57 se citan entre si. CU-57 tambien pide CU-01. CU-01 no pide a CU-57: el stock al confirmar es la precision, no un requisito del tipeo. Los tres quedan aqui.
- CU-50, CU-51, CU-52 y CU-53 se citan en circulo. El grupo, los tres cargos y el tope son un solo cambio de la escala que ya existe.
- CU-29 y CU-58 se citan entre si. El tipo de la OC y el alta del maestro van juntos. CU-29 no agrega modulo.
- CU-35 y CU-56 se citan entre si. El precio de origen y el documento que no rebaja la guia van juntos. CU-35 no agrega modulo.
- CU-54 no pide a CU-55. CU-59 no pide a CU-60 ni a CU-22. Esos tres quedan en la ola B.

No hay una ola anterior que construir.

### Ola B

Casos: CU-02, CU-07, CU-09, CU-10, CU-12, CU-15, CU-17, CU-22, CU-23, CU-28, CU-40, CU-49, CU-55, CU-60, CU-61.

Van juntos porque cada uno pide la ola A, un Completo, o ninguno. No se piden entre si.

Que no se puede codear antes de esta ola: CU-55 espera a CU-54. CU-60 espera a CU-59. CU-22 espera a CU-59 (y al Completo CU-38). CU-02 no es requisito de CU-47 ni de CU-57. Lo precisa CU-43, en la ola C.

### Ola C

Casos: CU-03, CU-05, CU-06, CU-08, CU-11, CU-14, CU-19, CU-20, CU-21, CU-25, CU-26, CU-30, CU-41, CU-42, CU-43.

Van juntos porque piden la ola A o la B, y el cierre de contratistas es un circulo que no se parte: CU-05, CU-19, CU-20, CU-21, CU-25, CU-26, CU-41 y CU-42 se citan entre si. El traspaso ya vive en `contratistas.service.ts`.

Que no se puede codear antes de esta ola: CU-03 y CU-43 esperan a CU-02. CU-43 tambien espera a CU-47. CU-06 espera a CU-59 y CU-60. CU-08 y CU-14 esperan a CU-15. CU-11 espera a CU-12. CU-30 espera a CU-07. Dentro del circulo de contratistas no hay un caso que se codee en otra ola.

### Ola D

Casos: CU-13, CU-16, CU-18, CU-27, CU-31, CU-32, CU-33, CU-34, CU-37, CU-38, CU-44, CU-45.

Regresion. No se construye. Solo se vuelve a pasar si una ola anterior toco el mismo archivo.

## 3. Casos

### CU-01. Ingreso manual de la guia mientras abastecimiento siga en Acepta

- Por donde entra hoy: `/insumos/guias-recibidas`. `POST guias-despacho-recibidas/manual` en `insumos.service.ts` (alta manual sobre `GuiaDespachoRecibida`). `POST guias-insumo-recibidas` es la guia fisica ya amarrada a una madre.
- Que deja el codigo hoy: la guia manual guarda adjuntos en `GuiaDespachoRecibida.adjuntos` y no mueve stock hasta asociarla a la madre.
- Que pide la sala: seguir digitando la guia mientras abastecimiento opere en Acepta, con varios archivos o un Excel de Acepta.
- Depende de: ninguno para el tipeo. El stock al confirmar es CU-57.
- Datos: `GuiaDespachoRecibida.adjuntos` (Json) ya existe. `GuiaInsumoRecibida` no tiene adjuntos. Excel de Acepta: punto de entrada no ubicado (busque `Acepta`).

### CU-02. La hija no queda con saldo

- Por donde entra hoy: `/insumos/guias-recibidas` al asociar, `asociarGuiaDespacho` y `createGuiaInsumoRecibida`. La hija la arma `crearOcHijaDeRecepcion` cuando `naceHijaPorGuia` ve que la guia no cierra la madre. Listado en `GET insumos/ordenes`.
- Que deja el codigo hoy: la hija nace por el trozo de la guia, con su neto, y la madre sigue siendo la orden con saldo pendiente.
- Que pide la sala: hija cerrada al facturar, siempre calzada, y saldo solo en la madre.
- Depende de: ninguno para nacer. Lo precisa CU-43. El articulo y el stock son CU-47 y CU-57.
- Datos: `OrdenCompra.ocPadreId`, `GuiaInsumoRecibida.ocMadreId` y `ocHijaId` ya existen. No hay un estado propio "hija cerrada al facturar" distinto de `EstadoDocumentoErp`.

### CU-03. La hija no se contabiliza en la orden

- Por donde entra hoy: `/insumos/cierre` y `POST insumos/cierre-bodega` (`cerrarBodega`). Tambien `POST insumos/ordenes/:id/contabilizar` y `previewContabilizarMadreInsumos` en compras.
- Que deja el codigo hoy: el cierre arma un asiento `CIERRE-BODEGA:{periodo}` con las cuentas del tipo de movimiento, y la guia puede llevar `asientoRecepcionId` de existencia contra facturas por recibir.
- Que pide la sala: esos asientos en el cierre de bodega, y sin accion de contabilizar en la orden hija.
- Depende de: CU-02. Las cuentas que falten son CU-65 y no se integran.
- Datos: `CierreBodega`, `CuentaTipoMovimientoBodega` y `MovimientoBodega.asientoRecepcionId` ya existen. No hay cuenta de merma. Schema de un asiento "de calce" distinto del cierre: no esta como modelo propio; el calce de facturas del periodo entra por `contabilizarFacturasCierreBodega`.

### CU-04. Activo fijo que no nace de una OC

No se integra. La regla que gana es CU-58.

### CU-05. Cierre de contratistas: aprobadas con factura, cuenta y glosa

- Por donde entra hoy: `/contratistas/traspaso`. El cierre vive en `contratistas.service.ts` (traspaso del periodo, glosa `Traspaso/cierre contratistas`).
- Que deja el codigo hoy: el cierre toma ingresos de proformas del periodo y usa la cuenta al debe y al haber guardadas en la empresa, con glosa editable en el dto.
- Que pide la sala: que entren las aprobadas, que la jefatura pueda cambiar cuenta y glosa, y el mismo par en bodega. La factura del mismo mes la aflojan CU-20 y CU-42.
- Depende de: CU-20 y CU-21.
- Datos: `Empresa.cierreContratistaDebeId` y `cierreContratistaHaberId` ya existen. `ProformaContratista.cuentaGastoId` ya existe. Un rol de sistema llamado jefatura para esa glosa: no esta; el visto bueno de contratistas vive en `SolicitudReversaEdicion`.

### CU-06. Ver el asiento, comentar, anular, reversar y filtrar activos

- Por donde entra hoy: `/contabilidad/asientos` y `/contabilidad/mayor`. `GET asientos?soloActivos`, `PATCH asientos/:id/glosa`, `POST asientos/:id/anular`.
- Que deja el codigo hoy: el comprobante contabilizado no cambia montos; anular crea un asiento de reverso y marca `ANULADO`; el listado puede omitir anulados.
- Que pide la sala: glosa visible, un comentario aparte, descarga por defecto de activos, y PDF. Anular es CU-60.
- Depende de: CU-60 y CU-59.
- Datos: `Asiento.glosa` y `Asiento.estado` ya existen. No hay columna de comentario distinta de la glosa. PDF de asientos: punto de entrada no ubicado (busque un pdf de comprobante en contabilidad).

### CU-07. Factor de honorarios e IPC en parametrizacion

- Por donde entra hoy: `/catalogos/factor-honorarios` y `/contabilidad/honorarios`, `GET/POST/PUT factores-honorario`. El IPC de activo esta en `GET/PUT activo-fijo/ipc`, no en ese mantenedor.
- Que deja el codigo hoy: el factor guarda valor anterior, valor nuevo y vigencia. El IPC de activo es un valor por `periodoYm`.
- Que pide la sala: el factor consultable en parametrizacion, y el IPC con historial de valores.
- Depende de: ninguno. CU-30 es la boleta, no este parametro.
- Datos: `FactorHonorario` y `ActivoFijoIpc` ya existen. No hay un IPC general fuera de activo fijo.

### CU-08. Presupuesto por centro de costo

- Por donde entra hoy: `/presupuestos`. `GET/POST/PUT/DELETE presupuestos` en `contabilidad.controller.ts`. La pagina ya tiene exportar PDF.
- Que deja el codigo hoy: guarda anio, centro (texto), monto presupuestado y monto ejecutado digitado.
- Que pide la sala: ver la ejecucion anual del centro y poder imprimirla.
- Depende de: CU-15 y CU-16. CU-16 ya esta.
- Datos: `Presupuesto` ya existe, con `centroCosto` string y `montoEjecutado` manual. No hay relacion al `CentroCosto` ni una ejecucion calculada desde imputaciones.

### CU-09. Filtro de fechas en los libros

- Por donde entra hoy: `/contabilidad/mayor` (`LibroDiarioMayorPages.tsx`) y `GET mayor?periodo`. El balance y los estados ya filtran en su pagina.
- Que deja el codigo hoy: el mayor del back es de un periodo `aaaa-mm`. La pantalla, si hay desde y hasta, pide varios periodos y los junta en el cliente.
- Que pide la sala: filtro de fechas en el mayor. El balance de 8 y el ER no se rehacen (CU-27 y CU-13).
- Depende de: CU-13 y CU-27.
- Datos: `Asiento.fecha` y `Asiento.periodo` ya existen. El endpoint del mayor no recibe desde y hasta.

### CU-10. Cartola: moneda, banco, pesos, PDF, adjunto y semana

- Por donde entra hoy: `/tesoreria/cartolas` y el pago en `/tesoreria/pagos`. Carga en `tesoreria.service.ts`.
- Que deja el codigo hoy: la cartola identifica banco y moneda, el movimiento se contabiliza con asiento `CARTOLA`, y el pago ya guarda adjuntos. La carga, la semana y el no duplicar son CU-31 a CU-34.
- Que pide la sala: vista en pesos, PDF de la cartola, y el adjunto del pago cuando Lupe lo cierre. El adjunto no se disena de cero: el pago ya tiene lista de archivos.
- Depende de: CU-31 a CU-34.
- Datos: `CartolaBancaria`, `MovimientoCartola` y adjuntos del `Pago` (Json) ya existen. Una vista "en pesos" distinta del monto original: schema no revisado mas alla de `tipoCambio` en el movimiento de cartola.

### CU-11. Estado de cuenta por RUT a Excel

- Por donde entra hoy: `/tesoreria/cuentas-corrientes`. `GET cuentas-corrientes/por-rut` y `GET cuentas-corrientes/:terceroId/movimientos`.
- Que deja el codigo hoy: consulta movimientos del tercero por RUT.
- Que pide la sala: un Excel del RUT con anticipos y facturas, filtrado por cliente, proveedor o productor.
- Depende de: CU-12.
- Datos: `CuentaCorrienteMovimiento` ya existe. El productor es `Cliente.esProductor` o el mismo RUT en proveedor, no una entidad. Export Excel de esta consulta: punto de entrada no ubicado (busque export en `cuentas-corrientes`).

### CU-12. Ficha unica y listas separadas

- Por donde entra hoy: `/catalogos/proveedores`, `/catalogos/productores`, `/comercial/clientes`, modal `FichaContraparteModal.tsx`. `GET proveedores?esProductor`.
- Que deja el codigo hoy: cliente y proveedor son fichas distintas. Productores es un listado de proveedores con `esProductor`, y abre la misma ficha.
- Que pide la sala: listas separadas, contacto compartido si el RUT es el mismo, y marca cuando el RUT tiene mas de un rol. Sin maestro Productor.
- Depende de: ninguno.
- Datos: `Cliente`, `Proveedor` y `esProductor` ya existen, por separado. No hay una ficha unica ni un vinculo de RUT compartido entre las dos tablas.

### CU-13. Resultado del mes y acumulado al 31/12

sin cambio de integracion. `/contabilidad/estado-resultados` y `/contabilidad/situacion-financiera` (`EstadosFinancierosPage.tsx`). Cuentas de resultado en `Empresa.cuentaResultadoEjercicioCodigo` y `cuentaResultadoAcumuladoCodigo`.

### CU-14. Carga masiva: se rechaza la linea, no el archivo

- Por donde entra hoy: `/contabilidad/asientos`, `POST asientos/bulk` (`bulkCreateAsientos`).
- Que deja el codigo hoy: valida linea por linea, arma la lista de errores y graba las validas en una sola transaccion. Si la transaccion falla, no queda ninguna.
- Que pide la sala: las lineas buenas cargadas, las malas fuera, y un reporte con el conteo.
- Depende de: CU-15.
- Datos: el asiento y sus `lineas` Json ya existen. No hay tabla de reporte de rechazo.

### CU-15. La cuenta acepta N centros, N elementos y N areas

- Por donde entra hoy: `/catalogos/plan-cuentas`, `/catalogos/centros-costo`, `/catalogos/elementos-costo`, `/catalogos/areas-negocio`. El back reemplaza los vinculos en `contabilidad.service.ts`.
- Que deja el codigo hoy: la cuenta tiene tres listas (`CuentaCentroCosto`, `CuentaElementoCosto`, `CuentaAreaNegocio`). Elemento, area y centro devuelven `cuentasAsociadas`.
- Que pide la sala: poder agregar y quitar los N, ofrecer solo los ligados, y el contador al clic en el mantenedor inverso. El elemento no se amarra al centro.
- Depende de: ninguno.
- Datos: las tres tablas de vinculo ya existen, sin relacion elemento-centro. El contador ya sale en el listado de elemento, area y centro.

### CU-16. En la OC primero la cuenta, despues el centro y el elemento

sin cambio de integracion. `/compras/ordenes/nueva` (`OrdenCompraWizardPage.tsx`) y la linea de la OC en `compras.service.ts`.

### CU-17. PDF de la OC al proveedor sin dimensiones

- Por donde entra hoy: accion Imprimir de `/compras/ordenes`, funcion `printOc` en `ComprasPages.tsx`. No hay endpoint de PDF de OC.
- Que deja el codigo hoy: la impresion agrega el centro de costo al texto de la linea y puede listar la distribucion de centros en la observacion.
- Que pide la sala: la hoja que va al proveedor sin centro, sin elemento y sin cuenta.
- Depende de: CU-16.
- Datos: ninguno nuevo. La linea de la OC ya guarda cuenta, centro y elemento en el Json `lineas`.

### CU-18. Lupe baja la cartola del banco

sin cambio de integracion. `/tesoreria/cartolas`, importacion en `tesoreria.service.ts`. La regla de no duplicar y el periodo son CU-31 y CU-32.

### CU-19. La actividad manda, y la aprobacion esta en la proforma

- Por donde entra hoy: `/catalogos/contratista` (actividad y labor), `/contratistas/ingreso-diario`, `/contratistas/proformas`. Modelos `Actividad`, `Labor`, `LaborActividad`, `IngresoLaborDiario`, `ProformaContratista`.
- Que deja el codigo hoy: la labor se asocia a actividades, el ingreso diario se carga aparte, y la proforma tiene su propia cadena (`GrupoAprobacion.tipo` admite proforma).
- Que pide la sala: la actividad agrupa muchas labores, el ingreso diario no se aprueba uno a uno, y la aprobacion queda en la proforma. La OV sigue sin cadena.
- Depende de: CU-25.
- Datos: `LaborActividad` ya existe. `EstadoIngresoLabor` incluye `PENDIENTE_APROBACION`. La sala no pidio ese estado en el ingreso.

### CU-20. Al cierre entra solo el bloque aprobado

- Por donde entra hoy: `/contratistas/traspaso` y la grilla `/contratistas/proformas`.
- Que deja el codigo hoy: el traspaso arma el asiento con los ingresos de las proformas que el cierre ya eligio. La grilla de proformas se filtra por periodo en la pantalla.
- Que pide la sala: un bloque que entra al asiento y otro visible que no entra (borrador, sin aprobacion, ingreso suelto). La factura puede ser del mes siguiente.
- Depende de: CU-05 y CU-21.
- Datos: `ProformaContratista.estado` y `periodo` ya existen. No hay una marca de "solo informativo" distinta del estado.

### CU-21. Un asiento de centralizacion, y la factura cancela el puente

- Por donde entra hoy: el traspaso de contratistas (origen `TRASPASO-CTR:{periodo}`) y el libro `/compras/registro` al contabilizar el registro.
- Que deja el codigo hoy: centralizar genera el asiento del periodo contra facturas por recibir. Contabilizar la factura del libro exige OC en estado que opera, o la proforma asociada, y no repite el gasto si el puente ya se uso.
- Que pide la sala: un asiento del periodo, y la factura del libro dejando el puente en cero cuando calza.
- Depende de: CU-20, CU-26 y CU-42.
- Datos: `Asiento.origen` y `ProformaContratista.registroCompraId` ya existen. El auxiliar del puente es CU-26.

### CU-22. La correccion sale del documento, no de reabrir el mes

- Por donde entra hoy: la proforma, `SolicitudReversaEdicion` (`contratistas` y `POST contabilidad/solicitudes-reversa/:id/vb-contabilidad`). Pantalla `/contabilidad/reversas`.
- Que deja el codigo hoy: la correccion se pide desde la proforma, con motivo. El periodo contable no se reabre desde el traspaso.
- Que pide la sala: que la correccion nazca en el documento y el mes siga cerrado. El resultado sobre la linea es CU-59.
- Depende de: CU-38 y CU-59.
- Datos: `SolicitudReversaEdicion` ya existe. No se construye una cascada de meses.

### CU-23. Planta fuera, e historial antes / despues

- Por donde entra hoy: la cuenta en `/catalogos/plan-cuentas` (`requierePlanta`) y `GET historial/:entidad/:entidadId` (`historial.service.ts`).
- Que deja el codigo hoy: el flag de planta sigue en la cuenta. El historial guarda titulo, detalle, usuario y fecha.
- Que pide la sala: imputar sin planta, y ver valor anterior, valor nuevo, fecha y quien, sin nombres de campos.
- Depende de: ninguno.
- Datos: `CuentaContable.requierePlanta` sigue en el schema. `HistorialDocumento` no tiene valor anterior ni valor nuevo.

### CU-24. Ajuste en mes cerrado y reversa en mes abierto

No se integra. La regla que gana es CU-59.

### CU-25. Jose Tomas arma la proforma y contabilidad calza la factura

- Por donde entra hoy: `/contratistas/proformas` para armar y aprobar. La asociacion de la factura esta en el libro `/compras/registro` y en `ProformaContratista.registroCompraId`.
- Que deja el codigo hoy: la proforma recorre su cadena de contratistas. El registro de compra puede apuntar a la proforma. El aviso de calce es CU-41.
- Que pide la sala: abastecimiento arma y aprueba; contabilidad asocia solo cuando monto y RUT calzan.
- Depende de: CU-19 y CU-41.
- Datos: `aprobadoPorId`, `creadoPorId` y `registroCompraId` ya existen. No hay un permiso de sistema distinto para esos dos roles; la sala no dio el codigo.

### CU-26. El cierre agrupa por centro, y facturas por recibir lleva RUT

- Por donde entra hoy: el mismo traspaso de CU-21, en `contratistas.service.ts` (debitos agrupados por `centroCostoId`, credito con `auxiliar` = RUT).
- Que deja el codigo hoy: el asiento del periodo ya parte el gasto por centro y pone el RUT en la linea del puente.
- Que pide la sala: eso mismo, con el RUT como auxiliar y no como texto suelto de la glosa.
- Depende de: CU-21.
- Datos: el centro va en la linea del asiento (Json) y el auxiliar ya se escribe en esa linea. No hay columna `auxiliar` en `Asiento`.

### CU-27. Balance de 8 columnas

sin cambio de integracion. `/contabilidad/balance-8-columnas` (`Balance8ColumnasPage.tsx`) y `GET balance-8-columnas?periodo`.

### CU-28. Nota de cobro del embarcador y de Asoex

- Por donde entra hoy: `/compras/notas-cobro`. `NotasCobroController` y `notas-cobro.service.ts`, incluido `POST prevalidar-excel`.
- Que deja el codigo hoy: hay nota con lineas y nota con facturas asociadas (`NotaCobro`, `NotaCobroLinea`, `NotaCobroFactura`), y una prevalidacion de Excel.
- Que pide la sala: nota de gasto directo y nota de tercero calzada con sus facturas. La carga de muchas filas por proveedores es la parte que la sala pidio y el caso deja faltante.
- Depende de: ninguno.
- Datos: los tres modelos ya existen, con cuenta de gasto. El caso no pide otro documento.

### CU-29. La OC puede ser de activo fijo

- Por donde entra hoy: `/compras/ordenes/nueva`, combo tipo `ACTIVO_FIJO` en `OrdenCompraWizardPage.tsx`. Enum `TipoOrdenCompra`.
- Que deja el codigo hoy: la OC guarda el tipo. El maestro no se crea al elegir el tipo.
- Que pide la sala: la OC marcada como activo fijo, y el alta recien cuando este recepcionada (CU-58).
- Depende de: CU-58 para el alta. CU-04 no se construye.
- Datos: `OrdenCompra.tipo` ya tiene `ACTIVO_FIJO`. No acompana un `ordenCompraId` en `ActivoFijo`.

### CU-30. Boleta de honorarios: se registra, no se emite

- Por donde entra hoy: el libro `/compras/registro`, modal `RegistroBoletaHonorariosModal.tsx`, que llama `createRegistroCompra` con `tipoDte` HONORARIOS.
- Que deja el codigo hoy: el modal graba un registro de compra con tipo SII, rendicion y un nombre de archivo. No hay emision.
- Que pide la sala: una boleta recibida, asociada a quien la rindio, sin folio emitido por Almahue.
- Depende de: CU-07 para el factor, no para existir el registro.
- Datos: `RegistroCompra.tipoDteSii` ya existe. No hay modelo de boleta de honorarios. El factor es `FactorHonorario`.

### CU-31. La cartola del mes no duplica al recargarla

sin cambio de integracion. Carga de `/tesoreria/cartolas` en `tesoreria.service.ts`.

### CU-32. Linea del mes anterior, y archivo de otro periodo

sin cambio de integracion. La misma carga de cartola, `tesoreria.service.ts`.

### CU-33. Partir un ingreso en dos o tres codigos

sin cambio de integracion. Contabilizacion del ingreso en `/tesoreria/cartolas`, `tesoreria.service.ts`.

### CU-34. Nombre de la cuenta junto al numero

sin cambio de integracion. Cuenta bancaria de tesoreria, modelo `BancoCuenta`.

### CU-35. La devolucion usa el precio de la guia, no el promedio

- Por donde entra hoy: `/insumos/movimientos`, `POST movimientos-bodega` (`createMovimiento`). El precio de origen se resuelve para `DEVOLUCION`, `DEVOLUCION_NC` y `SALIDA_PROVEEDOR`.
- Que deja el codigo hoy: la salida a proveedor toma el precio de la guia o de la factura, y mueve stock.
- Que pide la sala: ese precio, y que el stock de la guia origen no se toque. Esa mitad es CU-56.
- Depende de: CU-56. El consumo a promedio es CU-55.
- Datos: `MovimientoBodega.precioUnitario` y `parId` ya existen. No hay un documento de devolucion distinto del movimiento.

### CU-36. Proyectado de tesoreria

No se integra en este corte. Espera de reunion con Lupe. No hay diseno. Punto de entrada no ubicado (busque proyectado). No bloquea la cartola.

### CU-37. No se reabre el periodo desde Traspaso

sin cambio de integracion. `/contratistas/traspaso`. La reapertura no esta en ese flujo. La solicitud sigue en la proforma (CU-38).

### CU-38. Motivo y dos vistos buenos, sin la clave al tiro

sin cambio de integracion. `SolicitudReversaEdicion` y `/contabilidad/reversas`. El efecto sobre la linea es CU-59.

### CU-39. Asiento de ajuste al cerrar la reversa

No se integra. La regla que gana es CU-59.

### CU-40. Proformas del periodo, y factura solo si hay vinculo

- Por donde entra hoy: `/contratistas/proformas` (`ProformasContratistaNivel1Page.tsx`).
- Que deja el codigo hoy: la grilla trabaja el periodo de la proforma. El vinculo a la factura es `registroCompraId` y `FacturaContratista`.
- Que pide la sala: no listar proformas de otro periodo, y mostrar el recuadro de factura solo si hay vinculo.
- Depende de: ninguno.
- Datos: `periodo`, `registroCompraId` y `FacturaContratista` ya existen. No hay un flag de "mostrar recuadro".

### CU-41. Una proforma con una factura, y avisos de calce

- Por donde entra hoy: asociacion en el libro y en la proforma. `ProformaRegistroCompra` permite N vinculos. Hay `ProformaNotificacionEvento` para el modal Notificar.
- Que deja el codigo hoy: una proforma puede quedar ligada a mas de un registro, y el aviso de notificar guarda si el correo salio.
- Que pide la sala: vinculo 1 a 1, cobertura que puede ser parcial sin campo porcentaje, aviso verde si calza, aviso al creador si no, y correo al asociar.
- Depende de: CU-25.
- Datos: `ProformaRegistroCompra` y `FacturaContratista.proformasGrupoIds` ya existen y admiten mas de una proforma. No hay estado "descuadrada" ni un acuse al creador distinto de `ProformaNotificacionEvento`.

### CU-42. Contabilizar la factura contra facturas por recibir

- Por donde entra hoy: `/compras/registro`. Contabilizar pasa por `assertOcParaRegistroCompra` / `ocPermiteContabilizarOPagar` en `oc-estado.util.ts`.
- Que deja el codigo hoy: sin OC en estado que opera no se contabiliza. La proforma entra como vinculo del registro. El boton de la pantalla depende de ese vinculo.
- Que pide la sala: el asiento contra el puente, y en la vista la cobertura, el filtro por proveedor y la etiqueta contabilizada o pendiente.
- Depende de: CU-21 y CU-41.
- Datos: `RegistroCompra.estado`, `ocId` y el vinculo de proforma ya existen. Cobertura parcial contra la proforma: no hay campo; el caso pide verla, no un porcentaje.

### CU-43. La hija nace por guia, y solo la ultima ajusta la madre

- Por donde entra hoy: el mismo `naceHijaPorGuia` de CU-02. La madre pasa a `RECEPCIONADA` si la guia la completa y no nace hija.
- Que deja el codigo hoy: cada guia que no cierra la madre crea una hija. No hay una marca de "ultima guia" ni un solo ajuste de la madre.
- Que pide la sala: hijas por guia, y un solo ajuste de la madre, en la ultima guia, por cantidad.
- Depende de: CU-02 y CU-47.
- Datos: cantidades en el Json `lineas` de la OC y de la hija. No hay campo porcentaje ni flag de ultima guia.

### CU-44. Quien tiene el modulo puede entrar al grupo

sin cambio de integracion. Buscador del grupo en `/admin/aprobaciones` (`WorkflowAprobacionesPage.tsx`) y `approval-engine.ts` (`allowedIds`). Quien administra es CU-49.

### CU-45. El organigrama es una vista

sin cambio de integracion. `/admin/organigrama` (`OrganigramaPage.tsx`), arbol por `Usuario.jefeId`. La cadena que corre con grupos activos es `resolveCadenaCompleta` en `approval-engine.ts`. CU-46 no se hace.

### CU-46. No armar la cadena de la OC desde el organigrama

No se integra en este corte. La sala lo rechazo. La cadena sigue en grupos y escalas (CU-50). El arbol queda en CU-45 y CU-61.

### CU-47. En la recepcion no se adivina el articulo por la guia

- Por donde entra hoy: `asociarGuiaDespacho` (`lineasUsuario.insumoId`) y `createGuiaInsumoRecibida` (`insumoId`, `lineaOrden`). Pantalla `/insumos/guias-recibidas`.
- Que deja el codigo hoy: si el usuario no manda articulo, la guia de despacho busca uno por codigo o nombre (`insumoDeLineaGuia`). La guia fisica exige el insumo y, si hace falta, la linea de la OC.
- Que pide la sala: cada linea apuntando a un articulo elegido del maestro, sin calce por el texto de la guia.
- Depende de: CU-57 para el stock. El calce automatico se apaga en la misma ola.
- Datos: `GuiaInsumoRecibida.insumoId` ya existe. `GuiaDespachoRecibida.lineas` es Json y no guarda el id del maestro hasta asociar.

### CU-48. AlmaWeb

No se integra en este corte. Es otro sistema. Punto de entrada no ubicado (busque AlmaWeb). No se mezclan sus usuarios con los roles del ERP.

### CU-49. El acceso es el rol, no un administrador por modulo

- Por donde entra hoy: `/admin/roles` para el acceso, y `/admin/administradores` para `AdminConcepto`.
- Que deja el codigo hoy: el rol define las pantallas. Sigue el mantenedor de administradores por modulo, con flag `esJefe` en insumos.
- Que pide la sala: sacar ese mantenedor de la operacion. El acceso queda en el rol. La jefatura no administra parametros ni arma la cadena por ese flag.
- Depende de: CU-44, que no se rompe.
- Datos: `AdminConcepto` y `Rol` ya existen. No hay un dato nuevo; se deja de usar el flag como acceso.

### CU-50. Los grupos son las areas

- Por donde entra hoy: `/admin/aprobaciones`, modelos `GrupoAprobacion` y `UsuarioGrupoAprobacion`.
- Que deja el codigo hoy: hay grupos por modulo, con miembros y un aprobador inicial. No hay un grupo por area de compra ni las dos gerencias repetidas en cada uno.
- Que pide la sala: un grupo por area que compra, con jefatura, gerencia de area y gerencia general, y tope propio.
- Depende de: CU-51, CU-52 y CU-53. CU-46 no se usa como atajo.
- Datos: `GrupoAprobacion.nombre` y `modulo` ya existen. No hay area del grupo ni un cargo en el miembro, salvo `esJefe` en `UsuarioGrupoAprobacion`.

### CU-51. Jefatura, gerencia de area y gerencia general

- Por donde entra hoy: la escala del grupo, `NodoEscalaAprobacion` y `buildCadenaDesdeGrupo` en `approval-engine.ts`. Envio de la OC en compras.
- Que deja el codigo hoy: la cadena es la que el grupo tenga configurada. El primer eslabon entra desde monto 0. Un `montoMax` null cierra la cadena en ese nodo.
- Que pide la sala: siempre jefatura, despues gerencia de area y despues gerencia general, sin saltar el primero y sin cadena en la OV.
- Depende de: CU-50. El tope de cada nivel es CU-53. El techo del ultimo es CU-52.
- Datos: la escala ya guarda usuario, `montoMax` y el nodo siguiente. No hay tres cargos fijos.

### CU-52. El ultimo eslabon tiene techo

- Por donde entra hoy: al armar la cadena, `eslabonCubreMonto` en `approval-engine.ts`, y el envio a aprobacion de la OC.
- Que deja el codigo hoy: si el ultimo nodo tiene `montoMax` null, cualquier monto cierra ahi y la OC entra a la bandeja.
- Que pide la sala: si la OC pasa el tope del ultimo, no se encola y hay mensaje de que excede el monto de gerencia.
- Depende de: CU-51 y CU-53. Se citan en circulo con CU-50 y quedan en la misma ola.
- Datos: `NodoEscalaAprobacion.montoMax` es un solo monto. No hay estado "no encolada por techo".

### CU-53. Tope por peso, dolar y yuan

- Por donde entra hoy: el mismo `montoMax` de la escala. La OC guarda `OrdenCompra.moneda`. Los indicadores del dia estan en `IndicadorBc` (`/catalogos/indicadores-bc`).
- Que deja el codigo hoy: un tope por eslabon, en un solo numero. La recepcion guarda `RecepcionOc.tcAplicado`. La OC no guarda un tipo de cambio propio.
- Que pide la sala: tope en CLP, USD y yuan, y al tipear pesos un tipo del dia editable que despues queda fijo.
- Depende de: CU-52. El `montoMax` actual es el punto de partida, no se borra.
- Datos: no hay tres topes ni tipo de cambio propuesto y guardado en la OC. `IndicadorBc` ya existe para el valor del dia.

### CU-54. La receta es de embalaje, no de un packing

- Por donde entra hoy: `/insumos/ordenes-aplicacion`, `POST recetas-packing` y `POST producciones-packing` en `packing.service.ts`.
- Que deja el codigo hoy: la receta puede guardarse sin packing (`packingId` null). La produccion exige un packing, una receta y cajas, y descuenta stock.
- Que pide la sala: receta de embalaje con centro de costo, sin packing obligatorio, y consumo con cantidad por packing. La crea la jefatura, sin cadena. El consumo si pasa por aprobacion; la sala no dijo cual cadena.
- Depende de: ninguno para guardar la receta. CU-55 precisa el precio en la ola siguiente. CU-64 no bloquea los campos ya dichos.
- Datos: `RecetaPacking.packingId` ya es opcional. `RecetaPackingLinea.cantidadPorCaja` ya existe. No hay centro de costo en la receta ni cantidad por packing en el consumo. `ProduccionPacking.packingId` es obligatorio.

### CU-55. El consumo va al promedio del mes

- Por donde entra hoy: la produccion de CU-54 usa `costoUnitario` de la linea o `Insumo.costoPromedio`. El movimiento de bodega recalcula el promedio al entrar y al salir.
- Que deja el codigo hoy: el costo sale del maestro en el momento del consumo. No hay una opcion FIFO en esa pantalla.
- Que pide la sala: el promedio del stock del mes, incluido el saldo anterior, sin consumir de la guia mas vieja a la mas nueva, y sin reescribir un mes ya consumido.
- Depende de: CU-54. No cambia CU-35 ni CU-56.
- Datos: `Insumo.costoPromedio` ya existe. No hay un promedio guardado por mes en el consumo.

### CU-56. La devolucion no le saca stock a la guia

- Por donde entra hoy: `/insumos/movimientos`, tipos `DEVOLUCION`, `DEVOLUCION_NC` y `SALIDA_PROVEEDOR`. La empresa tiene que tener `permiteDevolucionProveedor`.
- Que deja el codigo hoy: la devolucion mueve stock y puede quedar pareada con `parId`. El precio es el de CU-35.
- Que pide la sala: un documento nuevo, al precio de la guia, sin rebajar la existencia de esa guia, aunque esas unidades ya se hayan consumido.
- Depende de: CU-35.
- Datos: el movimiento y el precio ya existen. No hay documento de devolucion que no descuente la guia. `GuiaInsumoRecibida` no guarda un saldo propio distinto del movimiento.

### CU-57. El stock sube al confirmar, y la guia lleva adjunto

- Por donde entra hoy: `createGuiaInsumoRecibida` crea el movimiento `ENTRADA_PROVEEDOR` en estado `CONFIRMADO` y llama `applyTipoToStock` en el mismo paso. Los adjuntos de la guia manual estan en CU-01.
- Que deja el codigo hoy: registrar la guia fisica ya suma bodega. No hay un confirmar distinto del alta. `MovimientoBodega.estado` si tiene `BORRADOR` y `CONFIRMADO`, y la guia fisica no lo usa.
- Que pide la sala: stock en cero hasta confirmar, con el articulo del maestro ya elegido, y foto o archivo en la guia.
- Depende de: CU-01 para el adjunto que ya existe en la guia manual, y CU-47 para el articulo.
- Datos: `estado` del movimiento ya existe. `GuiaInsumoRecibida` no tiene adjuntos ni fecha de confirmacion. `GuiaDespachoRecibida.adjuntos` si.

### CU-58. El maestro de activo fijo nace de la OC recepcionada

- Por donde entra hoy: `/activo-fijo/ingreso`, `POST activo-fijo/activos`. El alta busca `registroCompraId` o una factura del libro (`activo-fijo.service.ts`, `GET activo-fijo/facturas`).
- Que deja el codigo hoy: el bien se crea contra la factura del libro, con vida util financiera en meses y vida tributaria en anios, y puede llevar centro de costo.
- Que pide la sala: crearlo solo desde una OC tipo activo fijo ya recepcionada, avisar si falta factura, sin centro de costo en el alta, y una sola vida util en meses.
- Depende de: CU-29. No depende de CU-04.
- Datos: `ActivoFijo.registroCompraId`, `vidaUtilMeses`, `vidaUtilTributariaAnios`, `centroCostoId` y `ActivoFijoIpc` ya existen. No hay `ordenCompraId` ni un listado de OC recepcionadas en el alta.

### CU-59. Corregir la proforma edita la linea

- Por donde entra hoy: la solicitud de CU-38 y CU-22. `recentralizarPeriodo` cierra la solicitud y guarda en el Json `reCierre` un texto de asiento, sin crear comprobante en ese metodo. Editar un asiento contabilizado esta en `PATCH asientos/:id`.
- Que deja el codigo hoy: la solicitud y los dos vistos buenos existen. Anular, en cambio, si crea un reverso (eso lo cambia CU-60). La linea del asiento de la proforma no se reescribe por esta correccion.
- Que pide la sala: guardar el valor nuevo en la linea que ya existe, con historial, sin asiento de ajuste ni de reversa, y el mayor solo con activos.
- Depende de: CU-38. Reemplaza a CU-24 y CU-39.
- Datos: `Asiento.lineas` es Json. `SolicitudReversaEdicion` ya guarda motivo y vistos buenos. No hay valor anterior y valor nuevo de la linea en el asiento.

### CU-60. Anular el asiento no lo borra

- Por donde entra hoy: `POST asientos/:id/anular` (`anularAsiento` > `aplicarAnulacionConReverso`). Pantalla `/contabilidad/asientos`.
- Que deja el codigo hoy: marca `ANULADO` y crea otro comprobante de reverso. El motivo va a la glosa del reverso. No hay solicitud a la jefatura.
- Que pide la sala: la fila queda, con motivo, fuera del mayor. Lo hace la jefatura, o un analista solicita y la jefatura aprueba. Sin tope de monto.
- Depende de: CU-59 para el filtro del mayor.
- Datos: `EstadoAsiento.ANULADO` ya existe. No hay motivo, solicitante ni quien anulo en `Asiento`.

### CU-61. Organigrama con cuatro titulos

- Por donde entra hoy: `/admin/organigrama`. El nivel del arbol pinta "Gerencia general", "Gerencia de area", "Jefatura" y "Analista" segun la profundidad, no segun un cargo del usuario.
- Que deja el codigo hoy: el arbol sale de `Usuario.jefeId` y muestra el rol. En la misma tarjeta puede verse el tope `montoMaxAprobacion`.
- Que pide la sala: los cuatro titulos, solo como vista, sin efecto en la OC y sin montos.
- Depende de: CU-45 y CU-46.
- Datos: `Usuario.jefeId` y `montoMaxAprobacion` ya existen. No hay un cargo de esos cuatro titulos en el usuario.

### CU-62. CAF y emision en GoSocket productivo

No se integra en este corte. Emision productiva fuera. Este paquete no emite DTE ni pide folios.

### CU-63. Reportes por jefatura

No se integra en este corte. Espera de reunion con la jefatura cuando el modulo este cerrado. El modulo `reporteria` existe y no es ese paquete. La ruta `reportes/*` redirige al inicio.

### CU-64. Excel de receta y orden de aplicacion real

No se integra en este corte. Falta el Excel y la orden real. No se agregan columnas. La pantalla que hoy hay es `/insumos/ordenes-aplicacion` y no se toca por este caso. Los campos que la sala si dijo quedan anotados en el caso, no en un modelo nuevo.

### CU-65. Cuentas que faltan en el cierre de bodega

No se integra en este corte. Falta el listado. Sin merma. El cierre que ya existe es CU-03 y no gana una cuenta por esta frase.

### CU-66. Packing COMEX externo

No se integra en este corte. Fuera del ERP. Punto de entrada no ubicado (busque packing COMEX). El `Packing` de insumos es el de la receta, no las cajas y pallets de COMEX.

## 4. Cierre

Modulos tocados: insumos, compras, contratistas, contabilidad, tesoreria, activo fijo, aprobaciones (grupos y escalas), admin (organigrama, roles, administradores por modulo) y ficha de contraparte.

Quedan sin cambio de integracion, ola D, 12 casos: CU-13, CU-16, CU-18, CU-27, CU-31, CU-32, CU-33, CU-34, CU-37, CU-38, CU-44, CU-45.

No se integran en este corte, 11 casos: CU-04, CU-24 y CU-39 (pisados; ganan CU-58 y CU-59), CU-46 (no hacer), CU-36, CU-63, CU-64 y CU-65 (espera), CU-48, CU-62 y CU-66 (fuera).

Entran en alguna ola, 43 casos:

- Ola A: 13. CU-01, CU-29, CU-35, CU-47, CU-50, CU-51, CU-52, CU-53, CU-54, CU-56, CU-57, CU-58, CU-59. De esos, CU-29 y CU-35 no agregan modulo.
- Ola B: 15. CU-02, CU-07, CU-09, CU-10, CU-12, CU-15, CU-17, CU-22, CU-23, CU-28, CU-40, CU-49, CU-55, CU-60, CU-61.
- Ola C: 15. CU-03, CU-05, CU-06, CU-08, CU-11, CU-14, CU-19, CU-20, CU-21, CU-25, CU-26, CU-30, CU-41, CU-42, CU-43.

12 + 11 + 43 = 66.
