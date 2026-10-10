from pathlib import Path
import json,re,sys,subprocess
sys.path.insert(0,'/workspace/theme-analysis/tools')
import tinycss2
root=Path('/workspace/theme-product-restored-v9-1/theme');issues=[];schemas=[]
for p in root.rglob('*.json'):
 try:json.loads(p.read_text())
 except Exception as e:issues.append((str(p),str(e)))
for p in root.rglob('*.liquid'):
 s=p.read_text()
 for name in re.findall(r"{%[-\s]*(?:render|include)\s+['\"]([^'\"]+)['\"]",s):
  if not (root/'snippets'/f'{name}.liquid').is_file():issues.append((str(p),'Missing snippet '+name))
 for name in re.findall(r"['\"]([^'\"]+)['\"]\s*\|\s*asset_url",s):
  if not (root/'assets'/name).is_file():issues.append((str(p),'Missing asset '+name))
 for name in re.findall(r"{%[-\s]*sections?\s+['\"]([^'\"]+)['\"]",s):
  if not any((root/'sections'/f'{name}.{ext}').is_file() for ext in ['liquid','json']):issues.append((str(p),'Missing section '+name))
 m=re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}',s,re.S)
 if m:schemas.append((str(p),json.loads(m[1])))
for p in list((root/'templates').glob('*.json'))+list((root/'sections').glob('*-group.json')):
 d=json.loads(p.read_text())
 for key,sec in d.get('sections',{}).items():
  if not (root/'sections'/f"{sec['type']}.liquid").is_file():issues.append((str(p),'Missing section type '+sec['type']))
  if any(k not in sec.get('blocks',{}) for k in sec.get('block_order',[])):issues.append((str(p),'Invalid block order'))
 if any(k not in d.get('sections',{}) for k in d.get('order',[])):issues.append((str(p),'Invalid section order'))
for name,schema in schemas:
 for group in [schema]+schema.get('blocks',[]):
  fields=group.get('settings',[]);ids=[f['id'] for f in fields if 'id' in f]
  if len(ids)!=len(set(ids)):issues.append((name,'Duplicate setting IDs'))
  for f in fields:
   if f.get('type')=='range' and 'default' in f:
    value=f['default'];minimum=f['min'];maximum=f['max'];step=f.get('step',1)
    if not minimum<=value<=maximum or abs((value-minimum)/step-round((value-minimum)/step))>0.0001:issues.append((name,'Invalid range default '+f['id']))
   if f.get('type') in ['select','radio'] and 'default' in f and f['default'] not in [o['value'] for o in f['options']]:issues.append((name,'Invalid select default '+f['id']))
for p in (root/'assets').glob('*.js'):
 r=subprocess.run(['node','--check',str(p)],capture_output=True,text=True)
 if r.returncode:issues.append((str(p),r.stderr))
def css_errors(nodes,path):
 for n in nodes:
  if n.type=='error':issues.append((path,'CSS parse error: '+n.message))
  elif n.type=='at-rule' and n.content is not None and n.lower_at_keyword in ['media','supports','layer','container','keyframes','-webkit-keyframes']:
   css_errors(tinycss2.parse_rule_list(n.content,skip_whitespace=True,skip_comments=True),path)
  elif n.type=='qualified-rule':
   for declaration in tinycss2.parse_declaration_list(n.content,skip_whitespace=True,skip_comments=True):
    if declaration.type=='error':issues.append((path,'CSS declaration error: '+declaration.message))
for p in (root/'assets').glob('*.css'):css_errors(tinycss2.parse_stylesheet(p.read_text(),skip_whitespace=True,skip_comments=True),str(p))
for p in root.rglob('*.liquid'):
 for s in re.findall(r'<style>(.*?)</style>',p.read_text(),re.S):
  # Shopify font_face emits complete @font-face rules, not a scalar CSS value.
  s=re.sub(r'{{[^}]*\bfont_face\b[^}]*}}','',s,flags=re.S)
  s=re.sub(r'{{.*?}}','1',s,flags=re.S);s=re.sub(r'{%.*?%}','',s,flags=re.S)
  css_errors(tinycss2.parse_stylesheet(s,skip_whitespace=True,skip_comments=True),str(p))
print(json.dumps({'issues':issues,'section_schemas_checked':len(schemas)},indent=2));assert not issues
(root.parent/'review/static-checks.json').write_text(json.dumps({'json_valid':True,'references_valid':True,'schema_defaults_valid':True,'javascript_syntax_valid':True,'css_syntax_valid':True,'section_schemas_checked':len(schemas)},indent=2))
