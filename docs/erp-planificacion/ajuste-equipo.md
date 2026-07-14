# Ajuste de duraciones por tamaño de equipo

Validación generada por `tools/generate_erp_gantt.py`.

## Esfuerzo total

| Métrica | Valor |
|---|---|
| Persona-día total | **329** |
| Ventana 6 meses (días hábiles) | **130** |
| Ratio necesario | ~2,5 FTE promedio |

## Escenarios

| Escenario | Archivo CSV | Fin estimado | ¿Cumple 09/01/2027? | Desviación |
|---|---|---|---|---|
| 1 dev fullstack | `erp_gantt_tareas_1dev.csv` | 14/10/2027 | No | +199 días hábiles |
| 2 devs (1 back + 1 front) | `erp_gantt_tareas_2dev.csv` | 20/04/2027 | No | +72 días hábiles |
| **Plan recomendado (2 back + 2 front)** | **`erp_gantt_tareas.csv`** | **25/12/2026** | **Sí** | 0 |

## Recomendación

Para cumplir el plazo de 6 meses con los 9 módulos ERP en alcance:

- **Mínimo:** 2 desarrolladores backend + 2 frontend (o 4 fullstack con tracks asignados).
- **Alternativa si solo hay 2 devs:** reducir alcance v1 (posponer Producción o RRHH) o extender a ~9 meses.

## Distribución sugerida (4 FTE)

| Rol | Track | Módulos |
|---|---|---|
| Back-1 | Contabilidad → Integración contable → Reportes financieros | CONT, INT-CONT, REP-B02 |
| Back-2 | Inventario → Compras/Ventas → Producción | INV, COMP, VENT, PROD |
| Front-1 | Core + Admin + Contabilidad + Compras UI | CORE, CAT, CONT-F, COMP-F |
| Front-2 | Inventario + Ventas + RRHH + Integraciones UI | INV-F, VENT-F, RRHH-F, INT-F |

## Regenerar escenarios

```bash
python tools/generate_erp_gantt.py
```

Resultados en `validacion_fechas.json`.
