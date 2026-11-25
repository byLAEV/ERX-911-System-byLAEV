# ERX-CONSENSUS-SOURCE-INSPECTION-001
## Registro de inspección textual y delimitación de alcance — ERX-CONSENSUS-001 v0.1

| Campo | Valor |
|---|---|
| Identificador | ERX-CONSENSUS-SOURCE-INSPECTION-001 |
| Versión | 0.1.0 |
| Estado | EVIDENCIA DE WP-0.3 — PENDIENTE DE DISPOSICIÓN LAEV |
| Fuente inspeccionada | `docs/Consenso ERX byLAEV` (texto UTF-8) |
| Git Blob SHA-1 de la fuente | `64154f504b0a1ac48f76a438cf60f368e062eab6` |
| Tamaño de la fuente | 15,237 bytes |
| Fuente de planificación comparada | `docs/### ERX-ROADMAP-001`, versión 1.0 |
| Autoridad | LAEV / byLAEV |
| Fecha de inspección | 2026-11-24 |

## 1. Propósito y límite

Este registro documenta la inspección directa del texto del consenso, confirma su identidad frente a la cita del Roadmap y resume lo que el documento establece y lo que declara fuera de su alcance.

No aprueba ni modifica ERX-CONSENSUS-001 v0.1. No transforma su estado de propuesta en norma aprobada. No sustituye las decisiones de LAEV ni constituye una especificación técnica de consenso implementable.

## 2. Identidad documental confirmada

La portada/control textual de la fuente declara:

- Título: ERX byLAEV — Documento normativo, Protocolo de Consenso.
- Identificador: ERX-CONSENSUS-001.
- Versión: 0.1 — Propuesta normativa.
- Estado: Documento de diseño para revisión.
- Autoría: LAEV / byLAEV.
- Ámbito: Sistema ERX de comunicación y registro de emergencias 911.

ERX-ROADMAP-001 v1.0, sección 1, cita ERX-CONSENSUS-001 v0.1 como marco de consenso y referencia de coordinación que deberá completarse antes de incorporarse a una implementación multiinstitucional.

**Resultado:** la identidad y versión del texto coinciden con la referencia del Roadmap. DOC-ISS-002 queda resuelto en su componente de identidad. La propuesta documental no queda aprobada por esta verificación.

## 3. Inventario fiel del contenido de la fuente

| Sección fuente | Materia declarada |
|---|---|
| 1. Objeto | Define propósito, principios, responsabilidades y reglas funcionales del consenso ERX; establece tres objetivos independientes y complementarios |
| 2. Definición | Verificación distribuida por participantes institucionalmente autorizados; cada consenso tiene objeto, entradas, participantes, criterios y resultado |
| 3. Principios | Independencia de comunicaciones y consensos; evidencia; trazabilidad; no eliminación; independencia de atención de emergencia; responsabilidad institucional; distinción entre correlación y duplicidad |
| 4. Triple Consenso | Consenso 01: oficialidad de comunicación; Consenso 02: conformidad del protocolo; Consenso 03: correlación de acontecimientos |
| 5. Participantes | Infraestructura institucional, operadores, centrales receptoras, sistema ERX y participantes validadores; roles de producción de evidencia y validación distinguidos |
| 6. Separación por etapas | Recepción individual; contacto/recepción de denuncia; correlación y consenso de acontecimientos; el consenso no es condición para crear una llamada individual |
| 7. Registro de resultados | Registro independiente con ID, tipo, comunicaciones, participantes, evidencias, criterios, versión de reglas, resultado, fecha/hora, autenticación, discrepancias y revisión |
| 8. Relación con UTXO | UTXO controla estados/transiciones; consenso verifica condiciones/relaciones; mecanismos complementarios, no equivalentes |
| 9. Discrepancias | Diferencia falta de información, evidencia insuficiente, conflicto, incumplimiento, falta de autenticidad e imposibilidad de correlación; conserva registros y habilita revisión |
| 10. Invariantes | Identidad individual; consenso no requerido para existencia de recepción; verificaciones separadas; correlación sin borrar llamadas; resultados pendientes/disputados; historial preservado |
| 11. Alcance | Declara que no desarrolla código, algoritmos criptográficos específicos, JSON/UTXO definitivos, quórum matemático, número mínimo de validadores, protocolos entre centrales, correlación automática ni auditoría completa |
| 12. Documentos derivados | Enumera arquitectura técnica y tres especificaciones de consenso, más fases de recepción, contacto y correlación |

## 4. Reglas expresas relevantes para ERX

La fuente afirma expresamente:

1. Una llamada individual mantiene su identidad transaccional, aunque se relacione con otras.
2. Los tres consensos verifican propiedades distintas; aprobar uno no aprueba los otros.
3. Una comunicación no requiere consenso colectivo para existir como registro de recepción.
4. La oficialidad, conformidad de protocolo y correlación de acontecimiento se verifican separadamente.
5. La correlación no elimina la identidad individual de las llamadas.
6. Resultados negativos, discrepancias o falta de consenso no autorizan borrar comunicaciones originales.
7. La verificación no debe retrasar ni bloquear la atención de emergencia.
8. Un resultado posterior debe generar nueva evidencia vinculada, sin borrar el historial previo.
9. UTXO y consenso son mecanismos complementarios, no equivalentes.

## 5. Elementos que la fuente declara pendientes o fuera de alcance

No se presentan como reglas ya definidas en ERX-CONSENSUS-001 v0.1:

- Número mínimo de validadores, quórum y regla matemática de aceptación.
- Independencia, elegibilidad y peso institucional de participantes validadores.
- Mecanismo detallado para resolver desacuerdos y ausencia de consenso.
- Algoritmos criptográficos concretos y reglas completas de autenticación de validadores.
- Estructuras JSON y UTXO definitivas asociadas a cada consenso.
- Protocolo completo de comunicación entre centrales.
- Algoritmo de correlación automática y sus criterios/umbrales.
- Procedimientos completos de auditoría.
- Especificaciones técnicas derivadas y sus criterios de aceptación.

La sección 12 propone documentos derivados, pero su enumeración no equivale a que estén desarrollados, aprobados o implementados.

## 6. Correspondencia con ERX-ROADMAP-001

### Correspondencia confirmada
- Roadmap §1 incorpora ERX-CONSENSUS-001 v0.1 como referencia de coordinación.
- Roadmap §11.3 establece que el consenso debe evolucionar mediante una especificación independiente antes de utilizarse como fundamento de coordinación multiinstitucional.
- Roadmap §11.3 exige determinar qué constituye una aceptación válida, qué ocurre ante desacuerdos y si la coordinación distribuida es necesaria.
- La fuente de consenso establece los tres objetivos, los principios de evidencia y las salvaguardas de no interferencia con la atención.

### Límite de la comparación
La coincidencia de identidad y propósito no significa que el documento de consenso esté completo para uso multiinstitucional. La propia fuente y el Roadmap reservan la definición operativa para trabajo posterior.

## 7. Disposición documental

- DOC-ISS-002 — identidad de fuente: **RESUELTO POR EVIDENCIA**.
- DOC-ISS-011 — autoridad, estado de propuesta y completitud operativa: **ABIERTO; requiere disposición LAEV**.
- No se declara contradicción directa entre la fuente de consenso y el ciclo UTXO de comunicación por el mero hecho de que tengan objetos diferentes. El consenso verifica propiedades y relaciones; UTXO representa estados/transiciones.
- La asignación del documento técnico derivado, su paquete de requisitos y sus criterios de aceptación corresponde a LAEV. Debe quedar satisfecho antes de coordinación multiinstitucional, conforme al Roadmap.
- La atención de emergencia debe permanecer independiente de la disponibilidad o resultado del consenso.

## 8. Conclusión

ERX-CONSENSUS-001 v0.1 es una fuente identificada y leída, con un marco conceptual de Triple Consenso e invariantes documentales/operativas relevantes. Su propio estado es **Propuesta normativa / Documento de diseño para revisión** y su alcance excluye varias reglas indispensables para una especificación operacional completa.

La siguiente decisión no es localizar ni volver a identificar el documento. Es determinar su estatus/autoridad y encargar —con alcance y aceptación definidos— la especificación técnica que complete las reglas diferidas, antes de su uso multiinstitucional.

---
Fin del registro de inspección.
