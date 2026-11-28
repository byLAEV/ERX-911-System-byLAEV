# ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001
## Requirements Requiring Further Specification

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001 |
| Version | 0.4.1 |
| Status | RECONCILED GAP REGISTER — 82-CANDIDATE COVERAGE; CLOSURE OPEN |
| Work Package | WP-0.7 / Activity 0.7.7 |
| Date | 2026-11-25 |
| Source register | registers/requirements-traceability.csv |

## 1. Purpose

This register captures specification gaps that prevent a candidate requirement from being fully verifiable or safely allocated. It does not resolve the gaps or make design decisions. Requirement IDs remain unchanged.

## 2. Reconciled coverage and gap dispositions

The current canonical source register contains 82 candidates (26 columns; CSV blob SHA `1b1bd462b916ea1fbca9ba9449a8114e13011761`). This register is synchronized to that snapshot.

The gap inventory has **76 open specification gaps** and **6 candidate-level NO_GAP_WITH_EVIDENCE dispositions**, covering all 82 source candidates. This is candidate-level coverage only; the six no-gap findings do not waive individual-record, source-fidelity or later design review. The 76 gaps remain OPEN and require owner, applicability, closure evidence and approval.

The table below records individual gaps. Supplemental gap rows added after the earlier 63-row snapshot are part of the current 76-gap count; the earlier statement “63 gaps / 19 unassessed” is historical and superseded. No candidate is now classified UNASSESSED solely because it was absent from the earlier 63-row table.

## 3. Cross-cutting gaps requiring coordinated treatment

1. State machines: final communication state names, transitions, guards, authority, failure and recovery rules.
2. Agent availability: independent lifecycle, release authority, busy/paused semantics and recovery.
3. Transactional atomicity: storage boundary, concurrency control, idempotency, conflict result and crash recovery.
4. Data model: event-document versus UTXO-transition fields, canonicalization and non-circular cryptographic linkage.
5. Cryptography: signature algorithm/format, trust chain, key rotation/revocation and historical validation.
6. Interinstitutional coordination: transfer authority, incompatible transitions, interruption and reconciliation.
7. Independent verifier: trust anchors, export contract, dependency isolation and result semantics.
8. OTS: proof states, retries, update/verification behavior and non-blocking call-critical operation.
9. Privacy/custody: original-file location, access, retention, deletion and recovery rules.
10. Testing/acceptance: test vectors, twenty referenced protocol tests, numeric performance targets and discrepancy thresholds.

## 4. Control

A gap is closed only when its missing parameter is specified by an authorized source or approved decision and the requirement's verification criterion can be evaluated. If closure depends on an open decision, link the decision candidate; do not invent a value. Numeric targets remain TBD until authorized.

---
End of ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001


## 3. Coverage-control requirement

For each of the 19 currently unrepresented source candidates, record one of:
- GAP_IDENTIFIED (add a traceable row),
- NO_GAP_WITH_EVIDENCE (cite why current approved specification is sufficient),
- NOT_ASSESSED (retain open WP-0.7 status),
- BLOCKED_BY_DECISION (link an open decision candidate).

Do not close a gap solely because the candidate has a verification proposal or phase assignment. Child-level applicability must preserve the parent link and avoid duplicate gap records where a parent gap applies to multiple children.

---
End of reconciled gap register.



## 3. Disposition of the 19 previously unrepresented candidates

A source/criterion-level first-pass disposition has now been recorded for all 19 candidates. Thirteen are added as specification gaps; six have a documented NO_GAP_WITH_EVIDENCE decision at this candidate level. A NO_GAP decision does not waive parent/child review or future design decisions.

### 3.1 GAP_IDENTIFIED — 13 candidates

| Requirement ID | Source locator | Missing specification | Closure evidence |
|---|---|---|---|
| ERX-REQ-TEST-0001 | ERX-ROADMAP-001 PDF p.14 §4.1 | Simulator fixtures, event inputs, expected state outputs, reproducibility and failure paths are not fully specified. | Approved simulator scenario catalogue, fixture format, expected outputs and repeatable execution evidence. |
| ERX-REQ-TEST-0004 | ERX-ROADMAP-001 PDF p.24 §9.1; ERX-PROT-001 §19.1 | Roadmap references twenty mandatory tests but the requirement record does not yet map each source test to a named test case, preconditions, expected result and evidence. | Exact extraction of all twenty ERX-PROT-001 §19.1 tests and traceable test-case mapping. |
| ERX-REQ-RECV-0001 | ERX-PROT-001 PDF p.8 Step 1 | The source lists reception fields but does not fully define field types, required/conditional presence, canonical schema version or unavailable-value representation. | Approved JSON 01 schema and positive/negative validation vectors. |
| ERX-REQ-LOC-0001 | ERX-PROT-001 PDF p.9 Step 4 | Location provenance fields and states are listed, but coordinate reference, precision semantics, source taxonomy and validation-state transition rules are not fully defined. | Approved location data schema, state vocabulary and source/precision semantics. |
| ERX-REQ-CORR-0001 | ERX-PROT-001 PDF p.18 §10.9; pp.21–22 §14 | Correction flow is defined, but the complementary-document schema, signer/authorizer authority and multi-correction linkage rules need formal specification. | Correction/addendum schema, authority matrix and chain-reconstruction rules. |
| ERX-REQ-TIME-0001 | ERX-PROT-001 PDF p.18 §11 | Seven distinct time concepts are listed, but field-level schema, event applicability and ordering rules are not completely defined. | Versioned time-field schema and event applicability/ordering table. |
| ERX-REQ-TIME-0002 | ERX-PROT-001 PDF p.19 §11 | UTC, precision, source and monotonic time are required, but allowed precision, source authority, monotonic-clock scope and discrepancy handling need specification. | Time-source policy, precision model and discrepancy-record schema; no invented tolerance. |
| ERX-REQ-OTS-0003 | ERX-PROT-001 PDF pp.19–20 §12 | The evidence workflow is enumerated, but state transitions, canonicalization/signature dependencies, proof storage, update triggers and verification package boundaries remain unspecified. | Approved OTS workflow/state model and proof-retention/update contract. |
| ERX-REQ-PRIV-0003 | ERX-PROT-001 PDF p.20 §13 | Protection objectives are stated, but encryption profiles, key lifecycle, access roles, audit events and custody boundaries are not specified. | Approved data-protection profile, key/access model and audit-control mapping. |
| ERX-REQ-PRIV-0004 | ERX-PROT-001 PDF p.21 §13.1 | High-entropy commitments/equivalent structures are required where applicable, but construction, entropy policy, metadata minimization and verification disclosure controls remain undefined. | Approved anti-correlation commitment design and privacy threat-model evidence. |
| ERX-REQ-PRIV-0005 | ERX-PROT-001 PDF p.21 §13.2 | The institution must define retention/deletion under applicable law, but jurisdictional periods, legal holds, deletion evidence and minimum retained metadata are not specified. | Jurisdiction-specific retention/deletion schedule and auditable deletion/anchor distinction. |
| ERX-REQ-OPS-0004 | ERX-PROT-001 PDF p.24 §16.10 | The non-blocking identity-outage behavior is explicit, but retry cadence, authoritative revalidation source, timeout handling and transition from pending to final status remain unspecified. | Identity-service outage/recovery state machine and authorized revalidation rules. |
| ERX-REQ-OPS-0005 | ERX-PROT-001 PDF p.24 §16.8 | Durable local queue behavior is conditional on technical feasibility; queue encryption, capacity, ordering, replay protection, reconciliation and overflow handling need specification. | Degraded-mode queue contract, persistence/replay/reconciliation policy and recovery evidence. |

### 3.2 NO_GAP_WITH_EVIDENCE — 6 candidates

| Requirement ID | Source locator | Disposition | Rationale |
|---|---|---|---|
| ERX-REQ-LOC-0002 | ERX-PROT-001 PDF p.9 Step 4 | NO_GAP_WITH_EVIDENCE | The source explicitly states that absent location does not block the call and later location changes are new events without modifying JSON 01. The candidate-specific criterion provides an observable test; additional location schema detail is tracked under LOC-0001. |
| ERX-REQ-CONTACT-0001 | ERX-PROT-001 PDF p.11 Step 10 | NO_GAP_WITH_EVIDENCE | The source explicitly distinguishes initial reception time from agent response time. The criterion requires distinct event fields; shared timestamp schema work is tracked under TIME-0001. |
| ERX-REQ-AGENT-0003 | ERX-PROT-001 PDF p.12 Step 11 | NO_GAP_WITH_EVIDENCE | The source explicitly lists validation outcomes and prohibits representing pending identity as verified while attention continues. Credential lifecycle detail is covered by existing INST/AGENT gaps. |
| ERX-REQ-CONTACT-0002 | ERX-PROT-001 PDF p.12 Step 13 | NO_GAP_WITH_EVIDENCE | The source enumerates the contact outcomes and explicitly prohibits inventing human attention. The candidate-specific outcome-model criterion is directly testable; no additional specification gap identified at this level. |
| ERX-REQ-OTS-0004 | ERX-PROT-001 PDF p.20 §12.3 | NO_GAP_WITH_EVIDENCE | The source explicitly lists the evidentiary limits of OTS. The candidate is treated as a proof-boundary/design constraint, not a mandatory system obligation; verifier-result detail is covered by VERIFY requirements. |
| ERX-REQ-BOUND-0001 | ERX-PROT-001 PDF p.28 §20 | NO_GAP_WITH_EVIDENCE | The source explicitly defines the non-substitution boundary and institutional independence. The candidate-specific architecture/governance review criterion is sufficient at this requirements-identification level. |

## 4. Coverage result and closure control

- Original detailed gap entries: 63.
- Additional gaps identified through this review: 13.
- **Total detailed specification gaps: 76 unique candidate IDs.**
- **NO_GAP_WITH_EVIDENCE: 6 candidate IDs.**
- Total source-candidate coverage: 82/82.
- No requirement ID was deleted, merged or renumbered.
- The 107 individual records still require parent/child applicability review; a parent-level gap must not be duplicated across children.
- Existing gaps remain OPEN until their specified closure evidence is produced and reviewed. The 13 added gaps are not resolved by being recorded.
- The six NO_GAP dispositions apply only to the stated candidate-level scope and may be reopened if child decomposition or source review reveals additional obligations.

Activity 0.7.7 can be treated as **recording coverage complete for the 82 source-candidate layer**, while the 76 specification gaps remain open work items. Formal activity acceptance and child-level applicability remain separate controls.




## 4. Version and authority control — 2026-11-28

The canonical CSV blob SHA above is the controlling row snapshot. The status reconciliation, current phase-allocation register and this gap register must be interpreted against it. A gap disposition is not requirement approval, implementation authorization or WP-0.7 acceptance.

The current 107 individually identified records require child-level applicability review against the 76 open parent/candidate gaps. Do not duplicate parent gaps as independent obligations without evidence.

---
End of reconciled gap register.
