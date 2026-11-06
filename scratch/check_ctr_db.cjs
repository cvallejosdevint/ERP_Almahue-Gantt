const { PrismaClient } = require('E:/source/repos/Almahue/ERP/erp_back/node_modules/@prisma/client');
const prisma = new PrismaClient();

async function check() {
  const ctrs = await prisma.contratista.findMany({ where: { empresaId: 'EMP-EXPORT' } });
  console.log('Contratistas EMP-EXPORT:', ctrs.map(c => ({ id: c.id, rut: c.rut, razonSocial: c.razonSocial, activo: c.activo })));

  const acts = await prisma.actividad.findMany({ where: { empresaId: 'EMP-EXPORT' } });
  console.log('Actividades EMP-EXPORT:', acts.map(a => ({ id: a.id, codigo: a.codigo, nombre: a.nombre })));

  const labores = await prisma.labor.findMany({ where: { empresaId: 'EMP-EXPORT' }, include: { actividad: true } });
  console.log('Labores EMP-EXPORT:', labores.map(l => ({ id: l.id, codigo: l.codigo, nombre: l.nombre, actividad: l.actividad?.nombre })));

  const ccs = await prisma.centroCosto.findMany({ where: { empresaId: 'EMP-EXPORT' } });
  console.log('Centros de Costo EMP-EXPORT:', ccs.map(c => ({ id: c.id, codigo: c.codigo, nombre: c.nombre })));

  await prisma.$disconnect();
}
check();
