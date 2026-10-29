import re

path = 'ERP/erp_back/src/modules/contratistas/dto/contratistas.dto.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''export class ReabrirCierreContratistaDto {
  @ApiProperty({ minLength: 5 })
  @IsString()
  @MinLength(5)
  motivo: string;
}'''

addition = '''export class LineaAjusteCierreDto {
  @ApiProperty({ description: 'Monto al Debe en CLP' })
  @IsNumber()
  debe: number;

  @ApiProperty({ description: 'Monto al Haber en CLP' })
  @IsNumber()
  haber: number;

  @ApiPropertyOptional({ description: 'ID de la cuenta contable' })
  @IsOptional()
  @IsString()
  cuentaId?: string;

  @ApiPropertyOptional({ description: 'ID del centro de costo' })
  @IsOptional()
  @IsString()
  centroCostoId?: string;

  @ApiPropertyOptional({ description: 'RUT auxiliar del contratista/proveedor' })
  @IsOptional()
  @IsString()
  auxiliar?: string;

  @ApiPropertyOptional({ description: 'Glosa explicativa de la línea' })
  @IsOptional()
  @IsString()
  glosa?: string;
}

export class CrearAjusteCierreContratistaDto {
  @ApiProperty({ description: 'ID de la proforma afectada por el ajuste' })
  @IsString()
  @MinLength(1)
  proformaId: string;

  @ApiProperty({ description: 'Motivo del ajuste contable' })
  @IsString()
  @MinLength(5)
  motivo: string;

  @ApiPropertyOptional({ description: 'Glosa del comprobante' })
  @IsOptional()
  @IsString()
  glosa?: string;

  @ApiPropertyOptional({ description: 'PIN de aprobación de la jefatura' })
  @IsOptional()
  @IsString()
  pinAprobacion?: string;

  @ApiPropertyOptional({ description: 'Líneas contables específicas del ajuste', type: [LineaAjusteCierreDto] })
  @IsOptional()
  @IsArray()
  @ValidateNested({ each: true })
  @Type(() => LineaAjusteCierreDto)
  lineas?: LineaAjusteCierreDto[];
}
'''

norm_content = content.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')

if norm_target in norm_content:
    new_norm = norm_content.replace(norm_target, norm_target + '\n\n' + addition.replace('\r\n', '\n'))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_norm.replace('\n', '\r\n'))
    print("SUCCESS: contratistas.dto.ts updated")
else:
    print("ERROR: Target not found")

