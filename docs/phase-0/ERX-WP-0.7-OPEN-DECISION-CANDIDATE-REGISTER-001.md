# ERX-WP-0.7-OPEN-DECISION-CANDIDATE-REGISTER-001
## Requirements-Linked Decision Candidates — Phase 0

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-OPEN-DECISION-CANDIDATE-REGISTER-001 |
| Version | 0.1.0 |
| Status | WORKING REGISTER — LAEV DECISION REQUIRED WHERE INDICATED |
| Work Package | WP-0.7 / Activities 0.7.7–0.7.9 |
| Date | 2026-11-25 |
| Basis | ERX-ROADMAP-001 v1.0; ERX-PROT-001 v1.1; ERX-ATLAS-001 v1.1; UTXO-911-001 v1.0; approved WP-0.3 dispositions |

## 1. Purpose and boundary

This register identifies decisions that must not be silently settled during requirements extraction. It is a candidate decision inventory, not an ADR approval, source amendment, or technical authorization. Existing approved WP-0.3 dispositions remain controlling; this register does not reopen them.

## 2. Decision candidates

| Candidate ID | Question requiring decision/specification | Source / requirement links | Current evidence-based state | Required handling |
|---|---|---|---|---|
| ERX-DEC-CAND-001 | What are the definitive states, transition names and transition guards for the communication state machine? | Roadmap pp.6–8; ERX-REQ-STATE-0001/0002 | Roadmap lists provisional states and says final names/transitions require protocol approval. | Specify complete state/transition table; obtain protocol approval before normative baseline. |
| ERX-DEC-CAND-002 | What are the definitive states, authorities, release and recovery rules for the independent agent-availability cycle? | DOC-ISS-010; Roadmap pp.6–8; ERX-REQ-AVAIL-0001/0002; ERX-REQ-STATE-0001 | Independent cycle is accepted; detailed machine is deferred. | Preserve separation from communication UTXO lifecycle; specify authority, busy/paused, release, timeout and recovery semantics. |
| ERX-DEC-CAND-003 | What exact fields belong to event documents versus transactional UTXO records, and how are they linked without circular hashes/signatures? | Roadmap pp.6, 10; ERX-REQ-UTXO-0002; ERX-REQ-CRYPTO-0002 | Roadmap says this distinction must be determined and recommends separating the records. No approved schema decision is evidenced here. | Produce field ownership and dependency graph; distinguish requirement from recommendation; approve through controlled decision. |
| ERX-DEC-CAND-004 | Which signature algorithm, format, trust-chain model, revocation and rotation policy are approved? | Roadmap p.10; ERX-REQ-CRYPTO-0001; ERX-REQ-KEY-0001/0002 | Roadmap lists required specification topics and suggests protected key storage; it does not select an algorithm. | Compare options, document constraints and test vectors; no algorithm assumed. |
| ERX-DEC-CAND-005 | What is the authoritative coordination model for two centers attempting incompatible transitions or transferring a call? | DOC-ISS-010; Roadmap pp.8, 23–24; ERX-REQ-TRANS-0001/0002 | Roadmap identifies conflict and transfer cases; distributed coordination or delegated transition authority are alternatives, not a selected model. | Define authority boundary, failure behavior and reconciliation; do not assume ordinary database synchronization is sufficient. |
| ERX-DEC-CAND-006 | What is the detailed recovery/reconciliation procedure that prevents old backups from resurrecting consumed states or revoked credentials? | Roadmap p.8; ERX-REQ-INV-0004; ERX-REQ-UTXO-0004/0010 | Invariant is source-derived; mechanism and evidence remain unspecified. | Specify monotonicity/reconciliation evidence and adversarial restore tests before implementation. |
| ERX-DEC-CAND-007 | What independence boundary, trust anchors and export contract are required for the external verifier? | Roadmap pp.21–22; ERX-REQ-VERIFY-0001/0002/0003/0004 | Independent verification is required; sufficient independence and report schema need operational definition. | Define threat model, dependencies, inputs, trust roots and result semantics; validate in isolated environment. |
| ERX-DEC-CAND-008 | What is the operational status and completion path of ERX-CONSENSUS-001 v0.1 before any multi-institutional use? | DOC-ISS-011; Roadmap p.29 | Source is a proposal for review with important operational rules left open; it is not an approved operational consensus. | Retain proposal status; define missing rules and approval gate before multi-institutional use. |

## 3. Existing approved dispositions not reopened

- DOC-ISS-009 remains CLOSED under DP-02: acceptance is an authenticated, uniquely identified event/sub-state in the atomic UTXO 01→02 transition, not a fourth spendable output in the approved profile.
- DOC-ISS-010 remains DEFERRED under DP-03: independent agent-availability cycle accepted; detailed state machine deferred.
- DOC-ISS-011 remains DEFERRED under DP-08: consensus proposal is not an approved operational consensus.
- DOC-ISS-003 remains an accepted bounded source-location limitation; no content of ERX-IMPL-PROPOSAL-001 is inferred.

## 4. Control rules

1. No candidate in this register is an approved design decision.
2. Do not convert a Roadmap recommendation into a binding requirement without the appropriate approval.
3. A requirement may be valid while its implementation choice remains undecided.
4. Decisions affecting double-spend prevention, institutional authority, emergency continuity, privacy, evidence integrity or recovery require explicit evidence and approval.
5. When WP-0.8 is opened under its own gate, decision candidates may be converted into controlled ADRs; until then, this register preserves the open questions and their requirement links.

---
End of ERX-WP-0.7-OPEN-DECISION-CANDIDATE-REGISTER-001
