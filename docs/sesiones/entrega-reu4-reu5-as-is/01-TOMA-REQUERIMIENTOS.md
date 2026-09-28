> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: minuta Reu6 + [`qa/HUERFANOS-H1-H14.md`](../qa/HUERFANOS-H1-H14.md). Motivo: paquete 06/08 pre-OV unificado y pre-pipeline v2.

# Toma de requerimientos — ERP Almahue (Reu4 → Reu5)

**Fecha:** 2026-08-06  
**Ancla:** Reu4 `transcripcion-reunion4.md` L250–266 — ERP = única plataforma; GoSocket transparente.

**Prioridad:** Must = decisión bloqueante · Should = pedido fuerte · Could = 2ª etapa / nice-to-have  
**Estado AS-IS:** Implementado · Parcial · No · Diferido

---

## 0. Integración GoSocket (INT)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| INT-GOSOCKET-001 | Usuario trabaja **solo en el ERP**. GoSocket emite DTE al SII de forma transparente bajo “Grabar y contabilizar”. | reu4:L250–266 | Must | **Diferido** (sin código DTE; diseño canónico) |
| INT-GOSOCKET-002 | Folio DTE lo entrega el facturador (GoSocket); no lo inventa el digitador. | reu4:L280–282 | Must | **Diferido** (folio local provisorio) |
| INT-GOSOCKET-003 | Cuenta contable y CC **no** se envían a GoSocket; solo ERP/asiento. | reu4:L300–302 | Must | **Implementado** (regla de diseño; CC ventas no obligatorio Reu5) |
| INT-GOSOCKET-004 | Preview borrador con marca de agua; PDF timbrado = GoSocket post emisión. | reu4:L266–268 | Must | **Parcial** (preview local OK; PDF timbrado Diferido) |
| INT-GOSOCKET-005 | Timeline negocio: Acepta→GoSocket ago/sep; portal puede ir primero; ERP después. | reu4:L154–176 | Must | N/A (negocio) |
| INT-GOSOCKET-006 | Marcha blanca espejo Agrosoft↔ERP ~2 meses. | reu4:L180–186 | Must | N/A (operativo) |
| INT-GOSOCKET-007 | GoSocket alimenta documentos recibidos (compras) con vencimiento proveedor. | reu4:L632–636 | Should | **Diferido** |
| INT-GOSOCKET-008 | No existe panel “admin GoSocket”; como mucho consulta. | reu3:L213 | Should | **Implementado** (sin panel falso) |
| INT-GOSOCKET-009 | Asociar factura proveedor (GoSocket) a proformas. | reu3:L119–121 | Should | **Parcial** (factura N:1 interna; sin GoSocket) |
| INT-GOSOCKET-010 | Config SII “para GoSocket” no fantasear hasta docs. | reu5:L297 | Could | **Diferido** (Config SII = cuentas ERP) |

**Contradicción resuelta:** Reu2 hablaba de plataformas independientes. **Vigente = Reu4:** una plataforma ERP.

---

## 1. Administración (ADM)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| ADM-001 | Roles: usuarios asociados + salto a cambio de rol | reu4:L22 | Should | Parcial |
| ADM-002 | Búsqueda de roles | reu4:L22 | Should | Parcial |
| ADM-003 | Eliminar rol con usuarios → obligar reasignación | reu4:L26–28 | Must | Parcial |
| ADM-004 | Roles temporales creables/eliminables | reu4:L28 | Should | Implementado |
| ADM-005 | Selector permisos por módulo (todas/parcial) | reu4:L28 | Should | Implementado |
| ADM-006 | Plantilla documentos por empresa (logo, pie) | reu4:L28–30 | Should | Implementado |
| ADM-007 | Reglas de aprobación (módulo, N aprobadores) | reu4:L30 | Must | Implementado |
| ADM-008 | Aprobar con PIN por rol; PIN **por usuario** | reu5:L11–31 | Must | Implementado |
| ADM-009 | Cambiar PIN exige **password de cuenta** (correo diferido) | reu5:L47–53 | Must | Implementado |
| ADM-010 | Usuario elige empresa(s) de acceso | reu5:L37 | Must | Implementado |
| ADM-011 | Modelo ALM servicios / AlmaWeb exportación | reu4:L598–600 | Must | Modelo (parametrización) |

---

## 2. Contratistas (CON)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| CON-001 | CC scoped a empresa topbar (sin columna empresa) | reu4:L34–80 | Must | Implementado |
| CON-002 | CC + labores filtrados por empresa | reu4:L34–36 | Must | Implementado |
| CON-003 | Tarifas contratista/labor/UM/CC/vigencia | reu4:L84 | Must | Implementado |
| CON-004 | Proforma: solicitar → pendiente → aprobar/rechazar | reu4:L84–88 | Must | Implementado |
| CON-005 | Solicitante elige aprobador | reu5:L59–69 | Must | Implementado |
| CON-006 | Admin aprueba “por otro” con advertencia | reu4:L88; reu5:L71–79 | Must | Implementado |
| CON-007 | Inbox/contador aprobaciones | reu4:L88 | Should | Parcial |
| CON-008 | Proforma aprobada: no editar; solo asociar factura; reverso+PIN | reu4:L88–116 | Must | Implementado |
| CON-009 | PIN/clave reverso por usuario | reu4:L110–114 | Must | Implementado |
| CON-010 | Editar post-aprobación vuelve a autorización | reu3:L123–131 | Must | Implementado |
| CON-011 | Multi-proforma → 1 factura | reu3:L135–139 | Should | Implementado |
| CON-012 | Estados borrador/definitiva/facturada | reu3:L117 | Must | Implementado |
| CON-013 | Traspaso/cierre por periodo header + histórico | reu4; minuta R5 | Must | Implementado |
| CON-014 | Aprobación con PIN | reu5:L57–81 | Must | Implementado |

---

## 3. Compras (COM)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| COM-001 | OC con estados borrador→aprobado→recepcionado… | reu4:L122 | Must | Implementado |
| COM-002 | Aprobación ≠ recepción (pueden ser distinto mes) | reu4:L132–138 | Must | Implementado |
| COM-003 | Factura compra enlaza OC aprobadas y recepcionadas | reu4:L126–134 | Must | Implementado |
| COM-004 | Impresión OC detalle completo | reu4:L122 | Should | Parcial |
| COM-005 | CC **por ítem** en OC | reu5:L81–82 | Must | Implementado |
| COM-006 | OC: cuenta, CC, elemento costo | reu3:L215 | Must | Implementado |
| COM-007 | Totales neto + impuestos | reu3:L219 | Should | Implementado |
| COM-008 | Alerta afecto/exento OC vs factura | reu2:L421 | Should | Implementado |
| COM-009 | Libro compras totalizado | reu5:L97–113 | Must | Implementado |
| COM-010 | Resumen colapsable por tipo (NC restan) | reu5:L99–113 | Must | Parcial (panel; tipificación compras a reforzar) |
| COM-011 | Emisión/detalle redimensionable | reu5:L83–95 | Should | Implementado (panel + resize) |
| COM-012 | Productores fuera de menú Compras | reu5:L263–265 | Must | Implementado |
| COM-013 | Facturas recibidas con CC | reu5:L229 | Must | Implementado |

---

## 4. Ventas / Comercial (VEN)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| VEN-001 | Libro ventas = emitidos/contabilizados | reu4:L216–240 | Must | Implementado |
| VEN-002 | Emisión fuera del libro (pantalla dedicada) | reu4:L308–320 | Must | Implementado |
| VEN-003 | Borrador → Grabar y contabilizar (= emitir + asiento) | reu4:L250–264 | Must | Parcial (sin DTE GoSocket) |
| VEN-004 | Reverso = solo contable (CC/cuenta); no anula DTE | reu4:L214–240 | Must | Implementado |
| VEN-005 | Anulación tributaria = NC | reu4:L202–216 | Must | Implementado |
| VEN-006 | Folio clickeable → preview; borrador con watermark | reu4:L266–268 | Must | Implementado (PDF timbre Diferido) |
| VEN-007 | Imputación cuenta en emisión | reu4:L270–308 | Must | Implementado |
| VEN-008 | Ventas **sin CC obligatorio**; compras con CC | reu5:L229 | Must | Implementado |
| VEN-009 | Neto / exento / IVA; desc. global y línea | reu5:L221–227 | Must | Implementado |
| VEN-010 | Reenvío PDF+XML | reu4:L312–314 | Should | Diferido (SMTP/GoSocket) |
| VEN-011 | Totalizado tipo RCV | reu4:L324–330 | Must | Implementado |
| VEN-012 | Descargar libro Excel | reu4:L320 | Must | Implementado |
| VEN-013 | Despachos/guías → bodega, no libro ventas | reu4:L142–152 | Must | Parcial (API guías; sin UI) |
| VEN-014 | Libros compras/ventas independientes | reu5:L157–159 | Should | Implementado |
| VEN-015 | Bandeja borradores en emisión | reu5:L161–165 | Must | Implementado |
| VEN-016 | Borradores por usuario; admin filtra usuario | reu5:L173–257 | Should | Implementado |
| VEN-017 | Multi-periodo tope 1 año + paginación | reu5:L181–197 | Must | Implementado |
| VEN-018 | Menú acciones Better Soft | reu5:L139–145 | Should | Parcial (pago/correo/adjunto a cablear u ocultar) |
| VEN-019 | Filtros libros reformulados | reu5:L147–149 | Should | Implementado |
| VEN-020 | Panel resumen lateral colapsable | reu5:L99–105 | Must | Implementado |
| VEN-021 | Cotizaciones con registro (+ aprobación) | reu4:L334–346 | Should | Implementado |
| VEN-022 | Cotiz: emitir/anular/convertir/imprimir | reu5:L199–237 | Should | Implementado (NP→Factura UI) |
| VEN-023 | Alta cliente `+` panel derecho completo | reu5:L209–217 | Should | Implementado |
| VEN-024 | Tipos cliente export/nacional | reu4:L350–354 | Should | Parcial |
| VEN-025 | Factura exportación (aduana, puertos, SII) | reu4:L356–372 | Must | **Parcial UI** — campos COMEX en emisión + NC precarga; DTE GoSocket diferido |
| VEN-026 | NC/ND export precargadas desde factura | reu4:L374–386 | Must | Parcial |
| VEN-027 | Folio cotiz clickeable preview | reu5:L241–243 | Should | Implementado |
| VEN-028 | Vendedor = usuario sistema | reu3:L211–213 | Should | Parcial |

---

## 5. Insumos / Bodega (INS)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| INS-001 | Inventario existencias / movimientos | reu4:L400–414 | Must | Parcial |
| INS-002 | AlmaWeb bodega de paso + Excel packing | reu4:L400–418 | Must | Diferido |
| INS-003 | Flag inventariable | reu4:L412 | Must | Parcial |
| INS-004 | NC inventariable → reingreso | reu4:L390–398 | Should | Parcial |
| INS-005 | Stock fruta packing fuera ERP | reu4:L608–612 | Could | N/A alcance |
| INS-006 | Informe movimientos Excel | reu4:L716 | Should | Parcial |
| INS-007 | Guías en inventario | reu4:L150–152 | Must | Parcial (API sin UI) |

---

## 6. Contabilidad (CNT)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| CNT-001 | Plan/CC/elementos en Parametrización | reu4:L422–426 | Must | Implementado |
| CNT-002 | Periodos + cierres por módulo | reu4:L428–438 | Must | Implementado |
| CNT-003 | Periodo activo solo en header | reu5:L269–281 | Must | Implementado |
| CNT-004 | Historial abrir/cerrar; motivo al reabrir | reu5:L281–293 | Must | Implementado |
| CNT-005 | Config cuentas por tipo SII | reu4:L440–448 | Should | Implementado |
| CNT-006 | Indicadores BC automáticos | reu4:L448 | Should | Implementado |
| CNT-007 | Factor honorario por vigencia | reu4:L450–460 | Should | Implementado |
| CNT-008 | Libro diario y mayor | reu4:L462 | Must | Implementado |
| CNT-009 | Balance 8 columnas | reu4:L464–468 | Must | Implementado |
| CNT-010 | Contabilidad electrónica SII | reu4:L474–496 | Could | Diferido |
| CNT-011 | Plan 5 niveles + import Excel | reu4:L724–726 | Must | Parcial |
| CNT-012 | Contabilidad modular | reu4:L192–194 | Should | Implementado (principio) |
| CNT-013 | Asientos desde tesorería + TC | reu4:L546–576 | Must | Parcial |

---

## 7. Tesorería (TES)

| ID | Enunciado | Fuente | Prio | Estado |
|---|---|---|---|---|
| TES-001 | Flujo de caja | reu4:L504 | Must | Implementado |
| TES-002 | Cartolas Excel + calce | reu4:L506–528 | Must | **Parcial→mejorado** — parser multi-hoja MJ (ALM/Almahue/Scotia); calce base OK |
| TES-003 | Contabilizar mov cartola → asiento | reu4:L510–522 | Must | Implementado |
| TES-004 | Pagos + N° transacción cartola | reu4:L540–556 | Must | Implementado |
| TES-005 | TC auto editable + casos promedio | reu4:L558–578 | Must | Parcial |
| TES-006 | Dual moneda + diferencia TC | reu4:L570–576 | Must | Parcial |
| TES-007 | Anticipos productores/clientes | reu4:L594–600 | Must | Implementado |
| TES-008 | Aging / nóminas | reu4:L614–618 | Must | Implementado |
| TES-009 | Vencimiento doc + fecha pago operativa | reu4:L620–646 | Must | Parcial |
| TES-010 | Editar vencimiento solo rol tesorería | reu4:L642–648 | Must | Parcial |
| TES-011 | Cobranza (compromisos, mail) | reu4:L650–654 | Could | Diferido — propuesta R4-18 en [`../propuesta-modulo-cobranza.md`](../propuesta-modulo-cobranza.md) |
| TES-012 | Conciliación: pendientes + resumen | reu4:L658–674 | Must | Implementado |
| TES-013 | Estado de cuenta (ex Ctas cte) | reu4:L676–704 | Must | Implementado |
| TES-014 | Tipo movimiento + links + Excel | reu4:L696–712; reu5:L307 | Must | Implementado |
| TES-015 | Reportes preferir Excel | reu4:L708–712 | Must | Parcial |

---

## 8. Matriz REQ → pantalla/API (Must críticos)

| REQ | Pantalla / API AS-IS |
|---|---|
| INT-GOSOCKET-001..004 | Emitir + Libro + Contabilizar (rama GoSocket pendiente) |
| VEN-001..009 | `/comercial/libro`, `/comercial/emitir`, borradores |
| COM-002..005 | `/compras/ordenes`, aprobaciones, recepciones, registro |
| CON-004..014 | `/contratistas/proformas`, aprobaciones, traspaso |
| CNT-003..004 | Header periodo + `/contabilidad/periodos` |
| ADM-008..009 | Perfil PIN + roles |
| TES-002..004,012–014 | Cartolas, pagos, conciliación, estado cuenta |

---

## 9. Materiales cliente pendientes

Manual factura exportación · Excel AlmaWeb · Mayor/balance ejemplos · Excel cartolas finas MJ · Plan cuentas 5 niveles · Docs/API GoSocket (próxima entrega del cliente).
