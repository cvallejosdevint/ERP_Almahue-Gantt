# Validación capturas ERP demo — Reunión 1 + Reunión 2

**Fecha:** 23/07/2026  
**Modo:** Demo (`localStorage almahue-erp-demo-mode=true`)  
**Base:** http://localhost:5174 · `admin@almahue.local` / `Admin123!`  
**Capturas ERP:** `capturas-validacion-erp/reu1/` y `capturas-validacion-erp/reu2/`  
**Legacy reunión (referencia):** `pantallas-legacy/` y `pantallas-legacy/reunion2/`  
**Script:** `capture-validacion-reu1-reu2.mjs`

### Nota sobre el video Reu 2

En la demo el presentador pasó pantallas con poco tiempo entre cada una.  
La validación **no** depende de frames aislados del video: se cruza el **análisis documental** (`reunion2-analisis-2026-07-23.md` + índice Trello) con capturas **estables** del ERP en modo demo.

**Leyenda**

| Estado | Significado |
|---|---|
| OK | Cubierto en demo con captura ERP |
| PARCIAL | Cubierto en UX/mock, falta profundidad o backend |
| OUT | Explicitamente fuera de alcance |
| GAP | No aplicado / no visible |

---

## A) Reunión 1 — checklist vs ERP demo

| # | Lo mostrado / solicitado (legacy) | Ruta ERP | Captura | Estado | Evidencia |
|---|---|---|---|---|---|
| R1-01 | Login / cambio empresa | `/login` | `reu1/01-login.png` | OK | Formulario login demo |
| R1-01b | Temporada + mes contable (+ remuneración) | post-login / header | — | OK demo | Modal periodo + selector header; **capturar** |
| R1-02 | Panel operativo | `/` | `reu1/02-panel.png` | OK | KPIs operativos |
| R1-03 | Tarifas multi-línea | `/contratistas/tarifas` | `reu1/03-tarifas*.png` | OK | Lista + form labor/actividad/CC |
| R1-04 | CC por empresa activa | `/catalogos/centros-costo` | `reu1/04-centros-costo.png` | OK | CC con empresa |
| R1-05 | Perfiles Admin / Digitador / Intermedio | `/admin/roles` | `reu1/05-roles.png` | OK* | *Reu 2 renombró a Digitador contratistas / Analista / Admin |
| R1-06 | OC sin Solicitud de Compra | `/compras/ordenes` | `reu1/06-orden-compra.png` | OK | Listado OC |
| R1-07 | Distribución CC (en flujo OC) | `/compras/ordenes` | (misma) | OK demo | Form OC con líneas CC + cuadratura neto; **re-capturar** |
| R1-08 | Aprobación OC | `/compras/aprobaciones` | `reu1/08-aprobacion-oc.png` | OK | Cola aprobaciones |
| R1-09 | Recepción + TC | `/compras/recepciones` | `reu1/09-recepcion.png` | OK | Recepción con TC |
| R1-10 | Registro compra anti-cruzado + alerta A/E | `/compras/registro` | `reu1/10-registro-compra.png` | OK demo | Banner alerta afecto/exento + FAC-8809; **re-capturar** |
| R1-11 | Maestro artículos | `/insumos/maestro` | `reu1/11-maestro.png` | OK | Catálogo insumos |
| R1-12 | Bodegas por empresa | `/insumos/bodegas` | `reu1/12-bodegas.png` | OK | Bodegas |
| R1-13 | Movimientos / NC precio factura | `/insumos/movimientos` | `reu1/13-movimientos.png` | OK | Movimientos bodega |
| R1-14 | Asientos / carga | `/contabilidad/asientos` | `reu1/14-asientos.png` | OK | Asientos |
| R1-15 | Indicadores Banco Central | `/contabilidad/indicadores-bc` | `reu1/15-indicadores-bc.png` | OK | Serie BC |
| R1-16 | Proformas contratista | `/contratistas/proformas` | `reu1/16-proformas.png` | OK | Borrador→Definitiva→Factura |
| R1-17 | Traspaso / cierre | `/contratistas/traspaso` | `reu1/17-traspaso.png` | OK | Estados contables |
| R1-18 | Niveles almacenamiento | — | — | OUT | PEND-03 → OUT en Reu 2 (DEC-12) |
| R1-19 | Maquinaria | — | — | OUT | DEC-10 |

**Veredicto Reu 1 (demo):** cobertura **OK** de lo mockeable; OUT respetados.

---

## B) Reunión 2 — checklist vs ERP demo

| Código | Lo mostrado (legacy Reu 2) | Solicitud | Ruta ERP | Captura | Estado | Evidencia en captura |
|---|---|---|---|---|---|---|
| R2-C01 | 06-agrosmart-ingreso-mano-obra | Ingreso diario labores | `/contratistas/ingreso-diario` | `reu2/03-ingreso-diario*.png` | OK | Fecha, CC, labor, jornada/trato, precio, monto, estados |
| R2-C02 | 06 + tarifas | Precio editable (no tarifario rígido) | ingreso + form | `reu2/03-ingreso-diario-form.png` | OK | Campo precio unitario editable; hint tarifario |
| R2-C03 | 02-actividades-sin-filtro | Actividad filtrada por labor | `/contratistas/tarifas` | `reu2/01-tarifas-filtro-labor-form.png` | OK | Label «Actividad … filtrada por labor» |
| R2-C04 | 05-agrosmart-asociacion | Asociación masiva + calce | `/contratistas/asociacion` | `reu2/04-asociacion-labores.png` | OK | Checkboxes, proforma destino, calce monto |
| R2-C05 | 03/04 proforma | N proformas → 1 factura + multi-mes | `/contratistas/proformas` | `reu2/02-proformas-n1.png` | OK | Periodo `2026-06/2026-07`; botón Asociar factura (modal N:1) |
| R2-C05b | 03/04 proforma | Confirmación borrador → definitiva | proformas | `reu2/02-proformas-confirm-definitiva.png` | OK | Modal resumen + «Sí, emitir definitiva» |
| R2-C06 | demo cierre | Asiento facturas por recibir vs costo MO | `/contratistas/traspaso` | `reu2/05-traspaso-cierre.png` | OK | Totales + tasas CLP/USD/CNY/EUR |
| R2-V01 | 08-ventas-no-editar | Reversa reutiliza datos | `/comercial/libro` | `reu2/06-libro-comercial.png` | OK | Columna Origen «Reversa de…»; acción Reversar |
| R2-V01b | (mismo) | Cadena asientos original/reversador/nuevo | libro | (re-capturar) | OK demo | Asi. 472/473/474 en columna Origen/cadena |
| R2-V02 | (mismo) | Confirmación al grabar desde reversa | libro | (flujo) | OK | Confirm dialog en código + botón Grabar |
| R2-V03 | 09-ventas-guardar | Solo Grabar y contabilizar | libro | `reu2/06-libro-comercial.png` | OK | Texto explícito + botón (sin Guardar) |
| R2-V04 | — | Búsqueda clientes robusta | libro | `reu2/06-libro-comercial.png` | OK | Search folio/cliente/RUT |
| R2-T01 | 11-tesoreria-carga-cartola | Carga cartola Excel/PDF | `/tesoreria/cartolas` | `reu2/08-carga-cartola.png` | OK | Archivos .xlsx/.pdf, estados |
| R2-T01b | cartola | Contabilizar desde cartola | cartolas → Movimientos | (re-capturar) | OK demo | Pendientes + botón Contabilizar |
| R2-T02 | 12-conciliacion | Conciliación desde cartola | `/tesoreria/conciliacion` | `reu2/09-conciliacion.png` | OK | Link a cartolas + asiento |
| R2-T03 | 12 | Link a asiento si diferencia | conciliacion | `reu2/09-conciliacion.png` | OK | Columna Asiento |
| R2-T04 | 13-reversa-mes | Reversa selectiva | conciliacion | `reu2/09-conciliacion-movimientos.png` | OK | Modal Movimientos + Desconciliar por fila |
| R2-T05 | 14-anticipos | Anticipos calce parcial | `/tesoreria/anticipos` | `reu2/10-anticipos.png` | OK | Saldo / calzado / botón Calzar |
| R2-T06 | 10/15 pagos TC | TC bidireccional | `/tesoreria/pagos` | `reu2/07-pagos-tc*.png` | OK | Moneda pago/factura + dif. TC + docs |
| R2-T07 | — | Nóminas / aging >90 días | `/tesoreria/nominas` | — | OK demo | KPI + filtro >90; **capturar** |
| R2-R01 | 17/20 roles | Digitador / Analista / Admin | `/admin/roles` | `reu2/11-roles-matriz.png` | OK | Roles seed Reu 2 |
| R2-R02 | 17 | Checks R/W por pantalla | roles | `reu2/11-roles-matriz.png` | OK | Link matriz R/W |
| R2-K01 | 16 sync | Sync BC auto/manual | monedas + indicadores | `reu2/13` + `reu2/14` | OK | Traer BC / Actualizar ahora |
| R2-K02 | 18-centros-costo | Contacto encargado | `/catalogos/centros-costo` | `reu2/12-centros-encargado.png` | OK | Columna Encargado (Mario…) |
| R2-G01 | — | GoSocket ~01/09 indep. ERP | `/integraciones/gosocket` | `reu2/15-gosocket-dec14.png` | OK | Banner DEC-14 |
| DEC-12 | — | Niveles OUT | — | — | OUT | Sin pantalla de niveles |
| UI AgroSmart | 07-agrosmart-ui | UX amigable referencia | ingreso/asoc | `reu2/03`, `04` | PARCIAL | Flujos cubiertos; no clon visual AgroSmart |

**Veredicto Reu 2 (demo):** **OK** en mocks de reunión. G1–G5, G7–G8 y aging/nóminas cerrados en demo; regenerar capturas listadas como «re-capturar» / «capturar».

---

## C) Cómo regenerar

```powershell
# Front en :5174
cd E:\source\repos\Almahue\docs\erp-planificacion\agrosoft-levantamiento
node capture-validacion-reu1-reu2.mjs
```

---

## D) Conclusión

| Reunión | ¿Aplicado en demo? |
|---|---|
| Reu 1 | **Sí** — mocks operativos alineados a lo levantado |
| Reu 2 | **Sí** — pantallas nuevas + refinamientos; G1/G2 (reversa selectiva + confirm definitiva) capturados |

Las capturas legacy de `pantallas-legacy/reunion2/` siguen siendo la **referencia del sistema actual del cliente**; las de `capturas-validacion-erp/` demuestran que **nuestro ERP demo** absorbe esos requerimientos.
