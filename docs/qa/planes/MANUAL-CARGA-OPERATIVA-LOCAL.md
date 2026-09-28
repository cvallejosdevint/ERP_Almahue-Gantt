# Manual de carga operativa local (compras → ventas → tesorería → contabilidad)

Uso: datos locales ya limpios. Quedan las facturas/NC/ND que **sí se enviaron al SII** (aceptadas o rechazadas) y su OV, asiento y cuenta corriente. Parametrización (cuentas, conceptos, códigos, periodos, Config SII) no se toca ni se explica aquí.

- Front: http://localhost:5174
- Usuario: `admin@almahue.local` / `Admin123!` · PIN `4821`
- Empresa: **ALMAHUE EXPORT SPA**
- Periodo del banner: el mes en el que estás trabajando. Para la cartola nueva usa **2026-09**.
- Archivo de cartola: `E:\source\repos\Almahue\09-CARTOLA_SEPTIEMBRE_2026.xls` (misma cantidad de movimientos que junio; montos un 7 % distintos; fechas corridas a agosto/septiembre).

Cada listado (OC, libro, flujo, cartola, nómina, asientos, etc.) muestra **solo el mes del banner**. El botón **Todo** está en **esa pantalla**, no en el banner: sirve para ver otros meses sin cambiar el mes de trabajo.

---

## 1. Fijar empresa y mes

En el banner superior elige **ALMAHUE EXPORT SPA** y el periodo **2026-09** (Septiembre · ABIERTO).

**Significado en el flujo del negocio:** todo lo que cargues queda en la sociedad y en el mes contable con los que vas a cerrar caja y libros. Si el banner dice septiembre, las listas vacías no significan que “no hay sistema”: significan que ese mes aún no tiene operación tuya.

---

## 2. Compras · Orden de compra

1. Menú **Compras › Órdenes de compra**.
2. **Nueva**. Completa proveedor (ficha real, no QA), fecha del mes del banner, ítems y montos.
3. **Guardar borrador** si aún no está lista; **Enviar a aprobación** cuando sí.

**Significado en el flujo del negocio:** la OC es el compromiso de compra. Hasta que no esté aprobada, no es deuda pagable ni se contabiliza una factura de proveedor contra ella como operable.

---

## 3. Compras · Aprobar la OC

1. **Compras › Aprobaciones**.
2. Abre la OC pendiente e ingresa el **PIN** (`4821` en este ambiente).
3. Aprueba el paso que te corresponda.

**Significado en el flujo del negocio:** alguien con potestad autorizó gastar. Recién ahí la empresa puede recibir mercadería y, más adelante, pagar la factura del proveedor.

---

## 4. Compras · Recepción de la OC

1. **Compras › Recepciones** (o **Recepcionar** desde la OC aprobada).
2. Confirma cantidades recibidas.

**Significado en el flujo del negocio:** dejas constancia de que llegó lo pedido. **No mueve stock**: la bodega se carga en el paso siguiente.

---

## 5. Insumos · Entrada a bodega

1. **Insumos / Bodega › Movimientos**.
2. Alta **ENTRADA_PROVEEDOR** con la misma fecha del mes, bodega e ítem de la OC.

**Significado en el flujo del negocio:** el producto ya está en la bodega para usarlo o venderlo. Sin esta entrada, una orden de venta posterior puede fallar por falta de stock.

---

## 6. Compras · Factura del proveedor (Libro de compras)

1. **Compras › Libro de compras**.
2. Asocia la factura recibida a la OC (folio, fecha, montos).
3. Con permiso de escritura, **contabiliza** (cuentas por ítem si el sistema las pide).

**Significado en el flujo del negocio:** nace la deuda con el proveedor (cuenta por pagar) y el asiento de compra. Eso es lo que más tarde aparece en **Nómina** para programar el pago.

---

## 7. Ventas · Orden de venta

1. **Ventas › Órdenes de venta**.
2. Nueva OV: cliente, fecha del mes del banner, productos, precios (no bajo el precio de compra del maestro).
3. **Guardar** (valida stock). Queda **CONFIRMADA**.

**Significado en el flujo del negocio:** tomaste un pedido y reservaste/saliste mercadería. Todavía no es factura SII: el cliente aún no tiene DTE.

---

## 8. Ventas · Emitir DTE

1. **Ventas › Emitir DTE**.
2. Elige una OV tuya del mes (si no aparece, **Todo** en esa pantalla para ver otras).
3. Revisa cabecera y líneas. **Emitir**.

**Significado en el flujo del negocio:** sale el documento tributario hacia el facturador/SII. El cliente ya tiene factura (o NC/ND). En este ambiente el DTE queda **emitido**; la contabilidad interna se completa en el libro.

---

## 9. Ventas · Contabilizar en Libro de ventas

1. **Ventas › Libro de ventas**.
2. Filtra **Por contabilizar** (DTE `EMITIDO` sin asiento).
3. Abre el documento, asigna **cuenta por ítem** y **Guardar**.

**Significado en el flujo del negocio:** la venta entra a la contabilidad (ingreso + IVA + cuenta por cobrar). Recién ahí el estado de cuenta del cliente refleja la deuda y el libro diario tiene el asiento `DOC:…`.

---

## 10. Tesorería · Importar cartola del banco

1. Banner en **2026-09**.
2. **Tesorería › Cartolas › Importar Excel/CSV/PDF**.
3. Sube `09-CARTOLA_SEPTIEMBRE_2026.xls`.
4. Revisa hojas (CLP / USD / Yuan) y confirma el mes contable **2026/09**.
5. Importa.

**Significado en el flujo del negocio:** cargas lo que el banco dice que se movió. Todavía no es contabilidad ni flujo de caja: es el extracto crudo.

---

## 11. Tesorería · Contabilizar cada movimiento de cartola

En el detalle de la cartola, para cada línea (o lote de egresos):

1. Destino (factura, otro, sueldo, etc.).
2. Contracuenta, **código financiero** y, si es egreso a proveedor, **semana de nómina** `2026-09-S1` … `S4`.
3. **Contabilizar**.

**Significado en el flujo del negocio:** le pones sentido de negocio al movimiento bancario: cobro de cliente, pago a proveedor, sueldo, traspaso. Eso alimenta el **flujo de caja** (por fecha y código) y, si marcaste semana, el vínculo con la **nómina**.

---

## 12. Tesorería · Nómina semanal

1. **Tesorería › Nómina semanal**.
2. **Sincronizar** (trae facturas de compra contabilizadas por pagar).
3. Revisa la semana del mes del banner. Si ves vacío y el aviso de otras semanas, pulsa **Todo** en **esta** pantalla, no cambies el banner.
4. Aplaza o deja en la semana de compromiso. El pago no se hace aquí.

**Significado en el flujo del negocio:** es la lista interna de “esta semana hay que pagar esto”. No cambia el folio ni el vencimiento del DTE del proveedor; solo organiza la caja de la semana.

---

## 13. Tesorería · Registrar el pago o cobro

1. **Tesorería › Pagos › Nuevo pago** (o **Calzar** desde cartola / factura).
2. Elige proveedor o cliente, monto, medio. Si viene de cartola, conserva la referencia del movimiento.
3. Calza el folio de la factura de compra o de venta.

**Significado en el flujo del negocio:** se extingue (o baja) la deuda: el proveedor cobra o el cliente paga. La cuenta corriente y la nómina muestran menos saldo pendiente. No se genera un asiento extra `PAGO:…`; el banco ya se contabilizó en la cartola.

---

## 14. Tesorería · Flujo de caja y estado de cuenta

1. **Tesorería › Flujo de caja**: mira ingresos/egresos del mes (botón **Todo** solo si quieres el panorama de todos los meses).
2. **Tesorería › Estado de cuenta**: saldos de clientes y proveedores hasta el mes del banner.

**Significado en el flujo del negocio:** el flujo dice cómo se movió la caja por concepto (cereza, proveedores, etc.). El estado de cuenta dice quién te debe y a quién le debes. Si un movimiento de cartola no tiene código financiero, no va a armar bien el flujo.

---

## 15. Contabilidad · Ver el efecto (no parametrizar)

1. **Contabilidad › Asientos**: deben aparecer los `DOC:…` de ventas contabilizadas, `COMPRA:…` de facturas de proveedor y `CARTOLA:…` de extractos.
2. **Libro diario** / **Mayor**: mismo mes del banner ( **Todo** en esa pantalla para ver todos los periodos).

**Significado en el flujo del negocio:** es el libro legal interno. Si el asiento no está, el hecho de negocio (compra, venta o banco) todavía no está reflejado en contabilidad, aunque el documento exista en compras o ventas.

---

## Orden mínimo para un ciclo coherente

1. OC → aprobación → recepción → entrada de bodega → factura de compra contabilizada.  
2. OV → Guardar → Emitir DTE → contabilizar en libro de ventas.  
3. Importar cartola del mes → contabilizar líneas con código financiero.  
4. Sincronizar nómina → pagar/calzar.  
5. Revisar flujo, estado de cuenta y asientos.

Si saltas la contabilización del libro, la nómina y el estado de cuenta quedan vacíos. Si saltas el código financiero en cartola, el flujo queda vacío aunque el banco tenga movimientos.
