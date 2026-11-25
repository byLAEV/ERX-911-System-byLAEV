# ERX-DOCUMENT-HIERARCHY-MATRIX-001
## Document Hierarchy and Classification Matrix

| Field | Value |
|---|---|
| Document ID | ERX-DOCUMENT-HIERARCHY-MATRIX-001 |
| Version | 1.0.0 |
| Status | APPROVED — WP-0.3 |
| Work Package | WP-0.3 / Activities 0.3.1–0.3.3 |
| Project | ERX-911-System-byLAEV |
| Design and Approval Authority | LAEV |
| Evidence baseline | Five foundational PDFs inspected; WP-0.2 accepted in Workplan 2026-11-23 |
| Date | 2026-11-24 |

## 1. Purpose and limits
This matrix records the approved document classification and scoped governance hierarchy adopted by LAEV under decision record v1.0.0. It is not a universal precedence rule. A hierarchy level describes governance function and control, not an automatic power to override every document in a lower level.

## 2. Classification of the current source set

| ID | Document | Stated version | Class | Source basis / limit |
|---|---|---:|---|---|
| FND-001 | ERX-PROT-001 — Institutional Protocol | 1.1 | Foundational normative protocol source | Title/control metadata and Sections 1–16; defines the institutional communication protocol and mandatory uniqueness controls |
| FND-002 | ERX-ATLAS-001 — Institutional Atlas | Internal 1.1; supplied filename says v1 | Foundational graphical/operational representation | Control section identifies ERX-PROT-001 v1.1 as related normative document; plates 01–08 and correspondence table |
| FND-003 | UTXO-911-001 — UTXO de Comunicación 911 | 1.0 | Foundational functional UTXO source | Sections 1–8; describes communication UTXO stages and an additional agent-availability state cycle |
| FND-004 | ERX-ROADMAP-001 — Master Phase Plan | 1.0 | Foundational project planning source | 37-page roadmap; phase sequence, dependencies, deliverables and gates |
| FND-005 | Response to observations on ERX-ROADMAP-001 | Not stated | Technical response / review artifact | Two-page response; no formal ID, version or issue date stated in inspected control information |
| REF-001 | ERX-CONSENSUS-001 | 0.1 | Identity/content confirmed from text source; proposal for review | `docs/Consenso ERX byLAEV` text source directly matches Roadmap citation; operational completeness and authority are DOC-ISS-011 |
| REF-002 | ERX-IMPL-PROPOSAL-001 | Not stated | Referenced but not located | Roadmap reference only; content and provenance unverified |

## 3. Proposed governance hierarchy — decision required

| Level | Class | Included records | Governing effect | Limit |
|---|---|---|---|---|
| A | Project mandate and governance | LAEV-approved Charter, expressly approved project decisions, and an approved Workplan or approved amendments only after their express approval | Controls project scope, authorization, responsibilities and acceptance within the approved scope | Does not silently rewrite technical protocol content |
| B | Foundational sources and supporting review artifacts | FND-001 through FND-004 are the foundational protocol, graphical, functional and planning sources. FND-005 is included only as a supporting technical response/review artifact associated with FND-004. | FND-001–FND-004 establish the source and planning baseline. FND-005 records recommendations and technical positions only. | FND-005 does not amend the Roadmap or acquire normative authority without express approval. No universal precedence among FND-001–FND-004 is assumed |
| C | Approved derivative specifications and decisions | Approved requirements, ADRs, detailed specifications, controlled amendments and procedures | Elaborates or changes a source only within expressly approved scope and traceability | Must cite source versions and approval; cannot rely on publication alone |
| D | Working, implementation and verification artifacts | Drafts, working registers, code, configurations, tests, audit evidence and reports | Supports development, execution and verification | Does not become normative or amend a source by mere existence or commit |

**Important distinction:** Level D combines different artifact types for governance purposes. A later detailed document-control policy may split working drafts, implementation artifacts and verification evidence into separate classes without changing the core rule that none silently amends a source.

## 4. Classification rules
1. Classification is based on the document's stated purpose, contents, and provenance.
2. A document can have a primary class and secondary subject tags.
3. A document's date, filename, folder location, or Git commit does not alone establish authority.
4. A referenced but unavailable document remains unverified and is not assigned inferred content.
5. A technical response is not an amendment unless an approval record explicitly makes it one.
6. The Atlas filename/internal version discrepancy must be preserved as metadata, not silently normalized here.

## 5. Approval and maintenance evidence
The hierarchy was adopted by LAEV in ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0. The master index and document register shall be reconciled during WP-0.6. FND-005 remains a response/review artifact; REF-001 remains a proposal; REF-002 remains a bounded not-located reference.

## 6. Current disposition
**APPROVED — WP-0.3.** LAEV adopted the scoped hierarchy and classification in ERX-WP-0.3-LAEV-DECISION-RECORD-001 v1.0.0 (2026-11-24). This approval does not authorize Phase 1, implementation, or production operation.

---
END
