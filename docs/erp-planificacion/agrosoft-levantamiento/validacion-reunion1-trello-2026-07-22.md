# Validación Reunión 1 vs tablero Trello — 22/07/2026

**Fuente canónica:** `matriz-trazabilidad.csv`, `00-decisiones.md`, transcripción interna  
**Tablero:** [Almahue ERP](https://trello.com/b/wixKcrP0/almahue-erp)

---

## Resultado general

| Categoría | Cantidad | Estado |
|---|---|---|
| REQ matriz (C/P/I/K) | 26 | 22 con card/comentario · 4 parciales |
| DEC firmes | 10 | 10 reflejadas en comentarios |
| PEND cliente | 4 | 4 mencionadas donde aplica |
| OUT (Gestión/BI/Maquinaria) | 2 | Correctamente excluidas de etiqueta Reunión 1 |
| Pantallas nuevas (fuera Gantt F1) | 9 | 9 creadas con capturas legacy donde existían |

**Veredicto:** el tablero es **coherente en ~85%** con lo hablado. Los comentarios en mocks Gantt F1 y las 9 tarjetas nuevas cubren el flujo operativo acordado (Contratistas → Compras servicios → Bodega → Contabilidad BC). Quedan **4 ítems REQ** sin tarjeta dedicada ni comentario explícito (ver gaps).

---

## Coherente ✓

### Contratistas (C-01…C-07)
- **Login/empresa** (#1): selector, empresa visible, DEC-08 sesiones compartidas.
- **Roles** (#6): Admin / Digitador / Intermedio, auditoría permisos.
- **CC** (#9): solo empresa activa, vigencia — alineado C-04 / DEC-03.
- **Contratistas** (#18): CRUD, labor/actividad en contratistas (DEC-01), enlace a tarifas.
- **Tarifas** (card nueva #60): C-03 multi-línea, bug legacy, captura `03-tarifas-contratista.png`.
- **Proformas** (#61): C-06, bloqueo cierre, compromiso cliente ejemplos.
- **Traspaso/cierre** (#62): C-07, monedas PX/USD/CNY/EUR, solo Admin.

### Compras (P-01…P-08)
- **OC servicios** (#63): sin solicitud (DEC-02), distribución CC P-03, capturas OC + CC.
- **Recepción** (#64): P-07, TC productores.
- **Registro compra** (#65): P-08 anti-cruzado, PEND-01 Afecto/Exento.
- **Aprobaciones** (#24): P-06 badge pendientes (no confundir con workflow genérico Gantt).

### Insumos / Bodega (I-01…I-05)
- **Catálogo insumos** (#19): P-02 maestro anti-duplicado, DEC-07 compras≠insumos.
- **Bodegas** (#66): I-01 por empresa activa.
- **Movimientos/NC** (#67): I-04 movimientos, I-05 NC a precio factura (sin FIFO/LIFO).

### Contabilidad (K-01…K-05)
- **Plan de cuentas** (#11): K-01 flags CC/área/especie/variedad/elemento.
- **Asientos** (#12): K-04 carga masiva (comentario; captura legacy pendiente adjuntar).
- **Indicadores BC** (#68): K-05 / DEC-05 / DEC-06.

### Infra / multiempresa
- **Empresas** (#4), **Usuarios** (#5), **Monedas** (#7): DEC-03, DEC-05, ~15 usuarios.
- **Panel** (#3): KPIs operativos post-demo (síntesis válida; no inventa Power BI — referencia G-01 OUT).

### Correctamente sin etiqueta Reunión 1
Mocks Gantt F1 **comercial/Enterprise** (#20–23, #25–26, #16–17): no salieron en demo Agrosoft — coherente con DEC-09 y track Enterprise separado.

---

## Gaps (parcial o ausente)

| ID | Tema reunión | Estado en Trello | Acción recomendada |
|---|---|---|---|
| **P-05** | Informe OC por proveedor (contabilizadas, orden reciente→antigua) | No hay card ni comentario | Comentario en **OC servicios** (#63) o mock futuro |
| **I-03** | Param. contabilización movimientos bodega + complementarios | Solo implícito en Movimientos (#67) | Comentario en **Movimientos** (#67) o card param. |
| **K-02** | Elementos de costo: anular sin borrar + asociar depto | No mencionado | Comentario en **Plan de cuentas** (#11) |
| **K-03** | Historial factores honorarios | No mencionado | Comentario en **Plan de cuentas** (#11) |
| **K-04** | Carga masiva | Comentario en #12 OK | Adjuntar `14-carga-masiva.png` a **Asientos** |
| **I-02** | Niveles almacenamiento | PEND-03 — sin pantalla | Solo registro en tarjeta índice (pendiente cliente) |
| **X-01 / G-01** | Maquinaria / Gestión Power BI | OUT v1 | Panel #3 y tarjeta índice — no requieren mock |

---

## Decisiones y pendientes en tablero

| Tipo | IDs | ¿Reflejado? |
|---|---|---|
| DEC | DEC-01…10 | Sí, en comentarios de mocks/cards nuevas |
| PEND | PEND-01…04 | PEND-01 en Registro compra; PEND-02 Proformas; PEND-03/I-02 índice; PEND-04 índice |
| OUT | G-01, X-01 | Sin etiqueta Reunión 1 en mocks comerciales |

---

## Compromisos cliente (próxima reunión)

1. Ejemplos proforma + factura contratistas (área agrícola) → card **Proformas** (#61)
2. Ejemplos NC con diferencia precio promedio → card **Movimientos/NC** (#67)
3. Validar niveles almacenamiento (materiales) → PEND-03
4. Mario / AlmaWeb / dashboards — agosto → G-01 OUT

---

## Tarjeta índice Trello

Registro oficial en tablero: **«Reunión 1 - Registro demo (22/07/2026)»** (lista En QA Almahue).  
Plantilla: `reunion1-registro-trello-template.md`
