# Estado huérfanos H1–H14 (Reu6 vs código)

**Fecha corte:** 2026-08-14 (actualizado sesión cierre)  
**Fuente plan:** sesión auditoría Reu4–6 + `qa/resultados/2026-08-14-fase1-as-is-to-be.md`

Leyenda: **Listo** · **Parcial** · **Bloqueado externo** · **Diferido**

| ID | Huérfano | Estado | Notas |
|---|---|---|---|
| **H1** | Productor en lookup RUT | **Listo** | Flag `esProductor` en Cliente/Proveedor; lookup devuelve `productor` y arreglo `productores[]`. |
| **H2** | UI `ventaBajoCosto` | **Listo** | Admin › Empresas: bloqueo bajo costo + flags aprobación OV. |
| **H3** | Aprobación comercial OV | **Listo (off)** | Código + propuesta `04-PROPUESTA-APROBACIONES-COMERCIAL.md`; activar tras reunión (`comercialRequiereAprobacion`). |
| **H4** | `pantallas-permisos` vs Sidebar | **Listo** | Catálogo alineado: OV, Aprobaciones, Guías; Cotizaciones en Compras; sin Prospectos fantasma. |
| **H5** | PDF ficha solicitud | **Listo** | Print HTML «Imprimir solicitud» en `FichaContraparteModal` (piloto sin PDF servidor). |
| **H6** | Flag inventariable + AlmaWeb | **Listo (base)** | Campo `inventariable` en maestro; OV omite bodega/stock si false. Integración AlmaWeb = proyecto externo. |
| **H7** | NC → reingreso bodega | **Listo** | Al contabilizar NC: movimiento `DEVOLUCION_NC` + delta positivo; signo corregido en movimientos manuales. |
| **H8** | Guías despacho UI | **Listo** | Ventas › Guías de despacho (`/comercial/guias-despacho`); emisión vía Emitir (tipo GUIA). |
| **H9** | SMTP correo PIN | **Bloqueado externo** | Infra Almahue (Reu5 diferido). |
| **H10** | 3 cotizaciones comparativas compras | **Diferido** | No es proceso actual (Reu4 ideal futuro). |
| **H11** | GoSocket / DTE real | **Listo (stub)** | `billing/` + canonical + disclaimer stub; conexión real en proyecto aparte (datos brutos) — **no bloqueante**. |
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

## Resumen

- **Listos en código:** H1–H8, H11 (stub), H14 (checklist).
- **Externos / no deuda:** H9, H12, H13, H10.
