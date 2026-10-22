# Plan de integracion: primer eslabon y aprobaciones de insumos

Fecha: 2026-10-16. Fuente de los casos: `casos-de-uso.md` (CU-01 a CU-05). Este documento dice donde encaja cada caso en el flujo que el ERP ya tiene. No redefine pantallas ni propone codigo.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`, API `http://localhost:3001/api/v1`.

La cadena de este paquete es grupos y escalas. `workflowConfig` sigue leyendose al armar la cadena de Compras: si una regla legacy calza el monto, el pool de la escala se cruza con los aprobadores de esa regla. Este plan no usa esa tabla ni la pantalla `workflows-admin`.

## Ancla: que hace el flujo hoy

Una sola cadena, modulo `Compras`, para la orden de servicio y para la orden de insumos. La pantalla de reglas es `/admin/aprobaciones` (`WorkflowAprobacionesPage`, titulo "Reglas de aprobacion"). El cambio de familia es "Ordenes de compra" y "Proformas". La vista es Niveles o Arbol. El panel Configurar tiene Grupos, Suplencias, Simulador, Administradores e Importar / Exportar. No hay familia Insumos.

| Entrada | Donde esta | Que deja |
|---|---|---|
| Armado de la cadena | `resolveCadenaCompleta` en `approval-engine.ts`, llamado desde `computeCadenaAprobacion` con modulo fijo `Compras`. Grupos, nodos, simulador y preview (`POST ordenes-compra/preview-cadena`) usan el mismo motor. | El primer eslabon entra aunque el monto este bajo su numero. El siguiente entra cuando el monto alcanza el "monto desde" de ese eslabon. Un monto chico no se aprueba solo en el grabado: `bajo_umbral` lanza error. |
| Orden nueva | Compras, `createOrden`. El wizard elige tipo Servicio o Insumos. Enviar manda `PENDIENTE_APROBACION`. Borrador no arma cadena. | Servicio y madre de insumos salen a la misma cadena de Compras y a la misma bandeja `/compras/aprobaciones`. La madre de insumos exige que quien graba sea `aprobadorInicialId` de un grupo OC de Compras. |
| Edicion de una OC ya `APROBADO` | Compras, `updateOrden`. La abre el creador o un administrador, en `/compras/ordenes/:id/editar`. | Cualquier cambio del total, para abajo o para arriba, rearma la cadena y vuelve a `PENDIENTE_APROBACION`. No esta atado al cierre y se puede repetir cada vez que la orden queda otra vez `APROBADO`. |
| Cierre de la madre de insumos | Insumos, `POST insumos/ordenes/:id/cierre`, `solicitarCierreMadreInsumos`. El boton "Cerrar por menos" esta en `/insumos/ordenes`. | Si lo recibido es menor que el neto, la madre baja a esa suma y vuelve a la cadena de Compras. Si lo recibido ya cubre el neto, marca `cerradaAt` y no rearma la cadena. No hay cierre que suba el monto. |
| Nacimiento de la hija | Insumos, `createGuiaInsumoRecibida` y `asociarGuiaDespacho`. Las dos llaman `crearOcHijaDeRecepcion`. | La hija nace `APROBADO`, numero `{madre}.{n}`, con `ocPadreId`, sin aprobador y sin cadena. La madre sigue `APROBADO`. Compras rechaza recepcionar una orden de insumos. |

El jefe que hoy puede crear la madre es el aprobador inicial del grupo de Compras. `UsuarioGrupoAprobacion` no tiene una marca de jefe. Si esa persona es el primer eslabon, el motor la salta (no hay autofirma) y el documento lo recibe el eslabon siguiente.

## CU-01. No hay aprobacion automatica: el primer eslabon parte desde cero y el siguiente sigue desde ahi

- Entra hoy: al enviar una OC (`createOrden` o `updateOrden` cuando rearma) y al previsualizar (`previewCadena`, simulador `POST aprobaciones/simular`). El monto de la cadena es el neto en CLP. El grupo es el del solicitante en modulo `Compras`.
- Deja hoy: el primer eslabon se agrega aunque el monto este bajo su "monto desde". Un documento de pocos pesos, si hay alguien que no sea el solicitante en ese primer puesto, entra ahi y no sube. El eslabon de arriba entra cuando el monto es mayor o igual al "monto desde" de ese eslabon, no cuando pasa el numero del anterior. Con el primero en 1.000.000 y el siguiente en 2.000.000, 1.500.000 se queda solo en el primero. Si la cadena queda vacia con motivo `bajo_umbral`, el grabado responde "No hay aprobacion automatica por monto" y no deja la orden `APROBADO`. El wizard, si el preview trae `bajo_umbral`, igual muestra "Confirmar sin aprobacion" y el texto de que la orden queda aprobada sin firma. El campo de la escala se llama "Monto desde" y la columna dice ">= monto".
- Pide la sala: no hay tramo que se apruebe solo. El primer integrante cubre desde cero hasta el monto que la empresa le configura. Cinco pesos entra a ese primer eslabon. El siguiente cubre desde ese monto hacia el suyo, sin un hueco en el que el documento se apruebe solo. Un monto que cabe en el primer tramo no recorre los de arriba. Ella no fijo el nombre ni el 500.000 del ejemplo. La misma regla vale para la cadena de insumos de CU-04. Este paquete no abre proforma.
- Depende de: ninguno. CU-02, CU-03 y CU-05 mandan la madre por la cadena que esta regla define. CU-04 la usa en el flujo de insumos.

## CU-02. La edicion del monto, para abajo o para arriba, pasa por aprobacion

- Entra hoy: `updateOrden` de una OC en estado `APROBADO`, desde el wizard de edicion. El total que se compara es neto mas IVA, salvo exento. El solicitante de la cadena nueva es `creadoPorId`.
- Deja hoy: si el total cambia, para abajo o para arriba, rearma la cadena de Compras y pasa a `PENDIENTE_APROBACION`. Si el total no cambia, sigue `APROBADO`. El panel del wizard dice otra cosa: "Si el total sube, la OC vuelve a aprobacion. Si baja o solo cambia el texto, sigue aprobada." La madre de insumos, mientras llegan guias, sigue `APROBADO`, asi que esta edicion sigue abierta y cada cambio de monto vuelve a la cadena. No es el cierre. Una recepcion parcial no pasa por `updateOrden`.
- Pide la sala: una edicion del monto de la madre, menor o mayor, pide aprobacion. No queda un atajo para el monto inferior. El momento de esa edicion es el de CU-03. Una recepcion parcial, con la madre todavia abierta, no es esta edicion.
- Depende de CU-03 para el momento, de CU-01 para como se recorre la cadena y de CU-05 porque el documento es la madre de insumos. El "Si" del 01/10 cubre solo la subida. La bajada la agrega el 14/10.

## CU-03. La madre se edita una sola vez, al cerrarla, y esa edicion pide la aprobacion

- Entra hoy: el cierre, por quien creo la madre, en `/insumos/ordenes` con "Cerrar por menos" (`POST insumos/ordenes/:id/cierre`). La edicion general de monto entra por el wizard, CU-02, y no exige que sea el cierre.
- Deja hoy: el boton aparece si la madre esta `APROBADO`, no tiene `cerradaAt`, el usuario es el creador y el pendiente es mayor a 1. Si lo recibido es menor que el neto, el neto baja a lo recibido, las lineas se prorratean y la madre vuelve a `PENDIENTE_APROBACION` por la cadena de Compras. Al terminar esa aprobacion sin otro cambio de monto, `updateOrden` escribe `cerradaAt`. Si lo recibido ya cubre el neto, cierra sin rearma la cadena. No hay una accion de cierre que suba el monto: subir pasa por `updateOrden` mientras la madre sigue `APROBADO`, las veces que el creador o un administrador la guarden. `solicitarCierreSaldoOc` de compras rechaza el tipo insumos y no es este camino.
- Pide la sala: una sola edicion, en el cierre, para dejar el monto en el que se cierra (menor o mayor, CU-02), y esa edicion entra a la cadena. No se reabre en cada correccion. Si solo llego una parte y la madre sigue abierta, esa diferencia no es la edicion y no vuelve a la cadena. El otro cambio, el que se pide a contabilidad, queda fuera de este paquete.
- Depende de CU-02 para que la baja y la suba pidan aprobacion, y de CU-01 para el recorrido. La recepcion con la madre abierta es el nacimiento de la hija de CU-05: esa hija no rearma la cadena.

## CU-04. Insumos tiene su flujo de aprobacion, distinto del de servicios

- Entra hoy: el tipo de la orden, en `createOrden` y `updateOrden`. Servicio y madre de insumos llaman el mismo `resolveCadenaAprobacion` con modulo `Compras`. La pantalla de reglas no separa los dos tipos: el cambio de familia es orden de compra o proforma.
- Deja hoy: los dos tipos comparten grupo, escala, simulador y bandeja. Lo que si cambia con el tipo es la operacion. Servicio se recepciona en compras, completa, una a una, y `naceHija` queda en falso. Insumos no se recepciona en compras: el mensaje dice que ahi nace la hija, en la guia. La madre de insumos no sale en el listado de compras. Compras lista el servicio y la hija de insumos que ya tiene guia. La madre se lista en `/insumos/ordenes`.
- Pide la sala: dos flujos. El de insumos no es el de servicios. La orden de servicio sigue siendo aprobacion y recepcion, una a una. La de insumos es la que llega por partes. La cadena de insumos usa la regla de CU-01: su primer eslabon parte desde cero. El cliente no dijo tab, arbol ni Administracion. El lugar que el usuario pidio para construir este flujo esta al final de este plan. No es otro caso.
- Depende de CU-01. CU-05 usa este flujo para decir quien genera la madre y que la hija no entra.

## CU-05. Se marca al jefe: la madre pasa por la cadena de insumos y la hija no

- Entra hoy: la madre, al crearla con tipo `INSUMOS` (`assertJefeCreaMadreInsumos`) y al enviarla a la cadena de Compras. La hija, al recepcionar la guia en insumos (`createGuiaInsumoRecibida` o `asociarGuiaDespacho`), las dos por `crearOcHijaDeRecepcion`.
- Deja hoy: puede crear la madre quien sea `aprobadorInicialId` de algun grupo OC activo de Compras. No hay una marca entre los integrantes. Esa persona, si es el primer eslabon, no firma su propia orden: el motor la salta y sigue el eslabon de arriba. La madre, al enviarla, queda `PENDIENTE_APROBACION` en la bandeja de compras. Puede volver a esa bandeja en cada edicion de monto (CU-02) y en el cierre por menos (CU-03). La hija nace `APROBADO`, sin filas de `aprobacionOc` y sin snapshot de cadena. El administrativo que recepciona queda como `creadoPorId` de la hija. La guia exige madre `APROBADO`, no cerrada, del mismo proveedor, y no pasa el saldo. La madre sigue en el listado de insumos. El "jefe de abastecimiento" del 01/10, el de la guia fisica, no es esta marca.
- Pide la sala: en el grupo de insumos se marca un integrante como jefe. Solo ese jefe puede generar la madre. La madre entra una vez a la cadena de CU-04. La hija no entra: la genera el administrativo con la guia. La madre vive en insumos. El cliente dijo "el jefe" y "La madre es el jefe". No uso los titulos "jefe de insumos" ni "jefe de bodega", ni dijo submenu.
- Depende de CU-04 para el flujo y de CU-01 para el primer eslabon de esa cadena. La unica vuelta posterior que la sala pidio es la edicion del cierre (CU-03), y solo si ese cierre cambia el monto (CU-02). Una guia con la madre abierta no es esa vuelta.

## Lugar que el usuario pidio para CU-04 y CU-05

El cliente confirmo dos flujos, un jefe marcado, la madre en la cadena y la hija fuera. El usuario, al encargar este paquete, pidio construir eso en un tab nuevo llamado Insumos, en Administracion > Aprobaciones, con el arbol, y una marca de jefe de area entre los integrantes.

Ese tab es el lugar de CU-04 y CU-05. No es un sexto caso. El caso de uso dejo la palabra "tab" en la seccion 3 porque el cliente no la dijo, ni dijo arbol ni Administracion.

Hoy esa pantalla no tiene el tab. El arbol que existe es la vista Arbol de la familia "Ordenes de compra" (y la de Proformas, que este paquete no abre). La marca de jefe no existe en los integrantes: el permiso de crear la madre lee el aprobador inicial del grupo de Compras.

## Dependencias

```
CU-01 primer eslabon desde cero, el siguiente desde ese monto
    > CU-04 flujo de insumos, distinto del de servicios, con la misma regla
        > CU-05 jefe marcado genera la madre; la madre entra a esa cadena; la hija no
            > CU-03 la unica edicion posterior es al cerrar
                > CU-02 esa edicion, para abajo o para arriba, pide aprobacion
```

La guia con la madre abierta nace hija y no vuelve a CU-02. Proformas, libro, contabilizacion de la hija y quien ve cada documento quedan fuera de este paquete.

## Modulos Nest y carpetas React

Nest, en `ERP/erp_back/src`:

- `modules/aprobaciones`: `approval-engine.ts`, `aprobacion-cadena.util.ts`
- `modules/admin`: grupos, escalas, simulador, importacion
- `modules/compras`: `createOrden`, `updateOrden`, `computeCadenaAprobacion`, bandeja `aprobaciones-oc`, `solicitarCierreMadreInsumos`, `oc-madre-hija.util.ts`
- `modules/insumos`: `createGuiaInsumoRecibida`, `asociarGuiaDespacho`, `getOrdenesInsumos`, `POST insumos/ordenes/:id/cierre`

React, en `ERP/erp_front/src`:

- `features/admin/WorkflowAprobacionesPage.tsx`
- `components/aprobaciones` (arbol, niveles, flujo de la cadena)
- `features/compras/OrdenCompraWizardPage.tsx` y `compras-oc-helpers.ts`
- `features/compras` bandeja `/compras/aprobaciones`
- `features/insumos/OrdenesInsumosPage.tsx`
- `features/insumos/GuiasInsumosRecibidasPage.tsx`
