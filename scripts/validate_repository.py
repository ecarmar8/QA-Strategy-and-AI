"""Validate local references and unique skill/client contracts using the standard library."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
skills=json.loads((ROOT/'data/skills.json').read_text())
assert len(skills)==35 and len({s['id'] for s in skills})==35
assert len({s['name'] for s in skills})==35
for skill in skills:
    assert (ROOT/skill['path']).is_file(),skill['path']
    for client in ('.claude','.gemini'):
        entry=ROOT/client/'skills'/skill['name']/'SKILL.md'
        assert entry.is_file(),entry
        assert f'name: {skill["name"]}\n' in entry.read_text(),entry
for p in ROOT.rglob('*.md'):
    if any(x in p.parts for x in ('.git','node_modules')):
        continue
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if '://' in target or target.startswith(('#','mailto:')) or '<' in target:
            continue
        filename=target.split('#')[0]
        if filename:
            assert (p.parent/filename).exists(),f'{p.relative_to(ROOT)} -> {target}'
assert len(json.loads((ROOT/'data/metric-catalog.json').read_text()))==15
assert len(json.loads((ROOT/'data/problems.json').read_text()))==8
print('PASS: 35 unique skills, two client entry-point sets, local references, 15 metric definitions and eight problem patterns.')
