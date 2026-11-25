# ERX-WP-0.7.3-INDIVIDUAL-REQUIREMENT-IDENTIFICATION-RECORD-001

## Individual Identification, Atomicity and Decomposition

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7.3-INDIVIDUAL-REQUIREMENT-IDENTIFICATION-RECORD-001 |
| Version | 1.0.1 |
| Status | EXECUTION COMPLETE — SUBMITTED FOR LAEV ACCEPTANCE |
| Work Package | WP-0.7 / Activity 0.7.3 |
| Date | 2026-11-25 |
| Branch | wp-0.7-requirements-review |
| Source candidate register | registers/requirements-traceability.csv |
| Individual identification register | registers/requirement-identification-register.csv |
| Disposition record | ERX-WP-0.7.3-ATOMICITY-AND-OVERLAP-DISPOSITION-001 v1.0.0 |

## 1. Final identification result

| Measure | Result |
|---|---:|
| Source candidate records | 82 |
| Individual requirement records | 107 |
| Unique individual IDs | 107 |
| Unique parent candidates represented | 82 |
| Missing parent candidates | 0 |
| Orphan parent references | 0 |
| Compound candidates decomposed | 14 |
| Atomic child records created | 39 |
| Single-obligation records | 50 |
| Structured-list records with explicit atomicity disposition | 18 / 18 |
| Potential overlap groups with explicit disposition | 8 / 8 |
| Duplicate individual IDs | 0 |

All 82 source candidates reconcile to the 107 individual records. No source candidate was silently discarded, merged, rejected, or marked approved.

## 2. Decomposition

A candidate was decomposed where its source statement contained independently verifiable obligations with separate pass/fail outcomes. Child IDs use suffixes A, B, C, etc., link to the parent candidate and retain source ID, version and locator.

| Parent candidate | Children | Subject |
|---|---:|---|
| ERX-REQ-UTXO-0006 | 2 | Canonicalization / institutional signature |
| ERX-REQ-UTXO-0008 | 2 | OTS lifecycle / non-blocking emergency attention |
| ERX-REQ-UTXO-0009 | 4 | Event identity / retransmission / atomicity / retry result |
| ERX-REQ-AGENT-0001 | 3 | Institutional vs agent authentication / attention continuity |
| ERX-REQ-ARCH-0001 | 3 | Common core / adapter boundary / invariant preservation |
| ERX-REQ-TRANS-0001 | 2 | Transfer record / no duplicate admission |
| ERX-REQ-CORR-0001 | 3 | Immutability / complementary correction / history |
| ERX-REQ-CRYPTO-0002 | 2 | Non-circular relationship / Roadmap recommendation |
| ERX-REQ-TIME-0002 | 3 | UTC source and precision / monotonic ordering / discrepancies |
| ERX-REQ-OTS-0003 | 4 | Independent commitments / document preparation / OTS / verification |
| ERX-REQ-PRIV-0003 | 3 | Institutional custody / commitment-only anchoring / identifier disclosure |
| ERX-REQ-PRIV-0004 | 3 | Disclosure minimization / anti-enumeration / controlled verification |
| ERX-REQ-PRIV-0005 | 3 | Retention / deletion-anchor distinction / explanatory record |
| ERX-REQ-OPS-0005 | 2 | Durable local queue / separate recovery timestamps |
| **Total** | **39** | |

The Roadmap wording “should be considered separately” in ERX-REQ-CRYPTO-0002 remains a recommendation, not an adopted mandatory design rule.

## 3. Atomicity disposition

All 18 structured-list records have an explicit disposition in the machine-readable register. They are retained as cohesive acceptance units where their enumerated members jointly define a schema, control baseline, contract, test suite, verification package, metric set, operating mode, homologation/admission gate, outcome model, or taxonomy. The rationale for each individual record is stored in its `decomposition_note` and its `atomicity_result` field.

This is not a blanket rule that lists are always atomic. If subsequent design or verification work demonstrates independently testable obligations for list members, derived child requirements may be introduced under change control without changing the source statement.

## 4. Potential overlap disposition

All eight groups have a recorded relationship classification and rationale in the register and disposition report. The review found related requirements at different lifecycle boundaries, abstraction levels, or evidence roles. They are retained as distinct; no duplicates are merged or deleted.

| Group | Final relationship |
|---|---|
| OV-UTXO-DOUBLE-SPEND | Same invariant, different control levels |
| OV-UTXO-IDEMPOTENCY | Related but distinct lifecycle boundaries |
| OV-UTXO-ATOMIC-ADMISSION | Related but distinct transition boundaries |
| OV-OTS-NONBLOCKING | Same principle, different scope |
| OV-OTS-LIFECYCLE | Lifecycle states versus process sequence |
| OV-VERIFIER-OUTPUT | Evidence package versus result dimensions |
| OV-IDENTITY-SEPARATION | Institutional identity versus professional identity and operational effect |
| OV-TELEPHONE-CONTINUITY | Infrastructure availability versus identity-validation failure |

Full requirement-level rationale is in ERX-WP-0.7.3-ATOMICITY-AND-OVERLAP-DISPOSITION-001 v1.0.0.

## 5. Structural and referential validation

- 107 individual records and 14 columns.
- 107 unique individual identifiers.
- All records have parent candidate references.
- All 82 source candidate IDs are represented.
- No missing or orphan parent references.
- Every record retains source ID/version and source locator.
- All remain EXTRACTED / CANDIDATE — REVIEW PENDING / NOT_APPROVED.
- No requirement approval, type classification, phase assignment, or implementation authorization is implied.

## 6. Scope limits and dependencies

This activity identifies and relates requirements. It does not perform WP-0.7.4 classification, WP-0.7.5 mandatory assessment, WP-0.7.6 design assessment, WP-0.7.9 exact source-clause verification, or WP-0.7.10 phase allocation. Exact source verification may raise controlled corrections if a locator or interpretation is disproved.

## 7. Completion and acceptance

The identification, decomposition, atomicity-disposition, overlap-disposition, parent-reconciliation and structural-audit tasks for Activity 0.7.3 are complete. This record is submitted to LAEV for formal acceptance. Until express acceptance is recorded, Workplan status is **EXECUTION COMPLETE — ACCEPTANCE PENDING**, not COMPLETED / ACCEPTED.

---
End of record.
