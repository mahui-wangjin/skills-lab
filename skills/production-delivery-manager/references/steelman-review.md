# Steelman Counter-Review

Steelman review is mandatory before claiming completion for substantial engineering work.

The goal is not to be negative. The goal is to construct the strongest plausible case that the solution should not ship yet, then resolve that case with evidence.

## When To Run

Run before final handoff when the task includes:

- production-grade expectation
- cross-module behavior
- data, permission, payment, migration, or security impact
- new API, workflow, adapter, background job, or integration
- frontend interaction with meaningful user workflow
- substantial refactor
- prior build/test failure
- ambiguous requirement that was resolved by assumption
- complex or production-grade work where the lead agent did not use real sub-agents

For small tasks, run a compressed self-review.

## Review Stance

Assume at least one of these is true and try to prove it:

- The implementation satisfies the words but not the user's real goal.
- A requirement was assumed rather than confirmed.
- A local pattern was missed and the solution created unnecessary divergence.
- The design is overbuilt for the current need.
- The design is underbuilt for production failure modes.
- A happy path passes but an error path fails silently.
- Permissions, validation, tenant/data isolation, or audit trails are incomplete.
- A race, idempotency, retry, rollback, or migration problem exists.
- The tests prove implementation details but not user-visible behavior.
- The verification evidence does not cover the risky part.
- The final answer overclaims certainty.
- The lead agent avoided delegation or independent review for speed, then overtrusted self-review.
- Real sub-agents, specialist review, or independent verification were skipped without enough compensating evidence.
- The final handoff is technically complete but not human-validatable: architecture, core logic, evidence, screenshots, CI/workflow status, or residual risks are not organized so the user can accept or reject the delivery.
- A required HTML delivery report was skipped, incomplete, unlinked, local-only without explanation, or filled with raw logs instead of reviewable evidence.
- Process ledgers, debug chronology, raw command dumps, sub-agent transcripts, or repeated attempts were written into formal project docs instead of the final handoff, `.production-delivery-reports/`, or an explicitly approved ledger path.

## Method

1. Restate the acceptance criteria.
2. Restate the delegation decision for complex or production-grade work.
3. List the strongest objections.
4. For each objection, cite evidence:
   - code path
   - test result
   - command output
   - source document
   - explicit assumption
5. Decide:
   - Fix now
   - Add verification now
   - Add or repair the Human Validation Packet or HTML report now
   - Downgrade completion claim
   - Ask user
   - Accept as residual risk

For complex or production-grade work, include one objection that challenges the delivery process itself: "Was this implemented, reviewed, verified, and accepted by the same agent without a strong reason?" If yes, resolve it with independent evidence, extra verification, or a downgraded claim.

Also challenge the no-delegation exception directly:

- Was real delegation authorized by the user's wording or available tool policy?
- If delegation was available, why was it not used?
- Did the fallback verification objectively cover the missing specialist perspective?
- Should the final handoff say complete, partial, candidate, or self-reviewed?

Also challenge the user validation surface directly:

- Can a busy human validate the architecture and core logic without reading the full diff?
- Are screenshots classified as visible-state evidence rather than overclaimed backend proof?
- Does the evidence map say what each test, build, CI job, browser run, screenshot, or manual inspection proves and does not prove?
- If an HTML report was required, is it in `.production-delivery-reports/` or a documented project-specific equivalent, with relative links to evidence?
- Did any product, architecture, development, or governance doc receive process notes that should have stayed in working notes or report evidence?
- Are secrets, tokens, personal data, and noisy raw logs excluded or redacted?

## Output Template

Use this internally or in the final answer when the risk is high:

```md
### Steelman Counter-Review

- Strongest objection: <why this may still be wrong>
- Evidence checked: <files/tests/docs/commands>
- Decision: <fixed / verified / accepted residual risk / needs user decision>
- Remaining risk: <specific residual risk or none known>
- Human validation: <packet/report complete, repaired, omitted with reason, or downgraded>
```

## Quality Bar

Do not let a weak objection pass as steelman. A good objection would make a competent reviewer hesitate to merge.

Do not let a generic answer pass as resolution. Each objection needs evidence or an explicit risk decision.

If the steelman review finds a material issue, do not claim full completion until the issue is fixed or the user accepts the risk.
