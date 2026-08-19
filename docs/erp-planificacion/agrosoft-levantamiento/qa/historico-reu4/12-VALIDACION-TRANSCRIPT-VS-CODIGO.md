> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: minuta Reu4 editada + [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; transcripción vs código no gana a minuta + código 18/08.

# 12 — Validación Reu4: transcripción vs código

**Fecha validación:** 2026-08-03 (reloj alineado al MP4)  
**Fuente única:** [`transcripcion-reunion4.md`](../../docs/erp-planificacion/agrosoft-levantamiento/fuentes/transcripcion-reunion4.md) (30/07/2026)  
**Video:** `fuentes/videos/reunion4-2026-07-30.mp4` · tl;dv reunión  
**Código contrastado:** `ERP/erp_back` + `ERP/erp_front` (post-PIN unificado: login + PIN aprobación; sin clave de reversa separada)

Speakers: **00** Carlos · **01** María Jesús · **02** Sergio  

Timestamps = **reloj del player MP4** (corrección −5:51 vs tl;dv; ancla «invitación» = [00:40]).  
No se usaron archivos de planificación como fuente; solo la transcripción.

---

## Veredicto ejecutivo

| Bucket | Cant. |
|--------|------:|
| Cumple (aplicado en código) | ~22 |
| Parcial | ~6 |
| Pendiente Dev | ~5 |
| Diferido / externo (GoSocket, contab. electrónica, cobranza, puente PDF) | ~6 |
| Pedir a MJ esta semana | 11 materiales |

| Alcance | ¿Operativo? | Nota |
|---------|-------------|------|
| **Piloto interno** | Sí | Flujos core + oleada Reu4 cerrada en código |
| **Producción temporada** | No todavía | Inventariable/AlmaWeb, cartola Excel MJ, docs DTE, cotizaciones |

---

## Matriz ítem a ítem (transcripción → código)

### Administración / RBAC

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| A1 | Buscar rol; col. usuarios; delete con reasignación [11:09]–[27:20] | **Cumple** | `RolesPage.tsx` + `admin.service.ts` `deleteRol` |
| A2 | Selector pantallas módulo completo/parcial [27:20] | **Cumple** | Matriz R/W por módulo/pantalla |
| A3 | Plantilla docs: logo, footer, columnas [44:09] | **Cumple** | `PlantillaDocumentosPage.tsx` |
| A4 | Reglas aprobación Compras/Contratistas + jefes [44:29+] | **Cumple** | Workflow Admin + `workflowAprobacion.ts` |
| A5 | Roles temporales (vacaciones) [27:20] | **Cumple** | `rolVigenciaDesde/Hasta` + bloqueo login |
| A6 | PIN 4 dígitos (Sergio; consolidado post-reu) | **Cumple** | `Rol.aprobarConPin` + Mi Perfil + OC/proforma/reversa (mismo PIN) |

### Centros de costo / contratistas

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| C1 | CC solo de empresa seleccionada; sin col. empresa [01:14:39]–[01:38:20] | **Cumple** | Listado filtrado por empresa; sin columna empresa |
| C2 | Código CC puede repetirse entre empresas [01:34:39] | **Cumple** | `@@unique([empresaId, codigo])` |
| C3 | Proforma aprobada: sin editar/eliminar; solo factura + reversa [02:28:00]–[02:59:10] | **Cumple** | Lock DEFINITIVA; reversa con **PIN** (unificado). Aprobar/rechazar: solo jefes de Admin › Workflow (analista no; sin bypass `proformas:aprobar`) |

### Compras

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| OC1 | Factura compra solo OC aprobadas **y** recepcionadas [03:26:29]–[03:32:40] | **Cumple** | Elegibles `RECEPCIONADA\|CONTABILIZADA\|FACTURADO` (excluye borrador/anulada/emitida) |
| OC2 | Print OC con detalle (faltaba en demo) [03:04:39] | **Cumple** | Print con líneas + CC |
| OC3 | Quitar “iniciar” confuso en libro compras [03:21:59] | **Cumple** | UI: «Registrar factura» / carga masiva; sin «Iniciar» |
| OC4 | Libro orientado a **factura** (no grilla liderada por OC) [03:21:30]–[03:24:20] | **Cumple** | Grilla: Factura → Proveedor → OC asociada (Vite hot-reload) |
| OC5 | Puente sin GoSocket: cargar libro compras / PDF (Acepta) [04:09:00] | **Diferido** | Solo CSV genérico de registros; sin ingestión PDF/libro Acepta |

### Ventas / DTE

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| V1 | Despachos / tab Compras fuera del libro ventas [03:45:30]–[03:49:20] | **Cumple** | Sin tabs Despachos ni Compras; solo ventas + nota a Insumos / Libro compras |
| V2 | Libro = emitidos/contabilizados; reverso = modificación contable, no anular SII [05:00:40]–[05:22:40] | **Cumple** | Reverso contable + re-contabilizar |
| V3 | Quitar Emitir del libro [05:58:49]–[06:39:00] | **Cumple** | Emisión en menú aparte |
| V4 | Cuenta + CC en emisión (detalle) [06:03:00]–[06:24:20] | **Parcial** | `EmitirDocumentoPage.tsx`: cuenta/CC a **nivel documento** al contabilizar; transcript pide **por línea de ítem** |
| V5 | Folio → representación gráfica + watermark BORRADOR [05:49:00]–[05:57:49] | **Cumple** | Print con `forceWatermark: BORRADOR` |
| V6 | Totales tipo RCV [06:42:00]–[06:47:10] | **Cumple** | Cards Documentos/Neto/IVA/Exento/Total |
| V7 | Reenvío PDF/XML desde libro [06:30:50] | **Diferido** | Depende docs GoSocket; integración removida a propósito |
| V8 | Cotizaciones: dejar registro hasta definir flujo [06:48:30]–[07:02:20] | **Cumple (alcance)** | Sin cola de aprobación; **pregunta abierta** (MJ mute [06:55:19]) |
| V9 | Tipo cliente export/nacional; aduana/puertos [07:07:40]–[07:24:59] | **Pendiente** | Sin campos exportación en cliente/emisión |
| V10 | NC exportación precargada desde factura [07:29:40]–[07:43:09] | **Pendiente** | Post DTE |
| V11 | GoSocket [03:53:40]–[05:35:49] | **Diferido** | **Definición Sergio (canónica):** facturación **desde el ERP**; GoSocket = integración **backend** transparente que informa al **SII** (no portal como producto). Código DTE removido hasta docs oficiales. Puente portal agosto = contingencia comercial, no el diseño final |

### Insumos / inventario

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| I1 | Flag inventariable + stock en movimientos [08:17:09]–[08:20:49] | **Pendiente** | Modelo `Insumo` sin flag |
| I2 | Carga Excel AlmaWeb (cajas) [08:20:49]–[08:26:40] | **Pendiente** | Esperando Excel MJ |

### Contabilidad / parametrización

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| K1 | Plan/indicadores/elementos/CC → Parametrización; periodos en Contabilidad [08:34:00]–[08:49:50] | **Cumple** | Sidebar alineado |
| K2 | Conservar config SII [08:50:59]–[09:00:50] | **Cumple** | Panel contable SII |
| K3 | Factor honorario con vigencia/historial [09:05:19]–[09:12:20] | **Cumple** | `vigenciaHasta` + badge vigente |
| K4 | Balance 8 columnas [09:26:19] | **Cumple** | `Balance8ColumnasPage.tsx` |
| K5 | Contabilidad electrónica SII [09:38:00]–[10:09:40] | **Diferido** | 2ª etapa / certificación |
| K6 | Import plan 5 niveles [15:14:19]–[15:21:30] | **Parcial** | Import Excel + niveles en código; falta smoke con archivo MJ (dijo que está en Trello) |

### Tesorería

| # | Pedido (ts) | Estado | Cómo está hoy |
|---|-------------|--------|---------------|
| T1 | Cartola Excel → calzar/conciliar [10:22:40]–[10:49:39] | **Parcial** | Import genérico + parsers; falta Excel tipo MJ |
| T2 | Mantenedor códigos financieros [11:19:09] | **Pendiente** | Campo libre en anticipos; sin catálogo |
| T3 | TC automático + override (productores/materiales) [11:34:59]–[12:06:49] | **Pendiente / dudoso** | Ver video; no cerrado en código |
| T4 | Anticipos ALM (entregados) vs AlmaWeb (recibidos) [12:34:39]–[12:48:19] | **Parcial** | Solo anticipos productores genéricos |
| T5 | Aging: editar vencimiento solo rol tesorería [13:38:30]–[13:49:39] | **Cumple** | Gate `tesoreria:write` + historial |
| T6 | Propuesta cobranza [13:59:29]–[14:09:50] | **Propuesta** | Doc; sin UI |
| T7 | Conciliación: default pendientes + resumen cant/monto [14:14:40]–[14:23:20] | **Cumple** | KPI + tab Pendientes |
| T8 | Renombrar a Estado de cuenta; filtro Todos/Pendientes; links [14:42:00]–[15:03:29] | **Cumple** | Label + filtro + deep-links |
| T9 | Export Excel (y PDF en algunos) [15:03:29]–[15:08:20] | **Parcial** | Hay exports en varios módulos; no todos los reportes |

---

## Pedir a María Jesús esta semana

Solo lo que ella debe enviar o confirmar:

1. **[03:53:40]** Estado GoSocket: ¿conexión agosto o postergar temporada? (apretón comercial)
2. **[04:12:10]** Si GoSocket avanza: documentación oficial integración (PDF/XML/API)
3. **[07:24:59]** Manual factura exportación (+ NC/ND exportación)
4. **[07:17:30]** (si aplica) Listado puertos / país destino que usan hoy
5. **[08:20:49]** Excel inventario/seguimiento cajas AlmaWeb (ejemplo real)
6. **[09:32:09]** Libro mayor (una cuenta), balance, libro diario (aunque usen poco el diario)
7. **[10:45:00]** Excel cartola bancaria con su formato
8. **[11:01:09]** En ese Excel: marcar 1 fila conciliada vs factura + cómo quedó el asiento
9. **[15:11:00]** Listado reportes actuales + informe movimiento bodega por tipo documento
10. **[15:14:19]** Confirmar/reenviar plan de cuentas Excel 5 niveles (dijo que está en Trello)
11. **[15:28:40]** Correo Agustín + confirmar agenda jueves con Mario/Agustín

---

## Momentos dudosos — ver video (timestamps)

| Timestamp | Duda | Por qué marcar |
|-----------|------|----------------|
| **[04:06:19]–[04:18:49]** | Puente agosto: ¿portal GoSocket temporal? | Contingencia comercial; **no** redefine el diseño |
| **[05:34:40]–[05:35:49]** | ¿Facturar en GoSocket o en el ERP? | MJ duda; **Sergio aclara:** solo ERP; GoSocket debajo → SII |
| **[05:34:40]–[05:49:00]** | ¿Anulado puede existir en ERP si SII sigue válido? | Se aclara a medias (NC vs reverso contable) |
| **[05:58:49]–[06:10:09]** | Cuenta/CC: ¿por línea en emisión o solo visualizar en libro? | Pedido “por línea” vs implementación cabecera → **V4 Parcial** |
| **[06:55:19]–[07:02:20]** | Cotizaciones: ¿solo registro o aprobación jefatura? | MJ estuvo mute; respuesta ambigua → **V8** |
| **[07:55:59]–[08:26:40]** | AlmaWeb bodega de paso vs stock ALM vs packing | Alcance inventariable poco cerrado → **I1/I2** |
| **[10:28:00]–[10:39:39]** | Calce exacto cartola↔factura↔asiento | Quedó pendiente del Excel → **T1** |
| **[11:54:19]–[12:06:49]** | TC promedio productores vs BC | Sergio: “hay que dar una vuelta” → **T3** |
| **[13:25:59]–[13:37:00]** | Vencimiento documento GoSocket vs fecha operativa de pago | Impacta aging/GoSocket futuro |
| **[14:27:40]–[14:42:00]** | Qué era “cuentas corrientes” | Se reinterpreta como estado de cuenta RUT → **T8 Cumple** |

---

## Auditoría pendientes (2026-08-03)

Tras alinear reloj + re-leer transcript vs código:

- **Sin más gaps fuertes** fuera de la matriz (salvo **OC4/OC5** agregados en Compras).
- **Siguen abiertos (Dev):** V4, V9, V10, I1, I2, T2, T3 + parciales OC4, T1, T4, T9, K6.
- **Diferidos / externos:** V7, V11, K5, T6, OC5.
- **Decisión abierta:** V8 cotizaciones (MJ mute).
- **Materiales MJ:** los 11 de la lista (bloquean I2, T1, K6, V9/V10, V11).

## Prioridad Dev (si se abre oleada siguiente)

1. **OC4** — Libro compras: grilla/orden por factura (no OC primero) ([03:21:30]).
2. **V4** — Cuenta + CC por línea en emitir documento ([06:16:29]).
3. **I1/I2** — Flag inventariable + import Excel AlmaWeb (bloqueado por material MJ).
4. **T1** — Alinear import cartola al Excel MJ (bloqueado por material MJ).
5. **T2** — Mantenedor códigos financieros.
6. **V8** — Cerrar con Sergio/MJ si cotizaciones llevan cola de aprobación.
7. **V11 / V7 / V9 / V10 / OC5** — DTE / puente PDF solo con docs oficiales.

---

## Evidencia relacionada

- Ruta demo: [`11-RUTA-PRESENTACION-AJUSTES.md`](./11-RUTA-PRESENTACION-AJUSTES.md)
- AS-IS / TO-BE operativo: [`10-AS-IS-TO-BE-OPERATIVO.md`](./10-AS-IS-TO-BE-OPERATIVO.md)
- Matriz cumplimiento previa (referencia, no fuente de esta validación): [`06-MATRIZ-CUMPLIMIENTO-REU4.md`](./06-MATRIZ-CUMPLIMIENTO-REU4.md)
