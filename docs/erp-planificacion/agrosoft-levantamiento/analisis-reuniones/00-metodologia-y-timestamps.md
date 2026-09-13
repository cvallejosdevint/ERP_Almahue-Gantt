# Metodología del análisis de reuniones

## Cambio de criterio (03/09/2026)

Hasta hoy el proyecto trataba las minutas `reunionN-minuta-*.md` como fuente de verdad y las reglas del repo **prohibían** leer las transcripciones de `fuentes/`. Se revirtió.

| | Antes | Ahora |
|---|---|---|
| Fuente primaria | Minuta (generada por IA) | **Transcripción verbatim** de `fuentes/` |
| Rol de la minuta | Requisito | Índice para ubicar el minuto |
| Reu1–Reu3 | No leer | **As-is de Agrosoft**, referencia funcional |

Archivos corregidos: `.cursor/rules/almahue-core.mdc`, `.cursor/rules/almahue-reuniones.mdc`, `AGENTS.md`, `.cursor/skills/almahue-erp-contexto/SKILL.md` y su `reference.md`.

**Motivo.** Las minutas IA arrastran tres vicios comprobados: borran al hablante (una propuesta del proveedor y un requisito del cliente quedan indistinguibles), convierten preguntas abiertas en hechos afirmados, y reutilizan el mismo código de decisión para cosas distintas. El caso testigo es **D14**, que en la minuta de Reu4 significa «cartola: carga Excel banco → calzar/conciliar» y en la de Reu6 «stock ventas solo positivo». QA marcó `INV-014` como SKIP usando la segunda acepción.

## Escala de timestamps: Reu1–Reu5 NO están en tiempo real

Las transcripciones de Reu1 a Reu5 llevan una marca de tiempo **inflada 10×** respecto de la grabación. Reu6 y todas las sesiones de agosto sí están en tiempo real.

**Conversión:** leer la marca como `h:mm:ss`, pasarla a segundos y **dividir por 10**.

> Formulación equivalente: si se lee la cadena como `mm:ss:cc` y se multiplica por 6, da el mismo resultado (difieren en menos de 6 segundos en todo el rango). Ambas son válidas; en estos documentos se usa la división por 10 porque es la lectura literal del archivo.

### Verificación con ancla independiente

La minuta tl;dv de Reu4 sí está en tiempo real. Su entrada «Panel SII configurable asocia cuentas por tipo documento» está en **54:08**. En la transcripción, esa frase aparece así:

> Speaker 00 `[09:00:50]`: «Entonces lo conservamos como para parametrizar.»

`09:00:50` → 32 450 s ÷ 10 = 3 245 s = **54:05**. Error de 3 segundos.

Segunda comprobación, de rango largo: la última marca de Reu4 es `[15:32:20]` → 1:33:14, y el último ítem de la minuta tl;dv está en 1:33:42.

### Tabla por archivo

| Archivo | Última marca | ¿Escala? | Duración real |
|---|---|---|---|
| `transcripcion.md` (Reu1) | `19:21:50` | ÷10 | ≈ 1 h 56 min |
| `transcripcion-reunion2.md` | `13:24:31` | ÷10 | ≈ 1 h 20 min |
| `transcripcion-reunion3.md` | `09:37:01` | ÷10 | ≈ 58 min |
| `transcripcion-reunion4.md` | `15:32:20` | ÷10 | ≈ 1 h 33 min |
| `transcripcion-reunion5.md` | `07:04:51` | ÷10 | ≈ 42 min |
| `transcripcion-reunion6.md` | `01:06:08` | **real** | ≈ 1 h 06 min |
| `transcripcion-2026-08-19-demo-interno.md` | `11:35` | **real** | ≈ 12 min |
| `transcripcion-2026-08-20-reunion-sergio.md` | `30:45` | **real** | ≈ 31 min |
| `transcripcion-2026-08-20-tarde-lupe-mario.md` | `40:58` | **real** | ≈ 41 min |
| `transcripcion-reunion-gosocket-qa.md` | `30:37` | **real** | ≈ 31 min |
| `transcripcion-2026-08-28-tesoreria-mj-lupe.md` | — | sin marcas | — |

Sin esta conversión, cruzar transcripción y minuta parece imposible y se concluye que una de las dos está corrupta. No lo están.

## Cómo citar

Formato: `[T <marca cruda> ≈ <tiempo real>]`, indicando **quién** habla y si es cliente o proveedor.

- **Cliente** (Agustín, María José / MJ, Lupe, Mario, Fran) → requisito.
- **Proveedor** (Carlos Vallejos, Sergio, equipo de desarrollo) → propuesta o hipótesis, aunque la minuta la haya redactado como decisión.

## Índice de documentos

| Documento | Alcance |
|---|---|
| `01-reu1-reu2-asis-agrosoft.md` | Reu1 (21/07) + Reu2 (23/07) — recorrido de Agrosoft |
| `02-reu3-asis-agrosoft.md` | Reu3 (28/07) — demo del ERP nuevo, as-is filtrado |
| `03-reu4.md` | Reu4 (30/07) — contabilidad, tesorería, Config SII |
| `04-reu5-reu6.md` | Reu5 (03/08) + Reu6 (06/08) — auditoría de D4/D11/D16/D17 |
| `05-agosto-19-20.md` | 19/08 demo interno, 20/08 mañana y tarde |
| `06-tesoreria-28-08-y-gosocket.md` | 28/08 tesorería + frontera con GoSocket |
| `07-triage-skip-blocked.md` | Los 40 SKIP + 1 BLOCKED de QA revisados contra transcripción |
