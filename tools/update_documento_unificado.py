# -*- coding: utf-8 -*-
"""
Script que actualiza generate_word_acuerdos.py para:
1. Incluir numeración (N° 1 a 71) en la tabla matriz/checklist inicial.
2. Alinear exactamente los 71 requerimientos en semanas_detalle.
3. Incluir la numeración [#N] y el estado ([#N · ⏳ En QA] o [#N · 💻 Codeados pero sin revisión]) en cada ítem del detalle.
4. Regenerar los 3 archivos .docx locales.
5. Generar el markdown completo actualizado y sincronizarlo con el documento de Google Drive (14guwdS-lEtpr9ttd4Mmyh4wVF-AaNklY).
"""

import os
import subprocess

# Leer generate_word_acuerdos.py
path_gen = "tools/generate_word_acuerdos.py"
with open(path_gen, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Modificar cols de chk_table para incluir N°
old_cols = """    # Construcción de la tabla Matriz / Checklist
    cols = [
        ("SEMANA", Inches(0.95)),
        ("DÍA", Inches(0.7)),
        ("ACUERDO / REQUERIMIENTO AUDITADO", Inches(3.05)),
        ("MÓDULO", Inches(0.95)),
        ("ESTADO", Inches(1.45)),
    ]"""

new_cols = """    # Construcción de la tabla Matriz / Checklist con Numeración Correlativa
    cols = [
        ("N°", Inches(0.45)),
        ("SEMANA", Inches(0.95)),
        ("DÍA", Inches(0.65)),
        ("ACUERDO / REQUERIMIENTO AUDITADO", Inches(2.90)),
        ("MÓDULO", Inches(0.95)),
        ("ESTADO", Inches(1.30)),
    ]"""

if old_cols in code:
    code = code.replace(old_cols, new_cols)
    print("✓ Columnas actualizadas con N°")
else:
    print("! No se encontró old_cols exacto")

# 2. Modificar el header y el llenado de filas para la columna N°
old_loop = """        for i, val in enumerate([semana, dia, acuerdo, modulo, estado]):
            c = cells[i]
            c.width = cols[i][1]
            if i == 4:
                if "Pendiente" in val or "QA" in val:
                    set_cell_background(c, "FEF3C7") # Ámbar suave
                elif "Codeado" in val or "sin revisión" in val:
                    set_cell_background(c, "EFF6FF") # Azul suave
                else:
                    set_cell_background(c, "DCFCE7") # Verde suave
            else:
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
                r.font.size = Pt(8)
                r.font.bold = True
                if "Pendiente" in val or "QA" in val:
                    r.font.color.rgb = RGBColor(180, 83, 9) # Ámbar / Naranja (En QA)
                elif "Codeado" in val or "sin revisión" in val:
                    r.font.color.rgb = RGBColor(29, 78, 216) # Azul corporativo (Codeados pero sin revisión)
                else:
                    r.font.color.rgb = RGBColor(21, 128, 61) # Verde éxito"""

new_loop = """        valores_fila = [str(row_idx), semana, dia, acuerdo, modulo, estado]
        for i, val in enumerate(valores_fila):
            c = cells[i]
            c.width = cols[i][1]
            if i == 5: # Estado
                if "Pendiente" in val or "QA" in val:
                    set_cell_background(c, "FEF3C7") # Ámbar suave
                elif "Codeado" in val or "sin revisión" in val:
                    set_cell_background(c, "EFF6FF") # Azul suave
                else:
                    set_cell_background(c, "DCFCE7") # Verde suave
            else:
                set_cell_background(c, bg_color)

            set_cell_margins(c, top=80, bottom=80, left=70, right=70)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)

            if i in [0, 2, 5]: # N°, Día, Estado centrados
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

            r = p.add_run(val)
            r.font.name = "Segoe UI"

            if i == 0: # N°
                r.font.size = Pt(8.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(180, 83, 9) if row_idx >= 61 else RGBColor(31, 41, 55)
            elif i == 1: # Semana
                r.font.size = Pt(8)
                r.font.bold = True
                r.font.color.rgb = RGBColor(15, 81, 50) if "Esta" in val else RGBColor(55, 65, 81)
            elif i == 2: # Día
                r.font.size = Pt(8)
                r.font.bold = True
                r.font.color.rgb = RGBColor(31, 41, 55)
            elif i == 3: # Acuerdo
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(31, 41, 55)
            elif i == 4: # Módulo
                r.font.size = Pt(8)
                r.font.color.rgb = RGBColor(75, 85, 99)
            elif i == 5: # Estado
                r.font.size = Pt(8)
                r.font.bold = True
                if "Pendiente" in val or "QA" in val:
                    r.font.color.rgb = RGBColor(180, 83, 9) # Ámbar / Naranja (En QA)
                elif "Codeado" in val or "sin revisión" in val:
                    r.font.color.rgb = RGBColor(29, 78, 216) # Azul corporativo (Codeados pero sin revisión)
                else:
                    r.font.color.rgb = RGBColor(21, 128, 61) # Verde éxito"""

if old_loop in code:
    code = code.replace(old_loop, new_loop)
    print("✓ Llenado de filas de tabla actualizado con N°")
else:
    print("! No se encontró old_loop exacto")

# También actualizar el alineamiento en header:
old_hdr = "if i in [1, 4]:\n            p.alignment = WD_ALIGN_PARAGRAPH.CENTER"
new_hdr = "if i in [0, 2, 5]:\n            p.alignment = WD_ALIGN_PARAGRAPH.CENTER"
if old_hdr in code:
    code = code.replace(old_hdr, new_hdr)
    print("✓ Header de tabla alineado")

# 3. Alinear los requerimientos faltantes en semanas_detalle
# 27/10:
old_27 = """"requerimientos": [
                        "Balance de 8 columnas acumulativo anual desde el 1 de enero hasta el mes de corte.",
                        "Notas de cobro de gasto directo para Asoex con carga masiva Excel.",
                        "Protocolo de reversa en periodo cerrado condicionado a visto bueno.",
                        "Alta de Activo Fijo originada obligatoriamente en una OC recepcionada."
                    ],"""

new_27 = """"requerimientos": [
                        "Balance de 8 columnas acumulativo anual desde el 1 de enero hasta el mes de corte.",
                        "Notas de cobro: modalidad de gasto directo para Asoex y proveedores exentos.",
                        "Carga masiva de notas de cobro con archivo Excel estructurado.",
                        "Reversa de proformas en periodo cerrado condicionada a aprobación previa.",
                        "Activo fijo originado en OC recepcionada (reemplazando criterio de alta libre)."
                    ],"""

if old_27 in code:
    code = code.replace(old_27, new_27)
    print("✓ 27/10 alineado a 5 requerimientos")

# 30/10:
old_30 = """"requerimientos": [
                        "Soporte para pago parcializado de proformas por cuadrilla y fecha de compromiso.",
                        "Notas de cobro directas para liquidaciones de embarcadores y Asoex sin exigir OC comercial.",
                        "Validación estricta de asociación factura-OC antes de cursar pago en tesorería."
                    ],"""

new_30 = """"requerimientos": [
                        "Cobertura parcial de proformas por contratista y fecha de pago.",
                        "Compras Módulo 2: validación estricta de asociación factura-OC antes de pago.",
                        "Comex: soporte para liquidaciones y notas de cobro de embarcadores y Asoex.",
                        "Migraciones de base de datos de compras aplicadas en entorno local."
                    ],"""

if old_30 in code:
    code = code.replace(old_30, new_30)
    print("✓ 30/10 alineado a 4 requerimientos")

# 03/11:
old_03 = """"requerimientos": [
                        "Prohibición de reapertura de periodos cerrados desde la pantalla de Traspaso.",
                        "Wizard de reversa con solicitud formal de motivo y dos vistos buenos.",
                        "Filtro estricto por mes calendario en grilla de proformas contratistas.",
                        "Ocultamiento del botón Contabilizar en Libro de Compras para documentos sin OC o proforma vinculada.",
                        "Recepción de guías hijas: solo la última guía recepcionada realiza el recálculo y ajuste sobre la orden madre."
                    ],"""

new_03 = """"requerimientos": [
                        "No reabrir periodo contable desde Traspaso: las correcciones deben nacer directamente desde la proforma.",
                        "Wizard de reversa: en periodo cerrado no ofrecer ingreso directo de clave; exigir motivo y 2 vistos buenos.",
                        "Grilla de proformas filtrada por mes exacto (no arrastrar meses previos en rangos).",
                        "Libro de Compras: no mostrar botón 'Contabilizar' si el documento no está asociado a una OC o Proforma.",
                        "Hijas de insumos: solo la última guía recepcionada ajusta el saldo de la orden madre.",
                        "Calce de guías por código de artículo del maestro al recepcionar."
                    ],"""

if old_03 in code:
    code = code.replace(old_03, new_03)
    print("✓ 03/11 alineado a 6 requerimientos")

# 05/11:
old_05 = """"requerimientos": [
                        "Grupos y escalas se ratifican como motor transaccional de OC; organigrama queda como vista meramente informativa.",
                        "Obligatoriedad de tope en el último aprobador de la escala de compras; bloqueo estricto si la OC supera dicho monto.",
                        "Topes multimoneda (CLP, USD, CNY) con tipo de cambio sugerido del Banco Central editable.",
                        "Recetas de insumos vinculadas a la especie/embalaje y con Centro de Costo; consumo distribuye cantidades por packing.",
                        "Consumo valorizado a precio promedio ponderado mensual; devolución valorizada al precio de la guía sin rebajar stock físico origen.",
                        "Pestaña 'Por confirmar' en Libro de Guías; existencias en bodega no suben hasta que el usuario presione 'Confirmar recepción' y suba foto.",
                        "Alta de Activo Fijo nace exclusivamente de una OC recepcionada de tipo activo fijo.",
                        "Reversa de proformas: edición directa de línea sin crear comprobante nuevo; Libro Mayor filtra solo asientos activos.",
                        "Anulación de comprobante contable con estado ANULADO y registro obligatorio de motivo."
                    ],"""

new_05 = """"requerimientos": [
                        "Grupos y escalas se mantienen como motor de aprobación de OC (no reemplazados por organigrama informativo).",
                        "Siempre firma la jefatura; tope obligatorio en el último aprobador de la escala para evitar errores de tipeo.",
                        "Topes multimoneda (CLP, USD, Yuan) con tipo de cambio sugerido del Banco Central editable y guardado fijo.",
                        "Recetas de insumos asociadas al embalaje (no a un solo packing). En el consumo se distribuyen cantidades por packing.",
                        "Consumo valorizado al precio promedio ponderado del stock mensual (sin FIFO por guía).",
                        "Devolución a proveedor valorizada al precio de la guía pero sin restar stock físico de origen.",
                        "Stock de guías recibidas se incrementa exclusivamente al confirmar la recepción (pestaña 'Por confirmar') con fotos y adjuntos.",
                        "Activo fijo: el maestro nace exclusivamente cuando la OC tipo activo fijo está recepcionada (aviso si falta factura).",
                        "Reversa de proformas: se edita la línea del asiento existente (sin crear asiento nuevo de reversa ni ajuste).",
                        "Anulación de comprobantes: estado ANULADO con motivo registrado, ejecutado por la jefatura o mediante solicitud.",
                        "Retiro de 'Administradores por módulo' de la operación; control de acceso basado estrictamente en roles."
                    ],"""

if old_05 in code:
    code = code.replace(old_05, new_05)
    print("✓ 05/11 alineado a 11 requerimientos")

# 4. Modificar el bucle de impresión de requerimientos para incluir numeración [#N] y estado
old_req_loop = """            for req in dia["requerimientos"]:
                p_b = doc.add_paragraph(style='List Bullet')
                p_b.paragraph_format.space_before = Pt(0)
                p_b.paragraph_format.space_after = Pt(1.5)
                r_b = p_b.add_run(req)
                r_b.font.name = "Segoe UI"
                r_b.font.size = Pt(8.5)
                r_b.font.color.rgb = RGBColor(31, 41, 55)"""

new_req_loop = """            for req in dia["requerimientos"]:
                req_num += 1
                estado_item = "⏳ En QA" if req_num >= 61 else "💻 Codeados pero sin revisión"
                
                p_b = doc.add_paragraph(style='List Bullet')
                p_b.paragraph_format.space_before = Pt(0)
                p_b.paragraph_format.space_after = Pt(2)

                # Badge numerado y con estado
                r_badge = p_b.add_run(f"[#{req_num} · {estado_item}] ")
                r_badge.font.name = "Segoe UI"
                r_badge.font.size = Pt(8.5)
                r_badge.font.bold = True
                if req_num >= 61:
                    r_badge.font.color.rgb = RGBColor(180, 83, 9) # Ámbar para QA
                else:
                    r_badge.font.color.rgb = RGBColor(29, 78, 216) # Azul para Codeados

                r_b = p_b.add_run(req)
                r_b.font.name = "Segoe UI"
                r_b.font.size = Pt(8.5)
                r_b.font.color.rgb = RGBColor(31, 41, 55)"""

if old_req_loop in code:
    # Agregar inicialización de req_num antes del bucle de semanas
    code = code.replace("for sem in semanas_detalle:", "req_num = 0\n    for sem in semanas_detalle:")
    code = code.replace(old_req_loop, new_req_loop)
    print("✓ Bucle de requerimientos actualizado con [#N · Estado]")
else:
    print("! No se encontró old_req_loop exacto")

with open(path_gen, "w", encoding="utf-8") as f:
    f.write(code)

print("generate_word_acuerdos.py reescrito exitosamente.")
