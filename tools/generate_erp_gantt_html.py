#!/usr/bin/env python3
"""Genera HTML Gantt estilo Devint para ERP 6 meses."""

from __future__ import annotations

import json
from datetime import date, timedelta
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "docs" / "erp-planificacion" / "erp_dependencias.json"
OUT_DIR = ROOT / "docs" / "erp-planificacion"
LOGO_PATH = OUT_DIR / "assets" / "logo-devint-horizontal.png"
OUT_PATHS = [
    OUT_DIR / "erp_gantt_devint_6_meses.html",  # nombre principal (Devint)
    OUT_DIR / "erp_gantt_6_meses.html",           # alias
]

PROJECT_START = date(2026, 7, 13)
TOTAL_WEEKS = 26


def devint_logo_src() -> str:
    """Logo Devint recortado y embebido (base64) para que funcione al copiar el HTML."""
    if not LOGO_PATH.exists():
        return "assets/logo-devint-horizontal.png"
    import base64
    from io import BytesIO

    try:
        from PIL import Image
    except ImportError:
        b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
        return f"data:image/png;base64,{b64}"

    im = Image.open(LOGO_PATH).convert("RGBA")
    px = im.load()
    w, h = im.size
    threshold = 30
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a > 0 and (r > threshold or g > threshold or b > threshold):
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    if max_x >= min_x and max_y >= min_y:
        im = im.crop((min_x, min_y, max_x + 1, max_y + 1))

    buf = BytesIO()
    im.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/png;base64,{b64}"


MONTH_GROUPS = [
    ("MES 1 — Jul 2026", "F0 Definiciones Enterprise", "4", "#e0f2fe", "#0369a1"),
    ("MES 2 — Ago 2026", "F1 Mockups + Feedback", "5", "#dbeafe", "#1d4ed8"),
    ("MES 3 — Sep 2026", "F2 Core + Catálogos", "4", "#f3e8ff", "#6b21a8"),
    ("MES 4 — Oct 2026", "F3 Core Financiero", "4", "#ede9fe", "#5b21b6"),
    ("MES 5 — Nov 2026", "F4–F6 Comercial + GoSocket", "5", "#fce7f3", "#be185d"),
    ("MES 6 — Dic–Ene 2027", "F7 Reportes + QA + Go-live", "4", "#ffedd5", "#c2410c"),
]

PHASE_ORDER = ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7"]

PHASE_HEADER_COLORS = {
    "F0": ("#eff6ff", "#1e3a8a"),
    "F1": ("#f0fdf4", "#166534"),
    "F2": ("#faf5ff", "#581c87"),
    "F3": ("#fff7ed", "#c2410c"),
    "F4": ("#f0fdfa", "#0f766e"),
    "F5": ("#fdf4ff", "#7e22ce"),
    "F6": ("#fef2f2", "#b91c1c"),
    "F7": ("#fffbeb", "#b45309"),
}

PHASE_LABELS = {
    "F0": ("F0: Definiciones Enterprise — PDFs + ERD + OpenAPI /api/v1", "fa-file-lines"),
    "F1": ("F1: Mockups + Feedback — comercial, financiero, GoSocket", "fa-palette"),
    "F2": ("F2: Core + Catálogos — CORR → BACK → FRONT", "fa-layer-group"),
    "F3": ("F3: Core Financiero — Contab, Tesorería, Presupuestos, Insumos", "fa-calculator"),
    "F4": ("F4: Comercial + Workflow + spike GoSocket", "fa-store"),
    "F5": ("F5: Contabilización automática", "fa-link"),
    "F6": ("F6: GoSocket DTE producción", "fa-plug"),
    "F7": ("F7: Dashboard, QA, Hardening & Go-live", "fa-chart-pie"),
}

BAR_CLASS = {
    "def": "bar-def",
    "mock": "bar-mock",
    "fb": "bar-fb",
    "infra": "bar-infra",
    "back": "bar-back",
    "front": "bar-front",
    "qa": "bar-qa",
    "corr": "bar-corr",
}

RESPONSIBLE = {
    "def": "Analista / BA",
    "mock": "Frontend",
    "fb": "PM + Cliente",
    "infra": "DevOps",
    "back": "Backend",
    "front": "Frontend",
    "qa": "QA Analyst",
    "corr": "Frontend",
}

PREFIX = {
    "def": "DEF",
    "mock": "MOCK",
    "fb": "FB",
    "infra": "INFRA",
    "back": "BACK",
    "front": "FRONT",
    "qa": "QA",
    "corr": "CORR",
}

MODULE_META = {
    "core": ("Core", "#6366f1", "#eef2ff"),
    "catalogos": ("Catálogos", "#0891b2", "#ecfeff"),
    "contabilidad": ("Contabilidad", "#059669", "#ecfdf5"),
    "tesoreria": ("Tesorería", "#0d9488", "#ccfbf1"),
    "presupuestos": ("Presupuestos", "#7c3aed", "#f5f3ff"),
    "insumos": ("Insumos", "#d97706", "#fffbeb"),
    "comercial": ("Comercial", "#db2777", "#fdf2f8"),
    "workflow": ("Workflow", "#4f46e5", "#eef2ff"),
    "integraciones": ("Integraciones", "#0284c7", "#f0f9ff"),
    "reportes": ("Reportes", "#ca8a04", "#fefce8"),
    "qa": ("QA", "#f59e0b", "#fffbeb"),
    # legacy aliases
    "ventas": ("Comercial", "#db2777", "#fdf2f8"),
    "inventario": ("Insumos", "#d97706", "#fffbeb"),
    "compras": ("Insumos", "#d97706", "#fffbeb"),
}


def fmt_date(iso: str) -> str:
    return date.fromisoformat(iso).strftime("%d/%m/%Y")


def fmt_date_short(iso: str) -> str:
    return date.fromisoformat(iso).strftime("%d/%m")


def week_monday(week_num: int) -> date:
    return PROJECT_START + timedelta(days=(week_num - 1) * 7)


def module_badge(modulo: str) -> str:
    label, color, bg = MODULE_META.get(modulo, (modulo.title(), "#64748b", "#f1f5f9"))
    return (
        f'<span class="mod-badge" style="--mod-color:{color};--mod-bg:{bg};">{label}</span>'
    )


def tipo_badge(kind: str) -> str:
    label = PREFIX.get(kind, kind.upper())
    return f'<span class="tipo-badge tipo-{kind}">{label}</span>'


def risk_badge(riesgo: str) -> str:
    if riesgo == "alto":
        return '<span class="risk-badge risk-alto" title="Riesgo alto">!</span>'
    if riesgo == "medio":
        return '<span class="risk-badge risk-medio" title="Riesgo medio">·</span>'
    return ""


def trace_refs_block(refs: list[dict]) -> str:
    if not refs:
        return (
            '<span class="trace-wrap trace-wrap-empty" title="Sin referencia en PDFs">'
            '<i class="fa-solid fa-unlink"></i></span>'
        )
    items: list[str] = []
    for r in refs:
        page = r.get("page") or "—"
        items.append(
            f'<li><span class="trace-pop-doc">{r["doc_short"]}</span> '
            f'<code>{r["section_id"]}</code> · {r["chapter"]}, {page}'
            f'<div class="trace-pop-title">{escape(r["title"])}</div></li>'
        )
    tip = escape(" · ".join(f'{r["section_id"]} ({r["doc_short"]})' for r in refs[:3]))
    if len(refs) > 3:
        tip += escape(f" +{len(refs) - 3} más")
    return (
        f'<span class="trace-wrap" title="{tip}">'
        f'<button type="button" class="trace-info-btn" aria-label="Referencias PDF">'
        f'<i class="fa-solid fa-book-open"></i><span class="trace-count">{len(refs)}</span>'
        f"</button>"
        f'<div class="trace-popover" role="tooltip"><ul>{"".join(items)}</ul></div>'
        f"</span>"
    )


def trace_panel_html(documents: list[dict], coverage: dict) -> str:
    mapped = coverage.get("mapped_tasks", 0)
    total = coverage.get("total_tasks", 0)
    unmapped = coverage.get("unmapped_tasks", [])
    warn = ""
    if unmapped:
        warn = (
            f'<div class="trace-warn"><i class="fa-solid fa-triangle-exclamation"></i> '
            f'{len(unmapped)} tareas sin mapear: {", ".join(unmapped[:5])}'
            f'{"…" if len(unmapped) > 5 else ""}</div>'
        )
    doc_options = ['<option value="">Todos los documentos</option>']
    for doc in documents:
        doc_options.append(
            f'<option value="{doc["id"]}">{doc["short"]} — {doc["title"]}</option>'
        )
    sections_html: list[str] = []
    for doc in documents:
        for sec in doc["sections"]:
            if sec["task_count"] == 0:
                continue
            page = sec.get("page") or "—"
            summary = sec.get("summary", "")
            sections_html.append(
                f'<button type="button" class="trace-section-item" '
                f'data-section-id="{sec["id"]}" data-doc-id="{doc["id"]}" '
                f'title="{escape(summary)}">'
                f'<span class="trace-sec-head">'
                f'<code class="trace-sec-id">{sec["id"]}</code> '
                f'<span class="trace-sec-doc">{doc["short"]}</span>'
                f'<span class="trace-sec-count">{sec["task_count"]}</span>'
                f"</span>"
                f'<span class="trace-sec-title">{sec["title"]}</span>'
                f'<span class="trace-sec-meta">{sec["chapter"]} · {page}</span>'
                f"</button>"
            )
    return f"""
        <aside id="trace-panel" class="trace-panel collapsed no-print" aria-label="Trazabilidad PDF">
            <div class="trace-panel-head">
                <h3><i class="fa-solid fa-book-open"></i> Trazabilidad PDF</h3>
                <button type="button" class="trace-panel-close" onclick="toggleTracePanel(false)" title="Ocultar panel">×</button>
            </div>
            <div class="trace-coverage">
                <span class="trace-cov-num">{mapped}/{total}</span> tareas vinculadas a requisitos
            </div>
            {warn}
            <label class="trace-label" for="trace-doc-filter">Documento</label>
            <select id="trace-doc-filter" class="trace-select">{"".join(doc_options)}</select>
            <label class="trace-label" for="trace-search">Buscar ítem</label>
            <input type="search" id="trace-search" class="trace-search" placeholder="Capítulo, ID, título…">
            <label class="trace-check">
                <input type="checkbox" id="trace-hide-unmatched"> Ocultar tareas no asociadas
            </label>
            <div class="trace-section-list" id="trace-section-list">
                {"".join(sections_html)}
            </div>
            <button type="button" class="trace-clear-btn" id="trace-clear-btn">Limpiar filtro</button>
            <p class="trace-hint">Clic en un ítem del documento para resaltar tareas en el Gantt. Pasa el cursor sobre <i class="fa-solid fa-book-open"></i> en cada fila para ver la referencia exacta.</p>
        </aside>"""


def stats_cards_html(
    task_count: int,
    person_days: int,
    go_live: str,
    go_live_target: str,
    dentro_plazo: bool,
    phase_counts: dict[str, int],
) -> str:
    plazo_cls = "kpi-ok" if dentro_plazo else "kpi-warn"
    plazo_txt = "En plazo" if dentro_plazo else "Fuera de plazo"
    mock_count = phase_counts.get("F1", 0)
    impl_count = sum(phase_counts.get(f, 0) for f in PHASE_ORDER if f not in ("F0", "F1"))
    return f"""
        <div class="stats-grid no-print">
            <div class="kpi-card">
                <div class="kpi-icon" style="background:#eef2ff;color:#4f46e5;"><i class="fa-solid fa-list-check"></i></div>
                <div><div class="kpi-value">{task_count}</div><div class="kpi-label">Tareas totales</div></div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon" style="background:#f0fdf4;color:#16a34a;"><i class="fa-solid fa-calendar-days"></i></div>
                <div><div class="kpi-value">{person_days}</div><div class="kpi-label">Persona-día</div></div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon" style="background:#fef3c7;color:#d97706;"><i class="fa-solid fa-palette"></i></div>
                <div><div class="kpi-value">{mock_count}</div><div class="kpi-label">Mockups (F1)</div></div>
            </div>
            <div class="kpi-card">
                <div class="kpi-icon" style="background:#fce7f3;color:#db2777;"><i class="fa-solid fa-code"></i></div>
                <div><div class="kpi-value">{impl_count}</div><div class="kpi-label">Impl. (F2–F7)</div></div>
            </div>
            <div class="kpi-card {plazo_cls}">
                <div class="kpi-icon" style="background:#{'ecfdf5' if dentro_plazo else '#fef2f2'};color:#{'16a34a' if dentro_plazo else '#dc2626'};">
                    <i class="fa-solid fa-{'circle-check' if dentro_plazo else 'triangle-exclamation'}"></i>
                </div>
                <div>
                    <div class="kpi-value" style="font-size:1.1rem;">{go_live_target}</div>
                    <div class="kpi-label">Go-live obj. · {plazo_txt}</div>
                </div>
            </div>
        </div>"""


def phase_timeline_html(phase_counts: dict[str, int]) -> str:
    steps = []
    for fase in PHASE_ORDER:
        label, icon = PHASE_LABELS[fase]
        short = label.split(":")[0]
        bg, color = PHASE_HEADER_COLORS[fase]
        count = phase_counts.get(fase, 0)
        steps.append(
            f'<div class="phase-step" style="--step-bg:{bg};--step-color:{color};" title="{label}">'
            f'<div class="phase-step-icon"><i class="fa-solid {icon}"></i></div>'
            f'<div class="phase-step-label">{short}</div>'
            f'<div class="phase-step-count">{count}</div>'
            f'</div>'
        )
    connector = '<div class="phase-connector"></div>'
    inner = connector.join(steps)
    return f'<div class="phase-timeline no-print">{inner}</div>'


def tab_config(task_count: int) -> dict:
    return {
        "total": {
            "id": "tab-total",
            "btn": "btn-total",
            "table": "table-total",
            "icon": "fa-table-columns",
            "label": "Total",
            "eje": f"Vista consolidada — {task_count} tareas · metodología v2",
            "header_bg": "#f8fafc",
            "header_color": "#0f172a",
            "filter": lambda t: True,
        },
        "def": {
            "id": "tab-def",
            "btn": "btn-def",
            "table": "table-def",
            "icon": "fa-file-lines",
            "label": "1. Definiciones",
            "eje": "Specs funcionales, ERD Prisma y OpenAPI borrador",
            "header_bg": "#eff6ff",
            "header_color": "#1e3a8a",
            "filter": lambda t: t["fase"] == "F0",
        },
        "mock": {
            "id": "tab-mock",
            "btn": "btn-mock",
            "table": "table-mock",
            "icon": "fa-palette",
            "label": "2. Mockups & Feedback",
            "eje": "Maquetación HTML por módulo → presentación → acta correcciones",
            "header_bg": "#f0fdf4",
            "header_color": "#166534",
            "filter": lambda t: t["fase"] == "F1",
        },
        "impl": {
            "id": "tab-impl",
            "btn": "btn-impl",
            "table": "table-impl",
            "icon": "fa-code",
            "label": "3. Implementación",
            "eje": "Por módulo: CORR mockup → Backend → Front integrado",
            "header_bg": "#faf5ff",
            "header_color": "#581c87",
            "filter": lambda t: t["fase"] in ("F2", "F3", "F4", "F5", "F6", "F7"),
        },
    }


def task_bar_kind(task: dict) -> str:
    if "-CORR" in task["id"]:
        return "corr"
    return task["tipo"]


def week_index(d: date) -> int:
    delta = (d - PROJECT_START).days
    return min(TOTAL_WEEKS, max(1, delta // 7 + 1))


def task_weeks(task: dict) -> tuple[int, int]:
    start = date.fromisoformat(task["fecha_inicio"])
    end = date.fromisoformat(task["fecha_fin"])
    return week_index(start), week_index(end)


def bar_cells(
    start_w: int,
    end_w: int,
    bar_class: str,
    label: str,
    *,
    tooltip: str = "",
    is_milestone: bool = False,
    is_spike: bool = False,
) -> str:
    cells: list[str] = []
    w = 1
    tip = tooltip.replace('"', "&quot;")
    while w <= TOTAL_WEEKS:
        bg = "week-alt" if w % 2 == 0 else "week-base"
        if w < start_w:
            cells.append(f'<td class="week-cell {bg}"></td>')
            w += 1
        elif w == start_w:
            span = end_w - start_w + 1
            extra = " bar-milestone" if is_milestone else (" bar-spike" if is_spike else "")
            inner = f'<div class="bar-inner{extra}" title="{tip}"><span>{label}</span></div>'
            cells.append(
                f'<td colspan="{span}" class="week-cell bar-cell {bar_class}{extra}" title="{tip}">{inner}</td>'
            )
            w = end_w + 1
        else:
            cells.append(f'<td class="week-cell {bg}"></td>')
            w += 1
    return "".join(cells)


def milestones_row(milestones: list[dict]) -> str:
    cells = [
        '<th colspan="3" class="sticky-col-group milestone-label">'
        '<i class="fa-solid fa-flag-checkered"></i> Hitos</th>'
    ]
    for w in range(1, TOTAL_WEEKS + 1):
        bg = "week-alt" if w % 2 == 0 else "week-base"
        hits = [m for m in milestones if week_index(date.fromisoformat(m["fecha"])) == w]
        if hits:
            titles = " · ".join(m["nombre"] for m in hits)
            tip = titles.replace('"', "&quot;")
            cells.append(
                f'<th class="week-cell milestone-cell {bg}" title="{tip}">'
                f'<span class="milestone-diamond"></span></th>'
            )
        else:
            cells.append(f'<th class="week-cell {bg}"></th>')
    return (
        '<tr class="milestone-row">'
        + "".join(cells)
        + "</tr>"
    )


def group_tasks(tasks: list[dict], filt) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {f: [] for f in PHASE_LABELS}
    for t in tasks:
        if filt(t):
            grouped.setdefault(t["fase"], []).append(t)
    return grouped


def render_table_body(
    tasks: list[dict],
    filt,
    header_bg: str,
    header_color: str,
    *,
    use_phase_colors: bool = False,
    task_refs: dict[str, list[dict]] | None = None,
) -> str:
    grouped = group_tasks(tasks, filt)
    rows: list[str] = []
    row_idx = 0
    for fase in PHASE_ORDER:
        phase_tasks = grouped.get(fase, [])
        if not phase_tasks:
            continue
        label, icon = PHASE_LABELS[fase]
        bg, color = PHASE_HEADER_COLORS[fase] if use_phase_colors else (header_bg, header_color)
        rows.append(
            f'<tr class="gantt-phase-header phase-row">'
            f'<td colspan="{3 + TOTAL_WEEKS}" style="font-weight:800;color:{color};background-color:{bg};'
            f'border-left:4px solid {color};">'
            f'<i class="fa-solid {icon}"></i> {label}'
            f' <span class="phase-count">({len(phase_tasks)} tareas)</span>'
            f'</td></tr>'
        )
        phase_tasks = sorted(phase_tasks, key=lambda t: (t["fecha_inicio"], t["id"]))
        for t in phase_tasks:
            sw, ew = task_weeks(t)
            kind = task_bar_kind(t)
            bar = BAR_CLASS.get(kind, "bar-back")
            tip = (
                f"{t['nombre']}\n"
                f"{fmt_date(t['fecha_inicio'])} → {fmt_date(t['fecha_fin'])} "
                f"({t['duracion_dias']}d)\n"
                f"{t.get('entregable', '')}"
            )
            task_id = t["id"]
            refs = (task_refs or {}).get(task_id, [])
            section_ids = ",".join(sorted({r["section_id"] for r in refs}))
            doc_ids = ",".join(sorted({r["doc_id"] for r in refs}))
            trace_block = trace_refs_block(refs)
            task_name = t["nombre"]
            if len(task_name) > 72:
                task_name = task_name[:69] + "…"
            name = (
                f'<div class="task-cell">'
                f'<div class="task-top">'
                f'{tipo_badge(kind)}{module_badge(t["modulo"])}'
                f'<code class="task-id">{task_id}</code>{trace_block}{risk_badge(t.get("riesgo", "bajo"))}'
                f'</div>'
                f'<div class="task-name">{task_name}</div>'
                f'</div>'
            )
            resp = RESPONSIBLE.get(kind, RESPONSIBLE.get(t["tipo"], "Backend"))
            is_live = t["id"] == "DEP-02"
            is_spike = t["id"] in ("INT-GOSOCKET-SPIKE", "INT-SII-SPIKE-01")
            label_bar = "GO-LIVE" if is_live else task_id
            stripe = "row-even" if row_idx % 2 == 0 else "row-odd"
            row_idx += 1
            rows.append(
                f'<tr class="gantt-task-row {stripe}" data-task-id="{task_id}" '
                f'data-modulo="{t["modulo"]}" data-trace-sections="{section_ids}" '
                f'data-trace-docs="{doc_ids}">'
                f'<td class="sticky-col col-task">{name}</td>'
                f'<td class="sticky-col col-resp"><span class="resp-pill">{resp}</span></td>'
                f'<td class="sticky-col col-status">'
                f'<div class="status-badge status-pendiente">Pendiente</div></td>'
                f'{bar_cells(sw, ew, bar, label_bar, tooltip=tip, is_milestone=is_live, is_spike=is_spike)}'
                f'</tr>'
            )
    return "\n".join(rows)


def banner_block_html(go_live: str, eje: str) -> str:
    return (
        '<div class="gantt-banner">'
        '<div class="gantt-banner-logo">'
        f'<img src="{devint_logo_src()}" alt="Devint">'
        '</div>'
        '<div class="gantt-banner-meta">'
        '<div><span class="meta-k">Proyecto</span> <span class="meta-v accent">ERP v1 Web</span></div>'
        '<div><span class="meta-k">Cliente</span> <span class="meta-v">ALMAHUE / Devint</span></div>'
        f'<div><span class="meta-k">Eje</span> <span class="meta-v">{eje}</span></div>'
        '<div><span class="meta-k">Inicio</span> <span class="meta-v">13/07/2026</span>'
        f' <span class="meta-k">· Go-live obj.</span> <span class="meta-v">{go_live}</span></div>'
        '</div></div>'
    )


def month_header_row() -> str:
    parts = [
        '<th class="sticky-col col-task month-corner">Timeline</th>',
        '<th class="sticky-col col-resp month-corner month-corner-empty"></th>',
        '<th class="sticky-col col-status month-corner month-corner-empty"></th>',
    ]
    for label, sublabel, span, bg, color in MONTH_GROUPS:
        parts.append(
            f'<th colspan="{span}" class="month-header" style="background-color:{bg};color:{color};">'
            f'<div class="month-title">{label}</div>'
            f'<div class="month-sub">{sublabel}</div></th>'
        )
    return "<tr class=\"month-row\">" + "".join(parts) + "</tr>"


def colgroup_html() -> str:
    cols = [
        '<col class="col-task-col">',
        '<col class="col-resp-col">',
        '<col class="col-status-col">',
    ]
    cols.extend('<col class="week-col">' for _ in range(TOTAL_WEEKS))
    return f"<colgroup>{''.join(cols)}</colgroup>"


def week_header_row() -> str:
    cells = [
        '<th class="sticky-col col-task">Fase / Tarea</th>',
        '<th class="sticky-col col-resp">Responsable</th>',
        '<th class="sticky-col col-status">Estado</th>',
    ]
    for i in range(1, TOTAL_WEEKS + 1):
        mon = week_monday(i)
        bg = "week-alt" if i % 2 == 0 else "week-base"
        cells.append(
            f'<th class="week-cell week-head {bg}">'
            f'<div class="week-num">S{i}</div>'
            f'<div class="week-date">{mon.strftime("%d/%m")}</div></th>'
        )
    return '<tr class="week-row">' + "".join(cells) + "</tr>"


def render_tab(
    tab_key: str,
    tasks: list[dict],
    cfg: dict,
    active: bool,
    go_live: str,
    milestones: list[dict],
    task_refs: dict[str, list[dict]] | None = None,
) -> str:
    body = render_table_body(
        tasks,
        cfg["filter"],
        cfg["header_bg"],
        cfg["header_color"],
        use_phase_colors=(tab_key == "total"),
        task_refs=task_refs,
    )
    active_cls = " active" if active else ""
    return f"""
            <div id="{cfg['id']}" class="tab-content{active_cls}">
                {banner_block_html(go_live, cfg['eje'])}
                <div class="gantt-scroll">
                <table class="gantt-table" id="{cfg['table']}">
                    {colgroup_html()}
                    <thead>
                        {month_header_row()}
                        {week_header_row()}
                    </thead>
                    <tbody>
                        {body}
                    </tbody>
                </table>
                </div>
                <div class="print-legend" style="display:none;">
                    <strong>Leyenda:</strong>
                    <span class="bar-def" style="padding:1px 6px;margin:0 4px;">Def</span>
                    <span class="bar-mock" style="padding:1px 6px;margin:0 4px;">Mock</span>
                    <span class="bar-fb" style="padding:1px 6px;margin:0 4px;">Feedback</span>
                    <span class="bar-corr" style="padding:1px 6px;margin:0 4px;">CORR</span>
                    <span class="bar-infra" style="padding:1px 6px;margin:0 4px;">Infra</span>
                    <span class="bar-back" style="padding:1px 6px;margin:0 4px;">Backend</span>
                    <span class="bar-front" style="padding:1px 6px;margin:0 4px;">Frontend</span>
                    <span class="bar-qa" style="padding:1px 6px;margin:0 4px;">QA</span>
                    · ERP v1 v2 · Def → Mock → Impl · 13/07/2026 – {go_live}
                </div>
            </div>"""


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    tasks = data["tasks"]
    task_count = len(tasks)
    go_live = date.fromisoformat(data["fecha_fin"]).strftime("%d/%m/%Y")
    go_live_target = date.fromisoformat(data["fecha_fin_objetivo"]).strftime("%d/%m/%Y")
    person_days = sum(t["duracion_dias"] for t in tasks)
    dentro_plazo = data.get("dentro_plazo", False)
    milestones = data.get("milestones", [])
    trace = data.get("traceability", {})
    task_refs = trace.get("task_refs", {})
    trace_documents = trace.get("documents", [])
    trace_coverage = trace.get("coverage", {})
    phase_counts: dict[str, int] = {}
    for t in tasks:
        phase_counts[t["fase"]] = phase_counts.get(t["fase"], 0) + 1
    tabs = tab_config(task_count)
    tab_order = ["total", "def", "mock", "impl"]

    trace_panel = trace_panel_html(trace_documents, trace_coverage)

    tabs_html = ""
    for i, key in enumerate(tab_order):
        tabs_html += render_tab(
            key, tasks, tabs[key], active=(i == 0), go_live=go_live_target,
            milestones=milestones, task_refs=task_refs,
        )

    nav = ""
    for i, key in enumerate(tab_order):
        cfg = tabs[key]
        active = " active" if i == 0 else ""
        count = sum(1 for t in tasks if cfg["filter"](t))
        nav += f"""
            <button onclick="switchTab('{cfg['id']}')" id="{cfg['btn']}" class="tab-btn{active}{' tab-total' if key == 'total' else ''}">
                <i class="fa-solid {cfg['icon']}"></i> {cfg['label']}
                <span class="tab-badge">{count}</span>
            </button>"""

    tab_labels_js = {
        tabs[k]["id"]: f"{tabs[k]['label']} — {sum(1 for t in tasks if tabs[k]['filter'](t))} tareas"
        for k in tab_order
    }
    tab_labels_js["tab-total"] = f"Total — {task_count} tareas"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERP v1 Web - Planificación Estratégica (6 Meses)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --sticky-task: 300px;
            --sticky-resp: 108px;
            --sticky-status: 88px;
            --sticky-total: calc(var(--sticky-task) + var(--sticky-resp) + var(--sticky-status));
            --week-base: 34px;
            --gantt-zoom: 1;
            --week-col-w: 34px;
            --gantt-radius: 1rem;
        }}
        body {{ font-family:'Inter',sans-serif; background:linear-gradient(160deg,#eef2ff 0%,#f1f5f9 40%,#faf5ff 100%); color:#0f172a; min-height:100vh; }}
        .page-wrap {{ width:100%; max-width:1800px; margin-left:auto; margin-right:auto; }}
        .gantt-card {{ width:100%; }}
        .page-header {{ margin-bottom:1.25rem; }}
        .page-header h1 {{ letter-spacing:-0.02em; }}
        .hero-badge {{
            display:inline-flex; align-items:center; gap:8px; padding:6px 14px; border-radius:999px;
            background:linear-gradient(135deg,#4f46e5,#7c3aed); color:white; font-size:11px;
            font-weight:700; text-transform:uppercase; letter-spacing:0.06em; box-shadow:0 4px 14px rgba(79,70,229,0.35);
        }}
        .stats-grid {{
            display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; margin-bottom:1rem;
        }}
        .kpi-card {{
            display:flex; align-items:center; gap:12px; background:white; border-radius:12px;
            padding:14px 16px; border:1px solid #e2e8f0; box-shadow:0 1px 3px rgba(0,0,0,0.06);
            transition:transform 0.2s, box-shadow 0.2s;
        }}
        .kpi-card:hover {{ transform:translateY(-2px); box-shadow:0 8px 20px rgba(0,0,0,0.08); }}
        .kpi-card.kpi-warn {{ border-color:#fecaca; background:linear-gradient(135deg,#fff,#fef2f2); }}
        .kpi-icon {{
            width:42px; height:42px; border-radius:10px; display:flex; align-items:center;
            justify-content:center; font-size:18px; flex-shrink:0;
        }}
        .kpi-value {{ font-size:1.35rem; font-weight:800; line-height:1.1; color:#0f172a; }}
        .kpi-label {{ font-size:11px; color:#64748b; font-weight:600; margin-top:2px; }}
        .phase-timeline {{
            display:flex; align-items:stretch; gap:0; margin-bottom:1rem; overflow-x:auto;
            padding:4px 0 8px; scrollbar-width:thin;
        }}
        .phase-step {{
            flex:1; min-width:88px; text-align:center; padding:10px 6px; border-radius:10px;
            background:var(--step-bg); border:1px solid rgba(0,0,0,0.06); position:relative;
        }}
        .phase-step-icon {{ color:var(--step-color); font-size:16px; margin-bottom:4px; }}
        .phase-step-label {{ font-size:10px; font-weight:800; color:var(--step-color); text-transform:uppercase; }}
        .phase-step-count {{
            font-size:18px; font-weight:800; color:var(--step-color); opacity:0.85; margin-top:2px;
        }}
        .phase-connector {{ width:12px; align-self:center; height:2px; background:linear-gradient(90deg,#cbd5e1,#94a3b8); flex-shrink:0; }}
        .glass-container {{
            position:relative; background-color:#fff; border-radius:var(--gantt-radius);
            box-shadow:0 25px 50px -12px rgba(0,0,0,0.12),0 0 0 1px rgba(0,0,0,0.05); overflow:hidden;
        }}
        .glass-container::before {{
            content:""; position:absolute; top:0; left:0; right:0; bottom:0;
            background:radial-gradient(circle at 20% 20%,rgba(99,102,241,0.04),transparent 50%);
            pointer-events:none; z-index:0; border-radius:inherit;
        }}
        .gantt-scroll {{
            overflow:auto; max-height:72vh; position:relative; z-index:1;
            scrollbar-width:thin; scrollbar-color:#94a3b8 #f1f5f9;
            width:100%; flex:1; min-height:0;
        }}
        .gantt-banner {{
            display:flex; align-items:center; justify-content:space-between; gap:16px;
            width:100%; flex-shrink:0;
            background:linear-gradient(90deg,#000 0%,#080810 8%,#0f172a 26%,#312e81 58%,#1e1b4b 100%);
            border-bottom:1px solid rgba(255,255,255,0.06);
            border-top-left-radius:var(--gantt-radius);
            border-top-right-radius:var(--gantt-radius);
            overflow:hidden;
        }}
        .gantt-banner-logo {{ padding:12px 16px; flex-shrink:0; }}
        .gantt-banner-logo img {{
            height:56px; width:auto; max-width:min(280px,calc(var(--sticky-total) - 16px)); min-height:48px;
            object-fit:contain; object-position:left center; display:block;
        }}
        .gantt-banner-meta {{
            flex:1; min-width:0; color:white; text-align:right; font-size:13px; line-height:1.55;
            padding:14px 16px;
        }}
        .meta-k {{ color:#94a3b8; font-weight:500; }}
        .meta-v {{ font-weight:700; }}
        .meta-v.accent {{ color:#38bdf8; }}
        .gantt-scroll::-webkit-scrollbar {{ height:10px; width:10px; }}
        .gantt-scroll::-webkit-scrollbar-thumb {{ background:#94a3b8; border-radius:5px; }}
        .gantt-table {{
            border-collapse:separate; border-spacing:0;
            table-layout:fixed; font-size:12px; background:#fff;
            min-width:100%;
        }}
        .col-task-col, .sticky-col.col-task, th.col-task, td.col-task {{
            width:var(--sticky-task) !important; min-width:var(--sticky-task) !important; max-width:var(--sticky-task) !important;
        }}
        .col-resp-col, .sticky-col.col-resp, th.col-resp, td.col-resp {{
            width:var(--sticky-resp) !important; min-width:var(--sticky-resp) !important; max-width:var(--sticky-resp) !important;
        }}
        .col-status-col, .sticky-col.col-status, th.col-status, td.col-status {{
            width:var(--sticky-status) !important; min-width:var(--sticky-status) !important; max-width:var(--sticky-status) !important;
        }}
        .week-col, .week-cell {{
            width:var(--week-col-w) !important; min-width:var(--week-col-w) !important; max-width:var(--week-col-w) !important;
        }}
        .gantt-table th, .gantt-table td {{ border:1px solid #e2e8f0; padding:6px 8px; vertical-align:middle; line-height:1.3; }}
        .month-row th {{ padding:8px 6px; border-bottom:2px solid #cbd5e1; position:sticky; top:0; z-index:15; background:#f8fafc; }}
        .month-row th.month-corner {{
            text-align:left; font-weight:800; color:#475569; font-size:11px;
            background:#f8fafc !important; z-index:18;
        }}
        .month-row th.month-corner-empty {{ padding:0; }}
        .month-header {{ text-align:center; }}
        .month-title {{ font-weight:800; font-size:11px; }}
        .month-sub {{ font-size:9px; opacity:0.8; margin-top:2px; font-weight:600; }}
        .week-row th {{ position:sticky; top:38px; z-index:14; background:#f1f5f9; font-size:10px; color:#475569; padding:4px 2px; }}
        .week-num {{ font-weight:800; font-size:10px; }}
        .week-date {{ font-size:8px; color:#94a3b8; margin-top:1px; }}
        .milestone-row th {{ position:sticky; top:62px; z-index:13; padding:3px 2px; font-size:9px; background:#fffbeb; }}
        .milestone-label {{ text-align:left; font-weight:700; color:#b45309; left:0; z-index:16; background:#fffbeb !important; }}
        .milestone-cell {{ text-align:center; }}
        .milestone-diamond {{
            display:inline-block; width:10px; height:10px; background:#16a34a;
            transform:rotate(45deg); border-radius:1px; box-shadow:0 0 0 2px #fff, 0 0 0 3px #16a34a;
        }}
        .sticky-col {{ position:sticky; background:#fff; z-index:5; }}
        .month-row .sticky-col {{ background:#f8fafc !important; }}
        .col-task {{ left:0; box-shadow:2px 0 6px rgba(0,0,0,0.04); overflow:visible; }}
        .col-resp {{ left:var(--sticky-task); box-shadow:2px 0 4px rgba(0,0,0,0.03); }}
        .col-status {{ left:calc(var(--sticky-task) + var(--sticky-resp)); box-shadow:2px 0 4px rgba(0,0,0,0.03); }}
        thead .sticky-col, thead .col-task, thead .col-resp, thead .col-status {{ z-index:17; }}
        .month-row th.sticky-col {{ z-index:18; }}
        .week-cell {{ padding:2px !important; box-sizing:border-box; }}
        .week-base {{ background:#fff; }}
        .week-alt {{ background:#f8fafc; }}
        .task-cell {{ padding-left:8px !important; }}
        .task-top {{ display:flex; flex-wrap:wrap; align-items:center; gap:4px; margin-bottom:3px; }}
        .task-id {{ font-size:9px; color:#94a3b8; font-weight:600; background:#f1f5f9; padding:1px 5px; border-radius:4px; }}
        .task-name {{ font-weight:500; color:#1e293b; font-size:11px; line-height:1.35; }}
        .mod-badge {{
            font-size:8px; font-weight:700; padding:2px 6px; border-radius:999px;
            background:var(--mod-bg); color:var(--mod-color); border:1px solid color-mix(in srgb, var(--mod-color) 25%, transparent);
            text-transform:uppercase; letter-spacing:0.03em;
        }}
        .tipo-badge {{
            font-size:8px; font-weight:800; padding:2px 6px; border-radius:4px;
            letter-spacing:0.04em; text-transform:uppercase;
        }}
        .tipo-def {{ background:#e2e8f0; color:#475569; }}
        .tipo-mock {{ background:#ccfbf1; color:#0f766e; }}
        .tipo-fb {{ background:#cffafe; color:#0e7490; }}
        .tipo-corr {{ background:#ffedd5; color:#c2410c; }}
        .tipo-infra {{ background:#dbeafe; color:#1d4ed8; }}
        .tipo-back {{ background:#ede9fe; color:#6d28d9; }}
        .tipo-front {{ background:#fce7f3; color:#be185d; }}
        .tipo-qa {{ background:#fef3c7; color:#b45309; }}
        .risk-badge {{
            display:inline-flex; align-items:center; justify-content:center;
            width:14px; height:14px; border-radius:50%; font-size:9px; font-weight:900;
        }}
        .risk-alto {{ background:#fef2f2; color:#dc2626; border:1px solid #fecaca; }}
        .risk-medio {{ background:#fffbeb; color:#d97706; border:1px solid #fde68a; }}
        .resp-pill {{ font-size:10px; font-weight:600; color:#475569; background:#f1f5f9; padding:3px 8px; border-radius:999px; white-space:nowrap; }}
        .gantt-task-row {{ transition:background 0.15s; height:36px; }}
        .gantt-task-row td.week-cell {{ padding:0 !important; height:36px; vertical-align:middle; }}
        .gantt-task-row:hover {{ background:#f0f9ff !important; }}
        .gantt-task-row.row-even {{ background:#fafafa; }}
        .gantt-task-row.row-even .sticky-col {{ background:#fafafa; }}
        .gantt-task-row:hover .sticky-col {{ background:#f0f9ff !important; }}
        .gantt-phase-header td {{ padding:10px 14px; font-size:12px; }}
        .phase-count {{ font-weight:500; font-size:11px; opacity:0.7; }}
        .bar-cell {{
            padding:2px !important; vertical-align:middle; height:36px;
            border-color:#e2e8f0; position:relative; background:transparent !important;
        }}
        .bar-inner {{
            display:flex; align-items:center; justify-content:center;
            height:100%; width:100%; min-height:32px;
            border-radius:5px; font-size:9px; font-weight:700;
            padding:0 6px; box-shadow:inset 0 1px 0 rgba(255,255,255,0.2);
            cursor:default; overflow:hidden; white-space:nowrap; text-overflow:ellipsis;
            color:white;
        }}
        .bar-cell.bar-def .bar-inner {{ background:linear-gradient(180deg,#64748b,#475569); }}
        .bar-cell.bar-mock .bar-inner {{ background:linear-gradient(180deg,#14b8a6,#0d9488); }}
        .bar-cell.bar-fb .bar-inner {{ background:linear-gradient(180deg,#06b6d4,#0891b2); }}
        .bar-cell.bar-corr .bar-inner {{ background:linear-gradient(180deg,#f97316,#ea580c); }}
        .bar-cell.bar-infra .bar-inner {{ background:linear-gradient(180deg,#3b82f6,#2563eb); }}
        .bar-cell.bar-back .bar-inner {{ background:linear-gradient(180deg,#8b5cf6,#7c3aed); }}
        .bar-cell.bar-front .bar-inner {{ background:linear-gradient(180deg,#ec4899,#db2777); }}
        .bar-cell.bar-qa .bar-inner {{ background:linear-gradient(180deg,#f59e0b,#d97706); }}
        .bar-cell.bar-milestone .bar-inner {{ background:linear-gradient(180deg,#16a34a,#15803d) !important; font-size:8px; letter-spacing:0.05em; }}
        .bar-cell.bar-spike .bar-inner {{ background:linear-gradient(180deg,#f59e0b,#d97706) !important; border:2px dashed rgba(255,255,255,0.45); box-sizing:border-box; }}
        .bar-cell:hover .bar-inner {{ filter:brightness(1.08); }}
        .gantt-zoom-bar {{
            display:flex; flex-wrap:wrap; align-items:center; gap:8px; margin-bottom:10px;
            padding:8px 12px; background:white; border:1px solid #e2e8f0; border-radius:10px;
            font-size:12px; color:#475569;
        }}
        .gantt-zoom-bar .zoom-title {{ font-weight:700; color:#334155; display:inline-flex; align-items:center; gap:6px; margin-right:4px; }}
        .gantt-zoom-btn {{
            width:32px; height:32px; border:1px solid #cbd5e1; background:#f8fafc; border-radius:8px;
            font-size:18px; font-weight:700; line-height:1; cursor:pointer; color:#334155;
        }}
        .gantt-zoom-btn:hover {{ background:#eef2ff; border-color:#818cf8; }}
        .gantt-zoom-reset {{
            padding:6px 12px; border:1px solid #cbd5e1; background:white; border-radius:8px;
            font-size:11px; font-weight:600; cursor:pointer; color:#475569;
        }}
        .gantt-zoom-reset:hover {{ background:#f1f5f9; }}
        #gantt-zoom-slider {{ width:120px; accent-color:#4f46e5; cursor:pointer; }}
        #gantt-zoom-label {{ font-weight:800; color:#4f46e5; min-width:42px; }}
        .zoom-hint {{ font-size:10px; color:#94a3b8; margin-left:auto; }}
        .status-badge {{ display:inline-block; padding:3px 6px; border-radius:9999px; font-size:9px; font-weight:700; text-align:center; width:100%; box-sizing:border-box; text-transform:uppercase; letter-spacing:0.4px; }}
        .status-pendiente {{ background:#f8fafc; color:#64748b; border:1px solid #e2e8f0; }}
        .tab-btn {{
            transition:all 0.25s ease; display:inline-flex; align-items:center; gap:8px;
            padding:10px 18px; border-radius:10px 10px 0 0; border:1px solid #cbd5e1; border-bottom:none;
            font-weight:600; font-size:13px; background:white; color:#475569; cursor:pointer;
        }}
        .tab-badge {{
            background:#e2e8f0; color:#475569; font-size:10px; font-weight:800;
            padding:2px 7px; border-radius:999px; min-width:22px; text-align:center;
        }}
        .tab-btn.tab-total.active {{ background:linear-gradient(135deg,#4f46e5,#6366f1); border-color:#4f46e5; color:white; }}
        .tab-btn.tab-total.active .tab-badge {{ background:rgba(255,255,255,0.25); color:white; }}
        .tab-btn.active {{ background:#1e293b; color:white; border-color:#1e293b; }}
        .tab-btn.active .tab-badge {{ background:rgba(255,255,255,0.2); color:white; }}
        .tab-btn:not(.active):hover {{ background:#f8fafc; color:#0f172a; border-color:#94a3b8; }}
        .tab-content {{ display:none; animation:fadeIn 0.35s ease-out; width:100%; flex-direction:column; }}
        .tab-content.active {{ display:flex; }}
        @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(6px); }} to {{ opacity:1; transform:translateY(0); }} }}
        .legend-card {{
            background:white; border:1px solid #e2e8f0; border-radius:12px; padding:20px;
            box-shadow:0 1px 3px rgba(0,0,0,0.06);
        }}
        .legend-chips {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px; }}
        .legend-chip {{
            display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600;
            color:#475569; background:#f8fafc; padding:6px 10px; border-radius:8px; border:1px solid #e2e8f0;
        }}
        .legend-chip .swatch {{ width:14px; height:10px; border-radius:3px; display:inline-block; }}
        .legend-chip .swatch.bar-def {{ background:linear-gradient(135deg,#64748b,#475569); }}
        .legend-chip .swatch.bar-mock {{ background:linear-gradient(135deg,#14b8a6,#0d9488); }}
        .legend-chip .swatch.bar-fb {{ background:linear-gradient(135deg,#06b6d4,#0891b2); }}
        .legend-chip .swatch.bar-corr {{ background:linear-gradient(135deg,#f97316,#ea580c); }}
        .legend-chip .swatch.bar-infra {{ background:linear-gradient(135deg,#3b82f6,#2563eb); }}
        .legend-chip .swatch.bar-back {{ background:linear-gradient(135deg,#8b5cf6,#7c3aed); }}
        .legend-chip .swatch.bar-front {{ background:linear-gradient(135deg,#ec4899,#db2777); }}
        .legend-chip .swatch.bar-qa {{ background:linear-gradient(135deg,#f59e0b,#d97706); }}
        #toast {{
            position:fixed; bottom:20px; right:20px; background:#10b981; color:white; padding:12px 24px;
            border-radius:10px; box-shadow:0 10px 25px rgba(0,0,0,0.15);
            transform:translateY(100px); opacity:0; transition:all 0.4s cubic-bezier(0.68,-0.55,0.265,1.55); z-index:50;
            display:flex; align-items:center; gap:8px; font-weight:500;
        }}
        #toast.show {{ transform:translateY(0); opacity:1; }}
        .btn-action {{
            font-weight:600; padding:10px 18px; border-radius:10px; shadow:md;
            transition:all 0.2s; display:inline-flex; align-items:center; gap:8px; font-size:13px;
            border:1px solid transparent; cursor:pointer;
        }}
        .btn-excel {{ background:linear-gradient(135deg,#4f46e5,#6366f1); color:white; border-color:#4338ca; }}
        .btn-excel:hover {{ filter:brightness(1.08); transform:translateY(-1px); }}
        .btn-pdf {{ background:linear-gradient(135deg,#dc2626,#b91c1c); color:white; border-color:#991b1b; }}
        .btn-pdf:hover {{ filter:brightness(1.08); transform:translateY(-1px); }}
        .btn-print {{ background:linear-gradient(135deg,#334155,#1e293b); color:white; border-color:#0f172a; }}
        .btn-print:hover {{ filter:brightness(1.1); transform:translateY(-1px); }}
        .btn-trace {{ background:linear-gradient(135deg,#0d9488,#0f766e); color:white; border-color:#0f766e; }}
        .btn-trace:hover {{ filter:brightness(1.08); transform:translateY(-1px); }}
        .btn-trace.active {{ background:linear-gradient(135deg,#115e59,#134e4a); box-shadow:0 0 0 2px rgba(13,148,136,0.35); }}
        .gantt-layout {{ display:flex; gap:0; align-items:stretch; width:100%; }}
        .gantt-main {{ flex:1; min-width:0; width:100%; display:flex; flex-direction:column; }}
        .trace-panel {{
            width:320px; flex-shrink:0; background:#f8fafc; border-right:1px solid #e2e8f0;
            display:flex; flex-direction:column; max-height:72vh; overflow:hidden;
            transition:width 0.25s ease, opacity 0.25s ease, margin 0.25s ease;
        }}
        .trace-panel.collapsed {{ display:none; }}
        .trace-panel-head {{
            display:flex; align-items:center; justify-content:space-between; padding:12px 14px;
            background:linear-gradient(135deg,#0f766e,#115e59); color:white;
        }}
        .trace-panel-head h3 {{ font-size:13px; font-weight:800; display:flex; align-items:center; gap:8px; margin:0; }}
        .trace-panel-close {{
            background:rgba(255,255,255,0.15); border:none; color:white; width:28px; height:28px;
            border-radius:8px; cursor:pointer; font-size:18px; line-height:1;
        }}
        .trace-panel-close:hover {{ background:rgba(255,255,255,0.28); }}
        .trace-coverage {{ padding:10px 14px; font-size:11px; color:#475569; border-bottom:1px solid #e2e8f0; background:white; }}
        .trace-cov-num {{ font-weight:800; color:#0f766e; font-size:14px; }}
        .trace-warn {{
            padding:8px 12px; font-size:10px; background:#fef2f2; color:#b91c1c;
            border-bottom:1px solid #fecaca;
        }}
        .trace-label {{ display:block; font-size:10px; font-weight:700; color:#64748b; padding:8px 14px 4px; text-transform:uppercase; letter-spacing:0.04em; }}
        .trace-select, .trace-search {{
            margin:0 12px 8px; padding:8px 10px; border:1px solid #cbd5e1; border-radius:8px;
            font-size:12px; width:calc(100% - 24px); background:white;
        }}
        .trace-check {{
            display:flex; align-items:center; gap:8px; font-size:11px; color:#475569;
            padding:4px 14px 8px; cursor:pointer;
        }}
        .trace-section-list {{
            flex:1; overflow-y:auto; padding:4px 8px 8px; scrollbar-width:thin;
        }}
        .trace-section-item {{
            display:block; width:100%; text-align:left; padding:8px 10px; margin-bottom:4px;
            border:1px solid #e2e8f0; border-radius:8px; background:white; cursor:pointer;
            transition:all 0.15s; font-size:11px;
        }}
        .trace-section-item:hover {{ border-color:#5eead4; background:#f0fdfa; }}
        .trace-section-item.active {{ border-color:#0d9488; background:#ccfbf1; box-shadow:0 0 0 1px #0d9488; }}
        .trace-section-item.hidden-by-filter {{ display:none; }}
        .trace-sec-head {{ display:flex; align-items:center; gap:6px; margin-bottom:3px; }}
        .trace-sec-id {{ font-size:10px; background:#e0f2fe; color:#0369a1; padding:1px 5px; border-radius:4px; }}
        .trace-sec-doc {{ font-size:9px; color:#64748b; font-weight:600; flex:1; }}
        .trace-sec-count {{
            font-size:10px; font-weight:800; background:#f1f5f9; color:#475569;
            padding:1px 6px; border-radius:999px;
        }}
        .trace-sec-title {{ display:block; font-weight:600; color:#1e293b; line-height:1.3; }}
        .trace-sec-meta {{ display:block; font-size:9px; color:#94a3b8; margin-top:2px; }}
        .trace-clear-btn {{
            margin:8px 12px; padding:8px; border:1px dashed #94a3b8; background:white;
            border-radius:8px; font-size:11px; font-weight:600; color:#475569; cursor:pointer;
        }}
        .trace-clear-btn:hover {{ background:#f1f5f9; border-color:#64748b; }}
        .trace-hint {{
            font-size:9px; color:#94a3b8; padding:0 12px 12px; line-height:1.4; margin:0;
        }}
        .trace-wrap {{ position:relative; display:inline-flex; vertical-align:middle; }}
        .trace-wrap-empty {{ color:#cbd5e1; font-size:10px; }}
        .trace-info-btn {{
            display:inline-flex; align-items:center; gap:3px; padding:1px 5px; border-radius:4px;
            border:1px solid #99f6e4; background:#f0fdfa; color:#0f766e; cursor:pointer;
            font-size:9px; font-weight:700; line-height:1.2;
        }}
        .trace-info-btn:hover, .trace-wrap:focus-within .trace-info-btn {{ background:#ccfbf1; border-color:#0d9488; }}
        .trace-count {{ font-size:8px; }}
        .trace-popover {{
            display:none !important;
        }}
        #trace-floater {{
            display:none; position:fixed; z-index:9999;
            min-width:240px; max-width:min(320px, calc(100vw - 16px)); background:#0f172a; color:#e2e8f0;
            border-radius:8px; padding:8px 10px; font-size:10px; line-height:1.4;
            box-shadow:0 10px 25px rgba(0,0,0,0.35); pointer-events:none;
        }}
        #trace-floater ul {{ margin:0; padding:0; list-style:none; }}
        #trace-floater li {{ padding:6px 0; border-bottom:1px solid #334155; }}
        #trace-floater li:last-child {{ border-bottom:none; }}
        .trace-pop-doc {{ color:#5eead4; font-weight:700; }}
        .trace-pop-title {{ color:#94a3b8; margin-top:2px; font-size:9px; }}
        .gantt-task-row.trace-dimmed {{ opacity:0.28; }}
        .gantt-task-row.trace-dimmed .bar-cell {{ opacity:0.5; }}
        .gantt-task-row.trace-hidden {{ display:none; }}
        .gantt-task-row.trace-match {{ background:#ecfdf5 !important; }}
        .gantt-task-row.trace-match .sticky-col {{ background:#ecfdf5 !important; }}
        .gantt-task-row.trace-match .bar-cell .bar-inner {{ box-shadow:0 0 0 2px #10b981, inset 0 1px 0 rgba(255,255,255,0.2); }}
        #print-meta {{ display:none; }}
        #pdf-overlay {{
            display:none; position:fixed; inset:0; background:rgba(15,23,42,0.55); z-index:100;
            align-items:center; justify-content:center; backdrop-filter:blur(4px);
        }}
        #pdf-overlay.show {{ display:flex; }}
        #pdf-overlay .box {{
            background:white; border-radius:16px; padding:28px 32px; max-width:420px; text-align:center;
            box-shadow:0 25px 50px rgba(0,0,0,0.25);
        }}
        @page {{ size:A3 landscape; margin:6mm 5mm; }}
        /* Layout compacto compartido: impresión navegador + export html2pdf */
        html.gantt-printing .gantt-banner,
        .gantt-print-export .gantt-banner {{ display:none !important; }}
        html.gantt-printing thead,
        .gantt-print-export thead {{ display:table-row-group; }}
        html.gantt-printing .trace-wrap,
        .gantt-print-export .trace-wrap {{ display:none !important; }}
        html.gantt-printing .gantt-task-row,
        .gantt-print-export .gantt-task-row {{
            height:auto !important; page-break-inside:avoid; break-inside:avoid;
        }}
        html.gantt-printing .gantt-task-row td.week-cell,
        html.gantt-printing .bar-cell,
        .gantt-print-export .gantt-task-row td.week-cell,
        .gantt-print-export .bar-cell {{
            height:auto !important; min-height:16px !important; padding:0 1px !important;
        }}
        html.gantt-printing .bar-inner,
        .gantt-print-export .bar-inner {{
            min-height:14px !important; font-size:5pt !important; padding:0 2px !important; border-radius:3px !important;
        }}
        html.gantt-printing .gantt-phase-header,
        .gantt-print-export .gantt-phase-header {{
            page-break-before:auto !important; break-before:auto !important;
            page-break-after:avoid; break-after:avoid;
        }}
        html.gantt-printing .gantt-phase-header td,
        .gantt-print-export .gantt-phase-header td {{
            padding:3px 6px !important; font-size:7.5pt !important;
        }}
        html.gantt-printing .task-name,
        .gantt-print-export .task-name {{ font-size:6.5pt !important; line-height:1.15 !important; }}
        html.gantt-printing .task-top,
        .gantt-print-export .task-top {{ gap:2px !important; margin-bottom:1px !important; }}
        html.gantt-printing .tipo-badge, html.gantt-printing .mod-badge,
        .gantt-print-export .tipo-badge, .gantt-print-export .mod-badge {{
            font-size:5.5pt !important; padding:0 3px !important;
        }}
        html.gantt-printing .task-id,
        .gantt-print-export .task-id {{ font-size:5.5pt !important; padding:0 3px !important; }}
        html.gantt-printing .resp-pill,
        .gantt-print-export .resp-pill {{ font-size:6pt !important; padding:1px 4px !important; }}
        html.gantt-printing .status-badge,
        .gantt-print-export .status-badge {{ font-size:5.5pt !important; padding:1px 3px !important; }}
        html.gantt-printing .month-row th,
        .gantt-print-export .month-row th {{ padding:3px 2px !important; }}
        html.gantt-printing .month-title,
        .gantt-print-export .month-title {{ font-size:7pt !important; }}
        html.gantt-printing .month-sub,
        .gantt-print-export .month-sub {{ font-size:5.5pt !important; }}
        html.gantt-printing .week-row th,
        .gantt-print-export .week-row th {{ padding:1px 0 !important; font-size:6pt !important; }}
        html.gantt-printing .week-num,
        .gantt-print-export .week-num {{ font-size:6pt !important; }}
        html.gantt-printing .week-date,
        .gantt-print-export .week-date {{ font-size:5pt !important; }}
        html.gantt-printing .month-corner,
        .gantt-print-export .month-corner {{ font-size:6.5pt !important; padding:3px 4px !important; }}
        @media print {{
            .no-print, #toast, #pdf-overlay, .stats-grid, .phase-timeline, .trace-panel {{ display:none !important; }}
            html, body {{ background:white !important; padding:0 !important; margin:0 !important; -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }}
            .max-w-\\[1800px\\], .page-wrap, .glass-container, .gantt-card, .gantt-main, .gantt-layout {{
                max-width:none !important; width:auto !important; box-shadow:none !important; border-radius:0 !important; border:none !important;
            }}
            .gantt-scroll {{ max-height:none !important; overflow:visible !important; width:auto !important; }}
            .tab-content {{ display:none !important; }}
            .tab-content.print-target {{ display:block !important; width:auto !important; }}
            #print-meta {{ display:block !important; padding:0 0 4px 0; border-bottom:2px solid #0f172a; margin-bottom:4px; font-size:9pt; }}
            #print-meta h2 {{ font-size:11pt; margin:0 0 2px 0; }}
            #print-meta p {{ font-size:8pt; margin:0; }}
            .sticky-col {{ position:static !important; box-shadow:none !important; }}
            .month-row th, .week-row th, .milestone-row th {{ position:static !important; }}
            html.gantt-printing .gantt-table {{
                font-size:6pt !important; width:auto !important; max-width:none !important; table-layout:fixed !important;
            }}
            html.gantt-printing .week-col, html.gantt-printing .week-cell {{
                width:var(--week-col-w) !important; min-width:var(--week-col-w) !important; max-width:var(--week-col-w) !important;
            }}
            .gantt-table th, .gantt-table td {{ padding:1px 2px !important; border:0.5pt solid #cbd5e1 !important; }}
            .bar-inner {{ -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }}
            .print-legend {{ display:block !important; margin-top:6px; font-size:6.5pt; }}
        }}
        @media print {{ .print-legend {{ display:none; }} .print-target .print-legend {{ display:block !important; }} }}
    </style>
</head>
<body class="p-4 md:p-6 lg:p-8">
    <div class="page-wrap">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-4 gap-4 no-print page-header">
            <div>
                <div class="hero-badge mb-3">
                    <i class="fa-solid fa-rocket"></i> Master Plan ERP v1 · Enterprise PDF
                </div>
                <h1 class="text-3xl font-extrabold text-slate-900">ERP Web <span class="text-slate-400 font-light">| Gantt 6 Meses</span></h1>
                <p class="text-slate-600 text-sm mt-2 max-w-3xl leading-relaxed">
                    Alcance v1 según PDF Enterprise: Core financiero + Comercial + GoSocket.
                    Def → Mock → CORR → BACK → FRONT.
                    {task_count} tareas · {person_days} persona-día · Fin planificado <strong>{go_live}</strong> · Objetivo <strong>{go_live_target}</strong>.
                </p>
            </div>
            <div class="flex flex-wrap gap-2">
                <button type="button" onclick="toggleTracePanel()" id="btn-trace" class="btn-action btn-trace" title="Mostrar/ocultar panel de trazabilidad PDF">
                    <i class="fa-solid fa-book-open"></i> Trazabilidad PDF
                </button>
                <button onclick="copyActiveTable()" class="btn-action btn-excel">
                    <i class="fa-solid fa-file-excel"></i> Copiar Excel
                </button>
                <button onclick="exportToPdf(false)" class="btn-action btn-pdf">
                    <i class="fa-solid fa-file-pdf"></i> PDF (pestaña)
                </button>
                <button onclick="exportToPdf(true)" class="btn-action btn-pdf" title="Exporta las {task_count} tareas">
                    <i class="fa-solid fa-file-pdf"></i> PDF Total
                </button>
                <button onclick="printAsPdf(currentTabId)" class="btn-action btn-print" title="A3 horizontal">
                    <i class="fa-solid fa-print"></i> Imprimir
                </button>
            </div>
        </div>

        <div id="print-meta" class="no-screen">
            <h2 id="print-meta-title">ERP v1 Web — Carta Gantt</h2>
            <p id="print-meta-sub">Almahue / Devint · Inicio 13/07/2026 · Go-live obj. {go_live_target} · Fin plan {go_live}</p>
        </div>

        <div class="flex flex-wrap gap-2 mb-3 no-print">{nav}
        </div>

        <div class="gantt-zoom-bar no-print" id="gantt-zoom-bar">
            <span class="zoom-title"><i class="fa-solid fa-magnifying-glass-plus"></i> Zoom timeline</span>
            <button type="button" class="gantt-zoom-btn" id="gantt-zoom-out" title="Alejar">−</button>
            <input type="range" id="gantt-zoom-slider" min="75" max="250" step="5" value="100" aria-label="Zoom timeline">
            <button type="button" class="gantt-zoom-btn" id="gantt-zoom-in" title="Acercar">+</button>
            <span id="gantt-zoom-label">100%</span>
            <button type="button" class="gantt-zoom-reset" id="gantt-zoom-reset">Restablecer</button>
            <span class="zoom-hint">Ctrl + rueda del mouse sobre el Gantt</span>
        </div>

        <div class="glass-container gantt-card border-t-4 border-slate-800" id="gantt-card">
            <div class="gantt-layout" id="gantt-layout">
                {trace_panel}
                <div class="gantt-main">
                    {tabs_html}
                </div>
            </div>
        </div>

        <div class="mt-6 legend-card no-print">
            <h3 class="font-bold text-lg mb-3 text-indigo-900"><i class="fa-solid fa-palette mr-2"></i>Leyenda visual</h3>
            <div class="legend-chips">
                <span class="legend-chip"><span class="swatch bar-def"></span> Definiciones</span>
                <span class="legend-chip"><span class="swatch bar-mock"></span> Mockups</span>
                <span class="legend-chip"><span class="swatch bar-fb"></span> Feedback</span>
                <span class="legend-chip"><span class="swatch bar-corr"></span> CORR mockup</span>
                <span class="legend-chip"><span class="swatch bar-infra"></span> Infra</span>
                <span class="legend-chip"><span class="swatch bar-back"></span> Backend</span>
                <span class="legend-chip"><span class="swatch bar-front"></span> Frontend</span>
                <span class="legend-chip"><span class="swatch bar-qa"></span> QA</span>
            </div>
            <p class="text-sm text-slate-600 leading-relaxed">
                Pasa el cursor sobre las barras para ver fechas y entregables.
                Usa el <strong>zoom de timeline</strong> (+/− o Ctrl+rueda) para ensanchar las columnas de semanas y leer los títulos en las barras.
                Columnas fijas al hacer scroll horizontal.
                Usa <strong>Trazabilidad PDF</strong> para filtrar tareas por capítulo del documento Enterprise;
                el icono <i class="fa-solid fa-book-open"></i> en cada fila indica a qué requisito corresponde.
            </p>
            <p class="text-xs text-slate-400 mt-3">Regenerar: <code class="bg-slate-100 px-1.5 py-0.5 rounded">python tools/generate_erp_gantt_html.py</code></p>
        </div>
    </div>

    <div id="toast"><i class="fa-solid fa-circle-check text-xl"></i><span id="toast-msg">¡Listo!</span></div>

    <div id="pdf-overlay">
        <div class="box">
            <i class="fa-solid fa-spinner fa-spin text-3xl text-indigo-600 mb-3"></i>
            <p class="font-semibold text-slate-800" id="pdf-overlay-msg">Generando PDF…</p>
            <p class="text-sm text-slate-500 mt-2">Puede tardar unos segundos (pestaña Total).</p>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script>
        const TAB_LABELS = {json.dumps(tab_labels_js, ensure_ascii=False)};
        const GANTT_STICKY_TOTAL = 496;
        const GANTT_WEEK_BASE = 34;
        const GANTT_TOTAL_WEEKS = {TOTAL_WEEKS};
        const GANTT_PRINT_PAGE_PX = 1540;

        let currentTabId = 'tab-total';
        let traceFilterSection = null;
        let traceFilterDoc = null;
        let ganttZoom = parseFloat(localStorage.getItem('ganttZoom') || '1') || 1;
        let printLayoutBackup = null;

        function getPrintTimelineLayout(pagePx) {{
            const pageW = pagePx || GANTT_PRINT_PAGE_PX;
            const weekW = Math.max(20, (pageW - GANTT_STICKY_TOTAL) / GANTT_TOTAL_WEEKS);
            const tableW = Math.round(GANTT_STICKY_TOTAL + GANTT_TOTAL_WEEKS * weekW);
            return {{ weekW, tableW, pageW: tableW }};
        }}

        function applyPrintLayoutToRoot(queryRoot, layout, styleRoot) {{
            const cssRoot = styleRoot || queryRoot;
            cssRoot.style.setProperty('--week-col-w', layout.weekW + 'px');
            queryRoot.querySelectorAll('.gantt-scroll').forEach(el => {{
                el.style.overflow = 'visible';
                el.style.maxHeight = 'none';
                el.style.width = layout.tableW + 'px';
            }});
            queryRoot.querySelectorAll('.gantt-table').forEach(el => {{
                el.style.width = layout.tableW + 'px';
            }});
            queryRoot.querySelectorAll('.sticky-col').forEach(el => {{
                el.style.position = 'static';
                el.style.boxShadow = 'none';
            }});
        }}

        function applyPrintLayout() {{
            const layout = getPrintTimelineLayout();
            printLayoutBackup = {{
                weekColW: getComputedStyle(document.documentElement).getPropertyValue('--week-col-w'),
                tableWidths: Array.from(document.querySelectorAll('.gantt-table')).map(t => t.style.width),
                scrollWidths: Array.from(document.querySelectorAll('.gantt-scroll')).map(s => s.style.width),
            }};
            document.documentElement.classList.add('gantt-printing');
            document.documentElement.style.setProperty('--week-col-w', layout.weekW + 'px');
            applyPrintLayoutToRoot(document, layout, document.documentElement);
        }}

        function restorePrintLayout() {{
            document.documentElement.classList.remove('gantt-printing');
            if (!printLayoutBackup) return;
            document.documentElement.style.setProperty('--week-col-w', printLayoutBackup.weekColW || '');
            document.querySelectorAll('.gantt-table').forEach((el, i) => {{
                el.style.width = printLayoutBackup.tableWidths[i] || '';
            }});
            document.querySelectorAll('.gantt-scroll').forEach((el, i) => {{
                el.style.width = printLayoutBackup.scrollWidths[i] || '';
                el.style.overflow = '';
                el.style.maxHeight = '';
            }});
            printLayoutBackup = null;
            syncGanttTimelineWidth();
        }}

        function syncGanttTimelineWidth() {{
            if (document.documentElement.classList.contains('gantt-printing')) return;
            const scroll = document.querySelector('.tab-content.active .gantt-scroll')
                || document.querySelector('.gantt-scroll');
            if (!scroll) return;
            const containerW = scroll.clientWidth;
            const zoomedMin = GANTT_WEEK_BASE * ganttZoom;
            const fillW = Math.max(28, (containerW - GANTT_STICKY_TOTAL) / GANTT_TOTAL_WEEKS);
            const weekW = Math.max(zoomedMin, fillW);
            const timelineW = GANTT_TOTAL_WEEKS * weekW;
            const tableW = Math.max(containerW, GANTT_STICKY_TOTAL + timelineW);
            document.documentElement.style.setProperty('--week-col-w', weekW + 'px');
            document.querySelectorAll('.gantt-table').forEach(t => {{
                t.style.width = tableW + 'px';
            }});
        }}

        function applyGanttZoom(value) {{
            ganttZoom = Math.min(2.5, Math.max(0.75, value));
            document.documentElement.style.setProperty('--gantt-zoom', String(ganttZoom));
            const slider = document.getElementById('gantt-zoom-slider');
            const label = document.getElementById('gantt-zoom-label');
            if (slider) slider.value = String(Math.round(ganttZoom * 100));
            if (label) label.textContent = Math.round(ganttZoom * 100) + '%';
            try {{ localStorage.setItem('ganttZoom', String(ganttZoom)); }} catch (e) {{}}
            syncGanttTimelineWidth();
        }}

        function initGanttZoom() {{
            applyGanttZoom(ganttZoom);
            const slider = document.getElementById('gantt-zoom-slider');
            const step = 0.1;
            document.getElementById('gantt-zoom-in')?.addEventListener('click', () => applyGanttZoom(ganttZoom + step));
            document.getElementById('gantt-zoom-out')?.addEventListener('click', () => applyGanttZoom(ganttZoom - step));
            document.getElementById('gantt-zoom-reset')?.addEventListener('click', () => applyGanttZoom(1));
            slider?.addEventListener('input', e => applyGanttZoom(Number(e.target.value) / 100));
            document.querySelectorAll('.gantt-scroll').forEach(el => {{
                el.addEventListener('wheel', e => {{
                    if (!e.ctrlKey) return;
                    e.preventDefault();
                    applyGanttZoom(ganttZoom + (e.deltaY > 0 ? -0.08 : 0.08));
                }}, {{ passive: false }});
            }});
            window.addEventListener('resize', syncGanttTimelineWidth);
            const card = document.getElementById('gantt-card');
            if (card && typeof ResizeObserver !== 'undefined') {{
                new ResizeObserver(syncGanttTimelineWidth).observe(card);
            }}
        }}

        function toggleTracePanel(forceOpen) {{
            const panel = document.getElementById('trace-panel');
            const layout = document.getElementById('gantt-layout');
            const btn = document.getElementById('btn-trace');
            const open = forceOpen === true || (forceOpen !== false && panel.classList.contains('collapsed'));
            if (open) {{
                panel.classList.remove('collapsed');
                layout.classList.add('trace-open');
                btn.classList.add('active');
            }} else {{
                panel.classList.add('collapsed');
                layout.classList.remove('trace-open');
                btn.classList.remove('active');
            }}
            setTimeout(syncGanttTimelineWidth, 50);
        }}

        function getActiveTaskRows() {{
            const tab = document.getElementById(currentTabId);
            return tab ? tab.querySelectorAll('.gantt-task-row') : [];
        }}

        function applyTraceFilter() {{
            const hideUnmatched = document.getElementById('trace-hide-unmatched').checked;
            const rows = getActiveTaskRows();
            let matchCount = 0;
            rows.forEach(row => {{
                row.classList.remove('trace-dimmed', 'trace-hidden', 'trace-match');
                if (!traceFilterSection && !traceFilterDoc) return;
                const sections = (row.dataset.traceSections || '').split(',').filter(Boolean);
                const docs = (row.dataset.traceDocs || '').split(',').filter(Boolean);
                let match = true;
                if (traceFilterSection) match = sections.includes(traceFilterSection);
                else if (traceFilterDoc) match = docs.includes(traceFilterDoc);
                if (match) {{
                    row.classList.add('trace-match');
                    matchCount++;
                }} else if (hideUnmatched) {{
                    row.classList.add('trace-hidden');
                }} else {{
                    row.classList.add('trace-dimmed');
                }}
            }});
            document.querySelectorAll('.trace-section-item').forEach(el => {{
                el.classList.toggle('active', el.dataset.sectionId === traceFilterSection);
            }});
            const btn = document.getElementById('trace-clear-btn');
            if (btn) {{
                btn.textContent = traceFilterSection || traceFilterDoc
                    ? 'Limpiar filtro (' + matchCount + ' tareas)'
                    : 'Limpiar filtro';
            }}
        }}

        function clearTraceFilter() {{
            traceFilterSection = null;
            traceFilterDoc = null;
            document.getElementById('trace-doc-filter').value = '';
            document.getElementById('trace-search').value = '';
            filterTraceSectionList();
            applyTraceFilter();
        }}

        function filterTraceSectionList() {{
            const docId = document.getElementById('trace-doc-filter').value;
            const q = (document.getElementById('trace-search').value || '').toLowerCase();
            document.querySelectorAll('.trace-section-item').forEach(el => {{
                const matchDoc = !docId || el.dataset.docId === docId;
                const text = (el.textContent || '').toLowerCase();
                const matchSearch = !q || text.includes(q);
                el.classList.toggle('hidden-by-filter', !(matchDoc && matchSearch));
            }});
        }}

        function initTracePopovers() {{
            let floater = document.getElementById('trace-floater');
            if (!floater) {{
                floater = document.createElement('div');
                floater.id = 'trace-floater';
                document.body.appendChild(floater);
            }}
            function positionFloater(wrap) {{
                const pop = wrap.querySelector('.trace-popover');
                if (!pop) return;
                floater.innerHTML = pop.innerHTML;
                floater.style.display = 'block';
                const rect = wrap.getBoundingClientRect();
                const margin = 8;
                floater.style.visibility = 'hidden';
                floater.style.display = 'block';
                const fw = floater.offsetWidth;
                const fh = floater.offsetHeight;
                let left = rect.left;
                let top = rect.bottom + 4;
                if (left + fw > window.innerWidth - margin) {{
                    left = Math.max(margin, window.innerWidth - fw - margin);
                }}
                if (top + fh > window.innerHeight - margin) {{
                    top = Math.max(margin, rect.top - fh - 4);
                }}
                floater.style.left = left + 'px';
                floater.style.top = top + 'px';
                floater.style.visibility = 'visible';
            }}
            function hideFloater() {{
                floater.style.display = 'none';
            }}
            document.querySelectorAll('.trace-wrap:not(.trace-wrap-empty)').forEach(wrap => {{
                wrap.addEventListener('mouseenter', () => positionFloater(wrap));
                wrap.addEventListener('mouseleave', hideFloater);
                wrap.addEventListener('focusin', () => positionFloater(wrap));
                wrap.addEventListener('focusout', hideFloater);
            }});
        }}

        function initTracePanel() {{
            document.querySelectorAll('.trace-section-item').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    traceFilterSection = btn.dataset.sectionId;
                    traceFilterDoc = btn.dataset.docId;
                    document.getElementById('trace-doc-filter').value = traceFilterDoc;
                    toggleTracePanel(true);
                    applyTraceFilter();
                    const row = document.querySelector(
                        '.tab-content.active .gantt-task-row[data-trace-sections*="' + traceFilterSection + '"]'
                    );
                    if (row) row.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                }});
            }});
            document.getElementById('trace-doc-filter').addEventListener('change', e => {{
                traceFilterDoc = e.target.value || null;
                traceFilterSection = null;
                filterTraceSectionList();
                applyTraceFilter();
            }});
            document.getElementById('trace-search').addEventListener('input', filterTraceSectionList);
            document.getElementById('trace-hide-unmatched').addEventListener('change', applyTraceFilter);
            document.getElementById('trace-clear-btn').addEventListener('click', clearTraceFilter);
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            initGanttZoom();
            initTracePanel();
            initTracePopovers();
        }});

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            document.getElementById(tabId.replace('tab-','btn-')).classList.add('active');
            currentTabId = tabId;
            applyTraceFilter();
            setTimeout(syncGanttTimelineWidth, 0);
        }}

        function copyActiveTable() {{
            const table = document.getElementById(currentTabId.replace('tab-','table-'));
            const range = document.createRange();
            const sel = window.getSelection();
            range.selectNode(table);
            sel.removeAllRanges();
            sel.addRange(range);
            try {{
                document.execCommand('copy');
                showToast('¡Tabla copiada! Pega en Excel con Ctrl+V.');
            }} catch (err) {{
                alert('Selecciona la tabla manualmente y presiona Ctrl+C.');
            }}
            sel.removeAllRanges();
        }}

        function showToast(msg) {{
            document.getElementById('toast-msg').textContent = msg;
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 3500);
        }}

        function setPrintTarget(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('print-target'));
            document.getElementById(tabId).classList.add('print-target');
            const label = TAB_LABELS[tabId] || tabId;
            document.getElementById('print-meta-title').textContent = 'ERP v1 Web — ' + label;
        }}

        function clearPrintTarget() {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('print-target'));
        }}

        /** Imprimir → Guardar como PDF (más legible en tablas anchas) */
        function printAsPdf(tabId) {{
            if (tabId === 'tab-total') switchTab('tab-total');
            setPrintTarget(tabId);
            applyPrintLayout();
            setTimeout(() => {{
                window.print();
            }}, 250);
            showToast('Elige "Guardar como PDF" · Horizontal · A3');
        }}

        /** Descarga directa con html2pdf (requiere internet) */
        async function downloadPdf(tabId) {{
            const overlay = document.getElementById('pdf-overlay');
            const overlayMsg = document.getElementById('pdf-overlay-msg');
            if (typeof html2pdf === 'undefined') {{
                printAsPdf(tabId);
                return;
            }}
            if (tabId === 'tab-total') switchTab('tab-total');
            await new Promise(r => setTimeout(r, 250));

            const el = document.getElementById(tabId);
            const label = (TAB_LABELS[tabId] || 'Gantt').replace(/[^a-z0-9]+/gi, '_');
            const layout = getPrintTimelineLayout();
            const exportW = layout.pageW + 32;
            const clone = el.cloneNode(true);
            clone.classList.add('gantt-print-export');
            clone.style.display = 'block';
            clone.style.width = exportW + 'px';
            clone.style.fontSize = '8px';
            applyPrintLayoutToRoot(clone, layout);
            const wrap = document.createElement('div');
            wrap.className = 'gantt-print-export';
            wrap.style.cssText = 'position:fixed;left:-9999px;top:0;width:' + exportW + 'px;background:#fff;padding:8px;';
            wrap.style.setProperty('--week-col-w', layout.weekW + 'px');
            const hdr = document.createElement('div');
            hdr.innerHTML = '<h2 style="font-size:13px;margin:0 0 2px 0;">ERP v1 Web — ' + (TAB_LABELS[tabId]||'') + '</h2>'
                + '<p style="font-size:9px;color:#64748b;margin:0 0 6px 0;">Almahue/Devint · 13/07/2026 – {go_live_target} · {task_count} tareas</p>';
            wrap.appendChild(hdr);
            wrap.appendChild(clone);
            document.body.appendChild(wrap);

            overlay.classList.add('show');
            overlayMsg.textContent = 'Generando PDF…';

            try {{
                await html2pdf().set({{
                    margin: [4, 4, 5, 4],
                    filename: 'ERP_Gantt_' + label + '.pdf',
                    image: {{ type: 'jpeg', quality: 0.92 }},
                    html2canvas: {{
                        scale: 1.5,
                        useCORS: true,
                        logging: false,
                        windowWidth: exportW,
                        scrollX: 0,
                        scrollY: 0
                    }},
                    jsPDF: {{ unit: 'mm', format: 'a3', orientation: 'landscape' }},
                    pagebreak: {{ mode: ['css', 'legacy'], avoid: ['.gantt-phase-header', '.gantt-task-row'] }}
                }}).from(wrap).save();
                showToast('PDF descargado correctamente.');
            }} catch (e) {{
                console.error(e);
                document.body.removeChild(wrap);
                overlay.classList.remove('show');
                printAsPdf(tabId);
                return;
            }}
            document.body.removeChild(wrap);
            overlay.classList.remove('show');
        }}

        function exportToPdf(useTotal) {{
            const tabId = useTotal ? 'tab-total' : currentTabId;
            downloadPdf(tabId).catch(() => printAsPdf(tabId));
        }}

        window.addEventListener('beforeprint', () => {{
            if (document.querySelector('.print-target')) applyPrintLayout();
        }});
        window.addEventListener('afterprint', () => {{
            clearPrintTarget();
            restorePrintLayout();
        }});
    </script>
</body>
</html>"""

    for out_path in OUT_PATHS:
        out_path.write_text(html, encoding="utf-8")
        print(f"Generado: {out_path} ({len(tasks)} tareas)")


if __name__ == "__main__":
    main()
