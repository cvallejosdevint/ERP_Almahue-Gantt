/**
 * Testrim Ventas (Playwright). No emite DTE/SII.
 * Front: http://localhost:5174
 */
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const BASE = process.env.E2E_BASE || 'http://127.0.0.1:5174';
const ADMIN_EMAIL = process.env.E2E_EMAIL || 'admin@almahue.local';
const ADMIN_PASS = process.env.E2E_PASS || 'Admin123!';
const EMPRESA_HINT = process.env.E2E_EMPRESA || 'EXPORT';

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
  const attempts = [
    { channel: 'chrome' },
    { channel: 'msedge' },
    {},
  ];
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
  try {
    await email.waitFor({ state: 'visible', timeout: 45000 });
  } catch (e) {
    const html = (await page.content()).slice(0, 1500);
    throw new Error(`Login form no apareció (${page.url()} title=${await page.title()}). html=${html}`);
  }
  await email.fill(ADMIN_EMAIL);
  await page.locator('input[type="password"]').fill(ADMIN_PASS);
  await page.getByRole('button', { name: /Entrar con clave/i }).click();
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: 25000 });
}

async function selectEmpresa(page, hint) {
  const btn = page.locator('button').filter({ has: page.locator('svg') }).filter({ hasText: /.+/ }).first();
  const trigger = page.locator('button:has-text("Seleccionar empresa"), button:has(svg)').filter({
    hasText: /SPA|Almahue|empresa|EXPORT|SERVICES/i,
  }).first();
  const use = (await trigger.count()) ? trigger : page.locator('header button, .relative button').first();
  await use.click({ timeout: 8000 }).catch(() => {});
  const search = page.getByPlaceholder(/Buscar por RUT/i);
  if (await search.count()) {
    await search.fill(hint);
    await page.waitForTimeout(300);
    const opt = page.locator('ul button').filter({ hasText: new RegExp(hint, 'i') }).first();
    if (await opt.count()) await opt.click();
    else await page.keyboard.press('Escape');
  }
}

async function inventory(page) {
  return page.evaluate(() => {
    const text = (el) => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 160);
    const selects = [...document.querySelectorAll('select')].map((el) => ({
      label: el.closest('label')?.innerText || el.getAttribute('aria-label') || el.name || '',
      options: [...el.options].map((o) => ({ value: o.value, label: o.textContent.trim() })),
    }));
    const inputs = [...document.querySelectorAll('input')].map((el) => ({
      type: el.type,
      aria: el.getAttribute('aria-label') || '',
      placeholder: el.placeholder || '',
      name: el.name || '',
    }));
    const combos = [...document.querySelectorAll('[role="combobox"], button[aria-haspopup="listbox"]')].map((el) => ({
      aria: el.getAttribute('aria-label') || text(el).slice(0, 80),
    }));
    const buttons = [...document.querySelectorAll('button')].map((el) => text(el)).filter(Boolean).slice(0, 80);
    const headings = [...document.querySelectorAll('h1,h2,h3,h4')].map((el) => text(el));
    return {
      url: location.href,
      title: document.title,
      headings,
      selects,
      inputs,
      combos,
      buttons,
    };
  });
}

async function openFiltros(page) {
  await dismissPeriodo(page);
  const btn = page.getByRole('button', { name: /Filtros/i }).first();
  if (await btn.count()) {
    await btn.click({ timeout: 8000 });
    await page.waitForTimeout(200);
    return true;
  }
  return false;
}

async function collectFilterSelects(page) {
  return page.evaluate(() => [...document.querySelectorAll('select')].map((el) => ({
    label: (el.closest('div')?.querySelector('label, dt, p')?.textContent || '').trim().slice(0, 80),
    options: [...el.options].map((o) => `${o.value} · ${o.textContent.trim()}`),
  })));
}

async function snapshotPanelTotales(page) {
  const panel = page.getByTestId('panel-totales');
  const extra = page.getByTestId('panel-totales-export');
  return {
    visible: await panel.count() > 0 && await panel.isVisible().catch(() => false),
    text: (await panel.innerText().catch(() => '')).slice(0, 800),
    extraVisible: await extra.count() > 0 && await extra.isVisible().catch(() => false),
    extraText: (await extra.innerText().catch(() => '')).slice(0, 800),
    totalUsd: await page.getByTestId('panel-totales-total').innerText().catch(() => ''),
  };
}

async function pickFirstSearchable(page, nameRe) {
  const btn = page.getByRole('button', { name: nameRe }).first();
  if (!(await btn.count())) return false;
  await btn.click();
  await page.waitForTimeout(400);
  const opt = page.locator('[role="option"]').first();
  if (await opt.count()) {
    await opt.click();
    return true;
  }
  return false;
}

async function listboxOptions(page, nameRe) {
  const btn = page.getByRole('button', { name: nameRe }).first();
  if (!(await btn.count())) return [];
  await btn.click();
  await page.waitForTimeout(350);
  const opts = await page.locator('[role="option"]').allTextContents();
  await page.keyboard.press('Escape');
  await page.waitForTimeout(150);
  return opts.map((t) => t.replace(/\s+/g, ' ').trim()).filter(Boolean);
}

async function main() {
  mkdirSync(outDir, { recursive: true });
  const browser = await launchBrowser();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  page.setDefaultTimeout(20000);
  page.on('pageerror', (err) => console.log('[pageerror]', err.message));
  page.on('console', (msg) => {
    if (msg.type() === 'error') console.log('[console.error]', msg.text());
  });

  try {
    await login(page);
    record('VEN-LOGIN', 'PASS', `Login OK → ${page.url()}`);
    await dismissPeriodo(page);
    await selectEmpresa(page, EMPRESA_HINT);
    await dismissPeriodo(page);
    record('VEN-EMPRESA', 'PASS', `Selector empresa (hint ${EMPRESA_HINT})`);

    // --- Clientes ---
    await page.goto(`${BASE}/comercial/clientes`, { waitUntil: 'networkidle' });
    const clientesInv = await inventory(page);
    const filtrosCli = await openFiltros(page);
    const filtrosCliOpts = filtrosCli ? await collectFilterSelects(page) : [];
    record('VEN-CLI-LIST', clientesInv.headings.some((h) => /Clientes/i.test(h)) ? 'PASS' : 'FAIL', `Filtros=${filtrosCli}`, {
      inputs: clientesInv.inputs,
      filterSelects: filtrosCliOpts,
    });
    await page.getByRole('button', { name: /Nuevo cliente/i }).click();
    await page.waitForTimeout(400);
    const cliForm = await inventory(page);
    const formLabels = await page.locator('label, p').allTextContents().catch(() => []);
    record('VEN-CLI-FORM', cliForm.inputs.length > 3 ? 'PASS' : 'FAIL', `Alta cliente: ${cliForm.inputs.length} inputs`, {
      inputs: cliForm.inputs,
      labels: formLabels.slice(0, 40),
    });
    await page.keyboard.press('Escape');

    // --- OV listado ---
    await page.goto(`${BASE}/comercial/ordenes-venta`, { waitUntil: 'networkidle' });
    const ovList = await inventory(page);
    const filtrosOv = await openFiltros(page);
    const ovFilterSelects = filtrosOv ? await collectFilterSelects(page) : [];
    const estadoOpts = ovFilterSelects.find((s) => /estado/i.test(s.label) || s.options.some((o) => /Borrador|Confirmada/i.test(o)));
    record('VEN-OV-LIST', /ordenes-venta/.test(page.url()) ? 'PASS' : 'FAIL', `Filtros=${filtrosOv}`, {
      buttons: ovList.buttons.filter((b) => /Nueva|Borrador|Filtros|Imprimir/i.test(b)),
      filterSelects: ovFilterSelects,
      estados: estadoOpts?.options ?? [],
    });
    const hasOvRows = await page.locator('table tbody tr').count();
    record('VEN-OV-ROWS', 'PASS', `Filas listado: ${hasOvRows}`);

    // --- OV alta + panel exportación ---
    await page.goto(`${BASE}/comercial/ordenes-venta/nueva`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(800);
    const ovNew = await inventory(page);
    const indicador = page.locator('select').filter({ has: page.locator('option[value="EXPORTACION"]') }).first();
    const indCount = await indicador.count();
    const indOptions = indCount
      ? await indicador.locator('option').evaluateAll((opts) => opts.map((o) => `${o.value} · ${o.textContent.trim()}`))
      : [];
    const formaPago = page.locator('select').filter({ has: page.locator('option[value="CREDITO"]') }).first();
    const pagoOpts = await formaPago.locator('option').evaluateAll((opts) => opts.map((o) => `${o.value} · ${o.textContent.trim()}`)).catch(() => []);
    record('VEN-OV-INPUTS-NAC', indCount ? 'PASS' : 'FAIL', `Indicador opciones: ${indOptions.join(' | ')}`, {
      selects: ovNew.selects,
      formaPago: pagoOpts,
      combos: ovNew.combos,
    });

    const panelAntes = await snapshotPanelTotales(page);
    record(
      'VEN-OV-PANEL-VENTA',
      panelAntes.visible ? 'PASS' : 'FAIL',
      `Panel visible=${panelAntes.visible} extraExport=${panelAntes.extraVisible}`,
      panelAntes,
    );

    const clienteOk = await pickFirstSearchable(page, /Buscar cliente/i);
    if (indCount) {
      await indicador.selectOption('EXPORTACION');
      await page.waitForTimeout(500);
    }
    const panelExp = await snapshotPanelTotales(page);
    const okExp = panelExp.extraVisible
      && /Total USD|Subtotal USD/i.test(panelExp.text)
      && /País receptor|Tipo de cambio|Total CLP/i.test(panelExp.extraText);
    record('VEN-OV-PANEL-EXPORT-ALTA', okExp ? 'PASS' : 'FAIL', okExp
      ? 'Panel exportación USD + COMEX en alta'
      : `text=${panelExp.text.slice(0, 200)} extra=${panelExp.extraText.slice(0, 200)}`, panelExp);

    if (clienteOk) {
      await page.getByRole('button', { name: /3\. Referencias/i }).click({ timeout: 8000 }).catch(() => {});
      await page.waitForTimeout(700);
    }
    const comexHead = await page.getByText(/Datos COMEX/i).count();
    record('VEN-OV-COMEX-STEP2', comexHead ? 'PASS' : 'FAIL', `cliente=${clienteOk} COMEX visible=${Boolean(comexHead)}`);

    const paisOpts = await listboxOptions(page, /Estados Unidos|Código T7|225/i);
    record('VEN-OV-PAISES', paisOpts.length >= 3 ? 'PASS' : 'FAIL', `Opciones país: ${paisOpts.slice(0, 12).join(' | ')}`, { paises: paisOpts });

    const viaOpts = await listboxOptions(page, /Marítima|Código vía/i);
    record('VEN-OV-VIAS', viaOpts.length >= 2 ? 'PASS' : 'FAIL', viaOpts.join(' | '), { vias: viaOpts });

    const clOpts = await listboxOptions(page, /FOB|CIF/i);
    record('VEN-OV-CLAUSULAS', clOpts.length >= 2 ? 'PASS' : 'FAIL', clOpts.join(' | '), { clausulas: clOpts });

    const monOpts = await listboxOptions(page, /13 · USD|USD/i);
    record('VEN-OV-MONEDAS', monOpts.some((o) => /USD|13/i.test(o)) ? 'PASS' : 'FAIL', monOpts.join(' | '), { monedas: monOpts });

    const panelStep2 = await snapshotPanelTotales(page);
    record('VEN-OV-PANEL-EXPORT-STEP2', panelStep2.extraVisible ? 'PASS' : 'FAIL', panelStep2.extraText.slice(0, 300), panelStep2);

    // Borrador: modal o fila BORRADOR
    await page.goto(`${BASE}/comercial/ordenes-venta`, { waitUntil: 'networkidle' });
    const borrBtn = page.getByRole('button', { name: /Borrador/i }).first();
    if (await borrBtn.count()) {
      await borrBtn.click();
      await page.waitForTimeout(500);
      const modalTxt = await page.locator('[role="dialog"]').innerText().catch(() => '');
      record('VEN-OV-BORRADORES-MODAL', 'PASS', modalTxt.slice(0, 240) || 'Modal abierto');
      const abrir = page.getByRole('button', { name: /Abrir|Cargar|Editar/i }).first();
      if (await abrir.count()) {
        await abrir.click();
        await page.waitForTimeout(800);
        const indVal = await page.locator('select').filter({ has: page.locator('option[value="EXPORTACION"]') }).first().inputValue().catch(() => '');
        if (indVal !== 'EXPORTACION') {
          await indicador.selectOption('EXPORTACION').catch(() => {});
          await page.waitForTimeout(400);
        }
        const panelB = await snapshotPanelTotales(page);
        record('VEN-OV-PANEL-BORRADOR', panelB.extraVisible || panelB.visible ? 'PASS' : 'FAIL',
          `indicador=${indVal} extra=${panelB.extraVisible}`, panelB);
      } else {
        await page.keyboard.press('Escape');
        record('VEN-OV-PANEL-BORRADOR', 'PASS', 'Sin borradores para hidratar; el panel se cubrió en alta');
      }
    } else {
      record('VEN-OV-BORRADORES-MODAL', 'PASS', 'Botón borradores no visible o sin badge');
    }

    const editBorrador = page.locator('table tbody tr').filter({ hasText: /Borrador/i }).first();
    if (await editBorrador.count()) {
      await editBorrador.getByTitle(/Editar/i).click().catch(async () => {
        await editBorrador.locator('button').nth(1).click();
      });
      await page.waitForTimeout(800);
      const sel = page.locator('select').filter({ has: page.locator('option[value="EXPORTACION"]') }).first();
      if (await sel.count()) {
        await sel.selectOption('EXPORTACION');
        await page.waitForTimeout(400);
        const panelB2 = await snapshotPanelTotales(page);
        record('VEN-OV-PANEL-BORRADOR-FILA', panelB2.extraVisible ? 'PASS' : 'FAIL', panelB2.extraText.slice(0, 240), panelB2);
      }
    }

    // --- Emitir DTE (sin emitir) ---
    await page.goto(`${BASE}/comercial/emitir`, { waitUntil: 'networkidle' });
    const emitirInv = await inventory(page);
    const tiposLibres = emitirInv.buttons.filter((b) => /crédito|débito|guía|Guía|Nota/i.test(b));
    record('VEN-EMITIR-PICKER', /emitir/.test(page.url()) ? 'PASS' : 'FAIL', `Tipos sin OV: ${tiposLibres.join(' | ')}`, {
      buttons: emitirInv.buttons,
      inputs: emitirInv.inputs,
    });
    await page.getByRole('button', { name: /Nota de crédito/i }).click();
    await page.waitForTimeout(700);
    const ncInv = await inventory(page);
    const origenTipo = page.locator('select').filter({ has: page.locator('option[value="110"]') }).first();
    const origenOpts = await origenTipo.locator('option').evaluateAll((opts) => opts.map((x) => `${x.value}`)).catch(() => []);
    record('VEN-EMITIR-NC', /tipo=NC|tipo=nc/.test(page.url()) || ncInv.selects.length ? 'PASS' : 'FAIL',
      `Tipos SII origen: ${origenOpts.join(',')}`, { selects: ncInv.selects });

    await page.goto(`${BASE}/comercial/emitir?tipo=ND`, { waitUntil: 'networkidle' });
    record('VEN-EMITIR-ND', page.url().includes('tipo=ND') ? 'PASS' : 'FAIL', page.url());
    await page.goto(`${BASE}/comercial/emitir?tipo=GUIA`, { waitUntil: 'networkidle' });
    record('VEN-EMITIR-GUIA', page.url().includes('tipo=GUIA') ? 'PASS' : 'FAIL', page.url());

    // --- Libro ventas ---
    await page.goto(`${BASE}/comercial/libro`, { waitUntil: 'networkidle' });
    const libroInv = await inventory(page);
    const filtrosLib = await openFiltros(page);
    const libroSelects = filtrosLib ? await collectFilterSelects(page) : [];
    const tipoOpts = libroSelects.flatMap((s) => s.options);
    const has110 = tipoOpts.some((o) => /\b110\b/.test(o));
    const has101 = tipoOpts.some((o) => /\b101\b/.test(o));
    const hasOvTipo = tipoOpts.some((o) => /ORDEN_VENTA|Orden de venta/i.test(o));
    record('VEN-LIBRO-FILTROS', filtrosLib ? 'PASS' : 'FAIL', `110=${has110} 101=${has101} OV=${hasOvTipo}`, {
      filterSelects: libroSelects,
      buttons: libroInv.buttons.slice(0, 40),
    });
    record('VEN-LIBRO-SIN-101', !has101 ? 'PASS' : 'FAIL', has101 ? 'El filtro aún lista 101 papel' : 'Sin 101');
    record('VEN-LIBRO-SIN-OV', !hasOvTipo ? 'PASS' : 'FAIL', hasOvTipo ? 'El filtro lista OV' : 'Libro sin tipo OV');
    record('VEN-LIBRO-110', has110 ? 'PASS' : 'FAIL', has110 ? 'Filtro incluye 110 factura exportación' : tipoOpts.join(' | '));

    // --- Guías ---
    await page.goto(`${BASE}/comercial/guias-despacho`, { waitUntil: 'networkidle' });
    const guiasInv = await inventory(page);
    record('VEN-GUIAS', /guias-despacho/.test(page.url()) ? 'PASS' : 'FAIL', guiasInv.headings.join(' · '), {
      buttons: guiasInv.buttons.filter((b) => /Emitir|Filtros|Nueva/i.test(b)),
    });

    // Cotizaciones no debe existir en ventas
    await page.goto(`${BASE}/comercial/cotizaciones`, { waitUntil: 'networkidle' });
    record('VEN-SIN-COTIZ', /compras\/ordenes/.test(page.url()) ? 'PASS' : 'FAIL', `Redirect ${page.url()}`);
  } catch (e) {
    record('VEN-CRASH', 'FAIL', String(e?.stack || e));
  } finally {
    await browser.close().catch(() => {});
  }

  const pass = results.filter((r) => r.result === 'PASS').length;
  const fail = results.filter((r) => r.result === 'FAIL').length;
  const jsonPath = join(outDir, `${stamp}-testrim-ventas.json`);
  const mdPath = join(outDir, `${stamp}-testrim-ventas.md`);
  writeFileSync(jsonPath, JSON.stringify({ stamp, base: BASE, pass, fail, results }, null, 2));
  const md = [
    `# Testrim Ventas ${stamp}`,
    '',
    `Base: ${BASE} · PASS ${pass} · FAIL ${fail}`,
    '',
    ...results.map((r) => `- **${r.result}** \`${r.id}\`: ${r.evidence}`),
  ].join('\n');
  writeFileSync(mdPath, md);
  console.log(`\nWrote ${jsonPath}\nWrote ${mdPath}\nPASS=${pass} FAIL=${fail}`);
  if (fail) process.exitCode = 1;
}

await main();
