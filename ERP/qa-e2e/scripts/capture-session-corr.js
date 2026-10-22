const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.resolve('E:/source/repos/Almahue/docs/sesiones/correcciones-reunion-21-10-2026-10-22');

async function run() {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  const context = await browser.newContext({
    viewport: { width: 1536, height: 960 },
    deviceScaleFactor: 1
  });

  await context.addInitScript(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'true');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-1');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({ temporada: '2026', mesContable: '10', mesRemuneracion: '10', codigo: '2026-10' }));
    localStorage.setItem('almahue-erp-periodo-prompted', '1');
    localStorage.setItem('erp.session', JSON.stringify({
      id: 'USR-1',
      email: 'admin@almahue.local',
      nombre: 'Admin Almahue',
      rol: 'ADMIN',
      rolId: 'ROL-1',
      token: 'mock-token',
      refreshToken: 'mock-refresh',
      empresaId: 'EMP-1',
      empresa: 'ALMAHUE EXPORT SPA',
      permisos: ['*']
    }));
  });

  const page = await context.newPage();

  // 1. Reportes de Activo Fijo (modal con gráfico y detalle normalizado)
  console.log('1. Reportes Activo Fijo...');
  await page.goto('http://localhost:5174/activo-fijo/reportes');
  await page.waitForTimeout(1000);

  // Click on row AF-0001
  const rowAf = page.locator('tr').filter({ hasText: 'AF-0001' }).first();
  if (await rowAf.isVisible()) {
    await rowAf.click();
    await page.waitForTimeout(800);
  }

  const reportesBoxes = await page.evaluate(() => {
    const chart = document.querySelector('.recharts-wrapper') || document.querySelector('svg.recharts-surface')?.parentElement;
    const cards = document.querySelectorAll('.grid.grid-cols-1.md\\:grid-cols-3, .border.rounded-xl.p-4');
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return {
      chart: r(chart),
      cards: Array.from(cards).map(r).filter(Boolean)
    };
  });
  console.log('Reportes AF boxes:', reportesBoxes);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-reportes-af.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });

  // Close modal
  await page.keyboard.press('Escape');
  await page.waitForTimeout(500);

  // 2. Proveedores Lista
  console.log('2. Proveedores Lista...');
  await page.goto('http://localhost:5174/catalogos/proveedores');
  await page.waitForTimeout(1000);

  const provListBox = await page.evaluate(() => {
    const search = document.querySelector('input[placeholder*="Buscar"]') || document.querySelector('input[type="text"]');
    const table = document.querySelector('table');
    const filterBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Filtros'));
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return {
      search: r(search),
      table: r(table),
      filterBtn: r(filterBtn)
    };
  });
  console.log('Proveedores lista boxes:', provListBox);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-proveedores-lista.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });

  // 3. Proveedores Ficha (modo lectura con botón "Editar")
  console.log('3. Proveedores Ficha (modo lectura)...');
  const firstProvRow = page.locator('tbody tr').first();
  if (await firstProvRow.isVisible()) {
    await firstProvRow.locator('td').nth(1).click();
    await page.waitForTimeout(800);
  }

  const provFichaBox = await page.evaluate(() => {
    const editBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Editar');
    const closeBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Cerrar');
    const banners = Array.from(document.querySelectorAll('div, h3, h4')).filter(el => el.textContent.includes('IDENTIFICACIÓN') || el.textContent.includes('CONTACTO'));
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return {
      editBtn: r(editBtn),
      closeBtn: r(closeBtn),
      banner: r(banners[0])
    };
  });
  console.log('Proveedores ficha boxes:', provFichaBox);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-proveedores-ficha.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });

  // Close modal
  await page.keyboard.press('Escape');
  await page.waitForTimeout(500);

  // 4. Cierre Bodega (con cuentas y Guardar predeterminada)
  console.log('4. Cierre Bodega...');
  await page.goto('http://localhost:5174/insumos/cierre');
  await page.waitForTimeout(1000);

  const cierreBox = await page.evaluate(() => {
    const saveDefaultBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('predeterminada'));
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return {
      btn: r(saveDefaultBtn)
    };
  });
  console.log('Cierre bodega boxes:', cierreBox);

  await page.screenshot({
    path: path.join(OUT_DIR, 'despues-cierre-bodega.png'),
    clip: { x: 0, y: 0, width: 1536, height: 960 }
  });

  await browser.close();
  console.log('Captures finished!');
}

run().catch(err => {
  console.error('Capture failed:', err);
  process.exit(1);
});
