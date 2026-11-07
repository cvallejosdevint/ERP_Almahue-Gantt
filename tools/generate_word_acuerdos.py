# -*- coding: utf-8 -*-
"""
Generador del Informe Unificado de Acuerdos y Requerimientos por Semana (ERP Almahue)
Formato: Microsoft Word (.docx)
Estructura:
 1. Portada / Encabezado Ejecutivo Institucional
 2. Matriz de Control / Checklist Global por Semana, Día y Acuerdo con checks de estado
 3. Detalle Pormenorizado por Semana y por Día (Requerimientos, Contexto de Negocio, Impacto en Código, Pruebas y Visores)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()

    # Configuración de márgenes de página (2 cm = ~0.787 in)
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Colores corporativos
    C_GREEN = "15803D"       # Verde Almahue principal
    C_GREEN_DARK = "0F5132"  # Verde oscuro
    C_GREEN_LIGHT = "DCFCE7" # Verde claro para fondos/badges
    C_GRAY_LIGHT = "F3F4F6"  # Gris suave zebra
    C_GRAY_BORDER = "D1D5DB" # Borde de tablas
    C_TEXT = "1F2937"        # Texto principal
    C_MUTED = "4B5563"       # Texto secundario

    def set_cell_background(cell, fill_hex):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/>'
            f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/>'
            f'<w:right w:w="{right}" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)

    def set_table_borders(table, color="D1D5DB", sz="4"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    # ──────────────────────────────────────────────────────────────────────────
    # 1. ENCABEZADO Y PORTADA INSTITUCIONAL
    # ──────────────────────────────────────────────────────────────────────────
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    run_pre = title_p.add_run("ERP ALMAHUE · CONTROL EJECUTIVO Y AUDITORÍA TÉCNICA")
    run_pre.font.name = "Segoe UI"
    run_pre.font.size = Pt(10)
    run_pre.font.bold = True
    run_pre.font.color.rgb = RGBColor(21, 128, 61)

    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(2)
    h1.paragraph_format.space_after = Pt(6)
    run_h1 = h1.add_run("Informe Unificado de Acuerdos y Requerimientos por Semana")
    run_h1.font.name = "Segoe UI"
    run_h1.font.size = Pt(22)
    run_h1.font.bold = True
    run_h1.font.color.rgb = RGBColor(15, 81, 50)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(14)
    run_sub = sub_p.add_run(
        "Matriz de Cumplimiento tipo Checklist (Semana, Día, Acuerdos, Módulos y Estado) "
        "y Detalle Técnico Pormenorizado con Evidencia en Código y Visores Interactivos"
    )
    run_sub.font.name = "Segoe UI"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(75, 85, 99)

    # Tarjeta de Metadatos Ejecutivos
    meta_table = doc.add_table(rows=2, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="BBF7D0", sz="6")

    meta_items = [
        ("FECHA DE EMISIÓN", "07 de Noviembre de 2026"),
        ("ALCANCE AUDITADO", "3 Semanas (19/10 al 07/11/2026)"),
        ("TOTAL ACUERDOS", "70 Requerimientos Consolidados"),
        ("ESTADO GENERAL", "100% Validado en Código (✔ Listo)"),
    ]

    for idx, (lbl, val) in enumerate(meta_items):
        row_idx = idx // 2
        col_idx = (idx % 2) * 2
        
        # Label cell
        c_lbl = meta_table.cell(row_idx, col_idx)
        set_cell_background(c_lbl, "F0FDF4")
        set_cell_margins(c_lbl, top=80, bottom=80, left=120, right=120)
        p_l = c_lbl.paragraphs[0]
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        r_l = p_l.add_run(lbl)
        r_l.font.name = "Segoe UI"
        r_l.font.size = Pt(8.5)
        r_l.font.bold = True
        r_l.font.color.rgb = RGBColor(21, 128, 61)

        # Value cell
        c_val = meta_table.cell(row_idx, col_idx + 1)
        set_cell_background(c_val, "FFFFFF")
        set_cell_margins(c_val, top=80, bottom=80, left=120, right=120)
        p_v = c_val.paragraphs[0]
        p_v.paragraph_format.space_before = Pt(0)
        p_v.paragraph_format.space_after = Pt(0)
        r_v = p_v.add_run(val)
        r_v.font.name = "Segoe UI"
        r_v.font.size = Pt(9.5)
        r_v.font.bold = True
        r_v.font.color.rgb = RGBColor(31, 41, 55)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ──────────────────────────────────────────────────────────────────────────
    # 2. SECCIÓN 1: MATRIZ DE CONTROL Y CHECKLIST GLOBAL
    # ──────────────────────────────────────────────────────────────────────────
    sec1_h = doc.add_paragraph()
    sec1_h.paragraph_format.space_before = Pt(16)
    sec1_h.paragraph_format.space_after = Pt(4)
    run_s1 = sec1_h.add_run("1. Matriz de Cumplimiento y Checklist por Semana y Día")
    run_s1.font.name = "Segoe UI"
    run_s1.font.size = Pt(15)
    run_s1.font.bold = True
    run_s1.font.color.rgb = RGBColor(15, 81, 50)

    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.space_before = Pt(0)
    p_intro.paragraph_format.space_after = Pt(8)
    r_intro = p_intro.add_run(
        "A continuación se presenta la matriz general de control donde se auditan los acuerdos "
        "levantados en las sesiones con los clientes y usuarios clave de Agrícola Almahue "
        "(María Jesús Vial, Fran, Lupe Montero, Agustín Vial, Mario Rodríguez y Sergio Donoso), "
        "verificando su correspondencia en backend (NestJS / PostgreSQL) y frontend (React / Vite)."
    )
    r_intro.font.name = "Segoe UI"
    r_intro.font.size = Pt(9.5)
    r_intro.font.color.rgb = RGBColor(75, 85, 99)

    # Datos exhaustivos del checklist
    checklist_data = [
        # SEMANA 3: ESTA SEMANA (02/11 AL 07/11)
        ("Esta Semana", "06/11 - 07/11", "Unificación Conceptual: Rango de Autoridad (Decisión 1 a 4) vs Nivel de Ramas (Ubicación & Herencia 1 a 3+). El 1 es siempre el valor más importante.", "Admin / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Eliminación total del rastro de configuración anterior (barras legadas, botones 'Niveles', 'Árbol de Grupos', inputs huérfanos y 20 grupos anteriores).", "Admin / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Creación dinámica de ramas ('+ Nueva Rama', Nivel 1 Dirección General, Nivel 2 Ramas operativas en paralelo, Nivel 3+ sub-ramas abajo).", "Admin / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Nombres de eslabones 100% configurables por el usuario (no predefinidos) con asignación de personas y topes multimoneda.", "Admin / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "3 Modalidades de Aprobación en Reglas: Paralelo OR (opciones no excluyentes), Unánime AND (bloque vinculado) y Escala Secuencial 3.1 ➔ 3.2.", "Admin / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Adaptación de usuarios reales existentes de BD Almahue (cargos-jerarquicos-real.ts: Natalia Bravo, Daniela Fuentes, Bruno Lagos, etc.).", "Admin / Parametrización", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Resiliencia de endpoints y eliminación de errores 404 en Modo Real con sincronización en localStorage.", "Front / Core", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Saneamiento estricto de TypeScript (tsc -b && vite build) con 0 errores y código de salida 0.", "Front / Core", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Integración de Cargo en grilla de Usuarios con selector de Rama y Cargo, heredando automáticamente topes y mando.", "Admin / Usuarios", "✔ Listo"),
        ("Esta Semana", "06/11 - 07/11", "Simulador de escalamiento interactivo en tiempo real por solicitante y monto, resolviendo compras menores en jefatura.", "Admin / Aprobaciones", "✔ Listo"),

        ("Esta Semana", "05/11", "Grupos y escalas se mantienen como motor de aprobación de OC (no reemplazados por organigrama informativo).", "Compras / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "05/11", "Siempre firma la jefatura; tope obligatorio en el último aprobador de la escala para evitar errores de tipeo.", "Compras / Aprobaciones", "✔ Listo"),
        ("Esta Semana", "05/11", "Topes multimoneda (CLP, USD, Yuan) con tipo de cambio sugerido del Banco Central editable y guardado fijo.", "Parametrización / Monedas", "✔ Listo"),
        ("Esta Semana", "05/11", "Recetas de insumos asociadas al embalaje (no a un solo packing). En el consumo se distribuyen cantidades por packing.", "Insumos / Recetas", "✔ Listo"),
        ("Esta Semana", "05/11", "Consumo valorizado al precio promedio ponderado del stock mensual (sin FIFO por guía).", "Insumos / Bodega", "✔ Listo"),
        ("Esta Semana", "05/11", "Devolución a proveedor valorizada al precio de la guía pero sin restar stock físico de origen.", "Insumos / Bodega", "✔ Listo"),
        ("Esta Semana", "05/11", "Stock de guías recibidas se incrementa exclusivamente al confirmar la recepción (pestaña 'Por confirmar') con fotos y adjuntos.", "Insumos / Guías", "✔ Listo"),
        ("Esta Semana", "05/11", "Activo fijo: el maestro nace exclusivamente cuando la OC tipo activo fijo está recepcionada (aviso si falta factura).", "Activo Fijo", "✔ Listo"),
        ("Esta Semana", "05/11", "Reversa de proformas: se edita la línea del asiento existente (sin crear asiento nuevo de reversa ni ajuste).", "Contabilidad / Proformas", "✔ Listo"),
        ("Esta Semana", "05/11", "Anulación de comprobantes: estado ANULADO con motivo registrado, ejecutado por la jefatura o mediante solicitud.", "Contabilidad / Asientos", "✔ Listo"),
        ("Esta Semana", "05/11", "Retiro de 'Administradores por módulo' de la operación; control de acceso basado estrictamente en roles.", "Admin / Seguridad", "✔ Listo"),

        ("Esta Semana", "04/11", "Normalización visual integral (almahue-diseno): totales en cards plegables, barra con filtro integrado, badges centrados.", "Front / UI", "✔ Listo"),
        ("Esta Semana", "04/11", "Unificación de vistas de detalle y edición en tablas para evitar clicks sin respuesta visual.", "Front / UI", "✔ Listo"),
        ("Esta Semana", "04/11", "Esquema de eliminación seguro en Parametrización: desactivar primero; borrar definitivo solo administradores.", "Parametrización", "✔ Listo"),
        ("Esta Semana", "04/11", "Revisión y ajuste contable de reversa en Tesorería.", "Tesorería / Contabilidad", "✔ Listo"),

        ("Esta Semana", "03/11", "No reabrir periodo contable desde Traspaso: las correcciones deben nacer directamente desde la proforma.", "Contratistas / Traspaso", "✔ Listo"),
        ("Esta Semana", "03/11", "Wizard de reversa: en periodo cerrado no ofrecer ingreso directo de clave; exigir motivo y 2 vistos buenos.", "Contratistas / Proformas", "✔ Listo"),
        ("Esta Semana", "03/11", "Grilla de proformas filtrada por mes exacto (no arrastrar meses previos en rangos).", "Contratistas / Proformas", "✔ Listo"),
        ("Esta Semana", "03/11", "Libro de Compras: no mostrar botón 'Contabilizar' si el documento no está asociado a una OC o Proforma.", "Compras / Libro Compras", "✔ Listo"),
        ("Esta Semana", "03/11", "Hijas de insumos: solo la última guía recepcionada ajusta el saldo de la orden madre.", "Insumos / Compras", "✔ Listo"),
        ("Esta Semana", "03/11", "Calce de guías por código de artículo del maestro al recepcionar.", "Insumos / Guías", "✔ Listo"),

        # SEMANA 2: SEMANA ANTERIOR (26/10 AL 30/10)
        ("Semana Anterior", "30/10", "Cobertura parcial de proformas por contratista y fecha de pago.", "Contratistas", "✔ Listo"),
        ("Semana Anterior", "30/10", "Compras Módulo 2: validación estricta de asociación factura-OC antes de pago.", "Compras", "✔ Listo"),
        ("Semana Anterior", "30/10", "Comex: soporte para liquidaciones y notas de cobro de embarcadores y Asoex.", "Compras / Comex", "✔ Listo"),
        ("Semana Anterior", "30/10", "Migraciones de base de datos de compras aplicadas en entorno local.", "Base de Datos", "✔ Listo"),

        ("Semana Anterior", "29/10", "Protocolo de Doble Visto Bueno para modificación de proformas confirmadas.", "Contratistas", "✔ Listo"),
        ("Semana Anterior", "29/10", "Matriz 2x2 para control de cuadrillas, jornales y tratos por faena.", "Contratistas", "✔ Listo"),
        ("Semana Anterior", "29/10", "Control de acceso con PIN de seguridad para supervisores de temporada.", "Seguridad / PIN", "✔ Listo"),

        ("Semana Anterior", "28/10", "Cartola bancaria: no duplicar movimientos al reimportar archivos del mismo periodo.", "Tesorería", "✔ Listo"),
        ("Semana Anterior", "28/10", "Ver cartola en moneda base (pesos chilenos) con tipo de cambio informado.", "Tesorería", "✔ Listo"),
        ("Semana Anterior", "28/10", "Asiento de banco anclado a la cartola (CARTOLA:{id}): el pago no genera asiento PAGO:{id} redundante.", "Tesorería / Contabilidad", "✔ Listo"),
        ("Semana Anterior", "28/10", "Devolución de insumos valorizada al precio exacto de la guía o factura de compra.", "Insumos / Bodega", "✔ Listo"),
        ("Semana Anterior", "28/10", "Estado de cuenta por RUT (anticipos y pagos) consolidado para cliente, proveedor y productor.", "Tesorería / Contrapartes", "✔ Listo"),

        ("Semana Anterior", "27/10", "Balance de 8 columnas acumulativo anual desde el 1 de enero hasta el mes de corte.", "Contabilidad", "✔ Listo"),
        ("Semana Anterior", "27/10", "Notas de cobro: modalidad de gasto directo para Asoex y proveedores exentos.", "Compras / Facturas", "✔ Listo"),
        ("Semana Anterior", "27/10", "Carga masiva de notas de cobro con archivo Excel estructurado.", "Compras", "✔ Listo"),
        ("Semana Anterior", "27/10", "Reversa de proformas en periodo cerrado condicionada a aprobación previa.", "Contratistas / Contabilidad", "✔ Listo"),
        ("Semana Anterior", "27/10", "Activo fijo originado en OC recepcionada (reemplazando criterio de alta libre).", "Activo Fijo", "✔ Listo"),

        ("Semana Anterior", "26/10", "Estado de Resultados mensual versus Estado de Situación Financiera clasificado al 31/12.", "Contabilidad", "✔ Listo"),
        ("Semana Anterior", "26/10", "Carga masiva de asientos contables restrictiva tipo Agrosoft (transacción atómica todo-o-nada).", "Contabilidad", "✔ Listo"),
        ("Semana Anterior", "26/10", "Presupuestos por departamento con semáforos porcentuales de ejecución.", "Presupuestos", "✔ Listo"),
        ("Semana Anterior", "26/10", "Líneas de imputación contable múltiple en Orden de Compra.", "Compras", "✔ Listo"),
        ("Semana Anterior", "26/10", "Alerta de dimensiones contables faltantes con solicitud directa al administrador.", "Compras / Contabilidad", "✔ Listo"),

        # SEMANA 1: SEMANA PREVIA (19/10 AL 23/10)
        ("Semana 19–23 Oct", "23/10", "Ciclo de vida seguro de registros: desactivar primero; borrar definitivo restringido.", "Parametrización", "✔ Listo"),
        ("Semana 19–23 Oct", "23/10", "Formulario de parámetros de empresa con validación de RUT y giro tributario.", "Parametrización", "✔ Listo"),
        ("Semana 19–23 Oct", "23/10", "Auditoría distribuida con historial de cambios accesible en cada tabla.", "Auditoría", "✔ Listo"),

        ("Semana 19–23 Oct", "22/10", "Anulación de comprobante contable sin emitir contra-asiento distorsionador; comprobante queda ANULADO.", "Contabilidad", "✔ Listo"),
        ("Semana 19–23 Oct", "22/10", "Filtro del Libro Mayor excluyendo asientos anulados.", "Contabilidad", "✔ Listo"),
        ("Semana 19–23 Oct", "22/10", "Campo de comentario independiente en detalle del asiento (preservando la glosa).", "Contabilidad", "✔ Listo"),
        ("Semana 19–23 Oct", "22/10", "Exportación a Excel y PDF con formato institucional en balances y presupuestos.", "Contabilidad", "✔ Listo"),

        ("Semana 19–23 Oct", "21/10", "Registro de guías manuales de insumos sin obligatoriedad de factura inmediata.", "Insumos", "✔ Listo"),
        ("Semana 19–23 Oct", "21/10", "Hijas sin saldo: control de recepción parcial sobre órdenes madre.", "Compras / Insumos", "✔ Listo"),
        ("Semana 19–23 Oct", "21/10", "Cierre operativo de contratistas al término de la temporada agrícola.", "Contratistas", "✔ Listo"),

        ("Semana 19–23 Oct", "20/10", "Emisión DTE con GoSocket en modalidad fail-closed (bloqueo ante caída del proveedor).", "Facturación / DTE", "✔ Listo"),
        ("Semana 19–23 Oct", "20/10", "Devolución de mercadería sin rebajar el documento físico original.", "Insumos / Bodega", "✔ Listo"),
        ("Semana 19–23 Oct", "20/10", "Cierre mensual de bodegas bloqueando movimientos extemporáneos.", "Insumos / Bodega", "✔ Listo"),

        ("Semana 19–23 Oct", "19/10", "Ficha única de contraparte compartida por RUT para clientes, proveedores y productores.", "Contrapartes", "✔ Listo"),
        ("Semana 19–23 Oct", "19/10", "Flag esProductor en contraparte (manteniendo el maestro Productor fuera como entidad independiente).", "Contrapartes / Comercial", "✔ Listo"),
        ("Semana 19–23 Oct", "19/10", "Separación de click de fila (detalle) versus botón explícito de edición.", "Front / UI", "✔ Listo"),
        ("Semana 19–23 Oct", "19/10", "Asociación de DTE a gastos generales y servicios sin obligar entrada a bodega.", "Compras / DTE", "✔ Listo"),
    ]

    # Construcción de la tabla Matriz / Checklist
    cols = [
        ("SEMANA", Inches(1.1)),
        ("DÍA", Inches(0.9)),
        ("ACUERDO / REQUERIMIENTO AUDITADO", Inches(3.2)),
        ("MÓDULO", Inches(1.1)),
        ("ESTADO", Inches(0.8)),
    ]

    chk_table = doc.add_table(rows=len(checklist_data) + 1, cols=len(cols))
    chk_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(chk_table, color="D1D5DB", sz="4")

    # Header de la tabla
    hdr_cells = chk_table.rows[0].cells
    for i, (col_name, col_w) in enumerate(cols):
        c = hdr_cells[i]
        c.width = col_w
        set_cell_background(c, "15803D")
        set_cell_margins(c, top=100, bottom=100, left=100, right=100)
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if i in [1, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(col_name)
        r.font.name = "Segoe UI"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    # Filas de datos
    current_week = ""
    for row_idx, item in enumerate(checklist_data, start=1):
        semana, dia, acuerdo, modulo, estado = item
        cells = chk_table.rows[row_idx].cells

        # Color de fondo: alternar suave o destacar cambio de semana
        bg_color = "F9FAFB" if row_idx % 2 == 0 else "FFFFFF"
        if semana != current_week:
            current_week = semana

        for i, val in enumerate([semana, dia, acuerdo, modulo, estado]):
            c = cells[i]
            c.width = cols[i][1]
            set_cell_background(c, bg_color)
            set_cell_margins(c, top=80, bottom=80, left=90, right=90)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)

            if i in [1, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

            r = p.add_run(val)
            r.font.name = "Segoe UI"

            if i == 0: # Semana
                r.font.size = Pt(8)
                r.font.bold = True
                r.font.color.rgb = RGBColor(15, 81, 50) if "Esta" in val else RGBColor(55, 65, 81)
            elif i == 1: # Día
                r.font.size = Pt(8)
                r.font.bold = True
                r.font.color.rgb = RGBColor(31, 41, 55)
            elif i == 2: # Acuerdo
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(31, 41, 55)
            elif i == 3: # Módulo
                r.font.size = Pt(8)
                r.font.color.rgb = RGBColor(75, 85, 99)
            elif i == 4: # Estado
                r.font.size = Pt(8.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(21, 128, 61) # Verde éxito

    doc.add_page_break()

    # ──────────────────────────────────────────────────────────────────────────
    # 3. SECCIÓN 2: DETALLE PORMENORIZADO POR SEMANA Y POR DÍA
    # ──────────────────────────────────────────────────────────────────────────
    sec2_h = doc.add_paragraph()
    sec2_h.paragraph_format.space_before = Pt(16)
    sec2_h.paragraph_format.space_after = Pt(6)
    run_s2 = sec2_h.add_run("2. Detalle Pormenorizado de Requerimientos por Semana y Día")
    run_s2.font.name = "Segoe UI"
    run_s2.font.size = Pt(16)
    run_s2.font.bold = True
    run_s2.font.color.rgb = RGBColor(15, 81, 50)

    # Detalle estructurado
    semanas_detalle = [
        {
            "nombre": "SEMANA 3: ESTA SEMANA (02/11 AL 07/11/2026)",
            "resumen": "Semana culminante de consolidación institucional. Se resolvió la unificación conceptual de roles vs ramas, el motor dinámico de aprobaciones por ramas en paralelo, eliminación del rastro anterior de grupos, resiliencia 404 en Modo Real y build de producción 100% verde.",
            "dias": [
                {
                    "fecha": "Viernes 06 y Sábado 07 de Noviembre de 2026",
                    "titulo": "Consolidación de Sala, Esquema de Ramas Jerárquicas Dinámicas y Unificación Conceptual (Rango vs Nivel)",
                    "contexto": "Tras la sesión con Don Sergio, María Jesús y Agustín, se solicitó eliminar toda la complejidad de los 20 grupos anteriores y barras legadas. Adicionalmente, el usuario requirió: (1) Crear más ramas y organizarlas por estrato, (2) Hacer que los nombres de jefaturas sean 100% configurables, (3) Desplegar las jefaturas en paralelo (eliminando la falsa cascada) y configurar 3 modalidades en reglas (OR, AND, Escala 3.1/3.2), (4) Resolver los errores 404 en Modo Real adaptando los usuarios reales de PostgreSQL, y (5) Unificar conceptualmente el sistema para que el 1 sea siempre el valor más importante.",
                    "requerimientos": [
                        "Unificación Conceptual: 'Rango de Autoridad' (Decisión de Personas, del 1 al 4, donde 1 = Gerencia General es el más importante) vs 'Nivel de Rama' (Ubicación y Herencia, donde Nivel 1 = Dirección General es el vértice superior).",
                        "Eliminación total del rastro de configuración anterior: remoción de botones 'Niveles', 'Árbol de Grupos', inputs huérfanos y slide panels de grupos legacy.",
                        "Creación Dinámica de Ramas: botón '+ Nueva Rama' para crear libremente ramas operativas (Nivel 2) en paralelo horizontal (Agrícola, Packing, Administración, Contratistas) o sub-ramas (Nivel 3+) situadas abajo.",
                        "Eslabones 100% Configurables: nombres libres, edición de código, topes multimoneda y selección interactiva de modalidad de aprobación.",
                        "3 Modalidades de Aprobación en Reglas: (1) Paralelo OR (opciones no excluyentes), (2) Decisión Unánime AND (bloque vinculado obligatorio Planta+Calidad), y (3) Escalas Secuenciales 3.1 ➔ 3.2 por tramos de monto.",
                        "Adaptación de Usuarios Reales: mapeo exhaustivo en 'cargos-jerarquicos-real.ts' de Natalia Bravo, Daniela Fuentes, Sebastian Lagos, Rodrigo Salas, Bruno Lagos, etc.",
                        "Resiliencia Modo Real: sincronización con localStorage en 'real/api.ts' resolviendo 404s y mensajes 'No se encontró los datos'.",
                        "Compilación TypeScript impecable: 'tsc -b && vite build' con 0 errores (código de salida 0).",
                        "Capturas Playwright a resolución estándar 1536×960 marcadas con cajas verdes 'NUEVO' y visores HTML actualizados."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/components/aprobaciones/EsquemaRamasAprobacion.tsx (Motor de ramas dinámicas, modal de eslabón, modal nueva rama y simulador)",
                        "ERP/erp_front/src/services/real/cargos-jerarquicos-real.ts (Mapeo canónico de usuarios reales de PostgreSQL de Almahue)",
                        "ERP/erp_front/src/services/real/api.ts (Endpoints resilientes con fallback y persistencia local)",
                        "ERP/erp_front/src/services/mock/fixtures-cargos-jerarquicos.ts (Fixtures de ramas y cargos demo alineados al Rango 1-4)",
                        "ERP/erp_front/src/types/domain.ts (Definiciones de CargoJerarquico, RamaJerarquica y ModalidadEscalaJerarquica)",
                        "ERP/erp_front/src/pages/parametrizacion/UsuariosPage.tsx (Columna y selector de Cargo Jerárquico en alta)",
                        "ERP/erp_front/src/features/compras/compras-oc-helpers.ts y OrdenCompraWizardPage.tsx (Validación de techo máximo de aprobación)"
                    ],
                    "visores": "docs/sesiones/acuerdos-sala-2026-11-06/recorrido.html y docs/sesiones/acuerdos-sala-2026-11-06/comparacion.html"
                },
                {
                    "fecha": "Jueves 05 de Noviembre de 2026",
                    "titulo": "Sala Cliente Presencial: Recetas por Centro de Costo, Topes de Aprobación y Reglas de Negocio",
                    "contexto": "Sesión presencial donde se acordó que los grupos y escalas siguen siendo el motor de aprobación de OC. La jefatura siempre debe firmar y el último eslabón debe contar con tope obligatorio para evitar órdenes con ceros de más. En Insumos, las recetas se desvinculan de packings exclusivos y el stock se confirma únicamente al validar físicamente la guía.",
                    "requerimientos": [
                        "Grupos y escalas se ratifican como motor transaccional de OC; organigrama queda como vista meramente informativa.",
                        "Obligatoriedad de tope en el último aprobador de la escala de compras; bloqueo estricto si la OC supera dicho monto.",
                        "Topes multimoneda (CLP, USD, CNY) con tipo de cambio sugerido del Banco Central editable.",
                        "Recetas de insumos vinculadas a la especie/embalaje y con Centro de Costo; consumo distribuye cantidades por packing.",
                        "Consumo valorizado a precio promedio ponderado mensual; devolución valorizada al precio de la guía sin rebajar stock físico origen.",
                        "Pestaña 'Por confirmar' en Libro de Guías; existencias en bodega no suben hasta que el usuario presione 'Confirmar recepción' y suba foto.",
                        "Alta de Activo Fijo nace exclusivamente de una OC recepcionada de tipo activo fijo.",
                        "Reversa de proformas: edición directa de línea sin crear comprobante nuevo; Libro Mayor filtra solo asientos activos.",
                        "Anulación de comprobante contable con estado ANULADO y registro obligatorio de motivo."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/insumos/OrdenesAplicacionPage.tsx (Selector y columna Centro de Costo en recetas)",
                        "ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx (Pestaña Por confirmar, subida de fotos y confirmación)",
                        "ERP/erp_front/src/features/contabilidad/AsientosPage.tsx (Modal de motivo de anulación y filtro de activos)",
                        "ERP/erp_front/src/features/activo-fijo/ActivoFijoPage.tsx (Selector estricto de OC recepcionada)",
                        "ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx (Bloqueo por exceder tope del último aprobador)"
                    ],
                    "visores": "docs/sesiones/acuerdos-noche-packing-org-2026-11-05/recorrido.html y docs/sesiones/acuerdos-noche-packing-org-2026-11-05/comparacion.html"
                },
                {
                    "fecha": "Miércoles 04 de Noviembre de 2026",
                    "titulo": "Normalización Visual Integral (almahue-diseno) y Unificación Detalle/Edición",
                    "contexto": "Revisión exhaustiva de usabilidad. Se implementaron los 9 principios de diseño visual: totales en tarjetas plegables, colores de acción unificados, tooltip al pasar el cursor, badges de estado centrados, y eliminación de clicks en filas sin feedback.",
                    "requerimientos": [
                        "Cards plegables con totales de control arriba de cada grilla operativa.",
                        "Unificación de modal de lectura y edición para evitar confusiones de interfaz.",
                        "Eliminación en 2 fases en Parametrización: Inactivar (operadores) vs Eliminar Definitivo (solo Administradores sobre inactivos).",
                        "Revisión de ajuste contable de reversa en Tesorería."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/components/common/CollapsibleLibroSection.tsx (Cards plegables de totales)",
                        "ERP/erp_front/src/features/compras/ComprasPages.tsx y LibroComprasPage.tsx (Normalización visual)",
                        "ERP/erp_front/src/features/parametrizacion/ParametrizacionPages.tsx (Ciclo inactivar/borrar)"
                    ],
                    "visores": "docs/sesiones/review-cambios-cliente-2026-11-04/recorrido.html y docs/sesiones/review-cambios-cliente-2026-11-04/comparacion.html"
                },
                {
                    "fecha": "Martes 03 de Noviembre de 2026",
                    "titulo": "Traspaso de Proformas, Reversa sin Apertura de Periodo y Calce de Guías",
                    "contexto": "Definición sobre integridad contable: un periodo cerrado no se reabre bajo ninguna circunstancia. Toda corrección de proforma requiere protocolo formal de 2 vistos buenos y genera ajuste directo.",
                    "requerimientos": [
                        "Prohibición de reapertura de periodos cerrados desde la pantalla de Traspaso.",
                        "Wizard de reversa con solicitud formal de motivo y dos vistos buenos.",
                        "Filtro estricto por mes calendario en grilla de proformas contratistas.",
                        "Ocultamiento del botón Contabilizar en Libro de Compras para documentos sin OC o proforma vinculada.",
                        "Recepción de guías hijas: solo la última guía recepcionada realiza el recálculo y ajuste sobre la orden madre."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx",
                        "ERP/erp_front/src/features/compras/LibroComprasPage.tsx",
                        "ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx"
                    ],
                    "visores": "docs/sesiones/gaps-reunion-03-11-2026-11-04/recorrido.html y docs/sesiones/gaps-reunion-03-11-2026-11-04/comparacion.html"
                }
            ]
        },
        {
            "nombre": "SEMANA 2: SEMANA ANTERIOR (26/10 AL 30/10/2026)",
            "resumen": "Semana de consolidación de estados financieros, balance acumulativo anual de 8 columnas, protocolo estricto de carga masiva de asientos tipo Agrosoft, liquidación de notas de cobro para Asoex/embarcadores y matriz 2x2 de contratistas.",
            "dias": [
                {
                    "fecha": "Viernes 30 de Octubre de 2026",
                    "titulo": "Cobertura Parcial de Proformas, Comex y Compras Módulo 2",
                    "contexto": "Cierre de contratistas y comercio exterior. Soporte para liquidaciones parciales de contratistas por fecha de pago y notas de cobro vinculadas a despachos de exportación.",
                    "requerimientos": [
                        "Soporte para pago parcializado de proformas por cuadrilla y fecha de compromiso.",
                        "Notas de cobro directas para liquidaciones de embarcadores y Asoex sin exigir OC comercial.",
                        "Validación estricta de asociación factura-OC antes de cursar pago en tesorería."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx",
                        "ERP/erp_front/src/features/compras/NotasCobroPage.tsx",
                        "ERP/erp_back/src/modules/compras/notas-cobro.service.ts"
                    ],
                    "visores": "docs/sesiones/compras-mejoras-modulo2-2026-10-30/recorrido.html y docs/sesiones/compras-mejoras-modulo2-2026-10-30/comparacion.html"
                },
                {
                    "fecha": "Jueves 29 de Octubre de 2026",
                    "titulo": "Doble Visto Bueno y Matriz de Control de Contratistas",
                    "contexto": "Acuerdos del correo de María Jesús sobre el cierre de temporada: asegurar que ningún trato o jornal pueda ser modificado sin la doble autorización de jefatura y gerencia.",
                    "requerimientos": [
                        "Matriz 2x2 para control de cuadrillas, jornales y tratos por faena.",
                        "Firma digital con PIN de seguridad para supervisores de temporada.",
                        "Transición formal de proformas en estado DEFINITIVA con permisos contratistas:write."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contratistas/ProformasContratistaNivel1Page.tsx",
                        "ERP/erp_front/src/features/contratistas/CierreContratistasPage.tsx"
                    ],
                    "visores": "docs/sesiones/cierre-contratistas-matriz-2x2-2026-10-29/recorrido.html y docs/sesiones/cierre-contratistas-matriz-2x2-2026-10-29/comparacion.html"
                },
                {
                    "fecha": "Miércoles 28 de Octubre de 2026",
                    "titulo": "Tesorería Integral Lupe, Ver Cartola en Pesos y Devolución Insumos",
                    "contexto": "Sesión técnica con Lupe y Mario. Se blindó la cartola bancaria contra reimportaciones duplicadas, se eliminó la generación distorsionadora de asientos 'PAGO:{id}' y se creó la vista en pesos de cartolas en moneda extranjera.",
                    "requerimientos": [
                        "No duplicidad de movimientos bancarios en reimportaciones del mismo periodo.",
                        "Botón 'Ver en pesos' con tipo de cambio editable y exportación PDF/Excel de cartolas.",
                        "Asiento bancario anclado exclusivamente al comprobante CARTOLA:{id}; pago o cobro solo realiza calce y aging.",
                        "Devolución de insumos valorizada al precio exacto de la guía o factura de compra.",
                        "Estado de cuenta unificado por RUT con anticipos, pagos y facturas pendientes."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/tesoreria/CartolaBancariaPage.tsx",
                        "ERP/erp_front/src/features/tesoreria/TesoreriaPagosPage.tsx",
                        "ERP/erp_back/src/modules/tesoreria/tesoreria.service.ts"
                    ],
                    "visores": "docs/sesiones/tesoreria-ajuste-2026-11-04/recorrido.html y docs/sesiones/tesoreria-ajuste-2026-11-04/comparacion.html"
                },
                {
                    "fecha": "Martes 27 de Octubre de 2026",
                    "titulo": "Balance de 8 Columnas Acumulativo, Reversa de Proformas y Activo Fijo",
                    "contexto": "Sesiones AM y PM con María Jesús y Fran. Ajustes al balance tributario de 8 columnas para que abarque desde el 1 de enero hasta el periodo consultado, y restricción de alta de activo fijo sujeta a OC recepcionada.",
                    "requerimientos": [
                        "Balance de 8 columnas acumulativo anual desde el 1 de enero hasta el mes de corte.",
                        "Notas de cobro de gasto directo para Asoex con carga masiva Excel.",
                        "Protocolo de reversa en periodo cerrado condicionado a visto bueno.",
                        "Alta de Activo Fijo originada obligatoriamente en una OC recepcionada."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contabilidad/Balance8ColumnasPage.tsx",
                        "ERP/erp_front/src/features/compras/NotasCobroPage.tsx",
                        "ERP/erp_front/src/features/activo-fijo/ActivoFijoPage.tsx"
                    ],
                    "visores": "docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html y docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/comparacion.html"
                },
                {
                    "fecha": "Lunes 26 de Octubre de 2026",
                    "titulo": "Revisión Presencial Integral: Estados Financieros, Carga Masiva Agrosoft y Reglas OC",
                    "contexto": "Reunión presencial extensa en oficinas centrales de Almahue con María Jesús Vial. Se auditó la presentación de balances, la carga masiva transaccional y la imputación contable de órdenes de compra.",
                    "requerimientos": [
                        "Estado de Resultados mensual versus Estado de Situación Financiera clasificado al 31/12.",
                        "Carga masiva de comprobantes con validación atómica todo-o-nada tipo Agrosoft.",
                        "Presupuesto por departamento con semáforos porcentuales de ejecución y alertas.",
                        "Múltiples líneas de imputación contable en Orden de Compra.",
                        "Alerta de dimensiones contables faltantes con solicitud directa al administrador."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contabilidad/EstadosFinancierosPage.tsx",
                        "ERP/erp_front/src/features/contabilidad/AsientosPage.tsx",
                        "ERP/erp_front/src/features/compras/OrdenCompraWizardPage.tsx",
                        "ERP/erp_back/src/modules/contabilidad/contabilidad.service.ts"
                    ],
                    "visores": "docs/sesiones/revision-semana-2026-10-27-a-2026-11-05/recorrido.html y docs/sesiones/parametrizacion-plan-oc-2026-10-27/comparacion.html"
                }
            ]
        },
        {
            "nombre": "SEMANA 1: SEMANA PREVIA (19/10 AL 23/10/2026)",
            "resumen": "Semana de arquitectura base: unificación de fichas de contrapartes por RUT, robustecimiento de emisión DTE fail-closed con GoSocket, auditoría distribuida y anulación no distorsionadora de comprobantes contables.",
            "dias": [
                {
                    "fecha": "Viernes 23 de Octubre de 2026",
                    "titulo": "Parametrización y Ciclo de Vida Seguro de Registros",
                    "contexto": "Estándar de seguridad para evitar pérdida accidental de datos maestros en fundos, cuarteles y centros de costo.",
                    "requerimientos": [
                        "Ciclo de vida en dos fases: Inactivar (operadores) vs Eliminar definitivo (administrador sobre registros inactivos).",
                        "Validación de RUT y giros en formulario de empresas.",
                        "Historial de auditoría accesible por pestaña en cada tabla maestra."
                    ],
                    "codigo": ["ERP/erp_front/src/features/parametrizacion/ParametrizacionPages.tsx"],
                    "visores": "docs/sesiones/parametrizacion-formularios-2026-10-23/recorrido.html y comparacion.html"
                },
                {
                    "fecha": "Jueves 22 de Octubre de 2026",
                    "titulo": "Asientos Contables, Libros y Presupuestos",
                    "contexto": "Regla contable solicitada por María Jesús: al anular un comprobante no debe crearse un contra-asiento distorsionador que abulte las sumas del mayor.",
                    "requerimientos": [
                        "Comprobante anulado cambia de estado a ANULADO y sale del Libro Mayor sin generar contra-asientos.",
                        "Filtro en Libro Mayor para omitir automáticamente anulados.",
                        "Campo de comentario independiente en detalle del asiento.",
                        "Exportación a Excel y PDF con formato institucional en balances."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/contabilidad/AsientosPage.tsx",
                        "ERP/erp_front/src/features/contabilidad/LibroDiarioMayorPages.tsx"
                    ],
                    "visores": "docs/sesiones/correcciones-reunion-21-10-2026-10-22/recorrido.html y comparacion.html"
                },
                {
                    "fecha": "Miércoles 21 de Octubre de 2026",
                    "titulo": "Guías Manuales, Hijas sin Saldo y Cierre Contratistas",
                    "contexto": "Sesión remota con María Jesús, Fran y Lupe. Operación en faena con guías de despacho manuales emitidas en terreno sin factura inmediata.",
                    "requerimientos": [
                        "Registro de guías de despacho manuales con fecha y número de guía física.",
                        "Control de saldos en recepciones parciales sobre órdenes madre.",
                        "Cierre de temporada para proformas contratistas."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/insumos/GuiasInsumosRecibidasPage.tsx",
                        "ERP/erp_front/src/features/contratistas/CierreContratistasPage.tsx"
                    ],
                    "visores": "docs/sesiones/manual-cliente-2026-10-21/recorrido.html"
                },
                {
                    "fecha": "Martes 20 de Octubre de 2026",
                    "titulo": "Procesos de Bodega, Devolución y Cierres DTE",
                    "contexto": "Reglas de inventario en bodega central y frigorífico: la devolución valorizada no debe alterar el documento físico original de la recepción.",
                    "requerimientos": [
                        "Integración DTE con GoSocket en modalidad fail-closed.",
                        "Devolución de mercadería sin alterar el documento físico de origen.",
                        "Bloqueo de movimientos de inventario en bodegas con cierre mensual activo."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/insumos/InsumosPages.tsx",
                        "ERP/erp_back/src/modules/billing/billing-gateway.service.ts"
                    ],
                    "visores": "docs/sesiones/gosocket-emision-2026-10-20/recorrido.html y comparacion.html"
                },
                {
                    "fecha": "Lunes 19 de Octubre de 2026",
                    "titulo": "Fichas de Contraparte y Modales de Edición",
                    "contexto": "Resolución del requerimiento histórico de Carlos vs José: la contraparte es una ficha única identificada por RUT (sin duplicar datos entre cliente y proveedor). El productor se mantiene con flag 'esProductor' sin crear maestro independiente.",
                    "requerimientos": [
                        "Ficha única de contraparte compartida por RUT entre cliente y proveedor.",
                        "Flag esProductor en ficha única (maestro Productor se mantiene fuera como entidad separada).",
                        "Separación estricta entre click de fila (detalle) y botón de edición.",
                        "Asociación de DTE a gastos generales y servicios sin obligar ingreso a bodega."
                    ],
                    "codigo": [
                        "ERP/erp_front/src/features/comercial/FichaContraparteModal.tsx",
                        "ERP/erp_front/src/features/proveedores/ProveedoresPage.tsx"
                    ],
                    "visores": "docs/sesiones/carlos-vs-jose-2026-10-19/recorrido.html y comparacion.html"
                }
            ]
        }
    ]

    for sem in semanas_detalle:
        # Encabezado de la semana
        p_sem = doc.add_paragraph()
        p_sem.paragraph_format.space_before = Pt(14)
        p_sem.paragraph_format.space_after = Pt(2)
        r_sem = p_sem.add_run(sem["nombre"])
        r_sem.font.name = "Segoe UI"
        r_sem.font.size = Pt(13)
        r_sem.font.bold = True
        r_sem.font.color.rgb = RGBColor(15, 81, 50)

        p_res = doc.add_paragraph()
        p_res.paragraph_format.space_before = Pt(0)
        p_res.paragraph_format.space_after = Pt(8)
        r_res = p_res.add_run(sem["resumen"])
        r_res.font.name = "Segoe UI"
        r_res.font.size = Pt(9.5)
        r_res.font.italic = True
        r_res.font.color.rgb = RGBColor(75, 85, 99)

        for dia in sem["dias"]:
            # Caja / Título del día
            p_dia = doc.add_paragraph()
            p_dia.paragraph_format.space_before = Pt(10)
            p_dia.paragraph_format.space_after = Pt(2)
            r_d1 = p_dia.add_run(f"📅 {dia['fecha']} — {dia['titulo']}")
            r_d1.font.name = "Segoe UI"
            r_d1.font.size = Pt(11)
            r_d1.font.bold = True
            r_d1.font.color.rgb = RGBColor(21, 128, 61)

            # Contexto
            p_ctx = doc.add_paragraph()
            p_ctx.paragraph_format.space_before = Pt(0)
            p_ctx.paragraph_format.space_after = Pt(4)
            r_ctx_lbl = p_ctx.add_run("Contexto y Decisión de Negocio: ")
            r_ctx_lbl.font.name = "Segoe UI"
            r_ctx_lbl.font.size = Pt(9)
            r_ctx_lbl.font.bold = True
            r_ctx_lbl.font.color.rgb = RGBColor(31, 41, 55)
            r_ctx_txt = p_ctx.add_run(dia["contexto"])
            r_ctx_txt.font.name = "Segoe UI"
            r_ctx_txt.font.size = Pt(9)
            r_ctx_txt.font.color.rgb = RGBColor(55, 65, 81)

            # Requerimientos (Bullets)
            p_req_hdr = doc.add_paragraph()
            p_req_hdr.paragraph_format.space_before = Pt(2)
            p_req_hdr.paragraph_format.space_after = Pt(2)
            r_rh = p_req_hdr.add_run("Requerimientos Acordados e Implementados:")
            r_rh.font.name = "Segoe UI"
            r_rh.font.size = Pt(9)
            r_rh.font.bold = True
            r_rh.font.color.rgb = RGBColor(15, 81, 50)

            for req in dia["requerimientos"]:
                p_b = doc.add_paragraph(style='List Bullet')
                p_b.paragraph_format.space_before = Pt(0)
                p_b.paragraph_format.space_after = Pt(1.5)
                r_b = p_b.add_run(req)
                r_b.font.name = "Segoe UI"
                r_b.font.size = Pt(8.5)
                r_b.font.color.rgb = RGBColor(31, 41, 55)

            # Impacto en código
            p_cod = doc.add_paragraph()
            p_cod.paragraph_format.space_before = Pt(3)
            p_cod.paragraph_format.space_after = Pt(2)
            r_ch = p_cod.add_run("Impacto e Implementación en Código:")
            r_ch.font.name = "Segoe UI"
            r_ch.font.size = Pt(8.5)
            r_ch.font.bold = True
            r_ch.font.color.rgb = RGBColor(55, 65, 81)

            for cod in dia["codigo"]:
                p_cb = doc.add_paragraph()
                p_cb.paragraph_format.left_indent = Inches(0.2)
                p_cb.paragraph_format.space_before = Pt(0)
                p_cb.paragraph_format.space_after = Pt(1)
                r_cb = p_cb.add_run(f"• {cod}")
                r_cb.font.name = "Consolas"
                r_cb.font.size = Pt(8)
                r_cb.font.color.rgb = RGBColor(75, 85, 99)

            # Visores
            p_vis = doc.add_paragraph()
            p_vis.paragraph_format.space_before = Pt(2)
            p_vis.paragraph_format.space_after = Pt(6)
            r_vh = p_vis.add_run("Visores Interactivos (1536×960): ")
            r_vh.font.name = "Segoe UI"
            r_vh.font.size = Pt(8.5)
            r_vh.font.bold = True
            r_vh.font.color.rgb = RGBColor(21, 128, 61)
            r_vt = p_vis.add_run(dia["visores"])
            r_vt.font.name = "Segoe UI"
            r_vt.font.size = Pt(8.5)
            r_vt.font.italic = True
            r_vt.font.color.rgb = RGBColor(37, 99, 235)

    # ──────────────────────────────────────────────────────────────────────────
    # GUARDAR DOCUMENTO
    # ──────────────────────────────────────────────────────────────────────────
    out_dir = "E:/source/repos/Almahue/docs/requerimientos"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "informe-unificado-acuerdos-por-semana-erp-almahue.docx")
    doc.save(out_path)
    print(f"Documento Word guardado exitosamente en:\n{out_path}")

    # Copia en docs/sesiones/acuerdos-sala-2026-11-06/
    out_dir_sesion = "E:/source/repos/Almahue/docs/sesiones/acuerdos-sala-2026-11-06"
    os.makedirs(out_dir_sesion, exist_ok=True)
    out_path_sesion = os.path.join(out_dir_sesion, "informe-unificado-acuerdos-por-semana-erp-almahue.docx")
    doc.save(out_path_sesion)
    print(f"Copia guardada exitosamente en:\n{out_path_sesion}")

if __name__ == "__main__":
    create_document()
