# Resultados de pruebas: primer eslabon y aprobaciones de insumos

Fecha: 2026-10-16. Lectura: `plan-pruebas.md` (P-01 a P-05), `contraste-codigo.md`, `casos-de-uso.md`.

No se guardo, no se contabilizo y no se pago ninguna orden. No se pulso Enviar a aprobacion, Guardar cambios, Cerrar por menos ni una recepcion. No se emitio DTE, no se llamo al SII, no se pago, no se cerro el mes y no se corrio `prisma migrate deploy`. No se persistio un spec nuevo.

Un PASA es solo el resultado esperado de la sala (Maria Jesus, 14/10, y el tramo del 01/10 que el caso ya cito). Un verde que afirma el atajo de hoy no acredita el caso.

## 1. Que se corrio

Directorio de Jest: `E:\source\repos\Almahue\ERP\erp_back`.

```
npx jest --runInBand src/modules/aprobaciones/approval-engine.spec.ts --verbose --no-coverage
```

```
PASS src/modules/aprobaciones/approval-engine.spec.ts
Test Suites: 1 passed, 1 total
Tests:       29 passed, 29 total
Time:        19.284 s
```

Esos 29 verdes afirman el motor de hoy. En el describe de grupos, el fixture es G1: A con 1.000.000, C con 2.000.000, D cierra. Los `it` que el plan dejo fuera del pase salieron verdes y fijan el atajo:

- "Ana $800k entra al primer eslabon aunque este bajo su piso": cadena `U-A`.
- "Ana $1.5M pide solo el primer escalon": cadena `U-A`.
- "jefa de area (A) bajo su piso no se aprueba sola: sigue el eslabon siguiente": cadena `U-C`.

Sobre el mismo fixture, sin grabar un spec y sin grabar una OC, `resolveCadenaCompleta` con modulo Compras:

| Solicitante | Monto | Status | Cadena |
|---|---|---|---|
| Ana (`U-ANA`) | 5 | ok | `U-A` |
| A (`U-A`) | 5 | ok | `U-C` |
| Ana | 1.500.000 | ok | `U-A` |
| A | 1.500.000 | ok | `U-C` |

```
npx jest --runInBand src/modules/insumos/insumos.service.spec.ts --testNamePattern="al recepcionar la guia contra la madre nace una hija" --verbose --no-coverage
```

```
PASS src/modules/insumos/insumos.service.spec.ts
Tests: 13 skipped, 1 passed, 14 total
Time:  11.794 s
```

El `it` verde es "al recepcionar la guia contra la madre nace una hija APROBADA por el parcial". Es fixture en memoria. No se recepciono una guia real. Afirma la hija de hoy, no el cierre unico ni la marca de jefe.

Pantalla: el front `http://localhost:5174` respondio 200. La API `http://localhost:3001/api/v1/health` respondio 200 con `"db":"error"` y `"status":"degraded"`. Playwright abrio `http://localhost:5174/admin/aprobaciones` y cayo en `/login`. Entrar con `admin@almahue.local` dejo la pagina en el login. La consola del navegador y `POST /api/v1/auth/login` devolvieron 500, `Internal server error`. No se creo un grupo, no se guardo y no se importo. La familia en vivo no se pudo mirar. Eso es bloqueo de ambiente de la sesion, no el veredicto de P-04 ni de P-05: esas dos se leen en el fuente que el plan nombra.

## 2. P-01 a P-05

### P-01. Cinco pesos entra al primero, y el segundo no firma lo chico

- CU: CU-01.
- Que se corrio: el spec `approval-engine.spec.ts` (29 verdes) y la resolucion de monto 5 y de 1.500.000 sobre el fixture G1. Lectura, sin confirmar el wizard, de `OrdenCompraWizardPage.tsx`, `compras-oc-helpers.ts` (`ocCadenaPuedeEnviar`) y `ApprovalChainVisual.tsx`.
- Evidencia: Ana con 5 queda solo en A, y C no entra. A con 5 queda solo en C: el motor salta al solicitante y el siguiente entra como primer puesto, sin mirar su numero. Ana con 1.500.000 queda solo en A; C no entra porque su numero es 2.000.000. `ocCadenaPuedeEnviar` devuelve verdadero con `bajo_umbral`. El boton dice "Confirmar sin aprobacion". El parrafo dice que al confirmar la OC queda aprobada sin pedir firma. La etiqueta del nodo es "Desde" mas el monto. Con `bajo_umbral` el flujo dice "El monto no alcanza el primer escalon. No pide aprobacion." El campo del formulario es "Monto desde (vacio = cierra la cadena)".
- Sala: las tres lecturas juntas. Ana con 5 si entra solo al primero. El 5 con solicitante A lo firma C. 1.500.000 no llega al eslabon de 2.000.000. El verde de los `it` actuales afirma ese atajo.
- Veredicto: PARCIAL.

### P-02. La edicion del monto, para abajo o para arriba, pide aprobacion

- CU: CU-02.
- Que se corrio: lectura de `updateOrden` y del parrafo de OC aprobada en `OrdenCompraWizardPage.tsx`. No se guardo una OC. No se pulso Guardar cambios. No se corrio el `it` de `oc-parcial.compras.service.spec.ts`: el plan dice que ese verde no acredita.
- Evidencia: si el total de una OC `APROBADO` cambia, para abajo o para arriba, `montoCambia` rearma la cadena de Compras y el estado queda `PENDIENTE_APROBACION`. Si el total no cambia, sigue `APROBADO`. No exige que sea el cierre. Cada cambio de monto borra `cerradaAt`. El panel dice: "Si el total sube, la OC vuelve a aprobacion. Si baja o solo cambia el texto, sigue aprobada."
- Sala: bajar y subir piden aprobacion, no queda un camino en el que el monto menor siga aprobado, y esa edicion ocurre solo al cierre. El rearme sobre cualquier OC `APROBADO` hace las dos direcciones y deja la edicion abierta. El panel describe la baja como aprobada.
- Veredicto: PARCIAL.

### P-03. La madre se edita una sola vez, al cerrarla

- CU: CU-03.
- Que se corrio: lectura de `solicitarCierreMadreInsumos` y del boton "Cerrar por menos" en `OrdenesInsumosPage.tsx`. No se pulso el boton y no se cerro una madre. La recepcion parcial se leyo en `crearOcHijaDeRecepcion` y en el `it` verde de la hija. `solicitarCierreSaldoOc` rechaza el tipo insumos y manda a pedirlo en insumos; no se ejecuto.
- Evidencia: el boton aparece si la fila es madre, `APROBADO`, sin `cerradaAt`, el usuario es el creador y el pendiente es mayor a 1. Si lo recibido ya cubre el neto, escribe `cerradaAt` y no rearma. Si es menor, baja el neto a lo recibido, prorratea lineas y vuelve a `PENDIENTE_APROBACION` por la cadena de Compras. No hay un cierre que suba el monto. Subir pasa por `updateOrden` mientras la madre sigue `APROBADO`. El `it` verde crea la hija `APROBADO`, neto 2000, `ocPadreId` de la madre y `creadoPorId` del administrativo. `crearOcHijaDeRecepcion` no cambia el estado de la madre y no escribe filas de `aprobacionOc`.
- Sala: la unica edicion posterior es el cierre, sirve para bajar y para subir, entra a la cadena, y una recepcion parcial con la madre abierta no la devuelve. La recepcion parcial ya deja la madre como estaba. Eso no acredita el cierre unico ni la suba en ese cierre.
- Veredicto: PARCIAL.

### P-04. Insumos tiene su flujo, distinto del de servicios

- CU: CU-04.
- Que se corrio: Playwright en `http://localhost:5174/admin/aprobaciones`, sin achicar la ventana. La sesion no entro: login 500 y health con `db: error`. Bloqueo de ambiente de la foto. La lectura que el plan pide si se hizo: `data-familia-aprobacion` en `WorkflowAprobacionesPage.tsx`, y `createOrden` / `updateOrden` / `computeCadenaAprobacion`.
- Evidencia: el bloque de familia tiene dos botones, "Ordenes de compra" y "Proformas". La columna Tipo rotula "Proformas" u "Ordenes de compra". No hay familia Insumos. `computeCadenaAprobacion` fija `modulo: 'Compras'`. Servicio y madre de insumos, al enviar, llaman `resolveCadenaAprobacion`. `createRecepcion` rechaza el tipo insumos y manda a la guia, donde nace la hija. Ver esos dos botones, o ver que la guia y la recepcion de compras operan distinto, no alcanza: la cadena de insumos no esta.
- Sala: insumos tiene una cadena distinta de la de servicios, y el primer eslabon de esa cadena parte desde cero.
- Veredicto: FALLA.

### P-05. Se marca al jefe: la madre entra una vez y la hija no

- CU: CU-05.
- Que se corrio: lectura de `assertJefeCreaMadreInsumos`, de `crearOcHijaDeRecepcion` y del modelo `UsuarioGrupoAprobacion`. El `it` verde de la hija se toma como columna de hoy. No se creo una madre, no se recepciono una guia y no se envio a la bandeja. La pantalla de P-04 no quedo abierta, asi que no se miro un integrante en vivo. No se migro.
- Evidencia: puede crear la madre quien sea `aprobadorInicialId` de un grupo OC activo con modulo Compras. El mensaje dice "jefe del grupo de compras". `UsuarioGrupoAprobacion` es `usuarioId` y `grupoId`. `TipoGrupoAprobacion` es `OC` y `PROFORMA`. En el fuente de la pantalla las columnas del grupo son "Aprobador inicial" y "Miembros". La hija nace `APROBADO`, sin filas de `aprobacionOc` y sin snapshot de cadena. La madre, al enviarla, puede quedar `PENDIENTE_APROBACION` y volver a esa bandeja en cada cambio de monto y en el cierre por menos. `getOrdenes` de compras lista el servicio y la hija de insumos que ya tiene guia. `getOrdenesInsumos` lista madre e hija en insumos.
- Sala: las cuatro juntas. Existe la marca en el grupo de insumos, solo ese jefe crea la madre, la madre entra una vez a esa cadena, y la hija no entra. La hija `APROBADO` es el limite "la hija no entra". No cierra la marca ni la entrada unica.
- Veredicto: PARCIAL.

## 3. Recuento

| Veredicto | Pruebas | Cantidad |
|---|---|---|
| PASA | ninguna | 0 |
| FALLA | P-04 | 1 |
| PARCIAL | P-01, P-02, P-03, P-05 | 4 |
| BLOQUEO | ninguna. La sesion de `/admin/aprobaciones` no abrio (login 500, base en error). No se uso como veredicto. | 0 |
| Total | P-01 a P-05 | 5 |
