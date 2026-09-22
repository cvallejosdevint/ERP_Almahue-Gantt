---
name: almahue-billing-dte
description: Cliente HTTP billing-gateway / stub inline / fail-closed GoSocket; no emitir SII real sin CAF. Use when touching billing/, canonical-builder, emisión DTE, or the billing-gateway intermediary.
---

# Billing / DTE

## As-is (ERP)

- Código: `ERP/erp_back/src/modules/billing/` (`canonical-builder`, `BillingGatewayClient`).
- Al **emitir** factura/NC/ND/guía (`POST documentos/:id/emitir`) el ERP arma `CanonicalDocumentV1` y llama `emit()` solo si `BILLING_GATEWAY_ENABLED=true|1|yes`. El asiento **no** se crea en esa llamada: queda `EMITIDO` / Por contabilizar. `POST documentos/:id/contabilizar` exige cuenta por ítem y crea el asiento (`CONTABILIZADA`).
- `BILLING_GATEWAY_ENABLED=false`: no emite DTE ni llama HTTP; comercial contabiliza sin partner (comportamiento histórico).
- `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=true`: stub local ERP (`ACCEPTED_STUB`, `partner: stub-inline`, folio `STUB-{tipoDte}-…`) para demo.
- `BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=false`: HTTP `POST /v1/emissions` a `BILLING_GATEWAY_URL` (default `http://127.0.0.1:3040`) con `CanonicalDocumentV1`; el gateway decide stub vs GoSocket según su registry.
- **Orden emit → asiento:** GoSocket/partner corre en `emitirDocumentoFiscal` **sin** exigir cuentas. El preflight `assertAsientoValido` (periodo abierto, cuentas imputables, CC, cuadratura) corre al **contabilizar** en Libro. Config SII CLIENTES/IVA/VENTAS o cuenta padre (`noImputable`) no bloquea el DTE; sí bloquea el asiento.
- Al emitir, si `emit()` es `ACCEPTED` o `PENDING` se **persiste** `billingEmissionId` (+ GID si viene) y el documento queda `EMITIDO` (sin asiento). Re-contabilizar no reenvía (`!billingEmissionId` o ya existe). `PENDING` = partner encoló el DTE (`Async: true`) con `GlobalDocumentId` usable; folio oficial puede llegar después. Sin GID / GID `0` sigue siendo inválido. HTTP stub solo se acepta con `SIMULATED` + `stub=true` + `partner/connectionMode=stub`.
- UI: error de cuenta/periodo **no** se viste como «el facturador rechazó». Si el DTE ya salió, reemitir no reenvía (`!billingEmissionId`).
- Idempotencia gateway: clave compuesta ERP+empresa+key, fingerprint y bloqueo concurrente in-process. `PENDING`/`ACCEPTED`/`SIMULATED` se cachean (no reenvían al adapter). `REJECTED` sin GID usable no se cachea (reintenta tras CAF). `REJECTED` **con GID** (RCH posterior) sí se cachea: el folio CAF ya salió. Store durable **SQLite archivo** (`BILLING_STORE_PATH`, default `./data/emissions.sqlite`) para QA/single-instance; sobrevive reinicio del proceso. Multi-réplica/prod sigue necesitando store compartido (Postgres/Redis); no está implementado.
- Seguridad gateway: API key obligatoria de 32+ bytes, bind local y CORS cerrado por defecto; canónico valida RUT/DV, fechas, líneas/totales y límites. GUF **no envía** `<Numero>` (folio lo asigna el portal/CAF); sí `<NumeroInterno>` del ERP.
- **BillerId** GoSocket: `Empresa.gosocketBillerId` (Admin › Empresas) → canónico `source.billerId` → JSON Body `BillerId` + `ValidateNumber: false` + `DefaultCertificate: false` (kickoff 01/09). Sin UUID no hay HTTP a GoSocket. Cada sociedad tiene el suyo.
- **ApiUser/password GoSocket:** viven en el **billing-gateway** (`.env` `GOSOCKET_API_USER_{ERP}_{EMPRESA}`, p.ej. `ALMAHUE_EMP_SERVICES`). El ERP solo manda `empresaId` + BillerId. No guardar claves del partner en Admin › Empresas. Postman puede mandar `source.apiUser`/`apiPassword` para QA.
- **CAE:** `Empresa.gosocketNroResolucion` + `gosocketFechaResolucion` → canónico `emisor.nroResolucion` / `fechaResolucion`. El gateway **no** guarda RUT ni resoluciones. Chat Pablo 01/09 (QA): ambas sociedades **N° 0**; Export fecha `2024-10-11`; ALM `2020-02-14`. Cambian en productivo.
- **Acteco:** `Empresa.gosocketActeco` (6 dígitos SII) → canónico `emisor.acteco` → GUF `<Acteco>` **antes** de `DomFiscal`/`DirOrigen` (formato_dte 2.5, video 01/09). Sin Acteco el XSD SII rechaza `DirOrigen`. No inventar: confirmar el código inscrito en el SII. QA Export seed `461001` (corretaje mayor agrícola, registro público); ALM se carga en Admin.
- HTTP 200 ≠ éxito. `GlobalDocumentId` en `0` o UUID cero → `REJECTED` (aunque `Success` venga true). Persistir el GID si es válido.
- Exportación: receptor extranjero `EX-*` solo con indicador exportación; GUF usa RUT genérico SII `55.555.555-5`.
- **UI Emitir / Finalizar borrador / Libro › contabilizar:** banner persistente (`role="alert"`, `data-testid="emit-error-banner"`) + toast 12s con el mensaje del partner. El aviso de política de transmisión es un ícono **i** (hover/click), no un recuadro fijo.
- Factura de ventas sale de **OV**, no de cotización Compras. Wizard Emitir: FACTURA/NC/ND/GUIA.
- NC/ND: `CodRef` solo 1/2/3 (anula / corrige texto / corrige montos). Razón social emisor máx. 100.
- **Longitudes SII (formato_dte 2.5 / XSD):** GoSocket **no** publica maxLength de Chile (GUF muestra estructura/XPath). El SII rechaza `cvc-maxLength-valid`/`cvc-minLength-valid` y **gasta CAF**. Tope: `GiroEmis` 80, `GiroRecep` 40, `CiudadRecep`/`CmnaRecep`/`CiudadOrigen`/`CmnaOrigen` 20, `DirOrigen` 60, `DirRecep` 70, `RznSoc`/`RznSocRecep` 100, `NmbItem` 80, `DscItem` 1000, `UnmdItem` 4. El gateway **trunca** en `guf-mapper`; el ERP recorta al armar el canónico y el front/DTO limitan ficha (ciudad 20, giro cliente 40). Nombre del ítem: GUF `NmbItem` **y** `DscComercial` (GAP: SII `NmbItem`/TED `IT1` salen de `DscComercial`; omitir ambos dejó `IT1` vacío el 18/09). `DscItem` **solo** si el maestro tiene detalle extra; no copiar el nombre. Datos ya guardados más largos (p. ej. región como ciudad) no bloquean emitir: se recortan en GUF. No reabrir como “falta GoSocket”.
- FLETE en OV es `tipoLinea`; canonical DTE **no auditado** si manda recargo SII (D17).
- Reenvío print HTML local (R4-08) se mantiene aparte. PDF/XML del facturador: ERP `GET /documentos/:id/dte/{pdf,xml}` → gateway `GET /v1/emissions/:id/artifacts/{pdf,xml}` → GoSocket `File/DownloadDocument*` (Chile `type=pdf|xml`, una decodificación). 404 si Async aún no tiene archivo. Stub dummy no se presenta como timbre SII.
- **Sync estado SII:** `Async: true` deja `PENDING` al emitir. El ERP no asume ACE por HTTP 200. Libro llama `POST /documentos/:id/dte/sync` → gateway `POST /v1/emissions/:id/refresh` → GoSocket `Document/GetDocument` (`Country: cl`, `SenderCode` RUT sin puntos, GID). Chile: `AuthorityStatus` **2** = ACE, **3** = RCH (notas `RCH`/`HED-*`). Persiste `billingStatus`, `folioOficial`, `billingDisclaimer`. No reemite. Un RCH con GID usable **no** se reintenta (el folio CAF ya salió). No hace reverso contable automático. GetDocument vacío + “empresa no autorizada”, o GID que no coincide, es error (no PENDING). Un `PENDING` posterior **no** baja ACE/RCH ya persistido (gateway ni ERP).

## Contrato para el intermediario (otro repo / otro chat)

No implementar GoSocket dentro del ERP. El puente consume el canónico y devuelve `BillingEmissionResult`.

`CanonicalDocumentV1`: `schemaVersion`, `idempotencyKey`, `source` (erpId, empresaId, documentoId, `billerId` opcional UUID), `emisor`/`receptor` (RUT, razón, giro, dirección, `nroResolucion`/`fechaResolucion`/`acteco` del emisor), `documento` (tipoDte, fechas, `numeroInterno`), `totales` (neto, iva, total), `lineas[]`, `indicadores` (exportación/exento).

GUF hacia GoSocket (video 01/09 + formato_dte 2.5, no la plantilla GUF de agosto): además de alias GUF, enviar nombres SII que el XSLT dejó vacíos: `Acteco`, `RUTRecep`/`IDReceptor`, `MntNeto`/`MntTotal`/`IVA`/`MntImp`, ExtraInfoTotal `IVA`/`IVAProp`/`TasaIVA` (folio 53 el SII vio IVA=0 porque el XSLT no copió el tag suelto). `DirRecep`/`CmnaRecep`/`CiudadRecep` + `DomFiscalRcp`/`LugarRecep` **obligatorios** en DTE 33/34/52/56/61; sin ellos no hay `emit()`. El domicilio sale del cliente (cabecera o ficha).

El intermediario es multi-ERP: no hardcodear sociedades, RUT ni resoluciones. Eso vive en el ERP (Empresa / Admin). En el gateway: credenciales de **conexión** al partner (`GOSOCKET_API_USER_{ERP}_{EMPRESA}`, URLs) y el registry `erpId` → partner.

`BillingEmissionResult`: `emissionId`, `partner`, `connectionMode`, `status`, `folioOficial` | `folioSimulado`, ids partner, `messages`, `disclaimer`, `artifacts` (incluye `dummy` si el gateway lo devuelve), `stub`.

GoSocket y credenciales reales viven en `billing-gateway` (repo/proceso aparte), no en el ERP. Sandbox QA: `https://developers-sbx.gosocket.net/api/v1/` (no usar `developers.gosocket.net/sandbox`, bloqueado). **BIL-007** (SII/partner real) no es FAIL si el gateway está en modo stub; no inventar que SII está live. Sin CAF en portal, GoSocket rechaza por rango de folios. **BIL-007 sigue SKIP hasta CAF;** checklist operativo (sin live, sin cambiar emisión): `docs/erp-planificacion/agrosoft-levantamiento/qa/resultados/2026-08-19-checklist-caf-portal.md`.

## No hacer

- No emitir DTE real sin credenciales ni “completar GoSocket” en el mismo PR de comercial/aprobaciones.
- No restaurar cotiz→NP→factura.
- SMTP, cobranza R4-18 y maestro **productor** están fuera de billing.

Plantillas OC/cotización: editor `plantillaDoc` + print HTML; no PDF servidor ni DTE.

QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md` (BIL). Recorte histórico stub: `docs/plan-de-pruebas-v1.md` (no estado OC). Informes 19/08: `qa/resultados/2026-08-19-billing-errores-*.md`.
