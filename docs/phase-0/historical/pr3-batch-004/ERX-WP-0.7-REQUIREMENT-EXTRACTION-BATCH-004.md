# ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-004
## Controlled Extraction — Continuity, Privacy, Recovery and Verification

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-004 |
| Version | 0.1.0 |
| Status | EXTRACTED — TECHNICAL REVIEW PENDING |
| Work Package | WP-0.7 / Activities 0.7.2–0.7.9 |
| Date | 2026-11-25 |
| Method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 |
| Source inspection | ERX-WP-0.7-SOURCE-INSPECTION-RECORD-001 v1.0.0 |

## 1. Boundary

This batch adds source-derived candidate statements from exact passages in the five inspected foundational PDFs. It does not approve requirements, choose implementation mechanisms, establish numeric performance targets, resolve authority conflicts, or allocate requirements to a phase. The source modality and scope are preserved. Candidate statements remain EXTRACTED — REVIEW PENDING.

## 2. Candidate requirements

| Requirement ID | Candidate statement | Source locator | Type |
|---|---|---|---|
| ERX-REQ-OPS-0004 | When ERX is unavailable, and where technically possible, events must be stored in a durable, protected local queue; event time, recovery time and commitment-generation time must be recorded separately. | ERX-PROT-001 v1.1, PDF p.25, §16.8 | OPERATIONAL / DATA_AND_RECORDS |
| ERX-REQ-OPS-0005 | On recovery, pending events must be checked for integrity, duplication, identity and order, then processed idempotently; valid states must be reconstructed and pending evidence generated while incidents are retained. | ERX-PROT-001 v1.1, PDF p.26, §17.2 | OPERATIONAL / SECURITY / RECOVERY |
| ERX-REQ-OPS-0006 | Storage failure handling must include persistence, backup and recovery mechanisms; an event must not be represented as permanently recorded before storage confirmation. | ERX-PROT-001 v1.1, PDF p.25, §16.9 | OPERATIONAL / DATA_AND_RECORDS |
| ERX-REQ-SEC-0001 | Interfaces between ERX and institutional systems must use mutual authentication or an appropriate equivalent, transport protection, role-based authorization and message validation; unauthorized components must not issue institutional transitions. | ERX-PROT-001 v1.1, PDF p.26, §17.3 | SECURITY / INTERFACE |
| ERX-REQ-ARCH-0002 | ERX must be organized into four components with distinct responsibilities: ERX Protocol, ERX Core, ERX Institutional Module and ERX Verifier. | ERX-PROT-001 v1.1, PDF p.26, §19 | ARCHITECTURAL |
| ERX-REQ-TEST-0002 | Before institutional implementation, testing must cover the twenty categories/cases enumerated in ERX-PROT-001 §19.1, including double consumption, concurrency, replay, invalid signatures, transfer, outages, storage recovery, privacy and independent verification. | ERX-PROT-001 v1.1, PDF p.26, §19.1 | VERIFICATION / SECURITY / OPERATIONAL |
| ERX-REQ-PRIV-0002 | Sensitive call information remains under institutional custody; public disclosure is limited to cryptographic commitments and data strictly necessary to verify temporal proofs; call content is not published to Bitcoin. | ERX-ATLAS-001 v1.1, PDF pp.25–26, Lámina 08 | PRIVACY / DATA_AND_RECORDS |
| ERX-REQ-VERIFY-0005 | The verifier must distinguish cryptographic evidence of integrity or temporal commitment from proof of the material truth of the underlying content. | ERX-ATLAS-001 v1.1, PDF p.28, Categorías de verificación | VERIFICATION / GOVERNANCE |
| ERX-REQ-AVAIL-0003 | Agent availability is an independent state cycle, related to call states by identity, assignment and session references; the call's UTXO 03 must not substitute for the agent-availability UTXO. | ERX-ROADMAP-001 v1.0, PDF pp.4–5, §3.1 | ARCHITECTURAL / FUNCTIONAL |
| ERX-REQ-INV-0005 | Recovery must not restore a consumed communication state as spendable or active; continuity is reconstructed through new states linked to prior events, not by reusing consumed UTXOs. | UTXO-911-001 v1.0, PDF pp.9–10, §§5–6 | SECURITY / RECOVERY / TRANSACTIONAL |
| ERX-REQ-OTS-0002 | The system must retain OTS commitments, proofs and the data required to verify them; proof acquisition may complete later and must not delay or block emergency reception, acceptance or attention. | UTXO-911-001 v1.0, PDF p.11, §7 | DATA_AND_RECORDS / OPERATIONAL |

## 3. Review state

- Eleven additional source-derived candidates are added to the traceability register.
- Their lifecycle status is EXTRACTED — REVIEW PENDING; none is approved by this batch.
- Verification criteria and methods remain NOT_DEFINED where the source does not provide measurable acceptance thresholds.
- Phase allocation remains UNALLOCATED_PENDING_WP-0.7.10.
- The source does not provide numeric limits for queue capacity, retention duration, recovery time, authentication protocol selection or transport cryptography; these remain specification/decision matters.
- The technical response to ERX-ROADMAP-001 is treated as review guidance, not as a normative source that silently changes requirement strength.

## 4. Next work

Continue source-by-source reconciliation, check overlap across the 56 current candidates, identify all source-derived obligations and gaps, then carry out individual review, classification, mandatory/design/pending distinctions, open-decision capture and justified phase allocation. Do not begin WP-0.8 or Phase 1 as part of this batch.

---
End of ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-004
