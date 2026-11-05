# Organigrama vs aprobaciones vs roles (WhatsApp + PDF MJ)

Fecha: 2026-11-05  
Fuentes: chat WhatsApp ERP Almahue - DevInt; `DIAGRAMA DE APROBACION OC.pdf`.

## Acuerdo WhatsApp (tres pilares)

| Pilar | Que define | Donde vive hoy | Esta tanda |
|-------|------------|----------------|------------|
| **Aprobaciones** | Solo topes / niveles por monto ($) | `/admin/aprobaciones` (grupos + escalas) | Sin cambio de motor |
| **Jefaturas** | Quien reporta a quien; acciones de jefe | Campo `Usuario.jefeId` (ya en schema) | Shell UI `/admin/organigrama` |
| **Roles** | Modulos / submodulos | `/admin/roles` | Sin cambio |

## PDF (cadena deseada a futuro)

Ruta OC: analista → **su** jefatura → gerencia de area → gerencia general, con validacion de monto en cada nivel.

Eso **no** es lo que hace el ERP hoy: la cadena sale de **grupo + escala**, no del organigrama. Un grupo con tres jefes distintos no se resuelve con el checklist actual; el PDF lo resuelve por persona.

## Fase siguiente (fuera de esta tanda)

Al emitir OC, armar pasos desde `jefeId` del solicitante + `montoMaxAprobacion` por nivel; deprecar membresia de grupo para Compras. Impacta seed holding y plan QA de aprobaciones.

## UI entregada ahora

- Menu Admin › **Organigrama (jefaturas)** (`/admin/organigrama`): arbol read-only desde `jefeId`.
- Card **Cómo funciona el organigrama**: diagrama de ruta OC (estructura base), cerrable; sin nombres de personas.
- Edicion del jefe: sigue en **Usuarios** (campo jefe).
- Avisos con links a Aprobaciones / Roles / Usuarios.
