# Auditoría Reu5 vs Reu6 + gap «Emitir documento»

**Fecha:** 2026-08-14  
**Modo:** Auditoría de arquitectura y negocio (solo lectura; sin cambios de código)  
**Fuentes:** `reunion5-minuta-2026-08-03.md`, `fuentes/transcripcion-reunion5.md`, `fuentes/reunion5-minuta-tldv-2026-08-03.md`, `reunion6-minuta-2026-08-06.md`, `fuentes/transcripcion-reunion6.md`, `entrega-reu4-reu5-as-is/01-TOMA-REQUERIMIENTOS.md`, código `ERP/erp_front` + `ERP/erp_back` (corte 14/08/2026).

**Prioridad documental:** Reu6 > Reu5 > Reu4 (convención Almahue).

---

## 1. Resumen ejecutivo

La Reunión 5 (03/08, Devint interno) consolidó **ajustes operativos** sobre lo ya demo en Reu4: PIN por rol, aprobador elegido por solicitante, cotizaciones en Ventas con conversión NP/factura, emisión directa con líneas libres, libros y borradores.

La Reunión 6 (06/08, Almahue + Devint) **reorienta el producto** hacia ficha única, organigrama de aprobaciones, separación compras/ventas, **órdenes de venta con inventario**, y deja explícito que las «cotizaciones de venta» no son el flujo correcto.

El código actual (post-Reu6) implementa gran parte de Reu6, pero **mantiene el wizard `/comercial/emitir` con descripción libre**, heredado del modelo Reu5 de «emisión directa». Eso contradice el espíritu de Reu6 para productos inventariables (D12–D15), aunque el subtítulo del wizard ya redirige a OV para facturar desde stock.

---

## 2. Fase 1 — Contraste Reu5 vs Reu6

### 2.1 Tabla de discrepancias (Reu5 modificado, anulado o sobrescrito por Reu6)

| # | Tema | Reu5 (decisión / implementación) | Reu6 (decisión) | Efecto para evitar doble trabajo | Estado código (14/08) |
|---|---|---|---|---|---|
| R5-01 | **PIN y aprobaciones** | Checkbox «Aprobar con PIN» en **rol**; cada usuario con PIN propio (ADM-008) | **D5:** quitar PIN del rol; PIN solo para designados en **reglas de aprobación** | No seguir amarrando PIN al mantenedor de roles | Implementado (post-Reu6) |
| R5-02 | **Selección de aprobador** | Solicitante elige aprobador de lista de personas con permiso (proformas, OC, cotizaciones) | **D4/D6:** cadena **automática** por montos + línea de mando + suplencia; no elegir aprobador ajeno al área | No invertir en UI de «picker libre» como modelo final | Implementado (grupos/escalas); legacy workflows-admin persiste como deuda |
| R5-03 | **Cotizaciones en Ventas** | Cotizaciones en menú Ventas, estructura similar a OC, con aprobación; convertible a NP o factura (VEN-021/022; transcripción L235–236) | **D11:** «Cotizaciones» en Ventas → **Orden de venta**; MJ: cotizar es de **Compras**; ventas no cotizan | **No restaurar** cotiz→NP→factura en Ventas; no vender cotización ventas en demo | Compras › Cotizaciones; Ventas › OV; redirect `/comercial/cotizaciones` |
| R5-04 | **Flujo venta con stock** | Emisión directa de factura con ítems libres + cuenta contable; cotización como previo comercial | **D12–D15:** OV producto/servicio; producto **ligado a maestro + bodega + stock**; movimiento en OV; factura copia qty/desc, precio editable | El trabajo de catálogo/stock va en **OV**, no en duplicar lógica en emitir | OV implementada; emitir sin catálogo |
| R5-05 | **Conversión comercial** | Cotización → NP → Factura (UI «hecho» en minuta Reu5) | Reu6 no menciona NP en ventas; acuerdo posterior: **OV → factura** | Descartar NP como puente de ventas | `convertirDocumento` desde OV a FACTURA |
| R5-06 | **Aprobación cotizaciones venta** | Implementada «por si acaso» aunque MJ dijo que no la usaban (transcripción Reu5 L199) | Comercial en reglas queda **reservado**; foco en OC y proformas | No priorizar bandeja aprobación para OV hasta definición Almahue | Sin cadena OV/factura |
| R5-07 | **Alta de cliente en emisión** | Botón `+` panel derecho en cotizaciones (VEN-023) | **D8:** ficha única cliente/proveedor (bancos, contactos, despacho, trazabilidad) | Extender ficha, no solo modal rápido en cotización | Ficha con pestañas; emitir exige cliente en maestro |
| R5-08 | **Proveedores / clientes** | Productores fuera de menú Compras; bases separadas implícitas | **D7/D8:** bases separadas; lookup RUT unificado (sociedad/proveedor/cliente/productor) | Lookup unificado, listados separados | Parcial (productor sin maestro) |
| R5-09 | **Centro de costo en ventas** | Ventas **sin CC obligatorio**; compras con CC por ítem (acordado Reu5) | No revocado; plan de cuentas con flags CC/elemento/área (**D9**) | Mantener: ventas por cuenta en ítem, no CC | Cumple en emitir (cuenta por ítem) |
| R5-10 | **Administración usuarios** | Demo en ambiente dev; roles con permisos | **D1–D3:** usuarios desde ERP; multi-empresa; permisos por rol (variación = otro rol) | Panel Admin como fuente de verdad | Cumple |
| R5-11 | **SSO Microsoft** | No tratado en Reu5 | **D19:** incorporar Entra; botón disabled hasta `.env` | No bloquear login clásico | Parcial (MSAL stub) |
| R5-12 | **GoSocket / DTE** | Diferido explícito (Reu5 + Reu4) | **Diferido**; credenciales lunes con Pablo; stub PDF | Misma línea: no emitir SII real | Stub `billing/` |
| R5-13 | **Libros, borradores, totalizados** | Must Reu5: totalizados, panel colapsable, borradores por usuario, paginación periodos, folio clickeable | No anulado; Reu6 no los contradice | Seguir como baseline UI | Implementado |
| R5-14 | **Cartolas / tesorería demo** | Base cartolas; conciliación pendientes; estado cuenta con tipo movimiento | Reu6: demo contabilidad+tesorería **siguiente reunión** | No asumir demo cliente cerrada | Módulos existen; demo no cerrada |
| R5-15 | **Recargos SII en detalle** | Descuentos/recargos global y línea en factura (Reu5) | **D17:** flete = **línea adicional**, no recargo SII en detalle | Modelar FLETE como línea en OV | Parcial (OV sí; emitir no) |
| R5-16 | **Precio mínimo / costo** | No discutido en Reu5 | **D16:** no vender bajo costo (parametrizable; excepción merma) | Regla en maestro + OV; no en emitir libre | API `ventaBajoCosto`; sin UI admin |
| R5-17 | **Plan de cuentas** | Periodos solo header; historial abrir/cerrar | **D9/D10:** atributos por cuenta; **inactivar** vs eliminar | No permitir delete con movimiento | Cumple |
| R5-18 | **Ambiente piloto** | Deploy local; ajustes pendientes | **D20:** host publicado; datos de prueba; pueden cargar reales | Prod puede ir detrás de local | Parcial (deploy explícito pendiente) |

### 2.2 Decisiones Reu5 que **permanecen vigentes** (no las anula Reu6)

- Emisión fuera del libro en pantalla dedicada (`/comercial/emitir`).
- Borradores por usuario; libro solo contabilizados/emitidos.
- Ventas sin centro de costo obligatorio; imputación por **cuenta contable** en ítem.
- Neto / exento / IVA; descuento global y por línea.
- Reverso contable vs NC tributaria (heredado Reu4).
- GoSocket transparente bajo «Grabar y contabilizar» — **diferido** en ambas reuniones.
- SMTP, correo PIN, reenvío PDF — **diferido** Reu5.

### 2.3 Tensiones no resueltas entre minutas (requieren criterio explícito)

| Tema | Reu5 / Carlos-Sergio | Reu6 / MJ-Agustín | Riesgo si no se elige |
|---|---|---|---|
| Emisión directa con texto libre | Válida para factura «rápida» | Productos deben salir del maestro vía OV | Facturas sin trazabilidad de stock ni código DTE consistente |
| Servicios en emitir | Implícito (línea libre) | D12 permite tipo **servicio** sin stock | Servicios en emitir OK; productos en emitir **no** |
| Aprobación comercial | Cotizaciones con aprobación (Reu5) | D4 reserva módulo Comercial | Expectativa de «todo documento con PIN» en ventas |

---

## 3. Fase 2 — Auditoría de gap: «Emitir documento» y texto libre

### 3.1 Síntoma observado

En `/comercial/emitir`, paso **2. Ítems**, el campo **Descripción** es un `<Input>` de texto libre. El usuario puede escribir cualquier cadena (p. ej. «asd»), fijar cantidad y precio, y contabilizar sin elegir un artículo del maestro de insumos.

La pantalla **Órdenes de venta** (`/comercial/ordenes-venta`), en cambio, obliga para tipo **Producto** a seleccionar artículo vía `SearchableSelect` sobre `api.getInsumos()`, asignar bodega(s) y validar stock al confirmar.

### 3.2 Evidencia en frontend

| Aspecto | `EmitirDocumentoPage.tsx` | `OrdenVentaPage.tsx` |
|---|---|---|
| Selector de insumo | **No** — solo `Input` descripción | `SearchableSelect` sobre catálogo |
| `tipoLinea` | **No envía** | `PRODUCTO` \| `SERVICIO` \| `FLETE` |
| `insumoId` / `codigoProducto` | Campos en `LineItem` pero **nunca se populan** en UI | Obligatorio para producto |
| Bodega / splits | **No** | Sí, con `getInsumoStockBodegas` |
| Validación paso 2 | `descripcion` + `precioUnitario > 0` | Cliente + líneas con insumo o servicio |
| Subtítulo de página | Indica usar OV para facturar desde stock | «Producto con stock por bodega…» |

Fragmento representativo del wizard emitir (descripción libre):

```163:168:ERP/erp_front/src/features/comercial/EmitirDocumentoPage.tsx
        <Field label="Descripción" className="sm:col-span-2">
          <Input
            value={item.descripcion}
            placeholder="Producto o servicio"
            onChange={(e) => onUpdate(item.id, { descripcion: e.target.value })}
```

Payload al guardar: solo mapea `descripcion`, sin `tipoLinea` ni `insumoId`:

```731:741:ERP/erp_front/src/features/comercial/EmitirDocumentoPage.tsx
        lineas: items.filter((it) => it.descripcion).map((it) => ({
          descripcion: it.descripcion,
          cantidad: it.cantidad,
          precioUnitario: it.precioUnitario,
          ...
          codigoProducto: it.codigoProducto || undefined,
```

### 3.3 Evidencia en backend

`normalizeLineas` exige **texto** en `descripcion`, pero `insumoId` y `tipoLinea` son opcionales.

`assertLineasMaestro` (invocado en `createDocumento` / `updateDocumento`):

- Si `tipoLinea` no viene, asume **`SERVICIO`**.
- Solo si `tipoLinea === 'PRODUCTO'` exige `insumoId`, resuelve código/unidad desde `Insumo`, valida precio ≥ costo y (para `ORDEN_VENTA`) bodega/splits.
- Líneas **SERVICIO** aceptan cualquier descripción sin enlace al maestro.

```611:633:ERP/erp_back/src/modules/comercial/comercial.service.ts
  private async assertLineasMaestro(...) {
    ...
    const tipo = (l.tipoLinea || 'SERVICIO').toUpperCase();
    ...
    if (tipo !== 'PRODUCTO') continue;
    if (!l.insumoId) {
      throw new BadRequestException(
        `Línea «${l.descripcion}»: un producto debe usar un código del maestro de artículos`,
      );
    }
```

**Movimiento de inventario:** `applySalidaVentaOv` solo corre al **confirmar OV**, no al emitir factura directa. Una factura creada en emitir con líneas SERVICIO no toca `StockInsumoBodega` ni `MovimientoBodega`.

### 3.4 Modelo de datos

- **Maestro:** tabla `Insumo` (código, nombre, unidad, `costoPromedio`, empresa).
- **Stock:** `StockInsumoBodega` + movimientos en confirmación OV.
- **Documento:** `DocumentoComercial.lineas` (JSON) admite `tipoLinea`, `insumoId`, `bodegaId`, `splits`, `codigoProducto` — campos usados por OV, ignorados por emitir.

No hay FK línea→insumo a nivel relacional; la integridad depende de validación en servicio y de qué envíe cada pantalla.

### 3.5 Por qué existe el hueco (causa raíz)

1. **Herencia Reu5:** la emisión de factura se diseñó como wizard contable/tributario flexible (descripción + precio + cuenta), coherente con venta de servicios y con NC/ND/guía, **antes** del acuerdo Reu6 de inventario.
2. **Implementación incremental Reu6:** se entregó `OrdenVentaPage` con catálogo y stock, pero **no se restringió** emitir ni se unificó el componente de líneas.
3. **Backend permisivo por diseño dual:** `assertLineasMaestro` distingue PRODUCTO vs SERVICIO; emitir solo usa la rama SERVICIO por omisión.
4. **Separación de responsabilidades incompleta en UI:** el subtítulo de emitir advierte usar OV para stock, pero no hay gateway que impida facturar productos inventariables con texto libre.
5. **Reu6 no pidió eliminar emisión directa:** pidió que el **canal con stock** sea OV; el canal sin stock (servicios, ajustes, exportación COMEX) sigue siendo emitir.

### 3.6 Qué faltaría para amarrar a BD (to-be mínimo)

| Capa | Cambio | Objetivo |
|---|---|---|
| **Negocio** | Definir: ¿emitir admite solo SERVICIO/FLETE y NC/ND/guía? ¿Producto siempre vía OV? | Alinear con D12–D13 |
| **Front emitir** | Reutilizar patrón OV: `tipoLinea`, selector `getInsumos`, stock por bodega **o** bloquear PRODUCTO y exigir referencia OV | UX consistente |
| **Front emitir** | Precarga desde OV al facturar (ya existe `convertirDocumento` desde OV) | Cantidad/descripción bloqueadas, precio editable (D13) |
| **Back** | Para `FACTURA` con líneas PRODUCTO: exigir `insumoId` **o** `documentoOrigenId` tipo `ORDEN_VENTA` | Cerrar bypass API |
| **Back** | Opcional: rechazar líneas SERVICIO si `descripcion` coincide con patrón de producto inventariable (heurística débil; mejor regla explícita) | Defensa en profundidad |
| **Back** | No duplicar salida de stock en factura si OV ya confirmó | Evitar doble movimiento |
| **DTE** | Canonical builder debe recibir `codigoProducto` desde insumo | GoSocket futuro |
| **QA** | Caso: intentar facturar producto sin OV → FAIL; servicio en emitir → PASS; OV→factura → PASS | Regresión |

### 3.7 Clasificación del gap

| Dimensión | Severidad | Nota |
|---|---|---|
| vs Reu6 (productos) | **Alta** | Permite vender «cajas cerezas» sin código ni stock (cita Agustín, Reu6) |
| vs Reu5 (emisión directa) | **Coherente** | Reu5 no exigía maestro en emitir |
| Contabilidad | Media | Asiento con cuenta manual; sin dimensión inventario |
| Inventario | **Alta** | Cero impacto en bodega |
| Demo / piloto | **Alta** | Riesgo de datos incoherentes si usuarios mezclan OV y emitir |

---

## 4. Matriz de trazabilidad requerimiento → pantalla

| Requerimiento | Pantalla / API esperada | AS-IS |
|---|---|---|
| D11/D12 producto con maestro | `/comercial/ordenes-venta` | Cumple |
| D13 factura desde OV | `convertirDocumento` + emitir precarga | Cumple vía OV; emitir directo no |
| VEN-002 emisión dedicada | `/comercial/emitir` | Cumple pero sin catálogo |
| VEN-007 cuenta por ítem ventas | emitir paso 2 | Cumple |
| D16 no bajo costo | `assertLineasMaestro` en PRODUCTO | **No aplica** a líneas SERVICIO en emitir |

---

## 5. Conclusiones

1. **Reu6 no invalida Reu5 en bloque:** sobrescribe sobre todo el **modelo comercial de ventas con stock** (cotización ventas → OV + inventario) y el **modelo de aprobaciones** (cadena automática vs picker).
2. El **texto libre en emitir no es un bug de regresión** sino **deuda de diseño** entre el wizard Reu5 y el canal OV Reu6.
3. Cerrar el gap no es solo «poner un combo»: requiere regla de negocio (qué puede emitirse directo), reutilización del stack OV en front, y endurecer `assertLineasMaestro` / tipos de documento en back.
4. Para demo: **no mostrar emitir como vía para productos de bodega**; usar OV end-to-end hasta GoSocket esté listo.

---

## 6. Referencias

- Minuta Reu5: `docs/erp-planificacion/agrosoft-levantamiento/reunion5-minuta-2026-08-03.md`
- Minuta Reu6: `docs/erp-planificacion/agrosoft-levantamiento/reunion6-minuta-2026-08-06.md`
- AS-IS previo: `docs/erp-planificacion/agrosoft-levantamiento/qa/resultados/2026-08-14-fase1-as-is-to-be.md`
- BPMN AS-IS actualizado: `2026-08-14-flujo-negocio-actual.md` (mismo directorio)
