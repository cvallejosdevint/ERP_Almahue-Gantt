# Seed y simulador

Hay **tres** juegos. No mezclar: EMP-BOOT (Laura), EMP-1 (Jorge/S1–S6) y holding Export/Services.

Password operativo: `demo123`. Admin: `admin@almahue.local` / `Admin123!`. PIN: `4821`.

## A. QA desde cero (`seed:qa-desde-cero`, EMP-BOOT)

Admin **no** es miembro ni nodo. N1 tope **$500.000** → **Laura Soto** (`lsoto@almahue.cl`) final. Override implícito del admin: fuera de este ciclo.

| Persona | Email | Rol en el ciclo |
|---|---|---|
| Admin | admin@almahue.local | Parametriza; no cierra cadenas |
| Luis Herrera | lherrera@almahue.cl | Solicita OC |
| María González | mgonzalez@almahue.cl | N1 Compras |
| Camila Soto | csoto@almahue.cl | Solicita OV |
| Pablo Núñez | pnunez@almahue.cl | N1 Ventas |
| Laura Soto | lsoto@almahue.cl | N2 final (todos los módulos) |
| Diego Morales | dmorales@almahue.cl | Proforma |
| Ricardo Muñoz | rmunoz@almahue.cl | N1 Contratistas |
| Tomás Vidal / Ana Torres | tvidal@ / atorres@ | Bodega / tesorería |

Método: `qa/resultados/2026-08-18-ciclo-desde-cero-metodo.md`.

## B. Seed demo EMP-1 (`npm run seed` + `seed:aprobaciones-f2`)

Destruye grupos de EMP-1. Usuarios clásicos del **simulador S1–S6**. El admin **no** debe figurar en la escala de producto; esta tabla es el seed histórico de demo.

| Persona | Email | Id | Notas |
|---|---|---|---|
| Admin | admin@almahue.local | U-1 | Mantenedor; override, no nodo |
| Jorge Sánchez | jsanchez@almahue.cl | U-3 | Cadena GRP-COMPRAS-1; bandeja runtime (sin `compras:read` global) |
| María González | mgonzalez@almahue.cl | U-6 | Jefa; `compras:read` |
| Claudia Vargas | cvargas@almahue.cl | U-7 | AdminConcepto Compras |
| Ricardo Muñoz | rmunoz@almahue.cl | U-8 | AdminConcepto Contratistas |
| Luis Herrera | lherrera@almahue.cl | U-15 | Solicitante OC |
| Laura Soto | (seed f2) | — | Co-aprobador AND en S4 |

Claudia: 12 grupos Compras. Ricardo: 8 Contratistas.

## C. QA holding Almahue (`seed:qa-holding`)

Emula las dos sociedades del portal GoSocket QA sin documentos de negocio: `EMP-EXPORT` (`77.032.638-9`, ALMAHUE EXPORT SPA) y `EMP-SERVICES` (`77.032.639-7`, ALM SERVICES SPA). `EMP-BOOT` se deja existente pero inactiva.

Comandos:

```bash
cd ERP/erp_back
npm run reset:superadmin  # opcional si no existe U-1
npm run seed:qa-holding
```

Admin `U-1` queda con empresa primaria `EMP-EXPORT` y acceso a ambas. Los operadores son disjuntos por empresa; admin no es miembro ni nodo de grupos/escalas. Password operativo: `demo123`. Admin: `Admin123!`. PIN aprobadores: `4821`.

### EMP-EXPORT

Organigrama de 2 niveles: N1 tope $500.000 -> Natalia Bravo sin tope.

| Persona | Email | Rol | Jefe | Tope | PIN |
|---|---|---|---|---:|---|
| Natalia Bravo | nbravo@almahuexport.cl | Gerencia | - | sin tope | si |
| Felipe Castro | fcastro@almahuexport.cl | Compras N1 | Natalia | 500.000 | si |
| Elena Rojas | erojas@almahuexport.cl | Compras solicitante | Felipe | - | no |
| Andres Pino | apino@almahuexport.cl | Ventas N1 | Natalia | 500.000 | si |
| Valentina Diaz | vdiaz@almahuexport.cl | Ventas solicitante | Andres | - | no |
| Bruno Lagos | blagos@almahuexport.cl | Contratistas N1 | Natalia | 500.000 | si |
| Paula Mendez | pmendez@almahuexport.cl | Contratistas solicitante | Bruno | - | no |
| Hugo Saez | hsaez@almahuexport.cl | Bodega | - | - | no |
| Irene Soto | isoto@almahuexport.cl | Tesoreria | - | - | no |
| Clara Vidal | cvidal@almahuexport.cl | Contabilidad / AdminConcepto Compras | - | - | si |

| Grupo | Modulo | Miembros | Cadena |
|---|---|---|---|
| GRP-EX-COMPRAS | Compras | Elena, Felipe, Natalia | Felipe 500k -> Natalia |
| GRP-EX-COMERCIAL | Comercial | Valentina, Andres, Natalia | Andres 500k -> Natalia |
| GRP-EX-CTR | Contratistas | Paula, Bruno, Natalia | Bruno 500k -> Natalia |

### EMP-SERVICES

Organigrama distinto de 3 niveles para Compras/Comercial: N1 $200.000 -> N2 $800.000 -> German Ortiz sin tope. Contratistas es 1 nivel: Daniela sin tope.

| Persona | Email | Rol | Jefe | Tope | PIN |
|---|---|---|---|---:|---|
| German Ortiz | gortiz@almservices.cl | Gerencia N3 | - | sin tope | si |
| Rodrigo Salas | rsalas@almservices.cl | Gerencia N2 | German | 800.000 | si |
| Sofia Lagos | slagos@almservices.cl | Compras N1 | Rodrigo | 200.000 | si |
| Ignacio Perez | iperez@almservices.cl | Compras solicitante | Sofia | - | no |
| Catalina Vega | cvega@almservices.cl | Ventas N1 | Rodrigo | 200.000 | si |
| Martin Rios | mrios@almservices.cl | Ventas solicitante | Catalina | - | no |
| Daniela Fuenzalida | dfuenzalida@almservices.cl | Contratistas N1 | German | sin tope | si |
| Oscar Nunez | onunez@almservices.cl | Contratistas solicitante | Daniela | - | no |
| Beatriz Molina | bmolina@almservices.cl | Bodega | - | - | no |
| Leonor Campos | lcampos@almservices.cl | Tesoreria | - | - | no |
| Patricio Henriquez | phenriquez@almservices.cl | Contabilidad / AdminConcepto Contratistas | - | - | si |

| Grupo | Modulo | Miembros | Cadena |
|---|---|---|---|
| GRP-SV-COMPRAS | Compras | Ignacio, Sofia, Rodrigo, German | Sofia 200k -> Rodrigo 800k -> German |
| GRP-SV-COMERCIAL | Comercial | Martin, Catalina, Rodrigo, German | Catalina 200k -> Rodrigo 800k -> German |
| GRP-SV-CTR | Contratistas | Oscar, Daniela | Daniela sin tope |

## Simulador (esperados)

| ID | Caso | Esperado |
|---|---|---|
| S1 | Luis 200k GRP-COMPRAS-1 | Jorge (suplencia María) |
| S2 | Diego 500k GRP-COMPRAS-2 | Pablo Núñez |
| S3 | María 100k GRP-COMPRAS-1 | Jorge (sin auto-aprobación) |
| S4 | Bruno 800k GRP-COMPRAS-6 AND | Laura Soto + co-aprobador |
| S5 | Luis 3M GRP-COMPRAS-1 | Jorge → Claudia (escala) |
| S6 | Diego 400k Contratistas | Pablo Núñez |

Seed: `npm run seed:aprobaciones-f2` (borra grupos/escalas/AdminConcepto de EMP-1).
