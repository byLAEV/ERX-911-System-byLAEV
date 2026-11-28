# ERX-WP-0.7.5-CHILD-MODALITY-CORRECTION-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-CHILD-MODALITY-CORRECTION-001 |
| Version | 1.0.0 |
| Status | PARTIAL SOURCE-VERIFIED CORRECTION — ACTIVITY ACCEPTANCE OPEN |
| Date | 2026-11-28 |
| Work package/activity | WP-0.7 / 0.7.5 Identify mandatory requirements |
| Branch | wp-0.7-requirements-review |
| Source | ERX-ROADMAP-001 v1.0, PDF p.10, §2.4 |
| Registers | requirements-traceability.csv; requirement-identification-register.csv |

## 1. Purpose

Record a source-verified correction discovered during child-level modality review. The correction prevents a recommendation from being inherited as a mandatory requirement merely because it shares a parent candidate with a mandatory clause.

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

The source-candidate CSV now records MIXED_MODALITY for ERX-REQ-CRYPTO-0002. The individual recommendation is not promoted to a mandatory requirement. No requirement is approved by this correction.

## 4. Reconciled counts

Source-candidate layer:
- 75 MANDATORY_CANDIDATE
- 6 MODALITY_UNRESOLVED
- 1 MIXED_MODALITY (ERX-REQ-CRYPTO-0002; split disposition recorded)
- Total: 82

Individual layer:
- 97 inherited MANDATORY_CANDIDATE
- 9 MODALITY_UNRESOLVED
- 1 RECOMMENDATION_CANDIDATE (ERX-REQ-CRYPTO-0002-B)
- Total: 107

These are screening dispositions, not approved obligations.

## 5. Remaining acceptance blockers

This correction does not close WP-0.7.5. The remaining work is:
1. Complete exact clause/diagram fidelity dispositions for all 82 source candidates.
2. Independently review all 107 individual statements for normative force, scope, actor, trigger, condition and source fidelity.
3. Verify the four Atlas candidates against the actual graphical plates, not text extraction alone.
4. Review the Roadmap's conditional, procedural and stage-gate language so that future-phase requirements are not misrepresented as current operational obligations.
5. Confirm all six unresolved candidates retain justified and explicit dispositions.
6. Re-run counts, parent-child mapping and bidirectional traceability after all corrections.
7. Record LAEV's exact-baseline acceptance.

**Determination: WP-0.7.5 remains IN_PROGRESS — NOT ACCEPTED.** The mixed-modality defect is corrected; the complete 82/107 review is not yet evidenced.

---
End of correction record.
