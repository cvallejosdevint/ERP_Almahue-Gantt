const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
  await page.goto('http://localhost:5174/login');
  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'));
  await page.waitForTimeout(2000);

  // Close initial period modal
  const overlay = page.locator('.fixed.inset-0.z-50');
  if (await overlay.isVisible().catch(() => false)) {
    const btn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await btn.isVisible()) await btn.click();
    await page.waitForTimeout(1000);
  }

  // Switch to ALM SERVICES SPA
  console.log('Switching to ALM SERVICES SPA...');
  const empSelectorBtn = page.locator('header button').filter({ hasText: /ALMAHUE|SERVICES|EXPORT/i }).first();
  await empSelectorBtn.click();
  await page.waitForTimeout(500);

  const servicesBtn = page.locator('.absolute.left-0 button').filter({ hasText: /SERVICES/i }).first();
  await servicesBtn.click();
  await page.waitForTimeout(1000);

  // Set Periodo to 2026-10 in the modal
  if (await overlay.isVisible().catch(() => false)) {
    console.log('Setting period 2026-10 in modal...');
    const mes = page.getByLabel('Mes contable');
    if (await mes.isVisible().catch(() => false)) await mes.selectOption('10');
    const anio = page.getByLabel('Año');
    if (await anio.isVisible().catch(() => false)) await anio.selectOption('2026');
    await page.waitForTimeout(300);
    const btn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await btn.isVisible()) await btn.click();
    await page.waitForTimeout(1000);
  }

  // Navigate to Ventas -> Órdenes de venta
  console.log('Expanding Ventas in sidebar...');
  const ventasBtn = page.locator('aside button').filter({ hasText: 'Ventas' }).first();
  await ventasBtn.click();
  await page.waitForTimeout(500);

  console.log('Clicking Órdenes de venta...');
  const ovLink = page.locator('aside a').filter({ hasText: 'Órdenes de venta' }).first();
  await ovLink.click();
  await page.waitForTimeout(1500);

  console.log('Clicking Nueva orden...');
  const nuevaOvBtn = page.getByRole('button', { name: 'Nueva orden' }).first();
  await nuevaOvBtn.click();
  await page.waitForTimeout(1500);
  console.log('Current URL:', page.url());

  // Click Buscar cliente…
  const btnCliente = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnCliente.click();
  await page.waitForTimeout(800);

  const clientOpts = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[role="option"]')).map(b => b.innerText.trim());
  });
  console.log('Client options in ALM SERVICES SPA after client nav:', clientOpts);

  await browser.close();
})();
