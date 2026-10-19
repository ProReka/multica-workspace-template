# Product Development Delivery Playbook

Reference playbook for coordinators and reviewers; consult relevant sections for a task, never embed this entire document in every agent prompt. It is not a prerequisite checklist for every small coding task. Apply initiative contracts to initiatives, not repeatedly to each child issue. This is the domain playbook for the existing Product Development team. `workspace/governance-rules.md` remains authoritative. Use the contracts below in issues and release records; do not create a parallel tracking system.

## 1. Ownership & Intake

The human Project Lead owns product decisions. PM checks completeness, challenges unsupported assumptions, and coordinates execution; PM does not invent business approval. TL owns technical readiness. Every child issue inherits the initiative's human Owner unless explicitly reassigned.

Before dispatch, the Owner accepts this initiative contract:

```text
Problem / target user:
Evidence of the problem:
Desired outcome:
Success metric / baseline (or unknown + measurement task) / target:
Scope / non-goals:
Acceptance criteria (observable pass/fail):
Constraints: deadline, execution budget, data/privacy, dependencies:
Human Owner:
Risk Tier / Target Environment:
Release owner (human) / rollout and rollback authority:
Outcome checkpoint (date or observation window) / evaluator (human):
```

Unknowns must be explicit. If the solution is uncertain, dispatch a bounded discovery task with a question, time/budget ceiling, and decision artifact instead of committing to implementation. Missing ownership, acceptance criteria, or required approvals blocks dispatch. Measure a proxy only with Owner agreement; never invent a baseline.

## 2. Ready-to-Start Work Contract

PM creates the smallest independently verifiable tasks. Each task records:

```text
Parent initiative / human Owner:
Deliverable / acceptance criteria:
Assignee / dependencies:
Risk Tier / Target Environment:
Technical draft (required for high complexity):
Verification plan / applicable technical gate:
Checkpoint / execution budget or runtime limit:
```

- Resolve dependencies before dispatch. Use one trigger per step and a shared per-issue dispatch guard.
- Default to one active implementation task per agent. PM must account for review capacity before starting more work; do not parallelize edits to the same branch.
- Treat requests to change scope as change proposals. Record effect on outcome, acceptance criteria, schedule, and cost; obtain Owner approval before expanding work.
- Bound discovery, implementation, and review by agreed checkpoints. At a limit, report completed work and options; do not silently spend more or reduce quality.
- TL's three-round circuit-breaker is a recovery mechanism, not permission to bypass human gates.

## 3. Quality & Evidence Contract

The author verifies acceptance criteria and records exact commands, results, environment, and artifact revision. TL inspects the artifact and evidence directly; a developer's summary is not sufficient. Evidence must omit secrets and redact personal data.

| Change | Required verification where applicable |
|---|---|
| All implementation | Acceptance criteria mapped to results; relevant automated tests, lint/type/build checks; failures or unavailable checks disclosed |
| UI / mobile | Loading, empty, error and success states; keyboard/accessibility checks; supported screen sizes; visual inspection recorded (screenshots preferred) |
| API / authorization | Contract compatibility, validation, authentication/authorization, negative paths and error behavior |
| Data / migrations | Integrity, backward compatibility, migration dry-run, recovery plan; no unapproved destructive production action |
| AI behavior | Representative normal, adversarial, and failure cases; output validation, privacy, fallback, latency/cost bounds; record model/prompt revision |
| Infrastructure | Saved plan and revision, add/change/destroy summary, impact, security and recovery; DevOps gate |
| Non-PR artifacts | Versioned artifact, source provenance, acceptance checklist, TL review and explicit Owner acceptance |

For critical flows (payments, permissions, destructive changes, sensitive data), require an independently executed verification by TL or a human reviewer. If TL authored the implementation or takeover fix, a human reviewer performs that verification. No new QA agent is required.

Use this review record:

```text
Artifact / commit revision:
Acceptance criteria and linked results:
Checks run / results / environment:
Checks not run / reason / remaining risk:
Risk Tier / known limitations:
Applicable gate(s) / reviewer / decision:
Human acceptance / merge evidence:
```

Approval applies only to the reviewed revision. Any artifact, code, migration, or plan change invalidates its affected approvals and verification; rerun affected checks and obtain fresh approval. Missing required evidence blocks the gate. An unavailable check is not a passed check; any alternate verification requires the appropriate reviewer and human Owner's explicit acceptance. Mandatory security and production controls cannot be waived.

## 4. Separate Delivery, Release & Outcome

Track these as distinct records or linked issues, not additional implicit meanings of `done`:

1. **Delivery:** Child work completes under governance step 8. The implementation parent may close when all child delivery gates pass; it does not prove deployment or business impact.
2. **Release:** A linked release record remains open until authorized rollout and post-release verification finish. Human release owner decides go/no-go. Merge is not release authorization.
3. **Outcome:** The initiative remains open until the human evaluator records the agreed observation-window result and decides continue, iterate, or stop. Link the delivery parent, release record, and metric evidence.

Release record:

```text
Initiative / human release owner:
Exact artifact revision / target environment:
Technical approvals / human go-no-go evidence:
Rollout method / dependencies / migrations:
Verification: signals, thresholds, observation window, responsible agent:
Rollback: trigger, procedure, known limits, authorized executor:
Production approvals and access gate (if applicable):
Actual rollout time / deployed revision / verification results:
Disposition: verified / rolled back / blocked:
```

Every release requires explicit human release-owner authorization. All state-changing production execution, including application deployments and rollbacks, additionally requires both Owner and Director approval for the exact plan/revision and scoped actions. Only a configured runtime gate may grant execution access. Incident response does not waive these requirements. Agents may prepare a rollback but execute state-changing production actions only within explicit, scoped authorization.

If verification fails, stop rollout, preserve evidence, notify the release owner, and follow the authorized rollback or incident process. Never hide a failed release by closing its issue.

Outcome review:

```text
Metric / baseline / target / observation period:
Actual result / data source / data quality limitations:
User feedback / unintended effects:
Human evaluator / decision: continue, iterate, stop, or inconclusive:
Next action / responsible party / checkpoint:
```

An inconclusive result needs a reason and a new bounded checkpoint or an explicit decision to stop measurement. A failed experiment can be a valid learning outcome; it is not reported as target attainment.

## 5. Response & Escalation

At setup, agree a timezone, staffed hours, primary human contact, backup, and response targets. These are targets to validate in the pilot, not a claim of 24/7 coverage.

| Event | Initial operating target | Required action |
|---|---|---|
| P0: outage, active breach, suspected data loss | Human acknowledgment within 15 minutes during configured coverage | Route immediately to incident contacts; preserve evidence and assess safe containment |
| P1: severe degradation or critical flow unavailable | Human acknowledgment within 30 minutes during configured coverage | Route immediately to incident contacts; assess impact and mitigation |
| Delivery blocker | PM triage within 4 staffed hours | Name dependency owner and next checkpoint |
| Review / acceptance request | Acknowledge within 1 business day | Approve, request changes, or give an explicit review checkpoint |

For P0/P1, Application Support creates or updates one incident, records impact and evidence, and routes to TL, DevOps when relevant, and the designated human contact. Use event delivery, not the four-hour recovery schedule. Escalate to the backup when acknowledgment is overdue. Outside staffed hours, route to configured on-call; without on-call, disclose the coverage gap and keep autonomous actions within existing authorization.

Record a timeline, mitigation, user impact, restoration evidence, and follow-up prevention tasks. Fatal agent execution failures use the separate recovery procedure; they are not automatically product incidents.

## 6. Operating Review

PM maintains a weekly scorecard from actual timestamps and evidence:

- Outcome target attainment, with inconclusive results shown separately.
- Lead time: ready-to-start to human delivery acceptance, plus separate release wait.
- Queue time: waiting for technical review and waiting for human decisions.
- Escaped defects by severity and affected release; do not penalize reporting.
- Rework rounds and agent execution cost per accepted deliverable, including failed runs.
- Incident acknowledgment and mitigation time against configured coverage.

Start with measured baselines; Owner agrees targets after the pilot. Inspect bottlenecks and quality together. Task count, token usage alone, and merge volume are not success metrics.
