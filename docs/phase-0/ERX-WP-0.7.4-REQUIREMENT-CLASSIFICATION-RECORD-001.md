# ERX-WP-0.7.4-REQUIREMENT-CLASSIFICATION-RECORD-001
## Requirement classification execution record

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.4-REQUIREMENT-CLASSIFICATION-RECORD-001 |
| Version | 1.0.0 |
| Date | 2026-11-28 |
| Status | COMPLETED — CLASSIFICATION REVIEW RECORDED; SOURCE FIDELITY PENDING |
| Authority | LAEV — scope approval; classification remains provisional pending subsequent acceptance gates |
| Repository | byLAEV/ERX-911-System-byLAEV |
| Branch | main |

## 1. Purpose and method

Activity 0.7.4 applies the taxonomy in `ERX-REQUIREMENTS-METHOD-001` §5 to every parent candidate and every individually identified requirement. Each record receives exactly one primary type and zero or more secondary tags. The primary type is selected by the dominant acceptance concern of the statement; secondary tags retain additional concerns without replacing the primary type.

The taxonomy applied is: `FUNCTIONAL` (defines required behaviour, operation or system response); `SECURITY` (defines protection, authentication, authorization, integrity or resilience); `PRIVACY` (defines personal-data handling, disclosure, minimization, retention or access); `DATA_AND_RECORDS` (defines data structures, records, evidence, retention or auditability); `INTEROPERABILITY` (defines interaction among institutions, networks, systems or interfaces); `PERFORMANCE_AND_CAPACITY` (defines measurable timing, throughput, capacity, availability or resource limits); `OPERATIONAL` (defines procedures, roles, exception handling, continuity or support); `GOVERNANCE` (defines authority, approvals, accountability, policy or institutional controls); `COMPLIANCE` (defines an obligation traceable to an identified legal, regulatory, contractual or institutional source); `ARCHITECTURAL` (defines structural design constraints or separation of responsibilities); `INTERFACE` (defines inputs, outputs, messages, APIs or human-machine interactions); `VERIFICATION` (defines evidence, acceptance, validation or test obligations).

This activity classifies the statements currently recorded in the two canonical registers. It does not upgrade origin class, approve a requirement, determine mandatory modality, adopt a design, or verify exact source wording. Those are separate WP-0.7 activities, particularly 0.7.5, 0.7.6 and 0.7.9.

## 2. Coverage and integrity

| Population | Records | Unique IDs | Primary type present | Taxonomy-valid |
|---|---:|---:|---:|---:|
| Source candidates | 82 | 82 | 82 | PASS |
| Individual requirements | 107 | 107 | 107 | PASS |
| **Total reviewed** | **189** | **121** | **189** | **PASS** |

- All primary types and secondary tags are members of the approved method taxonomy.
- Every individual record retains a valid parent candidate link; missing parent references: 0.
- No candidate or individual ID was created, deleted or renumbered by classification.
- No source statement was rewritten as part of this activity.
- Four classifications were corrected from FUNCTIONAL / GOVERNANCE / SECURITY to VERIFICATION where the statement's controlling purpose is test evidence or a pre-integration demonstration: `ERX-REQ-TEST-0002`, `ERX-REQ-TEST-0003`, `ERX-REQ-TEST-0004`, `ERX-REQ-CORE-0001`.

## 3. Primary-type distribution

| Primary type | Source candidates (82) | Individual records (107) |
| FUNCTIONAL | 17 | 18 |
| SECURITY | 14 | 17 |
| PRIVACY | 3 | 7 |
| DATA_AND_RECORDS | 14 | 21 |
| INTEROPERABILITY | 2 | 2 |
| PERFORMANCE_AND_CAPACITY | 1 | 1 |
| OPERATIONAL | 4 | 7 |
| GOVERNANCE | 10 | 13 |
| COMPLIANCE | 0 | 0 |
| ARCHITECTURAL | 9 | 11 |
| INTERFACE | 1 | 1 |
| VERIFICATION | 7 | 9 |

## 4. Individual classification register

| Individual ID | Primary type | Secondary tags | Statement classified |
|---|---|---|---|
| `ERX-REQ-UTXO-0001` | FUNCTIONAL | DATA_AND_RECORDS | A valid transition consumes a prior state and creates the next; consumed state is unavailable for another transition but remains in institutional history. |
| `ERX-REQ-UTXO-0002` | SECURITY | DATA_AND_RECORDS | Each institutional UTXO must carry unique state, call and stage IDs; document cryptographic reference; prior-state reference when applicable; consumption state; process identity; observation/processing times; and institutional operation signature. |
| `ERX-REQ-UTXO-0003` | FUNCTIONAL | SECURITY | The implementation must prevent two processes from consuming the same valid state. |
| `ERX-REQ-UTXO-0004` | ARCHITECTURAL | SECURITY | Within authorized coordination scope, uniqueness is supported by persistent event IDs, storage uniqueness constraints, atomic operations, concurrency control, idempotency, transition history and safe recovery. |
| `ERX-REQ-UTXO-0005` | FUNCTIONAL | SECURITY | A retransmitted telephone event must not produce duplicate institutional effects. |
| `ERX-REQ-UTXO-0006-A` | SECURITY | DATA_AND_RECORDS | Canonicalized institutional documents conform to a documented canonicalization specification, such as RFC 8785 or a formally specified compatible alternative. |
| `ERX-REQ-UTXO-0006-B` | SECURITY | GOVERNANCE | Institutional documents are signed with an authorized institutional key. |
| `ERX-REQ-UTXO-0007` | FUNCTIONAL | — | UTXO 01 must be linked to the original event and a uniqueness rule, and its creation must be atomic. |
| `ERX-REQ-UTXO-0008-A` | DATA_AND_RECORDS | VERIFICATION | The OTS evidence lifecycle distinguishes not requested, sent, pending, updatable, anchored, verified and failed states. |
| `ERX-REQ-UTXO-0008-B` | OPERATIONAL | FUNCTIONAL | Emergency attention proceeds independently of OTS confirmation. |
| `ERX-REQ-UTXO-0009-A` | DATA_AND_RECORDS | FUNCTIONAL | Each call event receives a persistent identity. |
| `ERX-REQ-UTXO-0009-B` | SECURITY | FUNCTIONAL | Retransmission of a call event does not create a new admission. |
| `ERX-REQ-UTXO-0009-C` | FUNCTIONAL | SECURITY | Consumption of a state and creation of its successor are atomic. |
| `ERX-REQ-UTXO-0009-D` | FUNCTIONAL | DATA_AND_RECORDS | A retry returns the original result when applicable. |
| `ERX-REQ-UTXO-0010` | FUNCTIONAL | SECURITY | Concurrent processes must not complete two valid transitions against the same state; storage must implement verifiable concurrency constraints. |
| `ERX-REQ-UTXO-0011` | FUNCTIONAL | SECURITY | A valid UTXO can be consumed only once; validation checks input existence, current validity, executor authorization and absence of prior consumption; state update is atomic. |
| `ERX-REQ-UTXO-0012` | OPERATIONAL | INTERFACE | OTS proof acquisition may complete later and must not delay or block emergency reception, acceptance or attention. |
| `ERX-REQ-OPS-0001` | OPERATIONAL | — | ERX failure must not prevent the institution from receiving and attending calls through its official telephone infrastructure. |
| `ERX-REQ-OPS-0002` | DATA_AND_RECORDS | OPERATIONAL | An event must not be represented as permanently recorded unless storage has confirmed it. |
| `ERX-REQ-INT-0001` | INTEROPERABILITY | INTERFACE | Each institutional adapter specifies inputs, outputs, authentication, errors, retries and duplicate handling. |
| `ERX-REQ-INST-0001` | GOVERNANCE | SECURITY, OPERATIONAL | Each installation must have a validated institutional configuration covering institution and authorized-center identity, jurisdiction, certificates, verification keys, authorized agents, location sources, integrations, storage/retention/privacy policy, OTS, recovery and continuity. |
| `ERX-REQ-INST-0002` | GOVERNANCE | SECURITY | The system must distinguish recognized/authorized institution, recognized but outside jurisdiction, cryptographically valid but institutionally unverified identity, expired or revoked certificate, unknown identity and trust-validation-pending states. |
| `ERX-REQ-INST-0003` | GOVERNANCE | FUNCTIONAL | Territorial coverage and routing boundaries must derive from official jurisdiction/routing rules and authorized data, not solely antenna location. |
| `ERX-REQ-KEY-0001` | GOVERNANCE | SECURITY | Institutional private keys must remain under the institution's control. |
| `ERX-REQ-KEY-0002` | SECURITY | DATA_AND_RECORDS | Historical signature verification must determine which key was authorized at issuance time, including its validity period and recorded revocation state. |
| `ERX-REQ-ARCH-0001-A` | ARCHITECTURAL | FUNCTIONAL | Institutional differences are handled through adapters while the ERX Core remains common. |
| `ERX-REQ-ARCH-0001-B` | ARCHITECTURAL | INTERFACE | Institutional adapters do not modify fundamental single-consumption rules. |
| `ERX-REQ-ARCH-0001-C` | ARCHITECTURAL | SECURITY | Institutional adapters do not modify transaction-continuity rules. |
| `ERX-REQ-PRIV-0001` | SECURITY | PRIVACY, DATA_AND_RECORDS | Where recording is institutionally authorized, the original audio must remain in protected institutional storage and its reference, hash, format, duration, times, origin and retention state must be recorded. |
| `ERX-REQ-TRANS-0001-A` | DATA_AND_RECORDS | INTEROPERABILITY | A transfer record identifies the source and destination centers, delivering and receiving agents, time, reason, and continuity/interruption. |
| `ERX-REQ-TRANS-0001-B` | FUNCTIONAL | INTEROPERABILITY | Transfer of the same communication does not create duplicate admission. |
| `ERX-REQ-CLOSE-0001` | FUNCTIONAL | DATA_AND_RECORDS | Termination reason must distinguish normal farewell, citizen/agent termination, accidental disconnect, signal loss, technical interruption and transfer-related end; a disconnect must not be classified as normal farewell. |
| `ERX-REQ-VERIFY-0001` | SECURITY | VERIFICATION, DATA_AND_RECORDS | An exported case must be independently verifiable without direct production-database access and include the documents, transitions, trust references, signatures, OTS proofs, file manifests and historical identity references required for verification. |
| `ERX-REQ-VERIFY-0002` | INTERFACE | VERIFICATION | Verification output must distinguish success, failure, incomplete evidence, pending evidence and indeterminate results; unverified data must not be reported as satisfactory. |
| `ERX-REQ-AGENT-0001-A` | GOVERNANCE | SECURITY | Center institutional authentication is validated separately from professional-agent authentication. |
| `ERX-REQ-AGENT-0001-B` | SECURITY | GOVERNANCE | Professional-agent authentication is recorded as a separate validation from center institutional authentication. |
| `ERX-REQ-AGENT-0001-C` | OPERATIONAL | SECURITY | An unverified agent is recorded as unverified and does not stop emergency attention. |
| `ERX-REQ-AGENT-0002` | FUNCTIONAL | DATA_AND_RECORDS, OPERATIONAL | If no human agent responds, record the attempted contact/non-response and do not fabricate a professional identity or conversation. |
| `ERX-REQ-OTS-0001` | DATA_AND_RECORDS | VERIFICATION | OTS lifecycle must distinguish not sent, sent, pending, updatable, anchored, verifiable and generation/update error; pending evidence must not be represented as anchored. |
| `ERX-REQ-VERIFY-0003` | SECURITY | VERIFICATION | Verifier output must separately report document integrity, institutional authenticity, professional identity, UTXO continuity, double-consumption check, temporal evidence, file integrity and chronology. |
| `ERX-REQ-OPS-0003` | FUNCTIONAL | OPERATIONAL | Telephone communication closure must not automatically mean that the related emergency incident or subsequent institutional actions are complete. |
| `ERX-REQ-AVAIL-0001` | FUNCTIONAL | OPERATIONAL | Agent availability must reflect actual operational state; no available-state output may be issued while the agent is busy, paused or otherwise unable to receive calls. |
| `ERX-REQ-AVAIL-0002` | ARCHITECTURAL | DATA_AND_RECORDS | Agent identity and availability remain distinct from each call's request, acceptance, session, closure and evidence; each new call creates its own linked state/evidence cycle without reusing consumed states. |
| `ERX-REQ-STATE-0001` | ARCHITECTURAL | FUNCTIONAL | The communication lifecycle and the agent-availability lifecycle must be documented as two independent state machines; definitive state names and transitions remain subject to protocol approval. |
| `ERX-REQ-STATE-0002` | FUNCTIONAL | DATA_AND_RECORDS, SECURITY | Each valid transition specification must identify its input state, authorized authority, preconditions, action/event, output UTXO, generated evidence and failure handling. |
| `ERX-REQ-INV-0001` | FUNCTIONAL | — | A closed communication session must not become active again. |
| `ERX-REQ-INV-0002` | DATA_AND_RECORDS | — | A complementary correction must not retroactively modify a sealed document. |
| `ERX-REQ-INV-0003` | DATA_AND_RECORDS | — | Every state transition must preserve its provenance. |
| `ERX-REQ-INV-0004` | FUNCTIONAL | SECURITY | Recovery must not resurrect states already consumed or credentials already revoked. |
| `ERX-REQ-DATA-0001` | DATA_AND_RECORDS | INTEROPERABILITY | Each defined JSON data structure must have a formal schema, a version and validation rules. |
| `ERX-REQ-CRYPTO-0001` | SECURITY | — | The digital-signature specification must define the signature algorithm and format, signer identity, associated certificate, trust-chain reference, signing time, historical validation, revocation handling and key rotation. |
| `ERX-REQ-CRYPTO-0002-A` | ARCHITECTURAL | SECURITY | The cryptographic relationship among documents 01, 02 and 03 and their UTXO records is defined without circular dependencies. |
| `ERX-REQ-CRYPTO-0002-B` | GOVERNANCE | ARCHITECTURAL | The event document and UTXO transition record are considered separately, as recommended by the Roadmap. |
| `ERX-REQ-VERIFY-0004` | ARCHITECTURAL | VERIFICATION, SECURITY | The independent verifier must have sufficient independence from ERX Core that a producer-side failure or manipulation does not automatically compromise the audit result. |
| `ERX-REQ-TRANS-0002` | GOVERNANCE | FUNCTIONAL, INTEROPERABILITY | An interinstitutional transfer protocol must define the source center, receiving center, transfer authority, call identity, transfer state, receipt confirmation, transition responsibility, interruption handling and subsequent reconciliation. |
| `ERX-REQ-TEST-0001` | VERIFICATION | — | The test matrix must cover functional, transactional, cryptographic, adversarial, operational and interoperability categories. |
| `ERX-REQ-ARCH-0002` | ARCHITECTURAL | SECURITY | The system architecture must keep ERX Core, ERX Institutional Module and ERX Verifier functionally separated; the verifier must not be a privileged extension of the producer. |
| `ERX-REQ-UTXO-0013` | FUNCTIONAL | OPERATIONAL | Consumption of an input UTXO and creation of its successor must be designed as one transactional operation; external OTS processing must not be part of the transaction that conditions emergency attention. |
| `ERX-REQ-CORE-0001` | VERIFICATION | ARCHITECTURAL | The ERX Core must be demonstrated in a controlled environment before telephone or OTS integration begins. |
| `ERX-REQ-CORE-0002` | ARCHITECTURAL | FUNCTIONAL | The core development scope must include event intake, identity, admission, UTXO, state, idempotency, concurrency, document, signature, audit and recovery responsibilities. |
| `ERX-REQ-TEST-0002` | VERIFICATION | — | A controlled simulator must reproduce a complete call lifecycle, including admission, UTXO 01 creation, acceptance, UTXO 01 consumption, UTXO 02 creation, development, UTXO 02 consumption, UTXO 03 creation and case closure. |
| `ERX-REQ-TEST-0003` | VERIFICATION | OPERATIONAL | The core test suite must cover competing consumption, identical requests, retries after timeout, retransmission, replay of old operations, interruption during transition, backup restoration, inconsistent input/output persistence and incompatible concurrent center transitions. |
| `ERX-REQ-IDENT-0001` | GOVERNANCE | SECURITY | The system must maintain separate identity records for institution, PSAP center, gateway, professional agent, authorized device/component, trust authority and certificate issuer. |
| `ERX-REQ-IDENT-0002` | SECURITY | — | A credential with pending verification must not be treated as valid authentication; the system must distinguish valid, expired, revoked, territorially unauthorized, functionally unauthorized, unknown and pending states. |
| `ERX-REQ-KEY-0003` | GOVERNANCE | SECURITY | Key management must cover secure generation, public-key registration, private-key custody, institutional signing, rotation, revocation, historical verification and usage auditing. |
| `ERX-REQ-SEC-0001` | SECURITY | INTERFACE, OPERATIONAL | Security interfaces must provide mutual authentication, role-based authorization, encryption in transit and at rest, replay protection, session control, secret management, security logs and privilege separation. |
| `ERX-REQ-OTS-0002` | SECURITY | DATA_AND_RECORDS, VERIFICATION | The evidence process must receive the final document, validate its schema, canonicalize it, hash it, link it to its UTXO transition, obtain the institutional signature, create the timestamp commitment, retain the proof and support later update and verification. |
| `ERX-REQ-PRIV-0002` | SECURITY | PRIVACY, DATA_AND_RECORDS | Original audio and files must not be sent to Bitcoin; they must remain under institutional custody with identifiers, hashes, manifests, protected logical location, retention policy, access evidence and recovery tests. |
| `ERX-REQ-VERIFY-0005` | SECURITY | VERIFICATION, DATA_AND_RECORDS | An exported case verifier must report schema, document hash, signature, institutional identity, historical credential validity, UTXO continuity, single consumption, OTS state, file integrity and chronology outcomes. |
| `ERX-REQ-INT-0002` | GOVERNANCE | INTEROPERABILITY, VERIFICATION | Institutional integration must not begin until the core has demonstrated its transactional rules in a laboratory environment. |
| `ERX-REQ-TEST-0004` | VERIFICATION | — | The test program must cover functional, transactional, cryptographic, adversarial, operational and interoperability categories, including the twenty mandatory tests referenced in ERX-PROT-001 §19.1. |
| `ERX-REQ-TEST-0005` | PERFORMANCE_AND_CAPACITY | VERIFICATION, OPERATIONAL | Acceptance metrics must include ERX-added latency, processing time, accepted duplicate-operation rate, recovery time, case integrity, verifiable-test percentage, event loss and reconciliation capacity; numeric targets must be set before testing. |
| `ERX-REQ-PILOT-0001` | INTEROPERABILITY | OPERATIONAL, VERIFICATION | During shadow operation, the official infrastructure must continue receiving and attending calls while ERX receives authorized events, creates records and UTXOs, generates signatures and OTS commitments, verifies the case and compares results with official operation. |
| `ERX-REQ-PILOT-0002` | DATA_AND_RECORDS | VERIFICATION, OPERATIONAL | The shadow pilot must compare official and ERX-detected events, identifiers, timing differences, transfers, disconnects, integration errors, duplicate operations, recoveries and generated evidence. |
| `ERX-REQ-HOMO-0001` | GOVERNANCE | SECURITY, VERIFICATION, OPERATIONAL | Each center seeking technical homologation must demonstrate institutional identity, territorial authority, authorized credentials, adapter configuration, interface security, transactional integrity, UTXO operation, continuity, data protection, recovery and independent verification. |
| `ERX-REQ-HOMO-0002` | GOVERNANCE | INTEROPERABILITY, SECURITY | Admission of an additional center into multi-center operation must address institutional registration, identity/certificates, territorial configuration, authority rules, correlatable identifiers, transfer protocols, transaction coordination, interoperability tests, independent audit and institutional approval. |
| `ERX-REQ-RECV-0001` | DATA_AND_RECORDS | INTERFACE | The JSON 01 reception record includes the unique event ID, call ID, telephone-session ID, receiving gateway, reception source, observation time, available technical references and available origin information. |
| `ERX-REQ-LOC-0001` | DATA_AND_RECORDS | OPERATIONAL | Each location datum records its source, observation time, coordinates when available, estimated precision, location method and validation state. |
| `ERX-REQ-LOC-0002` | FUNCTIONAL | DATA_AND_RECORDS, OPERATIONAL | Absence of location does not block the call; subsequent location changes are recorded as new events and do not modify the original JSON 01. |
| `ERX-REQ-CONTACT-0001` | DATA_AND_RECORDS | OPERATIONAL | Initial call-reception time and agent-response time are recorded as distinct events. |
| `ERX-REQ-AGENT-0003` | SECURITY | OPERATIONAL, GOVERNANCE | Professional-agent verification records an explicit result; lack of authentication does not stop emergency attention, and a pending identity is never represented as verified. |
| `ERX-REQ-CONTACT-0002` | DATA_AND_RECORDS | FUNCTIONAL, OPERATIONAL | The contact result represents whether human contact was established, response without verifiable authentication, no response, transfer, termination before response or a technical exception; it must not represent human attention that did not occur. |
| `ERX-REQ-CORR-0001-A` | DATA_AND_RECORDS | SECURITY | Signed and committed JSON 01, JSON 02 and JSON 03 documents remain immutable. |
| `ERX-REQ-CORR-0001-B` | DATA_AND_RECORDS | SECURITY | A correction is recorded in a signed complementary document linked to the original and stating its reason. |
| `ERX-REQ-CORR-0001-C` | VERIFICATION | DATA_AND_RECORDS | The historical record remains reconstructable after a correction. |
| `ERX-REQ-TIME-0001` | DATA_AND_RECORDS | VERIFICATION | ERX distinguishes device-declared, gateway-observed, institutionally received, processed, signed, OTS-submitted and verifiably anchored times. |
| `ERX-REQ-TIME-0002-A` | DATA_AND_RECORDS | SECURITY | Times are retained in UTC with their precision and source. |
| `ERX-REQ-TIME-0002-B` | DATA_AND_RECORDS | OPERATIONAL | Local monotonic time is also recorded for session ordering when supported. |
| `ERX-REQ-TIME-0002-C` | OPERATIONAL | VERIFICATION | Timestamp discrepancies are documented rather than silently corrected. |
| `ERX-REQ-OTS-0003-A` | SECURITY | DATA_AND_RECORDS | Each JSON document has an independent cryptographic commitment. |
| `ERX-REQ-OTS-0003-B` | DATA_AND_RECORDS | VERIFICATION | The evidence workflow completes, freezes, canonicalizes and signs the document before calculating its commitment. |
| `ERX-REQ-OTS-0003-C` | VERIFICATION | SECURITY | The workflow requests OTS and retains and later updates the proof. |
| `ERX-REQ-OTS-0003-D` | VERIFICATION | DATA_AND_RECORDS | The proof is verified against the document and Bitcoin chain. |
| `ERX-REQ-OTS-0004` | VERIFICATION | SECURITY, GOVERNANCE | OTS evidence is not treated as proof that content is true, a person’s identity is genuine, an agent acted correctly, a location is exact, audio is complete, a center is authorized or an event occurred at the exact second claimed. |
| `ERX-REQ-PRIV-0003-A` | PRIVACY | GOVERNANCE | Original call content and sensitive personal data remain in protected institutional infrastructure. |
| `ERX-REQ-PRIV-0003-B` | PRIVACY | SECURITY | Bitcoin and OTS receive cryptographic commitments rather than private call content. |
| `ERX-REQ-PRIV-0003-C` | PRIVACY | DATA_AND_RECORDS | Sensitive direct identifiers are not published. |
| `ERX-REQ-PRIV-0004-A` | PRIVACY | SECURITY | ERX avoids exposing direct identifiers, isolated hashes of personal data and unnecessary metadata. |
| `ERX-REQ-PRIV-0004-B` | PRIVACY | SECURITY | Where applicable, ERX uses high-entropy random commitments or equivalent cryptographic structures against enumeration. |
| `ERX-REQ-PRIV-0004-C` | PRIVACY | GOVERNANCE | Verification information remains under authorized control. |
| `ERX-REQ-PRIV-0005-A` | GOVERNANCE | PRIVACY | The institution defines retention periods and deletion procedures under applicable law. |
| `ERX-REQ-PRIV-0005-B` | PRIVACY | DATA_AND_RECORDS | Authorized deletion of content is not represented as deletion of an already published Bitcoin anchor. |
| `ERX-REQ-PRIV-0005-C` | DATA_AND_RECORDS | VERIFICATION | Minimum information is retained to explain the evidence and applied policy. |
| `ERX-REQ-OPS-0004` | OPERATIONAL | SECURITY, FUNCTIONAL | When identity services are unavailable, the call continues and identity remains pending or unverified until checked; pending validation is not converted by default into successful authentication. |
| `ERX-REQ-OPS-0005-A` | OPERATIONAL | SECURITY | During ERX unavailability, events are retained in a durable protected local queue where technically possible. |
| `ERX-REQ-OPS-0005-B` | DATA_AND_RECORDS | OPERATIONAL | Recovery preserves original event time, recovery time and commitment-generation time separately. |
| `ERX-REQ-BOUND-0001` | ARCHITECTURAL | GOVERNANCE, OPERATIONAL | ERX does not replace the emergency number, telephone network, dispatch system, professional judgment of agents or public-authority competencies; each installation retains institutional independence and legal responsibilities. |

## 5. Candidate-level classification register

| Candidate ID | Primary type | Secondary tags | Statement classified |
|---|---|---|---|
| `ERX-REQ-UTXO-0001` | FUNCTIONAL | DATA_AND_RECORDS | A valid transition consumes a prior state and creates the next; consumed state is unavailable for another transition but remains in institutional history. |
| `ERX-REQ-UTXO-0002` | SECURITY | DATA_AND_RECORDS | Each institutional UTXO must carry unique state, call and stage IDs; document cryptographic reference; prior-state reference when applicable; consumption state; process identity; observation/processing times; and institutional operation signature. |
| `ERX-REQ-UTXO-0003` | FUNCTIONAL | SECURITY | The implementation must prevent two processes from consuming the same valid state. |
| `ERX-REQ-UTXO-0004` | ARCHITECTURAL | SECURITY | Within authorized coordination scope, uniqueness is supported by persistent event IDs, storage uniqueness constraints, atomic operations, concurrency control, idempotency, transition history and safe recovery. |
| `ERX-REQ-UTXO-0005` | FUNCTIONAL | SECURITY | A retransmitted telephone event must not produce duplicate institutional effects. |
| `ERX-REQ-UTXO-0006` | SECURITY | DATA_AND_RECORDS | Canonicalization must use a documented specification such as RFC 8785 or a formally specified compatible alternative; the institutional document is signed with an authorized institutional key. |
| `ERX-REQ-UTXO-0007` | FUNCTIONAL | — | UTXO 01 must be linked to the original event and a uniqueness rule, and its creation must be atomic. |
| `ERX-REQ-UTXO-0008` | DATA_AND_RECORDS | OPERATIONAL | OTS evidence states distinguish not requested, sent, pending, updatable, anchored, verified and failed; emergency attention continues independently of OTS confirmation. |
| `ERX-REQ-UTXO-0009` | FUNCTIONAL | SECURITY | Each call event receives a persistent identity; retransmission does not create a new admission; consumption and state creation are atomic; retries return the original result when applicable. |
| `ERX-REQ-UTXO-0010` | FUNCTIONAL | SECURITY | Concurrent processes must not complete two valid transitions against the same state; storage must implement verifiable concurrency constraints. |
| `ERX-REQ-UTXO-0011` | FUNCTIONAL | SECURITY | A valid UTXO can be consumed only once; validation checks input existence, current validity, executor authorization and absence of prior consumption; state update is atomic. |
| `ERX-REQ-UTXO-0012` | OPERATIONAL | INTERFACE | OTS proof acquisition may complete later and must not delay or block emergency reception, acceptance or attention. |
| `ERX-REQ-OPS-0001` | OPERATIONAL | — | ERX failure must not prevent the institution from receiving and attending calls through its official telephone infrastructure. |
| `ERX-REQ-OPS-0002` | DATA_AND_RECORDS | OPERATIONAL | An event must not be represented as permanently recorded unless storage has confirmed it. |
| `ERX-REQ-INT-0001` | INTEROPERABILITY | INTERFACE | Each institutional adapter specifies inputs, outputs, authentication, errors, retries and duplicate handling. |
| `ERX-REQ-INST-0001` | GOVERNANCE | SECURITY, OPERATIONAL | Each installation must have a validated institutional configuration covering institution and authorized-center identity, jurisdiction, certificates, verification keys, authorized agents, location sources, integrations, storage/retention/privacy policy, OTS, recovery and continuity. |
| `ERX-REQ-INST-0002` | GOVERNANCE | SECURITY | The system must distinguish recognized/authorized institution, recognized but outside jurisdiction, cryptographically valid but institutionally unverified identity, expired or revoked certificate, unknown identity and trust-validation-pending states. |
| `ERX-REQ-INST-0003` | GOVERNANCE | FUNCTIONAL | Territorial coverage and routing boundaries must derive from official jurisdiction/routing rules and authorized data, not solely antenna location. |
| `ERX-REQ-KEY-0001` | GOVERNANCE | SECURITY | Institutional private keys must remain under the institution's control. |
| `ERX-REQ-KEY-0002` | SECURITY | DATA_AND_RECORDS | Historical signature verification must determine which key was authorized at issuance time, including its validity period and recorded revocation state. |
| `ERX-REQ-ARCH-0001` | ARCHITECTURAL | INTEROPERABILITY | Institutional differences must be handled through adapters while the ERX core remains common; adapters must not modify fundamental single-consumption and transaction-continuity rules. |
| `ERX-REQ-PRIV-0001` | SECURITY | PRIVACY, DATA_AND_RECORDS | Where recording is institutionally authorized, the original audio must remain in protected institutional storage and its reference, hash, format, duration, times, origin and retention state must be recorded. |
| `ERX-REQ-TRANS-0001` | FUNCTIONAL | DATA_AND_RECORDS, INTEROPERABILITY | A transfer of the same communication must record source/destination centers, delivering/receiving agents, time, reason and continuity/interruption, without creating duplicate admission. |
| `ERX-REQ-CLOSE-0001` | FUNCTIONAL | DATA_AND_RECORDS | Termination reason must distinguish normal farewell, citizen/agent termination, accidental disconnect, signal loss, technical interruption and transfer-related end; a disconnect must not be classified as normal farewell. |
| `ERX-REQ-VERIFY-0001` | SECURITY | VERIFICATION, DATA_AND_RECORDS | An exported case must be independently verifiable without direct production-database access and include the documents, transitions, trust references, signatures, OTS proofs, file manifests and historical identity references required for verification. |
| `ERX-REQ-VERIFY-0002` | INTERFACE | VERIFICATION | Verification output must distinguish success, failure, incomplete evidence, pending evidence and indeterminate results; unverified data must not be reported as satisfactory. |
| `ERX-REQ-AGENT-0001` | SECURITY | OPERATIONAL | Center institutional authentication and professional-agent authentication are separate validations; an unverified agent must be recorded as such and must not stop emergency attention. |
| `ERX-REQ-AGENT-0002` | FUNCTIONAL | DATA_AND_RECORDS, OPERATIONAL | If no human agent responds, record the attempted contact/non-response and do not fabricate a professional identity or conversation. |
| `ERX-REQ-OTS-0001` | DATA_AND_RECORDS | VERIFICATION | OTS lifecycle must distinguish not sent, sent, pending, updatable, anchored, verifiable and generation/update error; pending evidence must not be represented as anchored. |
| `ERX-REQ-VERIFY-0003` | SECURITY | VERIFICATION | Verifier output must separately report document integrity, institutional authenticity, professional identity, UTXO continuity, double-consumption check, temporal evidence, file integrity and chronology. |
| `ERX-REQ-OPS-0003` | FUNCTIONAL | OPERATIONAL | Telephone communication closure must not automatically mean that the related emergency incident or subsequent institutional actions are complete. |
| `ERX-REQ-AVAIL-0001` | FUNCTIONAL | OPERATIONAL | Agent availability must reflect actual operational state; no available-state output may be issued while the agent is busy, paused or otherwise unable to receive calls. |
| `ERX-REQ-AVAIL-0002` | ARCHITECTURAL | DATA_AND_RECORDS | Agent identity and availability remain distinct from each call's request, acceptance, session, closure and evidence; each new call creates its own linked state/evidence cycle without reusing consumed states. |
| `ERX-REQ-STATE-0001` | ARCHITECTURAL | FUNCTIONAL | The communication lifecycle and the agent-availability lifecycle must be documented as two independent state machines; definitive state names and transitions remain subject to protocol approval. |
| `ERX-REQ-STATE-0002` | FUNCTIONAL | DATA_AND_RECORDS, SECURITY | Each valid transition specification must identify its input state, authorized authority, preconditions, action/event, output UTXO, generated evidence and failure handling. |
| `ERX-REQ-INV-0001` | FUNCTIONAL | — | A closed communication session must not become active again. |
| `ERX-REQ-INV-0002` | DATA_AND_RECORDS | — | A complementary correction must not retroactively modify a sealed document. |
| `ERX-REQ-INV-0003` | DATA_AND_RECORDS | — | Every state transition must preserve its provenance. |
| `ERX-REQ-INV-0004` | FUNCTIONAL | SECURITY | Recovery must not resurrect states already consumed or credentials already revoked. |
| `ERX-REQ-DATA-0001` | DATA_AND_RECORDS | INTEROPERABILITY | Each defined JSON data structure must have a formal schema, a version and validation rules. |
| `ERX-REQ-CRYPTO-0001` | SECURITY | — | The digital-signature specification must define the signature algorithm and format, signer identity, associated certificate, trust-chain reference, signing time, historical validation, revocation handling and key rotation. |
| `ERX-REQ-CRYPTO-0002` | ARCHITECTURAL | SECURITY, DATA_AND_RECORDS | The cryptographic relationship among documents 01, 02 and 03 and their UTXO records must be defined without circular dependencies; the event document and UTXO transition record should be considered separately as recommended by the Roadmap. |
| `ERX-REQ-VERIFY-0004` | ARCHITECTURAL | VERIFICATION, SECURITY | The independent verifier must have sufficient independence from ERX Core that a producer-side failure or manipulation does not automatically compromise the audit result. |
| `ERX-REQ-TRANS-0002` | GOVERNANCE | FUNCTIONAL, INTEROPERABILITY | An interinstitutional transfer protocol must define the source center, receiving center, transfer authority, call identity, transfer state, receipt confirmation, transition responsibility, interruption handling and subsequent reconciliation. |
| `ERX-REQ-TEST-0001` | VERIFICATION | — | The test matrix must cover functional, transactional, cryptographic, adversarial, operational and interoperability categories. |
| `ERX-REQ-ARCH-0002` | ARCHITECTURAL | SECURITY | The system architecture must keep ERX Core, ERX Institutional Module and ERX Verifier functionally separated; the verifier must not be a privileged extension of the producer. |
| `ERX-REQ-UTXO-0013` | FUNCTIONAL | OPERATIONAL | Consumption of an input UTXO and creation of its successor must be designed as one transactional operation; external OTS processing must not be part of the transaction that conditions emergency attention. |
| `ERX-REQ-CORE-0001` | VERIFICATION | ARCHITECTURAL | The ERX Core must be demonstrated in a controlled environment before telephone or OTS integration begins. |
| `ERX-REQ-CORE-0002` | ARCHITECTURAL | FUNCTIONAL | The core development scope must include event intake, identity, admission, UTXO, state, idempotency, concurrency, document, signature, audit and recovery responsibilities. |
| `ERX-REQ-TEST-0002` | VERIFICATION | — | A controlled simulator must reproduce a complete call lifecycle, including admission, UTXO 01 creation, acceptance, UTXO 01 consumption, UTXO 02 creation, development, UTXO 02 consumption, UTXO 03 creation and case closure. |
| `ERX-REQ-TEST-0003` | VERIFICATION | OPERATIONAL | The core test suite must cover competing consumption, identical requests, retries after timeout, retransmission, replay of old operations, interruption during transition, backup restoration, inconsistent input/output persistence and incompatible concurrent center transitions. |
| `ERX-REQ-IDENT-0001` | GOVERNANCE | SECURITY | The system must maintain separate identity records for institution, PSAP center, gateway, professional agent, authorized device/component, trust authority and certificate issuer. |
| `ERX-REQ-IDENT-0002` | SECURITY | — | A credential with pending verification must not be treated as valid authentication; the system must distinguish valid, expired, revoked, territorially unauthorized, functionally unauthorized, unknown and pending states. |
| `ERX-REQ-KEY-0003` | GOVERNANCE | SECURITY | Key management must cover secure generation, public-key registration, private-key custody, institutional signing, rotation, revocation, historical verification and usage auditing. |
| `ERX-REQ-SEC-0001` | SECURITY | INTERFACE, OPERATIONAL | Security interfaces must provide mutual authentication, role-based authorization, encryption in transit and at rest, replay protection, session control, secret management, security logs and privilege separation. |
| `ERX-REQ-OTS-0002` | SECURITY | DATA_AND_RECORDS, VERIFICATION | The evidence process must receive the final document, validate its schema, canonicalize it, hash it, link it to its UTXO transition, obtain the institutional signature, create the timestamp commitment, retain the proof and support later update and verification. |
| `ERX-REQ-PRIV-0002` | SECURITY | PRIVACY, DATA_AND_RECORDS | Original audio and files must not be sent to Bitcoin; they must remain under institutional custody with identifiers, hashes, manifests, protected logical location, retention policy, access evidence and recovery tests. |
| `ERX-REQ-VERIFY-0005` | SECURITY | VERIFICATION, DATA_AND_RECORDS | An exported case verifier must report schema, document hash, signature, institutional identity, historical credential validity, UTXO continuity, single consumption, OTS state, file integrity and chronology outcomes. |
| `ERX-REQ-INT-0002` | GOVERNANCE | INTEROPERABILITY, VERIFICATION | Institutional integration must not begin until the core has demonstrated its transactional rules in a laboratory environment. |
| `ERX-REQ-TEST-0004` | VERIFICATION | — | The test program must cover functional, transactional, cryptographic, adversarial, operational and interoperability categories, including the twenty mandatory tests referenced in ERX-PROT-001 §19.1. |
| `ERX-REQ-TEST-0005` | PERFORMANCE_AND_CAPACITY | VERIFICATION, OPERATIONAL | Acceptance metrics must include ERX-added latency, processing time, accepted duplicate-operation rate, recovery time, case integrity, verifiable-test percentage, event loss and reconciliation capacity; numeric targets must be set before testing. |
| `ERX-REQ-PILOT-0001` | INTEROPERABILITY | OPERATIONAL, VERIFICATION | During shadow operation, the official infrastructure must continue receiving and attending calls while ERX receives authorized events, creates records and UTXOs, generates signatures and OTS commitments, verifies the case and compares results with official operation. |
| `ERX-REQ-PILOT-0002` | DATA_AND_RECORDS | VERIFICATION, OPERATIONAL | The shadow pilot must compare official and ERX-detected events, identifiers, timing differences, transfers, disconnects, integration errors, duplicate operations, recoveries and generated evidence. |
| `ERX-REQ-HOMO-0001` | GOVERNANCE | SECURITY, VERIFICATION, OPERATIONAL | Each center seeking technical homologation must demonstrate institutional identity, territorial authority, authorized credentials, adapter configuration, interface security, transactional integrity, UTXO operation, continuity, data protection, recovery and independent verification. |
| `ERX-REQ-HOMO-0002` | GOVERNANCE | INTEROPERABILITY, SECURITY | Admission of an additional center into multi-center operation must address institutional registration, identity/certificates, territorial configuration, authority rules, correlatable identifiers, transfer protocols, transaction coordination, interoperability tests, independent audit and institutional approval. |
| `ERX-REQ-RECV-0001` | DATA_AND_RECORDS | INTERFACE | The JSON 01 reception record includes the unique event ID, call ID, telephone-session ID, receiving gateway, reception source, observation time, available technical references and available origin information. |
| `ERX-REQ-LOC-0001` | DATA_AND_RECORDS | OPERATIONAL | Each location datum records its source, observation time, coordinates when available, estimated precision, location method and validation state. |
| `ERX-REQ-LOC-0002` | FUNCTIONAL | DATA_AND_RECORDS, OPERATIONAL | Absence of location does not block the call; subsequent location changes are recorded as new events and do not modify the original JSON 01. |
| `ERX-REQ-CONTACT-0001` | DATA_AND_RECORDS | OPERATIONAL | Initial call-reception time and agent-response time are recorded as distinct events. |
| `ERX-REQ-AGENT-0003` | SECURITY | OPERATIONAL, GOVERNANCE | Professional-agent verification records an explicit result; lack of authentication does not stop emergency attention, and a pending identity is never represented as verified. |
| `ERX-REQ-CONTACT-0002` | DATA_AND_RECORDS | FUNCTIONAL, OPERATIONAL | The contact result represents whether human contact was established, response without verifiable authentication, no response, transfer, termination before response or a technical exception; it must not represent human attention that did not occur. |
| `ERX-REQ-CORR-0001` | DATA_AND_RECORDS | SECURITY, VERIFICATION | Signed and committed JSON 01, JSON 02 and JSON 03 documents remain immutable; a correction is recorded in a signed complementary document linked to the original with its reason, and the historical record remains reconstructable. |
| `ERX-REQ-TIME-0001` | DATA_AND_RECORDS | VERIFICATION | ERX distinguishes device-declared, gateway-observed, institutionally received, processed, signed, OTS-submitted and verifiably anchored times. |
| `ERX-REQ-TIME-0002` | DATA_AND_RECORDS | SECURITY, OPERATIONAL | Times are retained in UTC with precision and source; local monotonic time is also recorded for session ordering when supported, and discrepancies are documented rather than silently corrected. |
| `ERX-REQ-OTS-0003` | VERIFICATION | SECURITY, DATA_AND_RECORDS | Each JSON document has an independent cryptographic commitment; the evidence workflow completes, freezes, canonicalizes and signs the document, calculates its commitment, requests OTS, retains and later updates the proof, and verifies it against the document and Bitcoin chain. |
| `ERX-REQ-OTS-0004` | VERIFICATION | SECURITY, GOVERNANCE | OTS evidence is not treated as proof that content is true, a person’s identity is genuine, an agent acted correctly, a location is exact, audio is complete, a center is authorized or an event occurred at the exact second claimed. |
| `ERX-REQ-PRIV-0003` | PRIVACY | SECURITY, DATA_AND_RECORDS | Original call content and sensitive personal data remain in protected institutional infrastructure; Bitcoin and OTS receive cryptographic commitments rather than private call content, and sensitive direct identifiers are not published. |
| `ERX-REQ-PRIV-0004` | PRIVACY | SECURITY, DATA_AND_RECORDS | ERX avoids exposing direct identifiers, isolated hashes of personal data and unnecessary metadata; where applicable it uses high-entropy random commitments or equivalent cryptographic structures against enumeration, with verification information under authorized control. |
| `ERX-REQ-PRIV-0005` | PRIVACY | GOVERNANCE, DATA_AND_RECORDS | The institution defines retention periods and deletion procedures under applicable law; authorized deletion of content is not represented as deletion of an already published Bitcoin anchor, and minimum information is retained to explain the evidence and applied policy. |
| `ERX-REQ-OPS-0004` | OPERATIONAL | SECURITY, FUNCTIONAL | When identity services are unavailable, the call continues and identity remains pending or unverified until checked; pending validation is not converted by default into successful authentication. |
| `ERX-REQ-OPS-0005` | OPERATIONAL | DATA_AND_RECORDS, SECURITY | During ERX unavailability, where technically possible, events are retained in a durable protected local queue; recovery preserves original event time, recovery time and commitment-generation time separately. |
| `ERX-REQ-BOUND-0001` | ARCHITECTURAL | GOVERNANCE, OPERATIONAL | ERX does not replace the emergency number, telephone network, dispatch system, professional judgment of agents or public-authority competencies; each installation retains institutional independence and legal responsibilities. |

## 6. Limitations and retained gates

1. The classifications are based on the normalized statements in the current registers, not a fresh verbatim re-transcription of every source clause, diagram or table.
2. Classification does not establish whether a statement is mandatory. Normative modality and source authority remain for 0.7.5 and 0.7.9.
3. Classification does not determine whether a statement is a design requirement or an adopted design decision; that remains for 0.7.6 and WP-0.8.
4. A primary type is a controlled taxonomy label, not a priority, legal status, approval or implementation instruction.
5. Exact source fidelity, contradictions and unresolved terminology remain open and must not be silently inferred.

## 7. Controlled files updated

- `registers/requirements-traceability.csv` — all 82 candidate classifications reviewed.
- `registers/requirement-identification-register.csv` — all 107 individual classifications reviewed.
- `WORKPLAN-PHASE-0.md` — activity 0.7.4 marked complete with scope limitation recorded.

## 8. Determination

**Activity 0.7.4: COMPLETED — classification recorded for 82 source candidates and 107 individual requirements.** The classification review is complete at the statement/register level. Source-fidelity and normative approval remain separate gates. WP-0.7 overall remains IN_PROGRESS; no requirements baseline is approved by this record.

---
End of classification record v1.0.0.
