// Local pinned package, stdio preserved for the MCP client; no credentials or global install.
const {spawn}=require('node:child_process');const path=require('node:path');const fs=require('node:fs');
const root=path.resolve(__dirname,'..');const cli=path.join(root,'node_modules/@playwright/mcp/cli.js');
if(!fs.existsSync(cli)){process.stderr.write('Run npm ci in the repository before starting Playwright MCP.\n');process.exit(1)}
const args=[cli,'--isolated','--browser','chromium'];
let temporary;
if(process.env.QA_BROWSER_ARGS){const os=require('node:os');temporary=fs.mkdtempSync(path.join(os.tmpdir(),'qa-mcp-'));const config=path.join(temporary,'config.json');fs.writeFileSync(config,JSON.stringify({browser:{launchOptions:{args:JSON.parse(process.env.QA_BROWSER_ARGS)}}}));args.push('--config',config);process.on('exit',()=>fs.rmSync(temporary,{recursive:true,force:true}));}
if(process.env.QA_MCP_HEADLESS==='true')args.push('--headless');
// Both runners share the browser installed by the root locked Playwright version.
const executable=process.env.QA_BROWSER_EXECUTABLE||require('playwright').chromium.executablePath();
if(!fs.existsSync(executable)){process.stderr.write('Run npx playwright install chromium before starting MCP.\n');process.exit(1)}
args.push('--executable-path',executable);
const child=spawn(process.execPath,args,{cwd:root,stdio:'inherit',env:process.env});
child.on('error',err=>{process.stderr.write(err.message+'\n');process.exit(1)});
child.on('exit',code=>process.exit(code===null?1:code));
for(const signal of ['SIGINT','SIGTERM'])process.on(signal,()=>child.kill(signal));
