# Propuesta DTE exportación (110 / 111 / 112) — 10/09/2026

Fuente primaria: MJ (manual COMEX + Reu4). Técnico: Pablo GoSocket (Gap + GUF + kickoff 01/09). Esquema: tablas Aduana (Anexo 51) citadas en el Gap. **No** es requisito lo que Carlos/Sergio hipoteticen en internas.

Canvas: `canvases/dte-exportacion-propuesta.canvas.tsx`.

---

## Dónde viven los documentos

| Qué | Quién | Dónde en el repo | Para qué |
|---|---|---|---|
| Manual NC/ND cierre COMEX | **MJ** (Reu4, pack 30/07) | [`fuentes/mj-compartidos-2026-07-30/EMISION_DE_NOTA_DE_CREDITO_Y_DEBITO_FACTURAS_CIERRE_COMEX.docx`](../fuentes/mj-compartidos-2026-07-30/EMISION_DE_NOTA_DE_CREDITO_Y_DEBITO_FACTURAS_CIERRE_COMEX.docx) · extracto [`extractos/EMISION_NC_ND_COMEX.txt`](../fuentes/mj-compartidos-2026-07-30/extractos/EMISION_NC_ND_COMEX.txt) | Procedimiento de **negocio** (Acepta). Campos que el operador rellena hoy. |
| Inventario del pack MJ | — | [`fuentes/mj-compartidos-2026-07-30/00-README.md`](../fuentes/mj-compartidos-2026-07-30/00-README.md) | Índice; el resto del pack es conta/tesorería, no DTE. |
| Gap DTE CL v.7 (obligatoriedad M/O/C **incluye 110/111/112**) | **Pablo** vía MJ 05/08, ticket 14213 | [`fuentes/gosocket-2026-08-05/Integracion-API-cliente/Gap Analisis_DTE_CL_v.7.xlsx`](../fuentes/gosocket-2026-08-05/Integracion-API-cliente/Gap%20Analisis_DTE_CL_v.7.xlsx) · extracto [`extractos/gap_summary.txt`](../fuentes/gosocket-2026-08-05/extractos/gap_summary.txt) | Contrato de **campos** por tipo. Guía SII/Aduana embebida (catálogos Anexo 51). |
| Plantilla GUF + ejemplo JSON | Pablo | `DTE_33-34-39-41-46-52-56-61.xml` + `Example_integracion.json` | Ejemplo de **envoltorio** API. El XML de ejemplo es **tipo 33**, no 110. Kickoff 01/09: esa plantilla **no** es el contrato vigente (formato_dte 2.5). |
| Manual API | Pablo | `Manual API.pdf` | REST async Chile, PDF/XML download. |
| Kickoff API | Pablo 01/09 | [`reunion-2026-09-01-gosocket-kickoff.md`](../reunion-2026-09-01-gosocket-kickoff.md) | Set **básico primero**; exportación **después**. `CodRef` 1/2/3 también en NC/ND export. CAE Export N° 0 / 2024-10-11. |
| Tablas Aduana (SII/Aduana) | Gap → [Anexo 51](https://www.aduana.cl/compendio-de-normas-anexo-51/aduana/2009-11-19/163937.html) | Países T7, puertos T10, vías T12, cláusulas, modalidades, tipos de bulto | Códigos **numéricos** que el XML debe llevar. No “FOB” ni “MARITIMA” en claro. |

**No está en el repo:** un spool GUF **110** de Pablo (dijo que el de factura internacional servía para NC/ND si se validan aduana con MJ). Tampoco un Excel Comex de un embarque real (el manual lo cita). Si llega un XML 110, guardarlo en `fuentes/gosocket-2026-08-05/ejemplos-110/` y no mezclarlo con el Gap de agosto.

---

## Qué pidió el cliente (no el proveedor)

**Reu4 MJ (~46:28):** toda factura de exportación termina en **NC o ND al liquidar** la fruta (yo gané / tú me debes). No es anulación total: **corrige montos (CodRef 3)**.

**Manual MJ:** se emite en **Almahue Export Spa**. Cliente, dirección y especie salen de la factura 110. ID fiscal receptor = **55.555.555-5**. Precio = USD neto ÷ cajas, **6 decimales**. Unidad **caja**. Referencia tipo **110** + folio + fecha. Motivo cierre: “Corrige Monto: ND/NC por cierre”. Transporte: “DESPACHO POR CUENTA DEL EMISOR”. Aduana: modalidad, país, cláusula FOB/CIF, vía marítima/aérea, puertos, bulto **22** + marca `-`. Observación `TC` + tipo de cambio. Moneda **13 USD**. Otra moneda = CLP (total y exento iguales). Naming `ND 1263 EMB 65`.

**Pablo 01/09:** exportación = aduana + país destino + embarque **después** del set básico (33 ya en sandbox). No inventar tags; el XSLT de GoSocket copia nombres SII.

---

## Flujo que no se rompe

Hoy (nacional) queda igual:

```
OV CONFIRMADA → Ventas › Emitir DTE (33/61/56/52)
  → billing-gateway GUF → GoSocket
  → Libro de ventas EMITIDO → cuenta/CC por ítem → CONTABILIZADA
```

Exportación **reusa el mismo tubo**. Solo cambia el **indicador de venta** y el tipo SII:

| Indicador | Factura | NC | ND |
|---|---|---|---|
| VENTA / SERVICIO | 33 | 61 | 56 |
| EXENTO | 34 | 61 | 56 |
| **EXPORTACION** | **110** | **112** | **111** |

Reglas de no-regresión:

- El mapper **no emite tags COMEX** si `tipoDte` no es 110/111/112 (ya testeado).
- IVA 0 / `MntExe` solo en export/exento. El 33 sigue con IVA 19.
- D16 se **apaga** en exportación (precio de embarque, no piso de bodega). Nacional no se toca.
- Stock: igual que hoy (sale al confirmar OV). NC/ND de liquidación **no** reingresa bodega (fruta Almahue).
- Libro, tracker, CodRef 1/2/3, contabilizar: mismos botones. El 110 es una FACTURA más, con badge/indicador.
- Sociedad: **Export** (`gosocketBillerId` + CAE de Admin › Empresas). No emitir 110 con el biller de ALM.

---

## Qué hay hoy vs hueco

| Capa | Hay | Falta para que el SII/GoSocket acepte un 110 |
|---|---|---|
| UI Emitir paso 3 | Bloque «Datos COMEX» si indicador = Exportación. Defaults MJ. Cajas/USD/CLP calculados. | Combos con **códigos Aduana**, no texto libre. País del **receptor** (CodPaisRecep, M). `TpoMoneda` 13. Copiar COMEX al emitir NC/ND. Observación `TC …` automática. |
| Canónico ERP | `documento.comex` + `mapTipoDte` 110/111/112 | `codPaisRecep`, `tpoMoneda` (13), `indTraslado`/`bultoMarca` no viajan al GUF. |
| Gateway GUF | Tags sueltos: TpoCambio, MntTotOtrMnda, TotBultos, CodPto*, CodClauVenta… | Falta **MntExe**, **TpoMoneda**, **CodPaisRecep**. Los códigos FOB/MARITIMA no son los de la tabla. Posible wrap `Transporte`/`Aduana`/`OtraMoneda` si el XSLT 2.5 no copia tags sueltos (validar con spool Pablo). |
| Receptor | EX-* → 55.555.555-5 | Dirección/ciudad receptor **M** en 110 (el 33 ya exige DirRecep). |
| NC/ND cierre | Origen + CodRef 3 en Emitir | Precarga ítems + COMEX de la 110; precio 6 decimales; no pedir de nuevo aduana. |
| QA | Tests mapper 110 | Envío sandbox Export + CAF 110. Sin eso el ⌛ de GoSocket sigue. |

---

## Propuesta de producto (UI compatible)

**No hay menú nuevo.** Sigue **Ventas › Emitir DTE**, mismos 3 pasos, mismos `Field` / `Card` / `SearchableSelect`.

1. **Paso 1.** Indicador **Exportación** (ya existe). Al elegirlo: RUT receptor extranjero fijo si el cliente es export; no inventar RUT chileno. Totales panel: IVA 0, mostrar **USD y CLP**.
2. **Paso 2.** Ítems: unidad por defecto `caja`; precio 6 decimales; D16 off. Misma grilla.
3. **Paso 3.** El recuadro COMEX actual se **reordena** en tres grupos (como Acepta: Transporte / Aduana / Otra moneda), sin wizard extra:
   - Transporte: glosa fija MJ (solo lectura salvo override).
   - Aduana: modalidad, cláusula, vía, país receptor, país destino, puertos — `SearchableSelect` con código + nombre.
   - Bultos: tipo 22, cantidad = cajas (readonly), marca `-`.
   - Montos: USD y CLP readonly (cálculo cajas). TC editable. Observación se rellena `TC {tc}`.
4. **NC/ND.** Si el origen es FACTURA con indicador exportación: tipo DTE 112/111, referencia 110, COMEX **heredado**, ítems precargados. El operador solo ajusta cantidades/precios (cierre).
5. **Libro.** Misma fila FACTURA/NC/ND. Folio SII. Origen/cadena ya muestra 110 ↔ 112.

Catálogos: seed estático (países/puertos/vías más usados por Export) + código libre. No scraping Aduana.

---

## Orden de implementación (no mezclar oficios)

| Fase | Qué | Criterio de listo |
|---|---|---|
| **A** Gateway | GUF 110: MntExe, TpoMoneda=13, CodPaisRecep, TotBultos, mapear FOB→código Aduana, CIF, vía 1/4, bulto 22. Tests. 33/61 sin tags nuevos. | Tests verdes; XML de fixture comparado con Gap M. |
| **B** Canónico | Campos que faltan en `comex`; validar export fail-closed (sin país receptor / sin bultos / sin TC → no `emit()`). | No sale HTTP a GS si falta M. |
| **C** UI | Combos + herencia NC/ND + observación TC. Sin paso 4. | Misma pantalla; nacional idéntico. |
| **D** Sandbox | Emitir 110 con biller Export, GID ≠ 0, ACE o RCH leíble. | Pablo/CAF. No fingir ACE. |
| **E** Cierre COMEX | NC/ND CodRef 3 desde Libro (igual Anulación, pero montos). | MJ puede liquidar sin rellenar aduana. |

Fuera de esta tanda: recepción GS→compras, SMTP, guía logística, carga RCV xlsx.

---

## Riesgo si se implementa mal

- Mandar **33** con bloque COMEX → rechazo o XML sucio (el mapper ya lo evita).
- Mandar texto “FOB” en `CodClauVenta` → RCH Aduana.
- Usar biller ALM en sociedad Export (ya pasó en Postman).
- Tratar el cierre COMEX como **Anulación CodRef 1** → le dice al SII que la 110 no vale; MJ lo contradice.
