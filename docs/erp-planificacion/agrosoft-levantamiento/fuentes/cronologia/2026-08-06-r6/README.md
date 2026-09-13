# 2026-08-06 — R6 (demo ERP, cliente **MJ + Agustín**)

- **Video:** `C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-08-06 170730.mp4` (**1h06:12**)
- Meet: **ERP Almahue - Avances**. Carlos comparte `localhost:5174`
- Transcripción: `fuentes/transcripcion-reunion6.md` (reloj ≈ MP4)
- Minuta IA: `reunion6-minuta-2026-08-06.md` — **índice**; si choca, gana la transcripción
- Sala: Carlos, Sergio, **MJ**, **Agustín**. Sergio saluda a Mario al cierre (conectividad intermitente). «Se ve bien, Pablo» [03:35] es ASR; Pablo GoSocket **no** está en esta demo (credenciales = lunes)

El MP4 de la **mañana** (`110029`) es VND / Capacitación LAPRINCE — no usar.

Hitos en `hitos/`. El still `16m10-cadena` / `20m00` es el **modal de 1 jefe** (copy de R4): el audio de esos minutos es **organigrama**, no esa UI.

## 00:00–11:00 — login, Microsoft, admin

| t | Pantalla | Qué se ve / pide |
|---|---|---|
| 03:40 | Login `localhost:5174` | Autofill `pruebatest@devint.cl` / gmail Carlos. Sin botón Microsoft |
| audio | | Agustín: SSO Microsoft (mismo correo; bloquear Entra = corta apps). Sergio: se puede. Carlos: **no** estaba en el alcance; nota a futuro. MJ: se creó usuario con correo AlmaWeb y «pescó» |
| 06:40 | Admin › Usuarios | Empresas por usuario (SpA + Logística). Super-admin ve todas (Agustín). Permisos **por rol**; variación → otro rol. MJ: al crear usuario se eligen empresas; se puede despinchar acceso del rol |
| 09:40–11:00 | Empresas / roles | Periodo + empresa del header **no** se sincronizan entre PCs. Carlos: checkbox «aprobar PIN» en roles = **implementación antigua**, hay que sacarlo |

## 11:00–22:00 — aprobaciones (pedido fuerte de Agustín + MJ)

| t | Pantalla | Pedido (transcripción) |
|---|---|---|
| 11:40 | `/admin/aprobaciones` | 3 reglas demo: Comercial / OC / proformas. Rango 0–999.999.999. Copy: **un solo jefe** que elige el solicitante |
| 16:10–20:00 | modal **Nueva regla** (sigue «1 jefe») | **Agustín:** cadena por **monto + organigrama**. Sidri→Mario→él; si el monto cabe en Mario, corta ahí; si no, escala. Quien crea la OC **no elige** jefe (evita mandársela a la amiga). Vacaciones / suplencia. Una persona puede depender de **más de un** jefe (Lupe/Fran en varias áreas). Siempre deja rastro («Mario ya la miró») |
| audio | | **MJ [16:04]:** no solo monto: la analista de MJ **solo** ve a MJ, no a Mario (mismo tope, **otra línea**). Si falta el jefe → siguiente de la línea |
| audio | | Carlos: propuesta visual. Quedan a que Almahue **defina el flujo**; Devint arma propuesta mientras |

UI del día ≠ lo que piden. No citar este JPEG como «ya hay cadena».

## 22:00–36:00 — param, plan, ficha

| t | Pantalla | Pedido |
|---|---|---|
| audio | Proveedores vs clientes | Agustín: ¿misma base? **MJ:** listados **separados**; lookup RUT unificado (sociedad / proveedor / cliente / productor) |
| 25:00 | Plan de cuentas (396, toast «Cuenta **eliminada**») | MJ: flags por cuenta CC / elemento / área (como su Excel). Crear nivel 5 heredando código |
| audio | | **Agustín:** no borrar si hay movimiento → **inactivar**. ¿Rename pisa histórico? «Dejar solo deshabilitar». Gastos **próxima temporada** (cuenta puente / activar) — útil para presupuesto mayo; **no** lo piden implementar ya |
| 30:00 | mismo plan (raíces 1/2/5/6) | Prospectos: Agustín (vía MJ) = crear **directo como cliente** |
| 35:00 | Clientes (Packing + Frutas del Sur) | **Agustín:** **una ficha** bancos (N cuentas / monedas), contactos, despacho; no andar cazando el mail. Trazabilidad (estafas de cuenta). Sergio: pestañas. MJ aclara solicitud interna vs alta en el ERP |

## 36:00–58:00 — «cotizaciones» vs OV / stock / costo / flete

Pantalla todo el rato: `/comercial/cotizaciones` (tabs Cotizaciones / NP, copy «convertir a NP o factura»). Modal folio `110005`.

| t | Quién | Texto (no la minuta) |
|---|---|---|
| 38:14 | Agustín | Cotiz → **facturar la misma** |
| 38:58–40:21 | **MJ** | Cotizar es de **compras**. En ventas **no** cotizan; emiten en el facturador. Si esto es venta, el título es **orden de venta**. Link a stock (cajas AlmaWeb) sí tiene sentido |
| 40:56 | Carlos | «Este debería estar en el **panel de compras**» |
| 40:59 | **MJ** | «**Debe estar en el panel de compras**» |
| 41:02–41:52 | Agustín | Como dice MJ: **llamarla orden de venta**. La de compra queda OC. OV → se factura |
| 42:18+ | Agustín | OV tipo **servicio o producto**. Producto: catálogo + **bodega** + cantidad + precio + desc. Al emitir: **salida** e inventario |
| 45:02 | Sergio | ¿Quién mueve stock: nota o factura? Trazabilidad bodega/artículo/cantidad/usuario |
| 49:06 | MJ | Cantidad/producto de la OV; **precio editable** al facturar |
| 49:16 | **Agustín** | **No vender bajo costo** |
| 49:38 | Sergio | Precio compra en **mantenedor de productos**; la venta no deja ir bajo eso |
| 50:00 | MJ | «Si se puede, ideal» (minuta); aquí **[50:11] «No, ahí ya sería merma»** = la excepción es merma, no un combo Admin |
| 54:14–55:39 | MJ + Agustín | Stock **por bodega**; no vender más que hay. **Stock positivo** en venta. Tránsito = solo bodega |
| 56:50–57:12 | Sergio / MJ | Flete = **línea adicional**, no recargo SII de detalle. Sin impuestos adicionales |
| 57:34 | Carlos / MJ | API GoSocket: reunión **lunes** con Pablo. Carga masiva histórica con Acepta en curso |

Compras / conta / tesorería: **no** se recorrieron (tiempo).

## 58:00–fin

Publican al host **al día siguiente**; piloto con parametrizaciones. MJ quiere ciclo compra + venta reales. Diseño OC/cotiz **por cliente** + preview (datos fantasma; GoSocket no conectado). Recurrente jueves. Mini-review credenciales **lunes** (MJ se opera el martes; se conecta igual).

## Qué **no** cerrar con la minuta sola

- **D4/D11 de la minuta** mezclan frases. En audio hay **dos** cosas: (1) MJ: cotiz de **compra** / «en panel de compras»; (2) Agustín+MJ: el documento de **venta** = **OV** (producto/servicio, stock). El corte posterior (20/08 Lupe + 03/09) **suprimió** el CRUD de cotiz de compras — no reescribir esta reunión como si MJ hubiera pedido borrarlas.
- Copy «1 jefe a elección» en la UI **contradice** a Agustín/MJ en la misma hora.
- Toast **eliminar** cuenta vs pedido **inactivar**.
- Cadena **Comercial** en las 3 reglas = lo que Carlos tenía; no es «MJ pidió aprobar OV».
- SSO Microsoft = **pedido Agustín**, no implementado ese día.
