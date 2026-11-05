# Matriz UI - normalizacion visual ERP Almahue

Fecha: 2026-11-04. Alcance: `ERP/erp_front/src` (archivos `*Page*.tsx` / `*Pages.tsx`, excluye helpers comunes).

Referencia visual acordada en sesion:
- **Bueno (parametrizacion / ficha densa):** Plan de cuentas - modal `Detalle y edicion de cuenta` (tabs, grilla 2-3 cols ocupada, seccion de requisitos, footer ghost + primary).
- **Malo (mucho aire sin uso):** fichas tipo `Editar Ingreso` via `MockListPage` con `formColumns=3` y pocos campos visibles - tercera columna vacia, huecos grandes.

Skill operativa: `.cursor/skills/almahue-diseno/SKILL.md` (+ `reference-normalizacion.md`).

## 1. Requisitos visuales desde transcripciones (fuente primaria)

| Tema | Pedido | Evidencia | Quien / peso |
|---|---|---|---|
| Export PDF + Excel en todas las paginas | Regularizar export en todos los modulos | `transcripcion-2026-10-28-reunion.md` [02:46:11]-[02:46:18]; [58:40] "Todo siempre PDF y Excel" | Cliente operativo (sesion demo); pedido explicito |
| PDF y Excel en todos los modulos | "En todos" | `transcripcion-2026-10-22-reunion-cliente.md` [27:42]-[27:48] (Lupe pregunta; respuesta: en todos) | Cliente |
| PDF al clic de documento | Al pinchar factura/OC mostrar PDF primero; Excel tambien | 28/10 [01:06:58], [02:54:19], [02:58:44] | Demo + cliente |
| Export PDF OC | Primera hoja exportable PDF; detalle opcional | `transcripcion-2026-10-26-presencial.md` [51:44]-[53:19] | Presencial cliente |
| Filtros en grilla (RUT / razon social) | Filtros antes / en barra, no arriba sueltos | 03/11 [12:17]-[12:43] | Sesion cliente |
| Estados vs contabilizacion | Dos columnas o dos badges | 03/11 [01:28:08]-[01:30:54] | Cliente |
| Modal detalle nuevo | No expandir el modal actual en zigzag; abrir modal propio | 03/11 [01:19:38]-[01:19:52] | Cliente |
| Color estado (naranja > verde) | Cuadrito de estado coherente | 03/11 [18:16]-[18:26] | Cliente |
| Comprobante / imprimir | Misma visualizacion + marca de linea editada | 03/11 PM [02:18:50] | Cliente |
| Menu un nivel / Ventas orden | Ya en skill diseno (Reu6+) | Canonico + skill | - |

Notas: Carlos/Sergio en demos son hipotesis. Si choca con MJ/Lupe/Mario en transcripcion, gana el cliente. Reu5 no cuenta.

## 2. Categorias minimas (objetos reutilizables)

Una sola forma por categoria. Objetivo: **10 objetos**, no proliferar variantes.

| ID | Categoria | Objeto / API | Uso |
|---|---|---|---|
| C1 | Shell pagina | `PageHeader` | Titulo + migas; Export `outline` a la derecha; primario al final |
| C2 | Totales | `CollapsibleLibroSection` + `KpiStatCard` | Una fila horizontal; sin banners dentro |
| C3 | Lista | `DataTable` | Busqueda propia; filtros en `filterBarExtra`; chips vista en `toolbarExtra` |
| C4 | Modal ficha densa | `Modal` size `wide` + grilla 2/3 cols | Parametrizacion y edicion rica (ref Plan de cuentas) |
| C5 | Modal ficha corta | `Modal` + grilla 1-2 cols | Pocos campos; **no** forzar 3 cols vacias |
| C6 | Seccion formulario | bloque titulo + borde surface | Ej. "REQUISITOS DE IMPUTACION" |
| C7 | Estado | `Badge` | Centrado; sin pastillas emerald/amber custom |
| C8 | Acciones fila | `RowActions` + `RowActionIcons` | Una columna; iconos distintos |
| C9 | Aviso | fila mensaje + boton | Sin cajas sky/amber/emerald |
| C10 | Origen | `RelacionadosVer` / link documento | Columna Origen; no repetir en acciones |

Componentes a crear o endurecer en la normalizacion (fase siguiente):
- `FormSection` (C6)
- `ModalTabs` (patron Plan de cuentas)
- `FormGrid` con `cols={1|2|3}` y regla: si campos visibles < 4, max 2 cols
- Ajuste `MockListPage`: no abrir 3 cols si el form queda aireado

## 3. Reglas de densidad (imagen buena vs mala)

| | Bueno (Plan cuentas) | Malo (Editar Ingreso / MockList aireado) |
|---|---|---|
| Columnas | 3 cols solo si hay >= 5-6 campos en la vista | 3 cols con 1 campo por fila y huecos |
| Agrupacion | Tabs + seccion de requisitos | Lista plana de Fields |
| Footer | hint izquierda + Cancelar ghost + Guardar primary | Solo botones a la derecha OK, pero cuerpo vacio |
| Identidad | Badge codigo junto al titulo | Solo titulo generico |
| Espacio | gap-x-5 gap-y-4; celdas ocupadas | Espacio muerto en col 3 |

## 4. Resumen cuantitativo (70 archivos pagina)

| Metrica | Valor |
|---|---|
| Sin `PageHeader` | 17 |
| Sin `DataTable` | 29 |
| Con `<table>` HTML | 17 |
| Con banners color (amber/sky/emerald-50) | 19 |
| Con boton emerald custom | 13 |
| Con `DataTable` y sin mencion export | ver columna Deuda |
| Con `DataTable` y sin `RowActions` | ver columna Deuda |

Conteos = ocurrencias de patron en el archivo (no pantallas logicas unicas). Archivos `*Pages.tsx` agrupan varias rutas.

## 5. Matriz por archivo

Columnas: PH=PageHeader, Tot=Totales, DT=DataTable, Mod=Modal, HTML=table, Bd=Badge, RA=RowActions, Ban=BannerColor, Btn=BtnCustom, Fld=Field, Exp=Export menciones.

| Archivo | PH | Tot | DT | Mod | HTML | Bd | RA | Ban | Btn | Fld | Exp | Categorias | Deuda |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `src/features/activo-fijo/ActivoFijoPages.tsx` | 5 | 26 | 5 | 1 | 0 | 2 | 0 | 0 | 0 | 4 | 4 | Shell, Totales, Lista-DT, Modal, Badge, Export?, Form | sin RowActions |
| `src/features/activo-fijo/ParametrizacionActivoFijoPage.tsx` | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | Shell, Badge, Form | - |
| `src/features/admin/AdministradoresModuloPage.tsx` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Shell | - |
| `src/features/admin/ConfiguracionSmtpPage.tsx` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | Shell, Form | - |
| `src/features/admin/EmpresasPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Otros | sin PageHeader |
| `src/features/admin/PlantillaDocumentosPage.tsx` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 2 | Shell, Export?, Form | - |
| `src/features/admin/RolesPage.tsx` | 3 | 0 | 3 | 2 | 0 | 0 | 3 | 0 | 0 | 3 | 0 | Shell, Lista-DT, Modal, RowActions, Form | sin export aparente |
| `src/features/admin/UsuariosPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | BannerColor | sin PageHeader; banner color |
| `src/features/admin/WorkflowAprobacionesPage.tsx` | 3 | 0 | 5 | 6 | 0 | 0 | 0 | 2 | 0 | 24 | 1 | Shell, Lista-DT, Modal, BannerColor, Export?, Form | banner color; sin RowActions |
| `src/features/auth/LoginPage.tsx` | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | Modal, Form | sin PageHeader |
| `src/features/catalogos/AreasNegocioPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | Export? | sin PageHeader |
| `src/features/catalogos/BancosPage.tsx` | 3 | 0 | 3 | 1 | 0 | 0 | 3 | 0 | 0 | 8 | 0 | Shell, Lista-DT, Modal, RowActions, Form | sin export aparente |
| `src/features/catalogos/CatalogosPages.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 19 | Export? | sin PageHeader |
| `src/features/catalogos/CodigosFinancierosPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | Export? | sin PageHeader |
| `src/features/catalogos/ConceptosFlujoPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | Export? | sin PageHeader |
| `src/features/catalogos/FichaProveedoresPage.tsx` | 3 | 0 | 3 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 7 | Shell, Lista-DT, Badge, RowActions, Export? | - |
| `src/features/catalogos/ProductoresPage.tsx` | 3 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | Shell, Lista-DT, RowActions | sin export aparente |
| `src/features/comercial/ComercialPages.tsx` | 3 | 0 | 3 | 6 | 4 | 0 | 3 | 3 | 0 | 4 | 6 | Shell, Lista-DT, Lista-HTML, Modal, RowActions, BannerColor, Export?, Form | banner color |
| `src/features/comercial/ComexImportPage.tsx` | 4 | 11 | 0 | 1 | 1 | 4 | 0 | 2 | 1 | 3 | 5 | Shell, Totales, Lista-HTML, Modal, Badge, BannerColor, BtnCustom, Export?, Form | HTML table; banner color; btn emerald |
| `src/features/comercial/EmitirDocumentoPage.tsx` | 4 | 9 | 0 | 1 | 3 | 0 | 0 | 1 | 0 | 48 | 1 | Shell, Totales, Lista-HTML, Modal, BannerColor, Export?, Form | HTML table; banner color |
| `src/features/comercial/GuiasDespachoPage.tsx` | 3 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | Shell, Lista-DT, RowActions | sin export aparente |
| `src/features/comercial/OrdenVentaPage.tsx` | 3 | 10 | 3 | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 1 | Shell, Totales, Lista-DT, RowActions, BannerColor, BtnCustom, Export? | banner color; btn emerald |
| `src/features/compras/ComprasPages.tsx` | 5 | 10 | 5 | 8 | 4 | 33 | 5 | 10 | 0 | 4 | 6 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, RowActions, BannerColor, Export?, Form | banner color |
| `src/features/compras/notas-cobro/NotasCobroPage.tsx` | 3 | 6 | 3 | 5 | 4 | 8 | 0 | 5 | 11 | 0 | 20 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, BannerColor, BtnCustom, Export? | banner color; btn emerald; sin RowActions |
| `src/features/compras/OrdenCompraWizardPage.tsx` | 3 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 23 | 1 | Shell, Modal, Badge, Export?, Form | - |
| `src/features/contabilidad/AsientosPage.tsx` | 3 | 8 | 3 | 7 | 2 | 0 | 0 | 0 | 0 | 10 | 12 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Export?, Form | sin RowActions |
| `src/features/contabilidad/AuditoriaContabilidadPage.tsx` | 3 | 4 | 3 | 1 | 0 | 4 | 0 | 2 | 1 | 0 | 0 | Shell, Totales, Lista-DT, Modal, Badge, BannerColor, BtnCustom | banner color; btn emerald; sin export aparente; sin RowActions |
| `src/features/contabilidad/Balance8ColumnasPage.tsx` | 3 | 11 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | Shell, Totales, Lista-DT, Export? | sin RowActions |
| `src/features/contabilidad/CentralizacionMasivaPage.tsx` | 3 | 0 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 0 | Shell, Lista-DT, Badge, Form | sin export aparente; sin RowActions |
| `src/features/contabilidad/ContabilidadPages.tsx` | 4 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 15 | Shell, Badge, BannerColor, Export? | banner color |
| `src/features/contabilidad/EstadosFinancierosPage.tsx` | 3 | 12 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | Shell, Totales, Lista-DT, Export? | sin RowActions |
| `src/features/contabilidad/LibroDiarioMayorPages.tsx` | 4 | 16 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | Shell, Totales, Lista-DT, Export? | sin RowActions |
| `src/features/contabilidad/PeriodosContablesPage.tsx` | 3 | 0 | 3 | 4 | 0 | 3 | 0 | 2 | 1 | 2 | 0 | Shell, Lista-DT, Modal, Badge, BannerColor, BtnCustom, Form | banner color; btn emerald; sin export aparente; sin RowActions |
| `src/features/contabilidad/PlanCuentasPage.tsx` | 0 | 0 | 0 | 5 | 2 | 2 | 0 | 4 | 1 | 8 | 35 | Lista-HTML, Modal, Badge, BannerColor, BtnCustom, Export?, Form | sin PageHeader; HTML table; banner color; btn emerald |
| `src/features/contabilidad/SolicitudesReversaPage.tsx` | 3 | 10 | 3 | 3 | 0 | 12 | 3 | 0 | 0 | 6 | 2 | Shell, Totales, Lista-DT, Modal, Badge, RowActions, Export?, Form | - |
| `src/features/contratistas/AprobacionesContratistasPage.tsx` | 3 | 0 | 4 | 2 | 1 | 2 | 3 | 1 | 1 | 8 | 0 | Shell, Lista-DT, Lista-HTML, Modal, Badge, RowActions, BannerColor, BtnCustom, Form | banner color; btn emerald; sin export aparente |
| `src/features/contratistas/AsociacionLaboresPage.tsx` | 3 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | Shell, Lista-DT, Badge, Form | sin export aparente; sin RowActions |
| `src/features/contratistas/AuditoriaContratistasPage.tsx` | 3 | 4 | 3 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | Shell, Totales, Lista-DT, Modal, Badge | sin export aparente; sin RowActions |
| `src/features/contratistas/ContratistasPages.tsx` | 3 | 16 | 6 | 9 | 2 | 9 | 0 | 9 | 15 | 15 | 10 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, BannerColor, BtnCustom, Export?, Form | banner color; btn emerald; sin RowActions |
| `src/features/contratistas/EnvioOperativoContratistasPage.tsx` | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | Shell, Lista-DT, Form | sin export aparente; sin RowActions |
| `src/features/contratistas/IngresoLaborDiarioMasivoPage.tsx` | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | Shell, Lista-HTML, Form | HTML table |
| `src/features/contratistas/IngresoLaborDiarioPage.tsx` | 0 | 6 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | Totales, Badge, RowActions | sin PageHeader |
| `src/features/contratistas/ParametrizacionContratistasPage.tsx` | 3 | 0 | 3 | 0 | 0 | 5 | 0 | 0 | 0 | 4 | 25 | Shell, Lista-DT, Badge, Export?, Form | sin RowActions |
| `src/features/contratistas/ProformasContratistaNivel1Page.tsx` | 0 | 6 | 0 | 5 | 1 | 4 | 1 | 0 | 0 | 3 | 4 | Totales, Lista-HTML, Modal, Badge, RowActions, Export?, Form | sin PageHeader; HTML table |
| `src/features/contratistas/ReporteContratistasIngresoPage.tsx` | 3 | 10 | 3 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, Export? | sin RowActions |
| `src/features/contratistas/TarifasContratistaNivel1Page.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Otros | sin PageHeader |
| `src/features/dashboard/DashboardPage.tsx` | 0 | 0 | 4 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | Lista-DT, Badge | sin PageHeader; sin export aparente; sin RowActions |
| `src/features/dashboard/MisSolicitudesPage.tsx` | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | Shell, Badge | - |
| `src/features/dashboard/NotificacionesPage.tsx` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | Shell, Form | - |
| `src/features/insumos/AuditoriaInsumosPage.tsx` | 3 | 4 | 3 | 1 | 0 | 4 | 0 | 2 | 1 | 0 | 0 | Shell, Totales, Lista-DT, Modal, Badge, BannerColor, BtnCustom | banner color; btn emerald; sin export aparente; sin RowActions |
| `src/features/insumos/CierreBodegaPage.tsx` | 3 | 19 | 4 | 1 | 2 | 10 | 0 | 0 | 0 | 8 | 0 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, Form | sin export aparente; sin RowActions |
| `src/features/insumos/GuiasInsumosRecibidasPage.tsx` | 4 | 16 | 4 | 11 | 2 | 2 | 3 | 0 | 0 | 33 | 14 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, RowActions, Export?, Form | - |
| `src/features/insumos/InsumosPages.tsx` | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | Modal, Badge, Export? | sin PageHeader |
| `src/features/insumos/OrdenesAplicacionPage.tsx` | 3 | 10 | 5 | 4 | 1 | 1 | 3 | 0 | 0 | 18 | 10 | Shell, Totales, Lista-DT, Lista-HTML, Modal, Badge, RowActions, Export?, Form | - |
| `src/features/insumos/OrdenesInsumosPage.tsx` | 3 | 0 | 3 | 2 | 0 | 4 | 0 | 0 | 0 | 2 | 2 | Shell, Lista-DT, Modal, Badge, Export?, Form | sin RowActions |
| `src/features/insumos/StockMantenedorPage.tsx` | 3 | 16 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Shell, Totales, Lista-DT | sin export aparente; sin RowActions |
| `src/features/perfil/PerfilPage.tsx` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | Shell, Form | - |
| `src/features/presupuestos/PresupuestosPage.tsx` | 3 | 10 | 4 | 1 | 0 | 4 | 0 | 2 | 1 | 0 | 6 | Shell, Totales, Lista-DT, Modal, Badge, BannerColor, BtnCustom, Export? | banner color; btn emerald; sin RowActions |
| `src/features/reporteria/ReporteriaPages.tsx` | 8 | 24 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | Shell, Totales, Lista-DT, Form | sin export aparente; sin RowActions |
| `src/features/reportes/ReportesEjecutivoPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Otros | sin PageHeader |
| `src/features/tesoreria/AnticiposProductoresPage.tsx` | 0 | 0 | 0 | 1 | 0 | 4 | 0 | 0 | 0 | 2 | 0 | Modal, Badge, Form | sin PageHeader |
| `src/features/tesoreria/CartolaBancariaPage.tsx` | 3 | 8 | 0 | 2 | 1 | 15 | 0 | 3 | 1 | 11 | 9 | Shell, Totales, Lista-HTML, Modal, Badge, BannerColor, BtnCustom, Export?, Form | HTML table; banner color; btn emerald |
| `src/features/tesoreria/CompromisosAnticiposPage.tsx` | 3 | 11 | 3 | 5 | 0 | 11 | 3 | 0 | 0 | 17 | 2 | Shell, Totales, Lista-DT, Modal, Badge, RowActions, Export?, Form | - |
| `src/features/tesoreria/CuentasCorrientesPage.tsx` | 3 | 0 | 3 | 2 | 1 | 2 | 0 | 0 | 0 | 0 | 5 | Shell, Lista-DT, Lista-HTML, Modal, Badge, Export? | sin RowActions |
| `src/features/tesoreria/FlujoCajaPage.tsx` | 3 | 4 | 3 | 2 | 0 | 4 | 0 | 0 | 0 | 9 | 4 | Shell, Totales, Lista-DT, Modal, Badge, Export?, Form | sin RowActions |
| `src/features/tesoreria/NominasAgingPage.tsx` | 3 | 4 | 3 | 2 | 0 | 6 | 0 | 0 | 0 | 0 | 6 | Shell, Totales, Lista-DT, Modal, Badge, Export? | sin RowActions |
| `src/features/tesoreria/TesoreriaPages.tsx` | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 1 | 1 | 3 | 0 | Modal, Badge, BannerColor, BtnCustom, Form | sin PageHeader; banner color; btn emerald |
| `src/features/workflow/WorkflowPage.tsx` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Otros | sin PageHeader |
| `src/pages/parametrizacion/IndicadoresBCPage.tsx` | 3 | 7 | 3 | 1 | 0 | 2 | 0 | 2 | 2 | 3 | 2 | Shell, Totales, Lista-DT, Modal, Badge, BannerColor, BtnCustom, Export?, Form | banner color; btn emerald; sin RowActions |
| `src/pages/parametrizacion/MonedasPage.tsx` | 3 | 9 | 3 | 1 | 0 | 3 | 3 | 0 | 0 | 6 | 9 | Shell, Totales, Lista-DT, Modal, Badge, RowActions, Export?, Form | - |

## 6. Prioridad de normalizacion (despues del commit de respaldo)

1. **MockListPage + formularios aireados** (Ingreso diario y demas Mock) - alinear a C5/C4.
2. **Modales de la ultima semana** ya tocados (Reversas, Compromisos, OA, Guias, Asociar OC) - segunda pasada densidad.
3. **Listas con HTML table** restantes - migrar a C3.
4. **Export PDF+Excel** faltante en listados (pedido 22/10 y 28/10).
5. **Banners color + btn emerald** - C7/C9/Button.
6. **Parametrizacion / catalogos** - fichas densas tipo Plan de cuentas.

## 7. Fuera de alcance de esta matriz

- Logica de negocio / backend.
- Ordenes de compra listado (skill diseno: fuera hasta pedido).
- Cambiar tokens CSS globales sin acuerdo.

## 8. Como regenerar conteos

Desde `ERP/erp_front`, script de inventario por regex sobre `*Page*.tsx` (PageHeader, CollapsibleLibroSection|KpiStatCard, DataTable, Modal, table, Badge, RowActions, bg-amber-50|bg-sky-50|bg-emerald-50, bg-emerald-[567], Field, enableExport|Excel|PDF).