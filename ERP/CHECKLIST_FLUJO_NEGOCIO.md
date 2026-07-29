# Checklist — circuito flujo de negocio (Demo OFF)

**Fecha:** 2026-07-28 · **Actualizado:** 2026-07-28 (cierre deferred) · **Modo:** Demo Mode OFF (Nest → Prisma)  
**Credenciales seed:** `admin@almahue.local` / `Admin123!` · empresa EMP-1  
**URL publicada:** `http://45.7.229.46/almahue-erp/`

Precondiciones: `erp_back` migrado + seed; `erp_front` en local; toggle Demo **OFF**.

## Smoke (8–12 pasos)

1. **Login** → empresa Almahue (EMP-1) activa en header.
2. **Catálogos → Proveedores** → ver seed (`Agro Insumos Sur`); crear uno nuevo con RUT único.
3. **Compras → OC** → Nueva OC eligiendo proveedor del selector (no texto libre) + dist. CC que cuadre → Guardar → **Exportar / Imprimir** (plantilla logo).
4. **Compras → Aprobaciones** → aprobar OC pendiente (si aplica).
5. **Compras → Libro de compras** → registrar factura con proveedor del maestro; opcional carga masiva CSV y ver dupes en preview.
6. **Ventas → Libro de ventas** → factura borrador; **Grabar y contabilizar** con cuenta/CC (default SII); crear **NC** asociada a factura origen.
7. **Comercial → Cotizaciones** → crear/listar → **Exportar / Imprimir** (misma plantilla).
8. **Admin → Plantilla documentos** → logo/URL, sello, toggles pie/dirección/columnas → vista previa.
9. **Insumos → Movimientos** → `SALIDA_PROVEEDOR` con par automático + estados visibles.
10. **Contabilidad → Períodos** → periodo `2026-07` (o mes actual) **ABIERTO**.
11. **Contabilidad → Centralización** → Preview → Confirmar → docs marcados / asientos creados.
12. **Tesorería → Cartolas** → Importar Excel/CSV **o PDF** (texto seleccionable) → preview → import → ver movimientos.
13. **Contratistas** (opcional circuito corto): ingreso diario → asociación → proforma → aprobación → traspaso.

## Estado deferred / cerrado

| Ítem | Estado |
|---|---|
| GoSocket / DTE productivo (sin API keys) | **DEFERRED** — no tocar |
| Redeploy SSH / URL publicada | **DONE** — `http://45.7.229.46/almahue-erp/` |
| PDF logo cotización/OC (plantilla admin) | **DONE** — Admin → Plantilla documentos + print browser |
| Parser PDF cartola (heurística genérica) | **DONE** (mejor esfuerzo) — escaneados / banco-específico sin muestra aún limitado |
| BND | **DEFERRED** — sin reqs concretos de Diego en repo/docs; no inventar plataforma |

## Builds locales

```bash
cd ERP/erp_back && npx prisma migrate deploy && npm run seed && npx nest build
cd ERP/erp_front && npx tsc -b
```
