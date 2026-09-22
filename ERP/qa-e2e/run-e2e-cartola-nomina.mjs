/**
 * Sergio 14/09 (coda post-demo): nómina solo en egreso de cartola.
 * Front demo: http://127.0.0.1:5174
 */
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const BASE = process.env.E2E_BASE || 'http://127.0.0.1:5174';
const ADMIN_EMAIL = process.env.E2E_EMAIL || 'admin@almahue.local';
const ADMIN_PASS = process.env.E2E_PASS || 'Admin123!';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, 'resultados');
const stamp = new Date().toISOString().slice(0, 10);
const results = [];

function record(id, result, evidence, extra) {
  const row = { id, result, evidence, ...(extra ? { extra } : {}) };
  results.push(row);
  console.log(`[${result}] ${id}: ${evidence}`);
}

async function launchBrowser() {
  const attempts = [{ channel: 'chrome' }, { channel: 'msedge' }, {}];
  let last;
  for (const opts of attempts) {
    try {
      return await chromium.launch({ headless: true, ...opts });
    } catch (e) {
      last = e;
    }
  }
  throw last;
}

async function dismissPeriodo(page) {
  const heading = page.getByRole('heading', { name: /periodo contable/i });
  try {
    await heading.waitFor({ state: 'visible', timeout: 2500 });
  } catch {
    return;
  }
  const confirmar = page.getByRole('button', { name: /Confirmar \d{4}-\d{2}/ });
  if (await confirmar.count()) {
    await confirmar.click({ timeout: 8000 });
    await heading.waitFor({ state: 'hidden', timeout: 8000 }).catch(() => {});
    return;
  }
  await page.getByRole('button', { name: /Más tarde/i }).click().catch(() => {});
}

async function login(page) {
  const res = await page.goto(`${BASE}/login`, { waitUntil: 'load', timeout: 30000 });
  if (!res || !res.ok()) {
    throw new Error(`GET /login → ${res?.status()} ${page.url()}`);
  }
  const email = page.locator('input[type="email"], input[autocomplete="username"]').first();
  await email.waitFor({ state: 'visible', timeout: 45000 });
  await email.fill(ADMIN_EMAIL);
  await page.locator('input[type="password"]').fill(ADMIN_PASS);
  await page.getByRole('button', { name: /Entrar con clave/i }).click();
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: 25000 });
}

async function enableFreshDemo(page) {
  const btn = page.getByRole('button', { name: /Modo (demo|real)/i });
  await btn.waitFor({ state: 'visible', timeout: 15000 });
  const label = (await btn.innerText()).replace(/\s+/g, ' ').trim();
  if (/demo/i.test(label)) {
    await btn.click();
    await page.getByRole('button', { name: /Modo real/i }).waitFor({ timeout: 8000 });
  }
  await page.getByRole('button', { name: /Modo real/i }).click();
  await page.getByRole('button', { name: /Modo demo/i }).waitFor({ timeout: 8000 });
  await dismissPeriodo(page);
}

async function optionValues(locator) {
  return locator.locator('option').evaluateAll((opts) =>
    opts.map((o) => (o.value || '').trim()).filter(Boolean),
  );
}

async function shot(page, name) {
  mkdirSync(outDir, { recursive: true });
  await page.screenshot({ path: join(outDir, `${stamp}-cartola-nomina-${name}.png`), fullPage: true });
}

async function main() {
  mkdirSync(outDir, { recursive: true });
  const browser = await launchBrowser();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  page.setDefaultTimeout(15000);

  try {
    await login(page);
    await dismissPeriodo(page);
    record('SERGIO-LOGIN', 'PASS', `Login OK → ${page.url()}`);
  } catch (e) {
    record('SERGIO-LOGIN', 'BLOCKED', String(e));
    await shot(page, 'login-fail').catch(() => {});
    await browser.close();
    writeReport();
    process.exit(1);
  }

  try {
    await enableFreshDemo(page);
    record('SERGIO-DEMO', 'PASS', 'Modo demo fresco (agosto 2026)');
  } catch (e) {
    record('SERGIO-DEMO', 'FAIL', String(e));
    await shot(page, 'demo-fail').catch(() => {});
  }

  try {
    await page.goto(`${BASE}/tesoreria/cartolas`, { waitUntil: 'load', timeout: 30000 });
    await dismissPeriodo(page);
    await page.getByRole('heading', { name: 'Cartolas bancarias' }).waitFor({ state: 'visible', timeout: 15000 });
    const buscar = page.getByPlaceholder(/Buscar banco/i);
    await buscar.waitFor({ state: 'visible', timeout: 10000 });
    await buscar.fill('Banco Estado');
    await page.getByRole('button', { name: 'Aplicar' }).click();
    const row = page.locator('tbody tr').filter({ hasText: 'Banco Estado' }).filter({ hasText: '2026/08' }).first();
    await row.waitFor({ state: 'visible', timeout: 20000 });
    await row.getByRole('button', { name: 'Trabajar' }).click();
    await page.getByRole('heading', { name: /Banco Estado/i }).waitFor({ state: 'visible', timeout: 10000 });
    await page.getByText('DEP-910').waitFor({ state: 'visible', timeout: 10000 });
    await page.getByText('COM-20').waitFor({ state: 'visible', timeout: 10000 });
    record('SERGIO-CARTOLA', 'PASS', 'Cartola Estado ago14 abierta con DEP-910 y COM-20');
  } catch (e) {
    record('SERGIO-CARTOLA', 'FAIL', String(e));
    await shot(page, 'cartola-fail').catch(() => {});
    await browser.close();
    writeReport();
    process.exit(results.some((r) => r.result === 'FAIL' || r.result === 'BLOCKED') ? 1 : 0);
  }

  try {
    const ingreso = page.locator('div.rounded.border').filter({ hasText: 'DEP-910' }).first();
    await ingreso.getByRole('button', { name: 'Contabilizar' }).click();
    await ingreso.getByRole('button', { name: 'Confirmar contabilización' }).waitFor({ state: 'visible' });
    const nominaT2 = page.getByLabel('Nómina semanal del movimiento');
    const visible = await nominaT2.isVisible().catch(() => false);
    if (visible) {
      record('SERGIO-INGRESO-SIN-NOMINA', 'FAIL', 'El ingreso DEP-910 muestra el campo Nómina');
      await shot(page, 'ingreso-nomina');
    } else {
      record('SERGIO-INGRESO-SIN-NOMINA', 'PASS', 'Contabilizar DEP-910 (ingreso) no muestra Nómina');
    }
    await ingreso.getByRole('button', { name: 'Cancelar' }).click();
  } catch (e) {
    record('SERGIO-INGRESO-SIN-NOMINA', 'FAIL', String(e));
    await shot(page, 'ingreso-fail').catch(() => {});
  }

  try {
    const egreso = page.locator('div.rounded.border').filter({ hasText: 'COM-20' }).first();
    await egreso.getByRole('button', { name: 'Contabilizar' }).click();
    const nominaT2 = page.getByLabel('Nómina semanal del movimiento');
    await nominaT2.waitFor({ state: 'visible', timeout: 8000 });
    const values = await optionValues(nominaT2);
    const hasAgosto = values.includes('2026-08-S1') && values.includes('2026-08-S2');
    const calendarLeak = values.includes('2026-09-S3');
    if (!hasAgosto) {
      record('SERGIO-EGRESO-NOMINA', 'FAIL', `Faltan semanas 2026-08 en T2: ${values.join(', ')}`);
      await shot(page, 'egreso-semanas');
    } else if (calendarLeak) {
      record(
        'SERGIO-EGRESO-NOMINA',
        'FAIL',
        `El combo usa el mes de calendario (2026-09-S3) en vez del periodo 2026-08: ${values.join(', ')}`,
      );
      await shot(page, 'egreso-calendario');
    } else {
      await nominaT2.selectOption('2026-08-S2');
      record('SERGIO-EGRESO-NOMINA', 'PASS', 'COM-20 muestra Nómina y se elige 2026-08-S2');
    }
    await egreso.getByRole('button', { name: 'Cancelar' }).click();
  } catch (e) {
    record('SERGIO-EGRESO-NOMINA', 'FAIL', String(e));
    await shot(page, 'egreso-fail').catch(() => {});
  }

  try {
    const tipo = page.getByLabel('Filtrar ingresos o egresos');
    await tipo.selectOption('INGRESO');
    const asociarIngreso = page.getByRole('button', { name: 'Asociar nómina' });
    const visibleIngreso = await asociarIngreso.isVisible().catch(() => false);
    if (visibleIngreso) {
      record('SERGIO-LOTE-INGRESO', 'FAIL', 'Asociar nómina aparece con filtro Ingresos');
      await shot(page, 'lote-ingreso');
    } else {
      record('SERGIO-LOTE-INGRESO', 'PASS', 'Filtro Ingresos oculta Asociar nómina');
    }

    await tipo.selectOption('EGRESO');
    const asociar = page.getByRole('button', { name: 'Asociar nómina' });
    await asociar.waitFor({ state: 'visible', timeout: 5000 });
    const lote = page.getByLabel('Nómina semanal');
    await lote.waitFor({ state: 'visible' });
    await page.getByLabel('Seleccionar egreso COM-20').check();
    await lote.selectOption('2026-08-S2');
    await asociar.click();
    await page.getByText('Nómina 2026-08-S2', { exact: true }).waitFor({ state: 'visible', timeout: 8000 });
    record('SERGIO-LOTE-EGRESO', 'PASS', 'Egreso COM-20 asociado a nómina 2026-08-S2');
  } catch (e) {
    record('SERGIO-LOTE-EGRESO', 'FAIL', String(e));
    await shot(page, 'lote-fail').catch(() => {});
  }

  await browser.close();
  writeReport();
  const failed = results.filter((r) => r.result === 'FAIL' || r.result === 'BLOCKED').length;
  process.exit(failed ? 1 : 0);
}

function writeReport() {
  const pass = results.filter((r) => r.result === 'PASS').length;
  const fail = results.filter((r) => r.result === 'FAIL').length;
  const blocked = results.filter((r) => r.result === 'BLOCKED').length;
  const jsonPath = join(outDir, `${stamp}-testrim-cartola-nomina.json`);
  const mdPath = join(outDir, `${stamp}-testrim-cartola-nomina.md`);
  writeFileSync(jsonPath, JSON.stringify({ stamp, base: BASE, pass, fail, blocked, results }, null, 2));
  const lines = [
    `# Cartola × nómina (Sergio 14/09) ${stamp}`,
    '',
    `Base: ${BASE} · PASS ${pass} · FAIL ${fail} · BLOCKED ${blocked}`,
    '',
    ...results.map((r) => `- **${r.result}** \`${r.id}\`: ${r.evidence}`),
    '',
  ];
  writeFileSync(mdPath, lines.join('\n'));
  console.log(`\nWrote ${jsonPath}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
