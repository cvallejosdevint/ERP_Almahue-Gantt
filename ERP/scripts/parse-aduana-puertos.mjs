import { readFileSync, writeFileSync } from 'node:fs';

const html = readFileSync(`${process.env.TEMP}/aduana-puertos.html`, 'utf8');
const re = /<tr class="tablaItem">\s*<td><span>([^<]+)<\/span><\/td>\s*<td><span>([^<]*)<\/span><\/td>/g;
const rows = [];
let m;
while ((m = re.exec(html))) {
  const codigo = m[1].trim();
  const nombre = m[2].trim().replace(/\s+/g, ' ');
  if (codigo && nombre) rows.push({ codigo, nombre });
}
rows.sort((a, b) => Number(a.codigo) - Number(b.codigo) || a.codigo.localeCompare(b.codigo));

const lines = rows.map((r) => `  { codigo: ${JSON.stringify(r.codigo)}, nombre: ${JSON.stringify(r.nombre)} },`);
const ts = `/** Catálogo Puertos Aduana (opción 11). Fuente: http://comext.aduana.cl:7001/codigos/ — Anexo 51-11 / SII CodPtoEmbarque y CodPtoDesemb. */

export const PUERTOS_ADUANA: readonly { codigo: string; nombre: string }[] = [
${lines.join('\n')}
];
`;
writeFileSync(
  'E:/source/repos/Almahue/ERP/erp_front/src/features/comercial/comex-aduana-puertos.ts',
  ts,
);
console.log('wrote', rows.length);
