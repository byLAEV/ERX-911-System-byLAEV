# ERX-DOCUMENT-GOVERNANCE-001
## Document Organization and Hierarchy — Phase 0 / WP-0.3

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-GOVERNANCE-001 |
| Version | 0.5.0 |
| Status | WORKING DRAFT — PENDING LAEV APPROVAL |
| Work Package | WP-0.3 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and Approval Authority | LAEV |
| Evidence baseline | Five foundational PDFs inspected; WP-0.2 accepted by LAEV and recorded in Workplan |
| Updated | 2026-11-24 |

## 1. Purpose
This document proposes governance principles for classifying, organizing, interpreting, modifying and preserving ERX documentation. It is a working proposal and does not itself approve hierarchy or subject-matter authority.

## 2. Governing principles
1. Preserve supplied originals unchanged.
2. Maintain traceability from every derivative to exact source versions.
3. Do not silently reconcile different statements.
4. Distinguish subject-matter relevance from universal precedence.
5. A commit or publication is not approval.
6. Preserve version, provenance, history and unresolved uncertainty.
7. Do not infer contents of unavailable referenced documents.
8. Do not treat a response or recommendation as an amendment without express approval.

## 3. Document classes
- Foundational normative protocol source.
- Foundational graphical/operational source.
- Foundational functional source.
- Foundational planning source.
- Technical response/review artifact.
- Governance and approval artifact.
- Controlled development specification.
- Verification artifact.
- Implementation artifact.
- Working register or analysis artifact.
- Referenced but unavailable source.

The classification and source-specific assignments are in ERX-DOCUMENT-HIERARCHY-MATRIX-001.md.

## 4. Proposed hierarchy
The four-level governance model is:
- Level A — LAEV-approved project mandate and governance.
- Level B — foundational sources, each within its own subject and provenance.
- Level C — approved derivative specifications and decisions.
- Level D — working, implementation and verification artifacts.

These levels do not establish universal precedence between Level B sources. The detailed proposal and limits are in ERX-DOCUMENT-HIERARCHY-MATRIX-001.md. Adoption remains pending LAEV.

## 5. Subject-matter authority
The proposed allocation by subject is in ERX-SUBJECT-MATTER-AUTHORITY-MATRIX-001.md. It distinguishes institutional protocol, graphical representation, functional UTXO cycle, project planning, response/review, and unavailable cited sources. It is not binding until LAEV approves it.

## 6. Relationships and source alignment
The source-backed relationship map is ERX-DOCUMENT-RELATIONSHIP-MAP-001.md; the direct comparison is ERX-WP-0.3-SOURCE-ALIGNMENT-REVIEW-001 v0.7.0.

The comparison identifies:
- Broad correspondence among the three communication stages described in Protocol, Atlas and Roadmap.
- A structural divergence: UTXO-911 Sections 2.1–2.5 create a distinct call-acceptance UTXO before its initial-protocol UTXO; Protocol Step 15 and Atlas Plate 03 transition UTXO 01 directly to UTXO 02, which records contact and initial protocol. LAEV must decide the mapping.
- The Roadmap expressly establishes a related-but-independent agent-availability cycle in Section 3.1; UTXO-911 and the Technical Response support it. Remaining work is detailed state-machine formalization and assignment, not architectural discovery.
- An explicit Atlas-to-Protocol normative relationship.
- A Technical Response whose formal amendment effect on the Roadmap is not evidenced.
- ERX-CONSENSUS-001 v0.1 is confirmed from the plain-text repository source and matches the Roadmap citation; it is a proposal for review, with operational completion/authority tracked as DOC-ISS-011. ERX-IMPL-PROPOSAL-001 remains not located.

These are documented scope and authority questions; no direct contradiction is declared without incompatible statements in the same scope.

## 7. Contradiction and ambiguity handling
The controlled draft procedure is ERX-CONTRADICTION-AND-AMBIGUITY-HANDLING-001.md. It requires exact source/version/section references, classification, impact, interim treatment, review, LAEV disposition and synchronized registers. It remains pending approval.

## 8. Document evolution and supersession
The controlled draft policy is ERX-DOCUMENT-EVOLUTION-AND-SUPERSESSION-001.md. It requires baseline preservation, explicit change classification, impact review, competent approval, traceable publication and retention of prior versions. It remains pending approval.

## 9. Issue control
The current issue register is ERX-DOCUMENT-ISSUE-REGISTER-001 v0.9.0 and registers/document-issue-register.csv. It contains DOC-ISS-001 through DOC-ISS-011. DOC-ISS-008 is RESOLVED_EVIDENCE; DOC-ISS-009 remains a material structural mapping decision; DOC-ISS-010 is source-alignment-confirmed with detailed specification and target-WP disposition pending. Other entries remain pending disposition.

## 10. Approval and limits
This document and its referenced matrices are drafts/proposals. LAEV retains design and approval authority. Independent technical review evaluates consistency and evidence but does not replace LAEV approval. No source is amended or superseded by this proposal.

WP-0.3 remains IN_PROGRESS and is not ready for acceptance, as documented in ERX-WP-0.3-ACCEPTANCE-READINESS-REPORT-001 v0.4.0. WP-0.4 and WP-0.5 remain blocked until WP-0.3 is expressly completed and approved. Their drafts are preparatory only. No implementation, deployment, institutional operation or Phase 1 authorization is granted.

---
END
