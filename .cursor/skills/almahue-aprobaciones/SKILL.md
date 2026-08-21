---
name: almahue-aprobaciones
description: Grupos, escalas, cadena automática, AdminConcepto, PIN, simulador y bandeja OC/proformas. Use when working on /admin/aprobaciones, grupos-aprobacion, escalas, JWT adminConceptoModulos, PIN, or approval chains.
---

# Aprobaciones Almahue (fase 2)

## Modelo

```
Grupo (quién solicita → aprobador inicial)
  → NodoEscala (tope + escalaA + logica SIMPLE|AND|OR)
    → Cadena calculada (el solicitante no elige aprobador)
```

- Un usuario: **un grupo por módulo** (hoy **solo Compras**). Excepción: **ROL-1 / `*`** (mantenedor) arma cadena con el **primer grupo activo** del módulo, sin membresía. AdminConcepto y el resto **sí** exigen grupo.
- Módulos con cadena: **solo Compras (OC)**. Ventas (OV) y Contratistas (proformas) **no** tienen bandeja ni PIN de cadena (corte 21/08, sesión Lupe/Mario).
- El Administrador **no figura** en grupos ni escalas. Puede aprobar o rechazar cualquier eslabón pendiente de OC (override implícito). El tope de la cadena es un usuario operativo.
- El Administrador **no figura** en grupos ni escalas. Puede aprobar o rechazar cualquier eslabón pendiente (override implícito). El tope de la cadena es un usuario operativo.
- PIN ligado a **designación en reglas**, no al checkbox de rol. Demo: `4821`.

## API / auth

- Endpoints: `grupos-aprobacion`, `escalas-aprobacion`, `delegaciones-aprobacion`, `aprobaciones/simular`, `aprobaciones-config/export|import`
- Acceso config: `@RequireAprobacionesConfig` + JWT `adminConceptoModulos`
- CRUD `administradores-concepto` sigue exigiendo `admin:*`
- Tras cambiar AdminConcepto: **cerrar sesión y volver a entrar**

## UI

`ERP/erp_front` → `/admin/aprobaciones` (árbol, niveles, escalas, simulador, import/export).

## Convenciones

- Fuente de verdad de aprobaciones: grupos + escalas. `workflows-admin` es pool legacy (no mezclar en UI/API nuevas).
- Tras cambiar AdminConcepto: **cerrar sesión y volver a entrar**.
- KPI `ocPorAprobar`: mis pendientes (admin: total empresa).

## Additional resources

- Escenarios S1–S6 (seed-f2) y usuarios EMP-BOOT: [reference.md](reference.md)
- Plan QA: `docs/erp-planificacion/agrosoft-levantamiento/qa/PLAN-PRUEBAS-APROBACIONES.md`
