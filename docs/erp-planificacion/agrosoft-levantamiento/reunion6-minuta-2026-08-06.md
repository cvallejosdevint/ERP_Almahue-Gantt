# Reunión 6 — Minuta de avances (06/08/2026)

**Tipo:** Demo avance ERP Almahue (interfaz + BD; reportería/cálculos en afinación)  
**Participantes:** Carlos Vallejos (Devint), Sergio (Devint), María Jesús (Almahue), Agustín (Almahue), Mario (Almahue, conectividad intermitente), equipo Almahue  
**Presentación:** Carlos · Apertura: Sergio  
**Grabación:** Sí (referencia interna Devint / usuario Cursor)

| Fuente | Ubicación |
|---|---|
| Transcripción | [`fuentes/transcripcion-reunion6.md`](fuentes/transcripcion-reunion6.md) |
| Video | Grabaciones locales (usuario Cursor) — no versionado en git |

**Próxima reunión:** jueves siguiente, mismo horario (bloqueado recurrente).  
**Entrega intermedia:** lunes — mini review Carlos ↔ MJ (~5–10 min): login, credenciales, diseño nuevo.

---

## 1. Resumen ejecutivo

Demo transversal del ERP publicado en ambiente de prueba: login, administración (empresas, usuarios, roles, reglas de aprobación), parametrización, plan de cuentas, comercial (cotizaciones), compras pendiente de recorrido completo. Integración **GoSocket** en curso; credenciales API pendientes (reunión **lunes** con Pablo). Publicación al host para exploración Almahue **al día siguiente** de la reunión.

Decisiones fuertes: **ficha única** cliente/proveedor, **órdenes de venta** (renombrar/mover flujo comercial mal ubicado), **aprobaciones por organigrama y montos** (propuesta pendiente), SSO **Microsoft** como mejora futura, PIN/aprobador desacoplado del checkbox de rol (ver implementación post-reunión).

---

## 2. Decisiones de producto

| # | Decisión | Implicancia |
|---|---|---|
| D1 | Administración usuarios **desde el ERP** (no solo ambiente dev); multi-empresa por usuario | Panel Admin › Usuarios; empresa activa en header aísla datos entre usuarios |
| D2 | **Super admin** ve todas las empresas y puede aprobar cualquier pendiente (con advertencia si no es el asignado) | Rol master no editable en permisología |
| D3 | Permisos **por rol**, no por empresa; si hace falta variación → **rol por empresa** | No permisología duplicada por empresa en mismo rol |
| D4 | Reglas de aprobación (Admin › Aprobaciones): pool de jefes por módulo/monto; **1 firma** al solicitar | Compras OC, Contratistas proformas, Comercial (reservado) |
| D5 | Quitar checkbox **«Aprobar con PIN»** del mantenedor de roles (implementación antigua) | PIN ligado a **designación en reglas de aprobación**, no al rol |
| D6 | **Propuesta pendiente:** cadena de aprobación por **montos + línea de mando / organigrama** | No elegir libremente aprobador ajeno al área; escalamiento si monto excede facultad; suplencia vacaciones |
| D7 | Proveedores y clientes: **bases separadas**; consulta RUT unificada (sociedad / proveedor / cliente / productor) | Listados limpios; lookup por RUT |
| D8 | **Ficha única** cliente/proveedor: datos bancarios (N cuentas/monedas), contactos, direcciones despacho | Pestañas en mantenedor; trazabilidad en datos críticos |
| D9 | Plan de cuentas: atributos por cuenta (CC, elemento costo, área negocio) según Excel MJ | No solo clasificación; flags activo/inactivo |
| D10 | Cuenta contable: **no eliminar** si tiene movimiento; preferir **inactivar** | Evitar pérdida histórica; revisar si rename propaga a histórico |
| D11 | «Cotizaciones» en menú Ventas → renombrar/mover a **Orden de venta** (panel comercial/compras según acuerdo final) | MJ: ventas no cotizan; Agustín: proforma/orden previa a factura |
| D12 | Orden de venta: tipo **producto** (catálogo bodega + bodega + stock) o **servicio** | Producto enlazado a inventario; servicio sin stock |
| D13 | Movimiento inventario en **nota/orden de venta**; factura trae cantidad/descripción, **precio editable** | Margen distinto al costo bodega |
| D14 | Stock ventas **solo positivo** (real, no tránsito de venta) | Tránsito solo en bodega |
| D15 | Multi-bodega: elegir bodega(s) y cantidades; no vender sobre stock | Propuesta UI selector con stock por bodega |
| D16 | No vender **bajo costo** (parametrizable; excepción = merma) | Precio mínimo = costo en mantenedor producto |
| D17 | Recargos/flete → **línea adicional**, no recargo SII en detalle | Sin impuestos adicionales |
| D18 | Diseño documentos (OC/cotización): **configurable por cliente** con preview | Ya maquetado; GoSocket bloquea emisión real |
| D19 | SSO **Microsoft** (Entra): incorporar; redirect + Tenant/Client ID de IT Almahue | Botón deshabilitado hasta credenciales `.env` |
| D20 | Ambiente publicado: datos de prueba + parametrizaciones; **pueden cargar datos reales** en fase piloto | Proceso compra/venta end-to-end para feedback |

---

## 3. Temas diferidos / propuesta pendiente

| Tema | Responsable | Nota |
|---|---|---|
| Cadena aprobación multi-nivel + organigrama + suplentes | Devint (propuesta visual) | Agustín + MJ; incluye anti-«trampa» entre áreas |
| Traspaso gastos **próxima temporada** (cuenta puente / activación) | Producto + MJ | Presupuesto mayo; no bloqueante demo |
| Emisión DTE real | GoSocket + Devint | Credenciales lunes; stub PDF hasta entonces |
| Carga masiva histórica DTE | MJ ↔ Acepta | En curso |
| Contabilidad + Tesorería (demo completa) | Siguiente reunión | Tiempo insuficiente 06/08 |
| Inventario / insumos (demo profunda) | Siguiente reunión | Fuera alcance presentación parcial |

---

## 4. Action items

### Devint (Carlos / Sergio)

| # | Acción | Prioridad |
|---|---|---|
| 1 | Publicar build en host Almahue + credenciales exploración | Alta |
| 2 | Quitar PIN del rol; PIN solo para aprobadores en reglas (+ Admin master) | Alta |
| 3 | Documentar / implementar SSO Microsoft (botón disabled hasta env) | Media |
| 4 | Propuesta **organigrama + montos + escalamiento** aprobaciones | Alta |
| 5 | Renombrar/mover flujo «cotizaciones» → **orden de venta** | Alta |
| 6 | Ficha cliente/proveedor (bancos, contactos, despacho) | Alta |
| 7 | Plan cuentas: flags CC/elemento/área negocio + solo inactivar | Media |
| 8 | Selector producto + bodega + stock; regla precio ≥ costo | Media |
| 9 | Integrar GoSocket post-credenciales lunes | Alta |
| 10 | Mini review lunes con MJ (login, credenciales) | Alta |
| 11 | Actualizar Trello con ítems nuevos | Media |
| 12 | Diseño editable OC/cotización — mostrar cuando GoSocket disponible | Media |

### Almahue

| # | Acción | Quién |
|---|---|---|
| 1 | Reunión credenciales GoSocket (Pablo) — **lunes** | MJ |
| 2 | Coordinar carga masiva Acepta | MJ |
| 3 | Explorar ERP publicado; crear usuarios; feedback módulos | Equipo |
| 4 | Enviar definición organigrama / montos aprobación (borrador) | Agustín / MJ |
| 5 | Excel plan cuentas (atributos CC/elemento/área) — ya compartido parcial | MJ |

### Calendario

| Fecha | Evento |
|---|---|
| Lunes post 06/08 | Mini review MJ ↔ Carlos; credenciales GoSocket |
| Martes | MJ operación (ausente oficina); diseño presencial temporada (mencionado) |
| Jueves | Reunión avance semanal (mismo slot) |
| Pre-temporada | Reuniones presenciales + prueba de fuego producción |

---

## 5. Notas de conectividad

Mario / Agustín con problemas de audio e internet durante la demo (cámara apagada mejoró). No afecta decisiones registradas; módulos finales (compras completo, contabilidad, tesorería) quedaron para siguiente sesión.
