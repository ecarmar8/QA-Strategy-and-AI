// Local deterministic system under test. Binds loopback only; contains no real customer data.
import http from 'node:http';
import { randomUUID } from 'node:crypto';
const port = Number(process.env.QA_CONTRACT_PORT || 4317);
const records = new Map(), keys = new Map(), throttled = new Set();
const headers = { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' };
const send = (res, status, body, extra = {}) => { res.writeHead(status, { ...headers, ...extra }); res.end(JSON.stringify(body)); };
const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>QA Contract Target</title>
<style>body{font:16px/1.6 Arial;background:#f4f4ee;color:#173e35;margin:0}main{max-width:720px;margin:40px auto;padding:28px;background:white;border-radius:12px}input,button{font:inherit;padding:10px;margin:6px 0}button{background:#173e35;color:white;border:0;border-radius:5px}label{display:block}li{margin:12px 0}#error{color:#92271d}:focus-visible{outline:3px solid #b0522c;outline-offset:3px}</style></head>
<body><main><h1>Record workspace</h1><p>Local contract verification target.</p><form id="create"><label for="name">Record name</label><input id="name" name="name" aria-describedby="help"><p id="help">Use between 1 and 80 non-whitespace characters.</p><button type="submit">Create record</button></form><p id="error" role="alert"></p><p id="notice" role="status"></p><h2>Records</h2><ul id="records"></ul></main>
<script>const workspace=new URLSearchParams(location.search).get('workspace')||'interactive';
const headers={'Content-Type':'application/json','Authorization':'Bearer qa-local-contract','x-workspace-id':workspace};
async function refresh(){const r=await fetch('/api/records',{headers});const rows=await r.json();const list=document.getElementById('records');list.replaceChildren();for(const item of rows){const li=document.createElement('li');const label=document.createElement('span');label.textContent=item.name+' — '+item.status;const b=document.createElement('button');b.textContent='Complete '+item.name;b.disabled=item.status==='completed';b.onclick=async()=>{await fetch('/api/records/'+item.id,{method:'PATCH',headers,body:JSON.stringify({status:'completed'})});await refresh()};li.append(label,' ',b);list.append(li)}}
document.getElementById('create').onsubmit=async e=>{e.preventDefault();document.getElementById('error').textContent='';const name=document.getElementById('name').value.trim();if(!name||name.length>80){document.getElementById('error').textContent='Enter a name between 1 and 80 characters.';return}const r=await fetch('/api/records',{method:'POST',headers,body:JSON.stringify({name})});if(!r.ok){document.getElementById('error').textContent='Creation failed.';return}document.getElementById('notice').textContent='Record created.';document.getElementById('name').value='';await refresh()};refresh();</script></body></html>`;
const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://127.0.0.1:${port}`);
  if (url.pathname === '/' && req.method === 'GET') { res.writeHead(200, { ...headers, 'Content-Type': 'text/html; charset=utf-8' }); res.end(html); return; }
  if (url.pathname === '/health') { send(res, 200, { status: 'ready', target: 'local-contract', version: '1.0' }); return; }
  if (!url.pathname.startsWith('/api/records')) { send(res, 404, { error: 'not_found' }); return; }
  if (req.headers.authorization !== 'Bearer qa-local-contract') { send(res, 401, { error: 'unauthorized' }); return; }
  const workspace = req.headers['x-workspace-id'];
  if (typeof workspace !== 'string' || !/^[a-z0-9-]{1,80}$/.test(workspace)) { send(res, 400, { error: 'workspace_required' }); return; }
  const rows = records.get(workspace) || new Map(); records.set(workspace, rows);
  let body = {};
  if (['POST', 'PATCH'].includes(req.method)) {
    let raw='';for await (const chunk of req) {raw+=chunk;if(raw.length>16_384){send(res,413,{error:'payload_too_large'});return}}
    try { body = JSON.parse(raw); } catch { send(res,400,{error:'invalid_json'});return; }
  }
  const id = url.pathname.split('/')[3];
  if (req.method === 'GET') { if (id) { const item=rows.get(id);send(res,item?200:404,item||{error:'not_found'}); } else send(res,200,[...rows.values()]); return; }
  if (req.method === 'POST' && !id) {
    if (typeof body.name !== 'string' || !body.name.trim() || body.name.trim().length>80) { send(res,400,{error:'name_required'});return; }
    if (req.headers['x-qa-fault'] === 'throttle-once' && !throttled.has(workspace)) { throttled.add(workspace);send(res,429,{error:'rate_limited'},{'Retry-After':'0'});return; }
    const key = req.headers['idempotency-key']; const scopeKey=workspace+':'+key;
    if(key&&keys.has(scopeKey)){const prior=keys.get(scopeKey);send(res,prior.name===body.name.trim()?200:409,prior.name===body.name.trim()?prior:{error:'idempotency_conflict'});return;}
    const item={id:randomUUID(),name:body.name.trim(),status:'open'};rows.set(item.id,item);if(key)keys.set(scopeKey,item);send(res,201,item);return;
  }
  if (!rows.has(id)) { send(res,404,{error:'not_found'});return; }
  if (req.method === 'PATCH') { if(!['open','completed'].includes(body.status)){send(res,400,{error:'invalid_status'});return}const item={...rows.get(id),status:body.status};rows.set(id,item);send(res,200,item);return; }
  if (req.method === 'DELETE') { rows.delete(id); res.writeHead(204,headers);res.end();return; }
  send(res,405,{error:'method_not_allowed'});
});
server.listen(port,'127.0.0.1',()=>console.log(`Local contract target: http://127.0.0.1:${port}`));
for(const signal of ['SIGINT','SIGTERM'])process.on(signal,()=>server.close(()=>process.exit(0)));
