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

## Method

1. Restate the acceptance criteria.
2. List the strongest objections.
3. For each objection, cite evidence:
   - code path
   - test result
   - command output
   - source document
   - explicit assumption
4. Decide:
   - Fix now
   - Add verification now
   - Downgrade completion claim
   - Ask user
   - Accept as residual risk

## Output Template

Use this internally or in the final answer when the risk is high:

```md
### Steelman Counter-Review

- Strongest objection: <why this may still be wrong>
- Evidence checked: <files/tests/docs/commands>
- Decision: <fixed / verified / accepted residual risk / needs user decision>
- Remaining risk: <specific residual risk or none known>
```

## Quality Bar

Do not let a weak objection pass as steelman. A good objection would make a competent reviewer hesitate to merge.

Do not let a generic answer pass as resolution. Each objection needs evidence or an explicit risk decision.

If the steelman review finds a material issue, do not claim full completion until the issue is fixed or the user accepts the risk.
