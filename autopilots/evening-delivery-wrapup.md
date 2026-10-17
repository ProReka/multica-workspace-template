# Autopilot: Evening Delivery Wrap-up

## Operating Parameters
- **Assignee:** Project Manager
- **Trigger Type:** Scheduled Cron (`30 17 * * 1-5` / Weekdays at 17:30 local time)
- **Target Notification Channels:** Pluggable (Slack, Telegram, Discord, or Email Digest)

---

## Execution Prompt

Follow the [common autopilot contract](../workspace/governance-rules.md) and [Product Delivery](../workspace/product-delivery.md): record source/window and configured timezone; deduplicate runs/notifications; missing telemetry is unknown, not success. Notification failure escalates through an alternate channel, never blind retry. Dispatch uses the shared per-issue guard and one trigger only.

You are generating the end-of-day delivery summary and scheduling autonomous agent workloads for overnight execution.

### Steps
1. **Daily Deliverables:** List verified human merges and accepted non-PR artifacts in the working-day window; distinguish delivery from authorized release and measured outcome.
2. **Urgent Decision Gates:** Highlight any pending PRs or critical issues requiring human sign-off, merge approval, or elevated access before the end of the day.
3. **Overnight Autonomous Queue:**
   - Select only explicitly approved, scoped, ready-to-start tasks with human Owner, acceptance criteria, dependencies resolved, required draft/approvals, and checkpoints.
   - Confirm agent/review capacity, execution budget/runtime limit, configured coverage/contact, and a safe stop condition. No assumed 24/7 coverage or authorization; park tasks when these are absent.
   - Dispatch within approved scope using the shared per-issue guard and exactly one trigger (status assignment OR mention). Human decision waits remain parked; no overnight production authority is implied.
4. **Summary Broadcast:** Post a factual summary to the team channel with exact counts of completed tasks, blocked items, and overnight scheduled initiatives.
