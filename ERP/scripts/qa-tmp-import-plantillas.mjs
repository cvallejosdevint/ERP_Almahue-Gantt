/**
 * Importa plantillas de Descargas a prod (EMP-1 / EMP-2).
 * Uso: node scripts/qa-tmp-import-plantillas.mjs
 */
const API = process.env.ERP_API || 'http://45.7.229.46/almahue-erp/api/v1';
const EMAIL = process.env.ERP_EMAIL || 'admin@almahue.local';
const PASSWORD = process.env.ERP_PASSWORD || 'Admin123!';
const DOWNLOADS = process.env.DOWNLOADS || 'C:/Users/c/Downloads';
const EMPRESAS = (process.env.ERP_EMPRESAS || 'EMP-1,EMP-2').split(',');

const FILES = {
  centros: `${DOWNLOADS}/plantilla-centros-de-costo.xlsx`,
  elementos: `${DOWNLOADS}/plantilla-elementos-de-costo.xlsx`,
  codigos: `${DOWNLOADS}/plantilla-codigos-financieros.xlsx`,
  cuentas: `${DOWNLOADS}/plantilla-cuentas-contables.xlsx`,
};

function stripPreview(items) {
  return (items || []).map((it) => {
    const { accion, cambios, ...rest } = it;
    return rest;
  });
}

async function login() {
  const res = await fetch(`${API}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: EMAIL, password: PASSWORD }),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(`login ${res.status} ${JSON.stringify(json)}`);
  const token = json.accessToken || json.access_token || json.token;
  if (!token) throw new Error('login sin token');
  return token;
}

async function api(token, empresaId, path, { method = 'GET', json, form } = {}) {
  const headers = {
    Authorization: `Bearer ${token}`,
    'X-Empresa-Id': empresaId,
  };
  let body;
  if (form) {
    body = form;
  } else if (json !== undefined) {
    headers['Content-Type'] = 'application/json';
    body = JSON.stringify(json);
  }
  const res = await fetch(`${API}${path}`, { method, headers, body });
  const text = await res.text();
  let data;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = { raw: text.slice(0, 400) };
  }
  if (!res.ok) {
    throw new Error(`${method} ${path} ${res.status} ${JSON.stringify(data).slice(0, 800)}`);
  }
  return data;
}

async function fileBlob(path) {
  const { readFile } = await import('node:fs/promises');
  const { basename } = await import('node:path');
  const buf = await readFile(path);
  return { blob: new Blob([buf]), name: basename(path) };
}

async function previewAndImport(token, empresaId, previewPath, importPath, filePath, extraFields = []) {
  const { blob, name } = await fileBlob(filePath);
  const form = new FormData();
  form.append('file', blob, name);
  const preview = await api(token, empresaId, previewPath, { method: 'POST', form });
  const items = stripPreview(preview.items).map((it) => {
    const out = {};
    for (const k of ['codigo', 'nombre', 'activa', 'contactoEncargado', 'departamento', ...extraFields]) {
      if (it[k] !== undefined) out[k] = it[k];
    }
    return out;
  });
  const imported = await api(token, empresaId, importPath, {
    method: 'POST',
    json: { items, archivoNombre: name },
  });
  return {
    preview: {
      total: preview.total,
      nuevos: preview.nuevos,
      duplicados: preview.duplicados,
      sinCambios: preview.sinCambios,
      existingCount: preview.existingCount,
    },
    imported,
  };
}

async function importCuentas(token, empresaId, filePath) {
  const { blob, name } = await fileBlob(filePath);
  const form = new FormData();
  form.append('file', blob, name);
  form.append('replace', 'false');
  return api(token, empresaId, '/cuentas/import-excel', { method: 'POST', form });
}

async function main() {
  const token = await login();
  const out = {};
  for (const empresaId of EMPRESAS) {
    console.log(`== ${empresaId} ==`);
    const centros = await previewAndImport(
      token,
      empresaId,
      '/centros-costo/import-excel/preview',
      '/centros-costo/import-excel',
      FILES.centros,
    );
    console.log('centros', JSON.stringify(centros));
    const elementos = await previewAndImport(
      token,
      empresaId,
      '/elementos-costo/import-excel/preview',
      '/elementos-costo/import-excel',
      FILES.elementos,
    );
    console.log('elementos', JSON.stringify(elementos));
    const codigos = await previewAndImport(
      token,
      empresaId,
      '/codigos-financieros/import-excel/preview',
      '/codigos-financieros/import-excel',
      FILES.codigos,
    );
    console.log('codigos', JSON.stringify(codigos));
    const cuentas = await importCuentas(token, empresaId, FILES.cuentas);
    console.log('cuentas', JSON.stringify(cuentas));
    out[empresaId] = { centros, elementos, codigos, cuentas };
  }

  try {
    const sync = await api(token, 'EMP-1', '/sync-indicadores-bc', {
      method: 'POST',
      json: { desde: '2026-10-15', hasta: '2026-10-21' },
    });
    console.log('sync-bc', JSON.stringify({ count: sync.count, fuente: sync.items?.[0]?.fuente }));
    out.sync = { count: sync.count, fuente: sync.items?.[0]?.fuente };
  } catch (e) {
    console.log('sync-bc ERROR', String(e.message || e).slice(0, 500));
    out.syncError = String(e.message || e).slice(0, 500);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
