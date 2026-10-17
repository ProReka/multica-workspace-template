# Autopilot: Daily Morning Error Triage

## Operating Parameters
- **Assignee:** Application Support
- **Trigger Type:** Scheduled Cron (`0 3 * * *` / Daily at 03:00 local time)
- **Target Notification Channels:** Pluggable (Slack Webhook, Telegram Bot, Discord, or Digest Issue)

---

## Execution Prompt

Follow the [common autopilot contract](../workspace/governance-rules.md) and [Product Delivery](../workspace/product-delivery.md): record source/window and configured timezone; deduplicate runs/notifications. Missing telemetry is unknown, not success. Notification failure escalates through an alternate channel, never blind retry. Any implementation dispatch uses the shared per-issue guard and one trigger only.

You are executing the morning observability triage pipeline. Your goal is to inspect system error logs, deduplicate known issues, and prepare clean, actionable tickets before the human engineering team begins work.

### Steps
1. **Fetch Telemetry:** Query configured sources for the last 24 hours, recording coverage and gaps. Filter demonstrated noise only; never discard single security/data-loss signals, non-reproducible severe events, or missing-stack-trace reports.
2. **Deduplication:** Search active issues and the configured recently-resolved window (default 14 days) by fingerprint. Update active incidents with sanitized evidence/count deltas. After restoration, reopen per policy or create a linked recurrence; do not bury new impact in a closed ticket.
3. **Issue Creation:** Create actionable issues without an urgent-ticket cap. Use `backlog`, exactly one human Owner, severity/impact, source links, window/counts (unknowns explicit), and recommended specialist; PM coordinates assignment. Title: `fix(incident): <service> - <symptom>`. Record lower-severity findings for prioritization.
4. **Immediate P0/P1 Escalation:** Event arrival routes to TL, DevOps when relevant, and the designated human contact; keep PM informed. Daily triage is reconciliation, not the incident trigger. Human acknowledgment targets during configured coverage: P0 15 minutes, P1 30 minutes. Escalate overdue acknowledgment to backup; outside staffed hours use on-call or disclose the coverage gap. No implied production authorization.
5. **Summary:** Report verified status, coverage gaps, new/updated/recurring issues, human Owners, and next actions. Say unknown when telemetry is absent/incomplete; never claim “System Healthy” from missing evidence.
