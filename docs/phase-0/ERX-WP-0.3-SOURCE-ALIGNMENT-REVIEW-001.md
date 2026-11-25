# ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001
## Evidence-Based Comparison of Foundational Sources

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001 |
| Version | 1.0.0 |
| Status | COMPLETED TECHNICAL SOURCE ALIGNMENT — DISPOSITIONS APPROVED |
| Work Package | WP-0.3 / Activity 0.3.6 |
| Sources | FND-001, FND-002, FND-003, FND-004, FND-005 |
| Date | 2026-11-24 |
| Supplemental evidence | ERX-POST-APPROVAL-SOURCE-DISCOVERY-001 v0.1.0 |

## 1. Method
The five supplied PDFs were inspected directly. Findings below cite document sections, plates, or control information. This is a documentary alignment review, not a legal opinion and not an implementation validation. A difference in granularity is not labeled a contradiction unless incompatible requirements in the same scope are demonstrated.

## 2. Findings

### F-00 — Consensus source identity and repository evidence (DOC-ISS-002)
- Primary text source: `docs/Consenso ERX byLAEV`, 15,237 bytes, Git Blob SHA-1 `64154f504b0a1ac48f76a438cf60f368e062eab6`.
- The source control block directly states: Document ID `ERX-CONSENSUS-001`; version `0.1 — Propuesta normativa`; status `Documento de diseño para revisión`; authorship `LAEV / byLAEV`; scope ERX 911 communication and emergency record system.
- Roadmap §1 cites `ERX-CONSENSUS-001 v0.1` as a coordination reference; identity is therefore confirmed by the actual text, not inferred from filename. The PDF counterpart is also present in `docs/`.
- Disposition: close DOC-ISS-002 identity-verification component. Keep source lifecycle/status distinct: proposal for review is not evidence of express approval.



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

### F-03 — UTXO-911 includes a distinct call-acceptance output not shown in the three-output Protocol/Atlas chain
- Evidence: UTXO-911-001 v1.0 Sections 2.1–2.5: the call-request UTXO is consumed on operator acceptance and a new call-acceptance UTXO is generated. Sections 3.1–3.5 then describe a further UTXO for the operator's initial protocol.
- Evidence: ERX-PROT-001 v1.1 Sections 1–2 and 6–8 define UTXO 01 → UTXO 02 → UTXO 03. Section 7, Step 15, says UTXO 01 is consumed and UTXO 02 created after contact establishment and initial protocol results are recorded.
- Evidence: ERX-ATLAS-001 v1.1 Plates 02–05 and the Protocol/Atlas correspondence table depict the same three-output chain; Plate 05 explicitly says UTXO 02 consumes UTXO 01 and UTXO 03 consumes UTXO 02.
- Evidence: ERX-ROADMAP-001 v1.0 Section 3.1 adopts the three-UTXO communication cycle.
- Assessment: this is a structural state-model divergence. UTXO-911 explicitly names a separate call-acceptance UTXO between request and initial protocol; Protocol/Atlas do not show that as an additional spendable output. It may be intended as an intermediate ledger output or as a logical acceptance event/sub-state, but the source text does not settle that interpretation.
- Disposition: OPEN — LAEV must decide whether acceptance is an independent spendable output or a uniquely identified event within the UTXO 01 → UTXO 02 transition. See ERX-WP-0.3-LAEV-DECISION-PACKAGE-001, DP-02.
- Related issue: DOC-ISS-009.

### F-04 — Independent agent-availability cycle is expressly adopted by the Roadmap
- Evidence: UTXO-911-001 v1.0 Sections 4.5–6 define a new agent-availability UTXO, independent from each call's UTXOs, and consume it when the agent accepts a new call.
- Evidence: ERX-ROADMAP-001 v1.0 Section 3.1 expressly establishes two related but independent cycles: Cycle A — Communication 911 (UTXO 01–03); Cycle B — agent availability (AVAILABLE → ASSIGNED/ACCEPTED → BUSY → RELEASE AND NEW AVAILABILITY). It states that the agent cycle does not reuse call UTXOs and is related through identity, assignment and session references.
- Evidence: Technical Response to ERX-ROADMAP-001, page 1, explicitly supports keeping the communication and agent-availability UTXO cycles independent.
- Assessment: the architectural separation is source-confirmed, not an unresolved question. Protocol/Atlas do not fully detail the agent state machine, but the Roadmap establishes its independent scope.
- Disposition: source alignment established. Remaining work is to formalize transition rules, authority, release conditions, exceptions and verification in a later detailed specification. LAEV may accept this bounded treatment in WP-0.3 and assign detailed state-machine work to the applicable later package.
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

### F-08 — Cited sources and supplemental consensus text source
- Evidence: ERX-ROADMAP-001 v1.0 cites ERX-CONSENSUS-001 v0.1 and ERX-IMPL-PROPOSAL-001.
- Supplemental discovery: a PDF named `Consenso ERX byLAEV.pdf` is present at `docs/Consenso ERX byLAEV.pdf` on `main` (Git blob SHA `c2f965c9bf455506571ac4c1635b4fb47af34216`). The filename alone does not establish that it is ERX-CONSENSUS-001 v0.1. Its internal identity, version, provenance and content have not yet been verified.
- ERX-IMPL-PROPOSAL-001 was not located in the inspected repository tree.
- Assessment: DOC-ISS-002 identity/content is confirmed from the text source; DOC-ISS-011 governs proposal status and operational completion. DOC-ISS-003 remains NOT LOCATED / UNVERIFIED.
- Disposition: record the source under its confirmed identifier/version; do not equate identity with approval or complete operational specification.
- Related issues: DOC-ISS-002 and DOC-ISS-003. See ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.

## 3. Issue classification
- Confirmed source relationship: Atlas → Protocol (normative relationship as stated by Atlas).
- Confirmed broad correspondence: three-stage communication lifecycle across Protocol, Atlas and UTXO-911.
- Unresolved scope/granularity: request/acceptance state mapping (DOC-ISS-009).
- Unresolved additional lifecycle: agent availability state machine (DOC-ISS-010).
- Unresolved authority/interpretation: DOC-ISS-005 and DOC-ISS-006.
- Unresolved response effect: DOC-ISS-007.
- Consensus source identity confirmed; consensus operational completeness/authority remains DOC-ISS-011; missing-source limitation remains DOC-ISS-003.
- Metadata discrepancy: DOC-ISS-001 and DOC-ISS-004.

The structural state-model divergence DOC-ISS-009 is resolved by DP-02 (acceptance event/sub-state within UTXO 01→02). The independent agent-availability cycle is confirmed and accepted; detailed state-machine formalization is deferred under DOC-ISS-010. Subject authority, Atlas treatment and Technical Response effect are disposed by DP-01, DP-04 and DP-05. Source metadata limitations and missing ERX-IMPL-PROPOSAL-001 are accepted/deferred under DP-06, DP-07 and DP-09. Consensus operational completeness remains deferred under DP-08 / DOC-ISS-011.

## 4. WP-0.3.6 result
The activity produced a source-grounded issue classification and comparison record. All WP-0.3 material issues have now received a decision or bounded deferral in ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0. The dispositions are reflected in the issue register and CSV companion. Detailed deferred specifications remain visible and must be completed before their respective later uses.

---
END
