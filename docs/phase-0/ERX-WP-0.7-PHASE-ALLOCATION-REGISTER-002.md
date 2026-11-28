# ERX-WP-0.7 — Corrected Primary Phase Allocation Register

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-002 |
| Version | 1.0.0 |
| Status | HISTORICAL — SUPERSEDED; NOT CURRENT AUTHORITY |
| Date | 2026-11-26 |
| Work Package | WP-0.7 / Activity 0.7.10 |
| Canonical source | registers/requirements-traceability.csv |
| Allocation method | One primary lifecycle phase per canonical requirement ID; no execution authorization |

## Historical-use notice

This 45-row correction snapshot is retained solely as documentary history. Its 45/65-row figures describe an earlier incomplete inventory and are not the current requirements population. It is superseded by `ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-001 v0.3.3`, which covers the current 82 source candidates. Do not use this file for current allocation, traceability or acceptance decisions.

## 1. Historical reconciliation result

The current canonical CSV contains 45 data rows, 45 unique requirement IDs and 19 columns. The earlier allocation register contains 65 allocation rows and 65 unique IDs. Of those, 45 IDs occur in the canonical CSV and 20 are orphan allocation references.

This corrected working register retains only allocation rows whose IDs are present in the canonical CSV. The 20 orphan IDs are excluded from this version; they are not deleted from history and must be recovered as source-backed candidate rows or formally dispositioned before closure.

## 2. Corrected distribution

| Roadmap phase | Canonical requirements allocated |
|---|---:|
| PHASE_1 | 19 |
| PHASE_2 | 4 |
| PHASE_3 | 3 |
| PHASE_4 | 1 |
| PHASE_5 | 7 |
| PHASE_6 | 4 |
| PHASE_7 | 4 |
| PHASE_8 | 2 |
| PHASE_9 | 1 |
| **Total** | **45** |

## 3. Requirement allocation

| Requirement ID | Primary phase | Allocation basis | Dependencies |
|---|---|---|---|
| ERX-REQ-UTXO-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0003; WP-0.7 source review |
| ERX-REQ-UTXO-0002 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0001 |
| ERX-REQ-UTXO-0003 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0004; ERX-REQ-UTXO-0010 |
| ERX-REQ-UTXO-0004 | PHASE_3 — Software architecture and infrastructure | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_3 — Software architecture and infrastructure. | ERX-REQ-UTXO-0003; DOC-ISS-010 |
| ERX-REQ-UTXO-0005 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0009 |
| ERX-REQ-UTXO-0006 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | Cryptography/serialization ADR required |
| ERX-REQ-UTXO-0007 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0001; ERX-REQ-UTXO-0004 |
| ERX-REQ-UTXO-0008 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | OTS interface specification |
| ERX-REQ-UTXO-0009 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0005 |
| ERX-REQ-UTXO-0010 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0004 |
| ERX-REQ-UTXO-0011 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010 |
| ERX-REQ-UTXO-0012 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | ERX-REQ-UTXO-0008 |
| ERX-REQ-OPS-0001 | PHASE_3 — Software architecture and infrastructure | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_3 — Software architecture and infrastructure. | ERX-REQ-UTXO-0012 |
| ERX-REQ-OPS-0002 | PHASE_4 — ERX Core development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_4 — ERX Core development. | ERX-REQ-UTXO-0004 |
| ERX-REQ-INT-0001 | PHASE_8 — Institutional integration | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_8 — Institutional integration. | Adapter specification |
| ERX-REQ-INST-0001 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | WP-0.7 source review |
| ERX-REQ-INST-0002 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-INST-0001 |
| ERX-REQ-INST-0003 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-INST-0001 |
| ERX-REQ-KEY-0001 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | Key-management decision |
| ERX-REQ-KEY-0002 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-KEY-0001 |
| ERX-REQ-ARCH-0001 | PHASE_3 — Software architecture and infrastructure | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_3 — Software architecture and infrastructure. | ERX-REQ-UTXO-0003; ERX-REQ-INT-0001 |
| ERX-REQ-PRIV-0001 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | ERX-REQ-INST-0001; retention policy |
| ERX-REQ-TRANS-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0005; ERX-REQ-INT-0001; DOC-ISS-010 |
| ERX-REQ-CLOSE-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | UTXO-911-001 p.7 closure distinction |
| ERX-REQ-VERIFY-0001 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-OPS-0002; verifier specification |
| ERX-REQ-VERIFY-0002 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-VERIFY-0001 |
| ERX-REQ-AGENT-0001 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-INST-0002; ERX-REQ-OPS-0001 |
| ERX-REQ-AGENT-0002 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-AGENT-0001 |
| ERX-REQ-OTS-0001 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | ERX-REQ-UTXO-0008; ERX-REQ-UTXO-0012 |
| ERX-REQ-VERIFY-0003 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0002 |
| ERX-REQ-OPS-0003 | PHASE_1 — Normative closure and state model | Communication closure versus incident closure is a lifecycle/state-model distinction; detailed institutional incident workflow remains a dependency for later integration. | ERX-REQ-CLOSE-0001 |
| ERX-REQ-AVAIL-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0011; availability decision |
| ERX-REQ-AVAIL-0002 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0001; ERX-REQ-UTXO-0011 |
| ERX-REQ-STATE-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-AVAIL-0002; ERX-REQ-OPS-0003 |
| ERX-REQ-STATE-0002 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0001; ERX-REQ-UTXO-0002; ERX-REQ-UTXO-0011 |
| ERX-REQ-INV-0001 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-CLOSE-0001; ERX-REQ-OPS-0003 |
| ERX-REQ-INV-0002 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0002; ERX-REQ-UTXO-0006 |
| ERX-REQ-INV-0003 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0002; ERX-REQ-UTXO-0004 |
| ERX-REQ-INV-0004 | PHASE_1 — Normative closure and state model | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_1 — Normative closure and state model. | ERX-REQ-UTXO-0004; ERX-REQ-UTXO-0010; ERX-REQ-KEY-0002 |
| ERX-REQ-DATA-0001 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | ERX-REQ-UTXO-0002; ERX-REQ-UTXO-0006; ERX-REQ-CLOSE-0002 |
| ERX-REQ-CRYPTO-0001 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | ERX-REQ-UTXO-0006; ERX-REQ-KEY-0001; ERX-REQ-KEY-0002 |
| ERX-REQ-CRYPTO-0002 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | ERX-REQ-UTXO-0002; ERX-REQ-DATA-0001 |
| ERX-REQ-VERIFY-0004 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0003 |
| ERX-REQ-TRANS-0002 | PHASE_8 — Institutional integration | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_8 — Institutional integration. | ERX-REQ-TRANS-0001; ERX-REQ-ARCH-0001; DOC-ISS-010 |
| ERX-REQ-TEST-0001 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010; ERX-REQ-VERIFY-0001 |

## 4. Control and limitations

- This is a reconciliation of the current 45-row canonical CSV against the prior 65-row allocation table, not a semantic approval of all allocations.
- All 45 source records remain EXTRACTED — REVIEW PENDING; phase allocation does not promote them to APPROVED.
- Every allocation basis remains subject to row-by-row confirmation against ERX-ROADMAP-001 v1.0 and the source's subject-matter authority.
- The 20 orphan allocation IDs are evidence of additional candidate work not represented in the canonical CSV snapshot. They must not be silently discarded; investigate their source records and either add properly sourced rows to a later CSV revision or document why they are invalid.
- No future phase is authorized by this register.

---
End of ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-002
