> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# Retest final — gaps permisos + aprobaciones

Fecha: 2026-07-31 · Stack local MODO REAL · BD `localhost:5433` ok

## API — 20/20 PASS

| Área | Casos |
|------|--------|
| OC | crear / no-aprobar solicitante / no-aprobar lectura / aprobar / rechazar / bandeja aprobador |
| Proformas | solicitar / no-aprobar solicitante+digitador / aprobar / rechazar |
| RBAC | digitador 403 compras · lectura 403 create · solicitante 403 admin · lecturas OK |

Detalle: `04-RETEST-GAPS-API.json`

## UI — gaps cerrados

| Rol | Menú | OC / Aprobaciones | Proformas |
|-----|------|-------------------|-----------|
| **QA Lectura** | Sin Administración | Sin **Nueva OC**; solo **Ver** (sin Aprobar) | — |
| **Digitador** | Solo Contratistas | `/compras/ordenes` → redirect `/` | Acceso OK |
| **QA Solicitante** | Compras+Contratistas (sin Admin) | **Nueva OC** sí | Pendiente sin **Aprobar** |
| **QA Aprobador** | Compras+Contratistas | Ve **Aprobar/Rechazar**; UI aprobó `OC-UI-131819` → APROBADA | Ve **Aprobar/Rechazar** |

## Fix extra descubierto en retest

`decide()` de bandeja OC enviaba el objeto OC completo con `null`s → Nest 400.  
Payload limpio en `ComprasPages.tsx`; UI Aprobar funciona.

## Credenciales QA

| Email | Pass | Rol |
|-------|------|-----|
| `qa.aprobador@almahue.local` | `QaTest123!` | Aprobador |
| `qa.solicitante@almahue.local` | `QaTest123!` | Solicitante |
| `qa.lectura@almahue.local` | `QaTest123!` | Solo lectura |
| `jsanchez@almahue.cl` | `demo123` | Digitador |
