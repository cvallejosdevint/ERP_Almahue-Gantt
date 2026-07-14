# Ruta crítica — ERP v1 (6 meses)

Generado a partir de `erp_dependencias.json` (escenario plan: 2 back + 2 front).

## Secuencia crítica (cadena más larga)

```
INF-01 → INF-02 → INF-03 → CORE-B01 → CORE-B04 → CAT-B01
  → INV-B01 → INV-B02 → INV-B03 → INV-B04
  → COMP-B03 → COMP-B04 → COMP-B05
  → REP-B01 → REP-F01 → QA-01 → QA-02 → DEP-01 → DEP-02
```

**Duración calendario:** 13/07/2026 → 25/12/2026 (dentro del objetivo 09/01/2027).

## Cuellos de botella

| # | Tarea | Riesgo | Motivo |
|---|---|---|---|
| 1 | `INV-B03` | Alto | Kardex + movimientos; base de compras, ventas y producción |
| 2 | `VENT-B04` | Alto | Reserva stock + despacho; une inventario y ventas |
| 3 | `INT-CONT-01` | Alto | Contabilización cross-módulo |
| 4 | `INT-B02` | Alto | SII/DTE; depende del spike semana 10 |
| 5 | `CONT-B03` | Alto | Motor de asientos; prerequisito contable |

## Paralelización recomendada

| Paralelo A | Paralelo B | Fase |
|---|---|---|
| `CONT-B*` (back-1) | `INV-B*` (back-2) | F1 |
| `COMP-B*` (back-1) | `VENT-B*` (back-2) | F2 |
| `INT-SII-SPIKE-01` | `COMP-B03` / `VENT-B03` | F2 sem 10 |
| `PROD-B*` (back-1) | `INT-CONT-*` (back-2) | F3 |
| `RRHH-B*` (back-1) | `INT-B*` (back-2) | F4 |
| `COMP-F*` (front-1) | `VENT-F*` (front-2) | F2 |
| `CONT-F*` (front-1) | `INV-F*` (front-2) | F1 |

## Hitos

| Hito | Tarea disparadora | Fecha estimada |
|---|---|---|
| M-F0 | CAT-F02 | ~07/08/2026 |
| M-F1 | INV-F04 | ~11/09/2026 |
| M-F2 | VENT-F04 | ~16/10/2026 |
| M-F3 | INT-CONT-F01 | ~13/11/2026 |
| M-F4 | INT-F03 | ~11/12/2026 |
| M-F5 Go-live | DEP-02 | ~25/12/2026 |

Ver fechas exactas en `erp_dependencias.json` → `milestones`.

## Regla Back → Front

Para cada par del mismo módulo:

```
<MOD>-B{n}  ──►  <MOD>-F{n}
```

El front solo inicia cuando el back del que depende está terminado (ver columna `dependencias` en CSV).
