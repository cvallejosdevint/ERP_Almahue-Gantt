# Prompt para Cursor — Análisis de dependencias Back↔Front ERP

Copia y pega este prompt en una **nueva conversación de Cursor** (modo Agent o Plan).

---

```markdown
# Rol
Actúa como ingeniero de software senior y jefe de proyecto técnico. Tu objetivo es analizar un proyecto ERP y producir un mapa de dependencias detallado entre backend y frontend, listo para importar a una carta Gantt.

# Contexto del proyecto
- **Producto:** ERP web v1 (6 meses, inicio 13/07/2026, fin ~09/01/2027)
- **Stack backend:** NestJS 10, TypeScript, Prisma 7, PostgreSQL 16, JWT + RBAC multi-tenant, Swagger `/api`
- **Stack frontend:** React 19, Vite 8, TypeScript, TanStack Query, react-router v7, Tailwind v4, axios, zod + react-hook-form
- **Infra:** Docker Compose, migraciones Prisma, despliegue nginx
- **Sin mobile** en v1
- **Referencia de patrones:** analiza `E:\source\repos\Almahue\almahue_back` y `E:\source\repos\Almahue\almahue_front` SOLO para inferir convenciones de arquitectura, no para copiar módulos de negocio
- **Artefactos existentes:** revisa `E:\source\repos\Almahue\docs\erp-planificacion\` (CSV, JSON, convenciones) y extiéndelos si corresponde

# Módulos ERP en alcance
1. Core (auth, multi-tenant, usuarios, roles, permisos)
2. Catálogos maestros transversales
3. Contabilidad / Finanzas
4. Inventario / Almacén
5. Compras / Proveedores
6. Ventas / CRM
7. Producción / MRP
8. RRHH / Nómina
9. Integraciones externas (SII/DTE, bancos)
10. Reportes / Dashboard / BI

# Instrucciones de análisis

## Paso 1 — Inventario de convenciones (desde código existente)
Analiza la estructura real de:
- Backend: `src/modules/`, `src/auth/`, `prisma/schema.prisma`, guards, DTOs, seeds
- Frontend: `src/features/`, `src/services/real/api.ts`, `src/services/http.ts`, `src/lib/permissions.ts`, `App.tsx` (rutas)

Documenta el **patrón repetible por módulo**:
- Qué artefactos crea el backend antes de que el frontend pueda consumirlo
- Qué artefactos crea el frontend y de qué endpoints depende
- Permisos RBAC necesarios por módulo
- Componentes compartidos reutilizables (DataTable, hooks catálogo, export Excel)

## Paso 2 — Descomposición atómica por módulo ERP
Para CADA módulo, genera tareas **atómicas y ejecutables** (no generalices). Separar siempre:
- `BACK-*` (schema Prisma, migración, service, controller, DTOs, permisos, seeds, tests)
- `FRONT-*` (types, API client, pages, forms, rutas, i18n, permisos UI)
- `INFRA-*` (Docker, CI, deploy)
- `QA-*` (e2e, UAT)

Cada tarea debe tener:
| Campo | Descripción |
|---|---|
| `id` | Identificador único (ej. CONT-B03) |
| `nombre` | Nombre accionable |
| `tipo` | back / front / infra / qa |
| `modulo` | Módulo ERP |
| `duracion_dias` | Estimación realista (1 persona) |
| `dependencias` | IDs de tareas predecessoras |
| `entregable` | Qué existe al terminar |
| `criterio_aceptacion` | Condición verificable |
| `paralelizable_con` | IDs que pueden correr en paralelo |
| `riesgo` | alto / medio / bajo |

## Paso 3 — Grafo de dependencias Back→Front
Reglas:
- El frontend **NO inicia** hasta endpoints REST + permisos + seeds mínimos del backend
- Identifica dependencias cross-módulo (Compras → Inventario + Contabilidad)
- Identifica cross-cutting (Auth primero; ContabilizacionService antes de contabilización automática)
- Spike SII/DTE (`INT-SII-SPIKE-01`) en semana 10, paralelo a Compras/Ventas

## Paso 4 — Secuenciación en 6 meses (26 semanas)
Fases:
- F0 Fundación (sem 1-4)
- F1 Contabilidad + Inventario (sem 5-9)
- F2 Compras + Ventas + spike SII (sem 10-14)
- F3 Producción + integración contable (sem 15-18)
- F4 RRHH + Integraciones (sem 19-22)
- F5 Reportes + QA + Go-live (sem 23-26)

Asigna fechas Lun-Vie desde **13/07/2026**. Equipo mínimo validado: **2 back + 2 front**.

## Paso 5 — Outputs requeridos

### A) CSV Gantt
`docs/erp-planificacion/erp_gantt_tareas.csv`

### B) JSON dependencias
`docs/erp-planificacion/erp_dependencias.json`

### C) Diagrama Mermaid flowchart de módulos

### D) Ruta crítica + cuellos de botella + recomendaciones de paralelización

# Reglas
- NO generalices tareas
- Responde en español
- Regenera con `python tools/generate_erp_gantt.py` tras cambios
```

---

## Uso

1. Ejecutar el prompt apuntando a los repos Almahue como referencia.
2. Importar `erp_gantt_tareas.csv` a Excel, ProjectLibre o Notion Timeline.
3. Comparar escenarios en `validacion_fechas.json` (1 dev vs 2 dev vs plan).
4. Re-ejecutar cuando existan repos `erp_back` / `erp_front`.
