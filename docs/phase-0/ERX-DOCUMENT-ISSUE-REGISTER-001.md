# ERX-DOCUMENT-ISSUE-REGISTER-001
## Documentary Ambiguities, Missing Sources and Open Decisions — Phase 0

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-ISSUE-REGISTER-001 |
| Version | 0.5.0 |
| Status | WORKING REGISTER — PENDING LAEV REVIEW |
| Work Package | WP-0.2 carry-forward / WP-0.3 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Authority | LAEV |
| Updated | 2026-11-24 |

## 1. Purpose and status boundary
This register tracks metadata discrepancies, missing-source conditions, authority questions, scope differences, and possible contradictions. It is not itself an approval or adjudication. A difference in granularity is not automatically a contradiction.

The machine-readable companion is `registers/document-issue-register.csv`.

## 2. Evidence updates
- DOC-ISS-002 is no longer described simply as not located: a candidate named `Consenso ERX byLAEV.pdf` was discovered in `docs/` on 2026-11-24. Its internal identity/version and equivalence to Roadmap reference `ERX-CONSENSUS-001 v0.1` remain unverified. See `ERX-POST-APPROVAL-SOURCE-DISCOVERY-001.md`.
- DOC-ISS-003 remains NOT LOCATED / UNVERIFIED.
- DOC-ISS-008 is RESOLVED_EVIDENCE: all five original PDFs were located in `docs/`; the completion dossier records matching SHA-256 checksums and Git Blob SHA-1 identities.
- DOC-ISS-009 and DOC-ISS-010 were added after direct comparison of ERX-PROT-001 v1.1 Sections 5–10, UTXO-911-001 v1.0 Sections 2–6, and ERX-ATLAS-001 v1.1 Plates 01–08 and its correspondence table.
- The comparison found a broad three-stage communication lifecycle correspondence, alongside a more granular call-request/acceptance description and a distinct agent-availability UTXO in UTXO-911-001. These are unresolved scope/mapping questions, not proven contradictions.

## 3. Current issue status

| ID | Issue | Status | Work Package |
|---|---|---|---|
| DOC-ISS-001 | Atlas filename/internal version discrepancy | OPEN | WP-0.3 |
| DOC-ISS-002 | Candidate `Consenso ERX byLAEV.pdf`; identity to ERX-CONSENSUS-001 v0.1 unverified | CANDIDATE_LOCATED_IDENTITY_UNVERIFIED | WP-0.2 carry-forward / WP-0.3 |
| DOC-ISS-003 | ERX-IMPL-PROPOSAL-001 not located | OPEN | WP-0.2 carry-forward |
| DOC-ISS-004 | Technical Response lacks formal ID/version/date | OPEN | WP-0.3 |
| DOC-ISS-005 | UTXO-911 / Protocol authority relationship | OPEN | WP-0.3 |
| DOC-ISS-006 | Normative force and divergence handling for Atlas plates | OPEN | WP-0.3 |
| DOC-ISS-007 | Whether Technical Response amends Roadmap | OPEN | WP-0.3 |
| DOC-ISS-008 | Original PDF archival and hash verification | RESOLVED_EVIDENCE | WP-0.2 |
| DOC-ISS-009 | Structural divergence: UTXO-911 call-acceptance output vs Protocol/Atlas three-output chain | OPEN | WP-0.3 |
| DOC-ISS-010 | Formal detail of independent agent-availability state machine | SOURCE_ALIGNMENT_CONFIRMED_DETAIL_PENDING | WP-0.3 / later detailed specification |

The exact evidence, impact, required disposition, owner and status are maintained in the CSV companion.

## 4. Issue classes
- VERSION_METADATA — supplied filename and internal version differ.
- MISSING_SOURCE — a cited source was not located in the inspected source set.
- IDENTITY_METADATA — formal identifier, version or date is absent.
- AUTHORITY_AMBIGUITY — subject-matter authority is unresolved.
- DIAGRAM_AUTHORITY — graphical/normative relationship requires a rule.
- RESPONSE_EFFECT — formal effect of a response on its target is not evidenced.
- ARCHIVE_INTEGRITY — source identity and repository preservation evidence.
- SCOPE_GRANULARITY — related sources model the same process at different state granularity.
- STRUCTURAL_MODEL_DIVERGENCE — sources describe materially different state-output or transition decompositions; LAEV must decide whether the difference is a separate output, a sub-state or an approved profile.
- ADDITIONAL_STATE_MACHINE — a source describes a linked state lifecycle not fully specified in another source.

## 5. Handling rules
1. Preserve every supplied original unchanged.
2. Cite exact document IDs, versions, sections, pages and plate numbers where available.
3. Do not infer missing source contents.
4. Do not treat a recommendation as an approved requirement or amendment without approval evidence.
5. Do not infer universal precedence from date, filename or repository location.
6. Do not label a scope difference a contradiction without incompatible propositions in the same scope and conditions.
7. Record every disposition with rationale, evidence, approver and date.
8. Keep unresolved issues visible in the master index and Workplan.
9. Where an issue could affect emergency handling, unique call admission, agent availability, double-spend prevention, evidence integrity, privacy or security, no implementation assumption is approved by this register.

## 6. Dependencies and next action
DOC-ISS-002 requires identity/content verification of the candidate `docs/Consenso ERX byLAEV.pdf`; DOC-ISS-003 remains a source-location/provenance limitation. DOC-ISS-005, DOC-ISS-006 and DOC-ISS-009 require LAEV decisions after review of the source alignment report. DOC-ISS-010 has source alignment in Roadmap Section 3.1; its detailed state machine must be assigned and specified. DOC-ISS-001 and DOC-ISS-004 can be handled through document identification/control in WP-0.4 without altering the originals. DOC-ISS-007 remains a response-effect question.

**Status: WORKING REGISTER — PENDING LAEV REVIEW.** This update does not approve the hierarchy, subject-matter authority, or WP-0.3.

---
End of ERX-DOCUMENT-ISSUE-REGISTER-001
