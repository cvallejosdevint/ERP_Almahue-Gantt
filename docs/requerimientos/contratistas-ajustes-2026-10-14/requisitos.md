# Requisitos - Jose y Sergio 2026-10-14

Fuente hablada: `docs/reuniones/transcripciones/transcripcion-2026-10-14-jose-sergio.md` (Whisper large-v3 local, 26 min).
Maria Jesus 13/10: `docs/reuniones/transcripciones/transcripcion-2026-10-13-gosocket-almahue.md` [06:21] a [08:54].
Word de Maria Jesus (13/10 13:20): ficha con ciudad y comuna; tras guardar el ingreso, pasa a movimientos por aprobar; en asociacion se elige proveedor, facturas y proformas aprobadas.

## Lista que hay que corregir

1. Ciudad y comuna obligatorias en la ficha de contratistas.
2. Editar una tarifa actualiza la fila vigente. No abre otra.
3. La cuenta de gasto se asocia en la proforma. El traspaso la usa como debe. La factura del proveedor sigue asociandose en Compras.
4. Pantalla Contratistas > Aprobaciones. En el ingreso diario se muestra la cadena segun el monto y el grupo de Contratistas del usuario, igual que en la OC.

## Lo que la reunion agrega y esta lista no traia

- Seguimiento del envio de la proforma (fecha, de quien, a quien). Quedo anotado, no en este ajuste.
- El correo de la proforma debe adjuntar el documento, como Compras adjunta XML y PDF. Quedo anotado, no en este ajuste.
- Solo una proforma aprobada se puede asociar a la factura. El match es manual por RUT, con sugerencia por monto, porque el XML no trae la proforma. La asociacion N proformas a una factura ya existe en el libro.
- Orden madre: la hija queda aprobada; si el monto supera a la madre, la madre vuelve a aprobacion. La madre no se contabiliza si ya tiene hijas. Numeracion con guion 1 y columna de origen, como el libro de ventas. Fuera de este ajuste de contratistas.
- Exportar a PDF libro diario, libro mayor y balance de ocho columnas, con periodo y datos de la empresa. Fuera de este ajuste.
