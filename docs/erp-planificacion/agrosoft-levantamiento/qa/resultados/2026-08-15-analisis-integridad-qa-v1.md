# Análisis de integridad QA — Plan integral v1 (225 casos)

**Fecha:** 2026-08-15  
**Rol:** almahue-qa-reviewer (fase 2 pipeline — no re-ejecución)  
**Plan analizado:** `qa/PLAN-PRUEBAS-INTEGRAL-ERP-COMPLETO-2026-08-15.md` v1.0  
**Fuentes:** resultados `2026-08-12-veredicto-unificado.md`, `2026-08-14-fase1` … `fase5`, `retest-ui-demo`, `auditoria-reu5-reu6`, `AGENTS.md`, `HUERFANOS-H1-H14.md`, skill `almahue-qa-local`, código local (corte 15/08).

No incluir JWT ni passwords en informes derivados.

---

## 1. Resumen ejecutivo

### ¿Son confiables las pruebas previas?

**Parcialmente.** Existe un **núcleo confiable** (aprobaciones fase 2 + smoke/OV API post-fix) y un **marco documental sólido** (Fases 1–4), pero **no** hay una ejecución única, trazable y completa del plan v1 ni del plan Fase 4 (96 IDs API) que cubra los 225 casos.

| Bloque | Confianza | Motivo |
|---|---|---|
| Aprobaciones con seed (20 casos) | **Alta** | `2026-08-12-veredicto-unificado.md`: 20/20 reproducible; reconfirmado Fase 5 (14/08) tras seed correcto |
| E2E sin seed (34 casos) | **Alta** | Playwright exit 0 (12/08); fuera del plan v1 pero válido para bootstrap |
| AdminConcepto (6 casos UI) | **Alta** | Spec dedicado PASS |
| Smoke + OV P0 API (Fase 5) | **Media-alta** | PASS tras fixes mismo día; **sin informe de re-ejecución íntegra** post-fix |
| Retest UI Recorridos A/B/C | **Media** | Recorrido B (OV) PASS; A parcial; **baseline Emitir (UI-E2) obsoleto** vs código actual |
| Contabilidad / tesorería / contratistas profundo | **Baja** | Mayoría SKIP en Fase 5; solo muestras CT1, TB6, CTR1 |
| Plan v1 (225 casos) | **No ejecutado** | Plan creado 15/08; evidencia previa mapea ~legado Fase 4 + aprobaciones |

### Go / no-go como baseline para plan v2

| Uso | Veredicto |
|---|---|
| Reutilizar resultados **aprobaciones** (ADM-009–015, CMP-004–008, CTR bandeja parcial) | **GO** con artefactos `qa-retest-seed-results.json` |
| Reutilizar **OV API core** (VEN-002–010, 016–018) post-fix RB1/lookup/stock | **GO condicionado** — exigir retest mínimo RBAC-001, VEN-029–031 |
| Reutilizar **retest UI Emitir** (UI-E2 tipos COTIZ/NP/OC) | **NO-GO** — contradice código y plan v1 §1.4 |
| Usar Fase 1–3 como baseline de gaps sin revalidar | **NO-GO** — varios ítems cerrados en código/HUERFANOS pero reportes del 14/08 no actualizados |
| Arrancar plan v2 sin nueva corrida | **NO-GO** — cobertura evidenciada ~35 % del plan v1 |

**Conclusión baseline:** las pruebas previas son **baseline parcial confiable** para aprobaciones y flujo OV API; **no** sustituyen una ejecución del plan v1.

---

## 2. Cobertura plan v1 vs ejecutado

Estimación por **casos con evidencia explícita** (PASS/FAIL/DEBT/SKIP documentado en informes 12–14/08), mapeados al plan v1 vía anexo §10.3.

| Módulo | Casos plan v1 | Con evidencia | % | Hueco principal |
|---|---:|---:|---:|---|
| SMK | 8 | 7 | 88 % | SMK-007 UI dashboard sin JSON API |
| ADM | 22 | 11 | 50 % | ADM-001–008, 016–021, 022 re-login UI |
| PAR | 18 | 3 | 17 % | CRUD catálogos, import plan cuentas, PAR-016 RBAC menú |
| CMP | 24 | 14 | 58 % | Recepción parcial UI, CMP-012–013 match fail, CMP-019 masiva |
| VEN | 32 | 16 | 50 % | VEN-009–012 aprobación OV ALM-*; **VEN-021–028 Emitir sin retest post-fix** |
| INV | 18 | 6 | 33 % | INV-010 NC reingreso, movimientos UI, INV-018 demo |
| CTR | 22 | 4 | 18 % | CTR-005–009 flujo proforma+PIN; CTR-013 traspaso |
| CNT | 20 | 2 | 10 % | Centralización, reportes, CNT-016 cerrar periodo |
| TES | 18 | 3 | 17 % | Pagos, aging, TES-009 movimientos CC, TES-018 Recorrido C completo |
| FIC | 12 | 3 | 25 % | Pestañas UI, FIC-006 print, FIC-010 productor |
| BIL | 8 | 2 | 25 % | BIL-001 stub contabilizar, BIL-002 UI emitir+contabilizar |
| RBAC | 15 | 7 | 47 % | RBAC-001 post-fix sin informe dedicado; RBAC-007 pantallas; RBAC-014 comercial |
| E2E | 8 | 3 | 38 % | E2E-001–003 ALM-* no corridos end-to-end; E2E-008 prod SKIP |
| **Total** | **225** | **~81** | **~36 %** | **~144 casos sin evidencia ejecutada** |

**Notas:**

- Los 34 casos E2E sin seed **no** están en el conteo v1 (plan distinto); aportan confianza en bootstrap, no en módulos PAR/CNT/TES.
- VEN-021–022 el plan v1 marca DK-EMITIR **cerrado** (commit `2035773`); **no hay evidencia UI posterior** al cambio en `EmitirDocumentoPage.tsx` (solo FACTURA/NC/ND/GUIA).

---

## 3. Integridad metodológica (Fases 1–5 del 14/08)

| Fase | Objetivo | ¿Evidencia suficiente? | Hallazgos metodológicos |
|---|---|---|---|
| **1** As-is / to-be | Contraste Reu6 vs código | **Sí (doc)** — no runtime | Auto-contradicción §3 vs §4 (Emitir mezcla vs restringido). HUERFANOS (14/08 tarde) corrige H1–H8; Fase 1 no unificada en un solo corte |
| **2** Tools IA | Skills/rules vs gaps | **Sí (doc)** | Propuestas no aplicadas el 14/08; AGENTS.md **sí** actualizado después con huecos — alinear runner con AGENTS actual |
| **3** Demo cliente | Qué mostrar / seed | **Sí (doc)** | G1 «sin seed OV» **quedó obsoleto**: existe `seed-flujo-oc-ov-almahue.ts` + `npm run seed:demo-propuesta` con ALM-OV-001…004 |
| **4** Plan testing | Plan Fase 4 (96 API) | **Sí (doc)** | Correcto declarar «no se corrieron tests»; inventario Jest y mapa DK-* útil para v2 |
| **5** Ejecución | Correr plan Fase 4 | **Parcial** | Ver tabla siguiente |

### Fase 5 — checklist metodológico

| Criterio | Cumple | Detalle |
|---|---|---|
| Capturas UI | Parcial | Solo `retest-ui-demo.md`; sin carpeta `evidencias/` sistemática |
| API JSON anonimizado | Parcial | Menciona artefactos `.json`; no pegados en markdown (correcto) |
| Tenant `EMP-1` + header | Sí | Documentado en smoke y RB |
| Usuarios correctos (Luis/Jorge) | Parcial | CP2 documenta admin vs Luis; UI-A3 SKIP Jorge |
| Re-login AdminConcepto | Parcial | AC1 API PASS; RB10 SKIP; ADM-022 no retest UI |
| Seed antes de oleada 2 | **No inicialmente** | Primera corrida 3/20 — sesión inválida; re-seed corrige |
| Informe post-fix separado | **No** | Fixes en `fase5-lista-fixes.md` § post-fix **sin** nueva corrida completa Fase 5 |
| Clasificación FAIL vs deuda | Sí | Alineado con skill qa-local; OV11/14/16 bien como DEBT |

**Veredicto metodológico:** Fase 5 es **auditables** en aprobaciones y OV API, pero **no cierra** el plan Fase 4 (36 SKIP, oleadas 5–6 casi vacías). Mezclar «post-fix RESUELTO» con conteos pre-fix en un mismo informe **debilita** la trazabilidad.

---

## 4. Clasificación de hallazgos

### 4.1 Defectos nuevos (Fase 5 — estado al cierre 14/08)

| ID legado | ID plan v1 | Estado 15/08 | Clasificación |
|---|---|---|---|
| RB1 | RBAC-001 | Fix documentado | **Resuelto** — retest API 403; **falta evidencia en informe dedicado post-fix** |
| OV12, OV13 | VEN-029, VEN-030, FIC-009 | Fix documentado | **Resuelto API** — UI Emitir lookup aún PARCIAL en retest-ui |
| JT-RUN | SMK-008 | Fix documentado | **Resuelto** — 136 tests PASS |
| SM6 sin prep | SMK-006, INV-003 | Fix seed | **Resuelto** — stock bodega 1200 |
| OV15 | CMP-002 | Fix seed cotiz | **Resuelto** — proveedor en showcase |

**Defectos abiertos tras fixes:** ninguno P0 documentado en Fase 5 post-fix; **riesgo de regresión** por falta de re-corrida completa.

### 4.2 Deuda conocida (no FAIL en QA integral)

| Ref | Tema | Casos plan v1 | Nota 15/08 |
|---|---|---|---|
| DK-D4 | Aprobación comercial OV off / flag reunión | VEN-009–012 (SKIP si flag false) | Código listo (H3); `comercialRequiereAprobacion` en seed demo |
| DK-D16 | `ventaBajoCosto` | VEN-013–014 | **H2 listo** — UI Admin › Empresas existe; plan v1 ADM-002 lo cubre — **retest UI pendiente** |
| DK-D7 / H1 | Productor lookup | VEN-031, FIC-010 | **H1 listo** en HUERFANOS — Fase 5 clasificó OV14 DEBT **obsoleto** como gap producto |
| DK-EMITIR | Wizard Emitir | VEN-021–022 | **Código restringido** (`TIPOS_EMISION`); plan v1 cierra deuda; **retest UI obligatorio** |
| DK-D11 / H4 | pantallas-permisos | RBAC-007 | **H4 listo** — retest RBAC-007 pendiente |
| DK-DTE / H11 | Billing stub | BIL-* | Stub OK; no SII real |
| DK-LEGACY | workflows-admin | RBAC-008 | Deuda documentada |
| DK-D20 / H14 | Prod sin migrate | E2E-008, SMK prod | Entorno prod |
| DK-H13 | Excel cartolas | TES-004 | SKIP válido |
| DK-R4-18 | Cobranza | TES-017 | SKIP válido |
| DK-H10 | 3 cotiz comparativas | CMP-024 | SKIP válido |
| DK-G4 | Ingreso diario demo | CTR-018 | SKIP válido |
| DK-G5 | Traspaso vs gastos temporada | CTR-014 | SKIP válido (narrativa) |

### 4.3 Entorno / datos

| Caso | Tema | SKIP válido |
|---|---|---|
| OV15 (pre-fix) | Cotización sin proveedor | Sí — seed incompleto; corregido |
| SM6 (pre-fix) | Stock bodega 0 | Sí — G1; corregido en seed |
| Oleada 2 sin seed | 3/20 PASS | **No** — error metodológico de sesión |
| ADM-020 | SSO Microsoft | SKIP si sin `.env` |
| E2E-008 prod | H14 deploy | BLOCKED/SKIP |

### 4.4 SKIP válidos vs sospechosos (Fase 5)

| Tipo | Ejemplos | Validez |
|---|---|---|
| Alcance declarado | CT2–11, TB1–5, CTR2–7 | **Válido** si se planifica oleada 2 en v2 |
| Usuario alterno | UI-A3 Jorge | **Válido** solo porque API 20/20; **v2 debe incluir 1 captura UI bandeja** |
| «No ejecutado sesión» | 36 SKIP Fase 5 | **Válido como incompleto**, no como PASS implícito |

---

## 5. Casos del plan v1 sin cobertura — top 30 priorizados

### P0 — Bloquean confianza en plan v2 o demo ALM-*

| # | ID v1 | Motivo |
|---|---|---|
| 1 | **E2E-002** | ALM-OV-002 aprobación OV + stock — sin corrida golden |
| 2 | **E2E-003** | ALM-OV-004 → factura → stub ALM-FAC-101 |
| 3 | **E2E-001** | ALM-COT-001 → OC → aprobación → recepción cadena completa |
| 4 | **E2E-006** | Demo 15 min MJ (`DEMO-PROPUESTA-LOCAL.md`) |
| 5 | **VEN-009–012** | Cadena aprobación OV con flag true (checklist comercial) |
| 6 | **VEN-021–024** | Emitir unificado + contexto OV — **sin evidencia post-restricción tipos** |
| 7 | **RBAC-001** | Tenant documentos — fix sin informe de regresión formal |
| 8 | **ADM-022** | Re-login AdminConcepto UI tras cambio JWT |
| 9 | **CMP-012–013** | Match 3 vías OK/FAIL — CP8 PASS; CP9 SKIP |
| 10 | **BIL-001–002** | Contabilizar factura stub + disclaimer UI |
| 11 | **INV-010** | NC → DEVOLUCION_NC reingreso bodega (H7) |
| 12 | **SMK-008** | Jest suite — PASS post-fix pero no amarrado a corrida v1 |
| 13 | **RBAC-014** | Bandeja `/comercial/aprobaciones` usuario designado |
| 14 | **VEN-026** | Guías despacho UI (H8) |

### P1 — Flujos principales back-office y regresión

| # | ID v1 | Motivo |
|---|---|---|
| 15 | **CNT-006–008** | Centralización preview + UI |
| 16 | **CNT-016** | Cerrar periodo |
| 17 | **TES-008–010** | Pago → estado cuenta cliente |
| 18 | **TES-009** | Movimientos CC (TB7 nunca ejecutado en Fase 5) |
| 19 | **CTR-005–009** | Proforma → PIN → factura → reverso |
| 20 | **FIC-002–006** | Ficha pestañas + print HTML (H5) |
| 21 | **PAR-006–010** | Plan cuentas D9/D10 UI+API |
| 22 | **ADM-002** | Flags empresa (`ventaBajoCosto`, `comercialRequiereAprobacion`) |
| 23 | **RBAC-007** | Catálogo pantallas vs Sidebar (H4 cerrado en código) |
| 24 | **VEN-029–031** | Lookup RUT cliente/proveedor/productor post-fix |
| 25 | **INV-005–008** | Movimientos bodega UI |
| 26 | **CMP-018** | OC rechazada → re-envío bandeja |
| 27 | **ADM-016–018** | Plantillas + export/import reglas |
| 28 | **E2E-005** | Contabilidad + tesorería showcase |
| 29 | **E2E-004** | Contratistas E2E |
| 30 | **TES-018** | Recorrido C completo (cartola → conciliación → EC) |

---

## 6. Inconsistencias (reportes vs AGENTS.md vs código)

| # | Tema | Fuente A | Fuente B | Resolución 15/08 |
|---|---|---|---|---|
| 1 | **Emitir mezcla COTIZ/NP/OC** | Fase 1 §3, auditoría §3, retest UI-E2 | Plan v1 §1.4, HUERFANOS «Emitir listo», `EmitirDocumentoPage.tsx` L1436–1439 | **Código + plan v1 alineados** (solo FACTURA/NC/ND/GUIA). Retest UI **obsoleto**. Fase 1 §3 **desactualizado** |
| 2 | **Commit `2035773`** | Plan v1 §1.4, §6.1 | `git log` erp_back | Hash **no existe** en repo; cambio presente en working tree (commit reciente `dcc6f33` menciona flujo Reu6) |
| 3 | **Productor lookup** | Fase 5 OV14 DEBT DK-D7 | HUERFANOS H1 **Listo**, plan VEN-031 | Tratar como **listo en código**; reclasificar OV14; ejecutar VEN-031/FIC-010 |
| 4 | **pantallas-permisos** | Fase 1 §4 item 1 tachado pero Fase 3 tabla aún «desfasado» | HUERFANOS H4 **Listo** | Ejecutar RBAC-007; actualizar guion demo |
| 5 | **ventaBajoCosto sin UI** | Fase 1 D16 parcial, AGENTS hueco | HUERFANOS H2 **Listo**, ADM-002 plan v1 | UI existe en Admin › Empresas; **retest ADM-002** |
| 6 | **Sin seed OV (G1)** | Fase 3 P0-2, Fase 4 DK-G1 | `seed-flujo-oc-ov-almahue.ts`, `seed:demo-propuesta` | G1 **mitigado** si se corre seed demo; E2E ALM-* aún **no ejecutados** |
| 7 | **DK-EMITIR cerrado vs DEBT UI** | Plan v1 §6.1 | retest-ui UI-E2 DEBT | Cerrar deuda **solo tras** VEN-021–022 PASS en corrida v2 |
| 8 | **D4 comercial sin cadena** | AGENTS «activar tras reunión» | Plan v1 ADM-019 «Ya no reservado»; seed `comercialRequiereAprobacion=true` | **No contradicción funcional**: cadena **implementada**, activación **decisión reunión**. Documentar flag en precondiciones v2 |
| 9 | **Post-fix Fase 5 vs conteos Fase 5** | `fase5-ejecucion.md` 4 FAIL | `fase5-lista-fixes.md` RESUELTO | Informes **no reconciliados** en un único veredicto post-fix |
| 10 | **README resultados** | Apunta solo veredicto 12/08 | Pipeline 14/08 completo | Actualizar puntero a este análisis + estado integral |

---

## 7. Recomendaciones para plan v2

### 7.1 Correcciones al plan (sin modificar v1 en disco)

1. **Sincronizar deuda DK-EMITIR:** marcar cerrado solo tras casos VEN-021–022 ejecutados; hasta entonces «cerrado en código, pendiente QA UI».
2. **Eliminar referencia commit `2035773`** o sustituir por hash real (`dcc6f33` o tag) en v2.
3. **Precondición seed obligatoria:** `npm run seed && npm run seed:aprobaciones-f2 && npm run seed:demo-propuesta` antes de oleada 2 y E2E ALM-*.
4. **Duplicados / solapamiento:** SMK-002/E1, ADM-012–014 vs S1–S6, RBAC-002/E3 — en v2 un solo ID canonical + referencia cruzada.
5. **SKIP mal ubicados:** VEN-009–012 no deben SKIP por DK-D4 si precondición §3.5 activa flag true; usar SKIP solo cuando flag false **documentado**.
6. **Orden ejecución:** exigir **informe post-fix separado** (no mezclar con corrida pre-fix); Fase 0 seed → SMK → Jest → aprobaciones 20 → bloque P0 VEN/CMP → UI golden → back-office.
7. **Actualizar mapa OV1–OV17 → VEN-*:** OV12–14 son lookup (VEN-029–031), no duplicar en FIC.
8. **HUERFANOS como fuente de SKIP:** H1, H2, H4, H7, H8 «listo» → casos correspondientes **PASS esperado**, no DEBT.
9. **Prod:** mantener E2E-008 BLOCKED hasta checklist H14 ejecutado.
10. **Automatización:** priorizar script único `qa-integral-v2.ts` (propuesto Fase 4 §12) con salida JSON por ID v1.

### 7.2 Qué no repetir del pipeline 14/08

- Correr oleada 2 sin verificar usuarios QA en BD.
- Declarar RESUELTO en tabla aparte sin re-contar PASS/FAIL global.
- Usar retest UI Emitir del 14/08 como evidencia VEN-021–022.
- Clasificar productor/pantallas/ventaBajoCosto como gap Fase 1 si HUERFANOS ya cerró.

---

## 8. Checklist integridad para el runner (obligatorio)

El ejecutor del plan v2 **DEBE** cumplir antes y durante la corrida:

### Entorno

- [ ] Postgres `:5433`; API `:3001`; front `:5174`
- [ ] `npx prisma migrate deploy` sin pendientes (4 migraciones críticas §3.1 plan v1)
- [ ] `npm run seed` + `npm run seed:aprobaciones-f2` + `npm run seed:demo-propuesta`
- [ ] `.env`: `BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=true` para BIL-*
- [ ] Periodo `2026-08` ABIERTO; `GET .../stock-bodegas` INS-ALM-CEREZA > 0 **sin** movimiento manual

### Sesión y usuarios

- [ ] Tenant `EMP-1` en header y sesión
- [ ] OC solicitante **Luis** (`lherrera@almahue.cl`), aprobador **Jorge** + PIN `4821`
- [ ] AdminConcepto **Claudia/Ricardo**: **re-login** tras cambios en reglas (ADM-022, RB10)
- [ ] No usar admin como solicitante OC si prueba cadena (CP2)

### Evidencia

- [ ] JSON anonimizado por corrida en `qa/resultados/YYYY-MM-DD-integral-erp.json`
- [ ] **Prohibido** JWT/passwords en markdown
- [ ] UI: captura + URL + usuario por caso P0/P1
- [ ] Post-fix: **nueva corrida** completa o subconjunto declarado; no editar conteos viejos

### Clasificación

- [ ] FAIL solo si no está en tabla deuda §6.1 plan v1 + HUERFANOS + AGENTS
- [ ] BLOCKED vs FAIL: seed/migrate/API caída = BLOCKED
- [ ] DK-D4: no FAIL si flag comercial off **por decisión**; documentar flag en informe
- [ ] Jorge bandeja / S5 3M: cubiertos por seed — no reabrir como gap

### Cierre

- [ ] ≥ 90 % PASS excl. SKIP/BLOCKED documentados
- [ ] 0 FAIL P0 abiertos
- [ ] Invocar `almahue-qa-reviewer` sobre informe final
- [ ] Reconciliar post-fix en **un solo** documento de veredicto

---

## 9. Retest mínimo sugerido (sin batería completa)

Si v2 arranca antes de corrida total, ejecutar al menos:

| IDs | Motivo |
|---|---|
| SMK-001–008 | Gate entorno |
| ADM-009–015, ADM-022 | Aprobaciones + re-login |
| CMP-004–008, CMP-012–013 | OC + match |
| VEN-002–010, VEN-016–018, VEN-021–026, VEN-029–031 | OV + Emitir post-fix + lookup |
| RBAC-001, RBAC-007, RBAC-014 | Tenant + pantallas + bandeja comercial |
| INV-010 | H7 NC reingreso |
| BIL-001–002 | Stub DTE |
| E2E-002, E2E-003, E2E-006 | Golden ALM-* |

---

## 10. Veredicto final

| Pregunta | Respuesta |
|---|---|
| ¿Baseline confiable al 100 %? | **No** (~36 % plan v1 con evidencia) |
| ¿Reutilizar aprobaciones 20/20 y OV API core? | **Sí**, con retest RBAC-001 y lookup |
| ¿Listo para ejecutar plan v2 sin retrabajo documental? | **Parcial** — reconciliar inconsistencias §6 |
| **Veredicto pipeline** | **`REQUIERE_RETRABAJO`** |

**Condición para pasar a `LISTO_PARA_PLAN_V2`:**

1. Informe único post-fix Fase 5 (o descartar conteos pre-fix).
2. Retest VEN-021–022 + RBAC-001 + E2E-002/003 con `seed:demo-propuesta`.
3. Actualizar guías demo (Fase 3) con HUERFANOS y estado Emitir actual.
4. Primera corrida piloto plan v2 (mínimo retest §9) con checklist §8 cumplido.

---

*Revisor: almahue-qa-reviewer · Sin re-ejecución de pruebas en esta sesión.*
