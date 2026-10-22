# Plan de pruebas: primer eslabon y aprobaciones de insumos

Fecha: 2026-10-16. Casos: `casos-de-uso.md` (CU-01 a CU-05). Encaje de hoy: `plan-integracion.md`.

Este plan no se ejecuta en esta redaccion. No se implementa codigo y no se hace commit.

Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`. API `http://localhost:3001/api/v1`.

Quien lo corra despues no emite DTE, no llama al SII, no dispara un evento a GoSocket, no paga, no cierra el mes y no corre `prisma migrate deploy`. No guarda, no contabiliza y no paga un documento para sacar una foto. No pulsa Enviar a aprobacion, Guardar cambios, Cerrar por menos ni una recepcion de guia.

Hay 5 pruebas, P-01 a P-05. Una por caso. Los limites que la sala si dijo van dentro de esas pruebas y no se numeran aparte.

## Como se lee un resultado

Pasa solo la columna Resultado esperado (sala).

El codigo de salida de un spec no es el veredicto. Un verde que afirma el atajo de hoy se anota en Resultado de hoy. Ese verde no acredita el caso.

Los spec nombrados son de unidad, con fixture en memoria. Correrlos no graba una OC de ALMAHUE EXPORT SPA. Si una lectura necesitara mutar una OC real, queda como lectura de codigo o de pantalla ya abierta, y no se guarda.

Si la pantalla no carga o el stack no responde, el resultado es bloqueo de ambiente. No se migra para fabricar el dato.

La pantalla, cuando este plan la pide, se abre con Playwright. No se usa el navegador interno. No se achica el viewport: la captura es la ventana completa, con menu, contenido y paneles laterales.

## Limites que la sala dijo

Van dentro de P-01 a P-05. No son P-06.

| Limite | Prueba |
|---|---|
| Monto de 5 pesos entra al primer eslabon | P-01 |
| El segundo eslabon no firma lo chico | P-01 |
| La edicion es solo al cierre | P-03 |
| Una recepcion parcial, con la madre abierta, no vuelve a la cadena | P-03 |
| La hija no entra a la cadena | P-05 |
| Hoy hay un solo flujo | P-04, columna de hoy |

Lo que el caso de uso dejo fuera no es prueba. Un pase de P-01 a P-05 no lo cierra.

- "desde monto $1". Ella dijo desde cero y 5 pesos. El piso de la prueba es 5.
- Tab Insumos, arbol y Administracion. El cliente no uso esas palabras. El flujo aparte es P-04. El lugar pedido para construirlo se mira ahi, y no es otro caso.
- "jefe de insumos", "jefe de bodega" y un submenu. El cliente dijo "el jefe" y "La madre es el jefe". La marca es P-05.
- Proformas, centralizacion, cierre de mes, contratistas, libro de compras, contabilizacion de la hija, quien ve cada documento, reportes y estado de resultados.
- "jefe de abastecimiento" del 01/10. Controla la guia fisica. No es la marca de P-05.
- "pedir el municipal". No se entiende y no arma prueba.
- `workflowConfig` y `workflows-admin`. Este paquete no los usa.

## Indice

| ID | CU | Que se hace |
|---|---|---|
| P-01 | CU-01 | Ver si 5 pesos entra al primero y el segundo no lo firma |
| P-02 | CU-02 | Ver la edicion del monto, para abajo y para arriba |
| P-03 | CU-03 | Ver la edicion unica al cierre, y la recepcion parcial |
| P-04 | CU-04 | Ver si insumos y servicios tienen flujos distintos |
| P-05 | CU-05 | Ver la marca de jefe, la madre en la cadena y la hija fuera |

## P-01. Cinco pesos entra al primero, y el segundo no firma lo chico

- CU: CU-01. La misma regla la usa la cadena de insumos de P-04. Este paquete no abre proforma.
- Que se hace: Jest en `ERP/erp_back`, `src/modules/aprobaciones/approval-engine.spec.ts`, `resolveCadenaCompleta`. El fixture del describe de grupos ya tiene el grupo G1: A con tope 1.000.000, C con tope 2.000.000, D cierra. Correr los `it` ya escritos y anotarlos en la columna de hoy. Sobre ese mismo fixture, sin persistir un spec nuevo y sin grabar una OC, resolver monto 5 con solicitante Ana (no es A) y monto 5 con solicitante A. Lectura de codigo, sin confirmar el wizard: `OrdenCompraWizardPage.tsx` (boton y parrafo de `bajo_umbral`), `compras-oc-helpers.ts` (`ocCadenaPuedeEnviar`) y `ApprovalChainVisual.tsx` (texto de "No pide aprobacion" y etiqueta "Desde").
- Resultado de hoy: el primer eslabon se agrega aunque el monto este bajo su numero. Ana con 800.000 queda solo en A. Un monto de 5 con Ana recorre ese camino: entra a A y no sube a C. El siguiente entra cuando el monto es mayor o igual a su propio "monto desde", no cuando supera el numero del anterior. Ana con 1.500.000 queda solo en A, porque C parte en 2.000.000. Si el solicitante es el primer eslabon, el motor lo salta y sigue el de arriba: A con 800.000, y el mismo camino con 5, queda solo en C. El segundo firma lo chico. Si la cadena queda vacia con `bajo_umbral`, el grabado responde "No hay aprobacion automatica por monto" y no deja la orden `APROBADO`. El wizard igual muestra "Confirmar sin aprobacion" y el texto de que la orden queda aprobada sin firma. El campo de la escala es "Monto desde" y la etiqueta del nodo es "Desde {monto}".
- Resultado esperado (sala): no hay tramo que se apruebe solo. El primer integrante cubre desde cero hasta el monto que la empresa le configura. Cinco pesos entra a ese primer eslabon. El siguiente cubre desde ese monto hacia el suyo, sin un hueco en el que el documento se apruebe solo. En el fixture, 1.500.000 ya supero el tope de A y tiene que llegar a C. Un monto que cabe en el primer tramo no recorre los de arriba: 5 pesos no lo firma C, tampoco cuando el solicitante es A. Ella no fijo el nombre ni el 500.000. Los topes los configura la empresa.
- Cuando pasa: el monto 5 entra solo al primer eslabon, el segundo no firma ese 5, y el monto que ya paso el tope del primero entra al siguiente. Las tres lecturas juntas. Un verde de los `it` actuales no alcanza.
- No acredita: "Ana $800k entra al primer eslabon aunque este bajo su piso". "Ana $1.5M pide solo el primer escalon". "jefa de area (A) bajo su piso no se aprueba sola: sigue el eslabon siguiente". El comentario del motor "El primer eslabon parte en 0". El boton "Confirmar sin aprobacion". `ocCadenaPuedeEnviar` con `bajo_umbral` en verdadero.

## P-02. La edicion del monto, para abajo o para arriba, pide aprobacion

- CU: CU-02. El momento es P-03. El recorrido de la cadena es P-01. El documento es la madre de insumos de P-05.
- Que se hace: lectura de codigo de `updateOrden` en compras y del parrafo del wizard en `OrdenCompraWizardPage.tsx` cuando la OC ya esta `APROBADO`. No guardar una OC real. No pulsar Guardar cambios. Si una OC aprobada ya esta abierta en pantalla, se lee y no se guarda.
- Resultado de hoy: si el total cambia, para abajo o para arriba, rearma la cadena de Compras y pasa a `PENDIENTE_APROBACION`. Si el total no cambia, sigue `APROBADO`. El panel dice otra cosa: "Si el total sube, la OC vuelve a aprobacion. Si baja o solo cambia el texto, sigue aprobada." La madre de insumos, mientras llegan guias, sigue `APROBADO`, asi que esta edicion sigue abierta y cada cambio de monto vuelve a la cadena. No es el cierre. Una recepcion parcial no pasa por `updateOrden`.
- Resultado esperado (sala): una edicion del monto de la madre, menor o mayor, pide aprobacion. No queda un atajo para el monto inferior. El momento de esa edicion es el cierre de P-03, una sola vez. Una recepcion parcial, con la madre todavia abierta, no es esta edicion. El "Si" del 01/10 cubre solo la subida. La bajada la agrega el 14/10.
- Cuando pasa: bajar y subir piden aprobacion, no hay un camino en el que el monto menor siga aprobado, y esa edicion ocurre solo al cierre. El rearme de `updateOrden` sobre cualquier OC `APROBADO` no alcanza.
- No acredita: el `it` de `oc-parcial.compras.service.spec.ts` "P-09 bajar el monto de una madre APROBADO vuelve a aprobacion". Ese verde es el atajo de hoy. El texto del panel, que deja la baja aprobada, tampoco es la sala: la sala pide aprobacion tambien para la baja.

## P-03. La madre se edita una sola vez, al cerrarla

- CU: CU-03. La baja y la suba son P-02. El recorrido es P-01. La recepcion con la madre abierta es el nacimiento de la hija de P-05.
- Que se hace: lectura de codigo de `solicitarCierreMadreInsumos` (`POST insumos/ordenes/:id/cierre`) y del boton "Cerrar por menos" en `OrdenesInsumosPage.tsx`. No pulsar el boton. No cerrar una madre real. La recepcion parcial se lee en `crearOcHijaDeRecepcion` y en el `it` de `insumos.service.spec.ts` "al recepcionar la guia contra la madre nace una hija APROBADA por el parcial", sin recepcionar una guia real. `solicitarCierreSaldoOc` de compras rechaza el tipo insumos: no ejecutarlo. No es este camino.
- Resultado de hoy: el boton aparece si la madre esta `APROBADO`, no tiene `cerradaAt`, el usuario es el creador y el pendiente es mayor a 1. Si lo recibido es menor que el neto, el neto baja a lo recibido, las lineas se prorratean y la madre vuelve a `PENDIENTE_APROBACION` por la cadena de Compras. Al terminar esa aprobacion sin otro cambio de monto, `updateOrden` escribe `cerradaAt`. Si lo recibido ya cubre el neto, cierra sin rearma la cadena. No hay un cierre que suba el monto: subir pasa por `updateOrden` mientras la madre sigue `APROBADO`, las veces que el creador o un administrador la guarden. La recepcion parcial no rearma la cadena: la madre sigue `APROBADO`.
- Resultado esperado (sala): una sola edicion, en el cierre, para dejar el monto en el que se cierra (menor o mayor), y esa edicion entra a la cadena. No se reabre en cada correccion. Si solo llego una parte y la madre sigue abierta, esa diferencia no es la edicion y no vuelve a la cadena. El otro cambio, el que se pide a contabilidad, queda fuera de este paquete.
- Cuando pasa: la unica edicion posterior es el cierre, sirve para bajar y para subir, entra a la cadena, y una recepcion parcial con la madre abierta no la devuelve. Que la recepcion parcial ya deje la madre `APROBADO` no acredita el cierre unico ni la suba en ese cierre.
- No acredita: "Cerrar por menos" solo cuando lo recibido es menor. `updateOrden` para subir, repetible en cada `APROBADO`. `solicitarCierreSaldoOc`.

## P-04. Insumos tiene su flujo, distinto del de servicios

- CU: CU-04. Usa la regla de P-01. P-05 dice quien genera la madre en este flujo.
- Que se hace: Playwright en `http://localhost:5174/admin/aprobaciones`, sesion local de ALMAHUE EXPORT SPA. No achicar la ventana. Mirar el cambio de familia (`data-familia-aprobacion`): los botones son "Ordenes de compra" y "Proformas". No crear un grupo, no guardar, no importar. Ademas, lectura de `createOrden` y `updateOrden`: servicio y madre de insumos llaman `resolveCadenaAprobacion` con modulo `Compras`. Si la pantalla no carga, el resultado es bloqueo de ambiente.
- Resultado de hoy: un solo flujo. Los dos tipos comparten grupo, escala, simulador y bandeja `/compras/aprobaciones`. La pantalla no separa insumos: la familia es orden de compra o proforma. No hay familia Insumos. Lo que si cambia con el tipo es la operacion. Servicio se recepciona en compras, completa, una a una, y `naceHija` queda en falso. Insumos no se recepciona en compras: ahi nace la hija, en la guia. La madre de insumos no sale en el listado de compras. Compras lista el servicio y la hija de insumos que ya tiene guia. La madre se lista en `/insumos/ordenes`.
- Resultado esperado (sala): dos flujos. El de insumos no es el de servicios. La orden de servicio sigue siendo aprobacion y recepcion, una a una. La de insumos es la que llega por partes. La cadena de insumos usa la regla de P-01: su primer eslabon parte desde cero. El cliente no dijo tab, arbol ni Administracion. El lugar pedido para construir este flujo es un tab Insumos en esa pantalla, con el arbol. Hoy esa pantalla no tiene el tab. No es un sexto caso. Proformas no se abre.
- Cuando pasa: insumos tiene una cadena de aprobacion distinta de la de servicios, y el primer eslabon de esa cadena parte desde cero. Ver los dos botones de hoy, o ver que la guia y la recepcion de compras operan distinto, no alcanza.
- No acredita: compartir el modulo `Compras` y distinguir solo la recepcion. El boton Proformas no es el flujo de insumos.

## P-05. Se marca al jefe: la madre entra una vez y la hija no

- CU: CU-05. El flujo es P-04. El primer eslabon es P-01. La unica vuelta posterior que la sala pidio es el cierre de P-03, y solo si ese cierre cambia el monto (P-02).
- Que se hace: lectura de codigo de `assertJefeCreaMadreInsumos` y de `crearOcHijaDeRecepcion` (`createGuiaInsumoRecibida` y `asociarGuiaDespacho`). El `it` de `insumos.service.spec.ts` "al recepcionar la guia contra la madre nace una hija APROBADA por el parcial" se lee como columna de hoy. No crear una madre real. No recepcionar una guia. No enviar a la bandeja. En la pantalla de P-04, si ya esta abierta, mirar si un integrante tiene marca de jefe. No guardar. `UsuarioGrupoAprobacion` no tiene esa marca: se lee el modelo, no se migra.
- Resultado de hoy: puede crear la madre quien sea `aprobadorInicialId` de algun grupo OC activo de Compras. No hay una marca entre los integrantes. Esa persona, si es el primer eslabon, no firma su propia orden: el motor la salta y sigue el eslabon de arriba (el monto 5 con solicitante A, en P-01). La madre, al enviarla, queda `PENDIENTE_APROBACION` en la bandeja de compras. Puede volver a esa bandeja en cada edicion de monto y en el cierre por menos. La hija nace `APROBADO`, sin filas de `aprobacionOc` y sin snapshot de cadena. El administrativo que recepciona queda como `creadoPorId` de la hija. La guia exige madre `APROBADO`, no cerrada, del mismo proveedor, y no pasa el saldo. La madre sigue en el listado de insumos. El "jefe de abastecimiento" del 01/10 no es esta marca.
- Resultado esperado (sala): en el grupo de insumos se marca un integrante como jefe. Solo ese jefe puede generar la madre. La madre entra una vez a la cadena de insumos. La hija no entra: la genera el administrativo con la guia. La madre vive en insumos. El cliente dijo "el jefe" y "La madre es el jefe". No uso "jefe de insumos" ni "jefe de bodega", ni dijo submenu.
- Cuando pasa: existe la marca en el grupo de insumos, solo ese jefe crea la madre, la madre entra una vez a esa cadena, y la hija no entra. Las cuatro juntas.
- No acredita: la hija `APROBADO`, sin filas de `aprobacionOc`, mientras el permiso de crear la madre sea el aprobador inicial de Compras y la madre pueda volver a la bandeja. Ese nacimiento es el limite "la hija no entra", y no cierra la marca de jefe ni la entrada unica.
