# ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001
## Phase 0 Document Relationships and Dependency Register

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001 |
| Version | 0.2.2 |
| Status | IN_PROGRESS — CONTROLLED RELATIONSHIP REGISTER |
| Work Package | WP-0.6 |
| Authority | LAEV |
| Date | 2026-11-24 |
| Repository | byLAEV/ERX-911-System-byLAEV |

## 1. Purpose and authority

This derivative register consolidates source-backed relationships and Phase 0 governance dependencies for the master index. It supplements, and does not replace, the approved ERX-DOCUMENT-RELATIONSHIP-MAP-001 v1.0.0. The latter remains authoritative for its approved WP-0.3 source-relationship baseline and its source-native historical content.

Relationship labels are descriptive. A relationship does not create normative precedence, amend a source, or confer approval.

## 2. Foundational-source relationships

| From | Relation | To | Evidence / boundary |
|---|---|---|---|
| ERX-ROADMAP-001 v1.0 | foundational reference | ERX-PROT-001 v1.1 | Roadmap §1; DP-01 assigns scoped protocol authority to Protocol |
| ERX-ROADMAP-001 v1.0 | foundational reference | ERX-ATLAS-001 v1.1 | Roadmap §1; Atlas remains graphical/operational representation |
| ERX-ROADMAP-001 v1.0 | foundational reference | UTXO-911-001 v1.0 | Roadmap §1; DP-02 governs acceptance mapping |
| ERX-ATLAS-001 v1.1 | graphical representation of | ERX-PROT-001 v1.1 | Atlas control section and plates 01–08; DP-04 controls divergence |
| UTXO-911-001 v1.0 | functional elaboration / related model | ERX-PROT-001 v1.1 | DOC-ISS-009 closed by DP-02; acceptance represented as authenticated event/sub-state within atomic UTXO 01→02, not a fourth spendable output in the approved profile |
| ERX-ROADMAP-001 v1.0 | cites as coordination proposal | ERX-CONSENSUS-001 v0.1 | Identity/content confirmed; proposal for review only; DOC-ISS-011 deferred |
| ERX-ROADMAP-001 v1.0 | unverified reference | ERX-IMPL-PROPOSAL-001 | Not located; DOC-ISS-003 bounded limitation |
| Technical Response FND-005 | response/review of | ERX-ROADMAP-001 v1.0 | DP-05: not an amendment absent express controlled approval |
| FND-001–FND-005 | archived/integrity evidence | WP-0.2 completion dossier | Five supplied PDF originals, SHA-256 and Git blob identity evidence; accepted WP-0.2 baseline |
| Plain-text companions | derivative/extraction of | Corresponding original PDF/source | Catalogue entries IDX-069, 071–074; derivative is not replacement for original |

## 3. Phase 0 governance and deliverable relationships

| From | Relation | To | Controlling evidence |
|---|---|---|---|
| WP-0.1 Charter | defines | Phase 0 scope and objectives | ERX-PHASE-0-CHARTER-001 v1.0.0 |
| WP-0.2 | identifies and archives | FND-001–FND-005 | WP-0.2 approval record and completion dossier |
| WP-0.3 | classifies / assigns subject authority | foundational sources and documentary issues | DP-01–DP-09; approved hierarchy and authority matrices |
| WP-0.4 | governs metadata, identifiers, versions, lifecycle and provenance | all controlled documents and registers | ERX-DOCUMENT-CONTROL-001 v1.0.0; DC-01–DC-09 |
| WP-0.5 | governs repository identity, structure and repository controls | repository artifacts and custody | ERX-REPOSITORY-GOVERNANCE-001 v1.0.0; WP-0.5 acceptance |
| WP-0.2–WP-0.5 | prerequisites for | WP-0.6 | WP-0.6 initiation record; all four dependency gates satisfied |
| WP-0.6 | produces and reconciles | master index + document register | ERX-MASTER-DOCUMENT-INDEX-001 and registers/document-register.csv |
| WP-0.6 | must be accepted before | WP-0.7 | WORKPLAN-PHASE-0.md dependency chain; WP-0.7 remains blocked |

## 4. Issue relationships and retained limitations

| Issue | Relationship / status | Control |
|---|---|---|
| DOC-ISS-001 | Atlas filename/internal version discrepancy accepted limitation | Preserve supplied filename; cite internal v1.1 |
| DOC-ISS-002 | Consensus source identity/content confirmed | Proposal status separately controlled by DOC-ISS-011 |
| DOC-ISS-003 | ERX-IMPL-PROPOSAL-001 not located | No inferred content; retain NOT_LOCATED / UNVERIFIED |
| DOC-ISS-004 | FND-005 ID/version/date not stated | Preserve NOT_STATED |
| DOC-ISS-005–008 | Closed/accepted dispositions | Approved WP-0.3 decision record |
| DOC-ISS-009 | Closed by DP-02 | Acceptance event/sub-state within atomic UTXO 01→02 |
| DOC-ISS-010 | Deferred detail | Independent agent-availability cycle accepted; detailed state machine later |
| DOC-ISS-011 | Deferred operational consensus specification/authority | ERX-CONSENSUS-001 v0.1 remains proposal for review |

## 5. Consistency notes and review limits

1. The approved WP-0.3 relationship map is preserved unchanged. Its historical table contains an escaped newline/formatting defect in one source row and older pre-decision wording in some relationship descriptions. This derivative register states the controlling DP-02, DOC-ISS-009 and DOC-ISS-010 dispositions without rewriting that approved historical artifact.
2. The approved hierarchy matrix includes historical heading text “decision required”; its final section records LAEV approval. The controlling decision record and current status table govern.
3. The approved subject-matter authority matrix contains historical “proposed” phrasing in a column heading; its header and final section state APPROVED — WP-0.3. Treat the matrix as approved within its stated scope, not as a pending proposal.
4. The WP-0.3 audit/execution records contain historical downstream statuses in earlier snapshots. Later controlling WP-0.4/WP-0.5 acceptance and current Workplan tracking supersede those snapshots; historical files remain unchanged.
5. DOC-ISS-003 and DOC-ISS-011 remain open/deferred limitations in the project baseline. Their existence does not prevent WP-0.6 inventory acceptance if recorded accurately and bounded, but no dependent technical or institutional decision may infer their contents or approval.

## 6. Relationship validation record

The relationship rows above were cross-checked against the named source identities, WP-0.3 DP-01–DP-09 decision record, DOC-ISS-001–011 issue register, WP-0.4 DC-01–DC-09 control record, WP-0.5 acceptance record, and current Workplan dependency chain. The original/derivative relationships were checked against the corresponding catalogue entries IDX-001–005 and IDX-069–074. The missing-source edge to ERX-IMPL-PROPOSAL-001 remains explicitly unverified and is not represented as a resolved target. The governance dependencies remain one-way gates; WP-0.7 is not enabled until WP-0.6 acceptance.

The approved WP-0.3 relationship map remains unchanged. This supplement records the post-decision interpretation and does not rewrite or silently repair that approved historical artifact.

## 7. Acceptance tests for this register

- Each relationship has a source, target, typed relation and evidence/boundary.
- No relation is used to imply unapproved precedence.
- WP dependency links agree with the approved Workplan and acceptance records.
- Issue states agree with the approved WP-0.3 decision record and issue register.
- The master index and CSV cite this register without circular or unsupported claims.

**Current status: IN_PROGRESS.** Relationship semantics and named control references have received a second-pass documentary cross-check. The register is still a derivative WP-0.6 work product and is not itself accepted; final package-level readiness and closeout remain.

---
End of ERX-WP-0.6-DOCUMENT-RELATIONSHIP-REGISTER-001
