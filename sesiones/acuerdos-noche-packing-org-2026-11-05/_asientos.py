from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent
BASE = "http://localhost:5174"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    page = browser.new_context(viewport={"width": 1536, "height": 960}, device_scale_factor=1).new_page()
    page.goto(f"{BASE}/login", wait_until="domcontentloaded")
    page.fill('input[type="email"], input[name="email"]', "admin@almahue.local")
    page.fill('input[type="password"], input[name="password"]', "Admin123!")
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(2000)
    page.keyboard.press("Escape")
    page.goto(f"{BASE}/contabilidad/asientos", wait_until="domcontentloaded")
    page.wait_for_timeout(1000)
    page.keyboard.press("Escape")
    # Periodo con datos (agosto) o Todos
    todos = page.locator("button,label,span", has_text="Todos")
    if todos.count():
        todos.first.click(force=True)
        page.wait_for_timeout(1200)
    page.screenshot(path=str(OUT / "despues-asientos.png"), full_page=False)
    info = page.evaluate(
        """() => {
      const headers = [...document.querySelectorAll('th')].map(e => (e.textContent||'').trim()).filter(Boolean);
      const th = [...document.querySelectorAll('th')].find(e => /quién|quien|cuándo|cuando|creado/i.test(e.textContent||''));
      let quien = null;
      if (th) {
        const r = th.getBoundingClientRect();
        quien = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
      }
      return { headers, quien };
    }"""
    )
    print(info)
    browser.close()
