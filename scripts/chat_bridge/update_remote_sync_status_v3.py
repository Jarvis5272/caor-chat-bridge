#!/usr/bin/env python3
"""Update Bridge V3 remote status without exposing credentials."""
import argparse, datetime as dt, json
from pathlib import Path

p=argparse.ArgumentParser(); p.add_argument('--bridge',default='chat_bridge'); p.add_argument('--status',required=True); p.add_argument('--verified',choices=['true','false'],required=True); p.add_argument('--transport',default='none'); p.add_argument('--commit',default='pending'); p.add_argument('--error',default=''); a=p.parse_args()
path=Path(a.bridge)/'REMOTE_SYNC_STATUS.json'
state=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
state.update({'status':a.status,'verified':a.verified=='true','transport':a.transport,'commit':a.commit,'last_attempt':dt.datetime.now().astimezone().isoformat(timespec='seconds'),'last_error':a.error[:500]})
path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':state['status'],'verified':state['verified'],'transport':state['transport'],'commit':state['commit']},ensure_ascii=False))
