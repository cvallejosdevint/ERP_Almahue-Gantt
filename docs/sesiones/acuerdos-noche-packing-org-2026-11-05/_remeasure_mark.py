"""Remide controles NUEVO en modo demo y llama marcar-nuevo.ps1."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
MARK = ROOT / ".cursor" / "skills" / "almahue-antes-despues" / "marcar-nuevo.ps1"
BASE = "http://localhost:5174"
VIEW = {"width": 1536, "height": 960}


def dismiss(page):
    for _ in range(3):
        page.keyboard.press("Escape")
        page.wait_for_timeout(120)


def box(el):
    r = el.bounding_box()
    if not r:
        return None
    return [
        round(r["x"]),
        round(r["y"]),
        round(r["width"]),
        round(r["height"]),
    ]


def fmt(boxes: list[list[int]]) -> str:
    return ";".join(",".join(str(n) for n in b) for b in boxes if b)


def mark(image: str, boxes: list[list[int]]):
    payload = fmt(boxes)
    if not payload:
        print(f"SKIP mark {image}: sin boxes")
        return
    cmd = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(MARK),
        "-Image",
        str(OUT / image),
        "-Scale",
        "1",
        "-Boxes",
        payload,
    ]
    subprocess.run(cmd, check=True)
    print(f"MARK {image} -> {payload}")


def pin_pct(b: list[int]) -> tuple[float, float]:
    x, y, w, h = b
    return round((x + w / 2) / 1536 * 100, 1), round((y + h / 2) / 960 * 100, 1)


def main():
    measures: dict = {}
    pins: dict = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        ctx = browser.new_context(viewport=VIEW, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(f"{BASE}/login", wait_until="domcontentloaded")
        page.evaluate(
            """() => {
          localStorage.setItem('almahue-erp-demo-mode', 'true');
          localStorage.setItem('almahue_organigrama_flujo_abierto', '1');
          localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({
            temporada: '2026', mesContable: '08', mesRemuneracion: '08', codigo: '2026-08'
          }));
          localStorage.setItem('almahue-erp-periodo-prompted', '1');
        }"""
        )
        page.fill('input[type="email"], input[name="email"]', "admin@almahue.local")
        page.fill('input[type="password"], input[name="password"]', "Admin123!")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2500)
        dismiss(page)
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(1800)
        dismiss(page)

        # --- Organigrama ---
        page.goto(f"{BASE}/admin/organigrama", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        help_btn = page.locator("button", has_text="Cómo funciona el organigrama")
        if help_btn.count():
            help_btn.first.click(force=True)
            page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / "despues-organigrama.png"), full_page=False)
        org = page.evaluate(
            """() => {
          const out = {};
          const h = [...document.querySelectorAll('h3')].find(e => (e.textContent||'').includes('Cómo funciona'));
          if (h) {
            const card = h.closest('div.rounded-lg') || h.closest('div');
            if (card) {
              const r = card.getBoundingClientRect();
              out.flujo = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          const close = [...document.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Cerrar');
          if (close) {
            const r = close.getBoundingClientRect();
            out.cerrar = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          const tree = [...document.querySelectorAll('h2,h3')].find(e => /organigrama|jefatura|usuarios/i.test(e.textContent||''));
          const treeCard = document.querySelector('[data-testid="organigrama-tree"]')
            || [...document.querySelectorAll('div')].find(d => (d.textContent||'').includes('Gerente') && d.querySelectorAll('button,span').length > 3);
          if (treeCard) {
            const r = treeCard.getBoundingClientRect();
            if (r.height > 80 && r.y < 900) {
              out.arbol = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(Math.min(r.height, 400))];
            }
          }
          return out;
        }"""
        )
        measures["organigrama"] = org
        mark(
            "despues-organigrama.png",
            [org.get("flujo"), org.get("cerrar")],
        )
        if org.get("flujo"):
            pins["org_flujo"] = pin_pct(org["flujo"])
        if org.get("cerrar"):
            pins["org_cerrar"] = pin_pct(org["cerrar"])
        if org.get("arbol"):
            pins["org_arbol"] = pin_pct(org["arbol"])

        # --- Packings ---
        page.goto(f"{BASE}/insumos/packings", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-packings.png"), full_page=False)
        pack = page.evaluate(
            """() => {
          const out = {};
          const nuevo = [...document.querySelectorAll('button')].find(b => (b.textContent||'').includes('Nuevo packing'));
          if (nuevo) {
            const r = nuevo.getBoundingClientRect();
            out.nuevo = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          const aviso = [...document.querySelectorAll('p,div')].find(e => {
            const t = (e.textContent||'');
            return t.includes('Flujo MJ') || (t.includes('recepción') && t.includes('packing') && t.length < 220);
          });
          if (aviso) {
            const card = aviso.closest('div.rounded-lg') || aviso;
            const r = card.getBoundingClientRect();
            out.aviso = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          return out;
        }"""
        )
        measures["packings"] = pack
        mark("despues-packings.png", [pack.get("nuevo"), pack.get("aviso")])
        if pack.get("nuevo"):
            pins["pack_nuevo"] = pin_pct(pack["nuevo"])
        if pack.get("aviso"):
            pins["pack_aviso"] = pin_pct(pack["aviso"])

        # --- OA / Recetas ---
        page.goto(f"{BASE}/insumos/ordenes-aplicacion", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        dismiss(page)
        rec = page.locator("button", has_text="Recetas packing")
        if rec.count():
            rec.first.click(force=True)
            page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "despues-ordenes-aplicacion-packing.png"), full_page=False)
        oa = page.evaluate(
            """() => {
          const out = {};
          for (const label of ['Recetas packing', 'Producción packing', 'Nueva receta']) {
            const b = [...document.querySelectorAll('button')].find(el => (el.textContent||'').includes(label));
            if (b) {
              const r = b.getBoundingClientRect();
              out[label] = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          const kpis = document.querySelector('[data-testid="resumen-consumo"]')
            || [...document.querySelectorAll('h2,h3')].find(e => (e.textContent||'').includes('Resumen'));
          if (kpis) {
            const card = kpis.closest('div.rounded-lg') || kpis.parentElement;
            if (card) {
              const r = card.getBoundingClientRect();
              out.resumen = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          return out;
        }"""
        )
        measures["oa"] = oa
        mark(
            "despues-ordenes-aplicacion-packing.png",
            [oa.get("Recetas packing"), oa.get("Producción packing"), oa.get("Nueva receta")],
        )
        for key, pin_key in [
            ("Recetas packing", "oa_recetas"),
            ("Producción packing", "oa_prod"),
            ("Nueva receta", "oa_nueva"),
        ]:
            if oa.get(key):
                pins[pin_key] = pin_pct(oa[key])

        # --- Asientos ---
        page.goto(f"{BASE}/contabilidad/asientos", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-asientos.png"), full_page=False)
        asi = page.evaluate(
            """() => {
          const headers = [...document.querySelectorAll('th')].map(e => (e.textContent||'').trim());
          const th = [...document.querySelectorAll('th')].find(e => /quién|quien|cuándo|cuando|creado/i.test(e.textContent||''));
          if (!th) return { headers: headers.slice(0, 20) };
          const r = th.getBoundingClientRect();
          return {
            quien: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
            headers: headers.slice(0, 20),
          };
        }"""
        )
        measures["asientos"] = asi
        mark("despues-asientos.png", [asi.get("quien")] if asi.get("quien") else [])
        if asi.get("quien"):
            pins["asi_quien"] = pin_pct(asi["quien"])

        # --- Balance 8 ---
        page.goto(f"{BASE}/contabilidad/balance-8-columnas", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-balance-8.png"), full_page=False)
        bal = page.evaluate(
            """() => {
          const el = [...document.querySelectorAll('p,span,div,h1,h2,h3')].find(e => {
            const t = (e.textContent||'').trim();
            return t.length > 10 && t.length < 160 && /1.?ene|enero|desde.*hasta|rango/i.test(t);
          });
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return {
            t: (el.textContent||'').trim().slice(0, 120),
            box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
          };
        }"""
        )
        measures["balance"] = bal
        if bal and bal.get("box"):
            mark("despues-balance-8.png", [bal["box"]])
            pins["bal_rango"] = pin_pct(bal["box"])

        # --- ER ---
        page.goto(f"{BASE}/contabilidad/estado-resultados", wait_until="domcontentloaded")
        page.wait_for_timeout(1600)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-estado-resultados.png"), full_page=False)
        er = page.evaluate(
            """() => {
          const el = [...document.querySelectorAll('p,span,h1,h2,h3')].find(e => {
            const t = (e.textContent||'').trim();
            return t.length > 8 && t.length < 140 && /periodo|período|agosto|resultado|mes/i.test(t);
          });
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return {
            t: (el.textContent||'').trim().slice(0, 120),
            box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
          };
        }"""
        )
        measures["er"] = er
        if er and er.get("box"):
            mark("despues-estado-resultados.png", [er["box"]])
            pins["er_periodo"] = pin_pct(er["box"])

        # --- ESF / cierre / notas: solo shot + smoke ---
        for path, name in [
            ("/contabilidad/situacion-financiera", "despues-situacion-financiera.png"),
            ("/insumos/cierre", "despues-cierre-bodega.png"),
            ("/compras/notas-cobro", "despues-notas-cobro.png"),
        ]:
            page.goto(f"{BASE}{path}", wait_until="domcontentloaded")
            page.wait_for_timeout(1400)
            dismiss(page)
            errs = page.locator("text=No se encontró").count()
            page.screenshot(path=str(OUT / name), full_page=False)
            print(f"SHOT {name} errs={errs}")

        # ESF: marcar bloque resultado del ejercicio si aparece
        page.goto(f"{BASE}/contabilidad/situacion-financiera", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        esf = page.evaluate(
            """() => {
          const el = [...document.querySelectorAll('td,th,span,div,p')].find(e =>
            /resultado del ejercicio|resultado ejercicio/i.test(e.textContent||'')
          );
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(Math.max(r.height, 28))];
        }"""
        )
        measures["esf"] = esf
        if esf:
            mark("despues-situacion-financiera.png", [esf])

        # Cierre packing
        page.goto(f"{BASE}/insumos/cierre", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        cie = page.evaluate(
            """() => {
          const el = [...document.querySelectorAll('h2,h3,button,span,p,div')].find(e => {
            const t = (e.textContent||'').trim();
            return t.length < 60 && /packing|consumo packing/i.test(t);
          });
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
        }"""
        )
        measures["cierre"] = cie
        if cie:
            mark("despues-cierre-bodega.png", [cie])

        # Notas: tipo Asoex / gasto
        page.goto(f"{BASE}/compras/notas-cobro", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        notas = page.evaluate(
            """() => {
          const el = [...document.querySelectorAll('td,span,button,div')].find(e =>
            /asoex|gasto directo|embarcador/i.test(e.textContent||'')
          );
          if (!el) return null;
          const r = el.getBoundingClientRect();
          if (r.y > 900) return null;
          return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(Math.max(r.height, 24))];
        }"""
        )
        measures["notas"] = notas
        if notas:
            mark("despues-notas-cobro.png", [notas])

        # Smoke extra: tabs OA + producción + packings count + errores
        smoke = {}
        page.goto(f"{BASE}/insumos/ordenes-aplicacion", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        smoke["oa_errs"] = page.locator("text=No se encontró").count()
        smoke["oa_tabs"] = page.evaluate(
            """() => [...document.querySelectorAll('button')].map(b => (b.textContent||'').trim()).filter(t =>
              /Órdenes de aplicación|Recetas packing|Producción packing/.test(t)
            )"""
        )
        for tab in ["Órdenes de aplicación", "Producción packing"]:
            b = page.locator("button", has_text=tab)
            if b.count():
                b.first.click(force=True)
                page.wait_for_timeout(400)
        smoke["oa_after_tabs_errs"] = page.locator("text=No se encontró").count()

        page.goto(f"{BASE}/insumos/packings", wait_until="domcontentloaded")
        page.wait_for_timeout(1000)
        smoke["packings_rows"] = page.locator("table tbody tr").count()
        smoke["packings_errs"] = page.locator("text=No se encontró").count()

        measures["smoke"] = smoke
        measures["pins"] = pins

        browser.close()

    (OUT / "measurements.json").write_text(
        json.dumps(measures, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps({"pins": pins, "smoke": measures.get("smoke")}, indent=2, ensure_ascii=False))
    print("DONE")


if __name__ == "__main__":
    main()
