# Definiciones pendientes — ERP Almahue

**Fecha:** 2026-07-29 (actualizado implementación)  
**Propósito:** partidas diferidas; las codeables de este doc ya están implementadas salvo bloqueantes externos.  
**Estado del código factible:** ver checklist abajo + suite QA `qa-pruebas-flujo-completo-2026-07-29/`.

---

## Cómo usar este documento

| Columna | Significado |
|---|---|
| **Bloqueante** | Qué falta recibir / decidir antes de cerrar en prod |
| **Contrato propuesto** | Diseño (rutas, modelos, UX) |
| **Criterio de aceptación** | Qué debe pasar para marcarlo DONE |

---

## 1. GoSocket / DTE productivo — **código listo · keys pendientes**

| | |
|---|---|
| **Fuente** | Reu3 D7 · docs técnicos enterprise |
| **Estado actual** | `POST /dtes/emitir`, `GET /dtes/:id/estado`, `POST /dtes/sincronizar` (+ alias `/dtes/sync`). Modelo `DteEnvio` (cola, reintentos backoff). Idempotencia `@@unique([empresaId, folio, tipo])`. Estado `EMITIDO_SII`. Env en `.env.example`. UI: botón **Emitir DTE** en Libro comercial (docs CONTABILIZADA). Sin keys → stub local `ENVIADO`. |
| **Bloqueante** | `GOSOCKET_API_URL`, `GOSOCKET_API_KEY`, `GOSOCKET_EMPRESA_RUT`, ambiente SII cert/prod. |
| **Criterio de aceptación** | Emitir 1 factura en cert. SII, ver estado en UI, folio/track persistido. |
| **Fuera de alcance hasta keys** | CAF, timbre PDF SII oficial. |

---

## 2. Cuentas corrientes — **IMPLEMENTADO**

| | |
|---|---|
| **Fuente** | Validación Sergio |
| **Estado actual** | Modelo `CuentaCorrienteMovimiento`. API: `GET /cuentas-corrientes`, `GET /cuentas-corrientes/:terceroId/movimientos`, `POST /cuentas-corrientes/ajuste`. UI `/tesoreria/cuentas-corrientes` (+ link Contabilidad › Operaciones). Hooks: venta/NC al contabilizar, compra CONTABILIZADA, pago, anticipo productor. |
| **Criterio de aceptación** | Factura cliente → debe; pago proveedor → debe (reduce acreedor); saldo visible en kardex. |

---

## 3. Cartola banco-específica / PDF escaneado — **scaffold listo · muestras pendientes**

| | |
|---|---|
| **Fuente** | Reu2 |
| **Estado actual** | Carpeta `erp_back/src/modules/tesoreria/parsers/` (`detectBank`, stubs Chile/Estado/Santander). Mensaje “Formato no reconocido — adjunte muestra…”. OCR **no** implementado (sin muestras). |
| **Bloqueante** | Muestra real Agustín (PDF/Excel por banco). |
| **Criterio de aceptación** | ≥95% filas en cartola real de cada banco. |

---

## 4. Datos maestros Excel oficiales — **pipeline listo · Excel definitivo pendiente**

| | |
|---|---|
| **Fuente** | Mario |
| **Estado actual** | Seed + `scripts/import-plan-cuentas.ts` + import UI plan cuentas. Estados bodega ya tipados en dominio. |
| **Bloqueante** | Excel oficial definitivo firmado por cliente. |

---

## 5. Cron Banco Central 9:00 — **IMPLEMENTADO (activar en prod)**

| | |
|---|---|
| **Fuente** | Reu3 D13 |
| **Estado actual** | `@nestjs/schedule` + `BcSyncCron` lun–vie 09:00 `America/Santiago`. Env `BC_CRON_ENABLED=true`. `SyncBcMeta.lastStatus` / `lastError` / `failStreak` (alerta log si ≥ 2). |
| **Bloqueante** | Deploy con `BC_CRON_ENABLED=true`. |
| **Criterio de aceptación** | Logs 09:00 CLT + series UF/USD actualizadas. |

---

## 6. Reportería PDF avanzada por módulo — **diferido (UI visual)**

| | |
|---|---|
| **Estado actual** | Export CSV/Excel + print HTML plantilla documentos. |
| **Nota** | Fuera de esta pasada (interfaz visual). Prioridad cuando producto indique pantallas piloto. |

---

## 7. Assets reales de marca (logo / sello) — **diferido (assets cliente)**

| | |
|---|---|
| **Estado actual** | Plantilla documentos ya permite upload logo/sello. |
| **Bloqueante** | Archivos oficiales del cliente. Sin cambio de código. |

---

## 8. Libro comercial unificado + Libro despachos — **IMPLEMENTADO**

| | |
|---|---|
| **Fuente** | Sergio / docs técnicos enterprise |
| **Estado actual** | Ruta `/comercial/libro` con tabs Ventas \| Compras \| Despachos. API `GET /libro-comercial?ambito=`. Modelo `GuiaDespacho` + `POST /guias-despacho`. |
| **Nota** | Libro de compras legacy (`/compras/registro`) se mantiene. |

---

## Resumen de ownership

| Ítem | Owner externo | Estado código |
|---|---|---|
| GoSocket prod | Cliente / keys | Listo; falta keys |
| Cuentas corrientes | — | **DONE** |
| Cartola banco-específica | Agustín (muestras) | Scaffold; falta calibrar |
| Excel maestros | Mario | Pipeline listo |
| Cron BC 9am | Ops (`BC_CRON_ENABLED`) | **DONE** (activar en prod) |
| PDF avanzado | Feedback pantallas | Diferido (UI) |
| Logo/sello | Cliente (assets) | Solo carga UI |
| Libro unificado | — | **DONE** |

---

## Fuentes docs técnicos (2026-07-29)

Copiados en `docs/erp-planificacion/agrosoft-levantamiento/fuentes/docs-tecnicos-enterprise/`:

- `ERP-Contable-Financiero-Enterprise.pdf`
- `Modulo-Comercial-Documento-Tecnico-Enterprise.pdf`

---

## 9. Cotizaciones + reglas de aprobación OC — **IMPLEMENTADO**

| | |
|---|---|
| **Fuente** | María Jesús / reu aprobaciones |
| **Estado actual** | Cotizaciones: ver/editar/emitir/convertir (NP|Factura)/anular/PDF. Admin › Reglas de aprobación (`aprobadorIds`). OC con jefe aprobador; bandeja Compras › Aprobaciones filtrada por jefe. Edición real: bodegas, movimientos, anticipos. |
| **Nota** | Cotizaciones **sin** workflow de aprobación (solo ciclo comercial). Proformas siguen en su pantalla. |

---

## Fixes previos (2026-07-29)

1. Elementos de costo / honorarios `PUT`  
2. H4 SearchableSelect portal  
3. H5 Plan de cuentas acciones visibles  
4. H8 Periodo en Conciliación  
5. PC-04 `assertPeriodoAbierto`  
6. Toasts 5s + closeButton  
7. eslint.config.js front  
8. Cotizaciones CRUD + convertir; Admin workflows; OC jefe aprobador  
9. Anticipos/bodegas/movimientos `PUT` real  

