# Autopilot: Daily Standup & Blocker Digest

## Operating Parameters
- **Assignee:** Project Manager
- **Trigger Type:** Scheduled Cron (`30 8 * * 1-5` / Weekdays at 08:30 local time)
- **Target Notification Channels:** Pluggable (Slack, Telegram, Microsoft Teams, Discord)

---

## Execution Prompt

You are preparing the daily standup digest to synchronize human team members and autonomous agents prior to the morning sync.

### Steps
1. **Recent Completions:** List all issues merged and transitioned to `done` since the previous working day.
2. **Stalled & Blocked Items:** Identify all open issues in `in_progress`, `in_review`, or `blocked` that have had no progress or updates for more than 24 hours. For each item, record:
   - Issue Key & Title
   - Accountable Human Owner
   - Assigned Agent
   - Stated blocker or current waiting gate (`waiting for TL review`, `waiting for Owner merge`, `blocked on API dependency`).
3. **Owner Grouping:** Group active deliverables by human Owner.
4. **Actionable Priorities:** Recommend the top 3-5 high-priority focus items for the day, identifying the exact individual (human or agent) who needs to take action next.
5. **Dispatch:** Format the digest in concise, clear text and broadcast to the designated team chat channel.
