const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false
  });
  const context = await browser.newContext();
  await page.locator('input[name="email"]').click();
  await page.locator('input[name="email"]').fill('admin@almahue.local');
  await page.locator('input[name="email"]').press('Tab');
  await page.locator('input[name="password"]').fill('***');
  await page.locator('input[name="password"]').press('Enter');
  await page.getByRole('button', { name: 'Confirmar 2026-' }).click();
  await page.getByRole('button', { name: 'Modo demo' }).click();
  await page.getByRole('button', { name: 'Ventas' }).click();
  await page.getByRole('link', { name: 'Órdenes de venta' }).click();
  await page.getByRole('button', { name: 'Nueva orden' }).click();
  await page.getByRole('button', { name: 'Buscar cliente…' }).click();
  await page.getByRole('option', { name: '-7 · ALM SERVICES SPA' }).click();
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.getByRole('button', { name: 'Buscar…' }).click();
  await page.getByRole('option', { name: 'EX-CEREZA-CAJ · Cereza export' }).click();
  await page.getByRole('button', { name: 'Bodega…' }).click();
  await page.getByRole('option', { name: 'BDGCER, · disp.' }).click();
  await page.getByRole('spinbutton', { name: 'Cantidad' }).click();
  await page.getByRole('spinbutton', { name: 'Cantidad' }).press('ArrowRight');
  await page.getByRole('spinbutton', { name: 'Cantidad' }).fill('121');
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.getByRole('button', { name: 'Guardar' }).first().click();
  await page.getByRole('link', { name: 'Emitir DTE' }).click();
  await page.getByRole('button', { name: 'Facturar' }).first().click();
  await page.getByRole('button', { name: 'Confirmar y emitir' }).click();
  await page.getByRole('row', { name: '88 FA-101606909136-3709 33 ·' }).getByLabel('Contabilizar').click();
  await page.getByRole('button', { name: 'Escribe para buscar cuenta…' }).click();
  await page.getByRole('textbox', { name: 'Escribe para filtrar…' }).fill('venta');
  await page.getByRole('option', { name: '5-1-01-01-002 · Ingreso ·' }).click();
  await page.getByRole('cell', { name: 'Sin centro de costo' }).click();
  await page.getByRole('button', { name: 'Sin centro de costo' }).click();
  await page.getByRole('option', { name: '· VENTA EXPORTACIÓN CEREZAS' }).click();
  await page.getByRole('button', { name: 'Sin área de negocio' }).click();
  await page.getByRole('option', { name: 'PACK · Packing fruta export' }).click();
  await page.getByRole('button', { name: 'Guardar' }).click();
  await page.getByRole('button', { name: 'Contabilidad' }).click();
  await page.getByRole('link', { name: 'Comprobantes / asientos' }).click();
  await page.getByRole('button', { name: 'Ver' }).first().click();
  const page1Promise = page.waitForEvent('popup');
  await page.getByRole('button', { name: 'Imprimir' }).click();
  const page1 = await page1Promise;
  const page2Promise = page.waitForEvent('popup');
  await page.getByRole('button', { name: 'Imprimir' }).click();
  const page2 = await page2Promise;

  // ---------------------
  await context.close();
  await browser.close();
})();