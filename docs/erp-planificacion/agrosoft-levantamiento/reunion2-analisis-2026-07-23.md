# Reunión 2 — Análisis (23/07/2026)

**Participantes (según grabación):** María José (cliente), Rodrigo (contratistas / AgroSmart), Carlos (Devint), + mención Sergio/Agustín/Mario/Cristian GoSocket.  
**Duración video:** ~01:20:55  
**Fecha calendario:** jueves 23/07/2026  

| Fuente | Ubicación |
|---|---|
| Video local | [`fuentes/videos/reunion2-2026-07-23.mp4`](fuentes/videos/reunion2-2026-07-23.mp4) |
| tl;dv | https://tldv.io/app/meetings/6a624d3ff324400013c736cb |
| Capturas | [`pantallas-legacy/reunion2/`](pantallas-legacy/reunion2/) |
| Plan de acción | [`plan-accion-post-reunion2-2026-07-23.md`](plan-accion-post-reunion2-2026-07-23.md) |
| Gantt vs hoy | sección más abajo |

---

## 1. Resumen ejecutivo

La reunión cerró el gap pendiente de **Ventas + Tesorería**, profundizó el **dolor real de Contratistas** (AgroSoft vs referencia AgroSmart) y alineó el proceso de feedback vía **Trello + maqueta**.

Cambios de alcance / decisiones que impactan planificación:

1. **Contratistas v1** debe inspirarse en la UX de **AgroSmart** (ingreso diario, precio editable, asociar varias labores → proforma/factura), no clonar el flujo engorroso de AgroSoft.
2. **N:1 proformas → factura** y **ventanas multi-mes** son requisito (hoy AgroSoft fuerza workarounds).
3. **Tesorería** es módulo crítico: cartola PDF/Excel, conciliación usable, anticipos, diferencia TC bidireccional, reversa selectiva.
4. **Ventas (libro ventas):** reutilizar datos al reversar; eliminar “guardar” inútil; confirmar antes de grabar.
5. **PEND-03 niveles de almacenamiento = OUT** (no lo usan / no parametrizado).
6. **GoSocket 1/09** es independiente del ERP; conviene **no bloquear** ERP básico, pero sí coordinar reunión con soporte (Sergio).
7. Feedback cliente: **asíncrono en Trello** + reunión semanal **martes**.

---

## 2. Elementos de acción (compromisos)

| Quién | Acción | Cuándo | Estado doc |
|---|---|---|---|
| Agustín | Enviar Excel + PDF cartola bancaria | ASAP | Pendiente cliente |
| Mario | Lista actualizada centros de costo + elementos de costo | ASAP | Pendiente cliente |
| Equipo Dev | Actualizar capturas Trello con feedback Reu 2 | Lun–Mar | Dev |
| Carlos | Enviar link Trello + pantallas actualizadas | Lunes | Dev |
| Sergio | Coordinar GoSocket / reagendar post-ERP básico | Esta semana | Dev + comercial |
| Equipo Dev | Configurar roles Digitador / Analista / Admin | Próxima semana | Dev |
| Todos | Reunión planificación semanal | Martes próximo | Agenda |

---

## 3. Decisiones y pendientes — impacto en DEC/PEND

| ID | Antes (Reu 1) | Después (Reu 2) | Acción |
|---|---|---|---|
| PEND-01 Afecto/Exento | Abierto | Cliente indica que **sí lo vieron** (alerta afecta vs OC exento) | Documentar regla: alertar inconsistencia; cerrar detalle en mock compras |
| PEND-02 Facturas parciales / N proformas | Abierto | **Confirmado dolor:** 1 proforma/mes; no asociar 2 proformas a 1 factura; multi-mes forzado a trampa | Convertir a **REQ**: N labores/proformas → 1 factura; periodo flexible |
| PEND-03 Niveles almacenamiento | Abierto | **No usan / no parametrizado** | **OUT v1** |
| PEND-04 Maquinaria / AlmaWeb / dashboards | Abierto (Mario ago) | Sin cambio fuerte; dashboards siguen fuera | Mantener |
| DEC-04 Roles | Intermedio | Ejemplos reales: **Digitador contratistas**, **Analista**, **Admin** | Seed roles + matriz permisos |
| Nuevo | — | UX contratistas tipo AgroSmart | DEC/REQ nuevo en módulo contratistas |
| Nuevo | — | Tesorería: PDF cartola, conciliación diaria/semanal, reversa selectiva, TC simétrico | Ampliar spec tesorería (adelanta DEF-TES Gantt) |
| Nuevo | — | Ventas: reutilizar post-reversa; solo “grabar y contabilizar” | Ampliar spec comercial/ventas |

---

## 4. Requisitos nuevos / refinados por módulo

### 4.1 Contratistas (prioridad alta — cambia diseño)

**Dolor AgroSoft (evitar clonar):**

- Tarifario borra datos al agregar labores en mismo CC; refresh manual.
- Muchas pestañas / pasos repetidos; error en tarifario → volver al inicio.
- Actividades no filtradas por labor.
- Precio en control producción **no editable** (atado a tarifario) → impide control diario sin precio final.
- 1 proforma por mes; no asociar varias proformas a una factura.

**Tomar de AgroSmart (sí clonar idea UX):**

- Ingreso diario flexible con precio editable.
- Listado de labores pendientes → asociar a factura/proforma (multi-select, calce de monto).
- Flujo corto (crear proforma en minutos, no un día).

**Efecto contable confirmado:** cierre mes → asiento “facturas por recibir contratistas” vs costo mano de obra contratada (suma proformas del periodo).

Capturas: `01`…`07`, `19` en `pantallas-legacy/reunion2/`.

### 4.2 Ventas / libro ventas

- Tras reversar: poder **reutilizar datos** del documento (nuevo folio + asientos reversado/reversador).
- Confirmación al grabar documento proveniente de reversa.
- Quitar o no usar “guardar” (no aparece en reportes ni contabilidad); solo **grabar y contabilizar**.
- Búsqueda de clientes lenta/inconsistente → UX búsqueda robusta.

Capturas: `08`, `09`.

### 4.3 Tesorería (módulo crítico)

- Carga cartola: **Excel + PDF** (pedir muestras a Agustín).
- Ideal: cartola diaria/semanal → contabilizar desde cartola (fuente oficial).
- Link directo al asiento cuando hay diferencia en conciliación.
- Reversa **selectiva** de movimientos (no solo mes completo).
- Mejor búsqueda/eliminación de cartolas históricas.
- Anticipos productores: calce parcial sin traspasos manuales que ensucian.
- Diferencia TC debe calcularse en **ambos sentidos** (pago CLP/factura USD y viceversa).
- Roadmap control: nóminas de pago, por cobrar/pagar, atraso >90 días.

Capturas: `10`…`15`.

### 4.4 Roles / permisos

| Rol | Alcance mostrado |
|---|---|
| Digitador contratistas | Solo procesos diarios del módulo contratistas (+ empresas que ve) |
| Analista | Procesos diarios + informes; **sin** parametrización ni cierre de mes |
| Administrador | Todo + parametrizaciones + cierre |

UI: lista de pantallas con check lectura/escritura (mejorar mock actual de permisos string).

Capturas: `17`, `20`.

### 4.5 Catálogos / BC / seed datos

- Monedas + botón/config sync Banco Central (auto/manual, hora).
- UM, tipos documento, CC (posibilidad contacto encargado).
- Mario enviará lista CC + elementos de costo actualizada → seed día 1.

Capturas: `16`, `18`.

### 4.6 GoSocket / Acepta

- Firma propuesta → reunión soporte traspaso Acepta→GoSocket.
- Objetivo cliente: **1 septiembre** GoSocket operativo; agosto cierra en Acepta.
- ERP AlmaWeb y GoSocket **independientes**; conexión libro compras puede venir después.
- Acción Devint: Sergio coordina timing vs ERP básico (no bloquear facturación electrónica).

### 4.7 Proceso de trabajo con cliente

- Trello = canal de feedback con capturas.
- Maqueta en servidor de prueba (próximamente); mientras tanto capturas modo demo.
- Reunión semanal martes; WhatsApp para casos urgentes a grabar.
- Marcha blanca temprana en paralelo con operaciones reales (aunque no esté 100%).

---

## 5. Contraste con Carta Gantt (hoy = 23/07/2026)

Fuente: `docs/erp-planificacion/erp_gantt_tareas.csv` (escenario plan) + track Agrosoft ops.

### 5.1 Dónde debería estar el plan Enterprise

| Ítem Gantt | Fechas plan | Estado real 23/07 | Lectura |
|---|---|---|---|
| INF-01 repos | 13–14/07 | Hecho | OK / adelantado |
| INF-05/06 shell + UI | 15–21/07 | Hecho (+ demo mode) | Adelantado |
| DEF-CORE admin/RBAC | 21–23/07 | Hecho en producto | En fecha / adelantado |
| DEF-CAT catálogos | 24–27/07 | Parcial (mock + CC real) | Empieza mañana — OK |
| DEF-INSUMOS / contratistas | 30/07–03/08 | Levantamiento profundo Reu1+2; código parcial | **Adelantado en discovery** |
| DEF-TES tesorería | 06–10/08 | Discovery profundo **hoy** | **Adelantar DEF-TES** a esta semana |
| DEF-COM comercial/ventas | 04–07/08 | Discovery ventas hoy | Adelantar notas a DEF-COM |
| DEF-GOSOCKET | 10–11/08 | Cliente fija go-live DTE **01/09** | Spike/reunión soporte antes; integración ERP puede diferir |
| MOCK-* (F1) | desde 26/08 | Ya hay maqueta ~34 pantallas | **Track ops adelanta F1** |
| FB-PRES mockups cliente | 16/09 | Feedback ya activo vía Trello | Acortar ciclo feedback |
| INS-BACK / TES-BACK | oct–nov | Aún no | Mantener fechas back; no prometer GoSocket ERP en sep |

### 5.2 Tensiones a gestionar

1. **Doble track:** Gantt Enterprise (comercial/GoSocket F4–F6) vs **Agrosoft ops ahora** (contratistas, compras, tesorería). La Reu 2 refuerza el track ops; no contradice Gantt si se documenta como *adelanto de discovery + mock*, no como go-live Enterprise.
2. **GoSocket 1/09:** factible como **migración Acepta→GoSocket** sin ERP; la integración libro compras ERP puede quedar post-básico (alineado a lo dicho por MJ).
3. **Tesorería:** discovery completo antes de DEF-TES (ago) → conviene bajar a documento DEF ahora y mock TES en Trello **antes** de sept.
4. **Contratistas:** el diseño actual (proforma 1:1, tarifas rígidas) **queda corto** respecto a Reu 2 → hay que actualizar tarjetas Trello C-03/C-06/C-07 y mocks.

### 5.3 ¿Estamos de acuerdo con la Gantt?

| Área | ¿Alineado? | Nota |
|---|---|---|
| Core / login / admin | Sí | En o adelantado a DEF-CORE |
| Catálogos semana 24–27/07 | Sí | Seguir con DEF-CAT + seeds Mario |
| Mockups F1 (ago–sep) | Parcial | Ya hay mockups; Gantt se “adelantó” en la práctica |
| Tesorería / Ventas discovery | Sí, pero temprana | Incorporar a backlog ahora; back sigue en F3 |
| GoSocket ERP productivo (dic) | Sí | No confundir con go-live DTE cliente 01/09 |
| Contratistas productivos (nov Gantt) | Riesgo | Cliente pide marcha blanca temprana → priorizar C-* en sprints agosto |

**Veredicto:** la Gantt Enterprise sigue siendo válida como calendario de **implementación backend**. El trabajo actual (levantamiento + maqueta + feedback Trello) es un **adelanto correcto del track Agrosoft**. Hay que **actualizar backlog/Trello** (no la fecha de go-live 09/01) con los REQ de Reu 2, y **no comprometer integración ERP↔GoSocket para el 01/09**.

---

## 6. Qué agregar / actualizar en Trello

### Actualizar tarjetas existentes

| Tarjeta / tema | Cambio |
|---|---|
| Tarifas contratista | Precio editable en ingreso diario; no forzar tarifario previo rígido; filtrar actividad por labor |
| Proformas | Multi-labor → proforma; periodo flexible multi-mes; N proformas → 1 factura |
| Traspaso / cierre | Confirmar asiento cierre = suma proformas periodo |
| Registro compra / Afecto | Documentar alerta OC vs factura |
| Roles | Seed Digitador contratistas / Analista / Admin |
| Bodegas / niveles | Marcar niveles **OUT**; quitar del backlog activo |
| GoSocket | Nota: DTE cliente 01/09 independiente; sync ERP diferido |
| Tesorería (pagos / conciliación) | Ampliar descripción con REQ Reu 2 |
| Libro comercial / ventas | REQ reutilizar post-reversa; sin “guardar” muerto |

### Nuevas tarjetas sugeridas

1. **Ingreso diario labores contratista** (estilo AgroSmart) — pantallas nuevas
2. **Asociación masiva labores → proforma/factura** (calce monto)
3. **Carga cartola bancaria PDF/Excel** + muestras Agustín
4. **Conciliación: link a asiento + reversa selectiva**
5. **Anticipos productores — calce parcial**
6. **Diferencia TC bidireccional en pagos**
7. **Matriz roles Digitador/Analista/Admin** (capturas perfil legacy)
8. **Índice Reunión 2** (como el de Reu 1) con links + capturas

### Etiquetas

- Mantener: MockUp / Correcciones reunión / Planificación interna  
- Agregar o usar: **Correcciones reunión 2** (naranja/roja según convención ya usada)

---

## 7. Pendientes cliente (post Reu 2)

| # | Pendiente | Dueño |
|---|---|---|
| 1 | Excel + PDF cartola bancaria | Agustín |
| 2 | Lista CC + elementos de costo actualizada | Mario |
| 3 | Feedback asíncrono en Trello (cuando Carlos envíe link) | MJ + equipo |
| 4 | Confirmar disponibilidad martes (planificación semanal) | MJ |
| 5 | Avance firma propuesta GoSocket / fecha reunión soporte | MJ → Cristian; Devint (Sergio) |

**Cerrados en esta reunión (antes pendientes):**

- Proforma + flujo factura contratistas (visto con Rodrigo)
- Nota de crédito / proforma (revisado)
- Cuentas movimiento bodega (revisado)
- Niveles almacenamiento → no usan
- Perfiles digitador/analista (vistos en pantalla)

---

## 8. Capturas extraídas del video

| Archivo | Momento (approx) | Contenido |
|---|---|---|
| `01-tarifario-borrado-datos.png` | 06:05 | Bug tarifario AgroSoft |
| `02-actividades-sin-filtro-labor.png` | 10:21 | Actividades sin filtro |
| `03-proforma-borrador-folio0.png` | 14:03 | Proforma borrador |
| `04-proforma-asociacion-factura.png` | 15:38 | Asociación proforma-factura |
| `05-agrosmart-asociacion-facturas.png` | 17:24 | AgroSmart asociación |
| `06-agrosmart-ingreso-mano-obra.png` | 18:48 | Ingreso diario AgroSmart |
| `07-agrosmart-ui-amigable.png` | 24:48 | UX AgroSmart |
| `08-ventas-no-editar-post-reversa.png` | 28:09 | Limitación ventas |
| `09-ventas-guardar-sin-utilidad.png` | 34:38 | Guardar vs grabar |
| `10-tesoreria-calce-pagos.png` | 35:37 | Calce pagos |
| `11-tesoreria-carga-cartola.png` | 40:48 | Carga cartola |
| `12-tesoreria-conciliacion-diferencias.png` | 42:29 | Conciliación |
| `13-tesoreria-reversa-mes-completo.png` | 46:44 | Reversa mes |
| `14-anticipos-productores.png` | 50:20 | Anticipos |
| `15-diferencia-tc-pesos-dolar.png` | 54:38 | Diferencia TC |
| `16-erp-maqueta-modo-demo.png` | 57:07 | Maqueta ERP |
| `17-roles-permisos-configurables.png` | 59:53 | Roles |
| `18-catalogos-centros-costo.png` | 01:06:40 | Catálogos CC |
| `19-contratistas-tarifas-real.png` | 01:08:21 | Contratistas maqueta |
| `20-perfil-digitador-analista.png` | 01:18:27 | Perfil analista/digitador |
