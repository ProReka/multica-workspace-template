# Human–AI Workspace Starter Kit

Current team: **Product Development**. Templates for human–AI collaboration, not an executable runtime. Platform system instructions, permissions, and workflow always take precedence.

## Provisioning Contract

**Do not concatenate this repository into agent prompts.** Each layer has a separate destination:

| Source | Destination | Loading |
|---|---|---|
| `agents/` role file | Agent instructions | Only that file, verbatim; no generated preamble or appended documents |
| `workspace/shared-context.md` | Workspace-wide context | Once, shared; not copied into every role |
| `skills/` | Runtime skill registry | Relevant skills, loaded when needed |
| `workspace/governance-rules.md`, `workspace/product-delivery.md` | Accessible reference documents | Relevant sections on demand, not permanent prompt text |
| `workspace/operational-readiness.md` | Human/operator setup records | Setup and acceptance testing only; never agent instructions |
| `autopilots/`, `squads/` | Corresponding runtime configuration | Only when explicitly enabled |

If shared context or document retrieval is unavailable, disclose the limitation and provide a verified reference mechanism. Do not solve it by embedding every document into every agent. Runtime identity directories and permission controls remain the source for identities and access; do not generate long personalized boundary essays.

## Resetting an Existing Workspace

1. Confirm the target workspace and exact agent IDs with the human. Limit changes to explicitly selected configuration; do not delete issues, artifacts, or unrelated agents.
2. Replace each selected agent's entire instructions with its matching role file. Do not append to the existing instructions. Keep display names, models, tools, and permissions unless separately authorized.
3. Remove previously imported document copies from those instructions. Install shared context once; register skills and references separately. Never remove platform-owned system instructions or safety controls.
4. Keep schedules and dispatch disabled unless separately approved. Configuration changes do not authorize pilot runs, commits, publication, merges, or deployments.
5. Read instructions back from the platform. Confirm they match the role file; no governance/playbook/readiness blocks or workspace-specific essay should be present. Report configuration results and limitations, not runtime readiness.

This repository revision does not reset any remote workspace by itself.

## Example

For a backend developer, paste only `agents/backend-engineer.md` into agent instructions. It starts with “You are the Backend Engineer” and describes implementation, verification, boundaries, and handoff—not the organization's setup history.

## Adoption & Maintenance

Follow `workspace/operational-readiness.md` for permissions, setup tests, and a real pilot. Run `python3 checks/check_template.py` for source consistency and role-prompt size checks; it does not certify runtime enforcement.

Role names describe responsibilities, not fixed display names. Multica mention syntax lives in shared context. Repositories may use any host or naming convention; use `workspace/repository-catalog.md` to reference existing locations and instructions.

Keep each rule in its owning document. Do not repeat file inventories, counts, or deployment records across prompts.

## Future Teams — Coming Soon

Marketing; Sales; Customer Experience; Finance & Accounting; Legal; People & Organization; Corporate Strategy; Business Operations; Procurement; Manufacturing; Logistics & Distribution; Quality Management; IT & Workplace Technology; Security; Risk & Compliance; Data & Analytics; Research & Innovation; Facilities & Asset Management; Corporate Development & Investor Relations.

Only Product Development is implemented. Current specialists support that team, not standalone business teams. Future domains will use their own artifacts and approval controls; no delivery dates are promised.
