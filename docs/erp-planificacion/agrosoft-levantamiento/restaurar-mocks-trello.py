#!/usr/bin/env python3
"""Restaura mocks Trello: descripciones backup, capturas locales, comentarios Reunión 1."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN")

ROOT = Path(__file__).resolve().parents[2]  # docs/
REPO = ROOT.parent
BACKUP = Path(__file__).resolve().parent / "backups" / "trello-wixKcrP0-2026-07-22_1401.json"
CAPTURAS = REPO / "docs" / "trello-capturas-erp-mock"
LEGACY = REPO / "docs" / "erp-planificacion" / "agrosoft-levantamiento" / "pantallas-legacy"
ID_DEV = "6a54f9a0b29764593a66b1cd"
ID_PEND = "6a54f99a5153ecc06f9833b4"

BASE = "https://api.trello.com/1"


def api(method: str, path: str, data: dict | None = None):
    q = {"key": KEY, "token": TOKEN}
    body = None
    headers = {}
    if method == "GET":
        if data:
            q.update(data)
        url = f"{BASE}{path}?{urllib.parse.urlencode(q)}"
    else:
        url = f"{BASE}{path}?{urllib.parse.urlencode(q)}"
        if data is not None:
            body = urllib.parse.urlencode(data).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        raw = resp.read().decode()
        return json.loads(raw) if raw else None


def upload_file(card_id: str, filepath: Path):
    if not filepath.is_file():
        print("  skip missing", filepath.name)
        return
    url = f"{BASE}/cards/{card_id}/attachments?key={KEY}&token={TOKEN}&name={urllib.parse.quote(filepath.name)}"
    cmd = ["curl", "-s", "-S", "-X", "POST", url, "-F", f"file=@{filepath}"]
    subprocess.run(cmd, check=True, capture_output=True)
    print("  attach", filepath.name)


def add_comment(card_id: str, text: str):
    api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def delete_attachments(card_id: str):
    for att in api("GET", f"/cards/{card_id}/attachments") or []:
        api("DELETE", f"/cards/{card_id}/attachments/{att['id']}")


# idShort -> card id from backup
backup = json.loads(BACKUP.read_text(encoding="utf-8"))
BY_SHORT = {c["idShort"]: c for c in backup["cards"]}
ID_BY_SHORT = {c["idShort"]: c["id"] for c in backup["cards"]}

# Labels actuales
labels = api("GET", "/boards/wixKcrP0/labels")
L = {x["name"]: x["id"] for x in labels if x.get("name")}
MOCKUP = L.get("MockUp", "6a54f9864b98b4fe9372bc24")
LAB_SOL = L.get("Solicitudes reunión 1") or L.get("Solicitudes reunion 1")
if not LAB_SOL:
    LAB_SOL = api("POST", "/labels", {"idBoard": "6a54f9864b98b4fe9372bb74", "name": "Solicitudes reunión 1", "color": "orange"})["id"]

LAB_FUERA = L.get("Fuera Gantt F1")
if not LAB_FUERA:
    LAB_FUERA = api("POST", "/labels", {"idBoard": "6a54f9864b98b4fe9372bb74", "name": "Fuera Gantt F1", "color": "red"})["id"]


def restore_mock(id_short: int, files: list[str], reunion_comment: str | None, solicitud: bool):
    cid = ID_BY_SHORT[id_short]
    orig = BY_SHORT[id_short]
    desc = orig.get("desc") or ""
    # Pie estándar
    footer = "\n\n---\n**Fase Gantt:** F1 Mockups · **Etiqueta:** MockUp"
    if solicitud:
        footer += " · Solicitudes reunión 1"
    if desc and footer.strip() not in desc:
        desc = desc.rstrip() + footer
    label_ids = [MOCKUP]
    if solicitud:
        label_ids.append(LAB_SOL)
    api("PUT", f"/cards/{cid}", {
        "name": orig["name"].replace("—", "-").replace("–", "-") if "—" in orig["name"] else orig["name"],
        "desc": desc,
        "idList": ID_DEV,
        "idLabels": ",".join(label_ids),
        "closed": "false",
    })
    # Restaurar nombre con em dash si backup lo tenía
    api("PUT", f"/cards/{cid}", {"name": orig["name"], "desc": desc})
    print(f"#{id_short} {orig['name'][:45]}")
    delete_attachments(cid)
    for f in files:
        upload_file(cid, CAPTURAS / f)
        time.sleep(0.3)
    if reunion_comment:
        add_comment(cid, reunion_comment)
        print("  comment ok")


# Comentarios Reunión 1 (solicitudes nuevas)
COMMENTS = {
    1: """**Solicitudes Reunión 1** (demo Agrosoft · 22/07)

- [REQ] Login + selector empresas con permiso
- [REQ] Empresa activa siempre visible en pantalla
- [OPT] Temporada útil solo si hay reportería/gestión
- [DEC-08] ~15 usuarios; a veces 2 personas / 1 login → riesgo empresa incorrecta; ideal advertencia sesión concurrente""",
    3: """**Solicitudes Reunión 1** — Panel operativo (no Gestión Agrosoft)

KPIs sugeridos post-demo:
- OC por aprobar (badge)
- Proformas contratista sin factura
- Facturas por recibir contratistas
- TC del día (Banco Central)
- Alertas cierre de mes

No inventar dashboards Power BI / Gestión (Mario agosto · G-01).""",
    4: """**Solicitudes Reunión 1**

- [REQ] CRUD empresas multiempresa
- [DEC-03] Aislamiento estricto por empresa activa (datos, CC, bodegas)""",
    5: """**Solicitudes Reunión 1**

- Infra usuarios ERP (~15 usuarios)
- [DEC-08] Riesgo sesiones compartidas / empresa activa incorrecta""",
    6: """**Solicitudes Reunión 1**

- [DEC-04] Perfiles: Administrador / Digitador / **Intermedio**
- Roles independientes (editar rol A no altera rol B)
- Digitador: sin parametrización / traspaso / cierre
- Auditoría mínima cambios de permisos (quién/cuándo)""",
    7: """**Solicitudes Reunión 1**

- [DEC-05] Foco reportería: CLP, USD, CNY, EUR
- UF/UTM/IPC no se usan
- Relacionar con indicadores Banco Central (DEC-06)""",
    8: """**Solicitudes Reunión 1**

- Catálogo UM alineado a agro (KG, LT, CAJ, HR labor)
- OPT ingredientes activos (sin OK cliente aún)""",
    9: """**Solicitudes Reunión 1**

- [C-04 / DEC-03] CC **solo empresa activa** (bug cross-empresa en Agrosoft legacy)
- Vigencia de CC
- No permitir selección cross-empresa en tarifas/OC""",
    10: """**Solicitudes Reunión 1**

Priorizar tipos: OC, Factura compra, NC, Proforma contratista, Asiento.
Menor foco cotización/NP comercial outbound (no salió en demo).""",
    11: """**Solicitudes Reunión 1**

- [K-01] Flags: CC, área negocio, especie, variedad, elemento
- Cuenta «No imputable»
- Parametrización ER / estado situación financiera""",
    12: """**Solicitudes Reunión 1**

- [K-04] Carga masiva comprobantes con validación por línea
- Cuadratura debe/haber; advertir si falta TC del día""",
    13: """**Solicitudes Reunión 1**

Reportes balance / ER / mayor. No confundir con dashboards Gestión Agrosoft (OUT).""",
    14: """**Solicitudes Reunión 1**

Tesorería secundaria v1. TC manual en pagos (productores).""",
    15: """**Solicitudes Reunión 1**

Diferencia TC productores vs recepción; tesorería permite TC manual.
Pendiente validar dónde es la «verdad» del TC.""",
    18: """**Solicitudes Reunión 1**

- [C-01] CRUD contratista + vigencia (no borrar histórico); RUT único
- [DEC-01] Labor/Actividad parametrizable aquí (no Mano de Obra)
- Ver también tarjeta **Tarifas de contratista** (pantalla nueva, fuera Gantt F1)""",
    19: """**Solicitudes Reunión 1**

- [P-02 / DEC-07] Maestro Familia+Subfamilia+Descripción anti-duplicado
- Compras admin = servicios; materiales viven en Insumos/Bodega
- Ver tarjetas nuevas: Bodegas, Movimientos (fuera Gantt F1)""",
    24: """**Solicitudes Reunión 1**

- [P-06] Aprobación OC con badge de pendientes
- Aprobar/rechazar con líneas y CC visibles
- Correos automáticos = OPT (prefieren badge)""",
}

# Mocks con capturas ERP mock + solicitud reunión 1
MOCK_RESTORE = {
    1: (["01-login-lista.png"], True),
    3: (["02-dashboard-lista.png"], True),
    4: (["03-admin-empresas-lista.png", "03-admin-empresas-nuevo.png"], True),
    5: (["04-admin-usuarios-lista.png", "04-admin-usuarios-nuevo.png"], True),
    6: (["05-admin-roles-lista.png", "05-admin-roles-nuevo.png"], True),
    7: (["06-catalogos-monedas-lista.png", "06-catalogos-monedas-nuevo.png"], True),
    8: (["07-catalogos-unidades-lista.png", "07-catalogos-unidades-nuevo.png"], True),
    9: (["08-catalogos-centros-costo-lista.png", "08-catalogos-centros-costo-nuevo.png"], True),
    10: (["09-catalogos-tipos-documento-lista.png", "09-catalogos-tipos-documento-nuevo.png"], True),
    11: (["10-contabilidad-plan-cuentas-lista.png", "10-contabilidad-plan-cuentas-nuevo.png"], True),
    12: (["11-contabilidad-asientos-lista.png", "11-contabilidad-asientos-nuevo.png"], True),
    13: (["12-contabilidad-reportes-lista.png"], True),
    14: (["13-tesoreria-flujo-caja-lista.png", "13-tesoreria-flujo-caja-nuevo.png"], True),
    15: (["14-tesoreria-pagos-lista.png", "14-tesoreria-pagos-nuevo.png"], True),
    16: (["15-tesoreria-conciliacion-lista.png", "15-tesoreria-conciliacion-nuevo.png"], False),
    17: (["16-presupuestos-lista.png", "16-presupuestos-nuevo.png"], False),
    18: (["17-insumos-contratistas-lista.png", "17-insumos-contratistas-nuevo.png"], True),
    19: (["18-insumos-catalogo-lista.png", "18-insumos-catalogo-nuevo.png"], True),
    20: (["19-comercial-clientes-lista.png", "19-comercial-clientes-nuevo.png"], False),
    21: (["20-comercial-prospectos-lista.png", "20-comercial-prospectos-nuevo.png"], False),
    22: (["21-comercial-libro-lista.png", "21-comercial-libro-nuevo.png"], False),
    23: (["22-comercial-cotizaciones-lista.png", "22-comercial-cotizaciones-nuevo.png"], False),
    24: (["23-workflow-aprobaciones-lista.png", "23-workflow-aprobaciones-nuevo.png"], True),
    25: (["24-integraciones-gosocket-lista.png", "24-integraciones-gosocket-nuevo.png"], False),
    26: (["25-reportes-ejecutivo-lista.png"], False),
}

# Pantallas nuevas (Reunión 1 · no en Gantt F1)
NEW_CARDS = [
    {
        "name": "Mock — Tarifas de contratista",
        "desc": """**No contemplado en Carta Gantt F1** — identificado en Reunión 1 (demo Agrosoft).

Pantalla crítica: tabla persistente de líneas (labor, actividad, tarifa, UM, CC, vigencia).
Agregar/editar/eliminar línea sin resetear las demás.

**Ref Gantt:** MOCK-INSUMOS (solo listado contratista) · **Solicitud:** C-03
**Captura legacy reunión:** pantallas-legacy/03-tarifas-contratista.png
""",
        "files": [LEGACY / "03-tarifas-contratista.png"],
        "comment": """**Solicitudes Reunión 1**

- [C-03] Tarifas multi-línea persistentes
- [C-04 / DEC-03] CC solo empresa activa
- [DEC-01] Labor/Actividad aquí, no Mano de Obra
- Bug legacy: al agregar 2ª línea desaparece la 1ª""",
    },
    {
        "name": "Mock — Proformas y facturas (contratistas)",
        "desc": "**Fuera Gantt F1** · Reunión 1 · C-06\n\nFlujo proforma → factura. Estados Borrador/Definitiva/Facturada. Bloqueo cierre hasta asociar facturas (PEND-02).",
        "files": [],
        "comment": "**Solicitudes Reunión 1** · C-06. Cliente traerá ejemplos proforma+factura área agrícola.",
    },
    {
        "name": "Mock — Traspaso contable y cierre de mes (contratistas)",
        "desc": "**Fuera Gantt F1** · Reunión 1 · C-07\n\nSolo Administrador. Tasas CLP/USD/CNY/EUR. Digitador no cierra ni traspasa.",
        "files": [],
        "comment": "**Solicitudes Reunión 1** · C-07. Solo Administrador. Tasas CLP/USD/CNY/EUR.",
    },
    {
        "name": "Mock — Orden de compra (servicios)",
        "desc": "**Fuera Gantt F1** · Reunión 1 · P-01 / DEC-02\n\nOC sin Solicitud de Compra. Distribución CC con validación en tiempo real.",
        "files": [LEGACY / "06-orden-compra.png", LEGACY / "07-distribucion-cc.png"],
        "comment": "**Solicitudes Reunión 1** · P-01\n- Sin Solicitud de Compra\n- TC creación informativo; efectivo en recepción\n- Modo Directo vs Por Hectárea (problema todo-o-nada)",
    },
    {
        "name": "Mock — Recepción OC",
        "desc": "**Fuera Gantt F1** · Reunión 1 · P-07",
        "files": [LEGACY / "09-recepcion-oc.png"],
        "comment": "**Solicitudes Reunión 1** · P-07. TC visible en recepción; productores TC promedio.",
    },
    {
        "name": "Mock — Registro de compra (factura)",
        "desc": "**Fuera Gantt F1** · Reunión 1 · P-08 / PEND-01",
        "files": [LEGACY / "10-registro-compra.png"],
        "comment": "**Solicitudes Reunión 1** · P-08. Anti-cruzado proveedor/factura. Política Afecto/Exento pendiente.",
    },
    {
        "name": "Mock — Bodegas",
        "desc": "**Fuera Gantt F1** · Reunión 1 · I-01 / DEC-03",
        "files": [LEGACY / "12-bodegas.png"],
        "comment": "**Solicitudes Reunión 1** · I-01. Bodegas por empresa activa.",
    },
    {
        "name": "Mock — Movimientos bodega / NC devolución",
        "desc": "**Fuera Gantt F1** · Reunión 1 · I-04 / I-05",
        "files": [LEGACY / "13-nc-devolucion.png"],
        "comment": "**Solicitudes Reunión 1** · I-05. NC a precio factura; sin FIFO/LIFO.",
    },
    {
        "name": "Mock — Indicadores Banco Central",
        "desc": "**Fuera Gantt F1** · Reunión 1 · K-05 / DEC-06",
        "files": [LEGACY / "15-indicadores-bc.png"],
        "comment": "**Solicitudes Reunión 1** · K-05. Rellenar domingos/feriados. Monedas CLP/USD/CNY/EUR.",
    },
]


def archive_summary_cards():
    """Archiva las 6 tarjetas resumen en Pendiente (contenido pasa a comentarios en mocks)."""
    cards = api("GET", "/boards/wixKcrP0/cards", {"fields": "name,id,closed"})
    for c in cards:
        n = c["name"]
        if n.startswith("Solicitudes reunión 1 —") or n.startswith("Solicitudes reunion 1 —"):
            api("PUT", f"/cards/{c['id']}", {"closed": "true"})
            print("archived summary", n[:50])


def main():
    print("=== Archivar tarjetas resumen duplicadas ===")
    archive_summary_cards()

    print("\n=== Restaurar mocks #1-#26 ===")
    for id_short, (files, solicitud) in MOCK_RESTORE.items():
        restore_mock(id_short, files, COMMENTS.get(id_short), solicitud)
        time.sleep(0.5)

    # Gantt #2 — solo descripción corta, sin mockup label change
    gantt_id = ID_BY_SHORT[2]
    api("PUT", f"/cards/{gantt_id}", {
        "name": "Carta Gantt",
        "desc": "Planificación estratégica 6 meses (F0–F7).\n\n**Fase actual cliente:** F1 Mockups.\n\nReferencia: `docs/erp-planificacion/erp_gantt_devint_6_meses.html`",
        "idLabels": "",
    })
    print("#2 Carta Gantt ok")

    print("\n=== Crear mocks fuera Gantt F1 ===")
    existing = {c["name"] for c in api("GET", "/boards/wixKcrP0/cards", {"fields": "name"})}
    for spec in NEW_CARDS:
        if spec["name"] in existing:
            print("skip exists", spec["name"])
            continue
        card = api("POST", "/cards", {
            "idList": ID_DEV,
            "name": spec["name"],
            "desc": spec["desc"],
            "idLabels": f"{MOCKUP},{LAB_SOL},{LAB_FUERA}",
            "pos": "bottom",
        })
        cid = card["id"]
        print("+", spec["name"])
        for fp in spec["files"]:
            upload_file(cid, Path(fp))
            time.sleep(0.3)
        if spec.get("comment"):
            add_comment(cid, spec["comment"])
    print("\nDONE")


if __name__ == "__main__":
    main()
