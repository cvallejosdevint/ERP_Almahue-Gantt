# Estado QA — Aprobaciones fase 2 (2026-08-13)

**Entorno:** local · API `http://localhost:3001/api/v1` · Front `http://localhost:5174`  
Punto de entrada para un chat nuevo. No incluye JWT ni passwords.

## Resumen

| Área | Resultado | Nota |
|---|---|---|
| Plan **con seed** (`PLAN-PRUEBAS-APROBACIONES.md`) | **20/20 PASS** | `ERP/.qa-tmp/qa-retest-seed.mjs` (incluye S5 3M y OC2/OC3 Jorge+PIN por API) |
| AdminConcepto sin seed (`e2e-admin-concepto.spec.ts`) | **6/6 PASS** | Spec dedicado, `--workers=1` |
| E2E sin seed largo (`e2e-manual-sin-seed.spec.ts`) | **34/34 PASS** | Playwright exit 0 · `e2e-manual-results.json` |
| Fase 2 aprobaciones (permisos, bandeja, PIN, simulador) | **Cerrada en local** | Listo para chat nuevo / deploy |
| Listados UI Contratistas / tarifas | **OK** | `X-Empresa-Id` usa selector de empresa |

**No borrar** los planes `PLAN-PRUEBAS-APROBACIONES.md` ni `PLAN-PRUEBAS-E2E-MANUAL-SIN-SEED.md`: definen casos reutilizables.

Smoke post-deploy (cuando haya deploy): `ERP/DEPLOY-PROD-FASE2.md` §5–6.

---

## Qué está certificado (local)

- AdminConcepto por módulo (JWT, API grupos/usuarios, combo módulo, sidebar).
- Bandeja runtime: aprobador designado (p.ej. Jorge U-3) resuelve OC **sin** `compras:read` global (`bandejaModulos` + PIN). Cubierto por OC2/OC3 en el retest con seed.
- Validación `APROBADOR_SIN_BANDEJA` al guardar escalas.
- Simulador S1–S6, **incluido S5** (Luis $3.000.000 → Jorge → Claudia) vía `POST /aprobaciones/simular`.
- Flujo OC emitir → bandeja → PIN → rechazo/re-solicitud (E2E fases 3–4).
- Contratistas: alta UI, tarifas API+UI, proformas y aprobación (fase 5).
- Import/export reglas (fase 6); import cross-módulo corregido.
- `npx tsc -b` front **PASS**.
- KPI dashboard `ocPorAprobar`: pendientes del usuario (admin: total empresa).
- Parsers tesorería: `tryParseBankSpecific` recorre detectores; fixtures `.txt` no las captura `almahue-web`.

### Comandos de re-ejecución

```bash
# Con seed (20 casos API: E, S1–S6, AC, OC1–OC4, V1, R1)
cd ERP/erp_back && npm run seed && npm run seed:aprobaciones-f2
cd ERP/.qa-tmp && node qa-retest-seed.mjs

# AdminConcepto sin seed (6 casos UI+API)
cd ERP/erp_back && npm run reset:superadmin
cd ERP/.qa-tmp && npx playwright test e2e-admin-concepto.spec.ts --workers=1

# E2E completo sin seed (34 casos)
cd ERP/erp_back && npm run reset:superadmin
cd ERP/.qa-tmp && npx playwright test e2e-manual-sin-seed.spec.ts --workers=1
```

**Requisitos:** Postgres en `:5433`, API y front locales corriendo.

Artefactos: `ERP/.qa-tmp/qa-retest-seed-results.json`, `e2e-admin-concepto-results.json`, `e2e-manual-results.json`.

---

## Correcciones aplicadas (sesión 2026-08-12/13)

| Área | Cambio |
|---|---|
| `http.ts` | `X-Empresa-Id` usa `readSelectedEmpresaId()` (selector header) antes que `session.empresaId` |
| `countPendientesModulo` | Solo OC (Compras) o proformas (Contratistas) |
| `MockListPage` | `staleTime: 0`, `refetchOnMount: 'always'` |
| Workflows legacy | `hasGruposActivos` cuando hay grupos/escalas |
| Seguridad | Resolución OC sin mutar campos financieros; AdminConcepto revalidado en BD en writes; export delegaciones por módulo |
| E2E spec | `switchEmpresa` sincroniza localStorage+sesión+reload; E2E-1.5 navega a aprobaciones; E2E-5.2 valida UI; `expect` final si hay `record(FAIL)` |
| Dashboard KPI | `ocPorAprobar` filtra por aprobador (mismo criterio que notificaciones) |
| Tesorería parsers | Fallback si el primer detector no parsea; `almahue-web` ignora `.txt`/`.csv` |

---

## Histórico

Informes parciales del 2026-08-12 y el gap «Jorge sin bandeja» quedaron **obsoletos**. Ver `historico-reu4/` solo para contexto Reu4.

*Última actualización: 2026-08-13 (fase 2 local cerrada, sin gaps abiertos)*
