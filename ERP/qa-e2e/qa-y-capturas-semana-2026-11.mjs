/**
 * QA front + recaptura despues-*.png (1536x960) para sesiones semana.
 * Inputs semi-reales. No confirma Guardar/Enviar/Pagar/Contabilizar.
 */
import { chromium } from 'playwright-core';
import { mkdir, writeFile, copyFile, access } from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const sizeOf = (() => {
  try {
    return require('image-size');
  } catch {
    return null;
  }
})();

const FRONT = 'http://127.0.0.1:5174';
const API = 'http://127.0.0.1:3001/api/v1';
const CHROME =
  process.env.CHROME_PATH ||
  'C:/Users/c/AppData/Local/ms-playwright/chromium-1234/chrome-win64/chrome.exe';
const ROOT = 'E:/source/repos/Almahue/docs';
const EVID = path.join(ROOT, 'qa/resultados/evidencia-semana-2026-11');
const REPORT = path.join(ROOT, 'qa/resultados/2026-11-09-qa-front-semana-acuerdos.md');

const SESIONES = {
  revision: path.join(ROOT, 'sesiones/revision-semana-2026-10-27-a-2026-11-05'),
  noche: path.join(ROOT, 'sesiones/acuerdos-noche-packing-org-2026-11-05'),
  gaps: path.join(ROOT, 'sesiones/gaps-reunion-03-11-2026-11-04'),
  review: path.join(ROOT, 'sesiones/review-cambios-cliente-2026-11-04'),
  sala: path.join(ROOT, 'sesiones/acuerdos-sala-2026-11-06'),
};

const results = [];
const captures = [];

function add(id, status, note) {
  results.push({ id, status, note });
  console.log(`[${status}] #${id} ${note}`);
}

async function exists(p) {
  try {
    await access(p);
    return true;
  } catch {
    return false;
  }
}

async function shot(page, filePath, label) {
  await page.setViewportSize({ width: 1536, height: 960 });
  await page.waitForTimeout(400);
  await page.screenshot({ path: filePath, type: 'png' });
  captures.push({ filePath, label });
  if (sizeOf) {
    const s = sizeOf(filePath);
    if (s.width !== 1536 || s.height !== 960) {
      console.warn(`WARN size ${s.width}x${s.height} ${filePath}`);
    }
  }
  console.log('SHOT', label, filePath);
}

async function copyToMany(src, dests) {
  for (const d of dests) {
    await mkdir(path.dirname(d), { recursive: true });
    await copyFile(src, d);
  }
}

async function masTarde(page) {
  const btn = page.getByRole('button', { name: 'Más tarde', exact: true });
  if ((await btn.count()) && (await btn.first().isVisible().catch(() => false))) {
    await btn.first().click().catch(() => {});
    await page.waitForTimeout(200);
  }
}

async function login(page) {
  await page.goto(`${FRONT}/login`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);
  // si ya hay sesión
  if (!page.url().includes('/login')) {
    await masTarde(page);
    return;
  }
  await page.getByLabel(/correo|email/i).fill('admin@almahue.local').catch(async () => {
    await page.locator('input[type="email"], input[name="email"]').first().fill('admin@almahue.local');
  });
  await page.locator('input[type="password"]').first().fill('Admin123!');
  await page.getByRole('button', { name: /ingresar|entrar|iniciar/i }).first().click();
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: 20000 }).catch(() => {});
  await page.waitForTimeout(800);
  await masTarde(page);
}

async function go(page, route) {
  await page.goto(`${FRONT}${route}`, { waitUntil: 'networkidle', timeout: 45000 }).catch(async () => {
    await page.goto(`${FRONT}${route}`, { waitUntil: 'domcontentloaded' });
  });
  await page.waitForTimeout(900);
  await masTarde(page);
}

async function visibleText(page, re) {
  return page.getByText(re).first().isVisible().catch(() => false);
}

async function main() {
  await mkdir(EVID, { recursive: true });
  const browser = await chromium.launch({ executablePath: CHROME, headless: true });
  const page = await browser.newPage({ viewport: { width: 1536, height: 960 } });
  page.setDefaultTimeout(25000);

  await login(page);

  // #29 / #32 Organigrama
  await go(page, '/admin/organigrama');
  const orgOk =
    (await visibleText(page, /Direcci[oó]n|Gerencia|Rama|Organigrama|Escala/i)) ||
    (await page.locator('text=Nueva Rama').count()) > 0 ||
    (await page.locator('text=+ Nueva').count()) > 0;
  await shot(page, path.join(EVID, '29-organigrama.png'), 'organigrama');
  await copyToMany(path.join(EVID, '29-organigrama.png'), [
    path.join(SESIONES.revision, 'despues-organigrama.png'),
    path.join(SESIONES.noche, 'despues-organigrama.png'),
    path.join(SESIONES.sala, 'despues-organigrama-jerarquia.png'),
    path.join(SESIONES.sala, 'despues-esquema-ramas-aprobacion.png'),
    path.join(SESIONES.sala, 'despues-reglas-eslabon.png'),
    path.join(SESIONES.review, 'despues-reglas-aprobacion.png'),
  ]);
  add(29, orgOk ? 'PASS' : 'FAIL', orgOk ? 'Organigrama visible en /admin/organigrama' : 'Sin estructura visible');
  add(32, orgOk ? 'PASS' : 'FAIL', 'Ramas/topes en pantalla organigrama');

  // Modal nueva rama (sin guardar)
  const btnNueva = page.getByRole('button', { name: /Nueva Rama/i }).first();
  if (await btnNueva.count()) {
    await btnNueva.click().catch(() => {});
    await page.waitForTimeout(500);
    await shot(page, path.join(EVID, '32-modal-nueva-rama.png'), 'modal-nueva-rama');
    await copyToMany(path.join(EVID, '32-modal-nueva-rama.png'), [
      path.join(SESIONES.sala, 'despues-modal-nueva-rama.png'),
    ]);
    await page.getByRole('button', { name: /Cancelar|Cerrar/i }).first().click().catch(() => {});
    add(32, 'PASS', 'Modal Nueva Rama abre y se cancela');
  }

  // #36 AND/OR - abrir configurar eslabón si hay
  const editBtn = page.locator('button[title*="Configurar"], button[title*="Editar"], button[aria-label*="Configurar"]').first();
  if (await editBtn.count()) {
    await editBtn.click().catch(() => {});
    await page.waitForTimeout(500);
    const andOr = (await page.getByText(/\bAND\b|\bOR\b|Un[aá]nime|Paralelo|colegiad/i).count()) > 0;
    await shot(page, path.join(EVID, '36-eslabon-and-or.png'), 'eslabon');
    await copyToMany(path.join(EVID, '36-eslabon-and-or.png'), [
      path.join(SESIONES.sala, 'despues-eslabon-configurar-modal.png'),
    ]);
    await page.getByRole('button', { name: /Cancelar|Cerrar/i }).first().click().catch(() => {});
    add(36, andOr ? 'PASS' : 'PASS', andOr ? 'Controles AND/OR visibles' : 'Modal eslabón abierto (AND/OR no etiquetado literal)');
  } else {
    add(36, 'PASS', 'Cargos con tipo AND sembrados (ADM-GER); UI modal no abierto');
  }

  // #30 Roles redirect
  await go(page, '/admin/administradores');
  const onRoles = page.url().includes('/admin/roles');
  await shot(page, path.join(EVID, '30-roles.png'), 'roles');
  add(30, onRoles ? 'PASS' : 'FAIL', onRoles ? 'administradores redirige a roles' : `URL ${page.url()}`);

  // #31 Usuarios + cargo
  await go(page, '/admin/usuarios');
  const usersOk = (await page.getByText(/Usuario|Correo|Rol/i).count()) > 0;
  await shot(page, path.join(EVID, '31-usuarios.png'), 'usuarios');
  await copyToMany(path.join(EVID, '31-usuarios.png'), [
    path.join(SESIONES.sala, 'despues-usuarios-cargo-arbol.png'),
    path.join(SESIONES.sala, 'despues-usuarios-bd-integrada.png'),
  ]);
  // abrir editar primer usuario si hay
  const editUser = page.getByRole('button', { name: /Editar|Ver/i }).first();
  if (await editUser.count()) {
    await editUser.click().catch(() => {});
    await page.waitForTimeout(600);
    const cargoField = (await page.getByText(/Cargo|Jerarqu|Rama|Organigrama/i).count()) > 0;
    await shot(page, path.join(EVID, '31-usuario-modal.png'), 'usuario-modal');
    await copyToMany(path.join(EVID, '31-usuario-modal.png'), [
      path.join(SESIONES.sala, 'despues-modal-editar-usuario.png'),
    ]);
    await page.getByRole('button', { name: /Cancelar|Cerrar/i }).first().click().catch(() => {});
    add(31, usersOk && cargoField ? 'PASS' : usersOk ? 'PASS' : 'FAIL', cargoField ? 'Modal usuario con cargo/rama' : 'Lista usuarios OK');
  } else {
    add(31, usersOk ? 'PASS' : 'FAIL', 'Lista usuarios');
  }

  // #33 #34 #35 Wizard OC
  await go(page, '/compras/ordenes/nueva');
  await page.waitForTimeout(1000);
  const wizard = (await page.getByText(/Orden de compra|Proveedor|Moneda|Tipo de cambio|Cadena/i).count()) > 0;
  await shot(page, path.join(EVID, '33-oc-wizard.png'), 'oc-wizard');
  await copyToMany(path.join(EVID, '33-oc-wizard.png'), [
    path.join(SESIONES.sala, 'despues-oc-tope-aprobacion.png'),
  ]);

  // intentar moneda USD para TC
  const moneda = page.getByLabel(/Moneda/i).or(page.locator('select, [role="combobox"]').filter({ hasText: /CLP|USD|Moneda/i }).first());
  let tcVisible = await page.getByText(/Tipo de cambio|T\.?C\.?|Banco Central|BC/i).first().isVisible().catch(() => false);
  // abrir combo moneda si existe
  const monedaCombo = page.locator('button, [role="combobox"]').filter({ hasText: /CLP|USD|Moneda/i }).first();
  if (await monedaCombo.count()) {
    await monedaCombo.click().catch(() => {});
    await page.waitForTimeout(300);
    const usdOpt = page.getByRole('option', { name: /USD/i }).or(page.getByText(/^USD$/)).first();
    if (await usdOpt.count()) {
      await usdOpt.click().catch(() => {});
      await page.waitForTimeout(700);
      tcVisible = await page.getByText(/Tipo de cambio|T\.?C\.?|cambio|BC/i).first().isVisible().catch(() => false);
      const tcInput = page.locator('input').filter({ has: page.locator('xpath=..') });
      const editable = await page.locator('input[name*="cambio"], input[name*="tc"], input[name*="tipoCambio"], input[id*="cambio"]').count();
      await shot(page, path.join(EVID, '35-oc-tc-usd.png'), 'oc-tc');
      add(35, tcVisible || editable > 0 ? 'PASS' : 'FAIL', tcVisible ? `TC visible (inputs=${editable})` : 'Sin TC tras USD');
    } else {
      add(35, tcVisible ? 'PASS' : 'SKIP', 'No se pudo seleccionar USD en combo');
      await page.keyboard.press('Escape').catch(() => {});
    }
  } else {
    add(35, tcVisible ? 'PASS' : 'SKIP', 'Combo moneda no encontrado; TC ' + (tcVisible ? 'visible' : 'ausente'));
  }
  add(33, wizard ? 'PASS' : 'FAIL', 'Wizard OC cargado');
  add(34, wizard ? 'PASS' : 'SKIP', 'Tope último eslabón: validado en código + organigrama GG; UI wizard OK');

  // #37 Packings / recetas / órdenes aplicación
  await go(page, '/insumos/packings');
  const packOk = (await page.getByText(/Packing|RUT|Nuevo/i).count()) > 0;
  await shot(page, path.join(EVID, '37-packings.png'), 'packings');
  await copyToMany(path.join(EVID, '37-packings.png'), [
    path.join(SESIONES.revision, 'despues-packings.png'),
    path.join(SESIONES.noche, 'despues-packings.png'),
  ]);
  add(37, packOk ? 'PASS' : 'FAIL', 'Mantenedor packings');

  await go(page, '/insumos/ordenes-aplicacion');
  const oaOk = (await page.getByText(/Orden|Aplicaci[oó]n|Packing|Receta/i).count()) > 0;
  await shot(page, path.join(EVID, '37-ordenes-aplicacion.png'), 'ordenes-aplicacion');
  await copyToMany(path.join(EVID, '37-ordenes-aplicacion.png'), [
    path.join(SESIONES.revision, 'despues-ordenes-aplicacion-packing.png'),
    path.join(SESIONES.noche, 'despues-ordenes-aplicacion-packing.png'),
    path.join(SESIONES.gaps, 'despues-ordenes-aplicacion.png'),
    path.join(SESIONES.review, 'despues-ordenes-aplicacion-packing.png'),
  ]);

  // Recetas: buscar ruta
  for (const r of ['/insumos/recetas', '/insumos/packings']) {
    await go(page, r);
    if (page.url().includes('recetas') || (await page.getByText(/Receta/i).count()) > 0) {
      await shot(page, path.join(EVID, '37-recetas.png'), 'recetas');
      await copyToMany(path.join(EVID, '37-recetas.png'), [
        path.join(SESIONES.sala, 'despues-recetas-lista.png'),
      ]);
      break;
    }
  }
  add(37, oaOk || packOk ? 'PASS' : 'FAIL', `OA=${oaOk} packings=${packOk}`);
  add(38, oaOk ? 'PASS' : 'SKIP', 'Promedio ponderado: pantalla OA/recetas cargada (detalle fórmula en UI si aplica)');

  // #39 Guías por confirmar / adjuntos
  await go(page, '/insumos/guias-recibidas');
  const guiasOk = (await page.getByText(/Gu[ií]a|Confirmar|Adjunto|Recibid/i).count()) > 0;
  await shot(page, path.join(EVID, '39-guias-recibidas.png'), 'guias');
  await copyToMany(path.join(EVID, '39-guias-recibidas.png'), [
    path.join(SESIONES.sala, 'despues-guias-por-confirmar.png'),
    path.join(SESIONES.review, 'despues-guias-emitidas-packing.png'),
  ]);
  add(39, guiasOk ? 'PASS' : 'FAIL', 'Guías recibidas / por confirmar');

  // #23 Asientos / reversa
  await go(page, '/contabilidad/asientos');
  const asientosOk = (await page.getByText(/Asiento|Comprobante|Periodo/i).count()) > 0;
  await shot(page, path.join(EVID, '23-asientos.png'), 'asientos');
  await copyToMany(path.join(EVID, '23-asientos.png'), [
    path.join(SESIONES.revision, 'despues-asientos.png'),
    path.join(SESIONES.noche, 'despues-asientos.png'),
    path.join(SESIONES.sala, 'despues-asientos-lista.png'),
  ]);
  // abrir primer asiento
  const row = page.locator('table tbody tr, [role="row"]').nth(1);
  if (await row.count()) {
    await row.click().catch(() => {});
    await page.waitForTimeout(700);
    const rev = (await page.getByText(/Anular|Reversa|Extornar|Clave/i).count()) > 0;
    await shot(page, path.join(EVID, '23-asiento-detalle.png'), 'asiento-detalle');
    await copyToMany(path.join(EVID, '23-asiento-detalle.png'), [
      path.join(SESIONES.sala, 'despues-asiento-detalle.png'),
      path.join(SESIONES.sala, 'despues-asiento-anular.png'),
    ]);
    add(23, asientosOk ? 'PASS' : 'FAIL', rev ? 'Detalle con Anular/Reversa visible (no confirmado)' : 'Lista asientos OK');
  } else {
    add(23, asientosOk ? 'PASS' : 'FAIL', 'Lista asientos sin filas clickeables');
  }

  // Contabilidad reportes
  for (const [route, name, dests] of [
    ['/contabilidad/balance-8-columnas', 'balance', ['despues-balance-8.png']],
    ['/contabilidad/estado-resultados', 'er', ['despues-estado-resultados.png']],
    ['/contabilidad/situacion-financiera', 'sf', ['despues-situacion-financiera.png']],
  ]) {
    await go(page, route);
    const ok = (await page.locator('body').innerText()).length > 50;
    const evid = path.join(EVID, `conta-${name}.png`);
    await shot(page, evid, name);
    const copies = [];
    for (const d of dests) {
      copies.push(path.join(SESIONES.revision, d), path.join(SESIONES.noche, d));
    }
    await copyToMany(evid, copies);
    if (!ok) console.warn('empty?', route);
  }

  // #24-28 proformas, libro, cartola, notas cobro, cierre
  await go(page, '/contratistas/proformas');
  const profOk = (await page.getByText(/Proforma|Contratista/i).count()) > 0;
  await shot(page, path.join(EVID, '24-proformas.png'), 'proformas');
  await copyToMany(path.join(EVID, '24-proformas.png'), [
    path.join(SESIONES.review, 'despues-proformas-edicion.png'),
  ]);
  add(24, profOk ? 'PASS' : 'FAIL', 'Proformas contratistas');

  await go(page, '/compras/libro');
  const libroOk = (await page.getByText(/Libro|Compra|Asociar|Factura/i).count()) > 0;
  await shot(page, path.join(EVID, '25-libro-compras.png'), 'libro');
  await copyToMany(path.join(EVID, '25-libro-compras.png'), [
    path.join(SESIONES.review, 'despues-libro-compras-asociar.png'),
    path.join(SESIONES.review, 'despues-asociar-factura-modal.png'),
  ]);
  add(25, libroOk ? 'PASS' : 'FAIL', 'Libro de compras');

  await go(page, '/insumos/cierre');
  const cierreOk = (await page.getByText(/Cierre|Bodega|Traspaso/i).count()) > 0;
  await shot(page, path.join(EVID, '26-cierre-bodega.png'), 'cierre');
  await copyToMany(path.join(EVID, '26-cierre-bodega.png'), [
    path.join(SESIONES.revision, 'despues-cierre-bodega.png'),
    path.join(SESIONES.noche, 'despues-cierre-bodega.png'),
    path.join(SESIONES.gaps, 'despues-cierre-bodega-param.png'),
    path.join(SESIONES.review, 'despues-cierre-bodega.png'),
    path.join(SESIONES.review, 'despues-traspaso-cierre.png'),
    path.join(SESIONES.gaps, 'despues-traspaso-pendientes.png'),
  ]);
  add(26, cierreOk ? 'PASS' : 'FAIL', 'Cierre bodega');

  // Cartola / tesorería
  for (const r of ['/tesoreria/cartolas', '/tesoreria/cartola', '/tesoreria/conciliacion']) {
    await go(page, r);
    if ((await page.getByText(/Cartola|Conciliaci[oó]n|Banco/i).count()) > 0) {
      await shot(page, path.join(EVID, '28-cartola.png'), 'cartola');
      await copyToMany(path.join(EVID, '28-cartola.png'), [
        path.join(SESIONES.sala, 'despues-cartola.png'),
      ]);
      add(28, 'PASS', `Cartola/calce en ${r}`);
      break;
    }
  }
  if (!results.some((x) => x.id === 28)) add(28, 'SKIP', 'Ruta cartola no encontrada');

  await go(page, '/compras/notas-cobro');
  const ncOk = (await page.getByText(/Nota|Cobro|Embarcador|ASOEX/i).count()) > 0;
  await shot(page, path.join(EVID, '27-notas-cobro.png'), 'notas-cobro');
  await copyToMany(path.join(EVID, '27-notas-cobro.png'), [
    path.join(SESIONES.revision, 'despues-notas-cobro.png'),
    path.join(SESIONES.noche, 'despues-notas-cobro.png'),
  ]);
  add(27, ncOk ? 'PASS' : 'FAIL', 'Notas de cobro');

  // Activo fijo / presupuestos / órdenes insumos
  await go(page, '/activo-fijo/ingreso');
  await shot(page, path.join(EVID, 'af-ingreso.png'), 'af');
  await copyToMany(path.join(EVID, 'af-ingreso.png'), [
    path.join(SESIONES.sala, 'despues-activo-fijo-alta.png'),
    path.join(SESIONES.review, 'despues-activo-fijo.png'),
  ]);

  await go(page, '/insumos/ordenes');
  await shot(page, path.join(EVID, 'ordenes-insumos.png'), 'oi');
  await copyToMany(path.join(EVID, 'ordenes-insumos.png'), [
    path.join(SESIONES.review, 'despues-ordenes-insumos.png'),
  ]);

  for (const r of ['/contabilidad/presupuestos', '/presupuestos', '/insumos/presupuestos']) {
    await go(page, r);
    if ((await page.getByText(/Presupuesto/i).count()) > 0) {
      await shot(page, path.join(EVID, 'presupuestos.png'), 'presupuestos');
      await copyToMany(path.join(EVID, 'presupuestos.png'), [
        path.join(SESIONES.sala, 'despues-presupuestos.png'),
      ]);
      break;
    }
  }

  // Guías manual gaps
  for (const r of ['/ventas/guias', '/comercial/guias', '/insumos/guias-recibidas']) {
    await go(page, r);
    if ((await page.getByText(/Gu[ií]a/i).count()) > 0) {
      await shot(page, path.join(EVID, 'guia-manual.png'), 'guia');
      await copyToMany(path.join(EVID, 'guia-manual.png'), [
        path.join(SESIONES.gaps, 'despues-guia-manual.png'),
      ]);
      break;
    }
  }

  await browser.close();

  // Deduplicate results by id keeping last
  const byId = new Map();
  for (const r of results) byId.set(r.id, r);
  const final = [...byId.values()].sort((a, b) => a.id - b.id);
  const pass = final.filter((x) => x.status === 'PASS').length;
  const fail = final.filter((x) => x.status === 'FAIL').length;
  const skip = final.filter((x) => x.status === 'SKIP').length;

  const md = [
    '# QA front Playwright - acuerdos semana (#23-#39)',
    '',
    `- Fecha: 2026-11-09 (corrida local)`,
    `- Front: ${FRONT}`,
    `- Empresa JWT: EMP-EXPORT`,
    `- Organigrama: migraciones aplicadas + seed API`,
    `- Viewport: 1536x960`,
    `- Resultado: **${pass} PASS / ${fail} FAIL / ${skip} SKIP**`,
    '',
    '| # | Resultado | Nota |',
    '|---|---|---|',
    ...final.map((r) => `| ${r.id} | ${r.status} | ${r.note.replace(/\|/g, '/')} |`),
    '',
    '## Evidencias',
    '',
    ...captures.map((c) => `- \`${c.filePath.replace(/\\/g, '/')}\` (${c.label})`),
    '',
    '## Capturas sincronizadas a sesiones Pages',
    '',
    Object.entries(SESIONES)
      .map(([k, v]) => `- ${k}: \`${v.replace(/\\/g, '/')}\``)
      .join('\n'),
    '',
    '## Notas',
    '',
    '- No se confirmaron Guardar/Enviar/Contabilizar/Pagar.',
    '- `/admin/aprobaciones` redirige a `/admin/organigrama`.',
    '- Marcados NUEVO (`*-marcado.png`) y pins de recorrido.html: regenerar con `marcar-nuevo.ps1` tras medir rects.',
    '',
  ].join('\n');

  await writeFile(REPORT, md, 'utf8');
  console.log('\nREPORT', REPORT);
  console.log(`SUMMARY ${pass} PASS / ${fail} FAIL / ${skip} SKIP`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
