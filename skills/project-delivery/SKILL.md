---
name: project-delivery
description: Comprehensive project management and delivery framework. Covers Work Breakdown Structure (WBS), three-point estimation, RACI matrices, risk registers, and change control workflows for high-velocity teams.
---

# Project Delivery Framework

## 1. Work Breakdown Structure (WBS)
Decompose every project or major feature initiative into a 3-tier hierarchy:
`Phase ➔ Functional Deliverable ➔ Actionable Task`

Rules:
- **100% Rule:** The WBS must account for 100% of the scope, including automated testing, schema migrations, documentation, and operational telemetry.
- **Verb + Noun:** Every task must begin with an imperative action verb (e.g., "Implement JWT validation middleware", "Add database index on tenant_id").
- **Single Ownership:** Every task must have exactly one accountable owner.
- **Definition of Done:** Explicit verification criteria must be defined before work commences.

## 2. Three-Point Estimation Framework
Avoid single-point estimation. Apply the PERT distribution:
`Expected = (Optimistic + 4 × Likely + Pessimistic) / 6`
Standard buffers:
- Add 20% for integration boundaries and external third-party APIs.
- Add 15% for novel libraries or unproven framework features.

## 3. Communication & Accountability (RACI Matrix)
- **Responsible (R):** The specific agent or engineer executing the work.
- **Accountable (A):** The single human Owner who approves the completed deliverable and authorizes the merge.
- **Consulted (C):** Domain specialists or Technical Lead who provide architectural input.
- **Informed (I):** Stakeholders who receive status notifications.
