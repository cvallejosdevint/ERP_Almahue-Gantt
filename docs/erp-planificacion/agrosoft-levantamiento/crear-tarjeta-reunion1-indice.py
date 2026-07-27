#!/usr/bin/env python3
"""Tarjeta índice Reunión 1 en Trello. Plantilla: reunion1-registro-trello-template.md"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

KEY = os.environ.get("TRELLO_KEY", "")
TOKEN = os.environ.get("TRELLO_TOKEN", "")
if not KEY or not TOKEN:
    sys.exit("Faltan TRELLO_KEY / TRELLO_TOKEN")

BASE = "https://api.trello.com/1"
BOARD = "wixKcrP0"
ID_QA_ALMAHUE = "6a54f9be2f15b6cbeb89dfdd"
CARD_NAME = "Reunión 1 - Registro demo (22/07/2026)"
TEMPLATE = Path(__file__).resolve().parent / "reunion1-registro-trello-template.md"
LEGACY = Path(__file__).resolve().parent / "pantallas-legacy"


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
        return
    url = f"{BASE}/cards/{card_id}/attachments?key={KEY}&token={TOKEN}&name={urllib.parse.quote(filepath.name)}"
    subprocess.run(
        ["curl", "-s", "-S", "-X", "POST", url, "-F", f"file=@{filepath}"],
        check=True,
        capture_output=True,
    )


def add_comment(card_id: str, text: str):
    api("POST", f"/cards/{card_id}/actions/comments", {"text": text})


def card_map() -> dict[str, dict]:
    cards = api("GET", f"/boards/{BOARD}/cards", {"fields": "name,shortUrl,id,closed"})
    return {c["name"]: c for c in cards if not c.get("closed")}


def find_index_card(m: dict[str, dict]) -> dict | None:
    for c in m.values():
        if "Registro demo" in c["name"] and "Reunión 1" in c["name"]:
            return c
    return None


def label(card: dict | None) -> str:
    if not card:
        return "—"
    return card["name"].replace("Mock — ", "")


def link(card: dict | None) -> str:
    if not card:
        return "—"
    return f"[{label(card)}]({card['shortUrl']})"


def refs(*cards: dict | None) -> str:
    parts = [link(c) for c in cards if c]
    return " · ".join(parts) if parts else "—"


def block(code: str, tema: str, card_line: str, *extra: str) -> str:
    lines = [f"{code} {tema}", card_line, *extra]
    return "\n".join(lines)


def build_desc(cards: dict) -> str:
    """Genera descripción con enlaces Trello; mismo contenido que reunion1-registro-trello-template.md."""
    c = cards

    def g(sub: str) -> dict | None:
        for k, v in cards.items():
            if sub.lower() in k.lower():
                return v
        return None

    keys = {
        "login": g("Mock — Inicio"),
        "panel": g("Mock — Panel"),
        "empresas": g("Mock — Empresas"),
        "usuarios": g("Mock — Usuarios"),
        "roles": g("Mock — Roles"),
        "monedas": g("Mock — Monedas"),
        "unidades": g("Mock — Unidades"),
        "cc": g("Mock — Centros de costo"),
        "tipos": g("Mock — Tipos de documento"),
        "plan": g("Mock — Plan de cuentas"),
        "asientos": g("Mock — Asientos"),
        "reportes_c": g("Mock — Reportes contables"),
        "flujo": g("Mock — Flujo de caja"),
        "pagos": g("Mock — Pagos"),
        "contratistas": g("Mock — Contratistas"),
        "catalogo": g("Mock — Catálogo de insumos"),
        "aprobaciones": g("Mock — Aprobaciones"),
        "tarifas": g("Mock — Tarifas"),
        "proformas": g("Mock — Proformas"),
        "traspaso": g("Mock — Traspaso"),
        "oc": g("Mock — Orden de compra"),
        "recepcion": g("Mock — Recepción OC"),
        "registro": g("Mock — Registro de compra"),
        "bodegas": g("Mock — Bodegas"),
        "movimientos": g("Mock — Movimientos"),
        "indicadores": g("Mock — Indicadores Banco Central"),
    }
    k = keys

    sections = [
        "Reunión 1 - Registro demo",
        "",
        "Fecha: 21/07/2026",
        "Objetivo: Ver flujo operativo, validaciones y UX del sistema actual.",
        "",
        "CONTRATISTAS",
        "",
        block("C-01", "Login / cambio empresa", refs(k["login"], k["usuarios"])),
        "",
        block("C-02", "Sesiones compartidas (~15 usuarios)", refs(k["login"], k["usuarios"])),
        "",
        block("C-03", "Tarifas multi-línea", link(k["tarifas"])),
        "",
        block("C-04", "CC solo empresa activa", refs(k["cc"], k["tarifas"])),
        "",
        block("C-05", "Perfiles Admin / Digitador / Intermedio", link(k["roles"])),
        "",
        block("C-06", "Proforma y factura 1:1", link(k["proformas"])),
        "",
        block("C-07", "Traspaso y cierre de mes", link(k["traspaso"])),
        "",
        "COMPRAS (servicios administrativos)",
        "",
        block("P-01", "OC sin Solicitud de Compra", link(k["oc"])),
        "",
        block("P-02", "Maestro artículos anti-duplicado", link(k["catalogo"])),
        "",
        block("P-03", "Distribución CC cuadratura", link(k["oc"])),
        "",
        block("P-04", "Afecto/Exento (pendiente cliente)", link(k["registro"]), "PEND-01"),
        "",
        block("P-05", "Informe OC proveedor contabilizada", link(k["oc"]), "ver comentario en tarjeta OC"),
        "",
        block("P-06", "Aprobación OC con badge", link(k["aprobaciones"])),
        "",
        block("P-07", "Recepción y TC", link(k["recepcion"])),
        "",
        block("P-08", "Registro compra anti-cruzado", link(k["registro"])),
        "",
        "INSUMOS / BODEGA",
        "",
        block("I-01", "Bodegas por empresa", link(k["bodegas"])),
        "",
        block("I-02", "Niveles almacenamiento", "PEND-03 — pendiente de pantalla (validar con materiales)"),
        "",
        block("I-03", "Param. contabilización bodega", link(k["movimientos"]), "ver comentario en tarjeta Movimientos"),
        "",
        block("I-04", "Movimientos bodega", link(k["movimientos"])),
        "",
        block("I-05", "NC a precio factura", link(k["movimientos"])),
        "",
        "CONTABILIDAD",
        "",
        block("K-01", "Plan de cuentas (flags)", link(k["plan"])),
        "",
        block("K-02", "Elementos de costo", link(k["plan"]), "ver comentario en Plan de cuentas"),
        "",
        block("K-03", "Historial factores honorarios", link(k["plan"]), "ver comentario en Plan de cuentas"),
        "",
        block("K-04", "Carga masiva comprobantes", link(k["asientos"])),
        "",
        block("K-05", "Indicadores Banco Central", link(k["indicadores"])),
        "",
        "INFRA Y CATÁLOGOS",
        "",
        block("Multiempresa / aislamiento DEC-03", "", link(k["empresas"])),
        "",
        block("Monedas CLP/USD/CNY/EUR DEC-05", "", link(k["monedas"])),
        "",
        block("UM agro", "", link(k["unidades"])),
        "",
        block("Tipos documento operativos", "", link(k["tipos"])),
        "",
        block("Panel KPIs operativos (no Power BI)", "", link(k["panel"])),
        "",
        block("Tesorería secundaria v1", "", refs(k["flujo"], k["pagos"])),
        "",
        block("Reportes contables clásicos", "", link(k["reportes_c"])),
        "",
        "PANTALLAS NUEVAS (En base a requerimientos detectados en reunión)",
        "",
        link(k["tarifas"]),
        "",
        link(k["proformas"]),
        "",
        link(k["traspaso"]),
        "",
        link(k["oc"]),
        "",
        link(k["recepcion"]),
        "",
        link(k["registro"]),
        "",
        link(k["bodegas"]),
        "",
        link(k["movimientos"]),
        "",
        link(k["indicadores"]),
        "",
        "DECISIONES FIRMES (DEC-01 a DEC-10)",
        "",
        block("DEC-01", "Sin Mano de Obra; Labor/Actividad en Contratistas", link(k["contratistas"])),
        "",
        block("DEC-02", "Sin Solicitud de Compra", link(k["oc"])),
        "",
        block("DEC-03", "Aislamiento empresa activa", refs(k["empresas"], k["cc"], k["bodegas"])),
        "",
        block("DEC-04", "Perfil Intermedio", link(k["roles"])),
        "",
        block("DEC-05", "Monedas CLP/USD/CNY/EUR", link(k["monedas"])),
        "",
        block("DEC-06", "Indicadores Banco Central", link(k["indicadores"])),
        "",
        block("DEC-07", "Compras=servicios; materiales=Insumos", refs(k["catalogo"], k["oc"])),
        "",
        block("DEC-08", "~15 usuarios / sesiones compartidas", link(k["login"])),
        "",
        block("DEC-09", "AlmaWeb + Power BI (Mario); no Gestión Agrosoft", link(k["panel"])),
        "",
        "DEC-10 Maquinaria OUT v1 (sin pantalla en v1)",
        "",
        "PENDIENTES CLIENTE",
        "",
        f"PEND-01 Afecto/Exento OC/factura: {link(k['registro'])}",
        "",
        f"PEND-02 Facturas parciales contratista: {link(k['proformas'])}",
        "",
        "PEND-03 Niveles almacenamiento (validar con materiales)",
        "",
        "PEND-04 AlmaWeb / dashboards (Mario, agosto)",
        "",
        "FUERA DE ALCANCE REUNIÓN 1",
        "",
        "Comercial Enterprise: Clientes, Prospectos, Libro, Cotizaciones, GoSocket (pantallas Gantt sin etiqueta Reunión 1)",
        "",
        "Presupuestos, Conciliación, Reporte ejecutivo (track Enterprise / BI)",
        "",
        "Gestión Agrosoft / Power BI (G-01)",
        "",
        "Maquinaria (X-01 / DEC-10)",
        "",
        "COMPROMISOS CLIENTE (próxima sesión)",
        "",
        "Ejemplos proforma + factura (área agrícola)",
        "",
        "Ejemplos NC diferencia precio promedio",
        "",
        "Contacto materiales (niveles bodega)",
    ]
    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sync-desc",
        action="store_true",
        help="Sobrescribe descripción en Trello (por defecto no toca la editada a mano)",
    )
    args = parser.parse_args()

    m = card_map()
    desc = build_desc(m)
    labels = api("GET", f"/boards/{BOARD}/labels")
    lab_sol = next((l["id"] for l in labels if l.get("name") == "Solicitudes reunión 1"), "")

    existing = find_index_card(m)
    if existing:
        print("Ya existe:", existing["shortUrl"])
        fields = {"name": CARD_NAME, "idList": ID_QA_ALMAHUE}
        if args.sync_desc:
            fields["desc"] = desc
            print("Descripción sincronizada desde plantilla.")
        else:
            print("Descripción no modificada (usar --sync-desc para regenerar con enlaces).")
        api("PUT", f"/cards/{existing['id']}", fields)
        return

    payload = {
        "name": CARD_NAME,
        "desc": desc,
        "idList": ID_QA_ALMAHUE,
        "pos": "top",
    }
    if lab_sol:
        payload["idLabels"] = lab_sol
    card = api("POST", "/cards", payload)
    print("Creada:", card["shortUrl"])


if __name__ == "__main__":
    main()
