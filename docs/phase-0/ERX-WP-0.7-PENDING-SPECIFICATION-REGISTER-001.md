# ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001
## Requirements Requiring Further Specification

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001 |
| Version | 0.1.0 |
| Status | WORKING GAP REGISTER — REVIEW PENDING |
| Work Package | WP-0.7 / Activity 0.7.7 |
| Date | 2026-11-25 |
| Source register | registers/requirements-traceability.csv |

## 1. Purpose

This register captures specification gaps that prevent a candidate requirement from being fully verifiable or safely allocated. It does not resolve the gaps or make design decisions. Requirement IDs remain unchanged.

## 2. Candidate gaps

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
