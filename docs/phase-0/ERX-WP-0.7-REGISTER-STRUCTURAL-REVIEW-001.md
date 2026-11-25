# ERX-WP-0.7-REGISTER-STRUCTURAL-REVIEW-001
## Preliminary Register Integrity and Overlap Review

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-REGISTER-STRUCTURAL-REVIEW-001 |
| Version | 0.1.0 |
| Status | PRELIMINARY REVIEW — TECHNICAL DISPOSITION PENDING |
| Work Package | WP-0.7 / Activities 0.7.3–0.7.9 |
| Date | 2026-11-25 |
| Reviewed artifact | registers/requirements-traceability.csv |
| Reviewed snapshot | 45 data rows; 19 columns |

## 1. Structural checks

At the inspected repository snapshot:
- 45 data records and 19 columns.
- No duplicate requirement IDs.
- No malformed rows (each data row has 19 fields).
- All 45 candidates retain EXTRACTED — REVIEW PENDING.
- No candidate has an assigned owner or approval reference.
- All phase assignments remain UNALLOCATED_PENDING_WP-0.7.10.

These checks establish CSV structural integrity only. They do not establish source correctness, completeness, normative force, testability or approval.

## 2. Candidate overlap clusters requiring semantic review

The following are review leads, not declarations that the records are duplicates. Preserve separate IDs until source scope and conditions have been compared.

| Cluster | Candidate records | Review question |
|---|---|---|
| Single consumption and concurrency | ERX-REQ-UTXO-0001, 0003, 0010, 0011 | Are these distinct lifecycle, system-level concurrency and validator requirements, or should one be a parent with separately testable child requirements? |
| Idempotency/replay | ERX-REQ-UTXO-0005, 0009 | Does the later source locator add atomic retry/result semantics beyond the earlier retransmission constraint? |
| OTS lifecycle/non-blocking operation | ERX-REQ-UTXO-0008, 0012; ERX-REQ-OTS-0001 | Which state vocabulary is source-specific, and which statement concerns service continuity rather than evidence lifecycle? |
| Institutional/agent identity | ERX-REQ-INST-0002; ERX-REQ-AGENT-0001/0002; ERX-REQ-KEY-0001/0002 | Keep institution, center, agent, credential and key authorization as separate subjects; compare validation scope and failure behavior. |
| Transfer continuity | ERX-REQ-TRANS-0001/0002; ERX-REQ-ARCH-0001 | Distinguish the communication-level transfer record from the complete interinstitutional transfer protocol and adapter boundary. |
| Closure and incident lifecycle | ERX-REQ-CLOSE-0001; ERX-REQ-OPS-0003; ERX-REQ-INV-0001 | Distinguish termination classification, incident closure and prohibition on reactivating a closed communication session. |
| Verification | ERX-REQ-VERIFY-0001/0002/0003/0004 | Separate exported evidence inputs, result vocabulary, verification categories and independence of the verifier. |
| Data/cryptographic structure | ERX-REQ-UTXO-0002/0006; ERX-REQ-DATA-0001; ERX-REQ-CRYPTO-0001/0002 | Separate field inventory, formal schema, canonicalization/signature policy and non-circular document/UTXO linkage. |
| Recovery/integrity | ERX-REQ-UTXO-0004/0010; ERX-REQ-INV-0002/0003/0004 | Preserve distinct guarantees for concurrency, immutability, provenance and recovery; define their boundaries and verification evidence. |

## 3. Register quality findings

1. Verification criteria are uneven: several are preliminary prose, while the initial batch explicitly uses NOT_DEFINED. This is acceptable for extraction but does not satisfy WP-0.7 acceptance.
2. Priority remains TBD and owner NOT_ASSIGNED across the current register. No prioritization or accountability is inferred.
3. Phase assignment is uniformly unallocated. This is intentional until the complete requirement is mapped to the Roadmap and dependencies.
4. The 12 Roadmap-derived candidates distinguish requirements from recommendations in the batch narrative. That distinction must be preserved in any later classification.
5. The Technical Response (FND-005) is not yet represented as a source for new normative requirements. Its recommendations must remain non-normative unless an approved decision changes their status.
6. The register needs a controlled source-locator validation pass against the exact source pages and applicable document-authority rules before any candidate is promoted.

## 4. Required next actions within WP-0.7

- Validate all 45 source locators and candidate statements.
- Perform the semantic overlap review above and record retain/merge/split decisions with rationale; do not delete IDs silently.
- Classify each candidate as functional, non-functional, data, security, operational, interoperability, verification or other justified types.
- Distinguish mandatory source language from recommendations and design choices.
- Record pending specification and decision dependencies.
- Complete verification criteria or explicitly document why a criterion cannot yet be defined.
- Allocate phases only where the approved Roadmap supports a clear mapping.
- Generate a consolidated traceability matrix and readiness report before acceptance review.

---
End of ERX-WP-0.7-REGISTER-STRUCTURAL-REVIEW-001
