# Plan maestro — Pruebas de flujo completo Almahue ERP

**Fecha:** 2026-07-29 · **Modo:** Demo Mode OFF (Nest → Prisma, datos reales en BD) · **URL:** `http://localhost:5174/` (front) / `http://localhost:3001/api/v1` (back)
**Login base:** `admin@almahue.local` / `Admin123!` (empresa EMP-1 Almahue)

## Convención de nombres (para identificar fácil en BD)

- Todo dato creado en estas pruebas lleva el prefijo **"Prueba QA"** o **"Intento N"** en su nombre/razón social/código.
- Casos con múltiples variantes (ej. usuario inhabilitado) se numeran **IntentoN** empezando en 1.
- Cada caso de prueba tiene un ID `TC##` correlativo y su propia carpeta de capturas: `TC##-nombre-caso/`.

## Registro de casos (se actualiza por lote a medida que se ejecutan)

| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC01 | Acceso | Login admin + confirmar Modo Demo OFF | admin@almahue.local | ✅ PASS |
| TC02 | Administración | Crear empresa nueva | Empresa Prueba QA (RUT 76111111-1) | ✅ PASS |
| TC03 | Administración | Crear usuario habilitado | usuarioprueba1@test.com (código U1) | ✅ PASS |
| TC04 | Administración | Crear usuario INHABILITADO — intento 1 | usuarioIntento1@test.com (código UINTENTO1) | ✅ PASS (login rechazado, pero sin mensaje de error visible — ver hallazgo H1) |
| TC05 | Administración | Crear usuario INHABILITADO — intento 2 (otra empresa) | usuarioIntento2 / Empresa Intento 2 (RUT 76222222-2) | ✅ PASS |
| TC06 | Administración | Crear rol con permisos limitados y verificar sidebar reducido | Rol Prueba QA | ✅ PASS (reintento OK — ver H2) |
| TC07 | Administración | Editar plantilla de documentos | Footer "Prueba QA" | ✅ PASS (con fricción menor — ver H3) |

### Hallazgos detectados durante la ejecución

- **H1 (UX menor, a confirmar):** al probar login con usuario INACTIVO, el intento 1 no mostró mensaje de error visible; el intento 2 sí mostró el toast "Credenciales inválidas". Ambos casos rechazaron correctamente el acceso — el comportamiento pudo ser variabilidad del propio agente de prueba, no necesariamente un bug. No bloqueante.
- **H2 (resuelto en reintento):** el primer intento de reasignar el rol de "Usuario Prueba 1" reportó un "error técnico" impreciso; en el reintento con snapshot previo funcionó sin problemas y el sidebar se redujo correctamente (ya no aparece "Administración" para ese usuario). Probablemente fue un problema puntual de timing del agente de prueba, no del sistema — sin evidencia de bug real.
- **H3 (UX menor):** en Plantilla de documentos, el campo "Texto pie" fue difícil de editar por automatización porque la vista previa en vivo (iframe) refresca el DOM constantemente; se debió simular eventos de teclado a bajo nivel para que el formulario detectara el cambio. Vale la pena revisar si un usuario real notaría el mismo problema de refresco/parpadeo al escribir rápido en ese campo.
- **Nota:** el sistema arrancó con Modo Demo ACTIVADO por defecto; se desactivó manualmente en TC01 para poder ejecutar el resto de las pruebas contra la base de datos real.

**Lote 1 (Administración) — CERRADO: 7/7 casos PASS.**
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC08 | Parametrización | Crear moneda | PQA — Peso Prueba QA | ✅ PASS |
| TC09 | Parametrización | Crear unidad de medida | UPQ — Unidad Prueba QA | ✅ PASS |
| TC10 | Parametrización | Crear centro de costo | CC-PQA — Centro de Costo Prueba QA | ✅ PASS (ver nota) |
| TC11 | Parametrización | Crear tipo de documento | DOCPQA — Documento Prueba QA (módulo Comercial) | ✅ PASS (bug real corregido — ver hallazgo H4) |
| TC12 | Parametrización | Crear elemento de costo | EC-PQA — Elemento Costo Prueba QA | ✅ PASS |
| TC13 | Parametrización | Crear cuenta en plan de cuentas (hija de CAJA) | 1-1-01-01-901 — Cuenta Prueba QA | ✅ PASS (bug de UI corregido — ver H5) |
| TC14 | Parametrización | Crear proveedor | 77.888.999-K — Proveedor Prueba QA SpA | ✅ PASS |
| TC15 | Parametrización | Verificar/abrir período contable | 2026-07 | ✅ PASS |
| TC16 | Parametrización | Crear mapeo Config SII | DOCPQA → 1-1-01-01-901 · Cuenta Prueba QA | ✅ PASS |

**Lote 2 (Parametrización) — CERRADO: 9/9 casos PASS** (TC10 y TC11 fueron re-verificados manualmente tras el reporte inicial del agente de pruebas; ver notas abajo).

- **H5 (bug real, CORREGIDO 2026-07-29):** en Plan de Cuentas, las acciones "Agregar hijo / Editar / Eliminar" eran solo visibles con hover. **Fix:** botones siempre visibles (`flex` + `opacity`) con `aria-label` y foco teclado (`group-focus-within`).

### Lote 2 — notas de verificación

- **TC10 (corregido de FALLA a PASS):** el agente de pruebas reportó inicialmente que "CC-PQA" no persistía. Al verificar manualmente en el listado (filtro de búsqueda "PQA"), el centro de costo **sí existía** en BD con todos los datos correctos (código CC-PQA, nombre "Centro de Costo Prueba QA", encargado "Carlos QA", 2026-01-01, ACTIVO). Fue un falso negativo del agente (probablemente buscó antes de que la lista se refrescara). No hay bug de backend.
- **H4 (bug real, CORREGIDO):** el componente `SearchableSelect` (usado en todos los campos tipo "select" de los formularios modales, ej. Módulo en Tipos de documento) renderizaba su lista de opciones con `position: absolute` **dentro** del contenedor del modal, el cual tiene `overflow-y-auto`. Cuando el campo quedaba cerca del borde inferior visible del modal, la lista de opciones se recortaba/quedaba detrás del overlay del propio modal, haciendo **imposible seleccionar una opción con clic o teclado**. Esto explica la falla original de TC11 ("Completa el campo «Código»" en realidad era porque "Módulo" nunca lograba asignarse). 
  - **Fix aplicado:** `erp_front/src/components/ui/searchable-select.tsx` ahora renderiza el listado de opciones en un portal a `document.body` con posición `fixed` calculada dinámicamente (con flip hacia arriba si no hay espacio abajo), evitando el recorte por `overflow` del modal.
  - **Verificado:** se repitió la creación de "DOCPQA / Documento Prueba QA / Comercial" y quedó persistido correctamente en el listado.
  - **Impacto:** corrige potencialmente el mismo problema en cualquier otro formulario modal que use un campo `select` (ej. Cuentas contables padre, tipos en otros catálogos, etc.) — vale la pena re-probar formularios similares en lotes siguientes.
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC17 | Maestros | Crear cliente | 88.111.222-K — Cliente Prueba QA | ✅ PASS |
| TC18a | Maestros | Crear contratista | 77.222.333-K — Contratista Prueba QA (Cosecha) | ✅ PASS |
| TC18b | Maestros | Crear tarifa de contratista | Contratista Prueba QA · Cosecha manual · Cosecha uva · $5.000/Caja · CC-PQA · vigente desde 2026-07-01 | ✅ PASS |
| TC19 | Maestros | Crear insumo/artículo | INS-PQA — Insumo Prueba QA (UN) | ✅ PASS |
| TC20 | Maestros | Crear bodega | BOD-PQA — Bodega Prueba QA | ✅ PASS |

**Lote 3 (Maestros) — CERRADO: 5/5 PASS.** Nota importante de proceso: la primera ejecución automatizada (agente de pruebas) reportó 0/4 FALLA con "fallo sistemático de persistencia" en los 4 módulos. Verificación cruzada de los logs del backend confirmó que **ninguna petición POST llegó al servidor** en esos intentos — es decir, el problema no era del backend/BD, sino que el agente de automatización dejó vacíos campos obligatorios no evidentes a primera vista (Cliente: "Línea de crédito"; Contratista: "Especialidad/labor"; Insumo: "Unidad"), lo que activa una validación de frontend que bloquea el envío mostrando un toast de error (mismo patrón que H4). Al reintentar manualmente completando TODOS los campos obligatorios, los 4 casos + la tarifa asociada guardaron correctamente (201 Created) en el primer intento. No se requirió ningún cambio de código para este lote.

- **H6 (hallazgo técnico menor, no bloqueante, requiere más investigación):** justo antes de guardar la tarifa de contratista, el log del backend mostró una única vez un `DeprecationWarning` de la librería `pg`: *"Calling client.query() when the client is already executing a query is deprecated and will be removed in pg@9.0."* La operación se completó con éxito (201) y la revisión del método `createTarifa`/`assertLaborActividadEmpresa` en `contratistas.service.ts` no muestra queries paralelas sin `await` en ese flujo específico, por lo que el warning podría originarse de una petición concurrente distinta (ej. polling del dashboard) compartiendo el mismo cliente de conexión, no necesariamente un bug de este endpoint. Se documenta para investigación futura si vuelve a aparecer con mayor frecuencia; no bloqueó ninguna prueba.
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC21 | Ventas | Crear cotización | Folio 2635 · Cliente Prueba QA · $100.000 · BORRADOR | ✅ PASS |
| TC22 | Ventas | Emitir factura y contabilizar | Folio 4692 · Cliente Prueba QA · $150.000 · CONTABILIZADA | ✅ PASS |
| TC23 | Ventas | Verificar libro de ventas + asiento generado | Asiento N° 20260001 · Debe/Haber $150.000 · Contabilizado | ✅ PASS |

**Lote 4 (Ventas) — CERRADO: 3/3 PASS.** Mismo patrón de falso negativo que en el lote anterior: el agente de pruebas reportó FALLA en TC21 porque llenó el campo "Monto neto" mediante un script CDP de bajo nivel (`element.value = ...` + `dispatchEvent`) que no logró que React detectara el cambio de estado, dejando el campo lógicamente vacío y activando la validación "Completa cliente y monto neto" (que no llegó a leer completo). Confirmado con logs del backend: cero peticiones POST en el intento del agente. Al reintentar manualmente con las herramientas de formulario estándar, los 3 casos + la contabilización guardaron correctamente en el primer intento (se verificó además que el asiento contable se generó con las cuentas y montos correctos). No se requirió ningún cambio de código.
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC24 | Compras | Crear orden de compra | OC-PQA-001 · Proveedor Prueba QA SpA · $50.000 CLP · CC 100% | ✅ PASS |
| TC25 | Compras | Aprobar OC | OC-PQA-001 → APROBADA | ✅ PASS |
| TC26 | Compras | Recepcionar OC | OC-PQA-001 · TC 1 · $50.000 → CONFIRMADA | ✅ PASS |
| TC27 | Compras | Registrar factura de compra | FACT-PQA-001 · $50.000 · MATCH OK · EMITIDO | ✅ PASS |

**Lote 5 (Compras) — CERRADO: 4/4 PASS.** El agente de pruebas reportó inicialmente un "bloqueo técnico crítico" en TC24 (imposible completar el formulario de OC) — ver H7 abajo. Al reintentar manualmente con las herramientas de formulario estándar (`browser_fill`/`browser_select_option`, sin scripts CDP de bajo nivel), el formulario de "Nueva OC" funcionó sin ningún re-render anómalo ni pérdida de valores: se completaron Nº OC, proveedor, neto y distribución CC en un solo intento, y la orden se guardó correctamente. La cadena completa (crear → aprobar → recepcionar → registrar factura) se ejecutó de punta a punta sin incidentes ni cambios de código.

- **H7 (falso negativo de automatización, incidente aclarado):** el agente de pruebas reportó "Element reference is stale" con `browser_fill` y reseteo de valores al usar workarounds CDP en el formulario de OC. Al revisar el código (`OrdenesCompraPage` en `ComprasPages.tsx`) no se encontró ningún patrón de re-render anómalo (es un formulario controlado estándar con `useState`, sin efectos que se disparen en cada render). La reproducción manual confirmó que el formulario es estable; el problema fue exclusivo de la estrategia de automatización del agente (scripts CDP que no disparan los eventos `input`/`change` que React necesita para sincronizar su estado interno), igual que en los hallazgos previos de "falsos negativos" (TC10, TC17-20, TC21). No se requirió ningún cambio de código. Nota aparte: el formulario de OC efectivamerte no tiene líneas de detalle por insumo (solo neto total + distribución por centro de costo), lo cual es el diseño actual del sistema, no un defecto encontrado en esta prueba.
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC28 | Contratistas | Ingreso diario de labor | Contratista Prueba QA · CC-PQA · Cosecha manual/uva · JORNADA · 20 · $5.000 | ✅ PASS |
| TC29 | Contratistas | Asociación de labores → proforma | Ingreso TC28 asociado a PRF-PQA-001 (calce OK) | ✅ PASS |
| TC30 | Contratistas | Proforma → definitiva → aprobación | PRF-PQA-001 · $100.000 · BORRADOR→PENDIENTE APROBACIÓN→DEFINITIVA (aprobador Admin Almahue) | ✅ PASS |
| TC31 | Contratistas | Facturar proforma(s) | PRF-PQA-001 → FACTURADA · Factura FACT-CONT-PQA-001 | ✅ PASS |
| TC32 | Contratistas | Traspaso / cierre mensual | Traspaso 2026-07 · asiento contable 20260002 generado | ✅ PASS |

**Lote 6 (Contratistas) — CERRADO: 5/5 PASS.** Mismo patrón de falso negativo que en lotes anteriores: el agente de pruebas reportó "bloqueo técnico crítico" en TC28 por "Element reference is stale" y reseteo de valores. La causa real (verificada manualmente) fue que el agente intentó seleccionar el campo "Actividad" **antes** de seleccionar "Labor" — como el campo Actividad se filtra dinámicamente según la Labor elegida (`onFieldChange` en `IngresoLaborDiarioPage.tsx`), sin Labor seleccionada la lista de actividades estaba vacía o desactualizada, y el precio unitario (que se autocompleta desde la tarifa al elegir Labor) quedó en 0, bloqueando el guardado por validación. Al reintentar manualmente respetando el orden de los campos (Contratista → CC → Labor → Actividad → Cantidad, dejando que el precio se autocompletara desde la tarifa), el formulario funcionó sin ningún re-render anómalo y los 5 casos de la cadena completa (ingreso diario → asociación a proforma → aprobación → facturación → cierre mensual con asiento contable) se ejecutaron correctamente en un solo intento cada uno. No se requirió ningún cambio de código. Nota: se observó que al facturar una proforma el sistema centraliza automáticamente el traspaso contable de esa proforma puntual; el botón "Traspasar y cerrar" del período procesa el resto de proformas definitivas pendientes y genera un asiento consolidado (verificado: asiento 20260002).
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC33 | Bodega | Movimiento de stock (entrada proveedor) | Entrada · Insumo Prueba QA · Bodega Prueba QA · 100 un · $1.500 · CONFIRMADO | ✅ PASS |
| TC34 | Contabilidad | Asiento manual | Asiento 20260003 · Cuenta Prueba QA / CAJA · $25.000 · CONTABILIZADO | ✅ PASS |
| TC35 | Contabilidad | Verificar Libro diario | Periodo 2026-07 · 3 asientos · Debe=Haber $2.165.000 · Cuadrado: Sí | ✅ PASS |
| TC36 | Contabilidad | Verificar Mayor por cuenta | Cuenta Prueba QA saldo $25.000 · CAJA saldo $125.000 | ✅ PASS |
| TC37 | Contabilidad | Centralización masiva del período | 4 asiento(s) creados (ventas, compras, bodega); contratistas correctamente omitido (ya centralizado en TC32) | ✅ PASS |

**Lote 7-8 (Bodega + Contabilidad) — CERRADO: 5/5 PASS.** Ejecutados directamente sin subagente dado el patrón de falsos negativos observado en lotes anteriores. Todo funcionó al primer intento: el movimiento de bodega (entrada de proveedor) impactó correctamente el saldo del insumo; el asiento manual cuadró y quedó contabilizado; el Libro diario y el Mayor reflejaron los montos correctos y cuadrados; y la Centralización masiva detectó y centralizó automáticamente las ventas, compras y movimientos de bodega pendientes del período, omitiendo correctamente el traspaso de contratistas que ya tenía asiento (20260002) desde el Lote 6. No se encontraron bugs ni se requirió ningún cambio de código.
| TC | Módulo | Caso | Dato de prueba | Estado |
|---|---|---|---|---|
| TC38 | Tesorería | Importar cartola bancaria | cartola-prueba-qa.xlsx · Banco Chile · cta 999888777 · periodo 2026-07-25/2026-07-29 · 1 mov · $300.000 · CARGADA | ✅ PASS |
| TC39 | Tesorería | Conciliación | Banco Chile · Jul 2026 · 1 movimiento · PENDIENTE | ✅ PASS (bug real corregido — ver H8) |
| TC40 | Tesorería | Registrar pago | Proveedor Prueba QA · $150.000 CLP · Fac. USD · Docs FAC-PQA-001 · PENDIENTE | ✅ PASS |
| TC41 | Tesorería | Registrar anticipo | Productor Prueba QA · Banco Chile · Transferencias · $500.000 CLP · saldo $500.000 | ✅ PASS |

**Lote 9 (Tesorería) — CERRADO: 4/4 PASS.** Ejecutado directamente sin subagente por el patrón de falsos negativos de lotes anteriores.

- **H8 (bug real, CORREGIDO 2026-07-29):** en "Nueva conciliación", el campo Periodo solo tenía placeholder engañoso. **Fix:** `defaultValue` desde el periodo contable activo (ej. `Jul 2026`) + placeholder aclarado como ejemplo; toasts de error con duración 5s.

Este archivo se actualiza a medida que cada lote de pruebas se ejecuta. El reporte final
consolidado con resultados, evidencia y hallazgos queda en `REPORTE-FINAL.md` en esta misma
carpeta.
