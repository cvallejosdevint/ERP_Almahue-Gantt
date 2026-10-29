path = 'ERP/erp_back/src/modules/contratistas/contratistas.service.ts'
with open(path, 'rb') as f:
    text = f.read().decode('utf-8').replace('\r\n', '\n')

target_import = "import { assertPinAprobacion } from '../../auth/pin-aprobacion';"
replacement_import = "import { assertPinAprobacion, usuarioPuedeUsarPinAprobacion } from '../../auth/pin-aprobacion';"

target_ajuste = """    const cierre = await this.prisma.periodoCierreContratista.findUnique({
      where: { empresaId_periodo: { empresaId, periodo } },
    });
    if (!cierre?.cerrado) {
      throw new BadRequestException(`El período ${periodo} aún no ha sido cerrado/centralizado`);
    }

    await assertPinAprobacion(this.prisma, user.sub, dto.pinAprobacion, { force: true });"""

replacement_ajuste = """    const cierre = await this.prisma.periodoCierreContratista.findUnique({
      where: { empresaId_periodo: { empresaId, periodo } },
    });
    if (!cierre?.cerrado) {
      throw new BadRequestException(`El período ${periodo} aún no ha sido cerrado/centralizado`);
    }

    // Regla de autorización: el usuario debe ser Administrador o estar configurado en las reglas de aprobación
    const permisos = user.permisos ?? [];
    const esAdminORegla =
      permisos.includes('*')
      || isSuperAdmin(user)
      || (await usuarioPuedeUsarPinAprobacion(this.prisma, user.sub));
    if (!esAdminORegla) {
      throw new BadRequestException(
        'No está autorizado para emitir ajustes contables: debe ser Administrador o estar configurado en las reglas de aprobación',
      );
    }

    await assertPinAprobacion(this.prisma, user.sub, dto.pinAprobacion, { force: true });"""

if target_import in text:
    text = text.replace(target_import, replacement_import)
    print("Import updated")
else:
    print("ERROR: target_import not found")

if target_ajuste in text:
    text = text.replace(target_ajuste, replacement_ajuste)
    print("Ajuste approval check updated")
else:
    print("ERROR: target_ajuste not found")

with open(path, 'wb') as f:
    f.write(text.replace('\n', '\r\n').encode('utf-8'))

print("FINISHED UPDATING contratistas.service.ts")

