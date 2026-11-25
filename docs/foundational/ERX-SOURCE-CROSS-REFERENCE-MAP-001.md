# ERX-SOURCE-CROSS-REFERENCE-MAP-001
## Foundational Source Relationships and Inspection Map — WP-0.2

| Field | Value |
|---|---|
| Document ID | ERX-SOURCE-CROSS-REFERENCE-MAP-001 |
| Version | 0.2.0 |
| Status | WORKING DRAFT — NOT APPROVED |
| Work Package | WP-0.2 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Basis | Direct inspection of the five supplied original PDFs |
| Date | 2026-11-23 |

## 1. Purpose and boundary

This map records explicit references and subject-matter relationships observed in the five supplied PDFs. It supports WP-0.2 activity 0.2.8 and prepares evidence for WP-0.3.

It does not establish a binding document hierarchy, resolve contradictions, declare one source universally superior to another, or convert recommendations into approved requirements. Those determinations remain subject to the formal work packages and approval gates in the Workplan.

## 2. Source set inspected

| Source ID | Document | Version stated | Supplied file | Pages |
|---|---|---:|---|---:|
| FND-001 | ERX-PROT-001 — Institutional Protocol | 1.1 | `ERX byLAEV 1.pdf` | 29 |
| FND-002 | ERX-ATLAS-001 — Institutional Atlas | 1.1 | `ERX-ATLAS-001 v1.pdf` | 29 |
| FND-003 | UTXO-911-001 — UTXO de Comunicación 911 | 1.0 | `UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | 12 |
| FND-004 | ERX-ROADMAP-001 — Master Phase Plan | 1.0 | `### ERX-ROADMAP-001.pdf` | 37 |
| FND-005 | Technical Response to ERX-ROADMAP-001 | Not stated | `Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | 2 |

SHA-256 values and exact filenames are maintained in `ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md` and `registers/foundational-material-register.csv`.

## 3. Explicit source references

### 3.1 ERX-ROADMAP-001 references the foundational protocol set

In its purpose/foundation section, ERX-ROADMAP-001 identifies:
- ERX-PROT-001 v1.1 — institutional protocol.
- ERX-ATLAS-001 v1.1 — architecture atlas and diagrams.
- UTXO-911-001 v1.0 — UTXO for 911 communication.

It additionally names:
- ERX-CONSENSUS-001 v0.1 — consensus framework.
- ERX-IMPL-PROPOSAL-001 — institutional implementation proposal.

The latter two are not among the five supplied PDFs inspected for this map. Their existence is evidenced as a reference in the Roadmap only; their contents, exact versions, provenance, and current status are not verified.

### 3.2 ERX-ATLAS-001 identifies its normative relationship

The Atlas title/control section identifies ERX-PROT-001 v1.1 as its related normative document. This is an explicit document relationship stated by the Atlas itself.

### 3.3 Technical Response addresses ERX-ROADMAP-001

FND-005 is expressly titled as a response to observations on ERX-ROADMAP-001. It discusses the Roadmap's proposed architecture and management considerations. Its formal document identifier, version, and issue date are not stated in the supplied two-page document.

## 4. Subject-matter relationship matrix

| From | To | Relationship evidenced in source | Evidence location | Boundary |
|---|---|---|---|---|
| ERX-ATLAS-001 v1.1 | ERX-PROT-001 v1.1 | Atlas names Protocol as its related normative document | Atlas title/control section | Explicit relation; not a complete hierarchy |
| ERX-ROADMAP-001 v1.0 | ERX-PROT-001 v1.1 | Roadmap identifies Protocol as a foundation | Roadmap, Section 1, “Purpose” / foundational basis | Explicit reference |
| ERX-ROADMAP-001 v1.0 | ERX-ATLAS-001 v1.1 | Roadmap identifies Atlas as a foundation | Roadmap, Section 1, “Purpose” / foundational basis | Explicit reference |
| ERX-ROADMAP-001 v1.0 | UTXO-911-001 v1.0 | Roadmap identifies UTXO communication specification as a foundation | Roadmap, Section 1, “Purpose” / foundational basis | Explicit reference |
| ERX-PROT-001 v1.1 | ERX-ATLAS-001 v1.1 | Protocol's three-stage lifecycle is represented in Atlas diagrams | Protocol Sections 1, 5–8; Atlas objective and Plates 01–04 | Observed subject-matter correspondence; exact diagram-to-clause validation remains for technical review |
| UTXO-911-001 v1.0 | ERX-PROT-001 v1.1 | Both describe a three-stage UTXO lifecycle for an emergency communication | UTXO Sections 1–8; Protocol Sections 1, 5–10 | Subject-matter correspondence; no formal precedence inferred |
| ERX-ROADMAP-001 v1.0 | ERX-CONSENSUS-001 v0.1 | Roadmap cites the consensus framework as a reference to be completed before multi-institutional implementation | Roadmap, Section 1 and later consensus-related references | Referenced source not supplied/verified |
| ERX-ROADMAP-001 v1.0 | ERX-IMPL-PROPOSAL-001 | Roadmap cites an institutional implementation proposal as a foundation | Roadmap, Section 1 | Referenced source not supplied/verified |
| Technical Response FND-005 | ERX-ROADMAP-001 v1.0 | Response addresses observations and recommendations concerning Roadmap | Entire two-page response | Explicit response relationship |
| Technical Response FND-005 | ERX-PROT-001 / ERX-ATLAS-001 | Response supports maintaining separation of ERX Protocol, ERX Core, ERX Institutional Module, and ERX Verifier | Response, page 1 | Design position in response; not proof of a formal change to either source |

## 5. Topic inspection map

This section records source headings and themes observed during inspection. It is an index for later extraction, not a requirements register.

### FND-001 — ERX-PROT-001 v1.1

Identified sections include:
- 1. Purpose of the protocol.
- 2. Fundamental principle: one communication, one transactional sequence.
- 3. Participants and responsibilities.
- 4. Prior institutional requirements.
- 5. Integral architecture.
- 6. First transaction: reception.
- 7. Second transaction: contact establishment.
- 8. Third transaction: development and closure.
- 9. Structure of the three documents.
- 10. Uniqueness and double-spend prevention rules, including identity, admission, consumption, atomicity, idempotency, concurrency, event replay, history, corrections, state separation, and coordination between installations.
- 11–12. Temporal protection, ordering, and OpenTimestamps evidence.
- 13. Data protection and privacy.
- 14. Corrections, audit, and traceability.
- 15. Independent verification.
- 16. Exception handling.

### FND-002 — ERX-ATLAS-001 v1.1

The Atlas identifies its objective as graphical representation of the protocol from emergency-call intake through final record and verifiable cryptographic evidence. The inspected plates include:
- Plate 01 — General ERX protocol architecture.
- Plate 02 — Reception, location, and routing.
- Plate 03 — Contact establishment and agent authentication.
- Plate 04 — Comprehensive development and communication closure.

The Atlas states that UTXOs control uniqueness of institutional transitions and OTS supplies independent temporal evidence. It also states that neither replaces institutional authentication nor by itself proves the material truth of a conversation.

### FND-003 — UTXO-911-001 v1.0

Identified sections include:
- 1. General concept.
- 2. First stage: request and entry of the 911 call.
- 3. Second stage: initial communication protocol of the 911 operator.
- 4. Third stage: communication closure and generation of a new availability state.
- 5. Continuity of an operator's UTXO cycle.
- 6. Single-spend principle applied to 911 communication.
- 7. OpenTimestamps function within the protocol.
- 8. Architectural result.

### FND-004 — ERX-ROADMAP-001 v1.0

The inspected opening identifies the Roadmap's purpose as defining development order, phases, software architecture, separation of responsibilities, technical dependencies, deliverables, validation/testing, and phase progression criteria. Its foundation section cites the three supplied technical sources and the two additional unverified references.

The complete Roadmap contains 37 pages. This map does not reproduce its entire phase breakdown; the original PDF remains the source for detailed phase activities, dependencies, deliverables, and acceptance criteria.

### Supplemental source identity — ERX-CONSENSUS-001 v0.1
The Roadmap cites ERX-CONSENSUS-001 v0.1 as a coordination reference. The post-approval repository text source `docs/Consenso ERX byLAEV` directly declares that identifier/version, proposal-for-review status, and LAEV/byLAEV authorship; it matches the Roadmap citation. The source defines Triple Consensus and evidence/traceability principles but defers quorum, validator rules, conflict resolution, and detailed consensus UTXO/JSON and derived specifications. Source identity is confirmed; DOC-ISS-011 tracks authority and operational completion. This supplemental finding does not alter the five-PDF WP-0.2 acceptance baseline.

### FND-005 — Technical Response

The response discusses:
- Concurrency and duplicated events.
- Inter-institutional transfers.
- Documentary dependencies and normative consistency.
- Separate UTXO cycles for 911 communication and agent availability.
- Separation of Protocol, Core, Institutional Module, and Verifier.
- Asynchronous external timestamping and synchronization relative to emergency response.
- Independent verifier and quantitative acceptance criteria.
- Evidence-based progression rather than administrative progress indicators.

The response recommends retaining the Roadmap's development sequence while incorporating observations as implementation and validation requirements. This is a recommendation/position in FND-005, not an approval record for every individual item.

## 6. Matters reserved for WP-0.3

The following must not be decided by this map:
1. Which document has authority when two sources conflict.
2. Whether a diagram is normative, explanatory, or illustrative in every instance.
3. Whether FND-003 is subordinate to, complementary to, or independently authoritative alongside FND-001.
4. Whether the Technical Response modifies, interprets, or only comments on the Roadmap.
5. How later approved development documents affect foundational sources.
6. How to resolve version discrepancies or missing formal metadata.

These matters require a formal document hierarchy, subject-matter authority rules, and contradiction procedure under WP-0.3.

## 7. WP-0.2 status contribution

Activity 0.2.8 — Record references between sources: **PREPARED — WORKING DRAFT**.

This map provides an auditable first-pass relationship inventory based on direct source inspection. The five original PDFs have now been located in `docs/` on `main`; their SHA-256 checksums match the foundational register, and their Git blob identities match the repository objects. See `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`. ERX-CONSENSUS-001 v0.1 identity is now confirmed by supplemental text evidence; ERX-IMPL-PROPOSAL-001 remains NOT LOCATED / UNVERIFIED. Final register review and express LAEV approval remain outstanding.

---
End of ERX-SOURCE-CROSS-REFERENCE-MAP-001
