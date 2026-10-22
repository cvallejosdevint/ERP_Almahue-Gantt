const { chromium } = require('playwright-core');

(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  const context = await browser.newContext({ viewport: { width: 1536, height: 960 } });
  await context.addInitScript(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'true');
    localStorage.setItem('almahue-erp-selected-empresa', 'EMP-1');
    localStorage.setItem('almahue-erp-periodo-contable', JSON.stringify({ temporada: '2026', mesContable: '10', mesRemuneracion: '10', codigo: '2026-10' }));
    localStorage.setItem('almahue-erp-periodo-prompted', '1');
    localStorage.setItem('erp.session', JSON.stringify({
      id: 'USR-1', email: 'admin@almahue.local', nombre: 'Admin Almahue', rol: 'ADMIN',
      token: 'mock-token', refreshToken: 'mock-refresh', empresaId: 'EMP-1', empresa: 'ALMAHUE EXPORT SPA',
      permisos: ['admin:*', '*:*']
    }));
  });
  const page = await context.newPage();

  // 1. Reportes AF
  await page.goto('http://localhost:5174/activo-fijo/reportes');
  await page.waitForTimeout(800);
  await page.locator('tr').filter({ hasText: 'AF-0001' }).first().click();
  await page.waitForTimeout(600);

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
  console.log('Reportes boxes:', JSON.stringify(reportesBoxes));

  // 2. Proveedores Lista
  await page.goto('http://localhost:5174/catalogos/proveedores');
  await page.waitForTimeout(800);
  const provListBoxes = await page.evaluate(() => {
    const search = document.querySelector('input[type="text"]');
    const table = document.querySelector('table');
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return { search: r(search), table: r(table) };
  });
  console.log('Prov list boxes:', JSON.stringify(provListBoxes));

  // 3. Proveedores Ficha
  await page.locator('tbody tr').first().locator('td').nth(1).click();
  await page.waitForTimeout(600);
  const provFichaBoxes = await page.evaluate(() => {
    const editBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Editar proveedor'));
    const banner = Array.from(document.querySelectorAll('div')).find(d => d.textContent.includes('IDENTIFICACIÓN'));
    function r(el) {
      if (!el) return null;
      const b = el.getBoundingClientRect();
      return `${Math.round(b.x)},${Math.round(b.y)},${Math.round(b.width)},${Math.round(b.height)}`;
    }
    return { editBtn: r(editBtn), banner: r(banner) };
  });
  console.log('Prov ficha boxes:', JSON.stringify(provFichaBoxes));

  await browser.close();
})();
