# ERX-DOCUMENT-CONTROL-001
## Document Identification and Control — Phase 0 / WP-0.4

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-CONTROL-001 |
| Version | 0.3.1 |
| Status | IN_REVIEW — WORKING PROPOSAL; NOT APPROVED |
| Work Package | WP-0.4 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and approval authority | LAEV |
| Preparation date | 2026-11-24 |
| Dependencies | WP-0.1 APPROVED; WP-0.3 COMPLETED / ACCEPTED |
| Supersedes | Preparatory draft v0.2.0 for this controlled working line; no approved policy superseded |

## 1. Purpose and scope

This document develops the document identification and control policy required by WP-0.4. It operationalizes, without redefining, the hierarchy, subject-matter authority, contradiction handling, and evolution/supersession rules accepted under WP-0.3.

The scope covers:
1. Persistent document identifiers and allocation.
2. Canonical repository filenames.
3. Document versioning.
4. Document lifecycle statuses and transitions.
5. Required metadata by document class.
6. Authorship, design authority, review, and approval records.
7. Revision history and change records.
8. Cross-reference and source provenance rules.
9. Controlled onboarding of existing repository documents.

Out of scope: repository access controls and branch strategy (WP-0.5); final master index acceptance (WP-0.6); requirements definition (WP-0.7); ADR governance (WP-0.8); full project-wide change control (WP-0.11); implementation, deployment, institutional operation, or Phase 1 authorization.

## 2. Governing principles

1. Preserve supplied source files byte-for-byte and preserve their supplied filenames.
2. A persistent document ID identifies the document; a version identifies a specific revision.
3. IDs are unique, stable, and never reused.
4. A Git commit, publication, upload, or automated check is not substantive approval.
5. Approval must identify the exact document ID and version, authority, date, scope, conditions, and evidence.
6. Authorship, design authority, reviewer, approver, and repository contributor are distinct roles.
7. Unknown information is explicitly recorded as NOT_STATED, NOT_VERIFIED, NOT_RECORDED, or NOT_APPLICABLE; it is never inferred.
8. Derivative documents cite exact source IDs and versions wherever known.
9. Superseded, rejected, and withdrawn versions remain retrievable as historical records.
10. Apply the control policy prospectively. Existing records are migrated by metadata reconciliation, not silent rewriting.
11. WP-0.3's scoped subject-matter authority remains controlling; this policy does not create universal precedence.
12. A register entry is not a substitute for the controlled document or its approval evidence.

## 3. Persistent document identification

### 3.1 Proposed identifier pattern

For newly controlled ERX documents without an established identifier:

`ERX-[DOCUMENT-FAMILY]-[SEQUENCE]`

Examples: `ERX-PHASE-0-CHARTER-001`, `ERX-DOCUMENT-CONTROL-001`, `ERX-REQUIREMENTS-BASELINE-001`.

Rules:
- Use uppercase ASCII letters, numerals, and hyphens.
- Use a meaningful, stable family token; avoid embedding mutable status, version, date, author, branch, or phase progress in the ID.
- Sequence is three digits initially and expands only when needed; sequence is unique within the family.
- Reserve/allocate an ID in the document register before controlled drafting.
- Never recycle an ID, including after rejection or withdrawal.
- Record allocation date, allocator, title, family, and current status.
- An ID correction requires a recorded metadata correction and a permanent old-to-new alias; it must not erase the original identifier.

### 3.2 Existing identifiers and exceptions

Existing source IDs remain unchanged. In particular, preserve `ERX-PROT-001`, `ERX-ATLAS-001`, `UTXO-911-001`, and `ERX-ROADMAP-001`. Do not force legacy IDs into the proposed pattern. A source without a stated internal ID is recorded as NOT_STATED; a catalogue ID may be assigned separately and must be labelled catalogue-only.

### 3.3 ID and version are separate

The canonical identity is the pair (Document ID, Version). A document's ID persists across its revisions. A different document with a different purpose receives a different ID, even if it replaces or supersedes another document.

## 4. Canonical file naming

Proposed rule for newly controlled native Markdown documents:

`[DOCUMENT-ID].md`

Rules:
- Keep one stable canonical path/name for the current document line; version is recorded in document metadata, not routinely embedded in the canonical filename.
- Preserve supplied source filenames in the archive.
- Exported snapshots may include version in the export filename, e.g. `ERX-DOCUMENT-CONTROL-001-v1.0.0.pdf`, but the export must identify its canonical source and version.
- Avoid mutable labels such as `final`, `latest`, `new`, or `final-final`.
- Renaming a canonical path is a controlled metadata/path change: record old path, new path, date, reason, and commit; preserve links or redirects where feasible.
- File extension reflects actual format; a filename does not establish approval.

## 5. Document versioning

### 5.1 Proposed semantic format

Use `MAJOR.MINOR.PATCH` for controlled revisions.

| Component | Increment when |
|---|---|
| MAJOR | Approved change to purpose, scope, normative meaning, interfaces, or structure that is materially incompatible with the previous approved baseline |
| MINOR | Approved substantive addition or revision that preserves the prior baseline's essential compatibility |
| PATCH | Editorial, formatting, or metadata correction that does not change substantive meaning |

Examples: `1.0.0 → 2.0.0`; `1.0.0 → 1.1.0`; `1.0.0 → 1.0.1`.

### 5.2 Draft versions and release baseline

- Working drafts use `0.x.y`.
- The first formally approved baseline is `1.0.0), unless the approving decision explicitly records another starting point.
- A new draft derived from an approved baseline increments the appropriate component and remains unapproved until expressly accepted.
- A version increment does not itself indicate approval.
- Version changes require a short rationale in the revision history/change record.
- Do not retroactively renumber foundational originals or their source-stated versions.
- Registers may use the same version syntax, but a register's version tracks its own content revision, not the versions of records listed inside it.

## 6. Document lifecycle statuses

These statuses apply to documents, not work packages.

| Status | Meaning | Minimum control |
|---|---|---|
| DRAFT | Being prepared; not submitted for formal review | Author and current version identified |
| IN_REVIEW | Submitted for a defined review | Review scope, reviewer, and submission version recorded |
| APPROVED | Exact version expressly accepted by competent authority | Approval record required |
| REJECTED | Reviewed and not accepted | Decision, rationale, and review evidence retained |
| SUPERSEDED | Replaced within an expressly defined scope | Replacement ID/version and supersession decision required |
| WITHDRAWN | Removed from current use without direct replacement | Authority, reason, effective date, and impact recorded |
| ARCHIVED | Retained for reference/history; not represented as current | Archive location and provenance retained |
| ARCHIVED | Historical copy retained and not represented as the current working copy | Archive location and provenance retained; prior lifecycle status preserved in history |

Transition controls:
- DRAFT → IN_REVIEW: author submits a specific immutable review candidate.
- IN_REVIEW → APPROVED or REJECTED: competent authority records an explicit decision against that exact version.
- APPROVED → SUPERSEDED or WITHDRAWN: requires a separate controlled decision; approval history is retained.
- Any lifecycle status may acquire an archival-copy record; archiving does not replace or erase the document's lifecycle status.
- Evidence verification is tracked separately from lifecycle status using values such as VERIFIED, NOT_VERIFIED, NOT_LOCATED, or NOT_ASSESSED. These values describe evidence, not approval or document lifecycle.
- Revisions to an approved document create a new draft version; they do not mutate the approved baseline in place.

## 7. Required metadata by document class

### 7.1 Controlled document header

Mandatory fields for new controlled documents:
- Document ID.
- Title.
- Version.
- Lifecycle status.
- Project/system.
- Document class.
- Language.
- Authorship / responsible author.
- Creation date.
- Last modified date.
- Phase/work package, where applicable.
- Design authority, where applicable.
- Reviewer and review date, when reviewed.
- Approver and approval date, when approved.
- Source/provenance.
- Canonical repository path.
- Revision history.

Conditional fields:
- Related documents and exact versions.
- Approval scope, conditions, and evidence reference.
- Integrity algorithm and digest for immutable source/archive artifacts.
- Confidentiality/access classification, once governed by the applicable security/privacy work.
- Effective date, expiry/review date, and distribution record where relevant.

### 7.2 Metadata exceptions

- Foundational source: preserve source-native title, ID, version, date, and filename; catalogue-only fields must be clearly labelled.
- Derivative specification: cite each source ID/version and identify the derivation relationship.
- Register: include register ID/version/status and stable record keys; individual entries retain their own lifecycle state.
- Code/configuration/test artifact: identify repository path, commit or release reference, artifact version where applicable, and related requirement/specification; code commit is not document approval.
- Missing value: use NOT_STATED (source does not state it), NOT_VERIFIED (not verified), NOT_RECORDED (record not yet created), or NOT_APPLICABLE (does not apply). Do not use blank cells where the distinction matters.

## 8. Authorship, review, and approval

These roles must be recorded separately:
- **Author:** responsible for preparing the content.
- **Design authority:** responsible for design decisions within an assigned subject.
- **Reviewer:** evaluates the submitted version against a stated scope/criteria. For substantive technical or normative changes, the reviewer must be independent of the author; any exception requires explicit justification and approval by the competent authority.
- **Approver:** exercises the formal authority to accept or reject that exact version.
- **Repository contributor:** account/person that commits or uploads content; this role alone does not prove authorship or approval.

Minimum review record:
1. Document ID and exact version/hash or immutable commit reference.
2. Review scope and criteria.
3. Reviewer identity and review date.
4. Findings, required corrections, and disposition.
5. Review outcome: accepted for approval, changes required, or rejected.

Minimum approval record:
1. Document ID and exact version.
2. Decision: APPROVED or REJECTED.
3. Approving authority and authority basis.
4. Date/time and time zone where relevant.
5. Scope of approval.
6. Conditions/reservations.
7. Evidence reference (explicit decision record, signed record, or attributable approval instruction).
8. Effective date, if different from approval date.

A PR merge or green CI check is supporting publication/verification evidence only, not approval.

## 9. Revision history and change traceability

Each controlled document maintains an append-only revision history:

| Version | Date | Change class | Summary | Author | Reviewer | Approval reference | Status |
|---|---|---|---|---|---|---|---|
| 0.3.0 | 2026-11-24 | Consolidation / substantive draft | Reconciled preparatory draft with WP-0.3 accepted governance and opened WP-0.4 review | Project drafting record | NOT_RECORDED | NOT_APPROVED | HISTORICAL_DRAFT |
| 0.3.1 | 2026-11-24 | Technical clarification / metadata correction | Separated lifecycle status from evidence verification and archival-copy tracking; clarified draft version progression and independent review | Project drafting record | NOT_RECORDED | NOT_APPROVED | IN_REVIEW |

Every material change also links to a change record containing:
- Change ID.
- Affected document ID/version and exact sections.
- Change class (editorial, metadata, clarification, technical, normative, or supersession).
- Reason and source/evidence.
- Impact/dependency analysis.
- Alternatives considered, where material.
- Compatibility/migration effect.
- Author, reviewer, decision authority, outcome.
- New version/effective date and repository commit.
- Prior version retrieval location.

The detailed project-wide change workflow remains within WP-0.11. This section defines the minimum document-level traceability needed for WP-0.4.

## 10. Cross-reference and provenance rules

A controlled reference should state:
- Exact document ID.
- Exact version, if known.
- Section, clause, page, plate, requirement, or record key where available.
- Relationship type: based on, specifies, illustrates, responds to, supersedes, depends on, or records.
- Canonical repository path/link, where available.
- Verification qualifier if the source identity/version is uncertain.

Rules:
- Do not cite filename alone where a document ID is known.
- Do not silently upgrade a proposal or response to normative authority.
- Preserve distinctions established by WP-0.3 between textual protocol, graphical representation, functional source, planning source, and supporting response.
- Cross-reference changes are updated in the relevant register/index when those packages are formally active; WP-0.4 does not claim to complete WP-0.6.

## 11. Controlled header template

```markdown
# [DOCUMENT-ID]
## [Document title]

| Field | Value |
|---|---|
| Document ID | [DOCUMENT-ID] |
| Version | [MAJOR.MINOR.PATCH] |
| Status | DRAFT |
| Project/system | ERX byLAEV |
| Document class | [CLASS] |
| Phase / Work Package | [PHASE / WP / NOT_APPLICABLE] |
| Language | [LANGUAGE] |
| Authorship | [AUTHOR / NOT_RECORDED] |
| Design authority | [AUTHORITY / NOT_APPLICABLE] |
| Reviewer | [REVIEWER / NOT_RECORDED] |
| Approver | [APPROVER / NOT_APPROVED] |
| Creation date | [YYYY-MM-DD] |
| Last modified | [YYYY-MM-DD] |
| Sources / provenance | [DOCUMENT IDs AND VERSIONS] |
| Canonical repository path | [PATH] |

## Revision History

| Version | Date | Change class / summary | Author | Review / approval |
|---|---|---|---|---|
| 0.1.0 | [DATE] | Initial draft | [AUTHOR] | NOT_APPROVED |
```

This template is proposed for new controlled documents after approval of WP-0.4. It is not a retroactive requirement to rewrite original sources or every existing document.

## 12. Migration and initial application

Migration is a controlled metadata reconciliation, not a blanket rewrite.

1. Preserve the five accepted foundational PDF binaries and their original filenames, source identities, versions, and integrity evidence.
2. Preserve the existing WP-0.3 approval records and document history.
3. For each existing repository artifact, distinguish source-native metadata from catalogue-assigned metadata.
4. Assign or confirm a persistent ID only where the artifact is a controlled ERX document and no established ID exists; record the allocation in the document register.
5. Do not change an existing ID merely to match the new pattern.
6. Record actual version/status from evidence; do not infer approval from a commit, PR, filename, or Workplan checkbox.
7. Mark obsolete or contradictory metadata for controlled correction; retain the previous value in the correction history.
8. Migrate documents in batches with a reconciliation report and exception list.
9. Defer the authoritative master-index consolidation to WP-0.6.
10. Do not silently rewrite old headers. Apply the approved template prospectively; retrospective metadata additions require a traceable metadata-only change and must not alter source content.

### 12.1 Known migration exceptions

- ERX-ATLAS-001: supplied filename says “v1” while the internal source identifies v1.1; preserve both facts.
- Technical Response to ERX-ROADMAP-001: source-native ID/version/date are NOT_STATED in the inspected source; any catalogue key is catalogue-only.
- ERX-CONSENSUS-001 v0.1: retain proposal-for-review status; document control does not approve its operational consensus rules.
- ERX-IMPL-PROPOSAL-001: retain NOT_LOCATED / UNVERIFIED until the source is obtained or a separate approved disposition is made.
- Workplan and master index statuses/versions must be taken from their actual controlled records and reconciled in their own work packages.

## 13. Open decisions for LAEV review

The following are proposals, not approved policy until LAEV expressly decides:

- **DC-01:** Adopt the proposed ERX identifier pattern for new ERX-controlled documents, while preserving all established source IDs and recording catalogue-only IDs separately.
- **DC-02:** Adopt stable canonical filenames `[DOCUMENT-ID].md`; keep versions in document metadata and exported snapshot filenames only.
- **DC-03:** Adopt MAJOR.MINOR.PATCH versioning, with 0.x.y drafts and 1.0.0 as the first approved baseline.
- **DC-04:** Adopt the lifecycle status set and transition controls in Section 6.
- **DC-05:** Adopt the mandatory metadata set in Section 7, including explicit unknown-value tokens.
- **DC-06:** Adopt the separation of author, design authority, reviewer, approver, and repository contributor.
- **DC-07:** Require an exact-version review and approval record; a commit, merge, or CI result is not approval.
- **DC-08:** Adopt append-only revision/change history and the cross-reference rules.
- **DC-09:** Adopt prospective migration, preserving source originals and provenance; defer full master index acceptance to WP-0.6.

LAEV may accept, reject, or amend each proposal. No proposal becomes approved merely by inclusion in this draft.

## 14. WP-0.4 execution and acceptance

**Current status: IN_REVIEW — WP-0.4 EXECUTION OPEN; POLICY NOT APPROVED.**

Activities 0.4.1–0.4.9 are developed in this candidate but remain subject to LAEV review and evidence completion.

Acceptance requires:
1. A unique, non-reusable identifier rule and allocation method.
2. A canonical naming rule that preserves original filenames/provenance.
3. Defined version increments and draft/release boundary.
4. Document lifecycle statuses and controlled transitions distinct from work-package statuses.
5. Required metadata by document class, including explicit treatment of unknowns.
6. Separate authorship, design, review, and approval records.
7. Reconstructable revision history and change traceability.
8. Exact, versioned cross-references and provenance rules.
9. A migration plan that preserves original sources and does not imply retrospective approval.
10. LAEV's express decision on DC-01–DC-09 and a final approved v1.0.0 or other explicitly authorized baseline.
11. Updated execution/completion evidence and document register.

**Boundary:** WP-0.4 approval will not complete WP-0.5, WP-0.6, the whole Phase 0, or authorize Phase 1, implementation, deployment, or institutional operation.

---
End of ERX-DOCUMENT-CONTROL-001
