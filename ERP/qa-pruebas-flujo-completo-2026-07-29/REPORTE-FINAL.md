# Reporte final — Pruebas de flujo completo Almahue ERP

**Fecha de ejecución:** 2026-07-29
**Modo:** Demo Mode OFF (Nest → Prisma, datos reales en base de datos PostgreSQL)
**Frontend:** `http://localhost:5174/` · **Backend:** `http://localhost:3001/api/v1`
**Empresa base:** Almahue SpA (EMP-1) · **Login base:** `admin@almahue.local` / `Admin123!`
**Período contable activo:** 2026-07 (Julio)

## 1. Resumen ejecutivo

Se ejecutaron **41 casos de prueba (TC01–TC41)** cubriendo el flujo de negocio completo del ERP, de punta a punta: Administración → Parametrización → Maestros → Ventas → Compras → Contratistas → Bodega → Contabilidad → Tesorería.

| Resultado | Cantidad |
|---|---|
| ✅ PASS | **41 / 41 (100%)** |
| ❌ FALLA real de sistema | 0 |
| Bugs reales encontrados y corregidos | **H4, H5, H8** (+ PATCH elementos/honorarios, PC-04) |
| Hallazgos mitigados / no-bug cerrados | **H1, H2, H3, H7** |
| En monitoreo (no bloqueante) | **H6** (`pg` DeprecationWarning aislado) |

Ver matriz completa en `00-PLAN-MAESTRO.md` § «Matriz de hallazgos H1–H8».

Todos los datos de prueba fueron creados en la base de datos real bajo la convención de nombres **"Prueba QA"** / **"Intento N"**, quedando disponibles para revisión directa en BD o en la interfaz. Cada caso tiene su propia carpeta de evidencia con capturas de pantalla en `TC##-nombre-caso/`.

### Nota importante sobre "falsos negativos" de automatización

Durante la ejecución se delegaron varios lotes a un agente de pruebas autónomo (browser-use) que, en 5 lotes (Maestros, Ventas, Compras, Contratistas — primer intento), reportó fallas críticas de "bloqueo técnico" o "fallo sistemático de persistencia". En **todos los casos**, la verificación manual y el análisis de los logs del backend confirmaron que:
- El sistema **nunca recibió la petición POST** correspondiente (0 líneas en el log del backend en el momento del supuesto fallo), o
- El agente usó scripts de bajo nivel (CDP `Runtime.evaluate` con `element.value = ...`) que no disparan los eventos `input`/`change` que React necesita para sincronizar su estado interno, dejando campos "vacíos" para la validación aunque visualmente parecieran completos.

Es decir, estos fueron **problemas de la estrategia de automatización, no bugs del sistema**. Al reintentar manualmente con interacción estándar (equivalente a un clic/tecleo real de usuario), todos los formularios funcionaron correctamente al primer intento. Esto se documenta en detalle en cada lote del `00-PLAN-MAESTRO.md`.

## 2. Bugs reales encontrados y corregidos

### 🐛 H4 — `SearchableSelect` no seleccionable dentro de modales (CRÍTICO, CORREGIDO)
- **Dónde:** cualquier campo tipo "select" dentro de un modal de creación/edición (ej. "Módulo" en Tipos de documento, "Padre" en Plan de cuentas).
- **Causa:** el listado de opciones se renderizaba con `position: absolute` **dentro** del contenedor del modal (que tiene `overflow-y-auto`). Cuando el campo quedaba cerca del borde inferior visible, la lista de opciones se recortaba o quedaba detrás del overlay del modal, haciendo imposible seleccionar una opción.
- **Impacto:** bloqueaba silenciosamente el guardado de formularios (el usuario veía "Completa el campo «X»" sin entender por qué, ya que el selector parecía interactuable).
- **Fix:** `erp_front/src/components/ui/searchable-select.tsx` — el listado de opciones ahora se renderiza en un portal a `document.body` con posición `fixed` calculada dinámicamente (con flip hacia arriba si no hay espacio abajo), evitando el recorte por `overflow` del modal padre.
- **Verificado en:** TC11 (tipo de documento), y de forma indirecta en todos los formularios posteriores que usan selects en modales (TC13, TC16, TC18, TC19, TC24, TC28, TC33, TC39, etc.) — todos funcionaron sin fricción tras el fix.

### 🐛 H5 — Acciones de Plan de Cuentas solo por hover — **CORREGIDO**
Botones siempre visibles + `aria-label` + foco teclado (`PlanCuentasPage.tsx`).

### 🐛 H8 — Periodo Conciliación con placeholder engañoso — **CORREGIDO**
`defaultValue` desde periodo contable activo; toasts 5s.

## 3. Hallazgos H1–H8 (estado final 2026-07-29)

| ID | Estado | Nota |
|---|---|---|
| H1 | CERRADO | Toast de login + duración 5s; backend ya rechazaba inactivos. |
| H2 | CERRADO | No bug (timing agente). |
| H3 | CERRADO | Debounce preview plantilla 400ms. |
| H4 | CORREGIDO | Portal SearchableSelect. |
| H5 | CORREGIDO | Acciones plan cuentas visibles. |
| H6 | MONITOREO | Warning `pg` aislado; sin falla funcional. |
| H7 | CERRADO | No bug (automatización). |
| H8 | CORREGIDO | defaultValue Periodo conciliación. |

## 4. Detalle de casos por lote

### Lote 1 — Administración (TC01–TC07): 7/7 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC01 | Login admin + confirmar Modo Demo OFF | admin@almahue.local |
| TC02 | Crear empresa nueva | Empresa Prueba QA (RUT 76.111.111-1) |
| TC03 | Crear usuario habilitado | usuarioprueba1@test.com (U1) |
| TC04 | Usuario inhabilitado — intento 1 | usuarioIntento1@test.com (UINTENTO1) |
| TC05 | Usuario inhabilitado — intento 2 (otra empresa) | usuarioIntento2 / Empresa Intento 2 (RUT 76.222.222-2) |
| TC06 | Rol con permisos limitados | Rol Prueba QA (sidebar reducido verificado) |
| TC07 | Editar plantilla de documentos | Footer "Prueba QA" |

### Lote 2 — Parametrización (TC08–TC16): 9/9 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC08 | Moneda | PQA — Peso Prueba QA |
| TC09 | Unidad de medida | UPQ — Unidad Prueba QA |
| TC10 | Centro de costo | CC-PQA — Centro de Costo Prueba QA |
| TC11 | Tipo de documento | DOCPQA — Documento Prueba QA (módulo Comercial) |
| TC12 | Elemento de costo | EC-PQA — Elemento Costo Prueba QA |
| TC13 | Plan de cuentas (cuenta hija de CAJA) | 1-1-01-01-901 — Cuenta Prueba QA |
| TC14 | Proveedor | 77.888.999-K — Proveedor Prueba QA SpA |
| TC15 | Período contable | 2026-07 abierto |
| TC16 | Config SII | DOCPQA → 1-1-01-01-901 |

### Lote 3 — Maestros (TC17–TC20): 5/5 PASS (incluye tarifa TC18b)
| TC | Caso | Dato creado |
|---|---|---|
| TC17 | Cliente | 88.111.222-K — Cliente Prueba QA |
| TC18a | Contratista | 77.222.333-K — Contratista Prueba QA |
| TC18b | Tarifa de contratista | Cosecha manual/uva · $5.000/Caja · CC-PQA |
| TC19 | Insumo/artículo | INS-PQA — Insumo Prueba QA (UN) |
| TC20 | Bodega | BOD-PQA — Bodega Prueba QA |

### Lote 4 — Ventas (TC21–TC23): 3/3 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC21 | Cotización | Folio 2635 · Cliente Prueba QA · $100.000 |
| TC22 | Emitir factura y contabilizar | Folio 4692 · $150.000 · CONTABILIZADA |
| TC23 | Verificar libro de ventas | Asiento 20260001 · Debe=Haber $150.000 |

### Lote 5 — Compras (TC24–TC27): 4/4 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC24 | Orden de compra | OC-PQA-001 · $50.000 CLP |
| TC25 | Aprobar OC | OC-PQA-001 → APROBADA |
| TC26 | Recepcionar OC | TC 1 · $50.000 → CONFIRMADA |
| TC27 | Registrar factura de compra | FACT-PQA-001 · MATCH OK · EMITIDO |

### Lote 6 — Contratistas (TC28–TC32): 5/5 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC28 | Ingreso diario de labor | Contratista Prueba QA · 20 · $5.000 |
| TC29 | Asociación de labores → proforma | PRF-PQA-001 (calce OK) |
| TC30 | Proforma → definitiva → aprobación | $100.000 · DEFINITIVA (aprobador Admin Almahue) |
| TC31 | Facturar proforma | FACT-CONT-PQA-001 |
| TC32 | Traspaso / cierre mensual | Asiento 20260002 generado |

### Lote 7-8 — Bodega + Contabilidad (TC33–TC37): 5/5 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC33 | Movimiento de stock (entrada) | Insumo Prueba QA · 100 un · $1.500 · CONFIRMADO |
| TC34 | Asiento manual | Asiento 20260003 · $25.000 · CONTABILIZADO |
| TC35 | Verificar libro diario | 2026-07 · 3 asientos · Cuadrado |
| TC36 | Verificar mayor por cuenta | Cuenta Prueba QA $25.000 · CAJA $125.000 |
| TC37 | Centralización masiva | 4 asientos creados (ventas, compras, bodega) |

### Lote 9 — Tesorería (TC38–TC41): 4/4 PASS
| TC | Caso | Dato creado |
|---|---|---|
| TC38 | Importar cartola bancaria | cartola-prueba-qa.xlsx · Banco Chile · $300.000 · CARGADA |
| TC39 | Conciliación bancaria | Banco Chile · Jul 2026 · PENDIENTE |
| TC40 | Registrar pago | Proveedor Prueba QA · $150.000 CLP |
| TC41 | Registrar anticipo | Productor Prueba QA · $500.000 CLP |

## 5. Conclusión

El sistema Almahue ERP superó los 41 casos de prueba del flujo completo. Los bugs de producto de la suite (H4, H5, H8) y los hallazgos UX asociados (H1, H3) quedaron corregidos o mitigados. H2/H7 fueron falsos negativos de automatización. Solo H6 queda en monitoreo técnico (warning `pg` no bloqueante). Diferidos externos del ERP (GoSocket, cuentas corrientes, etc.) están en `DEFINICIONES_PENDIENTES.md`, no en esta suite.

**Evidencia completa:** 41 carpetas `TC##-*` en este directorio con capturas de pantalla de cada paso relevante. Detalle caso por caso, notas de verificación y hallazgos técnicos completos en `00-PLAN-MAESTRO.md`.
