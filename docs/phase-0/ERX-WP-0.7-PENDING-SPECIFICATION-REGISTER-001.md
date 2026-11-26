# ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001
## Requirements Requiring Further Specification

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001 |
| Version | 0.3.0 |
| Status | WORKING GAP REGISTER — 82-CANDIDATE COVERAGE; 19 DISPOSITIONS OPEN |
| Work Package | WP-0.7 / Activity 0.7.7 |
| Date | 2026-11-25 |
| Source register | registers/requirements-traceability.csv |

## 1. Purpose

This register captures specification gaps that prevent a candidate requirement from being fully verifiable or safely allocated. It does not resolve the gaps or make design decisions. Requirement IDs remain unchanged.

## 2. Candidate gaps

### Inventory reconciliation — 2026-11-25
The table below contains **63 unique candidate IDs with recorded specification gaps**. The canonical source register now has 82 candidates; therefore **19 candidate IDs are not represented in this gap table**. Their absence is NOT a determination that no specification gap exists: they remain UNASSESSED for this register until reviewed. The 107 individual records also require parent/child gap applicability review. This register is a gap list, not a completeness assertion.

| Requirement ID | Source locator | Missing specification / closure work | Closure evidence |
|---|---|---|---|
| ERX-REQ-UTXO-0001 | ERX-PROT-001 PDF p.3 | Define canonical consumed/successor state evidence and historical status semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0002 | ERX-PROT-001 PDF p.3, Section 2.1 | Specify required field set, uniqueness scope, canonical encoding and versioning. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0003 | ERX-PROT-001 PDF p.3, Section 2.1 | Specify atomicity boundary, concurrency model and conflict outcome. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0004 | ERX-PROT-001 PDF p.3, Section 2.2 | Specify monotonic recovery and authoritative state reconciliation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0005 | ERX-PROT-001 PDF p.4 | Specify idempotency key scope, retention and retry result behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0006 | ERX-PROT-001 PDF p.10 | Specify cryptographic linkage and event/transition document boundaries. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0007 | ERX-PROT-001 PDF p.10, Step 7 | Specify transaction commit/rollback and external service boundary. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0008 | ERX-PROT-001 PDF p.10, Step 8 | Define OTS state vocabulary, retry policy and non-blocking operation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0009 | ERX-PROT-001 PDF p.17, Sections 10.1–10.5 | Specify replay detection, duplicate handling and adversarial test vectors. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0010 | ERX-PROT-001 PDF p.17, Section 10.6 | Specify concurrency and recovery invariants and authoritative persistence semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0011 | UTXO-911-001 PDF p.10, Principle of single spend | Specify uniqueness boundary and input-consumption validation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0012 | UTXO-911-001 PDF p.11, OTS function | Define OTS proof lifecycle and evidence retention. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0001 | ERX-PROT-001 PDF p.25, Section 17.1 | Specify service continuity and degraded-mode behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0002 | ERX-PROT-001 PDF p.24, Section 16.9 | Define audit record structure, time source and chronology semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 PDF p.23, Section 8.1 | Specify adapter inputs/outputs, trust boundary and failure behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0001 | ERX-PROT-001 PDF pp.5–6, Section 4 | Specify authority registry, issuer trust and credential lifecycle. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0002 | ERX-PROT-001 PDF p.6, Section 4.1 | Define credential states and fail-closed behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INST-0003 | ERX-PROT-001 PDF p.6, Section 4.1 | Define authoritative jurisdiction sources and update responsibility. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0001 | ERX-PROT-001 PDF p.6, Section 4.2 | Select key custody policy and approved controls; HSM remains recommendation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0002 | ERX-PROT-001 PDF p.7, Section 4.2 | Define historical key-status lookup and verifier trust data. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 PDF p.8, Section 4.3 | Specify core/adaptor authority boundary and non-overridable validation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PRIV-0001 | ERX-PROT-001 PDF pp.14–15, Step 18 | Define protected original-to-evidence linkage, access and retention. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 PDF pp.15–16, Step 19 | Specify transfer event identity, receiving authority and replay handling. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 PDF p.16, Step 20 | Define communication closure vs incident/intervention closure. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 PDF pp.21–23, Section 7 | Define export package contract and independent verification boundary. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 PDF p.24, Section 7.3 | Define verifier result vocabulary and missing-evidence behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 PDF pp.7–8, Lámina 03 | Specify independent center/agent credential and availability state semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 PDF p.8, Lámina 03 | Define non-response handling and prohibited false event creation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 PDF p.19, Lámina 06 | Define pending/submitted/anchored/failed evidence states and proof semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 PDF pp.27–28, verifier categories | Specify category checks, report schema and non-success outcomes. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OPS-0003 | UTXO-911-001 PDF p.7, Section 4.2 | Define separate session and incident lifecycles. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AVAIL-0001 | UTXO-911-001 PDF pp.9–10, availability lifecycle | Specify agent availability state machine, issuance guards and release authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-AVAIL-0002 | UTXO-911-001 PDF pp.9–11, Sections 5–8 | Specify separate agent-availability UTXO and communication UTXO models. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-STATE-0001 | ERX-ROADMAP-001 PDF pp.6–7, Sections 1.2–1.3 | Approve final state names and transitions; source says these require protocol approval. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-STATE-0002 | ERX-ROADMAP-001 PDF p.7, Section 1.3 | Specify transition table fields, authorization, guards and failure behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0001 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify terminal-state transition guards. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0002 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify correction/addendum model without mutation of sealed source evidence. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0003 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify minimum provenance/audit fields and reconstruction test. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INV-0004 | ERX-ROADMAP-001 PDF p.8, Section 1.5 | Specify rollback/recovery monotonicity and credential revocation persistence. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-DATA-0001 | ERX-ROADMAP-001 PDF p.9, Section 2.1 | Define formal schemas, versions, required fields and validation vectors. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CRYPTO-0001 | ERX-ROADMAP-001 PDF p.10, Section 2.3 | Algorithm and signature format remain an open decision; do not select by inference. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CRYPTO-0002 | ERX-ROADMAP-001 PDF p.10, Section 2.4 | Define acyclic canonicalization/hash/signature dependency graph. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0004 | ERX-ROADMAP-001 PDF p.21, Section 7 | Specify verifier independence, trust roots and shared dependency threat model. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TRANS-0002 | ERX-ROADMAP-001 PDF pp.23–24, Section 8.2 | Specify multi-center transfer protocol and reconciliation authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-ARCH-0002 | ERX-ROADMAP-001 PDF pp.11–12, §3.1 | Define component responsibilities, interfaces, trust boundaries and privilege separation. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-UTXO-0013 | ERX-ROADMAP-001 PDF pp.12–13, §3.3 | Define transaction boundary and failure atomicity; OTS remains outside call-critical transaction. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CORE-0001 | ERX-ROADMAP-001 PDF p.14, opening paragraph | Define measurable core readiness gate before telephone/OTS integration. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-CORE-0002 | ERX-ROADMAP-001 PDF p.14, §4.1 | Specify module boundaries, interfaces and ownership of listed responsibilities. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0002 | ERX-ROADMAP-001 PDF pp.14–15, §§4.3 | Define simulator fixtures, event sequence, assertions and reproducible output. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0003 | ERX-ROADMAP-001 PDF p.15, §4.4 | Define fault injection, concurrency test fixtures and expected recovery behavior. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-IDENT-0001 | ERX-ROADMAP-001 PDF p.16, §5.1 | Define identity record schemas, issuer relations and authorization model. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-IDENT-0002 | ERX-ROADMAP-001 PDF pp.16–17, §5.2 | Define credential state machine and validation source semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-KEY-0003 | ERX-ROADMAP-001 PDF p.17, §5.3 | Define full key lifecycle policy; do not imply a specific hardware technology. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-SEC-0001 | ERX-ROADMAP-001 PDF pp.17–18, §§5.4 and deliverables | Select algorithms, policy parameters and control evidence for each interface safeguard. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-OTS-0002 | ERX-ROADMAP-001 PDF pp.18–19, §6.1 | Define canonicalization, document versioning, proof update and verification semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PRIV-0002 | ERX-ROADMAP-001 PDF p.20, §6.4 | Define custody locations, access, retention, recovery and deletion rules. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-VERIFY-0005 | ERX-ROADMAP-001 PDF p.21, §7.1 | Define export verifier schema and deterministic outcome semantics. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-INT-0002 | ERX-ROADMAP-001 PDF p.22, opening of Phase 8 | Define integration gate evidence and authorization authority. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-TEST-0005 | ERX-ROADMAP-001 PDF p.25, §9.3 | Set numeric thresholds and measurement methods before executing tests; values not specified in extraction. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PILOT-0001 | ERX-ROADMAP-001 PDF pp.26–27, §§10.1–10.2 | Define shadow-pilot permissions, event feed and no-interference safeguards. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-PILOT-0002 | ERX-ROADMAP-001 PDF p.27, §10.3 | Define discrepancy classification, severity and reporting thresholds. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-HOMO-0001 | ERX-ROADMAP-001 PDF p.28, §11.1 | Define homologation dossier evidence and distinguish technical homologation from legal authorization. | Approved specification, decision record or testable criterion linked to this requirement |
| ERX-REQ-HOMO-0002 | ERX-ROADMAP-001 PDF pp.28–29, §11.2 | Define multi-center onboarding evidence and institution approval gate. | Approved specification, decision record or testable criterion linked to this requirement |

## 3. Cross-cutting gaps requiring coordinated treatment

1. State machines: final communication state names, transitions, guards, authority, failure and recovery rules.
2. Agent availability: independent lifecycle, release authority, busy/paused semantics and recovery.
3. Transactional atomicity: storage boundary, concurrency control, idempotency, conflict result and crash recovery.
4. Data model: event-document versus UTXO-transition fields, canonicalization and non-circular cryptographic linkage.
5. Cryptography: signature algorithm/format, trust chain, key rotation/revocation and historical validation.
6. Interinstitutional coordination: transfer authority, incompatible transitions, interruption and reconciliation.
7. Independent verifier: trust anchors, export contract, dependency isolation and result semantics.
8. OTS: proof states, retries, update/verification behavior and non-blocking call-critical operation.
9. Privacy/custody: original-file location, access, retention, deletion and recovery rules.
10. Testing/acceptance: test vectors, twenty referenced protocol tests, numeric performance targets and discrepancy thresholds.

## 4. Control

A gap is closed only when its missing parameter is specified by an authorized source or approved decision and the requirement's verification criterion can be evaluated. If closure depends on an open decision, link the decision candidate; do not invent a value. Numeric targets remain TBD until authorized.

---
End of ERX-WP-0.7-PENDING-SPECIFICATION-REGISTER-001


## 3. Coverage-control requirement

For each of the 19 currently unrepresented source candidates, record one of:
- GAP_IDENTIFIED (add a traceable row),
- NO_GAP_WITH_EVIDENCE (cite why current approved specification is sufficient),
- NOT_ASSESSED (retain open WP-0.7 status),
- BLOCKED_BY_DECISION (link an open decision candidate).

Do not close a gap solely because the candidate has a verification proposal or phase assignment. Child-level applicability must preserve the parent link and avoid duplicate gap records where a parent gap applies to multiple children.

---
End of reconciled gap register.



## 3. Coverage disposition queue — all remaining candidate IDs

The following 19 candidates were absent from the original 63-row gap table. They are now explicitly tracked so that no candidate is silently omitted. **This table does not claim that each is a confirmed specification gap.** Each remains GAP_REVIEW_REQUIRED until an evidence-based disposition is recorded as GAP_IDENTIFIED, NO_GAP_WITH_EVIDENCE, BLOCKED_BY_DECISION, or NOT_APPLICABLE with rationale. The candidate-specific verification proposals are available in ERX-WP-0.7-VERIFICATION-CRITERIA-PROPOSAL-001 v0.3.0; proposed criteria do not close specification gaps.

| Requirement ID | Source locator | Current design / verification evidence | Required 0.7.7 disposition |
|---|---|---|---|
| ERX-REQ-TEST-0001 | ERX-ROADMAP-001 PDF p.24, Section 9.1 | VERIFICATION_DESIGN_CONSTRAINT; criterion: Test plan contains each of the six categories with mapped cases, expected results and evidence. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-TEST-0004 | ERX-ROADMAP-001 PDF p.24, §9.1 | VERIFICATION_DESIGN_CONSTRAINT; criterion: Test matrix traces every category and each of the twenty source-listed tests to case IDs, expected outcomes and evidence. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-RECV-0001 | ERX-PROT-001 PDF p.8, Step 1 | DATA_DESIGN_CONSTRAINT; criterion: Schema validation confirms every JSON 01 reception record contains the event, call, telephone-session, receiving-gateway, reception-source, observation-time, available technical-reference and available-origin fields; unavailable source data is represented as unavailable rather than fabricated. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-LOC-0001 | ERX-PROT-001 PDF p.9, Step 4 | DATA_DESIGN_CONSTRAINT; criterion: For each location datum, validate source, observation time, estimated precision, method and validation state; coordinates are required only when available, and each permitted availability state is represented distinctly. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-LOC-0002 | ERX-PROT-001 PDF p.9, Step 4 | FUNCTIONAL_DESIGN_CONSTRAINT; criterion: A missing location does not prevent call progression; a later location update creates a new linked event and leaves the original signed/committed JSON 01 unchanged. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-CONTACT-0001 | ERX-PROT-001 PDF p.11, Step 10 | DATA_DESIGN_CONSTRAINT; criterion: The record model stores initial call-reception time and agent-response time as distinct event fields with their respective event meanings; no value is substituted for the other. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-AGENT-0003 | ERX-PROT-001 PDF p.12, Step 11 | SECURITY_DESIGN_CONSTRAINT; criterion: Professional identity validation emits an explicit permitted result; a pending or failed check never yields VERIFIED, and call attention continues independently of the validation result. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-CONTACT-0002 | ERX-PROT-001 PDF p.12, Step 13 | FUNCTIONAL_DESIGN_CONSTRAINT; criterion: The contact outcome model represents each source-listed outcome distinctly and rejects a record that claims human attention when no human response occurred. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-CORR-0001 | ERX-PROT-001 PDF pp.18, 21–22, §§10.9 and 14 | DATA_DESIGN_CONSTRAINT; criterion: After a source document is signed/committed, its bytes and digest remain unchanged; a correction is a separately signed complementary document that identifies the original, reason and authorizing party and allows reconstruction of the full history. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-TIME-0001 | ERX-PROT-001 PDF p.18, §11 | DATA_DESIGN_CONSTRAINT; criterion: The data model distinguishes device-declared, gateway-observed, institutionally received, processed, signed, OTS-submitted and verifiably anchored times; each field retains its own meaning and is not substituted for another. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-TIME-0002 | ERX-PROT-001 PDF p.19, §11 | DATA_DESIGN_CONSTRAINT; criterion: Every stored time carries UTC representation, precision and source; where supported, a monotonic session reference is retained; clock discrepancies are recorded as discrepancies and not silently rewritten. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-OTS-0003 | ERX-PROT-001 PDF pp.19–20, §12 | SECURITY_DESIGN_CONSTRAINT; criterion: For each JSON document, the evidence workflow records completion/freeze, canonicalization, signature, commitment calculation, OTS request, proof retention, later proof update and verification against the document and Bitcoin chain; OTS unavailability leaves attention flow available. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-OTS-0004 | ERX-PROT-001 PDF p.20, §12.3 | VERIFICATION_DESIGN_CONSTRAINT; criterion: Verifier output explicitly separates what OTS establishes (commitment existence by anchored time) from claims it cannot establish, including truth, identity, conduct, exact location, audio completeness, institutional authority or exact event second. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-PRIV-0003 | ERX-PROT-001 PDF p.20, §13 | DATA_DESIGN_CONSTRAINT; criterion: Data-flow and storage review confirms original call content remains in protected institutional infrastructure, sensitive direct identifiers are not sent to Bitcoin/OTS, and data is encrypted at rest and in transit with authorized/audited access. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-PRIV-0004 | ERX-PROT-001 PDF p.21, §13.1 | SECURITY_DESIGN_CONSTRAINT; criterion: Public outputs contain no direct identifiers, isolated personal-data hashes or unnecessary metadata; commitment construction uses high-entropy random values or approved equivalent and verification material remains under authorized control. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-PRIV-0005 | ERX-PROT-001 PDF p.21, §13.2 | GOVERNANCE_DESIGN_CONSTRAINT; criterion: The institutional policy identifies retention periods and deletion procedures under applicable law; deletion records do not claim removal of an already published Bitcoin anchor and retain minimum policy/evidence metadata. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-OPS-0004 | ERX-PROT-001 PDF p.24, §16.10 | SECURITY_DESIGN_CONSTRAINT; criterion: When identity services are unavailable, the call continues and the identity state remains PENDING or NOT_VERIFIED; no transition may promote it to VERIFIED without a successful authorized check. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-OPS-0005 | ERX-PROT-001 PDF p.24, §16.8 | OPERATIONAL_DESIGN_CONSTRAINT; criterion: During ERX unavailability, official telephony continues; where local durable storage is available, queued events survive process restart and preserve original-event, recovery and commitment-generation times as distinct fields. | GAP_REVIEW_REQUIRED — source/child/decision review pending |
| ERX-REQ-BOUND-0001 | ERX-PROT-001 PDF p.28, §20 | ARCHITECTURAL_DESIGN_CONSTRAINT; criterion: Architecture and institutional responsibility documents explicitly state that ERX does not replace the emergency number, telephone network, dispatch system, agent judgment or public authority, and preserve each installation's institutional/legal responsibility. | GAP_REVIEW_REQUIRED — source/child/decision review pending |

## 4. Coverage completion rule

The 63 detailed gap records plus this 19-candidate disposition queue provide visibility across all 82 source candidates, but **do not mean activity 0.7.7 is complete**. For every queue item, reviewer must record one allowed disposition, exact source/child applicability, reason, owner, affected decision and closure evidence. Parent-level gaps must not be duplicated for children; child-only gaps must retain the parent candidate link. A NO_GAP decision requires evidence and reviewer/date.
