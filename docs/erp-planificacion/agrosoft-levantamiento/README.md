# Levantamiento Agrosoft → ERP Almahue (canónico)

Documento de trabajo **auditado** a partir de las demos del **2026-07-21 (Reu 1)** y **2026-07-23 (Reu 2)**.

## Objetivo del cliente

> “Un Agrosoft pero versión 3.0” — replicar pantallas/flujos actuales corrigiendo fallas críticas, sin mano de obra (usan Book) y con gestión vía Power BI / AlmaWeb por ahora.

## Cómo usar (Cursor / Trello)

1. Leer `00-decisiones.md` antes de cualquier sprint.
2. Abrir el módulo en `modulos/0X-*.md`.
3. Ver captura en `pantallas-legacy/` referenciada.
4. Implementar solo ítems **REQ** / **DEC**. Lo **OPT** requiere OK del cliente.
5. Timestamps: columna `ts_tldv` en `matriz-trazabilidad.csv` (preferir sobre relojes del transcript).

## Etiquetas

| Tag | Significado |
|---|---|
| REQ | Obligatorio (dicho/mostrado) |
| DEC | Decisión estratégica |
| OPT | Mejora deseable |
| OUT | Fuera de v1 / sin evidencia suficiente |

## Estructura

```
agrosoft-levantamiento/
  README.md
  00-decisiones.md
  reunion2-analisis-2026-07-23.md
  plan-accion-post-reunion2-2026-07-23.md
  preguntas-proxima-reunion.md
  matriz-trazabilidad.csv
  trello-depurado.md
  compromiso-actualizacion-tablero-2026-07-22.md
  consolidacion-tablero-2026-07-22.md
  backups/   ← respaldos JSON del tablero Trello
  fuentes/
    videos/  ← mp4 reu1/reu2 (gitignore)
  pantallas-legacy/
    reunion2/  ← capturas video 23/07
  modulos/
```

**Última consolidación Trello:** 22/07/2026 — ver `consolidacion-tablero-2026-07-22.md`.  
**Post Reunión 2:** `reunion2-analisis-2026-07-23.md` + `plan-accion-post-reunion2-2026-07-23.md`.

## Relación con Gantt Enterprise

Ver [../README.md](../README.md). Este levantamiento detalla Contratistas / Compras / Insumos / Contabilidad / Permisos para las fases F2–F3.
