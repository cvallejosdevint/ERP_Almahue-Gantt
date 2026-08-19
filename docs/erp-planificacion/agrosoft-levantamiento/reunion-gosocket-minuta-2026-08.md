# Reunión GoSocket QA — Minuta onboarding API y portal (agosto 2026)

**Tipo:** Onboarding GoSocket QA / portal sandbox / emisión API  
**Fecha:** agosto 2026, post-Reu6; transcripción entregada 19/08/2026  
**Participantes:** Pablo Rodriguez (GoSocket Chile, consultor), Maria Jesus Rodriguez / María Jesús (Almahue), Carlos Vallejos (Devint), Mario Andres Ubillo Labrin (Almahue)  
**Mencionados:** Cristian (contrato/factura GoSocket), Sergio (Devint), Nico (representante legal / certificado)  
**Grabación:** Sí, desde mitad de reunión aprox. según Carlos.

| Fuente | Ubicación |
|---|---|
| Transcripción | [`fuentes/transcripcion-reunion-gosocket-qa.md`](fuentes/transcripcion-reunion-gosocket-qa.md) |
| Plan gateway | [`partners-hub/00-PLAN-IMPLEMENTACION.md`](partners-hub/00-PLAN-IMPLEMENTACION.md) |

---

## 1. Resumen ejecutivo

GoSocket confirmó que el ambiente QA/API puede avanzar sin contrato comercial firmado. Pablo indicó que crearía o habilitaría el ambiente de pruebas y enviaría credenciales al salir de la reunión; esas credenciales QA quedaron recibidas posteriormente en el entorno local del `billing-gateway` sin versionar valores.

El contrato comercial sigue siendo requisito para habilitar IOFactura productivo. Cristian no había respondido al inicio de la reunión, pero Pablo informó durante la llamada que enviaría el borrador ese mismo día para revisión de MJ/Mario. IOFactura queda diferido hasta firma.

El portal GoSocket QA pasa a ser herramienta obligatoria de validación para Devint: los testers deben enrolarse, operar en `sandbox2`, revisar documentos emitidos, errores, XML construido, archivo de integración crudo y PDF. Las pruebas deben cubrir ambas empresas mencionadas por Pablo/MJ: Almago Export SpA y AlmaWeb.

La carga histórica DTE desde AlmaWeb/Acepta queda diferida. MJ reportó ~1000–1200 documentos, pérdida de historial al cambiar a Acepta y respaldos impresos; Pablo explicó que el SII permite descargar de a 20 documentos y ofreció revisarlo en otra reunión.

Importante para control de fuente: Carlos dijo que Devint ya tenía “aproximadamente la estructura” para enviar por API. Eso se registra como hipótesis o avance interno de Devint, no como producto cerrado **al momento de la reunión**.

**Addendum 2026-08-19 (código + QA, no la llamada):** el ERP ya llama HTTP a `billing-gateway` (`BILLING_GATEWAY_ENABLED=true` + `BILLING_STUB_INLINE=false`). GoSocket sandbox `developers-sbx` autenticó y respondió `REJECTED` por CAF/rango no cargado (fail-closed). No asumir SII live ni folio oficial hasta CAF/cert MJ.

---

## 2. Decisiones y hechos confirmados

| # | Decisión / hecho | Fuente | Implicancia |
|---|---|---|---|
| GOS-1 | QA/API GoSocket **no requiere contrato comercial firmado** | Pablo | Devint puede probar sandbox antes de IOFactura productivo |
| GOS-2 | IOFactura se habilita **después** de contrato firmado | Pablo / MJ | Contrato e IOFactura siguen como dependencia comercial |
| GOS-3 | Cristian enviaría borrador de contrato ese día | Pablo | MJ/Mario deben revisar; no bloquea QA/API |
| GOS-4 | Testers Devint deben enrolarse y usar portal GoSocket QA | Pablo | Validación de emisiones y errores ocurre en portal, no solo por API |
| GOS-5 | Validar integración con **ambas empresas**: Almago Export SpA y AlmaWeb | Pablo | Multiempresa/multi-RUT debe considerarse en pruebas QA |
| GOS-6 | Link recibido por correo falló; `sandbox2` funcionó | Carlos / Pablo | Usar URL sandbox2 para enrolamiento y pruebas QA |
| GOS-7 | Pablo agregó usuarios por invitación en QA | Pablo | En productivo, MJ probablemente administrará altas |
| GOS-8 | Folios QA son pocos y se cargan manualmente en Inbox › Gestión de folios | Pablo | Si API reporta falta de rango de folio, coordinar CAF con MJ |
| GOS-9 | En productivo los folios serán automáticos | Pablo | Diferenciar runbook QA vs productivo |
| GOS-10 | Certificado digital debe cargarse antes de emitir en QA | Pablo | Sin certificado/permiso de firma, documentos saldrán rechazados |
| GOS-11 | Certificado debe coincidir con usuario firmante autorizado en SII | Pablo / MJ | Certificado del representante legal no garantiza permiso de firma |
| GOS-12 | API keys se crean en Configuraciones › API keys › Agregar › Basic authentication | Pablo | QA permite hasta 10 keys; productivo normalmente 1 entregada por Pablo |
| GOS-13 | Emitir con fecha del día para que los documentos no se pierdan en filtros | Pablo | Portal filtra por fecha; usar últimos 3 meses para búsqueda |
| GOS-14 | Errores se revisan en Notas del documento | Pablo | “Error de carátula” suele apuntar a resolución SII mal informada |
| GOS-15 | Portal expone XML construido, archivo de integración crudo y PDF | Pablo | Sirve para distinguir error de mapeo XSLT vs request enviado |
| GOS-16 | Regenerar PDF no requiere reemitir el documento | Pablo | Cambios de representación gráfica se prueban sobre documentos anteriores |
| GOS-17 | Canal de soporte: correo o Teams directo con Pablo | Pablo / Carlos | Dudas de errores no identificados se escalan a GoSocket |

---

## 3. Aclaraciones de fuente

| Afirmación | Clasificación | Nota |
|---|---|---|
| “Ya tenemos aproximadamente la estructura de cómo vamos a enviar la información mediante la API” | Hipótesis / avance interno Devint | No confirma integración productiva ni QA desde ERP. Contrastar con código y pruebas antes de marcar cerrado |
| “Ahí te dejo con los expertos, Carlos y Sergio” | Derivación operativa MJ | MJ delega dudas técnicas API a Devint; no convierte opiniones de Devint en requisito |
| “Para QA no es necesario el contrato” | Hecho operativo GoSocket | Pablo confirma que las credenciales sandbox pueden entregarse antes de contrato |
| “IOFactura se habilita cuando contrato esté firmado” | Dependencia comercial | Pablo lo condiciona explícitamente a firma |

---

## 4. Diferidos / pendientes

| Tema | Responsable | Estado / nota |
|---|---|---|
| Contrato comercial GoSocket / IOFactura | Cristian + MJ/Mario + Pablo | Borrador anunciado para ese día; IOFactura post-firma |
| Carga histórica DTE AlmaWeb/Acepta | MJ + Pablo | ~1000–1200 docs; SII descarga máximo 20 por vez; requiere reunión aparte |
| Carga CAF QA | MJ | Manual en portal QA antes de pruebas API |
| Certificado digital QA | MJ | Debe estar cargado antes de que Devint emita |
| Permiso de firma SII | MJ | Validar usuario firmante; certificado de RL no siempre basta |
| Productivo API keys | Pablo + MJ | Normalmente 1 key productiva; no usar QA como señal de live |
| Integración real ERP → billing-gateway → GoSocket | Devint | No cerrada por esta reunión; requiere implementación y evidencia QA |

---

## 5. Action items

### María Jesús / Almahue

| # | Acción | Prioridad |
|---|---|---|
| 1 | Cargar certificado digital en Configuraciones › Certificados del portal QA | Alta |
| 2 | Validar que el certificado pertenezca a usuario firmante con permiso en SII | Alta |
| 3 | Solicitar y cargar CAF QA en Inbox › Gestión de folios | Alta |
| 4 | Revisar borrador de contrato enviado por Cristian | Alta |
| 5 | Coordinar IOFactura con Pablo una vez firmado el contrato | Media |
| 6 | Coordinar reunión aparte para recuperación histórica AlmaWeb/Acepta | Media |

### Devint

| # | Acción | Prioridad |
|---|---|---|
| 1 | Enrolarse en portal `sandbox2` y confirmar acceso a ambas empresas | Alta |
| 2 | Generar/usar API keys QA sin versionar secretos | Alta |
| 3 | Emitir documentos vía API QA y validar resultados en portal | Alta |
| 4 | Revisar Notas del documento ante rechazos y escalar a Pablo si no se identifica causa | Alta |
| 5 | Comparar archivo de integración crudo vs XML construido para diagnosticar mapeos | Media |
| 6 | ERP demo: `BILLING_STUB_INLINE=true`. HTTP+GoSocket QA: `ENABLED=true` + `STUB_INLINE=false` **después** de CAF/cert (si no, fail-closed bloquea contabilizar) | Alta |

### Pablo / GoSocket

| # | Acción | Prioridad |
|---|---|---|
| 1 | Enviar credenciales QA post-reunión | Alta |
| 2 | Invitar/agregar usuarios QA al portal | Alta |
| 3 | Acompañar corrección de errores de emisión por correo o Teams | Media |
| 4 | Habilitar IOFactura después de contrato firmado | Alta |
| 5 | Apoyar revisión de carga histórica en reunión separada | Media |

---

## 6. Checklist QA derivado

- [ ] Testers Devint con acceso a portal `sandbox2`.
- [ ] Ambas empresas visibles para testers: Almago Export SpA y AlmaWeb.
- [ ] Certificado digital cargado para usuario firmante autorizado en SII.
- [ ] CAF QA cargados manualmente antes de emitir.
- [ ] API key QA generada como Basic authentication y guardada solo en entorno gitignored.
- [ ] Primera emisión API con fecha del día.
- [ ] Documento ubicado en Emitidos con filtro últimos 3 meses.
- [ ] Notas revisadas ante rechazo.
- [ ] XML construido y archivo de integración crudo descargables para diagnóstico.
- [ ] PDF validado/regenerado sin reemitir si cambia representación gráfica.

---

## 7. Impacto en plan partners-hub

Actualizar `partners-hub/00-PLAN-IMPLEMENTACION.md` con fecha 2026-08-19: ApiKeys sandbox QA recibidas y existentes solo en `.env` local del `billing-gateway` (gitignored). Mantener pendiente contrato comercial / IOFactura y no asumir producción live.
