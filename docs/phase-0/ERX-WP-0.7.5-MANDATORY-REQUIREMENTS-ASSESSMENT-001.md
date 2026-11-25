# ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7.5-MANDATORY-REQUIREMENTS-ASSESSMENT-001 |
| Version | 0.1.0 |
| Status | WORKING ASSESSMENT — SOURCE-MODALITY REVIEW PENDING |
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
| MANDATORY_CANDIDATE | 57 | Normalized statement contains explicit normative wording; exact source-clause confirmation and authority review are still required. |
| MODALITY_UNRESOLVED | 25 | Existing evidence does not safely establish whether the source is mandatory, recommendatory, or descriptive. |
| **Total source candidates assessed** | **82** | All rows in the canonical source-candidate register received a disposition. |

The 57 records are candidates, not approved mandatory requirements. The 25 unresolved records are not treated as non-mandatory; their modality remains undetermined.

## 4. Controlled register changes

The field `mandatory_assessment` in `registers/requirements-traceability.csv` was updated for all 82 source candidates:

- 57 rows: `MANDATORY_CANDIDATE`, with explicit warning that clause-level confirmation remains pending.
- 25 rows: `MODALITY_UNRESOLVED`, with a reason not to infer normative force.
- Existing source IDs, source locators, origin classes, requirement text, classifications, lifecycle states, phase allocations and approval states were preserved.
- No row was changed to APPROVED.
- No source recommendation was converted into an obligation by this screening.

The 107 individually identified records remain linked to the 82 source candidates through their parent references. Their individual child-level normative review remains necessary wherever decomposition may have changed or narrowed the original obligation.

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
