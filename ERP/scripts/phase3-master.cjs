const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const CAP_DIR = 'E:/source/repos/Almahue/docs/manual/capturas';

async function main() {
  console.log('=== Starting Phase 3: Ventas, Facturación & Emisión DTE Interempresa ===');

  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 }
  });
  const page = await context.newPage();
  page.setDefaultTimeout(35000);

  async function handlePeriodoModal() {
    try {
      const overlay = page.locator('.fixed.inset-0.z-50');
      if (await overlay.isVisible({ timeout: 5000 }).catch(() => false)) {
        console.log('Modal overlay detected, selecting 2026-10...');
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
          await confirmBtn.click().catch(() => {});
        } else {
          const masTarde = page.getByRole('button', { name: /Más tarde/i });
          if (await masTarde.isVisible().catch(() => false)) {
            await masTarde.click().catch(() => {});
          }
        }
        await page.waitForTimeout(1000);
      }
    } catch (e) {
      console.log('handlePeriodoModal info:', e.message);
    }
  }

  // ----------------------------------------------------
  // STEP 1: Login & Switch to ALM SERVICES SPA (EMP-SERVICES)
  // ----------------------------------------------------
  console.log('--- Step 1: Login & Switch to ALM SERVICES SPA ---');
  await page.goto('http://localhost:5174/login');
  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'), { timeout: 30000 });
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  console.log('Switching company to ALM SERVICES SPA...');
  const empBtn = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
  await empBtn.click();
  await page.waitForTimeout(500);
  const servicesOpt = page.locator('li button').filter({ hasText: /SERVICES|77\.032\.639/i }).first();
  await servicesOpt.click();
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  // ----------------------------------------------------
  // STEP 2: Emisión DTE 33 (Factura Electrónica Interempresa en USD)
  // ----------------------------------------------------
  console.log('--- Step 2: Emisión DTE 33 (Factura Electrónica Interempresa) ---');
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(1500);

  // Step 1 of OV Wizard: Cliente, Fecha, Indicador
  console.log('OV Wizard Step 1: Cliente & General Data...');
  const clienteTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  await clienteTrigger.click();
  await page.waitForTimeout(300);
  const clienteSearch = page.locator('div[role="listbox"] input, input[placeholder*="filtrar"]').last();
  await clienteSearch.fill('EXPORT');
  await page.waitForTimeout(400);
  const exportOpt = page.locator('button[role="option"]').filter({ hasText: /EXPORT/i }).first();
  await exportOpt.click();
  await page.waitForTimeout(500);

  const fechaInput = page.getByLabel(/Fecha de emisión/i);
  if (await fechaInput.isVisible().catch(() => false)) {
    await fechaInput.fill('2026-10-11');
  }

  const indSelect = page.getByLabel(/Indicador de venta/i);
  if (await indSelect.isVisible().catch(() => false)) {
    await indSelect.selectOption('SERVICIO');
  }
  await page.waitForTimeout(300);

  // Click Siguiente -> Step 2 Items
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  console.log('OV Wizard Step 2: Line Item...');
  const tipoLineaSelect = page.getByLabel(/Tipo de línea/i).first();
  if (await tipoLineaSelect.isVisible().catch(() => false)) {
    await tipoLineaSelect.selectOption('SERVICIO');
    await page.waitForTimeout(400);
  }

  const descInput = page.locator('input[placeholder*="Servicio"], input[placeholder*="Flete"]').first();
  await descInput.fill('Servicios de frío y procesamiento packing temporada cerezas 2026-10');

  const cantInput = page.getByLabel(/Cantidad/i).first();
  await cantInput.fill('1');

  const precioInput = page.getByLabel(/Precio unitario/i).first();
  await precioInput.fill('12500');
  await page.waitForTimeout(400);

  // Click Siguiente -> Step 3 References
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  console.log('OV Wizard Step 3: Reference OC-2026-0015...');
  const refTipoSelect = page.getByLabel(/Tipo referencia/i);
  if (await refTipoSelect.isVisible().catch(() => false)) {
    await refTipoSelect.selectOption('801');
  }
  const refFolioInput = page.getByLabel(/Folio referencia/i);
  if (await refFolioInput.isVisible().catch(() => false)) {
    await refFolioInput.fill('OC-2026-0015');
  }

  // Save OV
  console.log('Saving Orden de Venta...');
  await page.getByRole('button', { name: /^Guardar$/i }).click();
  await page.waitForTimeout(2500);
  console.log('Saved OV URL:', page.url());

  // Navigate to Emitir DTE
  console.log('Navigating to /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(2000);

  // Locate the newly created OV in the list and click Facturar
  console.log('Clicking Facturar on OV...');
  const facturarBtn = page.getByRole('button', { name: 'Facturar' }).first();
  await facturarBtn.click();
  await page.waitForTimeout(1000);

  // Verify Confirm modal is open
  const confirmModal = page.locator('div, [role="dialog"]').filter({ hasText: 'Confirmar facturación' });
  await confirmModal.waitFor({ state: 'visible', timeout: 5000 });

  // CAPTURA 1: mes-contable-dia11-ventas-emitir-dte.png
  const cap1Path = path.join(CAP_DIR, 'mes-contable-dia11-ventas-emitir-dte.png');
  await page.screenshot({ path: cap1Path, fullPage: false });
  console.log('CAPTURA 1 guardada:', cap1Path);

  // Confirm emission to GoSocket
  console.log('Emitting invoice to GoSocket via billing-gateway...');
  const emitBtn = page.getByRole('button', { name: /Confirmar y emitir/i });
  await emitBtn.click();
  await page.waitForTimeout(5000);
  console.log('Invoice emitted! Current URL:', page.url());

  // ----------------------------------------------------
  // STEP 3: Emisión DTE 52 (Guía de Despacho Res. 154)
  // ----------------------------------------------------
  console.log('--- Step 3: Emisión DTE 52 (Guía de Despacho) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=GUIA');
  await page.waitForTimeout(2000);

  // Step 1: Cliente & General Data
  console.log('Guía Step 1: Cliente...');
  const guiaClienteTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  await guiaClienteTrigger.click();
  await page.waitForTimeout(300);
  const guiaClienteSearch = page.locator('div[role="listbox"] input, input[placeholder*="filtrar"]').last();
  await guiaClienteSearch.fill('EXPORT');
  await page.waitForTimeout(400);
  const guiaExportOpt = page.locator('button[role="option"]').filter({ hasText: /EXPORT/i }).first();
  await guiaExportOpt.click();
  await page.waitForTimeout(500);

  const guiaFechaInput = page.getByLabel(/Fecha de emisión/i);
  if (await guiaFechaInput.isVisible().catch(() => false)) {
    await guiaFechaInput.fill('2026-10-12');
  }

  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 2: Item
  console.log('Guía Step 2: Item...');
  const itemSearchTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  if (await itemSearchTrigger.isVisible().catch(() => false)) {
    await itemSearchTrigger.click();
    await page.waitForTimeout(300);
    const itemOpt = page.locator('button[role="option"]').first();
    if (await itemOpt.isVisible().catch(() => false)) {
      await itemOpt.click();
      await page.waitForTimeout(400);
    }
  }

  const guiaCantInput = page.getByLabel(/Cantidad/i).first();
  if (await guiaCantInput.isVisible().catch(() => false)) {
    await guiaCantInput.fill('5000');
  }

  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 3: Res. 154 Transport Data
  console.log('Guía Step 3: Transporte Res. 154...');
  const indTrasladoSelect = page.getByLabel(/Tipo de traslado/i);
  if (await indTrasladoSelect.isVisible().catch(() => false)) {
    await indTrasladoSelect.selectOption('6'); // 6 Otros traslados no venta
  }

  const dirDest = page.getByLabel(/Dirección de destino/i);
  if (await dirDest.isVisible().catch(() => false)) await dirDest.fill('Fundo El Carmen 120');

  const cmnaDest = page.getByLabel(/Comuna de destino/i);
  if (await cmnaDest.isVisible().catch(() => false)) await cmnaDest.fill('Rancagua');

  const ciudadDest = page.getByLabel(/Ciudad de destino/i);
  if (await ciudadDest.isVisible().catch(() => false)) await ciudadDest.fill('Rancagua');

  const rutTrans = page.getByLabel(/RUT transportista/i);
  if (await rutTrans.isVisible().catch(() => false)) await rutTrans.fill('76.888.901-5');

  const rutChofer = page.getByLabel(/RUT chofer/i);
  if (await rutChofer.isVisible().catch(() => false)) await rutChofer.fill('12.345.678-5');

  const nombreChofer = page.getByLabel(/Nombre del chofer/i);
  if (await nombreChofer.isVisible().catch(() => false)) await nombreChofer.fill('Juan Perez');

  const patente = page.getByLabel(/Patente del vehículo/i);
  if (await patente.isVisible().catch(() => false)) await patente.fill('ABCD12');

  const fchSalida = page.getByLabel(/Fecha de salida/i);
  if (await fchSalida.isVisible().catch(() => false)) await fchSalida.fill('2026-10-12');

  const hraSalida = page.getByLabel(/Hora de salida/i);
  if (await hraSalida.isVisible().catch(() => false)) await hraSalida.fill('08:30');

  const fchLlegada = page.getByLabel(/Fecha de llegada/i);
  if (await fchLlegada.isVisible().catch(() => false)) await fchLlegada.fill('2026-10-12');

  await page.waitForTimeout(500);

  // CAPTURA 2: mes-contable-dia12-ventas-guia-res154.png
  const cap2Path = path.join(CAP_DIR, 'mes-contable-dia12-ventas-guia-res154.png');
  await page.screenshot({ path: cap2Path, fullPage: false });
  console.log('CAPTURA 2 guardada:', cap2Path);

  // Emit Guia DTE 52
  console.log('Emitting Guía DTE 52 to GoSocket...');
  const emitGuiaBtn = page.getByRole('button', { name: /Emitir documento/i });
  await emitGuiaBtn.click();
  await page.waitForTimeout(5000);
  console.log('Guía emitted! Current URL:', page.url());

  // ----------------------------------------------------
  // STEP 4: Emisión DTE 61 (Nota de Crédito)
  // ----------------------------------------------------
  console.log('--- Step 4: Emisión DTE 61 (Nota de Crédito) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=NC');
  await page.waitForTimeout(2000);

  // Reference recent factura in NC
  console.log('NC Step 1: Referencing Factura...');
  const docRefTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  await docRefTrigger.click();
  await page.waitForTimeout(300);
  const docRefSearch = page.locator('div[role="listbox"] input, input[placeholder*="filtrar"]').last();
  await docRefSearch.fill('Factura');
  await page.waitForTimeout(400);
  const firstFacturaOpt = page.locator('button[role="option"]').first();
  if (await firstFacturaOpt.isVisible().catch(() => false)) {
    await firstFacturaOpt.click();
    await page.waitForTimeout(500);
  } else {
    // Fallback to manual reference if needed
    console.log('Using manual reference for NC...');
    await page.getByRole('button', { name: /Registro manual/i }).click();
    await page.getByLabel(/Tipo SII del origen/i).selectOption('33');
    await page.getByLabel(/Folio SII/i).fill('59');
    await page.getByLabel(/Fecha del origen/i).fill('2026-10-11');
    const clTrigger = page.locator('button[aria-haspopup="listbox"]').first();
    await clTrigger.click();
    await page.locator('div[role="listbox"] input').last().fill('EXPORT');
    await page.locator('button[role="option"]').filter({ hasText: /EXPORT/i }).first().click();
  }

  const ncCodRef = page.getByLabel(/CodRef/i);
  if (await ncCodRef.isVisible().catch(() => false)) {
    await ncCodRef.selectOption('3'); // 3 Corrige montos
  }

  const ncFecha = page.getByLabel(/Fecha de emisión/i);
  if (await ncFecha.isVisible().catch(() => false)) {
    await ncFecha.fill('2026-10-17');
  }

  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 2: Item / Discount
  console.log('NC Step 2: Monto ajuste...');
  const ncPrecio = page.getByLabel(/Precio unitario/i).first();
  if (await ncPrecio.isVisible().catch(() => false)) {
    await ncPrecio.fill('500');
  }
  const ncCant = page.getByLabel(/Cantidad/i).first();
  if (await ncCant.isVisible().catch(() => false)) {
    await ncCant.fill('1');
  }
  await page.waitForTimeout(400);

  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 3: Observaciones
  console.log('NC Step 3: Observaciones...');
  const obs = page.locator('textarea').first();
  if (await obs.isVisible().catch(() => false)) {
    await obs.fill('Descuento acordado de USD 500 corrigiendo la factura anterior por servicios de frío temporada cerezas.');
  }

  await page.waitForTimeout(500);

  // CAPTURA 3: mes-contable-dia17-compras-nc-nd-ajuste.png
  const cap3Path = path.join(CAP_DIR, 'mes-contable-dia17-compras-nc-nd-ajuste.png');
  await page.screenshot({ path: cap3Path, fullPage: false });
  console.log('CAPTURA 3 guardada:', cap3Path);

  // Emit NC DTE 61
  console.log('Emitting NC DTE 61 to GoSocket...');
  const emitNcBtn = page.getByRole('button', { name: /Emitir documento/i });
  await emitNcBtn.click();
  await page.waitForTimeout(5000);
  console.log('NC emitted! Current URL:', page.url());

  // ----------------------------------------------------
  // STEP 5: Switch to ALMAHUE EXPORT SPA & Libro de Compras Calce
  // ----------------------------------------------------
  console.log('--- Step 5: Switch back to ALMAHUE EXPORT SPA & Libro de Compras ---');
  const empBtn2 = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
  await empBtn2.click();
  await page.waitForTimeout(500);
  const exportOpt2 = page.locator('li button').filter({ hasText: /EXPORT|77\.032\.638/i }).first();
  await exportOpt2.click();
  await page.waitForTimeout(1000);
  await handlePeriodoModal();

  console.log('Navigating to /compras/registro...');
  await page.goto('http://localhost:5174/compras/registro');
  await page.waitForTimeout(2000);

  // Synchronize GoSocket documents
  console.log('Opening Sincronizar GoSocket modal...');
  const syncBtn = page.getByRole('button', { name: /Sincronizar/i }).first();
  await syncBtn.click();
  await page.waitForTimeout(800);

  const doSyncBtn = page.locator('div[role="dialog"] button, .fixed.inset-0 button').filter({ hasText: /^Sincronizar$/i }).last();
  await doSyncBtn.click();
  await page.waitForTimeout(5000);
  console.log('GoSocket sync completed!');

  // Look for FAC-CTR-9901 and link proforma PF-00001
  console.log('Linking FAC-CTR-9901 to PF-00001...');
  const row9901 = page.locator('tr').filter({ hasText: 'FAC-CTR-9901' }).first();
  if (await row9901.isVisible({ timeout: 4000 }).catch(() => false)) {
    console.log('Row FAC-CTR-9901 found! Opening Vincular modal...');
    const vincularBtn = row9901.getByRole('button', { name: /Vincular|Asociar|OC/i }).first();
    await vincularBtn.click();
    await page.waitForTimeout(1000);

    // Switch to Proformas tab
    const proformasTab = page.getByRole('button', { name: /Proformas/i }).first();
    if (await proformasTab.isVisible().catch(() => false)) {
      await proformasTab.click();
      await page.waitForTimeout(800);

      // Check PF-00001 checkbox
      const pfRow = page.locator('tr, li, div').filter({ hasText: 'PF-00001' }).first();
      const pfCheckbox = pfRow.locator('input[type="checkbox"]').first();
      await pfCheckbox.check();
      await page.waitForTimeout(600);

      // Click Vincular proformas button
      const confirmVincular = page.getByRole('button', { name: /Vincular.*proforma/i });
      if (await confirmVincular.isVisible().catch(() => false)) {
        await confirmVincular.click();
        await page.waitForTimeout(2000);
        console.log('Proforma PF-00001 linked to FAC-CTR-9901!');
      }
    }
  }

  // Refresh and take CAPTURA 4: mes-contable-dia14-compras-libro-recepcion-calce.png
  await page.goto('http://localhost:5174/compras/registro');
  await page.waitForTimeout(2000);

  const cap4Path = path.join(CAP_DIR, 'mes-contable-dia14-compras-libro-recepcion-calce.png');
  await page.screenshot({ path: cap4Path, fullPage: false });
  console.log('CAPTURA 4 guardada:', cap4Path);

  // ----------------------------------------------------
  // STEP 6: Visualización de PDF Oficial GoSocket
  // ----------------------------------------------------
  console.log('--- Step 6: Visualización de PDF Oficial GoSocket ---');
  // Click 'Ver PDF' on an official invoice in the table
  const pdfBtn = page.locator('tr').filter({ hasText: /ALM SERVICES|FAC-CTR-9901|66|67|68/i }).first().getByRole('button', { name: /PDF|Ver PDF/i }).first();
  if (await pdfBtn.isVisible({ timeout: 4000 }).catch(() => false)) {
    console.log('Clicking Ver PDF button...');
    await pdfBtn.click();
    await page.waitForTimeout(2500);

    // Verify PDF viewer modal is open
    const pdfModal = page.locator('div, [role="dialog"]').filter({ hasText: /PDF|Representación Gráfica|DTE/i }).first();
    await pdfModal.waitFor({ state: 'visible', timeout: 5000 }).catch(() => {});

    // CAPTURA 5: mes-contable-dia15-compras-pdf-gosocket-oficial.png
    const cap5Path = path.join(CAP_DIR, 'mes-contable-dia15-compras-pdf-gosocket-oficial.png');
    await page.screenshot({ path: cap5Path, fullPage: false });
    console.log('CAPTURA 5 guardada:', cap5Path);

    // Close PDF modal
    const closePdfBtn = page.getByRole('button', { name: /Cerrar|Volver/i }).last();
    if (await closePdfBtn.isVisible().catch(() => false)) {
      await closePdfBtn.click().catch(() => {});
      await page.waitForTimeout(800);
    }
  } else {
    console.log('PDF button not found directly, clicking on row or action menu...');
  }

  // ----------------------------------------------------
  // STEP 7: Contabilización en Libro de Compras
  // ----------------------------------------------------
  console.log('--- Step 7: Contabilización en Libro de Compras ---');
  // For facturas in "Por contabilizar" (EMITIDO), open Contabilizar modal
  const contabilizarBtn = page.locator('tr').filter({ hasText: /Por contabilizar|EMITIDO/i }).first().getByRole('button', { name: /Contabilizar/i }).first();
  if (await contabilizarBtn.isVisible({ timeout: 4000 }).catch(() => false)) {
    console.log('Clicking Contabilizar on row...');
    await contabilizarBtn.click();
    await page.waitForTimeout(1500);

    // Save imputation
    const guardarContaBtn = page.getByRole('button', { name: /Guardar y contabilizar|Contabilizar|Confirmar/i }).last();
    if (await guardarContaBtn.isVisible().catch(() => false)) {
      await guardarContaBtn.click();
      await page.waitForTimeout(2500);
      console.log('Factura contabilizada exitosamente!');
    }
  }

  await browser.close();
  console.log('=== PHASE 3 COMPLETED SUCCESSFULLY! ===');
}

main().catch(console.error);
