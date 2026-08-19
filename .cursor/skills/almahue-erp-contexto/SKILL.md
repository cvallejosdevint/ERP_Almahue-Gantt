---
name: almahue-erp-contexto
description: Contexto compacto del ERP Almahue (stack, paths, tenant, docs canónicas, URLs). Use when starting a new Almahue/ERP chat, planning sprints, or locating code vs documentation.
---

# ERP Almahue — contexto

## Stack

| Capa | Tech |
|---|---|
| Back | NestJS 10, Prisma 7, PostgreSQL 16+ (local a menudo 18 en `:5433`), JWT + RBAC |
| Front | React 19, Vite 8, TanStack Query, Tailwind 4 |
| Tenant | `empresaId` en modelos y queries |

Código: `ERP/erp_back`, `ERP/erp_front`. Docs: `docs/erp-planificacion/agrosoft-levantamiento/`.

## Prioridad de decisiones

**Reu6** > Reu5 > Reu4. No leer `fuentes/transcripcion*.md` a menos que el usuario lo pida.

Carlos/Sergio en reuniones = hipótesis. Requisitos = Agustín/MJ + minuta + código (rule `almahue-reuniones`).

Minutas: `reunion6-minuta-2026-08-06.md`, `reunion5-minuta-2026-08-03.md`, `reunion4-minuta-2026-07-30.md`.

## Auth / permisos

- Guards globales JWT + `@RequirePermissions('modulo:read'|'modulo:write')`
- AdminConcepto: JWT `adminConceptoModulos[]` — **re-login** tras asignar
- Config aprobaciones: `@RequireAprobacionesConfig('read'|'write')` (no solo `admin:*`)

## Entornos

- Local: front `5174`, API `3001`, Postgres a menudo `5433`
- Prod: `http://45.7.229.46/almahue-erp/` — SSH alias `erp-deploy` vía `ERP/.deploy/` (gitignored)

## Documentos (Reu6)

- Compras › Cotizaciones → proveedor → OC. Ventas › Orden de venta → cliente → stock → factura.
- Skill: `almahue-comercial-inventario`.

## Huecos de producto (no greenfield)

- Tesorería y contabilidad: módulos en código; smoke UI live 19/08 (EMP-BOOT) PASS. Demo cliente / «oficial SII» no cerrados.
- DTE: cliente HTTP a `billing-gateway` cuando `BILLING_GATEWAY_ENABLED=true` y `BILLING_STUB_INLINE=false`. Stub inline solo si ambos flags true. Sin CAF/cert en portal GoSocket QA el partner rechaza (fail-closed). **No** emisión SII live. Skill `almahue-billing-dte`.
- Aprobación: **sí cubre OV** si `comercialRequiereAprobacion` (piloto ON, migración `20260818180000`). Factura desde OV autorizada: sin segunda cadena. Admin **no** es nodo de escala.
- Skill comercial: `almahue-comercial-inventario`. Corte docs: inventario `qa/resultados/2026-08-18-ciclo-0-inventario-docs.md` (el as-is 14/08 está `{deprecado}`).
- Siguen: H14 prod, SMTP, cobranza R4-18, `workflows-admin` legacy, FLETE canonical, productor no maestro, recepción OC no mueve stock.

## Additional resources

- Minutas e inventario: [reference.md](reference.md)
- Convenciones de módulo: skill `almahue-modulo`
