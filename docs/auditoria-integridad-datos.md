# Auditoría de integridad de datos (UI vs Prisma)

**Alcance:** formularios Comercial, Compras, Insumos frente a `ERP/erp_back/prisma/schema.prisma`.  
**Fecha:** 2026-08-16 (actualizado mismo día: FKs inventario + flete canónico en código).  
**Objetivo:** cables sueltos **antes** de integrar GoSocket.

Tenant: toda fila de negocio lleva `empresaId`. Schema PostgreSQL `erp`.

---

## 1. Mapa de persistencia (lo que sí conecta)

| UI | Modelo / campos | Notas |
|---|---|---|
| Compras › OC | `OrdenCompra`: numero, fecha, proveedor/proveedorId, solicitante, moneda, neto, afacto, estado, departamento, cuenta/CC/elemento, `distribucionCc` JSON, `lineas` JSON, cadena aprobación | Formulario en `ComprasPages.tsx` persiste maestro proveedor |
| Compras › recepción / registro | `RecepcionOc`, `RegistroCompra` (match 3 vías) | |
| Ventas › OV (lista) | Filtra `DocumentoComercial.tipo = ORDEN_VENTA` | Alta/edición vía wizard Emitir `contexto=ov` |
| Ventas › Emitir | `DocumentoComercial` (folio, tipo, cliente, neto, iva, lineas, formaPago, vencimiento, receptor*, COMEX opcionales, referencia OC/NP) | Tipos UI: FACTURA/NC/ND/GUIA |
| Insumos › artículos | `Insumo`: codigo, familia, subfamilia, nombre, unidad, cuentaContableId, inventariable | No captura `stock` ni `costoPromedio` (correcto: viven en bodega/movimientos) |
| Insumos › bodegas | `Bodega`: codigo, nombre, activa, empresaId | |
| Insumos › movimientos | `MovimientoBodega`: `bodegaId` / `bodegaDestinoId` / `insumoId` (FK); `bodega`/`articulo` denormalizados (código/nombre) | UI envía ids; stock solo vía `StockInsumoBodega` |
| Admin › Empresas | `ventaBajoCosto`, `comercialRequiereAprobacion`, `comercialAprobacionDesde` | UI D16 solo opción `BLOQUEAR` |

---

## 2. Campos de UI que no guardan (o guardan mal) en BD

| # | Pantalla | Campo UI | Problema | Estado |
|---|---|---|---|---|
| U1 | Movimientos bodega | Bodega origen/destino | Antes el select usaba **`b.nombre`**. | **Resuelto (2026-08-16).** Persistencia y cruce de stock usan `bodegaId` / `bodegaDestinoId` (FK a `Bodega`). `bodega` queda como código denormalizado de lectura. UI: `InsumosPages` envía ids. Migración `20260816220000_movimiento_bodega_fks`. |
| U2 | Movimientos bodega | Artículo | Antes el select usaba **`i.nombre`**. | **Resuelto (2026-08-16).** `insumoId` obligatorio en create/update; lookup por nombre eliminado. `articulo` = nombre denormalizado. |
| U3 | OV / Emitir | Splits de bodega | El TO-BE pide `splits[{bodegaId, cantidad}]` en líneas. | **Parcial / resuelto en backend:** OV confirma stock con `splits`/`bodegaId` + `insumoId` (misma transacción). Seguir validando en QA que el wizard siempre envíe ids. |
| U4 | Empresas | `ventaBajoCosto` | Select sin `PERMITIR`; comentario Prisma menciona valor legado. No exponer ni usar ese legado. | Abierto |
| U5 | Plantilla documentos | Preview logo/sello/`plantillaDoc` | JSON en `Empresa`; no es DTE. No confundir con GoSocket. | Abierto |
| U6 | Guías | `GuiasDespachoPage` vs tipo GUIA en Emitir | Dos caminos: `GuiaDespacho` vs `DocumentoComercial` tipo GUIA. Riesgo de doble verdad. | Abierto |
| U7 | Compras OC | `proveedor` texto denormalizado | Se rellena desde maestro; si el usuario edita nombre a mano, diverge de `proveedorId`. | Abierto |
| U8 | Modo demo (toggle front) | Fixtures | Pueden mostrar campos que **no** pegan a API real. No usar demo como evidencia de persistencia. | Abierto |

---

## 3. Tablas / columnas de BD sin captura adecuada

| # | Prisma | Obligatorio / relevante | UI |
|---|---|---|---|
| D1 | `StockInsumoBodega` | Saldo venta (único serio) | Sin mantenedor de stock (correcto). Deltas solo por `empresaId`+`insumoId`+`bodegaId`. |
| D2 | `MovimientoBodega.insumoId` | Trazabilidad | **Resuelto:** form + API exigen `insumoId`. |
| D3 | `MovimientoBodega.parId` | Pareja traslado/salida | Interno; UI no lo muestra (aceptable si el API lo genera). |
| D4 | `DocumentoComercial` COMEX (puerto, cláusula, vía, etc.) | Exportación MJ | Wizard: bloque condicional; no auditado vs canonical DTE. |
| D5 | `Cliente.tipoCliente` NACIONAL/EXPORTACION | Reu4 | Verificar si ficha lo persiste siempre. |
| D6 | `AnticipoProductor` | Tesorería productor | Fuera de Comercial/Compras/Insumos; sin captura en estos módulos. |
| D7 | `Prospecto` | Modelo existe | Menú no debe revivir prospectos fantasma (H4). |
| D8 | `Insumo.stock` / `costoPromedio` | Legado | Form no los edita (bien). Lecturas de listado no deben vender con `Insumo.stock`. |
| D9 | `Empresa.logoUrl` / `selloUrl` / dirección | Plantillas | Admin empresas: confirmar si el form de D16 incluye domicilio/logo o solo flags. |
| D10 | `AprobacionOv` | Cadena comercial | UI bandeja existe; flag empresa a menudo desactiva el camino. |

---

## 4. Plan de refactorización (pre-GoSocket)

Orden. Los pasos 1, 2 y 4 quedaron **resueltos en código** (local, 2026-08-16).

1. **Identificadores de inventario — RESUELTO**  
   Movimientos y `StockInsumoBodega` cruzan solo con `bodegaId` + `insumoId` + `empresaId`. Nombres/códigos no resuelven stock. `requireBodega` / `requireInsumo` en `stock-bodega.util.ts`. Front de movimientos envía FKs.

2. **Líneas OV canónicas — RESUELTO (backend)**  
   Producto: `insumoId`, `splits[{ bodegaId, cantidad }]`, `tipoLinea`. Flete: `tipoLinea: FLETE` (legado `RECARGO` se normaliza a FLETE) como **línea explícita** en el JSON de `DocumentoComercial.lineas`; no mueve stock. Confirmación OV y NC usan las mismas FKs.

3. **Una verdad de guía — pendiente**  
   Elegir: `GuiaDespacho` es proyección de un `DocumentoComercial` tipo GUIA, o al revés. Evitar dos folios.

4. **Canonical DTE vs flete — RESUELTO**  
   `buildCanonicalFromDocumento` emite flete como línea de detalle (descripción prefijada «Flete · …»), no recargo SII. `BillingGatewayClient.emit` solo stub local (sin HTTP GoSocket).

5. **Stub estable — pendiente QA**  
   Timeout/error simulable; el front no debe colgar el wizard si el stub falla (caso QA).

6. **Tenant y concurrencia — pendiente**  
   Confirmar OV: lock por `(empresaId, insumoId, bodegaId)` o equivalente. Dos sesiones no pueden dejar stock negativo.

7. **Recién entonces GoSocket — no iniciado**  
   Credenciales, mapeo folio SII, XML/PDF partner, reenvío libro. No mezclar con carga Acepta ni SMTP.

---

## 5. Fuera de alcance de esta auditoría

Tesorería, contabilidad profunda, contratistas, workflows-admin legacy. No inventar UI de productor-maestro.
