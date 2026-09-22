# Tesorería — nómina primero (14/09/2026)

**Tipo:** plan de tarjetas post Meet cliente. **No hay código en esta tanda.**  
**Fecha:** lunes 14/09/2026 · Meet «ERP Almahue - Avances» ~77 min.  
**Cliente = requisito:** Mario (sala), María Jesús / MJ, Lupe (invitadas).  
**Devint en sala no es fuente:** Carlos, Sergio.

| Fuente | Ubicación |
|---|---|
| ASR | [`fuentes/transcripcion-2026-09-14-demo-avances.md`](fuentes/transcripcion-2026-09-14-demo-avances.md) (Whisper `small`; contrastar video) |
| Índice videos | [`reunion-2026-09-14.md`](reunion-2026-09-14.md) |
| Contrato que esto pisa en el **origen del asiento banco** | [`plan-tesoreria-ciclo-completo-2026-08-21.md`](plan-tesoreria-ciclo-completo-2026-08-21.md) F0 |
| T2 28/08 que esto pisa como **flujo feliz** | [`reunion-2026-08-28-tesoreria-mj-lupe.md`](reunion-2026-08-28-tesoreria-mj-lupe.md) §2.2 · Trello T2 en [`pm-barco-almahue-2026-08-31.md`](pm-barco-almahue-2026-08-31.md) |

**Frase que cierra el rediseño (MJ):** «Contabilizar con la nómina, no con la cartola» `[57:52]`.

**Cómo usar el tablero:** Sergio `[01:15:55]` — primero **ajustar tarjetas en columna Devint**; **no** pasar el paquete tesorería a Lupe. Solo la **nómina semanal (T5 UX)** está lista para que Lupe la mire. Semana tesorería a fondo con Lupe: a partir del **23/09** (pedido 10/09).

---

## 1. Qué cambia vs qué se queda

Tesorería **sigue sin crear la deuda** (la deuda nace en libro). Cambia **cuándo se mueve el mayor y el banco**.

```
Hoy (21/08 + T2):     Libro (deuda) → cartola 1:1 (asiento banco) → nómina solo mueve semana
Quedó (14/09):        Libro (deuda) → confirmar nómina (asiento puente, baja CC) → cartola cruza banco
```

| Pieza | 21/08 + T2 | 14/09 | ¿Pisa? |
|---|---|---|---|
| Asiento banco / mayor de tesorería | Línea de cartola `CARTOLA:{id}` | **Confirmar nómina** → asiento contra cuenta **puente** (no banco aún) | **Sí — F0 y T2 como flujo feliz** |
| Cartola | Lugar donde se contabiliza 1:1 | **Cruce** con nóminas (fecha + monto; casi todo transferencia) | **Sí — T2** |
| Pago operativo / CC / aging | Calce; sin asiento `PAGO:{id}` | Sigue sin `PAGO:{id}`. El asiento nuevo es **`NOMINA:{id}`** (o equivalente) vs puente | No reabre `PAGO:{id}` |
| Nómina T5 (calendario, aplazar, export) | Semana de compromiso; **no** asienta | UX **se queda**; al **confirmar** ahora **sí asienta** | **Amplía T5**; no tirar la pantalla |
| Conciliación | Resumen informativo (R4-19) | Elegir **factura o nómina**; multi-egreso si el total calza | **Sí — R4-19 “solo vista”** |
| Match auto RUT+monto / Chipax | Diferido | Mario: echar a andar, automatizar **el año que viene** `[50:34]` | **Sigue diferido** |
| T1 TC productor, T4 yuan/BC, T6 estado de cuenta | Hecho local | No se tocó | **No pisa** |
| Código financiero | En movimiento de cartola (T2/T3) | Sigue alimentando el **flujo**; no va en el asiento **banco** como CC | Ajusta T3, no inventa catálogo nuevo |
| Centro de costo en asiento banco de cartola | Duda interna 14/09 mañana | **No** `[36:22]`–`[37:08]` | Cierra la duda: no hacer |
| Lista negra proveedores | — | **No va** `[35:46]` | No abrir tarjeta |

**T2 no se borra del todo:** queda como **excepción** (traspaso, sueldo, movimiento que no nació en nómina). El 1:1 deja de ser el camino de los egresos de facturas.

---

## 2. Orden en Trello

Etiquetas: `tesoreria` · `14/09` · `cliente-MJ-Mario`.  
Columna actual: **Devint / correcciones**. No QA Almahue salvo T8-QA.

Orden de implementación cuando haya código: **T8-0 → T8-A → T8-B → T8-C → T8-E → T8-D → T8-F → T8-G → T8-I → T8-H**. T8-QA en paralelo cuando T5 esté estable en prod.

### T8-0 — Reordenar tablero (operativo, 0 código)

**Pisa:** ninguna de producto.  
**DoD:** tesorería (salvo T5) vuelta a columna Devint; texto de T2/T3/T5 actualizado con un renglón «superseded by T8-A/C/F»; Chipax/Fintoc y match auto **fuera** o en «después de marcha blanca».

---

### T8-A — Confirmar nómina asienta (P0)

**Pisa:** F0 (asiento = cartola) · T2 como camino feliz · T5 «nómina no muta asiento».  
**Fuente:** MJ `[54:47]`–`[57:52]`, Mario sostiene el puente `[56:25]`–`[56:47]`.

Al **confirmar** la nómina semanal:

- Asiento: CxP/CxC (facturas tiqueadas) **contra cuenta puente** («nómina» / «conciliación cartola» — el nombre lo fija Almahue en parametrización).
- Baja deuda en cuenta corriente y aging.
- **No** toca cuenta banco.
- Idempotente: reconfirmar no duplica.
- Reversa: solo periodo abierto; deja la nómina otra vez editable.

**DoD:** una nómina de 3 facturas genera 1 asiento (o 1 por factura, a definir con MJ en la prueba; default **un asiento con N líneas**); mayor y CC cuadran; banco intacto.

**Abrir con MJ en la prueba (no inventar ahora):** ¿un asiento por nómina o uno por factura? El audio mezcla «egreso automático» y «asiento por asiento». Default de implementación cuando toque código: **un asiento por nómina**.

---

### T8-B — Cuenta puente parametrizable (P0, bloquea T8-A)

**Pisa:** nada. Habilita T8-A.  
**Fuente:** MJ `[54:53]`–`[56:39]`.

- Maestro: una cuenta (o una por moneda) «Nómina / conciliación cartola».
- Sin cuenta configurada: confirmar nómina **fail-closed** (mensaje, no asiento a ciegas).
- No hardcodear código de cuenta.

**DoD:** Admin › Plan de cuentas / tesorería guarda la puente; confirmar sin puente = error claro.

---

### T8-C — Cartola cruza nómina (P0)

**Pisa:** T2 «subir y contabilizar encima 1:1» para egresos de facturas.  
**Fuente:** MJ `[58:39]`–`[01:03:36]`.

Al importar cartola:

- Egresos que calzan **fecha + monto** con una nómina ya confirmada → estado **conciliado** (banco queda cruzado).
- No exigir modal T2 en esos movimientos.
- Si varios cargos = una nómina: ver T8-E.
- Lo que no calza queda **pendiente** (ingresos, cheques, excepciones).

**DoD:** nómina confirmada el día D por $X; línea cartola D / $X aparece conciliada sin digitación 1:1. Banco del mayor se mueve **en este cruce** (puente → banco) o se documenta el asiento de cierre de puente en la misma operación — **un solo lugar**, no los dos.

**Nota de diseño (cuando haya código):** el asiento banco vive en el **cruce**, no en la carga cruda. Origen sugerido `CARTOLA:{id}` + ref `NOMINA:{id}`. No crear `PAGO:{id}`.

---

### T8-D — Carga semanal: rango desde–hasta (P1)

**Pisa:** filtro interno «descartar mes anterior» si existe.  
**Fuente:** MJ saldo de apertura `[46:55]`–`[47:08]`; Sergio+MJ rango y carga semanal `[48:11]`–`[49:36]`.

- Periodo de import con **desde / hasta**.
- No excluir por mes calendario a ciegas (31→1, feriados).
- La primera línea «mes anterior» que MJ deja como **saldo de inicio**: tratarla como apertura / no duplicar movimiento operativo si ya está en cartola previa (regla a probar con un Excel real de Lupe).

**DoD:** se puede subir la semana 2 de junio sin rechazar el archivo por fechas de mayo/junio mezcladas en el Excel.

---

### T8-E — Conciliación: factura o nómina + multi-calce (P0)

**Pisa:** R4-19 «solo vista».  
**Fuente:** MJ `[51:43]`–`[53:16]`, `[01:02:27]`–`[01:02:51]`.

- Desde conciliación/cartola: asociar movimiento a **factura** o a **nómina**.
- Multi-select de egresos → una nómina; **el total debe calzar perfecto** (si no, bloquear).
- No implementar en v1 el «match perfecto» RUT+monto de Carlos `[53:18]`.

**DoD:** operador marca 4 transferencias = total nómina → conciliado; 3 de 4 (falta plata) → error, nada se marca.

---

### T8-F — Flujo de caja: total moneda + códigos financieros (P1)

**Pisa:** T3 si el flujo hoy parte el total por **banco**.  
**Fuente:** MJ `[01:06:20]`–`[01:12:51]`. **No pisa** «flujo solo lectura».

- Arriba: totales **CLP / USD / yuan de todos los bancos** (empresa).
- Tabla: agrupado por **código financiero** (venta cereza, packing, servicios básicos…).
- **No** listar las 50 facturas del concepto (eso es reportería / detalle de código financiero, otra pantalla).
- **No** poner el desglose banco en esta vista.

**DoD:** 2 bancos CLP → un solo total CLP arriba; abajo N filas de código, no N×bancos.

---

### T8-G — Cartolas: indicador saldo por banco (P1)

**Pisa:** nada de T2. Mueve el «cuánto hay en cada banco» **fuera** del flujo (MJ `[01:08:33]`, `[01:13:11]`–`[01:13:53]`).

- En **Cartolas** (otra pestaña o encabezado): saldo por **banco**, moneda dentro del banco.
- Se alimenta de cartolas cargadas / conciliadas (misma verdad que el banco, no del flujo).

**DoD:** Chile CLP + Chile USD + Estado CLP se leen sin entrar a Flujo de caja.

---

### T8-H — Prueba nómina de ingresos (P2, spike)

**Pisa:** nada hasta que la prueba cierre.  
**Fuente:** MJ `[01:01:50]`–`[01:05:32]` — *«hay que hacer una prueba»*.

Mismo patrón que egresos: registrar cobros **antes** del banco; la cartola cruza. Ingresos **no son pocos**; el 1:1 duele.

**DoD de la tarjeta:** no es implementar producción. Es: 1 flujo en papel o demo interna + visto bueno MJ/Lupe. Si dicen que sí, nace T8-H2 (código).

---

### T8-I — Excepciones 1:1 (P2, hereda T2)

**Pisa:** no. **Acota** T2.

Traspasos, sueldos, cargos sin nómina: modal T2 (contracuenta + destino + código financiero). Sin centro de costo en el lado banco `[36:40]`–`[37:08]`.

**DoD:** un sueldo se contabiliza 1:1; una factura que ya salió por nómina **no** pide el modal.

---

### T8-QA — Lupe revisa nómina semanal (T5 UX)

**Pisa:** ninguna.  
**Fuente:** Sergio `[01:16:21]`–`[01:16:43]`.

Pasar **solo** esta tarjeta a Lupe: mover factura de semana, ver totalizadores, export. No mezclar T8-A (asiento) hasta que Devint lo tenga.

---

## 3. Explicitamente fuera (no crear tarjeta 14/09)

| Tema | Por qué |
|---|---|
| Chipax / Fintoc / API banco | Mario: después de marcha blanca `[50:34]` |
| Match automático RUT+monto | Hipótesis Carlos; Mario aplaza |
| Lista negra | Cerrada no `[35:46]` |
| CC en asiento banco cartola | MJ no `[36:22]` |
| Cobranza R4-18, SMTP H9, maestro Productor, SII live | Ya diferidos; 14/09 no los reabre |
| Rehacer T1 / T4 / T6 | No se hablaron |

---

## 4. Otras tarjetas del mismo Meet (no tesorería)

Para no perderlas; **otra etiqueta** (`compras` / `alertas`). No van en el sprint tesorería.

| Id | Título | Quién | Minuto | Notas |
|---|---|---|---|---|
| C-14-1 | Destacar (no rechazar) factura cuya OC no está aprobada | Mario / MJ | `[24:10]`–`[26:31]` | Ya hay `ocNoAprobada` en código local; validar en QA, no reabrir como hueco si cumple |
| C-14-2 | Filtro documentos recibidos **sin** OC para armar compra | sala | `[25:37]`–`[25:39]` | Compras / Mario |
| A-14-1 | Alerta especial por RUT (temporal, rol + campana + correo) | Mario | `[26:37]`–`[33:14]` | Distinta del plazo 8 días; no auto-rechazo |
| A-14-2 | Investigar si GoSocket trae proveedor objetado SII F19 | Mario | `[33:16]`–`[34:52]` | Solo spike; no inventar integración |
| OPS-14 | Reuniones semanales por módulo (lun contabilidad / mar tesorería) | Sergio + sala | `[01:14:21]` | Operativo WhatsApp |

---

## 5. Checklist cuando sí se toque código (no ahora)

1. Actualizar `plan-tesoreria-ciclo-completo-2026-08-21.md` F0 (asiento puente + cruce).
2. Skill `almahue-tesoreria`: T2 «hecho» → «flujo feliz reemplazado por T8; T2 = excepciones».
3. Una línea en `AGENTS.md` huecos tesorería.
4. Tests: confirmar nómina asienta; cartola no asienta egreso nominado; calce multi perfecto/falla; flujo no parte por banco.
5. No `migrate` a ciegas en QA local (regla Prisma vacía).
6. No seed destructivo en prod.
