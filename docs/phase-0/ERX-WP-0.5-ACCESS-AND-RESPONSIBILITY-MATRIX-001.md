# ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
## Repository Access and Responsibility Matrix

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001 |
| Version | 0.2.0 |
| Status | PROPOSED — NOT APPROVED |
| Work Package | WP-0.5 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Design and approval authority | LAEV |
| Date | 2026-11-24 |

## 1. Purpose

This matrix separates repository responsibility decisions from actual GitHub permission grants. It records the express DP-ACCESS-01 decision without implying that live GitHub settings have been changed or reconciled.

## 2. Role model and decision status

| Role | Responsibility | Conceptual access | Assignment / status |
|---|---|---|---|
| Design and approval authority | Defines and approves project design and controlled policy decisions | Approval authority; technical GitHub permission is separate | LAEV |
| Repository administrator | Controls repository administration, access settings and recovery | Admin | **LAEV — sole administrator by express DP-ACCESS-01 decision**; live permission configuration NOT_RECONCILED |
| Maintainer | Maintains approved repository structure and operational configuration | Maintain | NOT_ASSIGNED |
| Document author | Prepares controlled documents and records | Write only where needed | Named per artifact; no general roster supplied |
| Technical reviewer | Reviews technical correctness and consistency | Read; write only if assigned | NOT_ASSIGNED |
| Independent reviewer | Performs independent review when commissioned | Read-only by default; scoped access if needed | NOT_ASSIGNED; no independent review claimed |
| Contributor | Submits changes within assigned scope | Read and proposed changes through approved process | NOT_ASSIGNED |

## 3. DP-ACCESS-01 — recorded decision

LAEV selected `sole`: LAEV is the sole repository administrator. No additional administrator is designated by this decision. The controlling record is `ERX-WP-0.5-REPOSITORY-ADMINISTRATION-DECISION-001` v1.0.0.

The decision resolves repository-administration responsibility only. It does not automatically resolve maintainer, author, reviewer, contributor, merge, branch protection, recovery, or other access roles.

## 4. Permission principles

1. Apply least privilege and grant only the access needed for an assigned function.
2. Separate repository administration, authorship, review and approval.
3. Do not treat technical ability to push as substantive document approval.
4. Use named, individually accountable accounts; do not share credentials.
5. Review and revoke access when a role ends or changes.
6. Do not publish confidential personal or institutional data without authorization.
7. Preserve an auditable record of permission changes.
8. Keep external independent review separate from LAEV's design approval.

## 5. Current evidence boundary

GitHub repository metadata returned admin, maintain, push, pull and triage permissions for the connected integration identity. This confirms only the connected identity's reported permission. The complete collaborator/team roster and individual permission levels were not retrieved. A request to read classic branch protection returned 403 FORBIDDEN (Resource not accessible by integration); repository rulesets endpoint returned an empty list. These observations do not prove that no classic or inherited protection exists.

## 6. Implementation boundary

No GitHub permission, collaborator, team membership, token, branch protection, or repository setting was changed as part of DP-ACCESS-01. Any future permission modification requires separate, explicit authorization from LAEV. First inspect and reconcile the live access configuration with the recorded sole-administrator decision.

## 7. Remaining decisions and work

- Verify the collaborator and team roster and identify any live admin grants.
- Define maintainer, reviewer, contributor and merge authority.
- Define required review count and reviewer independence.
- Define external pull-request policy.
- Define emergency correction access and retrospective review.
- Define periodic access review and account-recovery procedure.
- Verify branch protection and inherited organization rules where access permits.

## 8. Status and acceptance boundary

This matrix remains PROPOSED — NOT APPROVED. DP-ACCESS-01 is an express decision recorded by LAEV; it does not grant, revoke or alter GitHub permissions. It does not assert that branch protection or mandatory reviews are configured, and it does not complete WP-0.5.

---
End of ERX-WP-0.5-ACCESS-AND-RESPONSIBILITY-MATRIX-001
