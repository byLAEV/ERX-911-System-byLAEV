# ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001
## Evidence-Based Comparison of Foundational Sources

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001 |
| Version | 0.1.0 |
| Status | TECHNICAL REVIEW — PENDING LAEV DISPOSITION |
| Work Package | WP-0.3 / Activity 0.3.6 |
| Sources | FND-001, FND-002, FND-003, FND-004, FND-005 |
| Date | 2026-11-24 |

## 1. Method
The five supplied PDFs were inspected directly. Findings below cite document sections, plates, or control information. This is a documentary alignment review, not a legal opinion and not an implementation validation. A difference in granularity is not labeled a contradiction unless incompatible requirements in the same scope are demonstrated.

## 2. Findings

### F-01 — Atlas identifies Protocol as its related normative document
- Evidence: ERX-ATLAS-001 v1.1 control section, page 1, identifies ERX-PROT-001 v1.1 as “Documento normativo relacionado”.
- Evidence: Atlas correspondence table maps Protocol topics to Plates 01–08.
- Assessment: explicit normative relationship for the Atlas as a graphical representation.
- Disposition: retain as source-derived relationship; detailed interpretation of a specific plate/text divergence remains open.
- Related issue: DOC-ISS-006.

### F-02 — Three communication transactions are consistently represented
- Evidence: ERX-PROT-001 v1.1 Sections 1, 2, 5–9 describe UTXO 01 reception/origin/routing, UTXO 02 contact establishment/initial protocol, and UTXO 03 development/closure.
- Evidence: Atlas Plates 01–04 and correspondence table represent the same three communication stages.
- Evidence: UTXO-911-001 v1.0 Sections 1 and 8 also describe a three-stage communication cycle.
- Assessment: broad three-stage lifecycle correspondence is supported.
- Disposition: relationship accepted as descriptive correspondence; not a full field-by-field equivalence.

### F-03 — UTXO-911 includes more granular request and acceptance states
- Evidence: UTXO-911-001 v1.0 Section 2 describes an initial call-request UTXO and a subsequent call-acceptance UTXO; Section 3 describes the operator's initial communication protocol UTXO.
- Evidence: ERX-PROT-001 v1.1 Sections 6–7 group reception/origin/routing in UTXO 01 and contact establishment/initial protocol in UTXO 02.
- Assessment: possible decomposition of the first two Protocol stages, or a difference in state granularity. Current evidence does not establish whether these are separate ledger outputs, internal sub-states, or alternate terminology.
- Disposition: OPEN — LAEV must decide the intended mapping before requirements extraction.
- Related issue: DOC-ISS-009.

### F-04 — UTXO-911 expressly defines an agent-availability state
- Evidence: UTXO-911-001 v1.0 Sections 4.5 and 5 define a new UTXO of agent availability, independent from each call's UTXOs, and consume it when the agent accepts a new call.
- Evidence: UTXO-911-001 v1.0 Section 6 prohibits simultaneous use of the same availability state for incompatible call acceptances.
- Evidence: ERX-PROT-001 v1.1 Sections 1–10 define the three communication UTXOs and mandatory uniqueness rules; the inspected sections do not fully specify this separate agent-availability lifecycle.
- Assessment: scope extension or complementary state machine; not proven contradiction.
- Disposition: OPEN — determine whether agent availability belongs to ERX protocol scope, an institutional module, or a separately governed functional subsystem.
- Related issue: DOC-ISS-010.

### F-05 — Atlas includes a dedicated UTXO engine plate
- Evidence: Atlas Plate 05 is titled “Motor UTXO y prevención del doble gasto” and depicts single consumption, atomic transition, rejection of duplicate concurrent consumption, and the three-state chain.
- Assessment: reinforces the Protocol's Section 10 uniqueness properties. Atlas Plate 05 also states the uniqueness boundary is the installation/shared infrastructure coordination domain and does not imply global consensus across all 911 institutions.
- Disposition: descriptive correspondence accepted; exact normative effect remains governed by DOC-ISS-006.

### F-06 — Protocol distinguishes UTXO state from OTS evidence
- Evidence: ERX-PROT-001 v1.1 Sections 10.10 and 12 separate call UTXO state from OTS state; OTS availability does not condition emergency handling.
- Evidence: UTXO-911-001 v1.0 Section 7 describes OTS as temporal evidence for the three stages.
- Evidence: Atlas Plate 06 depicts OTS generation, pending state and later update.
- Assessment: consistent subject-matter alignment in the inspected passages.
- Disposition: record as correspondence; do not treat OTS as a transaction state or a prerequisite to live emergency response.

### F-07 — Technical Response does not evidence a formal Roadmap amendment
- Evidence: FND-005 title and content identify it as a response to Roadmap observations and present recommendations.
- Assessment: no approval or revised Roadmap evidence in the supplied response establishes formal amendment.
- Disposition: treat as response/review artifact unless an express approval record is produced.
- Related issue: DOC-ISS-007.

### F-08 — Missing cited sources remain unassessable
- Evidence: ERX-ROADMAP-001 v1.0 cites ERX-CONSENSUS-001 v0.1 and ERX-IMPL-PROPOSAL-001; neither was included in the five-PDF source set or found in the inspected repository records described by WP-0.2.
- Assessment: their content, provenance and authority cannot be assessed.
- Disposition: carry as explicit limitations; no inference about their requirements or authority.
- Related issues: DOC-ISS-002 and DOC-ISS-003.

## 3. Issue classification
- Confirmed source relationship: Atlas → Protocol (normative relationship as stated by Atlas).
- Confirmed broad correspondence: three-stage communication lifecycle across Protocol, Atlas and UTXO-911.
- Unresolved scope/granularity: request/acceptance state mapping (DOC-ISS-009).
- Unresolved additional lifecycle: agent availability state machine (DOC-ISS-010).
- Unresolved authority/interpretation: DOC-ISS-005 and DOC-ISS-006.
- Unresolved response effect: DOC-ISS-007.
- Missing-source limitations: DOC-ISS-002 and DOC-ISS-003.
- Metadata discrepancy: DOC-ISS-001 and DOC-ISS-004.

No direct contradiction between the inspected passages is declared by this review. Two material scope questions are added for LAEV disposition.

## 4. WP-0.3.6 result
The activity has produced a source-grounded issue classification and comparison record. It is not fully closed because the material scope questions and authority questions require express LAEV dispositions. The issues may be formally deferred with documented impact and mitigation if LAEV decides that their resolution belongs to a later package, but they may not be silently ignored.

---
END
