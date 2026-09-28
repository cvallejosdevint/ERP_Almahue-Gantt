# -*- coding: utf-8 -*-
"""Genera el paquete de toma de requisitos (Word) desde el análisis de transcripciones."""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = Path(__file__).resolve().parent


def set_run_font(run, size=11, bold=False, color=None):
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        set_run_font(run, size={1: 18, 2: 14, 3: 12}.get(level, 11), bold=True)
    return p


def p(doc, text, *, bold=False, italic=False, size=11):
    para = doc.add_paragraph()
    run = para.add_run(text)
    set_run_font(run, size=size, bold=bold)
    run.italic = italic
    para.paragraph_format.space_after = Pt(8)
    return para


def quote(doc, text, attrib=""):
    para = doc.add_paragraph()
    run = para.add_run("«" + text + "»")
    set_run_font(run, size=11)
    run.italic = True
    if attrib:
        r2 = para.add_run("  — " + attrib)
        set_run_font(r2, size=10)
    para.paragraph_format.left_indent = Cm(0.75)
    para.paragraph_format.space_after = Pt(8)


def bullets(doc, items):
    for it in items:
        para = doc.add_paragraph(it, style="List Bullet")
        for run in para.runs:
            set_run_font(run, size=11)


def table(doc, headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = ""
        run = cell.paragraphs[0].add_run(h)
        set_run_font(run, size=10, bold=True)
    for r, row in enumerate(rows, start=1):
        for c, val in enumerate(row):
            cell = t.rows[r].cells[c]
            cell.text = ""
            run = cell.paragraphs[0].add_run(str(val))
            set_run_font(run, size=10)
    doc.add_paragraph()


def new_doc(title, subtitle):
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(1.8)
        section.bottom_margin = Cm(1.8)
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)
    h = doc.add_paragraph()
    r = h.add_run("TOMA DE REQUISITOS — PROYECTO ERP ALMAHUE")
    set_run_font(r, size=10, bold=True, color=(0x2E, 0x5A, 0x3C))
    h.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_heading(doc, title, 1)
    p(doc, subtitle, italic=True, size=11)
    p(
        doc,
        "Clasificación de voces: cliente (Agustín, MJ/María José/María Jesús, Lupe, Mario, Fran, Rodrigo) "
        "= requisito o as-is. Proveedor (Carlos Vallejos, Sergio / Devint) = hipótesis o propuesta. "
        "Minutas IA = índice, no evidencia. Transcripción verbatim = fuente primaria.",
        size=10,
        italic=True,
    )
    return doc


def save(doc, name):
    path = OUT / name
    doc.save(path)
    print("OK", path.name)


def doc_metodologia():
    d = new_doc(
        "00 — Metodología y catálogo de fuentes",
        "Paquete generado el 04/09/2026. Rol: analista de requisitos. No es diseño de software ni alcance de código.",
    )
    add_heading(d, "1. Propósito", 2)
    p(
        d,
        "Dejar registro formal de lo que el cliente mostró del sistema actual (Agrosoft) y de lo que pidió, "
        "antes de decidir desarrollo. El ERP nuevo se construyó en gran parte copiando pantallas de Agrosoft/AgroSmart; "
        "este paquete vuelve a la evidencia de las reuniones.",
    )
    add_heading(d, "2. Cómo se lee una reunión", 2)
    bullets(
        d,
        [
            "¿Había cliente en la sala? Si no, el documento se etiqueta INTERNA y no genera requisitos.",
            "¿Es recorrido de Agrosoft o demo del ERP nuevo? Solo el primero es as-is directo.",
            "Timestamps Reu1–Reu5: la marca de la transcripción está inflada ≈10×. Tiempo real ≈ marca ÷ 10.",
            "Reu6 y agosto: timestamps en tiempo real (salvo 28/08, sin marcas).",
            "Una pregunta cerrada del proveedor («¿cierto?») + «sí» del cliente = confirmación, no pedido espontáneo.",
        ],
    )
    add_heading(d, "3. Catálogo de reuniones", 2)
    table(
        d,
        ["Cód.", "Fecha", "Cliente en sala", "Tipo", "Transcripción", "Video / nota"],
        [
            ["R1", "21/07/2026", "MJ (casi cierta)", "AS-IS Agrosoft", "fuentes/transcripcion.md", "Screen Recording 2026-07-21 120114.mp4 · tl;dv 6a60394d"],
            ["R2", "23/07/2026", "MJ + Rodrigo", "AS-IS Agrosoft + AgroSmart", "transcripcion-reunion2.md", "fuentes/videos/reunion2-2026-07-23.mp4"],
            ["R3", "28/07/2026", "MJ", "Demo ERP nuevo + as-is filtrado", "transcripcion-reunion3.md", "fuentes/videos/reunion3-2026-07-28.mp4"],
            ["R4", "30/07/2026", "Solo MJ (Sigrid muda)", "Demo ERP + as-is contab/tesorería", "transcripcion-reunion4.md", "Usar minuta tl;dv para minutos reales"],
            ["R5", "03/08/2026", "NINGUNO", "INTERNA proveedor", "transcripcion-reunion5.md", "No es fuente de requisitos"],
            ["R6", "06/08/2026", "MJ + Agustín", "Demo avance + requisitos", "transcripcion-reunion6.md", "≈66 min, reloj real"],
            ["A19", "19/08/2026", "NINGUNO", "INTERNA demo", "transcripcion-2026-08-19-demo-interno.md", "Screen Recording 2026-08-19 162555.mp4"],
            ["A20a", "20/08 mañana", "NINGUNO", "INTERNA agenda", "transcripcion-2026-08-20-reunion-sergio.md", "Screen Recording 2026-08-20 105836.mp4"],
            ["A20b", "20/08 tarde", "Lupe + Mario", "Operativo compras/tesorería/ventas", "transcripcion-2026-08-20-tarde-lupe-mario.md", "Screen Recording 2026-08-20 174935.mp4"],
            ["T28", "28/08/2026", "MJ + Lupe (+ Mario tarde)", "AS-IS tesorería Agrosoft", "transcripcion-2026-08-28-tesoreria-mj-lupe.md", "Sin timestamps; Carlos sin audio"],
            ["GS", "ago/2026", "MJ + Mario", "Onboarding GoSocket", "transcripcion-reunion-gosocket-qa.md", "≈31 min"],
            ["K01", "01/09/2026", "MJ no se conectó", "Mesa API GoSocket (minuta)", "reunion-2026-09-01-gosocket-kickoff.md", "No verbatim"],
            ["I03", "03/09 ~14:42", "NINGUNO", "INTERNA Carlos–Sergio", "transcripcion-2026-09-03-interna-carlos-sergio.md", "20260903-1442…mp4 CON audio"],
            ["V03", "03/09 ~19:54", "Sin confirmar", "Grabación pantalla", "NO HAY (pista de audio VACÍA)", "Desktop/Nueva carpeta/20260903-1954…mp4"],
            ["V03b", "03/09 ~23:31", "Sin transcribir", "Grabación con audio", "Pendiente Whisper", "20260903-2331…mp4 CON audio ≈44 min"],
        ],
    )
    add_heading(d, "4. Limitaciones de este paquete", 2)
    bullets(
        d,
        [
            "No se re-vieron frame a frame todos los MP4; el as-is sale de transcripciones + análisis ya leídos íntegros.",
            "El video 19:54 del 03/09 no es recuperable (contenedor con pista AAC de 0 bytes).",
            "Diarización ASR rota en Reu1, Reu5 y 28/08: hay citas con atribución dudosa, marcadas.",
            "Este paquete no decide alcance de producto. Deja hallazgos y preguntas abiertas.",
        ],
    )
    save(d, "00-Metodologia-y-catalogo-fuentes.docx")


def doc_r1():
    d = new_doc(
        "R1 — 21/07/2026 · Recorrido Agrosoft (MJ)",
        "Única reunión que recorre el sistema en producción módulo por módulo. Nunca tuvo minuta IA.",
    )
    add_heading(d, "Ficha", 2)
    table(
        d,
        ["Campo", "Detalle"],
        [
            ["Fuente", "fuentes/transcripcion.md"],
            ["Video", "c:\\Users\\c\\Videos\\Screen Recordings\\Screen Recording 2026-07-21 120114.mp4"],
            ["Cliente", "Speaker 00 ≈ MJ (admin). Habla de «María Jesús» en tercera y de Agustín/Mario ausentes."],
            ["Proveedor", "Speaker 01 ≈ Carlos Vallejos"],
            ["Carácter", "AS-IS directo. Se crea OC 5207 en vivo «para después eliminarla»."],
            ["Reloj", "Marcas raw; factor ÷10 plausible (≈1 h 56 min) no anclado al 100%."],
        ],
    )
    add_heading(d, "Hallazgos AS-IS (Agrosoft)", 2)
    add_heading(d, "Acceso y multiempresa", 3)
    bullets(
        d,
        [
            "Queda en la última empresa; al cambiar pide mes contable y mes de remuneración.",
            "15 usuarios contratados; a veces 2 personas comparten usuario → siguen cargando en la empresa equivocada.",
            "Fuga de contexto: centros de costo, distribución de OC y bodegas muestran datos de OTRA empresa.",
            "Cambio de temporada existe pero «no sirve mucho» porque no usan el módulo de gestión; igual lo quieren en el ERP nuevo.",
        ],
    )
    add_heading(d, "Módulos que NO usan", 3)
    bullets(
        d,
        [
            "Mano de obra / liquidaciones: trabajan remuneraciones en BUK (ASR: «Book»). Labores/actividades quieren parametrizarlas en Contratistas.",
            "Solicitud de compra: van directo a OC.",
            "Maquinaria y Gestión: no relevantes en la demo.",
        ],
    )
    add_heading(d, "Compras — el proceso real está invertido", 3)
    quote(
        d,
        "se emite la factura y después creamos la orden de compra… en la observación ponemos factura tanto",
        "MJ, Reu1",
    )
    bullets(
        d,
        [
            "OC: departamento, solicitante, jefe que aprueba (Juan Agustín), proveedor, plazo, moneda, TC, tipo (servicio/existencia/AF), distribución CC.",
            "TC que muestra el sistema «después no lo reconoce»; el costo se reconoce a la fecha de recepción.",
            "Distribución: tres modos; usan DIRECTO. Descuadre 1010 vs 1000 se avisa solo al guardar.",
            "Estados de informe: anulada, aprobada, cerrada, contabilizada, pendiente, recepción parcial/total. Sin el estado no se encuentra.",
            "Aprobación: el jefe ve la bandeja; NO hay correo. Piden badge/pendientes, no mail masivo.",
            "Recepción: solo fecha → asiento gasto vs facturas por recibir (ej. comprobante 8310, OC 5207).",
            "Maestro de artículos duplicado Compras/Insumos; no valida duplicados (bolsas × N rompe el mayor de stock).",
        ],
    )
    add_heading(d, "Contratistas", 3)
    bullets(
        d,
        [
            "Tarifario: no hay listado; al ingresar otro registro «borra» la vista anterior.",
            "Cierre: cada contrato una factura; no cierra el módulo si falta asociación.",
            "Asiento: costo / facturas por recibir contratistas; traspaso pide TC; digitador no cierra mes.",
        ],
    )
    add_heading(d, "Requisitos / dolores explícitos", 2)
    bullets(
        d,
        [
            "Mantener pasos de aprobación y recepción aunque hoy la OC sea a posteriori (ideal: cada depto cree su OC).",
            "Aviso de pendientes de aprobación (icono), no correo por cada OC.",
            "Aislar maestros y bodegas por empresa.",
            "Un solo maestro de artículos en Insumos, con control de duplicados.",
        ],
    )
    add_heading(d, "Preguntas abiertas", 2)
    bullets(
        d,
        [
            "¿El ERP debe imponer OC-antes-de-factura (cambio de proceso) o soportar el as-is (factura primero)? Nadie lo declaró como cambio formal.",
        ],
    )
    save(d, "R1-2026-07-21-Agrosoft-recorrido.docx")


def doc_r2():
    d = new_doc(
        "R2 — 23/07/2026 · Agrosoft + AgroSmart (MJ, Rodrigo)",
        "Ciclo contratistas end-to-end, tesorería, libro de ventas y migración Acepta→GoSocket.",
    )
    add_heading(d, "Ficha", 2)
    table(
        d,
        ["Campo", "Detalle"],
        [
            ["Fuente", "fuentes/transcripcion-reunion2.md"],
            ["Video", "fuentes/videos/reunion2-2026-07-23.mp4 · tl;dv 6a624d3f"],
            ["Cliente", "Rodrigo (contable agrícola) demuestra; MJ («Mari») cierra"],
            ["Proveedor", "Carlos Vallejos (graba)"],
            ["Duración", "≈ 1 h 20 min (raw ÷10)"],
            ["Minuta IA", "Stub 1 KB; no usar."],
        ],
    )
    add_heading(d, "Ciclo contratistas (demostrado)", 2)
    bullets(
        d,
        [
            "1. Contrato (tipo mano de obra, faena, fechas) → folio anotado a mano (ej. 179).",
            "2. Enrolamiento personal + jefe de cuadrilla.",
            "3. Control de producción diario: reingresar fecha/faena/jefe; actividad↔labor invertida (hay que saberse la actividad de memoria).",
            "4. Precio viene del tarifario y NO se edita en el día — pero el precio real a menudo se conoce DESPUÉS del trabajo.",
            "5. Proforma: borrador vs definitivo (el definitivo dispara el proceso sin filtro). Se envía al contratista para que facture.",
            "6. Asociación proforma↔factura (tipo compra = contratista). Duro: UNA proforma por mes; dos meses en una factura no se asocian.",
            "Workaround: meten todo en un mes y llevan un segundo registro fuera del sistema → distorsiona gestión mensual.",
        ],
    )
    quote(
        d,
        "cuando empezamos a hacer las proformas… no alcanzamos a hacer una en todo un día de trabajo porque es muy largo",
        "Rodrigo",
    )
    add_heading(d, "AgroSmart (referencia UX, no el ERP destino)", 2)
    p(
        d,
        "Evaluaron migrar por contratistas; abandonaron por contabilidad «descuadrada». Siguen con acceso. "
        "Lo que sí quieren copiar: ingreso múltiple de labores, tarifario editable en el día, y pantalla de labores "
        "no asociadas para armar la proforma (calce contra factura).",
    )
    quote(
        d,
        "nosotros hacemos la proforma primero… ver todas las labores anotadas y decir esta, esta, esta, hago una proforma",
        "Rodrigo",
    )
    add_heading(d, "Tesorería y GoSocket (as-is + intención)", 2)
    bullets(
        d,
        [
            "Calce pago/factura; diferencia de TC en pesos vs dólares (demostrado).",
            "MJ: la idea de GoSocket conectado al ERP es que «nos aparezca el libro de compras en línea y podamos contabilizar directo» — recepción, no solo emisión.",
            "Facturador histórico: Acepta.",
        ],
    )
    save(d, "R2-2026-07-23-Agrosoft-AgroSmart.docx")


def doc_r3():
    d = new_doc(
        "R3 — 28/07/2026 · Demo ERP nuevo con MJ",
        "NO es recorrido de Agrosoft. El as-is aparece cuando MJ dice «actualmente nosotros…». El ERP se reconoció como calco de AgroSmart/Agrosoft.",
    )
    add_heading(d, "Ficha", 2)
    table(
        d,
        ["Campo", "Detalle"],
        [
            ["Fuente", "transcripcion-reunion3.md"],
            ["Video", "fuentes/videos/reunion3-2026-07-28.mp4"],
            ["Cliente", "Solo MJ"],
            ["Proveedor", "Carlos"],
            ["Duración", "≈ 58 min"],
        ],
    )
    add_heading(d, "AS-IS que declara MJ", 2)
    bullets(
        d,
        [
            "Roles administrativos vs operativos; usuarios por empresa.",
            "Contabilizar documento: cuenta, centro de costo, glosa, cliente.",
            "Devolución = salida proveedor.",
            "Plan de cuentas por niveles.",
        ],
    )
    add_heading(d, "Requisitos / comentarios de cliente sobre el ERP nuevo", 2)
    bullets(
        d,
        [
            "Aprobación de proformas con control (incluye re-aprobar si se edita y ver quién aprobó) — pedido explícito de MJ en esta reunión.",
            "Renombrar «Libro comercial» → «Libro de ventas» (la minuta IA lo omitió).",
            "Contraseña: poder visualizarla al escribir (hallazgo de UX).",
        ],
    )
    add_heading(d, "Riesgo documental", 2)
    p(
        d,
        "La minuta IA borra al hablante y convierte preguntas abiertas en hechos. Cualquier «decisión R3» debe re-leerse en la transcripción.",
    )
    save(d, "R3-2026-07-28-demo-ERP-MJ.docx")


def doc_r4():
    d = new_doc(
        "R4 — 30/07/2026 · Contabilidad y tesorería (solo MJ)",
        "Sin Agustín ni Mario (vacaciones). Sigrid asiste por Mario y no habla. Todo requisito = MJ.",
    )
    add_heading(d, "Ficha", 2)
    table(
        d,
        ["Campo", "Detalle"],
        [
            ["Fuente", "transcripcion-reunion4.md"],
            ["Reloj", "Marca transcripción ≈10×; navegar el video con minuta tl;dv"],
            ["Cliente", "MJ"],
            ["Proveedor", "Carlos (conduce) + Sergio (entra tarde)"],
        ],
    )
    add_heading(d, "AS-IS Agrosoft — Contabilidad", 2)
    bullets(
        d,
        [
            "Plan de cuentas de 5 niveles; exportable a Excel.",
            "Cada módulo parametriza «todo lo que uno cree».",
            "Trabajan con el MAYOR, casi no con el diario. El mayor se parece a un balance de 8 columnas.",
            "Contabilidad electrónica: SÍ, se sube UNA vez al año con la renta (contador externo), no mensual.",
            "Honorarios: factor escalonado hacia 20% de retención.",
            "Cierres de periodo POR MÓDULO (contabilidad, contratistas, insumos), no un cierre global.",
            "No existe un «panel SII» como el que mostró el proveedor; sí «una parte de configuración de las cuentas».",
        ],
    )
    add_heading(d, "AS-IS Agrosoft — Tesorería (MJ opera en vivo)", 2)
    bullets(
        d,
        [
            "Procesos diarios proveedores y clientes.",
            "Flujo: banco → código financiero (flujo de caja) → proveedor por RUT → factura → nº transacción cartola → grabar.",
            "Asiento automático: banco vs proveedor, en peso y dólar al TC del día.",
            "Hoy el nº de transacción se digita y «siempre ponen 1»; debería ser el nº real de cartola.",
        ],
    )
    add_heading(d, "Hallazgo de método: Config SII", 2)
    quote(
        d,
        "tenemos este panel configurable del SII… fue ideado por parte del equipo de desarrollo… este no lo utilizaban ustedes",
        "Carlos (proveedor)",
    )
    p(
        d,
        "MJ: no lo usaban, pero sí hay configuración de cuentas. Sergio objeta asociar cuenta a TIPO de documento si ya va por línea. "
        "Carlos: «entonces lo conservamos». La minuta IA vendió la objeción de Sergio como requisito. "
        "Conservar un panel ideado por desarrollo ≠ el cliente pidió construirlo.",
    )
    save(d, "R4-2026-07-30-contabilidad-tesoreria-MJ.docx")


def doc_r5():
    d = new_doc(
        "R5 — 03/08/2026 · INTERNA (sin cliente)",
        "Carlos ↔ Sergio. CERO requisitos de cliente. No citar como pedido de Almahue.",
    )
    add_heading(d, "Ficha", 2)
    bullets(
        d,
        [
            "Duración ≈ 42 min (reloj ÷10).",
            "Lo que se muestra es producto Devint / otros clientes, no Agrosoft.",
            "Cuando Carlos dice «como lo pidió Mari» es testimonio de segunda mano de R3/R4.",
            "La minuta IA invierte frases (p. ej. «SAI/SII necesario para GoSocket» cuando el verbatim habla de PIN).",
        ],
    )
    add_heading(d, "Uso permitido", 2)
    p(d, "Bitácora interna de diseño del proveedor. No entra al backlog de cliente ni al AS-IS de Agrosoft.")
    save(d, "R5-2026-08-03-INTERNA-sin-cliente.docx")


def doc_r6():
    d = new_doc(
        "R6 — 06/08/2026 · Demo con Agustín y MJ",
        "Primera sesión con gerencia. Mario y Lupe presentes casi sin hablar. Reloj real ≈ 66 min.",
    )
    add_heading(d, "AS-IS que declara el cliente", 2)
    table(
        d,
        ["Tema", "Quién", "Síntesis"],
        [
            ["Plan de cuentas", "MJ", "Por cuenta: CC, elemento, área de negocio, flags activo/inactivo"],
            ["Trazabilidad usuarios", "MJ", "Quién crea/modifica; mantenerlo"],
            ["Clave de reversa", "MJ", "Algunos paneles piden clave para reversar/eliminar"],
            ["Ventas", "MJ", "Hoy se emiten FUERA del ERP, en el facturador; «ya saben lo que van a vender»"],
            ["Cotizaciones", "MJ", "A su criterio son para COMPRAS, no para vender"],
            ["Datos bancarios", "Agustín", "Hoy se buscan en el correo; riesgo de estafa por cambio de cuentas"],
            ["Temporadas", "Agustín", "Cuenta «gastos próxima temporada»; admin traspasa cuenta por cuenta"],
            ["Stock", "MJ", "Tránsito solo en bodega; la venta exige stock real"],
            ["Aprobaciones", "Agustín", "Organigrama informal; él termina aprobando «sin sentido»"],
            ["DTE", "MJ", "Histórico Acepta; nuevo GoSocket (Pablo)"],
        ],
    )
    add_heading(d, "Pedidos / comentarios a no distorsionar", 2)
    bullets(
        d,
        [
            "Cotización: MJ pide que «esté en el panel de compras» — MOVER, no necesariamente borrar el concepto.",
            "Precio piso ventas (luego D16): Sergio propone asociar precio de compra en el mantenedor; MJ: «si se puede, ideal».",
            "Alcance de aprobaciones en esta sala: incluye conversación comercial; no es «solo compras».",
        ],
    )
    add_heading(d, "Calidad de fuente", 2)
    p(d, "Diarización mezcla turnos. Hay fragmentos ASR corruptos que no deben citarse. Ver analisis-reuniones/04-reu5-reu6.md.")
    save(d, "R6-2026-08-06-Agustin-MJ.docx")


def doc_agosto():
    d = new_doc(
        "19–20/08/2026 · Internas + sesión Lupe/Mario",
        "Dos internas sin cliente y una operativa de tarde. Las internas no generan requisitos.",
    )
    add_heading(d, "19/08 — demo interno (sin cliente)", 2)
    p(d, "Estado del producto: OV con cadena de aprobación viva, PIN, error de folios. El propio equipo admite que Mario «va a preguntar» y que no hay feedback operativo esa semana.")
    add_heading(d, "20/08 mañana — interna Sergio (sin cliente)", 2)
    p(d, "Se arma la lista de preguntas para la tarde. No es requisito.")
    add_heading(d, "20/08 tarde — Lupe y Mario (cliente operativo)", 2)
    bullets(
        d,
        [
            "Compras: Lupe — «nosotros solamente nos piden la orden de compra y nosotros solo generamos la orden de compra».",
            "Ventas: hay confirmaciones a preguntas CERRADAS sobre no aprobar OV (Lupe/Mario). No estaba MJ. Peso menor que R6.",
            "Proforma / contratista / labor / jornal: 0 menciones en las tres transcripciones del 19–20/08.",
            "Tesorería operativa: foco en lo que Lupe usa día a día.",
        ],
    )
    add_heading(d, "Conflicto de alcance a registrar", 2)
    p(
        d,
        "Si se usa esta sesión para apagar aprobaciones de OV o borrar proformas, hay que dejar constancia de que "
        "choca con pedidos de MJ (R3 proformas, R6 cotización en compras / alcance comercial) y que fueron respuestas a preguntas cerradas.",
    )
    save(d, "A19-A20-2026-08-internas-y-Lupe-Mario.docx")


def doc_t28():
    d = new_doc(
        "T28 — 28/08/2026 · Tesorería (MJ, Lupe)",
        "Sesión más reciente con cliente sobre tesorería. MJ comparte Agrosoft. Sin timestamps (citar por línea de archivo).",
    )
    add_heading(d, "AS-IS que opera MJ/Lupe", 2)
    bullets(
        d,
        [
            "Cartola: HOY se DIGITA a mano. Quieren invertir: cargar archivo del banco y contabilizar ENCIMA de la cartola.",
            "Bancos: 2 instituciones, cuentas en peso, dólar y yuan (3–4 cuentas).",
            "Pago proveedor: elige documento pendiente → banco → código financiero (flujo de caja) → contabiliza → asiento banco↓ proveedor↓.",
            "Anticipos a productores (Lupe) y nómina de compromiso: no deben mutar el DTE.",
            "Pedido de MJ: «toda la contabilización del sistema tenga las 3 conversiones» (peso / dólar / yuan) — el mayor actual no lo modela.",
        ],
    )
    add_heading(d, "To-be tesorería (dicho por cliente)", 2)
    bullets(
        d,
        [
            "Importar cartola (no tipear).",
            "Ver saldo por banco y moneda (dólar y yuan explícitos).",
            "Contabilizar el movimiento de cartola como hecho oficial.",
        ],
    )
    save(d, "T28-2026-08-28-tesoreria-MJ-Lupe.docx")


def doc_gosocket():
    d = new_doc(
        "GoSocket — onboarding QA + kickoff 01/09",
        "Tercero (Pablo Rodriguez). No redefine el negocio de Almahue; define enrolamiento, CAF, API y campos del DTE.",
    )
    add_heading(d, "Sesión QA (verbatim, MJ + Mario + Carlos)", 2)
    bullets(
        d,
        [
            "Portal sandbox, certificado, CAF/folios, API keys, lectura de errores, PDF.",
            "ASR: Cuba=QA, CUAA=CAF, IO Faktura=IOFactura.",
        ],
    )
    add_heading(d, "Kickoff 01/09 (minuta, MJ ausente)", 2)
    p(d, "Mesa API: BillerId, DefaultCertificate, resolución SII (CAE). Sin cliente → no es requisito de negocio; es contrato técnico del facturador.")
    add_heading(d, "Intención de negocio (viene de R2, no de esta mesa)", 2)
    p(d, "MJ quería libro de COMPRAS en línea (recepción) + contabilizar. La mesa se centró en EMISIÓN. Registrar la asimetría.")
    save(d, "GS-GoSocket-QA-y-kickoff.docx")


def doc_sep03():
    d = new_doc(
        "03/09/2026 · Videos de pantalla y sesión interna",
        "Tres MP4 en el escritorio. Solo uno está transcrito. Uno no tiene audio.",
    )
    add_heading(d, "Inventario de video", 2)
    table(
        d,
        ["Archivo", "Audio", "Qué es"],
        [
            ["20260903-1442…mp4 ≈28 min", "SÍ (AAC con frames)", "Interna Carlos–Sergio. Transcripción: transcripcion-2026-09-03-interna-carlos-sergio.md. Revisión OV/DTE/folio/SMTP."],
            ["20260903-1954…mp4 ≈55 min", "NO (pista 0 bytes)", "No se puede transcribir. Notas manuscritas del analista (abajo)."],
            ["20260903-2331…mp4 ≈44 min", "SÍ, sin transcribir", "Pendiente de Whisper. No usar hasta tener verbatim."],
        ],
    )
    add_heading(d, "Notas en caliente del analista (19:54) — NO son verbatim", 2)
    p(d, "Se registran para no perder la pista. Confirmar con quien estuvo o con el video 23:31 cuando se transcriba.")
    bullets(
        d,
        [
            "Libro de ventas: estado «por contabilizar» + asociar cuenta antes de contabilizar.",
            "Corrección de montos: amarrar factura origen y detalle de líneas.",
            "Validar envío GoSocket de venta exportación (COMEX).",
            "Cálculo de cajas → monto en peso y en dólar.",
            "En COMEX ignorar precio de bodega.",
            "Factura en el periodo de la sesión; notificar si no es el periodo actual.",
            "Formato montos: decimales con coma, miles con punto.",
            "SIN confirmar: «realizar el monto de venta», anulación+correos, origen exacto del tipo de cambio.",
        ],
    )
    add_heading(d, "Interna 14:42 (Carlos–Sergio) — no requisito", 2)
    p(d, "Ajustes de UX de emisión (fecha vencimiento, grilla de ítems, facturar solo en Emitir, tracking de folio, SMTP). Hipótesis de proveedor.")
    save(d, "S03-2026-09-03-videos-y-notas.docx")


def doc_asis():
    d = new_doc(
        "AS-IS Agrosoft — cómo funciona hoy el negocio",
        "Síntesis de R1+R2 (recorrido) + R4 tesorería/contab + T28. No describe el ERP nuevo.",
    )
    add_heading(d, "1. Qué es Agrosoft en la práctica", 2)
    p(
        d,
        "Conjunto de módulos (mano de obra, contratistas, compras, insumos, maquinaria, contabilidad, gestión, parámetros). "
        "Contabilidad es el núcleo: centraliza proveedores, ventas, tesorería y activos. Cada satélite: parametrizar → operar el día → "
        "traspaso contable + cierre de mes → informes.",
    )
    add_heading(d, "2. Quién usa qué", 2)
    table(
        d,
        ["Módulo", "¿Lo usan?", "Dueño operativo (voz en reuniones)"],
        [
            ["Contabilidad / mayor", "Sí (corazón)", "MJ"],
            ["Compras / OC / registro factura", "Sí, a posteriori", "MJ / Lupe"],
            ["Tesorería (pagos, cartola)", "Sí", "MJ / Lupe"],
            ["Contratistas / proformas", "Sí, muy doloroso", "Rodrigo / MJ"],
            ["Insumos / bodega", "Sí", "MJ"],
            ["Ventas / DTE", "Fuera de Agrosoft (Acepta→GoSocket)", "MJ"],
            ["Mano de obra / liquidaciones", "No (BUK)", "—"],
            ["Solicitud de compra", "No", "—"],
            ["Maquinaria / Gestión", "No / poco", "—"],
        ],
    )
    add_heading(d, "3. Procesos (ver también 99-diagramas-flujo-agrosoft.mmd)", 2)
    add_heading(d, "3.1 Compras (como lo viven hoy)", 3)
    bullets(
        d,
        [
            "Teórico del software: Solicitud → OC → aprobación → recepción → factura.",
            "Real: llega/emite la FACTURA → Contabilidad arma la OC (anota el nº de factura en observación) → aprobación (bandeja, sin mail) → recepción (reconoce gasto al TC de esa fecha) → registro de compra / asiento.",
            "Desean que cada departamento cree su OC, pero piden conservar aprobación y recepción.",
        ],
    )
    add_heading(d, "3.2 Contratistas", 3)
    bullets(
        d,
        [
            "Tarifario (ciego, sin listado) → contrato → enrolar → labores diarias (precio a menudo desconocido) → proforma (mandante→contratista) → el contratista factura → asociación 1:1 mes → traspaso «facturas por recibir» → factura cierra contra proveedor.",
            "AgroSmart es el modelo mental deseado para armar la proforma desde labores pendientes.",
        ],
    )
    add_heading(d, "3.3 Ventas", 3)
    bullets(
        d,
        [
            "Saben qué vender; emiten en el FACTURADOR, no en Agrosoft.",
            "Cotizar para vender no es su práctica (MJ: cotizaciones = compras).",
            "Stock de venta = físico real; tránsito queda en bodega.",
        ],
    )
    add_heading(d, "3.4 Tesorería", 3)
    bullets(
        d,
        [
            "Pago: elige factura pendiente + banco + código financiero + nº cartola (hoy «1») → asiento banco/proveedor en CLP y USD.",
            "Cartola: digitada. Quieren importar el Excel/archivo del banco y contabilizar sobre esos movimientos.",
            "Multibanco y multimmoneda (CLP, USD, CNY).",
            "Pago puede llevar TC manual (negociado); el costo se reconoció otro día → diferencia estructural, peor en fruta/productor.",
        ],
    )
    add_heading(d, "3.5 Contabilidad", 3)
    bullets(
        d,
        [
            "5 niveles; dimensiones por cuenta (CC, elemento, área).",
            "Cierre por módulo.",
            "Electrónica anual (renta), no mensual.",
            "Pedido 28/08: tres conversiones en toda la contabilización — HOY el mayor de un ERP típico es monomoneda: es el hueco más grande.",
        ],
    )
    add_heading(d, "4. Dolores estructurales (para el expediente, no para el sprint)", 2)
    bullets(
        d,
        [
            "Multiempresa permeable (CC, bodegas, OC).",
            "Usuarios compartidos.",
            "Maestros duplicados y sin unique.",
            "Proformas: 1 por mes; proceso de un día para una proforma.",
            "TC: una fecha para reconocer, otra para pagar.",
            "Informes que exigen saber el estado de antemano.",
        ],
    )
    add_heading(d, "5. Decisiones de proceso que el proyecto aún no tiene por escrito del cliente", 2)
    bullets(
        d,
        [
            "¿OC autoriza el gasto ANTES o documenta el gasto DESPUÉS?",
            "¿Las ventas viven en el ERP o solo se contabilizan tras el facturador?",
            "¿Proformas se aprueban en cadena (MJ R3) o no (silencio 20/08)?",
            "¿Cotización de compras existe como documento o solo como dato en la OC?",
            "¿El mayor será trimomoneda?",
        ],
    )
    save(d, "90-AS-IS-Agrosoft-consolidado.docx")


def write_mermaid():
    text = """%% AS-IS Agrosoft — procesos vistos en reuniones (R1, R2, R4, T28)
%% Pegar en https://mermaid.live

flowchart TB
  subgraph ACC["Acceso"]
    L[Login] --> UE[Última empresa]
    UE --> MES[Elige mes contable y mes remuneración]
    MES --> MOD[Módulos]
  end

  subgraph COMPRAS["Compras — proceso REAL"]
    F1[Llega / existe factura del proveedor] --> OC[Contabilidad crea OC\\nobserva nº factura]
    OC --> AP[Jefe aprueba o rechaza\\nen bandeja SIN correo]
    AP --> REC[Recepción: solo fecha\\nTC de ese día]
    REC --> ASI1[Asiento: gasto vs facturas por recibir]
    ASI1 --> REG[Registro de compra / asociar DTE]
  end

  subgraph COMPRAS_SW["Compras — lo que el software sugiere y NO usan"]
    SOL[Solicitud de compra] -.-> OC
  end

  subgraph CONTR["Contratistas"]
    TAR[Tarifario ciego] --> CTR[Contrato folio a mano]
    CTR --> ENR[Enrolar personal]
    ENR --> LAB[Labores diarias\\nprecio a menudo desconocido]
    LAB --> PRO[Proforma borrador / definitiva\\nse envía al contratista]
    PRO --> FAC[Contratista emite factura]
    FAC --> ASO[Asociación 1 proforma por mes]
    ASO --> TR[Traspaso: facturas por recibir]
    FAC --> CIE[Cierre: 1 factura por contrato]
  end

  subgraph VENTAS["Ventas"]
    SABE[Ya saben qué vender] --> FACT[Emisión en Acepta / GoSocket\\nFUERA de Agrosoft]
    FACT --> LV[Libro / contabilización posterior]
    STK[Stock tránsito solo bodega]
    STK --> VOK[Venta exige stock real]
  end

  subgraph TES["Tesorería"]
    CART[Cartola digitada a mano] --> PAG[Pago: factura + banco\\n+ código financiero + n° cartola]
    PAG --> ASI2[Asiento banco vs proveedor\\nCLP y USD]
    PAG --> FC[Flujo de caja por código financiero]
  end

  subgraph CONT["Contabilidad núcleo"]
    ASI1 --> MAY[Libro mayor / 8 columnas]
    ASI2 --> MAY
    TR --> MAY
    LV --> MAY
    MAY --> CIE2[Cierre POR MÓDULO]
    CIE2 --> XML[Contab. electrónica 1 vez al año]
  end
"""
    (OUT / "99-diagramas-flujo-agrosoft.mmd").write_text(text, encoding="utf-8")
    print("OK 99-diagramas-flujo-agrosoft.mmd")


def doc_flujos():
    d = new_doc(
        "Diagramas de flujo AS-IS — guía de lectura",
        "El archivo 99-diagramas-flujo-agrosoft.mmd se abre en mermaid.live o se exporta a PNG/SVG para presentaciones.",
    )
    add_heading(d, "Cómo usar el diagrama", 2)
    bullets(
        d,
        [
            "Abrir 99-diagramas-flujo-agrosoft.mmd en https://mermaid.live",
            "Exportar SVG/PNG y adjuntar a la ficha de proyecto / Trello.",
            "Las flechas punteadas son caminos del software que el cliente NO usa.",
        ],
    )
    add_heading(d, "Leyenda", 2)
    table(
        d,
        ["Caja", "Significado"],
        [
            ["Compras — proceso REAL", "Lo demostrado y dicho por MJ (factura → OC)"],
            ["Compras — software sugiere", "Solicitud de compra: existe, no la usan"],
            ["Contratistas", "R2 Rodrigo + R1 MJ"],
            ["Ventas", "Emisión fuera de Agrosoft (R6 MJ)"],
            ["Tesorería", "R4 + T28"],
            ["Contabilidad núcleo", "Todo termina en mayor y cierre por módulo"],
        ],
    )
    save(d, "91-AS-IS-guia-diagramas.docx")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    doc_metodologia()
    doc_r1()
    doc_r2()
    doc_r3()
    doc_r4()
    doc_r5()
    doc_r6()
    doc_agosto()
    doc_t28()
    doc_gosocket()
    doc_sep03()
    doc_asis()
    write_mermaid()
    doc_flujos()
    idx = new_doc(
        "LEEME — índice del paquete",
        "Carpeta: docs/erp-planificacion/agrosoft-levantamiento/toma-requerimientos-2026-09/",
    )
    add_heading(idx, "Orden de lectura", 2)
    bullets(
        idx,
        [
            "00 Metodología",
            "R1 y R2 — el as-is de verdad (Agrosoft en producción)",
            "90 AS-IS consolidado + 91 guía de diagramas + 99 .mmd",
            "R3, R4, R6, T28, 20/08 tarde — requisitos y matices",
            "R5, 19/08, 20/08 mañana, 03/09 14:42 — internas (no backlog)",
            "GoSocket — tercero",
        ],
    )
    add_heading(idx, "Qué no es este paquete", 2)
    p(idx, "No es especificación funcional del ERP actual ni lista de tickets. Es el expediente de levantamiento para poder discutir alcance con el cliente sin citar minutas IA.")
    save(idx, "LEEME.docx")


if __name__ == "__main__":
    main()
