import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
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

def build_docx(output_path):
    doc = Document()

    # Margins 0.7 inches for executive layout
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    # Palette
    c_navy = RGBColor(27, 54, 93)       # #1B365D Primary Corporate
    c_blue = RGBColor(30, 58, 138)      # #1E3A8A Blue Dark
    c_slate = RGBColor(71, 85, 105)     # #475569 Slate Subtitles
    c_charcoal = RGBColor(30, 41, 59)   # #1E293B Dark Text
    c_green = RGBColor(22, 101, 52)     # #166534 Success Dark
    c_amber = RGBColor(133, 77, 14)     # #854D0E Warning Dark
    c_red = RGBColor(153, 27, 27)       # #991B1B Danger Dark

    # Title Banner
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("ERP ALMAHUE · INFORME CONSOLIDADO DE REQUERIMIENTOS Y ESTADO")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = c_navy

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Auditoría Técnica y Operativa de Sesiones · Lunes 26, Martes 27 y Miércoles 28 de Octubre de 2026\nContraste Integral: Transcripciones Whisper large-v3 · Minutas de Sala · Apuntes de Consultoría · Base de Código")
    r_sub.font.name = "Segoe UI"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = c_slate

    # Metadata Table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    set_table_borders(meta_table, "E2E8F0", "4", "single")

    meta_rows = [
        ("Proyecto y Versión", "ERP Almahue · Versión Octubre 2026 (Semana 15 - Pre-Temporada Alta)"),
        ("Fuentes Primarias Analizadas", "5 Sesiones: Lunes 26 (AM 01:24:40 + PM 01:54:00) | Martes 27 (AM 01:18:10 + PM 01:47:50) | Miércoles 28 (03:04:06)"),
        ("Participantes Clave", "Cliente Almahue: María Jesús (MJ), Lupe, Fran, Mario, José Tomás, Agustín | Consultoría: Carlos V., Sergio"),
        ("Entornos de Validación", "Local Front: http://localhost:5174 | Local API: http://localhost:3001 | Servidor Prod: http://45.7.229.46/almahue-erp/"),
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
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(label)
        r0.font.name = "Segoe UI"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = c_navy

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(9)
        r1.font.color.rgb = c_charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 1. Resumen Ejecutivo
    p_h1 = doc.add_paragraph()
    p_h1.paragraph_format.space_before = Pt(12)
    p_h1.paragraph_format.space_after = Pt(4)
    p_h1.paragraph_format.keep_with_next = True
    r_h1 = p_h1.add_run("1. Resumen Ejecutivo y Matriz Global de Estado")
    r_h1.font.name = "Segoe UI"
    r_h1.font.size = Pt(13)
    r_h1.font.bold = True
    r_h1.font.color.rgb = c_navy

    p_exec = doc.add_paragraph()
    p_exec.paragraph_format.space_after = Pt(8)
    r_exec = p_exec.add_run(
        "A lo largo de las 5 sesiones de trabajo presenciales y remotas de los días 26, 27 y 28 de octubre de 2026, "
        "se consolidaron un total de 44 requerimientos y acuerdos operativos distribuidos en 7 módulos funcionales. "
        "Cada requerimiento ha sido contrastado contra las transcripciones oficiales generadas con Whisper large-v3, "
        "las minutas de sala, los apuntes originales de consultoría ('revision en cliente.txt') y la base de código "
        "actualmente desplegada en el servidor de pruebas y producción."
    )
    r_exec.font.name = "Segoe UI"
    r_exec.font.size = Pt(9.5)
    r_exec.font.color.rgb = c_charcoal

    # KPI Summary Cards (Table with 4 columns)
    kpi_table = doc.add_table(rows=2, cols=4)
    kpi_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    kpi_table.autofit = False
    set_table_borders(kpi_table, "CBD5E1", "6", "single")

    kpi_data = [
        ("TOTAL AUDITADO", "44 Puntos", "100% Requerimientos", "F1F5F9", c_navy),
        ("COMPLETOS", "23 Puntos", "52.3% Operativos", "DCFCE7", c_green),
        ("PARCIALES", "16 Puntos", "36.4% En Desarrollo", "FEF9C3", c_amber),
        ("FALTANTES", "5 Puntos", "11.4% Por Iniciar", "FEE2E2", c_red),
    ]

    col_widths = [Inches(1.77), Inches(1.77), Inches(1.77), Inches(1.77)]
    for col_idx, (title, count_val, sub_val, bg_hex, text_color) in enumerate(kpi_data):
        c_top = kpi_table.rows[0].cells[col_idx]
        c_bot = kpi_table.rows[1].cells[col_idx]
        c_top.width = col_widths[col_idx]
        c_bot.width = col_widths[col_idx]

        set_cell_background(c_top, bg_hex)
        set_cell_background(c_bot, bg_hex)
        set_cell_margins(c_top, 80, 20, 80, 80)
        set_cell_margins(c_bot, 20, 80, 80, 80)

        p_t = c_top.paragraphs[0]
        p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_t.paragraph_format.space_after = Pt(2)
        r_t = p_t.add_run(title)
        r_t.font.name = "Segoe UI"
        r_t.font.size = Pt(8.5)
        r_t.font.bold = True
        r_t.font.color.rgb = text_color

        p_b = c_bot.paragraphs[0]
        p_b.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_b.paragraph_format.space_after = Pt(0)
        r_b1 = p_b.add_run(f"{count_val}\n")
        r_b1.font.name = "Segoe UI"
        r_b1.font.size = Pt(13)
        r_b1.font.bold = True
        r_b1.font.color.rgb = text_color

        r_b2 = p_b.add_run(sub_val)
        r_b2.font.name = "Segoe UI"
        r_b2.font.size = Pt(8)
        r_b2.font.color.rgb = text_color

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Matrix Table by Module
    p_mat_h = doc.add_paragraph()
    p_mat_h.paragraph_format.space_before = Pt(8)
    p_mat_h.paragraph_format.space_after = Pt(4)
    r_mat_h = p_mat_h.add_run("Matriz de Estado por Módulo Operativo")
    r_mat_h.font.name = "Segoe UI"
    r_mat_h.font.size = Pt(11)
    r_mat_h.font.bold = True
    r_mat_h.font.color.rgb = c_navy

    mod_table = doc.add_table(rows=9, cols=6)
    mod_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    mod_table.autofit = False
    set_table_borders(mod_table, "E2E8F0", "4", "single")

    headers = ["Módulo Operativo", "Total", "Completo", "Parcial", "Faltante", "% Avance"]
    widths = [Inches(2.6), Inches(0.8), Inches(0.9), Inches(0.9), Inches(0.9), Inches(1.0)]

    hdr_row = mod_table.rows[0]
    for i, h in enumerate(headers):
        c = hdr_row.cells[i]
        c.width = widths[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 80, 80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if i == 0 else WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    matrix_rows = [
        ("1. Contabilidad, Plan de Cuentas y Reportes", "12", "6", "6", "0", "50.0%"),
        ("2. Compras, Proveedores y Notas de Cobro", "11", "5", "5", "1", "45.5%"),
        ("3. Contratistas Agrícolas", "7", "4", "3", "0", "57.1%"),
        ("4. Insumos y Bodega", "5", "3", "2", "0", "60.0%"),
        ("5. Activos Fijos", "3", "1", "0", "2", "33.3%"),
        ("6. Tesorería, Bancos y Contrapartes", "6", "3", "3", "0", "50.0%"),
        ("7. Comercial, Packing y Comex", "4", "1", "1", "2", "25.0%"),
        ("TOTAL GENERAL CONSOLIDADO", "44", "23", "16", "5", "52.3%"),
    ]

    for row_idx, data in enumerate(matrix_rows):
        row = mod_table.rows[row_idx + 1]
        is_total = (row_idx == len(matrix_rows) - 1)
        bg = "F1F5F9" if is_total else ("FFFFFF" if row_idx % 2 == 0 else "F8FAFC")

        for col_idx, val in enumerate(data):
            cell = row.cells[col_idx]
            cell.width = widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Segoe UI"
            r.font.size = Pt(9)
            if is_total:
                r.font.bold = True
                r.font.color.rgb = c_navy
            else:
                if col_idx == 2:
                    r.font.bold = True
                    r.font.color.rgb = c_green
                elif col_idx == 3:
                    r.font.bold = True
                    r.font.color.rgb = c_amber
                elif col_idx == 4 and val != "0":
                    r.font.bold = True
                    r.font.color.rgb = c_red
                else:
                    r.font.color.rgb = c_charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Helper function for Section headers
    def add_module_heading(title, count_info):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r1 = p.add_run(title)
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = c_navy

        r2 = p.add_run(f"  ·  [{count_info}]")
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(9.5)
        r2.font.italic = True
        r2.font.color.rgb = c_slate

    # Helper function for Item Cards
    def add_requirement_card(code_title, status, origin, desc, code_evidence):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True

        r_code = p.add_run(f"{code_title}  ")
        r_code.font.name = "Segoe UI"
        r_code.font.size = Pt(10.5)
        r_code.font.bold = True
        r_code.font.color.rgb = c_charcoal

        # Badge run
        r_badge = p.add_run(f" [{status}] ")
        r_badge.font.name = "Segoe UI"
        r_badge.font.size = Pt(9)
        r_badge.font.bold = True
        if status == "COMPLETO":
            r_badge.font.color.rgb = c_green
        elif status == "PARCIAL":
            r_badge.font.color.rgb = c_amber
        else:
            r_badge.font.color.rgb = c_red

        # Card table
        tbl = doc.add_table(rows=3, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        set_table_borders(tbl, "E2E8F0", "4", "single")

        card_rows = [
            ("Origen / Timestamps", origin),
            ("Descripción Operativa", desc),
            ("Estado en Código / Brecha", code_evidence),
        ]

        w_lbl = Inches(1.8)
        w_val = Inches(5.3)

        for r_i, (lbl, text_val) in enumerate(card_rows):
            row = tbl.rows[r_i]
            c_l, c_v = row.cells[0], row.cells[1]
            c_l.width = w_lbl
            c_v.width = w_val

            bg_col = "F8FAFC" if r_i % 2 == 0 else "FFFFFF"
            set_cell_background(c_l, "F1F5F9")
            set_cell_background(c_v, bg_col)
            set_cell_margins(c_l, 40, 40, 80, 80)
            set_cell_margins(c_v, 40, 40, 80, 80)

            pl = c_l.paragraphs[0]
            pl.paragraph_format.space_after = Pt(0)
            rl = pl.add_run(lbl)
            rl.font.name = "Segoe UI"
            rl.font.size = Pt(8.5)
            rl.font.bold = True
            rl.font.color.rgb = c_navy

            pv = c_v.paragraphs[0]
            pv.paragraph_format.space_after = Pt(0)
            rv = pv.add_run(text_val)
            rv.font.name = "Segoe UI"
            rv.font.size = Pt(8.5)
            rv.font.color.rgb = c_charcoal

    # ==========================================
    # 2. DETALLE DE REQUERIMIENTOS POR MÓDULO
    # ==========================================
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(16)
    p_sec2.paragraph_format.space_after = Pt(4)
    p_sec2.paragraph_format.keep_with_next = True
    r_sec2 = p_sec2.add_run("2. Detalle Exhaustivo de Requerimientos por Módulo (44 Puntos)")
    r_sec2.font.name = "Segoe UI"
    r_sec2.font.size = Pt(14)
    r_sec2.font.bold = True
    r_sec2.font.color.rgb = c_navy

    # MÓDULO 1
    add_module_heading("Módulo 1: Contabilidad, Plan de Cuentas y Reportes Financieros", "12 Puntos · 6 Completos · 6 Parciales · 0 Faltantes")

    add_requirement_card(
        "1.1 Selector Multi-Empresa al Crear Usuarios (A-1)", "COMPLETO",
        "Lunes 26/10 apuntes de sala 'revision en cliente.txt'.",
        "Los usuarios asignados a dos razones sociales deben poder seleccionar y operar ambas empresas con aislamiento estricto de datos en compras, ventas y contabilidad.",
        "Implementado y verificado en EmpresaSelector.tsx y en el contexto de sesión JWT (empresaId / empresasHabilitadas)."
    )

    add_requirement_card(
        "1.2 Asociación N:N de Dimensiones por Cuenta (Plan de Cuentas) (P-1)", "COMPLETO",
        "Lunes AM [22:15 - 25:59], aprobado por MJ; validado Martes AM [01:03].",
        "Por cada cuenta contable imputable, se asocian de forma independiente múltiples Centros de Costo, Elementos de Gasto y Áreas de Negocio. Al usar la cuenta en OC, asientos o importaciones, solo se ofrecen las dimensiones vinculadas. Pantalla con 3 columnas con scroll independiente, buscadores y checkboxes anclados arriba con contador.",
        "Implementado en CuentaAsociadosPanel.tsx y PlanCuentasPage.tsx. Validado con 3 columnas, búsqueda en tiempo real, anclaje superior de checks y contador dinámico de asignados."
    )

    add_requirement_card(
        "1.3 Matriz de Plan de Cuentas con Scroll Bidireccional (P-8)", "COMPLETO",
        "Lunes apuntes P-8.",
        "Lista maestra de cuentas con scroll vertical fijo en códigos y nombres; a la derecha, rejilla de permisos y dimensiones con scroll horizontal y vertical sin perder de vista la fila.",
        "Implementado en la vista Matriz de PlanCuentasPage.tsx."
    )

    add_requirement_card(
        "1.4 Balance de 8 Columnas Acumulativo Anual (K-15)", "COMPLETO",
        "Lunes AM [00:19], Martes PM [04:20 - 09:20].",
        "Reporte oficial con Sumas (Débitos/Créditos), Saldos (Deudor/Acreedor), Inventario (Activo/Pasivo) y Resultados (Pérdida/Ganancia). El cálculo del Resultado del Ejercicio cuadra exactamente entre Ganancia - Pérdida e Inventario Activo - Pasivo. Acumulativo desde el 1 de enero hasta la fecha de corte.",
        "Implementado en Balance8ColumnasPage.tsx con las 8 columnas requeridas, cálculo dinámico de saldos y cuadre del resultado del ejercicio."
    )

    add_requirement_card(
        "1.5 Estado de Resultados Mensual vs Situación Financiera al 31/12 (K-16, K-18, K-19)", "COMPLETO",
        "Lunes AM [00:19 - 02:03].",
        "El Estado de Resultados mensual muestra exclusivamente los movimientos del mes consultado. Al 31 de diciembre, la utilidad del ejercicio se traspasa al Estado de Situación Financiera como Resultado Acumulado, donde deben coexistir ambos conceptos para cuadre formal (validado contra balances de MJ ene-2026 / dic-2025).",
        "Implementado en EstadosFinancierosPage.tsx y CierreAnualModal.tsx. Incluye alternancia entre movimientos del mes y acumulado anual con cálculo dinámico de pérdidas y ganancias del periodo, coexistencia formal de Resultado Acumulado (2-4-04-02-001) y Resultado del Ejercicio (2-4-04-02-004) en Situación Financiera para cuadre patrimonial formal, y comando de Asiento de Cierre Anual automático al 31/12 con previsualización en 3 columnas (Ingresos, Gastos, Patrimonio), comprobante cuadrado y persistencia en periodo diciembre."
    )

    add_requirement_card(
        "1.6 Carga Masiva Restrictiva Tipo Agrosoft (K-20)", "PARCIAL",
        "Lunes AM [06:55 - 17:09].",
        "Importador Excel fail-closed. Campos: correlativo (líneas de comprobante), tipo de comprobante, fecha, periodo contable, tipo de cambio, cuenta contable, dimensiones (CC, elemento, área). Si una cuenta exige CC y no viene en la fila, rechazar el lote completo. Validación previa de fecha vs periodo y Debe = Haber en CLP y USD.",
        "Existe importador contable base; falta implementar el validador estricto fail-closed específico para el formato Agrosoft y reporte detallado de filas erróneas."
    )

    add_requirement_card(
        "1.7 Tipos de Comprobante Contable y Nomenclatura (K-3, K-6)", "COMPLETO",
        "Lunes AM / Apuntes K-3, K-6, K-8.",
        "Clasificación: APERTURA, EGRESOS, INGRESOS, PROVEEDORES, TRASPASOS, VENTAS. Al crear manual solicita tipo; si viene de módulo operativo es automático. Pasa directo a CONTABILIZADO al guardar.",
        "Implementado en tipo-comprobante.ts y en la persistencia de asientos con prefijos por origen."
    )

    add_requirement_card(
        "1.8 Detalle de Asiento en 3 Columnas, Glosas y Adjuntos (K-4, K-5)", "COMPLETO",
        "Lunes apuntes K-4, K-5.",
        "Grilla balanceada en tres columnas, regularización de botones de edición de glosa en cabecera y líneas, y soporte de adjuntos de Registro de Compras (RC).",
        "Implementado en AsientosPage.tsx con grilla balanceada en 3 columnas, edición de glosa en cabecera y por línea (patch /asientos/:id/lineas/:index/glosa), y panel lateral de gestión de adjuntos con subida y visualización de respaldos de Registro de Compras (RC)."
    )

    add_requirement_card(
        "1.9 Protocolo de Reversas y Comprobantes de Ajuste (Mes Abierto vs Cerrado) (A-3)", "COMPLETO",
        "Lunes PM [01:07], Martes AM [48:10 - 01:06:40].",
        "Mes Abierto: Se desvincula la factura en compras, el documento pasa a REVERSADA, Admin Concepto habilita edición con PIN, re-aprueba y re-asocia. Mes Cerrado: Prohibido desarmar la centralización. Se genera un Comprobante de Ajuste / Traspaso puntual con doble visto bueno (Jefatura de Área + Contabilidad).",
        "Implementado en AsientoReversoModal.tsx, ComprobanteAjusteModal.tsx y asiento-reverso.ts. En mes abierto desvincula la factura y pasa a REVERSADA con autorización PIN de AdminConcepto; en mes cerrado bloquea la desvinculación y exige Comprobante de Ajuste/Traspaso puntual con doble visto bueno (Jefatura de Área + Contabilidad)."
    )

    add_requirement_card(
        "1.10 Auditoría e Historial Distribuida por Módulo (A-2)", "COMPLETO",
        "Lunes PM [48:40], Martes PM [00:00 - 02:40].",
        "Pestañas locales de auditoría en Contabilidad, Contratistas, Insumos y Activos Fijos con comparativa antes/después legible para Jefatura y Contabilidad (sin metadatos técnicos visibles al usuario).",
        "Implementado en AuditoriaContabilidadPage.tsx, AuditoriaContratistasPage.tsx y ActivoFijoHistorialPanel.tsx con comparativa antes/después estructurada y legible para Jefatura y Contabilidad, sin volcado técnico de metadatos."
    )

    add_requirement_card(
        "1.11 Libro Mayor y Diario: Filtros de Periodo y Arrastre Interanual (K-12, K-13, K-14)", "COMPLETO",
        "Lunes apuntes K-12, K-13, K-14.",
        "Filtros mes y año; opción 'Todos' restringe al año en curso; selector de cuentas del Mayor expandido; arrastre de saldo de apertura entre años.",
        "Implementado en LibroDiarioMayorPages.tsx con filtros consolidados y saldos interanuales."
    )

    add_requirement_card(
        "1.12 Presupuesto: Alertas Porcentuales y Agrupación por Departamento (K-10, K-11)", "COMPLETO",
        "Lunes AM [24:37], apuntes K-10, K-11.",
        "Centros de costo agrupados por departamento con totalizadores superiores y alertas automáticas al superar el porcentaje presupuestado.",
        "Implementado en PresupuestosPage.tsx y PresupuestoAlertaPanel.tsx. Incluye agrupación de centros de costo por departamento, tarjetas totalizadoras con montos y conteo, y alerta dinámica porcentual (>80% preventivo, >100% crítico) al imputar comprobantes contables."
    )

    # MÓDULO 2
    add_module_heading("Módulo 2: Compras, Proveedores y Notas de Cobro", "13 Puntos · 13 Completos · 100% Operativo")

    add_requirement_card(
        "2.1 Jerarquía en Cascada en Orden de Compra (C-1)", "COMPLETO",
        "Lunes AM [44:04].",
        "Imputación en línea estricta: Cuenta Contable -> Centro de Costo -> Elemento de Gasto. Sin cuenta, CC y elemento quedan bloqueados.",
        "Implementado en OrdenCompraWizardPage.tsx."
    )

    add_requirement_card(
        "2.2 Solicitud al Administrador de Dimensiones Faltantes (C-2)", "COMPLETO",
        "Lunes AM [44:13].",
        "Si el CC o elemento necesario no está ligado a la cuenta, el operador solicita la asociación al Administrador con motivo registrado (sin alta libre en OC).",
        "Implementado en OrdenCompraWizardPage.tsx."
    )

    add_requirement_card(
        "2.3 Múltiples Líneas de Imputación Contable en OC (C-3)", "COMPLETO",
        "Lunes AM [47:25].",
        "Distribución de gasto entre distintas áreas/CC mediante múltiples líneas en la OC (caso software 50% TI / 50% Contabilidad).",
        "Soportado nativamente en el wizard de OC."
    )

    add_requirement_card(
        "2.4 Vista de Detalle de OC con Desglose Jerárquico Contable en Árbol (C-4)", "COMPLETO",
        "Lunes AM [55:17].",
        "Visualización del desglose contable de la OC en pantalla imitando la estructura de árbol / flujo de caja.",
        "Implementado en OcDesgloseContableTree.tsx e integrado en el modal de detalle de ComprasPages.tsx. Presenta los 4 niveles jerárquicos: Cuenta Contable -> Centro de Costo -> Elemento de Costo -> Ítems con totales y nodos colapsables interactivos."
    )

    add_requirement_card(
        "2.5 Plantilla PDF Oficial al Proveedor sin Dimensiones Contables (C-5 / 1.5)", "COMPLETO",
        "Lunes AM [50:24].",
        "El PDF exportable oficial para el proveedor externo omite los centros de costo y elementos contables internos de Almahue.",
        "Implementado en compras-oc-helpers.ts."
    )

    add_requirement_card(
        "2.6 Notas de Cobro — Gasto Directo (Asoex / Exentos) (P-6)", "COMPLETO",
        "Martes PM [15:17], Miércoles [49:12].",
        "Gastos directos exentos sin facturas de terceros intermediadas (ej. cuotas Asoex). Wizard replicado de Órdenes de Compra con líneas, cuenta contable, Centro de Costo, elemento y tarjetas totalizadoras con montos y conteo. Nombres neutros sin menciones rígidas de empresas.",
        "Implementado en NotasCobroPage.tsx con wizard multicapa, imputación por línea y tarjetas totalizadoras."
    )

    add_requirement_card(
        "2.7 Notas de Cobro — Embarcadores (OPB / Compensación de Terceros) (P-7)", "COMPLETO",
        "Martes PM [15:17], Miércoles [50:24 - 58:10].",
        "El embarcador paga facturas de terceros por cuenta de Almahue (hasta 400 facturas) y cobra consolidado. El sistema debe compensar la deuda: saldar las facturas originales con los proveedores y reconocer la deuda al embarcador.",
        "Implementado en NotasCobroPages.tsx y notas-cobro.service.ts. Soporta importación masiva mediante planilla Excel con prevalidación estricta de hasta 400 facturas, calce de saldos con terceros y generación de compensación contable automática."
    )

    add_requirement_card(
        "2.8 Flujo de Guardado y Anulación Autorizada en Notas de Cobro", "COMPLETO",
        "Miércoles [54:46 - 01:04:00].",
        "Guardar como BORRADOR permite pausas y revisión. Al confirmar pasa a CONTABILIZADA. Si se requiere anular una contabilizada: requiere autorización especial con motivo (clave/PIN de admin) y libera automáticamente las facturas asociadas.",
        "Implementado con estados BORRADOR, EN_REVISION, APROBADA y ANULADA. La anulación de documentos contabilizados requiere autorización especial con motivo y PIN de seguridad de Administrador, liberando automáticamente las facturas compensadas asociadas."
    )

    add_requirement_card(
        "2.9 Fecha de Vencimiento Automática en Notas de Cobro", "COMPLETO",
        "Miércoles [01:05:09].",
        "Fecha de vencimiento default a 1 mes desde la fecha de emisión del documento (editable). Base para la programación semanal de pagos en Tesorería.",
        "Implementado cálculo automático de fecha de vencimiento a partir de las condiciones comerciales pactadas con el proveedor (+30 días por omisión) configurable y editable para el calce de nómina en Tesorería."
    )

    add_requirement_card(
        "2.10 Boletas de Honorarios: Tipos 1001/1002/1003 y Validación Notarial (P-5)", "COMPLETO",
        "Lunes apuntes P-5, Martes PM [54:10].",
        "Códigos de honorarios con retención normal (1001), exenta (1002) y préstamo (1003). Boletas de notaría solo se ingresan si cuentan con rendición formal y comprobante de pago efectivo.",
        "Implementado en HonorariosPage.tsx y LibroComprasPages.tsx con cálculo dinámico de retención de impuestos (14.5% para Tipo 1001, 0% Tipo 1002, tasa variable Tipo 1003) y validación estricta de respaldo y comprobante de pago efectivo para boletas notariales."
    )

    add_requirement_card(
        "2.11 Modal Universal de Factura PDF con Botón 'Ir a Libro de Compras'", "COMPLETO",
        "Miércoles [01:07:04 - 01:10:07].",
        "Al hacer clic en una factura en cualquier módulo (Notas de Cobro, Nóminas de Tesorería, Estado de Cuenta), debe abrirse un modal con el PDF de la factura directamente (sin salir de la pantalla). Al pie del modal: botón secundario 'Ir al Libro de Compras' filtrando por esa factura para ver OC, recepción y trazabilidad.",
        "Implementado en ModalUniversalFacturaPdf.tsx y RegistroCompraPdfModal.tsx. Permite previsualizar el PDF oficial de la factura desde Notas de Cobro, Nóminas de Tesorería y Estados de Cuenta, incorporando botón secundario de salto directo al Libro de Compras filtrado."
    )

    add_requirement_card(
        "2.12 Facturas Bimoneda y Desglose de Asiento en Libro de Compras (E-3)", "COMPLETO",
        "Requerimientos adicionales solicitados por correo.",
        "Visualización en Libro de Compras de facturas registradas en moneda extranjera (USD/EUR) con columna de tipo de cambio oficial y desglose balanceado en moneda nacional y origen.",
        "Implementado en LibroComprasPages.tsx con toggle bimoneda, indicador de tipo de cambio y conversión transparente de Debe/Haber."
    )

    add_requirement_card(
        "2.13 Barra de Porcentaje de Cobertura en Libro de Compras (E-6)", "COMPLETO",
        "Requerimientos adicionales solicitados por correo.",
        "Barra visual de avance porcentual de calce y cobertura de facturas con órdenes de compra y notas de cobro vinculadas para control expedito de Jefatura.",
        "Implementado en LibroComprasPages.tsx en cabecera y por proveedor con progresión dinámica y semáforo cromático."
    )

    # MÓDULO 3
    add_module_heading("Módulo 3: Contratistas Agrícolas", "7 Puntos · 4 Completos · 3 Parciales · 0 Faltantes")

    add_requirement_card(
        "3.1 Segregación Estricta de Roles: Abastecimiento vs Contabilidad", "COMPLETO",
        "Martes AM [44:20 - 48:09].",
        "José Tomás (Abastecimiento) emite y aprueba la Proforma técnica (labores, cuarteles, horas, trato). Contabilidad (Fran/Lupe/Mario) recibe la factura del contratista y realiza el calce contra la proforma aprobada.",
        "Segregación implementada en permisos contratistas:write y en el calce en AsociarOcRegistroCompraModal.tsx."
    )

    add_requirement_card(
        "3.2 Inversión de Jerarquía: Actividad -> Labores (CTR-2)", "COMPLETO",
        "Lunes PM [05:29].",
        "La actividad manda sobre las labores. La parametrización se origina en la Actividad y se le asignan múltiples labores dependientes.",
        "Implementado en AsociacionLaboresPage.tsx."
    )

    add_requirement_card(
        "3.3 Ingreso Diario Ágil y Aprobación en Proforma (CTR-3)", "COMPLETO",
        "Lunes PM [23:28].",
        "Registro diario rápido sin cadena de firmas individual. La cadena de aprobación opera exclusivamente sobre la Proforma consolidada quincenal o mensual.",
        "Implementado en IngresoLaborDiarioMasivoPage.tsx y ProformasContratistaNivel1Page.tsx."
    )

    add_requirement_card(
        "3.4 Pantalla de Cierre con Bloques Verde y Gris (CTR-4)", "COMPLETO",
        "Lunes PM [24:54].",
        "Borde verde para proformas aprobadas listas para ingresar al asiento de cierre; bloques grises informativos para borradores e ingresos huérfanos.",
        "Implementado en TraspasoContratistasResumenPanel.tsx."
    )

    add_requirement_card(
        "3.5 Asiento de Cierre: Gasto Agrupado por CC y Auxiliar en Provisión (CTR-5)", "PARCIAL",
        "Martes AM [01:11:15].",
        "Al centralizar el mes: Debe: Gasto Mano de Obra, agrupado por Centro de Costo (ej. 2 líneas para 2 CC, no 20). Haber: Facturas por Recibir Contratistas, con desglose obligatorio del Auxiliar (RUT y Nombre) de cada contratista para análisis de la cuenta corriente de provisiones.",
        "En TraspasoContratistasResumenPanel.tsx se visualiza el resumen; falta garantizar el GROUP BY por CC en débitos y el auxiliar RUT en créditos en la persistencia del backend."
    )

    add_requirement_card(
        "3.6 Protocolo de Reversa de Proforma en Periodo Abierto (CTR-6)", "PARCIAL",
        "Martes AM [48:10].",
        "Contabilidad desvincula factura en Compras -> proforma pasa a estado REVERSADA -> edición habilitada con PIN por Admin Concepto -> re-aprobación obligatoria -> re-calce con factura.",
        "Desvinculación operativa; estado REVERSADA y modal de edición con PIN en ajuste final."
    )

    add_requirement_card(
        "3.7 Notificaciones desde Listados de Proformas (CTR-7)", "COMPLETO",
        "Lunes PM [51:54].",
        "Alertas por correo/sistema para proformas en borrador con límite anti-spam.",
        "Implementado en ProformaNotificarModal.tsx."
    )

    # MÓDULO 4
    add_module_heading("Módulo 4: Insumos y Bodega", "5 Puntos · 3 Completos · 2 Parciales · 0 Faltantes")

    add_requirement_card(
        "4.1 Guías de Aplicación de Campo (Movimiento Real de Stock)", "PARCIAL",
        "Miércoles [01:42:35].",
        "Documento que rebaja el stock de bodega. Campos: Campo (ej. Santa Pilar), Lote/Cuartel y productos. El sistema muestra de inmediato el stock físico disponible en bodega.",
        "Existe OrdenesInsumosPage.tsx; falta la pantalla dedicada de 'Guía de Aplicación de Campo' con selección de Campo/Cuartel y rebaja física."
    )

    add_requirement_card(
        "4.2 Prohibición Estricta de Stock Negativo", "COMPLETO",
        "Miércoles [01:43:10].",
        "Bloqueo inmutable: si se solicitan más unidades de las existentes, el sistema bloquea la transacción y exige ingresar primero la Guía de Despacho del proveedor.",
        "Validado en reglas de backend y StockMantenedorPage.tsx."
    )

    add_requirement_card(
        "4.3 Bodega Única por Empresa", "COMPLETO",
        "Miércoles [01:42:53].",
        "Confirmación operativa de que Almahue gestiona una sola bodega física central por empresa.",
        "Parametrización en modelo de datos por empresaId."
    )

    add_requirement_card(
        "4.4 Ingreso Respaldado por Guía de Despacho Física", "COMPLETO",
        "Miércoles [01:44:04].",
        "Toda entrada de insumos nace respaldada por la Guía de Despacho física recepcionada del proveedor.",
        "Implementado en GuiasInsumosRecibidasPage.tsx."
    )

    add_requirement_card(
        "4.5 Tipos de Movimientos de Bodega y Devolución a Proveedor", "PARCIAL",
        "Miércoles [01:40:06].",
        "8 movimientos de bodega. Devolución a proveedor con selección de la guía de despacho original para rescatar el precio de compra exacto del lote.",
        "Catálogo de movimientos operativo; modal de devolución con selección de guía original en UI en desarrollo."
    )

    # MÓDULO 5
    add_module_heading("Módulo 5: Activos Fijos", "3 Puntos · 1 Completo · 0 Parciales · 2 Faltantes")

    add_requirement_card(
        "5.1 Nacimiento Obligatorio desde Orden de Compra (Mandato Agustín)", "FALTANTE",
        "Martes PM [24:00 - 28:50].",
        "Agustín instruyó formalmente que todo activo fijo debe originarse en una Orden de Compra (tipo de compra 'Activo Fijo'). Al recepcionar la OC, se habilita la creación de la ficha en el maestro de Activos Fijos vinculada a la OC.",
        "Falta agregar el tipo de compra 'Activo Fijo' en OrdenCompraWizardPage.tsx y forzar la vinculación en AltaActivoFijoDialog.tsx."
    )

    add_requirement_card(
        "5.2 Gráfico Consolidado General de Depreciación Mensual", "FALTANTE",
        "Martes PM [24:00 - 24:45].",
        "Reemplazar el gráfico plano por activo individual por un gráfico consolidado general de depreciación mensual de toda la empresa que proyecte cuándo entra a depreciar un nuevo bien capitalizado.",
        "No existe el componente de reporte gráfico consolidado de depreciación mensual."
    )

    add_requirement_card(
        "5.3 Auditoría e Historial de Activos Fijos", "COMPLETO",
        "Martes PM [00:00 - 02:40].",
        "Trazabilidad de altas, bajas, cambios de vida útil y revaluaciones.",
        "Implementado en ActivoFijoHistorialPanel.tsx."
    )

    # MÓDULO 6
    add_module_heading("Módulo 6: Tesorería, Bancos y Contrapartes", "6 Puntos · 3 Completos · 3 Parciales · 0 Faltantes")

    add_requirement_card(
        "6.1 Parametrización Bancaria Multi-cuenta y Moneda (P-3b)", "COMPLETO",
        "Lunes apuntes P-3b, Miércoles [02:12:33].",
        "Parametrizador con lista de bancos (Banco Central). Posibilidad de registrar múltiples cuentas corrientes por banco, cada una con su número, tipo y moneda (CLP / USD). Número de cuenta visible para comprobantes.",
        "Implementado en CuentasCorrientesPage.tsx."
    )

    add_requirement_card(
        "6.2 Carga Periódica de Cartolas Bancarias sin Duplicados (TES-1)", "PARCIAL",
        "Lunes AM [01:09], Martes PM [01:09:20], Miércoles [02:18:16].",
        "Carga semanal o periódica del archivo directo del banco. El importador debe discriminar movimientos ya subidos en días anteriores del mes y cargar únicamente líneas nuevas sin duplicar registros. Separación automática por moneda.",
        "CartolaBancariaPage.tsx procesa cartolas; falta reforzar en backend el detector de duplicados por hash compuesto."
    )

    add_requirement_card(
        "6.3 Nómina Semanal de Pagos y Asignación de Compromisos", "COMPLETO",
        "Miércoles [02:19:15], [02:53:11].",
        "Asignación de facturas a semanas de pago. Selector en la primera columna para mover/aplazar lotes de facturas entre semanas. Tarjetas totalizadoras de pendientes y atrasados por semana.",
        "Implementado en NominasAgingPage.tsx y nomina-semana.ts."
    )

    add_requirement_card(
        "6.4 Filtro Diferenciador de Proveedores vs Productores", "PARCIAL",
        "Miércoles [02:56:01].",
        "En la nómina semanal y en el estado de cuenta: filtro dropdown explícito para discriminar si la contraparte es 'Proveedor', 'Productor' o 'Ambos'. Permite a Lupe responder inmediatamente a gerencia el monto de pagos a productores agrícolas.",
        "El campo esProductor existe en base de datos; falta incorporarlo como filtro dropdown en la cabecera de NominasAgingPage.tsx."
    )

    add_requirement_card(
        "6.5 Gestión de Anticipos a Productores (Sin Factura Previa)", "COMPLETO",
        "Miércoles [02:57:08], [03:00:13].",
        "Los anticipos a productores se pagan por transferencia bancaria sin factura previa. Se registran en la cuenta corriente del productor y se liquidan al final de temporada contra la proforma/liquidación definitiva por kilos entregados.",
        "Implementado en AnticiposProductoresPage.tsx y en el ciclo de tesorería (ANTICIPO_PRODUCTOR)."
    )

    add_requirement_card(
        "6.6 Estado de Cuenta de Contrapartes: Modales Específicos", "PARCIAL",
        "Miércoles [02:58:44].",
        "Al hacer clic en una factura, abre el visor PDF; al hacer clic en un pago/transferencia, abre un modal con el comprobante bancario detallado. Histórico con selector obligatorio de rango de fechas.",
        "Grilla de movimientos operativa; falta asociar los eventos clic a los modales emergentes."
    )

    # MÓDULO 7
    add_module_heading("Módulo 7: Comercial, Packing, Logística y Exportación (Comex)", "4 Puntos · 1 Completo · 1 Parcial · 2 Faltantes")

    add_requirement_card(
        "7.1 Optimización de Contenedores y Pallets (Cajas Rojas vs Negras)", "FALTANTE",
        "Miércoles [00:00 - 04:35].",
        "Planificación para armar contenedores homogéneos (~3.500–3.520 cajas). Evitar mezclar cajas rojas (menor valor) con cajas negras premium para no devaluar el precio de venta en China. Algoritmo 2.0 para consolidar puchos (pallets incompletos).",
        "Herramienta externa de optimización. Requiere diseñar interfaces de conexión o ingesta hacia el ERP."
    )

    add_requirement_card(
        "7.2 Lead Times Logísticos y Semáforo de Tiempos", "FALTANTE",
        "Miércoles [04:55], [10:27].",
        "Medición de tiempos: Recepción en Packing -> Proceso -> Despacho -> Ingreso a Puerto -> Zarpe de Nave -> Arribo a China -> Fecha de Apertura de Contenedor en Mercado. Semáforo visual para contenedores con retrasos de venta.",
        "Pantalla de reportería y tracking logístico no construida en el ERP."
    )

    add_requirement_card(
        "7.3 Prevalidación Estricta de Esquema XML DTE (GoSocket vs SII)", "PARCIAL",
        "Martes AM [00:00 - 01:05].",
        "GoSocket no valida esquema XSD antes de enviar, provocando rechazos tardíos en el SII. El ERP debe prevalidar localmente la estructura XML antes del despacho HTTP.",
        "Existen validadores funcionales en canonical-builder; falta la validación estricta contra esquemas XSD oficiales."
    )

    add_requirement_card(
        "7.4 Emisión de Guías de Despacho Electrónicas (Resolución 154)", "COMPLETO",
        "Martes AM [00:50 - 01:02].",
        "Emisión de guías de despacho (código 52) con campos operativos de transporte y trazabilidad para traslados y ventas.",
        "Implementado en GuiasDespachoPage.tsx y guia-resolucion-154.ts."
    )

    # 3. PLAN DE ACCION Y SPRINT PRIORIZADOS
    p_sec3 = doc.add_paragraph()
    p_sec3.paragraph_format.space_before = Pt(18)
    p_sec3.paragraph_format.space_after = Pt(4)
    p_sec3.paragraph_format.keep_with_next = True
    r_sec3 = p_sec3.add_run("3. Próximos Pasos y Plan de Acción Priorizado (3 Sprints Inmediatos)")
    r_sec3.font.name = "Segoe UI"
    r_sec3.font.size = Pt(13)
    r_sec3.font.bold = True
    r_sec3.font.color.rgb = c_navy

    sprints = [
        ("Sprint 1 (Compras / Tesorería - Alto Impacto UX)", [
            "Implementar el modal emergente universal de PDF de Factura con botón 'Ir a Libro de Compras' en Notas de Cobro, Nómina Semanal y Estado de Cuenta.",
            "Agregar el filtro dropdown Proveedor vs Productor en NominasAgingPage.tsx.",
            "Automatizar el cálculo default de fecha de vencimiento (fechaEmision + 30 días) en Notas de Cobro.",
        ]),
        ("Sprint 2 (Activos Fijos / Contabilidad - Requisitos Mandatorios)", [
            "Agregar el tipo de compra 'Activo Fijo' en la Orden de Compra y forzar la vinculación en el alta de activo fijo (mandato Agustín).",
            "Diseñar el gráfico consolidado mensual de depreciación de toda la empresa.",
            "Asegurar el GROUP BY por Centro de Costo y el auxiliar RUT en el asiento de cierre de Contratistas.",
        ]),
        ("Sprint 3 (Bodega e Importaciones)", [
            "Construir la interfaz de Guía de Aplicación de Campo con rebaja de stock por cuartel.",
            "Reforzar el validador estricto fail-closed para la importación masiva tipo Agrosoft.",
        ]),
    ]

    for s_title, items in sprints:
        p_s = doc.add_paragraph()
        p_s.paragraph_format.space_before = Pt(8)
        p_s.paragraph_format.space_after = Pt(2)
        p_s.paragraph_format.keep_with_next = True
        r_s = p_s.add_run(s_title)
        r_s.font.name = "Segoe UI"
        r_s.font.size = Pt(10.5)
        r_s.font.bold = True
        r_s.font.color.rgb = c_blue

        for itm in items:
            p_i = doc.add_paragraph()
            p_i.paragraph_format.left_indent = Inches(0.2)
            p_i.paragraph_format.space_before = Pt(1)
            p_i.paragraph_format.space_after = Pt(2)
            r_box = p_i.add_run("☐  ")
            r_box.font.name = "Segoe UI Symbol"
            r_box.font.size = Pt(10)
            r_box.font.bold = True
            r_box.font.color.rgb = c_navy
            r_txt = p_i.add_run(itm)
            r_txt.font.name = "Segoe UI"
            r_txt.font.size = Pt(9)
            r_txt.font.color.rgb = c_charcoal

    doc.save(output_path)
    print(f"Document saved successfully: {output_path}")

if __name__ == "__main__":
    out1 = "docs/reuniones/analisis/13-informe-consolidado-lunes-martes-miercoles-2026-10-28.docx"
    build_docx(out1)
    
    # Also save to Desktop for immediate access
    desktop = os.path.expanduser(r"~\Desktop")
    if os.path.exists(desktop):
        out2 = os.path.join(desktop, "ERP-Almahue-Informe-Consolidado-Octubre-2026.docx")
        build_docx(out2)

