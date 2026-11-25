# ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-005
## Supplemental Source-Grounded Extraction — ERX-PROT-001 v1.1

| Field | Record |
|---|---|
| Document ID | ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-005 |
| Version | 0.1.0 |
| Status | EXTRACTED — REVIEW PENDING |
| Work Package | WP-0.7 / Activity 0.7.2 |
| Date | 2026-11-25 |
| Source | ERX-PROT-001 v1.1 |
| Inspection basis | Direct inspection of the supplied 29-page PDF, including page-level text and source page locators |
| Canonical register | registers/requirements-traceability.csv |

## 1. Purpose and boundary

This supplemental batch records independently locatable source statements that were present in the foundational Protocol but not represented as distinct candidate records in batches 001–004. It adds no new technical decisions. Statements remain source-derived candidates, not approved requirements. Classification, mandatory status, design assessment, phase allocation and verification remain reserved for their corresponding WP-0.7 activities.

## 2. Candidate inventory

| Requirement ID | Candidate statement | Source locator |
|---|---|---|
| ERX-REQ-RECV-0001 | The JSON 01 reception record includes the unique event ID, call ID, telephone-session ID, receiving gateway, reception source, observation time, available technical references and available origin information. | ERX-PROT-001 v1.1, PDF p.8, Step 1 |
| ERX-REQ-LOC-0001 | Each location datum records its source, observation time, coordinates when available, estimated precision, location method and validation state. | ERX-PROT-001 v1.1, PDF p.9, Step 4 |
| ERX-REQ-LOC-0002 | Absence of location does not block the call; subsequent location changes are recorded as new events and do not modify the original JSON 01. | ERX-PROT-001 v1.1, PDF p.9, Step 4 |
| ERX-REQ-CONTACT-0001 | Initial call-reception time and agent-response time are recorded as distinct events. | ERX-PROT-001 v1.1, PDF p.11, Step 10 |
| ERX-REQ-AGENT-0003 | Professional-agent verification records an explicit result; lack of authentication does not stop emergency attention, and a pending identity is never represented as verified. | ERX-PROT-001 v1.1, PDF p.12, Step 11 |
| ERX-REQ-CONTACT-0002 | The contact result represents whether human contact was established, response without verifiable authentication, no response, transfer, termination before response or a technical exception; it must not represent human attention that did not occur. | ERX-PROT-001 v1.1, PDF p.12, Step 13 |
| ERX-REQ-CORR-0001 | Signed and committed JSON 01, JSON 02 and JSON 03 documents remain immutable; a correction is recorded in a signed complementary document linked to the original with its reason, and the historical record remains reconstructable. | ERX-PROT-001 v1.1, PDF pp.18, 21–22, §§10.9 and 14 |
| ERX-REQ-TIME-0001 | ERX distinguishes device-declared, gateway-observed, institutionally received, processed, signed, OTS-submitted and verifiably anchored times. | ERX-PROT-001 v1.1, PDF p.18, §11 |
| ERX-REQ-TIME-0002 | Times are retained in UTC with precision and source; local monotonic time is also recorded for session ordering when supported, and discrepancies are documented rather than silently corrected. | ERX-PROT-001 v1.1, PDF p.19, §11 |
| ERX-REQ-OTS-0003 | Each JSON document has an independent cryptographic commitment; the evidence workflow completes, freezes, canonicalizes and signs the document, calculates its commitment, requests OTS, retains and later updates the proof, and verifies it against the document and Bitcoin chain. | ERX-PROT-001 v1.1, PDF pp.19–20, §12 |
| ERX-REQ-OTS-0004 | OTS evidence is not treated as proof that content is true, a person’s identity is genuine, an agent acted correctly, a location is exact, audio is complete, a center is authorized or an event occurred at the exact second claimed. | ERX-PROT-001 v1.1, PDF p.20, §12.3 |
| ERX-REQ-PRIV-0003 | Original call content and sensitive personal data remain in protected institutional infrastructure; Bitcoin and OTS receive cryptographic commitments rather than private call content, and sensitive direct identifiers are not published. | ERX-PROT-001 v1.1, PDF p.20, §13 |
| ERX-REQ-PRIV-0004 | ERX avoids exposing direct identifiers, isolated hashes of personal data and unnecessary metadata; where applicable it uses high-entropy random commitments or equivalent cryptographic structures against enumeration, with verification information under authorized control. | ERX-PROT-001 v1.1, PDF p.21, §13.1 |
| ERX-REQ-PRIV-0005 | The institution defines retention periods and deletion procedures under applicable law; authorized deletion of content is not represented as deletion of an already published Bitcoin anchor, and minimum information is retained to explain the evidence and applied policy. | ERX-PROT-001 v1.1, PDF p.21, §13.2 |
| ERX-REQ-OPS-0004 | When identity services are unavailable, the call continues and identity remains pending or unverified until checked; pending validation is not converted by default into successful authentication. | ERX-PROT-001 v1.1, PDF p.24, §16.10 |
| ERX-REQ-OPS-0005 | During ERX unavailability, where technically possible, events are retained in a durable protected local queue; recovery preserves original event time, recovery time and commitment-generation time separately. | ERX-PROT-001 v1.1, PDF p.24, §16.8 |
| ERX-REQ-BOUND-0001 | ERX does not replace the emergency number, telephone network, dispatch system, professional judgment of agents or public-authority competencies; each installation retains institutional independence and legal responsibilities. | ERX-PROT-001 v1.1, PDF p.28, §20 |

## 3. Source-fidelity and duplication controls

- The candidate statements above summarize source passages; they are not quotations.
- The candidates are separated where they produce independently inspectable outcomes, including location metadata versus non-blocking location absence, timestamp categories versus timestamp normalization, and OTS evidence workflow versus OTS probative limits.
- Existing records covering general privacy, OTS non-interference, agent authentication, corrections, recovery and product boundaries may overlap. Their IDs are retained pending WP-0.7.3 semantic disposition; no automatic merge is authorized.
- The source's conditional phrases (for example, “when supported”, “where applicable”, and “where technically possible”) are retained and must not be strengthened during later normalization.
- The technical response to ERX-ROADMAP-001 was not used to add mandatory statements.

## 4. Result

This batch adds 17 source-derived candidate records. The extraction inventory rises from 65 to 82 candidates, subject to successful incorporation and structural validation in the canonical CSV. All records remain EXTRACTED — REVIEW PENDING. This batch closes only an additional extraction pass; it does not close WP-0.7.3–0.7.11 or authorize Phase 1.

## 5. Next extraction controls

Before declaring activity 0.7.2 complete, reconcile these 17 IDs against the canonical register, validate uniqueness and exact source locators, verify diagram-derived candidates against the Atlas images, and record an explicit completeness statement for the bounded five-source baseline. The Atlas must be visually reviewed; its text extraction alone does not establish diagram completeness.

---
End of ERX-WP-0.7-REQUIREMENT-EXTRACTION-BATCH-005
