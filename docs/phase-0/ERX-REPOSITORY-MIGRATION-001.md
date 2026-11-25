# ERX-REPOSITORY-MIGRATION-001
## Controlled Repository Migration Manifest — WP-0.5

| Field | Value |
|---|---|
| Document ID | ERX-REPOSITORY-MIGRATION-001 |
| Version | 0.1.0 |
| Status | PREPARATORY MANIFEST — NOT APPROVED; NO FILE MOVES AUTHORIZED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | https://github.com/byLAEV/ERX-911-System-byLAEV |
| Source branch | main |
| Source tree commit | 739583eb1cc537ca76f69b2dff0b17a7e66d80fb |
| Manifest date | 2026-11-24 (UTC−06:00) |
| Architecture dependency | ERX-REPOSITORY-ARCHITECTURE-001 v0.1.0 — pending LAEV approval |
| Authority | LAEV |
| Execution condition | Express approval of architecture, this manifest, and migration PR plan |

## 1. Purpose and authorization boundary

This manifest classifies the six PDF/text companion pairs currently located in `docs/`: the five original WP-0.2 baseline sources and the supplemental ERX-CONSENSUS-001 source. It records proposed destinations, document identity, documentary nature, available integrity identifiers, and migration controls.

**This is a preparatory manifest only. No file move, rename, deletion, content replacement, or path change is authorized by this document.** All proposed destination paths are conditional on LAEV approving ERX-REPOSITORY-ARCHITECTURE-001 and this manifest.

## 2. Classification principles

1. PDF files are preserved as source/original binaries. Their byte identity is established by the SHA-256 values in the approved foundational register for FND-001 through FND-005, plus the source identity of the supplemental consensus PDF.
2. Extensionless companions are treated as text renditions/derivatives associated with the PDFs because they are separate Git blobs containing readable text. The repository does not currently record the extraction tool, extraction date, transformation procedure, or a signed provenance statement for each companion. Therefore, the more specific subtype (OCR, PDF text extraction, source-native text, or manually transcribed text) remains NOT VERIFIED.
3. A related PDF and text rendition are not duplicates merely because their content is similar. They have different roles and distinct Git blob identities.
4. Original filenames and document-internal identifiers are separate data and must not be conflated.
5. No document identifier, version, date, authorship, or legal status may be invented where the source/register says “not stated” or “unverified”.
6. Git blob SHA-1 values below identify the exact objects in the audited Git tree. They are not represented as SHA-256 checksums. SHA-256 values for derivatives and the supplemental consensus PDF remain to be calculated and registered before migration.

## 3. Individual source and derivative classification

### Pair 1 — ERX-PROT-001

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/ERX byLAEV 1.pdf` | `docs/ERX byLAEV 1.1` |
| Proposed destination | `docs/foundational/originals/ERX byLAEV 1.pdf` | `docs/foundational/derivatives/ERX byLAEV 1.1` |
| Document ID | ERX-PROT-001 / FND-001 | ERX-PROT-001 / FND-001 (associated rendition) |
| Internal version | 1.1 | Content indicates ERX-PROT-001 v1.1; rendition version not independently controlled |
| Nature | Original supplied institutional protocol specification; normative/functional source | Readable text companion; derivative subtype and provenance NOT VERIFIED |
| Git blob SHA-1 | `59590bff8a6139e6d4900ce471f2955ca5fda463` | `23dd2774c44ec2c686c6dd37b36986b2d0715360` |
| Size | 337,697 bytes | 38,619 bytes |
| SHA-256 | `5e1647c30f1aae77726619272c7730306b2e7c138e920cf8be91542e1ee77fbd` | NOT CALCULATED |
| References affected | Foundational register FND-001; source cross-reference map; master document index; README/workplan links if any | Same references, plus links that explicitly target the extensionless companion |

Classification: retain the PDF as the source authority; retain the text companion as a non-authoritative access/analysis rendition unless LAEV establishes another status. Do not treat the text rendition as a separately approved protocol version.

### Pair 2 — ERX-ATLAS-001

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/ERX-ATLAS-001 v1.pdf` | `docs/ERX-ATLAS-001 v1` |
| Proposed destination | `docs/foundational/originals/ERX-ATLAS-001 v1.pdf` | `docs/foundational/derivatives/ERX-ATLAS-001 v1` |
| Document ID | ERX-ATLAS-001 / FND-002 | ERX-ATLAS-001 / FND-002 (associated rendition) |
| Internal version | 1.1 (filename retains supplied “v1”) | Content indicates Atlas v1.1; rendition version not independently controlled |
| Nature | Original supplied graphical/operational atlas | Readable text companion; does not preserve the full graphical function of the Atlas; derivative subtype/provenance NOT VERIFIED |
| Git blob SHA-1 | `6f7436779457994ec8d786df9aeb051a52110bd3` | `334890b2a861d9911a72d6aaf90f5179acaac5eb` |
| Size | 321,960 bytes | 44,217 bytes |
| SHA-256 | `7029d5f5cabeedd783eb5fec6cf66ddafa7e224c16ef7644656e89dd7921ec7f` | NOT CALCULATED |
| References affected | Foundational register FND-002; cross-reference map; master index; references to Atlas plates/diagrams | Same references plus direct links to the text companion |

Classification: the PDF remains the authoritative graphical source. The text companion cannot replace diagrams, plates, or graphical details. Retain both and explicitly label the text companion as derivative/non-authoritative.

### Pair 3 — UTXO-911-001

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/UTXO DE COMUNICACIÓN 911 byLAEV` |
| Proposed destination | `docs/foundational/originals/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/foundational/derivatives/UTXO DE COMUNICACIÓN 911 byLAEV` |
| Document ID | UTXO-911-001 / FND-003 | UTXO-911-001 / FND-003 (associated rendition) |
| Internal version | 1.0 | Content indicates UTXO-911-001 v1.0; rendition version not independently controlled |
| Nature | Original supplied conceptual and functional specification of the three-stage 911 communication UTXO cycle | Readable text companion; derivative subtype/provenance NOT VERIFIED |
| Git blob SHA-1 | `23126dd32795fc0d5fb46038faa91c3c04efef8a` | `6f911a6754645f287ae6b6c1816c7e53f3fa2a73` |
| Size | 171,221 bytes | 18,837 bytes |
| SHA-256 | `39fa464f8ec774bf55f50e7d042c19728e2467be2bbb7234b15142a89321c4cc` | NOT CALCULATED |
| References affected | Foundational register FND-003; cross-reference map; master index; UTXO cycle references in normative/architecture material | Same references plus direct links to text companion |

Classification: the PDF is the original supplied source. The text companion is a readable rendition; do not promote it to a new normative revision.

### Pair 4 — ERX-ROADMAP-001

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/### ERX-ROADMAP-001.pdf` | `docs/### ERX-ROADMAP-001` |
| Proposed destination | `docs/foundational/originals/### ERX-ROADMAP-001.pdf` | `docs/foundational/derivatives/### ERX-ROADMAP-001` |
| Document ID | ERX-ROADMAP-001 / FND-004 | ERX-ROADMAP-001 / FND-004 (associated rendition) |
| Internal version | 1.0 | Content indicates Roadmap v1.0; rendition version not independently controlled |
| Nature | Original supplied master development plan | Readable text companion; derivative subtype/provenance NOT VERIFIED |
| Git blob SHA-1 | `042c89922acfc9d86181c3626f486871156f24f4` | `5668a1acff4864d1f4723f0d5a6b9d0f8f9d775f` |
| Size | 393,901 bytes | 45,838 bytes |
| SHA-256 | `b529fb306c19704bd163ed3a26f9d9b737057415a6d5839056f394791fdadca3` | NOT CALCULATED |
| References affected | Foundational register FND-004; cross-reference map; master index; Phase 0 workplan and roadmap citations | Same references plus direct links to text companion |

Classification: retain the PDF as original source. The text rendition is a reading/search aid and cannot silently replace the controlled PDF.

### Pair 5 — Technical Response to ERX-ROADMAP-001

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` |
| Proposed destination | `docs/foundational/originals/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/foundational/derivatives/Respuesta técnica a las observaciones de ERX-ROADMAP-001` |
| Document ID | FND-005; formal ID not stated in source | FND-005 associated rendition; no formal ID stated |
| Internal version | Not stated | Not stated |
| Nature | Original supplied two-page technical response; signed LAEV/byLAEV according to WP-0.2 register | Readable text companion; derivative subtype/provenance NOT VERIFIED |
| Git blob SHA-1 | `d044bdbe3a331e96846a768124f5e6e69134fa0e` | `8bc0ca82d1ffedf178eec562a6e7e1d44344dba5` |
| Size | 63,749 bytes | 3,443 bytes |
| SHA-256 | `1b8bd77ac2b7789269d6152d172fbb301d3609fc2db223aa1e4b8ed35884fba9` | NOT CALCULATED |
| References affected | Foundational register FND-005; cross-reference map; master index; Roadmap response references | Same references plus direct links to text companion |

Classification: do not invent a formal document identifier or version. Retain the PDF as the original signed source; retain text as derivative.

### Pair 6 — ERX-CONSENSUS-001 (supplemental source)

| Field | PDF source | Text companion |
|---|---|---|
| Current path | `docs/Consenso ERX byLAEV.pdf` | `docs/Consenso ERX byLAEV` |
| Proposed destination | `docs/foundational/originals/Consenso ERX byLAEV.pdf` | `docs/foundational/derivatives/Consenso ERX byLAEV` |
| Document ID | ERX-CONSENSUS-001 (supplemental discovery) | ERX-CONSENSUS-001 (associated rendition) |
| Internal version | 0.1 — Propuesta normativa | Content indicates ERX-CONSENSUS-001 v0.1; rendition version not independently controlled |
| Nature | Supplemental consensus framework proposal; status “Documento de diseño para revisión”; LAEV/byLAEV authorship shown in the text source, PDF identity must be cross-checked against its internal cover/control fields | Readable text companion; derivative subtype/provenance NOT VERIFIED |
| Git blob SHA-1 | `c2f965c9bf455506571ac4c1635b4fb47af34216` | `64154f504b0a1ac48f76a438cf60f368e062eab6` |
| Size | 157,848 bytes | 15,237 bytes |
| SHA-256 | NOT CALCULATED | NOT CALCULATED |
| References affected | Supplemental source discovery record; Roadmap references; master document index; issue DOC-ISS-011 and relevant consensus references | Same references plus direct links to text companion |

Classification: supplemental source, not part of the original five-file WP-0.2 baseline. Its existence and text identity are verified in the repository. The proposal's review status and operational completeness remain as recorded in the post-approval source-discovery record; this manifest does not approve the proposal or elevate it to normative authority.

## 4. Proposed path mapping summary

| Current path | Proposed destination | Classification | Move authorized? |
|---|---|---|---|
| `docs/ERX byLAEV 1.pdf` | `docs/foundational/originals/ERX byLAEV 1.pdf` | Original PDF FND-001 | NO |
| `docs/ERX byLAEV 1.1` | `docs/foundational/derivatives/ERX byLAEV 1.1` | Text companion FND-001 | NO |
| `docs/ERX-ATLAS-001 v1.pdf` | `docs/foundational/originals/ERX-ATLAS-001 v1.pdf` | Original PDF FND-002 | NO |
| `docs/ERX-ATLAS-001 v1` | `docs/foundational/derivatives/ERX-ATLAS-001 v1` | Text companion FND-002 | NO |
| `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/foundational/originals/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | Original PDF FND-003 | NO |
| `docs/UTXO DE COMUNICACIÓN 911 byLAEV` | `docs/foundational/derivatives/UTXO DE COMUNICACIÓN 911 byLAEV` | Text companion FND-003 | NO |
| `docs/### ERX-ROADMAP-001.pdf` | `docs/foundational/originals/### ERX-ROADMAP-001.pdf` | Original PDF FND-004 | NO |
| `docs/### ERX-ROADMAP-001` | `docs/foundational/derivatives/### ERX-ROADMAP-001` | Text companion FND-004 | NO |
| `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/foundational/originals/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | Original PDF FND-005 | NO |
| `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` | `docs/foundational/derivatives/Respuesta técnica a las observaciones de ERX-ROADMAP-001` | Text companion FND-005 | NO |
| `docs/Consenso ERX byLAEV.pdf` | `docs/foundational/originals/Consenso ERX byLAEV.pdf` | Supplemental PDF ERX-CONSENSUS-001 | NO |
| `docs/Consenso ERX byLAEV` | `docs/foundational/derivatives/Consenso ERX byLAEV` | Supplemental text companion | NO |

No other existing file is in scope for this six-pair migration. Existing governance documents, Phase 0 records, registers, README and workplan remain in their current locations unless a separately approved manifest amendment is issued.

## 5. Reference impact and path dependency scan

The following controlled artifacts are known to refer to one or more of the six source documents or their present paths:
- `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`
- `docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md`
- `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md`
- `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md`
- `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md`
- `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`
- `registers/foundational-material-register.csv`
- `README.md` and `WORKPLAN-PHASE-0.md`, where direct links or path references may exist.

This is the initial known-reference list, not yet a completed exhaustive link scan. Before migration, search the entire repository for each current path, filename, document ID, and Markdown link target. Record every hit and update all affected references atomically in the migration PR. If a reference is intentionally retained as a historical path, document that exception.

## 6. Integrity requirements before and after migration

For every one of the twelve files:
1. Calculate and record SHA-256 from the exact source bytes before migration.
2. Record current Git blob SHA-1, byte size, and source commit.
3. Confirm the source bytes are readable and the PDF/text classification remains correct.
4. Move the file without modifying its bytes.
5. Calculate SHA-256 from the destination bytes and compare with the pre-migration value.
6. Confirm the destination Git blob object matches the source Git blob SHA-1 when the content is unchanged.
7. Update the foundational material register and any relevant supplemental source record with the approved destination path.
8. Verify all links and cross-reference targets after the migration commit.

The five baseline PDF SHA-256 values are recorded in Section 3 and the approved WP-0.2 register. SHA-256 for all five text companions and both supplemental consensus files has now been calculated from the exact GitHub file bytes in base64 mode and independently validated by recomputing one baseline PDF hash against the registered SHA-256. See Appendix A. A Git blob SHA-1 is not a substitute for this SHA-256 requirement.

## 7. Controlled migration procedure

### 7.1 Preconditions
- LAEV approves ERX-REPOSITORY-ARCHITECTURE-001.
- LAEV approves this manifest and all twelve source-to-destination mappings.
- All derivative subtypes are either verified or explicitly accepted as “text companion — provenance not verified”.
- SHA-256 is recorded for all twelve files.
- The complete reference/path scan is attached to the PR.
- A migration branch is created from the then-current `main`.
- The migration branch starts from a clean and recorded base commit.

### 7.2 Execution
1. Create `docs/foundational/originals/` and `docs/foundational/derivatives/` only within the approved migration branch.
2. Move the twelve files to the exact destinations in Section 4 using Git-aware moves where practical; do not alter content.
3. Update all links, registers, source maps, index entries, completion dossier, source-discovery record, README and workplan references identified by the path scan.
4. Do not rewrite document contents, titles, versions, or normative status as part of a path-only migration.
5. Run link/path validation and a complete tree inventory.
6. Recalculate and compare SHA-256 and Git blob identities.
7. Produce a migration evidence report listing every old path, new path, before/after hashes, and updated reference.
8. Open a PR containing only the approved path migration and reference updates.

### 7.3 Review and merge
- LAEV reviews the migration evidence and confirms no source bytes changed.
- Any unplanned file, content, or status change blocks acceptance.
- Merge only after explicit approval and all required checks pass.
- Update this manifest to record actual commit and final paths after merge.

## 8. Rollback procedure

Rollback is required if any file is missing, any SHA-256 differs, a link/reference breaks, a source is misclassified, or an unapproved content change occurs.

1. Stop the migration; do not continue partial moves.
2. Preserve the migration branch and failed CI/log evidence for audit.
3. If the migration PR has not merged, close/revert the migration branch and retain `main` unchanged.
4. If the migration PR has merged, prepare a dedicated revert commit or PR that restores all twelve original paths and all pre-migration references from the recorded base commit. Do not force-push or rewrite shared history.
5. Verify restored SHA-256 and Git blob identities against the pre-migration manifest.
6. Re-run the complete path/reference scan.
7. Record the rollback event, reason, commit, evidence, and corrective action in this manifest and the WP-0.5 execution record.
8. A new migration attempt requires a corrected manifest revision and fresh LAEV approval.

## 9. Acceptance criteria for the manifest

- [x] Six PDF/text pairs individually classified at a preliminary documentary level.
- [x] Five baseline PDF SHA-256 values transcribed from the approved WP-0.2 register.
- [x] Git blob SHA-1 and byte size recorded for all twelve current objects.
- [x] Proposed destination path recorded for every source and companion.
- [x] Supplemental consensus source kept distinct from the original five-file baseline.
- [x] No unstated document IDs or versions invented.
- [x] SHA-256 calculated for five text companions and two supplemental consensus files.
- [ ] Derivative provenance/subtype verified or explicitly accepted as unknown.
- [ ] Exhaustive repository-wide path/reference scan attached (targeted scan of principal control records completed; broader scan remains).
- [ ] Architecture ERX-REPOSITORY-ARCHITECTURE-001 approved by LAEV.
- [ ] This manifest approved by LAEV.
- [ ] Migration branch and rollback point recorded.
- [ ] Migration PR reviewed and accepted.

## 10. Current disposition

**PREPARATORY MANIFEST COMPLETE FOR REVIEW; NOT APPROVED. NO FILE MOVES AUTHORIZED.**

The current paths remain authoritative until the architecture and this manifest are both expressly approved by LAEV. The next action is to finish the repository-wide reference scan and confirm the derivative-provenance disposition, then submit the architecture and manifest for approval. Only after both approvals may a migration PR be executed.


## Appendix A — Calculated SHA-256 values for text companions and supplemental consensus

Calculation basis: exact file bytes fetched from the `main` branch using GitHub's base64 content representation and decoded without text normalization. Byte counts and Git blob SHA-1 values match the audited tree. The SHA-256 implementation was validated by hashing `docs/ERX byLAEV 1.pdf` and reproducing the registered value `5e1647c30f1aae77726619272c7730306b2e7c138e920cf8be91542e1ee77fbd` exactly.

| File | Bytes | Git blob SHA-1 | SHA-256 |
|---|---:|---|---|
| `docs/ERX byLAEV 1.1` | 38,619 | `23dd2774c44ec2c686c6dd37b36986b2d0715360` | `1570122c6d41c6a47f18360344cd8f2adf0c4b9805e9994048cf5c286974e43b` |
| `docs/ERX-ATLAS-001 v1` | 44,217 | `334890b2a861d9911a72d6aaf90f5179acaac5eb` | `85c63f75fd876b6e0619640d4a3da720d43a23a5f0bf00ca9550d2caf53893f7` |
| `docs/UTXO DE COMUNICACIÓN 911 byLAEV` | 18,837 | `6f911a6754645f287ae6b6c1816c7e53f3fa2a73` | `0c38f24fab18cd7d66234f1f327dfb874088c4692fb0f2508a0d9b30348d1c6f` |
| `docs/### ERX-ROADMAP-001` | 45,838 | `5668a1acff4864d1f4723f0d5a6b9d0f8f9d775f` | `33c40308cd34c4945db91ccc58fcadf4d0b1d3d26e8c88f1bb0d9af29302d123` |
| `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` | 3,443 | `8bc0ca82d1ffedf178eec562a6e7e1d44344dba5` | `1473604c643af4e750da45d30a223c91cdc5d46a3524821b3fd02d2e2e208bd4` |
| `docs/Consenso ERX byLAEV` | 15,237 | `64154f504b0a1ac48f76a438cf60f368e062eab6` | `7f7f647c44fe246e96c8532d45aa110907a6bca12a0293cea39cbdbe7c69a930` |
| `docs/Consenso ERX byLAEV.pdf` | 157,848 | `c2f965c9bf455506571ac4c1635b4fb47af34216` | `afcc2708c02d98fdb486ab0a667cbed37b3bb1429a0c6a7563a9af334a1d89fc` |

## Appendix B — Text-companion content inspection and provenance disposition

Direct inspection of the opening/control content of all six text companions confirms they contain readable, structured text corresponding to their associated document topics and, where declared, document IDs and versions. This supports classifying them as text companions/readable renditions. It does **not** establish whether they were produced by OCR, PDF text extraction, manual transcription, or exported from a source-native document. No extraction log, tool name, generation date, or signed provenance record was found in the inspected content.

Accordingly:
- Classification: `TEXT_COMPANION — DERIVATIVE SUBTYPE NOT VERIFIED`.
- Authority: non-authoritative for migration planning unless an existing approved governance record states otherwise.
- Retention: preserve exact bytes and original current path until migration approval.
- Required follow-up: LAEV may accept the subtype as unknown for archival purposes, or request a provenance investigation before approving migration.
- The Atlas text companion is explicitly not a replacement for the PDF's graphical plates and diagrams.

The supplemental consensus text directly declares:
- Identifier: `ERX-CONSENSUS-001`.
- Version: `0.1 — Propuesta normativa`.
- Status: `Documento de diseño para revisión`.
- Authorship: `LAEV / byLAEV`.

The consensus PDF counterpart is present in the same repository directory and its bytes have now been hashed. The PDF's full internal metadata/control-page equivalence to the text companion has not been separately established by a page-by-page comparison. The pair remains supplemental and does not modify the accepted five-source WP-0.2 baseline.

## Appendix C — Targeted reference trace completed

The following principal controlled records were directly inspected on `main` and contain references to the source IDs, filenames, or source relationships:

| Controlled record | Confirmed trace |
|---|---|
| `WORKPLAN-PHASE-0.md` | Five-PDF WP-0.2 baseline, supplemental consensus source, acceptance record, and source-status caveats |
| `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md` | FND-001–FND-005, filenames, SHA-256, source relations, supplemental consensus discovery |
| `docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md` | Source filenames/IDs, document relationships and consensus status |
| `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md` | Proposed destination paths for five original PDFs and verification instructions |
| `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md` | Current source paths, source identities, statuses and relationships |
| `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md` | Supplemental consensus text/PDF paths and discovery evidence |
| `registers/foundational-material-register.csv` | Five baseline source rows, identifiers, current filenames, registered SHA-256 values and archive status |

This is a **targeted trace of the principal controlled records**, not yet a claim of exhaustive search across every repository file. A full-repository path/reference scan remains a pre-migration gate. The archive procedure already contains proposed future PDF paths; these are planned destinations, not evidence that files have moved. The migration must reconcile and update that procedure together with the register, cross-reference map, master index, discovery record, workplan, CSV register, and any additional references found in the exhaustive scan.

## Appendix D — Updated readiness

- [x] SHA-256 recorded for all twelve source/companion files (five baseline PDF hashes from accepted register; five text companions and two consensus files calculated in Appendix A).
- [x] Hash calculation cross-checked against one known baseline PDF SHA-256.
- [x] Readable text content inspected for all six companions.
- [x] Companion subtype honestly bounded as unverified provenance.
- [x] Principal controlled-record references traced.
- [ ] Exhaustive full-repository path/reference scan.
- [ ] Decide whether LAEV accepts unknown derivative provenance or requires further investigation.
- [ ] LAEV approval of architecture and manifest.
- [ ] Migration execution, still prohibited until all gates pass.


---

End of ERX-REPOSITORY-MIGRATION-001
