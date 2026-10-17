# Workspace Governance & Operating Rules

These rules apply universally to all autonomous AI agents and human collaborators in this workspace. Role-specific instructions extend these rules; they never override or cancel them.

---

## 1. Architecture & System Ecosystem
Organizations operate across modern modular or distributed architectures:
- **Client Interfaces:** Responsive web applications and mobile clients (iOS, Android, cross-platform).
- **Core Platform & Services:** High-throughput backend services, monolithic engines, or microservices managing core business logic, transactional records, and data persistence.
- **Auxiliary & Specialized Engines:** Async queues, event buses, AI/LLM automation pipelines, and third-party partner integrations.
- **Infrastructure Layer:** Cloud infrastructure managed via Infrastructure as Code (IaC), container orchestration, and automated CI/CD runners.
- **Architectural Single Source of Truth:** Any cross-service change touching data contracts, database schemas, or API interfaces requires technical alignment with the **Technical Lead** before implementation begins.

---

## 2. Team Structure & Authority Matrix

### Human Team
Human mentions notify individuals for consultation, business decisions, and approval gates. Human mentions **never** trigger autonomous agent execution runs.

| Role | Responsibility & Authority | Mention Syntax |
|---|---|---|
| **Workspace Director** | Executive leadership. Approves High-Risk actions (production deployments, budget/cloud spending, sensitive data, security policies). | `[@Workspace Director](mention://member/[DIRECTOR_ID])` |
| **Project Lead** | Domain/product owner. Defines WHAT and WHY (goals, scope, priority, acceptance criteria) and acts as the accountable Issue Owner. | `[@Project Lead](mention://member/[PROJECT_LEAD_ID])` |
| **Senior Engineer** | Human engineering staff. Reviews critical architecture, provides secondary sign-off, and merges pull requests. | `[@Senior Engineer](mention://member/[SENIOR_ENG_ID])` |
| **Dynamic Roles** | Adaptable per organization: Human PM, Human DevOps, Operations, Finance Admin, Domain Specialists. | `[@<Role Name>](mention://member/[MEMBER_ID])` |

### Autonomous Agent Team
Agent mentions with official URI links initiate execution runs. Plain text mentions do nothing.

| Role | Core Function | Mention Syntax |
|---|---|---|
| **Project Manager** | Work breakdown (WBS), agent task assignment, blocker tracking, stakeholder sync. | `[@Project Manager](mention://agent/[PM_ID])` |
| **Technical Lead** | Technical architecture, technical drafts, code review gate, and circuit-breaker coding. | `[@Technical Lead](mention://agent/[TL_ID])` |
| **Backend Engineer** | Polyglot backend service implementation, API endpoints, database schemas, unit tests. | `[@Backend Engineer](mention://agent/[BACKEND_ID])` |
| **Frontend Engineer** | Web user interfaces, design system compliance, client state, web performance. | `[@Frontend Engineer](mention://agent/[FRONTEND_ID])` |
| **Mobile Engineer** | Mobile clients, native/cross-platform modules, build pipeline, secure app storage. | `[@Mobile Engineer](mention://agent/[MOBILE_ID])` |
| **DevOps Engineer** | IaC, container platforms, CI/CD runners, cloud resources, production change reviews. | `[@DevOps Engineer](mention://agent/[DEVOPS_ID])` |
| **AI Engineer** | LLM services, schema-validated outputs, prompt engineering, RAG, workflow automation. | `[@AI Engineer](mention://agent/[AI_ENG_ID])` |
| **Application Support** | Observability, error monitoring triage, deduplication, P0/P1 incident ticketing. | `[@Application Support](mention://agent/[APP_SUPPORT_ID])` |
| **Data Analyst** | Read-only SQL query analysis, metric verification, executive dashboards and reports. | `[@Data Analyst](mention://agent/[DATA_ANALYST_ID])` |
| **UI/UX Designer** | Production-ready screen specs, design system tokens, WCAG 2.2 accessibility, UX flows. | `[@UI/UX Designer](mention://agent/[DESIGNER_ID])` |
| **Technical Writer** | System documentation, OpenAPI/API schemas, ADR curation, verified knowledge base. | `[@Technical Writer](mention://agent/[TECH_WRITER_ID])` |

---

## 3. Issue Ownership & Accountability
Every issue must have **exactly one human Owner**:
1. Defined via the custom issue property `Owner`, or the first line of the issue description: `Owner: <Role/Name>`.
2. Fallback: The **Project Lead** of the associated project.
3. The Owner is accountable for business scope decisions, reviews the work after Technical Lead approval, and performs the final merge.

---

## 4. End-to-End Delivery Workflow (8-Step Cycle)

```text
[1. Intake & Assignment] ──> [2. Technical Draft] ──> [3. Implementation] ──> [4. Request TL Review]
                                                                                     │
[8. Done] <── [7. Human Merge Gate] <── [6. TL Approved] <── [5. Review Gate & Circuit-Breaker]
```

1. **Assignment:** Only Project Manager, Technical Lead, or DevOps Engineer assign agents. Other agents creating issues leave them in `backlog` unassigned and mention the Project Manager.
2. **Technical Draft:** Mandatory for High-complexity issues, optional otherwise. Technical Lead specifies approach, affected files, data contracts, risks, and acceptance criteria before implementation.
3. **Implementation:** The assigned developer:
   - Reads the issue and comments; clarifies unknowns before coding.
   - Sets status to `in_progress`, checks out a dedicated branch, and posts a short plan.
   - Writes clean, self-documenting code with unit/integration tests and zero linter warnings.
   - Opens a Pull Request adhering to Conventional Commits and attaches verification evidence.
4. **Request Review:** Developer sets status to `in_review` and comments:
   `[@Technical Lead](mention://agent/[TL_ID]) please review: <PR URL> — summary, tests run, risks.`
   *Developers never request human review or merge directly.*
5. **Review Gate & Pragmatic Circuit-Breaker:**
   - Technical Lead inspects diff accuracy, test coverage, security boundaries, and acceptance criteria.
   - If changes are needed: TL provides numbered, actionable feedback and mentions the developer.
   - **Pragmatic Circuit-Breaker:** After 3 failed review rounds, or immediately during critical production incidents (P0/P1), the Technical Lead has full authority to directly take over the branch, write or fix the required code, run tests, and complete delivery. This prevents token waste and eliminates infinite review loops.
6. **TL Approved:** Technical Lead posts `APPROVED (TL)` summarizing changes, risk tier (Routine or High-Risk), PR link, and mentions the human Owner.
7. **Human Merge Gate:** Merge is performed exclusively by humans (Owner, Senior Engineer, or Workspace Director for High-Risk changes). Agents are strictly forbidden from merging into protected branches (`main`, `master`, `production`).
8. **Done:** An issue transitions to `done` only after the PR is merged by a human.

---

## 5. Pull Request & Commit Standards
- **Conventional Commits Mandatory:** All commit messages and PR titles must strictly follow Conventional Commits (e.g., `feat(auth): add OAuth2 provider support`, `fix(api): resolve race condition in token refresh`).
- **No Issue Keys in PR Titles:** Do NOT prefix PR titles with issue keys. Link issue keys cleanly inside the PR body or comments (e.g., `Closes #[PREFIX]-123` or `Ref: #[PREFIX]-123`).
- **Branch Protection:** Never push directly to `main`, `master`, `develop`, or `production`. Never force-push or bypass branch protection rules.

---

## 6. Agent Run Trigger Mechanics
- Agent execution starts only when:
  a. An issue is assigned to the agent with an active status (`todo`, `in_progress`).
  b. The agent is invoked via an official mention URI link.
- **One trigger per step:** Use status assignment OR mention, never both simultaneously.
- Status `backlog` parks work; assigning in backlog triggers nothing.

---

## 7. Review Evidence Standards
- Evidence is required for every Pull Request to enable informed human review and prevent blind merging.
- **Visual Evidence Preferred (Not Mandatory):** For UI, frontend, and mobile changes, visual artifacts (screenshots, video recordings) are strongly preferred.
- **Technical Evidence:** For backend, logic, data, and infrastructure tasks, terminal test outputs, benchmark metrics, linter execution logs, or dry-run execution plans are fully valid evidence.
- *Rule:* No evidence = not done.

---

## 8. Code Standards & Comments
- **Self-Documenting Code:** Write clean, expressive, readable code. Minimize inline comments.
- **No Ticket References in Code:** NEVER write issue keys, ticket identifiers, or task URLs into source code comments. Tracking belongs in commit metadata and issue management systems, not the codebase.

---

## 9. Closed-Loop Handoff Contract
Every actionable update between collaborators must provide:
1. **Decision:** Current verified fact, disposition, or blocker.
2. **Next Action:** Concrete single next step.
3. **Responsible Party:** Exactly one designated agent or person.
4. **Required Evidence:** Verifiable artifacts required to proceed.
5. **Agreed Checkpoint:** Clear timeframe or evaluation milestone.
