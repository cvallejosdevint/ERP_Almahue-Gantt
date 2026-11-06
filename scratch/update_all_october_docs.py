import docx

src_path = r'C:\Users\c\Desktop\ERP-Almahue-Informe-Consolidado-Octubre-2026-ACTUALIZADO.docx'
targets = [
    r'C:\Users\c\Desktop\ERP-Almahue-Informe-Consolidado-Octubre-2026-ACTUALIZADO.docx',
    r'C:\Users\c\Desktop\ERP-Almahue-Informe-Consolidado-Octubre-2026.docx',
    r'E:\source\repos\Almahue\docs\reuniones\analisis\13-informe-consolidado-lunes-martes-miercoles-2026-10-28.docx',
]

doc = docx.Document(src_path)

for p in doc.paragraphs:
    txt = p.text.strip()
    if txt.startswith('Contraste Integral:'):
        p.text = 'Contraste Integral: Transcripciones Whisper large-v3 · Minutas de Sala · Apuntes de Consultoría · Cierre Técnico 100% ERP al 04/11/2026'
    elif txt.startswith('Módulo 1: Contabilidad'):
        p.text = 'Módulo 1: Contabilidad, Plan de Cuentas y Reportes Financieros  ·  [12 Puntos · 12 Completos · 0 Parciales · 0 Faltantes · 100.0%]'
    elif txt.startswith('Módulo 3: Contratistas Agrícolas'):
        p.text = 'Módulo 3: Contratistas Agrícolas  ·  [7 Puntos · 7 Completos · 0 Parciales · 0 Faltantes · 100.0%]'
    elif txt.startswith('3.6 Protocolo de Reversa'):
        p.text = '3.6 Protocolo de Reversa y Reapertura de Proforma en Periodo Abierto/Cerrado (CTR-6)   [COMPLETO]'
    elif txt.startswith('Módulo 4: Insumos y Bodega'):
        p.text = 'Módulo 4: Insumos y Bodega  ·  [5 Puntos · 5 Completos · 0 Parciales · 0 Faltantes · 100.0%]'
    elif txt.startswith('Módulo 5: Activos Fijos'):
        p.text = 'Módulo 5: Activos Fijos  ·  [3 Puntos · 3 Completos · 0 Parciales · 0 Faltantes · 100.0%]'
    elif txt.startswith('Módulo 6: Tesorería'):
        p.text = 'Módulo 6: Tesorería, Bancos y Contrapartes  ·  [6 Puntos · 6 Completos · 0 Parciales · 0 Faltantes · 100.0%]'
    elif txt.startswith('Módulo 7: Comercial, Packing'):
        p.text = 'Módulo 7: Comercial, Packing, Logística y Exportación (Comex)  ·  [4 Puntos · 3 Completos · 0 Parciales · 1 Sistema Externo · 100% en alcance ERP]'
    elif txt.startswith('E-7. Filtro Rápido por Módulo y Trazabilidad en Solicitudes de Reversa Contable'):
        p.text = (
            'E-7. Filtro Rápido por Módulo y Trazabilidad en Solicitudes de Reversa Contable   [COMPLETO]\n'
            'Implementado íntegramente en SolicitudesReversaPage.tsx (/contabilidad/reversas), solicitud-reversa-edicion.service.ts y contratistas.service.ts: '
            'soporta selección de 1..N proformas, Doble VºBº con PIN, desbloqueo puntual de assertPeriodoOperable para edición de Labor/Cuartel/Cantidad/Precio, '
            'actualización inmediata de Reportería en Árbol y registro completo de fotografía Antes / Después en Auditoría sin alterar asientos contables cerrados.'
        )

t0 = doc.tables[0]
t0.rows[0].cells[1].text = 'ERP Almahue · Versión Octubre–Noviembre 2026 (Cierre Técnico 100% ERP al 04/11/2026)'

t1 = doc.tables[1]
t1.rows[1].cells[0].text = '48 Puntos Base + 7 Correo\n55 Requerimientos Auditados'
t1.rows[1].cells[1].text = '54 Puntos\n98.2% Completos (100% ERP)'
t1.rows[1].cells[2].text = '0 Puntos\n0.0% Parciales'
t1.rows[1].cells[3].text = '1 Punto (Sistema Externo)\n0.0% Faltantes en ERP'

t2 = doc.tables[2]
rows_data = [
    (1, '12', '12', '0', '0', '100.0%'),
    (2, '11', '11', '0', '0', '100.0%'),
    (3, '7',  '7',  '0', '0', '100.0%'),
    (4, '5',  '5',  '0', '0', '100.0%'),
    (5, '3',  '3',  '0', '0', '100.0%'),
    (6, '6',  '6',  '0', '0', '100.0%'),
    (7, '4',  '3',  '0', '1 (Ext.)', '100.0% ERP'),
    (8, '48', '47', '0', '1 (Ext.)', '97.9% (100% ERP)'),
]
for idx, tot, comp, parc, falt, pct in rows_data:
    t2.rows[idx].cells[1].text = tot
    t2.rows[idx].cells[2].text = comp
    t2.rows[idx].cells[3].text = parc
    t2.rows[idx].cells[4].text = falt
    t2.rows[idx].cells[5].text = pct

doc.tables[31].rows[2].cells[1].text = (
    'COMPLETO. Implementado el ciclo completo de Reversa y Reapertura por excepción en período abierto y cerrado: '
    'selección de 1..N proformas, Doble VºBº (1º Contratistas + 2º Contabilidad con PIN), desbloqueo puntual en assertPeriodoOperable, '
    'edición de Labor, Cuartel (Centro de Costo), Cantidad y Precio Unitario, actualización de Reportería en Árbol (Labor -> CC -> Proforma), '
    'snapshot Antes / Después en Auditoría y endpoint POST contratistas/traspaso-cierre/:periodo/recentralizar.'
)

doc.tables[33].rows[2].cells[1].text = (
    'COMPLETO. OrdenesAplicacionPage.tsx implementa las 3 pestañas operativas: (1) Órdenes de Aplicación Agrícola con validación obligatoria de stock > 0, '
    'Cadena de Aprobación de Insumos con PIN y rebaja física de stock; (2) Mantenedor de Recetas de Packing (1 a 1 y plantilla Excel); '
    'y (3) Producción Mensual Packing conectada al Cierre de Bodega.'
)

doc.tables[37].rows[2].cells[1].text = (
    'COMPLETO. MovimientosBodegaPage incluye selector de Guía de Despacho Recibida original para devoluciones aún no facturadas, '
    'GuiasInsumosRecibidasPage.tsx cuenta con 2 pestañas (Guías Recibidas y Guías Emitidas DTE 52 de traslado interno a Packing) '
    'y CierreBodegaPage.tsx centraliza los consumos del mes (Consumo de materiales Campo + Materiales de exportación Packing) con pestaña de Parametrización.'
)

doc.tables[44].rows[2].cells[1].text = (
    'COMPLETO. Selector diferenciador de Rol (Todos / Proveedor / Productor) operativo en CuentasCorrientesPage.tsx, '
    'CompromisosAnticiposPage.tsx y NominasAgingPage.tsx.'
)

doc.tables[49].rows[2].cells[1].text = (
    'COMPLETO. Prevalidación de código de producto (<VlrCodigo>) desde el maestro en linea-detalle-dte.ts y canonical-builder.ts, '
    'previsualización PDF (DtePdfPreviewModal.tsx) y selector de Unidad de Medida por línea en ComercialPages.tsx.'
)

for dst in targets:
    doc.save(dst)
    print('Saved:', dst)
