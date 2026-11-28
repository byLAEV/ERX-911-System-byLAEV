# ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001 |
| Version | 0.7.0 |
| Status | COMPLETED / ACCEPTED — SOURCE FIDELITY AND CHILD SEMANTIC REVIEW VERIFIED |
| Work package | WP-0.7 — Requirements Identification and Classification |
| Activity | 0.7.5 — Identify mandatory requirements |
| Date | 2026-11-28 |
| Authority | LAEV |
| Repository branch | `wp-0.7-requirements-review` |
| Governing method | ERX-REQUIREMENTS-METHOD-001 v1.0.0 §§3.2, 3.3, 6.1 and 8 |

## 1. Purpose and acceptance boundary

This assessment records the completed source-candidate fidelity review and independent child-level semantic/modality review. The exact supplied source PDFs were reopened, cited passages and Atlas plates inspected, source hashes recorded, modality and scope preserved, and all 82 source candidates plus 107 individual records passed the deterministic evidence gate. This is documentary acceptance of Activity 0.7.5 only; it does not approve the requirements baseline or authorize implementation.

Completion of activity 0.7.5 means the source modality has been identified and recorded. It does **not** mean that every candidate is an approved requirement, that the requirements baseline is approved, or that implementation is authorized. Every extracted candidate retains its existing non-approved lifecycle state.

## 2. Source baseline and method

The review reopened the exact supplied PDFs and inspected the cited pages, sections and Atlas diagrams:

- ERX-PROT-001 v1.1 — `ERX byLAEV 1.pdf`.
- ERX-ATLAS-001 v1.1 — `ERX-ATLAS-001 v1.pdf`.
- UTXO-911-001 v1.0 — `UTXO DE COMUNICACIÓN 911 byLAEV.pdf`.
- ERX-ROADMAP-001 v1.0 — `### ERX-ROADMAP-001.pdf`.
- Technical response to ERX-ROADMAP-001 — formal document ID/version are not stated in the source; no candidate in this review relies on it as an independent normative authority.

The method in ERX-REQUIREMENTS-METHOD-001 §§3.2–3.3 and 6.1 controls: preserve source terminology and modal force; descriptive statements, examples and recommendations are not upgraded to mandatory requirements; ambiguous material receives an explicit non-mandatory or unresolved classification; a faithful source summary and reproducible locator are recorded.

## 3. Source-candidate screening snapshot — 82/82 structurally represented

| Recorded preliminary screening disposition | Count | Meaning |
|---|---:|---|
| MANDATORY_CANDIDATE | 73 | Source expresses an explicit obligation, prohibition or imperative applicable to the candidate |
| NOT_MANDATORY | 7 | Definition, diagram-derived process path, proposed architecture, descriptive development scope/event distinction or evidentiary boundary; not an explicit mandatory obligation |
| MIXED_MODALITY_SPLIT | 2 | One mandatory clause plus recommendation; one mandatory commitment output plus descriptive workflow retained separately |
| **Total** | **82** | **82 unique source candidates; 82/82 have source locators and evidence summaries** |

The 73 records remain candidates, not approved requirements. The seven NOT_MANDATORY records remain in the register and are not deleted or misrepresented as requirements. Both mixed parents are split at the individual layer: CRYPTO-0002 separates mandatory definition from recommendation; OTS-0003 separates the per-JSON independent commitment candidate from the descriptive evidence-workflow sequence.

## 4. Resolution of the six prior unresolved source records

| Candidate | Final disposition | Source basis |
|---|---|---|
| ERX-REQ-UTXO-0001 | NOT_MANDATORY — DESCRIPTIVE_DEFINITION | ERX-PROT-001 v1.1 p.3 defines a valid transition and consumed-state history; no independent explicit obligation is stated in the cited passage |
| ERX-REQ-AGENT-0002 | NOT_MANDATORY — DIAGRAM_DERIVED_PROCEDURAL_PATH | ERX-ATLAS-001 v1.1 p.8, Lámina 03 depicts NO RESPONSE → REGISTER NO RESPONSE; this is a flowchart path, not an explicit normative modal |
| ERX-REQ-LOC-0002 | MANDATORY_CANDIDATE | ERX-PROT-001 v1.1 p.9 Step 4 states absence of location does not block the call and later changes are recorded as new events without modifying original JSON 01; the non-blocking prohibition/continuity boundary is explicit |
| ERX-REQ-CONTACT-0001 | NOT_MANDATORY — DESCRIPTIVE_EVENT_DISTINCTION | ERX-PROT-001 v1.1 p.11 Step 10 distinguishes initial reception time from agent-response time as different events; the passage defines event semantics |
| ERX-REQ-OTS-0003 | MIXED_MODALITY_SPLIT | ERX-PROT-001 v1.1 pp.19–20 §12 states each JSON produces an independent cryptographic commitment, then describes an ordered evidence workflow; the commitment output and workflow steps require separate dispositions |
| ERX-REQ-OTS-0004 | NOT_MANDATORY — EVIDENCE_SCOPE_BOUNDARY | ERX-PROT-001 v1.1 p.20 §12.3 describes what OTS does not prove; this is an evidentiary limitation, not an independent system obligation |

## 5. Mixed-modality correction

ERX-REQ-CRYPTO-0002 (ERX-ROADMAP-001 v1.0 p.10 §2.4) contains two distinct source modalities:
- ERX-REQ-CRYPTO-0002-A: define the cryptographic relationship among documents 01, 02 and 03 and their UTXO records without circular dependencies — MANDATORY_CANDIDATE.
- ERX-REQ-CRYPTO-0002-B: consider the event document and UTXO transition record separately — explicitly recommended — RECOMMENDATION_CANDIDATE.

The parent remains MIXED_MODALITY_SPLIT in the source register. The recommendation is not promoted to a mandatory obligation. ERX-REQ-OTS-0003 is also split: child -A (one independent commitment per JSON document) is MANDATORY_CANDIDATE; children -B through -D are descriptive workflow steps and remain NOT_MANDATORY.

## 6. Individual register coverage — 107/107 mapped and semantically verified

| Recorded inherited screening disposition (provisional) | Count |
|---|---:|
| MANDATORY_CANDIDATE | 95 |
| NOT_MANDATORY | 11 |
| RECOMMENDATION_CANDIDATE | 1 |
| **Total** | **107** |

Validation results:
- 107/107 individual IDs are unique.
- 107/107 child records retain a parent candidate reference.
- 0 orphan parent references.
- 107/107 have a source ID, source locator and individual statement.
- All 107 child records have independent semantic-fidelity VERIFIED dispositions; condition/scope checks PASS; actor/trigger/outcome checks PASS or explicitly justified NOT_APPLICABLE for descriptive/definitional records.
- Nine inherited unresolved children have provisional screening labels; their independent modality and source-fidelity determinations remain open.
- Conditional scope (including “when available”, “where technically possible”, and “when institutionally authorized”) is preserved in the individual statements.
- The 0002-A / 0002-B split preserves the original parent lineage and separates obligation from recommendation.

The individual-level results and rationale are recorded in `registers/wp-0.7.5-individual-semantic-review.csv`; the canonical `registers/requirement-identification-register.csv` was synchronized with all 107 child reviews. The source-candidate `registers/requirements-traceability.csv` was synchronized with all 82 source dispositions.

## 7. Traceability and machine-readable evidence

The following records form the completed Activity 0.7.5 evidence set:
1. `registers/wp-0.7.5-source-fidelity-review.csv` — 82/82 exact source passage/Atlas fidelity dispositions VERIFIED.
2. `registers/wp-0.7.5-individual-semantic-review.csv` — 107/107 independent child semantic/modality reviews VERIFIED; condition/scope checks PASS and non-applicable actor/trigger checks are explicitly justified.
3. `registers/requirements-traceability.csv` — canonical source candidates updated with final screening disposition.
4. `registers/requirement-identification-register.csv` — individual statements updated with their child-level review rationale.
5. `ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 v1.4.0` — human-readable partial review and mapping counts.

All source-candidate and individual rows remain NOT_APPROVED. The source class is foundational project documentation, not an external legal/regulatory authority. No claim of legal compliance, external audit, operational readiness or institutional acceptance is made.

## 8. Determination

**Activity WP-0.7.5 — COMPLETED / ACCEPTED.** All 82 source candidates have exact source/Atlas fidelity dispositions VERIFIED. All 107 individual records have independent semantic/modality dispositions VERIFIED, condition/scope PASS, and actor/trigger/outcome PASS or explicitly justified NOT_APPLICABLE. The deterministic GitHub Actions evidence gate passed on run #18 (commit `35fcd16455b5c849e7103245f7a7ad2e63faf440`). The Workplan checkbox for 0.7.5 may be `[x]`.

**WP-0.7 remains IN_PROGRESS.** Completion of this activity does not close WP-0.7. Activity 0.7.9 source-linkage/bidirectional traceability, other WP-0.7 acceptance gates, exact baseline approval and the formal WP-0.7 acceptance determination remain governed by their own controls.

No Phase 1 execution, software implementation, institutional deployment or emergency-service operation is authorized by this activity completion.

---
End of ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001 v0.7.0.
