# Human–AI Workspace Starter Kit

Current team: **Product Development**. Operating templates for humans and AI agents delivering measurable product outcomes. This is not an executable runtime or a claim of production readiness.

## Start Here

1. Load `workspace/governance-rules.md` as authoritative policy and `workspace/product-delivery.md` as the domain playbook.
2. Follow `workspace/operational-readiness.md` for setup, runtime enforcement, sandbox benchmarks, and a real pilot.
3. Enable only the roles, skills, and automations needed. Source templates live in `agents/`, `skills/`, `squads/`, and `autopilots/`.
4. Run `python3 checks/check_template.py` for source consistency. Runtime behavior must be tested separately.

## Adaptation

Role names describe responsibilities, not required display names. Resolve actual agents, members, repositories, and permissions from the target workspace. Multica mention syntax is defined once in governance; setup records hold actual identities.

Repositories may use any host or naming convention. Record existing locations and access boundaries using `workspace/repository-catalog.md`; do not rename repositories to fit this template.

Maintain each rule in its owning document. Other documents should link to it rather than repeat inventories, counts, or policy details. Deployed workspaces own their configuration; this source remains reusable.

## Future Teams — Coming Soon

Only Product Development is implemented. Planned domain templates:

- Marketing; Sales; Customer Experience; Finance & Accounting.
- Legal; People & Organization; Corporate Strategy; Business Operations.
- Procurement; Manufacturing; Logistics & Distribution; Quality Management.
- IT & Workplace Technology; Security; Risk & Compliance; Data & Analytics.
- Research & Innovation; Facilities & Asset Management; Corporate Development & Investor Relations.

Current support specialists serve Product Development, not standalone business teams. Future templates will share governance concepts but use domain-specific artifacts, evidence, and approval controls. No delivery dates are promised.
