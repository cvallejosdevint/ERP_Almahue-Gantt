# Validacion errores demo 10/11/2026

Minuta: [`docs/reuniones/minutas/reunion-2026-11-10-cliente.md`](../../reuniones/minutas/reunion-2026-11-10-cliente.md)  
Transcripcion: [`docs/reuniones/transcripciones/transcripcion-2026-11-10-reunion.md`](../../reuniones/transcripciones/transcripcion-2026-11-10-reunion.md)

**Ambiente de retest:** local `http://localhost:5174` (admin@almahue.local), 10/11/2026 ~19:37. Viewport 1536x960 Playwright.  
**Deploy prod del dia:** fixes E1-E4 ya subidos (api/web 200) antes de esta validacion.

Capturas en `capturas/`.

---

## Errores de la muestra

| ID | Minuto sala | Sintoma en demo | Evidencia antes | Retest 10/11 noche | Estado |
|---|---|---|---|---|---|
| E1 | `[20:22]` | Crear/asignar cargo usuario: validacion "40 caracteres" / DTO | Relato sala | Modal editar usuario carga rama + cargo; guardar clave sin toast DTO | **Resuelto** |
| E2 | `[48:01]` | Error al asignar rama desde perfil/usuario | Relato sala | Mismo flujo editar usuario con rama seleccionada | **Resuelto** |
| E3 | `[01:03:41]` | Cambiar clave: toast `ramaId must be a string`, `codigo`, `nombre`, `rango` | [`E3-antes-error-cambiar-clave.png`](capturas/E3-antes-error-cambiar-clave.png) | Guardar clave Admin > toast de exito, **sin** errores DTO [`03-guardar-clave-resultado.png`](capturas/03-guardar-clave-resultado.png) | **Resuelto** |
| E4 | `[01:39:05]` | Ejecutar reversa: "Debes registrar tu clave de reversa en Mi Perfil" | [`E4-antes-error-clave-reversa.png`](capturas/E4-antes-error-clave-reversa.png) | Backend usa `assertPinAprobacion`; Mi Perfil solo PIN [`04-mi-perfil-pin.png`](capturas/04-mi-perfil-pin.png); modal pide PIN (codigo). En local no habia proforma "autorizada" para abrir Ejecutar | **Resuelto** (codigo + deploy; retest de Ejecutar en prod con MJ pendiente) |
| E5 | `[55:42]` | Crear ingreso diario fallaba | Relato sala | Era rama Contratistas sin modulo Compras; al corregir permisos/rama dejo crear | **No es bug** (config) |
| E6 | `[01:01:00]` | Proforma "borrador" vs "pendiente" | Relato sala | En sala luego aparecio en bandeja pendiente; sin reproduccion fallida nueva | **Aclarado** / vigilar |

### Capturas retest

| Archivo | Que muestra |
|---|---|
| [`01-usuarios-lista.png`](capturas/01-usuarios-lista.png) | Lista usuarios con cargo, rango y tope CLP |
| [`02-editar-usuario-con-clave.png`](capturas/02-editar-usuario-con-clave.png) | Modal editar + clave + rama/cargo cargados |
| [`03-guardar-clave-resultado.png`](capturas/03-guardar-clave-resultado.png) | Post-guardar sin errores `ramaId`/`codigo` |
| [`04-mi-perfil-pin.png`](capturas/04-mi-perfil-pin.png) | Solo PIN de aprobacion (no clave reversa separada) |
| [`05-organigrama.png`](capturas/05-organigrama.png) | Organigrama actual (sin vista simple / zoom) |
| [`06-proformas-lista.png`](capturas/06-proformas-lista.png) | Proformas local |
| [`08-solicitar-reversa-modal.png`](capturas/08-solicitar-reversa-modal.png) | Modal solicitud; texto habla de PIN, no de clave legacy |

---

## Acuerdos sala 10/11 - estado

| ID | Pedido sala | Evidencia / touch | Estado |
|---|---|---|---|
| P1 | Vista simple + detalle + zoom organigrama `[24:08]` | UI organigrama (sesion cierre 11/11) | **Listo** (cerrar en QA humano) |
| P2 | Tope por moneda editable en ficha usuario `[23:02]` | Modal usuario CLP/USD/CNY | **Listo** (cerrar en QA humano) |
| P3 | Rangos por color (MJ manda paleta) `[48:26]` | `lib/rango-colores.ts` | **Listo** (paleta fija 1-9; falta OK MJ) |
| P4 | Identificar VºBº reversa en edit rama `[01:58:14]` | Parametro Empresa (no por rama) `VbReversaParamPage` | **Listo** (corte 11/11) |
| P5 | Tras 2 VºBº, auto ejecutar reversa sin PIN solicitante `[01:41:05]` | `aprobarVbContabilidadSolicitud` auto-llama `reversarProforma`; UI toast + protocolo | **Listo** (11/11) |
| P6 | Mantenedor temporadas (sep-ago / may-abr) `[54:21]` | `/catalogos/temporadas` | **Listo** |
| P7 | OC servicio: RECEPCIONADA + asiento en recepcion; no centralizar servicios `[02:05:18]`, `[02:10:59]` | Gate `oc-estado.util`; asiento `RECEPCION:`; centralizacion omite SERVICIO/ACTIVO_FIJO | **Listo** (11/11) |
| P8 | Usuario con dos jefaturas visible en ficha `[01:57:06]` | `cargosAsignados` / multi jefatura | **Listo** |
| P9 | Correo contratista solo post-aprobacion (check ok) `[01:00:03]` | Confirmado en sala | **Vigilar** |

### Detalle P5 (auto-ejecutar) - 11/11/2026

- Al otorgar el 2º VºBº Contabilidad, el backend ejecuta la reversa de la proforma vinculada sin pedir PIN ni clic del solicitante.
- Si la auto-ejecucion falla, deja `edicionHabilitada` y notifica para completar manual en Proformas (boton Ejecutar sin PIN).
- Front: toast en Contabilidad › Reversas; textos de protocolo actualizados.

### Detalle P7 (servicio fuera de centralizacion) - 11/11/2026

- Factura de OC SERVICIO solo tras estado RECEPCIONADA (ya vigente).
- Recepcion confirmada arma asiento individual gasto vs Facturas por recibir.
- Traspaso/centralizacion mensual solo admite origen `contratistas`; rama defensiva de `compras` omite SERVICIO/ACTIVO_FIJO con motivo explicito.

---

## Checklist retest

- [x] E3 cambiar clave sin toast DTO (local)
- [x] Mi Perfil = PIN, no clave reversa
- [x] Codigo reversa > `assertPinAprobacion`
- [ ] E4 / P5 smoke prod: 2º VºBº Contabilidad auto-ejecuta reversa (sin PIN solicitante)
- [x] P5 + P7 implementados en codigo 11/11 (auto-ejecutar + servicio fuera de centralizacion)
- [ ] Pasada humana con capturas de P5/P7 en prod tras deploy
