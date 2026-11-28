# ERX-WP-0.7.5-CHILD-MODALITY-CORRECTION-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-CHILD-MODALITY-CORRECTION-001 |
| Version | 1.1.0 |
| Status | CORRECTIONS INCORPORATED — ACTIVITY 0.7.5 COMPLETED / ACCEPTED |
| Date | 2026-11-28 |
| Work package/activity | WP-0.7 / 0.7.5 Identify mandatory requirements |
| Branch | wp-0.7-requirements-review |
| Source | ERX-ROADMAP-001 v1.0, PDF p.10, §2.4 |
| Registers | requirements-traceability.csv; requirement-identification-register.csv |

## 1. Purpose

Record a source-verified correction discovered during child-level modality review. This record preserves the CRYPTO-0002 correction and the additional OTS-0003 mixed-modality split discovered during final child-level review. It prevents recommendations and descriptive workflow steps from being inherited as mandatory requirements.

## 2. Exact source distinction

ERX-REQ-CRYPTO-0002 currently combines two distinct statements:
1. The cryptographic relationship among JSON 01, 02 and 03 and their UTXO records must be defined without circular dependencies.
2. The event document and UTXO transition record should be considered separately, as recommended by the Roadmap.

The first clause is mandatory wording in the source. The second is expressly framed as a recommendation. These cannot share one undifferentiated mandatory disposition.

## 3. Correct disposition

| Record | Disposition | Reason |
|---|---|---|
| ERX-REQ-CRYPTO-0002 (parent) | MIXED_MODALITY — SPLIT REQUIRED | Compound parent combines obligation and recommendation |
| ERX-REQ-CRYPTO-0002-A | MANDATORY_CANDIDATE | Derived from the source's mandatory “must be defined” clause |
| ERX-REQ-CRYPTO-0002-B | RECOMMENDATION_CANDIDATE | Source explicitly says “should be considered separately” and labels it recommended |

The source-candidate CSV records MIXED_MODALITY_SPLIT for ERX-REQ-CRYPTO-0002 and ERX-REQ-OTS-0003. For OTS-0003, child -A (each JSON's independent commitment) is MANDATORY_CANDIDATE; children -B through -D remain NOT_MANDATORY descriptive workflow steps. No requirement is approved by these corrections.

## 4. Reconciled counts

Source-candidate layer:
- 73 MANDATORY_CANDIDATE
- 7 NOT_MANDATORY
- 2 MIXED_MODALITY_SPLIT (ERX-REQ-CRYPTO-0002 and ERX-REQ-OTS-0003)
- Total: 82

Individual layer:
- 95 MANDATORY_CANDIDATE
- 11 NOT_MANDATORY
- 1 RECOMMENDATION_CANDIDATE (ERX-REQ-CRYPTO-0002-B)
- Total: 107

These are screening dispositions, not approved obligations.

## 5. Completion evidence and boundary

The exact source PDFs and Atlas plates were inspected. All 82 source candidates have VERIFIED fidelity dispositions; all 107 individual records have VERIFIED semantic/modality dispositions, condition/scope PASS and actor/trigger/outcome PASS or justified NOT_APPLICABLE. The source and child canonical registers are synchronized.

GitHub Actions evidence gate: PASS, run #18 — https://github.com/byLAEV/ERX-911-System-byLAEV/actions/runs/46153543878.

**Determination: WP-0.7.5 COMPLETED / ACCEPTED.** This correction record documents the two mixed-modality parent splits and the final reconciled counts. Requirements remain NOT_APPROVED as a baseline. WP-0.7 remains IN_PROGRESS; activity 0.7.9 and other WP-0.7 gates remain open.
---
End of ERX-WP-0.7.5-CHILD-MODALITY-CORRECTION-001 v1.1.0.
