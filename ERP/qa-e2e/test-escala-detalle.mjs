import { chromium } from 'playwright-core';

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});

const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
await page.goto('http://127.0.0.1:5174/login', { waitUntil: 'networkidle' });

// Iniciar sesión como admin real
await page.fill('input[type="email"]', 'admin@almahue.local');
await page.fill('input[type="password"]', 'Admin123!');
await page.click('button:has-text("Entrar con clave")');
await page.waitForURL('**/panel', { timeout: 10000 }).catch(() => {});
await page.waitForTimeout(1000);

// Cerrar modal de bienvenida / PIN si aparece
const btnMasTarde = page.getByRole('button', { name: 'Más tarde', exact: true });
if (await btnMasTarde.count() && await btnMasTarde.first().isVisible().catch(() => false)) {
  await btnMasTarde.first().click().catch(() => {});
  await page.waitForTimeout(300);
}

// 1. Organigrama & Jerarquía
await page.goto('http://127.0.0.1:5174/admin/organigrama', { waitUntil: 'networkidle' });
await page.waitForTimeout(1500);

if (await btnMasTarde.count() && await btnMasTarde.first().isVisible().catch(() => false)) {
  await btnMasTarde.first().click().catch(() => {});
  await page.waitForTimeout(300);
}

// Scroll a la escala y rango 4 en la columna Agrícola
const escalaSecuencial = page.locator('text=Escala Secuencial Interna (3.2 ➔ 3.1)').first();
if (await escalaSecuencial.count()) {
  await escalaSecuencial.scrollIntoViewIfNeeded();
  await page.waitForTimeout(600);
}

await page.screenshot({ path: 'docs/sesiones/acuerdos-sala-2026-11-06/despues-escala-agricola-detalle.png' });
console.log('Captura despues-escala-agricola-detalle.png generada');

// 2. Admin > Usuarios: Marcar "Mostrar todas las empresas" para ver toda la BD de usuarios integrada
await page.goto('http://127.0.0.1:5174/admin/usuarios', { waitUntil: 'networkidle' });
await page.waitForTimeout(1500);

const chkTodasEmpresas = page.locator('label:has-text("Mostrar todas las empresas") input[type="checkbox"]');
if (await chkTodasEmpresas.count() && !(await chkTodasEmpresas.isChecked())) {
  await chkTodasEmpresas.check();
  await page.waitForTimeout(800);
}

await page.screenshot({ path: 'docs/sesiones/acuerdos-sala-2026-11-06/despues-usuarios-bd-integrada.png' });
console.log('Captura despues-usuarios-bd-integrada.png generada');

await browser.close();
