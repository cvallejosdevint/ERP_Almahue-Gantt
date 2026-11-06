const { chromium } = require('E:/source/repos/Almahue/ERP/.qa-tmp/node_modules/playwright');
const path = require('path');
const fs = require('fs');

async function run() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 }
  });
  const page = await context.newPage();
  page.setDefaultTimeout(30000);

  console.log('1. Navigating to login...');
  await page.goto('http://localhost:5174/login');
  await page.waitForSelector('input[type="email"]');
  await page.locator('input[type="email"]').fill('admin@almahue.local');
  await page.locator('input[type="password"]').fill('Admin123!');
  await page.getByRole('button', { name: 'Entrar con clave' }).click();

  await page.waitForURL((u) => !String(u).includes('/login'), { timeout: 30000 });
  console.log('Logged in, current URL:', page.url());

  // Handle period modal if it appears
  const modalPeriodo = page.locator('div, [role="dialog"]').filter({ hasText: /Periodo|Mes contable/i });
  if (await modalPeriodo.first().isVisible({ timeout: 3000 }).catch(() => false)) {
    console.log('Period modal detected');
    const selectMes = page.getByLabel(/Mes contable/i);
    if (await selectMes.isVisible({ timeout: 1000 }).catch(() => false)) {
      await selectMes.selectOption('10');
    }
    const selectAnio = page.getByLabel(/Año/i);
    if (await selectAnio.isVisible({ timeout: 1000 }).catch(() => false)) {
      await selectAnio.selectOption('2026');
    }
    const btnConfirmar = page.getByRole('button', { name: /Confirmar 2026-10|Confirmar/i });
    if (await btnConfirmar.isVisible({ timeout: 1000 }).catch(() => false)) {
      await btnConfirmar.click();
    }
    await page.waitForTimeout(1000);
  }

  // Switch company to ALM SERVICES SPA
  console.log('Switching to ALM SERVICES SPA...');
  const empBtn = page.getByRole('button').filter({ hasText: /EXPORT|SERVICES|Almahue|Empresa/i }).first();
  await empBtn.click();
  await page.waitForTimeout(500);
  const servicesOpt = page.getByRole('button', { name: /SERVICES|77\.032\.639/i }).first();
  await servicesOpt.click();
  await page.waitForTimeout(1000);

  // Period modal again if needed
  const btnConf2 = page.getByRole('button', { name: /Confirmar 2026-10|Confirmar/i });
  if (await btnConf2.isVisible({ timeout: 2000 }).catch(() => false)) {
    await btnConf2.click();
    await page.waitForTimeout(800);
  }

  console.log('Navigating to /comercial/emitir...');
  await page.goto('http://localhost:5174/comercial/emitir');
  await page.waitForTimeout(2000);
  console.log('Current URL at /comercial/emitir:', page.url());

  const title = await page.title();
  console.log('Page title:', title);

  // Check what's on the page
  const pageText = await page.locator('body').innerText();
  console.log('Snippet of body:', pageText.slice(0, 500));

  await browser.close();
}

run().catch(console.error);
