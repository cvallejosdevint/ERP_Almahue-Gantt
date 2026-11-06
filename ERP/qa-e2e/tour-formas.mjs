import { chromium } from 'playwright-core';
import { mkdir, writeFile } from 'node:fs/promises';

const out = 'E:/source/repos/Almahue/ERP/erp_back/qa-results/formas-2026-11-06';
await mkdir(out, { recursive: true });

const routes = [
  '/admin/empresas',
  '/admin/usuarios',
  '/admin/roles',
  '/admin/configuracion-correos',
  '/admin/aprobaciones',
  '/catalogos/monedas',
  '/catalogos/unidades',
  '/catalogos/centros-costo',
  '/catalogos/areas-negocio',
  '/catalogos/conceptos-flujo',
  '/catalogos/codigos-financieros',
  '/catalogos/tipos-documento',
  '/catalogos/plan-cuentas',
  '/catalogos/elementos-costo',
  '/catalogos/indicadores-bc',
  '/catalogos/bancos',
  '/catalogos/factor-honorarios',
  '/catalogos/contratista',
  '/catalogos/activo-fijo',
  '/catalogos/proveedores',
  '/contratistas',
  '/contratistas/ingreso-diario',
  '/contratistas/proformas',
  '/compras/ordenes',
  '/compras/ordenes/nueva',
  '/compras/registro',
  '/compras/notas-cobro',
  '/insumos/maestro',
  '/insumos/bodegas',
  '/insumos/packings',
  '/insumos/movimientos',
  '/insumos/ordenes-aplicacion',
  '/insumos/guias-recibidas',
  '/activo-fijo/maestro',
  '/activo-fijo/ingreso',
  '/activo-fijo/traspaso',
  '/contabilidad/asientos',
  '/contabilidad/periodos',
  '/presupuestos',
  '/tesoreria/pagos',
  '/tesoreria/compromisos-anticipos',
  '/tesoreria/cartolas',
  '/comercial/clientes',
  '/comercial/ordenes-venta',
  '/comercial/emitir',
  '/comercial/prospectos',
];

const browser = await chromium.launch({
  executablePath: 'C:/Users/c/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe',
  headless: true,
});
const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
page.setDefaultTimeout(12000);

async function masTarde() {
  const btn = page.getByRole('button', { name: 'Más tarde', exact: true });
  if (await btn.count() && await btn.first().isVisible().catch(() => false)) {
    await btn.first().click().catch(() => {});
    await page.waitForTimeout(200);
  }
}

async function measure() {
  return page.evaluate(() => {
    const dialogs = [...document.querySelectorAll('[role="dialog"]')].filter((d) => d.getBoundingClientRect().width > 40);
    const dialog = dialogs[dialogs.length - 1];
    const root = dialog || document.body;
    const title = (dialog?.querySelector('h2,h1') || document.querySelector('h1'))?.textContent?.trim().slice(0, 90) || '';
    const labels = [...root.querySelectorAll('label')]
      .map((l) => (l.textContent || '').replace(/\s+/g, ' ').trim())
      .filter(Boolean)
      .slice(0, 24);
    const grids = [...root.querySelectorAll('.grid')].map((g) => {
      const cs = getComputedStyle(g);
      const cols = cs.gridTemplateColumns.split(' ').filter((x) => x && x !== 'none').length;
      const kids = [...g.children];
      const empty = kids.filter((k) => {
        const t = (k.textContent || '').trim();
        const hasControl = k.querySelector('input,select,textarea,button');
        return !t && !hasControl;
      }).length;
      return {
        cols,
        kids: kids.length,
        empty,
        gap: cs.columnGap,
        cls: String(g.className).slice(0, 140),
      };
    }).filter((g) => g.cols >= 2 && g.kids > 0);
    return { dialog: Boolean(dialog), title, nLabels: labels.length, labels, grids };
  });
}

function flags(m) {
  if (!m?.dialog && !m?.grids) return [];
  const outFlags = [];
  for (const g of m.grids || []) {
    if (g.cols >= 3 && m.nLabels > 0 && m.nLabels < 4) outFlags.push('3-cols-con-menos-de-4-campos');
    if (g.empty > 0 && g.cols >= 2) outFlags.push(`celda-vacia:${g.empty}`);
    if (g.cols >= 3 && g.kids > 0 && g.kids < 4) outFlags.push('grilla-3-corta');
  }
  return [...new Set(outFlags)];
}

async function cerrar() {
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(150);
  const cancel = page.getByRole('button', { name: 'Cancelar', exact: true });
  if (await cancel.count() && await cancel.first().isVisible().catch(() => false)) {
    await cancel.first().click().catch(() => {});
  }
}

async function abrirPrimero() {
  const candidatos = page.getByRole('button', { name: /^(Nuevo|Nueva|Crear|Agregar)\b/ });
  const n = await candidatos.count();
  for (let i = 0; i < n; i += 1) {
    const b = candidatos.nth(i);
    if (await b.isVisible().catch(() => false)) {
      const name = (await b.innerText()).replace(/\s+/g, ' ').trim();
      await b.click();
      await page.waitForTimeout(450);
      return name;
    }
  }
  return null;
}

const report = [];

await page.goto('http://127.0.0.1:5174/login', { waitUntil: 'domcontentloaded' });
await page.locator('input[type=email]').fill('admin@almahue.local');
await page.locator('input[type=password]').fill('Admin123!');
await page.getByRole('button', { name: 'Entrar con clave' }).click();
await page.waitForURL((u) => !u.pathname.endsWith('/login'), { timeout: 25000 });
await masTarde();

for (const path of routes) {
  const id = path.replace(/\//g, '_').replace(/^_/, '');
  try {
    await page.goto(`http://127.0.0.1:5174${path}`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(700);
    await masTarde();
    const overlay = await page.locator('vite-error-overlay').count();
    const button = await abrirPrimero();
    const m = await measure();
    const f = flags(m);
    const shot = Boolean(button) || path.endsWith('/nueva') || path.endsWith('/emitir') || f.length > 0;
    if (shot) await page.screenshot({ path: `${out}/${id}.png` });
    report.push({ path, button, overlay, flags: f, ...m });
    console.log(path, button || '-', f.join(',') || 'ok', m.title);
    if (button) await cerrar();
  } catch (e) {
    report.push({ path, error: String(e).slice(0, 240) });
    console.log(path, 'ERROR', String(e).slice(0, 160));
    await page.keyboard.press('Escape').catch(() => {});
  }
}

try {
  await page.goto('http://127.0.0.1:5174/admin/aprobaciones', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(600);
  await masTarde();
  await page.getByRole('button', { name: 'Configurar' }).click();
  await page.waitForTimeout(300);
  await page.getByRole('button', { name: 'Nuevo grupo' }).click();
  await page.waitForTimeout(400);
  const grupo = await measure();
  await page.screenshot({ path: `${out}/aprobaciones-grupo.png` });
  report.push({ path: '/admin/aprobaciones#grupo', button: 'Nuevo grupo', flags: flags(grupo), ...grupo });
  console.log('grupo', flags(grupo).join(',') || 'ok', grupo.title);
  await cerrar();
  await page.getByRole('button', { name: 'Configurar' }).click().catch(() => {});
  await page.getByRole('button', { name: 'Suplencias' }).click();
  await page.getByRole('button', { name: 'Nueva suplencia' }).click();
  await page.waitForTimeout(400);
  const supl = await measure();
  await page.screenshot({ path: `${out}/aprobaciones-suplencia.png` });
  report.push({ path: '/admin/aprobaciones#suplencia', button: 'Nueva suplencia', flags: flags(supl), ...supl });
  console.log('suplencia', flags(supl).join(',') || 'ok', supl.title);
  await cerrar();
  await page.keyboard.press('Escape');
  const maria = page.getByText('María González', { exact: true }).first();
  if (await maria.count()) {
    await maria.click();
    await page.getByRole('button', { name: 'Editar', exact: true }).first().click();
    await page.waitForTimeout(400);
    const escala = await measure();
    await page.screenshot({ path: `${out}/aprobaciones-escala.png` });
    report.push({ path: '/admin/aprobaciones#escala', button: 'Editar', flags: flags(escala), ...escala });
    console.log('escala', flags(escala).join(',') || 'ok', escala.title);
  }
} catch (e) {
  report.push({ path: '/admin/aprobaciones#extra', error: String(e).slice(0, 240) });
  console.log('extra ERROR', String(e).slice(0, 180));
}

await writeFile(`${out}/reporte.json`, JSON.stringify(report, null, 2));
await browser.close();
console.log('listo', report.length);
