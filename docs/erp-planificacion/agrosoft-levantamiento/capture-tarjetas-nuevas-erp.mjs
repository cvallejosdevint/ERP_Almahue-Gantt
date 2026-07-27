/**
 * Capturas pantallas nuevas Reunión 1 — ERP mock (erp_front)
 * Uso: node capture-tarjetas-nuevas-erp.mjs
 */
import { chromium } from 'playwright';
import { mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = join(__dirname, '..', 'docs', 'erp-planificacion', 'agrosoft-levantamiento', 'pantallas-legacy');
mkdirSync(OUT, { recursive: true });

const BASE = (process.env.BASE_URL || 'http://localhost:5174').replace(/\/$/, '');
const NAV_TIMEOUT = 45000;
const WAIT_MS = 2000;

const SHOTS = [
  { url: '/contratistas/proformas', file: '16-proformas-contratista.png', label: 'Proformas' },
  { url: '/contratistas/traspaso', file: '17-traspaso-cierre-contratistas.png', label: 'Traspaso' },
  { url: '/contratistas/tarifas', file: '03-tarifas-contratista.png', label: 'Tarifas' },
  { url: '/compras/ordenes', file: '06-orden-compra.png', label: 'OC' },
  { url: '/compras/recepciones', file: '09-recepcion-oc.png', label: 'Recepción' },
  { url: '/compras/registro', file: '10-registro-compra.png', label: 'Registro' },
  { url: '/insumos/bodegas', file: '12-bodegas.png', label: 'Bodegas' },
  { url: '/insumos/movimientos', file: '13-nc-devolucion.png', label: 'Movimientos' },
  { url: '/contabilidad/indicadores-bc', file: '15-indicadores-bc.png', label: 'Indicadores BC' },
];

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  try {
    await page.goto(`${BASE}/login`, { waitUntil: 'networkidle', timeout: NAV_TIMEOUT });
    await page.evaluate(() => localStorage.setItem('almahue-erp-demo-mode', 'true'));
    await page.fill('input[type="email"]', 'admin@almahue.local');
    await page.fill('input[type="password"]', 'Admin123!');
    await page.click('button[type="submit"]');
    await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: NAV_TIMEOUT });
    await page.waitForTimeout(WAIT_MS);

    for (const s of SHOTS) {
      await page.goto(`${BASE}${s.url}`, { waitUntil: 'networkidle', timeout: NAV_TIMEOUT });
      await page.waitForTimeout(WAIT_MS);
      const path = join(OUT, s.file);
      await page.screenshot({ path, fullPage: true });
      console.log('OK', s.label, '->', s.file);
    }
  } catch (err) {
    console.error('ERROR:', err.message);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
}

main();
