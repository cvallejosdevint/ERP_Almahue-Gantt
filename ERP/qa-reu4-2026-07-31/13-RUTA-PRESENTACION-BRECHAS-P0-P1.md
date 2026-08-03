# Ruta de presentación — Avances post Reunión 4 (para Sergio)

**Fecha:** 03/08/2026  
**Audiencia:** Sergio  
**Entorno:** MODO REAL · Front `http://127.0.0.1:5174` · API `:3001`  
**Login:** `admin@almahue.local` / `Admin123!` · PIN `4821`  
**Aprobador (PIN en vivo):** `qa.aprobador@almahue.local` / `QaTest123!` · PIN `4821`

**Idea de la sala:** contar lo que **se pidió en la reunión** y mostrar que quedó hecho.  
Nombres de menú = **como se ven en pantalla** (no rutas de código).

**Datos listos (seed `prepare-demo-sergio.ts`):** OC / factura compra / venta / proformas DEMO abajo.

---

## Cómo usar (~35 min)

| Min   | Bloque                   | Eje (lo que pediste en la reu)                                                       |
| ----- | ------------------------ | ------------------------------------------------------------------------------------ |
| 0–2   | Apertura                 | Una sola plataforma; contabilidad al centro                                          |
| 2–8   | 1 · Aprobaciones         | PIN / clave por usuario; proforma bloqueada; OC                                      |
| 8–14  | 2 · Compras              | Factura solo OC aprobada **y** recepcionada; print OC; libro por factura             |
| 14–22 | 3 · Ventas               | Emisión aparte; cuenta+CC; reverso contable ≠ anular SII; folio/preview; totales RCV |
| 22–28 | 4 · Contabilidad / Param | Menú Parametrización; Balance 8 col; factor honorario                                |
| 28–33 | 5 · Tesorería            | Estado de cuenta; aging por rol; conciliación pendientes                             |
| 33–35 | Cierre                   | Diferidos (GoSocket, AlmaWeb, cartola MJ) + 1 pregunta                               |

---

## Datos de demo (no inventar en la sala)

| Pieza                         | Dato                                                  | Para qué                                      |
| ----------------------------- | ----------------------------------------------------- | --------------------------------------------- |
| OC pendiente PIN              | `OC-DEMO-PEND-01` ($850.000)                          | Compras › Aprobaciones                        |
| OC aprobada (print + CC)      | `OC-DEMO-APR-02` ($420.000)                           | Compras › Órdenes → Imprimir                  |
| OC recepcionada + factura     | `OC-DEMO-REC-03` → factura `FAC-DEMO-3001`            | Libro de compras / match                      |
| Proforma pendiente PIN        | `PF-DEMO-PEND-01`                                     | Contratistas › Proformas                      |
| Proforma definitiva (bloqueada) | `PF-DEMO-001`                                       | Mostrar que no edita / no elimina             |
| Factura electrónica venta     | Folio `88001` CONTABILIZADA (neto 1.000.000 + IVA)  | Libro ventas → preview + **Reversar**         |
| Borrador watermark            | Folio `88002` BORRADOR                                | Preview con watermark                         |
| Proveedor                     | Agro Insumos Sur                                      | Compras                                       |
| Cliente                       | Exportadora Pacífico SpA                              | Ventas / Estado de cuenta                       |
| Periodo                       | `2026-08` abierto                                     | Contabilidad                                  |

**Regenerar datos limpios:**

```bash
cd ERP/erp_back
npx ts-node -r tsconfig-paths/register scripts/prepare-demo-sergio.ts
```

---

## Apertura (decir en voz alta)

> “En la reunión acordamos el foco: ustedes trabajan en **una sola plataforma (el ERP)**; GoSocket va por debajo cuando llegue la documentación. Y que todo el movimiento termine bien en **contabilidad**, de forma modular.  
> Hoy te muestro, en el mismo orden del negocio que vimos en la reu, lo que pediste priorizar y ya está operativo.”

Anclas Reu4 (solo si pregunta):

- Una sola plataforma — Sergio [04:15:50] / [05:35:49]
- Contabilidad al centro / escalable — [04:31:29]

---

## Checklist pre-reunión (2 min)

- [ ] Nest + Vite + Postgres; **MODO REAL**
- [ ] Periodo `2026-08` abierto; empresa en el header
- [ ] Seed corrido: aparecen `OC-DEMO-*`, `88001`, `PF-DEMO-*`
- [ ] Login aprobador listo si vas a mostrar PIN en vivo
- [ ] Este doc abierto

---

# BLOQUE 1 — Aprobaciones y control

**Pedidos Reu4:** proforma aprobada sin editar; reversa con clave **por usuario**; PIN; solo el jefe aprueba; reglas en Admin.

### Dónde ir

1. **Admin › Roles** → rol con “Aprobar con PIN”.
2. **Mi Perfil** (como aprobador) → sección PIN.
3. Login `qa.aprobador@almahue.local` → **Compras › Aprobaciones** → `OC-DEMO-PEND-01` → Aprobar / Rechazar → **PIN `4821`**.
4. (Alt.) **Contratistas › Proformas** → `PF-DEMO-PEND-01` con el mismo PIN.
5. Abrir `PF-DEMO-001` (DEFINITIVA) → **no** deja editar ni eliminar.

### Narración

> “Quedó como pediste: aprobado = cerrado. Para deshacer, PIN del usuario, no una clave compartida de todo el equipo. Y aprueba el jefe de la regla, no cualquiera con permiso de escritura.”

---

# BLOQUE 2 — Compras (aprobación ≠ recepción ≠ factura)

**Pedidos Reu4:** factura de compra solo sobre OC **aprobada y recepcionada**; print con detalle; libro orientado a factura; sin “Iniciar” confuso.

### Dónde ir

1. **Compras › Órdenes de compra** → Imprimir `OC-DEMO-APR-02` → se ven **líneas** y centro de costo.
2. **Compras › Libro de compras** → ver `FAC-DEMO-3001` ligada a `OC-DEMO-REC-03` (match OK).
3. **Registrar factura** (si hay tiempo): en el selector solo OC elegibles (recepcionadas).
4. Demo negativa rápida: `OC-DEMO-PEND-01` (solo emitida) **no** sirve para facturar.

### Narración

> “Son dos procesos: el jefe aprueba; ustedes recepcionan cuando reconocen el gasto. La factura de compra solo enlaza OC que ya pasaron por ambos.”

---

# BLOQUE 3 — Ventas

**Pedidos Reu4:**

- Quitar Emitir del libro
- Emisión con cuenta + centro de costo
- Libro = emitidos/contabilizados; **reverso = modificación contable**, no anular en el SII
- Folio abre representación gráfica; borrador con watermark
- Totales tipo RCV
- Despachos **no** van en el libro de ventas

### 3.1 Emisión (menú aparte)

1. Menú **Ventas › Emitir documento** (no desde el libro).
2. Tipo en pantalla: **Factura electrónica**.
3. Completar receptor + ítems; en el detalle pedir **cuenta contable** y **centro de costo**.

### 3.2 Libro de ventas

1. **Ventas › Libro de ventas**
2. Cards de totales (Documentos / Neto / IVA / Exento / Total).
3. Click folio **`88001`** → preview / representación gráfica.
4. Folio **`88002`** → watermark **BORRADOR**.
5. Acción **Reversar** sobre `88001`:
  - *La factura electrónica no se “anula” en el SII sin NC; acá el reverso ordena la **contabilidad**; el documento tributario sigue válido hasta trabajar con nota de crédito.*
6. Confirmar que **no** hay pestañas Despachos/Compras dentro de este libro.

### Narración

> “Tal como quedó en la reu: emitir es una pantalla; el libro es para consultar, ver la representación, contabilizar y, si hace falta, reversar contablemente. La NC es el camino tributario; no inventamos una anulación SII desde el ERP.”

### Qué NO vender en este bloque

- NC automática “anular total” desde el libro (idea tuya [04:53:10], **aún no cerrada** con GoSocket/MJ).
- Folio timbrado / PDF oficial GoSocket → diferido a docs.

---

# BLOQUE 4 — Contabilidad y Parametrización

**Pedidos Reu4:** plan/indicadores/elementos/CC en Parametrización; periodos en Contabilidad; config SII; Balance 8 columnas; factor honorario con vigencia.

### Dónde ir

1. Sidebar **Parametrización** → plan de cuentas / indicadores / elementos / centros de costo.
2. **Contabilidad › Periodos** → `2026-08` abierto.
3. **Contabilidad › Balance 8 columnas** → KPIs + 8 grupos.
4. Factor honorario: vigencia / badge vigente.
5. Config contable SII (mención: listo para cuando entre GoSocket).

### Narración

> “Ordenamos el menú como pediste y el Balance de 8 columnas ya está para revisión. La contabilidad electrónica SII la dejamos en 2ª etapa, como acordamos.”

---

# BLOQUE 5 — Tesorería

**Pedidos Reu4:** renombrar a Estado de cuenta; filtro Todos/Pendientes; links; aging solo tesorería; conciliación con pendientes y resumen.

### Dónde ir

1. **Tesorería › Estado de cuenta** → filtro Todos / Pendientes → movimiento de folio `88001` (cliente).
2. **Aging** → documento `88001` por cobrar; editar vencimiento solo con rol tesorería.
3. **Conciliación** → tab/default Pendientes + resumen.
4. Cartola: *import genérico listo; el calce fino espera Excel de ejemplo (MJ)* — no alargar.

### Narración

> “Estado de cuenta por RUT, aging controlado por tesorería, y conciliación mirando primero lo pendiente — como pediste en la reu.”

---

## Diferidos (decir al cierre; no demo como listo)

| Tema                                    | Mensaje                                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| GoSocket / DTE / reenvío PDF-XML        | “Diseño: todo desde el ERP; GoSocket debajo. Código de integración a la espera de docs oficiales.” |
| NC automática desde el libro            | “Tu idea de acceso rápido queda post-definición con GoSocket.”                                     |
| Excel AlmaWeb / inventariable           | “Bloqueado por material de MJ.”                                                                    |
| Cartola Excel MJ                        | “Import base listo; falta la plantilla real.”                                                      |
| Cotizaciones con aprobación de jefatura | “Sigue abierta: ¿solo registro o cola de aprobación?”                                              |

---

## Una pregunta para Sergio (elige una)

1. ¿El match OC–recepción–factura debe **bloquear** contabilizar o solo alertar (hoy alerta)?
2. ¿Cotizaciones llevan aprobación de jefatura esta temporada o siguen solo registro/conversión?
3. Cuando llegue docs GoSocket, ¿priorizamos integración DTE o NC automática desde el libro?

---

## Cheatsheet de clicks (orden de sala)

```
Login aprobador (qa.aprobador…)
→ Compras › Aprobaciones → OC-DEMO-PEND-01 → PIN 4821
→ (opc) Contratistas › Proformas → PF-DEMO-PEND-01 / PF-DEMO-001 bloqueada
Login admin
→ Compras › Órdenes → OC-DEMO-APR-02 → Imprimir
→ Compras › Libro de compras → FAC-DEMO-3001
→ Ventas › Emitir documento → Factura electrónica (cuenta + CC)
→ Ventas › Libro de ventas → 88001 preview / Reversar · 88002 watermark
→ Parametrización + Contabilidad › Balance 8 columnas
→ Tesorería › Estado de cuenta (88001) + Aging + Conciliación
→ Cierre: GoSocket / materiales MJ / 1 pregunta
```

---

## Plan B si algo falla

| Falla                          | Qué hacer                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------- |
| No hay pendiente de aprobación | Re-correr seed; o narrar PIN en Mi Perfil + Roles                            |
| Emitir falla                   | Abrir Libro de ventas con `88001` y mostrar reverso + folio                  |
| Sin OC recepcionada            | Usar `OC-DEMO-REC-03` / `FAC-DEMO-3001` ya creados                           |
| Sin tiempo                     | Bloques 1→3 son el mínimo; 4–5 en mención                                    |

---

*Documento hermano: `[11-RUTA-PRESENTACION-AJUSTES.md](./11-RUTA-PRESENTACION-AJUSTES.md)`.*  
*Ruta 13 = hablarle a Sergio en el idioma de la reunión, no en lista técnica P0/P1.*
