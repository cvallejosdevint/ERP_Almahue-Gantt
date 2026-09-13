# Reglas y skills del sistema (manifiesto)

**Fecha:** 2026-08-16 · Convenciones de código y UI del ERP Almahue. No incluye secretos ni `.env`.

Punto de entrada para agentes: [`AGENTS.md`](../AGENTS.md).

---

## 1. Idioma y requisitos

- Responder y documentar en **español**.  
- Filtrar siempre por **tenant** (`empresaId`).  
- Carlos/Sergio en reuniones = hipótesis. Verdad: Agustín / MJ, minutas Reu6→Reu5→Reu4, código + pruebas.  
- No leer `fuentes/transcripcion*.md` salvo pedido explícito. Limpieza local: skill `almahue-transcript-local`.  
- **No** existe el concepto de mermas en el negocio; no implementarlo ni documentarlo como excepción de venta.

---

## 2. Rules (`.cursor/rules`)

| Rule | Contenido |
|---|---|
| `almahue-core` | Español, tenant, no commit secretos, skills antes que transcripciones |
| `almahue-reuniones` | Contrastar demo vs minuta; no “ya está” sin código |
| `erp-backend` | Orden Nest; no mezclar workflows-admin con grupos/escalas |
| `erp-frontend` | Orden front; API real; Emitir ≠ cotización/NP/OC |
| `erp-prisma` | Solo `prisma/migrations/`; `grupoId` en nodos de escala |
| `erp-comercial` | Cotización Compras vs OV Ventas |
| `erp-tesoreria` | Cartolas/conciliación (si se toca tesorería) |

---

## 3. Skills de dominio

| Skill | Cuándo |
|---|---|
| `almahue-erp-contexto` | Orientación de repo, URLs, huecos |
| `almahue-modulo` | Nuevo módulo Nest/React |
| `almahue-comercial-inventario` | OV, cotización, stock, flete, lookup RUT |
| `almahue-aprobaciones` | Grupos, PIN, AdminConcepto, simulador |
| `almahue-billing-dte` | Stub; no SII real |
| `almahue-ficha-contraparte` | Bancos, contactos, despacho |
| `almahue-contabilidad` | Plan cuentas, inactivar vs borrar |
| `almahue-tesoreria` | Cartolas, aging |
| `almahue-pantallas-permisos` | Catálogo vs Sidebar |
| `almahue-qa-local` | Planes y runners |
| `almahue-deploy` | Host, seed, SSH |
| `almahue-demo-mode` | Fixtures del toggle demo |
| `almahue-transcript-local` | Ollama en `E:\Ollama`, modelos `E:\OllamaModels` |

Subagentes de revisión: `almahue-security`, `almahue-db`, `almahue-architecture`, `almahue-patterns`, `almahue-qa-runner`, `almahue-qa-reviewer`.

---

## 4. Convenciones de código (resumen)

**Backend**

1. Modelo Prisma + `empresaId` + `@@schema("erp")`  
2. Migración versionada  
3. DTO con class-validator  
4. Service filtra tenant  
5. Controller: `@ApiTags` + permisos  

**Frontend**

1. Tipos en `domain.ts`  
2. API axios real  
3. `ProtectedRoute` + permisos  
4. Listados con DataTable existente  
5. Al añadir pantalla: actualizar catálogo permisos (OV en Ventas; Cotizaciones en Compras)

**Prohibido en producto**

- Restaurar cotización → NP → factura  
- Usar `Insumo.stock` global como saldo de venta  
- Commit de `.env`, JWT, dumps, `ERP/.deploy/`  
- DDL solo en `prisma/sql/`

---

## 5. UI

- Estados con badges compartidos.  
- Empresa y periodo visibles en header.  
- Escritura implica lectura en la matriz de roles.  
- Copy en español de Chile, sin jerga de demo.
