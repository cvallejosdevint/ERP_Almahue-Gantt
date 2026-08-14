# Checklist reunión — Aprobación comercial (OV)

**Fecha objetivo:** próxima sesión con MJ / Agustín  
**Código:** implementado en rama actual (migraciones pendientes de `deploy` en prod)  
**Demo local:** ver [DEMO-PROPUESTA-LOCAL.md](./DEMO-PROPUESTA-LOCAL.md) (`BILLING_STUB_INLINE` + seed OV-PROP-00x).
**Propuesta base:** [04-PROPUESTA-APROBACIONES-COMERCIAL.md](../04-PROPUESTA-APROBACIONES-COMERCIAL.md)

---

## 1. Objetivo de la reunión

Validar reglas de negocio **antes** de ejecutar `prisma migrate deploy` y activar `comercialRequiereAprobacion` en piloto/producción.

**Frase guía:** *«La OV se aprueba como la OC, antes de tocar bodega; la factura solo ajusta margen.»*

**Nota D16:** no vender bajo costo (`ventaBajoCosto` = `BLOQUEAR` por defecto). El concepto «merma» de la transcripción **no aplica** al negocio de frutas; no hay excepción ni paso extra por ese motivo.

---

## 2. Checklist §13 — marcar en vivo

| # | Pregunta | Propuesta default | Decisión (Sí / No / Ajustar) | Notas / responsable |
|---|----------|-------------------|------------------------------|---------------------|
| 1 | ¿Aprueban la **OV antes de descontar stock**? | **Sí** | | |
| 2 | ¿La **factura** desde OV confirmada necesita segunda aprobación? | **No** | | |
| 3 | ¿Umbral mínimo para exigir cadena? (ej. $500.000) | A definir → `comercialAprobacionDesde` | | |
| 4 | ¿OV solo **servicio** pasa por la misma cadena? | **Sí** | | |
| 5 | ¿**Bloquear** venta bajo costo de producto (D16)? | **Sí** — sin excepciones en piloto | | Default API `BLOQUEAR` |
| 6 | ¿Montos escala Comercial = Compras u **matriz aparte**? | Matriz aparte | | |
| 7 | ¿Quiénes son los **grupos** comerciales (nombres + miembros)? | Almahue entrega borrador | | |
| 8 | ¿Piloto con aprobación **on** desde día 1 u **off** hasta organigrama? | **Off** hasta cargar grupos/escalas | | |
| 9 | ¿Emisión directa sin OV requiere cadena por monto? | **Sí** si ≥ umbral (v1.1) | | Fuera de esta migración |
| 10 | ¿Algún cliente/producto **exento** de aprobación? | Listar excepciones | | |

---

## 3. Material que debe enviar Almahue (antes de activar flag)

| # | Entregable | Formato sugerido | Estado |
|---|------------|------------------|--------|
| A | Grupos Comercial (nombres, miembros, aprobador inicial) | Tabla o Excel | ☐ |
| B | Escalas / topes CLP por aprobador | Igual que Compras | ☐ |
| C | Umbral `comercialAprobacionDesde` y decisión piloto on/off | Correo o fila en tabla §2 | ☐ |
| D | Confirmación escrita preguntas §13 | Este documento firmado / correo | ☐ |

---

## 4. Casos demo (post-migración, local)

| Caso | Qué probar | Resultado esperado |
|------|------------|-------------------|
| **A** | OV $800k, un paso | Jefe AW aprueba → AUTORIZADA → confirmar stock |
| **B** | OV $3,8M, dos pasos | Jefe + gerente, PIN cada paso |
| **C** | Jefa área solicita | Omite paso propio, escala al siguiente |
| **D** | Línea producto con precio &lt; costo | **400** — no se guarda OV (D16) |
| **E** | `comercialRequiereAprobacion = false` | BORRADOR → confirmar directo (sin regresión) |

**Rechazo:** motivo obligatorio (mín. 5 caracteres); OV vuelve a `BORRADOR` con `motivoRechazoOv` visible.

---

## 5. Configuración Admin (cuando Almahue confirme)

1. **Admin › Reglas de aprobación** → módulo **Comercial** (ya no «reservado» en código).
2. Crear **grupos** y **escalas** según entregables A y B.
3. Parámetro empresa (SQL o futura UI):  
   - `comercialRequiereAprobacion` = `true` cuando organigrama listo  
   - `comercialAprobacionDesde` = umbral acordado  
   - `ventaBajoCosto` = `BLOQUEAR` (recomendado; sin excepción merma)

---

## 6. Gate pre-migración (Devint)

No ejecutar migración ni activar flag en prod hasta:

- [ ] Filas 1–8 y 10 de §2 con decisión explícita (mínimo correo de MJ/Agustín).
- [ ] Entregables A–B recibidos o fecha acordada para cargarlos en Admin.
- [ ] Decisión piloto (fila 8): si **off**, migración puede aplicarse sin impacto operativo.

---

## 7. Post-validación

1. `npx prisma migrate deploy` en `ERP/erp_back` (incluye OV + motivo rechazo).
2. Seed / carga manual grupos Comercial en demo local.
3. QA: `almahue-qa-runner` escenarios A–E.
4. Actualizar `AGENTS.md` hueco D4 y activar flag solo en entorno acordado.

---

## 8. Registro de la reunión

| Campo | Valor |
|-------|-------|
| Fecha | |
| Asistentes | |
| Decisión global (aprobar propuesta v1) | ☐ Sí ☐ Ajustar ☐ Rechazar |
| Fecha objetivo activación piloto | |
| Responsable carga organigrama Almahue | |
| Observaciones | |
