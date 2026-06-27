# documentation-governance skill

## Background

Software project documentation becomes hard to maintain when agents treat every task as a reason to append more text. The failure mode is not missing prose; it is weak information architecture: current truth, proposed change, decision rationale, evidence, process logs, raw references, and archives get mixed together.

The existing `documentation-and-adrs` skill covers useful writing practices for ADRs, comments, README, API docs, and changelogs. It does not provide a hard governance layer for deciding whether to write, where to write, how to avoid duplicate truth, and when to use OpenSpec-style change specs versus ADRs versus formal source-of-truth docs.

## Goal

Add a reusable `documentation-governance` skill for software engineering projects. The skill should make documentation routing explicit before writing and should prevent temporary process notes, debugging chronology, raw command output, and sub-agent transcripts from polluting formal docs.

## Design

- Add `skills/documentation-governance/SKILL.md` with a mandatory Documentation Governance Gate.
- Add `references/document-taxonomy.md` for artifact taxonomy and directory split principles.
- Add `references/routing-decisions.md` for OpenSpec/change spec, ADR, formal docs, traceability, and status-header rules.
- Add `references/governance-review-checklist.md` for steelman counter-review and evidence hygiene.
- Update repository README and docs index so the new skill is discoverable and installable.

## Core Decisions

- Treat OpenSpec/change specs as the proposed or active change layer, not as permanent current-state documentation.
- Treat ADRs as accepted decision rationale, not task plans or implementation logs.
- Treat formal docs as current source of truth for product behavior, architecture, API contracts, operations, and engineering rules.
- Treat delivery reports and explicitly approved audit/evidence artifacts as outcome and evidence surfaces, not product or architecture truth.
- Treat deprecation, supersession, archiving, and deletion as explicit lifecycle actions, not afterthoughts.
- Treat unified maintenance as unified discovery, status, owner, update trigger, traceability, and validation; do not merge everything into one large document.
- Treat searchability and modification cost as first-class design constraints: canonical docs need predictable paths, searchable names/headings, index aliases, and one edit location per durable fact.
- Prefer one canonical home per durable fact; indexes may summarize and link, but should not duplicate full content.
- Use owner, lifecycle, status, update trigger, source links, and supersession links to preserve traceability without storing process logs.
- Split bloated docs by lifecycle, audience, domain, owner, or source-of-truth responsibility, not by agent session or date by default.

## Steelman Counter-Review

### Objection: This could create more process overhead for small doc edits.

Response: The gate is intentionally short. Tiny typo fixes and obvious index updates can compress it mentally or in one sentence. The full review checklist is only required when creating a new long-lived doc, reorganizing docs, or changing documentation policy.

### Objection: Refusing process logs may hide important accountability.

Response: The skill does not forbid audit trails. It routes them to approved report/evidence locations and requires labels, evidence scope, and redaction. It forbids storing them as current product, architecture, or governance truth.

### Objection: OpenSpec, ADR, and formal docs may overlap in real projects.

Response: The skill separates the question each artifact answers: proposed change and acceptance, accepted rationale, and current truth. It allows project-specific names and equivalents such as RFCs or design specs.

### Objection: A default docs taxonomy may conflict with existing repository conventions.

Response: Existing repository conventions take precedence. The taxonomy is a fallback and method for chaotic projects, not a universal folder mandate.

### Objection: Single-file growth rules could cause over-splitting.

Response: The rule explicitly says line count is only an alarm. Split decisions depend on audience, lifecycle, owner, update trigger, source-of-truth responsibility, and reader discoverability.

### Objection: More structure can make docs harder to find and harder to update.

Response: The skill now treats searchability and modification cost as explicit gate fields. A split is not valid unless the canonical answer remains discoverable and future changes have a small edit surface.

## Acceptance

- `documentation-governance` validates with `quick_validate.py`.
- Repository skill discovery lists the new skill.
- README includes install commands and smoke checks.
- docs index links this design record and the new skill.
- Steelman review confirms the skill distinguishes OpenSpec, ADR, formal docs, reports, approved audit/evidence artifacts, archives, deprecation, deletion, and "write nothing".
