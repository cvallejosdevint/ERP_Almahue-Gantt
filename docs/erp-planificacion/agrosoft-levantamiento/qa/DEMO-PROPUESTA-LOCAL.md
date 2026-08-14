# Demo local — flujo OC/OV Almahue + emisión stub

**Uso:** reunión / demo con MJ y Agustín **sin** GoSocket ni billing-gateway levantado.

---

## 1. Migraciones

```bash
cd ERP/erp_back
npx prisma migrate deploy
```

---

## 2. Variables `.env` (API)

```env
BILLING_GATEWAY_ENABLED=true
BILLING_STUB_INLINE=true
```

---

## 3. Seed demo

```bash
cd ERP/erp_back
npm run seed
```

Por defecto `SEED_DEMO_PROPUESTA=true` (desactivar con `SEED_DEMO_PROPUESTA=false`).

### Maestros Almahue (EMP-1)

| Tipo | IDs / detalle |
|------|----------------|
| **Bodegas** | `BOD-ALM-FRIG` Frigorífico · `BOD-ALM-PACK` Packing · `BOD-ALM-MAT` Materiales · `BOD-ALM-DESP` Despacho |
| **Insumos** | `INS-ALM-CEREZA` cereza 5 kg · `INS-ALM-CAJA` cajas · `INS-SEED-1` urea · `INS-ALM-PALLET` pallets |
| **Proveedores** | `PROV-SEED-1` Agro Insumos Sur · `PROV-SEED-2` Packaging Chile · `PROV-ALM-QUIM` Química del Valle |
| **Clientes** | `CLI-SEED-1` Exportadora Frutas del Sur · `CLI-SEED-1B` Packing Centro (productor) |

Stock inicial: cereza en frigorífico/despacho, cajas y urea en materiales, pallets en packing.

### Compras (cadena ALM-*)

| Folio | Estado | Notas |
|-------|--------|-------|
| `ALM-COT-001` | Cotización emitida | Packaging Chile — cajas |
| `ALM-COT-002` | Cotización borrador | Agro Insumos — fertilizante |
| `ALM-OC-001` | OC emitida · aprobación **pendiente** | Urea $2,5M |
| `ALM-OC-002` | OC **aprobada** · recepción borrador | Cajas $2,1M |
| `ALM-OC-003` | OC **recepcionada** · registro contabilizado | Urea + movimiento bodega |

Además: showcase legacy `OC-2026-001`…`004` (variedad de estados).

### Ventas (cadena ALM-*)

| Folio | Estado | Notas |
|-------|--------|-------|
| `ALM-OV-001` | Borrador | Bajo umbral $500k |
| `ALM-OV-002` | Pendiente aprobación | Cereza + flete · paso 1 bandeja |
| `ALM-OV-003` | Autorizada | Listo «Confirmar stock» |
| `ALM-OV-004` | Aprobado (stock confirmado) | Salida `SALIDA_VENTA` frigorífico |
| `ALM-FAC-101` | Factura borrador | Desde OV-004 → contabilizar = stub DTE |

Empresa: `comercialRequiereAprobacion=true`, umbral **$500.000**, `ventaBajoCosto=BLOQUEAR`.

Login: `admin@almahue.local` / `Admin123!` · PIN: `4821`

Re-ejecutar solo documentos flujo:

```bash
npm run seed:demo-propuesta
```

---

## 4. Recorrido sugerido (15 min)

1. **Inventario › Bodegas / Insumos** — maestros Almahue y stock por bodega.
2. **Compras › Cotizaciones** — `ALM-COT-001` → generar OC.
3. **Compras › Aprobaciones OC** — `ALM-OC-001` pendiente + `OC-2026-001` showcase.
4. **Compras › Recepción** — `ALM-OC-003` recepcionada.
5. **Ventas › Orden de venta** — `ALM-OV-002`…`004` (cereza + bodega frigorífico).
6. **Ventas › Aprobaciones OV** — aprobar `ALM-OV-002` con admin + PIN.
7. **Emitir documento** — `ALM-FAC-101` → contabilizar → folio stub.

---

## 5. Producción

No aplicar este seed ni flags de demo en `45.7.229.46` sin acuerdo. Ver `DEPLOY-PROD-FASE2.md`.
