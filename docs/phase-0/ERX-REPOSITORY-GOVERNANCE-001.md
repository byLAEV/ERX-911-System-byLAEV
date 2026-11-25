# ERX-REPOSITORY-GOVERNANCE-001
## Repository Identity, Structure and Governance — Phase 0 / WP-0.5

| Field | Record |
|---|---|
| Document ID | ERX-REPOSITORY-GOVERNANCE-001 |
| Version | 1.0.0 |
| Status | APPROVED — CONDITIONAL LAEV ACCEPTANCE |
| Document class | Repository governance policy |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | byLAEV/ERX-911-System-byLAEV |
| Design and approval authority | LAEV |
| Approval basis | LAEV standing conditional approval instruction: accept each in-scope part automatically only when complete, correct, and supported by verifiable evidence |
| Date | 2026-11-24 |
| Work Package | WP-0.5 |

## 1. Purpose and scope

This policy establishes the documented identity, purpose, organization, source custody, access model, branch governance, change control, Git-history practice, and intellectual-property/licensing status of the ERX repository.

The repository already exists. WP-0.5 organizes and governs that repository; it does not create a new repository, implement ERX, validate the 911 protocol, authorize deployment, or establish institutional operation.

This policy is a repository-level governance baseline. It does not supersede the approved document-control policy, WP-0.3 document hierarchy, foundational source documents, or LAEV's exact decision records.

## 2. Repository identity and objective

- Canonical repository: https://github.com/byLAEV/ERX-911-System-byLAEV
- Repository name: ERX-911-System-byLAEV
- Owner/namespace: byLAEV
- Project identity: ERX byLAEV — 911 Double-Spend System
- Default branch: main
- Observed visibility: public
- Observed archived state: false
- Primary design and approval authority: LAEV

The repository's objective is to preserve original foundational materials and provenance; maintain controlled ERX documentation; record requirements, architecture decisions, risks, dependencies, reviews and approvals; and hold implementation artifacts only when the applicable phase authorizes them.

Public visibility does not constitute normative approval, institutional acceptance, a license grant, a declaration that every future artifact may be published, or permission to reuse any content.

## 3. Repository structure — as-built baseline

The complete non-truncated recursive Git tree snapshot for main is recorded in `ERX-WP-0.5-REPOSITORY-TREE-INVENTORY-001.md` (root tree SHA `4be78630ab694b1f2c970684e6b6db3f074b1e68`, `truncated=false`).

The observed root structure is:

```text
/
├── README.md
├── WORKPLAN-PHASE-0.md
├── docs/
│   ├── foundational/
│   ├── phase-0/
│   ├── [five original source PDFs and related source text]
│   └── [other source materials]
└── registers/
    ├── document-issue-register.csv
    ├── document-register.csv
    ├── foundational-material-register.csv
    ├── repository-governance-evidence.csv
    └── requirements-traceability.csv
```

The exact file-level listing is in the tree inventory and is the controlling as-built record for that tree SHA. The five original foundational PDFs remain under `docs/`; the foundational inventory, archive procedure, and cross-reference map are under `docs/foundational/`; Phase 0 controlled documents are under `docs/phase-0/`.

The earlier proposed logical structure included future locations such as `docs/requirements/`, `docs/decisions/`, `docs/risks/`, `docs/governance/`, `docs/reports/`, `templates/`, and `.github/`. These are target locations to be created only when a later approved work package requires them. They are not represented as existing. Do not create empty directories solely to match a proposal.

Any future structural change must identify its purpose, affected paths, migration/cross-reference impact, responsible work package, and commit evidence.

## 4. Foundational-source custody and document locations

The accepted WP-0.2 completion dossier is the controlling evidence for the five original supplied PDFs' byte identity: SHA-256 values matched the supplied originals and locally calculated Git blob SHA-1 values matched GitHub blob SHAs. WP-0.5's tree inspection confirms their current paths under `docs/`, but did not repeat binary re-hashing.

Rules:
1. Preserve supplied originals byte-for-byte and retain supplied filenames.
2. Do not overwrite originals with OCR, translation, annotations, extracts, or revised editions.
3. Store derivatives separately and identify their source ID/version and derivation relationship.
4. Keep provenance, integrity digest, archive location, and relevant commit references in the foundational register/dossier.
5. If a source is replaced or supplemented, retain the historical source and document the relationship; do not silently substitute.
6. Record missing or unverified sources explicitly. Never reconstruct missing source content by inference.

The complete current Phase 0 document paths are recorded in the repository tree inventory. The inventory is a point-in-time snapshot and does not replace the document register or the accepted WP-0.2 integrity evidence.

## 5. Access policy and responsibilities

### 5.1 Controlling LAEV decisions

- DP-ACCESS-01: LAEV is the intended sole repository administrator. Decision record: `ERX-WP-0.5-REPOSITORY-ADMINISTRATION-DECISION-001` v1.0.0.
- Repository visibility: KEEP PUBLIC. Decision record: `ERX-WP-0.5-REPOSITORY-VISIBILITY-DECISION-001` v1.0.0.
- DP-ACCESS-02: the role/responsibility and main-branch governance matrix v0.4.0 is APPROVED. Decision record: `ERX-WP-0.5-ACCESS-DECISION-002` v1.0.0.
- Review model: one independent technical review when an independent reviewer is available and assigned. No reviewer has been appointed.

### 5.2 Approved role model

| Role | Governance responsibility | Intended technical permission | Assignment/status |
|---|---|---|---|
| LAEV | Sole repository administrator, design authority, final approval/merge authority | Admin | Owner account byLAEV observed as Admin; sole-admin condition across all access paths NOT_VERIFIED |
| Maintainer | Ordinary repository maintenance; no authority to change administration policy | Maintain | None assigned |
| Independent technical reviewer | Review change against stated criteria; no design-authority transfer | Read; Triage only if needed | None assigned |
| Contributor/document author | Propose changes through fork and pull request; authorship separately recorded | Read upstream; fork/PR contribution | No named upstream collaborator assigned |
| CI automation | Execute only approved checks with least privilege | Minimal workflow token permissions | Workflow token configuration NOT_AUDITED |

GitHub permission levels do not confer ERX authorship, design authority, document approval, or institutional authority.

### 5.3 Live access evidence and limitation

The connected GitHub integration permission object reports admin/maintain/push/pull/triage for that connected identity. A separate permission lookup reports the owner account `byLAEV` as `admin`. These are bounded observations only.

The available interface did not return the complete collaborator/team/inherited-access roster. Therefore:
- The LAEV sole-administrator decision is approved as the governance model.
- The live sole-administrator condition is NOT_VERIFIED / NOT_RECONCILED.
- No claim is made that no other account or inherited principal has Admin-equivalent access.
- No collaborator, team, permission, token, or repository setting was changed.
- Any grant/revocation or access reconciliation requiring configuration changes needs separate express implementation authorization from LAEV.

Access should follow least privilege. Confidential or personal information must not be added to the public repository without an applicable authorization and security/privacy review.

## 6. Branch organization and controls

### 6.1 Canonical branch and approved workflow

- `main` is the canonical repository history and the branch LAEV authorized for WP-0.5 documentation work.
- Ordinary contributors submit changes through fork-based pull requests; no direct upstream write is granted by this policy.
- Maintainers, if later assigned, use pull requests and do not acquire authority to alter administration or branch-protection policy.
- LAEV retains final approval and merge authority.
- A LAEV-authored change cannot be described as independently reviewed by LAEV.
- One independent technical review is required when a reviewer is available and assigned; no reviewer is currently assigned.
- Material changes require traceable purpose, affected paths/documents, review/approval evidence as applicable, and a commit reference.

### 6.2 Observed technical state

Read-only inspection on 2026-11-24 returned:
- `main`: `protected=false`.
- Branch protection enabled: false.
- Required status-check enforcement: off / not shown as enforced.
- Repository rulesets query with `includes_parents=true`: empty list `[]`.
- Branch-protection detail endpoint: 403 FORBIDDEN to the available integration.
- Complete collaborator/team/inherited-access roster: NOT_VERIFIED.

The empty rulesets result does not establish absence of every possible external or inherited control. The branch endpoint's `protected=false` is the direct observation for `main` at the time queried.

### 6.3 Implementation boundary

The governance workflow is approved, but GitHub technical enforcement is not implemented. No branch protection, ruleset, required review, status check, force-push restriction, or repository setting was changed. DP-ACCESS-02 explicitly requires separate express implementation authorization before technical configuration. This policy does not silently provide that authorization.

## 7. Repository change control

The approved `ERX-DOCUMENT-CONTROL-001` v1.0.0 is the controlling document-level identification, versioning, lifecycle, review, approval, provenance, and revision-history policy. The following repository procedure applies it operationally:

1. Identify the purpose, work package, affected paths, and source/decision/requirement references before changing a controlled artifact.
2. Preserve original sources and approved baselines; create derivative drafts rather than silently editing source material.
3. Use a stable document ID and canonical path. Record version, status, author, date, authority, provenance, and revision history.
4. Classify changes as editorial, metadata, clarification, technical, normative, or supersession; assess downstream references and dependencies.
5. Submit material changes for the applicable review. One independent technical review applies when a reviewer is available and assigned under DP-ACCESS-02.
6. Record the competent approval against the exact document version and, where useful, blob/commit identity. A commit, publication, merge, or passing CI is not approval.
7. Only LAEV or expressly delegated authority may approve a controlled design/policy artifact within the delegated scope. No delegation is currently recorded for WP-0.5.
8. Publish the accepted artifact and synchronize the relevant workplan, matrix, and evidence register.
9. Retain prior versions and decision history; never erase rejected, superseded, or withdrawn records.
10. Record unresolved issues as NOT_VERIFIED, NOT_DECIDED, NOT_LOCATED, or NOT_APPLICABLE as appropriate, with impact and resolution owner/condition.

A change to repository settings, collaborator access, license, or other sensitive administrative configuration is outside ordinary document publication and requires its own explicit authorization where the controlling decision records require it.

## 8. Git history, traceability and recovery boundary

- Preserve the Git commit history; do not rewrite published history to conceal changes.
- Use descriptive commit messages naming the work package or affected artifact.
- Link material commits to the relevant controlled document, decision, issue, or approval record.
- Record immutable commit/tree/blob references where they support evidence.
- Retain prior approved versions and their approval records.
- Treat Git history as evidence of repository changes, not proof of correctness, authorship, approval, backup independence, or recoverability.
- GitHub commit history and the recorded tree SHA provide repository traceability. A separate tested backup/restore system has NOT been demonstrated in WP-0.5.
- External backup provider, retention period, recovery-point objective, recovery-time objective, and restore test are NOT_DEFINED / NOT_VERIFIED. Do not claim disaster-recovery readiness. These may be specified in a later authorized work package if required.

## 9. Intellectual property, copyright and licensing

### 9.1 Current state

- Repository metadata reports `license=null`.
- The complete inspected root tree contains no root `LICENSE` or `COPYRIGHT.md`.
- No repository-wide open-source or proprietary license is assigned by WP-0.5.
- The identity of rights holders and the rights status of every contribution/source have not been comprehensively verified.
- Public repository visibility does not grant reuse, modification, distribution, or sublicensing rights.
- No copyright ownership claim, transfer, waiver, or license grant is created by this policy.

### 9.2 Controls

1. Do not add a LICENSE file, copyright declaration, trademark grant, or reuse statement without a separate express LAEV decision based on a defined rights scope.
2. Before a future license decision, identify rights holders and contributors, repository content categories, original-source terms, third-party materials, and any incompatible obligations.
3. Keep foundational originals distinct from LAEV-authored derivatives and third-party contributions.
4. Record provenance and known license/rights statements for each source; use NOT_STATED or NOT_VERIFIED where facts are unavailable.
5. A future license decision must identify exact scope, covered files/content, exclusions, rights basis, effective date, and approving authority.
6. Until such a decision exists, record repository license status as NO LICENSE ASSIGNED / RIGHTS REVIEW OPEN. Do not infer a license from public visibility.

This is a documented current-state and control decision, not a legal opinion or complete title/ownership audit.

## 10. Third-party contributions and external pull requests

Public visibility permits viewing and forking under GitHub's platform features; it does not itself grant a project license to reuse submitted content. No blanket contribution license or contributor agreement is established by this policy. Before accepting third-party content into a normative or implementation baseline, record contributor provenance, the submitted change, any stated rights/license terms, review, and LAEV's acceptance decision. If rights are unclear, do not incorporate the material as an approved project baseline.

## 11. Responsibility and approval separation

- Author: prepares the artifact and is recorded separately.
- Reviewer: evaluates the exact submitted version against stated criteria.
- Design authority: makes design decisions within the approved subject scope.
- Approver: accepts/rejects the exact version under recorded authority.
- Repository contributor: account that commits content; a commit does not establish authorship or approval.
- Repository administrator: maintains GitHub administration under DP-ACCESS-01.

LAEV retains the WP-0.5 design and approval authority. No independent reviewer, maintainer, or additional administrator is appointed by this policy.

## 12. Controlled open matters and limitations

| Matter | Current status | Impact | Owner / resolution condition |
|---|---|---|---|
| Full collaborator/team/inherited access roster | NOT_VERIFIED | Cannot prove live sole-admin condition | LAEV; obtain complete read-only roster and reconcile before claiming enforcement; any permission change separately authorized |
| Technical branch protection and required reviews | NOT_IMPLEMENTED; main observed unprotected | Approved governance workflow is not technically enforced | LAEV; separate express implementation authorization, configure, then verify |
| Independent technical reviewer | NOT_ASSIGNED | One-review control is conditional on availability/assignment | LAEV; appoint a qualified independent reviewer when available and before relying on that review |
| Workflow token/security configuration | NOT_AUDITED | Least-privilege automation not verified | Assigned security/technical owner in a later authorized scope |
| Independent backup/restore | NOT_VERIFIED | Git history alone does not prove recovery | LAEV; define and test recovery controls if required by later scope |
| License and comprehensive rights review | NO LICENSE ASSIGNED / RIGHTS REVIEW OPEN | No reuse grant or complete title opinion can be claimed | LAEV; define rights holders/scope and issue separate express decision |
| Future target directories | NOT_CREATED where absent | No current impact; later packages create only needed paths | Respective future WP when authorized |

These are explicit bounded limitations. They are not silently resolved, and they do not change the WP-0.5 Workplan acceptance criterion, which requires the relevant repository matters to be documented accurately.

## 13. Evidence references

- `WORKPLAN-PHASE-0.md` v1.3.1 — WP-0.5 scope, activities, dependencies, acceptance criterion.
- `ERX-WP-0.5-INITIATION-RECORD-001.md` v1.0.0 — formal initiation and constraints.
- `ERX-WP-0.5-REPOSITORY-TREE-INVENTORY-001.md` v1.0.0 — complete as-built tree snapshot.
- `ERX-WP-0.5-REPOSITORY-AUDIT-001.md` — repository metadata, branch/access limitations.
- `ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001.md` v0.4.0 — approved role and branch governance model.
- `ERX-WP-0.5-ACCESS-DECISION-002.md` v1.0.0 — LAEV approval of the matrix and one-review model.
- `ERX-WP-0.5-REPOSITORY-ADMINISTRATION-DECISION-001.md` v1.0.0 — DP-ACCESS-01.
- `ERX-WP-0.5-REPOSITORY-VISIBILITY-DECISION-001.md` v1.0.0 — KEEP PUBLIC.
- `ERX-DOCUMENT-CONTROL-001.md` v1.0.0 — document lifecycle and change traceability.
- `ERX-WP-0.2-COMPLETION-DOSSIER-001.md` — five-PDF integrity evidence.
- `registers/repository-governance-evidence.csv` — RGE-001 onward.

## 14. Approval and effectiveness

This version is the WP-0.5 repository governance baseline. It was internally checked against the ten WP-0.5 activities, the approved DP-ACCESS decisions, the as-built repository inventory, and the read-only GitHub observations. All material limitations are explicitly stated; no unverified setting, legal right, collaborator, reviewer, license, backup, or implementation is represented as established.

LAEV's standing conditional approval instruction applies to in-scope work only when the relevant part is complete, correct, and supported by evidence. On that basis, this exact v1.0.0 governance baseline is recorded as APPROVED — CONDITIONAL LAEV ACCEPTANCE. The approval does not extend beyond the documented WP-0.5 repository governance scope.

**Approval limitations:** no GitHub settings are changed; no license is assigned; no live sole-admin enforcement, independent review, legal ownership, or disaster-recovery readiness is claimed. Any action expressly requiring separate implementation authorization remains outside this approval.

---
End of ERX-REPOSITORY-GOVERNANCE-001
