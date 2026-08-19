> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md) + skill `almahue-contabilidad`. Motivo: levantamiento Reu1; no spec ERP actual.

# Módulo: Contabilidad

Centraliza plan de cuentas, auxiliares, elementos de costo, comprobantes, carga masiva, indicadores.

## Plan de cuentas

- **Timestamp:** 01:27:14–01:28:10+
- **Etiqueta:** REQ

### To-Be
- [REQ] Flags por cuenta: CC, área negocio, especie, variedad, elemento; “No imputable”.
- [REQ] Parametrización ER / estado situación financiera.

## Elementos de costo / rigidez por departamento

- **Timestamp:** ~01:32–01:35
- **Etiqueta:** REQ

### To-Be
- [REQ] Asociar CC/elementos por área/departamento (menos mezcla libre).
- [REQ] **Anular** uso de elemento sin borrar histórico (no solo eliminar).

## Honorarios / factores

- **Timestamp:** 01:37:07–01:38:01
- **Etiqueta:** REQ (historial) — reduce antigua tarjeta #70

### To-Be
- [REQ] Factor actual/anterior + fecha vigencia.
- [REQ] Historial: factor ant/nuevo, fecha, usuario.

## Carga masiva de comprobantes

- **Timestamp:** 01:39:53–01:45:19
- **Captura:** `../pantallas-legacy/14-carga-masiva.png`
- **Etiqueta:** REQ

### To-Be
- [REQ] Validar período, campos requeridos, cuadratura debe/haber, flags de cuenta.
- [REQ] Plantilla estándar estable (evitar errores por celda número→texto).
- [REQ] No “olvidar” archivos con error; feedback por línea.

## Indicadores financieros (Banco Central)

- **Timestamp:** 01:49:10–01:54:43
- **Captura:** `../pantallas-legacy/15-indicadores-bc.png`
- **Etiqueta:** REQ

### To-Be
- [REQ] Auto-actualización matutina BC (**DEC-06**).
- [REQ] Completar domingos/feriados (hoy faltan / hay que digitar).
- [REQ] Priorizar dólar/euro/yuan; no depender de UF/UTM/IPC (**DEC-05**).
- [REQ] Bloquear o advertir contabilización si falta TC del día.

## Cierre transversal

El timestamp de “cierre contabilidad” del resumen reutiliza el de contratistas; tratar cierre como capacidad transversal Admin, no pantalla inventada.
