# Plan de acción post Reunión 2 (23/07/2026)

Horizonte: **jue 23/07 → mar ~28/07** (primera reunión semanal) y sprint corto hasta **vie 01/08**.  
Detalle analítico: [`reunion2-analisis-2026-07-23.md`](reunion2-analisis-2026-07-23.md).

---

## Objetivo de la semana

1. Dejar el **tablero Trello** como canal oficial de feedback (capturas actualizadas Reu 2).  
2. Congelar **decisiones cerradas** (niveles OUT, roles, N proformas→factura).  
3. Re-diseñar mock **Contratistas** hacia UX AgroSmart (sin romper lo ya real).  
4. Ampliar backlog **Tesorería + Ventas** con REQ de hoy (sin implementar back aún).  
5. Coordinar **GoSocket 01/09** sin descarrilar ERP básico.

---

## Semana A — Inmediato (hoy → lunes 27/07)

| # | Acción | Dueño | Entregable | Done when |
|---|---|---|---|---|
| A1 | Commit front (demo mode + proformas + limpieza UI) | Carlos | Push `erp_front` | Repo actualizado |
| A2 | Actualizar mocks Contratistas (filtros labor→actividad, copy UX, estados proforma) | Carlos | Capturas nuevas | Subidas a Trello |
| A3 | Crear/actualizar tarjetas Trello Reu 2 (lista §6 del análisis) | Carlos | Tablero | Labels + desc + 20 capturas |
| A4 | Enviar a MJ: link Trello + nota “pantallas actualizadas” | Carlos | WhatsApp/mail lunes | MJ confirma acceso |
| A5 | Pedir a Agustín Excel+PDF cartola; a Mario lista CC/elementos | Carlos/MJ | Archivos en Drive/docs | Guardados en `fuentes/` |
| A6 | Sergio: invitación GitHub OK + conversación timing GoSocket | Sergio | Acuerdo escrito | “ERP básico primero / DTE 01/09 independiente” |
| A7 | Montar maqueta en servidor prueba (si hay capacidad) | Sergio | URL UAT | Equipo cliente puede abrir |

---

## Semana B — Martes planificación + mié–vie

| # | Acción | Dueño | Entregable |
|---|---|---|---|
| B1 | Reunión martes: plan semanal + recorrer Trello con MJ | Carlos + MJ | Acta corta / checklist |
| B2 | Spec corta **Ingreso diario labores + asociación a proforma/factura** | Carlos | Doc en `modulos/01-contratistas.md` |
| B3 | Spec corta **Tesorería Reu 2** (cartola PDF, conciliación, TC, anticipos) | Carlos/Sergio | Doc en `modulos/` o DEF-TES draft |
| B4 | Spec corta **Ventas post-reversa** | Carlos | Bullet REQ en módulo comercial |
| B5 | Seed roles: Digitador contratistas / Analista / Admin | Sergio/Carlos | Backend + front permisos |
| B6 | Backend viernes: priorizar C-07 cierre/traspaso **o** modelo ingreso diario (decidir martes) | Sergio | PR / endpoints |
| B7 | Adjuntar muestras cartola + actualizar mock conciliación | Equipo | Fixture + UI mock |

---

## Priorización producto (orden sugerido)

```
P0  Feedback Trello + capturas (confianza cliente)
P0  Roles Digitador/Analista/Admin
P1  Rediseño flujo Contratistas (AgroSmart-like) — mock primero
P1  Proformas N:1 + periodo flexible — ajustar modelo C-06
P2  Tesorería mock enriquecido (cartola PDF, conciliación)
P2  Ventas: reutilizar post-reversa (mock)
P3  C-07 cierre mes (back)
P3  GoSocket reunión soporte (sin bloquear P0–P2)
```

---

## Decisiones de alcance a aplicar YA en docs/código mock

| Decisión | Acción concreta |
|---|---|
| Niveles almacenamiento OUT | Quitar/ocultar de UI mock y Trello activo |
| N proformas → 1 factura | Cambiar copy y validaciones mock; planificar cambio API |
| Precio editable en ingreso diario | Nueva pantalla mock (no solo tarifas rígidas) |
| Guardar ventas inútil | En mock ventas: solo “Grabar y contabilizar” |
| GoSocket ERP ≠ 01/09 | No inventar dependencia en Gantt F6 para esa fecha |

---

## Alineación Gantt (recordatorio)

| Track | Qué hacemos ahora | Qué NO prometemos |
|---|---|---|
| Agrosoft ops | Discovery + mock + feedback + back incremental contratistas | ERP completo en agosto |
| Enterprise Gantt | DEF-CAT esta semana; DEF-TES/COM notes adelantadas | GoSocket ERP productivo el 01/09 |
| Cliente DTE | Acompañar traspaso Acepta→GoSocket | Libro compras ERP online en septiembre |

Detalle: sección 5 de [`reunion2-analisis-2026-07-23.md`](reunion2-analisis-2026-07-23.md).

---

## Checklist reunión martes

- [ ] MJ vio Trello y dejó ≥1 comentario de prueba  
- [ ] Agustín/Mario: estado de archivos  
- [ ] Decidir: ¿siguiente back = C-07 o ingreso diario?  
- [ ] Confirmar roles seed con MJ (nombres finales)  
- [ ] Fecha tentativa reunión soporte GoSocket (Sergio)  
- [ ] ¿Hace falta miércoles/jueves ad-hoc?

---

## Definición de “semana exitosa”

1. Cliente puede comentar en Trello con capturas actualizadas.  
2. Backlog Reu 2 está reflejado en docs + tarjetas (sin perder PEND cerrados).  
3. Hay acuerdo escrito GoSocket vs ERP básico.  
4. Hay 1 spec contratistas AgroSmart-like lista para implementar mock/back.  
5. Roles base configurados o con ticket listo para viernes.
