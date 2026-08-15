# Veredicto encargado de proyecto — Pipeline QA integral 15/08/2026

**Rol:** Encargado de proyecto (MJ / Agustín)  
**Fecha:** 2026-08-15  
**Alcance revisado:** Plan v1 (225 casos) → Análisis integridad → Plan v2 (215 casos) → Ola A (29 casos ejecutados) + huecos `AGENTS.md` / `HUERFANOS-H1-H14.md`  
**Audiencia:** Steering piloto Almahue — decisión demo cliente y despliegue producción

---

## 1. Resumen ejecutivo (1 página)

### ¿Listo para demo con el cliente?

**Condicional — GO local con guion acotado.** El núcleo comercial e inventario del piloto **funciona en entorno local** tras la Ola A: smoke completo, wizard Emitir unificado (solo FACTURA/NC/ND/GUIA), lookup RUT con productor, aislamiento tenant, guías de despacho y datos seed `ALM-*` verificados. Jest backend: **150 tests PASS**.

No es aún una **validación integral** del piloto. La Ola A ejecutó **29 de ~55 casos P0** previstos; faltan retests críticos de aprobación OV (VEN-009–012), match 3 vías compras (CMP-012–013), NC → reingreso bodega (INV-010), re-login AdminConcepto (ADM-022) y el recorrido golden filmado (E2E-001, E2E-004/005). Billing stub DTE (**BIL-001/002**) quedó **BLOCKED** por configuración `.env`, no por defecto de producto.

**Recomendación demo:** mostrar Recorrido B (OV → stock → Emitir) y Recorrido A parcial (cotización → OC → aprobación) **solo en local** con seed `demo-propuesta`, evitando contabilizar factura con folio stub hasta activar flags billing. Acordar en reunión si se activa cadena aprobación comercial (D4) en la demo o se deja como «implementado, pendiente activación».

### ¿Listo para producción?

**No-Go.** Producción (`45.7.229.46`) no tiene evidencia de smoke post-migrate. H14 documenta checklist de deploy pero **migrate no ejecutado** en prod (OV, stock por bodega, aprobación comercial, huérfanos ficha/inventario). E2E-008 y SMK prod permanecen BLOCKED. No asumir paridad local/prod hasta deploy explícito acordado en reunión.

### Veredicto global

| Dimensión | Estado | Confianza |
|---|---|---|
| Código piloto Fase 1 (local) | **Avanzado** — huecos H1–H8 cerrados en código | Media-alta en módulos probados |
| Evidencia QA integral | **Parcial** — ~40 % plan v2 con corrida trazable 15/08 | Media en Ola A; baja en back-office |
| Demo cliente (local) | **GO condicionado** | Media |
| Producción piloto | **No-Go** | Nula hasta H14 |

---

## 2. Matriz de riesgo — P0 / P1 abierto

| ID / tema | Sev. | Estado | Impacto si no se cierra | Dueño sugerido |
|---|---|---|---|---|
| **BIL-001 / BIL-002** — stub DTE sin `.env` billing | P0 | BLOCKED entorno | Demo no puede mostrar folio stub al contabilizar factura `ALM-FAC-101` | Devint |
| **VEN-009–012** — cadena aprobación OV con flag `true` | P0 | No ejecutado Ola A | Riesgo de mostrar D4 «implementado» sin evidencia runtime; decisión reunión sin validación | Devint + Cliente (D4) |
| **CMP-012–013** — match 3 vías OK/FAIL | P0 | No ejecutado Ola A | Flujo compras registro vs recepción sin evidencia reciente | Devint |
| **INV-010** — NC → `DEVOLUCION_NC` reingreso bodega (H7) | P0 | No ejecutado Ola A | Regresión inventario NC no verificada en corrida 15/08 | Devint |
| **ADM-022** — re-login AdminConcepto tras cambio JWT | P0 | No ejecutado Ola A | Riesgo operativo en configuración aprobaciones en demo | Devint |
| **E2E-001** — golden ALM-COT → OC → aprobación → recepción | P0 | Pendiente Ola C | Recorrido A demo sin evidencia end-to-end | Devint |
| **E2E-002 / E2E-003** — solo validación API en Ola A | P0 | Parcial | Aprobación OV + factura stub no recorridos en UI con PIN/capturas | Devint |
| **H14 / E2E-008** — prod sin migrate OV/stock | P0 | BLOCKED prod | Cliente no puede usar piloto remoto con paridad local | Devint + Cliente |
| **Ola B** — PAR, CNT, TES, CTR profundo (~10–17 % cobertura previa) | P1 | No iniciada | Back-office (centralización, tesorería, contratistas E2E) sin evidencia | Devint |
| **ADM-002 / VEN-013** — `ventaBajoCosto` UI (H2) | P1 | No ejecutado | D16 acordado en Reu6 sin retest UI en corrida 15/08 | Devint |
| **E2E-004 / E2E-005** — contratistas + contabilidad/tesorería showcase | P1 | Pendiente Ola C | Recorridos C y contratistas sin golden path | Devint |
| **E2E-006** — demo 15 min sin video/capturas archivadas | P1 | Parcial | Evidencia demo MJ insuficiente para auditoría | Devint |
| **DK-D4** — flag `comercialRequiereAprobacion` en piloto | P1 | Decisión reunión | Comportamiento demo depende de configuración empresa | Cliente |
| **H9, H12, H13** — SMTP, Acepta, Excel cartolas | P1 | Externo / SKIP | No bloquean piloto; documentar como fuera de alcance Fase 1 | Cliente |

**P0 abiertos en producto:** ninguno documentado con FAIL en Ola A. Los P0 vigentes son **cobertura QA** y **entorno** (billing, prod).

---

## 3. Confianza en evidencias — plan v1 → v2 → Ola A

| Etapa | Qué aporta | Confianza | Limitación principal |
|---|---|---|---|
| **Plan v1** (225 casos) | Marco exhaustivo Reu6, mapa de deuda, criterios PASS/FAIL | **Alta (diseño)** | No ejecutado; baseline histórico solo ~36 % |
| **Análisis integridad v1** | Reconciliación Fases 1–5 (12–14/08), top 30 gaps, checklist runner | **Alta (metodología)** | Veredicto `REQUIERE_RETRABAJO`; retest UI Emitir 14/08 obsoleto |
| **Plan v2** (215 casos, oleadas A/B/C) | HEREDADO (~41), eliminación duplicados, HUERFANOS H1–H8 como PASS esperado | **Alta (ejecución)** | Depende de corrida Ola A completa |
| **Ola A** (29 casos, 20 PASS) | Smoke 8/8, Emitir OV post-fix, lookup H1, RBAC tenant/pantallas/bandeja OV, Jest 150 | **Media-alta en lo ejecutado** | Subconjunto ~53 % de Ola A P0; 2 BLOCKED billing; E2E parcial API; 7 HEREDADO sin rerun |

### Bloques con confianza consolidada

| Bloque | Fuente evidencia | Nivel |
|---|---|---|
| Aprobaciones Compras/Contratistas (seed 20/20) | 12/08 veredicto + `qa-retest-seed.mjs` | **Alta** (HEREDADO; revalidar si cambian reglas) |
| OV API core (crear, stock, convertir factura) | Fase 5 post-fix + HEREDADO v2 | **Media-alta** |
| Emitir unificado + lookup + guías (H1, H4, H8) | Ola A 15/08 UI/API | **Alta** |
| Smoke + tenant + Jest | Ola A 15/08 | **Alta** |
| Billing stub | — | **Baja** (BLOCKED) |
| Contabilidad / tesorería / parametrización profunda | Fases 5 SKIP mayoritario | **Baja** |
| Prod | Sin corrida | **Nula** |

**Conclusión:** la cadena v1 → análisis → v2 **mejoró trazabilidad** y corrigió deudas documentales obsoletas (Emitir, productor, pantallas-permisos). La Ola A **desbloquea Ola B** a nivel runner (0 FAIL P0), pero **no cierra** la confianza del encargado de proyecto para demo integral ni para prod.

---

## 4. Decisiones pendientes de reunión

| # | Tema | Contexto | Opciones | Recomendación encargado |
|---|---|---|---|---|
| **D4** | Activar `comercialRequiereAprobacion` en demo/piloto | Código y seed local con flag `true`; AGENTS indica «activar tras reunión» | (a) Mantener `true` y demo con bandeja OV · (b) `false` y demo sin aprobación OV · (c) Mostrar ambos escenarios | **(a)** si se ejecutan VEN-009–012 antes de demo; si no hay tiempo QA, **(b)** con narrativa «listo para activar» |
| **H14** | Deploy prod migrate OV/stock/aprobación | Checklist listo; 4 migraciones críticas sin `deploy` en `45.7.229.46` | (a) Deploy ventana acordada + E2E-008 · (b) Mantener solo local hasta cierre Ola B/C | **(b)** hasta 0 FAIL P0 en Ola A completa + flags billing; luego **(a)** con smoke prod documentado |
| **D16** | Política `ventaBajoCosto` en EMP-1 | Seed `BLOQUEAR`; UI Admin existe (H2) | Confirmar valor producción piloto | Mantener **BLOQUEAR** (Reu6) |
| **DTE stub** | Mostrar folio stub en demo | BIL BLOCKED por `.env` | Activar stub local vs omitir paso contabilizar | Activar stub **solo local** para demo (Devint pre-reunión) |
| **Alcance demo** | Qué recorridos mostrar | Ola B/C sin ejecutar | Recorrido A+B acotado vs esperar golden completo | **Recorrido B + compras aprobación** (HEREDADO); evitar tesorería/contabilidad profunda |

---

## 5. Go / No-Go por oleada

| Oleada | Alcance | Veredicto | Condición de cierre |
|---|---|---|---|
| **Ola A** | Retest P0 (~55 EJECUTAR + HEREDADO) | **GO condicionado** | Runner: `LISTO_PARA_OLA_B`. Encargado: **aceptar avance** con deuda documentada (billing, VEN-009–012, CMP-012–013, INV-010, ADM-022, E2E UI completo) |
| **Ola B** | PAR, INV movimientos, CTR, CNT, TES, ADM resto, FIC | **No-Go** (no iniciada) | Iniciar tras cerrar BLOCKED billing y completar huecos P0 Ola A pendientes |
| **Ola C** | E2E golden ALM-* (001, 004, 005; 002/003/006 completos) | **No-Go** | E2E-002/003/006 solo parcial; E2E-001/004/005 sin ejecutar |
| **Prod** | E2E-008 + smoke post-H14 | **No-Go** | Decisión reunión deploy + smoke documentado |

### Criterio de salida piloto (recordatorio plan v2)

- ≥ 90 % PASS excl. SKIP/BLOCKED/HEREDADO  
- 0 FAIL P0 abiertos  
- Informe único reconciliado (este documento + Ola B/C)

**Estado actual estimado plan v2:** ~**35–40 %** con evidencia trazable 15/08 (20 PASS Ola A + ~41 HEREDADO baseline − solapamientos). Por debajo del umbral 90 %.

---

## 6. Acciones inmediatas (máx. 5)

1. **Devint — Activar billing stub local** (`BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=true`), reiniciar API y re-ejecutar **BIL-001/002** antes de cualquier demo con factura `ALM-FAC-101`.
2. **Devint — Completar Ola A pendiente** (VEN-009–012, CMP-012–013, INV-010, ADM-022) en una sola sesión con JSON + capturas según checklist §8 plan v2.
3. **Cliente — Decidir D4** en reunión: flag `comercialRequiereAprobacion` en demo y fecha objetivo de activación en piloto real.
4. **Devint + Cliente — Acordar ventana H14** solo después de Ola A cerrada y smoke local golden; no prometer paridad prod hasta E2E-008 PASS.
5. **Devint — Ejecutar Ola B mínima pre-demo** (CNT-006–008 preview centralización, TES-005–010 conciliación/estado cuenta, E2E-001 golden compras) si la demo incluye back-office; si no, documentar explícitamente fuera de guion.

---

## 7. Síntesis para steering

El pipeline del 15/08 **ordenó** el QA (v1 → análisis → v2 → Ola A) y **confirmó** fixes críticos de comercial/inventario en local. No constituye aún certificación de piloto completo ni habilitación de producción.

| Pregunta | Respuesta |
|---|---|
| ¿Podemos hacer demo local esta semana? | **Sí, con guion acotado y flags billing corregidos** |
| ¿Podemos invitar al cliente a prod? | **No** |
| ¿Hay defectos P0 en producto? | **No reportados**; riesgo en **cobertura y entorno** |
| ¿Siguiente hito QA? | Cerrar Ola A pendiente → Ola B → Ola C → decisión H14 |

---

## 8. Addendum post-retest Ola A (misma fecha)

**Fuente:** `2026-08-15-revision-ola-a-cierre.md` · retest `2026-08-15-integral-erp-ola-a-retest.md` (11 PASS, 0 FAIL).

| Dimensión | Actualización |
|---|---|
| Demo local | **GO local reforzado** — cadena OV (flag `true`), match 3 vías, NC reingreso, billing stub validados en runtime |
| Ola A | **Cerrada** — veredicto revisor **`LISTO_OLA_B`** |
| Ola B | **Go iniciar** (PAR, CNT, TES, CTR según guion demo) |
| Prod | **Sin cambio — No-Go** (H14 pendiente) |
| Confianza QA plan v2 | **~45–50 %** trazable (sigue bajo 90 % piloto completo) |

**P0 cerrados en retest:** BIL-001/002, VEN-009–012, CMP-012/013, INV-010, ADM-022, ADM-015.

**Acciones §6:** ítems 1–2 **completados**. Priorizar ítem 3 (narrativa D4 en demo) e ítem 5 (Ola B pre-demo si back-office en guion).

**Guion demo ampliado:** OV → stock → Emitir + stub billing · aprobación OV con PIN · match compras OK/FAIL · NC reingreso bodega. Evitar prod remoto y back-office profundo hasta Ola B/C.

---

## 9. Addendum post Ola B + TES-015 (misma fecha)

**Fuente:** `2026-08-15-revision-ola-b-cierre.md` · retest `2026-08-15-integral-erp-ola-b-tes015-retest.md`.

| Dimensión | Actualización |
|---|---|
| Ola B | **Cerrada** — **`LISTO_OLA_C`** |
| TES-015 | Fix `parseEstadoGenerico`; retest PASS |
| Demo local back-office | PAR, INV, CTR, CNT, TES (crear pago) validados |
| Ola C | **Autorizada** — E2E-001/004/005 |
| Prod | **Sin cambio — No-Go** (H14) |
| Confianza QA plan v2 | **~70 %** estimado |

**Guion demo:** puede incluir tesorería (pagos, conciliación, CXC) y preview centralización; evitar prod remoto.

---

## 10. Addendum post Ola C — cierre pipeline local (misma fecha)

**Fuente:** `2026-08-15-revision-ola-c.md` · corrida `2026-08-15-integral-erp-ola-c.md` / `.json` (6 PASS, 0 FAIL, 1 BLOCKED, 1 SKIP).

| Dimensión | Actualización |
|---|---|
| Pipeline local A+B+C | **Cerrado** — veredicto revisor **`PIPELINE_LOCAL_CERRADO`** |
| Ola C | **Cerrada** — E2E-001–006 PASS · E2E-007 SKIP · E2E-008 BLOCKED prod |
| Demo local | **Go demo integral** — golden ALM-* (compras, OV, proforma, back-office, recorrido 15 min) |
| Prod | **Sin cambio — No-Go** (H14 / E2E-008) |
| Confianza QA plan v2 | **~75–80 %** trazable (sigue bajo 90 % umbral piloto completo) |

**E2E cerrados:** 001 compras · 002 OV aprobación+stock · 003 factura stub · 004 proforma · 005 centralización/tesorería · 006 smoke rutas.

**Deuda no bloqueante:** capturas/video E2E-006; UI bandeja `mgonzalez` (opcional); E2E-001 registro `BORRADOR`; E2E-007 greenfield; H14 prod.

**Acciones §6:** ítem 5 **completado**. Priorizar ítem 3 (narrativa D4) e ítem 4 (ventana H14).

---

*Documento emitido por encargado de proyecto. Fuentes: `PLAN-PRUEBAS-INTEGRAL-ERP-COMPLETO-2026-08-15.md`, `2026-08-15-analisis-integridad-qa-v1.md`, `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`, `2026-08-15-integral-erp-ola-a.md` / `.json`, `2026-08-15-integral-erp-ola-a-retest.md`, `2026-08-15-revision-ola-a-cierre.md`, `2026-08-15-integral-erp-ola-b.md`, `2026-08-15-revision-ola-b-cierre.md`, `2026-08-15-integral-erp-ola-c.md`, `2026-08-15-revision-ola-c.md`, `AGENTS.md`, `HUERFANOS-H1-H14.md`.*
