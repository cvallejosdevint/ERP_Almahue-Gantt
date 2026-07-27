# Implementación tarjetas nuevas — Reunión 1

Plan técnico para pasar de **mock UI** a **backend + BD + front real** en las 9 pantallas fuera del Gantt F1.

**Referencias:** `modulos/*.md`, `matriz-trazabilidad.csv`, mocks en `ERP/erp_front`, estado real en `ERP/erp_back`.

**Convenciones existentes:**
- API prefix: `/api/v1`
- Multiempresa: header `X-Empresa-Id` + `resolveOperationalEmpresa()` (`erp_back/src/auth/tenant.util.ts`)
- Permisos: decoradores `@RequirePermissions` / `@RequireAnyPermission`
- Front: `src/services/api.ts` → `real/api.ts` (reemplazar stubs en `real/stub.ts`)

---

## Sprint 0 — Base de datos (una migración inicial versionada)

Hoy `prisma/migrations/` está vacío. Crear migración `init_core_contratistas` (schema actual) + `reunion1_modulos_operativos`.

### Modelos nuevos (resumen)

```prisma
// --- CONTRATISTAS (C-06, C-07) ---
enum EstadoProforma { BORRADOR DEFINITIVA FACTURADA }

model ProformaContratista {
  id            String   @id @default(cuid())
  numero        String
  contratistaId String
  contratista   Contratista @relation(...)
  empresaId     String
  periodo       String   // ej. 2026-07
  estado        EstadoProforma
  montoNeto     Decimal
  moneda        String   // CLP|USD|CNY|EUR
  facturaId     String?  @unique
  factura       FacturaContratista? @relation(...)
  lineas        ProformaLinea[]
  @@unique([empresaId, numero])
}

model FacturaContratista {
  id          String @id @default(cuid())
  numero      String
  proformaId  String @unique
  fecha       DateTime
  montoNeto   Decimal
  empresaId   String
}

model CierreMesContratistas {
  id          String   @id @default(cuid())
  empresaId   String
  periodo     String   // YYYY-MM
  cerradoAt   DateTime?
  cerradoPor  String?
  traspasado  Boolean  @default(false)
  @@unique([empresaId, periodo])
}

model TraspasoContratistas {
  id          String   @id @default(cuid())
  cierreId    String
  tasasJson   Json     // { CLP:1, USD:..., CNY:..., EUR:... }
  asientoId   String?  // link futuro contabilidad
  createdAt   DateTime @default(now())
}

// --- COMPRAS (P-01, P-07, P-08) ---
enum EstadoOC { BORRADOR PENDIENTE_APROBACION APROBADA RECHAZADA RECEPCIONADA PARCIAL CERRADA }

model Proveedor {
  id        String @id @default(cuid())
  rut       String
  razonSocial String
  empresaId String
  @@unique([empresaId, rut])
}

model OrdenCompra {
  id              String @id @default(cuid())
  numero          String
  empresaId       String
  proveedorId     String
  fecha           DateTime
  moneda          String
  tipoPago        String?
  afectoExento    String?  // PEND-01 nullable hasta decisión
  neto            Decimal
  estado          EstadoOC
  tcCreacion      Decimal? // informativo
  lineas          OrdenCompraLinea[]
  distribuciones  OrdenCompraDistribucion[]
  recepciones     RecepcionOC[]
  @@unique([empresaId, numero])
}

model OrdenCompraLinea {
  id            String @id @default(cuid())
  ordenId       String
  descripcion   String
  cantidad      Decimal
  precio        Decimal
  centroCostoId String
}

model OrdenCompraDistribucion {
  id            String @id @default(cuid())
  ordenId       String
  centroCostoId String
  monto         Decimal
  // validación: sum(distribuciones) == neto OC
}

model RecepcionOC {
  id        String @id @default(cuid())
  ordenId   String
  fecha     DateTime
  tcAplicado Decimal
  asientoId String?
}

model RegistroCompra {
  id           String @id @default(cuid())
  ordenId      String
  proveedorId  String  // debe coincidir con OC
  numeroFactura String
  monto        Decimal
  fecha        DateTime
}

// --- INSUMOS / BODEGA (I-01, I-04, I-05) ---
model ArticuloInsumo {
  id          String @id @default(cuid())
  familia     String
  subfamilia  String
  descripcion String
  empresaId   String
  @@unique([empresaId, familia, subfamilia, descripcion])
}

model Bodega {
  id        String @id @default(cuid())
  codigo    String
  nombre    String
  empresaId String
  activa    Boolean @default(true)
  @@unique([empresaId, codigo])
}

enum TipoMovimientoBodega { ENTRADA_PROVEEDOR TRASLADO DEVOLUCION_NC }

model MovimientoBodega {
  id          String @id @default(cuid())
  tipo        TipoMovimientoBodega
  bodegaId    String
  articuloId  String
  cantidad    Decimal
  precioUnit  Decimal? // NC: precio factura origen
  facturaRef  String?
  empresaId   String
}

model ParamContabilizacionBodega {
  id           String @id @default(cuid())
  tipoMovimiento TipoMovimientoBodega
  familia      String?
  cuentaDebe   String
  cuentaHaber  String
  empresaId    String
}

// --- CONTABILIDAD (K-05) ---
model IndicadorFinanciero {
  id        String   @id @default(cuid())
  fecha     DateTime @db.Date
  moneda    String   // USD|EUR|CNY
  valor     Decimal
  fuente    String   @default("BC")
  @@unique([fecha, moneda])
}
```

---

## Por tarjeta — entregables

### 1. Tarifas contratista (C-03) — ✅ HECHO

| Capa | Estado | Notas |
|---|---|---|
| BD | `TarifaContratista` | Multi-línea, CC empresa |
| API | `GET/POST/PUT/DELETE /tarifas-contratista` | `contratistas.controller.ts` |
| Front | `TarifasContratistaPage` | `onSave` → API real |

**Pendiente menor:** POST centros de costo desde catálogo UI.

---

### 2. Proformas y facturas (C-06) — ✅ IMPLEMENTADO (22/07/2026)

| Capa | Estado |
|---|---|
| BD | `ProformaContratista`, `FacturaContratista`, enum `EstadoProforma` |
| Migración | `20260722163000_proformas_contratista` |
| API | `GET/POST/PUT/DELETE /proformas-contratista`, `POST .../definitiva`, `POST .../factura` |
| Front | `ProformasContratistaPage` con CRUD + flujo Definitiva/Factura |
| Seed | 3 proformas demo (BORRADOR, DEFINITIVA, FACTURADA) |

---

### 3. Traspaso y cierre mes contratistas (C-07)

**Reglas:** solo Admin; tasas CLP/USD/CNY/EUR; digitador no cierra.

| Back | Detalle |
|---|---|
| Endpoints | `GET /cierres-contratistas?periodo=`, `POST /cierres-contratistas/:periodo/cerrar`, `POST /traspaso-contratistas` |
| Validaciones | Todas proformas del periodo en FACTURADA (configurable PEND-02); permiso admin |
| Side effect | Marca `CierreMesContratistas.cerradoAt`; prepara asiento (stub hasta módulo contabilidad) |

| Front | `TraspasoContratistasPage` — form tasas + botón cerrar/traspasar con confirmación |

---

### 4. Orden de compra servicios (P-01 / P-03)

**Reglas:** sin solicitud compra; distribución CC cuadra neto; CC solo empresa activa.

| Back | Módulo `compras/` |
|---|---|
| Endpoints | CRUD `ordenes-compra`, `POST /ordenes-compra/:id/distribucion/validar` |
| Modelos | `OrdenCompra`, líneas, distribuciones, `Proveedor` |
| Validación | `sum(distribucion.monto) === orden.neto` → 400 si no cuadra |
| Estados | BORRADOR → PENDIENTE_APROBACION al enviar |

| Front | `OrdenesCompraPage` — wire form + validación inline suma CC |

**Dependencia:** catálogo proveedores (mínimo CRUD en mismo módulo).

---

### 5. Recepción OC (P-07)

| Back | `POST /recepciones-oc`, `GET /recepciones-oc` |
|---|---|
| Reglas | TC del día desde `IndicadorFinanciero` o manual; genera asiento pendiente |
| Link | `ordenId` debe estar APROBADA |

| Front | `RecepcionesOcPage` — mostrar TC antes de confirmar |

**Dependencia:** P-01 + K-05 (TC).

---

### 6. Registro compra / factura (P-08)

| Back | `POST /registros-compra` |
|---|---|
| Reglas | `proveedorId` factura = OC; anti-cruzado por monto; alerta Afecto/Exento (PEND-01) |

| Front | `RegistroCompraPage` — validación cliente + errores API |

**Dependencia:** P-07.

---

### 7. Bodegas (I-01)

| Back | Módulo `insumos/` — `GET/POST/PUT /bodegas` |
|---|---|
| Reglas | Código único por empresa; filtro `empresaId` |

| Front | `BodegasPage` — CRUD real |

---

### 8. Movimientos bodega / NC (I-04 / I-05)

| Back | `POST /movimientos-bodega` tipos ENTRADA_PROVEEDOR, TRASLADO, DEVOLUCION_NC |
|---|---|
| Reglas | NC a precio factura (`precioUnit` + `facturaRef`); sin FIFO/LIFO |
| I-03 | `ParamContabilizacionBodega` — endpoint CRUD separado o seed inicial |

| Front | `MovimientosBodegaPage` — tipos + selector factura en NC |

**Dependencia:** I-01 + maestro artículos (P-02).

---

### 9. Indicadores Banco Central (K-05)

| Back | Módulo `contabilidad/` — `GET /indicadores-bc`, job `syncBcIndicadores` |
|---|---|
| Reglas | USD/EUR/CNY; rellenar feriados/domingos; DEC-06 |
| Job | Cron 09:00 CL — fetch API BC (o CSV manual v1) → upsert `IndicadorFinanciero` |
| Consumo | Recepción OC, traspaso contratistas, asientos |

| Front | `IndicadoresBcPage` — lectura real + badge “última sync” |

---

## Integración front (patrón por módulo)

Para cada entidad, replicar el patrón **tarifas**:

1. DTO/types alineados en `domain.ts` (ya existen)
2. Métodos en `services/real/api.ts`
3. Export en `services/api.ts` (siempre real, no demo)
4. Página: pasar `onSave` / `onDelete` a `MockListPage`
5. Quitar entrada de `stub.ts` correspondiente
6. Seed en `prisma/seed.ts` para UAT

---

## Checklist por sprint

### Sprint A — Contratistas (C-06, C-07)
- [x] Migración Prisma proformas + factura
- [x] Endpoints proformas/facturas
- [ ] Endpoints cierre/traspaso + guard admin (C-07)
- [x] Front proformas wired
- [ ] Tests e2e happy path proforma→factura→cierre

### Sprint B — Compras (P-01, P-07, P-08)
- [ ] Migración proveedores + OC + recepción + registro
- [ ] Validación distribución CC
- [ ] Wire 3 páginas compras
- [ ] Integrar aprobación (P-06) en mismo módulo

### Sprint C — Insumos (I-01, I-04, I-05)
- [ ] Migración artículos + bodegas + movimientos
- [ ] Param contabilización (I-03) seed mínimo
- [ ] Wire bodegas + movimientos

### Sprint D — Indicadores BC (K-05)
- [ ] Modelo + sync job
- [ ] Consumo en recepción OC
- [ ] Wire indicadores page

---

## Estimación orientativa

| Sprint | Back + BD | Front | UAT |
|---|---|---|---|
| A Contratistas | 3–4 d | 1–2 d | 1 d |
| B Compras | 5–6 d | 2–3 d | 2 d |
| C Insumos | 4–5 d | 2 d | 1 d |
| D Indicadores BC | 2 d | 0.5 d | 0.5 d |

**Total ~3–4 semanas** con un dev full-stack, asumiendo Sprint A parcialmente adelantado (tarifas listas).

---

## Próximo paso inmediato

1. Crear migración Prisma versionada (`npx prisma migrate dev --name reunion1_proformas`)
2. Implementar **C-06 Proformas** (backend completo)
3. Conectar front `ProformasContratistaPage`
4. Validar UAT con datos seed
5. Repetir para C-07, luego módulo `compras`
