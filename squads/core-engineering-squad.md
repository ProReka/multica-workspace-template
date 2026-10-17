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

Follow [Product Delivery](../workspace/product-delivery.md); governance remains authoritative. PM owns intake completeness, ready-work dispatch, separate delivery/release/outcome records, and the evidence-based operating review.

### Optional Existing Specialists
PM may route bounded work to existing **UI/UX Designer**, **AI Engineer**, **Data Analyst**, and **Technical Writer** as needed; no new agents or mandatory squad expansion. Non-PR artifacts require TL review and explicit human Owner acceptance.

### 1. Issue Ingestion & WBS Breakdown
When a parent issue is assigned to the squad:
1. The **Project Manager** identifies the human `Owner` and breaks the initiative down into atomic, self-contained sub-issues.
2. Work is routed by specialty and complexity:
   - High-complexity OR High-Risk tasks: Route first to **Technical Lead** for a pre-implementation *Technical Draft*, coordinating infrastructure plans with DevOps.
   - Dispatch only approved ready-to-start work within scope, budget, agent/review capacity, and coverage; use the shared per-issue guard and one trigger.
   - Standard domain tasks: Assigned directly to the respective engineer (Backend, Frontend, Mobile, DevOps) with status `todo`.
   - DevOps and infrastructure tasks: Assigned directly to the **DevOps Engineer**, who self-reviews and coordinates independent change plans.

### 2. Intra-Squad Quality & Review Gates
- Developers work on dedicated feature branches, execute tests, and open Conventional Commit Pull Requests.
- Application PRs and non-PR deliverables require **Technical Lead** review. Pure infrastructure uses `READY (DevOps)`; mixed changes require both gates. Human handoff occurs only after the applicable gates.
- The Technical Lead evaluates the PR against functional acceptance criteria, test coverage, and security boundaries.
- **Circuit-Breaker Intervention:** After 3 failed review rounds or for P0/P1, TL may take over and verify fixes without bypassing human gates. Critical flows require independently executed verification; TL-authored code/fixes require a human verifier.
- Approvals bind the exact artifact revision; changes invalidate affected approvals/checks and require fresh verification and approval. Missing evidence blocks handoff.

### 3. Parent Delivery Roll-Up
- The parent issue remains in `in_progress` while sub-tasks are active.
- The parent issue moves to `in_review` only when all children pass the applicable technical gates with verified evidence; mixed changes require both approvals.
- The Project Manager compiles evidence for human acceptance and merge. Completion follows governance step 8, including explicit Owner acceptance for non-PR deliverables and completion of all children.
