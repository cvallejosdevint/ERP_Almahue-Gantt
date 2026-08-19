> **{deprecado}** — 2026-08-18. Conservar como archivo. No usar como fuente de verdad.
> Sustituye: [`../PLAN-PRUEBAS-APROBACIONES.md`](../PLAN-PRUEBAS-APROBACIONES.md). Motivo: QA 31/07; evidencia HEREDADO, no plan vigente.

# 09 — Auditoría BD completa (local)

Fecha: 2026-07-31T19:38:04.360Z
DB: `postgresql://almahue:***@localhost:5433/almahue?schema=erp`

## Veredicto

**PASS** — CRIT 0 · HIGH 0 · MED 10 · LOW 0 · INFO 9

## Hallazgos

| Sev | Área | Código | Detalle | N |
|-----|------|--------|---------|---|
| MED | rbac | `ROL_SIN_PANTALLAS` | Digitador contratistas (ROL-3) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | Contador (ROL-4) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | Aprobación proformas (ROL-5) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | Compras demo (ROL-6) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | Aprobador OC demo (ROL-7) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | QA Aprobador (ROL-9) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | QA Solicitante (ROL-10) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | QA Solo lectura (ROL-11) sin matriz permisosPantalla | — |
| MED | rbac | `ROL_SIN_PANTALLAS` | Analista (ROL-2) sin matriz permisosPantalla | — |
| MED | insumos | `MOV_BODEGA_NO_CATALOGO` | MovimientoBodega.bodega (texto) no matchea Bodega del tenant | 1 |
| INFO | core | `EMPRESAS` | 6 empresas (4 activas): Almahue SpA, Almahue Logística Ltda., Frutícola Sur SpA, test, Empresa Prueba QA, Empresa Intento 2 | 6 |
| INFO | rbac | `USUARIOS` | 18 users (2 inactivos). Roles: Analista, QA Solo lectura, Digitador contratistas, Contador, Administrador, Compras demo, Aprobador OC demo, Aprobación proformas, QA Aprobador, QA Solicitante | 18 |
| INFO | compras | `OC_RESUMEN` | OC=5; estados: EMITIDO:2, RECHAZADO:1, ANULADO:1, APROBADO:1 | 5 |
| INFO | contratistas | `PROFORMA_RESUMEN` | proformas=12; DEFINITIVA:6, RECHAZADA:4, FACTURADA:1, PENDIENTE_APROBACION:1 | 12 |
| INFO | comercial | `DOC_RESUMEN` | docs=18; FACTURADO:6, BORRADOR:5, EMITIDO:4, ANULADO:2, CONTABILIZADA:1 | 18 |
| INFO | contabilidad | `PERIODOS` | 2 periodos (1 abiertos, 1 cerrados) | 2 |
| INFO | tesoreria | `PAGOS_RESUMEN` | pagos=4; ACTIVO:3, PENDIENTE:1 | 4 |
| INFO | insumos | `MOV_RESUMEN` | movimientos=1 | 1 |
| INFO | notificaciones | `NOTIF_TOTAL` | total=49 | 49 |

## Volúmenes por tabla

| Tabla | Filas |
|-------|------:|
| `CuentaContable` | 792 |
| `ElementoCosto` | 208 |
| `RefreshToken` | 182 |
| `TipoDocumento` | 54 |
| `Notificacion` | 49 |
| `CentroCosto` | 37 |
| `UsuarioEmpresa` | 28 |
| `_prisma_migrations` | 25 |
| `DocumentoComercial` | 18 |
| `Usuario` | 18 |
| `Asiento` | 14 |
| `ProformaContratista` | 12 |
| `Rol` | 11 |
| `ConfigContableSii` | 10 |
| `Contratista` | 7 |
| `Empresa` | 6 |
| `UnidadMedida` | 6 |
| `AprobacionOc` | 5 |
| `LaborActividad` | 5 |
| `Moneda` | 5 |
| `OrdenCompra` | 5 |
| `Actividad` | 4 |
| `Cliente` | 4 |
| `IndicadorBc` | 4 |
| `Labor` | 4 |
| `Pago` | 4 |
| `TarifaContratista` | 4 |
| `CuentaCorrienteMovimiento` | 3 |
| `DocumentoAging` | 3 |
| `Proveedor` | 3 |
| `WorkflowConfig` | 3 |
| `IngresoLaborDiario` | 2 |
| `PeriodoContable` | 2 |
| `AnticipoProductor` | 1 |
| `Bodega` | 1 |
| `CartolaBancaria` | 1 |
| `Conciliacion` | 1 |
| `DteGoSocket` | 1 |
| `FacturaContratista` | 1 |
| `Insumo` | 1 |
| `MovimientoBodega` | 1 |
| `MovimientoCartola` | 1 |
| `PeriodoCierreContratista` | 1 |
| `Sucursal` | 1 |
| `SyncBcMeta` | 1 |
| `UiTablePreference` | 1 |
| `DteEnvio` | 0 |
| `FactorHonorario` | 0 |
| `GuiaDespacho` | 0 |
| `MovimientoCaja` | 0 |
| `MovimientoConciliacion` | 0 |
| `PasswordResetToken` | 0 |
| `Presupuesto` | 0 |
| `Prospecto` | 0 |
| `RecepcionOc` | 0 |
| `RegistroCompra` | 0 |

## Cobertura chequeada

- Core: empresas, usuarios, roles, vínculos usuario-empresa
- Workflows: aprobadores existentes/activos, módulos Compras/Contratistas
- Compras: OC↔aprobación, proveedores, recepciones, registros, afacto
- Contratistas: proformas, tarifas, ingresos
- Comercial: documentos, clientes, DTE GoSocket
- Contabilidad: periodos, plan cuentas, descuadre asientos
- Tesorería: cartolas, conciliaciones, pagos
- Insumos: movimientos vs bodega/insumo
- Parametrización: CC, elementos, monedas
- Tenant: empresaId huérfano en tablas clave
- Notificaciones: userId válido
