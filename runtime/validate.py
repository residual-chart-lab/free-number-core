"""Reproduce the extension without altering published evidence or TE inputs."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import re
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--time-engine',type=Path)
    parser.add_argument('--output',type=Path,default=root/'.work/demand-runtime-validation')
    args = parser.parse_args()
    output = args.output.resolve()
    evidence = (root/'research/demand-runtime-v001').resolve()
    if output == evidence or evidence in output.parents:
        raise ValueError('write fresh output outside the published evidence directory')
    output.mkdir(parents=True,exist_ok=True)
    commands = [[sys.executable,'-m','unittest','discover','-s','tests','-v'],
                [sys.executable,'examples/strengthening_study.py','--output',str(output/'study.json')]]
    if args.time_engine:
        commands.append([sys.executable,'examples/time_engine_bridge.py','--time-engine',str(args.time_engine.resolve()),
                         '--output',str(output/'te-bridge.json')])
    logs, runs = [],[]
    for command in commands:
        result = subprocess.run(command,cwd=root,text=True,encoding='utf-8',capture_output=True)
        logs.append(result.stdout+result.stderr)
        runs.append(dict(command=command[1:],returncode=result.returncode))
        if result.returncode:
            (output/'validation.log').write_bytes('\n'.join(logs).encode('utf-8'))
            print(logs[-1])
            raise SystemExit(result.returncode)
    count = int(re.search(r'Ran (\d+) tests',logs[0]).group(1))
    source_paths = sorted(path for folder in ('runtime','tests','examples') for path in (root/folder).rglob('*.py'))
    source_paths.append(root/'pyproject.toml')
    sources = {path.relative_to(root).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in source_paths}
    study = json.loads((output/'study.json').read_bytes())
    te = json.loads((output/'te-bridge.json').read_bytes()) if args.time_engine else None
    files = ('study.json','te-bridge.json') if te else ('study.json',)
    report = dict(schema='free-numbers-demand-runtime-validation-v1',passed=True,tests=count,
                  study_groups=study['groups'],TE_bridge_groups=te['groups'] if te else None,
                  python=sys.version,platform=platform.platform(),commands=runs,source_sha256=sources,
                  result_sha256={name:hashlib.sha256((output/name).read_bytes()).hexdigest() for name in files})
    (output/'validation.log').write_bytes('\n'.join(logs).encode('utf-8'))
    (output/'validation.json').write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps(dict(passed=True,tests=count,study_groups=study['groups'],TE_bridge_groups=report['TE_bridge_groups'])))


if __name__ == '__main__':
    main()
