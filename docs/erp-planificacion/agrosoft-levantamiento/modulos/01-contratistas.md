> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`reunion6-minuta-2026-08-06.md`](../reunion6-minuta-2026-08-06.md) + código. Motivo: levantamiento Reu1 pantalla a pantalla; no spec ERP actual.

# Módulo: Contratistas

Partner agrícola: labores/actividades más específicas que industrial. Parametrización que hoy vive en Mano de Obra debe vivir aquí (**DEC-01**).

## Pantalla: Login / cambio empresa / temporada

- **Timestamp tl;dv:** 00:21–00:45
- **Captura:** `../pantallas-legacy/01-login-empresa.png`
- **Etiqueta:** REQ (empresa) · OPT (temporada funcional)

### As-Is
- Última empresa queda seleccionada.
- Selector de temporada existe pero “no sirve mucho” porque no usan Gestión.

### To-Be
- [REQ] Login + selector empresas con permiso.
- [REQ] Empresa activa siempre visible.
- [OPT] Selector temporada útil si se implementa reportería/gestión.

### Sesiones compartidas
- **Timestamp:** 01:39–02:45 · Captura `../pantallas-legacy/02-sesiones-compartidas.png`
- [DEC-08] 15 usuarios; a veces 2 personas / 1 login → la última empresa activa “se queda”.
- [REQ] Ideal: una sesión por usuario; advertencia si hay sesión concurrente; empresa visible.

---

## Pantalla: Listado / alta contratista

- **Timestamp:** 06:14–06:56
- **Etiqueta:** REQ

### To-Be
- [REQ] CRUD contratista + cambiar vigencia (no borrar histórico).
- [REQ] RUT único; campos obligatorios claros.

---

## Pantalla: Ingreso de tarifas (crítico)

- **Timestamp:** 04:34–10:50
- **Captura:** `../pantallas-legacy/03-tarifas-contratista.png`
- **Etiqueta:** REQ

### As-Is
- Al agregar 2ª tarifa/labor, la primera **desaparece** de la vista.
- Hay que limpiar y reingresar; no hay listado para revisar errores.
- Permite seleccionar centros de costo de **otra empresa**.

### To-Be
- [REQ] Tabla persistente de líneas (labor, actividad, tarifa, unidad, CC, fechas).
- [REQ] Agregar/editar/eliminar línea sin resetear el resto.
- [REQ] CC solo de empresa activa (**DEC-03**). Captura cross-empresa: `../pantallas-legacy/04-centros-costo-cross-empresa.png` @ 11:29.
- [REQ] Actividad ↔ Labor parametrizable aquí (no en Mano de Obra). Generalmente 1 labor/actividad; N:N permitido.

---

## Pantalla: Proforma + asociación factura

- **Timestamp:** 19:14–22:34
- **Etiqueta:** REQ

### As-Is
- Estados Borrador / Definitiva; definitiva bloquea cambios.
- **CRÍTICO:** cada contrato solo **una** factura; **no se puede cerrar el módulo** hasta asociar todos.

### To-Be
- [REQ] Flujo proforma → factura con estados.
- [REQ] Documentar/decidir política de cierre (PEND-02: ¿múltiples facturas?).
- [OPT] Reversión Definitiva→Borrador con auditoría.

---

## Pantalla: Traspaso contable + cierre de mes

- **Timestamp:** 22:38–25:53
- **Etiqueta:** REQ

### To-Be
- [REQ] Traspaso con tasas peso/dólar/yuan/euro (**DEC-05**).
- [REQ] Cierre de mes solo Admin; Digitador no parametriza ni cierra ni traspasa.
- [REQ] Traspaso deja pendiente “facturas por recibir contratistas” hasta ingreso factura.

## Permisos relacionados

Ver `05-permisos-config.md`. Captura perfiles: `../pantallas-legacy/05-perfiles-admin.png`.
