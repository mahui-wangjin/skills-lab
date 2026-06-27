# Routing Decisions

Use this reference for the hard choice among OpenSpec/change specs, ADRs, and formal documentation.

## OpenSpec / Change Spec

Create or update an OpenSpec-style change spec when the work is not yet stable truth and needs agreement.

Triggers:

- cross-module or cross-team change,
- public API or data contract change,
- migration, rollout, compatibility, or deprecation plan,
- product behavior that needs explicit acceptance criteria,
- security, permission, billing, data retention, workflow, or integration impact,
- multiple implementation slices that must be tracked against one intent,
- user or reviewer must approve scope before implementation.

Do not use a change spec as the permanent current-state doc. When accepted and implemented, update the formal docs and link back to the change spec for history.

If the project has no OpenSpec tool, use its nearest equivalent: RFC, proposal, design spec, issue with acceptance criteria, or `docs/specs/`.

## ADR

Write an ADR when a significant decision has been accepted and future readers need the rationale.

Good ADR subjects:

- framework, runtime, database, queue, hosting, auth, search, AI runtime, or integration strategy,
- module boundary or data ownership choice,
- API style or compatibility policy,
- security, privacy, retention, or permission model,
- irreversible migration or deprecation path,
- trade-off where rejected alternatives are likely to be reopened.

Do not write ADRs for:

- unresolved proposals,
- ordinary implementation steps,
- tiny preferences with low reversal cost,
- implementation summaries,
- evidence logs,
- "we changed X" without a decision and alternatives.

ADR lifecycle:

```text
Proposed -> Accepted -> Superseded / Deprecated
```

Never silently rewrite an accepted ADR into a new decision. Add a new ADR that supersedes it, or update status with a clear supersession link.

## Formal Source-of-Truth Docs

Update formal docs when the repository's current truth changed or became clearer.

Examples:

- current product behavior,
- current architecture/module responsibility,
- API contract,
- development workflow rule,
- deployment/runbook procedure,
- onboarding map,
- stable directory ownership.

Formal docs should read like durable truth, not like a delivery diary. They should not say "the agent did..." or preserve repeated failed attempts.

## Long-Term Decision vs ADR vs Formal Doc

Use this decision rule:

| Question | Route |
| --- | --- |
| "What are we proposing to change, and how will we know it is done?" | OpenSpec/change spec |
| "Why did we choose this among alternatives?" | ADR |
| "What is true now for users, developers, operators, or agents?" | Formal source-of-truth docs |
| "Where do I find the canonical docs?" | README/index |
| "What happened in this delivery and how was it verified?" | Final handoff/report/evidence |
| "What did the agent try while debugging?" | Nowhere durable, unless explicitly requested as audit trail |

## Traceability Chain

Prefer links over copied content:

```text
Issue/request
  -> OpenSpec/change spec for scope and acceptance
  -> ADR for accepted significant decisions
  -> current docs for stable truth
  -> code/tests/generated docs for executable truth
  -> delivery report/evidence for final proof
  -> archive when superseded
```

Each layer should answer a different question. If two docs answer the same question with overlapping full text, consolidate or choose one canonical home.

## Directory Design Method

When a project has no clear docs taxonomy:

1. Inventory current docs by purpose, audience, lifecycle, owner, and update trigger.
2. Mark source-of-truth docs versus proposals, decisions, references, evidence, and archive.
3. Choose a minimal top-level taxonomy that separates lifecycle before topic.
4. Move or rename only when it reduces ambiguity; otherwise add index entries and status headers first.
5. Add backlinks and supersession notes before deleting or archiving.
6. Define write rules in the project rules file or docs index.

Avoid a big-bang reorganization unless stale or duplicated docs are already causing incorrect implementation decisions.

## Deprecation and Archiving

Deprecate before archiving when readers may still arrive through links.

Deprecation requires:

- status at the top,
- replacement link or reason no replacement exists,
- date or release where deprecation started,
- removal or review trigger,
- owner.

Archive when:

- the replacement is linked and discoverable,
- current indexes no longer point to the old doc as authoritative,
- backlinks from the replacement preserve traceability,
- the old doc is still useful for history or audit.

Delete instead of archive when:

- it is a duplicate of a canonical doc,
- it contains no unique decision, contract, source, or evidence,
- keeping it would create false current truth,
- git or the external source already preserves the history.

Never archive by dumping files into an unlabeled folder. Archived docs must be visibly non-current.

## Unified Maintenance Model

For repositories with many docs, maintain one index or inventory that answers:

- What is the canonical doc for each area?
- What lifecycle state is it in?
- Who owns updates?
- What event requires an update?
- Which ADR/spec/code/report explains the trace path?

Do not centralize by merging content into one large document. Centralize discovery, status, ownership, and validation.

## Search and Maintenance Trade-Offs

Use this decision rule when choosing between one file, many files, and an index:

| Shape | Use when | Avoid when |
| --- | --- | --- |
| Single doc | One owner, one audience, one update trigger, readers need the whole context together | Multiple lifecycles or domains are mixed |
| Split docs | Independent owners, domains, lifecycles, or update triggers | One conceptual change would require many edits |
| Index/inventory | Discovery, aliases, lifecycle state, ownership, and routing | It starts duplicating canonical content |
| Source-adjacent doc | Local module/API knowledge is easiest to find near code | The rule applies broadly across modules |
| Generated reference | Code/schema is canonical and docs can be regenerated | People manually edit generated output |

Aim for "easy to find, cheap to change." If those conflict, add index links and aliases before duplicating content.

## Status Header

For long-lived docs, use a lightweight status block when the repository has no existing template:

```md
Status: Current | Proposed | Accepted | Deprecated | Superseded | Archived
Owner: <team/role>
Last reviewed: <date or release>
Update trigger: <what change requires updating this doc>
Source links: <OpenSpec / ADR / issue / code / report>
Supersedes / Superseded by: <links if relevant>
```

Do not add heavy frontmatter to every tiny doc if the project does not need it. Use it when stale-doc risk is real.
