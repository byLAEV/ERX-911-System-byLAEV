# ERX-WP-0.7-OPEN-DECISION-CANDIDATES-001
## Preliminary decision candidates identified during requirements review

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-OPEN-DECISION-CANDIDATES-001 |
| Version | 0.1.0 |
| Status | PRELIMINARY CANDIDATE LIST — NOT ADRs / NOT APPROVED |
| Date | 2026-11-25 |
| Work Package | WP-0.7 activity 0.7.8 |
| Intended downstream use | WP-0.8 Architecture Decision Register, after dependency release |

## 1. Purpose and boundary

This document records unresolved choices exposed by the 56-candidate requirements review. It does not decide them, select an architecture, create adopted ADRs, or start WP-0.8. Candidate IDs are stable references for review; they are not approved decision-register IDs unless formally adopted by the WP-0.8 method.

A candidate may be split, merged, deferred or rejected only through a recorded review disposition. The absence of an answer is not permission to infer one.

## 2. Preliminary decision candidates

| Candidate ID | Decision question | Affected requirements | Source basis / locator | Alternatives known from source | Consequence if unresolved |
|---|---|---|---|---|---|
| DCC-001 | What is the authorized coordination domain and authority for consuming an institutional UTXO, especially when more than one center participates? | ERX-REQ-UTXO-0001, 0003, 0004, TRANS-0001, TRANS-0002 | ERX-PROT-001 v1.1 §§2.1–2.2, Step 19; ERX-ROADMAP-001 v1.0 §8.2 | Coordination within an authorized installation/group; distributed transaction coordination; delegated transition authority. The Roadmap identifies the latter two as possibilities, not a selection. | Cannot prove single consumption across a multi-center call or assign conflict resolution authority. |
| DCC-002 | What are the approved communication and agent-availability state vocabularies, transitions and authorities? | ERX-REQ-STATE-0001, STATE-0002, AVAIL-0001, AVAIL-0002, AVAIL-0003, CLOSE-0001 | ERX-ROADMAP-001 v1.0 §§1.2–1.5, §3.1; UTXO-911-001 v1.0 §§5–8 | Roadmap lists provisional states and explicitly reserves definitive names/transitions for protocol approval. | Transition specifications and test oracles cannot be finalized. |
| DCC-003 | Which event identity, idempotency key, deduplication retention and atomic persistence boundary are authoritative? | ERX-REQ-UTXO-0003, 0005, 0007, 0009, 0010, OPS-0002, OPS-0006 | ERX-PROT-001 v1.1 §§2.1–2.2, §§10.1–10.6, §16.9 | Source lists required properties and possible concurrency mechanisms but does not select a database or mechanism. | Replay, concurrent consumption and recovery behavior remain underspecified. |
| DCC-004 | Which canonicalization profile, document/hash boundary and signature algorithm/format are adopted? | ERX-REQ-UTXO-0006, CRYPTO-0001, CRYPTO-0002, DATA-0001 | ERX-PROT-001 v1.1 p.10; ERX-ROADMAP-001 v1.0 §§2.1–2.4 | RFC 8785 or a formally specified compatible alternative; signature algorithm and document/transition separation remain to be defined. | Independent implementations may produce incompatible hashes, signatures or document references. |
| DCC-005 | What are the institutional key custody, rotation, revocation, recovery and historical-validation policies? | ERX-REQ-KEY-0001, KEY-0002, CRYPTO-0001, INST-0002, SEC-0001 | ERX-PROT-001 v1.1 §§4.1–4.2, §17.3; ERX-ROADMAP-001 v1.0 §2.3 | Institution-controlled private keys; hardware protection is recommended where available; detailed mechanisms not selected. | Historical signature validity and authorized signing cannot be consistently determined. |
| DCC-006 | What persistence, backup, local queue, recovery and reconciliation guarantees must be measured and accepted? | ERX-REQ-OPS-0001, OPS-0002, OPS-0004, OPS-0005, OPS-0006, INV-0004, INV-0005 | ERX-PROT-001 v1.1 §§16.8–16.9, §17.1–17.2; ERX-ROADMAP-001 v1.0 §1.5; UTXO-911-001 v1.0 §§5–6 | Durable protected local queue where technically possible; persistence confirmation; recovery/reconciliation required. Numeric RPO/RTO/durability targets are not specified in these sources. | Cannot establish measurable recovery acceptance or rule out rollback/resurrection. |
| DCC-007 | What OTS lifecycle transitions, retry/update policy, failure semantics, retention and final verification rules apply? | ERX-REQ-UTXO-0008, UTXO-0012, OTS-0001, OTS-0002 | ERX-PROT-001 v1.1 Step 8; ERX-ATLAS-001 v1.1 Lámina 06; UTXO-911-001 v1.0 §7 | Evidence may remain pending/updatable and complete later; emergency service must not be blocked. Exact retry/finality profile is not selected. | Temporal evidence may be misreported or unavailable for reproducible verification. |
| DCC-008 | Which jurisdiction-specific rules govern recording, privacy, retention, access, disclosure and deletion? | ERX-REQ-PRIV-0001, PRIV-0002, INST-0001, INST-0003 | ERX-PROT-001 v1.1 §§4, Step 18; ERX-ATLAS-001 v1.1 Lámina 08 | Institutional authorization and custody; public commitments limited to verification needs. Applicable legal rules depend on jurisdiction and must be sourced separately. | Recording or disclosure could occur without an established institutional/legal basis. |
| DCC-009 | What independence boundary, trust roots, evidence package and result semantics are required for the external verifier? | ERX-REQ-VERIFY-0001 through VERIFY-0005 | ERX-PROT-001 v1.1 §7; ERX-ROADMAP-001 v1.0 §7; ERX-ATLAS-001 v1.1 pp.27–28 | Verifier operates on exported evidence without direct production DB access and with sufficient independence; concrete separation is not selected. | A producer-side compromise may undermine the audit or produce ambiguous outcomes. |
| DCC-010 | Which schemas, versioning rules, adapter contracts and transfer protocol fields are normative and how are they validated? | ERX-REQ-DATA-0001, INT-0001, TRANS-0001, TRANS-0002, ARCH-0001, ARCH-0002 | ERX-ROADMAP-001 v1.0 §§2.1, 8.1–8.2; ERX-PROT-001 v1.1 §§4.3, 19 | Formal schemas and adapter contracts are required; transfer coordination may use distributed transaction coordination or delegated authority. | Integrations may diverge or produce incompatible transitions and evidence. |

## 3. Candidate control

- Total preliminary decision candidates: 10.
- Adopted decisions: 0.
- Rejected decisions: 0.
- Superseded decisions: 0.
- Each candidate requires WP-0.8 review for context, alternatives, rationale, consequences, source authority, owner and decision status.
- Legal/regulatory decisions require jurisdiction-specific authoritative sources; no legal rule is inferred here.
- Quantitative performance, capacity, latency and recovery thresholds are not invented. If needed, they must be proposed, justified and approved through the proper decision process.

## 4. Next actions within WP-0.7

1. Validate that each candidate is a true unresolved choice rather than a requirement that can be specified directly from an approved source.
2. Add exact source passage locators and any relevant source conflict references.
3. Link each candidate to the requirement records it affects.
4. Identify decision authority and required-by milestone where known; otherwise retain NOT_ASSIGNED / TBD.
5. Transfer these candidates into the WP-0.8 decision register only after WP-0.7 acceptance and WP-0.8 initiation.

---
End of ERX-WP-0.7-OPEN-DECISION-CANDIDATES-001
