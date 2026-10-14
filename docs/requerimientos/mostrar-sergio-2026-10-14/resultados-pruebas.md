# Resultados de pruebas: qué mostrar el 14/10/2026

Fecha: 2026-10-14. Fuentes: `plan-pruebas.md` y `contraste-codigo.md`.

No se abrió el ERP. No se escribió en la base. No se emitió un DTE, no se pagó, no se cerró el mes, no se envió correo y no se corrió prisma migrate deploy. Los veredictos de la tabla salen del contraste de código. Esta pasada solo corrió specs unitarios.

## Comandos

### 1. Jest, patrón asociar-oc-registro.util

Directorio: `ERP/erp_back`.

```
npx jest --runInBand --testPathPattern="asociar-oc-registro.util"
```

Resultado: **failed**. Exit 1. `No tests found`. Jest revisó 230 archivos en `src`. 67 coinciden con `.*\.spec\.ts$`. 0 coinciden con el patrón. El spec que cita el contraste no vive en el back: es `ERP/erp_front/src/features/compras/asociar-oc-registro.util.node.spec.ts` y usa el runner de Node, no Jest.

Ese archivo se corrió aparte, porque cubre el combo de OC y el texto del aviso:

```
node --experimental-strip-types --test src/features/compras/asociar-oc-registro.util.node.spec.ts
```

Directorio: `ERP/erp_front`.

Resultado: **passed**. Exit 0. 2 pruebas, 0 fallos, unos 203 ms.

- mantiene la OC del mismo proveedorId aunque la razón social no coincida
- nombra proveedor y monto y no habla de enviar correo

No hizo falta corregir el test ni el filtro. El combo conserva la OC del mismo proveedor.

### 2. Jest, compras.service.spec, solo notificar

Directorio: `ERP/erp_back`.

```
npx jest --runInBand --testPathPattern="compras.service.spec" --testNamePattern="notificarRegistroCompra"
```

Resultado: **passed**. Exit 0. 2 passed, 92 skipped, 94 en el archivo. Unos 8 s.

El patrón de ruta también nombra `oc-parcial.compras.service.spec.ts`. Ese archivo quedó skipped: ningún nombre coincidió con `notificarRegistroCompra`. No se corrió `compras.service.spec` entero. Quedaron fuera los fallos viejos de asiento sin cuenta y del inbox GoSocket.

Casos que pasaron:

- usa logo/firma de VENTAS si COMPRAS no los tiene y adjunta CID
- con la casilla de correo apagada deja el aviso y no encola SMTP

El segundo cubre el cambio de hoy: con `enviarCorreo` en false no se encola el correo. No hizo falta corregir el test.

En este spec no hay un caso de OC candidata ni de proforma. El combo está en el spec de Node del punto 1. La proforma entera está en el contraste.

### 3. Spec de proforma que no se parte en hija

No se ejecutó. En `ERP/erp_back`, entre los `*.spec.ts`, no hay un caso que diga que la proforma no se parte en hija.

`contratistas.service.spec.ts` tiene el describe `EX-20 asociarFacturaProforma N>1` ("genera una sola OC en Compras y enlaza varias proformas"). Ese caso arma una OC. No dice que la proforma quede entera sin hija, y no se corrió.

## Tabla P-1-01 a P-5-03

El veredicto es el del contraste. Ninguna fila se cerró abriendo una pantalla ni leyendo la base.

| Prueba | Veredicto | De dónde sale |
|---|---|---|
| P-1-01 | cumple | Contraste: glosa, auxiliar sin dígito y IVA débito. No se abrió el asiento 20260041. |
| P-1-02 | cumple | Contraste: columnas peso, dólar y yuan. No se abrió el comprobante. |
| P-1-03 | parcial | Contraste. Pendiente: la compra no arma una línea de comprobante por cada línea de la OC. |
| P-1-04 | solo mostrar | Contraste: balance de 8 columnas y libro diario. No se abrieron. |
| P-2-01 | parcial | Contraste. Pendiente: el ingreso diario no tiene forma de pago ni duración. |
| P-2-02 | parcial | Contraste. Pendiente: la pantalla de proformas sigue ofreciendo Generar OC. |
| P-2-03 | cumple | Contraste: no hay proforma hija. No existe un spec de ese caso y no se corrió. |
| P-3-01 | cumple | Contraste y spec de Node: el combo deja la OC del mismo proveedorId. |
| P-3-02 | cumple | Contraste: madre e hija en el listado de Compras. No se abrió el listado. |
| P-3-03 | cumple | Contraste: la OC queda en el registro de compra. La guía no tiene ocId. |
| P-4-01 | cumple | Contraste: varias proformas suman en el mismo registro y no piden cuenta. |
| P-4-02 | solo mostrar | Contraste: la asociación no escribe cuenta. No se inventó una. |
| P-5-01 | cumple | Contraste, spec de Node (texto con proveedor y monto) y Jest (casilla apagada, sin SMTP). |
| P-5-02 | parcial | Contraste. Pendiente: Notificar contratista marca enviada sin correo. |
| P-5-03 | solo mostrar | Contraste: plantilla VENTAS. No se abrió ni se grabó. |

## Pendientes que no se implementan

El contraste dejó cuatro parciales. Esta pasada no los cierra:

- Compra línea por línea (P-1-03). El preview toma la primera línea con cuenta o centro, no una línea de comprobante por cada línea de la OC.
- Ingreso diario sin forma de pago ni duración (P-2-01). Esos campos no están en el ingreso.
- Botón Generar OC de la proforma (P-2-02). La pantalla de proformas sigue ofreciéndolo.
- Notificar contratista marca la proforma enviada sin correo (P-5-02).

## Conteo

15 filas. **8 cumple**, **4 parcial**, **0 no cumple**, **3 solo mostrar**, **0 no ejecutado**.
