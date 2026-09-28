# Checklist de flujo completo — Almahue ERP (27/08/2026)

**Qué es:** mapa operativo para QA y onboarding interno. **No** es un ERP de manual (SAP/Softland/Gemini).  
**Autoridad:** Reu6 (MJ/Agustín) > Reu5 > Reu4 > Lupe/Mario 20/08 (operativo; no pisa Reu6) > código 21/08. Carlos/Sergio en demo = hipótesis.

**QA menú Ventas (esta fecha):** modo demo en `http://localhost:5174` (Postgres local no arrancó sin privilegios; login real → 500). Recorrido SPA con admin `*`.

---

## 0. GoSocket: cómo leer Reu1–Reu3 vs el resto

En **Reu1, Reu2 y Reu3** se pensó GoSocket / Acepta como **plataforma aparte** donde Almahue emitía (portal del facturador). El ERP era gestión; el DTE vivía afuera.

| Reunión | Lectura de GoSocket | ¿Sigue vigente? |
|---|---|---|
| Reu1–Reu3 | Facturador **aparte**; coordinar implementación después del ERP básico; en compras, partner trae facturas de proveedores | **Histórico.** No diseñar el menú del ERP como si el operador emitiera en el portal. |
| Reu4 | *«Emisión portal primero; integración ERP ~2 semanas»* (marcha blanca). MJ preguntó si facturan en GoSocket o en el ERP. **Acuerdo: una sola plataforma = ERP**; GoSocket transparente debajo. D8: quitar Emitir del libro. | **Transición.** Portal = CAF, cert, XML/PDF, errores (GOS-4). Operador emite en el ERP. |
| GoSocket QA (ago) | API sandbox sin contrato; IOFactura post-firma; CAF/cert en portal; fail-closed sin rango de folio | **Técnico vigente.** |
| Código hoy | ERP → `billing-gateway` → GoSocket sandbox. Sin CAF = `REJECTED`, no asiento. No SII live. | **As-is.** |

Instructivo MJ de NC/ND Comex (Acepta) describe el **portal**. Los campos (puertos, cláusula, bultos, RUT `55.555.555-5`) deben vivir en **Emitir DTE** del ERP, no mandar al usuario a otra web.

---

## 1. Menú Ventas (implementado 27/08)

```
Ventas
  Operación
    Órdenes de venta          /comercial/ordenes-venta
    Emitir DTE                /comercial/emitir
  Libros
    Libro de ventas           /comercial/libro
    Libro de guías            /comercial/guias-despacho
  Maestros
    Clientes                  /comercial/clientes
```

| Caso | Esperado | QA 27/08 |
|---|---|---|
| Orden del menú | OV y Emitir DTE antes que los libros | PASS |
| Labels | No dice «Emitir documento» ni «Guías de despacho» como alta | PASS |
| FACTURA sin OV | `/comercial/emitir` → «Seleccione orden de venta» | PASS |
| NC / ND / GUÍA | `/comercial/emitir?tipo=NC\|ND\|GUIA` → título Emitir DTE, sin exigir OV | PASS |
| Libro de guías → Emitir guía | `/comercial/emitir?tipo=GUIA` | PASS |
| Libro de ventas | Consulta; **sin** botón Emitir (Reu4 D8) | PASS |
| Bookmark cotiz | `/comercial/cotizaciones` → `/compras/ordenes` | PASS |
| Compras | OC, Aprobaciones, Recepciones, Libro. Sin Cotizaciones | PASS |
| Roles | Catálogo «Emitir DTE» y «Libro de guías»; alias de nombres viejos | PASS (unit + UI) |
| Sidebar colapsado | Flyout con los mismos destinos | PASS |
| Wizard OV | `/comercial/ordenes-venta/nueva` distinto de Emitir DTE | PASS |

Permisos: `Ventas · Emitir documento` y `Ventas · Guías de despacho` se mapean a las claves nuevas (`PANTALLA_ALIASES`).

---

## 2. Compras (Procure-to-Pay) — Almahue, no Gemini

1. Cotización del proveedor llega **fuera** del ERP (mail/PDF). Lupe 20/08: *al tiro se genera la OC*.
2. **Compras › Órdenes de compra**: referencia cotiz opcional (tipo/folio/fecha). Guardar borrador **o** Enviar a aprobación. Correlativo `OC-AAAA-NNNN`.
3. Cadena PIN **solo Compras** (servicios y materiales). Lupe/Mario 20/08; corte 21/08 (se eliminó cadena OV).
4. **Recepcionar**: hito de cantidades. **No** entra stock. **No** crea el asiento de deuda (distinto de Agrosoft, donde recepcionar servicio hacía gasto vs facturas por recibir).
5. Material: **Insumos › Movimientos** `ENTRADA_PROVEEDOR`.
6. **Libro de compras**: asociar factura **recibida** (no emitir DTE de compra). OC no aprobada = destacar; **no** contabilizar ni pagar hasta OC `APROBADO` o posterior (Lupe/Mario). Reu4 D4 pedía aprobada+recepcionada; el corte 21/08 relajó el *alta* y endureció el *asiento/pago*.
7. Cuadratura de montos (`matchOk`) al asociar. Contabilizar es un paso explícito → pasivo + CC + aging.
8. **Tesorería › Pagos / Nómina semanal**: calce. **No** asiento `PAGO:{id}`. Banco = **cartola** contabilizada (`CARTOLA:{id}`).

Contratistas (ingreso diario, proformas) **no** es esta OC ni un portal de proveedores.

---

## 3. Ventas (Order-to-Cash) — Almahue, no Gemini

1. **No** hay cotización de cliente (Reu6 D11). Documento = **Orden de venta**.
2. OV `BORRADOR` → **Confirmar (stock)** → `SALIDA_VENTA`. Precio editable; no vender bajo `costoPromedio` (D16).
3. **Emitir DTE** factura desde esa OV (`contexto=factura-ov`). NC/ND/guía pueden ir sin OV.
4. La **guía** en menú es un **libro**. El alta DTE tipo 52 está en Emitir DTE. Despacho logístico (picking/packing) sigue incompleto. Reu4 D5 (guía mueve bodega) vs Reu6 D13 (stock en la OV): **el código sigue D13**.
5. Libro de ventas = emitidos/contabilizados (D6/D8). Reverso = contable; anulación SII = NC.
6. Cobro: factura `CONTABILIZADA`; calce en tesorería. Banco = cartola. Cobranza R4-18 diferida.
7. Export: tipo 110 + NC/ND de liquidación Comex (MJ Reu4). Indicador exportación / RUT extranjero en Emitir. No es un ítem de menú aparte (gap de industria, no de este PR).

Aprobación de OV: **eliminada** 21/08. No restaurar.

---

## 4. Tesorería y contabilidad (puentes)

| Evento | Qué mueve |
|---|---|
| Contabilizar compra/venta | Asiento de deuda/ingreso + CC + aging |
| Pago / cobro en Tesorería | Calce; **no** asiento de pago |
| Cartola › contabilizar TRX | Asiento banco |
| Nómina semanal | Semana de compromiso S1–S5 del periodo; aplazar no muta DTE |

---

## 5. Recorrido QA sugerido (operadores, no superadmin)

**Compras:** OC borrador → enviar → PIN N1 (y N2 si monto > tope) → recepcionar → (si material) entrada bodega → libro asociar factura → contabilizar → pagos / nómina. Caso OC no aprobada: asociar se ve destacada; contabilizar/pagar bloqueados.

**Ventas:** OV nueva → confirmar stock → Emitir DTE (factura) → ver en libro. NC/ND desde Emitir con referencia. Guía desde Libro de guías › Emitir guía. Sin CAF: borrador / error partner (no FAIL de producto).

**Holding:** probar con empresa Export y Services (dos RUT). No mezclar tenant.

---

## 6. No reabrir

- Menú/CRUD Cotizaciones; cotiz → NP → factura.
- Emitir DTE al aprobar OV.
- Factura de compra «emitida» como wizard SII.
- Asiento `PAGO:{id}`.
- SII live / GoSocket productivo sin CAF.
- Cadena de aprobación en OV o proformas.
- Maestro Productor.

---

## 7. Evidencia menú 27/08

- Unit: `pantallas-permisos.spec.ts`, `filterMenuByPermissions.spec.ts` (9 tests).
- UI demo: grupos Operación / Libros / Maestros; Emitir DTE; Libro de guías; redirect cotiz; Roles con nombres nuevos; libro ventas sin botón emitir; `?tipo=GUIA` desde CTA.
