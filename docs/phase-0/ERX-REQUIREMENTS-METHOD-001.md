# ERX-REQUIREMENTS-METHOD-001
## Requirements Identification and Classification Method — Phase 0 / WP-0.7

| Field | Value |
|---|---|
| Document ID | ERX-REQUIREMENTS-METHOD-001 |
| Version | 1.0.0 |
| Status | CONTROLLED WP-0.7 METHOD — CONDITIONAL ACCEPTANCE APPLIED |
| Work Package | WP-0.7 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | https://github.com/byLAEV/ERX-911-System-byLAEV |
| Prepared / controlled | 2026-11-25 |
| Authority | LAEV |
| Dependencies | WP-0.3 and WP-0.6 — COMPLETED / ACCEPTED |

## 1. Purpose

This document defines a repeatable method for identifying, extracting, classifying, tracing, and assigning ERX requirements to project phases. It is a preparatory method, not an approved requirements baseline.

The method is designed to preserve the distinction between:
- A statement explicitly present in an authoritative source.
- A requirement derived by interpretation from one or more source statements.
- A proposed requirement introduced to close a documented gap.
- An open decision for which no requirement can yet be stated.
- A verification criterion used to determine whether a requirement has been satisfied.

No requirement is considered approved merely because it appears in a register or is published in GitHub.

## 2. Scope

The method covers WP-0.7 activities:
- 0.7.1 Identification methodology.
- 0.7.2 Extraction of existing requirements.
- 0.7.3 Individual requirement identification.
- 0.7.4 Requirement classification.
- 0.7.5 Mandatory requirements.
- 0.7.6 Design requirements.
- 0.7.7 Requirements pending specification.
- 0.7.8 Open decisions.
- 0.7.9 Source linkage.
- 0.7.10 Phase allocation.
- 0.7.11 Traceability matrix.

This draft establishes the extraction protocol and register structure. It does not claim that the full foundational PDFs have been re-opened and re-examined in this activity. The prior master index and foundational register provide document metadata and references, not substitutes for the source text. Consequently, no substantive requirement is asserted here as extracted from those PDFs.

## 3. Source Authority and Evidence Rules

### 3.1 Source classes

For requirements extraction, classify each source as one of:
- Foundational source document.
- Approved governance document.
- Approved requirement or specification document.
- Approved decision record.
- Working or preparatory development document.
- External legal, regulatory, technical, or institutional source (when expressly included in scope).
- Unverified or missing source.

The final precedence and subject-matter authority rules depend on WP-0.3 and must not be inferred by this method.

### 3.2 Evidence rules

1. Open and inspect the exact source document and version before extracting a requirement.
2. Record the exact source identifier, version, section, page, diagram, or paragraph.
3. Preserve the source's terminology and normative strength.
4. Do not convert descriptive statements, examples, aspirations, or explanatory text into mandatory requirements without an explicit rationale.
5. If wording is ambiguous, record an ambiguity rather than silently resolving it.
6. If two sources conflict, record both statements and create a contradiction item for WP-0.3 / ADR review.
7. A requirement inferred from a source must be labelled DERIVED, identify its rationale, and retain links to all supporting passages.
8. A proposed gap-filling requirement must be labelled PROPOSED and must not be represented as an existing source requirement.
9. A missing source cannot support an extracted requirement.
10. Do not infer regulatory obligations without identifying the jurisdiction and authoritative legal source.

### 3.3 Evidence locator

Each extracted statement must have a reproducible locator:
- Document ID and exact version.
- File name and repository path or source location.
- Section / subsection.
- PDF page or diagram identifier, if available.
- Short quotation or faithful statement summary.
- Integrity hash where the source is an archived binary.

## 4. Requirement Record Structure

Each requirement receives a stable unique ID. Proposed pattern:

`ERX-REQ-[DOMAIN]-[NNNN]`

The ID must not encode status, priority, version, or phase. IDs are never reused.

Required fields:

| Field | Requirement |
|---|---|
| Requirement ID | Unique persistent identifier |
| Requirement statement | One clear, testable obligation or constraint |
| Requirement type | Classification from Section 5 |
| Origin class | EXTRACTED, DERIVED, or PROPOSED |
| Source ID and version | Exact source reference |
| Source locator | Section/page/diagram/paragraph |
| Rationale | Why the requirement exists; source-derived or explicitly inferred |
| Verification criterion | Observable condition for satisfaction |
| Verification method | Inspection, analysis, demonstration, or test; TBD if unknown |
| Priority / criticality | Only when justified and approved |
| Status | Lifecycle state from Section 7 |
| Assigned phase | Proposed phase allocation with rationale |
| Dependencies | Related requirements, decisions, risks, or prerequisites |
| Owner | Assigned responsible authority or NOT_ASSIGNED |
| Change history | Changes and approval references |

## 5. Classification Taxonomy

A requirement may have one primary type and optional secondary tags.

| Type | Meaning |
|---|---|
| FUNCTIONAL | Defines a behavior, operation, service, or system response |
| SECURITY | Defines protection, authentication, authorization, integrity, confidentiality, or resilience obligations |
| PRIVACY | Defines personal-data handling, disclosure, minimization, retention, or access constraints |
| DATA_AND_RECORDS | Defines data structures, records, evidence, retention, or auditability |
| INTEROPERABILITY | Defines interaction with external systems, institutions, networks, or interfaces |
| PERFORMANCE_AND_CAPACITY | Defines measurable timing, throughput, capacity, availability, or resource limits |
| OPERATIONAL | Defines procedures, roles, monitoring, exception handling, continuity, or support |
| GOVERNANCE | Defines authority, approvals, accountability, policy, or institutional controls |
| COMPLIANCE | Defines an obligation traceable to an identified legal, regulatory, contractual, or institutional source |
| ARCHITECTURAL | Defines a structural design constraint or separation of responsibilities |
| INTERFACE | Defines inputs, outputs, messages, APIs, or human-machine interactions |
| VERIFICATION | Defines evidence, acceptance, validation, or test obligations |

Classification is not a statement of priority or approval. A requirement may carry multiple concerns, but its primary classification must be consistent and justified.

## 6. Mandatory, Design, Pending, and Open Decision Treatment

### 6.1 Mandatory requirements

Use MANDATORY only when the source or an approved authority makes the obligation explicit. Record the normative wording and evidence. Do not label a requirement mandatory solely because it appears technically desirable.

### 6.2 Design requirements

Use DESIGN for a structural or implementation constraint explicitly specified by an approved design source, or for a derived design constraint that is clearly labelled DERIVED and awaits approval. Do not confuse a design proposal with an adopted architecture decision.

### 6.3 Pending specification

Use PENDING_SPECIFICATION where the source establishes a need or behavior but does not provide enough detail to make it verifiable. Record the missing parameters, affected decisions, owner, and closure condition.

### 6.4 Open decisions

An unresolved choice is recorded as a decision item, not disguised as a requirement. Link it to the relevant ADR when WP-0.8 is established. Record alternatives, consequences, decision authority, and the point in the lifecycle by which it must be resolved.

## 7. Requirement Lifecycle Statuses

| Status | Meaning |
|---|---|
| CANDIDATE | Identified for review; not yet validated |
| SOURCE_VERIFIED | Exact source passage inspected and locator confirmed |
| IN_REVIEW | Submitted for classification or technical review |
| APPROVED | Explicitly approved by the authorized authority |
| REJECTED | Reviewed and not accepted; rationale retained |
| DEFERRED | Formally assigned to a later phase with justification |
| SUPERSEDED | Replaced by a later approved requirement |
| WITHDRAWN | Formally removed from scope with authority and rationale |
| BLOCKED | Verification or approval cannot proceed because of a named dependency |

A requirement's lifecycle status is separate from its source origin, classification, and assigned phase.

## 8. Extraction Procedure

For each source document:

1. Confirm the exact source file, document ID, version, provenance, and integrity status.
2. Inspect the complete source, including diagrams, tables, appendices, and notes.
3. Identify normative language (for example must, shall, required, prohibited) and explicit design constraints.
4. Separately flag descriptive statements that may imply a requirement but are not normative.
5. Create one candidate record per independently verifiable obligation.
6. Split compound statements where separate verification outcomes are needed.
7. Preserve source terminology; define any normalized wording in a separate field.
8. Record the exact source locator and evidence excerpt or faithful summary.
9. Classify the candidate and label its origin as EXTRACTED, DERIVED, or PROPOSED.
10. Identify missing parameters, ambiguities, contradictions, and dependencies.
11. Propose a verification criterion without inventing numerical thresholds.
12. Propose phase allocation based on lifecycle responsibility and approved roadmap dependencies.
13. Submit candidates for review and approval.
14. Preserve rejected, superseded, deferred, and withdrawn records.

## 9. Phase Allocation Method

Phase assignment must follow the approved ERX roadmap and the approved phase boundaries. Until those are reconciled under WP-0.3, phase allocation remains PROPOSED.

Use the following decision questions:
- Is this a governance or preparation obligation required before design begins?
- Does it define protocol behavior or architecture?
- Does it require software implementation?
- Does it require integration with a 911 center or external institution?
- Does it require controlled testing, independent validation, or certification?
- Does it require operational deployment or institutional authorization?

Do not assign a requirement to Phase 1 or any later phase solely from a guess. Record UNALLOCATED_PENDING_ROADMAP when the source and approved roadmap do not establish a defensible assignment.

## 10. Traceability Model

The traceability register must support these relationships:

`SOURCE → REQUIREMENT → DESIGN DECISION → IMPLEMENTATION ARTIFACT → VERIFICATION EVIDENCE → ACCEPTANCE`

Not every link exists during Phase 0. Missing downstream artifacts are recorded as NOT_YET_CREATED or NOT_APPLICABLE, not fabricated.

Minimum traceability checks:
- Every EXTRACTED requirement links to a verified source locator.
- Every DERIVED requirement links to all supporting source statements and a derivation rationale.
- Every PROPOSED requirement links to a documented gap or decision.
- Every APPROVED requirement has an explicit approval reference.
- Every verification result links to evidence and identifies the verifier.
- Changes to source or requirement versions trigger an impact review.

## 11. Contradictions, Ambiguities, and Change Impact

When two sources appear inconsistent:
- Preserve both exact statements and locators.
- Identify whether the conflict is direct, contextual, temporal, or caused by different scope.
- Record affected requirements and decisions.
- Do not select a winner until document authority is approved under WP-0.3.
- Route the matter to the contradiction register and, where appropriate, an ADR.
- Record the approved disposition and its impact on all linked requirements.

When a source changes, identify affected requirement records and downstream decisions, designs, tests, and reports.

## 12. Source Inspection Baseline and Extraction Boundary

The provisional master index records five foundational source files:
- ERX-PROT-001 v1.1 — supplied as `ERX byLAEV 1.pdf`.
- ERX-ATLAS-001 v1.1 — supplied as `ERX-ATLAS-001 v1.pdf`.
- UTXO-911-001 v1.0 — supplied as `UTXO DE COMUNICACIÓN 911 byLAEV.pdf`.
- ERX-ROADMAP-001 v1.0 — supplied as `### ERX-ROADMAP-001.pdf`.
- Technical response to ERX-ROADMAP-001 — formal identifier and version not stated in the provisional index.

The master index also records ERX-CONSENSUS-001 v0.1 and ERX-IMPL-PROPOSAL-001 as referenced but not located.

The five foundational PDFs were directly opened and text-extracted from the exact supplied files for the WP-0.7 source-inspection pass on 2026-11-25. The inspection set and source integrity metadata remain governed by the accepted WP-0.2 dossier. Their contents are now eligible for requirement extraction only with exact source/page/section locators and source-native wording.

The inspection confirmed the following identity/control facts without substituting extraction for approval:
- ERX-PROT-001 v1.1; 29 pages; source status describes a design specification for implementation/evaluation/institutional homologation.
- ERX-ATLAS-001 v1.1; 29 pages; graphical representation related to ERX-PROT-001 v1.1.
- UTXO-911-001 v1.0; 12 pages; conceptual and functional three-stage communication UTXO cycle.
- ERX-ROADMAP-001 v1.0; 37 pages; development and phase-planning source.
- Technical response to the Roadmap; 2 pages; formal ID/version not stated in source.

ERX-CONSENSUS-001 v0.1 remains a proposal for review; ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED. Neither may be used as an inspected requirement source.

No requirement is approved merely by extraction. Source fidelity takes precedence over inferred completion.

## 13. Required Register and Matrix

Canonical machine-readable register:
`registers/requirements-traceability.csv`

The register must use the fields defined in Section 4. The initial schema is published separately. A human-readable requirement specification or analysis may be added under `docs/requirements/` after source extraction begins.

The matrix must allow filtering by source, type, origin, status, phase, owner, and verification method.

## 14. WP-0.7 Acceptance and Dependency Gate

**Status: WP-0.7 EXECUTION INITIATED — ACTIVITY 0.7.1 METHOD CONTROLLED.**

The Workplan dependencies WP-0.3 and WP-0.6 are COMPLETED / ACCEPTED. Formal execution is recorded in ERX-WP-0.7-INITIATION-RECORD-001 v1.0.0. This controlled method fulfills the method deliverable for activity 0.7.1; the remaining activities are still open.

Acceptance of the entire WP-0.7 requires:
1. WP-0.3 hierarchy and subject-matter authority approved.
2. WP-0.6 master index accepted and reconciled.
3. Exact source versions inspected and locators recorded.
4. Existing requirements extracted without silent inference.
5. Every requirement individually identified and classified.
6. Mandatory, design, pending-specification, and open-decision items distinguished.
7. Every requirement linked to source evidence or clearly labelled DERIVED / PROPOSED.
8. Phase assignments justified against the approved roadmap.
9. Traceability matrix validated for completeness and consistency.
10. LAEV review and express approval recorded under the standing conditional acceptance instruction when the complete WP-0.7 evidence package is ready.

**Acceptance of this method closes only the method deliverable for activity 0.7.1. It does not complete WP-0.7, approve extracted requirements, or authorize Phase 1.**

---
End of ERX-REQUIREMENTS-METHOD-001


## 12. Controlled batch continuation

Each additional extraction batch must state the exact source/version, page/section range inspected, candidate IDs added, treatment of recommendation language, and resulting register row count. A batch count is not an acceptance metric. Candidate IDs must be unique across the full register. Before merging a batch, validate CSV field count, ID uniqueness, source locator presence, origin class, lifecycle status and explicit non-approval state. Any record whose source modality is not explicit must remain DERIVED or PROPOSED rather than being represented as EXTRACTED.
