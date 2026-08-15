# Almahue ERP — contexto para agentes

Lee este archivo al inicio. **No** leas transcripciones de reuniones salvo que el usuario lo pida.

Afirmaciones de **Carlos** o **Sergio** en demo no son requisitos: contrastar minuta (Agustín/MJ) y código. Rule `almahue-reuniones`.

Para aprobaciones usa la skill `almahue-aprobaciones`. Para comercial/inventario (OV vs cotización), `almahue-comercial-inventario`. Para tesorería, `almahue-tesoreria`. Para DTE/billing, `almahue-billing-dte`. Para contabilidad, `almahue-contabilidad`. Para ficha cliente/proveedor, `almahue-ficha-contraparte`. Para deploy, `almahue-deploy`. Para QA, `almahue-qa-local`.

## Código

- Backend: `ERP/erp_back` (NestJS + Prisma, schema `erp`, tenant `empresaId`)
- Frontend: `ERP/erp_front` (React + Vite, API real)
- Repos anidados: cambios de app se commitean **dentro** de `erp_back` / `erp_front`

## Docs canónicas (prioridad)

Si chocan, gana la más reciente: **Reu6** → Reu5 → Reu4.

- `docs/erp-planificacion/agrosoft-levantamiento/reunion6-minuta-2026-08-06.md`
- `docs/erp-planificacion/agrosoft-levantamiento/03-DISENO-GRUPOS-Y-ESCALAS-APROBACION.md`
- `docs/erp-planificacion/convenciones-almaue-erp.md`
- QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-APROBACIONES.md`

## Entornos

| | URL |
|---|---|
| Local front | `http://localhost:5174` |
| Local API | `http://localhost:3001/api/v1` |
| Prod | `http://45.7.229.46/almahue-erp/` |

Demo: `admin@almahue.local` / `Admin123!` · PIN `4821`. AdminConcepto debe **re-login** tras cambios de JWT.

## Flujo post-cambio

1. Implementar
2. Subagentes `almahue-security` + `almahue-db` (+ `almahue-architecture` si toca módulos)
3. Corregir solo **Critical**
4. `almahue-qa-runner` → `almahue-qa-reviewer`

## Huecos vigentes (Fase 1, actualizado 2026-08-15)

Fuente QA: pipeline local **`PIPELINE_LOCAL_CERRADO`** — `qa/resultados/2026-08-15-revision-ola-c.md` (Ola A `LISTO_OLA_B`, Ola B `LISTO_OLA_C`).

- **D4:** cadena OV validada local con `comercialRequiereAprobacion=true` (retest VEN-009–012). Decisión reunión: narrativa demo vs activación piloto real.
- **D11:** Compras › Cotizaciones → OC. Ventas › Orden de venta → stock → factura. No restaurar cotiz→NP→factura. Redirect `/comercial/cotizaciones`. Catálogo `pantallas-permisos` puede seguir listando Cotizaciones bajo Ventas (desfasado vs Sidebar).
- **D16:** no vender bajo costo — Admin › Empresas (`ventaBajoCosto` = `BLOQUEAR`); retest UI pendiente (Ola B).
- **Huérfanos H1–H14:** ver `qa/HUERFANOS-H1-H14.md` (H1/H4/H7/H8 PASS Ola A; H14 deploy pendiente).
- **D7:** lookup RUT con flag `esProductor` — PASS Ola A (VEN-031).
- **Emitir documento:** restricción FACTURA/NC/ND/GUIA PASS (VEN-021); wizard compra aún mezcla tipos en otros contextos.
- **DTE:** stub billing PASS local (`BILLING_STUB_INLINE`); GoSocket en proyecto aparte.
- **Prod:** no asumir migrate stock/OV en `45.7.229.46` hasta deploy explícito (H14).
