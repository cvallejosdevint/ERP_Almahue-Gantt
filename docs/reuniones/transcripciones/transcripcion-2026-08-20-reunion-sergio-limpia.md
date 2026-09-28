# Transcripción limpia (español chileno) — reunión 20/08/2026 Sergio + Carlos

**Fuente:** Whisper `small` sobre `Screen Recording 2026-08-20 105836.mp4` (~30:47).  
**Nota:** el ASR mete ruido (“bohua”, “Sador”, “Google Sock”). Esta versión corrige a chileno claro **sin inventar** requisitos. Verdad de producto = MJ/Agustín + minutas.  
**Bruta:** `transcripcion-2026-08-20-reunion-sergio.md` · **Contraste PM:** `reunion-2026-08-20-contraste-sergio.md`

---

## Resumen

Hablaron el flujo de **ventas** (OV → aprobación → el solicitante continúa → factura) y abrieron dudas fuertes de **compras** (cotización vs orden de compra vs factura recibida). Quedaron en armar un **dibujito** para Almahue. Sin CAF todavía: mostrar error o stub con leyenda.

---

## Decisiones / acuerdos internos (Devint — no son minuta)

1. Quien **aprueba** no emite la factura: o sigue la cadena, o avisa al **solicitante** para que él confirme y facture.
2. La OV no es solo stock: también es **control y aprobaciones**. Los **servicios** también deberían pasar por OV.
3. Emitir factura **sin OV** permite saltarse la cadena → debe ser restrictivo / configurable (luego producto: Emitir exige OV).
4. Al fallar CAF, la factura queda en **borrador**.
5. Stock: hoy descuenta al confirmar; propusieron **reserva** al aprobar, con plazo y stock disponible = total − reservado.
6. Compras: **no cerrar** sin Almahue; preparar diagrama y preguntas (cotiz → ¿OC? → factura recibida).

---

## Dudas abiertas (para MJ / Agustín)

- ¿Toda venta (también solo servicio) obliga OV?
- ¿Reserva al aprobar, descuento al confirmar, o al facturar?
- Compras: cotización → OC (Reu6) vs cotización → factura del proveedor sin OC.
- Factura de compra sin referencia: ¿auto-rechazo o bandeja?
- Devoluciones de fruta / “merma”: solo preguntar; no inventar módulo.
- ¿Cuándo hay CAF?

---

## Citas clave (aproximadas)

### ~00:00–02:10 — Aprobador no factura; servicios por OV

> Hago la orden de venta, mando la solicitud de aprobaciones, pasa por los niveles, y después **yo** la tengo que facturar. Al aprobador le debería llegar… no: a **ti** te llega que se aprobó y **tú** confirmas.

> El gerente solo aprueba; no te va a hacer la pega de las facturas.

> Cuando son solo servicios no baja stock. ¿Puedo emitir sin OV? … La OV también es para control y aprobaciones. Entonces los servicios **igual deberían pasar por OV**.

### ~02:10–03:40 — Emitir directo salta el control

> Si tengo tope de quinientas lucas y voy directo a facturar el servicio, me salto la aprobación. Restrictivo no va… me gustaría que fuera **configurable**: bloquear factura si hay niveles de aprobación.

### ~04:00–08:20 — Demo OV → aprobar → confirmar → facturar → error CAF

Crean OV, envían a aprobación, superadmin aprueba con PIN, confirman (descuenta), Facturar, falla por rango de números (CAF), queda borrador. Mencionan intermediario **billing-gateway**.

### ~08:30–11:00 — Reversa / stock

Si el DTE se rechaza y ya movió inventario, hay que reversar. Sergio recuerda algo de MJ sobre fruta y devoluciones; **hay que validar**, no asumir módulo merma.

### ~12:00–16:00 — Reserva de stock

> Si apruebo dos OV del mismo stock 10, la primera se asegura el stock. Hoy descuenta; debería ser **reserva**, stock disponible = total menos reservas, con vigencia, y poder liberar (súper usuario).

Falta vista clara de stock total / por bodega (permisos / módulo).

### ~16:20–28:00 — Compras (hipótesis; choca con D11)

Sergio: ideal recibir facturas del proveedor (GoSocket), comparar con lo pedido. Cotización → aprobación → proveedor emite factura referenciando la cotización. Cuestiona **convertir a OC**. Carlos muestra cotiz → OC en pantalla. Acuerdan **dibujito** y preguntar a Almahue; no pelear el modelo sin ellos.

### ~28:00–fin — CAF / demo

Sin CAF: se puede falsear emisión local con folio fake y leyenda amarilla “esto no es DTE real”, o mostrar el error de CAF como evidencia del pipe.

---

## Qué no se pierde respecto al Whisper ruidoso

| ASR / ruido | Lectura correcta |
|---|---|
| “bohua”, “bohachay” | muletillas / “poh” / “cachai” |
| “Google Sock” | GoSocket |
| “servicio puesto interno” | SII / servicio de impuestos (contexto DTE) |
| “Sador” | probablemente “así ahora” / “armado” |
| Cotización “rara” en compras | Sergio duda del doc; Reu6 la deja en Compras → OC hasta que Almahue diga otra cosa |
