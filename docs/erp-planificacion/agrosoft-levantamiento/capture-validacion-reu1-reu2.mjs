/**
 * Capturas ERP demo para validar cobertura Reunión 1 + Reunión 2.
 * Nota Reu 2: en el video el presentador pasó pantallas muy rápido;
 * esta corrida usa waits estables (no frame-a-frame del video).
 *
 * Uso (front en :5174, modo demo):
 *   node capture-validacion-reu1-reu2.mjs
 */
import { chromium } from 'playwright';
import { mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = join(__dirname, 'capturas-validacion-erp');
mkdirSync(OUT, { recursive: true });
mkdirSync(join(OUT, 'reu1'), { recursive: true });
mkdirSync(join(OUT, 'reu2'), { recursive: true });

const BASE = (process.env.BASE_URL || 'http://localhost:5174').replace(/\/$/, '');
const NAV_TIMEOUT = 45000;
const WAIT_MS = 1800;

/** Reu 1 — pantallas legacy vs rutas ERP */
const REU1 = [
  { url: '/login', file: 'reu1/01-login.png', label: 'Login', guest: true },
  { url: '/', file: 'reu1/02-panel.png', label: 'Panel' },
  { url: '/contratistas/tarifas', file: 'reu1/03-tarifas.png', label: 'Tarifas', open: /agregar tarifa/i },
  { url: '/catalogos/centros-costo', file: 'reu1/04-centros-costo.png', label: 'Centros costo' },
  { url: '/admin/roles', file: 'reu1/05-roles.png', label: 'Roles' },
  { url: '/compras/ordenes', file: 'reu1/06-orden-compra.png', label: 'OC' },
  { url: '/compras/aprobaciones', file: 'reu1/08-aprobacion-oc.png', label: 'Aprobación OC' },
  { url: '/compras/recepciones', file: 'reu1/09-recepcion.png', label: 'Recepción' },
  { url: '/compras/registro', file: 'reu1/10-registro-compra.png', label: 'Registro compra' },
  { url: '/insumos/maestro', file: 'reu1/11-maestro.png', label: 'Maestro artículos' },
  { url: '/insumos/bodegas', file: 'reu1/12-bodegas.png', label: 'Bodegas' },
  { url: '/insumos/movimientos', file: 'reu1/13-movimientos.png', label: 'Movimientos/NC' },
  { url: '/contabilidad/asientos', file: 'reu1/14-asientos.png', label: 'Asientos' },
  { url: '/contabilidad/indicadores-bc', file: 'reu1/15-indicadores-bc.png', label: 'Indicadores BC' },
  { url: '/contratistas/proformas', file: 'reu1/16-proformas.png', label: 'Proformas' },
  { url: '/contratistas/traspaso', file: 'reu1/17-traspaso.png', label: 'Traspaso' },
];

/** Reu 2 — lo mostrado en demo (pantallas rápidas del video → captura estable en ERP) */
const REU2 = [
  { url: '/contratistas/tarifas', file: 'reu2/01-tarifas-filtro-labor.png', label: 'Tarifas + filtro labor', open: /agregar tarifa/i },
  { url: '/contratistas/proformas', file: 'reu2/02-proformas-n1.png', label: 'Proformas N:1', click: /^Definitiva$/i, shotAs: 'reu2/02-proformas-confirm-definitiva.png' },
  { url: '/contratistas/ingreso-diario', file: 'reu2/03-ingreso-diario.png', label: 'Ingreso diario', open: /nuevo ingreso/i },
  { url: '/contratistas/asociacion', file: 'reu2/04-asociacion-labores.png', label: 'Asociación labores' },
  { url: '/contratistas/traspaso', file: 'reu2/05-traspaso-cierre.png', label: 'Traspaso cierre' },
  { url: '/comercial/libro', file: 'reu2/06-libro-comercial.png', label: 'Libro comercial' },
  { url: '/tesoreria/pagos', file: 'reu2/07-pagos-tc.png', label: 'Pagos TC', open: /nuevo pago/i },
  { url: '/tesoreria/cartolas', file: 'reu2/08-carga-cartola.png', label: 'Carga cartola' },
  { url: '/tesoreria/conciliacion', file: 'reu2/09-conciliacion.png', label: 'Conciliación', click: /^Movimientos$/i, shotAs: 'reu2/09-conciliacion-movimientos.png' },
  { url: '/tesoreria/anticipos', file: 'reu2/10-anticipos.png', label: 'Anticipos' },
  { url: '/admin/roles', file: 'reu2/11-roles-matriz.png', label: 'Roles R/W' },
  { url: '/catalogos/centros-costo', file: 'reu2/12-centros-encargado.png', label: 'CC encargado' },
  { url: '/catalogos/monedas', file: 'reu2/13-monedas-sync-bc.png', label: 'Monedas sync BC' },
  { url: '/contabilidad/indicadores-bc', file: 'reu2/14-indicadores-sync.png', label: 'Indicadores sync' },
  { url: '/integraciones/gosocket', file: 'reu2/15-gosocket-dec14.png', label: 'GoSocket DEC-14' },
  { url: '/', file: 'reu2/16-panel-demo.png', label: 'Panel demo' },
];

async function ensureDemoLogin(page) {
  await page.goto(`${BASE}/login`, { waitUntil: 'networkidle', timeout: NAV_TIMEOUT });
  await page.evaluate(() => {
    localStorage.setItem('almahue-erp-demo-mode', 'true');
  });
  // Si ya hay sesión, AuthProvider puede redirigir fuera de /login
  if (!page.url().includes('/login')) {
    await page.waitForTimeout(WAIT_MS);
    return;
  }
  await page.waitForSelector('input[type="email"]', { timeout: NAV_TIMEOUT });
  await page.fill('input[type="email"]', 'admin@almahue.local');
  await page.fill('input[type="password"]', 'Admin123!');
  await page.click('button[type="submit"]');
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: NAV_TIMEOUT });
  await page.waitForTimeout(WAIT_MS);
}

async function capture(page, shot) {
  if (shot.guest) {
    await page.goto(`${BASE}${shot.url}`, { waitUntil: 'networkidle', timeout: NAV_TIMEOUT });
    await page.evaluate(() => {
      localStorage.setItem('almahue-erp-demo-mode', 'true');
      // limpiar sesión para ver login real
      Object.keys(localStorage).forEach((k) => {
        if (k !== 'almahue-erp-demo-mode' && (k.includes('token') || k.includes('auth') || k.includes('almahue'))) {
          if (k !== 'almahue-erp-demo-mode') localStorage.removeItem(k);
        }
      });
    });
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForTimeout(WAIT_MS);
    await page.screenshot({ path: join(OUT, shot.file), fullPage: true });
    console.log('OK', shot.label, '->', shot.file);
    return;
  }

  await page.goto(`${BASE}${shot.url}`, { waitUntil: 'networkidle', timeout: NAV_TIMEOUT });
  await page.waitForTimeout(WAIT_MS);

  const listPath = join(OUT, shot.file);
  await page.screenshot({ path: listPath, fullPage: true });
  console.log('OK', shot.label, '->', shot.file);

  if (shot.open) {
    const btn = page.getByRole('button', { name: shot.open });
    if (await btn.count()) {
      await btn.first().click();
      await page.waitForTimeout(700);
      const modalFile = shot.file.replace('.png', '-form.png');
      await page.screenshot({ path: join(OUT, modalFile), fullPage: true });
      console.log('OK', shot.label, 'form ->', modalFile);
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300);
    } else {
      console.warn('SKIP form', shot.label);
    }
  }

  if (shot.click) {
    const btn = page.getByRole('button', { name: shot.click });
    if (await btn.count()) {
      await btn.first().click();
      await page.waitForTimeout(900);
      const modalFile = shot.shotAs || shot.file.replace('.png', '-action.png');
      await page.screenshot({ path: join(OUT, modalFile), fullPage: true });
      console.log('OK', shot.label, 'action ->', modalFile);
      await page.keyboard.press('Escape');
      await page.waitForTimeout(300);
    } else {
      console.warn('SKIP click', shot.label);
    }
  }
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  try {
    // Login primero (sin sesión) para captura guest; luego autenticar
    console.log('--- REU 1 ---');
    const guest = REU1.filter((s) => s.guest);
    const logged = REU1.filter((s) => !s.guest);
    for (const s of guest) await capture(page, s);
    await ensureDemoLogin(page);
    for (const s of logged) await capture(page, s);

    console.log('--- REU 2 ---');
    for (const s of REU2) await capture(page, s);
    console.log('\nListo:', OUT);
  } catch (err) {
    console.error('ERROR:', err.message);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
}

main();
