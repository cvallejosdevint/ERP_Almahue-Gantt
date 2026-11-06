const fs = require('fs');

// 1. Fix contabilidad.dto.ts
let dtoPath = 'ERP/erp_back/src/modules/contabilidad/dto/contabilidad.dto.ts';
let dto = fs.readFileSync(dtoPath, 'utf8');

// Fix CreateCuentaDto duplicates
const dupTarget = `  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVariedad?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereAux?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereRef?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereAux?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereRef?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereAux?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereRef?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVencimiento?: boolean;`;

const singleRepl = `  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVariedad?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereAux?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereRef?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVencimiento?: boolean;`;

dto = dto.replace(/\r\n/g, '\n');
if (dto.includes(dupTarget.replace(/\r\n/g, '\n'))) {
  dto = dto.replace(dupTarget.replace(/\r\n/g, '\n'), singleRepl.replace(/\r\n/g, '\n'));
  console.log('Fixed CreateCuentaDto duplicates');
}

// Add to UpdateCuentaDto
const updateTarget = `  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVariedad?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVencimiento?: boolean;`;
const updateRepl = `  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVariedad?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereAux?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereRef?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVencimiento?: boolean;`;

if (dto.includes(updateTarget)) {
  dto = dto.replace(updateTarget, updateRepl);
  console.log('Added requiereAux/Ref to UpdateCuentaDto');
}

// Add to BulkCuentaItemDto
const bulkTarget = `  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVariedad?: boolean;
  @ApiPropertyOptional() @IsOptional() @IsBoolean() requiereVencimiento?: boolean;`;
if (dto.includes(bulkTarget)) {
  dto = dto.replace(bulkTarget, updateRepl);
  console.log('Added requiereAux/Ref to BulkCuentaItemDto');
}

fs.writeFileSync(dtoPath, dto.replace(/\n/g, '\r\n'), 'utf8');

// 2. Fix contabilidad.service.ts
let svcPath = 'ERP/erp_back/src/modules/contabilidad/contabilidad.service.ts';
let svc = fs.readFileSync(svcPath, 'utf8').replace(/\r\n/g, '\n');

// In findMany select (around line 1308)
const selectTarget = `          requierePlanta: true,
          requiereVariedad: true,
          requiereVencimiento: true,`;
const selectRepl = `          requierePlanta: true,
          requiereVariedad: true,
          requiereAux: true,
          requiereRef: true,
          requiereVencimiento: true,`;
if (svc.includes(selectTarget)) {
  svc = svc.replace(selectTarget, selectRepl);
  console.log('Added requiereAux/Ref to findMany select in contabilidad.service.ts');
}

// In clasificarFilaImport lines (1333-1334 and 1354-1355)
const fieldsTarget = `      { key: 'requiereVariedad' as const, label: 'VAR' },
      { key: 'requiereAux' as const, label: 'AUX' },
      { key: 'requiereRef' as const, label: 'REF' },
      { key: 'requiereVencimiento' as const, label: 'VCTO' },`;
const fieldsRepl = `      { key: 'requiereVariedad' as const, label: 'VAR' },
      { key: 'requiereVencimiento' as const, label: 'VCTO' },`;
if (svc.includes(fieldsTarget)) {
  svc = svc.replace(fieldsTarget, fieldsRepl);
  console.log('Removed AUX/REF from Excel fields import definition');
}

const callTarget = `          requierePlanta: it.requierePlanta,
          requiereVariedad: it.requiereVariedad,
          requiereAux: it.requiereAux,
          requiereRef: it.requiereRef,
          requiereVencimiento: it.requiereVencimiento,`;
const callRepl = `          requierePlanta: it.requierePlanta,
          requiereVariedad: it.requiereVariedad,
          requiereVencimiento: it.requiereVencimiento,`;
if (svc.includes(callTarget)) {
  svc = svc.replace(callTarget, callRepl);
  console.log('Removed it.requiereAux/Ref from clasificarFilaImport call');
}

const prevTarget = `              requierePlanta: prev.requierePlanta,
              requiereVariedad: prev.requiereVariedad,
              requiereAux: prev.requiereAux,
              requiereRef: prev.requiereRef,
              requiereVencimiento: prev.requiereVencimiento,`;
const prevRepl = `              requierePlanta: prev.requierePlanta,
              requiereVariedad: prev.requiereVariedad,
              requiereVencimiento: prev.requiereVencimiento,`;
if (svc.includes(prevTarget)) {
  svc = svc.replace(prevTarget, prevRepl);
  console.log('Removed prev.requiereAux/Ref from clasificarFilaImport call');
}

fs.writeFileSync(svcPath, svc.replace(/\n/g, '\r\n'), 'utf8');
console.log('Backend files fixed.');

