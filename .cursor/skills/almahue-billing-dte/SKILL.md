---
name: almahue-billing-dte
description: Cliente HTTP billing-gateway / stub inline / fail-closed GoSocket; no emitir SII real sin CAF. Use when touching billing/, canonical-builder, emisión DTE, or the billing-gateway intermediary.
---

# Billing / DTE

## As-is (ERP)

- Código: `ERP/erp_back/src/modules/billing/` (`canonical-builder`, `BillingGatewayClient`).
- Al contabilizar factura/NC/ND/guía el ERP arma `CanonicalDocumentV1` y llama `emit()` solo si `BILLING_GATEWAY_ENABLED=true|1|yes`.
- `BILLING_GATEWAY_ENABLED=false`: no emite DTE ni llama HTTP; comercial contabiliza sin partner (comportamiento histórico).
- `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=true`: stub local ERP (`ACCEPTED_STUB`, `partner: stub-inline`, folio `STUB-{tipoDte}-…`) para demo.
- `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=false`: HTTP `POST /v1/emissions` a `BILLING_GATEWAY_URL` (default `http://127.0.0.1:3040`) con `CanonicalDocumentV1`; el gateway decide stub vs GoSocket según su registry.
- Al contabilizar, si `emit()` es `ACCEPTED` se **persiste** `billingEmissionId` **antes** del asiento (evita reenviar al partner si el asiento falla). HTTP stub solo se acepta con `SIMULATED` + `stub=true` + `partner/connectionMode=stub`.
- Idempotencia gateway: clave compuesta ERP+empresa+key, fingerprint y bloqueo concurrente in-process. `PENDING`/`ACCEPTED`/`SIMULATED` se cachean (no reenvían al adapter); `REJECTED` no se cachea (reintenta tras CAF). Store durable **SQLite archivo** (`BILLING_STORE_PATH`, default `./data/emissions.sqlite`) para QA/single-instance; sobrevive reinicio del proceso. Multi-réplica/prod sigue necesitando store compartido (Postgres/Redis); no está implementado.
- Seguridad gateway: API key obligatoria de 32+ bytes, bind local y CORS cerrado por defecto; canónico valida RUT/DV, fechas, líneas/totales y límites. GUF **no envía** `<Numero>` (folio lo asigna el portal/CAF); sí `<NumeroInterno>` del ERP.
- **BillerID** GoSocket: `Empresa.gosocketBillerId` → canónico `source.billerId` → JSON Body `BillerID`. Sin UUID no hay HTTP a GoSocket. QA export `9a518154-b579-4d43-9cd8-af38762199c0`; services `d23bdecb-0776-433b-aaf2-ab4e11e76501`.
- Exportación: receptor extranjero `EX-*` solo con indicador exportación; GUF usa RUT genérico SII `55.555.555-5`.
- **UI Emitir / Finalizar borrador / Libro › contabilizar:** banner persistente (`role="alert"`, `data-testid="emit-error-banner"`) + toast 12s con el mensaje del partner. El aviso de política de transmisión es un ícono **i** (hover/click), no un recuadro fijo.
- Factura de ventas sale de **OV**, no de cotización Compras. Wizard Emitir: FACTURA/NC/ND/GUIA.
- FLETE en OV es `tipoLinea`; canonical DTE **no auditado** si manda recargo SII (D17).
- Reenvío PDF/XML libro (R4-08): print HTML local; XML/PDF partner diferido.

## Contrato para el intermediario (otro repo / otro chat)

No implementar GoSocket dentro del ERP. El puente consume el canónico y devuelve `BillingEmissionResult`.

`CanonicalDocumentV1`: `schemaVersion`, `idempotencyKey`, `source` (erpId, empresaId, documentoId, `billerId` opcional UUID), `emisor`/`receptor` (RUT, razón, giro, dirección), `documento` (tipoDte, fechas, `numeroInterno`), `totales` (neto, iva, total), `lineas[]`, `indicadores` (exportación/exento).

`BillingEmissionResult`: `emissionId`, `partner`, `connectionMode`, `status`, `folioOficial` | `folioSimulado`, ids partner, `messages`, `disclaimer`, `artifacts` (incluye `dummy` si el gateway lo devuelve), `stub`.

GoSocket y credenciales reales viven en `billing-gateway` (repo/proceso aparte), no en el ERP. Sandbox QA: `https://developers-sbx.gosocket.net/api/v1/` (no usar `developers.gosocket.net/sandbox`, bloqueado). **BIL-007** (SII/partner real) no es FAIL si el gateway está en modo stub; no inventar que SII está live. Sin CAF en portal, GoSocket rechaza por rango de folios. **BIL-007 sigue SKIP hasta CAF;** checklist operativo (sin live, sin cambiar emisión): `docs/erp-planificacion/agrosoft-levantamiento/qa/resultados/2026-08-19-checklist-caf-portal.md`.

## No hacer

- No emitir DTE real sin credenciales ni “completar GoSocket” en el mismo PR de comercial/aprobaciones.
- No restaurar cotiz→NP→factura.
- SMTP, cobranza R4-18 y maestro **productor** están fuera de billing.

Plantillas OC/cotización: editor `plantillaDoc` + print HTML; no PDF servidor ni DTE.

QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (BIL). Recorte histórico stub: `docs/plan-de-pruebas-v1.md` (no estado OC). Informes 19/08: `qa/resultados/2026-08-19-billing-errores-*.md`.
