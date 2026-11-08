import { chromium } from 'playwright-core';

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
await page.goto('http://127.0.0.1:5174/', { waitUntil: 'domcontentloaded' });
await page.evaluate(() => {
  localStorage.setItem('almahue-erp-demo-mode', 'true');
  localStorage.setItem('almahue-erp-empresa-id', 'EMP-1');
  localStorage.setItem('erp.session', JSON.stringify({
    id: 'U-1',
    nombre: 'Admin Almahue',
    email: 'admin@almahue.local',
    rolId: 'ROL-1',
    rolNombre: 'Administrador General',
    empresaId: 'EMP-1',
    permisos: ['*'],
    token: 'demo-token',
  }));
});
await page.goto('http://127.0.0.1:5174/admin/organigrama', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);

const btnMasTarde = page.getByRole('button', { name: 'Más tarde', exact: true });
if (await btnMasTarde.count() && await btnMasTarde.first().isVisible().catch(() => false)) {
  await btnMasTarde.first().click().catch(() => {});
  await page.waitForTimeout(300);
}

// Crear una rama de nivel 1 llamada 'test' si no existe
const btnNuevaRama = page.getByRole('button', { name: /\+ Nueva Rama/i });
if (await btnNuevaRama.count()) {
  await btnNuevaRama.click();
  await page.waitForTimeout(400);

  // Rellenar modal rama
  const inputs = page.locator('.fixed input[type="text"]');
  if (await inputs.count() >= 2) {
    await inputs.nth(0).fill('test'); // Nombre
  }

  // Nivel 1
  const inputNivel = page.locator('.fixed input[type="number"]').first();
  if (await inputNivel.count()) {
    await inputNivel.fill('1');
  }

  // Guardar rama
  const btnGuardar = page.getByRole('button', { name: /Crear Rama/i });
  if (await btnGuardar.count()) {
    await btnGuardar.click();
  }
  await page.waitForTimeout(800);
}

await page.screenshot({ path: 'docs/sesiones/acuerdos-sala-2026-11-06/despues-segunda-rama-nivel1.png' });
await browser.close();
console.log('Captura despues-segunda-rama-nivel1.png generada con exito');
