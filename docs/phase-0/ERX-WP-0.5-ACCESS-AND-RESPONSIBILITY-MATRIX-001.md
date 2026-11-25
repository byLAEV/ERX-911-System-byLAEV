# ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
## Repository Access, Responsibility and Branch Modification Matrix

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001 |
| Version | 0.3.0 |
| Status | PROPOSED — NOT APPROVED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and approval authority | LAEV |
| Date | 2026-11-24 |

## 1. Purpose and boundary

This matrix defines a proposed least-privilege model for repository administration, maintenance, review, contribution and modification of `main`. It distinguishes governance authority from GitHub technical permissions. It records DP-ACCESS-01 (LAEV as sole repository administrator) but does not implement or approve any new permission grant or repository control.

## 2. Controlling decisions

- **DP-ACCESS-01 — RECORDED:** LAEV is the sole repository administrator. No other administrator is designated. See `ERX-WP-0.5-REPOSITORY-ADMINISTRATION-DECISION-001` v1.0.0.
- **Repository visibility — RECORDED:** KEEP PUBLIC. See `ERX-WP-0.5-REPOSITORY-VISIBILITY-DECISION-001` v1.0.0.
- **This matrix — NOT APPROVED:** all role mappings and branch rules below are proposals awaiting LAEV's express decision.

## 3. Proposed role-to-permission model

| Role | Proposed GitHub permission | Permitted activity | Restrictions | Current assignment |
|---|---|---|---|---|
| LAEV — repository administrator and design/approval authority | Admin | Repository settings, access administration, policy decisions, final merge authority | Sole administrator; no other Admin role | LAEV; live sole-admin condition NOT_VERIFIED across all users |
| Maintainer | Maintain | Maintain repository content, triage work, manage ordinary repository maintenance | No Admin; no changes to access policy or protected-branch rules; no bypass of required reviews | NONE_ASSIGNED |
| Technical reviewer | Read (or Triage only if issue/PR triage is needed) | Inspect diffs, comment, submit PR review | No direct push; review does not itself constitute LAEV design approval unless expressly delegated for a defined scope | NONE_ASSIGNED |
| Document author / contributor | Read; contribute through fork and pull request | Read public content, prepare proposed changes in a fork, submit PR | No direct write to upstream `main`; no settings access | Open public contribution path; no named collaborators assigned |
| CI automation identity | No standing human role; minimum workflow token permissions only | Execute approved checks | Read-only by default; write scopes only when a specific workflow requires them | Workflow permissions NOT_AUDITED |

**Interpretation:** GitHub's `Admin`, `Maintain`, `Write`, `Triage`, and `Read` are technical permission levels. They do not automatically confer ERX design authority, authorship, document approval, or institutional authority.

## 4. Proposed rules for `main`

1. `main` is the canonical controlled branch.
2. No collaborator other than LAEV receives direct push permission to `main) under this proposal.
3. External and ordinary contributor changes enter through fork-based pull requests.
4. Maintainers, if later appointed, work through pull requests; Maintain permission must not imply permission to alter repository administration or protection policy.
5. LAEV retains final authority to approve and merge changes to `main`.
6. A pull request authored by LAEV cannot be approved by LAEV as an independent reviewer. If independent review is required for that change, a separately appointed reviewer must review it. No reviewer is appointed by this matrix.
7. Until branch rules are expressly approved and technically configured, these are proposed governance rules only, not enforced controls.
8. Force-push and branch deletion on `main) should be disabled when protection is configured.
9. Required CI/status checks must not be named until the actual workflow checks exist and have been verified.
10. Emergency exceptions, if any, must be separately authorized and recorded by LAEV with scope, reason, commit and retrospective review requirement.

## 5. Live configuration verification — 2026-11-24

| Check | Result | Evidence and limitation |
|---|---|---|
| Repository identity | byLAEV/ERX-911-System-byLAEV | GitHub repository metadata |
| Default branch | `main` | GitHub repository metadata |
| Connected integration identity | Admin permission object | Repository metadata reports admin=true, maintain=true, push=true, pull=true, triage=true for the connected identity only |
| Owner account `byLAEV` | `admin` | Collaborator-permission lookup for username `byLAEV` returned `admin` |
| `main` protected flag | `false` | Branch endpoint returned `protected:false`, protection enabled=false, required status-check enforcement off |
| Repository rulesets | Empty list | Rulesets query with includes_parents=true returned `[]`; does not prove absence of every possible organization-level or other control |
| Complete collaborator roster | NOT_VERIFIED | Available fetch interface rejected the collaborators-list endpoint; no complete user/team roster was returned |
| Other users with Admin | NOT_VERIFIED | Cannot confirm sole live administrator without complete collaborator/team and inherited-access inspection |
| Required reviews/status checks | NOT_CONFIGURED on returned `main` branch object | No protection shown; no checks listed/enforced |
| Workflow token permissions | NOT_AUDITED | Requires separate workflow and Actions settings inspection |

The owner lookup confirms `byLAEV` as Admin, but does not prove that no other user or inherited principal has Admin-equivalent access. The live repository is currently not protected on `main` according to the branch endpoint response. No configuration was changed.

## 6. Required reconciliation before implementation

1. Obtain an authorized, complete collaborator and inherited-access roster.
2. Identify every account/team with Admin, Maintain, Write, Triage or Read.
3. Confirm whether any additional Admin grant conflicts with DP-ACCESS-01.
4. Decide whether to remove/reduce any conflicting grant; this requires separate explicit authorization from LAEV.
5. Approve the proposed role mapping and the `main` workflow.
6. Decide how LAEV-authored changes are reviewed, given that the author cannot independently approve their own PR.
7. Approve the required review count, bypass policy, force-push/deletion restrictions and any status checks.
8. Only after express authorization, configure GitHub settings and verify the effective result.

## 7. Implementation boundary

No GitHub permissions, collaborators, teams, tokens, branch protection, rulesets, workflow permissions, or repository settings were modified during this review. This document is a proposal, not an authorization to change them. Do not claim the sole-administrator decision is technically enforced until all effective access paths have been inspected and reconciled.

## 8. Status and acceptance boundary

This matrix remains **PROPOSED — NOT APPROVED**. DP-ACCESS-01 remains a recorded governance decision. The live `main` branch is observed as unprotected; the complete collaborator roster and inherited access remain NOT_VERIFIED. WP-0.5 remains IN_PROGRESS and is not accepted or closed by this update.

---
End of ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
