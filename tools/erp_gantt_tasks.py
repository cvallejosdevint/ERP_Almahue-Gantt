"""Tareas Gantt ERP v3 Enterprise: alineado a PDFs Contable-Financiero + Módulo Comercial."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    id: str
    nombre: str
    tipo: str
    modulo: str
    fase: str
    duracion_dias: int
    dependencias: list[str] = field(default_factory=list)
    entregable: str = ""
    criterio_aceptacion: str = ""
    paralelizable_con: list[str] = field(default_factory=list)
    riesgo: str = "bajo"
    recurso: str = "fullstack"
    fecha_minima: date | None = None


TASKS: list[Task] = [
    # ─── F0: DEFINICIONES (PDF Enterprise) ───
    Task("INF-01", "Crear repos erp_back/erp_front (NestJS + Vite, convenciones Almahue)", "infra", "core", "F0", 2, [], "Repos listos", "build exitoso", [], "bajo", "infra"),
    Task("DEF-DOC-REV", "Revisión PDF ERP Contable-Financiero Enterprise (alcance global)", "def", "core", "F0", 2, ["INF-01"], "Matriz requisitos global", "Gaps vs plan documentados", [], "bajo", "back"),
    Task("DEF-DOC-COM", "Revisión PDF Módulo Comercial Enterprise (spec detallada)", "def", "comercial", "F0", 2, ["INF-01"], "Matriz requisitos comercial", "Entidades y APIs mapeadas", [], "bajo", "back"),
    Task("DEF-ARQ", "Def. arquitectura: Clean/Hexagonal, DDD, modular monolith, /api/v1", "def", "core", "F0", 2, ["DEF-DOC-REV"], "Doc arquitectura v2", "Alineado PDF Enterprise", [], "bajo", "back"),
    Task("DEF-ALCANCE", "Acta alcance v1: módulos IN/OUT (Prod/RRHH → fase 2)", "def", "core", "F0", 2, ["DEF-DOC-REV", "DEF-DOC-COM"], "Acta alcance firmada", "Stakeholders aprueban v1", [], "medio", "back"),
    Task("DEF-CORE", "Def. Admin & Seguridad: JWT+refresh, RBAC granular, multiempresa", "def", "core", "F0", 3, ["DEF-ARQ"], "Spec Core", "Casos auth/RBAC documentados", [], "bajo", "back"),
    Task("DEF-CAT", "Def. catálogos: monedas, UM, centros costo, tipos documento", "def", "catalogos", "F0", 2, ["DEF-CORE"], "Spec catálogos", "CRUD y relaciones definidas", [], "bajo", "back"),
    Task("DEF-SUCURSALES", "Def. sucursales/branches multiempresa + restricción por sucursal", "def", "core", "F0", 1, ["DEF-CAT"], "Spec sucursales", "Sucursal en JWT y RBAC", [], "bajo", "back"),
    Task("DEF-AUDIT", "Def. auditoría: audit_logs, integration/email logs, retención 5 años", "def", "core", "F0", 2, ["DEF-CORE"], "Spec auditoría", "Campos audit_logs definidos", [], "medio", "back"),
    Task("DEF-SEC", "Def. seguridad: rate limit, Helmet, OWASP, Redis token blacklist", "def", "core", "F0", 2, ["DEF-CORE"], "Spec seguridad", "Controles OWASP listados", [], "medio", "back"),
    Task("DEF-CONT", "Def. contabilidad: plan cuentas, asientos, periodos, reportes", "def", "contabilidad", "F0", 4, ["DEF-CAT"], "Spec contabilidad", "Reglas debe/haber definidas", [], "medio", "back"),
    Task("DEF-TES", "Def. tesorería: flujo caja, pagos, conciliación bancaria", "def", "tesoreria", "F0", 3, ["DEF-CONT"], "Spec tesorería", "Flujo conciliación definido", [], "medio", "back"),
    Task("DEF-PRES", "Def. presupuestos: elaboración, seguimiento, vs real", "def", "presupuestos", "F0", 2, ["DEF-CONT"], "Spec presupuestos", "Dimensiones presupuesto definidas", [], "medio", "back"),
    Task("DEF-INSUMOS", "Def. contratistas e insumos: proveedores, catálogo, trazabilidad", "def", "insumos", "F0", 3, ["DEF-CAT"], "Spec insumos", "Movimientos insumo definidos", [], "medio", "back"),
    Task("DEF-COM", "Def. comercial: prospectos, clientes, motor documentos, libro comercial", "def", "comercial", "F0", 4, ["DEF-DOC-COM", "DEF-CAT", "DEF-CONT"], "Spec comercial Enterprise", "Flujo prospecto→factura definido", [], "alto", "back"),
    Task("DEF-WF", "Def. motor workflow: estados, transiciones, aprobaciones por monto", "def", "workflow", "F0", 3, ["DEF-COM"], "Spec workflow", "Reglas aprobación configurables", [], "alto", "back"),
    Task("DEF-GOSOCKET", "Def. GoSocket: interfaz ElectronicInvoiceProvider, estados, resiliencia", "def", "integraciones", "F0", 2, ["DEF-COM"], "Spec GoSocket v1", "Responsabilidades ERP vs PFE claras", [], "alto", "back"),
    Task("DEF-REP", "Def. dashboard ejecutivo + reportes financieros/operativos", "def", "reportes", "F0", 2, ["DEF-CONT", "DEF-COM"], "Spec reportes/KPIs", "KPIs comercial y financiero definidos", [], "bajo", "back"),
    Task("DEF-PRISMA", "ERD + schema Prisma draft (módulos v1 Enterprise)", "def", "core", "F0", 4, ["DEF-TES", "DEF-PRES", "DEF-INSUMOS", "DEF-COM", "DEF-WF", "DEF-GOSOCKET", "DEF-REP", "DEF-ALCANCE", "DEF-SUCURSALES", "DEF-AUDIT", "DEF-SEC"], "schema.prisma draft", "Modelo validado con cliente", [], "medio", "back"),
    Task("DEF-API", "OpenAPI borrador /api/v1/ por módulo (paginación, DTOs)", "def", "core", "F0", 3, ["DEF-PRISMA"], "OpenAPI v1 draft", "Endpoints comercial + financiero", [], "bajo", "back"),

    # ─── F1: MAQUETACIÓN + FEEDBACK ───
    Task("INF-05", "Front shell: layout, sidebar, rutas mock, design system base", "front", "core", "F1", 3, ["INF-01"], "App navegable sin backend", "Rutas mock accesibles", ["INF-06"], "bajo", "front"),
    Task("INF-06", "UI base: DataTable, Modal, formularios, i18n ES", "front", "core", "F1", 2, ["INF-05"], "Componentes UI base", "DataTable con fixtures", [], "bajo", "front"),
    Task("MOCK-SHELL", "Wireframe navegación + mapa pantallas (14 módulos v1)", "mock", "core", "F1", 2, ["INF-06", "DEF-API"], "Mapa pantallas HTML", "Cliente navega módulos mock", [], "bajo", "front"),
    Task("MOCK-CORE", "Boceto: login, admin empresas/usuarios/roles RBAC", "mock", "core", "F1", 2, ["MOCK-SHELL"], "Mock Core", "Flujos login/admin clicables", [], "bajo", "front"),
    Task("MOCK-CAT", "Boceto: mantenedores catálogos maestros", "mock", "catalogos", "F1", 1, ["MOCK-SHELL"], "Mock catálogos", "CRUD simulado", [], "bajo", "front"),
    Task("MOCK-CONT", "Boceto: plan cuentas, asiento manual, diario/mayor/balance", "mock", "contabilidad", "F1", 3, ["MOCK-SHELL"], "Mock contabilidad", "Form asiento simulado", [], "bajo", "front"),
    Task("MOCK-TES", "Boceto: flujo caja, pagos, conciliación bancaria", "mock", "tesoreria", "F1", 2, ["MOCK-SHELL"], "Mock tesorería", "Conciliación simulada", [], "bajo", "front"),
    Task("MOCK-PRES", "Boceto: presupuesto, seguimiento vs real", "mock", "presupuestos", "F1", 2, ["MOCK-SHELL"], "Mock presupuestos", "Comparativo demo", [], "bajo", "front"),
    Task("MOCK-INSUMOS", "Boceto: contratistas, catálogo insumos, movimientos", "mock", "insumos", "F1", 2, ["MOCK-SHELL"], "Mock insumos", "Catálogo + movimiento demo", [], "bajo", "front"),
    Task("MOCK-COM-CLI", "Boceto: clientes, prospectos, conversión lead→cliente", "mock", "comercial", "F1", 2, ["MOCK-SHELL"], "Mock CRM comercial", "Prospecto convierte a cliente", [], "bajo", "front"),
    Task("MOCK-COM-LIBRO", "Boceto: Libro Comercial, cotizaciones, OC/NP, conversiones", "mock", "comercial", "F1", 3, ["MOCK-SHELL"], "Mock libro comercial", "Motor documentos simulado", [], "bajo", "front"),
    Task("MOCK-COM-WF", "Boceto: workflow aprobaciones por monto y tipo documento", "mock", "workflow", "F1", 2, ["MOCK-SHELL"], "Mock workflow", "Estados y aprobación visible", [], "bajo", "front"),
    Task("MOCK-COM-DASH", "Boceto: dashboard comercial KPIs (conversión, top, pendientes WF)", "mock", "comercial", "F1", 2, ["MOCK-SHELL"], "Mock dashboard comercial", "KPIs fixture interactivos", [], "bajo", "front"),
    Task("MOCK-GOSOCKET", "Boceto: panel GoSocket — estados DTE, reenvíos, XML/PDF", "mock", "integraciones", "F1", 2, ["MOCK-SHELL"], "Mock GoSocket", "Estado timbraje simulado", [], "bajo", "front"),
    Task("MOCK-REP", "Boceto: dashboard ejecutivo + reportes export", "mock", "reportes", "F1", 2, ["MOCK-SHELL"], "Mock reportes", "Gráficos fixture", [], "bajo", "front"),
    Task(
        "FB-PRES",
        "Presentación mockups v1 con cliente (walkthrough Enterprise)",
        "fb",
        "core",
        "F1",
        1,
        [
            "MOCK-CORE", "MOCK-CAT", "MOCK-CONT", "MOCK-TES", "MOCK-PRES",
            "MOCK-INSUMOS", "MOCK-COM-CLI", "MOCK-COM-LIBRO", "MOCK-COM-WF",
            "MOCK-COM-DASH", "MOCK-GOSOCKET", "MOCK-REP",
        ],
        "Acta presentación",
        "Cliente recorre módulos v1",
        [],
        "bajo",
        "front",
    ),
    Task("FB-ACTA", "Acta correcciones UX/UI por módulo (priorizada y firmada)", "fb", "core", "F1", 2, ["FB-PRES"], "Acta correcciones v1", "Lista CORR por módulo aprobada", [], "medio", "front"),

    # ─── F2: Core + Catálogos (Fase 1 doc) ───
    Task("INF-02", "Docker Compose PostgreSQL 16 + API + NGINX dev", "infra", "core", "F2", 2, ["FB-ACTA"], "docker compose up", "PG + API ok", [], "bajo", "infra"),
    Task("INF-03", "Prisma init + migración base + soft delete pattern", "back", "core", "F2", 1, ["INF-02"], "Migrate ok", "PrismaService operativo", [], "bajo", "back"),
    Task("INF-04", "Swagger /api/v1/docs + ValidationPipe + guards base", "back", "core", "F2", 1, ["INF-03"], "Swagger live", "OpenAPI /api/v1 publicado", [], "bajo", "back"),
    Task("INF-07", "CI GitHub Actions (lint, test, build) + README deploy", "infra", "core", "F2", 1, ["INF-02"], "Pipeline CI", "lint+build ok", [], "medio", "infra"),
    Task("CORE-CORR", "Aplicar correcciones mockup — Core/Auth/Admin", "front", "core", "F2", 2, ["FB-ACTA", "MOCK-CORE"], "Mock Core v2", "Acta CORR Core en UI", [], "bajo", "front"),
    Task("CORE-BACK", "Backend Core: JWT+refresh+blacklist, RBAC, multi-tenant, admin, sucursales", "back", "core", "F2", 8, ["CORE-CORR", "INF-04"], "API auth + admin", "Login JWT operativo", [], "medio", "back"),
    Task("AUDIT-BACK", "Backend auditoría: audit_logs, integration logs, email logs inmutables", "back", "core", "F2", 5, ["CORE-BACK"], "API/middleware auditoría", "Cambio genera audit_log", [], "medio", "back"),
    Task("CORE-FRONT", "Front Core: login, sesión, admin empresas/usuarios/roles", "front", "core", "F2", 5, ["CORE-BACK"], "Core productivo", "Admin contra API real", [], "bajo", "front"),
    Task("CAT-CORR", "Aplicar correcciones mockup — Catálogos", "front", "catalogos", "F2", 2, ["FB-ACTA", "MOCK-CAT"], "Mock catálogos v2", "Correcciones aplicadas", [], "bajo", "front"),
    Task("CAT-BACK", "Backend catálogos: schema, CRUD, seeds", "back", "catalogos", "F2", 5, ["CAT-CORR", "CORE-BACK"], "API catalogos/v1/*", "Seeds demo", [], "bajo", "back"),
    Task("CAT-FRONT", "Front catálogos: mantenedores + hooks cascada", "front", "catalogos", "F2", 4, ["CAT-BACK"], "Catálogos productivos", "CRUD UI real", [], "bajo", "front"),

    # ─── F3: Core Financiero (Fase 2 doc) ───
    Task("CONT-CORR", "Aplicar correcciones mockup — Contabilidad", "front", "contabilidad", "F3", 2, ["FB-ACTA", "MOCK-CONT"], "Mock contabilidad v2", "Correcciones UI aplicadas", [], "bajo", "front"),
    Task("CONT-BACK", "Backend contabilidad: plan cuentas, asientos, reportes", "back", "contabilidad", "F3", 10, ["CONT-CORR", "CAT-BACK"], "API contabilidad", "Asiento cuadrado + diario", [], "alto", "back"),
    Task("CONT-FRONT", "Front contabilidad integrado API", "front", "contabilidad", "F3", 7, ["CONT-BACK"], "Contabilidad productiva", "Asiento manual operativo", [], "medio", "front"),
    Task("TES-CORR", "Aplicar correcciones mockup — Tesorería", "front", "tesoreria", "F3", 2, ["FB-ACTA", "MOCK-TES"], "Mock tesorería v2", "Correcciones aplicadas", [], "bajo", "front"),
    Task("TES-BACK", "Backend tesorería: flujo caja, pagos, conciliación", "back", "tesoreria", "F3", 8, ["TES-CORR", "CONT-BACK"], "API tesorería", "Conciliación bancaria ok", [], "alto", "back"),
    Task("TES-FRONT", "Front tesorería integrado API", "front", "tesoreria", "F3", 5, ["TES-BACK"], "Tesorería productiva", "Match cartola operativo", [], "medio", "front"),
    Task("PRES-CORR", "Aplicar correcciones mockup — Presupuestos", "front", "presupuestos", "F3", 2, ["FB-ACTA", "MOCK-PRES"], "Mock presupuestos v2", "Correcciones aplicadas", [], "bajo", "front"),
    Task("PRES-BACK", "Backend presupuestos: elaboración y seguimiento vs real", "back", "presupuestos", "F3", 6, ["PRES-CORR", "CONT-BACK"], "API presupuestos", "Comparativo presup vs real", [], "medio", "back"),
    Task("PRES-FRONT", "Front presupuestos integrado API", "front", "presupuestos", "F3", 4, ["PRES-BACK"], "Presupuestos productivo", "Seguimiento UI ok", [], "bajo", "front"),
    Task("INS-CORR", "Aplicar correcciones mockup — Contratistas e insumos", "front", "insumos", "F3", 2, ["FB-ACTA", "MOCK-INSUMOS"], "Mock insumos v2", "Correcciones aplicadas", [], "bajo", "front"),
    Task("INS-BACK", "Backend insumos: contratistas, contratos, catálogo, movimientos", "back", "insumos", "F3", 8, ["INS-CORR", "CAT-BACK"], "API insumos", "Trazabilidad movimientos ok", [], "medio", "back"),
    Task("INS-FRONT", "Front insumos integrado API", "front", "insumos", "F3", 5, ["INS-BACK"], "Insumos productivo", "CRUD + movimientos UI", [], "bajo", "front"),

    # ─── F4: Comercial + Workflow + Spike GoSocket (Fase 3 doc) ───
    Task("WF-CORR", "Aplicar correcciones mockup — Motor workflow", "front", "workflow", "F4", 2, ["FB-ACTA", "MOCK-COM-WF"], "Mock workflow v2", "Correcciones WF aplicadas", [], "bajo", "front"),
    Task("WF-BACK", "Backend workflow: estados, transiciones, aprobaciones configurables", "back", "workflow", "F4", 8, ["WF-CORR", "CORE-BACK"], "API workflow", "Aprobación por monto operativa", [], "alto", "back"),
    Task("WF-FRONT", "Front admin workflow: config estados y aprobadores", "front", "workflow", "F4", 4, ["WF-BACK"], "Config workflow UI", "Reglas editables sin código", [], "medio", "front"),
    Task("COM-CORR", "Aplicar correcciones mockup — Módulo comercial", "front", "comercial", "F4", 3, ["FB-ACTA", "MOCK-COM-CLI", "MOCK-COM-LIBRO", "MOCK-COM-DASH"], "Mock comercial v2", "Correcciones libro/CRM aplicadas", [], "bajo", "front"),
    Task("COM-BACK", "Backend comercial: motor documentos, clientes, prospectos, import Excel, CxC", "back", "comercial", "F4", 14, ["COM-CORR", "WF-BACK", "INS-BACK", "CONT-BACK"], "API comercial/v1/*", "Flujo cotización→NP→CxC", [], "alto", "back"),
    Task("COM-NC", "Backend notas de crédito en motor documentos comerciales", "back", "comercial", "F4", 4, ["COM-BACK"], "API notas crédito", "NC emite y ajusta saldo", [], "medio", "back"),
    Task("COM-EMAIL", "Envío cotización/documento por email con PDF adjunto", "back", "comercial", "F4", 3, ["COM-BACK"], "Servicio email + email_log", "PDF enviado y registrado", [], "medio", "back"),
    Task("COM-FRONT", "Front comercial: libro, cotizaciones, NC, conversiones, dashboard KPIs", "front", "comercial", "F4", 10, ["COM-BACK", "COM-NC", "COM-EMAIL"], "Comercial productivo", "Libro comercial operativo", [], "alto", "front"),
    Task(
        "INT-GOSOCKET-SPIKE",
        "Spike GoSocket: sandbox API, ElectronicInvoiceProvider POC",
        "back",
        "integraciones",
        "F4",
        3,
        ["DEF-GOSOCKET", "COM-CORR"],
        "Doc spike + POC timbraje GoSocket",
        "POC emisión JSON→GoSocket ok",
        ["COM-BACK"],
        "alto",
        "back",
        date(2026, 9, 14),
    ),

    # ─── F5: Contabilización automática ───
    Task("INT-CONT-CORR", "Aplicar correcciones mockup — Config contabilización auto", "front", "contabilidad", "F5", 1, ["FB-ACTA"], "UI config v2", "Pantalla mapeo corregida", [], "bajo", "front"),
    Task("INT-CONT-BACK", "ContabilizacionService: eventos comercial/insumos→asientos", "back", "contabilidad", "F5", 6, ["INT-CONT-CORR", "COM-BACK", "INS-BACK", "CONT-BACK"], "Servicio contabilización", "Documento comercial genera asiento", [], "alto", "back"),
    Task("INT-CONT-FRONT", "Front config contabilización automática por tipo transacción", "front", "contabilidad", "F5", 3, ["INT-CONT-BACK"], "Config contable UI", "Mapeo editable por empresa", [], "bajo", "front"),

    # ─── F6: GoSocket producción + Integraciones (Fase 3 doc DTE) ───
    Task("INT-CORR", "Aplicar correcciones mockup — Panel GoSocket / integraciones", "front", "integraciones", "F6", 2, ["FB-ACTA", "MOCK-GOSOCKET"], "Mock GoSocket v2", "Correcciones panel DTE aplicadas", [], "bajo", "front"),
    Task("INT-BACK", "Backend GoSocket: provider, timbraje, reintentos, circuit breaker, logs", "back", "integraciones", "F6", 10, ["INT-CORR", "COM-BACK", "INT-GOSOCKET-SPIKE"], "API integraciones DTE", "DTE aceptado vía GoSocket cert", [], "alto", "back"),
    Task("INT-FRONT", "Front GoSocket: emisión desde factura, estados, reenvíos, XML/PDF", "front", "integraciones", "F6", 6, ["INT-BACK"], "Integración DTE productiva", "Estado GoSocket en UI", [], "alto", "front"),

    # ─── F7: Inteligencia + Hardening + Go-live (Fases 4-5 doc) ───
    Task("REP-CORR", "Aplicar correcciones mockup — Dashboard ejecutivo y reportes", "front", "reportes", "F7", 2, ["FB-ACTA", "MOCK-REP"], "Mock reportes v2", "Correcciones KPIs aplicadas", [], "bajo", "front"),
    Task("REP-BACK", "Backend reportes: KPIs ejecutivo/comercial, financieros, export PDF/Excel", "back", "reportes", "F7", 8, ["REP-CORR", "COM-BACK", "CONT-BACK", "TES-BACK"], "API reportes", "Dashboard KPIs JSON", [], "medio", "back"),
    Task("REP-FRONT", "Front reportes + dashboard ejecutivo integrado", "front", "reportes", "F7", 6, ["REP-BACK"], "Reportes productivos", "Export Excel/PDF ok", [], "bajo", "front"),
    Task("QA-01", "Tests e2e flujos críticos (comercial, contab, GoSocket) + smoke", "qa", "qa", "F7", 5, ["REP-FRONT", "INT-FRONT", "COM-FRONT"], "Suite e2e CI", "Flujos críticos pasan", [], "medio", "qa"),
    Task("QA-LOAD", "Pruebas carga k6: documentos comerciales, latencia p95 < 500ms", "qa", "qa", "F7", 2, ["QA-01"], "Reporte k6", "p95 bajo umbral en staging", [], "medio", "qa"),
    Task("QA-SEC", "Escaneo OWASP ZAP + validación controles seguridad", "qa", "qa", "F7", 2, ["QA-01"], "Reporte seguridad", "0 vulnerabilidades críticas", [], "medio", "qa"),
    Task("INF-OBS", "Observabilidad: logs JSON, health checks, métricas, alertas básicas", "infra", "core", "F7", 2, ["REP-FRONT"], "Stack observabilidad", "Health + logs centralizados", [], "medio", "infra"),
    Task("QA-02", "UAT cliente + performance básico + bugs P1/P2", "qa", "qa", "F7", 5, ["QA-LOAD", "QA-SEC", "INF-OBS"], "Acta UAT firmada", "0 bugs P1 abiertos", [], "medio", "qa"),
    Task("DEP-01", "Deploy producción: Docker prod, nginx TLS, backup, rollback", "infra", "core", "F7", 3, ["QA-02"], "Entorno prod", "Deploy + rollback ok", [], "medio", "infra"),
    Task("DEP-02", "Capacitación + documentación usuario + go-live", "infra", "core", "F7", 2, ["DEP-01"], "Go-live", "Usuarios capacitados", [], "bajo", "infra"),
]

MILESTONES = [
    {"id": "M-F0", "nombre": "Hito F0: Specs Enterprise + ERD + OpenAPI v1", "fase": "F0", "after": "DEF-API"},
    {"id": "M-F1", "nombre": "Hito F1: Mockups v1 + acta correcciones cliente", "fase": "F1", "after": "FB-ACTA"},
    {"id": "M-F2", "nombre": "Hito F2: Core + Catálogos productivos", "fase": "F2", "after": "CAT-FRONT"},
    {"id": "M-F3", "nombre": "Hito F3: Core financiero (Contab + Tes + Pres + Insumos)", "fase": "F3", "after": "INS-FRONT"},
    {"id": "M-F4", "nombre": "Hito F4: Comercial + Workflow + spike GoSocket", "fase": "F4", "after": "COM-FRONT"},
    {"id": "M-F5", "nombre": "Hito F5: Contabilización automática", "fase": "F5", "after": "INT-CONT-FRONT"},
    {"id": "M-F6", "nombre": "Hito F6: GoSocket DTE productivo", "fase": "F6", "after": "INT-FRONT"},
    {"id": "M-F7", "nombre": "Hito F7: Go-live", "fase": "F7", "after": "DEP-02"},
]
