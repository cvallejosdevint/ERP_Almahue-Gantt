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
  const overlay = page.locator('.fixed.inset-0.z-50');
  if (await overlay.isVisible().catch(() => false)) {
    const btn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await btn.isVisible()) await btn.click();
  }
  await page.waitForTimeout(1000);

  // Switch to ALM SERVICES SPA
  const empBtn = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
  await empBtn.click();
  await page.waitForTimeout(500);
  await page.locator('li button').filter({ hasText: /SERVICES|77\.032\.639/i }).first().click();
  await page.waitForTimeout(1000);
  if (await overlay.isVisible().catch(() => false)) {
    const btn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await btn.isVisible()) await btn.click();
  }
  await page.waitForTimeout(1000);

  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(2000);

  const btnCliente = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnCliente.click();
  await page.waitForTimeout(800);

  const options = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[role="listbox"] button, [role="option"]')).map(b => ({
      text: b.innerText.trim(),
      role: b.getAttribute('role')
    }));
  });
  console.log('Options after clicking Buscar cliente…:', options);
  await browser.close();
})();
