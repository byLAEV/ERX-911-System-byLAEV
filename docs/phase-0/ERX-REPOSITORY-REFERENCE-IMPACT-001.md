# ERX-REPOSITORY-REFERENCE-IMPACT-001
## Repository-Wide Path and Identifier Impact Analysis — WP-0.5

| Field | Value |
|---|---|
| Document ID | ERX-REPOSITORY-REFERENCE-IMPACT-001 |
| Version | 0.1.0 |
| Status | WORKING EVIDENCE ANNEX — NOT APPROVED |
| Work Package | WP-0.5 |
| Repository | https://github.com/byLAEV/ERX-911-System-byLAEV |
| Scanned branch | main |
| Scanned commit | 739583eb1cc537ca76f69b2dff0b17a7e66d80fb |
| Git tree | 762229e878e97fcca18a7db9fb04160af64b8442 |
| Tree object response | 54 blobs; 4 directories; truncated=false |
| Date | 2026-11-24 UTC−06:00 |
| Authority | LAEV |
| Dependency | ERX-REPOSITORY-ARCHITECTURE-001 and ERX-REPOSITORY-MIGRATION-001 |
| Authorization | No file moves, renames, deletions, or rewrites authorized |

## 1. Purpose and scope

This annex records the repository-wide textual reference scan performed against the exact `main` snapshot above. It identifies Markdown links, relative paths, source identifiers, FND identifiers, ERX document identifiers, CSV references, and links between procedures, registers, historical records, and source materials.

The annex is an impact-control artifact. Its purpose is to prevent references from becoming broken or semantically detached if LAEV later approves a path migration.

No file was moved, renamed, deleted, or rewritten during this scan. All current paths remain the source of truth until a separate approved migration execution.

## 2. Coverage and method

The recursive Git tree returned 54 blobs and four directory objects, with `truncated=false`. All 54 blob paths were accounted for.

The 48 non-PDF files were retrieved from `main` and inspected line by line for:
- Markdown link syntax `[label](target)` and image/link targets.
- HTML `href` and `src` attributes where present.
- Relative path expressions and file references ending in known repository extensions.
- `FND-###` identifiers.
- `ERX-...` document identifiers.
- References to the six source/text-companion pairs.
- CSV rows and path-bearing register fields.
- References in historical procedures, execution records, approval records, and workplans.

The six PDF blobs were inventoried by exact repository path, size, and Git blob SHA-1. The GitHub text-file retrieval interface does not expose the PDFs' internal hyperlink annotations or a decoded PDF text layer for this scan. Therefore, PDF-embedded hyperlinks, URI annotations, and text-only references inside compressed PDF streams are **not yet certified as scanned**. This is the remaining binary-content limitation; it must be closed by a PDF-aware local inspection before the annex can be called fully exhaustive across embedded PDF content.

## 3. Coverage result

| Category | Result |
|---|---|
| Recursive tree | 54/54 blobs accounted for |
| Non-PDF text/CSV files | 48/48 retrieved and scanned |
| PDF files | 6/6 path, size and blob identity inventoried |
| Markdown/relative path references | Scanned across all 48 text/CSV files |
| FND identifiers | Scanned across all 48 text/CSV files |
| ERX identifiers | Scanned across all 48 text/CSV files |
| CSV registers | All four CSV files inspected |
| Historical and procedural records | All repository text records included in the 48-file scan |
| PDF internal annotations/text references | Pending PDF-aware extraction |
| Exact duplicate Git blobs | No duplicate blob SHA identified in tree inventory |

The six PDFs comprise the five original WP-0.2 sources plus the supplemental ERX-CONSENSUS-001 PDF. The supplemental consensus pair remains distinct from the accepted five-source baseline.

## 4. Current source paths and proposed destination paths

The following source-to-destination mapping reproduces the proposed paths in the WP-0.5 migration manifest. These destinations remain proposals only.

| Source identity | Current PDF path | Proposed PDF path | Current text path | Proposed text path |
|---|---|---|---|---|
| FND-001 / ERX-PROT-001 | `docs/ERX byLAEV 1.pdf` | `docs/foundational/originals/ERX byLAEV 1.pdf` | `docs/ERX byLAEV 1.1` | `docs/foundational/derivatives/ERX byLAEV 1.1` |
| FND-002 / ERX-ATLAS-001 | `docs/ERX-ATLAS-001 v1.pdf` | `docs/foundational/originals/ERX-ATLAS-001 v1.pdf` | `docs/ERX-ATLAS-001 v1` | `docs/foundational/derivatives/ERX-ATLAS-001 v1` |
| FND-003 / UTXO-911-001 | `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/foundational/originals/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/UTXO DE COMUNICACIÓN 911 byLAEV` | `docs/foundational/derivatives/UTXO DE COMUNICACIÓN 911 byLAEV` |
| FND-004 / ERX-ROADMAP-001 | `docs/### ERX-ROADMAP-001.pdf` | `docs/foundational/originals/### ERX-ROADMAP-001.pdf` | `docs/### ERX-ROADMAP-001` | `docs/foundational/derivatives/### ERX-ROADMAP-001` |
| FND-005 / Technical Response | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/foundational/originals/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` | `docs/foundational/derivatives/Respuesta técnica a las observaciones de ERX-ROADMAP-001` |
| Supplemental / ERX-CONSENSUS-001 | `docs/Consenso ERX byLAEV.pdf` | `docs/foundational/originals/Consenso ERX byLAEV.pdf` | `docs/Consenso ERX byLAEV` | `docs/foundational/derivatives/Consenso ERX byLAEV` |

No canonical renaming is proposed in this mapping. Original filenames, including spaces, punctuation, accents, and the `###` prefix, are preserved.

## 5. Reference impact register

The following controlled records contain references to current source paths, source identifiers, FND identifiers, source relationships, or proposed archive locations. Each must be included in the migration review. The line references are to the audited `main` snapshot.

| File | Relevant lines / reference class | Required migration treatment |
|---|---|---|
| `WORKPLAN-PHASE-0.md` | 102, 116, 120, 140–145, 167–168, 191–206, 224, 244, 373–379; links to Phase 0 deliverables, five-source register, and work-package status | Update only approved paths; preserve historical references; reconcile WP-0.4/WP-0.5 status discrepancy before release |
| `docs/### ERX-ROADMAP-001` | 55–67, 296–306, 547 onward, 2055–2185; ERX source IDs and proposed future repository tree | Preserve source-internal content; do not rewrite the original source as part of migration |
| `docs/ERX byLAEV 1.1` | Internal ID ERX-PROT-001; no repository path links identified in scanned text | Preserve bytes; update external catalogue only if needed |
| `docs/ERX-ATLAS-001 v1` | Lines 1–7, 2010, 2088–2098; ERX-PROT-001 relationship | Preserve text companion; preserve PDF as graphical source |
| `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` | Lines 1, 6, 24; Roadmap relationship | Preserve source identity and relationship; do not invent ID/version |
| `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md` | Lines 15, 33–49, 55–67, 80–84, 103, 117, 130; five current PDF paths and proposed archive paths | Update procedure's current/destination path table after approval; reconcile its five-source scope with supplemental consensus handling |
| `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md` | Lines 31–35, 65–69, 83–98, 106, 114–124, 141–144; FND-001–FND-005, source IDs, consensus and implementation proposal | Update source paths; preserve original checksums; keep supplemental source separately classified |
| `docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md` | Lines 24–30, 36–43, 47–68, 74–67, 121–143, 154; FND/source relationships and text companion path | Update any changed source paths and retain relationship semantics |
| `docs/foundational/README.md` | Lines 18–19; references foundational register and CSV | Confirm links remain valid; revise if register path changes |
| `docs/phase-0/ERX-CONSENSUS-SOURCE-INSPECTION-001.md` | Lines 12, 27, 33, 84–87, 105; Roadmap and consensus identity | Update consensus source path if moved; preserve proposal status |
| `docs/phase-0/ERX-DOCUMENT-CONTROL-001.md` | Lines 56, 69, 79, 84, 293–296, 301, 314, 320; legacy IDs, filenames, WP-0.4 approval evidence | Preserve original source names/IDs as historical metadata; path references in policy examples must remain accurate |
| `docs/phase-0/ERX-DOCUMENT-GOVERNANCE-001.md` | Lines 41, 50, 53, 56, 64, 69, 72, 75, 80; hierarchy, relationship map, issue register, consensus source | Update path references only; preserve authority and status statements |
| `docs/phase-0/ERX-DOCUMENT-HIERARCHY-MATRIX-001.md` | Lines 22–28, 35, 50, 53; FND-001–FND-005 and REF-001/002 | Preserve source identities and scope classification |
| `docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md` | Lines 17, 20–24, 33–34; source paths and FND/ERX references | Update any explicit paths; preserve issue IDs and dispositions |
| `docs/phase-0/ERX-DOCUMENT-RELATIONSHIP-MAP-001.md` | Lines 30–39, 45–50, 73, 76; document relationships and source paths | Update source path citations; preserve relationship assertions and caveats |
| `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md` | Lines 38–60, 63–87, 93–105, 119–131, 138, 145; IDX-001–IDX-042, current source paths and statuses | Update every path field and link; retain historical IDs and statuses; reconcile duplicate/missing IDX numbers if required by document-control rules |
| `docs/phase-0/ERX-PHASE-0-CHARTER-001.md` | Lines 17, 33–42, 88, 135, 185, 254, 277; foundational document IDs and Roadmap | Preserve source references; update only path-based links if present |
| `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md` | Lines 22–29, 32; consensus PDF/text paths | Update both PDF and text paths; preserve supplemental discovery status |
| `docs/phase-0/ERX-REPOSITORY-GOVERNANCE-001.md` | Lines 11, 24, 26, 49–51; repository identity and target tree | Reconcile target structure with final approved architecture; avoid editing until architecture approval |
| `docs/phase-0/ERX-REQUIREMENTS-METHOD-001.md` | Lines 231–237, 251; foundational filenames and requirements register path | Update source path references and keep source-native titles |
| `docs/phase-0/ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001.md` | Lines 12, 22–33, 39–50, 61; FND and ERX source identifiers | Preserve source authority mapping; path updates only where paths are present |
| `docs/phase-0/ERX-WP-0.2-APPROVAL-RECORD-001.md` | Lines 31–32, 48; source discovery and approval evidence | Historical approval record should normally remain immutable; use an addendum or index update rather than rewriting decision evidence |
| `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md` | Lines 30–42, 48–71, 105; five PDF paths, SHA-256, blob IDs and related register links | Preserve as historical evidence; append a path migration crosswalk rather than changing historical paths |
| `docs/phase-0/ERX-WP-0.2-LAEV-REVIEW-AND-DISPOSITION-001.md` | Lines 22–27, 36, 49; foundational register paths and source metadata | Preserve historical decision form; add crosswalk if path links need updating |
| `docs/phase-0/ERX-WP-0.2-SOURCE-INSPECTION-AND-COMPARISON-001.md` | Lines 23–26, 32, 46–50, 67–88, 120–123; FND sources and source links | Preserve as historical evidence; update only by controlled addendum or migration crosswalk |
| `docs/phase-0/ERX-WP-0.2-SOURCE-SEARCH-AND-DISPOSITION-001.md` | Lines 15–17, 24, 31, 39; Roadmap source identifiers and bounded search | Preserve historical search result and status |
| `docs/phase-0/ERX-WP-0.3-ACCEPTANCE-READINESS-REPORT-001.md` | Lines 13, 33, 35; decision and source references | Preserve historical acceptance evidence |
| `docs/phase-0/ERX-WP-0.3-AUDIT-REPORT-001.md` | Lines 20, 36, 41, 66, 102; source paths, consensus, issue dispositions | Preserve audit evidence; use an addendum if paths are cited as historical |
| `docs/phase-0/ERX-WP-0.3-DELIVERABLE-COMPLETION-MATRIX-001.md` | Lines 17, 21, 23, 24, 42; controlled document references | Preserve evidence; update only controlled links if required |
| `docs/phase-0/ERX-WP-0.3-EXECUTION-RECORD-001.md` | Lines 16–17, 22, 32–43, 46–57; decisions, source documents and consensus source path | Preserve execution history; use a migration crosswalk/addendum |
| `docs/phase-0/ERX-WP-0.3-ISSUE-REVIEW-MATRIX-001.md` | Lines 23–25, 35; consensus source and FND-005 | Preserve historical analysis; path updates via crosswalk |
| `docs/phase-0/ERX-WP-0.3-LAEV-DECISION-PACKAGE-001.md` | Lines 22–32, 45–48, 54, 67–69, 82, 95, 102, 111–121, 139; source relationships and consensus path | Preserve source-backed decision rationale; do not rewrite historical decision text |
| `docs/phase-0/ERX-WP-0.3-LAEV-DECISION-RECORD-001.md` | Lines 23–28, 32, 39, 42, 45, 50, 53; formal dispositions | Immutable historical decision evidence; add migration crosswalk, not silent edits |
| `docs/phase-0/ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001.md` | Lines 10, 12, 21–22, 28, 35, 43–45, 52–53, 71, 77–82, 94, 97; FND IDs and consensus path | Preserve source alignment conclusions; update path citations only through controlled revision/addendum |
| `docs/phase-0/ERX-WP-0.4-APPROVAL-RECORD-001.md` | Lines 20, 32, 36–38, 44; approved document-control policy and evidence records | Historical approval record; preserve exact approved version/hash |
| `docs/phase-0/ERX-WP-0.4-CLOSEOUT-AUDIT-001.md` | Lines 31, 33, 54; approval and review evidence | Preserve closeout evidence; no source path rewrite expected |
| `docs/phase-0/ERX-WP-0.4-EXECUTION-RECORD-001.md` | Lines 12, 17, 20, 27–31; PR, decision record, closeout and document-register paths | Historical execution record; append path crosswalk if needed |
| `docs/phase-0/ERX-WP-0.4-INTERNAL-REVIEW-001.md` | Lines 10, 37; reviewed exact candidate and supporting records | Preserve internal review evidence |
| `docs/phase-0/ERX-WP-0.4-LAEV-DECISION-RECORD-001.md` | Lines 18, 27, 40–43; approved decisions and source metadata | Immutable LAEV decision evidence; preserve |
| `registers/document-issue-register.csv` | Rows DOC-ISS-001–011; source IDs, source paths, affected document identifiers | Update path-bearing cells only if they refer to a moved file; preserve issue IDs and decision content |
| `registers/document-register.csv` | Rows IDX-001–IDX-042; canonical path column for every controlled artifact, source and register | Primary path migration control surface; update every changed path atomically with the Markdown master index |
| `registers/foundational-material-register.csv` | Rows FND-001–FND-005; source filename and source integrity data | Update current path/location field only if schema is extended or path is added; do not alter source SHA-256 |
| `registers/requirements-traceability.csv` | Schema/header only; no substantive requirements or source paths | Confirm no path references; retain unchanged unless future requirements populate it |

### 5.1 Files with no path-bearing source references detected

- `README.md` (repository title only).
- `docs/UTXO DE COMUNICACIÓN 911 byLAEV` (content is a source companion; no repository path/link pattern was detected by the scan).

This finding is limited to the textual patterns scanned; it does not imply that the files are semantically unrelated to other ERX documents.

## 6. Cross-reference hazards and inconsistencies found

### 6.1 Historical evidence versus live links

WP-0.2 approval, completion, source inspection, WP-0.3 decisions, and WP-0.4 approval/closeout documents are historical evidence. Their original paths may be quoted as historical facts. A migration must not silently rewrite the historical record as though the new path had existed at the time.

Required treatment:
1. Keep the historical statement and original path intact where it describes the state at the time.
2. Add a controlled current-path crosswalk or migration addendum.
3. Update active indexes, registers, procedures, and current workplan links to the new path.
4. Preserve old paths in the migration manifest as source paths and the new paths as destinations.

### 6.2 Existing procedure and register drift

The archive procedure `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md` records proposed destinations under `docs/foundational/originals/` for five PDFs. It also references the foundational register and CSV. These are planned locations, not evidence of a completed move. The supplemental consensus pair is handled in other records and must be added to the migration scope without changing the accepted five-source WP-0.2 baseline.

The document register contains status/path metadata that must be reconciled with the final approved architecture and current WP-0.4 evidence before migration. In particular, its WP-0.4 and WP-0.5 records must be checked against the approved WP-0.4 closeout and the actual branch state.

### 6.3 Workplan status inconsistency

In the audited `WORKPLAN-PHASE-0.md`, lines 376–377 label WP-0.4 as `NOT_STARTED — GATE RELEASED` and WP-0.5 as `BLOCKED`. However, `ERX-WP-0.4-APPROVAL-RECORD-001.md`, `ERX-WP-0.4-CLOSEOUT-AUDIT-001.md`, and `ERX-WP-0.4-EXECUTION-RECORD-001.md` state that WP-0.4 was completed/accepted and its policy baseline approved. This is a real synchronization defect in `main`, not a path-only issue. It must be dispositioned and the workplan synchronized under document control before WP-0.5 approval is requested.

### 6.4 Repository migration documents are not in main

At the audited `main` commit, neither `ERX-REPOSITORY-ARCHITECTURE-001.md` nor `ERX-REPOSITORY-MIGRATION-001.md` exists. Both are present on branch `wp-0.5-repository-governance`. Therefore, the branch work products must not be described as already merged into `main`. The annex itself is a branch work product and does not change the audited `main` snapshot.

### 6.5 Source identifiers versus filenames

- FND-001 through FND-005 are catalogue identifiers; they are not filenames.
- ERX-ATLAS-001 internally identifies version 1.1 while its supplied PDF filename retains `v1`.
- FND-005 has no source-native formal document ID/version established by the inspected source.
- ERX-CONSENSUS-001 v0.1 is supplemental and remains a proposal for review.
- ERX-IMPL-PROPOSAL-001 is referenced by the Roadmap but remains NOT LOCATED / UNVERIFIED in the audited repository.
- Extensionless source companions are separate Git blobs; their derivative subtype/provenance remains unverified.

Migration scripts must use exact paths and catalogue IDs from the approved manifest, never derive one from the other.

## 7. Required migration update set

Before any move, the approved migration PR must update or explicitly disposition the following path-bearing/control records:

1. `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md`
2. `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`
3. `docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md`
4. `docs/foundational/README.md`
5. `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md`
6. `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md`
7. `docs/phase-0/ERX-DOCUMENT-RELATIONSHIP-MAP-001.md`
8. `docs/phase-0/ERX-DOCUMENT-HIERARCHY-MATRIX-001.md`
9. `docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md`
10. `docs/phase-0/ERX-DOCUMENT-CONTROL-001.md` where canonical paths or examples require update
11. `WORKPLAN-PHASE-0.md` after resolving the WP-0.4 status mismatch
12. `registers/document-register.csv`
13. `registers/document-issue-register.csv`
14. `registers/foundational-material-register.csv` if a path column is added or existing location is changed
15. `ERX-REPOSITORY-MIGRATION-001.md` itself, with exact path crosswalk and updated hashes after move
16. Any additional file discovered by PDF-aware inspection or by a second scan of the migration PR branch

Historical approval and execution records should normally remain immutable; add a migration crosswalk/addendum instead of rewriting historical evidence.

## 8. Migration execution and rollback requirements

### 8.1 Pre-migration
- Freeze the source commit SHA and record it in the PR.
- Confirm all source and derivative SHA-256 values against exact bytes.
- Confirm no untracked or newly added source files exist after the audited tree snapshot.
- Close PDF-aware internal-link/text inspection.
- Resolve the WP-0.4 workplan status discrepancy.
- Approve the architecture, migration manifest, and this impact annex.
- Generate a complete old-path → new-path map from the approved manifest.

### 8.2 Migration
- Use a dedicated branch and a single controlled migration PR.
- Move files without transforming their bytes.
- Update all active links and path-bearing registers in the same PR.
- Keep historical references as historical, with a crosswalk.
- Do not rename originals or normalize filenames unless separately approved.
- Do not delete either PDF/text companion.

### 8.3 Post-migration verification
- Re-fetch every moved file and calculate SHA-256 from exact bytes.
- Compare each PDF and text companion hash with the pre-migration manifest.
- Verify all old paths are absent only where a move was intended.
- Verify every destination exists exactly once.
- Repeat repository-wide link/path/identifier scans on the PR branch.
- Run link/path validation and CSV parsing.
- Confirm all Markdown links resolve, all relative paths are valid, and no FND/ERX relationship was lost.
- Compare the post-migration Git tree against the expected path map.

### 8.4 Rollback
- Preserve the pre-migration commit SHA as the rollback point.
- If any hash mismatch, missing file, broken reference, or unexpected content change occurs, do not merge.
- Revert the entire migration PR/commit as one unit; do not perform partial ad hoc reversals.
- Re-run the source-path and hash verification against the pre-migration commit.
- Record the failed attempt and corrective action in the execution record.

## 9. Acceptance gates

- [x] Complete recursive Git tree captured; API response not truncated.
- [x] All 54 blob paths accounted for.
- [x] All 48 non-PDF files retrieved and textually scanned.
- [x] All six PDF paths, sizes and blob IDs inventoried.
- [x] Markdown links, relative paths, FND IDs and ERX IDs scanned in all non-PDF files.
- [x] Four CSV registers inspected.
- [x] Historical and procedural references included.
- [x] Five original WP-0.2 PDFs confirmed in the audited tree; supplemental consensus PDF distinguished.
- [x] No file move, rename, deletion or content rewrite performed.
- [ ] PDF internal links and text references inspected with PDF-aware tooling.
- [ ] WP-0.4 workplan status discrepancy resolved in a controlled revision.
- [ ] Architecture, migration manifest and this annex approved by LAEV.
- [ ] Migration PR created and post-migration scan passed.

## 10. Conclusion

The textual reference scan establishes the active repository documents and registers that are affected by the proposed source/derivative reorganization. It also identifies historical records that must be preserved rather than rewritten, and detects a WP-0.4 status inconsistency in the audited `main` workplan.

The scan is complete for the 48 non-PDF files in the audited tree. It is not yet certified as fully exhaustive for embedded PDF annotations or compressed PDF text. That final binary inspection is a mandatory pre-approval gate.

**Control decision:** all original files remain in their current `main` paths; all hashes remain associated with the original byte sequences; no migration is authorized until LAEV expressly approves the architecture, migration manifest, and impact annex.

---
End of ERX-REPOSITORY-REFERENCE-IMPACT-001
