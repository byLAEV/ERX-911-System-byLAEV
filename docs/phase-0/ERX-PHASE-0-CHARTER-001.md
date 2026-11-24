# ERX-PHASE-0-CHARTER-001
## Definición y fundamento de FASE 0
### Gobierno y preparación del proyecto ERX byLAEV

| Campo | Registro |
|---|---|
| Proyecto | 911 — Sistema de Doble Gasto byLAEV |
| Sistema | ERX byLAEV |
| Identificador | ERX-PHASE-0-CHARTER-001 |
| Versión | 1.0.0 |
| Fase | FASE 0 — Gobierno y preparación del proyecto |
| Paquete de trabajo | WP-0.1 |
| Autoría y diseño | LAEV / byLAEV |
| Estado documental | APPROVED |
| Aprobación | LAEV — aprobación expresa registrada |
| Fecha de aprobación | 2026-11-23 |
| Documento rector de planificación | ERX-ROADMAP-001 v1.0 |

---

## 0. CONTROL DOCUMENTAL

### 0.1. Identificación y función

Este documento establece la definición, fundamento, propósito, objetivos, justificación, alcance, exclusiones, principios y criterios de finalización de la FASE 0 del proyecto ERX byLAEV.

Constituye el documento de apertura conceptual y organizativa de la fase y el entregable principal del paquete WP-0.1.

### 0.2. Fuentes y procedencia

La elaboración se basa en los siguientes documentos examinados:

- ERX-PROT-001 v1.1 — Protocolo institucional.
- ERX-ATLAS-001 v1.1 — Atlas institucional de arquitectura y diagramas.
- UTXO-911-001 v1.0 — Especificación funcional del ciclo UTXO de comunicación 911.
- ERX-ROADMAP-001 v1.0 — Plan maestro de fases.
- Respuesta técnica a las observaciones de ERX-ROADMAP-001 — documento de respuesta técnica.

ERX-ROADMAP-001 también referencia:

- ERX-CONSENSUS-001 v0.1 — Marco de consenso, señalado en el Roadmap como referencia de coordinación que deberá completarse antes de incorporarse a una implementación multiinstitucional.
- ERX-IMPL-PROPOSAL-001 — Propuesta de implementación institucional.

La referencia de estos dos últimos documentos se conserva como procedencia declarada por el Roadmap. Su archivo íntegro, versión vigente, disponibilidad y contenido deberán verificarse e inventariarse en WP-0.2. Este Charter no presume haberlos examinado ni completa su contenido por inferencia.

### 0.3. Naturaleza y autoridad

Documento de desarrollo y gobierno del proyecto. No sustituye las fuentes fundacionales, no modifica por sí mismo los documentos normativos y no prevalece sobre las reglas de autoridad documental que se establecerán en WP-0.3.

### 0.4. Registro de aprobación

Este documento fue aprobado expresamente por LAEV, sujeto a la incorporación de cuatro ajustes técnicos: (1) conservar las referencias documentales adicionales del Roadmap y marcar su verificación como pendiente; (2) precisar que los principios del Roadmap son restricciones de diseño y no pruebas de implementación; (3) explicitar la independencia de los ciclos UTXO de comunicación y disponibilidad del agente; y (4) permitir el traslado controlado de asuntos pendientes a fases posteriores, sin ocultarlos ni declararlos resueltos.

La aprobación se aplica a esta versión consolidada 1.0.0, que incorpora dichos ajustes.

---

# 1. IDENTIFICACIÓN DE LA FASE

**FASE 0 — GOBIERNO Y PREPARACIÓN DEL PROYECTO**

La FASE 0 constituye la primera etapa del desarrollo de ERX byLAEV.

Es una fase preparatoria destinada a organizar las condiciones documentales, arquitectónicas, técnicas y organizativas necesarias para desarrollar, implementar, verificar y posteriormente evaluar el sistema institucional.

Su ubicación al inicio del plan maestro responde a la necesidad de establecer reglas de desarrollo, procedencia y autoridad de fuentes, trazabilidad de requisitos y mecanismos de control antes de avanzar hacia el cierre normativo y la construcción del software.

La FASE 0 no es una etapa de implementación funcional de ERX. Prepara y gobierna el entorno documental y de trabajo bajo el cual deberán ejecutarse las fases posteriores.

# 2. PROPÓSITO

Establecer una estructura de gobierno, documentación, identificación, trazabilidad, planificación y control que permita desarrollar ERX byLAEV de manera ordenada, verificable y coherente con su arquitectura fundacional.

La fase busca preservar la continuidad entre documentos existentes, decisiones de diseño, requisitos identificados y futuros componentes de software. Cada modificación, decisión, requisito, dependencia y resultado deberá poder relacionarse con su procedencia y evidencia.

El trabajo distinguirá, sin confundir sus respectivas funciones:

- Arquitectura normativa y protocolo.
- Representación gráfica y documentación funcional.
- Modelo institucional de estados UTXO.
- Arquitectura de software.
- Implementación técnica.
- Verificación independiente.
- Integración, adopción y homologación institucional.

# 3. OBJETIVO GENERAL

Establecer y aprobar el marco documental, organizativo y de control necesario para ejecutar el desarrollo de ERX byLAEV conforme a ERX-ROADMAP-001, garantizando la identificación y preservación de las fuentes fundacionales, la jerarquía documental, la trazabilidad de requisitos y decisiones, el registro de riesgos y dependencias, la asignación de responsabilidades y el control verificable de las modificaciones del proyecto.

# 4. OBJETIVOS ESPECÍFICOS

1. **Consolidación documental:** identificar, inventariar y preservar los documentos que constituyen el fundamento del proyecto.
2. **Jerarquía documental:** establecer la relación entre documentos normativos, funcionales, gráficos, arquitectónicos, técnicos y de planificación.
3. **Identificación y versionado:** definir un sistema uniforme de identificación, nomenclatura, versiones y estados documentales.
4. **Organización del repositorio:** establecer el repositorio ERX como espacio de preservación, desarrollo, revisión y seguimiento.
5. **Índice maestro:** crear un registro centralizado de documentos, versiones, estados y relaciones.
6. **Identificación de requisitos:** extraer y clasificar requisitos existentes, distinguiendo obligaciones documentadas, requisitos de diseño, aspectos pendientes y decisiones abiertas.
7. **Registro de decisiones:** documentar contexto, alternativas, justificación y consecuencias de las decisiones arquitectónicas.
8. **Identificación de riesgos:** registrar riesgos documentales, técnicos, arquitectónicos e institucionales, así como sus dependencias y medidas de tratamiento.
9. **Gobernanza:** delimitar responsabilidades de diseño, protocolo, software, seguridad, revisión y validación.
10. **Control de modificaciones:** establecer procedimientos de revisión, aprobación, conservación de versiones anteriores y continuidad documental.
11. **Verificación de preparación:** comprobar que las condiciones para iniciar FASE 1 estén documentadas y que los asuntos pendientes estén identificados y tratados.

# 5. JUSTIFICACIÓN DE LA FASE

ERX comprende distintas disciplinas y responsabilidades que deben mantenerse coordinadas sin perder su independencia funcional. Su arquitectura contempla un protocolo institucional de comunicación 911, un modelo de estados UTXO, mecanismos criptográficos, evidencias temporales, almacenamiento institucional, integración de software y verificación independiente.

El desarrollo requiere un marco que conserve la coherencia entre documentos, decisiones y componentes, y que impida confundir una propuesta, una especificación, una implementación y una validación.

La FASE 0 responde a estas necesidades:

### 5.1. Continuidad documental
Evitar que nuevas versiones sustituyan o contradigan las fuentes originales sin procedimiento, justificación y trazabilidad.

### 5.2. Consistencia arquitectónica
Evitar que el desarrollo separado de componentes introduzca comportamientos incompatibles con las reglas del protocolo.

### 5.3. Trazabilidad
Relacionar cada requisito y decisión con una fuente documental o con una decisión nueva identificada como tal.

### 5.4. Control de evolución
Permitir que ERX evolucione mediante versiones identificables, revisables y recuperables.

### 5.5. Responsabilidad técnica
Distinguir quién diseña, implementa, revisa, aprueba y valida cada elemento.

### 5.6. Prevención de errores de gestión
Evitar que el cumplimiento administrativo de actividades sea interpretado como evidencia de funcionamiento, seguridad o aceptación institucional.

### 5.7. Preparación para el desarrollo normativo
Establecer las condiciones para abordar FASE 1, cuyo objetivo es cerrar formalmente las reglas del modelo de estados y del gasto único antes de desarrollar el motor transaccional.

# 6. ALCANCE DE TRABAJO

FASE 0 comprende los doce paquetes de trabajo definidos en WORKPLAN-FASE-0.md:

1. Definición y fundamento de la fase.
2. Identificación y consolidación del material fundacional.
3. Organización y jerarquía documental.
4. Identificación y control de documentos.
5. Creación y organización del repositorio ERX.
6. Elaboración del índice maestro y registro documental.
7. Identificación y clasificación de requisitos.
8. Registro de decisiones arquitectónicas.
9. Registro de riesgos y dependencias.
10. Gobernanza y responsabilidades.
11. Planificación y control de versiones.
12. Verificación y cierre formal.

El alcance incluye documentos, registros, matrices, procedimientos, criterios de aceptación y mecanismos de seguimiento necesarios para cumplir esos objetivos. También incluye identificar los asuntos cuya resolución corresponda a fases posteriores.

# 7. EXCLUSIONES DEL ALCANCE

FASE 0 no comprende:

1. **Cierre normativo definitivo:** no modifica ni declara cerradas las reglas normativas de ERX-PROT-001.
2. **Especificación definitiva UTXO:** no constituye la especificación completa de identificadores, estados, transiciones, consumo, concurrencia, atomicidad, idempotencia y recuperación. Estas materias deberán formalizarse principalmente en FASE 1.
3. **Desarrollo de software:** no implementa ERX Core, ERX Institutional Module ni ERX Verifier.
4. **Implementación criptográfica:** no desarrolla ni valida algoritmos, formatos de firma, estructuras de datos o mecanismos criptográficos definitivos.
5. **Integración productiva OTS:** no realiza integración ni envío productivo de sellos OpenTimestamps.
6. **Integración institucional:** no conecta sistemas reales de telefonía, localización, CAD, agentes, proveedores o centros 911.
7. **Validación operacional:** no certifica seguridad, interoperabilidad, disponibilidad ni funcionamiento institucional.
8. **Homologación:** no autoriza operar ERX en centros de emergencia ni sustituye las aprobaciones de autoridades competentes.

# 8. PRINCIPIOS DE DESARROLLO

Los principios siguientes se adoptan como restricciones y criterios rectores del desarrollo conforme a ERX-ROADMAP-001 v1.0. Su inclusión en este Charter no significa que estén implementados, probados o certificados. Su formalización verificable y su demostración técnica corresponden a las fases pertinentes.

| Principio | Condición establecida en el Roadmap | Tratamiento en FASE 0 |
|---|---|---|
| No interferencia | ERX nunca condiciona la atención de emergencias. | Preservar como restricción operativa prioritaria. |
| Gasto único | Ningún estado puede consumirse dos veces. | Registrar como fundamento del diseño UTXO. |
| Atomicidad | Consumo y creación de estados deben ser coherentes. | Registrar como requisito por formalizar y verificar. |
| Idempotencia | Repetir una solicitud no duplica sus efectos. | Registrar como requisito por formalizar y verificar. |
| Historial | Los acontecimientos anteriores no se eliminan por una transición. | Preservar trazabilidad e historial. |
| Identidad | Toda transición debe tener un emisor y una autorización verificables. | Registrar necesidades de identidad y autorización. |
| Privacidad | Los datos sensibles permanecen bajo custodia institucional. | Preservar como restricción de diseño y gobernanza. |
| Independencia temporal | OTS no condiciona el cierre ni la atención. | Mantener evidencia temporal fuera de la ruta crítica de atención. |
| Recuperación | Las interrupciones no deben resucitar estados consumidos. | Registrar como requisito de continuidad y recuperación. |
| Verificación | La evidencia debe poder comprobarse independientemente. | Mantener separación entre producción y verificación de evidencia. |
| Separación institucional | Cada centro conserva su autoridad y responsabilidad. | Preservar límites de autoridad entre instituciones. |

### 8.1. Separación obligatoria de los ciclos UTXO

Conforme a ERX-ROADMAP-001, ERX mantiene dos ciclos relacionados, pero independientes:

**Ciclo A — Comunicación 911**

- UTXO 01: Recepción.
- UTXO 02: Contacto y protocolo inicial.
- UTXO 03: Desarrollo y cierre.

Cada llamada posee su propio ciclo y expediente.

**Ciclo B — Disponibilidad del agente**

- DISPONIBLE.
- ASIGNADO / ACEPTADO.
- OCUPADO.
- LIBERACIÓN Y NUEVA DISPONIBILIDAD.

El ciclo de disponibilidad del agente tiene estados propios y no reutiliza los UTXO de la llamada. El UTXO 03 no sustituye el estado de disponibilidad del agente. Tampoco debe emitirse una nueva disponibilidad mientras el agente continúe ocupado, en pausa o sujeto a otra condición que impida recibir solicitudes.

La relación entre ambos ciclos se establece mediante referencias de identidad, asignación y sesión. Esta relación no fusiona sus estados ni sus condiciones de consumo y transición.

La formalización completa de identificadores, transiciones, invariantes, concurrencia, atomicidad y recuperación de ambos ciclos corresponde al trabajo normativo y técnico posterior, principalmente FASE 1.

### 8.2. Independencia de la evidencia temporal

La evidencia OTS y los procesos externos de sincronización deben mantenerse fuera de la ruta crítica de atención. Su generación, confirmación o disponibilidad no puede condicionar la recepción, atención, despacho ni cierre operativo de una emergencia. La respuesta técnica a las observaciones del Roadmap respalda que los procesos externos de evidencia temporal y sincronización se ejecuten de manera asíncrona respecto de las operaciones transaccionales locales.

### 8.3. Preservación de fuentes

Los documentos originales se conservan como referencias de procedencia. Las modificaciones se documentan en nuevas versiones o documentos derivados.

### 8.4. No inferencia silenciosa

Los vacíos, contradicciones y decisiones no resueltas permanecen identificados hasta que exista una resolución documentada.

### 8.5. Separación de responsabilidades

La autoridad de diseño, la implementación, la revisión y la validación independiente no deben confundirse.

### 8.6. Aprobación por evidencia

Ninguna fase se considera completada únicamente por haber producido archivos, ejecutado tareas o satisfecho listas administrativas. El avance requiere evidencias verificables y criterios de aceptación.

### 8.7. Continuidad

Toda modificación debe permitir reconstruir qué existía, qué cambió, por qué cambió y quién autorizó el cambio.

# 9. CRITERIOS DE FINALIZACIÓN

FASE 0 podrá declararse completada cuando se verifique el cumplimiento de los criterios de los doce paquetes de trabajo y de las siguientes condiciones generales:

- [ ] Fuentes conocidas inventariadas, preservadas o identificadas como faltantes.
- [ ] Versiones y procedencia de las fuentes registradas.
- [ ] Jerarquía documental y autoridad por materia definidas y aprobadas.
- [ ] Contradicciones y vacíos registrados con tratamiento asignado.
- [ ] Identificadores, nomenclatura, versiones y estados documentales definidos.
- [ ] Repositorio, accesos y control de cambios documentados.
- [ ] Índice maestro consistente con los documentos existentes.
- [ ] Requisitos identificados, clasificados y vinculados a una fuente documental o a una decisión nueva claramente señalada.
- [ ] Decisiones arquitectónicas aprobadas y pendientes registradas.
- [ ] Riesgos y dependencias con impacto, tratamiento, responsables y condiciones de resolución.
- [ ] Gobernanza, responsabilidades, revisión y aprobación definidas.
- [ ] Continuidad y conservación de versiones establecidas.
- [ ] Informe de cumplimiento y registro formal de cierre disponibles.
- [ ] Aprobación expresa de LAEV para el cierre de FASE 0.
- [ ] Autorización expresa para iniciar la fase siguiente.

Los asuntos técnicos que correspondan a FASE 1 o posteriores no tienen que resolverse anticipadamente durante FASE 0. Podrán trasladarse si están identificados, clasificados, vinculados a su fuente o decisión, justificados, asignados a una fase de resolución y aceptados expresamente en el proceso de cierre. Su traslado no equivale a declararlos resueltos ni a dispensar requisitos que el Roadmap exija para avanzar.

El criterio de avance establecido por ERX-ROADMAP-001 exige que todos los requisitos existentes estén identificados, clasificados y vinculados a una fuente documental o a una decisión nueva claramente señalada.

# 10. RESULTADO ESPERADO

Al finalizar FASE 0, ERX byLAEV deberá disponer de un entorno de desarrollo organizado y gobernado documentalmente, que incluya:

- Repositorio institucional de desarrollo.
- Material fundacional preservado e inventariado.
- Jerarquía y autoridad documental.
- Sistema de identificación y versionado.
- Índice maestro.
- Matriz de requisitos y trazabilidad.
- Registro de decisiones arquitectónicas.
- Registro de riesgos y dependencias.
- Modelo de gobernanza y matriz de responsabilidades.
- Procedimiento de control de cambios.
- Informe de cumplimiento.
- Registro formal de cierre.

Este resultado permitirá iniciar FASE 1 con una base documental identificable, organizada y controlada. No implica que el modelo UTXO esté completamente cerrado ni que exista software funcional o aceptación institucional.

# 11. RELACIÓN CON FASE 1

ERX-ROADMAP-001 identifica FASE 1 como **Cierre normativo y modelo de estados**, con prioridad crítica.

Su objetivo es definir de forma inequívoca cómo funciona el sistema de gasto único antes de desarrollar el motor transaccional.

FASE 0 prepara las condiciones documentales y organizativas para ese trabajo. FASE 1 deberá formalizar, entre otras materias:

- Identificadores UTXO y de entidades.
- Estados institucionales y tipos de salida.
- Reglas de consumo y creación de estados.
- Transiciones válidas e invariantes.
- Atomicidad e idempotencia.
- Concurrencia y prevención de doble consumo.
- Separación entre el ciclo de comunicación y el ciclo de disponibilidad del agente.
- Referencias de identidad, asignación y sesión entre ciclos.
- Excepciones, interrupciones y recuperación.
- Condiciones de verificación.

La autorización para iniciar FASE 1 deberá quedar registrada expresamente después del cierre de FASE 0. La aprobación de este Charter no constituye esa autorización.

# 12. AUTORIDAD, APROBACIÓN Y CONTROL DE CAMBIOS

LAEV / byLAEV conserva la autoridad de diseño del proyecto y la responsabilidad de aprobar las decisiones de diseño que correspondan a su ámbito. Las responsabilidades de implementación, revisión y validación técnica deberán identificarse conforme al modelo de gobernanza que se establezca durante FASE 0.

La aprobación de este documento establece formalmente la definición y fundamento de FASE 0 como marco de trabajo del proyecto. No aprueba automáticamente los demás documentos, no declara completada la fase y no autoriza operación institucional ni inicio de FASE 1.

Toda modificación posterior deberá generar una nueva revisión documental, conservar el historial y registrar su justificación y aprobación correspondiente.

## Registro formal de aprobación

| Campo | Registro |
|---|---|
| Documento | ERX-PHASE-0-CHARTER-001 |
| Versión aprobada | 1.0.0 |
| Autoría | LAEV / byLAEV |
| Autoridad aprobadora | LAEV |
| Decisión | APPROVED — aprobación expresa del autor |
| Condición | Cuatro ajustes técnicos incorporados en esta versión |
| Fecha de aprobación | 2026-11-23 |
| Evidencia de aprobación | Instrucción expresa de LAEV en la conversación del proyecto, 2026-11-23 |
| Publicación en repositorio | Pendiente de commit |

---

**FIN DEL DOCUMENTO**

ERX-PHASE-0-CHARTER-001  
ERX byLAEV — Sistema de Doble Gasto para Comunicaciones 911  
LAEV / byLAEV
