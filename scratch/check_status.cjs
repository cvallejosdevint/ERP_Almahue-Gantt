const { Client } = require('E:/source/repos/Almahue/ERP/erp_back/node_modules/pg');
const client = new Client({ connectionString: 'postgresql://almahue:almahue@localhost:5433/almahue?schema=erp' });

async function checkAsiento() {
  await client.connect();
  const asiento = await client.query('SELECT * FROM erp."Asiento" WHERE numero = \'20260009\'');
  console.log('Asiento 20260009:', JSON.stringify(asiento.rows[0], null, 2));
  await client.end();
}

checkAsiento().catch(console.error);
