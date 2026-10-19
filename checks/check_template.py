"""Run with: python3 checks/check_template.py (source checks, not runtime certification)."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
agents = sorted((root / "agents").glob("*.md"))
skills = sorted((root / "skills").glob("*/SKILL.md"))

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

for path in agents:
    text = path.read_text()
    assert text.startswith("You are "), f"{path}: role prompt must be directly pasteable"
    assert len(re.findall(r"^## ", text, re.M)) >= 3, f"{path}: missing role structure"
    assert "workspace/" not in text and "## Instructions" not in text, f"{path}: embedded reference/metadata"
    assert "mention://" not in text, f"{path}: platform routing belongs to runtime"

shared = (root / "workspace/shared-context.md").read_text()
for section in ("Identity & Product Boundaries", "Authority & Ownership", "Living Workspace Data", "Delivery & Review", "Evidence & Closed-Loop Follow-Through", "Safety & Escalation"):
    assert section in shared, f"Shared context missing {section}"
assert "mention://" not in shared, "Shared context must not duplicate platform mention syntax"
assert not re.search(r"\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b", shared, re.I), "Shared context must not embed directory IDs"

readiness = (root / "workspace/operational-readiness.md").read_text()
benchmark_ids = re.findall(r"^\| (B\d+) \|", readiness, re.M)
assert benchmark_ids and len(benchmark_ids) == len(set(benchmark_ids)), "Missing/duplicate benchmark IDs"
print(f"Source checks passed: {len(agents)} agents, {len(skills)} skills, {len(benchmark_ids)} benchmark scenarios. Runtime readiness not tested.")
