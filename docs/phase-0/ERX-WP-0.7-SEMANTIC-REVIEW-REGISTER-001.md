# ERX-WP-0.7-SEMANTIC-REVIEW-REGISTER-001
## Individuality, atomicity and overlap review — reconciled scope

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-SEMANTIC-REVIEW-REGISTER-001 |
| Version | 0.2.0 |
| Status | REVIEW REGISTER — HUMAN DISPOSITION REQUIRED |
| Date | 2026-11-25 |
| Canonical source | registers/requirements-traceability.csv (82 candidates) |
| Individual layer | registers/requirement-identification-register.csv (107 records) |

## 1. Conflict correction and control
The former v0.1.0 register stated a 65-candidate scope while its table covered only the earlier 65-row snapshot. That scope is stale. This revision preserves the overlap clusters as **review prompts**, not completed dispositions, and aligns the scope to the canonical 82/107 records.

- Do not delete, merge, renumber or silently supersede an ID.
- Similarity is not proof of duplication.
- A merge, split, parent/child or retain decision requires source evidence and reason.
- No automated disposition or human acceptance is asserted by this update.
- The 107 individual records are children/individualized views linked to the 82 source candidates; they are not 107 additional source requirements.

## 2. Overlap clusters — candidates for review only

| Cluster | Subject | IDs to inspect | Required distinction |
|---|---|---|---|
| SEM-01 | UTXO single-spend, atomicity, concurrency, replay | ERX-REQ-UTXO-0001; 0003; 0004; 0005; 0007; 0009; 0010; 0011; 0013 | Invariant vs mechanism vs event identity vs recovery/test outcome |
| SEM-02 | OTS proof lifecycle / non-blocking emergency path | ERX-REQ-UTXO-0008; 0012; ERX-REQ-OTS-0001; 0002 | State vocabulary vs workflow vs operational availability |
| SEM-03 | Institution, center, agent, credential, trust | ERX-REQ-INST-*; ERX-REQ-AGENT-*; ERX-REQ-IDENT-*; ERX-REQ-KEY-* | Entity identity, authority, credential status, key custody and non-response |
| SEM-04 | Transfer, availability and lifecycle | ERX-REQ-TRANS-*; ERX-REQ-AVAIL-*; ERX-REQ-STATE-*; ERX-REQ-CLOSE-*; ERX-REQ-OPS-0003; ERX-REQ-INV-0001 | Call-state, agent availability, transfer authorization and incident lifecycle |
| SEM-05 | Verifier output and evidence package | ERX-REQ-VERIFY-* | Package content, verifier independence, result vocabulary and evidence dimensions |
| SEM-06 | Architecture, adapters and integration gates | ERX-REQ-ARCH-*; ERX-REQ-INT-*; ERX-REQ-CORE-* | Boundary, interface contract, core scope and authorization gate |
| SEM-07 | Privacy, audio/file custody | ERX-REQ-PRIV-* | Audio-specific metadata vs general custody and prohibited data scope |
| SEM-08 | Tests, quantitative criteria, simulator | ERX-REQ-TEST-* | Test taxonomy, simulator, scenario coverage, source-mandated tests and target selection |
| SEM-09 | Shadow pilot and homologation | ERX-REQ-PILOT-*; ERX-REQ-HOMO-* | Pilot operation/comparison vs center acceptance and expansion |
| SEM-10 | UTXO schema, cryptography and serialization | ERX-REQ-UTXO-0002; 0006; ERX-REQ-DATA-*; ERX-REQ-CRYPTO-* | Field obligations, schema, canonicalization, signature and link semantics |

Wildcard notation identifies families for reviewer navigation; it is not a replacement for the individual IDs in the canonical CSV.

## 3. Mandatory review disposition per record
For each of the 82 candidates and relevant 107 individual records, record: source passage/diagram; atomicity; actor and authority; trigger/preconditions; observable outcome; normative force; primary/secondary classification; overlap disposition; source correction/split/parent-child decision; criterion and method; reviewer/date; status.

Allowed dispositions: RETAIN_ATOMIC, SPLIT_REQUIRED, PARENT_CHILD, OVERLAP_DISTINCT_SCOPE, MERGE_PROPOSAL, DERIVED_RECLASSIFICATION, SOURCE_CORRECTION_REQUIRED, BLOCKED_BY_OPEN_DECISION.

All entries remain PENDING until individually evidenced. No cluster-level statement constitutes acceptance.

---
End of reconciled semantic-review register.
