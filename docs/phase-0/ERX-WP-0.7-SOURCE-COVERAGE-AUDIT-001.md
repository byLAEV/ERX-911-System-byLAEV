# ERX-WP-0.7-SOURCE-COVERAGE-AUDIT-001
## Foundational source inspection and locator coverage

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-SOURCE-COVERAGE-AUDIT-001 |
| Version | 0.2.0 |
| Status | INSPECTION EVIDENCE — LOCATOR/CLAUSE REVIEW PARTIAL |
| Date | 2026-11-25 |
| Work Package | WP-0.7 / Activities 0.7.2 and 0.7.9 |

## 1. Source files reopened in this execution
The five supplied PDF files were opened from the active project workspace and their text extracted for inspection. PDF page counts were read from the files themselves.

| Document | Version identified in source | PDF pages | Candidate rows in canonical register |
|---|---:|---:|---:|
| ERX-PROT-001 — ERX byLAEV 1.pdf | 1.1 | 29 | 23 |
| ERX-ATLAS-001 — ERX-ATLAS-001 v1.pdf | 1.1 | 29 | 4 |
| UTXO-911-001 — UTXO DE COMUNICACIÓN 911 byLAEV.pdf | 1.0 | 12 | 5 |
| ERX-ROADMAP-001 — ### ERX-ROADMAP-001.pdf | 1.0 | 37 | 33 |
| Respuesta técnica a ERX-ROADMAP-001 | version not stated in extracted title page | 2 | 0 |

## 2. Register structure and source-reference checks
- Canonical CSV contains 82 candidate records and 26 unique columns.
- Requirement IDs: 82 unique; no duplicates found.
- All 82 rows have a source ID, source version and non-empty page/section locator.
- All source IDs resolve to one of the four foundational source documents listed above.
- First cited page number in each locator is within the corresponding PDF page count.
- No dangling dependency reference to another ERX-REQ ID was found.
- All 65 records remain EXTRACTED — REVIEW PENDING; no approval is implied.

## 3. Inspection scope
The full text of all five supplied PDFs was extracted. Source content inspected included:
- ERX-PROT-001: UTXO state fields, scoped uniqueness, retransmission handling, institutional identity, authorization, three communication stages, transfers, closure, mandatory single-spend rules, atomicity, idempotency, concurrency, recovery, timestamps, OTS, privacy, verification and operational continuity.
- UTXO-911-001: three-stage communication UTXO cycle, single-spend principle, OTS separation and agent-availability lifecycle.
- ERX-ATLAS-001: visual sequence and state/verification diagrams referenced by candidate records.
- ERX-ROADMAP-001: phase gates, architecture, core scope, test categories, quantitative acceptance metrics, shadow pilot and homologation.
- Technical response: recommendations about concurrent centers, independent cycles, separation of ERX Protocol/Core/Institutional Module/Verifier and asynchronous external evidence processing. Recommendations were not promoted to mandatory extracted requirements.

## 4. Limitations — what this audit does not prove
1. A page-range check is not the same as confirming that the exact sentence/diagram supports every clause of a normalized requirement.
2. Diagram references require visual review of the corresponding plate; extracted text alone does not validate visual arrows, branches or labels.
3. No external legal or institutional regulatory source was supplied or used to create legal compliance obligations.
4. ERX-CONSENSUS-001 and ERX-IMPL-PROPOSAL-001 are not among these five supplied PDFs and are not treated as inspected here.
5. The technical response has no requirement rows because its recommendations were retained as design/decision context, not source-mandatory requirements.

## 5. Required final locator audit
For each candidate, a reviewer must compare the exact page, section, clause or plate against the entire normalized statement and record PASS / CORRECT / SPLIT / DERIVED / BLOCKED. A locator is not source-verified merely because its page exists.

---
End of ERX-WP-0.7-SOURCE-COVERAGE-AUDIT-001


## 6. Reconciliation addendum — 2026-11-25
The current canonical snapshot is 82 unique candidate IDs / 26 columns (blob SHA `df36822682576568f491c90f68bde9b631635d84`). All 82 page/section locators were checked against source PDF page bounds: ERX-PROT-001 29 pages, ERX-ATLAS-001 29 pages, UTXO-911-001 12 pages, ERX-ROADMAP-001 37 pages. No out-of-bounds locator or unknown source ID was found. This remains a locator-boundary check, not a row-by-row quotation/diagram fidelity pass. The 63-gap table still omits 19 candidate IDs; these remain unresolved for activity 0.7.7.
