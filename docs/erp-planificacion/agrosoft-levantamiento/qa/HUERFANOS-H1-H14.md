# Estado huérfanos H1–H14 (Reu6 vs código)

**Fecha corte:** 2026-08-14 (H3 18/08; H11 HTTP+CAF 19/08)  
**Fuente plan:** HUERFANOS + P0 17/08 + ciclo 18/08. El as-is 14/08 está `{deprecado}`.

Leyenda: **Listo** · **Parcial** · **Bloqueado externo** · **Diferido**

| ID | Huérfano | Estado | Notas |
|---|---|---|---|
| **H1** | Productor en lookup RUT | **Listo** | Flag `esProductor` en Cliente/Proveedor; lookup devuelve `productor` y arreglo `productores[]`. |
| **H2** | UI `ventaBajoCosto` | **Listo** | Admin › Empresas: bloqueo bajo costo + flags aprobación OV. |
| **H3** | Aprobación comercial OV | **Listo (on en seed/default local)** | `comercialRequiereAprobacion` default true; seed EMP-1; migración `20260818180000_comercial_aprobacion_piloto_on` (`comercialAprobacionDesde=0`). Prod = reunión + migrate (H14). |
| **H4** | `pantallas-permisos` vs Sidebar | **Listo** | Catálogo alineado: OV, Aprobaciones, Guías; Cotizaciones en Compras; sin Prospectos fantasma. |
| **H5** | PDF ficha solicitud | **Listo** | Print HTML «Imprimir solicitud» en `FichaContraparteModal` (piloto sin PDF servidor). |
| **H6** | Flag inventariable + AlmaWeb | **Listo (base)** | Campo `inventariable` en maestro; OV omite bodega/stock si false. Integración AlmaWeb = proyecto externo. |
| **H7** | NC → reingreso bodega | **Listo** | Al contabilizar NC: movimiento `DEVOLUCION_NC` + delta positivo; signo corregido en movimientos manuales. |
| **H8** | Guías despacho UI | **Listo** | Ventas › Guías de despacho (`/comercial/guias-despacho`); emisión vía Emitir (tipo GUIA). |
| **H9** | SMTP correo PIN | **Bloqueado externo** | Infra Almahue (Reu5 diferido). |
| **H10** | 3 cotizaciones comparativas compras | **Diferido** | No es proceso actual (Reu4 ideal futuro). |
| **H11** | GoSocket / DTE real | **Parcial (HTTP + CAF pendiente)** | Cliente HTTP ERP→`billing-gateway`→sandbox `developers-sbx` (19/08). Fail-closed si REJECTED. **Bloqueo:** CAF/cert MJ. SII live = no. No reabrir «falta GoSocket». |
| **H12** | Carga masiva Acepta | **Bloqueado externo** | MJ ↔ Acepta en curso. |
| **H13** | Excel cartolas finas | **Bloqueado externo** | Plantilla banco MJ (R4-16). |
| **H14** | Deploy prod OV/stock | **Listo (doc)** | `DEPLOY.md` + `DEPLOY-PROD-FASE2.md`; migrate pendiente ejecución en `45.7.229.46`. |

## También cerrados (no numerados en H1–H14)

| Tema | Estado |
|---|---|
| Emitir solo FACTURA/NC/ND/GUIA (sin COTIZ/NP/OC) | **Listo** |
| OV → stock → factura (D11–D17) | **Listo** en local; prod con migrate H14 |
| Redirect `/comercial/cotizaciones` → Compras | **Listo** |

## Migraciones pendientes de `migrate deploy` (local/prod)

Incluyen OV/aprobación y huérfanos de esta sesión — **no aplicar en prod** hasta acuerdo reunión:

- `20260813230000_stock_ov_ficha`
- `20260814180000_comercial_aprobacion_ov`
- `20260814180000_tipo_doc_nd_guia`
- `20260815200000_huerfanos_ficha_inventario`
- `20260818180000_comercial_aprobacion_piloto_on`

## Resumen

- **Listos en código:** H1–H8, H14 (checklist). **H11:** HTTP+fail-closed listo; ACCEPTED/SII bloqueado por CAF.
- **Externos / no deuda:** H9, H12, H13, H10.
