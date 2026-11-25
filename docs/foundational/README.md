# FOUNDATIONAL SOURCE FILES — CUSTODY README

## Purpose and actual repository location

This document records custody rules for the immutable original source PDFs used by ERX byLAEV.

**Current as-built location:** the five original PDFs in the accepted WP-0.2 baseline are stored directly under the repository's `docs/` directory, preserving their supplied filenames. They are not stored inside `docs/foundational/`. The `docs/foundational/` directory contains registers, custody guidance and derivative evidence.

## Rules

- Preserve original source files byte-for-byte; do not edit, re-export, translate, or rename them.
- Preserve the original supplied filename.
- Record the document's internal identifier and version separately from its filename.
- Use the accepted WP-0.2 completion dossier as the controlling SHA-256 and Git blob identity evidence for the five baseline PDFs.
- Store translations, OCR output, extracts, annotations, and derivative documents separately from original binaries.
- Never treat a derivative as a replacement for its source.
- Any later-discovered source must be recorded as a supplemental discovery; do not silently rewrite the accepted five-file WP-0.2 baseline.

## Registers and evidence

The five-source baseline and source metadata are recorded in:

- `docs/foundational/ERX-FOUNDATIONAL-MATERIAL-REGISTER-001.md`
- `registers/foundational-material-register.csv`
- `docs/phase-0/ERX-WP-0.2-COMPLETION-DOSSIER-001.md`

The SHA-256 values and Git blob identities recorded in the accepted WP-0.2 dossier remain the controlling integrity evidence. This README corrects the previous location statement; it does not independently re-hash the binary files.

---
Custody README — metadata not assigned
