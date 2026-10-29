# 1. Update contratistas.service.ts
path_svc = 'ERP/erp_back/src/modules/contratistas/contratistas.service.ts'
with open(path_svc, 'rb') as f:
    text_svc = f.read().decode('utf-8').replace('\r\n', '\n')

target_reversa = """    if (existing.estado !== 'DEFINITIVA' && existing.estado !== 'ENVIADA_CONTRATISTA') {
      throw new BadRequestException(
        'Solo se puede reversar una proforma Definitiva o notificada al contratista',
      );
    }
    await this.assertPeriodoOperable(existing.empresaId, existing.periodo);"""

replacement_reversa = """    if (existing.estado !== 'DEFINITIVA' && existing.estado !== 'ENVIADA_CONTRATISTA') {
      throw new BadRequestException(
        'Solo se puede reversar una proforma Definitiva o notificada al contratista',
      );
    }
    this.assertProformaSinFacturaParaModificacion(existing);
    await this.assertPeriodoOperable(existing.empresaId, existing.periodo);"""

target_ajuste = """    if (proforma.empresaId !== empresaId) {
      throw new BadRequestException('La proforma no pertenece a la empresa actual');
    }
    const cierre = await this.prisma.periodoCierreContratista.findUnique({
      where: { empresaId_periodo: { empresaId, periodo } },
    });
    if (!cierre?.cerrado) {
      throw new BadRequestException(`El período ${periodo} aún no ha sido cerrado/centralizado`);
    }

    if (dto.pinAprobacion) {
      await assertPinAprobacion(this.prisma, user.sub, dto.pinAprobacion, { force: true });
    }"""

replacement_ajuste = """    if (proforma.empresaId !== empresaId) {
      throw new BadRequestException('La proforma no pertenece a la empresa actual');
    }
    if (proforma.periodo !== periodo) {
      throw new BadRequestException(`La proforma pertenece al período ${proforma.periodo}, no al período ${periodo}`);
    }
    const cierre = await this.prisma.periodoCierreContratista.findUnique({
      where: { empresaId_periodo: { empresaId, periodo } },
    });
    if (!cierre?.cerrado) {
      throw new BadRequestException(`El período ${periodo} aún no ha sido cerrado/centralizado`);
    }

    await assertPinAprobacion(this.prisma, user.sub, dto.pinAprobacion, { force: true });"""

if target_reversa in text_svc:
    text_svc = text_svc.replace(target_reversa, replacement_reversa)
    print("Reversa updated in service")
else:
    print("ERROR: target_reversa not found")

if target_ajuste in text_svc:
    text_svc = text_svc.replace(target_ajuste, replacement_ajuste)
    print("Ajuste updated in service")
else:
    print("ERROR: target_ajuste not found")

with open(path_svc, 'wb') as f:
    f.write(text_svc.replace('\n', '\r\n').encode('utf-8'))

# 2. Update contratistas.dto.ts
path_dto = 'ERP/erp_back/src/modules/contratistas/dto/contratistas.dto.ts'
with open(path_dto, 'rb') as f:
    text_dto = f.read().decode('utf-8').replace('\r\n', '\n')

target_dto_pin = """  @ApiPropertyOptional({ description: 'PIN de aprobación de la jefatura' })
  @IsOptional()
  @IsString()
  pinAprobacion?: string;"""

replacement_dto_pin = """  @ApiProperty({ description: 'PIN de aprobación de la jefatura (4 dígitos)' })
  @IsString()
  @MinLength(4)
  @MaxLength(4)
  pinAprobacion: string;"""

if target_dto_pin in text_dto:
    text_dto = text_dto.replace(target_dto_pin, replacement_dto_pin)
    print("PIN updated in dto")
else:
    print("ERROR: target_dto_pin not found")

with open(path_dto, 'wb') as f:
    f.write(text_dto.replace('\n', '\r\n').encode('utf-8'))

print("SECURITY REMEDIATIONS APPLIED")

