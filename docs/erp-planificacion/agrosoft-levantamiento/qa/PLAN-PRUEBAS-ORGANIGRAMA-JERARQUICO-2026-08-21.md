# Plan QA — organigrama jerárquico mixto SIMPLE / AND / OR (21/08)

**Objetivo.** Una cadena de Compras tipo packing/agro: digitador → jefe de área (1) → comité (2) → gerencia (1). Cubrir montos que cortan en cada eslabón, aprobar todo el tramo, rechazar en cada nivel, y ver **todos** los integrantes en el seguimiento.

No reset BD. EMP-EXPORT. Prefijo `QA-ORG-2108-*`. PIN `4821`. Password `demo123`. Admin parametriza; no cierra cadenas salvo override 1 caso.

Un usuario = un grupo Compras: **no reutilizar** SOL/AP-S/AND/OR del ciclo `QA-APR-2108`.

---

## Organigrama A — comité AND (firma dual)

```
SOL-ORG  →  JEFE (SIMPLE, tope $200.000)
         →  COMITÉ AND (dos personas, tope $800.000)
         →  GERENCIA (SIMPLE, sin tope)
```

| Id | Email | Rol |
|---|---|---|
| SOL-ORG | `qa.org.sol@almahue.cl` | Digitador; Órdenes write; sin bandeja |
| JEFE | `qa.org.jefe@almahue.cl` | N1 SIMPLE $200.000 |
| COM-A | `qa.org.coma@almahue.cl` | Comité AND |
| COM-B | `qa.org.comb@almahue.cl` | Comité AND |
| GER | `qa.org.ger@almahue.cl` | N3 SIMPLE sin tope |

Grupo `GRP-QA-ORG-AND`: miembros SOL-ORG + JEFE (jefa de área). Aprobador inicial = JEFE.  
Escala: JEFE SIMPLE 200k → nodo COM-A **AND** [COM-A, COM-B] 800k → GER sin tope.

Simulador (antes de emitir):

| ID | Monto | Cadena esperada |
|---|---|---|
| SIM-1 | 150.000 | JEFE |
| SIM-2 | 400.000 | JEFE → AND(COM-A, COM-B) |
| SIM-3 | 1.200.000 | JEFE → AND → GER |
| SIM-AUTO | JEFE solicita 150.000 | sin auto-aprobación: AND (monto ≤ 800k) **o** GER si el motor salta el comité; evidenciar |

---

## Organigrama B — comité OR (basta uno)

Misma forma, otro grupo (solicitante distinto):

`SOL-OR2` `qa.org.solor@almahue.cl` → `JEFE-OR` 200k SIMPLE → `ORA`+`ORB` **OR** 800k → `GER-OR` sin tope.

Emails: `qa.org.jefeor@` `qa.org.ora@` `qa.org.orb@` `qa.org.geror@almahue.cl`. Grupo `GRP-QA-ORG-OR`.

Simulador $400k: JEFE-OR → OR(ORA, ORB). $1.200.000: + GER-OR.

---

## Casos runtime (OC + referencia cotiz opcional)

### AND

| ID | Monto | Qué hacer | Esperado visual |
|---|---|---|---|
| JER-1N | 150k | JEFE PIN | 1 eslabón SIMPLE; OC APROBADO |
| JER-2N | 400k | JEFE PIN; COM-A PIN (no cierra); COM-B PIN | Tras N1: 2 del AND en espera. Tras 1 AND: uno aprobó, el otro espera. Cierre: ambos «aprobó» |
| JER-3N | 1.200k | JEFE → COM-A+COM-B → GER | Tres eslabones; el del medio **siempre 2 nombres** |
| JER-R1 | 150k | JEFE rechaza + motivo | 1 persona en el eslabón; motivo visible |
| JER-R2 | 400k | JEFE OK; COM-A rechaza + motivo | AND: quien rechazó + el otro **gris omitido** (2 nombres) |
| JER-R3 | 1.200k | dual AND OK; GER rechaza + motivo | Pasos 1–2 done (AND con 2); GER rechazó |

### OR

| ID | Monto | Qué hacer | Esperado |
|---|---|---|---|
| JER-OR | 400k | JEFE-OR PIN; **ORA** PIN (ORB no firma) | OR: ORA aprobó, ORB gris omitido; OC APROBADO |
| JER-OR-3 | 1.200k | JEFE-OR → un OR → GER-OR PIN | Tres eslabones; medio 2 nombres |

---

## Informe

`qa/resultados/2026-08-21-organigrama-jerarquico.md`. Sin JWT. Folios OC. Screenshot mental: cuántos nombres por eslabón.

Si el simulador no arma 3 pasos (escalaA mal enlazada), BLOCKED de config, no SKIP. Arreglar escala (N1 escala al nodo AND, AND escala a GER) y reintentar.
