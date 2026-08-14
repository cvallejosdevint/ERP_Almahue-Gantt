# Flujo de negocio AS-IS — ERP Almahue

**Fecha:** 2026-08-14  
**Alcance:** estado actual del software (post-Reu6 en código local).  
**Notación:** Mermaid estilo BPMN — diamantes = compuertas **XOR** (una rama) salvo indicación.  
**Leyenda cobertura:** Implementado · Parcial · No · Diferido

Diagramas listos para renderizar en visor Mermaid (GitHub, VS Code, etc.).

---

## 0. Mapa de módulos (contexto)

```mermaid
flowchart LR
  subgraph ADM[Administración]
    emp[Empresas / Periodos]
    usr[Usuarios / Roles]
    apr[Reglas aprobación]
  end
  subgraph PAR[Parametrización]
    pc[Plan cuentas]
    cc[CC / Elementos / Áreas]
    cli[Clientes]
    prov[Proveedores]
  end
  subgraph COM[Comercial]
    ov[Órdenes venta]
    em[Emitir documento]
    lb[Libro ventas]
  end
  subgraph CMP[Compras]
    cot[Cotizaciones]
    oc[Órdenes compra]
    rec[Recepciones]
    reg[Registro compra]
  end
  subgraph INS[Insumos / Bodega]
    ma[Maestro insumos]
    bod[Bodegas]
    mov[Movimientos stock]
  end
  subgraph CON[Contratistas]
    pf[Proformas]
    tr[Traspaso]
  end
  subgraph CNT[Contabilidad]
    as[Asientos]
    per[Periodos]
  end
  subgraph TES[Tesorería]
    pay[Pagos]
    car[Cartolas]
    con[Conciliación]
    ec[Estado cuenta]
  end
  ADM --> PAR
  ov --> ma
  ov --> mov
  em --> lb
  cot --> oc
  oc --> reg
  em --> CNT
  reg --> CNT
  pf --> CNT
  lb --> TES
```

---

## 1. Autenticación y tenant

```mermaid
flowchart TD
  start([Usuario abre ERP]) --> login[Pantalla login]
  login --> gwAuth{XOR método}
  gwAuth -->|Email + password| jwt[JWT + permisos + empresa activa]
  gwAuth -->|Microsoft SSO| gwMs{XOR credenciales .env?}
  gwMs -->|No| disabled[Botón SSO deshabilitado]
  gwMs -->|Sí| msal[Token Entra]
  msal --> jwt
  disabled --> login
  jwt --> gwEmp{XOR multi-empresa}
  gwEmp -->|Una empresa| shell[Shell ERP]
  gwEmp -->|Varias| pick[Selector header empresa]
  pick --> shell
  shell --> gwAdmin{XOR rol master?}
  gwAdmin -->|Sí| allEmp[Ve todas las empresas]
  gwAdmin -->|No| oneEmp[Solo empresas asignadas]
```

| Gateway | Ramas | AS-IS |
|---|---|---|
| XOR método auth | Password vs SSO | Parcial (SSO sin credenciales) |
| XOR multi-empresa | Una vs varias | Implementado |
| XOR master | Master vs operativo | Implementado |

---

## 2. Aprobaciones (OC, proformas; Comercial reservado)

```mermaid
flowchart TD
  doc[Documento requiere aprobación] --> gwMod{XOR módulo}
  gwMod -->|Compras OC| chainOC[Motor grupos + escalas + organigrama]
  gwMod -->|Contratistas proforma| chainPF[Idem]
  gwMod -->|Comercial OV/factura| reserved[Sin cadena — reservado D4]
  chainOC --> gwMonto{XOR monto vs facultad aprobador}
  gwMonto -->|Dentro límite| pin[PIN aprobador designado]
  gwMonto -->|Excede| escala[Escalamiento siguiente nivel]
  escala --> pin
  pin --> gwRes{XOR resultado}
  gwRes -->|Aprobado| ok[Estado APROBADO]
  gwRes -->|Rechazado| rej[RECHAZADO / re-editar]
  gwAdmin{XOR admin aprueba por otro?}
  ok --> gwAdmin
  gwAdmin -->|Sí| warn[Advertencia + traza]
  gwAdmin -->|No| fin([Fin])
  warn --> fin
  reserved --> fin
```

| Gateway | AS-IS |
|---|---|
| XOR módulo | Parcial (Comercial sin cadena) |
| XOR monto / escalamiento | Implementado (OC/proformas) |
| XOR admin por otro | Implementado |

> **Nota Reu5→Reu6:** ya no rige «solicitante elige aprobador de lista» como modelo final; queda sustituido por cadena automática.

---

## 3. Ventas — Orden de venta (canal con inventario)

```mermaid
flowchart TD
  start([Nueva OV]) --> cli[Seleccionar cliente maestro]
  cli --> linea[Agregar líneas]
  linea --> gwTipo{XOR tipo línea}
  gwTipo -->|PRODUCTO| selProd[SearchableSelect Insumo]
  gwTipo -->|SERVICIO| txtSvc[Descripción libre]
  gwTipo -->|FLETE| txtFlete[Línea flete]
  selProd --> gwBod{XOR bodegas}
  gwBod -->|Una bodega| split1[Split cantidad]
  gwBod -->|Varias| splitN[Splits multi-bodega]
  split1 --> gwStock{XOR stock >= cantidad?}
  splitN --> gwStock
  gwStock -->|No| blockStock[Bloqueo API]
  gwStock -->|Sí| save[Guardar OV BORRADOR]
  txtSvc --> save
  txtFlete --> save
  save --> gwConf{XOR confirmar OV?}
  gwConf -->|No| edit[Editar borrador]
  edit --> gwConf
  gwConf -->|Sí| salida[Movimiento bodega SALIDA]
  salida --> ovOk[OV APROBADO/EMITIDO]
  ovOk --> gwFac{XOR facturar?}
  gwFac -->|No| park[Queda en bandeja OV]
  gwFac -->|Sí| conv[convertirDocumento → FACTURA]
  conv --> factBorrador[Factura BORRADOR precio editable]
  factBorrador --> emitirFac[Grabar y contabilizar]
  emitirFac --> libro[Libro ventas]
```

| Gateway | AS-IS |
|---|---|
| XOR tipo línea | Implementado |
| XOR stock | Implementado (solo positivo) |
| XOR confirmar | Implementado |
| XOR facturar | Implementado |
| Precio ≥ costo (D16) | Implementado en API PRODUCTO; sin UI param empresa |

---

## 4. Ventas — Emitir documento (canal directo DTE)

```mermaid
flowchart TD
  start([Emitir documento]) --> gwRoute{XOR intención}
  gwRoute -->|Producto con stock| hint[Subtítulo: usar Órdenes de venta]
  gwRoute -->|Servicio / NC / ND / Guía / Export| wizard[Wizard 3 pasos]
  hint -.->|Usuario puede ignorar| wizard
  wizard --> s1[Paso 1: Cliente maestro + tipo doc]
  s1 --> gwCliente{XOR cliente registrado?}
  gwCliente -->|No| blockCli[Bloqueo — alta en Clientes]
  gwCliente -->|Sí| s2[Paso 2: Ítems]
  s2 --> gwLinea{Tipo línea enviado?}
  gwLinea -->|No — default SERVICIO| freeText[Descripción texto libre]
  gwLinea -->|PRODUCTO + insumoId| catalogo[Validación maestro — no expuesto en UI]
  freeText --> cuenta[Cuenta contable por ítem]
  cuenta --> s3[Paso 3: Referencias / COMEX]
  s3 --> gwDraft{XOR acción}
  gwDraft -->|Borrador| borr[BORRADOR usuario]
  gwDraft -->|Emitir| gwPer{XOR periodo abierto?}
  gwPer -->|No| blockPer[Bloqueo contabilizar]
  gwPer -->|Sí| gwGuia{XOR tipo GUIA?}
  gwGuia -->|Sí| emGuia[EMITIDO sin asiento]
  gwGuia -->|No| asiento[Asiento contable]
  asiento --> gwDte{XOR GoSocket integrado?}
  gwDte -->|No — AS-IS| local[EMITIDO folio local + stub DTE]
  gwDte -->|TO-BE| gos[Envío SII]
  local --> libro[Libro ventas / despachos]
  emGuia --> libro
  gos --> libro
  borr --> fin([Fin])
  libro --> fin
```

| Gateway | AS-IS | Gap |
|---|---|---|
| XOR cliente maestro | Implementado | — |
| XOR línea catálogo | **Siempre SERVICIO** en UI | **Hueco texto libre** |
| XOR GoSocket | Diferido | Stub |
| Movimiento inventario | **No** en este flujo | Por diseño Reu6 parcial |

---

## 5. Compras — Cotización → OC → recepción → factura

```mermaid
flowchart TD
  start([Cotización compras]) --> cotB[Cotización BORRADOR]
  cotB --> gwAprCot{XOR requiere aprobación?}
  gwAprCot -->|Sí| aprCot[Cadena aprobación]
  gwAprCot -->|No| cotOk[Aprobada]
  aprCot --> cotOk
  cotOk --> gwConv{XOR convertir}
  gwConv -->|OC| oc[Orden compra]
  gwConv -->|Otro| fin1([Fin])
  oc --> gwAprOc{XOR aprobación OC?}
  gwAprOc -->|Sí| pinOc[PIN / cadena]
  gwAprOc -->|No| ocOk[OC APROBADA]
  pinOc --> ocOk
  ocOk --> rec[Recepción — puede otro mes]
  rec --> gwRec{XOR confirmar recepción?}
  gwRec -->|Borrador| rec
  gwRec -->|Confirmada| facCom[Registro factura compra]
  facCom --> gwAfecto{XOR afecto OC vs factura}
  gwAfecto -->|Mismatch| alerta[Alerta usuario]
  gwAfecto -->|OK| asiento[Asiento compra + CC ítem]
  alerta --> gwForce{XOR continuar?}
  gwForce -->|Sí| asiento
  gwForce -->|No| fix[Corregir]
```

| Gateway | AS-IS |
|---|---|
| XOR aprobación cotización/OC | Implementado |
| XOR recepción vs mes OC | Implementado |
| XOR afecto/exento | Parcial (alerta) |

> **Nota Reu6:** cotización de **ventas** eliminada; redirect `/comercial/cotizaciones` → Compras.

---

## 6. Contratistas — Proforma → factura → traspaso

```mermaid
flowchart TD
  ing[Ingreso labores] --> pf[Proforma BORRADOR]
  pf --> gwDef{XOR a solicitar aprobación?}
  gwDef -->|Sí| apr[Cadena + PIN]
  gwDef -->|No| def[DEFINITIVA]
  apr --> gwPin{XOR aprobado?}
  gwPin -->|Sí| def
  gwPin -->|No| pf
  def --> gwEdit{XOR editar post-aprobación?}
  gwEdit -->|Sí| rev[Reverso + vuelve a autorización]
  gwEdit -->|No| gwFac{XOR facturar}
  gwFac -->|1 o N proformas| fac[Factura proveedor interna]
  fac --> tras[Traspaso periodo]
  tras --> asiento[Asiento cierre]
```

| Gateway | AS-IS |
|---|---|
| XOR PIN | Implementado |
| XOR N:1 factura | Implementado |
| GoSocket factura proveedor | Diferido |

---

## 7. Contabilidad — Periodos

```mermaid
flowchart TD
  p[Periodo contable] --> gwEst{XOR estado}
  gwEst -->|ABIERTO| op[Operar: contabilizar docs]
  gwEst -->|CERRADO| block[Bloqueo nuevos asientos]
  block --> gwReab{XOR reabrir?}
  gwReab -->|Sí| motivo[Motivo obligatorio + historial]
  motivo --> op
  op --> gwCerr{XOR cerrar mes?}
  gwCerr -->|Sí| cerrar[CERRAR + evento auditoría]
```

| Gateway | AS-IS |
|---|---|
| XOR periodo header único | Implementado (Reu5) |
| XOR reabrir + motivo | Implementado |

---

## 8. Tesorería — Cartola, pago, conciliación

```mermaid
flowchart TD
  imp[Importar cartola Excel] --> movs[Movimientos PENDIENTE]
  movs --> gwPath{XOR acción}
  gwPath -->|Contabilizar| asB[Asiento banco]
  gwPath -->|Crear pago| pago[Pago + N° transacción]
  pago --> asB
  asB --> conc[Conciliación]
  conc --> gwConc{XOR}
  gwConc -->|Conciliar| ok[CONCILIADO]
  gwConc -->|Pendiente| movs
  libro[Libro ventas] --> gwPay{XOR registrar pago?}
  gwPay -->|UI stub / parcial| tes[Pantalla pagos]
  ec[Estado cuenta cliente] --> aging[Aging / vencimientos]
```

| Gateway | AS-IS |
|---|---|
| XOR cartola → pago | Parcial→mejorado |
| XOR bridge libro→pago | Parcial |
| Excel cartolas finas MJ | Diferido |

---

## 9. Corrección ventas — Reverso vs NC

```mermaid
flowchart TD
  fac[Factura CONTABILIZADA] --> gwCorr{XOR tipo corrección}
  gwCorr -->|Solo imputación CC/cuenta| rev[Reverso contable]
  rev --> recont[Re-contabilizar]
  gwCorr -->|Anulación / monto tributario| nc[Emitir NC]
  nc --> gwOrig{XOR factura origen}
  gwOrig -->|Seleccionada| precarga[Precarga líneas / saldo NC]
  precarga --> gwSaldo{XOR monto <= saldo?}
  gwSaldo -->|No| blockNc[Bloqueo API]
  gwSaldo -->|Sí| emNc[NC contabilizada]
  emNc --> libro[Libro — NC resta]
```

| Gateway | AS-IS |
|---|---|
| XOR reverso vs NC | Implementado |
| XOR saldo NC | Implementado (P1-9) |

---

## 10. Flujo integrado compra + venta (piloto D20)

```mermaid
flowchart TD
  subgraph VENTA[Venta con stock — camino feliz Reu6]
    A1[Maestro insumo] --> A2[OV producto + bodega]
    A2 --> A3[Confirmar → stock-]
    A3 --> A4[Facturar OV]
    A4 --> A5[Contabilizar factura]
    A5 --> A6[Libro ventas]
    A6 --> A7[Estado cuenta / cobro]
  end
  subgraph VENTA_ALT[Venta sin stock — AS-IS permitido]
    B1[Emitir documento] --> B2[Línea texto libre SERVICIO]
    B2 --> B3[Contabilizar]
    B3 --> A6
  end
  subgraph COMPRA[Compra]
    C1[Cotización proveedor] --> C2[OC aprobada]
    C2 --> C3[Recepción]
    C3 --> C4[Factura compra]
    C4 --> C5[Asiento + CC]
  end
  A7 --> TES[Tesorería pago]
  C5 --> TES
```

---

## 11. Resumen de gateways y huecos críticos

| Flujo | Gateways modelados | Hueco principal AS-IS |
|---|---|---|
| Login / tenant | 3 | SSO sin credenciales |
| Aprobaciones | 5 | Comercial sin cadena |
| OV + inventario | 6 | Param `ventaBajoCosto` sin UI |
| Emitir directo | 7 | **Texto libre = sin catálogo ni stock** |
| Compras | 6 | GoSocket compras diferido |
| Contratistas | 5 | DTE proveedor diferido |
| Periodos | 3 | — |
| Tesorería | 4 | Bridge pago desde libro |
| NC / reverso | 4 | — |

**Conclusión:** el BPMN AS-IS refleja la bifurcación Reu6 — **OV** para productos con trazabilidad de bodega, **Emitir** para documentos tributarios directos y servicios, con un **puente débil** (el usuario puede facturar productos ficticios por emitir). Cerrar ese puente es prioridad de alineación negocio antes de piloto con datos reales (D20).

---

## 12. Referencias

- Auditoría detallada: `2026-08-14-auditoria-reu5-reu6.md`
- BPMN histórico Reu4–Reu5: `entrega-reu4-reu5-as-is/02-BPMN-FLUJOS.md`
- Minutas: Reu5 (03/08/2026), Reu6 (06/08/2026)
