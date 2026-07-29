# Definiciones pendientes — ERP Almahue

**Fecha:** 2026-07-29  
**Propósito:** dejar especificadas (listas para implementar) las partidas diferidas que **no** se pueden cerrar sin datos, credenciales o decisiones externas.  
**Estado del código factible:** cerrado (ver `CHECKLIST_CIERRE_100.md`, `CHECKLIST_QA_REUNIONES_2026-07-28.md`, suite QA `qa-pruebas-flujo-completo-2026-07-29/`).

---

## Cómo usar este documento

| Columna | Significado |
|---|---|
| **Bloqueante** | Qué falta recibir / decidir antes de codear |
| **Contrato propuesto** | Diseño listo (rutas, modelos, UX) para el próximo sprint |
| **Criterio de aceptación** | Qué debe pasar para marcarlo DONE |

---

## 1. GoSocket / DTE productivo

| | |
|---|---|
| **Fuente** | Reu3 D7 · checklist residual #1 |
| **Estado actual** | Panel de consulta en `/integraciones/gosocket`. Sync real solo si existen env vars. |
| **Bloqueante** | `GOSOCKET_API_URL`, API key / token de producción, ambiente SII (certificación vs prod), decisión de quién emite (Almahue vs GoSocket como intermediario). |
| **Contrato propuesto** | |
| | 1. Env: `GOSOCKET_API_URL`, `GOSOCKET_API_KEY`, `GOSOCKET_EMPRESA_RUT` (por tenant). |
| | 2. Endpoints back: `POST /dtes/emitir`, `GET /dtes/:id/estado`, `POST /dtes/sincronizar` (ya hay stub de listado). |
| | 3. Flujo: Libro ventas → documento CONTABILIZADO → Emitir DTE → estado `EMITIDO_SII` / `RECHAZADO`. |
| | 4. Idempotencia por `folio + tipo + empresaId`. |
| | 5. No loguear tokens; reintentos con backoff; cola simple en BD (`DteEnvio`). |
| **Criterio de aceptación** | Emitir 1 factura de prueba en cert. SII, ver estado en UI, folio SII persistido y visible en Libro ventas. |
| **Fuera de alcance hasta recibir keys** | Emisión real, CAF, timbre PDF SII. |

---

## 2. Cuentas corrientes (menú Sergio / DTEMITE)

| | |
|---|---|
| **Fuente** | Validación Sergio · residual cuentas corrientes |
| **Estado actual** | Gap. Anticipos productores y conciliación bancaria cubren parte del dominio, pero no hay módulo “Cuentas corrientes”. |
| **Bloqueante** | Confirmación de producto: ¿CC de clientes, proveedores, o ambos? ¿Saldo por documento o por tercero? |
| **Contrato propuesto (asumiendo clientes + proveedores)** | |
| | **Ruta UI:** `/tesoreria/cuentas-corrientes` (también link en Contabilidad › Operaciones si se alinea a Sergio). |
| | **Modelo Prisma:** |
| | ``` |
| | model CuentaCorrienteMovimiento { |
| |   id String @id |
| |   empresaId String |
| |   terceroTipo  // CLIENTE \| PROVEEDOR \| PRODUCTOR |
| |   terceroId String |
| |   terceroNombre String |
| |   fecha DateTime |
| |   documentoRef String?   // folio factura / NC / pago |
| |   documentoTipo String? |
| |   debe Decimal |
| |   haber Decimal |
| |   saldo Decimal |
| |   glosa String? |
| |   origen String?         // VENTA \| COMPRA \| PAGO \| ANTICIPO \| AJUSTE |
| |   createdAt DateTime |
| | } |
| | ``` |
| | **Pantallas:** |
| | 1. Listado de terceros con saldo actual (filtros: tipo, buscar, saldo ≠ 0). |
| | 2. Detalle (kardex) del tercero: movimientos ordenados + saldo corrido. |
| | 3. Botón “Registrar ajuste” (manual, genera asiento opcional). |
| | **Sinergias:** al contabilizar venta/compra y al registrar pago/anticipo → append movimiento. |
| | **API:** `GET /cuentas-corrientes`, `GET /cuentas-corrientes/:terceroId/movimientos`, `POST /cuentas-corrientes/ajuste`. |
| **Criterio de aceptación** | Crear factura cliente → aparece debe en CC; registrar pago → haber; saldo cuadra con aging/nóminas. |
| **Decisión pendiente (producto)** | ¿Vive bajo Tesorería, Contabilidad, o ambos (shortcut)? Recomendación: Tesorería canónico + link en Contabilidad. |

---

## 3. Cartola banco-específica / PDF escaneado

| | |
|---|---|
| **Fuente** | Reu2 / flujo · residual cartola |
| **Estado actual** | Parser genérico Excel/CSV/PDF de texto (`cartola-parser.util.ts`). PDF escaneado (imagen) no soportado. Formatos banco-específicos no calibrados. |
| **Bloqueante** | Muestra real de Agustín (PDF/Excel Banco Chile / Estado / Santander). |
| **Contrato propuesto** | |
| | 1. Carpeta `erp_back/src/modules/tesoreria/parsers/` con un parser por banco (`banco-chile.ts`, …) + `detectBank(file)`. |
| | 2. Contrato de salida unificado: `{ fecha, glosa, cargo, abono, saldo, referencia }[]`. |
| | 3. PDF escaneado: OCR opcional (Tesseract o servicio) **solo** si llegan muestras; no implementar OCR a ciegas. |
| | 4. UI: al fallar parse genérico, mensaje “Formato no reconocido — adjunte muestra al equipo” + descarga del archivo original en log. |
| **Criterio de aceptación** | Importar 1 cartola real de cada banco solicitado → ≥95% filas parseadas; calce manual de 1 movimiento. |

---

## 4. Datos maestros Excel oficiales del cliente

| | |
|---|---|
| **Fuente** | Dependencia Mario · residual maestros |
| **Estado actual** | Seed con plan 396 / CC 233 / elementos 208 (Exceles ya procesados 28/07). Estados de bodega razonables en seed. |
| **Bloqueante** | Excel “oficial definitivo” + catálogo de estados de bodega firmado por cliente. |
| **Contrato propuesto** | |
| | 1. Mantener pipeline actual: JSON en `prisma/data/*` + `seed.ts` + import Excel en Plan de cuentas. |
| | 2. Al recibir Excel nuevo: reemplazar JSON vía `scripts/import-plan-cuentas.ts` (ya existe) y re-seed en staging. |
| | 3. Estados bodega: tabla `EstadoMovimientoBodega` o enum Prisma acordado; UI select desde catálogo. |
| **Criterio de aceptación** | Import sin errores; conteos validados por Mario; 0 códigos huérfanos en OC/insumos. |

---

## 5. Cron Banco Central 9:00 (producción)

| | |
|---|---|
| **Fuente** | Reu3 D13 · residual cron BC |
| **Estado actual** | Sync manual OK (`Indicadores BC`). Cron prod no validado en el servidor. |
| **Bloqueante** | Acceso deploy / confirmación de scheduler en el host (systemd timer, cron Docker, o Nest `@Cron`). |
| **Contrato propuesto** | |
| | 1. Nest: `@Cron('0 9 * * 1-5', { timeZone: 'America/Santiago' })` llamando al mismo servicio de sync mindicador. |
| | 2. Env: `BC_CRON_ENABLED=true` solo en prod. |
| | 3. Log + fila `SyncBcMeta` con `lastRunAt`, `lastStatus`, `lastError`. |
| | 4. Alerta (toast admin / mail) si falla 2 días seguidos. |
| **Criterio de aceptación** | Tras deploy, verificar en logs del servidor ejecución 09:00 CLT y series UF/USD actualizadas. |

---

## 6. Reportería PDF avanzada por módulo

| | |
|---|---|
| **Fuente** | Cierre 100 · DEFERRED |
| **Estado actual** | Export CSV/Excel en DataTable (`enableExport`). Print HTML de documentos comerciales con plantilla. |
| **Bloqueante** | Feedback de pantallas prioritarias (¿libro diario PDF? ¿OC PDF? ¿proforma?). |
| **Contrato propuesto** | |
| | 1. Reutilizar `documentoPrint.ts` / plantilla empresa. |
| | 2. Por módulo: botón “PDF” que genera HTML → `window.print` o pdf-lib si se pide archivo. |
| | 3. Prioridad sugerida: (1) Factura/cotización, (2) OC, (3) Proforma, (4) Libro diario. |
| **Criterio de aceptación** | PDF legible A4 con logo/colores de plantilla; una pantalla piloto aprobada por cliente. |

---

## 7. Assets reales de marca (logo / sello cotización-OC)

| | |
|---|---|
| **Fuente** | Interno I5 |
| **Estado actual** | Plantilla documentos configurable (colores, tipografía, logo upload base64, pie). Límite body 15MB. |
| **Bloqueante** | Archivos oficiales de logo y sello del cliente (PNG/SVG). |
| **Contrato propuesto** | Subir en Admin › Plantilla documentos; sin cambio de código adicional. |
| **Criterio de aceptación** | Impresión de cotización/OC con logo y sello reales, sin overflow. |

---

## 8. Libro comercial unificado + Libro despachos

| | |
|---|---|
| **Fuente** | Sergio / producto |
| **Estado actual** | Libro ventas y Libro compras separados (decisión de producto actual). |
| **Bloqueante** | Decisión explícita de unificar vs mantener separados. |
| **Contrato propuesto (si se unifica)** | |
| | Ruta `/comercial/libro` con tabs Ventas \| Compras \| Despachos. |
| | Despachos: modelo `GuiaDespacho` o tipo documento `GD` enlazado a factura. |
| **Criterio de aceptación** | Aprobado en demo con cliente; permisos pantalla actualizados. |

---

## Resumen de ownership

| Ítem | Owner externo | ¿Puede codearse ya? |
|---|---|---|
| GoSocket prod | Cliente / keys | No |
| Cuentas corrientes | Producto (decisión scope) | **Sí (spec arriba)** — esperar OK de producto |
| Cartola banco-específica | Agustín (muestras) | No |
| Excel maestros | Mario | Parcial (pipeline listo) |
| Cron BC 9am | Ops / deploy | **Sí** en próximo deploy |
| PDF avanzado | Feedback pantallas | Parcial |
| Logo/sello | Cliente (assets) | Solo carga UI |
| Libro unificado | Producto | No hasta decisión |

---

## Fixes de código cerrados en esta pasada (2026-07-29)

Ya no son residuales abiertos:

1. ~~Elementos de costo / honorarios sin PATCH~~ → `PUT` implementado.  
2. ~~H4 SearchableSelect en modales~~ → portal fixed.  
3. ~~H5 Plan de cuentas solo hover~~ → acciones siempre visibles + a11y.  
4. ~~H8 placeholder Periodo en Conciliación~~ → `defaultValue` desde periodo activo.  
5. ~~PC-04 periodo → ventas/asientos~~ → `assertPeriodoAbierto` al contabilizar.  
6. ~~Toasts demasiado breves~~ → duración 5s + closeButton.  
7. ~~eslint.config.js faltante~~ → flat config ESLint 9+.
