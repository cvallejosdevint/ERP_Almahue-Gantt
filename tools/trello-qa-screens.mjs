/**
 * Capturas locales 1920x1080 para tarjetas QA Trello.
 * No commitear las PNG.
 */
import { chromium } from 'playwright-core';
import { mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const BASE = process.env.E2E_BASE || 'http://127.0.0.1:5174';
const ADMIN_EMAIL = process.env.E2E_EMAIL || 'admin@almahue.local';
const ADMIN_PASS = process.env.E2E_PASS || 'Admin123!';
const EMPRESA_HINT = process.env.E2E_EMPRESA || 'EXPORT';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = 'E:\\source\\repos\\Almahue\\.tmp-trello-qa';
mkdirSync(outDir, { recursive: true });

export const PAGES = [
  { slug: 'inicio-login', path: '/login', title: 'Inicio - Inicio de sesion', beforeLogin: true },
  { slug: 'inicio-panel', path: '/', title: 'Inicio - Panel operativo' },
  { slug: 'admin-plantilla', path: '/admin/plantilla-documentos', title: 'Administración - Plantilla documentos' },
  { slug: 'param-monedas', path: '/catalogos/monedas', title: 'Parametrización - Monedas' },
  { slug: 'param-unidades', path: '/catalogos/unidades', title: 'Parametrización - Unidades de medida' },
  { slug: 'param-cc', path: '/catalogos/centros-costo', title: 'Parametrización - Centros de costo' },
  { slug: 'param-elementos', path: '/catalogos/elementos-costo', title: 'Parametrización - Elementos de costo' },
  { slug: 'param-areas', path: '/catalogos/areas-negocio', title: 'Parametrización - Areas de negocio' },
  { slug: 'param-codigos', path: '/catalogos/codigos-financieros', title: 'Parametrización - Codigos financieros' },
  { slug: 'param-tipos', path: '/catalogos/tipos-documento', title: 'Parametrización - Tipos de documento' },
  { slug: 'param-plan', path: '/catalogos/plan-cuentas', title: 'Parametrización - Plan de cuentas' },
  { slug: 'param-indicadores', path: '/catalogos/indicadores-bc', title: 'Parametrización - Indicadores BC' },
  { slug: 'param-proveedores', path: '/catalogos/proveedores', title: 'Parametrización - Proveedores' },
  { slug: 'ctr-listado', path: '/contratistas', title: 'Contratistas - Listado' },
  { slug: 'ctr-ingreso', path: '/contratistas/ingreso-diario', title: 'Contratistas - Ingreso diario' },
  { slug: 'ctr-asociacion', path: '/contratistas/asociacion', title: 'Contratistas - Asociacion labores' },
  { slug: 'ctr-tarifas', path: '/contratistas/tarifas', title: 'Contratistas - Tarifas / labores' },
  { slug: 'ctr-proformas', path: '/contratistas/proformas', title: 'Contratistas - Proformas y facturas' },
  { slug: 'ctr-traspaso', path: '/contratistas/traspaso', title: 'Contratistas - Traspaso y cierre' },
  { slug: 'compras-oc', path: '/compras/ordenes', title: 'Compras - Ordenes de compra', example: true },
  { slug: 'compras-aprob', path: '/compras/aprobaciones', title: 'Compras - Aprobaciones', example: true },
  { slug: 'compras-recep', path: '/compras/recepciones', title: 'Compras - Recepciones' },
  { slug: 'compras-libro', path: '/compras/registro', title: 'Compras - Libro de compras', example: true },
  { slug: 'insumos-maestro', path: '/insumos/maestro', title: 'Insumos / Bodega - Maestro articulos' },
  { slug: 'insumos-bodegas', path: '/insumos/bodegas', title: 'Insumos / Bodega - Bodegas' },
  { slug: 'insumos-stock', path: '/insumos/stock', title: 'Insumos / Bodega - Stock por bodega / producto' },
  { slug: 'insumos-mov', path: '/insumos/movimientos', title: 'Insumos / Bodega - Movimientos / NC' },
  { slug: 'conta-periodos', path: '/contabilidad/periodos', title: 'Contabilidad - Periodos contables' },
  { slug: 'conta-sii', path: '/contabilidad/config-sii', title: 'Contabilidad - Cuentas por tipo de documento' },
  { slug: 'conta-asientos', path: '/contabilidad/asientos', title: 'Contabilidad - Comprobantes / asientos' },
  { slug: 'conta-central', path: '/contabilidad/centralizacion', title: 'Contabilidad - Centralizacion masiva' },
  { slug: 'conta-honorarios', path: '/contabilidad/honorarios', title: 'Contabilidad - Factores honorarios' },
  { slug: 'conta-presup', path: '/presupuestos', title: 'Contabilidad - Presupuestos' },
  { slug: 'conta-diario', path: '/contabilidad/libro-diario', title: 'Contabilidad - Libro diario' },
  { slug: 'conta-mayor', path: '/contabilidad/mayor', title: 'Contabilidad - Libro mayor' },
  { slug: 'conta-balance', path: '/contabilidad/balance-8-columnas', title: 'Contabilidad - Balance de 8 columnas' },
  { slug: 'conta-resumen', path: '/contabilidad/reportes', title: 'Contabilidad - Resumen contable' },
  { slug: 'teso-cartolas', path: '/tesoreria/cartolas', title: 'Tesorería - Cartolas' },
  { slug: 'teso-conc', path: '/tesoreria/conciliacion', title: 'Tesorería - Conciliacion' },
  { slug: 'teso-flujo', path: '/tesoreria/flujo-caja', title: 'Tesorería - Flujo de caja' },
  { slug: 'teso-pagos', path: '/tesoreria/pagos', title: 'Tesorería - Pagos' },
  { slug: 'teso-nomina', path: '/tesoreria/nominas', title: 'Tesorería - Nomina semanal' },
  { slug: 'teso-cc', path: '/tesoreria/cuentas-corrientes', title: 'Tesorería - Estado de cuenta' },
];

async function launchBrowser() {
  const attempts = [
    { channel: 'chrome' },
    { channel: 'msedge' },
    {},
  ];
  let last;
  for (const opts of attempts) {
    try {
      return await chromium.launch({
        headless: true,
        ...opts,
        args: ['--window-size=1920,1080'],
      });
    } catch (e) {
      last = e;
    }
  }
  throw last;
}

async function dismissPeriodo(page) {
  const heading = page.getByRole('heading', { name: /periodo contable/i });
  try {
    await heading.waitFor({ state: 'visible', timeout: 2000 });
  } catch {
    return;
  }
  const confirmar = page.getByRole('button', { name: /Confirmar \d{4}-\d{2}/ });
  if (await confirmar.count()) {
    await confirmar.click({ timeout: 8000 });
    await heading.waitFor({ state: 'hidden', timeout: 8000 }).catch(() => {});
    return;
  }
  await page.getByRole('button', { name: /Más tarde|Mas tarde/i }).click().catch(() => {});
}

async function login(page) {
  await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded', timeout: 30000 });
  const email = page.locator('input[type="email"]').first();
  await email.waitFor({ state: 'visible', timeout: 45000 });
  await email.fill(ADMIN_EMAIL);
  await page.locator('input[type="password"]').fill(ADMIN_PASS);
  await page.getByRole('button', { name: /Entrar con clave/i }).click();
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: 25000 });
  await dismissPeriodo(page);
}

async function selectEmpresa(page, hint) {
  const trigger = page.locator('button').filter({
    hasText: /SPA|Almahue|empresa|EXPORT|SERVICES|Seleccionar/i,
  }).first();
  await trigger.click({ timeout: 8000 }).catch(() => {});
  const search = page.getByPlaceholder(/Buscar por RUT/i);
  if (await search.count()) {
    await search.fill(hint);
    await page.waitForTimeout(400);
    const opt = page.locator('ul button').filter({ hasText: new RegExp(hint, 'i') }).first();
    if (await opt.count()) await opt.click();
    else await page.keyboard.press('Escape');
  }
}

async function shot(page, slug) {
  const file = join(outDir, `${slug}.png`);
  await page.waitForTimeout(700);
  await page.screenshot({ path: file, type: 'png' });
  console.log('OK', slug, file);
  return file;
}

async function main() {
  const browser = await launchBrowser();
  const page = await browser.newPage({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 1,
  });
  page.setDefaultTimeout(20000);

  await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.locator('input[type="email"]').first().waitFor({ state: 'visible', timeout: 45000 });
  await shot(page, 'inicio-login');

  await login(page);
  await selectEmpresa(page, EMPRESA_HINT);
  await dismissPeriodo(page);

  for (const p of PAGES) {
    if (p.beforeLogin) continue;
    await page.goto(`${BASE}${p.path}`, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await dismissPeriodo(page);
    await shot(page, p.slug);
  }

  await browser.close();
  console.log('DIR', outDir);
}

const isDirect = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isDirect) {
  main().catch((e) => {
    console.error(e);
    process.exit(1);
  });
}
