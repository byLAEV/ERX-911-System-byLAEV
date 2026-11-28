# WORKPLAN-PHASE-0
## ERX byLAEV Project Governance and Preparation

- **Project:** ERX-911-System-byLAEV
- **Identifier:** ERX-WP-PHASE-0-001
- **Phase:** 0 — Project Governance and Preparation
- **Version:** 1.5.5
- **Status:** APPROVED — WORK-PACKAGE SCOPE AUTHORIZATION, 2026-11-24
- **Design and Approval Authority:** LAEV

## 1. Purpose and Nature

This Workplan converts the Phase 0 breakdown into an execution and tracking instrument. It organizes the twelve work packages, their activities, dependencies, deliverables, evidence, and acceptance criteria.

This document plans the work; it does not declare activities executed, replace foundational sources or normative documents, or constitute approval of Phase 0.

## 2. Execution Rules

1. Preserve original documents; develop changes in derivative documents with traceability.
2. Do not resolve contradictions or gaps through silent inference. Record sources, impact, owner, and status.
3. Identify each document by code, version, status, authorship, provenance, history, and approval where applicable.
4. Change statuses only when verifiable evidence exists.
5. Allow parallel work only when dependencies are satisfied.
6. A commit or file publication does not constitute approval.
7. Keep pending matters visible; do not present them as resolved.
8. Phase 0 does not authorize implementation, deployment, or institutional operation of the 911 system.

## 3. Tracking Statuses

**Governance clarification approved 2026-11-24:** For this Workplan, every WP-0.1–WP-0.12 has LAEV approval of its scope and planned deliverables. `APPROVED` records authorization/approval of the work-package scope; it does **not** mean that its activities have been executed, deliverables completed, acceptance criteria satisfied, or dependencies released. Execution state is therefore shown separately in each WP and in Section 7. Dependency gates remain binding. No later WP may begin execution until its prerequisites are satisfied and its execution is formally initiated. WP-0.12 approval does not constitute Phase 0 closure or authorize Phase 1.

| Status | Meaning |
|---|---|
| NOT_STARTED | No verifiable work has been recorded. |
| IN_PROGRESS | Work is underway; partial evidence exists. |
| IN_REVIEW | Deliverable submitted for review. |
| BLOCKED | A pending dependency or decision prevents progress. |
| APPROVED | Expressly approved by the relevant authority. |
| COMPLETED | Acceptance criteria satisfied and evidence recorded. |
| DEFERRED | Formally moved to another phase with approved justification. |

**Historical baseline:** all work packages were initially NOT_STARTED when the Workplan was first prepared. Current statuses are maintained in Section 5 and the Tracking Register in Section 7; this historical baseline is not the current status declaration.

## 4. Sequence and Control Gates

```text
START
  |
  v
0.1 Phase Definition and Rationale
  |
  v
0.2 Foundational Materials
  |
  v
0.3 Document Hierarchy
  |
  +------> 0.4 Document Control
  +------> 0.5 Repository
                 |
                 v
          0.6 Master Index
                 |
          +------+------+
          v             v
     0.7 Requirements  0.8 ADR Decisions
          +------+------+
                 v
        0.9 Risks and Dependencies
                 |
                 v
        0.10 Governance and Responsibilities
                 |
                 v
        0.11 Version and Change Control
                 |
                 v
        0.12 Verification and Closure
                 |
          Formal LAEV Approval
                 |
                 v
       Authorization of Next Phase
```

The sequence represents logical dependencies. Iteration and controlled concurrency are permitted without changing source authority.

## 5. Work Packages

### WP-0.1 — Phase 0 Definition and Rationale
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** APPROVED / baseline activities recorded; not separately declared COMPLETED.

**Activities**
- [x] 0.1.1 Phase identification.
- [x] 0.1.2 Purpose.
- [x] 0.1.3 General objective.
- [x] 0.1.4 Specific objectives.
- [x] 0.1.5 Phase justification.
- [x] 0.1.6 Scope of work.
- [x] 0.1.7 Scope exclusions.
- [x] 0.1.8 Development principles.
- [x] 0.1.9 Completion criteria.

**Deliverable:** `docs/phase-0/ERX-PHASE-0-CHARTER-001.md`  
**Acceptance:** SATISFIED for WP-0.1 through LAEV's express approval of Charter version 1.0.0. WP-0.1 is APPROVED; it is not declared COMPLETED until evidence and the tracking record are consolidated under Phase 0 controls.  
**Input:** Phase 0 breakdown defined by LAEV.

### WP-0.2 — Identification and Consolidation of Foundational Materials
**Approval status:** APPROVED — LAEV, 2026-11-23
**Execution status:** baseline accepted and evidence recorded; approval is not a claim of implementation.

**Activities**
- [x] 0.2.1 Identify existing sources (five supplied PDFs inspected).
- [x] 0.2.2 Inventory original documents (five-source baseline recorded).
- [x] 0.2.3 Record available provenance; missing metadata explicitly flagged.
- [x] 0.2.4 Record versions stated in the source documents; unstated versions flagged.
- [x] 0.2.5 Provisional classification by document type.
- [x] 0.2.6 Archive exact original PDF binaries in `docs/` and verify byte identity/integrity against the supplied originals.
- [x] 0.2.7 Identify sources referenced but not supplied (ERX-CONSENSUS-001 and ERX-IMPL-PROPOSAL-001).
- [x] 0.2.8 Record identified source cross-references and prepare bounded cross-document comparison.
- [x] 0.2.9 Publish the initial foundational materials register (baseline; final review pending).

**Deliverables:** `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`, `docs/foundational/README.md`, `registers/foundational-material-register.csv`, [`docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md`](docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md) v0.1.0 — WORKING DRAFT, and [`docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md`](docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md) with [`registers/document-issue-register.csv`](registers/document-issue-register.csv) as preparatory WP-0.3 inputs. **Evidence:** five supplied PDFs inspected, source topics and bounded cross-document correspondences recorded, and present on `main` under `docs/`; registered SHA-256 checksums match the supplied originals, and locally calculated Git blob SHA-1 values match the GitHub blob SHAs for all five. See `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`. DOC-ISS-008 is RESOLVED_EVIDENCE. ERX-CONSENSUS-001 v0.1 identity/content is confirmed from the repository plain-text source discovered after approval; proposal status and operational completeness are tracked under DOC-ISS-011. The accepted WP-0.2 five-PDF baseline remains unchanged. ERX-IMPL-PROPOSAL-001 remains NOT LOCATED / UNVERIFIED (DOC-ISS-003). **Acceptance:** SATISFIED by LAEV's explicit approval in the project conversation on 2026-11-23. The five-source inventory, archival integrity evidence and bounded source-inspection record are accepted as the WP-0.2 baseline. At the time of approval, both Roadmap references were recorded as not located; subsequent supplemental text inspection confirms ERX-CONSENSUS-001 v0.1 identity/content, while it remains a proposal for review and DOC-ISS-011 tracks operational completeness. ERX-IMPL-PROPOSAL-001 remains not located. These post-approval findings do not retroactively alter the accepted baseline.  
**Acceptance:** each known source has an ID, name, provenance, version, location, integrity, and status; missing sources and uncertainties are explicit. Do not reconstruct missing sources through assumptions.  
**Dependency:** WP-0.1.

### WP-0.3 — Document Organization and Hierarchy
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** COMPLETED / ACCEPTED — documentary deliverables and evidence recorded.

**Activities**
- [x] 0.3.1 Classify documents and distinguish sources from project artifacts.
- [x] 0.3.2 Establish source/artifact separation and rationale.
- [x] 0.3.3 Approve document hierarchy (DP-01).
- [x] 0.3.4 Approve subject-matter authority (DP-01).
- [x] 0.3.5 Record source-backed relationships and dependencies.
- [x] 0.3.6 Compare and disposition documentary issues DOC-ISS-001–011.
- [x] 0.3.7 Approve contradiction/ambiguity handling procedure.
- [x] 0.3.8 Approve document evolution and supersession policy.

**Controlling evidence**
- LAEV decision record: `docs/phase-0/ERX-WP-0.3-LAEV-DECISION-RECORD-001.md` v1.0.0 — APPROVED; DP-01–DP-09 and issue dispositions.
- Deliverable matrix: `docs/phase-0/ERX-WP-0.3-DELIVERABLE-COMPLETION-MATRIX-001.md` v1.0.2 — COMPLETED / ACCEPTED.
- Execution record: `docs/phase-0/ERX-WP-0.3-EXECUTION-RECORD-001.md` v1.0.1 — COMPLETED / ACCEPTED.
- Acceptance readiness: `docs/phase-0/ERX-WP-0.3-ACCEPTANCE-READINESS-REPORT-001.md` v1.0.0 — ACCEPTED.
- Internal audit: `docs/phase-0/ERX-WP-0.3-AUDIT-REPORT-001.md` v1.0.3 — final result in Section 9; Sections 2–8 are preserved historical snapshots.
- Issue register: `docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md` v1.0.0 and `registers/document-issue-register.csv` — disposition states synchronized.

**Accepted residual controls**
- DOC-ISS-003 / ERX-IMPL-PROPOSAL-001: NOT LOCATED / UNVERIFIED; accepted bounded source-location limitation. No content inferred.
- DOC-ISS-010: independent agent-availability cycle accepted; detailed state-machine specification deferred.
- DOC-ISS-011 / ERX-CONSENSUS-001 v0.1: remains a proposal for review; operational consensus specification/approval deferred. No operational or multi-institutional consensus authorization.
- Independent external review: NOT PERFORMED / NOT CLAIMED; separate from LAEV approval and internal documentary acceptance.
- DOC-ISS-001 and DOC-ISS-004 preserve source-native metadata limitations; catalogue treatment is controlled under WP-0.4.

**Acceptance:** Activities 0.3.1–0.3.8 have evidence; DP-01–DP-09 are recorded in LAEV's approved decision record; all DOC-ISS-001–011 have a final disposition; Markdown and CSV issue registers are synchronized; governance procedures are approved; bounded limitations and deferred specifications are explicit. WP-0.3 documentary acceptance does not certify implementation, security, external audit, institutional homologation or production readiness.

**Dependency:** WP-0.2 APPROVED. WP-0.3 COMPLETED / ACCEPTED. WP-0.4 retains its own separate approval and closeout evidence; WP-0.5 remains subject to its stated dependencies. No Phase 1 or production authorization is granted.

### WP-0.4 — Document Identification and Control
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** COMPLETED / ACCEPTED — baseline v1.0.0 approved under its separate approval record.

**Activities**
- [x] 0.4.1 Develop ERX identifier system proposal.
- [x] 0.4.2 Develop canonical document naming proposal.
- [x] 0.4.3 Develop versioning proposal.
- [x] 0.4.4 Define proposed document lifecycle statuses and transitions.
- [x] 0.4.5 Define required metadata by document class.
- [x] 0.4.6 Define separate authorship and design-authority records.
- [x] 0.4.7 Define review and approval record requirements.
- [x] 0.4.8 Define revision history and change traceability.
- [x] 0.4.9 Define cross-reference and provenance rules.

**Candidate deliverable:** [`docs/phase-0/ERX-DOCUMENT-CONTROL-001.md`](docs/phase-0/ERX-DOCUMENT-CONTROL-001.md) v1.0.0 — APPROVED — LAEV; candidate v0.4.2 approved by exact blob SHA-1 and released as first baseline.
**Execution evidence:** candidate v0.4.2 prepared on branch `wp-0.4-document-control`; LAEV approved DC-01–DC-09 and issued Addendum B deferring independent external review/audit until after planned project work, recorded in `ERX-WP-0.4-LAEV-DECISION-RECORD-001` v1.2.0. Internal consistency review is recorded in `ERX-WP-0.4-INTERNAL-REVIEW-001` v0.2.0; LAEV exact-version approval is recorded in `ERX-WP-0.4-APPROVAL-RECORD-001` v1.0.0; closeout audit is `ERX-WP-0.4-CLOSEOUT-AUDIT-001` v0.5.0. The former v0.2.0, v0.3.1, and v0.4.0 candidates were reconciled; none was treated as an approved policy baseline.
**Closeout:** LAEV approved exact candidate v0.4.2 (blob SHA-1 `7cde15d1776ed913c3136f8116f8eb3912b302f1`) as baseline v1.0.0. Approval, internal review, closeout audit, execution record, and register are synchronized. WP-0.4 is COMPLETED / ACCEPTED. Independent external review/audit is deferred until after planned project work and is not an inter-work-package gate.
**Acceptance:** unique non-reusable identifiers; canonical naming with original-source preservation; versioning; document lifecycle statuses distinct from work-package statuses; metadata by document class; separate authorship/review/approval; reconstructable revision history; exact cross-references; controlled migration; express LAEV approval of the exact final version.
**Dependencies:** WP-0.1 APPROVED and WP-0.3 COMPLETED / ACCEPTED. WP-0.4 has its own approval/closeout record and its prerequisite WP-0.3 is now accepted; the earlier sequencing-deviation concern is resolved by the current DP-01–DP-09 decision record and synchronized closeout evidence.

### WP-0.5 — ERX Repository Creation and Organization
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** COMPLETED / ACCEPTED — LAEV conditional acceptance recorded 2026-11-24 in `ERX-WP-0.5-ACCEPTANCE-RECORD-001` v1.0.0.

**Activities**
- [x] 0.5.1 Repository identity.
- [x] 0.5.2 Repository objective.
- [x] 0.5.3 Directory structure.
- [x] 0.5.4 Foundational materials location.
- [x] 0.5.5 Phase 0 documents location.
- [x] 0.5.6 Access policy.
- [x] 0.5.7 Branch organization.
- [x] 0.5.8 Change control.
- [x] 0.5.9 Git change history.
- [x] 0.5.10 Intellectual property and license.

**As-built structure:** the actual main-branch structure is recorded in `ERX-WP-0.5-REPOSITORY-TREE-INVENTORY-001` v1.0.0 (recursive tree SHA `4be78630ab694b1f2c970684e6b6db3f074b1e68`, `truncated=false`). Future target directories are distinguished from paths that currently exist; no empty directories were created merely to match a proposal.

**Controlling deliverables and acceptance evidence:**
- `ERX-WP-0.5-INITIATION-RECORD-001` v1.0.0 — RECORDED.
- `ERX-WP-0.5-REPOSITORY-TREE-INVENTORY-001` v1.0.0 — VERIFIED SNAPSHOT.
- `ERX-WP-0.5-REPOSITORY-AUDIT-001` v0.4.0 — preliminary observations retained as historical evidence; final closeout in separate audit.
- `ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001` v0.4.0 — APPROVED by DP-ACCESS-02.
- `ERX-WP-0.5-ACCESS-DECISION-002` v1.0.0 — LAEV decision; one independent technical review when available and assigned.
- `ERX-WP-0.5-REPOSITORY-VISIBILITY-DECISION-001` v1.0.0 — KEEP PUBLIC.
- `ERX-WP-0.5-REPOSITORY-ADMINISTRATION-DECISION-001` v1.0.0 — DP-ACCESS-01, LAEV sole administrator as intended governance model.
- `ERX-REPOSITORY-GOVERNANCE-001` v1.0.0 — APPROVED, conditional LAEV acceptance.
- `ERX-WP-0.5-DELIVERABLE-COMPLETION-MATRIX-001` v1.0.2 — COMPLETED / ACCEPTED.
- `ERX-WP-0.5-ACCEPTANCE-READINESS-REPORT-001` v1.0.0 — READY FOR CONDITIONAL ACCEPTANCE.
- `ERX-WP-0.5-CLOSEOUT-AUDIT-001` v1.0.0 — COMPLETED.
- `ERX-WP-0.5-ACCEPTANCE-RECORD-001` v1.0.0 — RECORDED — COMPLETED / ACCEPTED.
- `registers/repository-governance-evidence.csv` — bounded observations and decisions.

**Acceptance:** SATISFIED. Repository identity/objective, actual directory and document locations, access governance, branch model/current branch state, change control, Git history traceability, and intellectual-property/license status are documented with evidence and explicit limitations.

**Residual limitations retained, not represented as resolved:** complete collaborator/team/inherited-access roster NOT_VERIFIED; live sole-admin condition NOT_RECONCILED; `main` observed unprotected and technical enforcement NOT_IMPLEMENTED; independent reviewer NOT_ASSIGNED; workflow token/security settings NOT_AUDITED; independent backup/restore NOT_VERIFIED; comprehensive rights review OPEN; NO LICENSE ASSIGNED. Any GitHub permission/protection change or license decision remains subject to the separate express authorization specified by the controlling decision records. No external audit, legal opinion, security certification, or disaster-recovery readiness is claimed.

**Dependencies:** WP-0.3 and WP-0.4 — both COMPLETED / ACCEPTED. All ten WP-0.5 documentary activities satisfy the Workplan criterion. WP-0.5 is COMPLETED / ACCEPTED; the WP-0.6 dependency gate is SATISFIED. This does not close Phase 0 or authorize Phase 1.

### WP-0.6 — Master Index and Document Register
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** COMPLETED / ACCEPTED — 2026-11-25.
**Acceptance evidence:** ERX-WP-0.6-ACCEPTANCE-RECORD-001 v1.0.1; readiness report v1.0.0; closeout audit v1.0.1.

**Activities**
- [x] 0.6.1 General document register — ERX-DOCUMENT-REGISTER-001 v1.2.4; current catalogue 80 records, 16 columns, 79 live paths plus one NOT_LOCATED reference-only source; live-tree coverage rechecked 79/79.
- [x] 0.6.2 Identify foundational documents — five accepted originals and supplemental consensus source identified; missing implementation proposal bounded under DOC-ISS-003.
- [x] 0.6.3 Identify development documents — recursive-tree inventory and path coverage completed.
- [x] 0.6.4 Record versions — source-native versions, formal IDs and NOT_STATED exceptions reconciled.
- [x] 0.6.5 Classify documents — classifications checked against approved WP-0.3 hierarchy and WP-0.4 document control.
- [x] 0.6.6 Record each document's status — lifecycle, source status, acceptance, evidence, custody and presence separated.
- [x] 0.6.7 Record relationships — approved WP-0.3 baseline preserved; typed supplement reconciled.
- [x] 0.6.8 Identify pending documents — missing, proposal, deferred and metadata gaps recorded without inference.
- [x] 0.6.9 Consolidate master index — index and CSV synchronized; final structural checks and closeout passed.

**Controlled deliverables:** Master index; ERX-DOCUMENT-REGISTER-001 CSV; activity matrix v0.5.4; relationship register v0.2.2; internal review v0.3.3; readiness report v1.0.0; closeout audit v1.0.1; acceptance record v1.0.1.
**Accepted limitation:** ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED / UNVERIFIED under DOC-ISS-003. This is explicitly recorded and does not invalidate the completed inventory.
**Dependency release:** WP-0.7 may proceed under its previously approved scope. This acceptance does not authorize Phase 1, implementation or institutional operation.

### WP-0.7 — Requirements Identification and Classification
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** IN_PROGRESS — formally initiated 2026-11-25; dependency gate satisfied by WP-0.6 acceptance. Formal acceptance determination v1.0.0: **NOT GRANTED** (2026-11-28).

**Current reconciled inventory (2026-11-25):** 82 source candidates in the canonical traceability CSV (26 columns); 107 individually identified records in the companion register. The former 65-row matrix v0.2.0 and 65-candidate snapshots are superseded by source-candidate matrix v0.4.3. All candidates remain NOT_APPROVED.

**Activities**
- [x] 0.7.1 Identification methodology — controlled ERX-REQUIREMENTS-METHOD-001 v1.0.0.
- [x] 0.7.2 Extract existing requirements — bounded five-source extraction completed through batches 001–005; 82 unique candidates. Exact clause support remains a separate 0.7.9 acceptance gate.
- [x] 0.7.3 Individually identify requirements — COMPLETED / ACCEPTED by LAEV; 107 unique records reconcile to 82 parent candidates, with decomposition, atomicity and overlap dispositions recorded.
- [x] 0.7.4 Classify requirements — classification executed for 82 source candidates and 107 individuals; controlled taxonomy and rationale recorded. **Semantic review and LAEV acceptance remain pending as separate baseline-acceptance gates.**
- [x] 0.7.5 Identify mandatory requirements — COMPLETED / ACCEPTED, 2026-11-28. Exact source/Atlas fidelity: 82/82 VERIFIED. Independent individual semantic/modality review: 107/107 VERIFIED; condition/scope PASS; actor/trigger/outcome PASS or explicitly justified NOT_APPLICABLE for descriptive/definitional items. Source and child canonical registers synchronized. GitHub Actions evidence gate PASS, run #18 (`35fcd16455b5c849e7103245f7a7ad2e63faf440`). Controlling records: [mandatory assessment v0.7.0](docs/phase-0/ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001.md), [individual modality review v1.4.0](docs/phase-0/ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001.md), [source fidelity matrix](registers/wp-0.7.5-source-fidelity-review.csv), [individual semantic matrix](registers/wp-0.7.5-individual-semantic-review.csv), and [completion record v1.1.0](docs/phase-0/ERX-WP-0.7.5-COMPLETION-RECORD-001.md). This closes Activity 0.7.5 only; all requirements remain NOT_APPROVED pending the separate WP-0.7 baseline process.
- [x] 0.7.6 Identify design requirements — design-assessment categories recorded for all 82 source candidates; derived design proposals remain distinct. Child-level semantic review and LAEV acceptance remain pending.
- [x] 0.7.7 Record requirements pending specification — 76 OPEN detailed specification gaps (63 historical + 13 supplemental) and six NO_GAP_WITH_EVIDENCE dispositions cover all 82 source candidates. The activity's candidate-level coverage is documented and phase-routed; technical closure of 76 gaps, named owner assignment and 107-child applicability remain pending. 
- [x] 0.7.8 Record open decisions — eight open-decision candidates reviewed for inventory completeness and source/requirement linkage; decisions remain OPEN for WP-0.8. LAEV decision ownership is recognized, but due points and formal ADR outcomes remain pending. No decision resolved and no ADR approved.
- [ ] 0.7.9 Link requirements to sources — all 82 source candidates have exact passage/diagram fidelity VERIFIED under Activity 0.7.5; the separate 0.7.9 source-linkage/bidirectional traceability activity remains IN_PROGRESS.
- [x] 0.7.10 Assign requirements to phases — all 82 source candidates have a preliminary primary phase and dependency rationale recorded in allocation v0.3.3. Allocations are planning-only; child-level mappings remain an acceptance gate.
- [x] 0.7.11 Build traceability matrix — regenerated matrix v0.4.3 for 82 source candidates from CSV SHA 5a428e40a29f31558330ffc8ab25dc1f8970285e; semantic/referential and child-level acceptance audit remains pending.

**Latest audit:** [Bidirectional traceability audit v1.0.0](docs/phase-0/ERX-WP-0.7-BIDIRECTIONAL-TRACEABILITY-AUDIT-001.md) — structural PASS at source-candidate layer; [acceptance determination v1.0.0](docs/phase-0/ERX-WP-0.7-ACCEPTANCE-DETERMINATION-001.md) — ACCEPTANCE NOT GRANTED.\n\n**Controlled evidence:** initiation and source-inspection records; extraction batches 001–005; extraction completion record; accepted 0.7.3 record and atomicity/overlap disposition; classification record; design-requirements assessment v0.1.1; mandatory assessment v0.4.0; individual modality review v1.1.0; child modality correction v1.0.0; source-coverage audit v0.3.0; pending-specification register v0.5.0; open-decision review; phase-allocation register v0.3.2; LAEV baseline decision pack; verification-criteria proposal v0.3.1; semantic review register; review report; canonical source and individual registers; regenerated matrix v0.4.3; WP-0.7 status reconciliation v0.5.0; bidirectional traceability audit v1.0.0; acceptance determination v1.0.0.

**Acceptance gate:** each candidate/individual must have stable ID and lineage, atomic/unambiguous statement, exact source-fidelity disposition, origin class, semantically validated type and normative/design status, specification and decision links, justified phase/dependencies, approved objective criterion/method, and recorded review disposition. Structural matrix and parent/dependency integrity audit has passed; semantic and source-fidelity acceptance remains open. Derived/proposed content must remain distinguishable from source requirements. Explicit LAEV acceptance must identify exact baseline versions and commit.

**Dependency and authorization boundary:** WP-0.3 and WP-0.6 are COMPLETED / ACCEPTED. WP-0.7 execution is authorized under its approved scope. WP-0.8 remains NOT_STARTED until WP-0.7 is formally completed and accepted. No Phase 1 execution, implementation, deployment or institutional operation is authorized.

### WP-0.8 — Architecture Decision Register (ADR)
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** NOT_STARTED.

**Activities**
- [ ] 0.8.1 ADR purpose and format.
- [ ] 0.8.2 Identify decisions.
- [ ] 0.8.3 Record context.
- [ ] 0.8.4 Describe the problem being solved.
- [ ] 0.8.5 Record alternatives considered.
- [ ] 0.8.6 Record adopted or pending decision.
- [ ] 0.8.7 Document rationale.
- [ ] 0.8.8 Document consequences.
- [ ] 0.8.9 Identify approved decisions.
- [ ] 0.8.10 Identify pending decisions.
- [ ] 0.8.11 Maintain history and supersessions.

**Deliverable:** `docs/decisions/` and `registers/decision-register.csv`.  
**Acceptance:** each material decision contains context, alternatives, decision, rationale, consequences, sources, owner, and status; superseded decisions remain accessible.  
**Dependencies:** WP-0.3, WP-0.6, and WP-0.7.

### WP-0.9 — Risk and Dependency Register
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** NOT_STARTED.

**Activities**
- [ ] 0.9.1 Identification methodology.
- [ ] 0.9.2 Record documentary risks.
- [ ] 0.9.3 Record architectural risks.
- [ ] 0.9.4 Record technical risks.
- [ ] 0.9.5 Record institutional risks.
- [ ] 0.9.6 Classify impact and priority.
- [ ] 0.9.7 Define mitigation measures.
- [ ] 0.9.8 Record documentary dependencies.
- [ ] 0.9.9 Record technical dependencies.
- [ ] 0.9.10 Record institutional dependencies.
- [ ] 0.9.11 Record inter-phase dependencies.
- [ ] 0.9.12 Define resolution conditions.

**Deliverable:** `registers/risk-dependency-register.csv` and `docs/phase-0/ERX-RISK-METHOD-001.md`.  
**Acceptance:** each risk or dependency has an ID, category, source, impact, priority, mitigation, owner, status, and closure condition.  
**Dependencies:** WP-0.6, WP-0.7, and WP-0.8.

### WP-0.10 — Governance and Responsibilities
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** NOT_STARTED.

**Activities**
- [ ] 0.10.1 Define the ERX governance model.
- [ ] 0.10.2 Document LAEV design authority.
- [ ] 0.10.3 Define protocol responsibility.
- [ ] 0.10.4 Define software responsibility.
- [ ] 0.10.5 Define security responsibility.
- [ ] 0.10.6 Define validation responsibility.
- [ ] 0.10.7 Define independent technical validation.
- [ ] 0.10.8 Define review procedure.
- [ ] 0.10.9 Define approval procedure.
- [ ] 0.10.10 Define handling of comments.
- [ ] 0.10.11 Build the responsibility matrix.

**Deliverable:** `docs/governance/ERX-GOVERNANCE-MODEL-001.md` and RACI matrix.  
**Acceptance:** authority and functions are delimited; approvals are identifiable; comments are traceable; independent validation is separate from authorship and design.  
**Dependencies:** WP-0.1, WP-0.3, and WP-0.7 through WP-0.9.

### WP-0.11 — Version Planning and Control
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** NOT_STARTED.

**Activities**
- [ ] 0.11.1 Versioning policy.
- [ ] 0.11.2 Document versioning.
- [ ] 0.11.3 Repository versioning.
- [ ] 0.11.4 Identify draft versions.
- [ ] 0.11.5 Identify approved versions.
- [ ] 0.11.6 Change procedure.
- [ ] 0.11.7 Change review.
- [ ] 0.11.8 Change approval.
- [ ] 0.11.9 Retain previous versions.
- [ ] 0.11.10 Maintain change log.
- [ ] 0.11.11 Define documentary continuity.

**Deliverable:** `docs/phase-0/ERX-VERSION-AND-CHANGE-CONTROL-001.md` and `registers/change-log.md`.  
**Acceptance:** every change can be traced from request, review, and approval through the commit and resulting version; previous versions are recoverable.  
**Dependencies:** WP-0.4, WP-0.5, WP-0.6, and WP-0.10.

### WP-0.12 — Phase 0 Verification and Closure
**Approval status:** APPROVED — LAEV, 2026-11-24
**Execution status:** NOT_STARTED.

**Activities**
- [ ] 0.12.1 Consolidate deliverables.
- [ ] 0.12.2 Verify repository.
- [ ] 0.12.3 Verify sources.
- [ ] 0.12.4 Verify master index.
- [ ] 0.12.5 Verify requirements.
- [ ] 0.12.6 Verify decisions.
- [ ] 0.12.7 Verify risks and dependencies.
- [ ] 0.12.8 Verify responsibilities.
- [ ] 0.12.9 Verify version control.
- [ ] 0.12.10 Record pending comments.
- [ ] 0.12.11 Issue compliance report.
- [ ] 0.12.12 Obtain LAEV approval.
- [ ] 0.12.13 Formally record closure.
- [ ] 0.12.14 Authorize the start of the next phase.

**Deliverables:** `docs/reports/ERX-PHASE-0-COMPLIANCE-REPORT-001.md` and `docs/reports/ERX-PHASE-0-CLOSURE-RECORD-001.md`.  
**Acceptance:** work packages are COMPLETED or DEFERRED with approved justification; pending matters are recorded with impact and mitigation; the report links verifiable evidence; LAEV expressly approves; a closure record and authorization for the next phase exist.  
**Dependencies:** WP-0.1 through WP-0.11.

## 6. Dependency Matrix

| Work Package | Dependencies | Enabled Outcome |
|---|---|---|
| WP-0.1 | Phase 0 breakdown | Mandate and boundaries |
| WP-0.2 | WP-0.1 | Source inventory |
| WP-0.3 | WP-0.2 | Document hierarchy |
| WP-0.4 | WP-0.1, WP-0.3 | Document control |
| WP-0.5 | WP-0.3, WP-0.4 | Organized repository |
| WP-0.6 | WP-0.2 through WP-0.5 | Master index |
| WP-0.7 | WP-0.3, WP-0.6 | Traceable requirements |
| WP-0.8 | WP-0.3, WP-0.6, WP-0.7 | Traceable decisions |
| WP-0.9 | WP-0.6 through WP-0.8 | Risks and dependencies |
| WP-0.10 | WP-0.1, WP-0.3, WP-0.7 through WP-0.9 | Governance and responsibilities |
| WP-0.11 | WP-0.4 through WP-0.6, WP-0.10 | Change control |
| WP-0.12 | WP-0.1 through WP-0.11 | Closure and authorization |

## 7. Tracking Register

| ID | Work Package | Status | Owner | Evidence | Notes |
|---|---|---|---|---|---|
| WP-0.1 | Definition and Rationale | APPROVED | LAEV | [ERX-PHASE-0-CHARTER-001 v1.0.0](docs/phase-0/ERX-PHASE-0-CHARTER-001.md) · express approval 2026-11-23 | Four technical adjustments incorporated; WP-0.1 approved, not declared COMPLETED. |
| WP-0.2 | Foundational Materials | APPROVED | LAEV | [Source inventory](docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md) · [CSV register](registers/foundational-material-register.csv) · [Cross-reference map](docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md) · [Archive procedure](docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md) · [Completion dossier](docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md) | Five originals archived in `docs/` and byte-identity verified; DOC-ISS-008 resolved; LAEV expressly accepted WP-0.2 baseline on 2026-11-23. A post-approval text source `docs/Consenso ERX byLAEV` confirms ERX-CONSENSUS-001 v0.1 identity/content; DOC-ISS-011 tracks proposal status and operational completeness; ERX-IMPL-PROPOSAL-001 remains NOT LOCATED / UNVERIFIED (DOC-ISS-003). |
| WP-0.3 | Document Hierarchy | APPROVED — execution COMPLETED / ACCEPTED | LAEV | [Decision record v1.0.0](docs/phase-0/ERX-WP-0.3-LAEV-DECISION-RECORD-001.md) · [Completion matrix v1.0.2](docs/phase-0/ERX-WP-0.3-DELIVERABLE-COMPLETION-MATRIX-001.md) · [Execution record v1.0.1](docs/phase-0/ERX-WP-0.3-EXECUTION-RECORD-001.md) · [Acceptance readiness v1.0.0](docs/phase-0/ERX-WP-0.3-ACCEPTANCE-READINESS-REPORT-001.md) · [Final internal audit v1.0.3](docs/phase-0/ERX-WP-0.3-AUDIT-REPORT-001.md) · [Issue register](docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md) · [CSV](registers/document-issue-register.csv) | DP-01–DP-09 recorded; DOC-ISS-001–011 dispositioned; DOC-ISS-003 bounded limitation; DOC-ISS-010/011 deferred; ERX-CONSENSUS-001 remains proposal; no external audit or operational approval claimed. |
| WP-0.4 | Document Control | APPROVED — execution COMPLETED / ACCEPTED | LAEV | [Approved baseline](docs/phase-0/ERX-DOCUMENT-CONTROL-001.md) · [Approval record](docs/phase-0/ERX-WP-0.4-APPROVAL-RECORD-001.md) · [Closeout audit](docs/phase-0/ERX-WP-0.4-CLOSEOUT-AUDIT-001.md) | WP-0.4 has its own approval/closeout record; WP-0.3 is now accepted. External independent review remains deferred under WP-0.4's approved record, not represented as performed. |
| WP-0.5 | ERX Repository | APPROVED — execution COMPLETED / ACCEPTED | LAEV | [Governance v1.0.0](docs/phase-0/ERX-REPOSITORY-GOVERNANCE-001.md) · [Tree inventory](docs/phase-0/ERX-WP-0.5-REPOSITORY-TREE-INVENTORY-001.md) · [Acceptance readiness](docs/phase-0/ERX-WP-0.5-ACCEPTANCE-READINESS-REPORT-001.md) · [Closeout audit](docs/phase-0/ERX-WP-0.5-CLOSEOUT-AUDIT-001.md) · [Acceptance record](docs/phase-0/ERX-WP-0.5-ACCEPTANCE-RECORD-001.md) · [Access matrix](docs/phase-0/ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001.md) · [Evidence register](registers/repository-governance-evidence.csv) | All ten documentary activities accepted. Residual limitations remain explicit: full access roster NOT_VERIFIED; main unprotected; no license assigned; independent backup/restore and reviewer not verified/assigned. WP-0.6 dependency gate SATISFIED. No Phase 1 authorization. |
| WP-0.6 | Master Index | APPROVED — execution COMPLETED / ACCEPTED | LAEV / project drafting | [Initiation](docs/phase-0/ERX-WP-0.6-INITIATION-RECORD-001.md) · [Master index v1.5.2](docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md) · [Completion matrix v0.5.9](docs/phase-0/ERX-WP-0.6-DELIVERABLE-COMPLETION-MATRIX-001.md) · [Internal review v0.3.8](docs/phase-0/ERX-WP-0.6-INTERNAL-REVIEW-001.md) · [Relationship register v0.2.2](docs/phase-0/ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001.md) · [ERX-DOCUMENT-REGISTER-001 v1.2.4](registers/document-register.csv) · [Acceptance record](docs/phase-0/ERX-WP-0.6-ACCEPTANCE-RECORD-001.md) | WP-0.6 accepted under the recorded conditional acceptance. Current post-acceptance synchronization confirms 80 catalogue records/16 columns, 79 live paths plus one NOT_LOCATED reference, 79/79 path coverage and zero duplicate IDs/paths or stale/missing paths. WP-0.7 execution was initiated under its existing approval; no Phase 1 or implementation authorization. |
| WP-0.7 | Requirements | APPROVED — execution IN_PROGRESS; dependencies SATISFIED | LAEV / project drafting | [Initiation v1.0.0](docs/phase-0/ERX-WP-0.7-INITIATION-RECORD-001.md) · [Method v1.0.0](docs/phase-0/ERX-REQUIREMENTS-METHOD-001.md) · [Status reconciliation v0.4.1](docs/phase-0/ERX-WP-0.7-STATUS-RECONCILIATION-001.md) · [Source register](registers/requirements-traceability.csv) · [Individual register](registers/requirement-identification-register.csv) · [Traceability matrix v0.4.3](docs/phase-0/ERX-REQ-TRACEABILITY-MATRIX-001.md) | Current snapshot: 82 source candidates / 107 individual records; 76 open specification gaps + 6 evidence-backed no-gap dispositions; eight open decision candidates. Activities 0.7.1–0.7.8, 0.7.10 and 0.7.11 have execution artifacts; 0.7.9 exact passage/diagram fidelity review remains open. Semantic, child-level and cross-register acceptance audit, gap owners, decision owners/deadlines, criteria approval and exact-version LAEV baseline approval remain open. No requirement is approved by extraction alone. |
| WP-0.8 | ADR Decisions | APPROVED — execution NOT_STARTED | LAEV / to be assigned | — | — |
| WP-0.9 | Risks and Dependencies | APPROVED — execution NOT_STARTED | To be assigned | — | — |
| WP-0.10 | Governance | APPROVED — execution NOT_STARTED | LAEV / to be assigned | — | — |
| WP-0.11 | Versions and Changes | APPROVED — execution NOT_STARTED | To be assigned | — | — |
| WP-0.12 | Verification and Closure | APPROVED — execution NOT_STARTED | LAEV | — | — |

## 8. Phase 0 Exit Conditions

- [ ] Sources inventoried and preserved, or formally identified as missing.
- [ ] Document hierarchy and subject-matter authority approved.
- [ ] Document identification, versioning, and statuses defined.
- [ ] Repository, access, and change control approved.
- [ ] Master index consistent with actual documents.
- [ ] Requirements identified and traced to their sources.
- [ ] Architecture decisions recorded, including pending decisions.
- [ ] Risks and dependencies have mitigations and owners.
- [ ] Governance, review, and approval defined.
- [ ] Documentary continuity established.
- [ ] Compliance report and closure record available.
- [ ] Formal LAEV approval and authorization for the next phase.

A pending item does not automatically block closure if it is classified, has an owner, impact, mitigation, and an approved resolution phase. An open matter must not be presented as resolved.

## 9. Exclusions

This Workplan does not execute or declare complete detailed design or software implementation, UTXO implementation in the operational workflow, OpenTimestamps integration or timestamp submission, interoperability testing with 911 centers, regulatory certification, institutional acceptance, production deployment, or live emergency operations. These items will be assigned to later phases through approved requirements and decisions.

## 10. Approval Record

| Role | Authority | Status | Date | Evidence |
|---|---|---|---|---|
| Design and Approval Authority — WP-0.1 through WP-0.12 scope approval | LAEV | APPROVED | 2026-11-24 | LAEV's explicit instruction in the project conversation: “Necesito todos los wp como aprobados no completados o aceptados los ocupo aprobados”. Formalized in `docs/phase-0/ERX-PHASE-0-WORK-PACKAGE-APPROVAL-RECORD-001.md`. |
| Independent Technical Review | To be assigned | NOT_ASSIGNED / NOT CLAIMED | — | No independent review is represented as performed. |

This approval authorizes the defined scope and planned deliverables of each work package, subject to the dependency sequence and execution controls in this Workplan. It does not mark unexecuted work as completed, accepted, verified, or independently reviewed.

LAEV approved the scope and planned deliverables of WP-0.1 through WP-0.12 on 2026-11-24, as recorded in ERX-PHASE-0-WORK-PACKAGE-APPROVAL-RECORD-001. This approval does not declare every WP executed or completed, does not waive dependency gates, does not close Phase 0, and does not authorize Phase 1.

---
**End of WORKPLAN-PHASE-0 — ERX byLAEV**
