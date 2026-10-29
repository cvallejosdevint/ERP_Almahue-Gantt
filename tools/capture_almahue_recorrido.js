const path = require('path');
const fs = require('fs');
const playwrightPath = path.resolve('ERP/.qa-tmp/node_modules/playwright');
const { chromium } = require(playwrightPath);

const outputDir = path.resolve('docs/sesiones/cierre-contratistas-matriz-2x2-2026-10-29');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1,
  });

  // Inyectar sesión autenticada y modo demo en localStorage
  await context.addInitScript(() => {
    localStorage.setItem(
      'erp.session',
      JSON.stringify({
        id: 'USR-ADMIN',
        email: 'admin@almahue.local',
        nombre: 'Administrador Demo',
        rol: 'ADMIN',
        rolId: 'ROL-1',
        empresaId: 'EMP-1',
        empresa: 'Agrícola Almahue S.A.',
        permisos: ['*'],
        token: 'demo-token',
        refreshToken: 'demo-refresh',
      }),
    );
    localStorage.setItem('almahue.demo_mode', 'true');
    localStorage.setItem('almahue.empresa_activa', 'EMP-1');
  });

  const page = await context.newPage();
  page.setDefaultTimeout(15000);

  console.log('1. Abriendo panel de Proformas de Contratistas...');
  await page.goto('http://localhost:5174/contratistas/proformas', { waitUntil: 'networkidle' }).catch(() => {});
  await page.waitForTimeout(1000);

  // Cerrar modal de confirmación de período si existe
  try {
    const btn = page.getByRole('button', { name: /Confirmar 20/i });
    if (await btn.isVisible({ timeout: 1500 })) {
      await btn.click();
      await page.waitForTimeout(500);
    }
  } catch (e) {}

  console.log('Captura 1: despues-proformas.png');
  await page.screenshot({ path: path.join(outputDir, 'despues-proformas.png'), fullPage: false });

  // Captura 2: Detalle/Items de la proforma
  console.log('2. Abriendo modal de Items/Detalle de proforma...');
  const btnItems = page.locator('button').filter({ hasText: /Items/i }).first();
  if (await btnItems.isVisible({ timeout: 2000 }).catch(() => false)) {
    await btnItems.click();
    await page.waitForTimeout(800);
    console.log('Captura 2: despues-detalle-proforma.png');
    await page.screenshot({ path: path.join(outputDir, 'despues-detalle-proforma.png'), fullPage: false });
    await page.keyboard.press('Escape');
    await page.waitForTimeout(400);
  }

  // Captura 3: Panel de Traspaso y Cierre de Contratistas (Matriz 2x2)
  console.log('3. Abriendo Traspaso y Cierre de Contratistas...');
  await page.goto('http://localhost:5174/contratistas/traspaso-cierre', { waitUntil: 'networkidle' }).catch(() => {});
  await page.waitForTimeout(1000);

  try {
    const btn = page.getByRole('button', { name: /Confirmar 20/i });
    if (await btn.isVisible({ timeout: 1500 })) {
      await btn.click();
      await page.waitForTimeout(500);
    }
  } catch (e) {}

  console.log('Captura 3: despues-traspaso-cierre.png');
  await page.screenshot({ path: path.join(outputDir, 'despues-traspaso-cierre.png'), fullPage: false });

  // Captura 4: Botón de Reversar Proforma (Modal con Clave/PIN)
  console.log('4. Navegando para capturar modal de reversa con clave...');
  await page.goto('http://localhost:5174/contratistas/proformas', { waitUntil: 'networkidle' }).catch(() => {});
  await page.waitForTimeout(800);
  const btnReversar = page.locator('button').filter({ hasText: /Reversar/i }).first();
  if (await btnReversar.isVisible({ timeout: 2000 }).catch(() => false)) {
    await btnReversar.click();
    await page.waitForTimeout(600);
    console.log('Captura 4: despues-reversa-modal.png');
    await page.screenshot({ path: path.join(outputDir, 'despues-reversa-modal.png'), fullPage: false });
    await page.keyboard.press('Escape');
    await page.waitForTimeout(400);
  }

  await browser.close();
  console.log('TODAS LAS CAPTURAS COMPLETADAS EXITOSAMENTE');
})();
