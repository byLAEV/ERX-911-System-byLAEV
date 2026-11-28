# ERX-WP-0.7-EXACT-SOURCE-AND-MATRIX-AUDIT-001
## Exact source review, compound-obligation assessment and traceability validation

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-EXACT-SOURCE-AND-MATRIX-AUDIT-001 |
| Version | 0.1.0 |
| Status | WORKING AUDIT — NOT APPROVED |
| Work Package | WP-0.7 / Activities 0.7.2–0.7.11 |
| Date | 2026-11-25 |
| Repository baseline | `wp-0.7-extraction-batch-004` |
| Baseline commit | `3e3c12038feee5a14fcaba9a7f061c020e830f47` |
| Requirements register | `registers/requirements-traceability.csv` — 56 rows / 23 columns |
| Method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 |
| Authority | LAEV — review proposal only; no requirement approval recorded |

## 1. Purpose and limits

This working audit compares the 56 candidate records with the exact text of the five archived foundational PDFs, gives special attention to ERX-ATLAS-001 diagrams, identifies compound obligations, records source conflicts and proposes phase allocation against ERX-ROADMAP-001 v1.0.

It does not amend the original PDFs, adopt an architecture decision, approve a requirement, authorize implementation, release WP-0.8, or authorize Phase 1. All 56 lifecycle statuses remain `EXTRACTED — REVIEW PENDING`. The recommendations below must be reviewed before the canonical CSV is changed.

The page references in this audit mean **physical PDF page numbers**, consistent with the WP-0.7 locator-bounds audit. A section number is recorded separately. Page-bound validity alone does not establish exact passage support.

## 2. Source integrity and review baseline

The SHA-256 values recomputed from the five supplied PDFs match the accepted values in `registers/foundational-material-register.csv`:

| Source | Version | Pages | SHA-256 result |
|---|---:|---:|---|
| ERX-PROT-001 | 1.1 | 29 | MATCH |
| ERX-ATLAS-001 | 1.1 | 29 | MATCH |
| UTXO-911-001 | 1.0 | 12 | MATCH |
| ERX-ROADMAP-001 | 1.0 | 37 | MATCH |
| Technical Response to ERX-ROADMAP-001 | NOT_STATED | 2 | MATCH |

The five binary sources inspected are byte-identical to the archived baseline. FND-005 remains a response/review artifact with no source-native formal ID or version stated. It is not treated as an independent normative source. ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED / UNVERIFIED under DOC-ISS-003 and is not used to support a requirement. ERX-CONSENSUS-001 v0.1 remains a proposal for review under DOC-ISS-011.

The source distribution in the current 56-row register is:

| Source ID | Candidate rows |
|---|---:|
| ERX-PROT-001 | 29 |
| ERX-ROADMAP-001 | 14 |
| UTXO-911-001 | 7 |
| ERX-ATLAS-001 | 6 |
| **Total** | **56** |

## 3. Exact-source findings and proposed locator corrections

The source statements generally support the subject matter of the candidates, but several current locators are incomplete, misnumbered, or assigned to the wrong source. The following corrections are required before any row is marked SOURCE_VERIFIED.

| Requirement ID | Current locator / source | Exact-source finding | Proposed correction |
|---|---|---|---|
| ERX-REQ-KEY-0002 | ERX-PROT-001 p.7, §4.2 | Historical authorized-key lookup, validity periods and revocations are on physical p.6, §4.2. | ERX-PROT-001 p.6, §4.2 |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 p.8, §4.3 | Common core and adapter boundary are on physical p.7, §4.3. | ERX-PROT-001 p.7, §4.3 |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 pp.15–16, Step 19 | Transfer participants and no-duplicate-admission rule are in Step 19 on physical pp.14–15. | ERX-PROT-001 pp.14–15, Step 19 |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 p.16, Step 20 | Closure reasons and prohibition on treating disconnection as normal farewell are on physical p.15, Step 20. | ERX-PROT-001 p.15, Step 20 |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 pp.21–23, “Section 7” | The Protocol supports independent verification without relying on the operational database and lists verification dimensions in physical pp.22–23, §15. The detailed export-package contents are separately enumerated by the Roadmap. | Add ERX-PROT-001 pp.22–23, §15 **and** ERX-ROADMAP-001 p.21, §7.2. Split independent-verification boundary from package-content obligation if separate acceptance outcomes are retained. |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 p.24, “Section 7.3” | The five output states (satisfactory, failed, incomplete, pending, indeterminate) and prohibition on showing unchecked data as satisfactory are in ERX-ROADMAP-001 physical p.21, §7.3. The Protocol supports independent and explicit check results in pp.22–23, §15. | Primary source ERX-ROADMAP-001 p.21, §7.3; supporting source ERX-PROT-001 pp.22–23, §15. |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 pp.7–8, Plate 03 | The flow is on pp.7–8, but the explicit rule distinguishing center identity from agent identity, recording an unverified agent and continuing attention is on p.9. Protocol p.8 also states that ERX validation must not delay or block telephone attention. | ERX-ATLAS-001 pp.7–9, Plate 03 and authentication rules; cross-reference ERX-PROT-001 p.8, Step 2. |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 p.8, Plate 03 | The diagram branch records “no response”; the explicit prohibitions on inventing an identity or nonexistent conversation and the instruction to record the contact attempt are on p.9. The Atlas coordination rule repeats the no-invention boundary on p.28. | ERX-ATLAS-001 pp.8–9 and p.28; supporting ERX-PROT-001 p.23, §16.3. |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 p.19, Plate 06 | The seven lifecycle states and “pending must never be represented as anchored” are on p.19. The Protocol p.10 and Roadmap Phase 6 use related but non-identical labels. | Keep Atlas p.19 as the direct source; add cross-source ambiguity reference to ERX-PROT-001 p.10, Step 8 and ERX-ROADMAP-001 Phase 6.2. |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 pp.27–28 | The eight separated verification categories are listed on physical p.27. Physical p.28 contains the Protocol/Atlas correspondence table and coordination rules. | ERX-ATLAS-001 p.27 for the eight outputs; p.28 only for cross-document rules. |
| ERX-REQ-VERIFY-0005 | ERX-ATLAS-001 p.28, “Categories of verification” | The exact material-truth limitation is on physical p.27, following the eight verification categories. ERX-PROT-001 §12.3, physical p.20, independently states what OTS does not prove. | ERX-ATLAS-001 p.27 and ERX-PROT-001 p.20, §12.3. |
| ERX-REQ-OPS-0004 | ERX-PROT-001 p.25, §16.8 | Durable protected local queue and separate event/recovery/commitment times are on physical p.24, §16.8. | ERX-PROT-001 p.24, §16.8 |
| ERX-REQ-OPS-0005 | ERX-PROT-001 p.26, §17.2 | The nine recovery actions are on physical p.25, §17.2. | ERX-PROT-001 p.25, §17.2 |
| ERX-REQ-OPS-0006 | ERX-PROT-001 p.25, §16.9 | Persistence, backup, recovery and storage-confirmation condition are on physical p.24, §16.9. | ERX-PROT-001 p.24, §16.9 |
| ERX-REQ-SEC-0001 | ERX-PROT-001 p.26, §17.3 | Interface authentication, transport protection, role authorization, message validation and transition restriction are on physical p.25, §17.3. | ERX-PROT-001 p.25, §17.3 |
| ERX-REQ-TEST-0002 | ERX-PROT-001 p.26, §19.1 | The 20 mandatory pre-implementation test subjects are on physical p.27, §19.1. Physical p.26 contains §19 component structure. | ERX-PROT-001 p.27, §19.1 |
| ERX-REQ-AVAIL-0003 | ERX-ROADMAP-001 pp.4–5, §3.1 | The independent communication/agent-availability cycle rule begins on physical p.3 and continues on p.4. | ERX-ROADMAP-001 pp.3–4, §3.1 |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 p.23, §8.1 | The adapter-specific input/output/authentication/error/retry/duplicate contract is in the body of §8.1 on p.23; the §8.1 heading and integration context begin on p.22. | ERX-ROADMAP-001 pp.22–23, §8.1 |

The remaining candidate mappings have not yet all received a complete row-by-row exact-passage audit in this pass. Their existing source IDs, versions and page bounds are present, but they must remain SOURCE REVIEW PENDING until each passage, modality and scope is checked. This working paper therefore does not claim 56/56 exact-source verification. The corrections above are not yet applied to the canonical CSV.

## 4. Additional source links required

Two verifier requirements need more than one source to support the complete wording:

1. **ERX-REQ-VERIFY-0001:** ERX-PROT-001 §15 supports independent verification without exclusive reliance on the production database and defines the verification domains. ERX-ROADMAP-001 §7.2 supplies the exact exported evidence bundle (JSON 01–03, transition records, certificates/trust references, signatures, OTS proofs, file manifests and historical identity references). A single-source locator is insufficient.
2. **ERX-REQ-VERIFY-0002:** ERX-ROADMAP-001 §7.3 supplies the five verifier result states and the rule that unchecked data cannot be shown as satisfactory. The current attribution to ERX-PROT-001 §7.3 is not supported by the source structure.

A many-to-many source-to-requirement relationship is preferable to placing several document IDs in a single source_id field. A controlled requirement-source-link register should be added before the canonical matrix is revised.

## 5. Atlas diagram review

The following Atlas passages were visually inspected, not only extracted from text:

- **Plate 03 / physical pp.7–9:** UTXO 01 active → center identified → connection event → center connected → response decision. The “yes” branch identifies and validates the agent; valid and unverified outcomes are recorded distinctly. The “no” branch records no response. The following text expressly says center and professional-agent identities are separate validations, unverified identity must be recorded, and attention must not stop. It also prohibits inventing a professional identity or nonexistent conversation.
- **Plate 06 / physical p.19:** commitment → OTS service → hash aggregation → root commitment → Bitcoin anchor → OTS update → independent verification. Seven evidence states are listed. A pending proof is not an anchored proof.
- **Plate 08 / physical pp.25–27:** private institutional information is separated from public commitments; original records remain in protected institutional storage; public disclosure is limited to commitments and minimum temporal-proof data; the independent verifier checks documents, signatures, UTXO chain, consumption, OTS, file hashes and chronology. The eight result categories and the material-truth limitation are on p.27.
- **Cross-document control / physical p.28:** the Atlas maps Protocol sections to Plates 01–08 and states 14 coordination rules, including the three-output chain, asynchronous OTS, no fabricated identity/conversation, transfer continuity, private custody and the distinction between cryptographic verification and material truth.

### Atlas findings

1. AGENT-0001 and AGENT-0002 currently point only to diagram pages; their explicit text rules on p.9 and the cross-document rule on p.28 must be linked.
2. The Atlas eight-category verifier output is not identical to the Roadmap's ten verifier functions in §7.1. They are related taxonomies, not silently interchangeable lists. A crosswalk is required.
3. The Atlas OTS state labels are not textually identical to the Protocol/Roadmap labels. A controlled state crosswalk is required.
4. Atlas is a graphical/operational representation under DP-01, not a silent amendment to ERX-PROT-001. Atlas-only detail must be checked against the approved subject-matter authority boundary; where no direct Protocol counterpart exists, retain it as a design/source interpretation pending disposition rather than silently promoting it.

## 6. Compound-obligation decomposition

The method in ERX-REQUIREMENTS-METHOD-001 §8 requires one candidate per independently verifiable obligation and splitting where separate verification outcomes are needed. The following parent candidates contain multiple obligations or independently testable controls. “Split” below means create traceable child candidates or separate acceptance checks; it does not mean delete the parent or silently rewrite it.

| Parent requirement | Decomposition required |
|---|---|
| UTXO-0001 | Separate transition consumption/creation from historical retention of consumed state. Scope the rule to transitions with a prior state; preserve the Atlas rule that the first UTXO issuance consumes no prior state. |
| UTXO-0002 | Keep as a UTXO data-contract parent if validated as one schema; separately enumerate required identity, call/stage, document, predecessor, consumption, process, time and signature fields as schema assertions. |
| UTXO-0004 | Separate persistent event identity, storage uniqueness, atomicity, concurrency control, idempotency, transition history and safe recovery. Preserve the authorized-coordination-scope limitation. |
| UTXO-0006 | Separate canonicalization-profile obligation from institutional document-signing obligation. |
| UTXO-0007 | Separate event/uniqueness binding from atomic UTXO 01 creation. |
| UTXO-0008 | Separate OTS lifecycle-state reporting from non-interference with emergency attention. |
| UTXO-0009 | Separate persistent call identity, no duplicate admission on retransmission, atomic consumption/creation and idempotent retry result. |
| UTXO-0011 | Separate one-time consumption, validation preconditions (existence/current validity/authorization/no prior consumption) and atomic state update. |
| INST-0001 | Retain a validated installation-configuration parent; make each source-listed configuration domain independently checkable. |
| PRIV-0001 | Separate conditional custody of the original audio from metadata/format/hash/time/retention recording. Preserve the “where institutionally authorized” condition. |
| TRANS-0001 | Separate transfer participant/metadata recording from the no-duplicate-admission invariant. |
| CLOSE-0001 | Separate the termination-reason taxonomy from the specific rule that a disconnect is not a normal farewell. |
| VERIFY-0001 | Separate verifier independence/no production-database dependency from required exported evidence-package contents. |
| VERIFY-0002 | Separate the five result states from the rule that unverified data cannot be shown as satisfactory. |
| AGENT-0001 | Separate center-vs-agent validation, recording unverified-agent status and non-blocking emergency attention. |
| AGENT-0002 | Separate recording the no-response/contact-attempt condition from the prohibition on fabricating identity or conversation. |
| VERIFY-0003 | Separate the eight Atlas verification outputs into independently reportable categories; preserve a crosswalk to Roadmap §7.1. |
| AVAIL-0002 | Separate identity/availability state separation, call-specific linked cycles and no reuse of consumed call states. |
| STATE-0002 | Keep the transition specification as a contract parent; validate input, authority, precondition, action, output, evidence and failure handling as distinct fields. |
| INV-0004 | Separate non-resurrection of consumed states from non-resurrection of revoked credentials. |
| CRYPTO-0001 | Keep a signature-profile parent; independently verify algorithm, format, signer, certificate, trust reference, signing time, historical validation, revocation and rotation fields. |
| CRYPTO-0002 | Separate the mandatory non-circular document/UTXO relationship from the Roadmap's recommendation to separate event document and transition record. The latter is not an adopted requirement. |
| TRANS-0002 | Keep an interinstitutional transfer-protocol parent; separately validate source/destination, authority, call identity, transfer state, receipt, responsibility, interruption and reconciliation. |
| OPS-0004 | Separate conditional durable protected local queue from recording the three distinct times. |
| OPS-0005 | Retain a recovery-workflow parent and make the nine source-listed recovery actions separately testable. |
| OPS-0006 | Separate persistence/backup/recovery capability from the storage-confirmation rule. |
| SEC-0001 | Separate mutual authentication/equivalent, transport protection, role authorization, message validation and prohibition on unauthorized transitions. |
| PRIV-0002 | Separate institutional custody, public disclosure limitation and non-publication of call content to Bitcoin. |
| AVAIL-0003 | Separate independent-cycle relationship/reference requirements from the prohibition on substituting UTXO 03 for agent-availability UTXO. |
| OTS-0002 | Separate retention of commitments/proofs/verification data from asynchronous proof acquisition and non-blocking emergency care. |

No child requirement IDs are assigned in this working paper. They must be allocated only after the decomposition is confirmed, to prevent duplicate IDs and preserve the original 56 parent records and their change history.

## 7. Contradictions, ambiguities and boundaries

| ID | Finding | Required treatment |
|---|---|---|
| SRC-AMB-001 | OTS lifecycle labels differ: Protocol p.10 uses “No solicitado / Enviado / Pendiente / Actualizable / Anclado / Verificado / Fallido”; Atlas p.19 uses “Solicitud no enviada / Solicitud enviada / Prueba pendiente / Prueba actualizable / Prueba anclada / Prueba verificable / Error de generación o actualización”; Roadmap Phase 6.2 gives technical identifiers. | Create an approved state crosswalk. Do not normalize “verificable” to “verificado” or “error” to “failed” without a decision. |
| SRC-AMB-002 | Protocol §2.2 scopes uniqueness to an authorized coordination domain and does not assume a global shared state across independent databases; Roadmap §8.2 requires a specific interinstitutional transfer protocol. | Not a contradiction. Preserve local uniqueness scope and treat multi-center transfer authority/coordination as a separate Phase 8 design obligation. |
| SRC-AMB-003 | Atlas presents eight verifier result categories; Roadmap §7.1 lists ten functions/categories. | Build a crosswalk; preserve the distinction between source taxonomies. |
| SRC-AMB-004 | Protocol §2.1 says a valid transition consumes a prior state, while Atlas p.28 states the first UTXO issuance consumes no prior state. | Clarify UTXO-0001 as applying to subsequent transitions with an input; retain initial issuance as an explicit exception. |
| SRC-AMB-005 | UTXO-911-001 describes a separate call-acceptance UTXO; Protocol/Atlas use three spendable communication outputs. | Already resolved by DP-02: acceptance is a uniquely identified event/sub-state within UTXO 01→02, not a fourth spendable output in the approved profile. Do not reopen without a new decision. |
| SRC-AMB-006 | Agent identity/availability is detailed in Atlas/UTXO-911, while Roadmap §3.1 and DP-03 establish an independent availability cycle. | Architectural separation is adopted; detailed transitions, authority, release and recovery remain Phase 1 specification work. |
| SRC-AMB-007 | The Technical Response supports local atomic operations and says distributed consensus should not be imposed where unnecessary; Roadmap §11.3 requires a separate consensus specification before using consensus for multi-institutional coordination. | Not a contradiction. Do not impose distributed consensus on local transitions; do not use multi-institutional consensus until separately specified and approved. FND-005 remains a response, not a Roadmap amendment. |
| SRC-AMB-008 | Installation configuration/homologation is not the same as legal authority to receive emergency calls. | Preserve Protocol §19.2 and Roadmap Phase 11.1 as separate technical and legal/administrative conditions. A dedicated requirement is missing from the current 56. |
| SRC-AMB-009 | Recording is conditional on institutional authorization; audio custody cannot be generalized to every jurisdiction or installation. | Preserve the conditional modality in PRIV-0001 and add jurisdiction-specific authorization/retention decisions where needed. |
| SRC-AMB-010 | Protocol §17.1 requires validation, signature, storage and OTS not to introduce waits conditioning human attention; OPS-0001 currently captures only the failure/telephone-continuity aspect. | Expand decomposition or add a separate requirement for non-blocking processing under normal/degraded operation. |

## 8. Proposed phase allocation — 56 candidates

The following is a **proposed primary phase** for the phase-allocation field. Secondary implementation and verification touchpoints are shown in the rationale. This is not an approval of requirements or authorization to execute the phases.

| Proposed primary phase | Requirement IDs | Allocation basis |
|---|---|---|
| Phase 1 — Normative closure and state model | UTXO-0001, UTXO-0002, UTXO-0003, UTXO-0004, UTXO-0005, UTXO-0007, UTXO-0009, UTXO-0010, UTXO-0011, OPS-0001, OPS-0003, CLOSE-0001, AVAIL-0001, AVAIL-0002, AVAIL-0003, STATE-0001, STATE-0002, INV-0001, INV-0002, INV-0003, INV-0004, INV-0005 | These define UTXO identity/transition semantics, state machines, exceptions, invariants, non-interference boundary and the separate agent-availability cycle. Core execution later belongs to Phase 4; tests to Phase 9. |
| Phase 2 — Formal data and cryptography | UTXO-0006, DATA-0001, CRYPTO-0001, CRYPTO-0002 | Canonicalization, JSON schema/version/validation and document/signature/UTXO cryptographic relationships are Phase 2 deliverables. |
| Phase 3 — Software architecture and infrastructure | OPS-0002, INT-0001, ARCH-0001, OPS-0004, OPS-0006, ARCH-0002 | Persistence/atomicity architecture, API/adapter contracts, common-core boundary, durable queue, backup/recovery architecture and four-component product structure are designed in Phase 3. Actual adapter integration is Phase 8; storage/recovery tests are Phase 9. |
| Phase 4 — ERX Core development | OPS-0005 | The recovery workflow is implemented by the Core recovery functionality; Phase 9 validates it under failures and concurrency. |
| Phase 5 — Identity, trust and security | INST-0002, KEY-0001, KEY-0002, AGENT-0001, AGENT-0002, SEC-0001 | Institutional/professional identity, credentials, historical trust, key custody and secure interfaces map to Phase 5. Institutional adapter activation is later in Phase 8. |
| Phase 6 — Evidence and OpenTimestamps | UTXO-0008, UTXO-0012, PRIV-0001, OTS-0001, PRIV-0002, OTS-0002 | OTS lifecycle, asynchronous evidence, evidence retention, file/audio custody and privacy of commitments map to the Evidence Engine and Phase 6.4. Recording adapter integration remains Phase 8. |
| Phase 7 — ERX Verifier | VERIFY-0001, VERIFY-0002, VERIFY-0003, VERIFY-0004, VERIFY-0005 | Exported evidence, result states, separated verification outputs, verifier independence and cryptographic/material-truth boundaries are verifier functions. |
| Phase 8 — Institutional integration | INST-0001, INST-0003, TRANS-0001, TRANS-0002 | Validated institutional configuration, jurisdiction/routing sources, transfer records and interinstitutional transfer protocol are integration/homologation-facing obligations. Phase 11 verifies each installation's conformity and legal authorization. |
| Phase 9 — Tests, audit and recovery | TEST-0001, TEST-0002 | Test-category coverage and the 20 Protocol test subjects are explicit Phase 9 deliverables. |

Count check: Phase 1 = 22; Phase 2 = 4; Phase 3 = 6; Phase 4 = 1; Phase 5 = 6; Phase 6 = 6; Phase 7 = 5; Phase 8 = 4; Phase 9 = 2; **total = 56**.

No candidate is primarily assigned to Phase 0, 10 or 11. Phase 0 is the governance/requirements-preparation context; Phases 10 and 11 are operational pilot and homologation gates, and the current register lacks explicit candidate coverage for several of their conditions.

## 9. Missing or underrepresented requirement candidates

The 56 rows do not exhaust all requirement-bearing material in the inspected sources and Roadmap. The following gaps should be considered for additional candidates, with source status and modality preserved:

1. **Legal/administrative authorization:** Protocol §19.2, physical p.27, says software installation does not constitute legal authorization to receive emergency calls; Roadmap Phase 11.1 requires each center's authority and homologation. Candidate gap, Phase 11.
2. **Shadow-mode restrictions:** Roadmap Phase 10.2 says the official infrastructure continues to receive/attend calls and ERX does not make dispatch decisions or control call assignment. Candidate gap, Phase 10.
3. **Quantitative acceptance targets:** Roadmap §9.3, physical p.25, requires numerical objectives to be established before testing for latency, processing, duplicates, recovery, integrity, verifiability, event loss and reconciliation. Candidate gap, Phase 9.
4. **Normal-operation non-interference:** Protocol §17.1, physical p.25, says validation, signing, storage and OTS must not introduce waits conditioning human attention. OPS-0001 currently captures only ERX failure continuity; a distinct obligation is needed.
5. **Identity-authority outage:** Protocol §16.10, physical p.24, requires the call to continue, identity to remain pending/unverified and no default success. INST-0002 captures state names but not this operational behavior.
6. **Unrecognized institutional identity handling:** Protocol §16.2, physical p.23, requires an observation/rejection record, differentiated identity/certificate/authorization/impersonation/authority-unavailable states, and says a failure does not automatically prove fraud.
7. **Retention and authorized deletion:** Protocol §13.2, physical p.21, requires retention periods and deletion procedures under applicable law and prohibits representing deletion of content as deletion of an already published Bitcoin anchor.
8. **Key lifecycle completeness:** Protocol §4.2, physical p.6, enumerates generation, custody, rotation, revocation, renewal, recovery, usage logging, separation of duties and historical signature validation. KEY-0001/0002 cover only part of that list.
9. **First UTXO issuance:** Atlas p.28 expressly says first UTXO issuance consumes no prior state. This must be represented as an exception/positive rule alongside UTXO-0001.
10. **Product boundary:** Protocol §20 states ERX does not replace the emergency number, telephone network, dispatch system, agent judgment or public authority. Decide whether to record this as a scope constraint rather than a functional requirement.
11. **Identity validation delay:** Protocol §8 Step 2 and Atlas Plate 03 say identity validation must not delay or block telephone attention; preserve this independently from the OTS-specific non-blocking rule.
12. **OTS/Bitcoin outage:** Protocol §16.7, physical p.24, requires documents, signatures and commitments to be retained while proofs are updated later. Current OTS candidates only partially represent this behavior.

These are extraction gaps, not approved new requirements. Each must receive a source locator, origin/modality, decomposition review and stable ID only after its inclusion is confirmed.

## 10. Matrix structural validation

The current CSV was parsed and checked programmatically against its header and row structure.

| Check | Result |
|---|---:|
| Columns | 23 |
| Candidate rows | 56 |
| Unique requirement IDs | 56 |
| Duplicate IDs | 0 |
| Malformed row widths | 0 |
| Missing source ID/version/locator | 0 |
| Empty fields | 1 (secondary_tags on ARCH-0002) |
| Origin EXTRACTED | 56 |
| Lifecycle EXTRACTED — REVIEW PENDING | 56 |
| Phase unallocated | 56 |
| Priority TBD | 56 |
| Owner NOT_ASSIGNED | 56 |
| Approval NOT_APPROVED | 56 |
| Verification criteria NOT_DEFINED/TBD | 26 |
| Verification method NOT_DEFINED/TBD | 1 |
| Provisional normative dispositions | 49 MANDATORY; 4 DESIGN; 2 CONDITIONAL_MANDATORY; 1 PENDING_SPECIFICATION |

### Validation conclusion

- **Structural integrity:** PASS for row count, column count, ID uniqueness and row widths.
- **Source field completeness:** PASS for presence of source ID, version and locator in every row.
- **Exact source locator fidelity:** NOT PASS — corrections and secondary-source links in §3–4 remain to be applied.
- **Compound-obligation granularity:** NOT PASS — decomposition in §6 remains pending controlled child-record allocation.
- **Phase allocation:** NOT COMPLETE — the 56 proposed primary phases in §8 have not been applied or reviewed.
- **Verification completeness:** NOT COMPLETE — 26 criteria remain NOT_DEFINED/TBD and one method remains NOT_DEFINED/TBD.
- **Controlled field completeness:** one empty secondary_tags field requires an explicit “not applicable” value or controlled empty-field convention.
- **Normative classification:** working disposition exists for all 56; it remains provisional and is not requirement approval.
- **Approval and ownership:** intentionally pending; no owner or approval is fabricated.

The matrix is therefore **structurally valid but not semantically validated or ready for WP-0.7 acceptance**.

## 11. Required next actions

1. Correct the source locators in the working review and add a many-to-many requirement-source-link register for multi-source requirements.
2. Complete the Atlas/Protocol and Atlas/Roadmap crosswalks for agent identity, OTS states, verifier categories and privacy.
3. Confirm the compound-obligation decomposition and allocate new child IDs without deleting or overwriting the 56 parent records.
4. Add the missing candidate requirements in §9 only after source authority and normative modality are checked.
5. Apply the proposed primary phase assignments from §8 and retain downstream implementation/test touchpoints in the rationale.
6. Define the 26 missing verification criteria and the one missing method without inventing numerical thresholds; Roadmap §9.3 quantitative targets must be a separate, explicit pre-test decision.
7. Re-run structural and semantic validation, update the canonical CSV and synchronized index/document register, and produce a final WP-0.7 readiness/closeout package.
8. Submit the completed WP-0.7 evidence package for LAEV's express acceptance. WP-0.8 remains NOT_STARTED until its dependency gate is released; Phase 1 remains NOT AUTHORIZED.

---

End of ERX-WP-0.7-EXACT-SOURCE-AND-MATRIX-AUDIT-001
