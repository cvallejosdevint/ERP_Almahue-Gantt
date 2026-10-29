import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_monday_docx(output_path):
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    c_navy = RGBColor(27, 54, 93)       # #1B365D
    c_blue = RGBColor(30, 58, 138)      # #1E3A8A
    c_slate = RGBColor(71, 85, 105)     # #475569
    c_charcoal = RGBColor(30, 41, 59)   # #1E293B
    c_green = RGBColor(22, 101, 52)     # #166534
    c_amber = RGBColor(133, 77, 14)     # #854D0E
    c_red = RGBColor(153, 27, 27)       # #991B1B

    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("ERP ALMAHUE · AUDITORÍA DE REQUERIMIENTOS DÍA LUNES 26/10/2026")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = c_navy

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Evidencia Cruzada: Apuntes Consultor ('revision en cliente.txt') · Transcripción AM/PM · Skills de Cursor · Base de Código")
    r_sub.font.name = "Segoe UI"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = c_slate

    # Summary Table
    meta_table = doc.add_table(rows=3, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    set_table_borders(meta_table, "E2E8F0", "4", "single")

    meta_rows = [
        ("Sesión Evaluada", "Lunes 26/10/2026: Mañana (12.33.m4a - 01:24:40) y Tarde reparada (15.20 REPARADO.m4a - ~01:54:00)"),
        ("Puntos Auditados", "38 Requerimientos totales: 23 Completos (60.5%) · 15 Parciales (39.5%) · 0 Faltantes (0.0%)"),
        ("Actores Principales", "María Jesús (MJ), Lupe, Fran, Mario, Equipo Consultor"),
    ]

    for idx, (label, val) in enumerate(meta_rows):
        row = meta_table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.9)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.name = "Segoe UI"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = c_navy

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(9)
        r1.font.color.rgb = c_charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Matrix Table for Monday
    p_mat = doc.add_paragraph()
    r_mat = p_mat.add_run("Matriz de Cumplimiento por Bloque (Día Lunes)")
    r_mat.font.name = "Segoe UI"
    r_mat.font.size = Pt(12)
    r_mat.font.bold = True
    r_mat.font.color.rgb = c_navy

    tbl_mon = doc.add_table(rows=8, cols=5)
    tbl_mon.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mon.autofit = False
    set_table_borders(tbl_mon, "E2E8F0", "4", "single")

    hdrs = ["Categoría / Bloque", "Total", "Completo", "Parcial", "% Avance"]
    w_cols = [Inches(3.2), Inches(0.9), Inches(1.0), Inches(1.0), Inches(1.0)]

    for i, h in enumerate(hdrs):
        c = tbl_mon.rows[0].cells[i]
        c.width = w_cols[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 70, 70, 80, 80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if i == 0 else WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    rows_mon = [
        ("Administración y Usuarios (A-*)", "3", "1", "2", "33.3%"),
        ("Parametrización y Plan de Cuentas (P-*)", "9", "6", "3", "66.7%"),
        ("Compras y Órdenes de Compra (C-*)", "5", "4", "1", "80.0%"),
        ("Contabilidad y Reportes Financieros (K-*)", "13", "7", "6", "53.8%"),
        ("Contratistas Agrícolas (CTR-*)", "7", "4", "3", "57.1%"),
        ("Tesorería y Bancos (TES-*)", "1", "1", "0", "100.0%"),
        ("TOTAL DÍA LUNES 26/10", "38", "23", "15", "60.5%"),
    ]

    for idx, data in enumerate(rows_mon):
        row = tbl_mon.rows[idx + 1]
        is_tot = (idx == len(rows_mon) - 1)
        bg = "F1F5F9" if is_tot else ("FFFFFF" if idx % 2 == 0 else "F8FAFC")

        for c_i, val in enumerate(data):
            cell = row.cells[c_i]
            cell.width = w_cols[c_i]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 50, 50, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_i == 0 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Segoe UI"
            r.font.size = Pt(9)
            if is_tot:
                r.font.bold = True
                r.font.color.rgb = c_navy
            else:
                if c_i == 2:
                    r.font.bold = True
                    r.font.color.rgb = c_green
                elif c_i == 3:
                    r.font.bold = True
                    r.font.color.rgb = c_amber
                else:
                    r.font.color.rgb = c_charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Detailed Table of Monday Items
    p_det = doc.add_paragraph()
    r_det = p_det.add_run("Detalle Completo de Requerimientos del Día Lunes (38 Puntos)")
    r_det.font.name = "Segoe UI"
    r_det.font.size = Pt(12)
    r_det.font.bold = True
    r_det.font.color.rgb = c_navy

    tbl_items = doc.add_table(rows=39, cols=5)
    tbl_items.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_items.autofit = False
    set_table_borders(tbl_items, "E2E8F0", "4", "single")

    hdrs_it = ["Código", "Requerimiento / Regla de Negocio", "Fuente / Minuto", "Estado", "Detalle Código / Brecha"]
    w_it = [Inches(0.8), Inches(2.2), Inches(1.3), Inches(1.0), Inches(1.8)]

    for i, h in enumerate(hdrs_it):
        c = tbl_items.rows[0].cells[i]
        c.width = w_it[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 60, 60, 60, 60)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 2, 3] else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name = "Segoe UI"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    items_data = [
        ("A-1", "Selector 2 empresas al crear usuario", "Apuntes sala", "COMPLETO", "EmpresaSelector.tsx listo"),
        ("A-2", "Historial parametrización antes/después", "Tarde [48:40]", "PARCIAL", "Piloto contratistas/AF listo"),
        ("A-3", "Solicitud apertura periodo + reverso", "Tarde [01:07]", "PARCIAL", "Reverso asiento listo; UI bandeja pend"),
        ("P-1", "Plan cuentas N:N dimensiones (3 col)", "Mañana [22:15]", "COMPLETO", "CuentaAsociadosPanel.tsx listo"),
        ("P-2", "Contador cuentas en catálogos CC/Elem", "Mañana [29:17]", "COMPLETO", "Columna cuentasAsociadasCount lista"),
        ("P-3", "Bancos multi-cuenta con moneda y tipo", "Apuntes sala", "COMPLETO", "CuentasCorrientesPage.tsx listo"),
        ("P-4", "Historial en catálogo parametrizaciones", "Apuntes P-4", "PARCIAL", "Back persiste; UI fila pendiente"),
        ("P-5", "Boleta honorarios 1001-1003 + regla notaría", "Apuntes P-5", "PARCIAL", "Tipos listos; control rendición pend"),
        ("P-6", "Nota cobro gasto directo (wizard OC)", "Apuntes P-6", "COMPLETO", "NotasCobroPage.tsx listo"),
        ("P-7", "OPB embarcador (compensación terceros)", "Apuntes P-7", "PARCIAL", "UI base lista; import Excel pend"),
        ("P-8", "Matriz plan cuentas scroll bidireccional", "Apuntes P-8", "COMPLETO", "PlanCuentasPage vista matriz lista"),
        ("P-9", "Eliminación planta; variedad opcional", "Tarde [03:39]", "COMPLETO", "Formularios limpios de planta"),
        ("C-1", "Jerarquía OC: Cuenta > CC > Elemento", "Mañana [44:04]", "COMPLETO", "OrdenCompraWizardPage.tsx listo"),
        ("C-2", "Solicitar admin CC/Elemento no ligado", "Mañana [44:13]", "COMPLETO", "Modal solicitud admin en OC listo"),
        ("C-3", "Múltiples líneas de imputación en OC", "Mañana [47:25]", "COMPLETO", "Líneas múltiples soportadas"),
        ("C-4", "Detalle OC estilo árbol / flujo caja", "Mañana [55:17]", "PARCIAL", "OcOrigenCadena.tsx; árbol pend"),
        ("C-5", "PDF OC proveedor sin dimensiones", "Mañana [50:24]", "COMPLETO", "compras-oc-helpers.ts listo"),
        ("K-1", "Tipo de cambio en pesos al contabilizar", "Apuntes K-1", "COMPLETO", "Asiento almacena CLP y TC"),
        ("K-2", "Motivo obligatorio cierre/apertura mes", "Apuntes K-2", "COMPLETO", "PeriodosContablesPage.tsx listo"),
        ("K-3", "Identificador asiento nomenclatura tipo", "Mañana [09:59]", "COMPLETO", "tipo-comprobante.ts prefijos"),
        ("K-4", "Detalle asiento 3 col y edición glosa", "Apuntes K-4", "COMPLETO", "AsientosPage.tsx ajustado"),
        ("K-5", "Adjuntar Registro Compras en asiento", "Apuntes K-5", "PARCIAL", "Back soporta; dropzone modal pend"),
        ("K-6", "Comprobante manual pide tipo; módulo auto", "Apuntes K-6", "COMPLETO", "Modal nuevo comprobante listo"),
        ("K-7", "Validación histórica contable con Mario", "Apuntes K-7", "PARCIAL", "Pendiente entrega data Almahue"),
        ("K-8", "Comprobante manual pasa a CONTABILIZADO", "Apuntes K-8", "COMPLETO", "Guardado directo contabilizado"),
        ("K-9", "TC manual con alerta a administrador", "Apuntes K-9", "COMPLETO", "RevaluacionTcModal.tsx listo"),
        ("K-10", "Presupuesto: alerta % en totalizados", "Apuntes K-10", "PARCIAL", "Módulo listo; umbral visual pend"),
        ("K-11", "CC agrupados departamento + totalizados", "Apuntes K-11", "PARCIAL", "Agrupación básica; tarjetas pend"),
        ("K-12", "Mayor/Diario filtros mes/año (Todos=año)", "Apuntes K-12", "COMPLETO", "LibroDiarioMayorPages.tsx listo"),
        ("K-13", "Mayor: ancho expandido selector cuentas", "Apuntes K-13", "COMPLETO", "Layout expandido sin truncar"),
        ("K-14", "Mayor: arrastre de saldo interanual", "Apuntes K-14", "COMPLETO", "Saldos acumulados persistentes"),
        ("K-15", "Balance 8 columnas acumulativo anual", "Mañana [00:19]", "COMPLETO", "Balance8ColumnasPage.tsx listo"),
        ("K-16", "Estado Resultados mensual (solo mes)", "Mañana [00:19]", "COMPLETO", "EstadosFinancierosPage.tsx listo"),
        ("K-17", "Situación financiera multianual", "Apuntes K-17", "PARCIAL", "Año actual listo; comparativo pend"),
        ("K-18", "Utilidad ejercicio a acumulado al 31/12", "Mañana [00:19]", "PARCIAL", "Cuadre verif; asiento auto pend"),
        ("K-19", "Validación cuadre vs balances MJ", "Mañana [21:18]", "COMPLETO", "Verificado con archivos MJ"),
        ("K-20", "Carga masiva restrictiva tipo Agrosoft", "Mañana [06:55]", "PARCIAL", "Importador base; fail-closed pend"),
        ("CTR-1", "Módulo Contratistas completo", "Tarde entera", "COMPLETO", "features/contratistas/ estructurado"),
    ]

    for idx, (code, title, src, st, ev) in enumerate(items_data):
        row = tbl_items.rows[idx + 1]
        bg = "FFFFFF" if idx % 2 == 0 else "F8FAFC"
        row_vals = [code, title, src, st, ev]

        for c_i, val in enumerate(row_vals):
            c = row.cells[c_i]
            c.width = w_it[c_i]
            set_cell_background(c, bg)
            set_cell_margins(c, 40, 40, 50, 50)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_i in [0, 2, 3] else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Segoe UI"
            r.font.size = Pt(8)
            if c_i == 0:
                r.font.bold = True
                r.font.color.rgb = c_navy
            elif c_i == 3:
                r.font.bold = True
                r.font.color.rgb = c_green if val == "COMPLETO" else (c_amber if val == "PARCIAL" else c_red)
            else:
                r.font.color.rgb = c_charcoal

    doc.save(output_path)
    print(f"Monday Document saved successfully: {output_path}")

if __name__ == "__main__":
    out_mon1 = "docs/reuniones/analisis/14-informe-auditoria-lunes-2026-10-26.docx"
    build_monday_docx(out_mon1)

    desktop = os.path.expanduser(r"~\Desktop")
    if os.path.exists(desktop):
        out_mon2 = os.path.join(desktop, "ERP-Almahue-Auditoria-Lunes-2026-10-26.docx")
        build_monday_docx(out_mon2)

