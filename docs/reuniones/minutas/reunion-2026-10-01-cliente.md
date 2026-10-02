# Reunion cliente 01/10/2026 - MJ, Fran y Lupe

**Tipo:** demo de avances (parametrizacion, ventas/contabilizar, libro de compras, nomina) mas plan de lo que sigue.
**Fecha:** jueves 01/10/2026. Grabacion `Screen Recording 2026-10-01 170426.mp4`, 01:08:41. Meet desde ~17:04.
**Cliente en sala (requisito):** Maria Jesus / MJ, Fran, Lupe. Entran ~[09:54].
**No estuvo:** Mario. MJ dice que iba a estar hasta las 16:20 y quedo en otra reunion `[11:42]`-`[11:53]`. Lo que "Mario comento" llega de segunda mano.
**Devint:** Carlos (demo), Sergio (plan y Trello).
**Nombrados, no en sala:** Jose (ajustes de asociacion OC), Felipe (monedas / Banco Central), Pablo (GoSocket, reunion de los martes 12:00), Rodrigo (area agricola, otra empresa, no esta en Trello).

Los primeros ~10 min son Carlos con Sergio, antes de que entre el cliente. Eso no es requisito. MJ manda sobre Carlos/Sergio. Lupe aprueba la nomina en sala. Fran esta, el ASR casi no le atribuye pedidos.

| Fuente | Ubicacion |
|---|---|
| Transcripcion ASR | [`../transcripciones/transcripcion-2026-10-01-reunion-cliente.md`](../transcripciones/transcripcion-2026-10-01-reunion-cliente.md) |
| Whisper | `medios/whisper-local/2026-10-01-reunion/` (wav gitignored) |
| Video | `G:\Mi unidad\ERP ALMHAUE\Sesiones\Semana 11 - 2026-09-28 a 2026-10-04\2026-10-01 Reunion cliente - MJ, Fran y Lupe\` |

---

## 1. Pedidos del cliente

### Ficha proveedor y cliente (MJ)

1. Dejar los modulos **separados**. No unificar el alta en un solo formulario. `[25:50]`-`[26:06]`.
2. Que **conversen por RUT**: al crear cliente, si ese RUT ya es proveedor, traer los datos y no duplicar el nombre. `[26:06]`-`[26:25]`.
3. El 98% es solo proveedor o solo cliente. El caso raro es un RUT que era proveedor y pasa a ser tambien cliente. `[25:23]`-`[25:40]`.
4. Una consulta por RUT tiene que mostrar movimientos de proveedor y de cliente. `[27:11]`-`[27:21]`.
5. Falta un indicador visible de que ese RUT tambien existe en el otro rol. Carlos lo reconoce `[27:03]`-`[27:09]`.
6. El alta sigue en jefatura (MJ), por seguridad. No hace falta partir el formulario entre "solo proveedores" y "solo clientes". Clientes van por broker: uno o dos por temporada. `[19:47]`-`[20:33]`, `[24:24]`-`[25:01]`.

### Comprobante de venta (MJ)

7. La contabilidad es **siempre peso y dolar**, aunque el documento vaya en otra moneda. `[32:41]`-`[33:14]`.
8. Si no ingresan tipo de cambio, usar el **del dia, Banco Central**. Ellos si lo cambian al ingresar la factura o un caso puntual. `[32:50]`-`[33:22]`.
9. Sumar el **yuan como tercera columna**, en todos los casos. `[33:22]`-`[33:38]`.
10. AUX = RUT del cliente, en general **sin digito verificador**. `[33:44]`-`[34:02]`.
11. Glosa util para el mayor: el **comentario que ellos escriben** (numero de factura + una descripcion corta). No alargar con el texto del item. `[37:23]`-`[38:18]`.
12. Esa misma glosa se **repite en todas las lineas** (cliente, IVA, ingreso), para leer el mayor sin abrir el comprobante. `[39:36]`-`[40:16]`.
13. La cuenta que en el PDF salio como "caja" tiene que ser **IVA debito**. `[38:48]`-`[39:16]`.
14. El nombre del dueno que salia en el comprobante de ellos **no va**. `[38:20]`-`[38:46]`.
15. El PDF que ellos mandaron trae en la glosa tipo, folio y tipo de cambio ademas del numero manual. MJ vio numeros que no calzan (F1905 contra el folio) y lo marco como error de ese respaldo ("una red nuestra"). La glosa que piden para reportar es la del comentario, no repetir lo que ya esta al lado. `[34:16]`-`[37:23]`.

### Libro de compras, OC madre e hijas (MJ)

16. Si el DTE no trae OC, avisar y poder **notificar a quien debe crear la OC** (proveedor no creado, OC inexistente o con diferencia). `[45:47]`-`[46:23]`.
17. **OC madre** solo informativa y **solo en insumos**. No se refleja en otros modulos. Lo que se contabiliza son las **hijas**. `[47:07]`-`[47:43]`.
18. Si el monto de la OC **sube**, vuelve a la cadena de aprobacion. MJ: "Si". `[47:45]`-`[48:05]`.

### Guias y bodega, solo ALM (MJ)

19. Guia **solo para insumos**. Lo demas entra con factura directa. Es ALM, no la exportacion. `[55:22]`-`[55:38]`.
20. La guia **actualiza bodega**. La OC se asocia a la **factura de fin de mes**, no a la guia. Ejemplo: OC madre 100 cajas, entregan 10 por semana, 4 guias de 10, factura del mes por 40. `[55:44]`-`[56:45]`.
21. En insumos hay que **listar las guias recibidas**. La recepcion de material es con guia, 100%. `[56:46]`-`[57:03]`.
22. El control es con **guia fisica** (jefe de abastecimiento), no alcanza con el documento electronico. `[57:03]`-`[57:16]`.
23. Devolucion a proveedor (factura rechazada, devolver material) **solo ALM**. Almahue exportacion compra lo justo que vende; ahi no hay reintegro. `[58:12]`-`[01:00:18]`.

### Nomina (Lupe)

24. Vista de periodo actual / historico, semanas, pendientes y atrasados, y banderas configurables (atrasado, critico, 90 dias): **Lupe la aprobo**. `[49:56]`-`[49:59]`.

### Lo que no pidieron

- Importar/exportar **area de negocio**. Hoy no la usan ni para gestion. Mario (control de gestion) podria pedirla despues; en esta sala no quedo pedida. `[16:13]`-`[16:52]`.
- Nombre del dueno en el comprobante. Ver punto 14.

---

## 2. Compromisos

| Que | Quien | Cuando |
|---|---|---|
| Flujo del modulo **contratista**, del mismo tipo que el diagrama de compras que mando Mario | MJ. "Trabajamos en el." `[13:54]` | Adelanto el **martes** (reunion de las 12 con Carlos, tema conexion con Pablo), si no alcanza el proceso completo `[01:01:26]`-`[01:01:40]` |
| Apoyarse en **Rodrigo** (agricola, otra empresa) por si el contratista necesita algo distinto. No esta en Trello | MJ `[01:03:08]`-`[01:03:28]` | Sin fecha |
| Notificaciones de compras, asociacion de OC y flujo de **OC hija** | Sergio, dicho en sala `[01:01:08]`-`[01:01:19]` | Proxima semana (semana del 6/10) |
| Despues de cerrar OC: contabilizacion de compras, luego tesoreria. Contratista al final, y sin el flujo se estancan la semana siguiente | Sergio `[13:30]`, `[01:01:19]` | Plan dicho al cliente |
| Visita presencial | Sergio: semana del **26/10**. MJ manda la ubicacion al grupo `[01:04:00]`, `[01:04:38]` | Rosario, ~10 min de Rengo |
| Contabilidad en Trello **vuelve a Devint** (falta la base y ajustes). Contratista queda en Lupe. Compras y ventas: alguien del cliente dijo "yo me caso con eso"; el ASR no distingue si fue MJ, Fran o Lupe | Sergio arma el tablero `[53:19]`-`[54:41]` | En la reunion |
| Corregir el comprobante (TC del dia, peso/dolar, yuan, glosa, IVA debito) | Carlos, "vamos a hacer entonces la correccion" `[33:15]`, `[39:06]` | Sin fecha distinta del avance de ventas |
| Validar con **Pablo** si GoSocket trae guias **recibidas** codigo 52 (el RCV del SII no las muestra; pueden ser solo emitidas) | Sergio le pide a Carlos `[57:16]`-`[57:58]` | Martes, junto a la conexion con Pablo |
| Avisar cuando haya avance del reintegro de bodega solo en ALM | Carlos `[01:00:23]` | Sin fecha |

---

## 3. Para desarrollar

Orden sugerido por lo que la sala dejo abierto, no por el relato de la demo.

1. **Comprobante de venta.** Columnas peso y dolar siempre. Tipo de cambio del dia (Banco Central) si no lo ingresan, editable en la factura. Tercera columna yuan. AUX = RUT sin DV. Glosa = comentario manual, repetida en cada linea. Cuenta IVA debito, no "caja". Sin nombre del dueno.
2. **Asociar OC en libro de compras, filtrada por RUT.** En el ensayo previo al cliente, en el servidor salian todas las OC, no las del RUT. Carlos dijo que el filtro estaba en local y no se habia publicado `[04:17]`-`[05:42]`. Si el RUT no tiene OC, no mostrar el universo completo.
3. **Monto pendiente de la OC**, no solo el neto total. Lo vieron antes de que entrara MJ `[05:44]`-`[06:29]`. Jose venia en ese ajuste.
4. **OC madre / hijas.** Madre informativa y solo en insumos. Contabiliza la hija. Subir el monto reabre la aprobacion. Sigue maqueta `[47:15]`.
5. **Guia de insumos (ALM).** Recepcion a bodega con guia fisica. La factura de fin de mes es la que se vincula a la OC. Listar guias recibidas en insumos. No armar ese flujo en Almahue exportacion.
6. **Devolucion a proveedor solo ALM.** Flag por empresa, o la diferenciacion por RUT que pidio mirar Sergio antes de cerrar el diseno `[59:01]`-`[59:13]`.
7. **Notificacion** a quien debe crear la OC. El correo no esta conectado. La bandeja interna esta dibujada y **no envia** `[46:23]`-`[46:42]`.
8. **Ficha por RUT compartida** entre proveedor y cliente, modulos separados, mas la marca de que el RUT existe en el otro rol.
9. **Bug al agregar integrantes** en reglas de aprobacion. Carlos lo nombro al mostrarle la cadena a MJ `[51:09]`-`[51:13]`.
10. **Contratista:** no cerrar proforma a OC hasta que el cliente confirme. Sergio dejo la duda abierta y nadie la respondio `[54:07]`-`[54:22]`. El insumo de ese modulo es el flujo que MJ se comprometio a traer el martes, con posible detalle de Rodrigo.

### Ya quedo aceptado en sala (no reabrir como hueco)

- Vigencia de elementos de costo: anulado no se usa y no se borra el historial `[17:36]`-`[18:04]`.
- Dias de neto e IVA editables a mano (ejemplo 45); en los otros modulos son sugerencia `[18:27]`-`[18:42]`.
- Historico de monedas desde el Banco Central, sin pisar los demas modulos `[28:43]`-`[29:48]`.
- Nomina semanal con banderas configurables: Lupe `[49:56]`.

### Preguntas abiertas

- Proforma de contratista: se convierte en OC o no. `[54:12]`.
- Guias codigo 52 en documentos recibidos de GoSocket, emitidas contra recibidas. `[57:16]`.
- Quien del cliente quedo dueño de compras y ventas en Trello. `[54:36]`.
- Area de negocio: esperar a Mario si la quiere para control de gestion. `[16:39]`.
