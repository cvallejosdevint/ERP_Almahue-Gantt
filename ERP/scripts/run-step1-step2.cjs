const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

async function main() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 }
  });
  const page = await context.newPage();
  page.setDefaultTimeout(30000);

  async function handlePeriodoModal() {
    try {
      // Wait for any modal overlay if it appears
      const overlay = page.locator('.fixed.inset-0.z-50');
      if (await overlay.isVisible({ timeout: 5000 }).catch(() => false)) {
        console.log('Overlay detected, content:', (await overlay.innerText().catch(() => '')).slice(0, 200));
        const anioSelect = page.getByLabel('Año');
        if (await anioSelect.isVisible({ timeout: 1000 }).catch(() => false)) {
          await anioSelect.selectOption('2026').catch(() => {});
        }
        const mesSelect = page.getByLabel('Mes contable');
        if (await mesSelect.isVisible({ timeout: 1000 }).catch(() => false)) {
          await mesSelect.selectOption('10').catch(() => {});
        }
        await page.waitForTimeout(400);
        const confirmBtn = page.getByRole('button', { name: /Confirmar /i }).last();
        if (await confirmBtn.isVisible({ timeout: 1000 }).catch(() => false)) {
          console.log('Clicking confirm button:', await confirmBtn.innerText());
          await confirmBtn.click().catch(() => {});
        } else {
          const masTarde = page.getByRole('button', { name: /Más tarde/i });
          if (await masTarde.isVisible().catch(() => false)) {
            await masTarde.click().catch(() => {});
          }
        }
        await page.waitForTimeout(1000);
      } else {
        console.log('No overlay detected');
      }
    } catch (e) {
      console.log('handlePeriodoModal error:', e.message);
    }
  }

  // 1. Login
  console.log('Logging in...');
  await page.goto('http://localhost:5174/login');
  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'), { timeout: 30000 });
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  // 2. Switch to ALM SERVICES SPA
  console.log('Switching to ALM SERVICES SPA...');
  const empBtn = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
  await empBtn.click();
  await page.waitForTimeout(500);
  const servicesOpt = page.locator('li button').filter({ hasText: /SERVICES|77\.032\.639/i }).first();
  await servicesOpt.click();
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  // 3. Navigate to Nueva Orden de Venta
  console.log('Navigating to /comercial/ordenes-venta/nueva...');
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(1500);

  // Step 1: Datos generales y receptor
  console.log('Filling Step 1...');
  // Select Cliente: ALMAHUE EXPORT SPA
  const clienteBox = page.locator('div, label').filter({ hasText: /^Cliente$/i }).first();
  const selectBtn = clienteBox.getByRole('button').first();
  await selectBtn.click();
  await page.waitForTimeout(300);
  const searchInput = page.locator('[role="listbox"] input, input[placeholder*="Buscar"]').last();
  await searchInput.fill('EXPORT');
  await page.waitForTimeout(400);
  const opt = page.locator('[role="listbox"] [role="option"], ul li').filter({ hasText: /EXPORT/i }).first();
  await opt.click();
  await page.waitForTimeout(500);

  // Fecha de emision: 2026-10-11
  const fechaInput = page.getByLabel(/Fecha de emisión/i);
  if (await fechaInput.isVisible().catch(() => false)) {
    await fechaInput.fill('2026-10-11');
  }

  // Indicador de venta: SERVICIO
  const indSelect = page.getByLabel(/Indicador de venta/i);
  if (await indSelect.isVisible().catch(() => false)) {
    await indSelect.selectOption('SERVICIO');
  }
  await page.waitForTimeout(300);

  // Click Siguiente
  console.log('Moving to Step 2...');
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 2: Items
  console.log('Filling Step 2...');
  // Tipo de línea: SERVICIO
  const tipoLineaSelect = page.getByLabel(/Tipo de línea/i).first();
  if (await tipoLineaSelect.isVisible().catch(() => false)) {
    await tipoLineaSelect.selectOption('SERVICIO');
    await page.waitForTimeout(400);
  }

  // Descripcion: 'Servicios de frío y procesamiento packing temporada cerezas 2026-10'
  const descInput = page.locator('input[placeholder*="Servicio"], input[placeholder*="Flete"]').first();
  await descInput.fill('Servicios de frío y procesamiento packing temporada cerezas 2026-10');

  // Cantidad: 1
  const cantInput = page.getByLabel(/Cantidad/i).first();
  await cantInput.fill('1');

  // Precio unitario: 12500
  const precioInput = page.locator('input[type="number"], input[role="spinbutton"]').nth(1);
  await precioInput.fill('12500');
  await page.waitForTimeout(500);

  // Click Siguiente
  console.log('Moving to Step 3...');
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 3: Referencias y pagos
  console.log('Filling Step 3...');
  const refTipoSelect = page.getByLabel(/Tipo referencia/i);
  if (await refTipoSelect.isVisible().catch(() => false)) {
    await refTipoSelect.selectOption('801');
  }

  const refFolioInput = page.getByLabel(/Folio referencia/i);
  if (await refFolioInput.isVisible().catch(() => false)) {
    await refFolioInput.fill('OC-2026-0015');
  }

  // Guardar OV
  console.log('Saving OV...');
  await page.getByRole('button', { name: /^Guardar$/i }).click();
  await page.waitForTimeout(2000);
  console.log('OV saved, URL:', page.url());

  // 4. Navigate to /comercial/emitir
  console.log('Navigating to /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(1500);

  // Look for the OV in the table and click Facturar
  console.log('Locating OV in Emitir list...');
  const facturarBtn = page.getByRole('button', { name: 'Facturar' }).first();
  await facturarBtn.click();
  await page.waitForTimeout(1000);

  // Check the confirmation modal is open
  const confirmModal = page.locator('div, [role="dialog"]').filter({ hasText: 'Confirmar facturación' });
  await confirmModal.waitFor({ state: 'visible', timeout: 5000 });
  console.log('Confirm modal visible!');

  // Take screenshot 1: mes-contable-dia11-ventas-emitir-dte.png
  const capDir = 'E:/source/repos/Almahue/docs/manual/capturas';
  const cap1 = path.join(capDir, 'mes-contable-dia11-ventas-emitir-dte.png');
  await page.screenshot({ path: cap1, fullPage: false });
  console.log('Screenshot 1 saved at:', cap1);

  // Confirm emission to GoSocket
  console.log('Clicking Confirmar y emitir...');
  const emitBtn = page.getByRole('button', { name: /Confirmar y emitir/i });
  await emitBtn.click();
  await page.waitForTimeout(4000);

  console.log('After emission, URL:', page.url());
  const toastMsg = await page.locator('[data-sonner-toast]').first().innerText().catch(() => 'no toast');
  console.log('Toast:', toastMsg);

  await browser.close();
  console.log('Step 1 & 2 done successfully!');
}

main().catch(console.error);
