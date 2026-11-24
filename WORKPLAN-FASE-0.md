# WORKPLAN-FASE-0
## Gobierno y preparación del proyecto ERX byLAEV

- **Proyecto:** ERX-911-System-byLAEV
- **Identificador:** ERX-WP-FASE-0-001
- **Fase:** 0 — Gobierno y preparación del proyecto
- **Versión:** 1.0.0
- **Estado:** DRAFT / PENDIENTE DE APROBACIÓN
- **Autoridad de diseño y aprobación:** LAEV

## 1. Propósito y naturaleza

Este Workplan convierte el desglose de FASE 0 en un instrumento de ejecución y seguimiento. Organiza los doce paquetes de trabajo, sus actividades, dependencias, entregables, evidencias y criterios de aceptación.

Este documento planifica el trabajo; no declara que las actividades hayan sido ejecutadas, no sustituye fuentes fundacionales ni documentos normativos y no constituye aprobación de FASE 0.

## 2. Reglas de ejecución

1. Preservar los documentos originales; desarrollar cambios en documentos derivados con trazabilidad.
2. No resolver contradicciones ni vacíos por inferencia silenciosa. Registrar fuentes, impacto, responsable y estado.
3. Identificar cada documento con código, versión, estado, autoría, procedencia, historial y aprobación cuando corresponda.
4. Cambiar estados únicamente cuando exista evidencia verificable.
5. Permitir trabajo paralelo solo cuando las dependencias estén satisfechas.
6. Un commit o la publicación de un archivo no equivale a aprobación.
7. Mantener visibles los asuntos pendientes, sin presentarlos como resueltos.
8. FASE 0 no autoriza implementación, despliegue ni operación institucional del sistema 911.

## 3. Estados de seguimiento

| Estado | Significado |
|---|---|
| NOT_STARTED | Sin trabajo verificable registrado. |
| IN_PROGRESS | En elaboración; existe evidencia parcial. |
| IN_REVIEW | Entregable presentado para revisión. |
| BLOCKED | Una dependencia o decisión pendiente impide avanzar. |
| APPROVED | Aprobado expresamente por la autoridad correspondiente. |
| COMPLETED | Criterios de aceptación satisfechos y evidencia registrada. |
| DEFERRED | Trasladado formalmente a otra fase con justificación aprobada. |

**Estado inicial de todos los paquetes: NOT_STARTED.** La publicación de este Workplan no cambia esos estados.

## 4. Secuencia y puertas de control

```text
INICIO
  |
  v
0.1 Definición y fundamento
  |
  v
0.2 Material fundacional
  |
  v
0.3 Jerarquía documental
  |
  +------> 0.4 Control documental
  +------> 0.5 Repositorio
                 |
                 v
          0.6 Índice maestro
                 |
          +------+------+
          v             v
     0.7 Requisitos  0.8 Decisiones ADR
          +------+------+
                 v
        0.9 Riesgos y dependencias
                 |
                 v
        0.10 Gobernanza y responsabilidades
                 |
                 v
        0.11 Versiones y cambios
                 |
                 v
        0.12 Verificación y cierre
                 |
          Aprobación formal LAEV
                 |
                 v
       Autorización de fase siguiente
```

La secuencia representa dependencias lógicas. Se permite iteración y concurrencia controlada sin alterar la autoridad de las fuentes.

## 5. Paquetes de trabajo

### WP-0.1 — Definición y fundamento de FASE 0
**Estado:** APPROVED  
**Actividades**
- [x] 0.1.1 Identificación de la fase.
- [x] 0.1.2 Propósito.
- [x] 0.1.3 Objetivo general.
- [x] 0.1.4 Objetivos específicos.
- [x] 0.1.5 Justificación de la fase.
- [x] 0.1.6 Alcance de trabajo.
- [x] 0.1.7 Exclusiones del alcance.
- [x] 0.1.8 Principios de desarrollo.
- [x] 0.1.9 Criterios de finalización.

**Entregable:** `docs/phase-0/ERX-PHASE-0-CHARTER-001.md`  
**Aceptación:** SATISFECHA para WP-0.1 mediante aprobación expresa de LAEV de la versión 1.0.0 del Charter. WP-0.1 queda en APPROVED; no se declara COMPLETED hasta que la evidencia y el registro de seguimiento estén consolidados conforme al control de FASE 0.  
**Entrada:** desglose de FASE 0 definido por LAEV.

### WP-0.2 — Identificación y consolidación del material fundacional
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.2.1 Identificar fuentes existentes.
- [ ] 0.2.2 Inventariar documentos originales.
- [ ] 0.2.3 Registrar procedencia.
- [ ] 0.2.4 Identificar versiones originales.
- [ ] 0.2.5 Clasificar por naturaleza documental.
- [ ] 0.2.6 Preservar archivos originales.
- [ ] 0.2.7 Identificar fuentes faltantes.
- [ ] 0.2.8 Registrar referencias entre fuentes.
- [ ] 0.2.9 Consolidar el registro de material fundacional.

**Entregable:** `docs/foundational/` y `registers/foundational-material-register.csv`.  
**Aceptación:** cada fuente conocida cuenta con ID, nombre, procedencia, versión, ubicación, integridad y estado; faltantes y dudas quedan explícitos. No reconstruir fuentes ausentes mediante supuestos.  
**Dependencia:** WP-0.1.

### WP-0.3 — Organización y jerarquía documental
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.3.1 Clasificar documentos.
- [ ] 0.3.2 Diferenciar fuentes y documentos de desarrollo.
- [ ] 0.3.3 Definir jerarquía documental.
- [ ] 0.3.4 Definir autoridad documental por materia.
- [ ] 0.3.5 Registrar relaciones y dependencias.
- [ ] 0.3.6 Identificar contradicciones.
- [ ] 0.3.7 Definir tratamiento de contradicciones.
- [ ] 0.3.8 Establecer reglas de evolución documental.

**Entregable:** `docs/phase-0/ERX-DOCUMENT-GOVERNANCE-001.md`.  
**Aceptación:** jerarquía y autoridad por materia explícitas; contradicciones registradas con fuentes enfrentadas, impacto, responsable, disposición y estado.  
**Dependencia:** WP-0.2.

### WP-0.4 — Identificación y control de documentos
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.4.1 Sistema de identificadores ERX.
- [ ] 0.4.2 Nomenclatura documental.
- [ ] 0.4.3 Sistema de versiones.
- [ ] 0.4.4 Estados documentales.
- [ ] 0.4.5 Metadatos obligatorios.
- [ ] 0.4.6 Registro de autoría.
- [ ] 0.4.7 Registro de aprobación.
- [ ] 0.4.8 Historial de modificaciones.
- [ ] 0.4.9 Referencias cruzadas.

**Entregable:** `docs/phase-0/ERX-DOCUMENT-CONTROL-001.md` y plantilla documental.  
**Aceptación:** cada documento puede identificarse inequívocamente; se distingue borrador, revisión y aprobado; el historial puede reconstruirse.  
**Dependencias:** WP-0.1 y WP-0.3.

### WP-0.5 — Creación y organización del repositorio ERX
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.5.1 Identidad del repositorio.
- [ ] 0.5.2 Objetivo del repositorio.
- [ ] 0.5.3 Estructura de directorios.
- [ ] 0.5.4 Ubicación del material fundacional.
- [ ] 0.5.5 Ubicación de documentos de FASE 0.
- [ ] 0.5.6 Política de acceso.
- [ ] 0.5.7 Organización de ramas.
- [ ] 0.5.8 Control de modificaciones.
- [ ] 0.5.9 Historial de cambios Git.
- [ ] 0.5.10 Propiedad intelectual y licencia.

**Estructura inicial propuesta**
```text
/
├── README.md
├── WORKPLAN-FASE-0.md
├── COPYRIGHT.md
├── docs/
│   ├── foundational/
│   ├── phase-0/
│   ├── requirements/
│   ├── decisions/
│   ├── risks/
│   ├── governance/
│   └── reports/
├── registers/
└── templates/
```

**Entregable:** estructura aprobada y `docs/phase-0/ERX-REPOSITORY-GOVERNANCE-001.md`.  
**Aceptación:** ubicaciones, accesos, ramas, control de cambios y propiedad intelectual documentados. No crear ni atribuir una licencia sin decisión expresa.  
**Dependencias:** WP-0.3 y WP-0.4.

### WP-0.6 — Índice maestro y registro documental
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.6.1 Registro general de documentos.
- [ ] 0.6.2 Identificar documentos fundacionales.
- [ ] 0.6.3 Identificar documentos de desarrollo.
- [ ] 0.6.4 Registrar versiones.
- [ ] 0.6.5 Clasificar documentos.
- [ ] 0.6.6 Registrar estado de cada documento.
- [ ] 0.6.7 Registrar relaciones entre documentos.
- [ ] 0.6.8 Identificar documentos pendientes.
- [ ] 0.6.9 Consolidar índice maestro.

**Entregable:** `registers/document-register.csv` y `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md`.  
**Aceptación:** todos los documentos identificados y creados durante FASE 0 aparecen con ID, versión, clasificación, estado y referencias consistentes.  
**Dependencias:** WP-0.2 a WP-0.5.

### WP-0.7 — Identificación y clasificación de requisitos
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.7.1 Metodología de identificación.
- [ ] 0.7.2 Extraer requisitos existentes.
- [ ] 0.7.3 Identificar individualmente cada requisito.
- [ ] 0.7.4 Clasificar requisitos.
- [ ] 0.7.5 Identificar requisitos obligatorios.
- [ ] 0.7.6 Identificar requisitos de diseño.
- [ ] 0.7.7 Registrar requisitos pendientes de especificación.
- [ ] 0.7.8 Registrar decisiones abiertas.
- [ ] 0.7.9 Vincular requisitos con fuentes.
- [ ] 0.7.10 Asignar requisitos a fases.
- [ ] 0.7.11 Construir matriz de trazabilidad.

**Entregable:** `registers/requirements-traceability.csv` y `docs/phase-0/ERX-REQUIREMENTS-METHOD-001.md`.  
**Aceptación:** cada requisito tiene ID, enunciado verificable, tipo, fuente, estado, fase asignada y criterio de verificación. Los requisitos inferidos se distinguen de los extraídos.  
**Dependencias:** WP-0.3 y WP-0.6.

### WP-0.8 — Registro de decisiones arquitectónicas (ADR)
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.8.1 Propósito y formato ADR.
- [ ] 0.8.2 Identificar decisiones.
- [ ] 0.8.3 Registrar contexto.
- [ ] 0.8.4 Describir problema que resuelve.
- [ ] 0.8.5 Registrar alternativas consideradas.
- [ ] 0.8.6 Registrar decisión adoptada o pendiente.
- [ ] 0.8.7 Documentar justificación.
- [ ] 0.8.8 Documentar consecuencias.
- [ ] 0.8.9 Identificar decisiones aprobadas.
- [ ] 0.8.10 Identificar decisiones pendientes.
- [ ] 0.8.11 Mantener historial y sustituciones.

**Entregable:** `docs/decisions/` y `registers/decision-register.csv`.  
**Aceptación:** cada decisión material contiene contexto, alternativas, decisión, fundamento, consecuencias, fuentes, responsable y estado; las sustituidas permanecen consultables.  
**Dependencias:** WP-0.3, WP-0.6 y WP-0.7.

### WP-0.9 — Registro de riesgos y dependencias
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.9.1 Metodología de identificación.
- [ ] 0.9.2 Registrar riesgos documentales.
- [ ] 0.9.3 Registrar riesgos arquitectónicos.
- [ ] 0.9.4 Registrar riesgos técnicos.
- [ ] 0.9.5 Registrar riesgos institucionales.
- [ ] 0.9.6 Clasificar impacto y prioridad.
- [ ] 0.9.7 Definir medidas de tratamiento.
- [ ] 0.9.8 Registrar dependencias documentales.
- [ ] 0.9.9 Registrar dependencias técnicas.
- [ ] 0.9.10 Registrar dependencias institucionales.
- [ ] 0.9.11 Registrar dependencias entre fases.
- [ ] 0.9.12 Definir condiciones de resolución.

**Entregable:** `registers/risk-dependency-register.csv` y `docs/phase-0/ERX-RISK-METHOD-001.md`.  
**Aceptación:** cada riesgo o dependencia tiene ID, categoría, fuente, impacto, prioridad, tratamiento, responsable, estado y condición de cierre.  
**Dependencias:** WP-0.6, WP-0.7 y WP-0.8.

### WP-0.10 — Gobernanza y responsabilidades
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.10.1 Definir modelo de gobierno ERX.
- [ ] 0.10.2 Documentar autoridad de diseño LAEV.
- [ ] 0.10.3 Definir responsabilidad de protocolo.
- [ ] 0.10.4 Definir responsabilidad de software.
- [ ] 0.10.5 Definir responsabilidad de seguridad.
- [ ] 0.10.6 Definir responsabilidad de validación.
- [ ] 0.10.7 Definir validación técnica independiente.
- [ ] 0.10.8 Definir procedimiento de revisión.
- [ ] 0.10.9 Definir procedimiento de aprobación.
- [ ] 0.10.10 Definir tratamiento de observaciones.
- [ ] 0.10.11 Construir matriz de responsabilidades.

**Entregable:** `docs/governance/ERX-GOVERNANCE-MODEL-001.md` y matriz RACI.  
**Aceptación:** autoridad y funciones delimitadas; aprobaciones identificables; observaciones trazables; validación independiente separada de autoría y diseño.  
**Dependencias:** WP-0.1, WP-0.3 y WP-0.7 a WP-0.9.

### WP-0.11 — Planificación y control de versiones
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.11.1 Política de versionado.
- [ ] 0.11.2 Versionado documental.
- [ ] 0.11.3 Versionado del repositorio.
- [ ] 0.11.4 Identificar versiones preliminares.
- [ ] 0.11.5 Identificar versiones aprobadas.
- [ ] 0.11.6 Procedimiento de modificación.
- [ ] 0.11.7 Revisión de cambios.
- [ ] 0.11.8 Aprobación de cambios.
- [ ] 0.11.9 Conservar versiones anteriores.
- [ ] 0.11.10 Mantener registro de cambios.
- [ ] 0.11.11 Definir continuidad documental.

**Entregable:** `docs/phase-0/ERX-VERSION-AND-CHANGE-CONTROL-001.md` y `registers/change-log.md`.  
**Aceptación:** cada modificación puede rastrearse desde solicitud, revisión y aprobación hasta commit y versión resultante; las versiones anteriores son recuperables.  
**Dependencias:** WP-0.4, WP-0.5, WP-0.6 y WP-0.10.

### WP-0.12 — Verificación y cierre de FASE 0
**Estado:** NOT_STARTED  
**Actividades**
- [ ] 0.12.1 Consolidar entregables.
- [ ] 0.12.2 Verificar repositorio.
- [ ] 0.12.3 Verificar fuentes.
- [ ] 0.12.4 Verificar índice maestro.
- [ ] 0.12.5 Verificar requisitos.
- [ ] 0.12.6 Verificar decisiones.
- [ ] 0.12.7 Verificar riesgos y dependencias.
- [ ] 0.12.8 Verificar responsabilidades.
- [ ] 0.12.9 Verificar control de versiones.
- [ ] 0.12.10 Registrar observaciones pendientes.
- [ ] 0.12.11 Emitir informe de cumplimiento.
- [ ] 0.12.12 Obtener aprobación de LAEV.
- [ ] 0.12.13 Registrar formalmente el cierre.
- [ ] 0.12.14 Autorizar inicio de fase siguiente.

**Entregables:** `docs/reports/ERX-PHASE-0-COMPLIANCE-REPORT-001.md` y `docs/reports/ERX-PHASE-0-CLOSURE-RECORD-001.md`.  
**Aceptación:** paquetes COMPLETED o DEFERRED con justificación aprobada; pendientes registrados con impacto y tratamiento; informe enlaza evidencias verificables; LAEV aprueba expresamente; existe registro de cierre y autorización de la fase siguiente.  
**Dependencias:** WP-0.1 a WP-0.11.

## 6. Matriz de dependencias

| Paquete | Dependencias | Resultado habilitado |
|---|---|---|
| WP-0.1 | Desglose de FASE 0 | Mandato y límites |
| WP-0.2 | WP-0.1 | Inventario de fuentes |
| WP-0.3 | WP-0.2 | Jerarquía documental |
| WP-0.4 | WP-0.1, WP-0.3 | Control documental |
| WP-0.5 | WP-0.3, WP-0.4 | Repositorio organizado |
| WP-0.6 | WP-0.2 a WP-0.5 | Índice maestro |
| WP-0.7 | WP-0.3, WP-0.6 | Requisitos trazables |
| WP-0.8 | WP-0.3, WP-0.6, WP-0.7 | Decisiones trazables |
| WP-0.9 | WP-0.6 a WP-0.8 | Riesgos y dependencias |
| WP-0.10 | WP-0.1, WP-0.3, WP-0.7 a WP-0.9 | Gobierno y responsabilidades |
| WP-0.11 | WP-0.4 a WP-0.6, WP-0.10 | Control de cambios |
| WP-0.12 | WP-0.1 a WP-0.11 | Cierre y autorización |

## 7. Registro de seguimiento

| ID | Paquete | Estado inicial | Responsable | Evidencia | Observaciones |
|---|---|---|---|---|---|
| WP-0.1 | Definición y fundamento | APPROVED | LAEV | [ERX-PHASE-0-CHARTER-001 v1.0.0](docs/phase-0/ERX-PHASE-0-CHARTER-001.md) · aprobación expresa 2026-11-23 | Cuatro ajustes técnicos incorporados; WP-0.1 aprobado, no declarado COMPLETED. |
| WP-0.2 | Material fundacional | NOT_STARTED | Por asignar | — | — |
| WP-0.3 | Jerarquía documental | NOT_STARTED | Por asignar | — | — |
| WP-0.4 | Control documental | NOT_STARTED | Por asignar | — | — |
| WP-0.5 | Repositorio ERX | NOT_STARTED | LAEV / por asignar | — | — |
| WP-0.6 | Índice maestro | NOT_STARTED | Por asignar | — | — |
| WP-0.7 | Requisitos | NOT_STARTED | Por asignar | — | — |
| WP-0.8 | Decisiones ADR | NOT_STARTED | LAEV / por asignar | — | — |
| WP-0.9 | Riesgos y dependencias | NOT_STARTED | Por asignar | — | — |
| WP-0.10 | Gobernanza | NOT_STARTED | LAEV / por asignar | — | — |
| WP-0.11 | Versiones y cambios | NOT_STARTED | Por asignar | — | — |
| WP-0.12 | Verificación y cierre | NOT_STARTED | LAEV | — | — |

## 8. Condiciones de salida de FASE 0

- [ ] Fuentes inventariadas y preservadas, o faltantes formalmente identificados.
- [ ] Jerarquía documental y autoridad por materia aprobadas.
- [ ] Identificación, versionado y estados documentales definidos.
- [ ] Repositorio, accesos y control de cambios aprobados.
- [ ] Índice maestro consistente con documentos reales.
- [ ] Requisitos identificados y trazados a sus fuentes.
- [ ] Decisiones arquitectónicas registradas, incluidos pendientes.
- [ ] Riesgos y dependencias con tratamiento y responsables.
- [ ] Gobernanza, revisión y aprobación definidas.
- [ ] Continuidad documental establecida.
- [ ] Informe de cumplimiento y registro de cierre disponibles.
- [ ] Aprobación formal de LAEV y autorización de fase siguiente.

Un pendiente no bloquea automáticamente el cierre si está clasificado, tiene responsable, impacto, tratamiento y fase de resolución aprobada. No se presentará como resuelto un asunto que siga abierto.

## 9. Exclusiones

Este Workplan no ejecuta ni declara completados el diseño detallado o implementación de software, la implementación UTXO en el flujo operativo, la integración o envío de sellos OpenTimestamps, pruebas de interoperabilidad con centros 911, certificación regulatoria, aceptación institucional, despliegue productivo ni operación real de emergencias. Estos elementos se asignarán a fases posteriores mediante requisitos y decisiones aprobados.

## 10. Registro de aprobación

| Rol | Autoridad | Estado | Fecha | Evidencia |
|---|---|---|---|---|
| Autoridad de diseño y aprobación | LAEV | PENDING | — | — |
| Revisión técnica independiente | Por designar | NOT_ASSIGNED | — | — |

La incorporación de este archivo al repositorio establece el Workplan como instrumento disponible para seguimiento. La aprobación del Charter WP-0.1 no implica la aprobación de este Workplan en su conjunto, no declara completada FASE 0 y no autoriza el inicio de FASE 1.

---
**Fin de WORKPLAN-FASE-0 — ERX byLAEV**
