---
name: duoc
description: >-
  Marco del proyecto de título DUOC (ERP, con Felipe) y planificación de la
  carta Gantt por sprint en el Trello https://trello.com/b/mwuark1s/erp-almahue.
  Usar únicamente cuando el usuario invoca el comando /duoc. No aplica a
  entregas ni al Trello de cliente Almahue.
disable-model-invocation: true
---

# /duoc — proyecto de título DUOC

Activar este marco **solo** si el mensaje invoca `/duoc`. Sin ese comando, no leer ni aplicar este skill.

## Para qué existe este workspace

Este workspace está hecho para usar al agente en el **proyecto de título**. No va orientado a entregas a cliente.

Casa de estudios: **DUOC**. Equipo: **Carlos Vallejos** y **Felipe Cuevas**.

Bajo `/duoc`, las reglas, skills y tableros de operación con el cliente Almahue no gobiernan la tarea. La realidad del código y de las transcripciones puede consultarse para que la planificación sea fiel. El destinatario de lo que se escribe es la entrega académica.

## No tocar Almahue

No crear, editar ni borrar nada dentro de `E:\source\repos\Almahue\`. Eso incluye las carpetas que ya existen (`ERP`, `docs`, `tools`, `.cursor` y el resto).

Tampoco crear, editar ni borrar nada en `G:\Mi unidad\ERP ALMHAUE\Sesiones` ni en el resto de `G:\Mi unidad\ERP ALMHAUE\`. Ahí están la mayoría de las transcripciones. Solo se leen.

Se puede leer (código, transcripciones, `tools/.env`) para que la evidencia sea fiel. No se reescribe.

La única excepción es este archivo, `.cursor/skills/duoc/SKILL.md`, y solo cuando el usuario pida actualizar `/duoc`.

## Dónde se escribe

| Qué | Dónde |
|---|---|
| Documentación, respaldos de Trello y evidencias de sprint | `E:\source\repos\capstone_cursor\documentacion\` |
| Evidencias ya armadas del APT | `E:\source\repos\capstone_cursor\Fase 1\` (y Fase 2/3 si el usuario lo pide) |
| Repo oficial del grupo | `E:\source\repos\Capstone_grupo_7` |

`Capstone_grupo_7` no se modifica salvo que el usuario lo diga de forma explícita en ese mensaje.

Al redactar en `capstone_cursor`, seguir la skill `escritura-humana` de ese repo (tono de alumno, sin raya larga).

La documentacion de entrega (sprint, Fase 2 y lo que complemente evidencias ya hechas) se construye en **Word** (`.docx`). El markdown de trabajo en `documentacion/` no reemplaza ese Word.

## Trello

El tablero de `/duoc` es distinto al de Almahue ERP:

https://trello.com/b/mwuark1s/erp-almahue

Todo lo que se planifique con este comando va a ese tablero. No usar el Trello de Almahue ERP.

Credenciales en `E:\source\repos\Almahue\tools\.env` (no commitear, no pegar en el chat):

| Quién comenta | Clave | Token |
|---|---|---|
| Carlos | `TRELLO_API_KEY` | `TRELLO_TOKEN` |
| Felipe | `TRELLO_API_KEY_FELIPE_CUEVAS` | `TRELLO_TOKEN_FELIPE_CUEVAS` |

Cada comentario usa la pareja clave+token de esa persona. Un token no sirve con la clave del otro.

La redaccion de los comentarios copia el tono de Carlos en el tablero Almahue ERP (`wixKcrP0`): frases cortas, "en QA" / "en desarrollo", quien lo hizo, y la reunion si la hubo ("segun lo conversado el dia ... con Lupe").

- Lo que hizo Felipe se publica con el token de Felipe, pero con esa redaccion.
- Lo de Diego, Jose, las decisiones del cliente y las de Sergio las publica Carlos.

Respaldo del tablero: `capstone_cursor/documentacion/trello/`.

## Carta Gantt y sprints reales

La carta Gantt (13/07/2026 a 21/01/2027, semanas S1-S26) es el plan. El tablero la copia: una lista por semana, la tarjeta en la semana donde empieza.

Las evidencias de sprint del profesor no copian las barras futuras. Describen lo que pasó hasta la fecha, con reuniones y código. Hoy (28/09/2026) el corte es **S12**.

Artefactos ágiles por sprint (guía `capstone_cursor/info adicional/Evidencias_Metodologicas.html`): sprint backlog y scrumboard, burndown, daily, impedimentos, review y retrospectiva. Van en `capstone_cursor/documentacion/sprints/`.

## Cómo actuar

1. Seguir las instrucciones que el usuario dé a continuación de `/duoc`.
2. No modificar carpetas ni archivos de `E:\source\repos\Almahue\`.
3. Si esas instrucciones aún no están, no inventar la carta ni escribir en Trello.
4. Las ceremonias que el profesor pide y no quedaron grabadas (daily, review, burndown narrado, retrospectiva) se pueden redactar como si el equipo las hubiera llevado. El fondo sale de los commits y de las reuniones de esa semana. No se inventa una reunion con el cliente que no este en Sesiones.
5. Cada retrospectiva lleva la seccion **No contemplado en el sprint**: trabajo real de esa semana que la carta Gantt no tenia en esas fechas. Ejemplo: en S6, GoSocket y la decision de un tercer proyecto, `billing-gateway`, intermediario entre el ERP y GoSocket.
6. Responder en español.
