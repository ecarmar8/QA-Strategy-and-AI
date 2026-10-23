from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
template=(ROOT/'templates/test-case-export.html').read_text()
data=json.dumps(json.loads((ROOT/'data/test-cases.json').read_text())).replace('<','\\u003c')
(ROOT/'test-case-export.html').write_text(template.replace('__DATA__',data).replace('__ENGINE__',(ROOT/'scripts/azure-test-cases.js').read_text()))
