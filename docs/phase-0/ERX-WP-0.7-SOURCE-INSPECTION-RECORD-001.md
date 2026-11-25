# ERX-WP-0.7-SOURCE-INSPECTION-RECORD-001
## Direct Inspection Baseline — Foundational Requirements Sources

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-SOURCE-INSPECTION-RECORD-001 |
| Version | 1.0.0 |
| Status | SOURCE INSPECTION COMPLETED — REQUIREMENT EXTRACTION IN PROGRESS |
| Work Package | WP-0.7 / Activity 0.7.2 |
| Date | 2026-11-25 |
| Repository | byLAEV/ERX-911-System-byLAEV |
| Source integrity authority | Accepted WP-0.2 completion dossier |

## 1. Purpose and boundary

This record establishes that the five original foundational PDFs were directly opened and text-extracted for the WP-0.7 requirements-identification pass. It records source identity, page counts, direct inspection method, and initial locatable normative statements.

It is not a complete requirements extraction, source amendment, independent technical validation, legal interpretation, or approval of every statement as a binding requirement. A modal statement in a source is a candidate requirement only after its scope, authority, context, and verification conditions are recorded.

## 2. Exact source set inspected

| FND | Source-native identity | Original supplied filename | Pages | Source treatment |
|---|---|---|---:|---|
| FND-001 | ERX-PROT-001 v1.1 | ERX byLAEV 1.pdf | 29 | Direct PDF text extraction; source-native status says design specification for implementation/evaluation/homologation |
| FND-002 | ERX-ATLAS-001 v1.1 | ERX-ATLAS-001 v1.pdf | 29 | Direct PDF text extraction; graphical/operational representation related to Protocol v1.1 |
| FND-003 | UTXO-911-001 v1.0 | UTXO DE COMUNICACIÓN 911 byLAEV.pdf | 12 | Direct PDF text extraction; conceptual and functional specification |
| FND-004 | ERX-ROADMAP-001 v1.0 | ### ERX-ROADMAP-001.pdf | 37 | Direct PDF text extraction; phase planning and development gates |
| FND-005 | Technical response to ERX-ROADMAP-001 | Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf | 2 | Direct PDF text extraction; formal ID/version/date not stated in source |

The five supplied filenames and binary integrity identities remain governed by the accepted WP-0.2 dossier. The files were not re-exported or modified.

## 3. Inspection method

- Opened each exact PDF from the supplied project files.
- Confirmed page count using PDF metadata.
- Extracted searchable text with layout-preserving PDF text extraction.
- Inspected page-specific statements containing normative or constraint language (e.g., “debe”, “deberá”, “no puede”, “no debe”).
- Recorded page numbers as PDF page locators; line numbers from extracted text are not treated as source-native locators.
- Source text was not silently harmonized across documents. Differences remain candidates for source alignment or decision review.

## 4. Initial requirement-bearing source locations

The following are source locators for the initial extraction queue, not yet approved requirement records:

| Source | PDF pages | Candidate topic represented in source |
|---|---|---|
| ERX-PROT-001 v1.1 | 3–4 | UTXO identity, consumed/created state, prevention of concurrent double consumption, retransmission/idempotency |
| ERX-PROT-001 v1.1 | 5–8 | Institutional identity, trust source, validation status and non-blocking telephone service |
| ERX-PROT-001 v1.1 | 9–11 | Event data, canonicalization, atomic state creation and explicit outcomes |
| ERX-PROT-001 v1.1 | 14–18 | Supplementary evidence, transfer, schema metadata, persistent event identity, recovery and multi-center uniqueness boundaries |
| ERX-PROT-001 v1.1 | 20–25 | Access control, privacy, evidence verification, persistence, recovery and continuity |
| ERX-ATLAS-001 v1.1 | 6–9, 13, 15, 19, 27–28 | Duplicate admission, telephone continuity, identity status, disconnect semantics, UTXO single consumption, OTS pending/anchored distinction and verifier outputs |
| UTXO-911-001 v1.0 | 2–5, 7, 9–11 | Three-stage communication lifecycle, agent identity, personal data, closure distinction, availability, atomic transitions and evidence independence |
| ERX-ROADMAP-001 v1.0 | 3–10, 14–17, 21–24, 27–30 | Identity/authorization/evidence principles, UTXO transition requirements, concurrency, simulator, verification, adapters, inter-center transfer and consensus limits |
| Technical response | 1–2 | Recommendations concerning independent availability cycle, asynchronous OTS, transfer authority, verifier independence and evidence-based acceptance; these are response positions, not automatically normative requirements |

## 5. Excluded / bounded sources

- ERX-CONSENSUS-001 v0.1 is a proposal for review; it may be recorded as a source-status/open-decision reference, not treated as an approved operational requirement baseline.
- ERX-IMPL-PROPOSAL-001 remains NOT_LOCATED / UNVERIFIED under DOC-ISS-003; it cannot support an extracted requirement.
- FND-005 has no formal source-native ID or version stated; no metadata is inferred.

## 6. Next extraction controls

Each requirement created from this inspection must carry:
- stable ERX-REQ identifier;
- EXTRACTED / DERIVED / PROPOSED origin;
- exact source ID/version and PDF page/section locator;
- faithful statement preserving modality and context;
- requirement type and status;
- rationale if derived;
- verification criterion or explicitly NOT_DEFINED;
- assigned phase only when supported by the approved Roadmap;
- decision/ambiguity reference where applicable.

No candidate statement is approved solely by its inclusion in the traceability CSV.

---
End of ERX-WP-0.7-SOURCE-INSPECTION-RECORD-001
