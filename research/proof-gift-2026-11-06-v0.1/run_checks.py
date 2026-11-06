"""Execute the unmodified proof/application checkers in separate processes."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys

ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--out',type=Path,required=True)
    out=parser.parse_args().out.resolve()
    if out.exists(): raise SystemExit('Use a new output directory; saved evidence is never overwritten.')
    if out==ROOT or ROOT in out.parents and not out.name.startswith('fresh-'):
        raise SystemExit('Inside the package, use an output name starting with fresh-.')
    spec=importlib.util.spec_from_file_location('gift_manifest',ROOT/'verify_manifest.py')
    verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)
    count=verify.verify();out.mkdir(parents=True)
    rows=[]
    tasks=[
      ('proofs', ['proofs/checker.py','--out',str(out/'proofs')]),
      ('imaginary-gaps',['proofs/extensions/pure_gap_checks.py','--out',str(out/'pure-gaps.json')]),
      ('line-dimensions',['proofs/extensions/line_dimension_checks.py','--out',str(out/'dimensions.json')]),
      ('centered-amplitude',['proofs/extensions/centered_amplitude_checks.py','--out',str(out/'centered.json')]),
      ('independent-main',['proofs/review/initial/independent_checks.py','--study',str(ROOT/'proofs'),'--out',str(out/'independent-main.json')]),
      ('independent-supplements',['proofs/review/initial/supplement_independent_checks.py','--out',str(out/'independent-supplements.json')]),
      ('connection-holonomy',['examples/connection-holonomy/model.py','--out',str(out/'connection-holonomy')]),
      ('generated-transport',['examples/generated-transport/model.py','--out',str(out/'generated-transport')]),
      ('independent-applications',['audit/applications/independent_checks.py','--source',str(ROOT),'--out',str(out/'independent-applications.json')]),
    ]
    for name,args in tasks:
        cmd=[sys.executable,'-I','-B','-X','utf8',str(ROOT/args[0]),*args[1:]]
        result=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        (out/(name+'.stdout.txt')).write_text(result.stdout,encoding='utf-8')
        (out/(name+'.stderr.txt')).write_text(result.stderr,encoding='utf-8')
        rows.append({'task':name,'returncode':result.returncode})
        print(name+': '+('PASS' if result.returncode==0 else 'FAIL'),flush=True)
        if result.returncode: raise RuntimeError(name+' failed; inspect saved stderr')
    pairs=[('proofs/EXACT_CERTIFICATES.json','proofs/run/EXACT_CERTIFICATES.json'),
           ('pure-gaps.json','proofs/run/PURE_GAP_RESULTS.json'),
           ('dimensions.json','proofs/run/LINE_DIMENSION_RESULTS.json'),
           ('centered.json','proofs/run/CENTERED_AMPLITUDE_RESULTS.json'),
           ('connection-holonomy/EXACT_CERTIFICATE.json','examples/connection-holonomy/run/EXACT_CERTIFICATE.json'),
           ('connection-holonomy/CONNECTION.json','examples/connection-holonomy/run/CONNECTION.json'),
           ('generated-transport/EXACT_CERTIFICATE.json','examples/generated-transport/run/EXACT_CERTIFICATE.json')]
    comparisons=[]
    for current,saved in pairs:
        a=(out/current).read_bytes();b=(ROOT/saved).read_bytes()
        comparisons.append({'result':current,'saved':saved,'byte_identical':a==b,'sha256':hashlib.sha256(a).hexdigest()})
        if a!=b: raise RuntimeError('Saved certificate mismatch: '+current)
    # Compare structured results, retaining but separating environment-only fields.
    structures=[]
    for current,saved,env in [
       ('proofs/RESULTS.json','proofs/run/RESULTS.json',['runtime']),
       ('connection-holonomy/RESULTS.json','examples/connection-holonomy/run/RESULTS.json',['runtime']),
       ('generated-transport/RESULTS.json','examples/generated-transport/run/RESULTS.json',['runtime'])]:
        a=json.loads((out/current).read_text(encoding='utf-8'));b=json.loads((ROOT/saved).read_text(encoding='utf-8'))
        ea={k:a.pop(k,None) for k in env};eb={k:b.pop(k,None) for k in env}
        structures.append({'result':current,'equal_except_environment':a==b,'current_environment':ea,'saved_environment':eb})
        if a!=b: raise RuntimeError('Structured result mismatch: '+current)
    summary={'status':'PASS','manifest_files':count,'tasks':rows,'certificates':comparisons,'results':structures,
             'scope':'Finite implementation verification; quantified claims depend on written proofs and hypotheses.'}
    (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','tasks':len(rows),'certificate_matches':len(comparisons),'manifest_files':count}))

if __name__=='__main__': main()
