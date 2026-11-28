# ERX-WP-0.7-65-TO-82-SCOPE-RECONCILIATION-001
## Reconciliation of the historical 65-candidate snapshot with the current canonical register

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-65-TO-82-SCOPE-RECONCILIATION-001 |
| Version | 0.1.0 |
| Status | CONTROLLED RECONCILIATION NOTE — SEMANTIC ACCEPTANCE OPEN |
| Date | 2026-11-28 |
| Work Package | WP-0.7 |
| Branch | `wp-0.7-requirements-review` |
| Canonical register | `registers/requirements-traceability.csv` |
| Linked individual register | `registers/requirement-identification-register.csv` |

## 1. Determination

The historical **65-candidate** snapshot is not the current canonical scope. The current branch contains **82 source-candidate records** in the canonical traceability CSV and **107 individually identified records** in the linked individual register.

The 107 records are a decomposition/identification layer linked to the 82 source candidates; they are not 107 additional source requirements. The current semantic-review register explicitly identifies the former 65-candidate scope as stale and prohibits deleting, merging, renumbering or silently superseding IDs.

Accordingly, WP-0.7 must reconcile the historical 65 snapshot **to the controlled 82-candidate register**, rather than roll the canonical register back to 65.

## 2. Verified current source distribution

The current source-coverage audit records the following 82 candidates:

| Source | Candidate records |
|---|---:|
| ERX-PROT-001 v1.1 | 40 |
| ERX-ATLAS-001 v1.1 | 4 |
| UTXO-911-001 v1.0 | 5 |
| ERX-ROADMAP-001 v1.0 | 33 |
| Technical response to ERX-ROADMAP-001 | 0 |
| **Total** | **82** |

The technical response remains contextual material; its recommendations have not been silently promoted to source-mandatory requirements.

## 3. Historical-count reconciliation

The prior 65-count must be retained as a historical snapshot and superseded by explicit versioned evidence. It must not be represented as the current register count.

A one-to-one row mapping from each of the historical 65 statements to the current 82 statements is **not certified by this note**. That requires the exact historical CSV/batch snapshot and a row-level ID/statement crosswalk. Where the old snapshot is available in Git history, its commit/blob must be recorded in that crosswalk.

No statement is made here that the 17-record numerical difference is exactly 17 newly created, uniquely scoped obligations; numerical difference alone cannot prove additions, splits, corrections or reclassification.

## 4. Conflicting controlled artifacts requiring synchronization

The branch currently contains documents with stale or conflicting figures:

1. The canonical CSV and current status reconciliation state 82 source candidates / 107 individual records.
2. The semantic-review register states that its former 65-candidate scope is stale.
3. The pending-specification register's narrative/table still describes 63 gaps and 19 unassessed candidates, while the current status reconciliation reports 76 open gaps plus six `NO_GAP_WITH_EVIDENCE` dispositions. The row-level gap register must be regenerated and checked against the current canonical CSV before either count is treated as authoritative.
4. The LAEV baseline decision package contains historical statements referring to 65 candidates, 63 gaps and phase-allocation figures that conflict with the current 82-candidate snapshot. Its baseline fields remain NOT APPROVED and must be version-corrected before submission.
5. The source-coverage audit and status reconciliation agree that page-bound checks are complete but exact clause/diagram fidelity is still open.

## 5. Reconciliation rules

- Preserve every existing canonical requirement ID and its change history.
- Compare historical and current statements, source locators and parent/child links; classify each difference as unchanged, corrected, split/decomposed, derived, superseded with evidence, or unresolved.
- Do not merge similar requirements merely because they share a subject. Record invariant, mechanism, actor, trigger, scope and independently testable outcome.
- Keep extracted source requirements distinct from derived proposals and recommendations.
- Do not resolve the eight decision candidates during WP-0.7; maintain their open status for the governed decision work package.
- Do not infer approval from a commit, PR, structural check or generated matrix.

## 6. Current acceptance boundary

This note reconciles the **scope/count discrepancy** and establishes the current baseline reference. It does not complete the semantic review of all 82 candidates or 107 individual records.

WP-0.7 remains **IN_PROGRESS — ACCEPTANCE OPEN** until:
- the 65-to-82 historical crosswalk is evidenced;
- exact clause/diagram fidelity dispositions are recorded for all 82 candidates;
- all 107 individual records pass semantic, modality, classification and phase review;
- the gap register and eight decision candidates are synchronized to the canonical snapshot;
- all traceability relations and document versions are audited;
- the exact baseline is submitted for LAEV approval.

No implementation, deployment, Phase 1 execution or institutional operation is authorized by this note.

---
End of scope reconciliation.
