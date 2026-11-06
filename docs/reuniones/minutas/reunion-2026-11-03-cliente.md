# Reunion Almahue - 03/11/2026 (Minuta para desarrollo)

| Parametro | Detalle |
|---|---|
| **Fecha** | 03/11/2026 |
| **Fuente AM** | `Screen Recording 2026-11-03 115116.mp4` (00:42:16) |
| **Fuente PM** | `Screen Recording 2026-11-03 173934.mp4` (02:38:24) |
| **Transcripcion** | [`transcripcion-2026-11-03-reunion.md`](../transcripciones/transcripcion-2026-11-03-reunion.md) |
| **Minuta interactiva** | [`reunion-2026-11-03-cliente-interactiva.html`](reunion-2026-11-03-cliente-interactiva.html) |
| **Modelo STT** | faster-whisper `large-v3` + lexico ERP |

**Participantes (segun transcripcion):** Devint (Carlos, Sergio en demo AM). Voz cliente / operacion en PM (preguntas de negocio tipo contabilidad y modulos; no siempre con nombre). AM incluye coordinacion con Jose (AlmaWeb / Temite) y referencias a Maria Jose (MJ), Mario, Diego.

**Nota:** Carlos/Sergio en demo = hipotesis de implementacion hasta contrastar con voz cliente en la cita.

---

## 1. Contratistas: reversa, periodo y traspaso (AM) `[00:35 - 03:46]`

* **Sin reapertura desde Traspaso y cierre:** Quitar boton de reapertura en traspaso/cierre contable de contratistas. Cualquier correccion de proforma se inicia con **solicitud de reversa desde la proforma**, no reabriendo el panel de cierre. `[00:50]`, `[01:12]`
* **Periodo abierto vs cerrado:** En periodo **abierto**, al solicitar reversa debe abrirse el **wizard** (motivo + PIN) y quedar visible el flujo de **dos vistos buenos** (jefatura contratistas + contabilidad). **Bug acordado:** hoy no levanta el wizard y en periodo cerrado aparece mensaje incorrecto; en periodo cerrado aun se ve habilitada la reversa cuando no deberia. `[01:45]`, `[02:13]`, `[03:24]`
* **Filtro de proformas por periodo:** No mostrar proformas de periodos anteriores en la grilla del periodo actual. `[30:02]`, `[30:45]`
* **Indicador factura vinculada:** Mostrar recuadro de factura asociada **solo** si existe vinculo real; si no hay factura, no mostrar el bloque. `[30:55]`
* **Demo sin modo demo:** Continuar pruebas con **facturacion real entre empresas** (no modo demo) para centralizar, reversa y trazabilidad end-to-end. `[02:38]`, `[02:44]`

---

## 2. AlmaWeb / Temite (AM, coordinacion Jose) `[35:23 - 41:51]`

* **Prioridad externa:** Compromisos de fechas en Temite/AlmaWeb retrasados; se pide apoyo de Devint sin bloquear entrega ERP acordada. `[35:23]`, `[35:34]`
* **Pendientes AlmaWeb (MJ):** (1) tema de **numeros** en portal; (2) permisos **usuarios administradores** vs carga de evidencias desde portal (Paola). Corregir en AlmaWeb. `[36:49]`, `[40:15]`, `[40:30]`
* **Compromiso operativo:** Mario arma **documento consolidado de pendientes** AlmaWeb; Devint indica que puntos ya resueltos no se dupliquen en el archivo. `[40:39]`, `[40:51]`, `[41:14]`

---

## 3. Admin, roles y aprobaciones (PM) `[02:23 - 08:16]`

* **Usuarios en reglas de aprobacion:** Al crear grupo/regla de aprobacion (ej. OC), debe listarse claramente **quienes ya tienen el rol**; hoy la UI queda restrictiva y confusa. `[02:23]`, `[05:22]`
* **Mejora UX:** Preferencia de ver **todos los usuarios** con el **grupo/rol actual** al armar la cadena, no ocultar opciones. `[07:21]`, `[08:16]`

---

## 4. DTE / GoSocket (PM) `[08:16 - 09:44]`

* **Lentitud sandbox:** Desde ~12:00 del dia anterior, GoSocket muy lento (~15 min por factura); impacta demo de PDF/XML en pantalla. Seguir emisiones reales pero tolerar demora en reunion. `[08:16]`, `[18:47]`
* **Plantilla PDF:** Documento interno personalizable se ve distinto al PDF GoSocket; validar paridad visual en otro hito. `[09:28]`

---

## 5. Proformas, asociacion factura y notificaciones (PM) `[09:44 - 19:34]`

* **Estados:** **Definitiva** = proforma asociada a ingreso diario; **Notificada** = envio de correo con tracking registrado. `[09:44]`, `[09:51]`
* **Asociar proforma-factura:** Una proforma **no** puede asociarse a mas de una factura ni reutilizar facturas ya calzadas. `[12:30]`, `[19:19]`, `[19:24]`
* **Feedback visual:** Al asociar, mostrar aviso en **verde** cuando cuadra (no solo naranja cuando descuadra). `[17:45]`, `[18:16]`
* **Notificacion al asociar:** Al confirmar asociacion, disparar **notificacion interna + correo**. `[15:52]`, `[15:58]`
* **Descuadres:** Si monto o periodo no calza (ej. neto vs bruto, dias fuera del rango), **notificar al usuario que creo la proforma**. `[14:17]`, `[15:19]`
* **Vista proforma:** En detalle de proforma debe verse si ya tiene factura asociada; factura asociada no debe reaparecer en listado para otra proforma. `[19:09]`, `[19:24]`

---

## 6. Insumos: OC madre, hijas y guias (PM) `[19:34 - 21:56]`

* **Hijas por guia:** Cada recepcion con guia que no cierra la madre genera **OC hija**; varias hijas pueden apuntar a **una o mas facturas** de la madre. `[19:42]`, `[20:35]`, `[20:46]`
* **Regla de cierre:** Solo la **ultima guia de despacho** de la compra puede generar el ajuste/hija final; si no cuadra, emitir **nueva OC madre** (un solo ajuste por madre). `[21:32]`, `[21:42]`, `[21:44]`
* **Traspaso y cierre:** Proformas/facturas aprobadas y facturadas deben reflejarse en traspaso/cierre insumos/contratistas segun corresponda. `[21:56]`

---

## 7. Contabilizacion contratistas vs libro de compras (PM) `[22:28 - 01:05:42]`

* **Dos pasos contables:** (1) Cierre contratistas: **gasto mano de obra vs facturas por recibir** al centralizar proformas. (2) Libro de compras: al contabilizar factura DTE, **facturas por recibir (debe) vs proveedor (haber)** + IVA. La factura asociada a proforma queda **bloqueada** pero **no contabilizada** hasta libro compras. `[23:52]`, `[24:35]`, `[25:23]`
* **Libro compras - UX:** Mostrar facturas de contratistas con **cobertura 100%** vs proforma; filtro/vista por proveedor **individual** (no solo total agregado); segunda etiqueta **contabilizada / pendiente** junto a OC o proforma vinculada. `[26:06]`, `[26:40]`, `[27:00]`
* **Calce modular:** Compras es checklist de documentos que llegan por GoSocket; el **reconocimiento de gasto** ocurre en cierre de cada modulo. `[01:04:40]`
* **Proformas sin factura en mes:** Puede haber proformas aprobadas en un mes y factura en el siguiente; facturas por recibir debe permitir detectar documentos faltantes. `[01:03:33]`, `[01:04:00]`

---

## 8. Reversas y cierres de mes (PM) `[27:36 - 31:06]`

* **Mes contable cerrado:** Sin modificaciones directas; reversa vía **solicitud con doble VB** (contratistas + contabilidad). `[28:57]`, `[29:25]`
* **Dos niveles de cierre:** Cierre **modulo** (mensual operativo) vs cierre **contable** (periodo). Alinear botones: no reabrir centralizacion desde contabilidad si el modulo ya cerro; reversa desde proforma es el camino. `[29:03]`, `[30:54]`, `[31:06]`
* **Traspaso/cierre UI:** Mostrar **nombre completo** de cuenta/insumo ademas de codigo en resumen de centralizacion. `[22:28]`

---

## 9. Insumos / bodega / guias en compras (PM) `[01:07:45 - 01:28:15]`

* **Pestaña compras:** En flujo compras-contratistas, donde hoy se habla de guias, debe poder asociarse **proforma aprobada** y contabilizar factura en modulo compras (no duplicar logica en contratistas). `[01:07:04]`, `[01:08:28]`
* **Cierre bodega ALM:** Consumo mensual por receta; ajustes de temporada al cierre. Separar **estado operativo** vs **estado contable** en columnas o doble etiqueta (aprobado vs contabilizado). `[01:28:08]`

---

## 10. DTE guias / recepcion insumos (PM) `[01:14:25 - 01:21:21]`

* **Recepcion vs maestro:** Matching de lineas por **codigo** de producto, no solo nombre (nombres truncados en pantalla). `[01:20:51]`, `[01:21:21]`
* **Habilitacion recepcion:** Ajustar reglas para permitir recepcionar cuando corresponda (caso probado en reunion con habilitacion manual). `[01:14:25]`

---

## 11. Compromisos y proximos pasos

1. **Corregir wizard reversa proforma** (periodo abierto, doble VB, ocultar reversa en periodo cerrado). Responsable: Devint. Evidencia: AM `[01:32]`, `[03:24]`.
2. **Filtro proformas por periodo + indicador factura condicional.** Devint. AM `[30:02]`, `[30:55]`.
3. **Asociacion proforma-factura:** bloqueo 1:1, badge verde al cuadrar, notificacion mail al asociar, aviso a creador si descuadra. Devint. PM `[17:45]` - `[19:24]`.
4. **Libro compras contratistas:** contabilizar contra facturas por recibir, filtros y estado contabilizada/pendiente. Devint. PM `[25:23]` - `[26:45]`.
5. **OC insumos madre/hijas:** mantener regla ultima guia y multiples facturas por madre. Validar en QA. PM `[20:35]` - `[21:44]`.
6. **Roles/aprobaciones:** listado claro de usuarios al crear reglas OC. Devint. PM `[05:22]`, `[07:21]`.
7. **AlmaWeb (Jose/Mario/MJ):** documento de pendientes y correccion numeros + admin portal. **Fuera del repo ERP** pero bloqueante operativo. AM `[40:30]` - `[41:14]`.
8. **Segunda vuelta UX modulo compras** (vista libro / calce visual). Cliente PM `[26:56]`, `[27:23]`.

---

## Referencias

- Parte AM en transcripcion: encabezado `## Parte AM`
- Parte PM en transcripcion: encabezado `## Parte PM`
- Informe consolidado previo (26-28/10): `docs/reuniones/analisis/13-informe-consolidado-lunes-martes-miercoles-2026-10-28.md` (no sustituye esta minuta)
