"""Capturas modo demo 1536x960 para cerrar la sesión antes/después."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
BASE = "http://localhost:5174"
VIEW = {"width": 1536, "height": 960}


def dismiss(page):
    for _ in range(3):
        page.keyboard.press("Escape")
        page.wait_for_timeout(120)


def main():
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
            temporada: 'T2026', mesContable: '08', mesRemuneracion: '08', codigo: '2026-08'
          }));
          localStorage.setItem('almahue-erp-periodo-prompted', '1');
        }"""
        )
        page.fill('input[type="email"], input[name="email"]', "admin@almahue.local")
        page.fill('input[type="password"], input[name="password"]', "Admin123!")
        page.locator('button[type="submit"]').click()
        page.wait_for_timeout(2500)
        dismiss(page)
        # forzar demo + reset store vía toggle si hace falta
        page.evaluate(
            """() => {
          localStorage.setItem('almahue-erp-demo-mode', 'true');
        }"""
        )
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(2000)
        dismiss(page)

        shots = [
            ("/insumos/ordenes-aplicacion", "despues-ordenes-aplicacion-packing.png", "Recetas packing"),
            ("/insumos/packings", "despues-packings.png", None),
            ("/admin/organigrama", "despues-organigrama.png", None),
            ("/contabilidad/asientos", "despues-asientos.png", None),
            ("/contabilidad/balance-8-columnas", "despues-balance-8.png", None),
            ("/contabilidad/estado-resultados", "despues-estado-resultados.png", None),
            ("/contabilidad/situacion-financiera", "despues-situacion-financiera.png", None),
            ("/insumos/cierre", "despues-cierre-bodega.png", None),
            ("/compras/notas-cobro", "despues-notas-cobro.png", None),
        ]
        for path, name, tab in shots:
            page.goto(f"{BASE}{path}", wait_until="domcontentloaded")
            page.wait_for_timeout(1600)
            dismiss(page)
            if tab:
                b = page.locator("button", has_text=tab)
                if b.count():
                    b.first.click(force=True)
                    page.wait_for_timeout(500)
            # comprobar toasts de error
            errs = page.locator("text=No se encontró").count()
            page.screenshot(path=str(OUT / name), full_page=False)
            print(f"OK {name} errs={errs}", flush=True)

        browser.close()
        print("DONE", flush=True)


if __name__ == "__main__":
    main()
