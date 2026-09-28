# Matriz AS-IS / TO-BE (conversaciones + código)

**Fecha:** 2026-08-16  
**Conversaciones:** transcripciones Reu1–Reu6 depuradas en [`transcripcion-limpia-v2.md`](transcripcion-limpia-v2.md).  
**Minutas:** Reu6 > Reu5 > Reu4.  
**No copiar ciega** la matriz de 2026-07-31 (`qa/historico-reu4/10-AS-IS-TO-BE-OPERATIVO.md`): D11, stub DTE y stock por bodega ya cambiaron.

**Piloto local:** front `5174`, API `3001`, Postgres típico `5433`, `BILLING_STUB_INLINE`.  
**Prod:** `http://45.7.229.46/almahue-erp/` — no asumir migrate OV/stock hasta H14.

Sin concepto de mermas.

---

## Resumen

| Estado | Lectura |
|---|---|
| **OK piloto** | Login/tenant, OC + bandeja, OV local (confirmar stock), insumos base, stub DTE, ficha contraparte, grupos/escalas OC |
| **Parcial** | Aprobación OV (código listo, flag empresa a menudo off), SSO Microsoft, plantillas documento, tesorería/contabilidad en demo cliente |
| **Gap / cable** | Movimiento bodega por **nombre** vs `StockInsumoBodega` por id; canonical DTE vs flete; pantallas vs menú puede re-desfasarse |
| **Diferido / externo** | GoSocket real, Acepta, SMTP, Excel AlmaWeb/cartolas, temporada puente |

---

## Matriz

| ID | Área | TO-BE (conversación) | AS-IS (código 2026-08) | Estado | Piloto | Prod |
|---|---|---|---|---|---|---|
| ADM-01 | Usuarios | Admin en ERP; multi-empresa | Panel Admin › Usuarios + `UsuarioEmpresa` | OK | Sí | Sí |
| ADM-02 | Roles | Lectura/escritura por pantalla | `permisos` + `permisosPantalla` | OK | Sí | Sí |
| ADM-03 | Super admin | Ve todo; puede aprobar con aviso | Rol master + bandeja | OK | Sí | Sí |
| AUTH-01 | SSO Microsoft | Login Entra | Campo `microsoftOid`; botón hasta `.env` | Parcial | Sí (local pwd) | Parcial |
| APB-01 | Cadena OC | Organigrama + montos + PIN | Grupos/escalas; PIN en reglas | OK | Sí | Sí |
| APB-02 | Cadena OV | Misma lógica comercial | `AprobacionOv` + flag `comercialRequiereAprobacion` (default false) | Parcial | Decisión piloto | No asumir |
| CMP-01 | Cotización | Proveedor → OC | `COTIZACION` en Compras | OK | Sí | Sí* |
| CMP-02 | OC | Afecto, CC, aprobación, recepción | `OrdenCompra` + recepción + registro | OK | Sí | Sí* |
| VEN-01 | OV | Previa a factura; stock al confirmar | `ORDEN_VENTA` + `confirmarOrdenVenta` | OK local | Sí | H14 |
| VEN-02 | Factura | Copia qty/desc; precio editable | Wizard Emitir FACTURA desde OV | OK local | Stub | Stub |
| VEN-03 | Libro | Solo emitidos; sin botón emitir | Libro + print local | OK | Sí | Parcial XML |
| VEN-04 | Bajo costo | Bloquear por empresa | `Empresa.ventaBajoCosto` UI Admin (solo BLOQUEAR) | OK | Sí | Sí |
| INV-01 | Stock venta | Positivo por bodega | `StockInsumoBodega` | OK | Sí | H14 |
| INV-02 | Movimientos | Tipos + NC reingreso | UI movimientos; bodega **texto** | Parcial | Sí | Sí |
| INV-03 | Inventariable | Servicio no mueve stock | Flag maestro + OV | OK | Sí | Sí |
| FIC-01 | Ficha única | Bancos, contactos, despacho | Modelos Cliente/Proveedor + modal | OK | Sí | Sí |
| FIC-02 | Lookup RUT | Sociedad/cliente/proveedor | API lookup; productor = flag | OK | Sí | Sí |
| DTE-01 | Emisión SII | GoSocket transparente | Stub billing; no SII | Diferido | Stub | No |
| CNT-01 | Plan cuentas | Flags + inactivar | Modelos + UI parametrización | OK base | Sí | Parcial demo |
| TES-01 | Cartola | Excel banco → calce | Parsers + conciliación base | Parcial | Sí | Excel MJ |
| OUT-01 | Cotiz ventas | No existe | Redirect `/comercial/cotizaciones` | OK | — | — |
| OUT-02 | Mano de obra / maquinaria | Fuera | No módulo | OK | — | — |

\*Prod: validar seed y migrate; no asumir paridad con local.

---

## Contradicciones resueltas

| Antes (Reu4/Reu5 o demo) | Ahora (Reu6 + código) |
|---|---|
| Cotización cliente → NP → factura | Cotización Compras → OC; Ventas = OV → factura |
| 1 firma pool | Cadena grupos/escalas |
| PIN en checkbox de rol | PIN por designación + hash usuario |
| GoSocket “en 2 semanas” | Stub suficiente para piloto; integración en proyecto aparte |
| UI venta bajo costo “sin pantalla” (deuda antigua) | Existe en Admin › Empresas (H2) |

---

## Lectura para integración GoSocket

No es el siguiente cable de **datos maestros**. Primero: persistencia coherente (bodega id, líneas OV, canonical flete), tenant, stub estable. Luego credenciales y espejo de folios. Ver [`auditoria-integridad-datos.md`](auditoria-integridad-datos.md).
