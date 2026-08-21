# Cadena documental ERP Almahue (identificación)

Orden cronológico confirmado · actualizado 2026-08-21

## Timeline

| # | Etapa | Quién | Documentos |
|---|---|---|---|
| 1 | Toma de requerimientos (no equipo TI) | Marketing proveedor + marketing cliente | **Dos PDFs Enterprise** (ver abajo) |
| 2 | Planificación | Devint (tú) | **Carta Gantt** 6 meses |
| 3 | Primera reunión / demo Agrosoft | Cliente + Devint | Video 21/07 + tl;dv |
| 4 | Post-reunión 1 (IA + análisis) | Devint | Transcripción, planes Trello v1 + corrección, consolidación |
| 5 | Reunión 2 (contratistas AgroSmart, ventas, tesorería) | Cliente + Devint | Video 23/07 + tl;dv + capturas |
| 6 | Post-reunión 2 | Devint | Análisis, plan de acción, DEC-11…15 |

---

## 1) Dos documentos de requerimientos (marketing)

| Doc | Ubicación | Fecha approx. |
|---|---|---|
| **1a** ERP Contable-Financiero Enterprise | `C:\Users\c\Downloads\ERP-Contable-Financiero-Enterprise.pdf` | 2026-07-10 |
| **1b** Módulo Comercial Enterprise | `C:\Users\c\Downloads\Modulo-Comercial-Documento-Tecnico-Enterprise.pdf` | 2026-07-10 |

Cruce interno: `docs/erp-planificacion/validacion-pdf-enterprise.md`

### NO son estos (otros productos)

| Archivo | Por qué no |
|---|---|
| `MarketManager-Levantamiento-Funcional-v3.pdf` (raíz repo) | Producto hermano MarketManager |
| `Documentación API Export Manager China.pdf` (raíz repo) | Producto hermano Export Manager |
| `Pantallazos_primera_Versión_comentarios_Almahue.docx` (Downloads, ~06/07) | Feedback UI previo; no el par marketing Enterprise |

---

## 2) Carta Gantt (planificación Devint)

| Artefacto | Ubicación |
|---|---|
| PDF plan (versión reciente) | `C:\Users\c\Downloads\ERP Web - Planificación Estratégica (6 Meses).pdf` (~13/07) |
| PDF plan v1 | `C:\Users\c\Downloads\ERP v1 Web - Planificación Estratégica (6 Meses).pdf` (~10/07) |
| Fuente editable | `docs/erp-planificacion/erp_gantt_devint_6_meses.html` |
| Tareas | `docs/erp-planificacion/erp_gantt_tareas.csv` (+ variantes) |
| Generadores | `tools/generate_erp_gantt*.py` |

En Trello cliente: tarjeta **Carta Gantt** (En QA Almahue).

---

## 3) Primera reunión

| Artefacto | Ubicación |
|---|---|
| Video (en repo docs) | `fuentes/videos/reunion1-2026-07-21.mp4` |
| Video (origen) | `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-07-21 120114.mp4` |
| tl;dv | https://tldv.io/app/meetings/6a60394d4959970013159ad2 |

---

## 3b) Segunda reunión (23/07/2026)

| Artefacto | Ubicación |
|---|---|
| Video (en repo docs) | `fuentes/videos/reunion2-2026-07-23.mp4` |
| Video (origen) | `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-07-23 113533.mp4` |
| tl;dv | https://tldv.io/app/meetings/6a624d3ff324400013c736cb |
| Minuta tl;dv | `fuentes/reunion2-minuta-tldv-2026-07-23.md` |
| Análisis | `../reunion2-analisis-2026-07-23.md` |
| Plan de acción | `../plan-accion-post-reunion2-2026-07-23.md` |
| Capturas | `../pantallas-legacy/reunion2/` |

---

## 4) Documentos post-reunión 1

| Rol | Archivo |
|---|---|
| **Transcripción** | `agrosoft-levantamiento/fuentes/transcripcion.md` |
| **Plan Trello fase 1** (~70 cards) | Downloads `resumen.docx` ≡ `fuentes/resumen-trello-70.txt` |
| **Corrección del plan Trello** | Downloads `REPORTE DE AUDITORÍA DE CALIDAD.docx` ≡ `fuentes/auditoria-calidad.txt` |
| **Minuta / síntesis** (no hay Word “minuta”) | Más cercano: `consolidacion-tablero-2026-07-22.md` + `00-decisiones.md` + `preguntas-proxima-reunion.md` |
| Tablero depurado (derivado) | `trello-depurado.md` |
| Canónico módulos | `modulos/*.md` + `matriz-trazabilidad.csv` |

---

## Estado de identificación

| Afirmación | ¿Correcto? |
|---|---|
| Dos docs marketing = Enterprise Contable + Comercial | **Sí** |
| MarketManager + Export Manager = esos dos | **No** (otros productos) |
| Gantt = plan Devint previo a reunión Agrosoft | **Sí** |
| Tras reunión: transcripción + Trello v1 + auditoría | **Sí** |
| Existe un archivo literal “minuta.docx” | **No encontrado**; síntesis repartida en MD de consolidación/decisiones |

Si los dos docs de marketing fueran otros archivos, indicar nombres exactos para corregir este índice.

---

## 20/08/2026 — dos grabaciones distintas

| Cuándo | Quién | Docs |
|---|---|---|
| Mañana (~10:58) | Solo Carlos + Sergio (interna) | [`../reunion-2026-08-20-contraste-sergio.md`](../reunion-2026-08-20-contraste-sergio.md) · video `105836` |
| Tarde (~17:49, ~41 min) | Sergio, Lupe, Mario, Carlos | [`../reunion-2026-08-20-tarde-lupe-mario.md`](../reunion-2026-08-20-tarde-lupe-mario.md) · transcripción [`transcripcion-2026-08-20-tarde-lupe-mario.md`](transcripcion-2026-08-20-tarde-lupe-mario.md) · tl;dv [6a877e1e644c1a00131f8046](https://tldv.io/app/meetings/6a877e1e644c1a00131f8046) · video `174935` (~1,12 GB, no git) |

La de la tarde **no** es Reu7 y **no** pisa Reu6 (MJ/Agustín).
