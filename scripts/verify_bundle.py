from pathlib import Path
import hashlib, json, re, sys

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'skills-manifest.json').read_text(encoding='utf-8'))
errors=[]
if len(manifest['skills'])!=8: errors.append('Expected exactly eight skills')
for entry in manifest['skills']:
    folder=root/entry['directory']
    expected={f['path'] for f in entry['files']}
    actual={p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    if actual!=expected: errors.append(entry['name']+': file set mismatch')
    for file in entry['files']:
        p=folder/file['path']
        if not p.is_file(): continue
        with p.open('rb') as stream: digest=hashlib.file_digest(stream,'sha256').hexdigest()
        if digest!=file['sha256']: errors.append(str(p.relative_to(root))+': hash mismatch')
    md=(folder/'SKILL.md').read_text(encoding='utf-8-sig')
    if not re.search(r'^name:\s*'+re.escape(entry['name'])+r'\s*$',md,re.M): errors.append(entry['name']+': frontmatter name mismatch')
    if not re.search(r'^\s+version:\s*["\']?'+re.escape(entry['version'])+r'["\']?\s*$',md,re.M): errors.append(entry['name']+': version mismatch')
    for file in folder.rglob('*.md'):
        text=file.read_text(encoding='utf-8-sig')
        for line in text.splitlines():
            for target in re.findall(r'(?<![A-Za-z0-9_\-./])(?:\./)?references/([A-Za-z0-9_\-./]+?\.(?:md|txt))\b',line):
                if (folder/'references'/target).is_file(): continue
                named_owners=[other for other in manifest['skills'] if other['name'] in line and other['name']!=entry['name']]
                if any((root/other['directory']/'references'/target).is_file() for other in named_owners): continue
                errors.append(entry['name']+': missing local reference '+target)
print(json.dumps({'passed':not errors,'skills':len(manifest['skills']),'files':sum(len(e['files']) for e in manifest['skills']),'errors':errors},ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
