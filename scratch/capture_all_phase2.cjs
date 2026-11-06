const { chromium } = require('E:/source/repos/Almahue/ERP/qa-e2e/node_modules/playwright-core');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.resolve('E:/source/repos/Almahue/docs/manual/capturas');

async function capture() {
  console.log('Launching browser...');
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  console.log('Logging in...');
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

  const pinCoordinates = {};

  // -------------------------------------------------------------
  // CAPTURA 1: Día 06 - Ingreso Diario
  // -------------------------------------------------------------
  console.log('1. Navigating to /contratistas/ingreso-diario...');
  await page.goto('http://localhost:5174/contratistas/ingreso-diario');
  await page.waitForTimeout(2000);

  const newIngresoBtn = page.getByRole('button', { name: /Nuevo ingreso/i }).first();
  const newIngresoBox = await newIngresoBtn.boundingBox();
  console.log('newIngresoBox:', newIngresoBox);

  const row06 = page.locator('tr', { hasText: '06-10-2026' }).first();
  const row06Box = await row06.boundingBox();
  console.log('row06Box:', row06Box);

  const badge06 = row06.locator('span, div').filter({ hasText: 'ASOCIADO' }).first();
  let badge06Box = await badge06.boundingBox();
  if (!badge06Box) {
    const fallbackBadge = row06.locator('span, div').filter({ hasText: /ASOCIADO|PENDIENTE|FACTURADO/i }).first();
    badge06Box = await fallbackBadge.boundingBox();
  }
  console.log('badge06Box:', badge06Box);

  const monto06 = row06.locator('td', { hasText: '$700.000' }).first();
  const monto06Box = await monto06.boundingBox();
  console.log('monto06Box:', monto06Box);

  const cap1Path = path.join(OUT_DIR, 'mes-contable-dia06-ctr-ingreso-diario.png');
  await page.screenshot({ path: cap1Path });
  console.log('Saved:', cap1Path);

  pinCoordinates['mes-contable-dia06-ctr-ingreso-diario'] = {
    nuevoIngresoBtn: newIngresoBox ? { x: Math.round(newIngresoBox.x + newIngresoBox.width / 2), y: Math.round(newIngresoBox.y + newIngresoBox.height / 2) } : null,
    fila06: row06Box ? { x: Math.round(row06Box.x + 120), y: Math.round(row06Box.y + row06Box.height / 2) } : null,
    monto700k: monto06Box ? { x: Math.round(monto06Box.x + monto06Box.width / 2), y: Math.round(monto06Box.y + monto06Box.height / 2) } : null,
    badgeEstado: badge06Box ? { x: Math.round(badge06Box.x + badge06Box.width / 2), y: Math.round(badge06Box.y + badge06Box.height / 2) } : null,
  };

  // -------------------------------------------------------------
  // CAPTURA 2: Día 08 - Proforma Definitiva
  // -------------------------------------------------------------
  console.log('2. Navigating to /contratistas/proformas...');
  await page.goto('http://localhost:5174/contratistas/proformas');
  await page.waitForTimeout(2000);

  const rowPf = page.locator('tr', { hasText: 'PF-00001' }).first();
  const rowPfBox = await rowPf.boundingBox();
  console.log('rowPfBox:', rowPfBox);

  const badgeDef = rowPf.locator('span, div').filter({ hasText: 'DEFINITIVA' }).first();
  const badgeDefBox = await badgeDef.boundingBox();
  console.log('badgeDefBox:', badgeDefBox);

  const montoPf = rowPf.locator('td', { hasText: '$7.600.000' }).first();
  const montoPfBox = await montoPf.boundingBox();
  console.log('montoPfBox:', montoPfBox);

  const contratistaPf = rowPf.locator('td', { hasText: 'Servicios Agrícolas del Valle' }).first();
  const contratistaPfBox = await contratistaPf.boundingBox();
  console.log('contratistaPfBox:', contratistaPfBox);

  const cap2Path = path.join(OUT_DIR, 'mes-contable-dia08-ctr-proforma-definitiva.png');
  await page.screenshot({ path: cap2Path });
  console.log('Saved:', cap2Path);

  pinCoordinates['mes-contable-dia08-ctr-proforma-definitiva'] = {
    filaProforma: rowPfBox ? { x: Math.round(rowPfBox.x + 80), y: Math.round(rowPfBox.y + rowPfBox.height / 2) } : null,
    contratista: contratistaPfBox ? { x: Math.round(contratistaPfBox.x + contratistaPfBox.width / 2), y: Math.round(contratistaPfBox.y + contratistaPfBox.height / 2) } : null,
    monto7600k: montoPfBox ? { x: Math.round(montoPfBox.x + montoPfBox.width / 2), y: Math.round(montoPfBox.y + montoPfBox.height / 2) } : null,
    badgeDefinitiva: badgeDefBox ? { x: Math.round(badgeDefBox.x + badgeDefBox.width / 2), y: Math.round(badgeDefBox.y + badgeDefBox.height / 2) } : null,
  };

  // -------------------------------------------------------------
  // CAPTURA 3: Día 10 - Traspaso y Asiento Contable
  // -------------------------------------------------------------
  console.log('3. Navigating to /contratistas/traspaso...');
  await page.goto('http://localhost:5174/contratistas/traspaso');
  await page.waitForTimeout(2000);

  const asientoLink = page.locator('a', { hasText: /asiento 20260009/i }).first();
  const asientoLinkBox = await asientoLink.boundingBox();
  console.log('asientoLinkBox:', asientoLinkBox);

  const resumenCard = page.locator('div', { hasText: 'ELEMENTOS DE CIERRE' }).first();
  const resumenCardBox = await resumenCard.boundingBox();
  console.log('resumenCardBox:', resumenCardBox);

  const rowTraspaso = page.locator('tr', { hasText: 'En cierre · 20260009' }).first();
  const rowTraspasoBox = await rowTraspaso.boundingBox();
  console.log('rowTraspasoBox:', rowTraspasoBox);

  const cap3Path = path.join(OUT_DIR, 'mes-contable-dia10-ctr-traspaso-asiento.png');
  await page.screenshot({ path: cap3Path });
  console.log('Saved:', cap3Path);

  pinCoordinates['mes-contable-dia10-ctr-traspaso-asiento'] = {
    bloqueResumenVerde: resumenCardBox ? { x: Math.round(resumenCardBox.x + resumenCardBox.width / 2), y: Math.round(resumenCardBox.y + resumenCardBox.height / 2) } : null,
    bannerCierreAsiento: asientoLinkBox ? { x: Math.round(asientoLinkBox.x + asientoLinkBox.width / 2), y: Math.round(asientoLinkBox.y + asientoLinkBox.height / 2) } : null,
    filaEnCierre: rowTraspasoBox ? { x: Math.round(rowTraspasoBox.x + 120), y: Math.round(rowTraspasoBox.y + rowTraspasoBox.height / 2) } : null,
  };

  console.log('Pin coordinates summary:');
  console.log(JSON.stringify(pinCoordinates, null, 2));

  fs.writeFileSync('scratch/pin_coordinates.json', JSON.stringify(pinCoordinates, null, 2));

  await browser.close();
  console.log('ALL CAPTURES FINISHED SUCCESSFULLY!');
}

capture().catch(console.error);
