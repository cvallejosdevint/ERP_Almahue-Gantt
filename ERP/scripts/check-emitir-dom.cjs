const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });

  await page.goto('http://localhost:5174/login');
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'false');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-SERVICES');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({
      temporada: '2026',
      mesContable: '10',
      mesRemuneracion: '10',
      codigo: '2026-10'
    }));
    localStorage.setItem('almahue-erp-periodo-prompted', '1');
  });
  await page.reload();

  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'));
  await page.waitForTimeout(1000);

  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(3000);

  const rowButtons = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('table tbody tr button')).map(b => ({
      text: b.innerText,
      title: b.title,
      html: b.outerHTML
    }));
  });
  console.log('Row buttons on /comercial/emitir:', JSON.stringify(rowButtons, null, 2));

  await browser.close();
})().catch(console.error);
