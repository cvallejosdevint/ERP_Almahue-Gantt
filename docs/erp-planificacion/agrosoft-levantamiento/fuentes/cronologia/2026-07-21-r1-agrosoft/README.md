# 2026-07-21 — R1 Demo Agrosoft (primera grabación, no primer contacto)

- Video: `fuentes/videos/reunion1-2026-07-21.mp4` (~4,1 GB, **1h56m**)
- Transcripción: `fuentes/transcripcion.md` (reloj ×10)
- Meet: `meet.google.com` título **Demo Almahue ERP**
- Presenta: **Maria Rodriguez (MJ)**. En sala al inicio: Carlos; invitados MJ + Sergio.
- Reloj de Windows en los frames: **21-07-2026 10:04**. El nombre histórico `Screen Recording 2026-07-21 120114` encaja con el **fin** (~10:04 + 1h56 ≈ 12:00).

## Visión 00:00–03:00 (36 frames cada 5 s)

| t aprox | Qué se ve | Encaje con el audio |
|---|---|---|
| 0:00–0:50 | Meet + aviso «pantalla en pantalla». Pestaña **Agrosoft**. MJ «Presentando y anotando». | Charla de clima / setup. Aún no hay UI de negocio. |
| ~1:00 | Espejo Meet-sobre-Meet (compartió la ventana de la llamada). Frames poco útiles. | — |
| ~1:00–1:30 | Home Agrosoft `…/principal/principal.aspx` — **Sistema de Gestión AGROSOFT r.3.0.2**, empresa **ALM SERVICES SPA**, bienvenida **JUAN AGUSTIN VILLELA**, temporada 2023/2024, mes contable **7/2026**, indicadores dólar/UF. Menú: Mano de obra, Contratistas, Compras, Insumos, Maquinarias, Contabilidad, Gestión, Parámetros. | MJ: «ingresamos a un link… página de inicio… usuario y clave… última empresa» |
| ~1:30–3:00 | `UsrCambiaEmpresa.aspx` — 8 razones sociales (agrícolas + ALM + Almahue Export + servicios). Cambia de ALM (empresa 1) a **ALMAHUE EXPORT SPA** / planta **CHAMONATE**. Temporada código 4 = 2023/2024 (MJ: el cambio de temporada «no sirve mucho» porque no usan Gestión). | «podemos hacer cambio de empresa… 15 usuarios… si dos personas usan el mismo usuario…» |

## Visión 03:00–08:00 (60 frames cada 5 s)

Sigue en **ALM SERVICES SPA**, usuario `javillela` (Agustín). MJ no usa Mano de obra (trabajan con Book).

| t aprox | Pantalla | Audio (reloj transcripción ÷10) |
|---|---|---|
| 3:00–4:00 | Home otra vez + menú. Despliega **Contratistas** | «no usamos mano de obra… Book… no te lo voy a mostrar» |
| ~5:00 | **TARIFAS MANO DE OBRA CONTRATISTAS** — filtros año/mes/código; grilla vacía («No hay datos»). Submenú: Ingreso/Informe tarifas, Parámetros contabilización, Ficha, Contratos, Enrolamiento, Asistencia, Control producción, Proforma, Traspaso, Cierre mes | Limitante: al agregar 2 tarifas la primera desaparece |
| ~7:00 | Listado **Ficha contratista** — 19 registros, pág. 2; códigos 11–19; vigente S; editar / vigencia | «historial… agregar o cambiar vigencia» |
| ~8:00 | Tarifario contratista **1 JOSE HERNAN PLAZA GALLARDO** + modal **Labor** (111 labores, pág. 8/12: pintar troncos, podas, polinización…) | «labores anexadas a actividad… pintar troncos… packing cereza» |

Reloj de trabajo: **Whisper** (`fuentes/whisper-local/reu1/`) = tiempo real. Hitos en `hitos/`. Si el still no era la pantalla que MJ nombra, se subdivió a 5 s (`sub-proforma/`).

## Visión 08:00–29:00 — contratistas (cierre)

| t Whisper | Pantalla | Qué dice / qué importa |
|---|---|---|
| 08:12 | Mano de obra › **Actividad/Labor** (grilla vacía) | «te voy a mostrar acá»: labor se anexa a actividad (packing cereza / pintar troncos). Quiere esa param **en contratista**, no en Book |
| 11:30 | Parámetros generales › CC — **Cargando…** | CC se crean acá; limitante: en ALM puede elegir CC de **otra empresa** |
| 16:20 | Sigue tarifario (still flojo) | Perfil admin vs digitador; un cambio de perfil «activó pestañas» a digitadores |
| 17:20 | **Contabilización contratista** | Tipo 1 Mano de obra / tipo 2 Transporte: Debe `610101002` MO contratista, Haber `210802003` **FACT X RECIBIR CONTRATISTAS**. Admin distinta (maquinaria vs MO) |
| 19:40–21:10 | Mismos params (hito inicial no sirvió) | Audio: factura cierra vs proforma; «mañana traigo proforma agrícola» |
| **~21:35** (`sub-proforma` pf_024) | **Emisión factura proforma**: Fundo, contratista desde/hasta, por folio o fecha, **Borrador / Definitiva**, icono PDF | Borrador editable; Definitiva no. Un contrato ↔ una factura; no cierra hasta asociar todas |
| ~22:55 | **Reemisión** proforma (vacío) | |
| 24:00 | **Genera contabilización** mes 7/2026 + **tasa de cambio** | Peso y dólar; pide yuan y euro. Traspaso cierra contratista; queda abierto en conta como facturas por recibir |
| ~29:00 | **Cierre mensual** contratistas (hasta 06/2026, usuario `mjrodriguez`) | Digitador no tiene cierre ni traspaso |

## Visión 29:00–65:00 — compras + registro factura

| t | Pantalla | Qué importa |
|---|---|---|
| 29:45 | Menú **Compras** (solicitud, OC, informe, cerrar/reactivar, **aprobación**, **recepción servicios**) sobre cierre mensual | Empieza compras; «te voy a mostrar compras e insumos en paralelo» |
| 36:00 | Form **Orden de compra** vacío: sin solicitud, depto, fechas, jefe, proveedor, tipo/forma pago, moneda, **TC 933**, grilla artículo/CC/impuesto | No usan solicitud. TC de cabecera **no** es el de recepción |
| 40:00 | Modal **Distribución CC** + lookup 143 CC (fundo + especie). Artículo `51010001` reparación activos, neto 1000, cta `610104009` | Directo / x ha / grupos. En ALM puede pickear CC de Almahue/Santa Pilar. x ha = todo o nada |
| **43:20** | Alert **«Se genero Orden de Compra Nro.: 5207»**. Sandoval y Fuentes, 30 días, obs «PRUEBA SISTEMA», **exento**, 1 × 1.000 | Folio numérico (no `OC-AAAA-NNNN`). «lo anotamos para eliminarla» |
| 46:08 audio | — | **AS-IS: se emite la factura y después crean la OC**; en observación ponen «factura tanto». Conta crea las OC hoy; quieren que cada depto las cree |
| 48:35 | **Aprobación OC**: Aprobar/Rechazar; lista 5207…3876; PDF OC 5207 **PENDIENTE**; solicita MJ, comprador/aprobador Agustín | Sin correo de aviso; pide badge de pendientes |
| 50:20 | Misma bandeja: línea con cta `610104009`, CC `10100` Adm. y finanzas ALM, elemento `1001`, monto 1.000 | |
| 51:25–53:40 | **Recepción / contabilización OC** 5207 **APROBADA**, botón Recepcionar + fecha | TC = fecha de recepción (no el de la OC). Productores: TC promedio |
| **53:55** | SSRS **Comprobante 8310** 21/07/2026: Debe `610104009` 1.000 / Haber `210802004` FACT X RECIBIR SERVICIOS, ref OC **5207**, TC 933, USD 1,07 | Gasto reconocido **antes** de la factura |
| 54:50–57:00 | Conta › Proveedores › **Registro de compras**. Tipo compra 3 Servicios, OC 5207, doc **33**, afecto, RUT Sandoval, línea cta `210802004` + ref OC | Puede cruzar proveedor si el monto coincide. TC editable **solo en auxiliar**, no en costo (parche productores) |
| ~60:50 | Mismo registro | OC exenta + factura afecta **sí deja** grabar. Combustible: específico. Facturas mixtas: suman neto+exento en la OC |

Gate: registro de compra **solo si OC aprobada y recepcionada**.

## Visión 65:00–fin — insumos, maquinaria, conta, params

| t | Pantalla | Qué importa |
|---|---|---|
| 66:00 | Hito se quedó en recepción (still flojo) | Audio: maestro artículos **en insumos**; compras = servicios; insumos = material/agroquímico. No usan ingrediente activo (sí para agrícola) |
| 77:20 | **Movimientos de bodega**: tipo, bodega, O/C, proveedor, TC, grilla vacía | Entrada proveedor / entre bodegas / devolución. Bodega Chamonate. **NC por cantidad** sale a **precio promedio**, no al de la factura |
| 85:20 | (menú maquinaria) | **No lo usan** en ningún rubro; agrícola (tractores, prorrateo cuartel) |
| 87:20 | Hito cayó en reporte guías existencia | Audio: plan de cuentas; flags CC / área / especie / elemento; **no imputable** |
| **90:15** | **Tipos de referencia** (57, pág. 1): honorarios 1000–1005, **101** fact. exp., **104/106** ND/NC exp., **110 FACTURA EXPORTACION ELECT** | Libro compras elige tipo acá. MJ creó el 31 |
| 93:40 | Elementos de costo (Excel «sagrado») | Quieren **amarrar** artículo+CC+elemento por área (hoy el jefe industrial cambia el elemento a cada rato). No pueden inactivar, solo borrar |
| 96:30 | **Códigos financieros** (68): 1002 venta exp. cerezas, 1003 nac. cerezas, agroquímicos, nectarín… | Flujo de caja / tesorería |
| 100:20 | **Carga de traspasos desde Excel** (validación + errores por línea) | Centralización remuneraciones. Cambia a junio para que el periodo calce. Celda número→texto rompe el archivo |
| 107:00 | Gestión | **No usan**; nació el área de Mario (Power BI). Vuelve en agosto |
| 112:00 | **Indicadores financieros** (BC): dólar 933, euro, UF, UTM; fila 21/07 | Auto BC (antes manual). Faltan **domingo/feriado**. Quieren dólar/euro/**yuan**; UF/UTM/IPC poco usados |

Cierre ~1h56: «mañana perfiles»; «Agrosoft 3.0».

## Hallazgos visuales que la transcripción sola no fija

- Folio OC de prueba: **5207**. Asiento recepción: **8310**.
- Cuentas vistas: gasto `610104009`, facturas por recibir servicios `210802004`, contratistas `210802003` / MO `610101002`.
- Tipo SII **110** ya existe en Agrosoft (exportación electrónica).
- Proforma: pantalla **Borrador vs Definitiva** + fundo + rango contratista (el still a 19:50 no la mostró; hizo falta subdividir).
