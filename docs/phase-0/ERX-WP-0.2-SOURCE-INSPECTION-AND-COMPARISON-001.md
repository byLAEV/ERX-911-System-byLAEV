# ERX-WP-0.2-SOURCE-INSPECTION-AND-COMPARISON-001
## Source Inspection Record and Bounded Cross-Document Comparison

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.2-SOURCE-INSPECTION-AND-COMPARISON-001 |
| Version | 0.1.0 |
| Status | WORKING EVIDENCE — SUBMITTED FOR LAEV REVIEW |
| Work Package | WP-0.2 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Inspection basis | Five mounted original PDFs and repository inventory |
| Date | 2026-11-23 |
| Approval | NOT APPROVED |

## 1. Purpose and boundaries

This record deepens WP-0.2 source inspection and cross-reference activity. It identifies the subject structure and documented concepts of each of the five available originals, then records only relationships and differences directly supportable by their contents.

It is an inspection aid, not a requirements extraction, technical validation, document hierarchy, legal assessment, or resolution of conflicts. The record does not silently normalize terminology, fill omissions, or treat a recommendation as an approved amendment.

## 2. Inspection set and identity

The five PDFs correspond to FND-001 through FND-005 in the foundational register. The exact repository paths, SHA-256 checksums, Git blob identities, and archival evidence are in:
- `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`
- `registers/foundational-material-register.csv`
- `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`

The files were text-extracted for inspection. Text extraction supports heading/topic review but does not replace the visual review of diagrams, tables, signatures, or layout-dependent statements. This limitation is particularly relevant to the Atlas.

## 3. Source-by-source inspection

### FND-001 — ERX-PROT-001 v1.1 (29 pages)

The document identifies itself as an institutional protocol specification for admission, communication, transactional uniqueness, and verifiable evidence for 911 calls. It states that v1.1 updates v1.0 and retains the fundamental architecture while strengthening identity, uniqueness, concurrency, continuity, privacy, audit, and independent verification.

The inspected structure includes:
- Sections 1–4: purpose, fundamental principle, participants, and prior institutional requirements.
- Sections 5–9: integral architecture, three transaction stages, and the three-document structure.
- Section 10 and subsections 10.1–10.11: identity/admission/consumption uniqueness, atomicity, idempotency, concurrency, event replay, history, corrections, state separation, and inter-installation coordination.
- Sections 11–12: temporal protection/order and OpenTimestamps evidence.
- Sections 13–18: privacy, corrections/audit/traceability, independent verification, exceptions, continuity, and security.
- Sections 19–21: implementation/validation requirements, product boundary, and final protocol definition.

These headings are a topic map only. Detailed requirement statements must be extracted separately with exact clause references and source wording.

### FND-002 — ERX-ATLAS-001 v1.1 (29 pages)

The supplied filename is `ERX-ATLAS-001 v1.pdf`; internal document control identifies version 1.1. Both are retained without renaming the original.

The Atlas identifies ERX-PROT-001 v1.1 as its related normative document. Its stated purpose is to graphically represent the protocol from emergency-call intake through final record and cryptographic evidence.

The inspected diagrams cover:
- General protocol architecture.
- Reception, location, routing, and institutional validation.
- Contact, agent authentication, and the second transition.
- Development, chronological recording, and closure.
- Prevention of duplicate consumption and atomic transition behavior.
- Temporal evidence and OTS anchoring.
- Continuity, recovery, and exceptional conditions.
- Institutional storage, privacy boundaries, and independent verification.
- Protocol-to-Atlas correspondence and documentary coordination.

The Atlas states that UTXO transitions control uniqueness of institutional transitions and OTS supplies temporal evidence; it also distinguishes these functions from institutional authentication and proof of the material truth of a conversation.

Diagram interpretation is not decided here. The exact authority of individual plates relative to protocol clauses remains assigned to WP-0.3.

### FND-003 — UTXO-911-001 v1.0 (12 pages)

The document describes the functional concept of three linked stages in a 911 communication lifecycle:
1. Request/entry and creation of the first communication state.
2. Initial operator communication and creation of the second state.
3. Communication closure and creation of a new agent-availability state.

Its sections address stage definitions and processing, UTXO generation/consumption, OTS evidence, operator continuity, single-spend principles, and architectural result.

The source is functional/conceptual in its own stated classification. This record does not decide whether it is subordinate to, complementary with, or independently authoritative alongside ERX-PROT-001 v1.1.

### FND-004 — ERX-ROADMAP-001 v1.0 (37 pages)

The Roadmap defines the development sequence, phases, software architecture, responsibility separation, technical dependencies, deliverables, validation/testing, and progression criteria.

It cites ERX-PROT-001 v1.1, ERX-ATLAS-001 v1.1, UTXO-911-001 v1.0, ERX-CONSENSUS-001 v0.1, and ERX-IMPL-PROPOSAL-001.

The first three are in the inspected source set. The latter two are references in the Roadmap, but their original content and provenance have not been located or verified. Their reference in this source is not treated as evidence of their full contents.

The Roadmap remains the source for its detailed work-package and phase definitions. This inspection record does not alter its sequence or acceptance criteria.

### FND-005 — Technical Response to ERX-ROADMAP-001 (2 pages)

The supplied response has no formal document ID, version, or issue date stated in its visible title/control text. Its exact supplied filename is preserved.

It addresses:
- concurrency and duplicate events;
- inter-institutional transfers;
- documentary dependencies and normative consistency;
- independent UTXO cycles for 911 communication and agent availability;
- separation of ERX Protocol, ERX Core, ERX Institutional Module, and ERX Verifier;
- local transactional consumption/creation and asynchronous external temporal evidence/synchronization;
- evidence-based governance, independent verification, and quantitative acceptance criteria.

The response recommends retaining the Roadmap sequence and incorporating observations as implementation and validation requirements. It states that acceptance of proposed solutions depends on implementation, reproducible tests, and auditable evidence.

This is a recommendation/technical position. No approval or amendment record was supplied to establish that it formally revises ERX-ROADMAP-001.

## 4. Cross-source comparison — observed correspondences

| Topic | Sources | Directly supported correspondence | Not established by this record |
|---|---|---|---|
| Three-stage communication lifecycle | ERX-PROT-001; UTXO-911-001; Atlas | All describe a staged 911 communication lifecycle linked by UTXO state transitions | Final precedence, complete clause-to-diagram equivalence, or whether every term is identical in meaning |
| Institutional protocol and diagrams | ERX-PROT-001; ERX-ATLAS-001 | Atlas explicitly names Protocol v1.1 as related normative document and depicts protocol operations | Normative status of every diagram and rule for diagram/text divergence |
| OTS evidence | Protocol; Atlas; UTXO; Roadmap; Response | OTS appears as temporal/cryptographic evidence; Response says external evidence should not condition emergency attention | Exact service availability guarantees, timing, final implementation design, or proof beyond each source's stated limits |
| Single-use state and duplicate prevention | Protocol; Atlas; UTXO | Sources describe consumption/creation transitions and preventing reuse of a state/event | Whether all implementation race conditions and cross-center transfer semantics are fully specified |
| Institutional transfer/coordination | Protocol; Roadmap; Response; Atlas | Coordination, transfers, and exceptional continuity are identified as relevant concerns | A complete approved transfer authority/receipt/reconciliation protocol |
| Governance and validation | Roadmap; Response; Protocol | Progression should rely on defined deliverables, validation, and evidence; Response expressly favors evidence-based acceptance | Formal approval effect of Response and a complete independent-verifier acceptance specification |
| Missing referenced sources | Roadmap | Roadmap cites Consensus and Implementation Proposal | Their content, authority, version authenticity, and current approval status |

## 5. Source-dependent matters carried forward

1. **DOC-ISS-001:** Atlas filename/internal version discrepancy — preserve filename; cite internal v1.1; canonical naming decision reserved for document control.
2. **DOC-ISS-002:** ERX-CONSENSUS-001 v0.1 — NOT LOCATED / UNVERIFIED.
3. **DOC-ISS-003:** ERX-IMPL-PROPOSAL-001 — NOT LOCATED / UNVERIFIED.
4. **DOC-ISS-004:** Technical Response formal ID/version/date — not stated in supplied source.
5. **DOC-ISS-005:** UTXO-911-001 and ERX-PROT-001 authority/scope relationship — not adjudicated.
6. **DOC-ISS-006:** Atlas diagram authority and clause-to-plate mapping — not adjudicated.
7. **DOC-ISS-007:** Technical Response amendment effect on Roadmap — no approval evidence identified.
8. **DOC-ISS-008:** Repository archival/byte identity — RESOLVED_EVIDENCE in completion dossier.

## 6. WP-0.2 evidence status

This record advances source inspection and cross-reference preparation. It does not by itself close WP-0.2 because:
- the two Roadmap-referenced sources remain unlocated and require LAEV's disposition;
- the Atlas filename/internal-version discrepancy and response metadata remain open;
- LAEV's acceptance of the source inventory and proposed bounded treatment has not been recorded.

Recommended status remains **IN_REVIEW — LAEV DECISION PENDING**.

## 7. Handoff boundary to WP-0.3

After WP-0.2 acceptance, WP-0.3 can formally examine document classes, hierarchy, subject-matter authority, diagram/text interpretation, amendment effect, and contradiction handling using this inspection record and the issue register.

No hierarchy or conflict resolution is approved by this document.

---
End of ERX-WP-0.2-SOURCE-INSPECTION-AND-COMPARISON-001
