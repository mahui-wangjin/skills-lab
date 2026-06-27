# Governance Review Checklist

Use this checklist before committing documentation governance changes, new long-lived docs, or doc reorganizations.

## Steelman Counter-Review

Challenge the change with these objections:

| Objection | What to check |
| --- | --- |
| "This creates more documentation sprawl." | Did you update an existing source of truth instead of creating a new doc? Is the new doc's owner and lifecycle clear? |
| "This hides useful traceability." | Are important decisions linked through issue/spec/ADR/docs/report without copying process logs? |
| "This should be OpenSpec, not current docs." | Is the content still a proposal or active change requiring acceptance? |
| "This should be ADR, not a generic architecture note." | Is the main value accepted rationale, alternatives, and consequences? |
| "This should be current docs, not ADR." | Does the reader mainly need what is true now rather than why it was chosen? |
| "This belongs nowhere durable." | Is it scratch reasoning, raw output, debugging chronology, or a superseded attempt? |
| "This file is becoming a dumping ground." | Are unrelated audiences, lifecycles, owners, or update triggers mixed? |
| "This duplicates another doc." | Is there one canonical home and only short index summaries elsewhere? |
| "This will go stale." | Is there an owner, update trigger, status, or generated source? |
| "This reorganization is too broad." | Can index/status/backlinks solve the problem with less churn? |
| "This should be deprecated or archived first." | Is an old doc still linked as current? Is the replacement discoverable? |
| "This deletes history too aggressively." | Is any unique decision, contract, source, or evidence being lost outside VCS? |
| "Unified maintenance became a giant document." | Is the index duplicating content instead of only routing, status, owner, and update trigger? |
| "Readers will not find this." | Are filename, headings, index entries, aliases, and backlinks aligned with likely search terms? |
| "This is expensive to update." | Will the next change require editing many docs with the same fact? |

## Required Checks

- The destination matches content type and lifecycle.
- Existing project documentation conventions were followed unless explicitly improved.
- New long-lived docs are linked from the docs index or nearest README.
- Superseded docs are archived or marked with backlinks.
- Deprecated docs state replacement, reason, owner, and removal/review trigger.
- Archived docs are visibly non-current and removed from current navigation.
- Deleted docs contain no unique durable fact beyond what VCS or an external system preserves.
- Unified indexes do not duplicate canonical content.
- Search terms, aliases, and index entries point to the canonical doc.
- A future change to the same fact has one canonical edit location plus indexes/generated outputs.
- Current docs do not contain process notes, raw logs, repeated failed attempts, or sub-agent transcripts.
- ADRs include status, date, context, decision, alternatives, consequences, and supersession path.
- OpenSpec/change specs include scope, non-goals, acceptance, affected contracts, risks, and docs to update.
- Source-of-truth docs define current behavior or current architecture without duplicating full ADR/spec content.
- Large files were checked for split/archive opportunities.
- Validation was run or a reason for not running it is stated.

## Evidence Hygiene

When evidence must be durable:

- Store screenshots, traces, CI logs, and command excerpts in a report/evidence location approved by the project.
- Summarize what each artifact proves and what it does not prove.
- Redact secrets, tokens, session values, and personal data.
- Do not paste full raw logs into formal docs.

## Final Handoff

Report documentation work by outcome:

- what canonical docs changed,
- what new routing rule or taxonomy was introduced,
- what stale or duplicate material was archived or left untouched,
- what validation ran,
- what risk remains.

Do not narrate the step-by-step editing process.
