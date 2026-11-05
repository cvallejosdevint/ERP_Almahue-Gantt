"""Recaptura organigrama actualizado + medidas NUEVO."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
BASE = "http://localhost:5174"
VIEW = {"width": 1536, "height": 960}


def dismiss(page):
    for _ in range(3):
        page.keyboard.press("Escape")
        page.wait_for_timeout(150)


def main():
    measures = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        ctx = browser.new_context(viewport=VIEW, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(f"{BASE}/login", wait_until="domcontentloaded")
        page.fill('input[type="email"], input[name="email"]', "admin@almahue.local")
        page.fill('input[type="password"], input[name="password"]', "Admin123!")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2000)
        dismiss(page)

        page.evaluate("localStorage.setItem('almahue_organigrama_flujo_abierto','1')")
        page.goto(f"{BASE}/admin/organigrama", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        help_btn = page.locator("button", has_text="Cómo funciona el organigrama")
        if help_btn.count():
            help_btn.first.click(force=True)
            page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "despues-organigrama.png"), full_page=False)
        measures["organigrama"] = page.evaluate(
            """() => {
          const out = {};
          const h = [...document.querySelectorAll('h3')].find(e => (e.textContent||'').includes('Cómo funciona'));
          if (h) {
            const card = h.closest('div.rounded-lg');
            if (card) {
              const r = card.getBoundingClientRect();
              out.flujo = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          const close = [...document.querySelectorAll('button')].find(b => (b.textContent||'').includes('Cerrar'));
          if (close) {
            const r = close.getBoundingClientRect();
            out.cerrar = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          return out;
        }"""
        )

        page.goto(f"{BASE}/insumos/packings", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-packings.png"), full_page=False)
        measures["packings"] = page.evaluate(
            """() => {
          const out = {};
          const nuevo = [...document.querySelectorAll('button')].find(b => (b.textContent||'').includes('Nuevo packing'));
          if (nuevo) {
            const r = nuevo.getBoundingClientRect();
            out.nuevo = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          const nav = [...document.querySelectorAll('a')].find(a => (a.textContent||'').trim() === 'Packings');
          if (nav) {
            const r = nav.getBoundingClientRect();
            out.menu = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          const aviso = [...document.querySelectorAll('p')].find(e => (e.textContent||'').includes('Flujo MJ') || (e.textContent||'').includes('packing'));
          if (aviso) {
            const card = aviso.closest('div');
            if (card) {
              const r = card.getBoundingClientRect();
              out.aviso = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          return out;
        }"""
        )

        page.goto(f"{BASE}/insumos/ordenes-aplicacion", wait_until="domcontentloaded")
        page.wait_for_timeout(1000)
        dismiss(page)
        rec = page.locator("button", has_text="Recetas packing")
        if rec.count():
            rec.first.click(force=True)
            page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "despues-ordenes-aplicacion-packing.png"), full_page=False)
        measures["oa"] = page.evaluate(
            """() => {
          const out = {};
          for (const label of ['Recetas packing', 'Producción packing', 'Nueva receta']) {
            const b = [...document.querySelectorAll('button')].find(el => (el.textContent||'').includes(label));
            if (b) {
              const r = b.getBoundingClientRect();
              out[label] = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
            }
          }
          return out;
        }"""
        )

        page.goto(f"{BASE}/contabilidad/asientos", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-asientos.png"), full_page=False)
        measures["asientos"] = page.evaluate(
            """() => {
          const headers = [...document.querySelectorAll('th')].map(e => (e.textContent||'').trim());
          const th = [...document.querySelectorAll('th')].find(e => /quién|quien|cuándo|cuando|creado/i.test(e.textContent||''));
          if (!th) return { headers: headers.slice(0, 15) };
          const r = th.getBoundingClientRect();
          return { quien: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)], headers: headers.slice(0, 15) };
        }"""
        )

        page.goto(f"{BASE}/contabilidad/balance-8-columnas", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-balance-8.png"), full_page=False)
        measures["balance"] = page.evaluate(
            """() => {
          const candidates = [...document.querySelectorAll('p,span,div,h1,h2')].filter(e => {
            const t = (e.textContent||'').trim();
            return t.length > 8 && t.length < 140 && /1.?ene|enero|rango|periodo|período/i.test(t);
          }).slice(0, 8).map(e => {
            const r = e.getBoundingClientRect();
            return { t: (e.textContent||'').trim().slice(0, 100), box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)] };
          });
          return candidates;
        }"""
        )

        page.goto(f"{BASE}/contabilidad/estado-resultados", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-estado-resultados.png"), full_page=False)

        page.goto(f"{BASE}/contabilidad/situacion-financiera", wait_until="domcontentloaded")
        page.wait_for_timeout(1400)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-situacion-financiera.png"), full_page=False)

        page.goto(f"{BASE}/insumos/cierre", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-cierre-bodega.png"), full_page=False)
        measures["cierre"] = page.evaluate(
            """() => {
          const out = {};
          const pack = [...document.querySelectorAll('button,span,h2,h3,p')].find(e => /packing|exportaci/i.test(e.textContent||'') && (e.textContent||'').length < 80);
          if (pack) {
            const r = pack.getBoundingClientRect();
            out.packing = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
          }
          return out;
        }"""
        )

        page.goto(f"{BASE}/compras/notas-cobro", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-notas-cobro.png"), full_page=False)

        browser.close()

    (OUT / "measurements.json").write_text(json.dumps(measures, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(measures, indent=2, ensure_ascii=False))
    print("DONE")


if __name__ == "__main__":
    main()
