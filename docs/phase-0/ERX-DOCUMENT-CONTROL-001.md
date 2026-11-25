# ERX-DOCUMENT-CONTROL-001
## Document Identification and Control — Phase 0 / WP-0.4

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-CONTROL-001 |
| Version | 0.2.0 |
| Status | PREPARATORY WORKING DRAFT — NOT APPROVED |
| Work Package | WP-0.4 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and approval authority | LAEV |
| Date | 2026-11-24 |
| Dependencies | WP-0.1 approved; WP-0.3 formal approval pending |

## 1. Purpose

This draft prepares a document identification and control system for ERX. It proposes document identifiers, naming rules, version conventions, lifecycle statuses, minimum metadata, authorship and approval records, modification history, and cross-reference practices.

This document is preparatory only. The Workplan defines WP-0.4 as dependent on WP-0.3. Since WP-0.3 remains blocked pending completion and acceptance of WP-0.2, this draft does not initiate formal WP-0.4 execution, establish an approved control policy, or authorize retrospective alteration of existing source documents.

## 2. Control Principles

1. Every controlled document has one persistent identifier.
2. A document identifier identifies the document across versions; the version identifies a particular revision.
3. Original source files retain their supplied names and bytes. Repository display names or catalog labels do not replace original provenance.
4. A new revision is a new controlled version; historical versions remain recoverable.
5. Publication or a Git commit is not approval.
6. Approval must be explicit, attributable, scoped to a specific version, and recorded.
7. Missing metadata is recorded as NOT_STATED or NOT_VERIFIED, never guessed.
8. Derivative documents identify the exact source versions used.
9. Superseded and withdrawn documents remain in the historical record.
10. Control rules are applied prospectively unless an approved migration decision specifies otherwise.

## 3. Proposed ERX Identifier Structure

Proposed pattern:

`ERX-[DOCUMENT-FAMILY]-[SEQUENCE]`

Examples:
- `ERX-PHASE-0-CHARTER-001`
- `ERX-DOCUMENT-GOVERNANCE-001`
- `ERX-DOCUMENT-CONTROL-001`

Where an existing foundational document has a distinct established identifier, preserve it exactly. Do not rename source identifiers merely to make them fit this proposed pattern. UTXO-911-001 remains UTXO-911-001 unless LAEV approves a formal identifier migration.

### 3.1 Identifier allocation

- Identifiers are unique and never reused.
- Allocate an identifier when a document enters controlled drafting.
- Record reserved identifiers to prevent collisions.
- Do not encode version, status, author, date, or repository branch into the persistent identifier.
- A correction to an identifier is recorded as a controlled metadata correction; the original value remains in history.

## 4. Proposed File Naming Convention

For controlled Markdown documents:

`[DOCUMENT-ID].md`

For a versioned export or external distribution copy, the version may be appended to the exported filename, but the canonical repository filename should remain stable unless a specific archival rule requires preserving the original filename.

Original supplied files retain their exact supplied filenames in the original-source archive. Their internal document identifiers and versions are metadata, not replacement filenames.

Avoid ambiguous names such as `final.md`, `final-final.md`, `latest.pdf`, or filenames containing approval claims that are not recorded in the control metadata.

## 5. Proposed Versioning Convention

Use semantic document versions `MAJOR.MINOR.PATCH`:

| Component | Proposed meaning | Example |
|---|---|---|
| MAJOR | Approved change to purpose, scope, normative meaning, or structure that is not backward-compatible | 1.0.0 → 2.0.0 |
| MINOR | Approved substantive addition or revision that preserves the document's overall compatibility | 1.0.0 → 1.1.0 |
| PATCH | Editorial correction, formatting, metadata correction, or clarification that does not change substantive meaning | 1.0.0 → 1.0.1 |

Drafts may use 0.x.y while under development. Moving to 1.0.0 requires the applicable approval. This proposal does not retroactively assign new versions to existing foundational sources.

The exact version increment for a given change must be justified in the change record; version numbers must not be used to imply approval.

## 6. Proposed Document Lifecycle Statuses

| Status | Meaning | Control condition |
|---|---|---|
| DRAFT | Work in progress | Not approved; may change under draft control |
| IN_REVIEW | Submitted for a defined review | Review scope and reviewer recorded |
| APPROVED | Explicitly approved version | Approval record identifies authority, version, and date |
| REJECTED | Reviewed but not accepted | Review outcome and reasons recorded |
| SUPERSEDED | Replaced by a later approved version or formally substituted document | Replacement reference required |
| WITHDRAWN | Formally withdrawn from use without a direct replacement | Withdrawal authority and reason required |
| ARCHIVED | Preserved for historical/reference purposes | Must not be presented as current |
| NOT_VERIFIED | Status or provenance cannot yet be established | Uncertainty explicitly retained |

A document's lifecycle status is distinct from a work package's execution status. For example, an APPROVED Charter does not mean all activities in its work package or phase are COMPLETED.

## 7. Required Document Metadata

Proposed minimum metadata:

| Field | Required | Description |
|---|---|---|
| Document title | Yes | Full descriptive title |
| Document ID | Yes, when controlled | Persistent unique identifier |
| Version | Yes, when controlled | Exact revision |
| Document status | Yes | Lifecycle status from Section 6 |
| Project/system | Yes | ERX byLAEV / ERX-911-System-byLAEV |
| Work package / phase | Where applicable | Governing work package |
| Language | Yes | Language of this artifact |
| Authorship | Yes | Person or organization responsible for content |
| Design authority | Where applicable | Authority responsible for design decisions |
| Reviewer | When reviewed | Named reviewer or review body |
| Approver | When approved | Explicit approving authority |
| Approval date | When approved | Date of approval |
| Creation date | Yes | Initial creation date |
| Last modified date | Yes | Date of latest revision |
| Source/provenance | Yes | Original source, request, or derivation |
| Related documents | Where applicable | Exact IDs and versions |
| Repository path | For repository-controlled documents | Canonical path |
| Integrity hash | For immutable source/archive artifacts | Algorithm and digest |
| Change summary | For revisions | Material changes in this version |

If a field is unknown, record `NOT_STATED`, `NOT_VERIFIED`, or `NOT_APPLICABLE` as appropriate. Do not fabricate values.

## 8. Authorship, Review, and Approval Records

Authorship, design authority, review, and approval are separate roles and must not be conflated.

Minimum approval record:

- Document ID and exact version.
- Approval decision: APPROVED or REJECTED.
- Approving authority.
- Approval date and time zone where relevant.
- Scope of approval.
- Conditions or reservations, if any.
- Evidence reference (explicit instruction, signed record, or approved decision artifact).

A commit author, GitHub account, file uploader, or automated workflow is not by itself evidence of substantive authorship or approval.

## 9. Modification History

Every controlled document must maintain a revision history:

| Version | Date | Change summary | Author | Reviewer | Approval reference | Status |
|---|---|---|---|---|---|---|
| 0.1.0 | 2026-11-23 | Initial preparatory draft | LAEV / byLAEV project documentation | NOT_RECORDED | NOT_APPROVED | DRAFT |

For subsequent changes, add a new row; do not erase previous history. Link substantive changes to the relevant issue, ADR, review, or approval record.

## 10. Cross-References

Cross-references must use:
- Exact document identifier.
- Exact version, if known.
- Section, page, diagram, or requirement identifier where available.
- Relationship type (based on, specifies, illustrates, responds to, supersedes, or depends on).
- Link to the canonical repository path when available.

Do not cite a document by filename alone where an internal identifier is known. If version is not stated or not verified, say so.

## 11. Proposed Document Header Template

```markdown
# [DOCUMENT-ID]
## [Full document title]

| Field | Value |
|---|---|
| Document ID | [DOCUMENT-ID] |
| Version | [MAJOR.MINOR.PATCH] |
| Status | DRAFT |
| Project | ERX byLAEV |
| Phase / Work Package | [PHASE / WP] |
| Language | [LANGUAGE] |
| Authorship | [AUTHOR] |
| Design authority | [AUTHORITY / NOT_APPLICABLE] |
| Reviewer | [REVIEWER / NOT_RECORDED] |
| Approver | [APPROVER / NOT_APPROVED] |
| Creation date | [YYYY-MM-DD] |
| Last modified | [YYYY-MM-DD] |
| Sources | [DOCUMENT IDs AND VERSIONS] |
| Repository path | [PATH] |

## Revision History

| Version | Date | Change | Author | Review / Approval |
|---|---|---|---|---|
| 0.1.0 | [DATE] | Initial draft | [AUTHOR] | NOT_APPROVED |
```

This template is illustrative until WP-0.4 is formally executed and approved. Existing approved documents must not be silently rewritten to conform to it.

## 12. Migration and Existing Documents

The initial application must preserve current evidence:

- The Phase 0 Charter remains `ERX-PHASE-0-CHARTER-001`, version 1.0.0, APPROVED, with its existing express approval record.
- The Workplan remains `ERX-WP-PHASE-0-001`, currently version 1.0.5, DRAFT / PENDING APPROVAL. Its current version does not mean the Workplan itself is approved.
- `ERX-DOCUMENT-GOVERNANCE-001` is currently version 0.3.0, WORKING DRAFT — PENDING LAEV APPROVAL.
- `ERX-FOUNDATIONAL-MATERIAL-REGISTER-001` records the five-source baseline accepted by LAEV under WP-0.2 on 2026-11-23; supplemental candidate discovery remains separately tracked and does not retroactively alter the accepted baseline.
- `ERX-WP-0.3-EXECUTION-RECORD-001` is currently v0.5.0, IN_PROGRESS; WP-0.3 has not been approved.
- The provisional master index is currently v0.9.0 and remains NOT APPROVED because its formal dependencies are incomplete.
- Original source document IDs, filenames, versions, and hashes are preserved as recorded; unresolved metadata remains visible.

This list reflects the repository records inspected while preparing this draft and must be rechecked during formal WP-0.4 execution.

## 13. Open Decisions for Formal Review

1. Confirm whether the proposed identifier pattern applies to all new ERX documents or only governance/development artifacts.
2. Confirm whether semantic versioning is appropriate for all document classes, including immutable source records and registers.
3. Approve the canonical lifecycle statuses and distinguish them from work package statuses.
4. Confirm the minimum mandatory metadata by document class.
5. Define who may review and approve each class of document.
6. Define whether the canonical Markdown filename remains stable across versions and how released snapshots are archived.
7. Define hash algorithms and storage location for integrity metadata.
8. Approve the document header template.
9. Define a controlled migration approach for existing documents, without rewriting their original provenance.

No option in this list is considered approved by publication of this draft.

## 14. WP-0.4 Status and Acceptance

**Status: BLOCKED — PREPARATORY DRAFT ONLY.**

This document is prepared to reduce future drafting work and expose policy decisions for review. It does not satisfy formal WP-0.4 execution or acceptance.

Formal WP-0.4 may begin only after:
1. WP-0.3 has completed and its hierarchy/governance document has been expressly approved.
2. The document classes and subject-matter authority rules are sufficiently stable.
3. The identifier, naming, versioning, status, metadata, authorship, approval, history, and cross-reference proposals are reviewed.
4. LAEV expressly approves the final WP-0.4 document and template.

**This draft does not approve a document-control policy, close WP-0.2 or WP-0.3, change the status of the Workplan, or authorize Phase 1.**

---
End of ERX-DOCUMENT-CONTROL-001
