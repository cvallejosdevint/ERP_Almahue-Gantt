const { Client } = require('E:/source/repos/Almahue/ERP/erp_back/node_modules/pg');
const client = new Client({ connectionString: 'postgresql://almahue:almahue@localhost:5433/almahue?schema=erp' });

async function cleanupSample() {
  await client.connect();
  console.log('Cleaning up old Oct 21 test sample...');
  
  // Delete eventos de cierre if any
  await client.query('DELETE FROM erp."PeriodoCierreContratistaEvento" WHERE "cierreId" = \'cmvi76ygf000j9oty1wljpn99\'');
  
  // Delete cierre
  await client.query('DELETE FROM erp."PeriodoCierreContratista" WHERE id = \'cmvi76ygf000j9oty1wljpn99\'');
  
  // Delete old asiento
  await client.query('DELETE FROM erp."Asiento" WHERE id = \'cmvi76ygc000i9otyvv8ad1l2\'');
  
  // Delete old ingreso
  await client.query('DELETE FROM erp."IngresoLaborDiario" WHERE id = \'cmvi5sy2600019otyra7newsl\'');
  
  // Delete old proforma
  await client.query('DELETE FROM erp."ProformaContratista" WHERE id = \'cmvi5sy4800029otyk6d8nuwc\'');
  
  console.log('Cleanup completed successfully.');
  await client.end();
}

cleanupSample().catch(console.error);
