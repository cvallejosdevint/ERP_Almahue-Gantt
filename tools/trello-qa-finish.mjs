import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { chromium } from 'playwright-core';

const LIST_QA = '6a54f9be2f15b6cbeb89dfdd';
const LIST_REV = '6a95bee361fe59b99646bc7c';
const OUT = 'E:\\source\\repos\\Almahue\\.tmp-trello-qa';
const BASE = process.env.E2E_BASE || 'http://127.0.0.1:5174';
const ADMIN_EMAIL = process.env.E2E_EMAIL || 'admin@almahue.local';
const ADMIN_PASS = process.env.E2E_PASS || 'Admin123!';
const EMPRESA_HINT = process.env.E2E_EMPRESA || 'EXPORT';

const RESTYLE = [
  { slug: 'admin-empresas', path: '/admin/empresas', title: 'Administración - Empresas' },
  { slug: 'admin-usuarios', path: '/admin/usuarios', title: 'Administración - Usuarios' },
  { slug: 'admin-roles', path: '/admin/roles', title: 'Administración - Roles y permisos' },
];

const PHRASES = [
  'validar todas las opciones de la pagina:',
  'Validar las funciones implementadas de pagina:',
  'Probar las funcionalidades de la pagina:',
  'Favor validar todas las funcionalidades de la pagina:',
  'favor probar funcionalidades de la pagina:',
];

function loadEnv() {
  const raw = readFileSync('E:\\source\\repos\\Almahue\\tools\\.env', 'utf8');
  const env = {};
  for (const line of raw.split(/\r?\n/)) {
    const m = line.match(/^([A-Z0-9_]+)=(.*)$/);
    if (m) env[m[1]] = m[2];
  }
  return env;
}

function qs(env) {
  return `key=${encodeURIComponent(env.TRELLO_API_KEY)}&token=${encodeURIComponent(env.TRELLO_TOKEN)}`;
}

async function trelloJson(url, opts) {
  const res = await fetch(url, opts);
  const text = await res.text();
  if (!res.ok) throw new Error(`${res.status} ${url.split('?')[0]} ${text.slice(0, 400)}`);
  return text ? JSON.parse(text) : null;
}

function previewUrl(att) {
  const previews = att.previews || [];
  const scaled = previews.filter((p) => p.scaled && (p.width || 0) >= 600);
  const pick = [...scaled].sort((a, b) => (b.width || 0) - (a.width || 0))[0]
    || [...previews].sort((a, b) => (b.width || 0) - (a.width || 0))[0];
  if (pick?.url) return pick.url;
  return att.url;
}

async function launchBrowser() {
  const attempts = [{ channel: 'chrome' }, { channel: 'msedge' }, {}];
  let last;
  for (const opts of attempts) {
    try {
      return await chromium.launch({ headless: true, ...opts, args: ['--window-size=1920,1080'] });
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

async function captureRestyle() {
  const browser = await launchBrowser();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.setDefaultTimeout(20000);
  await page.goto(`${BASE}/login`, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.locator('input[type="email"]').first().waitFor({ state: 'visible', timeout: 45000 });
  await page.locator('input[type="email"]').first().fill(ADMIN_EMAIL);
  await page.locator('input[type="password"]').fill(ADMIN_PASS);
  await page.getByRole('button', { name: /Entrar con clave/i }).click();
  await page.waitForURL((u) => !u.pathname.includes('/login'), { timeout: 25000 });
  await dismissPeriodo(page);
  const trigger = page.locator('button').filter({
    hasText: /SPA|Almahue|empresa|EXPORT|SERVICES|Seleccionar/i,
  }).first();
  await trigger.click({ timeout: 8000 }).catch(() => {});
  const search = page.getByPlaceholder(/Buscar por RUT/i);
  if (await search.count()) {
    await search.fill(EMPRESA_HINT);
    await page.waitForTimeout(400);
    const opt = page.locator('ul button').filter({ hasText: new RegExp(EMPRESA_HINT, 'i') }).first();
    if (await opt.count()) await opt.click();
    else await page.keyboard.press('Escape');
  }
  await dismissPeriodo(page);
  for (const p of RESTYLE) {
    await page.goto(`${BASE}${p.path}`, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await dismissPeriodo(page);
    await page.waitForTimeout(700);
    await page.screenshot({ path: join(OUT, `${p.slug}.png`), type: 'png' });
    console.log('SHOT', p.slug);
  }
  await browser.close();
}

async function main() {
  const env = loadEnv();
  const auth = qs(env);

  await captureRestyle();

  const qaCards = await trelloJson(`https://api.trello.com/1/lists/${LIST_QA}/cards?fields=name,id,desc,idAttachmentCover&${auth}`);
  const revCards = await trelloJson(`https://api.trello.com/1/lists/${LIST_REV}/cards?fields=name,id,shortUrl&${auth}`);

  for (let i = 0; i < RESTYLE.length; i++) {
    const page = RESTYLE[i];
    const card = qaCards.find((c) => c.name === page.title);
    if (!card) {
      console.log('MISSING', page.title);
      continue;
    }
    const oldAtts = await trelloJson(`https://api.trello.com/1/cards/${card.id}/attachments?${auth}`);
    const buf = readFileSync(join(OUT, `${page.slug}.png`));
    const form = new FormData();
    form.append('file', new Blob([buf], { type: 'image/png' }), 'image.png');
    form.append('setCover', 'false');
    const att = await trelloJson(
      `https://api.trello.com/1/cards/${card.id}/attachments?${auth}`,
      { method: 'POST', body: form },
    );
    const intro = PHRASES[i % PHRASES.length];
    const md = `${intro}\n\n![image.webp](${previewUrl(att)})`;
    const descUrl = new URL(`https://api.trello.com/1/cards/${card.id}`);
    descUrl.searchParams.set('key', env.TRELLO_API_KEY);
    descUrl.searchParams.set('token', env.TRELLO_TOKEN);
    descUrl.searchParams.set('desc', md);
    await trelloJson(descUrl.toString(), { method: 'PUT' });
    for (const old of oldAtts || []) {
      if (old.id === att.id) continue;
      await trelloJson(
        `https://api.trello.com/1/cards/${card.id}/attachments/${old.id}?${auth}`,
        { method: 'DELETE' },
      );
    }
    console.log('RESTYLE', page.title);
  }

  for (const card of revCards) {
    const u = new URL(`https://api.trello.com/1/cards/${card.id}`);
    u.searchParams.set('key', env.TRELLO_API_KEY);
    u.searchParams.set('token', env.TRELLO_TOKEN);
    u.searchParams.set('idList', LIST_QA);
    u.searchParams.set('pos', 'bottom');
    await trelloJson(u.toString(), { method: 'PUT' });
    console.log('MOVED', card.name, card.shortUrl);
  }

  const finalQa = await trelloJson(`https://api.trello.com/1/lists/${LIST_QA}/cards?fields=name,idAttachmentCover,shortUrl&${auth}`);
  const stillRev = await trelloJson(`https://api.trello.com/1/lists/${LIST_REV}/cards?fields=name&${auth}`);
  const withCover = finalQa.filter((c) => c.idAttachmentCover);
  console.log(`QA=${finalQa.length} REV=${stillRev.length} COVERS=${withCover.length}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
