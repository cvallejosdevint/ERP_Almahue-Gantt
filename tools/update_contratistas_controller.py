path = 'ERP/erp_back/src/modules/contratistas/contratistas.controller.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target_import = "  ReabrirCierreContratistaDto,"
replacement_import = "  ReabrirCierreContratistaDto,\n  CrearAjusteCierreContratistaDto,"

endpoint = """
  @Post('contratistas/traspaso-cierre/:periodo/ajuste')
  @RequirePermissions(P.close)
  crearAjusteCierre(
    @CurrentUser() user: JwtPayload,
    @Param('periodo') periodo: string,
    @Body() dto: CrearAjusteCierreContratistaDto,
    @Headers('x-empresa-id') empresaHeader?: string,
  ) {
    return this.contratistas.crearAjusteCierre(
      user,
      periodo,
      dto,
      empresaHeader,
    );
  }
"""

norm_content = content.replace('\r\n', '\n')
norm_target_import = target_import.replace('\r\n', '\n')

if norm_target_import in norm_content:
    norm_content = norm_content.replace(norm_target_import, replacement_import.replace('\r\n', '\n'))
    last_brace = norm_content.rfind('}')
    norm_content = norm_content[:last_brace] + endpoint.replace('\r\n', '\n') + '\n}\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(norm_content.replace('\n', '\r\n'))
    print("SUCCESS: contratistas.controller.ts updated")
else:
    print("ERROR: Target import not found")

