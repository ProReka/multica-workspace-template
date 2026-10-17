# Autopilot: Evening Delivery Wrap-up

## Operating Parameters
- **Assignee:** Project Manager
- **Trigger Type:** Scheduled Cron (`30 17 * * 1-5` / Weekdays at 17:30 local time)
- **Target Notification Channels:** Pluggable (Slack, Telegram, Discord, or Email Digest)

---

## Execution Prompt

You are generating the end-of-day delivery summary and scheduling autonomous agent workloads for overnight execution.

### Steps
1. **Daily Deliverables:** Detail all pull requests merged and features completed during the working day.
2. **Urgent Decision Gates:** Highlight any pending PRs or critical issues requiring human sign-off, merge approval, or elevated access before the end of the day.
3. **Overnight Autonomous Queue:**
   - Autonomous AI agents run 24/7. Identify ready tasks in the backlog (e.g., integration test suites, static analysis refactors, documentation updates, or initial technical drafts).
   - Verify that selected tasks have explicit acceptance criteria and dependencies resolved.
   - Assign and schedule these tasks for autonomous overnight execution.
4. **Summary Broadcast:** Post a factual summary to the team channel with exact counts of completed tasks, blocked items, and overnight scheduled initiatives.
