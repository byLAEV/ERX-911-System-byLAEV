# ERX-WP-0.7-NORMATIVE-DISPOSITION-REVIEW-001
## Individual normative disposition of 56 requirement candidates

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-NORMATIVE-DISPOSITION-REVIEW-001 |
| Version | 0.1.0 |
| Status | TECHNICAL WORKING REVIEW — NOT APPROVED |
| Date | 2026-11-25 |
| Method | ERX-REQUIREMENTS-METHOD-001 v1.0.0, §§6, 8, 10–14 |
| Register baseline | requirements-traceability.csv, 56 candidate records |

## 1. Purpose and boundary

This review applies a provisional normative disposition to each of the 56 extracted candidates. It distinguishes an explicit obligation, an architectural/design constraint, a conditional obligation, and a source item that requires further specification before a final technical profile can be stated.

This is not an approval of the requirements baseline. It does not change the lifecycle status of any candidate, authorize implementation, select a technology, assign phases, resolve authority conflicts, or accept WP-0.7. All candidates remain `EXTRACTED — REVIEW PENDING`.

## 2. Disposition vocabulary

- `MANDATORY`: the cited source expressly states an obligation or prohibition within its stated scope. This means the source makes the statement mandatory; it does not mean LAEV has separately approved the candidate as a baseline requirement.
- `CONDITIONAL_MANDATORY`: the source states an obligation that applies only under an express condition (for example, where recording is institutionally authorized or where local queuing is technically possible).
- `DESIGN`: the source establishes an architectural or structural constraint, but it must not be confused with a fully specified implementation design or an adopted ADR.
- `PENDING_SPECIFICATION`: the source explicitly requires a specification to be developed, but does not itself select the algorithm, profile, values or detailed behavior.
- `OPEN_DECISION`: reserved for unresolved alternatives requiring an authorized decision. The current register records these separately as decision candidates; no candidate has been converted into an adopted decision by this review.

A source's planning instruction to define a future specification is recorded as an obligation to perform that specification work, not as evidence that the technical choice has already been made.

## 3. Individual dispositions

| Requirement ID | Source / locator | Proposed disposition | Evidence basis and limitation |
|---|---|---|---|
| ERX-REQ-UTXO-0001 | ERX-PROT-001 v1.1 PDF p.3 | MANDATORY | The source states that a valid transition consumes the prior state, creates the next, and preserves the consumed state in history. Define transition record and historical-retention fields; no contradiction with single consumption. |
| ERX-REQ-UTXO-0002 | ERX-PROT-001 v1.1 PDF p.3, Section 2.1 | MANDATORY | ERX-PROT-001 §2.1 says each institutional unit must have the listed identifiers, references, consumption state, process identity, times and institutional signature. Field schema, encoding, cardinality and validation rules remain unspecified. |
| ERX-REQ-UTXO-0003 | ERX-PROT-001 v1.1 PDF p.3, Section 2.1 | MANDATORY | ERX-PROT-001 §2.1 explicitly says the implementation must prevent two processes consuming the same valid state. Concurrency model and demonstrable acceptance test remain to be specified. |
| ERX-REQ-UTXO-0004 | ERX-PROT-001 v1.1 PDF p.3, Section 2.2 | MANDATORY | ERX-PROT-001 §2.2 expressly lists the uniqueness-support mechanisms within the authorized coordination scope. Mechanism composition, scope boundary and cross-installation coordination remain to be specified; source does not assert automatic global uniqueness across independent databases. |
| ERX-REQ-UTXO-0005 | ERX-PROT-001 v1.1 PDF p.4 | MANDATORY | ERX-PROT-001 p.4 says telephone retransmissions must not produce duplicate institutional effects. Define event identity, deduplication window/retention and idempotent response semantics. |
| ERX-REQ-UTXO-0006 | ERX-PROT-001 v1.1 PDF p.10 | MANDATORY | ERX-PROT-001 p.10 requires a documented canonicalization specification or formally specified compatible alternative, and an authorized institutional signing key. RFC 8785 is an example, not selected by the source; canonicalization profile and signature mechanism require an authorized decision. |
| ERX-REQ-UTXO-0007 | ERX-PROT-001 v1.1 PDF p.10, Step 7 | MANDATORY | ERX-PROT-001 p.10, Step 7 describes linking UTXO 01 to the original event and uniqueness rule and creating it atomically. Exact atomic boundary and storage transaction semantics remain to be specified. |
| ERX-REQ-UTXO-0008 | ERX-PROT-001 v1.1 PDF p.10, Step 8 | MANDATORY | ERX-PROT-001 p.10, Step 8 enumerates OTS evidence states and states that emergency attention continues independently of OTS confirmation. State transition rules, retry/update/finality semantics and evidence schema remain pending. |
| ERX-REQ-UTXO-0009 | ERX-PROT-001 v1.1 PDF p.17, Sections 10.1–10.5 | MANDATORY | ERX-PROT-001 §§10.1–10.5 sets out persistent call identity, no new admission on retransmission, atomic consumption/state creation and idempotent retry behavior. Define the precise event key, atomic transaction and replay response contract. |
| ERX-REQ-UTXO-0010 | ERX-PROT-001 v1.1 PDF p.17, Section 10.6 | MANDATORY | ERX-PROT-001 §10.6 says concurrent processes must not complete two valid transitions against one state and storage must implement verifiable concurrency constraints. Select and prove the storage/concurrency mechanism; source examples are not a technology selection. |
| ERX-REQ-UTXO-0011 | UTXO-911-001 v1.0 PDF p.10, Principle of single spend | MANDATORY | UTXO-911-001 p.10 states a valid UTXO can be consumed only once and lists validation and atomic update conditions. Detailed validation order, failure results and atomic persistence remain to be specified. |
| ERX-REQ-UTXO-0012 | UTXO-911-001 v1.0 PDF p.11, OTS function | MANDATORY | UTXO-911-001 p.11 states proof acquisition may complete later and must not delay or block emergency reception, acceptance or attention. Define asynchronous workflow and operational failure handling without blocking emergency care. |
| ERX-REQ-OPS-0001 | ERX-PROT-001 v1.1 PDF p.25, Section 17.1 | MANDATORY | ERX-PROT-001 §17.1 states ERX failure must not prevent reception and attention through official telephone infrastructure. Define outage scenarios, fallback ownership, measurable continuity targets and tests. |
| ERX-REQ-OPS-0002 | ERX-PROT-001 v1.1 PDF p.24, Section 16.9 | MANDATORY | ERX-PROT-001 §16.9 prohibits representing an event as permanently recorded before storage confirmation. Define confirmation level, durability guarantee and response semantics. |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 v1.0 PDF p.23, Section 8.1 | MANDATORY | ERX-ROADMAP-001 §8.1 says each adapter must specify inputs, outputs, authentication, errors, retries and duplicate handling. Individual adapter contracts are not yet supplied; phase implementation remains to be allocated. |
| ERX-REQ-INST-0001 | ERX-PROT-001 v1.1 PDF pp.5–6, Section 4 | MANDATORY | ERX-PROT-001 §4 says each installation must have validated institutional configuration and enumerates its contents. Define configuration schema, validating authority and jurisdiction-specific values. |
| ERX-REQ-INST-0002 | ERX-PROT-001 v1.1 PDF p.6, Section 4.1 | MANDATORY | ERX-PROT-001 §4.1 says the system must distinguish the seven listed institution/identity/trust states. Define state model, transition rules, trust source and behavior during pending validation. |
| ERX-REQ-INST-0003 | ERX-PROT-001 v1.1 PDF p.6, Section 4.1 | MANDATORY | ERX-PROT-001 §4.1 says territorial boundaries must derive from official routing/jurisdiction data and must not be inferred solely from antenna location. Identify official authoritative data sources and update/exception rules per jurisdiction. |
| ERX-REQ-KEY-0001 | ERX-PROT-001 v1.1 PDF p.6, Section 4.2 | MANDATORY | ERX-PROT-001 §4.2 states institutional private keys must remain under institutional control. Custody, access control, backup and hardware protection mechanism remain open; hardware protection is recommended when available, not an unconditional requirement. |
| ERX-REQ-KEY-0002 | ERX-PROT-001 v1.1 PDF p.7, Section 4.2 | MANDATORY | ERX-PROT-001 §4.2 requires the verifier to determine which key was authorized at issuance, including validity periods and revocations. Historical trust registry, revocation semantics and evidence format remain to be specified. |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 v1.1 PDF p.8, Section 4.3 | DESIGN | ERX-PROT-001 §4.3 defines a common ERX core and institution-specific adapters; adapters must not alter fundamental single-consumption and continuity rules. Architecture boundary and adapter contract need formalization; the source establishes the design constraint. |
| ERX-REQ-PRIV-0001 | ERX-PROT-001 v1.1 PDF pp.14–15, Step 18 | CONDITIONAL_MANDATORY | ERX-PROT-001 Step 18 conditions the requirement on recording being institutionally authorized, then requires protected institutional storage and specified metadata. Recording authorization, applicable jurisdiction, retention schedule, access and deletion rules are institution-specific and must be identified. |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 v1.1 PDF pp.15–16, Step 19 | MANDATORY | ERX-PROT-001 Step 19 requires recording transfer source/destination, agents, time, reason and continuity/interruption without duplicate admission. Transfer authority, receiving acknowledgment, responsibility and distributed coordination remain unresolved. |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 v1.1 PDF p.16, Step 20 | MANDATORY | ERX-PROT-001 Step 20 requires distinct termination reasons and prohibits classifying a disconnect as normal farewell. Finalize controlled reason vocabulary and mapping from telephony events. |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 v1.1 PDF pp.21–23, Section 7 | MANDATORY | ERX-PROT-001 §7 defines independent verification and the required evidence package without direct production-database access. Export format, verifier trust model and independence assurance criteria remain to be specified. |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 v1.1 PDF p.24, Section 7.3 | MANDATORY | ERX-PROT-001 §7.3 requires distinct verification outcomes and prohibits reporting unverified data as satisfactory. Define result schema, severity semantics and propagation of incomplete/indeterminate evidence. |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 v1.1 PDF pp.7–8, Lámina 03 | MANDATORY | ERX-ATLAS-001 Lámina 03 separates center authentication from professional-agent authentication and records an unverified agent without stopping service. Confirm source page's normative wording and define exception/escalation process; Atlas is a diagrammatic source. |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 v1.1 PDF p.8, Lámina 03 | MANDATORY | ERX-ATLAS-001 Lámina 03 defines non-response handling and prohibits fabricating a professional identity or conversation. Define evidence fields for attempted contact and non-response. |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 v1.1 PDF p.19, Lámina 06 | MANDATORY | ERX-ATLAS-001 Lámina 06 enumerates OTS states and disallows representing pending evidence as anchored. Define lifecycle transitions, retry/update policy and proof verification conditions. |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 v1.1 PDF pp.27–28, verifier categories | MANDATORY | ERX-ATLAS-001 verifier categories enumerate separate integrity, authenticity, identity, UTXO, double-consumption, temporal, file and chronology checks. Define report schema, each check's evidence inputs and fail/indeterminate semantics. |
| ERX-REQ-OPS-0003 | UTXO-911-001 v1.0 PDF p.7, Section 4.2 | MANDATORY | UTXO-911-001 §4.2 distinguishes telephone communication closure from incident or subsequent institutional action closure. Define linked but independent incident/action lifecycle and responsible system. |
| ERX-REQ-AVAIL-0001 | UTXO-911-001 v1.0 PDF pp.9–10, availability lifecycle | MANDATORY | UTXO-911-001 availability lifecycle states that availability must reflect actual operational state and unavailable states cannot be advertised as available. Define authoritative availability source, update atomicity and controlled state vocabulary. |
| ERX-REQ-AVAIL-0002 | UTXO-911-001 v1.0 PDF pp.9–11, Sections 5–8 | DESIGN | UTXO-911-001 §§5–8 separate agent identity/availability from each call's request, acceptance, session, closure and evidence cycles. Define stable references and lifecycle interfaces; preserve the separate cycles. |
| ERX-REQ-STATE-0001 | ERX-ROADMAP-001 v1.0 PDF pp.6–7, Sections 1.2–1.3 | MANDATORY | ERX-ROADMAP-001 §§1.2–1.3 requires two independent state machines while expressly reserving definitive names and transitions for protocol approval. State names/transitions are pending specification and approval; only separation is fixed by this source. |
| ERX-REQ-STATE-0002 | ERX-ROADMAP-001 v1.0 PDF p.7, Section 1.3 | MANDATORY | ERX-ROADMAP-001 §1.3 enumerates input, authority, condition, action, output, evidence and failure for every transition specification. Actual transition catalogue and exception behavior remain to be authored. |
| ERX-REQ-INV-0001 | ERX-ROADMAP-001 v1.0 PDF p.8, Section 1.5 | MANDATORY | ERX-ROADMAP-001 §1.5 lists as a minimum invariant that a closed session does not become active again. Define correction/continuity handling without reopening a consumed session. |
| ERX-REQ-INV-0002 | ERX-ROADMAP-001 v1.0 PDF p.8, Section 1.5 | MANDATORY | ERX-ROADMAP-001 §1.5 states complementary correction must not retroactively modify a sealed document. Define correction artifact and linkage rules. |
| ERX-REQ-INV-0003 | ERX-ROADMAP-001 v1.0 PDF p.8, Section 1.5 | MANDATORY | ERX-ROADMAP-001 §1.5 lists provenance preservation for every state transition as a minimum invariant. Define minimum provenance fields and validation. |
| ERX-REQ-INV-0004 | ERX-ROADMAP-001 v1.0 PDF p.8, Section 1.5 | MANDATORY | ERX-ROADMAP-001 §1.5 requires recovery not to resurrect consumed states or revoked credentials. Define backup rollback prevention, revocation history and reconciliation tests. |
| ERX-REQ-DATA-0001 | ERX-ROADMAP-001 v1.0 PDF p.9, Section 2.1 | MANDATORY | ERX-ROADMAP-001 §2.1 says each defined JSON structure must have a formal schema, version and validation rules. Schemas and versioning policy are not yet produced. |
| ERX-REQ-CRYPTO-0001 | ERX-ROADMAP-001 v1.0 PDF p.10, Section 2.3 | PENDING_SPECIFICATION | ERX-ROADMAP-001 §2.3 explicitly lists signature algorithm, format, signer identity, certificate, trust-chain reference, signing time, historical validation, revocation and rotation as topics to define. The source mandates specification work but does not select values; final profile requires a decision. |
| ERX-REQ-CRYPTO-0002 | ERX-ROADMAP-001 v1.0 PDF p.10, Section 2.4 | MANDATORY | ERX-ROADMAP-001 §2.4 requires a defined non-circular relationship among documents 01/02/03 and UTXO records. Separating event document and UTXO transition record is a recommendation, not an adopted requirement; record it as an alternative for decision. |
| ERX-REQ-VERIFY-0004 | ERX-ROADMAP-001 v1.0 PDF p.21, Section 7 | MANDATORY | ERX-ROADMAP-001 §7 requires sufficient verifier independence so producer-side failure/manipulation does not automatically compromise audit. Define independence boundary, trust dependencies, reproducible verifier and test criteria. |
| ERX-REQ-TRANS-0002 | ERX-ROADMAP-001 v1.0 PDF pp.23–24, Section 8.2 | MANDATORY | ERX-ROADMAP-001 §8.2 says a specific interinstitutional transfer protocol must be developed and enumerates its required elements. Choice between distributed transaction coordination and delegated transition authority remains open; simple database synchronization is explicitly insufficient as an assumption. |
| ERX-REQ-TEST-0001 | ERX-ROADMAP-001 v1.0 PDF p.24, Section 9.1 | MANDATORY | ERX-ROADMAP-001 §9.1 requires the test matrix to include six categories of tests. Detailed test cases, oracles, coverage and thresholds remain to be specified. |
| ERX-REQ-OPS-0004 | ERX-PROT-001 v1.1 PDF p.25, §16.8 | CONDITIONAL_MANDATORY | ERX-PROT-001 §16.8 requires a durable protected local queue when ERX is unavailable, where technically possible, and separate event/recovery/commitment times. Define what qualifies as technically possible, queue durability, protection and time-source semantics. |
| ERX-REQ-OPS-0005 | ERX-PROT-001 v1.1 PDF p.26, §17.2 | MANDATORY | ERX-PROT-001 §17.2 lists integrity, duplication, identity, order, idempotent processing, state reconstruction, evidence generation and incident retention on recovery. Specify exact reconciliation algorithm, conflict handling and recovery acceptance tests. |
| ERX-REQ-OPS-0006 | ERX-PROT-001 v1.1 PDF p.25, §16.9 | MANDATORY | ERX-PROT-001 §16.9 requires persistence, backup and recovery mechanisms and prohibits permanent-record claims before storage confirmation. Define durability classes, confirmation protocol, backup objectives and recovery objectives. |
| ERX-REQ-SEC-0001 | ERX-PROT-001 v1.1 PDF p.26, §17.3 | MANDATORY | ERX-PROT-001 §17.3 specifies mutual authentication or appropriate equivalent, transport protection, role authorization and message validation; unauthorized components cannot issue transitions. Select mechanisms and define trust/authorization policies and message schemas. |
| ERX-REQ-ARCH-0002 | ERX-PROT-001 v1.1 PDF p.26, §19 | DESIGN | ERX-PROT-001 §19 defines four components with distinct responsibilities: Protocol, Core, Institutional Module and Verifier. Formalize component boundaries, APIs and deployment separation; do not infer internal implementation. |
| ERX-REQ-TEST-0002 | ERX-PROT-001 v1.1 PDF p.26, §19.1 | MANDATORY | ERX-PROT-001 §19.1 enumerates twenty mandatory pre-implementation test subjects. Create test cases, oracles, coverage thresholds, test data and evidence format. |
| ERX-REQ-PRIV-0002 | ERX-ATLAS-001 v1.1 PDF pp.25–26, Lámina 08 | MANDATORY | ERX-ATLAS-001 Lámina 08 separates sensitive institutional call information from public cryptographic commitments and states call content is not published to Bitcoin. Define exact public commitment/metadata schema, access rules and privacy threat model. |
| ERX-REQ-VERIFY-0005 | ERX-ATLAS-001 v1.1 PDF p.28, Categorías de verificación | MANDATORY | ERX-ATLAS-001 verifier categories expressly distinguish cryptographic integrity/temporal evidence from material truth of content. Define report language and verifier limitation disclosure. |
| ERX-REQ-AVAIL-0003 | ERX-ROADMAP-001 v1.0 PDF pp.4–5, §3.1 | DESIGN | ERX-ROADMAP-001 §3.1 explicitly separates communication and agent-availability cycles and prohibits substituting UTXO 03 for agent-availability UTXO. State vocabulary and transition approval remain pending; preserve cycle separation. |
| ERX-REQ-INV-0005 | UTXO-911-001 v1.0 PDF pp.9–10, §§5–6 | MANDATORY | UTXO-911-001 §§5–6 requires continuity through new states linked to prior events and no reuse of consumed states. Define backup rollback safeguards and test that consumed states remain non-spendable after restoration. |
| ERX-REQ-OTS-0002 | UTXO-911-001 v1.0 PDF p.11, §7 | MANDATORY | UTXO-911-001 §7 requires retention of OTS commitments/proofs and allows proof completion later without blocking emergency care. Specify proof format, retention, retry/update policy and verification evidence. |

## 4. Cross-cutting review findings

1. **UTXO single consumption is a source requirement, not a claim of automatic global uniqueness.** ERX-PROT-001 §2.2 scopes uniqueness to the authorized transaction-coordination domain and expressly does not assume that independent databases share a global state.
2. **Atomicity and idempotency are mandatory properties; their concrete implementation remains open.** Locks, version checks, compare-and-swap, distributed transactions or delegated authority must not be silently selected by this review.
3. **The two state cycles remain independent.** Communication and agent availability must not be collapsed into one UTXO lifecycle. Definitive state names and transition authority remain subject to protocol approval.
4. **OTS is evidence, not a prerequisite to emergency care.** Pending, updatable, anchored, verified and failed states must not be conflated. Proof acquisition must not block reception or attention.
5. **Cryptographic verification does not establish material truth.** The verifier must report integrity/authenticity/temporal evidence separately from factual truth of the call content.
6. **The Atlas is graphical support.** Where the candidate derives from a diagrammatic label or explanatory visual, the source locator and the corresponding normative prose in ERX-PROT-001 should be checked before final approval.
7. **Roadmap requirements to define algorithms, schemas or transfer protocols are obligations to complete design work.** They do not pre-approve RFC 8785, a signature algorithm, a specific database, a consensus protocol or a distributed transaction model.
8. **Conditional institutional obligations require jurisdiction-specific inputs.** Recording authorization, retention, privacy, routing and institutional trust cannot be generalized without the applicable authority and jurisdiction.

## 5. Required follow-up

- Complete a row-by-row exact-locator and normative-wording audit, particularly for diagram-derived Atlas candidates.
- Split any compound candidate only where distinct verification outcomes are genuinely required; preserve source traceability and IDs.
- Convert unresolved technical alternatives into decision candidates for WP-0.8, without adopting them prematurely.
- Complete phase allocation under WP-0.7.10 only after reconciling the approved Roadmap and WP-0.3 boundaries.
- Define verification criteria and methods without inventing quantitative thresholds absent from approved sources.
- Obtain LAEV's express review and acceptance of the completed WP-0.7 package.

## 6. Status

The register now records a proposed normative disposition and basis for 56/56 candidates. This closes a working pass for the modality-disposition task but does not, by itself, close activities 0.7.2–0.7.11. WP-0.7 remains IN_PROGRESS. WP-0.8 remains APPROVED / NOT_STARTED pending formal release of its WP-0.7 dependency.

---
End of ERX-WP-0.7-NORMATIVE-DISPOSITION-REVIEW-001
