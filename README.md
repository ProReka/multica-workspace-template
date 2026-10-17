# Human–AI Workspace Starter Kit

Current team: **Product Development**. A reusable operating specification for humans and AI agents delivering measurable product outcomes: discovery, design, engineering, verification, release, and learning.

This is a starter kit and acceptance benchmark, not a running platform or a claim of production readiness. It contains 11 agents and 5 skills; enable only those your workspace needs. Other business teams are **coming soon**.

## Start Here

1. Read the authoritative policy: `workspace/governance-rules.md`.
2. Use `workspace/product-delivery.md` for outcome, readiness, quality, release, and evaluation contracts.
3. Complete `workspace/operational-readiness.md`; run the sandbox benchmark and a real pilot before enabling production automation.
4. Validate this source with `python3 checks/check_template.py`. Static checks do not validate runtime enforcement.

**Architecture:** shared ownership, evidence, approvals, handoff, escalation, and audit form the reusable foundation. PRs, CI, releases, and rollback are the current Product Development domain. Future teams will use domain-specific artifacts and controls; they are not implemented here.

---

## 1. Architectural Philosophy & Pillars

### 1. Outcome-Led Product Delivery
The **Project Manager Agent** coordinates scope, task decomposition, dispatch, dependencies, evidence, and reporting within approved limits. Humans own product decisions, priorities, budgets, acceptance, and production authorization. Delivery, release, and outcome evaluation remain distinct; completed tasks do not prove customer value.

### 2. Dual Quality & Safety Gates
- **Technical Review Gate:** Application changes require Technical Lead review (`APPROVED (TL)`). Pure infrastructure changes use DevOps self-review (`READY (DevOps)`); mixed application/infrastructure changes require both. Implementation agents hand off to humans only after the applicable gate.
- **Pragmatic Circuit-Breaker:** The Technical Lead is empowered to directly write and fix code during critical production incidents (P0/P1) or after 3 failed developer review rounds. Authorship must be disclosed; human gates remain mandatory. Critical self-authored changes require independent human verification.
- **Human Merge Gate:** Protected branch merges (`main`, `master`, `production`) are strictly reserved for humans (Project Lead, Senior Engineer, Workspace Director). Autonomous agents cannot merge into protected branches.

### 3. Industry-Agnostic & Polyglot
- Designed for diverse domains: B2B SaaS, E-Commerce, Digital Agencies, FinTech, and internal developer tooling.
- True polyglot backend capability (TypeScript/Node.js, Go, Python, PHP, Java, Rust).
- Architecture-first terminology (*Error Monitoring System*, *Cloud Infrastructure Provider*, *Infrastructure as Code*) rather than vendor lock-in.

### 4. Git Hygiene & Review Standards
- **Conventional Commits Mandatory:** PR titles follow `<type>(<scope>): <summary>` strictly. No issue keys in PR titles.
- **Evidence-Driven Review:** Evidence (test logs, benchmarks, or visual screenshots) is required on every PR to prevent blind review. Visual evidence is preferred for UI changes, but not mandatory.
- **Self-Documenting Code:** Minimal inline comments. Writing issue tracking keys or ticket numbers in source code comments is strictly forbidden.

---

## 2. Directory Structure

```text
multica-workspace-template/
├── README.md                          # Framework architecture guide & replication handbook
├── workspace/                         # Governance policies & organizational operating models
│   ├── governance-rules.md            # Authoritative policy, approval & runtime contracts
│   ├── product-delivery.md            # Outcome, readiness, quality, release & evaluation
│   ├── operational-readiness.md       # Setup record, activation sequence & benchmark
│   ├── projects-model.md              # Domain portfolio archetypes (SaaS, E-Commerce, Agency)
│   ├── repository-catalog.md          # Architectural catalog mapping repositories to layers
│   ├── taxonomy-and-attributes.md     # Custom properties (Owner, Reviewers) & semantic labels
│   └── human-roles.md                 # Human governance matrix (Director, Leads, Engineers)
├── agents/                            # Role prompt templates for 11 agents
│   ├── project-manager.md             # WBS, agent assignment, blocker tracking & daily sync
│   ├── technical-lead.md              # Architecture, review gate & emergency coding circuit-breaker
│   ├── backend-engineer.md            # Polyglot backend service engineering & database optimization
│   ├── frontend-engineer.md           # Modern web interfaces, accessibility (WCAG 2.2) & state
│   ├── mobile-engineer.md             # Mobile apps (Flutter/React Native/Native), secure storage
│   ├── devops-engineer.md             # Cloud platforms, IaC plan-first guardrails & CI/CD
│   ├── ai-engineer.md                 # LLM services, schema-validated outputs, prompt engineering
│   ├── application-support.md         # Observability, error log deduplication & incident triage
│   ├── data-analyst.md                # Read-only SQL analytics, BI dashboards & data integrity
│   ├── ui-ux-designer.md              # Design system tokens, anti-generic specs & state matrices
│   ├── technical-writer.md            # Central documentation, OpenAPI schemas & verified facts
├── squads/                            # Standing multi-disciplinary execution units
│   └── core-engineering-squad.md      # Core squad topology, leadership dispatch & handoffs
├── autopilots/                        # Pluggable scheduled & event-driven automations
│   ├── morning-error-triage.md        # Pre-workday error monitoring triage (03:00)
│   ├── daily-standup-digest.md        # Morning standup & blocker summary (08:30)
│   ├── evening-delivery-wrapup.md     # EOD delivery summary & overnight workload planning (17:30)
│   ├── stuck-tasks-recovery.md        # Autonomous watchdog for halted or failing agent runs
│   └── inbound-chat-router.md         # Inbound chat & webhook router (Slack, Telegram, Discord)
├── checks/check_template.py            # Dependency-free source consistency check
└── skills/                            # 5 shared knowledge packs
    ├── project-delivery/              # WBS, RACI, three-point estimation & change control
    ├── technical-leadership/          # Architecture guidelines, review gate & circuit-breaker
    ├── ui-ux-design-system/           # Tokens, WCAG 2.2 accessibility & anti-generic principles
    ├── specification-builder/         # Structured requirements synthesis from discussions
    └── secure-engineering/            # Enterprise AppSec, zero-secret leakage & input boundaries
```

---

## 3. Template Placeholder Dictionary

When replicating this blueprint to a new organization, replace these placeholders:

| Placeholder | Meaning / Function | Example Replacement |
|---|---|---|
| `[COMPANY_NAME]` | Organization or Company Name | Acme Technologies / Global Retail Inc. |
| `[COMPANY_DOMAIN]` | Primary Organization Domain | acme.com / globalretail.io |
| `[ORG_NAME]` | Git Version Control Account/Org | acme-tech / global-retail |
| `[PREFIX]` | Issue Tracker Key Prefix | ACM / CORE / ENG |
| `[APP_NAME]` | Core Product or Application Slug | platform / web-portal |
| `[DIRECTOR_ID]` | Workspace Director Account Identifier | UUID of executive director |
| `[PROJECT_LEAD_ID]` | Project Lead Account Identifier | UUID of domain/product owner |
| `[SENIOR_ENG_ID]` | Senior Engineer Account Identifier | UUID of human technical reviewer |
| `[PM_ID]` | Project Manager Agent Identifier | Agent UUID |
| `[TL_ID]` | Technical Lead Agent Identifier | Agent UUID |
| `[BACKEND_ID]` | Backend Engineer Agent Identifier | Agent UUID |
| `[FRONTEND_ID]` | Frontend Engineer Agent Identifier | Agent UUID |
| `[MOBILE_ID]` | Mobile Engineer Agent Identifier | Agent UUID |
| `[DEVOPS_ID]` | DevOps Engineer Agent Identifier | Agent UUID |
| `[AI_ENG_ID]` | AI Engineer Agent Identifier | Agent UUID |
| `[APP_SUPPORT_ID]` | Application Support Agent Identifier | Agent UUID |
| `[DATA_ANALYST_ID]` | Data Analyst Agent Identifier | Agent UUID |
| `[DESIGNER_ID]` | UI/UX Designer Agent Identifier | Agent UUID |
| `[TECH_WRITER_ID]` | Technical Writer Agent Identifier | Agent UUID |

---

## 4. Quickstart: Replicating to a New Workspace

This repository contains policy and prompt templates, not an executable runtime. `workspace/governance-rules.md` is the authoritative policy; role prompts and skills extend it. Configure permissions, scheduling, issue transitions, and integrations in your runtime before enabling agents.

1. **Initialize Governance:**
   - Create a workspace on your agent runtime platform.
   - Load `workspace/governance-rules.md` and `workspace/product-delivery.md` as shared context for every enabled agent.
   - Complete the setup record in `workspace/operational-readiness.md`, including runtime-specific trigger mapping, contacts, coverage, budgets, and permissions.
   - Configure custom properties (`Owner`, `Reviewers`, `Risk Tier`, `Target Environment`) according to `workspace/taxonomy-and-attributes.md`.
2. **Link Repositories:**
   - Connect your organization repositories using the mapping principles in `workspace/repository-catalog.md`.
3. **Register Skills:**
   - Import the 5 folders in `skills/` into the workspace skills registry.
4. **Deploy Autonomous Agents:**
   - Register the needed roles from the 11 agents in `agents/`; keep unused roles disabled. Start with PM, TL, and one engineer.
   - Bind the corresponding skills as documented in each agent's specification.
5. **Enforce Runtime Guardrails:**
   - Apply the permissions and approval controls in section 10 of `workspace/governance-rules.md`; prompts alone are not security controls.
6. **Pilot Before Scaling:**
   - Follow `workspace/operational-readiness.md`: run the sandbox benchmark, then one small real change through human acceptance, authorized release, verification, and an outcome checkpoint. Include a separate human reviewer where independent verification is required.
   - Add other roles as needed using `squads/core-engineering-squad.md`.
   - Enable autopilots individually only after their applicable benchmark scenarios pass. Production automation requires recorded human go-live approval.

## 5. Future Teams — Coming Soon

Only Product Development is implemented. Planned team templates, with domain-specific approval and evidence controls:

| Status | Teams |
|---|---|
| Coming soon | Marketing; Sales; Customer Experience; Finance & Accounting |
| Coming soon | Legal; People & Organization; Corporate Strategy; Business Operations |
| Coming soon | Procurement; Manufacturing; Logistics & Distribution; Quality Management |
| Coming soon | IT & Workplace Technology; Security; Risk & Compliance; Data & Analytics |
| Coming soon | Research & Innovation; Facilities & Asset Management; Corporate Development & Investor Relations |

Current engineering support roles (DevOps, analyst, designer, support) serve Product Development; they do not imply those standalone teams are implemented. No delivery dates or autonomous authority are promised for future teams.
