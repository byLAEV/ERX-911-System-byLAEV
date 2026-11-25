# ERX-WP-0.3-LAEV-DECISION-PACKAGE-001
## Documentary Authority, UTXO Mapping and Open Source Dispositions

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.3-LAEV-DECISION-PACKAGE-001 |
| Version | 0.4.0 |
| Status | DECISION PROPOSALS — PENDING LAEV REVIEW |
| Work Package | WP-0.3 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Decision authority | LAEV |
| Evidence baseline | Five original PDFs; supplemental repository discovery; direct text and visual inspection |
| Date | 2026-11-24 |

## 1. Purpose
This package converts the open documentary issues into explicit decision items. It presents source evidence, alternatives, a recommended treatment and the effect of each choice. It does not make decisions on LAEV's behalf and does not amend any foundational source.

## 2. Source authority and interpretation

### DP-01 — Scope and subject-matter authority of the foundational documents
**Evidence**
- ERX-PROT-001 v1.1 identifies itself as the institutional protocol specification and defines the three-transaction communication chain.
- ERX-ATLAS-001 v1.1 identifies ERX-PROT-001 v1.1 as its related normative document; its correspondence table maps Protocol topics to Plates 01–08.
- UTXO-911-001 v1.0 describes the functional 911 communication lifecycle, including request, acceptance, initial operator protocol, closure and agent availability.
- ERX-ROADMAP-001 v1.0 identifies ERX-PROT-001 as institutional norm, ERX-ATLAS-001 as diagrams/representation, UTXO-911-001 as the UTXO-cycle foundation, and ERX-CONSENSUS-001 as a coordination reference.

**Proposed allocation**
- ERX-PROT-001: textual institutional protocol and the three-stage communication transaction model.
- ERX-ATLAS-001: graphical and operational representation of ERX-PROT-001; it does not silently override the Protocol text.
- UTXO-911-001: functional source describing additional event and agent-availability detail; any structural divergence from Protocol/Atlas requires an approved mapping or amendment.
- ERX-ROADMAP-001: development sequence, dependencies, architecture direction and progression criteria.
- Technical Response to ERX-ROADMAP-001: technical response and recommendation; not a Roadmap amendment without an express approval record.

**Recommendation:** adopt this scoped allocation without declaring universal precedence among all foundational sources. Where a specific statement differs, record the exact clause/section/plate and decide its scope before applying it.

LAEV decision: PENDING — ADOPT / REVISE / REJECT.

## 3. Communication UTXO model

### DP-02 — Request and acceptance states: separate UTXO or sub-state
**Exact evidence**
- UTXO-911-001 v1.0, Sections 2.1–2.5: creates a call-request UTXO; when an operator accepts, the request UTXO is consumed and a new call-acceptance UTXO is generated.
- UTXO-911-001 v1.0, Sections 3.1–3.5: after the agent has accepted, a further UTXO of initial operator protocol is generated.
- UTXO-911-001 v1.0, Sections 4.1–4.5: communication closure consumes the active communication state and creates a closure state, then creates a new agent-availability UTXO.
- ERX-PROT-001 v1.1, Sections 1–2 and 6–8: defines UTXO 01 for reception/origin/routing, UTXO 02 for contact establishment and initial protocol, and UTXO 03 for development and closure.
- ERX-PROT-001 v1.1, Section 7, Step 15: explicitly consumes UTXO 01 and creates UTXO 02 after recording contact, agent identity and initial protocol result.
- ERX-ATLAS-001 v1.1, Plates 02–05 and its correspondence table: depicts the same three-state chain; Plate 05 states UTXO 02 consumes UTXO 01 and UTXO 03 consumes UTXO 02.
- ERX-ROADMAP-001 v1.0, Section 3.1: adopts the three-UTXO communication cycle and separately defines agent availability.

**Finding**
UTXO-911-001 describes a distinct call-acceptance UTXO between request and initial protocol. Protocol and Atlas do not show that as an additional spendable output; their UTXO 02 represents the contact result and initial protocol after consuming UTXO 01. This is a structural difference in the state model, not merely a wording difference. The sources do not establish whether the acceptance UTXO is intended as a separately spendable ledger output or as a logical sub-state/event that should be represented inside the Protocol's UTXO 02.

**Options**
- A — Separate spendable acceptance output: preserve UTXO-911-001 literally and formalize a four-output per-call chain (request → acceptance → initial protocol/contact → closure). ERX-PROT-001 and Atlas would require an approved revision or a clearly scoped extension.
- B — Acceptance as an internal sub-state/event: preserve the three-output Protocol/Atlas chain. Record the acceptance event with its own event identifier, timestamp, operator identity and idempotency key inside the transition that consumes UTXO 01 and creates UTXO 02. UTXO-911-001 would require an approved clarification or derivative mapping so the term “UTXO de aceptación” is not misrepresented as a separate spendable output.
- C — Parallel compatibility profiles: maintain the three-UTXO normative profile and a separately identified UTXO-911 functional profile, with explicit conversion/correlation rules. This increases complexity and requires strict profile identification.

**Recommendation for LAEV consideration:** Option B is the least disruptive reconciliation if ERX-PROT-001 v1.1 and Atlas v1.1 remain the controlling three-output communication model. However, this recommendation changes the interpretation of the explicit “new UTXO” language in UTXO-911-001 and therefore must not be applied without LAEV's express decision and a controlled clarification. If LAEV intends the acceptance event to be an independent spendable state, choose Option A and authorize the corresponding protocol/Atlas amendment.

LAEV decision: PENDING — A / B / C / OTHER.

## 4. Agent availability cycle

### DP-03 — Independent availability state machine
**Exact evidence**
- UTXO-911-001 v1.0, Sections 4.5, 5 and 6: defines an agent-availability UTXO independent from each call's UTXOs; it is consumed when the agent accepts a new call and must not be used for simultaneous incompatible acceptances.
- ERX-ROADMAP-001 v1.0, Section 3.1: expressly establishes two related but independent cycles: Cycle A — Communication 911 (UTXO 01–03), and Cycle B — agent availability (AVAILABLE → ASSIGNED/ACCEPTED → BUSY → RELEASE AND NEW AVAILABILITY). It says the agent cycle does not reuse call UTXOs and is related by identity, assignment and session references.
- Technical Response to ERX-ROADMAP-001, page 1: explicitly supports keeping 911 communication UTXO cycles and agent availability UTXO cycles independent.
- ERX-PROT-001 v1.1 and Atlas v1.1 describe the three communication UTXOs; they do not fully detail the separate agent availability cycle.

**Finding**
The independence of the agent-availability cycle is already an explicit Roadmap architectural decision, supported by UTXO-911-001 and the Technical Response. The remaining work is to specify the state machine, permitted transitions, authoritative actor, relationship to call assignment, busy/paused states, transfer behavior, release conditions and recovery rules.

**Recommendation:** accept the two-cycle architecture as the Roadmap baseline. Carry detailed state-transition specification, edge cases and verification criteria into WP-0.7/WP-0.8 or the applicable later normative package. Do not collapse agent availability into UTXO 01–03 or permit an availability output to be reused.

LAEV decision: PENDING — ACCEPT SOURCE-CONFIRMED SEPARATION / REVISE / ASSIGN DETAIL TO WP.

## 5. Atlas normative treatment

### DP-04 — Rule for diagram/text divergence
**Evidence**
- ERX-ATLAS-001 v1.1 control section identifies ERX-PROT-001 v1.1 as its related normative document.
- Atlas correspondence table maps Protocol sections to Plates 01–08.
- Atlas Plate 05 depicts the same three-output UTXO chain and the same single-consumption/atomicity principles as Protocol Section 10.

**Recommendation:** use Protocol clauses as the textual normative reference and Atlas plates as the controlled graphical representation. If a plate appears to differ from a clause, do not silently select one: register the exact clause/plate pair, preserve the plate, assess impact, and obtain LAEV disposition. Any corrected plate must be issued as a controlled derivative or new approved version.

LAEV decision: PENDING — ADOPT / REVISE / REJECT.

## 6. Technical Response effect

### DP-05 — Does the Technical Response amend the Roadmap?
**Evidence:** the two-page response calls itself a response to Roadmap observations and states a recommendation to maintain the Roadmap architecture and sequence while incorporating observations as implementation and validation requirements. It conditions acceptance of solutions on implementation, reproducible tests and auditable evidence. No separate approval record or revised Roadmap is present in the inspected evidence.

**Recommendation:** classify FND-005 as a response/review artifact and a source of recommendations. Treat its proposals as unapproved until each is adopted in a controlled decision, requirement or Roadmap amendment.

LAEV decision: PENDING — RESPONSE ONLY / APPROVED AMENDMENT / PARTIAL ADOPTION.

## 7. Metadata and source availability

### DP-06 — Atlas filename and internal version
Preserve the supplied filename ERX-ATLAS-001 v1.pdf. Cite the internal document identity as ERX-ATLAS-001 v1.1. Do not overwrite or rename the original without a controlled alias/canonical-name record and checksum linkage.

LAEV decision: PENDING — ACCEPT PROPOSED CITATION / OTHER.

### DP-07 — Technical Response metadata
The supplied response does not state a formal document identifier, version or issue date in its inspected title/control content. Preserve those fields as NOT STATED. If a repository catalogue identifier is assigned, distinguish it from an identifier originally printed in the source.

LAEV decision: PENDING — ACCEPT CATALOGUE-ONLY IDENTIFICATION / OTHER.

### DP-08 — ERX-CONSENSUS-001 v0.1: identity confirmed; proposal status and operational completion
The repository text source `docs/Consenso ERX byLAEV` directly declares identifier ERX-CONSENSUS-001, version 0.1 — Propuesta normativa, status Documento de diseño para revisión, and authorship LAEV/byLAEV. This matches ERX-ROADMAP-001 v1.0 §1; identity is confirmed from content, not filename.

Decision options: (A) retain as a source-level proposal/reference pending express approval; (B) approve its conceptual framework with defined scope and separately commission the missing operational specification; (C) revise or reject it through a controlled LAEV decision. The source itself defers quorum, validator count/independence, conflict resolution, detailed consensus UTXO/JSON structures and derived specifications. See DOC-ISS-011.

Recommendation: do not treat the source identity check as approval or operational completeness. Assign a consensus completion package and acceptance criteria before multi-institutional use.

LAEV decision: PENDING — A / B / C.

### DP-09 — ERX-IMPL-PROPOSAL-001
The Roadmap cites ERX-IMPL-PROPOSAL-001, but it was not found in the inspected repository tree or five supplied PDFs. Locate and verify the original, or explicitly accept the bounded missing-source limitation with owner, impact and target work package. Do not infer its contents.

LAEV decision: PENDING — LOCATE / ACCEPT LIMITATION / DEFER.

## 8. Consolidated decision register
| Decision | Topic | Proposed treatment | LAEV status |
|---|---|---|---|
| DP-01 | Subject-matter authority | Scoped source allocation; no universal precedence | PENDING |
| DP-02 | Request/acceptance mapping | Option B recommended only if LAEV preserves three-output Protocol/Atlas model | PENDING |
| DP-03 | Agent availability | Accept separate linked cycle per Roadmap 3.1; detail later | PENDING |
| DP-04 | Atlas divergence | Protocol text normative; Atlas graphical representation; register divergences | PENDING |
| DP-05 | Technical Response | Response/recommendation, not automatic Roadmap amendment | PENDING |
| DP-06 | Atlas filename/version | Preserve filename; cite internal v1.1 | PENDING |
| DP-07 | Technical Response metadata | Keep source fields unstated; catalogue-only ID if approved | PENDING |
| DP-08 | Consensus source identity confirmed; proposal status/completeness | Retain proposal status pending express approval; separately assign operational completion criteria | PENDING |
| DP-09 | Implementation proposal | Locate or formally accept limitation/deferment | PENDING |

## 9. Acceptance boundary
These are proposed decisions, not approved decisions. No item becomes binding until LAEV records an express decision with date and rationale. A decision affecting source meaning must be implemented through controlled derivative documentation and synchronized registers. DOC-ISS-010 may be dispositioned as source-alignment-confirmed with detailed specification assigned to a later package, provided LAEV accepts that scope and target. WP-0.3 remains IN_PROGRESS until its acceptance criteria are met.

---
END