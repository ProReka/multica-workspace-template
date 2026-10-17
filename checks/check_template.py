"""Run with: python3 checks/check_template.py (source checks, not runtime certification)."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text()
agents = sorted((root / "agents").glob("*.md"))
skills = sorted((root / "skills").glob("*/SKILL.md"))
assert set(re.findall(r"(\d+) agents", readme)) == {str(len(agents))}, "README agent count is stale"
assert set(re.findall(r"(\d+) skills", readme)) == {str(len(skills))}, "README skill count is stale"

for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text()
    for reference in re.findall(r"`((?:workspace|agents|autopilots|squads|skills|checks)/[^`\n]+\.(?:md|py))`", text):
        assert (root / reference).is_file(), f"{path}: missing {reference}"
    for reference in re.findall(r"\]\(([^)\s]+)\)", text):
        if ":" not in reference and not reference.startswith("#"):
            target = reference.split("#", 1)[0]
            assert (path.parent / target).exists(), f"{path}: broken link {reference}"
    assert text.count("```") % 2 == 0, f"{path}: unclosed code fence"
    columns = None
    for line in text.splitlines():
        if line.startswith("|") and line.endswith("|"):
            count = len(re.split(r"(?<!\\)\|", line))
            assert columns in (None, count), f"{path}: inconsistent table columns: {line}"
            columns = count
        else:
            columns = None

skill_names = {path.parent.name for path in skills}
for path in agents:
    text = path.read_text()
    binding = re.search(r"^- \*\*Bound Skills:\*\* (.+)$", text, re.M)
    assert binding, f"{path}: missing skill binding"
    for skill in re.findall(r"`([^`]+)`", binding.group(1)):
        assert skill in skill_names, f"{path}: unknown skill {skill}"
    assert "workspace/product-delivery.md" in text, f"{path}: missing domain context"

governance = (root / "workspace/governance-rules.md").read_text()
assert all(gate in governance for gate in ("APPROVED (TL)", "READY (DevOps)"))
assert "Non-PR work is `done` only" in governance
assert "both `APPROVED (TL)` and `READY (DevOps)`" in governance
assert "Merge is not release authorization" in governance
recovery = (root / "autopilots/stuck-tasks-recovery.md").read_text()
assert "0 */4 * * *" in recovery and "Every 4 hours" in recovery
assert "ALL of the following" in recovery
assert "No execution is queued or running" in recovery
assert "at most two automatic recovery attempts" in recovery
readiness = (root / "workspace/operational-readiness.md").read_text()
benchmark_ids = re.findall(r"^\| (B\d+) \|", readiness, re.M)
assert benchmark_ids == [f"B{i:02}" for i in range(1, 18)], "Missing/duplicate benchmark scenario"
assert "Coming soon" in readme
print(f"Source checks passed: {len(agents)} agents, {len(skills)} skills, {len(benchmark_ids)} benchmark scenarios. Runtime readiness not tested.")
