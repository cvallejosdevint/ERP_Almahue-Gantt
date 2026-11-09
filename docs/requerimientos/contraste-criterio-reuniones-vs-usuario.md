---
name: almahue-criterio-contraste
description: >-
  Guía y contraste metodológico entre la interpretación literal/teórica de las reuniones
  por parte de la IA y el criterio práctico operativo de terreno exigido por el usuario (Carlos).
  Usar proactivamente antes de diseñar o codificar requerimientos derivados de reuniones, minutas
  o solicitudes de usuarios en el ERP Almahue para evitar sobre-ingeniería, flujos burocráticos
  innecesarios y regresiones visuales.
---

# Contraste Canónico: Interpretación de Reuniones (IA) vs Criterio Operativo Real (Carlos)

> **Propósito del Documento:**  
> Analizar sistemáticamente la brecha existente entre la forma en que el asistente (IA) interpreta inicialmente las grabaciones/minutas de las reuniones y la forma en que **Carlos (Director de Proyecto / Usuario)** corrige, aterriza y exige las implementaciones en el ERP Almahue.  
> Este documento sirve de base para la skill `almahue-criterio-contraste` a fin de que ningún agente futuro caiga en sobre-ingeniería abstracta o distorsione la ergonomía operativa de terreno.

---

## 1. Diagnóstico de la Brecha Cognitiva

```
┌─────────────────────────────────────────────────────────┐
│     FUENTE: REUNIÓN / CLIENTE (Agustín, MJ, Lupe)       │
│  "Queremos controlar quién autoriza y que se ordene..."  │
└───────────────────────────┬─────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
┌───────────────────────────┐ ┌───────────────────────────┐
│  INTERPRETACIÓN IA        │ │  CRITERIO REAL (CARLOS)   │
│  (Sesgo Teórico/Académico)│ │  (Pragmatismo Operativo)  │
├───────────────────────────┤ ├───────────────────────────┤
│ • Sobre-ingeniería de grafos│ • Flujo vertical legible   │
│ • Reglas en todos los nive-│ • La base no aprueba, solo │
│   les (incluyendo la base)│   digita (sin fricción)   │
│ • Cajas apretadas lado a  │ • Eslabones apilados uno  │
│   lado en horizontal      │   sobre otro con badges   │
│ • Replicar compras en ven-│ • Criterio de negocio dife-│
│   tas (cadenas en OV)     │   renciado (OV valida stk)│
│ • Modales compactos       │ • Modales anchos de tra-  │
│ • Datos mock inventados   │   bajo y BD real conectada│
└───────────────────────────┘ └───────────────────────────┘
```

### 1.1 El Sesgo de la IA (Teórico / Literalista)
1. **Literalismo sin filtro:** Toma cualquier idea exploratoria o pregunta abierta de una reunión como un requerimiento arquitectónico estricto.
2. **Hiper-generalización:** Si una regla aplica a Gerencia, asume que debe aplicar idéntica a los Asistentes de Riego y Operadores de Cuadrilla.
3. **Ceguera espacial en UI:** Modela árboles teóricos en horizontal (`display: flex; flex-direction: row;`) sin considerar que las pantallas tienen ancho limitado y los usuarios leen de arriba a abajo.
4. **Burocratización del flujo:** Asume que más pasos, estados intermedios y wizards significan mayor calidad, cuando en terreno representan fricción destructiva.
5. **Aislamiento en Mocks:** Tiende a resolver interfaces con 2 o 3 usuarios ficticios (`user1`, `user2`), sin confrontar la dotación real de la empresa ni sus roles reales.

### 1.2 El Criterio de Carlos (Pragmático / Operativo de Terreno)
1. **La base operativa solo emite:** Quienes están en el peldaño inferior (asistentes, administrativos de campo, bodegueros) no configuran condiciones de aprobación; su único rol es digitar y emitir.
2. **La lógica condicional (AND/OR) solo existe donde hay decisión compartida:** Si dos o más jefaturas comparten un mismo nivel de decisión, se debe configurar explícitamente si basta la firma de uno (OR) o se exige la de ambos (AND).
3. **Ergonomía visual vertical:** Las aprobaciones y escalamientos deben verse **uno arriba del otro** (secuencial vertical claro) con badges distintivos, nunca cajas apretadas que recorten nombres o montos.
4. **Respeto estricto al Sistema de Diseño (`almahue-diseno`):** Modales anchos (`max-w-5xl` / `max-w-6xl`), botones con colores estandarizados por acción (verde para guardar, azul para crear, rojo para eliminar/inactivar, gris para cancelar), tablas legibles y sin márgenes arbitrarios.
5. **Integración con datos reales de la BD:** No inventar usuarios aislados. Integrar toda la dotación de la empresa con sus respectivos correos, RUTs y cargos para que el organigrama refleje la realidad de Almahue.

---

## 2. Matriz de Casos Reales: IA vs Correcciones de Carlos

A continuación se detallan los casos más relevantes donde se evidenció esta discrepancia y cómo Carlos redefinió la arquitectura:

| # | Área / Funcionalidad | Lo que la IA interpretó (De la reunión / código) | Lo que Carlos corrigió y exigió | Causa Raíz de la Desviación |
|---|---|---|---|---|
| **1** | **Estructura de Ramas (Organigrama)** | Asumió un único vértice jerárquico absoluto (árbol singleton) sin permitir ramas paralelas en Nivel 1. Al crear una segunda rama en Nivel 1, la IA no la mostraba o rompía el layout. | **Permitir múltiples ramas en Nivel 1** (ej. dos gerencias o ramas de supervisión general independientes) y poder bautizarlas libremente. | La IA modeló un árbol binario matemático en vez de una estructura empresarial flexible de grupos corporativos. |
| **2** | **Disposición de Eslabones Paralelos** | Colocó los eslabones en paralelo uno al lado del otro horizontalmente, provocando que las cajas se achicaran, los textos se cortaran y se perdiera la proporción. | **"Hagamos que sí o sí se vean uno arriba del otro aunque sean eslabones AND/OR"**. Flujo vertical uniforme con badges claros (`Paralelo (OR)` o `Paralelo (AND)`). | La IA confundió "lógica paralela" con "disposición geométrica horizontal". |
| **3** | **Configuración del Nivel Base (Rango 4 / Asistentes)** | Exigía configurar montos topes, banderas de aprobación y lógica de firma en el nivel más bajo (Rango 4). | **"La idea es que solo el nivel más bajo pueda contener todos los integrantes sin configurar su aprobación ya que son la base"**. Son emisores/digitadores puros. | La IA aplicó recursión ciega del algoritmo de aprobación a todos los nodos del árbol. |
| **4** | **Reglas AND / OR en Jefaturas** | No dejaba claro quién aprueba cuando hay varios miembros en un cargo (si ambos, cualquiera o si dependía del monto). | **Configuración explícita AND vs OR solo a partir del Rango 3 hacia arriba**: Si se comparte puesto, el modal debe permitir definir claramente si firman todos (AND) o cualquiera (OR). | Ambigüedad en la minuta no resuelta por la IA; no preguntó cómo opera la doble firma en terreno. |
| **5** | **Sentido de la Escala Jerárquica (3.1 vs 3.2)** | Invirtió los niveles colocando 3.1 como si fuera superior a 3.2 o escalando hacia abajo en la pantalla. | **Orden corregido y coherente con el escalamiento natural:** 3.1 (Subjefatura / primer tramo) escala hacia arriba a 3.2 (Jefatura General / tramo mayor). | La IA leyó el orden numérico textual sin asociarlo a la dirección de la delegación de autoridad. |
| **6** | **Población de Usuarios y Dotación** | Usó 2 usuarios de prueba hardcodeados (`Admin`, `Natalia`) en los mocks y pruebas e2e. | **"Hay que usar más usuarios para ser los eslabones más bajos, la idea es que corrijas toda la BD de usuarios y la integres aquí"**. Se mapeó la nómina real con 12+ usuarios por áreas y fundos. | Preferencia perezosa de la IA por stubs mínimos para que "el test pase" en lugar de validar con datos reales de negocio. |
| **7** | **Ancho y Diseño del Modal de Eslabón** | Construyó un modal angosto (`max-w-md`), centrado, con botones y estilos CSS ad-hoc ajenos a la aplicación. | **"La pantalla de configurar eslabón debería usar más el ancho de la página... audita los cambios y valida que sigue la skill de diseño en colores, formas y ubicaciones"**. Modal amplio (`max-w-4xl`/`5xl`), inputs consistentes y botones normalizados. | La IA no consultó la skill obligatoria `almahue-diseno` antes de implementar componentes visuales. |
| **8** | **Cotizaciones en Compras (D11)** | En Reu6 se habló de cotizaciones y la IA diseñó un flujo completo con menú de Cotizaciones, estados y conversión a OC. | **"El documento de arranque de compras es la OC. La cotización es solo una referencia opcional (tipo/folio/fecha) dentro de la OC; no hay CRUD de Cotizaciones"**. | La IA tomó el deseo teórico de un consultor y no la operación real de Lupe ("solo nos piden la OC y generamos la OC"). |
| **9** | **Aprobaciones en Ventas / OV (D4)** | La IA asumió simetría entre Compras y Ventas: diseñó una bandeja de aprobación y estados pendientes para Órdenes de Venta. | **"Cadena de aprobación SOLO Compras (OC). Se eliminó la cadena de OV. Guardar valida stock y deja CONFIRMADA; se factura directo en Emitir DTE"**. | Asunción de simetría teórica: "si compras aprueba montos, ventas también debe aprobar". En fruta/exportación la venta es inmediata contra stock. |
| **10** | **Asignación de Cuentas Contables en Emisión** | La IA intentó obligar al usuario a elegir cuentas contables al emitir cada factura o nota de venta en el wizard de emisión. | **Emisión limpia sin cuentas contables**: el DTE se emite como documento tributario y las cuentas contables se asignan centralizadamente en el **Libro de Ventas**. | La IA mezcló el rol de facturación comercial con el rol de contabilización contable. |

---

## 3. Los 5 Principios de Diseño Operativo de Carlos

Para evitar que la IA vuelva a desviarse, todo desarrollo futuro debe contrastarse contra estos cinco principios fundamentales:

### Principio 1: "La Base solo Digita" (Zero Fricción Operativa)
> *En los niveles operativos no hay burocracia de aprobación.*  
- El Rango 4 (o nivel base) es el punto de entrada de datos (digitadores, asistentes, inspectores de campo).
- No se les exige configurar topes de aprobación, cadenas de mando ni reglas AND/OR.
- Solo contienen la lista de usuarios habilitados para emitir el documento.

### Principio 2: "Ergonomía Vertical y Legibilidad Directa"
> *Si compite la teoría de grafos con la legibilidad humana, gana la legibilidad humana.*  
- Los flujos de decisión y jerarquías se representan verticalmente: de abajo hacia arriba (escalamiento) o de arriba hacia abajo (supervisión).
- Aunque dos cargos actúen en paralelo, se apilan verticalmente con badges explicativos (`Paralelo OR` / `Paralelo AND`), evitando que las tarjetas colapsen horizontalmente.
- Nombres de personas, cargos y montos deben ser visibles a primer golpe de vista, sin truncar textos con elipsis innecesarias.

### Principio 3: "Condiciones AND/OR Exclusivamente en Puestos Compartidos"
> *No inventes bifurcaciones complejas si no hay dos personas en el mismo escalón de decisión.*  
- La disyunción (OR) o conjunción (AND) solo tiene sentido cuando un mismo tramo jerárquico tiene dos o más responsables asignados.
- El sistema debe preguntar de forma clara y directa:  
  *¿Basta con que firme uno de ellos (Cualquiera - OR)?* o *¿Se requiere la firma de todos (Mancomunada - AND)?*

### Principio 4: "Estandarización Rigurosa de Pantalla (`almahue-diseno`)"
> *No inventar paletas, estilos ni tamaños particulares por pantalla.*  
- **Modales de configuración:** Siempre amplios (`max-w-4xl`, `max-w-5xl` o ancho disponible), nunca cajitas apretadas de 400px.
- **Acciones y botones:**
  - `Guardar` / `Confirmar`: Verde (`bg-emerald-600 hover:bg-emerald-700 text-white`).
  - `Crear` / `Nuevo`: Azul (`bg-blue-600 hover:bg-blue-700 text-white`).
  - `Eliminar` / `Inactivar`: Rojo (`bg-rose-600 hover:bg-rose-700 text-white`).
  - `Cancelar` / `Cerrar`: Gris (`bg-gray-100 hover:bg-gray-200 text-gray-700 border border-gray-300`).
- **Totales y cifras:** Siempre en tarjetas plegables o encabezados visibles, nunca escondidos en footers secundarios.

### Principio 5: "Separación Estricta de Roles de Negocio"
> *No forzar al operador de campo o al facturador a realizar tareas contables o administrativas complejas.*  
- Quien emite un DTE no tiene por qué saber la cuenta contable de imputación (lo hace el contador en el Libro).
- Quien emite una OV no pasa por una mesa de aprobación financiera si el stock físico en bodega está validado.
- Quien hace una OC incluye la cotización como dato informativo de respaldo, no como un documento transaccional que bloquee la compra.

---

## 4. Protocolo de Contraste Pre-Implementación (Checklist de la Futura Skill)

Antes de que un agente o desarrollador escriba código tras analizar una reunión o requerimiento, debe responder obligatoriamente este checklist de 6 preguntas:

```markdown
### Checklist de Contraste Operativo Almahue

1. [ ] ¿Estoy creando un flujo o pantalla porque alguien lo mencionó al pasar en una reunión, 
       o porque responde a una necesidad transaccional concreta validada por el usuario?
2. [ ] ¿El nivel más bajo de este módulo está sobre-configurado? 
       (Verificar: si son asistentes/operadores, deben solo emitir sin reglas de aprobación).
3. [ ] ¿La interfaz propuesta se lee cómodamente en vertical sin comprimir tarjetas ni cortar textos?
4. [ ] ¿Los modales de edición usan el ancho adecuado (mínimo max-w-4xl) y los botones respetan 
       la paleta semántica de la skill `almahue-diseno`?
5. [ ] ¿Estoy utilizando la nómina real de usuarios y roles de la base de datos, o caí en 
       la tentación de poner 2 mocks estáticos para salir del paso?
6. [ ] ¿Estoy mezclando roles? (Ej: exigir imputación contable al emitir, o exigir aprobación 
       financiera donde solo se requería validación de inventario).
```

---

## 5. Próximos Pasos para Convertir en Skill

1. Copiar este documento como base a `.agents/skills/almahue-criterio-contraste/SKILL.md`.
2. Integrar el prompt de validación a los subagentes ejecutados por `almahue-analisis-reunion` (especialmente en la fase 4: *Contraste con el Código* y fase 2: *Plan de Integración*).
3. Registrar la regla en `AGENTS.md` bajo la sección de directrices prioritarias de análisis.

