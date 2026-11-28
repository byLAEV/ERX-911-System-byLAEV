# ERX-WP-0.7.8-OPEN-DECISION-REVIEW-001

Version: 0.1.0  
Date: 2026-11-25  
Status: REVIEW COMPLETED — READY FOR LAEV ACCEPTANCE; NOT APPROVED  
Work Package: WP-0.7 / Activity 0.7.8

## Purpose
Review the completeness of the eight decision candidates recorded in `docs/phase-0/ERX-WP-0.7-OPEN-DECISION-CANDIDATE-REGISTER-001.md`. This review records questions; it does not resolve them, approve architecture, or create approved ADRs.

## Reviewed candidates

| ID | Open question | Evidence / links | Handling |
|---|---|---|---|
| ERX-DEC-CAND-001 | Definitive communication state machine states, transitions and guards | Roadmap pp. 6–8; ERX-REQ-STATE-0001/0002 | Specify transition table and obtain protocol approval |
| ERX-DEC-CAND-002 | Independent agent-availability cycle states, authority, release and recovery | DOC-ISS-010; Roadmap pp. 6–8; ERX-REQ-AVAIL-0001/0002; ERX-REQ-STATE-0001 | Preserve independence from communication UTXO lifecycle; specify detailed machine |
| ERX-DEC-CAND-003 | Event-document fields vs transactional UTXO fields and non-circular cryptographic linkage | Roadmap pp. 6, 10; ERX-REQ-UTXO-0002; ERX-REQ-CRYPTO-0002 | Define field ownership and dependency graph; distinguish requirement from recommendation |
| ERX-DEC-CAND-004 | Signature algorithm, format, trust chain, revocation and rotation | Roadmap p. 10; ERX-REQ-CRYPTO-0001; ERX-REQ-KEY-0001/0002 | Compare options and test vectors; no algorithm assumed |
| ERX-DEC-CAND-005 | Coordination authority for conflicting center transitions and transfers | DOC-ISS-010; Roadmap pp. 8, 23–24; ERX-REQ-TRANS-0001/0002 | Define authority boundary, failure behavior and reconciliation |
| ERX-DEC-CAND-006 | Recovery/reconciliation against stale backups and revoked credentials | Roadmap p. 8; ERX-REQ-INV-0004; ERX-REQ-UTXO-0004/0010 | Specify monotonicity evidence and adversarial restore tests |
| ERX-DEC-CAND-007 | External verifier independence, trust anchors and export contract | Roadmap pp. 21–22; ERX-REQ-VERIFY-0001/0002/0003/0004 | Define threat model, dependencies, inputs, trust roots and result semantics |
| ERX-DEC-CAND-008 | Status and completion path of ERX-CONSENSUS-001 v0.1 | DOC-ISS-011; Roadmap p. 29 | Keep proposal status; define missing rules and approval gate before multi-institutional use |

## Completeness review

All eight entries have a distinct candidate ID, a decision question, source and/or requirement links, an evidence-based current state in the controlling candidate register, and a required handling path. No candidate is marked resolved. No technical option is selected by this review.

## Existing dispositions not reopened

- DOC-ISS-009 / DP-02 remains CLOSED: acceptance is an authenticated, uniquely identified event/sub-state in the atomic UTXO 01→02 transition, not a fourth spendable output in the approved profile.
- DOC-ISS-010 / DP-03 remains DEFERRED: independent agent-availability cycle accepted; detailed state machine deferred.
- DOC-ISS-011 / DP-08 remains DEFERRED: consensus proposal is not an approved operational consensus.
- DOC-ISS-003 remains an accepted bounded source-location limitation; no content of ERX-IMPL-PROPOSAL-001 is inferred.

## Boundary and recommendation

The eight entries remain decision candidates, not approved ADRs. Their conversion into controlled ADRs and technical approval belongs to WP-0.8 under its own dependency and initiation gate. No implementation choice is authorized here.

**Review result:** the candidate inventory is complete for the recording purpose of Activity 0.7.8. Recommend marking 0.7.8 ready for LAEV acceptance, provided LAEV confirms that the activity records open decisions rather than resolving them. Until express acceptance is recorded, Activity 0.7.8 remains not formally COMPLETED.
