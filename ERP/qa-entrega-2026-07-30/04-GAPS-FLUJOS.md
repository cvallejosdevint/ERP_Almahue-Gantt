# Gaps flujos back+front — entrega

**Fecha:** 2026-07-30  
**Fuente:** [Gaps flujos](15c3d9ad-b8fe-438c-b2b9-0d9b9caf3108)

## Top 10 (orden de bloqueo)

| ID | Sev | Hallazgo |
|---|---|---|
| **GAP-05** | BLOQ | Calzar pago desde cartola no cierra ciclo: texto libre, sin FK, `terceroId`=nombre, no marca mov cartola |
| **GAP-02** | BLOQ | `EmitirDocumentoPage` wizard completo **sin ruta** en App/Sidebar |
| **GAP-07** | ALTO | Presupuestos: redirect a `/` + sin backend (`GET /presupuestos` 404) |
| **GAP-06** | ALTO | Aging/Nóminas: solo lectura; tabla nunca se puebla |
| **GAP-03** | ALTO | OC sin líneas de ítems (solo dist. CC) |
| **GAP-04** | ALTO | Registro compra sin líneas (monto global) |
| **GAP-08** | MEDIO | `ReportesEjecutivoPage` huérfana |
| **GAP-01** | MEDIO | Reglas Admin no preseleccionan jefe en OC (selección manual obligatoria) |
| **GAP-09** | BAJO | `WorkflowPage` legacy duplicado |
| DIFERIDO | — | GoSocket keys, cotización sin workflow, parsers banco |

## Flujos OK (happy path ya en TC)

- A Admin, B Parametrización, E Contratistas, F Insumos, G Contabilidad (asientos/centralización/periodos), C Ventas cabecera+líneas cotización, I GoSocket como stub documentado.

## Acción sugerida hoy (mínimo entrega)

1. **GAP-05:** al crear pago desde cartola → marcar mov como calzado/contabilizado + `proveedorId` real; default estado Pagado; ocultar “Calzar” si ya hay pago.
2. **GAP-02:** cablear `/comercial/emitir` **o** borrar/archivar wizard para no confundir QA.
3. Documentar GAP-03/04/06/07 como diferidos explícitos si no hay tiempo de implementar líneas OC/aging/presupuestos.
