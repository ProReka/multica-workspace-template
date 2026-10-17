---
name: project-delivery
description: Outcome-led delivery, right-sized work breakdown, estimation, accountability, risk registers, and change control.
---

# Project Delivery Framework

Follow [Product Delivery](../../workspace/product-delivery.md); [governance](../../workspace/governance-rules.md) remains authoritative. Use existing issues and release records, not parallel trackers.

## 1. Intake & Ready Work
- Obtain the human Owner's initiative contract: evidence, outcome, metric/baseline/target, scope, acceptance criteria, constraints, risk/environment, release authority, and outcome evaluator/checkpoint. Unknown baselines require measurement, not invention.
- Decompose into the smallest independently verifiable tasks; use phases only when useful, not a mandatory three-tier hierarchy. Include testing, migrations, documentation, and telemetry as applicable.
- Each task has one human Owner, assignee, dependencies, deliverable/acceptance criteria, risk/environment, verification gate, checkpoint, and execution budget. High-complexity OR High-Risk work needs a TL draft; coordinate infrastructure planning with DevOps.
- Resolve dependencies and required approvals before dispatch. Use bounded discovery when the solution is uncertain. Default to one active implementation per agent, account for review capacity, and use one trigger with the shared dispatch guard.

## 2. Estimation & Limits
Use estimates proportionate to uncertainty; three-point estimation is optional: `(Optimistic + 4 × Likely + Pessimistic) / 6`. Explain assumptions and dependency risks rather than imposing fixed percentage buffers. Agree checkpoints and execution budgets with the Owner; stop and report options at limits.

## 3. Accountability & Evidence
- Responsible: executing agent/engineer. Accountable: exactly one human Owner. Consulted: TL/domain specialists. Informed: affected stakeholders.
- Link acceptance results and exact artifact revisions to the applicable gate. Non-PR work needs TL review and explicit Owner acceptance; PR work needs human merge. Changed revisions invalidate affected approvals.
- Track delivery, release authorization/verification, and outcome evaluation separately. Maintain the playbook's weekly evidence-based scorecard; task counts and merge volume are not success metrics.

## 4. Change Control & Risk Register
- Record proposed scope changes on the initiative: reason, outcome/acceptance impact, schedule/cost, dependencies, and risk. Obtain human Owner approval before expansion; revise ready contracts and affected approvals.
- Keep a risk register in existing issues: risk/evidence, likelihood/impact, human owner, mitigation, escalation trigger, status, and next checkpoint. Review at checkpoints and when evidence changes; escalate security/production risks under governance, never waive controls.
