# ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 |
| Version | 1.1.0 |
| Status | PARTIAL INDIVIDUAL REVIEW — ACCEPTANCE PENDING |
| Date | 2026-11-28 |
| Activity | WP-0.7.5 — Identify mandatory requirements |
| Canonical source register | registers/requirements-traceability.csv |
| Individual register | registers/requirement-identification-register.csv |

## 1. Purpose and method

This review evaluates the individual record layer against its parent source candidate and flags child statements that cannot safely inherit a blanket mandatory disposition. It is a controlled review record, not an approval of the requirements baseline.

For each child, the minimum review dimensions are: source locator, source modal force, actor, trigger, scope, condition, observable outcome, parent-child lineage and recommendation/option separation. A child that inherits a parent disposition without independent semantic inspection is not accepted by this review.

## 2. Reconciled population

- Source candidates: 82.
- Individual records: 107.
- Parent-child references: 107/107 resolve to one of 82 source candidates.
- No child record is an additional source candidate.
- No requirement is approved by this review.

## 3. Current modality map

The current source CSV contains:
- 75 MANDATORY_CANDIDATE parents.
- 6 MODALITY_UNRESOLVED parents.
- 1 MIXED_MODALITY parent (ERX-REQ-CRYPTO-0002), which contains one mandatory clause and one recommendation.

The corresponding individual layer contains:
- 97 MANDATORY_CANDIDATE children.
- 9 MODALITY_UNRESOLVED children.
- 1 RECOMMENDATION_CANDIDATE child (ERX-REQ-CRYPTO-0002-B).

Totals: 107 individual records.

## 4. Confirmed mixed-modality defect and correction

ERX-ROADMAP-001 v1.0, PDF p.10 §2.4, combines:
- a requirement to define the cryptographic relationship without circular dependencies; and
- a recommendation that the event document and UTXO transition record be considered separately.

The parent ERX-REQ-CRYPTO-0002 is now recorded as MIXED_MODALITY / SPLIT_REQUIRED. Child -0002-A is MANDATORY_CANDIDATE. Child -0002-B is RECOMMENDATION_CANDIDATE. The canonical source and individual registers were updated accordingly. This is a source-faithful correction, not an approval.

## 5. Direct graphical evidence reviewed

The original ERX-ATLAS-001 v1.1 PDF was visually inspected at:
- p.8, Lámina 03: the no-response branch explicitly displays “REGISTRAR NO RESPUESTA”. It supports a process outcome, but the graphic alone does not unambiguously establish a normative modal; ERX-REQ-AGENT-0002 remains MODALITY_UNRESOLVED.
- p.19, Lámina 06: “Cada OTS debe distinguir” followed by seven evidence states; pending proof must never be presented as anchored. This supports explicit mandatory modality for ERX-REQ-OTS-0001.
- p.27: “El verificador debe producir resultados separados” followed by eight verification categories. This supports explicit mandatory modality for ERX-REQ-VERIFY-0003.

The four Atlas source candidates are ERX-REQ-AGENT-0001, AGENT-0002, OTS-0001 and VERIFY-0003. Their graphical evidence is not to be treated as interchangeable with text extraction.

## 6. Unresolved individual records

The nine unresolved child records remain:
- ERX-REQ-UTXO-0001 — state-transition definition/description; modal force requires approved protocol definition.
- ERX-REQ-AGENT-0002 — diagram-derived no-response path; explicit imperative is visible, but source status/modal force requires controlled disposition.
- ERX-REQ-LOC-0002 — compound behavior (location absence does not block; later changes are new events); split/condition scope requires review.
- ERX-REQ-CONTACT-0001 — descriptive distinction between reception and agent-response times.
- ERX-REQ-OTS-0003-A through -0003-D — workflow sequence decomposed into four child statements; exact imperative force is not established by the normalized parent.
- ERX-REQ-OTS-0004 — evidentiary boundary describing what OTS does not prove; preserve as verification/design boundary, not silently promote to mandatory system obligation.

## 7. Remaining individual acceptance work

1. Independently inspect all 107 individual statements against the exact source passage or diagram.
2. Record PASS / CORRECT / SPLIT / DERIVED / BLOCKED for every child, with exact source locator and rationale.
3. Verify that all conditional wording remains conditional (e.g. “when available”, “where technically possible”, “when institutionally authorized”).
4. Detect compound children, broadened scope, missing actor/trigger, and recommendation leakage.
5. Confirm all 82 parent records and 107 child records reconcile after corrections.
6. Re-run the bidirectional traceability audit and update the source-fidelity matrix.
7. Obtain the exact baseline acceptance required by the governing WP-0.7 acceptance procedure.

## 8. Determination

**Individual modality coverage is complete at the mapping level, but semantic/source fidelity acceptance is NOT complete.** The current map is 97 mandatory candidates, 9 unresolved and 1 recommendation candidate. No child is APPROVED. WP-0.7.5 remains IN_PROGRESS — NOT ACCEPTED.

---
End of ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 v1.1.0.
