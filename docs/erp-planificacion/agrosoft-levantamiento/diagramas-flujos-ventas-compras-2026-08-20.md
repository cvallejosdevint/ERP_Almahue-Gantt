# Diagramas para reunión Almahue — flujos Ventas y Compras (preguntas)

**Fecha:** 2026-08-20  
**Origen:** reunión interna Carlos + Sergio; **no** son requisitos cerrados.  
**Uso:** editar en vivo con MJ/Agustín. Compras **congelada** en código hasta su OK.

---

## 1. Ventas (implementado en local — validar con cliente)

```mermaid
flowchart TD
  A[Solicitante crea OV] --> B{¿Requiere aprobación<br/>por monto/empresa?}
  B -->|Sí| C[Enviar a aprobación]
  B -->|No| D[Confirmar stock]
  C --> E{¿Hay más pasos<br/>en la cadena?}
  E -->|Sí| F[Notifica al siguiente aprobador]
  F --> G[Aprobador firma con PIN]
  G --> E
  E -->|No · último paso| H[OV AUTORIZADA]
  H --> I[Reserva stock 7 días<br/>físico no baja]
  I --> J[Notificación al solicitante<br/>Confirmar / Facturar]
  J --> K[Solicitante confirma]
  K --> L[Consume reserva<br/>SALIDA_VENTA]
  L --> M[OV APROBADO]
  M --> N[Emitir: elige OV propia]
  N --> O[Factura electrónica DTE]
  O --> P{¿CAF / partner OK?}
  P -->|No| Q[Borrador · no contabiliza]
  P -->|Sí| R[Emitido / contabilizable]

  style H fill:#dbeafe
  style I fill:#fef3c7
  style O fill:#fde68a
  style Q fill:#fecaca
```

### Preguntas Ventas (marcar en la reunión)

| # | Pregunta | Opción A | Opción B |
|---|---|---|---|
| V1 | ¿Toda venta (también solo servicio) debe pasar por OV? | Sí, siempre | Emitir directo bajo umbral / flag |
| V2 | Stock: ¿reserva al autorizar (7 días) está bien? | Sí | Solo descontar al confirmar / al facturar |
| V3 | ¿Quién puede facturar una OV? | Solo el solicitante | Cualquiera con permiso Ventas |
| V4 | Al vencer la reserva (7 días) ¿qué pasa? | Liberar y avisar | Bloquear OV hasta re-autorizar |

---

## 2. Compras (hipótesis Sergio vs D11 — **decidir con Almahue**)

### A) Lo que pide Reu6 / código actual (D11)

```mermaid
flowchart TD
  A[Necesidad de compra] --> B[Cotización en Compras]
  B --> C[Enviar a aprobación]
  C --> D{Cadena OK?}
  D -->|No| E[Rechazo / borrador]
  D -->|Sí| F[Convertir a OC borrador]
  F --> G[Enviar OC a aprobación si aplica]
  G --> H[OC autorizada]
  H --> I[Recepción operativa]
  I --> J[Factura RECIBIDA del proveedor<br/>Libro de compras / GoSocket]
  J --> K[Asociar a OC · IVA crédito]

  style F fill:#bbf7d0
  style J fill:#fde68a
```

### B) Lo que Sergio planteó el 20/08 (a validar)

```mermaid
flowchart TD
  A[Cotización interna] --> B[Aprobación por montos]
  B --> C[Cotización aprobada]
  C --> D[¿Enviar cotización al proveedor?]
  D --> E[Proveedor emite factura<br/>referenciando cotización]
  E --> F[Almahue recibe DTE compra<br/>GoSocket]
  F --> G{¿Referencia válida<br/>y cotiz aprobada?}
  G -->|No| H[¿Auto-rechazo o bandeja?]
  G -->|Sí| I[Aceptar en libro de compras]
  X[Convertir a OC] -.->|Sergio: ¿está mal?| Y[Pendiente decisión]

  style X fill:#fecaca
  style H fill:#fef3c7
  style I fill:#bbf7d0
```

### Preguntas Compras (marcar en la reunión)

| # | Pregunta | Opción A (D11) | Opción B (Sergio) |
|---|---|---|---|
| C1 | Documento previo a la factura del proveedor | Cotización → **OC** → factura recibida | Cotización aprobada → factura recibida **sin OC** |
| C2 | Si la factura llega sin referencia / cotiz no aprobada | Bandeja / aviso | Auto-rechazo |
| C3 | ¿Hay que subir PDF o basta el DTE del partner? | Partner + carga manual opcional | Solo referencia de folio |
| C4 | ¿La cotización se “envía” al proveedor desde el ERP? | No (interno → OC) | Sí, tras aprobar |

---

## 3. Mensaje corto para la demo

1. **Ventas:** pedido interno (OV) ≠ factura SII. Quien aprueba no factura; el solicitante confirma y emite desde su OV.  
2. **Stock:** al autorizar se **reserva** 7 días; al confirmar sale de bodega. Ver Insumos › Stock.  
3. **Emitir:** ya no hay factura libre; elige OV. Sin CAF queda borrador.  
4. **Compras:** traemos el dibujo; **no cambiamos código** hasta que Almahue elija A o B.
