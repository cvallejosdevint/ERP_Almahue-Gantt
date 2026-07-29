# Plan maestro — Pruebas de flujo completo Almahue ERP

**Fecha:** 2026-07-29 · **Actualizado:** 2026-07-29 (cierre hallazgos)  
**Modo:** Demo Mode OFF (Nest → Prisma, datos reales en BD)  
**URL:** `http://localhost:5174/` (front) / `http://localhost:3001/api/v1` (back)  
**Login base:** `admin@almahue.local` / `Admin123!` (empresa EMP-1 Almahue)

## Convención de nombres (para identificar fácil en BD)

- Todo dato creado en estas pruebas lleva el prefijo **"Prueba QA"** o **"Intento N"** en su nombre/razón social/código.
- Casos con múltiples variantes (ej. usuario inhabilitado) se numeran **IntentoN** empezando en 1.
- Cada caso de prueba tiene un ID `TC##` correlativo y su propia carpeta de capturas: `TC##-nombre-caso/`.

---

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| Casos de prueba | **41 / 41 PASS (100%)** |
| Bugs de producto encontrados | 4 (H4, H5, H8 + PATCH elementos/honorarios) |
| Bugs de producto abiertos | **0** |
| Hallazgos de automatización / no-bug | 3 (H2, H7, falsos negativos de lotes) — cerrados como aclarados |
| Hallazgos técnicos en monitoreo | 1 (H6 — warning `pg`, no bloqueante) |
| Diferidos externos (no son bugs de esta suite) | Ver [`../DEFINICIONES_PENDIENTES.md`](../DEFINICIONES_PENDIENTES.md) |

---

## Matriz de hallazgos H1–H8 — ¿están solucionados?

| ID | Tipo | Estado | ¿Solucionado? | Detalle |
|---|---|---|---|---|
| **H1** | UX / login inactivo | **CERRADO** | Sí (mitigado) | Backend siempre responde `Credenciales inválidas` para usuario inactivo. El “silencio” del intento 1 fue variabilidad del agente. Toasts ahora duran **5s** + botón cerrar (`ThemedToaster`). |
| **H2** | Automatización | **CERRADO** | Sí (no era bug) | Reintento OK; timing del agente. Sin cambio de producto. |
| **H3** | UX plantilla docs | **CERRADO** | Sí (mitigado) | Vista previa con **debounce 400ms** para no reescribir el iframe en cada tecla (`PlantillaDocumentosPage`). |
| **H4** | Bug crítico UI | **CORREGIDO** | Sí | `SearchableSelect` con portal `fixed` a `document.body`. |
| **H5** | Bug a11y UI | **CORREGIDO** | Sí | Acciones Plan de cuentas siempre visibles + `aria-label` + foco teclado. |
| **H6** | Técnico (`pg`) | **MONITOREO** | No aplica fix producto | Warning aislado de `pg` en log; operación 201 OK. No hay query sin `await` en el flujo de tarifas. Reabrir solo si se repite con frecuencia. |
| **H7** | Automatización | **CERRADO** | Sí (no era bug) | Formulario OC estable; fallo del agente por CDP/stale refs. |
| **H8** | Bug UX | **CORREGIDO** | Sí | Periodo de Conciliación con `defaultValue` del periodo activo (ya no solo placeholder). |

### Fixes adicionales cerrados fuera de H1–H8 (misma pasada)

| Ítem | Estado |
|---|---|
| Elementos de costo / Factores honorarios sin update | **CORREGIDO** — `PUT /elementos-costo/:id` y `PUT /factores-honorario/:id` |
| PC-04 periodo cerrado → contabilizar | **CORREGIDO** — `assertPeriodoAbierto` en asientos CONTABILIZADO + check en Libro ventas |
| `eslint.config.js` faltante | **CORREGIDO** — flat config; `npm run lint` sin errors |

**Respuesta corta:** los hallazgos de **producto/UX de esta suite están solucionados o mitigados (H1–H5, H7–H8)**. Queda solo **H6 en monitoreo** (no es un bug funcional). Lo diferido (GoSocket, cuentas corrientes, cartolas banco-específicas, etc.) no son hallazgos de esta QA; están especificados en `DEFINICIONES_PENDIENTES.md`.

---

## Registro de casos

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC01 | Acceso | Login admin + confirmar Modo Demo OFF | admin@almahue.local | ✅ PASS |
| TC02 | Administración | Crear empresa nueva | Empresa Prueba QA (RUT 76111111-1) | ✅ PASS |
| TC03 | Administración | Crear usuario habilitado | usuarioprueba1@test.com (código U1) | ✅ PASS |
| TC04 | Administración | Crear usuario INHABILITADO — intento 1 | usuarioIntento1@test.com (código UINTENTO1) | ✅ PASS (H1 cerrado) |
| TC05 | Administración | Crear usuario INHABILITADO — intento 2 (otra empresa) | usuarioIntento2 / Empresa Intento 2 (RUT 76222222-2) | ✅ PASS |
| TC06 | Administración | Crear rol con permisos limitados y verificar sidebar reducido | Rol Prueba QA | ✅ PASS (H2 cerrado — no bug) |
| TC07 | Administración | Editar plantilla de documentos | Footer "Prueba QA" | ✅ PASS (H3 mitigado) |

**Lote 1 (Administración) — CERRADO: 7/7 PASS.**

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC08 | Parametrización | Crear moneda | PQA — Peso Prueba QA | ✅ PASS |
| TC09 | Parametrización | Crear unidad de medida | UPQ — Unidad Prueba QA | ✅ PASS |
| TC10 | Parametrización | Crear centro de costo | CC-PQA — Centro de Costo Prueba QA | ✅ PASS (falso negativo agente aclarado) |
| TC11 | Parametrización | Crear tipo de documento | DOCPQA — Documento Prueba QA (módulo Comercial) | ✅ PASS (H4 corregido) |
| TC12 | Parametrización | Crear elemento de costo | EC-PQA — Elemento Costo Prueba QA | ✅ PASS |
| TC13 | Parametrización | Crear cuenta en plan de cuentas (hija de CAJA) | 1-1-01-01-901 — Cuenta Prueba QA | ✅ PASS (H5 corregido) |
| TC14 | Parametrización | Crear proveedor | 77.888.999-K — Proveedor Prueba QA SpA | ✅ PASS |
| TC15 | Parametrización | Verificar/abrir período contable | 2026-07 | ✅ PASS |
| TC16 | Parametrización | Crear mapeo Config SII | DOCPQA → 1-1-01-01-901 · Cuenta Prueba QA | ✅ PASS |

**Lote 2 (Parametrización) — CERRADO: 9/9 PASS.**

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC17 | Maestros | Crear cliente | 88.111.222-K — Cliente Prueba QA | ✅ PASS |
| TC18a | Maestros | Crear contratista | 77.222.333-K — Contratista Prueba QA (Cosecha) | ✅ PASS |
| TC18b | Maestros | Crear tarifa de contratista | Contratista Prueba QA · Cosecha manual · Cosecha uva · $5.000/Caja · CC-PQA · vigente desde 2026-07-01 | ✅ PASS (H6 monitoreo) |
| TC19 | Maestros | Crear insumo/artículo | INS-PQA — Insumo Prueba QA (UN) | ✅ PASS |
| TC20 | Maestros | Crear bodega | BOD-PQA — Bodega Prueba QA | ✅ PASS |

**Lote 3 (Maestros) — CERRADO: 5/5 PASS.** Primer pase del agente = falso negativo (campos obligatorios vacíos; 0 POST al back). Reintento manual OK.

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC21 | Ventas | Crear cotización | Folio 2635 · Cliente Prueba QA · $100.000 · BORRADOR | ✅ PASS |
| TC22 | Ventas | Emitir factura y contabilizar | Folio 4692 · Cliente Prueba QA · $150.000 · CONTABILIZADA | ✅ PASS |
| TC23 | Ventas | Verificar libro de ventas + asiento generado | Asiento N° 20260001 · Debe/Haber $150.000 · Contabilizado | ✅ PASS |

**Lote 4 (Ventas) — CERRADO: 3/3 PASS.** Falso negativo del agente (CDP no sincronizó React); reintento manual OK.

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC24 | Compras | Crear orden de compra | OC-PQA-001 · Proveedor Prueba QA SpA · $50.000 CLP · CC 100% | ✅ PASS |
| TC25 | Compras | Aprobar OC | OC-PQA-001 → APROBADA | ✅ PASS |
| TC26 | Compras | Recepcionar OC | OC-PQA-001 · TC 1 · $50.000 → CONFIRMADA | ✅ PASS |
| TC27 | Compras | Registrar factura de compra | FACT-PQA-001 · $50.000 · MATCH OK · EMITIDO | ✅ PASS |

**Lote 5 (Compras) — CERRADO: 4/4 PASS.** H7 aclarado (no bug de re-render).

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC28 | Contratistas | Ingreso diario de labor | Contratista Prueba QA · CC-PQA · Cosecha manual/uva · JORNADA · 20 · $5.000 | ✅ PASS |
| TC29 | Contratistas | Asociación de labores → proforma | Ingreso TC28 asociado a PRF-PQA-001 (calce OK) | ✅ PASS |
| TC30 | Contratistas | Proforma → definitiva → aprobación | PRF-PQA-001 · $100.000 · BORRADOR→PENDIENTE APROBACIÓN→DEFINITIVA | ✅ PASS |
| TC31 | Contratistas | Facturar proforma(s) | PRF-PQA-001 → FACTURADA · Factura FACT-CONT-PQA-001 | ✅ PASS |
| TC32 | Contratistas | Traspaso / cierre mensual | Traspaso 2026-07 · asiento contable 20260002 generado | ✅ PASS |

**Lote 6 (Contratistas) — CERRADO: 5/5 PASS.** Falso negativo por orden de campos Labor→Actividad; reintento manual OK.

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC33 | Bodega | Movimiento de stock (entrada proveedor) | Entrada · Insumo Prueba QA · Bodega Prueba QA · 100 un · $1.500 · CONFIRMADO | ✅ PASS |
| TC34 | Contabilidad | Asiento manual | Asiento 20260003 · Cuenta Prueba QA / CAJA · $25.000 · CONTABILIZADO | ✅ PASS |
| TC35 | Contabilidad | Verificar Libro diario | Periodo 2026-07 · Debe=Haber cuadrado | ✅ PASS |
| TC36 | Contabilidad | Verificar Mayor por cuenta | Cuenta Prueba QA / CAJA con saldos | ✅ PASS |
| TC37 | Contabilidad | Centralización masiva del período | 4 asiento(s); contratistas omitido (ya en TC32) | ✅ PASS |

**Lote 7-8 (Bodega + Contabilidad) — CERRADO: 5/5 PASS.**

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC38 | Tesorería | Importar cartola bancaria | cartola-prueba-qa.xlsx · Banco Chile · $300.000 · CARGADA | ✅ PASS |
| TC39 | Tesorería | Conciliación | Banco Chile · Jul 2026 · PENDIENTE | ✅ PASS (H8 corregido) |
| TC40 | Tesorería | Registrar pago | Proveedor Prueba QA · $150.000 CLP · FAC-PQA-001 | ✅ PASS |
| TC41 | Tesorería | Registrar anticipo | Productor Prueba QA · $500.000 CLP | ✅ PASS |

**Lote 9 (Tesorería) — CERRADO: 4/4 PASS.**

---

## Detalle técnico de hallazgos (referencia)

### Bugs reales — CORREGIDOS

- **H4 — SearchableSelect en modales:** portal a `document.body` con posición `fixed` (`searchable-select.tsx`).
- **H5 — Plan de cuentas hover-only:** botones siempre visibles + a11y (`PlanCuentasPage.tsx`).
- **H8 — Periodo Conciliación:** `defaultValue` desde periodo contable activo (`TesoreriaPages.tsx`).

### Mitigaciones UX

- **H1 / toasts:** `ThemedToaster` duración 5s + `closeButton`.
- **H3 — Plantilla docs:** debounce preview **400ms** (`PlantillaDocumentosPage.tsx`).

### No-bugs / automatización — CERRADOS

- **H2, H7** y falsos negativos de lotes 3–6: estrategia del agente (campos vacíos, CDP, orden Labor/Actividad). Sistema OK en reintento manual.

### Monitoreo (no bloquea cierre)

- **H6:** `DeprecationWarning` aislado de `pg`. Sin acción de código mientras no se reproduzca.

### Relacionado (fuera de H1–H8, ya cerrado)

- PATCH elementos de costo / factores honorarios.
- PC-04 bloqueo contabilizar con periodo cerrado/inexistente.
- ESLint flat config.

---

## Evidencia y documentos relacionados

- Capturas por caso: carpetas `TC##-*` en este directorio.
- Reporte consolidado: [`REPORTE-FINAL.md`](./REPORTE-FINAL.md).
- Diferidos externos (GoSocket, cuentas corrientes, cartolas, etc.): [`../DEFINICIONES_PENDIENTES.md`](../DEFINICIONES_PENDIENTES.md).
