const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const CAP_DIR = 'E:/source/repos/Almahue/docs/manual/capturas';

if (!fs.existsSync(CAP_DIR)) {
  fs.mkdirSync(CAP_DIR, { recursive: true });
}

async function run() {
  console.log('=== [PHASE 3] Starting Full Interactive Execution ===');

  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 }
  });
  const page = await context.newPage();
  page.setDefaultTimeout(35000);

  // Helper to close period modal if open
  async function handlePeriodoModal() {
    try {
      await page.waitForTimeout(500);
      const overlay = page.locator('.fixed.inset-0.z-50');
      if (await overlay.isVisible({ timeout: 2000 }).catch(() => false)) {
        console.log('Modal overlay detected, clicking Confirmar...');
        const confirmBtn = page.getByRole('button', { name: /Confirmar /i }).last();
        if (await confirmBtn.isVisible({ timeout: 1000 }).catch(() => false)) {
          await confirmBtn.click().catch(() => {});
        } else {
          const masTarde = page.getByRole('button', { name: /Más tarde/i });
          if (await masTarde.isVisible().catch(() => false)) {
            await masTarde.click().catch(() => {});
          }
        }
        await page.waitForTimeout(800);
      }
    } catch (e) {
      console.log('handlePeriodoModal warning:', e.message);
    }
  }

  // ----------------------------------------------------
  // STEP 1: Login & Switch to ALM SERVICES SPA (EMP-SERVICES)
  // ----------------------------------------------------
  console.log('--- Step 1: Login & Switch to ALM SERVICES SPA ---');
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
  await page.waitForTimeout(500);

  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'), { timeout: 30000 });
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  console.log('Verifying company selector...');
  const currentCompany = await page.getByRole('button').filter({ hasText: /SERVICES|EXPORT|Empresa/i }).first().innerText().catch(() => '');
  console.log('Current company text:', currentCompany);
  if (!currentCompany.includes('SERVICES')) {
    console.log('Switching to ALM SERVICES SPA...');
    const empBtn = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
    await empBtn.click();
    await page.waitForTimeout(500);
    const servicesOpt = page.locator('li button').filter({ hasText: /SERVICES|77\.032\.639/i }).first();
    await servicesOpt.click();
    await page.waitForTimeout(1000);
    await handlePeriodoModal();
  }

  // ----------------------------------------------------
  // STEP 2: Emisión DTE 33 (Factura Electrónica Interempresa)
  // ----------------------------------------------------
  console.log('--- Step 2: Emisión DTE 33 (Factura Electrónica Interempresa) ---');
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(2000);

  console.log('OV Wizard Step 1: Cliente & General Data...');
  const btnCliente = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnCliente.click();
  await page.waitForTimeout(500);

  const exportOpt = page.locator('[role="option"]').filter({ hasText: /EXPORT/i }).first();
  await exportOpt.click();
  await page.waitForTimeout(500);

  console.log('Setting fechaEmision 2026-10-11...');
  const fechaInput = page.locator('input[type="date"]').first();
  await fechaInput.fill('2026-10-11');

  const indSelect = page.getByLabel(/Indicador de venta/i);
  if (await indSelect.isVisible().catch(() => false)) {
    await indSelect.selectOption('SERVICIO').catch(() => {});
  }
  await page.waitForTimeout(400);

  // Click Siguiente -> Step 2
  console.log('Moving to Step 2...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('OV Wizard Step 2: Line Item...');
  const tipoLineaBtn = page.locator('table tbody tr').first().locator('button[aria-haspopup="listbox"]').first();
  await tipoLineaBtn.click();
  await page.waitForTimeout(400);
  const servicioOpt = page.locator('[role="option"]').filter({ hasText: /^Servicio$/i }).first();
  await servicioOpt.click();
  await page.waitForTimeout(500);

  const descInput = page.locator('table tbody tr input[placeholder*="Servicio"]').first();
  await descInput.fill('Servicios de frío y procesamiento packing temporada cerezas 2026-10');

  const cantInput = page.getByLabel('Cantidad').first();
  await cantInput.fill('1');

  const precioInput = page.getByLabel('Precio unitario').first();
  await precioInput.fill('12500');
  await page.waitForTimeout(400);

  // Click Siguiente -> Step 3
  console.log('Moving to Step 3...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('OV Wizard Step 3: Reference OC-2026-0015...');
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

  // Save OV
  console.log('Saving Orden de Venta...');
  await page.getByRole('button', { name: /^Guardar$/i }).first().click();
  await page.waitForTimeout(3000);
  console.log('Saved OV, URL is:', page.url());

  // Go to /comercial/emitir
  console.log('Navigating to /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(2500);

  // Click Facturar on the confirmed OV
  console.log('Waiting for Facturar button on OV...');
  const facturarBtn = page.getByRole('button', { name: 'Facturar' }).first();
  await facturarBtn.waitFor({ state: 'visible', timeout: 15000 });
  await facturarBtn.click();
  await page.waitForTimeout(2000);

  // Modal "Confirmar facturación"
  console.log('Modal Confirmar facturación open! Taking Screenshot 1...');
  const cap1 = path.join(CAP_DIR, 'mes-contable-dia11-ventas-emitir-dte.png');
  await page.screenshot({ path: cap1, fullPage: true });
  console.log('Saved:', cap1);

  // Click Confirmar y emitir
  console.log('Confirming and emitting Factura DTE 33...');
  const emitirFacturaBtn = page.getByRole('button', { name: /Confirmar y emitir/i }).first();
  await emitirFacturaBtn.click();
  await page.waitForTimeout(5000);
  console.log('Factura emitted to GoSocket. Navigated to:', page.url());

  // ----------------------------------------------------
  // STEP 3: Emisión DTE 52 (Guía de Despacho Res. 154)
  // ----------------------------------------------------
  console.log('--- Step 3: Emisión DTE 52 (Guía de Despacho Res. 154) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=GUIA');
  await page.waitForTimeout(2000);

  console.log('Guía Step 1: Cliente & Fecha...');
  const btnClienteGuia = page.getByRole('button', { name: 'Buscar cliente…' });
  await btnClienteGuia.click();
  await page.waitForTimeout(500);
  const exportOptGuia = page.locator('[role="option"]').filter({ hasText: /EXPORT/i }).first();
  await exportOptGuia.click();
  await page.waitForTimeout(500);

  const fechaGuiaInput = page.locator('input[type="date"]').first();
  if (await fechaGuiaInput.isVisible().catch(() => false)) {
    await fechaGuiaInput.fill('2026-10-12');
  }

  // Next to Step 2
  console.log('Moving to Guía Step 2...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('Guía Step 2: Line items...');
  const tipoLineaGuiaBtn = page.locator('table tbody tr').first().locator('button[aria-haspopup="listbox"]').first();
  await tipoLineaGuiaBtn.click();
  await page.waitForTimeout(400);
  const servicioOptGuia = page.locator('[role="option"]').filter({ hasText: /^Servicio$/i }).first();
  await servicioOptGuia.click();
  await page.waitForTimeout(500);

  const descGuiaInput = page.locator('table tbody tr input[placeholder*="Servicio"]').first();
  await descGuiaInput.fill('Traslado pallets y materiales de packing bodega');

  const cantGuiaInput = page.getByLabel('Cantidad').first();
  await cantGuiaInput.fill('5000');

  const precioGuiaInput = page.getByLabel('Precio unitario').first();
  await precioGuiaInput.fill('0');
  await page.waitForTimeout(400);

  // Next to Step 3
  console.log('Moving to Guía Step 3...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('Guía Step 3: Resolución 154 transport fields...');
  // Type of traslado: Otros traslados no venta (6)
  const indTrasladoBtn = page.locator('button[aria-haspopup="listbox"]').filter({ hasText: /Operación constituye|traslado|Seleccionar/i }).first();
  if (await indTrasladoBtn.isVisible().catch(() => false)) {
    await indTrasladoBtn.click();
    await page.waitForTimeout(400);
    const opt6 = page.locator('[role="option"]').filter({ hasText: /Otros traslados no venta|6/i }).first();
    if (await opt6.isVisible().catch(() => false)) {
      await opt6.click();
      await page.waitForTimeout(400);
    }
  }

  const dirDestInput = page.getByLabel(/Dirección destino/i);
  if (await dirDestInput.isVisible().catch(() => false)) await dirDestInput.fill('Camino Los Boldos Km 4');

  const cmnaDestInput = page.getByLabel(/Comuna destino/i);
  if (await cmnaDestInput.isVisible().catch(() => false)) await cmnaDestInput.fill('Requínoa');

  const ciudadDestInput = page.getByLabel(/Ciudad destino/i);
  if (await ciudadDestInput.isVisible().catch(() => false)) await ciudadDestInput.fill('Rancagua');

  const rutTranspInput = page.getByLabel(/RUT transportista/i);
  if (await rutTranspInput.isVisible().catch(() => false)) await rutTranspInput.fill('76.310.201-7');

  const rutChoferInput = page.getByLabel(/RUT chofer/i);
  if (await rutChoferInput.isVisible().catch(() => false)) await rutChoferInput.fill('15.888.999-4');

  const nomChoferInput = page.getByLabel(/Nombre chofer/i);
  if (await nomChoferInput.isVisible().catch(() => false)) await nomChoferInput.fill('Juan Perez');

  const patenteInput = page.getByLabel(/Patente vehículo/i);
  if (await patenteInput.isVisible().catch(() => false)) await patenteInput.fill('AB1234');

  const fchSalidaInput = page.getByLabel(/Fecha de salida/i);
  if (await fchSalidaInput.isVisible().catch(() => false)) await fchSalidaInput.fill('2026-10-12');

  const hraSalidaInput = page.getByLabel(/Hora de salida/i);
  if (await hraSalidaInput.isVisible().catch(() => false)) await hraSalidaInput.fill('08:30');

  const fchLlegadaInput = page.getByLabel(/Fecha de llegada/i);
  if (await fchLlegadaInput.isVisible().catch(() => false)) await fchLlegadaInput.fill('2026-10-12');
  await page.waitForTimeout(500);

  console.log('Taking Screenshot 2: mes-contable-dia12-ventas-guia-res154.png...');
  const cap2 = path.join(CAP_DIR, 'mes-contable-dia12-ventas-guia-res154.png');
  await page.screenshot({ path: cap2, fullPage: true });
  console.log('Saved:', cap2);

  console.log('Emitting Guía DTE 52...');
  const emitirGuiaBtn = page.getByRole('button', { name: /Emitir documento|Confirmar y emitir/i }).first();
  await emitirGuiaBtn.click();
  await page.waitForTimeout(5000);
  console.log('Guía emitted to GoSocket. Navigated to:', page.url());

  // ----------------------------------------------------
  // STEP 4: Emisión DTE 61 (Nota de Crédito)
  // ----------------------------------------------------
  console.log('--- Step 4: Emisión DTE 61 (Nota de Crédito) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=NC');
  await page.waitForTimeout(2000);

  console.log('NC Step 1: Origin Document...');
  const docRefTrigger = page.locator('button[aria-haspopup="listbox"]').filter({ hasText: /Buscar factura|coincidencias/i }).first();
  if (await docRefTrigger.isVisible().catch(() => false)) {
    await docRefTrigger.click();
    await page.waitForTimeout(500);
    const invoiceOpt = page.locator('[role="option"]').first();
    console.log('Selected origin invoice:', await invoiceOpt.innerText().catch(() => ''));
    await invoiceOpt.click();
    await page.waitForTimeout(600);
  }

  const fechaNcInput = page.locator('input[type="date"]').first();
  if (await fechaNcInput.isVisible().catch(() => false)) {
    await fechaNcInput.fill('2026-10-17');
  }

  // Next to Step 2
  console.log('Moving to NC Step 2...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('NC Step 2: Line items...');
  const descNcInput = page.locator('table tbody tr input[placeholder*="Servicio"], table tbody tr input[value*="Servicios"]').first();
  if (await descNcInput.isVisible().catch(() => false)) {
    await descNcInput.fill('Descuento comercial acordado temporada cerezas 2026-10');
  }

  const precioNcInput = page.getByLabel('Precio unitario').first();
  if (await precioNcInput.isVisible().catch(() => false)) {
    await precioNcInput.fill('500');
  }
  await page.waitForTimeout(400);

  // Next to Step 3
  console.log('Moving to NC Step 3...');
  await page.getByRole('button', { name: 'Siguiente' }).first().click();
  await page.waitForTimeout(1500);

  console.log('NC Step 3: Observations & Reason...');
  const obsInput = page.getByLabel(/Observaciones/i);
  if (await obsInput.isVisible().catch(() => false)) {
    await obsInput.fill('Descuento comercial acordado USD 500 por servicios temporada cerezas 2026-10');
  }
  await page.waitForTimeout(500);

  console.log('Taking Screenshot 3: mes-contable-dia17-compras-nc-nd-ajuste.png...');
  const cap3 = path.join(CAP_DIR, 'mes-contable-dia17-compras-nc-nd-ajuste.png');
  await page.screenshot({ path: cap3, fullPage: true });
  console.log('Saved:', cap3);

  console.log('Emitting Nota de Crédito DTE 61...');
  const emitirNcBtn = page.getByRole('button', { name: /Emitir documento|Confirmar y emitir/i }).first();
  await emitirNcBtn.click();
  await page.waitForTimeout(5000);
  console.log('NC emitted to GoSocket. Navigated to:', page.url());

  // ----------------------------------------------------
  // STEP 5: Switch to ALMAHUE EXPORT SPA & Libro de Compras
  // ----------------------------------------------------
  console.log('--- Step 5: Switch back to ALMAHUE EXPORT SPA (EMP-EXPORT) ---');
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-EXPORT');
  });
  await page.goto('http://localhost:5174/compras/registro');
  await page.waitForTimeout(2500);
  await handlePeriodoModal();

  console.log('Opening Sincronizar GoSocket Modal in Libro de compras...');
  const syncBtn = page.getByRole('button', { name: /Sincronizar/i }).first();
  await syncBtn.click();
  await page.waitForTimeout(1000);

  const doSyncBtn = page.locator('.fixed.z-50 button, [role="dialog"] button').filter({ hasText: /^Sincronizar$/i }).first();
  console.log('Clicking Sincronizar button inside modal...');
  await doSyncBtn.click();
  await page.waitForTimeout(6000);
  console.log('GoSocket sync completed! Refreshing page...');
  await page.reload();
  await page.waitForTimeout(2500);
  await handlePeriodoModal();

  console.log('Taking Screenshot 4: mes-contable-dia14-compras-libro-recepcion-calce.png...');
  const cap4 = path.join(CAP_DIR, 'mes-contable-dia14-compras-libro-recepcion-calce.png');
  await page.screenshot({ path: cap4, fullPage: true });
  console.log('Saved:', cap4);

  // ----------------------------------------------------
  // STEP 6: Visualización de PDF Oficial GoSocket
  // ----------------------------------------------------
  console.log('--- Step 6: Visualización de PDF Oficial GoSocket ---');
  const verPdfBtn = page.getByRole('button', { name: 'Ver PDF' }).first();
  if (await verPdfBtn.isVisible({ timeout: 3000 }).catch(() => false)) {
    console.log('Clicking direct Ver PDF button...');
    await verPdfBtn.click();
  } else {
    console.log('Checking row action dropdown for Ver PDF...');
    const actionBtn = page.locator('table tbody tr button').filter({ hasText: /PDF|Ver/i }).first();
    if (await actionBtn.isVisible().catch(() => false)) {
      await actionBtn.click();
    } else {
      const moreBtn = page.locator('table tbody tr').first().locator('button[aria-haspopup="menu"]').first();
      await moreBtn.click();
      await page.waitForTimeout(400);
      const pdfItem = page.locator('[role="menuitem"], li button').filter({ hasText: /Ver PDF/i }).first();
      await pdfItem.click();
    }
  }
  await page.waitForTimeout(4000);

  console.log('Taking Screenshot 5: mes-contable-dia15-compras-pdf-gosocket-oficial.png...');
  const cap5 = path.join(CAP_DIR, 'mes-contable-dia15-compras-pdf-gosocket-oficial.png');
  await page.screenshot({ path: cap5, fullPage: true });
  console.log('Saved:', cap5);

  // Close PDF modal
  console.log('Closing PDF modal...');
  const closePdfBtn = page.getByRole('button', { name: 'Cerrar' }).first();
  if (await closePdfBtn.isVisible().catch(() => false)) {
    await closePdfBtn.click();
    await page.waitForTimeout(800);
  }

  // ----------------------------------------------------
  // STEP 7: Contabilización en Libro de Compras
  // ----------------------------------------------------
  console.log('--- Step 7: Contabilización en Libro de Compras ---');
  const contabilizarBtn = page.getByRole('button', { name: /Contabilizar/i }).first();
  if (await contabilizarBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
    console.log('Clicking Contabilizar button on invoice...');
    await contabilizarBtn.click();
    await page.waitForTimeout(2000);

    const aceptarBtn = page.getByRole('button', { name: 'Aceptar y contabilizar' });
    if (await aceptarBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
      console.log('Clicking Aceptar y contabilizar...');
      await aceptarBtn.click();
      await page.waitForTimeout(3500);
      console.log('Invoice successfully CONTABILIZADA!');
    }
  }

  console.log('=== [PHASE 3] Completed successfully! ===');
  await browser.close();
}

run().catch((e) => {
  console.error('FATAL ERROR in run():', e);
  process.exit(1);
});
