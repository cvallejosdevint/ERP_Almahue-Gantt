"""Capturas despues 1536x960 - acuerdos noche 04/05-11. Sin Guardar/Contabilizar."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
BASE = "http://localhost:5174"
VIEW = {"width": 1536, "height": 960}


def shot(page, name: str):
    path = OUT / name
    page.screenshot(path=str(path), full_page=False)
    print(f"OK {name}", flush=True)


def dismiss(page):
    for _ in range(3):
        page.keyboard.press("Escape")
        page.wait_for_timeout(200)
    # botones tipicos de cerrar modal / aviso
    for sel in [
        'button:has-text("Cerrar")',
        'button:has-text("Cancelar")',
        'button:has-text("Entendido")',
        '[aria-label="Cerrar"]',
    ]:
        loc = page.locator(sel)
        if loc.count():
            try:
                loc.first.click(timeout=800)
            except Exception:
                pass


def login(page):
    page.goto(f"{BASE}/login", wait_until="domcontentloaded")
    page.wait_for_timeout(500)
    page.fill('input[type="email"], input[name="email"]', "admin@almahue.local")
    page.fill('input[type="password"], input[name="password"]', "Admin123!")
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(2500)
    dismiss(page)
    print("logged", page.url, flush=True)


def goto(page, path: str):
    page.goto(f"{BASE}{path}", wait_until="domcontentloaded")
    page.wait_for_timeout(1600)
    dismiss(page)
    page.wait_for_timeout(400)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport=VIEW, device_scale_factor=1)
        page = context.new_page()
        login(page)

        goto(page, "/admin/organigrama")
        shot(page, "despues-organigrama.png")

        goto(page, "/insumos/packings")
        shot(page, "despues-packings.png")

        goto(page, "/insumos/ordenes-aplicacion")
        dismiss(page)
        rec = page.locator("button", has_text="Recetas packing")
        if rec.count():
            rec.first.click(force=True)
            page.wait_for_timeout(600)
        shot(page, "despues-ordenes-aplicacion-packing.png")

        goto(page, "/insumos/cierre")
        shot(page, "despues-cierre-bodega.png")

        goto(page, "/contabilidad/asientos")
        shot(page, "despues-asientos.png")

        goto(page, "/contabilidad/balance-8-columnas")
        shot(page, "despues-balance-8.png")

        goto(page, "/contabilidad/estado-resultados")
        shot(page, "despues-estado-resultados.png")

        goto(page, "/contabilidad/situacion-financiera")
        shot(page, "despues-situacion-financiera.png")

        goto(page, "/compras/notas-cobro")
        shot(page, "despues-notas-cobro.png")

        goto(page, "/insumos/ordenes-aplicacion")
        dismiss(page)
        prod = page.locator("button", has_text="Producción packing")
        if prod.count():
            prod.first.click(force=True)
            page.wait_for_timeout(400)
        declare = page.locator("button", has_text="Declarar producción")
        if declare.count():
            declare.first.click(force=True)
            page.wait_for_timeout(800)
            shot(page, "despues-produccion-modal.png")
            page.keyboard.press("Escape")

        browser.close()
        print("DONE", flush=True)


if __name__ == "__main__":
    main()
