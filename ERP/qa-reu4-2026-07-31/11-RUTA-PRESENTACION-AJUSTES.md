# Ruta de presentación — Ajustes Reu3/Reu4 + indicaciones Sergio

**Fecha:** 31/07/2026  
**Audiencia sugerida:** Sergio / MJ / equipo interno  
**Entorno demo:** MODO REAL · Front `127.0.0.1:5174` · API `:3001` · Postgres `:5433`  
**Credenciales QA:** `qa.aprobador@almahue.local` / `QaTest123!` · **PIN `4821`**  
**Admin:** `admin@almahue.local` / `Admin123!` · PIN `4821`

Documento hermano: [`10-AS-IS-TO-BE-OPERATIVO.md`](./10-AS-IS-TO-BE-OPERATIVO.md) · Matriz: [`06-MATRIZ-CUMPLIMIENTO-REU4.md`](./06-MATRIZ-CUMPLIMIENTO-REU4.md)

---

## Cómo usar esta ruta (15–25 min)

| Min | Bloque | Objetivo |
|----:|--------|----------|
| 0–2 | Veredicto | Piloto sí / producción aún no |
| 2–8 | Aprobaciones + PIN (Sergio) | Demo viva del cambio más reciente |
| 8–14 | Flujo OC + proformas | Re-solicitud, print, elegibilidad |
| 14–18 | Ventas / contabilidad / tesorería | Folio, factor, aging audit |
| 18–22 | RBAC / roles temporales | Matriz pantallas + vigencia |
| 22–25 | Qué NO se tocó / diferido | Cotizaciones, DTE, inventariable |

En cada ítem: **Pedido → Antes → Ahora → Dónde verlo**.

---

## 0. Veredicto en una frase

El slice de reuniones (alto/medio impacto) + la indicación de Sergio del **PIN de 4 dígitos** quedó implementado y probado en BD local (**19/19 casos API PIN**). Cotizaciones **sin cambio** (mute en reu; pendiente confirmar con Sergio). Integración DTE/GoSocket **retirada** hasta documentación oficial.

---

## 1. PIN de aprobación (indicación Sergio — post-reu)

| | |
|--|--|
| **Pedido** | Sistema de PIN de 4 dígitos según rol. Visible en perfil solo si el rol aprueba con PIN; se puede cambiar en perfil; al aprobar/rechazar debe pedir el PIN. |
| **Antes** | Aprobar/rechazar OC o proforma solo con login + permisos. Sin segundo factor. Perfil sin sección PIN. Roles sin flag. |
| **Ahora** | `Rol.aprobarConPin` (Admin → Roles). Si true, sesión expone `aprobarConPin` / `tienePinAprobacion`. Mi Perfil muestra crear/cambiar PIN (bcrypt). OC y proformas en cola pendiente exigen PIN. Si el usuario deja de ser aprobador, la sección desaparece. |
| **Demo** | 1) Roles → marcar «Aprobar con PIN». 2) Login aprobador → Mi Perfil → PIN. 3) Bandeja OC / proforma → Aprobar → modal pide PIN. 4) Sin PIN / PIN malo → error API. |
| **Prueba** | `npx ts-node -r tsconfig-paths/register scripts/setup-and-test-pin-aprobacion.ts` |

---

## 2. Órdenes de compra

### 2.1 Re-solicitud tras rechazo (OC-02 / gap operativo)

| | |
|--|--|
| **Pedido** | Si una OC se rechaza, poder reenviar a aprobación con bandeja limpia. |
| **Antes** | Editar OC `RECHAZADO` conservaba estado; `updateOrden` no recreaba `AprobacionOc` → no aparecía en bandeja. |
| **Ahora** | Al guardar desde `RECHAZADO`/`BORRADOR` → `EMITIDO`, se recrea bandeja `PENDIENTE` y se notifica al jefe. Front fuerza `EMITIDO` en ese caso. |
| **Demo** | OC rechazada → Editar → Guardar → Aprobaciones OC muestra nueva pendiente. |

### 2.2 Impresión con detalle (R4-24)

| | |
|--|--|
| **Pedido** | Print OC con ítems (y CC si aplica), no solo cabecera. |
| **Antes** | Print = folio/contraparte/neto; sin líneas. |
| **Ahora** | Print incluye tabla de líneas + distribución CC cuando existe. |
| **Demo** | Compras → Órdenes → Imprimir en una OC con ítems. |

### 2.3 OC → recepción → factura (D4 / R4-05)

| | |
|--|--|
| **Pedido** | Solo OC aprobadas y recepcionadas elegibles para factura de compra. |
| **Antes** | Riesgo de elegir OC no elegibles. |
| **Ahora** | Filtro por `RECEPCIONADA` / `CONTABILIZADA` / `FACTURADO`. Seed E2E `OC-QA-REC-005`. |
| **Demo** | Libro compras → nueva factura: solo OC elegibles en el selector. |

### 2.4 Anulación OC

| | |
|--|--|
| **Pedido** | Anular OC y cerrar bandeja. |
| **Antes** | Posibles pendientes “zombie”. |
| **Ahora** | Anular → estado `ANULADA` en bandeja; migración/estado de aprobación alineado. |

---

## 3. Proformas / contratistas

| | |
|--|--|
| **Pedido (D2/D3)** | Aprobada = sin editar; asociar factura; reversa con clave **por usuario**. |
| **Antes** | Lock parcial; clave no siempre personal. |
| **Ahora** | Solo `BORRADOR` editable. DEFINITIVA → Asociar + Reversar (clave en Mi Perfil). Solicitud de aprobación a jefe de regla; se registra quién solicitó vs quién resolvió. + **PIN** si el rol lo exige. |
| **Demo** | Proforma pendiente → Aprobar con PIN → Associar factura; otra → Reversar con clave personal. |

---

## 4. Ventas / documentos

### 4.1 Libro de ventas (D6/D8/R4-07/R4-09/R4-10)

| | |
|--|--|
| **Pedido** | Sin «Emitir» en libro; totales tipo RCV; folio → representación gráfica; borrador con watermark. |
| **Antes** | Emisión mezclada en libro; sin preview por folio; watermark solo si plantilla lo tenía. |
| **Ahora** | Emitir vive en menú aparte. Cards Documentos/Neto/IVA/Exento/Total. Click folio/PDF. Watermark `BORRADOR` forzado en borradores. |
| **Demo** | Libro ventas → click folio; emitir desde Ventas › Emitir documento. |

### 4.2 Emisión con cuenta + CC (D7/R4-06)

| | |
|--|--|
| **Pedido** | En detalle de emisión, cuenta contable + centro de costo. |
| **Antes** | Faltaba en wizard. |
| **Ahora** | Paso ítems exige Cuenta + CC al emitir. |

### 4.3 Cotizaciones (D9) — **sin cambio**

| | |
|--|--|
| **Pedido** | Definir flujo (se cortó audio / mute MJ). |
| **Antes / Ahora** | Se mantiene registro/envío/conversión actual. **No** se armó cola de aprobación. |
| **Pregunta abierta** | ¿Solo registro, o aprobación de jefatura para temporada? |

### 4.4 DTE / GoSocket (R4-08 / GS-01) — **retirado a pedido**

| | |
|--|--|
| **Pedido (equipo)** | Eliminar rastros de GoSocket hasta tener documentación oficial. |
| **Antes** | Módulo GoSocket, modelos DTE, auto-emisión, pantalla Integraciones. |
| **Ahora** | Código y migraciones de remoción aplicados. Emisión local / print / libro se mantienen. Config SII contable se conserva. Reintegrar cuando exista docs del proveedor. |

---

## 5. Contabilidad / parametrización

### 5.1 Menú Parametrización (D11/R4-13)

| | |
|--|--|
| **Pedido** | Plan, indicadores, elementos, CC en Parametrización; periodos en Contabilidad. |
| **Antes** | Mezcla en Contabilidad. |
| **Ahora** | Sidebar Parametrización + redirects. Periodos siguen en Contabilidad. |

### 5.2 Factor honorario vigente (R4-14)

| | |
|--|--|
| **Pedido** | Historial / vigencia del factor. |
| **Antes** | Solo `vigenciaDesde`; catálogo aislado. |
| **Ahora** | `vigenciaHasta` + resolución de factor vigente a fecha; badge en UI. |

### 5.3 Balance 8 columnas (R4-15)

| | |
|--|--|
| **Pedido** | Menú Balance 8 columnas. |
| **Antes** | No estaba. |
| **Ahora** | Página con 8 grupos + KPIs. |

### 5.4 Periodos / cierre

| | |
|--|--|
| **Pedido** | No contabilizar en periodo cerrado. |
| **Antes** | Riesgo de asientos en cerrado. |
| **Ahora** | Bloqueo + tests; excepciones de cierre donde aplica. |

---

## 6. Tesorería

### 6.1 Aging — vencimiento + auditoría (D15 / gap Sergio)

| | |
|--|--|
| **Pedido** | Editar vencimiento solo rol tesorería; trazabilidad quién/cuándo. |
| **Antes** | Edit inline sin historial. |
| **Ahora** | Gate `tesoreria:write` + historial JSON + columna «Última edición». |

### 6.2 Estado de cuenta (D16/R4-20/21/22)

| | |
|--|--|
| **Pedido** | Renombrar CC → Estado de cuenta; filtro Todos/Pendientes; links a pago/factura. |
| **Antes** | Nombre «cuentas corrientes»; sin links claros. |
| **Ahora** | Label nuevo, filtro, columna Ver con deep-links (`?q=`). |

### 6.3 Conciliación (R4-19)

| | |
|--|--|
| **Pedido** | Default pendientes + resumen cantidad/monto. |
| **Antes** | Vista menos orientada a pendientes. |
| **Ahora** | KPI Conciliados/Pendientes; tab Pendientes. |

### 6.4 Cartola (D14/R4-16) — parcial

| | |
|--|--|
| **Pedido** | Excel tipo MJ → calzar. |
| **Antes / Ahora** | Import genérico CSV/Excel/PDF + parsers bancos. Falta alinear plantilla exacta MJ. |

---

## 7. RBAC, roles y notificaciones

### 7.1 Matriz pantallas (R4-01/R4-02 / RBAC-02)

| | |
|--|--|
| **Pedido** | Selector pantallas por módulo; búsqueda de rol. |
| **Antes** | Seed solo `permisos` string; proyección UI parcial. |
| **Ahora** | `permisosPantalla` en Roles; script `seed-permisos-pantalla.ts`; búsqueda rol/módulo. |

### 7.2 Roles temporales (ROL-01)

| | |
|--|--|
| **Pedido** | Usuarios/roles con vigencia. |
| **Antes** | Sin fechas en usuario. |
| **Ahora** | `rolVigenciaDesde` / `rolVigenciaHasta` en Usuarios; login/refresh bloquean fuera de vigencia. |

### 7.3 Solo el jefe asignado aprueba

| | |
|--|--|
| **Pedido** | No cualquiera con write aprueba. |
| **Antes** | Gaps de autorización. |
| **Ahora** | 403 si no es el aprobador (salvo superadmin / `compras:aprobar-all`). |

### 7.4 Inbox notificaciones

| | |
|--|--|
| **Pedido** | Avisar pendientes / resoluciones. |
| **Antes** | Sin inbox persistente. |
| **Ahora** | Modelo notificaciones + topbar. |

---

## 8. Admin / UX varios (slice jueves)

| Ítem | Pedido | Antes → Ahora |
|------|--------|----------------|
| R4-03 | Sin columna empresa en CC | Columna empresa → solo Código/Nombre/Encargado/Desde/Estado |
| R4-01 | Buscar rol | Sin búsqueda dedicada → input «Buscar rol…» |
| Centros / maestros | Vigencias | Campos vigencia en CC/tarifas donde aplica |
| Plantilla documentos | Preview/footer | Conservado; watermark usable en print |

---

## 9. Insumos / bodega — gaps conscientes

| | |
|--|--|
| **Pedido (D10/R4-11/R4-12)** | Flag inventariable, Excel AlmaWeb, NC reingreso. |
| **Antes / Ahora** | Movimientos con bodega por nombre (soft catálogo). **Sin** inventariable ni import AlmaWeb. Gap de producción. |

---

## 10. Diferidos / propuestas (no demo como “listo”)

| Tema | Estado | Mensaje en sala |
|------|--------|-----------------|
| Cotizaciones aprobación | Abierto Sergio | «Sin cambio; necesitamos cerrar si hay jefatura» |
| DTE proveedor | Removido | «Sale del producto hasta docs oficiales» |
| Cobranza R4-18 | Solo propuesta | Doc, sin UI |
| Exportación / aduana | Pendiente | Post temporada |
| Contabilidad electrónica | Diferido D13 | 2ª etapa |
| Cartola Excel MJ / plan Excel cliente | Parcial | Código base; falta archivo MJ |

---

## 11. Guion demo vivo (orden recomendado)

1. **Login** `qa.aprobador@almahue.local` → Topbar/notificaciones.
2. **Mi Perfil** → sección PIN (porque el rol tiene flag) → comentar que Digitador no la ve.
3. **Admin › Roles** (con Admin) → checkbox «Aprobar con PIN».
4. **Compras › Aprobaciones** → aprobar/rechazar pidiendo PIN `4821`.
5. **OC rechazada** → reabrir → vuelve a bandeja.
6. **Print OC** con líneas.
7. **Contratistas › Proformas** → aprobar pendiente con PIN; reversa con clave.
8. **Libro ventas** → folio → print/watermark.
9. **Tesorería › Aging** → editar vencimiento → ver «Última edición».
10. **Cierre** → cotizaciones sin tocar; DTE fuera hasta docs; inventariable pendiente MJ.

---

## 12. Evidencia técnica rápida

| Artefacto | Path |
|-----------|------|
| Migración PIN | `erp_back/prisma/migrations/20260731230000_pin_aprobacion/` |
| Assert PIN | `erp_back/src/auth/pin-aprobacion.ts` |
| Script setup+test PIN | `erp_back/scripts/setup-and-test-pin-aprobacion.ts` |
| Seed pantallas | `erp_back/scripts/seed-permisos-pantalla.ts` |
| Reset flujo OC | `erp_back/scripts/audit-and-reset-flujo-oc.ts` |
| Remoción GoSocket | migración `20260731220000_remove_gosocket_dte` |
| UI PIN perfil/roles | `PerfilPage`, `RolesPage`, modales OC/proformas |
| Matriz cumplimiento | `06-MATRIZ-CUMPLIMIENTO-REU4.md` |

---

## 13. Checklist pre-reunión (2 min)

- [ ] Nest + Vite + Postgres arriba  
- [ ] MODO REAL (`almahue-erp-demo-mode=false`)  
- [ ] Correr `setup-and-test-pin-aprobacion.ts` si se resetó la BD  
- [ ] Tener una OC pendiente y una proforma pendiente  
- [ ] Abrir este doc + captura carpeta `capturas-cumplimiento/`  

---

*Fin de la ruta. Para detalle operativo por ID: ver documento 10 y matriz 06.*
