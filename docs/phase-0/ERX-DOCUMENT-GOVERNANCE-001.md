# ERX-DOCUMENT-GOVERNANCE-001
## Document Organization and Hierarchy — Phase 0 / WP-0.3

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-GOVERNANCE-001 |
| Version | 0.1.0 |
| Status | WORKING DRAFT — NOT APPROVED |
| Work Package | WP-0.3 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design authority | LAEV |
| Basis | Five supplied foundational PDFs inspected; initial WP-0.2 register |
| Date | 2026-11-23 |

## 1. Purpose

This document proposes a controlled organization and hierarchy for ERX project documents. It distinguishes original sources from development artifacts, assigns provisional subject-matter roles, records known relationships, and defines how contradictions and document evolution are to be handled.

This is a preparatory draft only. WP-0.2 remains IN_PROGRESS and its source inventory has not been approved. Consequently, this document does not establish a final or approved hierarchy, does not supersede any source, and does not resolve any technical or normative conflict.

## 2. Governing Principles

1. **Source preservation:** an original source remains unchanged. Corrections, translations, extracts, and revisions are derivative artifacts.
2. **Traceability:** every derivative must identify the sources on which it relies.
3. **No silent reconciliation:** inconsistent statements are recorded as issues; they are not harmonized by editorial assumption.
4. **Subject-matter authority:** authority is determined by the subject explicitly covered by a document, not merely by its date, file name, or position in a directory.
5. **Explicit approval:** publication, a Git commit, or a draft status does not constitute approval.
6. **Version awareness:** references must identify the exact document version wherever known.
7. **Preservation of history:** superseded documents remain discoverable and must not be overwritten as if they had never existed.
8. **Uncertainty visibility:** missing sources, unverified versions, and unresolved decisions remain explicitly marked.

## 3. Document Classes

| Class | Definition | Examples in current source set |
|---|---|---|
| Foundational source | Original design, protocol, functional, or planning document supplied as a source | ERX-PROT-001; ERX-ATLAS-001; UTXO-911-001; ERX-ROADMAP-001 |
| Technical response / review | A response, assessment, or observation concerning another document | Technical Response to ERX-ROADMAP-001 |
| Governance artifact | Charter, workplan, policy, register, approval, or closure record governing project work | ERX-PHASE-0-CHARTER-001; WORKPLAN-PHASE-0; foundational register |
| Development specification | A new or revised technical specification created during controlled development | Future ERX component specifications |
| Verification artifact | Test plan, test result, audit evidence, validation report, or independent review | Future verification reports |
| Implementation artifact | Source code, configuration, build, release, or deployment material | Future software repository contents |

Classification is provisional until WP-0.2 is complete and the relevant documents have been verified.

## 4. Provisional Document Hierarchy

The following hierarchy is proposed as an organizational model. It is not an automatic precedence rule and does not grant one document authority over all subjects.

### Level A — Project mandate and governance

- Approved Phase 0 Charter.
- Approved project governance and authority decisions.
- Approved workplan and formally approved changes to it.

These artifacts govern project scope, process, responsibility, and approval. They do not independently redefine the technical behavior of the ERX protocol.

### Level B — Foundational technical and planning sources

- ERX-PROT-001 v1.1 — institutional protocol specification.
- ERX-ATLAS-001 v1.1 — graphical representation explicitly related to ERX-PROT-001 v1.1.
- UTXO-911-001 v1.0 — conceptual and functional specification of the three-stage 911 communication UTXO cycle.
- ERX-ROADMAP-001 v1.0 — development, implementation, and institutional homologation plan.
- Technical Response to the Observations on ERX-ROADMAP-001 — technical and management response.

These documents retain their individual scopes. Their inclusion in one level does not imply that they are interchangeable or that all have the same normative force.

### Level C — Controlled development documents

- Detailed requirements and traceability matrices.
- Architecture decision records.
- Detailed protocol and component specifications.
- Interface and data specifications.
- Security and privacy specifications.
- Operational procedures.

These documents must cite the source requirements and decisions they elaborate. They may not silently alter an approved foundational rule.

### Level D — Verification and implementation evidence

- Test plans and test cases.
- Test results and validation reports.
- Code, configuration, build and release records.
- Audit and integrity evidence.
- Deployment and operational evidence, when later authorized.

Evidence demonstrates implementation or verification results; it does not amend a protocol specification by itself.

## 5. Provisional Subject-Matter Authority Matrix

| Subject | Primary source / proposed authority | Supporting source | Boundary / unresolved point |
|---|---|---|---|
| Institutional 911 communication protocol | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Detailed interpretation must be traced to exact sections and diagrams. |
| Graphical flow and operational representation | ERX-ATLAS-001 v1.1 | ERX-PROT-001 v1.1 | The Atlas is a representation; a diagram must not silently override protocol text. |
| Three-stage UTXO communication cycle | UTXO-911-001 v1.0 | ERX-PROT-001 v1.1 | Exact alignment and any differences require a section-by-section comparison. |
| Development phase sequence and gates | ERX-ROADMAP-001 v1.0 | Technical Response to the Roadmap | Changes require a recorded decision and versioned Roadmap revision. |
| Technical observations on Roadmap | Technical Response to the Observations on ERX-ROADMAP-001 | ERX-ROADMAP-001 v1.0 | It is a response, not an automatic replacement for the Roadmap. |
| Consensus architecture | ERX-CONSENSUS-001 v0.1 (cited, not located) | ERX-ROADMAP-001 v1.0 | Authority and contents cannot be assessed until the source is recovered. |
| Institutional implementation proposal | ERX-IMPL-PROPOSAL-001 (cited, not located) | ERX-ROADMAP-001 v1.0 | Authority and contents cannot be assessed until the source is recovered. |
| Project governance and approval | Approved ERX Phase 0 governance artifacts | Workplan and decision records | The Phase 0 Charter is approved; the Workplan itself remains pending approval. |

This matrix is provisional. “Primary source” means the source most directly assigned to the subject in this working model; it does not establish a legally binding precedence rule.

## 6. Known Document Relationships

- ERX-ATLAS-001 v1.1 explicitly identifies ERX-PROT-001 v1.1 as its related normative document.
- ERX-ROADMAP-001 v1.0 identifies ERX-PROT-001 v1.1, ERX-ATLAS-001 v1.1, UTXO-911-001 v1.0, ERX-CONSENSUS-001 v0.1, and ERX-IMPL-PROPOSAL-001 as foundational references.
- The Technical Response addresses observations and risks associated with ERX-ROADMAP-001 and recommends retaining its development sequence while incorporating observations as implementation and validation requirements.
- The Phase 0 Charter authorizes the governance and preparation work of Phase 0; it does not authorize operational implementation of ERX.

These relationships are based on the supplied documents' opening/control information and inspected content. A complete cross-reference map requires full-document review and section-level citations.

## 7. Contradiction and Ambiguity Handling

Every suspected contradiction must be recorded before any resolution is proposed.

Minimum issue record:

| Field | Required content |
|---|---|
| Issue ID | Unique ERX issue identifier |
| Sources | Exact document IDs, versions, sections/pages/diagram IDs |
| Statements | Concise description or quotation of each conflicting statement |
| Issue type | Contradiction, ambiguity, omission, outdated reference, or version mismatch |
| Impact | Protocol, architecture, safety, privacy, security, institutional, implementation, or documentary impact |
| Interim treatment | Whether work must stop, proceed with a documented assumption, or remain unaffected |
| Owner | Person responsible for analysis |
| Options | Viable interpretations or resolutions |
| Decision authority | Authority empowered to approve the resolution |
| Status | OPEN, UNDER_REVIEW, DECIDED, or DEFERRED |
| Evidence | ADR, approved amendment, review, or other disposition record |

No source is considered amended merely because a later document describes it differently. A conflict is resolved only through an explicit, traceable decision by the designated authority and, where necessary, a new version or amendment of the affected document.

## 8. Document Evolution Rules

1. Assign a unique document identifier before controlled publication.
2. Preserve the original supplied file and record its checksum.
3. Create revisions as new versions; do not replace the historical source artifact.
4. Record change rationale, affected sections, source references, author, reviewer, approver, and date.
5. Mark a document DRAFT, IN_REVIEW, APPROVED, SUPERSEDED, or WITHDRAWN only under the project's approved document-control policy.
6. A derivative document must list the exact source versions used.
7. A superseding document must identify the version it replaces and explain the change.
8. A translation is a derivative; it does not silently replace the original-language source.
9. Keep unresolved conflicts and missing-source references visible.
10. Update the master index and cross-reference records when a document is created, revised, approved, superseded, or withdrawn.

The detailed identifier, metadata, and versioning rules are assigned to WP-0.4 and WP-0.11 and remain subject to their approval.

## 9. Open Items and Preconditions

- WP-0.2 has not been completed or approved.
- The five source PDFs have been inspected, but their original binary files have not yet been archived in the GitHub repository and post-commit hashes have not been verified.
- ERX-CONSENSUS-001 v0.1 has not been located.
- ERX-IMPL-PROPOSAL-001 has not been located.
- Full section-by-section comparison among ERX-PROT-001, ERX-ATLAS-001, and UTXO-911-001 remains outstanding.
- The formal document hierarchy and subject-matter authority matrix have not been approved.
- The technical response's formal identifier and version remain unstated in the supplied source.

## 10. Preliminary Issue Register

The preparatory issue inventory is recorded in [`ERX-DOCUMENT-ISSUE-REGISTER-001.md`](ERX-DOCUMENT-ISSUE-REGISTER-001.md) and [`registers/document-issue-register.csv`](../../registers/document-issue-register.csv). It records open metadata, missing-source, authority, diagram interpretation, response-effect, and archive-integrity matters. These entries are not adjudicated contradictions and remain open pending WP-0.2 acceptance and formal WP-0.3 execution.

## 11. WP-0.3 Status and Acceptance

**Status: BLOCKED — PREPARATORY DRAFT ONLY.**

This draft has been prepared to make the next work package reviewable and to identify the hierarchy questions that must be decided. Formal WP-0.3 execution and approval remain dependent on completion and acceptance of WP-0.2.

WP-0.3 may be submitted for formal review only after:
1. WP-0.2 source inventory is completed and reviewed.
2. Original source preservation and integrity evidence are addressed or formally dispositioned.
3. Referenced but missing documents are located or formally recorded as unavailable with an approved treatment.
4. The subject-matter matrix and document relationships are checked against the complete source set.
5. All material contradictions and ambiguities are entered in a traceable issue register.

**This document is not approved. It does not close WP-0.2, start formal WP-0.3 execution, approve a document hierarchy, or authorize Phase 1.**

---
End of ERX-DOCUMENT-GOVERNANCE-001
