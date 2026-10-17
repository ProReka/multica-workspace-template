# Autonomous Multi-Agent Workspace Framework

An architectural blueprint for building and operating autonomous multi-agent engineering organizations. This framework defines the division of labor between **Human Leadership** (*Human-in-the-Loop*) and **Autonomous AI Agents** across software engineering, DevOps, observability, design, and project delivery.

---

## 1. Architectural Philosophy & Pillars

### 1. Autonomous Project Delivery (No Human PM Required)
Task decomposition, Work Breakdown Structure (WBS), agent task assignment, dependency tracking, and daily standup digests are fully automated by the **Project Manager Agent**. Human team members focus on strategic direction, product vision, and final merge authorization.

### 2. Dual Quality & Safety Gates
- **Technical Review Gate:** Application changes require Technical Lead review (`APPROVED (TL)`). Pure infrastructure changes use DevOps self-review (`READY (DevOps)`); mixed application/infrastructure changes require both. Implementation agents hand off to humans only after the applicable gate.
- **Pragmatic Circuit-Breaker:** The Technical Lead is empowered to directly write and fix code during critical production incidents (P0/P1) or after 3 failed developer review rounds. This guarantees delivery and eliminates token waste.
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
agentic-workspace-template/
├── README.md                          # Framework architecture guide & replication handbook
├── workspace/                         # Governance policies & organizational operating models
│   ├── governance-rules.md            # 8-step delivery workflow & closed-loop handoff contract
│   ├── projects-model.md              # Domain portfolio archetypes (SaaS, E-Commerce, Agency)
│   ├── repository-catalog.md          # Architectural catalog mapping repositories to layers
│   ├── taxonomy-and-attributes.md     # Custom properties (Owner, Reviewers) & semantic labels
│   └── human-roles.md                 # Human governance matrix (Director, Leads, Engineers)
├── agents/                            # Production-grade prompt configurations for 11 agents
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
└── skills/                            # 5 Lean, non-conflicting core knowledge packs
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
   - Set the contents of `workspace/governance-rules.md` as the core workspace context.
   - Configure custom properties (`Owner`, `Reviewers`, `Risk Tier`, `Target Environment`) according to `workspace/taxonomy-and-attributes.md`.
2. **Link Repositories:**
   - Connect your organization repositories using the mapping principles in `workspace/repository-catalog.md`.
3. **Register Skills:**
   - Import the 5 folders in `skills/` into the workspace skills registry.
4. **Deploy Autonomous Agents:**
   - Create the 11 agents using the instruction prompts in `agents/`.
   - Bind the corresponding skills as documented in each agent's specification.
5. **Enforce Runtime Guardrails:**
   - Apply the permissions and approval controls in section 10 of `workspace/governance-rules.md`; prompts alone are not security controls.
6. **Pilot Before Scaling:**
   - Start with Project Manager, Technical Lead, one engineer, and one human Owner. Complete one small change through review and human merge; verify triggers do not create duplicate runs.
   - Add other roles as needed using `squads/core-engineering-squad.md`.
   - Enable the 5 autopilots only after verifying permissions, run-state inspection, recovery deduplication, notification channels, and the scheduler timezone.
