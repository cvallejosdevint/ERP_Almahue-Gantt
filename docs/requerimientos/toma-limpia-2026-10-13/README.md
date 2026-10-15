# Toma de requerimientos en limpio (13/10/2026)

Lectura nueva de las 28 transcripciones en `docs/reuniones/transcripciones/` (21/07 a 06/10/2026, cerca de 1,15 millones de caracteres). No se usaron skills, minutas, analisis ni `AGENTS.md` como fuente del pedido. Esos textos ya interpretan las reuniones. Aqui manda lo dicho en la transcripcion.

El codigo se miro solo para la columna de estado del checklist: que existe hoy en `ERP/erp_back` y `ERP/erp_front`.

## Como se armo

1. Cada transcripcion se leyo aparte y se volco a una ficha (enunciado, modulo, clase, voz, cita, marca de tiempo).
2. Los cuatro digest estan en `digests/`. Salieron 534 fichas. 337 tienen voz de cliente (Agustin, Maria Jose / MJ, Lupe, Mario, o el relato que el texto les atribuye). Los digest conservan los nombres como salieron de la lectura.
3. Si dos reuniones se contradicen, queda anotada la evolucion y manda la fecha mas nueva dicha por el cliente.
4. Carlos y Sergio, cuando hablan solos, quedan como voz de equipo en los digest. No entran al checklist salvo que el cliente lo haya confirmado despues.

## Archivos

| Archivo | Que es |
|---|---|
| `mapa.md` | Modulos, flujo y decisiones que cambiaron de fecha |
| `diagrama.md` | Flujos que el cliente describio |
| `checklist.md` | Pedido vigente contra el codigo: hecho, a medias, falta |
| `digests/` | Fichas con la cita, por bloque de reuniones |

## Quien habla, y cuando

| Bloque | Archivos | Quien pesa |
|---|---|---|
| 21/07 a 30/07 | `transcripcion.md`, reunion 2, 3 y 4 | Cliente mostrando Agrosoft / AlmaWeb (as-is) y pidiendo el ERP nuevo |
| 03/08 a 28/08 | reunion 5 y 6, tarde Lupe y Mario, tesoreria MJ y Lupe | Decisiones de alcance |
| 10/09 a 01/10 | demos y reuniones de cliente | Ajustes de factura, compra parcial, libros y nomina |
| 03/09 a 06/10 | internas y GoSocket | En el checklist solo entra lo que el texto atribuye al cliente. El 06/10 Maria Jose redefine contratistas |
