# ERX-WP-0.7-SEMANTIC-REVIEW-REGISTER-001
## Individuality, atomicity and overlap review — working disposition

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-SEMANTIC-REVIEW-REGISTER-001 |
| Version | 0.1.0 |
| Status | REVIEW REGISTER — HUMAN DISPOSITION REQUIRED |
| Date | 2026-11-25 |
| Scope | All 65 canonical requirement candidates |
| Source of truth | registers/requirements-traceability.csv |

## 1. Rules
- No requirement ID is deleted, merged, renumbered or silently superseded in this review.
- Similarity is a review signal, not proof of duplication.
- Retain, split, parent/child, merge or reject dispositions require a recorded reason and source check.
- A compound requirement is split only when its parts have independently testable outcomes or distinct authority/scope.
- This register does not approve any requirement or amend ERX-PROT-001, ERX-ATLAS-001, UTXO-911-001 or ERX-ROADMAP-001.

## 2. Overlap clusters requiring explicit disposition

| Cluster | Subject | Candidate IDs | Review rule |
|---|---|---|---|
| SEM-01 | UTXO single-spend, atomicity, concurrency and replay | ERX-REQ-UTXO-0001; ERX-REQ-UTXO-0003; ERX-REQ-UTXO-0004; ERX-REQ-UTXO-0005; ERX-REQ-UTXO-0007; ERX-REQ-UTXO-0009; ERX-REQ-UTXO-0010; ERX-REQ-UTXO-0011; ERX-REQ-UTXO-0013 | Potential overlap across invariant, implementation mechanism, event identity and testable outcome. Preserve separate IDs until scope and verification independence are reviewed; consider parent/child grouping, not automatic merge. |
| SEM-02 | OTS evidence lifecycle and non-blocking emergency handling | ERX-REQ-UTXO-0008; ERX-REQ-UTXO-0012; ERX-REQ-OTS-0001; ERX-REQ-OTS-0002 | Separate proof-state vocabulary, pipeline steps and operational non-blocking constraint. Avoid duplicate requirement if one is state semantics and another workflow. |
| SEM-03 | Institution, center, agent, credentials and trust | ERX-REQ-INST-0001; ERX-REQ-INST-0002; ERX-REQ-INST-0003; ERX-REQ-AGENT-0001; ERX-REQ-AGENT-0002; ERX-REQ-IDENT-0001; ERX-REQ-IDENT-0002; ERX-REQ-KEY-0001; ERX-REQ-KEY-0002; ERX-REQ-KEY-0003 | Separate entity types, credential status, territorial authority, key custody and non-response. Review scope boundaries and whether any record combines multiple independent validation outcomes. |
| SEM-04 | Communication transfer, availability and lifecycle states | ERX-REQ-TRANS-0001; ERX-REQ-TRANS-0002; ERX-REQ-AVAIL-0001; ERX-REQ-AVAIL-0002; ERX-REQ-STATE-0001; ERX-REQ-STATE-0002; ERX-REQ-CLOSE-0001; ERX-REQ-OPS-0003; ERX-REQ-INV-0001 | Keep call state, agent availability, transfer authority and incident lifecycle distinct. Verify each transition's independently testable outcome. |
| SEM-05 | Verifier outputs, export package and evidence dimensions | ERX-REQ-VERIFY-0001; ERX-REQ-VERIFY-0002; ERX-REQ-VERIFY-0003; ERX-REQ-VERIFY-0004; ERX-REQ-VERIFY-0005 | Separate export contents, verifier independence, result vocabulary and category reporting; possible hierarchical requirements rather than merge. |
| SEM-06 | Architecture, adapters, integration and gates | ERX-REQ-ARCH-0001; ERX-REQ-ARCH-0002; ERX-REQ-INT-0001; ERX-REQ-INT-0002; ERX-REQ-CORE-0001; ERX-REQ-CORE-0002 | Separate architecture boundary, adapter contract, core scope and integration authorization gate. |
| SEM-07 | Privacy, files, audio and institutional custody | ERX-REQ-PRIV-0001; ERX-REQ-PRIV-0002 | Potentially overlapping custody rules; distinguish audio-specific metadata from general file custody and Bitcoin exclusion. |
| SEM-08 | Test coverage, quantitative acceptance and simulator | ERX-REQ-TEST-0001; ERX-REQ-TEST-0002; ERX-REQ-TEST-0003; ERX-REQ-TEST-0004; ERX-REQ-TEST-0005 | Separate test taxonomy, lifecycle simulator, adversarial scenario list, mandatory test references and measurable target-setting. |
| SEM-09 | Shadow pilot and homologation | ERX-REQ-PILOT-0001; ERX-REQ-PILOT-0002; ERX-REQ-HOMO-0001; ERX-REQ-HOMO-0002 | Separate pilot operation/comparison from center homologation and multi-center onboarding prerequisites. |
| SEM-10 | Cryptographic document structure and schema | ERX-REQ-UTXO-0002; ERX-REQ-UTXO-0006; ERX-REQ-DATA-0001; ERX-REQ-CRYPTO-0001; ERX-REQ-CRYPTO-0002 | Review compound fields, schema, signing and document linkage for independent verification outcomes and circular dependency risks. |

## 3. Individual candidate register

| Requirement ID | Source | Locator | Primary type | Phase | Candidate cluster | Semantic disposition |
|---|---|---|---|---|---|---|
| ERX-REQ-UTXO-0001 | ERX-PROT-001 v1.1 | PDF p.3 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0002 | ERX-PROT-001 v1.1 | PDF p.3, Section 2.1 | SECURITY | PHASE_1 — Normative closure and state model | SEM-10 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0003 | ERX-PROT-001 v1.1 | PDF p.3, Section 2.1 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0004 | ERX-PROT-001 v1.1 | PDF p.3, Section 2.2 | ARCHITECTURAL | PHASE_3 — Software architecture and infrastructure | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0005 | ERX-PROT-001 v1.1 | PDF p.4 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0006 | ERX-PROT-001 v1.1 | PDF p.10 | SECURITY | PHASE_2 — Formal data and cryptography | SEM-10 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0007 | ERX-PROT-001 v1.1 | PDF p.10, Step 7 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0008 | ERX-PROT-001 v1.1 | PDF p.10, Step 8 | DATA_AND_RECORDS | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-02 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0009 | ERX-PROT-001 v1.1 | PDF p.17, Sections 10.1–10.5 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0010 | ERX-PROT-001 v1.1 | PDF p.17, Section 10.6 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0011 | UTXO-911-001 v1.0 | PDF p.10, Principle of single spend | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0012 | UTXO-911-001 v1.0 | PDF p.11, OTS function | OPERATIONAL | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-02 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-OPS-0001 | ERX-PROT-001 v1.1 | PDF p.25, Section 17.1 | OPERATIONAL | PHASE_3 — Software architecture and infrastructure | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-OPS-0002 | ERX-PROT-001 v1.1 | PDF p.24, Section 16.9 | DATA_AND_RECORDS | PHASE_4 — ERX Core development | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 v1.0 | PDF p.23, Section 8.1 | INTEROPERABILITY | PHASE_8 — Institutional integration | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INST-0001 | ERX-PROT-001 v1.1 | PDF pp.5–6, Section 4 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INST-0002 | ERX-PROT-001 v1.1 | PDF p.6, Section 4.1 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INST-0003 | ERX-PROT-001 v1.1 | PDF p.6, Section 4.1 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-KEY-0001 | ERX-PROT-001 v1.1 | PDF p.6, Section 4.2 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-KEY-0002 | ERX-PROT-001 v1.1 | PDF p.7, Section 4.2 | SECURITY | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 v1.1 | PDF p.8, Section 4.3 | ARCHITECTURAL | PHASE_3 — Software architecture and infrastructure | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-PRIV-0001 | ERX-PROT-001 v1.1 | PDF pp.14–15, Step 18 | SECURITY | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-07 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 v1.1 | PDF pp.15–16, Step 19 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 v1.1 | PDF p.16, Step 20 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 v1.1 | PDF pp.21–23, Section 7 | SECURITY | PHASE_7 — ERX Verifier development | SEM-05 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 v1.1 | PDF p.24, Section 7.3 | INTERFACE | PHASE_7 — ERX Verifier development | SEM-05 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 v1.1 | PDF pp.7–8, Lámina 03 | SECURITY | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 v1.1 | PDF p.8, Lámina 03 | FUNCTIONAL | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 v1.1 | PDF p.19, Lámina 06 | DATA_AND_RECORDS | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-02 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 v1.1 | PDF pp.27–28, verifier categories | SECURITY | PHASE_7 — ERX Verifier development | SEM-05 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-OPS-0003 | UTXO-911-001 v1.0 | PDF p.7, Section 4.2 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-AVAIL-0001 | UTXO-911-001 v1.0 | PDF pp.9–10, availability lifecycle | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-AVAIL-0002 | UTXO-911-001 v1.0 | PDF pp.9–11, Sections 5–8 | ARCHITECTURAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-STATE-0001 | ERX-ROADMAP-001 v1.0 | PDF pp.6–7, Sections 1.2–1.3 | ARCHITECTURAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-STATE-0002 | ERX-ROADMAP-001 v1.0 | PDF p.7, Section 1.3 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INV-0001 | ERX-ROADMAP-001 v1.0 | PDF p.8, Section 1.5 | FUNCTIONAL | PHASE_1 — Normative closure and state model | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INV-0002 | ERX-ROADMAP-001 v1.0 | PDF p.8, Section 1.5 | DATA_AND_RECORDS | PHASE_1 — Normative closure and state model | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INV-0003 | ERX-ROADMAP-001 v1.0 | PDF p.8, Section 1.5 | DATA_AND_RECORDS | PHASE_1 — Normative closure and state model | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INV-0004 | ERX-ROADMAP-001 v1.0 | PDF p.8, Section 1.5 | FUNCTIONAL | PHASE_1 — Normative closure and state model | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-DATA-0001 | ERX-ROADMAP-001 v1.0 | PDF p.9, Section 2.1 | DATA_AND_RECORDS | PHASE_2 — Formal data and cryptography | SEM-10 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-CRYPTO-0001 | ERX-ROADMAP-001 v1.0 | PDF p.10, Section 2.3 | SECURITY | PHASE_2 — Formal data and cryptography | SEM-10 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-CRYPTO-0002 | ERX-ROADMAP-001 v1.0 | PDF p.10, Section 2.4 | ARCHITECTURAL | PHASE_2 — Formal data and cryptography | SEM-10 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-VERIFY-0004 | ERX-ROADMAP-001 v1.0 | PDF p.21, Section 7 | ARCHITECTURAL | PHASE_7 — ERX Verifier development | SEM-05 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TRANS-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.23–24, Section 8.2 | GOVERNANCE | PHASE_8 — Institutional integration | SEM-04 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TEST-0001 | ERX-ROADMAP-001 v1.0 | PDF p.24, Section 9.1 | VERIFICATION | PHASE_9 — Testing, audit and recovery | SEM-08 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-ARCH-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.11–12, §3.1 | ARCHITECTURAL | PHASE_3 — Software architecture and infrastructure | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-UTXO-0013 | ERX-ROADMAP-001 v1.0 | PDF pp.12–13, §3.3 | FUNCTIONAL | PHASE_3 — Software architecture and infrastructure | SEM-01 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-CORE-0001 | ERX-ROADMAP-001 v1.0 | PDF p.14, opening paragraph | GOVERNANCE | PHASE_4 — ERX Core development | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-CORE-0002 | ERX-ROADMAP-001 v1.0 | PDF p.14, §4.1 | ARCHITECTURAL | PHASE_4 — ERX Core development | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TEST-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.14–15, §§4.3 | FUNCTIONAL | PHASE_9 — Testing, audit and recovery | SEM-08 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TEST-0003 | ERX-ROADMAP-001 v1.0 | PDF p.15, §4.4 | SECURITY | PHASE_9 — Testing, audit and recovery | SEM-08 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-IDENT-0001 | ERX-ROADMAP-001 v1.0 | PDF p.16, §5.1 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-IDENT-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.16–17, §5.2 | SECURITY | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-KEY-0003 | ERX-ROADMAP-001 v1.0 | PDF p.17, §5.3 | GOVERNANCE | PHASE_5 — Identity, trust and institutional security | SEM-03 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-SEC-0001 | ERX-ROADMAP-001 v1.0 | PDF pp.17–18, §§5.4 and deliverables | SECURITY | PHASE_5 — Identity, trust and institutional security | UNCLUSTERED | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-OTS-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.18–19, §6.1 | SECURITY | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-02 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-PRIV-0002 | ERX-ROADMAP-001 v1.0 | PDF p.20, §6.4 | SECURITY | PHASE_6 — Documentary evidence and OpenTimestamps | SEM-07 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-VERIFY-0005 | ERX-ROADMAP-001 v1.0 | PDF p.21, §7.1 | SECURITY | PHASE_7 — ERX Verifier development | SEM-05 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-INT-0002 | ERX-ROADMAP-001 v1.0 | PDF p.22, opening of Phase 8 | GOVERNANCE | PHASE_8 — Institutional integration | SEM-06 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TEST-0004 | ERX-ROADMAP-001 v1.0 | PDF p.24, §9.1 | SECURITY | PHASE_9 — Testing, audit and recovery | SEM-08 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-TEST-0005 | ERX-ROADMAP-001 v1.0 | PDF p.25, §9.3 | PERFORMANCE_AND_CAPACITY | PHASE_9 — Testing, audit and recovery | SEM-08 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-PILOT-0001 | ERX-ROADMAP-001 v1.0 | PDF pp.26–27, §§10.1–10.2 | INTEROPERABILITY | PHASE_10 — Shadow pilot | SEM-09 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-PILOT-0002 | ERX-ROADMAP-001 v1.0 | PDF p.27, §10.3 | DATA_AND_RECORDS | PHASE_10 — Shadow pilot | SEM-09 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-HOMO-0001 | ERX-ROADMAP-001 v1.0 | PDF p.28, §11.1 | GOVERNANCE | PHASE_11 — Homologation and institutional expansion | SEM-09 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |
| ERX-REQ-HOMO-0002 | ERX-ROADMAP-001 v1.0 | PDF pp.28–29, §11.2 | GOVERNANCE | PHASE_11 — Homologation and institutional expansion | SEM-09 | PENDING — verify atomicity, scope, actor, trigger, precondition, outcome, source fidelity and independent testability |

## 4. Mandatory semantic checks
For each of the 65 rows, the reviewer must record:
1. Whether the statement expresses exactly one obligation or combines multiple outcomes.
2. Whether the actor/authority, trigger, scope and preconditions are clear.
3. Whether the outcome is observable and independently verifiable.
4. Whether another requirement covers the same outcome under the same conditions.
5. Whether any apparent overlap is actually a parent/child relationship or a separate control layer.
6. Whether the statement preserves source modality and does not strengthen a recommendation.
7. Whether the source locator supports every clause in the normalized statement.

## 5. Candidate disposition vocabulary
- RETAIN_ATOMIC
- SPLIT_REQUIRED
- PARENT_CHILD
- OVERLAP_DISTINCT_SCOPE
- MERGE_PROPOSAL
- DERIVED_RECLASSIFICATION
- SOURCE_CORRECTION_REQUIRED
- BLOCKED_BY_OPEN_DECISION

No disposition has been assigned by automated similarity. All candidates remain pending human semantic review.

---
End of ERX-WP-0.7-SEMANTIC-REVIEW-REGISTER-001
