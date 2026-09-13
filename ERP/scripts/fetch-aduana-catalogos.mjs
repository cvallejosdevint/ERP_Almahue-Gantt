import { writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const BASE = 'http://comext.aduana.cl:7001';
const jar = join(tmpdir(), 'aduana-codigos.ck');
const { execSync } = await import('node:child_process');
const { readFileSync } = await import('node:fs');

const CATALOGOS = [
  { opcion: '03', key: 'CLAUSULAS_ADUANA', title: 'Cláusula compra-venta (opción 03 / CodClauVenta)' },
  { opcion: '07', key: 'FORMAS_PAGO_ADUANA', title: 'Formas de pago Aduana (opción 07)' },
  { opcion: '09', key: 'MONEDAS_ADUANA', title: 'Monedas (opción 09 / TpoMoneda)' },
  { opcion: '10', key: 'PAISES_ADUANA', title: 'Países (opción 10 / CodPaisRecep-Destin)' },
  { opcion: '13', key: 'BULTOS_ADUANA', title: 'Tipos de bulto (opción 13 / CodTpoBultos)' },
  { opcion: '17', key: 'UNIDADES_ADUANA', title: 'Unidad de medida (opción 17)' },
  { opcion: '18', key: 'VIAS_ADUANA', title: 'Vías de transporte (opción 18 / CodViaTransp)' },
];

async function main() {
  const { execSync } = await import('node:child_process');
  const home = join(tmpdir(), 'aduana-home.html');
  execSync(`curl -sS -c "${jar}" -b "${jar}" -m 30 -L "${BASE}/codigos/" -o "${home}"`, { stdio: 'inherit' });
  const htmlHome = (await import('node:fs')).readFileSync(home, 'utf8');
  const jsid = /buscar\.do;jsessionid=([^"]+)/.exec(htmlHome)?.[1];
  if (!jsid) throw new Error('sin jsessionid');
  const re = /<tr class="tablaItem">\s*<td><span>([^<]+)<\/span><\/td>\s*<td><span>([^<]*)<\/span><\/td>/g;
  const blocks = [];
  const counts = {};
  for (const cat of CATALOGOS) {
    const out = join(tmpdir(), `aduana-${cat.opcion}.html`);
    execSync(
      `curl -sS -c "${jar}" -b "${jar}" -m 40 -L "${BASE}/codigos/buscar.do;jsessionid=${jsid}" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "wlw-select_key:{actionForm.opcion}OldValue=true" --data-urlencode "wlw-select_key:{actionForm.opcion}=${cat.opcion}" -o "${out}"`,
      { stdio: 'inherit' },
    );
    const html = (await import('node:fs')).readFileSync(out, 'utf8');
    const rows = [];
    let m;
    const local = new RegExp(re.source, 'g');
    while ((m = local.exec(html))) {
      const codigo = m[1].trim();
      const nombre = m[2]
        .trim()
        .replace(/&amp;/g, '&')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'")
        .replace(/\s+/g, ' ');
      if (codigo && nombre) rows.push({ codigo, nombre });
    }
    rows.sort((a, b) => Number(a.codigo) - Number(b.codigo) || a.codigo.localeCompare(b.codigo));
    counts[cat.key] = rows.length;
    const lines = rows.map((r) => `  { codigo: ${JSON.stringify(r.codigo)}, nombre: ${JSON.stringify(r.nombre)} },`);
    blocks.push(`/** ${cat.title}. Fuente: ${BASE}/codigos/ */\nexport const ${cat.key}: readonly { codigo: string; nombre: string }[] = [\n${lines.join('\n')}\n];`);
    const sample = rows.filter((r) =>
      /FOB|CIF|DOLAR|YUAN|EURO|ESTADOS UNIDOS|USA|CAJA|MARITIMA|CONSIGNA|FLUVIAL/i.test(`${r.nombre} ${r.codigo}`),
    ).slice(0, 20);
    console.log(cat.key, rows.length, JSON.stringify(sample));
  }
  const ts = `/** Catálogos Aduana (comext) usados en DTE exportación SII. */\n\n${blocks.join('\n\n')}\n`;
  writeFileSync(
    'E:/source/repos/Almahue/ERP/erp_front/src/features/comercial/comex-aduana-catalogos.ts',
    ts,
  );
  console.log('counts', counts);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
