import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { createRequire } from 'node:module';

const PAGES = createRequire(import.meta.url)('./trello-qa-pages.json');

const LIST_QA = '6a54f9be2f15b6cbeb89dfdd';
const LIST_REV = '6a95bee361fe59b99646bc7c';
const OUT = 'E:\\source\\repos\\Almahue\\.tmp-trello-qa';

const RESIDUAL = [
  '6a56dec8fb1a1ac94fdcd621',
  '6a56e78c1a9286c6838183b6',
  '6a56dffbbf9687330c65e8b7',
  '6a56e86990ba6e5ac5e5819b',
  '6a56e0d0e5456db74c0efc37',
  '6a6118908eb76f8053d6450b',
  '6a56ddbec8142db625d510fa',
  '6a61189578c54561ff6ff53b',
  '6a611896f9465c0efa91f4ef',
  '6a61189fc8a0596579582723',
  '6a56dc880008fd50372a09fa',
  '6a568f048f82b87faa923f45',
  '6a56dd486f710f9a72c8f914',
  '6a56de52f10c2c1776593f86',
  '6a5506270fe5f85bf4307ac5',
  '6a568d0c5fc4c3189b67bea1',
  '6a56dcee171c9d3f7378b861',
  '6a629b3830929fd6f6379b02',
  '6a629b2b237bd0ce1dbbb7e0',
  '6a6118a3d0f97628cf8c7edc',
  '6a56e09cdb55b3605f0fde7f',
  '6a6118a88c58cbc8a7c90389',
  '6a6118ac2952e7b746b8dce0',
  '6a56e05f97f435379103f6d9',
  '6a611895cffa241b01a66dc9',
  '6a56e807a68a12300a6d2cbd',
  '6a56dfc90311652545c4855b',
  '6a99cb76f8525ed78ab9ed27',
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

function introFor(page, idx) {
  if (page.slug === 'compras-oc') {
    return 'Validar todas las funcionales de este menu, como por ejemplo crear una nueva orden de compra.\n\nPagina de generacion de Ordenes de compra:';
  }
  return PHRASES[idx % PHRASES.length];
}

function previewUrl(cardId, att) {
  const previews = att.previews || [];
  const scaled = previews.filter((p) => p.scaled && (p.width || 0) >= 600);
  const pick = [...scaled].sort((a, b) => (b.width || 0) - (a.width || 0))[0]
    || [...previews].sort((a, b) => (b.width || 0) - (a.width || 0))[0];
  if (pick?.url) return pick.url;
  return att.url;
}

async function trelloJson(url, opts) {
  const res = await fetch(url, opts);
  const text = await res.text();
  if (!res.ok) throw new Error(`${res.status} ${url.split('?')[0]} ${text.slice(0, 400)}`);
  return text ? JSON.parse(text) : null;
}

async function main() {
  const env = loadEnv();
  const auth = qs(env);
  const created = [];

  const existing = [];
  for (const listId of [LIST_QA, LIST_REV]) {
    const rows = await trelloJson(`https://api.trello.com/1/lists/${listId}/cards?fields=name,id,shortUrl,desc,idAttachmentCover&${auth}`);
    existing.push(...rows);
  }
  const byName = new Map(existing.map((c) => [c.name, c]));

  for (let i = 0; i < PAGES.length; i++) {
    const page = PAGES[i];
    const idList = page.example ? LIST_QA : LIST_REV;
    const png = join(OUT, `${page.slug}.png`);
    const intro = introFor(page, i);

    if (byName.has(page.title)) {
      const prev = byName.get(page.title);
      if (!String(prev.desc || '').includes('![image')) {
        const atts = await trelloJson(`https://api.trello.com/1/cards/${prev.id}/attachments?${auth}`);
        const att = Array.isArray(atts) ? atts[0] : atts;
        if (att) {
          const md = `${intro}\n\n![image.webp](${previewUrl(prev.id, att)})`;
          const descUrl = new URL(`https://api.trello.com/1/cards/${prev.id}`);
          descUrl.searchParams.set('key', env.TRELLO_API_KEY);
          descUrl.searchParams.set('token', env.TRELLO_TOKEN);
          descUrl.searchParams.set('desc', md);
          await trelloJson(descUrl.toString(), { method: 'PUT' });
        }
      }
      console.log(`SKIP ${page.title} ${prev.shortUrl}`);
      continue;
    }

    const u = new URL('https://api.trello.com/1/cards');
    u.searchParams.set('key', env.TRELLO_API_KEY);
    u.searchParams.set('token', env.TRELLO_TOKEN);
    u.searchParams.set('idList', idList);
    u.searchParams.set('name', page.title);
    u.searchParams.set('desc', intro);
    u.searchParams.set('pos', 'bottom');
    const card = await trelloJson(u.toString(), { method: 'POST' });

    const buf = readFileSync(png);
    const form = new FormData();
    form.append('file', new Blob([buf], { type: 'image/png' }), 'image.png');
    form.append('setCover', 'false');
    const att = await trelloJson(
      `https://api.trello.com/1/cards/${card.id}/attachments?${auth}`,
      { method: 'POST', body: form },
    );

    const md = `${intro}\n\n![image.webp](${previewUrl(card.id, att)})`;
    const descUrl = new URL(`https://api.trello.com/1/cards/${card.id}`);
    descUrl.searchParams.set('key', env.TRELLO_API_KEY);
    descUrl.searchParams.set('token', env.TRELLO_TOKEN);
    descUrl.searchParams.set('desc', md);
    await trelloJson(descUrl.toString(), { method: 'PUT' });

    created.push({
      title: page.title,
      list: page.example ? 'En QA Almahue' : 'en revision',
      url: card.shortUrl,
      cover: card.idAttachmentCover,
    });
    console.log(`${page.example ? 'QA' : 'REV'} ${page.title} ${card.shortUrl}`);
  }

  for (const id of RESIDUAL) {
    const closeUrl = new URL(`https://api.trello.com/1/cards/${id}`);
    closeUrl.searchParams.set('key', env.TRELLO_API_KEY);
    closeUrl.searchParams.set('token', env.TRELLO_TOKEN);
    closeUrl.searchParams.set('closed', 'true');
    await trelloJson(closeUrl.toString(), { method: 'PUT' });
    console.log(`ARCHIVED ${id}`);
  }

  console.log(`CREATED=${created.length} ARCHIVED=${RESIDUAL.length}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
