"""Verify offline-signed binary inputs; contains no Stellaria application source."""
import base64,hashlib,json,pathlib,re,subprocess,tempfile
root=pathlib.Path('payload');manifest=root/'update-darwin-arm64.json';m=json.loads(manifest.read_text())
pin='J6fjqarY0xjNvpavgV9lu9hVyoiVqWjSfkiZV4yxdqA='
assert re.fullmatch(r'\d+\.\d+\.\d+',m['version'])and m['tag']=='v'+m['version']
assert m['schema']==1 and m['channel']=='beta'and m['os']=='darwin'and m['arch']=='arm64'
with tempfile.TemporaryDirectory()as d:
 key=pathlib.Path(d)/'public.der';key.write_bytes(bytes.fromhex('302a300506032b6570032100')+base64.b64decode(pin,validate=True))
 for data,sig in [(manifest,root/'update-darwin-arm64.sig'),(root/'SHA256SUMS',root/'SHA256SUMS.sig')]:
  subprocess.run(['openssl','pkeyutl','-verify','-pubin','-keyform','DER','-inkey',str(key),'-rawin','-in',str(data),'-sigfile',str(sig)],check=True)
checks={}
for line in (root/'SHA256SUMS').read_text().splitlines():
 digest,name=line.split('  ',1);assert re.fullmatch('[A-Za-z0-9_.-]+',name)and re.fullmatch('[0-9a-f]{64}',digest)
 p=root/name;assert p.is_file()and not p.is_symlink();assert hashlib.sha256(p.read_bytes()).hexdigest()==digest;checks[name]=digest
for kind in ['app','core']:
 a=m[kind];p=root/a['file'];assert checks[a['file']]==a['sha256']and p.stat().st_size==a['bytes']
assert len(checks)==5 and sum(n.endswith('.dmg')for n in checks)==1
pathlib.Path('verified-release.json').write_text(json.dumps({'tag':m['tag'],'version':m['version'],'files':list(checks)+['SHA256SUMS','SHA256SUMS.sig']}))
print('Offline release signature and every binary digest verified')
