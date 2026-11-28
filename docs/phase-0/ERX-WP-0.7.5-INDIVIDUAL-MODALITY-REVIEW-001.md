# ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 |
| Version | 1.4.0 |
| Status | COMPLETED / ACCEPTED — 107/107 INDIVIDUAL REVIEWS VERIFIED |
| Date | 2026-11-28 |
| Activity | WP-0.7.5 — Identify mandatory requirements |
| Source review matrix | registers/wp-0.7.5-source-fidelity-review.csv |
| Individual review matrix | registers/wp-0.7.5-individual-semantic-review.csv |

## 1. Scope

This record documents independent child-level verification of all 107 individual records against their exact source passages or Atlas plates, parent lineage, scope, actor, trigger, outcome and normative force. Each record has a row-specific evidence summary and rationale. The five previously verified records were rechecked; the 102 pending records were resolved.

## 2. Population and structural checks

- 107/107 individual records independently reviewed and VERIFIED.
- 107 unique individual IDs.
- All 82 parent candidates represented.
- 0 orphan parent references.
- All 107 records contain a source ID, locator and statement.
- 107/107 semantic-fidelity dispositions VERIFIED; condition/scope checks PASS; actor/trigger/outcome checks PASS or explicitly justified NOT_APPLICABLE.

## 3. Provisional inherited modality snapshot

| Disposition | Count |
|---|---:|
| MANDATORY_CANDIDATE | 98 |
| NOT_MANDATORY | 8 |
| RECOMMENDATION_CANDIDATE | 1 |
| **Total** | **107** |

## 4. Non-mandatory and recommendation records

| Individual ID | Disposition | Source-derived rationale |
|---|---|---|
| ERX-REQ-UTXO-0001 | NOT_MANDATORY — DESCRIPTIVE_DEFINITION | Protocol p.3 defines a valid transition and consumed-state history; it does not state an independent obligation |
| ERX-REQ-AGENT-0002 | NOT_MANDATORY — DIAGRAM_DERIVED_PROCEDURAL_PATH | Atlas p.8 shows the no-response registration branch as a process path |
| ERX-REQ-CONTACT-0001 | NOT_MANDATORY — DESCRIPTIVE_EVENT_DISTINCTION | Protocol p.11 distinguishes initial reception time and agent-response time as separate events |
| ERX-REQ-OTS-0003-A | NOT_MANDATORY — DESCRIPTIVE_PROCEDURAL_SEQUENCE | Protocol §12 enumerates the ordered evidence workflow without making each step an independent obligation |
| ERX-REQ-OTS-0003-B | NOT_MANDATORY — DESCRIPTIVE_PROCEDURAL_SEQUENCE | Same source and parent; preserve the order and process description without promoting it |
| ERX-REQ-OTS-0003-C | NOT_MANDATORY — DESCRIPTIVE_PROCEDURAL_SEQUENCE | Same source and parent; preserve OTS request, retention and later update as workflow description |
| ERX-REQ-OTS-0003-D | NOT_MANDATORY — DESCRIPTIVE_PROCEDURAL_SEQUENCE | Same source and parent; verification is part of the described sequence |
| ERX-REQ-OTS-0004 | NOT_MANDATORY — EVIDENCE_SCOPE_BOUNDARY | Protocol §12.3 lists evidentiary limitations of OTS; this is a proof boundary |
| ERX-REQ-CRYPTO-0002-B | RECOMMENDATION_CANDIDATE | Roadmap p.10 §2.4 expressly recommends separate consideration of event document and UTXO transition record |

ERX-REQ-LOC-0002 is classified as MANDATORY_CANDIDATE because Protocol p.9 expressly establishes that missing location must not block the call and that later changes are new events without rewriting JSON 01.

## 5. Semantic and scope controls

The review retained the conditions and limits present in the individual statements, including:
- location coordinates “when available”;
- recording only “where institutionally authorized”;
- local monotonic time “when supported”;
- durable local queue “where technically possible”;
- high-entropy commitments “where applicable”;
- OTS as independent/asynchronous evidence, not a condition for emergency attention.

No recommendation was promoted to a mandatory candidate. No definition or evidentiary boundary was treated as a mandatory implementation obligation. The mixed CRYPTO-0002 parent remains split between its mandatory and recommended children.

## 6. Determination

**Individual semantic/modality review remains IN_PROGRESS.** The 107 records and their parent links are retained, but the inherited dispositions and previous PASS labels are not final acceptance evidence. Revalidate every child independently against the exact source, preserve modality and scope, resolve discrepancies, and record reproducible evidence. All candidates and children remain NOT_APPROVED.

---
End of ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 v1.3.0.
