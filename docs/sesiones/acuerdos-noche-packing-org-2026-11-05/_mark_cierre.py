from pathlib import Path
import json
import subprocess
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
MARK = OUT.parents[2] / ".cursor" / "skills" / "almahue-antes-despues" / "marcar-nuevo.ps1"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    ctx = browser.new_context(viewport={"width": 1536, "height": 960}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto("http://localhost:5174/login", wait_until="domcontentloaded")
    page.evaluate(
        """() => {
          localStorage.setItem('almahue-erp-demo-mode', 'true');
          localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({
            temporada: '2026', mesContable: '08', mesRemuneracion: '08', codigo: '2026-08'
          }));
          localStorage.setItem('almahue-erp-periodo-prompted', '1');
        }"""
    )
    page.fill('input[type="email"]', "admin@almahue.local")
    page.fill('input[type="password"]', "Admin123!")
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(2200)
    page.goto("http://localhost:5174/insumos/cierre", wait_until="domcontentloaded")
    page.wait_for_timeout(1800)
    for _ in range(3):
        page.keyboard.press("Escape")
        page.wait_for_timeout(100)

    cands = page.evaluate(
        """() => {
          const out = [];
          for (const e of document.querySelectorAll('h1,h2,h3,h4,p,span,button,div,td,th')) {
            const t = (e.textContent || '').replace(/\\s+/g, ' ').trim();
            if (!t) continue;
            if (!/Packing|39\\.692|Materiales de exportación|Producción según Recetas/i.test(t)) continue;
            if (t.length > 90) continue;
            const r = e.getBoundingClientRect();
            if (r.width < 20 || r.height < 10) continue;
            if (r.y < 70 || r.y > 900) continue;
            out.push({
              t: t.slice(0, 80),
              box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
            });
          }
          return out.slice(0, 25);
        }"""
    )
    print(json.dumps(cands, indent=2, ensure_ascii=False))

    # Prefer KPI title "Consumo Packing" or amount card around y 120-280
    pick = None
    for c in cands:
        t = c["t"]
        x, y, w, h = c["box"]
        if "Consumo Packing" in t and w < 420 and y < 320:
            pick = [x, y, min(w, 360), max(h, 28)]
            break
    if not pick:
        for c in cands:
            if "39.692" in c["t"]:
                x, y, w, h = c["box"]
                pick = [max(0, x - 8), max(0, y - 8), min(w + 16, 360), min(h + 40, 120)]
                break
    if not pick:
        for c in cands:
            if "Producción según Recetas" in c["t"] or "Bloque 2" in c["t"]:
                x, y, w, h = c["box"]
                pick = [x, y, min(w + 40, 420), max(h, 32)]
                break

    print("PICK", pick)
    if pick:
        payload = ",".join(map(str, pick))
        subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(MARK),
                "-Image",
                str(OUT / "despues-cierre-bodega.png"),
                "-Scale",
                "1",
                "-Boxes",
                payload,
            ],
            check=True,
        )
        pin = (
            round((pick[0] + pick[2] / 2) / 1536 * 100, 1),
            round((pick[1] + pick[3] / 2) / 960 * 100, 1),
        )
        print("PIN", pin)
        pins_path = OUT / "pins.json"
        pins = json.loads(pins_path.read_text(encoding="utf-8")) if pins_path.exists() else {}
        pins["cierre"] = list(pin)
        pins_path.write_text(json.dumps(pins, indent=2), encoding="utf-8")
    browser.close()
