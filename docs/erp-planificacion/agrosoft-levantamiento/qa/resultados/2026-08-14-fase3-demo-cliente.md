# Fase 3 — Demo cliente (lo no discutido en reuniones)

**Fecha:** 2026-08-14  
**Alcance:** módulos/pantallas/flujos en código que **no** figuran (o figuran de forma incompleta) en minutas Reu4–Reu6, pero que el cliente podría esperar ver en demo.  
**Fuentes:** Fase 1, Fase 2, `reunion4-minuta-2026-07-30.md`, `reunion5-minuta-2026-08-03.md`, `reunion6-minuta-2026-08-06.md`, `AGENTS.md`, `Sidebar.tsx`, `App.tsx`, módulos Nest, seeds.  
**No se leyeron transcripciones.** Carlos/Sergio en demo = hipótesis.

Leyenda **en reuniones:** **sí** · **parcial** · **no** · **diferido**  
Leyenda **en código:** **cumple** · **parcial** · **no hay** · **mock**  
Leyenda **estado demo:** **listo** · **parcial** · **no preparado** · **ocultar** · **diferido**  
Clasificación: **(a)** en código, no mostrado en reuniones · **(b)** necesario demo, incompleto · **(c)** ocultar/evitar · **(d)** diferido explícito

---

## 1. Resumen ejecutivo

### Qué mostrar (con guion cerrado)

| Bloque | Por qué |
|---|---|
| **Compras** cotización → OC → aprobación (grupos/escalas + PIN) → recepción → libro compras | Recorrido más maduro; alineado Reu4–Reu6; datos en `prepare-demo-sergio.ts` / `seed-demo-showcase.ts`. |
| **Contratistas** proformas → aprobación → asociar factura | Mostrado Reu4; seed presentable. |
| **Ventas Reu6** OV → confirmar stock → factura desde OV → libro ventas | Decisión D11–D13; **no** usar wizard Emitir como flujo canónico. |
| **Admin** usuarios, roles, multi-empresa (header), reglas de aprobación (árbol + simulador) | Reu6 D1–D6; verificar prod con Fase 2 deploy. |
| **Parametrización** plan de cuentas (dimensiones CC/elemento/área), proveedores, ficha cliente | Reu6 D7–D10. |

### Qué preparar antes (P0 abajo)

1. **Entorno:** confirmar prod/local con migrate `20260813230000_stock_ov_ficha` y API `grupos-aprobacion` (no legacy `workflows-admin` vacío).  
2. **Seed OV:** hoy no hay OV de demostración en `seed.ts` / `prepare-demo-sergio.ts`; solo factura directa legacy. Crear OV confirmada + stock en bodega antes de demo ventas.  
3. **Guion del presentador:** no abrir Emitir con tipos Cotización/NP/OC; no vender aprobación comercial; no prometer DTE SII.

### Qué no mostrar (o solo con disclaimer)

- Wizard **Emitir documento** con selector COTIZACION / NP / OC (mezcla Compras/Ventas; contradice D11).  
- **Presupuestos** (`MockListPage` — datos no operativos).  
- **Prospectos** (ruta redirige a Clientes; catálogo permisos obsoleto).  
- **Aprobación OV/factura** (D4 reservado).  
- **DTE real** / reenvío XML (diferido GoSocket).  
- **Traspaso gastos próxima temporada** (diferido Reu6).  
- **Guías de despacho** (API `guias-despacho`; sin pantalla en menú).

### Qué el cliente pidió explícitamente y quedó para “siguiente reunión” (Reu6)

Contabilidad completa, tesorería completa, inventario profundo — **existen en código** (Reu4 ya los recorrió parcialmente) pero Reu6 **diferió** la demo cerrada. Son candidatos a recorrido 2 si hay datos y tiempo.

---

## 2. Tabla módulo / pantalla

| Módulo / pantalla | En reuniones (Reu4–6) | En código | Estado demo | Riesgo si se muestra | Recomendación demo | Tipo |
|---|---|---|---|---|---|---|
| Panel operativo (`/`) | **parcial** (Reu4 menciona gestión/Power BI futuro; no KPIs actuales) | **cumple** — KPIs OC, proformas, gráfico gasto, TC USD | **parcial** — útil apertura 2 min | Cliente espera dashboards especie/presupuesto (fuera alcance) | Mostrar como “inbox operativo”, no como BI | (a) |
| Admin › Empresas / Usuarios / Roles | **sí** D1–D3 | **cumple** | **listo** | Multi-empresa mal explicada | Demo cambio empresa + rol sin PIN en checkbox | — |
| Admin › Plantilla documentos | **parcial** Reu4 | **cumple** | **listo** | Preview ≠ DTE | Mostrar preview HTML; disclaimer GoSocket | (a) |
| Admin › Reglas aprobación (grupos/escalas/simulador) | **sí** D4–D6 (post-Reu6) | **cumple** | **parcial** en prod | Prod puede tener UI legacy vacía (D20) | Verificar deploy Fase 2 antes; usar simulador | (b) |
| Admin › `workflows-admin` API legacy | **no** (reemplazado por grupos) | **parcial** — API aún en `admin.controller` | **ocultar** | Confusión “dos sistemas” | No mencionar; no abrir DevTools a legacy | (c) |
| Parametrización › Monedas, UM, CC, tipos doc | **sí** Reu4 D1, D11 | **cumple** | **listo** | — | Rápido | — |
| Parametrización › **Áreas de negocio** | **parcial** (D9 atributo cuenta; pantalla no nombrada) | **cumple** — `AreasNegocioPage` | **parcial** | Catálogo permisos **no** lista esta pantalla | Mostrar si se explica D9; opcional | (a) |
| Parametrización › Plan cuentas + dimensiones | **sí** D9–D10 | **cumple** | **listo** | — | Demo inactivar cuenta + impacto | — |
| Parametrización › **Indicadores BC** (sync programable) | **parcial** Reu4 D11 “indicadores → Parametrización” | **cumple** — sync manual/auto + cron | **parcial** | TC incorrecto si no sync | Sync manual antes; 1 min | (a) |
| Parametrización › Proveedores + ficha | **sí** D7–D8 | **cumple** | **listo** | Productor ausente en lookup | No prometer productor | (b) |
| Contratistas › Listado / Tarifas | **sí** Reu4 | **cumple** (listado mock CRUD) | **parcial** | Mock feel en listado | Enfocar proformas | (a) |
| Contratistas › **Ingreso diario** | **no** en minuta (sí BPMN entrega) | **cumple** | **no preparado** | Flujo largo sin seed | Omitir o mencionar “en construcción operativa” | (a) |
| Contratistas › **Asociación labores** | **no** en minuta | **cumple** | **no preparado** | Idem | Omitir en demo corta | (a) |
| Contratistas › Proformas + aprobaciones | **sí** Reu4 D2 | **cumple** | **listo** | — | Cadena + PIN | — |
| Contratistas › **Traspaso y cierre** | **no** (≠ traspaso gastos temporada Diferido Reu6) | **cumple** — cierre contable contratistas | **parcial** | Confundir con “gastos próxima temporada” | Solo si hay tiempo; aclarar alcance | (a) |
| Ventas › **Órdenes de venta** | **sí** Reu6 D11–D17 | **cumple** | **no preparado** — sin seed OV | Sin datos, demo vacía | **P0:** seed OV + stock bodega | (b) |
| Ventas › Emitir documento | **sí** Reu4–5 (emisión); **no** como mezcla tipos | **parcial** — FACTURA/NC + COTIZ/NP/OC | **ocultar** tipos compra | Rompe D11; revive NP | Solo FACTURA/NC con disclaimer; ideal omitir | (c) |
| Ventas › Libro de ventas | **sí** Reu4 D6–D8 | **cumple** | **listo** con seed | Libro vs borradores | Mostrar emitidos/contabilizados | — |
| Ventas › Clientes + ficha | **sí** D7–D8 | **cumple** | **listo** | — | Pestañas banco/contacto/despacho | — |
| Ventas › **Prospectos** (`/comercial/prospectos`) | **no** decisión minuta | **parcial** — redirect a Clientes | **ocultar** | Catálogo permisos miente | No navegar; ruta huérfana | (c) |
| Ventas › **Guías despacho** | **parcial** Reu4 D5; UI **diferido** Reu5 | **parcial** — API `guias-despacho`; **no** UI | **ocultar** | “¿Dónde despacho?” | Decir: API lista; UI próxima | (d) |
| Compras › Cotizaciones → OC | **sí** D11 (Compras) | **cumple** | **listo** | — | Flujo estrella compras | — |
| Compras › OC / aprobaciones / recepción / libro | **sí** Reu4 | **cumple** | **listo** | — | Con PIN y CC por ítem | — |
| Insumos › Maestro / bodegas / movimientos | **parcial** Reu4 + Reu6 “demo profunda” diferida | **cumple** | **parcial** | Stock por bodega post-migrate; sin Excel AlmaWeb | 1 bodega + 1 producto; no Excel masivo | (b) |
| Contabilidad › Períodos / config SII | **sí** Reu4 D11–D12 | **cumple** | **listo** | — | Breve | — |
| Contabilidad › Asientos / **centralización masiva** | **parcial** (Reu4 reportes; centralización no destacada) | **cumple** | **parcial** — seed asientos en showcase | Pocos asientos si BD limpia | Segundo recorrido opcional | (a) |
| Contabilidad › Reportes (diario, mayor, balance 8 col) | **sí** Reu4 R4-15 | **cumple** | **listo** con datos | Ceros si BD vacía | Usar post-seed | — |
| Contabilidad › **Presupuestos** (menú bajo Contabilidad) | **parcial** Reu4 (pestaña vista; sin decisión fuerte) | **mock** — `MockListPage` | **ocultar** | Parece funcional y no lo es | No abrir | (c) |
| Tesorería › Flujo caja, cartolas, pagos, anticipos, nóminas, conciliación, estado cuenta | **sí** Reu4 (recorrido); Reu6 **diferido** demo cerrada | **cumple** | **parcial** — showcase tiene filas | Excel banco fino diferido; cobranza R4-18 no existe | Recorrido 2: cartola + conciliación + estado cuenta | (a)+(b) |
| Tesorería › Estado cuenta (duplicado menú Contabilidad) | **sí** R4-16–R4-22 | **cumple** | **listo** | Duplicidad menú | Usar desde Tesorería | — |
| Login Microsoft SSO | **sí** D19 | **parcial** — botón según `.env` | **parcial** | Botón roto sin credenciales | Mostrar disabled + narrativa IT | — |
| Perfil / PIN aprobación | **parcial** Reu5–6 | **cumple** | **listo** | PIN en rol legacy | Perfil usuario aprobador | (a) |
| Topbar: modo demo / periodo / notificaciones | **no** | **cumple** | **parcial** | “Modo demo” confunde con datos reales piloto D20 | Dejar **modo real**; explicar periodo header | (a) |
| Billing / DTE GoSocket | **diferido** Reu4–6 | **parcial** — stub `billing/` | **diferido** | Prometer SII | Solo mencionar integración en curso | (d) |
| Catálogo `pantallas-permisos.ts` vs Sidebar | **no** | **parcial** — desfasado | **ocultar** en demo | OV ausente; Cotizaciones en Ventas; Prospectos fantasma | No demo de Roles hasta alinear catálogo | (c) |
| **Prod** `45.7.229.46` vs local | **sí** D20 | **parcial** | **no preparado** sin deploy | OV/stock/grupos ausentes | Deploy + migrate antes de demo cliente | (b) |

### Rutas huérfanas (`App.tsx` sin ítem Sidebar)

| Ruta | Comportamiento | Recomendación |
|---|---|---|
| `/comercial/prospectos` | Redirect → `/comercial/clientes` | No enlazar |
| `/perfil` | Topbar usuario | OK |
| `/insumos/catalogo` | Redirect → maestro | — |
| `/tesoreria/aging` | Redirect → nóminas | — |
| `/contabilidad/indicadores-bc` | Redirect → catálogo | Dashboard KPI enlaza aquí (OK) |
| `/workflow/*` | Redirect → compras/aprobaciones | Legacy URL |
| `/reportes/*` | Redirect → `/` | No existe módulo reportes |

### Menú Sidebar sin ruta propia inexistente

Todos los ítems del `MENU` en `Sidebar.tsx` tienen ruta en `App.tsx`. Excepción: subgrupos anidados (Configuración / Operaciones / Reportes) son agrupadores.

---

## 3. Flujos demo sugeridos (15–20 min c/u)

### Recorrido A — «Operación compras + aprobaciones» (~18 min)

**Audiencia:** MJ / Agustín / compras.  
**Usuario:** solicitante + aprobador (PIN `4821`).

1. Login → Panel operativo (KPI OC pendientes).  
2. Parametrización › Proveedores (ficha rápida).  
3. Compras › Cotizaciones → crear → **Convertir a OC**.  
4. Compras › Aprobaciones → cadena grupos/escalas → aprobar con PIN.  
5. Compras › OC aprobada → imprimir preview plantilla.  
6. Compras › Recepciones → confirmar.  
7. Compras › Libro de compras (match OC–factura).  
8. *(Opcional 3 min)* Admin › Reglas → simulador con monto de la OC.

**Pre-requisitos:** `seed-aprobaciones-fase2` + `prepare-demo-sergio` o datos equivalentes; prod con grupos-aprobacion.

---

### Recorrido B — «Venta Reu6: OV + stock + factura» (~20 min)

**Audiencia:** MJ / Agustín / ventas.  
**Mensaje clave:** cotización es de **Compras**; ventas usa **OV**.

1. Insumos › Maestro + Bodegas (stock Urea en Bodega Central tras migrate).  
2. Ventas › Clientes (ficha exportación si aplica).  
3. Ventas › **Órdenes de venta** → línea PRODUCTO + splits bodega → guardar → **Confirmar** (movimiento stock).  
4. Desde OV → generar **Factura** (qty/desc bloqueados, precio editable).  
5. Ventas › Libro de ventas (contabilizada / preview).  
6. **No abrir** Emitir documento con tipo Cotización/NP/OC.

**Pre-requisitos P0:** migrate `stock_ov_ficha`; seed manual 1 OV confirmada si no hay script; insumo con `StockInsumoBodega` > 0.

---

### Recorrido C — «Back-office: contabilidad + tesorería» (~18 min)

**Audiencia:** MJ / contabilidad (prometido “siguiente reunión” Reu6).  
**Datos:** `seed-demo-showcase` (cartolas, pagos, aging, asientos).

1. Parametrización › Plan de cuentas (dimensiones + inactivar).  
2. Contabilidad › Períodos (periodo header 2026-08).  
3. Contabilidad › Comprobantes / asientos (1 ejemplo).  
4. Contabilidad › Centralización masiva (vista; sin ejecutar si BD sensible).  
5. Contabilidad › Balance 8 columnas / libro diario.  
6. Tesorería › Cartolas (carga ejemplo) → Conciliación (resumen pendientes).  
7. Tesorería › Estado de cuenta (filtro pendientes) → Nóminas aging.

**Disclaimer:** Excel cartolas formato MJ fino = diferido; cobranza con mail = no hay.

---

## 4. Datos / seed necesarios antes de demo

| Acción | Script / fuente | Motivo |
|---|---|---|
| Seed base + showcase | `npx prisma db seed` → incluye `seedDemoShowcase` | OC, facturas, tesorería, contabilidad, prospectos legacy |
| Aprobaciones fase 2 | `seed-aprobaciones-fase2.ts` (en seed principal) | Grupos S1–S6, usuarios QA, PIN |
| Limpieza + flujo Sergio | `scripts/prepare-demo-sergio.ts` | Quita basura QA; OC pendiente/aprobada/recepcionada; factura 88001 |
| **Crear OV demo** | **Manual o script nuevo (gap)** | Ningún seed crea `ORDEN_VENTA` ni confirma stock |
| Migrate stock/OV | `20260813230000_stock_ov_ficha` | `StockInsumoBodega` desde stock insumo legacy |
| Prod deploy | `DEPLOY-PROD-FASE2.md` | grupos-aprobacion, JWT AdminConcepto, código OV |
| Credenciales demo | `admin@almahue.local` / `Admin123!`; PIN `4821` | `AGENTS.md` |
| Periodo activo | 2026-08 ABIERTO | seeds alineados agosto 2026 |

**Conflictos seed a conocer:**

- `seed-demo-showcase.ts` aún siembra cadena **Cotiz → NP → Factura** (pre-D11) y prospectos — útil para libro ventas legacy, **no** para narrativa OV.  
- `prepare-demo-sergio.ts` siembra **factura directa** sin OV — válido para libro/tesorería, no para Recorrido B.  
- `Insumo.stock` en seed (1200) se proyecta a `StockInsumoBodega` solo tras migrate.

---

## 5. Lista «NO mostrar» / «mostrar con disclaimer»

### NO mostrar

| Ítem | Motivo |
|---|---|
| Emitir documento › tipos Cotización, NP, OC | Mezcla módulos; NP contradice Reu6 |
| Presupuestos | UI mock |
| Prospectos (ruta) | Redirect; sin valor |
| Guías despacho UI | No existe |
| Aprobación comercial / facturas en reglas | D4 reservado |
| DTE / timbre SII real | Stub + GoSocket diferido |
| Traspaso gastos próxima temporada | Diferido Reu6 |
| Cobranza (compromisos, mail) | R4-18 propuesta sin código |
| Contabilidad electrónica certificación | Diferido R4 D13 |
| `workflows-admin` en API herramientas | Legacy |

### Mostrar con disclaimer

| Ítem | Disclaimer sugerido |
|---|---|
| Preview / print HTML documentos | “Representación gráfica local; timbre SII cuando GoSocket esté conectado.” |
| Emitir solo FACTURA/NC (si se usa) | “Flujo de venta recomendado es Orden de venta; esta pantalla es emisión directa.” |
| Indicadores BC | “Tipo de cambio referencial BC; validar fecha sync.” |
| SSO Microsoft | “Pendiente credenciales IT Almahue.” |
| Inventario / AlmaWeb Excel | “Carga masiva y bodega tránsito: siguiente iteración.” |
| Prod vs piloto datos reales D20 | “Ambiente de prueba; piloto con datos reales coordinado con MJ.” |
| Parametrización `ventaBajoCosto` | “Regla activa (bloqueo bajo costo); pantalla admin del parámetro pendiente.” |

---

## 6. Gaps nuevos no cubiertos en Fase 1

| # | Gap | Evidencia | Severidad demo |
|---|---|---|---|
| G1 | **Sin seed/script OV E2E** (confirmar stock → factura) | `seed.ts`, `prepare-demo-sergio.ts`, `seed-demo-showcase.ts` sin `ORDEN_VENTA` | **Alta** |
| G2 | **Prospectos** en catálogo permisos pero ruta = redirect a Clientes | `ComercialPages.tsx` L195–197; `pantallas-permisos.ts` | Media |
| G3 | **Dashboard** enlaza indicadores BC vía redirect contabilidad → catálogo | `DashboardPage.tsx` L86; confuso pero funciona | Baja |
| G4 | **Contratistas** ingreso diario + asociación: código completo, **cero** mención minutas Reu4–6 | Sidebar; BPMN entrega only | Media (alcance) |
| G5 | **Traspaso y cierre contratistas** ≠ traspaso gastos temporada — riesgo de homónimo | `TraspasoContratistasPage` vs Reu6 diferido | Media |
| G6 | **Indicadores BC**: sync programable + cron (`bc-sync.cron`) no discutido en reuniones | `IndicadoresBcPage`, `catalogos` | Baja |
| G7 | **Modo demo** topbar sin narrativa en minutas | `DemoModeToggle.tsx` | Baja |
| G8 | **Áreas de negocio** en menú pero ausente en catálogo permisos | `Sidebar.tsx` vs `pantallas-permisos.ts` | Baja |
| G9 | **Estado de cuenta** duplicado en menú Contabilidad y Tesorería | `Sidebar.tsx` L135, L162 | Baja |
| G10 | `seed-demo-showcase` mantiene **NP** y documentos cotización cliente | Contradice guion ventas post-Reu6 | **Alta** si se mezcla con Recorrido B |

---

## 7. Priorización P0 / P1 / P2

### P0 — Bloquea demo fiable (7 ítems)

| ID | Tarea |
|---|---|
| P0-1 | Deploy prod + migrate `stock_ov_ficha` + verificar `GET /grupos-aprobacion` 200 |
| P0-2 | Crear datos demo **OV confirmada** + stock bodega + factura derivada (script o checklist manual) |
| P0-3 | Ejecutar `prepare-demo-sergio.ts` (o equivalente) en BD de demo; eliminar basura QA |
| P0-4 | Guion presentador: **no** Emitir COTIZ/NP/OC; ventas solo por OV |
| P0-5 | Verificar usuarios aprobadores + PIN y re-login AdminConcepto tras cambios JWT |
| P0-6 | Confirmar periodo contable 2026-08 abierto y empresa EMP-1 en header |
| P0-7 | No prometer cadena aprobación en facturas/OV (D4) |

### P1 — Mejora demo / reduce riesgo

| ID | Tarea |
|---|---|
| P1-1 | Recorrido C contabilidad+tesorería con datos showcase (Reu6 pendiente) |
| P1-2 | Alinear `pantallas-permisos.ts` con Sidebar (OV, Cotizaciones Compras, quitar Prospectos) |
| P1-3 | UI param `ventaBajoCosto` o narrativa fija “bloqueo activo” |
| P1-4 | Limpiar o etiquetar filas NP/cotización cliente en showcase si se usa misma BD |
| P1-5 | Probar flujo compras completo con rol no-admin (permisos reales) |

### P2 — Post-demo / deuda

| ID | Tarea |
|---|---|
| P2-1 | UI guías despacho |
| P2-2 | Restringir tipos en Emitir documento |
| P2-3 | Seed OV en `prepare-demo-sergio.ts` |
| P2-4 | Prospectos: quitar de permisos o implementar CRM mínimo |
| P2-5 | Presupuestos: quitar mock o implementar |
| P2-6 | Productor en lookup RUT |
| P2-7 | Excel AlmaWeb / inventariable flag |

---

## 8. Referencias cruzadas

- Huecos producto vigentes: Fase 1 §4, `AGENTS.md`  
- Tools IA / riesgo demo mal narrada: Fase 2 §1  
- Deploy prod aprobaciones: `ERP/DEPLOY-PROD-FASE2.md`  
- Siguiente: Fase 4–5 (tests / matriz cumplimiento)
