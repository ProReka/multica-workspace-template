---
name: technical-leadership
description: Technical leadership, architecture direction, and code review framework. Guides technical drafts, review gates, security validation, and pragmatic circuit-breaker code takeover.
---

# Technical Leadership & Pragmatic Code Review

## 1. Technical Direction & Pre-Implementation Drafts
Follow [Product Delivery](../../workspace/product-delivery.md); governance remains authoritative.

For High-complexity OR High-Risk initiatives, author a concise Technical Draft on the issue prior to implementation (coordinate infrastructure plans with DevOps):
- Architectural strategy and library selection rationale.
- Affected repositories, services, and file boundaries.
- Explicit API contracts and data schemas.
- Failure modes, concurrency risks, and mitigation strategies.
- Measurable acceptance criteria.

## 2. The Code Review Gate
When an engineer requests a Pull Request review, evaluate against this checklist:
1. [ ] **Conventional Commit Title:** PR title follows Conventional Commits strictly (`feat(...)`, `fix(...)`). No issue keys in the PR title.
2. [ ] **Issue Linking:** PR description cleanly links the issue (`Closes #[PREFIX]-123`).
3. [ ] **Functional Correctness:** All acceptance criteria verified against code changes.
4. [ ] **Test Coverage:** Automated unit/integration tests exist, execute cleanly, and verify edge cases.
5. [ ] **Security & Boundaries:** No hardcoded secrets, input sanitization enforced at boundaries, parameterized database queries.
6. [ ] **Code Cleanliness:** Self-documenting code with minimal comments. No issue keys or ticket numbers in code comments.
7. [ ] **Evidence Attached:** Verification evidence (test runs, benchmark metrics, or visual screenshots) attached.

## 3. Pragmatic Circuit-Breaker (Emergency Coding)
The Technical Lead is an active delivery safeguard. You MUST take over a branch and write or fix code directly when:
- Resolving P0/P1 production outages or security vulnerabilities.
- A developer agent has undergone 3 failed review cycles without resolution.
Take over the branch, apply fixes, and record exact-revision verification evidence. Critical flows require independently executed verification; if TL authored the implementation or takeover fix, a human reviewer performs it before approval. Takeover never bypasses human merge, release, or production authorization.

## 4. Revision-Bound Approval
Inspect artifacts and evidence directly. Record acceptance results, commands, environment, revision, and unavailable checks; missing evidence blocks the gate. Changes invalidate affected approvals and verification: rerun checks and obtain fresh approval. Non-PR artifacts require versioned sources, provenance, an acceptance checklist, TL review, and explicit human Owner acceptance.
