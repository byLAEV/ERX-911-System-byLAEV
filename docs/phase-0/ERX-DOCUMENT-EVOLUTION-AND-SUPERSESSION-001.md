# ERX-DOCUMENT-EVOLUTION-AND-SUPERSESSION-001
## Document Evolution, Amendment and Supersession Policy

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-EVOLUTION-AND-SUPERSESSION-001 |
| Version | 0.1.0 |
| Status | DRAFT — PENDING LAEV APPROVAL |
| Work Package | WP-0.3 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Owner / Approval Authority | LAEV |
| Date | 2026-11-23 |

## 1. Purpose
Establish principles for controlled evolution of ERX documents while preserving source identity, history, and traceability.

## 2. Core principles
1. Preserve supplied originals byte-for-byte.
2. Never silently edit, overwrite, or reinterpret an approved source.
3. Create a derivative document or new version for every proposed change.
4. A later timestamp, Git commit, publication, implementation, or technical response does not itself amend or supersede a source.
5. Supersession requires explicit approval by the authority assigned to the affected subject and a recorded decision.
6. Preserve superseded and withdrawn versions as historical evidence.
7. Distinguish editorial correction from semantic or normative change.
8. Record unresolved dependencies and missing sources as limitations, not assumptions.

## 3. Change classes
- **Editorial:** spelling, formatting, layout, or typographical correction that does not alter meaning.
- **Metadata:** correction or completion of title, identifier, version, date, provenance, or status.
- **Clarification:** explanation that does not change an approved requirement or behavior.
- **Technical change:** modifies design, interface, data, behavior, constraints, or verification.
- **Normative change:** modifies an approved protocol rule, obligation, authority, or acceptance condition.
- **Supersession:** formally replaces a specified prior version or document within a defined scope.

The change class must be proposed and confirmed during review. A change must not be called editorial if it changes meaning.

## 4. Minimum change record
Every change request records: change ID; affected document ID and version; exact sections; change class; reason; source/evidence; impact analysis; alternatives; compatibility and migration effects where relevant; author; independent reviewer; approval authority; decision; effective version/date; repository commit; and links to prior versions.

## 5. Controlled lifecycle
1. Submit a change request.
2. Identify and preserve the baseline version.
3. Classify the proposed change.
4. Analyze impact and dependencies.
5. Prepare a derivative or candidate revision.
6. Review technical and documentary consistency.
7. Obtain express approval from the competent authority.
8. Publish the approved revision with a traceable commit.
9. Update master index, cross-references, issue register, decision register, and change log.
10. Mark the prior version SUPERSEDED only to the extent explicitly stated in the approval record.
11. Verify retrieval of both current and historical versions.

## 6. Source-specific limits
A diagram may be revised only under the authority and scope assigned to it; a technical response does not automatically amend its target document; code does not silently redefine protocol text; and a missing or unverified reference cannot be used as evidence for a substantive change.

## 7. Version and status boundary
Detailed version syntax, document metadata, and status transitions are governed by WP-0.4 and WP-0.11. This policy establishes the preservation and supersession principles only and does not pre-empt those packages.

## 8. Acceptance criteria
Approval requires: defined change classes; baseline preservation; minimum change record; review and approval path; explicit supersession semantics; historical retention; and synchronized register updates.

## 9. Status
DRAFT — PENDING LAEV APPROVAL. No existing document is amended or superseded by this draft.

---
END
