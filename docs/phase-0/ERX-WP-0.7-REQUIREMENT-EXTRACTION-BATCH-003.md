# ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-003
## Roadmap-Grounded Candidate Extraction — Batch 3

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-003 |
| Version | 0.1.0 |
| Status | EXTRACTED — TECHNICAL REVIEW PENDING |
| Work Package | WP-0.7 / Activities 0.7.2–0.7.9 |
| Date | 2026-11-25 |
| Source | ERX-ROADMAP-001 v1.0 |
| Source-native locators | PDF pages 6–10, 21, 23–24 |
| Register | registers/requirements-traceability.csv |

## 1. Scope and method

This batch records 12 additional candidate requirements from direct inspection of the supplied ERX-ROADMAP-001 PDF. It supplements, rather than replaces, the Protocol/Atlas/UTXO-based batches 001 and 002.

Roadmap language that explicitly requires an element is recorded as a candidate. Recommendations (for example, separating event documents from UTXO transition records) remain recommendations and are not promoted to approved design decisions. Where the Roadmap says a state name or transition must later be approved, this batch preserves that qualification.

All entries remain `EXTRACTED — REVIEW PENDING`. No priority, owner, approval, final state vocabulary, algorithm, implementation method or phase allocation is inferred.

## 2. Candidate inventory

| Requirement ID | PDF locator | Candidate subject |
|---|---|---|
| ERX-REQ-STATE-0001 | pp.6–7, §1.2 | Independent communication and agent-availability state machines |
| ERX-REQ-STATE-0002 | p.7, §1.3 | Required fields for each transition specification |
| ERX-REQ-INV-0001 | p.8, §1.5 | Closed communication session cannot reactivate |
| ERX-REQ-INV-0002 | p.8, §1.5 | Correction cannot retroactively modify sealed document |
| ERX-REQ-INV-0003 | p.8, §1.5 | Transition provenance preservation |
| ERX-REQ-INV-0004 | p.8, §1.5 | Recovery cannot resurrect consumed states or revoked credentials |
| ERX-REQ-DATA-0001 | p.9, §2.1 | Formal schema, version and validation rules for JSON structures |
| ERX-REQ-CRYPTO-0001 | p.10, §2.3 | Signature specification elements and historical validation |
| ERX-REQ-CRYPTO-0002 | p.10, §2.4 | Non-circular cryptographic relationship among documents and UTXO |
| ERX-REQ-VERIFY-0004 | p.21, §7 | Sufficient independence of verifier from ERX Core |
| ERX-REQ-TRANS-0002 | pp.23–24, §8.2 | Required interinstitutional transfer-protocol elements |
| ERX-REQ-TEST-0001 | p.24, §9.1 | Six categories of testing |

## 3. Interpretation controls

1. The two state machines are required as separate models; the Roadmap says definitive names and transitions require protocol approval.
2. The transition checklist is a source-derived specification requirement; no particular transition implementation is selected.
3. Recovery, sealed-document correction and provenance statements are retained as separate invariants; their overlap with existing UTXO requirements requires review.
4. The Roadmap recommends a separation between event documents and UTXO transition records. This recommendation is not recorded as an already approved architecture.
5. The verifier's "sufficient independence" is qualitative in the source; the independence boundary and threat model remain to be defined.
6. The transfer list records required specification topics; it does not decide the authority model or select distributed transaction coordination.
7. The six testing categories are a planning requirement; test cases, coverage thresholds and acceptance criteria remain to be designed.

## 4. Result and pending work

The traceability CSV now contains 45 candidate records: 15 in batch 001, 18 in batch 002 and 12 in batch 003. This is an extraction inventory, not an approved requirements baseline.

Remaining WP-0.7 work includes source-by-source extraction of uncovered Roadmap and response material, review of all source locators and normative modality, classification and mandatory/design/pending distinctions, overlap and conflict analysis, open-decision linkage, verification-criterion completion, justified phase allocation, and construction of the consolidated traceability matrix.

---
End of ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-003
