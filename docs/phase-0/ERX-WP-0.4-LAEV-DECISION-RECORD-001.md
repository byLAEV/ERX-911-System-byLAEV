# ERX-WP-0.4-LAEV-DECISION-RECORD-001
## Formal Disposition of Document-Control Decisions DC-01 through DC-09

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.4-LAEV-DECISION-RECORD-001 |
| Version | 1.2.0 |
| Status | APPROVED — LAEV DECISION RECORDED |
| Work Package | WP-0.4 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Decision authority | LAEV |
| Decision date | 2026-11-24 (Costa Rica, UTC−06:00) |
| Decision evidence | Explicit LAEV instruction in project conversation |
| Decision subject | DC-01 through DC-09; Addendum A and Addendum B clarify review timing |

## 1. Formal decision

LAEV expressly approves DC-01 through DC-09 according to the technical recommendation, retaining all nine proposals and requiring incorporation of the technical corrections in ERX-DOCUMENT-CONTROL-001 v0.3.1.

This record approves the policy choices listed below. It does not, by itself, approve a later document version that has not yet been reviewed and identified in an exact-version approval record.

## 2. Decision register

| Decision | LAEV disposition | Approved rule |
|---|---|---|
| DC-01 | APPROVED | Adopt ERX-[DOCUMENT-FAMILY]-[SEQUENCE] for new controlled ERX documents; preserve established source IDs and label catalogue-only IDs. |
| DC-02 | APPROVED | Use stable canonical filenames [DOCUMENT-ID].md; keep version in document metadata and versioned exports. |
| DC-03 | APPROVED | Adopt MAJOR.MINOR.PATCH; use 0.x.y for drafts and 1.0.0 for the first approved baseline unless an approval decision states otherwise. |
| DC-04 | APPROVED WITH TECHNICAL CLARIFICATION | Adopt document lifecycle states and transitions; keep evidence-verification and archive-custody attributes separate from lifecycle state. |
| DC-05 | APPROVED | Adopt mandatory/conditional metadata by document class and explicit unknown-value tokens. |
| DC-06 | APPROVED | Keep author, design authority, reviewer, approver, and repository contributor as distinct roles. |
| DC-07 | APPROVED | Require review and approval against an exact document version; commits, merges, and CI checks are not substantive approval. |
| DC-08 | APPROVED | Adopt append-only revision/change history and exact-version cross-reference/provenance rules. |
| DC-09 | APPROVED | Adopt prospective migration, preserve original sources and provenance, and defer authoritative master-index acceptance to WP-0.6. |

## 3. Conditions and interpretation

1. The corrections in v0.3.1 are retained: lifecycle status is distinct from evidence verification; archive custody is a preservation attribute; draft progression is explicit; and review/approval roles remain distinct. The timing and nature of independent external review are clarified by Addendum A and superseding Addendum B.
2. Existing foundational documents retain their source-native identifiers, versions, filenames, and original bytes.
3. ERX-ATLAS-001's supplied filename/internal version discrepancy remains visible.
4. The technical response to ERX-ROADMAP-001 retains unstated source-native metadata; no metadata is invented.
5. ERX-CONSENSUS-001 v0.1 remains a proposal for review; this decision does not approve its operational consensus rules.
6. ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED / UNVERIFIED until its source is obtained or separately dispositioned.
7. WP-0.6 remains responsible for authoritative master-index acceptance.

## 4. Approval boundary

This record is the formal approval of the nine policy decisions only. The final consolidated policy document must still be prepared as an exact candidate version, reviewed, and approved by an explicit exact-version approval record. Internal exact-version review and LAEV approval are required for WP-0.4. Independent external review/audit is deferred until after completion of planned project work and is not a WP-0.4 or inter-work-package gate.

This decision does not close WP-0.4, approve WP-0.5, complete Phase 0, or authorize Phase 1, implementation, deployment, or institutional operation.

---
End of ERX-WP-0.4-LAEV-DECISION-RECORD-001


## Addendum A — LAEV clarification on independent review

| Field | Value |
|---|---|
| Addendum date | 2026-11-24 (Costa Rica, UTC−06:00) |
| Decision authority | LAEV |
| Decision evidence | Explicit LAEV instruction in project conversation |
| Effect | Clarifies DC-06 and the WP-0.4 closeout sequence prospectively |

LAEV instructs that an independent reviewer must not be required as a prerequisite to completing WP-0.4 or the planned project work. Independent external review/audit is to take place after the planned project work is completed, under the appropriate later verification/audit activity.

For WP-0.4, the required controls remain: (1) documented internal consistency/technical review of the exact candidate version; (2) disposition of findings; and (3) LAEV's express approval of the exact version. The internal reviewer must be identified truthfully; no claim of independence is made unless supported. This addendum does not remove the reviewer role or the need for exact-version review and approval.

This addendum amends the timing of independent external review only. It does not waive any substantive acceptance criterion, authorize implementation/deployment, or itself close WP-0.4.

---
End of Addendum A


## Addendum B — Superseding clarification of review timing

| Field | Value |
|---|---|
| Addendum date | 2026-11-24 (Costa Rica, UTC−06:00) |
| Decision authority | LAEV |
| Decision evidence | Explicit instruction: “Evita el revisor independiente. Porque un revisor independiente va estar después de terminar todo” |
| Supersedes | Any inconsistent wording in Sections 3.1 and 4 of this decision record and any earlier draft that makes independent external review a WP-0.4 or pre-project-completion prerequisite |

**Binding clarification:** The independent external reviewer/auditor will be engaged after the planned project work is complete. Independent external review is not a prerequisite for closing WP-0.4, beginning WP-0.5, or progressing through the remaining Phase 0 work packages. It is a later assurance activity.

For each work package, the project may perform internal review and consistency checks appropriate to its acceptance criteria. The reviewer must be identified truthfully; internal review must not be labelled independent external review. LAEV retains express approval authority for the exact final document version wherever the work package requires it.

Addendum B supersedes any conflicting wording in the earlier decision record and Addendum A. It does not remove internal review, technical verification, evidence completion, LAEV approval, or any substantive acceptance criterion.

---
End of Addendum B
