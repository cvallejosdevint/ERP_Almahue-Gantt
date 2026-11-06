const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
  });

  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });

  const page = await context.newPage();

  // 1. Login as admin
  console.log('Navigating to login...');
  await page.goto('http://localhost:5174/login', { waitUntil: 'networkidle' });
  await page.fill('input[type="email"], input[name="email"], input[name="username"]', 'admin@almahue.local');
  await page.fill('input[type="password"]', 'Admin123!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(1500);

  // 2. Navigate to Plan de cuentas
  console.log('Navigating to Plan de cuentas...');
  await page.goto('http://localhost:5174/parametrizacion/plan-cuentas', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  // Expand all to show accounts with AUX and REF
  try {
    const expandBtn = page.getByRole('button', { name: /Expandir/i });
    if (await expandBtn.isVisible()) {
      await expandBtn.click();
      await page.waitForTimeout(1000);
    }
  } catch (e) {
    console.log('Could not find expand button, continuing...');
  }

  // Filter or scroll to ensure 1-1-02 or 2-1-04 is visible
  try {
    const searchInput = page.locator('input[placeholder*="Buscar"]').first();
    if (await searchInput.isVisible()) {
      await searchInput.fill('Proveedores');
      await page.waitForTimeout(1000);
    }
  } catch (e) {
    console.log('No search input found');
  }

  const outDir = path.resolve('docs/manual/capturas');
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, 'mes-contable-dia01-param-plan-cuentas.png');

  await page.screenshot({ path: outPath, fullPage: false });
  console.log(`Plan de cuentas screenshot saved to ${outPath}`);

  await browser.close();
})();

