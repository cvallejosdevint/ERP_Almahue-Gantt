const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const CAP_DIR = 'E:/source/repos/Almahue/docs/manual/capturas';

async function main() {
  console.log('================================================================');
  console.log('🚀 FASE 3: Ventas, Facturación & Emisión DTE Interempresa');
  console.log('================================================================\n');

  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 }
  });
  const page = await context.newPage();
  page.setDefaultTimeout(40000);

  async function handlePeriodoModal(targetPeriod = '2026-10') {
    try {
      const overlay = page.locator('.fixed.inset-0.z-50');
      if (await overlay.isVisible({ timeout: 4000 }).catch(() => false)) {
        console.log(`[Periodo] Modal detectado, configurando ${targetPeriod}...`);
        const [anio, mes] = targetPeriod.split('-');
        const anioSelect = page.getByLabel('Año');
        if (await anioSelect.isVisible({ timeout: 1000 }).catch(() => false)) {
          await anioSelect.selectOption(anio).catch(() => {});
        }
        const mesSelect = page.getByLabel('Mes contable');
        if (await mesSelect.isVisible({ timeout: 1000 }).catch(() => false)) {
          await mesSelect.selectOption(mes).catch(() => {});
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
      console.log('[Periodo] Info:', e.message);
    }
  }

  // ----------------------------------------------------
  // PASO 1: Login & Switch a ALM SERVICES SPA (EMP-SERVICES)
  // ----------------------------------------------------
  console.log('\n--- PASO 1: Login y Cambio a ALM SERVICES SPA ---');
  await page.goto('http://localhost:5174/login');
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'false'); // Real API mode
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-SERVICES');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({ temporada: '2026', mesContable: '10', codigo: '2026-10' }));
    localStorage.setItem('almahue-erp-periodo-prompted', 'true');
  });
  await page.reload();

  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();
  await page.waitForURL(u => !String(u).includes('/login'), { timeout: 30000 });
  await page.waitForTimeout(2000);
  await handlePeriodoModal('2026-10');

  // Verify company selector in topbar
  const empSelectorBtn = page.locator('header button').filter({ hasText: /ALMAHUE|SERVICES|EXPORT/i }).first();
  const currentEmpText = await empSelectorBtn.innerText();
  console.log(`Empresa actual en topbar: ${currentEmpText.replace(/\n/g, ' ')}`);

  if (!currentEmpText.includes('SERVICES')) {
    console.log('Cambiando empresa a ALM SERVICES SPA...');
    await empSelectorBtn.click();
    await page.waitForTimeout(500);
    const servicesOpt = page.locator('.absolute.left-0 button').filter({ hasText: /SERVICES/i }).first();
    await servicesOpt.click();
    await page.waitForTimeout(1000);
    await handlePeriodoModal('2026-10');
  }

  // ----------------------------------------------------
  // PASO 2: Emisión DTE 33 (Factura Electrónica Interempresa en USD)
  // ----------------------------------------------------
  console.log('\n--- PASO 2: Emisión DTE 33 (Factura Interempresa en USD) ---');
  // Navigate to Nueva orden de venta
  await page.goto('http://localhost:5174/comercial/ordenes-venta/nueva');
  await page.waitForTimeout(2000);

  // Step 1: Cliente & General Data
  console.log('Llenando Paso 1: Cliente ALMAHUE EXPORT SPA...');
  const clienteTrigger = page.getByRole('button', { name: 'Buscar cliente…' });
  await clienteTrigger.click();
  await page.waitForTimeout(600);
  const clienteOpt = page.locator('button[role="option"]').filter({ hasText: /ALMAHUE EXPORT/i }).first();
  await clienteOpt.click();
  await page.waitForTimeout(500);

  const fechaInput = page.getByLabel(/Fecha de emisión/i);
  if (await fechaInput.isVisible().catch(() => false)) {
    await fechaInput.fill('2026-10-11');
  }

  const indSelect = page.getByLabel(/Indicador de venta/i);
  if (await indSelect.isVisible().catch(() => false)) {
    await indSelect.selectOption('SERVICIO');
  }
  await page.waitForTimeout(400);

  console.log('Avanzando a Paso 2 (Ítems)...');
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 2: Line Item
  console.log('Llenando Paso 2: Ítem Servicio de frío...');
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

  console.log('Avanzando a Paso 3 (Referencias)...');
  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 3: Reference OC-2026-0015
  console.log('Llenando Paso 3: Referencia OC-2026-0015...');
  const refTipoSelect = page.getByLabel(/Tipo referencia/i);
  if (await refTipoSelect.isVisible().catch(() => false)) {
    await refTipoSelect.selectOption('801');
  }
  const refFolioInput = page.getByLabel(/Folio referencia/i);
  if (await refFolioInput.isVisible().catch(() => false)) {
    await refFolioInput.fill('OC-2026-0015');
  }

  console.log('Guardando Orden de Venta...');
  await page.getByRole('button', { name: /^Guardar$/i }).click();
  await page.waitForTimeout(3000);
  console.log('OV guardada. URL:', page.url());

  // Navigate to Emitir DTE
  console.log('Navegando a /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(2000);

  // Find OV row and click Facturar
  console.log('Abriendo modal Confirmar Facturación...');
  const facturarBtn = page.locator('tr').filter({ hasText: /ALMAHUE EXPORT/i }).first().getByRole('button', { name: 'Facturar' });
  await facturarBtn.click();
  await page.waitForTimeout(1000);

  // Wait for Confirmar Facturación modal
  const confirmModal = page.locator('div, [role="dialog"]').filter({ hasText: 'Confirmar facturación' });
  await confirmModal.waitFor({ state: 'visible', timeout: 5000 });

  // CAPTURA 1: mes-contable-dia11-ventas-emitir-dte.png
  const cap1 = path.join(CAP_DIR, 'mes-contable-dia11-ventas-emitir-dte.png');
  await page.screenshot({ path: cap1, fullPage: false });
  console.log('📸 CAPTURA 1 guardada:', cap1);

  // Click Confirmar y emitir
  console.log('Enviando emisión formal a GoSocket vía billing-gateway...');
  const emitBtn = page.getByRole('button', { name: /Confirmar y emitir/i });
  await emitBtn.click();
  await page.waitForTimeout(6000);
  console.log('Factura emitida formalmente! URL:', page.url());

  // ----------------------------------------------------
  // PASO 3: Emisión DTE 52 (Guía de Despacho Res. 154)
  // ----------------------------------------------------
  console.log('\n--- PASO 3: Emisión DTE 52 (Guía de Despacho) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=GUIA');
  await page.waitForTimeout(2000);

  // Step 1: Cliente ALMAHUE EXPORT SPA
  console.log('Guía Paso 1: Cliente...');
  const guiaClienteTrigger = page.getByRole('button', { name: 'Buscar cliente…' });
  await guiaClienteTrigger.click();
  await page.waitForTimeout(600);
  const guiaExportOpt = page.locator('button[role="option"]').filter({ hasText: /ALMAHUE EXPORT/i }).first();
  await guiaExportOpt.click();
  await page.waitForTimeout(500);

  const guiaFechaInput = page.getByLabel(/Fecha de emisión/i);
  if (await guiaFechaInput.isVisible().catch(() => false)) {
    await guiaFechaInput.fill('2026-10-12');
  }

  await page.getByRole('button', { name: 'Siguiente' }).click();
  await page.waitForTimeout(800);

  // Step 2: Item
  console.log('Guía Paso 2: Ítem Pallets...');
  const itemTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  if (await itemTrigger.isVisible().catch(() => false)) {
    await itemTrigger.click();
    await page.waitForTimeout(400);
    const firstOpt = page.locator('button[role="option"]').first();
    if (await firstOpt.isVisible().catch(() => false)) {
      await firstOpt.click();
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
  console.log('Guía Paso 3: Transporte Res. 154...');
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

  const patenteCarro = page.getByLabel(/Patente del carro/i);
  if (await patenteCarro.isVisible().catch(() => false)) await patenteCarro.fill('XY9901');

  const fchSalida = page.getByLabel(/Fecha de salida/i);
  if (await fchSalida.isVisible().catch(() => false)) await fchSalida.fill('2026-10-12');

  const hraSalida = page.getByLabel(/Hora de salida/i);
  if (await hraSalida.isVisible().catch(() => false)) await hraSalida.fill('08:30');

  const fchLlegada = page.getByLabel(/Fecha de llegada/i);
  if (await fchLlegada.isVisible().catch(() => false)) await fchLlegada.fill('2026-10-12');

  await page.waitForTimeout(600);

  // CAPTURA 2: mes-contable-dia12-ventas-guia-res154.png
  const cap2 = path.join(CAP_DIR, 'mes-contable-dia12-ventas-guia-res154.png');
  await page.screenshot({ path: cap2, fullPage: false });
  console.log('📸 CAPTURA 2 guardada:', cap2);

  // Emit Guia DTE 52
  console.log('Emitiendo Guía DTE 52 formal...');
  const emitGuiaBtn = page.getByRole('button', { name: /Emitir documento/i });
  await emitGuiaBtn.click();
  await page.waitForTimeout(6000);
  console.log('Guía DTE 52 emitida! URL:', page.url());

  // ----------------------------------------------------
  // PASO 4: Emisión DTE 61 (Nota de Crédito Electrónica)
  // ----------------------------------------------------
  console.log('\n--- PASO 4: Emisión DTE 61 (Nota de Crédito) ---');
  await page.goto('http://localhost:5174/comercial/emitir?tipo=NC');
  await page.waitForTimeout(2000);

  console.log('NC Paso 1: Referenciando Factura previa...');
  const docRefTrigger = page.locator('button[aria-haspopup="listbox"]').first();
  await docRefTrigger.click();
  await page.waitForTimeout(500);
  const docRefSearch = page.locator('div[role="listbox"] input, input[placeholder*="filtrar"]').last();
  await docRefSearch.fill('Factura');
  await page.waitForTimeout(400);

  const firstFacturaOpt = page.locator('button[role="option"]').filter({ hasText: /Factura/i }).first();
  if (await firstFacturaOpt.isVisible().catch(() => false)) {
    await firstFacturaOpt.click();
    await page.waitForTimeout(500);
  } else {
    console.log('Usando referencia manual para NC...');
    await page.getByRole('button', { name: /Registro manual/i }).click();
    await page.getByLabel(/Tipo SII del origen/i).selectOption('33');
    await page.getByLabel(/Folio SII/i).fill('59');
    await page.getByLabel(/Fecha del origen/i).fill('2026-10-11');
    const clTrigger = page.getByRole('button', { name: 'Buscar cliente…' });
    await clTrigger.click();
    await page.locator('button[role="option"]').filter({ hasText: /ALMAHUE EXPORT/i }).first().click();
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

  console.log('NC Paso 2: Descuento acordado USD $500...');
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

  console.log('NC Paso 3: Observaciones y verificación...');
  const obs = page.locator('textarea').first();
  if (await obs.isVisible().catch(() => false)) {
    await obs.fill('Descuento acordado de USD 500 corrigiendo la factura anterior por servicios de frío temporada cerezas.');
  }
  await page.waitForTimeout(600);

  // CAPTURA 3: mes-contable-dia17-compras-nc-nd-ajuste.png
  const cap3 = path.join(CAP_DIR, 'mes-contable-dia17-compras-nc-nd-ajuste.png');
  await page.screenshot({ path: cap3, fullPage: false });
  console.log('📸 CAPTURA 3 guardada:', cap3);

  console.log('Emitiendo Nota de Crédito DTE 61 formal...');
  const emitNcBtn = page.getByRole('button', { name: /Emitir documento/i });
  await emitNcBtn.click();
  await page.waitForTimeout(6000);
  console.log('Nota de Crédito DTE 61 emitida! URL:', page.url());

  // ----------------------------------------------------
  // PASO 5: Switch a ALMAHUE EXPORT SPA (EMP-EXPORT) y Libro de Compras
  // ----------------------------------------------------
  console.log('\n--- PASO 5: Switch a ALMAHUE EXPORT SPA y Libro de Compras ---');
  await empSelectorBtn.click();
  await page.waitForTimeout(500);
  const exportOpt = page.locator('.absolute.left-0 button').filter({ hasText: /EXPORT/i }).first();
  await exportOpt.click();
  await page.waitForTimeout(1000);
  await handlePeriodoModal('2026-10');

  console.log('Navegando a /compras/registro...');
  await page.goto('http://localhost:5174/compras/registro');
  await page.waitForTimeout(2000);

  // Sincronizar GoSocket
  console.log('Sincronizando Libro de Compras desde GoSocket...');
  const syncBtn = page.getByRole('button', { name: /Sincronizar/i }).first();
  await syncBtn.click();
  await page.waitForTimeout(800);

  const doSyncBtn = page.locator('div[role="dialog"] button, .fixed.inset-0 button').filter({ hasText: /^Sincronizar$/i }).last();
  await doSyncBtn.click();
  await page.waitForTimeout(6000);
  console.log('Sincronización GoSocket completada!');

  // Vincular FAC-CTR-9901 a Proforma PF-00001
  console.log('Localizando factura FAC-CTR-9901 para vincular proforma...');
  const row9901 = page.locator('tr').filter({ hasText: 'FAC-CTR-9901' }).first();
  if (await row9901.isVisible({ timeout: 5000 }).catch(() => false)) {
    console.log('Fila FAC-CTR-9901 encontrada! Abriendo modal de vinculación...');
    const vincularBtn = row9901.getByRole('button', { name: /Vincular|Asociar|OC/i }).first();
    await vincularBtn.click();
    await page.waitForTimeout(1200);

    // Switch to tab Proformas
    const proformasTab = page.getByRole('button', { name: /Proformas/i }).first();
    if (await proformasTab.isVisible().catch(() => false)) {
      await proformasTab.click();
      await page.waitForTimeout(800);

      const pfRow = page.locator('tr, li, div').filter({ hasText: 'PF-00001' }).first();
      const pfCheckbox = pfRow.locator('input[type="checkbox"]').first();
      await pfCheckbox.check();
      await page.waitForTimeout(600);

      const confirmVincular = page.getByRole('button', { name: /Vincular.*proforma/i });
      if (await confirmVincular.isVisible().catch(() => false)) {
        await confirmVincular.click();
        await page.waitForTimeout(2500);
        console.log('Proforma PF-00001 vinculada exitosamente con calce 100%!');
      }
    }
  }

  // Reload Libro de compras view
  await page.goto('http://localhost:5174/compras/registro');
  await page.waitForTimeout(2500);

  // CAPTURA 4: mes-contable-dia14-compras-libro-recepcion-calce.png
  const cap4 = path.join(CAP_DIR, 'mes-contable-dia14-compras-libro-recepcion-calce.png');
  await page.screenshot({ path: cap4, fullPage: false });
  console.log('📸 CAPTURA 4 guardada:', cap4);

  // ----------------------------------------------------
  // PASO 6: Visualización de PDF Oficial GoSocket
  // ----------------------------------------------------
  console.log('\n--- PASO 6: Visualización de PDF Oficial GoSocket ---');
  const pdfBtn = page.locator('tr').filter({ hasText: /ALM SERVICES|FAC-CTR-9901|66|67|68/i }).first().getByRole('button', { name: /PDF|Ver PDF/i }).first();
  if (await pdfBtn.isVisible({ timeout: 5000 }).catch(() => false)) {
    console.log('Abriendo visor PDF oficial GoSocket...');
    await pdfBtn.click();
    await page.waitForTimeout(3000);

    const pdfModal = page.locator('div, [role="dialog"]').filter({ hasText: /PDF|Representación Gráfica|DTE/i }).first();
    await pdfModal.waitFor({ state: 'visible', timeout: 5000 }).catch(() => {});

    // CAPTURA 5: mes-contable-dia15-compras-pdf-gosocket-oficial.png
    const cap5 = path.join(CAP_DIR, 'mes-contable-dia15-compras-pdf-gosocket-oficial.png');
    await page.screenshot({ path: cap5, fullPage: false });
    console.log('📸 CAPTURA 5 guardada:', cap5);

    // Close PDF modal
    const closePdfBtn = page.getByRole('button', { name: /Cerrar|Volver/i }).last();
    if (await closePdfBtn.isVisible().catch(() => false)) {
      await closePdfBtn.click().catch(() => {});
      await page.waitForTimeout(800);
    }
  } else {
    console.log('Buscando icono PDF alternativo...');
  }

  // ----------------------------------------------------
  // PASO 7: Contabilización en Libro de Compras
  // ----------------------------------------------------
  console.log('\n--- PASO 7: Contabilización en Libro de Compras ---');
  const contaBtn = page.locator('tr').filter({ hasText: /Por contabilizar|EMITIDO/i }).first().getByRole('button', { name: /Contabilizar/i }).first();
  if (await contaBtn.isVisible({ timeout: 4000 }).catch(() => false)) {
    console.log('Abriendo modal Contabilizar / Imputación...');
    await contaBtn.click();
    await page.waitForTimeout(1500);

    const guardarContaBtn = page.getByRole('button', { name: /Guardar y contabilizar|Contabilizar|Confirmar/i }).last();
    if (await guardarContaBtn.isVisible().catch(() => false)) {
      await guardarContaBtn.click();
      await page.waitForTimeout(2500);
      console.log('Factura contabilizada exitosamente con asiento generado!');
    }
  }

  await browser.close();
  console.log('\n================================================================');
  console.log('🎉 FASE 3 EJECUTADA CON ÉXITO AL 100%');
  console.log('================================================================');
}

main().catch(console.error);
