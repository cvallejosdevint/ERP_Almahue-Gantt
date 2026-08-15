# Revisión QA — Cierre pipeline integral local (Ola C)

**Fecha:** 2026-08-15  
**Revisor:** almahue-qa-reviewer  
**Entradas:**

| Documento | Rol |
|---|---|
| `2026-08-15-revision-ola-a-cierre.md` | Gate Ola A → **`LISTO_OLA_B`** |
| `2026-08-15-revision-ola-b-cierre.md` | Gate Ola B → **`LISTO_OLA_C`** |
| `2026-08-15-integral-erp-ola-c.md` / `.json` | Corrida Ola C (runner) |
| `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` §4.2, §9 | Alcance y orden Ola C |
| `2026-08-15-veredicto-encargado-proyecto.md` | Decisión steering (addenda §8–9) |
| `AGENTS.md`, `HUERFANOS-H1-H14.md` | Huecos vigentes / no-FAIL Fase 1 |
| Skill `almahue-aprobaciones` | PIN por designación; re-login AdminConcepto |

Sin JWT. Sin re-ejecución de pruebas en esta sesión.

---

## 1. Integridad corrida Ola C

### 1.1 Precondiciones §3 + checklist §8

| Ítem | Estado | Nota revisor |
|---|---|---|
| API `:3001` + `db=ok` | **PASS** | Alineado Ola A/B |
| Front `:5174` | **PASS** | `/login` y rutas demo sin 500 |
| `seed:demo-propuesta` | **PASS** | Re-aplicado pre-corrida (ALM-*) |
| Billing stub | **PASS** | Heredado retest Ola A |
| Periodo `2026-08` ABIERTO | **PASS** | E2E-005 centralización |
| Stock `INS-ALM-CEREZA` | **PASS** | Δ=320 E2E-002 coherente |
| Tenant EMP-1 | **PASS** | Sesiones por usuario seed |
| JSON anonimizado | **PASS** | `2026-08-15-integral-erp-ola-c.json` |
| Sin JWT en markdown | **PASS** | |

### 1.2 Casos §4.2 — trazabilidad JSON ↔ informe

| ID | P | Resultado | Evidencia consolidada | Revisor |
|---|---|---|---|---|
| E2E-001 | P0 | PASS | `ALM-COT-001` → OC → Jorge PIN U-3 → recepción CONFIRMADA · registro `matchOk=true` | **Aceptado** — golden compras cerrado |
| E2E-002 | P0 | PASS | `ALM-OV-002` cadena 3 pasos admin PIN → `AUTORIZADA` → stock Δ=320 · UI `/comercial/aprobaciones` 200 | **Aceptado** — ver reserva §2 |
| E2E-003 | P0 | PASS | `ALM-OV-004` → `ALM-FAC-101` stub `ACCEPTED_STUB` · UI `/comercial/emitir` 200 | **Aceptado** |
| E2E-004 | P1 | PASS | Proforma Jorge → admin PIN → `DEFINITIVA` + factura | **Aceptado** |
| E2E-005 | P1 | PASS | Preview centralización 201 · cartolas/conciliaciones/pagos 201 · UI showcase | **Aceptado** — TES-015 cerrado Ola B |
| E2E-006 | P0 | PASS | 8/8 rutas demo HTTP 200 · folios seed presentes | **Aceptado** — ver reserva §2 |
| E2E-007 | P2 | SKIP | Greenfield sin seed | **Válido** — opcional plan |
| E2E-008 | P0 | BLOCKED | Prod `45.7.229.46` sin migrate H14 | **Esperado** — no bloquea local |

**Conteo Ola C:** 6 PASS · 0 FAIL · 1 BLOCKED · 1 SKIP · veredicto runner `PIPELINE_LOCAL_CERRADO`.

**Conclusión integridad:** informe y JSON **coherentes**. Script `ERP/.qa-tmp/run-ola-c-e2e.mjs` ejecutó el alcance §9 Ola C. Sin divergencia crítica artefacto/informe (a diferencia de reserva Ola B §1.3).

### 1.3 Cadena prerequisitos A → B → C

| Oleada | Veredicto cierre | ¿Vigente? |
|---|---|---|
| Ola A + retest | `LISTO_OLA_B` | Sí — 11/11 retest PASS |
| Ola B + retest TES-015 | `LISTO_OLA_C` | Sí — 100/100 PASS |
| Ola C | Runner `PIPELINE_LOCAL_CERRADO` | **Confirmado** por revisor |

---

## 2. Reservas evidencia (no bloquean gate local)

| Tema | Hallazgo | Clasificación | ¿Bloquea cierre? |
|---|---|---|---|
| **E2E-002** bandeja OV UI | Aprobación vía admin superadmin PIN; no sesión `mgonzalez` en UI | **Deuda conocida** (Ola A VEN-010) | **No** — API + RBAC-014 validan designación |
| **E2E-006** demo 15 min | Smoke HTTP 8/8; sin video ni carpeta `evidencias/` | **Deuda evidencia P1** | **No** — funcional PASS; capturas opcionales pre-reunión MJ |
| **E2E-001** registro compra | `BORRADOR` en golden; `CONTABILIZADA` exige cuenta en líneas asiento | **Deuda evidencia** | **No** — match 3 vías y recepción validados |
| **E2E-007** greenfield | SKIP P2 | **Deuda plan** | **No** |

Alineado skill aprobaciones: PIN no depende de `comercial:write` del aprobador; Jorge/bandeja y S5 3M cubiertos por seed HEREDADO + E2E-001/004.

---

## 3. E2E-008 / H14 — BLOCKED prod

| Aspecto | Veredicto |
|---|---|
| Causa | Migrate OV/stock/aprobación **no ejecutado** en `45.7.229.46` |
| Clasificación | **Deuda deploy** — documentada `HUERFANOS-H1-H14.md` H14 |
| Impacto local | **Ninguno** — pipeline local no incluye prod |
| Impacto demo cliente remota | **No-Go prod** hasta ventana H14 + smoke post-deploy |

**No es defecto de producto ni FAIL de entorno local.** BLOCKED aceptable según plan v2 §4.2 y `AGENTS.md`.

---

## 4. FAIL clasificados

**Sin FAIL en Ola C.** No aplica reclasificación defecto nuevo / entorno.

### Deuda no bloqueante Fase 1 (no reclasificar como defecto)

| ID / tema | Tipo | Nota |
|---|---|---|
| E2E-008 / H14 | Deuda deploy | Prod sin paridad local |
| E2E-007 | Deuda plan P2 | SKIP válido |
| D4 narrativa demo | Decisión reunión | Cadena OV **validada** runtime; activar/mostrar en demo |
| D16 `ventaBajoCosto` UI | Deuda conocida | ADM-002/VEN-013 no ejecutados Ola C |
| `pantallas-permisos` vs Sidebar | Deuda conocida | Catálogo desfasado; Sidebar correcto |
| Wizard Emitir mezcla tipos compra | Deuda conocida | Restricción VEN PASS |
| DTE stub / productor ausente maestro | Deuda conocida | H11 stub; H1 lookup PASS |
| workflows-admin legacy | Deuda conocida | No mezclar en UI nueva |

---

## 5. Veredicto consolidado pipeline local

### Gate Ola C (§4.2 plan v2)

| Criterio | Estado |
|---|---|
| 0 FAIL P0/P1 en casos **EJECUTAR** Ola C | **Cumplido** |
| E2E-001 golden compras ALM-COT | **Cumplido** |
| E2E-002/003 OV aprobación + factura stub | **Cumplido** (API + smoke UI) |
| E2E-004 proforma contratistas | **Cumplido** |
| E2E-005 centralización + tesorería | **Cumplido** |
| E2E-006 recorrido demo | **Cumplido** (smoke rutas) |
| E2E-008 prod | **BLOCKED esperado** |
| Prerequisito `LISTO_OLA_C` | **Cumplido** |

### Pipeline integral A + B + C

| Dimensión | Estado |
|---|---|
| Ola A P0 retest | **Cerrado** (`LISTO_OLA_B`) |
| Ola B §4.1 | **Cerrado** (`LISTO_OLA_C`, 100/100) |
| Ola C E2E golden | **Cerrado** (6/6 ejecutables PASS) |
| Defectos P0 producto abiertos | **Ninguno** |
| Prod piloto | **No-Go** (H14) |
| ≥ 90 % plan v2 total | **No cumplido** (~75–80 % estimado) — criterio **piloto completo**, no gate oleada |

### Veredicto

**`PIPELINE_LOCAL_CERRADO`**

Motivo: las tres oleadas cumplen sus gates formales (0 FAIL P0/P1 en alcance ejecutado). E2E-008 BLOCKED es deuda deploy esperada. La deuda restante es **evidencia demo** (capturas/video, sesión aprobador designado en UI) y **prod H14**, no regresiones de producto.

No aplica **`OLA_C_PARCIAL`** — todos los casos EJECUTAR de Ola C pasaron; las reservas §2 son deuda documentada, no FAIL.

No aplica **`REQUIERE_RETEST`** — sin ambigüedad que exija nueva corrida sobre el mismo alcance.

---

## 6. Go / No-Go por entorno

| Entorno | Veredicto | Condición |
|---|---|---|
| **Local piloto / demo** | **Go** | Guion A+B+C con seed `demo-propuesta`; billing stub activo |
| **Prod** `45.7.229.46` | **No-Go** | E2E-008 BLOCKED hasta migrate H14 + smoke documentado |
| **Reunión cliente D4** | **Decisión narrativa** | Implementación validada; elegir mostrar cadena OV o «listo para activar» |

### Guion demo integral sugerido (post-pipeline)

1. **Compras (E2E-001):** `ALM-COT-001` → OC → Jorge PIN → recepción.
2. **Ventas (E2E-002/003):** OV aprobación cadena → confirmar stock → Emitir factura stub.
3. **Contratistas (E2E-004):** Proforma → PIN → factura.
4. **Back-office (E2E-005):** Preview centralización + tesorería (pagos, conciliación).
5. **Recorrido 15 min (E2E-006):** Inventario → Compras → Ventas → Emitir.
6. **Evitar:** prod remoto, E2E-007 greenfield, contabilización profunda registro compra sin cuentas.

---

## 7. Defectos priorizados (post-cierre)

| Prioridad | ID / tema | Tipo | Acción |
|---|---|---|---|
| — | — | — | **Sin defectos P0/P1 nuevos** |
| P0 prod | H14 / E2E-008 | Deuda deploy | Acordar ventana migrate + smoke prod |
| P2 evidencia | E2E-006 video/capturas | Deuda evidencia | Archivar pre-auditoría MJ si se exige |
| P2 evidencia | E2E-002 UI `mgonzalez` | Deuda conocida | Captura opcional bandeja designado |
| P2 evidencia | E2E-001 registro CONTABILIZADA | Deuda evidencia | Opcional si demo incluye asiento compra |
| P1 producto | ADM-002 / VEN-013 `ventaBajoCosto` | Deuda conocida D16 | Retest UI si demo incluye política bajo costo |
| P2 plan | E2E-007 greenfield | Deuda plan | Solo si se requiere escenario sin seed |

---

## 8. Retest sugerido (solo si cambia alcance)

No se requiere retest mínimo adicional sobre Ola C 15/08.

| ID | Cuándo re-ejecutar |
|---|---|
| **E2E-008** | Tras deploy prod + migrate H14 |
| **E2E-001–006** | Tras cambio cadena OC/OV, billing stub o seed ALM-* |
| **E2E-002** | Si regresión bandeja Comercial o permisos aprobadores |
| **Subset pipeline** | Tras fix P0 en módulos VEN/CMP/CTR/CNT/TES/BIL |

---

## 9. Referencias cruzadas

| Documento | Relación |
|---|---|
| `2026-08-15-integral-erp-ola-c.json` | Evidencia anonimizada Ola C |
| `2026-08-15-revision-ola-a-cierre.md` | Prerequisito A |
| `2026-08-15-revision-ola-b-cierre.md` | Prerequisito B |
| `2026-08-15-veredicto-encargado-proyecto.md` | Actualizar §10 addendum |
| `HUERFANOS-H1-H14.md` | H14 prod pendiente |
| `AGENTS.md` | Puntero huecos vigentes — actualizar post-cierre |

---

## 10. § Cierre — addendum encargado de proyecto

Recomendación de actualización para `2026-08-15-veredicto-encargado-proyecto.md`:

| Dimensión | Antes (§9) | Después (recomendado) |
|---|---|---|
| Pipeline local A+B+C | Ola C autorizada, no ejecutada | **Cerrado** — veredicto revisor **`PIPELINE_LOCAL_CERRADO`** |
| Ola C | No-Go | **Cerrada** — 6 PASS · E2E-008 BLOCKED prod |
| Demo local | Back-office validado Ola B | **Go demo integral** — golden ALM-* E2E-001–006 |
| Prod | No-Go | **Sin cambio — No-Go** (H14 / E2E-008) |
| Confianza QA plan v2 | ~70 % | **~75–80 %** trazable (sigue bajo 90 % umbral piloto completo) |
| Acciones §6 | Ítem 5 Ola B pendiente | **Completado** · priorizar ítem 3 (D4) e ítem 4 (ventana H14) |
| E2E-001/004/005 | Pendiente Ola C | **PASS** 15/08 |
| E2E-002/003/006 | Parcial API | **PASS** Ola C (smoke UI; capturas opcionales) |

**Pregunta steering actualizada:**

| Pregunta | Respuesta |
|---|---|
| ¿Pipeline QA local cerrado? | **Sí** — `PIPELINE_LOCAL_CERRADO` |
| ¿Demo local integral esta semana? | **Sí** — guion §6 |
| ¿Prod con paridad local? | **No** — H14 pendiente |
| ¿Defectos P0 producto? | **No reportados** |
| ¿Siguiente hito? | Decisión D4 + ventana H14 + capturas opcionales |

---

*Revisión documental de cierre pipeline integral. Ejecutor Ola C: almahue-qa-runner · Revisor: almahue-qa-reviewer.*
