# ERX-WP-0.7.4-CLASSIFICATION-RECORD-001

Version: 0.2.0  
Date: 2026-11-25  
Status: CLASSIFICATION REVIEWED — SOURCE FIDELITY PENDING; NO REQUIREMENTS BASELINE APPROVAL  
Work Package: WP-0.7 / Activity 0.7.4  
Method: ERX-REQUIREMENTS-METHOD-001 v1.0.0, §5  
Branch: `wp-0.7-requirements-review`

## 1. Scope and distinction

Classification was applied at both linked levels:
- 82 source-derived candidate records in `registers/requirements-traceability.csv`.
- 107 individually identified records in `registers/requirement-identification-register.csv`.

The 107 records are not 107 additional independent source passages. They comprise the individual requirement set reconciled to 82 source candidates under accepted WP-0.7.3. Child records retain their parent candidate and source locator.

## 2. Taxonomy

Each record has one primary type and zero or more secondary tags, using the controlled taxonomy in ERX-REQUIREMENTS-METHOD-001 §5:
FUNCTIONAL; SECURITY; PRIVACY; DATA_AND_RECORDS; INTEROPERABILITY; PERFORMANCE_AND_CAPACITY; OPERATIONAL; GOVERNANCE; COMPLIANCE; ARCHITECTURAL; INTERFACE; VERIFICATION.

Legacy/preliminary tokens were normalized only where they mapped to a defined taxonomy category (e.g. TRANSACTIONAL to FUNCTIONAL, CRYPTOGRAPHY to SECURITY, RESILIENCE to OPERATIONAL, IDENTITY to GOVERNANCE, QUALITY/AUDITABILITY to VERIFICATION, INTEGRITY to DATA_AND_RECORDS). This normalization is recorded in the classification rationale and does not change the source statement.

## 3. Source-candidate classification counts

| Primary type | Records |
|---|---:|
| FUNCTIONAL | 17 |
| SECURITY | 14 |
| PRIVACY | 3 |
| DATA_AND_RECORDS | 14 |
| INTEROPERABILITY | 2 |
| PERFORMANCE_AND_CAPACITY | 1 |
| OPERATIONAL | 4 |
| GOVERNANCE | 10 |
| ARCHITECTURAL | 9 |
| INTERFACE | 1 |
| VERIFICATION | 7 |
| **Total** | **82** |

## 4. Individual requirement classification counts

| Primary type | Records |
|---|---:|
| FUNCTIONAL | 18 |
| SECURITY | 17 |
| PRIVACY | 7 |
| DATA_AND_RECORDS | 21 |
| INTEROPERABILITY | 2 |
| PERFORMANCE_AND_CAPACITY | 1 |
| OPERATIONAL | 7 |
| GOVERNANCE | 13 |
| ARCHITECTURAL | 11 |
| INTERFACE | 1 |
| VERIFICATION | 9 |
| **Total** | **107** |

The 39 decomposed child records received child-level primary/secondary labels according to their individual obligation. Other individual records inherit the parent candidate's provisional taxonomy and explicitly say so in their rationale; that inheritance remains subject to semantic review.

## 5. Completion and validation performed

- All 82 source candidate rows have one valid primary taxonomy type.
- All 107 individual requirement rows have one valid primary taxonomy type.
- Secondary tags use only controlled taxonomy values.
- The 17 records previously marked NOT_CLASSIFIED were individually classified.
- Primary/secondary values and rationale were written to both machine-readable registers.
- Reconciled four primary/secondary taxonomy assignments against the later WP-0.7.4 review record on `main`: `ERX-REQ-CORE-0001`, `ERX-REQ-TEST-0002`, `ERX-REQ-TEST-0003`, and `ERX-REQ-TEST-0004` are `VERIFICATION` primary; secondary tags are respectively `ARCHITECTURAL`, none, `OPERATIONAL`, and none. The same assignments are synchronized in the 107-record individual register where those IDs occur.
- Both registers preserve source origin, source references, lifecycle review status and NOT_APPROVED state.
- No priority, mandatory status, legal compliance status, design approval, phase assignment or implementation authorization was inferred from classification.
- No candidate was deleted or merged.

## 6. Classification limitations and review findings

This is a controlled working classification, not an approved requirements baseline. Primary type is selected by the principal acceptance concern; secondary tags capture additional concerns. Some cross-domain requirements can reasonably be debated. In particular:
- UTXO single-consumption and atomic-transition statements are FUNCTIONAL with SECURITY secondary tags; their security significance is preserved.
- Signature, cryptographic commitment and key-control statements are SECURITY unless their primary acceptance outcome is a data/evidence record or verification result.
- Privacy/custody/retention statements are PRIVACY even when security or governance controls are secondary.
- Homologation, authority and institutional admission statements are GOVERNANCE.
- Evidence production and verifier-output statements are VERIFICATION.
- System boundary/separation constraints are ARCHITECTURAL.
- No COMPLIANCE classification is asserted because the inspected source candidate set does not by itself establish a jurisdiction-specific legal/regulatory obligation. This does not mean legal review is unnecessary.

Exact source clause verification remains WP-0.7.9. Normative modality and mandatory/prohibitory/recommendatory assessment remain WP-0.7.5; WP-0.7.5 is independently IN_PROGRESS and its check is not granted. Design constraints versus recommendations/options remain WP-0.7.6.

## 7. Acceptance recommendation

Activity 0.7.4 classification review is recorded for the 82 source candidates and 107 individual records. The four disputed assignments have been reconciled and the machine-readable registers synchronized. Exact source fidelity remains pending under WP-0.7.9; normative modality remains pending under WP-0.7.5. This record does not grant WP-0.7.5 completion or approve the requirements baseline. This record does not approve requirements or authorize implementation.

---
End of record.
