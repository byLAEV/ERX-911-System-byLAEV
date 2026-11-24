# ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001
## Exact-Byte Preservation Procedure for Foundational PDF Sources

| Field | Value |
|---|---|
| Document ID | ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001 |
| Version | 0.1.0 |
| Status | WORKING PROCEDURE — NOT APPROVED |
| Work Package | WP-0.2 |
| Project | ERX byLAEV — 911 Double-Spend System |
| Date | 2026-11-23 |

## 1. Purpose

This procedure defines a reproducible method for placing the five supplied foundational PDF files into the ERX Git repository without changing their bytes, and for verifying the resulting repository objects against the SHA-256 values recorded in ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.

This procedure is a working instruction. It does not assert that archival has occurred.

## 2. Preservation Requirements

- Preserve the exact original bytes.
- Preserve each supplied filename, including the leading `### ` in the Roadmap filename.
- Do not print-to-PDF, optimize, OCR, translate, annotate, or re-export the originals.
- Do not substitute a newly generated PDF for an original.
- Keep derivative files outside the original-source directory.
- Verify SHA-256 before and after committing.
- Record the commit SHA and final repository path in the register.

## 3. Required Repository Paths

| Original supplied filename | Repository path |
|---|---|
| `ERX byLAEV 1.pdf` | `docs/foundational/originals/ERX byLAEV 1.pdf` |
| `ERX-ATLAS-001 v1.pdf` | `docs/foundational/originals/ERX-ATLAS-001 v1.pdf` |
| `UTXO DE COMUNICACIÓN 911 byLAEV.pdf` | `docs/foundational/originals/UTXO DE COMUNICACIÓN 911 byLAEV.pdf` |
| `### ERX-ROADMAP-001.pdf` | `docs/foundational/originals/### ERX-ROADMAP-001.pdf` |
| `Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` | `docs/foundational/originals/Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf` |

## 4. Pre-Commit Integrity Check

Run from a working directory containing the five original files:

```bash
sha256sum \
  "ERX byLAEV 1.pdf" \
  "ERX-ATLAS-001 v1.pdf" \
  "UTXO DE COMUNICACIÓN 911 byLAEV.pdf" \
  "### ERX-ROADMAP-001.pdf" \
  "Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf"
```

Expected SHA-256 values:

```text
ERX byLAEV 1.pdf
5e1647c30f1aae77726619272c7730306b2e7c138e920cf8be91542e1ee77fbd

ERX-ATLAS-001 v1.pdf
7029d5f5cabeedd783eb5fec6cf66ddafa7e224c16ef7644656e89dd7921ec7f

UTXO DE COMUNICACIÓN 911 byLAEV.pdf
39fa464f8ec774bf55f50e7d042c19728e2467be2bbb7234b15142a89321c4cc

### ERX-ROADMAP-001.pdf
b529fb306c19704bd163ed3a26f9d9b737057415a6d5839056f394791fdadca3

Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf
1b8bd77ac2b7789269d6152d172fbb301d3609fc2db223aa1e4b8ed35884fba9
```

If any value differs, STOP. Do not commit the mismatched file. Reacquire the exact original or investigate the discrepancy.

## 5. Copy and Commit

After all five pre-commit hashes match:

```bash
mkdir -p docs/foundational/originals
cp --preserve=mode,timestamps -- \
  "ERX byLAEV 1.pdf" \
  "ERX-ATLAS-001 v1.pdf" \
  "UTXO DE COMUNICACIÓN 911 byLAEV.pdf" \
  "### ERX-ROADMAP-001.pdf" \
  "Respuesta técnica a las observaciones de ERX-ROADMAP-001.pdf" \
  docs/foundational/originals/

git add docs/foundational/originals/
git diff --cached --stat
git diff --cached --name-only
git commit -m "docs(wp-0.2): preserve original foundational PDF sources"
git push origin main
```

Review the staged filenames before committing. Do not add unrelated or derivative files to this archival commit.

## 6. Post-Commit Verification

After push, verify the files from a fresh repository checkout:

```bash
git fetch origin
git checkout main
sha256sum docs/foundational/originals/*.pdf
```

Compare each checksum to Section 4 and the foundational material register. The verification is successful only if all five exact values match.

Also record:
- Repository URL.
- Commit SHA containing the five files.
- Repository path for each source.
- Date and identity of the person who performed verification.
- Result for each hash: MATCH or MISMATCH.

## 7. Register Update

Update `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md` and `registers/foundational-material-register.csv` only after post-commit verification.

For each source, record the repository path, archival commit SHA, and verified hash result. Do not mark a file ARCHIVED or VERIFIED before that evidence exists.

## 8. Operational Limitation in Current Session

The GitHub integration exposes Git Data API operations capable of creating blobs with Base64 encoding. However, the current execution boundary does not provide a direct file-byte-to-tool-payload transfer from the mounted local PDF files into those operations. Therefore, this session has not uploaded the PDFs. A local Git push or another authorized binary upload path is required to complete the operation.

## 9. WP-0.2 Acceptance Boundary

WP-0.2 remains IN_PROGRESS until:
1. All five originals are committed at the paths above.
2. Post-commit SHA-256 verification matches all five registered values.
3. ERX-CONSENSUS-001 v0.1 and ERX-IMPL-PROPOSAL-001 are located and inventoried, or their unavailability is formally dispositioned by LAEV.
4. The register is complete enough for review.
5. LAEV reviews and expressly approves the inventory.

Publication of this procedure is not evidence of archival and does not close WP-0.2 or Phase 0.

---
End of ERX-FOUNDATIONAL-ARCHIVE-PROCEDURE-001
