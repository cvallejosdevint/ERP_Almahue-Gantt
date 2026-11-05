"""Smoke modo demo: pantallas del lote sin toast «No se encontró» y con filas/KPIs."""
from __future__ import annotations

import json
from playwright.sync_api import sync_playwright

BASE = "http://localhost:5174"
VIEW = {"width": 1536, "height": 960}

ROUTES = [
    ("/insumos/ordenes-aplicacion", "OA", True),
    ("/insumos/packings", "Packings", True),
    ("/admin/organigrama", "Organigrama", False),
    ("/contabilidad/asientos", "Asientos", True),
    ("/contabilidad/balance-8-columnas", "Balance8", False),
    ("/contabilidad/estado-resultados", "ER", False),
    ("/contabilidad/situacion-financiera", "ESF", False),
    ("/insumos/cierre", "Cierre", False),
    ("/compras/notas-cobro", "Notas", True),
    ("/compras/ordenes", "OC", True),
    ("/contratistas/proformas", "Proformas", True),
]


def main():
    report = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        ctx = browser.new_context(viewport=VIEW, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(f"{BASE}/login", wait_until="domcontentloaded")
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
        page.wait_for_timeout(2500)
        page.reload(wait_until="domcontentloaded")
        page.wait_for_timeout(1800)
        for _ in range(3):
            page.keyboard.press("Escape")
            page.wait_for_timeout(80)

        for path, name, expect_rows in ROUTES:
            page.goto(f"{BASE}{path}", wait_until="domcontentloaded")
            page.wait_for_timeout(1400)
            for _ in range(2):
                page.keyboard.press("Escape")
                page.wait_for_timeout(80)
            errs = page.locator("text=No se encontró").count()
            rows = page.locator("table tbody tr").count()
            empty = page.locator("text=No hay").count()
            body = page.locator("body").inner_text()[:400]
            report.append(
                {
                    "name": name,
                    "path": path,
                    "errs": errs,
                    "rows": rows,
                    "emptyHints": empty,
                    "ok": errs == 0 and (not expect_rows or rows > 0),
                }
            )
            print(f"{name}: errs={errs} rows={rows} ok={report[-1]['ok']}")

        # OA tabs variants
        page.goto(f"{BASE}/insumos/ordenes-aplicacion", wait_until="domcontentloaded")
        page.wait_for_timeout(1200)
        tabs = {}
        for tab in ["Órdenes de aplicación", "Recetas packing", "Producción packing"]:
            b = page.locator("button", has_text=tab)
            if b.count():
                b.first.click(force=True)
                page.wait_for_timeout(400)
            tabs[tab] = {
                "errs": page.locator("text=No se encontró").count(),
                "rows": page.locator("table tbody tr").count(),
            }
        report.append({"name": "OA-tabs", "tabs": tabs})
        print("OA-tabs", tabs)

        browser.close()
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
