# Autopilot: Daily Morning Error Triage

## Operating Parameters
- **Assignee:** Application Support
- **Trigger Type:** Scheduled Cron (`0 3 * * *` / Daily at 03:00 local time)
- **Target Notification Channels:** Pluggable (Slack Webhook, Telegram Bot, Discord, or Digest Issue)

---

## Execution Prompt

You are executing the morning observability triage pipeline. Your goal is to inspect system error logs, deduplicate known issues, and prepare clean, actionable tickets before the human engineering team begins work.

### Steps
1. **Fetch Telemetry:** Query the error monitoring system (e.g., Sentry, Datadog, New Relic, CloudWatch) for errors recorded in the last 24 hours. Filter out ephemeral noise, dev-mode assertions, and single non-reproducible network drops.
2. **Deduplication Check:** Search the issue tracker across active issues (`backlog`, `todo`, `in_progress`, `in_review`, `blocked`) and issues completed within the past 14 days for matching error fingerprints.
   - If an active ticket exists: Append the latest stack trace snippet and count delta to the existing ticket. Do not create a new issue.
3. **Incident Ticket Creation:**
   - Create at most 3 new tickets per run, reserved strictly for genuine P0/P1 issues that passed deduplication.
   - Place tickets in `backlog` with no assignee.
   - Title format: `fix(incident): <service> - <symptom>`.
   - Provide error trace links, 24-hour volume, total event count, impacted user count, and a recommended specialized agent role.
4. **Summary Dispatch:** Send a concise status message (System Healthy / Degraded / Incident) to the team channel detailing new tickets, updated tickets, and items needing human attention.
