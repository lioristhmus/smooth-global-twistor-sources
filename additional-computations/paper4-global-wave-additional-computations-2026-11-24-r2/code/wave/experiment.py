from pathlib import Path
import json,sys
if sys.argv[1]=='waves':
    from waves import run
elif sys.argv[1]=='local':
    from curved import run
else:
    from atlas import run
Path('results.json').write_text(json.dumps(run(),allow_nan=False,indent=2))
