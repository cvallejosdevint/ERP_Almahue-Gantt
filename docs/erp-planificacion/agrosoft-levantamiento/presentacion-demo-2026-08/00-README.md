> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`qa/DEMO-PROPUESTA-LOCAL.md`](../qa/DEMO-PROPUESTA-LOCAL.md). Motivo: guion con «Ventas › Cotizaciones / NP» (D11 invertido).

# Presentación demo Almahue ERP (2026-08)

| Archivo | Contenido |
|---|---|
| [`00-PRESENTACION-Y-FAQ.md`](./00-PRESENTACION-Y-FAQ.md) | **Parte A:** guion/speech del flujo completo (sin bodega/inventario; con aprobaciones). **Parte B:** FAQ por módulo/página (campos, significado, origen). |

**Fuera de alcance en esta presentación:** Insumos / Bodega / Inventario y derivados (acuerdo MJ).

**Nota de navegación:** las **Notas de pedido (NP)** no tienen ítem propio en el menú; viven en **Ventas › Cotizaciones / NP** (pestañas junto al título en `/comercial/cotizaciones`).

## Prep ambiente (antes de la reunión)

```bash
cd ERP/erp_back
npx prisma migrate reset --force   # o: npx prisma db seed
```

| Dato | Valor |
|---|---|
| Login | `admin@almahue.local` / `Admin123!` (email; sin username en UI) |
| PIN aprobación | `4821` (seed en Admin) |
| Empresa | Almahue SpA |
| Periodo | **2026-08 ABIERTO** (2026-07 queda CERRADO para contraste) |
| Modo | Real (API/BD) |
| Front / API | `:5174` / `:3001` |

El seed (`prisma/seed.ts` + `prisma/seed-demo-showcase.ts`) deja **datos y estados** en cada pantalla del guion. Validar conteos:

```bash
npx ts-node -r tsconfig-paths/register scripts/validate-demo-counts.ts
```

## SSO Microsoft (pruebas locales)

Ver guía: [`01-SSO-MICROSOFT-LOCAL.md`](./01-SSO-MICROSOFT-LOCAL.md).

Login dual: **clave ERP** (sigue igual) + **Iniciar con Microsoft** (cuando `MICROSOFT_AUTH_ENABLED=true` en `erp_back`).
