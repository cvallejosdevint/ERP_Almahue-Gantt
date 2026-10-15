"""Playwright: generar OC (borrador / enviar) vs piso de escala. No entra a bandeja."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

FRONT = "http://localhost:5174"
API = "http://localhost:3001/api/v1"
PISO = 500000
OUT = Path(r"E:\source\repos\Almahue\docs\qa\resultados\2026-10-08-playwright-oc-cadena.json")
MD = Path(r"E:\source\repos\Almahue\docs\qa\resultados\2026-10-08-playwright-oc-cadena.md")

results: list[dict] = []
log: list[str] = []


def toast_text(page) -> str:
    loc = page.locator("[data-sonner-toast]").first
    try:
        if loc.is_visible(timeout=4000):
            return re.sub(r"\s+", " ", loc.inner_text()).strip()
    except Exception:
        pass
    return ""


def dismiss_periodo(page) -> None:
    modal = page.get_by_role("heading", name=re.compile("Seleccionar periodo", re.I))
    try:
        if not modal.is_visible(timeout=1500):
            return
    except Exception:
        return
    later = page.get_by_role("button", name=re.compile("Más tarde", re.I))
    try:
        later.click(force=True, timeout=3000)
        page.wait_for_timeout(400)
        return
    except Exception:
        pass
    page.get_by_role("button", name=re.compile("Confirmar", re.I)).click(force=True)
    page.wait_for_timeout(400)


def login(page, email: str, password: str) -> None:
    page.goto(FRONT + "/login")
    page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); }")
    page.goto(FRONT + "/login")
    page.locator('input[type="email"]').wait_for(state="visible", timeout=20000)
    page.locator('input[type="email"]').fill(email)
    page.locator('input[type="password"]').fill(password)
    page.get_by_role("button", name=re.compile("Entrar con clave", re.I)).click()
    page.wait_for_url(lambda u: "/login" not in str(u), timeout=30000)
    page.get_by_role("button", name=re.compile("Cerrar sesión", re.I)).wait_for(timeout=20000)
    dismiss_periodo(page)
    demo = page.get_by_role("button", name=re.compile(r"^Modo demo$", re.I))
    try:
        if demo.is_visible(timeout=2500):
            demo.click(force=True)
            page.wait_for_timeout(500)
            dismiss_periodo(page)
    except Exception:
        pass
    dismiss_periodo(page)


def expand_totales(page) -> None:
    enviar = page.get_by_role("button", name=re.compile("Enviar a aprobación|Confirmar sin aprobación|Guardar borrador"))
    try:
        if enviar.first.is_visible(timeout=1200):
            return
    except Exception:
        pass
    exp = page.get_by_title("Expandir panel")
    try:
        if exp.is_visible(timeout=1200):
            exp.click()
    except Exception:
        pass


def fill_oc(page, *, neto: float, moneda: str, descripcion: str) -> None:
    page.goto(FRONT + "/compras/ordenes/nueva")
    page.wait_for_timeout(800)
    dismiss_periodo(page)
    expand_totales(page)
    page.get_by_role("button", name=re.compile("Buscar proveedor", re.I)).click()
    box = page.locator('[role="listbox"] input').last
    try:
        if box.is_visible(timeout=2000):
            box.fill("a")
    except Exception:
        pass
    page.wait_for_timeout(400)
    opt = page.locator('[role="listbox"] [role="option"]').first
    if not opt.is_visible(timeout=5000):
        raise RuntimeError("Sin proveedores en el combo")
    opt.click()
    moneda_sel = page.locator("select").filter(has=page.locator('option[value="CLP"]')).first
    try:
        if moneda_sel.count():
            moneda_sel.select_option(moneda)
    except Exception:
        pass
    page.get_by_role("button", name=re.compile(r"2\. Ítems", re.I)).click()
    page.wait_for_timeout(500)
    row = page.locator(".rounded.border").filter(has_text="Descripción").first
    row.get_by_role("textbox").first.fill(descripcion)
    cuenta_btn = row.get_by_role("button", name=re.compile(r"Seleccionar", re.I))
    if cuenta_btn.count():
        cuenta_btn.first.click()
        page.wait_for_timeout(300)
        opt = page.locator("[role=listbox] [role=option]").nth(1)
        if not opt.count():
            opt = page.locator("[role=option]").nth(1)
        if opt.count():
            opt.click()
        else:
            page.locator("[role=option]").first.click()
    row.locator('input[type="number"]').fill("1")
    precio = row.get_by_role("textbox").nth(1)
    precio.click()
    precio.fill("")
    precio.fill(str(int(neto) if float(neto).is_integer() else neto))
    page.wait_for_timeout(1200)


def cadena_panel(page) -> str:
    box = page.locator("h3", has_text="Cadena de aprobación").locator("xpath=..")
    try:
        return re.sub(r"\s+", " ", box.inner_text()).strip()
    except Exception:
        return ""


def run_case(page, cid: str, *, neto: float, moneda: str, modo: str, esperado: str) -> None:
    rec = {
        "id": cid,
        "neto": neto,
        "moneda": moneda,
        "modo": modo,
        "esperado": esperado,
        "resultado": "BLOCKED",
        "toast": "",
        "cadena": "",
        "url": "",
        "nota": "",
        "enviarDisabled": None,
    }
    try:
        fill_oc(page, neto=neto, moneda=moneda, descripcion=f"{cid} neto {neto} {moneda}")
        rec["cadena"] = cadena_panel(page)
        rec["url"] = page.url
        enviar = page.get_by_role("button", name=re.compile("Enviar a aprobación|Confirmar sin aprobación"))
        borrador = page.get_by_role("button", name="Guardar borrador").last
        rec["enviarDisabled"] = enviar.is_disabled()
        if modo == "borrador":
            borrador.click()
            rec["toast"] = toast_text(page)
            rec["url"] = page.url
            ok = bool(re.search(r"Borrador guardado", rec["toast"], re.I)) or (
                "ordenes" in rec["url"] and "nueva" not in rec["url"]
            )
            rec["resultado"] = "PASS" if ok else "FAIL"
            rec["nota"] = "Guardar borrador no debe pedir cadena"
        else:
            before = page.url
            if rec["enviarDisabled"]:
                rec["toast"] = rec["cadena"]
                rec["resultado"] = "PASS" if esperado == "bloquea" else "FAIL"
                rec["nota"] = "Botón Enviar deshabilitado"
            else:
                enviar.click()
                rec["toast"] = toast_text(page)
                page.wait_for_timeout(900)
                rec["url"] = page.url
                moved = rec["url"] != before and "ordenes" in rec["url"] and "nueva" not in rec["url"]
                wait_toast = bool(re.search(r"Espere a que se calcule", rec["toast"], re.I))
                sent = bool(re.search(r"enviada a aprobación|APROBADO|aprobada", rec["toast"], re.I)) or moved
                if esperado == "bloquea":
                    rec["resultado"] = "PASS" if (wait_toast or not sent) else "FAIL"
                elif esperado in ("auto_aprobado", "pendiente"):
                    rec["resultado"] = "PASS" if sent else "FAIL"
                else:
                    rec["resultado"] = "PASS" if sent else "FAIL"
                rec["nota"] = (
                    "Toast de espera (sintoma Jose: bajo umbral no envia)"
                    if wait_toast
                    else ("El wizard persistió la OC" if sent else "No se persistió")
                )
    except Exception as e:
        rec["resultado"] = "BLOCKED"
        rec["nota"] = str(e)
    results.append(rec)
    log.append(f"{cid} {rec['resultado']} {rec['toast']}")


def session_auth(page) -> dict:
    return page.evaluate(
        """() => {
      const keys = Object.keys(localStorage);
      for (const k of keys) {
        try {
          const s = JSON.parse(localStorage.getItem(k));
          const token = s && (s.accessToken || s.token || s.access_token);
          if (token) {
            return { token, empresaId: s.empresaId || (s.user && s.user.empresaId) || '' };
          }
        } catch {}
      }
      return { token: '', empresaId: '' };
    }"""
    )


def api_json(page, method: str, path: str, body=None) -> dict:
    auth = session_auth(page)
    return page.evaluate(
        """async ({ method, url, token, empresaId, body }) => {
      const headers = { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' };
      if (empresaId) headers['x-empresa-id'] = empresaId;
      const res = await fetch(url, { method, headers, body: body ? JSON.stringify(body) : undefined });
      const text = await res.text();
      let data = text;
      try { data = JSON.parse(text); } catch {}
      return { status: res.status, data };
    }""",
        {"method": method, "url": API + path, "token": auth.get("token") or "", "empresaId": auth.get("empresaId") or "", "body": body},
    )


def write_out(piso_nodo) -> None:
    payload = {
        "dump": "ERP/backups/almahue-erp-20261008-105736.dump",
        "pisoNodo": piso_nodo,
        "pass": sum(1 for r in results if r["resultado"] == "PASS"),
        "fail": sum(1 for r in results if r["resultado"] == "FAIL"),
        "blocked": sum(1 for r in results if r["resultado"] == "BLOCKED"),
        "results": results,
        "log": log,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Playwright OC vs escalas — 2026-10-08",
        "",
        "Solo hasta generar la OC (Guardar borrador / Enviar a aprobación). Empresa ALMAHUE EXPORT. Solicitante Elena Rojas.",
        f"Respaldo BD: `ERP/backups/almahue-erp-20261008-105736.dump`.",
        "",
        f"| PASS | FAIL | BLOCKED | Total |",
        f"|---|---|---|---|",
        f"| {payload['pass']} | {payload['fail']} | {payload['blocked']} | {len(results)} |",
        "",
        "| ID | Neto | Moneda | Modo | Esperado API | Resultado | Nota |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        nota = (r.get("nota") or "").replace("|", "/")
        toast = (r.get("toast") or "").replace("|", "/")[:80]
        lines.append(
            f"| {r['id']} | {r['neto']} | {r['moneda']} | {r['modo']} | {r['esperado']} | {r['resultado']} | {nota}. {toast} |"
        )
    lines += [
        "",
        "Esperado API: bajo el piso = auto APROBADO; igual/alto = PENDIENTE. Un FAIL en bajo umbral confirma el corte del wizard.",
        "No se incluye JWT ni claves.",
    ]
    MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    piso_nodo = None
    with sync_playwright() as p:
        chrome = r"C:\Users\c\AppData\Local\ms-playwright\chromium-1243\chrome-win64\chrome.exe"
        browser = p.chromium.launch(headless=True, executable_path=chrome)
        page = browser.new_page(viewport={"width": 1536, "height": 960})
        page.set_default_timeout(25000)
        try:
            login(page, "admin@almahue.local", "Admin123!")
            escalas = api_json(page, "GET", "/escalas-aprobacion")
            data = escalas.get("data")
            lista = data if isinstance(data, list) else (data.get("items") if isinstance(data, dict) else [])
            nodo = next((n for n in lista if n.get("montoMax") in (PISO, 500000)), None)
            if not nodo:
                nodo = next((n for n in lista if n.get("montoMax") is not None), None)
            if nodo:
                piso_nodo = {"id": nodo.get("id"), "montoMax": nodo.get("montoMax"), "snapshot": nodo}
            log.append(f"escalas {len(lista)} nodo={piso_nodo}")

            login(page, "erojas@almahuexport.cl", "demo123")
            run_case(page, "T1-CLP-bajo", neto=100000, moneda="CLP", modo="enviar", esperado="auto_aprobado")
            run_case(page, "T1-CLP-igual", neto=500000, moneda="CLP", modo="enviar", esperado="pendiente")
            run_case(page, "T1-CLP-alto", neto=2500000, moneda="CLP", modo="enviar", esperado="pendiente")
            run_case(page, "T2-BOR-bajo", neto=50000, moneda="CLP", modo="borrador", esperado="borrador")
            run_case(page, "T2-BOR-igual", neto=500000, moneda="CLP", modo="borrador", esperado="borrador")
            run_case(page, "T2-BOR-alto", neto=9000000, moneda="CLP", modo="borrador", esperado="borrador")
            run_case(page, "T3-USD-bajo", neto=50, moneda="USD", modo="enviar", esperado="auto_aprobado")
            run_case(page, "T3-USD-medio", neto=520, moneda="USD", modo="enviar", esperado="pendiente")
            run_case(page, "T3-USD-alto", neto=4000, moneda="USD", modo="enviar", esperado="pendiente")

            def body_nodo(monto):
                s = piso_nodo["snapshot"]
                return {
                    "grupoId": s["grupoId"],
                    "modulo": s.get("modulo") or "Compras",
                    "usuarioId": s["usuarioId"],
                    "montoMax": monto,
                    "escalaAUsuarioId": s.get("escalaAUsuarioId"),
                    "logica": s.get("logica") or "SIMPLE",
                    "activo": True,
                }

            if piso_nodo and piso_nodo.get("id"):
                login(page, "admin@almahue.local", "Admin123!")
                cleared = api_json(page, "PUT", "/escalas-aprobacion/" + piso_nodo["id"], body_nodo(None))
                log.append(f"clear piso HTTP {cleared.get('status')} {str(cleared.get('data'))[:180]}")
                login(page, "erojas@almahuexport.cl", "demo123")
                run_case(page, "T4-SINMONTO-bajo", neto=100000, moneda="CLP", modo="enviar", esperado="pendiente")
                run_case(page, "T4-SINMONTO-igual", neto=500000, moneda="CLP", modo="enviar", esperado="pendiente")
                run_case(page, "T4-SINMONTO-alto", neto=2500000, moneda="CLP", modo="enviar", esperado="pendiente")
                login(page, "admin@almahue.local", "Admin123!")
                restored = api_json(page, "PUT", "/escalas-aprobacion/" + piso_nodo["id"], body_nodo(piso_nodo.get("montoMax") or PISO))
                log.append(f"restore piso HTTP {restored.get('status')} {str(restored.get('data'))[:180]}")
            else:
                for cid in ("T4-SINMONTO-bajo", "T4-SINMONTO-igual", "T4-SINMONTO-alto"):
                    results.append({"id": cid, "neto": None, "moneda": "CLP", "modo": "enviar", "esperado": "pendiente", "resultado": "BLOCKED", "nota": "Sin nodo 500000", "toast": "", "cadena": "", "url": ""})
        finally:
            write_out(piso_nodo)
            browser.close()


if __name__ == "__main__":
    main()
