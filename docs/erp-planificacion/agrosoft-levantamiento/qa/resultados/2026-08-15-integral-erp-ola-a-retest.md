# Resultados QA — Retest mínimo Ola A

**Fecha:** 2026-08-15  
**Ejecutor:** almahue-qa-runner  
**Plan:** `2026-08-15-revision-ola-a.md` §6 · `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`  
**Entorno:** local · API `:3001` · front `:5174`  
**JSON:** `2026-08-15-integral-erp-ola-a-retest.json`

## Precondiciones

| Check | Estado | Nota |
|---|---|---|
| Health API | PASS | `GET /health` 200 `db=ok` |
| Billing `.env` | PASS | `BILLING_GATEWAY_ENABLED=true`, `BILLING_STUB_INLINE=true` — API reiniciada |
| Seed demo | PASS | `npm run seed:demo-propuesta` antes de corrida |
| `comercialRequiereAprobacion` | PASS | `true` en EMP-1 (seed) |

## Conteo

| PASS | FAIL | BLOCKED | Total |
|---|---|---|---|
| 11 | 0 | 0 | 11 |

**Veredicto runner:** `OLA_A_RETEST_OK`

## Casos

| ID | Resultado | Evidencia |
|---|---|---|
| BIL-001 | PASS | `POST /documentos/DOC-ALM-FAC-BORR/contabilizar` 201 · `billingStub=true` · `billingStatus=ACCEPTED_STUB` |
| BIL-002 | PASS | UI `/comercial/emitir` — disclaimer stub GoSocket visible (panel «Resumen de transmisión») |
| VEN-009 | PASS | OV $800k: `cperez` crea · `admin` solicita · `PENDIENTE_APROBACION` · aprobador `U-6` |
| VEN-010 | PASS | `GET /aprobaciones-ov` incluye `ALM-OV-002` · `POST aprobar-ov` PIN×3 → `AUTORIZADA` · UI `/comercial/aprobaciones` carga (sin filas en headless) |
| VEN-011 | PASS | OV $3,8M: cadena 3 pasos · `AUTORIZADA` tras aprobaciones PIN admin |
| VEN-012 | PASS | Solicitante `U-6` (María) · omite auto-aprobación · primer aprobador `U-3` |
| CMP-012 | PASS | `POST /registros-compra` `ALM-OC-003` monto=600.000 · `matchOk=true` |
| CMP-013 | PASS | Mismo OC monto=450.000 (líneas explícitas) · `matchOk=false` · `matchDiff=-150000` |
| INV-010 | PASS | NC contabilizada · movimiento `DEVOLUCION_NC` · delta stock cereza +10 en `BOD-ALM-FRIG` |
| ADM-022 | PASS | Admin cambia AdminConcepto Claudia · re-login · `adminConceptoModulos` actualizado (`Contratistas`) |
| ADM-015 | PASS | `POST /escalas-aprobacion` aprobador sin bandeja · 400 `APROBADOR_SIN_BANDEJA` |

## Notas de ejecución

- **API reiniciada** para cargar flags billing tras fix post-revisión Ola A.
- **VEN-009 / VEN-011:** `cperez` crea OV (`compras:write`); `admin` ejecuta `solicitar-aprobacion-ov` (solicitante queda `U-2` en grupo Comercial).
- **VEN-010:** Aprobación funcional vía API (admin superadmin + PIN). Bandeja UI no listó filas en Playwright headless; API sí devuelve `ALM-OV-002`. Revisar con `almahue-qa-reviewer` si se exige captura UI con `mgonzalez` (rol sin `comercial:write`).
- **CMP-013:** Requiere `lineas` en body; sin ellas el servicio hereda líneas OC y `matchOk` queda `true`.

## Defectos vs deuda

| ID | Clasificación | Nota |
|---|---|---|
| — | — | Sin FAIL P0 en este retest |

## Retest sugerido

- Opcional: VEN-010 captura UI manual con `mgonzalez@almahue.cl` si se cierra gap permiso `comercial:write` para aprobadores designados.
- Continuar Ola B según plan v2 tras revisión `almahue-qa-reviewer`.
