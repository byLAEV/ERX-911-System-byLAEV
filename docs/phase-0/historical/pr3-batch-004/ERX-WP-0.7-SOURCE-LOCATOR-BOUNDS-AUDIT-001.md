# ERX-WP-0.7-SOURCE-LOCATOR-BOUNDS-AUDIT-001
## Preliminary source locator integrity check — 56 candidates

| Field | Value |
|---|---|
| Document ID | ERX-WP-0.7-SOURCE-LOCATOR-BOUNDS-AUDIT-001 |
| Version | 0.1.0 |
| Status | PRELIMINARY BOUNDS AUDIT — NOT FINAL SOURCE VERIFICATION |
| Date | 2026-11-25 |
| Register baseline | requirements-traceability.csv, 56 records |

## 1. Scope

This pass checks that each candidate's cited source ID maps to the inspected foundational PDF and that the page number(s) written in its locator fall within that PDF's physical page count. It is a mechanical bounds check, not proof that the exact cited clause supports the entire candidate wording. Exact passage, section, diagram and normative-modality confirmation remains required before SOURCE_VERIFIED or APPROVED status.

## 2. Inspected source page counts

| Source | Version | PDF page count |
|---|---:|---:|
| ERX-PROT-001 | 1.1 | 29 |
| ERX-ATLAS-001 | 1.1 | 29 |
| UTXO-911-001 | 1.0 | 12 |
| ERX-ROADMAP-001 | 1.0 | 37 |

## 3. Candidate locator results

| Requirement ID | Source | Locator | Pages parsed | Result |
|---|---|---|---|---|
| ERX-REQ-UTXO-0001 | ERX-PROT-001 | PDF p.3 | 3 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0002 | ERX-PROT-001 | PDF p.3, Section 2.1 | 3 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0003 | ERX-PROT-001 | PDF p.3, Section 2.1 | 3 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0004 | ERX-PROT-001 | PDF p.3, Section 2.2 | 3 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0005 | ERX-PROT-001 | PDF p.4 | 4 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0006 | ERX-PROT-001 | PDF p.10 | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0007 | ERX-PROT-001 | PDF p.10, Step 7 | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0008 | ERX-PROT-001 | PDF p.10, Step 8 | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0009 | ERX-PROT-001 | PDF p.17, Sections 10.1–10.5 | 17 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0010 | ERX-PROT-001 | PDF p.17, Section 10.6 | 17 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0011 | UTXO-911-001 | PDF p.10, Principle of single spend | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-UTXO-0012 | UTXO-911-001 | PDF p.11, OTS function | 11 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0001 | ERX-PROT-001 | PDF p.25, Section 17.1 | 25 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0002 | ERX-PROT-001 | PDF p.24, Section 16.9 | 24 | PAGE_BOUNDS_VALID |
| ERX-REQ-INT-0001 | ERX-ROADMAP-001 | PDF p.23, Section 8.1 | 23 | PAGE_BOUNDS_VALID |
| ERX-REQ-INST-0001 | ERX-PROT-001 | PDF pp.5–6, Section 4 | 5, 6 | PAGE_BOUNDS_VALID |
| ERX-REQ-INST-0002 | ERX-PROT-001 | PDF p.6, Section 4.1 | 6 | PAGE_BOUNDS_VALID |
| ERX-REQ-INST-0003 | ERX-PROT-001 | PDF p.6, Section 4.1 | 6 | PAGE_BOUNDS_VALID |
| ERX-REQ-KEY-0001 | ERX-PROT-001 | PDF p.6, Section 4.2 | 6 | PAGE_BOUNDS_VALID |
| ERX-REQ-KEY-0002 | ERX-PROT-001 | PDF p.7, Section 4.2 | 7 | PAGE_BOUNDS_VALID |
| ERX-REQ-ARCH-0001 | ERX-PROT-001 | PDF p.8, Section 4.3 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-PRIV-0001 | ERX-PROT-001 | PDF pp.14–15, Step 18 | 14, 15 | PAGE_BOUNDS_VALID |
| ERX-REQ-TRANS-0001 | ERX-PROT-001 | PDF pp.15–16, Step 19 | 15, 16 | PAGE_BOUNDS_VALID |
| ERX-REQ-CLOSE-0001 | ERX-PROT-001 | PDF p.16, Step 20 | 16 | PAGE_BOUNDS_VALID |
| ERX-REQ-VERIFY-0001 | ERX-PROT-001 | PDF pp.21–23, Section 7 | 21, 22, 23 | PAGE_BOUNDS_VALID |
| ERX-REQ-VERIFY-0002 | ERX-PROT-001 | PDF p.24, Section 7.3 | 24 | PAGE_BOUNDS_VALID |
| ERX-REQ-AGENT-0001 | ERX-ATLAS-001 | PDF pp.7–8, Lámina 03 | 7, 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-AGENT-0002 | ERX-ATLAS-001 | PDF p.8, Lámina 03 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-OTS-0001 | ERX-ATLAS-001 | PDF p.19, Lámina 06 | 19 | PAGE_BOUNDS_VALID |
| ERX-REQ-VERIFY-0003 | ERX-ATLAS-001 | PDF pp.27–28, verifier categories | 27, 28 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0003 | UTXO-911-001 | PDF p.7, Section 4.2 | 7 | PAGE_BOUNDS_VALID |
| ERX-REQ-AVAIL-0001 | UTXO-911-001 | PDF pp.9–10, availability lifecycle | 9, 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-AVAIL-0002 | UTXO-911-001 | PDF pp.9–11, Sections 5–8 | 9, 10, 11 | PAGE_BOUNDS_VALID |
| ERX-REQ-STATE-0001 | ERX-ROADMAP-001 | PDF pp.6–7, Sections 1.2–1.3 | 6, 7 | PAGE_BOUNDS_VALID |
| ERX-REQ-STATE-0002 | ERX-ROADMAP-001 | PDF p.7, Section 1.3 | 7 | PAGE_BOUNDS_VALID |
| ERX-REQ-INV-0001 | ERX-ROADMAP-001 | PDF p.8, Section 1.5 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-INV-0002 | ERX-ROADMAP-001 | PDF p.8, Section 1.5 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-INV-0003 | ERX-ROADMAP-001 | PDF p.8, Section 1.5 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-INV-0004 | ERX-ROADMAP-001 | PDF p.8, Section 1.5 | 8 | PAGE_BOUNDS_VALID |
| ERX-REQ-DATA-0001 | ERX-ROADMAP-001 | PDF p.9, Section 2.1 | 9 | PAGE_BOUNDS_VALID |
| ERX-REQ-CRYPTO-0001 | ERX-ROADMAP-001 | PDF p.10, Section 2.3 | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-CRYPTO-0002 | ERX-ROADMAP-001 | PDF p.10, Section 2.4 | 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-VERIFY-0004 | ERX-ROADMAP-001 | PDF p.21, Section 7 | 21 | PAGE_BOUNDS_VALID |
| ERX-REQ-TRANS-0002 | ERX-ROADMAP-001 | PDF pp.23–24, Section 8.2 | 23, 24 | PAGE_BOUNDS_VALID |
| ERX-REQ-TEST-0001 | ERX-ROADMAP-001 | PDF p.24, Section 9.1 | 24 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0004 | ERX-PROT-001 | PDF p.25, §16.8 | 25 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0005 | ERX-PROT-001 | PDF p.26, §17.2 | 26 | PAGE_BOUNDS_VALID |
| ERX-REQ-OPS-0006 | ERX-PROT-001 | PDF p.25, §16.9 | 25 | PAGE_BOUNDS_VALID |
| ERX-REQ-SEC-0001 | ERX-PROT-001 | PDF p.26, §17.3 | 26 | PAGE_BOUNDS_VALID |
| ERX-REQ-ARCH-0002 | ERX-PROT-001 | PDF p.26, §19 | 26 | PAGE_BOUNDS_VALID |
| ERX-REQ-TEST-0002 | ERX-PROT-001 | PDF p.26, §19.1 | 26 | PAGE_BOUNDS_VALID |
| ERX-REQ-PRIV-0002 | ERX-ATLAS-001 | PDF pp.25–26, Lámina 08 | 25, 26 | PAGE_BOUNDS_VALID |
| ERX-REQ-VERIFY-0005 | ERX-ATLAS-001 | PDF p.28, Categorías de verificación | 28 | PAGE_BOUNDS_VALID |
| ERX-REQ-AVAIL-0003 | ERX-ROADMAP-001 | PDF pp.4–5, §3.1 | 4, 5 | PAGE_BOUNDS_VALID |
| ERX-REQ-INV-0005 | UTXO-911-001 | PDF pp.9–10, §§5–6 | 9, 10 | PAGE_BOUNDS_VALID |
| ERX-REQ-OTS-0002 | UTXO-911-001 | PDF p.11, §7 | 11 | PAGE_BOUNDS_VALID |

## 4. Findings and limits

- Candidates checked: 56.
- Locators with page numbers within the mapped PDF bounds: 56.
- Locators requiring review because the source mapping or page bounds could not be established: 0.
- A page-bounds pass does not establish that the excerpt is exact, that the section number is correct, or that a diagram is normative.
- Atlas-derived candidates require an explicit check against the visual/diagram and the corresponding prose in ERX-PROT-001 where applicable.
- Any candidate combining several obligations still requires an independent-verifiability review.
- No lifecycle status or approval field is changed by this audit.

## 5. Next source-verification work

1. Open each cited page and confirm the exact paragraph, table, diagram or section.
2. Compare the source's normative wording with the candidate's disposition.
3. Record exact evidence excerpts or faithful summaries.
4. Record conflicts, ambiguities and conditional scope.
5. Only after review may a candidate move from EXTRACTED to SOURCE_VERIFIED or IN_REVIEW under the method's lifecycle controls.

---
End of ERX-WP-0.7-SOURCE-LOCATOR-BOUNDS-AUDIT-001
