const { Client } = require('E:/source/repos/Almahue/ERP/erp_back/node_modules/pg');

const client = new Client({
  connectionString: 'postgresql://almahue:almahue@localhost:5433/almahue?schema=erp'
});

async function run() {
  await client.connect();
  
  const bancos = await client.query('SELECT * FROM erp."Banco" WHERE "empresaId" = \'EMP-EXPORT\'');
  console.log('Bancos EMP-EXPORT:', bancos.rows);

  const acts = await client.query('SELECT id, codigo, nombre FROM erp."Actividad" WHERE "empresaId" = \'EMP-EXPORT\'');
  console.log('Actividades EMP-EXPORT:', acts.rows);

  const labores = await client.query('SELECT id, codigo, nombre FROM erp."Labor" WHERE "empresaId" = \'EMP-EXPORT\'');
  console.log('Labores EMP-EXPORT:', labores.rows);

  const ccs = await client.query('SELECT id, codigo, nombre FROM erp."CentroCosto" WHERE "empresaId" = \'EMP-EXPORT\'');
  console.log('Centros de Costo EMP-EXPORT:', ccs.rows);

  await client.end();
}

run().catch(console.error);
