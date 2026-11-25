# ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
## Proposed Repository Access and Responsibility Matrix

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001 |
| Version | 0.1.0 |
| Status | PROPOSED — NOT APPROVED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and approval authority | LAEV |
| Date | 2026-11-24 |

## 1. Purpose

This proposal separates repository roles from actual GitHub permission grants. It provides a decision basis for access policy and identifies responsibilities without inventing named contributors, reviewers or administrators.

## 2. Role model — proposed

| Role | Responsibility | Minimum conceptual access | Assignment |
|---|---|---|---|
| Design and approval authority | Approves project policy and controlled documents within its authority | Review and approval authority; GitHub admin only if separately granted | LAEV is identified by the Workplan as design/approval authority; actual account grant observed separately |
| Repository administrator | Maintains repository settings, access and recovery | Admin | NOT_ASSIGNED in this matrix |
| Maintainer | Maintains approved repository structure and operational configuration | Maintain | NOT_ASSIGNED |
| Document author | Prepares controlled documents and records | Write only where needed | Named per artifact; no roster supplied |
| Technical reviewer | Reviews technical correctness and consistency | Read; write only if assigned | NOT_ASSIGNED |
| Independent reviewer | Performs independent review when commissioned | Read-only by default; scoped access if needed | NOT_ASSIGNED; no independent review claimed |
| Contributor | Submits changes within assigned scope | Read and proposed changes through approved process | NOT_ASSIGNED |

## 3. Proposed permission principles

1. Apply least privilege and grant only the access needed for an assigned function.
2. Separate repository administration, authorship, review and approval.
3. Do not treat the GitHub account's technical ability to push as substantive document approval.
4. Use named, individually accountable accounts; do not share credentials.
5. Review and revoke access when a role ends or changes.
6. Do not publish confidential personal or institutional data without authorization.
7. Preserve an auditable record of permission changes.
8. Keep external independent review separate from LAEV's design approval.

## 4. Current evidence boundary

GitHub repository metadata returned admin, maintain, push, pull and triage permissions for the connected identity used by the integration. This confirms the connected identity's reported permission only. The collaborator/team roster and permission level of each other user were not retrieved in the preliminary audit.

## 5. Decisions required

- Confirm who is authorized to administer the repository.
- Confirm whether LAEV's GitHub identity is the sole administrator or whether other administrators are required.
- Define who may merge to main and under what review conditions.
- Define whether outside contributions and pull requests are accepted.
- Define required review count and reviewer independence.
- Define emergency correction access and retrospective review.
- Define periodic access review and account-recovery owner.

## 6. Status and acceptance boundary

This matrix is a proposal for LAEV review. It does not grant, revoke or alter GitHub permissions; it does not identify unnamed people; and it does not assert that branch protection or mandatory reviews are configured.

---
End of ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
