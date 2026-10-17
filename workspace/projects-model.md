# Project Portfolio & Domain Modeling Guide

The current Product Development team supports these product portfolio archetypes. These are software project boundaries, not implementations of finance, operations, or other business teams.

For each initiative, use the outcome and work contracts in `workspace/product-delivery.md`. Link the human Owner, approved scope and assumptions, success metric/baseline/target, delivery tasks, release record, dependencies, budget, and outcome checkpoint. A project portfolio alone is not authorization to dispatch work.

---

## Example Portfolio Configurations

### 1. B2B / Multi-Tenant SaaS
| Project Name | Lead Role | Scope & Objective |
|---|---|---|
| **Core Platform Engine** | Project Lead (Platform) | REST/GraphQL APIs, tenant isolation, auth, database scaling, background jobs. |
| **Web Customer Portal** | Project Lead (Frontend) | Responsive web app, dashboard metrics, customer onboarding, billing self-service. |
| **Integrations & Public API** | Project Lead (Ecosystem) | Developer documentation, public webhooks, SDKs, external partner connectors. |
| **Cloud Infrastructure & SRE** | DevOps Lead | IaC definitions, observability stack, autoscaling, zero-downtime deployment pipelines. |

### 2. Consumer E-Commerce & Retail
| Project Name | Lead Role | Scope & Objective |
|---|---|---|
| **Consumer Web & Mobile** | Project Lead (Consumer) | Product catalog, search & filtering, checkout flows, customer loyalty. |
| **Order & Inventory Engine** | Project Lead (Operations) | Stock management, cart processing, logistics/shipping integrations. |
| **Payment & Settlement Service**| Project Lead (Finance) | Payment gateway integration, escrow handling, ledger settlement, reconciliation. |
| **Merchant Backoffice** | Project Lead (Merchant) | Vendor store portal, analytics reporting, order fulfillment management. |

### 3. Digital Agency / Multi-Client Engineering
| Project Name | Lead Role | Scope & Objective |
|---|---|---|
| **Client Alpha Dedicated App**| Project Lead Alpha | Isolated client web/mobile platform with dedicated git repositories. |
| **Client Beta Service Revamp**| Project Lead Beta | Legacy modernization, database migration, performance optimization. |
| **Shared Core Libraries** | Senior Tech Lead | Reusable UI design system packages, common auth libraries, CI starter kits. |

---

## Project Configuration Checklist
1. **Clear Scope:** Define boundary between in-scope deliverables and out-of-scope backlog items.
2. **Single Lead:** Every project has a designated human Project Lead responsible for priorities.
3. **Repository Binding:** Link all source repositories relevant to the project domain.
4. **Issue Prefix:** Standardize issue prefixes for cross-referencing (e.g., `CORE-`, `WEB-`, `API-`).
