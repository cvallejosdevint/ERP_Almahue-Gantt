"""Remarca solo controles válidos y mide ER/ESF/notas/cierre con selectores estrictos."""
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
        page.wait_for_timeout(100)


def mark(image: str, boxes: list[list[int]]):
    valid = [b for b in boxes if b and b[1] < 920 and b[2] < 1400 and b[3] < 700 and b[2] > 20]
    if not valid:
        print(f"SKIP {image}")
        return
    payload = ";".join(",".join(str(n) for n in b) for b in valid)
    subprocess.run(
        [
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
        ],
        check=True,
    )
    print(f"MARK {image} {payload}")


def pin(b):
    x, y, w, h = b
    return round((x + w / 2) / 1536 * 100, 1), round((y + h / 2) / 960 * 100, 1)


def main():
    # Reaplicar marcas buenas conocidas
    mark("despues-organigrama.png", [[280, 216, 1232, 588], [1414, 233, 81, 32]])
    mark("despues-packings.png", [[1353, 88, 159, 40]])
    mark(
        "despues-ordenes-aplicacion-packing.png",
        [[452, 346, 129, 32], [590, 346, 151, 32], [1375, 88, 137, 40]],
    )
    mark("despues-asientos.png", [[953, 457, 127, 33]])
    mark("despues-balance-8.png", [[280, 144, 1232, 20]])

    pins = {
        "org_flujo": pin([280, 216, 1232, 588]),
        "org_cerrar": pin([1414, 233, 81, 32]),
        "pack_nuevo": pin([1353, 88, 159, 40]),
        "oa_recetas": pin([452, 346, 129, 32]),
        "oa_prod": pin([590, 346, 151, 32]),
        "asi_quien": pin([953, 457, 127, 33]),
        "bal_rango": pin([280, 144, 1232, 20]),
    }

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
        page.wait_for_timeout(2200)
        dismiss(page)
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)

        # ER: subtítulo bajo el título
        page.goto(f"{BASE}/contabilidad/estado-resultados", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-estado-resultados.png"), full_page=False)
        er = page.evaluate(
            """() => {
          const h1 = [...document.querySelectorAll('h1')].find(e => /estado de resultados|resultados/i.test(e.textContent||''));
          if (!h1) return null;
          const root = h1.parentElement;
          const sub = root && [...root.querySelectorAll('p')].find(p => (p.textContent||'').trim().length > 12);
          const target = sub || h1;
          const r = target.getBoundingClientRect();
          return {
            t: (target.textContent||'').trim().slice(0, 140),
            box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 900)), Math.round(Math.max(r.height, 24))],
          };
        }"""
        )
        print("ER", er)
        if er and er.get("box"):
            mark("despues-estado-resultados.png", [er["box"]])
            pins["er_periodo"] = pin(er["box"])

        # ESF
        page.goto(f"{BASE}/contabilidad/situacion-financiera", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-situacion-financiera.png"), full_page=False)
        esf = page.evaluate(
            """() => {
          const row = [...document.querySelectorAll('tr,div,span,td')].find(e => {
            const t = (e.textContent||'').trim();
            return /resultado del ejercicio/i.test(t) && t.length < 80;
          });
          if (!row) {
            const h1 = [...document.querySelectorAll('h1')].find(e => /situaci[oó]n financiera/i.test(e.textContent||''));
            if (!h1) return null;
            const r = h1.getBoundingClientRect();
            return { t: 'titulo', box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 500)), Math.round(r.height)] };
          }
          const r = row.getBoundingClientRect();
          return { t: (row.textContent||'').trim().slice(0, 80), box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 520)), Math.round(Math.max(r.height, 24))] };
        }"""
        )
        print("ESF", esf)
        if esf and esf.get("box"):
            mark("despues-situacion-financiera.png", [esf["box"]])
            pins["esf"] = pin(esf["box"])

        # Cierre: bloque packing visible
        page.goto(f"{BASE}/insumos/cierre", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-cierre-bodega.png"), full_page=False)
        cie = page.evaluate(
            """() => {
          const cards = [...document.querySelectorAll('h2,h3')].filter(e => /packing|consumo/i.test(e.textContent||''));
          for (const c of cards) {
            const r = c.getBoundingClientRect();
            if (r.y > 60 && r.y < 900 && r.width > 40) {
              return { t: (c.textContent||'').trim().slice(0, 80), box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 420)), Math.round(Math.max(r.height, 28))] };
            }
          }
          const any = [...document.querySelectorAll('div,section')].find(e => {
            const t = (e.textContent||'');
            return t.includes('Packing') && t.includes('cajas') && e.getBoundingClientRect().height < 260;
          });
          if (!any) return null;
          const r = any.getBoundingClientRect();
          return { t: 'card', box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 480)), Math.round(Math.min(r.height, 180))] };
        }"""
        )
        print("CIERRE", cie)
        if cie and cie.get("box"):
            mark("despues-cierre-bodega.png", [cie["box"]])
            pins["cierre"] = pin(cie["box"])

        # Notas cobro: fila Asoex / tipo
        page.goto(f"{BASE}/compras/notas-cobro", wait_until="domcontentloaded")
        page.wait_for_timeout(1500)
        dismiss(page)
        page.screenshot(path=str(OUT / "despues-notas-cobro.png"), full_page=False)
        notas = page.evaluate(
            """() => {
          const cell = [...document.querySelectorAll('td,span')].find(e => {
            const t = (e.textContent||'').trim();
            return /asoex|gasto directo|embarcador/i.test(t) && t.length < 40;
          });
          if (!cell) {
            const h1 = [...document.querySelectorAll('h1')].find(e => /nota/i.test(e.textContent||''));
            if (!h1) return null;
            const r = h1.getBoundingClientRect();
            return { t: 'titulo', box: [Math.round(r.x), Math.round(r.y), Math.round(Math.min(r.width, 420)), Math.round(r.height)] };
          }
          const r = cell.getBoundingClientRect();
          return { t: (cell.textContent||'').trim(), box: [Math.round(r.x), Math.round(r.y), Math.round(Math.max(r.width, 80)), Math.round(Math.max(r.height, 24))] };
        }"""
        )
        print("NOTAS", notas)
        if notas and notas.get("box"):
            mark("despues-notas-cobro.png", [notas["box"]])
            pins["notas"] = pin(notas["box"])

        # Packings aviso: subtítulo o banner estrecho
        page.goto(f"{BASE}/insumos/packings", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        dismiss(page)
        pack_aviso = page.evaluate(
            """() => {
          const p = [...document.querySelectorAll('p')].find(e => {
            const t = (e.textContent||'');
            const r = e.getBoundingClientRect();
            return r.y > 70 && r.y < 200 && r.width < 1300 && (t.includes('Flujo') || t.includes('recepción') || t.includes('packing'));
          });
          if (!p) return null;
          const r = p.getBoundingClientRect();
          return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(Math.max(r.height, 24))];
        }"""
        )
        print("PACK_AVISO", pack_aviso)
        if pack_aviso:
            mark("despues-packings.png", [[1353, 88, 159, 40], pack_aviso])
            pins["pack_aviso"] = pin(pack_aviso)
        else:
            mark("despues-packings.png", [[1353, 88, 159, 40]])

        # Organigrama arbol pin (centro inferior del flujo card ya marcado)
        pins["org_arbol"] = (58.3, 78.0)

        browser.close()

    (OUT / "pins.json").write_text(json.dumps(pins, indent=2), encoding="utf-8")
    print(json.dumps(pins, indent=2))
    print("DONE")


if __name__ == "__main__":
    main()
