> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`reunion6-minuta-2026-08-06.md`](reunion6-minuta-2026-08-06.md). Motivo: DEC Reu1–2; no cubre D11/OV/grupos.

# 00 — Decisiones estratégicas (DEC)

## Meta

Construir el nuevo ERP como **Agrosoft 3.0**: mismos módulos operativos que usan hoy, con validaciones y UX corregidas.

## Decisiones confirmadas en reunión

| ID | Decisión | Evidencia |
|---|---|---|
| DEC-01 | **NO** implementar módulo Mano de Obra (usan Book). Actividad/Labor se parametriza en **Contratistas**. | Transcript |
| DEC-02 | **Eliminar** flujo de Solicitud de Compra. Ir directo a Orden de Compra. | ~35:56 |
| DEC-03 | Aislamiento estricto por **empresa activa** (CC, bodegas, datos). | 11:29, bodegas |
| DEC-04 | Perfil **intermedio** (entre Digitador y Admin) es requisito; cambiar un perfil no debe alterar permisos de otros usuarios. | 13:11–14:22 |
| DEC-05 | Monedas foco reportería: **peso, dólar, yuan, euro**. UF/UTM/IPC no se usan. | 01:52 |
| DEC-06 | Indicadores financieros desde **Banco Central** (~09:00); rellenar domingos/feriados. | 01:51–01:54 |
| DEC-07 | Compras administrativas = **servicios**; materiales/agroquímicos = **Insumos/Bodega**. Maestro preferido en Insumos. | Transcript |
| DEC-08 | Contexto usuarios: **15 usuarios**; a veces 2 personas comparten login → riesgo de empresa activa incorrecta. | 01:39–02:45 |
| DEC-09 | Existe **AlmaWeb** + Power BI (Mario / control de gestión). Gestión Agrosoft no se usa. | 01:46–01:48 |
| DEC-10 | Maquinaria: mencionada (mantenciones/desgaste/prorrateo) pero **no se usa en ningún rubro** y sin demo de pantalla → **OUT v1** hasta validar. | 01:25 |

## Decisiones confirmadas / actualizadas en Reunión 2 (23/07/2026)

| ID | Decisión | Evidencia |
|---|---|---|
| DEC-11 | UX Contratistas v1 se inspira en **AgroSmart** (ingreso diario, precio editable, asociación masiva labores→proforma/factura), no clonar el flujo engorroso de AgroSoft. Contabilidad sigue el modelo AgroSoft (cierre → facturas por recibir). | Reu 2 demo Rodrigo |
| DEC-12 | **Niveles de almacenamiento = OUT v1** (no parametrizados / no usados). | Reu 2 MJ |
| DEC-13 | Roles base: **Digitador contratistas**, **Analista** (diarios + informes, sin parametrización ni cierre), **Admin**. Permisos lectura/escritura por pantalla. | Reu 2 perfiles legacy |
| DEC-14 | GoSocket go-live cliente **~01/09** es **independiente** del ERP; integración libro compras ERP puede diferirse. | Reu 2 MJ |
| DEC-15 | Feedback de maqueta vía **Trello** (asíncrono) + reunión semanal **martes**. | Reu 2 |

## Decisiones pendientes de cliente

| ID | Tema | Estado post Reu 2 |
|---|---|---|
| PEND-01 | Afecto/Exento en OC: detalle casos mixtos + combustible. MJ indicó que ya vieron alerta afecta vs OC exento. | Parcialmente visto — cerrar regla exacta en mock |
| PEND-02 | N labores/proformas → 1 factura; periodos multi-mes. | **Confirmado como REQ** (dolor actual) — implementar en diseño |
| PEND-03 | Niveles de almacenamiento | **Cerrado → OUT (DEC-12)** |
| PEND-04 | Alcance Maquinaria / AlmaWeb / dashboards (Mario agosto) | Sigue abierto |
| PEND-05 | Entregar Excel+PDF cartola bancaria (Agustín) | Nuevo — Reu 2 |
| PEND-06 | Lista actualizada centros de costo + elementos de costo (Mario) | Nuevo — Reu 2 |

## Core técnico propio (no levantado en demo)

El CRUD de **Usuarios** en `feature/backend-core` es infraestructura del ERP nuevo (no apareció en la demo). Se mantiene. No confundir con la tarjeta #49 del resumen (eliminada del backlog de reunión).

## Captura de contexto

![Login / empresa](pantallas-legacy/01-login-empresa.png)
