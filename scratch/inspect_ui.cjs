const { chromium } = require('E:/source/repos/Almahue/ERP/qa-e2e/node_modules/playwright-core');
const fs = require('fs');

async function measurePins() {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  await page.goto('http://localhost:5174/login');
  await page.waitForTimeout(1000);

  const emailInput = page.locator('input[type="email"], input[name="email"]').first();
  const passInput = page.locator('input[type="password"], input[name="password"]').first();
  if (await emailInput.isVisible()) {
    await emailInput.fill('admin@almahue.local');
    await passInput.fill('Admin123!');
    await page.click('button[type="submit"]');
    await page.waitForTimeout(1500);
  }

  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'false');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-EXPORT');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({
      temporada: '2026',
      mesContable: '10',
      mesRemuneracion: '10',
      codigo: '2026-10'
    }));
    localStorage.setItem('almahue-erp-periodo-prompted', '1');
  });

  await page.goto('http://localhost:5174/contratistas/traspaso');
  await page.waitForTimeout(1500);

  const card = page.locator('div', { hasText: 'Elementos de cierre' }).locator('.rounded-md').first();
  const cardBox = await card.boundingBox();
  console.log('Card Elementos de cierre box:', cardBox);

  const pins = JSON.parse(fs.readFileSync('scratch/pin_coordinates.json', 'utf8'));
  if (cardBox) {
    pins['mes-contable-dia10-ctr-traspaso-asiento']['bloqueResumenVerde'] = {
      x: Math.round(cardBox.x + cardBox.width / 2),
      y: Math.round(cardBox.y + cardBox.height / 2)
    };
  }
  console.log('Updated pins:');
  console.log(JSON.stringify(pins, null, 2));
  fs.writeFileSync('scratch/pin_coordinates.json', JSON.stringify(pins, null, 2));

  await browser.close();
}

measurePins().catch(console.error);
