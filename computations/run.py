"""Run one recorded calculation suite. Use a fresh output filename. The lock covers all containers."""
import datetime
import json
from pathlib import Path
import subprocess
import sys
import uuid

IMAGE="sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b"
LOCK=Path.home()/".local/state/math-job.lock"
HERE=Path(__file__).resolve().parent
def docker(*args, timeout=12, payload=None):
    proc=subprocess.run(["docker",*args],text=True,input=payload,capture_output=True,timeout=timeout)
    if proc.returncode:
        raise RuntimeError(f"Docker {args[0]} failed ({proc.returncode}): {proc.stderr[-1800:]}")
    return proc.stdout.strip()

def main(path):
    if path.exists():
        raise FileExistsError(path)
    name="global-wave-"+uuid.uuid4().hex
    LOCK.parent.mkdir(parents=True,exist_ok=True)
    LOCK.mkdir()
    owner=LOCK/"owner"
    owner.write_text(json.dumps(dict(executor="global wave supplement",job_name=name,
                    started_at=datetime.datetime.now(datetime.timezone.utc).isoformat()))+"\n")
    submitted=False
    try:
        info=json.loads(docker("info","--format",'{"cpus":{{.NCPU}},"memory_bytes":{{.MemTotal}}}'))
        image=docker("image","inspect",IMAGE,"--format","{{.Id}}")
        require=image==IMAGE and info["memory_bytes"] >= 256*1024**2
        if not require:
            raise RuntimeError("VM or image preflight")
        census=docker("stats","--no-stream","--format","{{.MemUsage}} {{.CPUPerc}}")
        submitted=True
        docker("create","-i","--name",name,"--pull","never","--restart","no",
               "--network","none","--memory","128m","--memory-swap","128m","--cpus","0.5",
               "--pids-limit","32","--read-only","--cap-drop","ALL","--security-opt","no-new-privileges",
               "--ulimit","fsize=32768:32768","--log-driver","json-file","--log-opt","max-size=64k",
               "--log-opt","max-file=1","--tmpfs","/check:rw,noexec,nosuid,nodev,size=1m",
               "--env","PYTHONDONTWRITEBYTECODE=1",IMAGE,"python","-B","-c",
               "import json,sys,os,runpy; from pathlib import Path; os.chdir('/check'); "
               "d=json.load(sys.stdin); "
               "[Path(k).write_text(d[k]) for k in ('inputs.json','check.py','job.py')]; "
               "sys.path.insert(0,'/check'); runpy.run_path('/check/job.py',run_name='__main__')")
        host=json.loads(docker("inspect","--format","{{json .HostConfig}}",name))
        wanted=dict(NetworkMode="none",Memory=134217728,MemorySwap=134217728,
                    NanoCpus=500000000,PidsLimit=32,ReadonlyRootfs=True)
        if any(host[k]!=v for k,v in wanted.items()) or host["RestartPolicy"]["Name"]!="no" or host["OomKillDisable"]:
            raise RuntimeError("container limit mismatch")
        payload=json.dumps({k:(HERE/k).read_text() for k in ("inputs.json","check.py","job.py")})
        if len(payload)>32768:
            raise ValueError("input cap")
        data=json.loads(docker("start","-ai",name,timeout=60,payload=payload))
        state=json.loads(docker("inspect","--format","{{json .State}}",name))
        if state["Running"] or state["OOMKilled"] or state["ExitCode"]!=0:
            raise RuntimeError(state)
        data["environment"].update(image=image,vm=info,existing_service_usage=census.splitlines(),
                    container_config=wanted,restart="no",oom_kill_enabled=True,wall_limit_seconds=60)
        with path.open("x") as f:
            json.dump(data,f,indent=2,sort_keys=True)
            f.write("\n")
    finally:
        if submitted:
            # Match the unique name exactly. An unavailable daemon leaves the lock in place.
            matches=docker("ps","-aq","--filter","name=^/"+name+"$")
            if matches:
                if docker("inspect","--format","{{.State.Running}}",name)=="true":
                    docker("kill",name)
                if docker("inspect","--format","{{.State.Running}}",name)!="false":
                    raise RuntimeError("stop unconfirmed; lock retained")
                docker("rm",name)
        owner.unlink()
        LOCK.rmdir()

if __name__=="__main__":
    main(Path(sys.argv[1]))

