import { chromium } from 'playwright-core';
import { mkdir } from 'node:fs/promises';

const out = 'e:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06';
await mkdir(out, { recursive: true });

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
page.setDefaultTimeout(20000);

async function masTarde() {
  const btn = page.getByRole('button', { name: 'Más tarde' });
  if (await btn.count()) {
    await btn.first().click().catch(() => {});
  }
}

await page.goto('http://127.0.0.1:5174/login', { waitUntil: 'domcontentloaded' });
await page.locator('input[type=email]').fill('admin@almahue.local');
await page.locator('input[type=password]').fill('Admin123!');
await page.getByRole('button', { name: 'Entrar con clave' }).click();
await page.waitForURL((u) => !u.pathname.endsWith('/login'), { timeout: 20000 });
await page.waitForTimeout(600);
await masTarde();

// Go to guias-recibidas
await page.goto('http://127.0.0.1:5174/insumos/guias-recibidas', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1000);
await masTarde();

// Click 'Por confirmar' tab
const tabPorConfirmar = page.getByRole('button', { name: /Por confirmar/i });
if (await tabPorConfirmar.count()) {
  await tabPorConfirmar.first().click();
  await page.waitForTimeout(600);
}

// Screenshot despues-guias-por-confirmar.png
await page.screenshot({ path: `${out}/despues-guias-por-confirmar.png` });
console.log('Screenshot despues-guias-por-confirmar.png taken at 1536x960');

// Get bounding box of the table / action button
const rowAction = page.locator('button[title*="Confirmar recepción"]').first();
if (await rowAction.count()) {
  const box = await rowAction.boundingBox();
  console.log('Action box:', box);
}

await browser.close();
console.log('Done!');

