> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md) + código. Motivo: levantamiento Reu1 («jefe aprobador»); no spec ERP actual.

# Módulo: Compras (servicios)

Flujo real: **Crear OC → Aprobación → Recepción (reconoce gasto + TC) → Registro compra (factura)**.
Sin Solicitud de Compra (**DEC-02**).

## Pantalla: Orden de Compra (formulario único)

- **Timestamp:** 29:33–43:46
- **Captura:** `../pantallas-legacy/06-orden-compra.png`
- **Etiqueta:** REQ

### Campos REQ
Departamento, Solicitante, Fecha, Jefe aprobador, Proveedor, Tipo pago, Moneda, Observación, líneas (artículo servicio, cantidad, precio, CC), selector Afecto/Exento (ver PEND-01).

### As-Is
- Siempre eligen “sin solicitud”.
- TC mostrado al crear **no** es el que se usa al registrar (se usa fecha de recepción).
- Distribución CC: sin alerta temprana de descuadre; “Por Hectárea” es todo-o-nada y errores quedan eternos.
- CC de otras empresas seleccionables.

### To-Be
- [DEC-02] Sin campo Solicitud.
- [REQ] TC de creación solo informativo; gasto/TC efectivos en recepción (documentar).
- [REQ] Distribución: validación en tiempo real suma = neto; bloquear guardar si descuadra. Captura `../pantallas-legacy/07-distribucion-cc.png` @ 40:30.
- [REQ] Modo Directo (CC + elemento + monto). Modo Por Hectárea: edición granular de cuarteles (problema a resolver, no spec inventada).
- [REQ] CC solo empresa activa.
- [PEND-01] Política Afecto/Exento vs facturas mixtas / impuesto específico.

---

## Pantalla: Listado / informe OC

- **Timestamp:** 43:38–46:16
- **Etiqueta:** REQ

### To-Be
- [REQ] Búsqueda por número independiente del estado.
- [REQ] Búsqueda por proveedor también en contabilizadas (mostrar proveedor).
- [REQ] Orden reciente→antigua por defecto.
- [OPT] PDF automático al crear.

---

## Pantalla: Aprobación

- **Timestamp:** 48:03–50:31
- **Captura:** `../pantallas-legacy/08-aprobacion-oc.png`
- **Etiqueta:** REQ

### To-Be
- [REQ] Badge/visual de pendientes (prefieren no spamear correo).
- [REQ] Aprobar/Rechazar con detalle de líneas y CC.
- [OPT] Historial.

---

## Pantalla: Recepción

- **Timestamp:** 51:00–54:51
- **Captura:** `../pantallas-legacy/09-recepcion-oc.png`
- **Etiqueta:** REQ

### As-Is
- Al recepcionar se genera asiento (gasto vs facturas por recibir) con TC del día de recepción.
- Productores: a veces TC **promedio** sin fecha exacta → diferencia vs pago (tesorería permite TC manual).

### To-Be
- [REQ] Mostrar TC que se aplicará antes de confirmar.
- [REQ] Asiento trazable a OC.
- [REQ] Nota especial productores (PEND política TC).

---

## Pantalla: Registro de compra (factura)

- **Timestamp:** 54:51–01:03:15
- **Captura:** `../pantallas-legacy/10-registro-compra.png`
- **Etiqueta:** REQ

### As-Is
- Permite contabilizar **cruzado** (mismo monto, otro proveedor).
- Modificar TC en factura solo afecta proveedor, no el costo.
- Dejó asociar factura afecta a OC exenta.

### To-Be
- [REQ] Proveedor factura = proveedor OC.
- [REQ] Bloquear cruzado por monto.
- [REQ] Decidir/aplicar política Afecto-Exento (PEND-01); al menos alertar inconsistencias.
- [REQ] Preferir corregir TC en recepción, no parche en factura.
