#!/usr/bin/env python3
"""Build a content-addressed standalone snapshot from this source repository.

Run after committing the reviewed payload. Scientific code can be executed
from the extracted archive without this builder or a git checkout.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,zipfile

VERSION='research-2026-09-07-audit1'
RELEASE=Path(__file__).resolve().parent
DGG=RELEASE.parents[1]
REPO=DGG.parents[1]

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',required=True)
    a=ap.parse_args();out=Path(a.output_dir).resolve();out.mkdir(parents=True,exist_ok=True)
    dirty=subprocess.run(['git','status','--porcelain','--untracked-files=all','--',str(DGG)],cwd=REPO,capture_output=True,text=True,check=True).stdout
    if dirty.strip():raise SystemExit('Commit the complete DGG payload before recording its source commit.')
    root=out/('DGG-'+VERSION)
    if root.exists(): raise SystemExit('Use a new output directory; existing snapshot will not be overwritten.')
    root.mkdir()
    for folder in ('notes','certificates','synthesis'):
        for p in sorted((DGG/folder).iterdir()):
            if p.is_file() and p.suffix in ('.md','.py','.cpp','.json'):
                target=root/folder/p.name;target.parent.mkdir(exist_ok=True);shutil.copyfile(p,target)
    for p in sorted(RELEASE.iterdir()):
        if p.is_file() and (p.suffix in ('.md','.json','.cff') or p.name=='LICENSE'):
            shutil.copyfile(p,root/p.name)
    for folder,suffixes in [('manuscript',('.md','.tex','.pdf','.sh','.lua')),('verification',('.json','.log','.py'))]:
        for p in sorted((RELEASE/folder).iterdir()):
            if p.is_file() and p.suffix in suffixes:
                target=root/folder/p.name;target.parent.mkdir(exist_ok=True);shutil.copyfile(p,target)
    # LaTeX build logs/auxiliaries and compiled binaries are excluded.
    files=sorted(p for p in root.rglob('*') if p.is_file())
    source_commit=subprocess.run(['git','rev-parse','HEAD'],cwd=REPO,capture_output=True,text=True,check=True).stdout.strip()
    manifest={'series':'Depth-Generated Geometry','version':VERSION,
        'prepared_source_commit':source_commit,'suggested_local_tag':'dgg-'+VERSION,
        'mathematics_base_commit':'09b77f329d0c825c794443a0cd98cde89d8f1d73',
        'note26_commit':'881ff66','frozen_core_version':'1.0.0','frozen_core_doi':'10.5281/zenodo.21328471',
        'scope':'Finite ordered quotient atlas through n=7 and the specified n=8/222 residual comparison; not a complete three-spectator atlas.',
        'file_count_excluding_manifest_and_checksums':len(files),
        'files':[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files]}
    (root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    payload=sorted(p for p in root.rglob('*') if p.is_file())
    (root/'SHA256SUMS').write_text(''.join(digest(p)+'  '+str(p.relative_to(root))+'\n' for p in payload))
    # Verify manifest, complete checksum coverage, and the archive bytes.
    for f in manifest['files']:
        p=root/f['path'];assert p.stat().st_size==f['bytes'] and digest(p)==f['sha256']
    assert len(list((root/'notes').glob('*.md')))==27
    assert len(list((root/'certificates').glob('*.py')))==25
    result=json.loads((root/'verification/n8-222-result.json').read_text())
    assert result['quotient_dimension']==444 and result['full_suspension_obstruction_rank']==432
    for name in ('n8-222-clean-run.log','seed-tetrahedron.log','theta-operator.log'):
        assert 'ALL CHECKS PASSED' in (root/'verification'/name).read_text()
    for name in ('audit-independent-result.json','audit-guard-result.json'):
        assert json.loads((root/'verification'/name).read_text())['status']=='passed'
    audited=json.loads((root/'verification'/'verification-record.json').read_text())
    assert audited['snapshot']==VERSION
    for check in audited['checks']:
        if check.get('record') and check.get('require_pass_marker'):
            assert 'ALL CHECKS PASSED' in (root/check['record']).read_text()
    target=out/('DGG-'+VERSION+'.zip')
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if p.is_file():z.write(p,root.name+'/'+str(p.relative_to(root)))
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        for p in sorted(root.rglob('*')):
            if p.is_file():assert hashlib.sha256(z.read(root.name+'/'+str(p.relative_to(root)))).hexdigest()==digest(p)
    pdf=out/'DGG-ordered-quaternionic-response-quotients-2026-09-07-audit1.pdf'
    shutil.copyfile(root/'manuscript/ordered-quaternionic-response-quotients.pdf',pdf)
    guide=out/'DGG-research-snapshot-2026-09-07-audit1.md';shutil.copyfile(root/'README.md',guide)
    report=out/'DGG-audit-report-2026-09-07.md';shutil.copyfile(root/'AUDIT_REPORT.md',report)
    print(json.dumps({'snapshot_root':str(root),'archive':str(target),'pdf':str(pdf),'guide':str(guide),'files':len(list(p for p in root.rglob('*') if p.is_file())),'zip_bytes':target.stat().st_size,'zip_sha256':digest(target),'prepared_source_commit':source_commit},indent=2))

if __name__=='__main__':main()
