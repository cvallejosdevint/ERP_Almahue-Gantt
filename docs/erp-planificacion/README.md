# ERP v1 — Carta Gantt y dependencias

Planificación de 6 meses (inicio **lunes 13/07/2026**, go-live objetivo **09/01/2027**).

## Metodología v3 (Enterprise PDF)

| Fase | Enfoque | Alineación doc cliente |
|---|---|---|
| **F0** | Definiciones | Revisión PDFs + acta alcance + ERD + OpenAPI `/api/v1` |
| **F1** | Mockups + Feedback | Libro comercial, GoSocket, workflow, core financiero |
| **F2–F7** | Implementación | CORR → BACK → FRONT por módulo |

**Alcance v1 (PDF Enterprise):** Admin, Catálogos, Contabilidad, Tesorería, Presupuestos, Contratistas/Insumos, Comercial, Workflow, GoSocket, Reportes.

**Fuera de v1:** Producción, RRHH (fase 2), integración SII directa (usa GoSocket).

## Levantamiento Agrosoft (jul-2026)

Detalle funcional auditado de la demo del sistema actual (**Agrosoft 3.0** a reemplazar):

→ [`agrosoft-levantamiento/README.md`](agrosoft-levantamiento/README.md)

Incluye decisiones DEC, módulos canónicos (Contratistas / Compras / Insumos / Contabilidad / Permisos), matriz de trazabilidad con timestamps tl;dv, capturas legacy del video y pauta Trello depurada. Usar como backlog de pantallas para F2–F3; la Gantt de abajo sigue siendo el calendario.

Fuente de tareas: `tools/erp_gantt_tasks.py`

| Archivo | Descripción |
|---|---|
| [`erp_gantt_tareas.csv`](erp_gantt_tareas.csv) | **Gantt principal** — escenario plan (2 back + 2 front) |
| [`erp_gantt_tareas_1dev.csv`](erp_gantt_tareas_1dev.csv) | Escenario 1 dev fullstack |
| [`erp_gantt_tareas_2dev.csv`](erp_gantt_tareas_2dev.csv) | Escenario 2 devs (1 back + 1 front) |
| [`erp_dependencias.json`](erp_dependencias.json) | Tareas + ruta crítica + hitos (JSON) |
| [`validacion_fechas.json`](validacion_fechas.json) | Comparativa de escenarios por equipo |
| [`erp_gantt_devint_6_meses.html`](erp_gantt_devint_6_meses.html) | **Gantt visual HTML** (estilo Devint, 4 pestañas) |
| [`erp_gantt_6_meses.html`](erp_gantt_6_meses.html) | Alias del HTML anterior |

Fuente de tareas: `tools/erp_gantt_tasks.py`

## Regenerar

Desde la **raíz del repo** (`E:\source\repos\Almahue`):

```bash
python tools/generate_erp_gantt.py
python tools/generate_erp_gantt_html.py
```

## Gantt HTML (estilo Devint)

Abrir en navegador: [`erp_gantt_devint_6_meses.html`](erp_gantt_devint_6_meses.html)

- **4 pestañas:** Total · Definiciones · Mockups & Feedback · Implementación
- **26 semanas** (S1–S26) agrupadas en 6 meses
- Colores: Def · Mock · Feedback · CORR · Back · Front · QA
- Export: Copiar Excel, PDF (pestaña), PDF Total, Imprimir PDF (A3)
- Copia en `Desktop/erp_gantt_devint_6_meses.html`

## Fases v2

| Fase | Contenido |
|---|---|
| F0 | Definiciones Enterprise (PDFs, alcance, ERD, API v1) |
| F1 | Mockups: comercial, GoSocket, workflow, financiero |
| F2 | Core + Catálogos |
| F3 | Contabilidad + Tesorería + Presupuestos + Insumos |
| F4 | Comercial + Workflow + spike GoSocket |
| F5 | Contabilización automática |
| F6 | GoSocket DTE producción |
| F7 | Dashboard, QA, Go-live |

## Validación de fechas (escenario plan 2 back + 2 front)

| Escenario | Fin | ¿Dentro de plazo? |
|---|---|---|
| Plan (2 back + 2 front) | ~11/01/2027 | +1 día vs objetivo |
| 2 devs back+front | ~26/04/2027 | No |
| 1 dev fullstack | ~30/07/2027 | No |

## Tareas totales

**76 tareas** (275 persona-día) — alcance Enterprise v1.
