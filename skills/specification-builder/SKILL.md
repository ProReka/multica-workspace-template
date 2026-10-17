---
name: specification-builder
description: Structured specification synthesis. Converts freeform discussions, meeting transcripts, and raw notes into rigorous, buildable engineering specifications.
---

# Specification Builder

## Technical Specification Template

Transform freeform discussions into this standardized structure:

```markdown
# [ID] <Feature / Component Title>

## 1. Problem Statement & User Value
- **User Context:** Target persona and friction point.
- **Measurable Value:** Desired operational or business outcome.

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
- [ ] Automated tests pass 100% and verification evidence is attached to PR.
```
