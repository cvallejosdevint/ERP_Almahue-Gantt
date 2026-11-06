# FAQs operativas - mes contable interempresa (octubre 2026)

## Emision DTE

### Por que Facturar one-click pone fecha de hoy?

El atajo Facturar sella `fecha: new Date()`. Para octubre usa Ventas > Emitir DTE con contexto `factura-ov` y la fecha de la OV (GAP-F3-01).

### Puedo anular desde Libro de ventas?

El modal Anulacion puede fallar con `property total should not exist` (GAP-F3-03). Workaround: wizard Nota de credito en Emitir DTE.

### Lookup de cobro no encuentra el folio 73 del SII

Antes solo buscaba folio interno. Desde el fix F4-01 acepta folio interno o `folioOficial`.

## Compras / OC

### Match Alerta MONTO_NO_COINCIDE con OC en USD

Si la OC esta en USD y la factura en CLP (o al reves) el Match queda en Alerta y bloquea Aceptar/Rechazar GoSocket. Dejar como ejemplo o emitir OC CLP alineada (caso 0016/0017).

### Contabilizar compra pide referencia o auxiliar

Las cuentas PROVEEDORES con `requiereRef`/`requiereAux` exigen tipo/folio y RUT en el asiento. El plan de compra/cartola ya envia esos campos (fix F4-05).

## Tesoreria

### La cartola no encuentra la cuenta banco

El match usa el nombre del banco del CSV contra cuentas `1-1-01-02*`. Tolera variantes ("Banco de Chile" vs "BANCO CHILE $") tras fix F4-02.

### Estado de cuenta no muestra la compra del mes

La CC de compra debe usar la fecha fiscal del DTE (`fechaDocumento`), no el dia en que se contabilizo (fix F4-03).

### Flujo de caja vacio / error incluirProyecciones

El front envia el flag; el back lo acepta (fix F4-04). Sin proyecciones solo muestra cartolas Contabilizadas + aperturas.

### Pago/cobro genera asiento PAGO?

No. El asiento de banco sale de la cartola (`CARTOLA:{id}`). El pago solo calza CC/aging.

## Contabilidad / cierre

### Que cierra Contabilidad > Periodos?

Solo el candado del mes contable (no se pueden nuevos asientos en ese periodo). Contratistas y bodega tienen su propio cierre/traspaso.

### Como reabrir un periodo cerrado?

Boton Abrir + motivo obligatorio.

### El boton Cerrar cerro otro mes

En la grilla, el contenedor padre a veces incluye filas vecinas. Confirmar en el modal el codigo del periodo (ej. 2026-10) antes de Si, cerrar periodo.
