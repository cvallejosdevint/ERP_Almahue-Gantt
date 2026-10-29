path = 'ERP/erp_back/src/modules/contratistas/contratistas.service.spec.ts'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update proforma mocks in traspasoCierre tests to include rut and id
target_pf1 = """          tipoContrato: { nombre: 'Mano de obra' },
          estado: 'FACTURADA',
          contratista: { razonSocial: 'Ctr Demo' },"""

replacement_pf1 = """          tipoContrato: { nombre: 'Mano de obra' },
          estado: 'FACTURADA',
          contratistaId: 'CTR-1',
          contratista: { id: 'CTR-1', razonSocial: 'Ctr Demo', rut: '76.123.456-7' },"""

target_pf2 = """          tipoContrato: { nombre: 'Mano de obra' },
          estado: 'DEFINITIVA',
          contratista: { razonSocial: 'Ctr Demo' },"""

replacement_pf2 = """          tipoContrato: { nombre: 'Mano de obra' },
          estado: 'DEFINITIVA',
          contratistaId: 'CTR-1',
          contratista: { id: 'CTR-1', razonSocial: 'Ctr Demo', rut: '76.123.456-7' },"""

# Update expect lineas in test 1
target_lines1 = """          lineas: [
            expect.objectContaining({ debe: 200, haber: 0, cuentaId: 'CTA-MO', centroCostoId: 'CC-1' }),
            expect.objectContaining({ debe: 0, haber: 200, cuentaId: 'CTA-FXR' }),
          ],"""

replacement_lines1 = """          lineas: [
            expect.objectContaining({ debe: 200, haber: 0, cuentaId: 'CTA-MO', centroCostoId: 'CC-1', glosa: expect.stringContaining('MO contratista') }),
            expect.objectContaining({ debe: 0, haber: 200, cuentaId: 'CTA-FXR', auxiliar: '761234567', glosa: expect.stringContaining('Facturas por recibir') }),
          ],"""

# Update R4-04 reversarProforma
target_reversa_test = """    it('reversa DEFINITIVA a BORRADOR con clave de reversa válida', async () => {
      const hash = await bcrypt.hash('4821', 10);
      prisma.proformaContratista.findUnique.mockResolvedValue({
        id: 'PRF-1',
        numero: 'PRF-1',
        empresaId: 'EMP-1',
        periodo: '2026-07',
        estado: 'DEFINITIVA',
      });
      prisma.usuario.findUnique.mockResolvedValue({
        activo: true,
        claveReversaHash: hash,
      });
      prisma.proformaContratista.update.mockResolvedValue({
        id: 'PRF-1',
        numero: 'PRF-1',
        contratistaId: 'CTR-1',
        empresaId: 'EMP-1',
        periodo: '2026-07',
        montoNeto: 1000,
        moneda: 'CLP',
        estado: 'BORRADOR',
        facturaNumeroRef: null,
        contratista: { razonSocial: 'CTR' },
        factura: null,
        registroCompra: null,
        tipoContrato: null,
      });

      const result = await service.reversarProforma(
        tenantUser({ permisos: ['contratistas:reverse'] }),
        'PRF-1',
        { claveReversa: '4821' },
      );
      expect(result.estado).toBe('BORRADOR');
      expect(prisma.ingresoLaborDiario.updateMany).toHaveBeenCalledWith(
        expect.objectContaining({
          where: expect.objectContaining({
            empresaId: 'EMP-1',
            proformaId: 'PRF-1',
            estado: 'ASOCIADO',
          }),
          data: expect.objectContaining({
            estado: 'PENDIENTE',
            proformaId: null,
          }),
        }),
      );
      expect(prisma.proformaContratista.update).toHaveBeenCalledWith(
        expect.objectContaining({
          data: expect.objectContaining({ estado: 'BORRADOR' }),
        }),
      );
    });"""

replacement_reversa_test = """    it('reversa DEFINITIVA a REVERSADA con clave de reversa válida manteniendo ingresos asociados', async () => {
      const hash = await bcrypt.hash('4821', 10);
      prisma.proformaContratista.findUnique.mockResolvedValue({
        id: 'PRF-1',
        numero: 'PRF-1',
        empresaId: 'EMP-1',
        periodo: '2026-07',
        estado: 'DEFINITIVA',
      });
      prisma.usuario.findUnique.mockResolvedValue({
        activo: true,
        claveReversaHash: hash,
      });
      prisma.proformaContratista.update.mockResolvedValue({
        id: 'PRF-1',
        numero: 'PRF-1',
        contratistaId: 'CTR-1',
        empresaId: 'EMP-1',
        periodo: '2026-07',
        montoNeto: 1000,
        moneda: 'CLP',
        estado: 'REVERSADA',
        facturaNumeroRef: null,
        contratista: { razonSocial: 'CTR' },
        factura: null,
        registroCompra: null,
        tipoContrato: null,
      });

      const result = await service.reversarProforma(
        tenantUser({ permisos: ['contratistas:reverse'] }),
        'PRF-1',
        { claveReversa: '4821' },
      );
      expect(result.estado).toBe('REVERSADA');
      expect(prisma.ingresoLaborDiario.updateMany).toHaveBeenCalledWith(
        expect.objectContaining({
          where: expect.objectContaining({
            empresaId: 'EMP-1',
            proformaId: 'PRF-1',
          }),
          data: expect.objectContaining({
            estado: 'ASOCIADO',
          }),
        }),
      );
      expect(prisma.proformaContratista.update).toHaveBeenCalledWith(
        expect.objectContaining({
          data: expect.objectContaining({ estado: 'REVERSADA' }),
        }),
      );
    });"""

ajuste_test = """
    it('genera Comprobante de Ajuste referenciado a la centralización cuando el período está cerrado', async () => {
      const createAsiento = jest.fn().mockResolvedValue({ id: 'ASI-AJUSTE', numero: 'A-200' });
      const harness = createPrismaMock();
      prisma = harness.prisma;
      service = new ContratistasService(harness.mock, { createAsiento } as never);

      prisma.periodoCierreContratista.findUnique.mockResolvedValue({
        id: 'CIE-1',
        periodo: '2026-07',
        cerrado: true,
        asientoNumero: 'A-100',
      });
      prisma.proformaContratista.findUnique.mockResolvedValue({
        id: 'PRF-1',
        numero: 'PRF-1',
        empresaId: 'EMP-1',
        periodo: '2026-07',
        montoNeto: 500,
        moneda: 'CLP',
        contratista: { razonSocial: 'Ctr Demo', rut: '76.123.456-7' },
      });
      prisma.cuentaContable.findFirst.mockImplementation(async (args: { where?: { codigo?: string } }) => {
        if (args?.where?.codigo === '6-1-01-01-002') return { id: 'CTA-MO' };
        if (args?.where?.codigo === '2-1-08-02-003') return { id: 'CTA-FXR' };
        return null;
      });
      prisma.usuario.findUnique.mockResolvedValue({ nombre: 'Supervisor' });
      prisma.periodoCierreContratistaEvento.create.mockResolvedValue({ id: 'EVT-1' });

      const res = await service.crearAjusteCierre(
        tenantUser({ permisos: ['contratistas:close'] }),
        '2026-07',
        { proformaId: 'PRF-1', motivo: 'Reclasificación centro de costo' },
        'EMP-1',
      );

      expect(res.ok).toBe(true);
      expect(res.asientoNumero).toBe('A-200');
      expect(createAsiento).toHaveBeenCalledWith(
        expect.objectContaining({
          tipo: 'CIERRE',
          origen: 'AJUSTE-CTR:2026-07:PRF-1',
        }),
      );
    });
"""

norm_content = content.replace('\r\n', '\n')

def apply_sub(text, t, r, name):
    norm_t = t.replace('\r\n', '\n')
    norm_r = r.replace('\r\n', '\n')
    if norm_t not in text:
        raise ValueError(f"Target not found: {name}")
    print(f"Applied: {name}")
    return text.replace(norm_t, norm_r)

norm_content = apply_sub(norm_content, target_pf1, replacement_pf1, "proforma 1")
norm_content = apply_sub(norm_content, target_pf2, replacement_pf2, "proforma 2")
norm_content = apply_sub(norm_content, target_lines1, replacement_lines1, "lines 1")
norm_content = apply_sub(norm_content, target_reversa_test, replacement_reversa_test, "reversa test")

# Add ajuste_test into EX-04/EX-05 describe
target_ex = "      expect(result.detalle).toHaveLength(1);\n    });"
replacement_ex = "      expect(result.detalle).toHaveLength(1);\n    });\n" + ajuste_test.replace('\r\n', '\n')

norm_content = apply_sub(norm_content, target_ex, replacement_ex, "ajuste test")

with open(path, 'w', encoding='utf-8') as f:
    f.write(norm_content.replace('\n', '\r\n'))

print("ALL CHANGES APPLIED TO contratistas.service.spec.ts")

