# ERX-REPOSITORY-ARCHITECTURE-001
## Repository Tree Audit and Target Architecture — Phase 0 / WP-0.5

| Field | Value |
|---|---|
| Document ID | ERX-REPOSITORY-ARCHITECTURE-001 |
| Version | 0.1.0 |
| Status | WORKING DRAFT — AUDIT BASELINE RECORDED; NOT APPROVED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | https://github.com/byLAEV/ERX-911-System-byLAEV |
| Design and approval authority | LAEV |
| Audit date | 2026-11-24 (UTC−06:00) |
| Audited ref | main |
| Audited commit | 739583eb1cc537ca76f69b2dff0b17a7e66d80fb |
| Tree object | 762229e878e97fcca18a7db9fb04160af64b8442 |
| Dependencies | WP-0.3 and WP-0.4 recorded as accepted in Phase 0 workplan |
| Scope boundary | Inventory and target architecture only; no file moves or renames authorized |

## 1. Purpose

This document records the complete Git tree observed on the default branch `main` and proposes a controlled target architecture for repository organization. It is an evidence-based WP-0.5 design artifact.

The audit is a snapshot of the audited commit, not a claim that no subsequent commit has occurred. No file was moved, renamed, deleted, rewritten, or reclassified as part of this audit. This document does not approve branch protection, access policy, intellectual-property terms, a license, or implementation of the target tree.

## 2. Audit method and limits

1. Retrieved the Git tree for `main` recursively from GitHub Git Data API.
2. Confirmed `truncated=false`; the API returned the complete tree.
3. Enumerated every blob and tree object and recorded paths, sizes, and blob SHAs.
4. Retrieved repository metadata, branch listing, and repository rulesets.
5. Compared the five WP-0.2 original PDF files in the mounted project files against their Git blob identities using `git hash-object`.
6. Compared current layout to the proposed directory responsibilities in ERX-REPOSITORY-GOVERNANCE-001.

Limitations:
- This is a Git tree audit, not a full source-code, security, semantic-content, or legal audit.
- Repository rulesets endpoint returned an empty list. This does not alone prove every possible classic branch-protection setting is absent; the branch API explicitly reports `protected=false` for all listed branches.
- Collaborator roster, organization-level policy, backup/restore capability, and all permission assignments were not established by this tree inspection.
- Git blob SHA-1 is used here as an object identity cross-check, not as a substitute for the SHA-256 source-integrity digest in the foundational register.

## 3. Snapshot summary

| Measure | Observed |
|---|---:|
| Files (blob objects) | 54 |
| Directories (tree objects, excluding implicit root) | 4 |
| Tree response truncated | No |
| File extensions | 38 .md; 6 .pdf; 4 .csv; 5 extensionless; 1 extension `.1` |
| Audited default branch | `main` |
| Audited commit | `739583eb1cc537ca76f69b2dff0b17a7e66d80fb` |

Observed directories:
- `docs/`
- `docs/foundational/`
- `docs/phase-0/`
- `registers/`

No `src/`, `tests/`, `schemas/`, `simulator/`, `deployment/`, `templates/`, or `.github/` directory was present in the audited tree. Their absence is not a defect by itself; implementation artifacts must only be introduced when authorized by the applicable phase.

## 4. Complete current file inventory

All paths below were returned by the non-truncated recursive Git tree at the audited commit.

### Root (2 files)
- `README.md`
- `WORKPLAN-PHASE-0.md`

### docs/ (12 files)
- `docs/### ERX-ROADMAP-001`
- `docs/### ERX-ROADMAP-001.pdf`
- `docs/Consenso ERX byLAEV`
- `docs/Consenso ERX byLAEV.pdf`
- `docs/ERX byLAEV 1.1`
- `docs/ERX byLAEV 1.pdf`
- `docs/ERX-ATLAS-001 v1`
- `docs/ERX-ATLAS-001 v1.pdf`
- `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001`
- `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf`
- `docs/UTXO DE COMUNICACIÓN 911 byLAEV`
- `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf`

### docs/foundational/ (4 files)
- `docs/foundational/ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md`
- `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`
- `docs/foundational/ERX-SOURCE-CROSS-REFERENCE-MAP-001.md`
- `docs/foundational/README.md`

### docs/phase-0/ (32 files)
- `docs/phase-0/ERX-CONSENSUS-SOURCE-INSPECTION-001.md`
- `docs/phase-0/ERX-CONTRADICTION-AND-AMBIGUITY-HANDLING-001.md`
- `docs/phase-0/ERX-DOCUMENT-CONTROL-001.md`
- `docs/phase-0/ERX-DOCUMENT-EVOLUTION-AND-SUPERSESSION-001.md`
- `docs/phase-0/ERX-DOCUMENT-GOVERNANCE-001.md`
- `docs/phase-0/ERX-DOCUMENT-HIERARCHY-MATRIX-001.md`
- `docs/phase-0/ERX-DOCUMENT-ISSUE-REGISTER-001.md`
- `docs/phase-0/ERX-DOCUMENT-RELATIONSHIP-MAP-001.md`
- `docs/phase-0/ERX-MASTER-DOCUMENT-INDEX-001.md`
- `docs/phase-0/ERX-PHASE-0-CHARTER-001.md`
- `docs/phase-0/ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md`
- `docs/phase-0/ERX-REPOSITORY-GOVERNANCE-001.md`
- `docs/phase-0/ERX-REQUIREMENTS-METHOD-001.md`
- `docs/phase-0/ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001.md`
- `docs/phase-0/ERX-WP-0.2-APPROVAL-RECORD-001.md`
- `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`
- `docs/phase-0/ERX-WP-0.2-LAEV-REVIEW-AND-DISPOSITION-001.md`
- `docs/phase-0/ERX-WP-0.2-SOURCE-INSPECTION-AND-COMPARISON-001.md`
- `docs/phase-0/ERX-WP-0.2-SOURCE-SEARCH-AND-DISPOSITION-001.md`
- `docs/phase-0/ERX-WP-0.3-ACCEPTANCE-READINESS-REPORT-001.md`
- `docs/phase-0/ERX-WP-0.3-AUDIT-REPORT-001.md`
- `docs/phase-0/ERX-WP-0.3-DELIVERABLE-COMPLETION-MATRIX-001.md`
- `docs/phase-0/ERX-WP-0.3-EXECUTION-RECORD-001.md`
- `docs/phase-0/ERX-WP-0.3-ISSUE-REVIEW-MATRIX-001.md`
- `docs/phase-0/ERX-WP-0.3-LAEV-DECISION-PACKAGE-001.md`
- `docs/phase-0/ERX-WP-0.3-LAEV-DECISION-RECORD-001.md`
- `docs/phase-0/ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001.md`
- `docs/phase-0/ERX-WP-0.4-APPROVAL-RECORD-001.md`
- `docs/phase-0/ERX-WP-0.4-CLOSEOUT-AUDIT-001.md`
- `docs/phase-0/ERX-WP-0.4-EXECUTION-RECORD-001.md`
- `docs/phase-0/ERX-WP-0.4-INTERNAL-REVIEW-001.md`
- `docs/phase-0/ERX-WP-0.4-LAEV-DECISION-RECORD-001.md`

### registers/ (4 files)
- `registers/document-issue-register.csv`
- `registers/document-register.csv`
- `registers/foundational-material-register.csv`
- `registers/requirements-traceability.csv`

## 5. Foundational PDF preservation verification

The five original WP-0.2 PDF files were found in `docs/` on `main`. Their local Git blob identities were independently recomputed from the mounted original PDFs and match the GitHub tree blob SHA values.

| Original supplied file | Repository path | Git blob SHA-1 | Result |
|---|---|---|---|
| `ERX byLAEV 1.pdf` | `docs/ERX byLAEV 1.pdf` | `59590bff8a6139e6d4900ce471f2955ca5fda463` | MATCH |
| `ERX-ATLAS-001 v1.pdf` | `docs/ERX-ATLAS-001 v1.pdf` | `6f7436779457994ec8d786df9aeb051a52110bd3` | MATCH |
| `UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `23126dd32795fc0d5fb46038faa91c3c04efef8a` | MATCH |
| `### ERX-ROADMAP-001.pdf` | `docs/### ERX-ROADMAP-001.pdf` | `042c89922acfc9d86181c3626f486871156f24f4` | MATCH |
| `Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `d044bdbe3a331e96846a768124f5e6e69134fa0e` | MATCH |

The SHA-256 values in ERX-FOUNDATIONAL-MATERIAL-REGISTER-001 are the controlling source-integrity digests; the corresponding five original files are present and their Git blob identities match the local originals. Therefore, the earlier archival statement in the working draft that the PDFs were absent is stale and must be corrected in the next controlled revision.

A sixth PDF, `docs/Consenso ERX byLAEV.pdf`, also exists in the repository. It is additional to the five-file WP-0.2 baseline and must be classified through the supplemental source-discovery and document-control process; it is not silently added to the original five-source baseline.

## 6. Duplicate and placement analysis

### 6.1 Exact duplicate files

No two files in the enumerated tree share a Git blob SHA in the observed tree data. Therefore, this audit identifies **no exact byte-identical duplicate blobs**.

### 6.2 Related source and text-export pairs

The following pairs share a common base title and appear to be source-PDF plus text/converted companion files:
- `docs/### ERX-ROADMAP-001` and `docs/### ERX-ROADMAP-001.pdf`
- `docs/Consenso ERX byLAEV` and `docs/Consenso ERX byLAEV.pdf`
- `docs/ERX byLAEV 1.1` and `docs/ERX byLAEV 1.pdf`
- `docs/ERX-ATLAS-001 v1` and `docs/ERX-ATLAS-001 v1.pdf`
- `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001` and its PDF
- `docs/UTXO DE COMUNICACIÓN 911 byLAEV` and its PDF

These are not classified as duplicates. The extensionless companions require content-format, provenance, and intended-use inspection before classification as OCR, extracted text, source-native files, or working derivatives. Do not delete either member of a pair.

### 6.3 Placement observations

- The five original foundational PDFs and related source companions are mixed directly in `docs/`, rather than separated into a dedicated originals/source area.
- Phase 0 controlled artifacts are grouped in `docs/phase-0/`; this is a coherent existing boundary and should be retained.
- Foundational registers and cross-reference materials are grouped in `docs/foundational/`; this boundary should be retained.
- Machine-readable registers are grouped in `registers/`; this boundary should be retained.
- `WORKPLAN-PHASE-0.md` remains at root and should remain there as the project-level execution index unless the approved governance decision directs otherwise.
- Repository governance and document control files are currently in `docs/phase-0/`, consistent with their current WP-0.5 / Phase 0 context.
- Several filenames in `docs/` contain spaces, Unicode characters, punctuation, or absent extensions. These names are valid Git paths; do not rename them as part of a bulk normalization without a controlled path-migration table and link/reference update plan.

## 7. Repository configuration snapshot

| Item | Observation | Evidence / limitation |
|---|---|---|
| Default branch | `main` | Repository metadata and branch listing |
| Visibility | Public | Repository metadata |
| Archived | No | Repository metadata |
| Listed branches | `main`, `wp-0.3-controlled-closeout`, `wp-0.4-document-control`, `wp-0.5-repository-governance` | Branch API listing |
| Protected branch flag | false for each listed branch | Branch API |
| Repository rulesets | Empty list | Rulesets API |
| Merge methods | Merge, squash, rebase enabled | Repository metadata |
| Auto-merge | Disabled | Repository metadata |
| Collaborator roster | NOT_VERIFIED | Not audited in this inventory |
| Backup / restore | NOT_VERIFIED | Not audited in this inventory |
| License / rights scope | NOT_DECIDED | No license inferred or proposed as granted |

## 8. Comparison with proposed structure

The prior ERX-REPOSITORY-GOVERNANCE-001 draft proposed:
- `docs/foundational/originals/`
- `docs/phase-0/`
- `docs/requirements/`
- `docs/decisions/`
- `docs/risks/`
- `docs/governance/`
- `docs/reports/`
- `registers/`
- `templates/`
- `.github/`

Observed comparison:
- `docs/foundational/`, `docs/phase-0/`, and `registers/` already exist.
- `docs/foundational/originals/`, `docs/requirements/`, `docs/decisions/`, `docs/risks/`, `docs/governance/`, `docs/reports/`, `templates/`, and `.github/` do not exist in the audited tree.
- The proposed target is broader than the current Phase 0 documentary needs. Empty directories should not be created merely to make the tree look complete.
- Requirements, decisions, risks, reports, templates, and GitHub automation directories should be introduced only when there are approved artifacts or authorized workflows that need them.
- No source-code directory is proposed for immediate creation by this document; software implementation remains subject to the applicable roadmap gate.

## 9. Proposed target architecture (logical, not yet implemented)

The following is the recommended target for the current documentary stage. It preserves current working boundaries and separates immutable source originals from derivative text and controlled project documents.

```text
ERX-911-System-byLAEV/
├── README.md
├── WORKPLAN-PHASE-0.md
├── docs/
│   ├── foundational/
│   │   ├── originals/              # exact original source binaries
│   │   ├── derivatives/            # OCR, extracted text, translations, annotations
│   │   ├── ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md
│   │   ├── ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001.md
│   │   ├── ERX-SOURCE-CROSS-REFERENCE-MAP-001.md
│   │   └── README.md
│   └── phase-0/                    # Phase 0 policies, decisions, reviews and closeouts
├── registers/                      # machine-readable controlled registers
└── .github/                        # only when approved automation/configuration exists
    └── workflows/
```

Potential future directories are conditional, not part of this immediate target:
- `docs/requirements/`: when controlled requirements artifacts are approved/needed.
- `docs/decisions/`: when formal ADRs are introduced under WP-0.8.
- `docs/risks/`: when the risk register structure is authorized under the relevant WP.
- `docs/reports/`: only if reports need a separate classification from their governing WP folder.
- `templates/`: after templates are approved.
- `src/`, `tests/`, `schemas/`, `simulator/`, `deployment/`: only when authorized implementation work begins.

## 10. Migration principles and safety controls

1. No migration until LAEV approves the target architecture and the path mapping.
2. Preserve original PDF bytes and supplied filenames.
3. Move only after a source-to-destination mapping has been recorded.
4. Update all Markdown links, CSV paths, cross-reference maps, and workplan references in the same controlled migration change.
5. Preserve Git history; do not use history rewriting to disguise path changes.
6. Keep original PDFs separate from OCR, extracted text, translated, or annotated derivatives.
7. Do not delete extensionless source companions until their format and provenance are verified and a disposition is approved.
8. Do not create licenses, copyright grants, branch restrictions, or access policy by implication.
9. Verify each migrated file by SHA-256 before and after migration.
10. Produce a migration manifest and rollback plan before the first move.
11. Perform the migration in an isolated branch and use a PR for review/integration.
12. Do not combine migration with content revision or substantive document changes.

## 11. Findings and required dispositions

| ID | Finding | Disposition |
|---|---|---|
| RA-01 | Five original WP-0.2 PDFs are present in `docs/` and blob identities match local originals | Correct stale archival statement in governance draft; retain paths pending approved migration |
| RA-02 | Sixth consensus PDF exists beyond the original five-source baseline | Keep as supplemental source; maintain separate status/disposition |
| RA-03 | Six PDF/text companion pairs exist in `docs/` | Classify each text companion's format/provenance; do not treat as exact duplicates |
| RA-04 | Current directory tree has only foundational, phase-0, registers groupings | Preserve these stable boundaries |
| RA-05 | Several proposed folders do not exist and may not yet be needed | Defer until approved content/workflows require them |
| RA-06 | All listed branches report `protected=false`; rulesets list empty | LAEV decision required on branch protection and PR enforcement |
| RA-07 | Collaborator roster and backup/restore were not established | Verify in dedicated access/recovery audit |
| RA-08 | Filenames in `docs/` have inconsistent extensions and punctuation | Retain for now; create path migration map only after derivative/source classification |
| RA-09 | No exact duplicate Git blobs identified | No deletion justified by duplicate analysis |
| RA-10 | Source code, schemas, tests, simulator and deployment directories absent | No defect; do not pre-create absent implementation layers before their roadmap gates |

## 12. Acceptance criteria for this audit deliverable

- [x] Complete recursive tree retrieved; `truncated=false`.
- [x] All 54 files enumerated.
- [x] All four explicit directories enumerated.
- [x] Five original PDF blob identities compared with the local originals.
- [x] Current structure compared with the prior proposed structure.
- [x] Exact duplicate blobs distinguished from related PDF/text pairs.
- [x] Configuration observations and unverified limits recorded.
- [x] Target architecture proposed without changing existing paths.
- [ ] LAEV approval of target architecture.
- [ ] Source/derivative classification for all extensionless companions.
- [ ] Full migration manifest and rollback plan.
- [ ] Branch/access/recovery policy decisions under repository governance.
- [ ] Implementation of approved migration through a separate PR.

## 13. WP-0.5 status

**Status: IN_PROGRESS — INVENTORY COMPLETE; ARCHITECTURE PROPOSED; MIGRATION NOT AUTHORIZED.**

The audit and target architecture are recorded. The repository remains unchanged by this audit. WP-0.5 cannot be marked complete until LAEV approves the architecture, unresolved governance decisions are disposed, the migration plan is prepared, and any authorized implementation is verified and accepted.

---

End of ERX-REPOSITORY-ARCHITECTURE-001
