---
name: almahue-analisis-reunion
description: >-
  Analiza una reunion del ERP Almahue con cinco subagentes en orden: casos de
  uso, plan de integracion, plan de pruebas, contraste con el codigo
  (conservar o cambiar) y ejecucion de pruebas. Usar cuando pidan analizar una
  reunion, armar casos de uso desde una transcripcion, plan de integracion,
  contraste con el codigo o el paquete de requerimientos de una sala.
---

# Analisis de reunion

Pedido, en este orden:

> analizaremos la reunion y con un sub agente haremos todos los casos de uso que se detecten en esa reunion. despues, otor sub agente planificara la integracion, otro sub agente generara el plan de pruebas, luego otro sub agente, analizara la implementacion y la contrastara con el codigo actual para ver que conservar/cambiar y finalmente otro sub agente debe realizar las pruebas.

El agente padre no escribe esos cinco documentos. Lanza un subagente, espera el archivo, y recien entonces lanza el siguiente. No van en paralelo: cada uno lee lo que dejo el anterior.

No se implementa codigo, no se hace commit y no se toca produccion. Si falta la transcripcion, primero la skill `almahue-transcript-local`. Sin markdown de la sala no arranca el primer subagente.

Modelo de salida: `docs/requerimientos/oc-dte-parcial-2026-10-14/`.

## Carpeta

`docs/requerimientos/<tema>-<fecha>/`

| Orden | Subagente | Archivo |
|---|---|---|
| 1 | Casos de uso | `casos-de-uso.md` |
| 2 | Plan de integracion | `plan-integracion.md` |
| 3 | Plan de pruebas | `plan-pruebas.md` |
| 4 | Contraste con el codigo | `contraste-codigo.md` |
| 5 | Pruebas | `resultados-pruebas.md` |

## Como lanzarlos

Herramienta Task, `subagent_type` `generalPurpose`, un llamado por vez, `run_in_background` false. El subagente no ve el chat: el prompt trae la ruta de la transcripcion, la carpeta de salida y el bloque de reglas. Si la sesion obliga a dejarlo en segundo plano, no lances el siguiente hasta el aviso de que termino, y no abras el 2, el 3, el 4 ni el 5 juntos.

Si el archivo de esa etapa no quedo escrito, te detienes y dices cual fallo. No saltas a las pruebas.

Al cerrar, respondes en espanol con las cinco rutas, cuantos casos salieron, el recuento conservar / cambiar / no usar, y cuantas pruebas pasaron. No reescribas los documentos.

## Reglas que van en los cinco prompts

- Escribe en espanol. No uses raya larga ni flecha. Usa `-` y `>`.
- La transcripcion es la fuente. La minuta es un indice. Si chocan, gana la transcripcion.
- Carlos y Sergio son hipotesis. Un caso entra si lo dice el cliente (Agustin, Maria Jesus, Lupe, Mario, Rodrigo, Fran) o si el cliente confirma la frase.
- Reu1 a Reu3 son el as-is de Agrosoft. Reu5 no cuenta: no hubo cliente. Si Reu6 y Reu4 chocan, gana Reu6.
- No inventes un caso para tapar un silencio. Si la voz no tiene nombre, dilo y usa la pista de la sala.
- No implementes, no hagas commit, no emitas DTE, no pagues, no cierres el mes y no corras `prisma migrate deploy`.
- Empresa de lectura: ALMAHUE EXPORT SPA, local. Front `http://localhost:5174`, API `http://localhost:3001/api/v1`.

## 1. Casos de uso

Lee la transcripcion completa. Busca el mismo tema en otras `docs/reuniones/transcripciones/transcripcion*.md` y anota cuales no aplican.

Cada caso: quien, archivo y minuto, que pasa, documento, que debe quedar. Numerados CU-01, CU-02, ...

Devuelve la ruta y la cantidad de casos.

## 2. Plan de integracion

Lee `casos-de-uso.md` y el codigo que esos casos tocan (`ERP/erp_back`, `ERP/erp_front`). No redefinás pantallas ni propongas un parche.

Por caso: por donde entra hoy, que deja el codigo hoy, que pide la sala, de que otros casos depende.

Devuelve la ruta y los modulos que toca.

## 3. Plan de pruebas

Lee `casos-de-uso.md` y `plan-integracion.md`. No ejecutes nada.

Un caso, una prueba (P-01, ...), mas los limites. Cada prueba tiene el resultado de hoy y el resultado esperado de la sala. Pasa solo la columna de la sala. Un atajo del codigo actual no acredita el caso.

La factura de proveedor, si el tema es compras, entra por un registro del libro ya existente o por carga manual. No se dispara emision ni un evento a GoSocket para ver que pasa.

Devuelve la ruta y la cantidad de pruebas.

## 4. Contraste con el codigo

Lee los tres documentos y el codigo. No propongas un parche.

Tabla por pieza, con veredicto `CONSERVAR`, `CAMBIAR` o `NO USAR PARA ESTE CASO`, el CU y por que. Di que hace hoy esa pieza y que tendria que hacer para el caso.

Devuelve la ruta y el recuento de cada veredicto.

## 5. Pruebas

Lee `plan-pruebas.md` y `contraste-codigo.md`. Escribe `resultados-pruebas.md`.

Corre lo que el plan nombre (Jest en `ERP/erp_back`, y pantalla solo si el plan la pide y el stack responde). Para la pantalla usa Playwright, no el navegador interno. No achiques el viewport. No guardes, contabilices ni pagues un documento para sacar una foto.

No corrijas bugs de producto. No emitas DTE, no llames al SII, no pagues, no cierres el mes y no corras `prisma migrate deploy`. Si el arranque falla, el resultado es bloqueo de ambiente, no un fallo del caso.

Un pase es solo el resultado esperado de la sala.

Devuelve la ruta y, por prueba, pasa, falla o bloqueo.
