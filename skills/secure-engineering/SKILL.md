---
name: secure-engineering
description: Enterprise secure coding guardrails. Enforces zero-secret leakage, input validation boundaries, defense against prompt injection, and OWASP Top 10 mitigations.
---

# Secure Engineering Guardrails

## 1. Zero-Secret Leakage Policy
- **Absolute Prohibition:** Never commit passwords, API keys, private certificates, JWT secrets, or raw `.env` files into source control repositories.
- **Runtime Injection:** All secrets must be injected at runtime via environment variables or cloud secret managers.
- **Client Bundle Protection:** Assets compiled into web or mobile client bundles are publicly extractable. Never include private service credentials in client-side code.

## 2. Input Sanitization & Trust Boundaries
- **Never Trust Input:** Validate all incoming parameters (headers, query params, request bodies) against strict validation schemas at the network boundary.
- **SQL Injection Prevention:** Exclusively use parameterized queries and ORM abstractions. Raw SQL concatenation is forbidden.
- **Output Encoding:** Ensure all dynamic output rendered in web views is properly context-encoded to prevent Cross-Site Scripting (XSS).

## 3. AI Safety & Prompt Injection Defense
- Treat all external user prompts as untrusted content.
- Never incorporate system credentials, internal API keys, or proprietary data into system prompt contexts that can be leaked via prompt extraction attacks.
- Enforce strict JSON schema validation on all model responses before executing business actions.
