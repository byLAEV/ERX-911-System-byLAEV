# ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-001
## Primary Roadmap Phase Allocation

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-001 |
| Version | 0.1.2 |
| Status | PRELIMINARY ALLOCATION — REVIEW PENDING |
| Date | 2026-11-25 |
| Canonical source | registers/requirements-traceability.csv |

## Allocation rule
Each requirement receives one primary lifecycle phase based on its principal work product. Dependencies may span earlier and later phases and are preserved from the canonical traceability register. This is a planning allocation, not authorization to begin a later phase. Phase 0 remains the governance/preparation phase in which WP-0.7 identifies and maps requirements.

## Distribution
| Roadmap phase | Requirements |
|---|---:|
| PHASE_1 — Normative closure and state model | 19 |
| PHASE_3 — Software architecture and infrastructure | 5 |
| PHASE_2 — Formal data and cryptography | 4 |
| PHASE_6 — Documentary evidence and OpenTimestamps | 6 |
| PHASE_4 — ERX Core development | 3 |
| PHASE_8 — Institutional integration | 3 |
| PHASE_5 — Identity, trust and institutional security | 11 |
| PHASE_7 — ERX Verifier development | 5 |
| PHASE_9 — Testing, audit and recovery | 5 |
| PHASE_10 — Shadow pilot | 2 |
| PHASE_11 — Homologation and institutional expansion | 2 |
| **Total** | **65** |

## Requirement allocation
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
| ERX-REQ-DATA-0001 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | WP-0.7 source review; ERX-REQ-CLOSE-0001 |
| ERX-REQ-CRYPTO-0001 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | ERX-REQ-UTXO-0006; ERX-REQ-KEY-0001; ERX-REQ-KEY-0002 |
| ERX-REQ-CRYPTO-0002 | PHASE_2 — Formal data and cryptography | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_2 — Formal data and cryptography. | ERX-REQ-UTXO-0002; ERX-REQ-DATA-0001 |
| ERX-REQ-VERIFY-0004 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0003 |
| ERX-REQ-TRANS-0002 | PHASE_8 — Institutional integration | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_8 — Institutional integration. | ERX-REQ-TRANS-0001; ERX-REQ-ARCH-0001; DOC-ISS-010 |
| ERX-REQ-TEST-0001 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010; ERX-REQ-VERIFY-0001 |
| ERX-REQ-ARCH-0002 | PHASE_3 — Software architecture and infrastructure | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_3 — Software architecture and infrastructure. | ERX-REQ-VERIFY-0004 |
| ERX-REQ-UTXO-0013 | PHASE_3 — Software architecture and infrastructure | Atomic consume/create boundary and external-service isolation are architecture/transaction-boundary constraints; implementation depends on the Phase 1 state model and Phase 2 formal data/cryptography. | ERX-REQ-UTXO-0007; ERX-REQ-UTXO-0012 |
| ERX-REQ-CORE-0001 | PHASE_4 — ERX Core development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_4 — ERX Core development. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010 |
| ERX-REQ-CORE-0002 | PHASE_4 — ERX Core development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_4 — ERX Core development. | ERX-REQ-ARCH-0001; ERX-REQ-ARCH-0002 |
| ERX-REQ-TEST-0002 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-UTXO-0001; ERX-REQ-STATE-0001 |
| ERX-REQ-TEST-0003 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0010; ERX-REQ-INV-0004 |
| ERX-REQ-IDENT-0001 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-INST-0001; ERX-REQ-AGENT-0001 |
| ERX-REQ-IDENT-0002 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-INST-0002; ERX-REQ-KEY-0002 |
| ERX-REQ-KEY-0003 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-KEY-0001; ERX-REQ-KEY-0002; ERX-REQ-CRYPTO-0001 |
| ERX-REQ-SEC-0001 | PHASE_5 — Identity, trust and institutional security | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_5 — Identity, trust and institutional security. | ERX-REQ-CRYPTO-0001; ERX-REQ-IDENT-0002 |
| ERX-REQ-OTS-0002 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | ERX-REQ-UTXO-0006; ERX-REQ-CRYPTO-0002; ERX-REQ-UTXO-0012 |
| ERX-REQ-PRIV-0002 | PHASE_6 — Documentary evidence and OpenTimestamps | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_6 — Documentary evidence and OpenTimestamps. | ERX-REQ-PRIV-0001; ERX-REQ-VERIFY-0001 |
| ERX-REQ-VERIFY-0005 | PHASE_7 — ERX Verifier development | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_7 — ERX Verifier development. | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0002; ERX-REQ-VERIFY-0003 |
| ERX-REQ-INT-0002 | PHASE_8 — Institutional integration | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_8 — Institutional integration. | ERX-REQ-CORE-0001; ERX-REQ-TEST-0003 |
| ERX-REQ-TEST-0004 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-TEST-0001; ERX-REQ-TEST-0003 |
| ERX-REQ-TEST-0005 | PHASE_9 — Testing, audit and recovery | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_9 — Testing, audit and recovery. | ERX-REQ-TEST-0001; ERX-REQ-TEST-0004 |
| ERX-REQ-PILOT-0001 | PHASE_10 — Shadow pilot | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_10 — Shadow pilot. | ERX-REQ-OPS-0001; ERX-REQ-INT-0001; ERX-REQ-VERIFY-0001 |
| ERX-REQ-PILOT-0002 | PHASE_10 — Shadow pilot | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_10 — Shadow pilot. | ERX-REQ-PILOT-0001; ERX-REQ-TEST-0005 |
| ERX-REQ-HOMO-0001 | PHASE_11 — Homologation and institutional expansion | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_11 — Homologation and institutional expansion. | ERX-REQ-INST-0001; ERX-REQ-VERIFY-0004; ERX-REQ-OPS-0001 |
| ERX-REQ-HOMO-0002 | PHASE_11 — Homologation and institutional expansion | Primary lifecycle allocation by subject and explicit Roadmap phase gate; cross-phase dependencies remain recorded separately. Target: PHASE_11 — Homologation and institutional expansion. | ERX-REQ-TRANS-0002; ERX-REQ-INT-0002; ERX-REQ-VERIFY-0004 |

## Conflict resolution record
The main branch and the WP-0.7 review branch independently added this same allocation register. This resolved version preserves the main-branch document identity, control metadata and allocation rule while retaining the review branch's newer phase assignments and reconstructing the dependency column directly from the canonical CSV. No requirement row or dependency was intentionally dropped.

## Acceptance limitations
All allocations are provisional and require review against the approved Roadmap, dependency gates and requirement scope. A phase assignment does not approve a requirement, close a specification gap, or authorize implementation. All 65 records remain EXTRACTED — REVIEW PENDING.

---
End of ERX-WP-0.7-PHASE-ALLOCATION-REGISTER-001
