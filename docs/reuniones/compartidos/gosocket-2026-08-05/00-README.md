# Fuentes GoSocket — Holding Almahue (05/08/2026)

Material reenviado por **María Jesús Rodríguez** (`mjesus.rodriguez@almahuexport.cl`) el 5 ago 2026, originado por **Pablo Rodríguez** (Consultor GoSocket Chile) — ticket **14213** (*Set Básico y de Exportación por API, IoFacturo y Conciliación — 2 RUTs*).

## Contenido

| Archivo | Uso |
|---|---|
| `Integracion-API-cliente/Manual API.pdf` | Contrato REST (auth, endpoints, Chile async) |
| `Integracion-API-cliente/Example_integracion.json` | Ejemplo emisión: JSON wrapper + XML GUF en `FileContent` |
| `Integracion-API-cliente/DTE_33-34-39-41-46-52-56-61.xml` | Plantilla campos GUF por tipo DTE |
| `Integracion-API-cliente/Gap Analisis_DTE_CL_v.7.xlsx` | Obligatoriedad M/O/C por tipo (incluye export 110/111/112) |
| `Informacion para representacion grafica.xlsx` | Ficha emisor para PDF/timbre (onboarding, no API) |

## Hallazgo de contrato (importante)

GoSocket **no** recibe HTML ni PDF de entrada. El flujo real es:

1. Cliente envía **JSON** a `POST .../Document/SendDocumentToAuthority`
2. `FileContent` = **XML GUF** (string embebido)
3. GoSocket transforma a XML SII, firma y responde; el acuse SII en Chile es **asíncrono** → polling `GetDocument`
4. PDF/XML timbrados se **descargan** (`DownloadDocumentPdf` / `DownloadDocumentXml`)

**Propuesta DTE 110/111/112 (10/09):** [`../../analisis-reuniones/10-propuesta-dte-exportacion-2026-09-10.md`](../../analisis-reuniones/10-propuesta-dte-exportacion-2026-09-10.md). El XML de ejemplo de esta carpeta es tipo **33**; el Gap sí cubre 110/111/112. Un spool 110 de Pablo, si llega, va en `ejemplos-110/`.

## Relación con billing-gateway

Servicio propuesto (repo git separado, nombre temporal): **`billing-gateway`**.  
Plan: [`../../partners-hub/00-PLAN-IMPLEMENTACION.md`](../../partners-hub/00-PLAN-IMPLEMENTACION.md).
