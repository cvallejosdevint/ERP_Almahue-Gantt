# Matriz casos — marzo 2026 (Contratistas, Insumos, Compras, Contabilidad)

Periodo **`2026-03`** · Empresa **`EMP-EXPORT`** · DTE reales vía pedido [`PEDIDO-EMISIONES-DTE-MARZO-2026.md`](./PEDIDO-EMISIONES-DTE-MARZO-2026.md)

## A. Parametrización y apertura

| # | Caso | Modulo | Evidencia |
|---|------|--------|-----------|
| A1 | Periodo contable 2026-03 ABIERTO | Contabilidad | Admin periodos |
| A2 | Cierre Contratistas 2026-03 ABIERTO (sin asiento) | Contratistas | Traspaso / periodo |
| A3 | Cuentas cierre CTR + cuentas imputación OC/proforma | Admin Empresas | IDs debe/haber |
| A4 | Bodegas e insumos con stock inicial | Insumos | Stock por bodega |

## B. Insumos y Compras (calce DTE)

| # | Caso | Documento ERP | DTE esperado |
|---|------|---------------|--------------|
| B1 | OC pendiente aprobación | OC-2026-MAR-003 | (ninguno aún) |
| B2 | OC aprobada + guía + factura insumos | OC-2026-MAR-001 | BIL-MAR-02 guía + BIL-MAR-03 factura |
| B3 | Segunda OC guía + factura | OC-2026-MAR-002 | BIL-MAR-04 + BIL-MAR-05 |
| B4 | Recepción / movimiento ENTRADA_PROVEEDOR | Mov. bodega MAR | Match 3 vías |
| B5 | Registro libro compras + contabilizar | REG-MAR26-* | Asiento compras |
| B6 | Factura intercompany servicios | REG-MAR26-INTERCO-001 | BIL-MAR-01 |
| B7 | Factura exenta compras | REG-MAR26-EXENTA-001 | BIL-MAR-07 |
| B8 | NC compras (ref OC-001) | Libro compras | BIL-MAR-08 |
| B9 | ND compras (ref proforma) | Libro compras | BIL-MAR-09 |

## C. Contratistas

| # | Caso | Documento | Notas |
|---|------|-----------|-------|
| C1 | Ingresos labor marzo | IngresoLaborDiario | Tarifa / CC |
| C2 | Proforma definitiva sin notificar | PF-MAR26-002 | Modificaciones |
| C3 | Proforma notificada | PF-MAR26-001 | Asociar factura post DTE **BIL-MAR-06** (`REG-MAR26-CTR-001`) |
| C4 | Traspaso + cierre periodo | 2026-03 | Ver asiento traspaso |
| C5 | Reversa / solicitud (opcional feb cerrado) | Protocolo 2x2 | Solo si repetimos cierre |

## D. Ventas (emisión ERP Export, no chat ALM)

| # | Caso | Documento | DTE |
|---|------|-----------|-----|
| D1 | OV confirmada stock | OV-MAR26-001 | Emitir factura 33 local |
| D2 | Guía despacho venta | Libro ventas | Emitir guía 52 local |
| D3 | Contabilizar factura venta | Libro ventas | Asiento |
| D4 | NC / ND venta | Libro ventas | Emitir 61/56 local |

## E. Contabilidad y tesorería (post-DTE)

| # | Caso |
|---|------|
| E1 | Centralización compras / ventas |
| E2 | CC + aging al contabilizar |
| E3 | Pago proveedor calzado (opcional) |
| E4 | Cierre contable 2026-03 (al final del ciclo) |

## Datos sembrados

```bash
cd ERP/erp_back
npm run clean:solicitudes-export
npm run regularize:local-proforma-export   # enum + PF-00001 oct (baseline)
npm run seed:marzo-2026-export
```

Referencia octubre (`PF-00001` / `2026-10` cerrado) queda para prueba reversa aparte.
