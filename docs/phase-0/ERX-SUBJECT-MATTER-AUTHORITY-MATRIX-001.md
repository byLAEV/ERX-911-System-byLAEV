# ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001
## Subject-Matter Authority and Scope Matrix

| Field | Value |
|---|---|
| Document ID | ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001 |
| Version | 1.0.0 |
| Status | APPROVED — WP-0.3 |
| Work Package | WP-0.3 / Activity 0.3.4 |
| Project | ERX-911-System-byLAEV |
| Design and Approval Authority | LAEV |
| Evidence baseline | Direct inspection of FND-001–FND-005, including page-level Protocol, UTXO-911 and Roadmap comparison |
| Date | 2026-11-24 |

## 1. Purpose and rule
This matrix records the subject-matter allocations adopted by LAEV in ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0. It establishes scoped authority, not universal precedence among foundational documents.

## 2. Subject-matter matrix

| Subject | Directly relevant source | Supporting / related source | Evidence inspected | Proposed authority boundary |
|---|---|---|---|---|
| Institutional 911 protocol purpose, participants, institutional prerequisites and lifecycle | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Protocol Sections 1–5; Atlas control section and Plates 01–02 | Protocol is the direct textual protocol source; Atlas represents it graphically |
| Three institutional communication transactions | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1; ERX-ROADMAP-001 v1.0; UTXO-911-001 v1.0 | Protocol Sections 1–2, 6–8 and Step 15; Atlas Plates 02–04; Roadmap Section 3.1 | Protocol/Atlas/Roadmap define UTXO 01 reception, UTXO 02 contact and initial protocol, UTXO 03 development and closure; UTXO-911 has an additional separate acceptance output described in Sections 2.5 and 3.1, requiring the DP-02 mapping decision |
| Call request and agent acceptance states | UTXO-911-001 v1.0 | ERX-PROT-001 v1.1; ERX-ATLAS-001 v1.1; ERX-ROADMAP-001 v1.0 | UTXO Sections 2.1–2.5 and 3.1; Protocol Step 15 (PDF p.13); Atlas Plate 03 | UTXO-911 explicitly consumes a request UTXO and generates a distinct acceptance UTXO before the initial-protocol UTXO. Protocol Step 15 instead consumes UTXO 01 and creates UTXO 02 representing contact and initial protocol result. DP-02 resolves the mapping: acceptance is an event/sub-state in UTXO 01→02, not a separate spendable output in the approved three-output profile |
| Independent agent-availability cycle and reuse prevention | ERX-ROADMAP-001 v1.0 | UTXO-911-001 v1.0; Technical Response FND-005 | Roadmap Section 3.1 (PDF p.3); UTXO Sections 4.5–5 (PDF pp.8–9); Technical Response p.1 | The Roadmap expressly establishes Cycle B as related to but independent from the three communication UTXOs; UTXO-911 and FND-005 support this separation. Detailed transitions, authority and release conditions remain to be specified; the existence/independence of the cycle is not an unresolved question |
| UTXO uniqueness, atomicity, idempotency, concurrency, replay and history | ERX-PROT-001 v1.1 | UTXO-911-001 v1.0; Atlas Plate 05 | Protocol Section 10.1–10.11; UTXO Section 6; Atlas Plate 05 | Shared subject matter; Protocol gives explicit mandatory rules; implementation mechanisms remain subject to later technical specifications |
| OTS evidence and its independence from emergency handling | ERX-PROT-001 v1.1 | UTXO-911-001 v1.0; Atlas Plate 06 | Protocol Sections 11–12; UTXO Section 7; Atlas Plate 06 | OTS is temporal evidence, not call admission, institutional authentication or proof of content truth |
| Privacy, protected data and access | ERX-PROT-001 v1.1 | Atlas Plate 08 | Protocol Section 13; Atlas verification/privacy representation | Protocol is the direct textual source; operational controls require detailed requirements later |
| Exception handling, continuity and verification | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Protocol Sections 14–16; Atlas Plates 07–08 | Text and diagrams must be mapped at clause/plate level; no silent diagram override |
| Project phase sequence, dependencies, deliverables and acceptance gates | ERX-ROADMAP-001 v1.0 | Technical Response FND-005 | Roadmap full 37-page source; response pages 1–2 | Roadmap is the planning source; response remains a response/recommendation absent explicit amendment approval |
| Project scope, authorization and approval | Approved Phase 0 Charter and express LAEV decisions | Workplan and approval records | Charter and Workplan repository records | Governance authority within the exact scope approved by LAEV; Workplan itself remains DRAFT / PENDING APPROVAL |
| Consensus architecture | ERX-CONSENSUS-001 v0.1 identity/content confirmed; source is a proposal for review | Roadmap §1; text source `docs/Consenso ERX byLAEV`; source inspection record | Direct title/control and substantive text inspected; Roadmap identity confirmed. Source explicitly defers operational quorum, validator rules, conflict handling and consensus UTXO/JSON specifications | Source is the identified consensus proposal/reference. LAEV must approve/revise its authority/status and assign completion criteria under DOC-ISS-011 before multi-institutional implementation |
| Institutional implementation proposal | ERX-IMPL-PROPOSAL-001 cited, not located | Roadmap | Roadmap reference only | No substantive authority or content can be inferred until the source is located or an explicit alternative is approved |

## 3. Specific alignment finding: communication acceptance output and independent agent availability

The inspected sources describe related but not identical levels of modeling:

1. ERX-PROT-001 v1.1 describes a three-transaction communication chain: UTXO 01 for reception/origin/routing; UTXO 02 for contact establishment and initial protocol; UTXO 03 for development and closure. Section 10 defines mandatory uniqueness, atomicity, idempotency, concurrency, replay protection, history, corrections and coordination limits.
2. ERX-ATLAS-001 v1.1 maps the three communication transactions to Plates 02–04 and represents the UTXO double-spend engine on Plate 05. Its correspondence table maps Protocol sections to plates 01–08.
3. UTXO-911-001 v1.0 Sections 2.1–2.5 describe a call-request UTXO, then an acceptance transition that consumes that request and creates a distinct acceptance UTXO. Section 3.1 then describes a further UTXO for the operator's initial communication protocol. Sections 4.1–4.5 address closure and the creation of a new agent-availability UTXO.
4. ERX-ROADMAP-001 v1.0 Section 3.1 (PDF p.3) expressly adopts two related but independent cycles: Cycle A, communication UTXO 01–03; Cycle B, agent availability, with states AVAILABLE → ASSIGNED/ACCEPTED → BUSY → RELEASE AND NEW AVAILABILITY. It says the agent cycle has its own states and does not reuse call UTXOs; references between cycles use identity, assignment and session.
5. The Technical Response to ERX-ROADMAP-001, page 1, supports separate UTXO cycles for communication and agent availability.

**Finding A — Structural mapping resolved by DP-02:** UTXO-911 explicitly represents acceptance as a separate spendable UTXO before the initial-protocol UTXO. ERX-PROT-001 Step 15 and Atlas Plate 03 represent the transition from UTXO 01 directly to UTXO 02, where UTXO 02 records contact and initial protocol. LAEV selected the uniquely identified event/sub-state within the UTXO 01 → UTXO 02 transition. DOC-ISS-009 is CLOSED for the approved profile.

**Finding B — Agent availability separation is source-confirmed:** the Roadmap has already adopted a separate, related-but-independent availability cycle. DOC-ISS-010 therefore concerns detailed state-machine formalization, transition permissions, release/recovery conditions and verification, not whether the cycle is independent.

## 4. Authority and interpretation rules proposed
- Textual protocol requirements are traced to exact ERX-PROT clauses.
- Atlas plates are traced to the clauses and process they represent; the Atlas control section names ERX-PROT-001 as its related normative document.
- UTXO-911 remains a distinct foundational functional source until its scope and mapping are expressly decided.
- A technical response does not amend its target Roadmap without an explicit approval record.
- Missing sources do not acquire inferred authority.
- Where sources overlap, classify the relation as complement, decomposition, representation, dependency, or unresolved divergence before deciding precedence.

## 5. Required decisions
LAEV decisions are recorded in DP-01 through DP-09. Detailed agent-availability state-machine work and consensus operational specification are deferred with interim controls. The unlocated implementation proposal remains a bounded limitation. Future changes require a new controlled decision.

## 6. Current status
**APPROVED — WP-0.3.** Subject-matter allocations and the specific UTXO/agent-cycle dispositions are approved by ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0 (2026-11-24). Detailed agent-availability state-machine requirements remain deferred; consensus remains a proposal pending a separate operational specification. This matrix establishes no universal precedence outside its stated scopes.

---
END
