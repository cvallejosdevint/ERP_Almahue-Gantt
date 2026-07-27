# Propuesta Trello Reunión 2 — VALIDADA (previa subida)

Patrón canónico (igual imagen *Mock — Tarifas de contratista*):

1. **No tocar** etiqueta ni comentario de **Solicitudes reunión 1**.
2. Agregar etiqueta nueva **`Solicitudes reunión 2`** (única para esta ola).
3. Agregar **comentario nuevo** titulado `Solicitudes Reunión 2` con bullets `[R2-…]`.
4. Pantallas nuevas = tarjeta Mock nueva con `MockUp` + `Solicitudes reunión 2` (+ `Fuera Gantt F1` si aplica).
5. Índice `Reunión 2 - Registro demo (23/07/2026)` + adjuntar capturas.

Confirmaciones usuario:
- Anticipos = **tarjeta aparte**
- Comentario + etiqueta nueva (sin reemplazar Reu 1)
- Nombre índice OK
- Adjuntar capturas OK

Fuentes: `reunion2-analisis-2026-07-23.md`, `00-decisiones.md`, `reunion2-registro-trello-template.md`, backup Trello labels.

---

## Etiquetas

| Etiqueta | Acción |
|---|---|
| **Solicitudes reunión 1** | No modificar / no quitar |
| **Solicitudes reunión 2** | **Crear** (discriminar mocks tocados por Reu 2) |
| **MockUp** | Solo en mocks (existentes ya la tienen; nuevas también) |
| **Fuera Gantt F1** | **Solo Reu 1** — pantallas nuevas pedidas en Reu 1 fuera del Gantt. No usarla en Reu 2. |
| **Fuera Gantt F1 · Reunión 2** | **Crear** — pantallas nuevas pedidas en Reu 2 fuera del Gantt. Así se distingue origen Reu 1 vs Reu 2. |

### Por qué separar «Fuera Gantt»

Con una sola etiqueta `Fuera Gantt F1` no se sabría si la pantalla nueva salió de la Reu 1 o de la Reu 2.  
Convención:

| Origen | Etiqueta fuera de Gantt |
|---|---|
| Reunión 1 (Tarifas, Proformas, OC, …) | `Fuera Gantt F1` *(existente — no renombrar salvo que quieran alias «· Reunión 1»)* |
| Reunión 2 (Ingreso diario, Asociación, Cartola, Anticipos) | `Fuera Gantt F1 · Reunión 2` *(nueva)* |

Opcional más adelante: renombrar la actual a `Fuera Gantt F1 · Reunión 1` para simetría (no obligatorio; el nombre corto ya identifica Reu 1 por uso histórico).

---

## A) Tarjeta índice (1)

| Campo | Valor |
|---|---|
| Nombre | `Reunión 2 - Registro demo (23/07/2026)` |
| Lista | En QA Almahue |
| Etiqueta | `Solicitudes reunión 2` |
| Desc | `reunion2-registro-trello-template.md` (con links) |
| Adjuntos | Las 20 capturas de `pantallas-legacy/reunion2/` |

---

## B) Mocks EXISTENTES afectados — solo comentario + etiqueta

**Regla:** conservar `Solicitudes reunión 1` + su comentario. Añadir `Solicitudes reunión 2` + comentario nuevo.

### B1. Mock — Tarifas de contratista  
**¿Requerimiento nuevo?** Parcial — **refina** C-03 (Reu 1) con dolor confirmado Reu 2.

```
Solicitudes Reunión 2

• [R2-C02] Precio editable en control/ingreso diario (no atar siempre al tarifario rígido).
• [R2-C03] Actividades filtradas por labor seleccionada (hoy salen todas).
• Bug legacy confirmado: al agregar labor en mismo CC se borran tarifas; refresh manual.
• Ref: captura 01, 02 · DEC-11 (UX AgroSmart).
```

### B2. Mock — Proformas y facturas (contratistas)  
**¿Nuevo?** Sí en regla de negocio — PEND-02 pasa a **REQ** (N:1 + multi-mes). Reu 1 pedía 1:1; Reu 2 lo corrige.

```
Solicitudes Reunión 2

• [R2-C05] Permitir N proformas → 1 factura (hoy AgroSoft no asocia 2 proformas).
• [R2-C05] Periodo flexible / multi-mes (dejar de forzar 1 proforma = 1 mes calendario).
• [PEND-02 → REQ] Actualiza alcance vs comentario Reunión 1 (1:1).
• Ref: captura 03, 04 · DEC-11.
```

### B3. Mock — Traspaso contable y cierre de mes  
**¿Nuevo?** Refina C-07 (efecto contable confirmado en demo).

```
Solicitudes Reunión 2

• [R2-C06] Cierre de mes: asiento facturas por recibir contratistas vs costo MO contratada (suma proformas del periodo).
• Confirmar tasas CLP/USD/CNY/EUR al traspasar.
• Ref: demo Rodrigo + DEC-11 (contabilidad sigue modelo AgroSoft).
```

### B4. Mock — Libro comercial  
**¿Nuevo?** Sí — módulo Ventas no tenía solicitudes Reu 1 de este tipo.

```
Solicitudes Reunión 2

• [R2-V01] Al reversar, reutilizar datos del documento para el nuevo folio (reversado + reversador + nuevo).
• [R2-V02] Confirmación antes de grabar si viene de una reversa.
• [R2-V03] Quitar utilidad de «Guardar» (no sale en reportes ni contabilidad); solo «Grabar y contabilizar».
• [R2-V04] Búsqueda de clientes robusta/rápida.
• Ref: captura 08, 09.
```

### B5. Mock — Conciliación bancaria  
**¿Nuevo?** Sí — discovery Tesorería Reu 2 (Gantt DEF-TES era ago; ahora hay REQ mock).

```
Solicitudes Reunión 2

• [R2-T02] Conciliación diaria/semanal tomando cartola como fuente oficial.
• [R2-T03] Link directo al asiento contable cuando hay diferencia.
• [R2-T04] Reversa selectiva de movimientos (no solo mes completo).
• Mejorar búsqueda/eliminación de cartolas históricas.
• Ref: captura 11, 12, 13 · ver también Mock Carga cartola (nuevo).
```

### B6. Mock — Pagos  
**¿Nuevo?** Sí (TC bidireccional); anticipos van a tarjeta aparte.

```
Solicitudes Reunión 2

• [R2-T06] Diferencia de tipo de cambio en ambos sentidos (pago CLP/factura USD y viceversa).
• Calce pago–factura con validación (no grabar sin seleccionar documentos).
• Anticipos productores → ver Mock — Anticipos productores (tarjeta nueva).
• Ref: captura 10, 15.
```

### B7. Mock — Roles y permisos  
**¿Nuevo?** Refina DEC-04 con roles reales mostrados.

```
Solicitudes Reunión 2

• [R2-R01] Seed roles: Digitador contratistas / Analista / Administrador.
• [R2-R02] UI permisos: checks lectura/escritura por pantalla (no solo strings).
• [R2-R03] Digitador: solo procesos diarios del módulo + empresas visibles; Analista: diarios + informes, sin parametrización ni cierre.
• Ref: captura 17, 20 · DEC-13.
```

### B8. Mock — Monedas  
**¿Nuevo?** Sí (sync BC desde catálogo).

```
Solicitudes Reunión 2

• [R2-K01] Botón/config «traer Banco Central»; automático o manual + hora.
• Diferenciar indicadores del sistema vs datos actuales BC.
• Ref: captura 16 · DEC-06 / DEC-05.
```

### B9. Mock — Indicadores Banco Central  
**¿Nuevo?** Complemento de B8.

```
Solicitudes Reunión 2

• [R2-K01] Vista de indicadores vigentes + acción actualizar / última sync.
• Coordinar con Mock — Monedas (misma solicitud R2-K01).
• Ref: captura 16.
```

### B10. Mock — Centros de costo  
**¿Nuevo?** Parcial — campo contacto + seed Mario (PEND-06).

```
Solicitudes Reunión 2

• [R2-K02] Campo contacto/encargado del CC (opcional).
• [PEND-06] Seed con lista actualizada que enviará Mario.
• Ref: captura 18.
```

### B11. Mock — Facturación electrónica (GoSocket)  
**¿Nuevo?** Decisión de timing (DEC-14), no pantalla nueva.

```
Solicitudes Reunión 2

• [R2-G01 / DEC-14] Go-live DTE cliente ~01/09 independiente del ERP AlmaWeb.
• Integración libro compras ERP↔GoSocket puede diferirse; no bloquea facturación electrónica.
• Sergio coordina reunión soporte vs avance ERP básico.
```

### B12. Mock — Bodegas *(solo comentario; sin etiqueta obligatoria si no hay mock de niveles)*  
**¿Nuevo?** Cierre PEND-03 → OUT.

```
Solicitudes Reunión 2

• [DEC-12] Niveles de almacenamiento OUT v1 (no parametrizados / no usados).
• No construir pantalla de niveles. PEND-03 cerrado.
```

### B13. Mock — Registro de compra (factura) *(comentario)*  
**¿Nuevo?** Afina PEND-01.

```
Solicitudes Reunión 2

• [PEND-01] Cliente confirmó alerta OC exento vs factura afecta. Afinar casos mixtos/combustible en mock.
• No cambia anti-cruzado P-08 de Reunión 1.
```

---

## C) REQUERIMIENTOS / PANTALLAS NUEVAS (tarjeta Mock nueva)

Etiquetas: **`MockUp` + `Solicitudes reunión 2` + `Fuera Gantt F1 · Reunión 2`**.  
(No usar `Fuera Gantt F1` a secas — esa queda para Reu 1.)  
Lista: En desarrollo.

| # | Nombre | Códigos | ¿Por qué es nuevo? | Capturas a adjuntar |
|---|---|---|---|---|
| N1 | Mock — Ingreso diario labores (contratistas) | R2-C01, R2-C02 | No existía; Reu 1 solo tarifas/proforma. DEC-11 AgroSmart. | 06, 07 |
| N2 | Mock — Asociación labores a proforma/factura | R2-C04 | Flujo multi-select/calce no estaba en mocks. | 05 |
| N3 | Mock — Carga cartola bancaria | R2-T01 | Solo había Conciliación genérica; falta carga Excel/PDF. PEND-05. | 11 |
| N4 | Mock — Anticipos productores | R2-T05 | Confirmado tarjeta aparte; calce parcial sin traspaso sucio. | 14 |

### Texto descripción tipo (N1) — estilo Fuera Gantt Reu 2

```
**Fuera Gantt F1 · Reunión 2** · R2-C01 / DEC-11

Pantalla crítica: ingreso diario de labores de contratista (empresa, fecha, CC/cuartel, labor, jornada/trato, precio editable).
Inspirada en UX AgroSmart. No clonar tarifario→contrato→producción de AgroSoft.

Captura legacy reunión:
```

### Comentario inicial en N1

```
Solicitudes Reunión 2

• [R2-C01] Ingreso múltiple / diario de mano de obra contratista.
• [R2-C02] Precio editable según situación del día.
• [DEC-11] Referencia AgroSmart; contabilidad de cierre sigue modelo AgroSoft.
```

*(N2–N4 mismo patrón con sus códigos.)*

---

## D) Matriz: ¿existe en origen? ¿es nuevo?

| ID | Tema | En docs origen | En Trello hoy | Acción Trello |
|---|---|---|---|---|
| R2-C01 | Ingreso diario labores | Sí (análisis §4.1, DEC-11) | No | **Nueva tarjeta** |
| R2-C02 | Precio editable diario | Sí | Tarifas (parcial) | Comentario + etiqueta en Tarifas + N1 |
| R2-C03 | Filtro actividad×labor | Sí | Tarifas | Comentario + etiqueta Tarifas |
| R2-C04 | Asociación masiva | Sí | No | **Nueva tarjeta** |
| R2-C05 | N:1 + multi-mes | Sí (PEND-02→REQ) | Proformas (decía 1:1) | Comentario + etiqueta Proformas |
| R2-C06 | Asiento cierre | Sí | Traspaso | Comentario + etiqueta Traspaso |
| R2-V01…V04 | Ventas post-reversa | Sí §4.2 | Libro comercial | Comentario + etiqueta Libro |
| R2-T01 | Cartola PDF/Excel | Sí §4.3, PEND-05 | No | **Nueva tarjeta** |
| R2-T02…T04 | Conciliación avanzada | Sí | Conciliación | Comentario + etiqueta |
| R2-T05 | Anticipos | Sí | No / Pagos genérico | **Nueva tarjeta** |
| R2-T06 | TC bidireccional | Sí | Pagos | Comentario + etiqueta Pagos |
| R2-R01…R03 | Roles | Sí DEC-13 | Roles | Comentario + etiqueta |
| R2-K01 | Sync BC | Sí | Monedas + Indicadores | Comentario + etiqueta (ambas) |
| R2-K02 | CC + Mario | Sí PEND-06 | Centros de costo | Comentario + etiqueta |
| R2-G01 | GoSocket timing | Sí DEC-14 | GoSocket | Comentario + etiqueta |
| DEC-12 | Niveles OUT | Sí | Bodegas | Solo comentario |
| PEND-01 | Afecto afinar | Sí | Registro compra | Solo comentario |

---

## E) Totales a publicar

| Acción | Cantidad |
|---|---|
| Crear etiqueta `Solicitudes reunión 2` | 1 |
| Crear etiqueta `Fuera Gantt F1 · Reunión 2` | 1 |
| Crear índice + 20 adjuntos | 1 |
| Crear mocks nuevos (N1–N4) | 4 |
| Pegar etiqueta + comentario en mocks existentes | 11 (B1–B11) |
| Solo comentario (Bodegas, Registro compra) | 2 |
| **No borrar / no editar** comentarios ni etiqueta Reu 1 | — |

---

## F) Checklist pre-subida

- [x] Anticipos = tarjeta aparte (N4)
- [x] Etiqueta única `Solicitudes reunión 2` (no reemplaza Reu 1)
- [x] Comentario nuevo por mock afectado
- [x] Índice nombre `Reunión 2 - Registro demo (23/07/2026)`
- [x] Capturas a adjuntar (índice 20; nuevas N1–N4 las suyas)
- [x] Validado contra análisis Reu 2 + DEC-11…15 + PEND
- [x] Aprobación usuario (índice + comentarios/etiquetas; **sin** N1–N4 por ahora)
- [x] Subida Trello 23/07/2026 → https://trello.com/c/DAITP1gF

Alcance subido: etiqueta `Solicitudes reunión 2` + índice + 20 adjuntos + comentarios/etiquetas en existentes.  

**Completado 23/07/2026 (pantallas nuevas):**
- Etiqueta `Fuera Gantt F1 · Reunión 2`
- N1 https://trello.com/c/kD5faLBC
- N2 https://trello.com/c/TbhPZfMp
- N3 https://trello.com/c/8wHl30Q3
- N4 https://trello.com/c/iMCx4eXp
- Índice actualizado: https://trello.com/c/DAITP1gF
- Script: `crear-pantallas-nuevas-reunion2-trello.py`
