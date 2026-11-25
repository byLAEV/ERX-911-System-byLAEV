# ERX-WP-0.7.3-INDIVIDUAL-REQUIREMENT-IDENTIFICATION-RECORD-001
## Individual Identification, Atomicity and Decomposition

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7.3-INDIVIDUAL-REQUIREMENT-IDENTIFICATION-RECORD-001 |
| Version | 0.1.0 |
| Status | IN_REVIEW — ATOMICITY AND OVERLAP DISPOSITION OPEN |
| Work Package | WP-0.7 / Activity 0.7.3 |
| Date | 2026-11-25 |
| Branch | wp-0.7-requirements-review |
| Input | registers/requirements-traceability.csv (82 candidates) |
| Output | registers/requirement-identification-register.csv |

## 1. Result

The individual identification register contains 107 records, 107 unique individual IDs and 14 columns. It preserves the parent candidate, source ID/version, source locator, evidence summary, origin, lifecycle status and approval state.

| Measure | Count |
|---|---:|
| Source candidates | 82 |
| Individual records | 107 |
| Compound candidates decomposed | 14 |
| Atomic child records created | 39 |
| Single-obligation records retained | 50 |
| Structured-list / multi-part records requiring final atomicity disposition | 18 |
| Duplicate individual IDs | 0 |

The 107 records are not yet 107 accepted atomic requirements: 18 records retain structured lists, cases, or multiple acceptance dimensions and require explicit disposition. All remain EXTRACTED, CANDIDATE — REVIEW PENDING, NOT_APPROVED.

## 2. Decomposition performed

A candidate was decomposed where its source statement contained independently verifiable obligations with separate pass/fail outcomes. Child IDs use suffixes A, B, C, etc.; each child links to its parent candidate and retains the parent's source ID, version and locator.

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

## 3. Structured records requiring final atomicity disposition

- ERX-REQ-UTXO-0002 — UTXO field set.
- ERX-REQ-UTXO-0004 — uniqueness-support mechanisms.
- ERX-REQ-UTXO-0011 — single consumption and validation conditions.
- ERX-REQ-INT-0001 — adapter contract fields.
- ERX-REQ-INST-0001 — installation configuration set.
- ERX-REQ-VERIFY-0001 — exported-case verification package.
- ERX-REQ-CRYPTO-0001 — signature specification contents.
- ERX-REQ-TEST-0003 — core test scenarios.
- ERX-REQ-SEC-0001 — security-interface controls.
- ERX-REQ-TEST-0004 — test categories and referenced tests.
- ERX-REQ-TEST-0005 — acceptance metric set and numeric target setting.
- ERX-REQ-PILOT-0001 — shadow operation activities and non-interference.
- ERX-REQ-PILOT-0002 — shadow-pilot comparison dimensions.
- ERX-REQ-HOMO-0001 — center homologation evidence set.
- ERX-REQ-HOMO-0002 — additional-center admission evidence and governance.
- ERX-REQ-RECV-0001 — JSON 01 reception fields.
- ERX-REQ-CONTACT-0002 — contact outcome cases and prohibition on fabricated attention.
- ERX-REQ-TIME-0001 — distinct timestamp categories.

These lists may be one schema, test program, verification output or acceptance condition; they must not be split mechanically without checking the source's intended acceptance boundary.

## 4. Potential overlap groups

The register flags these groups; no merge or duplicate decision is made here.

| Group | Candidate IDs |
|---|---|
| OV-UTXO-DOUBLE-SPEND | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010; ERX-REQ-UTXO-0011 |
| OV-UTXO-IDEMPOTENCY | ERX-REQ-UTXO-0005; ERX-REQ-UTXO-0009 |
| OV-UTXO-ATOMIC-ADMISSION | ERX-REQ-UTXO-0007; ERX-REQ-UTXO-0009; ERX-REQ-UTXO-0013 |
| OV-OTS-NONBLOCKING | ERX-REQ-UTXO-0008; ERX-REQ-UTXO-0012 |
| OV-OTS-LIFECYCLE | ERX-REQ-OTS-0001; ERX-REQ-OTS-0002; ERX-REQ-OTS-0003 |
| OV-VERIFIER-OUTPUT | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0003; ERX-REQ-VERIFY-0005 |
| OV-IDENTITY-SEPARATION | ERX-REQ-AGENT-0001; ERX-REQ-AGENT-0003; ERX-REQ-INST-0002; ERX-REQ-IDENT-0002 |
| OV-TELEPHONE-CONTINUITY | ERX-REQ-OPS-0001; ERX-REQ-OPS-0004 |

Shared subject does not establish duplication. The final decision must distinguish principle, implementation constraint, lifecycle detail and verification condition.

## 5. Validation

- 107 rows; 14 columns.
- 107 unique individual identifiers.
- Every row contains a parent candidate ID, statement, source ID/version, locator, origin, lifecycle and approval state.
- All rows remain EXTRACTED / CANDIDATE — REVIEW PENDING / NOT_APPROVED.
- No source candidate was silently discarded, merged, rejected or superseded.

## 6. Remaining acceptance work

Activity 0.7.3 remains IN_REVIEW until:
1. all 18 structured records receive an explicit atomicity disposition;
2. all eight overlap groups receive a documented distinct/refinement/duplicate-candidate disposition;
3. disputed decompositions and relationships are checked against exact source clauses/diagrams;
4. all 82 source candidates reconcile to the identification register without missing or orphaned parents;
5. a final structural and referential audit is recorded.

No work from activities 0.7.4–0.7.11 is performed or approved by this record.

---
End of record.
