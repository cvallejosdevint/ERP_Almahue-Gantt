const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.resolve(__dirname, '../../docs/sesiones/correcciones-reunion-21-10-2026-10-22');

async function run() {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });
  const page = await context.newPage();

  console.log('Navigating to login...');
  await page.goto('http://localhost:5174/login');
  await page.waitForLoadState('networkidle');

  // Login
  if (page.url().includes('/login')) {
    const emailInput = await page.locator('input[type="email"], input[name="email"]').first();
    const passInput = await page.locator('input[type="password"], input[name="password"]').first();
    if (await emailInput.isVisible()) {
      await emailInput.fill('admin@almahue.local');
      await passInput.fill('Admin123!');
      await page.click('button[type="submit"]');
      await page.waitForTimeout(1500);
    }
  }

  // Confirm period modal if visible
  try {
    const confirmPeriodBtn = page.getByRole('button', { name: /Confirmar 2026/i });
    if (await confirmPeriodBtn.isVisible({ timeout: 2000 })) {
      await confirmPeriodBtn.click();
      await page.waitForTimeout(500);
    }
  } catch (e) {}

  console.log('Current URL after login:', page.url());

  // 1. Reportes de Activo Fijo (modal con gráfico y detalle normalizado)
  console.log('Capturing Reportes Activo Fijo...');
  await page.goto('http://localhost:5174/activo-fijo/reportes');
  await page.waitForTimeout(1000);

  // Click row AF-0001
  const rowAf = page.locator('tr').filter({ hasText: 'AF-0001' }).first();
  if (await rowAf.isVisible()) {
    await rowAf.click();
    await page.waitForTimeout(800);
  }

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-reportes-af.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-reportes-af.png');

  // Close modal
  try {
    const closeBtn = page.getByRole('button', { name: /Cerrar/i }).last();
    if (await closeBtn.isVisible()) await closeBtn.click();
  } catch(e) {}
  await page.waitForTimeout(500);

  // 2. Proveedores Lista
  console.log('Capturing Proveedores Lista...');
  await page.goto('http://localhost:5174/catalogos/proveedores');
  await page.waitForTimeout(1000);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-proveedores-lista.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-proveedores-lista.png');

  // 3. Proveedores Ficha (Modo lectura al hacer clic en fila)
  console.log('Capturing Proveedores Ficha (modo lectura)...');
  const firstRow = page.locator('tbody tr').first();
  if (await firstRow.isVisible()) {
    // Click on cell (not action button)
    await firstRow.locator('td').nth(1).click();
    await page.waitForTimeout(800);
  }

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-proveedores-ficha.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-proveedores-ficha.png');

  // Close modal
  try {
    const closeBtn = page.getByRole('button', { name: /Cerrar/i }).last();
    if (await closeBtn.isVisible()) await closeBtn.click();
  } catch(e) {}
  await page.waitForTimeout(500);

  // 4. Aprobaciones Contratistas (estado Aprobada y layout 3 columnas)
  console.log('Capturing Aprobaciones Contratistas...');
  await page.goto('http://localhost:5174/contratistas/aprobaciones');
  await page.waitForTimeout(1000);

  // Open detail if available
  const verDetalleBtn = page.getByRole('button', { name: /Ver detalle|Detalle/i }).first();
  if (await verDetalleBtn.isVisible()) {
    await verDetalleBtn.click();
    await page.waitForTimeout(800);
  }

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-aprobaciones-contratistas.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-aprobaciones-contratistas.png');

  // 5. Cierre Bodega (con cuentas y botón predeterminada)
  console.log('Capturing Cierre Bodega...');
  await page.goto('http://localhost:5174/insumos/cierre');
  await page.waitForTimeout(1000);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-cierre-bodega.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-cierre-bodega.png');

  // 6. Alta Activo Fijo (con simulación e historial/gráfico abierto)
  console.log('Capturing Alta Activo Fijo...');
  await page.goto('http://localhost:5174/activo-fijo/maestro');
  await page.waitForTimeout(1000);
  const nuevoBtn = page.getByRole('button', { name: /Nuevo activo/i });
  if (await nuevoBtn.isVisible()) {
    await nuevoBtn.click();
    await page.waitForTimeout(600);
    // Expand historial if button is there
    const toggleBtn = page.getByRole('button', { name: /Ver proyección e historial|Historial y gráfico/i });
    if (await toggleBtn.isVisible()) {
      await toggleBtn.click();
      await page.waitForTimeout(500);
    }
  }

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-alta.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });
  console.log('Saved despues-alta.png');

  await browser.close();
  console.log('All captures done successfully!');
}

run().catch(err => {
  console.error('Error running capture:', err);
  process.exit(1);
});
