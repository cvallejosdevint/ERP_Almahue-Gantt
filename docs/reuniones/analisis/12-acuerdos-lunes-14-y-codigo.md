# Lista fina lunes 14/09/2026 — cada acuerdo vs back y vs front

**Reunión cliente:** Meet «ERP Almahue - Avances», ~77 min.  
**Fuente:** `fuentes/transcripcion-2026-09-14-demo-avances.md` (Whisper large-v3).  
**En sala:** Carlos, Sergio, **Mario**. Invitadas: MJ / María Jesús, Lupe, Sigrid.  
**No son requisito:** las tres internas del mismo día (mañana, mediodía, tesorería noche). La coda de Sergio se cita solo cuando implementa lo que el cliente acaba de pedir.

Ciclo de vida y obsolescencia semanal: [`11-ciclo-vida-whisper-v3-2026-09-17.md`](11-ciclo-vida-whisper-v3-2026-09-17.md).  
Corte anterior (10/09): [`09-acuerdos-definitivos-2026-09-10.md`](09-acuerdos-definitivos-2026-09-10.md).

**Cómo se marca**

| Estado | Significa |
|---|---|
| **CUMPLE** | Back aplica la regla y el front la representa (pantalla, badge, bloqueo, ruta). |
| **PARCIAL** | Una de las dos capas falta, o el happy path está y el caso del cliente no. |
| **PENDIENTE** | No hay símbolo en código. |
| **N/A** | Acuerdo de proceso (Trello, agenda), no de producto. |

ASR: «Chipas» = Chipax; «CUA» = columna Devint; «MAU» = tablero Almahue; «ACRI» = año siguiente.

---

## Resumen

| Capa | CUMPLE | PARCIAL | PENDIENTE | N/A |
|---|---:|---:|---:|---:|
| Acuerdos **nuevos o reafirmados el 14/09** (A14-G / C / T) | 10 | 4 | 4 | 4 |
| Stock vigente **no reabierto** el 14 (V-*) | 8 | 2 | 4 | 0 |

Lo que el cliente se lleva de esa tarde y **aún no está** en producto: alerta RUT, rango fechas cartola, asiento puente de nómina, destacar/alta **sin** OC, Chipax (aplazado a propósito).

---

## A. Gobernanza de la reunión (no es código)

### A14-G1 — Asignar tarjetas Trello por módulo y persona

- **Qué:** Mario parametrización / plan de cuentas; Lupe tesorería; MJ contabilidad; un ejecutivo por menú. `[08:02]`–`[15:23]`
- **Quién:** Sergio propone; Mario acepta el esquema.
- **Back / Front:** N/A
- **Estado:** **N/A** — proceso. No se valida en repo.

### A14-G2 — No pasar aún las tarjetas de Compras

- **Qué:** «los de compra yo creo que aún no lo pasemos porque se van a hacer los ajustes de la aprobación y el reclamo». `[09:14]`
- **Estado:** **N/A**. El producto de aprobaciones OC **sí** existe; el pendiente de esta frase es **reclamo / recepción DTE** (ver A14-C4 y V-GoSocket).

### A14-G3 — Reuniones semanales por módulo

- **Qué:** lunes contabilidad, martes tesorería, etc. La semana del 10/09 «solo venta + GoSocket» funcionó. Coordinar por WhatsApp. `[01:14:20]`–`[01:15:18]`
- **Estado:** **N/A**

### A14-G4 — Tesorería: devolver tarjetas a CUA; nómina semanal sí a Lupe

- **Qué:** «hay que ajustar un poquito las tarjetas… no pasarle todas a Lupe antes de aplicar las correcciones». Nómina semanal «está bastante avanzada» → Lupe mueve factura de semana. `[01:15:54]`–`[01:16:36]`
- **Estado:** **N/A** (Trello). El software de nómina se valida en A14-T6 / pantallas.

---

## B. Compras y documentos recibidos (cliente, 14/09)

### A14-C1 — Factura referenciando OC aún no aprobada: destacar, no rechazar

- **Verbatim:** Mario: «en teoría no, en la práctica sí». Sergio: ¿auto-rechazar o destacar? Cliente: **no rechazar** («si no la rechazan los productores»); «la cultura de la plata todavía no está»; **destacar** que la OC no está aceptada. `[24:00]`–`[26:27]`
- **Back:** **CUMPLE.** Se puede asociar factura a OC en `BORRADOR` / `PENDIENTE_APROBACION`. Contabilizar/pagar exige `APROBADO` o posterior.
  - `ocNoAprobada` / `ocPermiteContabilizarOPagar` — `ERP/erp_back/src/modules/compras/oc-estado.util.ts`
  - `assertOcParaRegistroCompra` — `compras.service.ts`
- **Front:** **CUMPLE.** Badge «OC sin aprobar»; contabilizar deshabilitado + toast «No se puede contabilizar: la OC aún no está aprobada».
  - `ERP/erp_front/src/features/compras/ComprasPages.tsx` (badge ~1834, gate ~1682, combo OC ~2150)
- **Estado conjunto:** **CUMPLE**

### A14-C2 — Destacar también las facturas **sin** OC (el 90 %)

- **Verbatim:** «¿Y si llega una factura antes?» — «El 90% de las facturas que llega sin orden de compra» — «también los documentos que no están referenciando orden de compra también que se destaquen». Quedan pendientes hasta los 8 días. `[25:10]`–`[26:32]`
- **Back:** **PARCIAL.** `createRegistro` permite `ocNumero` vacío (`if (!oc && dto.ocNumero.trim())` no dispara si el string es vacío). No hay flag `sinOc` ni listado filtrable «sin OC».
- **Front:** **PENDIENTE / contradice.** El alta exige OC: `if (!form.ocNumero || !form.factura) toast.error('Completa OC y factura')` (`ComprasPages.tsx` ~1752). El empty state «Sin OC» es de otra grilla (listado de órdenes), no un badge de factura recibida. Solo existe badge «OC sin aprobar».
- **Estado conjunto:** **PARCIAL** — el caso real del cliente (90 % sin OC) no se puede cargar ni destacar en Libro de compras.

### A14-C3 — Plazo 8 días: si no se rechaza, pasa automático a aceptado

- **Verbatim:** «va a quedar en pendiente hasta los 8 días» / «si no se rechaza va a pasar automático como aprobado». `[25:39]`–`[26:13]` y `[31:23]`
- **Back:** **CUMPLE.** Default `aceptacionCompraPlazoDias = 8`; cron `aceptacion-compra.cron.ts`; `runAceptacionCompraAutoIfDue` en `compras.service.ts`.
- **Front:** **CUMPLE.** Admin › Empresas, campo `aceptacionCompraPlazoDias` (`EmpresasPage.tsx`).
- **Estado conjunto:** **CUMPLE**  
- **Nota:** Mario duda de si 8 días es «muy bueno» cuando hay disputa o factura al contado `[31:23]`. No se cambió el plazo; se pidió **alerta** (C4), no acortar los 8 días.

### A14-C4 — Alerta por RUT específico (reclamar), no auto-rechazo

- **Verbatim:** MJ/Mario: alerta si un RUT de watchlist emite. **Para reclamar**, no para aceptar. Sergio ofrece auto-rechazo; cliente: «no necesitamos que automáticamente se rechacen, sino que se emite una alerta». Campana + correo a N usuarios (MJ, Mario, …), parametrizable y con vigencia. Casos: disputa legal, productor objetado SII. `[26:36]`–`[33:32]`
- **Back:** **PENDIENTE.** No hay watchlist de RUT, ni notificación al recepcionar DTE de compra, ni correo de alerta (H9 SMTP sigue pendiente).
- **Front:** **PENDIENTE.** Campana actual = OC/aprobaciones, no «alerta especial» diferenciada.
- **Estado conjunto:** **PENDIENTE**  
- **Dependencia:** tiene sentido pleno cuando exista **recepción GoSocket → libro compras** (Reu2). Hoy el libro de compras es carga/asociación manual.

---

## C. Tesorería (cliente, 14/09)

### A14-T1 — Chipax / Fintox / sync banco: no ahora

- **Verbatim:** Mario `[50:29]`: «yo prefiero que sigamos así en primera instancia… en el ACRI del próximo año vamos y lo automatizamos.»
- **Back / Front:** no hay integración Chipax. Import Excel/CSV/PDF sí (eso es el «seguir así»).
- **Estado conjunto:** **CUMPLE** como **aplazamiento** (no construir sync). No es un hueco de esta semana.

### A14-T2 — Cartola: fechas del mes anterior + rango desde–hasta

- **Verbatim (misma reunión, se pisa a sí mismo):**
  1. Incluir el movimiento del mes anterior porque es el saldo de apertura `[47:09]`–`[47:15]`
  2. «Debería excluirse» `[47:17]`
  3. Rollback Sergio `[48:12]`: «como es un control interno, lo vamos a eliminar y que sí se pueda leer la fecha del mes anterior»
  4. Mario: pagos viernes post-14:00 caen el lunes; pedir **día desde–hasta** para subir semanal `[49:01]`–`[49:30]`
- **Vigente:** cargar lo que traiga el Excel (no filtrar mes anterior como regla rígida) + selector **desde–hasta**.
- **Back:** **PARCIAL.** `parseCartolaWorkbook` importa filas del archivo. No hay filtro de rango de fechas en el API de carga.
- **Front:** **PARCIAL.** Selector de **periodo/mes** (`mesesContablesCercanos`), no rango día–día. Saldos por banco/moneda sí (T8).
  - `CartolaBancariaPage.tsx` + `tesoreria.service.ts`
- **Estado conjunto:** **PARCIAL**

### A14-T3 — Conciliación = vista de información

- **Verbatim:** «esta era solamente vista de información, ¿verdad?» — confirmado. Filtro pendientes/todos. `[51:03]`–`[51:42]`
- **Back:** **CUMPLE.** `createConciliacion` vacío bloqueado; el trabajo está en cartola.
- **Front:** **CUMPLE.** `ConciliacionPage` en `TesoreriaPages.tsx` — resumen, link a cartolas.
- **Estado conjunto:** **CUMPLE**

### A14-T4 — Contabilizar 1:1 en la cartola; al confirmar, aparece conciliado

- **Verbatim:** por cada movimiento de la carga, cuenta + confirmar → «automáticamente se concilia y aparece acá». `[52:20]`–`[52:39]`
- **Back:** **CUMPLE** para el movimiento: `contabilizarMovimientoCartola` → asiento `CARTOLA:{id}`.
- **Front:** **CUMPLE.** Modal T2 en `CartolaBancariaPage.tsx`.
- **Estado conjunto:** **CUMPLE** para ingresos y para el 1:1 genérico. Los **egresos vs nómina** los precisa T6/T7.

### A14-T5 — Al contabilizar, poder seleccionar la factura (match RUT + monto)

- **Verbatim:** «sería perfecto que pudieran seleccionar la factura» — match perfecto RUT+monto; imperfecto solo RUT ± pesos. `[53:07]`–`[53:38]`
- **Back:** **CUMPLE.** `lookupDocumentoCartola` — `tesoreria.service.ts` ~1629, controller ~311.
- **Front:** **CUMPLE.** Lookup en el modal T2 de cartola.
- **Estado conjunto:** **CUMPLE** (el «match imperfecto» de 1–3 pesos no está modelado como umbral; es lookup, no auto-calce).

### A14-T6 — Nómina **antes** de la cartola; asociar egresos a una nómina que calce

- **Verbatim:** «en una instancia antes de la cartola nosotros emitimos una nómina de pago». Seleccionar egresos y asociarlos a una nómina; «esa selección tiene que calzar». `[53:53]`–`[01:02:42]`
- **Back:** **CUMPLE** asociación. `asociarNominaCartola` + `MovimientoCartola.nominaSemana`.
- **Front:** **CUMPLE** asociación. Filtro egresos, multi-select, columna semana, acción «asociar nómina» en `CartolaBancariaPage.tsx` (~332, ~764). Nómina semanal: año/mes/semana, aplazar, export, default = mes del header (`NominasAgingPage.tsx`).
- **Calce perfecto selección vs total nómina:** **PARCIAL** — se asocia; no hay validación dura de que Σ egresos = Σ nómina.
- **Estado conjunto:** **PARCIAL** (asociar sí; calce obligatorio no)

### A14-T7 — Contabilizar egresos **con la nómina** (asiento puente) — discusión abierta

- **Verbatim:** Sergio propone «asiento puente» banco vs nómina. MJ: «yo contabilizaría con la nómina, no con la cartola» porque la nómina ya trae los documentos. Aclara: **ambas**, «porque la nómina son egresos». Ingresos no van por nómina. `[54:24]`–`[57:53]`
- **Naturaleza:** pedido de **cliente** (MJ) + diseño de Sergio. No hubo «no lo hagamos». Quedó como trabajo («nos faltó revisar la nómina»).
- **Back:** **PENDIENTE.** No existe asiento puente de nómina ni `confirmar nómina → contabiliza el tiro`. El asiento sigue siendo `CARTOLA:{id}` línea a línea.
- **Front:** **PENDIENTE.** No hay botón «contabilizar nómina».
- **Estado conjunto:** **PENDIENTE**  
- **No confundir** con T6 (asociar semana), que sí está.

### A14-T8 — Flujo de caja totalizado por moneda + concepto/código; saldos banco en cartolas

- **Verbatim:**
  - Flujo: «cuánto se gastó independiente del banco»; totalizado; manda el **código financiero**; agrupado por **concepto** (servicios básicos, packing…); detalle de 50 facturas = otro reporte. `[01:08:27]`–`[01:12:36]`
  - Cartolas: «indicadores que digan cuánto saldo por los bancos» **y por moneda**. `[01:13:21]`–`[01:13:49]`
  - Mario envía Excel (WhatsApp 17:51; captura en `whisper-local/2026-09-14-interna-tesoreria/`).
- **Back:** **CUMPLE.** Rollup concepto+código+periodo, totales por moneda — `flujo-caja` / `tesoreria.service.ts`. Saldos — `getSaldosBancos`.
- **Front:** **CUMPLE.** `/tesoreria/flujo-caja` (`FlujoCajaPage.tsx`) sin columna banco en el Excel-like. `/tesoreria/cartolas` header de saldos banco×moneda. Maestro `/catalogos/conceptos-flujo`.
- **Estado conjunto:** **CUMPLE**  
- **Matiz:** consolidado **grupo** Almahue+ALM (pie del Excel de Mario) no está como vista «holding»; el flujo es por `empresaId`.

### A14-T9 — Maestro de concepto de flujo (coda interna, mismo día)

- **Qué:** Sergio a Carlos: el Excel se arma por concepto → códigos financieros. No lo pidió el cliente con esas palabras; el Excel de Mario **sí** trae esa jerarquía.
- **Back / Front:** **CUMPLE.** Modelo `ConceptoFlujo`, CRUD catálogo, FK en código financiero.
- **Estado conjunto:** **CUMPLE** (trazabilidad: interna 14/09 noche, alineada al Excel del cliente)

---

## D. Pantallas que el 14/09 recorrió — ¿existen?

| Ruta | Menú | Archivo | ¿Se ve lo acordado? |
|---|---|---|---|
| `/tesoreria/cartolas` | Tesorería › Cartolas | `CartolaBancariaPage.tsx` | Sí: import, saldos, T2, asociar nómina. **No** rango desde–hasta |
| `/tesoreria/flujo-caja` | Tesorería › Flujo de caja | `FlujoCajaPage.tsx` | Sí: totalizados moneda, concepto/código. No columna banco |
| `/tesoreria/nominas` | Tesorería › Nómina semanal | `NominasAgingPage.tsx` | Sí: semana, aplazar, default mes header. **No** contabilizar lote |
| `/tesoreria/cuentas-corrientes` | Tesorería › Estado de cuenta | `CuentasCorrientesPage.tsx` | Sí; **no** duplicado en Contabilidad |
| `/catalogos/conceptos-flujo` | Parametrización › Conceptos | `ConceptosFlujoPage.tsx` | Sí |
| `/compras/ordenes` + libro compras | Compras | `ComprasPages.tsx` | Badge OC sin aprobar. **No** alta/badge sin OC |
| Conciliación | Tesorería | `TesoreriaPages.tsx` | Vista/resumen |

Rutas en `ERP/erp_front/src/App.tsx` y `app/Sidebar.tsx`.

---

## E. Stock vigente que el 14/09 **no reabrió**

Sigue valiendo el corte 10/09 + dueño 03/09. Validación rápida para no diluir la lista fina:

| Id | Acuerdo | Back | Front | Estado |
|---|---|---|---|---|
| V-D4 | Aprobaciones solo OC; OV → `CONFIRMADA`; sin bandeja ventas | `ov-estado.util.ts`; no `solicitarAprobacionOv` | Sidebar `/compras/aprobaciones` | **CUMPLE** |
| V-D11 | Cotización sin CRUD | — | Redirect `/compras/cotizaciones` y `/comercial/cotizaciones` → `/compras/ordenes` (`App.tsx`) | **CUMPLE** |
| V-D16 | No vender bajo precio compra maestro | `comercial.service.ts` (~D16) + `comercial-ov.spec.ts` | OV/Emitir usan API | **CUMPLE** |
| V-Emitir | Sin cuenta/CC en Emitir | — | `mostrarCuenta={false}` en `EmitirDocumentoPage.tsx` ~2456 | **CUMPLE** |
| V-Libro | Cuenta+CC por ítem al contabilizar | `comercial.service.ts` contabilizar | Modal Libro ventas `ComercialPages.tsx` | **CUMPLE** |
| V-NC | CodRef 1/2/3 + TC origen | `referenciaCod`, `tipoCambio: origen.tipoCambio` | UI NC `ComercialPages.tsx` | **CUMPLE** |
| V-CC | Estado de cuenta por RUT, corte mes | `cuenta-corriente.service.ts` | Solo Tesorería | **CUMPLE** |
| V-NominaUI | Nómina no muta DTE; semana compromiso | aging `semanaCompromiso` | `NominasAgingPage.tsx` | **CUMPLE** |
| V-3FX | Triple conversión en el mayor | `Asiento.lineas` JSON monomoneda | Diario/Mayor | **PENDIENTE** |
| V-GS-Recep | GoSocket → libro compras en línea | gateway emisión sí | no hay bandeja recibidos SII | **PENDIENTE** (el 14 lo reabre: C4 + aceptar/reclamar) |
| V-SMTP | Correo PIN / alertas | — | — | **PENDIENTE** (H9; ahora también C4) |
| V-Exp | Set pruebas DTE exportación | parcial canónico | parcial | **PENDIENTE** |
| V-Reversa | Reversa contable reutilizable en Libro | API sí | botón/UX parcial | **PARCIAL** |
| V-SII-xlsx | Carga masiva SII + dedup solape | CSV/folio | parcial | **PARCIAL** |

---

## F. Lista para validar juntos (prioridad producto)

Orden sugerido al revisar back+front en `localhost:5174`:

1. **Libro de compras** — asociar factura a OC `PENDIENTE_APROBACION` → badge, no se contabiliza. **CUMPLE hoy.**
2. **Libro de compras** — intentar registrar factura **sin** OC (el 90 %). **No se puede en front.** ¿Aflojamos el `Completa OC y factura` y agregamos badge «Sin OC»?
3. **Cartolas** — saldos banco×moneda; contabilizar T2 con lookup factura; multi-select egresos → semana. **CUMPLE.** ¿Falta calendario desde–hasta?
4. **Flujo de caja** — totalizados CLP/USD/yuan; filas concepto/código; sin banco. **CUMPLE.** ¿Falta vista holding (Almahue+ALM) del Excel de Mario?
5. **Nómina** — mover factura de semana (tarjeta para Lupe). **CUMPLE.** Contabilizar **con** la nómina: **no está.**
6. **Alerta RUT** — no hay pantalla. ¿Watchlist en Admin + campana, o espera recepción GoSocket?
7. **Chipax** — no construir. Mario lo aplazó.

Nada de esta lista reabre D4, D11 ni D16.
