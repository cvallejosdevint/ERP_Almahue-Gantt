# Demo cliente 10/09/2026 — Meet «ERP Almahue - Avances»

**Tipo:** Demo de ventas (exportación + nacional) + NC/ND + planificación. **Cliente en sala.**  
**Fecha:** jueves 10/09/2026 · grabación ~17:13 (el Meet en pantalla marca ~16:00).  
**Duración útil:** ~[02:54]–[59:50] (~57 min; el MP4 dura 01:14:14, cola en silencio / calendario Meet).

**Participantes (cliente = requisito):** María Jesús / MJ, Lupe, Pía (COMEX), Mario (entra ~[46:01]).  
**Devint:** Carlos Vallejos, Sergio Silva, Felipe Cuevas (levantamiento; en `[04:17]` Carlos dice que Felipe queda de escucha).  
**Nombrados:** José y Diego (se incorporarían al proyecto, Sergio `[51:56]`); Pablo/Cristian GoSocket (contrato/factura, no ERP).

**No es Reu7 canónica.** MJ manda sobre Carlos/Sergio. Lupe/Mario/Pía son cliente operativo (regla `almahue-reuniones`).

| Fuente | Ubicación |
|---|---|
| Transcripción ASR | [`fuentes/transcripcion-2026-09-10-demo-cliente.md`](fuentes/transcripcion-2026-09-10-demo-cliente.md) |
| Whisper + wav | `fuentes/whisper-local/demo-2026-09-10/` (wav gitignored) |
| Video | `fuentes/videos/reunion-2026-09-10-demo-cliente.mp4` (gitignored) + origen Screen Recordings `171320` |

La grabación muestra **localhost:5174** (ALMAHUE EXPORT SPA) y, a la vez, el deploy a `45.7.229.46` que se avisó en esta misma sesión.

---

## 1. Cómo les fue

Bien. MJ/Pía: «buenísimo», «superbuena», «voy maravilloso» `[32:58]`, `[44:30]`. Mario entra al cierre y no pide rehacer la demo. Quedó **marcha blanca** en sandbox GoSocket y **próxima reunión lunes 15/09 17:00** (MJ se va de vacaciones el martes).

---

## 2. Pedidos a corregir (cliente)

Ordenados por quien lo pidió. Citas de la transcripción (ASR).

### MJ

1. **NC/ND CodRef 3: poder editar el tipo de cambio.** Que venga el de la **factura origen**, no el del día; **un TC para toda la nota**, no por ítem. `[25:02]`–`[26:37]`. (Hoy el cierre COMEX lo deja solo lectura; esto **cambia** ese diseño si se implementa.)
2. **Venta nacional (ALM): D16 se cayó en la demo.** No vender bajo el precio de bodega; **mostrar el precio de bodega** en la OV; mayor o igual. `[27:42]`–`[29:03]`. Carlos reconoció que la restricción «se eliminó» al aplicar DTE exportación `[28:17]`.
3. **Exportación: el precio no es el de bodega** (se calcula). ALM sí se alimenta de bodega; Almahue Export no. `[23:34]`–`[24:52]`, `[46:40]`.
4. **Panel COMEX: resumen del cliente** (y lo ya cargado en pasos anteriores) para no perder el receptor al cambiar de pestaña. `[35:34]`–`[36:08]`. Pía no veía el receptor.
5. **Puertos filtrados por país** (desembarque). Ejemplo: China → solo puertos de China. **Chancén** no está en el combo (sí lo veían en SII). `[36:26]`–`[37:36]`.
6. **NC de compras / existencias:** si hay devolución a proveedor sobre una OC/factura, **no forzar precio promedio de bodega**; precio de la factura / manual. `[29:05]`–`[31:34]`. Quedó para **próxima revisión de compras**, no de esta demo de ventas.
7. **Centro de costo** sale de parametrización (no datos demo raros). `[20:23]`–`[20:58]`.
8. **Códigos de producto** a estandarizar desde maestro (cereza / nectarín), no inventar en la emisión. `[40:26]`–`[40:57]`.

### Pía (COMEX)

9. Confirmar **campos obligatorios** vs manual de facturación; algunos no son SII-obligatorios pero ellos los quieren. Marca de bulto. `[34:00]`–`[34:58]`.
10. TC del Banco Central y conversión a pesos: validó que está bien `[33:18]`–`[33:39]`.

### Mario (cierre)

11. **Casilla SMTP propia** en parametrización; él arma la cuenta. Distintos **formatos**: notificación de aprobaciones vs correo al **cliente** con PDF de factura (razón social, total, forma de pago). `[52:16]`–`[55:16]`. Sergio abre tarjeta Trello.

### Lupe / MJ (plan)

12. Mientras MJ está de vacaciones: **tesorería con Lupe**, **abastecimiento/compras con Mario**. `[13:50]`–`[14:21]`.

---

## 3. Compromisos Devint (Carlos / Sergio)

| Qué | Quién lo dijo | Minuto |
|---|---|---|
| Cadena Libro: NC solo del mismo tipo DTE (no folio 70 cruzado) | Carlos (ya hecho en local; deploy en la reunión) | `[03:03]` |
| Tras CodRef 3, no CodRef 1; mensaje de saldo | Sergio + Carlos | `[04:46]`–`[05:22]` |
| TC de NC/ND = el de la factura (no reingresar) | Carlos, alineado con MJ | `[16:42]`–`[17:34]` |
| Selectores de moneda **solo** los de parametrización | Carlos (dijo que falta) | `[16:19]`–`[16:26]` |
| TC editable en corrige montos, heredado de la 110/33 | Carlos «sí se puede» | `[26:16]`–`[26:24]` |
| Arreglar filtro Libro post-emisión (folio 76 no filtró) | Carlos | `[27:30]`–`[27:40]` |
| Restaurar D16 nacional + mostrar precio bodega | Carlos | `[28:15]`–`[29:03]` |
| NC compras precio manual / de factura | Carlos: revisar e implementar; próxima revisión | `[30:30]` |
| Usuarios de prueba por WhatsApp (no admin); marcha blanca | Carlos | `[41:55]`–`[42:19]` |
| Ejemplo de asiento de venta | Carlos pidió; **MJ envió correo + PDF** en la misma reunión | `[49:34]`, `[56:32]`–`[57:14]` |
| SMTP + diseño de correos; Trello | Sergio + Mario | `[52:16]`–`[53:37]` |
| Semana del **23/09**: tesorería a fondo con Lupe | MJ | `[50:19]` |
| **Lunes 15/09 17:00** reunión de planificación (módulos y encargados), no solo demo | MJ; si se corre, martes con «los chicos» | `[57:38]`–`[59:02]` |
| 1ª semana de **octubre** presencial, premarcha blanca con datos reales | Sergio | `[47:43]`–`[49:18]` |

Carlos/Sergio **no** son fuente de verdad en lo que solo ellos proponen (p. ej. «referencia a bodega pero no restrictivo» `[24:18]` — MJ cortó con «No» `[24:24]` para exportación).

---

## 4. Qué ya se dio por OK en sala (no reabrir como hueco nuevo)

- Flujo OV export → Guardar → Facturar (resumen) → Libro con filtro folio+tipo.
- COMEX: países, vía, cláusulas, TC BCCH, USD/EUR/yen, panel de totales USD + CLP.
- Contabilizar: cuenta + CC por ítem; cliente/RUT/giro arriba.
- PDF GoSocket sandbox.
- Anulación / corrige montos / texto; origen-cadena de **movimientos** de esa factura.
- Tracking compartido; correo de DTE deshabilitado hasta SMTP.
- Ambiente de pruebas: no va al SII live; sí consume CAF sandbox.

---

## 5. Pendientes extra (no nuevos de esta hora, pero se tocaron)

- **H9 SMTP** (ya estaba en huecos): ahora hay dueño (Mario) y fecha de configuración.
- **D16** nacional: tratar como **regresión** si en código local sigue fallando (la demo lo mostró roto).
- **GoSocket comercial:** MJ `[18:37]` Cristian no manda cuenta ni contrato — operativo partner, no ERP.
- **Usuarios no-admin** para marcha blanca: falta que MJ mande correos por WhatsApp.
- **Carga de maestro** productos/CC reales en el tenant de pruebas.
- **Compras / existencias / OC anticipada Cartocor:** explícitamente **fuera** de esta entrega de ventas.
- **Guías:** Mario las nombra al entrar `[46:05]`; no se recorrieron.

---

## 6. Cómo leer el ASR

Whisper `small` confunde: COMEX, bodega, D16, GoSocket, nectarín, Chancén, parametrización, «anulación» vs corrige montos. Contrastar con el video en esos minutos antes de codear el TC editable en NC (choca con el diseño COMEX de «TC de la 110, no se edita»).
