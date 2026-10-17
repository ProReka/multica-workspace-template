# Taxonomy, Custom Properties & Semantic Labels

Standard classification system for issues, PRs, and workstreams:

---

## 1. Custom Issue Properties

| Property Name | Property Type | Description |
|---|---|---|
| `Owner` | Actor (Member) | Single human accountable for the business deliverable, review sign-off, and final merge. |
| `Reviewers` | Multi-Actor | Secondary reviewers or domain specialists assigned to provide feedback. |
| `Risk Tier` | Single Select | `Routine` (standard automated verification) vs `High-Risk` (payment, security, infra, production data). |
| `Target Environment`| Single Select | Target deployment tier: `Development`, `Staging`, or `Production`. |

Record these additional fields in the issue body; extra custom properties are optional:
- **Record Type:** `Initiative`, `Delivery`, `Release`, `Incident`, or `Discovery`. Initiatives track outcomes; delivery records track accepted artifacts; release records track rollout verification.
- **Complexity:** `Standard` for a known bounded approach; `High` for uncertain architecture, cross-service contracts, or significant dependencies. High-complexity or High-Risk work requires a Technical Draft.
- **Risk:** Use `High-Risk` for money movement, permission/security boundaries, sensitive data, infrastructure, production changes, or irreversible actions. Unknown risk stays High-Risk pending assessment. PM proposes; TL/DevOps confirms; downgrades require documented human Owner and applicable reviewer agreement.
- **Checkpoint:** Named next action, responsible party, and timestamp or evaluation window.
- **Revision / Evidence:** Exact artifact revision and linked checks/approvals, including invalidation when the artifact changes.
- **Severity (incidents):** P0 outage/active breach/suspected data loss; P1 severe degradation or critical flow unavailable; lower severity follows approved backlog priority.

---

## 2. Universal Semantic Labels

| Label Name | Color Hex | Primary Usage |
|---|---|---|
| `feature` | `#22c55e` | New user-facing or platform capability |
| `bug` | `#ef4444` | Defect or unexpected system behavior |
| `incident-p0-p1` | `#991b1b` | Critical system outage or data-integrity issue requiring immediate resolution |
| `backend` | `#3b82f6` | Server-side logic, database schemas, queues, or API endpoints |
| `frontend` | `#0ea5e9` | Web user interfaces, client components, and web performance |
| `mobile` | `#ec4899` | Mobile application logic, screens, or build configurations |
| `infra-devops` | `#64748b` | Infrastructure as Code, CI/CD runners, cloud resources, networking |
| `security` | `#881337` | Vulnerability patching, access control, credential rotation |
| `tech-debt` | `#f59e0b` | Code refactoring, test additions, dependency upgrades |
| `ai-automation` | `#8b5cf6` | LLM prompts, model routing, automated workflow pipelines |
| `documentation` | `#6b7280` | Technical architecture docs, API references, onboarding guides |
