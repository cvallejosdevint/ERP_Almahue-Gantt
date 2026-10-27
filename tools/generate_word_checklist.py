import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document(output_path):
    doc = Document()

    # Page setup - Margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Styles
    primary_color = RGBColor(27, 54, 93)     # Navy #1B365D
    secondary_color = RGBColor(71, 85, 105) # Slate #475569
    dark_text = RGBColor(30, 41, 59)        # #1E293B
    accent_green = RGBColor(22, 101, 52)    # #166534

    # Header section
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    run_title = title_p.add_run("ERP ALMAHUE · CHECKLIST INTEGRAL DE PRESENTACIÓN")
    run_title.font.name = "Segoe UI"
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = primary_color

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(14)
    run_sub = sub_p.add_run("Reunión Presencial con Cliente · 26 de Octubre de 2026\nParticipantes: María Jesús (MJ), Lupe, Fran, Mario, Carlos y Sergio")
    run_sub.font.name = "Segoe UI"
    run_sub.font.size = Pt(10.5)
    run_sub.font.color.rgb = secondary_color

    # Credentials table
    table_cred = doc.add_table(rows=3, cols=2)
    table_cred.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_cred.autofit = False

    creds_data = [
        ("Entornos de Acceso", "Local: http://localhost:5174 | Servidor: http://45.7.229.46/almahue-erp/"),
        ("Usuario Demo / Operador", "admin@almahue.local  |  Clave: Admin123!  |  PIN Firma: 4821"),
        ("Empresas de Demostración", "Agrícola Almahue (RUT principal)  |  ALM Service (Dualidad y Servicios)"),
    ]

    for idx, (lbl, val) in enumerate(creds_data):
        row = table_cred.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        cell_lbl.width = Inches(2.2)
        cell_val.width = Inches(4.7)
        
        set_cell_background(cell_lbl, "F1F5F9")
        set_cell_background(cell_val, "FFFFFF")
        set_cell_margins(cell_lbl, 80, 80, 120, 120)
        set_cell_margins(cell_val, 80, 80, 120, 120)

        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(lbl)
        r0.font.name = "Segoe UI"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = primary_color

        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = dark_text

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    def add_section_header(title, audience):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        
        r1 = p.add_run(title)
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = primary_color

        r2 = p.add_run(f"  ·  [{audience}]")
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(10)
        r2.font.italic = True
        r2.font.color.rgb = secondary_color

    def add_checklist_item(code, title, details, key_rule=None):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)

        r_box = p.add_run("☐  ")
        r_box.font.name = "Segoe UI Symbol"
        r_box.font.size = Pt(11)
        r_box.font.bold = True
        r_box.font.color.rgb = primary_color

        r_title = p.add_run(f"{title}: ")
        r_title.font.name = "Segoe UI"
        r_title.font.size = Pt(10)
        r_title.font.bold = True
        r_title.font.color.rgb = dark_text

        r_det = p.add_run(details)
        r_det.font.name = "Segoe UI"
        r_det.font.size = Pt(9.5)
        r_det.font.color.rgb = dark_text

        if key_rule:
            p_rule = doc.add_paragraph()
            p_rule.paragraph_format.left_indent = Inches(0.45)
            p_rule.paragraph_format.space_before = Pt(1)
            p_rule.paragraph_format.space_after = Pt(4)
            r_rule_lbl = p_rule.add_run("Acuerdo / Regla: ")
            r_rule_lbl.font.name = "Segoe UI"
            r_rule_lbl.font.size = Pt(9)
            r_rule_lbl.font.bold = True
            r_rule_lbl.font.color.rgb = accent_green
            r_rule_val = p_rule.add_run(key_rule)
            r_rule_val.font.name = "Segoe UI"
            r_rule_val.font.size = Pt(9)
            r_rule_val.font.italic = True
            r_rule_val.font.color.rgb = secondary_color

    # 1. PARAMETRIZACION
    add_section_header("1. Parametrización y Catálogos Maestros", "Base transversal · Lupe, MJ y Fran")
    add_checklist_item(
        "PAR-01", "Mantenedor de Bancos (/catalogos/bancos)",
        "Crear una nueva institución seleccionando de la lista oficial chilena (Banco de Chile, Santander, BCI, Estado) y asociar a cuenta contable 1-1-01.",
        "Los bancos creados impactan automáticamente en Cartolas, Cuentas Corrientes y Flujo sin tocar código."
    )
    add_checklist_item(
        "PAR-02", "Mantenedor de Productores separado de Proveedores (/catalogos/productores)",
        "Mostrar en el menú la ubicación dedicada entre Proveedores y Contratistas. Probar creación con un RUT existente para mostrar la sinergia automática de contactos y direcciones.",
        "Se separa el catálogo para liquidaciones y fruta, evitando informes cruzados con proveedores de insumos."
    )
    add_checklist_item(
        "PAR-03", "Factor de Honorarios e Indicadores BC (/catalogos/factor-honorarios)",
        "Mostrar que el factor (13.75%) fue retirado del uso diario de contabilidad y quedó en Parametrización como dato maestro anual. Revisar tabla de IPC mensual para activo fijo.",
        "Configuración limpia sin interferir en la digitación periódica."
    )
    add_checklist_item(
        "PAR-04", "Monedas dinámicas y Alertas de Configuración Faltante",
        "Demostrar que monedas (CLP, USD, EUR, CNY) se gestionan dinámicamente. Mostrar la alerta visual con icono '!' si la empresa carece de bancos o tipo de cambio del día.",
        "Protección activa para evitar que los operadores ingresen asientos o cartolas sin parámetros."
    )

    # 2. INSUMOS Y BODEGAS
    add_section_header("2. Insumos, Bodegas y Libro de Guías", "Fran y MJ")
    add_checklist_item(
        "INS-01", "Maestro de Insumos y Precio de Compra (/insumos/articulos)",
        "Mostrar artículos con unidad de medida parametrizada. Revisar el campo 'Precio de compra del maestro' y costo promedio.",
        "Regla D16: el sistema bloquea comercialmente vender o valorar por debajo del costo de compra oficial."
    )
    add_checklist_item(
        "INS-02", "Libro de Guías: Ingreso Manual y Acepta (/insumos/guias)",
        "Mostrar el botón 'Ingreso manual' para guías físicas de campo. Subir archivos adjuntos escaneados o importar planilla Excel bajada de Acepta.",
        "Resuelve la dualidad operativa mientras abastecimiento migra gradualmente desde Acepta a GoSocket."
    )
    add_checklist_item(
        "INS-03", "Estados de Ley y Trazabilidad SII",
        "Visualizar columnas de acuse comercial, reclamo de contenido y recibo de mercaderías para cumplimiento tributario.",
        "Transparencia total con el SII y trazabilidad por número de guía."
    )
    add_checklist_item(
        "INS-04", "Cierre Mensual de Bodega e Insumos (/insumos/cierre-bodega)",
        "Explicar que las recepciones individuales no mueven caja ni generan deuda directa; se acumulan y al cierre de mes generan un único asiento: Existencias vs Facturas por Recibir.",
        "Cuenta preseleccionada y glosa editable a cargo de la jefatura contable."
    )

    # 3. COMPRAS Y APROBACIONES
    add_section_header("3. Compras, Órdenes y Aprobaciones", "Lupe, MJ y Mario")
    add_checklist_item(
        "COM-01", "Wizard de Orden de Compra (OC-AAAA-NNNN)",
        "Crear una orden con numeración formal. En el paso 1, seleccionar condiciones de pago comerciales (Contado, 15, 30, 45, 60, 90, 120 días). Notar alerta si coincide con la ficha.",
        "Cotización es solo una referencia opcional en la OC (D11); no hay menú ni trámite previo de cotización."
    )
    add_checklist_item(
        "COM-02", "Cadena de Aprobación por Escalas y Grupos (/admin/aprobaciones)",
        "Demostrar que la aprobación es exclusiva de Compras (OC). Firmar con PIN de 4 dígitos (4821). Mostrar simulador de cadena según tramos en UF/CLP.",
        "Regla canónica D4: se eliminó la cadena en Ventas (la OV va directo a facturar con stock)."
    )
    add_checklist_item(
        "COM-03", "Ciclo de Órdenes Madre e Hijas",
        "Demostrar que la OC Hija se crea con la recepción física. Al asociarle la factura en el Libro de Compras, la Hija se calza al 100% y muere/cierra sin saldo remanente.",
        "La única orden que conserva saldo para futuras recepciones es la OC Madre."
    )
    add_checklist_item(
        "COM-04", "Libro de Compras y Control de OC No Aprobada (/compras/libro)",
        "Asociar factura a orden de compra. Mostrar cómo se mata la cuenta 'Facturas por Recibir' y nace 'Proveedores'. Si la OC no está aprobada, se bloquea la contabilización y el pago.",
        "Garantiza que no se emita ningún cheque ni transferencia sin la firma previa de la orden."
    )

    # 4. CONTRATISTAS
    add_section_header("4. Contratistas y Proformas", "MJ y Operaciones")
    add_checklist_item(
        "CTR-01", "Proformas de Contratistas (/contratistas/proformas)",
        "Mostrar paso de Borrador a Definitiva con permiso de rol (contratistas:write), sin cadena burocrática de PIN.",
        "Desglose por contratista, faena, cuartel y labor agrícola con respaldo de adjuntos."
    )
    add_checklist_item(
        "CTR-02", "Cierre y Centralización de Contratistas (/contratistas/traspaso)",
        "Mostrar que al asiento de centralización solo pasan las proformas facturadas; las demás quedan como informativas.",
        "Cuenta preseleccionada 'Mano de obra contratista' y glosa editable."
    )

    # 5. VENTAS Y DTE
    add_section_header("5. Ventas, Facturación y DTE", "MJ y Facturación")
    add_checklist_item(
        "VEN-01", "Órdenes de Venta con Validación de Stock y Costo (/comercial/ordenes)",
        "Al pulsar Guardar, el sistema valida existencias en bodega y deja la orden directamente en CONFIRMADA. Probar bloqueo si el precio de venta es inferior al costo de compra (D16).",
        "Protege el margen comercial y agiliza la facturación sin pasos innecesarios."
    )
    add_checklist_item(
        "VEN-02", "Emisión de DTE Factura/NC/ND/Guía (/comercial/emitir)",
        "Seleccionar cliente normalizado. Emitir Factura electrónica (33). Explicar que en la emisión no se piden cuentas contables para no distraer al emisor.",
        "El documento queda EMITIDO y viaja automáticamente al Libro de Ventas como 'Por contabilizar'."
    )
    add_checklist_item(
        "VEN-03", "Libro de Ventas y Contabilización (/comercial/libro)",
        "Mostrar las órdenes 'Por facturar' y los DTEs 'Por contabilizar'. Abrir modal de asignación de cuentas por ítem y generar el asiento formal.",
        "Desacoplamiento limpio entre la operación de venta y el control contable."
    )

    # 6. TESORERIA Y FLUJOS
    add_section_header("6. Tesorería, Cartolas y Cuentas Corrientes", "Lupe y MJ")
    add_checklist_item(
        "TES-01", "Cartolas Bancarias y Adjuntos (/tesoreria/cartolas)",
        "Cargar archivo de cartola bancaria. Mostrar switch de conversión de monedas (USD/CNY a CLP). Abrir un movimiento y subir adjuntos de boletas o comprobantes de transferencia.",
        "Parser dinámico por nombres de columnas (no posicional). Totales por concepto plegables."
    )
    add_checklist_item(
        "TES-02", "Nómina Semanal y Aging (/tesoreria/nominas-aging)",
        "Mostrar grilla limpia con un único badge prioritario por fila (Pagada > OC no operable > Crítico/90d > Semana movida > Pendiente). Demostrar cambio de semana de pago con motivo obligatorio.",
        "El sistema exige justificación obligatoria (mín. 5 car.) para respaldo y trazabilidad de prórrogas."
    )
    add_checklist_item(
        "TES-03", "Estado de Cuenta por RUT / Cuentas Corrientes (/tesoreria/cuentas-corrientes)",
        "Kardex unificado por RUT con filtro directo por rol: Proveedor, Productor o Cliente. Abrir modal de detalle con filtro Pendiente vs Histórico y pinchar 'Exportar Excel'.",
        "Genera Excel con cabecera de RUT, razón social y detalle cronológico de calces y saldos."
    )

    # 7. CONTABILIDAD OFICIAL
    add_section_header("7. Contabilidad General y Libros Oficiales", "María Jesús")
    add_checklist_item(
        "CON-01", "Comprobantes y Asientos (/contabilidad/asientos)",
        "Filtro 'Solo activos' activo por defecto (reversas ocultas). Pinchar 'Editar glosa' para agregar comentarios de auditoría sin alterar cuentas ni montos. Pinchar 'Exportar PDF'.",
        "Cumple invariables P0-1: la glosa es editable para auditoría, las cuentas y montos quedan protegidos."
    )
    add_checklist_item(
        "CON-02", "Libro Mayor con Fechas y Multi-Año (/contabilidad/mayor)",
        "Filtro con calendario (Desde/Hasta) e input de búsqueda rápida de cuentas. Mostrar que el Mayor sí permite consultar rangos que cruzan múltiples años.",
        "Permite auditorías históricas profundas con totales de Debe y Haber agregados."
    )
    add_checklist_item(
        "CON-03", "Balance de 8 Columnas y Estados Financieros (/contabilidad/balance)",
        "Intentar consultar cruzando de un año a otro (ej: dic-2025 a ene-2026). Mostrar la advertencia bloqueante: 'Cuentas de resultado cierran al 31 de diciembre; consulta dentro del mismo año'.",
        "Acuerdo explícito del 22/10 con MJ: garantiza que los balances anuales no arrastren distorsiones."
    )
    add_checklist_item(
        "CON-04", "Presupuestos por Centro de Costo (/presupuestos)",
        "Visualizar ejecución anual de montos por centro de costo y pinchar 'Exportar PDF / Imprimir'.",
        "Reporte ejecutivo estructurado con porcentajes de consumo y saldos disponibles."
    )

    # 8. ACTIVO FIJO
    add_section_header("8. Activo Fijo", "María Jesús")
    add_checklist_item(
        "ACT-01", "Alta de Activo Fijo (/catalogos/activo-fijo)",
        "Alta directa ligada exclusivamente a una factura del Libro de Compras. Sin centro de costo en el alta y con vida útil única en meses (sin fechas de fin ni campos duplicados).",
        "Acuerdo 21/10: el activo no nace de bodega ni de órdenes de insumos; nace de la factura de compra."
    )
    add_checklist_item(
        "ACT-02", "IPC Mensual y Depreciación Tributaria",
        "Revisar tabla de IPC mensual cargada y preview de cálculo de corrección monetaria y depreciación tributaria mensual.",
        "Ajuste automático de valor neto mes a mes sin alterar el valor histórico de adquisición."
    )

    # PREGUNTAS FRECUENTES Y BLINDAJE
    p_faq_title = doc.add_paragraph()
    p_faq_title.paragraph_format.space_before = Pt(16)
    p_faq_title.paragraph_format.space_after = Pt(6)
    r_faq_title = p_faq_title.add_run("9. Respuestas Blindadas ante Preguntas Clave del Cliente")
    r_faq_title.font.name = "Segoe UI"
    r_faq_title.font.size = Pt(13)
    r_faq_title.font.bold = True
    r_faq_title.font.color.rgb = primary_color

    faq_data = [
        ("¿Por qué las Órdenes de Venta no tienen cadena de aprobación?",
         "En la sesión del 20 de agosto se acordó que la aprobación se concentra en el egreso de fondos (Compras). La Orden de Venta valida stock y costo de compra (D16) y pasa directo a facturación para no frenar despachos comerciales."),
        ("¿Dónde se crea una Cotización para Compras?",
         "La cotización se simplificó como referencia informativa (número y fecha) en la Orden de Compra (D11). La OC es el documento vinculante de arranque, evitando burocracia previa."),
        ("¿Cómo se evita mezclar Proveedores con Productores?",
         "Se creó el módulo exclusivo de Productores en Parametrización. Al registrarlos allí, se les asigna el rol productor y en Cuentas Corrientes se puede filtrar su listado puro para anticipos y liquidaciones."),
        ("¿Qué pasará con la pantalla de Pagos si la Cartola manda?",
         "La Cartola ya permite imputar cuentas, centros de costo, semanas y adjuntos en cada movimiento. La pantalla de pagos se mantuvo vinculada para definir juntos en esta sesión si se apaga definitivamente o queda de consulta."),
        ("¿Por qué el Balance bloquea rangos de más de un año?",
         "Por norma contable (ratificada con MJ el 22/10): las cuentas de gasto e ingreso se saldan al 31 de diciembre. Para evoluciones históricas multi-año se utiliza el Libro Mayor; el Balance opera estrictamente por ejercicio fiscal."),
    ]

    table_faq = doc.add_table(rows=len(faq_data) + 1, cols=2)
    table_faq.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_faq.autofit = False

    # Header row
    hdr_cells = table_faq.rows[0].cells
    hdr_cells[0].width = Inches(2.3)
    hdr_cells[1].width = Inches(4.6)
    set_cell_background(hdr_cells[0], "1B365D")
    set_cell_background(hdr_cells[1], "1B365D")
    set_cell_margins(hdr_cells[0], 100, 100, 120, 120)
    set_cell_margins(hdr_cells[1], 100, 100, 120, 120)

    for i, h_text in enumerate(["Pregunta Esperada", "Respuesta Técnica y de Negocio"]):
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (q, a) in enumerate(faq_data):
        row_cells = table_faq.rows[idx + 1].cells
        row_cells[0].width = Inches(2.3)
        row_cells[1].width = Inches(4.6)
        bg = "F8FAFC" if idx % 2 == 0 else "FFFFFF"
        set_cell_background(row_cells[0], bg)
        set_cell_background(row_cells[1], bg)
        set_cell_margins(row_cells[0], 80, 80, 120, 120)
        set_cell_margins(row_cells[1], 80, 80, 120, 120)

        pq = row_cells[0].paragraphs[0]
        pq.paragraph_format.space_after = Pt(0)
        rq = pq.add_run(q)
        rq.font.name = "Segoe UI"
        rq.font.size = Pt(9)
        rq.font.bold = True
        rq.font.color.rgb = dark_text

        pa = row_cells[1].paragraphs[0]
        pa.paragraph_format.space_after = Pt(0)
        ra = pa.add_run(a)
        ra.font.name = "Segoe UI"
        ra.font.size = Pt(9)
        ra.font.color.rgb = dark_text

    # CHECKLIST CIERRE
    p_close_title = doc.add_paragraph()
    p_close_title.paragraph_format.space_before = Pt(16)
    p_close_title.paragraph_format.space_after = Pt(4)
    r_close = p_close_title.add_run("10. Acuerdos de Cierre de la Sesión")
    r_close.font.name = "Segoe UI"
    r_close.font.size = Pt(13)
    r_close.font.bold = True
    r_close.font.color.rgb = primary_color

    add_checklist_item("ACC-01", "Creación de Usuarios Reales", "Validar con MJ la nómina de usuarios reales de abastecimiento y contabilidad para crearlos en vivo en el sistema.")
    add_checklist_item("ACC-02", "Cartola Real Quincenal", "Pedir a Lupe una cartola reciente de octubre para realizar un ejercicio guiado de carga real.")
    add_checklist_item("ACC-03", "Archivo Muestra de Acepta", "Solicitar a Fran un export de guías de Acepta para calibrar el importador masivo.")
    add_checklist_item("ACC-04", "Minuta y Acta de Pase a Producción", "Tomar nota de refinamientos menores y formalizar la aceptación de los módulos contabilidad y tesorería.")

    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    out = r"e:\source\repos\Almahue\docs\Checklist-Presentacion-ERP-Almahue-2026-10-26.docx"
    create_document(out)
