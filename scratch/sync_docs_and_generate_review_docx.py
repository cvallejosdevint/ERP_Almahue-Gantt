import shutil
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. Sync Markdown files
src_oct_md = r'C:\Users\c\.gemini\antigravity\brain\bd2c2896-4eda-4509-a896-4ba61346224b\informe-consolidado-requerimientos-semana-2026-10-26.md'
shutil.copyfile(src_oct_md, r'E:\source\repos\Almahue\docs\reuniones\analisis\13-informe-consolidado-lunes-martes-miercoles-2026-10-28.md')
shutil.copyfile(src_oct_md, r'E:\source\repos\Almahue\docs\requerimientos\informe-consolidado-requerimientos-semana-2026-10-26.md')

src_nov_md = r'C:\Users\c\.gemini\antigravity\brain\bd2c2896-4eda-4509-a896-4ba61346224b\checklist-conectores-review-2026-11-03.md'
shutil.copyfile(src_nov_md, r'E:\source\repos\Almahue\docs\reuniones\analisis\15-checklist-conectores-y-definiciones-review-2026-11-03.md')

# 2. Generate Word document for Nov 3 Review Checklist & Connectors
doc = docx.Document()

for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

def add_title(text, subtitle):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text + '\n')
    r.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(26, 92, 46)
    r2 = p.add_run(subtitle)
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = RGBColor(90, 90, 90)

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(26, 92, 46)

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(30, 58, 95)

def add_bullet(bold_prefix, body):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Inches(0.2)
    r1 = p.add_run('• ' + bold_prefix + ': ')
    r1.bold = True
    r1.font.size = Pt(9.5)
    r2 = p.add_run(body)
    r2.font.size = Pt(9.5)

add_title(
    'ERP ALMAHUE · CHECKLIST, CONECTORES Y DEFINICIONES POST-REVIEW',
    'Reunión de Revisión de Cambios del Martes 03/11/2026 (AM + PM) · Estado: 14 / 14 Ítems Implementados (100% COMPLETO)'
)

# Metadata table
t_meta = doc.add_table(rows=4, cols=2)
t_meta.style = 'Table Grid'
meta_rows = [
    ('Grabaciones Origen', 'Screen Recording 2026-11-03 115116.mp4 (AM 00:42:16) y Screen Recording 2026-11-03 173934.mp4 (PM 02:38:24)'),
    ('Transcripciones Primarias', 'docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md (-am.md / -pm.md)'),
    ('Participantes Sala', 'Cliente Almahue: María José (MJ), Francisca (Fran), Lupe, Mario | Consultoría: Carlos, Sergio'),
    ('Estado de Implementación', '14 / 14 requerimientos y 7 / 7 conectores inter-módulos implementados y verificados en erp_back y erp_front (04/11/2026)'),
]
for idx, (k, v) in enumerate(meta_rows):
    t_meta.rows[idx].cells[0].text = k
    t_meta.rows[idx].cells[1].text = v

add_h1('1. Definiciones del Cliente Post-Review (03/11/2026)')

add_h2('1.1. Contratistas ↔ Libro de Compras ↔ Contabilidad')
add_bullet(
    'Dirección única de asociación Factura ↔ Proformas (PM [24:24], [01:09:12], [01:10:20], [02:14:37])',
    'MJ definió que la factura NO se asocia desde Contratistas, sino SIEMPRE desde Compras › Libro de Compras. Se eliminó el botón "Asociar factura" en Contratistas › Proformas; al asociar en Libro de Compras, el folio de la factura se refleja automáticamente en Proformas.'
)
add_bullet(
    'Dos pasos contables independientes (PM [23:52], [01:03:15], [02:14:27])',
    '(Paso 1) Al Traspaso y Cierre mensual de Contratistas entran TODAS las proformas aprobadas del mes (tengan o no factura asociada) generando Debe = Mano de Obra (6-1-01-01-002 agrupado por CC) vs Haber = Facturas por Recibir Contratistas (2-1-08-02-003 con Auxiliar RUT), mostrando tarjeta "Pendientes de asociación" y vista en Árbol (Labor -> CC -> Proforma). (Paso 2) En Libro de Compras, al contabilizar el DTE calzado al 100%, se netea Debe = Facturas por Recibir (2-1-08-02-003) + IVA vs Haber = Proveedores (2-1-01-01-001).'
)
add_bullet(
    'Eliminación de "Reabrir" y Efecto del Doble VºBº en Período Cerrado (AM [00:50], PM [28:13], [02:20:32–02:26:42])',
    'Un módulo cerrado nunca se reabre masivamente. Con período cerrado se solicita modificación sobre 1 o N proformas (Motivo + PIN) con Doble VºBº (1º Jefatura Contratistas + 2º Contabilidad). Con el período contable cerrado, la edición autorizada actualiza la Reportería de Gestión de Contratistas (labores/cuarteles) y el Log de Auditoría Antes/Después sin modificar el asiento contable histórico ya cerrado.'
)

add_h2('1.2. Insumos / Bodega ↔ Compras (OC Madre / Hijas / Guías) ↔ Contabilidad')
add_bullet(
    'Recepción en Bodega (Existencia) ≠ Cierre Mensual de Bodega (Consumo) (PM [01:31:16–01:49:42])',
    'MJ y Mario aclararon que la recepción de compras solo alimenta la Existencia (activo en bodega). El Cierre de Bodega mensual contabiliza exclusivamente lo CONSUMIDO en el mes.'
)
add_bullet(
    'Flujo A de Consumo — Agrícola / Campo (Órdenes de Aplicación) (PM [02:06:20–02:11:36])',
    'Rebaja stock agrícola validando stock > 0, pasa por Cadena de Aprobación del módulo Insumos y en el Cierre de Bodega mensual se centraliza contra "Consumo de materiales".'
)
add_bullet(
    'Flujo B de Consumo — Exportadora / Packing (Traspaso DTE 52 + Recetas + Producción) (PM [01:38:03–01:57:27])',
    'Los materiales de embalaje se traspasan desde Bodega Central (La Chamonata) a Bodega Packing emitiendo Guía de Despacho electrónica (DTE 52 traslado interno) desde el Libro de Guías de Insumos (2 pestañas: Guías Recibidas y Guías Emitidas). Con el mantenedor de Recetas (1 a 1 o Excel) y el registro de Producción Mensual de Packing se rebaja el stock de Bodega Packing y se centraliza contra "Materiales de exportación".'
)

add_h1('2. Mapa de Conectores entre Módulos (7 / 7 Operativos)')

t_conn = doc.add_table(rows=1, cols=4)
t_conn.style = 'Table Grid'
hdr = t_conn.rows[0].cells
hdr[0].text = 'ID'
hdr[1].text = 'Conector Inter-Módulos'
hdr[2].text = 'Estado'
hdr[3].text = 'Implementación en Código'

connectors = [
    ('C-1', 'Proformas (Contratistas) ↔ Asociar Factura (Libro de Compras)', 'COMPLETO',
     'Eliminado botón "Asociar factura" en Contratistas; cobertura 100% exacta y botón "Notificar diferencia al creador de la proforma" en AsociarOcRegistroCompraModal.tsx.'),
    ('C-2', 'Traspaso/Cierre (Contratistas) ↔ Provisión 2-1-08-02-003 (Contabilidad) ↔ Neteo (Libro de Compras)', 'COMPLETO',
     'getCierreTraspaso incluye todas las proformas aprobadas (ESTADOS_PROFORMA_TRASPASO); tarjeta "Pendientes de asociación", nombres completos de cuentas y vista árbol Labor -> CC -> Proforma.'),
    ('C-3', 'Reversa Proforma (Contratistas) ↔ Bandeja Doble VºBº (Contabilidad) ↔ Reportería y Auditoría', 'COMPLETO',
     'Selección de 1..N proformas, desbloqueo puntual de assertPeriodoOperable, edición de Labor/Cuartel/Cantidad/Precio y snapshot Antes/Después sin alterar asiento contable cerrado.'),
    ('C-4', 'OC Madre (Insumos) ↔ Recepción Guía ↔ OC Hijas (.1, .2) ↔ Libro de Compras', 'COMPLETO',
     'Filtro exclusivo tipo INSUMOS en recepción de guía; checkboxes múltiples para N OC Hijas en AsociarOcRegistroCompraModal.tsx; acordeón de hijas y doble columna de estado en OrdenesInsumosPage.tsx.'),
    ('C-5', 'Consumo Campo (Órdenes Aplicación) + Packing (Traspaso DTE 52 + Recetas + Producción) ↔ Cierre Bodega', 'COMPLETO',
     'Centro de 3 pestañas en OrdenesAplicacionPage.tsx, pestaña Guías Emitidas DTE 52 en GuiasInsumosRecibidasPage.tsx y Cierre de Bodega por Consumos en CierreBodegaPage.tsx.'),
    ('C-6', 'Activo Fijo ↔ Libro de Compras y Parametrización Contable', 'COMPLETO',
     'Tipo ACTIVO_FIJO en OrdenCompraWizardPage.tsx, vínculo en AltaActivoFijoDialog.tsx, pestaña "Activos fijos" en AsociarOcRegistroCompraModal.tsx y Parametrización en ActivoFijoPages.tsx.'),
    ('C-7', 'Perfiles de Usuario (Admin) ↔ Grupos y Escalas (Reglas de Aprobación)', 'COMPLETO',
     'Listado sin bloqueo por rol en WorkflowAprobacionesPage.tsx mostrando Rol + Grupo actual, y validación de secuencia estricta + Suplencia activa en workflowAprobacion.ts.'),
]

for cid, cname, ccurr, cgap in connectors:
    row = t_conn.add_row().cells
    row[0].text = cid
    row[1].text = cname
    row[2].text = ccurr
    row[3].text = cgap

add_h1('3. Checklist Detallado — Reunión 03/11/2026 (14 / 14 Completados)')

t_chk = doc.add_table(rows=1, cols=5)
t_chk.style = 'Table Grid'
ch = t_chk.rows[0].cells
ch[0].text = 'Estado / Código'
ch[1].text = 'Módulo'
ch[2].text = 'Requerimiento Implementado'
ch[3].text = 'Timestamp'
ch[4].text = 'Archivos de Código Actualizados'

chk_items = [
    ('CHK-01 [P0]', 'Contratistas', 'Eliminado botón "Asociar factura" y "Generar OC" de Contratistas › Proformas (asociación solo en Libro de Compras).', 'PM [01:10:20], [02:14:37]', 'ProformasContratistaNivel1Page.tsx, ContratistasPages.tsx'),
    ('CHK-02 [P0]', 'Contratistas', 'Filtro de período por defecto en "Todos" y ocultar "Sin envío" si la proforma aún no está aprobada.', 'AM [05:49], PM [11:46]', 'ProformasContratistaNivel1Page.tsx'),
    ('CHK-03 [P0]', 'Contratistas / Contab.', 'Traspaso y Cierre: incluir todas las aprobadas, tarjeta "Pendientes de asociación", nombre de cuenta y vista en árbol (Labor -> CC -> Proforma).', 'PM [22:28], [39:07], [01:03:15]', 'contratistas.service.ts, ContratistasPages.tsx, TraspasoContratistasResumenPanel.tsx'),
    ('CHK-04 [P0]', 'Contratistas / Contab.', 'Reapertura / Reversa en Período Cerrado: desbloqueo puntual de assertPeriodoOperable, multi-proforma, Reportería Árbol y Auditoría Antes/Después sin tocar asiento cerrado.', 'AM [00:35], PM [27:36], [02:20:32]', 'contratistas.service.ts, solicitud-reversa-edicion.service.ts, SolicitudesReversaPage.tsx'),
    ('CHK-05 [P0]', 'Compras', 'Modal Asociar Factura: quitada pestaña "Guías recibidas", agregada "Activos fijos", calce 100% en Proformas y checkboxes para múltiples OC Hijas.', 'PM [16:50], [20:11], [01:06:17], [02:02:32]', 'AsociarOcRegistroCompraModal.tsx'),
    ('CHK-06 [P1]', 'Compras', 'Doble etiqueta en documento asociado (Proforma/OC + Contabilizada/Pendiente) y botón de notificación de diferencia.', 'PM [14:17], [26:06]', 'ComprasPages.tsx, AsociarOcRegistroCompraModal.tsx'),
    ('CHK-07 [P0]', 'Insumos / Bodega', 'Recepción de Guías: filtrado exclusivo de OCs tipo INSUMOS, eliminado botón "Crear producto" y modal independiente "Pedir creación".', 'PM [01:17:55–01:20:27]', 'insumos.service.ts, GuiasInsumosRecibidasPage.tsx'),
    ('CHK-08 [P1]', 'Insumos / Bodega', 'Ingreso Manual de Guía: selector de proveedor con búsqueda por RUT y campos de Tipo de Despacho / Traslado.', 'PM [01:14:39]', 'GuiasInsumosRecibidasPage.tsx'),
    ('CHK-09 [P1]', 'Insumos / Bodega', 'Grilla Órdenes de Insumos: OC Hijas (.1, .2) en acordeón bajo OC Madre y columnas separadas "Estado Aprobación" y "Estado Recepción".', 'PM [01:23:43–01:30:54]', 'OrdenesInsumosPage.tsx'),
    ('CHK-10 [P1]', 'Insumos / Bodega', 'CRUD de Órdenes de Aplicación (Consumo Campo) con validación stock > 0 y Cadena de Aprobación de Insumos.', 'PM [01:34:01], [02:06:20]', 'OrdenesAplicacionPage.tsx'),
    ('CHK-11 [P1]', 'Insumos / Packing', 'Libro de Guías con 2 pestañas (Recibidas / Emitidas DTE 52 por traspaso a Bodega Packing), Mantenedor de Recetas (1 a 1 y Excel) y Producción Mensual.', 'PM [01:38:03–02:01:09]', 'GuiasInsumosRecibidasPage.tsx, OrdenesAplicacionPage.tsx'),
    ('CHK-12 [P1]', 'Insumos / Todos', 'Cierre Mensual de Bodega centrado en Consumos (Aplicación Campo + Producción Packing), sin botón "Reabrir" y pestaña Parametrización por módulo.', 'PM [01:31:16], [02:10:00]', 'CierreBodegaPage.tsx, ParametrizacionContratistasPage.tsx, ActivoFijoPages.tsx'),
    ('CHK-13 [P0]', 'Admin / Aprobaciones', 'Permitir agregar cualquier perfil de usuario a un Grupo de Aprobación y mostrar Rol + Grupo actual en el selector.', 'PM [01:24–07:47]', 'WorkflowAprobacionesPage.tsx'),
    ('CHK-14 [P1]', 'Admin / Aprobaciones', 'Garantizar secuencia estricta de firma en Bandejas de Aprobación y salto automático por Suplencia activa.', 'PM [52:30–54:28]', 'workflowAprobacion.ts'),
]

for code, mod, desc, ts, files in chk_items:
    r = t_chk.add_row().cells
    r[0].text = '☑ ' + code + ' (COMPLETO)'
    r[1].text = mod
    r[2].text = desc
    r[3].text = ts
    r[4].text = files

out_paths = [
    r'C:\Users\c\Desktop\ERP-Almahue-Checklist-y-Conectores-Review-2026-11-03.docx',
    r'E:\source\repos\Almahue\docs\reuniones\analisis\15-checklist-conectores-y-definiciones-review-2026-11-03.docx',
]
for p in out_paths:
    doc.save(p)
    print('Saved Review Checklist docx:', p)
