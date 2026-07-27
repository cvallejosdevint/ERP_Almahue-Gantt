#!/usr/bin/env python3
"""Actualiza tablero Almahue ERP tras consolidación reunión 22/07.
Credenciales vía env TRELLO_KEY / TRELLO_TOKEN. No versionar secrets."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
BOARD = "wixKcrP0"
BASE = "https://api.trello.com/1"
IDS_PATH = Path(__file__).resolve().parent / "backups" / "trello-ids.json"

if not KEY or not TOKEN:
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN")

ids = json.loads(IDS_PATH.read_text(encoding="utf-8"))
L = ids["labels"]
LIST = ids["lists"]
ID_DEC = ids["idDec"]
ID_AGRO = ids["idAgro"]
ID_OUT = ids["idOut"]
ID_DEV = LIST.get("En desarrollo") or LIST.get("En proceso")
ID_PEND = LIST["Pendiente"]
ID_QA_DEV = LIST["En QA Devint"]


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
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise RuntimeError(f"{method} {path} → {e.code}: {err}") from e


def put_card(card_id: str, **fields):
    return api("PUT", f"/cards/{card_id}", fields)


def post_card(**fields):
    return api("POST", "/cards", fields)


def add_comment(card_id: str, text: str):
    return api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def id_labels(*names: str) -> str:
    return ",".join(L[n] for n in names if n in L)


# --- Actualización mocks existentes ---
UPDATES = {
    "6a5506270fe5f85bf4307ac5": {  # #1 Login
        "name": "[C-01] Login + empresa activa",
        "desc": """**Estado:** Sprint real (API) · UAT listo
**Fuente:** reunión 22/07 · DEC-08

## Alcance
- [REQ] Login + selector empresas con permiso
- [REQ] Empresa activa siempre visible
- [OPT] Temporada (solo si hay reportería/gestión)
- [REQ ideal] Advertencia sesión concurrente (2 personas / 1 login)

## Hecho en código
Auth JWT, sesión, selector empresa, header X-Empresa-Id.

## Pendiente
Aviso sesión concurrente; temporada útil.
""",
        "idLabels": id_labels("REQ", "Sprint Real", "DEC"),
    },
    "6a568d0c5fc4c3189b67bea1": {  # #3 Panel
        "name": "[Panel] Operativo Agrosoft (no Gestión/BI)",
        "desc": """**Estado:** Mock visual · reescrito post-reunión
**Fuente:** G-01 OUT hasta Mario

## KPIs sugeridos (reunión)
OC por aprobar (badge), proformas sin factura, facturas por recibir contratistas, TC del día (BC), alertas cierre mes.

## NO hacer
Dashboards Gestión Agrosoft / Power BI inventados. Mario vuelve en agosto.
""",
        "idLabels": id_labels("Mock", "OPT", "OUT"),
    },
    "6a568e25201839d8929a8674": {  # #4 Empresas
        "name": "[Admin] Empresas + aislamiento DEC-03",
        "desc": """**Estado:** Sprint real (API)
CRUD empresas. Aislamiento estricto por empresa activa (CC, bodegas, tarifas).
Fondos/geografía = poca relevancia; tipo terreno agrícola = revisar en permisos.
""",
        "idLabels": id_labels("REQ", "Sprint Real", "DEC"),
    },
    "6a568e73f739160fabeadf4c": {  # #5 Usuarios
        "name": "[Admin] Usuarios (~15 · DEC-08)",
        "desc": """**Estado:** Sprint real (API)
Infra ERP nuevo (no confundir con #49 del resumen 70 tarjetas — eliminada en auditoría).
Contexto: ~15 usuarios; a veces 2 personas comparten login → riesgo empresa incorrecta.
""",
        "idLabels": id_labels("REQ", "Sprint Real", "DEC"),
    },
    "6a568ebe2af3f4099b42cc15": {  # #6 Roles
        "name": "[C-05] Roles: Admin / Digitador / Intermedio",
        "desc": """**Estado:** Sprint real (parcial) · DEC-04
- Perfil **Intermedio** entre Digitador y Admin
- Roles independientes (editar A no muta B)
- Digitador: sin parametrización / traspaso / cierre
- Auditoría mínima quién/cuándo de cambios de permisos (pendiente)
Seed Intermedio/Digitador ya existe en erp_back.
""",
        "idLabels": id_labels("REQ", "Sprint Real", "DEC"),
    },
    "6a568f048f82b87faa923f45": {  # #7 Monedas
        "name": "[DEC-05] Monedas: CLP / USD / CNY / EUR",
        "desc": """**Estado:** Mock catálogo · alinear a DEC-05/06
Foco reportería: peso, dólar, yuan, euro. UF/UTM/IPC no se usan.
Relacionar con indicadores Banco Central.
""",
        "idLabels": id_labels("REQ", "DEC", "Mock"),
    },
    "6a56dc880008fd50372a09fa": {  # #8 UM
        "name": "[Catálogo] Unidades de medida (agro)",
        "desc": """**Estado:** Mock
Alinear a insumos/agro: KG, LT, CAJ, HR labor. OPT ingredientes activos sin OK cliente.
""",
        "idLabels": id_labels("Mock", "OPT"),
    },
    "6a56dcee171c9d3f7378b861": {  # #9 CC
        "name": "[C-04/DEC-03] Centros de costo · solo empresa activa",
        "desc": """**Estado:** Listado REAL (API) · alta UI aún no persiste
Bug reunión: se podían elegir CC de otra empresa.
- GET filtrado por empresa activa (incl. Super Admin vía X-Empresa-Id)
- Usado en tarifas contratista
- POST API existe; form mock del catálogo aún sin onSave → pendiente cablear create
""",
        "idLabels": id_labels("REQ", "Sprint Real", "DEC"),
    },
    "6a56dd486f710f9a72c8f914": {  # #10 Tipos doc
        "name": "[Catálogo] Tipos documento (OC, factura, NC, proforma)",
        "desc": """**Estado:** Mock · reescrito
Priorizar: OC, Factura compra, NC, Proforma contratista, Asiento.
Quitar foco cotización/NP comercial outbound (no salió en demo 22/07).
""",
        "idLabels": id_labels("Mock", "REQ"),
    },
    "6a56ddbec8142db625d510fa": {  # #11 Plan cuentas
        "name": "[K-01] Plan de cuentas (flags CC/área/especie/elemento)",
        "desc": """**Estado:** Mock
Flags: CC, área negocio, especie, variedad, elemento; «No imputable».
Parametrización ER / estado situación financiera.
""",
        "idLabels": id_labels("Mock", "REQ"),
    },
    "6a56de52f10c2c1776593f86": {  # #12 Asientos
        "name": "[K-04] Asientos + carga masiva",
        "desc": """**Estado:** Mock
Carga masiva con validación; cuadratura debe/haber; feedback por línea; advertir si falta TC del día.
""",
        "idLabels": id_labels("Mock", "REQ"),
    },
    "6a56dec8fb1a1ac94fdcd621": {  # #13 Reportes
        "name": "[K] Reportes contables (balance / ER / mayor)",
        "desc": """**Estado:** Mock
No confundir con dashboards Gestión Agrosoft (OUT, G-01 / Mario agosto).
""",
        "idLabels": id_labels("Mock", "REQ"),
    },
    "6a56df7fe3dff29cf42ad789": {  # #14 Flujo
        "name": "[Tesorería] Flujo de caja (secundario v1)",
        "desc": """**Estado:** Mock · prioridad menor que Compras/Contratistas
Apoyo tesorería; TC manual en pagos (productores).
""",
        "idLabels": id_labels("Mock", "OPT"),
    },
    "6a56dfc90311652545c4855b": {  # #15 Pagos
        "name": "[Tesorería] Pagos · TC manual",
        "desc": """**Estado:** Mock · secundario
Diferencia TC productores vs recepción; tesorería permite TC manual.
Pregunta abierta: ¿dónde está la verdad del TC? (PEND reunión)
""",
        "idLabels": id_labels("Mock", "PEND"),
    },
    "6a56dffbbf9687330c65e8b7": {  # #16 Conciliación
        "name": "[Tesorería] Conciliación bancaria (baja prioridad)",
        "desc": """**Estado:** Mock · sin foco en reunión 22/07 → backlog OPT
""",
        "idLabels": id_labels("Mock", "OPT", "OUT"),
    },
    "6a56e032ffa5359c8b895d10": {  # #17 Presupuestos
        "name": "[OUT/PEND] Presupuestos → Power BI / Mario",
        "desc": """**Estado:** Fuera foco demo · G-01
Desviación presupuesto deseada vía Power BI. No inventar módulo Gestión.
""",
        "idLabels": id_labels("OUT", "PEND"),
        "idList": ID_OUT,
        "closed": "false",
    },
    "6a56e05f97f435379103f6d9": {  # #18 Contratistas
        "name": "[Contratistas] Módulo (C-01…C-07) — epic",
        "desc": """**Estado código (22/07 tarde):**
- Listado/alta + vigencia: **REAL**
- Tarifas multi-línea + Labor/Actividad + CC empresa: **REAL (UAT)**
- Proforma/factura (C-06): **MOCK**
- Traspaso/cierre (C-07): **MOCK**

**Decisiones:** DEC-01 (no Mano Obra), DEC-03, PEND-02 (¿múltiples facturas?)
""",
        "idLabels": id_labels("REQ", "Sprint Real", "Mock"),
        "idList": ID_QA_DEV,
    },
    "6a56e09cdb55b3605f0fde7f": {  # #19 Insumos
        "name": "[P-02/I] Maestro insumos + Bodega (epic)",
        "desc": """**Estado:** Mock UI · DEC-07
Maestro Familia+Subfamilia+Descripción anti-duplicado.
Compras admin = servicios; materiales aquí.
Ampliar: Bodegas (I-01), Movimientos (I-04), NC precio factura (I-05), param contable (I-03).
Niveles almacenamiento = PEND-03 (no construir aún).
""",
        "idLabels": id_labels("Mock", "REQ", "DEC"),
    },
    "6a56e807a68a12300a6d2cbd": {  # #24 Aprobaciones
        "name": "[P-06] Aprobación OC (badge) — reemplaza workflow genérico",
        "desc": """**Estado:** Mock · reescrito
Aprobar/rechazar con líneas y CC; badge pendientes.
Correos = OPT (prefieren badge).
""",
        "idLabels": id_labels("Mock", "REQ"),
    },
    "6a5515ed340e797dac6c3082": {  # #2 Gantt
        "name": "Carta Gantt (plan 6 meses) — validar vs Agrosoft 22/07",
        "desc": """**Estado:** En QA Almahue
Plan Enterprise/PDF (Contable + Comercial) + Gantt HTML.
**Conflicto:** Gantt/PDF Enterprise priorizan Comercial/GoSocket/Presupuestos; reunión Agrosoft prioriza Contratistas → Compras → Bodega → Contabilidad BC.
Ver doc consolidación `docs/.../consolidacion-tablero-2026-07-22.md`.
""",
        "idLabels": id_labels("PEND", "Conflicto"),
    },
}

# Comercial / GoSocket → Fuera reunión
OUT_CARDS = {
    "6a56e0d0e5456db74c0efc37": ("[OUT] Mock Clientes (comercial)", "No foco demo Agrosoft 22/07. PDF Enterprise comercial ≠ prioridad reunión."),
    "6a56e743917543b1c4a1779a": ("[OUT] Mock Prospectos", "Fuera foco reunión."),
    "6a56e78c1a9286c6838183b6": ("[OUT] Mock Libro comercial", "Fuera foco reunión. Convivencia con PDF Comercial Enterprise = duda mañana."),
    "6a56e7bce93b80fedee6471c": ("[OUT] Mock Cotizaciones", "Fuera foco reunión."),
    "6a56e86990ba6e5ac5e5819b": ("[OUT] GoSocket / facturación electrónica", "No levantado como núcleo en demo. Spike SII/DTE existe en docs; no sprint Agrosoft."),
    "6a56e8af8f615e9b9f290312": ("[OUT] Reporte ejecutivo genérico", "Reemplazar por panel operativo; Gestión/BI = Mario agosto (G-01)."),
}

NEW_DECISIONES = [
    ("[DEC-01] No Mano de Obra — Labor/Actividad en Contratistas", "Usan Book. Parametrizar en Contratistas. YA en código (catálogo Labor/Actividad).", "DEC", True),
    ("[DEC-02] Eliminar Solicitud de Compra", "Ir directo a OC. Confirmar mañana con cliente.", "DEC", False),
    ("[DEC-03] Aislamiento por empresa activa", "CC/bodegas/datos. Implementado en tarifas + header X-Empresa-Id.", "DEC", True),
    ("[DEC-04] Perfil Intermedio + roles independientes", "Seed parcial; auditoría cambios permisos pendiente.", "DEC", False),
    ("[DEC-05/06] Monedas CLP/USD/CNY/EUR + Indicadores BC", "UF/UTM/IPC out. BC rellena domingos/feriados.", "DEC", False),
    ("[DEC-07] Compras=servicios / Insumos=materiales", "Maestro preferido en Insumos.", "DEC", False),
    ("[DEC-08] Sesiones compartidas (~15 usuarios)", "Ideal 1 sesión/usuario + advertencia. Pregunta costo licencias.", "DEC", False),
    ("[DEC-09] AlmaWeb + Power BI (Mario agosto)", "Gestión Agrosoft no se usa. OUT dashboards inventados.", "OUT", False),
    ("[DEC-10] Maquinaria OUT v1", "Mención verbal sin demo. No inventar UI (alucinación corregida en auditoría).", "OUT", False),
    ("[PEND-01] Afecto/Exento en OC", "¿Quitar o matching rígido? Facturas mixtas + combustible.", "PEND", False),
    ("[PEND-02] ¿Múltiples facturas por contrato contratista?", "Hoy 1:1 + bloqueo cierre. Traer ejemplos proforma/factura.", "PEND", False),
    ("[PEND-03] Niveles de almacenamiento bodega", "Validar con persona materiales. No construir aún.", "PEND", False),
    ("[PEND-04] Alcance Maquinaria / AlmaWeb / dashboards", "Mario agosto + decisión AlmaWeb integrar/reemplazar/convivir.", "PEND", False),
]

NEW_ALCANCE = [
    ("[C-03] Tarifas multi-línea + Labor/Actividad + CC", "Sprint REAL cerrado 22/07. UAT: multi-línea, delete, vigencia, catálogo, DEC-03. Ruta /contratistas/tarifas", "REQ", ID_QA_DEV, True),
    ("[C-06] Proforma → factura 1:1 + bloqueo cierre", "Mock UI. Esperar ejemplos cliente. PEND-02.", "REQ", ID_AGRO, False),
    ("[C-07] Traspaso contable + cierre mes", "Mock UI. Solo Admin; monedas PX/USD/CNY/EUR. Digitador bloqueado.", "REQ", ID_AGRO, False),
    ("[P-01] OC sin solicitud + distribución CC en tiempo real", "Mock. DEC-02. Validar suma=neto; modo Directo vs Por Hectárea (problema todo-o-nada).", "REQ", ID_AGRO, False),
    ("[P-05] Informe OC (búsqueda proveedor contabilizadas)", "Mock. Orden reciente→antigua.", "REQ", ID_AGRO, False),
    ("[P-07] Recepción OC + TC visible", "Mock. TC creación solo informativo; efectivo en recepción.", "REQ", ID_AGRO, False),
    ("[P-08] Registro compra anti-cruzado", "Mock. + política Afecto/Exento (PEND-01).", "REQ", ID_AGRO, False),
    ("[I-01] Bodegas por empresa", "Mock. DEC-03.", "REQ", ID_AGRO, False),
    ("[I-04] Movimientos bodega (entrada/traslado/devolución)", "Mock.", "REQ", ID_AGRO, False),
    ("[I-05] NC a precio factura (sin FIFO/LIFO)", "Mock. Cliente traerá ejemplos NC con diferencia precio promedio.", "REQ", ID_AGRO, False),
    ("[K-02] Elementos de costo (anular sin borrar)", "Mock.", "REQ", ID_AGRO, False),
    ("[K-03] Historial factores honorarios", "Mock. Reduce auditoría transversal global (#70).", "REQ", ID_AGRO, False),
    ("[K-05] Indicadores Banco Central", "Mock. DEC-06.", "REQ", ID_AGRO, False),
    ("[Conflicto] PDF Enterprise vs reunión Agrosoft", """**Conflicto de planificación**
- PDF Contable/Comercial Enterprise + Gantt: Comercial, GoSocket, Presupuestos, Workflow genérico.
- Reunión 22/07 + auditoría del informe 70 cards: Agrosoft 3.0 = Contratistas → Compras servicios → Bodega → Contab BC. Comercial/GoSocket OUT o diferido.
- Informe 70 cards tenía alucinaciones (Maquinaria detallada, dashboards inventados, FIFO/LIFO) — corrección en fuentes/auditoria-calidad.txt.
**Pregunta mañana:** ¿El Gantt Enterprise se replanifica o conviven dos tracks (Agrosoft ops + Enterprise comercial)?
""", "Conflicto", ID_DEC, False),
]


def main():
    print("=== Actualizando mocks ===")
    for cid, fields in UPDATES.items():
        put_card(cid, **fields)
        print("  OK", (fields.get("name", cid)[:60]).encode("ascii", "replace").decode())

    print("=== Moviendo OUT comercial ===")
    for cid, (name, desc) in OUT_CARDS.items():
        put_card(
            cid,
            name=name,
            desc=desc + "\n\nMovido a «Fuera reunión / OUT» tras consolidación 22/07.",
            idList=ID_OUT,
            idLabels=id_labels("OUT", "Mock"),
        )
        print(f"  OUT {name[:50]}")

    print("=== Decisiones / PEND ===")
    for name, desc, tag, sprint in NEW_DECISIONES:
        labels = [tag]
        if sprint:
            labels.append("Sprint Real")
        post_card(
            idList=ID_DEC,
            name=name,
            desc=desc,
            idLabels=id_labels(*labels),
            pos="bottom",
        )
        print(f"  + {name[:55]}")

    print("=== Alcance Agrosoft ===")
    for row in NEW_ALCANCE:
        name, desc, tag, id_list, sprint = row
        labels = [tag]
        if sprint:
            labels.append("Sprint Real")
        if tag == "Conflicto":
            labels = ["Conflicto", "PEND"]
        elif tag == "REQ":
            labels.append("Mock" if not sprint else "Sprint Real")
        post_card(
            idList=id_list,
            name=name,
            desc=desc,
            idLabels=id_labels(*labels),
            pos="bottom",
        )
        print(f"  + {name[:55]}")

    add_comment(
        "6a5515ed340e797dac6c3082",
        "Consolidación 22/07: se creó tarjeta [Conflicto] PDF Enterprise vs reunión Agrosoft. Revisar antes de QA Almahue final de Gantt.",
    )
    print("DONE")


if __name__ == "__main__":
    main()
