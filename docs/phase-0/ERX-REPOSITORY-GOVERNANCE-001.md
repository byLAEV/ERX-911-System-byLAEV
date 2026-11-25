# ERX-REPOSITORY-GOVERNANCE-001
## Repository Identity, Structure and Governance — Phase 0 / WP-0.5

| Field | Value |
|---|---|
| Document ID | ERX-REPOSITORY-GOVERNANCE-001 |
| Version | 0.2.0 |
| Status | IN_PROGRESS — CONTROLLED WORKING DRAFT; NOT APPROVED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Repository | byLAEV/ERX-911-System-byLAEV |
| Design and approval authority | LAEV |
| Date | 2026-11-23 |
| Dependencies | WP-0.3 COMPLETED / ACCEPTED; WP-0.4 COMPLETED / ACCEPTED; gates released |

## 1. Purpose

This draft proposes governance rules for the ERX GitHub repository, including repository identity, purpose, directory organization, foundational-source custody, Phase 0 documentation, access, branches, modification control, Git history, and intellectual property.

The repository already exists. This document does not claim to have created it, does not approve its current configuration, and does not grant permissions or change repository settings. It is a preparation artifact for WP-0.5 only.

## 2. Repository Identity

- **Repository name:** ERX-911-System-byLAEV
- **Owner/namespace:** byLAEV
- **Canonical repository:** https://github.com/byLAEV/ERX-911-System-byLAEV
- **Project identity:** ERX byLAEV — 911 Double-Spend System
- **Primary design and approval authority:** LAEV

The repository name and owner are recorded as observed in the project repository. Changes to ownership, visibility, naming, or administrative settings require explicit authorization.

## 3. Repository Purpose

The repository is intended to provide a controlled environment for:
- Preserving original foundational sources and their provenance.
- Developing and maintaining ERX governance and technical documentation.
- Recording requirements, architecture decisions, risks, dependencies, reviews, and approvals.
- Maintaining source-code and implementation artifacts only when authorized by the applicable project phase.
- Preserving an auditable history of changes.

Repository publication is not equivalent to normative approval, implementation validation, institutional acceptance, or authorization to operate ERX.

## 4. Proposed Directory Structure

The following is a proposed logical structure, subject to approval after WP-0.3 and WP-0.4:

```text
/
├── README.md
├── WORKPLAN-PHASE-0.md
├── COPYRIGHT.md
├── docs/
│   ├── foundational/
│   │   └── originals/
│   ├── phase-0/
│   ├── requirements/
│   ├── decisions/
│   ├── risks/
│   ├── governance/
│   └── reports/
├── registers/
├── templates/
└── .github/
```

### 4.1 Directory responsibilities

| Directory | Intended content |
|---|---|
| `docs/foundational/originals/` | Exact original source files, preserved without modification |
| `docs/foundational/` | Source inventory, provenance, custody instructions and archival evidence |
| `docs/phase-0/` | Phase 0 Charter, governance drafts, policies, and closure artifacts |
| `docs/requirements/` | Requirements methodology and controlled specifications |
| `docs/decisions/` | Architecture Decision Records and decision evidence |
| `docs/risks/` | Risk analyses and supporting reports |
| `docs/governance/` | Approved governance and responsibility policies |
| `docs/reports/` | Review, audit, validation and progress reports |
| `registers/` | Machine-readable document, requirement, decision, risk and dependency registers |
| `templates/` | Approved templates for controlled documents and records |
| `.github/` | Repository workflows and contribution controls, when authorized |

No directory's existence alone means its policy or contents are approved.

## 5. Foundational Material Custody

- Preserve original source files byte-for-byte.
- Keep original supplied filenames.
- Store translations, OCR, extracts, annotations, and rewritten copies separately from originals.
- Record the internal document identifier and version separately from the supplied filename.
- Record SHA-256 or another expressly approved integrity digest.
- Verify hashes after upload or repository transfer.
- Record the commit containing each archived original.
- Do not mark a source as archived until repository-side verification succeeds.

The current five-source inventory and the archival procedure remain working artifacts. This draft does not claim that the five original PDFs have been committed to the repository.

## 6. Access and Permissions

Proposed access principles:
- Grant only the minimum permissions necessary for a person's assigned role.
- Distinguish read, write, review, and administrative permissions.
- Protect repository administration and branch settings from unauthorized modification.
- Do not publish confidential institutional or personal information without authorization.
- Review access when responsibilities change.

Actual GitHub visibility, collaborators, teams, branch protection, and permission settings must be inspected and expressly approved. This draft does not assert any particular setting is currently enabled.

## 7. Branch Organization

Proposed minimum branch model:

| Branch | Intended role | Control |
|---|---|---|
| `main` | Canonical project history | Changes only through the approved change process |
| `docs/*` | Isolated documentation changes | Review before integration |
| `feature/*` | Future implementation work, only when authorized | Must follow the applicable phase and technical controls |
| `hotfix/*` | Urgent correction to an existing approved artifact | Document reason, impact, review and retrospective record |

This is a proposal, not a statement that these branches currently exist. The final branch model must align with the approved document-control policy and repository capabilities.

## 8. Modification and Review Control

Every substantive repository change should identify:
- Purpose and affected artifacts.
- Source requirements or decision references.
- Author or responsible contributor.
- Reviewer, where required.
- Approval evidence, where required.
- Test or integrity evidence, where applicable.
- Commit or pull-request reference.

A commit message is useful traceability metadata but does not replace a review or approval record. Changes to approved documents must create a new version or controlled amendment; historical content must remain recoverable.

## 9. Git History and Auditability

- Preserve the repository's commit history.
- Do not rewrite published history to conceal changes.
- Use descriptive commit messages.
- Link material changes to the relevant work package, issue, ADR, or approval.
- Retain prior versions of controlled documents.
- Treat Git history as evidence of repository changes, not as proof that the content is correct or institutionally approved.

## 10. Intellectual Property and Licensing

No open-source or proprietary license is assigned by this draft.

Before adding or changing a license:
1. Identify the rights holder and relevant contributions.
2. Define which repository contents are covered.
3. Distinguish original sources, documentation, code, trademarks, and third-party materials.
4. Review any third-party license obligations.
5. Obtain LAEV's express decision.
6. Publish the approved license and record its scope and effective date.

A copyright notice may identify authorship or rights claims but does not itself grant a license. Do not add a license file or claim permissions without an explicit decision.

## 11. Repository Governance Responsibilities

| Responsibility | Proposed accountable authority | Status |
|---|---|---|
| Project design and repository policy | LAEV | Design authority identified; detailed policy pending |
| Document authorship | Named document author | Must be recorded per document |
| Technical review | Assigned reviewer | Not yet assigned by this draft |
| Approval | LAEV or expressly delegated authority | Must be recorded per artifact |
| Repository administration | Authorized GitHub administrator | Current assignment/settings not verified |
| Independent validation | Independent reviewer when required | To be defined in WP-0.10 |

## 12. Current Repository Observations and Limitations

The repository has been used to publish Phase 0 working documents, including the Workplan, Charter, foundational register, and preparatory governance drafts.

The repository tree inspection previously recorded that the five original PDF binaries were not present in the inspected default-branch tree. The current inventory therefore does not claim repository custody of those original files.

The following live repository metadata was inspected for WP-0.5 on 2026-11-24 (Costa Rica, UTC−06:00): repository `byLAEV/ERX-911-System-byLAEV`; visibility `public`; default branch `main`; repository not archived; merge commits, squash merges and rebase merges enabled; auto-merge disabled; update-branch option disabled; authenticated integration reports admin/maintain/push/pull/triage permissions. These metadata do not establish branch protection, required status checks, collaborator roster, signed-commit enforcement, backup policy, or the complete repository tree. Those items remain NOT_VERIFIED pending direct inspection. The five original PDF binaries are recorded in the WP-0.2 register as present on `main` with byte-identity verification; the earlier statement that they were absent is historical and must not be carried forward as current fact.

## 13. Open Decisions

1. Approve the proposed directory structure or define changes.
2. Confirm repository visibility and access policy.
3. Confirm branch model and protection requirements.
4. Define mandatory review and approval paths.
5. Approve source archival location and retention policy.
6. Decide whether and how Git commits must be signed.
7. Decide intellectual property and licensing scope.
8. Define repository administration responsibility and recovery procedure.
9. Approve rules for third-party contributions and external pull requests.
10. Define archival and backup policy beyond Git history.

No open decision is considered resolved by publication of this draft.

## 14. WP-0.5 Status and Acceptance

**Status: IN_PROGRESS — CONTROLLED WORKING DRAFT; NOT APPROVED.**

WP-0.3 and WP-0.4 dependency gates are satisfied. WP-0.5 execution is initiated on branch `wp-0.5-repository-governance`. Initial repository metadata inspection is recorded in Section 12. The following remain open for this work package:
1. Complete repository tree and directory inventory.
2. Verify branch list and protection/rulesets, required reviews and status checks.
3. Verify collaborator/access model and administrative recovery responsibilities.
4. Decide and document branch model, change-control path, and commit-signing requirements.
5. Confirm foundational source custody and retention/backup controls.
6. Decide intellectual-property and licensing scope; no license may be created or implied without express LAEV approval.
7. Resolve open decisions in Section 13 and update the final governance baseline.
8. Verify acceptance criteria and prepare the WP-0.5 closeout evidence.

**This update initiates WP-0.5 but does not approve repository settings, create a license, complete WP-0.5, close Phase 0, or authorize Phase 1.**

---
End of ERX-REPOSITORY-GOVERNANCE-001
