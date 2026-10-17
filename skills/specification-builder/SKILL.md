---
name: specification-builder
description: Structured specification synthesis. Converts freeform discussions, meeting transcripts, and raw notes into rigorous, buildable engineering specifications.
---

# Specification Builder

Follow [Product Delivery](../../workspace/product-delivery.md); governance remains authoritative. Obtain human Owner acceptance of the initiative contract before dispatch. Unknowns stay explicit; uncertain solutions use bounded discovery.

## Technical Specification Template

Transform freeform discussions into this standardized structure:

```markdown
# [ID] <Feature / Component Title>

## 1. Problem Statement & User Value
- **User Context:** Target persona and friction point.
- **Measurable Value:** Desired outcome; metric, baseline (or unknown + measurement task), target, and source.
- **Outcome Review:** Observation window/checkpoint, human evaluator, and continue/iterate/stop decision.
- **Authority:** Human Owner; human release owner and rollout/rollback authority.

## 2. Scope Boundaries
- **In-Scope (Deliverable):** Exact capabilities implemented in this release.
- **Out-of-Scope (Deferred):** Explicitly excluded items reserved for future iterations.

## 3. User & System Flows
1. Primary Flow: Step 1 ➔ Step 2 ➔ Step 3.
2. Edge Cases & Recovery: Error handling, offline behavior, invalid input paths.

## 4. Technical Contracts & Schemas
- API Endpoints: `METHOD /v1/path`
- Request & Response JSON schemas.
- Database schema changes and migration requirements.

## 5. Acceptance Criteria (Definition of Done)
- [ ] Criteria 1: ...
- [ ] Criteria 2: ...
- [ ] Applicable tests/checks and observable acceptance results link exact artifact revision, commands, results, and environment; unavailable checks disclosed.
- [ ] Non-PR artifact includes provenance and checklist for TL review and explicit human Owner acceptance.

## 6. Ready-to-Start Contract
- Parent initiative / human Owner / assignee / resolved dependencies.
- Risk Tier / Target Environment / constraints (deadline, budget, privacy).
- TL Technical Draft for High-complexity OR High-Risk work; DevOps coordinates infrastructure plans.
- Verification plan / applicable gate / checkpoint / execution budget.
- Required approvals recorded; unresolved ownership, criteria, or approvals block dispatch.
- Separate linked delivery, release (rollout/verification/rollback), and outcome records.
```
