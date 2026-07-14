"""Trazabilidad requisitos PDF Enterprise ↔ tareas Gantt."""

from __future__ import annotations

from erp_gantt_tasks import TASKS

# Ítems = secciones/capítulos de los PDFs oficiales
PDF_DOCUMENTS: list[dict] = [
    {
        "id": "pdf-global",
        "file": "ERP-Contable-Financiero-Enterprise.pdf",
        "short": "PDF Global",
        "title": "ERP Contable Financiero Enterprise",
        "sections": [
            {
                "id": "G-01",
                "chapter": "Cap. 1",
                "title": "Visión general, objetivos y alcance",
                "page": "p.2-3",
                "summary": "ERP modular multitenant, horizonte 10 años, alcance oficial v1.",
                "tasks": ["DEF-DOC-REV", "DEF-ALCANCE", "DEF-ARQ"],
            },
            {
                "id": "G-02",
                "chapter": "Cap. 4",
                "title": "Arquitectura general (Clean, DDD, Hexagonal)",
                "page": "p.3-4",
                "summary": "Módulos desacoplados, API central, inversión de dependencias.",
                "tasks": ["DEF-ARQ", "DEF-PRISMA", "DEF-API"],
            },
            {
                "id": "G-03",
                "chapter": "Cap. 4",
                "title": "Stack tecnológico (NestJS, React, PostgreSQL)",
                "page": "p.4-5",
                "summary": "Backend NestJS, front React, PG con soft delete y auditoría.",
                "tasks": ["INF-01", "INF-03", "INF-05", "INF-06", "DEF-PRISMA"],
            },
            {
                "id": "G-04",
                "chapter": "Cap. 9",
                "title": "Administration & Seguridad",
                "page": "p.5-6",
                "summary": "Usuarios, roles RBAC, empresas, sucursales, JWT refresh.",
                "tasks": [
                    "DEF-CORE", "DEF-SUCURSALES", "DEF-SEC", "MOCK-CORE", "CORE-CORR",
                    "CORE-BACK", "CORE-FRONT",
                ],
            },
            {
                "id": "G-05",
                "chapter": "Cap. 9",
                "title": "Contratistas & Insumos",
                "page": "p.5-6",
                "summary": "Proveedores, contratos, catálogo insumos, trazabilidad.",
                "tasks": [
                    "DEF-INSUMOS", "DEF-CAT", "MOCK-INSUMOS", "MOCK-CAT",
                    "INS-CORR", "INS-BACK", "INS-FRONT", "CAT-BACK", "CAT-FRONT", "CAT-CORR",
                ],
            },
            {
                "id": "G-06",
                "chapter": "Cap. 9",
                "title": "Comercial & Facturación",
                "page": "p.5-6",
                "summary": "OC venta, cotizaciones, notas crédito, ciclo comercial.",
                "tasks": [
                    "DEF-COM", "DEF-DOC-COM", "MOCK-COM-CLI", "MOCK-COM-LIBRO", "MOCK-COM-DASH",
                    "COM-CORR", "COM-BACK", "COM-NC", "COM-EMAIL", "COM-FRONT",
                ],
            },
            {
                "id": "G-07",
                "chapter": "Cap. 9",
                "title": "Contabilidad & Tesorería",
                "page": "p.5-6",
                "summary": "Plan cuentas, asientos, CC, flujo caja, conciliación, pagos.",
                "tasks": [
                    "DEF-CONT", "DEF-TES", "MOCK-CONT", "MOCK-TES",
                    "CONT-CORR", "CONT-BACK", "CONT-FRONT",
                    "TES-CORR", "TES-BACK", "TES-FRONT",
                ],
            },
            {
                "id": "G-08",
                "chapter": "Cap. 9",
                "title": "Presupuestos & Dashboard ejecutivo",
                "page": "p.5-6",
                "summary": "Presupuestos, KPIs tiempo real, alertas, drill-down.",
                "tasks": [
                    "DEF-PRES", "DEF-REP", "MOCK-PRES", "MOCK-REP",
                    "PRES-CORR", "PRES-BACK", "PRES-FRONT",
                    "REP-CORR", "REP-BACK", "REP-FRONT",
                ],
            },
            {
                "id": "G-09",
                "chapter": "Cap. 9",
                "title": "Workflow, Reportes & Auditoría",
                "page": "p.5-6",
                "summary": "Motor aprobaciones, reportes export, trazabilidad total.",
                "tasks": [
                    "DEF-WF", "DEF-AUDIT", "MOCK-COM-WF",
                    "WF-CORR", "WF-BACK", "WF-FRONT", "AUDIT-BACK",
                ],
            },
            {
                "id": "G-10",
                "chapter": "Integración",
                "title": "GoSocket PFE / Facturación electrónica",
                "page": "p.6-7",
                "summary": "IElectronicInvoiceProvider, JSON→GoSocket, XML/PDF, estados SII.",
                "tasks": [
                    "DEF-GOSOCKET", "MOCK-GOSOCKET", "INT-GOSOCKET-SPIKE",
                    "INT-CORR", "INT-BACK", "INT-FRONT",
                ],
            },
            {
                "id": "G-11",
                "chapter": "Cap. 10-11",
                "title": "Seguridad, multiempresa y estándares",
                "page": "p.7-8",
                "summary": "RBAC granular, tenant_id, OWASP, rate limit, GitFlow.",
                "tasks": ["DEF-SEC", "DEF-SUCURSALES", "DEF-AUDIT", "CORE-BACK", "QA-SEC"],
            },
            {
                "id": "G-12",
                "chapter": "Cap. 12-13",
                "title": "DevOps, CI/CD, monitoreo y DR",
                "page": "p.8-9",
                "summary": "Docker, GitHub Actions, logs JSON, health checks, backup.",
                "tasks": ["INF-02", "INF-07", "INF-OBS", "DEP-01", "DEP-02"],
            },
            {
                "id": "G-13",
                "chapter": "Cap. 26",
                "title": "Roadmap técnico (5 fases)",
                "page": "p.9-10",
                "summary": "Base → Core financiero → Comercial/DTE → Inteligencia → Hardening.",
                "tasks": [
                    "DEF-DOC-REV", "DEF-ALCANCE", "FB-ACTA",
                    "CAT-FRONT", "INS-FRONT", "COM-FRONT", "INT-FRONT", "REP-FRONT", "DEP-02",
                ],
            },
            {
                "id": "G-14",
                "chapter": "Transversal",
                "title": "Contabilización automática eventos→asientos",
                "page": "p.5-7",
                "summary": "Integración contable entre módulos transaccionales.",
                "tasks": ["INT-CONT-CORR", "INT-CONT-BACK", "INT-CONT-FRONT"],
            },
            {
                "id": "G-15",
                "chapter": "F1",
                "title": "Validación UX / wireframes con cliente",
                "page": "PDF Com. p.19",
                "summary": "Mockups, walkthrough, acta correcciones priorizada.",
                "tasks": [
                    "MOCK-SHELL", "FB-PRES", "FB-ACTA",
                    "INF-05", "INF-06",
                ] + [t.id for t in TASKS if t.tipo in ("mock", "corr", "fb")],
            },
            {
                "id": "G-16",
                "chapter": "Cap. 14",
                "title": "QA, UAT y hardening",
                "page": "p.9-10",
                "summary": "E2E, carga, seguridad, UAT, go-live.",
                "tasks": ["QA-01", "QA-LOAD", "QA-SEC", "QA-02"],
            },
        ],
    },
    {
        "id": "pdf-comercial",
        "file": "Modulo-Comercial-Documento-Tecnico-Enterprise.pdf",
        "short": "PDF Comercial",
        "title": "Módulo Comercial Enterprise",
        "sections": [
            {
                "id": "C-01",
                "chapter": "Índice 01",
                "title": "Stack y arquitectura comercial",
                "page": "p.2-4",
                "summary": "Clean/DDD, motor documentos común, event driven.",
                "tasks": ["DEF-DOC-COM", "DEF-COM", "DEF-ARQ", "DEF-API"],
            },
            {
                "id": "C-02",
                "chapter": "Índice 03",
                "title": "Flujo comercial completo",
                "page": "p.4-5",
                "summary": "Prospecto→Cliente→Cotización→Aprobación→Orden→Contabilidad.",
                "tasks": ["DEF-COM", "COM-BACK", "COM-FRONT", "INT-CONT-BACK"],
            },
            {
                "id": "C-03",
                "chapter": "Submódulo",
                "title": "Clientes (customers)",
                "page": "p.5-6",
                "summary": "CRUD, crédito, listas precio, import Excel, direcciones.",
                "tasks": [
                    "DEF-COM", "MOCK-COM-CLI", "COM-CORR", "COM-BACK", "COM-FRONT",
                ],
            },
            {
                "id": "C-04",
                "chapter": "Submódulo",
                "title": "Prospectos y cotizaciones",
                "page": "p.6-7",
                "summary": "Leads, estados, versionado cotización, vigencia, email PDF.",
                "tasks": [
                    "MOCK-COM-CLI", "MOCK-COM-LIBRO", "COM-BACK", "COM-EMAIL", "COM-FRONT",
                ],
            },
            {
                "id": "C-05",
                "chapter": "Motor",
                "title": "Motor común de documentos",
                "page": "p.7-8",
                "summary": "commercial_documents, document_items, tipos parametrizables.",
                "tasks": ["DEF-COM", "DEF-PRISMA", "COM-BACK", "COM-NC"],
            },
            {
                "id": "C-06",
                "chapter": "Libro",
                "title": "Libro Comercial",
                "page": "p.9-10",
                "summary": "Filtros avanzados, acciones masivas, export Excel/PDF/CSV.",
                "tasks": ["MOCK-COM-LIBRO", "COM-FRONT", "COM-BACK", "REP-BACK"],
            },
            {
                "id": "C-07",
                "chapter": "Índice 04",
                "title": "APIs REST /api/v1",
                "page": "p.10-11",
                "summary": "customers, documents, convert, invoice, paginación y DTOs.",
                "tasks": ["DEF-API", "INF-04", "COM-BACK", "INT-BACK"],
            },
            {
                "id": "C-08",
                "chapter": "Índice 05",
                "title": "Integración GoSocket (ElectronicInvoiceProvider)",
                "page": "p.11-12",
                "summary": "Resiliencia, circuit breaker, logs, dashboard DTE.",
                "tasks": [
                    "DEF-GOSOCKET", "MOCK-GOSOCKET", "INT-GOSOCKET-SPIKE",
                    "INT-BACK", "INT-FRONT", "INT-CORR",
                ],
            },
            {
                "id": "C-09",
                "chapter": "Índice 03",
                "title": "Motor workflow y aprobaciones",
                "page": "p.12-13",
                "summary": "Estados configurables, aprobación por monto, escalamiento.",
                "tasks": ["DEF-WF", "MOCK-COM-WF", "WF-CORR", "WF-BACK", "WF-FRONT"],
            },
            {
                "id": "C-10",
                "chapter": "Índice 04",
                "title": "Seguridad RBAC comercial",
                "page": "p.13-14",
                "summary": "Roles Admin/Supervisor/Vendedor/Lectura, JWT, OWASP.",
                "tasks": ["DEF-SEC", "DEF-CORE", "CORE-BACK", "QA-SEC"],
            },
            {
                "id": "C-11",
                "chapter": "Índice 04",
                "title": "Auditoría y logging",
                "page": "p.14-15",
                "summary": "audit_logs, integration log, email log, retención.",
                "tasks": ["DEF-AUDIT", "AUDIT-BACK", "COM-EMAIL", "INT-BACK"],
            },
            {
                "id": "C-12",
                "chapter": "Índice 05",
                "title": "UX/UI — wireframes y validación",
                "page": "p.15-16",
                "summary": "Responsive, accesibilidad, navegación, validación pendiente.",
                "tasks": [
                    "MOCK-SHELL", "INF-05", "INF-06", "FB-PRES", "FB-ACTA",
                ] + [t.id for t in TASKS if t.tipo == "mock"],
            },
            {
                "id": "C-13",
                "chapter": "Dashboard",
                "title": "Dashboard comercial KPIs",
                "page": "p.16-17",
                "summary": "Conversión, top clientes, workflow pendiente, export.",
                "tasks": ["MOCK-COM-DASH", "COM-FRONT", "REP-BACK", "REP-FRONT"],
            },
            {
                "id": "C-14",
                "chapter": "Índice 05",
                "title": "QA y DevOps pipeline",
                "page": "p.17-19",
                "summary": "Jest 80%, Supertest, k6, OWASP ZAP, CI/CD staging/prod.",
                "tasks": ["INF-07", "QA-01", "QA-LOAD", "QA-SEC", "QA-02"],
            },
        ],
    },
    {
        "id": "internal",
        "file": "(Metodología proyecto)",
        "short": "Metodología",
        "title": "Metodología mock-first (no en PDF)",
        "sections": [
            {
                "id": "M-01",
                "chapter": "Proceso",
                "title": "Correcciones post-mockup (CORR)",
                "page": "—",
                "summary": "Aplicar acta FB-ACTA antes de implementación back/front.",
                "tasks": [t.id for t in TASKS if "-CORR" in t.id or t.tipo == "corr"],
            },
        ],
    },
]


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def build_traceability() -> dict:
    """Construye mapas doc↔tareas y valida cobertura."""
    all_task_ids = {t.id for t in TASKS}
    task_refs: dict[str, list[dict]] = {tid: [] for tid in all_task_ids}
    section_index: dict[str, dict] = {}
    seen_pairs: set[tuple[str, str]] = set()

    documents_out: list[dict] = []
    for doc in PDF_DOCUMENTS:
        sections_out: list[dict] = []
        for sec in doc["sections"]:
            tasks = _dedupe(sec["tasks"])
            existing = [t for t in tasks if t in all_task_ids]
            missing = [t for t in tasks if t not in all_task_ids]
            sec_out = {
                **sec,
                "tasks": existing,
                "task_count": len(existing),
                "missing_tasks": missing,
            }
            sections_out.append(sec_out)
            section_index[sec["id"]] = {
                "doc_id": doc["id"],
                "doc_short": doc["short"],
                "doc_title": doc["title"],
                "section_id": sec["id"],
                "chapter": sec["chapter"],
                "title": sec["title"],
                "page": sec.get("page", ""),
                "summary": sec.get("summary", ""),
            }
            ref = {
                "doc_id": doc["id"],
                "doc_short": doc["short"],
                "section_id": sec["id"],
                "chapter": sec["chapter"],
                "title": sec["title"],
                "page": sec.get("page", ""),
            }
            for tid in existing:
                key = (tid, sec["id"])
                if key in seen_pairs:
                    continue
                seen_pairs.add(key)
                task_refs[tid].append(ref)

        documents_out.append({**doc, "sections": sections_out})

    unmapped_tasks = sorted(tid for tid, refs in task_refs.items() if not refs)
    empty_sections = [
        f"{doc['id']}:{sec['id']}"
        for doc in documents_out
        for sec in doc["sections"]
        if sec["task_count"] == 0
    ]

    return {
        "documents": documents_out,
        "task_refs": task_refs,
        "section_index": section_index,
        "coverage": {
            "total_tasks": len(all_task_ids),
            "mapped_tasks": len(all_task_ids) - len(unmapped_tasks),
            "unmapped_tasks": unmapped_tasks,
            "empty_sections": empty_sections,
        },
    }


if __name__ == "__main__":
    import json

    data = build_traceability()
    print(json.dumps(data["coverage"], ensure_ascii=False, indent=2))
