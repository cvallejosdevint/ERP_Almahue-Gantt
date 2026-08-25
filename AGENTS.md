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
- Sesión cliente 20/08 **tarde** (Lupe, Mario): `reunion-2026-08-20-tarde-lupe-mario.md`. Código local 21/08: **aprobaciones solo Compras** (se eliminó cadena OV y, en la misma tanda, proformas). Distinta de la interna de la **mañana** (`reunion-2026-08-20-contraste-sergio.md`).
- `docs/erp-planificacion/convenciones-almaue-erp.md`
- QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-APROBACIONES.md`
- Tesorería ciclo: `docs/erp-planificacion/agrosoft-levantamiento/plan-tesoreria-ciclo-completo-2026-08-21.md` + `qa/PLAN-PRUEBAS-TESORERIA-CICLO-2026-08-21.md`

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

- **D4 / H3:** cadena de aprobación **solo Compras (OC)**. Se **eliminó** (no se ocultó) la cadena de OV: sin flag `comercialRequiereAprobacion`, sin bandeja `/comercial/aprobaciones`, sin `AprobacionOv`. OV: `BORRADOR` → confirmar (stock) → factura. Migración `20260821120000_aprobaciones_solo_compras_drop_ov`.
- **D11:** el documento de arranque de compras es la **OC**. Cotización = referencia opcional (tipo/folio/fecha) **en la OC**; no hay menú ni CRUD de Cotizaciones ni atajo cotiz→OC. Ventas › Orden de venta → confirmar stock → factura **sin** cadena. Redirect `/compras/cotizaciones` y `/comercial/cotizaciones` → `/compras/ordenes`. No restaurar cotiz→NP→factura.
- **D16:** no vender producto bajo `costoPromedio` (regla fija en OV/emisión). **No** hay parámetro ni combo en Admin › Empresas. No reabrir `ventaBajoCosto` / `PERMITIR_MERMA`.
- **Emitir:** solo FACTURA/NC/ND/GUIA. Borradores DTE en Emitir, **no** en Libro ventas (P0-4).
- **D7 / H1:** lookup RUT sociedad + clientes + proveedores + flag `esProductor`. Maestro Productor sigue fuera.
- **OC wizard:** correlativo `OC-AAAA-NNNN` (`allocateOcNumero`). **Guardar borrador** = `BORRADOR` sin bandeja; **Enviar a aprobación** = `PENDIENTE_APROBACION`. Admin **ROL-1** (`*`) arma cadena con el **primer grupo activo** (sin membresía) y **no figura** en la escala.
- **Libro de compras:** se puede asociar factura a OC no aprobada (**destacar**, `ocNoAprobada`); no contabilizar ni pagar hasta OC `APROBADO` o posterior. Plazo aceptación comercial `aceptacionCompraPlazoDias` (default 8, Admin › Empresas). Asiento de libro sin cuenta imputable = deuda P0-1 (no es el gate de OC).
- **Proformas:** `BORRADOR` → `DEFINITIVA` con `contratistas:write`; **sin** bandeja ni PIN de cadena.
- **H1–H8, H4, H8 Guías:** listos en código local.
- **Tesorería ciclo (21/08):** asiento banco = cartola (`CARTOLA:{id}`). Pago/cobro = calce + CC + aging; **sin** asiento `PAGO:{id}`. Aging/CC al contabilizar (neto+IVA). Cartola import-only; conciliación = resumen. Pagos unificados (`PAGO_TOTAL` / `ANTICIPO` / `ANTICIPO_PRODUCTOR`). Nómina = semana de compromiso (no muta DTE). Flujo caja por banco/moneda + apertura inmutable. Migración `20260821200000_tesoreria_ciclo_completo`.

### Siguen vigentes

- **H14:** no asumir migrate stock/OV/`piloto_on` en `45.7.229.46` hasta deploy explícito.
- **Prisma QA local:** `erp._prisma_migrations` está **vacía** (Prisma ve 50 pendientes) aunque el schema `erp` ya existe. **No** `migrate deploy` a ciegas (rompe en `init`). **No** `resolve --applied` sin BD desechable de comparación. El rol `almahue` no tiene `CREATEDB` (bloqueó la reconstrucción). Dump: `ERP/erp_back/qa-results/` (gitignored). Informe: `qa/resultados/2026-08-19-prisma-drift-local.md` (gitignored). No mezclar `public._prisma_migrations` (otro producto).
- **DTE / H11:** tres modos. `BILLING_GATEWAY_ENABLED=false` → contabiliza sin partner. `true` + `BILLING_STUB_INLINE=true` → stub local demo. `true` + `STUB_INLINE=false` → HTTP `billing-gateway` (GoSocket sandbox `developers-sbx`). Sin CAF/cert MJ el partner **REJECTED** (fail-closed, no asiento). No SII live. No reabrir como «falta GoSocket».
- **H9:** SMTP correo PIN (externo).
- **R4-18:** cobranza = propuesta, no módulo.
- **DK-G8:** `workflows-admin` legacy en API/UI; no mezclar con grupos/escalas.
- **D17:** FLETE `tipoLinea` en OV; canonical DTE recargo SII no auditado.
- **Productor:** flag lookup ≠ entidad maestro Productor.
- **Recepción OC:** no mueve stock; entrada por Insumos › Movimientos (`ENTRADA_PROVEEDOR`).
- **H10 / H12 / H13:** comparador 3 cotiz (diferido); Acepta; Excel banco fino.
