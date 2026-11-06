const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });

  // 1. Setup localStorage and login
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

  // Close period modal if it appears
  const overlay = page.locator('.fixed.inset-0.z-50');
  if (await overlay.isVisible({ timeout: 2000 }).catch(() => false)) {
    const confirmBtn = page.getByRole('button', { name: /Confirmar /i }).last();
    if (await confirmBtn.isVisible()) await confirmBtn.click();
    await page.waitForTimeout(1000);
  }

  // Go to /comercial/ordenes-venta/nueva
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(2000);

  console.log('Selecting Cliente...');
  const btnCliente = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnCliente.click();
  await page.waitForTimeout(500);

  const exportOpt = page.locator('[role="option"]').filter({ hasText: /EXPORT/i }).first();
  await exportOpt.click();
  await page.waitForTimeout(500);

  console.log('Setting fechaEmision...');
  const fechaInput = page.locator('input[type="date"]').first();
  await fechaInput.fill('2026-10-11');
  console.log('Date input value after fill:', await fechaInput.inputValue());

  const indSelect = page.getByLabel(/Indicador de venta/i);
  if (await indSelect.isVisible()) {
    await indSelect.selectOption('SERVICIO');
  }
  await page.waitForTimeout(400);

  console.log('Clicking Siguiente...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  // In table, the first column button has text 'Producto'
  console.log('Changing line type to Servicio...');
  const tipoLineaBtn = page.locator('table tbody tr').first().locator('button[aria-haspopup="listbox"]').first();
  await tipoLineaBtn.click();
  await page.waitForTimeout(400);

  const servicioOpt = page.locator('[role="option"]').filter({ hasText: /^Servicio$/i }).first();
  await servicioOpt.click();
  await page.waitForTimeout(500);

  // Now the description input should appear
  const descInput = page.locator('table tbody tr input[placeholder*="Servicio"]').first();
  await descInput.fill('Servicios de frío y procesamiento packing temporada cerezas 2026-10');

  const cantInput = page.getByLabel('Cantidad').first();
  await cantInput.fill('1');

  const precioInput = page.getByLabel('Precio unitario').first();
  await precioInput.fill('12500');
  await page.waitForTimeout(500);

  console.log('Clicking Siguiente to Step 3...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('Step 3: Reference...');
  const refTipoBtn = page.locator('button[aria-haspopup="listbox"]').filter({ hasText: /Sin referencia|referencia/i }).first();
  if (await refTipoBtn.isVisible().catch(() => false)) {
    await refTipoBtn.click();
    await page.waitForTimeout(400);
    const ocRefOpt = page.locator('[role="option"]').filter({ hasText: /Orden de compra/i }).first();
    if (await ocRefOpt.isVisible().catch(() => false)) {
      await ocRefOpt.click();
      await page.waitForTimeout(400);
    }
  }

  const refFolioInput = page.getByLabel(/Folio referencia/i);
  if (await refFolioInput.isVisible().catch(() => false)) {
    await refFolioInput.fill('OC-2026-0015');
  }

  const refFechaInput = page.getByLabel(/Fecha referencia/i);
  if (await refFechaInput.isVisible().catch(() => false)) {
    await refFechaInput.fill('2026-10-02');
  }

  console.log('Saving Orden de Venta...');
  await page.getByRole('button', { name: /^Guardar$/i }).first().click();
  await page.waitForTimeout(3000);
  console.log('Saved OV URL:', page.url());

  // Go to /comercial/emitir
  console.log('Navigating to /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(2500);

  const facturarBtns = await page.getByRole('button', { name: 'Facturar' }).all();
  console.log('Facturar buttons found on /comercial/emitir:', facturarBtns.length);

  if (facturarBtns.length > 0) {
    console.log('Clicking Facturar...');
    await facturarBtns[0].click();
    await page.waitForTimeout(2000);
    const modalText = await page.locator('.fixed.z-50, [role="dialog"]').innerText().catch(() => '');
    console.log('Modal Confirmar facturación open! Text:', modalText.slice(0, 300));
  } else {
    console.log('Table content:', await page.locator('table').innerText().catch(() => 'No table'));
  }

  await browser.close();
  console.log('SUCCESS in debug test!');
})().catch(console.error);
