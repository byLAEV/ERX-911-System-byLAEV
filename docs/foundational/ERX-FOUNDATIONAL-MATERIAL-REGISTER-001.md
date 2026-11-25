# ERX-FOUNDATIONAL-MATERIAL-REGISTER-001
## Foundational Source Inventory — Phase 0 / WP-0.2

| Field | Value |
|---|---|
| Project | ERX byLAEV — 911 Double-Spend System |
| Register ID | ERX-FOUNDATIONAL-MATERIAL-REGISTER-001 |
| Version | 0.3.0 |
| Status | WP-0.2 BASELINE APPROVED BY LAEV — SUPPLEMENTAL DISCOVERIES TRACKED SEPARATELY |
| Work Package | WP-0.2 |
| Prepared by | LAEV / byLAEV project documentation |
| Inventory basis | Five original PDF files supplied in the project conversation |
| Inventory date | 2026-11-23 |

## 1. Purpose

This register records the foundational ERX source files that were directly available for inspection during WP-0.2. It distinguishes source identity, the document's internal identifier and version, the supplied filename, documentary nature, provenance, integrity evidence, and unresolved matters.

This register records the five-file WP-0.2 baseline accepted by LAEV on 2026-11-23. Later-discovered repository sources are recorded in separate supplemental evidence notes and do not silently rewrite the accepted baseline. WP-0.2 approval does not declare Phase 0 complete.

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

**Repository archival is verified in `docs/`.** On 2026-11-23, all five exact original PDF files were located on the repository `main` branch under `docs/`. Their local SHA-256 values matched the registered checksums, and each locally calculated Git blob SHA-1 matched the GitHub blob SHA returned for the corresponding repository object. The archival paths and integrity evidence are consolidated in `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`. The original supplied filenames are preserved.

The archival procedure has been executed for the five listed originals. Their exact repository paths and byte-identity evidence are recorded in the WP-0.2 completion dossier. Preserve the files unchanged; future replacement or re-upload must repeat the exact-byte and checksum verification steps and record the resulting commit.

## 8. Repository Source Discovery and Custody Verification

The five original PDF files were located on the repository default branch (`main`) under `docs/`, using their exact supplied filenames. Each file was fetched from GitHub in Base64 form and its returned Git blob SHA was recorded. The locally mounted original bytes were independently hashed: SHA-256 matched the inventory, and `git hash-object` matched the corresponding GitHub blob SHA for all five sources. This provides byte-identity evidence between the supplied originals and the repository objects.

At the time of the original five-source WP-0.2 inspection, neither Roadmap reference had been located in the supplied five-file set. Subsequent post-approval repository inspection directly read `docs/Consenso ERX byLAEV` (text; Git Blob SHA-1 `64154f504b0a1ac48f76a438cf60f368e062eab6`), confirming its internal ID ERX-CONSENSUS-001, version 0.1 — Propuesta normativa, status Documento de diseño para revisión, and LAEV/byLAEV authorship. This matches the Roadmap citation and resolves DOC-ISS-002 source identity. Its proposal status and operational completeness remain subject to DOC-ISS-011. `ERX-IMPL-PROPOSAL-001` remains NOT LOCATED / CONTENT AND PROVENANCE UNVERIFIED (DOC-ISS-003). See `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md`.

The archival evidence and paths are consolidated in `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`.

## 9. Limitations and Open Items

- This baseline covers the five PDF files supplied in the project conversation, not every possible source in prior conversations, external storage, or the GitHub repository.
- The formal issue dates for FND-001, FND-002, FND-003, and FND-005 were not established from the inspected title/control sections unless explicitly stated above.
- The source document named “ERX-ATLAS-001 v1” internally identifies itself as v1.1; this discrepancy is recorded, not silently corrected.
- The technical response lacks a formal identifier and version in the supplied content.
- ERX-CONSENSUS-001 v0.1 identity/content is confirmed by the supplemental text source; proposal lifecycle and operational completeness are DOC-ISS-011. ERX-IMPL-PROPOSAL-001 remains not located.
- This inventory does not assess whether the sources are mutually consistent or establish authority precedence.

## 10. WP-0.2 Evidence and Review Status

**WP-0.2 BASELINE APPROVED — LAEV acceptance recorded 2026-11-23.**

Completed in this baseline:
- Five supplied original PDF sources identified and opened.
- Internal identifiers and versions recorded where stated.
- Supplied filenames preserved.
- Documentary nature classified provisionally.
- Page counts and SHA-256 checksums recorded.
- Explicit references and missing/unverified sources recorded.

Still pending:
- DOC-ISS-002 identity verification is evidence-resolved. LAEV disposition of the proposal's authority/status and operational completion remains DOC-ISS-011; this post-approval update does not reopen the accepted five-source inventory.
- Locate or formally disposition ERX-IMPL-PROPOSAL-001 under DOC-ISS-003.
- Formal hierarchy, subject-matter authority and conflict dispositions remain assigned to WP-0.3.
- Supplemental post-approval discovery: text source `docs/Consenso ERX byLAEV` confirms the Roadmap-cited ERX-CONSENSUS-001 v0.1 identity; the PDF counterpart is also present. See `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md` and DOC-ISS-011.
- `ERX-IMPL-PROPOSAL-001` remains not located/unverified.

**This register is the accepted five-source WP-0.2 baseline plus traceable supplemental notes. It is not a Phase 0 closure record.**

---
End of ERX-FOUNDATIONAL-MATERIAL-REGISTER-001
