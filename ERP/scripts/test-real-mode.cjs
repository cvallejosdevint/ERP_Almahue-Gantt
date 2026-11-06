const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });

  // Set demo mode to false BEFORE loading
  await page.goto('http://localhost:5174/login');
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'false');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-SERVICES');
  });
  await page.reload();

  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'));
  await page.waitForTimeout(2000);

  // Close period modal if open
  const overlay = page.locator('.fixed.inset-0.z-50');
  if (await overlay.isVisible().catch(() => false)) {
    const mes = page.getByLabel('Mes contable');
    if (await mes.isVisible().catch(() => false)) await mes.selectOption('10');
    const anio = page.getByLabel('Año');
    if (await anio.isVisible().catch(() => false)) await anio.selectOption('2026');
    await page.waitForTimeout(300);
    const btn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await btn.isVisible()) await btn.click();
    await page.waitForTimeout(1000);
  }

  // Go to /comercial/ordenes-venta/nueva
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(2000);

  // Click Buscar cliente…
  const btnCliente = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnCliente.click();
  await page.waitForTimeout(800);

  const clientOpts = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[role="option"]')).map(b => b.innerText.trim());
  });
  console.log('REAL API Client options in ALM SERVICES SPA:', clientOpts);

  await browser.close();
})();
