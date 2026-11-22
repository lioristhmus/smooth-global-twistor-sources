"""Entry point inside the constrained container. stdout is the sole result channel."""
import json
import platform
import resource
import time
from pathlib import Path
from check import carriers, frame, require, torus

cfg=json.loads((Path(__file__).parent/"inputs.json").read_text())
cg=Path("/sys/fs/cgroup")
limits={f:(cg/f).read_text().strip() for f in ("memory.max","memory.swap.max","cpu.max","pids.max")}
require(limits == {"memory.max":"134217728","memory.swap.max":"0","cpu.max":"50000 100000","pids.max":"32"},
        "unexpected live cgroup v2 limits")
start=time.monotonic()
small=dict(cfg["torus"],cutoffs=[1])
pilot=torus(small)
pilot_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
require(pilot_rss < 65536 and time.monotonic()-start < 5, "pilot exceeds budget")
report=dict(environment=dict(python=platform.python_version(),arch=platform.machine(),cgroup=limits),
            pilot=dict(cutoff=1,rss_kib=pilot_rss),
            results=dict(torus=pilot+torus(dict(cfg["torus"],cutoffs=cfg["torus"]["cutoffs"][1:])),
                         carriers=carriers(cfg["carriers"]),frame=frame(cfg["frame"])),
            run=dict(elapsed_seconds=round(time.monotonic()-start,6),
                     peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
data=json.dumps(report,default=str,sort_keys=True,indent=2)
require(len(data)<32768, "output cap")
print(data)

