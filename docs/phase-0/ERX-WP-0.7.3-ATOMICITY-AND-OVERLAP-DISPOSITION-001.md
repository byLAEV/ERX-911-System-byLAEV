# ERX-WP-0.7.3-ATOMICITY-AND-OVERLAP-DISPOSITION-001

Version: 1.0.0  
Date: 2026-11-25  
Status: EXECUTION COMPLETE — SUBMITTED FOR LAEV ACCEPTANCE  
Work Package: WP-0.7 / Activity 0.7.3  
Controlling identification register: `registers/requirement-identification-register.csv` (107 records)  
Source candidate register: `registers/requirements-traceability.csv` (82 candidates)

## 1. Decision rule

A requirement is treated as individually identifiable when it expresses one independently assessable acceptance outcome. A list of fields, states, test cases, metrics, or evidence items may remain one requirement only where the source defines them as one cohesive schema, suite, output contract, measurement set, or gate and the acceptance test evaluates that unit as a whole. Items that represent separately pass/fail obligations must be decomposed. Similarity of subject does not establish duplication.

This is an identification disposition only. It does not classify, approve, prioritize, assign implementation, or select architecture.

## 2. Disposition of the 18 structured records

All 18 are retained as cohesive acceptance units, not left unresolved. The source locator and parent candidate remain authoritative. Their constituent lists are attributes or members of one defined contract/output/gate, rather than separately independent obligations at this identification level. Verification must validate completeness of the whole set.

| Requirement | Disposition | Atomicity rationale |
|---|---|---|
| ERX-REQ-UTXO-0002 | ATOMIC_COHESIVE_SCHEMA | The fields jointly define the institutional UTXO record schema; schema completeness is one acceptance outcome. |
| ERX-REQ-UTXO-0004 | ATOMIC_COHESIVE_CONTROL_SET | The listed mechanisms collectively define the uniqueness-support control set; individual mechanisms are not independently mandated as separate implementations by this statement. |
| ERX-REQ-UTXO-0011 | ATOMIC_COHESIVE_VALIDATION_AND_TRANSITION | The listed checks are conjunctive preconditions for one valid single-consumption transition. |
| ERX-REQ-INT-0001 | ATOMIC_COHESIVE_ADAPTER_CONTRACT | The fields jointly define the minimum adapter interface contract. |
| ERX-REQ-INST-0001 | ATOMIC_COHESIVE_INSTALLATION_PROFILE | The elements jointly constitute one validated institutional installation profile. |
| ERX-REQ-VERIFY-0001 | ATOMIC_COHESIVE_VERIFICATION_PACKAGE | The evidence members jointly form the export package needed for one independent-verification outcome. |
| ERX-REQ-CRYPTO-0001 | ATOMIC_COHESIVE_SIGNATURE_SPECIFICATION | The list defines the required contents of one signature specification; it does not select each algorithm/lifecycle option. |
| ERX-REQ-TEST-0003 | ATOMIC_COHESIVE_CORE_TEST_SUITE | The scenarios are members of one core test-suite coverage obligation. |
| ERX-REQ-SEC-0001 | ATOMIC_COHESIVE_SECURITY_CONTROL_BASELINE | The controls form one baseline to be assessed as a complete security-interface contract. |
| ERX-REQ-TEST-0004 | ATOMIC_COHESIVE_TEST_PROGRAM | Categories and referenced mandatory tests collectively define test-program coverage. |
| ERX-REQ-TEST-0005 | ATOMIC_COHESIVE_ACCEPTANCE_METRIC_SET | The metrics form one acceptance measurement set; numeric targets are a separate specification dependency, not multiple independent requirements here. |
| ERX-REQ-PILOT-0001 | ATOMIC_COHESIVE_SHADOW_MODE | The listed activities define one non-interfering shadow-operation mode. |
| ERX-REQ-PILOT-0002 | ATOMIC_COHESIVE_COMPARISON_SET | The listed dimensions jointly define one pilot comparison protocol. |
| ERX-REQ-HOMO-0001 | ATOMIC_COHESIVE_HOMOLOGATION_GATE | The evidence items collectively constitute one center homologation gate. |
| ERX-REQ-HOMO-0002 | ATOMIC_COHESIVE_ADMISSION_GATE | The items collectively constitute one additional-center admission gate. |
| ERX-REQ-RECV-0001 | ATOMIC_COHESIVE_RECEPTION_SCHEMA | The fields jointly define one JSON 01 reception-record schema. |
| ERX-REQ-CONTACT-0002 | ATOMIC_COHESIVE_CONTACT_OUTCOME_MODEL | The mutually exclusive outcomes and prohibition jointly define one contact-result model. |
| ERX-REQ-TIME-0001 | ATOMIC_COHESIVE_TIMESTAMP_TAXONOMY | The timestamp names are distinct members of one temporal-evidence taxonomy; each is not a separate system obligation by this statement alone. |

If later design or verification work establishes independently testable obligations for individual list members, those may be derived as child requirements under change control; this does not invalidate the present source-level identification.

## 3. Disposition of the eight overlap groups

No candidates are merged or deleted. The relationships are classified as follows:

| Group | Relationship | Disposition |
|---|---|---|
| OV-UTXO-DOUBLE-SPEND | SAME INVARIANT / DIFFERENT CONTROL LEVELS | ERX-REQ-UTXO-0003 states the outcome invariant; 0010 specifies concurrent-transition prevention/control; 0011 specifies validation and atomic transition conditions. Retain distinct. |
| OV-UTXO-IDEMPOTENCY | RELATED BUT DISTINCT | ERX-REQ-UTXO-0005 addresses duplicate institutional effects on telephone-event retransmission; ERX-REQ-UTXO-0009-B addresses duplicate admission for a retransmitted event. Different lifecycle boundary; retain distinct. |
| OV-UTXO-ATOMIC-ADMISSION | RELATED BUT DISTINCT | ERX-REQ-UTXO-0007 binds initial UTXO 01 to original event and uniqueness rule; ERX-REQ-UTXO-0009-C governs atomic consumption/successor creation; ERX-REQ-UTXO-0013 defines transaction boundary and OTS exclusion. Retain distinct. |
| OV-OTS-NONBLOCKING | SAME PRINCIPLE / DIFFERENT SCOPE | ERX-REQ-UTXO-0008-B states emergency-attention independence from OTS confirmation; ERX-REQ-UTXO-0012 states non-blocking behavior across reception, acceptance and attention. Retain both; mark related, not duplicates. |
| OV-OTS-LIFECYCLE | LIFECYCLE VS PROCESS | ERX-REQ-OTS-0001 defines evidence states; 0002 defines the evidence-processing sequence; 0003 defines independent commitments/verification steps. Retain distinct. |
| OV-VERIFIER-OUTPUT | PACKAGE VS RESULT DIMENSIONS | ERX-REQ-VERIFY-0001 defines verifier input package and independence; 0003 defines result dimensions; 0005 defines concrete report/check outcomes. Retain distinct. |
| OV-IDENTITY-SEPARATION | INSTITUTIONAL VS PROFESSIONAL IDENTITY / OPERATIONAL EFFECT | ERX-REQ-INST-0002 defines institutional trust states; ERX-REQ-IDENT-0002 defines credential-validation states; ERX-REQ-AGENT-0003 defines agent verification and attention continuity. Retain distinct. |
| OV-TELEPHONE-CONTINUITY | INFRASTRUCTURE AVAILABILITY VS IDENTITY-VALIDATION FAILURE | ERX-REQ-OPS-0001 protects official telephone operation during ERX failure; ERX-REQ-OPS-0004 preserves call continuation while identity remains pending/unverified. Retain distinct. |

## 4. Reconciliation and structural audit

- Source candidate rows: 82.
- Individual identification rows: 107.
- Unique individual IDs: 107.
- Candidate parents represented: 82.
- Missing parent candidates: 0.
- Orphan parent references: 0.
- Duplicate individual IDs: 0.
- Compound source candidates decomposed: 14.
- Atomic child records created: 39.
- Structured records dispositioned: 18/18.
- Potential overlap groups dispositioned: 8/8.
- Source-derived records silently discarded, merged, or marked approved: 0.
- All records retain source-derived origin, review-pending lifecycle, and NOT_APPROVED status.

## 5. Scope and limits

The register and this disposition identify and relate source requirements. They do not decide whether a requirement is mandatory, classify it under WP-0.7.4, determine design, close specification gaps, resolve architecture decisions, approve the requirement baseline, or authorize implementation. Exact clause verification remains in WP-0.7.9 and may raise a controlled correction if a source locator or interpretation is disproved.

## 6. Completion recommendation

The individual identification activity has completed its identification, decomposition, atomicity-disposition, overlap-disposition, and parent-reconciliation work. It is submitted to LAEV for acceptance against the WP-0.7.3 criterion. Until LAEV expressly accepts it, the controlled workplan must show **EXECUTION COMPLETE — ACCEPTANCE PENDING**, not COMPLETED / ACCEPTED.

---
End of record.
