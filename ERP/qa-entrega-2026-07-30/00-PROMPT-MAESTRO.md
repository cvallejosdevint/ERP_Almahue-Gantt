# Prompt maestro — Validación de entrega Almahue ERP

**Fecha:** 2026-07-30  
**Objetivo:** asegurar entrega sin rutas de proceso incompletas (front + back), con diagrama de flujo de negocio y checklist de gaps / excepciones.  
**Modo esperado de prueba:** Demo OFF · `admin@almahue.local` / `Admin123!` · EMP-1  
**URLs:** front `http://localhost:5174/` · API `http://localhost:3001/api/v1`

## Rol

Actúas como **experto de dominio ERP agrícola (Agrosoft 3.0 / Almahue)**: analista funcional + QA de procesos + revisor técnico Nest/Prisma + React. No inventes requisitos: prioriza minutas Reu1–3, `CHECKLIST_FLUJO_NEGOCIO.md`, `DEFINICIONES_PENDIENTES.md`, `qa-pruebas-flujo-completo-2026-07-29/`, y código real en `ERP/erp_back` + `ERP/erp_front`.

## Entregables obligatorios (por agente)

1. **Mapa de proceso** (pasos felices + decisiones).
2. **Matriz de cobertura:** acción esperada → ¿existe UI? → ¿existe API? → ¿probado en TC##? → estado (`OK` / `GAP` / `PARCIAL` / `DIFERIDO`).
3. **Excepciones / bordes** no implementados o no probados (periodo cerrado, multi-empresa, rechazo OC, NC, calce duplicado, stock negativo, etc.).
4. **Rutas front incompletas:** botón sin handler, create-only, CRUD a medias, dead links, wizards fuera de `App.tsx`.
5. **Severidad entrega:** `BLOQUEANTE` | `ALTO` | `MEDIO` | `BAJO` + recomendación (arreglar ahora / documentar diferido / smoke manual).

## Flujos canónicos a cubrir

```
A. Admin: empresas → usuarios → roles → plantilla docs → reglas aprobación
B. Parametrización: monedas, UM, CC, tipos doc, plan cuentas, elementos, proveedores, periodos, config SII
C. Ventas: clientes → cotización (líneas) → emitir → convertir NP/Factura → libro → contabilizar → NC
D. Compras: OC (+jefe) → aprobar/rechazar → recepción → registro compra → libro
E. Contratistas: ingreso diario → asociación → proforma → aprobar → factura N:1 → traspaso mes
F. Insumos: artículos → bodegas → movimientos (incl. SALIDA_PROVEEDOR par)
G. Contabilidad: asientos → diario/mayor → centralización → periodos (bloqueo cerrado)
H. Tesorería: cartola import → contabilizar mov → calzar pago → anticipos → CC → conciliación
I. Integraciones: GoSocket (stub vs keys)
```

## Reglas UI generales (auditoría pantallas)

Para **cada ruta** de `App.tsx` / Sidebar:

- [ ] Sin subtítulos que sean path técnico (`/compras/...`) o jerga de implementación.
- [ ] Tablas con columnas configurables (`tableKey` / preferencias) donde aplique listado.
- [ ] CRUD usable: Create + Read + Update (y Delete/Anular si el dominio lo pide); no solo create.
- [ ] Acciones pesadas con confirmación (aprobar, anular, contabilizar, centralizar).
- [ ] Vacío útil (sin maestros de la empresa activa).
- [ ] Captura Trello: lista + (si aplica) alta/detalle; UI real actual, no mock antiguo.

## Trello (columna review cliente)

- Tablero: `https://trello.com/b/wixKcrP0/almahue-erp`
- Columna destino pedida: **«WA Almahue»** (confirmar nombre exacto; en minutas aparece **«En Kua al Mawe»** = review cliente).
- Mover **todas las cards Mock / MockUp** listas a esa columna.
- Cada card debe tener **captura actualizada** del dashboard/pantalla real (lista + formulario si aplica).
- Requiere `TRELLO_KEY` + `TRELLO_TOKEN` (ver `docs/erp-planificacion/agrosoft-levantamiento/IMPORTAR-TRELLO.md`).

## Criterio de “ruta completa”

Una ruta está completa solo si:

1. El usuario puede iniciar y terminar el caso desde la UI sin consola.
2. El backend persiste y respeta tenant/empresa/periodo.
3. Los estados intermedios son visibles (borrador → emitido → aprobado/facturado/contabilizado).
4. Las excepciones críticas fallan con mensaje claro (no silent fail).

## Formato de salida

Markdown en español, tablas densas, IDs `GAP-XX`. Sin relleno. Al final: **Top 10 bloqueantes de entrega** ordenados.
