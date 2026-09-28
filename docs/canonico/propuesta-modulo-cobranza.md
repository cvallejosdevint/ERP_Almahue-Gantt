# Propuesta — Módulo de cobranza (R4-18)

**Origen:** Reunión 4 (30/07/2026) · action item R4-18  
**Fuentes:** minuta Reu4 · transcripción `[13:57:51]`–`[14:15:41]` (y contexto aging/estado de cuenta)  
**Estado:** Documento de propuesta (sin implementación de feature completa en este sprint)  
**Validación producto:** [`ERP/qa-reu4-2026-07-31/06-MATRIZ-CUMPLIMIENTO-REU4.md`](../../../ERP/qa-reu4-2026-07-31/06-MATRIZ-CUMPLIMIENTO-REU4.md)

---

## 1. Por qué existe esta propuesta (justificación desde la reu)

### 1.1 Problema que planteó Almahue

María Jesús describe la gestión actual como **arcaica** y de muchos saltos:

> «…tengo un informe que se llama inventario balance, y ahí me salen por cliente o por proveedor el total de deuda… Entonces ahí yo veo los clientes que yo tengo pendientes y me meto al detalle a ver qué documentos son y qué antigüedad tienen, pero tengo que darme toda esa vuelta para saber.»  
> — MJ · `[13:59:31]`

Es decir: hoy el “cobrar” depende de un informe de saldos + drill-down manual, **sin** compromisos, **sin** historial de contactos y **sin** tracking de gestiones.

### 1.2 Qué ofreció Devint y qué se aceptó

Sergio propone explicitamente un módulo / capa de cobranza sobre documentos de venta, y MJ acepta:

> «¿te parece… que nosotros hagamos una propuesta para cómo hacer la cobranza de los documentos de ventas… seguir una trazabilidad… por compromiso de fecha de pago, qué usuario registró un nuevo compromiso… mandar la factura que tiene deuda por correo… y que quede un tracking completo…?»  
> — Sergio · `[14:05:20]`

> «Sí, buenísimo.» — MJ · `[14:14:30]`  
> «Ok, perfecto.» — Sergio · `[14:15:41]`

La minuta lo materializa como **R4-18 = propuesta (no código)** en el slice del próximo jueves. Por eso este documento es el entregable acordado.

### 1.3 Cómo se justifica respecto al resto del ERP (ya en curso)

La reu **no** pide reinventar saldos: pide una capa de gestión encima de piezas que ya se están alineando:

| Pieza Reu4 | Rol respecto a cobranza |
|---|---|
| Aging / nóminas (R4-17) | Detecta vencidos y permite (solo tesorería) ajustar fecha de vencimiento |
| Estado de cuenta (R4-20–22) | Vista por RUT con saldos, pendientes y link a docs/pagos |
| Conciliación / cartolas (R4-16, R4-19) | Cuando el cliente paga, el calce cierra el ciclo |
| Libro / emitir ventas | Origen de la factura que se cobra |

**Conclusión de diseño:** cobranza **lee** Estado de cuenta + Aging; **no duplica** saldos contables. El valor nuevo es operativo: compromiso → gestión → mail/nota → cumplimiento al calzar pago.

---

## 2. Objetivo de producto

1. Registrar **compromisos de pago** (fecha prometida, monto, documento, responsable).  
2. Registrar **gestiones** (llamada, mail, nota, WhatsApp) con resultado y usuario.  
3. Enviar o registrar el envío de la **factura con deuda** (fase 1: plantilla + log; SMTP cuando haya infra).  
4. Vista operativa: cartera vencida + agenda de compromisos + alertas de incumplimiento.  
5. Trazabilidad completa: quién prometió qué, cuántas veces se reprogramó, qué se envió.

---

## 3. Alcance MVP (propuesto)

| Capacidad | Incluido en MVP | Justificación desde reu |
|---|---|---|
| Compromisos sobre facturas/NC **por cobrar** | Sí | Sergio acotó «documentos de ventas» `[14:05:20]` |
| Bitácora de gestiones por cliente/documento | Sí | «tracking completo» |
| Agenda por fecha de compromiso | Sí | Ejemplo «te pago mañana» + reprogramación |
| Entrada desde Estado de cuenta / Aging | Sí | Flujo natural post-demo tesorería |
| Mail real SMTP | Fase 1b (opcional) | Pedido en reu; puede partir como “registrar envío” |
| Por pagar / cobranza a proveedores | No MVP | No fue el foco de la aceptación |
| Discador / CRM / judicial | Fuera | Fuera de alcance ERP operativo |

### Modelo de datos (borrador)

- `CompromisoCobranza`: empresaId, clienteRut, documentoRef, monto, fechaCompromiso, estado (`PENDIENTE`\|`CUMPLIDO`\|`INCUMPLIDO`\|`REPROGRAMADO`), creadoPor, createdAt  
- `GestionCobranza`: compromisoId?, clienteRut, canal (`MAIL`\|`LLAMADA`\|`NOTA`\|`WHATSAPP`), detalle, resultado, adjuntoRef?, userId, createdAt  

### UX propuesta

- **Tesorería › Cobranza** (tabs: Compromisos · Bitácora · Vencidos).  
- Acción en fila de Estado de cuenta / Aging con saldo: **Gestionar cobranza**.  
- Permisos: `tesoreria:write` (o permiso fino `cobranza:write`) para crear; lectura para consulta.  
- Al calzar pago (cartola/conciliación) → sugerir marcar compromiso **CUMPLIDO**.

---

## 4. Criterios de éxito (demo siguiente a la del 06/08)

1. Crear compromiso desde una factura con saldo en Estado de cuenta o Aging.  
2. Registrar ≥2 gestiones (nota + mail simulado).  
3. Reprogramar un compromiso incumplido y ver historial.  
4. Al registrar pago/calce, marcar compromiso cumplido (manual o semi-auto).

**Estimación:** ~1 sprint Dev (UI + API + seed) **después** de estabilizar R4-17 / R4-20–22.

---

## 5. Preguntas a cerrar (interrupciones y ambigüedades de la reu)

En la llamada hubo mute, pérdida de hilo («se me fue»), re-compartir pantalla y un «me perdí» en cuentas corrientes. Donde el audio/contexto se cortó o quedó implícito, conviene **cerrar estas definiciones** antes de construir:

### 5.1 Cobranza (R4-18) — críticas

1. **¿Solo por cobrar (ventas) o también gestión de por pagar?**  
   La propuesta verbal fue ventas; aging cubre ambos lados.  
2. **¿Quién es el dueño del módulo?** ¿Solo encargada de tesorería, o también comercial/exportaciones?  
3. **¿Mail desde la plataforma es obligatorio en MVP**, o basta bitácora + plantilla descargable?  
4. **¿Un compromiso por documento o por cliente (varios docs)?**  
5. **¿Alertas** (correo interno / inbox ERP) cuando se incumple un compromiso?  
6. **¿Integración con “inventario balance”** de Agrosoft: lo reemplazamos o lo convivimos un tiempo?

### 5.2 Aging / vencimiento — quedaron a medias

7. Sergio preguntó **trazabilidad** de edición de vencimiento (`[13:44:21]`); MJ cerró **rol** (solo tesorería edita).  
   **¿Audit log (quién/cuándo/valor anterior) entra en MVP o post?**  
8. Tras GoSocket, ¿la fecha de vencimiento “del documento” se sobrescribe o se mantiene un campo separado “fecha pacto de pago”?

### 5.3 Cotizaciones — mute en medio

9. Tras unmute (`[07:01:10]`), se dejó la página como **registro** hasta definir flujo.  
   **¿Para la próxima temporada hay aprobación formal de cotizaciones, o se mantiene el modelo actual de jefatura?**

### 5.4 Conciliación — “se me fue”

10. Confirmar: **¿la pantalla Conciliación es solo resumen de pendientes**, y el trabajo diario queda 100% en Cartolas (como dice el copy actual), o se espera matching cartola↔asiento en la misma UI?

### 5.5 Estado de cuenta — confusión inicial

11. Tras el “me perdí” (`[14:35:01]`), se acordó nombre y filtros. Confirmar con MJ:  
    - compensación cliente↔proveedor mismo RUT en una sola vista;  
    - Excel siempre; PDF “en algunos casos”.

### 5.6 GoSocket / emisión

12. Timeline: emisión portal primero vs ERP transparente.  
    **¿Hasta cuándo aceptan libro de ventas “sin reenvío PDF/XML real” (R4-08)?**

---

## 6. Dependencias y orden sugerido

```
Estado de cuenta estable (R4-20–22)
        + Aging editable (R4-17)
        + Conciliación/cartola (R4-16/19, Excel MJ)
                ↓
        MVP Cobranza (este doc)
                ↓
        Mail SMTP / plantillas / alertas inbox
```

---

## 7. Fuera de alcance (explícito)

- Scoring crediticio, cobranza judicial, discador.  
- Automatización masiva de mails sin infraestructura.  
- Reemplazo completo de reportes Agrosoft en el mismo sprint.  
- Contabilidad electrónica / certificación SII (D13).

---

## 8. Decisión pedida al cliente (próxima reu)

| # | Pregunta | Opciones sugeridas |
|---|---|---|
| A | ¿Aprobamos el MVP de la §3? | Sí / Sí con cambios / No |
| B | Mail en MVP | Solo bitácora · Registro de envío · SMTP real |
| C | Dueño del permiso | Solo tesorería · Tesorería + comercial |
| D | Audit de vencimiento | Sí MVP · Post |
| E | Alcance docs | Solo ventas · Ventas + compras |

Con A = Sí, este documento pasa a backlog de implementación post-demo del slice Reu4.
