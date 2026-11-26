# ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001
## Requirements Requiring Further Specification

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001 |
| Version | 0.4.0 |
| Status | WORKING GAP REGISTER — 82-CANDIDATE COVERAGE REVIEWED |
| Work Package | WP-0.7 / Activity 0.7.7 |
| Date | 2026-11-25 |
| Source register | registers/requirements-traceability.csv |

## 1. Purpose

This register captures specification gaps that prevent a candidate requirement from being fully verifiable or safely allocated. It does not resolve the gaps or make design decisions. Requirement IDs remain unchanged.

## 2. Candidate gaps

### Inventory reconciliation — 2026-11-25
The table below contains **63 unique candidate IDs with recorded specification gaps**. The canonical source register now has 82 candidates; therefore **19 candidate IDs are not represented in this gap table**. Their absence is NOT a determination that no specification gap exists: they remain UNASSESSED for this register until reviewed. The 107 individual records also require parent/child gap applicability review. This register is a gap list, not a completeness assertion.

| Requirement ID | Source locator | Missing specification / closure work | Closure evidence |
|---|---|---|---|
| ERX-REQ-UTXO-0001 | ERX-PROT-001 PDF p.3 | Define canonical consumed/successor state evidence and historical status semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0002 | ERX-PROT-001 PDF p.3, Section 2.1 | Specify required field set, uniqueness scope, canonical encoding and versioning. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0003 | ERX-PROT-001 PDF p.3, Section 2.1 | Specify atomicity boundary, concurrency model and conflict outcome. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0004 | ERX-PROT-001 PDF p.3, Section 2.2 | Specify monotonic recovery and authoritative state reconciliation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0005 | ERX-PROT-001 PDF p.4 | Specify idempotency key scope, retention and retry result behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0006 | ERX-PROT-001 PDF p.10 | Specify cryptographic linkage and event/transition document boundaries. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0007 | ERX-PROT-001 PDF p.10, Step 7 | Specify transaction commit/rollback and external service boundary. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0008 | ERX-PROT-001 PDF p.10, Step 8 | Define OTS state vocabulary, retry policy and non-blocking operation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0009 | ERX-PROT-001 PDF p.17, Sections 10.1–10.5 | Specify replay detection, duplicate handling and adversarial test vectors. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0010 | ERX-PROT-001 PDF p.17, Section 10.6 | Specify concurrency and recovery invariants and authoritative persistence semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0011 | UTXO-911-001 PDF p.10, Principle of single spend | Specify uniqueness boundary and input-consumption validation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0012 | UTXO-911-001 PDF p.11, OTS function | Define OTS proof lifecycle and evidence retention. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0001 | ERX-PROT-001 PDF p.25, Section 17.1 | Specify service continuity and degraded-mode behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0002 | ERX-PROT-001 PDF p.24, Section 16.9 | Define audit record structure, time source and chronology semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 PDF p.23, Section 8.1 | Specify adapter inputs/outputs, trust boundary and failure behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0001 | ERX-PROT-001 PDF pp.5–6, Section 4 | Specify authority registry, issuer trust and credential lifecycle. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0002 | ERX-PROT-001 PDF p.6, Section 4.1 | Define credential states and fail-closed behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0003 | ERX-PROT-001 PDF p.6, Section 4.1 | Define authoritative jurisdiction sources and update responsibility. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0001 | ERX-PROT-001 PDF p.6, Section 4.2 | Select key custody policy and approved controls; HSM remains recommendation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0002 | ERX-PROT-001 PDF p.7, Section 4.2 | Define historical key-status lookup and verifier trust data. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 PDF p.8, Section 4.3 | Specify core/adaptor authority boundary and non-overridable validation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PRIV-0001 | ERX-PROT-001 PDF pp.14–15, Step 18 | Define protected original-to-evidence linkage, access and retention. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 PDF pp.15–16, Step 19 | Specify transfer event identity, receiving authority and replay handling. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 PDF p.16, Step 20 | Define communication closure vs incident/intervention closure. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 PDF pp.21–23, Section 7 | Define export package contract and independent verification boundary. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 PDF p.24, Section 7.3 | Define verifier result vocabulary and missing-evidence behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 PDF pp.7–8, Lámina 03 | Specify independent center/agent credential and availability state semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 PDF p.8, Lámina 03 | Define non-response handling and prohibited false event creation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 PDF p.19, Lámina 06 | Define pending/submitted/anchored/failed evidence states and proof semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 PDF pp.27–28, verifier categories | Specify category checks, report schema and non-success outcomes. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0003 | UTXO-911-001 PDF p.7, Section 4.2 | Define separate session and incident lifecycles. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AVAIL-0001 | UTXO-911-001 PDF pp.9–10, availability lifecycle | Specify agent availability state machine, issuance guards and release authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AVAIL-0002 | UTXO-911-001 PDF pp.9–11, Sections 5–8 | Specify separate agent-availability UTXO and communication UTXO models. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-STATE-0001 | ERX-ROADMAP-001 PDF pp.6–7, Sections 1.2–1.3 | Approve final state names and transitions; source says these require protocol approval. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-STATE-0002 | ERX-ROADMAP-001 PDF p.7, Section 1.3 | Specify transition table fields, authorization, guards and failure behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0001 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify terminal-state transition guards. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0002 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify correction/addendum model without mutation of sealed source evidence. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0003 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify minimum provenance/audit fields and reconstruction test. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0004 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify rollback/recovery monotonicity and credential revocation persistence. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-DATA-0001 | ERX-ROADMAP-001 PDF p.9, Section 2.1 | Define formal schemas, versions, required fields and validation vectors. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CRYPTO-0001 | ERX-ROADMAP-001 PDF p.10, Section 2.3 | Algorithm and signature format remain an open decision; do not select by inference. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CRYPTO-0002 | ERX-ROADMAP-001 PDF p.10, Section 2.4 | Define acyclic canonicalization/hash/signature dependency graph. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0004 | ERX-ROADMAP-001 PDF p.21, Section 7 | Specify verifier independence, trust roots and shared dependency threat model. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TRANS-0002 | ERX-ROADMAP-001 PDF pp.23–24, Section 8.2 | Specify multi-center transfer protocol and reconciliation authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-ARCH-0002 | ERX-ROADMAP-001 PDF pp.11–12, §3.1 | Define component responsibilities, interfaces, trust boundaries and privilege separation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0013 | ERX-ROADMAP-001 PDF pp.12–13, §3.3 | Define transaction boundary and failure atomicity; OTS remains outside call-critical transaction. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CORE-0001 | ERX-ROADMAP-001 PDF p.14, opening paragraph | Define measurable core readiness gate before telephone/OTS integration. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CORE-0002 | ERX-ROADMAP-001 PDF p.14, §4.1 | Specify module boundaries, interfaces and ownership of listed responsibilities. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0002 | ERX-ROADMAP-001 PDF pp.14–15, §§4.3 | Define simulator fixtures, event sequence, assertions and reproducible output. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0003 | ERX-ROADMAP-001 PDF p.15, §4.4 | Define fault injection, concurrency test fixtures and expected recovery behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-IDENT-0001 | ERX-ROADMAP-001 PDF p.16, §5.1 | Define identity record schemas, issuer relations and authorization model. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-IDENT-0002 | ERX-ROADMAP-001 PDF pp.16–17, §5.2 | Define credential state machine and validation source semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0003 | ERX-ROADMAP-001 PDF p.17, §5.3 | Define full key lifecycle policy; do not imply a specific hardware technology. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-SEC-0001 | ERX-ROADMAP-001 PDF pp.17–18, §§5.4 and deliverables | Select algorithms, policy parameters and control evidence for each interface safeguard. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OTS-0002 | ERX-ROADMAP-001 PDF pp.18–19, §6.1 | Define canonicalization, document versioning, proof update and verification semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PRIV-0002 | ERX-ROADMAP-001 PDF p.20, §6.4 | Define custody locations, access, retention, recovery and deletion rules. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0005 | ERX-ROADMAP-001 PDF p.21, §7.1 | Define export verifier schema and deterministic outcome semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INT-0002 | ERX-ROADMAP-001 PDF p.22, opening of Phase 8 | Define integration gate evidence and authorization authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0005 | ERX-ROADMAP-001 PDF p.25, §9.3 | Set numeric thresholds and measurement methods before executing tests; values not specified in extraction. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PILOT-0001 | ERX-ROADMAP-001 PDF pp.26–27, §§10.1–10.2 | Define shadow-pilot permissions, event feed and no-interference safeguards. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PILOT-0002 | ERX-ROADMAP-001 PDF p.27, §10.3 | Define discrepancy classification, severity and reporting thresholds. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-HOMO-0001 | ERX-ROADMAP-001 PDF p.28, §11.1 | Define homologation dossier evidence and distinguish technical homologation from legal authorization. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-HOMO-0002 | ERX-ROADMAP-001 PDF pp.28–29, §11.2 | Define multi-center onboarding evidence and institution approval gate. | Approved specification, decision record or testable criterion linked to this requirement |

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


