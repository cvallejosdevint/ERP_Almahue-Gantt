const { chromium } = require('E:/source/repos/Almahue/ERP/qa-e2e/node_modules/playwright-core');
const path = require('path');
const fs = require('fs');

const CAPTURAS_DIR = path.resolve('E:/source/repos/Almahue/docs/manual/capturas');

async function main() {
  console.log('--- STARTING PHASE 2 AUTOMATION ---');
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  // 1. Login and session setup
  console.log('1. Logging in at http://localhost:5174/login...');
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

  await page.goto('http://localhost:5174/contratistas');
  await page.waitForTimeout(1500);

  const header = await page.locator('header').innerText();
  console.log('Header text:', header.replace(/\n+/g, ' | '));

  // 2. Check / create contractor
  console.log('2. Checking if Servicios Agrícolas del Valle exists...');
  const tableContent = await page.locator('table').innerText().catch(() => '');
  if (tableContent.includes('76.111.222-3') || tableContent.includes('Servicios Agrícolas del Valle')) {
    console.log('Contratista already exists in table.');
  } else {
    console.log('Contratista does not exist. Creating new contratista...');
    const newBtn = page.getByRole('button', { name: /Nuevo contratista/i });
    await newBtn.click();
    await page.waitForTimeout(800);

    // Fill RUT
    const rutInput = page.getByPlaceholder('12.345.678-9');
    await rutInput.fill('76.111.222-3');

    // Fill Nombre / Razón Social
    const nombreLabel = page.locator('label', { hasText: 'Nombre / razón social' });
    const nombreInput = nombreLabel.locator('..').locator('input');
    await nombreInput.fill('Servicios Agrícolas del Valle');

    // Fill Ciudad
    const ciudadLabel = page.locator('label', { hasText: 'Ciudad' });
    const ciudadInput = ciudadLabel.locator('..').locator('input');
    await ciudadInput.fill('Almahue');

    // Fill Comuna
    const comunaLabel = page.locator('label', { hasText: 'Comuna' });
    const comunaInput = comunaLabel.locator('..').locator('input');
    await comunaInput.fill('Almahue');

    // Save
    const saveBtn = page.getByRole('button', { name: /Guardar/i }).last();
    await saveBtn.click();
    await page.waitForTimeout(2000);
    console.log('Contratista saved.');
  }

  // Verify contratista exists
  const updatedTable = await page.locator('table').innerText().catch(() => '');
  console.log('Table contains contractor:', updatedTable.includes('76.111.222-3'));

  await browser.close();
}

main().catch(console.error);
