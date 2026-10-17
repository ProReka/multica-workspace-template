# Autopilot: Stuck Tasks Watchdog & Recovery

## Operating Parameters
- **Assignee:** Project Manager (single recovery coordinator)
- **Trigger Type:** Scheduled Cron (`0 */4 * * *` / Every 4 hours in the configured workspace timezone)
- **Target Notification Channels:** Internal Workspace Watchdog
- **Prerequisites:** Authoritative run-state inspection, durable recovery records, and an atomic per-issue dispatch guard shared with normal dispatch. Without these, report candidates to PM and human Owner; do not automatically retry.

---

## Execution Prompt

Detect failed executions and resume safely without duplicating work. Follow `workspace/governance-rules.md`; an inactive issue is not proof of a failed run.

### Steps
1. **Inspect Candidates:** Fetch assigned issues in `todo` or `in_progress`, their comments, checkpoints, and authoritative execution records. Exclude blocked issues, review/approval waits, cancelled work, and missing assignees.
2. **Evaluate Eligibility:** Automatic recovery requires ALL of the following:
   - The latest execution failed with a fatal runtime error or a runtime-confirmed timeout.
   - No progress update has been posted for more than 6 hours, measured from the later of the latest progress update or run start.
   - No execution is queued or running for the issue, and no future agreed checkpoint is pending.
   - A checkpoint or execution log identifies a safe resume point. Verify external side effects before repeating any operation; uncertainty requires human review.
   - Silence alone, a successful run, cancellation, missing timestamps, or unknown run state requires investigation, not automatic recovery.
3. **Claim & Recheck:** Atomically claim the per-issue dispatch guard and re-read eligibility. Deduplicate by issue ID and failed run ID. If already claimed, retried, or superseded, skip. Persist the dispatch intent before sending a trigger; ambiguous delivery must be reconciled, never blindly resent.
4. **Resume Once:** Post one recovery comment mentioning the assignee, including the failed run link, verified checkpoint, completed work, and required next evidence. Use the mention as the ONLY trigger; do not also reassign or change status. Record the comment ID, resulting run ID, and attempt count. Release the guard after dispatch is reconciled.
5. **Bound Retries:** Allow at most two automatic recovery attempts per issue episode, at most one per watchdog cycle and one per failed run. If an attempt remains unresolved at the next cycle, do not retrigger it; escalate with diagnostics to TL and human Owner. After the second attempt fails, stop automatic recovery. Reset the episode only after verified new progress or explicit human authorization; retain the audit history.
