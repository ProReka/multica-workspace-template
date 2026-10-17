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

skill_names = {path.parent.name for path in skills}
for path in agents:
    text = path.read_text()
    binding = re.search(r"^- \*\*Bound Skills:\*\* (.+)$", text, re.M)
    assert binding, f"{path}: missing skill binding"
    for skill in re.findall(r"`([^`]+)`", binding.group(1)):
        assert skill in skill_names, f"{path}: unknown skill {skill}"
    assert "workspace/product-delivery.md" in text, f"{path}: missing domain context"

readiness = (root / "workspace/operational-readiness.md").read_text()
benchmark_ids = re.findall(r"^\| (B\d+) \|", readiness, re.M)
assert benchmark_ids and len(benchmark_ids) == len(set(benchmark_ids)), "Missing/duplicate benchmark IDs"
print(f"Source checks passed: {len(agents)} agents, {len(skills)} skills, {len(benchmark_ids)} benchmark scenarios. Runtime readiness not tested.")
