# ERX-MASTER-DOCUMENT-INDEX-001
## Master Document Index — Phase 0 / WP-0.6

| Field | Value |
|---|---|
| Document ID | ERX-MASTER-DOCUMENT-INDEX-001 |
| Version | 1.3.1 |
| Status | IN_PROGRESS — CONTROLLED RECONCILIATION DRAFT |
| Work Package | WP-0.6 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | https://github.com/byLAEV/ERX-911-System-byLAEV |
| Prepared | 2026-11-24 |
| Authority | LAEV |
| Dependencies | WP-0.2, WP-0.3, WP-0.4 and WP-0.5 — SATISFIED |
| Initiation | [ERX-WP-0.6-INITIATION-RECORD-001 v1.0.0](ERX-WP-0.6-INITIATION-RECORD-001.md) |
| Live tree snapshot | `a03e0cf62c43f3a23a77c9faab54bd5e44084bcb` (`truncated=false`, 73 files; snapshot immediately before this index refresh) |

## 1. Purpose and control boundary

This controlled working revision advances v1.2.0 after direct metadata reconciliation and a second-pass review of controlling WP-0.3/WP-0.4 decisions and WP-0.5 acceptance evidence. It reconciles the current repository inventory against the approved document-control policy and accepted WP-0.2 through WP-0.5 evidence. It is not yet the final accepted master index.

The index distinguishes: (a) source-native identity and version; (b) catalogue Index ID; (c) document lifecycle; (d) work-package execution/acceptance; (e) repository presence; and (f) evidence-verification status. These fields are not interchangeable.

A file's presence or a Git commit does not establish correctness, approval, or acceptance. Unknown source metadata remains NOT_STATED, NOT_VERIFIED, or NOT_RECORDED. No missing source is reconstructed by inference.

## 2. Governing records and method

1. [ERX-DOCUMENT-CONTROL-001 v1.0.0](ERX-DOCUMENT-CONTROL-001.md) controls persistent IDs, versions, lifecycle states, metadata, authorship/review/approval and traceability.
2. WP-0.3 accepted decision record controls hierarchy, subject-matter authority, issue dispositions and source relationships.
3. WP-0.2 completion dossier and foundational register control the five-source baseline and byte-integrity evidence.
4. WP-0.5 acceptance record and repository governance control repository identity, current governance and documented limitations.
5. The recursive Git tree is the current path-presence baseline for this revision. Its exact SHA is recorded above; GitHub reported `truncated=false` and 71 repository files.
6. The machine-readable companion is [registers/document-register.csv](../../registers/document-register.csv). It preserves existing catalogue IDs and adds inventory entries for paths absent from the previous CSV. The CSV includes 72 catalogue records: 71 paths present in the live tree plus one NOT_LOCATED referenced source. The latest check found no duplicate catalogue IDs, no duplicate paths, no missing live paths, and no stale paths. All previously marked metadata-reconciliation-pending rows were directly inspected and reclassified; two older foundational support files remain NOT_VERIFIED.

## 3. Foundational source baseline

| Index ID | Source ID | Title | Source version | Repository path | Evidence/status |
|---|---|---|---|---|---|
| IDX-001 | ERX-PROT-001 / FND-001 | ERX byLAEV Institutional Protocol | 1.1 | `docs/ERX byLAEV 1.pdf` | Original archived; byte identity accepted under WP-0.2 dossier |
| IDX-002 | ERX-ATLAS-001 / FND-002 | Institutional Atlas of ERX byLAEV Flow Diagrams and Operation | 1.1 | `docs/ERX-ATLAS-001 v1.pdf` | Internal v1.1; supplied filename retained; byte identity accepted |
| IDX-003 | UTXO-911-001 / FND-003 | UTXO de Comunicación 911 byLAEV | 1.0 | `docs/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | Original archived; byte identity accepted |
| IDX-004 | ERX-ROADMAP-001 / FND-004 | Master Phase Plan for ERX Development, Implementation and Institutional Homologation | 1.0 | `docs/### ERX-ROADMAP-001.pdf` | Original archived; byte identity accepted |
| IDX-005 | NOT_STATED / FND-005 | Technical Response to the Observations on ERX-ROADMAP-001 | NOT_STATED | `docs/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | Supplied response; source does not state formal ID/version; byte identity accepted |
| IDX-016 | ERX-CONSENSUS-001 | ERX byLAEV — Documento normativo, Protocolo de Consenso | 0.1 — Propuesta normativa | `docs/Consenso ERX byLAEV` and PDF counterpart | Identity/content confirmed; remains proposal for review; DOC-ISS-011 controls operational completeness/authority |

ERX-IMPL-PROPOSAL-001 remains NOT LOCATED / UNVERIFIED within the inspected supplied sources and repository evidence (DOC-ISS-003). This does not establish that it does not exist elsewhere.

## 4. Phase 0 document and artifact coverage

The verified live repository path inventory is the recursive tree snapshot `a03e0cf62c43f3a23a77c9faab54bd5e44084bcb` (`truncated=false`, 73 files). The CSV includes 74 catalogue records: 73 live paths plus one NOT_LOCATED referenced source; no duplicate IDs/paths, missing live paths or stale paths were detected. The CSV companion contains the path-level inventory, including Phase 0 and supporting files. Catalogue IDs (IDX-xxx) are not formal document IDs. Current validation: 71/71 live paths represented; one additional NOT_LOCATED referenced source; no duplicate IDs or paths.

Current accepted package states:
- WP-0.2: accepted under `ERX-WP-0.2-APPROVAL-RECORD-001`.
- WP-0.3: COMPLETED / ACCEPTED; decision record `ERX-WP-0.3-LAEV-DECISION-RECORD-001`; DOC-ISS-003 remains bounded limitation, DOC-ISS-010/011 deferred.
- WP-0.4: COMPLETED / ACCEPTED; `ERX-DOCUMENT-CONTROL-001` v1.0.0 approved.
- WP-0.5: COMPLETED / ACCEPTED; `ERX-WP-0.5-ACCEPTANCE-RECORD-001` v1.0.0.

Current WP-0.6 execution artifacts:
- `ERX-WP-0.6-INITIATION-RECORD-001` v1.0.0 — EXECUTION INITIATED.
- `ERX-MASTER-DOCUMENT-INDEX-001` v1.3.0 — controlled reconciliation draft.
- `registers/document-register.csv` — 73 catalogue records planned after adding IDX-076: 72 live repository paths plus one NOT_LOCATED referenced source. Last verified pre-addition tree check found no duplicate IDs/paths, missing live paths or stale paths; final recheck pending.

## 5. Classification model

Apply the approved document-control and hierarchy policies:
- Foundational source / planning source.
- Controlled governance or normative document.
- Work-package execution, decision, approval, acceptance, review, audit or evidence record.
- Register / machine-readable register.
- Supporting procedure, map, matrix or methodology.
- Historical draft / superseded / withdrawn artifact.
- Source derivative or extracted text; never silently substitute for the supplied original.

For each entry, preserve the exact source-native title, document ID and version when stated. A catalogue-only Index ID is used where a source has no formal identifier. Source-native metadata is recorded where directly inspected. Remaining NOT_VERIFIED entries are explicitly preserved rather than inferred.

## 6. Status and relationship controls

Document lifecycle status is taken from the exact controlled document and its decision/approval record. Historical headers are not overwritten by later approvals; instead, the index records the current disposition and points to the controlling approval/closeout record.

The WP-0.6 typed relationship supplement is [ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001 v0.1.0](ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001.md). Internal review findings are recorded in [ERX-WP-0.6-INTERNAL-REVIEW-001 v0.1.0](ERX-WP-0.6-INTERNAL-REVIEW-001.md); that review concludes NOT READY FOR ACCEPTANCE. It supplements, and does not replace, the approved WP-0.3 relationship baseline. Relationships must be source-backed and typed, including:
- cites / referenced by;
- graphically represents;
- derived from / supporting evidence for;
- approves / accepts / closes;
- supersedes / superseded by;
- companion register for;
- dependency of / prerequisite for.

A relationship does not itself imply normative precedence. WP-0.3's subject-matter authority rules remain controlling.

## 7. Pending-source and metadata register

| Item | Current status | Required handling |
|---|---|---|
| ERX-IMPL-PROPOSAL-001 | NOT LOCATED / UNVERIFIED (DOC-ISS-003) | Retain as missing referenced source; obtain original or formal disposition before dependent institutional decision |
| ERX-CONSENSUS-001 v0.1 | Identity confirmed; proposal for review (DOC-ISS-011) | Do not label approved/operational; preserve unresolved quorum, validator, conflict and detailed UTXO rules |
| FND-005 formal ID/version/date | NOT_STATED in supplied source | Preserve unknown values; catalogue separately |
| Legacy WP-0.3 draft headers | Historical versions/statuses | Link to accepted decision and closeout records; do not rewrite historical artifacts |
| ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001 v0.1.0 | IN_PROGRESS | Typed supplement; validate links against approved decisions and live paths |
| Root LICENSE/COPYRIGHT | Not present in WP-0.5 verified tree; no license assigned | Do not infer a reuse grant |

## 8. Reconciliation controls and open work

The previous v1.0.9 draft and CSV were not internally consistent with the current repository and accepted WP-0.3–WP-0.5 status records. This v1.2.0 revision preserves historical catalogue IDs, reconciles the 71 live paths and the missing referenced source, and records direct metadata inspections. It does not claim that every listed document is approved or substantively reviewed.

Remaining WP-0.6 work:
1. Complete semantic review of all remaining controlled Markdown artifacts and exact current headers; preserve source-native historical headers.
2. Resolve the README custody-location contradiction by stating that original PDFs are stored under docs/ root, not docs/foundational/.
3. Validate all typed relationships in the WP-0.6 relationship register against approved DP-01–DP-09, DC-01–DC-09, WP-0.2–WP-0.5 acceptance records and current Workplan.
4. Verify every live path, formal ID uniqueness, CSV/Markdown row consistency and all canonical cross-references after final commits.
5. Review all pending source and deferred issue entries, ensuring DOC-ISS-003 and DOC-ISS-011 remain visible.
6. Produce internal review, readiness report, closeout audit and conditional acceptance record only after every activity passes.

## 9. WP-0.6 status

**WP-0.6: IN_PROGRESS — formally initiated; structural inventory passes at prior snapshot; internal review v0.1.0 records NOT READY FOR ACCEPTANCE; semantic relationship, link validation and closeout evidence remain.**

The dependency gate is satisfied and execution is authorized under the existing scope approval. This v1.2.0 revision is an intermediate reconciliation baseline, not final acceptance. Activities 0.6.1–0.6.9 remain subject to final semantic, relationship, cross-reference and internal consistency evidence.

LAEV's standing conditional acceptance instruction applies automatically to each completed in-scope deliverable once it is correct and evidence-supported. Scope approval is not completion; publication is not acceptance. No repeated scope approval is required.

WP-0.7 remains blocked until WP-0.6 is completed and accepted. Phase 0 remains OPEN; Phase 1 is NOT AUTHORIZED.

---
End of ERX-MASTER-DOCUMENT-INDEX-001
