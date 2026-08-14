# Fase 1 — As-is / to-be (Reu6 vs código)

**Fecha:** 2026-08-14  
**Alcance:** contrastar minutas (Reu6 > Reu5 > Reu4) con `ERP/erp_back` + `ERP/erp_front`.  
**No se leyeron transcripciones.** Carlos/Sergio en demo = hipótesis.  
**Código visto:** implementación Reu6 comercial/inventario (OV, stock por bodega, cotización→OC) + módulos ya existentes.

Leyenda de estado: **cumple** · **parcial** · **no hay** · **diferido** · **contradicción** (doc de chat/minuta anterior vs código actual).

---

## 1. Decisiones Reu6 (D1–D20)

| ID | Pedido (minuta) | As-is (código) | To-be | Gap | Evidencia | Bloqueado |
|---|---|---|---|---|---|---|
| D1 | Usuarios desde el ERP; multi-empresa | **Cumple.** Admin › Usuarios; `UsuarioEmpresa`; header aísla tenant | Igual | — | `erp_front` Admin usuarios; `erp_back` admin usuarios | — |
| D2 | Super admin ve todas las empresas y puede aprobar con advertencia | **Cumple** (aprobaciones fase 2 + QA 12/13 ago) | Advertencia si no es el asignado | Verificar copy de advertencia en bandeja (no re-auditado hoy) | `approval-engine`, bandejas OC/proformas, rol `ROL-1` | — |
| D3 | Permisos por rol, no por empresa | **Cumple.** Variación = otro rol | No duplicar permisos por empresa en el mismo rol | — | `Rol.permisos`; no hay permisos por `empresaId` | — |
| D4 | Cadena secuencial automática por módulo/monto; Comercial reservado | **Parcial.** OC y proformas con grupos/escalas. Comercial (OV/factura) **sin** cadena de aprobación | Encadenar comercial cuando Almahue defina montos | Comercial reservado a propósito | `grupos-aprobacion`, `compras.service`, `contratistas.service` | Agustín/MJ: organigrama/montos |
| D5 | Quitar «Aprobar con PIN» del rol; PIN en reglas | **Cumple** (post-Reu6) | PIN solo designados + master | — | Perfil PIN; `RequireAprobacionesConfig`; skill aprobaciones | — |
| D6 | Montos + mando + suplencia | **Cumple** (grupos, escalas, delegaciones) | No elegir aprobador ajeno | Datos reales de organigrama aún de Almahue | `DelegacionAprobacion`, simulador | Almahue: definición |
| D7 | Bases cliente/proveedor separadas; lookup RUT unificado (sociedad/proveedor/cliente/**productor**) | **Parcial.** Listados separados. `GET lookup-rut` sociedad+clientes+proveedores. **Productor** no es maestro propio (`productor: false`) | Productor como tipo o flag real | Lookup no consulta SII externo | `comercial.controller` `lookup-rut`; `EmitirDocumentoPage` | — |
| D8 | Ficha única: bancos, contactos, despacho, trazabilidad | **Parcial.** Pestañas + historial + `solicitadoPor`. Sin PDF de solicitud interna | Ficha operativa suficiente para demo; PDF opcional | Helpers en `modules/ficha/` sin controller propio | `FichaContraparteModal`, clientes comercial, `FichaProveedoresPage` | — |
| D9 | Atributos CC / elemento / área por cuenta; activo/inactivo | **Cumple.** Dimensiones N:N + flags | Excel MJ como fuente de carga | Calidad del Excel vs import | migración `cuenta_dimensiones`; Plan de cuentas UI | — |
| D10 | No eliminar cuenta con movimiento; inactivar; rename al histórico | **Cumple.** DELETE → 409; impacto; rename usa maestro en diario/mayor; wipe `replace` bloqueado si hay asientos | Igual | — | `contabilidad.service` cuentas | — |
| D11 | Cotizaciones vs Orden de venta (MJ compras / Agustín ventas) | **Cumple (acuerdo 13/08: ambos).** Compras › Cotizaciones (proveedor→OC). Ventas › OV (cliente→stock→factura). Redirect `/comercial/cotizaciones` | Alinear `pantallas-permisos.ts` (aún lista Cotizaciones bajo Ventas, sin OV) | Permisos de pantalla desfasados del menú | `Sidebar.tsx`, `App.tsx`, `OrdenVentaPage.tsx`, `CotizacionesPage` | — |
| D12 | OV producto (maestro+bodega+stock) o servicio | **Cumple.** PRODUCTO / SERVICIO / FLETE | Producto exige `insumoId` + splits | — | `comercial.service` `assertLineasMaestro`; `OrdenVentaPage` | — |
| D13 | Movimiento en OV; factura copia qty/desc, precio editable | **Cumple** en API (+ test). UI OV confirma y factura | Emitir documento (wizard) puede seguir emitiendo tipos de compra (Warning arquitectura) | Wizard emitir no está atado solo a factura/NC | `confirmarOrdenVenta`, `assertFacturaLineasLocked`, `comercial-ov.spec.ts` | — |
| D14 | Stock venta solo positivo (no tránsito) | **Parcial.** `StockInsumoBodega` rechaza saldo negativo. No hay estado «tránsito de venta» separado | Modelo de reserva/tránsito si packing lo exige (Reu4 AlmaWeb) | Tránsito Reu4 (AlmaWeb) **no** modelado | `stock-bodega.util.ts` | — |
| D15 | Multi-bodega; no sobre-stock | **Cumple** API+UI OV (splits + selector con cantidad) | Recepciones/traslados deben mantener saldos (util ya en movimientos) | Bodega en movimiento sigue siendo string + id | `OrdenVentaPage`; `insumos.service` | — |
| D16 | No vender bajo costo; param; excepción merma | **Parcial.** `Empresa.ventaBajoCosto` BLOQUEAR \| PERMITIR_MERMA; motivo en línea OV. **Sin UI admin** para el parámetro (default BLOQUEAR) | Pantalla empresa o param para cambiar modo | — | schema `Empresa.ventaBajoCosto`; `assertLineasMaestro` | — |
| D17 | Flete = línea extra, no recargo SII | **Parcial.** `tipoLinea: FLETE` en OV. Cotización/emitir pueden no ofrecerlo igual | Unificar FLETE en emitir y cotización | Canonical DTE: no auditado si manda recargo SII | `OrdenVentaPage`; DTO comercial | Billing/DTE |
| D18 | Plantilla OC/cotización configurable + preview | **Parcial.** Editor `plantillaDoc` + print HTML. No PDF servidor ni DTE | Preview suficiente; DTE cuando GoSocket | — | `PlantillaDocumentosPage`, `documentoPrint.ts` | GoSocket |
| D19 | SSO Microsoft; botón disabled sin credenciales | **Parcial.** Login MSAL + API config/token. Depende `.env` / IT | Botón off hasta Tenant/Client ID | — | `LoginPage`, `microsoft-token.ts` | IT Almahue |
| D20 | Ambiente publicado; piloto con datos reales | **Parcial.** Prod `45.7.229.46/almahue-erp/`. Código local de OV/stock **puede no estar en prod** hasta deploy | Deploy fase comercial + migrate `stock_ov_ficha` | E2E compra/venta en prod no cerrado | `DEPLOY.md` | Deploy |

---

## 2. Temas diferidos Reu6 (y vivos Reu5/Reu4)

| Tema | Minuta | As-is | To-be | Estado | Bloqueado |
|---|---|---|---|---|---|
| Traspaso gastos próxima temporada | Reu6; Agustín: no hacer | No implementado (correcto) | Fuera de alcance hasta presupuesto mayo | **diferido** | Producto + MJ |
| DTE real GoSocket | Reu6 / Reu5 / Reu4 | Stub `billing/` + env | Emisión SII real | **diferido** | Pablo/MJ credenciales |
| Carga masiva DTE Acepta | Reu6 | No | Histórico en piloto | **diferido** | MJ ↔ Acepta |
| Demo completa contabilidad + tesorería | Reu6 «siguiente reunión» | Módulos **existen** (asientos, periodos, cartolas, pagos, estado de cuenta, balance 8 col) | Recorrido cliente, no greenfield | **parcial** (código sí, demo no) | Agenda demo |
| Demo profunda inventario | Reu6 | Maestro, bodegas, movimientos, stock OV | Recorrido + Excel AlmaWeb | **parcial** | Excel MJ (R4-11) |
| SMTP / correo al cambiar PIN, reenvío mail | Reu5 | Correo/adjunto ocultos | SMTP | **diferido** | Infra |
| Excel cartolas finas MJ | Reu5 / R4-16 | Carga Excel **base** | Formato banco Almahue | **parcial** | MJ |
| Guías de despacho en UI (no en libro ventas) | Reu4 D5 / Reu5 | API `guias-despacho`; menú Ventas **sin** despachos | UI despacho → bodega | **parcial** | — |
| Flag inventariable + AlmaWeb tránsito | Reu4 D10 / R4-12 | No hay `inventariable` en código | Producto inventariable vs servicio; AlmaWeb paso | **no hay** | Excel/definición MJ |
| Contabilidad electrónica SII | Reu4 D13 | Config SII de cuentas; no certificación | Segunda etapa | **diferido** | — |
| Reenvío PDF/XML libro ventas | R4-08 | Print HTML local | XML/PDF partner | **diferido** | GoSocket |
| Cobranza (compromisos, mail, tracking) | R4-18 | No (solo estado de cuenta / aging) | Propuesta, no feature | **diferido** | Producto |
| Mantenedor códigos flujo caja | R4-25 | Flujo caja UI; códigos Agrosoft no auditados | Param tesorería | **parcial** | — |
| Cotiz→NP→Factura (Reu5 «hecho») | Reu5 | **Contradicción superada por Reu6+código 13/08:** cotización ya no va a NP/factura | No restaurar NP en Compras | **contradicción** resuelta en código | — |

---

## 3. Flujos de negocio (corte transversal)

| Flujo | As-is | Hueco de flujo | Severidad |
|---|---|---|---|
| Login / RBAC / AdminConcepto / PIN | Operativo | Re-login AdminConcepto; SSO sin credenciales | Baja (operativa) |
| Aprobaciones OC / proformas | Cadena grupos+escalas | Comercial sin aprobación; `workflows-admin` legacy sigue en API/UI | Media (deuda) |
| Compras: cotización → OC → recepción → libro | Cableado | Cotización en `features/comercial`; matching OC-factura (R4-05) hay que revalidar en Fase 4 | Media |
| Ventas: OV → stock → factura → libro | Cableado API+pantalla OV | Wizard **Emitir** aún puede crear cotización/NP/OC (mezcla); libro vs solo emitidos/contabilizados (Reu4 D6) a revalidar | Alta (demo) |
| Ficha cliente/proveedor | Pestañas + historial | Productor; PDF solicitud | Baja |
| Plan de cuentas | Inactivar + dimensiones | — | — |
| Insumos / bodega | Stock por bodega + movimientos | Inventariable, Excel AlmaWeb, NC→reingreso automático | Media |
| Contabilidad | Asientos, periodos, centralización, reportes | Demo y «oficial SII» no cerrados | Media (agenda) |
| Tesorería | Pagos, cartolas, conciliación, estado de cuenta, anticipos, aging | SMTP; Excel banco fino; cobranza | Media |
| DTE | Stub | Emisión real | Alta (piloto SII) |
| Plantilla PDF | HTML print | PDF/DTE | Baja hasta GoSocket |

---

## 4. Inconsistencias de producto (prioridad demo)

1. **`pantallas-permisos.ts` vs menú:** ~~Cotizaciones en Ventas~~ → **alineado** (ver `qa/HUERFANOS-H1-H14.md`).  
2. **Emitir documento** restringido a FACTURA/NC/ND/GUIA; producto con stock vía OV.  
3. **`ventaBajoCosto`** parametrizable en Admin › Empresas.  
4. **Prod vs local:** migraciones OV/aprobación pendientes deploy explícito.  
5. **Aprobación comercial** implementada; activar flag tras reunión (checklist QA).

---

## 5. Qué no entra en Fase 1

- Editar skills/reglas (Fase 2).  
- Lista «no mostrado al cliente» detallada (Fase 3; hay insumo arriba).  
- Ejecutar tests (Fase 4–5).

Siguiente: **Fase 2** (skills/rules vs este as-is) cuando lo pidas.
