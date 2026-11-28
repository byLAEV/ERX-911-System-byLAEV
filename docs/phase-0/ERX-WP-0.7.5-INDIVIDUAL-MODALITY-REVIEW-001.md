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

## 3. Final individual modality disposition

| Disposition | Count |
|---|---:|
| MANDATORY_CANDIDATE | 95 |
| NOT_MANDATORY | 11 |
| RECOMMENDATION_CANDIDATE | 1 |
| **Total** | **107** |

## 4. Non-mandatory and recommendation records

| Individual ID | Disposition | Source-derived rationale |
|---|---|---|
| ERX-REQ-UTXO-0001 | NOT_MANDATORY — DESCRIPTIVE_DEFINITION | Protocol p.3 defines a valid transition and consumed-state history; it does not state an independent obligation |
| ERX-REQ-AGENT-0001-A / -B | NOT_MANDATORY — DIAGRAM_DERIVED_PROCEDURAL_PATH | Atlas Lámina 03 depicts separate center and agent identification/credential branches; they are diagram-derived process structure, not independent modal commands |
| ERX-REQ-AGENT-0002 | NOT_MANDATORY — DIAGRAM_DERIVED_PROCEDURAL_PATH | Atlas p.8 shows the no-response registration branch as a process path |
| ERX-REQ-ARCH-0002 | NOT_MANDATORY — PROPOSED_ARCHITECTURE | Roadmap §3.1 expressly says “Se propone organizar ERX”; proposal language is not an approved mandatory obligation |
| ERX-REQ-CORE-0002 | NOT_MANDATORY — DESCRIPTIVE_DEVELOPMENT_SCOPE | Roadmap §4.1 presents a module/responsibility table as development scope, not an independent imperative |\n| ERX-REQ-CONTACT-0001 | NOT_MANDATORY — DESCRIPTIVE_EVENT_DISTINCTION | Protocol p.11 distinguishes initial reception time and agent-response time as separate events |
| ERX-REQ-OTS-0003-A | MANDATORY_CANDIDATE | Protocol §12 says each JSON document produces an independent cryptographic commitment; this per-document output is retained separately from the descriptive workflow sequence |
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

No recommendation was promoted to a mandatory candidate. No definition, diagram-derived path, proposed architecture, descriptive scope or evidentiary boundary was treated as a mandatory implementation obligation. The independent per-JSON commitment output in OTS-0003-A remains a mandatory candidate. Both mixed parents remain split: CRYPTO-0002-A is mandatory and CRYPTO-0002-B is a recommendation; OTS-0003-A is mandatory and OTS-0003-B through -D are descriptive workflow steps.

## 6. Determination

**Individual semantic/modality review COMPLETED / ACCEPTED.** All 107 child records have been independently checked against exact source evidence. The 95 mandatory candidates, 11 non-mandatory descriptive/derived records and one recommendation are separately classified. Scope/condition checks pass; actor/trigger/outcome is PASS or explicitly justified NOT_APPLICABLE. All candidates and children remain NOT_APPROVED pending the separate baseline approval process.

---
End of ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 v1.4.0.
