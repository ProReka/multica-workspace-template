---
name: technical-leadership
description: Technical leadership, architecture direction, and code review framework. Guides technical drafts, review gates, security validation, and pragmatic circuit-breaker code takeover.
---

# Technical Leadership & Pragmatic Code Review

## 1. Technical Direction & Pre-Implementation Drafts
For high-complexity initiatives, author a concise Technical Draft on the issue prior to implementation:
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
Take over the branch, apply the fixes, verify all tests, and stamp `APPROVED (TL)` to eliminate token waste and guarantee delivery.
