# ERX-WP-0.7-CLASSIFICATION-REGISTER-001
## Controlled Classification and Modality Review

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-CLASSIFICATION-REGISTER-001 |
| Version | 0.1.0 |
| Status | WORKING CLASSIFICATION — CLAUSE-LEVEL REVIEW PENDING |
| Work Package | WP-0.7 / Activities 0.7.3–0.7.6 |
| Date | 2026-11-25 |
| Register snapshot | 65 candidates; 28 columns |
| Method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 |

## 1. Purpose

This register records a consistent preliminary classification for all current candidate requirements. It does not approve any requirement and does not make a final determination of mandatory force. It keeps four separate questions apart:
- primary requirement type;
- secondary concern tags;
- source modality evidence;
- design-constraint character.

## 2. Controlled primary taxonomy

The primary type is selected from the method's controlled taxonomy: FUNCTIONAL, SECURITY, PRIVACY, DATA_AND_RECORDS, INTEROPERABILITY, PERFORMANCE_AND_CAPACITY, OPERATIONAL, GOVERNANCE, COMPLIANCE, ARCHITECTURAL, INTERFACE, VERIFICATION.

The original multi-label value is retained through secondary tags and classification rationale. Normalization is not deletion of the original classification meaning.

## 3. Mandatory assessment rule

The current register records that normative language occurs on the cited source page. That is only a screening signal. It does NOT establish that the exact requirement statement is itself explicitly mandatory. A reviewer must match each candidate statement to the exact clause and determine whether it is:
- explicitly mandatory/prohibitory;
- descriptive or explanatory;
- a recommendation/option;
- derived by interpretation;
- proposed to close a gap.

Until that clause-level match is completed, the record remains EXTRACTED — REVIEW PENDING and must not be labelled APPROVED or finally MANDATORY.

## 4. Design assessment rule

The design assessment is a working identification of the kind of constraint or design domain implicated by the requirement. It is not an adopted implementation decision. Recommendations in the sources remain recommendations. For example, the Roadmap's HSM recommendation does not mandate HSM; the multi-center coordination alternatives do not select a consensus model; and a technology option does not become an approved architecture solely through this classification.

## 5. Current inventory

All 65 candidate records have:
- one primary taxonomy type;
- zero or more secondary tags;
- a classification rationale;
- a preliminary design assessment;
- a pending-specification note;
- a clause-level mandatory assessment still awaiting exact match.

The machine-readable source of truth is `registers/requirements-traceability.csv`.

## 6. Acceptance still required

0.7.3 and 0.7.4 require human semantic review of the individual statement, its scope, testability, overlap and type. 0.7.5 requires exact clause-level modality review. 0.7.6 requires a distinction between source-defined design constraints and optional/proposed implementation choices. This register is evidence of progress, not completion of those activities.

---
End of ERX-WP-0.7-CLASSIFICATION-REGISTER-001
