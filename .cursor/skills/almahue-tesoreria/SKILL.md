---
name: almahue-tesoreria
description: Cartolas, conciliación, pagos, estado de cuenta y aging; parsers banco Almahue. Use when working on tesorería, cartolas, conciliación or flujo de caja.
---

# Tesorería Almahue

Módulo **existe**. Contrato ciclo: `docs/erp-planificacion/agrosoft-levantamiento/plan-tesoreria-ciclo-completo-2026-08-21.md`. Tesorería **no crea** la deuda; solo la liquida.

## Cerrado 21/08 (ciclo)

- Asiento banco = movimiento de cartola (`origen CARTOLA:{id}`). Periodo ABIERTO.
- Pago/cobro = calce + CC + aging. **No** asiento `PAGO:{id}` (ni con cartola ni sin ella).
- Al contabilizar compra/venta: CC + aging (neto+IVA).
- Gate: no pagar OC no operable; no cobrar factura no `CONTABILIZADA`.
- Cartola: solo import con líneas; `usuarioCarga` = email de sesión.
- `updatePago`: no edita calce/monto/contraparte.
- Conciliación: resumen de cartolas (R4-19). No alta huérfana.
- Pagos unificados: `PAGO_TOTAL` | `ANTICIPO` | `ANTICIPO_PRODUCTOR` (flag `esProductor` + TC). `/tesoreria/anticipos` redirige.
- Nómina: `semanaCompromiso` (aplazar no muta DTE). R4-17 vencimiento queda en aging.
- Flujo caja: banco + CLP/USD + apertura inmutable.
- Menú: cartola → conciliación → flujo → pagos → nómina → estado de cuenta.

## No inventar / diferido

- **Cobranza R4-18** (compromisos, mail, tracking).
- **SMTP** / H9.
- Match automático cartola↔factura (RUT+monto): calce **manual** 1:1.
- Parsers Chile/Estado/Santander sin muestra MJ (**H13**). Queda Almahue-web + CSV/Excel genérico.
- Maestro Productor.
- DTE real / SII live.

## Backlog master 28/08 (antes que el resto)

Fuente: `docs/.../reunion-2026-08-28-tesoreria-mj-lupe.md` + `pm-barco-almahue-2026-08-31.md` §3. Orden: **T2 → T1 → T6 → T5 → T3 → T4**.

- T2: **hecho (Fase 2).** Contabilizar 1:1 en cartola (contracuenta + destino + código financiero). Maestro `CodigoFinanciero` en Parametrización (catálogo vacío hasta que Almahue cargue). Lookup documento en tesorería; miss → mensaje Anticipo, sin cambio silencioso. Sin batch. Cerrar cartola: pago solo si destino factura/anticipo.
- T1: **hecho (local, sin merge).** `PagoTcEvento`; TC editable al crear/editar; `POST /pagos/:id/calzar-productor` si nació sin folio; `GET .../tc-eventos`. Cartola inmutable. No maestro Productor.
- T6: **hecho (local, sin merge).** Estado de cuenta por RUT (`GET /cuentas-corrientes/por-rut`); dual cliente+proveedor; pendiente/calzado; folio→libro; calce desplegable; multi-select informativo.
- T5: **hecho (local, sin merge).** UX año→mes→semana (default año actual, semanas futuras); título «Nómina semanal de pagos»; totalizadores semana vs mes; filtro pendientes/todos; export CSV/Excel. Aplazar sigue en `semanaCompromiso` (no muta DTE).
- T3: **hecho (local, sin merge).** Flujo solo lectura; filtro moneda CLP/USD/yuan nativo; nutrir desde cartola CONTABILIZADO + apertura inmutable; columna código financiero (T2). Eje nativo; equivalente CLP es T4 (opt-in).
- T4: **hecho (local, sin merge).** `tcDeFecha` (hábil anterior) en back/front; default TC BC al crear pago no productor (no pisa `ANTICIPO_PRODUCTOR`); flujo equivalente CLP opt-in (fecha vs “hoy” con pinzas, default OFF); sync CNY = yuan (no yen); import CSV/Excel + plantilla en Indicadores BC. Yuan 0 no pisa histórico. GET indicadores con `tesoreria:read` + `apiErrorMessage`.

Rule: `erp-tesoreria`. Integridad UI↔Prisma: `docs/auditoria-integridad-secundaria.md`.
