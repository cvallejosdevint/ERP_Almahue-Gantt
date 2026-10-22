# Cumplimiento vs cliente · 21/10/2026

Contraste del ERP (código local) contra transcripciones, docs Almahue y GoSocket. Fuente primaria: transcripciones. Carlos/Sergio no cuentan salvo confirmación del cliente. Reu5 no cuenta.

Mapa anterior: `mapa-transcripciones-2026-10-13.md` (varios ítems ya cambiaron).

## Veredicto

El ciclo que el cliente usa para operar **está en el software**: OC (servicio e insumos), OV sin cadena, emitir DTE, libro de compras con inbox GoSocket, libro de guías, proformas y cierre CTR, cartola/nómina/pagos, cierre de bodega. **No está cerrado** el paquete GoSocket de emisión (27 casos, descuento en PDF, 34 `MntExe`), ni varios detalles de compras/contratistas/tesorería que MJ pidió en octubre.

## Fuente

| Tipo | Qué se usó |
|---|---|
| Cliente | Reu1-3 as-is Agrosoft; Reu6; 20/08 tarde Lupe/Mario; 28/08 tesorería; 23-24/09; 01/10; 06/10 contratistas; 13/10 GoSocket; 14/10 presentación |
| GoSocket | Manual API, gap Excel, plan emisión 06/10, kickoff 15/09 y 13/10, skill billing |
| Código | `ERP/erp_back`, `ERP/erp_front`, `billing-gateway` al 21/10 |

## Por módulo

Marca: **CUBRE** el pedido; **PARCIAL**; **DEUDA**.

### Compras

| Pedido | Quién | Marca |
|---|---|---|
| OC es el documento; cotiz solo referencia | Lupe 20/08; corte D11 | CUBRE |
| Cadena por monto; rechazo con motivo | Agustín/MJ Reu6 | CUBRE |
| Factura con OC no aprobada: destacar, no contabilizar ni pagar | Lupe 20/08 | CUBRE |
| Asociar DTE a OC o proforma en el libro | MJ 13/10 | CUBRE |
| Hija nace al recepcionar guía; factura se asocia a hijas | MJ 14/10 | CUBRE (madre de insumos no se lista ni se asocia en Compras) |
| Solo hijas recepcionadas para asociar/contabilizar | MJ 14/10 | CUBRE |
| Escalas distintas insumos vs servicios; quién crea madre vs hija | MJ 14/10 | DEUDA |
| Neto e IVA con plazos distintos; TC en la OC | MJ 01/10 | PARCIAL (IVA día en proveedor; aging un vencimiento) |
| Adjuntos en OC; PDF en alta manual | 24/09 | DEUDA |
| Plazo aceptación 7 días | 23/09 | PARCIAL (sigue 8) |
| Notificar si falta OC/proveedor o hay diferencia | MJ 01/10 | PARCIAL (notificaciones existen; no cubre todos los casos) |
| Sin auto-aprobación por monto bajo | MJ 14/10 | CUBRE (proforma ya no se aprueba sola) |

### Ventas

| Pedido | Quién | Marca |
|---|---|---|
| OV, Guardar valida stock, CONFIRMADA, facturar en Emitir | Reu6 + D4 | CUBRE |
| Sin cadena OV | D4 ratificado | CUBRE |
| No vender bajo precio de compra del maestro | D16 | CUBRE |
| Cuenta solo al contabilizar el libro | Reu6 | PARCIAL (la OV aún puede guardar cuenta) |
| Emitir FACTURA/NC/ND/GUIA; PDF/XML | AGENTS + GoSocket | CUBRE ruta; PARCIAL lote 27 (GUF en tests, sin emitir contra 65) |

### Insumos

| Pedido | Quién | Marca |
|---|---|---|
| Guía mueve stock; recepción OC no | MJ | CUBRE recepción; CUBRE guía |
| Precio de la guía = precio de la OC | mapa 13/10 | CUBRE (`precio-guia-oc.util`) |
| Libro de guías; Recibo SII 30+32 | MJ 01/10, 14/10 | CUBRE código; PARCIAL (sandbox 502 en guía 57) |
| Cierre de bodega + cuentas por tipo + Excel cajas | MJ / mapa | CUBRE (asiento 20260007 en muestra 21/10) |
| Devolución solo ALM al precio de esa factura | MJ 01/10 | CUBRE (bodega ALM si existe en la empresa; precio de esa factura) |
| Promedio informativo (no pisa el movimiento) | mapa | CUBRE (solo ENTRADA_PROVEEDOR actualiza el promedio) |

### Contratistas

| Pedido | Quién | Marca |
|---|---|---|
| Ingreso > proforma > notificar > asociar DTE en compras | MJ 06/10 y 13/10 | CUBRE camino; PARCIAL campos predio/faena/cuartel |
| Cierre de mes: costo vs facturas por recibir aunque no haya factura | MJ 14/10 | CUBRE |
| Varias proformas, una factura; no parcializar | MJ 06/10 | CUBRE |
| Reversar vuelve ingreso a jefatura | MJ | CUBRE (ingresos ASOCIADO vuelven a PENDIENTE) |
| Haber del asiento a nombre del contratista | MJ 13/10 | CUBRE (auxiliar = razón social del contratista) |
| Cerrar mes con ingresos sueltos o reabrir | MJ 14/10 | PARCIAL |
| Labor > actividad automática | MJ/Rodrigo | DEUDA |

### Tesorería

| Pedido | Quién | Marca |
|---|---|---|
| Cartola import-only; asiento banco = cartola; pago sin asiento | 21/08 + 28/08 | CUBRE |
| Nómina por semana; no muta el DTE | Lupe 01/10 | CUBRE |
| Egresos calzan con la nómina | MJ/Lupe | CUBRE (post 13/10: error si no calza) |
| Flujo informado en pesos | 28/08 | CUBRE (totalesClp con TC del BC; marca Ver en pesos) |
| Anticipo productor: una sola tabla/pantalla | mapa | PARCIAL (Pago real; pantalla legacy) |
| Banco en línea | cliente lo dejó después | NO (acordado) |

### Contabilidad

| Pedido | Quién | Marca |
|---|---|---|
| Asientos de compra/venta/cierre en el mayor | MJ | PARCIAL (existen; poco spec e2e) |
| Tres monedas en el comprobante | MJ 28/08 y 14/10 | PARCIAL (columnas en vista; líneas no siempre convierten) |
| Borrar cuenta sin movimientos | MJ 01/10 | CUBRE |
| Glosa del usuario en todas las líneas; PDF de reportes con cabecera | MJ 01/10 y 14/10 | DEUDA |
| Cierre por módulo | MJ | PARCIAL (CTR + bodega + periodo; no un candado único) |

### GoSocket

Intención MJ Reu2: **libro de compras en línea**, no solo emitir.

| Pedido | Marca |
|---|---|
| Inbox GetDocument / GetReceivedDocument + sync periodo | CUBRE |
| PDF/XML recibido y emitido | CUBRE |
| Eventos 30 acuse, 32 recibo, 33 aceptación, 31 reclamo | CUBRE código; PARCIAL reglas (OC/proveedor) y 502 sandbox |
| Tipos 33, 52, 56, 61, 110, 111, 112 emisión | CUBRE ruta |
| Tipo 34 exenta `MntExe` | CUBRE |
| Resolución 154 en guía 52 | CUBRE |
| COMEX en 110-112 | CUBRE |
| Descuento de línea visible (DscRcgGlobal, caso 33-2) | CUBRE |
| Plan 27 documentos emitidos y revisados en PDF | PARCIAL (GUF del lote en tests; no se emitió al sandbox contra la factura 65) |
| Iofacturo / portal gráfico | DEUDA externa |
| CAF live SII | NO (sandbox) |

## Qué cambió después del mapa 13/10

Cerrados o subieron de deuda a cubre/parcial: proforma en libro sin crear OC; cierre de bodega; precio guía desde OC; recibo SII 30/32; resolución 154; COMEX 110; borrar cuenta vacía; calce de nómina; rechazo de auto-aprobación de proforma; hija en APROBADO; Excel de cajas; cuentas por tipo de movimiento.

## Deudas que el cliente sí pidió y siguen

1. Adjuntos en OC/venta y PDF en alta manual.
2. Dos vencimientos (neto e IVA) y tipo de cambio guardado en la OC.
3. Escalas distintas insumos vs servicios (madre vs hija).
4. (cerrado 21/10) Haber contratista al nombre.
5. (cerrado 21/10) Reversa de proforma devuelve el ingreso.
6. (cerrado 21/10) Flujo de caja en pesos.
7. (cerrado 21/10) Descuento 33-2 y MntExe en 34 en el GUF.
8. Emitir el lote 27 en sandbox y revisar PDF (GUF listo; no contra factura 65).
9. Glosa replicada y PDF de reportes contables.
10. (cerrado 21/10) Devolución ALM atada a bodega; promedio informativo.

## Conflictos de sala (no son bugs)

| Tema | Gana |
|---|---|
| Cotización CRUD vs solo referencia en OC | Corte D11: referencia. MJ Reu6 pidió moverla a compras. |
| Cadena OV | D4: no hay. |
| Hija al asociar factura (demo) vs hija al recepcionar guía (MJ) | MJ 14/10: nace en insumos con la guía. |
| Aprobación del ingreso diario vs de la proforma | MJ 06/10 cierra en la proforma. |
| Editar madre a la baja sin cadena | MJ dijo las dos cosas; no está cerrado. |

## Qué no pedir como “falta el ERP”

- Banco en línea y contabilidad electrónica al SII: el cliente lo dejó después.
- GoSocket no hace asientos internos ni mapeo de cuentas.
- Recibo SII 502 en sandbox no bloquea bodega ni cierre.
- NC/ND/34/110 contra la factura 65: no se emitieron a propósito para no romper el cuadre de la muestra.
