/**
 * Siembra ramas/cargos jerárquicos vía API real (EMP-EXPORT holding QA).
 * Completa lo que falte (idempotente por codigo).
 */
const BASE = 'http://localhost:3001/api/v1';

async function login() {
  const r = await fetch(`${BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'admin@almahue.local', password: 'Admin123!' }),
  });
  if (!r.ok) throw new Error(`login ${r.status}`);
  const j = await r.json();
  return j.accessToken || j.token;
}

function headers(token, empresaId) {
  return {
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json',
    'x-empresa-id': empresaId,
  };
}

const RAMAS = [
  {
    codigo: 'DIRECCION',
    nombre: 'Dirección General',
    subtitulo: 'Gerencia General y Directorio',
    nivel: 1,
    modulos: ['COMPRAS', 'INSUMOS', 'CONTRATISTAS'],
    colorBadge: 'bg-rose-100 text-rose-800 border-rose-300',
    colorBorder: 'border-rose-400',
    colorBg: 'bg-rose-50/70',
    colorText: 'text-rose-900',
    orden: 1,
  },
  {
    codigo: 'AGRICOLA',
    nombre: 'Rama Agrícola / Faena',
    subtitulo: 'Fundos Norte/Sur, Riego y Maquinaria',
    nivel: 2,
    modulos: ['COMPRAS', 'INSUMOS'],
    colorBadge: 'bg-emerald-100 text-emerald-800 border-emerald-300',
    colorBorder: 'border-emerald-400',
    colorBg: 'bg-emerald-50/70',
    colorText: 'text-emerald-900',
    orden: 2,
  },
  {
    codigo: 'PACKING',
    nombre: 'Rama Packing y Frío',
    subtitulo: 'Planta, Calidad y Frigorífico',
    nivel: 2,
    modulos: ['COMPRAS', 'INSUMOS'],
    colorBadge: 'bg-blue-100 text-blue-800 border-blue-300',
    colorBorder: 'border-blue-400',
    colorBg: 'bg-blue-50/70',
    colorText: 'text-blue-900',
    orden: 3,
  },
  {
    codigo: 'ADMINISTRACION',
    nombre: 'Rama Administración y Finanzas',
    subtitulo: 'Finanzas, Adquisiciones y RRHH',
    nivel: 2,
    modulos: ['COMPRAS', 'INSUMOS', 'CONTRATISTAS'],
    colorBadge: 'bg-purple-100 text-purple-800 border-purple-300',
    colorBorder: 'border-purple-400',
    colorBg: 'bg-purple-50/70',
    colorText: 'text-purple-900',
    orden: 4,
  },
  {
    codigo: 'CONTRATISTAS',
    nombre: 'Rama Contratistas y Servicios',
    subtitulo: 'Supervisión de Cuadrillas y Proformas',
    nivel: 2,
    modulos: ['CONTRATISTAS'],
    colorBadge: 'bg-amber-100 text-amber-800 border-amber-300',
    colorBorder: 'border-amber-400',
    colorBg: 'bg-amber-50/70',
    colorText: 'text-amber-900',
    orden: 5,
  },
];

async function main() {
  const token = await login();
  const payload = JSON.parse(
    Buffer.from(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8'),
  );
  const empresaId = payload.empresaId || 'EMP-EXPORT';
  const h = headers(token, empresaId);
  console.log('empresaId', empresaId);

  let ramas = await (await fetch(`${BASE}/ramas-jerarquicas`, { headers: h })).json();
  if (!Array.isArray(ramas)) ramas = [];

  // Borrar stub incompleto DIR sin cargos si existe
  for (const r of ramas) {
    if (r.codigo === 'DIR' || (r.codigo === 'DIRECCION' && (!r.modulos || r.modulos.length === 0))) {
      const del = await fetch(`${BASE}/ramas-jerarquicas/${r.id}`, { method: 'DELETE', headers: h });
      console.log('delete stub', r.codigo, del.status);
    }
  }
  ramas = await (await fetch(`${BASE}/ramas-jerarquicas`, { headers: h })).json();
  if (!Array.isArray(ramas)) ramas = [];

  const ramaIds = {};
  for (const existing of ramas) ramaIds[existing.codigo] = existing.id;

  for (const rama of RAMAS) {
    if (ramaIds[rama.codigo]) {
      console.log('rama ok', rama.codigo);
      continue;
    }
    const r = await fetch(`${BASE}/ramas-jerarquicas`, {
      method: 'POST',
      headers: h,
      body: JSON.stringify(rama),
    });
    const body = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(`rama ${rama.codigo}: ${r.status} ${JSON.stringify(body)}`);
    ramaIds[rama.codigo] = body.id;
    console.log('rama+', rama.codigo, body.id);
  }

  let users = [];
  for (const path of ['usuarios', 'admin/usuarios']) {
    const ur = await fetch(`${BASE}/${path}`, { headers: h });
    if (ur.ok) {
      const j = await ur.json();
      users = Array.isArray(j) ? j : j?.data || j?.items || [];
      if (users.length) break;
    }
  }
  const adminId = users.find((u) => String(u.email || '').includes('admin@'))?.id || users[0]?.id || 'U-1';
  const u2 = users[1]?.id || adminId;
  const u3 = users[2]?.id || adminId;
  console.log('miembros', { adminId, u2, u3, users: users.length });

  let cargos = await (await fetch(`${BASE}/cargos-jerarquicos`, { headers: h })).json();
  if (!Array.isArray(cargos)) cargos = [];
  const cargoIds = {};
  for (const c of cargos) cargoIds[c.codigo] = c.id;

  const defs = [
    {
      codigo: 'GG-01',
      nombre: 'Gerencia General',
      ramaId: ramaIds.DIRECCION,
      rango: 1,
      nivel: 1,
      modalidadEscala: 'PARALELO_OR',
      tipoAprobacion: 'OR',
      topeClp: null,
      topeUsd: null,
      topeCny: null,
      modulos: ['COMPRAS', 'INSUMOS', 'CONTRATISTAS'],
      miembroIds: [adminId],
    },
    {
      codigo: 'AGR-GER',
      nombre: 'Gerencia Agrícola',
      ramaId: ramaIds.AGRICOLA,
      rango: 2,
      nivel: 2,
      modalidadEscala: 'PARALELO_OR',
      tipoAprobacion: 'OR',
      topeClp: 50000000,
      topeUsd: 50000,
      topeCny: 350000,
      modulos: ['COMPRAS', 'INSUMOS'],
      miembroIds: [u2, adminId],
    },
    {
      codigo: 'AGR-JEF',
      nombre: 'Jefatura de Faena',
      ramaId: ramaIds.AGRICOLA,
      rango: 3,
      nivel: 3,
      modalidadEscala: 'PARALELO_OR',
      tipoAprobacion: 'OR',
      topeClp: 2000000,
      topeUsd: 2000,
      topeCny: 14000,
      modulos: ['COMPRAS', 'INSUMOS'],
      miembroIds: [u3, u2],
    },
    {
      codigo: 'PCK-GER',
      nombre: 'Gerencia Packing',
      ramaId: ramaIds.PACKING,
      rango: 2,
      nivel: 2,
      modalidadEscala: 'PARALELO_OR',
      tipoAprobacion: 'OR',
      topeClp: 30000000,
      topeUsd: 30000,
      topeCny: 200000,
      modulos: ['COMPRAS', 'INSUMOS'],
      miembroIds: [adminId],
    },
    {
      codigo: 'ADM-GER',
      nombre: 'Gerencia Administración',
      ramaId: ramaIds.ADMINISTRACION,
      rango: 2,
      nivel: 2,
      modalidadEscala: 'UNANIME_AND',
      tipoAprobacion: 'AND',
      topeClp: 40000000,
      topeUsd: 40000,
      topeCny: 280000,
      modulos: ['COMPRAS', 'INSUMOS', 'CONTRATISTAS'],
      miembroIds: [adminId, u2],
    },
    {
      codigo: 'CTR-GER',
      nombre: 'Gerencia Contratistas',
      ramaId: ramaIds.CONTRATISTAS,
      rango: 2,
      nivel: 2,
      modalidadEscala: 'PARALELO_OR',
      tipoAprobacion: 'OR',
      topeClp: 15000000,
      topeUsd: 15000,
      topeCny: 100000,
      modulos: ['CONTRATISTAS'],
      miembroIds: [adminId],
    },
  ];

  for (const c of defs) {
    if (!c.ramaId) throw new Error(`sin ramaId para ${c.codigo}`);
    if (cargoIds[c.codigo]) {
      console.log('cargo ok', c.codigo);
      continue;
    }
    const r = await fetch(`${BASE}/cargos-jerarquicos`, {
      method: 'POST',
      headers: h,
      body: JSON.stringify({ ...c, tieneAprobacion: true }),
    });
    const body = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(`cargo ${c.codigo}: ${r.status} ${JSON.stringify(body)}`);
    cargoIds[c.codigo] = body.id;
    console.log('cargo+', c.codigo, body.id);
  }

  if (!cargoIds['AGR-ASI'] && cargoIds['AGR-JEF']) {
    const r = await fetch(`${BASE}/cargos-jerarquicos`, {
      method: 'POST',
      headers: h,
      body: JSON.stringify({
        codigo: 'AGR-ASI',
        nombre: 'Asistente Agrícola',
        ramaId: ramaIds.AGRICOLA,
        rango: 4,
        nivel: 4,
        padreCargoId: cargoIds['AGR-JEF'],
        modalidadEscala: 'PARALELO_OR',
        tieneAprobacion: true,
        tipoAprobacion: 'AND',
        topeClp: 500000,
        topeUsd: 500,
        topeCny: 3500,
        modulos: ['COMPRAS'],
        miembroIds: [u2, u3],
      }),
    });
    const body = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(`asist: ${r.status} ${JSON.stringify(body)}`);
    console.log('cargo+ AGR-ASI', body.id);
  }

  const finalRamas = await (await fetch(`${BASE}/ramas-jerarquicas`, { headers: h })).json();
  const finalCargos = await (await fetch(`${BASE}/cargos-jerarquicos`, { headers: h })).json();
  console.log('OK', { ramas: finalRamas.length, cargos: finalCargos.length });
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
