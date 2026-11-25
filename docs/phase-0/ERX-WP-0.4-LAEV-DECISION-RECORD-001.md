# ERX-WP-0.4-LAEV-DECISION-RECORD-001
## Formal Disposition of Document-Control Decisions DC-01 through DC-09

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.4-LAEV-DECISION-RECORD-001 |
| Version | 1.0.0 |
| Status | APPROVED — LAEV DECISION RECORDED |
| Work Package | WP-0.4 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Decision authority | LAEV |
| Decision date | 2026-11-24 (Costa Rica, UTC−06:00) |
| Decision evidence | Explicit LAEV instruction in project conversation |
| Decision subject | DC-01 through DC-09 in ERX-DOCUMENT-CONTROL-001 v0.3.1 |

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

1. The corrections in v0.3.1 are retained: lifecycle status is distinct from evidence verification; archive custody is a preservation attribute; draft progression is explicit; and substantive technical/normative review requires reviewer independence from the author unless a justified exception is expressly approved.
2. Existing foundational documents retain their source-native identifiers, versions, filenames, and original bytes.
3. ERX-ATLAS-001's supplied filename/internal version discrepancy remains visible.
4. The technical response to ERX-ROADMAP-001 retains unstated source-native metadata; no metadata is invented.
5. ERX-CONSENSUS-001 v0.1 remains a proposal for review; this decision does not approve its operational consensus rules.
6. ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED / UNVERIFIED until its source is obtained or separately dispositioned.
7. WP-0.6 remains responsible for authoritative master-index acceptance.

## 4. Approval boundary

This record is the formal approval of the nine policy decisions only. The final consolidated policy document must still be prepared as an exact candidate version, reviewed, and approved by an explicit exact-version approval record. The independent-review requirement adopted in DC-06/Section 8 must not be represented as satisfied without evidence.

This decision does not close WP-0.4, approve WP-0.5, complete Phase 0, or authorize Phase 1, implementation, deployment, or institutional operation.

---
End of ERX-WP-0.4-LAEV-DECISION-RECORD-001
