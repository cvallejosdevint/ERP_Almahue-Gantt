---
name: almahue-qa-local
description: QA local del ERP Almahue (operadores, cadenas, comercial, tesorería, DTE/billing-gateway). Use when testing locally, writing test plans, retesting after deploy, or invoking almahue-qa-runner / almahue-qa-reviewer.
---

# QA local

## Entorno

- Front `http://localhost:5174` · API `http://localhost:3001/api/v1` · Postgres `localhost:5433`
- Sesión: `localStorage['erp.session']`. AdminConcepto: **re-login** tras tocar grupos.
- **Roles en QA desde cero:** el superadmin no ejecuta OC/OV/cobros ni cierra la cadena. Prepara usuarios, catálogos y grupos. Los procesos van en el **front** con operadores (N1 + Laura Soto como final). Superadmin aparte: solo que **puede intervenir** sin estar en la escala. Arranque: `npm run reset:superadmin` + `npm run seed:qa-desde-cero`. **No** `npm run seed` ni `seed:aprobaciones-f2`. Método: `qa/resultados/2026-08-18-ciclo-desde-cero-metodo.md`.
- **Holding GoSocket QA (dos RUT reales):** `npm run seed:qa-holding` → `EMP-EXPORT` (`77.032.638-9` ALMAHUE EXPORT SPA) y `EMP-SERVICES` (`77.032.639-7` ALM SERVICES SPA), operadores disjuntos y organigramas distintos. Método: `qa/resultados/2026-08-19-holding-almahue-metodo.md`. Skill aprobaciones → `reference.md` sección C.
- Cadenas de prueba: tope N1 **$500.000**. Caso 1 nivel (monto ≤ tope) y 2 niveles (monto > tope → Laura). Rechazo en N1 y en N2. El final **no** es admin. **Prohibido SKIP por tiempo** de Ventas/CTR/tesorería.
- **Antes de QA:** levantar stack. Docker Desktop suele no estar en PATH. Postgres Windows: servicio `postgresql-x64-18` (puerto 5433) o `pg_ctl start -D "C:\Program Files\PostgreSQL\18\data"`. Luego `npx prisma migrate deploy`, Nest `npm run start:dev` (`ERP/erp_back`), Vite `npm run dev` (`ERP/erp_front`). Health debe ser `db=ok`. No SKIP/BLOCKED de UI por puertos caídos sin haber intentado arrancar.
- Evidencia código/Jest solo si el arranque **falló** (permisos, PG ausente). Eso no es FAIL de producto.

Plan canónico aprobaciones (seed-f2 / Jorge): `qa/PLAN-PRUEBAS-APROBACIONES.md`  
Integral: `qa/PLAN-PRUEBAS-INTEGRAL-ERP-v2-2026-08-15.md`  
Operadores EMP-BOOT: `qa/resultados/2026-08-19-ciclo-panorama-completo.md` + review.  
Inventario docs: `qa/resultados/2026-08-18-ciclo-0-inventario-docs.md` (no existe `ciclo-0-mapa-modulos.md`).  
Emisión OC: `qa/resultados/2026-08-17-p0-emision-registro.md` (el as-is 14/08 está `{deprecado}`).

## Deuda conocida — no FAIL de producto

No reabrir como gap: cadena OV (D4), Emitir solo FACTURA/NC/ND/GUIA, D16 bloqueo bajo costo **sin** flag/UI de empresa, catálogo vs Sidebar (D11), Libro de compras montaje (fix 19/08), Emitir-desde-OV sin exigir cuenta en piloto.

Sigue vigente:

- DTE: HTTP ERP→`billing-gateway`→GoSocket sandbox existe. Sin CAF/cert MJ = rechazo fail-closed (no FAIL). SII live = SKIP (BIL-007). Stub inline solo si `BILLING_STUB_INLINE=true`.
- `workflows-admin` legacy aún en API/UI (no mezclar con grupos/escalas)
- H14 prod: no asumir migrate stock/OV/`piloto_on`
- H9 SMTP correo PIN
- Cobranza R4-18 (propuesta, no módulo)
- FLETE canonical DTE no auditado
- Productor no es maestro (flag lookup sí)
- Recepción OC no mueve stock
- H13 Excel banco fino (parser Almahue-web sí parsea cartola MJ en Jest)
- TES-CARTOLA-IMP: file picker no automatizable (prueba manual)
- OV rechazada vuelve a **BORRADOR** (no `RECHAZADO` de OC); es diseño, no FAIL

## Cómo ejecutar

1. Levantar stack (arriba). Health `db=ok` + front 200.
2. Subagente `almahue-qa-runner` sigue el plan (no arregla producto).
3. Escribe resultado en `qa/resultados/` **sin JWT**.
4. Subagente `almahue-qa-reviewer` clasifica defectos vs gaps conocidos.

## Additional resources

- Seed demo EMP-1 (Jorge) vs QA EMP-BOOT (Laura): skill `almahue-aprobaciones` → `reference.md`
- Plantilla: `qa/resultados/PLANTILLA.md`
