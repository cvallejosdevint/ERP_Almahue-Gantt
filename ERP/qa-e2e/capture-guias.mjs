import { chromium } from 'playwright-core';
import { mkdir } from 'node:fs/promises';

const out = 'E:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06';
await mkdir(out, { recursive: true });

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
page.setDefaultTimeout(15000);

async function masTarde() {
  const btn = page.getByRole('button', { name: 'Más tarde', exact: true });
  if (await btn.count() && await btn.first().isVisible().catch(() => false)) {
    await btn.first().click().catch(() => {});
    await page.waitForTimeout(200);
  }
}

// Inicializar sesión y modo demo en localStorage
await page.goto('http://127.0.0.1:5174/', { waitUntil: 'domcontentloaded' });
await page.evaluate(() => {
  localStorage.setItem('almahue-erp-demo-mode', 'true');
  localStorage.setItem('almahue-erp-empresa-id', 'EMP-1');
  localStorage.setItem('almahue-erp-periodo-contable', '2026-08');
  localStorage.setItem('erp.session', JSON.stringify({
    id: 'U-1',
    nombre: 'Admin Almahue',
    email: 'admin@almahue.local',
    rolId: 'ROL-1',
    rolNombre: 'Administrador General',
    empresaId: 'EMP-1',
    empresaNombre: 'ALMAHUE EXPORT SPA',
    permisos: ['*'],
    token: 'demo-token',
  }));
});

// Navegar a guías recibidas
await page.goto('http://127.0.0.1:5174/insumos/guias-recibidas', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1000);
await masTarde();

// Clic en pestaña 'Por confirmar'
const tabPorConfirmar = page.getByRole('button', { name: /Por confirmar/i });
let tabBox = null;
if (await tabPorConfirmar.count()) {
  tabBox = await tabPorConfirmar.first().boundingBox();
  await tabPorConfirmar.first().click();
  await page.waitForTimeout(800);
}
await masTarde();

// Captura despues-guias-por-confirmar.png
await page.screenshot({ path: `${out}/despues-guias-por-confirmar.png` });
console.log('Captura despues-guias-por-confirmar.png guardada exitosamente a 1536x960');

// Medir cajas con Playwright locator
let actionBox = null;
const actionBtn = page.locator('button[title*="Confirmar recepción"]').first();
if (await actionBtn.count()) {
  actionBox = await actionBtn.boundingBox();
}

let tableBox = null;
const table = page.locator('table').first();
if (await table.count()) {
  tableBox = await table.boundingBox();
}

console.log('Boxes:', JSON.stringify({ tabBox, actionBox, tableBox }));

await browser.close();
console.log('Listo!');
