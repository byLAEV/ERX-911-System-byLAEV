# ERX-PHASE-0-CHARTER-001
## Phase 0 Definition and Rationale
### ERX byLAEV Project Governance and Preparation

| Field | Record |
|---|---|
| Project | 911 — Double-Spend System byLAEV |
| System | ERX byLAEV |
| Identifier | ERX-PHASE-0-CHARTER-001 |
| Version | 1.0.0 |
| Phase | PHASE 0 — Project Governance and Preparation |
| Work Package | WP-0.1 |
| Authorship and Design | LAEV / byLAEV |
| Document Status | APPROVED |
| Approval | Express approval by LAEV recorded |
| Approval Date | 2026-11-23 |
| Governing Planning Document | ERX-ROADMAP-001 v1.0 |

---

## 0. DOCUMENT CONTROL

### 0.1. Identification and Purpose

This document establishes the definition, rationale, purpose, objectives, justification, scope, exclusions, development principles, and completion criteria for Phase 0 of the ERX byLAEV project.

It is the conceptual and organizational opening document for the phase and the primary deliverable of work package WP-0.1.

### 0.2. Sources and Provenance

This document is based on the following examined documents:

- ERX-PROT-001 v1.1 — Institutional Protocol.
- ERX-ATLAS-001 v1.1 — Institutional Atlas of Architecture and Diagrams.
- UTXO-911-001 v1.0 — Functional Specification of the 911 Communication UTXO Cycle.
- ERX-ROADMAP-001 v1.0 — Master Phase Roadmap.
- Technical Response to the Observations on ERX-ROADMAP-001 — technical response document.

ERX-ROADMAP-001 also references:

- ERX-CONSENSUS-001 v0.1 — Consensus Framework, identified in the Roadmap as a coordination reference that must be completed before inclusion in a multi-institutional implementation.
- ERX-IMPL-PROPOSAL-001 — Institutional Implementation Proposal.

References to these two documents are retained as provenance declared by the Roadmap. Their complete files, current versions, availability, and contents must be verified and inventoried in WP-0.2. This Charter does not presume to have examined them and does not fill in their contents by inference.

### 0.3. Document Nature and Authority

This is a project development and governance document. It does not replace foundational sources, does not independently amend normative documents, and does not supersede the document-authority rules to be established in WP-0.3.

### 0.4. Approval Record

LAEV expressly approved this document subject to four technical adjustments: (1) retain the additional document references cited by the Roadmap and mark their verification as pending; (2) clarify that Roadmap principles are design constraints, not evidence of implementation; (3) explicitly state the independence of the communication and agent-availability UTXO cycles; and (4) permit controlled deferral of pending matters to later phases without concealing them or declaring them resolved.

Approval applies to this consolidated version 1.0.0, which incorporates those adjustments.

---

# 1. PHASE IDENTIFICATION

**PHASE 0 — PROJECT GOVERNANCE AND PREPARATION**

Phase 0 is the first stage of ERX byLAEV development.

It is a preparatory phase intended to organize the documentary, architectural, technical, and organizational conditions required to develop, implement, verify, and subsequently evaluate the institutional system.

Its position at the beginning of the master roadmap reflects the need to establish development rules, source provenance and authority, requirements traceability, and control mechanisms before proceeding to normative closure and software construction.

Phase 0 is not a functional implementation phase of ERX. It prepares and governs the documentary and working environment under which subsequent phases will be carried out.

# 2. PURPOSE

Establish a governance, documentation, identification, traceability, planning, and control structure that enables ERX byLAEV to be developed in an orderly, verifiable manner consistent with its foundational architecture.

The phase aims to preserve continuity among existing documents, design decisions, identified requirements, and future software components. Every change, decision, requirement, dependency, and result must be traceable to its provenance and supporting evidence.

The work shall distinguish, without conflating their respective functions:

- Normative architecture and protocol.
- Graphical representation and functional documentation.
- Institutional UTXO state model.
- Software architecture.
- Technical implementation.
- Independent verification.
- Institutional integration, adoption, and homologation.

# 3. GENERAL OBJECTIVE

Establish and approve the documentary, organizational, and control framework required to carry out ERX byLAEV development in accordance with ERX-ROADMAP-001, ensuring identification and preservation of foundational sources, document hierarchy, requirements and decision traceability, risk and dependency recording, allocation of responsibilities, and verifiable control of project changes.

# 4. SPECIFIC OBJECTIVES

1. **Document consolidation:** identify, inventory, and preserve the documents that form the project's foundation.
2. **Document hierarchy:** establish the relationships among normative, functional, graphical, architectural, technical, and planning documents.
3. **Identification and versioning:** define a consistent system for document identifiers, naming, versions, and statuses.
4. **Repository organization:** establish the ERX repository as the environment for preservation, development, review, and tracking.
5. **Master index:** create a centralized register of documents, versions, statuses, and relationships.
6. **Requirements identification:** extract and classify existing requirements, distinguishing documented obligations, design requirements, pending matters, and open decisions.
7. **Decision register:** document the context, alternatives, rationale, and consequences of architectural decisions.
8. **Risk identification:** record documentary, technical, architectural, and institutional risks, together with dependencies and mitigation measures.
9. **Governance:** define responsibilities for design, protocol, software, security, review, and validation.
10. **Change control:** establish procedures for review, approval, preservation of previous versions, and documentary continuity.
11. **Readiness verification:** verify that the conditions for starting Phase 1 are documented and that pending matters are identified and addressed.

# 5. PHASE JUSTIFICATION

ERX encompasses multiple disciplines and responsibilities that must remain coordinated without losing their functional independence. Its architecture includes an institutional 911 communications protocol, a UTXO state model, cryptographic mechanisms, timestamp evidence, institutional storage, software integration, and independent verification.

The project therefore requires a framework that preserves consistency among documents, decisions, and components, and prevents a proposal, specification, implementation, and validation from being treated as equivalent.

Phase 0 addresses the following needs:

### 5.1. Documentary Continuity
Prevent new versions from replacing or contradicting original sources without a documented procedure, rationale, and traceability.

### 5.2. Architectural Consistency
Prevent independent component development from introducing behavior incompatible with protocol rules.

### 5.3. Traceability
Link each requirement and decision to a documentary source or to a new decision explicitly identified as such.

### 5.4. Evolution Control
Enable ERX to evolve through identifiable, reviewable, and recoverable versions.

### 5.5. Technical Accountability
Distinguish who designs, implements, reviews, approves, and validates each element.

### 5.6. Prevention of Management Errors
Prevent administrative completion of activities from being interpreted as evidence of functionality, security, or institutional acceptance.

### 5.7. Preparation for Normative Development
Establish the conditions for Phase 1, whose objective is to formally close the rules governing the state model and single-spend mechanism before development of the transaction engine.

# 6. SCOPE OF WORK

Phase 0 comprises the twelve work packages defined in WORKPLAN-PHASE-0.md:

1. Phase definition and rationale.
2. Identification and consolidation of foundational materials.
3. Document organization and hierarchy.
4. Document identification and control.
5. ERX repository creation and organization.
6. Master index and document register.
7. Requirements identification and classification.
8. Architecture decision register.
9. Risk and dependency register.
10. Governance and responsibilities.
11. Version planning and control.
12. Phase verification and formal closure.

The scope includes the documents, registers, matrices, procedures, acceptance criteria, and tracking mechanisms required to meet these objectives. It also includes identifying matters whose resolution belongs to later phases.

# 7. SCOPE EXCLUSIONS

Phase 0 does not include:

1. **Final normative closure:** it does not amend or declare the normative rules of ERX-PROT-001 closed.
2. **Final UTXO specification:** it is not the complete specification of identifiers, states, transitions, consumption, concurrency, atomicity, idempotency, and recovery. These matters must be formalized primarily in Phase 1.
3. **Software development:** it does not implement ERX Core, ERX Institutional Module, or ERX Verifier.
4. **Cryptographic implementation:** it does not develop or validate definitive algorithms, signature formats, data structures, or cryptographic mechanisms.
5. **Production OTS integration:** it does not perform production integration or submission of OpenTimestamps timestamps.
6. **Institutional integration:** it does not connect live telephony, location, CAD, agent, provider, or 911-center systems.
7. **Operational validation:** it does not certify security, interoperability, availability, or institutional operation.
8. **Homologation:** it does not authorize ERX operation in emergency centers or replace approvals required from competent authorities.

# 8. DEVELOPMENT PRINCIPLES

The following principles are adopted as development constraints and guiding criteria under ERX-ROADMAP-001 v1.0. Their inclusion in this Charter does not mean that they have been implemented, tested, or certified. Their verifiable formalization and technical demonstration belong to the relevant phases.

| Principle | Condition established in the Roadmap | Treatment in Phase 0 |
|---|---|---|
| Non-interference | ERX must never condition emergency response. | Preserve as a priority operational constraint. |
| Single spend | No state may be consumed more than once. | Record as a foundation of the UTXO design. |
| Atomicity | State consumption and creation must be consistent. | Record as a requirement to be formalized and verified. |
| Idempotency | Repeating a request must not duplicate its effects. | Record as a requirement to be formalized and verified. |
| History | Previous events are not erased by a transition. | Preserve traceability and history. |
| Identity | Every transition must have a verifiable issuer and authorization. | Record identity and authorization requirements. |
| Privacy | Sensitive data remains under institutional custody. | Preserve as a design and governance constraint. |
| Temporal independence | OTS must not condition closure or emergency response. | Keep timestamp evidence outside the critical response path. |
| Recovery | Interruptions must not resurrect consumed states. | Record as a continuity and recovery requirement. |
| Verification | Evidence must be independently verifiable. | Maintain separation between evidence production and verification. |
| Institutional separation | Each center retains its authority and responsibility. | Preserve institutional authority boundaries. |

### 8.1. Mandatory Separation of UTXO Cycles

Under ERX-ROADMAP-001, ERX maintains two related but independent cycles:

**Cycle A — 911 Communication**

- UTXO 01: Intake.
- UTXO 02: Contact and Initial Protocol.
- UTXO 03: Development and Closure.

Each call has its own cycle and record.

**Cycle B — Agent Availability**

- AVAILABLE.
- ASSIGNED / ACCEPTED.
- BUSY.
- RELEASE AND RETURN TO AVAILABILITY.

The agent-availability cycle has its own states and does not reuse the call UTXOs. UTXO 03 does not replace the agent's availability state. A new availability state must not be issued while the agent remains busy, on pause, or subject to another condition that prevents accepting requests.

The relationship between both cycles is established through identity, assignment, and session references. This relationship does not merge their states or their consumption and transition conditions.

The complete formalization of identifiers, transitions, invariants, concurrency, atomicity, and recovery for both cycles belongs to subsequent normative and technical work, primarily Phase 1.

### 8.2. Independence of Timestamp Evidence

OTS evidence and external synchronization processes must remain outside the critical path of emergency handling. Their generation, confirmation, or availability must not condition emergency intake, response, dispatch, or operational closure. The technical response to the Roadmap observations supports running external timestamp-evidence and synchronization processes asynchronously relative to local transactional operations.

### 8.3. Source Preservation

Original documents are retained as provenance references. Changes are documented in new versions or derivative documents.

### 8.4. No Silent Inference

Gaps, contradictions, and unresolved decisions remain identified until a documented resolution exists.

### 8.5. Separation of Responsibilities

Design authority, implementation, review, and independent validation must not be conflated.

### 8.6. Evidence-Based Approval

A phase is not considered complete merely because files have been produced, tasks executed, or administrative checklists satisfied. Progress requires verifiable evidence and fulfillment of acceptance criteria.

### 8.7. Continuity

Every change must make it possible to reconstruct what existed, what changed, why it changed, and who authorized the change.

# 9. COMPLETION CRITERIA

Phase 0 may be declared complete only after fulfillment of the criteria for all twelve work packages and verification of the following general conditions:

- [ ] Known sources are inventoried, preserved, or explicitly identified as missing.
- [ ] Source versions and provenance are recorded.
- [ ] Document hierarchy and subject-matter authority are defined and approved.
- [ ] Contradictions and gaps are recorded with assigned handling.
- [ ] Document identifiers, naming, versions, and statuses are defined.
- [ ] Repository, access, and change control are documented.
- [ ] The master index is consistent with the actual documents.
- [ ] Requirements are identified, classified, and linked to a documentary source or a clearly identified new decision.
- [ ] Approved and pending architecture decisions are recorded.
- [ ] Risks and dependencies have impact, mitigation, owners, and resolution conditions.
- [ ] Governance, responsibilities, review, and approval are defined.
- [ ] Documentary continuity and version preservation are established.
- [ ] A compliance report and formal closure record are available.
- [ ] LAEV has expressly approved Phase 0 closure.
- [ ] Express authorization to start the next phase is recorded.

Technical matters belonging to Phase 1 or later do not need to be resolved prematurely during Phase 0. They may be deferred if they are identified, classified, linked to their source or decision, justified, assigned to a resolution phase, and expressly accepted during closure. Deferral does not mean they are resolved or waive any requirements the Roadmap requires for progression.

The progression criterion established by ERX-ROADMAP-001 requires all existing requirements to be identified, classified, and linked to a documentary source or a clearly identified new decision.

# 10. EXPECTED OUTCOME

At the end of Phase 0, ERX byLAEV must have an organized and document-governed development environment, including:

- Institutional development repository.
- Preserved and inventoried foundational materials.
- Document hierarchy and authority.
- Identification and versioning system.
- Master index.
- Requirements and traceability matrix.
- Architecture decision register.
- Risk and dependency register.
- Governance model and responsibility matrix.
- Change-control procedure.
- Compliance report.
- Formal closure record.

This outcome will allow Phase 1 to begin on an identifiable, organized, and controlled documentary basis. It does not imply that the UTXO model is fully closed, that functional software exists, or that institutional acceptance has been granted.

# 11. RELATIONSHIP WITH PHASE 1

ERX-ROADMAP-001 identifies Phase 1 as **Normative Closure and State Model**, with critical priority.

Its objective is to define unambiguously how the single-spend system works before development of the transaction engine.

Phase 0 prepares the documentary and organizational conditions for that work. Phase 1 must formalize, among other matters:

- UTXO and entity identifiers.
- Institutional states and output types.
- State-consumption and state-creation rules.
- Valid transitions and invariants.
- Atomicity and idempotency.
- Concurrency and double-consumption prevention.
- Separation between the communication cycle and the agent-availability cycle.
- Identity, assignment, and session references between cycles.
- Exceptions, interruptions, and recovery.
- Verification conditions.

Authorization to begin Phase 1 must be expressly recorded after Phase 0 closure. Approval of this Charter does not constitute that authorization.

# 12. AUTHORITY, APPROVAL, AND CHANGE CONTROL

LAEV / byLAEV retains project design authority and responsibility for approving design decisions within its scope. Implementation, review, and technical-validation responsibilities must be identified under the governance model established during Phase 0.

Approval of this document formally establishes the definition and rationale of Phase 0 as the project's working framework. It does not automatically approve other documents, declare the phase complete, authorize institutional operation, or authorize the start of Phase 1.

Any subsequent modification must generate a new document revision, preserve the history, and record its rationale and corresponding approval.

## Formal Approval Record

| Field | Record |
|---|---|
| Document | ERX-PHASE-0-CHARTER-001 |
| Approved Version | 1.0.0 |
| Authorship | LAEV / byLAEV |
| Approving Authority | LAEV |
| Decision | APPROVED — express approval by the author |
| Condition | Four technical adjustments incorporated in this version |
| Approval Date | 2026-11-23 |
| Approval Evidence | Express instruction from LAEV in the project conversation, 2026-11-23 |
| Repository Publication | Published in the ERX repository |

---

**END OF DOCUMENT**

ERX-PHASE-0-CHARTER-001  
ERX byLAEV — Double-Spend System for 911 Communications  
LAEV / byLAEV
