# ERX-WP-0.7-INITIAL-REQUIREMENT-EXTRACTION-001
## First Controlled Extraction Batch — Source-Derived Candidates

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-INITIAL-REQUIREMENT-EXTRACTION-001 |
| Version | 0.1.0 |
| Status | EXTRACTED — TECHNICAL REVIEW PENDING |
| Work Package | WP-0.7 / Activities 0.7.2–0.7.9 |
| Date | 2026-11-25 |
| Source inspection | ERX-WP-0.7-SOURCE-INSPECTION-RECORD-001 v1.0.0 |
| Requirements method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 |

## 1. Extraction rule

This first batch records candidate requirements from explicit normative statements in the five directly inspected foundational PDFs. Statements are summarized faithfully and retain source modality and scope. They are **EXTRACTED — REVIEW PENDING**, not approved requirements. The CSV contains the stable IDs, classifications, source locators, verification gaps and current status.

The technical response (FND-005) is treated as a review/recommendation source, not as an independently normative source. It is not used to strengthen a requirement's modality.

## 2. First batch

| Requirement ID | Candidate statement | Source locator | Type |
|---|---|---|---|
| ERX-REQ-UTXO-0001 | A valid transition consumes a prior state and creates the next; consumed state is unavailable for another transition but remains in institutional history. | ERX-PROT-001 v1.1, PDF p.3 | FUNCTIONAL / DATA_AND_RECORDS |
| ERX-REQ-UTXO-0002 | Each institutional UTXO must carry a unique state ID, call ID, stage ID, document cryptographic reference, prior-state reference when applicable, consumption state, process identity, observation/processing times and institutional operation signature. | ERX-PROT-001 v1.1, PDF p.3 | DATA_AND_RECORDS / SECURITY |
| ERX-REQ-UTXO-0003 | The implementation must prevent two processes from consuming the same valid state. | ERX-PROT-001 v1.1, PDF p.3 | SECURITY / TRANSACTIONAL |
| ERX-REQ-UTXO-0004 | Within the authorized coordination scope, uniqueness must be supported by persistent event identity, storage uniqueness constraints, atomic operations, concurrency control, idempotency, transition history and safe recovery. | ERX-PROT-001 v1.1, PDF p.3 | ARCHITECTURAL / SECURITY |
| ERX-REQ-UTXO-0005 | A retransmitted telephone event must not produce duplicate institutional effects. | ERX-PROT-001 v1.1, PDF p.4 | FUNCTIONAL / SECURITY |
| ERX-REQ-UTXO-0006 | Canonicalization must use a documented specification such as RFC 8785 or a formally specified compatible alternative; the institutional document is signed with an authorized institutional key. | ERX-PROT-001 v1.1, PDF p.10 | SECURITY / DATA_AND_RECORDS |
| ERX-REQ-UTXO-0007 | Creation of UTXO 01 must link the state to the original event and a uniqueness rule, and must be atomic. | ERX-PROT-001 v1.1, PDF p.10 | TRANSACTIONAL / FUNCTIONAL |
| ERX-REQ-UTXO-0008 | OTS evidence states must distinguish not requested, sent, pending, updatable, anchored, verified and failed; emergency service continues independently of OTS confirmation. | ERX-PROT-001 v1.1, PDF p.10 | DATA_AND_RECORDS / OPERATIONAL |
| ERX-REQ-UTXO-0009 | Every call event must receive a persistent identity; retransmission must not create a new admission; consumption and state creation must be atomic; retries must return the original operation result when applicable. | ERX-PROT-001 v1.1, PDF p.17 | SECURITY / TRANSACTIONAL |
| ERX-REQ-UTXO-0010 | Concurrent processes must not complete two valid transitions against the same state; storage must implement verifiable concurrency constraints. | ERX-PROT-001 v1.1, PDF p.17 | SECURITY / PERFORMANCE_AND_CAPACITY |
| ERX-REQ-UTXO-0011 | A valid UTXO may be consumed only once; the transition validator checks input existence, current validity, operator authorization and absence of prior consumption; update is atomic. | UTXO-911-001 v1.0, PDF p.10 | FUNCTIONAL / SECURITY |
| ERX-REQ-UTXO-0012 | OTS proof acquisition may finish later and must not delay or block emergency reception, acceptance or attention. | UTXO-911-001 v1.0, PDF p.11 | OPERATIONAL / INTERFACE |
| ERX-REQ-OPS-0001 | ERX failure must not prevent the institution from receiving and attending calls through its official telephone infrastructure. | ERX-PROT-001 v1.1, PDF p.25 | OPERATIONAL / RESILIENCE |
| ERX-REQ-OPS-0002 | An event must not be represented as permanently recorded until storage confirmation exists. | ERX-PROT-001 v1.1, PDF p.24 | DATA_AND_RECORDS / OPERATIONAL |
| ERX-REQ-INT-0001 | Each institutional adapter must specify inputs, outputs, authentication, errors, retries and duplicate handling. | ERX-ROADMAP-001 v1.0, PDF p.23 | INTEROPERABILITY / INTERFACE |

## 3. Review and assignment state

- All 15 entries are EXTRACTED from the cited source statements; technical review and LAEV approval remain pending.
- Verification criteria are marked NOT_DEFINED until the relevant design/test method is specified.
- Phase assignment remains UNALLOCATED_PENDING_WP-0.7.10; no implementation phase is inferred from source location alone.
- Priority, owner and approval references remain NOT_ASSIGNED / NOT_APPROVED.
- These entries do not resolve multi-institutional coordination, consensus, transfer authority, privacy/legal retention, or other open decisions. Related sources and issues must be linked as the extraction expands.

## 4. Next batch

Continue source-by-source extraction from ERX-PROT-001 v1.1, ERX-ATLAS-001 v1.1, UTXO-911-001 v1.0 and ERX-ROADMAP-001 v1.0, with exact page/section locators. Then reconcile overlap, assign types and review origin/status, and populate phase allocation only from a justified roadmap mapping.

---
End of ERX-WP-0.7-INITIAL-REQUIREMENT-EXTRACTION-001
