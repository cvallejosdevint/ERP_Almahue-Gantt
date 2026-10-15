# Word de contratistas (6/10) y deck de compras de Mario

María José lo mandó en la reunión del 6/10 con GoSocket, hacia el minuto 11:26: un Word con la trazabilidad del módulo, para ir conversando. En la misma reunión dijo que el archivo está armado para el área agrícola y que el contrato de Agrosoft no se lleva.

La copia de trabajo es `flujo-modulo-contratistas.docx`. El texto, en el orden del documento, está en `texto-word.md`. Las nueve figuras están en `imagenes/`.

El 13/10, a las 13:20, se volvió a bajar el mismo Word (`Flujo de Trabajo - Módulo de Contratistas (1).docx`). El hash SHA-256 es el mismo que el del 6/10 y que esta copia: `70A3C32F2037D29CF14336514F189E57CC60CD545B335D48CBCFE0D6490D053D`. No hay una versión nueva.

El deck de Mario ya estaba en el repo: [`../whatsapp-mario-lupe-2026-09/07-compras-almahue-flujo.pptx`](../whatsapp-mario-lupe-2026-09/07-compras-almahue-flujo.pptx). El de Descargas (`Compras_Almahue_ Flujo.pptx`) tiene el mismo hash. El texto de las 15 diapositivas está en `texto-ppt-mario.md`. Lo expuso como flujo de compras (versión 1.2, septiembre 2026, asientos por definir). No es el flujo de proformas.

## Dónde está el código de Diego

Los commits del 13/10 son:

- Back `9df72b6`, `Contratistas: olas B/C, facturación RC y QA release local.`
- Front `3c4f66e`, `Contratistas: pantallas olas A-C y fix facturar con RC.`

Entraron a `carlos-dev` el mismo día, en `d350806` (back) y `6189d49` (front): `Integrar r_diego en carlos-dev`. En el schema de esa rama están `SectorContratista`, `FaenaContratista`, `predio`, `temporada` y el estado `ENVIADA_CONTRATISTA`. El único cambio de Diego en compras es el guardado de `distribucionCc` al crear la orden hija. No implementa el deck de Mario.

Lo de abajo compara el Word y el deck con ese código ya integrado.

## Texto del Word contra sus imágenes

El texto y las figuras no dicen lo mismo en cuatro puntos. En el resto coinciden.

| Tema | Texto | Imagen | Qué hizo Diego en `r_diego` |
|---|---|---|---|
| Contrato | El paso 1 deja al contratista listo para asociarlo a un contrato. El paso 4 dice que la proforma cierra el contrato. | `01-flujo-siete-pasos.png` pone la caja Contrato entre la ficha y el registro diario. | No hay contrato. Sigue el cierre hablado del 6/10 (minuto 12:37), no el Word. El desfase está en el texto y en el diagrama a la vez. |
| Quién se aprueba | Debajo del paso 4: al guardar cada ingreso, pasa a movimientos por aprobar. | El diagrama pone Aprobación después de Proforma, no después de cada fila. | Aprueba la proforma. Sigue la imagen y la corrección que ella misma hizo en la reunión (minuto 24:05). La frase del texto quedó vieja. |
| Trabajador | La lista de campos del registro no lo nombra. | `04-registro-masivo-trabajador.png` tiene columna Trabajador y avisa que varias filas de la misma faena se guardan en un solo registro. | No hay maestro de trabajador. El ingreso masivo fusiona filas de la misma faena. Toma la nota de la imagen, no una ficha de persona. En la reunión ella dijo que el trabajador no es necesario. |
| Cabecera del registro | La lista dice fecha, cuartel, faena, forma de pago, unidad, contratista, duración, jornada, tipo, valor, cantidad y total. No nombra empresa, temporada, predio ni sector. | `03-registro-masivo-cabecera.png` abre con empresa, temporada y predio, y la grilla parte en sector, cuartel y faena. | Predio y temporada son texto opcional. Sector y faena son mantenedores. Eso está en la imagen y en la reunión, y el párrafo «Se registra» no lo trae. |
| Cuartel | Lo nombra como campo. | Es un combo distinto del de sector. | El rótulo es «Cuartel / centro de costo» y el dato es `CentroCosto`. No hay mantenedor de cuartel. El combo separado es de la imagen. |
| Asociación | Elegir proveedor, ver sus facturas y sus proformas aprobadas, e ir descontando el total. | `06-nueva-asociacion.png` y `07-lista-asociaciones.png` son esa pantalla, dentro de contratistas. La imagen 6 además parte la línea en «sin asignar» y «a asignar». | Sigue en Contratistas. Si no se indica un registro de compra, crea una orden. Si el monto no calza con la suma de proformas, rechaza. No parte una proforma. El descuento parcial de la imagen 6 no está. El texto pide comprobar que no haya duplicados, no partir el monto. |
| Pago | «Pasa automáticamente al módulo de tesorería.» | `09-menu-costos.png` solo muestra el menú Ingresar faenas, Registro múltiple y Asignación de facturas. No hay pantalla de pago. | No hay pase automático a tesorería. Eso lo dice solo el texto. |
| Informe de faena | Pide ver las proformas por separado y un total. | `05-informe-faena.png` agrega especie, variedad, niveles y un trabajador. `08-detalle-totalizado.png` es el detalle por día con cuadrilla y centro de costo. | El ingreso no tiene especie ni variedad. Esas columnas son de la imagen, no del texto. |

El texto también se contradice solo: el título dice 7 pasos y la línea siguiente dice ocho. No hay paso 3. La figura 1 tiene siete cajas, contando el contrato.

Ficha: texto e imagen coinciden en código, RUT, nombre, dirección, ciudad, comuna y creador. La imagen suma apellidos, correo y teléfonos. En el código integrado la ficha tiene `codigo`, `razonSocial`, dirección, ciudad, comuna, correo, dos teléfonos y `creadoPorNombre`. Los apellidos van en la razón social.

## Qué queda corto, y de dónde sale

Diego siguió la reunión del 6/10 y, en varios puntos, el texto. Las pantallas de Agrosoft que van pegadas en el Word piden más de lo que él dejó.

Sale de la imagen, y el texto no lo pide: cuartel como combo distinto del sector, columnas «sin asignar» y «a asignar» para ir descontando el saldo de la factura, especie, variedad y la columna Trabajador. El código no tiene ese cuartel, no parte el saldo y no tiene especie ni trabajador. En el descuento, el texto solo pide comprobar que no haya duplicados: ahí Diego siguió el texto y la imagen muestra otra cosa.

Sale del texto, y la imagen no lo muestra: el paso 6, que manda la factura asociada a tesorería sola. El menú de la imagen 9 no tiene pago. Eso no está en el código.

Sale del texto y de la imagen a la vez, y la reunión del 6/10 lo sacó: el contrato. No está, y coincide con lo que ella dijo en la sala, no con el Word.

No sale ni del texto ni de las imágenes: el estado `ENVIADA_CONTRATISTA`, que hoy bloquea la asociación. Eso lo agregó el código de Diego. El 13/10 al mediodía María José pidió asociar en Compras las proformas aprobadas. El Word, texto e imágenes, deja esa pantalla en Contratistas, y el código sigue ahí.

## Lo que el 13/10 cambió y el Word no

A las 12 del 13/10 María José dejó la asociación del DTE en Compras: ahí se elige orden o proforma, y la cuenta de costo se asigna solo en Contratistas. El Word, en el texto y en las imágenes 6, 7 y 9, deja «Asignación de facturas» dentro de contratistas.

Diego no movió esa pantalla al libro de compras. Asociar sigue en Contratistas y, sin registro, `asociarFacturaProforma` llama a `createOrden`. El estado nuevo `ENVIADA_CONTRATISTA` obliga a marcar el envío antes de facturar. Ella dijo que un correo al contacto «sería bueno»; no pidió un estado que bloquee la asociación. El 13/10 pidió que en compras aparezcan las aprobadas, no las ya enviadas.

## Deck de Mario contra el código

El deck es de compras. Diego no lo tocó, salvo el arreglo de `distribucionCc` en la hija. El contraste es con el código que está en `carlos-dev`.

| Lo que dice el deck | En el código |
|---|---|
| La hija de insumos nace autorizada y no vuelve a aprobarse. La madre conserva el saldo. | La hija nace en `BORRADOR`. No hay un corte que le impida entrar a la cadena. La madre, al cerrar saldo, vuelve a `PENDIENTE_APROBACION`. |
| Toda alerta impide guardar el paso. | La factura de una orden aún no aprobada se destaca y se puede recibir. Eso lo pidió María José el 14/09, después de este deck. |
| Guardar el tipo de cambio generado (pesos de la factura dividido por el monto de la orden en su moneda). | El calce usa el tipo observado de la fecha. La orden no guarda ese tipo generado. |
| Factura manual: el usuario indica orden, monto y tipo de cambio. | Hay alta manual. No sube el PDF. |
| Una línea de neto y una de IVA por cada orden hija, con vencimientos distintos. | El IVA a día 10 está en el proveedor. La orden solo arrastra `condicionPagoDias`. No hay dos líneas de pago por hija. |
| Cinco estados: pendiente de aprobación, aprobada con recepción pendiente, factura pendiente, pendiente de pago, pagada. | Los estados del modelo no usan esos cinco nombres. |
| Asientos de recepción y de factura, por tipo de compra. | La tapa del deck los deja por definir. Siguen sin esa tabla. |
| La madre sigue en el flujo de compras. | El 01/10 María José dijo que la madre es solo un dato de insumos. El deck y esa frase chocan. El listado de compras sigue mostrando la madre. |

Recepción parcial solo en insumos, una factura que cubre varias hijas y no una hija en partes, y días de pago de una lista o digitados: eso sí está encaminado en el código (`ocPadreId`, `assertFacturaCompletaOcHija`, `condicionPagoDias`).
