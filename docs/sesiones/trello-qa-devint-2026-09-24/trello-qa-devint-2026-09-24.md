# En QA Devint — tarjetas para planificar (corte 24/09/2026)

Tablero **Almahue ERP**, lista **En QA Devint**. 14 tarjetas abiertas. Los adjuntos quedaron en [`trello-qa-devint-2026-09-24/`](trello-qa-devint-2026-09-24/).

Ocho tarjetas tienen un pedido de **Mario Ubillo** escrito el **17/09/2026**. Una (Flujo de caja) tiene el ejemplo que Mario mandó por WhatsApp y un comentario de Carlos. Las otras cinco son capturas de validación del **14/09**, sin comentario de Mario.

Centros, elementos, códigos financieros y la carga del Excel de maestros quedaron en Parametrización el 24/09. El antes y el después están en [`parametrizacion-ajustes-2026-09-24/comparacion.html`](parametrizacion-ajustes-2026-09-24/comparacion.html). El resto de esta lista no se tocó.

## Índice

| Tarjeta | Quién pidió | Qué hay que decidir | Trello |
|---|---|---|---|
| Inicio de sesión | Mario 17/09 | Logo oficial Almahue Export | [nZxF2zT2](https://trello.com/c/nZxF2zT2) |
| Administración — Empresas | Mario 17/09 | 4 campos opcionales del representante | [rYa9lRan](https://trello.com/c/rYa9lRan) |
| Administración — Usuarios | Mario 17/09 | Solo admin crea, edita y resetea; nombre en un solo caso | [CSpgLHIY](https://trello.com/c/CSpgLHIY) |
| Plantilla documentos | Mario 17/09 | Formato parecido al PDF de Acepta (ND exportación) | [Eoz706MH](https://trello.com/c/Eoz706MH) |
| Centros de costo | Mario 17/09 | Código numérico, nombre en mayúscula, vigencia automática, no repetir ni pisar | [T8aF6AyE](https://trello.com/c/T8aF6AyE) |
| Elementos de costo | Mario 17/09 | Lo mismo + sugerir el siguiente correlativo | [CeZ2zzwm](https://trello.com/c/CeZ2zzwm) |
| Códigos financieros | Mario 17/09 | Igual que centros de costo | [82uWZJwB](https://trello.com/c/82uWZJwB) |
| Maestros contabilidad | Mario 17/09 | Carga masiva del Excel (4 hojas) | [nfrmQKOa](https://trello.com/c/nfrmQKOa) |
| Tesorería — Flujo de caja | Ejemplo de Mario; comentario de Carlos 14/09 | Grilla mensual consolidada por grupo y por empresa | [PQK1bQUU](https://trello.com/c/PQK1bQUU) |
| Inicio — Panel operativo | Sin pedido nuevo | Solo captura de validación | [Z2PYymve](https://trello.com/c/Z2PYymve) |
| Compras — Órdenes | Sin pedido nuevo | Solo captura de validación | [vnevrzXL](https://trello.com/c/vnevrzXL) |
| Compras — Aprobaciones | Sin pedido nuevo | Solo captura de validación | [9dh0NW2S](https://trello.com/c/9dh0NW2S) |
| Compras — Recepciones | Sin pedido nuevo | Solo captura de validación | [hushL7wu](https://trello.com/c/hushL7wu) |
| Compras — Libro | Sin pedido nuevo | Solo captura de validación | [OXp5jEPS](https://trello.com/c/OXp5jEPS) |

---

## Pedidos de Mario (17/09)

### 1. Inicio de sesión

[Tarjeta](https://trello.com/c/nZxF2zT2). Asignada a Mario.

Comentario de Mario (17/09 15:23):

> Usar logo oficial de Almahue

Adjuntó el wordmark **Almahue EXPORT** (hojas verdes, wordmark burdeo).

Pantalla que está en la tarjeta hoy: login partido, panel verde/burdeo con el isotipo triangular «Almahue ERP» y el texto «ERP Enterprise Almahue».

![Login actual](trello-qa-devint-2026-09-24/inicio-inicio-de-sesion/01-image.png)

![Logo que pide Mario](trello-qa-devint-2026-09-24/inicio-inicio-de-sesion/02-2024-06-21-09-20-16-invitacion-almahue.png)

Para planificar: cambiar el isotipo del login (y, si corresponde, el del sidebar) por este wordmark. El archivo es un PNG chico (9 KB), recorte de una invitación; conviene pedir el original en vector si se va a usar en pantalla grande.

### 2. Administración — Empresas

[Tarjeta](https://trello.com/c/rYa9lRan). Etiquetas MockUp y Solicitudes reunión 1. Asignada a Mario.

Comentario de Mario (17/09 12:40):

> 1. Mock up — OK
> 2. Al crear la empresa, solicitaría la siguiente información adicional: NOMBRE REPRESENTANTE LEGAL, RUT REPRESENTANTE LEGAL, MAIL CONTACTO, DIRECCION. Todos de carácter opcional.

Comentario anterior de Carlos (22/07), reunión 1: CRUD empresas multiempresa y aislamiento estricto por empresa activa.

La captura de la tarjeta es el listado actual: RUT, razón social, giro, aceptación compra (días), billing id, nº resolución SII, estado. Empresas visibles: ALMAHUE EXPORT SPA y ALM SERVICES SPA.

![Empresas](trello-qa-devint-2026-09-24/administracion-empresas/01-image.png)

Para planificar: cuatro campos opcionales en el alta (y en la edición) de empresa. No reemplazan RUT, razón social ni giro. Mail y dirección de la **empresa** ya aparecen en Plantilla documentos; aquí Mario los pide en el alta de la empresa, más los datos del representante legal.

### 3. Administración — Usuarios

[Tarjeta](https://trello.com/c/CSpgLHIY). Mismas etiquetas. Asignada a Mario.

Comentario de Mario (17/09 13:12):

> Solo usuario administrador debe poder crear y editar usuarios.
> Que solo el admin tenga la opción de reestablecer la contraseña a otro usuario.
> Al crear los nombres de usuario, solo por orden: si se crean ya sea en mayúscula o minúscula, se estandarice al guardar, para mantener un orden en la base de datos.

Comentarios anteriores de Carlos: infra de ~15 usuarios y riesgo de sesiones compartidas (22/07); renombre a Administración / Usuarios (31/08).

![Usuarios](trello-qa-devint-2026-09-24/administracion-usuarios/01-image.png)

Para planificar, tres reglas:

1. Crear y editar usuarios queda solo en el rol administrador.
2. Reestablecer la contraseña de otro usuario queda solo en el administrador. El propio usuario sigue pudiendo cambiar la suya.
3. Al guardar, el nombre queda en un solo caso. Mario no dice si mayúscula o minúscula, ni si habla del nombre visible o del correo de login. Hay que cerrarlo antes de implementarlo: el login por correo no puede cambiar de caso si el correo ya se usa para entrar.

### 4. Plantilla documentos

[Tarjeta](https://trello.com/c/Eoz706MH). Asignada a Mario.

Comentario de Mario (17/09 15:31):

> Se podrá llegar a tener un formato más parecido al de hoy en día?

Adjuntó `PdfViewMedia.pdf` (1 página). No es una factura nacional: es una **nota de débito de exportación electrónica** emitida por Acepta (RUT 77.032.638-9, SII Rancagua, folio 1616, 15/09/2026).

Datos que trae el PDF:

- Receptor: SHANGHAI HUI ZHAN INTERNATIONAL TRADE CO., LTD, dirección en Fengxian, id. fiscal 55555555.
- Despacho marítimo. Ítem `009 CIRUELA 9KN`, 2.400 cajas, precio unitario 6,659166, total USD 15.982.
- Texto de embarque: total neto 21.600 kg, contenedor TTNU815309-3, EMB REF 395, nave MSC MARGARITA, venta FOB.
- Referencia: factura de exportación electrónica folio 1938 del 03/02/2026, razón «Corrige monto: ND por cierre».
- Moneda dólar USA, monto exento y total 15.982. Otra moneda peso CL, 13.880.687. Observación TC 868,52.
- Bultos: 22-CAJACARTON, cantidad 2.400.
- Pie: timbre SII, Res. 80 de 2014, solución Escritorio / www.acepta.com.

La captura de la tarjeta es la plantilla actual: colores, tipografía, logo, sello y una vista previa de **factura electrónica nacional** marcada BORRADOR (`N° FAC-DEMO-001`, IVA 19 %).

![Plantilla actual](trello-qa-devint-2026-09-24/administracion-plantilla-documentos/01-image.png)

PDF de referencia: [`02-pdfviewmedia.pdf`](trello-qa-devint-2026-09-24/administracion-plantilla-documentos/02-pdfviewmedia.pdf).

Para planificar: la pregunta de Mario es de formato impreso, no de campos de la ficha. El ejemplo es una ND de exportación (bilingüe, sin IVA, con puertos, bultos, nave y referencia), y la vista previa del ERP es una factura nacional con IVA. Hay que acordar si el parecido aplica a la impresión de DTE de exportación, a la OC, o a ambos. El DTE real lo sigue emitiendo el partner; esto es la plantilla interna / el PDF que el usuario ve.

### 5. Centros de costo

[Tarjeta](https://trello.com/c/T8aF6AyE). Asignada a Mario.

Comentario de Mario (17/09 15:48):

> 1. El código solo admite carácter numérico.
> 2. Al registrar el nombre, que siempre se guarde con mayúscula.
> 3. La vigencia sea automática desde la fecha de creación.
> 4. Que por nada del mundo deje pisar códigos ya creados, ni tampoco repetir, aunque el nombre sea distinto.

La captura muestra el mantenedor demo: códigos `ADM`, `PACK`, `CAMPO`, `FIN` (letras), columnas código, nombre, encargado, desde, estado. Ya existe el botón **Importar Excel**.

![Centros de costo](trello-qa-devint-2026-09-24/parametrizacion-centros-de-costo/01-image.png)

Para planificar:

- Código numérico choca con los códigos demo en letras. El Excel de Mario usa `10100`, `10200`, etc. (ver maestros).
- «Desde» deja de editarse a mano: se llena con la fecha de alta.
- Unicidad del código por empresa, y el update no puede reasignar un código ya usado a otro registro.
- Importar Excel acepta `ccos` / `nomCcos` de la hoja «Centros de costo».

### 6. Elementos de costo

[Tarjeta](https://trello.com/c/CeZ2zzwm). Asignada a Mario.

Comentario de Mario (17/09 15:54):

> Mismas solicitudes que para los centros de costos.
> Ideal que cuando uno vaya a crear el elemento, la plataforma recomiende el siguiente correlativo disponible sin asignar. Que no sea obligatorio usarlo, pero que ya aparezca ahí.

![Elementos de costo](trello-qa-devint-2026-09-24/parametrizacion-elementos-de-costo/01-image.png)

Para planificar: las cuatro reglas de centros, más un sugerido del siguiente número libre al abrir el alta. El usuario puede cambiarlo. En el Excel los códigos no son una secuencia continua (`1001`…`1006`, después `1101`, `1201`). El sugerido tiene que ser el siguiente hueco numérico, no `max+1` si Mario quiere rellenar huecos; hay que confirmar cuál de las dos.

### 7. Códigos financieros

[Tarjeta](https://trello.com/c/82uWZJwB). Asignada a Mario.

Comentario de Mario (17/09 16:07):

> idem centro costos y elementos de costo

No repite lo del correlativo sugerido. Lo de elementos dice «mismas solicitudes que centros» y después, aparte, el correlativo. Acá solo dice «idem» a los dos. Para planificar lo tomamos como las cuatro reglas de centros. El correlativo sugerido queda solo en elementos, salvo que al planificar lo queramos igual en los tres mantenedores.

![Códigos financieros](trello-qa-devint-2026-09-24/parametrizacion-codigos-financieros/01-image.png)

### 8. Maestros contabilidad Almahue

[Tarjeta](https://trello.com/c/nfrmQKOa). Sin asignar. La creó el hilo del 17/09.

Descripción:

1. Centros de costos
2. Cuentas contables
3. Elementos de costos
4. Códigos financieros

Comentario de Mario (17/09 16:09):

> ¿Podemos hacer una carga masiva de estos parámetros?

Archivo: [`01-maestros-contabilidad.xlsx`](trello-qa-devint-2026-09-24/maestros-contabilidad-almahue/01-maestros-contabilidad.xlsx).

| Hoja | Filas de datos | Columnas |
|---|---:|---|
| Centros de costo | 46 | `ccos`, `nomCcos` |
| Cuentas contables | 184 | `ctaContable`, `nomCtaContable` |
| Elementos de costo | 131 | `codElementoCosto`, `nomElementoCosto` |
| Códigos financieros | 49 | `codFinanciero`, `nomFinanciero` |

Centros: códigos de 5 dígitos. Hay dos familias de nombre, `ALM` y `ALMAHUE` (por ejemplo `10100 DAGGEN ALM` y `20100 DAGGEN ALMAHUE`), más `75200 GERENCIA SANTA PETRA`.

Cuentas: 9 dígitos, desde `110101001 CAJA` hasta `640101001 IMPUESTO RENTA 1RA. CATEGORIA`. Incluye bancos, anticipos, existencias, IVA, productores, «FACT X RECIBIR» de insumos, contratistas y servicios.

Elementos: 4 dígitos, desde `1001 SERVICIOS DE REPARACIÓN ACTIVOS` hasta `4005 DONACIONES`. Muchos códigos de comercio exterior (fletes, BL, gate, almacenaje).

Códigos financieros: 4 dígitos. Ventas por especie y mercado (`1002 VENTA EXPORTACIÓN CEREZAS` …), gastos (`3001 MATERIA PRIMA` …) y financieros (`6001 FINANC. BANCO CHILE`, `7006 DIFERENCIA TIPO DE CAMBIO`).

La carga es por empresa. El Excel de Mario ya entra por el Importar Excel de cada mantenedor: centros (`ccos` / `nomCcos`), elementos (`codElementoCosto` / `nomElementoCosto`), códigos financieros (`codFinanciero` / `nomFinanciero`) y plan de cuentas (hoja «Cuentas contables», `ctaContable` / `nomCtaContable`). Un código de 9 dígitos como `110101001` queda como cuenta hoja `1-1-01-01-001`. El archivo no trae las cuentas padre, así que esas 184 filas quedan sin padre. Elementos sin departamento quedan en GENERAL. Códigos nuevos quedan sin concepto; si el código ya existía, el concepto no se borra.

---

## Flujo de caja

[Tarjeta](https://trello.com/c/PQK1bQUU). Asignada a **LUPE ALVAREZ**. Comentario de Carlos (14/09 21:18):

> se debe dejar como resultado esperado la imagen «flujo de caja» cargada en tarjeta

La imagen es una captura de WhatsApp de Mario («Hoy a las 17:54»). A la izquierda está el flujo del ERP (filas por movimiento, apertura QA, yuan). A la derecha, el Excel que Mario usa: meses en columnas (septiembre a agosto, atravesando dos años), filas por tipo (operacional, inversión, financiamiento) e ítems (venta exportación cerezas, insumos, remuneraciones, etc.), y una fila final de saldo caja. El texto de Mario en el chat:

> ejemplo flujos de caja, la idea es que se pueda ver consolidado como grupo (ALMAHUE Y ALM JUNTOS) y por verlo como empresa.

![Flujo de caja — ERP y Excel de Mario](trello-qa-devint-2026-09-24/tesoreria-flujo-de-caja/02-flujo-de-caja.png)

La otra imagen de la tarjeta es solo la pantalla del ERP, sin el Excel:

![Flujo de caja — captura ERP](trello-qa-devint-2026-09-24/tesoreria-flujo-de-caja/01-image.png)

Para planificar: no es un bug de la grilla actual. Pide otra vista: columnas = meses, filas = conceptos del flujo, más un corte **grupo** (Almahue Export + Alm Services) y un corte **por empresa**. Los montos del Excel en la foto no se leen (están pixelados).

---

## Tarjetas sin pedido nuevo

Quedaron en la misma lista con una captura del 14/09 y el texto de validación. No hay comentario de Mario.

### Inicio — Panel operativo

[Z2PYymve](https://trello.com/c/Z2PYymve). «Validar las funciones implementadas de pagina».

![Panel operativo](trello-qa-devint-2026-09-24/inicio-panel-operativo/01-image.png)

### Compras — Órdenes de compra

[vnevrzXL](https://trello.com/c/vnevrzXL). «Validar todas las funcionales de este menu, como por ejemplo crear una nueva orden de compra.»

![Órdenes de compra](trello-qa-devint-2026-09-24/compras-ordenes-de-compra/01-image.png)

### Compras — Aprobaciones

[9dh0NW2S](https://trello.com/c/9dh0NW2S). «validar todas las opciones de la pagina».

![Aprobaciones](trello-qa-devint-2026-09-24/compras-aprobaciones/01-image.png)

### Compras — Recepciones

[hushL7wu](https://trello.com/c/hushL7wu). «Validar las funciones implementadas de pagina».

![Recepciones](trello-qa-devint-2026-09-24/compras-recepciones/01-image.png)

### Compras — Libro de compras

[OXp5jEPS](https://trello.com/c/OXp5jEPS). «Probar las funcionalidades de la pagina».

![Libro de compras](trello-qa-devint-2026-09-24/compras-libro-de-compras/01-image.png)

---

## Orden sugerido para implementar juntos

1. **Reglas de los tres mantenedores** (centros, elementos, códigos financieros): numérico, mayúsculas, vigencia automática, no pisar código. El correlativo sugerido solo en elementos hasta confirmar.
2. **Carga del Excel** sobre esas reglas, por empresa. Revisar el import que ya está en centros y el del plan de cuentas antes de hacer uno nuevo.
3. **Empresa:** cuatro campos opcionales.
4. **Usuarios:** permisos de admin y el caso del nombre, después de cerrar si es el nombre visible o el correo.
5. **Logo** del login, idealmente con el archivo original.
6. **Plantilla:** acordar si el PDF de la ND de exportación es el objetivo de la impresión, porque la vista previa actual es una factura nacional.
7. **Flujo de caja:** vista mensual consolidada grupo / empresa. Es otra pantalla, no un ajuste de la grilla de movimientos.
