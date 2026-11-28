#!/usr/bin/env python3
"""Deterministic acceptance gate for ERX WP-0.7.5.

This validator does not decide whether a source is normative. It checks that
human-reviewed dispositions and their supporting evidence have been recorded
for every source candidate and individual record before the Workplan check can
be changed to [x].
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "registers/wp-0.7.5-source-fidelity-review.csv"
INDIVIDUAL = ROOT / "registers/wp-0.7.5-individual-semantic-review.csv"
EXPECTED_SOURCE_ROWS = 82
EXPECTED_INDIVIDUAL_ROWS = 107
ALLOWED_MODALITIES = {
    "MANDATORY_CANDIDATE",
    "NOT_MANDATORY",
    "RECOMMENDATION_CANDIDATE",
}


def load(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def nonempty(row: dict[str, str], field: str) -> bool:
    return bool((row.get(field) or "").strip())


def accepted(value: str) -> bool:
    return (value or "").strip().upper().startswith("VERIFIED")


def audit() -> list[str]:
    errors: list[str] = []
    try:
        source = load(SOURCE)
        individual = load(INDIVIDUAL)
    except (OSError, csv.Error) as exc:
        return [f"Cannot read review registers: {exc}"]

    if len(source) != EXPECTED_SOURCE_ROWS:
        errors.append(f"Source register: expected {EXPECTED_SOURCE_ROWS} rows, found {len(source)}.")
    if len(individual) != EXPECTED_INDIVIDUAL_ROWS:
        errors.append(f"Individual register: expected {EXPECTED_INDIVIDUAL_ROWS} rows, found {len(individual)}.")

    source_ids = [r.get("requirement_id", "").strip() for r in source]
    individual_ids = [r.get("individual_requirement_id", "").strip() for r in individual]
    if len(set(source_ids)) != len(source_ids) or not all(source_ids):
        errors.append("Source candidate IDs are missing or duplicated.")
    if len(set(individual_ids)) != len(individual_ids) or not all(individual_ids):
        errors.append("Individual requirement IDs are missing or duplicated.")

    source_id_set = set(source_ids)
    for row in source:
        rid = row.get("requirement_id", "<missing ID>")
        for field in ("source_id", "source_version", "source_locator",
                      "normalized_requirement_statement", "source_excerpt_or_faithful_summary",
                      "review_rationale"):
            if not nonempty(row, field):
                errors.append(f"{rid}: missing {field}.")
        modality = (row.get("modality_disposition") or "").strip()
        if modality not in ALLOWED_MODALITIES:
            errors.append(f"{rid}: unresolved/unsupported modality disposition '{modality}'.")
        if not accepted(row.get("source_fidelity_disposition", "")):
            errors.append(f"{rid}: exact source/Atlas fidelity is not VERIFIED.")
        if (row.get("approval_state") or "").strip() != "NOT_APPROVED_BY_WP-0.7.5":
            errors.append(f"{rid}: approval boundary changed or is missing.")

    for row in individual:
        rid = row.get("individual_requirement_id", "<missing ID>")
        parent = (row.get("parent_candidate_id") or "").strip()
        if parent not in source_id_set:
            errors.append(f"{rid}: parent candidate '{parent}' does not resolve.")
        for field in ("source_id", "source_version", "source_locator",
                      "individual_statement", "source_evidence_summary", "review_rationale"):
            if not nonempty(row, field):
                errors.append(f"{rid}: missing {field}.")
        modality = (row.get("modality_disposition") or "").strip()
        if modality not in ALLOWED_MODALITIES:
            errors.append(f"{rid}: unresolved/unsupported modality disposition '{modality}'.")
        if not accepted(row.get("semantic_fidelity_disposition", "")):
            errors.append(f"{rid}: child semantic/source fidelity is not VERIFIED.")
        for field in ("condition_scope_check", "actor_trigger_outcome_check"):
            if (row.get(field) or "").strip().upper() != "PASS":
                errors.append(f"{rid}: {field} is not PASS.")
        if (row.get("approval_state") or "").strip() != "NOT_APPROVED_BY_WP-0.7.5":
            errors.append(f"{rid}: approval boundary changed or is missing.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="Print concise gate result.")
    args = parser.parse_args()
    errors = audit()
    if errors:
        print("WP-0.7.5 ACCEPTANCE GATE: BLOCKED")
        print(f"Outstanding validation findings: {len(errors)}")
        if not args.summary:
            for item in errors:
                print(f"- {item}")
        return 1
    print("WP-0.7.5 ACCEPTANCE GATE: PASS")
    print("82/82 source candidates and 107/107 individual records have verified evidence.")
    print("This is a technical gate result; LAEV's formal acceptance remains separately required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
