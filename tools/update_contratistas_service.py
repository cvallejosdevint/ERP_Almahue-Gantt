import re

path = 'ERP/erp_back/src/modules/contratistas/contratistas.service.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
target_import = "  TraspasoCierreDto,\n  ReabrirCierreContratistaDto,"
replacement_import = "  TraspasoCierreDto,\n  ReabrirCierreContratistaDto,\n  CrearAjusteCierreContratistaDto,"

# 2. Update updateProforma editable condition
target_update_editable = """    const editable =
      existing.estado === 'BORRADOR'
      || existing.estado === 'PENDIENTE_APROBACION'
      || (
        Boolean(existing.modificacionAutorizadaAt)
        && existing.estado !== 'FACTURADA'
        && !existing.registroCompraId
      );"""

replacement_update_editable = """    const editable =
      existing.estado === 'BORRADOR'
      || existing.estado === 'PENDIENTE_APROBACION'
      || existing.estado === 'REVERSADA'
      || (
        Boolean(existing.modificacionAutorizadaAt)
        && existing.estado !== 'FACTURADA'
        && !existing.registroCompraId
      );"""

# 3. Update patchCentrosCostoProforma editable condition
target_patch_editable = """    const editable =
      existing.estado === 'BORRADOR'
      || existing.estado === 'PENDIENTE_APROBACION'
      || Boolean(existing.modificacionAutorizadaAt);"""

replacement_patch_editable = """    const editable =
      existing.estado === 'BORRADOR'
      || existing.estado === 'PENDIENTE_APROBACION'
      || existing.estado === 'REVERSADA'
      || Boolean(existing.modificacionAutorizadaAt);"""

# 4. Update solicitarAprobacionProforma condition
target_solicitar = """    if (existing.estado !== 'BORRADOR') {
      throw new BadRequestException(
        'Solo proformas en Borrador pueden solicitarse para aprobación',
      );
    }"""

replacement_solicitar = """    if (existing.estado !== 'BORRADOR' && existing.estado !== 'REVERSADA') {
      throw new BadRequestException(
        'Solo proformas en Borrador o Reversadas pueden solicitarse para aprobación',
      );
    }"""

# 5. Update reversarProforma implementation
target_reversar = """    await this.prisma.ingresoLaborDiario.updateMany({
      where: {
        empresaId: existing.empresaId,
        proformaId: existing.id,
        estado: 'ASOCIADO',
      },
      data: {
        estado: 'PENDIENTE',
        proformaId: null,
      },
    });

    const row = await this.prisma.proformaContratista.update({
      where: { id },
      data: {
        estado: 'BORRADOR',
        aprobadoPorId: null,
        aprobadoPorNombre: null,
        aprobadaAt: null,
        enviadaContratistaAt: null,
        enviadaContratistaPorId: null,
        enviadaContratistaPorNombre: null,
      },
      include: proformaInclude,
    });"""

replacement_reversar = """    // Mantener los ingresos vinculados para permitir edición de CC, tarifa o líneas
    await this.prisma.ingresoLaborDiario.updateMany({
      where: {
        empresaId: existing.empresaId,
        proformaId: existing.id,
      },
      data: {
        estado: 'ASOCIADO',
      },
    });

    const row = await this.prisma.proformaContratista.update({
      where: { id },
      data: {
        estado: 'REVERSADA',
        aprobadoPorId: null,
        aprobadoPorNombre: null,
        aprobadaAt: null,
        enviadaContratistaAt: null,
        enviadaContratistaPorId: null,
        enviadaContratistaPorNombre: null,
      },
      include: proformaInclude,
    });"""

# 6. Update traspasoCierre proformas findMany and asiento generation
target_proformas_find = """    const proformas = await this.prisma.proformaContratista.findMany({
      where: {
        empresaId,
        periodo,
        estado: { in: [...ESTADOS_PROFORMA_TRASPASO] },
      },
      include: {
        contratista: { select: { razonSocial: true } },
        tipoContrato: { select: { nombre: true } },
      },
      orderBy: { numero: 'asc' },
    });"""

replacement_proformas_find = """    const proformas = await this.prisma.proformaContratista.findMany({
      where: {
        empresaId,
        periodo,
        estado: { in: [...ESTADOS_PROFORMA_TRASPASO] },
      },
      include: {
        contratista: { select: { id: true, razonSocial: true, rut: true } },
        tipoContrato: { select: { nombre: true } },
      },
      orderBy: { numero: 'asc' },
    });"""

target_ingresos_and_asiento = """      const ingresos = await this.prisma.ingresoLaborDiario.findMany({
        where: {
          empresaId,
          proformaId: { in: proformaIds },
          estado: { in: ['ASOCIADO', 'FACTURADO'] },
        },
        select: {
          id: true,
          proformaId: true,
          tipoContratoId: true,
          centroCostoId: true,
          laborId: true,
          actividadId: true,
          monto: true,
          labor: { select: { nombre: true } },
          actividad: { select: { nombre: true } },
        },
      });
      const cuentasCierre = await this.resolveCuentasCierreSala(empresaId, {
        debeId: dto.cuentaDebeId,
        haberId: dto.cuentaHaberId,
      });
      const proformaById = new Map(proformas.map((p) => [p.id, p]));
      type GrupoCierre = {
        centroCostoId: string;
        laborId: string;
        actividadId: string;
        laborNombre: string;
        actividadNombre: string;
        monto: number;
      };
      const grupos = new Map<string, GrupoCierre>();
      for (const ingreso of ingresos) {
        const proforma = ingreso.proformaId
          ? proformaById.get(ingreso.proformaId)
          : undefined;
        if (!proforma) {
          throw new BadRequestException(
            `El ingreso ${ingreso.id} no tiene una proforma del periodo`,
          );
        }
        const centroCostoId = ingreso.centroCostoId;
        const laborId = ingreso.laborId;
        const actividadId = ingreso.actividadId;
        const groupKey = `${centroCostoId}|${laborId}|${actividadId}`;
        const actual = grupos.get(groupKey) ?? {
          centroCostoId,
          laborId,
          actividadId,
          laborNombre: ingreso.labor.nombre,
          actividadNombre: ingreso.actividad.nombre,
          monto: 0,
        };
        actual.monto +=
          Number(ingreso.monto) * tiposCambio[proforma.moneda.toUpperCase()];
        grupos.set(groupKey, actual);
      }
      const lineasDebe = [...grupos.values()].map((grupo) => ({
        debe: Math.round(grupo.monto * 100) / 100,
        haber: 0,
        cuentaId: cuentasCierre.debeId,
        centroCostoId: grupo.centroCostoId,
        glosa: `MO contratista · ${grupo.laborNombre} / ${grupo.actividadNombre}`,
      }));
      const lineasHaber = [{
        debe: 0,
        haber: Math.round(lineasDebe.reduce((sum, l) => sum + l.debe, 0) * 100) / 100,
        cuentaId: cuentasCierre.haberId,
        glosa: 'Facturas por recibir contratista',
      }];"""

replacement_ingresos_and_asiento = """      const ingresos = await this.prisma.ingresoLaborDiario.findMany({
        where: {
          empresaId,
          proformaId: { in: proformaIds },
          estado: { in: ['ASOCIADO', 'FACTURADO'] },
        },
        select: {
          id: true,
          proformaId: true,
          tipoContratoId: true,
          centroCostoId: true,
          centroCosto: { select: { id: true, nombre: true, codigo: true } },
          laborId: true,
          actividadId: true,
          monto: true,
          labor: { select: { nombre: true } },
          actividad: { select: { nombre: true } },
        },
      });
      const cuentasCierre = await this.resolveCuentasCierreSala(empresaId, {
        debeId: dto.cuentaDebeId,
        haberId: dto.cuentaHaberId,
      });
      const proformaById = new Map(proformas.map((p) => [p.id, p]));

      // 3.5 Débitos: agrupados estrictamente por Centro de Costo (GROUP BY centroCostoId)
      type GrupoCentroCosto = {
        centroCostoId: string;
        centroCostoNombre: string;
        monto: number;
      };
      const gruposCC = new Map<string, GrupoCentroCosto>();
      for (const ingreso of ingresos) {
        const proforma = ingreso.proformaId
          ? proformaById.get(ingreso.proformaId)
          : undefined;
        if (!proforma) {
          throw new BadRequestException(
            `El ingreso ${ingreso.id} no tiene una proforma del periodo`,
          );
        }
        const centroCostoId = ingreso.centroCostoId;
        const actual = gruposCC.get(centroCostoId) ?? {
          centroCostoId,
          centroCostoNombre: ingreso.centroCosto?.nombre || 'Centro de Costo',
          monto: 0,
        };
        actual.monto +=
          Number(ingreso.monto) * tiposCambio[proforma.moneda.toUpperCase()];
        gruposCC.set(centroCostoId, actual);
      }
      const lineasDebe = [...gruposCC.values()].map((grupo) => ({
        debe: Math.round(grupo.monto * 100) / 100,
        haber: 0,
        cuentaId: cuentasCierre.debeId,
        centroCostoId: grupo.centroCostoId,
        glosa: `MO contratista · ${grupo.centroCostoNombre}`,
      }));

      // 3.5 Créditos: provisión segregada por Contratista con auxiliar RUT / Razón Social
      type GrupoContratista = {
        contratistaId: string;
        razonSocial: string;
        rut: string;
        monto: number;
      };
      const gruposContratista = new Map<string, GrupoContratista>();
      for (const proforma of proformas) {
        const contratistaId = proforma.contratistaId;
        const actual = gruposContratista.get(contratistaId) ?? {
          contratistaId,
          razonSocial: proforma.contratista.razonSocial,
          rut: proforma.contratista.rut,
          monto: 0,
        };
        actual.monto +=
          Number(proforma.montoNeto) * tiposCambio[proforma.moneda.toUpperCase()];
        gruposContratista.set(contratistaId, actual);
      }
      const lineasHaber = [...gruposContratista.values()].map((gc) => ({
        debe: 0,
        haber: Math.round(gc.monto * 100) / 100,
        cuentaId: cuentasCierre.haberId,
        auxiliar: normalizeRut(gc.rut),
        glosa: `Facturas por recibir contratista · ${gc.razonSocial}`,
      }));

      const totalDebe = lineasDebe.reduce((sum, l) => sum + l.debe, 0);
      const totalHaber = lineasHaber.reduce((sum, l) => sum + l.haber, 0);
      const diffCentavos = Math.round((totalDebe - totalHaber) * 100) / 100;
      if (diffCentavos !== 0 && lineasHaber.length > 0) {
        lineasHaber[lineasHaber.length - 1].haber =
          Math.round((lineasHaber[lineasHaber.length - 1].haber + diffCentavos) * 100) / 100;
      }"""

# 7. Add crearAjusteCierre method
metodo_ajuste = """  /**
   * Comprobante Contable de Ajuste referenciado a la centralización mensual
   * cuando el período está cerrado (sin desarmar el asiento original de centralización).
   */
  async crearAjusteCierre(
    user: JwtPayload,
    periodoRaw: string,
    dto: CrearAjusteCierreContratistaDto,
    empresaHeader?: string,
  ) {
    const empresaId = this.activeEmpresa(user, empresaHeader);
    const periodo = assertPeriodoContratista(periodoRaw);
    const proforma = await this.prisma.proformaContratista.findUnique({
      where: { id: dto.proformaId },
      include: { contratista: { select: { razonSocial: true, rut: true } } },
    });
    if (!proforma) throw new NotFoundException('Proforma no encontrada');
    if (proforma.empresaId !== empresaId) {
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
    }

    if (!this.contabilizar) {
      throw new BadRequestException('Servicio de contabilización no disponible');
    }

    const actor = await this.prisma.usuario.findUnique({
      where: { id: user.sub },
      select: { nombre: true },
    });
    const usuarioNombre = actor?.nombre ?? user.email;

    const cuentasCierre = await this.resolveCuentasCierreSala(empresaId, {});
    let lineasInput: LineaAsientoInput[] = [];

    if (dto.lineas && dto.lineas.length > 0) {
      lineasInput = dto.lineas.map((l) => ({
        debe: Math.round(Number(l.debe || 0) * 100) / 100,
        haber: Math.round(Number(l.haber || 0) * 100) / 100,
        cuentaId: l.cuentaId || (l.debe > 0 ? cuentasCierre.debeId : cuentasCierre.haberId),
        centroCostoId: l.centroCostoId,
        auxiliar: l.auxiliar ? normalizeRut(l.auxiliar) : undefined,
        glosa: l.glosa || `Ajuste proforma ${proforma.numero} · ${dto.motivo.trim()}`,
      }));
    } else {
      lineasInput = [
        {
          debe: Math.round(Number(proforma.montoNeto) * 100) / 100,
          haber: 0,
          cuentaId: cuentasCierre.debeId,
          glosa: `Ajuste MO proforma ${proforma.numero} · ${dto.motivo.trim()}`,
        },
        {
          debe: 0,
          haber: Math.round(Number(proforma.montoNeto) * 100) / 100,
          cuentaId: cuentasCierre.haberId,
          auxiliar: normalizeRut(proforma.contratista.rut),
          glosa: `Ajuste provisión ${proforma.contratista.razonSocial} · ${dto.motivo.trim()}`,
        },
      ];
    }

    const totalDebe = lineasInput.reduce((s, l) => s + l.debe, 0);
    const totalHaber = lineasInput.reduce((s, l) => s + l.haber, 0);
    if (Math.abs(totalDebe - totalHaber) > 0.01) {
      throw new BadRequestException('El comprobante de ajuste contable debe estar cuadrado (Debe = Haber)');
    }

    const glosaAsiento = dto.glosa?.trim() || `Ajuste Contratistas ${periodo} · Proforma ${proforma.numero}: ${dto.motivo.trim()}`;

    const asiento = await this.contabilizar.createAsiento({
      empresaId,
      glosa: glosaAsiento,
      tipo: 'CIERRE',
      origen: `AJUSTE-CTR:${periodo}:${proforma.id}`,
      periodo,
      lineas: lineasInput,
    });

    await this.prisma.periodoCierreContratistaEvento.create({
      data: {
        cierreId: cierre.id,
        empresaId,
        accion: 'AJUSTE_CONTABLE',
        motivo: `Asiento ${asiento.numero}: ${dto.motivo.trim()}`,
        usuarioId: user.sub,
        usuarioNombre,
      },
    });

    await this.registrarAuditoria(user, {
      empresaId,
      entidad: 'CIERRE_CONTRATISTA',
      entidadId: cierre.id,
      accion: 'AJUSTE_CONTABLE',
      antes: { asientoOriginal: cierre.asientoNumero },
      despues: { asientoAjuste: asiento.numero, motivo: dto.motivo.trim() },
    });

    return {
      ok: true,
      asientoId: asiento.id,
      asientoNumero: asiento.numero,
      mensaje: `Comprobante de ajuste ${asiento.numero} generado exitosamente referenciado a la centralización ${periodo}`,
    };
  }
"""

norm_content = content.replace('\r\n', '\n')

def apply_replace(text, t, r, name):
    norm_t = t.replace('\r\n', '\n')
    norm_r = r.replace('\r\n', '\n')
    if norm_t not in text:
        raise ValueError(f"Target not found: {name}")
    print(f"Applied: {name}")
    return text.replace(norm_t, norm_r)

norm_content = apply_replace(norm_content, target_import, replacement_import, "Import Dto")
norm_content = apply_replace(norm_content, target_update_editable, replacement_update_editable, "Update editable")
norm_content = apply_replace(norm_content, target_patch_editable, replacement_patch_editable, "Patch editable")
norm_content = apply_replace(norm_content, target_solicitar, replacement_solicitar, "Solicitar proforma")
norm_content = apply_replace(norm_content, target_reversar, replacement_reversar, "Reversar proforma")
norm_content = apply_replace(norm_content, target_proformas_find, replacement_proformas_find, "Proformas find")
norm_content = apply_replace(norm_content, target_ingresos_and_asiento, replacement_ingresos_and_asiento, "Ingresos and Asiento CC + Contratista")

# Insert crearAjusteCierre before the closing brace of the class
last_brace = norm_content.rfind('}')
norm_content = norm_content[:last_brace] + '\n' + metodo_ajuste.replace('\r\n', '\n') + '\n}\n'

with open(path, 'w', encoding='utf-8') as f:
    f.write(norm_content.replace('\n', '\r\n'))

print("ALL CHANGES APPLIED TO contratistas.service.ts")

