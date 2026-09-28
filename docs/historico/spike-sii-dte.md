# Spike técnico SII/DTE — Semana 10

## Ubicación en la Gantt

| Campo | Valor |
|---|---|
| ID | `INT-SII-SPIKE-01` |
| Nombre | Spike SII/DTE: sandbox API, certificados, flujo emisión mock |
| Fase | F2 (Compras + Ventas) |
| **Semana 10** | **14/09/2026 → 16/09/2026** (lun–mié) |
| Duración | 3 días hábiles |
| Riesgo | **Alto** |

## Dependencias

- `VENT-B01` — Schema ventas/facturación debe existir
- `CORE-B03` — Auth/permisos operativos

## Paralelo con

- `COMP-B03` — Flujo OC en desarrollo
- `VENT-B03` — Cotizaciones → pedido

## Entregables del spike

1. Documento técnico: API SII certificación, certificado digital, ambiente maullin
2. POC backend: emisión DTE tipo 33 (factura) en ambiente certificación
3. Matriz de riesgos y estimación refinada para `INT-B02` (8 días)

## Criterio de aceptación

POC emite DTE tipo 33 aceptado en ambiente certificación SII (maullin).

## Flujo posterior

```
INT-SII-SPIKE-01  →  INT-B01 (módulo integraciones base)
                   →  INT-B02 (DTE producción, 8d)
                   →  INT-F02 (UI emisión DTE)
```

## Mitigación de riesgo

| Riesgo | Mitigación |
|---|---|
| Certificado digital demorado | Solicitar certificado en F0 (INF-07) |
| API SII inestable | Mock local + adapter pattern |
| Complejidad tributaria | Limitar v1 a DTE 33 y 61 (nota crédito) |
