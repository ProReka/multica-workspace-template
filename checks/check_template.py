"""Run with: python3 checks/check_template.py"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text()
agent_count = len(list((root / "agents").glob("*.md")))
assert set(re.findall(r"(\d+) agents", readme)) == {str(agent_count)}, "README agent count is stale"

for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for reference in re.findall(r"`((?:workspace|agents|autopilots|squads|skills)/[^`]+\.md)`", path.read_text()):
        assert (root / reference).is_file(), f"{path}: missing {reference}"

governance = (root / "workspace/governance-rules.md").read_text()
assert all(gate in governance for gate in ("APPROVED (TL)", "READY (DevOps)"))
assert "Non-PR work is `done` only" in governance
assert "both `APPROVED (TL)` and `READY (DevOps)`" in governance
recovery = (root / "autopilots/stuck-tasks-recovery.md").read_text()
assert "0 */4 * * *" in recovery and "Every 4 hours" in recovery
assert "ALL of the following" in recovery
assert "No execution is queued or running" in recovery
assert "at most two automatic recovery attempts" in recovery
print(f"Template checks passed: {agent_count} agents; references, gates, recovery contracts valid.")
