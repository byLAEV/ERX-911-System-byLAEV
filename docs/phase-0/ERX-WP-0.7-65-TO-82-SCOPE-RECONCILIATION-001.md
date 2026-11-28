# ERX-WP-0.7-65-TO-82-SCOPE-RECONCILIATION-001
## Historical baseline to current canonical requirement register — row-level evidence

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-65-TO-82-SCOPE-RECONCILIATION-001 |
| Version | 0.2.0 |
| Status | ROW-LEVEL EXTRACTION RECONCILIATION — SEMANTIC ACCEPTANCE OPEN |
| Date | 2026-11-28 |
| Work Package | WP-0.7 |
| Branch | `wp-0.7-requirements-review` |
| Current canonical CSV SHA | `1b1bd462b916ea1fbca9ba9449a8114e13011761` |
| Historical 45-row CSV SHA | `2cb2b5171eaac5dc8102421fe9e4f7265d3b6aaa` |
| Batch 004 | ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-004 v0.1.0 |
| Batch 005 | ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-005 v0.1.0 |

## 1. Row-level count and lineage determination

The historical 65-candidate extraction baseline is reconstructed as:
- 45 rows from the historical canonical CSV blob `2cb2b5171eaac5dc8102421fe9e4f7265d3b6aaa` at commit `612537ccf7b6b831a02293448f03196c42ac534e`;
- 20 rows explicitly enumerated in extraction Batch 004.

Current canonical source register:
- 82 data rows;
- 82 unique requirement IDs;
- 26 columns;
- blob SHA `1b1bd462b916ea1fbca9ba9449a8114e13011761`.

Batch 005 enumerates 17 supplemental ERX-PROT-001 candidates. Reconciliation verified that all 45 historical IDs remain present with unchanged candidate statements in the current CSV, and all 20 Batch 004 IDs are present. The 17 Batch 005 IDs are present as the current additions. Thus the controlled extraction arithmetic is **45 + 20 = 65 historical candidates; 65 + 17 = 82 current candidates**.

This reconciles the inventory lineage and IDs. It does not assert that all 82 are semantically approved, nor that extraction alone completed WP-0.7.

## 2. Historical 65 — preserved IDs

The 45 IDs below are retained from the historical canonical CSV. The 20 Batch 004 IDs are retained from its enumerated inventory. Their current canonical statements and source locators remain in `registers/requirements-traceability.csv`; no ID was renumbered or deleted.

### 2.1 Historical CSV — 45 IDs

- `ERX-REQ-UTXO-0001`
- `ERX-REQ-UTXO-0002`
- `ERX-REQ-UTXO-0003`
- `ERX-REQ-UTXO-0004`
- `ERX-REQ-UTXO-0005`
- `ERX-REQ-UTXO-0006`
- `ERX-REQ-UTXO-0007`
- `ERX-REQ-UTXO-0008`
- `ERX-REQ-UTXO-0009`
- `ERX-REQ-UTXO-0010`
- `ERX-REQ-UTXO-0011`
- `ERX-REQ-UTXO-0012`
- `ERX-REQ-OPS-0001`
- `ERX-REQ-OPS-0002`
- `ERX-REQ-INT-0001`
- `ERX-REQ-INST-0001`
- `ERX-REQ-INST-0002`
- `ERX-REQ-INST-0003`
- `ERX-REQ-KEY-0001`
- `ERX-REQ-KEY-0002`
- `ERX-REQ-ARCH-0001`
- `ERX-REQ-PRIV-0001`
- `ERX-REQ-TRANS-0001`
- `ERX-REQ-CLOSE-0001`
- `ERX-REQ-VERIFY-0001`
- `ERX-REQ-VERIFY-0002`
- `ERX-REQ-AGENT-0001`
- `ERX-REQ-AGENT-0002`
- `ERX-REQ-OTS-0001`
- `ERX-REQ-VERIFY-0003`
- `ERX-REQ-OPS-0003`
- `ERX-REQ-AVAIL-0001`
- `ERX-REQ-AVAIL-0002`
- `ERX-REQ-STATE-0001`
- `ERX-REQ-STATE-0002`
- `ERX-REQ-INV-0001`
- `ERX-REQ-INV-0002`
- `ERX-REQ-INV-0003`
- `ERX-REQ-INV-0004`
- `ERX-REQ-DATA-0001`
- `ERX-REQ-CRYPTO-0001`
- `ERX-REQ-CRYPTO-0002`
- `ERX-REQ-VERIFY-0004`
- `ERX-REQ-TRANS-0002`
- `ERX-REQ-TEST-0001`

### 2.2 Batch 004 — 20 IDs

- `ERX-REQ-ARCH-0002`
- `ERX-REQ-UTXO-0013`
- `ERX-REQ-CORE-0001`
- `ERX-REQ-CORE-0002`
- `ERX-REQ-TEST-0002`
- `ERX-REQ-TEST-0003`
- `ERX-REQ-IDENT-0001`
- `ERX-REQ-IDENT-0002`
- `ERX-REQ-KEY-0003`
- `ERX-REQ-SEC-0001`
- `ERX-REQ-OTS-0002`
- `ERX-REQ-PRIV-0002`
- `ERX-REQ-VERIFY-0005`
- `ERX-REQ-INT-0002`
- `ERX-REQ-TEST-0004`
- `ERX-REQ-TEST-0005`
- `ERX-REQ-PILOT-0001`
- `ERX-REQ-PILOT-0002`
- `ERX-REQ-HOMO-0001`
- `ERX-REQ-HOMO-0002`

## 3. Batch 005 — 17 supplemental IDs

These IDs were added in Batch 005 and are present in the current canonical CSV. Their source is ERX-PROT-001 v1.1; exact page/step locator is retained in the canonical register and Batch 005.

- `ERX-REQ-RECV-0001`
- `ERX-REQ-LOC-0001`
- `ERX-REQ-LOC-0002`
- `ERX-REQ-CONTACT-0001`
- `ERX-REQ-AGENT-0003`
- `ERX-REQ-CONTACT-0002`
- `ERX-REQ-CORR-0001`
- `ERX-REQ-TIME-0001`
- `ERX-REQ-TIME-0002`
- `ERX-REQ-OTS-0003`
- `ERX-REQ-OTS-0004`
- `ERX-REQ-PRIV-0003`
- `ERX-REQ-PRIV-0004`
- `ERX-REQ-PRIV-0005`
- `ERX-REQ-OPS-0004`
- `ERX-REQ-OPS-0005`
- `ERX-REQ-BOUND-0001`

## 4. Reconciliation checks

- Historical CSV records: 45; unique IDs: 45.
- Batch 004 distinct IDs in current register: 20.
- Batch 005 distinct IDs in current register: 17.
- Historical 65 IDs found in current canonical CSV: 65 / 65.
- Historical ID/statement changes detected in the 45-row CSV comparison: 0.
- Current canonical rows: 82; unique canonical IDs: 82.
- Reconciled lineage count: 82.

## 5. Corrected controlled interpretation

The 65 count is the earlier extraction snapshot (batches 001–004), not the current canonical total. The 82 count is the current extraction inventory after Batch 005. The 107 individual records are a linked identification/decomposition layer, not 107 additional source candidates.

The current semantic-review register's prohibition controls: do not delete, merge, renumber or silently supersede IDs. Similarity is not duplication. Any semantic correction, split or parent-child disposition must preserve source lineage and be recorded independently.

## 6. Acceptance boundary

This reconciliation closes the historical count/ID lineage discrepancy. It does **not** close:
- exact clause/diagram fidelity for all 82 candidates;
- semantic and child-level review of 107 individual records;
- modality/classification approval;
- gap owner and closure-evidence assignment;
- eight decision candidate ownership and WP-0.8 disposition;
- verification-criteria approval;
- final cross-register audit and LAEV baseline approval.

WP-0.7 remains **IN_PROGRESS — ACCEPTANCE OPEN**. No implementation or Phase 1 authorization is implied.

---
End of row-level scope reconciliation.
