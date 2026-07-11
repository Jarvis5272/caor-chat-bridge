#!/usr/bin/env python3
"""Fetch and semantically verify the stable Bridge V3 raw entry points."""
from __future__ import annotations
import argparse,csv,json,time,urllib.error,urllib.request
from pathlib import Path

LABEL='FINAL_RESULT_CROSS_VALIDATION_PASS_AND_NUMBERS_LOCKED'; OUTPUT='results/final_result_cross_validation_20260711'
p=argparse.ArgumentParser();p.add_argument('--raw-base',default='https://raw.githubusercontent.com/Jarvis5272/caor-chat-bridge/main');p.add_argument('--bridge',default='chat_bridge');p.add_argument('--out',default='results/chat_bridge_v3_repair_20260711/RAW_BRIDGE_VERIFICATION.tsv');p.add_argument('--retries',type=int,default=3);p.add_argument('--retry-sleep',type=int,default=3);a=p.parse_args()
local=json.loads((Path(a.bridge)/'LATEST_RESULT.json').read_text()); marker=local['commit_marker']; timestamp=local['generated_timestamp']
urls={'latest_md':a.raw_base+'/chat_bridge/LATEST_FOR_CHATGPT.md','latest_json':a.raw_base+'/chat_bridge/LATEST_RESULT.json'}; fetched={}; errors={}
for key,url in urls.items():
 for attempt in range(1,a.retries+1):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'caor-bridge-v3-validator'}); fetched[key]=urllib.request.urlopen(req,timeout=20).read().decode();break
  except Exception as e:
   errors[key]=f'{type(e).__name__}:{e}'
   if attempt<a.retries: time.sleep(a.retry_sleep)
rows=[]
def add(item,ok,expected,observed):rows.append({'check_item':item,'status':'pass' if ok else 'fail','expected':expected,'observed':str(observed)[:500]})
add('fetch_latest_md','latest_md' in fetched,'success',errors.get('latest_md','success'));add('fetch_latest_json','latest_json' in fetched,'success',errors.get('latest_json','success'))
if 'latest_md' in fetched:
 text=fetched['latest_md']; add('md_final_label',LABEL in text,LABEL,'present' if LABEL in text else 'missing');add('md_output_dir',OUTPUT in text,OUTPUT,'present' if OUTPUT in text else 'missing');add('md_runtime',all(x in text for x in ('90.13','15.02','9.23')),'90.13/15.02/9.23','present' if all(x in text for x in ('90.13','15.02','9.23')) else 'missing');add('md_marker',marker in text,marker,'present' if marker in text else 'missing');add('md_timestamp',timestamp in text,timestamp,'present' if timestamp in text else 'missing')
if 'latest_json' in fetched:
 try:r=json.loads(fetched['latest_json'])
 except Exception as e:r={};errors['json_parse']=str(e)
 add('json_final_label',r.get('final_label')==LABEL,LABEL,r.get('final_label'));add('json_output_dir',r.get('output_dir')==OUTPUT,OUTPUT,r.get('output_dir'));add('json_marker',r.get('commit_marker')==marker,marker,r.get('commit_marker'));add('json_timestamp',r.get('generated_timestamp')==timestamp,timestamp,r.get('generated_timestamp'))
out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
with out.open('w',newline='',encoding='utf-8') as h:w=csv.DictWriter(h,delimiter='\t',fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
fails=[r for r in rows if r['status']!='pass'];print(json.dumps({'checks':len(rows),'failures':fails},ensure_ascii=False,indent=2));raise SystemExit(0 if not fails else 1)
