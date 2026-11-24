# ERX-FOUNDATIONAL-MATERIAL-REGISTER-001
## Foundational Source Inventory — Phase 0 / WP-0.2

| Field | Value |
|---|---|
| Project | ERX byLAEV — 911 Double-Spend System |
| Register ID | ERX-FOUNDATIONAL-MATERIAL-REGISTER-001 |
| Version | 0.1.0 |
| Status | IN_PROGRESS — inventory baseline |
| Work Package | WP-0.2 |
| Prepared by | LAEV / byLAEV project documentation |
| Inventory basis | Five original PDF files supplied in the project conversation |
| Inventory date | 2026-11-23 |

## 1. Purpose

This register records the foundational ERX source files that were directly available for inspection during WP-0.2. It distinguishes source identity, the document's internal identifier and version, the supplied filename, documentary nature, provenance, integrity evidence, and unresolved matters.

This is an inventory baseline, not a declaration that WP-0.2 or Phase 0 is complete.

## 2. Inventory Method and Evidence

The five supplied PDF files were opened and their text extracted for inspection. Page counts and SHA-256 checksums were recorded from the supplied files. The checksum identifies the exact supplied PDF bytes; it does not establish authorship, publication date, or legal authenticity by itself.

Original supplied filenames are preserved in this register. Where the filename differs from the document's internal title or version, both are recorded without silently renaming the source.

## 3. Foundational Source Inventory

| Register ID | Internal document ID / title | Internal version | Supplied original filename | Nature / role | Authorship shown in source | Pages | SHA-256 |
|---|---|---:|---|---|---|---:|---|
| FND-001 | ERX-PROT-001 — ERX byLAEV Institutional Protocol | 1.1 | `ERX byLAEV 1.pdf` | Institutional protocol specification; normative/functional source | LAEV / byLAEV | 29 | `5e1647c30f1aae77726619272c7730306b2e7c138e920cf8be91542e1ee77fbd` |
| FND-002 | ERX-ATLAS-001 — Institutional Atlas of ERX byLAEV Flow Diagrams and Operation | 1.1 | `ERX-ATLAS-001 v1.pdf` | Graphical and operational representation of the protocol | LAEV / byLAEV | 29 | `7029d5f5cabeedd783eb5fec6cf66ddafa7e224c16ef7644656e89dd7921ec7f` |
| FND-003 | UTXO-911-001 — UTXO de Comunicación 911 byLAEV | 1.0 | `UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | Conceptual and functional specification of the three-stage 911 communication UTXO cycle | LAEV / byLAEV | 12 | `39fa464f8ec774bf55f50e7d042c19728e2467be2bbb7234b15142a89321c4cc` |
| FND-004 | ERX-ROADMAP-001 — Master Phase Plan for ERX Development, Implementation and Institutional Homologation | 1.0 | `### ERX-ROADMAP-001.pdf` | Development planning document; phase sequence, dependencies, deliverables and progression criteria | LAEV / byLAEV | 37 | `b529fb306c19704bd163ed3a26f9d9b737057415a6d5839056f394791fdadca3` |
| FND-005 | Technical Response to the Observations on ERX-ROADMAP-001 | Not stated in supplied document | `Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | Technical response and design/management observations associated with the Roadmap | Signed LAEV / byLAEV | 2 | `1b8bd77ac2b7789269d6152d172fbb301d3609fc2db223aa1e4b8ed35884fba9` |

## 4. Source Details and Observations

### FND-001 — ERX-PROT-001 v1.1

The document identifies itself as an institutional protocol for admission, communication, transactional uniqueness, and verifiable evidence for 911 emergency calls. It states that version 1.1 updates version 1.0, strengthening institutional identity, transactional uniqueness, concurrency, operational continuity, privacy, audit, and independent verification.

Its stated three-stage communication structure is:
1. Origin registration, reception, available location, and routing.
2. Contact establishment and authentication of the receiving agent.
3. Comprehensive development and closure of the communication.

It describes three independent JSON documents, three UTXO transitions, cryptographic commitments, and three OpenTimestamps evidence references for the basic call record.

### FND-002 — ERX-ATLAS-001 v1.1

The supplied filename includes “v1”, while the document's internal title and control information identify version 1.1. The register therefore records the internal version as 1.1 and retains the filename exactly as supplied.

The Atlas graphically represents the ERX protocol from emergency-call intake through the final record and cryptographic evidence. It states that UTXOs control uniqueness of institutional transitions and OTS provides independent temporal evidence; neither replaces institutional authentication nor independently proves the material truth of a conversation.

### FND-003 — UTXO-911-001 v1.0

The document identifies itself as a conceptual and functional protocol document describing the three stages of the 911 communication cycle. It describes each stage as consuming a prior state and producing a new state, with the objective of preventing reuse of a request, acceptance, communication session, or closure as a new event.

No document issue date is stated in the inspected title/control section.

### FND-004 — ERX-ROADMAP-001 v1.0

The Roadmap identifies its reference date as 23 November 2026, 21:06, UTC−06:00, and gives an approximate location reference of San Ramón, Costa Rica. It identifies the following source documents:
- ERX-PROT-001 v1.1.
- ERX-ATLAS-001 v1.1.
- UTXO-911-001 v1.0.
- ERX-CONSENSUS-001 v0.1.
- ERX-IMPL-PROPOSAL-001.

The first three are present in the supplied inventory. The latter two are cited by the Roadmap but were not among the five supplied PDFs inspected for this baseline. Their availability and versions therefore remain unverified.

### FND-005 — Technical Response to ERX-ROADMAP-001

The two-page response addresses concurrency, duplicated events, inter-institutional transfers, documentary dependencies, governance, and normative consistency. It supports maintaining separate UTXO cycles for 911 communication and agent availability, separating ERX Protocol, ERX Core, ERX Institutional Module, and ERX Verifier, and running external temporal evidence and synchronization asynchronously relative to emergency response.

The supplied document does not state a formal document identifier, version, or issue date in the inspected content. Those fields must remain “not stated” unless an authoritative source is located.

## 5. Source Relationships Identified

| Source | Relationship |
|---|---|
| ERX-PROT-001 v1.1 | Primary institutional protocol specification. |
| ERX-ATLAS-001 v1.1 | Graphical/operational representation explicitly related to ERX-PROT-001 v1.1. |
| UTXO-911-001 v1.0 | Functional specification of the 911 communication UTXO cycle; cited by ERX-ROADMAP-001. |
| ERX-ROADMAP-001 v1.0 | Development plan based on the existing ERX documents and references ERX-CONSENSUS-001 and ERX-IMPL-PROPOSAL-001. |
| Technical Response to ERX-ROADMAP-001 | Response to observations and recommendations concerning the Roadmap; supports retaining its development sequence subject to verifiable implementation and validation. |

These relationships record explicit references and observed subject-matter relationships. They do not, by themselves, establish a complete document hierarchy or resolve conflicts. Those are WP-0.3 matters.

## 6. Missing or Unverified Sources

The following documents are referenced by ERX-ROADMAP-001 but were not present in the five supplied PDFs inspected for this inventory baseline:

| Reference | Description in Roadmap | Inventory status | Required action |
|---|---|---|---|
| ERX-CONSENSUS-001 v0.1 | Consensus framework; coordination reference to be completed before multi-institutional implementation | NOT LOCATED / UNVERIFIED | Locate the original file; verify title, version, contents, provenance and status. |
| ERX-IMPL-PROPOSAL-001 | Institutional implementation proposal | NOT LOCATED / UNVERIFIED | Locate the original file; verify title, version, contents, provenance and status. |

No conclusion is made that these documents do not exist. Only their absence from the five-file source set inspected for this baseline is established.

## 7. Preservation and Repository Custody

The five PDFs were available as original supplied files in the working conversation environment and were inspected without editing their contents. Their exact SHA-256 checksums are recorded above.

**Repository preservation is still pending.** The binary PDF originals have not yet been committed to `docs/foundational/` in the GitHub repository as part of this WP-0.2 operation. This register must not be interpreted as evidence that repository archival has already occurred.

Before repository archival:
1. Confirm the canonical original filename for each PDF.
2. Copy the exact original bytes without re-exporting or modifying the PDF.
3. Recalculate SHA-256 after upload or download and compare it with this register.
4. Record the repository path, Git commit, and verification result.
5. Keep derivative translations or working copies separate from the original source files.

## 8. Limitations and Open Items

- This baseline covers the five PDF files supplied in the project conversation, not every possible source in prior conversations, external storage, or the GitHub repository.
- The formal issue dates for FND-001, FND-002, FND-003, and FND-005 were not established from the inspected title/control sections unless explicitly stated above.
- The source document named “ERX-ATLAS-001 v1” internally identifies itself as v1.1; this discrepancy is recorded, not silently corrected.
- The technical response lacks a formal identifier and version in the supplied content.
- ERX-CONSENSUS-001 v0.1 and ERX-IMPL-PROPOSAL-001 remain unverified.
- This inventory does not assess whether the sources are mutually consistent or establish authority precedence.

## 9. WP-0.2 Baseline Status

**IN_PROGRESS**

Completed in this baseline:
- Five supplied original PDF sources identified and opened.
- Internal identifiers and versions recorded where stated.
- Supplied filenames preserved.
- Documentary nature classified provisionally.
- Page counts and SHA-256 checksums recorded.
- Explicit references and missing/unverified sources recorded.

Still pending:
- Search the repository and other authorized project source locations for additional originals.
- Locate and inspect ERX-CONSENSUS-001 and ERX-IMPL-PROPOSAL-001.
- Archive exact original PDFs in the repository and verify post-commit hashes.
- Complete the provenance and source-location fields.
- Submit the completed WP-0.2 package for LAEV review and approval.

**This register is a working inventory baseline, not an approved final register and not a Phase 0 closure record.**

---
End of ERX-FOUNDATIONAL-MATERIAL-REGISTER-001
