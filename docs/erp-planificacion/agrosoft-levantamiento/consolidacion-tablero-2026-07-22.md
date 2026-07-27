# Consolidación proyecto ERP Almahue — 22/07/2026

**Para:** reunión de seguimiento (mañana)  
**Tablero:** [Almahue ERP](https://trello.com/b/wixKcrP0/almahue-erp)  
**Respaldo Trello:** `backups/trello-wixKcrP0-2026-07-22_1401.json` (+ `.md`)  
**Video:** [tl;dv](https://tldv.io/app/meetings/6a60394d4959970013159ad2)

---

## 1. Fuentes cruzadas

| # | Fuente | Rol |
|---|---|---|
| A | Transcripción + capturas `pantallas-legacy/` | Verdad de lo **dicho/mostrado** en demo Agrosoft |
| B | `resumen-trello-70.txt` (informe enviado) | Primer mapeo a ~70 tarjetas — **no canónico solo** |
| C | `auditoria-calidad.txt` (corrección enviada) | Corrige alucinaciones/omisiones/timestamps del informe |
| D | `00-decisiones.md` + `modulos/*.md` + `matriz-trazabilidad.csv` | **Canónico** post-auditoría |
| E | PDFs Enterprise Contable + Comercial (Downloads) + Gantt HTML | Plan “Enterprise” 6 meses (otro eje) |
| F | PDF MarketManager + API Export Manager China | Productos hermanos / no son Agrosoft |
| G | Código `ERP/erp_back` + `ERP/erp_front` | Estado real de implementación |

---

## 2. Qué quedó alineado (consenso)

Objetivo cliente: **“Agrosoft 3.0”** — mismos flujos operativos, validaciones/UX corregidas.

**Orden de negocio (reunión):**  
Login/empresa → Contratistas (tarifas) → Compras servicios (sin solicitud) → Insumos/Bodega → Contabilidad (plan, carga masiva, BC) → Tesorería ligera.

**Decisiones firmes (DEC-01…10):** ver `00-decisiones.md` (Mano de Obra OUT, sin Solicitud Compra, aislamiento empresa, Intermedio, monedas CLP/USD/CNY/EUR, BC, compras≠insumos, sesiones, AlmaWeb/BI, Maquinaria OUT v1).

**Implementación real hoy (UAT):**
- Login + Admin (empresas/usuarios/roles)
- Contratistas listado + **tarifas multi-línea** (Labor/Actividad, CC empresa, vigencia, delete)
- Listado CC por empresa activa

**Mock UI alineado al sidebar Agrosoft** (no persiste): Compras, Bodega, Contab, Tesorería, Proforma, Traspaso.

---

## 3. Inconsistencias / conflictos (llevar mañana)

### CONF-01 — Dos roadmaps distintos
| Eje Enterprise (PDF + Gantt) | Eje reunión Agrosoft 22/07 |
|---|---|
| Comercial, cotizaciones, GoSocket/DTE, presupuestos, workflow genérico | Contratistas → OC servicios → Bodega → Contab BC |
| Gantt en QA Almahue (#2) | Comercial/GoSocket movidos a **Fuera reunión / OUT** en Trello |

**Pregunta:** ¿Replanificamos Gantt a Agrosoft 3.0, o mantenemos **dos tracks** (ops agrícolas ahora + comercial Enterprise después)?

### CONF-02 — Informe 70 tarjetas vs auditoría
El informe enviado tenía alucinaciones corregidas (ej.):
- Maquinaria con prorrateo/desgaste **no demo**
- Dashboards Gestión inventados
- FIFO/LIFO **no pedido**
- “Por hectárea” sobre-especificado
- Timestamps incorrectos en varios ítems  

**Canónico = módulos MD + matriz**, no el Word de 70 cards sin la auditoría.

### CONF-03 — MarketManager / Export Manager vs ERP Agrosoft
PDFs en raíz del repo son **otros productos**. No mezclar alcance en el mismo sprint sin decisión explícita.

### CONF-04 — Presupuestos / reporte ejecutivo
En Enterprise = módulo. En reunión = OUT / Power BI (Mario agosto). Trello: movidos a OUT.

### CONF-05 — Centros de costo
Listado real OK; **alta desde UI catálogo aún no persiste** (API POST existe). No vender como CRUD 100% en UAT.

### CONF-06 — Fecha reunión en docs
README dice demo `2026-07-21`; compromiso/auditoría `2026-07-22`. Unificar con cliente (mismo video tl;dv).

---

## 4. Dudas / validaciones para mañana

Compromisos que **el cliente** traería (ya en `preguntas-proxima-reunion.md`):
1. Proforma + factura contratistas (área agrícola)
2. Ejemplos NC con diferencia por precio promedio
3. Cuenta perfil **digitador** para demo
4. Cuentas contables por tipo de movimiento de bodega

### Preguntas a cerrar

| # | Tema | Impacto |
|---|---|---|
| 1 | ¿Confirmamos **eliminar Solicitud de Compra**? (DEC-02) | Compras |
| 2 | Afecto/Exento: ¿quitar de OC o matching rígido? Mixtas + combustible (PEND-01) | Compras/Registro |
| 3 | ¿Múltiples facturas parciales por contrato? (PEND-02) | C-06 cierre |
| 4 | ¿Niveles de bodega? (PEND-03, persona materiales) | Insumos |
| 5 | Maquinaria: ¿OUT v1 confirmado? (DEC-10) | Scope |
| 6 | AlmaWeb: ¿integrar / reemplazar / convivir? | Arquitectura |
| 7 | Con Mario: ¿qué KPIs mínimos en ERP vs solo Power BI? | Panel |
| 8 | ¿Dónde es verdad el TC productores (recepción vs tesorería)? | Compras/Tesorería |
| 9 | ¿1 sesión/usuario obligatoria pese a costo licencias? (DEC-08) | Auth |
| 10 | **¿Gantt Enterprise se reescribe o convive?** (CONF-01) | Planificación |
| 11 | ¿GoSocket/DTE entra en v1 Agrosoft o queda diferido? | Integraciones |

---

## 5. Cambios hechos en Trello

### Primera pasada (detalle interno)
Respaldo + tarjetas DEC/PEND/alcance (luego archivadas para no saturar al cliente).

### Segunda pasada (tablero cliente — aplicar lineamientos)
1. **Columnas originales** restauradas (`Pendiente` → … → `En producción`). Listas extras archivadas.
2. **Fase F1 Gantt:** 25 mocks restaurados en **En desarrollo** con etiqueta **MockUp**.
3. **Carta Gantt** limpia en **En QA Almahue**.
4. Etiqueta **Correcciones reunión 1** (naranja): 6 tarjetas resumidas en **Pendiente** (alineadas a FB-ACTA del Gantt).
5. Etiqueta **Planificación interna**: detalle DEC/PEND/alcance **archivado** (sigue en el board archivado + docs locales).
6. Canónico interno sigue en `modulos/*.md` + este archivo.

---

## 6. Cómo probar mañana / esta semana (interno)

Ver guía UAT en chat previo. Prioridad:
1. `/contratistas/tarifas` (multi-línea, CC, labor/actividad)
2. `/contratistas` (vigencia)
3. Login + empresa + admin
4. Resto = mock (no esperar persistencia)

Login demo: `admin@almahue.local` / `Admin123!` · Front `:5174` · API `:3001/api/v1`
