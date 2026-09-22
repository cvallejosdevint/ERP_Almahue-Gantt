# Testrim Ventas 2026-09-10

Base: http://127.0.0.1:5174 · PASS 27 · FAIL 0

- **PASS** `VEN-LOGIN`: Login OK → http://127.0.0.1:5174/
- **PASS** `VEN-EMPRESA`: Selector empresa (hint EXPORT)
- **PASS** `VEN-CLI-LIST`: Filtros=true
- **PASS** `VEN-CLI-FORM`: Alta cliente: 17 inputs
- **PASS** `VEN-OV-LIST`: Filtros=true
- **PASS** `VEN-OV-ROWS`: Filas listado: 2
- **PASS** `VEN-OV-INPUTS-NAC`: Indicador opciones: VENTA · Venta | SERVICIO · Servicio | EXENTO · Exento | EXPORTACION · Exportación
- **PASS** `VEN-OV-PANEL-VENTA`: Panel visible=true extraExport=false
- **PASS** `VEN-OV-PANEL-EXPORT-ALTA`: Panel exportación USD + COMEX en alta
- **PASS** `VEN-OV-COMEX-STEP2`: cliente=true COMEX visible=true
- **PASS** `VEN-OV-PAISES`: Opciones país: 225 · Estados Unidos | 336 · China | 563 · Países Bajos | 826 · Reino Unido | 276 · Alemania | 250 · Francia | 380 · Italia | 392 · Japón | 124 · Canadá | 076 · Brasil
- **PASS** `VEN-OV-VIAS`: 1 · Marítima | 4 · Aérea
- **PASS** `VEN-OV-CLAUSULAS`: 5 · FOB | 1 · CIF
- **PASS** `VEN-OV-MONEDAS`: 13 · USD
- **PASS** `VEN-OV-PANEL-EXPORT-STEP2`: EXPORTACIÓN / OTRA MONEDA
Moneda transacción
13 · USD
Cajas
1
Tipo de cambio
—
Total CLP
$0
Exento CLP
$0
País receptor
225 · Estados Unidos
País destino
225 · Estados Unidos
Cláusula
5 · FOB
Vía
1 · Marítima
Modalidad
9 · Consignación libre
Puerto embarque
—
Puerto desembarque
—
Tipo bulto
22 · Caj
- **PASS** `VEN-OV-BORRADORES-MODAL`: Modal abierto
- **PASS** `VEN-OV-PANEL-BORRADOR`: indicador=VENTA extra=true
- **PASS** `VEN-EMITIR-PICKER`: Tipos sin OV: Nota de crédito | Nota de débito | Guía de despacho
- **PASS** `VEN-EMITIR-NC`: Tipos SII origen: ,33,34,52,56,61,110,111,112
- **PASS** `VEN-EMITIR-ND`: http://127.0.0.1:5174/comercial/emitir?tipo=ND
- **PASS** `VEN-EMITIR-GUIA`: http://127.0.0.1:5174/comercial/emitir?tipo=GUIA
- **PASS** `VEN-LIBRO-FILTROS`: 110=true 101=false OV=false
- **PASS** `VEN-LIBRO-SIN-101`: Sin 101
- **PASS** `VEN-LIBRO-SIN-OV`: Libro sin tipo OV
- **PASS** `VEN-LIBRO-110`: Filtro incluye 110 factura exportación
- **PASS** `VEN-GUIAS`: Libro de guías
- **PASS** `VEN-SIN-COTIZ`: Redirect http://127.0.0.1:5174/compras/ordenes