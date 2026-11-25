# ERX-DOCUMENT-RELATIONSHIP-MAP-001
## Foundational and Phase 0 Document Relationship Map

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-RELATIONSHIP-MAP-001 |
| Version | 1.0.0 |
| Status | APPROVED WP-0.3 RELATIONSHIP BASELINE |
| Work Package | WP-0.3 / Activity 0.3.5 |
| Project | ERX-911-System-byLAEV |
| Authority | LAEV |
| Date | 2026-11-24 |

## 1. Purpose
Record relationships supported by direct source references and content inspection. Relationship types are descriptive and do not automatically establish precedence or amendment.

## 2. Relationship types
- **Normative reference:** a document expressly identifies another as normative or governing.
- **Foundational reference:** a plan identifies a document as a basis.
- **Graphical representation:** a diagram or plate represents a process described elsewhere.
- **Functional elaboration:** a document describes a more detailed operational or functional view.
- **Response/review:** a document comments on or responds to another.
- **Governance dependency:** a work package requires an earlier package's acceptance.
- **Unverified reference:** a cited source whose content has not been inspected.

## 3. Source relationship table

| Source A | Source B | Relationship | Evidence | Interpretation limit |
|---|---|---|---|---|
| ERX-ATLAS-001 v1.1 | ERX-PROT-001 v1.1 | Normative reference / graphical representation | Atlas control section names Protocol as related normative document; correspondence table maps Protocol topics to Plates 01–08 | Does not by itself resolve every plate/text discrepancy |
| ERX-ROADMAP-001 v1.0 | ERX-PROT-001 v1.1 | Foundational reference | Roadmap Section 1 foundation | Does not mean Roadmap rewrites Protocol |
| ERX-ROADMAP-001 v1.0 | ERX-ATLAS-001 v1.1 | Foundational reference | Roadmap Section 1 foundation | Atlas remains its own source |
| ERX-ROADMAP-001 v1.0 | UTXO-911-001 v1.0 | Foundational reference | Roadmap Section 1 foundation | Functional relationship needs detailed alignment |
| ERX-ROADMAP-001 v1.0 | ERX-CONSENSUS-001 v0.1 | Cited coordination reference; source identity/content confirmed; proposal for review | Roadmap §1; text source `docs/Consenso ERX byLAEV`; PDF counterpart | Direct text-source comparison confirms ID/version and substantive framework; DOC-ISS-011 tracks operational completeness and authority |
| ERX-ROADMAP-001 v1.0 | ERX-IMPL-PROPOSAL-001 | Unverified reference | Roadmap cites source | Content and provenance unavailable |
| FND-005 Technical Response | ERX-ROADMAP-001 v1.0 | Response/review | Title and two-page content | Not an amendment without express approval evidence |
| ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Graphical representation | Protocol three-transaction lifecycle; Atlas Plates 01–04 and 05–08 | Exact clause-to-plate verification remains bounded by the Atlas correspondence table |
| UTXO-911-001 v1.0 | ERX-PROT-001 v1.1 / ERX-ATLAS-001 v1.1 | Structural state-model divergence requiring disposition | UTXO Sections 2.1–2.5 and 3.1; Protocol Step 15 (PDF p.13); Atlas Plates 02–03 | UTXO-911 creates a separate call-acceptance UTXO before the initial-protocol UTXO; Protocol/Atlas create UTXO 02 directly from UTXO 01 with contact and initial-protocol result. LAEV must decide separate spendable output vs acceptance event/sub-state; see DOC-ISS-009 / DP-02 |
| UTXO-911-001 v1.0 | ERX-ROADMAP-001 v1.0 / Technical Response FND-005 | Functional support for an independently linked agent-availability cycle | UTXO Sections 4.5–5 (PDF pp.8–9); Roadmap Section 3.1 (PDF p.3); Technical Response p.1 | Roadmap expressly establishes two related but independent cycles; the unresolved work is detailed state-machine specification, not architectural separation |\n| WP-0.2 | WP-0.3 | Governance dependency | Workplan Section 4 and WP-0.3 dependency | WP-0.2 acceptance authorizes WP-0.3 |
| WP-0.3 | WP-0.4 | Governance dependency | Workplan WP-0.4 dependency | WP-0.4 formal execution remains blocked until WP-0.3 is completed and approved |
| WP-0.3 | WP-0.5 | Governance dependency | Workplan WP-0.5 dependency | WP-0.5 formal execution remains blocked until WP-0.3 and WP-0.4 are approved |
| WP-0.2 through WP-0.5 | WP-0.6 | Governance dependency | Workplan WP-0.6 dependency | Master index formal acceptance requires these packages |

## 4. Functional alignment observations
- ERX-PROT-001 v1.1 Sections 1–9 define three communication transactions and their institutional purpose.
- ERX-PROT-001 v1.1 Section 10 defines mandatory uniqueness and double-spend prevention properties.
- UTXO-911-001 v1.0 Sections 2.1–2.5 describe call request and a separate call-acceptance UTXO; Section 3.1 describes a further initial-protocol UTXO; Sections 4.1–4.5 describe communication closure and a new agent-availability output.
- ERX-ROADMAP-001 v1.0 Section 3.1 (PDF p.3) expressly adopts Cycle A — three communication UTXOs — and Cycle B — the separate agent-availability state cycle.
- Technical Response to ERX-ROADMAP-001, page 1, supports independent cycles for 911 communication and agent availability.
- ERX-ATLAS-001 v1.1 Plates 02–04 correspond to the three communication stages; Plate 05 depicts the UTXO double-spend engine; Plate 06 depicts OTS; Plates 07–08 depict exception/continuity and verification/privacy.
- Atlas's own correspondence table maps Protocol purpose/architecture to Plate 01; participants and prerequisites to Plates 01–02; transaction 1 to Plate 02; transaction 2 to Plate 03; transaction 3 to Plate 04; uniqueness to Plate 05; OTS to Plate 06; exceptions and continuity to Plate 07; privacy and verification to Plate 08.

These are source-derived observations. The independence of the agent-availability cycle is expressly stated in Roadmap 3.1. The remaining structural question is the representation of call acceptance in UTXO-911 versus the direct UTXO 01 → UTXO 02 transition in Protocol/Atlas.

## 5. Work package dependencies
The official Workplan dependency chain is:
- WP-0.1 enables WP-0.2.
- WP-0.2 enables WP-0.3.
- WP-0.3 enables WP-0.4 and WP-0.5.
- WP-0.2 through WP-0.5 enable WP-0.6.
- WP-0.3 and WP-0.6 enable WP-0.7.
- WP-0.3, WP-0.6 and WP-0.7 enable WP-0.8.
- WP-0.6 through WP-0.8 enable WP-0.9.
- WP-0.1, WP-0.3 and WP-0.7 through WP-0.9 enable WP-0.10.
- WP-0.4 through WP-0.6 and WP-0.10 enable WP-0.11.
- WP-0.1 through WP-0.11 feed WP-0.12.

## 6. Open relationships
1. Exact mapping of UTXO-911's separate call-acceptance output to Protocol UTXO 01 → UTXO 02 (DOC-ISS-009).
2. Detailed transitions, permissions, release and recovery conditions for the Roadmap's independent agent-availability cycle (DOC-ISS-010; architectural separation already source-confirmed).
3. Normative force of each Atlas plate in the event of textual divergence.
4. Formal effect, if any, of the Technical Response on Roadmap.
5. DOC-ISS-011 consensus proposal status/completeness; ERX-IMPL-PROPOSAL-001 remains not located (DOC-ISS-003).

## 7. Status
**APPROVED WP-0.3 RELATIONSHIP BASELINE.** The source relationships and scoped dispositions are approved by ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0. The map remains descriptive and does not create precedence beyond the approved subject-matter matrix.

---
END
