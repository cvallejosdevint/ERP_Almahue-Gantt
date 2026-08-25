# Plan QA — tesorería ciclo OC/OV → libro → asiento → banco (21/08)

No reset BD. Tenant local: EMP-EXPORT (o EMP-1 en prod). Toggle **API real**. Periodo contable ABIERTO.

Password operadores `demo123`. Admin `admin@almahue.local` / `Admin123!`.

## Precondiciones

- Empresa con proveedor, cliente, insumo, periodo `2026-08` ABIERTO.
- Config SII / cuentas banco o fallback imputable (P0-1).
- Parser: CSV genérico o Excel Almahue-web. **SKIP** TES-004 Excel banco fino MJ (H13).

## Casos

| ID | Qué hacer | Esperado |
|---|---|---|
| TES-PRE-1 | OC no aprobada + factura en libro → POST pago | 400; no CC ni aging |
| TES-PRE-2 | OC APROBADO → contabilizar registro compra | Asiento COMPRA + CC haber proveedor + aging POR_PAGAR (neto+IVA) |
| TES-PRE-3 | Factura venta no CONTABILIZADA → cobro | 400 |
| TES-PRE-4 | Factura venta CONTABILIZADA → cobro | CC haber cliente + aging baja saldo |
| TES-CART-1 | Import CSV/Excel **completa** | Todas las líneas; `usuarioCarga` = sesión, no `demo` |
| TES-CART-2 | Alta cartola sin líneas | 400 / UI sin «nueva cartola» vacía |
| TES-CART-3 | Contabilizar TRX | Asiento `CARTOLA:{id}`; periodo cerrado = 400 |
| TES-CART-4 | Calzar egreso → pago; calzar ingreso → cobro | 1:1; segundo calce = 400 |
| TES-CART-5 | Pago **sin** cartola de factura contabilizada | CC+aging sí; **sin** asiento PAGO |
| TES-CART-6 | Cerrar cartola con pendiente o egreso sin calce | 400 |
| TES-CON-1 | Conciliación | Resumen pendientes/conciliados; no crear cabecera huérfana |
| TES-PAG-1 | Tipos PAGO_TOTAL / ANTICIPO / ANTICIPO_PRODUCTOR | Productor = flag + TC; `/tesoreria/anticipos` redirige |
| TES-NOM-1 | Nómina semanal POR_PAGAR | KPIs; aplazar mueve semana, no `fechaVencimiento` |
| TES-CAJ-1 | Flujo por banco + CLP/USD | Apertura no se recalcula; movimientos sí |
| TES-CC-1 | Estado de cuenta | Link abre pago/factura por id |
| TES-PERM-1 | Menú | Cartola primero; label = catálogo pantallas |

## Diferido (SKIP válido)

TES-004 H13 · R4-18 cobranza · SMTP · match automático RUT.
