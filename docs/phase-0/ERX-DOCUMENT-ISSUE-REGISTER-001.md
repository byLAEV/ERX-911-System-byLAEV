# ERX-DOCUMENT-ISSUE-REGISTER-001
## Preliminary Documentary Ambiguities and Open Issues — Phase 0

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-ISSUE-REGISTER-001 |
| Version | 0.1.0 |
| Status | PREPARATORY REGISTER — NOT APPROVED |
| Work Package | WP-0.3 preparation; WP-0.2 dependencies |
| Project | ERX byLAEV — 911 Double-Spend System |
| Date | 2026-11-23 |
| Authority | LAEV |

## 1. Purpose

This register records documentary ambiguities, missing-source conditions, metadata issues, and unresolved authority questions identified from the five supplied foundational PDFs and the repository inspection recorded in the foundational materials register and source cross-reference map.

It is an issue log, not a final contradiction determination. An ambiguity is not automatically a contradiction. No issue is resolved by this register, and no proposed treatment becomes binding without the applicable review and approval.

## 2. Classification

- VERSION_METADATA — discrepancy between supplied filename and internal version metadata.
- MISSING_SOURCE — a referenced source was not present in the inspected source set.
- IDENTITY_METADATA — document identity/version metadata is absent or incomplete.
- AUTHORITY_AMBIGUITY — subject-matter authority or precedence is not established.
- DIAGRAM_AUTHORITY — relationship between graphical and textual normative content requires determination.
- RESPONSE_EFFECT — whether a response formally changes another document is not established.
- ARCHIVE_INTEGRITY — original binary custody and repository integrity evidence remain incomplete.

## 3. Issue Register

See the machine-readable companion: `registers/document-issue-register.csv`.

Current evidence update (2026-11-23): DOC-ISS-008 is **RESOLVED_EVIDENCE**. The five original PDFs were located in `docs/` on `main`; their local SHA-256 checksums match the foundational register and their Git blob SHA-1 values match the GitHub repository objects. The evidence is recorded in `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`. The remaining seven issues are OPEN and retain their existing work-package assignments.

| ID | Issue | Current status | Responsible authority |
|---|---|---|---|
| DOC-ISS-001 | Atlas filename/internal version discrepancy | OPEN | LAEV |
| DOC-ISS-002 | ERX-CONSENSUS-001 v0.1 not located | OPEN | LAEV |
| DOC-ISS-003 | ERX-IMPL-PROPOSAL-001 not located | OPEN | LAEV |
| DOC-ISS-004 | Technical Response lacks formal identifier/version/date | OPEN | LAEV |
| DOC-ISS-005 | UTXO-911-001 / ERX-PROT-001 authority relationship | OPEN | LAEV |
| DOC-ISS-006 | Normative force of Atlas diagrams | OPEN | LAEV |
| DOC-ISS-007 | Whether Technical Response amends Roadmap | OPEN | LAEV |
| DOC-ISS-008 | Original PDF archival and post-commit hash verification | RESOLVED_EVIDENCE | LAEV |

## 4. Handling Rules

1. Preserve each supplied original unchanged.
2. Cite internal document identifiers and versions where stated; preserve the original supplied filename separately.
3. Do not infer that a missing source does not exist outside inspected locations.
4. Do not convert a technical recommendation into an approved requirement or amendment without approval evidence.
5. Do not infer universal precedence from document date, directory location, or a related-document label.
6. Resolve authority questions only after complete source comparison and explicit approval.
7. Record every disposition with rationale, evidence, approver, and date.
8. Keep unresolved items open and visible in the master index and Workplan.

## 5. Dependencies and Status

DOC-ISS-002 and DOC-ISS-003 remain WP-0.2 source-location/provenance matters. DOC-ISS-008 has been resolved by repository byte-identity evidence and is retained as a closed audit item. The remaining issues are prepared for WP-0.3 review but must not be treated as formally adjudicated until WP-0.2 is accepted and WP-0.3 is authorized.

**Status: PREPARATORY — NOT APPROVED.**

This register does not close WP-0.2, approve WP-0.3, establish the final hierarchy, or authorize Phase 1.

---
End of ERX-DOCUMENT-ISSUE-REGISTER-001
