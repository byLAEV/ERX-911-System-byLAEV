# ERX-WP-0.7 — Register Reconciliation and Control Report

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-REGISTER-RECONCILIATION-001 |
| Version | 1.0.0 |
| Status | CONTROL REPORT — CORRECTION REQUIRED |
| Date | 2026-11-26 |
| Work Package | WP-0.7 |
| Authority | LAEV design authority; technical preparation under delegated review |
| Sources | Batch 001, Batch 002, Batch 003; current traceability CSV; phase-allocation register; WORKPLAN-PHASE-0 v1.5.3 |

## 1. Purpose

Resolve the conflicting requirement counts and establish which records may be used as the WP-0.7 working baseline. This report does not approve individual requirements and does not itself close WP-0.7.

## 2. Reconciled extraction inventory

The three controlled extraction records state:
- Batch 001: 15 candidates.
- Batch 002: 18 additional candidates.
- Batch 003: 12 additional candidates.

The cumulative extraction inventory is therefore 45 candidate requirements. The CSV's controlling structural review snapshot also records 45 data rows and 19 columns. The 45 records remain candidate/source-review records, not an approved requirement baseline.

The current WORKPLAN-PHASE-0 v1.5.3 WP-0.7 narrative contains an obsolete sentence referring to 15 candidates across batches 001–003. That statement describes the initial batch only and is inconsistent with batches 002 and 003. It must be corrected to 45 cumulative candidates, while preserving the status EXTRACTED — REVIEW PENDING.

## 3. Phase-allocation discrepancy

The current phase-allocation register declares a distribution total of 65. Its own stated source of truth is registers/requirements-traceability.csv, whose documented structural review snapshot contains 45 rows.

A 20-record difference is not explained by the current evidence. No additional 20 approved or source-verified requirements may be presumed. Until every allocation row is reconciled to a unique requirement ID present in the canonical CSV, the 65 total and the associated distribution are NOT ACCEPTABLE as a controlled allocation result.

Required disposition:
1. Preserve the historical v0.1.0 allocation register as evidence; do not silently rewrite its history.
2. Produce a corrected allocation revision containing exactly one primary phase allocation per canonical requirement ID.
3. Reject orphan allocation IDs, duplicates, and requirements absent from the canonical CSV.
4. Justify each allocation against the approved ERX-ROADMAP-001 phase purpose and boundaries.
5. Treat allocation as planning only; it does not authorize execution of later phases.

## 4. Canonical working baseline

Until semantic validation is completed:
- Canonical working register: registers/requirements-traceability.csv.
- Baseline count: 45 candidate records, subject to a fresh current-branch integrity check.
- Origin class: EXTRACTED for records whose source locators are directly supported by the five inspected foundational sources.
- Lifecycle status: EXTRACTED — REVIEW PENDING.
- Approval: NOT_APPROVED.
- Owners: NOT_ASSIGNED unless a controlled authority record says otherwise.
- Phase assignment: only valid after the corrected allocation reconciliation.

No candidate is promoted to APPROVED by this report.

## 5. Classification and normative-strength controls

For every row, the review must separately establish:
- primary requirement type and justified secondary tags;
- origin class (EXTRACTED, DERIVED, PROPOSED);
- whether the source uses mandatory, permissive, descriptive, or recommendatory language;
- whether the record is a true independently verifiable obligation or a specification topic;
- verification criterion and method, or an explicit NOT_DEFINED/PENDING_SPECIFICATION reason;
- ambiguity, overlap, contradiction and decision links.

A source's use of "must/shall/debe/deberá" does not by itself prove that the statement applies universally; context, subject-matter authority and scope must also be checked. Conversely, recommendations in the technical response or Roadmap must not be promoted to mandatory requirements without a recorded authority decision.

## 6. Technical-response source treatment

The technical response to ERX-ROADMAP-001 is FND-005, with no source-native formal document ID/version stated in the supplied PDF. It may support review notes and decision candidates. It must not be treated as an independent normative source or used to increase the normative strength of another source. Any adopted recommendation requires a controlled decision record.

## 7. Required corrective actions

| Action | Activity | Completion evidence |
|---|---|---|
| Correct stale cumulative count in Workplan | 0.7.2 | Workplan commit and reconciliation report |
| Revalidate all 45 CSV rows against exact source pages/sections | 0.7.2–0.7.3, 0.7.9 | Row-by-row review register |
| Complete semantic classification and mandatory/design distinction | 0.7.4–0.7.6 | Controlled classification register |
| Reconcile pending specifications and open decisions | 0.7.7–0.7.8 | Linked pending-specification and decision registers |
| Replace unsupported 65 allocation with canonical-ID mapping | 0.7.10 | Corrected allocation register and automated integrity check |
| Produce consolidated traceability matrix and audit | 0.7.11 | CSV, human-readable matrix, validation report |
| Perform final acceptance review | All | Acceptance-readiness report and closure decision |

## 8. Current decision

WP-0.7 remains IN_PROGRESS. The 45-candidate inventory is the only cumulative count supported by the three batch records. The 65-row allocation total is not accepted as reconciled. This report corrects the control narrative and identifies the work required; it does not assert that the substantive row-by-row review or all eleven activities are complete.

---
End of ERX-WP-0.7-REGISTER-RECONCILIATION-001
