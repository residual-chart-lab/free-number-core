"""Verify package file bytes, allowing separate fresh output directories."""
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent

def verify():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
    for row in manifest['files']:
        rel=Path(row['path'])
        if rel.is_absolute() or '..' in rel.parts: raise ValueError('Unsafe manifest path')
        blob=(ROOT/rel).read_bytes()
        if len(blob)!=row['bytes'] or hashlib.sha256(blob).hexdigest()!=row['sha256']:
            raise ValueError('File differs: '+row['path'])
    return len(manifest['files'])

if __name__=='__main__':
    print(json.dumps({'status':'PASS','verified_files':verify()}))
