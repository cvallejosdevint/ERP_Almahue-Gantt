# Informe ejecutivo - cierre mes contable interempresa octubre 2026

Fecha informe: 02/11/2026. Simulacion EXPORT ↔ SERVICES. Periodo `2026-10` **CERRADO** en ambas empresas.

## Empresas

| Empresa | ID | RUT |
|---------|----|-----|
| ALMAHUE EXPORT SPA | EMP-EXPORT | 77.032.638-9 |
| ALM SERVICES SPA | EMP-SERVICES | 77.032.639-7 |

## Caso que cierra el mes (packing CLP)

| Paso | EXPORT | SERVICES |
|------|--------|----------|
| OC | OC-2026-0016 APROBADO $12.500.000 | - |
| OV | - | 10016881 CONFIRMADA |
| DTE 33 | Libro compras folio SII **73**, Match Perfecto, Aceptado | Folio SII **73** / interno `100168781372`, Contabilizada, SII ACE |
| Asiento compra/venta | 20260011 COMPRA:73 | 20260002 venta |
| Cartola | Pago $14.875.000 asiento **20260012** | Cobro asiento **20260003** |
| CC | Compra+pago Calzado (fecha fiscal 12-10) | Venta+cobro Calzado |

## Balance al cierre

| Tenant | Sumas Debe = Haber | Resultado KPI |
|--------|--------------------|---------------|
| EXPORT | $53.020.890 | Perdida ejercicio (incl. gasto packing + CTR) |
| SERVICES | $29.869.000 | Utilidad $12.600.000 |

## Otros asientos EXPORT relevantes

- **20260013** TRASPASO-CTR:2026-10 $7.600.000 (PF-00001 Servicios Agricolas del Valle)
- Cluster rechazo dejado como ejemplo: 33/#71, NC 61/#51, 33/#72, 34/#51 (ver fase3)

## Fiscal / GoSocket (sandbox)

| Doc | Emisor | Folio SII | Resultado |
|-----|--------|-----------|-----------|
| 33 packing | SERVICES | 73 | ACE / Contabilizada / cobrada |
| 34 asesoria | SERVICES | 52 | Comercial Perfecto en EXPORT; **SII RCH** en emisor (sin cobro) |
| 52 guia | EXPORT | 54 | Emitida; sync guias recibidas SERVICES |

## Gaps corregidos en la tanda (codigo)

F4-01 lookup folioOficial · F4-02 banco label · F4-03 fecha CC fiscal · F4-04 flujo `incluirProyecciones` · F4-05 tipoRef/auxiliar en asientos compra/cartola.

## Capturas clave

- Periodos cerrado: `capturas/mes-contable-dia31-periodos-export-cerrado.png`, `...-services-cerrado.png`
- Balance: `capturas/mes-contable-dia31-balance-8col-export-post-cierre.png`, `...-services-post-cierre.png`
- Cartolas / CC / DTE: ver `docs/qa/resultados/2026-11-02-fase*.md`

## Documentacion

- Manual con capturas: [`MANUAL-USUARIO-ERP-ALMAHUE.html`](MANUAL-USUARIO-ERP-ALMAHUE.html)
- FAQs: [`faqs.html`](faqs.html)
