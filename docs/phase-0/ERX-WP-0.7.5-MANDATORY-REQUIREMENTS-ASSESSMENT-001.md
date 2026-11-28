# ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001 |
| Version | 0.3.0 |
| Status | CONTROLLED SCREENING AND INDIVIDUAL MAPPING — ACCEPTANCE PENDING |
| Work package | WP-0.7 — Requirements Identification and Classification |
| Activity | 0.7.5 — Identify mandatory requirements |
| Date | 2026-11-25 |
| Authority | LAEV |
| Repository branch | `wp-0.7-requirements-review` |

## 1. Purpose

This record performs the preliminary mandatory-requirement assessment of the 82 source-candidate records in `registers/requirements-traceability.csv`. It distinguishes explicit obligation/prohibition language from requirements whose source modality remains unresolved.

This is a screening and review record. It does not approve the requirements baseline, create legal obligations, or declare every technically desirable property mandatory.

## 2. Method applied

The assessment follows `ERX-REQUIREMENTS-METHOD-001` §§3, 6.1 and 8:

1. Preserve the source ID, version, page/section locator and extracted statement.
2. Examine whether the requirement statement carries explicit normative language, including obligation or prohibition.
3. Do not infer mandatory status solely from technical importance, a requirement-like sentence, or a classification tag.
4. Preserve recommendations as recommendations; do not upgrade them to obligations.
5. Where the normalized register does not preserve sufficient source wording to establish modality, mark the item unresolved.
6. Keep every item unapproved until the source clause and authority are confirmed.

The assessment is against the five supplied foundational source documents already archived and inspected for WP-0.7: ERX-PROT-001 v1.1, ERX-ATLAS-001 v1.1, UTXO-911-001 v1.0, ERX-ROADMAP-001 v1.0, and the technical response to ERX-ROADMAP-001 (formal ID/version not stated in the source).

## 3. Results


| Preliminary disposition | Count | Meaning |
|---|---:|---|
| MANDATORY_CANDIDATE | 76 | Normalized statement contains explicit normative wording; exact source-clause confirmation and authority review are still required. |
| MODALITY_UNRESOLVED | 6 | Existing evidence does not safely establish whether the source is mandatory, recommendatory, or descriptive. |
| **Total source candidates assessed** | **82** | All rows in the canonical source-candidate register received a disposition. |

The 76 records are candidates, not approved mandatory requirements. The 6 unresolved records are not treated as non-mandatory; their modality remains undetermined.

## 4. Controlled register changes

The field `mandatory_assessment` in `registers/requirements-traceability.csv` was updated for all 82 source candidates:

- 76 rows: `MANDATORY_CANDIDATE`, with explicit warning that clause-level confirmation remains pending.
- 6 rows: `MODALITY_UNRESOLVED`, with a reason not to infer normative force.
- Existing source IDs, source locators, origin classes, requirement text, classifications, lifecycle states, phase allocations and approval states were preserved.
- No row was changed to APPROVED.
- No source recommendation was converted into an obligation by this screening.

The 107 individually identified records remain linked to the 82 source candidates through their parent references. The new `ERX-WP-0.7.5-INDIVIDUAL-MODALITY-REVIEW-001 v1.0.0` maps the parent's preliminary modality to every child: 98 inherit `MANDATORY_CANDIDATE` and 9 inherit `MODALITY_UNRESOLVED`. This is a coverage/inheritance mapping, not independent child-level semantic acceptance.

## 5. Important source distinctions to preserve

The foundational sources contain requirements and constraints that must not be collapsed into one generic “mandatory” category. Examples requiring precise handling include:

- The institutional UTXO's fields and unique-state identity (ERX-PROT-001 v1.1, p.3, §2.1).
- Prevention of two processes consuming the same valid state (ERX-PROT-001 v1.1, p.3, §2.1).
- The scope of uniqueness within an authorized coordination domain and the enumerated mechanisms supporting it (ERX-PROT-001 v1.1, p.3, §2.2).
- The prohibition on retransmissions producing duplicate institutional effects (ERX-PROT-001 v1.1, p.4).
- The Roadmap's explicit requirements for UTXO fields, two separate state machines, transition definitions, invariants, architecture and test gates (ERX-ROADMAP-001 v1.0, §§1–4 and subsequent phase sections).
- The Atlas's distinction between emergency continuity and ERX/identity/OTS validation, including its separate lifecycle and evidence states (ERX-ATLAS-001 v1.1).
- The communication UTXO document's agent identity, call stages, evidence, chronology and privacy/custody constraints (UTXO-911-001 v1.0).

A recommendation (for example, a recommended technology or protective mechanism) must remain a recommendation unless an approved authority adopts it. A design constraint is not automatically a legal or regulatory obligation. A source requirement is not automatically an approved implementation design.

## 6. Outstanding work

Before this activity can be submitted for acceptance:

1. Review the exact original clause for each of the 57 mandatory candidates and replace summaries with a reproducible clause quotation or sufficiently precise faithful extract where appropriate.
2. Confirm whether each clause is an obligation, prohibition, recommendation, option, explanatory statement or condition.
3. Record the authority basis: foundational design source, approved governance decision, or identified external legal/regulatory source. No legal compliance claim may be made without jurisdiction and authoritative citation.
4. Resolve all 25 modality-unresolved records by direct source inspection, or retain them as unresolved with a named reason and disposition.
5. Assess all 107 individual records, including child-level effects of decomposition, and retain the parent-source link.
6. Check overlaps and conflicts; do not silently reconcile distinct scopes such as telephone continuity, ERX availability, agent availability, UTXO consumption, event admission and OTS evidence.
7. Obtain LAEV's express review/acceptance of the exact assessment version.

## 7. Acceptance boundary

**Activity 0.7.5 is IN_PROGRESS.** The preliminary screening of all 82 source candidates is recorded. It is not yet COMPLETED / ACCEPTED because exact clause-level modality validation, child-level review of 107 records and LAEV acceptance remain outstanding.

This record does not authorize protocol implementation, Phase 1, institutional deployment, or operational use of ERX.

---

End of ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001


## 7. Direct-source modality correction — 2026-11-25
The 82 candidate rows were rechecked against the exact cited PDF pages for the previously unresolved set. The updated disposition is 76 MANDATORY_CANDIDATE and six MODALITY_UNRESOLVED. The six retained unresolved are: ERX-REQ-UTXO-0001 (definition/transition description); ERX-REQ-AGENT-0002 (Atlas flowchart no-response path, graphical process evidence without explicit textual modal); ERX-REQ-LOC-0002 (composite of non-blocking location and later-event behavior); ERX-REQ-CONTACT-0001 (descriptive distinction between reception and response time); ERX-REQ-OTS-0003 (descriptive workflow sequence); ERX-REQ-OTS-0004 (evidentiary limitations of OTS, better treated as proof-boundary/design semantics than a direct mandatory system obligation). The remaining 19 candidates received source-specific modal rationales in the canonical CSV. MANDATORY_CANDIDATE remains a screening category, not an approved obligation or legal conclusion.


## 8. Reconciliation correction — 2026-11-28

This version corrects stale count language in v0.2.0. The canonical CSV and the v0.2.0 results table both establish 76 MANDATORY_CANDIDATE and 6 MODALITY_UNRESOLVED (82 total). Any reference in v0.2.0 to 57 candidates and 25 unresolved records is superseded and must not be used.

The individual register contains 107 records linked to 82 parents. The individual modality mapping is 98 inherited MANDATORY_CANDIDATE and 9 inherited MODALITY_UNRESOLVED. The nine unresolved children are UTXO-0001, AGENT-0002, LOC-0002, CONTACT-0001, OTS-0003-A, OTS-0003-B, OTS-0003-C, OTS-0003-D and OTS-0004. No child was promoted to approved mandatory status.

## 9. Remaining acceptance gates

- Exact source-clause and diagram fidelity disposition for each of the 82 candidates remains to be completed and evidenced.
- Independent semantic review of all 107 individual statements remains open; parent inheritance alone is not a child-level review.
- For each candidate, the source modality and its authority class must be explicitly distinguished: source-design obligation/prohibition, procedural instruction, descriptive definition, diagram-derived process, recommendation/option, or external legal/regulatory obligation. The five-source baseline does not itself establish external legal compliance.
- Any candidate combining mandatory and recommendatory clauses must be corrected or split without losing lineage.
- LAEV's exact-baseline acceptance remains outstanding.

**Determination: WP-0.7.5 remains IN_PROGRESS — NOT ACCEPTED.** The corrected 82/107 counts and complete parent-to-child mapping are now recorded; they do not satisfy the outstanding exact-source and semantic gates.

---
End of version 0.3.0.
