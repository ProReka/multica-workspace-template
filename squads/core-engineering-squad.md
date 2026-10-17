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
- Application PRs and non-PR deliverables require **Technical Lead** review. Pure infrastructure uses `READY (DevOps)`; mixed changes require both gates. Human handoff occurs only after the applicable gates.
- The Technical Lead evaluates the PR against functional acceptance criteria, test coverage, and security boundaries.
- **Circuit-Breaker Intervention:** If a sub-task encounters 3 failed review rounds or blocks a P0/P1 delivery, the Technical Lead steps in directly, finishes the code, and stamps approval to prevent token exhaustion.

### 3. Parent Delivery Roll-Up
- The parent issue remains in `in_progress` while sub-tasks are active.
- The parent issue moves to `in_review` only when all children pass the applicable technical gates with verified evidence; mixed changes require both approvals.
- The Project Manager compiles evidence for human acceptance and merge. Completion follows governance step 8, including explicit Owner acceptance for non-PR deliverables and completion of all children.
