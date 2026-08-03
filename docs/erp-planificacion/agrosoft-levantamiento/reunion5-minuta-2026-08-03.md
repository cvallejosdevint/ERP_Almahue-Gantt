# Reunión 5 — Minuta y plan accionable (03/08/2026)

**Fecha calendario:** lunes 03/08/2026  
**Próxima revisión:** **mañana (04/08) a la misma hora** — revisar ajustes implementados  
**Objetivo:** demo local de avances post Reu4 (PIN, aprobaciones, libros, emisión, param, tesorería) + feedback Sergio  
**Participantes:** Carlos (Devint), Sergio (Devint); intervención corta de un tercero

| Fuente | Ubicación |
|---|---|
| tl;dv | https://tldv.io/app/meetings/6a71065851275b0013b6f1d9 |
| Video local (gitignored) | [`fuentes/videos/reunion5-2026-08-03.mp4`](fuentes/videos/reunion5-2026-08-03.mp4) |
| Video origen | `c:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-03 164322.mp4` |
| Minuta cruda tl;dv | [`fuentes/reunion5-minuta-tldv-2026-08-03.md`](fuentes/reunion5-minuta-tldv-2026-08-03.md) |
| Transcripción | [`fuentes/transcripcion-reunion5.md`](fuentes/transcripcion-reunion5.md) |
| Ruta demo usada | [`ERP/qa-reu4-2026-07-31/13-RUTA-PRESENTACION-BRECHAS-P0-P1.md`](../../ERP/qa-reu4-2026-07-31/13-RUTA-PRESENTACION-BRECHAS-P0-P1.md) |

> tl;dv etiquetó los action items como “Sergio implementar…”. **Quién implementa = Carlos / equipo Dev.** Sergio pide y valida.

---

## 1. Resumen ejecutivo

Demo **local** (sin deploy al server). Se validó PIN por rol/usuario, aprobaciones de proforma/OC (admin puede aprobar con advertencia), print OC con CC, borradores de emisión, libros separados, param reordenado. Sergio compartió referencia Better Software / Demirel (resumen por tipo doc, preview PDF, menú de acciones). Quedó backlog fuerte de UX/libros/periodos/tesorería y **cita mañana** para revisar lo implementado.

**Bug en sala:** factura `88001` no se reflejaba bien en Estado de cuenta (posible efecto del wipe de BD pre-demo).

---

## 2. Decisiones de producto

| # | Decisión | Implicancia |
|---|---|---|
| D1 | Cambio de PIN: pedir **contraseña de la cuenta** (no correo, por ahora) | Menos fricción que mail; mitiga PC desbloqueado |
| D2 | Admin puede ver/aprobar solicitudes de otros con **advertencia** (“súper jefe”) | Mantener; fácil restringir si lo piden |
| D3 | **Centro de costo por ítem** en OC (no solo cabecera) | Ajuste modelo/UI líneas OC |
| D4 | Emisión: pantalla **redimensionable / expandible** (ref. Better Software) | UX ventana |
| D5 | **Todos los libros** con totalizados; resumen por tipo doc **colapsable** (panel) | NC restan; ND / afectas / exentas suman |
| D6 | Acciones tipo Better Software: pago / facturar / imprimir / correo / adjuntar / anular | Correo stub sin SMTP; adjuntos sí |
| D7 | Preview: folio/PDF abre vista; preferir print nativo del navegador | Folio clickeable (estilo botón/borde) |
| D8 | Filtros de libros: funcionan → **rehacer estética** | Ref. UI que pasó Sergio |
| D9 | Multi-periodo en libros: **máx. año actual** + paginación; rangos vía búsqueda avanzada | Evitar freeze (22k docs/mes) |
| D10 | Borradores: viven en el usuario; admin puede listar **todos** con **filtro usuario** | Ver / Cargar a emisión |
| D11 | Cotizaciones ≈ OC; quitar mantención clientes embebida; alta cliente = **+** → panel derecho | Campos: RUT, RS, dir, comuna, ciudad, tel, mail |
| D12 | Completar campos emisión factura (neto/exento/IVA/desc. globales y línea); **replicar** a cotiz. y OC | Orden de trabajo: factura → resto |
| D13 | **Ventas sin centro de costo**; compras / facturas recibidas **con** CC | Aclara duda Reu4 |
| D14 | Quitar “cambiar periodo activo” desde Contabilidad (confunde); control desde selector de trabajo | Sí: historial abrir/cerrar + **motivo** al reabrir |
| D15 | Productores: solo Parametrización (sacar duplicado de Compras) | Menú |
| D16 | Config SII/SAI: dejar hasta docs GoSocket (no inventar) | Diferido |
| D17 | Estado de cuenta: columna **tipo de movimiento** (venta/compra/…) | + fix 88001 |
| D18 | Cartolas bancarias: **pendiente** (aún no tocado) | Próximo bloque tesorería |

---

## 3. Action items — Dev (para revisión 04/08)

Prioridad sugerida para “mañana a la misma hora”:

### P0 — Cerrar antes / durante la demo de mañana

| # | Acción | Notas |
|---|---|---|
| A1 | Al cambiar PIN, exigir **password de cuenta** | Acordado vs correo |
| A2 | OC: **CC por ítem** | Confirmado Sergio |
| A3 | Libro compras: **totalizados** (como ventas) | Todos los libros |
| A4 | Fix Estado de cuenta: doc `88001` / detalle click | Revisar seed + query |
| A5 | Estado de cuenta: columna **tipo movimiento** | Venta / compra / … |
| A6 | Quitar Productores duplicado de Compras | Solo Param |
| A7 | Cotizaciones: folio **clickeable** (estilo botón/PDF) | Libro cotizaciones |
| A8 | Sacár/ocultar “cambiar periodo” confuso en Contabilidad | Dejar historial |

### P1 — UX libros / emisión (referencia Better Software)

| # | Acción | Notas |
|---|---|---|
| A9 | Emisión redimensionable / expandible | |
| A10 | Panel resumen por tipo doc **colapsable** | NC − / ND + |
| A11 | Menú acciones alineado (pago, facturar, print, mail stub, adjuntar, anular) | Mail sin server |
| A12 | Reformular filtros libros (estética) | Ref. Sergio |
| A13 | Multi-periodo: tope **1 año** + paginación | Avanzada = rangos |
| A14 | Admin borradores: filtro por usuario | Ver / Cargar |
| A15 | Alta cliente desde cotiz: ícono **+** → panel derecho | Campos completos |
| A16 | Campos totales emisión (neto/exento/IVA/desc.) | Luego replicar cotiz/OC |

### P2 — Contabilidad / tesorería

| # | Acción | Notas |
|---|---|---|
| A17 | Historial apertura/cierre de periodos | Quién / cuándo |
| A18 | Motivo obligatorio al **reabrir** periodo cerrado | |
| A19 | Módulo **cartolas bancarias** | Aún no iniciado |
| A20 | Conciliación: asegurar resumen con datos | Falló post-wipe |

### Externo / agenda

| Quién | Acción |
|---|---|
| Carlos + Sergio | Reunión **04/08 misma hora** (avisar si hay avances antes) |
| Sergio | Pasar refs UI / acciones Better Software (si no quedaron en chat) |

---

## 4. Validado en demo (no reabrir salvo regresión)

- PIN habilitado por **rol**; PIN **por usuario** (cambiar/restablecer)
- Aprobaciones proforma + compras con PIN; solicitante elige aprobador
- Admin ve todas + advertencia al aprobar “por otro”
- Libro ventas sin shortcuts a compras; solo contabilizados en libro
- Borradores en menú rápido de emisión; solo del usuario (hoy)
- Parametrización reordenada (pedido Mari)
- Filtros Estado de cuenta Todos / Pendientes

---

## 5. Diferidos (igual que Reu4 / explicitados)

- Correo real (cambio PIN / envío documentos) → falta SMTP
- GoSocket / config SII “seria” → docs
- Cartolas Excel finas → material MJ + trabajo A19
