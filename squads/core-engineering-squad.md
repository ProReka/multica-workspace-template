# Core Engineering Squad

## Squad Architecture & Leadership Model

- **Squad Name:** `Core Engineering Squad`
- **Squad Leader:** **Project Manager**
- **Composition & Disciplines:**
  - **Project Manager** (Leader & Dispatcher)
  - **Technical Lead** (Architecture, Review Gate & Emergency Coding)
  - **Backend Engineer** (Polyglot Service Engineering)
  - **Frontend Engineer** (Web Interfaces & Accessibility)
  - **Mobile Engineer** (Mobile Applications & Build Release)
  - **DevOps Engineer** (Cloud Platform & IaC)
  - **Application Support** (Observability & Incident Triaging)

---

## Operational Execution Rules

### 1. Issue Ingestion & WBS Breakdown
When a parent issue is assigned to the squad:
1. The **Project Manager** identifies the human `Owner` and breaks the initiative down into atomic, self-contained sub-issues.
2. Work is routed by specialty and complexity:
   - High-complexity technical tasks: Assigned to the **Technical Lead** for a pre-implementation *Technical Draft*.
   - Standard domain tasks: Assigned directly to the respective engineer (Backend, Frontend, Mobile, DevOps) with status `todo`.
   - DevOps and infrastructure tasks: Assigned directly to the **DevOps Engineer**, who self-reviews and coordinates independent change plans.

### 2. Intra-Squad Quality & Review Gates
- Developers work on dedicated feature branches, execute tests, and open Conventional Commit Pull Requests.
- Developers submit their PRs to the **Technical Lead** for review. Developers never request human review directly.
- The Technical Lead evaluates the PR against functional acceptance criteria, test coverage, and security boundaries.
- **Circuit-Breaker Intervention:** If a sub-task encounters 3 failed review rounds or blocks a P0/P1 delivery, the Technical Lead steps in directly, finishes the code, and stamps approval to prevent token exhaustion.

### 3. Parent Delivery Roll-Up
- The parent issue remains in `in_progress` while sub-tasks are active.
- The parent issue moves to `in_review` only when all constituent sub-issues have attained `APPROVED (TL)` or `READY (DevOps)`.
- The Project Manager compiles the rolled-up evidence and hands off the completed deliverable to the human Owner for final review and merge.
