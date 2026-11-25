# ERX-WP-0.7-CANDIDATE-REVIEW-001
## Preliminary Candidate Reconciliation Review

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-CANDIDATE-REVIEW-001 |
| Version | 0.1.0 |
| Status | PRELIMINARY REVIEW — NOT APPROVED |
| Work Package | WP-0.7 / Activities 0.7.3–0.7.4 |
| Date | 2026-11-25 |
| Register reviewed | registers/requirements-traceability.csv — 56 candidate records |
| Method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 |

## 1. Purpose and boundary

This review identifies overlaps, scope distinctions and classification inconsistencies among the 56 candidate records extracted in batches 001–004. It is a review aid only. It does not approve, reject, merge, withdraw, reclassify or reword any requirement. Original source wording and locators must be preserved when a disposition is later made.

## 2. Candidate overlap and relationship clusters

| Cluster | Candidate IDs | Preliminary finding | Required treatment |
|---|---|---|---|
| Single consumption and concurrency | ERX-REQ-UTXO-0003, UTXO-0010, UTXO-0011, UTXO-0004 | Related but not identical: prohibition on double consumption, concurrency enforcement, validation preconditions and scoped uniqueness mechanisms. | Compare source passages; retain distinct testable obligations or cross-link them. Do not collapse the source-specific conditions. |
| Retransmission, replay and recovery | ERX-REQ-UTXO-0005, UTXO-0009, OPS-0005 | Overlap around duplicate effects and idempotency, but different scopes: incoming retransmission, operation retry and recovery queue replay. | Define scope boundaries and common invariant; avoid counting one obligation multiple times. |
| OTS lifecycle and asynchronous evidence | ERX-REQ-UTXO-0008, UTXO-0012, OTS-0001, OTS-0002 | Related obligations for state reporting, non-blocking emergency care, retention of proofs and later completion. | Separate lifecycle states, operational non-interference and evidence-retention duties; link them. |
| Storage confirmation and recovery | ERX-REQ-OPS-0002, OPS-0006, OPS-0004, OPS-0005 | Storage confirmation, durable local queue, recovery processing and incident retention are connected but distinct. | Preserve each failure boundary; define exact persistence and recovery semantics later. |
| Privacy and institutional custody | ERX-REQ-PRIV-0001, PRIV-0002 | One addresses original audio and associated metadata; the other defines the broader private/public information boundary. | Link by data class; do not treat the broader boundary as a substitute for audio-specific custody requirements. |
| Verifier scope and limits | ERX-REQ-VERIFY-0001 through VERIFY-0005 | Includes exportability, result semantics, verification categories, independence and the distinction between cryptographic proof and material truth. | Build a verifier capability map; keep independence and truth-boundary obligations explicit. |
| Agent identity and availability | ERX-REQ-AGENT-0001, AGENT-0002, AVAIL-0001, AVAIL-0002, AVAIL-0003 | Identity verification, non-response handling, actual availability and separation of the agent cycle from the call cycle are different concerns. | Maintain separate identity, availability and communication state domains. |
| Inter-center transfer | ERX-REQ-TRANS-0001, TRANS-0002 | The first records transfer continuity and participants; the second requires authority, receipt, responsibility, interruption and reconciliation rules. | Treat as related requirements with a distinct unresolved multi-center authority problem. |
| Test coverage | ERX-REQ-TEST-0001, TEST-0002 | One states test categories; the other points to the twenty cases in ERX-PROT-001 §19.1. | Reconcile into a single coverage model without losing the source's explicit cases. |
| Architecture and state machines | ERX-REQ-ARCH-0001, ARCH-0002, STATE-0001, AVAIL-0003 | Common core/adapters, four-component package, separate communication and availability cycles. | Map component responsibilities separately from state-machine boundaries. |

## 3. Classification consistency finding

The controlled method defines one primary requirement type from its Section 5 taxonomy and permits optional secondary tags. The current CSV frequently stores multiple slash-separated values in the requirement_type field, and includes labels not present in the controlled taxonomy, such as TRANSACTIONAL, RECOVERY, CRYPTOGRAPHY, INTEGRITY, AUDITABILITY, RESILIENCE and QUALITY.

This is a register normalization issue, not evidence that the underlying source statements are invalid. Before activity 0.7.4 can be closed, each candidate must receive exactly one primary taxonomy type; any additional concern should be represented as a secondary tag or a controlled extension with an approved rationale. Do not silently add new taxonomy values.

## 4. Material boundaries that must remain explicit

1. **Local uniqueness versus multi-institutional uniqueness:** ERX-PROT-001 v1.1 p.3 scopes its uniqueness mechanisms to the authorized transactional coordination domain. ERX-ROADMAP-001 v1.0 pp.23–24 separately requires an inter-institutional transfer protocol and leaves the coordination mechanism to an approved model. A local atomic transaction must not be represented as a proven global uniqueness solution.
2. **Communication UTXO versus agent availability UTXO:** ERX-ROADMAP-001 v1.0 pp.4–5 and UTXO-911-001 v1.0 §§4.5–6 keep these cycles separate. UTXO 03 cannot substitute for agent availability.
3. **Emergency service versus external evidence:** OTS/Bitcoin evidence acquisition is asynchronous and must not delay or block reception, acceptance or attention.
4. **Cryptographic verification versus material truth:** ERX-ATLAS-001 v1.1 p.28 expressly limits what cryptographic evidence establishes.
5. **Event time versus later processing:** ERX-PROT-001 v1.1 p.25 distinguishes original event time, recovery time and commitment-generation time.
6. **Institutional software installation versus legal authority:** ERX-PROT-001 v1.1 §19.2 states that installation does not itself authorize an entity to receive emergency calls.

## 5. Open-decision candidates for later governance routing

These are unresolved decision topics, not approved decisions and not newly created ADRs:

- Authority and conflict resolution for a communication transferred between independent institutions.
- Scope and operational status of ERX-CONSENSUS-001 v0.1; it remains a proposal for review.
- Exact state model and transition authority for the independent agent-availability cycle.
- Canonicalization profile, signature algorithms/formats, key rotation and historical revocation validation.
- Jurisdiction-specific privacy, access, retention and disclosure rules.
- OTS proof retry, update, failure and finality semantics.
- Durability guarantees and capacity limits for local queues and backup/recovery.
- Quantitative acceptance thresholds for latency, recovery, loss, throughput and verifier completeness.
- Disposition of ERX-IMPL-PROPOSAL-001, still NOT_LOCATED / UNVERIFIED under DOC-ISS-003.

These topics should be linked to their source and issue references. WP-0.8 remains NOT_STARTED; this review does not initiate it.

## 6. Disposition

- Candidate count reviewed: 56.
- Candidate records approved by this review: 0.
- Candidate records rejected or withdrawn by this review: 0.
- Candidate merges executed: 0.
- Primary-type normalization: OPEN.
- Source locator and wording audit: OPEN.
- Phase allocation: UNALLOCATED_PENDING_WP-0.7.10.
- WP-0.7: IN_PROGRESS.
- Phase 0: OPEN.
- Phase 1: NOT AUTHORIZED.

---
End of ERX-WP-0.7-CANDIDATE-REVIEW-001