> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`docs/matriz-asis-tobe.md`](../../../matriz-asis-tobe.md) + [`qa/HUERFANOS-H1-H14.md`](../qa/HUERFANOS-H1-H14.md). Motivo: paquete 06/08 pre-OV unificado y pre-pipeline v2.

# AS-IS — ERP Almahue (estado actual del proyecto)

**Fecha:** 2026-08-06  
**Stack:** `erp_front` (React/Vite) · `erp_back` (NestJS/Prisma) · schema `erp` · API `/api/v1`  
**Branches:** `feature/backend-core` (front ahead 12, back ahead 9 + working tree Reu5)

---

## 1. Principio AS-IS vs TO-BE GoSocket

| | AS-IS | TO-BE (post docs GoSocket) |
|---|---|---|
| Plataforma usuario | Solo ERP | Solo ERP (sin cambio) |
| Emisión DTE | Folio local; sin SII | ERP → GoSocket → SII transparente |
| PDF | Preview local / watermark borrador | + PDF timbrado GoSocket |
| Compras electrónicas | Digitación / Excel | + recepción docs GoSocket |

---

## 2. Mapa de menú (Sidebar)

| Módulo | Rutas principales | Permiso |
|---|---|---|
| Panel | `/` | — |
| Admin | empresas, plantilla, usuarios, roles, aprobaciones | `admin:read` |
| Parametrización | monedas, UM, CC, tipos doc, plan cuentas, elementos, BC, proveedores | `catalogos` / `admin` |
| Contratistas | listado, ingreso, asociación, tarifas, proformas, aprobaciones, traspaso | `contratistas:read` |
| Ventas | libro, cotizaciones, emitir, clientes, prospectos | `comercial:read` |
| Compras | órdenes, aprobaciones, recepciones, registro | `compras:read` |
| Insumos | maestro, bodegas, movimientos | `insumos:read` |
| Contabilidad | periodos, config SII, asientos, centralización, libros, balance 8 col | `contabilidad:read` |
| Tesorería | flujo caja, cartolas, pagos, anticipos, aging, conciliación, estado cuenta | `tesoreria:read` |

**No hay:** menú NP dedicado · panel GoSocket · guías de despacho en UI.

---

## 3. Capacidad por módulo

### Admin
Empresas multi-tenant, usuarios/roles/permisos, workflows aprobación, PIN por usuario + password al cambiar PIN, plantilla documentos.  
**Gap:** SMTP recovery.

### Ventas
Emitir (wizard), borradores (filtro admin), libro (solo emitidos/contabilizados, resumen colapsable, año tope), cotizaciones (convert NP/Factura), clientes (alta panel derecho), reverso contable, NC, preview folio.  
**Gaps:** `convertirDocumento` pierde campos; NP sin UI Facturar; stubs pago/correo/adjunto; sin DTE.

### Compras
OC con CC por ítem, PIN, recepción, registro factura + alerta afecto, libro + resumen.  
**Gaps:** bridge pago; stubs mail/adjunto.

### Contratistas
Ingreso→asociación→proforma→PIN→factura N:1→traspaso/cierre con periodo header.  
**Gap:** factura = registro interno (no GoSocket).

### Contabilidad
Periodos abrir/cerrar/reabrir+motivo+historial, asientos, centralización, diario/mayor, balance 8 col, config SII (cuentas).  
**Gap:** contabilidad electrónica SII diferida.

### Tesorería
Cartolas (import base), pagos, conciliación, estado cuenta con tipo movimiento, aging, anticipos.  
**Gaps:** Excel cartolas “finas” MJ; deep-link desde libros.

### Insumos
Maestro, bodegas, movimientos.  
**Gaps:** inventariable AlmaWeb, guías UI.

---

## 4. Estados clave

| Entidad | Estados |
|---|---|
| DocumentoComercial | BORRADOR → EMITIDO → CONTABILIZADA / FACTURADO / ANULADO |
| OrdenCompra | BORRADOR → EMITIDO → APROBADO / RECHAZADO → RECEPCIONADA |
| Proforma | BORRADOR → PENDIENTE_APROBACION → DEFINITIVA → FACTURADA |
| PeriodoContable | ABIERTO / CERRADO (+ eventos CREAR/CERRAR/REABRIR) |
| Cartola | CARGADA → EN_CONCILIACION → CERRADA |

---

## 5. Deuda / diferidos (post-cierre P0 06/08)

| # | Síntoma | Severidad | Estado |
|---|---|---|---|
| 1 | Cotiz→NP sin salida UI a factura | P0 | **Cerrado** (pestaña NP + Facturar) |
| 2 | `convertirDocumento` no copia EXENTO/creadoPor/wizard | P0 | **Cerrado** |
| 3 | Destino OC comercial ≠ OrdenCompra compras | P0 | **Cerrado** (rechazo + mensaje) |
| 4 | “Registrar pago” toast stub | P0 | **Cerrado** (bridge → Tesorería) |
| 5 | Correo / adjunto | P1 | **Cerrado UI** (ocultos; SMTP diferido) |
| 6 | Guías API sin menú | P2 | Abierto |
| 7 | GoSocket / SMTP | Diferido | Abierto (`billing-gateway`) |
| 8 | Excel cartolas finas MJ | P1 | **Cerrado parser** multi-hoja (pack 06-CARTOLA) |
| 9 | Campos COMEX emisión/NC | P0 docs MJ | **Cerrado modelo+UI** (DTE diferido) |

---

## 6. Scorecard Reu5 (honesto)

| Ítem | Estado real |
|---|---|
| PIN + password | Hecho |
| CC por ítem OC | Hecho |
| Totalizados / resumen libros | Hecho (WT) |
| Emisión resize + EXENTO | Hecho |
| Multi-periodo 1 año | Hecho (WT) |
| Borradores filtro admin | Hecho (WT) |
| Historial + motivo periodos | Hecho (WT + migración) |
| Alta cliente panel | Hecho |
| Ventas sin CC | Hecho |
| Folio preview | Hecho |
| Menú acciones | Hecho (pago→Tesorería; mail oculto) |
| 88001 estado cuenta | Seed-dependiente |
| Cartolas | Base |
| GoSocket / SMTP | Diferido |

---

## 7. Integraciones

| Sistema | Estado |
|---|---|
| GoSocket / SII DTE | Ausente (removido a propósito) |
| SMTP | Ausente |
| Banco Central indicadores | Sync presente |
| Agrosoft legacy | Referencia de negocio; no API |

---

## 8. Criterio de piloto “en línea”

Operable **sin SII**: compras, emisión directa, contratistas, contabilidad, tesorería base, admin.  
No operable como producción DTE hasta GoSocket.  
Tras Fase 2 de código: sin menús que lleven a toast muerto; NP facturable; convert conserva datos.
