# ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001
## Subject-Matter Authority and Scope Matrix

| Field | Value |
|---|---|
| Document ID | ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001 |
| Version | 0.1.0 |
| Status | PROPOSAL — PENDING LAEV APPROVAL |
| Work Package | WP-0.3 / Activity 0.3.4 |
| Project | ERX-911-System-byLAEV |
| Design and Approval Authority | LAEV |
| Evidence baseline | Direct inspection of FND-001, FND-002 and FND-003 PDFs |
| Date | 2026-11-24 |

## 1. Purpose and rule
This matrix identifies the source most directly relevant to each subject, the corroborating sources, and unresolved boundaries. It proposes subject-matter allocation; it does not establish a universal precedence among the foundational documents. Final authority assignments require LAEV approval.

## 2. Subject-matter matrix

| Subject | Directly relevant source | Supporting / related source | Evidence inspected | Proposed authority boundary |
|---|---|---|---|---|
| Institutional 911 protocol purpose, participants, institutional prerequisites and lifecycle | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Protocol Sections 1–5; Atlas control section and Plates 01–02 | Protocol is the direct textual protocol source; Atlas represents it graphically |
| Three institutional communication transitions | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1; UTXO-911-001 v1.0 | Protocol Sections 5–9; Atlas Plates 01–04 and correspondence table; UTXO Sections 1–4 | Protocol describes three transactions; exact functional alignment with UTXO-911 requires a controlled mapping |
| Initial call request, acceptance and operator protocol | UTXO-911-001 v1.0 | ERX-PROT-001 v1.1; Atlas Plates 02–03 | UTXO Sections 2–3; Protocol Sections 6–7 | UTXO-911 describes request/acceptance details; whether these are sub-states within Protocol UTXO 01/02 or separate outputs requires decision |
| Agent availability and reuse prevention | UTXO-911-001 v1.0 | Atlas Plate 05 and operational flow plates | UTXO Sections 4.5–5; Atlas Plate 05 | UTXO-911 expressly describes an agent availability UTXO separate from the communication states; Protocol's three-stage chain does not fully define this agent lifecycle in the inspected sections |
| UTXO uniqueness, atomicity, idempotency, concurrency, replay and history | ERX-PROT-001 v1.1 | UTXO-911-001 v1.0; Atlas Plate 05 | Protocol Section 10.1–10.11; UTXO Section 6; Atlas Plate 05 | Shared subject matter; Protocol gives explicit mandatory rules; implementation mechanisms remain subject to later technical specifications |
| OTS evidence and its independence from emergency handling | ERX-PROT-001 v1.1 | UTXO-911-001 v1.0; Atlas Plate 06 | Protocol Sections 11–12; UTXO Section 7; Atlas Plate 06 | OTS is temporal evidence, not call admission, institutional authentication or proof of content truth |
| Privacy, protected data and access | ERX-PROT-001 v1.1 | Atlas Plate 08 | Protocol Section 13; Atlas verification/privacy representation | Protocol is the direct textual source; operational controls require detailed requirements later |
| Exception handling, continuity and verification | ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Protocol Sections 14–16; Atlas Plates 07–08 | Text and diagrams must be mapped at clause/plate level; no silent diagram override |
| Project phase sequence, dependencies, deliverables and acceptance gates | ERX-ROADMAP-001 v1.0 | Technical Response FND-005 | Roadmap full 37-page source; response pages 1–2 | Roadmap is the planning source; response remains a response/recommendation absent explicit amendment approval |
| Project scope, authorization and approval | Approved Phase 0 Charter and express LAEV decisions | Workplan and approval records | Charter and Workplan repository records | Governance authority within the exact scope approved by LAEV; Workplan itself remains DRAFT / PENDING APPROVAL |
| Consensus architecture | ERX-CONSENSUS-001 v0.1 cited; candidate `docs/Consenso ERX byLAEV.pdf` located, identity unverified | Roadmap; candidate PDF pending inspection | Roadmap citation and candidate filename only; no internal identity/content verification yet | No substantive authority or content can be inferred until candidate identity and contents are verified or an explicit alternative is approved |
| Institutional implementation proposal | ERX-IMPL-PROPOSAL-001 cited, not located | Roadmap | Roadmap reference only | No substantive authority or content can be inferred until the source is located or an explicit alternative is approved |

## 3. Specific alignment finding: three communication UTXOs and agent availability

The inspected sources describe related but not identical levels of modeling:

1. ERX-PROT-001 v1.1 describes a three-transaction communication chain: UTXO 01 for reception/origin/routing; UTXO 02 for contact establishment and initial protocol; UTXO 03 for development and closure. Section 10 defines mandatory uniqueness, atomicity, idempotency, concurrency, replay protection, history, corrections and coordination limits.
2. ERX-ATLAS-001 v1.1 maps the three communication transactions to Plates 02–04 and represents the UTXO double-spend engine on Plate 05. Its correspondence table maps Protocol sections to plates 01–08.
3. UTXO-911-001 v1.0 describes more granular request and acceptance states in Section 2, operator protocol in Section 3, communication closure in Section 4, and a distinct agent-availability UTXO in Sections 4.5–5. It expressly prevents one availability state from accepting multiple incompatible calls.

This is not declared a contradiction. It is a scope/granularity and lifecycle-alignment question: the documents may describe different layers of one system, but the exact mapping of request, acceptance, communication lifecycle and agent availability must be expressly decided before requirements extraction or implementation.

## 4. Authority and interpretation rules proposed
- Textual protocol requirements are traced to exact ERX-PROT clauses.
- Atlas plates are traced to the clauses and process they represent; the Atlas control section names ERX-PROT-001 as its related normative document.
- UTXO-911 remains a distinct foundational functional source until its scope and mapping are expressly decided.
- A technical response does not amend its target Roadmap without an explicit approval record.
- Missing sources do not acquire inferred authority.
- Where sources overlap, classify the relation as complement, decomposition, representation, dependency, or unresolved divergence before deciding precedence.

## 5. Required decisions
LAEV must:
1. Adopt, revise or reject each proposed subject allocation.
2. Decide the mapping of UTXO-911 request/acceptance states to ERX-PROT's three transaction states.
3. Decide whether agent availability is a separate UTXO state machine linked to, but not part of, the three communication UTXOs.
4. Decide the normative status of Atlas plates relative to the Protocol text.
5. Decide treatment of the Roadmap technical response.
6. Record whether the two unavailable cited sources remain accepted limitations or must be supplied before later requirements work.

## 6. Current status
**PROPOSED — NOT APPROVED.** Exact source comparisons have identified the scope distinction above. Activity 0.3.4 remains pending LAEV approval. No technical requirement, implementation behavior, or universal document precedence is approved by this matrix.

---
END
