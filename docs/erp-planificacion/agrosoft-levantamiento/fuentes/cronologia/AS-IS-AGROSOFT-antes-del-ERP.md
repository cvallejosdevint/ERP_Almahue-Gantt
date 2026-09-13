# AS-IS — cómo opera Almahue **antes** del ERP (Agrosoft + satélites)

**Fecha de este corte:** 2026-09-05.  
**Qué es:** el sistema que el cliente usa **hoy**, reconstruido con videos + transcripciones.  
**Qué no es:** el prototipo Nest/React (R3+), ni el TO-BE, ni hipótesis de Carlos/Sergio.

**Fuentes (prioridad):** transcripción + frames de **R1 21/07** y **R2 23/07** (Agrosoft 3.0.2 en vivo). Complemento: R4 ~69:30 (pago Agrosoft), Lupe/Mario **20/08**, tesorería **28/08** (cómo trabajan cartola), Excel MJ, R6 (ficha / organigrama = pedido, no AS-IS).

---

## 0. ¿Falta video o transcripción?

Inventario local cerrado: `Videos\Screen Recordings`, `E:\grabaciones`, `fuentes/videos/`, Desktop 03/09.

| Hueco | Por qué importa | Dónde buscar |
|---|---|---|
| **28/08 tesorería** MJ+Lupe+Fran+Mario | Hay transcripción tl;dv; **no** hay MP4 en disco (el `172119` del 27 es interna UI) | tl;dv [6a91a445…](https://tldv.io/app/meetings/6a91a445564eaa0013e057cd) · máquina de otro |
| Kickoff API **01/09** (Pablo) | Minuta sí; local = Postman/Trello, no el Meet | tl;dv [6a96f651…](https://tldv.io/app/meetings/6a96f651fb2cc300133c3cd5) |
| Verbatim **04/08, 13/08, 25/08** GoSocket | Video sí; transcripción no (solo bot) | Export tl;dv de esas llamadas |
| **08/07 y 13/07** | Video en `E:\grabaciones`; sin transcripción | Whisper local. 08/07 = Freshlink (no Agrosoft). 13/07 = kickoff Gantt/Trello |
| **09/07** | Hay SRT sucio | Re-Whisper si se cita AlmaWeb |
| Walkthrough **Acepta**, **Book**, **Gestión/Power BI**, portal banco PDF | Nunca se grabó la UI | Pedir a MJ 15 min o pantallazos |
| R1/R2 original en `Videos\` | Ya no está; **copia** en `fuentes/videos/` | No rebuscar salvo backup |
| R6 | Solo `Screen Recordings\170730`, no en `fuentes/videos/` | Copiar si se quiere el set junto |

Con R1+R2+clip R4+20/08+28/08+Excel MJ **alcanza** para el AS-IS operativo. Lo que falta no cambia el mapa; afina DTE (Acepta) y Book.

---

## 1. Mapa de sistemas (as-is)

```
                    ┌─ Book ──────────── mano de obra propia (no mostrado)
Operación ─────────┤
                    └─ Agrosoft 3.0.2 ── conta, contratistas, compras, insumos, ventas, tesorería parche
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
   Acepta (DTE SII)     Excel banco / cartola   AlmaWeb / Freshlink
   contrato a sep/2026  (verdad del banco,      embarques, cajas, COMEX
                         a veces Power BI yuan)  (otro producto)
                              │
                              ▼
                        Mario / Gestión = Power BI (módulo Gestión Agrosoft no se usa)
```

Intentaron **AgroSmart** (`app.agrosmart.cl`) para contratistas: UX de labores→factura útil; **conta descuadraba**. Se quedaron en Agrosoft.

---

## 2. Tenancy, usuarios, reloj

- URL tipo `…/principal/principal.aspx`. Login usuario+clave. Queda en **la última empresa**.
- Cambio de empresa: 8 razones (agrícolas + **ALM Services** + **Almahue Export** + servicios). Temporada (ej. 2023/2024) «no sirve mucho»: no usan Gestión.
- Mes contable independiente (julio 2026 en R1).
- ~15 usuarios. **Mismo usuario en dos PCs** = se pisan. Perfil mal cambiado **abrió pestañas a digitadores**.
- Digitadora `MGAJARDO`: solo **Contratistas + Insumos**. Analista: procesos + informes; **sin** param ni cierre. Cierre de mes = MJ.
- CC en ALM puede elegir CC de **otra empresa** (Almahue, Santa Pilar). Cada empresa tiene CC «con apellido» (Adm. ALM / AlmaWeb / Santa Pilar).
- Indicadores BC (dólar, euro, UF, UTM). Faltan **domingo/feriado**. Quieren **yuan**. Código banco yuan ya existe: `110102006`.

---

## 3. Contratistas (Agrosoft)

**Diseño:** tarifario → contrato → enrolamiento → control producción → proforma (borrador/definitiva) → registro compra tipo **6** → traspaso (facturas por recibir) → cierre mes.

**Cómo duele:**

| Hecho | Evidencia |
|---|---|
| Agregar una 2ª tarifa **borra** las anteriores | R1 + R2 Gómez (hay que salir y volver) |
| Labor ↔ actividad **al revés** (hay que saberse la actividad) | R2 Rodrigo |
| Precio tarifario **bloqueado**; a veces se negocia **después** | R2 |
| Proforma **borrador** editable; **definitiva sin confirmación** | R2 |
| 1 contrato → 1 factura; no cierra hasta asociar todas | R1 MJ |
| **1 proforma / mes**; dos meses en una factura **no se asocian** → meten todo en el mes de la factura («gestión mensual mentira») | R2 |
| Imputación fija tipo MO: Debe `610101002` / Haber `210802003` FACT X RECIBIR CONTRATISTAS | R1 |
| Traspaso pide TC (peso/dólar; piden yuan/euro). Digitador **sin** cierre/traspaso | R1 |
| Folio visto: contrato **179** → PDF borrador folio factura **0** → definitiva **155** → compra 37.500 | R2 Santa Pilar |

AgroSmart que **sí** quieren copiar: registro múltiple de labores + tildar labores contra un documento (ellos hoy arman la proforma **antes**).

---

## 4. Compras (servicios) — el flujo real ≠ el menú

Menú tiene solicitud, OC, aprobación, recepción, registro. **No usan solicitud.**

**AS-IS operativo (MJ R1 + Lupe 20/08):**

1. Llega la **factura** (o el área ya «hizo» la cotización afuera).
2. Conta **crea la OC después** y en observación pone «factura tanto». Folio **numérico** (5207), no `OC-AAAA-NNNN`.
3. Lupe: «nosotros solamente nos piden la **orden de compra** y nosotros solo generamos la orden de compra». Cotiz = adjunto/SAT o ni se anexa (Mario).
4. Aprobación: bandeja Aprobar/Rechazar; **sin correo**. Solicitante ≠ aprobador (MJ vs Agustín en 5207).
5. Recepción = **reconocer gasto** (puede ser **otro mes**). TC = fecha de recepción, no el de la OC. Productores: TC promedio.
6. Asiento ejemplo OC 5207: compr. **8310** Debe `610104009` / Haber `210802004` FACT X RECIBIR SERVICIOS.
7. Registro compra (tipo 3 servicios, doc 33…): **solo si OC aprobada y recepcionada**. Puede **cruzar proveedor** si el monto coincide. OC exenta + factura afecta **deja grabar**.

Compras = **servicios**. Material/agroquímico = **Insumos**.

---

## 5. Insumos / bodega

- Maestro artículos **en insumos** (no en compras).
- Movimientos: entrada proveedor, entre bodegas, devolución. Bodega ej. Chamonate.
- **NC por cantidad** sale a **precio promedio**, no al de la factura.
- **Niveles de bodega no se usan** (R2).
- Maquinaria: menú existe; **no lo usan** (prorrateo agrícola).
- AlmaWeb: cajas = **bodega de paso**, sin stock mes a mes (IVA exportador: archivo compra/cantidad). Stock físico en **ALM**. ALM factura a AlmaWeb el packing; AlmaWeb exporta.

---

## 6. Ventas y DTE (as-is)

- **Registro de ventas** en Agrosoft: más campos que compras (fax, despacho… **no se usan**).
- **Guardar** = temporal, **no** sale en informes. Vale **Grabar y contabilizar**.
- Códigos de venta (exportación `510101004`, nacional `510101001`, fruta comercial, guías, rebate…).
- Reversa: **no** edita línea (a diferencia de proveedores). Cadena asiento orig / reversa / nuevo. Motivo real: **CC o cuenta mal**, no anular el DTE. Folio SII **único**; anular ante SII = **NC**.
- Tipos de referencia ya incluyen **110 FACTURA EXPORTACION ELECT**, 101/104/106 exp.
- Facturador vivo: **Acepta** (se renueva **septiembre**). Quieren cambiar en agosto. GoSocket = reemplazo, no AS-IS.
- COMEX (puerto, país) vive hoy en **GoSocket/Acepta / AlmaWeb**, no en el libro Agrosoft.

---

## 7. Contabilidad

- Plan de cuentas con flags por cuenta: CC, elemento, área, especie; **no imputable**.
- Elementos: Excel «sagrado». Jefe industrial **cambia el elemento**. No se puede **inactivar**, solo borrar.
- Códigos financieros (~68): alimentan **flujo de caja** (venta exp. cereza, agroquímico…).
- Centralización remuneraciones: **Excel** con validación por línea (número como texto rompe).
- Honorarios: % retención con vigencia por periodo.
- Libros: trabajan el **mayor**; poco el diario. Contabilidad electrónica = **anual** (renta), no mensual.
- Gastos **próxima temporada**: cuenta puente; MJ «activa» y después pasa a gasto (presupuesto mayo).

---

## 8. Tesorería (parche)

MJ R2: «este ERP **no está hecho para conciliar ni calzar** pago↔factura».

| Práctica | Detalle |
|---|---|
| Pago proveedores | Banco + forma TRANS + radio peso/dólar. **Se puede grabar sin tildar** factura. ΔTC solo si calzan en dólar |
| N° cartola | Hoy ponen **1** a mano; debería ir el n° real (ej. 5200156) — R4 Agrosoft ALM, Alarcón, tipo 33 |
| Conciliación | **Manual**, 2 grillas cartola vs conta. Import **solo Excel**. Quieren PDF banco (lo intentaron, no). ~300 líneas. Varias cartolas/mes = lío al borrar |
| Orden real | Contabilizan **primero**; suben cartola a **fin de mes**. Quieren: cartola = verdad, imputar **encima** (28/08) |
| Reversa conciliación | **Todo el mes**, no una línea. Error de empresa = rehacer el mes |
| Anticipos | ALM **da** a productores (USD/contrato; a veces pagan CLP). AlmaWeb **recibe** de clientes. A veces «traspaso» para partir anticipo |
| Yuan | Cuenta `110102006`; seguimiento fino en **Excel / Power BI** |

Excel visto 20/08: `06-CARTOLA_JUNIO_2026.xls` — Scotiabank ALM + pestañas ALM/Almahue CLP/USD/**YUAN**.

---

## 9. Lo que el menú tiene y **no usan**

- Mano de obra Agrosoft → **Book**.
- Maquinarias.
- Gestión Agrosoft → **Power BI** (Mario).
- Solicitud de compra.
- Niveles de bodega.
- Ingrediente activo (sí en agrícola, no en el flujo que mostró MJ).

---

## 10. Freshlink / AlmaWeb (hermano, no este ERP)

08–09/07 (`E:\grabaciones`): embarques, formatos uva/cereza, Guangzhou Fresh Link, MM Manager. Es el **as-is COMEX/cajas**, no el as-is contable. El ERP nuevo no lo reemplaza en esas demos.

---

## 11. Cuentas y folios ancla (para no inventar)

| Pieza | Valor visto |
|---|---|
| Producto | Agrosoft **r.3.0.2** |
| Empresas demo | ALM `javillela` / `mjrodriguez`; Santa Pilar `ROLGUIN` |
| OC prueba | **5207** Sandoval y Fuentes, exenta 1.000 |
| Asiento recepción | **8310** · `610104009` / `210802004` |
| Haber contratistas | `210802003` |
| Contrato / proforma | **179** → definitiva **155** · 37.500 |
| Banco yuan | `110102006` |
| Banco Chile $ (pago R4) | `110102001` |
| Tipo ref. export | **110** |

---

## 12. Lectura corta

Almahue no opera «OC → aprueba → recibe → factura» como el menú. Opera **factura/servicio primero**, OC de conta después, gasto en la **recepción**, DTE en **Acepta**, banco en **Excel**, cajas en **AlmaWeb**, MO propia en **Book**. El ERP se diseña para **dejar de parchar** eso; no para clonar cada pantalla.
