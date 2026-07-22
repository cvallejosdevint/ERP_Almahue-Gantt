# Compromiso de actualización — Tablero Almahue ERP

**Origen:** reunión demo Agrosoft / levantamiento ERP · **22/07/2026**  
**Tablero:** [Almahue ERP](https://trello.com/b/wixKcrP0/almahue-erp) (`wixKcrP0`)  
**Snapshot base:** `trello-snapshot.md` (26 tarjetas)  
**Fuentes canónicas:** `00-decisiones.md`, `modulos/*.md`, `matriz-trazabilidad.csv`  
**Video:** [tl;dv](https://tldv.io/app/meetings/6a60394d4959970013159ad2)

## Objetivo

Actualizar las tarjetas **Mock** actuales para que reflejen lo conversado en la reunión del 22/07, como **compromiso de trabajo para la próxima semana**.  
El mockup de producto se alinea a Agrosoft 3.0; **se conserva** lo ya implementado de **Login** y **Administración (empresas / usuarios / roles-permisos)**.

## Resumen ejecutivo (qué cambia en el tablero)

| Acción | Cantidad aprox. | Criterio |
|---|---|---|
| **Mantener y enriquecer** | 6 | Login, Empresas, Usuarios, Roles, Monedas, CC |
| **Reescribir alcance** | 8 | Contratistas, Insumos, Contabilidad, Asientos, Reportes, Flujo, Pagos, Conciliación |
| **Reemplazar / archivar** | 10 | Comercialas comerciales genéricas (prospectos, cotizaciones, emitir, libro, clientes, GoSocket, presupuestos genéricos, reporte ejecutivo genérico) |
| **Crear nuevas (próx. semana)** | ~20 | Flujos Contratistas / Compras / Bodega / Contabilidad BC (ver lista abajo) |
| **Fuera v1** | 2 menciones | Maquinaria, Gestión/Power BI/AlmaWeb (Mario agosto) |

---

## Lista de actualización por tarjeta actual

> Formato: **Acción** · qué hacer en Trello · vínculo a decisión/módulo.

### Conservar (base ya acordada / core nuevo)

1. **Mock — Inicio de sesión** → **ACTUALIZAR**  
   - Mantener como REQ.  
   - Agregar: empresa activa siempre visible; temporada = OPT; riesgo sesiones compartidas (**DEC-08**, C-02).  
   - Checklist: selector empresas con permiso; advertencia sesión concurrente (ideal).  
   - Link tl;dv `t=21`.

2. **Mock — Empresas** → **ACTUALIZAR**  
   - Mantener CRUD (core técnico).  
   - Agregar REQ: aislamiento de datos por empresa activa (**DEC-03**).  
   - OPT/OUT v1: fondos / geografía (poca relevancia); sí importa tipo de terreno agrícola (05-permisos).

3. **Mock — Usuarios** → **ACTUALIZAR**  
   - Mantener (infra ERP nuevo; no es tarjeta #49 del resumen).  
   - Nota: ~15 usuarios; a veces 2 personas / 1 login → empresa incorrecta (**DEC-08**).

4. **Mock — Roles y permisos** → **ACTUALIZAR (crítico)**  
   - Perfiles: Administrador / Digitador / **Intermedio** (**DEC-04**, C-05).  
   - Roles independientes: editar rol A no muta rol B.  
   - Digitador: sin parametrización / traspaso / cierre.  
   - Auditoría mínima de cambios de permisos (quién/cuándo).  
   - Link tl;dv `t=780`.

5. **Mock — Monedas** → **ACTUALIZAR**  
   - Foco reportería: **peso, dólar, yuan, euro** (**DEC-05**).  
   - Desactivar o marcar OUT: UF/UTM/IPC como dependencia.  
   - Relacionar con indicadores Banco Central (**DEC-06**, K-05).

6. **Mock — Centros de costo** → **ACTUALIZAR**  
   - Solo CC de **empresa activa** (bug cross-empresa @ 11:29, C-04).  
   - Vigencia; no permitir selección cross-empresa en Contratistas/OC.

7. **Carta Gantt** (En QA Almahue) → **MANTENER**  
   - Fuera del alcance mock de módulos; no bloquear actualización de mocks.

### Reescribir (misma tarjeta, nuevo alcance Agrosoft)

8. **Mock — Panel principal** → **REESCRIBIR**  
   - Dejar de ser “ventas/DTE/presupuesto genérico”.  
   - KPIs reunión: OC por aprobar (badge), proformas contratista sin factura, facturas por recibir, TC del día (BC), alertas cierre mes.  
   - Gestión/Power BI = OUT hasta Mario (**G-01**).

9. **Mock — Unidades de medida** → **ACTUALIZAR**  
   - Mantener catálogo; alinear a insumos/agro (KG, LT, CAJ, HR labor).  
   - OPT: UM relevantes + ingredientes activos (mencionado, no sprint sin OK).

10. **Mock — Tipos de documento** → **REESCRIBIR**  
    - Priorizar: OC, Factura compra, NC, Proforma contratista, Asiento.  
    - Quitar foco cotización/NP comercial outbound si no salió en demo.

11. **Mock — Plan de cuentas** → **REESCRIBIR** (K-01)  
    - Flags: CC, área negocio, especie, variedad, elemento; “No imputable”.  
    - Parametrización ER / estado situación financiera.

12. **Mock — Asientos contables** → **REESCRIBIR**  
    - Incluir carga masiva con validación (K-04).  
    - Cuadratura debe/haber; feedback por línea; plantilla estable.  
    - Advertir si falta TC del día.

13. **Mock — Reportes contables** → **ACTUALIZAR**  
    - Mantener balance / ER / mayor.  
    - No confundir con dashboards Gestión Agrosoft (OUT, G-01).

14. **Mock — Flujo de caja** → **ACTUALIZAR (secundario v1)**  
    - Mantener como apoyo tesorería; TC manual en pagos (mencionado en recepción productores).  
    - No es el núcleo de la demo; prioridad menor que Compras/Contratistas.

15. **Mock — Pagos** → **ACTUALIZAR (secundario)**  
    - Nota: diferencia TC productores vs recepción; tesorería permite TC manual.

16. **Mock — Conciliación bancaria** → **DEJAR / BAJAR PRIORIDAD**  
    - No hubo foco en reunión → mover a Backlog OPT o dejar mock mínimo.

17. **Mock — Presupuestos** → **ARCHIVAR o relabel OUT/PEND**  
    - Desviación presupuesto deseada vía Power BI / Mario agosto (**G-01**).  
    - No inventar módulo Gestión.

18. **Mock — Contratistas** → **REESCRIBIR (módulo completo)**  
    - Separar en subtareas/tarjetas hijas (próx. semana):  
      - Listado/alta + vigencia (no borrar histórico)  
      - **Tarifas multi-línea** persistentes (C-03) — bug crítico  
      - Actividad/Labor aquí, **NO** Mano de Obra (**DEC-01**)  
      - Proforma ↔ factura 1:1 + bloqueo cierre (C-06, PEND-02)  
      - Traspaso + cierre mes Admin; monedas PX/USD/CNY/EUR (C-07)

19. **Mock — Catálogo de insumos** → **REESCRIBIR** (P-02, DEC-07)  
    - Maestro único Familia+Subfamilia+Descripción (anti-duplicado).  
    - Compras admin = servicios; materiales viven aquí.  
    - Ampliar a: Bodegas (I-01), Movimientos (I-04), NC a precio factura (I-05), param. contable (I-03).  
    - Niveles almacenamiento = PEND-03 / no construir aún (I-02).

### Archivar / reemplazar (no alineadas a la reunión)

20. **Mock — Clientes** → **ARCHIVAR** (fuera del foco demo Agrosoft 22/07) o mover a “Comercial futuro”.  
21. **Mock — Prospectos** → **ARCHIVAR**.  
22. **Mock — Libro comercial** → **ARCHIVAR**.  
23. **Mock — Cotizaciones** → **ARCHIVAR**.  
24. **Mock — Aprobaciones** (workflow genérico) → **REEMPLAZAR** por **Aprobación de OC** (P-06): badge pendientes, aprobar/rechazar con líneas y CC; correos = OPT.  
25. **Mock — Facturación electrónica (GoSocket)** → **ARCHIVAR / OUT reunión** (no levantado como núcleo).  
26. **Mock — Reporte ejecutivo** → **REEMPLAZAR** por panel operativo (ver #8) o marcar OUT hasta Mario.

---

## Tarjetas NUEVAS a crear la próxima semana (compromiso)

Listas sugeridas (pueden vivir en el mismo tablero con labels `REQ|DEC|PEND|OUT|MockUp`):

### Decisiones
- [DEC-01] No Mano de Obra — parametrizar en Contratistas  
- [DEC-02] Eliminar Solicitud de Compra  
- [DEC-03] Aislamiento por empresa activa  
- [DEC-04] Perfil Intermedio + roles independientes  
- [DEC-05]/DEC-06] Monedas + indicadores Banco Central  
- [DEC-07] Compras=servicios / Insumos=materiales  
- [DEC-08] Sesiones compartidas / 15 usuarios  
- [DEC-09]/[DEC-10] AlmaWeb-PowerBI / Maquinaria OUT v1  
- [PEND-01]…[PEND-04] (ver `00-decisiones.md`)

### Contratistas
- Tarifas multi-línea + CC empresa  
- Proforma + asociación factura  
- Traspaso contable y cierre de mes  

### Compras (servicios)
- OC sin solicitud + distribución CC en tiempo real  
- Informe OC (búsqueda proveedor también contabilizadas)  
- Aprobación con badge  
- Recepción + TC visible  
- Registro compra anti-cruzado + política Afecto/Exento (PEND-01)

### Insumos / Bodega
- Maestro anti-duplicado  
- Bodegas por empresa  
- Param. contabilización + movimientos complementarios  
- Movimientos (entrada / traslado / devolución)  
- NC vinculada a factura (precio factura, sin FIFO/LIFO)

### Contabilidad
- Elementos de costo (anular sin borrar)  
- Historial factores honorarios  
- Carga masiva comprobantes  
- Indicadores BC (domingos/feriados)

---

## Compromiso de la próxima semana

| # | Entregable | Dueño sugerido |
|---|---|---|
| 1 | Actualizar descripciones/checklists de las 26 tarjetas según esta lista | Producto / Devint |
| 2 | Crear tarjetas nuevas REQ de Contratistas + Compras + Bodega + Contabilidad BC | Producto |
| 3 | Archivar o mover a “Fuera reunión” las mocks comerciales/GoSocket | Producto |
| 4 | Mockup UI alineado a reunión (este repo `ERP/erp_front`) — **hecho en paralelo a este doc** | Dev |
| 5 | Definir prioridad de implementación real post-mock (ver abajo) | Tech lead |

---

## Prioridad de implementación real (post-mock)

Orden según **flujo de negocio** levantado (no según orden del sidebar genérico):

1. **Ya hecho / conservar:** Login + empresa activa + Admin (empresas/usuarios/roles) → completar **perfil Intermedio** y permisos Digitador vs Admin (DEC-04).  
2. **Siguiente prioridad (sprint real):** **Contratistas — tarifas multi-línea + CC solo empresa activa**.  
   - Es el dolor operativo #1 de la demo (líneas que “desaparecen”, cross-empresa).  
   - Desbloquea DEC-01 (labores fuera de Mano de Obra).  
3. **Luego:** Compras OC sin solicitud → aprobación (badge) → recepción (TC) → registro anti-cruzado.  
4. **Luego:** Insumos maestro + movimientos + NC a precio factura.  
5. **Luego:** Contabilidad (flags plan cuentas, carga masiva, indicadores BC).  
6. **Paralelo ligero:** Tesorería solo donde afecta TC/pagos.  
7. **No ahora:** Maquinaria, Gestión/Power BI/AlmaWeb, niveles bodega, comercial outbound, GoSocket como epic.

**Criterio:** cerrar el circuito *labor contratista → costo → contabilidad* antes de ampliar a módulos no demostrados.
