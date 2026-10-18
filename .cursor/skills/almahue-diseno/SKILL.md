---
name: almahue-diseno
description: >-
  Reglas visuales del ERP Almahue: totales en tarjetas plegables, colores de
  boton por tipo de accion, iconos distintos, tooltip al pasar el mouse,
  estados centrados, filtro en la barra, aviso al lado del mensaje, columna
  Origen, marca de configuracion faltante y menu de un solo nivel. Usar al
  tocar pantallas, tablas, botones, badges, menus o totales del front.
---

# Diseño Almahue

Una sola forma por tipo de control. Ordenes de compra (el listado de Compras) queda fuera hasta que se pida.

## Orden de la pantalla

De arriba a abajo: titulo, totales, tabla.

- El titulo es `PageHeader`: migas y titulo a la izquierda, botones de la pagina a la derecha, en la misma fila. La bajada va debajo y no empuja los botones. Exportar (Excel, CSV o PDF) va en esa fila, en blanco (`outline`). El primario, si existe, va al final.
- Los totales van debajo del titulo, nunca arriba. Si hay varias tarjetas, quedan en una sola fila (si no caben, la fila se desplaza). No se parten en una segunda linea.
- El filtro de la lista (contratista, fechas, periodo, moneda) va en la barra de la tabla, junto a la busqueda (`filterBarExtra`), en la misma linea que Filtros y Aplicar filtros. Cada campo tiene ancho fijo: no uses un input a todo el ancho, porque baja a una segunda linea. No arriba del titulo, no en una tarjeta entre el titulo y los totales, y no repitas el periodo: el panel superior ya lo muestra.
- No agregues un boton Buscar propio si la tabla ya tiene busqueda y Aplicar filtros, o si el dato sigue al campo.
- Los checks de vista (ver en pesos, ver totales) van en la misma fila que Todos y Columnas, una sola linea, justo arriba de la tabla. En esa fila, los botones de moneda (Todas, CLP, USD, Yuan) quedan a la izquierda y los checks a la derecha.
- Si la tarjeta de total es angosta, ingreso, egreso y saldo van en tres lineas (etiqueta y cifra en la misma linea) para que el saldo tenga espacio.
- El cuerpo del total es solo la grilla de tarjetas. El boton de la pagina no va dentro de ese bloque.

## Totales

Bloque de solo lectura (KPI, saldo, suma del periodo): `CollapsibleLibroSection`.

- Boton a todo el ancho. Cerrado: `ChevronRight`. Abierto: `ChevronDown`. Icono 14.
- Titulo en mayusculas. La cifra principal, a la derecha.
- Abierto por defecto si es el total principal de la pantalla.
- El cuerpo abierto es una fila de `KpiStatCard`: etiqueta arriba, cifra grande, detalle chico. No un parrafo, no una caja suelta y no una segunda linea de tarjetas.
- Ordenes y documentos: ordenes, clientes distintos, monto y un recuadro por estado.
- Reporte de ingresos: en Totales, una fila con el monto, los contratistas, la cantidad de ingresos y la cantidad de proformas. Debajo, las semanas del periodo en otra fila horizontal (4 o 5, de 7 dias dentro del mes), cada una con su total. El total por dia va en la vista Calendario: el dia con ingresos se destaca y el dia en cero queda opaco.
- Atajos (Traspaso): un boton por lista. Al pulsarlo se abre esa lista y se cierran las demas. El Excel del cierre va en el titulo, en blanco. Cerrar mes va a su derecha, en verde: primero la lista de lo que entra, luego la cuenta de la sala y la glosa editable. Con el mes cerrado, Entran al asiento pasa a Elementos de cierre, tambien en los totales.

Un total que se edita (descuento del wizard Emitir) sigue en `CollapsibleRightPanel`. No lo conviertas en el bloque de solo lectura.

## Botones

El color dice el tipo de accion. Usa `Button`, tamaño normal, en el pie del detalle. No un boton a todo el ancho en el cuerpo.

| Accion | Variante | Color |
|---|---|---|
| Avanza o cierra el documento (editar, contabilizar, cerrar orden, confirmar, facturar) | `primary` | Verde |
| Imprime o exporta, sin cambiar el documento | `outline` en el titulo; `secondary` si va dentro de un documento | Blanco en la pagina; bordo en el documento |
| Anula, elimina, rechaza o reversa | `danger` | Rojo |
| Consulta (historial, notificar) | `outline` | Borde |
| Cierra el dialogo | `ghost` | Sin fondo |

## Acciones de fila

Una sola columna Acciones.

- Iconos de `RowActions`. En la misma fila, cada accion tiene un icono distinto: items, trazabilidad, PDF, notificar, factura, reclamo, reenviar, modificar, reversar y reemitir no se repiten entre si ni con el lapiz de editar.
- Editar y eliminar van en esa misma columna, no en una segunda.
- El nombre sale al entrar el mouse al icono y sigue visible mientras el puntero este encima, aunque se mueva dentro del boton. Lo pinta `AccionConNombre` (tambien `RowActions` y `Button` cuando trae `title`). No uses el `title` del navegador: ese espera a que el mouse se detenga.

## Aviso y filtro

- El texto del aviso y su boton van en la misma fila: mensaje a la izquierda, boton a la derecha.
- El filtro de la lista va en `toolbarExtra` de la tabla, junto a la busqueda. No arriba del titulo de la pagina.

## Estado

`Badge` centra el texto. Si el estado ocupa dos lineas, las dos quedan centradas. No lo alinees a la izquierda dentro de la pastilla.

## Origen

Si la fila nace de otro documento o apunta a uno (factura, OC, OV, guia, proforma), una columna **Origen** con el enlace. No repitas ese vinculo como un boton de acciones.

## Historial

Orden de compra, orden de insumos, orden de venta y DTE: clic en la fila abre el documento, y desde ahi **Historial** (usuario, dia y hora). No pulses Guardar, Contabilizar, Emitir ni Pagar para mostrarlo.

## Menu

Un modulo, un nivel. Sin grupo Operacion, Libros ni Maestros.

Ventas, en este orden: Ordenes de venta, Emitir DTE, Libro de ventas, Libro de guias, Clientes.

Si falta configuracion para que el sistema opere, el menu muestra un `!` amarillo en el modulo y en la pantalla (`parametros-faltantes`). Aplanar el menu no quita esa marca: el `!` va en el item cuya ruta coincide y tambien en el modulo.

## Al revisar una pantalla

Recorrela en este orden y anota lo que no coincida. No des por bueno un bloque solo porque ya es una tarjeta.

1. Titulo a la izquierda. Exportar y el resto de botones de la pagina a la derecha, en la misma fila que el titulo. La bajada no los baja.
2. Nada entre el titulo y los totales: ni filtros, ni un boton Buscar, ni el texto del periodo.
3. Totales plegables, abiertos, solo `KpiStatCard`, una sola fila. En reporte de ingresos no hay una tarjeta por dia.
4. La tabla va despues. Contratista, fechas y moneda estan en su barra, junto a la busqueda.
5. El estado de cada fila es un `Badge` centrado.
6. Una columna Acciones, iconos distintos, nombre al pasar el mouse.
