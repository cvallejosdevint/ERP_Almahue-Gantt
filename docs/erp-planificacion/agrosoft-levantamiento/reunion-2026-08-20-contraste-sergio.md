# Reunión interna 20/08/2026 — contraste Sergio (PM)

**Grabación:** `Screen Recording 2026-08-20 105836.mp4` (~30:47)  
**Quién:** Carlos (desarrollo) y Sergio (Devint). **No hay Agustín ni MJ.**  
**ASR:** Whisper local `small` (ES). Audio y frames en `fuentes/2026-08-20-reunion-sergio/` (gitignored / pesado).  
**Transcripción bruta:** [`fuentes/transcripcion-2026-08-20-reunion-sergio.md`](fuentes/transcripcion-2026-08-20-reunion-sergio.md)  
**Regla:** Sergio/Carlos = hipótesis. Verdad = Reu6 > Reu5 > Reu4 (MJ/Agustín) + código.

---

## Resumen ejecutivo (PM)

La reunión **alineó ventas** (OV → aprobación → confirmar → facturar) y **abrió dudas fuertes en compras** (¿cotización → OC o cotización → factura recibida del proveedor?). También propusieron **reserva de stock** (hoy el sistema descuenta al confirmar) y un modo demo de emisión sin CAF.

Nada de esto reemplaza minuta. Varias ideas de Sergio **chocan con D11** ya cerrado en código.

---

## Bloque 1 — Ventas (OV vs factura) — ~00:00–16:00

### Qué se dijo (limpio)

1. Flujo: OV → solicitud de aprobación (hasta 3 niveles) → notificar al solicitante → **él** confirma / sigue → **facturar**. El aprobador (ej. gerente) **solo aprueba**; no hace la pega de emitir.
2. OV = parte **no tributaria** (control + aprobaciones). Emitir = DTE.
3. Sergio pregunta: ¿servicios pueden ir directo a Emitir sin OV? Al inicio lo veía lógico (OV = stock). Luego: **servicios también deberían pasar por OV** por control y aprobación.
4. Emitir sin OV “puede darse”, pero si hay rangos de aprobación (ej. $500.000), ir directo a factura **salta el control** → conviene que sea **configurable / restrictivo**.
5. Demo en vivo: nueva OV → enviar a aprobación → superadmin aprueba con PIN → confirmar (descuento stock) → Facturar → error CAF (sin folio) → queda **borrador**.
6. Carlos: bug UX con superadmin (pendientes vs “mías”, botón emitir); unificar listados; notificación post-aprobación + botón para continuar.
7. Reversa / anulación de factura: si movió inventario, hay que devolver stock. Sergio recuerda a MJ: fruta no se “devuelve” como stock → **merma** (a validar).
8. Stock: hoy al aprobar/confirmar **descuenta**. Proponen **reserva** al aprobar OV, stock disponible = total − reservas, vigencia (ej. 10 días), liberación manual por súper usuario. Módulo de stock total faltante / permisos.

### Qué aplica (alineado con cliente / código)

| Tema | Minuta / código | PM |
|---|---|---|
| OV no es DTE; factura sí | D11 | **Aplica** |
| Aprobar ≠ facturar; solicitante sigue el flujo | D4 + D13 | **Aplica** (corrige el “PIN emite factura” de ayer) |
| Servicios también pueden ir por OV (aprobación) | D12 permite servicio en OV | **Aplica** como política de control |
| Emitir sin OV posible pero no debe saltarse control | D13: emisión directa no descuenta stock | **Aplica el riesgo**; la regla exacta (bloquear siempre vs configurable) **preguntar MJ** |
| CAF falla → borrador, no contabiliza | H11 fail-closed | **Aplica** |
| Factura desde OV autorizada | Código piloto | **Aplica** |

### Qué no implementar sin MJ / choca

| Tema | Por qué |
|---|---|
| **Reserva de stock** con TTL y liberación manual | Hipótesis Devint útil; **no está en Reu6**. Hoy: descuento al **confirmar** OV. Diseñar + preguntar MJ antes de sprint grande. |
| Producto “merma” / devoluciones de fruta | Skill: no inventar mermas. Si MJ dijo algo en Reu4, **preguntar** con cita; no construir módulo merma. |
| Que el **aprobador** emita el DTE | Sergio y Carlos coinciden en que **no**; el solicitante continúa. Mantener. |
| Unificar “todo Emitir” otra vez | No: ya diferenciaron OV vs Emitir en esta misma reunión. |

---

## Bloque 2 — Compras — ~16:18–28:00

### Qué se dijo (limpio)

1. Libro/registro de compras: ideal = **documentos recibidos** (GoSocket) + carga manual poco usada.
2. Aprobaciones: más críticas en **compras** que en ventas (control de gasto); ventas solo montos grandes.
3. Confusión de nombres: cotización vs nota de venta / OC (Sergio lo admite).
4. Flujo que Sergio imagina: cotización interna → aprobación → (¿enviar al proveedor?) → proveedor emite **factura** referenciando la cotización → Almahue recibe/valida. Si factura sin referencia o cotiz no aprobada → ¿auto-rechazo o marca manual?
5. Carlos muestra: cotización → **convertir a OC** (y nota que “emitir cotización” no dispara bien la cadena; a ajustar o esperar confirmación).
6. Sergio: **convertir a OC está mal**; tras aprobar cotiz se espera la factura del proveedor (GoSocket). La OC sería el doc “autorizo comprar”; la cotización en compras le parece “rara” (en otros ERPs cotiz = lado ventas).
7. Acción acordada: **dibujito de flujo** (Excalidraw / Lucid) con preguntas marcadas para la reunión con el cliente; no pelear en abstracto.

### Contraste con D11 (cerrado)

| Dicho Sergio / Carlos | Cliente (Reu6 D11) | Decisión PM |
|---|---|---|
| Cotización Compras → aprobar → esperar factura proveedor (sin OC) | Cotización Compras → **OC** (borrador) → recepción / libro recibido | **No cambiar código a ciegas.** Llevar dibujo a MJ/Agustín. |
| Cotización “rara” en compras; debería ser de ventas | Reu6: ventas **no** cotizan; previo a factura = **OV** | **No restaurar cotiz de cliente en Ventas.** |
| Referencia factura↔cotización + auto-rechazo | Reu4: libro compras + asociar a OC / carga | Preguntar MJ: referencia a **OC** vs cotiz; rechazo auto vs bandeja. |
| Subir PDF de factura vs solo folio | Reu4 carga Acepta/PDF | Ya hay dirección libro; detalle UX con MJ. |

**Veredicto compras:** la reunión **reabre** el debate cotiz→OC. En código local D11 está cerrado. Como PM: **congelar implementación** de “quitar convertir a OC” hasta el dibujo + OK de MJ. Sí preparar el diagrama y las preguntas.

---

## Bloque 3 — DTE / CAF / demo — ~28:14–fin

| Tema | Lectura PM |
|---|---|
| Sin CAF / GoSocket aún | H11; no vender “ya emite SII” |
| Intermediario `billing-gateway` → JSON→XML→GoSocket | Ya en arquitectura; OK mostrar |
| Variable que “falsea” emisión: folio fake + leyenda amarilla “no es DTE real” | Útil para **demo de proceso**; no confundir con SII live. Stub inline / flags ya existen en skills. |
| Mostrar error CAF como evidencia de que el pipe funciona | OK mensaje: “falta folio de Almahue” |

---

## Decisiones / acciones (solo internas Devint)

| # | Acción | Dueño | ¿Backlog producto? |
|---|---|---|---|
| 1 | Dibujar flujo compras (cotiz → ¿OC? → factura recibida) + preguntas | Carlos | **Sí para reunión cliente**; no código hasta OK |
| 2 | Ajustar UX aprobaciones OV (notificación, botón continuar, bug superadmin) | Carlos | Sí, UX piloto |
| 3 | Unificar listados OV / pendientes | Carlos | Nice-to-have |
| 4 | Diseño reserva stock (disponible vs total, TTL, liberar) | Carlos+Sergio | **Propuesta**; validar MJ |
| 5 | Vista stock total (permisos) | Carlos | Bug/regresión UI |
| 6 | Política: ¿Emitir sin OV bloqueado si hay escalas? | Preguntar MJ | Configurable vs siempre OV |
| 7 | Devoluciones / “merma” | Preguntar MJ | No implementar merma |
| 8 | Demo con stub/leyenda sin CAF | Carlos | Operativo demo |
| 9 | No migrar mal cotiz→OC “al otro lado” sin confirmar | Sergio | Esperar cliente |

---

## Preguntas concretas para MJ / Agustín (próxima reunión)

1. ¿Toda venta (incluido solo servicios) debe pasar por **OV + aprobación**, o Emitir directo queda permitido bajo umbral / flag?
2. Stock: ¿al aprobar OV se **reserva**, se **descuenta al confirmar**, o solo al facturar?
3. Compras: ¿el documento previo a la factura del proveedor es **cotización → OC** (como Reu6) o cotización aprobada → factura recibida **sin** OC?
4. Si llega una factura de compra sin referencia / con cotiz no aprobada: ¿rechazo automático, bandeja, o solo aviso?
5. ¿Hay devolución física de fruta a bodega o solo NC tributaria / merma? (sin inventar módulo)
6. ¿Cuándo cargan CAF / portal GoSocket para dejar de usar stub?

---

## Qué NO vender en la demo de hoy / jueves

- Que compras “ya no usa OC”.
- Que hay reserva de stock con vigencia.
- Que la emisión sin CAF es factura SII real (sí: proceso + error o stub con leyenda).
- Que Sergio “definió” el flujo: **no**; el cliente cierra con el dibujo.

---

## Relación con el modelo OV vs factura (tu razonamiento)

| Tu modelo | Esta reunión |
|---|---|
| OV orientada a stock + aprobación → factura | **Confirmado** por ambos; además: OV también para **servicios** (control), no solo stock |
| Factura puede no venir de OV | Sergio: posible pero **peligroso** si salta aprobación → configurable |
| Producto vs servicio | Servicio sin bodega **sí**; sin OV **no necesariamente** |

Sergio **corrigió** su lectura de ayer (Emitir = todo): hoy empuja OV como control de aprobaciones también para servicios.
