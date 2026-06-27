# Document Taxonomy

Use this reference when deciding where information belongs. The goal is to keep long-lived facts discoverable and stop temporary work notes from polluting source-of-truth docs.

## Routing Matrix

| Artifact | Purpose | Write when | Required fields | Must not contain |
| --- | --- | --- | --- | --- |
| README / docs index | Entry point and navigation map | A durable doc, module, or workflow becomes important enough to find again | Scope, links, short descriptions, owner or area when useful | Full specs, copied decisions, process logs |
| Current-state product docs | What the product does now | Stable behavior, requirement, UX rule, or acceptance baseline is current | Status/current date, owner, source links, verification or review trigger | Proposed behavior, rejected alternatives, implementation chronology |
| Current-state architecture docs | How the system is shaped now | Boundaries, module ownership, data flow, deployment/runtime model, integration contract is current | Scope, diagrams or references, owner, related ADR/spec/code, update trigger | Active proposals, low-level task lists, stale diagrams without status |
| Development/governance docs | How engineers and agents work in this repo | Rules affect recurring development, review, testing, release, docs, or agent behavior | Rule, reason, applicability, verification, owner | One-off session notes or personal preferences without project impact |
| API/interface docs | Public or cross-module contract | Callers need stable inputs, outputs, errors, side effects, versioning, or examples | Version/status, schema, errors, auth/permission, examples, generated source if any | Internal debugging notes or duplicated implementation details |
| Runbooks/operations docs | How to operate or recover systems | A procedure must be repeatable under pressure | Preconditions, steps, rollback, verification, escalation, owner | Architecture essays or unverified folklore |
| OpenSpec/change spec/RFC | Proposed or active change | Scope, acceptance, contracts, migration, rollout, or multi-role coordination must be agreed before it becomes current truth | Problem, goals, non-goals, proposed changes, acceptance, risks, affected docs | Accepted historical rationale after the change is done unless summarized and linked |
| ADR | Accepted significant decision | A costly-to-reverse choice has been made and future readers need why | Status, date, context, decision, alternatives, consequences, supersession | Implementation plan, checklist, issue log, implementation diary |
| Research docs | Validated external or internal findings | Research will be reused for decisions or implementation | Question, sources, date, conclusion, confidence, limitations | Raw bookmarks without synthesis or outdated claims without date |
| Reference/raw materials | Original inputs | Source material must be preserved for traceability | Source, date, provenance, relation to synthesized docs | Claims presented as accepted project truth |
| Approved audit/evidence artifact | Concise final evidence or continuity state | Project explicitly has an approved audit/evidence artifact and future work needs continuity | Goal, key changes, verification, risk/blocker, next step | Debug chronology, raw logs, full sub-agent transcripts |
| Delivery report/evidence | Human validation and final proof | Complex delivery needs evidence map, screenshots, CI, or acceptance package | Outcome, key changes, evidence grades, gaps, residual risk | Current product/architecture truth as the only copy |
| Archive | Historical trace | A doc is superseded but still useful for why/history | Archived status, superseded-by link, date, reason | Anything that should still look current |

## Lifecycle States

Use these states unless the repository already has stronger labels:

| State | Meaning | Required action |
| --- | --- | --- |
| Proposed | Not accepted as current truth | Keep in change spec/RFC area; link acceptance criteria |
| Current | Authoritative current truth | Link from index; define owner and update trigger when stale-risk exists |
| Accepted | Decision has been made | Store as ADR or decision record; link current docs |
| Deprecated | Still exists but should be phased out | State replacement, reason, and removal trigger |
| Superseded | Replaced by a newer artifact | Add superseded-by link and remove from current navigation |
| Archived | Historical only | Move or mark clearly; preserve backlinks |
| Deleted | No durable value beyond VCS history | Delete only after confirming no canonical facts are lost |

Do not use "old", "latest", or "final" as lifecycle states. They are ambiguous and become stale quickly.

## Write Gate Questions

Ask these before writing:

1. Will a future engineer rely on this after the current task is forgotten?
2. Is this current truth, a proposed change, accepted rationale, or evidence?
3. Who owns keeping it correct?
4. What event should trigger an update?
5. Does a canonical doc already exist?
6. Can this be a link or index entry instead of duplicated text?
7. Would this still make sense without knowing this agent session happened?
8. What search terms should find the canonical answer?
9. How many files must change when this fact changes next time?

If the answer to 1, 3, or 4 is unclear, do not create a new durable doc yet.

If the answer to 8 is unclear, add an index entry, alias, or clearer heading. If the answer to 9 is "many", consolidate the canonical fact and replace duplicates with links.

## Directory Split Principles

Prefer directories that separate lifecycle first, then audience or domain:

- `current/`, `architecture/`, `product/`, or similar for stable truth.
- `specs/`, `openspec/`, `rfcs/`, or similar for proposed/active change.
- `decisions/` or `adr/` for accepted rationale.
- `operations/` for repeatable operational procedures.
- `reference/` for raw sources.
- `archive/` for superseded material.

Avoid directories named only after process moments such as `latest`, `worklog`, `agent-output`, `misc`, or `temp` unless the repository explicitly treats them as disposable.

## Searchability

Optimize for both human search and agent search:

- Use filenames that contain durable domain terms, not only dates.
- Use headings that answer likely questions directly.
- Keep short index summaries with synonyms when teams use multiple names for the same concept.
- Link from nearest code/module docs to cross-cutting canonical docs.
- Do not bury current truth in archive folders, delivery reports, or dated change proposals.
- Prefer a single route from root README or `docs/README.md` to every canonical doc.

Good:

```text
docs/architecture/auth-boundaries.md
docs/decisions/ADR-004-auth-session-storage.md
```

Risky:

```text
docs/2026-06-27-notes-final-v3.md
docs/misc/agent-output.md
```

## Modification Cost

Keep change cost low:

- Stable truth and active proposals should be separate so active proposals do not churn stable docs.
- Cross-cutting rules should have one canonical doc and be linked from feature docs.
- Domain-specific details should live near the owning domain to avoid global merge conflicts.
- Generated docs should declare their generator and source; edit the source, not the generated output.
- If one small product/API behavior change requires coordinated edits in many docs, reduce duplication before adding more text.

## File Size and Shape

Line count is an alarm, not the only rule.

Consider splitting a file when:

- readers must scan unrelated domains to answer one question,
- headings have different owners,
- update triggers differ,
- accepted decisions, current rules, and proposed work are mixed,
- append-only history hides the current answer,
- the index cannot summarize the file in one sentence.

Keep a file together when:

- the sections always change together,
- one owner maintains the whole artifact,
- splitting would create pass-through stubs,
- the document is a short index intentionally linking elsewhere.
