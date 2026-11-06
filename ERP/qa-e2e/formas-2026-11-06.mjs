import { chromium } from 'playwright-core';
import { mkdir } from 'node:fs/promises';

const out = 'E:/source/repos/Almahue/ERP/erp_back/qa-results/formas-2026-11-06';
await mkdir(out, { recursive: true });
const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
page.setDefaultTimeout(20000);

async function shot(name) {
  await page.screenshot({ path: `${out}/${name}.png` });
  console.log('shot', name);
}

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
await masTarde();

await page.goto('http://127.0.0.1:5174/admin/aprobaciones', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(800);
await masTarde();
const maria = page.getByText('María González', { exact: true }).first();
if (await maria.count()) {
  await maria.click();
  await page.getByRole('button', { name: 'Editar', exact: true }).first().click();
  await page.waitForTimeout(400);
  await shot('escala');
  await page.keyboard.press('Escape');
}

await page.goto('http://127.0.0.1:5174/activo-fijo/maestro', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(600);
await masTarde();
const nuevoActivo = page.getByRole('button', { name: 'Nuevo activo' });
if (await nuevoActivo.count()) {
  await nuevoActivo.click();
  await page.waitForTimeout(400);
  await shot('activo');
  await page.keyboard.press('Escape');
}

await page.goto('http://127.0.0.1:5174/presupuestos', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(600);
await masTarde();
const nuevoPres = page.getByRole('button', { name: 'Nuevo Presupuesto' });
if (await nuevoPres.count()) {
  await nuevoPres.click();
  await page.waitForTimeout(400);
  await shot('presupuesto');
  await page.keyboard.press('Escape');
}

await page.goto('http://127.0.0.1:5174/catalogos/proveedores', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(600);
await masTarde();
const nuevoProv = page.getByRole('button', { name: /Nuevo/ }).first();
if (await nuevoProv.count()) {
  await nuevoProv.click();
  await page.waitForTimeout(400);
  await shot('proveedor');
  await page.keyboard.press('Escape');
}

await browser.close();
console.log('listo');

