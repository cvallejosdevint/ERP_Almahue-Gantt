with open('ERP/erp_back/prisma/schema.prisma', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'enum EstadoProforma {\n  BORRADOR\n  PENDIENTE_APROBACION\n  DEFINITIVA\n  ENVIADA_CONTRATISTA\n  FACTURADA\n  RECHAZADA\n\n  @@schema("erp")\n}'
replacement = 'enum EstadoProforma {\n  BORRADOR\n  PENDIENTE_APROBACION\n  DEFINITIVA\n  ENVIADA_CONTRATISTA\n  FACTURADA\n  RECHAZADA\n  REVERSADA\n\n  @@schema("erp")\n}'

# normalize to \n for replacement
norm_text = text.replace('\r\n', '\n')
if target in norm_text:
    new_norm = norm_text.replace(target, replacement, 1)
    # restore \r\n if original had \r\n
    if '\r\n' in text:
        final_text = new_norm.replace('\n', '\r\n')
    else:
        final_text = new_norm
    with open('ERP/erp_back/prisma/schema.prisma', 'w', encoding='utf-8') as f:
        f.write(final_text)
    print('schema.prisma updated successfully!')
else:
    print('Target not found!')

