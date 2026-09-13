# Kickoff GoSocket 14213 — Holding Almahue (01/09/2026)

**Tipo:** Mesa API GoSocket (directrices nuevas de campos y body).  
**Fecha:** 2026-09-01 ~16:00 UTC (~38 min).  
**Participantes:** Pablo Rodriguez (GoSocket), Carlos Vallejos, Sergio Silva; invitados MJ, Mario, Vanessa Adams, Cristian Zúñiga (MJ no se conectó: contrato).  
**tl;dv:** https://tldv.io/app/meetings/6a96f651fb2cc300133c3cd5  
**Peso:** esta reunión **pisa** el addendum portal 31/08 en `DefaultCertificate` y concreta el CAE que la minuta de agosto solo mencionaba como “error de carátula”.

No es la minuta de onboarding de agosto (`reunion-gosocket-minuta-2026-08.md`).

---

## Acciones inmediatas (Pablo → Carlos)

| # | Qué | Estado en código |
|---|---|---|
| K-1 | `BillerId` de la sociedad que se está probando (Export ≠ ALM). Usar el UUID que Pablo pegó en el chat. | Ya iba por `Empresa.gosocketBillerId`. El fallo de Postman fue probar Export con el biller de ALM. |
| K-2 | `DefaultCertificate: false` (Carlos lo repitió; Pablo confirmó). | El ejemplo oficial ya lo traía en false; el 31/08 quedó en true. **Queda false.** |
| K-3 | `NroResolucion` + `FechaResolucion` **obligatorios** en el GUF (`CAE`). Null no es datetime. | Chat Pablo: **ambas** N° **0**. Export `77032638-9` fecha **11-10-2024** (`2024-10-11`). ALM `77032639-7` fecha **14-02-2020** (`2020-02-14`). El “9” del audio era ruido. Viven en Admin › Empresas y viajan en el canónico. Cambian en productivo. |
| K-4 | Guardar `GlobalDocumentId` para consultas posteriores. HTTP 200 ≠ éxito. Si el GID viene en **0**, responder negativo al usuario. | Gateway: GID 0 / UUID cero → `REJECTED` aunque `Success: true`. |
| K-5 | Pablo reenvía a Carlos el documento de validaciones (largos, obligatoriedad 1/2/3). | Pendiente de correo. |

---

## Campos que el servicio pidió en los XML de prueba

Obligatorios ahora (set básico, factura electrónica):

- Fecha y número de resolución (CAE)
- Dirección de origen (`DomFiscal/Calle` de Almahue Export)
- Razón social del receptor
- RUT del receptor
- Monto total
- Monto de ítem en el detalle

Video (formato_dte 2.5 + XML SII válido `DOC_33_*`): el XSD exige **Acteco** (6 dígitos) **antes** de `DirOrigen`; `RUTRecep` **antes** de `RznSocRecep`; `MntNeto`/`MntTotal`/`IVA`; detalle `NmbItem`/`PrcItem`/`MontoItem`. TED `RR`/`MNT`/`IT1` se arman solos si eso va lleno. La plantilla GUF de agosto (`DTE_33-34-…xml`) **no** es el contrato de hoy.

No mandar (el servicio los menciona si falta DirOrigen, pero no hacen falta):

- Teléfono emisor
- Correo emisor

Ignorar en el diagnóstico de esquema (los arma la firma/TED si arriba está el RUT receptor):

- RR / RSR / IT1 de firma

Límites dichos en la mesa:

- Razón social emisor: **100** alfanuméricos. GoSocket **no trunca**; si te pasás, rechaza.
- `CodRef` en NC nacional y de exportación: solo **1** (anula), **2** (corrige texto), **3** (corrige montos). Texto “anular” no sirve.

Personalizados: ilimitados, el servicio no los valida; se **sacan** del XML que va al SII. Sirven para la representación gráfica.

---

## Cómo leer la respuesta API

1. `200 OK` = contactaste la API.
2. Mirar `Success` true/false **o** (recomendado) `GlobalDocumentId` en 0 → no se emitió.
3. Ejemplo de GID 0: Pablo quitó el BillerId → el asignador de folio no encuentra rango CAF.

Portal: pegar el GID; filtro últimos 3 meses; Control+clic en folio abre el detalle.

---

## Alcance de sets (no ahora)

- Primero set **básico** nacional; después diferencias por tipo (exenta informa exento, no subtotal).
- **Boletas:** otro esquema.
- **Exportación:** aduana, país destino, embarque — después del set básico.
- Representación gráfica a medida: Pablo necesita spool válido (Sergio: próxima semana). PDF API = `Get Download Document PDF` en base64, plantilla estándar.
- IO Facturo: post contrato MJ/Cristian. Distinto de API.

---

## Chat Pablo — resoluciones QA (fuente)

| Sociedad | RUT | N° | Fecha (chat) | ISO en ERP |
|---|---|---|---|---|
| ALMAHUE EXPORT SPA | 77.032.638-9 | 0 | 11-10-2024 | 2024-10-11 |
| ALM SERVICES SPA | 77.032.639-7 | 0 | 14-02-2020 | 2020-02-14 |

BillerId por sociedad: Admin › Empresas (no en el gateway).
