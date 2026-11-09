import { chromium } from 'playwright-core';

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});

const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
await page.goto('http://127.0.0.1:5174/', { waitUntil: 'domcontentloaded' });
await page.evaluate(() => {
  localStorage.setItem('almahue-erp-demo-mode', 'false'); // Probar con la API real / almacenamiento real
  localStorage.setItem('almahue-erp-empresa-id', 'EMP-1');
  localStorage.setItem('erp.session', JSON.stringify({
    id: 'U-1',
    nombre: 'Admin Almahue',
    email: 'admin@almahue.local',
    rolId: 'ROL-1',
    rolNombre: 'Administrador General',
    empresaId: 'EMP-1',
    permisos: ['*'],
    token: 'test-token',
  }));
});

// 1. Captura de Organigrama
await page.goto('http://127.0.0.1:5174/admin/organigrama', { waitUntil: 'networkidle' });
await page.waitForTimeout(1000);

const btnMasTarde = page.getByRole('button', { name: 'Más tarde', exact: true });
if (await btnMasTarde.count() && await btnMasTarde.first().isVisible().catch(() => false)) {
  await btnMasTarde.first().click().catch(() => {});
  await page.waitForTimeout(300);
}

// Scroll a la rama Agrícola para enfocar la escala 3.1/3.2 y el Rango 4 con múltiples usuarios
await page.screenshot({ path: 'docs/sesiones/acuerdos-sala-2026-11-06/despues-organigrama-escala-invertida.png' });
console.log('Captura despues-organigrama-escala-invertida.png generada');

// 2. Captura de Admin > Usuarios
await page.goto('http://127.0.0.1:5174/admin/usuarios', { waitUntil: 'networkidle' });
await page.waitForTimeout(1200);

await page.screenshot({ path: 'docs/sesiones/acuerdos-sala-2026-11-06/despues-usuarios-bd-integrada.png' });
console.log('Captura despues-usuarios-bd-integrada.png generada');

await browser.close();

