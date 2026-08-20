# Demo interno 19/08/2026 — contraste Sergio vs minutas Almahue

**Grabación:** `Screen Recording 2026-08-19 162555.mp4` (~11:47)  
**Quién habla:** Carlos (desarrollo) y Sergio (Devint). **No hay Agustín ni MJ.**  
**Entorno en pantalla:** `localhost:5174`, usuario **Admin Almahue**, empresa **ALM SERVICES SPA**, periodo 2026-08 abierto.  
**ASR:** Whisper local `small` (español) + limpieza Ollama `qwen2.5-coder:14b`. El ASR mete errores (Berri/berry, GoSocket, SII, PIN).  
**Regla:** Sergio/Carlos = hipótesis. Verdad = Reu6 > Reu5 > Reu4 (MJ/Agustín) + código.

Capturas locales (no git; carpeta pesada):  
`docs/erp-planificacion/agrosoft-levantamiento/fuentes/2026-08-19-demo-interno/frames/`  
(f001 Emitir/OV · f030 ítems factura + cuenta · f038 bodega OV · f043 PIN aprobar OV · f050 guías vacías)

Transcripción bruta: [`fuentes/transcripcion-2026-08-19-demo-interno.md`](fuentes/transcripcion-2026-08-19-demo-interno.md)

---

## Qué sí aplica (Sergio alineado con el cliente)

| Dicho en la demo (~min) | Minuta / código | Estado |
|---|---|---|
| La **orden de venta no es DTE**; no vale ante el SII. La **factura electrónica** sí es DTE y se declara. | D11: OV → stock → factura. Emitir = FACTURA/NC/ND/GUÍA. | **Aplica** |
| En **compras** Almahue **no emite** factura de compra al proveedor: recibe la factura del otro y la declara como compra (IVA crédito). | Reu3/Reu4 MJ: libro de compras; asociar a OC; carga Acepta/PDF. | **Aplica** (concepto SII) |
| Libro de compras se alimenta de **sincronización partner** (GoSocket) + se puede **registrar a mano**. | Reu2 MJ libro compras en línea vía GoSocket; Reu4 «cargar libro o PDF». Código: `/compras/registro`. | **Aplica** como dirección; **GoSocket live / CAF = H11, no cerrado** |
| **Producto** pide bodega; **servicio** no. Precio editable. Multi-bodega: cantidades por bodega. | D12, D13, D15 | **Aplica** (en **OV**, no en Emitir directo) |
| Emisión directa **no descuenta stock**; stock por **OV confirmada**. | D13/D14; UI: «La emisión directa no descuenta stock… use Orden de Venta» (f030) | **Aplica** |
| Admin puede **aprobar** un pendiente que era de otro (Catalina). | D2 superadmin | **Aplica** |
| PIN de demo **4821**. | AGENTS.md | **Aplica** (dato operativo, no requisito de cliente) |
| Tras aprobar, **no salió factura** / partner sin folios. | H11 fail-closed sin CAF; factura es **otro paso**, no el PIN de la OV | **Hecho técnico**; Sergio lo mezcló con «emisión al aprobar» (ver abajo) |

---

## Qué no aplica o contradice al cliente

| Dicho de Sergio | Por qué no es requisito |
|---|---|
| «Desde Emitir puedes sacar boleta, factura, **cotización, OV, OC**» (~00:25) | **Contradice D11.** Cotización = Compras → OC. OV = Ventas. Emitir **no** es el alta de cotiz/OC/OV. No restaurar cotiz→NP. |
| «Indicador de venta» decide producto vs bodega (~04:34) | **Confunde campos.** D12 es **tipo de línea** producto/servicio. El indicador SII de venta es otro dato de DTE. En la misma demo después vieron tipo Producto + bodega en OV (f038): eso sí es D12. |
| Al aprobar la OV «debería realizarse la emisión» (~09:05) | **No.** Cadena autoriza la OV; stock al **confirmar**; factura en **Emitir/factura desde OV**. El PIN no emite DTE. |
| Dos «mantenedores»: documentos de venta a emitir vs documentos de compra a emitir, y una **factura de compra emitida** aparte (~09:56–11:15) | **Hipótesis Devint.** El cliente pidió **libro de compras recibido** + carga, no un segundo wizard de emisión de compra tipo SII. Dejar Compras como está (cotiz→OC + registro recibido) es lo que **tú** le dijiste al final y calza con D11. |
| Impuesto especial «berry / berries / exportadores» (~02:02) | **No está en minutas.** Preguntar a **MJ**. No implementar. |
| Publicar ya y que entren con credenciales (~10:57) | Operativo. **H14:** no asumir migrate/piloto en `45.7.229.46` hasta deploy explícito. |

---

## Problemas reales que se vieron (no son «opinión»)

1. **Folios/CAF GoSocket** al emitir: error esperado sin CAF (H11). No venderlo como «ya emite SII».
2. **UI Emitir vs OV:** al inicio tipo documento Factura vs OV (`?contexto=ov`); cuenta contable en factura directa; bodega a veces no aparece hasta elegir producto de stock (f038). Gap de demo, no de minuta.
3. **Guías de despacho** vacías en SERVICES (f050): libro no contabiliza; emitir guía es otro camino. No es bug de permisos de Valentina: esta sesión es **admin**.
4. **Empresa SERVICES** en la demo: Valentina es **EXPORT**. Mostrar admin en SERVICES no prueba el rol Ventas.
5. Sergio admite que **Mario no cierra definiciones** («voy a preguntar») y que **MJ no estaría el jueves** (vacaciones, dicho por Mario). Feedback de cliente esta semana = débil. No sustituir minutas.

---

## Sugerencias (solo si el cliente las confirma)

- Dejar **Emitir** = DTE de venta (FACTURA/NC/ND/GUÍA). OV y cotiz **fuera** de ese wizard.
- Libro de compras = **recibidos** (+ carga manual como ya existe). No «factura de compra emitida» en el mismo sentido que factura de venta salvo que MJ lo pida por escrito.
- Validar con MJ: indicador SII vs tipo producto/servicio; impuestos específicos (si existen, no «berry» inventado).
- Flujo a mostrar el jueves: Valentina OV → Andrés/Natalia aprueban → confirmar stock → facturar (y explicar el rechazo de folios).

---

## Gaps

| Gap | Dueño |
|---|---|
| CAF/folios partner | MJ / H11 |
| Definición indicador venta SII vs tipo línea | MJ |
| Impuesto berries / específico | MJ — no en Reu6 |
| Deploy prod vs local | H14 |
| Rol Ventas vs menú/403 (trabajo 19/08 en código) | Dev — no aparece en este video (sesión admin) |
