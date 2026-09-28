# Plan QA — tesorería T1–T6 (28/08) + ciclo 21/08

Fecha: 2026-09-02. Complementa `PLAN-PRUEBAS-TESORERIA-CICLO-2026-08-21.md`.  
Master: `reunion-2026-08-28-tesoreria-mj-lupe.md` + `pm-barco-almahue-2026-08-31.md` §3.  
Orden de tarjetas: **T2 → T1 → T6 → T5 → T3 → T4**. T7 = operativo (no caso de código).

No reset BD. **No** `prisma migrate deploy`. Tenant `EMP-EXPORT`. Toggle **API real**. Periodo del banner (junio 2026 ABIERTO o el ABIERTO que esté). Admin `admin@almahue.local` / `Admin123!`. Operadores `demo123` si hace falta cadena OC.

## Precondiciones

- Health API `db=ok` · front 200 en `5174`.
- Productor holding: `PROV-EX-PROD` Agricola Los Naranjos (`76.210.103-3`) `esProductor=true`. **No** usar Insumos Packing Sur como productor.
- Códigos financieros: ejemplos Reu en Parametrización (catálogo Agrosoft completo = SKIP, no FAIL).
- Indicadores BC: si USD del día es 0 o falta, el campo TC puede quedar vacío (correcto).

## No FAIL (deuda / diseño)

- P0-1 asiento libro sin cuenta imputable.
- Match automático cartola↔factura.
- Maestro Productor (flag sí).
- Asiento `PAGO:{id}` (no debe existir).
- Cadena OV / D11 cotiz / D16 / SII live.
- Tabs calendario (propuesta Carlos).
- File picker cartola no automatizable → import por API o SKIP `TES-CARTOLA-IMP`.
- Anular/reversar pago (no hay API; no es T1–T6).
- Calce 1 anticipo ↔ N facturas.
- R4-25 catálogo Agrosoft (combo existe; maestro lo carga Almahue).
- Aging 90 días ≠ T5.
- H13 parsers banco fino.

## Casos ciclo 21/08 (retest)

Ejecutar IDs del plan 21/08: TES-PRE-1…4, TES-CART-1…6, TES-CON-1, TES-PAG-1, TES-NOM-1, TES-CAJ-1, TES-CC-1, TES-PERM-1.  
SKIP válidos: TES-004, R4-18, SMTP, match auto.

Notas de retest vs 21/08:

- TES-PRE-2: si P0-1 sigue, **BLOCKED** (deuda), no FAIL tesorería.
- TES-PAG-1: ahora sí hay `PROV-EX-PROD`. Camino feliz `ANTICIPO_PRODUCTOR` + TC. Packing Sur + tipo productor = 400 / combo vacío.

## Casos T2 — cartola contabilizar 1:1

| ID | Qué hacer | Esperado |
|---|---|---|
| T2-1 | Abrir cartola / importar (API si no hay picker) | Modal grande (`full`); no cap 50 filas; banco/moneda por hoja si Excel multi-hoja |
| T2-2 | Contabilizar 1 movimiento: contracuenta + destino + código financiero | Asiento `CARTOLA:{id}`; Ingreso = debe banco; Egreso = haber banco; 1:1 |
| T2-3 | Lookup folio existente | Asocia documento; no cambia a Anticipo |
| T2-4 | Lookup miss | Mensaje Anticipo; no cambio silencioso de destino |
| T2-5 | Segundo contabilizar / calce del mismo mov | 400 |
| T2-6 | Cerrar con pendiente o egreso sin calce factura/anticipo | 400 |

## Casos T1 — TC productor + auditoría

| ID | Qué hacer | Esperado |
|---|---|---|
| T1-1 | Nuevo pago CLP + factura CLP, no productor | Campo TC y diferencia TC **ocultos** |
| T1-2 | Pago o factura USD/CNY/EUR | TC visible; sugiere BC de la **fecha del pago** (hábil anterior). Si indicador 0/ausente → vacío, no placeholder inventado |
| T1-3 | Tipo Anticipo productor | Combo solo `esProductor`; Packing Sur no aparece / 400 claro |
| T1-4 | `ANTICIPO_PRODUCTOR` + `PROV-EX-PROD` + TC | 201; historial `GET /pagos/:id/tc-eventos` ≥1 |
| T1-5 | Editar TC del mismo pago | Nuevo evento en historial; PUT **no** cambia calce/monto/contraparte |
| T1-6 | `POST /pagos/:id/calzar-productor` si nació sin folio | 201 primera vez; 400 si ya había calce; no muta monto de cartola |

## Casos T6 — estado de cuenta por RUT

| ID | Qué hacer | Esperado |
|---|---|---|
| T6-1 | GET `/cuentas-corrientes/por-rut` + UI | Agrupa por RUT; **sin** eje cliente\|proveedor |
| T6-2 | Detalle de un RUT | Pendiente/calzado; calce desplegable; link folio → libro / pago |
| T6-3 | Dual (mismo RUT en cliente y proveedor) | API suma ambos; si no hay dual en BD, anotar entorno no FAIL |

## Casos T5 — nómina semanal

| ID | Qué hacer | Esperado |
|---|---|---|
| T5-1 | `/tesoreria/nominas` | Título «Nómina semanal de pagos»; selector año→mes→semana (futuras) |
| T5-2 | KPIs | Semana vs mes; filtro pendientes/todos |
| T5-3 | Export | CSV y/o Excel baja |
| T5-4 | Aplazar | Cambia `semanaCompromiso`; `fechaVencimiento` intacta |

## Casos T3 — flujo de caja

| ID | Qué hacer | Esperado |
|---|---|---|
| T3-1 | `/tesoreria/flujo-caja` | Solo lectura de movimientos; chips CLP/USD/Yuan nativos |
| T3-2 | Fuente | Aperturas + cartola **CONTABILIZADO**; columna código financiero si hay T2 |
| T3-3 | Apertura | Inmutable (PUT 400); botón requiere `tesoreria:write` |
| T3-4 | Equivalente CLP | Opt-in T4, default **OFF** (no convertir contabilidad) |

## Casos T4 — triple moneda / BC

| ID | Qué hacer | Esperado |
|---|---|---|
| T4-1 | `tcDeFecha` (API o UI fecha no hábil) | Usa hábil anterior; yuan = CNY ≠ yen |
| T4-2 | Crear pago no productor con moneda extranjera | Default TC BC; no pisa anticipo productor |
| T4-3 | Import indicadores BC CSV/Excel + plantilla | Carga filas; Yuan 0 no pisa histórico |
| T4-4 | GET indicadores | Visible con `tesoreria:read`; error de API no traga JWT |

## Informe

Escribir `qa/resultados/2026-09-02-tesoreria-t1-t6.md` (plantilla `qa/resultados/PLANTILLA.md`). Sin JWT. Jest `tesoreria` / `tipo-cambio` / `catalogos` si se corre, anexo aparte (no mezclar conteo UI).
