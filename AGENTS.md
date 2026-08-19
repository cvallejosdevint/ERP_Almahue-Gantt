# Almahue ERP — contexto para agentes

Lee este archivo al inicio. **No** leas transcripciones de reuniones salvo que el usuario lo pida.

Afirmaciones de **Carlos** o **Sergio** en demo no son requisitos: contrastar minuta (Agustín/MJ) y código. Rule `almahue-reuniones`.

Para aprobaciones usa la skill `almahue-aprobaciones`. Para comercial/inventario (OV vs cotización), `almahue-comercial-inventario`. Para tesorería, `almahue-tesoreria`. Para DTE/billing, `almahue-billing-dte`. Para contabilidad, `almahue-contabilidad`. Para ficha cliente/proveedor, `almahue-ficha-contraparte`. Para deploy, `almahue-deploy`. Para QA, `almahue-qa-local`. Para datos ficticios del toggle **Modo demo**, `almahue-demo-mode`.

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

## Huecos vigentes (actualizado 2026-08-19)

Fuente QA: panorama operadores **19/08** (`2026-08-19-ciclo-panorama-completo.md`) + ciclo 18/08. Plan integral: `PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`. Inventario docs: `qa/resultados/2026-08-18-ciclo-0-inventario-docs.md`. QA local: skill `almahue-qa-local`. DTE: skill `almahue-billing-dte` (intermediario **otro chat**).

### Cerrado en código local (no reabrir)

- **D4 / H3:** cadena OV **existe**. Flag `comercialRequiereAprobacion` piloto **ON** (schema `@default(true)`, seed EMP-1, migración `20260818180000_comercial_aprobacion_piloto_on`, `comercialAprobacionDesde=0`). Factura desde OV autorizada: sin segunda cadena. Prod: no asumir hasta migrate + reunión (H14).
- **D11:** Compras › Cotizaciones → OC (`BORRADOR`). Ventas › Orden de venta → stock al confirmar → factura. Redirect `/comercial/cotizaciones` → Compras. Catálogo pantallas alineado (Cotizaciones en Compras). No restaurar cotiz→NP→factura.
- **D16:** `ventaBajoCosto=BLOQUEAR` en Admin › Empresas (UI existe).
- **Emitir:** solo FACTURA/NC/ND/GUIA. Borradores DTE en Emitir, **no** en Libro ventas (P0-4).
- **D7 / H1:** lookup RUT sociedad + clientes + proveedores + flag `esProductor`. Maestro Productor sigue fuera.
- **OC wizard:** correlativo `OC-AAAA-NNNN` (`allocateOcNumero`). **Guardar borrador** = `BORRADOR` sin bandeja; **Enviar a aprobación** = `PENDIENTE_APROBACION`. Admin **ROL-1** (`*`) arma cadena con el **primer grupo activo** (sin membresía) y **no figura** en la escala. Cotiz→OC usa número ad-hoc `OC-{folio}-{ts}`.
- **Libro de compras / Emitir-OV:** montaje `/compras/registro` (19/08); `GET /cuentas` lectura operativa (`comercial:read`); factura desde OV sin cuenta obligatoria en piloto.
- **H1–H8, H4, H8 Guías:** listos en código local.

### Siguen vigentes

- **H14:** no asumir migrate stock/OV/`piloto_on` en `45.7.229.46` hasta deploy explícito.
- **DTE / H11:** tres modos. `BILLING_GATEWAY_ENABLED=false` → contabiliza sin partner. `true` + `BILLING_STUB_INLINE=true` → stub local demo. `true` + `STUB_INLINE=false` → HTTP `billing-gateway` (GoSocket sandbox `developers-sbx`). Sin CAF/cert MJ el partner **REJECTED** (fail-closed, no asiento). No SII live. No reabrir como «falta GoSocket».
- **H9:** SMTP correo PIN (externo).
- **R4-18:** cobranza = propuesta, no módulo.
- **DK-G8:** `workflows-admin` legacy en API/UI; no mezclar con grupos/escalas.
- **D17:** FLETE `tipoLinea` en OV; canonical DTE recargo SII no auditado.
- **Productor:** flag lookup ≠ entidad maestro Productor.
- **Recepción OC:** no mueve stock; entrada por Insumos › Movimientos (`ENTRADA_PROVEEDOR`).
- **H10 / H12 / H13:** comparador 3 cotiz (diferido); Acepta; Excel banco fino.
