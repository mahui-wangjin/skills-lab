---
name: documentation-governance
description: Use when creating, changing, reorganizing, auditing, or deciding not to write software project documentation; when choosing between OpenSpec/change specs, ADRs, source-of-truth docs, README/index files, source-adjacent docs, delivery reports, approved audit/evidence artifacts, archives, or no durable artifact; or when docs are growing chaotic, duplicated, stale, process-heavy, hard to trace, or too large.
---

# Documentation Governance

## Overview

Govern documentation as a maintainable information architecture, not as a place to put everything the agent did. Every durable doc must have a purpose, owner, lifecycle, trace path, and reason to exist.

This skill complements `documentation-and-adrs`: use that skill for writing good ADRs and explanatory docs; use this skill before deciding whether a document should exist, where it belongs, how it stays current, and what must not be written.

## Core Rule

Do not write documentation until the content has passed the routing gate.

The default is not "write a new doc." The default is:

1. update the existing source of truth,
2. link from the index,
3. archive or supersede stale material,
4. or write nothing durable when the content is temporary process noise.

## Documentation Governance Gate

Before creating or editing durable documentation, emit this concise gate:

```md
### Documentation Governance Gate

- Content: <fact / decision / proposal / contract / guide / evidence / process note>
- Lifespan: <temporary / active-change / durable-current / historical>
- Audience: <developers / operators / product / reviewers / agents / users>
- Source of truth: <existing doc/path or new owner>
- Destination: <OpenSpec/change spec / ADR / formal docs / README-index / source-adjacent / report evidence / approved audit/evidence artifact / archive / nowhere durable>
- Update vs create: <update existing / create new / archive / do not persist>
- Traceability: <links to issue/spec/ADR/code/report or why none>
- Growth check: <will this bloat an existing file? split/index/archive decision>
- Searchability: <how a reader or agent will find the canonical answer>
- Change cost: <how many docs must change when this fact changes>
- Verification: <link check, doc governance check, review, generated docs, or manual inspection>

### Decision

- Write now: <yes / no / only after missing owner/path is defined>
- Required action: <one next action>
```

Keep this gate short. It is a decision aid, not a process record.

## Routing Summary

Use the detailed matrix in `references/document-taxonomy.md` when the destination is not obvious.

| Destination | Use when | Do not use for |
| --- | --- | --- |
| OpenSpec or change spec | A proposed or active change needs scope, acceptance, contracts, staged work, or review before it becomes current truth. | Already accepted architecture rationale or current-state docs. |
| ADR | A significant decision has been accepted and records trade-offs, alternatives, consequences, and supersession history. | Task plans, implementation logs, or every small preference. |
| Formal source-of-truth docs | Stable current product behavior, architecture boundaries, API contracts, operating rules, onboarding-critical maps. | Chronology, raw logs, failed attempts, sub-agent transcripts. |
| README or index | Entry points, navigation, setup, command map, and pointers to canonical docs. | Full specifications or duplicated decisions. |
| Source-adjacent docs/comments | Local API usage, generated docs, non-obvious constraints, module-specific gotchas close to code. | Cross-cutting architecture truth that will be missed by other modules. |
| Delivery report or approved audit/evidence artifact | Final outcome, evidence map, residual risk, and human validation when the project explicitly has such a place. | Product, architecture, or governance source-of-truth updates. |
| Archive | Superseded material kept for historical traceability. | Current truth. |
| Nowhere durable | Process notes, scratch reasoning, raw command output, repeated failed attempts, temporary evidence, duplicate summaries. | Anything future engineers must rely on. |

## OpenSpec, ADR, Formal Docs

Read `references/routing-decisions.md` when choosing among OpenSpec/change spec, ADR, and formal docs.

Default flow:

```text
Proposed change -> OpenSpec/change spec
Accepted significant decision -> ADR
Current stable behavior/contract -> formal docs
Entry point -> README/index
Superseded material -> archive with backlinks
```

Do not collapse these layers. A change spec answers "what should change and how will we accept it"; an ADR answers "why did we choose this"; a formal doc answers "what is true now."

## Directory Architecture

Follow the repository's existing documentation architecture first. If it is missing or chaotic, propose the smallest taxonomy that separates lifecycle and audience:

```text
docs/
  README.md                 # map and source-of-truth index
  current/ or architecture/  # current architecture and boundaries
  product/                  # current product behavior and requirements
  development/              # engineering conventions and workflow rules
  operations/               # runbooks, deployment, incidents, support
  decisions/ or adr/        # accepted decisions and supersession chain
  specs/ or openspec/       # proposed/active change specs
  reference/                # raw source material and external references
  research/                 # validated research conclusions and citations
  archive/                  # superseded docs with backlinks
```

These names are defaults, not universal law. The invariant is separation of responsibility:

- current truth is separate from proposed change,
- accepted decision rationale is separate from implementation plan,
- durable docs are separate from evidence reports and temporary process notes,
- raw references are separate from synthesized conclusions,
- archive is separate from current docs.

## One Fact, One Home

Each durable fact must have one canonical home.

Allowed duplication:

- index entries and short summaries that point to the canonical doc,
- generated API docs from code when code is the canonical source,
- release notes that summarize shipped changes without becoming the canonical behavior spec.

Forbidden duplication:

- copying the same rule into multiple long-lived docs,
- rewriting an ADR decision inside a current-state doc instead of linking,
- keeping old and new behavior descriptions both looking current,
- appending every delivery summary to an unrelated engineering plan.

## Searchability and Change Cost

A documentation structure is only good if readers can find the right answer and maintainers can update it without touching many files.

Searchability rules:

- Use stable, descriptive filenames and headings with the terms engineers will search for.
- Put canonical docs in predictable directories, not hidden inside dated reports.
- Keep a docs index that maps areas to canonical docs.
- Add aliases or short index summaries for common synonyms instead of duplicating full content.
- Link from code, ADRs, specs, and reports back to the canonical doc when they introduce a discoverability path.
- Prefer generated API/reference docs when code or schema is the real source of truth.

Change-cost rules:

- A fact changing should usually require editing one canonical doc plus indexes or generated outputs.
- If a change requires updating several long-lived docs with the same sentence, the information architecture is wrong.
- Do not split documents so narrowly that one conceptual change requires many coordinated edits.
- Do not centralize unrelated topics so broadly that every small change risks merge conflicts and stale sections.
- Keep volatile plans separate from stable current truth so active work does not churn core docs.

Before creating a new doc, name the search query that should find it and the next likely change that would update it. If either answer is vague, improve the route before writing.

## Single-File Growth Control

Do not let one document become a dumping ground.

Trigger a split or archive decision when any of these appear:

- the file now serves multiple audiences with different update rhythms,
- active plans, current truth, decisions, and process notes are mixed,
- a reader cannot find the canonical answer without reading large chronology,
- repeated task summaries are appended to the same long-lived doc,
- headings represent independent owners or independently changing domains,
- the file crosses roughly 800 lines and still keeps growing by append-only updates.

Do not split by date or agent session by default. Split by lifecycle, audience, domain, owner, or source-of-truth responsibility.

## Traceability

Durable docs should support backward and forward tracing:

- Status: proposed, current, accepted, deprecated, superseded, archived.
- Owner: team, role, or project area responsible for updates.
- Last reviewed or update trigger: release, schema change, API change, policy change, design freeze.
- Source links: issue, OpenSpec/change spec, ADR, code module, report, external source.
- Supersession: "supersedes" and "superseded by" links where relevant.
- Verification: command, review, generated check, or manual inspection that keeps it trustworthy.

Do not paste full process logs for traceability. Link concise evidence or final reports when needed.

## Lifecycle Governance

Every durable document needs a lifecycle state. Use the repository's existing labels if present; otherwise use:

```text
proposed -> current -> deprecated -> superseded -> archived
```

Lifecycle actions:

- **Current:** authoritative for now. It must have a canonical path, owner, update trigger, and index link.
- **Deprecated:** still available but no longer recommended. It must say what replaces it or why it is being phased out.
- **Superseded:** replaced by a newer doc, ADR, spec, contract, or code-generated source. Add bidirectional links.
- **Archived:** retained only for history. Move under an archive area or mark clearly at the top; remove it from current navigation except historical links.
- **Deleted:** allowed only when the content is duplicated elsewhere, has no durable value, and history remains recoverable through git or the external system.

Never leave two documents looking current when one supersedes the other.

## Unified Maintenance

Unify governance, not content.

Good unified maintenance:

- one docs index or map that points to canonical docs,
- consistent status labels,
- owner and update trigger on docs with stale-risk,
- one canonical home per durable fact,
- common archive/deprecation wording,
- project doc checks in CI or local validation when available.

Bad unified maintenance:

- one giant "all documentation" file,
- copying every decision into every related doc,
- appending delivery summaries to a long-lived architecture or development plan,
- keeping old docs in the main navigation without status.

If a project has many docs, maintain a small documentation inventory:

```md
| Area | Canonical doc | Status | Owner | Update trigger |
| --- | --- | --- | --- | --- |
```

This inventory is an index, not a second copy of the content.

## When Not To Write

Do not create or update durable docs for:

- raw command output,
- scratch reasoning,
- repeated failed attempts that were superseded,
- sub-agent transcripts,
- temporary future-work dumping,
- obvious restatements of code,
- duplicate summaries of facts already maintained elsewhere,
- speculative future work without owner, acceptance, or priority,
- temporary process notes unless the repository explicitly has an approved audit/evidence artifact.

If a user asks for an audit trail, store it in the approved report/evidence location and label it as evidence, not current truth.

## Completion Standard

Before claiming a documentation change is complete:

- route every changed doc through the governance gate,
- update or create the relevant index entry,
- remove or archive superseded contradictory material,
- preserve trace links instead of copying full content,
- run the project's doc validation or at least `git diff --check`,
- use `references/governance-review-checklist.md` for a steelman self-review when the change creates a new doc, reorganizes docs, or changes documentation policy.
