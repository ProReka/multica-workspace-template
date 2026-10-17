# Architecture Repository Catalog

Catalog template mapping organization repositories to architectural tiers, technology stacks, and access patterns:

| Architectural Tier | Component Type | Typical Tech Stack | Repository Template Pattern |
|---|---|---|---|
| **Client Layer** | Web Frontend Application | Next.js, React, Vue, Svelte, Tailwind CSS | `https://github.com/[ORG_NAME]/[APP_NAME]-web.git` |
| **Client Layer** | Mobile Native / Cross-Platform | Flutter, React Native, Swift, Kotlin | `https://github.com/[ORG_NAME]/[APP_NAME]-mobile.git` |
| **API & Core Logic** | Backend Service / Monolith | Node.js, Go, Python (FastAPI), PHP (Laravel), Java | `https://github.com/[ORG_NAME]/[APP_NAME]-core-api.git` |
| **Specialized Service** | Payment / Ledger Service | Go, Java, Python, Node.js, PostgreSQL | `https://github.com/[ORG_NAME]/[APP_NAME]-payment-service.git` |
| **Specialized Service** | Notification & Messaging | Node.js, Go, Redis, RabbitMQ, Kafka | `https://github.com/[ORG_NAME]/[APP_NAME]-notification-service.git` |
| **AI & Workflow Engine**| LLM Pipelines & Automation | Python (LangChain, LlamaIndex), Node.js, n8n | `https://github.com/[ORG_NAME]/[APP_NAME]-ai-engine.git` |
| **Infrastructure** | Infrastructure as Code (IaC) | Terraform, OpenTofu, Pulumi, CloudFormation | `https://github.com/[ORG_NAME]/infra-terraform.git` |
| **Documentation** | Central Knowledge Base & Specs| Markdown, Docusaurus, Astro Starlight, OpenAPI | `https://github.com/[ORG_NAME]/documentation.git` |

---

## Repository Hygiene for Autonomous Agents
- **Isolated Branching:** Agents work exclusively on feature or fix branches (`feat/<scope>-description` or `fix/<scope>-description`).
- **Build Respect:** Agents inspect existing package manifests (`package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`) and execute existing test scripts without introducing unsolicited tooling changes.
- **Commit Purity:** Strictly follow Conventional Commits. Clean history without merge commits in PR branches.
