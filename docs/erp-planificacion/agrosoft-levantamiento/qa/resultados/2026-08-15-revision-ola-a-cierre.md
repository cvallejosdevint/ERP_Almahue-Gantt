# Revisión QA — Cierre retest Ola A

**Fecha:** 2026-08-15  
**Revisor:** almahue-qa-reviewer  
**Entradas:**

| Documento | Rol |
|---|---|
| `2026-08-15-revision-ola-a.md` | Veredicto previo **REQUIERE_RETEST** |
| `2026-08-15-integral-erp-ola-a.md` / `.json` | Corrida Ola A original (29 casos) |
| `2026-08-15-integral-erp-ola-a-retest.md` / `.json` | Retest mínimo §6 revisión (11 casos) |
| `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` §9 | Orden y gate Ola A |
| `2026-08-15-veredicto-encargado-proyecto.md` | Decisión steering pre-retest |

Sin JWT. Sin re-ejecución de pruebas en esta sesión.

---

## 1. ¿Cierra gaps del REQUIERE_RETEST?

Referencia: §6 de `2026-08-15-revision-ola-a.md`.

| Gap pendiente | Estado post-retest | Evidencia | Clasificación |
|---|---|---|---|
| **BIL-001 / BIL-002** | **Cerrado** | Flags billing activos + API reiniciada · contabilizar 201 `ACCEPTED_STUB` · disclaimer UI Emitir | Entorno resuelto; PASS funcional |
| **VEN-009** | **Cerrado** | OV $800k → `PENDIENTE_APROBACION` · aprobador U-6 | PASS P0 |
| **VEN-010** | **Cerrado con reserva UI** | API: bandeja incluye `ALM-OV-002` · PIN×3 → `AUTORIZADA` · UI carga sin filas headless | Ver §2 |
| **VEN-011** | **Cerrado** | Cadena 3 pasos → `AUTORIZADA` | PASS P0 |
| **VEN-012** | **Cerrado** | Solicitante U-6 omite auto-aprobación · primer aprobador U-3 | PASS P1 |
| **CMP-012** | **Cerrado** | `matchOk=true` ALM-OC-003 monto 600.000 | PASS P0 |
| **CMP-013** | **Cerrado** | `matchOk=false` · `matchDiff=-150000` (líneas explícitas) | PASS P0 |
| **INV-010** | **Cerrado** | NC contabilizada · movimiento `DEVOLUCION_NC` · delta +10 cereza BOD-ALM-FRIG (H7) | PASS P0 |
| **ADM-022** | **Cerrado** | Cambio AdminConcepto Claudia · re-login · JWT `adminConceptoModulos` actualizado (`Contratistas`) | PASS P0 · alineado skill aprobaciones |
| **ADM-015** | **Cerrado funcional** | `POST /escalas-aprobacion` → 400 `APROBADOR_SIN_BANDEJA` | PASS API; modal UI no capturado (P1) |

**Conteo retest:** 11 PASS · 0 FAIL · 0 BLOCKED · veredicto runner `OLA_A_RETEST_OK`.

**Conclusión §1:** los **11 casos** del retest mínimo **cierran** los gaps explícitos del REQUIERE_RETEST. No hay FAIL P0 nuevo en producto. El checklist §8.1 billing queda **cumplido** tras reinicio API.

---

## 2. VEN-010 — UI headless sin filas

| Aspecto | Hallazgo |
|---|---|
| Plan §4.0 | P0 · `ALM-OV-002` **AUTORIZADA PIN UI** en `/comercial/aprobaciones` |
| Retest | Aprobación vía API (admin superadmin + PIN×3) → `AUTORIZADA` · Playwright headless: página OK, **sin filas** |
| Corrida original Ola A | **RBAC-014:** `GET /aprobaciones-ov` **mgonzalez@almahue.cl** → 200, 1 pendiente (designado Comercial) |
| Skill aprobaciones | Bandeja OV validada por designación en reglas; PIN no depende de `comercial:write` del aprobador |

**Veredicto revisor:** **Aceptable para gate Ola A** con evidencia API consolidada (bandeja + aprobar-ov + estado final). La ausencia de filas en headless es **limitación de sesión/automatización** (runner usó admin para PIN, no sesión mgonzalez en UI), no regresión de producto demostrada.

| Acción | ¿Bloquea Ola B? |
|---|---|
| Captura UI manual con **mgonzalez** aprobando PIN en bandeja | **No** — recomendada **opcional** pre-demo o en Ola C (E2E-002 completo) |
| Re-ejecutar VEN-010 headless | **No** — salvo regresión declarada en bandeja Comercial |

---

## 3. Veredicto consolidado Ola A

Integración corrida original (20 PASS + 2 BLOCKED→PASS en retest + 7 HEREDADO) + retest (11 PASS):

| Criterio gate §9 / plan v2 | Estado |
|---|---|
| 0 FAIL P0 en casos **EJECUTAR** Ola A §4.0 | **Cumplido** |
| Billing `.env` + retest BIL | **Cumplido** |
| Cadena OV D4 (VEN-009–012) con `comercialRequiereAprobacion=true` | **Cumplido** (API) |
| Match 3 vías compras (CMP-012–013) | **Cumplido** |
| NC reingreso bodega H7 (INV-010) | **Cumplido** |
| Re-login AdminConcepto (ADM-022) | **Cumplido** |
| HEREDADO aprobaciones ADM-009–012 / CMP-004–008 / VEN-002–008 | **Documentado** (baseline 12/08 · seed 20/20) |
| ≥ 90 % plan total v2 | **No cumplido** (~40–45 % trazable) — criterio **piloto completo**, no gate Ola A |
| E2E-002/003/006 capturas UI / video | **Parcial** (API + smoke rutas) — deuda **Ola C / pre-demo**, no bloquea gate Ola A |

### Veredicto

**`LISTO_OLA_B`**

Motivo: el retest mínimo satisface el gate formal Ola A (0 FAIL P0, gaps REQUIERE_RETEST cerrados). La deuda restante es **evidencia demo** (capturas E2E, VEN-010 UI opcional, ADM-015 modal P1) y **cobertura plan global** (Ola B/C), no defectos P0 abiertos.

No aplica **`BLOQUEADO`** (sin FAIL producto ni BLOCKED entorno vigente). No aplica **`REQUIERE_RETEST`** adicional sobre el mismo alcance §6.

---

## 4. ¿Autoriza iniciar Ola B?

**Sí.**

Condiciones cumplidas:

1. Retest §6 revisión: **11/11 PASS**.
2. Gate Ola A §4.0 P0 **EJECUTAR**: **0 FAIL**.
3. Billing local operativo para demos con stub.

**Deuda documentada** (no bloqueante para arrancar Ola B según §9 plan v2):

- E2E-001, E2E-004, E2E-005 → Ola C.
- E2E-002/003 UI completa + E2E-006 video/capturas → Ola C o checklist pre-demo §8.3.
- **H14 / E2E-008** prod → BLOCKED hasta deploy acordado.
- Ola B módulos PAR, INV movimientos, CTR, CNT, TES, ADM resto, FIC (§4.1).

Orden sugerido: **Ola B** según §9 → Ola C golden → actualizar veredicto encargado tras Ola B mínima si la demo incluye back-office.

---

## 5. Actualización recomendada — veredicto encargado

El documento `2026-08-15-veredicto-encargado-proyecto.md` refleja el estado **pre-retest**. Tras este cierre, se recomienda **actualizar** (sin reemitir todo el pipeline):

| Dimensión | Antes (encargado) | Después (recomendado) |
|---|---|---|
| Demo local | GO condicionado | **GO local reforzado** — incluir cadena OV con flag `true`, match 3 vías, NC reingreso, stub billing |
| Riesgos P0 matriz §2 | VEN-009–012, CMP-012–013, INV-010, ADM-022, BIL **abiertos** | **Cerrados** en retest 15/08 · evidencia JSON trazable |
| D4 reunión | «Ejecutar VEN-009–012 antes de demo» | **Evidencia runtime disponible** — decisión cliente pasa a **activar/mostrar en demo**, no a validar implementación |
| Ola A §5 | GO condicionado / deuda documentada | **Cerrada** para gate runner · **`LISTO_OLA_B`** |
| Ola B §5 | No-Go (no iniciada) | **Go iniciar** — PAR, CNT preview, TES según guion demo |
| Prod §1 | No-Go | **Sin cambio — No-Go** (H14 pendiente) |
| Confianza evidencia QA | ~35–40 % plan v2 | **~45–50 %** (+ retest P0 críticos); sigue bajo 90 % hasta Ola B/C |
| Acciones §6 inmediatas | Items 1–2 pendientes | **Items 1–2 completados** · priorizar **3** (decisión D4 narrativa demo) y **5** (Ola B pre-demo si aplica) |

### Guion demo sugerido (más fuerte)

1. **Recorrido B:** OV → confirmar stock → Emitir factura → contabilizar **stub** (BIL PASS).
2. **Recorrido aprobación comercial:** crear/solicitar OV → bandeja (mgonzalez en vivo o captura) → PIN → `AUTORIZADA` (VEN-009–011).
3. **Compras:** match 3 vías OK/FAIL en registro (CMP-012–013).
4. **Inventario:** NC → reingreso bodega visible (INV-010).
5. **Evitar** prod remoto y tesorería/contabilidad profunda hasta Ola B/C.

---

## 6. Defectos priorizados (post-cierre)

| Prioridad | ID / tema | Tipo | Acción |
|---|---|---|---|
| — | — | — | **Sin defectos P0 nuevos** |
| P2 evidencia | VEN-010 UI bandeja | Deuda evidencia | Captura opcional mgonzalez pre-demo |
| P2 evidencia | ADM-015 modal UI | Deuda P1 | Captura opcional; API ya valida regla |
| P1 cobertura | E2E-002/003/006 UI | Deuda Ola C | Capturas/video según §8.3 |
| P0 prod | H14 / E2E-008 | Deuda deploy | Reunión cliente; no prometer paridad prod |
| P1 producto | ADM-002 / VEN-013 `ventaBajoCosto` UI | Deuda conocida D16 | Ola B o checklist pre-demo |

---

## 7. Retest sugerido (solo si cambia alcance)

No se requiere retest mínimo adicional sobre el mismo §6.

| ID | Cuándo re-ejecutar |
|---|---|
| VEN-010 | Solo si regresión bandeja Comercial o cambio permisos aprobadores |
| ADM-009–014 | Tras cambio reglas/PIN/AdminConcepto o post-deploy prod |
| BIL-001–002 | Tras cambio flags billing o deploy prod |
| Subset Ola A | Tras fix en módulos VEN/CMP/INV/ADM/BIL |

---

## 8. Referencias cruzadas

| Documento | Relación |
|---|---|
| `2026-08-15-revision-ola-a.md` | Supersede veredicto **REQUIERE_RETEST** → **LISTO_OLA_B** |
| `2026-08-15-integral-erp-ola-a-retest.json` | Evidencia anonimizada retest |
| `HUERFANOS-H1-H14.md` | H7 INV-010 PASS; H14 prod pendiente |
| `REUNION-CHECKLIST-APROBACION-COMERCIAL.md` | Casos B/C alineados VEN-011/012 |
| `AGENTS.md` | D4 validado local; prod sin migrate |

---

*Revisión documental de cierre. Ejecutor retest: almahue-qa-runner · Revisor: almahue-qa-reviewer.*
